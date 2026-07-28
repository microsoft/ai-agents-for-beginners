---
name: local-ai-agents
license: MIT
---
# Skapa Lokala AI-agenter med Foundry Local och Qwen

> Kompisfärdighet för [Lektionen 17 – Skapa Lokala AI-agenter](../../../17-creating-local-ai-agents/README.md).
> Använd den för att hjälpa en lärande att bygga en agent som resonerar, anropar verktyg och söker
> dokumentation helt på deras egen maskin — ingen molninferens. Förankra varje
> rekommendation i lektionsinnehållet och det körbara anteckningsboken.

## Utlösare

Aktivera denna färdighet när en lärande vill:
- Köra en agent **helt på enheten** för integritet, kostnad eller offline-anledningar.
- Servera en modell lokalt med **Foundry Local** och anslut via OpenAI-kompatibel endpoint.
- Använda en **Qwen funktionsanropsmodell** för att driva pålitliga lokala verktygsanrop.
- Lägga till **lokal RAG** (Chroma) eller en **lokal MCP-server**.
- Designa en **hybrid** lokal/molnruttstrategi.

## Kärnmental modell

En SLM byter bredd mot integritet, kostnad och offline-drift. Den vinnande
strategin: **låt SLM orkestrera och låt verktygen göra det tunga jobbet.** Modellen
behöver inte *känna till* kodbasen — den behöver veta när den ska anropa
`read_file` och `search_docs`. Det spelar på en SLM:s styrka (begränsade beslut
som verktygsval) och bort från dess svaghet (bred kunskap, lång multi-hop
resonerande).

## Varför dessa specifika delar

- **Foundry Local** exponerar en **OpenAI-kompatibel HTTP-endpoint**, så molnagentkod överförs genom att endast byta `base_url` (och använda en lokal platshållar-API-nyckel). Den väljer också automatiskt bästa bygg (CPU/GPU/NPU) för maskinen.
- **Qwen**-modeller tränas för funktionsanrop och avger konsekvent väldefinierade verktygsanrop — det här är vad som förvandlar en lokal *chatt*modell till en lokal *agent*.
- **Chroma** körs i processen och lagrar vektorer på disk, så hela RAG-pipelinen (embed → store → retrieve → reason) förblir lokal.
- **MCP** är en transport, inte en molntjänst: en MCP-server kan köras lokalt över `stdio`.

## Grundläggande uppsättning

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokal platshållare
```

~8 GB RAM är en realistisk minimum; en GPU/NPU hjälper men är inte krävd.

## Viktiga mönster att reproducera

Peka den lärande mot anteckningsboken
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandlådafunktioner**: varje filverktyg löser sökvägar och avvisar allt utanför en enda projektrot — även lokalt körs ett verktyg med användarens behörigheter.
- **Verktygsanropsloop**: registrera verktyg med OpenAI verktygsschema, kör begärda verktyg lokalt, mata tillbaka resultat, upprepa tills ett slutgiltigt svar.
- **Lokal RAG**: uppdatera dokument i en Chroma-kollektion; `search_docs` returnerar topp-k delar.
- **Lokal MCP**: anslut till lokal server över `stdio`; begränsa den till en projektkatalog och validera dess utdata.

## Hybridriktning (lokal som en av modellerna)

| Situation | Var det körs |
|-----------|--------------|
| Känsliga data / offline | Lokal SLM |
| Enkel, begränsad uppgift | Lokal SLM (billig, snabb) |
| Svår multi-hop resonemang på icke-känsliga data | Molnmodell |
| Molnsavbrott | Lokal SLM (graciös degradering) |

Detta speglar modellruttidén från Lektion 16, med arbetsstationen som en
av rutterna. Föredra design som faller tillbaka till lokal så att agenten degraderas i
kvalitet snarare än att helt misslyckas.

## Skydd för assistenten

- Håll varje fil-/verktygsoperation begränsad till en sandlådad projektkatalog.
- Skicka inte kod eller data till molnet när den lärandes uttalade mål är integritet/offline — håll hela pipelinen lokal.
- Sätt realistiska förväntningar på SLM-kvalitet; luta dig mot verktyg och RAG snarare än modellens inlärda kunskap.
- Notera att Lektion 17 har **ingen** Foundry Responses endpoint, så molnets rökteståtgärd gäller inte — validera genom att köra anteckningsboken lokalt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->