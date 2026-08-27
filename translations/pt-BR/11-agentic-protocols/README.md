# Usando Protocolos Agentes (MCP, A2A e NLWeb)

[![Agentic Protocols](../../../translated_images/pt-BR/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

À medida que o uso de agentes de IA cresce, também cresce a necessidade de protocolos que garantam padronização, segurança e apoiem a inovação aberta. Nesta lição, abordaremos 3 protocolos que buscam atender essa necessidade - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introdução

Nesta lição, abordaremos:

• Como o **MCP** permite que Agentes de IA acessem ferramentas e dados externos para completar tarefas do usuário.

• Como o **A2A** permite comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces em linguagem natural para qualquer site, permitindo que agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** o propósito central e os benefícios do MCP, A2A e NLWeb no contexto de agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agenticos complexos.

## Model Context Protocol

O **Model Context Protocol (MCP)** é um padrão aberto que fornece uma forma padronizada para aplicações fornecerem contexto e ferramentas para LLMs. Isso possibilita um "adaptador universal" para diferentes fontes de dados e ferramentas que agentes de IA podem se conectar de maneira consistente.

Vamos analisar os componentes do MCP, os benefícios comparados ao uso direto de APIs, e um exemplo de como agentes de IA podem usar um servidor MCP.

### Componentes Centrais do MCP

O MCP opera em uma **arquitetura cliente-servidor** e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como VSCode) que iniciam as conexões com um servidor MCP.

• **Clientes** são componentes dentro da aplicação host que mantêm conexões one-to-one com servidores.

• **Servidores** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas principais, que são as capacidades de um Servidor MCP:

• **Ferramentas**: Estas são ações ou funções discretas que um agente de IA pode chamar para executar uma tarefa. Por exemplo, um serviço meteorológico pode expor uma ferramenta "obter clima", ou um servidor de comércio eletrônico pode expor uma ferramenta "comprar produto". Servidores MCP anunciam o nome, descrição e esquema de entrada/saída de cada ferramenta em sua listagem de capacidades.

• **Recursos**: Estes são itens de dados ou documentos somente leitura que um servidor MCP pode fornecer, e que clientes podem recuperar sob demanda. Exemplos incluem conteúdos de arquivos, registros de banco de dados ou arquivos de log. Recursos podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: São templates pré-definidos que fornecem sugestões de prompts, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor junto com descrições do que elas fazem. Isso contrasta com APIs tradicionais, que frequentemente requerem codificação estática para integrações, significando que qualquer mudança na API necessita de atualização de código. O MCP oferece uma abordagem "integre uma vez", levando a maior adaptabilidade.

• **Interoperabilidade entre LLMs**: O MCP funciona com diferentes LLMs, fornecendo flexibilidade para trocar modelos principais para avaliar desempenho melhor.

• **Segurança Padronizada**: O MCP inclui um método padrão de autenticação, melhorando a escalabilidade ao adicionar acesso a servidores MCP adicionais. Isso é mais simples do que gerenciar diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo de MCP

![MCP Diagram](../../../translated_images/pt-BR/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine um usuário que deseja reservar um voo usando um assistente de IA baseado no MCP.

1. **Conexão**: O assistente de IA (o cliente MCP) conecta-se a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea, "Quais ferramentas você tem disponíveis?" O servidor responde com ferramentas como "buscar voos" e "reservar voos".

3. **Invocação de Ferramenta**: Você então pede ao assistente de IA: "Por favor, pesquise um voo de Portland para Honolulu." O assistente de IA, usando seu LLM, identifica que precisa chamar a ferramenta "buscar voos" e passa os parâmetros relevantes (origem, destino) para o servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um invólucro, faz a chamada real para a API interna de reservas da companhia aérea. Ele recebe as informações do voo (por exemplo, dados JSON) e as envia de volta ao assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voo. Uma vez que você seleciona um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, completando a reserva.

## Protocolo Agente-para-Agente (A2A)

Enquanto o MCP foca em conectar LLMs a ferramentas, o **protocolo Agent-to-Agent (A2A)** vai um passo além, possibilitando comunicação e colaboração entre diferentes agentes de IA. O A2A conecta agentes de IA de diferentes organizações, ambientes e tecnologias para completar uma tarefa compartilhada.

Examinaremos os componentes e benefícios do A2A, junto com um exemplo de como ele pode ser aplicado em nossa aplicação de viagens.

### Componentes Centrais do A2A

O A2A foca em habilitar comunicação entre agentes e fazê-los trabalhar juntos para completar uma subtarefa do usuário. Cada componente do protocolo contribui para isso:

#### Cartão do Agente

Semelhante a como um servidor MCP compartilha uma lista de ferramentas, um Cartão do Agente contém:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que ele completa.
- Uma **lista de habilidades específicas** com descrições para ajudar outros agentes (ou até usuários humanos) a entender quando e por que chamariam esse agente.
- A **URL do Endpoint atual** do agente
- A **versão** e **capacidades** do agente, como respostas em streaming e notificações push.

#### Executor do Agente

O Executor do Agente é responsável por **passar o contexto do chat do usuário para o agente remoto**, o agente remoto precisa disso para entender a tarefa que precisa ser concluída. Em um servidor A2A, um agente usa seu próprio Modelo de Linguagem Grande (LLM) para analisar as requisições recebidas e executar tarefas usando suas próprias ferramentas internas.

#### Artefato

Uma vez que o agente remoto completa a tarefa solicitada, seu produto de trabalho é criado como um artefato. Um artefato **contém o resultado do trabalho do agente**, uma **descrição do que foi concluído** e o **contexto de texto** que é enviado pelo protocolo. Depois que o artefato é enviado, a conexão com o agente remoto é encerrada até ser necessária novamente.

#### Fila de Eventos

Este componente é utilizado para **lidar com atualizações e repassar mensagens**. É particularmente importante em ambientes de produção para sistemas agenticos para evitar que a conexão entre agentes seja fechada antes da tarefa ser concluída, especialmente quando a conclusão pode levar mais tempo.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, compartilhem contexto e trabalhem juntos, facilitando automação integrada entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Seleção de Modelo**: Cada agente A2A pode decidir qual LLM utilizar para atender suas solicitações, permitindo modelos otimizados ou ajustados para cada agente, diferente de uma única conexão LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação é incorporada diretamente ao protocolo A2A, fornecendo uma estrutura robusta de segurança para interações entre agentes.

### Exemplo de A2A

![A2A Diagram](../../../translated_images/pt-BR/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir nosso cenário de reserva de viagens, mas desta vez usando A2A.

1. **Solicitação do Usuário para Multi-Agente**: Um usuário interage com um cliente/agente A2A "Agente de Viagens", talvez dizendo: "Por favor, reserve uma viagem inteira para Honolulu na próxima semana, incluindo voos, hotel e aluguel de carro".

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe esta solicitação complexa. Usa seu LLM para raciocinar sobre a tarefa e determina que precisa interagir com outros agentes especializados.

3. **Comunicação Entre Agentes**: Em seguida, o Agente de Viagens usa o protocolo A2A para conectar-se a agentes downstream, como um "Agente de Companhia Aérea", um "Agente de Hotel" e um "Agente de Locadora de Carros" criados por diferentes empresas.

4. **Execução Delegada de Tarefas**: O Agente de Viagens envia tarefas específicas para esses agentes especializados (ex., "Encontre voos para Honolulu", "Reserve um hotel", "Alugue um carro"). Cada um desses agentes especializados, executando seus próprios LLMs e utilizando suas próprias ferramentas (que podem ser servidores MCP), realiza sua parte da reserva.

5. **Resposta Consolidada**: Uma vez que todos os agentes downstream concluem suas tarefas, o Agente de Viagens compila os resultados (detalhes do voo, confirmação do hotel, reserva do carro) e envia uma resposta abrangente em estilo chat para o usuário.

## Natural Language Web (NLWeb)

Sites da web há muito tempo são a principal forma de os usuários acessarem informações e dados na internet.

Vamos olhar para os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como nosso NLWeb funciona observando nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código do Serviço Central)**: O sistema que processa perguntas em linguagem natural. Ele conecta diferentes partes da plataforma para criar respostas. Pode ser visto como o **motor que alimenta as funcionalidades de linguagem natural** de um site.

- **Protocolo NLWeb**: É um **conjunto básico de regras para interação em linguagem natural** com um site. Responde em formato JSON (frequentemente usando Schema.org). Seu propósito é criar uma base simples para a "Web IA", da mesma forma que o HTML tornou possível compartilhar documentos online.

- **Servidor MCP (Endpoint do Model Context Protocol)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isso significa que pode **compartilhar ferramentas (como um método “ask”) e dados** com outros sistemas de IA. Na prática, isso torna o conteúdo e as capacidades do site utilizáveis por agentes de IA, permitindo que o site se torne parte do “ecossistema de agentes” mais amplo.

- **Modelos de Embeddings**: Esses modelos são usados para **converter o conteúdo do site em representações numéricas chamadas vetores** (embeddings). Esses vetores capturam o significado de forma que os computadores podem comparar e buscar. São armazenados em um banco de dados especial, e os usuários podem escolher qual modelo de embedding desejam usar.

- **Banco de Dados Vetorial (Mecanismo de Recuperação)**: Esse banco **armazenas os embeddings do conteúdo do site**. Quando alguém faz uma pergunta, o NLWeb consulta o banco vetorial para rapidamente encontrar a informação mais relevante. Fornece uma lista rápida de possíveis respostas, classificadas por similaridade. NLWeb funciona com diferentes sistemas de armazenamento vetorial, como Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/pt-BR/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere novamente nosso site de reserva de viagens, mas desta vez ele é alimentado pelo NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes do site de viagens (ex., listagens de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via feeds RSS. As ferramentas do NLWeb ingerem esses dados estruturados, criam embeddings e os armazenam em um banco de dados vetorial local ou remoto.

2. **Consulta em Linguagem Natural (Humano)**: Um usuário visita o site e, ao invés de navegar por menus, digita numa interface de chat: "Encontre um hotel para famílias em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe essa consulta. Envia a consulta para um LLM entender e simultaneamente busca em seu banco vetorial por listagens de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da busca no banco de dados, identificar as melhores correspondências com base nos critérios "para famílias", "piscina" e "Honolulu", e formata uma resposta em linguagem natural. Crucialmente, a resposta se refere a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação do Agente de IA**: Como o NLWeb serve como servidor MCP, um agente de viagens de IA externo também pode conectar-se à instância NLWeb deste site. O agente de IA poderia então usar o método `ask` do MCP para consultar diretamente o site: `ask("Existem restaurantes veganos recomendados pelo hotel na área de Honolulu?")`. A instância NLWeb processaria isso, aproveitando seu banco de dados de informações de restaurantes (se carregado), e retornaria uma resposta JSON estruturada.

### Tem Mais Perguntas sobre MCP/A2A/NLWeb?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Lição Anterior

[Agentes de IA em Produção](../10-ai-agents-production/README.md)

## Próxima Lição

[Engenharia de Contexto para Agentes IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->