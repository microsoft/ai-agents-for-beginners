[![How to Design Good AI Agents](../../../translated_images/pcm/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Click di image wey dey above to watch video of dis lesson)_

# Tool Use Design Pattern

Tools dey interesting because dem allow AI agents to get wider range of things wey dem fit do. Instead make agent get small set of actions wey e fit perform, by adding tool, agent fit now perform many-many actions. For dis chapter, we go look di Tool Use Design Pattern wey describe how AI agents fit use certain tools to achieve their goals.

## Introduction

For dis lesson, we dey try answer dis questions:

- Wetin be di tool use design pattern?
- Wetin be di use cases wey e fit apply for?
- Wetin be di elements/building blocks wey you need to implement di design pattern?
- Wetin be di special things to consider when you dey use di Tool Use Design Pattern to build better AI agents wey people go trust?

## Learning Goals

After you finish dis lesson, you go fit:

- Define di Tool Use Design Pattern and wetin e mean.
- Identify di use cases wey di Tool Use Design Pattern fit apply for.
- Understand di important elements wey you need to implement di design pattern.
- Recognize wetin you go consider to make sure AI agents wey use dis design pattern go trustable.

## Wetin be di Tool Use Design Pattern?

Di **Tool Use Design Pattern** na to give LLMs di ability to interact with external tools to achieve certain goals. Tools na code wey agent fit run to perform actions. Tool fit be simple function like calculator, or e fit be API call to third-party service like stock price check or weather forecast. For AI agents, tools dem be to help agents run code when dem get **model-generated function calls**.

## Wetin be di use cases wey e fit apply for?

AI Agents fit use tools to finish complex work, find information, or make decisions. Di tool use design pattern dey popular when you need to get dynamic interaction with external systems like databases, web services, or code interpreters. Dis kin ability dey useful for many use cases like:

- **Dynamic Information Retrieval:** Agents fit query external APIs or databases to get up-to-date data (example, you fit query SQLite database make you do data analysis, get stock prices or check weather).
- **Code Execution and Interpretation:** Agents fit run code or scripts to solve maths problems, generate reports, or run simulations.
- **Workflow Automation:** Make work wey repeat or get many steps run automatically by using tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents fit link up with CRM systems, ticketing platforms, or knowledge bases to solve user questions.
- **Content Generation and Editing:** Agents fit use tools like grammar checkers, text summarizers, or content safety evaluators to help for content creation work.

## Wetin be di elements/building blocks wey you need to implement di tool use design pattern?

Dis building blocks dey allow AI agent to perform many different tasks. Make we check di important elements wey you need to implement di Tool Use Design Pattern:

- **Function/Tool Schemas**: Detailed definitions of available tools, e include function name, purpose, parameters wey e need, plus wetin e go return. Dis schemas dey help LLM understand wetin tools dem dey available and how to make correct requests.

- **Function Execution Logic**: E dey govern when and how tools dem go run based on wetin user want and di conversation context. E fit get planning modules, routing systems, or conditional flows wey go decide tool usage based on wetin happen.

- **Message Handling System**: Di parts wey dey control di flow between user inputs, LLM response, tool calls, and di outputs of tools.

- **Tool Integration Framework**: Di system wey join agent to different tools, whether na simple functions or complex external services.

- **Error Handling & Validation**: Systems wey dey manage problems when tool no fit run well, check parameters, and handle unexpected answer dem.

- **State Management**: E dey track conversation context, previous tool uses, and persistent data to keep consistency across many turns of conversation.

Next, make we check Function/Tool Calling more detailed.

### Function/Tool Calling

Function calling na di main way we use make Large Language Models (LLMs) fit interact with tools. You go often see 'Function' and 'Tool' used as one because 'functions' (di blocks of reusable code) na di 'tools' wey agents use do their work. For function code to run, LLM must match user request with di function description. To do dis, schema wey get description of all functions wey available dey send to LLM. Di LLM go pick di best function for di work and go return di function name and arguments. Dem go run the function, e response go send back to LLM, and LLM go use dat info respond to user request.

For developers to implement function calling for agents, you need:

1. LLM model wey support function calling
2. Schema wey get function descriptions
3. Code for each function wey describe

Make we use example of finding current time for city to explain:

1. **Initialize an LLM wey dey support function calling:**

    Not all models dey support function calling, so make sure di LLM wey you dey use get am.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> dey support function calling. We fit start by initializing Azure OpenAI client. 

    ```python
    # Make we start di Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Create a Function Schema**:

    Next, we go define JSON schema wey get function name, description of wetin function do, plus names and descriptions of function parameters.
    We go take dis schema pass am to di client wey we create earlier, along with user request to find di time for San Francisco. Make you note say **tool call** na wetin dem go return, **no be** di final answer to the question. As e talk before, LLM go return name of function wey e choose for di work, plus arguments wey dem go pass to am.

    ```python
    # Di function wey show wetin di model go read
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
  
    # Di first message from user
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask di model make e use di function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Make we process di response wey model give
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **The function code wey e need to run the task:**

    Now wey LLM don choose di function wey dem need run, di code wey dey run the work go implement and execute.
    We fit write di code to get current time for Python. We go still need to write code to extract name and arguments from response_message to get di final result.

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
     # Handle function calls
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
  
      # Second API call: Comot di final response from di model
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

Function Calling na di heart of most, if no be all agent tool use designs, but e fit sometimes hard to implement from scratch.
As we learn for [Lesson 2](../../../02-explore-agentic-frameworks) agentic frameworks dey give us pre-built building blocks to implement tool use.
 
## Tool Use Examples with Agentic Frameworks

Here be some examples of how you fit implement di Tool Use Design Pattern by using different agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> na open-source AI framework for building AI agents. E dey make function calling easy by allowing you to define tools as Python functions with `@tool` decorator. Di framework dey handle di back-and-forth communication between model plus your code. E also give access to pre-built tools like File Search and Code Interpreter through `AzureAIProjectAgentProvider`.

Di diagram below shows how function calling dey work with Microsoft Agent Framework:

![function calling](../../../translated_images/pcm/functioncalling-diagram.a84006fc287f6014.webp)

For Microsoft Agent Framework, tools dey defined as decorated functions. We fit change `get_current_time` function wey we see before to tool by using `@tool` decorator. Di framework go automatically serialize di function plus parameters, create di schema to send to LLM.

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

# Make one agent and run am wit di tool
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> na new agentic framework wey dem design to empower developers to build, deploy, and scale high-quality, extensible AI agents safely without stress to manage compute and storage resources. E dey useful for enterprise applications because e be fully managed service wey get enterprise-grade security.

Compared to developing directly with LLM API, Azure AI Agent Service get some benefits like:

- Automatic tool calling – no need to parse tool call, run tool, and manage di response; all dis dey done server-side now
- Securely managed data – you no need manage your own conversation state, threads go store all di info wey you need
- Ready-made tools – Tools wey you fit use to link with your data sources, like Bing, Azure AI Search, and Azure Functions.

Di tools wey dey Azure AI Agent Service fit divide into two types:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service make us fit use all these tools together as one `toolset`. E dey also use `threads` wey keep track of message history from one conversation.

Imagine say you be sales agent for company wey dem call Contoso. You want build conversational agent wey fit answer questions about your sales data.

Di image below show how you fit use Azure AI Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/pcm/agent-service-in-action.34fb465c9a84659e.webp)

To use any of these tools with di service, we fit create client and define tool or toolset. For practical way, we fit use the Python code below. Di LLM go fit look di toolset and decide if e go use user created function, `fetch_sales_data_using_sqlite_query`, or di pre-built Code Interpreter based on user request.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function wey you fit find inside fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Start toolset
toolset = ToolSet()

# Start function calling agent with the fetch_sales_data_using_sqlite_query function and put am for the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Start Code Interpreter tool and put am for the toolset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wetin be di special things to consider when you dey use di Tool Use Design Pattern to build trustworthy AI agents?

One common worry with SQL wey LLMs generate dynamically be security, especially risk of SQL injection or bad things like deleting or changing di database. Even though dis kain concerns dey valid, you fit control am well by setting correct database access permissions. For most databases, dis mean to set database read-only. For databases like PostgreSQL or Azure SQL, app go get read-only (SELECT) role.

Running the app for secure environment go protect am more. For enterprise cases, data usually dem extract and transform from operational systems to read-only database or data warehouse wey get user-friendly schema. Dis approach make sure data dey safe, optimized for speed and access, and app get limited read-only access.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## You Get More Questions about di Tool Use Design Patterns?

Join di [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, join office hours, and get your AI Agents questions answered.

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
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->