# Agentes de IA para Iniciantes - Guia de Estudo

Use este guia como companheiro prático enquanto avança no curso. Não é
destinado a substituir as aulas. Ajuda-o a decidir onde começar, o que
procurar em cada lição, e como ligar as ideias numa pequena demo funcional
de agente.

Se é a sua primeira vez aqui, comece pelo simples:

1. Leia a [Configuração do Curso](./00-course-setup/README.md).
2. Complete as Lições 01-06 por ordem.
3. Mantenha uma pequena ideia de demo em mente enquanto aprende.
4. Após cada lição, pergunte: "O que é que o meu agente pode fazer agora que
   antes não conseguia?"

## Uma Demo Simples para Manter em Mente

Uma boa forma de aprender agentes é seguir uma ideia de demo ao longo do curso.

Exemplo de demo: **um agente ajudante do curso**.

O utilizador pede:

> "Quero aprender como os agentes usam ferramentas. Encontra as lições certas, 
> resume o que devo ler primeiro, e dá-me uma tarefa prática curta."

Um chatbot comum pode responder com base no que já sabe. Um agente pode fazer mais:

1. **Ler ou pesquisar ficheiros do curso** para encontrar as lições certas.
2. **Usar ferramentas** para obter links das lições, exemplos ou material de apoio.
3. **Planear** um caminho de aprendizagem curto em vez de dar uma resposta longa.
4. **Usar o contexto** da conversa atual para se manter focado no objetivo do aprendiz.

5. **Lembrar preferências úteis** se a aplicação suportar memória.
6. **Mostrar registos, citações ou logs** para o utilizador compreender o que aconteceu.
7. **Aplicar limites** antes de realizar ações arriscadas ou usar dados sensíveis.

À medida que estuda cada lição, regresse a esta demo e pergunte: que nova
capacidade acrescentaria esta lição?

## Para o que Está a Construir

No final do curso, deverá ser capaz de explicar e construir sistemas de agentes
que combinem estas partes:

| Parte | Significado em linguagem simples | Na demo |
|------|-------------------------------|-------------|
| Modelo | O motor de raciocínio que interpreta o pedido do utilizador | Entende que o aprendiz quer lições sobre uso de ferramentas |
| Ferramentas | Funções, APIs, ficheiros, browsers ou serviços que o agente pode usar | Pesquisa no repositório ou obtém conteúdo da lição |
| Conhecimento | Documentos ou dados usados para fundamentar a resposta | Ficheiros README do curso e material das lições |
| Contexto | Informação incluída na próxima chamada ao modelo | O objetivo do utilizador e os resultados das ferramentas |
| Memória | Informação guardada para uso posterior | O aprendiz prefere exemplos práticos em Python |
| Planeamento | Dividir um objetivo maior em passos menores | Encontrar lições, resumir, sugerir prática |
| Orquestração | Direcionar o trabalho entre ferramentas, passos ou agentes | Um planeador chama uma ferramenta de pesquisa e depois um sumarizador |
| Confiança | Segurança, avaliação, e observabilidade | Regista chamadas às ferramentas e pergunta antes de ações impactantes |

## Modelos e Fornecedores

Os exemplos de código do curso usam o **Microsoft Agent Framework (MAF)** e destinam-se à **Azure OpenAI Responses API** — a API recomendada para futuro, que combina chat completions, chamadas a ferramentas, input multimodal e conversas com estado numa única interface. Liga-se através de um projeto **Microsoft Foundry** (com `FoundryChatClient`) ou diretamente à Azure OpenAI (com `OpenAIChatClient`).


À medida que avança nas lições, tem algumas opções de fornecedor:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — o caminho principal usado nas lições. Inicie sessão com `az login` para autenticação Entra ID sem chave.
- **Foundry Local** — execute modelos totalmente no dispositivo através de uma API compatível com OpenAI (sem cloud, sem chaves API). Ideal para experimentação offline ou sem custos. Veja [Configuração do Curso](./00-course-setup/README.md).
- **MiniMax** — um fornecedor compatível com OpenAI com modelos de grande contexto, utilizável como alternativa plug-and-play.

> **Nota:** GitHub Models está descontinuado (desativação em julho de 2026) e não suporta a Responses API. Os exemplos foram atualizados para usar Azure OpenAI / Microsoft Foundry em vez disso.

## Escolha o Seu Percurso de Aprendizagem

Pode seguir o curso completo por ordem, ou saltar para um percurso baseado no que quer
construir.

