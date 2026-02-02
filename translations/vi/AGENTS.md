# AGENTS.md

## Tổng quan dự án

Kho lưu trữ này chứa "AI Agents for Beginners" - một khóa học giáo dục toàn diện hướng dẫn mọi thứ cần thiết để xây dựng AI Agents. Khóa học bao gồm hơn 15 bài học về các nguyên tắc cơ bản, mẫu thiết kế, khung làm việc và triển khai sản phẩm của các AI Agents.

**Công nghệ chính:**
- Python 3.12+
- Jupyter Notebooks để học tương tác
- Các khung AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Dịch vụ Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (có sẵn gói miễn phí)

**Kiến trúc:**
- Cấu trúc dựa trên bài học (các thư mục từ 00-15+)
- Mỗi bài học bao gồm: tài liệu README, mẫu mã (Jupyter notebooks), và hình ảnh
- Hỗ trợ đa ngôn ngữ thông qua hệ thống dịch tự động
- Nhiều tùy chọn khung làm việc cho mỗi bài học (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Lệnh thiết lập

### Yêu cầu trước
- Python 3.12 hoặc cao hơn
- Tài khoản GitHub (cho GitHub Models - gói miễn phí)
- Đăng ký Azure (tùy chọn, cho các dịch vụ Azure AI)

### Thiết lập ban đầu

1. **Clone hoặc fork kho lưu trữ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tạo và kích hoạt môi trường ảo Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Cài đặt các phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Thiết lập biến môi trường:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Biến môi trường cần thiết

Đối với **GitHub Models (Miễn phí)**:
- `GITHUB_TOKEN` - Mã truy cập cá nhân từ GitHub

Đối với **Dịch vụ Azure AI** (tùy chọn):
- `PROJECT_ENDPOINT` - Điểm cuối dự án Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Khóa API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL điểm cuối Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Tên triển khai cho mô hình chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Tên triển khai cho embeddings
- Cấu hình Azure bổ sung như được hiển thị trong `.env.example`

## Quy trình phát triển

### Chạy Jupyter Notebooks

Mỗi bài học chứa nhiều Jupyter notebooks cho các khung làm việc khác nhau:

1. **Khởi động Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Đi đến thư mục bài học** (ví dụ: `01-intro-to-ai-agents/code_samples/`)

3. **Mở và chạy notebooks:**
   - `*-semantic-kernel.ipynb` - Sử dụng khung Semantic Kernel
   - `*-autogen.ipynb` - Sử dụng khung AutoGen
   - `*-python-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Sử dụng Azure AI Agent Service

### Làm việc với các khung làm việc khác nhau

**Semantic Kernel + GitHub Models:**
- Có sẵn gói miễn phí với tài khoản GitHub
- Tốt cho việc học và thử nghiệm
- Mẫu tệp: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Có sẵn gói miễn phí với tài khoản GitHub
- Khả năng điều phối nhiều agent
- Mẫu tệp: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Khung làm việc mới nhất từ Microsoft
- Có sẵn trong Python và .NET
- Mẫu tệp: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Yêu cầu đăng ký Azure
- Các tính năng sẵn sàng cho sản xuất
- Mẫu tệp: `*-azureaiagent.ipynb`

## Hướng dẫn kiểm tra

Đây là kho lưu trữ giáo dục với mã ví dụ thay vì mã sản xuất có kiểm tra tự động. Để xác minh thiết lập và thay đổi của bạn:

### Kiểm tra thủ công

1. **Kiểm tra môi trường Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Kiểm tra thực thi notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Xác minh biến môi trường:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Chạy từng notebook riêng lẻ

Mở notebooks trong Jupyter và thực thi các ô theo thứ tự. Mỗi notebook là tự chứa và bao gồm:
- Các câu lệnh import
- Tải cấu hình
- Các triển khai agent ví dụ
- Kết quả mong đợi trong các ô markdown

## Phong cách mã

### Quy ước Python

- **Phiên bản Python**: 3.12+
- **Phong cách mã**: Tuân theo quy ước Python PEP 8 tiêu chuẩn
- **Notebooks**: Sử dụng các ô markdown rõ ràng để giải thích khái niệm
- **Imports**: Nhóm theo thư viện tiêu chuẩn, bên thứ ba, và imports cục bộ

### Quy ước Jupyter Notebook

- Bao gồm các ô markdown mô tả trước các ô mã
- Thêm ví dụ kết quả trong notebooks để tham khảo
- Sử dụng tên biến rõ ràng phù hợp với khái niệm bài học
- Giữ thứ tự thực thi notebook tuyến tính (ô 1 → 2 → 3...)

### Tổ chức tệp

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Xây dựng và triển khai

### Xây dựng tài liệu

Kho lưu trữ này sử dụng Markdown cho tài liệu:
- Các tệp README.md trong mỗi thư mục bài học
- README.md chính tại gốc kho lưu trữ
- Hệ thống dịch tự động thông qua GitHub Actions

### Pipeline CI/CD

Nằm trong `.github/workflows/`:

1. **co-op-translator.yml** - Dịch tự động sang hơn 50 ngôn ngữ
2. **welcome-issue.yml** - Chào mừng người tạo vấn đề mới
3. **welcome-pr.yml** - Chào mừng người đóng góp pull request mới

### Triển khai

Đây là kho lưu trữ giáo dục - không có quy trình triển khai. Người dùng:
1. Fork hoặc clone kho lưu trữ
2. Chạy notebooks cục bộ hoặc trong GitHub Codespaces
3. Học bằng cách sửa đổi và thử nghiệm với các ví dụ

## Hướng dẫn Pull Request

### Trước khi gửi

1. **Kiểm tra thay đổi của bạn:**
   - Chạy hoàn toàn các notebooks bị ảnh hưởng
   - Xác minh tất cả các ô thực thi không có lỗi
   - Kiểm tra rằng kết quả là phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật README.md nếu thêm khái niệm mới
   - Thêm nhận xét trong notebooks cho mã phức tạp
   - Đảm bảo các ô markdown giải thích mục đích

3. **Thay đổi tệp:**
   - Tránh commit các tệp `.env` (sử dụng `.env.example`)
   - Không commit các thư mục `venv/` hoặc `__pycache__/`
   - Giữ kết quả notebook khi chúng minh họa khái niệm
   - Xóa các tệp tạm thời và notebooks sao lưu (`*-backup.ipynb`)

### Định dạng tiêu đề PR

Sử dụng tiêu đề mô tả:
- `[Lesson-XX] Thêm ví dụ mới cho <khái niệm>`
- `[Fix] Sửa lỗi chính tả trong README bài học XX`
- `[Update] Cải thiện mẫu mã trong bài học XX`
- `[Docs] Cập nhật hướng dẫn thiết lập`

### Kiểm tra bắt buộc

- Notebooks phải thực thi không có lỗi
- Các tệp README phải rõ ràng và chính xác
- Tuân theo mẫu mã hiện có trong kho lưu trữ
- Duy trì sự nhất quán với các bài học khác

## Ghi chú bổ sung

### Những điều thường gặp

1. **Không khớp phiên bản Python:**
   - Đảm bảo sử dụng Python 3.12+
   - Một số gói có thể không hoạt động với phiên bản cũ hơn
   - Sử dụng `python3 -m venv` để chỉ định phiên bản Python rõ ràng

2. **Biến môi trường:**
   - Luôn tạo `.env` từ `.env.example`
   - Không commit tệp `.env` (nó nằm trong `.gitignore`)
   - Token GitHub cần quyền phù hợp

3. **Xung đột gói:**
   - Sử dụng môi trường ảo mới
   - Cài đặt từ `requirements.txt` thay vì các gói riêng lẻ
   - Một số notebooks có thể yêu cầu các gói bổ sung được đề cập trong các ô markdown của chúng

4. **Dịch vụ Azure:**
   - Dịch vụ Azure AI yêu cầu đăng ký hoạt động
   - Một số tính năng chỉ dành cho khu vực cụ thể
   - Các giới hạn gói miễn phí áp dụng cho GitHub Models

### Lộ trình học tập

Tiến trình được khuyến nghị qua các bài học:
1. **00-course-setup** - Bắt đầu từ đây để thiết lập môi trường
2. **01-intro-to-ai-agents** - Hiểu các nguyên tắc cơ bản của AI agent
3. **02-explore-agentic-frameworks** - Tìm hiểu về các khung làm việc khác nhau
4. **03-agentic-design-patterns** - Các mẫu thiết kế cốt lõi
5. Tiếp tục qua các bài học được đánh số theo thứ tự

### Lựa chọn khung làm việc

Chọn khung làm việc dựa trên mục tiêu của bạn:
- **Học tập/Thử nghiệm**: Semantic Kernel + GitHub Models (miễn phí)
- **Hệ thống nhiều agent**: AutoGen
- **Tính năng mới nhất**: Microsoft Agent Framework (MAF)
- **Triển khai sản xuất**: Azure AI Agent Service

### Nhận trợ giúp

- Tham gia [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Xem các tệp README bài học để được hướng dẫn cụ thể
- Kiểm tra [README.md chính](./README.md) để có tổng quan khóa học
- Tham khảo [Course Setup](./00-course-setup/README.md) để biết hướng dẫn thiết lập chi tiết

### Đóng góp

Đây là một dự án giáo dục mở. Hoan nghênh đóng góp:
- Cải thiện ví dụ mã
- Sửa lỗi chính tả hoặc sai sót
- Thêm nhận xét làm rõ
- Đề xuất chủ đề bài học mới
- Dịch sang các ngôn ngữ bổ sung

Xem [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) để biết các nhu cầu hiện tại.

## Ngữ cảnh cụ thể của dự án

### Hỗ trợ đa ngôn ngữ

Kho lưu trữ này sử dụng hệ thống dịch tự động:
- Hỗ trợ hơn 50 ngôn ngữ
- Các bản dịch trong thư mục `/translations/<lang-code>/`
- Workflow GitHub Actions xử lý cập nhật dịch
- Các tệp nguồn bằng tiếng Anh tại gốc kho lưu trữ

### Cấu trúc bài học

Mỗi bài học tuân theo một mẫu nhất quán:
1. Hình thu nhỏ video với liên kết
2. Nội dung bài học viết (README.md)
3. Mẫu mã trong nhiều khung làm việc
4. Mục tiêu học tập và yêu cầu trước
5. Tài nguyên học tập bổ sung được liên kết

### Đặt tên mẫu mã

Định dạng: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Bài học 4, Semantic Kernel
- `07-autogen.ipynb` - Bài học 7, AutoGen
- `14-python-agent-framework.ipynb` - Bài học 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Bài học 14, MAF .NET

### Thư mục đặc biệt

- `translated_images/` - Hình ảnh được bản địa hóa cho các bản dịch
- `images/` - Hình ảnh gốc cho nội dung tiếng Anh
- `.devcontainer/` - Cấu hình container phát triển VS Code
- `.github/` - Workflow và mẫu GitHub Actions

### Phụ thuộc

Các gói chính từ `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Khung AutoGen
- `semantic-kernel` - Khung Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Dịch vụ Azure AI
- `azure-search-documents` - Tích hợp tìm kiếm Azure AI
- `chromadb` - Cơ sở dữ liệu vector cho các ví dụ RAG
- `chainlit` - Khung giao diện chat
- `browser_use` - Tự động hóa trình duyệt cho các agent
- `mcp[cli]` - Hỗ trợ Model Context Protocol
- `mem0ai` - Quản lý bộ nhớ cho các agent

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.