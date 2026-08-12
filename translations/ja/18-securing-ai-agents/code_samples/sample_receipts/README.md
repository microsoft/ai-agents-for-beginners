# サンプル領収書フィクスチャ

ノートブックを実行せずに検査できる、事前生成された3つの領収書ファイル。

| ファイル | 内容 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` ツール呼び出しのための有効な署名済み領収書。検証はTrueを返す。 |
| `02_tampered_receipt.json` | 署名後に1つのフィールドを変更した同じ領収書。検証はFalseを返す。 |
| `03_chain_three_receipts.json` | 3つの有効な領収書（検索、保留、予約）をつなぐチェーンで、各領収書に `previous_receipt_hash` が前のものをリンクしている。 |

## サンプル検証

ノートブックは4つのセクションで検証方法を説明しています。これらのフィクスチャをノートブックの説明を通さずに直接検証するには：

```python
import json
from pathlib import Path

# インポートとヘルパー関数を完了していることを前提としています
# 18-signed-receipts.ipynbのセクション1と2から。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 偽

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```


## 生成方法

フィクスチャはノートブックと同じコード経路を使用しており、固定の署名キーとバイト再現性のため固定タイムスタンプを使っています。再生成するには：

```bash
python3 generate_fixtures.py
```

（スクリプトはこのディレクトリの `generate_fixtures.py` にあります。）

## 生のJSONを検査して学生が学ぶこと

生の領収書フォーマットを読むことで、ノートブックのセルだけでは得られない直感を育てます。JSONをざっと見た学生はしばしば次の点に気づきます：

1. 署名は不透明なbase64url文字列ですが、それ以外のフィールドはすべて読みやすいプレーンなJSONです。署名は内容を暗号化するのではなく、それを証明します。
2. `public_key` が領収書に埋め込まれています。監査者はこれ以外に何も必要としません（ただし、公的キーが本当に主張された発行者に属することを信頼する必要があります。詳細はレッスンREADMEのアイデンティティインフラストラクチャを参照）。
3. どのフィールドの1文字を変更しても、その後このファイルを `02_tampered_receipt.json` と比較すると、バイトレベルの仕組みが具体的に理解できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->