<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T14:44:45+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "pt"
}
-->
# Utilizar Protocolos Agênticos (MCP, A2A e NLWeb)

[![Protocolos Agênticos](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.pt.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Clique na imagem acima para ver o vídeo desta lição)_

À medida que o uso de agentes de IA cresce, também aumenta a necessidade de protocolos que garantam padronização, segurança e promovam a inovação aberta. Nesta lição, vamos abordar 3 protocolos que procuram atender a essa necessidade: Model Context Protocol (MCP), Agent to Agent (A2A) e Natural Language Web (NLWeb).

## Introdução

Nesta lição, vamos abordar:

• Como o **MCP** permite que agentes de IA acedam a ferramentas e dados externos para realizar tarefas dos utilizadores.

• Como o **A2A** possibilita a comunicação e colaboração entre diferentes agentes de IA.

• Como o **NLWeb** traz interfaces de linguagem natural para qualquer site, permitindo que agentes de IA descubram e interajam com o conteúdo.

## Objetivos de Aprendizagem

• **Identificar** o propósito principal e os benefícios do MCP, A2A e NLWeb no contexto de agentes de IA.

• **Explicar** como cada protocolo facilita a comunicação e interação entre LLMs, ferramentas e outros agentes.

• **Reconhecer** os papéis distintos que cada protocolo desempenha na construção de sistemas agênticos complexos.

## Model Context Protocol

O **Model Context Protocol (MCP)** é um padrão aberto que fornece uma forma padronizada para aplicações fornecerem contexto e ferramentas aos LLMs. Isto permite um "adaptador universal" para diferentes fontes de dados e ferramentas que os agentes de IA podem conectar de forma consistente.

Vamos explorar os componentes do MCP, os benefícios em comparação com o uso direto de APIs e um exemplo de como os agentes de IA podem usar um servidor MCP.

### Componentes Principais do MCP

O MCP opera numa **arquitetura cliente-servidor**, e os componentes principais são:

• **Hosts** são aplicações LLM (por exemplo, um editor de código como o VSCode) que iniciam as conexões com um servidor MCP.

• **Clientes** são componentes dentro da aplicação host que mantêm conexões individuais com servidores.

• **Servidores** são programas leves que expõem capacidades específicas.

Incluídos no protocolo estão três primitivas principais que representam as capacidades de um servidor MCP:

• **Ferramentas**: Estas são ações ou funções discretas que um agente de IA pode chamar para realizar uma ação. Por exemplo, um serviço meteorológico pode expor uma ferramenta "obter previsão do tempo", ou um servidor de e-commerce pode expor uma ferramenta "comprar produto". Os servidores MCP anunciam o nome, descrição e esquema de entrada/saída de cada ferramenta na sua lista de capacidades.

• **Recursos**: Estes são itens de dados ou documentos apenas para leitura que um servidor MCP pode fornecer, e os clientes podem recuperá-los sob demanda. Exemplos incluem conteúdos de ficheiros, registos de bases de dados ou arquivos de log. Os recursos podem ser texto (como código ou JSON) ou binários (como imagens ou PDFs).

• **Prompts**: Estes são modelos pré-definidos que fornecem sugestões de prompts, permitindo fluxos de trabalho mais complexos.

### Benefícios do MCP

O MCP oferece vantagens significativas para agentes de IA:

• **Descoberta Dinâmica de Ferramentas**: Os agentes podem receber dinamicamente uma lista de ferramentas disponíveis de um servidor, juntamente com descrições do que fazem. Isto contrasta com APIs tradicionais, que frequentemente requerem codificação estática para integrações, significando que qualquer alteração na API exige atualizações no código. O MCP oferece uma abordagem "integrar uma vez", proporcionando maior adaptabilidade.

• **Interoperabilidade Entre LLMs**: O MCP funciona com diferentes LLMs, oferecendo flexibilidade para alternar entre modelos principais e avaliar o desempenho.

• **Segurança Padronizada**: O MCP inclui um método de autenticação padrão, melhorando a escalabilidade ao adicionar acesso a servidores MCP adicionais. Isto é mais simples do que gerir diferentes chaves e tipos de autenticação para várias APIs tradicionais.

### Exemplo de MCP

![Diagrama MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.pt.png)

Imagine que um utilizador quer reservar um voo usando um assistente de IA alimentado por MCP.

1. **Conexão**: O assistente de IA (o cliente MCP) conecta-se a um servidor MCP fornecido por uma companhia aérea.

2. **Descoberta de Ferramentas**: O cliente pergunta ao servidor MCP da companhia aérea: "Que ferramentas estão disponíveis?" O servidor responde com ferramentas como "procurar voos" e "reservar voos".

3. **Invocação de Ferramentas**: O utilizador pede ao assistente de IA: "Por favor, procure um voo de Portland para Honolulu." O assistente de IA, usando o seu LLM, identifica que precisa chamar a ferramenta "procurar voos" e passa os parâmetros relevantes (origem, destino) ao servidor MCP.

4. **Execução e Resposta**: O servidor MCP, atuando como um intermediário, faz a chamada real à API interna de reservas da companhia aérea. Em seguida, recebe as informações do voo (por exemplo, dados em JSON) e envia-as de volta ao assistente de IA.

5. **Interação Adicional**: O assistente de IA apresenta as opções de voo. Depois de o utilizador selecionar um voo, o assistente pode invocar a ferramenta "reservar voo" no mesmo servidor MCP, concluindo a reserva.

## Protocolo Agente-para-Agente (A2A)

Enquanto o MCP se concentra em conectar LLMs a ferramentas, o **Protocolo Agente-para-Agente (A2A)** vai um passo além, permitindo a comunicação e colaboração entre diferentes agentes de IA. O A2A conecta agentes de IA de diferentes organizações, ambientes e tecnologias para completar uma tarefa partilhada.

Vamos examinar os componentes e benefícios do A2A, juntamente com um exemplo de como ele poderia ser aplicado na nossa aplicação de viagens.

### Componentes Principais do A2A

O A2A foca-se em permitir a comunicação entre agentes e fazê-los trabalhar juntos para completar uma subtarefa do utilizador. Cada componente do protocolo contribui para isso:

#### Cartão do Agente

Semelhante à forma como um servidor MCP partilha uma lista de ferramentas, um Cartão do Agente inclui:
- O Nome do Agente.
- Uma **descrição das tarefas gerais** que realiza.
- Uma **lista de competências específicas** com descrições para ajudar outros agentes (ou até utilizadores humanos) a entender quando e por que chamar esse agente.
- O **URL do Endpoint atual** do agente.
- A **versão** e **capacidades** do agente, como respostas em streaming e notificações push.

#### Executor do Agente

O Executor do Agente é responsável por **passar o contexto da conversa do utilizador ao agente remoto**, que precisa disso para entender a tarefa a ser realizada. Num servidor A2A, um agente usa o seu próprio LLM para interpretar pedidos recebidos e executar tarefas usando as suas ferramentas internas.

#### Artefacto

Depois de um agente remoto completar a tarefa solicitada, o produto do seu trabalho é criado como um artefacto. Um artefacto **contém o resultado do trabalho do agente**, uma **descrição do que foi realizado** e o **contexto textual** enviado através do protocolo. Após o envio do artefacto, a conexão com o agente remoto é encerrada até ser necessária novamente.

#### Fila de Eventos

Este componente é usado para **gerir atualizações e passar mensagens**. É particularmente importante em sistemas agênticos de produção para evitar que a conexão entre agentes seja encerrada antes de uma tarefa ser concluída, especialmente quando os tempos de conclusão podem ser mais longos.

### Benefícios do A2A

• **Colaboração Aprimorada**: Permite que agentes de diferentes fornecedores e plataformas interajam, partilhem contexto e trabalhem juntos, facilitando a automação entre sistemas tradicionalmente desconectados.

• **Flexibilidade na Seleção de Modelos**: Cada agente A2A pode decidir qual LLM usar para atender aos pedidos, permitindo modelos otimizados ou ajustados por agente, ao contrário de uma única conexão LLM em alguns cenários MCP.

• **Autenticação Integrada**: A autenticação está integrada diretamente no protocolo A2A, proporcionando um quadro de segurança robusto para interações entre agentes.

### Exemplo de A2A

![Diagrama A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.pt.png)

Vamos expandir o nosso cenário de reserva de viagens, mas desta vez usando A2A.

1. **Pedido do Utilizador ao Multi-Agente**: Um utilizador interage com um "Agente de Viagens" cliente/agente A2A, talvez dizendo: "Por favor, reserve uma viagem completa para Honolulu na próxima semana, incluindo voos, hotel e carro de aluguer."

2. **Orquestração pelo Agente de Viagens**: O Agente de Viagens recebe este pedido complexo. Usa o seu LLM para raciocinar sobre a tarefa e determinar que precisa interagir com outros agentes especializados.

3. **Comunicação Entre Agentes**: O Agente de Viagens usa o protocolo A2A para conectar-se a agentes especializados, como um "Agente de Companhia Aérea", um "Agente de Hotel" e um "Agente de Aluguer de Carros", criados por diferentes empresas.

4. **Execução de Tarefas Delegadas**: O Agente de Viagens envia tarefas específicas a esses agentes especializados (por exemplo, "Encontrar voos para Honolulu", "Reservar um hotel", "Alugar um carro"). Cada um desses agentes especializados, executando os seus próprios LLMs e utilizando as suas próprias ferramentas (que podem ser servidores MCP), realiza a sua parte específica da reserva.

5. **Resposta Consolidada**: Depois de todos os agentes especializados concluírem as suas tarefas, o Agente de Viagens compila os resultados (detalhes do voo, confirmação do hotel, reserva do carro) e envia uma resposta abrangente, em estilo de chat, ao utilizador.

## Natural Language Web (NLWeb)

Os websites há muito são a principal forma de os utilizadores acederem a informações e dados na internet.

Vamos explorar os diferentes componentes do NLWeb, os benefícios do NLWeb e um exemplo de como o NLWeb funciona, analisando a nossa aplicação de viagens.

### Componentes do NLWeb

- **Aplicação NLWeb (Código de Serviço Principal)**: O sistema que processa perguntas em linguagem natural. Conecta as diferentes partes da plataforma para criar respostas. Pode ser visto como o **motor que alimenta as funcionalidades de linguagem natural** de um site.

- **Protocolo NLWeb**: Este é um **conjunto básico de regras para interação em linguagem natural** com um site. Envia respostas em formato JSON (frequentemente usando Schema.org). O seu objetivo é criar uma base simples para a "Web de IA", da mesma forma que o HTML tornou possível partilhar documentos online.

- **Servidor MCP (Endpoint do Model Context Protocol)**: Cada configuração NLWeb também funciona como um **servidor MCP**. Isto significa que pode **partilhar ferramentas (como um método “ask”) e dados** com outros sistemas de IA. Na prática, isto torna o conteúdo e as capacidades do site utilizáveis por agentes de IA, permitindo que o site se torne parte do ecossistema agêntico mais amplo.

- **Modelos de Embedding**: Estes modelos são usados para **converter o conteúdo do site em representações numéricas chamadas vetores** (embeddings). Estes vetores capturam significado de forma que os computadores possam comparar e pesquisar. São armazenados numa base de dados especial, e os utilizadores podem escolher qual modelo de embedding desejam usar.

- **Base de Dados de Vetores (Mecanismo de Recuperação)**: Esta base de dados **armazena os embeddings do conteúdo do site**. Quando alguém faz uma pergunta, o NLWeb verifica a base de dados de vetores para encontrar rapidamente as informações mais relevantes. Dá uma lista rápida de possíveis respostas, classificadas por similaridade. O NLWeb funciona com diferentes sistemas de armazenamento de vetores, como Qdrant, Snowflake, Milvus, Azure AI Search e Elasticsearch.

### NLWeb por Exemplo

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.pt.png)

