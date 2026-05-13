[![Intro to AI Agents](../../../translated_images/pt-BR/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Introdução a Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso oferece o conhecimento fundamental — e código funcionando de verdade — para começar a construir Agentes de IA do zero.

Venha dizer oi na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> — está cheia de aprendizes e construtores de IA que têm prazer em responder perguntas.

Antes de começarmos a construir, vamos garantir que realmente entendemos o que é um Agente de IA *e* quando faz sentido usar um.

---

## Introdução

Esta aula aborda:

- O que são Agentes de IA, e os diferentes tipos que existem
- Para quais tipos de tarefas os Agentes de IA são mais indicados
- Os blocos principais que você usará ao projetar uma solução agentic

## Objetivos de Aprendizagem

Ao final desta aula, você deverá ser capaz de:

- Explicar o que é um Agente de IA e como ele difere de uma solução de IA comum
- Saber quando usar um Agente de IA (e quando não usar)
- Esboçar um design básico de solução agentic para um problema do mundo real

---

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar:

> **Agentes de IA são sistemas que permitem que Grandes Modelos de Linguagem (LLMs) realmente *façam coisas* — dando a eles ferramentas e conhecimento para agir no mundo, não apenas responder a comandos.**

Vamos detalhar um pouco:

- **Sistema** — Um Agente de IA não é apenas uma coisa. É uma coleção de partes que trabalham juntas. Na sua essência, todo agente tem três peças:
  - **Ambiente** — O espaço no qual o agente atua. Para um agente de reservas de viagem, seria a própria plataforma de reservas.
  - **Sensores** — Como o agente lê o estado atual do ambiente. Nosso agente de viagem pode verificar disponibilidade de hotéis ou preços de voos.
  - ** Atuadores** — Como o agente executa ações. O agente de viagens pode reservar um quarto, enviar uma confirmação ou cancelar uma reserva.

![What Are AI Agents?](../../../translated_images/pt-BR/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grandes Modelos de Linguagem** — Agentes existiam antes dos LLMs, mas são os LLMs que tornam os agentes modernos tão poderosos. Eles podem entender linguagem natural, raciocinar sobre o contexto e transformar uma solicitação vaga do usuário em um plano concreto de ação.

- **Executar Ações** — Sem um sistema de agente, um LLM apenas gera texto. Dentro de um sistema agente, o LLM pode realmente *executar* passos — pesquisar em banco de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — Quais ferramentas o agente pode usar depende de (1) o ambiente onde está rodando e (2) o que o desenvolvedor escolheu fornecer. Um agente de viagem pode ser capaz de pesquisar voos, mas não editar registros de clientes — tudo depende do que você conectar.

- **Memória + Conhecimento** — Agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (um banco de dados de clientes, interações anteriores). O agente de viagem pode "lembrar" que você prefere assentos na janela.

---

### Os Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está um resumo dos principais tipos, usando um agente de reservas de viagem como exemplo:

| **Tipo de Agente** | **O Que Faz** | **Exemplo do Agente de Viagem** |
|---|---|---|
| **Agentes Reflexos Simples** | Seguem regras codificadas — sem memória, sem planejamento. | Vê um e-mail de reclamação → encaminha para o serviço ao cliente. Só isso. |
| **Agentes Reflexos Baseados em Modelo** | Mantém um modelo interno do mundo e atualiza conforme as coisas mudam. | Acompanha preços históricos de voos e sinaliza rotas que ficaram caras de repente. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e descobre como alcançá-lo passo a passo. | Reserva uma viagem completa (voos, carro, hotel) partindo da sua localização para o destino. |
| **Agentes Baseados em Utilidade** | Não encontra apenas *uma* solução — encontra a *melhor* ao pesar vantagens e desvantagens. | Equilibra custo versus conveniência para achar a viagem que melhor corresponde às suas preferências. |
| **Agentes de Aprendizado** | Melhora com o tempo aprendendo com feedback. | Ajusta recomendações futuras de reserva com base em resultados de pesquisas pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega para agentes de nível inferior. | Um pedido de "cancelar viagem" se divide em: cancelar voo, cancelar hotel, cancelar aluguel de carro — cada um tratado por um subagente. |
| **Sistemas Multiagentes (MAS)** | Vários agentes independentes trabalham juntos (ou competem). | Cooperativo: agentes separados cuidam de hotéis, voos e entretenimento. Competitivo: agentes competem para preencher quartos de hotel ao melhor preço. |

---

## Quando Usar Agentes de IA

Só porque você *pode* usar um Agente de IA não significa que sempre *deva*. Aqui estão as situações em que os agentes realmente se destacam:

![When to use AI Agents?](../../../translated_images/pt-BR/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abertos** — Quando os passos para resolver um problema não podem ser pré-programados. Você precisa que o LLM descubra o caminho dinamicamente.
- **Processos Multi-Etapas** — Tarefas que exigem usar ferramentas ao longo de várias etapas, não apenas uma consulta ou geração única.
- **Melhoria ao Longo do Tempo** — Quando você quer que o sistema fique mais inteligente com base no feedback do usuário ou sinais do ambiente.

Exploraremos mais profundamente quando (e quando *não*) usar Agentes de IA na aula **Construindo Agentes de IA Confiáveis**, mais adiante no curso.

---

## Noções Básicas de Soluções Agentic

### Desenvolvimento de Agentes

A primeira coisa que você faz ao construir um agente é definir *o que ele pode fazer* — suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Azure AI Agent Service** como nossa plataforma principal. Ele suporta:

- Modelos de provedores como OpenAI, Mistral e Meta (Llama)
- Dados licenciados de provedores como Tripadvisor
- Definições padronizadas de ferramentas OpenAPI 3.0

### Padrões Agentic

Você se comunica com LLMs por meio de prompts. Com agentes, nem sempre dá para elaborar cada prompt manualmente — o agente precisa agir em muitos passos. É aí que entram os **Padrões Agentic**. São estratégias reutilizáveis para promptar e orquestrar LLMs de forma mais escalável e confiável.

Este curso é estruturado em torno dos padrões agentic mais comuns e úteis.

### Frameworks Agentic

Frameworks Agentic oferecem aos desenvolvedores modelos prontos, ferramentas e infraestrutura para construir agentes. Facilitam:

- Conectar ferramentas e capacidades
- Observar o que o agente está fazendo (e depurar quando algo dá errado)
- Colaborar entre vários agentes

Neste curso, focamos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Pronto para ver na prática? Aqui estão os exemplos de código para esta aula:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Perguntas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horas de atendimento e esclarecer suas dúvidas sobre Agentes de IA com a comunidade.

---

## Aula Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Aula

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->