# Thiết lập Khóa học

## Giới thiệu

Bài học này sẽ hướng dẫn cách chạy các ví dụ mã trong khóa học này.

## Tham gia cùng các học viên khác và nhận trợ giúp

Trước khi bạn bắt đầu sao chép repo của mình, hãy tham gia kênh [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) để nhận trợ giúp về thiết lập, hỏi đáp về khóa học hoặc kết nối với những người học khác.

## Sao chép hoặc Fork repo này

Để bắt đầu, vui lòng sao chép hoặc fork Kho lưu trữ GitHub. Điều này sẽ tạo phiên bản riêng của bạn về tài liệu khóa học để bạn có thể chạy, kiểm tra và chỉnh sửa mã!

Việc này có thể thực hiện bằng cách nhấp vào liên kết <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Bây giờ bạn sẽ có phiên bản fork riêng của khóa học này theo liên kết sau:

![Forked Repo](../../../translated_images/vi/forked-repo.33f27ca1901baa6a.webp)

### Sao chép nông (được khuyến nghị cho hội thảo / Codespaces)

  >Kho lưu trữ đầy đủ có thể lớn (~3 GB) khi bạn tải về toàn bộ lịch sử và tất cả các tập tin. Nếu bạn chỉ tham dự hội thảo hoặc chỉ cần một vài thư mục bài học, sao chép nông (hoặc sao chép thưa thớt) sẽ tránh hầu hết việc tải xuống đó bằng cách cắt bớt lịch sử và/hoặc bỏ qua các blob.

#### Sao chép nông nhanh — lịch sử tối thiểu, tất cả các tập tin

Thay `<your-username>` trong các lệnh dưới đây bằng URL fork của bạn (hoặc URL upstream nếu bạn thích).

