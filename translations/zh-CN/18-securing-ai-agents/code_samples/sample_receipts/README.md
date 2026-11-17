# 示例收据夹具

四个预生成的收据文件，可用于在不运行笔记本的情况下检查。

| 文件 | 说明 |
|---|---|
| `01_valid_receipt.json` | 用于 `lookup_flights` 工具调用的有效签名收据。验证返回 True。 |
| `02_tampered_receipt.json` | 相同的收据在签名后有一个字段被修改。验证返回 False。 |
| `03_chain_three_receipts.json` | 由三个有效收据 (search, hold, book) 组成的链，使用 `previous_receipt_hash` 将每个与前一个关联. |
| `04_resigned_receipt.json` | 相同的收据被攻击者篡改并重新签名，嵌入了攻击者自己的公钥. 使用其中的密钥可以验证通过. 使用发行者的密钥验证则失败. |

测试夹具直接使用 Ed25519 对有效载荷的规范 JCS 字节进行签名。
SHA-256 仍用于内容摘要和收据链链接，而不是作为一个
在签名前的额外预哈希。

## 验证示例

在 `18-signed-receipts.ipynb` 中，首先运行 Setup 和第1至第3节。
第3节定义了 `verify_chain`；仅第1和第2节不足以完成。
然后在一个新单元格中运行以下代码块，并将笔记本的工作目录
设置为 `18-securing-ai-agents/code_samples`。下面的夹具路径是相对于
该目录。

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### 在不使用 Jupyter 的情况下检查示例

在仓库根目录下，安装课程依赖并运行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

这些测试会执行笔记本中的 Python 示例以及 README 中的相同代码块
上方。它们还检查篡改和未固定的密钥是否会被
验证器。测试会跳过笔记本的 `%pip` 设置单元格，因为依赖
是单独安装的。它们不会更改笔记本或测试夹具。

## 这些是如何生成的

这些测试夹具与笔记本使用相同的代码路径，采用一个固定的签名密钥
以及固定的时间戳以实现字节可复现性。要重新生成：

```bash
python3 generate_fixtures.py
```

(脚本位于此目录的 `generate_fixtures.py`。)

`../test_signed_receipts.py` 会自动检查所有这些：它运行
笔记本的代码，验证这四个夹具与笔记本的
`verify_receipt` 和 `verify_chain`，并确认重新生成这些
夹具会产生相同的字节。来自 `code_samples`：

```bash
python -m unittest test_signed_receipts
```

## 学生从检查原始 JSON 中学到的内容

阅读原始收据格式可以培养对笔记本中单元格的直觉
并不总是能提供。略读 JSON 的学生经常会注意到：

1. 签名是一个不透明的 base64url 字符串，但其他每个字段都是纯
    可读的 JSON。签名并不加密内容；它证明内容的真实性。
2. `public_key` 被嵌入在收据中，这使得该文件
    自包含，但并不是审计者用来验证的对象。比较
    `02_tampered_receipt.json` 与 `04_resigned_receipt.json`：两者都在签名后被
    更改过，但第二个使用攻击者自己的密钥重新签名，
    因此它会用其自身携带的密钥进行验证。嵌入的密钥
    告诉你该文件在内部是一致的。只有从别处获得的密钥
    才能告诉你是谁签发了它。
3. 修改位于 `signature` 之外的任何字段中的单个字符，然后
    将此文件与 `02_tampered_receipt.json` 重新比较，会让
    字节级机制变得具体可见。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->