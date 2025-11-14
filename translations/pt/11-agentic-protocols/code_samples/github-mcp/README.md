<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:51:10+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "pt"
}
-->
# Exemplo de Servidor MCP do Github

## Descrição

Este foi um demo criado para o Hackathon de Agentes de IA organizado pelo Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios do Github de um utilizador. Isto é feito através de:

1. **Agente do Github** - Utiliza o Servidor MCP do Github para obter repositórios e informações sobre esses repositórios.
2. **Agente de Hackathon** - Usa os dados do Agente do Github para criar ideias criativas de projetos de hackathon com base nos projetos, nas linguagens utilizadas pelo utilizador e nas categorias de projetos do hackathon de Agentes de IA.
3. **Agente de Eventos** - Com base na sugestão do agente de hackathon, o agente de eventos recomendará eventos relevantes da série de hackathons de Agentes de IA.

## Executar o código

### Variáveis de Ambiente

Este demo utiliza o Azure Open AI Service, o Semantic Kernel, o Servidor MCP do Github e o Azure AI Search.

Certifique-se de que tem as variáveis de ambiente adequadas configuradas para usar estas ferramentas:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Executar o Servidor Chainlit

Para se conectar ao servidor MCP, este demo utiliza o Chainlit como interface de chat.

Para executar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```

Isto deverá iniciar o seu servidor Chainlit em `localhost:8000`, bem como preencher o seu Azure AI Search Index com o conteúdo do ficheiro `event-descriptions.md`.

## Conectar-se ao Servidor MCP

Para se conectar ao Servidor MCP do Github, selecione o ícone de "plug" abaixo da caixa de chat "Escreva a sua mensagem aqui...":

![Conectar MCP](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.pt.png)

A partir daí, pode clicar em "Connect an MCP" para adicionar o comando que conecta ao Servidor MCP do Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Personal Access Token real.

Depois de se conectar, deverá ver um (1) ao lado do ícone de plug para confirmar que está conectado. Caso contrário, tente reiniciar o servidor Chainlit com `chainlit run app.py -w`.

## Usar o Demo

Para iniciar o fluxo de trabalho do agente que recomenda projetos de hackathon, pode escrever uma mensagem como:

"Recomenda projetos de hackathon para o utilizador do Github koreyspace"

O Agente Router analisará o seu pedido e determinará qual a combinação de agentes (Github, Hackathon e Eventos) mais adequada para lidar com a sua consulta. Os agentes trabalham em conjunto para fornecer recomendações abrangentes com base na análise dos repositórios do Github, na criação de ideias de projetos e em eventos tecnológicos relevantes.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.