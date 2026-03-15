# Utilizando Protocolos Agentic (MCP, A2A e NLWeb)

[![Agentic Protocols](../../../translated_images/pt-PT/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para ver o vídeo desta lição)_

À medida que o uso de agentes de IA cresce, cresce também a necessidade de protocolos que garantam a padronização, segurança e apoiem a inovação aberta. Nesta lição, abordaremos 3 protocolos que procuram satisfazer essa necessidade - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introdução

Nesta lição, abordaremos:

• Como o **MCP** permite que Agentes de IA acedam a ferramentas e dados externos para completar tarefas do utilizador.

• Como o **A2A** permite a comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces de linguagem natural a qualquer site, permitindo que Agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** o propósito principal e os benefícios do MCP, A2A e NLWeb no contexto de agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agentic complexos.

## Model Context Protocol

O **Model Context Protocol (MCP)** é um standard aberto que fornece uma forma padronizada para aplicações disponibilizarem contexto e ferramentas aos LLMs. Isto permite um "adaptador universal" a diferentes fontes de dados e ferramentas às quais Agentes de IA podem ligar-se de forma consistente.

Vamos observar os componentes do MCP, os benefícios comparados com a utilização direta de APIs e um exemplo de como agentes de IA poderão usar um servidor MCP.

### Componentes Centrais do MCP

O MCP opera numa **arquitetura cliente-servidor** e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como o VSCode) que iniciam as ligações a um Servidor MCP.

• **Clientes** são componentes dentro da aplicação host que mantêm ligações um-para-um com servidores.

• **Servidores** são programas leves que expõem capacidades específicas.

Incluídas no protocolo estão três primitivas principais que são as capacidades de um Servidor MCP:

• **Ferramentas**: Estas são ações ou funções discretas que um agente de IA pode chamar para executar uma ação. Por exemplo, um serviço meteorológico pode expor uma ferramenta "obter tempo", ou um servidor de comércio eletrónico pode expor uma ferramenta "comprar produto". Os servidores MCP anunciam o nome, descrição e esquema de entrada/saída de cada ferramenta na sua listagem de capacidades.

• **Recursos**: São itens de dados ou documentos apenas de leitura que um servidor MCP pode fornecer, e os clientes podem recuperá-los sob demanda. Exemplos incluem conteúdos de ficheiros, registos de base de dados ou ficheiros de log. Os recursos podem ser texto (como código ou JSON) ou binário (como imagens ou PDFs).

• **Prompts**: São modelos predefinidos que fornecem prompts sugeridos, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Os agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor juntamente com descrições do que fazem. Isto contrasta com as APIs tradicionais, que muitas vezes exigem codificação estática para integrações, significando que qualquer alteração na API requer atualizações de código. O MCP oferece uma abordagem "integre uma vez", levando a maior adaptabilidade.

• **Interoperabilidade Entre LLMs**: O MCP funciona entre diferentes LLMs, proporcionando flexibilidade para trocar modelos principais e avaliar para melhor desempenho.

• **Segurança Padronizada**: O MCP inclui um método padrão de autenticação, melhorando a escalabilidade ao adicionar acessos a servidores MCP adicionais. Isto é mais simples do que gerir diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo MCP

