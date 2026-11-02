---
name: microsoft-docs
description: Kysy virallisesta Microsoftin dokumentaatiosta löytääksesi käsitteitä,
  oppaita ja koodiesimerkkejä Azuresta, .NET:stä, Agent Frameworkista, Aspiresta,
  VS Codesta, GitHubista ja muista. Käyttää oletuksena Microsoft Learn MCP:tä, sekä
  Context7:ää ja Aspire MCP:tä sisällöille, jotka sijaitsevat learn.microsoft.comin
  ulkopuolella.
---
# Microsoft Docs

Tutkimustaito Microsoftin teknologiaympäristössä. Kattaa learn.microsoft.comin ja sen ulkopuolella elävän dokumentaation (VS Code, GitHub, Aspire, Agent Framework -repositoriot).

---

## Oletus: Microsoft Learn MCP

Käytä näitä työkaluja **kaikkiin learn.microsoft.comin asioihin** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ja muut. Tämä on ensisijainen työkalu suurimmalle osalle Microsoftin dokumentaatiokyselyistä.

| Työkalu | Tarkoitus |
|------|---------|
| `microsoft_docs_search` | Etsi learn.microsoft.comista — käsitteet, oppaat, tutoriaalit, konfigurointi |
| `microsoft_code_sample_search` | Löydä toimivat koodiesimerkit Learn-dokumenteista. Anna `language` (`python`, `csharp` jne.) parhaiden tulosten saamiseksi |
| `microsoft_docs_fetch` | Hanki koko sivun sisältö tietystä URL-osoitteesta (kun hakupätkät eivät riitä) |

Käytä `microsoft_docs_fetch` haun jälkeen, kun tarvitset täydellisiä tutoriaaleja, kaikki konfigurointivaihtoehdot tai kun hakupätkät ovat lyhennettyjä.

---

## Poikkeukset: Milloin käyttää muita työkaluja

Seuraavat kategoriat sijaitsevat **learn.microsoft.comin ulkopuolella**. Käytä sijaan määriteltyä työkalua.

### Aspire — Käytä Aspire MCP Serveriä (suositus) tai Context7:ää

Aspire-dokumentaatiot löytyvät **aspire.dev** -osoitteesta, eivät Learnista. Paras työkalu riippuu Aspire CLI -versiostasi:

**CLI 13.2+** (suositus) — Aspire MCP -palvelimessa on sisäänrakennetut dokumentaation hakutyökalut:

| MCP-työkalu | Kuvaus |
|----------|-------------|
| `list_docs` | Listaa kaikki saatavilla olevat dokumentaatiot aspire.devistä |
| `search_docs` | Painotettu leksikaalinen haku aspire.dev-sisällöstä |
| `get_doc` | Hakee tietyn dokumentin nimen perusteella |

Nämä julkaistiin Aspire CLI 13.2:ssa ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Päivitä: `aspire update --self --channel daily`.

**CLI 13.1** — MCP-palvelin tarjoaa integraatiohaun (`list_integrations`, `get_integration_docs`) mutta **ei** dokumentaation hakua. Palaa Context7:ään:

| Kirjaston tunniste | Käyttötarkoitus |
|---|---|
| `/microsoft/aspire.dev` | Pääasiallinen — oppaat, integraatiot, CLI-viite, käyttöönotto |
| `/microsoft/aspire` | Suorituksen lähde — API:n sisäiset tiedot, toteutuksen yksityiskohdat |
| `/communitytoolkit/aspire` | Yhteisön integraatiot — Go, Java, Node.js, Ollama |

### VS Code — Käytä Context7:ää

VS Code -dokumentaatio löytyy osoitteesta **code.visualstudio.com**, ei Learnista.

| Kirjaston tunniste | Käyttötarkoitus |
|---|---|
| `/websites/code_visualstudio` | Käyttäjädokumentaatio — asetukset, ominaisuudet, virheenkorjaus, etäkehitys |
| `/websites/code_visualstudio_api` | Laajennuksen API — webview't, TreeView't, komennot, kontribuutiopisteet |

### GitHub — Käytä Context7:ää

GitHubin dokumentaatio on osoitteissa **docs.github.com** ja **cli.github.com**.

| Kirjaston tunniste | Käyttötarkoitus |
|---|---|
| `/websites/github_en` | Toiminnot, API, repositoriot, tietoturva, hallinta, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) komennot ja liput |

### Agent Framework — Käytä Learn MCP:tä + Context7:ää

Agent Frameworkin tutoriaalit löytyvät learn.microsoft.comista (käytä `microsoft_docs_search`), mutta **GitHub-repossa** on API-tasoisia tietoja, jotka ovat usein julkaistua dokumentaatiota edellä — erityisesti DevUI REST API -viite, CLI-vaihtoehdot ja .NET-integraatio.

| Kirjaston tunniste | Käyttötarkoitus |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriaalit — DevUI-oppaat, jäljitys, työnkulun orkestrointi |
| `/microsoft/agent-framework` | API-tiedot — DevUI REST -päätepisteet, CLI-liput, todennus, .NET `AddDevUI`/`MapDevUI` |

**DevUI-vinkki:** Kysy Learn-verkkosivun lähteestä miten-ohjeet ja sen jälkeen repositorion lähteestä API-tason yksityiskohdat (pääteskeemat, proxyn konfigurointi, todennustunnukset).

---

## Context7:n käyttöönotto

Jokaisen Context7-kyselyn kohdalla selvitä ensin kirjaston tunniste (kertaluonteinen per istunto):

1. Soita `mcp_context7_resolve-library-id` teknologian nimellä
2. Soita `mcp_context7_query-docs` saadulla kirjastontunnisteella ja tietyn kyselyn kanssa

---

## Tehokkaiden kyselyiden kirjoittaminen

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

Lisää konteksti:
- **Versio** kun relevantti (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Tehtävän tarkoitus** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Kieli** monikielisissä dokumentaatioissa (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->