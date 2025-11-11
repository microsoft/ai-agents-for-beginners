<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdd28bc00816d2773bb2b5968d782abc",
  "translation_date": "2025-11-11T11:10:53+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "br"
}
-->
[![Introdução aos Agentes de IA](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.br.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Introdução aos Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso "Agentes de IA para Iniciantes"! Este curso oferece conhecimentos fundamentais e exemplos práticos para construir Agentes de IA.

Participe da <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> para conhecer outros aprendizes e criadores de Agentes de IA e tirar suas dúvidas sobre este curso.

Para começar este curso, vamos entender melhor o que são Agentes de IA e como podemos utilizá-los em aplicações e fluxos de trabalho que criamos.

## Introdução

Esta aula aborda:

- O que são Agentes de IA e quais são os diferentes tipos de agentes?
- Quais casos de uso são mais adequados para Agentes de IA e como eles podem nos ajudar?
- Quais são alguns dos blocos básicos ao projetar Soluções Agentes?

## Objetivos de Aprendizado
Após concluir esta aula, você deverá ser capaz de:

- Compreender os conceitos de Agentes de IA e como eles diferem de outras soluções de IA.
- Aplicar Agentes de IA de forma mais eficiente.
- Projetar soluções agentes de forma produtiva para usuários e clientes.

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Agentes de IA são **sistemas** que permitem que **Modelos de Linguagem de Grande Escala (LLMs)** **executem ações**, ampliando suas capacidades ao fornecer **acesso a ferramentas** e **conhecimento**.

Vamos dividir essa definição em partes menores:

- **Sistema** - É importante pensar nos agentes não apenas como um único componente, mas como um sistema de vários componentes. No nível básico, os componentes de um Agente de IA são:
  - **Ambiente** - O espaço definido onde o Agente de IA está operando. Por exemplo, se tivermos um agente de reserva de viagens, o ambiente pode ser o sistema de reservas de viagens que o agente utiliza para realizar tarefas.
  - **Sensores** - Ambientes possuem informações e fornecem feedback. Agentes de IA utilizam sensores para coletar e interpretar essas informações sobre o estado atual do ambiente. No exemplo do Agente de Reserva de Viagens, o sistema de reservas pode fornecer informações como disponibilidade de hotéis ou preços de voos.
  - **Atuadores** - Após o Agente de IA receber o estado atual do ambiente, para a tarefa em questão, o agente determina qual ação realizar para alterar o ambiente. No exemplo do agente de reserva de viagens, pode ser reservar um quarto disponível para o usuário.

![O que são Agentes de IA?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.br.png)

**Modelos de Linguagem de Grande Escala** - O conceito de agentes existia antes da criação dos LLMs. A vantagem de construir Agentes de IA com LLMs é sua capacidade de interpretar linguagem humana e dados. Essa habilidade permite que os LLMs interpretem informações do ambiente e definam um plano para alterá-lo.

**Executar Ações** - Fora dos sistemas de Agentes de IA, os LLMs são limitados a situações em que a ação é gerar conteúdo ou informações com base no comando do usuário. Dentro dos sistemas de Agentes de IA, os LLMs podem realizar tarefas interpretando o pedido do usuário e utilizando ferramentas disponíveis em seu ambiente.

**Acesso a Ferramentas** - Quais ferramentas o LLM tem acesso é definido por 1) o ambiente em que está operando e 2) o desenvolvedor do Agente de IA. No exemplo do agente de viagens, as ferramentas do agente são limitadas pelas operações disponíveis no sistema de reservas e/ou o desenvolvedor pode limitar o acesso do agente às ferramentas de voos.

**Memória+Conhecimento** - A memória pode ser de curto prazo no contexto da conversa entre o usuário e o agente. A longo prazo, fora das informações fornecidas pelo ambiente, os Agentes de IA também podem recuperar conhecimento de outros sistemas, serviços, ferramentas e até outros agentes. No exemplo do agente de viagens, esse conhecimento pode ser as preferências de viagem do usuário localizadas em um banco de dados de clientes.

### Os diferentes tipos de agentes

Agora que temos uma definição geral de Agentes de IA, vamos analisar alguns tipos específicos de agentes e como eles seriam aplicados a um agente de reserva de viagens.

