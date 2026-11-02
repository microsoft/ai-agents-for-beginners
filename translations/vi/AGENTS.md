# AGENTS.md

## Tổng quan dự án

Kho lưu trữ này chứa "Các tác nhân AI cho người mới bắt đầu" - một khóa học giáo dục toàn diện dạy mọi thứ cần thiết để xây dựng các tác nhân AI. Khóa học gồm 18 bài học (đánh số 00-18) bao gồm các kiến thức cơ bản, mẫu thiết kế, framework, triển khai sản xuất, tác nhân cục bộ/trên thiết bị, và bảo mật của các tác nhân AI.

**Công nghệ chính:**
- Python 3.12+
- Jupyter Notebooks cho học tương tác
- Framework AI: Microsoft Agent Framework (MAF)
- Dịch vụ AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Kiến trúc:**
- Cấu trúc dựa trên bài học (thư mục 00-18)
- Mỗi bài học chứa: tài liệu README, mẫu code (Jupyter notebooks), và hình ảnh
- Hỗ trợ đa ngôn ngữ qua hệ thống dịch tự động
- Một notebook Python mỗi bài học sử dụng Microsoft Agent Framework

## Lệnh thiết lập

### Yêu cầu trước
- Python 3.12 trở lên
- Đăng ký Azure (cho Microsoft Foundry)
- Đã cài đặt và xác thực Azure CLI (`az login`)

### Thiết lập ban đầu

1. **Sao chép hoặc fork kho lưu trữ:**
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

Đối với **Microsoft Foundry** (Bắt buộc):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint dự án Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Tên triển khai mô hình (ví dụ: gpt-5-mini)

