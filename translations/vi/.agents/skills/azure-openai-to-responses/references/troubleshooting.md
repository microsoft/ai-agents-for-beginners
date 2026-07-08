# Khắc Phục Sự Cố, Bảng Rủi Ro & Lưu Ý Quan Trọng

## Khắc Phục Sự Cố 400s

| Lỗi | Sửa |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Định nghĩa công cụ dùng định dạng lồng Chat Completions cũ | Phẳng hóa từ `{"type": "function", "function": {"name": ...}}` thành `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters lên cấp cao nhất |
| `unknown_parameter: input[N].tool_calls` | Kết quả công cụ đa lượt dùng định dạng Chat Completions cũ | Thay `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` bằng các mục `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Công cụ `strict: true` thiếu mảng `required` | Khi `strict: true`, tất cả thuộc tính phải được liệt kê trong `required` và `additionalProperties: false` phải được đặt |
| `invalid_function_parameters: 'additionalProperties' is required` | Công cụ `strict: true` thiếu `additionalProperties: false` | Thêm `"additionalProperties": false` vào đối tượng parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID function_call vài shot có tiền tố sai | ID cuộc gọi function phải bắt đầu bằng `fc_` (ví dụ: `fc_example1`), không dùng `call_` |
| `missing_required_parameter: text.format.name` | Thêm khóa `"name"` vào dict format (ví dụ, `"name": "Output"`) |
| `invalid_type: text.format` | Đảm bảo `text.format` là dict có khóa `type`, `name`, `strict`, `schema` — không phải là chuỗi |
| `invalid input content type` | Dùng loại nội dung `input_text`/`output_text` thay cho Chat `text` |
| `invalid input content type` (image) | Nội dung ảnh vẫn dùng `"type": "image_url"` | Đổi thành `"type": "input_image"` |
| `Expected object, got string` trên `image_url` | `image_url` vẫn là đối tượng lồng `{"url": "..."}` | Phẳng hóa thành chuỗi: `"image_url": "https://..."` hoặc `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` cho `max_output_tokens` | Tối thiểu là **16** trên Azure OpenAI. Dùng 50+ cho test, 1000+ cho sản xuất. |
| `429 Too Many Requests` khi streaming | Bị giới hạn tần suất. Đóng gói streaming trong `try/except`, trả về JSON lỗi cho giao diện người dùng, triển khai backoff/thử lại. |
| `KeyError: 'innererror'` trên lỗi bộ lọc nội dung | Cấu trúc lỗi bộ lọc nội dung thay đổi trong Responses API | Chat Completions dùng `error.body["innererror"]["content_filter_result"]`; Responses API dùng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, trong mảng). Viết lại tất cả truy cập `innererror`. |

---

## Bảng Rủi Ro Khi Di Cư

