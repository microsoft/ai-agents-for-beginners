---
name: jupyter-notebook
description: ユーザーが実験、探索、またはチュートリアル用の Jupyter ノートブック（`.ipynb`）を作成、スキャフォールド、または編集するよう依頼したときに使用します。バンドルされたテンプレートを優先し、ヘルパースクリプト
  `new_notebook.py` を実行してクリーンな開始ノートブックを生成してください。
---
# Jupyter Notebookのスキル

クリーンで再現可能な Jupyter ノートブックを、主に次の2つのモード向けに作成します:

- 実験および探索的解析
- チュートリアルおよび教育向けのウォークスルー

同梱のテンプレートとヘルパースクリプトを使うことで、一貫した構造を保ち、JSONのミスを減らすことを推奨します。

## いつ使うか
- 新しい `.ipynb` ノートブックをゼロから作成するとき。
- ラフなノートやスクリプトを構造化されたノートブックに変換するとき。
- 既存のノートブックをより再現可能で読みやすくリファクタリングするとき。
- 他の人が読むまたは再実行する実験やチュートリアルを作成するとき。

## 決定木分析
- リクエストが探索的、分析的、または仮説駆動型であれば、`experiment` を選びます。
- リクエストが指導的、段階的、または特定の対象者向けであれば、`tutorial` を選びます。
- 既存のノートブックを編集する場合はリファクタとして扱い、意図を保持して構造を改善します。

## スキルパス（一度設定）

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

ユーザー限定スキルは `$CODEX_HOME/skills` ディレクトリにインストールされます（デフォルト：`~/.codex/skills`）。

## ワークフロー
1. インテントを確定する。
ノートブックの種類（`experiment` または `tutorial`）を特定する。
目的、対象ユーザー、完了状態を明確にする。

2. テンプレートからスキャフォールディングする。
ヘルパースクリプトを使用することで、ノートブックのJSONを手作業で作成する必要がなくなります。

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```
3. ノートブックには、実行可能な小さなステップを記述してください。
各コードセルは、1つのステップに焦点を絞ってください。
目的と期待される結果を説明する短いマークダウンセルを追加してください。
短い要約で済む場合は、長くて冗長な出力は避けてください。

4. 適切なパターンを適用します。
実験については、`references/experiment-patterns.md` を参照してください。
チュートリアルについては、`references/tutorial-patterns.md` を参照してください。

5. 既存のノートブックを編集する際は、安全に作業を進めてください。
ノートブックの構造を維持し、全体の流れを改善する場合を除き、セルの順序変更は避けてください。
全面的な書き換えよりも、対象を絞った編集を優先してください。
どうしてもJSONファイルを編集する必要がある場合は、まず`references/notebook-structure.md`を確認してください。

6. 結果を検証する。
環境が許せば、ノートブックを最初から最後まで実行してください。
実行できない場合は、その旨を明記し、ローカル環境での検証方法を指示してください。
最終合格チェックリストは、`references/quality-checklist.md` を参照してください。

## テンプレートとヘルパースクリプト
- テンプレートは `assets/experiment-template.ipynb` と `assets/tutorial-template.ipynb` にあります。
- ヘルパースクリプトはテンプレートを読み込み、タイトルセルを更新し、ノートブックを作成します。

スクリプトのパス:
- `$JUPYTER_NOTEBOOK_CLI`（インストール時のデフォルト: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`）

## 一時ファイルと出力ファイルの保存規則
- 中間ファイルは `tmp/jupyter-notebook/` に保存し、作業完了後に削除してください。
- このリポジトリで作業する場合は、最終成果物を `output/jupyter-notebook/` に保存してください。
- 安定した、分かりやすいファイル名を使用してください（例：`ablation-temperature.ipynb`）。

## 依存関係（必要な場合のみインストールしてください）
依存関係の管理には`uv`の使用を推奨します。

ローカルノートブック実行のためのオプションのPythonパッケージ：

```bash
uv pip install jupyterlab ipykernel
```

同梱されているスキャフォールディングスクリプトはPython標準ライブラリのみを使用しており、追加の依存関係は不要です。

## 環境
必須の環境変数はありません。

## 参照マップ
- `references/experiment-patterns.md`: 実験の構成と経験則。
- `references/tutorial-patterns.md`: チュートリアルの構成と教育的な流れ。
- `references/notebook-structure.md`: ノートブックJSONの構造と安全な編集ルール。
- `references/quality-checklist.md`: 最終検証チェックリスト。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確さには努めていますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文（原言語の文書）を正本としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
