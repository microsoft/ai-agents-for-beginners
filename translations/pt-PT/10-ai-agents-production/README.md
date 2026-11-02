# Agentes de IA em Produção: Observabilidade & Avaliação

[![Agentes de IA em Produção](../../../translated_images/pt-PT/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, a capacidade de compreender o seu comportamento, monitorizar o seu desempenho e avaliar sistematicamente os seus resultados torna-se importante.

## Objetivos de Aprendizagem

Após completar esta lição, irá saber/entender:
- Conceitos principais de observabilidade e avaliação de agentes
- Técnicas para melhorar o desempenho, custos e eficácia dos agentes
- O que e como avaliar os seus agentes de IA sistematicamente
- Como controlar custos ao implementar agentes de IA em produção
- Como instrumentar agentes construídos com o Microsoft Agent Framework

O objetivo é dotá-lo do conhecimento para transformar os seus agentes "caixa preta" em sistemas transparentes, geríveis e fiáveis.

_**Nota:** É importante implementar Agentes de IA que sejam seguros e confiáveis. Veja também a lição [Construir Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)._

## Rastreamentos e Spans

Ferramentas de observabilidade como [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) geralmente representam execuções de agentes como rastreamentos (traces) e spans.

- **Rastreamento** representa uma tarefa completa do agente do início ao fim (como tratar uma consulta de um utilizador).
- **Spans** são etapas individuais dentro do rastreamento (como chamar um modelo de linguagem ou recuperar dados).

![Árvore de rastreamento em Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- URL da imagem mantida para fins ilustrativos -->

Sem observabilidade, um agente de IA pode parecer uma "caixa preta" – o seu estado interno e raciocínio são opacos, dificultando o diagnóstico de problemas ou a otimização do desempenho. Com observabilidade, os agentes tornam-se "caixas de vidro", oferecendo transparência vital para construir confiança e garantir que operam conforme pretendido.

## Por Que a Observabilidade é Importante em Ambientes de Produção

A transição dos agentes de IA para ambientes de produção introduz um novo conjunto de desafios e requisitos. A observabilidade deixa de ser um "extra" e torna-se numa capacidade crítica:

*   **Depuração e Análise da Causa Raiz**: Quando um agente falha ou produz um resultado inesperado, as ferramentas de observabilidade fornecem os rastreamentos necessários para identificar a fonte do erro. Isto é especialmente importante em agentes complexos que podem envolver múltiplas chamadas a LLM, interações com ferramentas e lógica condicional.
*   **Gestão de Latência e Custos**: Os agentes de IA frequentemente dependem de LLMs e outras APIs externas que são cobradas por token ou por chamada. A observabilidade permite o rastreio preciso destas chamadas, ajudando a identificar operações que são excessivamente lentas ou caras. Isto permite às equipas otimizar prompts, selecionar modelos mais eficientes ou redesenhar fluxos de trabalho para gerir os custos operacionais e assegurar uma boa experiência ao utilizador.
*   **Confiança, Segurança e Conformidade**: Em muitas aplicações, é importante assegurar que os agentes se comportam de forma segura e ética. A observabilidade proporciona um registo das ações e decisões dos agentes. Isto pode ser usado para detectar e mitigar problemas como injeção de prompt, geração de conteúdo nocivo ou o manejo indevido de informação pessoal identificável (PII). Por exemplo, pode rever rastreamentos para entender porque é que um agente forneceu determinada resposta ou utilizou uma ferramenta específica.
*   **Ciclos de Melhoria Contínua**: Os dados de observabilidade são a base de um processo iterativo de desenvolvimento. Ao monitorizar como os agentes se comportam no mundo real, as equipas podem identificar áreas a melhorar, recolher dados para afinar modelos e validar o impacto das mudanças. Isto cria um ciclo de feedback onde os insights de produção da avaliação online informam a experimentação e refinamento offline, levando a um desempenho progressivamente melhor do agente.

## Métricas-Chave para Acompanhar

Para monitorizar e compreender o comportamento do agente, deve ser acompanhado um conjunto de métricas e sinais. Embora as métricas específicas possam variar conforme o propósito do agente, algumas são universalmente importantes.

Aqui estão algumas das métricas mais comuns que as ferramentas de observabilidade monitorizam:

**Latência:** Quão rapidamente o agente responde? Tempos de espera longos impactam negativamente a experiência do utilizador. Deve medir a latência para tarefas e etapas individuais rastreando as execuções do agente. Por exemplo, um agente que demora 20 segundos para todas as chamadas de modelo poderia ser acelerado usando um modelo mais rápido ou executando as chamadas em paralelo.

**Custos:** Qual é o custo por execução do agente? Os agentes de IA dependem de chamadas a LLM cobradas por token ou APIs externas. Uso frequente de ferramentas ou múltiplos prompts pode aumentar rapidamente os custos. Por exemplo, se um agente chama um LLM cinco vezes para uma melhoria marginal de qualidade, deve avaliar se o custo é justificado ou se poderia reduzir o número de chamadas ou usar um modelo mais barato. O monitoramento em tempo real também pode ajudar a identificar picos inesperados (ex.: bugs causando ciclos excessivos de API).

**Erros de Pedido:** Quantos pedidos falhou o agente? Isto pode incluir erros de API ou chamadas a ferramentas falhadas. Para tornar o seu agente mais robusto contra estes casos em produção, pode configurar fallback ou tentativas repetidas. Ex.: se o provedor LLM A falhar, muda para o provedor LLM B como reserva.

**Feedback do Utilizador:** Implementar avaliações diretas dos utilizadores fornece insights valiosos. Isto pode incluir classificações explícitas (👍gosto/👎não gosto, ⭐1-5 estrelas) ou comentários textuais. Feedback negativo consistente deve alertá-lo, pois indica que o agente não está a funcionar como esperado.

**Feedback Implícito do Utilizador:** Os comportamentos dos utilizadores fornecem feedback indireto mesmo sem classificações explícitas. Isto pode incluir reformulações imediatas da pergunta, consultas repetidas ou clicar num botão de tentar novamente. Ex.: se vir que os utilizadores perguntam repetidamente a mesma questão, isto é sinal que o agente não está a funcionar como esperado.

**Precisão:** Quão frequentemente o agente produz respostas corretas ou desejáveis? As definições de precisão variam (ex.: corretude da resolução de problemas, precisão na recuperação de informação, satisfação do utilizador). O primeiro passo é definir o que significa sucesso para o seu agente. Pode acompanhar a precisão através de verificações automáticas, pontuações de avaliação ou etiquetas de conclusão de tarefa. Por exemplo, marcar rastreamentos como "bem-sucedidos" ou "falhados".

**Métricas de Avaliação Automatizadas:** Também pode configurar avaliações automáticas. Por exemplo, pode usar um LLM para pontuar a saída do agente, ex.: se é útil, precisa, ou não. Existem várias bibliotecas open source que ajudam a pontuar diferentes aspetos do agente. Ex.: [RAGAS](https://docs.ragas.io/) para agentes RAG ou [LLM Guard](https://github.com/protectai/llm-guard) para detectar linguagem nociva ou injeção de prompt.

Na prática, uma combinação destas métricas oferece a melhor cobertura da saúde de um agente de IA. No [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) deste capítulo, mostraremos como estas métricas se apresentam em exemplos reais, mas primeiro, aprenderemos como é o fluxo de trabalho típico de avaliação.

## Instrumente o seu Agente

Para recolher dados de rastreamento, precisará de instrumentar o seu código. O objetivo é instrumentar o código do agente para emitir rastreamentos e métricas que podem ser capturados, processados e visualizados por uma plataforma de observabilidade.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) emergiu como um padrão da indústria para observabilidade de LLM. Fornece um conjunto de APIs, SDKs e ferramentas para gerar, recolher e exportar dados de telemetria.

Existem muitas bibliotecas de instrumentação que envolvem frameworks de agentes existentes e facilitam exportar spans OpenTelemetry para uma ferramenta de observabilidade. O Microsoft Agent Framework integra-se nativamente com o OpenTelemetry. Abaixo está um exemplo de instrumentar um agente MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

O [notebook de exemplo](./code_samples/10-expense_claim-demo.ipynb) neste capítulo demonstrará como instrumentar o seu agente MAF.

**Criação Manual de Spans:** Embora as bibliotecas de instrumentação forneçam uma base sólida, existem frequentemente casos em que são necessárias informações mais detalhadas ou personalizadas. Pode criar spans manualmente para adicionar lógica personalizada da aplicação. Mais importante, pode enriquecer spans criados automática ou manualmente com atributos personalizados (também conhecidos como etiquetas ou metadados). Estes atributos podem incluir dados específicos do negócio, cálculos intermédios ou qualquer contexto útil para depuração ou análise, como `user_id`, `session_id`, ou `model_version`.

Exemplo de criação manual de rastreamentos e spans com o [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Avaliação de Agentes

A observabilidade fornece métricas, mas a avaliação é o processo de analisar esses dados (e realizar testes) para determinar quão bem um agente de IA está a desempenhar e como pode ser melhorado. Por outras palavras, uma vez que tem esses rastreamentos e métricas, como os usa para avaliar o agente e tomar decisões?

A avaliação regular é importante porque os agentes de IA são muitas vezes não determinísticos e podem evoluir (através de atualizações ou desvio no comportamento do modelo) – sem avaliação, não saberia se o seu “agente inteligente” está realmente a fazer bem o seu trabalho ou se houve regressão.

Existem duas categorias de avaliações para agentes de IA: **avaliação online** e **avaliação offline**. Ambas são valiosas e complementares. Geralmente começamos com avaliação offline, pois é o passo mínimo necessário antes de implementar qualquer agente.

### Avaliação Offline

![Itens do dataset em Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Isto envolve avaliar o agente num ambiente controlado, tipicamente usando conjuntos de dados de teste, não consultas de utilizadores reais. Usamos datasets selecionados onde sabemos qual o resultado esperado ou comportamento correto, e depois executamos o agente nesses.

Por exemplo, se construiu um agente para resolver problemas matemáticos verbais, poderá ter um [dataset de teste](https://huggingface.co/datasets/openai/gsm8k) com 100 problemas e respostas conhecidas. A avaliação offline é frequentemente feita durante o desenvolvimento (e pode ser parte de pipelines CI/CD) para verificar melhorias ou evitar regressões. A vantagem é que é **repetível e pode obter métricas claras de precisão, pois tem a verdade fundamental**. Também pode simular consultas de utilizadores e medir as respostas do agente contra respostas ideais ou usar métricas automáticas como descrito acima.

O principal desafio da avaliação offline é garantir que o conjunto de dados de teste é abrangente e se mantém relevante – o agente pode ter bom desempenho num conjunto fixo, mas encontrar consultas muito diferentes em produção. Assim, deve manter os conjuntos de teste atualizados com novos casos extremos e exemplos que reflitam cenários do mundo real. Uma mistura de pequenos conjuntos “smoke test” e conjuntos maiores de avaliação é útil: pequenos para verificações rápidas e maiores para métricas de desempenho mais amplas.

### Avaliação Online

![Resumo de métricas de observabilidade](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Refere-se à avaliação do agente num ambiente real, ao vivo, ou seja, durante a utilização real em produção. A avaliação online envolve monitorizar o desempenho do agente em interações reais com utilizadores e analisar os resultados continuamente.

Por exemplo, pode acompanhar taxas de sucesso, pontuações de satisfação dos utilizadores, ou outras métricas no tráfego ao vivo. A vantagem da avaliação online é que **capta aspetos que pode não antecipar num laboratório** – pode observar desvios do modelo ao longo do tempo (se a eficácia do agente degradar conforme mudam os padrões de entrada) e identificar consultas ou situações inesperadas que não constavam dos seus dados de teste. Fornece uma imagem verdadeira de como o agente se comporta no mundo real.

A avaliação online frequentemente envolve recolher feedback implícito e explícito dos utilizadores, como discutido, e possivelmente executar testes sombra ou testes A/B (onde uma nova versão do agente corre em paralelo para comparação). O desafio é que pode ser difícil obter rótulos ou pontuações fiáveis para interações ao vivo – pode depender do feedback do utilizador ou métricas a jusante (ex.: se o utilizador clicou no resultado).

### Combinar os Dois

Avaliações online e offline não são mutuamente exclusivas; são altamente complementares. Insights da monitorização online (ex.: novos tipos de consultas onde o agente tem desempenho fraco) podem ser usados para ampliar e melhorar os datasets de teste offline. Por outro lado, agentes que têm bom desempenho em testes offline podem ser implementados e monitorizados online com mais confiança.

Na realidade, muitas equipas adotam um ciclo:

_avaliar offline -> implementar -> monitorizar online -> recolher novos casos de falha -> adicionar ao dataset offline -> refinar agente -> repetir_.

## Problemas Comuns

Ao implementar agentes de IA em produção, pode encontrar vários desafios. Aqui estão alguns problemas comuns e as suas soluções potenciais:

| **Problema**    | **Solução Potencial**   |
| ------------- | ------------------ |
| Agente de IA não realiza tarefas de forma consistente | - Refinar o prompt dado ao agente de IA; ser claro quanto aos objetivos.<br>- Identificar onde dividir as tarefas em subtarefas e tratá-las por múltiplos agentes pode ajudar. |
| Agente de IA entra em ciclos contínuos  | - Garantir termos e condições claros para a terminação para que o agente saiba quando interromper o processo.<br>- Para tarefas complexas que requerem raciocínio e planeamento, usar um modelo maior especializado para tarefas de raciocínio. |
| Chamadas a ferramentas pelo agente de IA não funcionam bem   | - Testar e validar a saída da ferramenta fora do sistema do agente.<br>- Refinar parâmetros definidos, prompts e nomes das ferramentas.  |
| Sistema Multi-Agente não funciona consistentemente | - Refinar prompts dados a cada agente para garantir que são específicos e distintos entre si.<br>- Construir um sistema hierárquico usando um agente "router" ou controlador para determinar qual agente é o correto. |

Muitos destes problemas podem ser identificados de forma mais eficiente com a observabilidade implementada. Os rastreamentos e métricas que discutimos anteriormente ajudam a localizar exatamente onde no fluxo de trabalho do agente ocorrem os problemas, tornando a depuração e otimização muito mais eficientes.

## Gestão de Custos

Aqui estão algumas estratégias para gerir os custos da implementação de agentes de IA em produção:

**Usar Modelos Menores:** Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentivos e reduzirão significativamente os custos. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor forma de entender quão bem um SLM vai funcionar no seu caso de uso. Considere usar SLMs para tarefas mais simples como classificação de intenção ou extração de parâmetros, reservando modelos maiores para raciocínios complexos.

**Usar um Modelo Roteador:** Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Pode utilizar um LLM/SLM ou função serverless para encaminhar pedidos baseando-se na complexidade para os modelos mais adequados. Isto também ajudará a reduzir custos, garantindo desempenho nas tarefas certas. Por exemplo, direcione consultas simples para modelos mais pequenos e rápidos, e use modelos caros e grandes apenas para tarefas de raciocínio complexas.

**Guardar Respostas em Cache:** Identificar pedidos e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agentivo é uma boa forma de reduzir o volume de pedidos semelhantes. Pode até implementar um fluxo para identificar o quão semelhante um pedido é relativamente aos pedidos guardados usando modelos de IA mais básicos. Esta estratégia pode reduzir significativamente os custos para perguntas frequentes ou fluxos de trabalho comuns.

## Vamos ver como isto funciona na prática

No [exemplo notebook desta secção](./code_samples/10-expense_claim-demo.ipynb), veremos exemplos de como podemos usar ferramentas de observabilidade para monitorizar e avaliar o nosso agente.


### Tem Mais Perguntas sobre Agentes de IA em Produção?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Lição Anterior

[Padrão de Design Metacognition](../09-metacognition/README.md)

## Próxima Lição

[Protocolos Agentivos](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->