Considere novamente o nosso site de reservas de viagens, mas desta vez alimentado pelo NLWeb.

1. **Ingestão de Dados**: Os catálogos de produtos existentes do site de viagens (por exemplo, listas de voos, descrições de hotéis, pacotes turísticos) são formatados usando Schema.org ou carregados via feeds RSS. As ferramentas do NLWeb ingerem esses dados estruturados, criam embeddings e armazenam-nos numa base de dados de vetores local ou remota.

2. **Consulta em Linguagem Natural (Humano)**: Um utilizador visita o site e, em vez de navegar por menus, escreve numa interface de chat: "Encontre-me um hotel familiar em Honolulu com piscina para a próxima semana".

3. **Processamento NLWeb**: A aplicação NLWeb recebe esta consulta. Envia a consulta a um LLM para interpretação e, simultaneamente, pesquisa na sua base de dados de vetores por listagens de hotéis relevantes.

4. **Resultados Precisos**: O LLM ajuda a interpretar os resultados da pesquisa na base de dados, identifica as melhores correspondências com base nos critérios "familiar", "piscina" e "Honolulu", e formata uma resposta em linguagem natural. Crucialmente, a resposta refere-se a hotéis reais do catálogo do site, evitando informações inventadas.

5. **Interação com Agentes de IA**: Como o NLWeb funciona como um servidor MCP, um agente de viagens externo de IA também poderia conectar-se à instância NLWeb deste site. O agente de IA poderia então usar o método `ask` do MCP para consultar diretamente o site: `ask("Existem restaurantes vegan-friendly na área de Honolulu recomendados pelo hotel?")`. A instância NLWeb processaria isto, aproveitando a sua base de dados de informações sobre restaurantes (se carregada), e retornaria uma resposta estruturada em JSON.

### Tem Mais Perguntas sobre MCP/A2A/NLWeb?

Junte-se ao [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para interagir com outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre agentes de IA.

## Recursos

- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repositório NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Guias do Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.