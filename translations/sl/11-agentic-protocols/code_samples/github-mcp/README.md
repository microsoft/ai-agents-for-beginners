<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T10:29:58+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "sl"
}
-->
# Github MCP Server Primer

## Opis

To je bil demo, ustvarjen za Hackathon AI Agents, ki ga je gostil Microsoft Reactor.

Orodje se uporablja za priporočanje projektov za hackathon na podlagi uporabnikovih Github repozitorijev. To se doseže z:

1. **Github Agent** - Uporaba Github MCP strežnika za pridobivanje repozitorijev in informacij o teh repozitorijih.
2. **Hackathon Agent** - Uporablja podatke iz Github Agenta in predlaga kreativne ideje za hackathon projekte na podlagi projektov, programskih jezikov, ki jih uporablja uporabnik, ter tematskih sklopov za hackathon AI Agents.
3. **Events Agent** - Na podlagi predlogov Hackathon Agenta bo Events Agent priporočil ustrezne dogodke iz serije AI Agent Hackathon.

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

To bi moralo zagnati vaš Chainlit strežnik na `localhost:8000` ter napolniti vaš Azure AI Search Index z vsebino datoteke `event-descriptions.md`.

## Povezava z MCP strežnikom

Za povezavo z Github MCP strežnikom kliknite na ikono "vtič" pod poljem "Type your message here.." v klepetu:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.sl.png)

Od tam lahko kliknete na "Connect an MCP", da dodate ukaz za povezavo z Github MCP strežnikom:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamenjajte "[YOUR PERSONAL ACCESS TOKEN]" z vašim dejanskim osebnim dostopnim žetonom.

Ko se povežete, bi morali videti (1) poleg ikone vtiča, kar potrjuje povezavo. Če ne, poskusite znova zagnati Chainlit strežnik z ukazom `chainlit run app.py -w`.

## Uporaba demo aplikacije 

Za začetek delovnega toka agenta, ki priporoča projekte za hackathon, lahko vnesete sporočilo, kot je:

"Priporoči projekte za hackathon za Github uporabnika koreyspace"

Router Agent bo analiziral vašo zahtevo in določil, katera kombinacija agentov (GitHub, Hackathon in Events) je najbolj primerna za obravnavo vašega vprašanja. Agenti sodelujejo, da zagotovijo celovita priporočila na podlagi analize Github repozitorijev, idej za projekte in ustreznih tehnoloških dogodkov.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.