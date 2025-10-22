<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T13:36:31+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "mo"
}
-->
# MCP 伺服器整合指南

## 先決條件
- 已安裝 Node.js（版本 14 或以上）
- npm 套件管理工具
- 配備必要依賴的 Python 環境

## 設置步驟

1. **安裝 MCP 伺服器套件**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **啟動 MCP 伺服器**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   伺服器應啟動並顯示連接 URL。

3. **驗證連接**  
   - 在 Chainlit 介面中尋找插頭圖示 (🔌)  
   - 插頭圖示旁應出現數字 (1)，表示連接成功  
   - 主控台應顯示：「GitHub 插件設置成功完成」（以及其他狀態行）

## 疑難排解

### 常見問題

1. **端口衝突**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   解決方法：使用以下指令更改端口：  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **身份驗證問題**  
   - 確保 GitHub 憑證已正確配置  
   - 檢查 .env 文件是否包含必要的令牌  
   - 驗證 GitHub API 訪問權限

3. **連接失敗**  
   - 確認伺服器正在預期的端口上運行  
   - 檢查防火牆設置  
   - 驗證 Python 環境是否安裝了必要的套件

## 連接驗證

當以下情況發生時，您的 MCP 伺服器已成功連接：
1. 主控台顯示「GitHub 插件設置成功完成」
2. 連接日誌顯示「✓ MCP 連接狀態：活躍」
3. GitHub 指令可在聊天介面中正常運作

## 環境變數

在您的 .env 文件中需要包含以下內容：  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## 測試連接

在聊天中發送以下測試訊息：  
```
Show me the repositories for username: [GitHub Username]
```  
成功的回應將顯示倉庫資訊。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。