---
name: microsoft-docs
description: Truy vấn tài liệu chính thức của Microsoft để tìm các khái niệm, hướng
  dẫn và ví dụ mã trên Azure, .NET, Agent Framework, Aspire, VS Code, GitHub và nhiều
  hơn nữa. Sử dụng Microsoft Learn MCP làm mặc định, với Context7 và Aspire MCP cho
  nội dung nằm ngoài learn.microsoft.com.
---
# Tài liệu Microsoft

Kỹ năng nghiên cứu cho hệ sinh thái công nghệ Microsoft. Bao gồm learn.microsoft.com và tài liệu nằm ngoài nó (VS Code, GitHub, Aspire, các kho Agent Framework).

---

## Mặc định: Microsoft Learn MCP

Sử dụng các công cụ này cho **mọi thứ trên learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, và nhiều hơn nữa. Đây là công cụ chính cho đa số các truy vấn tài liệu Microsoft.

| Công cụ | Mục đích |
|------|---------|
| `microsoft_docs_search` | Tìm kiếm learn.microsoft.com — khái niệm, hướng dẫn, bài học, cấu hình |
| `microsoft_code_sample_search` | Tìm đoạn mã hoạt động từ tài liệu Learn. Truyền `language` (`python`, `csharp`, v.v.) để có kết quả tốt nhất |
| `microsoft_docs_fetch` | Lấy nội dung trang đầy đủ từ URL cụ thể (khi đoạn trích tìm kiếm không đủ) |

Sử dụng `microsoft_docs_fetch` sau khi tìm kiếm khi bạn cần bài học hoàn chỉnh, tất cả các tùy chọn cấu hình, hoặc khi đoạn trích tìm kiếm bị cắt bớt.

---

## Ngoại lệ: Khi nào sử dụng công cụ khác

Các danh mục sau nằm **ngoài** learn.microsoft.com. Sử dụng công cụ chỉ định thay thế.

### Aspire — Sử dụng Aspire MCP Server (ưu tiên) hoặc Context7

Tài liệu Aspire nằm trên **aspire.dev**, không phải Learn. Công cụ tốt nhất phụ thuộc vào phiên bản Aspire CLI của bạn:

**CLI 13.2+** (khuyến nghị) — Máy chủ Aspire MCP bao gồm công cụ tìm kiếm tài liệu tích hợp:

| Công cụ MCP | Mô tả |
|----------|-------------|
| `list_docs` | Liệt kê tất cả tài liệu có sẵn từ aspire.dev |
| `search_docs` | Tìm kiếm trọng số theo từ ngữ trên nội dung aspire.dev |
| `get_doc` | Truy xuất tài liệu cụ thể theo slug |

Những công cụ này được phát hành trong Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Để cập nhật: `aspire update --self --channel daily`.

**CLI 13.1** — Máy chủ MCP cung cấp tra cứu tích hợp (`list_integrations`, `get_integration_docs`) nhưng **không** có tìm kiếm tài liệu. Lùi về sử dụng Context7:

| ID Thư viện | Sử dụng cho |
|---|---|
| `/microsoft/aspire.dev` | Chính — hướng dẫn, tích hợp, tham chiếu CLI, triển khai |
| `/microsoft/aspire` | Nguồn runtime — API nội bộ, chi tiết triển khai |
| `/communitytoolkit/aspire` | Tích hợp cộng đồng — Go, Java, Node.js, Ollama |

### VS Code — Sử dụng Context7

Tài liệu VS Code nằm trên **code.visualstudio.com**, không phải Learn.

| ID Thư viện | Sử dụng cho |
|---|---|
| `/websites/code_visualstudio` | Tài liệu người dùng — cài đặt, tính năng, gỡ lỗi, phát triển từ xa |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, lệnh, điểm đóng góp |

### GitHub — Sử dụng Context7

Tài liệu GitHub nằm trên **docs.github.com** và **cli.github.com**.

| ID Thư viện | Sử dụng cho |
|---|---|
| `/websites/github_en` | Actions, API, repo, bảo mật, quản trị, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) lệnh và cờ |

### Agent Framework — Sử dụng Learn MCP + Context7

Các bài học Agent Framework có trên learn.microsoft.com (sử dụng `microsoft_docs_search`), nhưng **kho GitHub** có chi tiết mức API thường đi trước tài liệu đã xuất bản — đặc biệt là tham chiếu REST API DevUI, tùy chọn CLI, và tích hợp .NET.

| ID Thư viện | Sử dụng cho |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Bài học — hướng dẫn DevUI, theo dõi, phối hợp luồng công việc |
| `/microsoft/agent-framework` | Chi tiết API — điểm cuối REST DevUI, cờ CLI, xác thực, .NET `AddDevUI`/`MapDevUI` |

**Mẹo DevUI:** Tra cứu nguồn trang Learn cho hướng dẫn cách làm, sau đó tra cứu nguồn kho cho chi tiết mức API (lược đồ điểm cuối, cấu hình proxy, token xác thực).

---

## Cài đặt Context7

Đối với bất kỳ truy vấn Context7 nào, hãy xác định ID thư viện trước (mỗi phiên chỉ một lần):

1. Gọi `mcp_context7_resolve-library-id` với tên công nghệ
2. Gọi `mcp_context7_query-docs` với ID thư viện trả về và truy vấn cụ thể

---

## Viết truy vấn hiệu quả

Hãy cụ thể — bao gồm phiên bản, mục đích, và ngôn ngữ:

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

Bao gồm bối cảnh:
- **Phiên bản** khi cần thiết (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Mục đích nhiệm vụ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Ngôn ngữ** cho tài liệu đa ngôn ngữ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->