# Primer Github MCP strežnika

## Opis

To je bila predstavitvena različica ustvarjena za AI Agents Hackathon, ki ga je gostil Microsoft Reactor.

Orodje se uporablja za priporočanje projektov za hackathon glede na uporabnikove Github repozitorije.
To se izvaja z:

1. **Github Agent** - Uporaba Github MCP Serverja za pridobivanje repozitorijev in informacij o teh repozitorijih.
2. **Hackathon Agent** - Prevzame podatke od Github Agenta in iz njih ustvari ustvarjalne ideje za hackathon projekte glede na projekte, jezike, ki jih uporablja uporabnik, in projektne smernice za AI Agents hackathon.
3. **Events Agent** - Na podlagi predlogov hackathon agenta, events agent priporoči ustrezne dogodke iz serije AI Agent Hackathon.
## Zagon kode 

### Spremenljivke okolja

Ta demo uporablja Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server in Azure AI Search.

Prepričajte se, da imate nastavljene ustrezne spremenljivke okolja za uporabo teh orodij:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Zagon Chainlit strežnika

Za povezavo s MCP strežnikom ta demo uporablja Chainlit kot klepetalni vmesnik. 

Za zagon strežnika uporabite naslednji ukaz v terminalu:

```bash
chainlit run app.py -w
```

To bi moralo zagnati vaš Chainlit strežnik na `localhost:8000` in tudi napolniti vaš Azure AI Search Index z vsebino `event-descriptions.md`. 

## Povezava s MCP strežnikom

Za povezavo s Github MCP Serverjem izberite ikono "vtič" pod vnosnim poljem za klepet "Type your message here..":

![Povezava MCP](../../../../../translated_images/sl/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Od tam lahko kliknete na "Connect an MCP", da dodate ukaz za povezavo z Github MCP Serverjem:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamenjajte "[YOUR PERSONAL ACCESS TOKEN]" z vašim dejanskim Personal Access Tokenom. 

Po povezavi bi morali poleg ikone vtiča videti (1), kar potrjuje, da je povezava vzpostavljena. Če ne, poskusite znova zagnati chainlit strežnik z `chainlit run app.py -w`.

## Uporaba demoja 

Za zagon delovnega toka agentov, ki priporočajo hackathon projekte, lahko vnesete sporočilo, kot na primer: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent bo analiziral vašo zahtevo in določil, katera kombinacija agentov (GitHub, Hackathon in Events) je najbolj primerna za obravnavo vaše poizvedbe. Agenti sodelujejo, da zagotovijo obsežna priporočila na osnovi analize GitHub repozitorijev, idej za projekte in ustreznih tehnoloških dogodkov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden s pomočjo storitve za prevajanje z uporabo umetne inteligence Co-op Translator (https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za kakršnekoli nesporazume ali napačne interpretacije, ki bi izhajale iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->