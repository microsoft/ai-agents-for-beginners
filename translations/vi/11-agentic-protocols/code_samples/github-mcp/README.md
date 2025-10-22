<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T18:33:43+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "vi"
}
-->
# Github MCP Server Example

## Mô tả

Đây là một bản demo được tạo ra cho cuộc thi Hackathon AI Agents do Microsoft Reactor tổ chức.

Công cụ này được sử dụng để đề xuất các dự án hackathon dựa trên các kho lưu trữ Github của người dùng. Điều này được thực hiện thông qua:

1. **Github Agent** - Sử dụng Github MCP Server để truy xuất các kho lưu trữ và thông tin về các kho lưu trữ đó.
2. **Hackathon Agent** - Sử dụng dữ liệu từ Github Agent để đưa ra các ý tưởng sáng tạo cho dự án hackathon dựa trên các dự án, ngôn ngữ lập trình mà người dùng sử dụng và các chủ đề của cuộc thi Hackathon AI Agents.
3. **Events Agent** - Dựa trên gợi ý của Hackathon Agent, Events Agent sẽ đề xuất các sự kiện liên quan từ chuỗi sự kiện Hackathon AI Agents.

## Chạy mã 

### Biến môi trường

Bản demo này sử dụng Azure Open AI Service, Semantic Kernel, Github MCP Server và Azure AI Search.

Hãy đảm bảo rằng bạn đã thiết lập đúng các biến môi trường để sử dụng các công cụ này:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chạy Chainlit Server

Để kết nối với MCP Server, bản demo này sử dụng Chainlit làm giao diện trò chuyện.

Để chạy server, sử dụng lệnh sau trong terminal của bạn:

```bash
chainlit run app.py -w
```

Lệnh này sẽ khởi động Chainlit server trên `localhost:8000` và đồng thời điền nội dung từ tệp `event-descriptions.md` vào Azure AI Search Index.

## Kết nối với MCP Server

Để kết nối với Github MCP Server, chọn biểu tượng "plug" bên dưới hộp trò chuyện "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.vi.png)

Từ đó, bạn có thể nhấp vào "Connect an MCP" để thêm lệnh kết nối với Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Thay thế "[YOUR PERSONAL ACCESS TOKEN]" bằng Personal Access Token thực tế của bạn.

Sau khi kết nối, bạn sẽ thấy số (1) bên cạnh biểu tượng plug để xác nhận rằng đã kết nối thành công. Nếu không, hãy thử khởi động lại Chainlit server bằng lệnh `chainlit run app.py -w`.

## Sử dụng bản demo 

Để bắt đầu quy trình làm việc của agent nhằm đề xuất các dự án hackathon, bạn có thể nhập một tin nhắn như:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent sẽ phân tích yêu cầu của bạn và xác định sự kết hợp tốt nhất giữa các agent (GitHub, Hackathon, và Events) để xử lý truy vấn của bạn. Các agent sẽ phối hợp với nhau để cung cấp các đề xuất toàn diện dựa trên phân tích kho lưu trữ Github, ý tưởng dự án, và các sự kiện công nghệ liên quan.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.