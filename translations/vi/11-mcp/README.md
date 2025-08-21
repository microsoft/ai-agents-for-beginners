<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:33:02+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "vi"
}
-->
# Bài học 11: Tích hợp Giao thức Ngữ cảnh Mô hình (MCP)

## Giới thiệu về Giao thức Ngữ cảnh Mô hình (MCP)

Giao thức Ngữ cảnh Mô hình (MCP) là một khung làm việc tiên tiến được thiết kế để chuẩn hóa các tương tác giữa các mô hình AI và ứng dụng khách. MCP đóng vai trò như một cầu nối giữa các mô hình AI và các ứng dụng sử dụng chúng, cung cấp một giao diện nhất quán bất kể cách triển khai mô hình bên dưới.

Các khía cạnh chính của MCP:

- **Giao tiếp chuẩn hóa**: MCP thiết lập một ngôn ngữ chung để các ứng dụng giao tiếp với các mô hình AI
- **Quản lý ngữ cảnh nâng cao**: Cho phép truyền thông tin ngữ cảnh hiệu quả đến các mô hình AI
- **Tương thích đa nền tảng**: Hoạt động trên nhiều ngôn ngữ lập trình như C#, Java, JavaScript, Python và TypeScript
- **Tích hợp liền mạch**: Giúp các nhà phát triển dễ dàng tích hợp các mô hình AI khác nhau vào ứng dụng của họ

MCP đặc biệt hữu ích trong việc phát triển các tác nhân AI, vì nó cho phép các tác nhân tương tác với nhiều hệ thống và nguồn dữ liệu thông qua một giao thức thống nhất, làm cho các tác nhân trở nên linh hoạt và mạnh mẽ hơn.

## Mục tiêu học tập
- Hiểu MCP là gì và vai trò của nó trong phát triển tác nhân AI
- Thiết lập và cấu hình máy chủ MCP để tích hợp với GitHub
- Xây dựng hệ thống đa tác nhân bằng các công cụ MCP
- Triển khai RAG (Retrieval Augmented Generation) với Azure Cognitive Search

## Yêu cầu trước
- Python 3.8+
- Node.js 14+
- Tài khoản Azure
- Tài khoản GitHub
- Kiến thức cơ bản về Semantic Kernel

## Hướng dẫn thiết lập

1. **Thiết lập môi trường**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Cấu hình dịch vụ Azure**
   - Tạo tài nguyên Azure Cognitive Search
   - Thiết lập dịch vụ Azure OpenAI
   - Cấu hình biến môi trường trong `.env`

3. **Thiết lập máy chủ MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Cấu trúc dự án

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Các thành phần cốt lõi

### 1. Hệ thống đa tác nhân
- Tác nhân GitHub: Phân tích kho lưu trữ
- Tác nhân Hackathon: Gợi ý dự án
- Tác nhân Sự kiện: Đề xuất sự kiện công nghệ

### 2. Tích hợp Azure
- Cognitive Search để lập chỉ mục sự kiện
- Azure OpenAI để cung cấp trí thông minh cho tác nhân
- Triển khai mô hình RAG

### 3. Công cụ MCP
- Phân tích kho lưu trữ GitHub
- Kiểm tra mã nguồn
- Trích xuất siêu dữ liệu

## Hướng dẫn mã

Ví dụ minh họa:
1. Tích hợp máy chủ MCP
2. Điều phối hệ thống đa tác nhân
3. Tích hợp Azure Cognitive Search
4. Triển khai mô hình RAG

Các tính năng chính:
- Phân tích kho lưu trữ GitHub theo thời gian thực
- Gợi ý dự án thông minh
- Ghép nối sự kiện bằng Azure Search
- Phản hồi theo luồng với Chainlit

## Chạy ví dụ

Để biết hướng dẫn thiết lập chi tiết và thêm thông tin, tham khảo [README ví dụ máy chủ MCP GitHub](./code_samples/github-mcp/README.md).

1. Khởi động máy chủ MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Khởi chạy ứng dụng:
   ```bash
   chainlit run app.py -w
   ```

3. Kiểm tra tích hợp:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Xử lý sự cố

Các vấn đề thường gặp và cách giải quyết:
1. Vấn đề kết nối MCP
   - Xác minh máy chủ đang chạy
   - Kiểm tra khả dụng của cổng
   - Xác nhận token GitHub

2. Vấn đề Azure Search
   - Kiểm tra chuỗi kết nối
   - Xác minh sự tồn tại của chỉ mục
   - Kiểm tra việc tải lên tài liệu

## Bước tiếp theo
- Khám phá thêm các công cụ MCP
- Triển khai các tác nhân tùy chỉnh
- Nâng cao khả năng RAG
- Thêm nhiều nguồn sự kiện hơn
- **Nâng cao**: Xem [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) để biết ví dụ về giao tiếp giữa các tác nhân

## Tài nguyên
- [MCP cho người mới bắt đầu](https://aka.ms/mcp-for-beginners)  
- [Tài liệu MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Tài liệu Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Hướng dẫn Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.