| Se o seu objetivo é... | Comece por | Depois estude |
|-----------------------|------------|------------|
| Compreender o que são agentes | 01, 02, 03 | 04, 05, 06 |
| Construir um agente que usa ferramentas | 04 | 05, 07, 14 |
| Construir um agente baseado em RAG | 05 | 04, 06, 12 |
| Desenhar fluxos de trabalho em vários passos | 07 | 08, 09, 14 |
| Compreender sistemas multi-agente | 08 | 07, 09, 11 |
| Preparar agentes para produção | 06, 10 | 12, 13, 16, 18 |
| Implantar e escalar agentes na Foundry | 10, 16 | 06, 13, 18 |
| Construir agentes locais / offline-primeiro | 17 | 04, 05, 11 |
| Explorar protocolos e automação de browser | 11, 15 | 10, 18 |

Dica: se é novo em agentes, não salte as Lições 01-06. Elas dão-lhe o
vocabulário que vai precisar para o restante do curso.

## Guia Lição a Lição

| Lição | O que aprende | Experimente isto após a lição |
|--------|----------------|---------------------------|
| [01 - Introdução a Agentes de IA](./01-intro-to-ai-agents/README.md) | O que torna um agente diferente de um chatbot básico. | Explique a sua ideia de demo como um agente, não apenas uma app de chat. |
| [02 - Estruturas Agentic](./02-explore-agentic-frameworks/README.md) | Como as estruturas ajudam com modelos, ferramentas, estado e fluxos de trabalho. | Identifique que partes da sua demo uma estrutura geriria. |
| [03 - Padrões de Design Agentic](./03-agentic-design-patterns/README.md) | Padrões comuns para desenhar o comportamento do agente. | Esboce a jornada do utilizador antes de escrever código. |
| [04 - Uso de Ferramentas](./04-tool-use/README.md) | Como agentes chamam ferramentas para obter dados ou agir. | Defina uma ferramenta de que o seu agente de demo precisaria. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Como a recuperação fundamenta as respostas do agente em documentos ou dados. | Decida qual fonte de conhecimento a sua demo deve procurar. |

| [06 - Agentes Fiáveis](./06-building-trustworthy-agents/README.md) | Como adicionar guard rails, supervisão e comportamento mais seguro. | Adicionar uma regra para quando o agente deve pedir primeiro ao utilizador. |
| [07 - Design de Planeamento](./07-planning-design/README.md) | Como os agentes dividem metas maiores em passos menores. | Escrever um plano em três passos para o seu pedido de demonstração. |
| [08 - Design Multi-Agente](./08-multi-agent/README.md) | Quando dividir o trabalho entre agentes especializados. | Decidir se a sua demonstração precisa de um agente ou de vários. |
| [09 - Metacognição](./09-metacognition/README.md) | Como os agentes podem rever e melhorar a sua própria saída. | Adicionar uma verificação final antes de o agente responder. |
| [10 - Agentes de IA em Produção](./10-ai-agents-production/README.md) | O que muda quando um agente passa da demonstração para a produção. | Liste o que monitorizaria: qualidade, custo, latência, falhas. |
| [11 - Protocolos Agentes](./11-agentic-protocols/README.md) | Como os protocolos ligam agentes a ferramentas e a outros agentes. | Identificar onde um protocolo padrão poderia simplificar a integração. |
| [12 - Engenharia de Contexto](./12-context-engineering/README.md) | Como selecionar, cortar, isolar e gerir o contexto. | Decidir o que deve pertencer ao prompt e o que deve ficar de fora. |
| [13 - Memória do Agente](./13-agent-memory/README.md) | Como os agentes podem guardar informações úteis ao longo das interações. | Escolher uma preferência segura que a sua demonstração poderia memorizar. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blocos de construção específicos do framework para agentes e fluxos de trabalho, além de hospedar agentes LangChain/LangGraph no Microsoft Foundry. | Mapear os passos da sua demonstração para conceitos do framework. |
| [15 - Agentes de Uso de Computador](./15-browser-use/README.md) | Como os agentes podem interagir com browsers ou interfaces de utilizador, incluindo exemplos reais como Microsoft Project Opal. | Escolher uma tarefa do browser que ainda deva requerer confirmação do utilizador. |
| [16 - Implantação de Agentes Escaláveis](./16-deploying-scalable-agents/README.md) | Como levar um agente do protótipo para uma implantação de produção escalável e observável no Microsoft Foundry (agentes hospedados, roteamento de modelos, caching, portões de avaliação, testes de fumo). | Liste as preocupações de produção que a sua demonstração ainda precisa: hospedagem, roteamento, custo, avaliação. |
| [17 - Criação de Agentes de IA Locais](./17-creating-local-ai-agents/README.md) | Como construir agentes local-first que correm inteiramente na sua máquina com Foundry Local e Qwen (ferramentas locais, RAG local, MCP local). | Decidir que partes da sua demonstração devem permanecer privadas e correr localmente. |
| [18 - Segurança de Agentes de IA](./18-securing-ai-agents/README.md) | Como tornar as ações do agente mais auditáveis e à prova de adulterações. | Decidir que ações na sua demonstração devem ser registadas ou terem recibo. |

## Validar Agentes Implantados com Testes de Fumo

