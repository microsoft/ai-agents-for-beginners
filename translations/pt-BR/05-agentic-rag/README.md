[![Agentic RAG](../../../translated_images/pt-BR/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Agentic RAG

Esta lição oferece uma visão abrangente sobre Agentic Retrieval-Augmented Generation (Agentic RAG), um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas. Diferente dos padrões estáticos de recuperação e leitura, Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. O sistema avalia os resultados, refina consultas, invoca ferramentas adicionais conforme necessário e continua esse ciclo até que uma solução satisfatória seja alcançada.

## Introdução

Esta lição abordará

- **Entender o Agentic RAG:** Aprenda sobre o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações em fontes externas.
- **Compreender o Estilo Iterativo Maker-Checker:** Entenda o loop de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas, projetado para melhorar a correção e lidar com consultas malformadas.
- **Explorar Aplicações Práticas:** Identifique cenários onde o Agentic RAG se destaca, como ambientes que priorizam a correção, interações complexas com bancos de dados e fluxos de trabalho estendidos.

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá/entenderá:

- **Entendimento do Agentic RAG:** Conhecer o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações em fontes externas.
- **Estilo Iterativo Maker-Checker:** Compreender o conceito de um loop de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas, projetado para melhorar a correção e lidar com consultas malformadas.
- **Assumir o Processo de Raciocínio:** Entender a capacidade do sistema de assumir seu processo de raciocínio, tomando decisões sobre como abordar problemas sem depender de caminhos predefinidos.
- **Fluxo de Trabalho:** Compreender como um modelo agentic decide de forma independente recuperar relatórios de tendências de mercado, identificar dados de concorrentes, correlacionar métricas internas de vendas, sintetizar achados e avaliar a estratégia.
- **Loops Iterativos, Integração de Ferramentas e Memória:** Aprender sobre a dependência do sistema em um padrão de interação em loop, mantendo estado e memória entre etapas para evitar repetições e tomar decisões informadas.
- **Lidando com Modos de Falha e Auto-Correção:** Explorar os mecanismos robustos de auto-correção do sistema, incluindo iteração e reconsulta, uso de ferramentas de diagnóstico e recurso à supervisão humana.
- **Limites da Agência:** Compreender as limitações do Agentic RAG, focando em autonomia específica do domínio, dependência de infraestrutura e respeito às diretrizes.
- **Casos de Uso Práticos e Valor:** Identificar cenários em que o Agentic RAG se destaca, como ambientes que priorizam a correção, interações complexas com bancos de dados e fluxos de trabalho estendidos.
- **Governança, Transparência e Confiança:** Entender a importância da governança e transparência, incluindo raciocínio explicável, controle de viés e supervisão humana.

## O que é Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas. Diferente dos padrões estáticos de recuperação e leitura, o Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. O sistema avalia os resultados, refina consultas, invoca ferramentas adicionais se necessário e continua esse ciclo até atingir uma solução satisfatória. Esse estilo iterativo “maker-checker” melhora a correção, lida com consultas malformadas e garante resultados de alta qualidade.

O sistema assume ativamente seu processo de raciocínio, reescrevendo consultas falhas, escolhendo métodos diferentes de recuperação e integrando múltiplas ferramentas — como busca vetorial no Azure AI Search, bancos de dados SQL ou APIs customizadas — antes de finalizar sua resposta. A qualidade distintiva de um sistema agentic é sua capacidade de assumir seu processo de raciocínio. Implementações tradicionais de RAG dependem de caminhos predefinidos, mas um sistema agentic determina autonomamente a sequência de passos com base na qualidade das informações encontradas.

## Definindo Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente no desenvolvimento de IA onde os LLMs não apenas recuperam informações de fontes externas, mas também planejam autonomamente seus próximos passos. Diferentemente dos padrões estáticos de recuperação e leitura ou das sequências de prompts cuidadosamente roteirizadas, o Agentic RAG envolve um loop de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. A cada etapa, o sistema avalia os resultados obtidos, decide se deve refinar suas consultas, invoca ferramentas adicionais se necessário e continua esse ciclo até alcançar uma solução satisfatória.

Esse estilo iterativo “maker-checker” é projetado para melhorar a correção, lidar com consultas malformadas em bancos de dados estruturados (ex: NL2SQL) e garantir resultados equilibrados e de alta qualidade. Em vez de depender exclusivamente de cadeias de prompts cuidadosamente elaboradas, o sistema assume ativamente seu processo de raciocínio. Ele pode reescrever consultas que falham, escolher métodos de recuperação diferentes e integrar múltiplas ferramentas — como busca vetorial no Azure AI Search, bancos de dados SQL ou APIs customizadas — antes de finalizar sua resposta. Isso elimina a necessidade de frameworks de orquestração excessivamente complexos. Em vez disso, um loop relativamente simples de “chamada LLM → uso da ferramenta → chamada LLM → …” pode gerar saídas sofisticadas e bem fundamentadas.

![Agentic RAG Core Loop](../../../translated_images/pt-BR/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Assumindo o Processo de Raciocínio

A qualidade distintiva que torna um sistema “agentic” é sua capacidade de assumir seu processo de raciocínio. Implementações tradicionais de RAG frequentemente dependem de humanos que predefinem um caminho para o modelo: uma cadeia de pensamento que orienta o que recuperar e quando.
Mas quando um sistema é verdadeiramente agentic, ele decide internamente como abordar o problema. Não está apenas executando um script; está determinando autonomamente a sequência de passos com base na qualidade das informações que encontra.
Por exemplo, se for solicitado a criar uma estratégia para lançamento de produto, não depende apenas de um prompt que descreve todo o fluxo de trabalho de pesquisa e tomada de decisão. Em vez disso, o modelo agentic decide independentemente:

1. Recuperar relatórios atuais de tendências de mercado usando Bing Web Grounding
2. Identificar dados relevantes de concorrentes utilizando Azure AI Search.
3. Correlacionar métricas históricas internas de vendas usando Azure SQL Database.
4. Sintetizar os resultados em uma estratégia coesa orquestrada via Azure OpenAI Service.
5. Avaliar a estratégia para lacunas ou inconsistências, solicitando outra rodada de recuperação se necessário.
Todas essas etapas — refinar consultas, escolher fontes, iterar até estar “satisfeito” com a resposta — são decididas pelo modelo, não pré-roteirizadas por um humano.

## Loops Iterativos, Integração de Ferramentas e Memória

![Arquitetura de Integração de Ferramentas](../../../translated_images/pt-BR/tool-integration.0f569710b5c17c10.webp)

Um sistema agentic depende de um padrão de interação em loop:

- **Chamada Inicial:** O objetivo do usuário (também conhecido como prompt do usuário) é apresentado ao LLM.
- **Invocação da Ferramenta:** Se o modelo identificar informações faltantes ou instruções ambíguas, ele seleciona uma ferramenta ou método de recuperação — como uma consulta a um banco de dados vetorial (ex: busca híbrida Azure AI Search em dados privados) ou uma chamada SQL estruturada — para coletar mais contexto.
- **Avaliação & Refinamento:** Após revisar os dados retornados, o modelo decide se as informações são suficientes. Caso contrário, ele refina a consulta, tenta uma ferramenta diferente ou ajusta sua abordagem.
- **Repetir Até Estar Satisfeito:** Esse ciclo continua até que o modelo determine ter clareza e evidência suficientes para fornecer uma resposta final bem fundamentada.
- **Memória & Estado:** Como o sistema mantém estado e memória entre etapas, ele pode recordar tentativas anteriores e seus resultados, evitando repetições e tomando decisões mais informadas no processo.

Com o tempo, isso cria uma sensação de compreensão evolutiva, permitindo que o modelo navegue por tarefas complexas e multi-etapas sem exigir que um humano intervenha constantemente ou reformule o prompt.

## Lidando com Modos de Falha e Auto-Correção

A autonomia do Agentic RAG também envolve mecanismos robustos de auto-correção. Quando o sistema encontra pontos cegos — como recuperar documentos irrelevantes ou enfrentar consultas malformadas — ele pode:

- **Iterar e Reconsultar:** Em vez de retornar respostas de baixo valor, o modelo tenta novas estratégias de busca, reescreve consultas ao banco de dados ou examina conjuntos de dados alternativos.
- **Usar Ferramentas de Diagnóstico:** O sistema pode invocar funções adicionais projetadas para ajudar a depurar seus passos de raciocínio ou confirmar a correção dos dados recuperados. Ferramentas como Azure AI Tracing serão importantes para possibilitar observabilidade e monitoramento robustos.
- **Recurso à Supervisão Humana:** Para cenários de alto risco ou falhas repetidas, o modelo pode sinalizar incertezas e solicitar orientação humana. Uma vez que o humano oferece feedback corretivo, o modelo pode incorporar essa lição daqui para frente.

Essa abordagem iterativa e dinâmica permite que o modelo melhore continuamente, assegurando que não seja apenas um sistema de uma única execução, mas um que aprende com seus erros durante uma sessão.

![Mecanismo de Auto-Correção](../../../translated_images/pt-BR/self-correction.da87f3783b7f174b.webp)

## Limites da Agência

Apesar de sua autonomia dentro de uma tarefa, o Agentic RAG não é análogo à Inteligência Artificial Geral. Suas capacidades “agentic” estão confinadas às ferramentas, fontes de dados e políticas fornecidas por desenvolvedores humanos. Ele não pode inventar suas próprias ferramentas nem ultrapassar os limites do domínio estabelecidos. Em vez disso, se destaca na orquestração dinâmica dos recursos disponíveis.
Diferenças-chave em relação a formas de IA mais avançadas incluem:

1. **Autonomia Específica de Domínio:** Sistemas Agentic RAG focam em atingir metas definidas pelo usuário dentro de um domínio conhecido, empregando estratégias como reescrita de consultas ou seleção de ferramentas para melhorar os resultados.
2. **Dependência de Infraestrutura:** As capacidades do sistema dependem das ferramentas e dados integrados pelos desenvolvedores. Ele não pode ultrapassar esses limites sem intervenção humana.
3. **Respeito às Diretrizes:** Diretrizes éticas, regras de conformidade e políticas de negócios permanecem muito importantes. A liberdade do agente está sempre limitada por medidas de segurança e mecanismos de supervisão (esperançosamente?).

## Casos de Uso Práticos e Valor

O Agentic RAG se destaca em cenários que requerem refinamento iterativo e precisão:

1. **Ambientes que Priorizam Correção:** Em verificações de conformidade, análises regulatórias ou pesquisas jurídicas, o modelo agentic pode verificar fatos repetidamente, consultar múltiplas fontes e reescrever consultas até produzir uma resposta minuciosamente validada.
2. **Interações Complexas com Bancos de Dados:** Ao lidar com dados estruturados onde consultas podem frequentemente falhar ou exigir ajustes, o sistema pode refinar autonomamente suas consultas usando Azure SQL ou Microsoft Fabric OneLake, garantindo que a recuperação final esteja alinhada à intenção do usuário.
3. **Fluxos de Trabalho Estendidos:** Sessões de longa duração podem evoluir conforme novas informações surgem. Agentic RAG pode continuamente incorporar novos dados, mudando estratégias à medida que aprende mais sobre o espaço do problema.

## Governança, Transparência e Confiança

À medida que esses sistemas se tornam mais autônomos em seu raciocínio, governança e transparência são cruciais:

- **Raciocínio Explicável:** O modelo pode fornecer uma trilha de auditoria das consultas que realizou, das fontes consultadas e dos passos de raciocínio para chegar à sua conclusão. Ferramentas como Azure AI Content Safety e Azure AI Tracing / GenAIOps podem ajudar a manter a transparência e mitigar riscos.
- **Controle de Viés e Recuperação Balanceada:** Desenvolvedores podem ajustar estratégias de recuperação para garantir que fontes de dados equilibradas e representativas sejam consideradas, e auditar regularmente as saídas para detectar vieses ou padrões distorcidos usando modelos customizados para organizações avançadas de ciência de dados utilizando Azure Machine Learning.
- **Supervisão Humana e Conformidade:** Para tarefas sensíveis, a revisão humana permanece essencial. Agentic RAG não substitui o julgamento humano em decisões de alto risco — ele o complementa fornecendo opções minuciosamente avaliadas.

Ter ferramentas que forneçam um registro claro das ações é fundamental. Sem elas, depurar um processo multi-etapas pode ser muito difícil. Veja o exemplo a seguir da Literal AI (empresa por trás do Chainlit) de uma execução de agente:

![AgentRunExample](../../../translated_images/pt-BR/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusão

Agentic RAG representa uma evolução natural na forma como sistemas de IA lidam com tarefas complexas e intensivas em dados. Ao adotar um padrão de interação em loop, selecionar ferramentas autonomamente e refinar consultas até alcançar um resultado de alta qualidade, o sistema ultrapassa o paradigma estático de seguir prompts, tornando-se um tomador de decisão mais adaptativo e consciente do contexto. Embora ainda limitado por infraestruturas e diretrizes éticas definidas por humanos, essas capacidades agentic possibilitam interações de IA mais ricas, dinâmicas e, em última análise, mais úteis para empresas e usuários finais.

### Tem mais perguntas sobre Agentic RAG?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implemente Retrieval Augmented Generation (RAG) com Azure OpenAI Service: Aprenda a usar seus próprios dados com o Azure OpenAI Service. Este módulo do Microsoft Learn oferece um guia completo sobre a implementação de RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de aplicações de IA generativa com Microsoft Foundry: Este artigo cobre a avaliação e comparação de modelos em conjuntos de dados públicos, incluindo aplicações de IA Agentic e arquiteturas RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">O que é Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Um Guia Completo para Agent-Based Retrieval Augmented Generation – Notícias da geração RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbinar seu RAG com reformulação de consultas e auto-consulta! Livro de Receitas de IA Open-Source da Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adicionando Camadas Agentes ao RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">O Futuro dos Assistentes de Conhecimento: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Como Construir Sistemas Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Usando o Microsoft Foundry Agent Service para escalar seus agentes de IA</a>

### Artigos Acadêmicos

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Refinamento Iterativo com Auto-feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agentes Linguísticos com Aprendizado por Reforço Verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Grandes Modelos de Linguagem Podem Auto-Corrigir com Criticismo Interativo com Ferramentas</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Um Levantamento sobre Agentic RAG</a>

## Teste Rápido deste Agente (Opcional)

Depois de aprender a implantar agentes em [Lesson 16](../16-deploying-scalable-agents/README.md), você pode fazer um teste rápido com o `TravelRAGAgent` desta lição — verificando se suas respostas permanecem fundamentadas na base de conhecimento — com [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Veja [`tests/README.md`](../tests/README.md) para saber como executá-lo.

## Lição Anterior

[Padrão de Design de Uso de Ferramentas](../04-tool-use/README.md)

## Próxima Lição

[Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->