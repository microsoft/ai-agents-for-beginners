# Agentes de IA em Produção: Observabilidade & Avaliação

[![AI Agents in Production](../../../translated_images/pt-PT/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA evoluem de protótipos experimentais para aplicações no mundo real, torna-se importante a capacidade de compreender o seu comportamento, monitorizar o seu desempenho e avaliar sistematicamente os seus outputs.

## Objetivos de Aprendizagem

Depois de concluir esta lição, irá saber como/compreender:
- Conceitos fundamentais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar os seus agentes de IA de forma sistemática
- Como controlar os custos ao colocar agentes de IA em produção
- Como instrumentar agentes construídos com Microsoft Agent Framework

O objetivo é dotá-lo do conhecimento para transformar os seus agentes “caixa preta” em sistemas transparentes, geríveis e fiáveis.

_**Nota:** É importante implementar Agentes de IA que sejam seguros e confiáveis. Consulte também a lição [Construir Agentes de IA Confiáveis](./06-building-trustworthy-agents/README.md)._

## Traces e Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como traces e spans.

- **Trace** representa uma tarefa completa do agente do início ao fim (como lidar com uma consulta de um utilizador).
- **Spans** são os passos individuais dentro do trace (como chamar um modelo de linguagem ou recuperar dados).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa preta" – o seu estado interno e raciocínio são opacos, dificultando a deteção de problemas ou a otimização do desempenho. Com observabilidade, os agentes tornam-se "caixas de vidro", oferecendo transparência vital para criar confiança e garantir que funcionam conforme o esperado.

## Porque é que a Observabilidade é Importante em Ambientes de Produção

A transição dos agentes de IA para ambientes de produção traz um novo conjunto de desafios e requisitos. A observabilidade deixa de ser um "luxo" e passa a ser uma capacidade crítica:

*   **Depuração e Análise da Causa Raiz**: Quando um agente falha ou produz um output inesperado, as ferramentas de observabilidade fornecem os traces necessários para identificar a origem do erro. Isto é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLMs, interações com ferramentas e lógica condicional.
*   **Gestão da Latência e Custos**: Os agentes de IA frequentemente dependem de LLMs e outras APIs externas cobradas por token ou chamada. A observabilidade permite o rastreamento preciso destas chamadas, ajudando a identificar operações excessivamente lentas ou dispendiosas. Isto permite às equipas otimizar prompts, escolher modelos mais eficientes ou redesenhar fluxos de trabalho para gerir os custos operacionais e garantir uma boa experiência ao utilizador.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportam de forma segura e ética. A observabilidade fornece um registo de auditoria das ações e decisões do agente. Isto pode ser usado para detetar e mitigar problemas como injeção de prompt, geração de conteúdo nocivo ou o tratamento incorreto de informação pessoal identificável (PII). Por exemplo, pode rever traces para compreender porque é que um agente forneceu uma certa resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Os dados de observabilidade são a base do processo iterativo de desenvolvimento. Ao monitorizar o desempenho dos agentes no mundo real, as equipas podem identificar áreas para melhoria, recolher dados para afinação de modelos e validar o impacto das alterações. Isto cria um ciclo de feedback onde os insights da avaliação online em produção informam a experimentação e refinamento offline, levando a um desempenho progressivamente melhor do agente.

## Métricas Principais a Monitorizar

Para monitorizar e compreender o comportamento do agente, deve-se acompanhar uma variedade de métricas e sinais. Embora as métricas específicas possam variar consoante o propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitorizam:

**Latência:** Com que rapidez responde o agente? Tempos de espera longos impactam negativamente a experiência do utilizador. Deve medir a latência das tarefas e passos individuais, acompanhando execuções do agente. Por exemplo, um agente que demora 20 segundos para todas as chamadas ao modelo pode ser acelerado usando um modelo mais rápido ou executando chamadas em paralelo.

**Custos:** Qual o custo por execução do agente? Os agentes de IA dependem de chamadas a LLM cobradas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts podem aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes para melhorar marginalmente a qualidade, deve avaliar se o custo é justificado ou se pode reduzir o número de chamadas ou usar um modelo mais barato. A monitorização em tempo real ajuda a identificar picos inesperados (por exemplo, bugs que causam ciclos excessivos de API).

**Erros nas Requisições:** Quantas requisições falhou o agente? Isto pode incluir erros de API ou chamadas a ferramentas falhadas. Para tornar o agente mais robusto em produção, pode configurar metodologias de fallback ou tentativas repetidas. Ex.: se o fornecedor LLM A estiver indisponível, alternar para o fornecedor LLM B como reserva.

**Feedback do Utilizador:** A implementação de avaliações diretas do utilizador fornece insights valiosos. Isto pode incluir classificações explícitas (👍gosto/👎não gosto, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois é sinal de que o agente não está a funcionar como esperado.

**Feedback Implícito do Utilizador:** O comportamento do utilizador fornece feedback indireto mesmo sem classificações explícitas. Pode incluir reestruturação imediata da pergunta, consultas repetidas ou clique num botão de retry. Ex.: se os utilizadores repetidamente fazem a mesma pergunta, é sinal de que o agente não está a funcionar como esperado.

**Precisão:** Com que frequência o agente produz outputs corretos ou desejáveis? As definições de precisão variam (exemplos: correção na resolução de problemas, precisão na recuperação de informação, satisfação do utilizador). O primeiro passo é definir o que significa sucesso para o seu agente. Pode acompanhar a precisão através de verificações automatizadas, pontuações de avaliação ou etiquetas de conclusão de tarefa. Por exemplo, marcar traces como "sucesso" ou "falha".

**Métricas de Avaliação Automática:** Também pode configurar avaliações automáticas. Por exemplo, usar um LLM para avaliar o output do agente, se é útil, preciso ou não. Existem várias bibliotecas open source que ajudam a pontuar diferentes aspetos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detetar linguagem nociva ou injeção de prompt.

Na prática, uma combinação destas métricas oferece a melhor cobertura da saúde de um agente de IA. No [exemplo de notebook](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como estas métricas se apresentam em exemplos reais, mas antes vamos aprender como é um fluxo típico de avaliação.

## Instrumentar o Seu Agente

Para recolher dados de tracing, precisará de instrumentar o seu código. O objetivo é instrumentar o código do agente para emitir traces e métricas que possam ser capturadas, processadas e visualizadas por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) emergiu como um padrão da indústria para a observabilidade de LLMs. Fornece um conjunto de APIs, SDKs e ferramentas para gerar, recolher e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks de agentes existentes e facilitam a exportação de spans OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo está um exemplo de instrumentação de um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é rastreada automaticamente
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) neste capítulo vai demonstrar como instrumentar o seu agente MAF.

**Criação Manual de Spans:** Embora as bibliotecas de instrumentação forneçam uma boa base, existem casos em que são necessárias informações mais detalhadas ou personalizadas. Pode criar spans manualmente para adicionar lógica personalizada à aplicação. Ainda mais importante, pode enriquecer spans criados automaticamente ou manualmente com atributos personalizados (também conhecidos como tags ou metadata). Estes atributos podem incluir dados específicos de negócio, cálculos intermédios ou qualquer contexto útil para debugar ou analisar, como `user_id`, `session_id` ou `model_version`.

Exemplo de criação manual de traces e spans com o [SDK Python Langfuse](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

A observabilidade fornece métricas, mas a avaliação é o processo de analisar esses dados (e realizar testes) para determinar quão bem um agente de IA está a desempenhar e como pode ser melhorado. Em outras palavras, uma vez que tem esses traces e métricas, como os usa para julgar o agente e tomar decisões?

A avaliação regular é importante porque os agentes de IA são frequentemente não determinísticos e podem evoluir (através de atualizações ou mudança no comportamento do modelo) – sem avaliação, não saberia se o seu “agente inteligente” está realmente a cumprir bem a sua função ou se regrediu.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e complementares. Normalmente começamos pela avaliação offline, pois é o passo mínimo necessário antes de colocar qualquer agente em produção.

### Avaliação Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Esta avaliação envolve testar o agente num ambiente controlado, tipicamente usando conjuntos de dados de teste, e não consultas de utilizadores ao vivo. Usa-se datasets curados onde se sabe qual o output esperado ou o comportamento correto, e depois executa o agente nesses dados.

Por exemplo, se construiu um agente para resolver problemas matemáticos em texto, pode ter um [dataset de teste](https://huggingface.co/datasets/gsm8k) com 100 problemas de respostas conhecidas. A avaliação offline é geralmente feita durante o desenvolvimento (e pode fazer parte das pipelines de CI/CD) para verificar melhorias ou prevenir regressões. A vantagem é que é **repetível e permite obter métricas claras de precisão dado que tem a verdade fundamental**. Pode também simular queries de utilizadores e medir as respostas do agente contra respostas ideais ou usar métricas automáticas conforme descrito acima.

O principal desafio da avaliação offline é garantir que o dataset de teste é abrangente e mantém-se relevante – o agente pode desempenhar bem num conjunto fixo mas encontrar queries muito diferentes em produção. Portanto, deve manter os conjuntos de teste atualizados com novos casos limite e exemplos que refletem cenários do mundo real. Uma mistura de pequenos casos para “teste rápido” e conjuntos maiores para métricas de desempenho mais amplas é útil: conjuntos pequenos para verificações rápidas e conjuntos grandes para métricas abrangentes.

### Avaliação Online

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Refere-se a avaliar o agente num ambiente ao vivo e real, ou seja, durante o uso efetivo em produção. A avaliação online envolve monitorizar o desempenho do agente em interações reais dos utilizadores e analisar os resultados de forma contínua.

Por exemplo, pode acompanhar taxas de sucesso, pontuações de satisfação do utilizador ou outras métricas no tráfego ao vivo. A vantagem da avaliação online é que **capta aspetos que talvez não consiga antecipar num ambiente de laboratório** – pode observar deriva do modelo ao longo do tempo (se a eficácia do agente degrada conforme os padrões de input mudam) e detectar queries ou situações inesperadas que não estavam nos dados de teste. Dá uma visão verdadeira de como o agente se comporta na realidade.

A avaliação online frequentemente envolve recolha de feedback implícito e explícito do utilizador, conforme discutido, e possivelmente a realização de testes shadow ou testes A/B (onde uma nova versão do agente corre em paralelo para comparação com a antiga). O desafio é que pode ser difícil obter etiquetas ou pontuações fiáveis para interações ao vivo – pode depender do feedback do utilizador ou métricas secundárias (como se o utilizador clicou no resultado).

### Combinando os dois

Avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Insights da monitorização online (ex.: novos tipos de queries onde o agente apresenta baixo desempenho) podem ser usados para aumentar e melhorar os datasets de teste offline. Por outro lado, agentes que apresentam bons resultados nos testes offline podem ser colocados em produção com maior confiança e monitorizados online.

De facto, muitas equipas adotam um ciclo: 

_avaliação offline -> deploy -> monitorização online -> recolha de novos casos de falha -> adição ao dataset offline -> refinamento do agente -> repetir_.

## Problemas Comuns

Ao colocar agentes de IA em produção, pode encontrar vários desafios. Aqui estão alguns problemas comuns e as suas potenciais soluções:

| **Problema**    | **Potencial Solução**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas de forma consistente | - Refinar o prompt dado ao Agente de IA; ser claro nos objetivos.<br>- Identificar onde dividir as tarefas em subtarefas e distribuí-las por múltiplos agentes pode ajudar. |
| Agente de IA entra em ciclos contínuos  | - Garantir termos e condições claras de terminação para que o Agente saiba quando parar o processo.<br>- Para tarefas complexas que requerem raciocínio e planeamento, usar um modelo maior especializado em raciocínio. |
| Chamadas a ferramentas do agente de IA com desempenho insatisfatório   | - Testar e validar a saída da ferramenta fora do sistema do agente.<br>- Refinar parâmetros definidos, prompts e a nomenclatura das ferramentas.  |
| Sistema Multi-Agente com desempenho inconsistente | - Refinar prompts dados a cada agente para garantir que são específicos e distintos entre si.<br>- Construir um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

Muitos destes problemas podem ser identificados de forma mais eficaz com a observabilidade implementada. Os traces e métricas discutidos anteriormente ajudam a identificar exatamente onde no fluxo do agente ocorrem problemas, tornando a depuração e otimização muito mais eficientes.

## Gestão de Custos
Aqui estão algumas estratégias para gerir os custos de implementação de agentes de IA em produção:

**Usar Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentivos e irão reduzir os custos significativamente. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor forma de entender quão bem um SLM irá funcionar no seu caso de uso. Considere usar SLMs para tarefas mais simples, como classificação de intenção ou extração de parâmetros, reservando os modelos maiores para raciocínio complexo.

**Usar um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Pode usar um LLM/SLM ou função serverless para encaminhar pedidos com base na complexidade para os modelos mais adequados. Isto também ajudará a reduzir custos garantindo o desempenho nas tarefas certas. Por exemplo, direcione consultas simples para modelos menores e mais rápidos, e utilize modelos grandes e dispendiosos apenas para tarefas de raciocínio complexo.

**Armazenar Respostas em Cache:** Identificar pedidos e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agentivo é uma boa forma de reduzir o volume de pedidos semelhantes. Pode até implementar um fluxo para identificar quão semelhante é um pedido em relação aos seus pedidos armazenados em cache usando modelos de IA mais básicos. Esta estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isto funciona na prática

No [notebook de exemplo desta secção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorizar e avaliar o nosso agente.

### Tem Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Discord do Microsoft Foundry](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar em horas de expediente e obter respostas às suas perguntas sobre Agentes de IA.

## Aula Anterior

[Metacognition Design Pattern](../09-metacognition/README.md)

## Aula Seguinte

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deverá ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional por um ser humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->