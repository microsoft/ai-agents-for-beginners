[![How to Design Good AI Agents](../../../translated_images/pcm/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik di piksha we de ontop so to watch video for dis leson)_

# Tool Use Design Pattern

Tools dey interesting becos dem dey allow AI agents make dem get plenty kain tin wey dem fit do. E no be say the agent get small amount of tins wey e fit do, but if you add tool, the agent fit do plenty tins. For dis chapter, we go check Tool Use Design Pattern, wey dey explain how AI agents fit use correct tools take achieve their goals.

## Introduction

For dis leson, we want answer di tins dem:

- Wetin be the tool use design pattern?
- Wetin be di kain uses we fit use am for?
- Wetin be di elements/building blocks wey we need make we fit implement the design pattern?
- Wetin be di special tins we gats consider wen we dey use Tool Use Design Pattern make AI agents wey we fit trust?

## Learning Goals

After you don finish dis leson, you go fit:

- Explain Tool Use Design Pattern and im work.
- Identify di kain uses we Tool Use Design Pattern fit do well for.
- Understand di main elements wey dem need to do di design pattern.
- Know wetin make AI agents wey dey use dis design pattern trustworthy.

## Wetin be the Tool Use Design Pattern?

The **Tool Use Design Pattern** na how we dey give LLMs power to interact with tools wey dey outside make dem fit achieve particular goals. Tools na code wey agent fit run to do certain actions. Tool fit be simple function like calculator, or e fit be API call to another service like checking stock price or weather forecast. For AI agents matter, tools na wetin agent go run after **model-generated function calls**.

## Wetin be di use cases wey e fit apply?

AI Agents fit use tools to finish complex work, find information, or make decisions. The tool use design pattern dey usually used when dynamic interaction with outside system like databases, web services, or code interpreters. Dis kain ability dey useful for many diff kinds cases like:

- **Dynamic Information Retrieval:** Agents fit ask outside APIs or databases to get fresh data (e.g., ask SQLite database for analysis, fetch stock price or weather info).
- **Code Execution and Interpretation:** Agents fit run code or scripts solve maths problem, generate reports, or do simulations.
- **Workflow Automation:** Make repetitive or multi-step workflow automatic by joining tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents fit work with CRM system, ticketing platform, or knowledge base to answer user questions.
- **Content Generation and Editing:** Agents fit use tools like grammar check, text summarizers, or content safety tools to help write content well.

## Wetin be di elements/building blocks wey dem need to do di tool use design pattern?

Dis building blocks dey allow AI agent fit do many tasks. Make we look di main tins wey we need to do Tool Use Design Pattern:

- **Function/Tool Schemas**: Detailed definition of tools wey dey available, including function name, wetin e dey do, parameters wey e need, plus wetin e go return. These schemas go help LLM sabi which tools dem get and how to do correct request.

- **Function Execution Logic**: How and wen tools go dey called based on wetin user want and conversation context. E fit get planner modules, routing, or conditional flow wey decide how to use tool for correct time.

- **Message Handling System**: Parts wey dey control conversation flow between user talk, LLM response, tool calls, and tool answer dem.

- **Tool Integration Framework**: Infrastructure wey connect agent with different tools, whether na simple functions or complex outside services.

- **Error Handling & Validation**: Ways to manage when tool no work well, check parameters, and manage unexpected answers.

- **State Management**: Keep track of conversation context, past tool calls, and maintain data across multiple turns.

Next, make we look Function/Tool Calling more inside.

### Function/Tool Calling

Function calling na main way we take enable Large Language Models (LLMs) to interact with tools. You go often see 'Function' and 'Tool' dey used like say na the same thing because 'functions' (block of code wey you fit use many times) na 'tools' wey agents dey use to do work. To run function code, LLM must compare user request with function description. To do dis, we send schema wey get all function description to LLM. Then LLM go pick best function for di work and return im name plus arguments. The chosen function go run, response go return to LLM, then LLM go use am respond to user.

For developers to implement function calling for agents, you need:

1. One LLM model wey dey support function calling
2. Schema wey get function descriptions
3. Code for every function wey dem describe

Make we use example of getting current time for one city to explain:

1. **Initialize LLM wey fit do function calling:**

    No all models fit do function calling, e important to check whether di LLM wey you dey use fit do am. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fit function calling. We fit start with Azure OpenAI client.

    ```python
    # Make we start di Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Make Function Schema:**

    Next, we go define JSON schema wey get function name, description of wetin function dey do, plus names and description of parameters.
    We go carry dis schema give di client we create before, plus user request to find time for San Francisco. Wetin we gats remember be say **tool call** na wetin go return, **no** be di final answer to question. As we talk before, LLM na e go return function name wey e pick and arguments wey e go pass.

    ```python
    # Function tok for di model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Di first message wey di user send
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Di first API call: Make di model use di function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Make we process wetin di model come reply
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Function code wey go run the task:**

    Now say LLM don pick which function to run, we need implement and run the code wey go carry out the work.
    We fit write code to get current time inside Python. We go also write code to take name and arguments from response_message to get final result.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Manage how function dem de call
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Make we collect the last response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Function Calling na heart of most, if no be all agent tool use design, but e fit hard sometimes to implement am from scratch.
As we learn for [Lesson 2](../../../02-explore-agentic-frameworks), agentic frameworks dey give us pre-built building blocks to implement tool use.
 
## Tool Use Examples with Agentic Frameworks

Here na some examples how you fit implement Tool Use Design Pattern using different agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> na open-source AI framework to build AI agents. E make function calling easy by letting you define tools as Python functions using `@tool` decorator. Di framework dey handle communication between model and your code. E also give access to pre-built tools like File Search and Code Interpreter through `AzureAIProjectAgentProvider`.

The diagram below show how function calling dey work with Microsoft Agent Framework:

![function calling](../../../translated_images/pcm/functioncalling-diagram.a84006fc287f6014.webp)

For Microsoft Agent Framework, tools dem be decorated functions. We fit change `get_current_time` function wey we see before to tool by using `@tool` decorator. Di framework go serialize function and im parameters, and create schema to send to LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Make di client
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Make one agent an run am wit di tool
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> na new agentic framework wey dey empower developers to build, deploy, and scale high-quality, extensible AI agents safely without managing compute and storage resources. E good wella for enterprise apps as e get full managed service with enterprise grade security.

Compared to developing directly with LLM API, Azure AI Agent Service get some better things, including:

- Automatic tool calling – you no need parse tool call, run tool, handle response; all dis dey done server-side
- Securely managed data – no need manage your own conversation state, threads go keep all info you need
- Out-of-the-box tools – Tools wey fit interact with your data sources, like Bing, Azure AI Search, and Azure Functions.

Tools wey dey inside Azure AI Agent Service fit be two kinds:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service allow make we fit use all these tools together as one `toolset`. E also use `threads` to keep history of messages from the conversation.

Imagine say you be sales agent for company wey name na Contoso. You want build conversational agent wey fit answer questions about your sales data.

The picture below show how you fit use Azure AI Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/pcm/agent-service-in-action.34fb465c9a84659e.webp)

