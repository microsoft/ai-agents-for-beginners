<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T00:24:34+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ja"
}
-->
# MCPサーバー統合ガイド

## 前提条件
- Node.js（バージョン14以上）がインストールされていること
- npmパッケージマネージャー
- 必要な依存関係を備えたPython環境

## セットアップ手順

1. **MCPサーバーパッケージのインストール**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCPサーバーの起動**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   サーバーが起動し、接続URLが表示されるはずです。

3. **接続の確認**  
   - Chainlitインターフェースでプラグアイコン（🔌）を探します  
   - プラグアイコンの横に数字（1）が表示されていれば、接続が成功しています  
   - コンソールに「GitHub plugin setup completed successfully」（および追加のステータス行）が表示されるはずです

## トラブルシューティング

### よくある問題

1. **ポートの競合**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   解決策: ポートを以下のコマンドで変更してください:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **認証の問題**  
   - GitHubの認証情報が正しく設定されていることを確認してください  
   - .envファイルに必要なトークンが含まれていることを確認してください  
   - GitHub APIへのアクセスを確認してください  

3. **接続失敗**  
   - サーバーが期待されるポートで稼働していることを確認してください  
   - ファイアウォールの設定を確認してください  
   - Python環境に必要なパッケージがインストールされていることを確認してください  

## 接続確認

MCPサーバーが正しく接続されている場合:  
1. コンソールに「GitHub plugin setup completed successfully」と表示される  
2. 接続ログに「✓ MCP Connection Status: Active」と表示される  
3. GitHubコマンドがチャットインターフェースで動作する  

## 環境変数

.envファイルに必要な内容:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## 接続テスト

チャットで以下のテストメッセージを送信してください:  
```
Show me the repositories for username: [GitHub Username]
```  
成功すると、リポジトリ情報が表示されます。  

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。