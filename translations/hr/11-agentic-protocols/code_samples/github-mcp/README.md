# Github MCP Server Primjer

## Opis

Ovo je demo kreiran za AI Agents Hackathon organiziran kroz Microsoft Reactor.

Alat se koristi za preporuku hackathon projekata na temelju korisničkih Github repozitorija.  
To se postiže putem:

1. **Github Agent** - Koristi Github MCP Server za dohvaćanje repozitorija i informacija o tim repozitorijima.  
2. **Hackathon Agent** - Preuzima podatke od Github Agenta i osmišljava kreativne ideje za hackathon projekte temeljene na projektima, jezicima koje korisnik koristi i projektnih smjerovima za AI Agents hackathon.  
3. **Events Agent** - Na temelju prijedloga hackathon agenta, Events Agent preporučuje relevantne događaje iz serije AI Agent Hackathona.  

## Pokretanje koda

### Varijable okoline

Ovaj demo koristi Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server i Azure AI Search.

Pobrinite se da imate pravilno postavljene varijable okoline za korištenje ovih alata:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 
  
## Pokretanje Chainlit Servera

Za povezivanje s MCP serverom, ovaj demo koristi Chainlit kao sučelje za chat.

Za pokretanje servera, u terminal unesite sljedeću naredbu:

```bash
chainlit run app.py -w
```
  
Time bi se trebao pokrenuti vaš Chainlit server na `localhost:8000` te također popuniti Azure AI Search indeks s sadržajem datoteke `event-descriptions.md`.

## Povezivanje na MCP Server

Za povezivanje na Github MCP Server, kliknite na ikonu "utikača" ispod unosa za chat "Type your message here..":

![MCP Connect](../../../../../translated_images/hr/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Odatle možete kliknuti na "Connect an MCP" kako biste dodali naredbu za povezivanje na Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```
  
Zamijenite "[YOUR PERSONAL ACCESS TOKEN]" vašim stvarnim Personal Access Tokenom.

Nakon povezivanja, trebali biste vidjeti (1) pored ikone utikača kao potvrdu da je povezano. Ako nije, pokušajte ponovno pokrenuti chainlit server s `chainlit run app.py -w`.

## Korištenje demo-a

Za pokretanje rada agenta za preporuku hackathon projekata, možete upisati poruku poput:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent će analizirati vaš zahtjev i odrediti koja kombinacija agenata (GitHub, Hackathon i Events) je najbolje prilagođena za obradu vašeg upita. Agenti surađuju kako bi pružili sveobuhvatne preporuke na temelju analize Github repozitorija, osmišljavanja projekata i relevantnih tech događaja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->