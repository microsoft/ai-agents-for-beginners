[![Introdução aos Agentes de IA](../../../translated_images/pt-PT/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Introdução aos Agentes de IA e Casos de Uso de Agentes

Bem-vindo ao curso **Agentes de IA para Iniciantes**! Este curso dá-lhe o conhecimento fundamental — e código funcional real — para começar a construir Agentes de IA a partir do zero.

Venha cumprimentar-nos na <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidade Discord Azure AI</a> — está cheia de aprendizes e construtores de IA felizes por responder a perguntas.

Antes de começarmos a construir, vamos garantir que realmente compreendemos o que é um Agente de IA *e* quando faz sentido usar um.

---

## Introdução

Esta lição cobre:

- O que são Agentes de IA, e os diferentes tipos que existem
- Que tipos de tarefas os Agentes de IA executam melhor
- Os blocos básicos que usará ao desenhar uma solução Agentic

## Objetivos de Aprendizagem

No final desta lição, deverá ser capaz de:

- Explicar o que é um Agente de IA e como é diferente de uma solução de IA regular
- Saber quando usar um Agente de IA (e quando não usar)
- Esboçar um design básico de solução Agentic para um problema do mundo real

---

## Definição de Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Aqui está uma forma simples de pensar nisso:

> **Agentes de IA são sistemas que permitem que Modelos de Linguagem Grande (LLMs) na verdade *façam coisas* — dando-lhes ferramentas e conhecimentos para agir no mundo, não apenas responder a prompts.**

Vamos desmembrar isso um pouco:

- **Sistema** — Um Agente de IA não é apenas uma coisa. É uma coleção de partes a trabalhar em conjunto. Na sua base, todo agente tem três partes:
  - **Ambiente** — O espaço onde o agente trabalha. Para um agente de reservas de viagens, seria a própria plataforma de reservas.
  - **Sensores** — Como o agente lê o estado atual do seu ambiente. O nosso agente de viagens pode verificar disponibilidade de hotéis ou preços de voos.
  - **Atuadores** — Como o agente toma ação. O agente de viagens pode reservar um quarto, enviar uma confirmação, ou cancelar uma reserva.

![O que São Agentes de IA?](../../../translated_images/pt-PT/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modelos de Linguagem Grande** — Agentes existiam antes dos LLMs, mas os LLMs são o que torna os agentes modernos tão poderosos. Eles conseguem compreender linguagem natural, raciocinar sobre contexto e transformar um pedido vago do utilizador num plano concreto de ação.

- **Executar Ações** — Sem um sistema agente, um LLM apenas gera texto. Dentro de um sistema agente, o LLM pode realmente *executar* passos — pesquisar numa base de dados, chamar uma API, enviar uma mensagem.

- **Acesso a Ferramentas** — As ferramentas que o agente pode usar dependem (1) do ambiente onde corre e (2) do que o programador lhe atribuiu. Um agente de viagens pode pesquisar voos mas não editar registos de clientes — tudo depende do que liga.

- **Memória + Conhecimento** — Os agentes podem ter memória de curto prazo (a conversa atual) e memória de longo prazo (uma base de dados de clientes, interações passadas). O agente de viagens pode "lembrar-se" que prefere lugares junto à janela.

---

### Os Diferentes Tipos de Agentes de IA

Nem todos os agentes são construídos da mesma forma. Aqui está uma divisão dos principais tipos, usando um agente de reservas de viagens como exemplo contínuo:

| **Tipo de Agente** | **O que Faz** | **Exemplo de Agente de Viagens** |
|---|---|---|
| **Agentes Reflexos Simples** | Seguem regras codificadas — sem memória, sem planeamento. | Vê um email de reclamação → encaminha para o serviço ao cliente. Só isso. |
| **Agentes Reflexos Baseados em Modelo** | Mantém um modelo interno do mundo e atualiza-o conforme as coisas mudam. | Acompanha preços históricos de voos e alerta rotas que ficaram subitamente caras. |
| **Agentes Baseados em Objetivos** | Tem um objetivo em mente e descobre como alcançá-lo passo a passo. | Reserva uma viagem completa (voos, carro, hotel) começando da sua localização atual para levá-lo ao destino. |
| **Agentes Baseados em Utilidade** | Não se limita a encontrar *uma* solução — encontra a *melhor* avaliando compensações. | Equilibra custo vs. conveniência para encontrar a viagem que melhor se adequa às suas preferências. |
| **Agentes de Aprendizagem** | Melhora com o tempo aprendendo com feedback. | Ajusta recomendações futuras de reservas com base nos resultados de inquéritos pós-viagem. |
| **Agentes Hierárquicos** | Um agente de alto nível divide o trabalho em subtarefas e delega a agentes de nível inferior. | Um pedido de "cancelar viagem" é dividido em: cancelar voo, cancelar hotel, cancelar aluguer de carro — cada um tratado por um subagente. |
| **Sistemas Multi-Agentes (MAS)** | Vários agentes independentes a trabalhar juntos (ou a competir). | Cooperativo: agentes separados tratam hotéis, voos e entretenimento. Competitivo: múltiplos agentes competem para preencher quartos de hotel ao melhor preço. |

---

## Quando Usar Agentes de IA

Só porque *pode* usar um Agente de IA, não significa que deva sempre. Aqui estão as situações em que os agentes realmente brilham:

![Quando usar Agentes de IA?](../../../translated_images/pt-PT/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemas de Final Aberto** — Quando os passos para resolver um problema não podem ser programados antecipadamente. Precisa que o LLM descubra o caminho de forma dinâmica.
- **Processos de Vários Passos** — Tarefas que requerem usar ferramentas em várias etapas, não apenas uma consulta ou geração.
- **Melhoria ao Longo do Tempo** — Quando quer que o sistema fique mais inteligente com base no feedback dos utilizadores ou sinais do ambiente.

Vamos aprofundar quando (e quando *não*) usar Agentes de IA na lição **Construindo Agentes de IA Confiáveis** mais adiante no curso.

---

## Noções Básicas de Soluções Agentic

### Desenvolvimento de Agentes

A primeira coisa a fazer ao construir um agente é definir *o que ele pode fazer* — suas ferramentas, ações e comportamentos.

Neste curso, usamos o **Microsoft Foundry Agent Service** como nossa plataforma principal. Ele suporta:

- Modelos de fornecedores como OpenAI, Mistral e Meta (Llama)
- Dados licenciados de fornecedores como Tripadvisor
- Definições padronizadas de ferramentas OpenAPI 3.0

### Padrões Agentic

Comunica com LLMs através de prompts. Com agentes, nem sempre é possível criar manualmente cada prompt — o agente precisa agir em vários passos. É aqui que entram os **Padrões Agentic**. São estratégias reutilizáveis para criar prompts e orquestrar LLMs de forma mais escalável e fiável.

Este curso está estruturado em torno dos padrões agentic mais comuns e úteis.

### Frameworks Agentic

Frameworks Agentic dão aos programadores modelos prontos, ferramentas e infraestrutura para construir agentes. Eles facilitam:

- Ligar ferramentas e capacidades
- Observar o que o agente está a fazer (e depurar quando algo corre mal)
- Colaborar entre vários agentes

Neste curso, focamo-nos no **Microsoft Agent Framework (MAF)** para construir agentes prontos para produção.

---

## Exemplos de Código

Pronto para ver em ação? Aqui estão os exemplos de código para esta lição:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Tem Perguntas?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conectar-se com outros aprendizes, participar nas horas de atendimento e obter respostas às suas perguntas sobre Agentes de IA pela comunidade.


---

## Teste Rápido Deste Agente (Opcional)

Depois de aprender a implementar agentes em [Lição 16](../16-deploying-scalable-agents/README.md), pode adicionar uma verificação rápida de saúde pós-implementação para o `TravelAgent` desta lição com o catálogo pronto [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Veja [`tests/README.md`](../tests/README.md) para saber como executá-lo.

---

## Lição Anterior

[Configuração do Curso](../00-course-setup/README.md)

## Próxima Lição

[Explorando Frameworks Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->