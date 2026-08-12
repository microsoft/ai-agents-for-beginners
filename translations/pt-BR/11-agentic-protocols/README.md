# Usando Protocolos Agentic (MCP, A2A e NLWeb)

[![Protocolos Agentic](../../../translated_images/pt-BR/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

À medida que o uso de agentes de IA cresce, cresce também a necessidade de protocolos que garantam padronização, segurança e suporte à inovação aberta. Nesta lição, vamos cobrir 3 protocolos que buscam atender a essa necessidade - Protocolo de Contexto de Modelo (MCP), Agente para Agente (A2A) e Web de Linguagem Natural (NLWeb).

## Introdução

Nesta lição, vamos abordar:

• Como o **MCP** permite que Agentes de IA acessem ferramentas externas e dados para completar tarefas do usuário.

• Como o **A2A** possibilita a comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces em linguagem natural para qualquer site, permitindo que Agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** o propósito central e os benefícios do MCP, A2A e NLWeb no contexto de agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e a interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agentic complexos.

## Protocolo de Contexto de Modelo

O **Protocolo de Contexto de Modelo (MCP)** é um padrão aberto que fornece uma maneira padronizada para aplicações proverem contexto e ferramentas para LLMs. Isso possibilita um "adaptador universal" para diferentes fontes de dados e ferramentas às quais os Agentes de IA podem se conectar de forma consistente.

Vamos analisar os componentes do MCP, os benefícios em comparação com o uso direto de API, e um exemplo de como agentes de IA podem usar um servidor MCP.

### Componentes Principais do MCP

O MCP opera em uma **arquitetura cliente-servidor** e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como o VSCode) que iniciam conexões com um Servidor MCP.

• **Clients** são componentes dentro da aplicação host que mantêm conexões um-para-um com servidores.

• **Servers** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas principais, que são as capacidades de um Servidor MCP:

• **Ferramentas**: São ações ou funções discretas que um agente de IA pode chamar para executar uma ação. Por exemplo, um serviço de clima pode expor uma ferramenta "obter clima", ou um servidor de comércio eletrônico pode expor uma ferramenta "comprar produto". Servidores MCP anunciam o nome de cada ferramenta, descrição e esquema de entrada/saída em sua lista de capacidades.

• **Recursos**: São itens de dados ou documentos somente leitura que um servidor MCP pode fornecer, e os clientes podem obtê-los sob demanda. Exemplos incluem conteúdo de arquivos, registros de banco de dados ou arquivos de log. Recursos podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: São modelos predefinidos que oferecem prompts sugeridos, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Os agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor junto com descrições do que elas fazem. Isso contrasta com APIs tradicionais, que frequentemente requerem codificação estática para integrações, significando que qualquer alteração na API exige atualização de código. O MCP oferece uma abordagem "integre uma vez", levando a maior adaptabilidade.

• **Interoperabilidade entre LLMs**: MCP funciona com diferentes LLMs, proporcionando flexibilidade para trocar modelos principais para avaliação de melhor desempenho.

• **Segurança Padronizada**: MCP inclui um método padrão de autenticação, melhorando a escalabilidade ao adicionar acesso a múltiplos servidores MCP. Isso é mais simples do que gerenciar diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo MCP

![Diagrama MCP](../../../translated_images/pt-BR/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine que um usuário deseja reservar um voo usando um assistente de IA alimentado pelo MCP.

1. **Conexão**: O assistente de IA (o cliente MCP) conecta-se a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea: "Quais ferramentas vocês têm disponíveis?" O servidor responde com ferramentas como "buscar voos" e "reservar voos".

3. **Invocação da Ferramenta**: Você então pede ao assistente de IA: "Por favor, procure um voo de Portland para Honolulu." O assistente de IA, usando seu LLM, identifica que precisa chamar a ferramenta "buscar voos" e passa os parâmetros relevantes (origem, destino) ao servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um wrapper, faz a chamada real para a API interna de reservas da companhia aérea. Ele então recebe as informações do voo (por exemplo, dados JSON) e as envia de volta ao assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voo. Uma vez que você selecione um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, completando a reserva.

## Protocolo Agente para Agente (A2A)

Enquanto o MCP foca em conectar LLMs a ferramentas, o **protocolo Agente para Agente (A2A)** vai além, permitindo comunicação e colaboração entre diferentes agentes de IA. A2A conecta agentes de IA em diferentes organizações, ambientes e pilhas tecnológicas para completar uma tarefa compartilhada.

Vamos examinar os componentes e os benefícios do A2A, junto com um exemplo de como ele poderia ser aplicado em nossa aplicação de viagens.

### Componentes Principais do A2A

A2A foca em possibilitar comunicação entre agentes e fazer com que eles trabalhem juntos para completar uma subtarefa do usuário. Cada componente do protocolo contribui para isso:

#### Cartão do Agente

Semelhante a como um servidor MCP compartilha uma lista de ferramentas, um Cartão do Agente tem:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que ele realiza.
- Uma **lista de habilidades específicas** com descrições para ajudar outros agentes (ou até usuários humanos) a entender quando e por que eles deveriam chamar esse agente.
- A **URL do Endpoint atual** do agente.
- A **versão** e as **capacidades** do agente, como respostas em streaming e notificações push.

#### Executor do Agente

O Executor do Agente é responsável por **passar o contexto da conversa do usuário para o agente remoto**, que precisa disso para entender a tarefa a ser completada. Em um servidor A2A, o agente usa seu próprio Modelo de Linguagem Grande (LLM) para interpretar solicitações recebidas e executar tarefas usando suas próprias ferramentas internas.

#### Artefato

Uma vez que o agente remoto tenha completado a tarefa solicitada, seu produto de trabalho é criado como um artefato. Um artefato **contém o resultado do trabalho do agente**, uma **descrição do que foi completado** e o **contexto textual** enviado pelo protocolo. Após o artefato ser enviado, a conexão com o agente remoto é encerrada até que seja necessária novamente.

#### Fila de Eventos

Este componente é usado para **manipular atualizações e transmitir mensagens**. É especialmente importante em produção para sistemas agentic para evitar que a conexão entre agentes seja encerrada antes da conclusão de uma tarefa, principalmente quando o tempo para completar a tarefa pode ser longo.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, compartilhem contexto e trabalhem juntos, facilitando automação contínua entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Seleção de Modelos**: Cada agente A2A pode decidir qual LLM usa para atender suas solicitações, permitindo otimização ou ajuste fino de modelos por agente, diferente de uma única conexão LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação é integrada diretamente no protocolo A2A, fornecendo uma estrutura robusta de segurança para interações entre agentes.

### Exemplo de A2A

![Diagrama A2A](../../../translated_images/pt-BR/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir nosso cenário de reserva de viagem, mas desta vez utilizando A2A.

1. **Solicitação do Usuário para Multi-Agentes**: Um usuário interage com um cliente/agente A2A "Agente de Viagens", talvez dizendo: "Por favor, reserve uma viagem completa para Honolulu na próxima semana, incluindo voos, hotel e aluguel de carro".

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe essa solicitação complexa. Ele usa seu LLM para raciocinar sobre a tarefa e determinar que precisa interagir com outros agentes especializados.

3. **Comunicação entre Agentes**: O Agente de Viagens usa então o protocolo A2A para conectar-se a agentes downstream, como um "Agente de Companhia Aérea", um "Agente de Hotel" e um "Agente de Aluguel de Carro" criados por diferentes empresas.

4. **Execução Delegada de Tarefas**: O Agente de Viagens envia tarefas específicas para esses agentes especializados (por exemplo, "Encontrar voos para Honolulu", "Reservar um hotel", "Alugar um carro"). Cada um desses agentes especializados, rodando seus próprios LLMs e utilizando suas próprias ferramentas (que podem ser servidores MCP), realiza sua parte específica da reserva.

5. **Resposta Consolidada**: Quando todos os agentes downstream completam suas tarefas, o Agente de Viagens compila os resultados (detalhes do voo, confirmação do hotel, reserva do aluguel de carro) e envia uma resposta abrangente, no estilo de chat, de volta ao usuário.

## Web de Linguagem Natural (NLWeb)

Sites da web há muito são a principal forma de os usuários acessarem informações e dados pela internet.

Vamos ver os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como nossa NLWeb funciona ao observar nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código do Serviço Principal)**: O sistema que processa perguntas em linguagem natural. Ele conecta as diferentes partes da plataforma para criar respostas. Pode-se pensar nele como o **motor que alimenta os recursos de linguagem natural** de um site.

- **Protocolo NLWeb**: É um **conjunto básico de regras para interação em linguagem natural** com um site. Ele responde em formato JSON (frequentemente usando Schema.org). Seu propósito é criar uma base simples para a “Web de IA”, da mesma forma que o HTML possibilitou compartilhar documentos online.

- **Servidor MCP (Endpoint do Protocolo de Contexto de Modelo)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isso significa que pode **compartilhar ferramentas (como o método “ask”) e dados** com outros sistemas de IA. Na prática, isso torna o conteúdo e as capacidades do site utilizáveis por agentes de IA, permitindo que o site faça parte do “ecossistema de agentes”.

- **Modelos de Embedding**: Esses modelos são usados para **converter o conteúdo do site em representações numéricas chamadas vetores** (embeddings). Esses vetores capturam significado de forma que os computadores podem comparar e buscar. Eles são armazenados em um banco de dados especial, e os usuários podem escolher qual modelo de embedding desejam usar.

- **Banco de Dados Vetorial (Mecanismo de Recuperação)**: Este banco armazena os embeddings do conteúdo do site. Quando alguém faz uma pergunta, o NLWeb consulta o banco de dados vetorial para encontrar rapidamente a informação mais relevante. Ele fornece uma lista rápida de possíveis respostas, classificadas por similaridade. NLWeb funciona com diferentes sistemas de armazenamento vetorial, como Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/pt-BR/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere novamente nosso site de reservas de viagem, mas desta vez alimentado pelo NLWeb.

1. **Ingestão de Dados**: Os catálogos existentes do site de viagens (ex., listas de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via RSS feeds. As ferramentas do NLWeb ingerem esses dados estruturados, criam embeddings e os armazenam em um banco de dados vetorial local ou remoto.

2. **Consulta em Linguagem Natural (Humano)**: Um usuário visita o site e, em vez de navegar por menus, digita em uma interface de chat: "Encontre um hotel para família em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe essa consulta. Envia a consulta para um LLM para compreensão e simultaneamente busca em seu banco de dados vetorial as listagens de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da busca no banco de dados, identifica as melhores correspondências baseadas nos critérios "para famílias", "piscina" e "Honolulu" e então formata uma resposta em linguagem natural. De maneira crucial, a resposta refere-se a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação com Agentes de IA**: Como o NLWeb serve como um servidor MCP, um agente externo de viagens de IA também poderia conectar-se a essa instância NLWeb do site. O agente poderia então usar o método `ask` do MCP para consultar o site diretamente: `ask("Existem restaurantes veganos recomendados na área de Honolulu pelo hotel?")`. A instância NLWeb processaria isso, aproveitando seu banco de dados de informações de restaurantes (se carregado), e retornaria uma resposta estruturada em JSON.

### Tem Mais Perguntas sobre MCP/A2A/NLWeb?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar de horas de plantão e esclarecer suas dúvidas sobre Agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Lição Anterior

[Agentes de IA em Produção](../10-ai-agents-production/README.md)

## Próxima Lição

[Engenharia de Contexto para Agentes de IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->