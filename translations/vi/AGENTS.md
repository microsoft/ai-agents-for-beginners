# AGENTS.md

## Tổng Quan Dự Án

Kho lưu trữ này chứa "Đại Lý AI cho Người Mới Bắt Đầu" - một khóa học giáo dục toàn diện dạy mọi thứ cần thiết để xây dựng Đại Lý AI. Khóa học bao gồm hơn 15 bài học bao quát các nền tảng, mẫu thiết kế, khung làm việc và triển khai sản xuất của các đại lý AI.

**Công nghệ chính:**
- Python 3.12+
- Jupyter Notebooks cho học tương tác
- Khung AI: Microsoft Agent Framework (MAF)
- Dịch vụ AI Azure: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Kiến trúc:**
- Cấu trúc dựa trên bài học (thư mục 00-15+)
- Mỗi bài học chứa: tài liệu README, mẫu mã (Jupyter notebooks) và hình ảnh
- Hỗ trợ đa ngôn ngữ qua hệ thống dịch tự động
- Một notebook Python cho mỗi bài học sử dụng Microsoft Agent Framework

## Các Lệnh Thiết Lập

### Yêu Cầu Trước

- Python 3.12 trở lên
- Đăng ký Azure (cho Azure AI Foundry)
- Azure CLI được cài và đăng nhập (`az login`)

### Thiết Lập Ban Đầu

1. **Sao chép hoặc fork kho lưu trữ:**
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

4. **Thiết lập biến môi trường:**
   ```bash
   cp .env.example .env
   # Chỉnh sửa .env với các khóa API và điểm cuối của bạn
   ```

### Biến Môi Trường Cần Thiết

Đối với **Azure AI Foundry** (Bắt buộc):
- `AZURE_AI_PROJECT_ENDPOINT` - điểm cuối dự án Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - tên triển khai mô hình (ví dụ: gpt-4o)

