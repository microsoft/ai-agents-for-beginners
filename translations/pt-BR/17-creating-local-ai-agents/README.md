# Criando Agentes de IA Locais Usando Microsoft Foundry Local e Qwen

![Criando Agentes de IA Locais](../../../translated_images/pt-BR/lesson-17-thumbnail.f86434c595a408fc.webp)

A lição anterior escalou agentes *para cima* na nuvem. Esta os traz *para baixo* para uma única máquina. Ao final, você terá um assistente de engenharia funcional que raciocina, chama ferramentas, lê seus arquivos e busca em sua documentação — **sem uma única chamada de inferência na nuvem.**

Por que você gostaria disso? Três razões que surgem constantemente no trabalho real de engenharia:

- **Privacidade.** O código e os documentos nunca deixam a máquina. Nenhum prompt, trecho de código ou dado do cliente atravessa a rede.
- **Custo.** A inferência local não tem custo por token. Você pode iterar o dia todo pelo preço da eletricidade.
- **Offline.** Em um avião, em uma instalação segura ou durante uma queda, o agente ainda funciona.

A questão é que você está trocando um modelo de ponta da nuvem por um **Modelo de Linguagem Pequeno (SLM)** rodando em seu CPU, GPU ou NPU. Esta lição é sobre construir agentes que sejam *bons* dentro dessa restrição em vez de fingir que ela não existe.

## Introdução

Esta lição vai abordar:

- **Modelos de Linguagem Pequenos (SLMs)** — o que são, onde se destacam e onde não.
- **Microsoft Foundry Local** — um runtime que baixa e serve modelos no dispositivo através de uma **API compatível com OpenAI**.
- **Modelos Qwen de chamada de função** — SLMs que produzem chamadas de ferramenta confiáveis, o que torna agentes locais (não apenas chat local) possíveis.
- **Ferramentas locais, RAG local e MCP local** — dando capacidade ao agente sem a nuvem.
- **Padrões híbridos** — quando manter algo local e quando recorrer à nuvem.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Explicar as trocas dos SLMs e escolher casos de uso apropriados para agentes locais.
- Servir um modelo Qwen localmente com Foundry Local e conectar-se por meio do endpoint compatível com OpenAI.
- Construir um agente que chama ferramentas e roda inteiramente em sua estação de trabalho.
- Adicionar RAG local sobre seus próprios documentos usando um banco de vetores local (Chroma).
- Conectar o agente a um servidor MCP local e raciocinar sobre designs híbridos local/nuvem.

## Pré-requisitos

Esta lição pressupõe que você tenha completado as lições anteriores e esteja confortável com:

- [Uso de Ferramentas](../04-tool-use/README.md) (Lição 4) e [Agentic RAG](../05-agentic-rag/README.md) (Lição 5).
- [Protocolos Agentes / MCP](../11-agentic-protocols/README.md) (Lição 11).
- O [Microsoft Agent Framework](../14-microsoft-agent-framework/README.md) (Lição 14).

Você também precisará de:

- Uma estação de trabalho de desenvolvedor. **8 GB de RAM é um mínimo realista**; 16 GB+ é confortável. Uma GPU ou NPU ajuda, mas não é obrigatório.
- **Microsoft Foundry Local** instalado (veja a seção de configuração abaixo).
- Python 3.12+ e os pacotes no repositório [`requirements.txt`](../../../requirements.txt), além de `foundry-local-sdk`, `openai` e `chromadb` para esta lição.

## Modelos de Linguagem Pequenos: A Ferramenta Certa para Trabalho Local

Um modelo de ponta na nuvem tem centenas de bilhões de parâmetros e um data center por trás. Um SLM tem alguns bilhões de parâmetros e precisa caber na RAM do seu laptop. Essa diferença estabelece expectativas claras.

**SLMs são bons em:**

- Tarefas estruturadas e delimitadas — classificação, extração, sumarização de um documento conhecido.
- **Chamada de ferramentas** — decidir qual função chamar e com quais argumentos.
- Iteração rápida, barata e privada em seus próprios dados.

**SLMs são menos eficientes em:**

- Raciocínio aberto, multi-hop, em grande contexto.
- Conhecimento amplo do mundo (eles viram menos e esquecem mais).

A estratégia vencedora para agentes locais é, portanto: **deixe o SLM orquestrar e deixe as ferramentas fazerem o trabalho pesado.** O modelo não precisa *conhecer* sua base de código — precisa saber quando chamar `read_file` e `search_docs`. Isso joga diretamente nas forças de um SLM.

