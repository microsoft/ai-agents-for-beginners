# Agentes de IA em Produção: Observabilidade e Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-BR/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, a capacidade de entender seu comportamento, monitorar seu desempenho e avaliar sistematicamente suas saídas se torna importante.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá/entenderá:
- Conceitos centrais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, os custos e a eficácia dos agentes
- O que e como avaliar seus agentes de IA de forma sistemática
- Como controlar os custos ao implantar agentes de IA em produção
- Como instrumentar agentes construídos com o Microsoft Agent Framework

O objetivo é equipar você com o conhecimento para transformar seus agentes "caixa-preta" em sistemas transparentes, gerenciáveis e confiáveis.

_**Nota:** É importante implantar Agentes de IA que sejam seguros e confiáveis. Confira também a lição [Construindo Agentes de IA Confiáveis](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como traces e spans.

- **Trace** representa uma tarefa completa do agente do início ao fim (como o tratamento de uma consulta de usuário).
- **Spans** são etapas individuais dentro do trace (como chamar um modelo de linguagem ou recuperar dados).

![Árvore de traces no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa-preta" — seu estado interno e raciocínio são opacos, tornando difícil diagnosticar problemas ou otimizar o desempenho. Com observabilidade, os agentes se tornam "caixas de vidro", oferecendo transparência que é vital para construir confiança e garantir que operem conforme o esperado.

## Por que a Observabilidade Importa em Ambientes de Produção

Levar agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. Observabilidade deixa de ser um "desejável" e passa a ser uma capacidade crítica:

*   **Depuração e Análise da Causa Raiz**: Quando um agente falha ou produz uma saída inesperada, as ferramentas de observabilidade fornecem os traces necessários para identificar a origem do erro. Isso é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLMs, interações com ferramentas e lógica condicional.
*   **Gerenciamento de Latência e Custos**: Agentes de IA frequentemente dependem de LLMs e outras APIs externas cobradas por token ou por chamada. A observabilidade permite rastrear essas chamadas com precisão, ajudando a identificar operações excessivamente lentas ou caras. Isso permite que equipes otimizem prompts, escolham modelos mais eficientes ou redesenhem fluxos de trabalho para gerenciar custos operacionais e garantir uma boa experiência do usuário.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportem de forma segura e ética. A observabilidade fornece um rastro de auditoria das ações e decisões do agente. Isso pode ser usado para detectar e mitigar problemas como injeção de prompt, geração de conteúdo prejudicial ou mau tratamento de informações pessoalmente identificáveis (PII). Por exemplo, você pode revisar traces para entender por que um agente forneceu certa resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Dados de observabilidade são a base de um processo iterativo de desenvolvimento. Ao monitorar como os agentes se comportam no mundo real, as equipes podem identificar áreas para melhoria, coletar dados para ajuste fino de modelos e validar o impacto de mudanças. Isso cria um ciclo de feedback onde insights de produção da avaliação online informam experimentos e refinamentos offline, levando a um desempenho progressivamente melhor do agente.

## Principais Métricas para Acompanhar

Para monitorar e entender o comportamento do agente, uma série de métricas e sinais deve ser acompanhada. Embora as métricas específicas possam variar com base no propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitoram:

**Latência:** Quão rapidamente o agente responde? Tempos de espera longos impactam negativamente a experiência do usuário. Você deve medir a latência para tarefas e etapas individuais traçando execuções de agentes. Por exemplo, um agente que demora 20 segundos para todas as chamadas de modelo poderia ser acelerado usando um modelo mais rápido ou executando chamadas de modelo em paralelo.

**Custos:** Qual é a despesa por execução do agente? Agentes de IA dependem de chamadas a LLM cobradas por token ou de APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes por uma melhoria marginal na qualidade, você deve avaliar se o custo é justificado ou se poderia reduzir o número de chamadas ou usar um modelo mais barato. Monitoramento em tempo real também pode ajudar a identificar picos inesperados (por exemplo, bugs causando loops excessivos de API).

**Erros de Requisição:** Quantas requisições o agente falhou? Isso pode incluir erros de API ou chamadas de ferramenta que falharam. Para tornar seu agente mais robusto contra esses problemas em produção, você pode configurar fallback ou tentativas de novo. Por exemplo, se o provedor de LLM A estiver fora do ar, você pode alternar para o provedor de LLM B como backup.

**Feedback do Usuário:** Implementar avaliações diretas pelos usuários fornece insights valiosos. Isso pode incluir classificações explícitas (👍thumbs-up/👎down, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois é um sinal de que o agente não está funcionando como esperado.

**Feedback Implícito do Usuário:** O comportamento dos usuários fornece feedback indireto mesmo sem classificações explícitas. Isso pode incluir reformulação imediata da pergunta, consultas repetidas ou clicar em um botão de tentar novamente. Por exemplo, se você perceber que usuários repetidamente fazem a mesma pergunta, isso é um sinal de que o agente não está funcionando como esperado.

**Precisão:** Com que frequência o agente produz saídas corretas ou desejáveis? Definições de precisão variam (por exemplo, correção na solução de problemas, precisão na recuperação de informações, satisfação do usuário). O primeiro passo é definir o que significa sucesso para seu agente. Você pode rastrear precisão via checagens automatizadas, pontuações de avaliação ou rótulos de conclusão de tarefas. Por exemplo, marcar traces como "succeeded" ou "failed".

**Métricas de Avaliação Automatizadas:** Você também pode configurar avaliações automatizadas. Por exemplo, é possível usar um LLM para pontuar a saída do agente, p.ex. se foi útil, precisa ou não. Existem também várias bibliotecas open source que ajudam a pontuar diferentes aspectos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detectar linguagem prejudicial ou injeção de prompt.

Na prática, uma combinação dessas métricas fornece a melhor cobertura da saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostramos como essas métricas aparecem em exemplos reais, mas primeiro, vamos aprender como é um fluxo de trabalho típico de avaliação.

## Instrumente seu Agente

Para coletar dados de trace, você precisará instrumentar seu código. O objetivo é instrumentar o código do agente para emitir traces e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) emergiu como um padrão da indústria para observabilidade de LLMs. Ele fornece um conjunto de APIs, SDKs e ferramentas para gerar, coletar e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks de agentes existentes e facilitam a exportação de spans do OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo está um exemplo de como instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é rastreada automaticamente
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) neste capítulo demonstrará como instrumentar seu agente MAF.

**Criação Manual de Spans:** Embora bibliotecas de instrumentação forneçam uma boa base, frequentemente há casos onde informações mais detalhadas ou personalizadas são necessárias. Você pode criar spans manualmente para adicionar lógica de aplicação personalizada. Mais importante, eles podem enriquecer spans criados automaticamente ou manualmente com atributos personalizados (também conhecidos como tags ou metadata). Esses atributos podem incluir dados específicos de negócio, cálculos intermediários ou qualquer contexto que possa ser útil para depuração ou análise, tal como `user_id`, `session_id` ou `model_version`.

Exemplo de criação de traces e spans manualmente com o [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

A observabilidade nos dá métricas, mas avaliação é o processo de analisar esses dados (e executar testes) para determinar quão bem um agente de IA está performando e como ele pode ser melhorado. Em outras palavras, uma vez que você tem esses traces e métricas, como usá-los para julgar o agente e tomar decisões?

A avaliação regular é importante porque agentes de IA costumam ser não determinísticos e podem evoluir (através de atualizações ou deriva no comportamento do modelo) — sem avaliação, você não saberia se seu "agente inteligente" está realmente fazendo bem seu trabalho ou se sofreu regressão.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e se complementam. Normalmente começamos com avaliação offline, pois este é o passo mínimo necessário antes de implantar qualquer agente.

### Avaliação Offline

![Itens do conjunto de dados no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isso envolve avaliar o agente em um ambiente controlado, tipicamente usando conjuntos de teste, não consultas de usuários ao vivo. Você usa datasets curados onde sabe qual é a saída esperada ou o comportamento correto e então executa seu agente sobre eles.

Por exemplo, se você construiu um agente para resolver problemas matemáticos em linguagem natural, pode ter um [conjunto de teste](https://huggingface.co/datasets/gsm8k) de 100 problemas com respostas conhecidas. A avaliação offline normalmente é feita durante o desenvolvimento (e pode fazer parte de pipelines de CI/CD) para verificar melhorias ou prevenir regressões. O benefício é que é **repetível e você pode obter métricas de precisão claras já que tem a verdade de referência**. Você também pode simular consultas de usuários e medir as respostas do agente contra respostas ideais ou usar métricas automáticas conforme descrito acima.

O principal desafio da avaliação offline é garantir que seu conjunto de teste seja abrangente e permaneça relevante — o agente pode se sair bem em um conjunto fixo de testes, mas encontrar consultas muito diferentes em produção. Portanto, você deve manter os conjuntos de teste atualizados com novos casos-limite e exemplos que reflitam cenários do mundo real. Uma mistura de pequenos casos de "smoke test" e conjuntos de avaliação maiores é útil: conjuntos pequenos para checagens rápidas e conjuntos maiores para métricas de desempenho mais amplas.

### Avaliação Online

![Visão geral das métricas de observabilidade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Refere-se a avaliar o agente em um ambiente ao vivo, no mundo real, ou seja, durante o uso real em produção. A avaliação online envolve monitorar o desempenho do agente em interações reais com usuários e analisar os resultados continuamente.

Por exemplo, você pode acompanhar taxas de sucesso, pontuações de satisfação do usuário ou outras métricas no tráfego ao vivo. A vantagem da avaliação online é que ela **captura coisas que você pode não antecipar em um ambiente de laboratório** — você pode observar deriva do modelo ao longo do tempo (se a eficácia do agente degradar à medida que os padrões de entrada mudam) e detectar consultas ou situações inesperadas que não estavam nos seus dados de teste. Ela fornece uma imagem verdadeira de como o agente se comporta no ambiente real.

A avaliação online frequentemente envolve coletar feedback implícito e explícito dos usuários, como discutido, e possivelmente executar testes shadow ou A/B (onde uma nova versão do agente roda em paralelo para comparar com a antiga). O desafio é que pode ser complicado obter rótulos ou pontuações confiáveis para interações ao vivo — você pode depender de feedback do usuário ou métricas downstream (como se o usuário clicou no resultado).

### Combinando os dois

Avaliações online e offline não são mutuamente exclusivas; elas se complementam fortemente. Insights do monitoramento online (por exemplo, novos tipos de consultas de usuários onde o agente performa mal) podem ser usados para aumentar e melhorar os conjuntos de teste offline. Por outro lado, agentes que se saem bem em testes offline podem então ser implantados com mais confiança e monitorados online.

De fato, muitas equipes adotam um ciclo:

_avaliar offline -> implantar -> monitorar online -> coletar novos casos de falha -> adicionar ao conjunto de dados offline -> aprimorar o agente -> repetir_.

## Problemas Comuns

Ao implantar agentes de IA em produção, você pode encontrar vários desafios. Aqui estão alguns problemas comuns e suas potenciais soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Refine o prompt dado ao Agente de IA; seja claro quanto aos objetivos.<br>- Identifique onde dividir as tarefas em subtarefas e tratá-las por múltiplos agentes pode ajudar. |
| AI Agent running into continuous loops  | - Garanta que você tenha termos e condições de término claros para que o Agente saiba quando finalizar o processo.<br>- Para tarefas complexas que exigem raciocínio e planejamento, use um modelo maior que seja especializado em tarefas de raciocínio. |
| AI Agent tool calls are not performing well   | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e a nomeação das ferramentas.  |
| Multi-Agent system not performing consistently | - Refine os prompts dados a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construa um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

Muitos desses problemas podem ser identificados de forma mais eficaz com observabilidade em funcionamento. Os traces e métricas que discutimos anteriormente ajudam a identificar exatamente onde no fluxo de trabalho do agente os problemas ocorrem, tornando a depuração e otimização muito mais eficientes.

## Gerenciamento de Custos
Aqui estão algumas estratégias para gerenciar os custos de colocar agentes de IA em produção:

**Using Smaller Models:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso com agentes e reduzirão os custos significativamente. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor maneira de entender quão bem um SLM funcionará no seu caso de uso. Considere usar SLMs para tarefas mais simples como classificação de intenções ou extração de parâmetros, reservando modelos maiores para raciocínios complexos.

**Using a Router Model:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou uma função sem servidor para roteirizar requisições com base na complexidade para os modelos mais adequados. Isso também ajudará a reduzir custos ao mesmo tempo em que garante desempenho nas tarefas corretas. Por exemplo, direcione consultas simples para modelos menores e mais rápidos, e use modelos grandes e caros apenas para tarefas de raciocínio complexas.

**Caching Responses:** Identificar requisições e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema com agentes é uma boa maneira de reduzir o volume de requisições semelhantes. Você pode até implementar um fluxo para identificar quão similar uma requisição é às suas requisições em cache usando modelos de IA mais básicos. Essa estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isso funciona na prática

In the [example notebook of this section](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.


### Tem mais perguntas sobre Agentes de IA em produção?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar de horários de atendimento e obter respostas para suas perguntas sobre Agentes de IA.

## Lição Anterior

[Padrão de Metacognição](../09-metacognition/README.md)

## Próxima Lição

[Protocolos Agenciais](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido usando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->