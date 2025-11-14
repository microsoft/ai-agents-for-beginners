<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:23:00+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "sk"
}
-->
# Github MCP Server Príklad

## Popis

Toto je demo vytvorené pre AI Agents Hackathon organizovaný prostredníctvom Microsoft Reactor.

Nástroj slúži na odporúčanie projektov na hackathon na základe Github repozitárov používateľa.
Toto sa dosahuje pomocou:

1. **Github Agent** - Používa Github MCP Server na získanie repozitárov a informácií o týchto repozitároch.
2. **Hackathon Agent** - Spracováva údaje z Github Agenta a navrhuje kreatívne nápady na hackathon projekty na základe projektov, jazykov používaných používateľom a tém hackathonu AI Agents.
3. **Events Agent** - Na základe návrhov Hackathon Agenta odporúča relevantné podujatia zo série AI Agent Hackathon.

## Spustenie kódu 

### Environmentálne premenné

Toto demo používa Azure Open AI Service, Semantic Kernel, Github MCP Server a Azure AI Search.

Uistite sa, že máte správne nastavené environmentálne premenné na používanie týchto nástrojov:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Spustenie Chainlit Servera

Na pripojenie k MCP serveru toto demo používa Chainlit ako chatovacie rozhranie.

Na spustenie servera použite nasledujúci príkaz vo vašom termináli:

```bash
chainlit run app.py -w
```

Týmto by sa mal spustiť váš Chainlit server na `localhost:8000` a zároveň naplniť váš Azure AI Search Index obsahom súboru `event-descriptions.md`.

## Pripojenie k MCP Serveru

Na pripojenie k Github MCP Serveru kliknite na ikonu "plug" pod chatovacím boxom "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.sk.png)

Odtiaľ môžete kliknúť na "Connect an MCP" a pridať príkaz na pripojenie k Github MCP Serveru:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Nahraďte "[YOUR PERSONAL ACCESS TOKEN]" vaším skutočným Personal Access Token.

Po pripojení by ste mali vidieť (1) vedľa ikony plug, čo potvrdzuje, že ste pripojení. Ak nie, skúste reštartovať Chainlit server príkazom `chainlit run app.py -w`.

## Používanie dema 

Na spustenie pracovného postupu agenta na odporúčanie projektov na hackathon môžete napísať správu ako:

"Odporuč hackathon projekty pre Github používateľa koreyspace"

Router Agent analyzuje vašu požiadavku a určí, ktorá kombinácia agentov (GitHub, Hackathon a Events) je najvhodnejšia na spracovanie vášho dotazu. Agenti spolupracujú, aby poskytli komplexné odporúčania na základe analýzy Github repozitárov, generovania nápadov na projekty a relevantných technologických podujatí.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.