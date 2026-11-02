# Nhật ký thay đổi

Mọi thay đổi đáng chú ý trong khóa học **AI Agents for Beginners** đều được ghi lại trong tệp này.

## [Phát hành] — 2026-07-14

Phiên bản này chuyển khóa học khỏi hai mô hình mới bị loại bỏ, di chuyển các sổ tay Bài học còn lại sang API Microsoft Agent Framework ổn định, và xác thực các sổ tay Python so với một triển khai Microsoft Foundry đang hoạt động.

### Đã thay đổi

- **Chuyển khỏi mô hình bị loại bỏ (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Cả `gpt-4.1` và `gpt-4.1-mini` hiện đã bị loại bỏ (ngày nghỉ hưu công bố là **14 tháng 10 năm 2026**). Thay thế mọi tham chiếu trong khóa học (tài liệu, `.env.example`, sổ tay Python/.NET và ví dụ) bằng `gpt-5-mini` không bị loại bỏ. Ví dụ định tuyến mô hình trong Bài học 16 giữ sự đối lập nhỏ/lớn bằng `gpt-5-nano` (nhỏ) và `gpt-5-mini` (lớn). Các tệp bên thứ ba được đóng gói ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), văn bản Mô hình GitHub lịch sử, và ghi chú năng lực của kỹ năng `azure-openai-to-responses` được giữ nguyên không thay đổi.
- **Sổ tay bàn giao Bài học 14 được di chuyển sang API ổn định.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) hiện sử dụng `agent_framework.orchestrations.HandoffBuilder` với `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, phát trực tiếp dựa trên `event.type`, và `FoundryChatClient` (thay thế các ký hiệu bị loại bỏ trước 1.0 như `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Sổ tay phản hồi người trong vòng lặp Bài học 14 được di chuyển sang API ổn định.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) giờ dừng qua `ctx.request_info(...)` + `@response_handler` (thay thế `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` bị loại bỏ), xây dựng bằng `WorkflowBuilder(start_executor=..., output_executors=[...])`, điều khiển đầu ra có cấu trúc qua `default_options={"response_format": ...}`, và sử dụng một câu trả lời kịch bản để sổ tay chạy tự động (không chặn `input()`).
- **Cấu hình môi trường** ([.env.example](../../.env.example)): đổi tên triển khai mô hình sang `gpt-5-mini`; thêm `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (định tuyến Bài học 16) và `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` vốn thiếu trước đây (sử dụng trình duyệt Bài học 15).
- **Phụ thuộc** ([requirements.txt](../../requirements.txt)): cố định `agent-framework`, `agent-framework-foundry`, và `agent-framework-openai` ở phiên bản `~=1.10.0` để có tập hợp nhất quán, xác thực (1.11.0 phát hành thay đổi phá vỡ thử nghiệm trên các giao diện những bài học này sử dụng).

### Ghi chú và giới hạn đã biết

- **Đã xác thực với Microsoft Foundry đang hoạt động.** Các sổ tay Python đã chạy không giao diện với `nbconvert` trên một dự án Microsoft Foundry dùng `gpt-5-mini` (và `gpt-5-nano` cho định tuyến Bài học 16). Hãy triển khai các mô hình tương đương không bị loại bỏ trong dự án của bạn; các sổ tay đọc tên triển khai từ `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Vẫn cần tài nguyên bổ sung cho một số bài học.** Bài 05 cần Azure AI Search; workflow nền Bing của Bài 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) cần kết nối Bing và công cụ lưu trữ Microsoft Foundry Agent Service; Bài 13 (Cognee) và Bài 17 (Foundry Local) cần môi trường runtime riêng.

## [Phát hành] — 2026-07-13

Phiên bản này thêm hai bài học mới hoàn chỉnh vòng triển khai — mở rộng agent tới Microsoft Foundry và thu nhỏ xuống chỉ một máy trạm — cùng một pipeline kiểm tra nhanh, dẫn hướng khóa học được làm mới, kỹ năng học viên mới, và thương hiệu cập nhật.

### Đã thêm