```mermaid
flowchart LR
    U[Desenvolvedor] --> A[Agente SLM Local]
    A -->|decide qual ferramenta| T1[ler_arquivo]
    A -->|decide qual ferramenta| T2[busca_docs RAG]
    A -->|decide qual ferramenta| T3[analisar_código]
    T1 --> A
    T2 --> A
    T3 --> A
    A --> R[Resposta, totalmente no dispositivo]
```

## Microsoft Foundry Local

**Microsoft Foundry Local** é um runtime leve que baixa, gerencia e serve modelos inteiramente na sua máquina. Sua característica mais importante para nós é que ele expõe um **endpoint HTTP compatível com OpenAI** — o que significa que o SDK OpenAI e o cliente OpenAI do Microsoft Agent Framework funcionam contra ele com apenas uma mudança de `base_url`. Tudo que você aprendeu sobre construir agentes se transfere diretamente; só o endpoint sai da nuvem para o `localhost`.

Foundry Local também seleciona automaticamente a melhor build do modelo para seu hardware — uma build para CPU, para CUDA/GPU ou para NPU — então você não precisa otimizar manualmente para cada máquina.

### Configuração

Instale o Foundry Local (veja a [documentação](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) para seu SO), depois confirme que está funcionando:

```bash
# Instale (exemplo; siga a documentação para sua plataforma)
winget install Microsoft.FoundryLocal      # Windows
# brew install microsoft/foundrylocal/foundrylocal   # macOS

# Baixe e execute um modelo Qwen, depois inicie o serviço local
foundry model run qwen2.5-7b-instruct
foundry service status
```

Uma vez que o serviço esteja rodando, você tem um endpoint local compatível com OpenAI (tipicamente `http://localhost:PORT/v1`). O notebook usa o `foundry-local-sdk` para descobrir o endpoint automaticamente, então você não precisa codificar a porta fixamente.

## Chamada de Função Qwen: Por que É Importante

Um agente é realmente um agente se ele pode chamar ferramentas. Muitos SLMs podem conversar, mas produzem chamadas de ferramenta pouco confiáveis e malformadas. Os modelos **Qwen** são treinados para chamada de função e emitem estruturas de chamada de ferramenta bem-formadas de forma consistente — que é exatamente o que transforma um modelo de chat local em um *agente* local.

O fluxo é o loop padrão de chamadas de ferramenta que você já conhece, só que rodando no dispositivo:

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Agente Qwen (local)
    participant T as Ferramenta Local
    U->>A: "O que o auth.py faz?"
    A->>A: Decidir: chamar read_file
    A->>T: read_file("auth.py")
    T-->>A: conteúdo do arquivo
    A->>A: Raciocinar sobre o conteúdo
    A-->>U: Explicação
```

## RAG Local

A busca na documentação é onde agentes locais realmente valem a pena. Em vez de esperar que o SLM memorize a documentação do seu framework, você incorpora esses documentos em um **banco de dados vetorial local** e deixa o agente recuperar os trechos relevantes sob demanda.

Usamos o **Chroma**, um armazenamento vetorial embarcado que roda no processo, sem servidor para gerenciar. O pipeline é inteiramente local: modelo de embedding local → vetores locais → recuperação local → SLM local.

```mermaid
flowchart TB
    D[Seus docs / código] --> E[Modelo de incorporação local]
    E --> V[(Banco de vetores Chroma - em disco)]
    Q[Consulta do agente] --> QE[Incorpore a consulta localmente]
    QE --> V
    V -->|principais pedaços k| A[Agente Qwen]
    A --> Ans[Resposta fundamentada]
```

Este é o mesmo padrão Agentic RAG da Lição 5 — a única mudança é que todos os componentes rodam na sua máquina.

## Servidores MCP Locais

[MCP](../11-agentic-protocols/README.md) é um transporte, não um serviço na nuvem. Um servidor MCP pode rodar como um processo local no `stdio`, expondo ferramentas para seu agente via protocolo padrão. Isso permite reutilizar o ecossistema crescente de servidores MCP — acesso ao sistema de arquivos, operações git, consultas a bancos de dados — inteiramente offline.

A postura de segurança é diferente da nuvem, mas não ausente: um servidor MCP local ainda roda com as permissões do seu usuário, então limite o que ele pode acessar (um diretório de projeto, não sua pasta pessoal inteira) e trate suas saídas como entradas para validar.

## Padrões Híbridos Nuvem-e-Local

Local-primeiro não significa apenas local. Sistemas maduros roteiam por sensibilidade e dificuldade:

| Situação | Onde roda |
| --- | --- |
| Código / dados sensíveis, ou offline | **SLM Local** |
| Tarefa simples e delimitada | **SLM Local** (barato, rápido) |
| Raciocínio multi-hop difícil em dados não sensíveis | **Modelo na Nuvem** |
| Tudo, durante uma queda | **SLM Local** (degradação graciosa) |

Isso espelha a ideia de **roteamento de modelo** da Lição 16 — exceto que um dos "modelos" agora é sua própria máquina. Um design robusto recua para o local quando a nuvem está indisponível, para que o agente degrade em qualidade e não falhe completamente.

```mermaid
flowchart LR
    Q[Solicitação] --> S{Sensível ou offline?}
    S -->|sim| L[SLM Local]
    S -->|não| C{Precisa de raciocínio profundo?}
    C -->|não| L
    C -->|sim| Cloud[Modelo em nuvem]
    L --> Out[Resposta]
    Cloud --> Out
