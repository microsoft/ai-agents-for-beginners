---
name: azure-openai-to-responses
license: MIT
---
# Di chuyển Ứng dụng Python từ Azure OpenAI Chat Completions sang Responses API

> **HƯỚNG DẪN CHÍNH THỐNG — TUÂN THỦ CHÍNH XÁC**
>
> Kỹ năng này di chuyển các codebase Python sử dụng Azure OpenAI Chat Completions
> sang API Responses thống nhất. Hãy làm theo hướng dẫn này một cách chính xác.
> Không tự ý gán ánh xạ tham số hoặc tạo ra các hình thức API mới.

---

## Các kích hoạt

Kích hoạt kỹ năng này khi người dùng muốn:
- Di chuyển ứng dụng Python từ Azure OpenAI Chat Completions sang Responses API
- Nâng cấp sử dụng SDK OpenAI Python lên hình dạng API mới nhất với Azure OpenAI
- Chuẩn bị code Python cho các mô hình GPT-5 hoặc mới hơn yêu cầu Responses trên Azure
- Chuyển từ `AzureOpenAI`/`AsyncAzureOpenAI` sang client chuẩn `OpenAI`/`AsyncOpenAI` với endpoint v1
- Sửa cảnh báo khấu hao liên quan đến constructors `AzureOpenAI` hoặc `api_version`

---

## ⚠️ Tương thích Mô hình — KIỂM TRA TRƯỚC

> **Trước khi di chuyển, xác minh việc triển khai Azure OpenAI của bạn hỗ trợ Responses API.**

### 1. Kiểm tra nhanh triển khai (nhanh nhất)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Lưu ý**: `max_output_tokens` có **giá trị tối thiểu là 16** trên Azure OpenAI. Giá trị dưới 16 sẽ trả lỗi 400. Dùng 50+ cho kiểm tra nhanh.

Nếu trả về 404, mô hình trong triển khai chưa hỗ trợ Responses — kiểm tra tham chiếu bên dưới hoặc triển khai lại với mô hình được hỗ trợ.

### 2. Kiểm tra các mô hình có sẵn trong vùng của bạn (khuyến nghị)

Chạy công cụ kiểm tra tương thích mô hình tích hợp để xem mô hình nào hỗ trợ Responses API trong vùng cụ thể của bạn:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Công cụ này truy vấn trực tiếp Azure ARM và hiển thị ma trận tương thích — mô hình nào hỗ trợ Responses, đầu ra cấu trúc, công cụ, v.v. Dùng `--filter gpt-5.1,gpt-5.2` để lọc kết quả hoặc `--json` cho scripting.

### 3. Tham chiếu hỗ trợ mô hình đầy đủ

