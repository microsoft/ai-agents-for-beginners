[![Trustworthy AI Agents](../../../translated_images/vi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Nhấp vào hình ảnh trên để xem video bài học này)_

# Xây dựng Các Đại lý AI Đáng Tin Cậy

## Giới thiệu

Bài học này sẽ bao gồm:

- Cách xây dựng và triển khai các Đại lý AI an toàn và hiệu quả
- Những cân nhắc quan trọng về bảo mật khi phát triển các Đại lý AI
- Cách duy trì bảo mật dữ liệu và quyền riêng tư người dùng khi phát triển các Đại lý AI

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xác định và giảm thiểu rủi ro khi tạo các Đại lý AI
- Thực hiện các biện pháp bảo mật để đảm bảo dữ liệu và quyền truy cập được quản lý đúng cách
- Tạo các Đại lý AI duy trì quyền riêng tư dữ liệu và mang lại trải nghiệm người dùng chất lượng

## An toàn

Trước tiên, hãy xem xét xây dựng các ứng dụng có tính đại lý an toàn. An toàn có nghĩa là đại lý AI hoạt động theo thiết kế. Là người xây dựng ứng dụng có tính đại lý, chúng ta có các phương pháp và công cụ để tối đa hóa an toàn:

### Xây dựng Khung Tin nhắn Hệ thống

Nếu bạn từng xây dựng ứng dụng AI sử dụng Mô hình Ngôn ngữ Lớn (LLMs), bạn sẽ hiểu tầm quan trọng của việc thiết kế lời nhắc hệ thống hoặc tin nhắn hệ thống vững chắc. Những lời nhắc này thiết lập các quy tắc meta, hướng dẫn và quy định về cách LLM tương tác với người dùng và dữ liệu.

Đối với các Đại lý AI, lời nhắc hệ thống còn quan trọng hơn vì các Đại lý AI cần các chỉ dẫn rất cụ thể để hoàn thành các nhiệm vụ mà chúng ta thiết kế cho chúng.

Để tạo lời nhắc hệ thống có thể mở rộng, chúng ta có thể sử dụng khung tin nhắn hệ thống để xây dựng một hoặc nhiều đại lý trong ứng dụng của mình:

![Building a System Message Framework](../../../translated_images/vi/system-message-framework.3a97368c92d11d68.webp)

#### Bước 1: Tạo Tin nhắn Meta Hệ thống

Lời nhắc meta sẽ được LLM sử dụng để tạo ra các lời nhắc hệ thống cho các đại lý mà chúng ta tạo. Chúng ta thiết kế nó dưới dạng mẫu để có thể tạo nhiều đại lý một cách hiệu quả nếu cần.

Dưới đây là ví dụ về tin nhắn meta hệ thống mà chúng ta cung cấp cho LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Bước 2: Tạo lời nhắc cơ bản

Bước tiếp theo là tạo một lời nhắc cơ bản để mô tả Đại lý AI. Bạn nên bao gồm vai trò của đại lý, các nhiệm vụ mà đại lý sẽ hoàn thành, và bất kỳ trách nhiệm nào khác của đại lý.

Dưới đây là ví dụ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Bước 3: Cung cấp Tin nhắn Hệ thống Cơ bản cho LLM

Giờ chúng ta có thể tối ưu tin nhắn hệ thống này bằng cách cung cấp tin nhắn meta hệ thống làm tin nhắn hệ thống cùng với tin nhắn hệ thống cơ bản của chúng ta.

Điều này sẽ tạo ra một tin nhắn hệ thống được thiết kế tốt hơn để hướng dẫn các đại lý AI của chúng ta:

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

Giá trị của khung tin nhắn hệ thống này là giúp dễ dàng mở rộng việc tạo tin nhắn hệ thống từ nhiều đại lý cũng như cải thiện tin nhắn hệ thống của bạn theo thời gian. Hiếm khi bạn có một tin nhắn hệ thống hoàn hảo ngay lần đầu tiên cho toàn bộ trường hợp sử dụng. Khả năng thực hiện các điều chỉnh nhỏ và cải tiến bằng cách thay đổi tin nhắn hệ thống cơ bản và chạy nó qua hệ thống cho phép bạn so sánh và đánh giá kết quả.

## Hiểu về Các Mối đe dọa

Để xây dựng các đại lý AI đáng tin cậy, rất quan trọng phải hiểu và giảm thiểu các rủi ro và mối đe dọa đối với đại lý AI của bạn. Hãy xem một số mối đe dọa khác nhau đối với các đại lý AI và cách bạn có thể lập kế hoạch và chuẩn bị tốt hơn để đối phó với chúng.

![Understanding Threats](../../../translated_images/vi/understanding-threats.89edeada8a97fc0f.webp)

### Nhiệm vụ và Hướng dẫn

**Mô tả:** Kẻ tấn công cố gắng thay đổi hướng dẫn hoặc mục tiêu của đại lý AI thông qua việc nhắc hoặc thao túng đầu vào.

**Giảm thiểu:** Thực hiện kiểm tra xác thực và bộ lọc đầu vào để phát hiện các lời nhắc có thể nguy hiểm trước khi chúng được đại lý AI xử lý. Vì các cuộc tấn công này thường yêu cầu tương tác thường xuyên với đại lý, giới hạn số lượt trong cuộc trò chuyện cũng là cách để ngăn ngừa kiểu tấn công này.

### Truy cập vào Hệ thống Quan trọng

**Mô tả:** Nếu đại lý AI có quyền truy cập vào các hệ thống và dịch vụ lưu trữ dữ liệu nhạy cảm, kẻ tấn công có thể làm tổn hại đến giao tiếp giữa đại lý và các dịch vụ này. Đây có thể là tấn công trực tiếp hoặc cố gắng gián tiếp thu thập thông tin về các hệ thống này qua đại lý.

**Giảm thiểu:** Các đại lý AI chỉ nên được phép truy cập các hệ thống khi cần thiết nhằm ngăn ngừa các loại tấn công này. Giao tiếp giữa đại lý và hệ thống cũng cần được bảo mật. Thực hiện xác thực và kiểm soát truy cập là một cách khác để bảo vệ thông tin này.

### Quá tải Tài nguyên và Dịch vụ

**Mô tả:** Đại lý AI có thể truy cập các công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Kẻ tấn công có thể tận dụng khả năng này để tấn công các dịch vụ đó bằng cách gửi lượng lớn yêu cầu qua Đại lý AI, có thể dẫn đến lỗi hệ thống hoặc chi phí cao.

**Giảm thiểu:** Triển khai các chính sách giới hạn số lượng yêu cầu mà đại lý AI được phép gửi đến một dịch vụ. Giới hạn số lượt trò chuyện và yêu cầu tới đại lý AI của bạn cũng là một cách khác để ngăn chặn các kiểu tấn công này.

### Đầu độc Cơ sở Kiến thức

**Mô tả:** Loại tấn công này không trực tiếp nhắm vào đại lý AI mà là nhắm tới cơ sở kiến thức và các dịch vụ khác mà đại lý AI sử dụng. Điều này có thể bao gồm làm hỏng dữ liệu hoặc thông tin mà đại lý AI sẽ dùng để hoàn thành nhiệm vụ, dẫn đến các phản hồi thiên lệch hoặc không như ý muốn đối với người dùng.

**Giảm thiểu:** Thực hiện kiểm tra định kỳ dữ liệu mà đại lý AI sử dụng trong các quy trình làm việc. Đảm bảo quyền truy cập vào dữ liệu này được bảo mật và chỉ có những người đáng tin cậy mới được thay đổi để tránh kiểu tấn công này.

### Lỗi Kéo theo

**Mô tả:** Đại lý AI truy cập nhiều công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Các lỗi do kẻ tấn công gây ra có thể làm hỏng các hệ thống khác mà đại lý AI kết nối, khiến cuộc tấn công trở nên lan rộng hơn và khó xử lý hơn.

**Giảm thiểu:** Một phương pháp để tránh điều này là để đại lý AI hoạt động trong môi trường giới hạn, ví dụ như thực hiện nhiệm vụ trong một container Docker, nhằm ngăn ngừa tấn công hệ thống trực tiếp. Tạo các cơ chế dự phòng và logic thử lại khi một số hệ thống phản hồi lỗi cũng là cách khác để ngăn ngừa lỗi hệ thống lớn hơn.

## Con Người Trong Vòng Lặp

Một cách hiệu quả khác để xây dựng các hệ thống đại lý AI đáng tin cậy là sử dụng con người trong vòng lặp (Human-in-the-loop). Điều này tạo ra một luồng mà người dùng có thể cung cấp phản hồi cho các Đại lý trong quá trình chạy. Người dùng về cơ bản đóng vai trò như các đại lý trong hệ thống đa đại lý và cung cấp sự chấp thuận hoặc ngừng quá trình đang chạy.

![Human in The Loop](../../../translated_images/vi/human-in-the-loop.5f0068a678f62f4f.webp)

Dưới đây là đoạn mã sử dụng Microsoft Agent Framework để minh họa cách triển khai khái niệm này:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Tạo nhà cung cấp với sự phê duyệt có sự tham gia của con người
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Tạo đại lý với bước phê duyệt của con người
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Người dùng có thể xem xét và phê duyệt phản hồi
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Kết luận

Xây dựng các đại lý AI đáng tin cậy đòi hỏi thiết kế cẩn thận, biện pháp bảo mật vững chắc và quá trình lặp lại liên tục. Bằng cách triển khai hệ thống meta prompt có cấu trúc, hiểu rõ các mối đe dọa tiềm ẩn và áp dụng các chiến lược giảm thiểu, các nhà phát triển có thể tạo ra các đại lý AI vừa an toàn vừa hiệu quả. Ngoài ra, kết hợp phương pháp con người trong vòng lặp đảm bảo các đại lý AI luôn phù hợp với nhu cầu người dùng đồng thời giảm thiểu rủi ro. Khi AI tiếp tục phát triển, duy trì thái độ chủ động trong bảo mật, quyền riêng tư và các cân nhắc đạo đức sẽ là chìa khóa để xây dựng niềm tin và độ tin cậy trong các hệ thống dựa trên AI.

## Mẫu mã lập trình

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Minh họa từng bước về khung hệ thống lời nhắc meta.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Cổng phê duyệt trước hành động, phân loại rủi ro, và ghi nhật ký kiểm toán cho các đại lý đáng tin cậy.

### Có nhiều câu hỏi hơn về Xây dựng Đại lý AI Đáng Tin Cậy?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Đại lý AI của bạn.

## Tài nguyên bổ sung

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tổng quan AI có Trách nhiệm</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các mô hình AI tạo sinh và ứng dụng AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Tin nhắn hệ thống an toàn</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mẫu Đánh giá Rủi ro</a>

## Bài học trước

[Agentic RAG](../05-agentic-rag/README.md)

## Bài học tiếp theo

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->