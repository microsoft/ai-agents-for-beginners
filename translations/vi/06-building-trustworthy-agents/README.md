[![Agent AI Đáng Tin Cậy](../../../translated_images/vi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Nhấn vào hình ảnh phía trên để xem video của bài học này)_

# Xây Dựng Các Agent AI Đáng Tin Cậy

## Giới Thiệu

Bài học này sẽ bao gồm:

- Cách xây dựng và triển khai các Agent AI an toàn và hiệu quả
- Các cân nhắc bảo mật quan trọng khi phát triển Agent AI.
- Cách duy trì quyền riêng tư dữ liệu và người dùng khi phát triển Agent AI.

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xác định và giảm thiểu rủi ro khi tạo các Agent AI.
- Triển khai các biện pháp bảo mật để đảm bảo quản lý đúng cách dữ liệu và quyền truy cập.
- Tạo các Agent AI duy trì quyền riêng tư dữ liệu và cung cấp trải nghiệm người dùng chất lượng.

## An Toàn

Trước tiên, hãy xem xét việc xây dựng các ứng dụng agentic an toàn. An toàn có nghĩa là agent AI hoạt động theo thiết kế. Là người xây dựng các ứng dụng agentic, chúng ta có các phương pháp và công cụ để tối đa hóa sự an toàn:

### Xây Dựng Khung Thông Điệp Hệ Thống

Nếu bạn từng xây dựng một ứng dụng AI sử dụng Mô hình Ngôn ngữ Lớn (LLMs), bạn sẽ hiểu tầm quan trọng của việc thiết kế một lời nhắc hệ thống hoặc thông điệp hệ thống mạnh mẽ. Những lời nhắc này thiết lập các quy tắc meta, hướng dẫn và chỉ dẫn về cách LLM sẽ tương tác với người dùng và dữ liệu.

Đối với các Agent AI, lời nhắc hệ thống càng quan trọng hơn vì các Agent AI sẽ cần các chỉ dẫn rất cụ thể để hoàn thành các nhiệm vụ mà chúng ta đã thiết kế.

Để tạo các lời nhắc hệ thống có thể mở rộng, chúng ta có thể sử dụng một khung thông điệp hệ thống để xây dựng một hoặc nhiều agent trong ứng dụng của mình:

![Xây Dựng Khung Thông Điệp Hệ Thống](../../../translated_images/vi/system-message-framework.3a97368c92d11d68.webp)

#### Bước 1: Tạo Thông Điệp Hệ Thống Meta

Lời nhắc meta sẽ được một LLM sử dụng để tạo ra các lời nhắc hệ thống dành cho các agent mà chúng ta tạo. Ta thiết kế nó dưới dạng mẫu để có thể tạo nhanh nhiều agent nếu cần.

Đây là một ví dụ về thông điệp hệ thống meta mà chúng ta sẽ cung cấp cho LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Bước 2: Tạo lời nhắc cơ bản

Bước tiếp theo là tạo một lời nhắc cơ bản để mô tả Agent AI. Bạn nên bao gồm vai trò của agent, các nhiệm vụ agent sẽ thực hiện, và bất kỳ trách nhiệm nào khác của agent.

Ví dụ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Bước 3: Cung cấp Thông Điệp Hệ Thống Cơ Bản cho LLM

Bây giờ chúng ta có thể tối ưu thông điệp hệ thống này bằng cách cung cấp thông điệp hệ thống meta làm thông điệp hệ thống cùng với thông điệp hệ thống cơ bản của chúng ta.

Điều này sẽ tạo ra một thông điệp hệ thống được thiết kế tốt hơn để hướng dẫn các Agent AI của chúng ta:

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

#### Bước 4: Lặp lại và Cải thiện

Giá trị của khung thông điệp hệ thống này là giúp mở rộng việc tạo các thông điệp hệ thống từ nhiều agent một cách dễ dàng cũng như cải thiện các thông điệp hệ thống của bạn theo thời gian. Hiếm khi bạn có một thông điệp hệ thống hoàn hảo ngay từ lần đầu sử dụng cho toàn bộ trường hợp của bạn. Có thể thực hiện các chỉnh sửa nhỏ và cải tiến bằng cách thay đổi thông điệp hệ thống cơ bản và chạy nó qua hệ thống cho phép bạn so sánh và đánh giá kết quả.

## Hiểu Về Các Mối Đe Dọa

Để xây dựng các agent AI đáng tin cậy, điều quan trọng là hiểu và giảm thiểu các rủi ro và mối đe dọa đối với agent AI của bạn. Hãy xem qua một số mối đe dọa đối với các agent AI và cách bạn có thể lên kế hoạch và chuẩn bị tốt hơn cho chúng.

![Hiểu Về Các Mối Đe Dọa](../../../translated_images/vi/understanding-threats.89edeada8a97fc0f.webp)

### Nhiệm Vụ và Hướng Dẫn

**Mô tả:** Kẻ tấn công cố gắng thay đổi hướng dẫn hoặc mục tiêu của agent AI thông qua việc nhắc lệnh hoặc thao túng đầu vào.

**Giảm thiểu**: Thực hiện các kiểm tra xác thực và bộ lọc đầu vào để phát hiện các lời nhắc có thể nguy hiểm trước khi chúng được xử lý bởi Agent AI. Vì các cuộc tấn công này thường yêu cầu tương tác thường xuyên với Agent, giới hạn số lượt trong một cuộc hội thoại là cách khác để ngăn chặn các kiểu tấn công này.

### Truy Cập Hệ Thống Quan Trọng

**Mô tả**: Nếu một agent AI có quyền truy cập vào các hệ thống và dịch vụ lưu trữ dữ liệu nhạy cảm, kẻ tấn công có thể làm gián đoạn liên lạc giữa agent và các dịch vụ này. Đây có thể là các cuộc tấn công trực tiếp hoặc các nỗ lực gián tiếp nhằm thu thập thông tin về các hệ thống đó thông qua agent.

**Giảm thiểu**: Agent AI chỉ nên có quyền truy cập vào các hệ thống khi thật sự cần thiết để ngăn chặn các kiểu tấn công này. Liên lạc giữa agent và hệ thống cũng cần được bảo mật. Việc triển khai xác thực và kiểm soát truy cập là cách khác để bảo vệ thông tin này.

### Quá Tải Tài Nguyên và Dịch Vụ

**Mô tả:** Agent AI có thể truy cập các công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Kẻ tấn công có thể lợi dụng khả năng này để tấn công các dịch vụ bằng cách gửi số lượng lớn yêu cầu qua Agent AI, có thể dẫn đến lỗi hệ thống hoặc chi phí cao.

**Giảm thiểu:** Áp dụng các chính sách giới hạn số lượng yêu cầu mà một agent AI có thể gửi đến một dịch vụ. Giới hạn số lượt hội thoại và yêu cầu gửi đến agent cũng là cách khác để ngăn các kiểu tấn công này.

### Đầu Độc Cơ Sở Kiến Thức

**Mô tả:** Loại tấn công này không nhắm trực tiếp vào agent AI mà là vào cơ sở kiến thức và các dịch vụ mà agent AI sẽ sử dụng. Điều này có thể bao gồm làm hỏng dữ liệu hoặc thông tin mà agent AI sẽ dùng để hoàn thành nhiệm vụ, dẫn đến các phản hồi thiên vị hoặc không mong muốn với người dùng.

**Giảm thiểu:** Thực hiện kiểm tra định kỳ dữ liệu mà agent AI sẽ sử dụng trong các quy trình làm việc. Đảm bảo rằng quyền truy cập vào dữ liệu này được bảo mật và chỉ được thay đổi bởi những người đáng tin cậy để tránh kiểu tấn công này.

### Lỗi Kéo Theo

**Mô tả:** Agent AI truy cập vào các công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Các lỗi do kẻ tấn công gây ra có thể dẫn đến sự cố ở các hệ thống khác mà agent AI kết nối, khiến cuộc tấn công trở nên lan rộng và khó khắc phục hơn.

**Giảm thiểu**: Một phương pháp để tránh điều này là để agent AI hoạt động trong môi trường hạn chế, chẳng hạn như thực hiện nhiệm vụ trong container Docker, nhằm ngăn chặn các cuộc tấn công trực tiếp đến hệ thống. Tạo cơ chế dự phòng và logic thử lại khi một hệ thống phản hồi lỗi cũng là cách khác để ngăn ngừa sự cố hệ thống lớn hơn.

## Con Người Trong Vòng Lặp

Một cách hiệu quả khác để xây dựng hệ thống Agent AI đáng tin cậy là sử dụng Con Người Trong Vòng Lặp. Điều này tạo ra một luồng nơi người dùng có thể cung cấp phản hồi cho các Agent trong quá trình chạy. Người dùng về cơ bản đóng vai trò như các agent trong hệ thống đa agent và bằng cách cung cấp sự chấp thuận hoặc dừng quá trình đang chạy.

![Con Người Trong Vòng Lặp](../../../translated_images/vi/human-in-the-loop.5f0068a678f62f4f.webp)

Dưới đây là đoạn mã sử dụng Microsoft Agent Framework để minh họa cách khái niệm này được triển khai:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Tạo nhà cung cấp với sự phê duyệt có sự tham gia của con người
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Tạo đại lý với một bước phê duyệt của con người
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Người dùng có thể xem lại và phê duyệt phản hồi
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Kết Luận

Việc xây dựng các agent AI đáng tin cậy đòi hỏi thiết kế cẩn thận, các biện pháp bảo mật vững chắc và sự lặp lại liên tục. Bằng cách triển khai các hệ thống meta prompting có cấu trúc, hiểu rõ các mối đe dọa tiềm ẩn, và áp dụng các chiến lược giảm thiểu, các nhà phát triển có thể tạo ra các agent AI vừa an toàn vừa hiệu quả. Thêm vào đó, tích hợp phương pháp con người trong vòng lặp đảm bảo các agent AI luôn phù hợp với nhu cầu người dùng đồng thời giảm thiểu rủi ro. Khi AI tiếp tục phát triển, việc duy trì tư thế chủ động về bảo mật, quyền riêng tư, và các cân nhắc đạo đức sẽ là chìa khóa để xây dựng sự tin tưởng và độ tin cậy trong các hệ thống được điều khiển bởi AI.

### Có Thêm Câu Hỏi về Việc Xây Dựng Các Agent AI Đáng Tin Cậy?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự các giờ làm việc và nhận câu trả lời cho các câu hỏi về Agent AI của bạn.

## Tài Nguyên Bổ Sung

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tổng quan về AI có trách nhiệm</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các mô hình AI tạo sinh và ứng dụng AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Thông điệp hệ thống an toàn</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mẫu Đánh giá Rủi ro</a>

## Bài Học Trước

[Agentic RAG](../05-agentic-rag/README.md)

## Bài Học Tiếp Theo

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính thức và đáng tin cậy. Đối với các thông tin quan trọng, chúng tôi khuyên bạn nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ hiểu lầm hoặc cách hiểu sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->