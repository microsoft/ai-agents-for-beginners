# Khắc phục sự cố, Bảng rủi ro & Những lưu ý quan trọng

## Khắc phục sự cố mã 400

| Lỗi | Sửa lỗi |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Định nghĩa công cụ sử dụng định dạng lồng nhau cũ của Chat Completions | Phẳng hóa từ `{"type": "function", "function": {"name": ...}}` sang `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters nằm ở cấp trên cùng |
| `unknown_parameter: input[N].tool_calls` | Kết quả công cụ đa lượt dùng định dạng cũ của Chat Completions | Thay thế `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` thành các mục `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Công cụ bật `strict: true` thiếu mảng `required` | Khi `strict: true`, tất cả thuộc tính phải được liệt kê trong `required` và phải đặt `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Công cụ bật `strict: true` thiếu `additionalProperties: false` | Thêm `"additionalProperties": false` vào đối tượng tham số |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID function_call của few-shot có tiền tố sai | ID cuộc gọi hàm phải bắt đầu bằng `fc_` (ví dụ `fc_example1`), không phải `call_` |
| `missing_required_parameter: text.format.name` | Thêm khóa `"name"` vào dict format (ví dụ `"name": "Output"`) |
| `invalid_type: text.format` | Đảm bảo `text.format` là dict với các khóa `type`, `name`, `strict`, `schema` — không phải chuỗi |
| `invalid input content type` | Dùng các loại nội dung `input_text`/`output_text` thay vì `text` của Chat |
| `invalid input content type` (hình ảnh) | Nội dung hình ảnh vẫn dùng `"type": "image_url"` | Chuyển sang `"type": "input_image"` |
| `Expected object, got string` trên `image_url` | `image_url` vẫn là đối tượng lồng `{"url": "..."}` | Phẳng thành chuỗi thuần: `"image_url": "https://..."` hoặc `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` đối với `max_output_tokens` | Giá trị tối thiểu là **16** trên Azure OpenAI. Dùng 50+ cho thử nghiệm, 1000+ cho sản xuất. |
| `429 Too Many Requests` khi streaming | Bị giới hạn tần suất. Bao quanh luồng với `try/except`, gửi lỗi JSON ra frontend, triển khai backoff/thử lại. |
| `KeyError: 'innererror'` khi lỗi bộ lọc nội dung | Cấu trúc lỗi bộ lọc nội dung đã thay đổi trong Responses API | Chat Completions dùng `error.body["innererror"]["content_filter_result"]`; Responses API dùng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, trong mảng). Viết lại toàn bộ truy cập `innererror`. |

---

## Bảng rủi ro khi di chuyển

| Triệu chứng | Sai sót có khả năng | Cách khắc phục |
|---------|---------------|-----|
| `output_text` trống / phản hồi bị cắt | `max_output_tokens` quá thấp với các mô hình suy luận | Đặt `max_output_tokens=1000` hoặc cao hơn — các token suy luận tính vào giới hạn |
| `400 invalid_type: text.format` | Truyền chuỗi `response_format` thay vì dict `text.format` | Dùng `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` trên `/openai/v1/responses` | Sai `base_url` — thiếu hậu tố `/openai/v1/` | Đảm bảo `base_url=f"{endpoint}/openai/v1/"` (có dấu gạch chéo cuối) |
| `401 Unauthorized` sau khi chuyển sang `OpenAI()` | `api_key` chưa thiết lập hoặc token provider không truyền đúng | Với EntraID: `api_key=token_provider` (callable). Với khoá API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mô hình trả về `deployment not found` | Tham số `model` không khớp tên triển khai Azure của bạn | Dùng `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — đây là tên triển khai, không phải tên mô hình |
| `json.loads(resp.output_text)` gây `JSONDecodeError` | Schema không được áp dụng hoặc mô hình không hỗ trợ JSON nghiêm ngặt | Đảm bảo `"strict": True` trong schema, đồng thời kiểm tra mô hình hỗ trợ output cấu trúc |
| Streaming không trả về sự kiện `delta` | Kiểm tra sai loại sự kiện | Lọc theo `event.type == "response.output_text.delta"`, không phải Chat `chat.completion.chunk` |
| Lỗi `400` với đầu vào hình ảnh sau khi di chuyển | Loại nội dung hình ảnh chưa cập nhật | Thay `"type": "image_url"` → `"type": "input_image"` và phẳng `"image_url": {"url": "..."}` → `"image_url": "..."` (chuỗi thuần) |
| Vòng lặp gọi công cụ vô tận | Thiếu kết quả công cụ trong `input` theo sau | Sau khi gọi công cụ, thêm mục `{"type": "function_call_output", "call_id": ..., "output": ...}` vào `input` trong yêu cầu tiếp theo |
| Lỗi `temperature` với GPT-5 hoặc dòng o-series | Giá trị `temperature` rõ ràng khác 1 | Bỏ `temperature` hoặc đặt về `1` cho các mô hình GPT-5 và dòng o-series (o1, o3-mini, o3, o4-mini) |
| Lỗi `top_p` với dòng o-series | `top_p` không được hỗ trợ | Bỏ `top_p` khi dùng các mô hình dòng o-series |
| Không nhận diện được `max_completion_tokens` | Dùng tham số riêng của Azure | Thay `max_completion_tokens` bằng `max_output_tokens`. Đặt 4096+ cho dòng o-series (token suy luận tính vào giới hạn). |
| Output trống hoặc bị cắt từ dòng o-series | `max_output_tokens` quá thấp | O-series dùng token suy luận nội bộ. Đặt `max_output_tokens=4096` hoặc cao hơn — không phải 500-1000. |
| `400 integer_below_min_value` với `max_output_tokens` | Giá trị dưới 16 | Azure OpenAI bắt buộc `max_output_tokens >= 16`. Dùng 50+ cho kiểm thử nhanh, 1000+ cho sản xuất. |
| `429 Too Many Requests` giữa luồng | Bị giới hạn tần suất bởi Azure OpenAI | Luồng bị gián đoạn im lặng khi không có xử lý lỗi. Luôn bao quanh `async for event in await coroutine:` với `try/except` và gửi `{"error": str(e)}` ra frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Sai tenant hoặc chưa đăng nhập | Truyền `tenant_id=os.getenv("AZURE_TENANT_ID")` rõ ràng. Chạy `azd auth login --tenant <tenant-id>` tại máy. |
| `404 Not Found` khi dùng GitHub Models (`models.github.ai`) | GitHub Models không hỗ trợ Responses API | Loại bỏ hoàn toàn đường dẫn GitHub Models trong code. Dùng Azure OpenAI, OpenAI, hoặc endpoint cục bộ tương thích (ví dụ Ollama hỗ trợ Responses). |
| MAF `OpenAIChatCompletionClient` vẫn dùng Chat Completions | Dùng client MAF cũ trong 1.0.0+ | Trong MAF 1.0.0+, `OpenAIChatClient` mặc định dùng Responses API. Thay `OpenAIChatCompletionClient` bằng `OpenAIChatClient`. Với phiên bản trước 1.0.0, nâng cấp lên `agent-framework-openai>=1.0.0`. |
| Agent LangChain trả về trống hoặc lỗi với gọi công cụ | `ChatOpenAI` không dùng Responses API | Thêm `use_responses_api=True` vào `ChatOpenAI(...)`. Đồng thời đổi `.content` → `.text` trên các tin nhắn phản hồi. |
| `KeyError: 'innererror'` trong trình xử lý lỗi bộ lọc nội dung | Cấu trúc lỗi thay đổi trong Responses API | Viết lại `error.body["innererror"]["content_filter_result"]["jailbreak"]` thành `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` không còn; chi tiết bộ lọc trong mảng `content_filters` cấp cao với `content_filter_results` (số nhiều) bên trong mỗi phần tử. |
| Gọi HTTP thô tới `/openai/deployments/.../chat/completions` trả về 404 | Endpoint REST Chat Completions cũ | Viết lại URL thành `/openai/v1/responses`. Thay đổi thân yêu cầu: `messages` → `input`, thêm `max_output_tokens` + `store: false`, loại bỏ tham số truy vấn `api-version`. Thay đổi cách phân tích phản hồi: `choices[0].message.content` → `output[0].content[0].text` (lưu ý: `output_text` là thuộc tính hỗ trợ SDK, không có trong JSON REST thô). |

