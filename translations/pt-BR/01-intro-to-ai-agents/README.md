[![Introdução aos Agentes de IA](../../../translated_images/pt-BR/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Introdução a Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso oferece o conhecimento fundamental — e código funcional real — para começar a construir Agentes de IA do zero.

Venha dizer oi na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Azure AI no Discord</a> — cheia de aprendizes e construtores de IA que ficam felizes em responder perguntas.

Antes de começarmos a construir, vamos garantir que entendemos realmente o que é um Agente de IA *e* quando faz sentido usar um.

---

## Introdução

Esta lição cobre:

- O que são Agentes de IA, e os diferentes tipos que existem
- Para quais tipos de tarefas os Agentes de IA são mais indicados
- Os blocos básicos que você usará ao projetar uma solução Agentic

## Objetivos de Aprendizagem

Ao final desta lição, você deve ser capaz de:

- Explicar o que é um Agente de IA e como ele difere de uma solução de IA comum
- Saber quando usar um Agente de IA (e quando não usar)
- Esboçar um design básico de solução Agentic para um problema do mundo real

---

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar sobre isso:

> **Agentes de IA são sistemas que permitem que Grandes Modelos de Linguagem (LLMs) realmente *façam coisas* — dando-lhes ferramentas e conhecimento para agir no mundo, e não apenas responder a comandos.**

Vamos detalhar um pouco:

- **Sistema** — Um Agente de IA não é só uma coisa. É uma coleção de partes trabalhando juntas. No seu núcleo, cada agente tem três componentes:
  - **Ambiente** — O espaço onde o agente atua. Para um agente de reserva de viagens, seria a própria plataforma de reservas.
  - **Sensores** — Como o agente lê o estado atual do seu ambiente. Nosso agente de viagens pode verificar disponibilidade de hotéis ou preços de voos.
  - **Atuadores** — Como o agente age. O agente pode reservar um quarto, enviar uma confirmação ou cancelar uma reserva.

![O que são Agentes de IA?](../../../translated_images/pt-BR/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grandes Modelos de Linguagem** — Agentes existiam antes dos LLMs, mas os LLMs são o que tornam os agentes modernos tão poderosos. Eles entendem linguagem natural, raciocinam sobre contexto, e transformam um pedido vago em um plano concreto.

- **Executar Ações** — Sem um sistema agente, um LLM apenas gera texto. Num sistema de agente, o LLM pode realmente *executar* etapas — pesquisar um banco de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — Quais ferramentas o agente pode usar depende (1) do ambiente em que está rodando e (2) do que o desenvolvedor escolheu fornecer. Um agente de viagens pode buscar voos, mas não editar registros de clientes — depende do que você conecta.

- **Memória + Conhecimento** — Agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (banco de dados de clientes, interações passadas). O agente de viagens pode "lembrar" que você prefere assentos na janela.

---

### Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está um resumo dos principais tipos, usando como exemplo um agente de reserva de viagens:

| **Tipo de Agente** | **O que Faz** | **Exemplo de Agente de Viagens** |
|---|---|---|
| **Agentes Reflexo Simples** | Seguem regras rígidas codificadas — sem memória, sem planejamento. | Veja um email de reclamação → encaminha para o serviço ao cliente. Só isso. |
| **Agentes Reflexo Baseados em Modelo** | Mantém um modelo interno do mundo e o atualiza conforme as coisas mudam. | Acompanha preços históricos de voos e alerta rotas que ficaram caras de repente. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e descobre como alcançá-lo passo a passo. | Reserva uma viagem completa (voos, carro, hotel) partindo da sua localização atual para te levar ao destino. |
| **Agentes Baseados em Utilidade** | Não encontra só *uma* solução — encontra a *melhor* ao pesar compensações. | Equilibra custo vs conveniência para achar a viagem que melhor se encaixa nas suas preferências. |
| **Agentes de Aprendizado** | Melhora com o tempo aprendendo com feedback. | Ajusta recomendações futuras de reserva baseado em resultados de pesquisas pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega a agentes de nível inferior. | Um pedido de "cancelar viagem" é dividido em: cancelar voo, cancelar hotel, cancelar aluguel de carro — cada um tratado por um sub-agente. |
| **Sistemas Multi-Agentes (MAS)** | Múltiplos agentes independentes trabalhando juntos (ou competindo). | Cooperativo: agentes separados cuidam de hotéis, voos e entretenimento. Competitivo: múltiplos agentes competem para preencher quartos de hotel pelo melhor preço. |

---

## Quando Usar Agentes de IA

Só porque você *pode* usar um Agente de IA não significa que sempre *deve*. Aqui estão as situações onde agentes realmente brilham:

![Quando usar Agentes de IA?](../../../translated_images/pt-BR/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas Abertos** — Quando os passos para resolver um problema não podem ser pré-programados. Você precisa que o LLM descubra o caminho dinamicamente.
- **Processos de Múltiplas Etapas** — Tarefas que requerem usar ferramentas em vários passos, não apenas uma consulta ou geração única.
- **Melhoria ao Longo do Tempo** — Quando você quer que o sistema fique mais inteligente com base no feedback do usuário ou sinais do ambiente.

Vamos explorar mais profundamente quando (e quando *não*) usar Agentes de IA na lição **Construindo Agentes de IA Confiáveis** mais adiante no curso.

---

## Noções Básicas de Soluções Agentic

### Desenvolvimento de Agentes

A primeira coisa que você faz ao construir um agente é definir *o que ele pode fazer* — suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Microsoft Foundry Agent Service** como nossa plataforma principal. Ele suporta:

- Modelos de provedores como OpenAI, Mistral e Meta (Llama)
- Dados licenciados de provedores como Tripadvisor
- Definições de ferramentas padronizadas OpenAPI 3.0

### Padrões Agentic

Você se comunica com LLMs através de prompts. Com agentes, você não pode sempre criar manualmente cada prompt — o agente precisa agir ao longo de muitos passos. É aí que entram os **Padrões Agentic**. São estratégias reutilizáveis para solicitar e orquestrar LLMs de forma mais escalável e confiável.

Este curso é estruturado em torno dos padrões agentic mais comuns e úteis.

### Frameworks Agentic

Frameworks Agentic dão aos desenvolvedores templates, ferramentas e infraestrutura prontas para construir agentes. Eles facilitam:

- Conectar ferramentas e capacidades
- Observar o que o agente está fazendo (e depurar quando dá errado)
- Colaborar entre múltiplos agentes

Neste curso, focamos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Pronto para ver em ação? Aqui estão os exemplos de código para esta lição:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Dúvidas?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para se conectar com outros aprendizes, participar de horas de atendimento e tirar suas dúvidas sobre Agentes de IA com a comunidade.


---

## Teste Rápido Deste Agente (Opcional)

Quando você aprender a implantar agentes na [Lição 16](../16-deploying-scalable-agents/README.md), poderá adicionar uma verificação rápida de saúde pós-implantação para o `TravelAgent` desta lição com o catálogo pronto [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Veja [`tests/README.md`](../tests/README.md) para instruções de execução.

---

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->