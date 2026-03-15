[![Intro to AI Agents](../../../translated_images/pt-PT/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para ver o vídeo desta lição)_


# Introdução aos Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso "Agentes de IA para Iniciantes"! Este curso oferece conhecimentos fundamentais e exemplos práticos para a construção de Agentes de IA.

Junte-se à <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Discord Azure AI</a> para conhecer outros aprendizes e Construtores de Agentes de IA e esclarecer quaisquer dúvidas que tenha sobre este curso.

Para começar este curso, iniciamos por compreender melhor o que são Agentes de IA e como podemos usá-los nas aplicações e fluxos de trabalho que construímos.

## Introdução

Esta lição abrange:

- O que são Agentes de IA e quais os diferentes tipos de agentes?
- Quais os casos de uso mais adequados para Agentes de IA e como podem ajudar-nos?
- Quais os blocos básicos na concepção de Soluções Agentes?

## Objetivos de Aprendizagem
Após concluir esta lição, deverá ser capaz de:

- Compreender os conceitos dos Agentes de IA e como eles diferem de outras soluções de IA.
- Aplicar Agentes de IA de forma mais eficiente.
- Conceber soluções Agentes produtivamente para utilizadores e clientes.

## Definição de Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Agentes de IA são **sistemas** que permitem a **Modelos de Linguagem de Grande Escala (LLMs)** **executar ações** ao ampliar as suas capacidades, dando aos LLMs **acesso a ferramentas** e **conhecimento**.

Vamos dividir esta definição em partes mais pequenas:

- **Sistema** – É importante pensar nos agentes não apenas como um componente único, mas como um sistema composto por muitos componentes. No nível básico, os componentes de um Agente de IA são:
  - **Ambiente** – O espaço definido onde o Agente de IA opera. Por exemplo, se tivermos um agente de reserva de viagens, o ambiente pode ser o sistema de reservas de viagens que o agente usa para completar tarefas.
  - **Sensores** – Os ambientes têm informação e fornecem feedback. Os Agentes de IA usam sensores para recolher e interpretar esta informação sobre o estado atual do ambiente. No exemplo do Agente de Reserva de Viagens, o sistema de reservas pode fornecer informações como disponibilidade de hotéis ou preços de voos.
  - **Atuadores** – Depois do Agente de IA receber o estado atual do ambiente, para a tarefa atual o agente determina qual ação executar para alterar o ambiente. Para o agente de reserva de viagens, poderá ser reservar um quarto disponível para o utilizador.

![What Are AI Agents?](../../../translated_images/pt-PT/what-are-ai-agents.1ec8c4d548af601a.webp)

**Modelos de Linguagem de Grande Escala** – O conceito de agentes existia antes da criação dos LLMs. A vantagem de construir Agentes de IA com os LLMs é a sua capacidade de interpretar a linguagem humana e dados. Esta capacidade permite aos LLMs interpretar informação ambiental e definir um plano para alterar o ambiente.

**Executar Ações** – Fora dos sistemas de Agentes de IA, os LLMs são limitados a situações onde a ação é gerar conteúdo ou informação com base na indicação do utilizador. Dentro dos sistemas de Agentes de IA, os LLMs podem realizar tarefas interpretando o pedido do utilizador e usando ferramentas disponíveis no seu ambiente.

**Acesso a Ferramentas** – As ferramentas às quais o LLM tem acesso são definidas por 1) o ambiente onde opera e 2) o desenvolvedor do Agente de IA. Para o nosso exemplo do agente de viagens, as ferramentas do agente são limitadas pelas operações disponíveis no sistema de reservas, e/ou o desenvolvedor pode limitar o acesso do agente a ferramentas apenas para voos.

**Memória+Conhecimento** – A memória pode ser de curto prazo no contexto da conversa entre o utilizador e o agente. A longo prazo, para além da informação fornecida pelo ambiente, os Agentes de IA podem também recuperar conhecimento de outros sistemas, serviços, ferramentas e até outros agentes. No exemplo do agente de viagens, este conhecimento pode ser o perfil das preferências de viagem do utilizador localizado numa base de dados de clientes.

### Os diferentes tipos de agentes

Agora que temos uma definição geral de Agentes de IA, vejamos alguns tipos específicos de agentes e como seriam aplicados a um agente de reserva de viagens.

