# Uso dos Protocolos Agentic (MCP, A2A e NLWeb)

[![Agentic Protocols](../../../translated_images/pt-PT/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para ver o vídeo desta aula)_

À medida que o uso de agentes de IA cresce, também cresce a necessidade de protocolos que assegurem a normalização, segurança e apoio à inovação aberta. Nesta aula, vamos abordar 3 protocolos que procuram satisfazer esta necessidade - Protocolo de Contexto do Modelo (MCP), Agente para Agente (A2A) e Web de Linguagem Natural (NLWeb).

## Introdução

Nesta aula, vamos cobrir:

• Como o **MCP** permite que Agentes de IA acedam a ferramentas externas e dados para completar tarefas do utilizador.

• Como o **A2A** possibilita a comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces de linguagem natural a qualquer website, permitindo que Agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** o propósito principal e os benefícios do MCP, A2A e NLWeb no contexto dos agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agentic complexos.

## Protocolo de Contexto do Modelo

O **Protocolo de Contexto do Modelo (MCP)** é um padrão aberto que oferece uma forma normalizada para aplicações fornecerem contexto e ferramentas a LLMs. Isto permite um "adaptador universal" para diferentes fontes de dados e ferramentas que os Agentes de IA podem ligar de forma consistente.

Vamos analisar os componentes do MCP, os benefícios em comparação com o uso direto de API, e um exemplo de como agentes de IA podem usar um servidor MCP.

### Componentes Principais do MCP

O MCP opera numa **arquitetura cliente-servidor** e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como VSCode) que iniciam as ligações a um Servidor MCP.

• **Clientes** são componentes dentro da aplicação host que mantêm ligações um-a-um com servidores.

• **Servidores** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas principais que correspondem às capacidades de um Servidor MCP:

• **Ferramentas**: São ações ou funções discretas que um agente de IA pode invocar para realizar uma ação. Por exemplo, um serviço meteorológico pode expor uma ferramenta "obter tempo", ou um servidor de comércio eletrónico pode expor uma ferramenta "comprar produto". Os servidores MCP anunciam o nome, descrição, e esquema de entrada/saída de cada ferramenta na sua listagem de capacidades.

• **Recursos**: São itens de dados apenas de leitura ou documentos que um servidor MCP pode fornecer e que os clientes podem recolher sob demanda. Exemplos incluem conteúdos de ficheiros, registos de base de dados, ou ficheiros de logs. Os recursos podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: São templates predefinidos que fornecem prompts sugeridos, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Os agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor juntamente com descrições do que fazem. Isto contrasta com APIs tradicionais, que frequentemente exigem codificação estática para integrações, significando que qualquer alteração na API necessita de atualizações de código. O MCP oferece uma abordagem "integrar uma vez", conduzindo a maior adaptabilidade.

• **Interoperabilidade entre LLMs**: O MCP funciona com diferentes LLMs, proporcionando flexibilidade para mudar modelos centrais para avaliar melhor desempenho.

• **Segurança Normalizada**: O MCP inclui um método padrão de autenticação, melhorando a escalabilidade ao adicionar acesso a servidores MCP adicionais. Isto é mais simples do que gerir diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo MCP

