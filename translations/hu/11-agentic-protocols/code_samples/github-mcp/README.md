<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:22:40+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "hu"
}
-->
# Github MCP Server Példa

## Leírás

Ez egy demó, amelyet a Microsoft Reactor által szervezett AI Agents Hackathonra készítettek.

Az eszköz célja, hogy hackathon projektek ajánlásával segítse a felhasználókat a Github repóik alapján. Ez a következőképpen működik:

1. **Github Agent** - A Github MCP Server segítségével lekéri a repókat és azok adatait.
2. **Hackathon Agent** - A Github Agent által gyűjtött adatok alapján kreatív hackathon projektötleteket javasol, figyelembe véve a felhasználó projektjeit, használt programozási nyelveit és az AI Agents hackathon projektpályáit.
3. **Events Agent** - A Hackathon Agent javaslatai alapján az Events Agent releváns eseményeket ajánl az AI Agents Hackathon sorozatból.

## A kód futtatása

### Környezeti változók

Ez a demó az Azure Open AI Service-t, a Semantic Kernel-t, a Github MCP Server-t és az Azure AI Search-t használja.

Győződj meg róla, hogy a megfelelő környezeti változók be vannak állítva ezekhez az eszközökhöz:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## A Chainlit Server futtatása

A MCP serverhez való csatlakozáshoz ez a demó a Chainlit-et használja chat interfészként.

A szerver futtatásához használd az alábbi parancsot a terminálban:

```bash
chainlit run app.py -w
```

Ez elindítja a Chainlit szervert a `localhost:8000` címen, és feltölti az Azure AI Search Indexet az `event-descriptions.md` tartalmával.

## Csatlakozás az MCP Serverhez

A Github MCP Serverhez való csatlakozáshoz kattints a "dugó" ikonra a "Írd be az üzeneted ide..." chat mező alatt:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.hu.png)

Ezután kattints a "Connect an MCP" gombra, hogy hozzáadd a parancsot a Github MCP Serverhez való csatlakozáshoz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Cseréld le a "[YOUR PERSONAL ACCESS TOKEN]" szöveget a saját személyes hozzáférési tokenedre.

A csatlakozás után egy (1) jelenik meg a dugó ikon mellett, jelezve, hogy sikeresen csatlakoztál. Ha nem, próbáld újraindítani a Chainlit szervert a `chainlit run app.py -w` parancs segítségével.

## A demó használata

A hackathon projektek ajánlására szolgáló agent workflow elindításához írhatsz egy üzenetet, például:

"Ajánlj hackathon projekteket a koreyspace Github felhasználónak"

A Router Agent elemzi a kérésedet, és meghatározza, hogy melyik agentek kombinációja (GitHub, Hackathon és Events) a legalkalmasabb a kérdésed kezelésére. Az agentek együttműködve átfogó ajánlásokat nyújtanak a Github repók elemzése, projektötletek kidolgozása és releváns technológiai események alapján.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.