# Memória para Agentes de IA 
[![Memória do Agente](../../../translated_images/pt-PT/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos de criar Agentes de IA, são principalmente discutidas duas coisas: a capacidade de chamar ferramentas para completar tarefas e a capacidade de melhorar ao longo do tempo. A memória está na base da criação de um agente autoaperfeiçoado que pode criar experiências melhores para os nossos utilizadores.

Nesta lição, iremos analisar o que é a memória para Agentes de IA e como podemos geri-la e usá-la para benefício das nossas aplicações.

## Introdução

Esta lição irá abranger:

• **Compreender a Memória do Agente de IA**: O que é a memória e por que é essencial para os agentes.

• **Implementar e Armazenar Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, focando na memória de curto e longo prazo.

• **Fazer com que os Agentes de IA se Autoaperfeiçoem**: Como a memória permite que os agentes aprendam com interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais completos em notebooks:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente grafo de conhecimento suportado por embeddings, visualizando o grafo e recuperação inteligente

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

• **Diferenciar entre vários tipos de memória de agente de IA**, incluindo memória de trabalho, de curto prazo e de longo prazo, bem como formas especializadas como memória de persona e episódica.

• **Implementar e gerir memória de curto prazo e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, memória Whiteboard, e integrando com Azure AI Search.

• **Compreender os princípios por trás dos agentes de IA autoaperfeiçoados** e como sistemas robustos de gestão de memória contribuem para aprendizagem contínua e adaptação.

## Compreendendo a Memória do Agente de IA

Na sua essência, **memória para agentes de IA refere-se aos mecanismos que lhes permitem reter e recordar informação**. Esta informação pode ser detalhes específicos sobre uma conversa, preferências do utilizador, ações passadas ou até padrões aprendidos.

Sem memória, as aplicações de IA são frequentemente sem estado, significando que cada interação começa do zero. Isto leva a uma experiência de utilizador repetitiva e frustrante, onde o agente "esquece" o contexto ou preferências anteriores.

### Por que é a Memória Importante?

A inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informação passada. A memória permite que os agentes sejam:

• **Reflexivos**: Aprender com ações e resultados passados.

• **Interativos**: Manter contexto ao longo de uma conversa em curso.

• **Proativos e Reativos**: Antecipar necessidades ou responder adequadamente com base em dados históricos.

• **Autónomos**: Operar de forma mais independente ao recorrer ao conhecimento armazenado.

O objetivo de implementar memória é tornar os agentes mais **fiáveis e capazes**.

### Tipos de Memória

#### Memória de Trabalho

Pense nisto como uma folha de rascunho que um agente usa durante uma única tarefa ou processo de pensamento em curso. Retém informação imediata necessária para computar o próximo passo.

Para agentes de IA, a memória de trabalho frequentemente captura a informação mais relevante de uma conversa, mesmo que o histórico completo do chat seja longo ou truncado. Foca-se em extrair elementos-chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória de Trabalho**

Num agente de reserva de viagens, a memória de trabalho pode capturar o pedido atual do utilizador, como "Quero reservar uma viagem para Paris". Este requisito específico é mantido no contexto imediato do agente para orientar a interação atual.

#### Memória de Curto Prazo

Este tipo de memória retém informação durante a duração de uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a turnos anteriores no diálogo.

**Exemplo de Memória de Curto Prazo**

Se um utilizador perguntar, "Quanto custa um voo para Paris?" e depois seguir com "E quanto custa alojamento lá?", a memória de curto prazo assegura que o agente sabe que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Este é o tipo de informação que persiste através de múltiplas conversas ou sessões. Permite que agentes recordem preferências do utilizador, interações históricas ou conhecimento geral durante períodos prolongados. Isto é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esqui e atividades ao ar livre, aprecia café com vista para a montanha e quer evitar pistas avançadas devido a uma lesão passada". Esta informação, aprendida em interações anteriores, influencia recomendações em futuras sessões de planeamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Este tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente se lembre de detalhes sobre si próprio ou do seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**

Se o agente de viagens é projetado para ser um "especialista em planeamento de esqui", a memória de persona pode reforçar este papel, influenciando as suas respostas para alinhar com o tom e o conhecimento de um especialista.

#### Memória de Fluxo de Trabalho/Episódica

Esta memória armazena a sequência de passos que um agente realiza durante uma tarefa complexa, incluindo sucessos e falhas. É como recordar "episódios" ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico e falhou devido a indisponibilidade, a memória episódica pode registar essa falha, permitindo ao agente tentar voos alternativos ou informar o utilizador sobre o problema de forma mais informada numa tentativa subsequente.

#### Memória de Entidades

Isto envolve extrair e recordar entidades específicas (como pessoas, lugares ou coisas) e eventos de conversas. Permite que o agente construa um entendimento estruturado dos elementos-chave discutidos.

**Exemplo de Memória de Entidades**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris", "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Numa interação futura, o agente poderia recordar "Le Chat Noir" e oferecer fazer uma nova reserva lá.

#### RAG Estruturado (Geração Aumentada por Recuperação)

Embora RAG seja uma técnica mais ampla, o "RAG Estruturado" é destacado como uma tecnologia poderosa de memória. Extrai informação densa e estruturada de várias fontes (conversas, emails, imagens) e usa-a para melhorar a precisão, o recall e a velocidade nas respostas. Ao contrário do RAG clássico, que depende apenas da semelhança semântica, o RAG Estruturado trabalha com a estrutura inerente da informação.

**Exemplo de RAG Estruturado**

Em vez de apenas corresponder palavras-chave, o RAG Estruturado poderia analisar detalhes de um voo (destino, data, hora, companhia aérea) de um email e armazená-los de forma estruturada. Isto permite consultas precisas como "Que voo reservei para Paris na terça-feira?"

## Implementar e Armazenar Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gestão de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou eliminar) informação. A recuperação é um aspeto particularmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma forma de armazenar e gerir a memória do agente é usar ferramentas especializadas como o Mem0. O Mem0 funciona como uma camada de memória persistente, permitindo que agentes recordem interações relevantes, armazenem preferências do utilizador e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se transformem em agentes com estado.

Funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, as mensagens adicionadas a um tópico de agente são enviadas para o serviço Mem0, que usa um Large Language Model (LLM) para resumir o histórico da conversa e extrair novas memórias. Subsequentemente, uma fase de atualização conduzida por LLM determina se deve adicionar, modificar ou eliminar essas memórias, armazenando-as numa base de dados híbrida que pode incluir bases de dados vetoriais, grafo e chave-valor. Este sistema também suporta vários tipos de memória e pode incorporar memória em grafo para gerir relacionamentos entre entidades.

#### Cognee

Outra abordagem poderosa é usar o **Cognee**, uma memória semântica open-source para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis suportados por embeddings. O Cognee fornece uma **arquitetura de armazenamento dupla** combinando pesquisa de similaridade vetorial com relacionamentos em grafo, permitindo aos agentes entender não apenas que informação é similar, mas como os conceitos se relacionam.

Destaca-se pelo **recuperação híbrida** que mistura similaridade vetorial, estrutura de grafo e raciocínio LLM - desde consulta direta de fragmentos brutos até respostas a perguntas conscientes do grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado, suportando tanto o contexto de sessão de curto prazo quanto a memória persistente de longo prazo.

O tutorial em notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra a construção desta camada unificada de memória, com exemplos práticos de ingestão de fontes de dados diversas, visualização do grafo de conhecimento e consultas com diferentes estratégias de pesquisa adaptadas às necessidades específicas do agente.

### Armazenar Memória com RAG

Para além de ferramentas especializadas de memória como o mem0, pode aproveitar serviços robustos de pesquisa como o **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para RAG estruturado.

Isto permite fundamentar as respostas do agente com os seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias de viagens específicas do utilizador, catálogos de produtos, ou qualquer outro conhecimento específico de domínio.

O Azure AI Search suporta capacidades como **RAG Estruturado**, que se destaca na extração e recuperação de informação densa e estruturada de grandes conjuntos de dados, como históricos de conversas, emails ou mesmo imagens. Isto oferece "precisão e recall sobre-humanos" comparado a abordagens tradicionais de segmentação de texto e embeddings.

## Fazer com que os Agentes de IA se Autoaperfeiçoem

Um padrão comum para agentes autoaperfeiçoados envolve introduzir um **"agente de conhecimento"**. Este agente separado observa a conversa principal entre o utilizador e o agente primário. O seu papel é:

1. **Identificar informação valiosa**: Determinar se alguma parte da conversa vale a pena salvar como conhecimento geral ou uma preferência específica do utilizador.

2. **Extrair e resumir**: Destilar a aprendizagem essencial ou preferência da conversa.

3. **Armazenar numa base de conhecimento**: Persistir esta informação extraída, frequentemente numa base de dados vetorial, para que possa ser recuperada mais tarde.

4. **Aumentar consultas futuras**: Quando o utilizador inicia uma nova consulta, o agente de conhecimento recupera a informação armazenada relevante e a acrescenta ao prompt do utilizador, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gestão de Latência**: Para evitar atrasar as interações do utilizador, pode ser usado inicialmente um modelo mais barato e rápido para verificar rapidamente se a informação é valiosa para armazenar ou recuperar, invocando o processo mais complexo de extração/recuperação apenas quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento em crescimento, informação menos usada pode ser movida para "armazenamento frio" para gerir custos.

## Tem mais perguntas sobre Memória de Agentes?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, é recomendada a tradução profissional por um ser humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->