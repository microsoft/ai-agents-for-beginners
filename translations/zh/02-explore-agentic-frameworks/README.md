<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:54:09+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "zh"
}
-->
根据维基百科，actor 是“并发计算的基本构建块。响应收到的消息时，actor 可以：做出本地决策、创建更多的 actors、发送更多消息，并决定如何响应接收到的下一条消息”。

**使用场景**：自动化代码生成、数据分析任务，以及构建用于规划和研究功能的自定义代理。

以下是 AutoGen 的一些重要核心概念：

- **代理（Agents）**。代理是一个软件实体，具有以下特性：
  - **通过消息进行通信**，这些消息可以是同步或异步的。
  - **维护自己的状态**，该状态可以被传入的消息修改。
  - **根据收到的消息或状态变化执行操作**。这些操作可能会修改代理的状态并产生外部效果，例如更新消息日志、发送新消息、执行代码或调用 API。
    
  下面是一个简短的代码片段，展示如何创建具有聊天功能的自定义代理：

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    在上面的代码中，`MyAssistant` 被创建并继承自 `RoutedAgent`。它有一个消息处理器，用于打印消息内容，然后使用 `AssistantAgent` 委托发送响应。特别注意我们如何将 `self._delegate` 赋值为 `AssistantAgent` 的实例，后者是一个预构建的代理，可以处理聊天完成。

    接下来让 AutoGen 知道这个代理类型并启动程序：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    在上面的代码中，代理被注册到运行时，然后向代理发送消息，产生如下输出：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **多代理（Multi agents）**。AutoGen 支持创建多个代理协同工作以完成复杂任务。代理可以通信、共享信息并协调行动以更高效地解决问题。要创建多代理系统，可以定义具有专门功能和角色的不同类型代理，如数据检索、分析、决策和用户交互。下面是一个示例，帮助你了解其创建方式：

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    在上面的代码中，我们有一个 `GroupChatManager`，它被注册到运行时。该管理器负责协调不同类型代理之间的交互，如作家、插画师、编辑和用户。

- **代理运行时（Agent Runtime）**。框架提供了一个运行时环境，支持代理间通信，管理它们的身份和生命周期，并执行安全和隐私边界。这意味着你可以在安全受控的环境中运行代理，确保它们能够安全高效地交互。有两种运行时值得关注：
  - **独立运行时（Stand-alone runtime）**。适合单进程应用，所有代理用同一种编程语言实现并运行在同一进程中。下面是其工作原理示意：

应用栈

    *代理通过运行时通过消息通信，运行时管理代理的生命周期*

  - **分布式代理运行时（Distributed agent runtime）**，适合多进程应用，代理可能用不同编程语言实现并运行在不同机器上。下面是其工作原理示意：

## Semantic Kernel + 代理框架

Semantic Kernel 是一个企业级 AI 编排 SDK。它包含 AI 和内存连接器，以及一个代理框架。

先介绍一些核心组件：

- **AI 连接器（AI Connectors）**：这是与外部 AI 服务和数据源的接口，支持 Python 和 C#。

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    这里是一个简单示例，展示如何创建一个 kernel 并添加聊天完成服务。Semantic Kernel 会创建到外部 AI 服务的连接，这里是 Azure OpenAI 聊天完成服务。

- **插件（Plugins）**：封装应用可用的函数。既有现成插件，也可以自定义。相关概念是“提示函数（prompt functions）”。不是通过自然语言提示调用函数，而是将某些函数广播给模型。基于当前聊天上下文，模型可能选择调用这些函数之一来完成请求或查询。示例如下：

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    这里，首先有一个模板提示 `skPrompt`，留有用户输入文本 `$userInput` 的位置。然后创建 kernel 函数 `SummarizeText`，并以插件名 `SemanticFunctions` 导入 kernel。注意函数名帮助 Semantic Kernel 理解函数作用及调用时机。

- **本地函数（Native function）**：框架也可以直接调用本地函数来执行任务。下面是一个从文件中读取内容的示例：

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **内存（Memory）**：抽象并简化 AI 应用的上下文管理。内存的理念是 LLM 应该“知道”这些信息。你可以将信息存储在向量存储中，最终形成内存数据库、向量数据库或类似结构。下面是一个非常简化的示例，展示如何将*事实*添加到内存：

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    这些事实随后存储在内存集合 `SummarizedAzureDocs` 中。虽然示例很简单，但你可以看到如何将信息存储到内存中供 LLM 使用。
## 上一课

[AI 代理及其应用案例介绍](../01-intro-to-ai-agents/README.md)

## 下一课

[理解代理设计模式](../03-agentic-design-patterns/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
