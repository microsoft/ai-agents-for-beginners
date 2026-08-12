# Agentes de IA em Produção: Observabilidade e Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-BR/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, torna-se importante a capacidade de entender seu comportamento, monitorar seu desempenho e avaliar sistematicamente seus resultados.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá/compreenderá:
- Conceitos fundamentais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar seus agentes de IA sistematicamente
- Como controlar custos ao implantar agentes de IA em produção
- Como instrumentar agentes construídos com o Microsoft Agent Framework

O objetivo é equipá-lo com o conhecimento para transformar seus agentes "caixa-preta" em sistemas transparentes, gerenciáveis e confiáveis.

_**Nota:** É importante implantar Agentes de IA que sejam seguros e confiáveis. Confira também a lição [Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)._

## Rastreamentos e Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como rastreamentos e spans.

- **Rastreamento (Trace)** representa uma tarefa completa do agente do início ao fim (como lidar com uma consulta do usuário).
- **Spans** são passos individuais dentro do rastreamento (como chamar um modelo de linguagem ou recuperar dados).

![Árvore de rastreamento no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sem observabilidade, um agente de IA pode parecer uma "caixa-preta" - seu estado interno e raciocínio são opacos, dificultando o diagnóstico de problemas ou a otimização do desempenho. Com observabilidade, agentes se tornam "caixas de vidro", oferecendo transparência vital para construir confiança e garantir que operem conforme o esperado.

## Por Que a Observabilidade é Importante em Ambientes de Produção

A transição dos agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. A observabilidade não é mais um "item desejável", mas uma capacidade crítica:

*   **Depuração e Análise de Causa Raiz**: Quando um agente falha ou produz um resultado inesperado, as ferramentas de observabilidade fornecem os rastreamentos necessários para identificar a origem do erro. Isso é especialmente importante em agentes complexos, que podem envolver múltiplas chamadas a LLM, interações com ferramentas e lógica condicional.
*   **Gerenciamento de Latência e Custos**: Agentes de IA frequentemente dependem de LLMs e outras APIs externas que são cobradas por token ou chamada. A observabilidade permite o acompanhamento preciso dessas chamadas, ajudando a identificar operações excessivamente lentas ou caras. Isso permite que as equipes otimizem prompts, selecionem modelos mais eficientes ou redesenhem fluxos de trabalho para controlar custos operacionais e garantir boa experiência do usuário.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante garantir que os agentes se comportem de forma segura e ética. A observabilidade fornece um registro de auditoria das ações e decisões do agente. Isso pode ser usado para detectar e mitigar problemas como injeção de prompt, geração de conteúdo prejudicial ou o manuseio incorreto de informações pessoalmente identificáveis (PII). Por exemplo, você pode revisar rastreamentos para entender por que um agente forneceu uma determinada resposta ou usou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Dados de observabilidade são a base de um processo iterativo de desenvolvimento. Ao monitorar o desempenho dos agentes no mundo real, as equipes podem identificar áreas para melhorias, coletar dados para ajuste fino dos modelos e validar o impacto das mudanças. Isso cria um ciclo de feedback onde insights da produção a partir da avaliação online informam experimentação e refinamento offline, levando a um desempenho progressivamente melhor dos agentes.

## Métricas-Chave para Acompanhar

Para monitorar e entender o comportamento do agente, uma variedade de métricas e sinais deve ser acompanhada. Embora as métricas específicas possam variar conforme o propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que ferramentas de observabilidade monitoram:

**Latência:** Quão rápido o agente responde? Tempos longos de espera impactam negativamente a experiência do usuário. Você deve medir a latência para tarefas e passos individuais rastreando execuções do agente. Por exemplo, um agente que leva 20 segundos para todas as chamadas de modelo poderia ser acelerado usando um modelo mais rápido ou executando chamadas em paralelo.

**Custos:** Qual é o custo por execução do agente? Agentes de IA dependem de chamadas a LLM cobradas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar custos rapidamente. Por exemplo, se um agente chama uma LLM cinco vezes para melhoria marginal da qualidade, você deve avaliar se o custo é justificado ou se poderia reduzir o número de chamadas ou usar um modelo mais barato. Monitoramento em tempo real também pode ajudar a identificar picos inesperados (ex.: bugs que causam loops excessivos da API).

**Erros de Solicitação:** Quantas solicitações o agente falhou? Isso pode incluir erros de API ou falhas em chamadas de ferramenta. Para tornar seu agente mais robusto contra isso em produção, você pode configurar fallback ou tentativas. Ex.: se o provedor LLM A estiver fora do ar, você alterna para o provedor LLM B como backup.

**Feedback do Usuário:** Implementar avaliações diretas dos usuários fornece insights valiosos. Isso pode incluir classificações explícitas (👍positivo/👎negativo, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois indica que o agente não está funcionando conforme esperado.

**Feedback Implícito do Usuário:** Comportamentos do usuário fornecem feedback indireto mesmo sem classificações explícitas. Isso pode incluir reformulação imediata de perguntas, consultas repetidas ou clicar em um botão de tentar novamente. Ex.: se você perceber que usuários fazem a mesma pergunta repetidamente, isso indica que o agente não está funcionando como esperado.

**Precisão:** Com que frequência o agente produz saídas corretas ou desejáveis? Definições de precisão variam (ex.: exatidão na resolução de problemas, precisão na recuperação de informações, satisfação do usuário). O primeiro passo é definir o que significa sucesso para seu agente. Você pode acompanhar a precisão por meio de verificações automatizadas, pontuações de avaliação ou rótulos de conclusão de tarefas. Por exemplo, marcar rastreamentos como "bem-sucedidos" ou "falhos".

**Métricas de Avaliação Automatizada:** Você também pode configurar avaliações automáticas. Por exemplo, usar uma LLM para pontuar o resultado do agente, avaliando se ele é útil, preciso ou não. Existem várias bibliotecas de código aberto que ajudam a pontuar diferentes aspectos do agente, como [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://llm-guard.com/) para detectar linguagem nociva ou injeção de prompt.

Na prática, uma combinação dessas métricas oferece a melhor cobertura da saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como essas métricas aparecem em exemplos reais, mas primeiro, aprenderemos como é o fluxo típico de avaliação.

## Instrumente seu Agente

Para coletar dados de rastreamento, você precisará instrumentar seu código. O objetivo é instrumentar o código do agente para emitir rastreamentos e métricas que possam ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) surgiu como um padrão da indústria para observabilidade de LLMs. Fornece um conjunto de APIs, SDKs e ferramentas para gerar, coletar e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks existentes de agentes e facilitam a exportação de spans do OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com OpenTelemetry. Abaixo há um exemplo de como instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # A execução do agente é rastreada automaticamente
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) neste capítulo demonstrará como instrumentar seu agente MAF.

**Criação Manual de Spans:** Embora as bibliotecas de instrumentação forneçam uma boa base, frequentemente há casos onde são necessárias informações mais detalhadas ou personalizadas. Você pode criar spans manualmente para adicionar lógica personalizada da aplicação. Mais importante, eles podem enriquecer spans criados automaticamente ou manualmente com atributos personalizados (também conhecidos como tags ou metadados). Esses atributos podem incluir dados específicos do negócio, cálculos intermediários ou qualquer contexto útil para depuração ou análise, como `user_id`, `session_id` ou `model_version`.

Exemplo de criação manual de rastreamentos e spans com o [SDK Python do Langfuse](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação do Agente

Observabilidade nos fornece métricas, mas avaliação é o processo de analisar esses dados (e realizar testes) para determinar o quão bem um agente de IA está performando e como ele pode ser melhorado. Em outras palavras, uma vez que você tem esses rastreamentos e métricas, como usá-los para julgar o agente e tomar decisões?

A avaliação regular é importante porque agentes de IA são frequentemente não determinísticos e podem evoluir (através de atualizações ou mudanças no comportamento do modelo) – sem avaliação, você não saberia se seu “agente inteligente” está realmente fazendo seu trabalho bem ou se regrediu.

Existem duas categorias de avaliação para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas, e se complementam. Geralmente começamos pela avaliação offline, pois é o passo mínimo necessário antes de implantar qualquer agente.

### Avaliação Offline

![Itens do dataset no Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isso envolve avaliar o agente em um ambiente controlado, tipicamente usando conjuntos de dados de teste, não consultas de usuários ao vivo. Você usa datasets curados nos quais sabe qual é a saída esperada ou comportamento correto, e então executa seu agente sobre eles.

Por exemplo, se você construiu um agente para resolver problemas matemáticos em linguagem natural, poderia ter um [dataset de teste](https://huggingface.co/datasets/gsm8k) com 100 problemas com respostas conhecidas. A avaliação offline é frequentemente feita durante o desenvolvimento (e pode fazer parte de pipelines de CI/CD) para checar melhorias ou evitar regressões. A vantagem é que é **repetível e você pode obter métricas claras de precisão, pois tem a verdade de base**. Você também pode simular consultas de usuários e medir as respostas do agente contra respostas ideais, ou usar métricas automatizadas como descrito acima.

O principal desafio da avaliação offline é garantir que seu dataset de teste seja abrangente e continue relevante – o agente pode performar bem em um conjunto de teste fixo, mas encontrar consultas muito diferentes em produção. Portanto, você deve manter os conjuntos de teste atualizados com novos casos extremos e exemplos que reflitam cenários reais. Uma mistura de pequenos casos de “teste rápido” e conjuntos maiores para avaliação é útil: pequenos conjuntos para verificações rápidas e maiores para métricas mais amplas de desempenho.

### Avaliação Online

![Visão geral de métricas de observabilidade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Isso se refere a avaliar o agente em um ambiente ao vivo, no mundo real, ou seja, durante o uso real em produção. A avaliação online envolve monitorar o desempenho do agente em interações reais de usuários e analisar os resultados continuamente.

Por exemplo, você pode acompanhar taxas de sucesso, pontuações de satisfação do usuário ou outras métricas sobre tráfego ao vivo. A vantagem da avaliação online é que ela **captura coisas que você talvez não antecipe em um ambiente de laboratório** – você pode observar deriva do modelo ao longo do tempo (se a eficácia do agente degrada conforme mudam os padrões de entrada) e detectar consultas ou situações inesperadas que não estavam nos seus dados de teste. Ela fornece um panorama verdadeiro de como o agente se comporta no mundo real.

Avaliação online muitas vezes envolve coletar feedback implícito e explícito do usuário, como discutido, e possivelmente executar testes sombra ou testes A/B (onde uma nova versão do agente roda em paralelo para comparar com a antiga). O desafio é que pode ser complicado obter rótulos ou pontuações confiáveis para interações ao vivo – você pode depender de feedback do usuário ou métricas subsequentes (como se o usuário clicou no resultado).

### Combinando os dois

Avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Insights do monitoramento online (ex.: novos tipos de consultas onde o agente performa mal) podem ser usados para incrementar e melhorar os datasets de teste offline. Por outro lado, agentes que performam bem em testes offline podem ser implantados e monitorados online com maior confiança.

De fato, muitas equipes adotam um ciclo:

_avaliar offline -> implantar -> monitorar online -> coletar novos casos de falha -> adicionar ao dataset offline -> refinar agente -> repetir_.

## Problemas Comuns

Ao implantar agentes de IA em produção, você pode encontrar vários desafios. Aqui estão alguns problemas comuns e suas possíveis soluções:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não executa tarefas consistentemente | - Refinar o prompt dado ao agente; ser claro nos objetivos.<br>- Identificar onde dividir tarefas em subtarefas e lidar com elas por múltiplos agentes pode ajudar. |
| Agente de IA entra em loops contínuos  | - Garantir termos e condições claros de encerramento para que o agente saiba quando parar o processo.<br>- Para tarefas complexas que exigem raciocínio e planejamento, usar um modelo maior especializado para tarefas de raciocínio. |
| Chamadas de ferramentas do agente de IA não funcionam bem   | - Testar e validar a saída da ferramenta fora do sistema do agente.<br>- Refinar parâmetros definidos, prompts e nomes das ferramentas.  |
| Sistema Multi-Agente não performa consistentemente | - Refinar prompts dados a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construir um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

Muitos desses problemas podem ser identificados com mais eficácia se houver observabilidade implementada. Os rastreamentos e métricas que discutimos ajudam a identificar precisamente onde, no fluxo do agente, os problemas ocorrem, tornando depuração e otimização muito mais eficientes.

## Gerenciamento de Custos


Aqui estão algumas estratégias para gerenciar os custos de implantação de agentes de IA em produção:

**Usando Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentes e reduzirão os custos significativamente. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor maneira de entender o quão bem um SLM se sairá no seu caso de uso. Considere usar SLMs para tarefas mais simples, como classificação de intenção ou extração de parâmetros, enquanto reserva modelos maiores para raciocínios complexos.

**Usando um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou função serverless para direcionar solicitações com base na complexidade para os modelos mais adequados. Isso também ajudará a reduzir custos enquanto garante o desempenho nas tarefas certas. Por exemplo, encaminhe consultas simples para modelos menores e mais rápidos, e use modelos grandes e caros apenas para tarefas de raciocínio complexo.

**Cacheando Respostas:** Identificar solicitações e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agente é uma boa maneira de reduzir o volume de solicitações semelhantes. Você pode até implementar um fluxo para identificar o quão semelhante uma solicitação é às suas solicitações em cache usando modelos de IA mais básicos. Essa estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isso funciona na prática

No [notebook de exemplo desta seção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como usar ferramentas de observabilidade para monitorar e avaliar nosso agente.


### Tem Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de atendimento e obter respostas para suas perguntas sobre Agentes de IA.

## Aula Anterior

[Padrão de Design Metacognição](../09-metacognition/README.md)

## Próxima Aula

[Protocolos Autônomos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->