Đối với **Azure AI Search** (Bài 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Khóa API Azure AI Search

Xác thực: Chạy `az login` trước khi chạy các notebook (sử dụng `AzureCliCredential`).

## Quy trình phát triển

### Chạy Jupyter Notebooks

Mỗi bài học chứa nhiều notebook Jupyter cho các framework khác nhau:

1. **Khởi động Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Đi đến thư mục bài học** (ví dụ: `01-intro-to-ai-agents/code_samples/`)

3. **Mở và chạy các notebook:**
   - `*-python-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (.NET)

### Làm việc với Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Cần đăng ký Azure
- Sử dụng `FoundryChatClient` cho Agent Service V2 (tác nhân hiển thị trong cổng Foundry)
- Sẵn sàng sản xuất với khả năng giám sát tích hợp
- Mẫu file: `*-python-agent-framework.ipynb`

## Hướng dẫn kiểm thử

Đây là kho lưu trữ giáo dục với ví dụ code thay vì code sản xuất có kiểm thử tự động. Để kiểm tra thiết lập và thay đổi của bạn:

### Kiểm thử thủ công

1. **Kiểm tra môi trường Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Kiểm tra chạy notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Xác minh biến môi trường:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Chạy từng notebook riêng lẻ

Mở notebook trong Jupyter và thực thi các ô theo thứ tự. Mỗi notebook tự chứa và bao gồm:
- Câu lệnh import
- Tải cấu hình
- Triển khai ví dụ tác nhân
- Kết quả kỳ vọng trong các ô markdown

### Kiểm thử nhanh các tác nhân đã triển khai

Đối với các bài học có tác nhân được triển khai dưới dạng tác nhân lưu trữ Microsoft Foundry (01, 04, 05, 16), repo cung cấp catalog kiểm thử nhanh dưới `tests/` được chạy bởi quy trình `.github/workflows/smoke-test.yml` qua action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Đây là bước kiểm tra nhẹ sau triển khai (tác nhân có truy cập được và tuân theo các kỳ vọng nhắc nhở cơ bản không?), bổ sung cho pipeline đánh giá trong Bài 10 và 16. Xem [tests/README.md](./tests/README.md) để biết sơ đồ liên kết catalog-bài học-tác nhân. Bài 17 chạy cục bộ với Foundry Local và không có endpoint lưu trữ, nên được xác nhận bằng cách chạy trực tiếp notebook.

## Style code

### Quy ước Python

- **Phiên bản Python**: 3.12+
- **Phong cách code**: Tuân theo chuẩn PEP 8 của Python
- **Notebook**: Dùng các ô markdown rõ ràng để giải thích khái niệm
- **Imports**: Nhóm theo thư viện chuẩn, thư viện bên ngoài, import cục bộ

### Quy ước Jupyter Notebook

- Bao gồm các ô markdown mô tả trước các ô code
- Thêm ví dụ kết quả trong notebook để tham khảo
- Dùng tên biến rõ ràng phù hợp khái niệm bài học
- Giữ thứ tự chạy notebook tuyến tính (ô 1 → 2 → 3...)

### Tổ chức file

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Xây dựng và Triển khai

### Xây dựng tài liệu

Kho lưu trữ này sử dụng Markdown cho tài liệu:
- Các file README.md trong mỗi thư mục bài học
- README.md chính ở thư mục gốc
- Hệ thống dịch tự động qua GitHub Actions

### Pipeline CI/CD

Nằm trong `.github/workflows/`:

1. **co-op-translator.yml** - Dịch tự động sang hơn 50 ngôn ngữ
2. **welcome-issue.yml** - Chào mừng người tạo issue mới
3. **welcome-pr.yml** - Chào mừng người đóng góp pull request mới

### Triển khai

Đây là kho lưu trữ giáo dục - không có quy trình triển khai. Người dùng:
1. Fork hoặc sao chép kho lưu trữ
2. Chạy notebook cục bộ hoặc trong GitHub Codespaces
3. Học bằng cách chỉnh sửa và thử nghiệm với các ví dụ

## Hướng dẫn Pull Request

### Trước khi gửi

1. **Kiểm tra các thay đổi của bạn:**
   - Chạy hoàn chỉnh các notebook bị ảnh hưởng
   - Xác nhận tất cả các ô không bị lỗi khi thực thi
   - Kiểm tra kết quả xuất ra phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật README.md nếu thêm khái niệm mới
   - Thêm chú thích trong notebook cho mã phức tạp
   - Đảm bảo các ô markdown giải thích mục đích

3. **Thay đổi file:**
   - Tránh commit file `.env` (sử dụng `.env.example`)
   - Không commit thư mục `venv/` hoặc `__pycache__/`
   - Giữ kết quả notebook khi nó minh họa khái niệm
   - Xóa file tạm thời và notebook backup (`*-backup.ipynb`)

### Định dạng tiêu đề PR

Dùng tiêu đề mô tả:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Các kiểm tra bắt buộc

- Notebook phải chạy không lỗi
- Các file README phải rõ ràng và chính xác
- Tuân theo mẫu code hiện có trong repo
- Duy trì sự nhất quán với các bài học khác

## Ghi chú thêm

### Những lưu ý phổ biến

1. **Không phù hợp phiên bản Python:**
   - Đảm bảo sử dụng Python 3.12+
   - Một số gói có thể không hoạt động với phiên bản cũ hơn
   - Dùng `python3 -m venv` để chỉ định rõ phiên bản Python

2. **Biến môi trường:**
   - Luôn tạo `.env` từ `.env.example`
   - Không commit file `.env` (nó nằm trong `.gitignore`)
   - Đăng nhập bằng `az login` cho xác thực Entra ID không cần khóa

3. **Xung đột gói:**
   - Dùng môi trường ảo mới
   - Cài đặt từ `requirements.txt` thay vì từng gói riêng lẻ
   - Một số notebook cần gói bổ sung được ghi trong ô markdown

4. **Dịch vụ Azure:**
   - Dịch vụ AI Azure yêu cầu đăng ký còn hiệu lực
   - Một số tính năng giới hạn theo khu vực
   - Đảm bảo triển khai mô hình Azure OpenAI hỗ trợ API Phản hồi

### Lộ trình học tập

Khuyến nghị học theo thứ tự bài học:
1. **00-course-setup** - Bắt đầu tại đây để thiết lập môi trường
2. **01-intro-to-ai-agents** - Hiểu các kiến thức cơ bản về tác nhân AI
3. **02-explore-agentic-frameworks** - Tìm hiểu các framework khác nhau
4. **03-agentic-design-patterns** - Các mẫu thiết kế cốt lõi
5. Tiếp tục theo thứ tự số bài học

### Lựa chọn Framework

Chọn framework dựa trên mục tiêu của bạn:
- **Tất cả các bài học**: Microsoft Agent Framework (MAF) với `FoundryChatClient`
- **Tác nhân đăng ký phía server** trong Microsoft Foundry Agent Service V2 và hiển thị trong cổng Foundry

### Nhận hỗ trợ

- Tham gia [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Xem các file README từng bài để hướng dẫn cụ thể
- Xem [README.md chính](./README.md) để tổng quan khóa học
- Tham khảo [Course Setup](./00-course-setup/README.md) cho hướng dẫn thiết lập chi tiết

### Đóng góp

Đây là dự án giáo dục mở. Hoan nghênh đóng góp:
- Cải thiện ví dụ code
- Sửa lỗi đánh máy hoặc lỗi cú pháp
- Thêm chú thích làm rõ
- Đề xuất chủ đề bài học mới
- Dịch sang các ngôn ngữ khác

Xem [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) để biết nhu cầu hiện tại.

## Ngữ cảnh dự án cụ thể

### Hỗ trợ đa ngôn ngữ

Kho này sử dụng hệ thống dịch tự động:
- Hỗ trợ hơn 50 ngôn ngữ
- Bản dịch trong các thư mục `/translations/<lang-code>/`
- Quy trình GitHub Actions xử lý cập nhật dịch
- File nguồn bằng tiếng Anh ở thư mục gốc repo

### Cấu trúc bài học

Mỗi bài học theo mẫu nhất quán:
1. Ảnh thu nhỏ video có link
2. Nội dung bài học viết (README.md)
3. Mẫu code trong nhiều framework
4. Mục tiêu học tập và yêu cầu trước
5. Tài nguyên học bổ sung liên kết

### Đặt tên mẫu code

Định dạng: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Bài 1, MAF Python
- `14-sequential.ipynb` - Bài 14, mẫu MAF nâng cao
- `16-python-agent-framework.ipynb` - Bài 16, tác nhân hỗ trợ khách hàng sản xuất
- `17-local-agent-foundry-local.ipynb` - Bài 17, tác nhân cục bộ với Foundry Local + Qwen

### Thư mục đặc biệt

- `translated_images/` - Hình ảnh bản địa hóa cho bản dịch
- `images/` - Hình ảnh gốc cho nội dung tiếng Anh
- `.devcontainer/` - Cấu hình container phát triển VS Code
- `.github/` - Workflow và mẫu GitHub Actions

### Phụ thuộc

Các gói chính từ `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Hỗ trợ giao thức Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Dịch vụ Azure AI
- `azure-identity` - Xác thực Azure (AzureCliCredential)
- `azure-search-documents` - Tích hợp Azure AI Search
- `mcp[cli]` - Hỗ trợ Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->