# Agentes de IA em Produção: Observabilidade & Avaliação

[![AI Agents in Production](../../../translated_images/pt-PT/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, torna-se importante a capacidade de compreender o seu comportamento, monitorizar o seu desempenho e avaliar sistematicamente os seus resultados.

## Objetivos de Aprendizagem

Após concluir esta lição, irá saber como/compreender:
- Conceitos fundamentais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar os seus agentes de IA sistematicamente
- Como controlar custos ao implantar agentes de IA em produção
- Como instrumentar agentes construídos com o Microsoft Agent Framework

O objetivo é dotá-lo com o conhecimento para transformar os seus agentes "caixa preta" em sistemas transparentes, geríveis e fiáveis.

_**Nota:** É importante implementar Agentes de IA que sejam seguros e de confiança. Consulte também a lição [Construir Agentes de IA Confiáveis](./06-building-trustworthy-agents/README.md)._

## Traços e Spans

Ferramentas de observabilidade como o [Langfuse](https://langfuse.com/) ou o [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como traços e spans.

- **Traço** representa uma tarefa completa do agente do início ao fim (por exemplo, tratar uma consulta de utilizador).
- **Spans** são os passos individuais dentro do traço (por exemplo, chamar um modelo de linguagem ou recuperar dados).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa preta" - o seu estado interno e raciocínio são opacos, dificultando o diagnóstico de problemas ou a otimização do desempenho. Com a observabilidade, os agentes tornam-se "caixas de vidro", oferecendo transparência que é vital para construir confiança e garantir que operam conforme o esperado.

## Porque é que a Observabilidade é Importante em Ambientes de Produção

A transição de agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. A observabilidade deixa de ser um luxo e passa a ser uma capacidade crítica:

*   **Depuração e Análise da Causa Raiz:** Quando um agente falha ou produz um resultado inesperado, as ferramentas de observabilidade fornecem os traços necessários para identificar a origem do erro. Isto é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLM, interações com ferramentas e lógica condicional.
*   **Gestão de Latência e Custos:** Os agentes de IA frequentemente dependem de LLM e outras APIs externas que são faturadas por token ou por chamada. A observabilidade permite monitorizar com precisão essas chamadas, ajudando a identificar operações excessivamente lentas ou caras. Isto permite às equipas otimizar prompts, escolher modelos mais eficientes ou redesenhar fluxos de trabalho para gerir custos operacionais e garantir uma boa experiência do utilizador.
*   **Confiança, Segurança e Conformidade:** Em muitas aplicações, é importante garantir que os agentes se comportam de forma segura e ética. A observabilidade fornece uma trilha de auditoria das ações e decisões do agente. Esta pode ser usada para detectar e mitigar problemas como injeção de prompts, geração de conteúdo nocivo ou manuseamento incorreto de informações pessoalmente identificáveis (PII). Por exemplo, pode rever traços para entender porque um agente deu determinada resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua:** Os dados de observabilidade são a base para um processo iterativo de desenvolvimento. Ao monitorizar como os agentes performam no mundo real, as equipas podem identificar áreas para melhoria, reunir dados para afinar modelos e validar o impacto das alterações. Isto cria um ciclo de feedback onde as informações de produção a partir da avaliação online informam experimentação e refinamento offline, conduzindo a um desempenho progressivamente melhor dos agentes.

## Métricas Principais a Monitorizar

Para monitorizar e compreender o comportamento do agente, devemo monitorizar uma gama de métricas e sinais. Embora as métricas específicas possam variar com base no propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitorizam:

**Latência:** Quão rápido responde o agente? Tempos de espera longos impactam negativamente a experiência do utilizador. Deve medir a latência para tarefas e passos individuais ao traçar execuções do agente. Por exemplo, um agente que demora 20 segundos em todas as chamadas ao modelo pode ser acelerado usando um modelo mais rápido ou executando chamadas em paralelo.

**Custos:** Qual é o custo por execução do agente? Os agentes de IA dependem de chamadas a LLM faturadas por token ou APIs externas. O uso frequente de ferramentas ou múltiplos prompts pode aumentar os custos rapidamente. Por exemplo, se um agente chama um LLM cinco vezes para uma melhoria marginal na qualidade, deve avaliar se o custo compensa ou se poderia reduzir o número de chamadas ou usar um modelo mais barato. A monitorização em tempo real pode também ajudar a identificar picos inesperados (ex.: bugs causando loops excessivos de API).

**Erros de Pedido:** Quantos pedidos falharam? Isto pode incluir erros de API ou falhas nas chamadas a ferramentas. Para tornar o agente mais robusto contra estas falhas em produção, pode configurar backups ou tentativas repetidas. Ex.: se o fornecedor A do LLM estiver indisponível, mudar para o fornecedor B como alternativa.

**Feedback do Utilizador:** Implementar avaliações diretas dos utilizadores fornece insights valiosos. Isto pode incluir classificações explícitas (👍positivo/👎negativo, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois é um sinal que o agente não está a funcionar como esperado.

**Feedback Implícito do Utilizador:** Os comportamentos dos utilizadores fornecem feedback indireto mesmo sem avaliações explícitas. Isto pode incluir reformulação imediata de perguntas, perguntas repetidas ou clique em botão de tentar novamente. Ex.: se verificar que os utilizadores repetidamente fazem a mesma pergunta, é sinal que o agente não está a funcionar como esperado.

**Precisão:** Com que frequência o agente produz resultados correctos ou desejáveis? As definições de precisão variam (ex.: correção na resolução de problemas, precisão na recuperação de informação, satisfação do utilizador). O primeiro passo é definir o que significa sucesso para o seu agente. Pode monitorizar a precisão via verificações automáticas, pontuações de avaliação ou etiquetas de conclusão de tarefas. Por exemplo, marcar traços como "sucesso" ou "falhou".

**Métricas de Avaliação Automatizada:** Pode também configurar avaliações automáticas. Por exemplo, pode usar um LLM para pontuar a saída do agente, avaliando se é útil, precisa ou não. Existem também várias bibliotecas open source que ajudam a pontuar diferentes aspetos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detectar linguagem nociva ou injeção de prompts.

Na prática, uma combinação destas métricas oferece a melhor cobertura do estado de saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como estas métricas se traduzem em exemplos reais, mas primeiro aprenderemos como é um fluxo típico de avaliação.

## Instrumentar o Seu Agente

Para recolher dados de tracing, precisará de instrumentar o seu código. O objetivo é instrumentar o código do agente para emitir traços e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** O [OpenTelemetry](https://opentelemetry.io/) emergiu como um padrão da indústria para observabilidade de LLM. Fornece um conjunto de APIs, SDKs e ferramentas para gerar, recolher e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks de agentes existentes e facilitam a exportação de spans OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo está um exemplo de como instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é registada automaticamente
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo demonstrará como instrumentar o seu agente MAF.

**Criação Manual de Span:** Embora as bibliotecas de instrumentação forneçam uma boa base, há frequentemente casos onde são necessárias informações mais detalhadas ou personalizadas. Pode criar spans manualmente para adicionar lógica personalizada à aplicação. Mais importante ainda, pode enriquecer spans criados automática ou manualmente com atributos personalizados (também conhecidos como etiquetas ou metadados). Estes atributos podem incluir dados específicos do negócio, cálculos intermédios ou qualquer contexto útil para depuração ou análise, como `user_id`, `session_id` ou `model_version`.

Exemplo de criação manual de traços e spans com o [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

A observabilidade fornece-nos métricas, mas a avaliação é o processo de analisar esses dados (e realizar testes) para determinar quão bem um agente de IA está a desempenhar e como pode ser melhorado. Ou seja, uma vez que tem esses traços e métricas, como os usa para avaliar o agente e tomar decisões?

A avaliação regular é importante porque os agentes de IA são frequentemente não determinísticos e podem evoluir (através de atualizações ou alteração do comportamento do modelo) – sem avaliação, não saberia se o seu “agente inteligente” está realmente a executar bem o seu trabalho ou se regrediu.

Existem duas categorias de avaliação para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas, e complementam-se. Normalmente começamos com avaliação offline, que é o passo mínimo necessário antes de implantar qualquer agente.

### Avaliação Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isto envolve avaliar o agente num ambiente controlado, normalmente usando conjuntos de dados de teste, não consultas de utilizadores em direto. Usa conjuntos de dados curados onde sabe qual a saída ou comportamento esperado, e depois executa o seu agente nesses dados.

Por exemplo, se construiu um agente para problemas matemáticos em texto, pode ter um [conjunto de dados de teste](https://huggingface.co/datasets/gsm8k) com 100 problemas com respostas conhecidas. A avaliação offline é frequentemente feita durante o desenvolvimento (e pode fazer parte de pipelines CI/CD) para verificar melhorias ou prevenir regressões. A vantagem é que é **repetível e pode obter métricas claras de precisão dado que tem a verdade de base**. Pode também simular consultas de utilizador e medir as respostas do agente contra respostas ideais ou usar métricas automatizadas como descrito acima.

O principal desafio da avaliação offline é garantir que o seu conjunto de dados de teste seja abrangente e se mantenha relevante – o agente pode performar bem num conjunto fixo de teste, mas encontrar consultas muito diferentes em produção. Portanto, deve manter os conjuntos de teste atualizados com novos casos extremos e exemplos que refletem cenários do mundo real. Uma mistura de pequenos casos de "teste de fumo" e conjuntos maiores de avaliação é útil: conjuntos pequenos para verificações rápidas e maiores para métricas de desempenho mais amplas.

### Avaliação Online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Refere-se à avaliação do agente num ambiente real e em tempo real, ou seja, durante o uso real em produção. A avaliação online envolve monitorizar o desempenho do agente em interações reais com utilizadores e analisar os resultados continuamente.

Por exemplo, pode monitorizar taxas de sucesso, pontuações de satisfação do utilizador ou outras métricas no tráfego real. A vantagem da avaliação online é que **capta situações que talvez não antecipasse num laboratório** – pode observar deriva do modelo ao longo do tempo (se a eficácia do agente degradar conforme os padrões de entrada mudam) e identificar consultas ou situações inesperadas que não estavam incluídas nos seus dados de teste. Proporciona uma visão real de como o agente se comporta no “campo”.

A avaliação online frequentemente envolve a recolha de feedback implícito e explícito dos utilizadores, como discutido, e possivelmente a execução de testes em paralelo (shadow tests) ou testes A/B (onde uma nova versão do agente corre em paralelo para comparação com a antiga). O desafio é que pode ser difícil obter rótulos ou pontuações fiáveis para interações em direto – pode ter de depender do feedback dos utilizadores ou métricas subsequentes (ex.: se o utilizador clicou no resultado).

### Combinar os Dois

As avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Os insights da monitorização online (ex.: novos tipos de consultas de utilizador onde o agente performa mal) podem ser usados para aumentar e melhorar conjuntos de teste offline. Por outro lado, agentes que performam bem em testes offline podem depois ser implantados com mais confiança e monitorizados online.

Na verdade, muitas equipas adotam um ciclo:

_avaliar offline -> implantar -> monitorizar online -> recolher novos casos de falha -> adicionar ao conjunto de dados offline -> refinar agente -> repetir_.

## Problemas Comuns

Ao implantar agentes de IA em produção, pode encontrar vários desafios. Aqui estão alguns problemas comuns e as suas possíveis soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas de forma consistente | - Refinar o prompt dado ao Agente de IA; ser claro nos objetivos.<br>- Identificar onde dividir as tarefas em subtarefas e lidar com elas por múltiplos agentes pode ajudar. |
| Agente de IA entra em loops contínuos  | - Garantir termos e condições claras de término para que o agente saiba quando parar o processo.<br>- Para tarefas complexas que requerem raciocínio e planeamento, usar um modelo maior especializado em tarefas de raciocínio. |
| Chamadas a ferramentas do agente de IA não funcionam bem   | - Testar e validar a saída da ferramenta fora do sistema do agente.<br>- Refinar os parâmetros definidos, prompts e nomes das ferramentas.  |
| Sistema Multi-Agente não performa consistentemente | - Refinar prompts dados a cada agente para garantir que são específicos e distintos entre si.<br>- Construir um sistema hierárquico usando um agente "routador" ou controlador para determinar qual agente é o correto. |

Muitos destes problemas podem ser identificados com maior eficácia se tiver observabilidade implementada. Os traços e métricas que discutimos anteriormente ajudam a localizar exatamente onde ocorrem os problemas no fluxo de trabalho do agente, tornando a depuração e otimização muito mais eficientes.

## Gestão de Custos
Aqui estão algumas estratégias para gerir os custos de implementação de agentes de IA em produção:

**Usar Modelos Mais Pequenos:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentes e irão reduzir significativamente os custos. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho face a modelos maiores é a melhor forma de compreender quão bem um SLM irá desempenhar no seu caso de uso. Considere usar SLMs para tarefas mais simples como classificação de intenções ou extração de parâmetros, reservando modelos maiores para raciocínios complexos.

**Usar um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Pode usar um LLM/SLM ou uma função serverless para encaminhar pedidos com base na complexidade para os modelos mais adequados. Isto também ajudará a reduzir custos garantindo o desempenho nas tarefas corretas. Por exemplo, encaminhe consultas simples para modelos menores e mais rápidos, e apenas use modelos grandes e dispendiosos para tarefas de raciocínio complexo.

**Cache de Respostas:** Identificar pedidos e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agente é uma boa forma de reduzir o volume de pedidos semelhantes. Pode até implementar um fluxo para identificar quão semelhante é um pedido aos seus pedidos em cache usando modelos de IA mais básicos. Esta estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isto funciona na prática

No [notebook de exemplo desta secção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorizar e avaliar o nosso agente.


### Tem Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar em horas de expediente e obter respostas às suas perguntas sobre Agentes de IA.

## Aula Anterior

[Metacognition Design Pattern](../09-metacognition/README.md)

## Próxima Aula

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automatizadas podem conter erros ou incorreções. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->