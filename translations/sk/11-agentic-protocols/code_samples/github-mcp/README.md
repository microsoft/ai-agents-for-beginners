# Github MCP Server Príklad

## Popis

Toto bolo demo vytvorené pre AI Agents Hackathon organizovaný prostredníctvom Microsoft Reactor.

Tento nástroj sa používa na odporúčanie hackathonových projektov na základe GitHub repozitárov používateľa.
To sa robí takto:

1. **Github Agent** - Používa Github MCP Server na získanie repozitárov a informácií o týchto repozitároch.
2. **Hackathon Agent** - Vezme dáta od Github Agent a vytvorí kreatívne nápady na hackathonové projekty na základe projektov, jazykov používaných používateľom a tém pre AI Agents hackathon.
3. **Events Agent** - Na základe návrhu Hackathon Agent odporučí relevantné udalosti zo série AI Agent Hackathon.
## Spustenie kódu 

### Premenné prostredia

Toto demo používa Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server a Azure AI Search.

Uistite sa, že máte nastavené správne premenné prostredia na použitie týchto nástrojov:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Spustenie Chainlit servera

Na pripojenie k MCP serveru toto demo používa Chainlit ako chatovacie rozhranie. 

Na spustenie servera použite v termináli nasledujúci príkaz:

```bash
chainlit run app.py -w
```

To by malo spustiť váš Chainlit server na `localhost:8000` a zároveň naplniť váš Azure AI Search Index obsahom `event-descriptions.md`. 

## Pripojenie k MCP serveru

Na pripojenie k Github MCP Serveru vyberte ikonu "plug" pod chatovacím políčkom "Sem zadajte svoju správu..":

![Pripojenie MCP](../../../../../translated_images/sk/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Odtiaľ môžete kliknúť na "Connect an MCP" na pridanie príkazu na pripojenie k Github MCP Serveru:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Nahraďte "[YOUR PERSONAL ACCESS TOKEN]" vaším skutočným Personal Access Token. 

Po pripojení by ste mali vidieť (1) vedľa ikony plug, čo potvrdzuje, že je pripojené. Ak nie, skúste reštartovať chainlit server pomocou `chainlit run app.py -w`.

## Používanie dema 

Ak chcete spustiť pracovný tok agentov na odporúčanie hackathonových projektov, môžete zadať správu napríklad: 

"Odporučte hackathonové projekty pre Github používateľa koreyspace"

Router Agent analyzuje vašu požiadavku a rozhodne, ktorá kombinácia agentov (GitHub, Hackathon a Events) je najvhodnejšia na spracovanie vášho dopytu. Agenti spolupracujú, aby poskytli komplexné odporúčania založené na analýze repozitárov GitHub, generovaní nápadov na projekty a relevantných technologických podujatiach.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vylúčenie zodpovednosti:

Tento dokument bol preložený pomocou AI prekladateľskej služby Co-op Translator (https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by sa mal považovať za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->