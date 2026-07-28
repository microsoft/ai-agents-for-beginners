---
name: testing-course-samples
---
# Kiểm thử Các Mẫu Khóa Học

Xác thực rằng các sổ tay bài học và mẫu mã chạy trên một thiết lập Microsoft Foundry / Azure OpenAI trực tiếp.
Kho lưu trữ cung cấp một trình chạy tại
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) để
thực thi mỗi sổ tay Python một cách không đầu cuối và in ra bảng PASS/FAIL.

## Khi nào sử dụng
- "Xác thực tất cả các sổ tay / mẫu mã với đăng ký Azure của tôi."
- "Kiểm tra nhanh khóa học sau khi nâng cấp gói hoặc thay đổi mô hình."
- "Bài học nào vẫn còn chạy / thất bại trực tiếp?"

Không **dùng** cho AI Smoke Test GitHub Action (xác thực các tác nhân đã *triển khai* —
xem [`tests/README.md`](../../../tests/README.md)). Kỹ năng này
chạy các sổ tay cục bộ.

## Yêu cầu đầu vào (kiểm tra trước)
1. **Python 3.12+** với các lệ thuộc của khóa học: `python -m pip install -r requirements.txt`
   cùng trình thực thi: `python -m pip install nbconvert ipykernel`.
2. **`.env` ở thư mục gốc repo** (sao chép từ [`.env.example`](../../../../../.env.example)) với ít nhất:
   - `AZURE_AI_PROJECT_ENDPOINT` — điểm cuối dự án Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — một triển khai không bị khấu hao (ví dụ `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) và `AZURE_OPENAI_DEPLOYMENT`
     cho các bài học gọi trực tiếp Azure OpenAI (Bài 06, 02-azure-openai, 14 handoff/human-loop).
3. Hoàn thành **`az login`** — mẫu mã xác thực với `AzureCliCredential` (Entra ID, không cần khóa).
4. Xác minh triển khai mô hình tồn tại:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Thực thi xác thực
```powershell
# Tất cả các sổ tay Python (bỏ qua .NET, .venv, site-packages, bản dịch, tài sản kỹ năng)
pwsh scripts/validate-notebooks.ps1

# Một bài học đơn, với thời gian chờ mỗi ô dài hơn
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Chỉ liệt kê những gì sẽ chạy (không thực thi)
pwsh scripts/validate-notebooks.ps1 -List

# Trình thông dịch rõ ràng (nếu `python` không có trong PATH, ví dụ bí danh Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Tập lệnh ghi các bản sao đã thực thi, nhật ký theo sổ tay, và `results.json` vào
`$env:TEMP\aiab-nbval` và thoát với số lỗi thất bại.

Thất bại tạm thời (giới hạn tốc độ HTTP 429 trên đăng ký chia sẻ, một sự cố
`AzureCliCredential` hiếm hoi, hoặc hết thời gian chờ) được thử lại tự động
(`-Retries`, mặc định 2, cùng độ trễ lặp lại `-RetryDelaySeconds`, mặc định 20). Nếu
một triển khai mô hình thường xuyên bị 429, kiểm tra hạn mức TPM GlobalStandard của đăng ký
(`az cognitiveservices usage list -l <region>`) — tăng công suất một
triển khai không giúp khi *đăng ký* đã hết hạn mức.

## Diễn giải kết quả
- `PASS` — sổ tay chạy trọn vẹn không lỗi cell.
- `FAIL` — hiển thị dòng `*Error` / `*Exception` đầu tiên; mở
  `log_*.txt` tương ứng trong thư mục đầu ra để xem dấu vết lỗi đầy đủ.
- Thất bại của một sổ tay được giới hạn bởi `-Timeout` (cho mỗi cell), nên một cell
  có tương tác người không phản hồi sẽ hiện thành `StdinNotImplementedError` thay vì bị treo.

## Bài học cần tài nguyên bổ sung (dự kiến sẽ thất bại nếu thiếu)
| Bài học | Yêu cầu bổ sung |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — có đường dự phòng trong bộ nhớ |
| 11 MCP / GitHub | Máy chủ MCP GitHub + PAT |
| 13 memory (cognee) | `cognee` được cấu hình với nhà cung cấp mô hình |
| 15 browser-use | Trình duyệt Playwright được cài (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Môi trường chạy Foundry Local + mô hình Qwen tải về (trên thiết bị, không đám mây) |
| Sổ tay `*-dotnet-*` | Kernel .NET Interactive (mặc định loại trừ; dùng `-IncludeDotnet`) |

## Báo cáo lại
Tóm tắt thành bảng PASS/FAIL nhóm theo bài học. Tách biệt các suy giảm thực tế
(lỗi mã/cấu hình cần sửa) với các thiếu hụt môi trường (thiếu Search/Foundry Local/PAT),
và dẫn chứng `log_*.txt` của mỗi lỗi thực sự.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->