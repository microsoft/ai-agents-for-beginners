# Cấu trúc Notebook

Các notebook Jupyter là các tài liệu JSON có cấu trúc cấp cao như sau:

- `nbformat` và `nbformat_minor`
- `metadata`
- `cells` (một danh sách các ô markdown và ô code)

Khi chỉnh sửa các tệp `.ipynb` bằng chương trình:

- Giữ nguyên `nbformat` và `nbformat_minor` từ mẫu.
- Giữ `cells` như một danh sách có thứ tự; không sắp xếp lại trừ khi có chủ ý.
- Đối với ô code, đặt `execution_count` thành `null` khi không rõ.
- Đối với ô code, đặt `outputs` thành một danh sách rỗng khi đang khởi tạo.
- Đối với ô markdown, giữ `cell_type="markdown"` và `metadata={}`.

Ưu tiên khởi tạo từ các mẫu được đóng gói hoặc `new_notebook.py` (ví dụ, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) thay vì tự viết JSON notebook thô bằng tay.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo tính chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn có thẩm quyền. Đối với những thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->