| **Tipo de Agente**            | **Descrição**                                                                                                                       | **Exemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes de Reflexo Simples**| Executam ações imediatas com base em regras predefinidas.                                                                             | O agente de viagens interpreta o contexto do e-mail e encaminha reclamações de viagem para o atendimento ao cliente.                                                                                                          |
| **Agentes de Reflexo Baseados em Modelo** | Executam ações com base em um modelo do mundo e mudanças nesse modelo.                                                          | O agente de viagens prioriza rotas com mudanças significativas de preço com base no acesso a dados históricos de preços.                                                                                                     |
| **Agentes Baseados em Objetivos** | Criam planos para alcançar objetivos específicos interpretando o objetivo e determinando ações para alcançá-lo.                     | O agente de viagens reserva uma jornada determinando os arranjos necessários (carro, transporte público, voos) do local atual até o destino.                                                                                 |
| **Agentes Baseados em Utilidade** | Consideram preferências e avaliam compensações numericamente para determinar como alcançar objetivos.                              | O agente de viagens maximiza a utilidade ao avaliar conveniência versus custo ao reservar viagens.                                                                                                                           |
| **Agentes de Aprendizado**     | Melhoram ao longo do tempo respondendo ao feedback e ajustando ações de acordo.                                                     | O agente de viagens melhora usando o feedback dos clientes de pesquisas pós-viagem para fazer ajustes em reservas futuras.                                                                                                   |
| **Agentes Hierárquicos**       | Apresentam múltiplos agentes em um sistema hierárquico, com agentes de nível superior dividindo tarefas em subtarefas para agentes de nível inferior completarem. | O agente de viagens cancela uma viagem dividindo a tarefa em subtarefas (por exemplo, cancelar reservas específicas) e fazendo com que agentes de nível inferior as completem, reportando ao agente de nível superior.                                              |
| **Sistemas Multiagentes (MAS)**| Agentes completam tarefas de forma independente, seja cooperativa ou competitiva.                                                   | Cooperativo: Múltiplos agentes reservam serviços específicos de viagem, como hotéis, voos e entretenimento. Competitivo: Múltiplos agentes gerenciam e competem por um calendário compartilhado de reservas de hotel para acomodar clientes no hotel. |

## Quando Usar Agentes de IA

Na seção anterior, usamos o caso de uso do Agente de Viagens para explicar como os diferentes tipos de agentes podem ser usados em diferentes cenários de reserva de viagens. Continuaremos a usar essa aplicação ao longo do curso.

Vamos analisar os tipos de casos de uso para os quais os Agentes de IA são mais adequados:

![Quando usar Agentes de IA?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.br.png)

- **Problemas Abertos** - permitindo que o LLM determine os passos necessários para completar uma tarefa, pois nem sempre é possível codificar isso em um fluxo de trabalho.
- **Processos de Múltiplas Etapas** - tarefas que exigem um nível de complexidade em que o Agente de IA precisa usar ferramentas ou informações em várias etapas, em vez de uma única recuperação.
- **Melhoria ao Longo do Tempo** - tarefas em que o agente pode melhorar ao longo do tempo recebendo feedback de seu ambiente ou usuários para oferecer melhor utilidade.

Abordamos mais considerações sobre o uso de Agentes de IA na aula Construindo Agentes de IA Confiáveis.

## Noções Básicas de Soluções Agentes

### Desenvolvimento de Agentes

O primeiro passo para projetar um sistema de Agente de IA é definir as ferramentas, ações e comportamentos. Neste curso, focamos no uso do **Azure AI Agent Service** para definir nossos Agentes. Ele oferece recursos como:

- Seleção de Modelos Abertos, como OpenAI, Mistral e Llama
- Uso de Dados Licenciados por meio de provedores como Tripadvisor
- Uso de ferramentas padronizadas OpenAPI 3.0

### Padrões Agentes

A comunicação com LLMs é feita por meio de prompts. Dada a natureza semi-autônoma dos Agentes de IA, nem sempre é possível ou necessário reconfigurar manualmente o LLM após uma mudança no ambiente. Usamos **Padrões Agentes** que permitem que o LLM seja configurado em várias etapas de forma mais escalável.

Este curso está dividido em alguns dos padrões agentes populares atuais.

### Frameworks Agentes

Frameworks Agentes permitem que os desenvolvedores implementem padrões agentes por meio de código. Esses frameworks oferecem templates, plugins e ferramentas para melhor colaboração entre Agentes de IA. Esses benefícios proporcionam melhores capacidades de observação e solução de problemas em sistemas de Agentes de IA.

Neste curso, exploraremos o framework AutoGen, baseado em pesquisa, e o framework Agent, pronto para produção, do Semantic Kernel.

## Códigos de Exemplo

- Python: [Framework de Agentes](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Framework de Agentes](./code_samples/01-dotnet-agent-framework.md)

## Tem mais dúvidas sobre Agentes de IA?

Participe do [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para interagir com outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Aula Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Aula

[Explorando Frameworks Agentes](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->