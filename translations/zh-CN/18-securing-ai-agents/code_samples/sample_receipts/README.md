# 示例收据夹具

三个预生成的收据文件，可在不运行笔记本的情况下进行检查。

| 文件 | 内容说明 |
|---|---|
| `01_valid_receipt.json` | 一个有效的签名收据，针对 `lookup_flights` 工具调用。验证结果为 True。 |
| `02_tampered_receipt.json` | 同一收据，在签名后修改了一个字段。验证结果为 False。 |
| `03_chain_three_receipts.json` | 三个有效收据的链（搜索、保留、预订），通过 `previous_receipt_hash` 将每个收据链接到前一个。 |

## 验证示例

笔记本分四部分讲解验证过程。要直接验证这些夹具文件而不运行笔记本叙述：

```python
import json
from pathlib import Path

# 假设您已经完成了导入和辅助函数的编写
# 来自18-signed-receipts.ipynb的第1和第2部分。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 假

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 这些文件是如何生成的

这些夹具使用与笔记本相同的代码路径，采用固定签名密钥和固定时间戳以实现字节级可复现。重新生成方法：

```bash
python3 generate_fixtures.py
```

（脚本位于本目录的 `generate_fixtures.py`。）

## 学生从检查原始 JSON 中学到的内容

阅读原始收据格式有助于建立直观认识，而这些认识在笔记本单元格中并不总是提供。快速浏览 JSON 的学生通常会注意到：

1. 签名是一个不透明的 base64url 字符串，而其他字段都是纯可读的 JSON。签名不对内容加密；它是内容的证明。
2. 收据中嵌入了 `public_key`。审核者无需其他东西即可验证（前提是信任该密钥确实属于声称的发行者；参考课程 README 中关于身份基础设施的部分）。
3. 修改任何字段的单个字符，然后将该文件与 `02_tampered_receipt.json` 进行字节级比较，使机制更具体。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->