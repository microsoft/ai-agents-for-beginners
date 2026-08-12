# Criando Agentes de IA Locais Usando Microsoft Foundry Local e Qwen

![Criando Agentes de IA Locais](../../../translated_images/pt-BR/lesson-17-thumbnail.f86434c595a408fc.webp)

A lição anterior escalou agentes *para cima* na nuvem. Esta traz eles *para baixo* em uma única máquina. Ao final, você terá um assistente de engenharia funcional que raciocina, chama ferramentas, lê seus arquivos e busca na sua documentação — **sem nenhuma chamada de inferência na nuvem.**

Por que você gostaria disso? Três motivos que surgem constantemente em trabalho real de engenharia:

- **Privacidade.** O código e documentos nunca saem da máquina. Nenhum prompt, snippet ou dado do cliente cruza o limite da rede.
- **Custo.** A inferência local não tem cobrança por token. Você pode iterar o dia todo pelo preço da eletricidade.
- **Offline.** No avião, em uma instalação segura ou durante uma queda, o agente ainda funciona.

O problema é que você está trocando um modelo de ponta na nuvem por um **Small Language Model (SLM)** rodando no seu CPU, GPU ou NPU. Esta lição trata de construir agentes que sejam *bons* dentro dessa limitação, e não fingir que a limitação não existe.

## Introdução

Esta lição abordará:

- **Small Language Models (SLMs)** — o que são, onde brilham e onde não.
- **Microsoft Foundry Local** — um runtime que baixa e serve modelos localmente através de uma **API compatível com OpenAI**.
- **Modelos Qwen de chamada de função** — SLMs que produzem chamadas de ferramenta confiáveis, permitindo agentes *locais* (não só chat local).
- **Ferramentas locais, RAG local e MCP local** — dando capacidade ao agente sem a nuvem.
- **Padrões híbridos** — quando manter local e quando usar a nuvem.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Explicar as concessões dos SLMs e escolher casos de uso adequados para agentes locais.
- Servir um modelo Qwen localmente com Foundry Local e conectar-se via endpoint compatível com OpenAI.
- Construir um agente que chama ferramentas e roda inteiramente na sua estação de trabalho.
- Adicionar RAG local sobre seus próprios documentos usando um banco vetorial local (Chroma).
- Conectar o agente a um servidor MCP local e raciocinar sobre designs híbridos local/nuvem.

## Pré-requisitos

Esta lição pressupõe que você completou as lições anteriores e está confortável com:

- [Uso de Ferramentas](../04-tool-use/README.md) (Lição 4) e [Agentic RAG](../05-agentic-rag/README.md) (Lição 5).
- [Protocolos Agentic / MCP](../11-agentic-protocols/README.md) (Lição 11).
- O [Microsoft Agent Framework](../14-microsoft-agent-framework/README.md) (Lição 14).

Você também precisará de:

- Uma estação de trabalho para desenvolvedor. **8 GB de RAM é o mínimo realista**; 16 GB+ é confortável. Um GPU ou NPU ajuda, mas não é obrigatório.
- **Microsoft Foundry Local** instalado (veja a seção de configuração abaixo).
- Python 3.12+ e os pacotes no repositório [`requirements.txt`](../../../requirements.txt), além de `foundry-local-sdk`, `openai` e `chromadb` para esta lição.

## Small Language Models: A Ferramenta Certa para Trabalho Local

Um modelo de ponta na nuvem tem centenas de bilhões de parâmetros e um datacenter atrás. Um SLM tem alguns bilhões de parâmetros e deve caber na RAM do seu laptop. Essa diferença define expectativas claras.

**SLMs são bons em:**

- Tarefas estruturadas e delimitadas — classificação, extração, resumo de um documento conhecido.
- **Chamada de ferramenta** — decidir qual função chamar e com quais argumentos.
- Iteração rápida, barata e privada nos seus próprios dados.

**SLMs são mais fracos em:**

- Raciocínio aberto e de múltiplos passos em contexto grande.
- Conhecimento amplo do mundo (viram menos dados e esquecem mais).

A estratégia vencedora para agentes locais é: **deixe o SLM orquestrar e deixe as ferramentas fazerem o trabalho pesado.** O modelo não precisa *conhecer* sua base de código — precisa saber quando chamar `read_file` e `search_docs`. Isso joga diretamente com as forças do SLM.

```mermaid
flowchart LR
    U[Desenvolvedor] --> A[Agente Local SLM]
    A -->|decide qual ferramenta| T1[ler_arquivo]
    A -->|decide qual ferramenta| T2[busca_docs RAG]
    A -->|decide qual ferramenta| T3[analisar_código]
    T1 --> A
    T2 --> A
    T3 --> A
    A --> R[Responder, totalmente no dispositivo]
```

