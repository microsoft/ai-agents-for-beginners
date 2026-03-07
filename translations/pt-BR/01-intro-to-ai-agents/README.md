[![Introdução aos Agentes de IA](../../../translated_images/pt-BR/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_


# Introdução aos Agentes de IA e Casos de Uso

Bem-vindo ao curso "Agentes de IA para Iniciantes"! Este curso fornece conhecimento fundamental e exemplos práticos para construir Agentes de IA.

Participe da <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> para encontrar outros aprendizes e construtores de Agentes de IA e tirar quaisquer dúvidas que tiver sobre este curso.

Para começar este curso, iniciamos entendendo melhor o que são Agentes de IA e como podemos usá-los nas aplicações e fluxos de trabalho que construímos.

## Introdução

Esta lição aborda:

- O que são Agentes de IA e quais são os diferentes tipos de agentes?
- Quais casos de uso são mais indicados para Agentes de IA e como eles podem nos ajudar?
- Quais são alguns dos blocos de construção básicos ao projetar Soluções Agentivas?

## Objetivos de Aprendizagem
Após concluir esta lição, você deverá ser capaz de:

- Compreender os conceitos de Agentes de IA e como eles diferem de outras soluções de IA.
- Aplicar Agentes de IA de forma mais eficiente.
- Projetar soluções agentivas de forma produtiva tanto para usuários quanto para clientes.

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Agentes de IA são **sistemas** que permitem que **Modelos de Linguagem de Grande Porte (LLMs)** **executem ações**, estendendo suas capacidades ao fornecer aos LLMs **acesso a ferramentas** e **conhecimento**.

Vamos dividir essa definição em partes menores:

- **Sistema** - É importante pensar nos agentes não apenas como um único componente, mas como um sistema de muitos componentes. Em um nível básico, os componentes de um Agente de IA são:
  - **Ambiente** - O espaço definido onde o Agente de IA está operando. Por exemplo, se tivéssemos um Agente de IA para reserva de viagens, o ambiente poderia ser o sistema de reservas de viagem que o Agente de IA usa para completar tarefas.
  - **Sensores** - Os ambientes possuem informações e fornecem feedback. Agentes de IA usam sensores para coletar e interpretar essas informações sobre o estado atual do ambiente. No exemplo do Agente de Reserva de Viagens, o sistema de reservas pode fornecer informações como disponibilidade de hotéis ou preços de voos.
  - **Atuadores** - Uma vez que o Agente de IA recebe o estado atual do ambiente, para a tarefa atual o agente determina qual ação executar para alterar o ambiente. Para o agente de reservas de viagens, pode ser reservar um quarto disponível para o usuário.

![O que são Agentes de IA?](../../../translated_images/pt-BR/what-are-ai-agents.1ec8c4d548af601a.webp)

**Modelos de Linguagem de Grande Porte** - O conceito de agentes existia antes da criação dos LLMs. A vantagem de construir Agentes de IA com LLMs é a habilidade deles de interpretar a linguagem humana e os dados. Essa habilidade permite que os LLMs interpretem informações do ambiente e definam um plano para alterar o ambiente.

**Executar Ações** - Fora de sistemas de Agentes de IA, os LLMs estão limitados a situações em que a ação é gerar conteúdo ou informações com base no prompt do usuário. Dentro de sistemas de Agentes de IA, os LLMs podem realizar tarefas interpretando a solicitação do usuário e usando as ferramentas disponíveis em seu ambiente.

**Acesso a Ferramentas** - Quais ferramentas o LLM tem acesso é definido por 1) o ambiente em que ele está operando e 2) o desenvolvedor do Agente de IA. No nosso exemplo do agente de viagens, as ferramentas do agente são limitadas pelas operações disponíveis no sistema de reservas, e/ou o desenvolvedor pode limitar o acesso do agente às ferramentas relacionadas a voos.

**Memória+Conhecimento** - A memória pode ser de curto prazo no contexto da conversa entre o usuário e o agente. A longo prazo, além das informações fornecidas pelo ambiente, Agentes de IA também podem recuperar conhecimento de outros sistemas, serviços, ferramentas e até mesmo outros agentes. No exemplo do agente de viagens, esse conhecimento pode ser as informações sobre as preferências de viagem do usuário localizadas em um banco de dados de clientes.

### Os diferentes tipos de agentes

Agora que temos uma definição geral de Agentes de IA, vejamos alguns tipos específicos de agentes e como eles seriam aplicados a um agente de reservas de viagens.

