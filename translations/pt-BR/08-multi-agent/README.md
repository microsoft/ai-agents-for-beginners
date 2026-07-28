[![Multi-Agent Design](../../../translated_images/pt-BR/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrões de design multiagente

Assim que você começar a trabalhar em um projeto que envolve múltiplos agentes, será necessário considerar o padrão de design multiagente. No entanto, pode não ficar imediatamente claro quando trocar para multiagentes e quais são as vantagens.

## Introdução

Nesta lição, buscamos responder às seguintes perguntas:

- Quais são os cenários em que multiagentes são aplicáveis?
- Quais são as vantagens de usar multiagentes em vez de apenas um agente único fazendo múltiplas tarefas?
- Quais são os blocos de construção para implementar o padrão de design multiagente?
- Como temos visibilidade de como os múltiplos agentes estão interagindo entre si?

## Objetivos de aprendizado

Após esta lição, você deverá ser capaz de:

- Identificar cenários onde multiagentes são aplicáveis
- Reconhecer as vantagens de usar multiagentes sobre um agente singular.
- Compreender os blocos de construção para implementar o padrão de design multiagente.

Qual é o panorama geral?

*Multiagentes são um padrão de design que permite que múltiplos agentes trabalhem juntos para alcançar um objetivo comum*.

Este padrão é amplamente utilizado em vários campos, incluindo robótica, sistemas autônomos e computação distribuída.

## Cenários onde multiagentes são aplicáveis

Então, quais cenários são um bom caso de uso para usar multiagentes? A resposta é que há muitos cenários onde empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes cargas de trabalho**: Grandes cargas de trabalho podem ser divididas em tarefas menores e atribuídas a diferentes agentes, permitindo processamento paralelo e conclusão mais rápida. Um exemplo disso é no caso de uma grande tarefa de processamento de dados.
- **Tarefas complexas**: Tarefas complexas, assim como grandes cargas de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado em um aspecto específico da tarefa. Um bom exemplo disso é no caso de veículos autônomos, onde diferentes agentes gerenciam navegação, detecção de obstáculos e comunicação com outros veículos.
- **Expertise diversa**: Diferentes agentes podem ter expertise diversa, permitindo que lidem com diferentes aspectos de uma tarefa de forma mais eficaz do que um único agente. Nesse caso, um bom exemplo é na área de saúde, onde agentes podem gerenciar diagnósticos, planos de tratamento e monitoramento de pacientes.

## Vantagens de usar multiagentes em vez de um agente singular

Um sistema com um único agente pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode oferecer várias vantagens:

- **Especialização**: Cada agente pode ser especializado para uma tarefa específica. A falta de especialização em um agente único significa que você tem um agente que pode fazer de tudo, mas pode ficar confuso sobre o que fazer quando enfrenta uma tarefa complexa. Ele pode, por exemplo, acabar fazendo uma tarefa para a qual não é o mais adequado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes do que sobrecarregar um único agente.
- **Tolerância a falhas**: Se um agente falhar, outros podem continuar funcionando, garantindo a confiabilidade do sistema.

Vamos tomar um exemplo, vamos reservar uma viagem para um usuário. Um sistema com um único agente teria que lidar com todos os aspectos do processo de reserva da viagem, desde encontrar voos até reservar hotéis e carros de aluguel. Para conseguir isso com um único agente, o agente precisaria ter ferramentas para lidar com todas essas tarefas. Isso poderia levar a um sistema complexo e monolítico, difícil de manter e escalar. Um sistema multiagente, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros de aluguel. Isso tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isso a uma agência de viagens operada como uma loja pequena versus uma agência de viagens operada como uma franquia. A loja pequena teria um agente único lidando com todos os aspectos do processo de reserva da viagem, enquanto a franquia teria diferentes agentes cuidando de diferentes aspectos do processo de reserva da viagem.

## Blocos de construção para implementar o padrão de design multiagente

Antes de você poder implementar o padrão de design multiagente, é necessário entender os blocos de construção que compõem o padrão.

Vamos tornar isso mais concreto novamente olhando para o exemplo de reservar uma viagem para um usuário. Neste caso, os blocos de construção incluiriam:

- **Comunicação entre agentes**: Agentes para encontrar voos, reservar hotéis e carros de aluguel precisam se comunicar e compartilhar informações sobre as preferências e restrições do usuário. Você precisa decidir os protocolos e métodos para essa comunicação. Isso significa concretamente que o agente responsável por encontrar voos precisa se comunicar com o agente de reserva de hotéis para garantir que o hotel seja reservado para as mesmas datas do voo. Isso significa que os agentes precisam compartilhar informações sobre as datas de viagem do usuário, o que implica que você precisa decidir *quais agentes estão compartilhando informações e como estão compartilhando*.
- **Mecanismos de coordenação**: Os agentes precisam coordenar suas ações para garantir que as preferências e restrições do usuário sejam atendidas. Uma preferência do usuário poderia ser que ele queira um hotel próximo ao aeroporto, enquanto uma restrição poderia ser que carros de aluguel só estão disponíveis no aeroporto. Isso significa que o agente responsável pela reserva do hotel precisa coordenar com o agente de reserva de carros para garantir que as preferências e restrições do usuário sejam atendidas. Isso significa que você precisa decidir *como os agentes estão coordenando suas ações*.
- **Arquitetura do agente**: Os agentes precisam ter a estrutura interna para tomar decisões e aprender com suas interações com o usuário. Isso significa que o agente para encontrar voos precisa ter a estrutura interna para tomar decisões sobre quais voos recomendar ao usuário. Isso significa que você precisa decidir *como os agentes estão tomando decisões e aprendendo com suas interações com o usuário*. Exemplos de como um agente aprende e melhora poderiam ser que o agente para encontrar voos poderia usar um modelo de aprendizado de máquina para recomendar voos ao usuário com base em suas preferências passadas.
- **Visibilidade nas interações multiagente**: Você precisa ter visibilidade de como múltiplos agentes estão interagindo entre si. Isso significa que você precisa ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode estar na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.
- **Padrões multiagente**: Existem diferentes padrões para implementar sistemas multiagente, como arquiteturas centralizadas, descentralizadas e híbridas. Você precisa decidir qual padrão se encaixa melhor no seu caso de uso.
- **Humano no loop**: Na maioria dos casos, você terá um humano no loop e precisa instruir os agentes sobre quando pedir intervenção humana. Isso pode ser na forma de um usuário pedindo por um hotel ou voo específico que os agentes não recomendaram ou pedindo confirmação antes de reservar um voo ou hotel.

## Visibilidade nas interações multiagente

É importante que você tenha visibilidade de como múltiplos agentes estão interagindo entre si. Essa visibilidade é essencial para depuração, otimização e garantia da eficácia geral do sistema. Para conseguir isso, você precisa ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode estar na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um usuário, você poderia ter um painel que mostra o status de cada agente, as preferências e restrições do usuário, e as interações entre os agentes. Este painel poderia mostrar as datas de viagem do usuário, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis, e os carros de aluguel recomendados pelo agente de carros. Isso lhe daria uma visão clara de como os agentes estão interagindo uns com os outros e se as preferências e restrições do usuário estão sendo atendidas.

Vamos analisar cada um desses aspectos com mais detalhes.

- **Ferramentas de registro e monitoramento**: Você quer ter registros feitos para cada ação tomada por um agente. Uma entrada de registro poderia armazenar informações sobre o agente que tomou a ação, a ação tomada, o horário em que a ação foi tomada e o resultado da ação. Essas informações podem então ser usadas para depuração, otimização e mais.

- **Ferramentas de visualização**: Ferramentas de visualização podem ajudar você a ver as interações entre agentes de uma forma mais intuitiva. Por exemplo, você poderia ter um gráfico que mostra o fluxo de informações entre os agentes. Isso poderia ajudá-lo a identificar pontos de estrangulamento, ineficiências e outros problemas no sistema.

- **Métricas de desempenho**: Métricas de desempenho podem ajudar você a acompanhar a eficácia do sistema multiagente. Por exemplo, você pode acompanhar o tempo levado para completar uma tarefa, o número de tarefas concluídas por unidade de tempo, e a precisão das recomendações feitas pelos agentes. Essas informações podem ajudar a identificar áreas para melhoria e otimizar o sistema.

## Padrões multiagente

Vamos mergulhar em alguns padrões concretos que podemos usar para criar aplicativos multiagente. Aqui estão alguns padrões interessantes a considerar:

### Bate-papo em grupo

Este padrão é útil quando você quer criar um aplicativo de bate-papo em grupo onde múltiplos agentes podem se comunicar entre si. Casos típicos de uso para este padrão incluem colaboração em equipe, suporte ao cliente e redes sociais.

Nesse padrão, cada agente representa um usuário no bate-papo em grupo, e as mensagens são trocadas entre agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para o grupo, receber mensagens do grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada, onde todas as mensagens são roteadas através de um servidor central, ou uma arquitetura descentralizada, onde as mensagens são trocadas diretamente.

![Group chat](../../../translated_images/pt-BR/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferência de tarefas

Este padrão é útil quando você quer criar um aplicativo onde múltiplos agentes podem transferir tarefas entre si.

Casos típicos de uso para este padrão incluem suporte ao cliente, gestão de tarefas e automação de fluxos de trabalho.

Nesse padrão, cada agente representa uma tarefa ou um passo em um fluxo de trabalho, e agentes podem transferir tarefas para outros agentes com base em regras predefinidas.

![Hand off](../../../translated_images/pt-BR/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtragem colaborativa

Este padrão é útil quando você quer criar um aplicativo onde múltiplos agentes podem colaborar para fazer recomendações aos usuários.

Por que você gostaria que múltiplos agentes colaborassem? Porque cada agente pode ter expertise diferente e pode contribuir para o processo de recomendação de formas diversas.

Vamos tomar um exemplo onde um usuário quer uma recomendação sobre a melhor ação para comprar no mercado de ações.

- **Especialista da indústria**: Um agente pode ser especialista em um setor específico.
- **Análise técnica**: Outro agente pode ser especialista em análise técnica.
- **Análise fundamentalista**: e outro agente pode ser especialista em análise fundamentalista. Ao colaborar, esses agentes podem fornecer uma recomendação mais abrangente para o usuário.

![Recommendation](../../../translated_images/pt-BR/multi-agent-filtering.d959cb129dc9f608.webp)

## Cenário: Processo de reembolso

Considere um cenário onde um cliente está tentando obter um reembolso por um produto, pode haver diversos agentes envolvidos nesse processo, mas vamos dividir entre agentes específicos para este processo e agentes gerais que podem ser usados em outros processos.

**Agentes específicos para o processo de reembolso**:

A seguir estão alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente cliente**: Este agente representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente vendedor**: Este agente representa o vendedor e é responsável por processar o reembolso.
- **Agente pagamento**: Este agente representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente resolução**: Este agente representa o processo de resolução e é responsável por resolver quaisquer problemas que surgirem durante o processo de reembolso.
- **Agente conformidade**: Este agente representa o processo de conformidade e é responsável por garantir que o processo de reembolso esteja em conformidade com regulamentações e políticas.

**Agentes gerais**:

Esses agentes podem ser usados por outras partes do seu negócio.

- **Agente de envio**: Este agente representa o processo de envio e é responsável por enviar o produto de volta para o vendedor. Este agente pode ser usado tanto para o processo de reembolso quanto para envio geral de um produto via compra, por exemplo.
- **Agente de feedback**: Este agente representa o processo de feedback e é responsável por coletar feedback do cliente. Feedback pode ser coletado a qualquer momento e não apenas durante o processo de reembolso.
- **Agente de escalonamento**: Este agente representa o processo de escalonamento e é responsável por escalar problemas para um nível superior de suporte. Você pode usar esse tipo de agente para qualquer processo onde precisa escalar um problema.
- **Agente de notificação**: Este agente representa o processo de notificação e é responsável por enviar notificações ao cliente em várias etapas do processo de reembolso.
- **Agente de analytics**: Este agente representa o processo de análise e é responsável por analisar dados relacionados ao processo de reembolso.
- **Agente de auditoria**: Este agente representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que está sendo realizado corretamente.
- **Agente de relatórios**: Este agente representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de conhecimento**: Este agente representa o processo de conhecimento e é responsável por manter uma base de conhecimento de informações relacionadas ao processo de reembolso. Este agente poderia ter conhecimento tanto sobre reembolsos quanto sobre outras partes do seu negócio.
- **Agente de segurança**: Este agente representa o processo de segurança e é responsável por garantir a segurança do processo de reembolso.
- **Agente de qualidade**: Este agente representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há muitos agentes listados anteriormente tanto para o processo específico de reembolso quanto para os agentes gerais que podem ser usados em outras partes do seu negócio. Esperamos que isso lhe dê uma ideia de como decidir quais agentes usar no seu sistema multiagente.

## Exercício

Projete um sistema multiagente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, seus papéis e responsabilidades, e como eles interagem entre si. Considere tanto agentes específicos para o processo de suporte ao cliente quanto agentes gerais que podem ser usados em outras partes do seu negócio.


> Reflita um pouco antes de ler a solução a seguir, você pode precisar de mais agentes do que imagina.

> DICA: Pense nas diferentes etapas do processo de suporte ao cliente e também considere os agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificações de conhecimento

### Pergunta 1

Qual cenário é o mais adequado para um sistema multiagente?

- [ ] A1: Um bot de suporte responde perguntas comuns usando uma base de conhecimento e um pequeno conjunto de ferramentas.
- [ ] A2: Um fluxo de trabalho de reembolso precisa de funções separadas de fraude, pagamento e conformidade, cada uma com suas próprias ferramentas, e seus resultados devem ser coordenados.
- [ ] A3: A mesma solicitação simples de classificação chega milhares de vezes por hora.

### Pergunta 2

Quando um agente único geralmente é a melhor escolha?

- [ ] A1: A tarefa pode ser realizada com um conjunto de instruções e ferramentas, sem transferências para especialistas.
- [ ] A2: O agente tem acesso a mais de uma ferramenta.
- [ ] A3: O fluxo de trabalho exige funções separadas com permissões diferentes e trilhas de auditoria independentes.

[Solução do questionário](./solution/solution-quiz.md)

## Resumo

Nesta lição, examinamos o padrão de design multiagente, incluindo os cenários em que multiagentes são aplicáveis, as vantagens de usar multiagentes em vez de um agente singular, os blocos de construção para implementar o padrão de design multiagente, e como ter visibilidade de como os múltiplos agentes estão interagindo entre si.

### Tem mais perguntas sobre o Padrão de Design Multiagente?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para encontrar outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos adicionais

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentação do Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Padrões de design agentic</a>


## Lição anterior

[Planejamento de Design](../07-planning-design/README.md)

## Próxima lição

[Metacognição em Agentes de IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->