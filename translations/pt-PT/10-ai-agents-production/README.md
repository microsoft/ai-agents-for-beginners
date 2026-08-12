# Agentes de IA em Produção: Observabilidade & Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-PT/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, a capacidade de compreender o seu comportamento, monitorizar o seu desempenho e avaliar sistematicamente os seus resultados torna-se importante.

## Objetivos de Aprendizagem

Após completar esta lição, saberá como/compreenderá:
- Conceitos principais da observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar os seus agentes de IA sistematicamente
- Como controlar custos ao implementar agentes de IA em produção
- Como instrumentar agentes construídos com Microsoft Agent Framework

O objetivo é equipá-lo com o conhecimento para transformar os seus agentes "caixa preta" em sistemas transparentes, geríveis e confiáveis.

_**Nota:** É importante implementar Agentes de IA que sejam seguros e confiáveis. Consulte também a lição [Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)._

## Traces e Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) normalmente representem execuções de agentes como traces e spans.

- **Trace** representa uma tarefa completa do agente do início ao fim (como tratar uma questão de um utilizador).
- **Spans** são passos individuais dentro do trace (como chamar um modelo de linguagem ou recuperar dados).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa preta" - o seu estado interno e raciocínio são opacos, tornando-se difícil diagnosticar problemas ou otimizar o desempenho. Com observabilidade, os agentes tornam-se "caixas de vidro", oferecendo transparência que é vital para construir confiança e garantir que operam conforme o esperado. 

## Porque a Observabilidade é Importante em Ambientes de Produção

Passar agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. A observabilidade deixa de ser apenas um "desejável" para uma capacidade crítica:

*   **Depuração e Análise da Causa-Raiz**: Quando um agente falha ou produz uma saída inesperada, as ferramentas de observabilidade fornecem os traces necessários para identificar a origem do erro. Isto é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLMs, interações com ferramentas e lógica condicional.
*   **Gestão de Latência e Custos**: Agentes de IA frequentemente dependem de LLMs e outras APIs externas que são faturadas por token ou por chamada. A observabilidade permite um rastreio preciso destas chamadas, ajudando a identificar operações excessivamente lentas ou caras. Isto permite às equipas otimizar prompts, selecionar modelos mais eficientes ou redesenhar fluxos de trabalho para gerir custos operacionais e garantir uma boa experiência de utilizador.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportam de forma segura e ética. A observabilidade fornece uma trilha de auditoria das ações e decisões do agente. Isto pode ser usado para detectar e mitigar questões como injeção de prompt, geração de conteúdos nocivos ou o tratamento inadequado de informação pessoal identificável (PII). Por exemplo, pode rever traces para compreender por que razão um agente forneceu certa resposta ou utilizou uma ferramenta específica.
*   **Ciclos Contínuos de Melhoria**: Os dados de observabilidade são a base de um processo iterativo de desenvolvimento. Ao monitorizar como os agentes desempenham no mundo real, as equipas podem identificar áreas para melhoria, recolher dados para ajuste de modelos e validar o impacto das alterações. Isto cria um ciclo de feedback onde as percepções de produção da avaliação online informam experimentações e refinamentos offline, levando a um desempenho progressivamente melhor dos agentes.

## Métricas Principais a Rastrear

Para monitorizar e entender o comportamento dos agentes, uma variedade de métricas e sinais deve ser monitorizada. Embora as métricas específicas possam variar consoante o propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitorizam:

**Latência:** Com que rapidez responde o agente? Tempos de espera longos impactam negativamente a experiência do utilizador. Deve medir latência para tarefas e passos individuais rastreando execuções do agente. Por exemplo, um agente que demora 20 segundos para todas as chamadas ao modelo pode ser acelerado usando um modelo mais rápido ou executando chamadas ao modelo em paralelo.

**Custos:** Qual é a despesa por execução do agente? Agentes de IA dependem de chamadas a LLM faturadas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes para melhorar marginalmente a qualidade, deve avaliar se o custo é justificado ou se pode reduzir o número de chamadas ou usar um modelo mais barato. O monitoramento em tempo real também ajuda a identificar picos inesperados (ex. bugs causando loops excessivos na API).

**Erros de Pedido:** Quantos pedidos falhou o agente? Isto pode incluir erros de API ou falhas em chamadas a ferramentas. Para tornar seu agente mais robusto contra estes problemas em produção, pode configurar fallback ou repetições. Ex.: Se o fornecedor LLM A estiver indisponível, alterna para o fornecedor LLM B como backup.

