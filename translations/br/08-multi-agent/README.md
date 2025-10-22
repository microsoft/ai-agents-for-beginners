<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T12:46:51+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "br"
}
-->
[![Design de Multi-Agentes](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.br.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Padrões de design de multi-agentes

Assim que você começar a trabalhar em um projeto que envolve múltiplos agentes, será necessário considerar o padrão de design de multi-agentes. No entanto, pode não ser imediatamente claro quando mudar para multi-agentes e quais são as vantagens.

## Introdução

Nesta lição, buscamos responder às seguintes perguntas:

- Quais são os cenários em que multi-agentes são aplicáveis?
- Quais são as vantagens de usar multi-agentes em vez de apenas um único agente realizando várias tarefas?
- Quais são os blocos de construção para implementar o padrão de design de multi-agentes?
- Como podemos ter visibilidade sobre como os múltiplos agentes estão interagindo entre si?

## Objetivos de Aprendizado

Após esta lição, você deverá ser capaz de:

- Identificar cenários em que multi-agentes são aplicáveis.
- Reconhecer as vantagens de usar multi-agentes em vez de um único agente.
- Compreender os blocos de construção para implementar o padrão de design de multi-agentes.

Qual é o panorama geral?

*Multi-agentes são um padrão de design que permite que múltiplos agentes trabalhem juntos para alcançar um objetivo comum*.

Esse padrão é amplamente utilizado em diversos campos, incluindo robótica, sistemas autônomos e computação distribuída.

## Cenários em que Multi-Agentes São Aplicáveis

Então, quais cenários são bons casos de uso para multi-agentes? A resposta é que há muitos cenários em que empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes volumes de trabalho**: Grandes volumes de trabalho podem ser divididos em tarefas menores e atribuídos a diferentes agentes, permitindo processamento paralelo e conclusão mais rápida. Um exemplo disso é no caso de uma grande tarefa de processamento de dados.
- **Tarefas complexas**: Tarefas complexas, assim como grandes volumes de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado em um aspecto específico da tarefa. Um bom exemplo disso é no caso de veículos autônomos, onde diferentes agentes gerenciam navegação, detecção de obstáculos e comunicação com outros veículos.
- **Diversidade de especialização**: Diferentes agentes podem ter especializações diversas, permitindo que lidem com diferentes aspectos de uma tarefa de forma mais eficaz do que um único agente. Para este caso, um bom exemplo é na área da saúde, onde agentes podem gerenciar diagnósticos, planos de tratamento e monitoramento de pacientes.

## Vantagens de Usar Multi-Agentes em Relação a um Único Agente

Um sistema de agente único pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode oferecer várias vantagens:

- **Especialização**: Cada agente pode ser especializado em uma tarefa específica. A falta de especialização em um único agente significa que ele pode fazer de tudo, mas pode se confundir ao enfrentar uma tarefa complexa. Por exemplo, ele pode acabar realizando uma tarefa para a qual não está melhor preparado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes do que sobrecarregando um único agente.
- **Tolerância a falhas**: Se um agente falhar, outros podem continuar funcionando, garantindo a confiabilidade do sistema.

Vamos pegar um exemplo: reservar uma viagem para um usuário. Um sistema de agente único teria que lidar com todos os aspectos do processo de reserva de viagem, desde encontrar voos até reservar hotéis e carros de aluguel. Para alcançar isso com um único agente, ele precisaria ter ferramentas para lidar com todas essas tarefas. Isso poderia levar a um sistema complexo e monolítico, difícil de manter e escalar. Um sistema de multi-agentes, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros de aluguel. Isso tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isso a uma agência de viagens administrada como uma loja familiar versus uma agência de viagens operada como uma franquia. A loja familiar teria um único agente lidando com todos os aspectos do processo de reserva de viagem, enquanto a franquia teria diferentes agentes lidando com diferentes aspectos do processo.

## Blocos de Construção para Implementar o Padrão de Design de Multi-Agentes

Antes de implementar o padrão de design de multi-agentes, é necessário entender os blocos de construção que compõem o padrão.

Vamos tornar isso mais concreto olhando novamente para o exemplo de reservar uma viagem para um usuário. Nesse caso, os blocos de construção incluiriam:

- **Comunicação entre agentes**: Agentes para encontrar voos, reservar hotéis e carros de aluguel precisam se comunicar e compartilhar informações sobre as preferências e restrições do usuário. É necessário decidir os protocolos e métodos para essa comunicação. Concretamente, isso significa que o agente para encontrar voos precisa se comunicar com o agente para reservar hotéis para garantir que o hotel seja reservado para as mesmas datas do voo. Isso significa que os agentes precisam compartilhar informações sobre as datas de viagem do usuário, ou seja, você precisa decidir *quais agentes estão compartilhando informações e como estão compartilhando*.
- **Mecanismos de coordenação**: Os agentes precisam coordenar suas ações para garantir que as preferências e restrições do usuário sejam atendidas. Uma preferência do usuário pode ser que ele queira um hotel próximo ao aeroporto, enquanto uma restrição pode ser que carros de aluguel estejam disponíveis apenas no aeroporto. Isso significa que o agente para reservar hotéis precisa coordenar com o agente para reservar carros de aluguel para garantir que as preferências e restrições do usuário sejam atendidas. Isso significa que você precisa decidir *como os agentes estão coordenando suas ações*.
- **Arquitetura do agente**: Os agentes precisam ter uma estrutura interna para tomar decisões e aprender com suas interações com o usuário. Isso significa que o agente para encontrar voos precisa ter a estrutura interna para tomar decisões sobre quais voos recomendar ao usuário. Isso significa que você precisa decidir *como os agentes estão tomando decisões e aprendendo com suas interações com o usuário*. Exemplos de como um agente aprende e melhora podem incluir o uso de um modelo de aprendizado de máquina para recomendar voos ao usuário com base em suas preferências anteriores.
- **Visibilidade nas interações de multi-agentes**: É necessário ter visibilidade sobre como os múltiplos agentes estão interagindo entre si. Isso significa que você precisa ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode ser na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.
- **Padrões de multi-agentes**: Existem diferentes padrões para implementar sistemas de multi-agentes, como arquiteturas centralizadas, descentralizadas e híbridas. É necessário decidir o padrão que melhor se adapta ao seu caso de uso.
- **Humano no loop**: Na maioria dos casos, haverá um humano no loop, e você precisa instruir os agentes sobre quando pedir intervenção humana. Isso pode ser na forma de um usuário solicitando um hotel ou voo específico que os agentes não recomendaram ou pedindo confirmação antes de reservar um voo ou hotel.

## Visibilidade nas Interações de Multi-Agentes

É importante ter visibilidade sobre como os múltiplos agentes estão interagindo entre si. Essa visibilidade é essencial para depuração, otimização e garantia da eficácia geral do sistema. Para alcançar isso, é necessário ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode ser na forma de ferramentas de registro e monitoramento, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um usuário, você poderia ter um painel que mostra o status de cada agente, as preferências e restrições do usuário e as interações entre os agentes. Esse painel poderia mostrar as datas de viagem do usuário, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis e os carros de aluguel recomendados pelo agente de carros de aluguel. Isso daria uma visão clara de como os agentes estão interagindo entre si e se as preferências e restrições do usuário estão sendo atendidas.

Vamos analisar cada um desses aspectos com mais detalhes.

- **Ferramentas de registro e monitoramento**: Você deve registrar cada ação realizada por um agente. Uma entrada de registro pode armazenar informações sobre o agente que realizou a ação, a ação realizada, o horário em que a ação foi realizada e o resultado da ação. Essas informações podem ser usadas para depuração, otimização e mais.
- **Ferramentas de visualização**: Ferramentas de visualização podem ajudar a ver as interações entre agentes de uma maneira mais intuitiva. Por exemplo, você poderia ter um gráfico que mostra o fluxo de informações entre os agentes. Isso pode ajudar a identificar gargalos, ineficiências e outros problemas no sistema.
- **Métricas de desempenho**: Métricas de desempenho podem ajudar a rastrear a eficácia do sistema de multi-agentes. Por exemplo, você poderia rastrear o tempo necessário para concluir uma tarefa, o número de tarefas concluídas por unidade de tempo e a precisão das recomendações feitas pelos agentes. Essas informações podem ajudar a identificar áreas para melhoria e otimizar o sistema.

## Padrões de Multi-Agentes

Vamos explorar alguns padrões concretos que podemos usar para criar aplicativos de multi-agentes. Aqui estão alguns padrões interessantes a serem considerados:

### Chat em grupo

Este padrão é útil quando você deseja criar um aplicativo de chat em grupo onde múltiplos agentes podem se comunicar entre si. Casos de uso típicos para este padrão incluem colaboração em equipe, suporte ao cliente e redes sociais.

Neste padrão, cada agente representa um usuário no chat em grupo, e as mensagens são trocadas entre os agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para o chat em grupo, receber mensagens do chat em grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada, onde todas as mensagens são roteadas por um servidor central, ou uma arquitetura descentralizada, onde as mensagens são trocadas diretamente.

![Chat em grupo](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.br.png)

### Transferência de tarefas

Este padrão é útil quando você deseja criar um aplicativo onde múltiplos agentes podem transferir tarefas entre si.

Casos de uso típicos para este padrão incluem suporte ao cliente, gerenciamento de tarefas e automação de fluxos de trabalho.

Neste padrão, cada agente representa uma tarefa ou uma etapa em um fluxo de trabalho, e os agentes podem transferir tarefas para outros agentes com base em regras predefinidas.

![Transferência de tarefas](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.br.png)

### Filtragem colaborativa

Este padrão é útil quando você deseja criar um aplicativo onde múltiplos agentes podem colaborar para fazer recomendações aos usuários.

Por que você gostaria que múltiplos agentes colaborassem? Porque cada agente pode ter diferentes especializações e pode contribuir para o processo de recomendação de maneiras diferentes.

Vamos pegar um exemplo onde um usuário deseja uma recomendação sobre a melhor ação para comprar no mercado de ações.

- **Especialista em indústria**: Um agente pode ser especialista em um setor específico.
- **Análise técnica**: Outro agente pode ser especialista em análise técnica.
- **Análise fundamental**: E outro agente pode ser especialista em análise fundamental. Ao colaborar, esses agentes podem fornecer uma recomendação mais abrangente ao usuário.

![Recomendação](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.br.png)

## Cenário: Processo de reembolso

Considere um cenário onde um cliente está tentando obter um reembolso por um produto. Pode haver vários agentes envolvidos nesse processo, mas vamos dividi-los entre agentes específicos para este processo e agentes gerais que podem ser usados em outros processos.

**Agentes específicos para o processo de reembolso**:

A seguir estão alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente do cliente**: Representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente do vendedor**: Representa o vendedor e é responsável por processar o reembolso.
- **Agente de pagamento**: Representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente de resolução**: Representa o processo de resolução e é responsável por resolver quaisquer problemas que surjam durante o processo de reembolso.
- **Agente de conformidade**: Representa o processo de conformidade e é responsável por garantir que o processo de reembolso esteja em conformidade com regulamentos e políticas.

**Agentes gerais**:

Esses agentes podem ser usados em outras partes do seu negócio.

- **Agente de envio**: Representa o processo de envio e é responsável por enviar o produto de volta ao vendedor. Este agente pode ser usado tanto para o processo de reembolso quanto para o envio geral de um produto, por exemplo, em uma compra.
- **Agente de feedback**: Representa o processo de feedback e é responsável por coletar feedback do cliente. O feedback pode ser coletado a qualquer momento, não apenas durante o processo de reembolso.
- **Agente de escalonamento**: Representa o processo de escalonamento e é responsável por escalar problemas para um nível superior de suporte. Este tipo de agente pode ser usado em qualquer processo onde seja necessário escalar um problema.
- **Agente de notificações**: Representa o processo de notificações e é responsável por enviar notificações ao cliente em várias etapas do processo de reembolso.
- **Agente de análise**: Representa o processo de análise e é responsável por analisar dados relacionados ao processo de reembolso.
- **Agente de auditoria**: Representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que ele esteja sendo realizado corretamente.
- **Agente de relatórios**: Representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de conhecimento**: Representa o processo de conhecimento e é responsável por manter uma base de conhecimento de informações relacionadas ao processo de reembolso. Este agente pode ser útil tanto para reembolsos quanto para outras partes do seu negócio.
- **Agente de segurança**: Representa o processo de segurança e é responsável por garantir a segurança do processo de reembolso.
- **Agente de qualidade**: Representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há muitos agentes listados anteriormente, tanto para o processo específico de reembolso quanto para os agentes gerais que podem ser usados em outras partes do seu negócio. Esperamos que isso lhe dê uma ideia de como decidir quais agentes usar em seu sistema de multi-agentes.

## Tarefa
## Solução

Projete um sistema multiagente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, seus papéis e responsabilidades, e como eles interagem entre si. Considere tanto agentes específicos para o processo de suporte ao cliente quanto agentes gerais que podem ser usados em outras partes do seu negócio.

> Pense bem antes de ler a solução a seguir, você pode precisar de mais agentes do que imagina.

> DICA: Pense nas diferentes etapas do processo de suporte ao cliente e também considere os agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificação de conhecimento

Pergunta: Quando você deve considerar o uso de multiagentes?

- [ ] A1: Quando você tem uma carga de trabalho pequena e uma tarefa simples.
- [ ] A2: Quando você tem uma grande carga de trabalho.
- [ ] A3: Quando você tem uma tarefa simples.

[Quiz da solução](./solution/solution-quiz.md)

## Resumo

Nesta lição, analisamos o padrão de design multiagente, incluindo os cenários onde os multiagentes são aplicáveis, as vantagens de usar multiagentes em vez de um agente singular, os blocos de construção para implementar o padrão de design multiagente e como ter visibilidade sobre como os múltiplos agentes estão interagindo entre si.

### Tem mais perguntas sobre o padrão de design multiagente?

Participe do [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre agentes de IA.

## Recursos adicionais

- 

## Lição anterior

[Planejamento e Design](../07-planning-design/README.md)

## Próxima lição

[Metacognição em Agentes de IA](../09-metacognition/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.