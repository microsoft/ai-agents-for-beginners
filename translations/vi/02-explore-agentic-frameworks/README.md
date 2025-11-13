<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T13:15:03+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "vi"
}
-->
[![Khám phá các khung AI Agent](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.vi.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

# Khám phá các khung AI Agent

Các khung AI Agent là các nền tảng phần mềm được thiết kế để đơn giản hóa việc tạo, triển khai và quản lý các AI agent. Những khung này cung cấp cho nhà phát triển các thành phần được xây dựng sẵn, các trừu tượng hóa và công cụ giúp tối ưu hóa việc phát triển các hệ thống AI phức tạp.

Những khung này giúp nhà phát triển tập trung vào các khía cạnh độc đáo của ứng dụng của họ bằng cách cung cấp các phương pháp tiêu chuẩn hóa để giải quyết các thách thức chung trong phát triển AI agent. Chúng tăng cường khả năng mở rộng, khả năng tiếp cận và hiệu quả trong việc xây dựng các hệ thống AI.

## Giới thiệu

Bài học này sẽ đề cập đến:

- AI Agent Frameworks là gì và chúng giúp nhà phát triển đạt được điều gì?
- Làm thế nào các nhóm có thể sử dụng chúng để nhanh chóng tạo mẫu, lặp lại và cải thiện khả năng của agent?
- Sự khác biệt giữa các khung và công cụ được tạo bởi Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, và <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> là gì?
- Tôi có thể tích hợp trực tiếp các công cụ hệ sinh thái Azure hiện có của mình hay cần các giải pháp độc lập?
- Azure AI Agents service là gì và nó giúp tôi như thế nào?

## Mục tiêu học tập

Mục tiêu của bài học này là giúp bạn hiểu:

- Vai trò của AI Agent Frameworks trong phát triển AI.
- Cách tận dụng AI Agent Frameworks để xây dựng các agent thông minh.
- Các khả năng chính được kích hoạt bởi AI Agent Frameworks.
- Sự khác biệt giữa AutoGen, Semantic Kernel và Azure AI Agent Service.

## AI Agent Frameworks là gì và chúng giúp nhà phát triển làm gì?

Các khung AI truyền thống có thể giúp bạn tích hợp AI vào ứng dụng và cải thiện các ứng dụng này theo các cách sau:

- **Cá nhân hóa**: AI có thể phân tích hành vi và sở thích của người dùng để cung cấp các gợi ý, nội dung và trải nghiệm cá nhân hóa.  
Ví dụ: Các dịch vụ phát trực tuyến như Netflix sử dụng AI để gợi ý phim và chương trình dựa trên lịch sử xem, tăng cường sự tương tác và hài lòng của người dùng.

- **Tự động hóa và hiệu quả**: AI có thể tự động hóa các tác vụ lặp lại, tối ưu hóa quy trình làm việc và cải thiện hiệu quả hoạt động.  
Ví dụ: Các ứng dụng dịch vụ khách hàng sử dụng chatbot hỗ trợ AI để xử lý các câu hỏi thông thường, giảm thời gian phản hồi và giải phóng nhân viên cho các vấn đề phức tạp hơn.

- **Cải thiện trải nghiệm người dùng**: AI có thể cải thiện trải nghiệm người dùng tổng thể bằng cách cung cấp các tính năng thông minh như nhận diện giọng nói, xử lý ngôn ngữ tự nhiên và văn bản dự đoán.  
Ví dụ: Các trợ lý ảo như Siri và Google Assistant sử dụng AI để hiểu và phản hồi các lệnh bằng giọng nói, giúp người dùng dễ dàng tương tác với thiết bị của họ.

### Nghe có vẻ tuyệt vời đúng không, vậy tại sao chúng ta cần AI Agent Framework?

Các khung AI Agent đại diện cho một điều gì đó hơn cả các khung AI thông thường. Chúng được thiết kế để tạo ra các agent thông minh có thể tương tác với người dùng, các agent khác và môi trường để đạt được các mục tiêu cụ thể. Những agent này có thể thể hiện hành vi tự động, đưa ra quyết định và thích nghi với các điều kiện thay đổi. Hãy cùng xem một số khả năng chính được kích hoạt bởi AI Agent Frameworks:

- **Hợp tác và phối hợp giữa các agent**: Cho phép tạo ra nhiều AI agent có thể làm việc cùng nhau, giao tiếp và phối hợp để giải quyết các nhiệm vụ phức tạp.
- **Tự động hóa và quản lý nhiệm vụ**: Cung cấp các cơ chế để tự động hóa các quy trình nhiều bước, phân công nhiệm vụ và quản lý nhiệm vụ động giữa các agent.
- **Hiểu và thích nghi theo ngữ cảnh**: Trang bị cho các agent khả năng hiểu ngữ cảnh, thích nghi với môi trường thay đổi và đưa ra quyết định dựa trên thông tin thời gian thực.

Tóm lại, các agent cho phép bạn làm được nhiều hơn, đưa tự động hóa lên một cấp độ mới, tạo ra các hệ thống thông minh hơn có thể thích nghi và học hỏi từ môi trường của chúng.

## Làm thế nào để nhanh chóng tạo mẫu, lặp lại và cải thiện khả năng của agent?

Đây là một lĩnh vực phát triển nhanh, nhưng có một số điều phổ biến trong hầu hết các AI Agent Frameworks có thể giúp bạn nhanh chóng tạo mẫu và lặp lại, cụ thể là các thành phần module, công cụ hợp tác và học tập theo thời gian thực. Hãy cùng tìm hiểu:

- **Sử dụng các thành phần module**: Các SDK AI cung cấp các thành phần được xây dựng sẵn như các kết nối AI và Memory, gọi hàm bằng ngôn ngữ tự nhiên hoặc plugin mã, mẫu gợi ý, và nhiều hơn nữa.
- **Tận dụng các công cụ hợp tác**: Thiết kế các agent với vai trò và nhiệm vụ cụ thể, cho phép thử nghiệm và tinh chỉnh các quy trình làm việc hợp tác.
- **Học tập theo thời gian thực**: Triển khai các vòng phản hồi nơi các agent học hỏi từ các tương tác và điều chỉnh hành vi của chúng một cách linh hoạt.

### Sử dụng các thành phần module

Các SDK như Microsoft Semantic Kernel và LangChain cung cấp các thành phần được xây dựng sẵn như các kết nối AI, mẫu gợi ý và quản lý bộ nhớ.

**Cách các nhóm có thể sử dụng chúng**: Các nhóm có thể nhanh chóng lắp ráp các thành phần này để tạo ra một nguyên mẫu chức năng mà không cần bắt đầu từ đầu, cho phép thử nghiệm và lặp lại nhanh chóng.

**Cách hoạt động trong thực tế**: Bạn có thể sử dụng một trình phân tích cú pháp được xây dựng sẵn để trích xuất thông tin từ đầu vào của người dùng, một module bộ nhớ để lưu trữ và truy xuất dữ liệu, và một trình tạo gợi ý để tương tác với người dùng, tất cả mà không cần phải xây dựng các thành phần này từ đầu.

**Ví dụ mã**. Hãy xem các ví dụ về cách bạn có thể sử dụng một AI Connector được xây dựng sẵn với Semantic Kernel Python và .Net sử dụng gọi hàm tự động để mô hình phản hồi đầu vào của người dùng:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Từ ví dụ này, bạn có thể thấy cách tận dụng một trình phân tích cú pháp được xây dựng sẵn để trích xuất thông tin chính từ đầu vào của người dùng, chẳng hạn như điểm xuất phát, điểm đến và ngày của yêu cầu đặt vé máy bay. Cách tiếp cận module này cho phép bạn tập trung vào logic cấp cao.

### Tận dụng các công cụ hợp tác

Các khung như CrewAI, Microsoft AutoGen và Semantic Kernel tạo điều kiện cho việc tạo ra nhiều agent có thể làm việc cùng nhau.

**Cách các nhóm có thể sử dụng chúng**: Các nhóm có thể thiết kế các agent với vai trò và nhiệm vụ cụ thể, cho phép thử nghiệm và tinh chỉnh các quy trình làm việc hợp tác và cải thiện hiệu quả hệ thống tổng thể.

**Cách hoạt động trong thực tế**: Bạn có thể tạo một nhóm các agent, mỗi agent có một chức năng chuyên biệt, chẳng hạn như truy xuất dữ liệu, phân tích hoặc ra quyết định. Những agent này có thể giao tiếp và chia sẻ thông tin để đạt được mục tiêu chung, chẳng hạn như trả lời câu hỏi của người dùng hoặc hoàn thành một nhiệm vụ.

**Ví dụ mã (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Trong mã trước, bạn thấy cách tạo một nhiệm vụ liên quan đến nhiều agent làm việc cùng nhau để phân tích dữ liệu. Mỗi agent thực hiện một chức năng cụ thể, và nhiệm vụ được thực hiện bằng cách phối hợp các agent để đạt được kết quả mong muốn. Bằng cách tạo các agent chuyên biệt với vai trò cụ thể, bạn có thể cải thiện hiệu quả và hiệu suất nhiệm vụ.

### Học tập theo thời gian thực

Các khung tiên tiến cung cấp khả năng hiểu ngữ cảnh và thích nghi theo thời gian thực.

**Cách các nhóm có thể sử dụng chúng**: Các nhóm có thể triển khai các vòng phản hồi nơi các agent học hỏi từ các tương tác và điều chỉnh hành vi của chúng một cách linh hoạt, dẫn đến cải tiến liên tục và tinh chỉnh khả năng.

**Cách hoạt động trong thực tế**: Các agent có thể phân tích phản hồi của người dùng, dữ liệu môi trường và kết quả nhiệm vụ để cập nhật cơ sở kiến thức của chúng, điều chỉnh các thuật toán ra quyết định và cải thiện hiệu suất theo thời gian. Quá trình học tập lặp lại này cho phép các agent thích nghi với các điều kiện thay đổi và sở thích của người dùng, nâng cao hiệu quả hệ thống tổng thể.

## Sự khác biệt giữa các khung AutoGen, Semantic Kernel và Azure AI Agent Service là gì?

Có nhiều cách để so sánh các khung này, nhưng hãy xem xét một số điểm khác biệt chính về thiết kế, khả năng và trường hợp sử dụng mục tiêu:

## AutoGen

AutoGen là một khung mã nguồn mở được phát triển bởi AI Frontiers Lab của Microsoft Research. Nó tập trung vào các ứng dụng *agentic* phân tán, dựa trên sự kiện, cho phép nhiều LLMs và SLMs, công cụ, và các mẫu thiết kế multi-agent tiên tiến.

AutoGen được xây dựng xung quanh khái niệm cốt lõi về các agent, là các thực thể tự động có thể nhận thức môi trường của chúng, đưa ra quyết định và thực hiện hành động để đạt được các mục tiêu cụ thể. Các agent giao tiếp thông qua các tin nhắn không đồng bộ, cho phép chúng làm việc độc lập và song song, tăng cường khả năng mở rộng và phản hồi của hệ thống.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Các agent dựa trên mô hình actor</a>. Theo Wikipedia, một actor là _khối xây dựng cơ bản của tính toán đồng thời. Để phản hồi một tin nhắn nhận được, một actor có thể: đưa ra quyết định cục bộ, tạo thêm các actor, gửi thêm tin nhắn, và xác định cách phản hồi tin nhắn tiếp theo nhận được_.

**Trường hợp sử dụng**: Tự động hóa tạo mã, nhiệm vụ phân tích dữ liệu, và xây dựng các agent tùy chỉnh cho các chức năng lập kế hoạch và nghiên cứu.

Dưới đây là một số khái niệm cốt lõi quan trọng của AutoGen:

- **Agents**. Một agent là một thực thể phần mềm mà:
  - **Giao tiếp qua tin nhắn**, các tin nhắn này có thể đồng bộ hoặc không đồng bộ.
  - **Duy trì trạng thái riêng**, trạng thái này có thể được sửa đổi bởi các tin nhắn đến.
  - **Thực hiện hành động** để phản hồi các tin nhắn nhận được hoặc thay đổi trạng thái của nó. Những hành động này có thể sửa đổi trạng thái của agent và tạo ra các hiệu ứng bên ngoài, chẳng hạn như cập nhật nhật ký tin nhắn, gửi tin nhắn mới, thực thi mã, hoặc thực hiện các cuộc gọi API.

  Dưới đây là một đoạn mã ngắn trong đó bạn tạo agent của riêng mình với khả năng Chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
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
    
    Trong mã trước, `MyAgent` đã được tạo và kế thừa từ `RoutedAgent`. Nó có một trình xử lý tin nhắn in nội dung của tin nhắn và sau đó gửi phản hồi bằng cách sử dụng đại diện `AssistantAgent`. Đặc biệt lưu ý cách chúng ta gán cho `self._delegate` một instance của `AssistantAgent`, là một agent được xây dựng sẵn có thể xử lý các hoàn thành chat.

    Hãy để AutoGen biết về loại agent này và khởi động chương trình tiếp theo:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Trong mã trước, các agent được đăng ký với runtime và sau đó một tin nhắn được gửi đến agent dẫn đến đầu ra sau:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen hỗ trợ việc tạo ra nhiều agent có thể làm việc cùng nhau để đạt được các nhiệm vụ phức tạp. Các agent có thể giao tiếp, chia sẻ thông tin và phối hợp hành động của chúng để giải quyết vấn đề hiệu quả hơn. Để tạo một hệ thống multi-agent, bạn có thể định nghĩa các loại agent khác nhau với các chức năng và vai trò chuyên biệt, chẳng hạn như truy xuất dữ liệu, phân tích, ra quyết định và tương tác với người dùng. Hãy xem cách tạo như vậy trông như thế nào để chúng ta có cảm nhận về nó:

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

    Trong mã trước, chúng ta có một `GroupChatManager` được đăng ký với runtime. Quản lý này chịu trách nhiệm phối hợp các tương tác giữa các loại agent khác nhau, chẳng hạn như người viết, người minh họa, biên tập viên và người dùng.

- **Agent Runtime**. Khung cung cấp một môi trường runtime, cho phép giao tiếp giữa các agent, quản lý danh tính và vòng đời của chúng, và thực thi các ranh giới bảo mật và quyền riêng tư. Điều này có nghĩa là bạn có thể chạy các agent của mình trong một môi trường an toàn và được kiểm soát, đảm bảo rằng chúng có thể tương tác một cách an toàn và hiệu quả. Có hai runtime đáng quan tâm:
  - **Runtime độc lập**. Đây là lựa chọn tốt cho các ứng dụng đơn quy trình nơi tất cả các agent được triển khai trong cùng một ngôn ngữ lập trình và chạy trong cùng một quy trình. Dưới đây là minh họa cách nó hoạt động:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime độc lập</a>   
Application stack

    *các agent giao tiếp qua tin nhắn thông qua runtime, và runtime quản lý vòng đời của các agent*

  - **Runtime agent phân tán**, phù hợp cho các ứng dụng đa quy trình nơi các agent có thể được triển khai trong các ngôn ngữ lập trình khác nhau và chạy trên các máy khác nhau. Dưới đây là minh họa cách nó hoạt động:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime phân tán</a>

## Semantic Kernel + Agent Framework

Semantic Kernel là một SDK Orchestration AI sẵn sàng cho doanh nghiệp. Nó bao gồm các kết nối AI và bộ nhớ, cùng với một Agent Framework.

Hãy cùng tìm hiểu một số thành phần cốt lõi:

- **AI Connectors**: Đây là giao diện với các dịch vụ AI bên ngoài và các nguồn dữ liệu để sử dụng trong cả Python và C#.

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

    Đây là một ví dụ đơn giản về cách bạn có thể tạo một kernel và thêm một dịch vụ hoàn thành chat. Semantic Kernel tạo kết nối với một dịch vụ AI bên ngoài, trong trường hợp này là Azure OpenAI Chat Completion.

- **Plugins**: Các plugin này đóng gói các chức năng mà ứng dụng có thể sử dụng. Có cả các plugin sẵn có và các plugin tùy chỉnh mà bạn có thể tạo. Một khái niệm liên quan là "prompt functions." Thay vì cung cấp các gợi ý ngôn ngữ tự nhiên để gọi hàm, bạn phát sóng một số chức năng nhất định đến mô hình. Dựa trên ngữ cảnh chat hiện tại, mô hình có thể chọn gọi một trong những chức năng này để hoàn thành yêu cầu hoặc truy vấn. Dưới đây là một ví dụ:

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

    Ở đây, bạn có một mẫu gợi ý `skPrompt` để người dùng nhập văn bản, `$userInput`. Sau đó, bạn tạo hàm kernel `SummarizeText` và nhập nó vào kernel với tên plugin `SemanticFunctions`. Lưu ý tên của hàm giúp Semantic Kernel hiểu hàm làm gì và khi nào nên gọi.

- **Native function**: Cũng có các hàm native mà khung có thể gọi trực tiếp để thực hiện nhiệm vụ. Dưới đây là một ví dụ về một hàm như vậy truy xuất nội dung từ một tệp:

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

- **Memory**: Trừu tượng hóa và đơn giản hóa việc quản lý ngữ cảnh cho các ứng dụng AI. Ý tưởng với bộ nhớ là đây là thứ mà LLM nên biết. Bạn có thể lưu trữ thông tin này trong một vector store, cuối cùng là một cơ sở dữ liệu trong bộ nhớ hoặc một cơ sở dữ liệu vector hoặc tương tự. Dưới đây là một ví dụ về một kịch bản rất đơn giản nơi *facts* được thêm vào bộ nhớ:

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

Những thông tin này sau đó được lưu trữ trong bộ sưu tập bộ nhớ `SummarizedAzureDocs`. Đây là một ví dụ rất đơn giản, nhưng bạn có thể thấy cách lưu trữ thông tin trong bộ nhớ để LLM sử dụng.

Vậy đó là những điều cơ bản về khung Semantic Kernel, còn về Agent Framework thì sao?

## Dịch vụ Azure AI Agent

Dịch vụ Azure AI Agent là một bổ sung gần đây, được giới thiệu tại Microsoft Ignite 2024. Nó cho phép phát triển và triển khai các agent AI với các mô hình linh hoạt hơn, chẳng hạn như gọi trực tiếp các LLM mã nguồn mở như Llama 3, Mistral và Cohere.

Dịch vụ Azure AI Agent cung cấp các cơ chế bảo mật doanh nghiệp mạnh mẽ và phương pháp lưu trữ dữ liệu, làm cho nó phù hợp với các ứng dụng doanh nghiệp.

Nó hoạt động ngay lập tức với các khung điều phối đa-agent như AutoGen và Semantic Kernel.

Dịch vụ này hiện đang ở giai đoạn Public Preview và hỗ trợ Python và C# để xây dựng các agent.

Sử dụng Semantic Kernel Python, chúng ta có thể tạo một Azure AI Agent với plugin do người dùng định nghĩa:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Các khái niệm cốt lõi

Dịch vụ Azure AI Agent có các khái niệm cốt lõi sau:

- **Agent**. Dịch vụ Azure AI Agent tích hợp với Azure AI Foundry. Trong AI Foundry, một AI Agent hoạt động như một microservice "thông minh" có thể được sử dụng để trả lời câu hỏi (RAG), thực hiện hành động, hoặc hoàn toàn tự động hóa các quy trình làm việc. Nó đạt được điều này bằng cách kết hợp sức mạnh của các mô hình AI sinh với các công cụ cho phép nó truy cập và tương tác với các nguồn dữ liệu thực tế. Đây là một ví dụ về agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Trong ví dụ này, một agent được tạo với mô hình `gpt-4o-mini`, tên `my-agent`, và hướng dẫn `You are helpful agent`. Agent được trang bị các công cụ và tài nguyên để thực hiện các nhiệm vụ giải thích mã.

- **Thread và messages**. Thread là một khái niệm quan trọng khác. Nó đại diện cho một cuộc trò chuyện hoặc tương tác giữa một agent và người dùng. Threads có thể được sử dụng để theo dõi tiến trình của cuộc trò chuyện, lưu trữ thông tin ngữ cảnh, và quản lý trạng thái của tương tác. Đây là một ví dụ về thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Trong đoạn mã trước, một thread được tạo. Sau đó, một tin nhắn được gửi đến thread. Bằng cách gọi `create_and_process_run`, agent được yêu cầu thực hiện công việc trên thread. Cuối cùng, các tin nhắn được lấy và ghi lại để xem phản hồi của agent. Các tin nhắn cho thấy tiến trình của cuộc trò chuyện giữa người dùng và agent. Cũng cần hiểu rằng các tin nhắn có thể thuộc các loại khác nhau như văn bản, hình ảnh, hoặc tệp, tức là công việc của agent đã tạo ra ví dụ như một hình ảnh hoặc một phản hồi văn bản. Là một nhà phát triển, bạn có thể sử dụng thông tin này để xử lý thêm phản hồi hoặc trình bày nó cho người dùng.

- **Tích hợp với các khung AI khác**. Dịch vụ Azure AI Agent có thể tương tác với các khung khác như AutoGen và Semantic Kernel, nghĩa là bạn có thể xây dựng một phần ứng dụng của mình trong một trong các khung này và ví dụ sử dụng dịch vụ Agent như một bộ điều phối hoặc bạn có thể xây dựng mọi thứ trong dịch vụ Agent.

**Các trường hợp sử dụng**: Dịch vụ Azure AI Agent được thiết kế cho các ứng dụng doanh nghiệp yêu cầu triển khai agent AI an toàn, có khả năng mở rộng và linh hoạt.

## Sự khác biệt giữa các khung này là gì?

Có vẻ như có nhiều điểm tương đồng giữa các khung này, nhưng có một số khác biệt chính về thiết kế, khả năng và các trường hợp sử dụng mục tiêu:

- **AutoGen**: Là một khung thử nghiệm tập trung vào nghiên cứu tiên tiến về hệ thống đa-agent. Đây là nơi tốt nhất để thử nghiệm và tạo mẫu các hệ thống đa-agent phức tạp.
- **Semantic Kernel**: Là một thư viện agent sẵn sàng sản xuất để xây dựng các ứng dụng agent doanh nghiệp. Tập trung vào các ứng dụng agent phân tán, dựa trên sự kiện, cho phép nhiều LLM và SLM, công cụ, và các mẫu thiết kế agent đơn/đa.
- **Azure AI Agent Service**: Là một nền tảng và dịch vụ triển khai trong Azure Foundry cho các agent. Nó cung cấp khả năng kết nối với các dịch vụ được hỗ trợ bởi Azure như Azure OpenAI, Azure AI Search, Bing Search và thực thi mã.

Vẫn chưa chắc chắn nên chọn cái nào?

### Các trường hợp sử dụng

Hãy xem liệu chúng tôi có thể giúp bạn bằng cách đi qua một số trường hợp sử dụng phổ biến:

> Q: Tôi đang thử nghiệm, học hỏi và xây dựng các ứng dụng agent proof-of-concept, và tôi muốn có thể xây dựng và thử nghiệm nhanh chóng
>

>A: AutoGen sẽ là một lựa chọn tốt cho trường hợp này, vì nó tập trung vào các ứng dụng agent phân tán, dựa trên sự kiện và hỗ trợ các mẫu thiết kế đa-agent tiên tiến.

> Q: Điều gì làm cho AutoGen là lựa chọn tốt hơn so với Semantic Kernel và Azure AI Agent Service cho trường hợp này?
>
> A: AutoGen được thiết kế đặc biệt cho các ứng dụng agent phân tán, dựa trên sự kiện, làm cho nó phù hợp với các nhiệm vụ tự động hóa tạo mã và phân tích dữ liệu. Nó cung cấp các công cụ và khả năng cần thiết để xây dựng các hệ thống đa-agent phức tạp một cách hiệu quả.

>Q: Nghe có vẻ như Azure AI Agent Service cũng có thể hoạt động ở đây, nó có các công cụ để tạo mã và hơn thế nữa?

>
> A: Đúng vậy, Azure AI Agent Service là một dịch vụ nền tảng cho các agent và bổ sung các khả năng tích hợp sẵn cho nhiều mô hình, Azure AI Search, Bing Search và Azure Functions. Nó giúp dễ dàng xây dựng các agent của bạn trong Foundry Portal và triển khai chúng ở quy mô lớn.

> Q: Tôi vẫn còn bối rối, chỉ cần cho tôi một lựa chọn
>
> A: Một lựa chọn tuyệt vời là xây dựng ứng dụng của bạn trong Semantic Kernel trước và sau đó sử dụng Azure AI Agent Service để triển khai agent của bạn. Cách tiếp cận này cho phép bạn dễ dàng duy trì các agent của mình trong khi tận dụng sức mạnh để xây dựng các hệ thống đa-agent trong Semantic Kernel. Ngoài ra, Semantic Kernel có một trình kết nối trong AutoGen, giúp dễ dàng sử dụng cả hai khung cùng nhau.

Hãy tóm tắt các điểm khác biệt chính trong một bảng:

| Khung | Tập trung | Các khái niệm cốt lõi | Các trường hợp sử dụng |
| --- | --- | --- | --- |
| AutoGen | Các ứng dụng agent phân tán, dựa trên sự kiện | Agents, Personas, Functions, Data | Tạo mã, nhiệm vụ phân tích dữ liệu |
| Semantic Kernel | Hiểu và tạo nội dung giống con người | Agents, Modular Components, Collaboration | Hiểu ngôn ngữ tự nhiên, tạo nội dung |
| Azure AI Agent Service | Các mô hình linh hoạt, bảo mật doanh nghiệp, Tạo mã, Gọi công cụ | Modularity, Collaboration, Process Orchestration | Triển khai agent AI an toàn, có khả năng mở rộng và linh hoạt |

Trường hợp sử dụng lý tưởng cho mỗi khung này là gì?

## Tôi có thể tích hợp trực tiếp các công cụ hệ sinh thái Azure hiện có của mình, hay tôi cần các giải pháp độc lập?

Câu trả lời là có, bạn có thể tích hợp trực tiếp các công cụ hệ sinh thái Azure hiện có của mình với Azure AI Agent Service, đặc biệt vì nó được xây dựng để hoạt động liền mạch với các dịch vụ Azure khác. Ví dụ, bạn có thể tích hợp Bing, Azure AI Search, và Azure Functions. Ngoài ra còn có tích hợp sâu với Azure AI Foundry.

Đối với AutoGen và Semantic Kernel, bạn cũng có thể tích hợp với các dịch vụ Azure, nhưng có thể yêu cầu bạn gọi các dịch vụ Azure từ mã của mình. Một cách khác để tích hợp là sử dụng các SDK của Azure để tương tác với các dịch vụ Azure từ các agent của bạn. Ngoài ra, như đã đề cập, bạn có thể sử dụng Azure AI Agent Service như một bộ điều phối cho các agent được xây dựng trong AutoGen hoặc Semantic Kernel, điều này sẽ cung cấp quyền truy cập dễ dàng vào hệ sinh thái Azure.

## Mã mẫu

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Có thêm câu hỏi về AI Agent Frameworks?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Tài liệu tham khảo

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Dịch vụ Azure Agent</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel và AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Khung Semantic Kernel Python Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Khung Semantic Kernel .Net Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dịch vụ Azure AI Agent</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Sử dụng Azure AI Agent Service với AutoGen / Semantic Kernel để xây dựng giải pháp đa-agent</a>

## Bài học trước

[Giới thiệu về AI Agents và các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

## Bài học tiếp theo

[Hiểu các mẫu thiết kế Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->