# Testes de Fumaça de Agente

Esta pasta contém **catálogos de teste de fumaça** para os agentes que você constrói no curso.
Um teste de fumaça é uma verificação barata e rápida para garantir que um **agente hospedado Microsoft Foundry
implantado** esteja acessível, respondendo e seguindo suas expectativas básicas de prompt.
É um primeiro filtro — não um substituto para o pipeline completo de avaliação
que você aprende na [Lição 10](../10-ai-agents-production/README.md) e
[Lição 16](../16-deploying-scalable-agents/README.md).

Os catálogos são consumidos pela [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via o fluxo de trabalho [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Como executar

1. **Implante o agente da lição** no Microsoft Foundry como um agente hospedado (veja
   a Lição 16 para o fluxo de implantação). Anote o **nome do agente** e seu
   **endpoint do projeto Foundry**.
2. Adicione os segredos do repositório (Configurações → Segredos e variáveis → Ações):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. A identidade federada
   precisa da função **Usuário Azure AI** no **escopo do projeto Foundry**.
3. Na aba **Ações**, execute **Smoke-test hosted agents** e escolha o
   `tests_file` para a lição, depois forneça o `agent_name` e
   `project_endpoint` correspondentes.

## Catálogo → lição → nome do agente

| Catálogo | Lição | Implantar agente como |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Introdução a Agentes de IA](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Uso de Ferramentas](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – RAG Agentic](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Implantando Agentes Escaláveis](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Quais lições possuem testes de fumaça?

Testes de fumaça se aplicam a lições onde você **implanta um agente** cujas respostas de texto podem
ser verificadas contra conteúdo conhecido. Lições que são conceituais, executam apenas localmente,
ou produzem saída criativa não determinística são intencionalmente excluídas:

- **Lição 17 (Criando Agentes de IA Locais)** roda inteiramente na sua estação de trabalho com
  Foundry Local e **não** expõe um endpoint de Respostas do Foundry, então esta
  ação não se aplica. Valide rodando o notebook localmente.
- Lições de padrões de design e teoria (02, 03, 06, 07, 09, 12) não entregam qualquer
  agente implantável para teste de fumaça.

## Esquema do catálogo (referência rápida)

Cada catálogo é um documento JSON com um array de `tests` no nível superior. Cada entrada faz um POST
com um prompt e verifica a resposta:

| Campo | Significado |
|-------|------------|
| `id` | Identificador único do passo impresso no log. |
| `description` | Propósito legível por humanos. |
| `prompt` | Mensagem enviada ao agente. |
| `assertions.status` | Status HTTP esperado (padrão 200). |
| `assertions.contains_any` | Passa se a resposta contém alguma dessas substrings. |
| `assertions.contains_all` | Passa se a resposta contém todas as substrings. |
| `assertions.contains_none` | Passa se a resposta não contém nenhuma dessas substrings. |
| `save_response_id_as` | Armazena o id da resposta para um passo posterior multi-turno. |
| `use_previous_response_id` | Envia esta interação encadeada a um id de resposta salvo. |

Asserções são verificações de substring que ignoram maiúsculas/minúsculas. Veja a
[documentação da ação](https://github.com/marketplace/actions/ai-smoke-test) para
o esquema completo, incluindo recursos de conversa gerenciados pelo Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->