```

## Exercício Prático: Um Assistente de Engenharia Local

Abra [`code_samples/17-local-agent-foundry-local.ipynb`](./code_samples/17-local-agent-foundry-local.ipynb) e siga-o. Você construirá um **assistente de engenharia local** que roda inteiramente na sua estação de trabalho e pode:

1. **Chamar ferramentas** — via chamada de função Qwen por meio do Foundry Local.
2. **Executar operações de arquivo locais** — listar e ler arquivos em um diretório de projeto.
3. **Analisar código** — relatar métricas básicas de um arquivo fonte.
4. **Buscar na documentação** — RAG local em uma pasta de docs com Chroma.
5. **Usar MCP** — conectar a um servidor MCP local (pulando suavemente se nenhum estiver configurado).

Nenhuma inferência na nuvem é usada em nenhum momento.

### Passo a passo

O assistente conecta ao Foundry Local por meio do endpoint compatível com OpenAI, então o código do agente fica quase idêntico ao das lições na nuvem — só muda o cliente:

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

Note a verificação de sandbox — mesmo localmente, uma ferramenta que lê caminhos arbitrários é um risco. O notebook mantém cada ferramenta limitada a uma raiz de projeto única.

## Verificação de Conhecimento

Teste seu entendimento antes de seguir para a tarefa.

**1. Dê duas razões concretas para rodar um agente localmente em vez de na nuvem.**

<details>
<summary>Resposta</summary>

Quaisquer duas de: **privacidade** (código e dados nunca deixam a máquina), **custo** (sem cobrança por token de inferência) e **capacidade offline** (funciona sem rede — em avião, instalação segura ou durante queda). Restrições regulatórias/compliance que proíbem enviar dados fora do dispositivo são um motivo comum da questão da privacidade.
</details>

**2. Qual é a divisão de trabalho recomendada entre um SLM e suas ferramentas em um agente local, e por quê?**

<details>
<summary>Resposta</summary>

Deixe o SLM **orquestrar** (decidir qual ferramenta chamar e com quais argumentos) e deixe as **ferramentas fazerem o trabalho pesado** (ler arquivos, recuperar docs, calcular resultados). SLMs são fortes em decisões delimitadas como seleção de ferramenta, mas mais fracos em conhecimento amplo e raciocínio multi-hop longo, então apoiar-se nas ferramentas joga a favor deles.
</details>

**3. O que torna possível reutilizar o código do agente na nuvem com Foundry Local?**

<details>
<summary>Resposta</summary>

Foundry Local expõe um **endpoint HTTP compatível com OpenAI**. O SDK OpenAI e o cliente OpenAI do Agent Framework funcionam contra ele mudando apenas o `base_url` (e usando uma chave API local fictícia). Todo o restante no código do agente fica igual.
</details>

**4. Por que usamos especificamente um modelo Qwen de chamada de função em vez de qualquer SLM?**

<details>
<summary>Resposta</summary>

Porque um agente deve produzir chamadas de ferramenta confiáveis e bem-formadas. Muitos SLMs podem conversar, mas emitem estruturas de chamada de ferramenta mal formadas ou inconsistentes. Modelos Qwen são treinados para chamada de função e produzem chamadas consistentes de ferramentas, o que transforma um modelo de chat local em um agente local funcional.
</details>

**5. No pipeline RAG local, quais componentes rodam na máquina?**

<details>
<summary>Resposta</summary>

Todos: o modelo de embedding, o banco vetorial (Chroma, em disco), a etapa de recuperação e o SLM. Os documentos são incorporados localmente, armazenados localmente, recuperados localmente e analisados por um modelo local — nenhum componente toca a nuvem.
</details>

**6. Um servidor MCP local roda na sua máquina. Isso o torna automaticamente seguro? Que precaução você ainda deve tomar?**

<details>
<summary>Resposta</summary>

Não. Um servidor MCP local roda com as permissões do seu usuário, então ele pode acessar tudo o que você pode. Limite-o ao que ele precisa (por exemplo, um único diretório de projeto em vez da sua pasta pessoal inteira) e trate suas saídas como entradas para validar antes de agir.
</details>

**7. Descreva uma regra sensata de roteamento híbrido que inclua um modelo local.**

<details>
<summary>Resposta</summary>

Roteie solicitações sensíveis ou offline para o SLM local; roteie tarefas simples e delimitadas para o SLM local para agilidade e custo; roteie raciocínio multi-hop difícil em dados não sensíveis para um modelo na nuvem; e recorra ao SLM local se a nuvem estiver indisponível para que o agente degrade graciosamente em vez de falhar. Isso é roteamento de modelo (Lição 16) com a máquina local como um dos modelos.
</details>

**8. Qual é um valor realista mínimo de RAM para rodar o agente local nesta lição e o que mais RAM permite?**

<details>
<summary>Resposta</summary>

Cerca de **8 GB** é um mínimo realista; 16 GB+ é confortável. Mais RAM permite rodar modelos maiores e mais capazes e manter mais contexto em memória. Uma GPU ou NPU acelera a inferência, mas não é necessária — Foundry Local seleciona uma build para CPU quando não há acelerador disponível.
</details>

## Tarefa

Estenda o assistente de engenharia local para um **revisor de documentação local** para um pequeno projeto de sua escolha (use uma das pastas de lições deste repositório se quiser).

Seu envio deve:

1. **Indexar uma pasta real de docs/código** no Chroma (pelo menos cinco arquivos).
2. **Adicionar uma ferramenta `find_todos`** que escaneie o projeto atrás de comentários `TODO`/`FIXME` e os retorne com arquivo e número da linha — mantendo a mesma verificação de sandbox que o `read_file`.

3. **Faça ao agente três perguntas** que forcem a combinação de ferramentas: uma pergunta pura de RAG, uma que exija ler um arquivo específico e uma que exija encontrar TODOs.
4. **Meça**: cronometre cada uma das três respostas e anote-as em uma célula markdown. Comente se a latência é aceitável para seu fluxo de trabalho pretendido.

Depois escreva um parágrafo curto sobre **o que você moveria para a nuvem e o que manteria localmente** para este revisor, e por quê. Você será avaliado sobre se os componentes locais estão conectados corretamente e se seu raciocínio híbrido é sólido — não sobre a qualidade do modelo.

## Resumo

Nesta lição você construiu um agente que roda inteiramente em sua própria máquina:

- **SLMs** trocam abrangência por privacidade, custo e operação offline — e brilham quando **orquestram ferramentas** ao invés de carregar todo o conhecimento por conta própria.
- **Foundry Local** serve modelos no dispositivo atrás de um **endpoint compatível com OpenAI**, para que seu código de agente na nuvem seja transferido com uma alteração de linha.
- **Modelos Qwen com chamadas de função** tornam possível chamadas confiáveis para ferramentas locais — e portanto *agentes* locais.
- **RAG local** (Chroma) e **MCP local** dão ao agente capacidades sem sair da máquina.
- **Padrões híbridos** permitem rotear por sensibilidade e dificuldade, com local como fallback elegante.

Isso completa o arco de implantação: a Lição 16 escalou agentes para o Microsoft Foundry, e esta lição os escalou para uma única estação de trabalho. A próxima lição aborda como manter agentes implantados seguros.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-foundry/foundry-local/" target="_blank">Documentação Microsoft Foundry Local</a>
- <a href="https://learn.microsoft.com/azure/ai-foundry/what-is-azure-ai-foundry" target="_blank">Documentação Microsoft Foundry</a>
- <a href="https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python" target="_blank">Microsoft Agent Framework</a>
- <a href="https://qwen.readthedocs.io/en/latest/framework/function_call.html" target="_blank">Documentação de chamadas de função do Qwen</a>
- <a href="https://modelcontextprotocol.io/" target="_blank">Protocolo Model Context (MCP)</a>
- <a href="https://docs.trychroma.com/" target="_blank">Banco de dados vetorial Chroma</a>

## Lição Anterior

[Implantando Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

## Próxima Lição

[Segurança para Agentes de IA](../18-securing-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->