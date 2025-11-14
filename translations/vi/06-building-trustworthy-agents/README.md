<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T17:50:52+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "vi"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.vi.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Nhấn vào hình ảnh trên để xem video của bài học này)_

# Xây dựng các tác nhân AI đáng tin cậy

## Giới thiệu

Bài học này sẽ đề cập đến:

- Cách xây dựng và triển khai các tác nhân AI an toàn và hiệu quả.
- Các cân nhắc quan trọng về bảo mật khi phát triển các tác nhân AI.
- Cách duy trì quyền riêng tư dữ liệu và người dùng khi phát triển các tác nhân AI.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xác định và giảm thiểu rủi ro khi tạo các tác nhân AI.
- Triển khai các biện pháp bảo mật để đảm bảo dữ liệu và quyền truy cập được quản lý đúng cách.
- Tạo các tác nhân AI duy trì quyền riêng tư dữ liệu và mang lại trải nghiệm người dùng chất lượng.

## An toàn

Hãy bắt đầu với việc xây dựng các ứng dụng tác nhân an toàn. An toàn có nghĩa là tác nhân AI hoạt động đúng như thiết kế. Là người xây dựng các ứng dụng tác nhân, chúng ta có các phương pháp và công cụ để tối đa hóa sự an toàn:

### Xây dựng khung thông điệp hệ thống

Nếu bạn đã từng xây dựng một ứng dụng AI sử dụng các mô hình ngôn ngữ lớn (LLMs), bạn sẽ hiểu tầm quan trọng của việc thiết kế một thông điệp hệ thống mạnh mẽ. Những thông điệp này thiết lập các quy tắc, hướng dẫn và chỉ dẫn cho cách LLM tương tác với người dùng và dữ liệu.

Đối với các tác nhân AI, thông điệp hệ thống càng quan trọng hơn vì các tác nhân AI cần các chỉ dẫn rất cụ thể để hoàn thành các nhiệm vụ mà chúng ta thiết kế cho chúng.

Để tạo các thông điệp hệ thống có thể mở rộng, chúng ta có thể sử dụng một khung thông điệp hệ thống để xây dựng một hoặc nhiều tác nhân trong ứng dụng của mình:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.vi.png)

#### Bước 1: Tạo một thông điệp hệ thống meta

Thông điệp meta sẽ được sử dụng bởi LLM để tạo các thông điệp hệ thống cho các tác nhân mà chúng ta tạo. Chúng ta thiết kế nó như một mẫu để có thể tạo nhiều tác nhân một cách hiệu quả nếu cần.

Dưới đây là một ví dụ về thông điệp hệ thống meta mà chúng ta sẽ cung cấp cho LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Bước 2: Tạo một thông điệp cơ bản

Bước tiếp theo là tạo một thông điệp cơ bản để mô tả tác nhân AI. Bạn nên bao gồm vai trò của tác nhân, các nhiệm vụ mà tác nhân sẽ hoàn thành, và bất kỳ trách nhiệm nào khác của tác nhân.

Dưới đây là một ví dụ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Bước 3: Cung cấp thông điệp hệ thống cơ bản cho LLM

Bây giờ chúng ta có thể tối ưu hóa thông điệp hệ thống này bằng cách cung cấp thông điệp hệ thống meta như thông điệp hệ thống và thông điệp hệ thống cơ bản của chúng ta.

Điều này sẽ tạo ra một thông điệp hệ thống được thiết kế tốt hơn để hướng dẫn các tác nhân AI của chúng ta:

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

#### Bước 4: Lặp lại và cải thiện

Giá trị của khung thông điệp hệ thống này là khả năng mở rộng việc tạo thông điệp hệ thống cho nhiều tác nhân dễ dàng hơn cũng như cải thiện thông điệp hệ thống của bạn theo thời gian. Hiếm khi bạn có một thông điệp hệ thống hoạt động hoàn hảo ngay từ lần đầu tiên cho toàn bộ trường hợp sử dụng. Việc có thể thực hiện các điều chỉnh nhỏ và cải tiến bằng cách thay đổi thông điệp hệ thống cơ bản và chạy nó qua hệ thống sẽ cho phép bạn so sánh và đánh giá kết quả.

## Hiểu các mối đe dọa

Để xây dựng các tác nhân AI đáng tin cậy, điều quan trọng là phải hiểu và giảm thiểu các rủi ro và mối đe dọa đối với tác nhân AI của bạn. Hãy cùng xem một số mối đe dọa khác nhau đối với các tác nhân AI và cách bạn có thể lập kế hoạch và chuẩn bị tốt hơn.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.vi.png)

### Nhiệm vụ và chỉ dẫn

**Mô tả:** Kẻ tấn công cố gắng thay đổi các chỉ dẫn hoặc mục tiêu của tác nhân AI thông qua việc nhắc nhở hoặc thao túng đầu vào.

**Giảm thiểu:** Thực hiện kiểm tra xác thực và bộ lọc đầu vào để phát hiện các nhắc nhở nguy hiểm tiềm ẩn trước khi chúng được xử lý bởi tác nhân AI. Vì các cuộc tấn công này thường yêu cầu tương tác thường xuyên với tác nhân, việc giới hạn số lượt trong một cuộc trò chuyện là một cách khác để ngăn chặn các cuộc tấn công loại này.

### Truy cập vào các hệ thống quan trọng

