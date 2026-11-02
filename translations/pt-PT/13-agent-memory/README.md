# Memória para Agentes de IA 
[![Agent Memory](../../../translated_images/pt-PT/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos de criar Agentes de IA, são principalmente abordadas duas coisas: a capacidade de chamar ferramentas para completar tarefas e a capacidade de melhorar ao longo do tempo. A memória está na base da criação de um agente que melhora a si próprio e que pode criar experiências melhores para os nossos utilizadores.

Nesta lição, vamos ver o que é a memória para Agentes de IA e como a podemos gerir e usar para o benefício das nossas aplicações.

## Introdução

Esta lição irá abordar:

• **Compreensão da Memória de Agentes de IA**: O que é memória e porque é essencial para os agentes.

• **Implementação e Armazenamento da Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, focando na memória de curto e longo prazo.

• **Fazer Agentes de IA Autoaperfeiçoáveis**: Como a memória permite que os agentes aprendam com interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais abrangentes em notebooks:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente um grafo de conhecimento suportado por embeddings, visualizando o grafo e recuperação inteligente

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

• **Diferenciar entre vários tipos de memória de agentes de IA**, incluindo memória de trabalho, de curto prazo e de longo prazo, bem como formas especializadas como memória de persona e memória episódica.

• **Implementar e gerir memória de curto prazo e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, memória Whiteboard, e integração com Azure AI Search.

• **Compreender os princípios por trás de agentes de IA autoaperfeiçoáveis** e como sistemas robustos de gestão de memória contribuem para a aprendizagem e adaptação contínuas.

## Compreensão da Memória de Agentes de IA

Na sua essência, **memória para agentes de IA refere-se aos mecanismos que lhes permitem reter e recordar informação**. Esta informação pode ser detalhes específicos sobre uma conversa, preferências do utilizador, ações passadas ou mesmo padrões aprendidos.

Sem memória, as aplicações de IA são frequentemente sem estado, significando que cada interação começa do zero. Isto conduz a uma experiência de utilizador repetitiva e frustrante onde o agente "esquece" o contexto ou as preferências anteriores.

### Porque é que a Memória é Importante?

a inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informação passada. A memória permite que os agentes sejam:

• **Reflexivos**: Aprender com ações e resultados passados.

• **Interativos**: Manter contexto ao longo de uma conversa em curso.

• **Proativos e Reativos**: Antecipar necessidades ou responder adequadamente com base em dados históricos.

• **Autónomos**: Operar de forma mais independente recorrendo ao conhecimento armazenado.

O objetivo de implementar memória é tornar os agentes mais **confiáveis e capazes**.

### Tipos de Memória

#### Memória de Trabalho

Pense nisto como um pedaço de papel para rascunho que um agente usa durante uma tarefa ou processo de pensamento único e contínuo. Guarda a informação imediata necessária para calcular o passo seguinte.

Para agentes de IA, a memória de trabalho captura frequentemente a informação mais relevante de uma conversa, mesmo que o histórico completo de chat seja longo ou truncado. Foca-se em extrair elementos-chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória de Trabalho**

Num agente de reserva de viagens, a memória de trabalho pode captar o pedido atual do utilizador, como "Quero reservar uma viagem para Paris". Este requisito específico é mantido no contexto imediato do agente para guiar a interação atual.

#### Memória de Curto Prazo

Este tipo de memória retém informação durante a duração de uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a voltas anteriores no diálogo.

Nos exemplos do SDK Python do [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), isto corresponde a `AgentSession`, criado com `agent.create_session()`. A sessão é a memória de curto prazo incorporada no framework: mantém o contexto da conversa disponível enquanto essa mesma sessão é reutilizada, mas esse contexto não é persistido quando a sessão termina ou a aplicação reinicia. Use memória de longo prazo para factos e preferências que precisam de sobreviver às sessões, tipicamente através de uma base de dados, índice vetorial ou outro armazenamento persistente.

**Exemplo de Memória de Curto Prazo**

Se um utilizador pergunta, "Quanto custaria um voo para Paris?" e depois segue com "E quanto à acomodação lá?", a memória de curto prazo assegura que o agente sabe que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Esta é a informação que persiste através de múltiplas conversas ou sessões. Permite que os agentes se lembrem de preferências do utilizador, interações históricas ou conhecimento geral ao longo de períodos extensos. Isto é importante para a personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esquiar e atividades ao ar livre, gosta de café com vista para a montanha, e quer evitar pistas de esqui avançadas devido a uma lesão passada". Esta informação, aprendida de interações anteriores, influencia recomendações em futuras sessões de planeamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Este tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente se lembre de detalhes sobre si próprio ou o seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**
Se o agente de viagens for projetado para ser um "planeador de esqui especialista", a memória de persona pode reforçar este papel, influenciando as respostas para se alinharem com o tom e o conhecimento de um especialista.

#### Memória de Fluxo de Trabalho/Episódica

Esta memória armazena a sequência de passos que um agente toma durante uma tarefa complexa, incluindo sucessos e falhas. É como recordar "episódios" específicos ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico mas falhou devido à indisponibilidade, a memória episódica poderia registar essa falha, permitindo que o agente tente voos alternativos ou informe o utilizador sobre o problema de forma mais informada numa tentativa subsequente.

#### Memória de Entidade

Isto envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos das conversas. Permite ao agente construir uma compreensão estruturada dos elementos-chave discutidos.

**Exemplo de Memória de Entidade**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris", "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Numa interação futura, o agente poderia recordar "Le Chat Noir" e oferecer-se para fazer uma nova reserva lá.

#### RAG Estruturado (Retrieval Augmented Generation)

Embora RAG seja uma técnica mais ampla, "RAG Estruturado" é destacado como uma tecnologia poderosa de memória. Extrai informação densa e estruturada de várias fontes (conversas, emails, imagens) e usa-a para melhorar a precisão, recuperação e rapidez nas respostas. Ao contrário do RAG clássico que depende apenas da similaridade semântica, o RAG Estruturado trabalha com a estrutura inerente da informação.

**Exemplo de RAG Estruturado**

Em vez de apenas corresponder palavras-chave, o RAG Estruturado poderia analisar detalhes de voo (destino, data, hora, companhia aérea) de um email e armazená-los de forma estruturada. Isto permite consultas precisas como "Que voo reservei para Paris na terça-feira?"

## Implementação e Armazenamento da Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gestão de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou apagar) informação. A recuperação é um aspeto particularmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma forma de armazenar e gerir a memória do agente é usando ferramentas especializadas como o Mem0. O Mem0 funciona como uma camada persistente de memória, permitindo que os agentes recordem interações relevantes, armazenem preferências do utilizador e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes stateless se tornem stateful.

Funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao tópico de um agente são enviadas para o serviço Mem0, que usa um Large Language Model (LLM) para resumir o histórico da conversa e extrair novas memórias. Subsequentemente, uma fase de atualização conduzida por um LLM determina se estas memórias devem ser adicionadas, modificadas ou apagadas, armazenando-as num armazenamento híbrido que pode incluir bases de dados vetoriais, grafos e chave-valor. Este sistema suporta também vários tipos de memória e pode incorporar memória de grafo para gerir relações entre entidades.

#### Cognee

Outra abordagem poderosa é usar o **Cognee**, uma memória semântica open source para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis suportados por embeddings. O Cognee oferece uma **arquitetura de armazenamento dual**, combinando pesquisa por similaridade vetorial com relações em grafos, permitindo aos agentes compreender não apenas que informação é similar, mas como os conceitos se relacionam.

Destaca-se na **recuperação híbrida** que mistura similaridade vetorial, estrutura de grafo e raciocínio LLM – desde a busca do fragmento bruto até ao questionamento consciente do grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado único, suportando tanto o contexto de sessão de curto prazo como a memória persistente de longo prazo.

O tutorial no notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra como construir esta camada unificada de memória, com exemplos práticos de ingestão de diversas fontes de dados, visualização do grafo de conhecimento e consultas com diferentes estratégias de pesquisa adaptadas às necessidades específicas dos agentes.

### Armazenar Memória com RAG

Para além de ferramentas especializadas como Mem0, pode aproveitar serviços robustos de pesquisa como o **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para RAG estruturado.

Isto permite fundamentar as respostas do seu agente com os seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias de viagem específicas do utilizador, catálogos de produtos ou qualquer outro conhecimento de domínio específico.

O Azure AI Search suporta capacidades como o **RAG Estruturado**, que se destaca na extração e recuperação de informação densa e estruturada de grandes conjuntos de dados como históricos de conversa, emails ou mesmo imagens. Isto proporciona "precisão e recall sobre-humanos" comparado com abordagens tradicionais de fragmentação e embedding de texto.

## Tornar os Agentes de IA Autoaperfeiçoáveis

Um padrão comum para agentes autoaperfeiçoáveis envolve introduzir um **"agente do conhecimento"**. Este agente separado observa a conversa principal entre o utilizador e o agente primário. O seu papel é:

1. **Identificar informação valiosa**: Determinar se alguma parte da conversa vale a pena guardar como conhecimento geral ou uma preferência específica do utilizador.

2. **Extrair e resumir**: Destilar o aprendizado essencial ou preferência da conversa.

3. **Armazenar numa base de conhecimento**: Persistir esta informação extraída, frequentemente numa base de dados vetorial, para que possa ser recuperada mais tarde.

4. **Aumentar consultas futuras**: Quando o utilizador inicia uma nova consulta, o agente do conhecimento recupera informação armazenada relevante e a anexa ao prompt do utilizador, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gestão da Latência**: Para evitar atrasos nas interações do utilizador, pode ser usado inicialmente um modelo mais barato e rápido para verificar rapidamente se a informação é valiosa para armazenar ou recuperar, invocando o processo de extração/recuperação mais complexo só quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento em crescimento, a informação menos usada pode ser movida para "armazenamento frio" para gerir custos.

## Tem Mais Perguntas Sobre Memória de Agentes?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.
## Lição Anterior

[Engenharia de Contexto para Agentes de IA](../12-context-engineering/README.md)

## Próxima Lição

[Explorando Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->