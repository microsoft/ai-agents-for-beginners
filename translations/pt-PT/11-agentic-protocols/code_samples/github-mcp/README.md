# Exemplo de Servidor MCP do Github

## Descrição

Esta foi uma demonstração criada para o AI Agents Hackathon organizado através do Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios do Github de um utilizador.
Isto é feito através de:

1. **Agente do Github** - Usando o Servidor MCP do Github para obter repositórios e informações sobre esses repositórios.
2. **Agente do Hackathon** - Recebe os dados do Agente do Github e cria ideias criativas para projetos de hackathon baseados nos projetos, nas linguagens usadas pelo utilizador e nas categorias de projeto para o AI Agents hackathon.
3. **Agente dos Eventos** - Com base na sugestão do agente do hackathon, o agente dos eventos irá recomendar eventos relevantes da série AI Agent Hackathon.

## Executar o código

### Variáveis de Ambiente

Esta demonstração usa o Microsoft Agent Framework, Azure OpenAI Service, o Servidor MCP do Github e Azure AI Search.

Certifique-se de que tem as variáveis de ambiente corretas definidas para usar estas ferramentas:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Executar o Servidor Chainlit

Para conectar ao servidor MCP, esta demo usa o Chainlit como uma interface de chat.

Para executar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```


Isto deverá iniciar o seu servidor Chainlit em `localhost:8000` assim como popular o seu Índice de Pesquisa do Azure AI com o conteúdo de `event-descriptions.md`.

## Conectar ao Servidor MCP

Para conectar ao Servidor MCP do Github, selecione o ícone "plug" por baixo da caixa de chat "Type your message here..":

![MCP Connect](../../../../../translated_images/pt-PT/mcp-chainlit-1.7ed66d648e3cfb28.webp)

A partir daí pode clicar em "Connect an MCP" para adicionar o comando para ligar ao Servidor MCP do Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Token de Acesso Pessoal real.

Após conectar, deverá ver um (1) ao lado do ícone do plugue para confirmar que está ligado. Caso contrário, tente reiniciar o servidor chainlit com `chainlit run app.py -w`.

## Usar a Demonstração

Para iniciar o fluxo de trabalho do agente de recomendação de projetos de hackathon, pode escrever uma mensagem como:

"Recomenda projetos de hackathon para o utilizador Github koreyspace"

O Agente Router irá analisar o seu pedido e determinar qual a combinação de agentes (GitHub, Hackathon e Eventos) é a mais adequada para tratar da sua consulta. Os agentes trabalham em conjunto para fornecer recomendações abrangentes com base na análise dos repositórios do GitHub, ideação de projetos e eventos tecnológicos relevantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->