[![Đại lý AI Đáng tin cậy](../../../translated_images/vi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Nhấp vào hình ảnh phía trên để xem video của bài học này)_

# Xây dựng Đại lý AI Đáng tin cậy

## Giới thiệu

Bài học này sẽ bao gồm:

- Cách xây dựng và triển khai các Đại lý AI an toàn và hiệu quả
- Những cân nhắc quan trọng về bảo mật khi phát triển Đại lý AI.
- Cách duy trì quyền riêng tư dữ liệu và người dùng khi phát triển Đại lý AI.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Nhận diện và giảm thiểu rủi ro khi tạo Đại lý AI.
- Thực hiện các biện pháp bảo mật để đảm bảo dữ liệu và quyền truy cập được quản lý đúng cách.
- Tạo ra các Đại lý AI giữ kín dữ liệu và cung cấp trải nghiệm người dùng chất lượng.

## An toàn

Trước tiên, hãy xem xét việc xây dựng các ứng dụng đại lý an toàn. An toàn có nghĩa là đại lý AI hoạt động như thiết kế. Là những nhà xây dựng ứng dụng đại lý, chúng ta có các phương pháp và công cụ để tối đa hóa độ an toàn:

### Xây dựng Khung Tin nhắn Hệ thống

Nếu bạn từng xây dựng ứng dụng AI sử dụng Mô hình Ngôn ngữ Lớn (LLMs), bạn sẽ biết tầm quan trọng của việc thiết kế một câu lệnh hệ thống hoặc tin nhắn hệ thống vững chắc. Những câu lệnh này thiết lập các quy tắc tổng thể, hướng dẫn và quy chuẩn về cách LLM tương tác với người dùng và dữ liệu.

Với Đại lý AI, câu lệnh hệ thống càng quan trọng hơn vì các Đại lý AI sẽ cần hướng dẫn cực kỳ cụ thể để hoàn thành các nhiệm vụ chúng ta thiết kế cho chúng.

Để tạo ra các câu lệnh hệ thống có thể mở rộng, chúng ta có thể sử dụng một khung tin nhắn hệ thống để xây dựng một hoặc nhiều đại lý trong ứng dụng của mình:

![Xây dựng Khung Tin nhắn Hệ thống](../../../translated_images/vi/system-message-framework.3a97368c92d11d68.webp)

#### Bước 1: Tạo một Tin nhắn Hệ thống Tổng quát

Câu lệnh tổng quát này sẽ được LLM sử dụng để tạo ra các câu lệnh hệ thống cho các đại lý mà chúng ta tạo. Chúng ta thiết kế nó như một mẫu để có thể tạo nhiều đại lý một cách hiệu quả nếu cần.

Đây là một ví dụ về tin nhắn hệ thống tổng quát mà chúng ta sẽ đưa cho LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Bước 2: Tạo câu lệnh cơ bản

Bước tiếp theo là tạo một câu lệnh cơ bản để mô tả Đại lý AI. Bạn nên bao gồm vai trò của đại lý, các nhiệm vụ đại lý sẽ hoàn thành và bất kỳ trách nhiệm nào khác của đại lý.

Đây là một ví dụ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Bước 3: Cung cấp Tin nhắn Hệ thống Cơ bản cho LLM

Bây giờ chúng ta có thể tối ưu tin nhắn hệ thống này bằng cách cung cấp tin nhắn hệ thống tổng quát làm tin nhắn hệ thống cùng với tin nhắn hệ thống cơ bản của chúng ta.

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

Giá trị của khung tin nhắn hệ thống này là có thể dễ dàng mở rộng việc tạo các tin nhắn hệ thống cho nhiều đại lý cũng như cải thiện các tin nhắn hệ thống theo thời gian. Hiếm khi bạn có được một tin nhắn hệ thống hoạt động hoàn hảo ngay lần đầu tiên cho toàn bộ trường hợp sử dụng của mình. Việc có thể thực hiện các chỉnh sửa nhỏ và cải tiến bằng cách thay đổi câu lệnh hệ thống cơ bản và chạy lại qua hệ thống sẽ giúp bạn so sánh và đánh giá kết quả.

## Hiểu các Mối đe dọa

Để xây dựng các đại lý AI đáng tin cậy, điều quan trọng là phải hiểu và giảm thiểu các rủi ro và mối đe dọa đối với đại lý AI của bạn. Hãy xem qua một số mối đe dọa khác nhau đối với đại lý AI và cách bạn có thể lên kế hoạch và chuẩn bị tốt hơn cho chúng.

![Hiểu các Mối đe dọa](../../../translated_images/vi/understanding-threats.89edeada8a97fc0f.webp)

### Nhiệm vụ và Hướng dẫn

**Mô tả:** Kẻ tấn công cố gắng thay đổi hướng dẫn hoặc mục tiêu của đại lý AI thông qua việc điều khiển câu lệnh hoặc thao túng đầu vào.

**Giảm thiểu**: Thực hiện các kiểm tra xác thực và bộ lọc đầu vào để phát hiện những câu lệnh tiềm ẩn nguy hiểm trước khi chúng được đại lý AI xử lý. Vì các cuộc tấn công này thường yêu cầu tương tác nhiều lần với Đại lý, việc giới hạn số lượt trong cuộc hội thoại là một cách khác để ngăn chặn loại tấn công này.

### Truy cập vào Hệ thống Quan trọng

**Mô tả**: Nếu đại lý AI có quyền truy cập vào các hệ thống và dịch vụ lưu trữ dữ liệu nhạy cảm, kẻ tấn công có thể làm gián đoạn giao tiếp giữa đại lý và các dịch vụ này. Đây có thể là các cuộc tấn công trực tiếp hoặc các cố gắng gián tiếp nhằm thu thập thông tin về các hệ thống này thông qua đại lý.

**Giảm thiểu**: Đại lý AI nên được cấp quyền truy cập theo nguyên tắc cần thiết để ngăn chặn các loại tấn công này. Giao tiếp giữa đại lý và hệ thống cũng phải được bảo mật. Thực hiện xác thực và kiểm soát truy cập là một cách khác để bảo vệ thông tin này.

### Tải quá Tài nguyên và Dịch vụ

**Mô tả:** Đại lý AI có thể truy cập các công cụ và dịch vụ khác nhau để hoàn thành nhiệm vụ. Kẻ tấn công có thể lợi dụng khả năng này để tấn công các dịch vụ bằng cách gửi lượng yêu cầu lớn qua Đại lý AI, điều này có thể dẫn đến sự cố hệ thống hoặc chi phí cao.

**Giảm thiểu:** Thực hiện các chính sách giới hạn số lượng yêu cầu mà một đại lý AI có thể gửi đến một dịch vụ. Giới hạn số lượt hội thoại và số yêu cầu gửi tới đại lý AI là cách khác để ngăn ngừa các loại tấn công này.

### Đầu độc Cơ sở Kiến thức

**Mô tả:** Loại tấn công này không nhằm trực tiếp vào đại lý AI mà nhắm vào cơ sở kiến thức và các dịch vụ khác mà đại lý AI sẽ sử dụng. Điều này có thể liên quan đến việc làm sai lệch dữ liệu hoặc thông tin mà đại lý AI sẽ dùng để hoàn thành nhiệm vụ, dẫn đến phản hồi thiên lệch hoặc không mong muốn đối với người dùng.

**Giảm thiểu:** Thực hiện kiểm tra thường xuyên dữ liệu mà đại lý AI sử dụng trong quy trình làm việc. Đảm bảo quyền truy cập dữ liệu được bảo mật và chỉ những cá nhân đáng tin cậy mới được phép thay đổi để tránh loại tấn công này.

### Lỗi Kéo theo

**Mô tả:** Đại lý AI truy cập vào nhiều công cụ và dịch vụ để hoàn thành nhiệm vụ. Các lỗi do kẻ tấn công gây ra có thể dẫn đến sự cố ở các hệ thống khác mà đại lý AI kết nối, khiến cuộc tấn công trở nên lan rộng và khó xử lý hơn.

**Giảm thiểu**: Một phương pháp để tránh điều này là để đại lý AI hoạt động trong môi trường giới hạn, chẳng hạn như thực hiện nhiệm vụ trong một Docker container, để ngăn chặn tấn công trực tiếp vào hệ thống. Tạo cơ chế dự phòng và logic thử lại khi một số hệ thống trả về lỗi là cách khác để ngăn chặn sự cố lớn hơn.

## Con người-trong-vòng-lặp

Một cách hiệu quả khác để xây dựng các hệ thống Đại lý AI đáng tin cậy là sử dụng Con người-trong-vòng-lặp. Điều này tạo ra một quy trình mà người dùng có thể đưa ra phản hồi cho các Đại lý trong khi nó đang chạy. Người dùng về cơ bản hoạt động như các đại lý trong một hệ thống đa đại lý bằng cách cung cấp sự chấp thuận hoặc kết thúc quá trình đang thực hiện.

![Con người trong Vòng lặp](../../../translated_images/vi/human-in-the-loop.5f0068a678f62f4f.webp)

Đây là một đoạn mã sử dụng Microsoft Agent Framework để cho thấy cách triển khai khái niệm này:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Tạo nhà cung cấp với sự phê duyệt có sự tham gia của con người
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Tạo tác nhân với một bước phê duyệt của con người
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

Xây dựng các đại lý AI đáng tin cậy đòi hỏi thiết kế cẩn thận, các biện pháp bảo mật chắc chắn và lặp lại liên tục. Bằng cách triển khai các hệ thống meta prompting có cấu trúc, hiểu các mối đe dọa tiềm năng và áp dụng các chiến lược giảm thiểu, các nhà phát triển có thể tạo ra đại lý AI vừa an toàn vừa hiệu quả. Thêm vào đó, việc kết hợp phương pháp con người-trong-vòng-lặp đảm bảo các đại lý AI luôn phù hợp với nhu cầu người dùng trong khi giảm thiểu rủi ro. Khi AI tiếp tục phát triển, việc duy trì quan điểm chủ động về bảo mật, quyền riêng tư và các cân nhắc đạo đức sẽ là chìa khóa để xây dựng niềm tin và độ tin cậy trong các hệ thống điều khiển bằng AI.

## Mẫu Code

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Hướng dẫn từng bước về khung chat meta-prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Các cổng phê duyệt trước hành động, phân lớp rủi ro và ghi chép kiểm tra cho các đại lý đáng tin cậy.

### Có thêm câu hỏi về xây dựng Đại lý AI Đáng tin cậy?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Đại lý AI của bạn.

## Tài nguyên Bổ sung

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tổng quan về AI Có Trách nhiệm</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các mô hình AI tạo sinh và ứng dụng AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Tin nhắn hệ thống an toàn</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Mẫu Đánh giá Rủi ro</a>

## Bài học trước

[Agentic RAG](../05-agentic-rag/README.md)

## Bài học tiếp theo

[Mẫu thiết kế Lập kế hoạch](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->