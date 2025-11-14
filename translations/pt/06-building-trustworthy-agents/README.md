<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-30T14:11:46+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "pt"
}
-->
[![Agentes de IA Confiáveis](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.pt.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clique na imagem acima para ver o vídeo desta lição)_

# Construindo Agentes de IA Confiáveis

## Introdução

Esta lição abordará:

- Como construir e implementar agentes de IA seguros e eficazes.
- Considerações importantes de segurança ao desenvolver agentes de IA.
- Como manter a privacidade de dados e usuários ao desenvolver agentes de IA.

## Objetivos de Aprendizagem

Após concluir esta lição, saberá como:

- Identificar e mitigar riscos ao criar agentes de IA.
- Implementar medidas de segurança para garantir que os dados e o acesso sejam geridos adequadamente.
- Criar agentes de IA que mantenham a privacidade dos dados e ofereçam uma experiência de qualidade ao utilizador.

## Segurança

Vamos primeiro analisar como construir aplicações agentivas seguras. Segurança significa que o agente de IA funciona conforme projetado. Como criadores de aplicações agentivas, temos métodos e ferramentas para maximizar a segurança:

### Construindo uma Estrutura de Mensagem de Sistema

Se já desenvolveu uma aplicação de IA usando Modelos de Linguagem de Grande Escala (LLMs), sabe da importância de projetar um prompt ou mensagem de sistema robusto. Esses prompts estabelecem as regras, instruções e diretrizes para como o LLM interagirá com o utilizador e os dados.

Para agentes de IA, o prompt de sistema é ainda mais importante, pois os agentes de IA precisam de instruções altamente específicas para realizar as tarefas que projetamos para eles.

Para criar prompts de sistema escaláveis, podemos usar uma estrutura de mensagem de sistema para construir um ou mais agentes na nossa aplicação:

![Construindo uma Estrutura de Mensagem de Sistema](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.pt.png)

#### Passo 1: Criar uma Meta Mensagem de Sistema

O meta prompt será usado por um LLM para gerar os prompts de sistema para os agentes que criamos. Projetamo-lo como um modelo para que possamos criar múltiplos agentes de forma eficiente, se necessário.

Aqui está um exemplo de uma meta mensagem de sistema que daríamos ao LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Criar um prompt básico

O próximo passo é criar um prompt básico para descrever o agente de IA. Deve incluir o papel do agente, as tarefas que o agente realizará e quaisquer outras responsabilidades do agente.

Aqui está um exemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornecer a Mensagem de Sistema Básica ao LLM

Agora podemos otimizar esta mensagem de sistema fornecendo a meta mensagem de sistema como a mensagem de sistema e a nossa mensagem de sistema básica.

Isso produzirá uma mensagem de sistema melhor projetada para orientar os nossos agentes de IA:

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

O valor desta estrutura de mensagem de sistema é poder escalar a criação de mensagens de sistema para múltiplos agentes de forma mais fácil, bem como melhorar as mensagens de sistema ao longo do tempo. É raro ter uma mensagem de sistema que funcione perfeitamente na primeira tentativa para o caso de uso completo. Ser capaz de fazer pequenos ajustes e melhorias alterando a mensagem de sistema básica e executando-a através do sistema permitirá comparar e avaliar os resultados.

## Compreendendo Ameaças

Para construir agentes de IA confiáveis, é importante compreender e mitigar os riscos e ameaças ao seu agente de IA. Vamos analisar algumas das diferentes ameaças aos agentes de IA e como pode planear e preparar-se melhor para elas.

![Compreendendo Ameaças](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.pt.png)

### Tarefa e Instrução

**Descrição:** Os atacantes tentam alterar as instruções ou objetivos do agente de IA através de prompts ou manipulação de entradas.

**Mitigação**: Execute verificações de validação e filtros de entrada para detetar prompts potencialmente perigosos antes de serem processados pelo agente de IA. Como esses ataques geralmente requerem interação frequente com o agente, limitar o número de turnos numa conversa é outra forma de prevenir esses tipos de ataques.

### Acesso a Sistemas Críticos

**Descrição**: Se um agente de IA tiver acesso a sistemas e serviços que armazenam dados sensíveis, os atacantes podem comprometer a comunicação entre o agente e esses serviços. Isso pode incluir ataques diretos ou tentativas indiretas de obter informações sobre esses sistemas através do agente.

**Mitigação**: Os agentes de IA devem ter acesso a sistemas apenas quando necessário para prevenir esses tipos de ataques. A comunicação entre o agente e o sistema também deve ser segura. Implementar autenticação e controlo de acesso é outra forma de proteger essas informações.

### Sobrecarga de Recursos e Serviços

**Descrição:** Os agentes de IA podem aceder a diferentes ferramentas e serviços para realizar tarefas. Os atacantes podem usar essa capacidade para atacar esses serviços enviando um grande volume de pedidos através do agente de IA, o que pode resultar em falhas no sistema ou custos elevados.

**Mitigação:** Implemente políticas para limitar o número de pedidos que um agente de IA pode fazer a um serviço. Limitar o número de turnos de conversa e pedidos ao seu agente de IA é outra forma de prevenir esses tipos de ataques.

### Envenenamento da Base de Conhecimento

**Descrição:** Este tipo de ataque não tem como alvo o agente de IA diretamente, mas sim a base de conhecimento e outros serviços que o agente de IA utilizará. Isso pode envolver a corrupção dos dados ou informações que o agente de IA usará para realizar uma tarefa, levando a respostas tendenciosas ou indesejadas ao utilizador.

**Mitigação:** Realize verificações regulares dos dados que o agente de IA usará nos seus fluxos de trabalho. Garanta que o acesso a esses dados seja seguro e apenas alterado por indivíduos de confiança para evitar este tipo de ataque.

### Erros em Cascata

**Descrição:** Os agentes de IA acedem a várias ferramentas e serviços para realizar tarefas. Erros causados por atacantes podem levar a falhas em outros sistemas aos quais o agente de IA está conectado, tornando o ataque mais abrangente e difícil de resolver.

**Mitigação**: Uma forma de evitar isso é fazer com que o agente de IA opere num ambiente limitado, como realizar tarefas num contêiner Docker, para prevenir ataques diretos ao sistema. Criar mecanismos de fallback e lógica de repetição quando certos sistemas respondem com um erro é outra forma de prevenir falhas maiores no sistema.

## Humano no Circuito

Outra forma eficaz de construir sistemas de agentes de IA confiáveis é usar um humano no circuito. Isso cria um fluxo onde os utilizadores podem fornecer feedback aos agentes durante a execução. Os utilizadores essencialmente atuam como agentes num sistema multiagente, fornecendo aprovação ou encerrando o processo em execução.

![Humano no Circuito](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.pt.png)

Aqui está um trecho de código usando AutoGen para mostrar como este conceito é implementado:

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

Construir agentes de IA confiáveis requer um design cuidadoso, medidas de segurança robustas e iteração contínua. Ao implementar sistemas estruturados de meta prompts, compreender ameaças potenciais e aplicar estratégias de mitigação, os desenvolvedores podem criar agentes de IA que sejam seguros e eficazes. Além disso, incorporar uma abordagem de humano no circuito garante que os agentes de IA permaneçam alinhados às necessidades dos utilizadores enquanto minimizam os riscos. À medida que a IA continua a evoluir, manter uma postura proativa em relação à segurança, privacidade e considerações éticas será fundamental para fomentar confiança e fiabilidade em sistemas impulsionados por IA.

### Tem Mais Perguntas sobre Construção de Agentes de IA Confiáveis?

Junte-se ao [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e obter respostas às suas perguntas sobre agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Visão geral de IA responsável</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de modelos de IA generativa e aplicações de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensagens de sistema de segurança</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modelo de Avaliação de Riscos</a>

## Lição Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lição

[Planeamento com Padrão de Design](../07-planning-design/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.