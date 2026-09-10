---
name: microsoft-docs
description: Kysy virallista Microsoftin dokumentaatiota löytääksesi käsitteitä, opetusohjelmia
  ja koodiesimerkkejä Azureen, .NET:iin, Agent Frameworkiin, Aspireen, VS Codeen,
  GitHubiin ja muihin liittyen. Käyttää oletuksena Microsoft Learn MCP:tä, sekä Context7:ää
  ja Aspire MCP:tä sisällölle, joka sijaitsee learn.microsoft.comin ulkopuolella.
---
# Microsoft Docs

Tutkimustaito Microsoftin teknologiaympäristöä varten. Kattaa learn.microsoft.comin ja dokumentaation, joka sijaitsee sen ulkopuolella (VS Code, GitHub, Aspire, Agent Framework -repositoriot).

---

## Default: Microsoft Learn MCP

Käytä näitä työkaluja **kaikkeen, mikä löytyy osoitteesta learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ja muut. Tämä on ensisijainen työkalu suurimmassa osassa Microsoft-dokumentaatioon liittyvistä kyselyistä.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Etsi learn.microsoft.com — käsitteet, oppaat, tutoriaalit, konfigurointi |
| `microsoft_code_sample_search` | Etsi toimivia koodikatkelmia Learn-dokumenteista. Anna `language` (`python`, `csharp`, jne.) parhaiten tuloksin |
| `microsoft_docs_fetch` | Hae täysi sivun sisältö tietystä URL-osoitteesta (kun hakukatkelmat eivät riitä) |

Käytä `microsoft_docs_fetch`-työkalua haun jälkeen, kun tarvitset täydelliset tutoriaalit, kaikki konfiguraatioasetukset tai kun hakukatkelmat on katkaistu.

---

## Exceptions: When to Use Other Tools

Seuraavat kategoriat sijaitsevat **sen ULKOPUOLELLA** learn.microsoft.com-sivustoa. Käytä sen sijaan määriteltyä työkalua.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire-dokumentaatio löytyy osoitteesta **aspire.dev**, ei Learnista. Paras työkalu riippuu Aspire CLI -versiostasi:

**CLI 13.2+** (suositeltu) — Aspire MCP -palvelin sisältää sisäänrakennetut dokumentaation hakutyökalut:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Luettelee kaiken saatavilla olevan dokumentaation osoitteesta aspire.dev |
| `search_docs` | Painotettu leksikaalinen haku aspire.dev -sisällöstä |
| `get_doc` | Hakee tietyn dokumentin slugin perusteella |

Nämä sisältyvät Aspire CLI 13.2:een ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Päivitä: `aspire update --self --channel daily`. Viite: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP-palvelin tarjoaa integraatiohaun (`list_integrations`, `get_integration_docs`) mutta **ei** dokumentaation hakua. Palaa Context7:aan:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Ensisijainen — oppaat, integraatiot, CLI-viite, käyttöönotto |
| `/dotnet/aspire` | Ajonaikainen lähdekoodi — API:n sisäiset osat, toteutusyksityiskohdat |
| `/communitytoolkit/aspire` | Yhteisön integraatiot — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code -dokumentaatio löytyy osoitteesta **code.visualstudio.com**, ei Learnista.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Käyttäjädokumentaatio — asetukset, ominaisuudet, virheenkorjaus, etäkehitys |
| `/websites/code_visualstudio_api` | Laajennuksen API — webviewt, TreeViewt, komennot, kontribuutiopisteet |

### GitHub — Use Context7

GitHub-dokumentaatio löytyy osoitteista **docs.github.com** ja **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repositoriot, suojaus, hallinta, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) -komennot ja liput |

### Agent Framework — Use Learn MCP + Context7

Agent Frameworkin tutoriaalit ovat learn.microsoft.comissa (käytä `microsoft_docs_search`), mutta **GitHub-repositorio** sisältää API-tason yksityiskohtia, jotka usein edeltävät julkaistuja docs-sivuja — erityisesti DevUI REST API -viite, CLI-valinnat ja .NET-integraatio.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Opetusohjelmat — DevUI-oppaat, jäljitys, työnkulun orkestrointi |
| `/microsoft/agent-framework` | API-yksityiskohdat — DevUI REST-päätepisteet, CLI-liput, autentikointi, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Hae Learn-verkkosivuston lähteestä how-to-oppaat ja tarkista sitten repositorion lähde API-tason yksityiskohtia varten (päätepisteiden skeemat, proxy-konfiguraatio, autentikointitunnukset).

---

## Context7 Setup

Context7-kyselyä varten ratkaise ensin kirjaston ID (kertakäyttö per istunto):

1. Kutsu `mcp_context7_resolve-library-id` teknologian nimellä
2. Kutsu `mcp_context7_query-docs` palautetulla kirjaston ID:llä ja tarkemmalla kyselyllä

---

## Writing Effective Queries

Ole tarkka — sisällytä versio, tarkoitus ja kieli:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Include context:
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty käyttämällä tekoälykäännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattikäännöksissä voi olla virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->