<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:42:27+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
# Cài đặt khóa học

## Giới thiệu

Bài học này sẽ hướng dẫn cách chạy các mẫu mã của khóa học này.

## Tham gia cùng các học viên khác và nhận hỗ trợ

Trước khi bắt đầu sao chép kho lưu trữ của bạn, hãy tham gia [kênh Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) để nhận hỗ trợ cài đặt, giải đáp thắc mắc về khóa học hoặc kết nối với các học viên khác.

## Sao chép hoặc Fork kho lưu trữ này

Để bắt đầu, vui lòng sao chép hoặc fork kho lưu trữ GitHub. Điều này sẽ tạo phiên bản riêng của bạn về tài liệu khóa học để bạn có thể chạy, kiểm tra và chỉnh sửa mã!

Bạn có thể thực hiện điều này bằng cách nhấp vào liên kết <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork kho lưu trữ</a>

Bây giờ bạn sẽ có phiên bản fork của khóa học này tại liên kết sau:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.vi.png)

### Sao chép nông (khuyến nghị cho workshop / Codespaces)

  >Kho lưu trữ đầy đủ có thể rất lớn (~3 GB) khi bạn tải xuống toàn bộ lịch sử và tất cả các tệp. Nếu bạn chỉ tham gia workshop hoặc chỉ cần một vài thư mục bài học, việc sao chép nông (hoặc sao chép rời rạc) sẽ tránh được phần lớn tải xuống bằng cách cắt ngắn lịch sử và/hoặc bỏ qua các blob.

#### Sao chép nông nhanh — lịch sử tối thiểu, tất cả các tệp

Thay thế `<your-username>` trong các lệnh dưới đây bằng URL fork của bạn (hoặc URL upstream nếu bạn muốn).

