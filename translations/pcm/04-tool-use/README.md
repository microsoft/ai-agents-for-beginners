[![How to Design Good AI Agents](../../../translated_images/pcm/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Click di picture wey dey top na so to watch video for dis lesson)_

# Tool Use Design Pattern

Tools dey interesting because dem dey allow AI agents to get beta range of things dem fit do. Instead make di agent get small small action dem fit do, if you add tool, di agent fit do plenty different actions. For dis chapter, we go look di Tool Use Design Pattern, wey dey talk how AI agents fit use specific tools to achieve dia goals.

## Introduction

For dis lesson, we wan answer dis questions:

- Wetin be di tool use design pattern?
- For which kain cases e fit apply?
- Wetin be di elements/building blocks wey you need to take implement di design pattern?
- Wetin be di special things wey you for consider when you dey use di Tool Use Design Pattern to build AI agents wey people fit trust?

## Learning Goals

After you finish dis lesson, you go fit:

- Define Wetin be di Tool Use Design Pattern and why e dey.
- Identify cases wey you fit use di Tool Use Design Pattern.
- Understand di main elements wey you go need to implement di design pattern.
- Recognize wetin to consider to make sure AI agents wey use dis design pattern dey trustworthy.

## Wetin be di Tool Use Design Pattern?

Di **Tool Use Design Pattern** dey focus on how to give LLMs power to dey interact with external tools to make dem fit achieve specific goals. Tools na code wey agent fit run make e perform actions. Tool fit be simple function like calculator, or e fit be API call go third-party service like check stock price or weather forecast. For AI agents matter, tools dem dey designed to run when agents see **model-generated function calls**.

## For which cases you fit use am?

AI Agents fit use tools do complex work, find information, or make decisions. Di tool use design pattern dey popular for situations wey require to dey interact with external systems dynamically, like databases, web services, or code interpreters. Dis kind power useful for different cases like:

- **Dynamic Information Retrieval:** Agents fit ask external APIs or databases to get current data (like SQLite database query for data, or check stock price or weather).
- **Code Execution and Interpretation:** Agents fit run code or scripts to solve math wahala, generate reports, or run simulations.
- **Workflow Automation:** Make repetitive or multi-step work automatically with tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents fit work with CRM systems, ticketing platforms, or knowledge bases to solve user questions.
- **Content Generation and Editing:** Agents fit use tools like grammar checkers, text summarizers, or content safety evaluators to help create content.

## Wetin be di elements/building blocks wey you go need for di tool use design pattern?

Dis building blocks go help AI agent perform plenty tasks. Make we check di main elements wey you go need for di Tool Use Design Pattern:

- **Function/Tool Schemas**: Exact description of tools wey dey available, including function name, reason for am, parameters wey e need, and output wey people expect. Dis schemas dey help LLM sabi which tools dey and how to create correct requests.

- **Function Execution Logic**: How and when tools dey call based on wetin user want and conversation context. E fit get planner modules, routing systems, or conditional flows wey dey decide how tools go run dynamically.

- **Message Handling System**: Di parts wey manage conversation flow between user inputs, LLM responses, tool calls, and tool outputs.

- **Tool Integration Framework**: Infrastructure wey connect agent to different tools, whether na simple functions or big external services.

- **Error Handling & Validation**: Ways to handle failure when tool no work, check parameters, and fix unexpected responses.

- **State Management**: E dey track conversation context, previous tool uses, and persistent data to make sure everything consistent for multi-turn interaction.

Next, make we check Function/Tool Calling well well.

### Function/Tool Calling

Function calling na di main way we dey enable Large Language Models (LLMs) to interact with tools. You go sabi see 'Function' and 'Tool' dey used like say dem be one because 'functions' (blocks of reusable code) na di 'tools' wey agents dey use to do things. For function code make e run, LLM must compare wetin user ask with how di function dey described. To take do dis, schema wey get all function description go send to LLM. LLM go then select di best function for di work, and e go return di function name and arguments. Di selected function go run, e reply go come back to di LLM, wey go use dat info settle user request.

For developers to implement function calling for agents, you need:

1. LLM model wey fit function calling
2. Schema wey get function description
3. Code wey fit run each function wey dem describe

Make we use example of to get current time for one city to explain:

1. **Initialize LLM wey support function calling:**

    No all models support function calling, so e important to check say di LLM wey you dey use fit do am. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> dey support function calling. We fit start by initializing di Azure OpenAI client.

    ```python
    # Start di Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Create Function Schema**:

    Next we go define JSON schema wey get function name, function description, plus di names and descriptions of di function parameters.
    Then we go send dis schema plus di user request to di client we don create before, like make we find time for San Francisco. Wetin important to know be say, di **tool call** na di thing wey go come back, **no be** di final answer to di question. Like we talk before, LLM go return function name wey e pick for di work, and di arguments wey e go pass.

    ```python
    # Function description wey di model go read
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
  
    # Di first message wey user send
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask di model make e use di function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process di response wey di model give
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Function code wey go carry out di work:**

    Now wey LLM don select which function to run, di code wey go run di work must dey implemented and executed.
    We fit write code to get current time for Python. We go also write code to extract function name and arguments from response_message to get final answer.

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
     # Handle how una dey call function
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
  
      # Second API call: Comot the last answer from the model
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

Function Calling na heart of most, if no be all agent tool use design, but sometimes to implement am from scratch fit hard.
Like we learn for [Lesson 2](../../../02-explore-agentic-frameworks) agentic frameworks dey give us pre-built building blocks to implement tool use.
 
## Tool Use Examples with Agentic Frameworks

Here some examples how you fit implement di Tool Use Design Pattern with different agentic frameworks:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> na open-source AI framework for .NET, Python, and Java developers wey dey work with Large Language Models (LLMs). E dey make function calling easy by automatically dey describe your functions and their parameters to di model via <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. E also dey manage di back-and-forth communication between di model and your code. Another advantages to use agentic framework like Semantic Kernel na say e allow you to use pre-built tools like <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> and <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Di diagram below dey show how function calling with Semantic Kernel dey go:

![function calling](../../../translated_images/pcm/functioncalling-diagram.a84006fc287f6014.webp)

For Semantic Kernel functions/tools na <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> dem dey call am. We fit change di `get_current_time` function wey we see before into plugin by turning am into class wey get di function inside. We fit also import di `kernel_function` decorator, wey dey take description of di function. When you create kernel with GetCurrentTimePlugin, di kernel go automatically serialize di function and parameters, for create schema to send go LLM.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Make di kernel
kernel = Kernel()

# Make di plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add di plugin go inside di kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> na new agentic framework wey design make developers fit build, deploy, and scale high-quality and extensible AI agents wey secure, without to worry about managing underlying compute and storage resources. E sef good wella for enterprise applications because na fully managed service with enterprise grade security.

Compared to just developing with LLM API direct, Azure AI Agent Service get advantages like:

- Automatic tool calling – you no need to parse tool call, run tool, and handle response; all these na server side dem dey do now
- Securely managed data – instead make you manage your own conversation state, you fit use threads to store all info you need
- Out-of-the-box tools – Tools wey you fit use to work with your data sources, like Bing, Azure AI Search, and Azure Functions.

Tools wey dey available for Azure AI Agent Service fit divided into two groups:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service allow us to fit use all these tools together as `toolset`. E also dey use `threads` to keep track of message history from one kain conversation.

Imagine say you be sales agent for company wey dem call Contoso. You want create conversational agent wey fit answer questions about your sales data.

Picture below explain how you fit use Azure AI Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/pcm/agent-service-in-action.34fb465c9a84659e.webp)

