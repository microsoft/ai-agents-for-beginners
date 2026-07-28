[![Multi-Agent Design](../../../translated_images/pt-PT/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrões de desenho multi-agente

Assim que começar a trabalhar num projeto que envolve múltiplos agentes, terá de considerar o padrão de desenho multi-agente. No entanto, pode não ser imediatamente claro quando passar para multi-agentes e quais as vantagens.

## Introdução

Nesta lição, procuramos responder às seguintes perguntas:

- Quais são os cenários onde os multi-agentes são aplicáveis?
- Quais são as vantagens de usar multi-agentes em vez de apenas um agente singular a realizar múltiplas tarefas?
- Quais são os blocos de construção para implementar o padrão de desenho multi-agente?
- Como podemos ter visibilidade de como os múltiplos agentes estão a interagir entre si?

## Objetivos de Aprendizagem

Após esta lição, deverá ser capaz de:

- Identificar cenários onde os multi-agentes são aplicáveis
- Reconhecer as vantagens de usar multi-agentes em vez de um agente singular.
- Compreender os blocos de construção para implementar o padrão de desenho multi-agente.

Qual é a visão geral?

*Os multi-agentes são um padrão de desenho que permite que múltiplos agentes trabalhem juntos para alcançar um objetivo comum*.

Este padrão é amplamente utilizado em vários campos, incluindo robótica, sistemas autónomos e computação distribuída.

## Cenários Onde os Multi-Agentes São Aplicáveis

Então, quais cenários são um bom caso de uso para usar multi-agentes? A resposta é que há muitos cenários onde empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes cargas de trabalho**: Grandes cargas de trabalho podem ser divididas em tarefas menores e atribuídas a diferentes agentes, permitindo processamento paralelo e conclusão mais rápida. Um exemplo disto é no caso de uma grande tarefa de processamento de dados.
- **Tarefas complexas**: Tarefas complexas, assim como grandes cargas de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado num aspeto específico da tarefa. Um bom exemplo disto é o caso de veículos autónomos, onde diferentes agentes gerem a navegação, deteção de obstáculos e comunicação com outros veículos.
- **Diversidade de especialização**: Diferentes agentes podem ter especializações diversas, permitindo-lhes lidar melhor com diferentes aspetos de uma tarefa do que um agente único. Para este caso, um bom exemplo é na área da saúde, onde agentes podem gerir diagnósticos, planos de tratamento e monitorização de pacientes.

## Vantagens de Usar Multi-Agentes em Vez de um Agente Singular

Um sistema de agente único pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode proporcionar várias vantagens:

- **Especialização**: Cada agente pode ser especializado numa tarefa específica. A falta de especialização num agente único significa que tem um agente que pode fazer tudo mas pode ficar confuso sobre o que fazer quando confrontado com uma tarefa complexa. Poderá, por exemplo, acabar por fazer uma tarefa para a qual não está melhor preparado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes do que sobrecarregando um único agente.
- **Tolerância a falhas**: Se um agente falhar, outros podem continuar a funcionar, garantindo a fiabilidade do sistema.

Vamos pegar num exemplo, vamos reservar uma viagem para um utilizador. Um sistema de agente único teria de lidar com todos os aspetos do processo de reserva da viagem, desde encontrar voos até reservar hotéis e carros de aluguer. Para conseguir isto com um único agente, o agente teria de ter ferramentas para lidar com todas estas tarefas. Isto poderia levar a um sistema complexo e monolítico que é difícil de manter e escalar. Um sistema multi-agente, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros de aluguer. Isto tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isto com uma agência de viagens gerida como uma loja familiar versus uma agência de viagens gerida como uma franquia. A loja familiar teria um único agente a tratar de todos os aspetos do processo de reserva da viagem, enquanto a franquia teria diferentes agentes a tratar de diferentes aspetos do processo de reserva.

## Blocos de Construção para Implementar o Padrão de Desenho Multi-Agente

Antes de poder implementar o padrão de desenho multi-agente, precisa de compreender os blocos de construção que compõem o padrão.

Vamos tornar isto mais concreto, novamente olhando para o exemplo de reservar uma viagem para um utilizador. Neste caso, os blocos de construção incluiriam:

- **Comunicação entre Agentes**: Agentes para encontrar voos, reservar hotéis e carros de aluguer precisam de comunicar e partilhar informações sobre as preferências e restrições do utilizador. Tem de decidir sobre os protocolos e métodos para esta comunicação. O que isto significa concretamente é que o agente para encontrar voos precisa de comunicar com o agente para reservar hotéis para assegurar que o hotel é reservado para as mesmas datas do voo. Isso significa que os agentes precisam de partilhar informações sobre as datas de viagem do utilizador, o que implica que tem de decidir *quais agentes estão a partilhar informações e como o estão a fazer*.
- **Mecanismos de Coordenação**: Os agentes precisam de coordenar as suas ações para garantir que as preferências e restrições do utilizador são cumpridas. Uma preferência do utilizador pode ser querer um hotel perto do aeroporto, enquanto uma restrição pode ser que carros de aluguer só estão disponíveis no aeroporto. Isto significa que o agente para reservar hotéis precisa de coordenar com o agente para reservar carros de aluguer para assegurar que as preferências e restrições do utilizador são cumpridas. Isto significa que precisa de decidir *como os agentes estão a coordenar as suas ações*.
- **Arquitetura do Agente**: Os agentes precisam de ter a estrutura interna para tomar decisões e aprender com as suas interações com o utilizador. Isto significa que o agente para encontrar voos precisa de ter a estrutura interna para tomar decisões sobre quais voos recomendar ao utilizador. Isto significa que precisa de decidir *como os agentes estão a tomar decisões e a aprender com as suas interações com o utilizador*. Exemplos de como um agente aprende e melhora poderiam ser que o agente para encontrar voos poderia usar um modelo de aprendizagem automática para recomendar voos ao utilizador com base nas suas preferências passadas.
- **Visibilidade nas Interações Multi-Agente**: Precisa de ter visibilidade de como os múltiplos agentes estão a interagir entre si. Isto significa que precisa de ter ferramentas e técnicas para rastrear atividades e interações dos agentes. Isto pode ser na forma de ferramentas de logging e monitorização, ferramentas de visualização e métricas de desempenho.
- **Padrões Multi-Agente**: Existem diferentes padrões para implementar sistemas multi-agente, como arquiteturas centralizadas, descentralizadas e híbridas. Precisa de decidir qual o padrão que melhor se adequa ao seu caso de uso.
- **Humano no ciclo**: Na maioria dos casos, terá um humano no ciclo e precisa de instruir os agentes quando devem pedir intervenção humana. Isto pode ser sob a forma de um utilizador a pedir um hotel específico ou voo que os agentes não recomendaram ou a pedir confirmação antes de reservar um voo ou hotel.

## Visibilidade nas Interações Multi-Agente

É importante que tenha visibilidade de como os múltiplos agentes estão a interagir entre si. Esta visibilidade é essencial para depurar, otimizar e garantir a eficácia geral do sistema. Para conseguir isto, precisa de ter ferramentas e técnicas para rastrear atividades e interações dos agentes. Isto pode ser na forma de ferramentas de logging e monitorização, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um utilizador, poderia ter um painel de controlo que mostra o estado de cada agente, as preferências e restrições do utilizador e as interações entre os agentes. Este painel poderia mostrar as datas de viagem do utilizador, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis e os carros de aluguer recomendados pelo agente de aluguer de carros. Isto dar-lhe-ia uma visão clara de como os agentes estão a interagir entre si e se as preferências e restrições do utilizador estão a ser cumpridas.

Vamos olhar a cada um destes aspetos com mais detalhe.

- **Ferramentas de Logging e Monitorização**: Deseja ter logging feito para cada ação tomada por um agente. Uma entrada de log poderia armazenar informação sobre o agente que tomou a ação, a ação tomada, o tempo em que a ação foi tomada e o resultado da ação. Esta informação pode então ser usada para depurar, otimizar e mais.

- **Ferramentas de Visualização**: As ferramentas de visualização podem ajudá-lo a ver as interações entre agentes de uma forma mais intuitiva. Por exemplo, poderia ter um gráfico que mostra o fluxo de informação entre agentes. Isto pode ajudá-lo a identificar pontos de congestionamento, ineficiências e outros problemas no sistema.

- **Métricas de Desempenho**: As métricas de desempenho podem ajudá-lo a rastrear a eficácia do sistema multi-agente. Por exemplo, poderia rastrear o tempo para completar uma tarefa, o número de tarefas completadas por unidade de tempo e a precisão das recomendações feitas pelos agentes. Esta informação pode ajudá-lo a identificar áreas de melhoria e otimizar o sistema.

## Padrões Multi-Agente

Vamos aprofundar alguns padrões concretos que podemos usar para criar aplicações multi-agente. Aqui estão alguns padrões interessantes que vale a pena considerar:

### Chat de grupo

Este padrão é útil quando quer criar uma aplicação de chat em grupo onde múltiplos agentes podem comunicar entre si. Casos de uso típicos para este padrão incluem colaboração de equipas, suporte ao cliente e redes sociais.

Neste padrão, cada agente representa um utilizador no chat de grupo, e mensagens são trocadas entre agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para o chat de grupo, receber mensagens do chat de grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada onde todas as mensagens são encaminhadas através de um servidor central, ou uma arquitetura descentralizada onde as mensagens são trocadas diretamente.

![Group chat](../../../translated_images/pt-PT/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferência de tarefas

Este padrão é útil quando quer criar uma aplicação onde múltiplos agentes podem passar tarefas uns aos outros.

Casos de uso típicos para este padrão incluem suporte ao cliente, gestão de tarefas e automação de fluxo de trabalho.

Neste padrão, cada agente representa uma tarefa ou um passo num fluxo de trabalho, e os agentes podem passar tarefas para outros agentes com base em regras predefinidas.

![Hand off](../../../translated_images/pt-PT/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtragem colaborativa

Este padrão é útil quando quer criar uma aplicação onde múltiplos agentes podem colaborar para fazer recomendações aos utilizadores.

Porque quer múltiplos agentes a colaborar? Porque cada agente pode ter diferentes especializações e pode contribuir para o processo de recomendação de diferentes maneiras.

Vamos pegar num exemplo onde um utilizador quer uma recomendação sobre a melhor ação para comprar no mercado de ações.

- **Especialista da indústria**: Um agente poderia ser especialista numa indústria específica.
- **Análise técnica**: Outro agente poderia ser especialista em análise técnica.
- **Análise fundamentalista**: e outro agente poderia ser especialista em análise fundamental. Colaborando, estes agentes podem fornecer uma recomendação mais abrangente ao utilizador.

![Recommendation](../../../translated_images/pt-PT/multi-agent-filtering.d959cb129dc9f608.webp)

## Cenário: Processo de reembolso

Considere um cenário onde um cliente está a tentar obter um reembolso por um produto, pode haver vários agentes envolvidos neste processo, mas vamos dividir entre agentes específicos para este processo e agentes gerais que podem ser usados noutros processos.

**Agentes específicos para o processo de reembolso**:

Seguem-se alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente do cliente**: Este agente representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente do vendedor**: Este agente representa o vendedor e é responsável por processar o reembolso.
- **Agente de pagamento**: Este agente representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente de resolução**: Este agente representa o processo de resolução e é responsável por resolver qualquer problema que surja durante o processo de reembolso.
- **Agente de conformidade**: Este agente representa o processo de conformidade e é responsável por garantir que o processo de reembolso está em conformidade com os regulamentos e políticas.

**Agentes gerais**:

Estes agentes podem ser usados em outras partes do seu negócio.

- **Agente de expedição**: Este agente representa o processo de expedição e é responsável por enviar o produto de volta ao vendedor. Este agente pode ser usado tanto no processo de reembolso como no envio geral de um produto através de uma compra, por exemplo.
- **Agente de feedback**: Este agente representa o processo de recolha de feedback e é responsável por recolher feedback do cliente. O feedback pode ser recolhido a qualquer momento e não apenas durante o processo de reembolso.
- **Agente de escalonamento**: Este agente representa o processo de escalonamento e é responsável por escalar problemas para um nível superior de suporte. Pode usar este tipo de agente para qualquer processo onde precise de escalar um problema.
- **Agente de notificações**: Este agente representa o processo de notificações e é responsável por enviar notificações ao cliente em várias fases do processo de reembolso.
- **Agente de análises**: Este agente representa o processo de análises e é responsável por analisar dados relacionados com o processo de reembolso.
- **Agente de auditoria**: Este agente representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que está a ser realizado corretamente.
- **Agente de relatórios**: Este agente representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de conhecimento**: Este agente representa o processo de conhecimento e é responsável por manter uma base de conhecimento de informações relacionadas com o processo de reembolso. Este agente poderia ter conhecimento tanto sobre reembolsos como sobre outras partes do seu negócio.
- **Agente de segurança**: Este agente representa o processo de segurança e é responsável por garantir a segurança do processo de reembolso.
- **Agente de qualidade**: Este agente representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há bastantes agentes listados anteriormente, tanto para o processo específico de reembolso como para os agentes gerais que podem ser usados noutras partes do seu negócio. Esperamos que isto lhe dê uma ideia sobre como pode decidir quais agentes usar no seu sistema multi-agente.

## Exercício

Desenhe um sistema multi-agente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, os seus papéis e responsabilidades, e como interagem entre si. Considere tanto agentes específicos para o processo de suporte ao cliente como agentes gerais que podem ser usados noutras partes do seu negócio.


> Pense um pouco antes de ler a solução seguinte, pode precisar de mais agentes do que pensa.

> DICA: Pense nas diferentes fases do processo de suporte ao cliente e considere também os agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificações de conhecimento

### Pergunta 1

Qual cenário é o que melhor se adequa a um sistema multi-agente?

- [ ] A1: Um bot de apoio responde a perguntas comuns usando uma base de conhecimento e um pequeno conjunto de ferramentas.
- [ ] A2: Um fluxo de trabalho de reembolso necessita de funções separadas de fraude, pagamento e conformidade, cada uma com as suas próprias ferramentas, e os seus resultados devem ser coordenados.
- [ ] A3: O mesmo pedido simples de classificação chega milhares de vezes por hora.

### Pergunta 2

Quando é que normalmente um agente único é a melhor escolha?

- [ ] A1: A tarefa pode ser executada com um conjunto único de instruções e ferramentas, sem transferências para especialistas.
- [ ] A2: O agente tem acesso a mais do que uma ferramenta.
- [ ] A3: O fluxo de trabalho requer funções separadas com permissões diferentes e auditorias independentes.

[Solução do questionário](./solution/solution-quiz.md)

## Resumo

Nesta lição, analisámos o padrão de design multi-agente, incluindo os cenários em que os multi-agentes são aplicáveis, as vantagens de usar multi-agentes em vez de um agente singular, os blocos de construção para implementar o padrão de design multi-agente e como ter visibilidade sobre como os múltiplos agentes estão a interagir entre si.

### Tem mais perguntas sobre o padrão de design Multi-Agente?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos adicionais

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentação do Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Padrões de design agentic</a>


## Lição anterior

[Planeamento de design](../07-planning-design/README.md)

## Próxima lição

[Metacognição em Agentes de IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->