| **Tipo de Agente**                | **Descrição**                                                                                                                       | **Exemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes Reflexos Simples**      | Executam ações imediatas com base em regras predefinidas.                                                                                  | O agente de viagens interpreta o contexto do email e encaminha reclamações sobre viagens para o serviço ao cliente.                                                                                                                          |
| **Agentes Reflexos Baseados em Modelo** | Executam ações com base num modelo do mundo e alterações a esse modelo.                                                              | O agente de viagens prioriza rotas com alterações significativas de preço com base em dados históricos de preços.                                                                                                             |
| **Agentes Baseados em Objetivos**         | Criam planos para alcançar objetivos específicos ao interpretar o objetivo e determinar ações para o atingir.                                  | O agente de viagens reserva uma jornada determinando as necessidades de transporte (carro, transporte público, voos) desde a localização atual até ao destino.                                                                                |
| **Agentes Baseados em Utilidade**      | Consideram preferências e pesam trade-offs numericamente para determinar como atingir os objetivos.                                               | O agente de viagens maximiza a utilidade ponderando conveniência vs. custo ao reservar a viagem.                                                                                                                                          |
| **Agentes Aprendizes**           | Melhoram ao longo do tempo respondendo a feedback e ajustando ações em conformidade.                                                        | O agente de viagens melhora ao usar o feedback dos clientes de inquéritos pós-viagem para ajustar futuras reservas.                                                                                                               |
| **Agentes Hierárquicos**       | Funcionam com múltiplos agentes num sistema em camadas, com agentes de nível superior a dividir tarefas em subtarefas para agentes de nível inferior completarem. | O agente de viagens cancela uma viagem ao dividir a tarefa em subtarefas (por exemplo, cancelar reservas específicas) e tendo agentes de nível inferior a completá-las, reportando ao agente de nível superior.                                     |
| **Sistemas Multi-Agente (MAS)** | Agentes completam tarefas independentemente, cooperando ou competindo.                                                           | Cooperativo: Vários agentes reservam serviços de viagem específicos como hotéis, voos e entretenimento. Competitivo: Vários agentes gerem e competem por um calendário de reservas partilhado de um hotel para reservar clientes no hotel. |

## Quando Usar Agentes de IA

Na seção anterior, usamos o caso de uso do Agente de Viagens para explicar como os diferentes tipos de agentes podem ser usados em diferentes cenários de reservas de viagens. Continuaremos a usar esta aplicação ao longo do curso.

Vamos analisar os tipos de casos de uso onde os Agentes de IA são mais indicados:

![When to use AI Agents?](../../../translated_images/pt-PT/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemas Abertos** – permitindo ao LLM determinar os passos necessários para concluir uma tarefa porque nem sempre pode ser codificado rigidamente num fluxo de trabalho.
- **Processos em múltiplas etapas** – tarefas que requerem um nível de complexidade onde o Agente de IA precisa usar ferramentas ou informação ao longo de múltiplas interações em vez de numa única recuperação.  
- **Melhoria ao Longo do Tempo** – tarefas onde o agente pode melhorar ao longo do tempo recebendo feedback quer do ambiente quer dos utilizadores para proporcionar melhor utilidade.

Abordamos mais considerações sobre o uso de Agentes de IA na lição Construindo Agentes de IA Confiáveis.

## Noções Básicas das Soluções Agentes

### Desenvolvimento do Agente

O primeiro passo na conceção de um sistema de Agente de IA é definir as ferramentas, ações e comportamentos. Neste curso, focamo-nos no uso do **Azure AI Agent Service** para definir os nossos Agentes. Oferece funcionalidades como:

- Seleção de Modelos Abertos como OpenAI, Mistral, e Llama
- Uso de Dados Licenciados através de fornecedores como Tripadvisor
- Uso de ferramentas padronizadas OpenAPI 3.0

### Padrões Agentes

A comunicação com LLMs é feita através de prompts. Dada a natureza semi-autónoma dos Agentes de IA, nem sempre é possível ou necessário reemitir prompts ao LLM manualmente após uma alteração no ambiente. Utilizamos **Padrões Agentes** que nos permitem solicitar ao LLM ao longo de múltiplas etapas de forma mais escalável.

Este curso está dividido em alguns dos padrões agentes atuais e populares.

### Frameworks Agentes

Frameworks agentes permitem aos desenvolvedores implementar padrões agentes por código. Estes frameworks oferecem templates, plugins e ferramentas para melhor colaboração entre Agentes de IA. Estes benefícios proporcionam capacidades para melhor observabilidade e resolução de problemas em sistemas de Agentes de IA.

Neste curso, exploraremos o Microsoft Agent Framework (MAF) para construir agentes de IA prontos para produção.

## Exemplos de Código

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre Agentes de IA?

Participe no [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, assistir a sessões de esclarecimento e obter respostas às suas questões sobre Agentes de IA.

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentes](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->