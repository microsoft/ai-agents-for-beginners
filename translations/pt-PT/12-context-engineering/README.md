# Engenharia de Contexto para Agentes de IA

[![Engenharia de Contexto](../../../translated_images/pt-PT/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Clique na imagem acima para ver o vídeo desta aula)_

Compreender a complexidade da aplicação para a qual está a construir um agente de IA é importante para criar um agente fiável. Precisamos construir Agentes de IA que gerem eficazmente a informação para responder a necessidades complexas para além da engenharia de prompts.

Nesta lição, vamos ver o que é a engenharia de contexto e o seu papel na construção de agentes de IA.

## Introdução

Esta lição irá abordar:

• **O que é Engenharia de Contexto** e por que é diferente da engenharia de prompts.

• **Estratégias para uma Engenharia de Contexto eficaz**, incluindo como escrever, selecionar, comprimir e isolar informação.

• **Falhas comuns de contexto** que podem comprometer o seu agente de IA e como as corrigir.

## Objetivos de Aprendizagem

Após completar esta lição, deverá entender como:

• **Definir engenharia de contexto** e diferenciá-la da engenharia de prompts.

• **Identificar os componentes principais do contexto** em aplicações de Modelos de Linguagem Grande (LLM).

• **Aplicar estratégias para escrever, selecionar, comprimir e isolar contexto** para melhorar o desempenho do agente.

• **Reconhecer falhas comuns de contexto** como contaminação, distração, confusão e conflito, e implementar técnicas de mitigação.

## O que é Engenharia de Contexto?

Para os Agentes de IA, o contexto é o que orienta o planeamento de um agente para tomar certas ações. Engenharia de Contexto é a prática de garantir que o agente de IA tem a informação certa para completar o próximo passo da tarefa. A janela de contexto é limitada em tamanho, portanto, como construtores de agentes, precisamos criar sistemas e processos para gerir a adição, remoção e condensação da informação na janela de contexto.

### Engenharia de Prompt vs Engenharia de Contexto

A engenharia de prompt está focada num conjunto único de instruções estáticas para guiar eficazmente os Agentes de IA com um conjunto de regras. A engenharia de contexto trata de como gerir um conjunto dinâmico de informação, incluindo o prompt inicial, para assegurar que o agente de IA tem o que precisa ao longo do tempo. A ideia principal da engenharia de contexto é tornar este processo repetível e fiável.

### Tipos de Contexto

[![Tipos de Contexto](../../../translated_images/pt-PT/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

É importante lembrar que o contexto não é apenas uma coisa. A informação que o agente de IA precisa pode vir de várias fontes diferentes, e cabe a nós garantir que o agente tem acesso a estas fontes:

Os tipos de contexto que um agente de IA pode precisar gerir incluem:

• **Instruções:** São como as "regras" do agente – prompts, mensagens do sistema, exemplos few-shot (mostrando ao IA como fazer algo) e descrições de ferramentas que pode usar. É aqui que o foco da engenharia de prompts se cruza com a engenharia de contexto.

• **Conhecimento:** Abrange factos, informação obtida de bases de dados, ou memórias de longo prazo que o agente acumulou. Isto inclui integrar um sistema de Geração Aumentada por Recuperação (RAG) se um agente precisar de aceder a diferentes bases de conhecimento e bases de dados.

• **Ferramentas:** São as definições de funções externas, APIs e Servidores MCP que o agente pode chamar, juntamente com o feedback (resultados) obtidos ao usá-las.

• **Histórico de Conversa:** O diálogo contínuo com um utilizador. À medida que o tempo passa, estas conversas ficam mais longas e complexas, o que significa que ocupam espaço na janela de contexto.

• **Preferências do Utilizador:** Informação aprendida sobre gostos ou desgostos de um utilizador ao longo do tempo. Estas podem ser armazenadas e chamadas quando são tomadas decisões chave para ajudar o utilizador.

## Estratégias para uma Engenharia de Contexto Eficaz

### Estratégias de Planeamento

[![Melhores Práticas de Engenharia de Contexto](../../../translated_images/pt-PT/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Uma boa engenharia de contexto começa com um bom planeamento. Aqui está uma abordagem que o ajudará a começar a pensar em como aplicar o conceito de engenharia de contexto:

1. **Definir Resultados Claros** - Os resultados das tarefas atribuídas aos Agentes de IA devem estar claramente definidos. Responda à pergunta - "Como será o mundo quando o agente de IA terminar a sua tarefa?" Em outras palavras, que mudança, informação ou resposta o utilizador deverá ter após interagir com o agente de IA.
2. **Mapear o Contexto** - Depois de definir os resultados do agente, precisa responder à pergunta "Que informação o agente de IA precisa para completar esta tarefa?". Assim pode começar a mapear o contexto de onde essa informação pode ser encontrada.
3. **Criar Fluxos de Contexto** - Agora que sabe onde está a informação, precisa responder à pergunta "Como é que o Agente vai obter esta informação?". Isto pode ser feito de várias maneiras, incluindo RAG, uso de servidores MCP e outras ferramentas.

### Estratégias Práticas

O planeamento é importante, mas assim que a informação começa a fluir para a janela de contexto do nosso agente, precisamos de estratégias práticas para gerir isso:

#### Gerir o Contexto

Embora alguma informação seja adicionada automaticamente à janela de contexto, a engenharia de contexto implica assumir um papel mais ativo nessa informação, o que pode ser feito através de algumas estratégias:

 1. **Bloco de Notas do Agente**
 Isso permite que um agente de IA tome notas de informação relevante sobre as tarefas atuais e interações com o utilizador durante uma única sessão. Deve existir fora da janela de contexto, num ficheiro ou objeto em runtime que o agente pode depois recuperar durante essa sessão, se necessário.

 2. **Memórias**
 Blocos de notas são bons para gerir informações fora da janela de contexto de uma única sessão. Memórias permitem que agentes armazenem e recuperem informação relevante ao longo de múltiplas sessões. Isto pode incluir resumos, preferências do utilizador e feedback para melhorias futuras.

 3. **Comprimir o Contexto**
  Assim que a janela de contexto cresce e está próxima do seu limite, técnicas como sumarização e aparar podem ser usadas. Isto inclui quer manter apenas a informação mais relevante, quer remover mensagens antigas.
  
 4. **Sistemas Multiagente**
  Desenvolver sistemas multiagente é uma forma de engenharia de contexto porque cada agente tem a sua própria janela de contexto. Como esse contexto é partilhado e passado a diferentes agentes é outra coisa a planear ao construir estes sistemas.
  
 5. **Ambientes Sandbox**
  Se um agente precisar executar um código ou processar grandes quantidades de informação num documento, isso pode requerer muitos tokens para processar os resultados. Em vez de ter tudo isto armazenado na janela de contexto, o agente pode usar um ambiente sandbox capaz de executar esse código e apenas ler os resultados e outra informação relevante.
  
 6. **Objetos de Estado em Runtime**
   Isto é feito criando contentores de informação para gerir situações em que o agente precisa de aceder a certa informação. Para uma tarefa complexa, isto permitiria a um agente armazenar os resultados de cada subtarefa passo a passo, permitindo que o contexto se mantenha ligado apenas àquela subtarefa específica.

#### Inspeção do Contexto

Depois de aplicar uma destas estratégias, vale a pena verificar o que a próxima chamada ao modelo realmente recebeu. Uma questão útil para depuração é:

> O agente carregou demasiado contexto, contexto errado, ou faltou contexto necessário?

Não precisa de registar prompts brutos, saídas de ferramentas ou conteúdos de memória para responder a essa questão. Em produção, prefira pequenos registos de inspeção de contexto que capturem contagens, ids, hashes e etiquetas de política:

- **Seleção:** Trace quantos fragmentos candidatos, ferramentas ou memórias foram considerados, quantos foram selecionados e qual a regra ou pontuação que causou a filtragem dos outros.
- **Compressão:** Registe o intervalo fonte ou id de traço, o id do resumo, uma contagem estimada de tokens antes e depois da compressão, e se o conteúdo bruto foi excluído da próxima chamada.
- **Isolamento:** Anote qual subtarefa foi executada num agente, sessão, ou sandbox separado, qual resumo limitado foi retornado, e se a saída grande de ferramentas ficou fora do contexto do agente principal.
- **Memória e RAG:** Armazene ids dos documentos de recuperação, ids de memória, pontuações, ids selecionados, e estado da redação em vez do texto íntegro recuperado.
- **Segurança e privacidade:** Prefira hashes, ids, baldes de tokens, e etiquetas de política em vez de texto sensível de prompts, argumentos, resultados de ferramentas ou conteúdo da memória do utilizador.

O objetivo não é manter mais contexto. É deixar evidências suficientes para que um desenvolvedor possa identificar qual estratégia de contexto foi aplicada e se isso alterou a próxima chamada ao modelo da forma pretendida.

### Exemplo de Engenharia de Contexto

Digamos que queremos que um agente de IA **"Reserve-me uma viagem para Paris."**

• Um agente simples usando apenas engenharia de prompt poderia responder apenas: **"Ok, quando gostaria de ir para Paris?"**. Apenas processou a sua pergunta direta no momento em que foi feita.

• Um agente usando as estratégias de engenharia de contexto abordadas faria muito mais. Antes de responder, o seu sistema poderia:

  ◦ **Verificar o seu calendário** para datas disponíveis (recuperando dados em tempo real).

 ◦ **Recordar preferências de viagem passadas** (da memória de longo prazo) como a companhia aérea preferida, orçamento, ou se prefere voos diretos.

 ◦ **Identificar ferramentas disponíveis** para reserva de voos e hotéis.

- Depois, uma resposta exemplo poderia ser:  "Olá [Seu Nome]! Vejo que está disponível na primeira semana de Outubro. Devo procurar voos diretos para Paris na [Companhia Aérea Preferida] dentro do seu orçamento habitual de [Orçamento]?". Esta resposta mais rica e consciente do contexto demonstra o poder da engenharia de contexto.

## Falhas Comuns de Contexto

### Contaminação do Contexto

**O que é:** Quando uma alucinação (informação falsa gerada pelo LLM) ou um erro entra no contexto e é repetidamente referenciada, fazendo o agente perseguir objetivos impossíveis ou desenvolver estratégias sem sentido.

**O que fazer:** Implementar **validação de contexto** e **quarentena**. Validar a informação antes de ser adicionada à memória de longo prazo. Se for detectada contaminação potencial, começar novos tópicos de contexto para evitar que a má informação se espalhe.

**Exemplo de Reserva de Viagem:** O seu agente alucina um **voo direto de um pequeno aeroporto local para uma cidade internacional distante** que, na realidade, não oferece voos internacionais. Este detalhe inexistente fica guardado no contexto. Mais tarde, quando pedir para reservar, ele continua a tentar encontrar bilhetes para esta rota impossível, levando a erros repetidos.

**Solução:** Implementar uma etapa que **valide a existência e rotas dos voos com uma API em tempo real** _antes_ de adicionar o detalhe do voo ao contexto de trabalho do agente. Se a validação falhar, a informação errada é "colocada em quarentena" e não usada mais.

### Distração do Contexto

**O que é:** Quando o contexto se torna tão grande que o modelo se foca demasiado no historial acumulado em vez de usar o que aprendeu durante o treino, levando a ações repetitivas ou inúteis. Modelos podem começar a cometer erros mesmo antes da janela de contexto estar cheia.

**O que fazer:** Usar **sumarização de contexto**. Periodicamente comprimir a informação acumulada em resumos mais curtos, mantendo detalhes importantes e removendo histórico redundante. Isto ajuda a "redefinir" o foco.

**Exemplo de Reserva de Viagem:** Tem discutido vários destinos de sonho durante muito tempo, incluindo um relato detalhado da sua viagem de mochila de há dois anos. Quando finalmente pede para **"encontrar um voo barato para o próximo mês,"** o agente fica preso em detalhes antigos e irrelevantes e continua a perguntar sobre o seu equipamento de mochila ou itinerários passados, ignorando o pedido atual.

**Solução:** Após um certo número de interações ou quando o contexto cresce demasiado, o agente deve **resumir as partes mais recentes e relevantes da conversa** – focando nas datas e destino atuais – e usar esse resumo condensado para a próxima chamada ao LLM, descartando o chat histórico menos relevante.

### Confusão de Contexto

**O que é:** Quando contexto desnecessário, muitas vezes sob a forma de demasiadas ferramentas disponíveis, faz com que o modelo gere respostas erradas ou chame ferramentas irrelevantes. Modelos menores são especialmente suscetíveis a isto.

**O que fazer:** Implementar **gestão da carga de ferramentas** usando técnicas RAG. Armazenar descrições das ferramentas numa base de dados vetorial e selecionar _apenas_ as ferramentas mais relevantes para cada tarefa específica. Pesquisas mostram limitar as seleções a menos de 30 ferramentas.

**Exemplo de Reserva de Viagem:** O seu agente tem acesso a dezenas de ferramentas: `reservar_voo`, `reservar_hotel`, `alugar_carro`, `encontrar_tours`, `conversor_moeda`, `previsao_tempo`, `reservas_restaurante`, etc. Você pergunta, **"Qual é a melhor maneira de se deslocar em Paris?"** Devido ao grande número de ferramentas, o agente fica confuso e tenta chamar `reservar_voo` _dentro de_ Paris, ou `alugar_carro` mesmo que prefira transporte público, porque as descrições das ferramentas podem sobrepor-se ou não consegue discernir a melhor.

**Solução:** Usar **RAG sobre descrições de ferramentas**. Quando perguntar sobre se deslocar em Paris, o sistema recupera dinamicamente _apenas_ as ferramentas mais relevantes como `alugar_carro` ou `info_transporte_publico` com base na sua consulta, apresentando uma "carga" focada de ferramentas ao LLM.

### Conflito de Contexto

**O que é:** Quando existe informação contraditória dentro do contexto, levando a raciocínios inconsistentes ou respostas finais erradas. Isto acontece frequentemente quando a informação chega em fases, e pressupostos incorretos iniciais permanecem no contexto.

**O que fazer:** Usar **poda de contexto** e **descarga**. Poda significa remover informação desatualizada ou conflituosa à medida que chegam novos detalhes. Descarga oferece ao modelo um espaço de trabalho "bloco de notas" separado para processar informação sem poluir o contexto principal.


**Exemplo de Reserva de Viagem:** Inicialmente diz ao seu agente, **"Quero viajar em classe económica."** Mais tarde na conversa, muda de opinião e diz, **"Na verdade, para esta viagem, vamos em classe executiva."** Se ambas as instruções permanecerem no contexto, o agente pode receber resultados de pesquisa conflitantes ou ficar confuso sobre qual preferência deve priorizar.

**Solução:** Implemente **poda de contexto**. Quando uma nova instrução contradiz uma mais antiga, a instrução mais antiga é removida ou explicitamente substituída no contexto. Alternativamente, o agente pode usar um **quadro de rascunho** para reconciliar preferências conflitantes antes de decidir, garantindo que só a instrução final e consistente guie as suas ações.

## Tem Mais Perguntas Sobre Engenharia de Contexto?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.
## Lição Anterior

[Protocolos Agentes](../11-agentic-protocols/README.md)

## Próxima Lição

[Memória para Agentes de IA](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->