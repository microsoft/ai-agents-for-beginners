# Exemplo do Servidor MCP do GitHub

## Descrição

Esta foi uma demonstração criada para o AI Agents Hackathon organizada pelo Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios do Github de um usuário.
Isso é feito por:

1. **Github Agent** - Usando o Servidor MCP do Github para recuperar repositórios e informações sobre esses repositórios.
2. **Hackathon Agent** - Recebe os dados do Github Agent e cria ideias criativas de projetos de hackathon com base nos projetos, nas linguagens usadas pelo usuário e nas trilhas do projeto para o AI Agents hackathon.
3. **Events Agent** - Com base nas sugestões do Hackathon Agent, o Events Agent recomendará eventos relevantes da série AI Agent Hackathon.
## Executando o código 

### Variáveis de Ambiente

Esta demonstração usa o Microsoft Agent Framework, Azure OpenAI Service, o Servidor MCP do Github e o Azure AI Search.

Certifique-se de que você tenha as variáveis de ambiente corretas definidas para usar essas ferramentas:

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

Isto deve iniciar seu servidor Chainlit em `localhost:8000` além de preencher seu índice do Azure AI Search com o conteúdo de `event-descriptions.md`. 

## Conectando ao Servidor MCP

Para se conectar ao Servidor MCP do Github, selecione o ícone "plug" abaixo da caixa de chat "Type your message here..":

![Conectar MCP](../../../../../translated_images/pt-BR/mcp-chainlit-1.7ed66d648e3cfb28.webp)

A partir daí você pode clicar em "Conectar um MCP" para adicionar o comando para conectar ao Servidor MCP do Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Token de Acesso Pessoal real. 

Após conectar, você deverá ver um (1) ao lado do ícone plug para confirmar que está conectado. Se não, tente reiniciar o servidor chainlit com `chainlit run app.py -w`.

## Usando a Demonstração 

Para iniciar o fluxo de trabalho dos agentes de recomendação de projetos de hackathon, você pode digitar uma mensagem como: 

"Recomende projetos de hackathon para o usuário do Github koreyspace"

O Router Agent analisará sua solicitação e determinará qual combinação de agentes (GitHub, Hackathon e Events) é mais adequada para lidar com sua consulta. Os agentes trabalham juntos para fornecer recomendações abrangentes com base na análise de repositórios do GitHub, geração de ideias de projetos e eventos tecnológicos relevantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido usando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original, em seu idioma nativo, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->