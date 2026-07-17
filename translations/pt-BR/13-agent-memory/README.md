# Memória para Agentes de IA 
[![Agent Memory](../../../translated_images/pt-BR/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos de criar Agentes de IA, dois aspectos são principalmente abordados: a capacidade de chamar ferramentas para completar tarefas e a capacidade de melhorar ao longo do tempo. A memória está na base da criação de agentes autoaperfeiçoados que podem proporcionar melhores experiências para nossos usuários.

Nesta lição, veremos o que é memória para Agentes de IA e como podemos gerenciá-la e usá-la para o benefício de nossas aplicações.

## Introdução

Esta lição abordará:

• **Entendendo a Memória do Agente de IA**: O que é memória e por que é essencial para agentes.

• **Implementando e Armazenando Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, com foco em memória de curto e longo prazo.

• **Tornando os Agentes de IA Autoaperfeiçoáveis**: Como a memória permite que agentes aprendam com interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais completos em notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente um grafo de conhecimento apoiado por embeddings, visualizando o grafo e recuperação inteligente

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá como:

• **Diferenciar entre vários tipos de memória de agentes de IA**, incluindo memória operacional, de curto prazo e de longo prazo, assim como formas especializadas como memória de persona e episódica.

• **Implementar e gerenciar memória de curto prazo e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, memória Whiteboard e integração com Azure AI Search.

• **Entender os princípios por trás de agentes de IA autoaperfeiçoáveis** e como sistemas robustos de gerenciamento de memória contribuem para aprendizagem contínua e adaptação.

## Entendendo a Memória do Agente de IA

Em sua essência, **memória para agentes de IA refere-se aos mecanismos que permitem que eles retenham e recuperem informações**. Essa informação pode ser detalhes específicos sobre uma conversa, preferências do usuário, ações passadas ou até padrões aprendidos.

Sem memória, aplicações de IA são frequentemente sem estado, significando que cada interação começa do zero. Isso leva a uma experiência repetitiva e frustrante em que o agente "esquece" o contexto ou preferências anteriores.

### Por que a Memória é Importante?

A inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informações passadas. A memória permite que os agentes sejam:

• **Reflexivos**: Aprendendo com ações e resultados anteriores.

• **Interativos**: Mantendo o contexto durante uma conversa em andamento.

• **Proativos e Reativos**: Antecipando necessidades ou respondendo adequadamente com base em dados históricos.

• **Autônomos**: Operando de forma mais independente ao recorrer ao conhecimento armazenado.

O objetivo de implementar memória é tornar os agentes mais **confiáveis e capazes**.

### Tipos de Memória

#### Memória Operacional

Pense nisso como um pedaço de papel rascunho que um agente usa durante uma única tarefa ou processo de pensamento em andamento. Ela mantém informações imediatas necessárias para calcular o próximo passo.

Para agentes de IA, a memória operacional frequentemente captura a informação mais relevante de uma conversa, mesmo que o histórico completo do chat seja longo ou truncado. Foca em extrair elementos chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória Operacional**

Em um agente de reserva de viagens, a memória operacional pode capturar o pedido atual do usuário, como "Quero reservar uma viagem para Paris". Este requisito específico é mantido no contexto imediato do agente para guiar a interação atual.

#### Memória de Curto Prazo

Esse tipo de memória retém informações durante a duração de uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a turnos anteriores no diálogo.

Nos exemplos do SDK Python do [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), isso corresponde a `AgentSession`, criado com `agent.create_session()`. A sessão é a memória de curto prazo interna do framework: mantém o contexto da conversa disponível enquanto essa mesma sessão é reutilizada, mas esse contexto não é persistido quando a sessão termina ou o aplicativo reinicia. Use a memória de longo prazo para fatos e preferências que precisam sobreviver entre sessões, tipicamente por meio de banco de dados, índice vetorial ou outro armazenamento persistente.

**Exemplo de Memória de Curto Prazo**

Se um usuário pergunta: "Quanto custaria um voo para Paris?" e depois complementa com "E em relação a acomodação lá?", a memória de curto prazo garante que o agente saiba que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Esta é a informação que persiste ao longo de várias conversas ou sessões. Permite que agentes lembrem preferências do usuário, interações históricas ou conhecimento geral por períodos prolongados. Isso é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esqui e atividades ao ar livre, prefere café com vista para a montanha e quer evitar pistas avançadas devido a uma lesão passada". Essa informação, aprendida em interações anteriores, influencia recomendações em futuras sessões de planejamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Esse tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente lembre detalhes sobre si mesmo ou seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**

Se o agente de viagens é projetado para ser um "especialista em planejamento de esqui", a memória de persona pode reforçar esse papel, influenciando suas respostas para alinhar com o tom e conhecimento de um especialista.

#### Memória de Fluxo de Trabalho/Episódica

Essa memória armazena a sequência de passos que um agente realiza durante uma tarefa complexa, incluindo sucessos e falhas. É como lembrar "episódios" específicos ou experiências passadas para aprender com elas.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico, mas falhou devido à indisponibilidade, a memória episódica pode registrar essa falha, permitindo que o agente tente voos alternativos ou informe o usuário sobre o problema de forma mais informada em uma tentativa subsequente.

#### Memória de Entidade

Envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos de conversas. Permite que o agente construa um entendimento estruturado dos elementos-chave discutidos.

**Exemplo de Memória de Entidade**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris," "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Em uma interação futura, o agente poderia recordar "Le Chat Noir" e oferecer fazer uma nova reserva lá.

#### RAG Estruturado (Retrieval Augmented Generation)

Embora o RAG seja uma técnica mais ampla, o "RAG Estruturado" é destacado como uma tecnologia poderosa de memória. Ele extrai informações densas e estruturadas de várias fontes (conversas, e-mails, imagens) e as usa para ampliar precisão, recuperação e velocidade nas respostas. Diferente do RAG clássico que se baseia apenas em similaridade semântica, o RAG Estruturado trabalha com a estrutura inerente das informações.

**Exemplo de RAG Estruturado**

Em vez de apenas emparelhar palavras-chave, o RAG Estruturado pode analisar detalhes de voos (destino, data, hora, companhia aérea) de um e-mail e armazená-los de forma estruturada. Isso permite consultas precisas como "Qual voo eu reservei para Paris na terça-feira?"

## Implementando e Armazenando Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gerenciamento de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou deletar) informações. A recuperação é um aspecto particularmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma maneira de armazenar e gerenciar memória do agente é usar ferramentas especializadas como o Mem0. O Mem0 funciona como uma camada de memória persistente, permitindo que agentes recordem interações relevantes, armazenem preferências de usuários e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se transformem em agentes com estado.

Ele opera por meio de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao tópico do agente são enviadas ao serviço Mem0, que usa um Large Language Model (LLM) para resumir o histórico da conversa e extrair novas memórias. Em seguida, uma fase de atualização comandada por LLM determina se deve adicionar, modificar ou deletar essas memórias, armazenando-as em um armazenamento híbrido que pode incluir bancos de dados vetoriais, grafos e chave-valor. Este sistema também suporta vários tipos de memória e pode incorporar memória de grafo para gerenciar relacionamentos entre entidades.

#### Cognee

Outra abordagem poderosa é usar o **Cognee**, uma memória semântica open-source para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis apoiados por embeddings. O Cognee oferece uma **arquitetura de dupla camada** combinando busca por similaridade vetorial com relacionamentos em grafo, permitindo que agentes entendam não apenas o que é informação similar, mas como conceitos se relacionam.

Ele se destaca em **recuperação híbrida** que combina similaridade vetorial, estrutura de grafo e raciocínio LLM — desde busca simples por fragmentos até perguntas conscientes do grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado, suportando tanto o contexto de sessão de curto prazo quanto memória persistente de longo prazo.

O tutorial em notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra como construir essa camada unificada de memória, com exemplos práticos de ingestão de diversas fontes de dados, visualização do grafo de conhecimento e consultas com diferentes estratégias de busca adaptadas às necessidades específicas do agente.

### Armazenando Memória com RAG

Além de ferramentas especializadas como mem0, você pode aproveitar serviços robustos de busca como o **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para RAG estruturado.

Isso permite fundamentar as respostas do seu agente com seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias específicas de viagens do usuário, catálogos de produtos ou qualquer outro conhecimento específico de domínio.

O Azure AI Search suporta capacidades como **RAG Estruturado**, que se destaca em extrair e recuperar informações densas e estruturadas de grandes conjuntos de dados, como históricos de conversas, e-mails ou até imagens. Isso oferece "precisão e recall super-humanos" comparado a abordagens tradicionais de fragmentação de texto e embeddings.

## Tornando os Agentes de IA Autoaperfeiçoados

Um padrão comum para agentes autoaperfeiçoados envolve introduzir um **"agente de conhecimento"**. Este agente separado observa a conversa principal entre o usuário e o agente primário. Seu papel é:

1. **Identificar informações valiosas**: Determinar se alguma parte da conversa vale a pena ser salva como conhecimento geral ou preferência específica do usuário.

2. **Extrair e resumir**: Destilar a aprendizagem essencial ou preferência da conversa.

3. **Armazenar em uma base de conhecimento**: Persistir essa informação extraída, frequentemente em um banco de dados vetorial, para que possa ser recuperada posteriormente.

4. **Ampliar consultas futuras**: Quando o usuário inicia uma nova consulta, o agente de conhecimento recupera informações armazenadas relevantes e as anexa ao prompt do usuário, fornecendo contexto crucial para o agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gerenciamento de Latência**: Para evitar retardar as interações do usuário, um modelo mais barato e rápido pode ser usado inicialmente para verificar se a informação vale a pena ser armazenada ou recuperada, invocando o processo mais complexo de extração/recuperação somente quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento crescente, informações usadas com menos frequência podem ser movidas para "armazenamento frio" para gerenciar custos.

## Tem Mais Perguntas Sobre Memória de Agentes?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e esclarecer suas dúvidas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->