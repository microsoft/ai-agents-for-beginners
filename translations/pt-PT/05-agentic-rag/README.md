[![Agentic RAG](../../../translated_images/pt-PT/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Agentic RAG

Esta lição fornece uma visão geral abrangente do Agentic Retrieval-Augmented Generation (Agentic RAG), um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planeiam autonomamente os seus próximos passos enquanto extraem informação de fontes externas. Ao contrário dos padrões estáticos de consulta-seguido-de-leitura, o Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. O sistema avalia os resultados, refina as consultas, invoca ferramentas adicionais se necessário e continua este ciclo até conseguir uma solução satisfatória.

## Introdução

Esta lição cobrirá

- **Compreender o Agentic RAG:** Conhecer o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planeiam autonomamente os seus próximos passos enquanto extraem informação de fontes de dados externas.
- **Entender o Estilo Iterativo Maker-Checker:** Compreender o ciclo de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas, concebido para melhorar a correção e lidar com consultas mal formadas.
- **Explorar Aplicações Práticas:** Identificar cenários onde o Agentic RAG sobressai, como ambientes que priorizam a correção, interações complexas com bases de dados e fluxos de trabalho prolongados.

## Objetivos de Aprendizagem

Após concluir esta lição, saberá/compreenderá:

- **Compreender o Agentic RAG:** Conhecer o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planeiam autonomamente os seus próximos passos enquanto extraem informação de fontes de dados externas.
- **Estilo Iterativo Maker-Checker:** Compreender o conceito de um ciclo de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas, concebido para melhorar a correção e lidar com consultas mal formadas.
- **Dominar o Processo de Raciocínio:** Compreender a capacidade do sistema de assumir o seu processo de raciocínio, tomando decisões sobre como abordar os problemas sem depender de caminhos pré-definidos.
- **Fluxo de Trabalho:** Entender como um modelo agenciado decide independentemente recuperar relatórios de tendências de mercado, identificar dados de concorrentes, correlacionar métricas internas de vendas, sintetizar as conclusões e avaliar a estratégia.
- **Ciclos Iterativos, Integração de Ferramentas e Memória:** Conhecer a dependência do sistema num padrão de interação em ciclo, mantendo estado e memória entre passos para evitar loops repetitivos e tomar decisões informadas.
- **Gerir Modos de Falha e Auto-Correção:** Explorar os robustos mecanismos de auto-correção do sistema, incluindo iterar e reenviar consultas, usar ferramentas de diagnóstico e recorrer à supervisão humana.
- **Limites da Agência:** Entender as limitações do Agentic RAG, focando na autonomia específica do domínio, dependência da infraestrutura e respeito pelas regras definidas.
- **Casos de Uso Práticos e Valor:** Identificar cenários onde o Agentic RAG destaca-se, como ambientes que priorizam a correção, interações complexas com bases de dados e fluxos de trabalho prolongados.
- **Governação, Transparência e Confiança:** Conhecer a importância da governação e transparência, incluindo raciocínio explicável, controlo de viés e supervisão humana.

## O que é o Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planeiam autonomamente os seus próximos passos enquanto extraem informação de fontes externas. Ao contrário dos padrões estáticos de consulta-seguido-de-leitura, o Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. O sistema avalia os resultados, refina as consultas, invoca ferramentas adicionais se necessário e continua este ciclo até obter uma solução satisfatória. Este estilo iterativo do tipo “maker-checker” melhora a correção, lida com consultas mal formadas e assegura resultados de alta qualidade.

O sistema assume ativamente o seu processo de raciocínio, reescrevendo consultas falhadas, escolhendo métodos de recuperação diferentes e integrando múltiplas ferramentas — como pesquisa vetorial no Azure AI Search, bases de dados SQL ou APIs personalizadas — antes de finalizar a sua resposta. A característica distintiva de um sistema agentic é a sua capacidade de assumir o seu processo de raciocínio. Implementações tradicionais de RAG baseiam-se em caminhos pré-definidos, mas um sistema agentic decide autonomamente a sequência de passos com base na qualidade da informação que encontra.

## Definição de Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente no desenvolvimento de IA onde os LLMs não só extraem informação de fontes de dados externas mas também planeiam autonomamente os seus próximos passos. Ao contrário dos padrões estáticos de consulta-seguido-de-leitura ou sequências cuidadosamente escritas de prompts, o Agentic RAG envolve um ciclo de chamadas iterativas ao LLM, intercaladas com chamadas a ferramentas ou funções e saídas estruturadas. A cada ciclo, o sistema avalia os resultados obtidos, decide se deve refinar as consultas, invoca ferramentas adicionais se necessário e continua este ciclo até alcançar uma solução satisfatória.

Este estilo iterativo de operação “maker-checker” foi concebido para melhorar a correção, lidar com consultas mal formadas para bases de dados estruturadas (por exemplo, NL2SQL) e assegurar resultados equilibrados e de alta qualidade. Em vez de depender exclusivamente de cadeias cuidadosamente elaboradas de prompts, o sistema assume ativamente o seu processo de raciocínio. Pode reescrever consultas que falham, escolher métodos de recuperação diferentes e integrar múltiplas ferramentas — como pesquisa vetorial no Azure AI Search, bases de dados SQL ou APIs personalizadas — antes de finalizar a resposta. Isto elimina a necessidade de frameworks de orquestração excessivamente complexos. Em vez disso, um ciclo relativamente simples de “chamada LLM → uso de ferramenta → chamada LLM → ...” pode gerar saídas sofisticadas e bem fundamentadas.

![Ciclo Principal do Agentic RAG](../../../translated_images/pt-PT/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Assumir o Processo de Raciocínio

A qualidade distintiva que torna um sistema “agentic” é a sua capacidade de assumir o seu processo de raciocínio. Implementações tradicionais de RAG dependem frequentemente de humanos a pré-definir um caminho para o modelo: uma cadeia de pensamento que indica o que recuperar e quando.
Mas quando um sistema é verdadeiramente agentic, ele decide internamente como abordar o problema. Não está apenas a executar um script; está a determinar autonomamente a sequência de passos com base na qualidade da informação que encontra.
Por exemplo, se lhe for pedido que crie uma estratégia de lançamento de produto, não depende apenas de um prompt que detalhe todo o fluxo de trabalho de investigação e tomada de decisão. Em vez disso, o modelo agentic decide independentemente:

1. Recuperar relatórios atuais de tendências de mercado usando Bing Web Grounding
2. Identificar dados relevantes de concorrentes usando Azure AI Search.
3. Correlacionar as métricas internas históricas de vendas usando Azure SQL Database.
4. Sintetizar as conclusões numa estratégia coesa orquestrada via Azure OpenAI Service.
5. Avaliar a estratégia para lacunas ou inconsistências, solicitando outra ronda de recuperação, se necessário.
Todos estes passos — refinar consultas, escolher fontes, iterar até ficar “satisfeito” com a resposta — são decididos pelo modelo, não pré-escritos por um humano.

## Ciclos Iterativos, Integração de Ferramentas e Memória

![Arquitetura de Integração de Ferramentas](../../../translated_images/pt-PT/tool-integration.0f569710b5c17c10.webp)

Um sistema agentic baseia-se num padrão de interação em ciclo:

- **Chamada Inicial:** O objetivo do utilizador (também conhecido como prompt do utilizador) é apresentado ao LLM.
- **Invocação da Ferramenta:** Se o modelo identificar informação em falta ou instruções ambíguas, seleciona uma ferramenta ou método de recuperação — como uma consulta a base de dados vetorial (por exemplo, pesquisa híbrida Azure AI Search sobre dados privados) ou uma chamada SQL estruturada — para recolher mais contexto.
- **Avaliação & Refinamento:** Depois de rever os dados devolvidos, o modelo decide se a informação é suficiente. Caso contrário, refina a consulta, tenta uma ferramenta diferente ou ajusta a sua abordagem.
- **Repetir Até Estar Satisfeito:** Este ciclo continua até o modelo determinar que tem clareza e evidência suficiente para fornecer uma resposta final bem fundamentada.
- **Memória & Estado:** Como o sistema mantém estado e memória entre passos, pode recordar tentativas anteriores e seus resultados, evitando loops repetitivos e tomando decisões mais informadas à medida que avança.

Ao longo do tempo, isto cria uma sensação de compreensão evolutiva, permitindo ao modelo navegar por tarefas complexas e com múltiplos passos sem exigir intervenção humana constante ou reformulação do prompt.

## Gerir Modos de Falha e Auto-Correção

A autonomia do Agentic RAG envolve também robustos mecanismos de auto-correção. Quando o sistema atinge impasses — como recuperar documentos irrelevantes ou encontrar consultas mal formadas — pode:

- **Iterar e Re-consultar:** Em vez de devolver respostas de baixo valor, o modelo tenta novas estratégias de pesquisa, reescreve consultas a bases de dados ou analisa conjuntos de dados alternativos.
- **Usar Ferramentas de Diagnóstico:** O sistema pode invocar funções adicionais concebidas para o ajudar a depurar os seus passos de raciocínio ou confirmar a correção dos dados recuperados. Ferramentas como Azure AI Tracing são importantes para permitir observabilidade e monitorização robustas.
- **Recorrer à Supervisão Humana:** Para cenários de alto risco ou falhas repetidas, o modelo pode assinalar incertezas e solicitar orientação humana. Uma vez que o humano fornece feedback corretivo, o modelo pode incorporar essa lição para o futuro.

Esta abordagem iterativa e dinâmica permite que o modelo melhore continuamente, assegurando que não é apenas um sistema de uma só vez, mas sim um que aprende com os seus erros durante uma sessão dada.

![Mecanismo de Auto-correção](../../../translated_images/pt-PT/self-correction.da87f3783b7f174b.webp)

## Limites da Agência

Apesar da sua autonomia dentro de uma tarefa, o Agentic RAG não é análogo à Inteligência Artificial Geral. As suas capacidades “agentic” estão confinadas às ferramentas, fontes de dados e políticas fornecidas pelos desenvolvedores humanos. Não pode inventar as suas próprias ferramentas nem ultrapassar os limites do domínio que foram estabelecidos. Em vez disso, destaca-se por orquestrar dinamicamente os recursos disponíveis.
As diferenças chave em relação a formas de IA mais avançadas incluem:

1. **Autonomia Específica de Domínio:** Os sistemas Agentic RAG estão focados em alcançar objetivos definidos pelo utilizador dentro de um domínio conhecido, empregando estratégias como reescrita de consultas ou seleção de ferramentas para melhorar resultados.
2. **Dependência da Infraestrutura:** As capacidades do sistema dependem das ferramentas e dados integrados pelos desenvolvedores. Não pode ultrapassar esses limites sem intervenção humana.
3. **Respeito pelas Regras:** Diretrizes éticas, regras de conformidade e políticas empresariais continuam a ser muito importantes. A liberdade do agente está sempre limitada por medidas de segurança e mecanismos de supervisão (esperemos).

## Casos de Uso Práticos e Valor

O Agentic RAG destaca-se em cenários que requerem refinamento iterativo e precisão:

1. **Ambientes que Prioritizam Correção:** Em verificações de conformidade, análises regulamentares ou investigação jurídica, o modelo agentic pode verificar factos repetidamente, consultar múltiplas fontes e reescrever consultas até fornecer uma resposta rigorosamente validada.
2. **Interações Complexas com Bases de Dados:** Ao lidar com dados estruturados onde as consultas podem frequentemente falhar ou necessitar de ajuste, o sistema pode refinar autonomamente as suas consultas usando Azure SQL ou Microsoft Fabric OneLake, assegurando que a recuperação final está alinhada com a intenção do utilizador.
3. **Fluxos de Trabalho Prolongados:** Sessões de maior duração podem evoluir à medida que surgem novas informações. O Agentic RAG pode continuamente incorporar novos dados, ajustando estratégias à medida que aprende mais sobre o domínio do problema.

## Governação, Transparência e Confiança

À medida que estes sistemas se tornam mais autónomos no seu raciocínio, a governação e transparência são cruciais:

- **Raciocínio Explicável:** O modelo pode fornecer uma trilha de auditoria das consultas que fez, das fontes que consultou e dos passos de raciocínio que tomou para alcançar a sua conclusão. Ferramentas como Azure AI Content Safety e Azure AI Tracing / GenAIOps podem ajudar a manter a transparência e mitigar riscos.
- **Controlo de Viés e Recuperação Equilibrada:** Os desenvolvedores podem ajustar estratégias de recuperação para garantir que são consideradas fontes de dados equilibradas e representativas, e auditar regularmente as saídas para detetar viés ou padrões desviantes usando modelos personalizados para organizações avançadas de ciência de dados que utilizam Azure Machine Learning.
- **Supervisão Humana e Conformidade:** Para tarefas sensíveis, a revisão humana continua a ser essencial. O Agentic RAG não substitui o julgamento humano em decisões críticas—ele o complementa ao fornecer opções mais rigorosamente validadas.

Ter ferramentas que forneçam um registo claro de ações é essencial. Sem elas, depurar um processo com múltiplos passos pode ser muito difícil. Veja o exemplo seguinte da Literal AI (empresa por trás do Chainlit) para uma execução de Agente:

![Exemplo de Execução de Agente](../../../translated_images/pt-PT/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusão

O Agentic RAG representa uma evolução natural na forma como os sistemas de IA lidam com tarefas complexas e intensivas em dados. Ao adotar um padrão de interação em ciclo, selecionar autonomamente ferramentas e refinar consultas até alcançar um resultado de alta qualidade, o sistema ultrapassa o meramente seguir prompts estáticos para se tornar um decisor mais adaptativo e consciente do contexto. Embora ainda esteja limitado por infraestruturas e diretrizes éticas definidas por humanos, estas capacidades agentic permitem interações de IA mais ricas, dinâmicas e, em última análise, mais úteis tanto para empresas como para utilizadores finais.

### Tem mais perguntas sobre Agentic RAG?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em sessões de esclarecimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implemente Retrieval Augmented Generation (RAG) com o Azure OpenAI Service: Aprenda como usar os seus próprios dados com o Azure OpenAI Service. Este módulo Microsoft Learn fornece um guia abrangente sobre a implementação do RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de aplicações de IA generativa com Microsoft Foundry: Este artigo abrange a avaliação e comparação de modelos em datasets publicamente disponíveis, incluindo aplicações Agentic AI e arquiteturas RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">O que é Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Guia Completo para Agent-Based Retrieval Augmented Generation – Notícias da geração RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: acelere o seu RAG com reformulação de consultas e auto-consulta! Livro de Receitas de IA Open-Source da Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Adicionando Camadas Agentes a RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">O Futuro dos Assistentes de Conhecimento: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Como Construir Sistemas Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Usar o Serviço Microsoft Foundry Agent para escalar os seus agentes de IA</a>

### Artigos Académicos

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Refinamento Iterativo com Auto-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agentes de Linguagem com Aprendizagem por Reforço Verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Grandes Modelos de Linguagem Podem Auto-Corrigir-se com Críticas Interativas por Ferramentas</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Geração Aumentada por Recuperação Agentic: Um Estudo Sobre Agentic RAG</a>

## Teste Rápido deste Agente (Opcional)

Após aprender a implementar agentes em [Lição 16](../16-deploying-scalable-agents/README.md), pode fazer um teste rápido ao `TravelRAGAgent` desta lição — verificando que as suas respostas mantêm-se fundamentadas na base de conhecimento — com [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Consulte [`tests/README.md`](../tests/README.md) para saber como executá-lo.

## Lição Anterior

[Padrão de Design de Utilização de Ferramentas](../04-tool-use/README.md)

## Próxima Lição

[Construir Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->