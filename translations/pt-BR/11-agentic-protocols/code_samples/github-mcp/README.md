# Exemplo do Servidor MCP do Github

## Descrição

Esta foi uma demonstração criada para o AI Agents Hackathon organizado pelo Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios do Github de um usuário.
Isto é feito por:

1. **Agente do Github** - Usando o Github MCP Server para recuperar repositórios e informações sobre esses repositórios.
2. **Agente Hackathon** - Recebe os dados do Agente do Github e cria ideias criativas de projetos para o hackathon com base nos projetos, nas linguagens usadas pelo usuário e nas trilhas de projeto do AI Agents hackathon.
3. **Agente de Eventos** - Com base na sugestão do agente de hackathon, o agente de eventos recomendará eventos relevantes da série AI Agent Hackathon.
## Executando o código 

### Variáveis de Ambiente

Esta demonstração usa o Microsoft Agent Framework, Azure OpenAI Service, o Github MCP Server e o Azure AI Search.

Certifique-se de que você tenha as variáveis de ambiente apropriadas configuradas para usar essas ferramentas:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Executando o Servidor Chainlit

Para se conectar ao servidor MCP, esta demonstração usa o Chainlit como interface de chat. 

Para executar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```

Isso deve iniciar seu servidor Chainlit em `localhost:8000`, além de popular seu Índice do Azure AI Search com o conteúdo de `event-descriptions.md`. 

## Conectando-se ao Servidor MCP

Para conectar ao Github MCP Server, selecione o ícone "plug" abaixo da caixa de chat "Type your message here..":

![Conectar MCP](../../../../../translated_images/pt-BR/mcp-chainlit-1.7ed66d648e3cfb28.webp)

A partir daí você pode clicar em "Connect an MCP" para adicionar o comando de conexão ao Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Personal Access Token real. 

Após conectar, você deve ver um (1) ao lado do ícone plug para confirmar que está conectado. Se não, tente reiniciar o servidor chainlit com `chainlit run app.py -w`.

## Usando a Demonstração 

Para iniciar o fluxo de trabalho de agentes para recomendar projetos de hackathon, você pode digitar uma mensagem como: 

"Recomende projetos de hackathon para o usuário do Github koreyspace"

O Agente de Roteamento analisará sua solicitação e determinará qual combinação de agentes (Github, Hackathon e Eventos) é mais adequada para lidar com sua consulta. Os agentes trabalham juntos para fornecer recomendações abrangentes com base na análise dos repositórios do GitHub, ideação de projetos e eventos tecnológicos relevantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original, no seu idioma nativo, deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->