Đối với **Azure AI Search** (Bài 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - điểm cuối Azure AI Search
- `AZURE_SEARCH_API_KEY` - khóa API Azure AI Search

Xác thực: Chạy `az login` trước khi chạy notebooks (sử dụng `AzureCliCredential`).

## Quy Trình Phát Triển

### Chạy Jupyter Notebooks

Mỗi bài học chứa nhiều notebook Jupyter cho các khung làm việc khác nhau:

1. **Khởi động Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Đi đến thư mục bài học** (ví dụ `01-intro-to-ai-agents/code_samples/`)

3. **Mở và chạy các notebook:**
   - `*-python-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (.NET)

### Làm Việc với Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Yêu cầu đăng ký Azure
- Sử dụng `AzureAIProjectAgentProvider` cho Agent Service V2 (các đại lý hiển thị trên cổng Foundry)
- Sẵn sàng cho sản xuất với khả năng quan sát tích hợp
- Mẫu tệp: `*-python-agent-framework.ipynb`

## Hướng Dẫn Kiểm Thử

Đây là kho lưu trữ giáo dục với mã ví dụ chứ không phải mã sản xuất có kiểm thử tự động. Để xác minh thiết lập và thay đổi của bạn:

### Kiểm Thử Thủ Công

1. **Kiểm thử môi trường Python:**
   ```bash
   python --version  # Nên là 3.12 trở lên
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Kiểm thử thực thi notebook:**
   ```bash
   # Chuyển đổi sổ tay sang kịch bản và chạy (kiểm tra nhập khẩu)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Xác minh biến môi trường:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Chạy Các Notebook Riêng Lẻ

Mở các notebook trong Jupyter và thực thi các ô theo thứ tự. Mỗi notebook có nội dung độc lập và bao gồm:
- Các lệnh import
- Tải cấu hình
- Ví dụ thực thi đại lý
- Kết quả dự kiến trong các ô markdown

## Phong Cách Mã

### Quy Ước Python

- **Phiên bản Python**: 3.12+
- **Phong cách mã**: Theo chuẩn PEP 8 Python
- **Notebooks**: Dùng các ô markdown rõ ràng để giải thích khái niệm
- **Import**: Nhóm theo thư viện chuẩn, bên thứ ba, và nhập khẩu cục bộ

### Quy Ước Jupyter Notebook

- Bao gồm các ô markdown mô tả trước các ô mã
- Thêm ví dụ đầu ra trong notebooks để tham khảo
- Dùng tên biến rõ ràng phù hợp với khái niệm bài học
- Giữ thứ tự thực thi notebook tuyến tính (ô 1 → 2 → 3...)

### Tổ Chức Tệp Tin

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Xây Dựng và Triển Khai

### Xây dựng Tài Liệu

Kho lưu trữ này dùng Markdown cho tài liệu:
- File README.md trong mỗi thư mục bài học
- README.md chính ở thư mục gốc kho lưu trữ
- Hệ thống dịch tự động qua GitHub Actions

### Pipeline CI/CD

Nằm trong thư mục `.github/workflows/`:

1. **co-op-translator.yml** - Dịch tự động sang hơn 50 ngôn ngữ
2. **welcome-issue.yml** - Chào mừng người tạo issue mới
3. **welcome-pr.yml** - Chào mừng người đóng góp pull request mới

### Triển Khai

Đây là kho lưu trữ giáo dục - không có quy trình triển khai. Người dùng:
1. Fork hoặc clone kho lưu trữ
2. Chạy notebooks tại chỗ hoặc trong GitHub Codespaces
3. Học qua chỉnh sửa và thử nghiệm ví dụ

## Hướng Dẫn Pull Request

### Trước Khi Gửi

1. **Kiểm thử thay đổi:**
   - Chạy hoàn toàn các notebooks bị ảnh hưởng
   - Đảm bảo các ô chạy không lỗi
   - Kiểm tra đầu ra phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật README.md khi thêm khái niệm mới
   - Thêm chú thích trong notebooks cho mã phức tạp
   - Đảm bảo ô markdown giải thích mục đích

3. **Thay đổi tệp:**
   - Không commit các file `.env` (dùng `.env.example`)
   - Không commit thư mục `venv/` hoặc `__pycache__/`
   - Giữ lại đầu ra notebook khi chúng minh hoạ khái niệm
   - Xoá các tệp tạm thời và backup notebooks (`*-backup.ipynb`)

### Định Dạng Tiêu Đề PR

Dùng tiêu đề mô tả:
- `[Lesson-XX] Thêm ví dụ mới cho <khái niệm>`
- `[Fix] Sửa lỗi chính tả trong README bài học-XX`
- `[Update] Cải thiện mẫu mã trong bài học-XX`
- `[Docs] Cập nhật hướng dẫn thiết lập`

### Yêu Cầu Kiểm Tra

- Notebooks chạy không lỗi
- Tệp README rõ ràng và chính xác
- Tuân theo mẫu mã tồn tại trong kho
- Giữ sự nhất quán với các bài học khác

## Ghi Chú Thêm

### Những Sự Cố Thường Gặp

1. **Phiên bản Python không phù hợp:**
   - Đảm bảo dùng Python 3.12+
   - Một số gói không hoạt động trên phiên bản cũ hơn
   - Dùng `python3 -m venv` để chỉ định rõ phiên bản Python

2. **Biến môi trường:**
   - Luôn tạo `.env` từ `.env.example`
   - Không commit file `.env` (đã nằm trong `.gitignore`)
   - Token GitHub cần có quyền thích hợp

3. **Xung đột gói:**
   - Dùng môi trường ảo mới hoàn toàn
   - Cài đặt từ `requirements.txt` thay vì từng gói riêng lẻ
   - Một số notebook cần thêm gói ghi trong các ô markdown

4. **Dịch vụ Azure:**
   - Dịch vụ AI Azure yêu cầu tài khoản đăng ký còn hiệu lực
   - Một số tính năng phụ thuộc vùng miền
   - Hạn chế cấp miễn phí áp dụng cho GitHub Models

### Lộ Trình Học

Khuyến nghị theo trình tự bài học:
1. **00-course-setup** - Bắt đầu với thiết lập môi trường
2. **01-intro-to-ai-agents** - Hiểu nền tảng đại lý AI
3. **02-explore-agentic-frameworks** - Tìm hiểu các khung làm việc khác nhau
4. **03-agentic-design-patterns** - Các mẫu thiết kế cốt lõi
5. Tiếp tục các bài học theo số thứ tự

### Lựa Chọn Khung Làm Việc

Chọn khung làm việc dựa trên mục tiêu:
- **Tất cả bài học**: Microsoft Agent Framework (MAF) với `AzureAIProjectAgentProvider`
- **Đại lý đăng ký phía máy chủ** trong Azure AI Foundry Agent Service V2 và hiển thị trong cổng Foundry

### Hỗ Trợ

- Tham gia [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Xem file README bài học để biết hướng dẫn cụ thể
- Xem [README.md](./README.md) chính cho tổng quan khóa học
- Tham khảo [Course Setup](./00-course-setup/README.md) cho hướng dẫn chi tiết

### Đóng Góp

Đây là dự án giáo dục mở. Hoan nghênh đóng góp:
- Cải thiện ví dụ mã
- Sửa lỗi chính tả hoặc lỗi
- Thêm chú thích làm rõ
- Đề xuất chủ đề bài học mới
- Dịch sang các ngôn ngữ khác

Xem [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) để biết các nhu cầu hiện tại.

## Bối Cảnh Dự Án Riêng

### Hỗ Trợ Đa Ngôn Ngữ

Kho lưu trữ này sử dụng hệ thống dịch tự động:
- Hỗ trợ hơn 50 ngôn ngữ
- Bản dịch trong thư mục `/translations/<mã-ngôn-ngữ>/`
- Quy trình GitHub Actions xử lý cập nhật dịch
- Các tệp nguồn bằng tiếng Anh ở thư mục gốc kho

### Cấu Trúc Bài Học

Mỗi bài học theo mẫu dưới đây:
1. Hình thu nhỏ video có liên kết
2. Nội dung bài học viết (README.md)
3. Mẫu mã trong nhiều khung làm việc
4. Mục tiêu học tập và yêu cầu trước
5. Tài nguyên học tập thêm liên kết

### Đặt Tên Mẫu Mã

Định dạng: `<số-bài>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Bài 1, MAF Python
- `14-sequential.ipynb` - Bài 14, MAF mẫu nâng cao

### Thư Mục Đặc Biệt

- `translated_images/` - Hình ảnh được bản địa hoá cho các bản dịch
- `images/` - Hình ảnh gốc cho nội dung tiếng Anh
- `.devcontainer/` - Cấu hình container phát triển VS Code
- `.github/` - Quy trình GitHub Actions và mẫu

### Phụ Thuộc

Các gói chính từ `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Hỗ trợ giao thức Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Dịch vụ AI Azure
- `azure-identity` - Xác thực Azure (AzureCliCredential)
- `azure-search-documents` - Tích hợp Azure AI Search
- `mcp[cli]` - Hỗ trợ Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->