<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T12:47:37+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "br"
}
-->
[![Agentes de IA Confiáveis](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.br.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Construindo Agentes de IA Confiáveis

## Introdução

Esta lição abordará:

- Como construir e implantar Agentes de IA seguros e eficazes.
- Considerações importantes de segurança ao desenvolver Agentes de IA.
- Como manter a privacidade de dados e usuários ao desenvolver Agentes de IA.

## Objetivos de Aprendizado

Após concluir esta lição, você saberá como:

- Identificar e mitigar riscos ao criar Agentes de IA.
- Implementar medidas de segurança para garantir que os dados e o acesso sejam gerenciados adequadamente.
- Criar Agentes de IA que mantenham a privacidade dos dados e proporcionem uma experiência de qualidade ao usuário.

## Segurança

Vamos começar analisando como construir aplicações agentivas seguras. Segurança significa que o agente de IA desempenha suas funções conforme projetado. Como desenvolvedores de aplicações agentivas, temos métodos e ferramentas para maximizar a segurança:

### Construindo uma Estrutura de Mensagem do Sistema

Se você já desenvolveu uma aplicação de IA usando Modelos de Linguagem de Grande Escala (LLMs), sabe a importância de projetar um prompt ou mensagem do sistema robusto. Esses prompts estabelecem as regras, instruções e diretrizes para como o LLM interagirá com o usuário e os dados.

Para Agentes de IA, o prompt do sistema é ainda mais importante, pois os Agentes de IA precisarão de instruções altamente específicas para realizar as tarefas que projetamos para eles.

Para criar prompts de sistema escaláveis, podemos usar uma estrutura de mensagem do sistema para construir um ou mais agentes em nossa aplicação:

![Construindo uma Estrutura de Mensagem do Sistema](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.br.png)

#### Passo 1: Criar uma Meta Mensagem do Sistema

O meta prompt será usado por um LLM para gerar os prompts do sistema para os agentes que criarmos. Nós o projetamos como um modelo para que possamos criar vários agentes de forma eficiente, se necessário.

Aqui está um exemplo de uma meta mensagem do sistema que forneceríamos ao LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Criar um Prompt Básico

O próximo passo é criar um prompt básico para descrever o Agente de IA. Você deve incluir o papel do agente, as tarefas que ele realizará e quaisquer outras responsabilidades do agente.

Aqui está um exemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornecer a Mensagem Básica do Sistema ao LLM

Agora podemos otimizar essa mensagem do sistema fornecendo a meta mensagem do sistema como a mensagem do sistema e nossa mensagem básica do sistema.

Isso produzirá uma mensagem do sistema melhor projetada para orientar nossos agentes de IA:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Passo 4: Iterar e Melhorar

O valor dessa estrutura de mensagem do sistema é a capacidade de escalar a criação de mensagens do sistema para vários agentes de forma mais fácil, bem como melhorar suas mensagens do sistema ao longo do tempo. É raro que uma mensagem do sistema funcione perfeitamente na primeira tentativa para todo o caso de uso. Fazer pequenos ajustes e melhorias alterando a mensagem básica do sistema e executando-a novamente permitirá que você compare e avalie os resultados.

## Compreendendo Ameaças

Para construir agentes de IA confiáveis, é importante entender e mitigar os riscos e ameaças ao seu agente de IA. Vamos analisar algumas das diferentes ameaças aos agentes de IA e como você pode planejar e se preparar melhor para elas.

![Compreendendo Ameaças](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.br.png)

### Tarefa e Instrução

**Descrição:** Os atacantes tentam alterar as instruções ou objetivos do agente de IA por meio de prompts ou manipulação de entradas.

**Mitigação**: Execute verificações de validação e filtros de entrada para detectar prompts potencialmente perigosos antes que sejam processados pelo Agente de IA. Como esses ataques geralmente exigem interação frequente com o Agente, limitar o número de turnos em uma conversa é outra maneira de prevenir esses tipos de ataques.

### Acesso a Sistemas Críticos

**Descrição**: Se um agente de IA tiver acesso a sistemas e serviços que armazenam dados sensíveis, os atacantes podem comprometer a comunicação entre o agente e esses serviços. Isso pode incluir ataques diretos ou tentativas indiretas de obter informações sobre esses sistemas por meio do agente.

**Mitigação**: Os agentes de IA devem ter acesso a sistemas apenas quando necessário para evitar esses tipos de ataques. A comunicação entre o agente e o sistema também deve ser segura. Implementar autenticação e controle de acesso é outra maneira de proteger essas informações.

### Sobrecarga de Recursos e Serviços

**Descrição:** Agentes de IA podem acessar diferentes ferramentas e serviços para realizar tarefas. Os atacantes podem usar essa capacidade para atacar esses serviços enviando um alto volume de solicitações por meio do Agente de IA, o que pode resultar em falhas no sistema ou altos custos.

**Mitigação:** Implemente políticas para limitar o número de solicitações que um agente de IA pode fazer a um serviço. Limitar o número de turnos de conversa e solicitações ao seu agente de IA é outra maneira de prevenir esses tipos de ataques.

### Envenenamento da Base de Conhecimento

**Descrição:** Esse tipo de ataque não visa diretamente o agente de IA, mas sim a base de conhecimento e outros serviços que o agente de IA usará. Isso pode envolver a corrupção dos dados ou informações que o agente de IA usará para realizar uma tarefa, levando a respostas tendenciosas ou não intencionais ao usuário.

**Mitigação:** Realize verificações regulares dos dados que o agente de IA usará em seus fluxos de trabalho. Certifique-se de que o acesso a esses dados seja seguro e que apenas pessoas confiáveis possam alterá-los para evitar esse tipo de ataque.

### Erros em Cascata

**Descrição:** Agentes de IA acessam várias ferramentas e serviços para realizar tarefas. Erros causados por atacantes podem levar a falhas em outros sistemas aos quais o agente de IA está conectado, fazendo com que o ataque se torne mais disseminado e difícil de solucionar.

**Mitigação**: Uma maneira de evitar isso é fazer com que o Agente de IA opere em um ambiente limitado, como realizar tarefas em um contêiner Docker, para evitar ataques diretos ao sistema. Criar mecanismos de fallback e lógica de repetição quando certos sistemas respondem com um erro é outra maneira de evitar falhas maiores no sistema.

## Humano no Ciclo

Outra maneira eficaz de construir sistemas de Agentes de IA confiáveis é usar um Humano no Ciclo. Isso cria um fluxo onde os usuários podem fornecer feedback aos Agentes durante a execução. Os usuários essencialmente atuam como agentes em um sistema multiagente, fornecendo aprovação ou encerrando o processo em execução.

![Humano no Ciclo](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.br.png)

Aqui está um trecho de código usando AutoGen para mostrar como esse conceito é implementado:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Conclusão

Construir agentes de IA confiáveis requer um design cuidadoso, medidas de segurança robustas e iteração contínua. Ao implementar sistemas estruturados de meta prompts, entender ameaças potenciais e aplicar estratégias de mitigação, os desenvolvedores podem criar agentes de IA que sejam seguros e eficazes. Além disso, incorporar uma abordagem de humano no ciclo garante que os agentes de IA permaneçam alinhados às necessidades dos usuários, minimizando riscos. À medida que a IA continua a evoluir, manter uma postura proativa em relação à segurança, privacidade e considerações éticas será fundamental para fomentar confiança e confiabilidade em sistemas impulsionados por IA.

### Tem Mais Perguntas sobre Construção de Agentes de IA Confiáveis?

Participe do [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Visão geral de IA responsável</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de modelos de IA generativa e aplicações de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensagens de sistema de segurança</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modelo de Avaliação de Riscos</a>

## Lição Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lição

[Padrão de Design de Planejamento](../07-planning-design/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.