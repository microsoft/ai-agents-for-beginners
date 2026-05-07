[![Introdução aos Agentes de IA](../../../translated_images/pt-PT/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Introdução aos Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso oferece-lhe o conhecimento fundamental — e código funcional real — para começar a construir Agentes de IA do zero.

Venha dizer olá na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> — está cheia de estudantes e construtores de IA que têm todo o gosto em responder a perguntas.

Antes de começarmos a construir, vamos garantir que realmente percebemos o que é um Agente de IA e quando faz sentido usar um.

---

## Introdução

Esta aula cobre:

- O que são Agentes de IA e os diferentes tipos que existem
- Para que tipos de tarefas os Agentes de IA são mais indicados
- Os blocos de construção fundamentais que vai usar ao desenhar uma solução agentic

## Objetivos de Aprendizagem

No final desta aula, deverá ser capaz de:

- Explicar o que é um Agente de IA e como se diferencia de uma solução de IA comum
- Saber quando recorrer a um Agente de IA (e quando não)
- Esboçar um design básico de uma solução agentic para um problema do mundo real

---

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar sobre isto:

> **Agentes de IA são sistemas que permitem que Grandes Modelos de Linguagem (LLMs) realmente *façam coisas* — oferecendo-lhes ferramentas e conhecimento para agir no mundo, não apenas responder a comandos.**

Vamos aprofundar um pouco:

- **Sistema** — Um Agente de IA não é apenas uma coisa. É um conjunto de partes a funcionar em conjunto. Na sua base, cada agente tem três partes:
  - **Ambiente** — O espaço onde o agente opera. Para um agente de reservas de viagens, este seria a própria plataforma de reservas.
  - **Sensores** — Como o agente lê o estado atual do seu ambiente. O nosso agente de viagens pode verificar a disponibilidade de hotéis ou preços de voos.
  - **Atuadores** — Como o agente toma ações. O agente pode reservar um quarto, enviar uma confirmação ou cancelar uma reserva.

![O que são Agentes de IA?](../../../translated_images/pt-PT/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grandes Modelos de Linguagem** — Agentes existiam antes dos LLMs, mas os LLMs são o que torna os agentes modernos tão poderosos. Eles compreendem linguagem natural, raciocinam sobre o contexto e transformam um pedido vago do utilizador num plano concreto de ação.

- **Executar Ações** — Sem um sistema de agente, um LLM apenas gera texto. Dentro de um sistema de agente, o LLM pode realmente *executar* passos — pesquisar numa base de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — As ferramentas que o agente pode usar dependem (1) do ambiente em que está a correr e (2) do que o programador escolheu disponibilizar. Um agente de viagens pode ser capaz de pesquisar voos mas não editar registos de clientes — tudo depende do que configurar.

- **Memória + Conhecimento** — Os agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (uma base de dados de clientes, interações passadas). O agente pode "lembrar-se" que prefere assentos junto à janela.

---

### Os Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está uma divisão dos principais tipos, usando um agente de reservas de viagens como exemplo:

| **Tipo de Agente** | **O que Faz** | **Exemplo de Agente de Viagens** |
|---|---|---|
| **Agentes Reflexos Simples** | Segue regras fixas — sem memória, sem planeamento. | Vê um email de reclamação → envia para o serviço ao cliente. Só isso. |
| **Agentes Reflexos Baseados em Modelo** | Mantém um modelo interno do mundo e atualiza-o conforme as coisas mudam. | Acompanha preços históricos de voos e alerta para rotas que ficam repentinamente caras. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e descobre como alcançá-lo passo a passo. | Reserva uma viagem completa (voos, carro, hotel) desde a localização atual até ao destino. |
| **Agentes Baseados em Utilidade** | Não encontra apenas *uma* solução — encontra a *melhor* ponderando os trade-offs. | Equilibra custo vs. conveniência para encontrar a viagem que melhor se adequa às suas preferências. |
| **Agentes de Aprendizagem** | Melhora com o tempo aprendendo com o feedback. | Ajusta recomendações futuras com base nos resultados de inquéritos pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega a agentes de nível inferior. | Um pedido de "cancelar viagem" é dividido em: cancelar voo, cancelar hotel, cancelar aluguer de carro — cada um gerido por um sub-agente. |
| **Sistemas Multi-Agentes (MAS)** | Vários agentes independentes a trabalhar juntos (ou a competir). | Cooperativo: agentes separadas gerem hotéis, voos e entretenimento. Competitivo: vários agentes competem para preencher quartos de hotel ao melhor preço. |

---

## Quando Usar Agentes de IA

Só porque pode usar um Agente de IA não significa que deva sempre usar. Aqui estão as situações em que os agentes realmente brilham:

![Quando usar Agentes de IA?](../../../translated_images/pt-PT/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abertos** — Quando os passos para resolver um problema não podem ser pré-programados. É necessário que o LLM descubra o caminho dinamicamente.
- **Processos em Múltiplas Etapas** — Tarefas que requerem usar ferramentas em várias interações, não apenas numa pesquisa ou geração única.
- **Melhoria ao Longo do Tempo** — Quando quer que o sistema fique mais inteligente baseado no feedback dos utilizadores ou sinais do ambiente.

Vamos aprofundar quando (e quando *não*) usar Agentes de IA na aula **Construir Agentes de IA Confiáveis** mais adiante no curso.

---

## Noções Básicas de Soluções Agentic

### Desenvolvimento de Agentes

A primeira coisa que faz ao construir um agente é definir *o que ele pode fazer* — as suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Azure AI Agent Service** como a nossa plataforma principal. Ele suporta:

- Modelos abertos como OpenAI, Mistral e Llama
- Dados licenciados de fornecedores como Tripadvisor
- Definições de ferramentas OpenAPI 3.0 padronizadas

### Padrões Agentic

Comunica com LLMs através de prompts. Com agentes, nem sempre pode criar manualmente cada prompt — o agente precisa agir em vários passos. É aqui que entram os **Padrões Agentic**. São estratégias reutilizáveis para promover e orquestrar LLMs de forma mais escalável e fiável.

Este curso é estruturado em torno dos padrões agentic mais comuns e úteis.

### Frameworks Agentic

Frameworks Agentic dão aos programadores templates prontos, ferramentas e infraestrutura para construir agentes. Facilitam:

- Ligação de ferramentas e capacidades
- Observação do que o agente está a fazer (e depuração de erros)
- Colaboração entre múltiplos agentes

Neste curso, focamo-nos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Pronto para ver isto em ação? Aqui estão os exemplos de código para esta aula:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Perguntas?

Junte-se ao [Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) para conectar-se com outros estudantes, participar em horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA pela comunidade.

---

## Aula Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Aula

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, é recomendada a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou más interpretações decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->