![MCP Diagram](../../../translated_images/pt-PT/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine que um utilizador quer reservar um voo usando um assistente de IA alimentado por MCP.

1. **Ligação**: O assistente de IA (o cliente MCP) liga-se a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea, "Que ferramentas tens disponíveis?" O servidor responde com ferramentas como "pesquisar voos" e "reservar voos".

3. **Invocação da Ferramenta**: Depois pedes ao assistente de IA: "Por favor, pesquisa um voo de Portland para Honolulu." O assistente de IA, usando o seu LLM, identifica que precisa chamar a ferramenta "pesquisar voos" e passa os parâmetros relevantes (origem, destino) ao servidor MCP.

4. **Execução e Resposta**: O servidor MCP, agindo como um wrapper, faz a chamada real à API interna de reservas da companhia aérea. Depois recebe a informação do voo (por exemplo, dados em JSON) e envia de volta ao assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voos. Depois de selecionares um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, completando a reserva.

## Protocolo Agente para Agente (A2A)

Enquanto o MCP se foca em ligar LLMs a ferramentas, o **protocolo Agent-to-Agent (A2A)** vai mais além, permitindo comunicação e colaboração entre diferentes agentes de IA. O A2A liga agentes de IA de diferentes organizações, ambientes e pilhas tecnológicas para completar uma tarefa partilhada.

Examinaremos os componentes e benefícios do A2A, junto com um exemplo de como poderá ser aplicado na nossa aplicação de viagens.

### Componentes Centrais do A2A

O A2A foca-se em permitir a comunicação entre agentes e fazê-los trabalhar juntos para completar uma subtarefa do utilizador. Cada componente do protocolo contribui para isto:

#### Agent Card

Semelhante a como um servidor MCP partilha uma lista de ferramentas, um Agent Card tem:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que completa.
- Uma **lista de competências específicas** com descrições para ajudar outros agentes (ou mesmo utilizadores humanos) a entender quando e porquê quereriam chamar esse agente.
- O **URL atual do Endpoint** do agente.
- A **versão** e **capacidades** do agente como respostas em streaming e notificações push.

#### Agent Executor

O Agent Executor é responsável por **passar o contexto da conversa do utilizador para o agente remoto**, o agente remoto precisa disto para compreender a tarefa que precisa ser completada. Num servidor A2A, um agente usa o seu próprio Large Language Model (LLM) para analisar pedidos recebidos e executar tarefas usando as suas ferramentas internas.

#### Artifact

Depois de um agente remoto completar a tarefa solicitada, o seu produto de trabalho é criado como um artefacto. Um artefacto **contém o resultado do trabalho do agente**, uma **descrição do que foi completado**, e o **contexto textual** enviado através do protocolo. Após o artefacto ser enviado, a ligação com o agente remoto é encerrada até ser necessária novamente.

#### Event Queue

Este componente é usado para **gerir atualizações e passar mensagens**. É especialmente importante em produção para sistemas agentic para evitar que a ligação entre agentes seja encerrada antes de uma tarefa estar concluída, especialmente quando os tempos de conclusão podem ser longos.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, partilhem contexto e trabalhem em conjunto, facilitando a automação contínua entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Seleção de Modelos**: Cada agente A2A pode decidir qual LLM usa para atender aos seus pedidos, permitindo modelos otimizados ou ajustados por agente, ao contrário de uma única ligação LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação está integrada diretamente no protocolo A2A, proporcionando um quadro robusto de segurança para as interações entre agentes.

### Exemplo A2A

![A2A Diagram](../../../translated_images/pt-PT/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir o nosso cenário de reserva de viagens, mas desta vez usando A2A.

1. **Pedido do Utilizador a Multi-Agente**: Um utilizador interage com um cliente/agente "Agente de Viagens" A2A, talvez dizendo, "Por favor, reserva uma viagem completa para Honolulu para a próxima semana, incluindo voos, hotel e carro de aluguer".

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe este pedido complexo. Usa o seu LLM para raciocinar sobre a tarefa e determinar que precisa interagir com outros agentes especializados.

3. **Comunicação Inter-agentes**: O Agente de Viagens usa então o protocolo A2A para ligar-se a agentes a jusante, como um "Agente da Companhia Aérea", um "Agente de Hotel" e um "Agente de Aluguer de Carros" criados por diferentes empresas.

4. **Execução Delegada de Tarefa**: O Agente de Viagens envia tarefas específicas a estes agentes especializados (ex.: "Encontra voos para Honolulu", "Reserva um hotel", "Aluga um carro"). Cada um desses agentes especializados, executando os seus próprios LLMs e usando as suas próprias ferramentas (que podem ser servidores MCP), realiza a sua parte específica da reserva.

5. **Resposta Consolidada**: Depois que todos os agentes a jusante completam as suas tarefas, o Agente de Viagens compila os resultados (detalhes dos voos, confirmação do hotel, reserva do carro) e envia uma resposta abrangente em estilo chat de volta ao utilizador.

## Natural Language Web (NLWeb)

Os websites têm sido durante muito tempo a principal forma de os utilizadores acederem a informação e dados na internet.

Vamos observar os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como o nosso NLWeb funciona olhando para a nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código do Serviço Central)**: O sistema que processa perguntas em linguagem natural. Liga as diferentes partes da plataforma para criar respostas. Pode pensar-se nele como o **motor que alimenta as funcionalidades de linguagem natural** de um website.

- **Protocolo NLWeb**: Este é um **conjunto básico de regras para interação em linguagem natural** com um website. Envia respostas em formato JSON (frequentemente usando Schema.org). O seu propósito é criar uma base simples para a “Web AI”, da mesma forma que o HTML tornou possível partilhar documentos online.

- **Servidor MCP (Endpoint Model Context Protocol)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isto significa que pode **partilhar ferramentas (como um método “ask”) e dados** com outros sistemas de IA. Na prática, isto torna o conteúdo e as capacidades do site utilizáveis por agentes de IA, permitindo que o site faça parte do “ecossistema agentic” mais vasto.

- **Modelos de Embedding**: Estes modelos são usados para **converter o conteúdo do website em representações numéricas chamadas vetores** (embeddings). Estes vetores capturam o significado de forma que os computadores possam comparar e pesquisar. São guardados numa base de dados especial, e os utilizadores podem escolher qual modelo de embedding querem usar.

- **Base de Dados Vetorial (Mecanismo de Recuperação)**: Esta base de dados **armazena os embeddings do conteúdo do website**. Quando alguém faz uma pergunta, o NLWeb verifica a base de dados vetorial para encontrar rapidamente a informação mais relevante. Dá uma lista rápida de possíveis respostas, classificadas por similaridade. O NLWeb funciona com diferentes sistemas de armazenamento vetorial como Qdrant, Snowflake, Milvus, Azure AI Search, e Elasticsearch.

### Exemplo NLWeb

![NLWeb](../../../translated_images/pt-PT/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere o nosso website de reserva de viagens novamente, mas desta vez, é alimentado por NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes do website de viagens (ex.: listagens de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via feeds RSS. As ferramentas do NLWeb ingerem esses dados estruturados, criam embeddings e armazenam-nos numa base de dados vetorial local ou remota.

2. **Consulta em Linguagem Natural (Humano)**: Um utilizador visita o site e, em vez de navegar por menus, escreve numa interface de chat: "Encontra-me um hotel familiar em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe esta consulta. Envia a consulta a um LLM para compreensão e simultaneamente pesquisa a sua base de dados vetorial por listagens de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da pesquisa da base de dados, identifica as melhores correspondências baseadas nos critérios "familiar", "piscina" e "Honolulu", e depois formata uma resposta em linguagem natural. Crucialmente, a resposta refere-se a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação com Agente de IA**: Porque o NLWeb serve como servidor MCP, um agente externo de viagens IA também poderia ligar-se à instância NLWeb deste site. O agente IA poderia usar o método `ask` do MCP para interrogar diretamente o site: `ask("Existem restaurantes vegan-friendly na área de Honolulu recomendados pelo hotel?")`. A instância NLWeb processaria isto, usando a sua base de dados de informação sobre restaurantes (se carregada), e retornaria uma resposta estruturada em JSON.

### Tem Mais Perguntas sobre MCP/A2A/NLWeb?

Junta-te ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrares outros aprendizes, assistires a horas de expediente e obteres respostas às tuas perguntas sobre Agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->