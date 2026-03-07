# Usando Protocolos Agênicos (MCP, A2A e NLWeb)

[![Protocolos Agênicos](../../../translated_images/pt-BR/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

À medida que o uso de agentes de IA cresce, também cresce a necessidade de protocolos que garantam padronização, segurança e incentivem a inovação aberta. Nesta lição, vamos cobrir 3 protocolos que buscam atender a essa necessidade - Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introdução

Nesta lição, vamos cobrir:

• Como o **MCP** permite que Agentes de IA acessem ferramentas e dados externos para completar tarefas dos usuários.

• Como o **A2A** possibilita comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces em linguagem natural para qualquer site, permitindo que Agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizado

• **Identificar** o propósito central e os benefícios do MCP, A2A e NLWeb no contexto de agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agênicos complexos.

## Model Context Protocol

O **Model Context Protocol (MCP)** é um padrão aberto que fornece uma forma padronizada para aplicações fornecerem contexto e ferramentas aos LLMs. Isso possibilita um "adaptador universal" para diferentes fontes de dados e ferramentas às quais Agentes de IA podem se conectar de maneira consistente.

Vamos ver os componentes do MCP, os benefícios em comparação com o uso direto de APIs e um exemplo de como agentes de IA podem usar um servidor MCP.

### Componentes Centrais do MCP

O MCP opera em uma **arquitetura cliente-servidor** e os componentes centrais são:

• **Hosts** são aplicações de LLM (por exemplo um editor de código como o VSCode) que iniciam as conexões com um Servidor MCP.

• **Clients** são componentes dentro da aplicação host que mantêm conexões um-a-um com servidores.

• **Servers** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas centrais que são as capacidades de um Servidor MCP:

• **Tools**: São ações ou funções discretas que um agente de IA pode chamar para executar uma ação. Por exemplo, um serviço meteorológico pode expor uma ferramenta "get weather", ou um servidor de e-commerce pode expor uma ferramenta "purchase product". Servidores MCP anunciam o nome de cada ferramenta, descrição e o esquema de entrada/saída em sua listagem de capacidades.

• **Resources**: São itens de dados ou documentos somente leitura que um servidor MCP pode fornecer, e os clients podem recuperá-los sob demanda. Exemplos incluem conteúdos de arquivos, registros de banco de dados ou arquivos de log. Resources podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: São modelos predefinidos que fornecem prompts sugeridos, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para Agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor junto com descrições do que elas fazem. Isso contrasta com APIs tradicionais, que frequentemente exigem codificação estática para integrações, significando que qualquer alteração na API exige atualizações de código. O MCP oferece uma abordagem de "integre uma vez", levando a maior adaptabilidade.

• **Interoperabilidade entre LLMs**: O MCP funciona com diferentes LLMs, fornecendo flexibilidade para trocar modelos centrais para avaliar melhor desempenho.

• **Segurança Padronizada**: O MCP inclui um método padrão de autenticação, melhorando a escalabilidade ao adicionar acesso a servidores MCP adicionais. Isso é mais simples do que gerenciar diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo de MCP

![Diagrama MCP](../../../translated_images/pt-BR/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine que um usuário queira reservar um voo usando um assistente de IA alimentado por MCP.

1. **Conexão**: O assistente de IA (o cliente MCP) se conecta a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O client pergunta ao servidor MCP da companhia aérea: "Quais ferramentas vocês têm disponíveis?" O servidor responde com ferramentas como "search flights" e "book flights".

3. **Invocação da Ferramenta**: Você então pede ao assistente de IA: "Por favor, procure um voo de Portland para Honolulu." O assistente de IA, usando seu LLM, identifica que precisa chamar a ferramenta "search flights" e passa os parâmetros relevantes (origem, destino) ao servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um wrapper, faz a chamada real à API interna de reservas da companhia aérea. Em seguida, recebe as informações do voo (por exemplo, dados JSON) e as envia de volta ao assistente de IA.

5. **Interação Posterior**: O assistente de IA apresenta as opções de voo. Uma vez que você seleciona um voo, o assistente pode invocar a ferramenta "book flight" no mesmo servidor MCP, completando a reserva.

## Agent-to-Agent Protocol (A2A)

Enquanto o MCP foca em conectar LLMs a ferramentas, o **Agent-to-Agent (A2A) protocol** dá um passo adiante ao permitir comunicação e colaboração entre diferentes agentes de IA. O A2A conecta agentes de IA entre diferentes organizações, ambientes e pilhas tecnológicas para completar uma tarefa compartilhada.

Vamos examinar os componentes e benefícios do A2A, junto com um exemplo de como ele poderia ser aplicado em nossa aplicação de viagens.

### Componentes Centrais do A2A

O A2A foca em permitir comunicação entre agentes e fazê-los trabalhar juntos para completar uma subtarefa do usuário. Cada componente do protocolo contribui para isso:

#### Agent Card

Semelhante a como um servidor MCP compartilha uma lista de ferramentas, um Agent Card possui:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que ele realiza.
- Uma **lista de habilidades específicas** com descrições para ajudar outros agentes (ou até usuários humanos) a entender quando e por que eles quereriam chamar esse agente.
- A **URL do Endpoint atual** do agente
- A **versão** e as **capacidades** do agente, como respostas em streaming e notificações push.

#### Agent Executor

O Agent Executor é responsável por **passar o contexto do chat do usuário para o agente remoto**, o agente remoto precisa disso para entender a tarefa que precisa ser completada. Em um servidor A2A, um agente usa seu próprio Large Language Model (LLM) para analisar requisições recebidas e executar tarefas usando suas próprias ferramentas internas.

#### Artifact

Uma vez que um agente remoto concluiu a tarefa solicitada, seu produto de trabalho é criado como um artifact. Um artifact **contém o resultado do trabalho do agente**, uma **descrição do que foi completado**, e o **contexto de texto** que é enviado através do protocolo. Após o envio do artifact, a conexão com o agente remoto é encerrada até que seja necessária novamente.

#### Event Queue

Esse componente é usado para **lidar com atualizações e passar mensagens**. É particularmente importante em produção para sistemas agênicos para evitar que a conexão entre agentes seja fechada antes que uma tarefa seja concluída, especialmente quando os tempos de conclusão de tarefas podem ser mais longos.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, compartilhem contexto e trabalhem juntos, facilitando automação contínua através de sistemas tradicionalmente desconectados.

• **Flexibilidade de Seleção de Modelo**: Cada agente A2A pode decidir qual LLM usa para atender suas requisições, permitindo modelos otimizados ou ajustados por agente, ao contrário de uma única conexão LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação é integrada diretamente ao protocolo A2A, fornecendo uma estrutura de segurança robusta para interações entre agentes.

### Exemplo de A2A

![Diagrama A2A](../../../translated_images/pt-BR/A2A-Diagram.8666928d648acc26.webp)

Vamos expandir nosso cenário de reserva de viagem, mas desta vez usando A2A.

1. **Requisição do Usuário para Multi-Agente**: Um usuário interage com um agente/cliente A2A "Travel Agent", talvez dizendo: "Por favor, reserve uma viagem inteira para Honolulu na próxima semana, incluindo voos, um hotel e um carro alugado".

2. **Orquestração pelo Travel Agent**: O Travel Agent recebe essa solicitação complexa. Ele usa seu LLM para raciocinar sobre a tarefa e determinar que precisa interagir com outros agentes especializados.

3. **Comunicação Inter-Agentes**: O Travel Agent então usa o protocolo A2A para conectar-se a agentes a jusante, como um "Airline Agent", um "Hotel Agent" e um "Car Rental Agent" criados por diferentes empresas.

4. **Execução Delegada de Tarefas**: O Travel Agent envia tarefas específicas a esses agentes especializados (por exemplo, "Encontrar voos para Honolulu", "Reservar um hotel", "Alugar um carro"). Cada um desses agentes especializados, executando seus próprios LLMs e utilizando suas próprias ferramentas (que poderiam ser servidores MCP), realiza sua parte específica da reserva.

5. **Resposta Consolidada**: Uma vez que todos os agentes a jusante completam suas tarefas, o Travel Agent compila os resultados (detalhes do voo, confirmação do hotel, reserva do carro) e envia uma resposta abrangente, em estilo de chat, de volta ao usuário.

## Natural Language Web (NLWeb)

Sites há muito tempo são a forma primária para usuários acessarem informações e dados na internet.

Vamos olhar para os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como nosso NLWeb funciona ao olhar para nossa aplicação de viagens.

### Componentes do NLWeb

- **NLWeb Application (Core Service Code)**: O sistema que processa perguntas em linguagem natural. Conecta as diferentes partes da plataforma para criar respostas. Você pode pensar nisso como o **motor que alimenta os recursos em linguagem natural** de um site.

- **NLWeb Protocol**: Este é um **conjunto básico de regras para interação em linguagem natural** com um site. Ele envia respostas em formato JSON (frequentemente usando Schema.org). Seu propósito é criar uma base simples para a "AI Web", da mesma forma que o HTML possibilitou compartilhar documentos online.

- **MCP Server (Model Context Protocol Endpoint)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isso significa que ele pode **compartilhar ferramentas (como um método “ask”) e dados** com outros sistemas de IA. Na prática, isso torna o conteúdo e as capacidades do site utilizáveis por agentes de IA, permitindo que o site se torne parte do ecossistema mais amplo de agentes.

- **Embedding Models**: Esses modelos são usados para **converter o conteúdo do site em representações numéricas chamadas vetores** (embeddings). Esses vetores capturam significado de uma forma que computadores podem comparar e pesquisar. Eles são armazenados em um banco de dados especial, e os usuários podem escolher qual modelo de embedding desejam usar.

- **Vector Database (Retrieval Mechanism)**: Esse banco de dados **armazena os embeddings do conteúdo do site**. Quando alguém faz uma pergunta, o NLWeb verifica o banco de dados vetorial para encontrar rapidamente as informações mais relevantes. Ele retorna uma lista rápida de possíveis respostas, ranqueadas por similaridade. NLWeb funciona com diferentes sistemas de armazenamento vetorial como Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/pt-BR/nlweb-diagram.c1e2390b310e5fe4.webp)

Considere novamente nosso site de reservas de viagem, mas desta vez, ele é alimentado por NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes do site de viagens (por exemplo, listagens de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via feeds RSS. As ferramentas do NLWeb ingerem esses dados estruturados, criam embeddings e os armazenam em um banco de dados vetorial local ou remoto.

2. **Consulta em Linguagem Natural (Humano)**: Um usuário visita o site e, em vez de navegar por menus, digita em uma interface de chat: "Encontre um hotel em Honolulu para família com piscina na próxima semana".

3. **Processamento pelo NLWeb**: A aplicação NLWeb recebe essa consulta. Ela envia a consulta a um LLM para entendimento e, simultaneamente, pesquisa seu banco de dados vetorial por listagens de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da busca no banco de dados, identifica as melhores correspondências com base nos critérios "family-friendly", "pool" e "Honolulu", e então formata uma resposta em linguagem natural. Crucialmente, a resposta faz referência a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação com Agente de IA**: Como o NLWeb funciona como um servidor MCP, um agente de viagem externo também poderia conectar-se à instância NLWeb deste site. O agente de IA poderia então usar o método `ask` do MCP para consultar diretamente o site: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. A instância NLWeb processaria isso, aproveitando seu banco de dados de informações sobre restaurantes (se carregado), e retornaria uma resposta JSON estruturada.

### Tem mais perguntas sobre MCP/A2A/NLWeb?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horário de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Framework de Agentes da Microsoft](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido utilizando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->