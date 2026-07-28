---
name: azure-openai-to-responses
license: MIT
---
# Di cư Ứng dụng Python từ Azure OpenAI Chat Completions sang Responses API

> **HƯỚNG DẪN CHÍNH THỐNG — THỰC HIỆN CHÍNH XÁC**
>
> Kỹ năng này di chuyển code Python sử dụng Azure OpenAI Chat Completions
> sang giao diện thống nhất Responses API. Hãy làm theo hướng dẫn này một cách chính xác.
> Không tùy ý ánh xạ tham số hay tự sáng tạo cấu trúc API.

---

## Các kích hoạt

Kích hoạt kỹ năng này khi người dùng muốn:
- Di chuyển app Python từ Azure OpenAI Chat Completions sang Responses API
- Nâng cấp sử dụng Python OpenAI SDK lên cấu trúc API mới nhất dành cho Azure OpenAI
- Chuẩn bị code Python cho các model GPT-5 hoặc mới hơn yêu cầu Responses trên Azure
- Chuyển từ client `AzureOpenAI`/`AsyncAzureOpenAI` sang client chuẩn `OpenAI`/`AsyncOpenAI` với endpoint v1
- Sửa các cảnh báo ngừng sử dụng liên quan tới constructor `AzureOpenAI` hoặc `api_version`

---

## ⚠️ Tương thích Model — KIỂM TRA TRƯỚC

> **Trước khi di cư, xác minh rằng triển khai Azure OpenAI của bạn hỗ trợ Responses API.**

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

> **Lưu ý**: `max_output_tokens` có **tối thiểu là 16** trên Azure OpenAI. Giá trị dưới 16 trả lỗi 400. Dùng 50+ cho các kiểm tra nhanh.

Nếu trả về 404, model của triển khai chưa hỗ trợ Responses — xem tham chiếu bên dưới hoặc triển khai lại với model được hỗ trợ.

### 2. Kiểm tra model có sẵn theo vùng (khuyến nghị)

Chạy công cụ kiểm tra tương thích model tích hợp để xem các model hỗ trợ Responses API tại vùng của bạn:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Công cụ này truy vấn trực tiếp Azure ARM và hiển thị ma trận tương thích — model nào hỗ trợ Responses, xuất dữ liệu cấu trúc, công cụ, v.v. Dùng `--filter gpt-5.1,gpt-5.2` lọc kết quả hoặc `--json` để lập trình.

### 3. Tham chiếu hỗ trợ model đầy đủ

