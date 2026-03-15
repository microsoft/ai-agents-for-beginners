# Thiết lập Khóa học

## Giới thiệu

Bài học này sẽ hướng dẫn cách chạy các ví dụ mã trong khóa học này.

## Tham gia cùng những người học khác và nhận trợ giúp

Trước khi bạn bắt đầu sao chép repo của mình, hãy tham gia [kênh Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) để nhận trợ giúp về thiết lập, mọi câu hỏi về khóa học, hoặc để kết nối với những người học khác.

## Sao chép hoặc Fork repo này

Để bắt đầu, hãy sao chép hoặc fork GitHub Repository. Điều này sẽ tạo phiên bản riêng của bạn của tài liệu khóa học để bạn có thể chạy, kiểm tra và chỉnh sửa mã!

Bạn có thể làm điều này bằng cách nhấp vào liên kết <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Bạn bây giờ nên có phiên bản repo đã fork của khóa học này tại liên kết sau:

![Repo đã fork](../../../translated_images/vi/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (được khuyến nghị cho workshop / Codespaces)

  >Toàn bộ repository có thể lớn (~3 GB) khi bạn tải xuống lịch sử đầy đủ và tất cả các tệp. Nếu bạn chỉ tham dự workshop hoặc chỉ cần một vài thư mục bài học, một shallow clone (hoặc sparse clone) tránh phần lớn việc tải xuống đó bằng cách rút ngắn lịch sử và/hoặc bỏ qua các blob.

#### Quick shallow clone — lịch sử tối thiểu, tất cả các tệp

Thay thế `<your-username>` trong các lệnh dưới bằng URL fork của bạn (hoặc URL upstream nếu bạn thích).

Để clone chỉ lịch sử commit mới nhất (tải xuống nhỏ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Để clone một nhánh cụ thể:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — blob tối thiểu + chỉ các thư mục được chọn

Điều này sử dụng partial clone và sparse-checkout (yêu cầu Git 2.25+ và khuyến nghị dùng Git hiện đại hỗ trợ partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Đi sâu vào thư mục repo:

```bash|powershell
cd ai-agents-for-beginners
```

Sau đó chỉ định các thư mục bạn muốn (ví dụ bên dưới hiển thị hai thư mục):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Sau khi clone và kiểm tra các tệp, nếu bạn chỉ cần các tệp và muốn giải phóng không gian (không còn lịch sử git), hãy xóa metadata của repository (💀không thể phục hồi — bạn sẽ mất toàn bộ chức năng Git: không còn commit, pull, push, hay truy cập lịch sử).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Sử dụng GitHub Codespaces (khuyến nghị để tránh tải xuống cục bộ lớn)

- Tạo một Codespace mới cho repo này qua [GitHub UI](https://github.com/codespaces).  

- Trong terminal của codespace mới tạo, chạy một trong các lệnh shallow/sparse clone ở trên để chỉ đưa các thư mục bài học bạn cần vào workspace của Codespace.
- Tùy chọn: sau khi clone bên trong Codespaces, xóa .git để thu hồi thêm dung lượng (xem các lệnh xóa ở trên).
- Lưu ý: Nếu bạn thích mở repo trực tiếp trong Codespaces (không clone thêm), hãy lưu ý Codespaces sẽ xây dựng môi trường devcontainer và có thể vẫn cung cấp nhiều hơn bạn cần. Clone một bản sao shallow bên trong Codespace mới cho phép bạn kiểm soát tốt hơn việc sử dụng đĩa.

#### Mẹo

- Luôn thay URL clone bằng fork của bạn nếu bạn muốn chỉnh sửa/commit.
- Nếu sau này bạn cần nhiều lịch sử hoặc tệp hơn, bạn có thể fetch chúng hoặc điều chỉnh sparse-checkout để bao gồm thêm thư mục.

## Chạy Mã

Khóa học này cung cấp một loạt Jupyter Notebooks mà bạn có thể chạy để có trải nghiệm thực hành xây dựng AI Agents.

Các ví dụ mã sử dụng **Microsoft Agent Framework (MAF)** với `AzureAIProjectAgentProvider`, kết nối với **Azure AI Agent Service V2** (Responses API) thông qua **Microsoft Foundry**.

Tất cả notebook Python được gán nhãn `*-python-agent-framework.ipynb`.

## Yêu cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài Python3.12, hãy cài đặt nó. Sau đó tạo venv bằng python3.12 để đảm bảo các phiên bản đúng được cài từ file requirements.txt.
  
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

- .NET 10+: Đối với các mã mẫu dùng .NET, đảm bảo bạn cài [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc phiên bản mới hơn. Sau đó, kiểm tra phiên bản .NET SDK đã cài:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Yêu cầu để xác thực. Cài đặt từ [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Để truy cập Microsoft Foundry và Azure AI Agent Service.
- **Microsoft Foundry Project** — Một project có mô hình được triển khai (ví dụ `gpt-4o`). Xem [Bước 1](../../../00-course-setup) bên dưới.

Chúng tôi đã bao gồm file `requirements.txt` ở gốc repository này chứa tất cả các gói Python cần thiết để chạy các ví dụ mã.

Bạn có thể cài chúng bằng cách chạy lệnh sau trong terminal tại thư mục gốc của repository:

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyến nghị tạo một môi trường ảo Python để tránh xung đột và sự cố.

## Thiết lập VSCode

Hãy đảm bảo rằng bạn đang sử dụng đúng phiên bản Python trong VSCode.

![hình ảnh](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Thiết lập Microsoft Foundry và Azure AI Agent Service

### Bước 1: Tạo một Microsoft Foundry Project

Bạn cần một **hub** và **project** Azure AI Foundry với một mô hình đã được triển khai để chạy các notebook.

1. Truy cập [ai.azure.com](https://ai.azure.com) và đăng nhập bằng tài khoản Azure của bạn.
2. Tạo một **hub** (hoặc dùng hub đã có). Xem: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Bên trong hub, tạo một **project**.
4. Triển khai một mô hình (ví dụ `gpt-4o`) từ **Models + Endpoints** → **Deploy model**.

### Bước 2: Lấy Endpoint Dự Án và Tên Triển Khai Mô Hình

Từ project của bạn trong cổng Microsoft Foundry:

- **Project Endpoint** — Vào trang **Overview** và sao chép URL endpoint.

![Chuỗi kết nối dự án](../../../translated_images/vi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vào **Models + Endpoints**, chọn mô hình đã triển khai của bạn, và ghi lại **Deployment name** (ví dụ `gpt-4o`).

### Bước 3: Đăng nhập vào Azure với `az login`

Tất cả các notebook sử dụng **`AzureCliCredential`** để xác thực — không có API key nào phải quản lý. Điều này yêu cầu bạn đăng nhập qua Azure CLI.

1. **Cài đặt Azure CLI** nếu bạn chưa: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Đăng nhập** bằng cách chạy:

    ```bash|powershell
    az login
    ```

    Hoặc nếu bạn ở môi trường remote/Codespace không có trình duyệt:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chọn subscription** nếu được nhắc — chọn subscription chứa project Foundry của bạn.

4. **Xác minh** bạn đã đăng nhập:

    ```bash|powershell
    az account show
    ```

> **Tại sao `az login`?** Các notebook xác thực bằng `AzureCliCredential` từ package `azure-identity`. Điều này có nghĩa session Azure CLI của bạn cung cấp thông tin xác thực — không có API key hay secret trong file `.env` của bạn. Đây là một [thực hành bảo mật tốt nhất](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Bước 4: Tạo file `.env` của bạn

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

Chỉ vậy là xong cho hầu hết các bài học! Các notebook sẽ xác thực tự động thông qua session `az login` của bạn.

### Bước 5: Cài các Phụ thuộc Python

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyến nghị chạy lệnh này bên trong môi trường ảo bạn đã tạo trước đó.

## Thiết lập thêm cho Bài học 5 (Agentic RAG)

Bài học 5 sử dụng **Azure AI Search** cho retrieval-augmented generation. Nếu bạn dự định chạy bài học đó, thêm các biến này vào file `.env` của bạn:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Thiết lập thêm cho Bài học 6 và Bài học 8 (GitHub Models)

Một số notebook trong bài học 6 và 8 sử dụng **GitHub Models** thay vì Azure AI Foundry. Nếu bạn dự định chạy những ví dụ đó, thêm các biến này vào file `.env` của bạn:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Thiết lập thêm cho Bài học 8 (Bing Grounding Workflow)

Notebook workflow có điều kiện trong bài học 8 sử dụng **Bing grounding** qua Azure AI Foundry. Nếu bạn dự định chạy ví dụ đó, thêm biến này vào file `.env` của bạn:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Khắc phục sự cố

### Lỗi xác thực chứng chỉ SSL trên macOS

Nếu bạn đang dùng macOS và gặp lỗi như:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Đây là vấn đề đã biết với Python trên macOS khi các chứng chỉ SSL của hệ thống không được tin cậy tự động. Hãy thử các giải pháp sau theo thứ tự:

**Tùy chọn 1: Chạy script Install Certificates của Python (khuyến nghị)**

```bash
# Thay 3.XX bằng phiên bản Python bạn đã cài đặt (ví dụ: 3.12 hoặc 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Tùy chọn 2: Sử dụng `connection_verify=False` trong notebook của bạn (chỉ cho các notebook GitHub Models)**

Trong notebook Bài 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), một cách khắc phục đã được chú thích sẵn. Bỏ chú thích `connection_verify=False` khi tạo client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Vô hiệu hóa việc xác minh SSL nếu bạn gặp lỗi chứng chỉ
)
```

> **⚠️ Cảnh báo:** Vô hiệu hóa xác thực SSL (`connection_verify=False`) làm giảm bảo mật bằng cách bỏ qua kiểm tra chứng chỉ. Chỉ sử dụng điều này như một giải pháp tạm thời trong môi trường phát triển, không bao giờ dùng trong sản xuất.

**Tùy chọn 3: Cài và sử dụng `truststore`**

```bash
pip install truststore
```

Sau đó thêm đoạn sau ở đầu notebook hoặc script trước khi thực hiện bất kỳ cuộc gọi mạng nào:

```python
import truststore
truststore.inject_into_ssl()
```

## Bị mắc kẹt ở đâu đó?

Nếu bạn có bất kỳ vấn đề nào khi chạy thiết lập này, hãy vào <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> của chúng tôi hoặc <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tạo một issue</a>.

## Bài học tiếp theo

Bây giờ bạn đã sẵn sàng để chạy mã cho khóa học này. Chúc bạn học vui về thế giới AI Agents! 

[Giới thiệu về AI Agents và Các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tuyên bố miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI Co-op Translator (https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn có thẩm quyền. Đối với thông tin quan trọng, khuyến nghị sử dụng bản dịch chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->