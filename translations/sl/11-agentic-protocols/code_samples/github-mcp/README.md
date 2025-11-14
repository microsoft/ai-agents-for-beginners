<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T00:19:01+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "sl"
}
-->
# Github MCP Server Primer

## Opis

To je bil demo, ustvarjen za Hackathon AI Agents, ki ga je gostil Microsoft Reactor.

Orodje se uporablja za priporočanje hackathon projektov na podlagi uporabnikovih Github repozitorijev. To se doseže z:

1. **Github Agent** - Uporablja Github MCP Server za pridobivanje repozitorijev in informacij o teh repozitorijih.
2. **Hackathon Agent** - Uporablja podatke iz Github Agenta in predlaga kreativne ideje za hackathon projekte na podlagi projektov, uporabljenih programskih jezikov in tematskih sklopov za hackathon AI Agents.
3. **Events Agent** - Na podlagi predlogov Hackathon Agenta Events Agent priporoča ustrezne dogodke iz serije hackathonov AI Agents.

## Zagon kode

### Spremenljivke okolja

Ta demo uporablja Azure Open AI Service, Semantic Kernel, Github MCP Server in Azure AI Search.

Prepričajte se, da imate pravilno nastavljene spremenljivke okolja za uporabo teh orodij:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Zagon Chainlit strežnika

Za povezavo z MCP strežnikom ta demo uporablja Chainlit kot vmesnik za klepet.

Za zagon strežnika uporabite naslednji ukaz v terminalu:

```bash
chainlit run app.py -w
```

To bi moralo zagnati vaš Chainlit strežnik na `localhost:8000` in napolniti vaš Azure AI Search Index z vsebino iz `event-descriptions.md`.

## Povezava z MCP strežnikom

Za povezavo z Github MCP Serverjem kliknite na ikono "vtič" pod poljem za klepet "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.sl.png)

Od tam lahko kliknete na "Connect an MCP", da dodate ukaz za povezavo z Github MCP Serverjem:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamenjajte "[YOUR PERSONAL ACCESS TOKEN]" z vašim dejanskim osebnim dostopnim žetonom.

Ko se povežete, bi morali videti (1) poleg ikone vtiča, kar potrjuje, da je povezava vzpostavljena. Če ne, poskusite znova zagnati Chainlit strežnik z `chainlit run app.py -w`.

## Uporaba Dema

Za začetek delovnega toka agenta, ki priporoča hackathon projekte, lahko vnesete sporočilo, kot je:

"Priporoči hackathon projekte za Github uporabnika koreyspace"

Router Agent bo analiziral vašo zahtevo in določil, katera kombinacija agentov (GitHub, Hackathon in Events) je najbolj primerna za obravnavo vaše poizvedbe. Agenti sodelujejo, da zagotovijo celovita priporočila na podlagi analize Github repozitorijev, idej za projekte in ustreznih tehnoloških dogodkov.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.