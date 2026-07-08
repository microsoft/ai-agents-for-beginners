# Thiết Lập Khóa Học

## Giới Thiệu

Bài học này sẽ hướng dẫn cách chạy các ví dụ mã trong khóa học này.

## Tham Gia Cùng Học Viên Khác và Nhận Trợ Giúp

Trước khi bắt đầu sao chép repo của bạn, hãy tham gia [kênh Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) để được hỗ trợ thiết lập, giải đáp thắc mắc về khóa học hoặc kết nối với những người học khác.

## Sao Chép hoặc Fork Repo Này

Để bắt đầu, vui lòng sao chép hoặc fork kho lưu trữ GitHub. Việc này sẽ tạo phiên bản riêng của bạn từ tài liệu khóa học để bạn có thể chạy, thử nghiệm và chỉnh sửa mã!

Việc này có thể làm bằng cách nhấn vào liên kết <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Bạn nên có phiên bản fork riêng của khóa học này theo liên kết sau:

![Forked Repo](../../../translated_images/vi/forked-repo.33f27ca1901baa6a.webp)

### Sao Chép Nông (khuyến nghị cho workshop / Codespaces)

  >Toàn bộ kho lưu trữ có thể lớn (~3 GB) khi bạn tải xuống toàn bộ lịch sử và tất cả các tệp. Nếu bạn chỉ tham gia workshop hoặc chỉ cần vài thư mục bài học, sao chép nông (hoặc sao chép thưa thớt) sẽ tránh hầu hết việc tải xuống đó bằng cách cắt bớt lịch sử và/hoặc bỏ qua các blob.

#### Sao chép nông nhanh — lịch sử tối thiểu, tất cả các tệp

Thay `<your-username>` trong các lệnh bên dưới bằng URL fork của bạn (hoặc URL upstream nếu bạn thích).