| Triệu chứng | Sai Lầm Có Thể | Sửa |
|---------|---------------|-----|
| `output_text` rỗng / phản hồi bị cắt ngắn | `max_output_tokens` quá thấp cho mô hình suy luận | Đặt `max_output_tokens=1000` hoặc cao hơn — token suy luận tính vào giới hạn |
| `400 invalid_type: text.format` | Truyền chuỗi `response_format` thay vì dict `text.format` | Dùng `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` trên `/openai/v1/responses` | `base_url` sai — thiếu hậu tố `/openai/v1/` | Đảm bảo `base_url=f"{endpoint}/openai/v1/"` (có dấu gạch chéo cuối) |
| `401 Unauthorized` sau khi chuyển sang `OpenAI()` | `api_key` không được đặt hoặc nhà cung cấp token không truyền đúng | Với EntraID: `api_key=token_provider` (hàm callable). Với API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mô hình trả về `deployment not found` | Tham số `model` không khớp tên triển khai Azure của bạn | Dùng `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — đây là tên triển khai, không phải tên mô hình |
| `json.loads(resp.output_text)` gây `JSONDecodeError` | Schema không được ép buộc hoặc mô hình không hỗ trợ JSON nghiêm ngặt | Đảm bảo `"strict": True` trong schema, kiểm tra mô hình hỗ trợ đầu ra cấu trúc |
| Streaming không tạo sự kiện `delta` nào | Kiểm tra sai loại sự kiện | Lọc theo `event.type == "response.output_text.delta"`, không phải `chat.completion.chunk` của Chat |
| Lỗi `400` trên ảnh đầu vào sau di cư | Loại nội dung ảnh chưa cập nhật | Đổi `"type": "image_url"` → `"type": "input_image"` và phẳng `"image_url": {"url": "..."}` → `"image_url": "..."` (chuỗi đơn thuần) |
| Vòng lặp gọi công cụ vô hạn | Thiếu kết quả công cụ trong `input` theo dõi | Sau khi dùng công cụ, thêm mục `{"type": "function_call_output", "call_id": ..., "output": ...}` vào `input` trong yêu cầu tiếp theo |
| Lỗi `temperature` với GPT-5 hoặc loạt o-series | Giá trị `temperature` rõ ràng khác 1 | Loại bỏ `temperature` hoặc đặt `1` cho GPT-5 và o-series (o1, o3-mini, o3, o4-mini) |
| Lỗi `top_p` với loạt o-series | `top_p` không được hỗ trợ | Loại bỏ `top_p` khi dùng mô hình loạt o-series |
| `max_completion_tokens` không được nhận diện | Dùng tham số đặc thù Azure | Thay `max_completion_tokens` bằng `max_output_tokens`. Đặt 4096+ cho o-series (token suy luận tính vào giới hạn). |
| Đầu ra rỗng/bị cắt từ o-series | `max_output_tokens` quá thấp | O-series dùng token suy luận nội bộ. Đặt `max_output_tokens=4096` hoặc cao hơn — không phải 500–1000. |
| Lỗi `400 integer_below_min_value` cho `max_output_tokens` | Giá trị dưới 16 | Azure OpenAI yêu cầu `max_output_tokens >= 16`. Dùng 50+ cho test nhanh, 1000+ cho sản xuất. |
| `429 Too Many Requests` giữa chừng stream | Bị giới hạn bởi Azure OpenAI | Stream tắt im lặng khi không xử lý lỗi. Luôn đóng gói `async for event in await coroutine:` trong `try/except` và trả về `{"error": str(e)}` cho frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant sai hoặc chưa đăng nhập | Truyền rõ `tenant_id=os.getenv("AZURE_TENANT_ID")`. Chạy `azd auth login --tenant <tenant-id>` cục bộ. |
| `404 Not Found` dùng GitHub Models (`models.github.ai`) | GitHub Models không hỗ trợ Responses API | Xóa hoàn toàn đường dẫn code GitHub Models. Dùng Azure OpenAI, OpenAI, hoặc endpoint địa phương tương thích (ví dụ, Ollama với hỗ trợ Responses). |
| MAF `OpenAIChatCompletionClient` vẫn dùng Chat Completions | Dùng client MAF kế thừa trong 1.0.0+ | Trong MAF 1.0.0+, `OpenAIChatClient` mặc định dùng Responses API. Thay `OpenAIChatCompletionClient` bằng `OpenAIChatClient`. Nếu dưới 1.0.0, nâng cấp `agent-framework-openai>=1.0.0`. |
| Agent LangChain trả về rỗng hoặc lỗi khi gọi công cụ | `ChatOpenAI` không dùng Responses API | Thêm `use_responses_api=True` vào `ChatOpenAI(...)`. Cũng đổi `.content` thành `.text` trên các message phản hồi. |
| `KeyError: 'innererror'` trong bộ xử lý lỗi bộ lọc nội dung | Cấu trúc lỗi thay đổi trong Responses API | Viết lại `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Bao `innererror` bị loại bỏ; chi tiết bộ lọc nội dung hiện ở mảng cấp trên `content_filters` với `content_filter_results` (số nhiều) bên trong mỗi mục. |
| Gọi HTTP thô tới `/openai/deployments/.../chat/completions` trả về 404 | Endpoint REST Chat Completions cũ | Đổi URL thành `/openai/v1/responses`. Thay nội dung yêu cầu: `messages` → `input`, thêm `max_output_tokens` + `store: false`, bỏ tham số truy vấn `api-version`. Thay phân tích phản hồi: `choices[0].message.content` → `output[0].content[0].text` (lưu ý: `output_text` là thuộc tính tiện lợi của SDK, không có trong JSON REST thô). |

