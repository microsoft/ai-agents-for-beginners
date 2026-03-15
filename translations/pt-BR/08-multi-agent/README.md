[![Multi-Design de Agentes](../../../translated_images/pt-BR/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Padrões de design multi-agente

Assim que você começar a trabalhar em um projeto que envolve múltiplos agentes, será necessário considerar o padrão de design multi-agente. No entanto, pode não ser imediatamente claro quando mudar para multi-agentes e quais são as vantagens.

## Introdução

Nesta aula, buscamos responder às seguintes perguntas:

- Quais são os cenários em que múltiplos agentes são aplicáveis?
- Quais são as vantagens de usar múltiplos agentes em vez de apenas um agente singular realizando várias tarefas?
- Quais são os blocos de construção para implementar o padrão de design multi-agente?
- Como temos visibilidade de como os múltiplos agentes estão interagindo entre si?

## Objetivos de Aprendizagem

Após esta aula, você deverá ser capaz de:

- Identificar cenários onde múltiplos agentes são aplicáveis
- Reconhecer as vantagens de usar múltiplos agentes em vez de um agente singular.
- Compreender os blocos de construção para implementar o padrão de design multi-agente.

Qual é a visão geral?

*Multi-agentes são um padrão de design que permite que múltiplos agentes trabalhem juntos para alcançar um objetivo comum*.

Este padrão é amplamente usado em vários campos, incluindo robótica, sistemas autônomos e computação distribuída.

## Cenários Onde Multi-Agentes São Aplicáveis

Então, quais cenários são um bom caso de uso para usar múltiplos agentes? A resposta é que existem muitos cenários onde empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes cargas de trabalho**: Grandes cargas de trabalho podem ser divididas em tarefas menores e atribuídas a diferentes agentes, permitindo processamento paralelo e conclusão mais rápida. Um exemplo disso é no caso de uma grande tarefa de processamento de dados.
- **Tarefas complexas**: Tarefas complexas, assim como grandes cargas de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado em um aspecto específico da tarefa. Um bom exemplo é no caso de veículos autônomos, onde diferentes agentes gerenciam navegação, detecção de obstáculos e comunicação com outros veículos.
- **Expertise diversificada**: Diferentes agentes podem ter expertise diversificada, permitindo-lhes lidar com diferentes aspectos de uma tarefa de forma mais eficaz do que um agente único. Para este caso, um bom exemplo é na área da saúde, onde agentes podem gerenciar diagnósticos, planos de tratamento e monitoramento de pacientes.

## Vantagens de Usar Multi-Agentes em Vez de um Agente Singular

Um sistema com um único agente pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode fornecer diversas vantagens:

- **Especialização**: Cada agente pode ser especializado para uma tarefa específica. A falta de especialização em um agente único significa que você tem um agente que pode fazer tudo, mas que pode ficar confuso sobre o que fazer quando enfrentando uma tarefa complexa. Ele pode, por exemplo, acabar executando uma tarefa para a qual não é o mais adequado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes em vez de sobrecarregar um único agente.
- **Tolerância a Falhas**: Se um agente falhar, outros podem continuar funcionando, garantindo a confiabilidade do sistema.

Vamos a um exemplo, vamos reservar uma viagem para um usuário. Um sistema com agente único teria que lidar com todos os aspectos do processo de reserva de viagem, desde encontrar voos até reservar hotéis e carros alugados. Para conseguir isso com um único agente, ele precisaria ter ferramentas para lidar com todas essas tarefas. Isso poderia levar a um sistema complexo e monolítico, difícil de manter e escalar. Um sistema multi-agente, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros. Isso tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isso a uma agência de viagens administrada como uma loja pequena e familiar versus uma agência de viagens administrada como uma franquia. A loja pequena teria um único agente lidando com todos os aspectos do processo de reserva, enquanto a franquia teria diferentes agentes lidando com diferentes aspectos do processo de reserva.

## Blocos de Construção para Implementar o Padrão de Design Multi-Agente

Antes que você possa implementar o padrão de design multi-agente, você precisa entender os blocos de construção que compõem o padrão.

Vamos tornar isso mais concreto novamente olhando para o exemplo de reservar uma viagem para um usuário. Neste caso, os blocos de construção incluem:

- **Comunicação entre Agentes**: Agentes para encontrar voos, reservar hotéis e carros precisam se comunicar e compartilhar informações sobre as preferências e restrições do usuário. Você precisa decidir os protocolos e métodos para essa comunicação. O que isso significa concretamente é que o agente para encontrar voos precisa se comunicar com o agente para reservar hotéis para garantir que o hotel seja reservado para as mesmas datas do voo. Isso significa que os agentes precisam compartilhar informações sobre as datas da viagem do usuário, o que quer dizer que você precisa decidir *quais agentes estão compartilhando informações e como eles compartilham essas informações*.
- **Mecanismos de Coordenação**: Os agentes precisam coordenar suas ações para garantir que as preferências e restrições do usuário sejam atendidas. Uma preferência do usuário pode ser querer um hotel próximo ao aeroporto, enquanto uma restrição pode ser que carros alugados estejam disponíveis somente no aeroporto. Isso significa que o agente que reserva hotéis precisa se coordenar com o agente que reserva carros para garantir que as preferências e restrições do usuário sejam cumpridas. Isso significa que você precisa decidir *como os agentes estão coordenando suas ações*.
- **Arquitetura do Agente**: Os agentes precisam ter a estrutura interna para tomar decisões e aprender com suas interações com o usuário. Isso significa que o agente para encontrar voos precisa ter a estrutura interna para tomar decisões sobre quais voos recomendar ao usuário. Isso significa que você precisa decidir *como os agentes tomam decisões e aprendem com suas interações com o usuário*. Exemplos de como um agente aprende e melhora poderiam ser o agente para encontrar voos usando um modelo de aprendizado de máquina para recomendar voos ao usuário com base em suas preferências passadas.
- **Visibilidade nas Interações Multi-Agente**: Você precisa ter visibilidade de como os múltiplos agentes estão interagindo entre si. Isso significa que você precisa de ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode ser na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.
- **Padrões Multi-Agentes**: Existem diferentes padrões para implementar sistemas multi-agentes, como arquiteturas centralizadas, descentralizadas e híbridas. Você precisa decidir qual padrão se encaixa melhor no seu caso de uso.
- **Humano no Loop**: Na maioria dos casos, você terá um humano no loop e precisa instruir os agentes sobre quando pedir intervenção humana. Isso pode ser na forma de um usuário pedindo um hotel ou voo específico que os agentes não recomendaram ou pedindo confirmação antes de reservar um voo ou hotel.

## Visibilidade nas Interações Multi-Agente

É importante que você tenha visibilidade de como os múltiplos agentes estão interagindo entre si. Essa visibilidade é essencial para depuração, otimização e garantia da eficácia geral do sistema. Para conseguir isso, você precisa de ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode ser na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um usuário, você poderia ter um painel que mostra o status de cada agente, as preferências e restrições do usuário e as interações entre agentes. Esse painel poderia mostrar as datas da viagem do usuário, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis e os carros recomendados pelo agente de aluguel. Isso lhe daria uma visão clara de como os agentes estão interagindo e se as preferências e restrições do usuário estão sendo atendidas.

Vamos analisar cada um desses aspectos com mais detalhes.

- **Ferramentas de Registro e Monitoramento**: Você vai querer ter o registro feito para cada ação tomada por um agente. Uma entrada de registro pode armazenar informações sobre o agente que realizou a ação, a ação tomada, o momento em que a ação foi tomada e o resultado da ação. Essa informação pode ser usada para depuração, otimização e outras finalidades.

- **Ferramentas de Visualização**: Ferramentas de visualização podem ajudar você a ver as interações entre agentes de uma forma mais intuitiva. Por exemplo, você poderia ter um gráfico que mostra o fluxo de informações entre agentes. Isso pode ajudar a identificar gargalos, ineficiências e outros problemas no sistema.

- **Métricas de Desempenho**: Métricas de desempenho podem ajudar você a acompanhar a eficácia do sistema multi-agente. Por exemplo, você pode acompanhar o tempo levado para completar uma tarefa, o número de tarefas completadas por unidade de tempo e a precisão das recomendações feitas pelos agentes. Essa informação pode ajudar a identificar áreas para melhorias e otimizar o sistema.

## Padrões Multi-Agentes

Vamos aprofundar em alguns padrões concretos que podemos usar para criar apps multi-agentes. Aqui estão alguns padrões interessantes que valem a pena considerar:

### Bate-papo em grupo

Este padrão é útil quando você quer criar um aplicativo de bate-papo em grupo onde múltiplos agentes podem se comunicar entre si. Casos de uso típicos para este padrão incluem colaboração em equipe, suporte ao cliente e redes sociais.

Neste padrão, cada agente representa um usuário no bate-papo em grupo, e mensagens são trocadas entre agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para o grupo, receber mensagens do grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada onde todas as mensagens são roteadas através de um servidor central, ou uma arquitetura descentralizada onde as mensagens são trocadas diretamente.

![Bate-papo em grupo](../../../translated_images/pt-BR/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transferência de tarefa

Este padrão é útil quando você quer criar um aplicativo onde múltiplos agentes podem transferir tarefas entre si.

Casos de uso típicos para este padrão incluem suporte ao cliente, gerenciamento de tarefas e automação de fluxo de trabalho.

Neste padrão, cada agente representa uma tarefa ou um passo em um fluxo de trabalho, e agentes podem transferir tarefas para outros agentes com base em regras predefinidas.

![Transferência de tarefa](../../../translated_images/pt-BR/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtragem colaborativa

Este padrão é útil quando você quer criar um aplicativo onde múltiplos agentes podem colaborar para fazer recomendações aos usuários.

Por que você gostaria que múltiplos agentes colaborassem é porque cada agente pode ter expertise diferente e pode contribuir para o processo de recomendação de maneiras distintas.

Vamos a um exemplo onde um usuário quer uma recomendação sobre a melhor ação para comprar no mercado de ações.

- **Especialista em indústria**: Um agente pode ser especialista em uma indústria específica.
- **Análise técnica**: Outro agente pode ser especialista em análise técnica.
- **Análise fundamentalista**: e outro agente pode ser especialista em análise fundamentalista. Colaborando, esses agentes podem fornecer uma recomendação mais completa ao usuário.

![Recomendação](../../../translated_images/pt-BR/multi-agent-filtering.d959cb129dc9f608.webp)

## Cenário: Processo de reembolso

Considere um cenário onde um cliente está tentando obter um reembolso por um produto, pode haver muitos agentes envolvidos neste processo, mas vamos dividir entre agentes específicos para este processo e agentes gerais que podem ser usados em outros processos.

**Agentes específicos para o processo de reembolso**:

Seguem alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente do cliente**: Este agente representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente do vendedor**: Este agente representa o vendedor e é responsável por processar o reembolso.
- **Agente de pagamento**: Este agente representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente de resolução**: Este agente representa o processo de resolução e é responsável por resolver quaisquer problemas que surjam durante o processo de reembolso.
- **Agente de conformidade**: Este agente representa o processo de conformidade e é responsável por garantir que o processo de reembolso cumpra regulamentações e políticas.

**Agentes gerais**:

Esses agentes podem ser usados por outras partes do seu negócio.

- **Agente de envio**: Este agente representa o processo de envio e é responsável por enviar o produto de volta ao vendedor. Este agente pode ser usado tanto para o processo de reembolso quanto para o envio geral de um produto via compra, por exemplo.
- **Agente de feedback**: Este agente representa o processo de feedback e é responsável por coletar o feedback do cliente. O feedback pode ser dado a qualquer momento, não apenas durante o processo de reembolso.
- **Agente de escalonamento**: Este agente representa o processo de escalonamento e é responsável por escalar problemas para um nível superior de suporte. Você pode usar esse tipo de agente para qualquer processo onde precise escalar um problema.
- **Agente de notificações**: Este agente representa o processo de notificações e é responsável por enviar notificações ao cliente em várias etapas do processo de reembolso.
- **Agente de análises**: Este agente representa o processo de análises e é responsável por analisar dados relacionados ao processo de reembolso.
- **Agente de auditoria**: Este agente representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que está sendo realizado corretamente.
- **Agente de relatórios**: Este agente representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de conhecimento**: Este agente representa o processo de conhecimento e é responsável por manter uma base de conhecimento de informações relacionadas ao processo de reembolso. Este agente pode ter conhecimento tanto sobre reembolsos quanto outras partes do seu negócio.
- **Agente de segurança**: Este agente representa o processo de segurança e é responsável por garantir a segurança do processo de reembolso.
- **Agente de qualidade**: Este agente representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há muitos agentes listados anteriormente, tanto para o processo específico de reembolso quanto para os agentes gerais que podem ser usados em outras partes do seu negócio. Esperamos que isso dê uma ideia de como decidir quais agentes usar no seu sistema multi-agente.

## Tarefa

Projete um sistema multi-agente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, seus papéis e responsabilidades, e como eles interagem entre si. Considere tanto agentes específicos para o processo de suporte ao cliente quanto agentes gerais que podem ser usados em outras partes do seu negócio.
> Reflita antes de ler a solução a seguir, você pode precisar de mais agentes do que pensa.

> DICA: Pense sobre as diferentes etapas do processo de suporte ao cliente e também considere agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificações de conhecimento

Pergunta: Quando você deve considerar o uso de múltiplos agentes?

- [ ] A1: Quando você tem uma carga de trabalho pequena e uma tarefa simples.
- [ ] A2: Quando você tem uma carga de trabalho grande
- [ ] A3: Quando você tem uma tarefa simples.

[Quiz da solução](./solution/solution-quiz.md)

## Resumo

Nesta lição, examinamos o padrão de design de múltiplos agentes, incluindo os cenários em que múltiplos agentes são aplicáveis, as vantagens de usar múltiplos agentes em vez de um agente singular, os blocos de construção para implementar o padrão de design de múltiplos agentes, e como ter visibilidade de como os vários agentes estão interagindo uns com os outros.

### Tem mais perguntas sobre o padrão de design de múltiplos agentes?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e esclarecer suas dúvidas sobre Agentes de IA.

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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->