---

## Những lưu ý quan trọng

1. Nếu trước đây bạn đã dùng Chat Completions để quản lý trạng thái hội thoại, thì giờ bạn phải tự quản lý trạng thái rõ ràng với Responses.
2. Ưu tiên dùng `max_output_tokens` thay cho `max_tokens` cũ.
3. Khi di chuyển sang `gpt-5`, đảm bảo không chỉ định `temperature` hoặc phải đặt thành `1`.
4. Thay thế Chat `content[].type: "text"` bằng Responses `content[].type: "input_text"` cho đầu vào của người dùng/hệ thống.
5. Với `text.format`, cung cấp một dict đúng chuẩn (ví dụ `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), không dùng chuỗi thuần.
6. Tham số `seed` không được hỗ trợ trong Responses; loại bỏ nó khỏi yêu cầu.
7. **Suy luận**: Chỉ bao gồm `reasoning` nếu mã gốc đã sử dụng. Không thêm `reasoning` cho các cuộc gọi API trước đây không có — nhiều mô hình không suy luận không hỗ trợ tham số này.
8. **Kích thước `max_output_tokens`**: Với các mô hình suy luận (GPT-5-mini, GPT-5, dòng o-series), đặt `max_output_tokens=4096` hoặc cao hơn — không phải 50–1000. Mô hình dùng token suy luận nội bộ trước khi tạo output hiển thị; giới hạn quá thấp khiến phản hồi bị cắt hoặc trống.
9. **`max_completion_tokens` dòng o-series**: Nếu mã gốc dùng `max_completion_tokens` (tham số riêng của Azure cho dòng o-series), hãy thay bằng `max_output_tokens`. Responses API không chấp nhận `max_completion_tokens`.
10. **`reasoning_effort` dòng o-series**: Nếu mã gốc dùng `reasoning_effort` (low/medium/high), di chuyển thành `reasoning={"effort": "<giá trị>"}` trong cuộc gọi Responses API.
11. **Độ trễ streaming dòng o-series**: Các mô hình o-series thực hiện suy luận nội bộ trước khi sinh output. Khi streaming, dự kiến có độ trễ dài hơn trước sự kiện đầu tiên `response.output_text.delta`. Đây là bình thường — mô hình đang suy luận, không bị treo.
9. **`_azure_ad_token_provider` đã biến mất**: `AsyncOpenAI` / `OpenAI` không còn thuộc tính `_azure_ad_token_provider`. Các test hoặc code truy cập thuộc tính này sẽ lỗi `AttributeError`. Token provider được truyền qua `api_key` và không thể kiểm tra trên đối tượng client.
10. **Tệp giám sát (snapshot) / tệp mẫu**: Nếu bộ test dùng snapshot testing, **tất cả** tệp snapshot chứa dạng streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, vv) phải cập nhật về dạng mới của Responses. Việc này dễ bị bỏ sót gây lỗi so sánh snapshot.
11. **Đường dẫn monkeypatch mô phỏng**: Mục tiêu monkeypatch thay đổi từ `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (hoặc `Responses.create` cho đồng bộ). Dùng đường dẫn cũ sẽ không làm gì — mock không được chặn, test gọi API thật hoặc thất bại.
12. **Dùng `input` thay vì `messages`**: Các hàm mock phải đọc `kwargs.get("input")` thay vì `kwargs.get("messages")`. Responses API dùng `input` để chứa lịch sử hội thoại.
13. **Đặt tên biến môi trường**: Azure Identity SDK dùng `AZURE_CLIENT_ID` (không phải `AZURE_OPENAI_CLIENT_ID`) cho `ManagedIdentityCredential(client_id=...)`. Đổi tên trong test, tệp `.env`, cài đặt app và Bicep/hạ tầng.
14. **`max_output_tokens` tối thiểu là 16**: Azure OpenAI từ chối giá trị dưới 16 với lỗi `400 integer_below_min_value`. Dùng `50` cho thử nghiệm nhanh, 1000+ cho sản xuất. `max_tokens` cũ không có giới hạn này.
15. **`tenant_id` cho `AzureDeveloperCliCredential`**: Khi tài nguyên Azure OpenAI thuộc tenant khác, bạn **phải** truyền `tenant_id` rõ ràng — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Nếu không, credential sẽ dùng tenant sai và trả `401`.
16. **Giới hạn tốc độ hiện ra khác trong streaming**: Với Chat Completions, lỗi 429 thường ngăn luồng khởi động. Với streaming Responses API, 429 có thể xảy ra **giữa luồng** — async iterator ném ngoại lệ. Luôn bao quanh vòng lặp streaming bằng `try/except` và gửi một dòng JSON lỗi để frontend xử lý khéo léo.

17. **Xử lý lỗi trong streaming là bắt buộc đối với các ứng dụng web**: Mẫu `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` rất quan trọng. Nếu không có nó, luồng SSE/JSONL sẽ âm thầm ngừng khi có bất kỳ lỗi máy chủ nào xảy ra và frontend sẽ bị treo.
18. **Định nghĩa công cụ phải sử dụng định dạng phẳng**: API Responses yêu cầu `{"type": "function", "name": ..., "parameters": ...}` — không phải định dạng lồng nhau của Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Đây là lỗi phổ biến nhất khi di chuyển mã gọi hàm.
19. **`pydantic_function_tool()` không tương thích**: Hàm trợ giúp `openai.pydantic_function_tool()` vẫn tạo định dạng lồng nhau cũ. Không sử dụng nó với `responses.create()`. Hãy định nghĩa các schema công cụ bằng tay hoặc làm phẳng đầu ra.
20. **Kết quả công cụ sử dụng `function_call_output`, không phải `role: tool`**: Sau khi thực thi công cụ, hãy thêm `{"type": "function_call_output", "call_id": ..., "output": ...}` — không phải `{"role": "tool", "tool_call_id": ..., "content": ...}`. Đối với yêu cầu công cụ của trợ lý, dùng `messages.extend(response.output)` — không dùng dict thủ công `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` yêu cầu `required` + `additionalProperties: false`**: Khi dùng `strict: true` trên một công cụ, mọi thuộc tính phải được liệt kê trong mảng `required` và `additionalProperties` phải đặt là `false`. Thiếu một trong hai sẽ gây lỗi 400.
22. **ID gọi hàm có các tiền tố cụ thể**: Khi cung cấp mục `function_call` vài ví dụ trong `input`, trường `id` phải bắt đầu với `fc_` và trường `call_id` phải bắt đầu với `call_` (ví dụ: `"id": "fc_example1", "call_id": "call_example1"`). Việc dùng tiền tố `call_` cũ của Chat Completions làm `id` sẽ bị từ chối.
23. **GitHub Models không hỗ trợ Responses API**: Nếu ứng dụng có đường dẫn mã GitHub Models (`base_url` trỏ đến `models.github.ai` hoặc `models.inference.ai.azure.com`), hãy loại bỏ hoàn toàn. Không có con đường di chuyển — hãy chuyển sang Azure OpenAI, OpenAI hoặc một endpoint cục bộ tương thích.
24. **Cấu trúc thân lỗi bộ lọc nội dung đã thay đổi**: Lỗi Chat Completions dùng `error.body["innererror"]["content_filter_result"]` (số ít). Lỗi Responses API dùng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, nằm trong mảng). Khóa `innererror` không còn tồn tại. Mã truy cập trực tiếp `innererror` sẽ gây lỗi `KeyError` khi chạy — điều này dễ bị bỏ sót khi di chuyển vì chỉ xuất hiện khi bộ lọc nội dung thực sự kích hoạt. Luôn tìm kiếm `innererror` khi di chuyển.
25. **Các cuộc gọi HTTP raw cần phải sửa URL + thân yêu cầu**: Ứng dụng gọi trực tiếp Azure OpenAI REST (qua `requests`, `httpx`, `aiohttp`) với `/openai/deployments/{name}/chat/completions?api-version=...` phải chuyển sang `/openai/v1/responses`. Thân yêu cầu dùng `input` thay vì `messages`, yêu cầu `max_output_tokens` và `store`, và bỏ tham số truy vấn `api-version`. Phần văn bản thân phản hồi ở `output[0].content[0].text` — **không phải** `output_text`, đây là thuộc tính tiện dụng của SDK không có trong JSON REST thô.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->