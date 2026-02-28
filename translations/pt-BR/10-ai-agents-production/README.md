# Agentes de IA em Produção: Observabilidade e Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-BR/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, a capacidade de entender seu comportamento, monitorar seu desempenho e avaliar sistematicamente suas saídas torna-se importante.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como/entenderá:
- Conceitos centrais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar seus agentes de IA de forma sistemática
- Como controlar custos ao implantar agentes de IA em produção
- Como instrumentar agentes construídos com o Microsoft Agent Framework

O objetivo é equipá-lo com o conhecimento para transformar seus agentes "caixa-preta" em sistemas transparentes, gerenciáveis e confiáveis.

_**Nota:** É importante implantar Agentes de IA que sejam seguros e confiáveis. Confira também a lição [Construindo Agentes de IA Confiáveis](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como traces e spans.

- **Trace** representa uma tarefa completa do agente do início ao fim (como lidar com uma consulta de usuário).
- **Spans** são etapas individuais dentro do trace (como chamar um modelo de linguagem ou recuperar dados).

![Árvore de traces no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa-preta" — seu estado interno e raciocínio são opacos, tornando difícil diagnosticar problemas ou otimizar o desempenho. Com observabilidade, os agentes se tornam "caixas de vidro", oferecendo transparência que é vital para construir confiança e garantir que operem conforme o esperado.

## Por que a Observabilidade Importa em Ambientes de Produção

A transição de agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. Observabilidade deixa de ser um "algo agradável de ter" e se torna uma capacidade crítica:

*   **Depuração e Análise de Causa Raiz**: Quando um agente falha ou produz uma saída inesperada, ferramentas de observabilidade fornecem os traces necessários para localizar a origem do erro. Isso é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLMs, interações com ferramentas e lógica condicional.
*   **Gerenciamento de Latência e Custos**: Agentes de IA frequentemente dependem de LLMs e outras APIs externas que são cobradas por token ou por chamada. A observabilidade permite o rastreamento preciso dessas chamadas, ajudando a identificar operações que são excessivamente lentas ou caras. Isso permite às equipes otimizar prompts, selecionar modelos mais eficientes ou redesenhar fluxos de trabalho para gerenciar custos operacionais e garantir uma boa experiência do usuário.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportem de maneira segura e ética. A observabilidade fornece uma trilha de auditoria das ações e decisões do agente. Isso pode ser usado para detectar e mitigar problemas como prompt injection, geração de conteúdo nocivo ou manuseio inadequado de informações pessoalmente identificáveis (PII). Por exemplo, você pode revisar traces para entender por que um agente deu determinada resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Dados de observabilidade são a base de um processo iterativo de desenvolvimento. Monitorando como os agentes performam no mundo real, as equipes podem identificar áreas para melhoria, coletar dados para ajuste fino de modelos e validar o impacto de mudanças. Isso cria um ciclo de feedback onde insights de produção de avaliações online informam experimentos e refinamentos offline, levando a um desempenho progressivamente melhor dos agentes.

## Principais Métricas a Monitorar

Para monitorar e entender o comportamento do agente, uma variedade de métricas e sinais deve ser acompanhada. Embora as métricas específicas possam variar com base no propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que ferramentas de observabilidade monitoram:

**Latência:** Quão rapidamente o agente responde? Tempos de espera longos impactam negativamente a experiência do usuário. Você deve medir a latência para tarefas e etapas individuais rastreando execuções do agente. Por exemplo, um agente que leva 20 segundos para todas as chamadas de modelo pode ser acelerado usando um modelo mais rápido ou executando chamadas de modelo em paralelo.

**Custos:** Qual é o gasto por execução do agente? Agentes de IA dependem de chamadas a LLMs cobradas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes por melhoria marginal de qualidade, é preciso avaliar se o custo é justificado ou se você poderia reduzir o número de chamadas ou usar um modelo mais barato. Monitoramento em tempo real também pode ajudar a identificar picos inesperados (por exemplo, bugs causando loops excessivos de API).

**Erros de Requisição:** Quantas requisições o agente falhou? Isso pode incluir erros de API ou chamadas de ferramentas que falharam. Para tornar seu agente mais robusto contra isso em produção, você pode configurar fallback ou retries. Ex.: se o provedor de LLM A estiver fora do ar, você alterna para o provedor de LLM B como backup.

**Feedback do Usuário:** Implementar avaliações diretas dos usuários fornece insights valiosos. Isso pode incluir avaliações explícitas (👍thumbs-up/👎down, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois é um sinal de que o agente não está funcionando como esperado.

**Feedback Implícito do Usuário:** Comportamentos dos usuários fornecem feedback indireto mesmo sem avaliações explícitas. Isso pode incluir reformulação imediata da pergunta, consultas repetidas ou clicar em um botão de tentar novamente. Ex.: se você perceber que os usuários repetidamente fazem a mesma pergunta, isso é um sinal de que o agente não está funcionando como esperado.

**Precisão:** Com que frequência o agente produz saídas corretas ou desejáveis? As definições de precisão variam (por exemplo, correção na resolução de problemas, precisão na recuperação de informações, satisfação do usuário). O primeiro passo é definir como o sucesso se parece para o seu agente. Você pode monitorar a precisão via verificações automatizadas, pontuações de avaliação ou rótulos de conclusão de tarefas. Por exemplo, marcar traces como "succeeded" ou "failed".

**Métricas de Avaliação Automatizadas:** Você também pode configurar avaliações automatizadas. Por exemplo, você pode usar um LLM para pontuar a saída do agente, p.ex. se foi útil, precisa ou não. Existem também várias bibliotecas open source que ajudam a pontuar diferentes aspectos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detectar linguagem prejudicial ou prompt injection.

Na prática, uma combinação dessas métricas oferece a melhor cobertura da saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como essas métricas aparecem em exemplos reais, mas primeiro, vamos aprender como é um fluxo típico de avaliação.

## Instrumente seu Agente

Para coletar dados de tracing, você precisará instrumentar seu código. O objetivo é instrumentar o código do agente para emitir traces e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) emergiu como um padrão da indústria para observabilidade de LLMs. Ele fornece um conjunto de APIs, SDKs e ferramentas para gerar, coletar e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks de agentes existentes e facilitam a exportação de spans do OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo está um exemplo de instrumentação de um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é rastreada automaticamente
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) neste capítulo demonstrará como instrumentar seu agente MAF.

**Criação Manual de Spans:** Embora bibliotecas de instrumentação forneçam uma boa linha de base, frequentemente existem casos em que informações mais detalhadas ou personalizadas são necessárias. Você pode criar spans manualmente para adicionar lógica de aplicação personalizada. Mais importante, eles podem enriquecer spans criados automaticamente ou manualmente com atributos personalizados (também conhecidos como tags ou metadados). Esses atributos podem incluir dados específicos de negócio, cálculos intermediários ou qualquer contexto que possa ser útil para depuração ou análise, tais como `user_id`, `session_id` ou `model_version`.

Exemplo de criação de traces e spans manualmente com o [SDK Python do Langfuse](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

Observabilidade nos dá métricas, mas avaliação é o processo de analisar esses dados (e realizar testes) para determinar quão bem um agente de IA está performando e como ele pode ser melhorado. Em outras palavras, uma vez que você tenha esses traces e métricas, como você os usa para julgar o agente e tomar decisões?

Avaliação regular é importante porque agentes de IA costumam ser não determinísticos e podem evoluir (por meio de atualizações ou mudança no comportamento do modelo) – sem avaliação, você não saberia se seu "agente inteligente" realmente está fazendo bem seu trabalho ou se regrediu.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e se complementam. Geralmente começamos com avaliação offline, pois este é o passo mínimo necessário antes de implantar qualquer agente.

### Avaliação Offline

![Itens do conjunto de dados no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isso envolve avaliar o agente em um ambiente controlado, tipicamente usando conjuntos de teste, não consultas de usuários ao vivo. Você usa conjuntos de dados curados nos quais você sabe qual é a saída esperada ou comportamento correto, e então executa seu agente nesses dados.

Por exemplo, se você construiu um agente para resolver problemas matemáticos em forma de texto, pode ter um [conjunto de dados de teste](https://huggingface.co/datasets/gsm8k) de 100 problemas com respostas conhecidas. A avaliação offline é frequentemente feita durante o desenvolvimento (e pode fazer parte de pipelines de CI/CD) para verificar melhorias ou proteger contra regressões. O benefício é que é **reproduzível e você pode obter métricas claras de precisão já que possui o ground truth**. Você também pode simular consultas de usuários e medir as respostas do agente contra respostas ideais ou usar métricas automatizadas conforme descrito acima.

O desafio principal com avaliação offline é garantir que seu conjunto de testes seja abrangente e permaneça relevante – o agente pode performar bem em um conjunto de teste fixo, mas encontrar consultas muito diferentes em produção. Portanto, você deve manter os conjuntos de teste atualizados com novos casos de borda e exemplos que reflitam cenários do mundo real​. Uma mistura de pequenos casos de "smoke test" e conjuntos de avaliação maiores é útil: conjuntos pequenos para verificações rápidas e maiores para métricas de desempenho mais amplas​.

### Avaliação Online 

![Visão geral das métricas de observabilidade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Refere-se a avaliar o agente em um ambiente ao vivo, no mundo real, ou seja, durante o uso real em produção. A avaliação online envolve monitorar o desempenho do agente em interações reais de usuários e analisar os resultados continuamente.

Por exemplo, você pode rastrear taxas de sucesso, pontuações de satisfação do usuário ou outras métricas no tráfego ao vivo. A vantagem da avaliação online é que ela **captura coisas que você pode não antecipar em um ambiente de laboratório** – você pode observar drift do modelo ao longo do tempo (se a eficácia do agente degradar conforme os padrões de entrada mudam) e detectar consultas ou situações inesperadas que não estavam em seus dados de teste​. Ela fornece uma imagem verdadeira de como o agente se comporta em produção.

A avaliação online frequentemente envolve coletar feedback implícito e explícito dos usuários, como discutido, e possivelmente executar testes shadow ou A/B (onde uma nova versão do agente roda em paralelo para comparar com a antiga). O desafio é que pode ser complicado obter rótulos ou pontuações confiáveis para interações ao vivo – você pode depender do feedback do usuário ou métricas downstream (como se o usuário clicou no resultado).

### Combinando os dois

Avaliações online e offline não são mutuamente exclusivas; elas se complementam bastante. Insights do monitoramento online (por exemplo, novos tipos de consultas de usuários onde o agente performa mal) podem ser usados para aumentar e melhorar os conjuntos de testes offline. Por outro lado, agentes que se saem bem em testes offline podem ser implantados com mais confiança e monitorados online.

De fato, muitas equipes adotam um loop:

_avaliar offline -> implantar -> monitorar online -> coletar novos casos de falha -> adicionar ao conjunto de dados offline -> refinar o agente -> repetir_.

## Problemas Comuns

Ao implantar agentes de IA em produção, você pode encontrar vários desafios. Aqui estão alguns problemas comuns e suas potenciais soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas de forma consistente | - Refine o prompt fornecido ao Agente de IA; seja claro quanto aos objetivos.<br>- Identifique onde dividir as tarefas em subtarefas e delegá-las a múltiplos agentes pode ajudar. |
| Agente de IA entrando em loops contínuos  | - Certifique-se de ter termos e condições de finalização claros para que o Agente saiba quando encerrar o processo.<br>- Para tarefas complexas que exigem raciocínio e planejamento, utilize um modelo maior especializado para tarefas de raciocínio. |
| Chamadas de ferramentas do Agente de IA não estão funcionando bem   | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e nomes das ferramentas.  |
| Sistema Multi-Agente não executa de forma consistente | - Refine os prompts dados a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construa um sistema hierárquico usando um agente "routing" ou controlador para determinar qual agente é o correto. |

Muitos desses problemas podem ser identificados de forma mais eficaz com observabilidade em funcionamento. Os traces e métricas que discutimos anteriormente ajudam a apontar exatamente onde no fluxo de trabalho do agente os problemas ocorrem, tornando a depuração e otimização muito mais eficientes.

## Gerenciando Custos
Here are some strategies to manage the costs of deploying AI agents to production:

**Usando Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentivos e reduzirão os custos significativamente. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor forma de entender quão bem um SLM irá performar no seu caso de uso. Considere usar SLMs para tarefas mais simples como classificação de intenção ou extração de parâmetros, reservando modelos maiores para raciocínios complexos.

**Usando um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou uma função serverless para rotear requisições com base na complexidade para os modelos mais adequados. Isso também ajudará a reduzir custos enquanto garante desempenho nas tarefas corretas. Por exemplo, direcione consultas simples para modelos menores e mais rápidos, e use modelos grandes e caros somente para tarefas de raciocínio complexas.

**Cache de Respostas:** Identificar solicitações e tarefas comuns e fornecer as respostas antes que elas passem pelo seu sistema de agentes é uma boa forma de reduzir o volume de requisições semelhantes. Você pode até implementar um fluxo para identificar quão similar uma solicitação é em relação às suas requisições em cache usando modelos de IA mais básicos. Essa estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isso funciona na prática

No [notebook de exemplo desta seção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorar e avaliar nosso agente.


### Tem mais perguntas sobre Agentes de IA em Produção?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horários de atendimento e ter suas perguntas sobre Agentes de IA respondidas.

## Lição Anterior

[Padrão de Metacognição](../09-metacognition/README.md)

## Próxima Lição

[Protocolos para Agentes](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->