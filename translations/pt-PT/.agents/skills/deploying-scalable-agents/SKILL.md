---
name: deploying-scalable-agents
description: Take a working agent prototype to a scalable, observable production deployment on Microsoft Foundry. Covers deployment patterns, the agent lifecycle, model routing, response caching, evaluation gates, human approval, OpenTelemetry observability, cost optimisation, and smoke-testing deployed agents.
license: MIT
---
# Desdobramento de Agentes Escaláveis com Microsoft Foundry

> Competência complementar para [Lição 16 – Desdobramento de Agentes Escaláveis](../../../16-deploying-scalable-agents/README.md).
> Utilize-a para ajudar um aprendiz a mover um agente de protótipo para um desdobramento
> de produção escalável e observável. Baseie todas as recomendações no conteúdo da lição e
> no bloco de notas executável; não invente APIs do Foundry.

## Gatilhos

Ative esta competência quando um aprendiz quiser:
- Desdobrar um agente no Microsoft Foundry como um **agente alojado** e torná-lo versionado/observável.
- Escolher entre os padrões de desdobramento **cliente-alojado, agente alojado e fluxo de trabalho do agente**.
- Adicionar **encaminhamento de modelo**, **cache de resposta** ou **concorrência limitada** para controlar latência e custo.
- Adicionar uma **porta de avaliação** para impedir que uma versão ruim do agente seja lançada.
- Adicionar uma etapa de **aprovação humana no processo** para ações de alto risco.
- Instrumentar um agente com rastreio **OpenTelemetry** para observabilidade em produção.
- Realizar um **teste rápido** a um agente desdobrado como uma porta rápida pós-desdobramento.

## Modelo mental central

Um agente de produção é principalmente o esqueleto operacional *à volta* do modelo (~80%),
não o modelo em si. Mapeie cada recomendação para uma destas preocupações:

| Preocupação | Protótipo → Produção |
|---------|------------------------|
| Alojamento | bloco de notas → serviço alojado versionado |
| Identidade | seu `az login` → identidade gerida + RBAC com escopo |
| Estado | na memória → armazenamento de threads/memória externalizado |
| Falha | rastreio → tentativas, alternativas, alertas |
| Custo | "uns cêntimos" → rastreado, encaminhado, cacheado, orçamentado |
| Qualidade | ver a olho → porta de avaliação automatizada |
| Confiança | você aprova → políticas + humano no processo |

## Padrões de desdobramento (escolha um, ou combine)

1. **Cliente-alojado** — o ciclo de raciocínio é executado no seu processo. Máximo controlo; você gere a escalabilidade/estado.
2. **Agente alojado (Foundry Agent Service)** — o Foundry aloja o ciclo, armazena threads, aplica RBAC/segurança de conteúdo, mostra o agente no portal. Menos controlo, superfície operacional muito menor.
3. **Fluxo de trabalho do agente** — múltiplos agentes/ferramentas compostos num grafo com ramificações, nós de aprovação e pontos de verificação duradouros.

## Ciclo de vida (o ciclo que lança um agente)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**A avaliação offline é uma porta, não um pensamento posterior** — uma versão não é lançada
a menos que ultrapasse o limiar. A observabilidade online retroalimenta falhas reais
para o conjunto de testes offline.

## Alavancas de escalabilidade e custo (por ordem de prioridade)

1. **Dimensionar corretamente o modelo** — use o menor modelo que passe a porta de avaliação.
2. **Encaminhar por complexidade** — modelo pequeno/rápido para pedidos simples, modelo grande para raciocínio real (classificador DIY ou Foundry Model Router).
3. **Cache** — sirva pedidos quase idênticos sem chamar o modelo.
4. **Design sem estado + concorrência limitada** — externalize o estado; reintente com recuo progressivo.

## Padrões chave a reproduzir

Direcione o aprendiz para estes no bloco de notas
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Manipulador de pedidos**: cache → encaminhar por complexidade → span de rastreio → executar → cache.
- **Porta de avaliação**: classifique um conjunto de testes offline; retorne `pass_rate >= threshold` e só faça o desdobramento se verdadeiro.
- **Aprovação humana**: `@tool(approval_mode="always_require")` para ações como grandes reembolsos.
- **Rastreio**: envolva cada pedido em `tracer.start_as_current_span(...)` e defina atributos como `routed.model`, `customer.id`.

## Teste rápido a um agente desdobrado

Após o desdobramento, verifique se o endpoint realmente responde (um desdobramento verde pode ainda ser
silencioso). Utilize a ação [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
através de [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
com o catálogo em [`tests/`](../../../tests/README.md). O executor envia por POST cada
prompt para `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
e verifica a resposta do texto. A identidade necessita da função **Azure AI User** no
âmbito do projeto Foundry; o público do token deve ser `https://ai.azure.com/`.

Sobreponha as portas: **teste rápido** (acessível/respondendo, em cada desdobramento) → **avaliação offline** (bom o suficiente para lançar, antes da promoção) → **avaliação online** (como está a funcionar no terreno, contínuo).



## Controlos empresariais

- **RBAC**: atribua a cada agente alojado uma identidade gerida com privilégios mínimos.
- **MCP em produção**: trate cada servidor MCP como fronteira não confiável — fixe a versão, delimite a sua identidade, valide saídas, limite taxas, nunca exponha segredos.

## Guardrails para o assistente

- Prefira o padrão canónico `FoundryChatClient(...)` + `provider.as_agent(...)` utilizado em todo o curso.
- Não prometa resultados Azure ao vivo que não tenha verificado; recomende o fluxo de trabalho de teste rápido para confirmar um desdobramento.
- Mantenha a avaliação e o aconselhamento de custos relacionados: a avaliação define o limite de qualidade, o encaminhamento/cache mantém o custo próximo desse limite.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->