# Thiết lập Khóa học

## Giới thiệu

Bài học này sẽ trình bày cách chạy các mẫu mã nguồn trong khóa học này.

## Tham gia Cộng đồng Người học và Nhận Hỗ trợ

Trước khi bắt đầu sao chép repo của bạn, hãy tham gia [kênh Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) để nhận được hỗ trợ về quá trình thiết lập, giải đáp thắc mắc về khóa học, hoặc kết nối với các người học khác.

## Sao chép hoặc Tạo Fork repo này

Để bắt đầu, vui lòng sao chép hoặc tạo fork Kho Lưu trữ GitHub. Điều này sẽ tạo ra phiên bản của riêng bạn của tài liệu khóa học để bạn có thể chạy, kiểm tra và chỉnh sửa mã nguồn!

Việc này có thể thực hiện bằng cách nhấp vào đường link <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">tạo fork repo</a>

Bạn sẽ có phiên bản fork riêng của khóa học này tại đường link sau:

![Forked Repo](../../../translated_images/vi/forked-repo.33f27ca1901baa6a.webp)

### Sao chép Shallow (khuyến nghị cho workshop / Codespaces)

  > Kho lưu trữ đầy đủ có thể rất lớn (~3 GB) khi bạn tải về toàn bộ lịch sử và tất cả các file. Nếu bạn chỉ tham gia workshop hoặc chỉ cần một vài thư mục bài học, sao chép shallow (hoặc sao chép sparse) sẽ tải ít dữ liệu hơn nhiều.

#### Sao chép shallow nhanh — lịch sử tối thiểu, tất cả file

Thay thế `<your-username>` trong các lệnh dưới đây bằng URL fork của bạn (hoặc URL upstream nếu bạn muốn).

Để sao chép chỉ lịch sử commit mới nhất (tải xuống nhỏ):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Để sao chép một nhánh cụ thể:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Sao chép Partial (sparse) — số lượng blob tối thiểu + chỉ những thư mục được chọn

