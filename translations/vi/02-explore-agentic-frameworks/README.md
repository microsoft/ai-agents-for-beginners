[![Khám phá các khung tác nhân AI](../../../translated_images/vi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Nhấp vào hình ảnh trên để xem video bài học này)_

# Khám phá các khung tác nhân AI

Các khung tác nhân AI là các nền tảng phần mềm được thiết kế để đơn giản hóa việc tạo, triển khai và quản lý các tác nhân AI. Các khung này cung cấp cho nhà phát triển các thành phần dựng sẵn, các trừu tượng hóa và các công cụ giúp tinh giản việc phát triển các hệ thống AI phức tạp.

Các khung này giúp nhà phát triển tập trung vào các khía cạnh độc đáo của ứng dụng bằng cách cung cấp các phương pháp chuẩn hóa cho các thách thức phổ biến trong phát triển tác nhân AI. Chúng nâng cao khả năng mở rộng, tính dễ tiếp cận và hiệu quả trong việc xây dựng các hệ thống AI.

## Giới thiệu

Bài học này sẽ đề cập đến:

- Khung tác nhân AI là gì và chúng cho phép nhà phát triển đạt được những gì?
- Các nhóm có thể sử dụng chúng để nhanh chóng tạo mẫu, lặp lại và cải thiện khả năng của tác nhân như thế nào?
- Sự khác biệt giữa các khung và công cụ do Microsoft tạo ra (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> và <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) là gì?
- Tôi có thể tích hợp các công cụ hệ sinh thái Azure hiện tại của mình trực tiếp không, hay cần các giải pháp độc lập?
- Microsoft Foundry Agent Service là gì và nó giúp tôi như thế nào?

## Mục tiêu học tập

Mục tiêu của bài học này là giúp bạn hiểu:

- Vai trò của các khung tác nhân AI trong phát triển AI.
- Cách tận dụng các khung tác nhân AI để xây dựng các tác nhân thông minh.
- Các khả năng chính được kích hoạt bởi các khung tác nhân AI.
- Sự khác biệt giữa Microsoft Agent Framework và Microsoft Foundry Agent Service.

## Khung tác nhân AI là gì và chúng cho phép nhà phát triển làm gì?

Các khung AI truyền thống có thể giúp bạn tích hợp AI vào các ứng dụng của mình và làm cho các ứng dụng này tốt hơn theo các cách sau:

- **Cá nhân hóa**: AI có thể phân tích hành vi và sở thích của người dùng để cung cấp các đề xuất, nội dung và trải nghiệm được cá nhân hóa.
Ví dụ: Các dịch vụ phát trực tuyến như Netflix sử dụng AI để đề xuất phim và chương trình dựa trên lịch sử xem, nâng cao sự tương tác và hài lòng của người dùng.
- **Tự động hóa và hiệu quả**: AI có thể tự động hóa các tác vụ lặp lại, tối ưu hóa quy trình làm việc và cải thiện hiệu quả vận hành.
Ví dụ: Ứng dụng dịch vụ khách hàng sử dụng chatbot được hỗ trợ AI để xử lý các câu hỏi thường gặp, giảm thời gian phản hồi và giải phóng nhân viên cho các vấn đề phức tạp hơn.
- **Cải thiện trải nghiệm người dùng**: AI có thể nâng cao trải nghiệm tổng thể bằng cách cung cấp các tính năng thông minh như nhận dạng giọng nói, xử lý ngôn ngữ tự nhiên và dự đoán văn bản.
Ví dụ: Trợ lý ảo như Siri và Google Assistant sử dụng AI để hiểu và đáp ứng các lệnh thoại, giúp người dùng dễ dàng tương tác với thiết bị của họ hơn.

### Nghe có vẻ tuyệt vời, vậy tại sao chúng ta cần Khung tác nhân AI?

Khung tác nhân AI đại diện cho một điều gì đó nhiều hơn chỉ là các khung AI thông thường. Chúng được thiết kế để tạo ra các tác nhân thông minh có thể tương tác với người dùng, các tác nhân khác và môi trường để đạt được các mục tiêu cụ thể. Những tác nhân này có thể thể hiện hành vi tự động, đưa ra quyết định và thích ứng với các điều kiện thay đổi. Hãy cùng xem một số khả năng chính được các khung tác nhân AI hỗ trợ:

- **Hợp tác và phối hợp tác nhân**: Cho phép tạo ra nhiều tác nhân AI có thể làm việc cùng nhau, giao tiếp và phối hợp để giải quyết các nhiệm vụ phức tạp.
- **Tự động hóa và quản lý nhiệm vụ**: Cung cấp các cơ chế để tự động hóa các quy trình làm việc đa bước, ủy thác nhiệm vụ và quản lý nhiệm vụ động giữa các tác nhân.
- **Hiểu và thích ứng theo ngữ cảnh**: Trang bị cho các tác nhân khả năng hiểu bối cảnh, thích ứng với môi trường thay đổi và đưa ra quyết định dựa trên thông tin thời gian thực.

Tóm lại, các tác nhân cho phép bạn làm được nhiều hơn, nâng tầm tự động hóa, tạo ra các hệ thống thông minh có thể thích nghi và học hỏi từ môi trường của chúng.

## Cách nhanh chóng tạo mẫu, lặp lại và cải thiện khả năng của tác nhân?

Đây là một lĩnh vực phát triển nhanh, nhưng có những yếu tố chung trong hầu hết các khung tác nhân AI có thể giúp bạn nhanh chóng tạo mẫu và lặp lại, đó là các thành phần mô-đun, công cụ hợp tác và học theo thời gian thực. Hãy cùng tìm hiểu những điều này:

- **Sử dụng các thành phần mô-đun**: SDK AI cung cấp các thành phần dựng sẵn như bộ kết nối AI và bộ nhớ, gọi chức năng bằng ngôn ngữ tự nhiên hoặc plugin mã, mẫu lời nhắc, và nhiều hơn nữa.
- **Tận dụng công cụ hợp tác**: Thiết kế các tác nhân với các vai trò và nhiệm vụ cụ thể, cho phép họ thử nghiệm và tinh chỉnh quy trình làm việc hợp tác.
- **Học theo thời gian thực**: Triển khai các vòng phản hồi nơi các tác nhân học hỏi từ các tương tác và điều chỉnh hành vi một cách động.

### Sử dụng các thành phần mô-đun

SDK như Microsoft Agent Framework cung cấp các thành phần dựng sẵn như bộ kết nối AI, định nghĩa công cụ và quản lý tác nhân.

**Cách các nhóm có thể sử dụng**: Các nhóm có thể nhanh chóng lắp ráp các thành phần này để tạo bản mẫu chức năng mà không cần bắt đầu từ con số không, cho phép thử nghiệm và lặp lại nhanh.

**Cách thức hoạt động trong thực tế**: Bạn có thể sử dụng bộ phân tích dựng sẵn để trích xuất thông tin từ đầu vào người dùng, mô-đun bộ nhớ để lưu trữ và truy xuất dữ liệu, và bộ tạo lời nhắc để tương tác với người dùng, tất cả mà không cần xây dựng các thành phần này từ đầu.

**Mã ví dụ**. Hãy xem ví dụ về cách bạn có thể sử dụng Microsoft Agent Framework với `FoundryChatClient` để mô hình phản hồi đầu vào người dùng với gọi công cụ:

``` python
# Ví dụ Python về Khung làm việc Microsoft Agent

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Định nghĩa một hàm công cụ mẫu để đặt chuyến đi
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Ví dụ kết quả: Chuyến bay của bạn đến New York vào ngày 1 tháng 1 năm 2025 đã được đặt thành công. Chúc bạn có chuyến đi an toàn! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Bạn có thể thấy từ ví dụ này cách tận dụng bộ phân tích dựng sẵn để trích xuất các thông tin chính từ đầu vào người dùng, chẳng hạn như điểm xuất phát, điểm đến và ngày tháng của yêu cầu đặt vé máy bay. Cách tiếp cận mô-đun này cho phép bạn tập trung vào logic ở cấp cao hơn.

### Tận dụng công cụ hợp tác

Các khung như Microsoft Agent Framework hỗ trợ việc tạo nhiều tác nhân có thể làm việc chung với nhau.

**Cách các nhóm có thể sử dụng**: Các nhóm có thể thiết kế các tác nhân với vai trò và nhiệm vụ cụ thể, cho phép thử nghiệm và cải thiện quy trình làm việc hợp tác và nâng cao hiệu quả hệ thống tổng thể.

**Cách thức hoạt động trong thực tế**: Bạn có thể tạo một nhóm các tác nhân mà mỗi tác nhân đảm nhận một chức năng chuyên biệt, chẳng hạn như lấy dữ liệu, phân tích hoặc ra quyết định. Các tác nhân này có thể giao tiếp và chia sẻ thông tin để đạt được mục tiêu chung, ví dụ trả lời câu hỏi người dùng hoặc hoàn thành một nhiệm vụ.

**Mã ví dụ (Microsoft Agent Framework)**:

```python
# Tạo nhiều agent làm việc cùng nhau sử dụng Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent Thu Thập Dữ Liệu
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent Phân Tích Dữ Liệu
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Chạy các agent theo tuần tự trên một nhiệm vụ
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Bạn sẽ thấy trong đoạn mã trên cách tạo nhiệm vụ liên quan đến nhiều tác nhân làm việc cùng nhau để phân tích dữ liệu. Mỗi tác nhân thực hiện một chức năng cụ thể, và nhiệm vụ được thực hiện bằng cách phối hợp các tác nhân để đạt kết quả mong muốn. Việc tạo các tác nhân chuyên biệt với vai trò riêng giúp cải thiện hiệu quả và hiệu suất công việc.

### Học theo thời gian thực

Các khung nâng cao cung cấp khả năng hiểu bối cảnh và thích ứng theo thời gian thực.

**Cách các nhóm có thể sử dụng**: Các nhóm có thể triển khai các vòng phản hồi, nơi các tác nhân học từ các tương tác và điều chỉnh hành vi một cách linh hoạt, dẫn đến việc cải tiến và tinh chỉnh liên tục các khả năng.

**Cách thức hoạt động trong thực tế**: Các tác nhân có thể phân tích phản hồi người dùng, dữ liệu môi trường và kết quả nhiệm vụ để cập nhật cơ sở kiến thức, điều chỉnh thuật toán ra quyết định và nâng cao hiệu suất theo thời gian. Quá trình học lặp này giúp các tác nhân thích nghi với các điều kiện và sở thích người dùng thay đổi, nâng cao hiệu quả hệ thống tổng thể.

## Sự khác biệt giữa Microsoft Agent Framework và Microsoft Foundry Agent Service?

Có nhiều cách so sánh hai phương pháp này, nhưng hãy cùng xem một số khác biệt chính về thiết kế, khả năng và mục tiêu sử dụng:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework cung cấp một SDK tinh giản để xây dựng các tác nhân AI sử dụng `FoundryChatClient`. Nó cho phép nhà phát triển tạo tác nhân tận dụng mô hình Azure OpenAI với chức năng gọi công cụ tích hợp, quản lý cuộc trò chuyện và bảo mật cấp doanh nghiệp qua Azure Identity.

**Trường hợp sử dụng**: Xây dựng các tác nhân AI sẵn sàng triển khai với sử dụng công cụ, quy trình làm việc đa bước và tích hợp doanh nghiệp.

Dưới đây là một số khái niệm cốt lõi quan trọng của Microsoft Agent Framework:

- **Tác nhân**. Một tác nhân được tạo bởi `FoundryChatClient` và cấu hình với tên, hướng dẫn và công cụ. Tác nhân có thể:
  - **Xử lý tin nhắn người dùng** và tạo phản hồi sử dụng mô hình Azure OpenAI.
  - **Tự động gọi công cụ** dựa trên ngữ cảnh cuộc trò chuyện.
  - **Duy trì trạng thái cuộc trò chuyện** qua nhiều tương tác.

  Dưới đây là đoạn mã minh họa cách tạo tác nhân:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Công cụ**. Khung hỗ trợ định nghĩa công cụ dưới dạng hàm Python mà tác nhân có thể tự động gọi. Công cụ được đăng ký khi tạo tác nhân:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Phối hợp đa tác nhân**. Bạn có thể tạo nhiều tác nhân với các chuyên môn khác nhau và phối hợp công việc của họ:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Tích hợp Azure Identity**. Khung sử dụng `AzureCliCredential` (hoặc `DefaultAzureCredential`) cho xác thực an toàn không cần khóa, loại bỏ nhu cầu quản lý khóa API trực tiếp.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service là một bổ sung mới hơn, được giới thiệu tại Microsoft Ignite 2024. Nó cho phép phát triển và triển khai các tác nhân AI với các mô hình linh hoạt hơn, chẳng hạn gọi trực tiếp các LLM mã nguồn mở như Llama 3, Mistral và Cohere.

Microsoft Foundry Agent Service cung cấp cơ chế bảo mật doanh nghiệp mạnh mẽ và phương pháp lưu trữ dữ liệu, phù hợp cho các ứng dụng doanh nghiệp.

Nó hoạt động sẵn sàng cùng Microsoft Agent Framework để xây dựng và triển khai tác nhân.

Dịch vụ này hiện đang trong giai đoạn Public Preview và hỗ trợ Python và C# để xây dựng tác nhân.

Sử dụng Python SDK của Microsoft Foundry Agent Service, chúng ta có thể tạo một tác nhân với công cụ do người dùng định nghĩa:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Định nghĩa các chức năng công cụ
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Khái niệm cốt lõi

Microsoft Foundry Agent Service có các khái niệm cốt lõi sau:

- **Tác nhân**. Microsoft Foundry Agent Service tích hợp với Microsoft Foundry. Trong Microsoft Foundry, một tác nhân AI hoạt động như một "microservice" thông minh có thể dùng để trả lời câu hỏi (RAG), thực hiện hành động hoặc tự động hoàn toàn các quy trình làm việc. Nó đạt được điều này bằng cách kết hợp sức mạnh của các mô hình AI sinh tạo với các công cụ cho phép truy cập và tương tác với nguồn dữ liệu thế giới thực. Dưới đây là ví dụ về một tác nhân:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Trong ví dụ này, một tác nhân được tạo với mô hình `gpt-5-mini`, tên `my-agent`, và hướng dẫn `You are helpful agent`. Tác nhân được trang bị công cụ và tài nguyên để thực hiện nhiệm vụ giải thích mã.

- **Chuỗi và tin nhắn**. Chuỗi là một khái niệm quan trọng khác. Nó đại diện cho cuộc trò chuyện hoặc tương tác giữa tác nhân và người dùng. Chuỗi có thể được sử dụng để theo dõi tiến trình trò chuyện, lưu trữ thông tin ngữ cảnh và quản lý trạng thái tương tác. Dưới đây là ví dụ về một chuỗi:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Yêu cầu tác nhân thực hiện công việc trên chuỗi
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Lấy và ghi lại tất cả các tin nhắn để xem phản hồi của tác nhân
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Trong đoạn mã trên, một chuỗi được tạo. Sau đó, một tin nhắn được gửi vào chuỗi. Bằng cách gọi `create_and_process_run`, tác nhân được yêu cầu thực hiện công việc trên chuỗi. Cuối cùng, các tin nhắn được lấy và ghi lại để xem phản hồi của tác nhân. Các tin nhắn cho thấy tiến trình cuộc trò chuyện giữa người dùng và tác nhân. Cũng quan trọng để hiểu rằng các tin nhắn có thể thuộc các loại khác nhau như văn bản, hình ảnh hoặc tập tin, nghĩa là công việc của tác nhân có thể tạo ra ví dụ như hình ảnh hoặc phản hồi văn bản. Là nhà phát triển, bạn có thể dùng những thông tin này để xử lý thêm phản hồi hoặc trình bày cho người dùng.

- **Tích hợp với Microsoft Agent Framework**. Microsoft Foundry Agent Service hoạt động liền mạch với Microsoft Agent Framework, nghĩa là bạn có thể xây dựng tác nhân sử dụng `FoundryChatClient` và triển khai qua Agent Service cho kịch bản sản xuất.

**Trường hợp sử dụng**: Microsoft Foundry Agent Service được thiết kế cho các ứng dụng doanh nghiệp yêu cầu triển khai tác nhân AI bảo mật, có khả năng mở rộng và linh hoạt.

## Sự khác biệt giữa các phương pháp này là gì?
 
Nghe có vẻ hơi trùng lặp, nhưng có một số khác biệt chính về thiết kế, khả năng và mục tiêu sử dụng:
 
- **Microsoft Agent Framework (MAF)**: Là SDK sẵn sàng sản xuất để xây dựng tác nhân AI. Nó cung cấp API tinh giản để tạo tác nhân với gọi công cụ, quản lý cuộc trò chuyện và tích hợp Azure Identity.
- **Microsoft Foundry Agent Service**: Là nền tảng và dịch vụ triển khai trong Microsoft Foundry cho tác nhân. Nó cung cấp kết nối tích hợp với các dịch vụ như Azure OpenAI, Azure AI Search, Bing Search và thực thi mã.
 
Vẫn chưa chắc chọn cái nào?

### Trường hợp sử dụng
 
Hãy xem liệu chúng tôi có thể giúp bạn thông qua một số trường hợp sử dụng phổ biến:
 
> Q: Tôi đang xây dựng ứng dụng tác nhân AI sản xuất và muốn bắt đầu nhanh chóng
>

>A: Microsoft Agent Framework là lựa chọn tuyệt vời. Nó cung cấp API đơn giản, phong cách Python qua `FoundryChatClient` cho phép bạn định nghĩa tác nhân với công cụ và hướng dẫn chỉ trong vài dòng mã.

>Q: Tôi cần triển khai cấp doanh nghiệp với tích hợp Azure như Tìm kiếm và thực thi mã
>
> A: Microsoft Foundry Agent Service phù hợp nhất. Đây là dịch vụ nền tảng cung cấp khả năng tích hợp sẵn cho nhiều mô hình, Azure AI Search, Bing Search và Azure Functions. Nó giúp bạn dễ dàng xây dựng tác nhân trong Foundry Portal và triển khai quy mô lớn.
 
> Q: Tôi vẫn còn bối rối, chỉ cho tôi một lựa chọn thôi
>
> A: Bắt đầu với Microsoft Agent Framework để xây dựng tác nhân của bạn, sau đó dùng Microsoft Foundry Agent Service khi cần triển khai và mở rộng trong sản xuất. Cách tiếp cận này giúp bạn nhanh chóng lặp lại logic tác nhân trong khi có con đường rõ ràng để triển khai doanh nghiệp.
 
Hãy tóm tắt các khác biệt chính trong bảng sau:

| Khung | Trọng tâm | Khái niệm cốt lõi | Trường hợp sử dụng |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK tác nhân tinh giản với gọi công cụ | Tác nhân, Công cụ, Azure Identity | Xây dựng tác nhân AI, sử dụng công cụ, quy trình làm việc đa bước |
| Microsoft Foundry Agent Service | Mô hình linh hoạt, bảo mật doanh nghiệp, tạo mã, gọi công cụ | Tính mô-đun, Hợp tác, Điều phối quy trình | Triển khai tác nhân AI bảo mật, mở rộng và linh hoạt |

## Tôi có thể tích hợp các công cụ hệ sinh thái Azure hiện tại của mình trực tiếp không, hay tôi cần các giải pháp độc lập?


Câu trả lời là có, bạn có thể tích hợp trực tiếp các công cụ hệ sinh thái Azure hiện có của mình với Microsoft Foundry Agent Service đặc biệt, vì nó được xây dựng để hoạt động liền mạch với các dịch vụ Azure khác. Ví dụ, bạn có thể tích hợp Bing, Azure AI Search và Azure Functions. Cũng có sự tích hợp sâu với Microsoft Foundry.

Microsoft Agent Framework cũng tích hợp với các dịch vụ Azure thông qua `FoundryChatClient` và nhận dạng Azure, cho phép bạn gọi các dịch vụ Azure trực tiếp từ các công cụ agent của mình.

## Mẫu Mã

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Có Thêm Câu Hỏi về AI Agent Frameworks?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Tham Khảo

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Bài Học Trước

[Giới Thiệu về AI Agents và Các Trường Hợp Sử Dụng Agent](../01-intro-to-ai-agents/README.md)

## Bài Học Tiếp Theo

[Hiểu Về Các Mẫu Thiết Kế Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->