## Microsoft Foundry Local

**Microsoft Foundry Local** é um runtime leve que baixa, gerencia e serve modelos inteiramente na sua máquina. A característica mais importante para nós é que ele expõe um **endpoint HTTP compatível com OpenAI** — o que significa que o SDK OpenAI e o cliente OpenAI do Microsoft Agent Framework funcionam contra ele apenas alterando `base_url`. Tudo que você aprendeu sobre construir agentes se transfere diretamente; só o endpoint muda da nuvem para `localhost`.

O Foundry Local também escolhe automaticamente a melhor versão do modelo para seu hardware — uma build para CPU, CUDA/GPU ou NPU — para que você não tenha que otimizar manualmente por máquina.

### Configuração

Instale o Foundry Local (veja a [documentação](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) para seu SO) e confirme que funciona:

```bash
# Instale (exemplo; siga a documentação para sua plataforma)
winget install Microsoft.FoundryLocal      # Windows
# brew install microsoft/foundrylocal/foundrylocal   # macOS

# Baixe e execute um modelo Qwen, depois inicie o serviço local
foundry model run qwen2.5-7b-instruct
foundry service status
```

Uma vez que o serviço esteja rodando você tem um endpoint local compatível com OpenAI (tipicamente `http://localhost:PORT/v1`). O notebook usa o `foundry-local-sdk` para descobrir o endpoint automaticamente, então você não precisa fixar a porta no código.

## Chamada de Função Qwen: Por Que Isso Importa

Um agente é realmente um agente se pode chamar ferramentas. Muitos SLMs conseguem conversar, mas produzem chamadas a ferramentas não confiáveis e mal formadas. Modelos **Qwen** são treinados para chamada de função e emitem estruturas bem formadas de chamadas de ferramenta consistentemente — o que transforma um modelo de chat local em um *agente* local.

O fluxo é o loop padrão de chamada de ferramenta que você já conhece, só que rodando localmente:

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agente Qwen (local)
    participant T as Ferramenta Local
    U->>A: "O que auth.py faz?"
    A->>A: Decidir: chamar read_file
    A->>T: read_file("auth.py")
    T-->>A: conteúdo do arquivo
    A->>A: Raciocinar sobre o conteúdo
    A-->>U: Explicação
```

## RAG Local

A busca em documentação é onde agentes locais se destacam. Ao invés de esperar que o SLM tenha decorado a documentação do seu framework, você incorpora esses documentos em um **banco vetorial local** e deixa o agente recuperar os trechos relevantes sob demanda.

Usamos o **Chroma**, um repositório vetorial embutido que roda no processo sem servidor. O pipeline é totalmente local: modelo de embedding local → vetores locais → recuperação local → SLM local.

```mermaid
flowchart TB
    D[Seus documentos / código] --> E[Modelo de incorporação local]
    E --> V[(Banco de dados vetorial Chroma - no disco)]
    Q[Consulta do agente] --> QE[Incorporar consulta localmente]
    QE --> V
    V -->|pedaços top-k| A[Agente Qwen]
    A --> Ans[Resposta fundamentada]
```

Este é o mesmo padrão Agentic RAG da Lição 5 — a única mudança é que todo componente roda na sua máquina.

## Servidores MCP Locais

[MCP](../11-agentic-protocols/README.md) é um transporte, não um serviço na nuvem. Um servidor MCP pode rodar como processo local em `stdio`, expondo ferramentas ao seu agente pelo protocolo padrão. Isso permite reutilizar o ecossistema crescente de servidores MCP — acesso ao sistema de arquivos, operações git, consultas a banco de dados — totalmente offline.

A postura de segurança é diferente da nuvem, mas não ausente: um servidor MCP local ainda roda com as permissões do seu usuário, então limite o que ele pode acessar (um diretório de projeto, não sua pasta home inteira) e trate suas saídas como entradas para validar.

## Padrões Híbridos de Nuvem e Local

Local-first não significa local-apenas. Sistemas maduros roteiam por sensibilidade e dificuldade:

| Situação | Onde roda |
| --- | --- |
| Código/dados sensíveis, ou offline | **SLM Local** |
| Tarefa simples e delimitada | **SLM Local** (barato, rápido) |
| Raciocínio multi-hop difícil em dados não sensíveis | **Modelo na Nuvem** |
| Tudo, durante queda | **SLM Local** (degradação graciosa) |

Isso reflete a ideia de **model routing** da Lição 16 — exceto que um dos "modelos" agora é sua própria máquina. Um design robusto recorre ao local quando a nuvem está indisponível, então o agente degrada em qualidade ao invés de falhar completamente.

```mermaid
flowchart LR
    Q[Solicitação] --> S{Sensível ou offline?}
    S -->|sim| L[SLM Local]
    S -->|não| C{Precisa de raciocínio profundo?}
    C -->|não| L
    C -->|sim| Cloud[Modelo na nuvem]
    L --> Out[Resposta]
    Cloud --> Out
