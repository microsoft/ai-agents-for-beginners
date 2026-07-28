---
name: local-ai-agents
license: MIT
---
# Criando Agentes de IA Locais com Foundry Local e Qwen

> Habilidade acompanhante para [Lição 17 – Criando Agentes de IA Locais](../../../17-creating-local-ai-agents/README.md).
> Use-a para ajudar um aprendiz a construir um agente que raciocina, chama ferramentas e busca
> documentação inteiramente na sua própria máquina — sem inferência na nuvem. Baseie toda
> recomendação no conteúdo da lição e no notebook executável.

## Gatihos

Ative essa habilidade quando um aprendiz quiser:
- Rodar um agente **totalmente no dispositivo** por motivos de privacidade, custo ou offline.
- Servir um modelo localmente com **Foundry Local** e conectar via endpoint compatível com OpenAI.
- Usar um modelo de **chamada de função Qwen** para conduzir chamadas confiáveis a ferramentas locais.
- Adicionar **RAG local** (Chroma) ou um **servidor MCP local**.
- Projetar uma estratégia de roteamento **híbrida** local/nuvem.

## Modelo mental principal

Um SLM troca amplitude por privacidade, custo e operação offline. A estratégia vencedora:
**deixe o SLM orquestrar e deixe as ferramentas fazerem o trabalho pesado.** O
modelo não precisa *conhecer* a base de código — precisa saber quando chamar
`read_file` e `search_docs`. Isso joga em favor da força do SLM (decisões delimitadas
como seleção de ferramenta) e contra sua fraqueza (conhecimento amplo, raciocínio
de múltiplos saltos longo).

## Por que essas peças específicas

- **Foundry Local** expõe um **endpoint HTTP compatível com OpenAI**, portanto o código do agente na nuvem transfere apenas alterando `base_url` (e usando uma chave API local fictícia). Ele também seleciona automaticamente a melhor compilação (CPU/GPU/NPU) para a máquina.
- Modelos **Qwen** são treinados para chamada de função e geram chamadas de ferramenta bem formadas de forma consistente — isso transforma um modelo *chat* local em um *agente* local.
- **Chroma** roda no processo e armazena vetores no disco, então todo o pipeline RAG (incorporar → armazenar → recuperar → raciocinar) permanece local.
- **MCP** é um transporte, não um serviço na nuvem: um servidor MCP pode rodar localmente por `stdio`.

## Essenciais para configuração

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # espaço reservado local
```

~8 GB de RAM é um mínimo realista; GPU/NPU ajuda mas não é obrigatório.

## Padrões-chave para reproduzir

Indique ao aprendiz o notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Ferramentas isoladas**: toda ferramenta de arquivo resolve caminhos e rejeita qualquer coisa fora da raiz do projeto — mesmo localmente, uma ferramenta roda com as permissões do usuário.
- **Loop de chamada de ferramenta**: registre ferramentas no esquema de ferramentas OpenAI, execute ferramentas solicitadas localmente, alimente os resultados de volta, repita até uma resposta final.
- **RAG local**: atualize documentos numa coleção Chroma; `search_docs` retorna os top-k chunks.
- **MCP local**: conecte a um servidor local via `stdio`; limite ao diretório do projeto e valide as saídas.

## Roteamento híbrido (local como um dos modelos)

| Situação | Onde roda |
|-----------|---------------|
| Dados sensíveis / offline | SLM local |
| Tarefa simples, delimitada | SLM local (barato, rápido) |
| Raciocínio complexo de múltiplos saltos em dados não sensíveis | Modelo na nuvem |
| Queda na nuvem | SLM local (degradação graciosa) |

Isso espelha a ideia do roteamento de modelos da Lição 16, com a estação de trabalho como uma
das rotas. Prefira designs que adotem fallback local para que o agente degrade em
qualidade ao invés de falhar totalmente.

## Guardrails para o assistente

- Mantenha toda operação de arquivo/ferramenta limitada a um diretório de projeto isolado.
- Não envie código ou dados para a nuvem quando o objetivo declarado do aprendiz for privacidade/offline — mantenha todo o pipeline local.
- Defina expectativas realistas para a qualidade do SLM; apoie-se em ferramentas e RAG ao invés do conhecimento memorizado do modelo.
- Note que a Lição 17 não tem endpoint Foundry Responses, então a ação de smoke-test na nuvem não se aplica — valide executando o notebook localmente.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->