To use any of these tools with service, we fit create client then define tool or toolset. To implement this plis we fit use Python code below. LLM go fit check toolset and decide whether to use user created function, `fetch_sales_data_using_sqlite_query`, or pre-built Code Interpreter depending on user request.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function wey you fit find for fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Set up tool dem
toolset = ToolSet()

# Set up function calling agent with the fetch_sales_data_using_sqlite_query function and add am join toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Set up Code Interpreter tool and add am join toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wetin dem gats consider special when you dey use Tool Use Design Pattern to build trustworthy AI agents?

One big worry be SQL wey LLM dey generate dynamically, especially security risks like SQL injection or bad tins wey fit happun, like drop or change database. Even though dis worry dey real, you fit reduce am well by setting database access permissions correct. For most databases, you fit set am as read-only. For database services like PostgreSQL or Azure SQL, the app suppose get read-only (SELECT) role.

If you run app inside secure environment, e go give better protection. For enterprise side, data normally dey extracted and transformed from working systems into read-only database or data warehouse with user-friendly schema. Dis way data dey protected, optimized for performance and access, plus app get limited read-only access.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## You get More Questions about Tool Use Design Patterns?

Join [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, join office hours and get your AI Agents questions well answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**: 
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg make you sabi say automatic translation fit get some error or wahala. Di original document wey dey dia language be di main correct one. If na important info, e better make person wey sabi human translation do am. We no go take responsibility if person no understand or get wrong meaning as dem use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->