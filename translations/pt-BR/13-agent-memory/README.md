# Memória para Agentes de IA 
[![Memória do Agente](../../../translated_images/pt-BR/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos da criação de Agentes de IA, duas coisas são principalmente abordadas: a capacidade de chamar ferramentas para realizar tarefas e a habilidade de melhorar com o tempo. A memória está na base da criação de um agente que se autoaperfeiçoa e pode criar melhores experiências para nossos usuários.

Nesta lição, veremos o que é memória para Agentes de IA e como podemos gerenciá-la e usá-la para o benefício de nossas aplicações.

## Introdução

Esta lição irá cobrir:

• **Entendendo a Memória do Agente de IA**: O que é memória e por que é essencial para os agentes.

• **Implementação e Armazenamento de Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, focando em memória de curto e longo prazo.

• **Fazendo Agentes de IA se Autoaperfeiçoarem**: Como a memória permite que os agentes aprendam com interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais abrangentes em notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente um grafo de conhecimento suportado por embeddings, visualizando o grafo e recuperação inteligente

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

• **Diferenciar entre vários tipos de memória de agente de IA**, incluindo memória ativa, de curto prazo e de longo prazo, assim como formas especializadas como memória de persona e episódica.

• **Implementar e gerenciar memória de curto e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, memória Whiteboard e integrando com Azure AI Search.

• **Entender os princípios por trás de agentes de IA autoaperfeiçoáveis** e como sistemas robustos de gerenciamento de memória contribuem para aprendizado e adaptação contínuos.

## Entendendo a Memória dos Agentes de IA

No seu cerne, **memória para agentes de IA refere-se aos mecanismos que permitem que eles retenham e recordem informações**. Essas informações podem ser detalhes específicos sobre uma conversa, preferências do usuário, ações passadas ou até mesmo padrões aprendidos.

Sem memória, as aplicações de IA frequentemente são sem estado, significando que cada interação começa do zero. Isso leva a uma experiência do usuário repetitiva e frustrante, onde o agente "esquece" o contexto ou preferências anteriores.

### Por que a Memória é Importante?

a inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informações passadas. A memória permite que os agentes sejam:

• **Reflexivos**: Aprendendo com ações e resultados passados.

• **Interativos**: Mantendo o contexto ao longo de uma conversa em andamento.

• **Proativos e Reativos**: Antecipando necessidades ou respondendo adequadamente com base em dados históricos.

• **Autônomos**: Operando de forma mais independente ao recorrer a conhecimento armazenado.

O objetivo de implementar memória é tornar os agentes mais **confiáveis e capazes**.

### Tipos de Memória

#### Memória Ativa

Pense nisso como um pedaço de papel rascunho que um agente usa durante uma única tarefa ou processo de pensamento em andamento. Ela guarda informações imediatas necessárias para computar o próximo passo.

Para agentes de IA, a memória ativa frequentemente captura as informações mais relevantes de uma conversa, mesmo que o histórico completo do chat seja longo ou truncado. Ela foca em extrair elementos chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória Ativa**

Em um agente de reservas de viagens, a memória ativa pode capturar o pedido atual do usuário, como "Quero reservar uma viagem para Paris". Essa exigência específica é mantida no contexto imediato do agente para guiar a interação atual.

#### Memória de Curto Prazo

Esse tipo de memória retém informações durante uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a trocas anteriores no diálogo.

Nos exemplos do SDK Python do [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), isso corresponde a `AgentSession`, criado com `agent.create_session()`. A sessão é a memória de curto prazo embutida no framework: ela mantém o contexto da conversa disponível enquanto a mesma sessão for reutilizada, mas esse contexto não é persistido quando a sessão termina ou o aplicativo reinicia. Use memória de longo prazo para fatos e preferências que precisam sobreviver entre sessões, tipicamente através de um banco de dados, índice vetorial ou outra loja persistente.

**Exemplo de Memória de Curto Prazo**

Se um usuário pergunta, "Quanto custaria um voo para Paris?" e depois segue com "E quanto à acomodação lá?", a memória de curto prazo garante que o agente saiba que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Esta é uma informação que persiste através de múltiplas conversas ou sessões. Permite que os agentes lembrem preferências do usuário, interações históricas ou conhecimento geral ao longo de períodos prolongados. Isso é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esquiar e de atividades ao ar livre, gosta de café com vista para a montanha e quer evitar pistas avançadas de esqui devido a uma lesão anterior". Essa informação, aprendida em interações passadas, influencia recomendações em futuras sessões de planejamento de viagem, tornando-as altamente personalizadas.

#### Memória de Persona

Esse tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente se lembre de detalhes sobre si mesmo ou seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**
Se o agente de viagens for projetado para ser um "especialista em planejamento de esqui", a memória de persona pode reforçar esse papel, influenciando suas respostas para alinhar-se ao tom e conhecimento de um especialista.

#### Memória de Fluxo de Trabalho/Episódica

Essa memória armazena a sequência de passos que um agente toma durante uma tarefa complexa, incluindo sucessos e falhas. É como lembrar "episódios" ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico mas falhou devido à indisponibilidade, a memória episódica poderia registrar essa falha, permitindo que o agente tente voos alternativos ou informe o usuário sobre o problema de forma mais informada durante uma tentativa subsequente.

#### Memória de Entidade

Isso envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos de conversas. Permite ao agente construir um entendimento estruturado dos elementos-chave discutidos.

**Exemplo de Memória de Entidade**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris", "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Em uma interação futura, o agente poderia recordar "Le Chat Noir" e oferecer-se para fazer uma nova reserva lá.

#### RAG Estruturada (Retrieval Augmented Generation)

Enquanto RAG é uma técnica mais ampla, a "RAG Estruturada" é destacada como uma tecnologia poderosa de memória. Ela extrai informações densas e estruturadas de várias fontes (conversas, e-mails, imagens) e as usa para melhorar precisão, recall e velocidade nas respostas. Ao contrário da RAG clássica que depende apenas da similaridade semântica, a RAG Estruturada trabalha com a estrutura inerente da informação.

**Exemplo de RAG Estruturada**

Em vez de apenas combinar palavras-chave, a RAG Estruturada pode analisar detalhes do voo (destino, data, hora, companhia aérea) de um e-mail e armazená-los de forma estruturada. Isso permite consultas precisas como "Qual voo eu reservei para Paris na terça-feira?"

## Implementação e Armazenamento de Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gerenciamento de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou deletar) informações. A recuperação é um aspecto especialmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma maneira de armazenar e gerenciar a memória do agente é usar ferramentas especializadas como o Mem0. O Mem0 funciona como uma camada de memória persistente, permitindo que agentes recordem interações relevantes, armazenem preferências do usuário e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se tornem agentes com estado.

Ele funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao thread do agente são enviadas ao serviço Mem0, que usa um Large Language Model (LLM) para resumir o histórico da conversa e extrair novas memórias. Subsequentemente, uma fase de atualização conduzida por LLM determina se adiciona, modifica ou apaga essas memórias, armazenando-as em uma loja híbrida de dados que pode incluir bancos de dados vetoriais, grafos e de chave-valor. Este sistema também suporta vários tipos de memória e pode incorporar memória gráfica para gerenciar relacionamentos entre entidades.

#### Cognee

Outra abordagem poderosa é usar o **Cognee**, uma memória semântica open-source para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis suportados por embeddings. O Cognee fornece uma **arquitetura de armazenamento dupla** combinando busca por similaridade vetorial com relacionamentos em grafos, permitindo que agentes entendam não apenas o que é similar, mas como os conceitos se relacionam.

Ele se destaca em **recuperação híbrida** que combina similaridade vetorial, estrutura gráfica e raciocínio LLM - desde busca direta de pedaços de dados até perguntas adaptadas ao grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado único, suportando tanto contexto de sessão de curto prazo quanto memória persistente de longo prazo.

O tutorial em notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra a construção dessa camada unificada de memória, com exemplos práticos de ingestão de diversas fontes de dados, visualização do grafo de conhecimento e consultas com diferentes estratégias de busca adaptadas às necessidades específicas do agente.

### Armazenando Memória com RAG

Além de ferramentas especializadas de memória como Mem0, você pode aproveitar serviços robustos de busca como **Azure AI Search como backend para armazenamento e recuperação de memórias**, especialmente para RAG estruturada.

Isso permite fundamentar as respostas do seu agente com os seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias específicas de viagens de usuários, catálogos de produtos ou qualquer outro conhecimento de domínio específico.

O Azure AI Search suporta capacidades como **RAG Estruturada**, que se destaca em extrair e recuperar informações densas e estruturadas de grandes conjuntos de dados como históricos de conversas, e-mails ou até imagens. Isso oferece "precisão e recall sobre-humanos" comparados a abordagens tradicionais de segmentação e embeddings de texto.

## Fazendo Agentes de IA se Autoaperfeiçoarem

Um padrão comum para agentes autoaperfeiçoáveis envolve a introdução de um **"agente de conhecimento"**. Esse agente separado observa a conversa principal entre o usuário e o agente primário. Seu papel é:

1. **Identificar informações valiosas**: Determinar se alguma parte da conversa vale a pena guardar como conhecimento geral ou preferência específica do usuário.

2. **Extrair e resumir**: Destilar o aprendizado essencial ou a preferência da conversa.

3. **Armazenar em uma base de conhecimento**: Persistir essa informação extraída, geralmente em um banco de dados vetorial, para que possa ser recuperada depois.

4. **Aumentar consultas futuras**: Quando o usuário iniciar uma nova consulta, o agente de conhecimento recupera informações relevantes armazenadas e as anexa ao prompt do usuário, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gerenciamento de Latência**: Para evitar desacelerar as interações do usuário, um modelo mais barato e rápido pode ser usado inicialmente para verificar rapidamente se uma informação é valiosa para armazenar ou recuperar, invocando o processo mais complexo de extração/recuperação somente quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento crescente, informações menos usadas com frequência podem ser movidas para "armazenamento frio" para gerenciar custos.

## Quer Saber Mais Sobre Memória de Agentes?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horas de expediente e obter respostas para suas perguntas sobre Agentes de IA.
## Lição Anterior

[Engenharia de Contexto para Agentes de IA](../12-context-engineering/README.md)

## Próxima Lição

[Explorando o Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->