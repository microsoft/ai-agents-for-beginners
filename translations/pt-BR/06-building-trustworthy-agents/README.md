[![Agentes de IA Confiáveis](../../../translated_images/pt-BR/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Construindo Agentes de IA Confiáveis

## Introdução

Esta lição abordará:

- Como criar e implantar agentes de IA seguros e eficazes
- Considerações importantes de segurança ao desenvolver agentes de IA.
- Como manter a privacidade de dados e dos usuários ao desenvolver agentes de IA.

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá como:

- Identificar e mitigar riscos ao criar agentes de IA.
- Implementar medidas de segurança para garantir que os dados e o acesso sejam gerenciados adequadamente.
- Criar agentes de IA que mantenham a privacidade dos dados e ofereçam uma experiência de usuário de qualidade.

## Segurança

Vamos primeiro olhar para a construção de aplicações agenticas seguras. Segurança significa que o agente de IA executa conforme projetado. Como construtores de aplicações agenticas, temos métodos e ferramentas para maximizar a segurança:

### Construindo uma Estrutura de Mensagem do Sistema

Se você já construiu uma aplicação de IA usando Modelos de Linguagem Grande (LLMs), sabe da importância de projetar um prompt de sistema robusto ou mensagem de sistema. Esses prompts estabelecem as regras meta, instruções e diretrizes para como o LLM interagirá com o usuário e os dados.

Para Agentes de IA, o prompt do sistema é ainda mais importante, pois os agentes de IA precisarão de instruções altamente específicas para completar as tarefas que projetamos para eles.

Para criar prompts de sistema escaláveis, podemos usar uma estrutura de mensagem do sistema para construir um ou mais agentes em nossa aplicação:

![Construindo uma Estrutura de Mensagem do Sistema](../../../translated_images/pt-BR/system-message-framework.3a97368c92d11d68.webp)

#### Passo 1: Criar uma Mensagem Meta do Sistema

O meta prompt será usado por um LLM para gerar os prompts do sistema para os agentes que criamos. Projetamos isso como um modelo para que possamos criar múltiplos agentes de forma eficiente, se necessário.

Aqui está um exemplo de uma mensagem meta do sistema que daríamos ao LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Criar um prompt básico

O próximo passo é criar um prompt básico para descrever o agente de IA. Você deve incluir o papel do agente, as tarefas que ele realizará e quaisquer outras responsabilidades do agente.

Aqui está um exemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornecer Mensagem Básica do Sistema para o LLM

Agora podemos otimizar essa mensagem do sistema fornecendo a mensagem meta do sistema como a mensagem do sistema e nossa mensagem básica do sistema.

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

O valor dessa estrutura de mensagem do sistema é poder escalar a criação de mensagens do sistema para múltiplos agentes com mais facilidade, além de melhorar suas mensagens do sistema ao longo do tempo. É raro que você tenha uma mensagem do sistema que funcione na primeira vez para seu caso de uso completo. Ser capaz de fazer pequenos ajustes e melhorias alterando a mensagem básica do sistema e executando-a pelo sistema permitirá que você compare e avalie os resultados.

## Compreendendo Ameaças

Para construir agentes de IA confiáveis, é importante entender e mitigar os riscos e ameaças ao seu agente de IA. Vamos olhar apenas para algumas das diferentes ameaças aos agentes de IA e como você pode planejar e se preparar melhor para elas.

![Compreendendo Ameaças](../../../translated_images/pt-BR/understanding-threats.89edeada8a97fc0f.webp)

### Tarefa e Instrução

**Descrição:** Atacantes tentam alterar as instruções ou objetivos do agente de IA por meio de prompts ou manipulação de entradas.

**Mitigação**: Execute verificações de validação e filtros de entrada para detectar prompts potencialmente perigosos antes que sejam processados pelo agente de IA. Como esses ataques normalmente exigem interação frequente com o agente, limitar o número de turnos em uma conversa é outra forma de prevenir esses tipos de ataques.

### Acesso a Sistemas Críticos

**Descrição**: Se um agente de IA tem acesso a sistemas e serviços que armazenam dados sensíveis, atacantes podem comprometer a comunicação entre o agente e esses serviços. Estes podem ser ataques diretos ou tentativas indiretas de obter informações sobre esses sistemas por meio do agente.

**Mitigação**: Agentes de IA devem ter acesso aos sistemas apenas quando necessário para evitar esses tipos de ataques. A comunicação entre o agente e o sistema também deve ser segura. Implementar autenticação e controle de acesso é outra forma de proteger essas informações.

### Sobrecarga de Recursos e Serviços

**Descrição:** Agentes de IA podem acessar diferentes ferramentas e serviços para completar tarefas. Atacantes podem usar essa capacidade para atacar esses serviços enviando um alto volume de requisições através do agente de IA, o que pode resultar em falhas do sistema ou altos custos.

**Mitigação:** Implemente políticas para limitar o número de requisições que um agente de IA pode fazer a um serviço. Limitar o número de turnos de conversa e requisições ao seu agente de IA é outra forma de prevenir esses tipos de ataques.

### Envenenamento da Base de Conhecimento

**Descrição:** Este tipo de ataque não tem como alvo direto o agente de IA, mas sim a base de conhecimento e outros serviços que o agente usará. Isso pode envolver corromper os dados ou informações que o agente utilizará para completar uma tarefa, levando a respostas tendenciosas ou não intencionais ao usuário.

**Mitigação:** Realize verificações regulares dos dados que o agente de IA usará em seus fluxos de trabalho. Assegure que o acesso a esses dados seja seguro e alterado apenas por indivíduos confiáveis para evitar esse tipo de ataque.

### Erros em Cascata

**Descrição:** Agentes de IA acessam várias ferramentas e serviços para completar tarefas. Erros causados por atacantes podem levar a falhas em outros sistemas aos quais o agente está conectado, causando a propagação do ataque, tornando-o mais amplo e difícil de solucionar.

**Mitigação**: Um método para evitar isso é fazer com que o agente de IA opere em um ambiente limitado, como executar tarefas em um contêiner Docker, para prevenir ataques diretos ao sistema. Criar mecanismos de fallback e lógica de retentativas quando certos sistemas respondem com erro é outra forma de evitar falhas sistêmicas maiores.

## Humano no Loop

Outra forma eficaz de construir sistemas de agentes de IA confiáveis é usar um humano no loop. Isso cria um fluxo onde os usuários podem fornecer feedback aos agentes durante a execução. Os usuários essencialmente atuam como agentes em um sistema multiagente, fornecendo aprovação ou terminando o processo em execução.

![Humano no Loop](../../../translated_images/pt-BR/human-in-the-loop.5f0068a678f62f4f.webp)

Aqui está um trecho de código usando o Microsoft Agent Framework para mostrar como esse conceito é implementado:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Crie o provedor com aprovação humana no processo
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Crie o agente com uma etapa de aprovação humana
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# O usuário pode revisar e aprovar a resposta
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusão

Construir agentes de IA confiáveis requer design cuidadoso, medidas robustas de segurança e iteração contínua. Ao implementar sistemas estruturados de meta prompts, compreender ameaças potenciais e aplicar estratégias de mitigação, os desenvolvedores podem criar agentes de IA que sejam seguros e eficazes. Além disso, incorporar uma abordagem de humano no loop garante que os agentes de IA permaneçam alinhados às necessidades dos usuários, minimizando riscos. À medida que a IA continua a evoluir, manter uma postura proativa em segurança, privacidade e considerações éticas será fundamental para fomentar confiança e confiabilidade em sistemas guiados por IA.

### Tem Mais Perguntas sobre Construir Agentes de IA Confiáveis?

Junte-se ao [Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de plantões de dúvidas e tirar suas perguntas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Visão geral de IA Responsável</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de modelos de IA generativa e aplicações de IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensagens de sistema de segurança</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modelo de Avaliação de Riscos</a>

## Lição Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lição

[Design Pattern de Planejamento](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->