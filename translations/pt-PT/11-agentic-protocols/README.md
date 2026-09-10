# Usar Protocolos Agentes (MCP, A2A e NLWeb)

[![Protocolos Agentes](../../../translated_images/pt-PT/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para ver o vídeo desta aula)_

À medida que o uso de agentes de IA cresce, também cresce a necessidade de protocolos que garantam a padronização, segurança e apoiem a inovação aberta. Nesta aula, iremos cobrir 3 protocolos que procuram satisfazer esta necessidade - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introdução

Nesta aula, iremos cobrir:

• Como o **MCP** permite que os Agentes de IA acedam a ferramentas e dados externos para completar tarefas do utilizador.

• Como o **A2A** possibilita a comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces de linguagem natural para qualquer site, permitindo que os Agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** a finalidade principal e os benefícios do MCP, A2A e NLWeb no contexto dos agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e a interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agentes complexos.

## Model Context Protocol

O **Model Context Protocol (MCP)** é um padrão aberto que fornece uma forma padronizada para aplicações fornecerem contexto e ferramentas a LLMs. Isto permite um "adaptador universal" a diferentes fontes de dados e ferramentas que os Agentes de IA podem conectar de forma consistente.

Vamos analisar os componentes do MCP, os benefícios comparados ao uso direto de API, e um exemplo de como agentes de IA podem usar um servidor MCP.

### Componentes Principais do MCP

O MCP funciona numa **arquitetura cliente-servidor** e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como VSCode) que iniciam as ligações a um Servidor MCP.

• **Clientes** são componentes dentro da aplicação host que mantêm ligações um-para-um com os servidores.

• **Servidores** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas principais que são as capacidades de um Servidor MCP:

• **Ferramentas**: São ações ou funções específicas que um agente de IA pode chamar para executar uma ação. Por exemplo, um serviço de meteorologia pode expor uma ferramenta "obter clima" ou um servidor de comércio eletrónico pode expor uma ferramenta "comprar produto". Os servidores MCP anunciam o nome, descrição e esquema de entrada/saída de cada ferramenta nas suas listagens de capacidades.

• **Recursos**: São itens de dados ou documentos somente de leitura que um servidor MCP pode fornecer, e os clientes podem recuperá-los sob demanda. Exemplos incluem conteúdos de ficheiros, registos de bases de dados, ou ficheiros de log. Os recursos podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: São templates predefinidos que fornecem prompts sugeridos, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para os Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Os agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor junto com descrições do que fazem. Isto contrasta com as APIs tradicionais, que geralmente requerem código estático para integrações, significando que qualquer alteração da API exige atualização do código. O MCP oferece uma abordagem "integra uma vez", levando a maior adaptabilidade.

• **Interoperabilidade entre LLMs**: MCP funciona através de diferentes LLMs, providenciando flexibilidade para alternar modelos centrais para avaliação por melhor desempenho.

• **Segurança Padronizada**: MCP inclui um método padrão de autenticação, melhorando a escalabilidade quando se adiciona acesso a servidores MCP adicionais. Isto é mais simples do que gerir chaves diferentes e tipos de autenticação para várias APIs tradicionais.

### Exemplo MCP

