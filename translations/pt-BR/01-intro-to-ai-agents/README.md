[![Intro to AI Agents](../../../translated_images/pt-BR/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Introdução a Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso oferece o conhecimento fundamental — e código funcional real — para começar a construir agentes de IA do zero.

Venha dizer oi na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade do Discord Azure AI</a> — está cheia de aprendizes e construtores de IA felizes em responder perguntas.

Antes de começarmos a construir, vamos garantir que realmente entendemos o que é um agente de IA e quando faz sentido usar um.

---

## Introdução

Esta lição cobre:

- O que são agentes de IA e os diferentes tipos que existem
- Para quais tipos de tarefas os agentes de IA são mais indicados
- Os blocos de construção principais que você usará ao projetar uma solução agentic

## Objetivos de Aprendizagem

Ao final desta lição, você deverá ser capaz de:

- Explicar o que é um agente de IA e como ele é diferente de uma solução de IA comum
- Saber quando recorrer a um agente de IA (e quando não)
- Esboçar um design básico de solução agentic para um problema do mundo real

---

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar sobre isso:

> **Agentes de IA são sistemas que permitem que Grandes Modelos de Linguagem (LLMs) realmente *façam coisas* — dando a eles ferramentas e conhecimento para agir no mundo, não apenas responder a prompts.**

Vamos detalhar um pouco:

- **Sistema** — Um agente de IA não é apenas uma coisa. É uma coleção de partes que trabalham juntas. No seu núcleo, todo agente tem três peças:
  - **Ambiente** — O espaço em que o agente trabalha. Para um agente de reservas de viagem, esse seria o próprio plataforma de reservas.
  - **Sensores** — Como o agente lê o estado atual do seu ambiente. Nosso agente de viagem pode checar a disponibilidade de hotéis ou preços de voos.
  - **Atuadores** — Como o agente executa ações. O agente de viagem pode reservar um quarto, enviar uma confirmação ou cancelar uma reserva.

![What Are AI Agents?](../../../translated_images/pt-BR/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grandes Modelos de Linguagem** — Agentes existiam antes dos LLMs, mas os LLMs são o que torna os agentes modernos tão poderosos. Eles podem entender linguagem natural, raciocinar sobre o contexto e transformar um pedido vago do usuário em um plano concreto de ação.

- **Executar Ações** — Sem um sistema de agente, um LLM apenas gera texto. Dentro de um sistema de agente, o LLM pode realmente *executar* passos — pesquisar um banco de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — Quais ferramentas o agente pode usar depende de (1) o ambiente onde está rodando e (2) o que o desenvolvedor escolheu fornecer. Um agente de viagem pode ser capaz de pesquisar voos, mas não editar registros de clientes — tudo depende do que você conecta.

- **Memória + Conhecimento** — Agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (um banco de dados de clientes, interações passadas). O agente de viagem pode "lembrar" que você prefere assentos na janela.

---

### Os Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está uma divisão dos principais tipos, usando um agente de reservas de viagem como exemplo:

| **Tipo de Agente** | **O que Faz** | **Exemplo de Agente de Viagem** |
|---|---|---|
| **Agentes Reflexos Simples** | Seguem regras fixas — sem memória, sem planejamento. | Vê um e-mail de reclamação → encaminha para o atendimento ao cliente. Só isso. |
| **Agentes Reflexos Baseados em Modelo** | Mantém um modelo interno do mundo e o atualiza conforme as coisas mudam. | Rastreia preços históricos de voos e sinaliza rotas que ficaram subitamente caras. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e descobre passo a passo como alcançá-lo. | Reserva uma viagem completa (voos, carro, hotel) desde sua localização atual para chegar ao destino. |
| **Agentes Baseados em Utilidade** | Não apenas encontra *uma* solução — encontra a *melhor* ao pesar trade-offs. | Equilibra custo vs. conveniência para achar a viagem que melhor atende suas preferências. |
| **Agentes de Aprendizado** | Melhora ao longo do tempo aprendendo com feedback. | Ajusta recomendações futuras de reserva com base em resultados de pesquisas pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega a agentes de nível inferior. | Um pedido de "cancelar viagem" é dividido em: cancelar voo, cancelar hotel, cancelar aluguel de carro — cada um tratado por um sub-agente. |
| **Sistemas Multi-Agentes (MAS)** | Múltiplos agentes independentes trabalhando juntos (ou competindo). | Cooperativo: agentes separados cuidam de hotéis, voos e entretenimento. Competitivo: múltiplos agentes competem para preencher quartos de hotel pelo melhor preço. |

---

## Quando Usar Agentes de IA

Só porque você *pode* usar um agente de IA não significa que sempre *deva*. Aqui estão as situações em que agentes realmente brilham:

![When to use AI Agents?](../../../translated_images/pt-BR/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abertos** — Quando os passos para resolver um problema não podem ser pré-programados. Você precisa que o LLM descubra o caminho dinamicamente.
- **Processos em Vários Passos** — Tarefas que requerem usar ferramentas em várias etapas, não apenas uma consulta ou geração única.
- **Melhoria ao Longo do Tempo** — Quando você quer que o sistema fique mais inteligente com base no feedback do usuário ou sinais do ambiente.

Vamos aprofundar quando (e quando *não*) usar agentes de IA na lição **Construindo Agentes de IA Confiáveis** mais adiante no curso.

---

## Noções Básicas de Soluções Agentic

### Desenvolvimento de Agentes

A primeira coisa a fazer ao construir um agente é definir *o que ele pode fazer* — suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Azure AI Agent Service** como nossa principal plataforma. Ele suporta:

- Modelos abertos como OpenAI, Mistral e Llama
- Dados licenciados de provedores como Tripadvisor
- Definições padronizadas de ferramentas OpenAPI 3.0

### Padrões Agentic

Você se comunica com LLMs por meio de prompts. Com agentes, nem sempre é possível criar manualmente cada prompt — o agente precisa agir em vários passos. É aí que entram os **Padrões Agentic**. Eles são estratégias reutilizáveis para prompting e orquestração de LLMs de maneira mais escalável e confiável.

Este curso é estruturado em torno dos padrões agentic mais comuns e úteis.

### Frameworks Agentic

Frameworks agentic dão aos desenvolvedores modelos prontos, ferramentas e infraestrutura para construir agentes. Eles facilitam:

- Conectar ferramentas e capacidades
- Observar o que o agente está fazendo (e depurar quando algo dá errado)
- Colaborar entre múltiplos agentes

Neste curso, focamos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Pronto para ver em ação? Aqui estão os exemplos de código para esta lição:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Perguntas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre agentes de IA com a comunidade.

---

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->