- **Truy vấn trực tiếp**: `python migrate.py models` (xem trên — theo vùng, luôn được cập nhật)
- **Xem sẵn có**: [Bảng tóm tắt model và vùng hỗ trợ](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Khởi động nhanh & hướng dẫn**: **https://aka.ms/openai/start**

### ⚠️ Giới hạn model cũ

> **CẢNH BÁO**: Các model cũ (trước `gpt-4.1`) có thể không hỗ trợ đầy đủ tất cả tính năng Responses API.
>
> Các hạn chế đã biết với model cũ:
> - **tham số `reasoning`**: Không được hỗ trợ trên nhiều model không dùng reasoning. Chỉ di cư `reasoning` nếu tham số này đã có trong code gốc.
> - **tham số `seed`**: Hoàn toàn không được hỗ trợ trong Responses API — loại bỏ khỏi tất cả các yêu cầu.
> - **Xuất dữ liệu cấu trúc qua `text.format`**: Model cũ có thể không chắc chắn tuân thủ schema JSON `strict: true`.
> - **Điều phối công cụ**: GPT-5+ điều phối gọi công cụ trong quá trình reasoning nội bộ. Model cũ trên Responses vẫn hoạt động nhưng không có tích hợp sâu này.
> - **Giới hạn nhiệt độ**: Khi di cư sang `gpt-5`, nhiệt độ phải bị bỏ hoặc đặt là `1`. Model cũ không có giới hạn này.

### Model reasoning dòng O-series (o1, o3-mini, o3, o4-mini)

Model dòng O có các hạn chế tham số đặc thù. Khi di cư app nhắm tới model O-series:

- **`temperature`**: Phải là `1` (hoặc không dùng). Model O không chấp nhận giá trị khác.
- **`max_completion_tokens` → `max_output_tokens`**: Ứng dụng dùng `max_completion_tokens` riêng Azure phải chuyển sang `max_output_tokens`. Đặt giá trị cao (4096+) vì token reasoning tính vào giới hạn.
- **`reasoning_effort`**: Nếu app dùng `reasoning_effort` (low/medium/high), giữ lại — Responses API hỗ trợ tham số này cho model O.
- **Hành vi phát trực tiếp**: Model O có thể đệm output đến khi reasoning xong mới phát sự kiện delta text. Streaming vẫn hoạt động, nhưng `response.output_text.delta` đầu tiên có thể đến muộn hơn so với model GPT.
- **`top_p`**: Không hỗ trợ trên O-series — loại bỏ nếu có.
- **Sử dụng công cụ**: Model O hỗ trợ công cụ qua Responses API như GPT, nhưng chất lượng điều phối cuộc gọi công cụ khác nhau theo model.

**Hành động — tư vấn model chủ động**: Trong bước quét, kiểm tra model app đang nhắm tới (tên triển khai, biến môi trường, cấu hình). Nếu model là trước `gpt-4.1` (không phải gpt-4.1+), chủ động báo người dùng:
- Việc di cư sẽ hoạt động với text cơ bản, chat, streaming và công cụ trên model hiện tại.
- Model mới hơn (`gpt-5.1`, `gpt-5.2`) cung cấp điều phối công cụ tốt hơn, áp dụng xuất dữ liệu cấu trúc, reasoning và khả năng chọn vùng linh hoạt.
- Họ nên xem xét nâng cấp triển khai khi sẵn sàng — việc này không chặn di cư.

Không chặn hoặc từ chối di cư dựa trên phiên bản model. Lời tư vấn chỉ mang tính thông tin.

### GitHub Models KHÔNG hỗ trợ Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) không hỗ trợ Responses API.**

Nếu code có đường dẫn code GitHub Models (tìm `base_url` trỏ tới `models.github.ai` hoặc `models.inference.ai.azure.com`), **xoá hoàn toàn** trong quá trình di cư. Responses API yêu cầu Azure OpenAI, OpenAI, hoặc endpoint local tương thích (ví dụ Ollama có hỗ trợ Responses).

Hành động trong bước quét:
- Đánh dấu mọi đường dẫn code GitHub Models để loại bỏ.

---

## Di cư Framework

Nhiều app sử dụng framework cấp cao trên OpenAI. Khi di cư, API của framework cũng thay đổi — không chỉ các gọi OpenAI bên dưới.

### Microsoft Agent Framework (MAF)

**Kiểm tra phiên bản MAF trước** — di cư phụ thuộc vào bạn đang dùng MAF >=1.0.0 hay phiên bản beta/rc trước 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **đã sử dụng Responses API** — không cần di cư. Nếu code dùng client cũ `OpenAIChatCompletionClient` (dùng `chat.completions.create`), thay bằng `OpenAIChatClient`.

| Trước | Sau |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Kiểm tra phiên bản: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF trước 1.0.0 (phát hành beta/rc)

Trong MAF trước 1.0.0, `OpenAIChatClient` dùng Chat Completions. Nâng cấp lên `agent-framework-openai>=1.0.0` để `OpenAIChatClient` dùng Responses API mặc định.

Không cần thay đổi khác — API `Agent` và công cụ vẫn giữ nguyên.

### LangChain (`langchain-openai`)

Thêm `use_responses_api=True` vào `ChatOpenAI()`. Cũng cập nhật truy cập response từ `.content` thành `.text`.

| Trước | Sau |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Ví dụ code trước/sau đầy đủ, xem [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hướng dẫn Di cư Frontend

> **Responses API là phía server.** Di chuyển backend Python của bạn; hợp đồng HTTP frontend không thay đổi trừ khi backend là một tầng chuyển tiếp mỏng — trong trường hợp đó, cân nhắc dùng cấu trúc request Responses để loại bỏ lớp dịch. Nếu frontend gọi OpenAI trực tiếp với key phía client, hãy chuyển các gọi đó về backend trước.

### Ngừng sử dụng `@microsoft/ai-chat-protocol`

Gói npm `@microsoft/ai-chat-protocol` đã ngừng và nên thay bằng [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Nếu frontend dùng nó:

1. Thay tag script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Xoá khởi tạo `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Thay `client.getStreamedCompletion(messages)` bằng gọi trực tiếp `fetch()` tới endpoint streaming backend.
4. Thay `for await (const response of result)` bằng `for await (const chunk of readNDJSONStream(response.body))`.
5. Cập nhật truy cập thuộc tính từ `response.delta.content` / `response.error` sang `chunk.delta.content` / `chunk.error`.

---

## Mục tiêu

- Liệt kê tất cả điểm gọi Python dùng Chat Completions hoặc legacy Completions với Azure OpenAI.
- Đề xuất kế hoạch và trình tự di cư cho code Python.
- Thực hiện chỉnh sửa an toàn, tối thiểu để chuyển sang Responses API.
- Cập nhật caller để dùng schema Output của Responses; không dùng wrapper tương thích ngược.
- Chạy test/lint; sửa lỗi phát sinh do di cư.
- Chuẩn bị các bộ thay đổi nhỏ dễ xem xét và cung cấp tóm tắt cuối với diff (không commit).

---

## Quy tắc bảo vệ

- Chỉ chỉnh sửa file trong workspace git. Không ghi ra ngoài.
- Không giữ shim tương thích ngược; di cư code sang cấu trúc API mới.
- Không để lại comment tombstone/transition hay file backup.
- Giữ nguyên semantics streaming nếu đã dùng; nếu không, dùng không streaming.
- Hỏi phê duyệt trước khi chạy lệnh hoặc gọi mạng nếu đang ở chế độ phê duyệt.
- Không chạy `git add`/`git commit`/`git push`; chỉ tạo sửa đổi trên cây làm việc.

---

## Bước 0: Di cư Client Azure OpenAI (Tiền đề)

Nếu code dùng constructor `AzureOpenAI` hoặc `AsyncAzureOpenAI`, di cư sang constructor chuẩn `OpenAI` / `AsyncOpenAI` trước. Constructor riêng Azure đã ngừng dùng trong `openai>=1.108.1`.

### Vì sao dùng endpoint v1?

Endpoint mới `/openai/v1` dùng client chuẩn `OpenAI()` thay vì `AzureOpenAI()`, không cần tham số `api_version`, và hoạt động giống nhau cả trên OpenAI và Azure OpenAI. Code client giống nhau và không cần quản lý phiên bản.

### Thay đổi chính

| Trước | Sau |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Xoá hoàn toàn |

### Danh sách dọn dẹp

- Xoá tham số `api_version` khỏi constructor client.
- Xoá biến môi trường `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` khỏi `.env`, cài đặt app, và file Bicep/infra.
- Đổi tên `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` trong `.env`, cài đặt app, Bicep/infra và fixtures kiểm thử (quy ước Azure Identity SDK chuẩn).
- Đảm bảo `openai>=1.108.1` trong `requirements.txt` hoặc `pyproject.toml`.

### Di cư biến môi trường

| Biến env cũ | Hành động | Ghi chú |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Xoá** | Không cần `api_version` với endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Xoá** | Giống trên |
| `AZURE_OPENAI_CLIENT_ID` | **Đổi tên** → `AZURE_CLIENT_ID` | Quy ước chuẩn Azure Identity SDK cho `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Giữ** | Vẫn cần để tạo `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Giữ** | Dùng làm param `model` trong `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Giữ** | Dùng làm `api_key` cho xác thực key |

Ví dụ code thiết lập client (đồng bộ, bất đồng bộ, EntraID, API key, đa tenant) xem [cheat-sheet.md](./references/cheat-sheet.md).

---

## Bước 1: Phát hiện Các điểm gọi Di sản

Chạy script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) để tìm tất cả điểm gọi cần di cư:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Hoặc chạy tìm kiếm tay — mỗi kết quả phù hợp là một mục tiêu di cư:

```bash
# Các cuộc gọi API kế thừa (phải viết lại)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Các hàm tạo client Azure đã ngừng hỗ trợ (phải thay thế)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Các mẫu truy cập kiểu phản hồi (phải cập nhật)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Định nghĩa công cụ ở định dạng lồng nhau cũ (phải làm phẳng)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Kết quả công cụ ở định dạng cũ (phải chuyển đổi sang function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Các tham số đã ngừng hỗ trợ (phải loại bỏ hoặc đổi tên)
rg "response_format"
rg "max_tokens\b"        # đổi tên thành max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Biến môi trường đã ngừng hỗ trợ (dọn dẹp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # nên là AZURE_CLIENT_ID

# Các điểm cuối Models của GitHub (phải loại bỏ — API Responses không được hỗ trợ)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Các mẫu kế thừa ở cấp Framework (phải cập nhật)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: thay thế bằng OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: cần use_responses_api=True

# Hạ tầng kiểm thử (phải cập nhật)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Truy cập phần thân lỗi bộ lọc nội dung (phải cập nhật — cấu trúc thay đổi)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # dạng số ít cũ — hiện là content_filter_results (số nhiều) bên trong mảng content_filters

# Các cuộc gọi HTTP thô đến điểm cuối Chat Completions (phải cập nhật URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Quy tắc (phát hiện và viết lại)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Trình khởi tạo client Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Công cụ**: chuyển đổi định nghĩa công cụ gọi hàm từ định dạng lồng nhau (`{"type": "function", "function": {"name": ...}}`) sang định dạng Phản hồi phẳng (`{"type": "function", "name": ...}`); sử dụng `tool_choice`; trả về kết quả công cụ dưới dạng các mục `{"type": "function_call_output", "call_id": ..., "output": ...}` (không phải `{"role": "tool", ...}`).
- **Vòng gọi lại công cụ**: khi mô hình trả về các cuộc gọi hàm, thêm các mục `response.output` vào cuộc hội thoại (không phải dict thủ công `{"role": "assistant", "tool_calls": [...]}`), rồi thêm các mục `function_call_output` cho từng kết quả.
- **Ví dụ công cụ ít bước**: nếu cuộc hội thoại bao gồm các ví dụ gọi công cụ mã cứng, chuyển chúng thành các mục `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID phải bắt đầu với `fc_`.
- **`pydantic_function_tool()`**: helper này vẫn tạo định dạng lồng nhau cũ và **không tương thích** với `responses.create()`. Thay thế bằng định nghĩa công cụ thủ công hoặc wrapper làm phẳng.
- **Nhiều lượt**: duy trì lịch sử hội thoại trong app; truyền các lượt trước thông qua các mục `input`.
- **Định dạng**: thay thế `response_format` cấp cao của Chat bằng `text.format` trong Responses. Hình thức chuẩn: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Mục nội dung**: thay thế Chat `content[].type: "text"` bằng Responses `content[].type: "input_text"` cho các lượt của người dùng/hệ thống.
- **Mục nội dung ảnh**: thay thế Chat `content[].type: "image_url"` bằng Responses `content[].type: "input_image"`. Trường `image_url` thay đổi từ đối tượng lồng nhau `{"url": "..."}` thành chuỗi phẳng. Xem cheat sheet để biết ví dụ trước/sau.
- **Nỗ lực suy luận**: **chỉ di chuyển `reasoning` nếu nó đã tồn tại trong mã gốc**.
- **Xử lý lỗi bộ lọc nội dung**: cấu trúc thân lỗi đã thay đổi. Chat Completions dùng `error.body["innererror"]["content_filter_result"]` (số ít); Responses API dùng `error.body["content_filters"][0]["content_filter_results"]` (số nhiều, trong mảng). Mã truy cập `innererror` sẽ gây ra `KeyError`. Viết lại để dùng đường dẫn mới.
- **Gọi HTTP thô**: nếu app gọi REST API Azure OpenAI trực tiếp (qua `requests`, `httpx`, v.v.) với `/openai/deployments/{name}/chat/completions?api-version=...`, viết lại thành `/openai/v1/responses`. Thân yêu cầu thay đổi: `messages` → `input`, thêm `max_output_tokens` và `store: false`, bỏ tham số truy vấn `api-version`. Thân phản hồi thay đổi: `choices[0].message.content` → `output[0].content[0].text` (lưu ý: `output_text` là thuộc tính tiện dụng SDK không có trong JSON REST thô).

---

## Bước 2: Áp dụng Di cư

### Ghi chú Di cư (Chat Completions → Responses)

- **Tại sao di cư**: Responses là API thống nhất cho văn bản, công cụ và streaming; Chat Completions là kế thừa. Với GPT-5, Responses là bắt buộc để có hiệu suất tốt nhất.
- **HTTP**: điểm cuối Azure chuyển từ `/openai/deployments/{name}/chat/completions` sang `/openai/v1/responses`.
- **Trường**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` giữ nguyên.
- **Định dạng**: `response_format` → `text.format` với một đối tượng phù hợp.
- **Mục nội dung**: Thay thế Chat `content[].type: "text"` bằng Responses `content[].type: "input_text"` cho các lượt hệ thống/người dùng.
- **Mục nội dung ảnh**: Thay thế Chat `content[].type: "image_url"` bằng Responses `content[].type: "input_image"`. Làm phẳng trường `image_url` từ `{"image_url": {"url": "..."}}` thành `{"image_url": "..."}` (chuỗi thuần — URL HTTPS hoặc URI dữ liệu `data:image/...;base64,...`).

### Tham chiếu ánh xạ tham số

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (mảng các mục) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (đối tượng) |
| `temperature` | `temperature` (không đổi) |
| `stop` | `stop` (không đổi) |
| `frequency_penalty` | `frequency_penalty` (không đổi) |
| `presence_penalty` | `presence_penalty` (không đổi) |
| `tools` / gọi hàm | `tools` (không đổi) |
| `seed` | **Loại bỏ** (không hỗ trợ) |
| `store` | `store` (đặt thành `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (chuỗi phẳng) |

Để xem ví dụ mã hoàn chỉnh trước/sau, xem [cheat-sheet.md](./references/cheat-sheet.md).

Để di cư hạ tầng kiểm thử (mocks, snapshots, assertions), xem [test-migration.md](./references/test-migration.md).

Để khắc phục lỗi và lưu ý, xem [troubleshooting.md](./references/troubleshooting.md).

---

## Lưu trữ Dữ liệu & Trạng thái

- Đặt `store: false` trên tất cả các yêu cầu Responses.
- Không dựa vào ID tin nhắn trước hoặc ngữ cảnh lưu trên máy chủ; quản lý trạng thái ở phía client và giảm thiểu metadata.

---

## Tiêu chí Chấp nhận

### Rào cản mức mã nguồn (phải đều đạt)

- [ ] Không có kết quả tìm thấy `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` trong các tệp đã di cư.
- [ ] Không có kết quả tìm thấy `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — tất cả trình khởi tạo sử dụng `OpenAI`/`AsyncOpenAI` với điểm cuối v1.
- [ ] Không có kết quả tìm thấy `rg "models\.github\.ai|models\.inference\.ai\.azure"` — các đường dẫn mã GitHub Models đã bị loại bỏ.
- [ ] Không có kết quả tìm thấy `rg "OpenAIChatCompletionClient"` — mã MAF 1.0.0+ sử dụng `OpenAIChatClient` (dùng Responses API). Trong pre-1.0.0, nâng cấp lên `agent-framework-openai>=1.0.0`.
- [ ] Tất cả các gọi `ChatOpenAI(...)` phải có `use_responses_api=True`.
- [ ] Không có kết quả tìm thấy `rg "choices\[0\]"` — toàn bộ truy cập phản hồi dùng `resp.output_text` hoặc schema đầu ra Responses.
- [ ] Không có `response_format` cấp cao; toàn bộ đầu ra cấu trúc sử dụng `text={"format": {...}}`.
- [ ] `openai>=1.108.1` và `azure-identity` trong `requirements.txt` hoặc `pyproject.toml`; cài lại dependencies.
- [ ] Đặt `store=False` trên mọi gọi `responses.create`.
- [ ] Không có `api_version` trong cấu tạo client; loại bỏ `AZURE_OPENAI_API_VERSION` khỏi các file env và hạ tầng.

### Rào cản hạ tầng kiểm thử (phải đều đạt)

- [ ] Không có kết quả tìm thấy `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Không có kết quả tìm thấy `rg "_azure_ad_token_provider" tests/` — các assertion đã được cập nhật để kiểm tra `isinstance(client, AsyncOpenAI)` hoặc `base_url`.
- [ ] Không có kết quả tìm thấy `rg "prompt_filter_results|content_filter_results" tests/` — loại bỏ mock bộ lọc đặc thù Azure.
- [ ] Các fixture mock dùng `kwargs.get("input")` thay vì `kwargs.get("messages")`.
- [ ] Các snapshot / golden files cập nhật theo hình dạng streaming Responses (không có `choices[0]`, `function_call`, `logprobs`, v.v.).
- [ ] `pytest` chạy thành công không lỗi sau mọi cập nhật test.

### Rào cản hành vi (xác minh thủ công hoặc qua test harness)

- [ ] **Hoàn thành cơ bản**: `responses.create` không streaming trả về `output_text` không rỗng.
- [ ] **Đồng bộ luồng**: nếu mã gốc dùng streaming, mã di cư cũng stream và yield các sự kiện `response.output_text.delta` với các delta không rỗng.
- [ ] **Đầu ra cấu trúc**: nếu dùng `text.format` với `json_schema`, `json.loads(resp.output_text)` thành công và khớp schema.
- [ ] **Vòng gọi công cụ**: nếu dùng công cụ, mô hình phát sinh gọi công cụ, app thực thi, và yêu cầu tiếp theo trả về `output_text` cuối cùng (không vòng lặp vô hạn).
- [ ] **Đồng bộ bất đồng bộ**: nếu dùng `AsyncAzureOpenAI`, tương đương `AsyncOpenAI` hoạt động với `await`.
- [ ] **Tỷ lệ lỗi**: không có lỗi 400/401/404 mới so với baseline trước di cư.

### Sản phẩm giao nộp

- Tóm tắt kết quả gồm các tệp đã chỉnh sửa, số lượng gọi legacy trước/sau, và bước tiếp theo.
- Thay đổi chỉ ở working-tree (không commit).

---

## Yêu cầu Phiên bản SDK

| Gói | Phiên bản Tối thiểu |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Mới nhất (cho xác thực EntraID) |

---

## Tài liệu Tham khảo

- [Cheat Sheet — tất cả đoạn mã](./references/cheat-sheet.md)
- [Di cư Kiểm thử — mocks, snapshots, assertions](./references/test-migration.md)
- [Khắc phục sự cố — lỗi, bảng rủi ro, lưu ý](./references/troubleshooting.md)
- [detect_legacy.py — trình quét tự động](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Tài liệu Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Vòng đời Phiên bản Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Tham khảo Azure OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->