Quando implanta um agente (Lição 16), um **teste de fumo** é a primeira verificação mais barata
que confirma se a implantação realmente responde. Este repositório inclui catálogos prontos a correr
em [tests/](./tests/README.md) para os agentes implantáveis das Lições
01, 04, 05, e 16, ligados à
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Execute-os a partir do separador **Actions** após implantar o agente da lição.
Testes de fumo são a primeira barreira — a avaliação offline e online (Lições 10 e 16)
indicam quão *bom* o agente é.

## Ideias Principais em Termos Simples para Iniciantes

### Ferramentas

Uma ferramenta é algo que o agente pode chamar para executar trabalho fora do modelo. Uma boa ferramenta
tem um nome claro, um trabalho restrito, entradas tipadas, saída previsível, e uma forma segura
de falhar.

Para a demonstração do assistente do curso, uma ferramenta pode ser:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG e Conhecimento

RAG ajuda o agente a responder com base em material de origem em vez de adivinhar. Neste
curso, esse material pode ser os README das lições, exemplos de código, ou recursos externos
referenciados nas lições.

Use RAG quando a resposta deve estar fundamentada em documentos, dados, ou ficheiros
atuais do projeto.

### Planeamento

Planeamento é útil quando o pedido tem mais do que um passo. Mantenha os planos curtos e
visíveis o suficiente para um desenvolvedor ou utilizador inspecionar.

Para a demonstração, um plano pode ser:

1. Encontrar lições relacionadas com o uso de ferramentas.
2. Resumir as lições mais relevantes.
3. Recomendar uma tarefa prática.

### Contexto

Contexto é o que o modelo vê neste momento. Contexto insuficiente pode levar o agente
a perder detalhes importantes. Contexto em excesso pode tornar o agente mais lento, mais caro,
ou mais fácil de confundir.

Boa engenharia de contexto significa escolher a informação correta para a próxima chamada
ao modelo.

### Memória

Memória é informação guardada para mais tarde. Não guarde tudo. Guarde informação
apenas quando for útil, segura, e fácil de atualizar ou apagar.

Por exemplo, lembrar que "o aprendiz prefere exemplos em Python" pode ser útil.
Lembrar dados pessoais sensíveis normalmente não é.

### Avaliação e Observabilidade

Avaliação pergunta: o agente fez a coisa certa?

Observabilidade pergunta: podemos ver como isso aconteceu?

Para agentes de produção, registe chamadas ao modelo, chamadas a ferramentas, contexto recuperado,
latência, custo, falhas, e feedback do utilizador.

### Confiança e Segurança

Agentes confiáveis precisam de mais do que um prompt útil. Use ferramentas com privilégios mínimos,
aprovação humana para ações de alto impacto, redação de dados quando necessário, e registos ou
recibos para ações que devem ser auditadas.

## Uma Rotina de Revisão de 15 Minutos

Use esta rotina após cada lição:

1. **Resuma a lição numa frase.**
2. **Nomeie a nova capacidade do agente.** Por exemplo: uso de ferramentas, recuperação,
   planeamento, memória, observabilidade, ou segurança.
3. **Adicione-a à demonstração do assistente do curso.** O que muda na demonstração agora?
4. **Encontre o risco.** O que pode correr mal se esta capacidade for mal utilizada?
5. **Escreva uma questão de teste.** Como verificaria que o agente se comporta bem?

## Auto-Verificação Rápida

Antes de avançar, tente responder a estas perguntas:

1. O que pode um agente fazer que um chatbot normal não pode fazer sozinho?
2. Que ferramenta o seu agente precisaria primeiro, e porquê?
3. Que fonte de conhecimento deve fundamentar a resposta do agente?
4. Que contexto deve ser incluído na próxima chamada ao modelo?

5. O que deve o agente lembrar, e o que deve evitar armazenar?
6. Quando deve o agente pedir aprovação humana?
7. Que registos, rastos, ou recibos o ajudariam a depurar ou auditar o agente mais tarde?


## Exercício Final Sugerido

No final do curso, construa um pequeno agente que ajude um aprendiz a navegar neste
repositório.

Versão mínima:

- Aceitar um tópico do utilizador.
- Encontrar as lições mais relevantes.
- Resumir o que deve ser lido primeiro.
- Sugerir uma tarefa prática.
- Mostrar quais ficheiros ou links das lições foram usados.

Versão avançada:

- Lembrar a linguagem de programação preferida do aprendiz.
- Usar um plano simples antes de responder.
- Adicionar um passo de autoverificação antes da resposta final.
- Registar chamadas de ferramentas e fontes recuperadas.
- Pedir confirmação antes de abrir o navegador ou executar tarefas de automação de interface.

Isto dá-lhe uma forma pequena mas realista de praticar ferramentas, RAG, planeamento,
contexto, memória, observabilidade e confiança num só projeto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->