---
name: microsoft-docs
description: Truy vấn tài liệu chính thức của Microsoft để tìm các khái niệm, hướng
  dẫn và ví dụ mã trên Azure, .NET, Agent Framework, Aspire, VS Code, GitHub và nhiều
  hơn nữa. Sử dụng Microsoft Learn MCP làm mặc định, với Context7 và Aspire MCP cho
  nội dung nằm ngoài learn.microsoft.com.
---
# Microsoft Docs

Kỹ năng nghiên cứu cho hệ sinh thái công nghệ Microsoft. Bao gồm learn.microsoft.com và tài liệu nằm ngoài trang đó (VS Code, GitHub, Aspire, các repo Agent Framework).

---

## Mặc định: Microsoft Learn MCP

Sử dụng những công cụ này cho **mọi thứ trên learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, và hơn thế nữa. Đây là công cụ chính cho phần lớn các truy vấn về tài liệu Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Tìm kiếm learn.microsoft.com — khái niệm, hướng dẫn, bài học, cấu hình |
| `microsoft_code_sample_search` | Tìm các đoạn mã hoạt động từ tài liệu Learn. Truyền `language` (`python`, `csharp`, etc.) để có kết quả tốt nhất |
| `microsoft_docs_fetch` | Lấy toàn bộ nội dung trang từ một URL cụ thể (khi đoạn trích tìm kiếm không đủ) |

Sử dụng `microsoft_docs_fetch` sau khi tìm kiếm khi bạn cần hướng dẫn đầy đủ, tất cả các tùy chọn cấu hình, hoặc khi các đoạn trích tìm kiếm bị rút gọn.

---

## Ngoại lệ: Khi nào sử dụng các công cụ khác

Các danh mục sau nằm **bên ngoài** learn.microsoft.com. Hãy sử dụng công cụ được chỉ định thay thế.

### .NET Aspire — Sử dụng Aspire MCP Server (ưu tiên) hoặc Context7

Tài liệu Aspire nằm trên **aspire.dev**, không phải Learn. Công cụ tốt nhất phụ thuộc vào phiên bản Aspire CLI của bạn:

**CLI 13.2+** (khuyến nghị) — Aspire MCP server bao gồm các công cụ tìm kiếm tài liệu tích hợp:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Liệt kê tất cả tài liệu có sẵn từ aspire.dev |
| `search_docs` | Tìm kiếm từ vựng có trọng số trên nội dung của aspire.dev |
| `get_doc` | Lấy một tài liệu cụ thể theo slug |

Những công cụ này được phát hành trong Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Để cập nhật: `aspire update --self --channel daily`. Tham khảo: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server cung cấp tra cứu tích hợp (`list_integrations`, `get_integration_docs`) nhưng **không** có tìm kiếm tài liệu. Quay về dùng Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Chính — hướng dẫn, tích hợp, tham chiếu CLI, triển khai |
| `/dotnet/aspire` | Nguồn runtime — nội bộ API, chi tiết triển khai |
| `/communitytoolkit/aspire` | Tích hợp cộng đồng — Go, Java, Node.js, Ollama |

### VS Code — Sử dụng Context7

Tài liệu VS Code nằm trên **code.visualstudio.com**, không phải Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Tài liệu người dùng — cài đặt, tính năng, gỡ lỗi, phát triển từ xa |
| `/websites/code_visualstudio_api` | API phần mở rộng — webviews, TreeViews, lệnh, điểm đóng góp |

### GitHub — Sử dụng Context7

Tài liệu GitHub nằm trên **docs.github.com** và **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, kho lưu trữ, bảo mật, quản trị, Copilot |
| `/websites/cli_github` | Lệnh và cờ của GitHub CLI (`gh`) |

### Agent Framework — Sử dụng Learn MCP + Context7

Các hướng dẫn Agent Framework có trên learn.microsoft.com (sử dụng `microsoft_docs_search`), nhưng **repo GitHub** có chi tiết ở cấp API thường đi trước tài liệu đã xuất bản — đặc biệt là tham chiếu DevUI REST API, tùy chọn CLI, và tích hợp .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Hướng dẫn — hướng dẫn DevUI, theo dõi, điều phối luồng công việc |
| `/microsoft/agent-framework` | Chi tiết API — endpoint REST DevUI, cờ CLI, xác thực, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Truy vấn nguồn trang Learn để lấy các hướng dẫn cách làm, sau đó truy vấn nguồn repo để biết các chi tiết ở cấp API (endpoint schemas, proxy config, auth tokens).

---

## Thiết lập Context7

Đối với bất kỳ truy vấn Context7 nào, hãy phân giải library ID trước (một lần cho mỗi phiên):

1. Gọi `mcp_context7_resolve-library-id` với tên công nghệ
2. Gọi `mcp_context7_query-docs` với ID thư viện trả về và một truy vấn cụ thể

---

## Viết truy vấn hiệu quả

Hãy cụ thể — bao gồm phiên bản, mục đích và ngôn ngữ:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Include context:
- **Version** khi cần thiết (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Mục đích tác vụ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Ngôn ngữ** cho tài liệu đa ngôn ngữ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Văn bản gốc bằng ngôn ngữ ban đầu nên được coi là nguồn có thẩm quyền. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->