| **Tipo de Agente**                | **Descrição**                                                                                                                       | **Exemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes Reflexos Simples**      | Executam ações imediatas com base em regras pré-definidas.                                                                                  | O agente de viagens interpreta o contexto do e-mail e encaminha reclamações de viagem para o atendimento ao cliente.                                                                                                                          |
| **Agentes Reflexos Baseados em Modelo** | Executam ações com base em um modelo do mundo e nas alterações desse modelo.                                                              | O agente de viagens prioriza rotas com mudanças de preço significativas com base no acesso a dados históricos de preços.                                                                                                             |
| **Agentes Baseados em Objetivos**         | Criam planos para alcançar objetivos específicos interpretando o objetivo e determinando ações para alcançá-lo.                                  | O agente de viagens reserva uma jornada determinando os arranjos de viagem necessários (carro, transporte público, voos) do local atual até o destino.                                                                                |
| **Agentes Baseados em Utilidade**      | Consideram preferências e ponderam trade-offs numericamente para determinar como alcançar objetivos.                                               | O agente de viagens maximiza a utilidade ao ponderar conveniência versus custo ao reservar uma viagem.                                                                                                                                          |
| **Agentes de Aprendizado**           | Melhoram ao longo do tempo respondendo a feedbacks e ajustando as ações de acordo.                                                        | O agente de viagens melhora usando o feedback dos clientes de pesquisas pós-viagem para fazer ajustes em reservas futuras.                                                                                                               |
| **Agentes Hierárquicos**       | Apresentam múltiplos agentes em um sistema em camadas, com agentes de nível superior dividindo tarefas em subtarefas para que agentes de nível inferior as completem. | O agente de viagens cancela uma viagem dividindo a tarefa em subtarefas (por exemplo, cancelar reservas específicas) e fazendo com que agentes de nível inferior as completem, reportando de volta ao agente de nível superior.                                     |
| **Sistemas Multiagentes (MAS)** | Agentes completam tarefas independentemente, seja de forma cooperativa ou competitiva.                                                           | Cooperativo: Múltiplos agentes reservam serviços de viagem específicos, como hotéis, voos e entretenimento. Competitivo: Múltiplos agentes gerenciam e competem por um calendário de reservas de hotel compartilhado para alocar clientes no hotel. |

## Quando Usar Agentes de IA

Na seção anterior, usamos o caso de uso do Agente de Viagens para explicar como os diferentes tipos de agentes podem ser usados em diferentes cenários de reserva de viagens. Continuaremos a usar essa aplicação ao longo do curso.

Vamos olhar os tipos de casos de uso para os quais Agentes de IA são mais indicados:

![Quando usar Agentes de IA?](../../../translated_images/pt-BR/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemas Abertos** - permitindo que o LLM determine as etapas necessárias para completar uma tarefa porque nem sempre é possível codificá-las rigidamente em um fluxo de trabalho.
- **Processos de Múltiplas Etapas** - tarefas que exigem um nível de complexidade em que o Agente de IA precisa usar ferramentas ou informações ao longo de múltiplas interações em vez de uma recuperação única.  
- **Melhora ao Longo do Tempo** - tarefas em que o agente pode melhorar ao longo do tempo recebendo feedback do seu ambiente ou dos usuários para fornecer melhor utilidade.

Cobrimos mais considerações sobre o uso de Agentes de IA na lição Construindo Agentes de IA Confiáveis.

## Noções Básicas de Soluções Agentivas

### Desenvolvimento de Agentes

O primeiro passo no projeto de um sistema de Agente de IA é definir as ferramentas, ações e comportamentos. Neste curso, focamos no uso do **Azure AI Agent Service** para definir nossos Agentes. Ele oferece recursos como:

- Seleção de Modelos Abertos, como OpenAI, Mistral e Llama
- Uso de Dados Licenciados por meio de provedores como o Tripadvisor
- Uso de ferramentas padronizadas OpenAPI 3.0

### Padrões Agentivos

A comunicação com LLMs é feita por meio de prompts. Dada a natureza semi-autônoma dos Agentes de IA, nem sempre é possível ou necessário reenviar prompts manualmente ao LLM após uma alteração no ambiente. Usamos **Padrões Agentivos** que nos permitem acionar o LLM em múltiplas etapas de forma mais escalável.

Este curso está dividido em alguns dos padrões agentivos populares atualmente.

### Frameworks Agentivos

Frameworks agentivos permitem que desenvolvedores implementem padrões agentivos por meio de código. Esses frameworks oferecem templates, plugins e ferramentas para melhor colaboração entre Agentes de IA. Esses benefícios fornecem capacidades para melhor observabilidade e solução de problemas de sistemas de Agentes de IA.

Neste curso, exploraremos o Microsoft Agent Framework (MAF) para construir agentes de IA prontos para produção.

## Códigos de Exemplo

- Python: [Framework de Agente](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Framework de Agente](./code_samples/01-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre Agentes de IA?

Participe do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e ter suas perguntas sobre Agentes de IA respondidas.

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentivos](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido usando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->