Để sao chép chỉ lịch sử commit mới nhất (tải xuống nhỏ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Để sao chép một nhánh cụ thể:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Sao chép một phần (thưa thớt) — blobs tối thiểu + chỉ các thư mục được chọn

Đây sử dụng sao chép một phần và sparse-checkout (yêu cầu Git 2.25+ và khuyến nghị Git hiện đại hỗ trợ sao chép một phần):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Di chuyển vào thư mục repo:

```bash|powershell
cd ai-agents-for-beginners
```

Sau đó xác định các thư mục bạn muốn (ví dụ dưới đây hiển thị hai thư mục):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Sau khi sao chép và kiểm tra các tập tin, nếu bạn chỉ cần các tập tin và muốn giải phóng không gian (không có lịch sử git), vui lòng xóa metadata của repo (💀 không thể hoàn tác — bạn sẽ mất tất cả chức năng Git: không thể commit, pull, push hoặc truy cập lịch sử).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Sử dụng GitHub Codespaces (khuyến nghị để tránh tải xuống lớn cục bộ)

- Tạo một Codespace mới cho repo này qua [Giao diện GitHub](https://github.com/codespaces).  

- Trong terminal của codespace mới tạo, chạy một trong các lệnh sao chép nông/thưa thớt phía trên để chỉ đưa các thư mục bài học bạn cần vào workspace Codespace.
- Tùy chọn: sau khi sao chép bên trong Codespaces, xóa .git để lấy lại không gian (xem các lệnh xóa phía trên).
- Lưu ý: Nếu bạn thích mở repo trực tiếp trong Codespaces (không sao chép thêm), hãy lưu ý Codespaces sẽ xây dựng môi trường devcontainer và có thể vẫn cấp phát nhiều hơn bạn cần. Sao chép một bản nông trong Codespace mới sẽ giúp bạn kiểm soát tốt hơn việc sử dụng đĩa.

#### Mẹo

- Luôn thay URL sao chép bằng fork của bạn nếu bạn muốn chỉnh sửa/commit.
- Nếu sau này bạn cần thêm lịch sử hoặc tập tin, bạn có thể lấy chúng hoặc điều chỉnh sparse-checkout để bao gồm thêm các thư mục.

## Chạy Mã

Khóa học này cung cấp chuỗi Jupyter Notebooks mà bạn có thể chạy để có trải nghiệm thực hành xây dựng AI Agents.

Các ví dụ mã sử dụng **Microsoft Agent Framework (MAF)** với `FoundryChatClient`, kết nối với **Microsoft Foundry Agent Service V2** (API Responses) qua **Microsoft Foundry**.

Tất cả các notebook Python đều được đánh dấu `*-python-agent-framework.ipynb`.

## Yêu cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài Python3.12, hãy đảm bảo cài đặt nó. Sau đó tạo venv bằng python3.12 để chắc chắn các phiên bản đúng được cài từ file requirements.txt.
  
    >Ví dụ

    Tạo thư mục Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Sau đó kích hoạt môi trường venv cho:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Đối với ví dụ mã dùng .NET, hãy đảm bảo bạn cài đặt [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc mới hơn. Sau đó kiểm tra phiên bản SDK .NET đã cài đặt:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Cần thiết cho xác thực. Cài đặt tại [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Để truy cập Microsoft Foundry và Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Một dự án có mô hình đã triển khai (ví dụ: `gpt-5-mini`). Xem [Bước 1](#bước-1-tạo-dự-án-microsoft-foundry) bên dưới.

Chúng tôi đã bao gồm file `requirements.txt` trong gốc repo chứa tất cả các gói Python cần thiết để chạy các ví dụ mã.

Bạn có thể cài đặt chúng bằng cách chạy lệnh sau trong terminal tại thư mục gốc repo:

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyên bạn tạo môi trường ảo Python để tránh xung đột và sự cố.

## Thiết lập VSCode

Đảm bảo bạn đang sử dụng đúng phiên bản Python trong VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Thiết lập Microsoft Foundry và Microsoft Foundry Agent Service

### Bước 1: Tạo dự án Microsoft Foundry

Bạn cần một **hub** và **dự án** Microsoft Foundry có mô hình đã triển khai để chạy các notebook.

1. Truy cập [ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.
2. Tạo một **hub** mới (hoặc sử dụng hub hiện có). Xem: [Tổng quan tài nguyên Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Trong hub, tạo một **dự án**.
4. Triển khai một mô hình (ví dụ: `gpt-5-mini`) từ **Models + Endpoints** → **Deploy model**.

### Bước 2: Lấy Endpoint dự án và Tên triển khai mô hình

Từ dự án của bạn trên cổng Microsoft Foundry:

- **Project Endpoint** — Vào trang **Overview** và sao chép URL endpoint.

![Project Connection String](../../../translated_images/vi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vào **Models + Endpoints**, chọn mô hình đã triển khai, và lưu ý **Deployment name** (ví dụ: `gpt-5-mini`).

### Bước 3: Đăng nhập Azure với `az login`

Tất cả notebook sử dụng **`AzureCliCredential`** để xác thực — không cần API key quản lý. Điều này yêu cầu bạn đăng nhập qua Azure CLI.

1. **Cài đặt Azure CLI** nếu bạn chưa cài: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Đăng nhập** bằng cách chạy:

    ```bash|powershell
    az login
    ```

    Hoặc nếu bạn ở môi trường remote/Codespace không có trình duyệt:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chọn subscription** nếu được yêu cầu — chọn subscription chứa dự án Foundry của bạn.

4. **Xác nhận** bạn đã đăng nhập:

    ```bash|powershell
    az account show
    ```

> **Tại sao dùng `az login`?** Các notebook xác thực sử dụng `AzureCliCredential` từ gói `azure-identity`. Điều này có nghĩa phiên đăng nhập Azure CLI cung cấp thông tin xác thực — không có API key hay bí mật trong tệp `.env`. Đây là [thực hành bảo mật tốt nhất](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Bước 4: Tạo file `.env`

Sao chép file ví dụ:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Mở `.env` và điền hai giá trị này:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Cổng Foundry → dự án của bạn → trang **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Cổng Foundry → **Models + Endpoints** → tên mô hình đã triển khai |

Xong phần lớn bài học rồi! Các notebook sẽ xác thực tự động qua phiên `az login` của bạn.

### Bước 5: Cài đặt các phụ thuộc Python

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyên bạn chạy lệnh này trong môi trường ảo Python bạn đã tạo trước đó.

## Thiết lập bổ sung cho Bài học 5 (Agentic RAG)

Bài học 5 sử dụng **Azure AI Search** cho tạo văn bản dựa trên truy vấn (retrieval-augmented generation). Nếu bạn dự định chạy bài học đó, thêm các biến này vào file `.env`:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Cổng Azure → tài nguyên **Azure AI Search** của bạn → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Cổng Azure → tài nguyên **Azure AI Search** của bạn → **Settings** → **Keys** → khóa admin chính |

## Thiết lập bổ sung cho các Bài học gọi Azure OpenAI trực tiếp (Bài 6 và 8)

Một vài notebook trong bài 6 và 8 gọi **Azure OpenAI** trực tiếp (dùng **API Responses**) thay vì thông qua dự án Microsoft Foundry. Các ví dụ này trước đây dùng GitHub Models, vốn đã ngưng (dừng vào tháng 7/2026) và không hỗ trợ API Responses. Nếu bạn dự định chạy các ví dụ đó, thêm các biến này vào file `.env`:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Cổng Azure → tài nguyên **Azure OpenAI** của bạn → **Keys and Endpoint** → Endpoint (ví dụ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Tên mô hình bạn đã triển khai (ví dụ `gpt-5-mini`) hỗ trợ API Responses |
| `AZURE_OPENAI_API_KEY` | Tùy chọn — chỉ nếu bạn dùng xác thực bằng key thay vì `az login` / Entra ID |

> API Responses dùng endpoint ổn định `/openai/v1/`, nên không cần `api-version`. Đăng nhập bằng `az login` để dùng xác thực Entra ID không cần key.

## Nhà cung cấp thay thế: MiniMax (tương thích OpenAI)

[MiniMax](https://platform.minimaxi.com/) cung cấp các mô hình ngữ cảnh lớn (tới 204K token) qua API tương thích OpenAI. Vì Microsoft Agent Framework’s `OpenAIChatClient` làm việc với mọi endpoint tương thích OpenAI, bạn có thể dùng MiniMax như một lựa chọn thay thế thay cho Azure OpenAI hoặc OpenAI.

Thêm các biến này vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Dùng `https://api.minimax.io/v1` (giá trị mặc định) |
| `MINIMAX_MODEL_ID` | Tên mô hình dùng (ví dụ `MiniMax-M3`) |

**Ví dụ các mô hình**: `MiniMax-M3` (khuyến nghị), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (phản hồi nhanh hơn). Tên mô hình và sẵn có có thể thay đổi theo thời gian, và quyền truy cập một mô hình nhất định có thể phụ thuộc vào tài khoản hoặc vùng của bạn — xem [MiniMax Platform](https://platform.minimaxi.com/) để biết danh sách hiện tại. Nếu `MiniMax-M3` không khả dụng với tài khoản bạn, đặt `MINIMAX_MODEL_ID` thành mô hình bạn có quyền truy cập (ví dụ `MiniMax-M2.7`).

Các ví dụ mã dùng `OpenAIChatClient` (ví dụ bài 14 workflow đặt phòng khách sạn) sẽ tự động phát hiện và dùng cấu hình MiniMax của bạn khi `MINIMAX_API_KEY` được thiết lập.

## Nhà cung cấp thay thế: Foundry Local (Chạy mô hình trên thiết bị)

[Foundry Local](https://foundrylocal.ai) là một runtime nhẹ tải về, quản lý và phục vụ các mô hình ngôn ngữ **hoàn toàn trên máy của bạn** qua API tương thích OpenAI — không dùng cloud, không đăng ký Azure, không API key. Đây là lựa chọn tuyệt vời cho phát triển offline, thử nghiệm mà không phát sinh chi phí cloud, hoặc giữ dữ liệu ngay trên thiết bị.

Vì Microsoft Agent Framework’s `OpenAIChatClient` hoạt động với mọi endpoint tương thích OpenAI, Foundry Local là lựa chọn thay thế local thay thế Azure OpenAI.

**1. Cài đặt Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Tải về và chạy một mô hình** (điều này cũng khởi động dịch vụ local):

```bash
foundry model list          # xem các mô hình có sẵn
foundry model run phi-4-mini
```

**3. Cài đặt Python SDK** dùng để phát hiện endpoint local:

```bash
pip install foundry-local-sdk
```

**4. Trỏ Microsoft Agent Framework về mô hình local của bạn:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Tải xuống (nếu cần) và phục vụ mô hình cục bộ, sau đó phát hiện điểm cuối/cổng.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ví dụ http://localhost:<port>/v1
    api_key=manager.api_key,        # luôn luôn là "không yêu cầu" đối với Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Lưu ý:** Foundry Local cung cấp endpoint **Chat Completions** tương thích OpenAI. Dùng nó cho phát triển local và trường hợp offline. Để dùng đầy đủ tính năng **Responses API** (đàm thoại giữ trạng thái, điều phối công cụ sâu rộng, và phát triển kiểu agent), hãy dùng **Azure OpenAI** hoặc dự án **Microsoft Foundry** như trong các bài học. Xem tài liệu [Foundry Local](https://foundrylocal.ai) để biết catalog mô hình và hỗ trợ nền tảng hiện tại.

## Thiết lập bổ sung cho Bài học 8 (Workflow đệm Bing)


Sổ tay quy trình làm việc có điều kiện trong bài học 8 sử dụng **Bing grounding** qua Microsoft Foundry. Nếu bạn định chạy ví dụ đó, hãy thêm biến này vào tệp `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `BING_CONNECTION_ID` | Cổng Microsoft Foundry → dự án của bạn → **Management** → **Connected resources** → kết nối Bing của bạn → sao chép ID kết nối |

## Xử lý sự cố

### Lỗi Xác thực Chứng chỉ SSL trên macOS

Nếu bạn đang dùng macOS và gặp lỗi như:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Đây là vấn đề đã biết với Python trên macOS khi các chứng chỉ SSL của hệ thống không được tin tưởng tự động. Hãy thử các giải pháp sau theo thứ tự:

**Lựa chọn 1: Chạy script Install Certificates của Python (khuyến nghị)**

```bash
# Thay thế 3.XX bằng phiên bản Python bạn đã cài đặt (ví dụ: 3.12 hoặc 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Lựa chọn 2: Dùng `connection_verify=False` trong sổ tay của bạn (chỉ dành cho các sổ tay Models trên GitHub)**

Trong sổ tay Bài học 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), một cách giải quyết được chú thích đã có sẵn. Bỏ chú thích `connection_verify=False` khi tạo client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vô hiệu hóa kiểm tra SSL nếu bạn gặp lỗi chứng chỉ
)
```

> **⚠️ Cảnh báo:** Vô hiệu hóa xác thực SSL (`connection_verify=False`) làm giảm bảo mật bằng cách bỏ qua kiểm tra chứng chỉ. Chỉ sử dụng tạm thời trong môi trường phát triển, không bao giờ dùng trong môi trường sản xuất.

**Lựa chọn 3: Cài đặt và sử dụng `truststore`**

```bash
pip install truststore
```

Sau đó thêm đoạn sau lên đầu sổ tay hoặc script của bạn trước khi thực hiện bất kỳ cuộc gọi mạng nào:

```python
import truststore
truststore.inject_into_ssl()
```

## Gặp khó khăn ở đâu đó?

Nếu bạn gặp bất kỳ vấn đề nào khi chạy thiết lập này, hãy tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> hoặc <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tạo một vấn đề</a>.

## Bài học tiếp theo

Bây giờ bạn đã sẵn sàng chạy code cho khóa học này. Chúc bạn học vui về thế giới của AI Agents! 

[Giới thiệu về AI Agents và các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->