- **Bài học 16 — Triển khai các Agent có khả năng mở rộng với Microsoft Foundry.** Bài học mới [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) và sổ tay có thể chạy [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) xây dựng một agent hỗ trợ khách hàng sản xuất (công cụ, RAG, bộ nhớ, định tuyến mô hình, lưu cache phản hồi, phê duyệt con người, cổng đánh giá, và theo dõi OpenTelemetry), với các sơ đồ Mermaid phát triển/triển khai/runtime, kiểm tra kiến thức, bài tập, và thử thách.
- **Bài học 17 — Tạo Agent AI cục bộ với Foundry Local và Qwen.** Bài học mới [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) và sổ tay [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) xây dựng một trợ lý kỹ thuật hoàn toàn trên thiết bị (gọi hàm Qwen qua Foundry Local, công cụ tập tin sandbox, RAG cục bộ với Chroma, MCP cục bộ tùy chọn), kèm các sơ đồ chỉ cục bộ / cục bộ-RAG / gọi công cụ, kiểm tra kiến thức, bài tập, và thử thách.
- **Pipeline kiểm tra nhanh.** Workflow mới [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) cùng các danh mục theo bài học trong [tests/](./tests/README.md) cho các agent có thể triển khai trong Bài 01, 04, 05, và 16, với README chỉ mục ánh xạ từng danh mục tới bài học và tên agent được lưu trữ. Bài 16 có thêm phần "Xác thực Agent Triển khai với Kiểm tra nhanh"; Bài 01/04/05 thêm một chỉ dẫn kiểm tra nhanh tùy chọn.
- **Kỹ năng học viên.** Kỹ năng Agent mới dưới `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (bao gồm hướng dẫn Bài 16 và 17), và [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cách xác thực các mẫu sổ tay so với Microsoft Foundry / Azure OpenAI đang chạy).
- **Trình chạy xác thực sổ tay.** Tập lệnh mới [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) thực thi từng sổ tay Python không giao diện với `nbconvert` và in ma trận ĐẬU/THẤT BẠI (kèm `results.json`). Tự động xác định thư mục gốc repo và Python, loại trừ mặc định sổ tay không thuộc khóa học (`.venv`, `site-packages`, `translations`, tài sản mẫu kỹ năng) và sổ tay `.NET`, hỗ trợ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, và `-Python`.
- **Dẫn hướng khóa học.** Thêm liên kết Bài học Trước/Sau cho các Bài 11–15 (trước đó thiếu) để toàn khóa giáo trình nối chuỗi 00 → 18 trong cả hai hướng.
- **Hình thu nhỏ mới.** Hình thu nhỏ bài học cho Bài 16 và 17, cùng hình ảnh mạng xã hội repo cập nhật [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (quảng bá hai bài học mới và URL `aka.ms/ai-agents-beginners`).
- **Phụ thuộc** ([requirements.txt](../../requirements.txt)): thêm `foundry-local-sdk` và `chromadb` cho Bài 17.

### Đã thay đổi

- **Bảng bài học chính [README.md](./README.md):** Bài 16 và 17 giờ liên kết tới nội dung (trước là "Sắp ra mắt"); hình ảnh repo nâng cấp thành `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** thêm Bài 16 và 17 vào hướng dẫn từng bài và lộ trình học, và phần "Xác thực Agent Triển khai với Kiểm tra nhanh".
- **[AGENTS.md](./AGENTS.md):** cập nhật số lượng/mô tả bài học (00–18), thêm phần xác thực kiểm tra nhanh, và thêm ví dụ đặt tên mẫu Bài 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "Bài Học Trước" giờ trỏ tới Bài 17 (trước là Bài 15), hoàn thiện chuỗi.
- **Chuẩn hóa tham chiếu mô hình trên các mô hình không bị loại bỏ.** Thay thế tất cả các tham chiếu `gpt-4o` / `gpt-4o-mini` trên toàn bộ khóa học (tài liệu, `.env.example`, sổ tay Python/.NET và ví dụ) bằng `gpt-4.1-mini` — `gpt-4o` (tất cả phiên bản) sẽ nghỉ hưu năm 2026. Ví dụ định tuyến mô hình Bài 16 vẫn giữ sự đối lập nhỏ/lớn bằng `gpt-4.1-mini` (nhỏ) và `gpt-4.1` (lớn). Các sổ tay Python bây giờ chọn mô hình từ biến môi trường (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) thay vì mã hóa cứng tên mô hình.

