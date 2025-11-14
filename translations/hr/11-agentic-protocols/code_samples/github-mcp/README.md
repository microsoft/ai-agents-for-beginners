<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T00:18:49+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "hr"
}
-->
# Github MCP Server Primjer

## Opis

Ovo je bio demo stvoren za AI Agents Hackathon koji je organizirao Microsoft Reactor.

Alat se koristi za preporuku hackathon projekata na temelju korisnikovih Github repozitorija. To se postiže putem:

1. **Github Agent** - Korištenjem Github MCP Servera za dohvaćanje repozitorija i informacija o tim repozitorijima.
2. **Hackathon Agent** - Uzima podatke od Github Agenta i osmišljava kreativne ideje za hackathon projekte na temelju projekata, jezika koje korisnik koristi i tema projekata za AI Agents hackathon.
3. **Events Agent** - Na temelju prijedloga Hackathon Agenta, Events Agent preporučuje relevantne događaje iz serije AI Agent Hackathon.

## Pokretanje koda

### Varijable okruženja

Ovaj demo koristi Azure Open AI Service, Semantic Kernel, Github MCP Server i Azure AI Search.

Provjerite imate li ispravno postavljene varijable okruženja za korištenje ovih alata:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Pokretanje Chainlit Servera

Za povezivanje s MCP serverom, ovaj demo koristi Chainlit kao sučelje za chat.

Za pokretanje servera, koristite sljedeću naredbu u svom terminalu:

```bash
chainlit run app.py -w
```

Ovo bi trebalo pokrenuti vaš Chainlit server na `localhost:8000` i popuniti vaš Azure AI Search Index sadržajem iz datoteke `event-descriptions.md`.

## Povezivanje s MCP Serverom

Za povezivanje s Github MCP Serverom, odaberite ikonu "utikača" ispod okvira za chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.hr.png)

Od tamo možete kliknuti na "Connect an MCP" kako biste dodali naredbu za povezivanje s Github MCP Serverom:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamijenite "[YOUR PERSONAL ACCESS TOKEN]" svojim stvarnim Personal Access Tokenom.

Nakon povezivanja, trebali biste vidjeti broj (1) pored ikone utikača kako biste potvrdili da je povezan. Ako nije, pokušajte ponovno pokrenuti Chainlit server s `chainlit run app.py -w`.

## Korištenje Dema

Za pokretanje tijeka rada agenta za preporuku hackathon projekata, možete upisati poruku poput:

"Preporuči hackathon projekte za Github korisnika koreyspace"

Router Agent će analizirati vaš zahtjev i odrediti koja kombinacija agenata (GitHub, Hackathon i Events) je najprikladnija za obradu vašeg upita. Agenti surađuju kako bi pružili sveobuhvatne preporuke na temelju analize Github repozitorija, osmišljavanja projekata i relevantnih tehnoloških događaja.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.