Để sao chép chỉ lịch sử commit mới nhất (tải xuống nhỏ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Để sao chép một nhánh cụ thể:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Sao chép rời rạc — blob tối thiểu + chỉ các thư mục được chọn

Điều này sử dụng sao chép rời rạc và sparse-checkout (yêu cầu Git 2.25+ và khuyến nghị Git hiện đại với hỗ trợ sao chép rời rạc):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Đi vào thư mục kho lưu trữ:

```bash|powershell
cd ai-agents-for-beginners
```

Sau đó chỉ định các thư mục bạn muốn (ví dụ dưới đây hiển thị hai thư mục):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Sau khi sao chép và xác minh các tệp, nếu bạn chỉ cần các tệp và muốn giải phóng không gian (không có lịch sử git), vui lòng xóa metadata của kho lưu trữ (💀không thể khôi phục — bạn sẽ mất tất cả chức năng Git: không có commit, pull, push hoặc truy cập lịch sử).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Sử dụng GitHub Codespaces (khuyến nghị để tránh tải xuống lớn cục bộ)

- Tạo một Codespace mới cho kho lưu trữ này thông qua [Giao diện GitHub](https://github.com/codespaces).  

- Trong terminal của Codespace vừa tạo, chạy một trong các lệnh sao chép nông/rời rạc ở trên để chỉ mang các thư mục bài học bạn cần vào không gian làm việc Codespace.
- Tùy chọn: sau khi sao chép trong Codespaces, xóa .git để giải phóng thêm không gian (xem các lệnh xóa ở trên).
- Lưu ý: Nếu bạn muốn mở kho lưu trữ trực tiếp trong Codespaces (không cần sao chép thêm), hãy lưu ý rằng Codespaces sẽ xây dựng môi trường devcontainer và có thể vẫn cung cấp nhiều hơn bạn cần. Sao chép một bản sao nông bên trong một Codespace mới cho phép bạn kiểm soát tốt hơn việc sử dụng dung lượng đĩa.

#### Mẹo

- Luôn thay thế URL sao chép bằng fork của bạn nếu bạn muốn chỉnh sửa/commit.
- Nếu sau này bạn cần thêm lịch sử hoặc tệp, bạn có thể fetch chúng hoặc điều chỉnh sparse-checkout để bao gồm các thư mục bổ sung.

## Chạy mã

Khóa học này cung cấp một loạt các Jupyter Notebooks mà bạn có thể chạy để trải nghiệm thực hành xây dựng AI Agents.

Các mẫu mã sử dụng:

**Yêu cầu tài khoản GitHub - Miễn phí**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Được gắn nhãn là (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Được gắn nhãn là (autogen.ipynb)

**Yêu cầu đăng ký Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Được gắn nhãn là (azureaiagent.ipynb)

Chúng tôi khuyến khích bạn thử cả ba loại ví dụ để xem loại nào phù hợp nhất với bạn.

Dù bạn chọn tùy chọn nào, điều đó sẽ xác định các bước cài đặt bạn cần thực hiện dưới đây:

## Yêu cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài đặt Python3.12, hãy đảm bảo bạn cài đặt nó. Sau đó tạo venv của bạn bằng python3.12 để đảm bảo các phiên bản chính xác được cài đặt từ tệp requirements.txt.
  
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

- .NET 10+: Đối với các mã mẫu sử dụng .NET, hãy đảm bảo bạn cài đặt [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc mới hơn. Sau đó, kiểm tra phiên bản .NET SDK đã cài đặt của bạn:

    ```bash|powershell
    dotnet --list-sdks
    ```

- Tài khoản GitHub - Để truy cập GitHub Models Marketplace
- Đăng ký Azure - Để truy cập Azure AI Foundry
- Tài khoản Azure AI Foundry - Để truy cập Azure AI Agent Service

Chúng tôi đã bao gồm một tệp `requirements.txt` trong thư mục gốc của kho lưu trữ này, chứa tất cả các gói Python cần thiết để chạy các mẫu mã.

Bạn có thể cài đặt chúng bằng cách chạy lệnh sau trong terminal tại thư mục gốc của kho lưu trữ:

```bash|powershell
pip install -r requirements.txt
```

Chúng tôi khuyến nghị tạo một môi trường ảo Python để tránh bất kỳ xung đột và vấn đề nào.

## Cài đặt VSCode

Đảm bảo rằng bạn đang sử dụng đúng phiên bản Python trong VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Cài đặt cho các mẫu sử dụng GitHub Models 

### Bước 1: Lấy mã truy cập cá nhân (PAT) GitHub của bạn

Khóa học này sử dụng GitHub Models Marketplace, cung cấp quyền truy cập miễn phí vào các mô hình ngôn ngữ lớn (LLMs) mà bạn sẽ sử dụng để xây dựng AI Agents.

Để sử dụng GitHub Models, bạn sẽ cần tạo một [mã truy cập cá nhân GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Điều này có thể được thực hiện bằng cách truy cập <a href="https://github.com/settings/personal-access-tokens" target="_blank">cài đặt mã truy cập cá nhân</a> trong tài khoản GitHub của bạn.

Vui lòng tuân theo [Nguyên tắc tối thiểu quyền](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) khi tạo mã của bạn. Điều này có nghĩa là bạn chỉ nên cấp cho mã các quyền cần thiết để chạy các mẫu mã trong khóa học này.

1. Chọn tùy chọn `Fine-grained tokens` ở phía bên trái màn hình của bạn bằng cách truy cập **Developer settings**

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.vi.png)

   Sau đó chọn `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.vi.png)

2. Nhập tên mô tả cho mã của bạn phản ánh mục đích của nó, giúp dễ dàng nhận diện sau này.

    🔐 Khuyến nghị thời gian tồn tại mã

    Thời gian khuyến nghị: 30 ngày
    Để bảo mật hơn, bạn có thể chọn thời gian ngắn hơn—chẳng hạn như 7 ngày 🛡️
    Đây là cách tuyệt vời để đặt mục tiêu cá nhân và hoàn thành khóa học trong khi động lực học tập của bạn đang cao 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.vi.png)

3. Giới hạn phạm vi của mã vào fork của kho lưu trữ này.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.vi.png)

4. Hạn chế quyền của mã: Trong **Permissions**, nhấp vào tab **Account**, và nhấp vào nút "+ Add permissions". Một menu thả xuống sẽ xuất hiện. Vui lòng tìm kiếm **Models** và đánh dấu vào ô.

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.vi.png)

5. Xác minh các quyền cần thiết trước khi tạo mã. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.vi.png)

6. Trước khi tạo mã, hãy đảm bảo bạn sẵn sàng lưu mã trong nơi an toàn như kho mật khẩu, vì nó sẽ không được hiển thị lại sau khi bạn tạo. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.vi.png)

Sao chép mã mới mà bạn vừa tạo. Bây giờ bạn sẽ thêm mã này vào tệp `.env` được bao gồm trong khóa học này.

### Bước 2: Tạo tệp `.env` của bạn

Để tạo tệp `.env`, chạy lệnh sau trong terminal của bạn.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Điều này sẽ sao chép tệp ví dụ và tạo một `.env` trong thư mục của bạn, nơi bạn điền các giá trị cho các biến môi trường.

Với mã của bạn đã được sao chép, mở tệp `.env` trong trình soạn thảo văn bản yêu thích của bạn và dán mã vào trường `GITHUB_TOKEN`.

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.vi.png)

Bây giờ bạn đã có thể chạy các mẫu mã của khóa học này.

## Cài đặt cho các mẫu sử dụng Azure AI Foundry và Azure AI Agent Service

### Bước 1: Lấy điểm cuối dự án Azure của bạn

Làm theo các bước để tạo hub và dự án trong Azure AI Foundry tại đây: [Tổng quan về tài nguyên hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Sau khi bạn đã tạo dự án của mình, bạn sẽ cần lấy chuỗi kết nối cho dự án của mình.

Điều này có thể được thực hiện bằng cách truy cập trang **Overview** của dự án trong cổng Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.vi.png)

### Bước 2: Tạo tệp `.env` của bạn

Để tạo tệp `.env`, chạy lệnh sau trong terminal của bạn.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Điều này sẽ sao chép tệp ví dụ và tạo một `.env` trong thư mục của bạn, nơi bạn điền các giá trị cho các biến môi trường.

Với mã của bạn đã được sao chép, mở tệp `.env` trong trình soạn thảo văn bản yêu thích của bạn và dán mã vào trường `PROJECT_ENDPOINT`.

### Bước 3: Đăng nhập vào Azure

Theo thực hành bảo mật tốt nhất, chúng ta sẽ sử dụng [xác thực không cần khóa](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) để xác thực vào Azure OpenAI với Microsoft Entra ID. 

Tiếp theo, mở terminal và chạy `az login --use-device-code` để đăng nhập vào tài khoản Azure của bạn.

Sau khi bạn đã đăng nhập, chọn đăng ký của bạn trong terminal.

## Các biến môi trường bổ sung - Azure Search và Azure OpenAI 

Đối với bài học Agentic RAG - Bài học 5 - có các mẫu sử dụng Azure Search và Azure OpenAI.

Nếu bạn muốn chạy các mẫu này, bạn sẽ cần thêm các biến môi trường sau vào tệp `.env` của bạn:

### Trang Tổng quan (Dự án)

- `AZURE_SUBSCRIPTION_ID` - Kiểm tra **Chi tiết dự án** trên trang **Overview** của dự án của bạn.

- `AZURE_AI_PROJECT_NAME` - Xem ở đầu trang **Overview** của dự án của bạn.

- `AZURE_OPENAI_SERVICE` - Tìm thấy trong tab **Included capabilities** cho **Azure OpenAI Service** trên trang **Overview**.

### Trung tâm Quản lý

- `AZURE_OPENAI_RESOURCE_GROUP` - Đi tới **Thuộc tính dự án** trên trang **Overview** của **Trung tâm Quản lý**.

- `GLOBAL_LLM_SERVICE` - Dưới **Connected resources**, tìm tên kết nối **Azure AI Services**. Nếu không được liệt kê, kiểm tra **cổng Azure** dưới nhóm tài nguyên của bạn để tìm tên tài nguyên AI Services.

### Trang Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Chọn mô hình embedding của bạn (ví dụ: `text-embedding-ada-002`) và ghi lại **Tên triển khai** từ chi tiết mô hình.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chọn mô hình chat của bạn (ví dụ: `gpt-4o-mini`) và ghi lại **Tên triển khai** từ chi tiết mô hình.

### Cổng Azure

- `AZURE_OPENAI_ENDPOINT` - Tìm **Azure AI services**, nhấp vào nó, sau đó đi tới **Quản lý tài nguyên**, **Keys and Endpoint**, cuộn xuống "Azure OpenAI endpoints", và sao chép cái có ghi "Language APIs".

- `AZURE_OPENAI_API_KEY` - Từ cùng màn hình, sao chép KEY 1 hoặc KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Tìm tài nguyên **Azure AI Search** của bạn, nhấp vào nó, và xem **Overview**.

- `AZURE_SEARCH_API_KEY` - Sau đó đi tới **Settings** và sau đó **Keys** để sao chép khóa admin chính hoặc phụ.

### Trang web bên ngoài

- `AZURE_OPENAI_API_VERSION` - Truy cập trang [vòng đời phiên bản API](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) dưới **Phiên bản API GA mới nhất**.

### Cài đặt xác thực không cần khóa

Thay vì mã hóa cứng thông tin đăng nhập của bạn, chúng ta sẽ sử dụng kết nối không cần khóa với Azure OpenAI. Để làm điều này, chúng ta sẽ import `DefaultAzureCredential` và sau đó gọi hàm `DefaultAzureCredential` để lấy thông tin đăng nhập.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bị mắc kẹt ở đâu đó?
Nếu bạn gặp bất kỳ vấn đề nào khi chạy thiết lập này, hãy tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord Cộng đồng Azure AI</a> của chúng tôi hoặc <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tạo một vấn đề mới</a>.

## Bài học tiếp theo

Bạn đã sẵn sàng để chạy mã cho khóa học này. Chúc bạn học vui về thế giới của AI Agents!

[Giới thiệu về AI Agents và các trường hợp sử dụng của Agent](../01-intro-to-ai-agents/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.