```

## Laboratório Prático: Um Assistente de Engenharia Local

Abra [`code_samples/17-local-agent-foundry-local.ipynb`](./code_samples/17-local-agent-foundry-local.ipynb) e faça o passo a passo. Você construirá um **assistente de engenharia local** que roda inteiramente na sua estação de trabalho e pode:

1. **Chamar ferramentas** — via chamada de função Qwen através do Foundry Local.
2. **Executar operações locais em arquivos** — listar e ler arquivos em um diretório de projeto.
3. **Analisar código** — reportar métricas básicas sobre um arquivo fonte.
4. **Buscar documentação** — RAG local sobre um diretório de docs usando Chroma.
5. **Usar MCP** — conectar a um servidor MCP local (pulando graciosamente caso não esteja configurado).

Nenhuma inferência na nuvem é usada em nenhum momento.

### Passo a Passo

O assistente se conecta ao Foundry Local pelo endpoint compatível com OpenAI, então o código do agente parece quase idêntico às lições na nuvem — só muda o cliente:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Foundry Local descobre/baixa o modelo e nos fornece um endpoint local.
manager = FoundryLocalManager(\"qwen2.5-7b-instruct\")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # api_key é um espaço reservado local
```

As ferramentas são funções Python comuns limitadas a um diretório de projeto:

```python
def read_file(path: str) -> str:
    \"\"\"Read a file, but only inside the sandboxed project directory.\"\"\"
    full = (PROJECT_ROOT / path).resolve()
    if PROJECT_ROOT not in full.parents and full != PROJECT_ROOT:
        return \"Access denied: path is outside the project directory.\"
    return full.read_text(encoding=\"utf-8\")
```

Note a verificação do sandbox — mesmo localmente, uma ferramenta que lê caminhos arbitrários é uma vulnerabilidade. O notebook mantém cada ferramenta limitada a uma raiz de projeto única.

## Verificação de Conhecimento

Teste seu entendimento antes de avançar para a tarefa.

**1. Dê duas razões concretas para rodar um agente localmente em vez de na nuvem.**

<details>
<summary>Resposta</summary>

Qualquer duas das seguintes: **privacidade** (código e dados nunca saem da máquina), **custo** (sem cobrança por token na inferência) e **capacidade offline** (funciona sem rede — em um avião, em uma instalação segura ou durante uma queda). Restrições regulatórias/compliance que proíbem enviar dados para fora do dispositivo são um motivo comum para a questão da privacidade.
</details>

**2. Qual é a divisão recomendada de trabalho entre um SLM e suas ferramentas em um agente local, e por quê?**

<details>
<summary>Resposta</summary>

Deixe o SLM **orquestrar** (decidir qual ferramenta chamar e com quais argumentos) e deixe as **ferramentas fazerem o trabalho pesado** (ler arquivos, recuperar docs, calcular resultados). SLMs são fortes em decisões delimitadas como seleção de ferramentas, mas mais fracos em conhecimento amplo e raciocínio longo multi-hop; apoiar-se nas ferramentas dá uso às suas forças.
</details>

**3. O que torna possível reutilizar código de agentes da nuvem com Foundry Local?**

<details>
<summary>Resposta</summary>

O Foundry Local expõe um **endpoint HTTP compatível com OpenAI**. O SDK OpenAI e o cliente OpenAI do Agent Framework funcionam contra ele apenas alterando o `base_url` (e usar uma chave API local simulada). Todo o resto do código do agente permanece igual.
</details>

**4. Por que usamos especificamente um modelo Qwen de chamada de função, e não qualquer SLM?**

<details>
<summary>Resposta</summary>

Porque um agente deve produzir chamadas de ferramenta confiáveis e bem formadas. Muitos SLMs podem conversar mas emitem estruturas de chamada de ferramenta mal formadas ou inconsistentes. Modelos Qwen são treinados para chamada de função e geram chamadas consistentes, o que transforma um modelo de chat local em um agente local funcional.
</details>

**5. No pipeline RAG local, quais componentes rodam na máquina?**

<details>
<summary>Resposta</summary>

Todos eles: o modelo de embedding, o banco vetorial (Chroma, no disco), a etapa de recuperação e o SLM. Documentos são incorporados localmente, armazenados localmente, recuperados localmente e raciocinados por um modelo local — nenhum componente acessa a nuvem.
</details>

