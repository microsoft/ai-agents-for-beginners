[![Design Multiagente](../../../translated_images/pt-PT/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrões de design multi-agente

Assim que começar a trabalhar num projeto que envolve múltiplos agentes, terá de considerar o padrão de design multi-agente. No entanto, pode não ser imediatamente óbvio quando mudar para múltiplos agentes e quais as vantagens.

## Introdução

Nesta lição, procuramos responder às seguintes questões:

- Quais são os cenários em que os multi-agentes são aplicáveis?
- Quais são as vantagens de usar multi-agentes em vez de um único agente a executar múltiplas tarefas?
- Quais são os blocos de construção para implementar o padrão de design multi-agente?
- Como temos visibilidade de como os múltiplos agentes estão a interagir entre si?

## Objetivos de aprendizagem

Após esta lição, deverá ser capaz de:

- Identificar cenários onde os multi-agentes são aplicáveis
- Reconhecer as vantagens de usar multi-agentes em vez de um agente singular.
- Compreender os blocos de construção para implementar o padrão de design multi-agente.

Qual é o panorama geral?

*Os multi-agentes são um padrão de design que permite a vários agentes trabalhar em conjunto para atingir um objetivo comum*.

Este padrão é amplamente utilizado em vários campos, incluindo robótica, sistemas autónomos e computação distribuída.

## Cenários onde os multi-agentes são aplicáveis

Então, que cenários são um bom caso de uso para usar multi-agentes? A resposta é que existem muitos cenários em que empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes cargas de trabalho**: Grandes cargas de trabalho podem ser divididas em tarefas menores e atribuídas a diferentes agentes, permitindo processamento em paralelo e conclusão mais rápida. Um exemplo disto é no caso de uma grande tarefa de processamento de dados.
- **Tarefas complexas**: Tarefas complexas, tal como grandes cargas de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado num aspeto específico da tarefa. Um bom exemplo disto é no caso de veículos autónomos onde diferentes agentes gerem a navegação, deteção de obstáculos e comunicação com outros veículos.
- **Diversidade de competências**: Diferentes agentes podem ter competências diversas, permitindo-lhes tratar diferentes aspetos de uma tarefa de forma mais eficaz do que um único agente. Para este caso, um bom exemplo é na área da saúde, onde agentes podem gerir diagnósticos, planos de tratamento e monitorização de pacientes.

## Vantagens de usar multi-agentes em vez de um agente singular

Um sistema com um único agente pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode oferecer várias vantagens:

- **Especialização**: Cada agente pode ser especializado numa tarefa específica. A falta de especialização num agente único significa que tem um agente que pode fazer tudo, mas que pode ficar confuso sobre o que fazer quando confrontado com uma tarefa complexa. Por exemplo, pode acabar por executar uma tarefa para a qual não é o mais indicado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes do que sobrecarregando um único agente.
- **Tolerância a falhas**: Se um agente falhar, outros podem continuar a funcionar, assegurando a fiabilidade do sistema.

Vamos tomar um exemplo: vamos reservar uma viagem para um utilizador. Um sistema com um único agente teria de tratar todos os aspetos do processo de reserva da viagem, desde encontrar voos até reservar hotéis e carros de aluguer. Para conseguir isto com um único agente, o agente teria de dispor de ferramentas para tratar todas estas tarefas. Isto poderia conduzir a um sistema complexo e monolítico que é difícil de manter e escalar. Um sistema multi-agente, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros de aluguer. Isto tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isto com uma agência de viagens gerida por uma pequena empresa familiar versus uma agência de viagens operada como uma franquia. A pequena agência teria um único agente a tratar todos os aspetos do processo de reserva da viagem, enquanto a franquia teria diferentes agentes a tratar de diferentes aspetos do processo de reserva da viagem.

## Blocos de construção para implementar o padrão de design multi-agente

Antes de poder implementar o padrão de design multi-agente, precisa de entender os blocos de construção que compõem o padrão.

Vamos tornar isto mais concreto voltando a olhar para o exemplo de reservar uma viagem para um utilizador. Neste caso, os blocos de construção incluiriam:

- **Comunicação entre agentes**: Agentes para encontrar voos, reservar hotéis e carros de aluguer precisam de comunicar e partilhar informação sobre as preferências e constrangimentos do utilizador. Precisa de decidir os protocolos e métodos para esta comunicação. O que isto significa concretamente é que o agente que encontra voos precisa de comunicar com o agente que reserva hotéis para assegurar que o hotel é reservado para as mesmas datas do voo. Isso significa que os agentes precisam de partilhar informação sobre as datas da viagem do utilizador, o que implica que precisa de decidir *quais os agentes que estão a partilhar informações e como estão a partilhá-las*.
- **Mecanismos de coordenação**: Os agentes precisam de coordenar as suas ações para garantir que as preferências e os constrangimentos do utilizador são respeitados. Uma preferência do utilizador poderia ser ficar num hotel perto do aeroporto, enquanto um constrangimento poderia ser que os carros de aluguer só estão disponíveis no aeroporto. Isto significa que o agente que reserva hotéis precisa de coordenar com o agente que reserva carros de aluguer para garantir que as preferências e os constrangimentos do utilizador são cumpridos. Isto significa que precisa de decidir *como os agentes estão a coordenar as suas ações*.
- **Arquitetura dos agentes**: Os agentes precisam de ter a estrutura interna para tomar decisões e aprender com as suas interações com o utilizador. Isto significa que o agente que encontra voos precisa de ter a estrutura interna para decidir que voos recomendar ao utilizador. Isto significa que precisa de decidir *como os agentes estão a tomar decisões e a aprender com as suas interações com o utilizador*. Exemplos de como um agente aprende e melhora poderiam ser que o agente que encontra voos poderia usar um modelo de machine learning para recomendar voos ao utilizador com base nas suas preferências anteriores.
- **Visibilidade nas interações multi-agente**: Precisa de ter visibilidade de como os múltiplos agentes estão a interagir entre si. Isto significa que precisa de ter ferramentas e técnicas para rastrear atividades e interações dos agentes. Isto poderia ser na forma de ferramentas de registo e monitorização, ferramentas de visualização e métricas de desempenho.
- **Padrões multi-agente**: Existem diferentes padrões para implementar sistemas multi-agente, tais como arquiteturas centralizadas, descentralizadas e híbridas. Precisa de decidir o padrão que melhor se adapta ao seu caso de uso.
- **Humano no processo**: Na maioria dos casos, terá um humano envolvido e precisa de instruir os agentes quando pedir intervenção humana. Isto poderia ser na forma de um utilizador a pedir um hotel ou voo específico que os agentes não recomendaram ou a pedir confirmação antes de reservar um voo ou hotel.

## Visibilidade nas interações multi-agente

É importante que tenha visibilidade de como os múltiplos agentes estão a interagir entre si. Esta visibilidade é essencial para depuração, otimização e garantia da eficácia global do sistema. Para alcançar isto, precisa de ferramentas e técnicas para rastrear atividades e interações dos agentes. Isto poderia ser na forma de ferramentas de registo e monitorização, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um utilizador, poderia ter um painel que mostre o estado de cada agente, as preferências e os constrangimentos do utilizador, e as interações entre agentes. Este painel poderia mostrar as datas da viagem do utilizador, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis e os carros de aluguer recomendados pelo agente de carros de aluguer. Isto daria uma visão clara de como os agentes estão a interagir entre si e se as preferências e os constrangimentos do utilizador estão a ser cumpridos.

Vamos analisar cada um destes aspetos com mais detalhe.

- **Ferramentas de registo e monitorização**: Quer que exista um registo para cada ação tomada por um agente. Uma entrada de registo poderia armazenar informação sobre o agente que efetuou a ação, a ação efetuada, o tempo em que a ação foi efetuada e o resultado da ação. Esta informação pode então ser usada para depuração, otimização e mais.
- **Ferramentas de visualização**: Ferramentas de visualização podem ajudar a ver as interações entre agentes de uma forma mais intuitiva. Por exemplo, poderia ter um grafo que mostre o fluxo de informação entre agentes. Isto poderia ajudar a identificar gargalos, ineficiências e outros problemas no sistema.
- **Métricas de desempenho**: As métricas de desempenho podem ajudar a acompanhar a eficácia do sistema multi-agente. Por exemplo, poderia acompanhar o tempo necessário para completar uma tarefa, o número de tarefas concluídas por unidade de tempo e a precisão das recomendações feitas pelos agentes. Esta informação pode ajudar a identificar áreas de melhoria e otimizar o sistema.

## Padrões multi-agente

Vamos aprofundar alguns padrões concretos que podemos usar para criar aplicações multi-agente. Aqui estão alguns padrões interessantes a considerar:

### Conversa de grupo

Este padrão é útil quando quer criar uma aplicação de conversa de grupo onde vários agentes podem comunicar entre si. Casos de uso típicos para este padrão incluem colaboração em equipa, suporte ao cliente e redes sociais.

Neste padrão, cada agente representa um utilizador na conversa de grupo, e as mensagens são trocadas entre agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para a conversa de grupo, receber mensagens da conversa de grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada onde todas as mensagens são encaminhadas através de um servidor central, ou uma arquitetura descentralizada onde as mensagens são trocadas diretamente.

![Conversa de grupo](../../../translated_images/pt-PT/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferência de tarefas

Este padrão é útil quando quer criar uma aplicação onde múltiplos agentes podem transferir tarefas entre si.

Casos de uso típicos para este padrão incluem suporte ao cliente, gestão de tarefas e automação de fluxos de trabalho.

Neste padrão, cada agente representa uma tarefa ou um passo num fluxo de trabalho, e os agentes podem transferir tarefas para outros agentes com base em regras predefinidas.

![Hand off](../../../translated_images/pt-PT/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtragem colaborativa

Este padrão é útil quando quer criar uma aplicação onde múltiplos agentes podem colaborar para fazer recomendações aos utilizadores.

Porque quererá múltiplos agentes a colaborar é porque cada agente pode ter diferentes áreas de especialização e pode contribuir para o processo de recomendação de formas distintas.

Vamos tomar um exemplo em que um utilizador quer uma recomendação sobre a melhor ação para comprar na bolsa.

- **Especialista da indústria**:. Um agente poderia ser um perito numa indústria específica.
- **Análise técnica**: Outro agente poderia ser um perito em análise técnica.
- **Análise fundamental**: e outro agente poderia ser um perito em análise fundamental. Ao colaborar, estes agentes podem fornecer uma recomendação mais abrangente ao utilizador.

![Recomendação](../../../translated_images/pt-PT/multi-agent-filtering.d959cb129dc9f608.webp)

## Cenário: processo de reembolso

Considere um cenário em que um cliente está a tentar obter um reembolso por um produto; podem estar envolvidos bastantes agentes neste processo, mas vamos dividi-los entre agentes específicos para este processo e agentes gerais que podem ser usados noutros processos.

**Agentes específicos para o processo de reembolso**:

Seguem-se alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente do cliente**: Este agente representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente do vendedor**: Este agente representa o vendedor e é responsável por processar o reembolso.
- **Agente de pagamento**: Este agente representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente de resolução**: Este agente representa o processo de resolução e é responsável por resolver quaisquer problemas que surjam durante o processo de reembolso.
- **Agente de conformidade**: Este agente representa o processo de conformidade e é responsável por garantir que o processo de reembolso cumpre regulamentos e políticas.

**Agentes gerais**:

Estes agentes podem ser usados por outras partes do seu negócio.

- **Agente de expedição**: Este agente representa o processo de expedição e é responsável por enviar o produto de volta ao vendedor. Este agente pode ser usado tanto para o processo de reembolso como para a expedição geral de um produto numa compra, por exemplo.
- **Agente de feedback**: Este agente representa o processo de recolha de feedback e é responsável por coletar feedback do cliente. O feedback pode ser recolhido a qualquer momento e não apenas durante o processo de reembolso.
- **Agente de escalonamento**: Este agente representa o processo de escalonamento e é responsável por escalar problemas para um nível superior de suporte. Pode usar este tipo de agente para qualquer processo onde seja necessário escalar um problema.
- **Agente de notificações**: Este agente representa o processo de notificações e é responsável por enviar notificações ao cliente em várias fases do processo de reembolso.
- **Agente de análise**: Este agente representa o processo de análise e é responsável por analisar dados relacionados com o processo de reembolso.
- **Agente de auditoria**: Este agente representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que está a ser executado corretamente.
- **Agente de relatórios**: Este agente representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de conhecimento**: Este agente representa o processo de conhecimento e é responsável por manter uma base de conhecimento de informações relacionadas com o processo de reembolso. Este agente poderia ter conhecimento tanto sobre reembolsos como sobre outras partes do seu negócio.
- **Agente de segurança**: Este agente representa o processo de segurança e é responsável por assegurar a segurança do processo de reembolso.
- **Agente de qualidade**: Este agente representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há bastantes agentes listados anteriormente, tanto para o processo específico de reembolso como para os agentes gerais que podem ser usados noutras partes do seu negócio. Espera-se que isto lhe dê uma ideia de como pode decidir quais os agentes a utilizar no seu sistema multi-agente.

## Tarefa

Desenhe um sistema multi-agente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, os seus papéis e responsabilidades, e como interagem entre si. Considere tanto agentes específicos do processo de suporte ao cliente como agentes gerais que podem ser usados noutras partes do seu negócio.
> Reflita antes de ler a solução seguinte, poderá precisar de mais agentes do que pensa.
>
> DICA: Pense nas diferentes etapas do processo de apoio ao cliente e considere também os agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificações de conhecimento

Pergunta: Quando deve considerar utilizar multi-agentes?

- [ ] A1: Quando tem uma carga de trabalho pequena e uma tarefa simples.
- [ ] A2: Quando tem uma carga de trabalho grande
- [ ] A3: Quando tem uma tarefa simples.

[Questionário da solução](./solution/solution-quiz.md)

## Resumo

Nesta lição, analisámos o padrão de design multi-agente, incluindo os cenários em que os multi-agentes são aplicáveis, as vantagens de utilizar múltiplos agentes em vez de um agente singular, os blocos construtivos para implementar o padrão de design multi-agente, e como obter visibilidade sobre a forma como os múltiplos agentes interagem entre si.

### Tem mais perguntas sobre o Padrão de Design Multi-Agente?

Junte-se ao [Discord do Microsoft Foundry](https://aka.ms/ai-agents/discord) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos adicionais

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentação do Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Padrões de design agentic</a>


## Lição anterior

[Planeamento do Design](../07-planning-design/README.md)

## Próxima lição

[Metacognição em Agentes de IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento foi traduzido com recurso ao serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela exatidão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deverá ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->