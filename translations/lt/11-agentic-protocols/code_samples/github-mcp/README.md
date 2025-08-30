<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T10:30:32+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "lt"
}
-->
# Github MCP Server Pavyzdys

## Aprašymas

Tai yra demonstracinis projektas, sukurtas AI Agentų hakatonui, organizuotam per Microsoft Reactor.

Įrankis naudojamas rekomenduoti hakatono projektus pagal vartotojo Github saugyklas. Tai atliekama:

1. **Github agentas** - Naudojant Github MCP serverį, gaunamos saugyklos ir informacija apie jas.
2. **Hakatono agentas** - Naudojant duomenis iš Github agento, sukuriamos kūrybinės hakatono projektų idėjos, remiantis vartotojo projektais, naudojamomis programavimo kalbomis ir AI Agentų hakatono projektų kryptimis.
3. **Renginių agentas** - Remiantis hakatono agento pasiūlymais, renginių agentas rekomenduoja aktualius renginius iš AI Agentų hakatono serijos.

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

## Chainlit serverio paleidimas

Norint prisijungti prie MCP serverio, šiame demonstraciniame projekte naudojamas Chainlit kaip pokalbių sąsaja.

Norėdami paleisti serverį, terminale naudokite šią komandą:

```bash
chainlit run app.py -w
```

Tai turėtų paleisti jūsų Chainlit serverį `localhost:8000` ir užpildyti jūsų Azure AI Search indeksą su `event-descriptions.md` turiniu.

## Prisijungimas prie MCP serverio

Norėdami prisijungti prie Github MCP serverio, pasirinkite „kištuko“ piktogramą po „Įveskite savo žinutę čia..“ pokalbių laukeliu:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.lt.png)

Iš ten galite spustelėti „Prisijungti prie MCP“, kad pridėtumėte komandą prisijungti prie Github MCP serverio:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Pakeiskite "[YOUR PERSONAL ACCESS TOKEN]" savo asmeniniu prieigos raktu.

Po prisijungimo turėtumėte matyti (1) šalia kištuko piktogramos, patvirtinančio, kad prisijungta. Jei ne, pabandykite iš naujo paleisti Chainlit serverį su `chainlit run app.py -w`.

## Demonstracijos naudojimas

Norėdami pradėti agentų darbo eigą, rekomenduojančią hakatono projektus, galite įvesti tokią žinutę:

„Rekomenduok hakatono projektus Github vartotojui koreyspace“

Maršruto agentas analizuos jūsų užklausą ir nustatys, kuri agentų kombinacija (GitHub, Hakatono ir Renginių) geriausiai tinka jūsų užklausai spręsti. Agentai dirbs kartu, kad pateiktų išsamias rekomendacijas, remiantis Github saugyklų analize, projektų idėjomis ir aktualiais technologijų renginiais.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.