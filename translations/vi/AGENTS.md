# AGENTS.md

## Tổng Quan Dự Án

Kho lưu trữ này chứa "Tác nhân AI cho Người Mới Bắt Đầu" - một khóa học giáo dục toàn diện dạy mọi thứ cần thiết để xây dựng Tác nhân AI. Khóa học gồm 18 bài học (đánh số 00-18) bao gồm các kiến thức cơ bản, mẫu thiết kế, khung làm việc, triển khai sản xuất, tác nhân tại chỗ/trên thiết bị, và bảo mật cho tác nhân AI.

**Công nghệ chính:**
- Python 3.12+
- Jupyter Notebooks cho học tương tác
- Khung AI: Microsoft Agent Framework (MAF)
- Dịch vụ AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Kiến trúc:**
- Cấu trúc dựa trên bài học (thư mục 00-15+)
- Mỗi bài học bao gồm: tài liệu README, mẫu mã (Jupyter notebooks), và hình ảnh
- Hỗ trợ đa ngôn ngữ qua hệ thống dịch tự động
- Một notebook Python cho mỗi bài học dùng Microsoft Agent Framework

## Lệnh Cài Đặt

### Yêu Cầu Trước
- Python 3.12 trở lên
- Tài khoản Azure đăng ký (cho Microsoft Foundry)
- Cài đặt và đăng nhập Azure CLI (`az login`)

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

Cho **Microsoft Foundry** (Bắt buộc):
- `AZURE_AI_PROJECT_ENDPOINT` - điểm cuối dự án Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - tên triển khai mô hình (ví dụ: gpt-5-mini)

