# Memória para Agentes de IA 
[![Agent Memory](../../../translated_images/pt-PT/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos da criação de Agentes de IA, são principalmente abordadas duas coisas: a capacidade de chamar ferramentas para completar tarefas e a capacidade de melhorar ao longo do tempo. A memória está na base da criação de um agente autoaperfeiçoador que pode criar melhores experiências para os nossos utilizadores.

Nesta lição, vamos analisar o que é a memória para Agentes de IA e como a podemos gerir e usar em benefício das nossas aplicações.

## Introdução

Esta lição cobrirá:

• **Compreender a Memória dos Agentes de IA**: O que é memória e porque é essencial para os agentes.

• **Implementação e Armazenamento da Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, focando em memória de curto e longo prazo.

• **Tornar os Agentes de IA Autoaperfeiçoáveis**: Como a memória permite que os agentes aprendam de interações passadas e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais completos em notebook:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com o Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente gráfico de conhecimento suportado por embeddings, visualizando o gráfico e recuperação inteligente

## Objetivos de Aprendizagem

Depois de completar esta lição, saberá como:

• **Diferenciar entre vários tipos de memória de agente de IA**, incluindo memória de trabalho, curto prazo e longo prazo, bem como formas especializadas como memória de persona e episódica.

• **Implementar e gerir memória de curto e longo prazo para agentes de IA** usando Microsoft Agent Framework, aproveitando ferramentas como Mem0, Cognee, memória Whiteboard, e integrando com Azure AI Search.

• **Compreender os princípios por trás dos agentes de IA autoaperfeiçoados** e como sistemas robustos de gestão da memória contribuem para o aprendizado contínuo e adaptação.

## Compreender a Memória dos Agentes de IA

Na sua essência, **memória para agentes de IA refere-se aos mecanismos que lhes permitem reter e recordar informação**. Esta informação pode ser detalhes específicos sobre uma conversa, preferências do utilizador, ações passadas ou mesmo padrões aprendidos.

Sem memória, aplicações de IA são frequentemente sem estado, o que significa que cada interação começa do zero. Isto conduz a uma experiência de utilizador repetitiva e frustrante onde o agente "esquece" o contexto ou preferências anteriores.

### Porque é que a Memória é Importante?

a inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informações passadas. A memória permite que os agentes sejam:

• **Reflexivos**: Aprender a partir de ações e resultados passados.

• **Interativos**: Manter o contexto ao longo de uma conversa em curso.

• **Proativos e Reativos**: Antecipar necessidades ou responder apropriadamente com base em dados históricos.

• **Autónomos**: Operar com mais independência tirando partido do conhecimento armazenado.

O objetivo de implementar memória é tornar os agentes mais **fiáveis e capazes**.

### Tipos de Memória

#### Memória de Trabalho

Pense nesta como uma folha de rascunho que o agente usa durante uma única tarefa ou processo de pensamento em curso. Contém informação imediata necessária para calcular o próximo passo.

Para agentes de IA, a memória de trabalho captura frequentemente a informação mais relevante de uma conversa, mesmo que o histórico completo do chat seja longo ou truncado. Foca-se em extrair elementos-chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória de Trabalho**

Num agente de reserva de viagens, a memória de trabalho pode capturar o pedido atual do utilizador, como "Quero reservar uma viagem para Paris". Este requisito específico é mantido no contexto imediato do agente para orientar a interação atual.

#### Memória de Curto Prazo

Este tipo de memória retém informação durante a duração de uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a passos anteriores no diálogo.

Nos exemplos do SDK Python do [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), isto corresponde a `AgentSession`, criado com `agent.create_session()`. A sessão é a memória de curto prazo incorporada no framework: mantém o contexto da conversa disponível enquanto essa sessão é reutilizada, mas esse contexto não é preservado quando a sessão termina ou a aplicação reinicia. Use memória de longo prazo para factos e preferências que precisam de sobreviver a várias sessões, tipicamente através de uma base de dados, índice vetorial ou outro armazenamento persistente.

**Exemplo de Memória de Curto Prazo**

Se um utilizador perguntar "Quanto custaria um voo para Paris?" e depois seguir com "E a acomodação lá?", a memória de curto prazo garante que o agente sabe que "lá" se refere a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Esta é informação que persiste através de múltiplas conversas ou sessões. Permite que os agentes se lembrem de preferências do utilizador, interações históricas ou conhecimento geral ao longo de períodos prolongados. Isto é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esquiar e atividades ao ar livre, gosta de café com vista para a montanha, e quer evitar pistas de esqui avançadas devido a uma lesão passada". Esta informação, aprendida de interações anteriores, influencia recomendações em futuras sessões de planeamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Este tipo especializado de memória ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente se lembre de detalhes sobre si próprio ou sobre o seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**

Se o agente de viagens for desenhado para ser um "planeador de esqui especialista", a memória de persona pode reforçar este papel, influenciando as suas respostas para se alinharem com o tom e conhecimento de um expert.

#### Memória de Fluxo de Trabalho/Episódica

Esta memória armazena a sequência de passos que um agente realiza durante uma tarefa complexa, incluindo sucessos e falhas. É como recordar "episódios" específicos ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico mas falhou devido a indisponibilidade, a memória episódica poderia registar essa falha, permitindo que o agente tente voos alternativos ou informe o utilizador sobre o problema de forma mais informada numa tentativa subsequente.

#### Memória de Entidade

Isto envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos das conversas. Permite que o agente construa uma compreensão estruturada dos elementos chave discutidos.

**Exemplo de Memória de Entidade**

Numa conversa sobre uma viagem passada, o agente pode extrair "Paris," "Torre Eiffel," e "jantar no restaurante Le Chat Noir" como entidades. Numa interação futura, o agente poderia recordar "Le Chat Noir" e oferecer-se para fazer uma nova reserva lá.

#### Structured RAG (Geração Aumentada por Recuperação Estruturada)

Embora RAG seja uma técnica mais ampla, o "Structured RAG" é destacado como uma tecnologia poderosa de memória. Extrai informação densa e estruturada de várias fontes (conversas, emails, imagens) e usa-a para melhorar a precisão, o recall e a rapidez nas respostas. Ao contrário do RAG clássico que depende apenas da similaridade semântica, o Structured RAG trabalha com a estrutura inerente da informação.

**Exemplo de Structured RAG**

Em vez de apenas corresponder palavras-chave, o Structured RAG pode analisar detalhes de voo (destino, data, hora, companhia aérea) a partir de um email e armazená-los de forma estruturada. Isto permite consultas precisas como "Que voo marquei para Paris na terça-feira?"

## Implementação e Armazenamento da Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gestão de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou eliminar) informação. A recuperação é um aspeto particularmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma forma de armazenar e gerir memória dos agentes é usando ferramentas especializadas como Mem0. O Mem0 funciona como uma camada de memória persistente, permitindo que os agentes recordem interações relevantes, armazenem preferências do utilizador e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se transformem em agentes com estado.

Funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao thread de um agente são enviadas ao serviço Mem0, que usa um Modelo de Linguagem Grande (LLM) para resumir o histórico da conversa e extrair novas memórias. Subsequentemente, uma fase de atualização conduzida por LLM determina se deve adicionar, modificar ou eliminar essas memórias, armazenando-as num repositório híbrido que pode incluir bases de dados vetoriais, de grafos, e chave-valor. Este sistema também suporta vários tipos de memória e pode incorporar memória de grafo para gerir relações entre entidades.

#### Cognee

Outra abordagem poderosa é usar o **Cognee**, uma memória semântica open-source para agentes de IA que transforma dados estruturados e não estruturados em gráficos de conhecimento consultáveis suportados por embeddings. O Cognee fornece uma **arquitetura de armazenamento dual** que combina pesquisa por similaridade vetorial com relações em grafos, permitindo que os agentes compreendam não apenas que informação é similar, mas como os conceitos se relacionam entre si.

Destaca-se na **recuperação híbrida** que mistura similaridade vetorial, estrutura de grafos e raciocínio LLM – desde a consulta direta a fragmentos até perguntas conscientes do gráfico. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um gráfico conectado, suportando tanto contexto de sessão de curto prazo como memória persistente de longo prazo.

O tutorial em notebook do Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra a construção desta camada unificada de memória, com exemplos práticos de ingestão de diversas fontes de dados, visualização do gráfico de conhecimento e consulta com diferentes estratégias de pesquisa adaptadas às necessidades específicas do agente.

### Armazenamento de Memória com RAG

Além das ferramentas especializadas de memória como o mem0, pode aproveitar serviços robustos de pesquisa como **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para Structured RAG.

Isto permite fundamentar as respostas do seu agente com os seus próprios dados, garantindo respostas mais relevantes e precisas. Azure AI Search pode ser usado para armazenar memórias de viagens específicas do utilizador, catálogos de produtos, ou qualquer outro conhecimento específico de domínio.

O Azure AI Search suporta capacidades como **Structured RAG**, que se destaca na extração e recuperação de informação densa e estruturada de grandes conjuntos de dados como históricos de conversa, emails ou até imagens. Isto proporciona "precisão e recall sobre-humanos" comparados com abordagens tradicionais de fragmentação de texto e embeddings.

## Tornar os Agentes de IA Autoaperfeiçoáveis

Um padrão comum para agentes autoaperfeiçoáveis envolve a introdução de um **"agente de conhecimento"**. Este agente separado observa a conversa principal entre o utilizador e o agente primário. O seu papel é:

1. **Identificar informação valiosa**: Determinar se alguma parte da conversa vale a pena salvar como conhecimento geral ou preferência específica do utilizador.

2. **Extrair e resumir**: Destilar a aprendizagem ou preferência essencial da conversa.

3. **Armazenar numa base de conhecimento**: Persistir esta informação extraída, frequentemente numa base de dados vetorial, para poder ser recuperada mais tarde.

4. **Aumentar consultas futuras**: Quando o utilizador iniciar uma nova consulta, o agente de conhecimento recupera a informação armazenada relevante e anexa-a ao prompt do utilizador, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para a Memória

• **Gestão de Latência**: Para evitar atrasar as interações do utilizador, pode usar inicialmente um modelo mais barato e rápido para verificar rapidamente se a informação é valiosa para armazenar ou recuperar, invocando o processo de extração/recuperação mais complexo apenas quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento em crescimento, a informação menos frequentemente usada pode ser movida para "armazenamento frio" para gerir custos.

## Tem Mais Perguntas Sobre Memória de Agentes?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar em horas de atendimento e obter respostas às suas questões sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->