# 示例收据文件

预先生成的三个收据文件，用于在不运行笔记本的情况下进行检查。

| 文件 | 内容说明 |
|---|---|
| `01_valid_receipt.json` | 一个有效的签名收据，用于 `lookup_flights` 工具调用。验证返回 True。 |
| `02_tampered_receipt.json` | 同一收据，其签名后被修改了一个字段。验证返回 False。 |
| `03_chain_three_receipts.json` | 三个有效收据的链条（查询、保留、预订），通过 `previous_receipt_hash` 将每个收据与前一个关联。 |

这些示例直接使用 Ed25519 对有效载荷的规范 JCS 字节签名。
SHA-256 仍用于内容摘要和收据链链接，而不是作为
签名前的额外预哈希。

## 验证示例

在 `18-signed-receipts.ipynb` 中，先运行 设置 和第 1 到第 3 节。
第 3 节定义了 `verify_chain`；仅第 1 节和第 2 节不足以满足要求。
然后在一个新单元格中运行以下代码块，并将笔记本的工作目录
设置为 `18-securing-ai-agents/code_samples`。下面的夹具路径是相对于
该目录。

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### 在不使用 Jupyter 时检查示例

在仓库根目录下，安装课程依赖并运行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

这些测试会执行笔记本的 Python 示例以及 README 中完全相同的代码块
如上所述。它们还会检查篡改和未固定的密钥是否会被
验证器拒绝。测试会跳过笔记本的 `%pip` 设置单元，因为依赖项
是单独安装的。它们不会更改笔记本或夹具。

## 这些示例是如何生成的

示例使用与笔记本相同的代码路径，使用固定的签名密钥
和固定时间戳以保证字节级重现。要重新生成：

```bash
python3 generate_fixtures.py
```

（脚本位于本目录的 `generate_fixtures.py`。）

## 学生通过检查原始 JSON 学到的内容

阅读原始收据格式建立了笔记本单元格中不一定提供的直觉。经常浏览 JSON 的学生
会注意到：

1. 签名是一个不透明的 base64url 字符串，但其他所有字段都是普通
   可读的 JSON。签名并未加密内容；它是对此内容的证明。
2. `public_key` 嵌入在收据中。审计员无需其他任何信息
   即可验证（前提是信任该密钥确实属于声称的
   发行人；参见课程 README 中的身份基础设施部分）。
3. 修改任何字段的一个字符，然后与
   `02_tampered_receipt.json` 进行字节级比较，会使该字节级机制更为具体。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
