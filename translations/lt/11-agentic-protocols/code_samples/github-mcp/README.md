# Github MCP Server pavyzdys

## Aprašymas

Tai demonstracija, sukurta AI Agents Hackathon renginiui, organizuotam Microsoft Reactor.

Šis įrankis naudojamas rekomenduoti hackathon projektus, remiantis vartotojo Github saugyklomis.
Tai atliekama taip:

1. **Github Agent** - Naudoja Github MCP Server, kad gautų repozitorijas ir informaciją apie jas.
2. **Hackathon Agent** - Paims duomenis iš Github Agent ir sukurs kūrybingas hackathon projektų idėjas remiantis projektais, vartotojo naudojamomis kalbomis ir AI Agents hackathon projekto kryptimis.
3. **Events Agent** - Remiantis Hackathon Agent pasiūlymais, Events Agent rekomenduos atitinkamus renginius iš AI Agent Hackathon serijos.
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

Norėdami prisijungti prie MCP serverio, ši demonstracija naudoja Chainlit kaip pokalbių sąsają. 

Norėdami paleisti serverį, naudokite šią komandą terminale:

```bash
chainlit run app.py -w
```

Tai turėtų paleisti jūsų Chainlit serverį adresu `localhost:8000`, taip pat užpildyti jūsų Azure AI Search indeksą su `event-descriptions.md` turiniu. 

## Prisijungimas prie MCP serverio

Norėdami prisijungti prie Github MCP Server, pasirinkite "plug" piktogramą po "Type your message here.." pokalbių laukeliu:

![Prisijungimas prie MCP](../../../../../translated_images/lt/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Iš ten galite paspausti "Connect an MCP", kad pridėtumėte komandą prisijungti prie Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Pakeiskite "[YOUR PERSONAL ACCESS TOKEN]" savo tikruoju Personal Access Token. 

Po prisijungimo, šalia plug piktogramos turėtumėte matyti (1), patvirtinantį, kad jis prijungtas. Jei ne, pabandykite iš naujo paleisti chainlit serverį su `chainlit run app.py -w`.

## Demonstracijos naudojimas 

Norėdami pradėti agentų darbo eigą, rekomenduojančią hackathon projektus, galite įvesti pranešimą, pvz.:

"Rekomenduokite hackathon projektus Github vartotojui koreyspace"

Router Agent išanalizuos jūsų užklausą ir nustatys, kuri agentų kombinacija (GitHub, Hackathon, ir Events) geriausiai tinka jūsų užklausai apdoroti. Agentai dirbs kartu, kad pateiktų išsamias rekomendacijas, remdamiesi GitHub saugyklų analize, projektų idėjų generavimu ir susijusiais technologijų renginiais.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas pradinėje kalboje turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojama pasitelkti profesionalų žmogaus vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->