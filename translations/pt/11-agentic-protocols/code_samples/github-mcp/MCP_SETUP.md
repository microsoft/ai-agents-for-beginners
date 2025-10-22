<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T15:00:10+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "pt"
}
-->
# Guia de Integração do Servidor MCP

## Pré-requisitos
- Node.js instalado (versão 14 ou superior)
- Gestor de pacotes npm
- Ambiente Python com as dependências necessárias

## Passos de Configuração

1. **Instalar o Pacote do Servidor MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Iniciar o Servidor MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   O servidor deverá iniciar e exibir um URL de conexão.

3. **Verificar a Conexão**  
   - Procure o ícone de ficha (🔌) na interface do Chainlit  
   - Um número (1) deverá aparecer ao lado do ícone de ficha, indicando uma conexão bem-sucedida  
   - A consola deverá exibir: "Configuração do plugin GitHub concluída com sucesso" (juntamente com linhas de estado adicionais)

## Resolução de Problemas

### Problemas Comuns

1. **Conflito de Porta**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solução: Altere a porta utilizando:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemas de Autenticação**  
   - Certifique-se de que as credenciais do GitHub estão configuradas corretamente  
   - Verifique se o ficheiro .env contém os tokens necessários  
   - Confirme o acesso à API do GitHub  

3. **Falha na Conexão**  
   - Confirme que o servidor está a ser executado na porta esperada  
   - Verifique as definições do firewall  
   - Certifique-se de que o ambiente Python possui os pacotes necessários  

## Verificação da Conexão

O seu servidor MCP está devidamente conectado quando:  
1. A consola exibe "Configuração do plugin GitHub concluída com sucesso"  
2. Os registos de conexão mostram "✓ MCP Connection Status: Active"  
3. Os comandos do GitHub funcionam na interface de chat  

## Variáveis de Ambiente

Necessárias no seu ficheiro .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testar a Conexão

Envie esta mensagem de teste no chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Uma resposta bem-sucedida exibirá informações do repositório.  

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.