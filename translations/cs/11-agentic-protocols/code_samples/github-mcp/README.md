<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:22:51+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "cs"
}
-->
# Github MCP Server Example

## Popis

Toto je demo vytvořené pro hackathon AI Agents pořádaný prostřednictvím Microsoft Reactor.

Nástroj slouží k doporučování projektů pro hackathon na základě Github repozitářů uživatele. To se provádí pomocí:

1. **Github Agent** - Používá Github MCP Server k získání repozitářů a informací o těchto repozitářích.
2. **Hackathon Agent** - Využívá data od Github Agenta a přichází s kreativními nápady na projekty pro hackathon na základě projektů, jazyků používaných uživatelem a témat hackathonu AI Agents.
3. **Events Agent** - Na základě návrhů Hackathon Agenta doporučuje Events Agent relevantní události ze série AI Agent Hackathon.

## Spuštění kódu 

### Proměnné prostředí

Toto demo využívá Azure Open AI Service, Semantic Kernel, Github MCP Server a Azure AI Search.

Ujistěte se, že máte správně nastavené proměnné prostředí pro použití těchto nástrojů:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Spuštění Chainlit Serveru

Pro připojení k MCP serveru toto demo používá Chainlit jako chatovací rozhraní.

Pro spuštění serveru použijte následující příkaz ve vašem terminálu:

```bash
chainlit run app.py -w
```

Tím by se měl spustit váš Chainlit server na `localhost:8000` a zároveň naplnit váš Azure AI Search Index obsahem souboru `event-descriptions.md`.

## Připojení k MCP Serveru

Pro připojení k Github MCP Serveru klikněte na ikonu "zástrčky" pod chatovacím polem "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.cs.png)

Odtud můžete kliknout na "Connect an MCP" a přidat příkaz pro připojení k Github MCP Serveru:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Nahraďte "[YOUR PERSONAL ACCESS TOKEN]" vaším skutečným osobním přístupovým tokenem.

Po připojení byste měli vidět (1) vedle ikony zástrčky, což potvrzuje, že je připojeno. Pokud ne, zkuste restartovat Chainlit server pomocí `chainlit run app.py -w`.

## Použití dema 

Pro zahájení pracovního postupu agenta, který doporučuje projekty pro hackathon, můžete napsat zprávu jako:

"Doporuč projekty pro hackathon pro Github uživatele koreyspace"

Router Agent analyzuje váš požadavek a určí, která kombinace agentů (GitHub, Hackathon a Events) je nejvhodnější pro zpracování vašeho dotazu. Agenti spolupracují, aby poskytli komplexní doporučení na základě analýzy Github repozitářů, návrhů projektů a relevantních technologických událostí.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.