- **Truy vấn trực tiếp**: `python migrate.py models` (xem trên — theo vùng, luôn cập nhật)
- **Duyệt khả dụng**: [Bảng tổng hợp mô hình và khả dụng vùng](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Khởi động nhanh & hướng dẫn**: **https://aka.ms/openai/start**

### ⚠️ Hạn chế mô hình cũ

> **CẢNH BÁO**: Các mô hình cũ (ví dụ `gpt-4o`, `gpt-4`) có thể không hỗ trợ đầy đủ tất cả tính năng Responses API.
>
> Hạn chế đã biết với mô hình cũ:
> - **tham số `reasoning`**: Không hỗ trợ trên `gpt-4o-mini`, `gpt-4o`, và nhiều mô hình không suy luận. Chỉ di chuyển `reasoning` nếu nó đã có trong code gốc.
> - **tham số `seed`**: Không được hỗ trợ trong Responses API — loại bỏ trong tất cả yêu cầu.
> - **Đầu ra có cấu trúc qua `text.format`**: Mô hình cũ có thể không kiểm soát nghiêm ngặt schema JSON với `strict: true`.
> - **Điều phối công cụ**: GPT-5+ điều phối gọi công cụ là một phần của suy luận nội bộ. Mô hình cũ dùng Responses vẫn hoạt động nhưng thiếu tích hợp sâu này.
> - **Giới hạn nhiệt độ**: Khi di chuyển sang `gpt-5`, nhiệt độ phải được bỏ hoặc đặt thành `1`. Mô hình cũ không có giới hạn này.

### Mô hình suy luận dòng O (o1, o3-mini, o3, o4-mini)

Mô hình dòng O có các giới hạn tham số riêng biệt. Khi di chuyển ứng dụng nhắm đến mô hình dòng o:

- **`temperature`**: Phải là `1` (hoặc bỏ). Mô hình dòng o không chấp nhận giá trị khác.
- **`max_completion_tokens` → `max_output_tokens`**: Ứng dụng dùng tham số Azure đặc thù `max_completion_tokens` phải chuyển sang `max_output_tokens`. Đặt giá trị lớn (4096+) vì token suy luận tính vào giới hạn.
- **`reasoning_effort`**: Nếu app dùng `reasoning_effort` (thấp/trung bình/cao), giữ lại — Responses API hỗ trợ tham số này cho mô hình dòng o.
- **Hành vi truyền phát**: Mô hình dòng o có thể bộ đệm đầu ra chờ suy luận xong mới phát sự kiện text delta. Streaming vẫn hoạt động, nhưng `response.output_text.delta` đầu tiên có thể đến muộn hơn so với mô hình GPT.
- **`top_p`**: Không hỗ trợ trên dòng o — bỏ nếu có.
- **Sử dụng công cụ**: Mô hình dòng o hỗ trợ công cụ qua Responses API giống như GPT, nhưng chất lượng điều phối gọi công cụ khác nhau tùy mô hình.

**Hành động — tư vấn mô hình chủ động**: Trong giai đoạn quét, kiểm tra mô hình app nhắm đến (tên triển khai, biến môi trường, cấu hình). Nếu mô hình là `gpt-4o` hoặc cũ hơn (không phải gpt-4.1+), chủ động thông báo cho người dùng:
- Việc di chuyển sẽ làm việc cho text cơ bản, chat, streaming, và công cụ với mô hình hiện tại.
- Mô hình mới hơn (`gpt-5.1`, `gpt-5.2`) có điều phối công cụ tốt hơn, kiểm soát đầu ra cấu trúc, suy luận, và có mặt liên vùng.
- Người dùng nên cân nhắc nâng cấp triển khai khi sẵn sàng — không phải điều kiện ngăn cản di chuyển.

Không chặn hoặc từ chối di chuyển dựa trên phiên bản mô hình. Tư vấn chỉ mang tính tham khảo.

### Mô hình GitHub không hỗ trợ Responses API

> **Mô hình GitHub (`models.github.ai`, `models.inference.ai.azure.com`) không hỗ trợ Responses API.**

Nếu codebase có đường code GitHub Models (tìm `base_url` trỏ đến `models.github.ai` hoặc `models.inference.ai.azure.com`), **xóa hoàn toàn** khi di chuyển. Responses API yêu cầu Azure OpenAI, OpenAI, hoặc endpoint local tương thích (ví dụ Ollama hỗ trợ Responses).

Hành động khi quét:
- Đánh dấu mọi đường code GitHub Models để xóa bỏ.

---

## Di chuyển Framework

Nhiều ứng dụng dùng các framework cao cấp trên OpenAI. Khi di chuyển, thay đổi là ở API của framework — không chỉ các lời gọi OpenAI bên dưới.

### Microsoft Agent Framework (MAF)

**Kiểm tra phiên bản MAF của bạn trước** — di chuyển khác nhau nếu bạn đang dùng MAF 1.0.0+ hay beta/rc trước 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **đã dùng Responses API** — không cần di chuyển. Nếu codebase dùng `OpenAIChatCompletionClient` cổ điển (dùng `chat.completions.create`), thay thế bằng `OpenAIChatClient`.

| Trước | Sau |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Để kiểm tra phiên bản: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF trước 1.0.0 (phát hành beta/rc)

Trong MAF trước 1.0.0, `OpenAIChatClient` dùng Chat Completions. Nâng cấp lên `agent-framework-openai>=1.0.0` để `OpenAIChatClient` mặc định dùng Responses API.

Không cần thay đổi gì khác — API `Agent` và công cụ vẫn giữ nguyên.

### LangChain (`langchain-openai`)

Thêm `use_responses_api=True` vào `ChatOpenAI()`. Cập nhật truy cập phản hồi từ `.content` sang `.text`.

| Trước | Sau |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Để xem ví dụ code đầy đủ trước/sau, xem [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hướng dẫn Di chuyển Frontend

> **Responses API là quan tâm phía server.** Di chuyển backend Python; hợp đồng HTTP frontend giữ nguyên trừ khi backend chỉ là lớp chuyển tiếp mỏng — trong trường hợp đó, cân nhắc dùng hình dạng yêu cầu Responses để loại bỏ lớp chuyển đổi. Nếu frontend gọi OpenAI trực tiếp với khóa client-side, hãy chuyển những gọi đó về backend trước.

### `@microsoft/ai-chat-protocol` lỗi thời

Gói npm `@microsoft/ai-chat-protocol` đã lỗi thời, nên thay bằng [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Nếu gặp trong frontend:

1. Thay thẻ script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Xóa khởi tạo `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Thay `client.getStreamedCompletion(messages)` bằng gọi `fetch()` thẳng tới endpoint streaming backend.
4. Thay `for await (const response of result)` bằng `for await (const chunk of readNDJSONStream(response.body))`.
5. Cập nhật truy cập thuộc tính từ `response.delta.content` / `response.error` thành `chunk.delta.content` / `chunk.error`.

---

## Mục tiêu

- Liệt kê tất cả call sites Python dùng Chat Completions hoặc Completions cổ với Azure OpenAI.
- Đề xuất kế hoạch và trình tự di chuyển codebase Python.
- Áp dụng chỉnh sửa an toàn, tối thiểu để chuyển sang Responses API.
- Cập nhật caller để dùng schema đầu ra của Responses; không có wrapper tương thích cũ.
- Chạy test/lint; sửa lỗi nhỏ phát sinh do di chuyển.
- Chuẩn bị các tập thay đổi nhỏ, dễ xem xét và cung cấp tóm tắt cuối với diff (không commit).

---

## Quy tắc

- Chỉ sửa file bên trong workspace git. Không ghi ngoài.
- Không giữ shims tương thích cũ; di chuyển code sang hình dạng API mới.
- Không để lại comment chuyển đổi hoặc backup file.
- Giữ nguyên ngữ nghĩa streaming nếu đã dùng trước đó; nếu không thì dùng không streaming.
- Hỏi phê duyệt trước khi chạy command hoặc gọi mạng nếu đang ở chế độ phê duyệt.
- Không chạy `git add`/`git commit`/`git push`; chỉ tạo chỉnh sửa trong working-tree.

---

## Bước 0: Di chuyển Client Azure OpenAI (Điều kiện tiên quyết)

Nếu codebase sử dụng constructors `AzureOpenAI` hoặc `AsyncAzureOpenAI`, di chuyển sang constructors chuẩn `OpenAI` / `AsyncOpenAI` trước. Constructors Azure đặc thù đã lỗi thời trong `openai>=1.108.1`.

### Tại sao dùng endpoint API v1?

Endpoint mới `/openai/v1` dùng client chuẩn `OpenAI()` thay vì `AzureOpenAI()`, không cần tham số `api_version`, và hoạt động giống nhau trên OpenAI và Azure OpenAI. Code client này là tương lai — không cần quản lý phiên bản.

### Thay đổi chính

| Trước | Sau |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Xóa hoàn toàn |

### Danh sách kiểm tra dọn dẹp

- Xóa tham số `api_version` khỏi khởi tạo client.
- Xóa biến môi trường `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` khỏi `.env`, cài đặt app, và file Bicep/infra.
- Đổi tên `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` trong `.env`, cài đặt app, Bicep/infra, và test fixtures (theo chuẩn SDK Azure Identity).
- Đảm bảo `openai>=1.108.1` trong `requirements.txt` hoặc `pyproject.toml`.

### Di chuyển biến môi trường

| Biến env cũ | Hành động | Ghi chú |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Xóa** | Không cần `api_version` với endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Xóa** | Như trên |
| `AZURE_OPENAI_CLIENT_ID` | **Đổi tên** → `AZURE_CLIENT_ID` | Chuẩn SDK Azure Identity cho `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Giữ** | Cần để xây dựng `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Giữ** | Dùng làm tham số `model` trong `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Giữ** | Dùng làm `api_key` cho xác thực khóa |

Ví dụ code thiết lập client (đồng bộ, bất đồng bộ, EntraID, khóa API, đa tenant), xem [cheat-sheet.md](./references/cheat-sheet.md).

---

## Bước 1: Phát hiện Call Sites Legacy

Chạy script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) để tìm tất cả call sites cần di chuyển:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Hoặc chạy các tìm kiếm thủ công — mỗi kết quả khớp là mục tiêu di chuyển:

```bash
# Các cuộc gọi API cũ (phải viết lại)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Các hàm tạo client Azure lỗi thời (phải thay thế)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Các mẫu truy cập cấu trúc phản hồi (phải cập nhật)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Định nghĩa công cụ theo định dạng lồng nhau cũ (phải làm phẳng)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Kết quả công cụ theo định dạng cũ (phải chuyển sang function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Tham số lỗi thời (phải loại bỏ hoặc đổi tên)
rg "response_format"
rg "max_tokens\b"        # đổi tên thành max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Biến môi trường lỗi thời (dọn dẹp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # nên là AZURE_CLIENT_ID

# Điểm cuối Mô hình GitHub (phải loại bỏ — API Phản hồi không được hỗ trợ)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Mẫu di sản cấp khung (phải cập nhật)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: thay bằng OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: cần use_responses_api=True

# Hạ tầng kiểm thử (phải cập nhật)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Truy cập thân lỗi bộ lọc nội dung (phải cập nhật — cấu trúc đã thay đổi)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # dạng số ít cũ — bây giờ là content_filter_results (số nhiều) trong mảng content_filters

# Cuộc gọi HTTP thô tới điểm cuối Chat Completions (phải cập nhật URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Phương pháp luận (phát hiện và viết lại)

- **Client Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Các trình khởi tạo client Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Công cụ**: chuyển đổi định nghĩa công cụ gọi hàm từ định dạng lồng nhau (`{"type": "function", "function": {"name": ...}}`) sang định dạng phẳng Responses (`{"type": "function", "name": ...}`); sử dụng `tool_choice`; trả về kết quả công cụ dưới dạng các mục `{"type": "function_call_output", "call_id": ..., "output": ...}` (không phải `{"role": "tool", ...}`).
- **Các vòng gọi công cụ**: khi mô hình trả về các cuộc gọi hàm, thêm các mục `response.output` vào cuộc trò chuyện (không phải dict thủ công `{"role": "assistant", "tool_calls": [...]}`), rồi thêm các mục `function_call_output` cho mỗi kết quả.
- **Ví dụ công cụ ít mẫu**: nếu cuộc trò chuyện bao gồm các ví dụ gọi công cụ mã cứng, chuyển chúng sang các mục `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID phải bắt đầu với `fc_`.
- **`pydantic_function_tool()`**: helper này vẫn tạo định dạng lồng nhau cũ và **không tương thích** với `responses.create()`. Thay bằng định nghĩa công cụ thủ công hoặc một wrapper làm phẳng.
- **Nhiều lượt hội thoại**: duy trì lịch sử trò chuyện trong ứng dụng; truyền các lượt trước qua các mục `input`.
- **Định dạng**: thay thế `response_format` cấp cao của Chat bằng `text.format` trong Responses. Hình thức chuẩn: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Mục nội dung**: thay thế `content[].type: "text"` của Chat bằng `content[].type: "input_text"` cho lượt của người dùng/hệ thống.
- **Mục nội dung hình ảnh**: thay thế `content[].type: "image_url"` của Chat bằng `content[].type: "input_image"` trong Responses. Trường `image_url` chuyển từ đối tượng lồng `{"url": "..."}` sang chuỗi phẳng. Xem bảng tóm tắt cho ví dụ trước/sau.
- **Nỗ lực suy luận**: **chỉ di chuyển `reasoning` nếu nó đã tồn tại trong mã nguồn gốc**.
- **Xử lý lỗi lọc nội dung**: cấu trúc thân lỗi thay đổi. Chat Completions dùng `error.body["innererror"]["content_filter_result"]` (số ít); Responses API dùng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, bên trong mảng). Mã truy cập `innererror` sẽ gây `KeyError`. Viết lại để dùng đường dẫn mới.
- **Gọi HTTP thô**: nếu ứng dụng gọi trực tiếp REST API Azure OpenAI (qua `requests`, `httpx`, v.v.) sử dụng `/openai/deployments/{name}/chat/completions?api-version=...`, chuyển sang `/openai/v1/responses`. Thân yêu cầu thay đổi: `messages` → `input`, thêm `max_output_tokens` và `store: false`, bỏ tham số query `api-version`. Thân phản hồi thay đổi: `choices[0].message.content` → `output[0].content[0].text` (lưu ý: `output_text` là thuộc tính tiện ích SDK không có trong JSON REST thô).

---

## Bước 2: Áp dụng di cư

### Ghi chú di cư (Chat Completions → Responses)

- **Tại sao di cư**: Responses là API hợp nhất cho văn bản, công cụ và luồng dữ liệu; Chat Completions là di sản. Với GPT-5, Responses bắt buộc để đạt hiệu năng tốt nhất.
- **HTTP**: điểm cuối Azure chuyển từ `/openai/deployments/{name}/chat/completions` sang `/openai/v1/responses`.
- **Trường dữ liệu**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` giữ nguyên.
- **Định dạng**: `response_format` → `text.format` với một đối tượng đúng chuẩn.
- **Mục nội dung**: Thay thế `content[].type: "text"` của Chat bằng `content[].type: "input_text"` trong Responses cho lượt hệ thống/người dùng.
- **Mục nội dung hình ảnh**: Thay thế `content[].type: "image_url"` của Chat bằng `content[].type: "input_image"` trong Responses. Làm phẳng trường `image_url` từ `{"image_url": {"url": "..."}}` thành `{"image_url": "..."}` (chuỗi thuần — có thể là URL HTTPS hoặc URI dữ liệu `data:image/...;base64,...`).

### Tham chiếu ánh xạ tham số

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (mảng mục) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (đối tượng) |
| `temperature` | `temperature` (không đổi) |
| `stop` | `stop` (không đổi) |
| `frequency_penalty` | `frequency_penalty` (không đổi) |
| `presence_penalty` | `presence_penalty` (không đổi) |
| `tools` / function-calling | `tools` (không đổi) |
| `seed` | **Loại bỏ** (không được hỗ trợ) |
| `store` | `store` (đặt là `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (chuỗi phẳng) |

Để xem ví dụ mã hoàn chỉnh trước/sau, xem [cheat-sheet.md](./references/cheat-sheet.md).

Để di cư hạ tầng kiểm thử (mocks, snapshot, assertion), xem [test-migration.md](./references/test-migration.md).

Để khắc phục sự cố lỗi và những điểm hay gặp, xem [troubleshooting.md](./references/troubleshooting.md).

---

## Giữ dữ liệu & Trạng thái

- Đặt `store: false` cho tất cả các yêu cầu Responses.
- Không dựa vào ID tin nhắn trước hoặc ngữ cảnh lưu trên máy chủ; giữ trạng thái do client quản lý và giảm thiểu metadata.

---

## Tiêu chí chấp nhận

### Các cổng kiểm tra cấp mã (tất cả phải vượt qua)

- [ ] Không tìm thấy kết quả cho `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` trong các tệp đã di cư.
- [ ] Không tìm thấy kết quả cho `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — tất cả constructor dùng `OpenAI`/`AsyncOpenAI` với điểm cuối v1.
- [ ] Không tìm thấy kết quả cho `rg "models\.github\.ai|models\.inference\.ai\.azure"` — loại bỏ các đường code GitHub Models.
- [ ] Không tìm thấy kết quả cho `rg "OpenAIChatCompletionClient"` — mã MAF 1.0.0+ sử dụng `OpenAIChatClient` (dùng Responses API). Trước 1.0.0, nâng cấp `agent-framework-openai>=1.0.0`.
- [ ] Tất cả lệnh gọi `ChatOpenAI(...)` bao gồm `use_responses_api=True`.
- [ ] Không tìm thấy kết quả cho `rg "choices\[0\]"` — mọi truy cập phản hồi dùng `resp.output_text` hoặc schema đầu ra Responses.
- [ ] Không có `response_format` ở cấp cao; mọi đầu ra có cấu trúc dùng `text={"format": {...}}`.
- [ ] `openai>=1.108.1` và `azure-identity` trong `requirements.txt` hoặc `pyproject.toml`; các phụ thuộc được cài lại.
- [ ] Đặt `store=False` trong mọi lần gọi `responses.create`.
- [ ] Không có `api_version` trong khởi tạo client; loại bỏ `AZURE_OPENAI_API_VERSION` khỏi các tệp env và hạ tầng.

### Các cổng kiểm tra hạ tầng (tất cả phải vượt qua)

- [ ] Không tìm thấy kết quả cho `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Không tìm thấy kết quả cho `rg "_azure_ad_token_provider" tests/` — cập nhật assertion kiểm tra `isinstance(client, AsyncOpenAI)` hoặc `base_url`.
- [ ] Không tìm thấy kết quả cho `rg "prompt_filter_results|content_filter_results" tests/` — loại bỏ mock lọc riêng Azure.
- [ ] Các mock fixture dùng `kwargs.get("input")` không phải `kwargs.get("messages")`.
- [ ] Snapshot / tệp golden cập nhật theo hình dạng streaming Responses (không có `choices[0]`, `function_call`, `logprobs`, v.v.).
- [ ] `pytest` chạy thành công không lỗi sau khi cập nhật tất cả kiểm thử.

### Các cổng hành vi (kiểm tra thủ công hoặc qua test harness)

- [ ] **Hoàn thành cơ bản**: `responses.create` không luồng trả về `output_text` không rỗng.
- [ ] **Tính tương đương luồng**: nếu mã gốc dùng luồng, mã di cư cũng luồng và phát sinh sự kiện `response.output_text.delta` với delta không rỗng.
- [ ] **Đầu ra có cấu trúc**: nếu dùng `text.format` với `json_schema`, `json.loads(resp.output_text)` thành công và khớp schema.
- [ ] **Vòng gọi công cụ**: nếu dùng công cụ, mô hình gọi chúng, ứng dụng thực thi, yêu cầu tiếp theo trả `output_text` cuối cùng (không vòng lặp vô hạn).
- [ ] **Tương đương bất đồng bộ**: nếu dùng `AsyncAzureOpenAI`, tương đương `AsyncOpenAI` hoạt động với `await`.
- [ ] **Tỷ lệ lỗi**: không có lỗi mới 400/401/404 so với nền tảng trước di cư.

### Các kết quả bàn giao

- Tóm tắt bao gồm các tệp đã chỉnh sửa, đếm trước/sau các điểm gọi di sản, và bước tiếp theo.
- Thay đổi chỉ là chỉnh sửa trên cây làm việc (không cam kết).

---

## Yêu cầu phiên bản SDK

| Gói | Phiên bản tối thiểu |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Mới nhất (cho xác thực EntraID) |

---

## Tham khảo

- [Bảng tóm tắt — tất cả đoạn mã](./references/cheat-sheet.md)
- [Di cư kiểm thử — mocks, snapshot, assertions](./references/test-migration.md)
- [Khắc phục sự cố — lỗi, bảng rủi ro, điểm cần lưu ý](./references/troubleshooting.md)
- [detect_legacy.py — bộ quét tự động](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Bộ khởi động Azure OpenAI](https://aka.ms/openai/start)
- [Tài liệu API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Vòng đời phiên bản API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Tham khảo API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->