![Diagrama MCP](../../../translated_images/pt-PT/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine que um utilizador quer reservar um voo usando um assistente de IA alimentado por MCP.

1. **Ligação**: O assistente de IA (o cliente MCP) liga-se a um servidor MCP providenciado por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea: "Que ferramentas têm disponíveis?" O servidor responde com ferramentas como "pesquisar voos" e "reservar voos".

3. **Invocação da Ferramenta**: Depois pede ao assistente de IA: "Por favor, procura um voo de Portland para Honolulu." O assistente de IA, usando o seu LLM, identifica que precisa invocar a ferramenta "pesquisar voos" e passa os parâmetros relevantes (origem, destino) para o servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um invólucro, faz a chamada real à API interna de reservas da companhia aérea. Depois recebe a informação do voo (por exemplo, dados JSON) e envia-a de volta ao assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voo. Uma vez selecionado um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, completando a reserva.

## Protocolo Agente-para-Agente (A2A)

Enquanto o MCP se foca em ligar LLMs a ferramentas, o protocolo **Agente-para-Agente (A2A)** vai um passo mais além ao permitir comunicação e colaboração entre diferentes agentes de IA. O A2A liga agentes de IA através de diferentes organizações, ambientes e stacks tecnológicos para completar uma tarefa partilhada.

Vamos examinar os componentes e benefícios do A2A, junto com um exemplo de como poderia ser aplicado na nossa aplicação de viagens.

### Componentes Principais do A2A

O A2A foca-se em permitir comunicação entre agentes e fazê-los trabalhar juntos para completar uma subtarefa do utilizador. Cada componente do protocolo contribui para isto:

#### Cartão do Agente

Semelhante a como um servidor MCP partilha uma lista de ferramentas, um Cartão do Agente contém:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que completa.
- Uma **lista de competências específicas** com descrições para ajudar outros agentes (ou mesmo utilizadores humanos) a entender quando e porque quereriam invocar esse agente.
- O **URL de Endpoint atual** do agente.
- A **versão** e **capacidades** do agente, como respostas em streaming e notificações push.

#### Executor do Agente

O Executor do Agente é responsável por **passar o contexto da conversa do utilizador para o agente remoto**, que precisa disto para compreender a tarefa a ser concluída. Num servidor A2A, um agente usa o seu próprio Modelo de Linguagem Grande (LLM) para analisar pedidos recebidos e executar tarefas usando as suas próprias ferramentas internas.

#### Artefato

Uma vez que o agente remoto tenha concluído a tarefa solicitada, o seu produto de trabalho é criado como um artefato. Um artefato **contém o resultado do trabalho do agente**, uma **descrição do que foi concluído** e o **contexto textual** que é transmitido através do protocolo. Depois do artefato ser enviado, a ligação com o agente remoto é fechada até ser necessária novamente.

#### Fila de Eventos

Este componente é usado para **gerir atualizações e passar mensagens**. É particularmente importante em produção para sistemas agentic para evitar que a ligação entre agentes seja fechada antes da conclusão de uma tarefa, especialmente quando o tempo de execução pode ser longo.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, compartilhem contexto e trabalhem juntos, facilitando uma automação fluida entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Seleção do Modelo**: Cada agente A2A pode decidir qual LLM usa para atender aos seus pedidos, permitindo modelos otimizados ou ajustados por agente, diferente de uma única ligação LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação está integrada diretamente no protocolo A2A, oferecendo um robusto enquadramento de segurança para as interações dos agentes.

### Exemplo A2A

![Diagrama A2A](../../../translated_images/pt-PT/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir o nosso cenário de reserva de viagens, mas desta vez usando A2A.

1. **Pedido do Utilizador a Multi-Agente**: Um utilizador interage com um cliente/agente A2A "Agente de Viagens", talvez dizendo: "Por favor, reserve uma viagem completa para Honolulu para a próxima semana, incluindo voos, hotel e aluguer de carro".

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe este pedido complexo. Usa o seu LLM para raciocinar sobre a tarefa e determinar que necessita de interagir com outros agentes especializados.

3. **Comunicação Entre Agentes**: O Agente de Viagens usa então o protocolo A2A para contactar agentes inferiores, como um "Agente de Companhia Aérea", um "Agente de Hotel" e um "Agente de Aluguer de Carros" criados por diferentes empresas.

4. **Execução Delegada de Tarefas**: O Agente de Viagens envia tarefas específicas a estes agentes especializados (ex.: "Encontrar voos para Honolulu", "Reservar um hotel", "Alugar um carro"). Cada um destes agentes especializados, executando os seus próprios LLMs e utilizando as suas próprias ferramentas (que podem ser servidores MCP também), executa a sua parte da reserva.

5. **Resposta Consolidada**: Uma vez que todos os agentes inferiores completem as suas tarefas, o Agente de Viagens compila os resultados (detalhes do voo, confirmação do hotel, reserva do aluguer de carro) e envia uma resposta abrangente, em estilo de chat, ao utilizador.

## Web de Linguagem Natural (NLWeb)

Os websites têm sido durante muito tempo a principal forma dos utilizadores acederem a informação e dados na internet.

Vamos olhar para os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como o nosso NLWeb funciona ao observar a nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código do Serviço Central)**: O sistema que processa perguntas em linguagem natural. Conecta as várias partes da plataforma para criar respostas. Pode pensar nele como o **motor que alimenta as funcionalidades de linguagem natural** de um website.

- **Protocolo NLWeb**: Este é um **conjunto básico de regras para interação em linguagem natural** com um website. Envia respostas em formato JSON (frequentemente usando Schema.org). O seu propósito é criar uma base simples para a “Web de IA”, da mesma forma que o HTML tornou possível a partilha de documentos online.

- **Servidor MCP (Endpoint do Protocolo de Contexto do Modelo)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isso significa que pode **partilhar ferramentas (como o método “ask”) e dados** com outros sistemas de IA. Na prática, isto torna o conteúdo e capacidades do website usáveis por agentes de IA, permitindo que o site faça parte do mais amplo “ecossistema de agentes.”

- **Modelos de Embedding**: Estes modelos são usados para **converter o conteúdo do website em representações numéricas chamadas vetores** (embeddings). Estes vetores capturam significado de uma forma que os computadores podem comparar e pesquisar. São armazenados numa base de dados especial, e os utilizadores podem escolher qual modelo de embedding querem usar.

- **Base de Dados Vetorial (Mecanismo de Recuperação)**: Esta base de dados **armazena os embeddings do conteúdo do website**. Quando alguém faz uma pergunta, o NLWeb consulta a base de dados vetorial para encontrar rapidamente a informação mais relevante. Fornece uma lista rápida de possíveis respostas, classificadas por similaridade. O NLWeb funciona com diferentes sistemas de armazenamento vetorial como Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/pt-PT/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere novamente o nosso website de reservas de viagens, mas desta vez, alimentado por NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes no website de viagens (ex.: listas de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via feeds RSS. As ferramentas do NLWeb ingerem estes dados estruturados, criam embeddings e armazenam-nas numa base de dados vetorial local ou remota.

2. **Consulta em Linguagem Natural (Humano)**: Um utilizador visita o website e, em vez de navegar por menus, escreve numa interface de chat: "Encontra um hotel familiar em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe esta consulta. Envia a consulta a um LLM para compreensão e simultaneamente pesquisa na sua base de dados vetorial listas relevantes de hotéis.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da pesquisa da base de dados, identifica as melhores correspondências baseadas nos critérios "familiar", "piscina" e "Honolulu", e depois formata uma resposta em linguagem natural. É fundamental que a resposta se refira a hotéis reais do catálogo do website, evitando informações inventadas.

5. **Interação com Agente de IA**: Como o NLWeb serve como um servidor MCP, um agente externo de viagens de IA também poderia ligar-se à instância NLWeb deste website. O agente IA poderia então usar o método `ask` do MCP para questionar o website diretamente: `ask("Existem restaurantes vegan-friendly na área de Honolulu recomendados pelo hotel?")`. A instância NLWeb processaria isto, valendo-se da sua base de dados de informação sobre restaurantes (se carregada), e retornaria uma resposta estruturada em JSON.

### Tem Mais Perguntas sobre MCP/A2A/NLWeb?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, assistir a horas de atendimento e esclarecer suas dúvidas sobre Agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Framework de Agentes Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

## Aula Anterior

[Agentes de IA em Produção](../10-ai-agents-production/README.md)

## Aula Seguinte

[Engenharia de Contexto para Agentes de IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->