**6. Um servidor MCP local roda na sua máquina. Isso o torna automaticamente seguro? Que precauções você ainda deve tomar?**

<details>
<summary>Resposta</summary>

Não. Um servidor MCP local roda com as permissões do seu usuário, então pode acessar tudo o que você pode. Limite-o ao necessário (por exemplo, um único diretório de projeto em vez da sua pasta home inteira) e trate suas saídas como entradas para validar antes de agir sobre elas.
</details>

**7. Descreva uma regra de roteamento híbrido sensata que inclua um modelo local.**

<details>
<summary>Resposta</summary>

Roteie requisições sensíveis ou offline para o SLM local; roteie tarefas simples e delimitadas para o SLM local por velocidade e custo; roteie raciocínio multi-hop difícil em dados não sensíveis para um modelo na nuvem; e recorra ao SLM local se a nuvem estiver indisponível para que o agente degrade com elegância em vez de falhar. Isso é model routing (Lição 16) com a máquina local como um dos modelos.
</details>

**8. Qual é uma cifra realista mínima de RAM para rodar o agente local nesta lição, e o que mais RAM compra para você?**

<details>
<summary>Resposta</summary>

Cerca de **8 GB** é o mínimo realista; 16 GB+ é confortável. Mais RAM permite rodar modelos maiores e mais capazes e manter mais contexto em memória. GPU ou NPU aceleram a inferência mas não são necessários — Foundry Local seleciona uma build para CPU quando nenhum acelerador está disponível.
</details>

## Tarefa

Estenda o assistente de engenharia local para um **revisor local de documentação** para um pequeno projeto de sua escolha (use uma das pastas de lições deste repositório se quiser).

Sua submissão deve:

1. **Indexar uma pasta real de docs/código** no Chroma (pelo menos cinco arquivos).
2. **Adicionar uma ferramenta `find_todos`** que escaneie o projeto em busca de comentários `TODO`/`FIXME` e os retorne com arquivo e número da linha — mantendo a mesma verificação sandbox do `read_file`.

3. **Faça ao agente três perguntas** que o obriguem a combinar ferramentas: uma pergunta pura de RAG, uma que exija ler um arquivo específico e uma que exija encontrar TODOs.
4. **Meça-o**: cronometre cada uma das três respostas e anote-as em uma célula markdown. Comente se a latência é aceitável para o seu fluxo de trabalho pretendido.

Em seguida, escreva um parágrafo curto sobre **o que você moveria para a nuvem e o que manteria localmente** para este revisor, e por quê. Você será avaliado se os componentes locais estão conectados corretamente e se seu raciocínio híbrido é sólido — não na qualidade do modelo.

## Resumo

Nesta lição você construiu um agente que roda inteiramente na sua própria máquina:

- **SLMs** trocam abrangência por privacidade, custo e operação offline — e brilham quando eles **orquestram ferramentas** ao invés de carregar todo o conhecimento sozinhos.
- **Foundry Local** serve modelos no dispositivo por trás de um **endpoint compatível com OpenAI**, assim o código do agente na nuvem é transferido com uma alteração de uma linha.
- **Modelos Qwen com chamadas de função** tornam chamada confiável de ferramentas locais — e, portanto, *agentes* locais — possível.
- **RAG local** (Chroma) e **MCP local** dão ao agente capacidade sem sair da máquina.
- **Padrões híbridos** permitem roteamento por sensibilidade e dificuldade, com o local como um fallback elegante.

Isto completa o arco de implantação: A Lição 16 escalou agentes para o Microsoft Foundry, e esta lição os escalou para baixo numa única estação de trabalho. A próxima lição aborda como manter agentes implantados seguros.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-foundry/foundry-local/" target="_blank">Documentação do Microsoft Foundry Local</a>
- <a href="https://learn.microsoft.com/azure/ai-foundry/what-is-azure-ai-foundry" target="_blank">Documentação do Microsoft Foundry</a>
- <a href="https://aka.ms/ai-agents-beginners/agent-framework" target="_blank">Microsoft Agent Framework</a>
- <a href="https://qwen.readthedocs.io/en/latest/framework/function_call.html" target="_blank">Documentação do Qwen para chamadas de função</a>
- <a href="https://modelcontextprotocol.io/" target="_blank">Protocolo de Contexto de Modelo (MCP)</a>
- <a href="https://docs.trychroma.com/" target="_blank">Banco de dados vetorial Chroma</a>

## Lição Anterior

[Implantando Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

## Próxima Lição

[Protegendo Agentes de IA](../18-securing-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->