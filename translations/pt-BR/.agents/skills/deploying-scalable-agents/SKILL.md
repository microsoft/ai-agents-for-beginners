---
name: deploying-scalable-agents
description: Take a working agent prototype to a scalable, observable production deployment on Microsoft Foundry. Covers deployment patterns, the agent lifecycle, model routing, response caching, evaluation gates, human approval, OpenTelemetry observability, cost optimisation, and smoke-testing deployed agents.
license: MIT
---
# Implantando Agentes Escaláveis com Microsoft Foundry

> Habilidade complementar para [Lição 16 – Implantando Agentes Escaláveis](../../../16-deploying-scalable-agents/README.md).
> Use-a para ajudar um aprendiz a mover um agente do protótipo para uma implantação
> de produção escalável e observável. Baseie toda recomendação no conteúdo da lição e
> no notebook executável; não invente APIs do Foundry.

## Gatilhos

Ative esta habilidade quando um aprendiz quiser:
- Implantar um agente no Microsoft Foundry como um **agente hospedado** e torná-lo versionado/observável.
- Escolher entre os padrões de implantação **cliente-hospedado, agente-hospedado e fluxo de trabalho de agente**.
- Adicionar **roteamento de modelo**, **cache de resposta** ou **concorrência limitada** para controlar latência e custo.
- Adicionar um **portal de avaliação** para que uma versão ruim do agente não seja entregue.
- Adicionar uma etapa de **aprovação humana no loop** para ações de alto risco.
- Instrumentar um agente com rastreamento **OpenTelemetry** para observabilidade em produção.
- Fazer um **teste rápido** de um agente implantado como um filtro rápido pós-implantação.

## Modelo mental central

Um agente de produção é principalmente o esqueleto operacional *em torno* do modelo (~80%),
não o modelo em si. Mapeie cada recomendação para uma dessas preocupações:

| Preocupação | Protótipo → Produção |
|------------|------------------------|
| Hospedagem | notebook → serviço hospedado versionado |
| Identidade | seu `az login` → identidade gerenciada + RBAC com escopo |
| Estado | em memória → armazenamento externo de thread/memória |
| Falha | rastreamento → tentativas, alternativas, alertas |
| Custo | "alguns centavos" → monitorado, roteado, cacheado, orçado |
| Qualidade | avaliação visual → portal de avaliação automatizado |
| Confiança | você aprova → política + aprovação humana no loop |

## Padrões de implantação (escolha um ou combine)

1. **Cliente-hospedado** — o loop de raciocínio roda no seu processo. Controle máximo; você gerencia a escalabilidade/estado.
2. **Agente hospedado (Foundry Agent Service)** — o Foundry hospeda o loop, armazena threads, aplica RBAC/segurança de conteúdo, mostra o agente no portal. Menos controle, muito menos superfície operacional.
3. **Fluxo de trabalho de agente** — múltiplos agentes/ferramentas compostos em um grafo com ramificações, nós de aprovação e checkpoints duráveis.

## Ciclo de vida (o loop que entrega um agente)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Avaliação offline é um portal, não um detalhe** — uma versão não é entregue
a menos que ultrapasse o limite. Observabilidade online alimenta falhas reais
de volta ao conjunto de testes offline.

## Alavancas para escalabilidade e custo (em ordem de prioridade)

1. **Dimensionar corretamente o modelo** — use o menor modelo que passe no portal de avaliação.
2. **Roteamento por complexidade** — modelo pequeno/rápido para solicitações simples, modelo grande para raciocínio real (classificador DIY ou Foundry Model Router).
3. **Cache** — atenda requisições quase duplicadas sem chamar o modelo.
4. **Design sem estado + concorrência limitada** — externalize estado; retente com backoff.

## Padrões chave para reproduzir

Aponte o aprendiz para estes no notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Manipulador de requisições**: cache → roteamento por complexidade → rastreamento span → executar → cache.
- **Portal de avaliação**: pontue um conjunto de testes offline; retorne `pass_rate >= threshold` e só implante se verdadeiro.
- **Aprovação humana**: `@tool(approval_mode="always_require")` para ações como grandes reembolsos.
- **Rastreamento**: envolva cada requisição em `tracer.start_as_current_span(...)` e defina atributos como `routed.model`, `customer.id`.

## Teste rápido de um agente implantado

Após a implantação, verifique se o endpoint realmente responde (uma implantação verde pode ainda estar
silenciosa). Use o [Teste Rápido de IA](https://github.com/marketplace/actions/ai-smoke-test)
via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
com o catálogo em [`tests/`](../../../tests/README.md). O runner POSTa cada
prompt para `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
e verifica o texto da resposta. A identidade precisa da função **Usuário Azure AI** no
escopo do projeto Foundry; a audiência do token deve ser `https://ai.azure.com/`.

Sobreponha os portais: **teste rápido** (alcançável/respondendo, toda implantação) → **avaliação offline** (bom o suficiente para entregar, antes da promoção) → **avaliação online** (como está na prática, contínua).



## Controles empresariais

- **RBAC**: dê a cada agente hospedado uma identidade gerenciada com privilégios mínimos.
- **MCP em produção**: trate todo servidor MCP como um limite não confiável — fixe a versão, delimite sua identidade, valide saídas, limite taxa, nunca exponha segredos.

## Barreiras de segurança para o assistente

- Prefira o padrão canônico `FoundryChatClient(...)` + `provider.as_agent(...)` usado em todo o curso.
- Não prometa resultados Azure ao vivo que você não tenha verificado; recomende o fluxo de trabalho de teste rápido para confirmar uma implantação.
- Mantenha as recomendações de avaliação e custo interligadas: a avaliação define o nível mínimo de qualidade, o roteamento/cache mantém o custo próximo a esse nível.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->