# Agentes de IA para Iniciantes - Guia de Estudo

Use este guia como um companheiro prático enquanto avança no curso. Ele não é
destinado a substituir as lições. Ajuda você a decidir onde começar, o que
procurar em cada lição e como conectar as ideias em uma pequena demonstração
funcional de agente.

Se esta é sua primeira vez aqui, comece simples:

1. Leia a [Configuração do Curso](./00-course-setup/README.md).
2. Complete as Lições 01-06 na ordem.
3. Mantenha uma pequena ideia de demonstração em mente enquanto aprende.
4. Após cada lição, pergunte: "O que meu agente pode fazer agora que não podia
   antes?"

## Uma Demonstração Simples para Manter em Mente

Uma boa maneira de aprender sobre agentes é seguir uma ideia de demonstração durante o curso.

Demonstração de exemplo: **um agente auxiliar do curso**.

O usuário pede:

> "Quero aprender como agentes usam ferramentas. Encontre as lições certas, resuma o que
> devo ler primeiro e me dê uma tarefa prática curta."

Um chatbot comum pode responder com base no que já sabe. Um agente pode fazer mais:

1. **Ler ou buscar arquivos do curso** para encontrar as lições certas.
2. **Usar ferramentas** para recuperar links das lições, exemplos ou material de apoio.
3. **Planejar** um caminho curto de aprendizado em vez de dar uma resposta longa.
4. **Usar o contexto** da conversa atual para manter o foco no objetivo do aprendiz.
5. **Lembrar preferências úteis** se o aplicativo suportar memória.
6. **Mostrar rastros, citações ou registros** para que o usuário entenda o que aconteceu.
7. **Aplicar salvaguardas** antes de tomar ações arriscadas ou usar dados sensíveis.


capacidade esta lição adicionaria?


## O Que Você Está Construindo

Ao final do curso, você deve ser capaz de explicar e construir sistemas de agentes
que combinam estas partes:

| Parte | Significado em linguagem simples | Na demonstração |
|------|-------------------------------|----------------|
| Modelo | O motor de raciocínio que interpreta o pedido do usuário | Entende que o aprendiz quer lições sobre uso de ferramentas |
| Ferramentas | Funções, APIs, arquivos, navegadores ou serviços que o agente pode usar | Busca no repositório ou recupera conteúdo da lição |
| Conhecimento | Documentos ou dados usados para fundamentar a resposta | Arquivos README do curso e material das lições |
| Contexto | Informações incluídas na próxima chamada do modelo | O objetivo do usuário e os resultados das ferramentas |
| Memória | Informações salvas para uso posterior | O aprendiz prefere exemplos práticos em Python |
| Planejamento | Dividir um objetivo maior em passos menores | Encontrar lições, resumi-las, sugerir prática |
| Orquestração | Direcionar o trabalho entre ferramentas, etapas ou agentes | Um planejador chama uma ferramenta de busca, depois um sumarizador |
| Confiança | Segurança, avaliação e observabilidade | Registra chamadas às ferramentas e pergunta antes de ações de alto impacto |

## Modelos e Provedores

Os exemplos de código do curso usam o **Microsoft Agent Framework (MAF)** e têm como alvo a **API Azure OpenAI Responses** — a API recomendada para o futuro, que combina conclusões de chat, chamadas de ferramenta, entrada multimodal e conversas estadofull em uma única interface. Você se conecta por meio de um projeto **Microsoft Foundry** (com `FoundryChatClient`) ou diretamente ao Azure OpenAI (com `OpenAIChatClient`).

Conforme avança nas lições, você tem algumas opções de provedores:

- **Microsoft Foundry / Azure OpenAI (API Responses)** — o caminho principal usado nas lições. Faça login com `az login` para autenticação Entra ID sem chave.
- **Foundry Local** — execute modelos totalmente no dispositivo por meio de uma API compatível com OpenAI (sem nuvem, sem chaves de API). Ideal para experimentos offline ou gratuitos. Veja [Configuração do Curso](./00-course-setup/README.md).
- **MiniMax** — um provedor compatível com OpenAI com modelos de grande contexto, utilizável como alternativa plug-and-play.

> **Nota:** GitHub Models está descontinuado (será encerrado em julho de 2026) e não suporta a Responses API. Os exemplos foram atualizados para usar Azure OpenAI / Microsoft Foundry.

## Escolha Seu Caminho de Aprendizado

Você pode fazer o curso completo em ordem ou pular para um caminho baseado no que deseja
construir.

