<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:51:34+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "lt"
}
-->
# Github MCP Server Pavyzdys

## Aprašymas

Tai yra demonstracinis projektas, sukurtas AI Agentų Hackathon renginiui, organizuotam per Microsoft Reactor.

Įrankis naudojamas rekomenduoti hackathon projektus, remiantis vartotojo Github saugyklomis. Tai atliekama:

1. **Github Agentas** - Naudojant Github MCP Serverį, siekiant gauti saugyklas ir informaciją apie jas.
2. **Hackathon Agentas** - Naudoja duomenis iš Github Agento ir sukuria kūrybingas hackathon projektų idėjas, remdamasis vartotojo projektais, naudojamomis programavimo kalbomis ir AI Agentų hackathon projektų temomis.
3. **Renginių Agentas** - Remdamasis Hackathon agento pasiūlymais, renginių agentas rekomenduoja aktualius renginius iš AI Agentų Hackathon serijos.

## Kodo paleidimas

### Aplinkos kintamieji

Šiame demonstraciniame projekte naudojamos Azure Open AI Service, Semantic Kernel, Github MCP Server ir Azure AI Search.

Įsitikinkite, kad turite tinkamai nustatytus aplinkos kintamuosius, kad galėtumėte naudoti šiuos įrankius:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Serverio paleidimas

Norint prisijungti prie MCP serverio, šiame demonstraciniame projekte naudojamas Chainlit kaip pokalbių sąsaja.

Norėdami paleisti serverį, terminale naudokite šią komandą:

```bash
chainlit run app.py -w
```

Tai turėtų paleisti jūsų Chainlit serverį `localhost:8000` ir užpildyti jūsų Azure AI Search indeksą su `event-descriptions.md` turiniu.

## Prisijungimas prie MCP Serverio

Norėdami prisijungti prie Github MCP Serverio, pasirinkite „kištuko“ ikoną po „Įveskite savo žinutę čia..“ pokalbių laukeliu:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.lt.png)

Iš ten galite spustelėti „Prisijungti prie MCP“, kad pridėtumėte komandą prisijungti prie Github MCP Serverio:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Pakeiskite "[YOUR PERSONAL ACCESS TOKEN]" savo asmeniniu prieigos raktu.

Po prisijungimo turėtumėte matyti (1) šalia kištuko ikonos, patvirtinant, kad prisijungta. Jei ne, pabandykite iš naujo paleisti Chainlit serverį su `chainlit run app.py -w`.

## Demonstracijos naudojimas

Norėdami pradėti agentų darbo eigą, rekomenduojančią hackathon projektus, galite įvesti tokią žinutę:

„Rekomenduok hackathon projektus Github vartotojui koreyspace“

Maršrutizavimo agentas analizuos jūsų užklausą ir nustatys, kuri agentų kombinacija (GitHub, Hackathon ir Renginių) geriausiai tinka jūsų užklausai. Agentai dirbs kartu, kad pateiktų išsamias rekomendacijas, remdamiesi Github saugyklų analize, projektų idėjomis ir aktualiais technologijų renginiais.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.