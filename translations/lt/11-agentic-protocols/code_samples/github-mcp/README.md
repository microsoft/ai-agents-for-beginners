# Github MCP serverio pavyzdys

## Aprašymas

Tai buvo demonstracija sukurta AI Agentų hakatonui, rengtam per Microsoft Reactor.

Šis įrankis naudojamas rekomenduoti hakatono projektus pagal vartotojo Github repozitorijas.
Tai daroma taip:

1. **Github Agent** - Naudoja Github MCP serverį, kad gautų repozitorijas ir informaciją apie tas repozitorijas.
2. **Hackathon Agent** - Ima duomenis iš Github Agent ir sugalvoja kūrybingas hakatono projektų idėjas, remdamasis projektais, vartotojo naudojamomis programavimo kalbomis ir AI Agentų hakatono projekto takais.
3. **Events Agent** - Remdamasis hackathon agento pasiūlymais, events agent rekomenduos tinkamus renginius iš AI Agentų hakatono serijos.

## Kodo paleidimas 

### Aplinkos kintamieji

Ši demonstracija naudoja Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server ir Azure AI Search.

Įsitikinkite, kad turite tinkamai nustatytus aplinkos kintamuosius, kad galėtumėte naudoti šiuos įrankius:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit serverio paleidimas

Norėdami prisijungti prie MCP serverio, ši demonstracija naudoja Chainlit kaip pokalbio sąsają. 

Norėdami paleisti serverį, savo terminale naudokite šią komandą:

```bash
chainlit run app.py -w
```

Tai turėtų paleisti jūsų Chainlit serverį adresu `localhost:8000`, taip pat užpildyti jūsų Azure AI Search indeksą su `event-descriptions.md` turiniu. 

## Prisijungimas prie MCP serverio

Norėdami prisijungti prie Github MCP Server, pasirinkite „plug“ piktogramą po pokalbio laukeliu "Type your message here..":

![MCP prisijungimas](../../../../../translated_images/lt/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Iš ten galite spustelėti „Connect an MCP“, kad pridėtumėte komandą prisijungti prie Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Pakeiskite "[YOUR PERSONAL ACCESS TOKEN]" savo tikruoju asmeniniu prieigos raktu. 

Prisijungus, šalia plug piktogramos turėtumėte pamatyti (1), patvirtinantį, kad jis prisijungęs. Jei ne, pabandykite perkrauti chainlit serverį su `chainlit run app.py -w`.

## Demonstracijos naudojimas 

Norėdami pradėti agentų darbo eigą, kuri rekomenduoja hakatono projektus, galite įrašyti žinutę, pavyzdžiui: 

" Pasiūlykite hakatono projektus Github naudotojui koreyspace"

Router Agent analizuos jūsų užklausą ir nustatys, kuri agentų kombinacija (GitHub, Hackathon ir Events) geriausiai tinka jūsų užklausai apdoroti. Agentai bendradarbiauja, kad pateiktų išsamaus pobūdžio rekomendacijas, paremtas GitHub saugyklų analize, projekto idėjų kūrimu ir susijusiais technologijų renginiais.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingas interpretacijas, kilusias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->