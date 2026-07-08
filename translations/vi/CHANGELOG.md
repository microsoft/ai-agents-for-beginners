# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý đối với khóa học **AI Agents for Beginners** đều được ghi lại trong tập tin này.

## [Chưa phát hành] — 2026-07-06

Phiên bản này chuyển khóa học sang **Azure OpenAI Responses API**, chuẩn hóa tên sản phẩm trên **Microsoft Foundry** và **Microsoft Agent Framework (MAF)**, ngừng sử dụng GitHub Models, cập nhật phiên bản SDK, và thêm nội dung mới về mô hình cục bộ và hosting các framework khác trên Foundry.

### Đã thêm

- **Kỹ năng Migration** — Cài đặt Kỹ năng Agent [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (từ [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) dưới thư mục `.agents/skills/`, bao gồm các tham chiếu và script quét.
- **Foundry Local (chạy mô hình trên thiết bị)** — Mục "Nhà cung cấp thay thế: Foundry Local" mới trong [00-course-setup/README.md](./00-course-setup/README.md) bao gồm cài đặt (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, và kết nối `FoundryLocalManager` với Microsoft Agent Framework thông qua `OpenAIChatClient`.
- **Hosting các agent LangChain / LangGraph trên Microsoft Foundry** — Mục mới trong [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) cùng ví dụ chạy được [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) sử dụng `langchain-azure-ai[hosting]` và `ResponsesHostServer` (giao thức `/responses`), dựa trên [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Mục mới "Ví dụ Thực tế: Microsoft Project Opal" trong [15-browser-use/README.md](./15-browser-use/README.md) trình bày Opal như một agent hỗ trợ sử dụng máy tính doanh nghiệp và liên kết với các khái niệm khóa học (con người trong vòng lặp, tin cậy/bảo mật, lập kế hoạch, Kỹ năng).
- **Mẫu Python Bài học 02 thứ hai** — Thêm [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (xem phần "Đã thay đổi" — di chuyển từ notebook Semantic Kernel cũ) và liên kết trong README bài học.
- Thêm mục **Models và Providers** vào [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Đã thay đổi

- **Chat Completions → Responses API (Python).** Các mẫu gọi trực tiếp mô hình đã được chuyển từ Chat Completions sang Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), sử dụng client `OpenAI` với endpoint `/openai/v1/` ổn định của Azure OpenAI (không có `api_version`). Các mẫu bị ảnh hưởng bao gồm:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — hướng dẫn gọi hàm đầy đủ (lược đồ công cụ được chuyển sang định dạng Responses, kết quả công cụ được trả về dưới dạng `function_call_output`, `max_output_tokens`, v.v.).
- **GitHub Models → Azure OpenAI.** GitHub Models đã ngừng hoạt động (ngừng sử dụng vào **tháng 7 năm 2026**) và không hỗ trợ Responses API. Tất cả đường dẫn mã GitHub Models đã được chuyển sang Azure OpenAI / Microsoft Foundry trong các mẫu Python và .NET:
  - Python: các notebook luồng công việc Bài 08 (`01`–`03`), Bài 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` các file `*-dotnet-agent-framework.cs` cùng tài liệu `.md` kèm theo, và các notebook/.md luồng công việc .NET Bài 08 (`01`–`03`) hiện sử dụng `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` với `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Notebook `02-semantic-kernel.ipynb` trước đây đã được viết lại để sử dụng Microsoft Agent Framework với Azure OpenAI (Responses API) và đổi tên thành `02-python-agent-framework-azure-openai.ipynb`.
- **Chuẩn hóa dùng `FoundryChatClient` + `as_agent`.** README và mã notebook tham chiếu `AzureAIProjectAgentProvider` được chuẩn hóa theo mẫu tiêu chuẩn dùng trong Bài 01 và các ví dụ của framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` kèm `provider.as_agent(...)`. Cập nhật trên README và notebook từ Bài 02 đến 14 (ví dụ: bộ nhớ Bài 13, tất cả notebook Bài 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Đặt tên sản phẩm.** Đổi tên trong nội dung tiếng Anh:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Không thay đổi: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" và tên biến môi trường.)
- **Phụ thuộc** ([requirements.txt](../../requirements.txt)):
  - Gắn chặt `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Gắn chặt `openai>=1.108.1` (tối thiểu cho Responses API).
  - Loại bỏ `azure-ai-inference` (chỉ dùng bởi các mẫu GitHub Models đã chuyển đổi).
- **Cấu hình môi trường** ([.env.example](../../.env.example)): loại bỏ biến môi trường GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); thêm `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, và tùy chọn `AZURE_OPENAI_API_KEY`; cập nhật tên thành Microsoft Foundry.
- **Tài liệu** — Cập nhật [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), và [STUDY_GUIDE.md](./STUDY_GUIDE.md) cho các mục trên (cài đặt biến môi trường, đoạn mã kiểm tra, hướng dẫn nhà cung cấp, đặt tên).

### Đã loại bỏ

- Các bước onboarding GitHub Models và biến môi trường trong tài liệu cài đặt (đã được thay thế bởi Azure OpenAI / Microsoft Foundry).

### Bảo mật / Riêng tư (dọn dẹp chia sẻ công khai)

- Xóa các kết quả thực thi trong các Jupyter notebook làm lộ **ID đăng ký Azure** thật, tên nhóm tài nguyên / tài nguyên, ID kết nối Bing, cùng **đường dẫn tệp và tên người dùng cục bộ** của nhà phát triển, trong:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Đảm bảo không còn khóa API, token, ID đăng ký hoặc đường dẫn cá nhân nào còn xuất hiện trong nội dung tiếng Anh được theo dõi (các tham chiếu `GITHUB_TOKEN` còn lại là token GitHub Actions trong workflow và PAT máy chủ GitHub MCP ở Bài 11 — đều hợp lệ và không liên quan đến GitHub Models).

### Ghi chú và hạn chế đã biết

- **Không được chạy/biên dịch.** Đây là các mẫu học tập được cập nhật về tính đúng API / tên gọi; chúng chưa chạy trên tài nguyên Azure thực, và các mẫu .NET chưa được biên dịch trong môi trường này. Hãy kiểm tra với triển khai Microsoft Foundry / Azure OpenAI của bạn.
- **Triển khai mô hình phải hỗ trợ Responses API.** Sử dụng triển khai như `gpt-4o-mini`, `gpt-4.1`, hoặc mô hình `gpt-5.x`. Các mô hình cũ hơn hỗ trợ chức năng Responses cốt lõi nhưng không hỗ trợ tất cả tính năng.
- **Phiên bản agent-framework.** Các mẫu hướng tới MAF mới nhất (`>=1.10.0`). Lệnh tạo agent chuẩn là `client.as_agent(...)`; API được xác thực dựa trên tài liệu phát hành của framework và bản build đã cài đặt. Nếu bạn dùng phiên bản khác, hãy kiểm tra tính khả dụng của phương thức (`as_agent` so với `create_agent`).
- **Notebook workflow Bài 08 số 04** giữ nguyên `AzureAIAgentClient` (từ `agent-framework-azure-ai`) vì nó dùng các công cụ hosted của Microsoft Foundry Agent Service (như grounding Bing, trình diễn mã); nó đã dựa trên Responses.
- **Triển khai mặc định .NET.** Hai mẫu luồng công việc .NET Bài 08 trước đây hard-code `gpt-4o`; hiện chuyển mặc định sang `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Nếu mẫu dựa trên input đa phương tiện/nhìn, hãy đặt `AZURE_OPENAI_DEPLOYMENT` thành mô hình phù hợp.
- **Foundry Local** cung cấp điểm cuối **Chat Completions** tương thích OpenAI và dành cho phát triển cục bộ; hãy dùng Azure OpenAI / Microsoft Foundry để có đầy đủ tính năng Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->