![Diagrama MCP](../../../translated_images/pt-PT/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine que um utilizador quer reservar um voo usando um assistente de IA alimentado por MCP.

1. **Ligação**: O assistente de IA (o cliente MCP) liga-se a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea, "Que ferramentas tens disponíveis?" O servidor responde com ferramentas como "pesquisar voos" e "reservar voos".

3. **Invocação da Ferramenta**: Você pede ao assistente de IA, "Por favor, procura um voo de Portland para Honolulu." O assistente de IA, usando o seu LLM, identifica que precisa chamar a ferramenta "pesquisar voos" e passa os parâmetros relevantes (origem, destino) para o servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um invólucro, faz a chamada real para a API interna de reservas da companhia aérea. Depois recebe a informação do voo (ex., dados JSON) e envia-a de volta para o assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voo. Após selecionar um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, concluindo a reserva.

## Protocolo Agent-to-Agent (A2A)

Enquanto o MCP se foca em conectar LLMs a ferramentas, o **protocolo Agent-to-Agent (A2A)** vai um passo além, permitindo comunicação e colaboração entre diferentes agentes de IA. O A2A conecta agentes de IA através de diferentes organizações, ambientes e tecnologias para completar uma tarefa partilhada.

Iremos analisar componentes e benefícios do A2A, junto com um exemplo de como pode ser aplicado na nossa aplicação de viagens.

### Componentes Principais do A2A

O A2A foca-se em permitir comunicação entre agentes e em fazê-los trabalhar juntos para completar uma subtarefa do utilizador. Cada componente do protocolo contribui para isto:

#### Cartão do Agente

Tal como um servidor MCP partilha uma lista de ferramentas, um Cartão do Agente tem:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que completa.
- Uma **lista de competências específicas** com descrições para ajudar outros agentes (ou mesmo utilizadores humanos) a entender quando e porquê fariam uma chamada a esse agente.
- A **URL do Endpoint atual** do agente.
- A **versão** e **capacidades** do agente como respostas em streaming e notificações push.

#### Executor do Agente

O Executor do Agente é responsável por **passar o contexto do chat do utilizador para o agente remoto**, o agente remoto necessita disto para entender a tarefa a ser completada. Num servidor A2A, um agente usa o seu próprio Large Language Model (LLM) para analisar pedidos recebidos e executar tarefas usando as suas próprias ferramentas internas.

#### Artefacto

Depois de um agente remoto completar a tarefa solicitada, o resultado do seu trabalho é criado como um artefacto. Um artefacto **contém o resultado do trabalho do agente**, uma **descrição do que foi completado**, e o **contexto textual** que é enviado através do protocolo. Após o envio do artefacto, a ligação com o agente remoto é fechada até ser necessária novamente.

#### Fila de Eventos

Este componente é usado para o **tratamento de atualizações e passagem de mensagens**. É especialmente importante em ambientes de produção de sistemas agentes para prevenir que as ligações entre agentes sejam fechadas antes da conclusão da tarefa, especialmente quando a duração das tarefas pode ser elevada.

### Benefícios do A2A

• **Colaboração Melhorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, partilhem contexto e trabalhem juntos, facilitando a automação fluida entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Escolha do Modelo**: Cada agente A2A pode decidir qual LLM utiliza para atender aos seus pedidos, permitindo modelos otimizados ou ajustados por agente, diferente de uma única ligação LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação está integrada diretamente no protocolo A2A, fornecendo uma estrutura robusta de segurança para interações entre agentes.

### Exemplo A2A

![Diagrama A2A](../../../translated_images/pt-PT/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir o nosso cenário de reserva de viagens, mas desta vez usando A2A.

1. **Pedido do Utilizador ao Multi-Agente**: Um utilizador interage com um cliente/agente A2A "Agente de Viagens", talvez dizendo, "Por favor, reserva uma viagem completa para Honolulu para a próxima semana, incluindo voos, hotel e aluguer de carro".

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe este pedido complexo. Usa o seu LLM para raciocinar sobre a tarefa e determinar que precisa interagir com outros agentes especializados.

3. **Comunicação Entre Agentes**: O Agente de Viagens usa então o protocolo A2A para conectar aos agentes de jusante, como "Agente da Companhia Aérea", "Agente de Hotel" e "Agente de Aluguer de Carros" criados por diferentes empresas.

4. **Execução Delegada de Tarefas**: O Agente de Viagens envia tarefas específicas a estes agentes especializados (ex., "Encontrar voos para Honolulu", "Reservar um hotel", "Alugar um carro"). Cada um destes agentes especializados, executando os seus próprios LLMs e utilizando as suas próprias ferramentas (que poderiam ser servidores MCP), realiza a sua parte específica da reserva.

5. **Resposta Consolidada**: Uma vez que todos os agentes de jusante completem as suas tarefas, o Agente de Viagens compila os resultados (detalhes do voo, confirmação do hotel, reserva do aluguer do carro) e envia uma resposta abrangente, em estilo de chat, de volta ao utilizador.

## Natural Language Web (NLWeb)

Os websites têm sido há muito o principal meio para utilizadores acederem a informações e dados pela internet.

Vamos olhar para os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como o nosso NLWeb funciona ao analisar a nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código do Serviço Principal)**: O sistema que processa perguntas em linguagem natural. Liga as diferentes partes da plataforma para criar respostas. Pode considerá-lo como o **motor que alimenta as funcionalidades de linguagem natural** de um site.

- **Protocolo NLWeb**: É um **conjunto básico de regras para interação em linguagem natural** com um site. Envia respostas em formato JSON (frequentemente usando Schema.org). O seu propósito é criar um fundamento simples para a “Web de IA”, da mesma forma que o HTML tornou possível partilhar documentos online.

- **Servidor MCP (Endpoint do Model Context Protocol)**: Cada instalação NLWeb também funciona como servidor MCP. Isto significa que pode **partilhar ferramentas (como um método "ask") e dados** com outros sistemas de IA. Na prática, isto torna o conteúdo e capacidades do site utilizáveis por agentes de IA, permitindo que o site se torne parte do ecossistema mais amplo de agentes.

- **Modelos de Embedding**: Estes modelos são usados para **converter conteúdo do site em representações numéricas chamadas vetores** (embeddings). Estes vetores capturam significado de uma forma que os computadores podem comparar e pesquisar. São guardados numa base de dados especial, e os utilizadores podem escolher qual modelo de embedding querem usar.

- **Base de Dados Vetorial (Mecanismo de Recuperação)**: Esta base de dados **armazena os embeddings do conteúdo do site**. Quando alguém faz uma pergunta, o NLWeb verifica a base de dados vetorial para encontrar rapidamente a informação mais relevante. Fornece uma lista rápida de possíveis respostas, ordenadas por similaridade. O NLWeb funciona com diferentes sistemas de armazenamento vetorial como Qdrant, Snowflake, Milvus, Azure AI Search, e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/pt-PT/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere novamente o nosso site de reserva de viagens, mas desta vez, é alimentado pelo NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes do site de viagens (ex., listas de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados através de RSS feeds. As ferramentas do NLWeb ingerem estes dados estruturados, criam embeddings e armazenam-nos numa base de dados vetorial local ou remota.

2. **Consulta em Linguagem Natural (Humano)**: Um utilizador visita o site e, invés de navegar por menus, escreve numa interface de chat: "Encontra-me um hotel para famílias em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe esta consulta. Envia a consulta para um LLM para entendimento e simultaneamente pesquisa na sua base de dados vetorial as listas de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da pesquisa da base de dados, identifica as melhores correspondências baseando-se nos critérios "familiar", "piscina" e "Honolulu", e formata uma resposta em linguagem natural. Crucialmente, a resposta refere-se a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação do Agente de IA**: Porque o NLWeb serve como servidor MCP, um agente de viagens externo de IA pode também ligar-se a esta instância NLWeb do site. O agente IA poderia então usar o método `ask` do MCP para consultar diretamente o site: `ask("Há restaurantes vegan-friendly recomendados pelo hotel na área de Honolulu?")`. A instância NLWeb processaria isto, aproveitando a sua base de dados de informações de restaurantes (se carregada), e retornaria uma resposta estruturada JSON.

### Tem mais perguntas sobre MCP/A2A/NLWeb?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros estudantes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos

- [MCP para Principiantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Aula Anterior

[Agentes de IA em Produção](../10-ai-agents-production/README.md)

## Próxima Aula

[Engenharia de Contexto para Agentes de IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->