---

## Lưu Ý Quan Trọng

1. Nếu trước đây bạn dùng Chat Completions để quản lý trạng thái hội thoại, hãy quản lý trạng thái riêng của bạn rõ ràng với Responses.
2. Ưu tiên dùng `max_output_tokens` thay vì `max_tokens` kế thừa.
3. Khi di cư sang `gpt-5`, đảm bảo không chỉ định `temperature` hoặc đặt bằng `1`.
4. Thay thế Chat `content[].type: "text"` bằng Responses `content[].type: "input_text"` cho đầu vào người dùng/hệ thống.
5. Với `text.format`, cung cấp dict đúng chuẩn (ví dụ, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), không phải chuỗi đơn thuần.
6. Tham số `seed` không được Responses hỗ trợ; loại bỏ nó khỏi yêu cầu.
7. **Suy luận**: Chỉ bao gồm `reasoning` nếu code gốc đã dùng. Không thêm `reasoning` vào các cuộc gọi API chưa có — nhiều mô hình (ví dụ, gpt-4o-mini) không hỗ trợ tham số này.
8. **Kích thước `max_output_tokens`**: Với mô hình suy luận (GPT-5-mini, GPT-5, o-series), dùng `max_output_tokens=4096` hoặc cao hơn — không dùng 50–1000. Mô hình sử dụng token suy luận nội bộ trước khi tạo đầu ra hiển thị; giới hạn quá thấp gây cắt hoặc rỗng khi phản hồi.
9. **`max_completion_tokens` của loạt O-series**: Nếu code gốc dùng `max_completion_tokens` (đặc thù Azure cho o-series), thay bằng `max_output_tokens`. Responses API không nhận `max_completion_tokens`.
10. **`reasoning_effort` của O-series**: Nếu code gốc dùng `reasoning_effort` (thấp/trung bình/cao), di cư thành `reasoning={"effort": "<value>"}` trong cuộc gọi Responses API.
11. **Độ trễ streaming của O-series**: Mô hình O-series thực hiện suy luận nội bộ trước khi tạo đầu ra. Khi streaming, dự kiến độ trễ dài hơn trước sự kiện `response.output_text.delta` đầu tiên. Đây là bình thường — mô hình đang suy luận chứ không bị treo.
9. **`_azure_ad_token_provider` không còn**: `AsyncOpenAI` / `OpenAI` không có thuộc tính `_azure_ad_token_provider`. Kiểm thử hoặc code truy cập thuộc tính này sẽ bị `AttributeError`. Nhà cung cấp token được truyền qua `api_key` và không thể xem trên đối tượng client.
10. **Snapshot / file golden**: Nếu bộ test dùng snapshot testing, **tất cả** file snapshot có hình dạng streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, v.v.) phải cập nhật sang cấu trúc Responses mới. Dễ bị bỏ sót gây lỗi so sánh snapshot.
11. **Đường dẫn mock monkeypatch**: Mục tiêu monkeypatch thay đổi từ `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (hoặc `Responses.create` với sync). Dùng đường dẫn cũ không gây lỗi nhưng mock sẽ không chặn, test sẽ gọi API thật hoặc fail.
12. **`input` chứ không phải `messages`**: Hàm mock phải đọc `kwargs.get("input")` chứ không phải `kwargs.get("messages")`. Responses API dùng `input` cho lịch sử hội thoại.
13. **Đặt tên biến môi trường**: Azure Identity SDK dùng `AZURE_CLIENT_ID` (không phải `AZURE_OPENAI_CLIENT_ID`) cho `ManagedIdentityCredential(client_id=...)`. Đổi tên ở test, `.env`, cài đặt ứng dụng, và Bicep/hạ tầng.
14. **Tối thiểu `max_output_tokens` là 16**: Azure OpenAI từ chối giá trị dưới 16 với lỗi `400 integer_below_min_value`. Dùng 50 cho test nhanh, 1000+ cho sản xuất. `max_tokens` cũ không giới hạn tối thiểu này.
15. **`tenant_id` cho `AzureDeveloperCliCredential`**: Khi tài nguyên Azure OpenAI thuộc tenant khác, bạn **phải** truyền `tenant_id` rõ ràng — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Thiếu bước này, credential dùng tenant sai và trả về `401`.
16. **Giới hạn tần suất khác biệt khi streaming**: Với Chat Completions, lỗi 429 thường ngăn stream bắt đầu. Với Responses API streaming, lỗi 429 có thể xảy ra **giữa stream** — bộ lặp async ném ngoại lệ. Luôn đóng gói vòng streaming trong `try/except` và trả về dòng JSON lỗi để giao diện xử lý mượt mà.

17. **Xử lý lỗi luồng phát trực tiếp là bắt buộc đối với các ứng dụng web**: Mẫu `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` rất quan trọng. Nếu không có mẫu này, luồng SSE/JSONL sẽ chết một cách lặng lẽ khi có lỗi phía máy chủ và frontend sẽ bị treo.
18. **Định nghĩa công cụ phải sử dụng định dạng phẳng**: Responses API mong đợi `{"type": "function", "name": ..., "parameters": ...}` — không phải định dạng lồng nhau Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Đây là lỗi di chuyển phổ biến nhất đối với mã gọi hàm.
19. **`pydantic_function_tool()` không tương thích**: Hàm trợ giúp `openai.pydantic_function_tool()` vẫn tạo định dạng lồng nhau cũ. Không sử dụng nó với `responses.create()`. Hãy định nghĩa schema công cụ thủ công hoặc làm phẳng đầu ra.
20. **Kết quả công cụ sử dụng `function_call_output`, không dùng `role: tool`**: Sau khi thực thi công cụ, thêm `{"type": "function_call_output", "call_id": ..., "output": ...}` — không phải `{"role": "tool", "tool_call_id": ..., "content": ...}`. Đối với yêu cầu công cụ của trợ lý, sử dụng `messages.extend(response.output)` — không phải dict thủ công `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` yêu cầu `required` + `additionalProperties: false`**: Khi sử dụng `strict: true` cho công cụ, mọi thuộc tính phải được liệt kê trong mảng `required` và `additionalProperties` phải là `false`. Thiếu một trong hai sẽ gây lỗi 400.
22. **ID cuộc gọi hàm có tiền tố cụ thể**: Khi cung cấp mục `function_call` dạng few-shot trong `input`, trường `id` phải bắt đầu bằng `fc_` và trường `call_id` phải bắt đầu bằng `call_` (ví dụ: `"id": "fc_example1", "call_id": "call_example1"`). Sử dụng tiền tố `call_` cũ của Chat Completions cho `id` sẽ bị từ chối.
23. **GitHub Models không hỗ trợ Responses API**: Nếu ứng dụng có đường dẫn mã GitHub Models (`base_url` trỏ đến `models.github.ai` hoặc `models.inference.ai.azure.com`), hãy loại bỏ hoàn toàn. Không có đường di chuyển — hãy chuyển sang Azure OpenAI, OpenAI hoặc endpoint cục bộ tương thích.
24. **Cấu trúc thân lỗi bộ lọc nội dung đã thay đổi**: Lỗi Chat Completions sử dụng `error.body["innererror"]["content_filter_result"]` (số ít). Lỗi Responses API sử dụng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, bên trong một mảng). Khóa `innererror` không còn tồn tại. Mã truy cập trực tiếp `innererror` sẽ gây `KeyError` khi chạy — điều này dễ bị bỏ sót khi di chuyển vì chỉ xuất hiện khi bộ lọc nội dung thực sự được kích hoạt. Luôn tìm kiếm `innererror` trong quá trình di chuyển.
25. **Các cuộc gọi HTTP thô cần viết lại URL + thân yêu cầu**: Các ứng dụng gọi Azure OpenAI REST trực tiếp (qua `requests`, `httpx`, `aiohttp`) sử dụng `/openai/deployments/{name}/chat/completions?api-version=...` phải chuyển sang `/openai/v1/responses`. Thân yêu cầu sử dụng `input` thay vì `messages`, yêu cầu `max_output_tokens` và `store`, và tham số truy vấn `api-version` bị loại bỏ. Văn bản trong thân phản hồi nằm ở `output[0].content[0].text` — **không phải** `output_text`, đây là thuộc tính tiện lợi của SDK không có trong REST JSON thô.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->