Để sao chép chỉ lịch sử cam kết mới nhất (tải xuống nhỏ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Để sao chép một nhánh cụ thể:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Sao chép một phần (thưa thớt) — tối thiểu blob + chỉ các thư mục được chọn

Phương pháp này sử dụng sao chép một phần và sparse-checkout (yêu cầu Git 2.25+ và khuyến nghị dùng Git hiện đại hỗ trợ sao chép một phần):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Điều hướng vào thư mục repo:

```bash|powershell
cd ai-agents-for-beginners
```

Sau đó chỉ định những thư mục bạn muốn (ví dụ dưới đây là hai thư mục):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Sau khi sao chép và kiểm tra các tệp, nếu bạn chỉ cần tệp và muốn giải phóng không gian (không giữ lịch sử git), vui lòng xóa dữ liệu metadata của kho lưu trữ (💀không thể hoàn tác — bạn sẽ mất tất cả chức năng Git: không còn commit, pull, push hay truy cập lịch sử).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Sử dụng GitHub Codespaces (khuyến nghị để tránh tải xuống lớn trên máy)

- Tạo một Codespace mới cho repo này qua [Giao diện GitHub](https://github.com/codespaces).  

- Trong terminal của Codespace mới tạo, chạy một trong các lệnh sao chép nông/thưa thớt ở trên để chỉ lấy những thư mục bài học bạn cần vào workspace Codespace.
- Tùy chọn: sau khi sao chép trong Codespaces, xóa .git để lấy lại không gian lưu trữ (xem lệnh xóa ở trên).
- Lưu ý: Nếu bạn muốn mở repo trực tiếp trong Codespaces (không cần sao chép thêm), hãy biết rằng Codespaces sẽ xây dựng môi trường devcontainer và có thể vẫn cung cấp nhiều hơn bạn cần. Sao chép một bản nông bên trong Codespace mới giúp bạn kiểm soát tốt hơn việc dùng đĩa.

#### Mẹo

- Luôn thay thế URL sao chép bằng fork của bạn nếu muốn chỉnh sửa/cam kết.
- Nếu sau này cần thêm lịch sử hoặc tệp, bạn có thể lấy chúng hoặc điều chỉnh sparse-checkout để bao gồm thêm thư mục.

## Chạy Mã

Khóa học này cung cấp một chuỗi Jupyter Notebooks mà bạn có thể chạy để có trải nghiệm thực hành xây dựng AI Agents.

Các ví dụ mã sử dụng **Microsoft Agent Framework (MAF)** với `FoundryChatClient`, kết nối với **Microsoft Foundry Agent Service V2** (API Phản hồi) thông qua **Microsoft Foundry**.

Tất cả các notebook Python có nhãn `*-python-agent-framework.ipynb`.

## Yêu Cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài đặt Python3.12, hãy chắc chắn cài đặt nó. Sau đó tạo môi trường ảo venv với python3.12 để đảm bảo phiên bản đúng được cài từ file requirements.txt.
  
    >Ví dụ

    Tạo thư mục venv Python:

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

- .NET 10+: Với ví dụ dùng .NET, hãy đảm bảo cài [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc phiên bản mới hơn. Sau đó kiểm tra phiên bản .NET SDK đã cài:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Cần thiết cho xác thực. Cài đặt tại [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Để truy cập Microsoft Foundry và Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Một dự án với mô hình đã triển khai (ví dụ: `gpt-4o`). Xem [Bước 1](#bước-1-tạo-dự-án-microsoft-foundry) bên dưới.

Chúng tôi đã bao gồm file `requirements.txt` trong thư mục gốc của repo này chứa tất cả các gói Python cần thiết để chạy ví dụ mã.

Bạn có thể cài đặt chúng bằng lệnh sau trong terminal tại thư mục gốc repo:

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyên bạn nên tạo môi trường ảo Python để tránh xung đột và lỗi.

## Thiết Lập VSCode

Hãy đảm bảo bạn đang sử dụng đúng phiên bản Python trong VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Thiết Lập Microsoft Foundry và Microsoft Foundry Agent Service

### Bước 1: Tạo Dự Án Microsoft Foundry

Bạn cần một **hub** và **dự án** Microsoft Foundry với mô hình đã triển khai để chạy notebook.

1. Truy cập [ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.
2. Tạo một **hub** (hoặc dùng hub hiện có). Xem: [Tổng quan tài nguyên Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Trong hub, tạo một **dự án**.
4. Triển khai mô hình (ví dụ: `gpt-4o`) từ **Models + Endpoints** → **Deploy model**.

### Bước 2: Lấy URL Endpoint và Tên Triển Khai Mô Hình Dự Án

Trong dự án của bạn trên cổng Microsoft Foundry:

- **Project Endpoint** — Vào trang **Overview** và sao chép URL endpoint.

![Project Connection String](../../../translated_images/vi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vào **Models + Endpoints**, chọn mô hình đã triển khai, ghi lại **Deployment name** (ví dụ: `gpt-4o`).

### Bước 3: Đăng nhập Azure với `az login`

Tất cả notebook sử dụng **`AzureCliCredential`** để xác thực — không phải quản lý khóa API. Điều này yêu cầu bạn đăng nhập qua Azure CLI.

1. **Cài đặt Azure CLI** nếu bạn chưa cài: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Đăng nhập** bằng cách chạy:

    ```bash|powershell
    az login
    ```

    Hoặc nếu bạn ở môi trường từ xa/Codespace không có trình duyệt:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chọn subscription** nếu được yêu cầu — chọn subscription chứa dự án Foundry của bạn.

4. **Xác minh** bạn đã đăng nhập:

    ```bash|powershell
    az account show
    ```

> **Tại sao `az login`?** Các notebook xác thực bằng `AzureCliCredential` từ gói `azure-identity`. Điều này nghĩa là phiên đăng nhập Azure CLI của bạn cung cấp thông tin xác thực — không cần khóa API hoặc bí mật trong file `.env`. Đây là [thực hành bảo mật tốt nhất](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Bước 4: Tạo File `.env` Của Bạn

Sao chép file mẫu:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Cổng Foundry → dự án của bạn → trang **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Cổng Foundry → **Models + Endpoints** → tên mô hình đã triển khai của bạn |

Đó là tất cả cho phần lớn các bài học! Các notebook sẽ tự xác thực qua phiên `az login` của bạn.

### Bước 5: Cài Đặt Phụ Thuộc Python

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyên bạn nên chạy lệnh này trong môi trường ảo đã tạo trước đó.

## Thiết Lập Thêm Cho Bài 5 (Agentic RAG)

Bài 5 sử dụng **Azure AI Search** để tạo kết quả tăng cường truy xuất. Nếu bạn định chạy bài này, thêm các biến sau vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Cổng Azure → tài nguyên **Azure AI Search** của bạn → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Cổng Azure → tài nguyên **Azure AI Search** của bạn → **Settings** → **Keys** → khóa quản trị viên chính |

## Thiết Lập Thêm Cho Các Bài Gọi Azure OpenAI Trực Tiếp (Bài 6 và 8)

Một số notebook trong bài 6 và 8 gọi **Azure OpenAI** trực tiếp (sử dụng **Responses API**) thay vì qua dự án Microsoft Foundry. Các ví dụ này trước đây dùng GitHub Models, giờ đã lỗi thời (ngừng hoạt động tháng 7 năm 2026) và không hỗ trợ Responses API. Nếu bạn định chạy các ví dụ đó, thêm các biến sau vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Cổng Azure → tài nguyên **Azure OpenAI** của bạn → **Keys and Endpoint** → Endpoint (ví dụ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Tên mô hình đã triển khai của bạn (ví dụ `gpt-4o-mini`) hỗ trợ Responses API |
| `AZURE_OPENAI_API_KEY` | Tùy chọn — chỉ nếu bạn dùng xác thực bằng khóa thay vì `az login` / Entra ID |

> Responses API dùng endpoint ổn định `/openai/v1/`, nên không cần `api-version`. Đăng nhập bằng `az login` để sử dụng xác thực Entra ID không khóa.

## Nhà Cung Cấp Thay Thế: MiniMax (Tương Thích OpenAI)

[MiniMax](https://platform.minimaxi.com/) cung cấp mô hình ngữ cảnh lớn (lên đến 204K tokens) thông qua API tương thích OpenAI. Vì Microsoft Agent Framework's `OpenAIChatClient` hoạt động với bất kỳ endpoint nào tương thích OpenAI, bạn có thể dùng MiniMax như một lựa chọn thay thế cho Azure OpenAI hoặc OpenAI.

Thêm các biến sau vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Dùng `https://api.minimax.io/v1` (giá trị mặc định) |
| `MINIMAX_MODEL_ID` | Tên mô hình dùng (ví dụ `MiniMax-M3`) |

**Các mô hình mẫu**: `MiniMax-M3` (khuyến nghị), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (phản hồi nhanh hơn). Tên và khả dụng mô hình có thể thay đổi theo thời gian, và quyền truy cập mô hình tùy thuộc tài khoản hoặc khu vực — kiểm tra [MiniMax Platform](https://platform.minimaxi.com/) để biết danh sách hiện tại. Nếu `MiniMax-M3` không có với tài khoản bạn, hãy đặt `MINIMAX_MODEL_ID` vào mô hình bạn có quyền truy cập (ví dụ `MiniMax-M2.7`).

Các ví dụ mã dùng `OpenAIChatClient` (ví dụ, bài 14 quy trình đặt phòng khách sạn) sẽ tự động phát hiện và dùng cấu hình MiniMax của bạn khi `MINIMAX_API_KEY` được thiết lập.

## Nhà Cung Cấp Thay Thế: Foundry Local (Chạy Mô Hình Trên Máy)

[Foundry Local](https://foundrylocal.ai) là runtime nhẹ tải xuống, quản lý và phục vụ mô hình ngôn ngữ **hoàn toàn trên máy của bạn** thông qua API tương thích OpenAI — không cần đám mây, không cần subscription Azure, và không cần khóa API. Đây là lựa chọn tuyệt vời cho phát triển offline, thử nghiệm không mất phí đám mây, hoặc giữ dữ liệu trên thiết bị.

Vì Microsoft Agent Framework's `OpenAIChatClient` hoạt động với bất kỳ endpoint nào tương thích OpenAI, Foundry Local là lựa chọn thay thế cục bộ thay cho Azure OpenAI.

**1. Cài đặt Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Tải xuống và chạy mô hình** (điều này cũng khởi động dịch vụ cục bộ):

```bash
foundry model list          # xem các mô hình có sẵn
foundry model run phi-4-mini
```

**3. Cài đặt SDK Python** dùng để phát hiện endpoint cục bộ:

```bash
pip install foundry-local-sdk
```

**4. Trỏ Microsoft Agent Framework đến mô hình cục bộ của bạn:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Tải xuống (nếu cần) và phục vụ mô hình tại chỗ, sau đó tìm điểm cuối/cổng.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ví dụ http://localhost:<port>/v1
    api_key=manager.api_key,        # luôn là "không cần thiết" cho Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Lưu ý:** Foundry Local cung cấp endpoint **Chat Completions** tương thích OpenAI. Dùng cho phát triển cục bộ và các kịch bản offline. Để sử dụng đầy đủ tính năng **Responses API** (hội thoại trạng thái, điều phối công cụ sâu, và phát triển kiểu agent), hãy dùng **Azure OpenAI** hoặc dự án **Microsoft Foundry** như trong bài học. Xem tài liệu [Foundry Local](https://foundrylocal.ai) để biết danh mục mô hình và hỗ trợ nền tảng hiện tại.

## Thiết Lập Thêm Cho Bài 8 (Quy Trình Bing Grounding)


Sổ tay luồng công việc có điều kiện trong bài học 8 sử dụng **Bing grounding** thông qua Microsoft Foundry. Nếu bạn dự định chạy mẫu đó, hãy thêm biến này vào tệp `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `BING_CONNECTION_ID` | Cổng Microsoft Foundry → dự án của bạn → **Management** → **Connected resources** → kết nối Bing của bạn → sao chép ID kết nối |

## Khắc phục sự cố

### Lỗi xác minh chứng chỉ SSL trên macOS

Nếu bạn dùng macOS và gặp lỗi như sau:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Đây là một vấn đề đã biết với Python trên macOS, nơi các chứng chỉ SSL hệ thống không tự động được tin cậy. Hãy thử các giải pháp sau theo thứ tự:

**Lựa chọn 1: Chạy tập lệnh Install Certificates của Python (khuyến nghị)**

```bash
# Thay thế 3.XX bằng phiên bản Python bạn đã cài đặt (ví dụ: 3.12 hoặc 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Lựa chọn 2: Sử dụng `connection_verify=False` trong sổ tay của bạn (chỉ dành cho sổ tay GitHub Models)**

Trong sổ tay Bài học 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), đã có sẵn giải pháp tạm thời được chú thích. Bỏ chú thích `connection_verify=False` khi tạo client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vô hiệu hóa xác minh SSL nếu bạn gặp lỗi chứng chỉ
)
```

> **⚠️ Cảnh báo:** Tắt xác minh SSL (`connection_verify=False`) làm giảm độ bảo mật bằng cách bỏ qua việc xác thực chứng chỉ. Chỉ sử dụng cách này như một giải pháp tạm thời trong môi trường phát triển, không bao giờ dùng trong môi trường sản xuất.

**Lựa chọn 3: Cài đặt và sử dụng `truststore`**

```bash
pip install truststore
```

Sau đó thêm đoạn sau lên đầu sổ tay hoặc script của bạn trước khi thực hiện bất kỳ cuộc gọi mạng nào:

```python
import truststore
truststore.inject_into_ssl()
```

## Bị kẹt ở đâu đó?

Nếu bạn gặp bất kỳ vấn đề nào khi chạy thiết lập này, hãy tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> hoặc <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tạo báo cáo lỗi</a>.

## Bài học tiếp theo

Bạn đã sẵn sàng chạy mã cho khóa học này. Chúc bạn học vui và khám phá thêm về thế giới các Agent AI!

[Giới thiệu về AI Agents và các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->