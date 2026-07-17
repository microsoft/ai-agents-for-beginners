[![How to Design Good AI Agents](../../../translated_images/pcm/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Click di pikshua we dey up dia for watch video of dis lesson)_

# Tool Use Design Pattern

Tools dey interesting because dem dey allow AI agents make dem get more plenty tins dem fit do. Instead make di agent get only few actions e fit do, if you add tool, e fit do plenty actions now. For dis chapter, we go look di Tool Use Design Pattern, wey dey show how AI agents fit use special tools take achieve dia goals.

## Introduction

For dis lesson, we wan find answer to these questions:

- Wetin be di tool use design pattern?
- Di tins we fit use am for?
- Di parts/wey dem go use build am?
- Wetin special wey we gots consider if we wan use Tool Use Design Pattern for build AI agents wey people go fit trust?

## Learning Goals

After you finish dis lesson, you go fit:

- Define Wetin be Tool Use Design Pattern and di reason why e dey.
- Identify tins we fit use di Tool Use Design Pattern for.
- Understand di main tins we need take build di design pattern.
- Know wetin dem suppose consider so dat di AI agents wey use dis design pattern go dey trustworthy.

## Wetin be di Tool Use Design Pattern?

Di **Tool Use Design Pattern** focus on make LLMs fit interact wit tools outside dem self to achieve exact goals. Tools be code wey agent fit run to do actions. Tool fit be simple function like calculator, or API call to third-party service like look stock price or weather forecast. For AI agents matter, tools dem dey designed make agents fit run dem when **model generate function calls**.

## Wetin dem fit use am for?

AI Agents fit take tools do complicated work, find information, or make decisions. Tool use design pattern dem dey use wella when you need make e interact well wit external things like database, web services, or code interpreters. Dis ability dey important for many use cases like:

- **Dynamic Information Retrieval:** Agents fit ask external APIs or databases for better information (like, ask sqlite database for data analysis, find stock price or weather info).
- **Code Execution and Interpretation:** Agents fit run code or scripts to solve math problem, make report, or do simulations.
- **Workflow Automation:** Make repetitive or many-step workflows automatic by joining tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents fit interact wit CRM systems, ticket platforms, or knowledge bases to answer user question.
- **Content Generation and Editing:** Agents fit use tools like grammar checkers, text summarizers, or content safety checkers to help for content creation work.

## Wetin be di parts we need take build di tool use design pattern?

All dis parts go allow AI agent do plenty tins. Make we check di main tins we need take build Tool Use Design Pattern:

- **Function/Tool Schemas**: Detailed definition of tools wey dey, including function name, wetin e suppose do, wetin parameters e need, and wetin e go return. Dis schemas dey make LLM sabi which tools dey and how to create proper requests.

- **Function Execution Logic**: Na dis one dey control when and how dem go call tools based on wetin user want and di gist context. E fit get planner modules, routing systems, or condition flows wey dey decide how to use tool.

- **Message Handling System**: Tins wey dey manage di conversation flow between user input, LLM response, tool calls, and tool output.

- **Tool Integration Framework**: Di system wey connect agents to different tools, whether na simple functions or big outside services.

- **Error Handling & Validation**: Tins wey dey catch tool execution failure, check parameters, and manage surprise response.

- **State Management**: Keep eye for conversation history, past tool usage, and data wey need to stay consistent for multi-turn interactions.

Next, make we check Function/Tool Calling well well.
 
### Function/Tool Calling

Function calling na main way we take let Large Language Models (LLMs) fit interact wit tools. You fit see 'Function' and 'Tool' mean are same because 'functions' (blocks of reusable code) be di 'tools' wey agents dey use to do work. To make function code run, LLM must compare user request with function description. For dis one, schema wey get all function description go send to LLM. Then LLM go pick di best function for di work, return e name and arguments. Di chosen function go run, e response go come back to LLM, wey go use am answer user request.

For developer wen wan build function calling for agents, you go need:

1. LLM model wey support function calling
2. Schema wey get function description
3. Code for every function wey dem describe

Make we use example of find current time for city to explain:

1. **Start LLM wey support function calling:**

    No all models support function calling, so make sure say di LLM wey you dey use get am.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> dey support function calling. We fit start by open OpenAI client for Azure OpenAI **Responses API** (stable `/openai/v1/` endpoint — no `api_version` needed). 

    ```python
    # Start di OpenAI client for Azure OpenAI (Responses API, v1 endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Create Function Schema**:

    Next, we go define JSON schema wey get function name, description, and parameters name and description.
    We go pass dis schema to client wey we create before, plus user request say make e find time for San Francisco. Wetin important to know be say **tool call** be wetin you go get back, **no na** final answer to question. Like we talk before, LLM go return name of function wey e pick for task, and arguments wey e go use.

    ```python
    # Function tok say how di model go read (Responses API flat tool format)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # First API call: Ask di model make e use di function
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Di Responses API dey return tool calls as function_call items inside response.output.
    # Add dem join di conversation make di model get complete context for di next turn.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Function code wey go do di work:**

    Now say LLM don pick di function to run, e code wey go do di work must dey implement and run.
    We fit write code to find current time for Python. We also need write code to take name and arguments from response_message to get final result.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Return the tool result as a function_call_output item
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Second API call: Get the final response from the model
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Function Calling na di main ting for most agent tool use design, but building am from scratch fit be challenge sometimes.
As we learn for [Lesson 2](../../../02-explore-agentic-frameworks) agentic frameworks dey give us pre-made building blocks to take use the tool use.
 
## Tool Use Examples wit Agentic Frameworks

Here na some examples how you fit use Tool Use Design Pattern wit different agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> na open-source AI framework to build AI agents. E make am easy to use function calling by allowing you define tools as Python functions wit `@tool` decorator. Di framework dey handle communication between di model and your code. E also give access to pre-made tools like File Search and Code Interpreter through `FoundryChatClient`.

Below diagram show how function calling dey work wit Microsoft Agent Framework:

![function calling](../../../translated_images/pcm/functioncalling-diagram.a84006fc287f6014.webp)

For Microsoft Agent Framework, tools dey define as decorated functions. We fit turn `get_current_time` function we see earlier into tool by using `@tool` decorator. Di framework go automatically serialize di function and parameters, create schema to send to LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Make di client
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Make one agent and run am wit di tool
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> na recent agentic framework wey dey help developers build, deploy, and scale strong, extensible AI agents without wahala of managing di underlying compute and storage. E good for enterprise applications because na full managed service wit top level security.

Compared to direct LLM API development, Microsoft Foundry Agent Service get advantage like:

- Automatic tool calling – no need to parse tool call, run tool, and manage response; all dis dey done server-side now
- Securely manage data – instead of you manage your own conversation state, you fit use threads to keep info you need
- Ready-to-use tools – Tools wey fit interact wit your data sources like Bing, Azure AI Search, and Azure Functions.

Tools wey dey Microsoft Foundry Agent Service fit divide into two:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding wit Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service allow us to fit use all dis tools together as `toolset`. E also use `threads` wey go keep history of messages for each conversation.

Imagine say you be sales agent for company wey dem call Contoso. You wan build conversational agent we fit answer questions about your sales data.

Dis picture show how you fit take Microsoft Foundry Agent Service analyze your sales data:

![Agentic Service In Action](../../../translated_images/pcm/agent-service-in-action.34fb465c9a84659e.webp)

To use any of these tools wit di service, we fit create client and define tool or toolset. To do am for real, we fit use dis Python code. LLM go fit check di toolset and decide to use user made function, `fetch_sales_data_using_sqlite_query`, or built-in Code Interpreter based on user request.

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

# Start function calling agent wit the fetch_sales_data_using_sqlite_query function make e join the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Start Code Interpreter tool make e join the toolset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wetin special we gots consider if we wan use the Tool Use Design Pattern to build trustworthy AI agents?

One common palava with SQL wey LLMs dey create dynamically be security, especially risk of SQL injection or malicious things like dropping or messing with database. Even though dis concerns dey real, you fit protect well by setting database access correctly. For most databases, e mean to set am as read-only. For PostgreSQL or Azure SQL, assign app read-only (SELECT) role.

Run di app for secure environment go also protect well. For enterprise setting, data dey usually come from operational systems turn read-only database or data warehouse wit easy-to-use schema. Dis way, data go dey safe, fast and easy to reach, plus app go only get small read-only access.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## You get more questions about Tool Use Design Patterns?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answer.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>


## Smoke-Test Dis Agent (Optional)

After you don sabi how to deploy agents for [Lesson 16](../16-deploying-scalable-agents/README.md), you fit smoke-test dis lesson `TravelToolAgent` (e still dey call im tools and answer?) wit [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). See [`tests/README.md`](../tests/README.md) to sabi how to run am.

## Lesson We Don Do Before

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->