**Mô tả:** Nếu một tác nhân AI có quyền truy cập vào các hệ thống và dịch vụ lưu trữ dữ liệu nhạy cảm, kẻ tấn công có thể xâm phạm giao tiếp giữa tác nhân và các dịch vụ này. Đây có thể là các cuộc tấn công trực tiếp hoặc các nỗ lực gián tiếp để lấy thông tin về các hệ thống này thông qua tác nhân.

**Giảm thiểu:** Các tác nhân AI chỉ nên có quyền truy cập vào các hệ thống khi thực sự cần thiết để ngăn chặn các cuộc tấn công loại này. Giao tiếp giữa tác nhân và hệ thống cũng nên được bảo mật. Việc triển khai xác thực và kiểm soát truy cập là một cách khác để bảo vệ thông tin này.

### Quá tải tài nguyên và dịch vụ

**Mô tả:** Các tác nhân AI có thể truy cập các công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Kẻ tấn công có thể sử dụng khả năng này để tấn công các dịch vụ bằng cách gửi một lượng lớn yêu cầu thông qua tác nhân AI, dẫn đến lỗi hệ thống hoặc chi phí cao.

**Giảm thiểu:** Triển khai các chính sách để giới hạn số lượng yêu cầu mà một tác nhân AI có thể gửi đến một dịch vụ. Giới hạn số lượt trò chuyện và yêu cầu đến tác nhân AI của bạn là một cách khác để ngăn chặn các cuộc tấn công loại này.

### Làm nhiễm độc cơ sở tri thức

**Mô tả:** Loại tấn công này không nhắm trực tiếp vào tác nhân AI mà nhắm vào cơ sở tri thức và các dịch vụ khác mà tác nhân AI sẽ sử dụng. Điều này có thể bao gồm việc làm hỏng dữ liệu hoặc thông tin mà tác nhân AI sẽ sử dụng để hoàn thành nhiệm vụ, dẫn đến các phản hồi thiên vị hoặc không mong muốn cho người dùng.

**Giảm thiểu:** Thực hiện xác minh thường xuyên dữ liệu mà tác nhân AI sẽ sử dụng trong quy trình làm việc của mình. Đảm bảo rằng quyền truy cập vào dữ liệu này được bảo mật và chỉ được thay đổi bởi những cá nhân đáng tin cậy để tránh loại tấn công này.

### Lỗi lan truyền

**Mô tả:** Các tác nhân AI truy cập vào nhiều công cụ và dịch vụ để hoàn thành nhiệm vụ. Các lỗi do kẻ tấn công gây ra có thể dẫn đến sự cố của các hệ thống khác mà tác nhân AI được kết nối, khiến cuộc tấn công trở nên lan rộng hơn và khó khắc phục hơn.

**Giảm thiểu:** Một phương pháp để tránh điều này là để tác nhân AI hoạt động trong một môi trường hạn chế, chẳng hạn như thực hiện nhiệm vụ trong một container Docker, để ngăn chặn các cuộc tấn công trực tiếp vào hệ thống. Tạo các cơ chế dự phòng và logic thử lại khi một số hệ thống phản hồi lỗi là một cách khác để ngăn chặn các sự cố hệ thống lớn hơn.

## Con người trong vòng lặp

Một cách hiệu quả khác để xây dựng các hệ thống tác nhân AI đáng tin cậy là sử dụng con người trong vòng lặp. Điều này tạo ra một luồng nơi người dùng có thể cung cấp phản hồi cho các tác nhân trong quá trình chạy. Người dùng về cơ bản đóng vai trò như các tác nhân trong một hệ thống đa tác nhân và bằng cách cung cấp sự chấp thuận hoặc chấm dứt quy trình đang chạy.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.vi.png)

Dưới đây là một đoạn mã sử dụng AutoGen để minh họa cách khái niệm này được triển khai:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Kết luận

Xây dựng các tác nhân AI đáng tin cậy đòi hỏi thiết kế cẩn thận, các biện pháp bảo mật mạnh mẽ và sự lặp lại liên tục. Bằng cách triển khai các hệ thống nhắc nhở meta có cấu trúc, hiểu các mối đe dọa tiềm ẩn và áp dụng các chiến lược giảm thiểu, các nhà phát triển có thể tạo ra các tác nhân AI vừa an toàn vừa hiệu quả. Ngoài ra, việc kết hợp cách tiếp cận con người trong vòng lặp đảm bảo rằng các tác nhân AI vẫn phù hợp với nhu cầu của người dùng đồng thời giảm thiểu rủi ro. Khi AI tiếp tục phát triển, duy trì một lập trường chủ động về bảo mật, quyền riêng tư và các cân nhắc đạo đức sẽ là chìa khóa để thúc đẩy sự tin tưởng và độ tin cậy trong các hệ thống do AI điều khiển.

### Có thêm câu hỏi về việc xây dựng các tác nhân AI đáng tin cậy?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về tác nhân AI của bạn.

## Tài nguyên bổ sung

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tổng quan về AI có trách nhiệm</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các mô hình AI tạo sinh và ứng dụng AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Thông điệp hệ thống an toàn</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mẫu đánh giá rủi ro</a>

## Bài học trước

[Agentic RAG](../05-agentic-rag/README.md)

## Bài học tiếp theo

[Planning Design Pattern](../07-planning-design/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.