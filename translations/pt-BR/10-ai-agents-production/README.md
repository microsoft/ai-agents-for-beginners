# Agentes de IA em Produção: Observabilidade & Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-BR/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, a capacidade de entender seu comportamento, monitorar seu desempenho e avaliar sistematicamente seus resultados torna-se importante.

## Objetivos de aprendizado

Após completar esta lição, você saberá/entenderá:
- Conceitos básicos de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar sistematicamente seus agentes de IA
- Como controlar custos ao implantar agentes de IA em produção
- Como instrumentar agentes construídos com Microsoft Agent Framework

O objetivo é equipá-lo com o conhecimento para transformar seus agentes "caixa-preta" em sistemas transparentes, gerenciáveis e confiáveis.

_**Nota:** É importante implantar Agentes de IA que sejam seguros e confiáveis. Confira também a lição [Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)._

## Rastros e Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) normalmente representam execuções de agentes como rastros e spans.

- **Rastro (Trace)** representa uma tarefa completa do agente do começo ao fim (como lidar com uma consulta do usuário).
- **Spans** são etapas individuais dentro do rastro (como chamar um modelo de linguagem ou recuperar dados).

![Árvore de rastros no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa-preta" - seu estado interno e raciocínio são opacos, dificultando diagnosticar problemas ou otimizar o desempenho. Com observabilidade, os agentes se tornam "caixas de vidro", oferecendo transparência que é vital para construir confiança e garantir que operem conforme o esperado.

## Por que a Observabilidade Importa em Ambientes de Produção

A transição de agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requerimentos. A observabilidade não é mais algo "bom de ter", mas uma capacidade crítica:

*   **Depuração e Análise de Causa Raiz**: Quando um agente falha ou produz uma saída inesperada, ferramentas de observabilidade fornecem os rastros necessários para identificar a fonte do erro. Isso é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLMs, interações com ferramentas e lógica condicional.
*   **Gerenciamento de Latência e Custo**: Agentes de IA frequentemente dependem de LLMs e outras APIs externas que são cobradas por token ou por chamada. A observabilidade permite o monitoramento preciso dessas chamadas, ajudando a identificar operações excessivamente lentas ou caras. Isso permite otimizar prompts, selecionar modelos mais eficientes ou redesenhar fluxos de trabalho para gerenciar custos operacionais e garantir uma boa experiência ao usuário.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportem de forma segura e ética. A observabilidade fornece um rastro de auditoria das ações e decisões do agente. Isso pode ser usado para detectar e mitigar problemas como injeção de prompt, geração de conteúdo prejudicial ou manuseio inadequado de informações pessoais identificáveis (PII). Por exemplo, você pode revisar rastros para entender por que um agente forneceu uma certa resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Dados de observabilidade são a base de um processo iterativo de desenvolvimento. Monitorando como os agentes performam no mundo real, as equipes podem identificar áreas para melhorias, coletar dados para ajuste fino dos modelos e validar o impacto das mudanças. Isso cria um ciclo de feedback onde insights de produção da avaliação online informam experimentação e refinamento offline, levando a um desempenho progressivamente melhor dos agentes.

## Métricas-chave para Monitorar

Para monitorar e entender o comportamento do agente, deve-se acompanhar uma variedade de métricas e sinais. Embora as métricas específicas possam variar com base no propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitoram:

**Latência:** Quão rápido o agente responde? Tempos longos de espera impactam negativamente a experiência do usuário. Você deve medir latência para tarefas e etapas individuais rastreando execuções do agente. Por exemplo, um agente que demora 20 segundos para todas as chamadas de modelo poderia ser acelerado usando um modelo mais rápido ou executando as chamadas em paralelo.

**Custos:** Qual o custo por execução do agente? Agentes de IA dependem de chamadas a LLM cobradas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes para uma melhoria marginal na qualidade, você deve avaliar se o custo é justificado ou se poderia reduzir o número de chamadas ou usar um modelo mais barato. Monitoramento em tempo real pode também ajudar a identificar picos inesperados (ex.: bugs causando loops excessivos de API).

**Erros nas Solicitações:** Quantas solicitações o agente falhou? Isso pode incluir erros de API ou chamadas de ferramenta falhadas. Para tornar seu agente mais robusto contra isso em produção, você pode configurar alternativas ou tentativas repetidas. Ex.: se o provedor de LLM A está fora do ar, você alterna para o provedor B como backup.

**Feedback do Usuário:** Implementar avaliações diretas dos usuários oferece insights valiosos. Isso pode incluir classificações explícitas (👍curtir/👎não curtir, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo pois é sinal que o agente não está funcionando como esperado.

**Feedback Implícito do Usuário:** O comportamento do usuário fornece feedback indireto mesmo sem classificações explícitas. Isso pode incluir reformulação imediata da pergunta, consultas repetidas ou clicar no botão de tentar novamente. Ex.: se usuários fazem repetidamente a mesma pergunta, é sinal que o agente não está funcionando como esperado.

**Precisão:** Com que frequência o agente produz resultados corretos ou desejáveis? Definições de precisão variam (ex.: correção na resolução de problemas, precisão em recuperação de informação, satisfação do usuário). O primeiro passo é definir como sucesso se parece para seu agente. Você pode acompanhar precisão via checagens automatizadas, pontuações de avaliação ou etiquetas de conclusão de tarefa. Por exemplo, marcar rastros como "bem-sucedido" ou "falhado".

**Métricas de Avaliação Automatizada:** Você também pode configurar avaliações automáticas. Por exemplo, pode usar um LLM para pontuar a saída do agente, ex.: se é útil, precisa ou não. Há também várias bibliotecas open source que ajudam a pontuar diferentes aspectos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://github.com/protectai/llm-guard) para detectar linguagem prejudicial ou injeção de prompt.

Na prática, uma combinação dessas métricas oferece a melhor cobertura da saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como essas métricas aparecem em exemplos reais, mas primeiro, vamos aprender como é um fluxo típico de avaliação.

## Instrumente seu Agente

Para coletar dados de rastreamento, você precisará instrumentar seu código. O objetivo é instrumentar o código do agente para emitir rastros e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) emergiu como padrão da indústria para observabilidade de LLMs. Ele fornece um conjunto de APIs, SDKs e ferramentas para gerar, coletar e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que encapsulam frameworks de agentes existentes e facilitam exportar spans do OpenTelemetry para uma ferramenta de observabilidade. Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo está um exemplo de como instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo demonstrará como instrumentar seu agente MAF.

**Criação Manual de Span:** Embora bibliotecas de instrumentação forneçam uma boa base, frequentemente são necessários casos para informações mais detalhadas ou customizadas. Você pode criar spans manualmente para adicionar lógica personalizada da aplicação. Mais importante, eles podem enriquecer spans criados automática ou manualmente com atributos personalizados (também conhecidos como tags ou metadados). Esses atributos podem incluir dados específicos do negócio, cálculos intermediários ou qualquer contexto útil para depuração ou análise, como `user_id`, `session_id`, ou `model_version`.

Exemplo de criação manual de rastros e spans com o [SDK Langfuse Python](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

Observabilidade nos dá métricas, mas avaliação é o processo de analisar esses dados (e realizar testes) para determinar o quão bem um agente de IA está performando e como pode ser melhorado. Em outras palavras, uma vez que você tenha esses rastros e métricas, como usá-los para julgar o agente e tomar decisões?

Avaliações regulares são importantes porque agentes de IA frequentemente são não determinísticos e podem evoluir (através de atualizações ou comportamento de modelo em deriva) – sem avaliação, você não saberia se seu “agente inteligente” está realmente fazendo bem seu trabalho ou se houve regressão.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e se complementam. Normalmente começamos com avaliação offline, pois este é o passo mínimo necessário antes de implantar qualquer agente.

### Avaliação Offline

![Itens do conjunto de dados no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isso envolve avaliar o agente em um ambiente controlado, normalmente usando conjuntos de dados de teste, e não consultas de usuários ao vivo. Você usa conjuntos de dados curados onde sabe qual a saída esperada ou comportamento correto, e então executa seu agente sobre eles.

Por exemplo, se você construiu um agente para resolver problemas matemáticos em linguagem natural, pode ter um [conjunto de dados de teste](https://huggingface.co/datasets/openai/gsm8k) com 100 problemas com respostas conhecidas. Avaliação offline é feita muitas vezes durante o desenvolvimento (e pode fazer parte de pipelines de CI/CD) para checar melhorias ou evitar regressões. O benefício é que é **repetível e você obtém métricas claras de precisão pois tem a verdade fundamental**. Você pode também simular consultas de usuários e medir as respostas do agente frente a respostas ideais ou usar métricas automatizadas conforme descrito acima.

O principal desafio da avaliação offline é garantir que seu conjunto de dados de teste seja abrangente e continue relevante – o agente pode performar bem em conjunto fixo de testes, mas encontrar consultas muito diferentes em produção. Portanto, você deve manter conjuntos de teste atualizados com novos casos extremos e exemplos que reflitam cenários do mundo real. Uma mistura de pequenos casos de “teste rápido” e conjuntos maiores de avaliação é útil: pequenos conjuntos para verificações rápidas e conjuntos maiores para métricas de desempenho mais amplas.

### Avaliação Online

![Visão geral das métricas de observabilidade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Isso se refere a avaliar o agente em ambiente real, ao vivo, ou seja, durante uso real em produção. Avaliação online envolve monitorar o desempenho do agente em interações reais com usuários e analisar os resultados continuamente.

Por exemplo, você pode monitorar taxas de sucesso, pontuações de satisfação do usuário ou outras métricas no tráfego ao vivo. A vantagem da avaliação online é que ela **captura coisas que você talvez não antecipasse em ambiente de laboratório** – você pode observar deriva do modelo ao longo do tempo (se a eficácia do agente se degrada conforme padrões de entrada mudam) e identificar consultas ou situações inesperadas que não estavam nos dados de teste. Ela fornece um retrato real de como o agente se comporta no mundo real.

Avaliação online frequentemente envolve coletar feedback implícito e explícito dos usuários, conforme discutido, e possivelmente executar testes “shadow” ou testes A/B (onde uma nova versão do agente roda paralelamente para comparação com a antiga). O desafio é que pode ser difícil obter rótulos ou pontuações confiáveis para interações ao vivo – você pode depender de feedback do usuário ou métricas subsequentes (ex.: se o usuário clicou no resultado).

### Combinando os dois

Avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Insights do monitoramento online (ex.: novos tipos de consultas onde o agente performa mal) podem ser usados para complementar e melhorar os conjuntos de teste offline. Por outro lado, agentes que performam bem em testes offline podem ser implantados com mais confiança e monitorados online.

De fato, muitas equipes adotam um ciclo:

_avaliar offline -> implantar -> monitorar online -> coletar novos casos de falha -> adicionar ao conjunto offline -> refinar agente -> repetir_.

## Problemas Comuns

Ao implantar agentes de IA em produção, você pode encontrar vários desafios. Aqui estão alguns problemas comuns e suas potenciais soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas consistentemente | - Refine o prompt dado ao agente de IA; seja claro nos objetivos.<br>- Identifique onde dividir as tarefas em subtarefas e tratá-las com múltiplos agentes pode ajudar. |
| Agente de IA entrando em loops contínuos  | - Assegure termos e condições claros de término para que o agente saiba quando parar o processo.<br>- Para tarefas complexas que requerem raciocínio e planejamento, use um modelo maior especializado em raciocínio. |
| Chamadas de ferramentas do agente de IA não performando bem   | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e nomes das ferramentas.  |
| Sistema multiagente não performando de forma consistente | - Refine os prompts dados a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construa um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

Muitos desses problemas podem ser identificados de forma mais eficiente com observabilidade em uso. Os rastros e métricas que discutimos anteriormente ajudam a localizar exatamente onde no fluxo do agente ocorrem problemas, tornando a depuração e otimização muito mais eficientes.

## Gerenciando Custos

Aqui estão algumas estratégias para gerenciar os custos de implantação de agentes de IA em produção:

**Usando Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem desempenhar bem em certos casos de uso agênticos e reduzirão os custos significativamente. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor maneira de entender quão bem um SLM funcionará no seu caso de uso. Considere usar SLMs para tarefas mais simples, como classificação de intenção ou extração de parâmetros, enquanto reserva modelos maiores para raciocínios complexos.

**Usando um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou função serverless para direcionar solicitações com base na complexidade para os modelos mais adequados. Isso também ajudará a reduzir custos, garantindo desempenho nas tarefas certas. Por exemplo, direcione consultas simples para modelos menores e mais rápidos, e use modelos grandes caros apenas para tarefas de raciocínio complexo.

**Armazenando em Cache Respostas:** Identificar solicitações e tarefas comuns e fornecer as respostas antes que elas passem pelo seu sistema agêntico é uma boa maneira de reduzir o volume de solicitações semelhantes. Você pode até implementar um fluxo para identificar quão semelhante uma solicitação é às suas solicitações em cache usando modelos de IA mais básicos. Essa estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isso funciona na prática

No [notebook de exemplo desta seção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorar e avaliar nosso agente.


### Quer Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Lição Anterior

[Padrão de Design Metacognição](../09-metacognition/README.md)

## Próxima Lição

[Protocolos Agênticos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->