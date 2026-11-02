---
name: local-ai-agents
license: MIT
---
# Criar Agentes IA Locais com Foundry Local e Qwen

> Competência acompanhante para [Lição 17 – Criar Agentes IA Locais](../../../17-creating-local-ai-agents/README.md).
> Use-a para ajudar um aluno a construir um agente que raciocine, utilize ferramentas e pesquise
> documentação inteiramente na sua própria máquina — sem inferência na nuvem. Baseie toda
> recomendação no conteúdo da lição e no caderno executável.

## Desencadeadores

Ative esta competência quando um aluno quiser:
- Executar um agente **totalmente no dispositivo** por razões de privacidade, custo ou offline.
- Servir um modelo localmente com **Foundry Local** e conectar via o endpoint compatível com OpenAI.
- Usar um modelo **Qwen de chamada de funções** para conduzir chamadas confiáveis a ferramentas locais.
- Adicionar **RAG local** (Chroma) ou um **servidor MCP local**.
- Projetar uma estratégia de encaminhamento **híbrida** local/nuvem.

## Modelo mental central

Um SLM troca amplitude por privacidade, custo e operação offline. A estratégia vencedora:
**deixar o SLM orquestrar e deixar as ferramentas fazerem o trabalho pesado.** O
modelo não precisa *conhecer* a base de código — precisa saber quando chamar
`read_file` e `search_docs`. Isso joga a favor da força de um SLM (decisões limitadas
como a seleção de ferramentas) e evita sua fraqueza (conhecimento amplo, raciocínio
multi-salto extenso).

## Por que estas peças específicas

- **Foundry Local** expõe um **endpoint HTTP compatível com OpenAI**, então o código do agente em nuvem transfere-se alterando apenas o `base_url` (e usando uma chave API local fictícia). Também seleciona automaticamente a melhor versão (CPU/GPU/NPU) para a máquina.
- Os modelos **Qwen** são treinados para chamadas de função e emitem chamadas de ferramentas bem formadas consistentemente — é isso que transforma um modelo *chat* local num *agente* local.
- **Chroma** executa em processo e armazena vetores no disco, então todo o pipeline RAG (embed → armazenar → recuperar → raciocinar) permanece local.
- **MCP** é um transporte, não um serviço em nuvem: um servidor MCP pode executar localmente sobre `stdio`.

## Elementos essenciais para configuração

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # marcador de posição local
```

~8 GB de RAM é um mínimo realista; uma GPU/NPU ajuda mas não é obrigatória.

## Padrões principais para reproduzir

Indique ao aluno o caderno
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Ferramentas isoladas**: cada ferramenta de ficheiros resolve caminhos e rejeita qualquer coisa fora da raiz única do projeto — mesmo localmente, uma ferramenta executa com as permissões do usuário.
- **Ciclo de chamada de ferramenta**: registar ferramentas com o esquema de ferramentas OpenAI, executar ferramentas solicitadas localmente, alimentar resultados, repetir até resposta final.
- **RAG Local**: inserir documentos numa coleção Chroma; `search_docs` retorna trechos top-k.
- **MCP Local**: conectar a um servidor local via `stdio`; delimitar ao diretório do projeto e validar as suas saídas.

## Encaminhamento híbrido (local como um dos modelos)

| Situação | Onde executa |
|-----------|---------------|
| Dados sensíveis / offline | SLM Local |
| Tarefa simples e limitada | SLM Local (barato, rápido) |
| Raciocínio multi-salto complexo em dados não sensíveis | Modelo na nuvem |
| Queda da nuvem | SLM Local (degradação gradual) |

Isto espelha a ideia de roteamento de modelos da Lição 16, com a estação de trabalho como uma das rotas. Prefira designs que regressam ao local para que o agente degrade em
qualidade em vez de falhar completamente.


## Guardrails para o assistente

- Mantenha todas as operações de ficheiros/ferramentas limitadas a um diretório de projeto isolado.
- Não envie código ou dados para a nuvem quando o objetivo declarado do aluno for privacidade/offline — mantenha toda a pipeline local.
- Estabeleça expectativas realistas para a qualidade do SLM; apoie-se em ferramentas e RAG em vez do conhecimento memorizado do modelo.
- Note que a Lição 17 não tem **endpoint de Respostas Foundry**, logo a ação de teste de fumos na nuvem não se aplica — valide executando o caderno localmente.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->