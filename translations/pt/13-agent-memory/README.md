<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1d90991499ad697c4ad24decaf36968",
  "translation_date": "2025-12-09T12:14:54+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "pt"
}
-->
# Memória para Agentes de IA 
[![Memória do Agente](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.pt.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Ao discutir os benefícios únicos de criar Agentes de IA, dois pontos principais são abordados: a capacidade de utilizar ferramentas para realizar tarefas e a capacidade de melhorar ao longo do tempo. A memória é a base para criar agentes autossuficientes que proporcionam melhores experiências aos nossos utilizadores.

Nesta lição, vamos explorar o que é memória para Agentes de IA e como podemos geri-la e utilizá-la para beneficiar as nossas aplicações.

## Introdução

Esta lição abordará:

• **Compreender a Memória de Agentes de IA**: O que é memória e por que é essencial para os agentes.

• **Implementar e Armazenar Memória**: Métodos práticos para adicionar capacidades de memória aos seus agentes de IA, com foco em memória de curto e longo prazo.

• **Tornar os Agentes de IA Autossuficientes**: Como a memória permite que os agentes aprendam com interações anteriores e melhorem ao longo do tempo.

## Implementações Disponíveis

Esta lição inclui dois tutoriais completos em notebooks:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementa memória usando Mem0 e Azure AI Search com o framework Semantic Kernel.

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementa memória estruturada usando Cognee, construindo automaticamente um grafo de conhecimento baseado em embeddings, visualizando o grafo e realizando recuperação inteligente.

## Objetivos de Aprendizagem

Após completar esta lição, saberá como:

• **Diferenciar entre os vários tipos de memória de agentes de IA**, incluindo memória de trabalho, de curto prazo e de longo prazo, bem como formas especializadas como memória de persona e episódica.

• **Implementar e gerir memória de curto e longo prazo para agentes de IA** usando o framework Semantic Kernel, aproveitando ferramentas como Mem0, Cognee, memória de quadro branco e integração com Azure AI Search.

• **Compreender os princípios por trás de agentes de IA autossuficientes** e como sistemas robustos de gestão de memória contribuem para aprendizagem e adaptação contínuas.

## Compreender a Memória de Agentes de IA

No seu núcleo, **memória para agentes de IA refere-se aos mecanismos que lhes permitem reter e recordar informações**. Estas informações podem incluir detalhes específicos sobre uma conversa, preferências do utilizador, ações anteriores ou até padrões aprendidos.

Sem memória, as aplicações de IA são frequentemente sem estado, o que significa que cada interação começa do zero. Isso leva a uma experiência repetitiva e frustrante para o utilizador, onde o agente "esquece" o contexto ou as preferências anteriores.

### Por que a Memória é Importante?

A inteligência de um agente está profundamente ligada à sua capacidade de recordar e utilizar informações passadas. A memória permite que os agentes sejam:

• **Reflexivos**: Aprender com ações e resultados anteriores.

• **Interativos**: Manter o contexto ao longo de uma conversa contínua.

• **Proativos e Reativos**: Antecipar necessidades ou responder adequadamente com base em dados históricos.

• **Autónomos**: Operar de forma mais independente ao recorrer a conhecimentos armazenados.

O objetivo de implementar memória é tornar os agentes mais **fiáveis e capazes**.

### Tipos de Memória

#### Memória de Trabalho

Pense nela como um pedaço de papel de rascunho que um agente usa durante uma única tarefa ou processo de pensamento em andamento. Ela mantém informações imediatas necessárias para calcular o próximo passo.

Para agentes de IA, a memória de trabalho frequentemente captura as informações mais relevantes de uma conversa, mesmo que o histórico completo do chat seja longo ou truncado. Ela foca em extrair elementos-chave como requisitos, propostas, decisões e ações.

**Exemplo de Memória de Trabalho**

Num agente de reserva de viagens, a memória de trabalho pode capturar o pedido atual do utilizador, como "Quero reservar uma viagem para Paris". Este requisito específico é mantido no contexto imediato do agente para orientar a interação atual.

#### Memória de Curto Prazo

Este tipo de memória retém informações durante uma única conversa ou sessão. É o contexto do chat atual, permitindo que o agente se refira a turnos anteriores no diálogo.

**Exemplo de Memória de Curto Prazo**

Se um utilizador perguntar, "Quanto custa um voo para Paris?" e depois seguir com "E quanto à acomodação lá?", a memória de curto prazo garante que o agente saiba que "lá" refere-se a "Paris" dentro da mesma conversa.

#### Memória de Longo Prazo

Esta é a informação que persiste ao longo de várias conversas ou sessões. Permite que os agentes se lembrem de preferências do utilizador, interações históricas ou conhecimentos gerais por períodos prolongados. Isto é importante para personalização.

**Exemplo de Memória de Longo Prazo**

Uma memória de longo prazo pode armazenar que "Ben gosta de esquiar e atividades ao ar livre, prefere café com vista para a montanha e quer evitar pistas de esqui avançadas devido a uma lesão anterior". Esta informação, aprendida em interações anteriores, influencia recomendações em futuras sessões de planeamento de viagens, tornando-as altamente personalizadas.

#### Memória de Persona

Este tipo de memória especializado ajuda um agente a desenvolver uma "personalidade" ou "persona" consistente. Permite que o agente se lembre de detalhes sobre si mesmo ou sobre o seu papel pretendido, tornando as interações mais fluidas e focadas.

**Exemplo de Memória de Persona**
Se o agente de viagens for projetado para ser um "especialista em planeamento de esqui", a memória de persona pode reforçar este papel, influenciando as suas respostas para alinhar-se com o tom e conhecimento de um especialista.

#### Memória de Fluxo/Episódica

Esta memória armazena a sequência de passos que um agente realiza durante uma tarefa complexa, incluindo sucessos e falhas. É como lembrar "episódios" específicos ou experiências passadas para aprender com eles.

**Exemplo de Memória Episódica**

Se o agente tentou reservar um voo específico, mas falhou devido à indisponibilidade, a memória episódica pode registrar esta falha, permitindo que o agente tente voos alternativos ou informe o utilizador sobre o problema de forma mais informada numa tentativa subsequente.

#### Memória de Entidade

Isto envolve extrair e lembrar entidades específicas (como pessoas, lugares ou coisas) e eventos de conversas. Permite que o agente construa uma compreensão estruturada dos elementos-chave discutidos.

**Exemplo de Memória de Entidade**

De uma conversa sobre uma viagem passada, o agente pode extrair "Paris", "Torre Eiffel" e "jantar no restaurante Le Chat Noir" como entidades. Numa interação futura, o agente pode recordar "Le Chat Noir" e oferecer-se para fazer uma nova reserva lá.

#### RAG Estruturado (Geração Aumentada por Recuperação)

Embora o RAG seja uma técnica mais ampla, o "RAG Estruturado" é destacado como uma tecnologia de memória poderosa. Ele extrai informações densas e estruturadas de várias fontes (conversas, e-mails, imagens) e usa-as para melhorar a precisão, recuperação e velocidade nas respostas. Diferentemente do RAG clássico que depende apenas de similaridade semântica, o RAG Estruturado trabalha com a estrutura inerente da informação.

**Exemplo de RAG Estruturado**

Em vez de apenas corresponder palavras-chave, o RAG Estruturado pode analisar detalhes de voos (destino, data, hora, companhia aérea) de um e-mail e armazená-los de forma estruturada. Isso permite consultas precisas como "Qual voo reservei para Paris na terça-feira?"

## Implementar e Armazenar Memória

Implementar memória para agentes de IA envolve um processo sistemático de **gestão de memória**, que inclui gerar, armazenar, recuperar, integrar, atualizar e até "esquecer" (ou eliminar) informações. A recuperação é um aspeto particularmente crucial.

### Ferramentas Especializadas de Memória

#### Mem0

Uma forma de armazenar e gerir memória de agentes é usar ferramentas especializadas como Mem0. Mem0 funciona como uma camada de memória persistente, permitindo que os agentes recordem interações relevantes, armazenem preferências do utilizador e contexto factual, e aprendam com sucessos e falhas ao longo do tempo. A ideia aqui é que agentes sem estado se transformem em agentes com estado.

Funciona através de um **pipeline de memória em duas fases: extração e atualização**. Primeiro, mensagens adicionadas ao thread de um agente são enviadas ao serviço Mem0, que usa um Modelo de Linguagem Grande (LLM) para resumir o histórico de conversas e extrair novas memórias. Posteriormente, uma fase de atualização orientada por LLM determina se deve adicionar, modificar ou eliminar essas memórias, armazenando-as num repositório de dados híbrido que pode incluir bases de dados de vetor, grafo e chave-valor. Este sistema também suporta vários tipos de memória e pode incorporar memória de grafo para gerir relações entre entidades.

#### Cognee

Outra abordagem poderosa é usar **Cognee**, uma memória semântica de código aberto para agentes de IA que transforma dados estruturados e não estruturados em grafos de conhecimento consultáveis, apoiados por embeddings. Cognee fornece uma **arquitetura de armazenamento duplo** que combina pesquisa por similaridade de vetor com relações de grafo, permitindo que os agentes compreendam não apenas o que é semelhante, mas como os conceitos se relacionam entre si.

Ele destaca-se na **recuperação híbrida**, que combina similaridade de vetor, estrutura de grafo e raciocínio LLM - desde a pesquisa de fragmentos brutos até respostas a perguntas conscientes do grafo. O sistema mantém uma **memória viva** que evolui e cresce enquanto permanece consultável como um grafo conectado, suportando tanto o contexto de sessão de curto prazo quanto a memória persistente de longo prazo.

O tutorial em notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstra a construção desta camada de memória unificada, com exemplos práticos de ingestão de diversas fontes de dados, visualização do grafo de conhecimento e consulta com diferentes estratégias de pesquisa adaptadas às necessidades específicas do agente.

### Armazenar Memória com RAG

Além de ferramentas especializadas de memória como Mem0, pode aproveitar serviços de pesquisa robustos como **Azure AI Search como backend para armazenar e recuperar memórias**, especialmente para RAG estruturado.

Isso permite fundamentar as respostas do agente com os seus próprios dados, garantindo respostas mais relevantes e precisas. O Azure AI Search pode ser usado para armazenar memórias específicas do utilizador sobre viagens, catálogos de produtos ou qualquer outro conhecimento específico de domínio.

O Azure AI Search suporta capacidades como **RAG Estruturado**, que destaca-se na extração e recuperação de informações densas e estruturadas de grandes conjuntos de dados como históricos de conversas, e-mails ou até imagens. Isso proporciona "precisão e recuperação super-humanas" em comparação com abordagens tradicionais de fragmentação de texto e embeddings.

## Tornar os Agentes de IA Autossuficientes

Um padrão comum para agentes autossuficientes envolve introduzir um **"agente de conhecimento"**. Este agente separado observa a conversa principal entre o utilizador e o agente primário. O seu papel é:

1. **Identificar informações valiosas**: Determinar se alguma parte da conversa vale a pena ser guardada como conhecimento geral ou uma preferência específica do utilizador.

2. **Extrair e resumir**: Destilar o aprendizado ou preferência essencial da conversa.

3. **Armazenar numa base de conhecimento**: Persistir esta informação extraída, frequentemente numa base de dados de vetor, para que possa ser recuperada mais tarde.

4. **Aumentar consultas futuras**: Quando o utilizador inicia uma nova consulta, o agente de conhecimento recupera informações armazenadas relevantes e adiciona-as ao prompt do utilizador, fornecendo contexto crucial ao agente primário (semelhante ao RAG).

### Otimizações para Memória

• **Gestão de Latência**: Para evitar atrasos nas interações do utilizador, um modelo mais barato e rápido pode ser usado inicialmente para verificar rapidamente se a informação é valiosa para armazenar ou recuperar, invocando apenas o processo de extração/recuperação mais complexo quando necessário.

• **Manutenção da Base de Conhecimento**: Para uma base de conhecimento em crescimento, informações menos utilizadas podem ser movidas para "armazenamento frio" para gerir custos.

## Tem Mais Perguntas Sobre Memória de Agentes?

Junte-se ao [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->