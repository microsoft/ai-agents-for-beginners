[![How to Design Good AI Agents](../../../translated_images/en/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Click the image above to view video of this lesson)_

# Tool Use Design Pattern

Tools are interesting because they allow AI agents to have a broader range of capabilities. Instead of the agent having a limited set of actions it can perform, by adding a tool, the agent can now perform a wide range of actions. In this chapter, we will look at the Tool Use Design Pattern, which describes how AI agents can use specific tools to achieve their goals.

## Introduction

In this lesson, we're looking to answer the following questions:

- What is the tool use design pattern?
- What are the use cases it can be applied to?
- What are the elements/building blocks needed to implement the design pattern?
- What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

## Learning Goals

After completing this lesson, you will be able to:

- Define the Tool Use Design Pattern and its purpose.
- Identify use cases where the Tool Use Design Pattern is applicable.
- Understand the key elements needed to implement the design pattern.
- Recognize considerations for ensuring trustworthiness in AI agents using this design pattern.

## What is the Tool Use Design Pattern?

The **Tool Use Design Pattern** focuses on giving LLMs the ability to interact with external tools to achieve specific goals. Tools are code that can be executed by an agent to perform actions. A tool can be a simple function such as a calculator, or an API call to a third-party service such as stock price lookup or weather forecast. In the context of AI agents, tools are designed to be executed by agents in response to **model-generated function calls**.

## What are the use cases it can be applied to?

AI Agents can leverage tools to complete complex tasks, retrieve information, or make decisions. The tool use design pattern is often used in scenarios requiring dynamic interaction with external systems, such as databases, web services, or code interpreters. This ability is useful for a number of different use cases including:

- **Dynamic Information Retrieval:** Agents can query external APIs or databases to fetch up-to-date data (e.g., querying a SQLite database for data analysis, fetching stock prices or weather information).
- **Code Execution and Interpretation:** Agents can execute code or scripts to solve mathematical problems, generate reports, or perform simulations.
- **Workflow Automation:** Automating repetitive or multi-step workflows by integrating tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents can interact with CRM systems, ticketing platforms, or knowledge bases to resolve user queries.
- **Content Generation and Editing:** Agents can leverage tools like grammar checkers, text summarizers, or content safety evaluators to assist with content creation tasks.

## What are the elements/building blocks needed to implement the tool use design pattern?

These building blocks allow the AI agent to perform a wide range of tasks. Let's look at the key elements needed to implement the Tool Use Design Pattern:

- **Function/Tool Schemas**: Detailed definitions of available tools, including function name, purpose, required parameters, and expected outputs. These schemas enable the LLM to understand what tools are available and how to construct valid requests.

- **Function Execution Logic**: Governs how and when tools are invoked based on the user’s intent and conversation context. This may include planner modules, routing mechanisms, or conditional flows that determine tool usage dynamically.

- **Message Handling System**: Components that manage the conversational flow between user inputs, LLM responses, tool calls, and tool outputs.

- **Tool Integration Framework**: Infrastructure that connects the agent to various tools, whether they are simple functions or complex external services.

- **Error Handling & Validation**: Mechanisms to handle failures in tool execution, validate parameters, and manage unexpected responses.

- **State Management**: Tracks conversation context, previous tool interactions, and persistent data to ensure consistency across multi-turn interactions.

Next, let's look at Function/Tool Calling in more detail.
 
### Function/Tool Calling

Function calling is the primary way we enable Large Language Models (LLMs) to interact with tools. You will often see 'Function' and 'Tool' used interchangeably because 'functions' (blocks of reusable code) are the 'tools' agents use to carry out tasks. In order for a function's code to be invoked, an LLM must compare the users request against the functions description. To do this a schema containing the descriptions of all the available functions is sent to the LLM. The LLM then selects the most appropriate function for the task and returns its name and arguments. The selected function is invoked, it's response is sent back to the LLM, which uses the information to respond to the users request.

For developers to implement function calling for agents, you will need:

1. An LLM model that supports function calling
2. A schema containing function descriptions
3. The code for each function described

Let's use the example of getting the current time in a city to illustrate:

1. **Initialize an LLM that supports function calling:**

    Not all models support function calling, so it's important to check that the LLM you are using does.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supports function calling. We can start by initiating the OpenAI client against the Azure OpenAI **Responses API** (the stable `/openai/v1/` endpoint — no `api_version` needed). 

    ```python
    # Initialize the OpenAI client for Azure OpenAI (Responses API, v1 endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Create a Function Schema**:

    Next we will define a JSON schema that contains the function name, description of what the function does, and the names and descriptions of the function parameters.
    We will then take this schema and pass it to the client created previously, along with the users request to find the time in San Francisco. What's important to note is that a **tool call** is what is returned, **not** the final answer to the question. As mentioned earlier, the LLM returns the name of the function it selected for the task, and the arguments that will be passed to it.

    ```python
    # Function description for the model to read (Responses API flat tool format)
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

    # First API call: Ask the model to use the function
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # The Responses API returns tool calls as function_call items in response.output.
    # Append them to the conversation so the model has full context on the next turn.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **The function code required to carry out the task:**

    Now that the LLM has chosen which function needs to be run the code that carries out the task needs to be implemented and executed.
    We can implement the code to get the current time in Python. We will also need to write the code to extract the name and arguments from the response_message to get the final result.

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

Function Calling is at the heart of most, if not all agent tool use design, however implementing it from scratch can sometimes be challenging.
As we learned in [Lesson 2](../../../02-explore-agentic-frameworks) agentic frameworks provide us with pre-built building blocks to implement tool use.
 
## Tool Use Examples with Agentic Frameworks

Here are some examples of how you can implement the Tool Use Design Pattern using different agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> is an open-source AI framework for building AI agents. It simplifies the process of using function calling by allowing you to define tools as Python functions with the `@tool` decorator. The framework handles the back-and-forth communication between the model and your code. It also provides access to pre-built tools like File Search and Code Interpreter through `FoundryChatClient`.

The following diagram illustrates the process of function calling with the Microsoft Agent Framework:

![function calling](../../../translated_images/en/functioncalling-diagram.a84006fc287f6014.webp)

In the Microsoft Agent Framework, tools are defined as decorated functions. We can convert the `get_current_time` function we saw earlier into a tool by using the `@tool` decorator. The framework will automatically serialize the function and its parameters, creating the schema to send to the LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Create the client
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Create an agent and run with the tool
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> is a newer agentic framework that is designed to empower developers to securely build, deploy, and scale high-quality, and extensible AI agents without needing to manage the underlying compute and storage resources. It is particularly useful for enterprise applications since it is a fully managed service with enterprise grade security.

When compared to developing with the LLM API directly, Microsoft Foundry Agent Service provides some advantages, including:

- Automatic tool calling – no need to parse a tool call, invoke the tool, and handle the response; all of this is now done server-side
- Securely managed data – instead of managing your own conversation state, you can rely on threads to store all the information you need
- Out-of-the-box tools – Tools that you can use to interact with your data sources, such as Bing, Azure AI Search, and Azure Functions.

The tools available in Microsoft Foundry Agent Service can be divided into two categories:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

The Agent Service allows us to be able to use these tools together as a `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

The following image illustrates how you could use Microsoft Foundry Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/en/agent-service-in-action.34fb465c9a84659e.webp)

To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the following Python code. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`, or the pre-built Code Interpreter depending on the user request.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize toolset
toolset = ToolSet()

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

A common concern with SQL dynamically generated by LLMs is security, particularly the risk of SQL injection or malicious actions, such as dropping or tampering with the database. While these concerns are valid, they can be effectively mitigated by properly configuring database access permissions. For most databases this involves configuring the database as read-only. For database services like PostgreSQL or Azure SQL, the app should be assigned a read-only (SELECT) role.

Running the app in a secure environment further enhances protection. In enterprise scenarios, data is typically extracted and transformed from operational systems into a read-only database or data warehouse with a user-friendly schema. This approach ensures that the data is secure, optimized for performance and accessibility, and that the app has restricted, read-only access.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>


## Smoke-Testing This Agent (Optional)

After you learn to deploy agents in [Lesson 16](../16-deploying-scalable-agents/README.md), you can smoke-test this lesson's `TravelToolAgent` (does it still call its tools and answer?) with [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). See [`tests/README.md`](../tests/README.md) for how to run it.

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->