**Feedback do Utilizador:** Implementar avaliações diretas dos utilizadores fornece perceções valiosas. Isto pode incluir classificações explícitas (👍gosto/👎não gosto, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alerta-lo, pois é sinal que o agente não está a funcionar como esperado. 

**Feedback Implícito do Utilizador:** Os comportamentos dos utilizadores fornecem feedback indireto mesmo sem classificações explícitas. Isto pode incluir reformulação imediata da pergunta, consultas repetidas ou clicar no botão de tentar novamente. Ex.: Se vir que os utilizadores perguntam repetidamente a mesma questão, é sinal que o agente não está a funcionar como esperado.

**Precisão:** Com que frequência o agente produz saídas corretas ou desejáveis? A definição de precisão varia (ex.: exactidão na resolução de problemas, precisão na recuperação de informação, satisfação do utilizador). O primeiro passo é definir como o sucesso se apresenta para o seu agente. Pode monitorizar a precisão por verificações automatizadas, pontuações de avaliação ou etiquetas de conclusão de tarefas. Por exemplo, marcar traces como "sucedido" ou "falhado". 

**Métricas de Avaliação Automatizada:** Também pode configurar avaliações automáticas. Por exemplo, pode usar um LLM para pontuar a saída do agente, ex.: se é útil, precisa ou não. Há várias bibliotecas de código aberto que ajudam a pontuar diferentes aspetos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detetar linguagem nociva ou injeção de prompt. 

Na prática, uma combinação destas métricas oferece a melhor cobertura da saúde de um agente de IA. No [exemplo de notebook](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostramos como estas métricas se apresentam em exemplos reais, mas antes, vamos aprender como é um fluxo típico de avaliação.

## Instrumentar o Seu Agente

Para recolher dados de tracing, precisará de instrumentar o seu código. O objetivo é instrumentar o código do agente para emitir traces e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) tornou-se o padrão industrial para observabilidade de LLM. Fornece um conjunto de APIs, SDKs e ferramentas para gerar, recolher e exportar dados de telemetria. 

Existem muitas bibliotecas de instrumentação que encapsulam frameworks de agentes existentes e facilitam a exportação de spans OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Segue um exemplo de como instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é rastreada automaticamente
    pass
```

O [exemplo de notebook](./code_samples/10-expense_claim-demo.ipynb) neste capítulo demonstrará como instrumentar o seu agente MAF.

**Criação Manual de Spans:** Embora as bibliotecas de instrumentação forneçam uma boa base, frequentemente há casos onde se precisa de informação mais detalhada ou personalizada. Pode criar spans manualmente para adicionar lógica específica da aplicação. Mais importante ainda, podem enriquecer spans criados automática ou manualmente com atributos personalizados (também conhecidos como tags ou metadados). Estes atributos podem incluir dados específicos do negócio, cálculos intermédios ou qualquer contexto útil para depuração ou análise, tais como `user_id`, `session_id` ou `model_version`.

Exemplo de criação manual de traces e spans com o [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

Observabilidade dá-nos métricas, mas a avaliação é o processo de analisar esses dados (e realizar testes) para determinar quão bem um agente de IA está a funcionar e como pode ser melhorado. Por outras palavras, uma vez que tem esses traces e métricas, como as usa para julgar o agente e tomar decisões? 

A avaliação regular é importante porque agentes de IA são frequentemente não determinísticos e podem evoluir (através de atualizações ou alteração do comportamento do modelo) – sem avaliação, não saberia se o seu “agente inteligente” está realmente a fazer o seu trabalho bem ou se regrediu.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e complementam-se mutuamente. Geralmente começamos com avaliação offline, pois este é o passo mínimo necessário antes de implementar qualquer agente.

### Avaliação Offline

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isto envolve avaliar o agente num ambiente controlado, tipicamente usando conjuntos de dados de teste, não consultas de utilizadores reais. Usa conjuntos de dados selecionados onde sabe qual é a saída esperada ou comportamento correto, e depois executa o seu agente sobre esses dados. 

Por exemplo, se construiu um agente de resolução de problemas matemáticos, pode ter um [conjunto de teste](https://huggingface.co/datasets/gsm8k) de 100 problemas com respostas conhecidas. A avaliação offline é frequentemente feita durante o desenvolvimento (e pode fazer parte de pipelines CI/CD) para verificar melhorias ou evitar regressões. A vantagem é que é **repetível e pode obter métricas claras de precisão pois tem truth de referência**. Pode também simular consultas de utilizadores e medir as respostas do agente em comparação com respostas ideais ou usar métricas automatizadas como descrito acima. 

O desafio principal da avaliação offline é garantir que o conjunto de dados de teste é abrangente e se mantém relevante – o agente pode performar bem num conjunto de testes fixo, mas encontrar consultas muito diferentes em produção. Portanto deve manter os conjuntos de teste atualizados com novos casos limite e exemplos que reflitam cenários do mundo real​. Uma mistura de conjuntos pequenos para testes rápidos e conjuntos maiores para métricas mais amplas é útil: conjuntos pequenos para verificações rápidas e maiores para métricas mais abrangentes​.

### Avaliação Online 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Isto refere-se à avaliação do agente num ambiente ao vivo e real, ou seja, durante utilização efetiva em produção. Avaliação online envolve monitorizar o desempenho do agente em interações reais com utilizadores e analisar continuamente os resultados. 

Por exemplo, pode acompanhar taxas de sucesso, pontuações de satisfação do utilizador ou outras métricas sobre tráfego real. A vantagem da avaliação online é que **captura aspectos que poderá não antecipar num ambiente de laboratório** – pode observar a deriva do modelo ao longo do tempo (se a eficácia do agente degradar conforme padrões de input mudam) e detectar consultas ou situações inesperadas que não estavam nos dados de teste​. Dá uma visão real de como o agente se comporta no campo. 

A avaliação online envolve frequentemente recolher feedback implícito e explícito dos utilizadores, conforme discutido, e possivelmente executar testes shadow ou testes A/B (onde uma nova versão do agente corre em paralelo para comparar com a antiga). O desafio é conseguir etiquetas ou pontuações fiáveis para interações ao vivo – poderá depender de feedback do utilizador ou métricas posteriores (ex.: se o utilizador clicou no resultado). 

### Combinando os dois

As avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Perceções da monitorização online (ex.: novos tipos de consultas onde o agente tem baixo desempenho) podem ser usadas para melhorar conjuntos de dados de teste offline. Por outro lado, agentes que performam bem em testes offline podem ser mais seguramente implementados e monitorizados online. 

Na verdade, muitas equipas adotam um ciclo: 

_avaliar offline -> implementar -> monitorizar online -> recolher novos casos de falha -> acrescentar ao conjunto offline -> refinar agente -> repetir_.

## Problemas Comuns

Ao implementar agentes de IA em produção, poderá enfrentar vários desafios. Aqui estão alguns problemas comuns e as suas possíveis soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas consistentemente | - Refinar o prompt dado ao agente de IA; ser claro nos objetivos.<br>- Identificar onde dividir tarefas em subtarefas e tratá-las com múltiplos agentes pode ajudar. |
| Agente de IA entra em loops contínuos  | - Garantir termos e condições claros de terminação para que o agente saiba quando parar o processo.<br>- Para tarefas complexas que requerem raciocínio e planeamento, usar um modelo maior especializado em tarefas de raciocínio. |
| Chamadas a ferramentas do agente de IA não estão a funcionar bem   | - Testar e validar a saída da ferramenta fora do sistema do agente.<br>- Refinar os parâmetros definidos, prompts, e nomeação das ferramentas.  |
| Sistema Multi-Agente não performa consistentemente | - Refinar os prompts dados a cada agente para garantir que sejam específicos e distintos uns dos outros.<br>- Construir um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

Muitos destes problemas podem ser identificados mais eficazmente com a observabilidade implementada. Os traces e métricas que discutimos anteriormente ajudam a identificar exatamente onde ocorrem os problemas no fluxo de trabalho do agente, tornando a depuração e otimização muito mais eficientes.

## Gestão de Custos


Aqui estão algumas estratégias para gerir os custos de implantação de agentes de IA em produção:

**Utilizar Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem ter um desempenho eficaz em certos casos de uso agentic e reduzirão significativamente os custos. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor forma de entender quão bem um SLM irá desempenhar no seu caso de uso. Considere usar SLMs para tarefas mais simples como classificação de intenção ou extração de parâmetros, reservando modelos maiores para raciocínio complexo.

**Utilizar um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Pode usar um LLM/SLM ou uma função serverless para encaminhar pedidos com base na complexidade para os modelos mais adequados. Isto também ajudará a reduzir custos, garantindo desempenho nas tarefas certas. Por exemplo, encaminhe consultas simples para modelos mais pequenos e rápidos, e use modelos grandes e caros apenas para tarefas de raciocínio complexo.

**Guardar em Cache as Respostas:** Identificar pedidos e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agentic é uma boa forma de reduzir o volume de pedidos similares. Pode até implementar um fluxo para identificar quão semelhante um pedido é em relação aos seus pedidos guardados em cache usando modelos de IA mais básicos. Esta estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isto funciona na prática

No [notebook de exemplo desta secção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorizar e avaliar o nosso agente.


### Tem Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar em horas de expediente e obter respostas para as suas perguntas sobre Agentes de IA.

## Lição Anterior

[Padrão de Desenho Metacognição](../09-metacognition/README.md)

## Próxima Lição

[Protocolos Agentic](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->