Cách này sử dụng partial clone và sparse-checkout (yêu cầu Git 2.25+ và khuyến nghị Git hiện đại hỗ trợ partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Chuyển vào thư mục repo:

```bash
cd ai-agents-for-beginners
```

Sau đó chỉ định những thư mục bạn muốn (ví dụ dưới đây có hai thư mục):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Sau khi sao chép và xác nhận các file, nếu bạn chỉ cần các file và muốn giải phóng dung lượng (không cần lịch sử git), hãy xóa metadata repo đi (💀không thể phục hồi — bạn sẽ mất tất cả chức năng Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Sử dụng GitHub Codespaces (khuyến nghị để tránh tải xuống lớn trên máy cục bộ)

- Tạo một Codespace mới cho repo này qua [Giao diện GitHub](https://github.com/codespaces).  

- Trong terminal của codespace mới tạo, chạy một trong các lệnh shallow/sparse clone ở trên để chỉ đưa những thư mục bài học cần thiết vào workspace Codespace.
- Tùy chọn: sau khi sao chép trong Codespaces, xóa .git để thu hồi thêm dung lượng (xem các lệnh xóa ở trên).
- Lưu ý: Nếu bạn muốn mở trực tiếp repo trong Codespaces (không sao chép thêm), Codespaces sẽ xây dựng môi trường devcontainer và có thể vẫn cung cấp nhiều hơn bạn cần.

#### Mẹo

- Luôn thay URL sao chép thành phiên bản fork của bạn nếu bạn muốn chỉnh sửa/commit.
- Nếu sau này bạn cần thêm lịch sử hoặc file, bạn có thể fetch chúng hoặc điều chỉnh sparse-checkout để bao gồm thêm thư mục.

## Chạy Mã Nguồn

Khóa học cung cấp một loạt các Jupyter Notebooks mà bạn có thể chạy để thực hành xây dựng AI Agents.

Các mẫu mã nguồn sử dụng **Microsoft Agent Framework (MAF)** với `FoundryChatClient`, kết nối tới **Microsoft Foundry Agent Service V2** (API Responses) thông qua **Microsoft Foundry**.

Tất cả notebooks Python đều được đánh dấu `*-python-agent-framework.ipynb`.

## Yêu cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài Python3.12, hãy chắc chắn cài đặt. Sau đó tạo môi trường venv bằng python3.12 để đảm bảo phiên bản đúng được cài từ file requirements.txt.
  
    >Ví dụ

    Tạo thư mục venv Python:

    ```bash
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

- .NET 10+: Đối với các mẫu mã sử dụng .NET, hãy chắc chắn bạn đã cài [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc mới hơn. Sau đó, kiểm tra phiên bản .NET SDK đã cài:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Cần thiết cho xác thực. Cài đặt tại [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Để truy cập Microsoft Foundry và Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Một dự án có mô hình đã triển khai (ví dụ `gpt-5-mini`). Xem [Bước 1](#bước-1-tạo-microsoft-foundry-project) bên dưới.

Chúng tôi đã bao gồm file `requirements.txt` ở thư mục gốc của repo chứa tất cả gói Python cần thiết để chạy các mẫu mã.

Bạn có thể cài đặt chúng bằng cách chạy lệnh sau trong terminal ở thư mục gốc repo:

```bash
pip install -r requirements.txt
```

Chúng tôi khuyên bạn nên tạo môi trường ảo Python để tránh xung đột và các vấn đề.

## Thiết lập VSCode

Đảm bảo bạn đang dùng đúng phiên bản Python trong VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Thiết lập Microsoft Foundry và Microsoft Foundry Agent Service

### Bước 1: Tạo Microsoft Foundry Project

Bạn cần có một **hub** và **project** trong Microsoft Foundry với mô hình đã triển khai để chạy các notebook.

1. Vào [ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.
2. Tạo một **hub** (hoặc dùng hub hiện có). Xem: [Tổng quan về tài nguyên Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Trong hub, tạo một **project**.
4. Triển khai một mô hình (ví dụ `gpt-5-mini`) từ **Models + Endpoints** → **Deploy model**.

### Bước 2: Lấy Endpoint Dự án và Tên Triển khai Mô hình

Từ dự án của bạn trong cổng Microsoft Foundry:

- **Project Endpoint** — Vào trang **Overview** và sao chép URL endpoint.

![Project Connection String](../../../translated_images/vi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vào **Models + Endpoints**, chọn mô hình đã triển khai, và ghi lại **Deployment name** (ví dụ `gpt-5-mini`).

### Bước 3: Đăng nhập Azure với `az login`

Hầu hết các notebook xác thực qua **đăng nhập Azure CLI** của bạn — dùng `AzureCliCredential` hoặc `DefaultAzureCredential` (cả hai đều dựa vào phiên `az login`) từ gói `azure-identity` — nên không cần API key. Một vài bài học và tích hợp tùy chọn dùng API key; kiểm tra yêu cầu từng bài học để biết biến môi trường thêm. Bạn cần đăng nhập qua Azure CLI.

1. **Cài Azure CLI** nếu bạn chưa có: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Đăng nhập** bằng cách chạy:

    ```bash
    az login
    ```

    Hoặc nếu bạn đang ở môi trường remote/Codespace không có trình duyệt:

    ```bash
    az login --use-device-code
    ```

3. **Chọn subscription** nếu được yêu cầu — chọn subscription chứa dự án Foundry của bạn.

4. **Xác nhận** bạn đã đăng nhập:

    ```bash
    az account show
    ```

> **Tại sao dùng `az login`?** Các notebook xác thực bằng `AzureCliCredential` (hoặc `DefaultAzureCredential`, cũng dựa vào đăng nhập Azure CLI) từ gói `azure-identity`. Nghĩa là phiên Azure CLI của bạn cung cấp chứng thực — không cần API key hay bí mật trong file `.env`. Đây là [thực hành bảo mật tốt nhất](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Bước 4: Tạo file `.env` của bạn

Sao chép file mẫu:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Mở `.env` và điền hai giá trị sau:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Cổng Foundry → dự án của bạn → trang **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Cổng Foundry → **Models + Endpoints** → tên mô hình đã triển khai |

Đó là tất cả cho hầu hết các bài học! Các notebook sẽ tự động xác thực qua phiên `az login` của bạn.

### Bước 5: Cài đặt các thư viện Python

```bash
pip install -r requirements.txt
```

Chúng tôi khuyến nghị chạy lệnh này trong môi trường ảo bạn đã tạo trước đó.

## Thiết lập Tùy chọn: Azure AI Search (Bài 5 và 16)

Notebook Bài 5 (Agentic RAG) và Bài 16 chạy trực tiếp với cơ sở kiến thức **lưu trong bộ nhớ** — không cần tài nguyên Azure thêm. Nếu bạn muốn sử dụng **Azure AI Search** thật, lưu ý rằng notebook Bài 16 hiện dùng xác thực bằng khóa: nó chuyển từ tìm kiếm trong bộ nhớ sang Azure AI Search chỉ khi **cả hai** biến `AZURE_SEARCH_SERVICE_ENDPOINT` **và** `AZURE_SEARCH_API_KEY` được đặt, nếu không vẫn dùng tìm kiếm trong bộ nhớ — nên để chạy trên chỉ mục thực bạn phải đặt khóa admin. Xác thực không khóa với Microsoft Entra ID (RBAC) là cách được khuyến nghị cho mã sản xuất, phù hợp với quy trình `az login` dùng trong toàn khóa học.

Các bước RBAC dưới đây áp dụng cho các mẫu trong hướng dẫn thiết lập và mã của bạn. Chúng không kích hoạt xác thực không khóa trong notebook Bài 16; Bài 16 vẫn cần cả endpoint và khóa admin để dùng Azure AI Search.

1. **Bật quyền truy cập dựa trên vai trò** trên dịch vụ tìm kiếm của bạn:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Gán cho bạn các vai trò cần thiết** (tạo/tải chỉ mục và truy vấn):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Thêm endpoint** vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Cổng Azure → tài nguyên **Azure AI Search** của bạn → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Bắt buộc (cùng endpoint) để bật Azure AI Search trong notebook Bài 16, dùng xác thực bằng khóa. Cổng Azure → **Settings** → **Keys** → khóa admin chính |

> **Tại sao không dùng khóa?** Khóa admin cấp quyền ghi toàn bộ cho dịch vụ tìm kiếm và có thể bị lộ qua file `.env`. Với RBAC, danh tính đăng nhập `az login` của bạn được dùng thay — cùng mẫu Entra ID không khóa mà các notebook khóa học dùng (qua `AzureCliCredential` / `DefaultAzureCredential`). Xem thêm [Kết nối tới Azure AI Search dùng vai trò](https://learn.microsoft.com/azure/search/search-security-rbac).

Xem [hướng dẫn thiết lập Azure AI Search](./AzureSearch.md) để có các mẫu tạo chỉ mục đầy đủ bằng Python và .NET.

## Thiết lập thêm cho các bài gọi Azure OpenAI Trực tiếp (Bài 6 và 8)

Một số notebook ở bài 6 và 8 gọi **Azure OpenAI** trực tiếp (dùng **Responses API**) thay vì qua dự án Microsoft Foundry. Các mẫu này trước đây dùng GitHub Models, đã bị ngừng hỗ trợ và không hỗ trợ Responses API. Thêm các biến này vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Cổng Azure → tài nguyên **Azure OpenAI** của bạn → **Keys and Endpoint** → Endpoint (ví dụ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Tên mô hình đã triển khai (ví dụ `gpt-5-mini`) hỗ trợ Responses API |
| `AZURE_OPENAI_API_KEY` | Tùy chọn — chỉ dùng nếu bạn dùng xác thực bằng khóa thay vì `az login` / Entra ID |

> Responses API dùng endpoint ổn định `/openai/v1/`, nên không cần `api-version`. Đăng nhập với `az login` để dùng xác thực Entra ID không khóa.

## Nhà cung cấp thay thế: MiniMax (tương thích OpenAI)

[MiniMax](https://platform.minimaxi.com/) cung cấp các mô hình ngữ cảnh lớn (lên tới 204K token) qua API tương thích OpenAI. Vì Microsoft Agent Framework's `OpenAIChatClient` có thể làm việc với bất kỳ endpoint tương thích OpenAI nào, bạn có thể dùng MiniMax như là lựa chọn thay thế cho các bài sử dụng `OpenAIChatClient`.

Thêm các biến này vào file `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Dùng `https://api.minimax.io/v1` (giá trị mặc định) |
| `MINIMAX_MODEL_ID` | Tên mô hình sử dụng (ví dụ `MiniMax-M3`) |

**Mô hình ví dụ**: `MiniMax-M3` (khuyến nghị), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (phản hồi nhanh hơn). Tên mô hình và khả dụng có thể thay đổi theo thời gian, và quyền truy cập vào mô hình nào tùy thuộc tài khoản của bạn.

Các mẫu mã dùng `OpenAIChatClient` (ví dụ workflow đặt phòng khách sạn Bài 14) sẽ tự động phát hiện và sử dụng cấu hình MiniMax của bạn khi `MINIMAX_API_KEY` được thiết lập.


## Nhà cung cấp thay thế: Novita AI (Tương thích OpenAI)

[Novita AI](https://novita.ai/llm-api) cung cấp API tương thích OpenAI cho các mô hình ngôn ngữ mở và tiên tiến (DeepSeek, Llama, Qwen và nhiều hơn nữa). Vì `OpenAIChatClient` của Microsoft Agent Framework hoạt động với bất kỳ điểm cuối tương thích OpenAI nào, bạn có thể sử dụng Novita AI như một lựa chọn thay thế thay thế hoàn toàn cho Azure OpenAI hoặc OpenAI.

Thêm các biến này vào tệp `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `NOVITA_API_KEY` | [Bảng điều khiển Novita AI](https://novita.ai/settings/key-management) → Khóa API |
| `NOVITA_BASE_URL` | Sử dụng `https://api.novita.ai/openai/v1` (giá trị mặc định) |
| `NOVITA_MODEL_ID` | Tên mô hình để sử dụng (ví dụ: `moonshotai/kimi-k3`) |

**Mẫu mô hình ví dụ**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI cũng lưu trữ nhiều họ mô hình mã nguồn mở khác (Llama, Qwen, GLM và nhiều hơn nữa) — xem [thư viện mô hình Novita AI](https://novita.ai/llm-api) để biết danh sách hiện tại các mô hình có sẵn và ID mô hình của chúng.

Các mẫu hiện tại không tự động sử dụng các biến `NOVITA_*`. Để sử dụng Novita AI, hãy truyền các giá trị này rõ ràng khi xây dựng `OpenAIChatClient` trong mẫu bạn đang chạy.

## Nhà cung cấp thay thế: Foundry Local (Chạy mô hình trên thiết bị)

[Foundry Local](https://foundrylocal.ai) là một runtime nhẹ tải xuống, quản lý và phục vụ các mô hình ngôn ngữ **hoàn toàn trên máy của bạn** thông qua API tương thích OpenAI — không cần đám mây.

Vì `OpenAIChatClient` của Microsoft Agent Framework hoạt động với bất kỳ điểm cuối tương thích OpenAI nào, Foundry Local là một lựa chọn thay thế cục bộ thay thế cho Azure OpenAI.

**1. Cài đặt Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Tải xuống và chạy một mô hình** (điều này cũng khởi động dịch vụ cục bộ):

```bash
foundry model list          # xem các mẫu có sẵn
foundry model run phi-4-mini
```

**3. Cài đặt SDK Python** được sử dụng để phát hiện điểm cuối cục bộ:

```bash
pip install foundry-local-sdk
```

**4. Đặt Microsoft Agent Framework trỏ tới mô hình cục bộ của bạn:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Tải xuống (nếu cần) và phục vụ mô hình cục bộ, sau đó phát hiện điểm cuối/cổng.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ví dụ http://localhost:<port>/v1
    api_key=manager.api_key,        # luôn luôn "không cần thiết" đối với Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Lưu ý:** Foundry Local cung cấp một điểm cuối **Chat Completions** tương thích OpenAI. Sử dụng nó cho phát triển cục bộ và các kịch bản ngoại tuyến. Để sử dụng đầy đủ bộ tính năng **Responses API** (cuộc hội thoại có trạng thái, v.v.), hãy sử dụng Azure OpenAI hoặc một dự án Microsoft Foundry.

## Thiết lập bổ sung cho Bài học 8 (Quy trình làm việc nền tảng Bing)

Sổ tay quy trình điều kiện trong bài học 8 sử dụng **nền tảng Bing** qua Microsoft Foundry. Nếu bạn dự định chạy mẫu đó, hãy thêm biến này vào tệp `.env` của bạn:

| Biến | Nơi tìm thấy |
|----------|-----------------|
| `BING_CONNECTION_ID` | Cổng Microsoft Foundry → dự án của bạn → **Quản lý** → **Tài nguyên kết nối** → kết nối Bing của bạn → sao chép ID kết nối |

## Khắc phục sự cố

### Lỗi xác thực chứng chỉ SSL trên macOS

Nếu bạn đang dùng macOS và gặp lỗi như sau:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Đây là sự cố đã biết với Python trên macOS khi các chứng chỉ SSL của hệ thống không được tin cậy tự động. Hãy thử các giải pháp sau theo thứ tự:

**Lựa chọn 1: Chạy script Cài đặt Chứng chỉ của Python (được khuyến nghị)**

```bash
# Thay thế 3.XX bằng phiên bản Python bạn đã cài đặt (ví dụ: 3.12 hoặc 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Lựa chọn 2: Sử dụng `connection_verify=False` trong sổ tay của bạn (chỉ dành cho sổ tay Mô hình GitHub)**

Trong sổ tay Bài học 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), đã có một cách khắc phục được chú thích. Bỏ chú thích `connection_verify=False` khi bạn gặp lỗi chứng chỉ:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vô hiệu hóa xác minh SSL nếu bạn gặp lỗi chứng chỉ
)
```

> **⚠️ Cảnh báo:** Tắt xác thực SSL (`connection_verify=False`) giảm độ an toàn bằng cách bỏ qua việc xác thực chứng chỉ. Chỉ sử dụng cách này như một giải pháp tạm thời trong môi trường phát triển. Không bao giờ sử dụng trong môi trường sản xuất.

**Lựa chọn 3: Cài đặt và sử dụng `truststore`**

```bash
pip install truststore
```

Sau đó thêm đoạn sau lên đầu sổ tay hoặc tập lệnh của bạn trước khi thực hiện bất kỳ gọi mạng nào:

```python
import truststore
truststore.inject_into_ssl()
```

## Bị mắc kẹt ở đâu đó?

Nếu bạn gặp bất kỳ sự cố nào khi chạy cài đặt này, hãy tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord Cộng đồng Azure AI</a> hoặc <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tạo một issue</a>.

## Bài học tiếp theo

Bây giờ bạn đã sẵn sàng chạy mã cho khóa học này. Chúc bạn học tập vui vẻ và tìm hiểu thêm về thế giới của các Đại lý AI! 

[Giới thiệu về Đại lý AI và Các trường hợp sử dụng đại lý](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->