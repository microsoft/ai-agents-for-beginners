# Github MCP Server пример

## Опис

Ово је демо креиран за AI Agents Hackathon који је организовао Microsoft Reactor.

Овај алат се користи за препоруку пројеката за хакатон на основу Github репозиторијума корисника. То се ради на следећи начин:

1. **Github Agent** - Користи Github MCP Server за преузимање репозиторијума и информација о тим репозиторијумима.
2. **Hackathon Agent** - Узима податке од Github Agent и осмишљава креативне идеје за хакатонске пројекте на основу пројеката, језика које корисник користи и категорија пројеката за AI Agents хакатон.
3. **Events Agent** - На основу предлога Hackathon Agent, Events Agent ће препоручити релевантне догађаје из серије AI Agent Hackathon.

## Покретање кода 

### Променљиве окружења

Овај демо користи Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server и Azure AI Search.

Уверите се да сте подесили одговарајуће променљиве окружења да бисте користили ове алате:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Покретање Chainlit сервера

Да би се повезао са MCP сервером, овај демо користи Chainlit као чат интерфејс. 

Да покренете сервер, користите следећу команду у терминалу:

```bash
chainlit run app.py -w
```

Ово би требало да покрене ваш Chainlit сервер на `localhost:8000` као и да попуни ваш Azure AI Search индекс садржајем `event-descriptions.md`. 

## Повезивање са MCP сервером

Да бисте се повезали са Github MCP Server-ом, изаберите икону "plug" испод поља за ћаскање "Type your message here..":

![MCP Повезивање](../../../../../translated_images/sr/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Одатле можете кликнути на "Connect an MCP" да додате команду за повезивање са Github MCP Server-ом:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

Након повезивања, требало би да видите (1) поред иконе plug да потврдите да је повезано. У супротном, покушајте да рестартујете chainlit сервер са `chainlit run app.py -w`.

## Коришћење демо-а 

Да бисте покренули ток рада агената за препоруку хакатонских пројеката, можете унети поруку попут: 

"Препоручи хакатонске пројекте за Github корисника koreyspace"

Router Agent ће анализирати ваш захтев и одредити која комбинација агената (GitHub, Hackathon, and Events) је најбоље погодна да обради ваш упит. Агенти раде заједно да пруже свеобухватне препоруке засноване на анализи GitHub репозиторијума, осмишљавању пројеката и релевантним технолошким догађајима.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Одрицање одговорности:
Овај документ је преведен помоћу услуге за превођење на бази вештачке интелигенције Co‑op Translator (https://github.com/Azure/co-op-translator). Иако настојимо да будемо прецизни, имајте у виду да аутоматски преводи могу да садрже грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати коначним и обавезујућим извором. За критичне информације препоручује се професионални, људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која произилазе из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->