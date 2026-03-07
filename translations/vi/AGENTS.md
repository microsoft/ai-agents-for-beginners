# AGENTS.md

## Tổng Quan Dự Án

Kho lưu trữ này chứa "AI Agents cho Người Mới Bắt Đầu" - một khóa học giáo dục toàn diện dạy mọi thứ cần thiết để xây dựng các AI Agents. Khóa học gồm hơn 15 bài học bao gồm các kiến thức cơ bản, mẫu thiết kế, framework và triển khai sản xuất các agent AI.

**Công nghệ chính:**
- Python 3.12+
- Jupyter Notebooks để học tương tác
- Framework AI: Microsoft Agent Framework (MAF)
- Dịch vụ AI Azure: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Kiến trúc:**
- Cấu trúc theo bài học (các thư mục 00-15+)
- Mỗi bài học có: tài liệu README, ví dụ code (Jupyter notebooks), và hình ảnh
- Hỗ trợ đa ngôn ngữ qua hệ thống dịch tự động
- Một notebook Python mỗi bài học sử dụng Microsoft Agent Framework

## Lệnh Cài Đặt

### Yêu Cầu Trước

- Python 3.12 trở lên
- Tài khoản Azure (cho Azure AI Foundry)
- Azure CLI được cài và đăng nhập (`az login`)

### Thiết Lập Ban Đầu

