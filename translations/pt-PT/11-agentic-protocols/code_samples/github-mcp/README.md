# Exemplo de Servidor MCP do Github

## Descrição

Esta foi uma demonstração criada para o AI Agents Hackathon organizado através do Microsoft Reactor.

A ferramenta é usada para recomendar projetos para hackathon com base nos repositórios do Github de um utilizador.
Isto é feito por:

1. **Agente do Github** - Usando o Servidor MCP do Github para recuperar repositórios e informações sobre esses repositórios.
2. **Agente do Hackathon** - Pega nos dados do Agente do Github e propõe ideias criativas de projetos para o hackathon com base nos projetos, nas linguagens usadas pelo utilizador e nas categorias de projeto para o AI Agents hackathon.
3. **Agente de Eventos** - Com base na sugestão do agente do hackathon, o agente de eventos recomendará eventos relevantes da série AI Agent Hackathon.

## Executar o código 

### Variáveis de Ambiente

Esta demo usa o Microsoft Agent Framework, Azure OpenAI Service, o Servidor MCP do Github e Azure AI Search.

Certifique-se de que tem as variáveis de ambiente corretas definidas para usar estas ferramentas:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Executar o Servidor Chainlit

Para ligar ao servidor MCP, esta demo usa o Chainlit como interface de chat. 

Para iniciar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```


Isto deverá iniciar o seu servidor Chainlit em `localhost:8000` assim como preencher o seu Índice Azure AI Search com o conteúdo do `event-descriptions.md`.

## Ligar ao Servidor MCP

Para ligar ao Servidor MCP do Github, selecione o ícone de "plug" em baixo da caixa de chat "Type your message here..":

![MCP Connect](../../../../../translated_images/pt-PT/mcp-chainlit-1.7ed66d648e3cfb28.webp)

A partir daí pode clicar em "Connect an MCP" para adicionar o comando para ligar ao Servidor MCP do Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Token de Acesso Pessoal real.

Depois de ligar, deverá ver um (1) ao lado do ícone de plug para confirmar que está ligado. Se não, tente reiniciar o servidor chainlit com `chainlit run app.py -w`.

## Usar a Demo 

Para iniciar o fluxo de trabalho do agente recomendando projetos para hackathon, pode escrever uma mensagem como: 

"Recommend hackathon projects for the Github user koreyspace"

O Agente Router vai analisar o seu pedido e determinar qual a combinação de agentes (GitHub, Hackathon, e Eventos) está melhor preparado para lidar com a sua consulta. Os agentes trabalham em conjunto para fornecer recomendações abrangentes baseadas na análise de repositórios GitHub, ideação de projetos e eventos tecnológicos relevantes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por qualquer mal-entendido ou interpretação incorreta decorrente da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->