### Ghi chú và giới hạn đã biết

- **Chưa thực thi trên Azure thực tế.** Các sổ tay bài học mới là ví dụ giáo dục; hãy chạy và xác thực chúng trên môi trường Microsoft Foundry / Foundry Local của bạn. Workflow kiểm tra nhanh yêu cầu bạn triển khai agent của bài học và cấu hình bí mật Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) với vai trò **Azure AI User** ở phạm vi dự án Foundry.
- **Bài 17 chỉ dùng cục bộ.** Không có endpoint Foundry Responses, do đó hành động kiểm tra nhanh không áp dụng; xác thực bằng cách chạy sổ tay trên máy trạm của bạn.

## [Phát hành] — 2026-07-06

Phiên bản này di chuyển khóa học sang **Azure OpenAI Responses API**, chuẩn hóa tên sản phẩm trên **Microsoft Foundry** và **Microsoft Agent Framework (MAF)**, nghỉ hưu GitHub Models, cập nhật phiên bản SDK, và bổ sung nội dung mới về mô hình cục bộ và lưu trữ các framework khác trên Foundry.

### Đã thêm

- **Kỹ năng di chuyển** — Cài đặt Kỹ năng Agent [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (từ [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) dưới `.agents/skills/`, gồm các tham chiếu và tập lệnh quét.
- **Foundry Local (chạy mô hình trên thiết bị)** — Mục mới "Nhà cung cấp thay thế: Foundry Local" trong [00-course-setup/README.md](./00-course-setup/README.md) trình bày cài đặt (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, và kết nối `FoundryLocalManager` với Microsoft Agent Framework qua `OpenAIChatClient`.
- **Lưu trữ agent LangChain / LangGraph trên Microsoft Foundry** — Mục mới trong [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) và ví dụ chạy từng bước [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) dùng `langchain-azure-ai[hosting]` và `ResponsesHostServer` (giao thức `/responses`), dựa trên [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Dự án Microsoft Opal** — Mục mới "Ví dụ Thực tế: Dự án Microsoft Opal" trong [15-browser-use/README.md](./15-browser-use/README.md) trình bày Opal như một agent sử dụng máy tính doanh nghiệp và kết nối nó với các khái niệm khóa học (người trong vòng lặp, tin cậy/bảo mật, lập kế hoạch, Kỹ năng).
- **Mẫu Python thứ hai của Bài 02** — Thêm [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (xem "Đã thay đổi" — di chuyển từ sổ tay Semantic Kernel trước đây) và liên kết trong README bài học.
- Mục **Mô hình và Nhà cung cấp** thêm vào [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Đã thay đổi

- **Chat Completions → Responses API (Python).** Các mẫu gọi mô hình trực tiếp đã được di chuyển từ Chat Completions sang Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), dùng client `OpenAI` truy cập endpoint Azure OpenAI `/openai/v1/` ổn định (không có `api_version`). Các mẫu bị ảnh hưởng bao gồm:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — toàn bộ hướng dẫn gọi hàm (schema công cụ được chuyển sang định dạng Responses, kết quả công cụ trả về như `function_call_output`, `max_output_tokens`, v.v.).

- **Mô hình GitHub → Azure OpenAI.** Mô hình GitHub đã bị ngừng sử dụng (sẽ ngừng hoạt động **tháng 7 năm 2026**) và không hỗ trợ Responses API. Tất cả các đường dẫn mã Mô hình GitHub đã được chuyển sang Azure OpenAI / Microsoft Foundry trong các ví dụ Python và .NET:
  - Python: sổ tay quy trình làm việc Bài học 08 (`01`–`03`), Bài học 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + tài liệu `.md` đi kèm, và các sổ tay quy trình làm việc dotNET Bài học 08/`.md` (`01`–`03`) hiện sử dụng `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` với `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Tệp `02-semantic-kernel.ipynb` trước đây đã được viết lại để sử dụng Microsoft Agent Framework với Azure OpenAI (Responses API) và đổi tên thành `02-python-agent-framework-azure-openai.ipynb`.
- **Chuẩn hóa dùng `FoundryChatClient` + `as_agent`.** README và mã trong sổ tay tham chiếu đến `AzureAIProjectAgentProvider` đã được chuẩn hóa theo mẫu phổ biến do Bài học 01 và các ví dụ của framework sử dụng: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` với `provider.as_agent(...)`. Đã cập nhật trên các README và sổ tay từ Bài học 02–14 (ví dụ: bộ nhớ Bài 13, tất cả sổ tay Bài 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Đặt tên sản phẩm.** Đổi tên trong toàn bộ nội dung tiếng Anh:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Không đổi: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" và tên biến môi trường.)
- **Phụ thuộc** ([requirements.txt](../../requirements.txt)):
  - Khóa phiên bản `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Khóa phiên bản `openai>=1.108.1` (tối thiểu cho Responses API).
  - Loại bỏ `azure-ai-inference` (chỉ được sử dụng trong các ví dụ di cư Mô hình GitHub).
- **Cấu hình môi trường** ([.env.example](../../.env.example)): loại bỏ các biến Mô hình GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); thêm `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` và tùy chọn `AZURE_OPENAI_API_KEY`; cập nhật tên thành Microsoft Foundry.
- **Tài liệu** — Cập nhật [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) và [STUDY_GUIDE.md](./STUDY_GUIDE.md) cho những thay đổi trên (cấu hình biến môi trường, đoạn kiểm tra, hướng dẫn nhà cung cấp, đặt tên).

### Đã loại bỏ

- Các bước onboarding Mô hình GitHub và biến môi trường từ tài liệu thiết lập (được thay thế bởi Azure OpenAI / Microsoft Foundry).

### Bảo mật / Quyền riêng tư (dọn dẹp chia sẻ công khai)

- Đã xóa các kết quả thực thi trong sổ tay Jupyter có rò rỉ **ID đăng ký Azure** thật, tên nhóm tài nguyên / tài nguyên và ID kết nối Bing, cùng các **đường dẫn tệp cục bộ và tên người dùng** của nhà phát triển, ở:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Đã xác minh không còn API key, token, ID đăng ký, hoặc đường dẫn cá nhân nào trong nội dung tiếng Anh được theo dõi (các tham chiếu `GITHUB_TOKEN` còn lại là token GitHub Actions trong workflows và PAT máy chủ GitHub MCP trong thiết lập Bài 11 — đều hợp lệ và không liên quan đến Mô hình GitHub).

### Ghi chú và những hạn chế đã biết

- **Chưa chạy / biên dịch.** Đây là các ví dụ giáo dục đã được cập nhật đúng API / tên gọi; chúng chưa được chạy trên tài nguyên Azure thật, và các ví dụ .NET chưa được biên dịch trong môi trường này. Vui lòng kiểm tra với triển khai Microsoft Foundry / Azure OpenAI của bạn.
- **Triển khai mô hình phải hỗ trợ Responses API.** Sử dụng các triển khai như `gpt-4.1-mini`, `gpt-4.1`, hoặc mô hình `gpt-5.x`. Các mô hình cũ hỗ trợ chức năng Responses cơ bản nhưng không có tất cả tính năng.
- **Phiên bản agent-framework.** Các ví dụ hướng đến MAF mới nhất (`>=1.10.0`). Lệnh gọi tạo agent chuẩn là `client.as_agent(...)`; API đã được xác thực với tài liệu công khai của framework và bản cài đặt. Nếu bạn khóa phiên bản khác, hãy kiểm tra tính khả dụng của phương thức (`as_agent` vs `create_agent`).
- **Sổ tay quy trình làm việc Bài 08 số 04** giữ lại `AzureAIAgentClient` (từ `agent-framework-azure-ai`) vì sử dụng công cụ Microsoft Foundry Agent Service (đặt nền Bing, trình thông dịch mã); nó đã dựa trên Responses.
- **Mặc định triển khai .NET.** Hai ví dụ quy trình dotNET Bài 08 trước đây cứng mã một mô hình cụ thể; giờ mặc định dùng `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Nếu ví dụ sử dụng đầu vào đa phương tiện/thị giác, hãy đặt `AZURE_OPENAI_DEPLOYMENT` thành mô hình phù hợp.
- **Foundry Local** cung cấp điểm cuối **Chat Completions** tương thích OpenAI và dành cho phát triển cục bộ; sử dụng Azure OpenAI / Microsoft Foundry để có đầy đủ tính năng Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->