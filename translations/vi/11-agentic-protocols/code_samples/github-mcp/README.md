# Ví dụ Github MCP Server

## Mô tả

Đây là một bản demo được tạo cho AI Agents Hackathon được tổ chức thông qua Microsoft Reactor.

Công cụ này được sử dụng để đề xuất các dự án hackathon dựa trên các repo Github của người dùng.
Điều này được thực hiện bằng:

1. **Github Agent** - Sử dụng Github MCP Server để truy xuất các repo và thông tin về những repo đó.
2. **Hackathon Agent** - Lấy dữ liệu từ Github Agent và đưa ra các ý tưởng dự án hackathon sáng tạo dựa trên các dự án, ngôn ngữ người dùng sử dụng và các chủ đề dự án cho AI Agents hackathon.
3. **Events Agent** - Dựa trên đề xuất của hackathon agent, events agent sẽ đề xuất các sự kiện liên quan từ chuỗi AI Agent Hackathon.
## Running the code 

### Environment Variables

Bản demo này sử dụng Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server và Azure AI Search.

Hãy chắc chắn rằng bạn đã thiết lập đúng các biến môi trường để sử dụng những công cụ này:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

Để kết nối với MCP server, demo này sử dụng Chainlit làm giao diện trò chuyện. 

Để chạy server, sử dụng lệnh sau trong terminal của bạn:

```bash
chainlit run app.py -w
```

Điều này sẽ khởi động Chainlit server của bạn trên `localhost:8000` cũng như điền Azure AI Search Index của bạn với nội dung của `event-descriptions.md`. 

## Connecting to the MCP Server

Để kết nối với Github MCP Server, chọn biểu tượng "plug" bên dưới hộp chat "Type your message here..":

![Kết nối MCP](../../../../../translated_images/vi/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Từ đó bạn có thể nhấp vào "Connect an MCP" để thêm lệnh kết nối tới Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Thay "[YOUR PERSONAL ACCESS TOKEN]" bằng Personal Access Token thực tế của bạn. 

Sau khi kết nối, bạn sẽ thấy một (1) bên cạnh biểu tượng plug để xác nhận rằng nó đã kết nối. Nếu không, hãy thử khởi động lại chainlit server bằng `chainlit run app.py -w`.

## Using the Demo 

Để bắt đầu quy trình agent đề xuất các dự án hackathon, bạn có thể gõ một tin nhắn như:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent sẽ phân tích yêu cầu của bạn và xác định sự kết hợp các agent (GitHub, Hackathon, và Events) phù hợp nhất để xử lý truy vấn của bạn. Các agent làm việc cùng nhau để cung cấp các đề xuất toàn diện dựa trên phân tích repository GitHub, ý tưởng dự án và các sự kiện công nghệ liên quan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa sai sót hoặc không chính xác. Văn bản gốc bằng ngôn ngữ ban đầu nên được coi là nguồn tham chiếu chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->