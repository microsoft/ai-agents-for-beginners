[![Agentes de IA Confiáveis](../../../translated_images/pt-BR/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

# Construindo Agentes de IA Confiáveis

## Introdução

Esta lição abordará:

- Como construir e implantar Agentes de IA seguros e eficazes
- Considerações importantes de segurança ao desenvolver Agentes de IA.
- Como manter a privacidade dos dados e dos usuários ao desenvolver Agentes de IA.

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá como:

- Identificar e mitigar riscos na criação de Agentes de IA.
- Implementar medidas de segurança para garantir que os dados e acessos sejam gerenciados corretamente.
- Criar Agentes de IA que mantenham a privacidade dos dados e proporcionem uma experiência de usuário de qualidade.

## Segurança

Vamos primeiro analisar como construir aplicações agentivas seguras. Segurança significa que o agente de IA atua conforme foi projetado. Como construtores de aplicações agentivas, temos métodos e ferramentas para maximizar a segurança:

### Construindo uma Estrutura de Mensagem de Sistema

Se você já construiu uma aplicação de IA usando Grandes Modelos de Linguagem (LLMs), sabe a importância de projetar um prompt robusto ou mensagem de sistema. Esses prompts estabelecem as regras meta, instruções e diretrizes para como o LLM irá interagir com o usuário e os dados.

Para agentes de IA, o prompt do sistema é ainda mais importante, pois os agentes precisarão de instruções altamente específicas para completar as tarefas que projetamos para eles.

Para criar prompts de sistema escaláveis, podemos usar uma estrutura de mensagem de sistema para construir um ou mais agentes em nossa aplicação:

![Construindo uma Estrutura de Mensagem de Sistema](../../../translated_images/pt-BR/system-message-framework.3a97368c92d11d68.webp)

#### Passo 1: Criar uma Mensagem de Sistema Meta

O prompt meta será usado por um LLM para gerar os prompts de sistema para os agentes que criamos. Projetamos isso como um modelo para que possamos criar vários agentes de maneira eficiente, se necessário.

Aqui está um exemplo de uma mensagem de sistema meta que forneceríamos ao LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Criar um prompt básico

O próximo passo é criar um prompt básico para descrever o Agente de IA. Você deve incluir a função do agente, as tarefas que ele realizará e quaisquer outras responsabilidades do agente.

Aqui está um exemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornecer Mensagem de Sistema Básica ao LLM

Agora podemos otimizar esta mensagem de sistema fornecendo a mensagem meta do sistema como a mensagem de sistema juntamente com nossa mensagem de sistema básica.

Isso produzirá uma mensagem de sistema melhor projetada para guiar nossos agentes de IA:

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

O valor dessa estrutura de mensagens de sistema é poder escalar a criação de mensagens de sistema para múltiplos agentes com mais facilidade, além de melhorar suas mensagens de sistema ao longo do tempo. É raro que você tenha uma mensagem de sistema que funcione perfeitamente na primeira tentativa para todo seu caso de uso completo. Poder fazer pequenos ajustes e melhorias alterando a mensagem básica do sistema e rodando-a através do sistema permitirá que você compare e avalie os resultados.

## Entendendo Ameaças

Para construir agentes de IA confiáveis, é importante entender e mitigar os riscos e ameaças ao seu agente de IA. Vamos ver apenas algumas das diferentes ameaças aos agentes de IA e como você pode se planejar e preparar melhor para elas.

![Entendendo Ameaças](../../../translated_images/pt-BR/understanding-threats.89edeada8a97fc0f.webp)

### Tarefa e Instrução

**Descrição:** Invasores tentam mudar as instruções ou objetivos do agente de IA por meio de prompts ou manipulação de entradas.

**Mitigação**: Execute verificações de validação e filtros de entrada para detectar prompts potencialmente perigosos antes que sejam processados pelo Agente de IA. Como esses ataques geralmente requerem interações frequentes com o agente, limitar o número de turnos em uma conversa é outra forma de evitar esses tipos de ataques.

### Acesso a Sistemas Críticos

**Descrição**: Se um agente de IA tem acesso a sistemas e serviços que armazenam dados sensíveis, invasores podem comprometer a comunicação entre o agente e esses serviços. Podem ser ataques diretos ou tentativas indiretas de obter informações sobre esses sistemas por meio do agente.

**Mitigação**: Agentes de IA devem ter acesso aos sistemas apenas quando necessário para prevenir esses tipos de ataques. A comunicação entre agente e sistema também deve ser segura. Implementar autenticação e controle de acesso é outra forma de proteger essas informações.

### Sobrecarga de Recursos e Serviços

**Descrição:** Agentes de IA podem acessar diferentes ferramentas e serviços para completar tarefas. Invasores podem usar essa capacidade para atacar esses serviços enviando um alto volume de solicitações por meio do agente, o que pode resultar em falhas no sistema ou custos elevados.

**Mitigação:** Implemente políticas para limitar o número de solicitações que um agente de IA pode fazer a um serviço. Limitar o número de turnos e solicitações em sua conversa com o agente é outra forma de prevenir esses ataques.

### Envenenamento da Base de Conhecimento

**Descrição:** Esse tipo de ataque não mira diretamente no agente de IA, mas sim na base de conhecimento e outros serviços que o agente usará. Pode envolver corromper os dados ou informações que o agente usará para concluir uma tarefa, levando a respostas tendenciosas ou não intencionais ao usuário.

**Mitigação:** Realize verificações regulares dos dados que o agente de IA utilizará em seus fluxos de trabalho. Garanta que o acesso a esses dados seja seguro e que as alterações sejam feitas apenas por pessoas confiáveis para evitar esse tipo de ataque.

### Erros em Cascata

**Descrição:** Agentes de IA acessam várias ferramentas e serviços para realizar tarefas. Erros causados por invasores podem levar a falhas em outros sistemas conectados ao agente, fazendo com que o ataque se espalhe e se torne mais difícil de diagnosticar.

**Mitigação**: Um método para evitar isso é fazer o agente operar em um ambiente limitado, como realizar tarefas em um container Docker, para prevenir ataques diretos ao sistema. Criar mecanismos de fallback e lógica de tentativas ao receber erros de certos sistemas é outra forma de prevenir falhas maiores.

## Humano no Loop

Outra forma eficaz de construir sistemas de Agentes de IA confiáveis é utilizando um Humano no loop. Isso cria um fluxo em que os usuários podem fornecer feedback aos agentes durante a execução. Os usuários atuam essencialmente como agentes em um sistema multiagente, aprovando ou interrompendo o processo em andamento.

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

Construir agentes de IA confiáveis requer design cuidadoso, medidas de segurança robustas e iteração contínua. Ao implementar sistemas estruturados de meta prompting, entender ameaças potenciais e aplicar estratégias de mitigação, os desenvolvedores podem criar agentes de IA que sejam seguros e eficazes. Além disso, incorporar uma abordagem humano no loop garante que os agentes de IA permaneçam alinhados com as necessidades dos usuários enquanto minimizam riscos. À medida que a IA continua evoluindo, manter uma postura proativa em segurança, privacidade e considerações éticas será fundamental para fomentar confiança e confiabilidade em sistemas baseados em IA.

### Tem Mais Perguntas sobre Construir Agentes de IA Confiáveis?

Junte-se ao [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para encontrar outros aprendizes, participar de horas de atendimento e obter respostas para suas perguntas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Visão geral da IA responsável</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de modelos e aplicações de IA generativa</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensagens de sistema para segurança</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template de Avaliação de Riscos</a>

## Lição Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Lição

[Padrão de Design de Planejamento](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->