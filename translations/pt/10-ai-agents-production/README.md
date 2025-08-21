<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:37:50+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "pt"
}
-->
# Agentes de IA em Produção: Observabilidade e Avaliação

À medida que os agentes de IA passam de protótipos experimentais para aplicações no mundo real, torna-se essencial compreender o seu comportamento, monitorizar o seu desempenho e avaliar sistematicamente os seus resultados.

## Objetivos de Aprendizagem

Após completar esta lição, saberá/compreenderá:

- Técnicas para melhorar o desempenho, custos e eficácia de um sistema de Agentes de IA em produção.
- O que e como avaliar os seus Agentes de IA.
- Como controlar os custos ao implementar Agentes de IA em produção.

É importante implementar Agentes de IA que sejam confiáveis. Consulte também a lição "Building Trustworthy AI Agents".

## Avaliação de Agentes de IA

Antes, durante e depois de implementar Agentes de IA, ter um sistema adequado para avaliar os seus Agentes é fundamental. Isto garante que o seu sistema está alinhado com os seus objetivos e os dos seus utilizadores.

Para avaliar um Agente de IA, é importante ter a capacidade de avaliar não só a saída do agente, mas também todo o sistema em que o seu Agente de IA está a operar. Isto inclui, mas não se limita a:

- O pedido inicial ao modelo.
- A capacidade do agente de identificar a intenção do utilizador.
- A capacidade do agente de identificar a ferramenta correta para realizar a tarefa.
- A resposta da ferramenta ao pedido do agente.
- A capacidade do agente de interpretar a resposta da ferramenta.
- O feedback do utilizador à resposta do agente.

Isto permite identificar áreas de melhoria de forma mais modular. Pode depois monitorizar o efeito das alterações a modelos, prompts, ferramentas e outros componentes com maior eficiência.

## Problemas Comuns e Soluções Potenciais com Agentes de IA

| **Problema**                                   | **Solução Potencial**                                                                                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agente de IA não executa tarefas de forma consistente | - Refine o prompt dado ao Agente de IA; seja claro nos objetivos.<br>- Identifique onde dividir as tarefas em subtarefas e delegá-las a vários agentes pode ajudar.                                                      |
| Agente de IA entra em ciclos contínuos         | - Assegure que existem termos e condições claros de término para que o Agente saiba quando parar o processo.<br>- Para tarefas complexas que requerem raciocínio e planeamento, use um modelo maior especializado nestas tarefas. |
| Chamadas a ferramentas do Agente de IA não funcionam bem | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e nomes das ferramentas.                                                                                        |
| Sistema Multi-Agente não funciona de forma consistente | - Refine os prompts dados a cada agente para garantir que são específicos e distintos entre si.<br>- Construa um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o mais adequado.         |

## Gestão de Custos

Aqui estão algumas estratégias para gerir os custos da implementação de Agentes de IA em produção:

- **Cache de Respostas** - Identificar pedidos e tarefas comuns e fornecer as respostas antes de passarem pelo seu sistema agentic é uma boa forma de reduzir o volume de pedidos semelhantes. Pode até implementar um fluxo para identificar o quão semelhante um pedido é aos pedidos em cache usando modelos de IA mais básicos.

- **Uso de Modelos Menores** - Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso agentic e reduzirão significativamente os custos. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho face a modelos maiores é a melhor forma de perceber quão bem um SLM irá funcionar no seu caso de uso.

- **Uso de um Modelo Roteador** - Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Pode usar um LLM/SLM ou função serverless para encaminhar pedidos com base na complexidade para os modelos mais adequados. Isto também ajuda a reduzir custos, garantindo desempenho nas tarefas certas.

## Parabéns

Esta é atualmente a última lição de "AI Agents for Beginners".

Planeamos continuar a adicionar lições com base no feedback e nas mudanças desta indústria em constante crescimento, por isso volte a visitar-nos em breve.

Se quiser continuar a aprender e a construir com Agentes de IA, junte-se ao <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Organizamos workshops, mesas redondas comunitárias e sessões de "pergunte-me qualquer coisa" lá.

Também temos uma coleção Learn com materiais adicionais que podem ajudar a começar a construir Agentes de IA em produção.

## Aula Anterior

[Metacognition Design Pattern](../09-metacognition/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.