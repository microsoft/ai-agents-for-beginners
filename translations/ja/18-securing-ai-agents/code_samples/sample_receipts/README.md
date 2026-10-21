# サンプル領収書フィクスチャ

ノートブックを実行せずに検査するための、3つの事前生成された領収書ファイルです。

| ファイル | 内容 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` ツール呼び出しの有効な署名済み領収書。検証は True を返します。 |
| `02_tampered_receipt.json` | 署名後に1つのフィールドが変更された同じ領収書。検証は False を返します。 |
| `03_chain_three_receipts.json` | `previous_receipt_hash` で前の領収書にリンクされた、3つの有効な領収書（検索、保持、予約）のチェーン。 |

これらのフィクスチャは、ペイロードの正準JCSバイト列をEd25519で直接署名しています。
SHA-256はコンテンツダイジェストと領収書チェーンのリンクには引き続き使われますが、
署名前の追加プレハッシュとしては使われません。

## サンプルの検証

ノートブックは4つのセクションで検証の手順を説明します。これらのフィクスチャを
ノートブックの説明なしで直接検証するには：

```python
import json
from pathlib import Path

# Assumes you have completed the imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## これらの生成方法

フィクスチャはノートブックと同じコードパスを使い、1つの固定署名鍵と
バイト再現性のための固定タイムスタンプがあります。再生成するには：

```bash
python3 generate_fixtures.py
```

（このディレクトリの `generate_fixtures.py` にスクリプトがあります。）

## 生のJSONを調べて学生が学ぶこと

生の領収書フォーマットを読むことで、ノートブック内のセルが常に提供しない直感が培われます。
JSONをざっと見る学生はよく以下に気づきます：

1. 署名は不透明なbase64url文字列ですが、他のすべてのフィールドはプレーンな
   読みやすいJSONです。署名は内容を暗号化しません；内容を証明します。
2. `public_key` が領収書内に埋め込まれています。監査者は、(実際に
   鍵が主張している発行者に属していると信頼する条件付きで；アイデンティティ
   インフラのレッスンREADMEを参照) 他に何も必要ありません。
3. 任意のフィールドの1文字を変更し、その後このファイルを
   `02_tampered_receipt.json` と再比較することで、バイトレベルの仕組みが具体的に理解できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->