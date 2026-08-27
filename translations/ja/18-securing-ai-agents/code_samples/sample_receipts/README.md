# サンプル領収書フィクスチャ

ノートブックを実行せずに検査できる3つの事前生成領収書ファイルです。

| ファイル | 内容 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights`ツール呼び出し用の有効な署名付き領収書。検証はTrueを返します。 |
| `02_tampered_receipt.json` | 署名後に1つのフィールドが改ざんされた同じ領収書。検証はFalseを返します。 |
| `03_chain_three_receipts.json` | 3つの有効な領収書（検索、保持、予約）の連鎖。各々が前のものに`previous_receipt_hash`でリンクされています。 |

フィクスチャはペイロードの正準JCSバイトを直接Ed25519で署名します。
SHA-256はコンテンツダイジェストや領収書チェーンリンクに使われており、
署名前の追加のプリハッシュとしては使われていません。

## サンプルの検証

ノートブックでは検証を4つのセクションで説明しています。これらのフィクスチャを
ノートブックの説明を経ずに直接検証するには：

```python
import json
from pathlib import Path

# インポートとヘルパー関数を完了していることを前提としています
# 18-signed-receipts.ipynb のセクション1および2より

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 偽

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 生成方法

フィクスチャはノートブックと同じコードパスを使い、1つの固定署名鍵と
バイト再現性のための固定タイムスタンプが設定されています。再生成するには：

```bash
python3 generate_fixtures.py
```

（スクリプトはこのディレクトリの`generate_fixtures.py`にあります。）

## 生のJSONを調べて学生が学ぶこと

生の領収書フォーマットを読むことで、ノートブックのセルでは得られない直感が育まれます。
JSONをざっと見る学生はしばしば以下に気づきます：

1. 署名は不透明なbase64url文字列ですが、他のすべてのフィールドは平易な
   読みやすいJSONです。署名は内容を暗号化するのではなく、それを証明します。
2. `public_key`は領収書に埋め込まれています。監査人は実際に当該
   発行者に属すると信頼できる限りにおいて（IDインフラのレッスンREADME参照）、
   他に何も必要としません。
3. 任意のフィールドの1文字を修正し、このファイルと
   `02_tampered_receipt.json`を再比較すると、バイトレベルの仕組みが具体的に理解できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->