To use any of dis tools with di service, we fit create client and define tool or toolset. For practical implementation we fit use this Python code. LLM go fit check di toolset make e decide whether to use user created function, `fetch_sales_data_using_sqlite_query`, or di pre-built Code Interpreter base on wetin user request.

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

# Make toolset ready
toolset = ToolSet()

# Make function calling agent ready wit the fetch_sales_data_using_sqlite_query function and join am for the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Make Code Interpreter tool ready and join am for the toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wetin be di special things to consider to build trustworthy AI agents using Tool Use Design Pattern?

One common worry about SQL wey LLMs generate dynamically na security, especially risk of SQL injection or bad bad actions like dropping or tampering database. Even though dis concerns dey real, dem fit reduce well well if database access permissions set well. For most databases, you fit set am as read-only. For database services like PostgreSQL or Azure SQL, app go get read-only (SELECT) role.
Running di app for secure environment go make protection beta. For enterprise situations, dem dey usually comot and change data from operational systems put am inside read-only database or data warehouse wey get user-friendly schema. Dis method dey make sure say di data secure, e dey optimized for performance and accessibility, plus di app get limited, read-only access.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join di [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you sabi say automated translation fit get some yawa or mistake inside. Di original document wey dem write for dia own language na im be di original true version. If na serious tin, make you find professional person wey sabi do human translation. We no go take any blame if person misunderstand or misinterpret anything because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->