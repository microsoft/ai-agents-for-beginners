<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-30T14:11:05+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "pt"
}
-->
[![Design de Multi-Agentes](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.pt.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Padrões de design de multi-agentes

Assim que começar a trabalhar num projeto que envolva múltiplos agentes, será necessário considerar o padrão de design de multi-agentes. No entanto, pode não ser imediatamente claro quando mudar para multi-agentes e quais são as vantagens.

## Introdução

Nesta lição, procuramos responder às seguintes perguntas:

- Quais são os cenários em que os multi-agentes são aplicáveis?
- Quais são as vantagens de usar multi-agentes em vez de um único agente a realizar várias tarefas?
- Quais são os blocos de construção para implementar o padrão de design de multi-agentes?
- Como podemos ter visibilidade sobre como os múltiplos agentes estão a interagir entre si?

## Objetivos de Aprendizagem

Após esta lição, deverá ser capaz de:

- Identificar cenários em que os multi-agentes são aplicáveis.
- Reconhecer as vantagens de usar multi-agentes em vez de um único agente.
- Compreender os blocos de construção para implementar o padrão de design de multi-agentes.

Qual é o panorama geral?

*Multi-agentes são um padrão de design que permite que múltiplos agentes trabalhem juntos para alcançar um objetivo comum*.

Este padrão é amplamente utilizado em vários campos, incluindo robótica, sistemas autónomos e computação distribuída.

## Cenários em que os Multi-Agentes São Aplicáveis

Então, quais são os cenários que justificam o uso de multi-agentes? A resposta é que existem muitos cenários em que empregar múltiplos agentes é benéfico, especialmente nos seguintes casos:

- **Grandes volumes de trabalho**: Grandes volumes de trabalho podem ser divididos em tarefas menores e atribuídos a diferentes agentes, permitindo processamento paralelo e conclusão mais rápida. Um exemplo disso é no caso de uma tarefa de processamento de dados em larga escala.
- **Tarefas complexas**: Tarefas complexas, assim como grandes volumes de trabalho, podem ser divididas em subtarefas menores e atribuídas a diferentes agentes, cada um especializado num aspeto específico da tarefa. Um bom exemplo disso é no caso de veículos autónomos, onde diferentes agentes gerem navegação, deteção de obstáculos e comunicação com outros veículos.
- **Diversidade de competências**: Diferentes agentes podem ter competências diversas, permitindo-lhes lidar com diferentes aspetos de uma tarefa de forma mais eficaz do que um único agente. Neste caso, um bom exemplo é na área da saúde, onde agentes podem gerir diagnósticos, planos de tratamento e monitorização de pacientes.

## Vantagens de Usar Multi-Agentes em Relação a um Único Agente

Um sistema com um único agente pode funcionar bem para tarefas simples, mas para tarefas mais complexas, usar múltiplos agentes pode oferecer várias vantagens:

- **Especialização**: Cada agente pode ser especializado numa tarefa específica. A falta de especialização num único agente significa que este pode realizar várias tarefas, mas pode ficar confuso ao lidar com uma tarefa complexa. Por exemplo, pode acabar por realizar uma tarefa para a qual não está melhor preparado.
- **Escalabilidade**: É mais fácil escalar sistemas adicionando mais agentes do que sobrecarregando um único agente.
- **Tolerância a falhas**: Se um agente falhar, outros podem continuar a funcionar, garantindo a fiabilidade do sistema.

Vamos a um exemplo: reservar uma viagem para um utilizador. Um sistema com um único agente teria de lidar com todos os aspetos do processo de reserva, desde encontrar voos até reservar hotéis e carros de aluguer. Para isso, o agente precisaria de ferramentas para lidar com todas essas tarefas. Isso poderia levar a um sistema complexo e monolítico, difícil de manter e escalar. Um sistema de multi-agentes, por outro lado, poderia ter diferentes agentes especializados em encontrar voos, reservar hotéis e carros de aluguer. Isso tornaria o sistema mais modular, mais fácil de manter e escalável.

Compare isso com uma agência de viagens gerida como um pequeno negócio familiar versus uma agência gerida como uma franquia. O pequeno negócio teria um único agente a lidar com todos os aspetos do processo de reserva, enquanto a franquia teria diferentes agentes a lidar com diferentes aspetos do processo.

## Blocos de Construção para Implementar o Padrão de Design de Multi-Agentes

Antes de implementar o padrão de design de multi-agentes, é necessário compreender os blocos de construção que compõem o padrão.

Vamos tornar isso mais concreto, olhando novamente para o exemplo de reservar uma viagem para um utilizador. Neste caso, os blocos de construção incluiriam:

- **Comunicação entre Agentes**: Agentes para encontrar voos, reservar hotéis e carros de aluguer precisam de comunicar e partilhar informações sobre as preferências e restrições do utilizador. É necessário decidir os protocolos e métodos para essa comunicação. Concretamente, isso significa que o agente para encontrar voos precisa de comunicar com o agente para reservar hotéis para garantir que o hotel é reservado para as mesmas datas do voo. Isso implica decidir *quais agentes partilham informações e como o fazem*.
- **Mecanismos de Coordenação**: Os agentes precisam de coordenar as suas ações para garantir que as preferências e restrições do utilizador são atendidas. Uma preferência do utilizador pode ser que ele queira um hotel próximo do aeroporto, enquanto uma restrição pode ser que os carros de aluguer só estão disponíveis no aeroporto. Isso significa que o agente para reservar hotéis precisa de coordenar com o agente para reservar carros de aluguer para garantir que as preferências e restrições do utilizador são atendidas. Isso implica decidir *como os agentes estão a coordenar as suas ações*.
- **Arquitetura dos Agentes**: Os agentes precisam de ter uma estrutura interna para tomar decisões e aprender com as suas interações com o utilizador. Isso significa que o agente para encontrar voos precisa de ter uma estrutura interna para tomar decisões sobre quais voos recomendar ao utilizador. Isso implica decidir *como os agentes estão a tomar decisões e a aprender com as suas interações com o utilizador*. Exemplos de como um agente aprende e melhora podem incluir o uso de um modelo de aprendizagem automática para recomendar voos ao utilizador com base nas suas preferências anteriores.
- **Visibilidade nas Interações entre Multi-Agentes**: É necessário ter visibilidade sobre como os múltiplos agentes estão a interagir entre si. Isso significa ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode incluir ferramentas de registo e monitorização, ferramentas de visualização e métricas de desempenho.
- **Padrões de Multi-Agentes**: Existem diferentes padrões para implementar sistemas de multi-agentes, como arquiteturas centralizadas, descentralizadas e híbridas. É necessário decidir o padrão que melhor se adapta ao seu caso de uso.
- **Humano no Circuito**: Na maioria dos casos, haverá um humano no circuito, e é necessário instruir os agentes sobre quando pedir intervenção humana. Isso pode incluir um utilizador a pedir um hotel ou voo específico que os agentes não recomendaram ou a pedir confirmação antes de reservar um voo ou hotel.

## Visibilidade nas Interações entre Multi-Agentes

É importante ter visibilidade sobre como os múltiplos agentes estão a interagir entre si. Essa visibilidade é essencial para depurar, otimizar e garantir a eficácia geral do sistema. Para isso, é necessário ter ferramentas e técnicas para rastrear as atividades e interações dos agentes. Isso pode incluir ferramentas de registo e monitorização, ferramentas de visualização e métricas de desempenho.

Por exemplo, no caso de reservar uma viagem para um utilizador, poderia haver um painel que mostra o estado de cada agente, as preferências e restrições do utilizador e as interações entre os agentes. Este painel poderia mostrar as datas de viagem do utilizador, os voos recomendados pelo agente de voos, os hotéis recomendados pelo agente de hotéis e os carros de aluguer recomendados pelo agente de carros de aluguer. Isso daria uma visão clara de como os agentes estão a interagir entre si e se as preferências e restrições do utilizador estão a ser atendidas.

Vamos analisar cada um desses aspetos com mais detalhe.

- **Ferramentas de Registo e Monitorização**: É importante registar cada ação realizada por um agente. Um registo pode armazenar informações sobre o agente que realizou a ação, a ação realizada, o momento em que a ação foi realizada e o resultado da ação. Essas informações podem ser usadas para depuração, otimização e mais.
- **Ferramentas de Visualização**: Ferramentas de visualização podem ajudar a ver as interações entre agentes de forma mais intuitiva. Por exemplo, poderia haver um gráfico que mostra o fluxo de informações entre agentes. Isso poderia ajudar a identificar gargalos, ineficiências e outros problemas no sistema.
- **Métricas de Desempenho**: Métricas de desempenho podem ajudar a acompanhar a eficácia do sistema de multi-agentes. Por exemplo, poderia acompanhar o tempo necessário para concluir uma tarefa, o número de tarefas concluídas por unidade de tempo e a precisão das recomendações feitas pelos agentes. Essas informações podem ajudar a identificar áreas para melhoria e otimizar o sistema.

## Padrões de Multi-Agentes

Vamos explorar alguns padrões concretos que podemos usar para criar aplicações de multi-agentes. Aqui estão alguns padrões interessantes a considerar:

### Chat em Grupo

Este padrão é útil quando se pretende criar uma aplicação de chat em grupo onde múltiplos agentes podem comunicar entre si. Casos de uso típicos para este padrão incluem colaboração em equipa, suporte ao cliente e redes sociais.

Neste padrão, cada agente representa um utilizador no chat em grupo, e as mensagens são trocadas entre agentes usando um protocolo de mensagens. Os agentes podem enviar mensagens para o chat em grupo, receber mensagens do chat em grupo e responder a mensagens de outros agentes.

Este padrão pode ser implementado usando uma arquitetura centralizada, onde todas as mensagens são encaminhadas através de um servidor central, ou uma arquitetura descentralizada, onde as mensagens são trocadas diretamente.

![Chat em Grupo](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.pt.png)

### Transferência de Tarefas

Este padrão é útil quando se pretende criar uma aplicação onde múltiplos agentes podem transferir tarefas entre si.

Casos de uso típicos para este padrão incluem suporte ao cliente, gestão de tarefas e automação de fluxos de trabalho.

Neste padrão, cada agente representa uma tarefa ou um passo num fluxo de trabalho, e os agentes podem transferir tarefas para outros agentes com base em regras predefinidas.

![Transferência de Tarefas](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.pt.png)

### Filtragem Colaborativa

Este padrão é útil quando se pretende criar uma aplicação onde múltiplos agentes podem colaborar para fazer recomendações aos utilizadores.

A razão para querer múltiplos agentes a colaborar é que cada agente pode ter competências diferentes e contribuir para o processo de recomendação de formas distintas.

Vamos a um exemplo onde um utilizador quer uma recomendação sobre a melhor ação para comprar no mercado de ações.

- **Especialista na Indústria**: Um agente poderia ser especialista numa indústria específica.
- **Análise Técnica**: Outro agente poderia ser especialista em análise técnica.
- **Análise Fundamental**: E outro agente poderia ser especialista em análise fundamental. Ao colaborar, esses agentes podem fornecer uma recomendação mais abrangente ao utilizador.

![Recomendação](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.pt.png)

## Cenário: Processo de Reembolso

Considere um cenário onde um cliente está a tentar obter um reembolso por um produto. Podem estar envolvidos vários agentes neste processo, mas vamos dividi-los entre agentes específicos para este processo e agentes gerais que podem ser usados noutros processos.

**Agentes específicos para o processo de reembolso**:

Os seguintes são alguns agentes que poderiam estar envolvidos no processo de reembolso:

- **Agente do Cliente**: Este agente representa o cliente e é responsável por iniciar o processo de reembolso.
- **Agente do Vendedor**: Este agente representa o vendedor e é responsável por processar o reembolso.
- **Agente de Pagamento**: Este agente representa o processo de pagamento e é responsável por reembolsar o pagamento do cliente.
- **Agente de Resolução**: Este agente representa o processo de resolução e é responsável por resolver quaisquer problemas que surjam durante o processo de reembolso.
- **Agente de Conformidade**: Este agente representa o processo de conformidade e é responsável por garantir que o processo de reembolso cumpre os regulamentos e políticas.

**Agentes gerais**:

Estes agentes podem ser usados noutras partes do seu negócio.

- **Agente de Envio**: Este agente representa o processo de envio e é responsável por enviar o produto de volta ao vendedor. Este agente pode ser usado tanto para o processo de reembolso como para o envio geral de um produto, por exemplo, numa compra.
- **Agente de Feedback**: Este agente representa o processo de feedback e é responsável por recolher feedback do cliente. O feedback pode ser recolhido a qualquer momento e não apenas durante o processo de reembolso.
- **Agente de Escalação**: Este agente representa o processo de escalação e é responsável por escalar problemas para um nível superior de suporte. Pode usar este tipo de agente para qualquer processo onde seja necessário escalar um problema.
- **Agente de Notificação**: Este agente representa o processo de notificação e é responsável por enviar notificações ao cliente em várias etapas do processo de reembolso.
- **Agente de Análise**: Este agente representa o processo de análise e é responsável por analisar dados relacionados ao processo de reembolso.
- **Agente de Auditoria**: Este agente representa o processo de auditoria e é responsável por auditar o processo de reembolso para garantir que está a ser realizado corretamente.
- **Agente de Relatórios**: Este agente representa o processo de relatórios e é responsável por gerar relatórios sobre o processo de reembolso.
- **Agente de Conhecimento**: Este agente representa o processo de conhecimento e é responsável por manter uma base de conhecimento com informações relacionadas ao processo de reembolso. Este agente pode ser conhecedor tanto de reembolsos como de outras partes do seu negócio.
- **Agente de Segurança**: Este agente representa o processo de segurança e é responsável por garantir a segurança do processo de reembolso.
- **Agente de Qualidade**: Este agente representa o processo de qualidade e é responsável por garantir a qualidade do processo de reembolso.

Há bastantes agentes listados anteriormente, tanto para o processo específico de reembolso como para os agentes gerais que podem ser usados noutras partes do seu negócio. Esperamos que isso lhe dê uma ideia de como pode decidir quais agentes usar no seu sistema de multi-agentes.

## Tarefa
Desenhe um sistema multi-agente para um processo de suporte ao cliente. Identifique os agentes envolvidos no processo, os seus papéis e responsabilidades, e como interagem entre si. Considere tanto agentes específicos para o processo de suporte ao cliente como agentes gerais que podem ser utilizados noutras partes do seu negócio.

> Pense bem antes de ler a solução abaixo, pode precisar de mais agentes do que imagina.

> TIP: Pense nas diferentes etapas do processo de suporte ao cliente e também nos agentes necessários para qualquer sistema.

## Solução

[Solução](./solution/solution.md)

## Verificação de conhecimentos

Pergunta: Quando deve considerar usar multi-agentes?

- [ ] A1: Quando tem uma carga de trabalho pequena e uma tarefa simples.
- [ ] A2: Quando tem uma grande carga de trabalho.
- [ ] A3: Quando tem uma tarefa simples.

[Solução do questionário](./solution/solution-quiz.md)

## Resumo

Nesta lição, analisámos o padrão de design multi-agente, incluindo os cenários onde os multi-agentes são aplicáveis, as vantagens de usar multi-agentes em vez de um agente singular, os blocos de construção para implementar o padrão de design multi-agente, e como ter visibilidade sobre como os múltiplos agentes interagem entre si.

### Tem mais perguntas sobre o Padrão de Design Multi-Agente?

Junte-se ao [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar em horários de atendimento e obter respostas às suas perguntas sobre Agentes de IA.

## Recursos adicionais

-

## Lição anterior

[Planeamento de Design](../07-planning-design/README.md)

## Próxima lição

[Metacognição em Agentes de IA](../09-metacognition/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.