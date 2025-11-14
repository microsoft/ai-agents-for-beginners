<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T13:30:40+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "br"
}
-->
# Github MCP Server Exemplo

## Descrição

Este foi um demo criado para o Hackathon de Agentes de IA organizado pelo Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios do Github de um usuário. Isso é feito por meio de:

1. **Agente Github** - Utilizando o Github MCP Server para recuperar repositórios e informações sobre esses repositórios.
2. **Agente Hackathon** - Usa os dados do Agente Github para criar ideias criativas de projetos de hackathon com base nos projetos, linguagens utilizadas pelo usuário e nas trilhas de projeto do hackathon de Agentes de IA.
3. **Agente Eventos** - Com base na sugestão do agente hackathon, o agente de eventos recomendará eventos relevantes da série de hackathons de Agentes de IA.

## Executando o código 

### Variáveis de Ambiente

Este demo utiliza Azure Open AI Service, Semantic Kernel, o Github MCP Server e Azure AI Search.

Certifique-se de que você tenha as variáveis de ambiente adequadas configuradas para usar essas ferramentas:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Executando o Servidor Chainlit

Para se conectar ao servidor MCP, este demo utiliza o Chainlit como interface de chat.

Para executar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```

Isso deve iniciar seu servidor Chainlit em `localhost:8000`, além de preencher seu Azure AI Search Index com o conteúdo de `event-descriptions.md`.

## Conectando ao Servidor MCP

Para se conectar ao Github MCP Server, selecione o ícone de "plug" abaixo da caixa de texto "Digite sua mensagem aqui...":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.br.png)

A partir daí, você pode clicar em "Connect an MCP" para adicionar o comando que conecta ao Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Personal Access Token real.

Após conectar, você deverá ver um (1) ao lado do ícone de plug para confirmar que está conectado. Caso contrário, tente reiniciar o servidor Chainlit com `chainlit run app.py -w`.

## Usando o Demo 

Para iniciar o fluxo de trabalho do agente recomendando projetos de hackathon, você pode digitar uma mensagem como:

"Recomende projetos de hackathon para o usuário do Github koreyspace"

O Router Agent analisará sua solicitação e determinará qual combinação de agentes (GitHub, Hackathon e Eventos) é mais adequada para lidar com sua consulta. Os agentes trabalham juntos para fornecer recomendações abrangentes com base na análise de repositórios do Github, ideação de projetos e eventos tecnológicos relevantes.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.