| Se seu objetivo é... | Comece com | Depois estude |
|---------------------|------------|-----------|
| Entender o que são agentes | 01, 02, 03 | 04, 05, 06 |
| Construir um agente que use ferramentas | 04 | 05, 07, 14 |
| Construir um agente baseado em RAG | 05 | 04, 06, 12 |
| Projetar fluxos de trabalho em múltiplas etapas | 07 | 08, 09, 14 |
| Entender sistemas multiagente | 08 | 07, 09, 11 |
| Preparar agentes para produção | 06, 10 | 12, 13, 16, 18 |
| Implantar e escalar agentes no Foundry | 10, 16 | 06, 13, 18 |
| Construir agentes locais / offline-first | 17 | 04, 05, 11 |
| Explorar protocolos e automação de navegador | 11, 15 | 10, 18 |

Dica: se você é novo em agentes, não pule as Lições 01-06. Elas fornecem o
vocabulário que você precisará para o resto do curso.

## Guia Lição por Lição

| Lição | O que você aprende | Tente isto após a lição |
|-------|-------------------|--------------------------|
| [01 - Introdução aos Agentes de IA](./01-intro-to-ai-agents/README.md) | O que torna um agente diferente de um chatbot básico. | Explique sua ideia de demonstração como um agente, não apenas um aplicativo de chat. |
| [02 - Frameworks Agentes](./02-explore-agentic-frameworks/README.md) | Como frameworks ajudam com modelos, ferramentas, estado e fluxos de trabalho. | Identifique quais partes da sua demonstração um framework gerenciaria. |
| [03 - Padrões de Design Agentic](./03-agentic-design-patterns/README.md) | Padrões comuns para projetar o comportamento do agente. | Desenhe a jornada do usuário antes de escrever código. |
| [04 - Uso de Ferramentas](./04-tool-use/README.md) | Como agentes chamam ferramentas para obter dados ou agir. | Defina uma ferramenta que seu agente de demonstração precisaria. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Como a recuperação fundamenta as respostas do agente em documentos ou dados. | Decida qual fonte de conhecimento sua demonstração deve buscar. |

| [06 - Agentes Confiáveis](./06-building-trustworthy-agents/README.md) | Como adicionar proteções, supervisão e comportamento mais seguro. | Adicione uma regra para quando o agente deve perguntar ao usuário primeiro. |
| [07 - Design de Planejamento](./07-planning-design/README.md) | Como agentes dividem grandes objetivos em etapas menores. | Escreva um plano de três etapas para sua solicitação de demonstração. |
| [08 - Design Multi-Agente](./08-multi-agent/README.md) | Quando dividir o trabalho entre agentes especializados. | Decida se sua demonstração precisa de um agente ou vários. |
| [09 - Metacognição](./09-metacognition/README.md) | Como agentes podem revisar e melhorar sua própria saída. | Adicione uma verificação final antes do agente responder. |
| [10 - Agentes de IA em Produção](./10-ai-agents-production/README.md) | O que muda quando um agente passa de demonstração para produção. | Liste o que você monitoraria: qualidade, custo, latência, falhas. |
| [11 - Protocolos Agentes](./11-agentic-protocols/README.md) | Como protocolos conectam agentes a ferramentas e outros agentes. | Identifique onde um protocolo padrão poderia simplificar a integração. |
| [12 - Engenharia de Contexto](./12-context-engineering/README.md) | Como selecionar, aparar, isolar e gerenciar o contexto. | Decida o que pertence no prompt e o que deve ficar de fora. |
| [13 - Memória do Agente](./13-agent-memory/README.md) | Como agentes podem salvar informações úteis entre interações. | Escolha uma preferência segura que sua demonstração poderia lembrar. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blocos de construção específicos do framework para agentes e fluxos de trabalho, além de hospedar agentes LangChain/LangGraph no Microsoft Foundry. | Mapeie os passos da sua demonstração para conceitos do framework. |
| [15 - Agentes de Uso do Computador](./15-browser-use/README.md) | Como agentes podem interagir com navegadores ou interfaces de usuário, incluindo exemplos reais como o Microsoft Project Opal. | Escolha uma tarefa no navegador que ainda deve requerer confirmação do usuário. |
| [16 - Implantação de Agentes Escaláveis](./16-deploying-scalable-agents/README.md) | Como levar um agente do protótipo para uma implantação escalável e observável em produção no Microsoft Foundry (agentes hospedados, roteamento de modelo, cache, portões de avaliação, testes rápidos). | Liste as preocupações de produção que sua demonstração ainda precisa: hospedagem, roteamento, custo, avaliação. |
| [17 - Criando Agentes de IA Locais](./17-creating-local-ai-agents/README.md) | Como construir agentes locais que rodam inteiramente na sua máquina com Foundry Local e Qwen (ferramentas locais, RAG local, MCP local). | Decida quais partes da sua demonstração devem permanecer privadas e rodar localmente. |
| [18 - Securing AI Agents](./18-securing-ai-agents/README.md) | Como tornar ações de agente mais auditáveis e evidentes para fraude. | Decida quais ações na sua demonstração devem ser registradas ou ter comprovantes. |

## Validando Agentes Implantados com Testes Rápidos

