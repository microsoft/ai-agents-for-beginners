<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T18:40:41+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Tích Hợp MCP Server

## Yêu Cầu Trước
- Node.js đã được cài đặt (phiên bản 14 hoặc cao hơn)
- Trình quản lý gói npm
- Môi trường Python với các thư viện cần thiết

## Các Bước Thiết Lập

1. **Cài Đặt Gói MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Khởi Động MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server sẽ khởi động và hiển thị một URL kết nối.

3. **Xác Minh Kết Nối**  
   - Tìm biểu tượng phích cắm (🔌) trong giao diện Chainlit  
   - Một số (1) sẽ xuất hiện bên cạnh biểu tượng phích cắm, cho biết kết nối thành công  
   - Console sẽ hiển thị: "GitHub plugin setup completed successfully" (cùng với các dòng trạng thái bổ sung)

## Xử Lý Sự Cố

### Các Vấn Đề Thường Gặp

1. **Xung Đột Cổng**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Giải pháp: Thay đổi cổng bằng:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Vấn Đề Xác Thực**  
   - Đảm bảo thông tin đăng nhập GitHub được cấu hình đúng  
   - Kiểm tra tệp .env có chứa các token cần thiết  
   - Xác minh quyền truy cập API của GitHub

3. **Kết Nối Thất Bại**  
   - Xác nhận server đang chạy trên cổng mong đợi  
   - Kiểm tra cài đặt tường lửa  
   - Xác minh môi trường Python đã có các thư viện cần thiết

## Xác Minh Kết Nối

Server MCP của bạn được kết nối đúng khi:  
1. Console hiển thị "GitHub plugin setup completed successfully"  
2. Nhật ký kết nối hiển thị "✓ MCP Connection Status: Active"  
3. Các lệnh GitHub hoạt động trong giao diện chat

## Biến Môi Trường

Cần thiết trong tệp .env của bạn:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kiểm Tra Kết Nối

Gửi tin nhắn kiểm tra này trong chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Phản hồi thành công sẽ hiển thị thông tin kho lưu trữ.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.