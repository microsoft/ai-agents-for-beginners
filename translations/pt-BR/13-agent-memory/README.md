# Memória para Agentes de IA 
[![Memória do Agente](../../../translated_images/pt-BR/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Quando discutimos os benefícios exclusivos de criar Agentes de IA, duas coisas são mencionadas principalmente: a capacidade de chamar ferramentas para completar tarefas e a capacidade de melhorar ao longo do tempo. A memória está na base da criação de um agente autoaperfeiçoável que pode criar melhores experiências para nossos usuários.

Nesta lição, veremos o que é memória para Agentes de IA e como podemos gerenciá-la e usá-la em benefício de nossas aplicações.

## Introdução

Esta lição cobrirá:

• **Entendendo a Memória de Agentes de IA**: O que é memória e por que é essencial para agentes.

• **Implementando e Armazenando Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, com foco em memória de curto e longo prazo.

• **Tornando Agentes de IA Autoaperfeiçoados**: Como a memória permite que os agentes aprendam com interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais completos em notebooks:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente um grafo de conhecimento suportado por embeddings, visualizando o grafo e recuperação inteligente

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá como:

• **Diferenciar entre vários tipos de memória de agentes de IA**, incluindo memória de trabalho, de curto prazo e de longo prazo, bem como formas especializadas como persona e memória episódica.

• **Implementar e gerenciar memória de curto e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, Whiteboard memory e integrando com Azure AI Search.

• **Entender os princípios por trás de agentes de IA autoaperfeiçoados** e como sistemas robustos de gerenciamento de memória contribuem para aprendizado e adaptação contínuos.

## Entendendo a Memória de Agentes de IA

No seu cerne, **memória para agentes de IA refere-se aos mecanismos que lhes permitem reter e recordar informações**. Essas informações podem ser detalhes específicos sobre uma conversa, preferências do usuário, ações passadas ou até padrões aprendidos.

Sem memória, aplicações de IA costumam ser sem estado, significando que cada interação começa do zero. Isso leva a uma experiência repetitiva e frustrante para o usuário, onde o agente "esquece" o contexto ou preferências anteriores.

### Por que a Memória é Importante?

a inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informações passadas. A memória permite que os agentes sejam:

• **Reflexivos**: Aprendendo com ações e resultados anteriores.

• **Interativos**: Mantendo o contexto durante uma conversa contínua.

• **Proativos e Reativos**: Antecipando necessidades ou respondendo apropriadamente com base em dados históricos.

• **Autônomos**: Operando com mais independência ao recorrer a conhecimentos armazenados.

O objetivo de implementar memória é tornar os agentes mais **confiáveis e capazes**.

### Tipos de Memória

#### Memória de Trabalho

Pense nisso como um pedaço de rascunho que um agente usa durante uma única tarefa ou processo de pensamento em andamento. Ela guarda informações imediatas necessárias para calcular o próximo passo.

Para agentes de IA, a memória de trabalho frequentemente captura as informações mais relevantes de uma conversa, mesmo que todo o histórico de chat seja longo ou truncado. Ela foca em extrair elementos-chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória de Trabalho**

Em um agente de reserva de viagens, a memória de trabalho pode capturar o pedido atual do usuário, como "Quero reservar uma viagem para Paris". Esse requisito específico é mantido no contexto imediato do agente para guiar a interação atual.

#### Memória de Curto Prazo

Esse tipo de memória mantém informações pela duração de uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a turnos anteriores no diálogo.

**Exemplo de Memória de Curto Prazo**

Se um usuário pergunta, "Quanto custaria um voo para Paris?" e depois complementa com "E quanto à acomodação lá?", a memória de curto prazo garante que o agente saiba que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

São informações que persistem através de múltiplas conversas ou sessões. Permite que agentes lembrem preferências do usuário, interações históricas ou conhecimento geral ao longo de períodos estendidos. Isso é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esqui e atividades ao ar livre, gosta de café com vista para a montanha e quer evitar pistas de esqui avançadas devido a uma lesão passada". Essa informação, aprendida em interações anteriores, influencia recomendações em futuras sessões de planejamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Esse tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente lembre detalhes sobre si mesmo ou seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**
Se o agente de viagens for projetado para ser um "planejador de esqui especialista", a memória de persona pode reforçar esse papel, influenciando suas respostas para alinhar com o tom e o conhecimento de um especialista.

#### Memória de Fluxo de Trabalho/Episódica

Essa memória armazena a sequência de passos que um agente toma durante uma tarefa complexa, incluindo sucessos e falhas. É como lembrar "episódios" específicos ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico, mas falhou devido à indisponibilidade, a memória episódica poderia registrar essa falha, permitindo que o agente tente voos alternativos ou informe o usuário sobre o problema de forma mais informada em uma tentativa subsequente.

#### Memória de Entidade

Isso envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos de conversas. Permite que o agente construa uma compreensão estruturada dos elementos-chave discutidos.

**Exemplo de Memória de Entidade**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris", "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Em uma interação futura, o agente poderia lembrar "Le Chat Noir" e oferecer-se para fazer uma nova reserva lá.

#### Structured RAG (Retrieval Augmented Generation)

Enquanto RAG é uma técnica mais ampla, "Structured RAG" é destacada como uma tecnologia de memória poderosa. Ela extrai informações densas e estruturadas de várias fontes (conversas, e-mails, imagens) e as usa para melhorar precisão, recall e velocidade nas respostas. Ao contrário do RAG clássico que depende apenas de similaridade semântica, o Structured RAG trabalha com a estrutura inerente da informação.

**Exemplo de Structured RAG**

Em vez de apenas casar palavras-chave, o Structured RAG poderia analisar detalhes de voo (destino, data, hora, companhia aérea) a partir de um e-mail e armazená-los de forma estruturada. Isso permite consultas precisas como "Qual voo eu reservei para Paris na terça-feira?"

## Implementando e Armazenando Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gerenciamento de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou deletar) informações. A recuperação é um aspecto particularmente crucial.

### Ferramentas de Memória Especializadas

#### Mem0

Uma maneira de armazenar e gerenciar a memória do agente é usando ferramentas especializadas como Mem0. O Mem0 funciona como uma camada de memória persistente, permitindo que agentes recordem interações relevantes, armazenem preferências de usuário e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se tornem agentes com estado.

Ele funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao thread de um agente são enviadas para o serviço Mem0, que usa um Large Language Model (LLM) para resumir o histórico de conversas e extrair novas memórias. Subsequentemente, uma fase de atualização conduzida por um LLM determina se deve adicionar, modificar ou deletar essas memórias, armazenando-as em um repositório híbrido que pode incluir bancos de dados vetoriais, grafos e chave-valor. Esse sistema também suporta vários tipos de memória e pode incorporar memória em grafo para gerenciar relacionamentos entre entidades.

#### Cognee

Outra abordagem poderosa é usar **Cognee**, uma memória semântica open-source para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis suportados por embeddings. O Cognee fornece uma **arquitetura de armazenamento dupla** combinando busca por similaridade vetorial com relações de grafo, permitindo que agentes entendam não apenas quais informações são similares, mas como os conceitos se relacionam entre si.

Ele se destaca em **recuperação híbrida** que mistura similaridade vetorial, estrutura de grafo e raciocínio de LLM - desde lookup de chunks brutos até perguntas e respostas conscientes do grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado, suportando tanto o contexto de sessão de curto prazo quanto a memória persistente de longo prazo.

O tutorial em notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra a construção dessa camada de memória unificada, com exemplos práticos de ingestão de fontes de dados diversas, visualização do grafo de conhecimento e consultas com diferentes estratégias de busca adaptadas às necessidades específicas do agente.

### Armazenando Memória com RAG

Além de ferramentas de memória especializadas como Mem0 , você pode aproveitar serviços de busca robustos como **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para Structured RAG.

Isso permite fundamentar as respostas do seu agente com seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias de viagem específicas do usuário, catálogos de produtos ou qualquer outro conhecimento específico de domínio.

O Azure AI Search suporta capacidades como **Structured RAG**, que se destaca em extrair e recuperar informações densas e estruturadas de grandes conjuntos de dados como históricos de conversa, e-mails ou até imagens. Isso fornece "precisão e recall sobre-humanos" comparado às abordagens tradicionais de chunking de texto e embeddings.

## Tornando Agentes de IA Autoaperfeiçoados

Um padrão comum para agentes autoaperfeiçoados envolve a introdução de um **"agente de conhecimento"**. Esse agente separado observa a conversa principal entre o usuário e o agente primário. Seu papel é:

1. **Identificar informações valiosas**: Determinar se alguma parte da conversa vale a pena ser salva como conhecimento geral ou preferência específica do usuário.

2. **Extrair e resumir**: Distinguir o aprendizado essencial ou preferência da conversa.

3. **Armazenar em uma base de conhecimento**: Persistir essa informação extraída, frequentemente em um banco de dados vetorial, para que possa ser recuperada mais tarde.

4. **Aumentar consultas futuras**: Quando o usuário inicia uma nova consulta, o agente de conhecimento recupera informações relevantes armazenadas e as acrescenta ao prompt do usuário, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gerenciamento de Latência**: Para evitar desacelerar as interações do usuário, um modelo mais barato e rápido pode ser usado inicialmente para verificar rapidamente se uma informação vale a pena ser armazenada ou recuperada, invocando o processo de extração/recuperação mais complexo somente quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento crescente, informações menos utilizadas podem ser movidas para "armazenamento frio" para gerenciar custos.

## Tem mais perguntas sobre Memória de Agentes?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução por um profissional humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->