Quando você implanta um agente (Lição 16), um **teste rápido** é a verificação inicial mais barata
para confirmar que a implantação realmente responde. Este repositório oferece catálogos prontos para uso
em [tests/](./tests/README.md) para os agentes implantáveis nas Lições
01, 04, 05 e 16, conectados à
Ação do GitHub [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test).
Execute-os na aba **Actions** após implantar o agente da lição.
Testes rápidos são uma primeira barreira — avaliações offline e online (Lições 10 e 16)
indicam quão *bom* o agente é.

## Ideias-Chave em Termos para Iniciantes

### Ferramentas

Uma ferramenta é algo que o agente pode chamar para realizar trabalho fora do modelo. Uma boa ferramenta
tem um nome claro, uma função específica, entradas tipadas, saída previsível e uma forma segura
de falhar.

Para o demo auxiliar do curso, uma ferramenta pode ser:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG e Conhecimento

RAG ajuda o agente a responder com base no material fonte em vez de especular. Neste
curso, esse material fonte pode ser os READMEs das lições, exemplos de código ou recursos externos
vinculados nas lições.

Use RAG quando a resposta deve ser fundamentada em documentos, dados ou arquivos
atuais do projeto.

### Planejamento

Planejamento é útil quando a solicitação envolve mais de uma etapa. Mantenha os planos curtos e
visíveis o suficiente para um desenvolvedor ou usuário inspecionar.

Para a demonstração, um plano pode ser:

1. Encontrar lições relacionadas ao uso de ferramentas.
2. Resumir as lições mais relevantes.
3. Recomendar uma tarefa prática.

### Contexto

Contexto é o que o modelo vê no momento. Pouco contexto pode fazer o agente
perder detalhes importantes. Muito contexto pode deixar o agente mais lento, mais caro,
ou mais fácil de confundir.

Boa engenharia de contexto significa escolher as informações certas para a próxima
chamada ao modelo.

### Memória

Memória é a informação salva para uso posterior. Não salve tudo. Salve informações
somente quando forem úteis, seguras e fáceis de atualizar ou excluir.

Por exemplo, lembrar que "o aprendiz prefere exemplos em Python" pode ser útil.
Lembrar dados pessoais sensíveis geralmente não é.

### Avaliação e Observabilidade

Avaliação pergunta: o agente fez a coisa certa?

Observabilidade pergunta: podemos ver como isso aconteceu?

Para agentes em produção, acompanhe chamadas ao modelo, chamadas à ferramenta, contexto recuperado,
latência, custo, falhas e feedback do usuário.

### Confiança e Segurança

Agentes confiáveis precisam de mais que um prompt útil. Use ferramentas com privilégios mínimos,
aprovação humana para ações de alto impacto, redação de dados onde necessário, e logs ou
recibos para ações que devem ser auditadas.

## Uma Rotina de Revisão de 15 Minutos

Use esta rotina após cada lição:

1. **Resuma a lição em uma frase.**
2. **Nomeie a nova capacidade do agente.** Por exemplo: uso de ferramenta, recuperação,
   planejamento, memória, observabilidade ou segurança.
3. **Adicione ao demo auxiliar do curso.** O que muda no demo agora?
4. **Identifique o risco.** O que poderia dar errado se essa capacidade for usada incorretamente?
5. **Escreva uma pergunta de teste.** Como você verificaria se o agente se comporta bem?

## Auto-Verificação Rápida

Antes de prosseguir, tente responder a estas perguntas:

1. O que um agente pode fazer que um chatbot comum não pode fazer sozinho?
2. Qual ferramenta seu agente precisaria primeiro, e por quê?
3. Qual fonte de conhecimento deveria fundamentar a resposta do agente?
4. Qual contexto deveria ser incluído na próxima chamada ao modelo?

5. O que o agente deve lembrar e o que deve evitar armazenar?
6. Quando o agente deve pedir aprovação humana?
7. Quais registros, rastros ou recibos ajudariam você a depurar ou auditar o agente depois?


## Exercício Sugerido de Conclusão

Ao final do curso, construa um pequeno agente que ajude um aprendiz a navegar por este
repositório.

Versão mínima:

- Aceitar um tópico do usuário.
- Encontrar as lições mais relevantes.
- Resumir o que ler primeiro.
- Sugerir uma tarefa prática.
- Mostrar quais arquivos de lição ou links foram usados.

Versão avançada:

- Lembrar a linguagem de programação preferida do aprendiz.
- Usar um plano simples antes de responder.
- Adicionar uma etapa de auto-verificação antes da resposta final.
- Registrar chamadas de ferramentas e fontes recuperadas.
- Pedir confirmação antes de abrir o navegador ou executar tarefas de automação de UI.

Isso oferece uma forma pequena, mas realista, de praticar ferramentas, RAG, planejamento,
contexto, memória, observabilidade, e confiança em um único projeto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->