<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T13:36:41+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "br"
}
-->
# Guia de Integração do Servidor MCP

## Pré-requisitos
- Node.js instalado (versão 14 ou superior)
- Gerenciador de pacotes npm
- Ambiente Python com dependências necessárias

## Etapas de Configuração

1. **Instalar o Pacote do Servidor MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Iniciar o Servidor MCP**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   O servidor deve iniciar e exibir uma URL de conexão.

3. **Verificar Conexão**
   - Procure pelo ícone de plug (🔌) na interface do Chainlit
   - Um número (1) deve aparecer ao lado do ícone de plug, indicando conexão bem-sucedida
   - O console deve exibir: "Configuração do plugin GitHub concluída com sucesso" (junto com outras linhas de status)

## Solução de Problemas

### Problemas Comuns

1. **Conflito de Porta**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Solução: Altere a porta usando:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemas de Autenticação**
   - Certifique-se de que as credenciais do GitHub estão configuradas corretamente
   - Verifique se o arquivo .env contém os tokens necessários
   - Confirme o acesso à API do GitHub

3. **Falha na Conexão**
   - Confirme se o servidor está rodando na porta esperada
   - Verifique as configurações do firewall
   - Certifique-se de que o ambiente Python possui os pacotes necessários

## Verificação de Conexão

Seu servidor MCP está devidamente conectado quando:
1. O console exibe "Configuração do plugin GitHub concluída com sucesso"
2. Os logs de conexão mostram "✓ Status da Conexão MCP: Ativo"
3. Comandos do GitHub funcionam na interface de chat

## Variáveis de Ambiente

Necessárias no seu arquivo .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testando a Conexão

Envie esta mensagem de teste no chat:
```
Show me the repositories for username: [GitHub Username]
```
Uma resposta bem-sucedida exibirá informações do repositório.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.