# 示例收据固定文件

三个预生成的收据文件，用于检查而不运行笔记本。

| 文件 | 说明 |
|---|---|
| `01_valid_receipt.json` | 一个有效签名的 `lookup_flights` 工具调用收据。验证返回 True。 |
| `02_tampered_receipt.json` | 同一收据在签名后修改了一个字段。验证返回 False。 |
| `03_chain_three_receipts.json` | 三个有效收据的链（搜索，保留，预订），通过 `previous_receipt_hash` 连接每一个到前一个。 |

这些固定文件直接用 Ed25519 签名负载的规范 JCS 字节。
SHA-256 仍用于内容摘要和收据链链接，而不是签名前的额外预哈希。


## 验证示例

笔记本分四部分演示验证步骤。若想直接验证这些固定文件而不执行笔记本内容：


```python
import json
from pathlib import Path

# 假设你已经完成了导入和辅助函数
# 来自18-signed-receipts.ipynb的第1和第2部分。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 假

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 这些文件的生成方法

这些固定文件使用与笔记本相同的代码路径，采用固定签名密钥
和固定时间戳以保证字节复现性。重新生成方法：

```bash
python3 generate_fixtures.py
```

（脚本位于本目录下的 `generate_fixtures.py` 文件。）

## 学生通过检查原始 JSON 学到的内容

阅读原始收据格式可以建立笔记本单元格中不总是显现的直觉。快速浏览 JSON 的学生通常注意到：


   可读 JSON。签名不加密内容；它是内容的证明。
2. `public_key` 嵌入在收据中。审计者无需其他信息即可验证（条件是相信该密钥确实属于声称的
   发行者；有关身份基础设施，请参见课程 README）。
3. 修改任何字段的单个字符，再与
   `02_tampered_receipt.json` 比较，使字节级机制具体可感知。



---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->