1. **Clone hoặc fork kho lưu trữ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # HOẶC
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tạo và kích hoạt môi trường ảo Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   ```

3. **Cài đặt các phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Đặt biến môi trường:**
   ```bash
   cp .env.example .env
   # Chỉnh sửa .env với khóa API và điểm cuối của bạn
   ```

### Biến Môi Trường Cần Thiết

Cho **Azure AI Foundry** (cần thiết):
- `AZURE_AI_PROJECT_ENDPOINT` - điểm cuối dự án Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - tên triển khai mô hình (ví dụ: gpt-4o)

Cho **Azure AI Search** (Bài 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - điểm cuối Azure AI Search
- `AZURE_SEARCH_API_KEY` - khóa API Azure AI Search

Xác thực: Chạy `az login` trước khi chạy notebooks (sử dụng `AzureCliCredential`).

## Quy Trình Phát Triển

### Chạy Jupyter Notebooks

Mỗi bài học gồm nhiều notebook Jupyter cho các framework khác nhau:

1. **Khởi động Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Đi tới thư mục bài học** (ví dụ, `01-intro-to-ai-agents/code_samples/`)

3. **Mở và chạy notebook:**
   - `*-python-agent-framework.ipynb` - Dùng Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Dùng Microsoft Agent Framework (.NET)

### Làm Việc Với Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Yêu cầu tài khoản Azure
- Sử dụng `AzureAIProjectAgentProvider` cho Agent Service V2 (agent hiển thị trong cổng Foundry)
- Sẵn sàng cho môi trường sản xuất với khả năng theo dõi tích hợp
- Định dạng file: `*-python-agent-framework.ipynb`

## Hướng Dẫn Kiểm Tra

Đây là kho mã giáo dục với mã ví dụ thay vì mã sản xuất có kiểm thử tự động. Để xác minh thiết lập và thay đổi:

### Kiểm Tra Thủ Công

1. **Kiểm tra môi trường Python:**
   ```bash
   python --version  # Nên là 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Kiểm tra thực thi notebook:**
   ```bash
   # Chuyển đổi sổ tay thành tập lệnh và chạy (kiểm tra các lần nhập)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Xác minh biến môi trường:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Chạy Từng Notebook Riêng Lẻ

Mở các notebook trong Jupyter và chạy các ô lần lượt. Mỗi notebook độc lập và gồm có:
- Câu lệnh import
- Tải cấu hình
- Ví dụ triển khai agent
- Kết quả dự kiến trong ô markdown

## Quy Tắc Viết Code

### Quy Ước Python

- **Phiên bản Python**: 3.12+
- **Phong cách code**: Tuân theo tiêu chuẩn PEP 8 của Python
- **Notebook**: Sử dụng ô markdown rõ ràng để giải thích khái niệm
- **Imports**: Nhóm theo thư viện chuẩn, thư viện bên thứ ba, import cục bộ

### Quy Ước Jupyter Notebook

- Bao gồm ô markdown mô tả trước ô code
- Thêm ví dụ đầu ra trong notebook để tham khảo
- Dùng tên biến rõ ràng phù hợp với khái niệm bài học
- Giữ thứ tự chạy notebook tuyến tính (ô 1 → 2 → 3...)

### Tổ Chức File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Xây Dựng Và Triển Khai

### Xây dựng Tài liệu

Kho lưu trữ dùng Markdown cho tài liệu:
- Các file README.md trong từng thư mục bài học
- README.md chính ở thư mục gốc
- Hệ thống dịch tự động qua GitHub Actions

### Quy trình CI/CD

Nằm trong `.github/workflows/`:

1. **co-op-translator.yml** - Dịch tự động sang hơn 50 ngôn ngữ
2. **welcome-issue.yml** - Chào mừng người tạo issue mới
3. **welcome-pr.yml** - Chào mừng người đóng góp pull request mới

### Triển khai

Đây là kho học tập - không có quy trình triển khai. Người dùng:
1. Fork hoặc clone kho lưu trữ
2. Chạy notebooks tại địa phương hoặc trong GitHub Codespaces
3. Học bằng cách chỉnh sửa và thử nghiệm ví dụ

## Hướng Dẫn Pull Request

### Trước Khi Gửi

1. **Kiểm tra thay đổi:**
   - Chạy đầy đủ các notebook ảnh hưởng
   - Đảm bảo các ô thực thi không lỗi
   - Kiểm tra đầu ra phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật README.md nếu thêm khái niệm mới
   - Thêm chú thích trong notebook cho đoạn code phức tạp
   - Đảm bảo ô markdown giải thích mục đích

3. **Thay đổi file:**
   - Tránh commit file `.env` (dùng `.env.example` thay thế)
   - Không commit thư mục `venv/` hay `__pycache__/`
   - Giữ đầu ra notebook nếu thể hiện khái niệm
   - Loại bỏ file tạm thời và notebook sao lưu (`*-backup.ipynb`)

### Định Dạng Tiêu Đề PR

Dùng tiêu đề mô tả:
- `[Lesson-XX] Thêm ví dụ mới cho <khái niệm>`
- `[Fix] Sửa lỗi chính tả trong README bài-XX`
- `[Update] Cải thiện ví dụ code trong bài-XX`
- `[Docs] Cập nhật hướng dẫn thiết lập`

### Các Kiểm Tra Bắt Buộc

- Notebooks chạy không lỗi
- README rõ ràng và chính xác
- Tuân theo mẫu code hiện có trong kho
- Giữ sự nhất quán với các bài học khác

## Ghi Chú Bổ Sung

### Các Vấn Đề Thường Gặp

1. **Phiên bản Python không phù hợp:**
   - Đảm bảo dùng Python 3.12+
   - Một số package không hoạt động với phiên bản cũ hơn
   - Dùng `python3 -m venv` để chỉ định phiên bản Python rõ ràng

2. **Biến môi trường:**
   - Luôn tạo `.env` từ `.env.example`
   - Không commit file `.env` (nằm trong `.gitignore`)
   - Token GitHub cần quyền phù hợp

3. **Xung đột package:**
   - Dùng môi trường ảo mới
   - Cài từ `requirements.txt` thay vì từng package riêng lẻ
   - Một số notebook yêu cầu thêm package được đề cập trong ô markdown

4. **Dịch vụ Azure:**
   - Dịch vụ AI Azure yêu cầu đăng ký còn hiệu lực
   - Một số tính năng chỉ hỗ trợ vùng cụ thể
   - Giới hạn tầng miễn phí áp dụng với GitHub Models

### Lộ Trình Học Tập

Khuyến nghị học theo trình tự:
1. **00-course-setup** - Bắt đầu thiết lập môi trường
2. **01-intro-to-ai-agents** - Tìm hiểu cơ bản AI agent
3. **02-explore-agentic-frameworks** - Tìm hiểu các framework khác nhau
4. **03-agentic-design-patterns** - Mẫu thiết kế cốt lõi
5. Tiếp tục theo các bài đánh số lần lượt

### Lựa Chọn Framework

Chọn framework dựa trên mục tiêu:
- **Tất cả bài học**: Microsoft Agent Framework (MAF) với `AzureAIProjectAgentProvider`
- **Agent đăng ký phía server** trong Azure AI Foundry Agent Service V2 và hiển thị trong cổng Foundry

### Hỗ Trợ

- Tham gia nhóm [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Xem README bài học để có hướng dẫn cụ thể
- Xem [README.md](./README.md) chính để tổng quan khóa học
- Tham khảo [Course Setup](./00-course-setup/README.md) cho hướng dẫn chi tiết

### Đóng Góp

Đây là dự án giáo dục mở. Hoan nghênh đóng góp:
- Cải thiện ví dụ code
- Sửa lỗi chính tả hoặc lỗi
- Thêm chú thích làm rõ
- Đề xuất chủ đề bài học mới
- Dịch sang ngôn ngữ khác

Xem [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) cho các nhu cầu hiện tại.

## Ngữ Cảnh Dự Án

### Hỗ Trợ Đa Ngôn Ngữ

Kho lưu trữ sử dụng hệ thống dịch tự động:
- Hỗ trợ hơn 50 ngôn ngữ
- Bản dịch trong thư mục `/translations/<mã-ngôn-ngữ>/`
- Quy trình GitHub Actions xử lý cập nhật dịch
- Các file nguồn bằng tiếng Anh ở thư mục gốc

### Cấu Trúc Bài Học

Mỗi bài có mẫu nhất quán:
1. Ảnh thumbnail video với liên kết
2. Nội dung bài học bằng văn bản (README.md)
3. Ví dụ code trên nhiều framework
4. Mục tiêu học tập và yêu cầu tiền đề
5. Liên kết đến tài liệu học thêm

### Đặt Tên File Ví Dụ

Định dạng: `<số-bài>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Bài 1, MAF Python
- `14-sequential.ipynb` - Bài 14, mẫu nâng cao MAF

### Thư Mục Đặc Biệt

- `translated_images/` - Hình ảnh bản địa hóa cho dịch thuật
- `images/` - Hình ảnh gốc cho nội dung tiếng Anh
- `.devcontainer/` - Cấu hình container phát triển cho VS Code
- `.github/` - Quy trình GitHub Actions và mẫu

### Phụ Thuộc

Các package chính từ `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Hỗ trợ giao thức agent-to-agent
- `azure-ai-inference`, `azure-ai-projects` - Dịch vụ AI Azure
- `azure-identity` - Xác thực Azure (AzureCliCredential)
- `azure-search-documents` - Tích hợp Azure AI Search
- `mcp[cli]` - Hỗ trợ Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->