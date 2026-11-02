# Engenharia de Contexto para Agentes de IA

[![Engenharia de Contexto](../../../translated_images/pt-BR/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

Entender a complexidade da aplicação para a qual você está construindo um agente de IA é importante para criar um agente confiável. Precisamos construir agentes de IA que gerenciem a informação de forma eficaz para atender necessidades complexas além da engenharia de prompt.

Nesta lição, vamos examinar o que é engenharia de contexto e seu papel na construção de agentes de IA.

## Introdução

Esta lição abordará:

• **O que é Engenharia de Contexto** e por que é diferente da engenharia de prompt.

• **Estratégias para uma Engenharia de Contexto eficaz**, incluindo como escrever, selecionar, comprimir e isolar informações.

• **Falhas comuns de Contexto** que podem atrapalhar seu agente de IA e como corrigí-las.

## Objetivos de Aprendizagem

Após completar esta lição, você entenderá como:

• **Definir engenharia de contexto** e diferenciá-la da engenharia de prompt.

• **Identificar os principais componentes do contexto** em aplicações de Modelos de Linguagem de Grande Porte (LLM).

• **Aplicar estratégias para escrever, selecionar, comprimir e isolar contexto** para melhorar o desempenho do agente.

• **Reconhecer falhas comuns de contexto** como envenenamento, distração, confusão e conflito, e implementar técnicas de mitigação.

## O que é Engenharia de Contexto?

Para agentes de IA, contexto é o que direciona o planejamento do agente para tomar certas ações. Engenharia de Contexto é a prática de garantir que o agente de IA tenha a informação certa para completar a próxima etapa da tarefa. A janela de contexto é limitada em tamanho, então, como construtores de agentes, precisamos construir sistemas e processos para gerenciar a adição, remoção e condensação da informação na janela de contexto.

### Engenharia de Prompt vs Engenharia de Contexto

Engenharia de prompt está focada em um conjunto único de instruções estáticas para guiar efetivamente os agentes de IA com um conjunto de regras. Engenharia de contexto é como gerenciar um conjunto dinâmico de informações, incluindo o prompt inicial, para garantir que o agente de IA tenha o que precisa ao longo do tempo. A ideia principal da engenharia de contexto é tornar esse processo repetível e confiável.

### Tipos de Contexto

[![Tipos de Contexto](../../../translated_images/pt-BR/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

É importante lembrar que contexto não é apenas uma coisa. A informação que o agente de IA precisa pode vir de várias fontes diferentes e cabe a nós garantir que o agente tenha acesso a essas fontes:

Os tipos de contexto que um agente de IA pode precisar gerenciar incluem:

• **Instruções:** São como as "regras" do agente – prompts, mensagens do sistema, exemplos few-shot (mostrando à IA como fazer algo), e descrições de ferramentas que ele pode usar. Aqui é onde o foco da engenharia de prompt se combina com a engenharia de contexto.

• **Conhecimento:** Abrange fatos, informações recuperadas de bancos de dados ou memórias de longo prazo que o agente acumulou. Isso inclui integrar um sistema Retrieval Augmented Generation (RAG) se um agente precisar acessar diferentes fontes de conhecimento e bancos de dados.

• **Ferramentas:** São as definições de funções externas, APIs e servidores MCP que o agente pode chamar, junto com o feedback (resultados) que obtém ao usá-las.

• **Histórico de Conversa:** O diálogo contínuo com um usuário. Com o tempo, essas conversas ficam mais longas e complexas, o que significa que ocupam espaço na janela de contexto.

• **Preferências do Usuário:** Informações aprendidas sobre gostos ou desgostos do usuário ao longo do tempo. Essas informações podem ser armazenadas e chamadas ao tomar decisões importantes para ajudar o usuário.

## Estratégias para uma Engenharia de Contexto Eficaz

### Estratégias de Planejamento

[![Melhores Práticas de Engenharia de Contexto](../../../translated_images/pt-BR/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Uma boa engenharia de contexto começa com um bom planejamento. Aqui está uma abordagem que ajudará você a começar a pensar em como aplicar o conceito de engenharia de contexto:

1. **Defina Resultados Claros** - Os resultados das tarefas que os agentes de IA irão executar devem ser claramente definidos. Responda à pergunta - "Como o mundo estará quando o agente de IA concluir sua tarefa?" Em outras palavras, qual mudança, informação ou resposta o usuário deve receber após interagir com o agente de IA.
2. **Mapeie o Contexto** - Depois de definir os resultados do agente de IA, você precisa responder à pergunta: "Que informações o agente de IA precisa para completar essa tarefa?". Assim, você pode começar a mapear o contexto de onde essas informações podem estar localizadas.
3. **Crie Pipelines de Contexto** - Agora que você sabe onde está a informação, precisa responder à pergunta "Como o agente obterá essa informação?". Isso pode ser feito de várias maneiras, incluindo RAG, uso de servidores MCP e outras ferramentas.

### Estratégias Práticas

Planejamento é importante, mas quando a informação começa a fluir na janela de contexto do nosso agente, precisamos ter estratégias práticas para gerenciá-la:

#### Gerenciamento de Contexto

Embora alguma informação seja adicionada automaticamente à janela de contexto, engenharia de contexto é assumir um papel mais ativo sobre essa informação, o que pode ser feito por algumas estratégias:

 1. **Bloco de Notas do Agente**
 Isso permite que um agente de IA tome notas de informações relevantes sobre as tarefas atuais e interações com o usuário durante uma única sessão. Isso deve existir fora da janela de contexto em um arquivo ou objeto de tempo de execução que o agente possa recuperar durante essa sessão, se necessário.

 2. **Memórias**
 Blocos de notas são bons para gerenciar informações fora da janela de contexto de uma única sessão. Memórias permitem que os agentes armazenem e recuperem informações relevantes ao longo de múltiplas sessões. Isso pode incluir resumos, preferências do usuário e feedback para melhorias futuras.

 3. **Comprimir Contexto**
  Quando a janela de contexto cresce e está se aproximando do limite, técnicas como sumarização e corte podem ser usadas. Isso inclui manter apenas a informação mais relevante ou remover mensagens antigas.
  
 4. **Sistemas Multi-Agentes**
  Desenvolver um sistema multi-agentes é uma forma de engenharia de contexto porque cada agente tem sua própria janela de contexto. Como esse contexto é compartilhado e passado para diferentes agentes é outra coisa a planejar ao construir esses sistemas.
  
 5. **Ambientes Sandbox**
  Se um agente precisa executar algum código ou processar grandes quantidades de informação em um documento, isso pode consumir muitos tokens para processar os resultados. Em vez de armazenar tudo isso na janela de contexto, o agente pode usar um ambiente sandbox que é capaz de executar esse código e ler apenas os resultados e outras informações relevantes.
  
 6. **Objetos de Estado em Tempo de Execução**
   Isso é feito criando contêineres de informação para gerenciar situações em que o agente precisa ter acesso a certas informações. Para uma tarefa complexa, isso permitiria que um agente armazenasse os resultados de cada subtarefa passo a passo, permitindo que o contexto permanecesse conectado apenas àquela subtarefa específica.

#### Inspecionando o Contexto

Depois de aplicar uma dessas estratégias, vale a pena verificar o que a próxima chamada ao modelo realmente recebeu. Uma pergunta útil para depuração é:

> O agente carregou contexto demais, contexto errado ou deixou de carregar contexto necessário?

Você não precisa registrar prompts brutos, saídas de ferramentas ou conteúdos da memória para responder a essa pergunta. Em produção, prefira pequenos registros de inspeção de contexto que capturem contagens, ids, hashes e rótulos de política:

- **Seleção:** Rastreie quantos blocos candidatos, ferramentas ou memórias foram considerados, quantos foram selecionados e qual regra ou pontuação causou o filtro dos demais.
- **Compressão:** Registre o intervalo de origem ou id de rastreamento, o id do resumo, uma contagem estimada de tokens antes e depois da compressão, e se o conteúdo bruto foi excluído da próxima chamada.
- **Isolamento:** Anote qual subtarefa rodou em agente, sessão ou sandbox separado, qual resumo limitado foi retornado e se a grande saída das ferramentas ficou fora do contexto do agente principal.
- **Memória e RAG:** Armazene ids de documentos de recuperação, ids de memória, pontuações, ids selecionados e status de redacção em vez do texto completo recuperado.
- **Segurança e privacidade:** Prefira hashes, ids, baldes de tokens e rótulos de política em vez de texto sensível do prompt, argumentos de ferramentas, resultados de ferramentas ou conteúdos de memória do usuário.

O objetivo não é manter mais contexto. É deixar evidências suficientes para que um desenvolvedor possa saber qual estratégia de contexto foi aplicada e se ela alterou a próxima chamada ao modelo da forma pretendida.

### Exemplo de Engenharia de Contexto

Digamos que queremos que um agente de IA **"Reserve uma viagem para Paris para mim."**

• Um agente simples usando apenas engenharia de prompt poderia responder: **"Ok, quando você gostaria de ir para Paris?"**. Ele só processou sua pergunta direta no momento em que o usuário perguntou.

• Um agente usando as estratégias de engenharia de contexto abordadas faria muito mais. Antes mesmo de responder, seu sistema poderia:

  ◦ **Verificar seu calendário** para datas disponíveis (recuperando dados em tempo real).

 ◦ **Relembrar preferências de viagem passadas** (da memória de longo prazo) como sua companhia aérea preferida, orçamento ou se prefere voos diretos.

 ◦ **Identificar ferramentas disponíveis** para reserva de voos e hotéis.

- Então, uma resposta exemplo poderia ser: "Olá [Seu Nome]! Vejo que você está livre na primeira semana de outubro. Devo procurar voos diretos para Paris pela [Companhia Aérea Preferida] dentro do seu orçamento usual de [Orçamento]?" Essa resposta mais rica e consciente do contexto demonstra o poder da engenharia de contexto.

## Falhas Comuns de Contexto

### Envenenamento de Contexto

**O que é:** Quando uma alucinação (informação falsa gerada pelo LLM) ou erro entra no contexto e é repetidamente referenciada, fazendo com que o agente persiga objetivos impossíveis ou desenvolva estratégias sem sentido.

**O que fazer:** Implemente **validação de contexto** e **quarentena**. Valide informações antes de adicioná-las à memória de longo prazo. Se for detectado potencial envenenamento, inicie novos tópicos de contexto para evitar que a má informação se espalhe.

**Exemplo de Reserva de Viagem:** Seu agente alucina um **voo direto de um pequeno aeroporto local para uma cidade internacional distante** que na verdade não oferece voos internacionais. Esse detalhe inexistente do voo é salvo no contexto. Depois, quando você pede para reservar, ele continua tentando encontrar passagens para essa rota impossível, levando a erros repetidos.

**Solução:** Implemente uma etapa que **valide a existência do voo e rotas com uma API em tempo real** _antes_ de adicionar o detalhe do voo ao contexto de trabalho do agente. Se a validação falhar, a informação errada é "quarentenada" e não é usada subsequentemente.

### Distração de Contexto

**O que é:** Quando o contexto fica tão grande que o modelo foca demais no histórico acumulado em vez de usar o que aprendeu durante o treinamento, levando a ações repetitivas ou inúteis. Modelos podem começar a cometer erros mesmo antes da janela de contexto estar cheia.

**O que fazer:** Use **sumarização de contexto**. Periodicamente comprima a informação acumulada em resumos mais curtos, mantendo detalhes importantes enquanto remove histórico redundante. Isso ajuda a "resetar" o foco.

**Exemplo de Reserva de Viagem:** Você tem discutido vários destinos dos sonhos por muito tempo, incluindo um relato detalhado da sua viagem mochileira de dois anos atrás. Quando finalmente pede para **"encontrar um voo barato para o próximo mês"**, o agente fica atolado nos detalhes antigos e irrelevantes, e continua perguntando sobre seu equipamento de mochila ou itinerários passados, negligenciando seu pedido atual.

**Solução:** Após certo número de interações ou quando o contexto crescer demais, o agente deve **resumir as partes mais recentes e relevantes da conversa** – focando nas suas datas e destino atuais – e usar esse resumo condensado para a próxima chamada ao LLM, descartando o histórico menos relevante.

### Confusão de Contexto

**O que é:** Quando contexto desnecessário, frequentemente na forma de muitas ferramentas disponíveis, faz com que o modelo gere respostas ruins ou chame ferramentas irrelevantes. Modelos menores são especialmente propensos a isso.

**O que fazer:** Implemente **gerenciamento de carregamento de ferramentas** usando técnicas RAG. Armazene descrições de ferramentas em um banco de dados vetorial e selecione _apenas_ as ferramentas mais relevantes para cada tarefa específica. Pesquisas mostram limitar seleções a menos de 30 ferramentas.

**Exemplo de Reserva de Viagem:** Seu agente tem acesso a dezenas de ferramentas: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, etc. Você pergunta: **"Qual é a melhor maneira de se locomover em Paris?"** Devido ao grande número de ferramentas, o agente fica confuso e tenta chamar `book_flight` _dentro_ de Paris, ou `rent_car` mesmo você preferindo transporte público, porque as descrições das ferramentas podem se sobrepor ou ele simplesmente não consegue discernir a melhor.

**Solução:** Use **RAG sobre descrições de ferramentas**. Quando você pergunta sobre locomoção em Paris, o sistema recupera dinamicamente _apenas_ as ferramentas mais relevantes, como `rent_car` ou `public_transport_info`, baseando-se na sua consulta, apresentando uma "seleção" focada de ferramentas ao LLM.

### Conflito de Contexto

**O que é:** Quando informações conflitantes existem dentro do contexto, levando a raciocínios inconsistentes ou respostas finais ruins. Isso geralmente acontece quando a informação chega em etapas, e suposições iniciais incorretas permanecem no contexto.

**O que fazer:** Use **poda de contexto** e **descarregamento**. Poda significa remover informação desatualizada ou conflitante à medida que novos detalhes chegam. Descarregamento dá ao modelo um espaço separado de "bloco de notas" para processar informações sem sobrecarregar o contexto principal.


**Exemplo de Reserva de Viagem:** Você inicialmente diz ao seu agente, **"Quero voar na classe econômica."** Mais tarde na conversa, você muda de ideia e diz, **"Na verdade, para esta viagem, vamos de classe executiva."** Se ambas as instruções permanecerem no contexto, o agente pode receber resultados de busca conflitantes ou se confundir sobre qual preferência priorizar.

**Solução:** Implemente **poda de contexto**. Quando uma instrução nova contradiz uma antiga, a instrução mais antiga é removida ou explicitamente substituída no contexto. Alternativamente, o agente pode usar um **rascunho** para reconciliar preferências conflitantes antes de decidir, garantindo que somente a instrução final e consistente guie suas ações.

## Tem Mais Perguntas Sobre Engenharia de Contexto?

Participe do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.
## Aula Anterior

[Protocolos Agentes](../11-agentic-protocols/README.md)

## Próxima Aula

[Memória para Agentes de IA](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->