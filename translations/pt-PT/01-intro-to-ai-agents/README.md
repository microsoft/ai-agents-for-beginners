[![Intro to AI Agents](../../../translated_images/pt-PT/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Introdução aos Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso oferece-lhe o conhecimento fundamental — e código funcional real — para começar a construir Agentes de IA do zero.

Venha dizer olá na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Discord Azure AI</a> — está cheia de aprendizes e construtores de IA que têm prazer em responder a perguntas.

Antes de começar a construir, vamos garantir que realmente entendemos o que é um Agente de IA e quando faz sentido usar um.

---

## Introdução

Esta lição cobre:

- O que são Agentes de IA e os diferentes tipos que existem
- Que tipos de tarefas os Agentes de IA são mais indicados para executar
- Os blocos de construção principais que usará ao projetar uma solução agentiva

## Objetivos de Aprendizagem

No final desta lição, deverá ser capaz de:

- Explicar o que é um Agente de IA e como ele é diferente de uma solução de IA regular
- Saber quando recorrer a um Agente de IA (e quando não recorrer)
- Esboçar um design básico de solução agentiva para um problema do mundo real

---

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar nisso:

> **Agentes de IA são sistemas que permitem que Modelos de Linguagem Grande (LLMs) realmente *façam coisas* — dando-lhes ferramentas e conhecimento para agir no mundo, não apenas responder a comandos.**

Vamos detalhar um pouco mais:

- **Sistema** — Um Agente de IA não é apenas uma coisa. É uma coleção de partes a trabalhar em conjunto. No seu núcleo, todo agente tem três componentes:
  - **Ambiente** — O espaço onde o agente opera. Para um agente de reservas de viagens, este seria a própria plataforma de reservas.
  - **Sensores** — Como o agente lê o estado corrente do seu ambiente. O nosso agente de viagens pode verificar a disponibilidade de hotéis ou preços de voos.
  - **Atuadores** — Como o agente toma ações. O agente de viagens pode reservar um quarto, enviar uma confirmação ou cancelar uma reserva.

![What Are AI Agents?](../../../translated_images/pt-PT/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelos de Linguagem Grande** — Os agentes existiam antes dos LLMs, mas os LLMs são o que torna os agentes modernos tão poderosos. Eles podem compreender linguagem natural, raciocinar sobre contexto e transformar um pedido vago do utilizador num plano de ação concreto.

- **Executar Ações** — Sem um sistema de agente, um LLM apenas gera texto. Dentro de um sistema de agente, o LLM pode realmente *executar* passos — pesquisar numa base de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — As ferramentas que o agente pode usar dependem (1) do ambiente onde está a correr e (2) do que o programador escolheu disponibilizar. Um agente de viagens poderá pesquisar voos mas não editar registos de clientes — tudo depende do que ligar.

- **Memória + Conhecimento** — Os agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (uma base de dados de clientes, interações passadas). O agente de viagens pode "lembrar-se" de que prefere lugares junto à janela.

---

### Os Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está uma divisão dos principais tipos, usando um agente de reservas de viagens como exemplo:

| **Tipo de Agente** | **O Que Faz** | **Exemplo de Agente de Viagens** |
|---|---|---|
| **Agentes Reflexos Simples** | Seguem regras codificadas — sem memória, sem planeamento. | Vêem um e-mail de reclamação → encaminham para o serviço de apoio ao cliente. Só isso. |
| **Agentes Reflexos Baseados em Modelos** | Mantêm um modelo interno do mundo e atualizam-no conforme as coisas mudam. | Acompanha preços históricos de voos e sinaliza rotas que ficarem subitamente caras. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e calcula como alcançá-lo passo a passo. | Reserva uma viagem completa (voos, carro, hotel) desde a sua localização até ao destino final. |
| **Agentes Baseados em Utilidade** | Não encontra apenas *uma* solução — encontra a *melhor* ao pesar compensações. | Equilibra custo vs. conveniência para encontrar a viagem que melhor corresponde às suas preferências. |
| **Agentes de Aprendizagem** | Melhora ao longo do tempo aprendendo com o feedback. | Ajusta recomendações futuras de reservas com base nos resultados de inquéritos pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega para agentes de nível inferior. | Um pedido de "cancelar viagem" divide-se em: cancelar voo, cancelar hotel, cancelar aluguer de carro — cada um tratado por um sub-agente. |
| **Sistemas Multi-Agentes (MAS)** | Múltiplos agentes independentes a trabalhar juntos (ou em competição). | Cooperativo: agentes separados tratam de hotéis, voos e entretenimento. Competitivo: múltiplos agentes competem para preencher quartos de hotel ao melhor preço. |

---

## Quando Usar Agentes de IA

Só porque pode usar um Agente de IA não significa que deva sempre fazê-lo. Aqui estão as situações onde os agentes realmente se destacam:

![When to use AI Agents?](../../../translated_images/pt-PT/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas em Aberto** — Quando os passos para resolver um problema não podem ser pré-programados. Precisa que o LLM descubra o caminho dinamicamente.
- **Processos de Vários Passos** — Tarefas que exigem usar ferramentas durante várias etapas, não apenas uma pesquisa ou geração simples.
- **Melhoria ao Longo do Tempo** — Quando quer que o sistema fique mais inteligente com base no feedback do utilizador ou sinais do ambiente.

Vamos aprofundar quando (e quando *não*) usar Agentes de IA na lição **Construindo Agentes de IA Confiáveis** mais adiante neste curso.

---

## Noções Básicas de Soluções Agentivas

### Desenvolvimento de Agentes

A primeira coisa que faz ao construir um agente é definir *o que ele pode fazer* — as suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Azure AI Agent Service** como nossa principal plataforma. Ele suporta:

- Modelos de fornecedores como OpenAI, Mistral e Meta (Llama)
- Dados licenciados de fornecedores como Tripadvisor
- Definições padronizadas de ferramentas OpenAPI 3.0

### Padrões Agentivos

Comunica com LLMs através de prompts. Com agentes, não pode sempre criar manualmente cada prompt — o agente precisa de agir em vários passos. É aqui que entram os **Padrões Agentivos**. São estratégias reutilizáveis para promptar e orquestrar LLMs de forma mais escalável e fiável.

Este curso está estruturado em torno dos padrões agentivos mais comuns e úteis.

### Frameworks Agentivos

Frameworks Agentivos dão aos programadores templates prontos, ferramentas e infraestrutura para construir agentes. Facilitam:

- Ligar ferramentas e capacidades
- Observar o que o agente está a fazer (e depurar quando algo corre mal)
- Colaborar entre múltiplos agentes

Neste curso, focamo-nos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Quer ver em ação? Aqui estão os exemplos de código para esta lição:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Perguntas?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar em horas de escritório e obter respostas às suas perguntas sobre Agentes de IA da comunidade.

---

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentivos](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->