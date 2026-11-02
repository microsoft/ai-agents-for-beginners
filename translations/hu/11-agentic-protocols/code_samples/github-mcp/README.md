# Github MCP Szerver Példa

## Leírás

Ez egy demó volt, amelyet az AI Agents Hackathonra készítettek, amelyet a Microsoft Reactor szervezett.

Az eszköz arra szolgál, hogy hackathon projekteket ajánljon egy felhasználó Github repozitóriumai alapján.
Ez a következőképpen történik:

1. **Github Ügynök** – A Github MCP Szerver használata a repozitóriumok és az azokkal kapcsolatos információk lekérésére.
2. **Hackathon Ügynök** – Átveszi az adatokat a Github Ügynöktől, és kreatív hackathon projektötleteket dolgoz ki a projektek, a felhasználó által használt nyelvek és az AI Agents hackathon projektjei alapján.
3. **Esemény Ügynök** – A hackathon ügynök javaslata alapján az esemény ügynök releváns eseményeket ajánl az AI Agent Hackathon sorozatból.

## A kód futtatása

### Környezeti változók

Ez a demó a Microsoft Agent Frameworköt, Azure OpenAI Szolgáltatást, a Github MCP Szervert és az Azure AI Keresést használja.

Győződj meg róla, hogy a megfelelő környezeti változók be vannak állítva ezen eszközök használatához:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## A Chainlit Szerver futtatása

Az MCP szerverhez való kapcsolódáshoz ez a demó a Chainlit chat felületet használja.

A szerver futtatásához használd a következő parancsot a terminálodban:

```bash
chainlit run app.py -w
```


Ez elindítja a Chainlit szerveredet a `localhost:8000` címen, valamint feltölti az Azure AI Keresési Indexedet az `event-descriptions.md` tartalommal.

## Kapcsolódás az MCP Szerverhez

A Github MCP Szerverhez való kapcsolódáshoz válaszd ki a „plug” ikont a „Type your message here..” chat mező alatt:

![MCP Connect](../../../../../translated_images/hu/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Innen kattinthatsz a „Connect an MCP” gombra, hogy hozzáadd a parancsot a Github MCP Szerverhez való kapcsolódáshoz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Cseréld ki a "[YOUR PERSONAL ACCESS TOKEN]" szöveget a saját Személyes Hozzáférési Tokenedre.

A kapcsolódás után a „plug” ikon mellett egy (1) jelenik meg, amely megerősíti a kapcsolatot. Ha nem látod, próbáld meg újraindítani a chainlit szervert a `chainlit run app.py -w` paranccsal.

## A demó használata

A hackathon projektek ajánlását indító ügynök munkafolyamat elindításához írhatsz egy üzenetet, például:

„Ajánlj hackathon projekteket a koreyspace Github felhasználónak”

A Router Ügynök elemezni fogja a kérésedet, és meghatározza, hogy az ügynökök (GitHub, Hackathon és Események) mely kombinációja a legalkalmasabb a lekérdezésed kezelésére. Az ügynökök együttműködve átfogó ajánlásokat nyújtanak a GitHub repozitórium elemzése, a projektötletelés és a releváns tech események alapján.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. A dokumentum eredeti nyelvű változata tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amelyek a fordítás használatából erednek.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->