# Testes de Fumo do Agente

Esta pasta contém **catálogos de testes de fumo** para os agentes que constrói durante o curso.
Um teste de fumo é uma verificação barata e rápida para confirmar que um **agente alojado Microsoft Foundry
em produção** está acessível, responde e cumpre as suas expectativas mais básicas da prompt.
É o primeiro filtro — não uma substituição para o pipeline completo de avaliação
que aprende em [Lição 10](../10-ai-agents-production/README.md) e
[Lição 16](../16-deploying-scalable-agents/README.md).

Os catálogos são utilizados pela [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action através do fluxo de trabalho [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Como executar

1. **Desdobre o agente da lição** para a Microsoft Foundry como um agente alojado (consulte
   a Lição 16 para o fluxo de trabalho de implantação). Tome nota do **nome do agente** e do seu
   **endpoint do projeto Foundry**.
2. Adicione estes segredos do repositório (Definições → Segredos e variáveis → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. A identidade federada
   precisa da função **Azure AI User** ao nível do **âmbito do projeto Foundry**.
3. No separador **Actions**, execute **Smoke-test hosted agents** e escolha o
   `tests_file` da lição, depois forneça o `agent_name` e o `project_endpoint` correspondentes.


## Catálogo → lição → nome do agente

| Catálogo | Lição | Implantar agente como |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Introdução a Agentes de IA](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Utilização de Ferramentas](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – RAG Agente](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Implantação de Agentes Escaláveis](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Que lições têm testes de fumo?

Os testes de fumo aplicam-se a lições onde **implantam um agente** cujas respostas de texto podem
ser validadas contra conteúdos conhecidos. Lições que são conceptuais, executam-se apenas localmente,
ou produzem saída criativa não determinística são intencionalmente excluídas:

- **Lição 17 (Criar Agentes IA Locais)** corre inteiramente no seu posto de trabalho com
  Foundry Local e **não** expõe um endpoint de Respostas Foundry, pelo que esta
  ação não se aplica. Valide-a executando o notebook localmente.
- Lições de padrões de design e teoria (02, 03, 06, 07, 09, 12) não contêm um agente
  implantável para testar com testes de fumo.

## Esquema do catálogo (referência rápida)

Cada catálogo é um documento JSON com um array `tests` no topo. Cada entrada submete via POST
um prompt e valida a resposta:

| Campo | Significado |
|-------|------------|
| `id` | Identificador único do passo impresso no registo. |
| `description` | Propósito legível por humanos. |
| `prompt` | A mensagem enviada ao agente. |
| `assertions.status` | Estado HTTP esperado (padrão 200). |
| `assertions.contains_any` | Sucesso se a resposta contiver qualquer uma destas subcadeias. |
| `assertions.contains_all` | Sucesso se a resposta contiver todas as subcadeias. |
| `assertions.contains_none` | Sucesso se a resposta não contiver nenhuma destas subcadeias. |
| `save_response_id_as` | Guarda o id da resposta para um passo multinível posterior. |
| `use_previous_response_id` | Envia esta interação encadeada a um id de resposta guardado. |

As afirmações são verificações de subcadeias ignorando caixa. Consulte a
[documentação da ação](https://github.com/marketplace/actions/ai-smoke-test) para
o esquema completo, incluindo recursos de conversação geridos pelo Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->