Cho **Azure AI Search** (Bài 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - điểm cuối Azure AI Search
- `AZURE_SEARCH_API_KEY` - khóa API Azure AI Search

Xác thực: Chạy `az login` trước khi chạy notebooks (sử dụng `AzureCliCredential`).

## Quy Trình Phát Triển

### Chạy Jupyter Notebooks

Mỗi bài học chứa nhiều Jupyter notebooks cho các khung làm việc khác nhau:

1. **Khởi động Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Đi đến thư mục bài học** (ví dụ, `01-intro-to-ai-agents/code_samples/`)

3. **Mở và chạy các notebook:**
   - `*-python-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Sử dụng Microsoft Agent Framework (.NET)

### Làm việc với Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Yêu cầu tài khoản Azure đăng ký
- Dùng `FoundryChatClient` cho Agent Service V2 (tác nhân hiện trên portal Foundry)
- Sẵn sàng sản xuất với tính năng giám sát tích hợp
- Mẫu tệp: `*-python-agent-framework.ipynb`

## Hướng Dẫn Kiểm Thử

Đây là kho lưu trữ giáo dục với mã ví dụ thay vì mã sản xuất có kiểm thử tự động. Để xác minh thiết lập và thay đổi:

### Kiểm Thử Thủ Công

1. **Kiểm thử môi trường Python:**
   ```bash
   python --version  # Nên là 3.12 trở lên
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Kiểm thử thực thi notebook:**
   ```bash
   # Chuyển đổi sổ tay thành tập lệnh và chạy (kiểm tra các thư viện nhập)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Xác minh biến môi trường:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Chạy Các Notebook Riêng Lẻ

Mở notebook trong Jupyter và thực thi các ô theo thứ tự. Mỗi notebook đều tự chứa và bao gồm:
- Các câu lệnh import
- Tải cấu hình
- Ví dụ thực hiện tác nhân
- Kết quả kỳ vọng trong các ô markdown

### Kiểm Tra Đơn Giản Cho Tác Nhân Được Triển Khai

Với các bài học có tác nhân được triển khai làm tác nhân được lưu trữ bởi Microsoft Foundry (01, 04, 05, 16), repo cung cấp catalog kiểm tra đơn giản ở thư mục `tests/` được chạy bởi workflow `.github/workflows/smoke-test.yml` qua hành động [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Đây là bước kiểm thử nhẹ sau triển khai (tác nhân có thể truy cập và tuân thủ yêu cầu cơ bản không?), bổ sung cho pipeline đánh giá trong Bài 10 và 16. Xem [tests/README.md](./tests/README.md) để xem bảng ánh xạ catalog-bài học-tác nhân. Bài 17 chạy cục bộ với Foundry Local và không có điểm cuối lưu trữ, nên được kiểm tra bằng cách chạy trực tiếp notebook của nó.

## Phong Cách Mã Nguồn

### Quy Ước Python

- **Phiên bản Python**: 3.12+
- **Phong cách mã nguồn**: Tuân theo chuẩn PEP 8 Python
- **Notebooks**: Sử dụng ô markdown rõ ràng để giải thích khái niệm
- **Nhập liệu**: Nhóm theo thư viện chuẩn, bên thứ ba, nhập liệu địa phương

### Quy Ước Jupyter Notebook

- Bao gồm ô markdown mô tả trước ô mã
- Thêm ví dụ đầu ra trong notebooks để tham khảo
- Sử dụng tên biến rõ ràng phù hợp với khái niệm bài học
- Giữ thứ tự chạy notebook theo trình tự tuyến tính (ô 1 → 2 → 3...)

### Tổ Chức Tệp

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

### Xây dựng tài liệu

Kho lưu trữ dùng Markdown cho tài liệu:
- Các tệp README.md trong mỗi thư mục bài học
- README.md chính ở thư mục gốc kho lưu trữ
- Hệ thống dịch tự động qua GitHub Actions

### Pipeline CI/CD

Nằm trong `.github/workflows/`:

1. **co-op-translator.yml** - Dịch tự động sang hơn 50 ngôn ngữ
2. **welcome-issue.yml** - Chào mừng người tạo issue mới
3. **welcome-pr.yml** - Chào mừng người đóng góp pull request mới

### Triển khai

Đây là kho lưu trữ giáo dục - không có quy trình triển khai. Người dùng:
1. Fork hoặc sao chép kho lưu trữ
2. Chạy notebooks cục bộ hoặc trong GitHub Codespaces
3. Học bằng cách sửa đổi và thử nghiệm ví dụ

## Hướng Dẫn Pull Request

### Trước Khi Gửi

1. **Kiểm tra thay đổi của bạn:**
   - Chạy hoàn chỉnh các notebook bị ảnh hưởng
   - Đảm bảo tất cả các ô chạy không lỗi
   - Kiểm tra đầu ra phù hợp

2. **Cập nhật tài liệu:**
   - Cập nhật README.md nếu thêm khái niệm mới
   - Thêm chú thích trong notebook cho mã phức tạp
   - Đảm bảo ô markdown giải thích mục đích

3. **Thay đổi tệp:**
   - Tránh commit tệp `.env` (dùng `.env.example`)
   - Không commit thư mục `venv/` hay `__pycache__/`
   - Giữ đầu ra notebook khi thể hiện khái niệm
   - Xóa tệp tạm thời và notebooks sao lưu (`*-backup.ipynb`)

### Định Dạng Tiêu Đề PR

Dùng tiêu đề mô tả:
- `[Lesson-XX] Thêm ví dụ mới cho <khái niệm>`
- `[Fix] Sửa lỗi chính tả trong README bài học-XX`
- `[Update] Cải thiện mẫu mã trong bài học-XX`
- `[Docs] Cập nhật hướng dẫn cài đặt`

### Kiểm Tra Bắt Buộc

- Notebooks phải chạy không lỗi
- Tệp README phải rõ ràng và chính xác
- Tuân theo mẫu mã hiện có trong kho lưu trữ
- Duy trì sự nhất quán với các bài học khác

## Ghi Chú Bổ Sung

### Các Lỗi Thường Gặp

1. **Sai phiên bản Python:**
   - Đảm bảo sử dụng Python 3.12+
   - Một số gói có thể không hoạt động với phiên bản cũ
   - Dùng `python3 -m venv` để chỉ rõ phiên bản Python

2. **Biến môi trường:**
   - Luôn tạo `.env` từ `.env.example`
   - Không commit tệp `.env` (nằm trong `.gitignore`)
   - Đăng nhập bằng `az login` để xác thực Entra ID không cần khóa

3. **Xung đột gói:**
   - Dùng môi trường ảo mới
   - Cài đặt từ `requirements.txt` thay vì từng gói riêng lẻ
   - Một số notebook có thể yêu cầu thêm gói được đề cập trong ô markdown

4. **Dịch vụ Azure:**
   - Dịch vụ AI Azure yêu cầu đăng ký hoạt động
   - Một số tính năng chỉ có ở vùng cụ thể
   - Đảm bảo triển khai mô hình Azure OpenAI của bạn hỗ trợ API Responses

### Lộ Trình Học Tập

Khuyến nghị tiến trình qua các bài học:
1. **00-course-setup** - Bắt đầu với thiết lập môi trường
2. **01-intro-to-ai-agents** - Hiểu cơ bản về tác nhân AI
3. **02-explore-agentic-frameworks** - Tìm hiểu về các khung khác nhau
4. **03-agentic-design-patterns** - Mẫu thiết kế cốt lõi
5. Tiếp tục lần lượt qua các bài đánh số

### Lựa Chọn Khung Làm Việc

Chọn khung dựa vào mục tiêu của bạn:
- **Tất cả các bài học**: Microsoft Agent Framework (MAF) với `FoundryChatClient`
- **Tác nhân đăng ký phía máy chủ** trong Microsoft Foundry Agent Service V2 và hiển thị trên portal Foundry

### Nhận Trợ Giúp

- Tham gia [Cộng đồng Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)
- Xem tệp README của bài học để có hướng dẫn cụ thể
- Kiểm tra [README.md](./README.md) chính để xem tổng quan khóa học
- Tham khảo [Course Setup](./00-course-setup/README.md) để biết hướng dẫn thiết lập chi tiết

### Đóng Góp

Đây là dự án giáo dục mở. Hoan nghênh đóng góp:
- Cải thiện ví dụ mã
- Sửa lỗi chính tả hoặc lỗi
- Thêm chú thích làm rõ
- Đề nghị chủ đề bài học mới
- Dịch sang các ngôn ngữ khác

Xem các [Vấn đề trên GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) để biết nhu cầu hiện tại.

## Bối Cảnh Riêng Dự Án

### Hỗ Trợ Đa Ngôn Ngữ

Kho lưu trữ này sử dụng hệ thống dịch tự động:
- Hỗ trợ hơn 50 ngôn ngữ
- Dịch nằm ở thư mục `/translations/<mã-ngôn-ngữ>/`
- Workflow GitHub Actions xử lý cập nhật dịch
- Các tệp gốc bằng tiếng Anh ở thư mục gốc kho lưu trữ

### Cấu Trúc Bài Học

Mỗi bài học theo một mẫu nhất quán:
1. Ảnh thu nhỏ video có liên kết
2. Nội dung bài học viết (README.md)
3. Mẫu mã trong nhiều khung làm việc
4. Mục tiêu học tập và yêu cầu trước
5. Liên kết tài nguyên học tập thêm

### Đặt Tên Mẫu Mã

Định dạng: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Bài 1, MAF Python
- `14-sequential.ipynb` - Bài 14, mẫu nâng cao MAF
- `16-python-agent-framework.ipynb` - Bài 16, tác nhân hỗ trợ khách hàng sản xuất
- `17-local-agent-foundry-local.ipynb` - Bài 17, tác nhân cục bộ với Foundry Local + Qwen

### Thư Mục Đặc Biệt

- `translated_images/` - Hình ảnh bản địa hóa cho dịch
- `images/` - Hình ảnh gốc cho nội dung tiếng Anh
- `.devcontainer/` - cấu hình container phát triển VS Code
- `.github/` - workflows và mẫu GitHub Actions

### Phụ Thuộc

Gói chính từ `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Hỗ trợ giao thức Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Dịch vụ AI Azure
- `azure-identity` - Xác thực Azure (AzureCliCredential)
- `azure-search-documents` - Tích hợp Azure AI Search
- `mcp[cli]` - Hỗ trợ Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->