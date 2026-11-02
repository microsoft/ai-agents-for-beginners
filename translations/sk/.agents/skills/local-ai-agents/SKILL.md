---
name: local-ai-agents
license: MIT
---
# Vytváranie lokálnych AI agentov s Foundry Local a Qwen

> Doplňujúca zručnosť pre [Lekciu 17 – Vytváranie lokálnych AI agentov](../../../17-creating-local-ai-agents/README.md).
> Použite ju na pomoc študentovi vybudovať agenta, ktorý uvažuje, volá nástroje a vyhľadáva
> dokumentáciu úplne na jeho vlastnom zariadení — bez cloudového vyhodnocovania. Každé
> odporúčanie podložte obsahom lekcie a spustiteľným notebookom.

## Spúšťače

Aktivujte túto zručnosť, keď chce študent:
- Spustiť agenta **úplne na zariadení** z dôvodu ochrany súkromia, nákladov alebo offline prevádzky.
- Poskytnúť model lokálne pomocou **Foundry Local** a pripojiť sa prostredníctvom endpointu kompatibilného s OpenAI.
- Použiť model **Qwen s volaním funkcií** na riadenie spoľahlivých lokálnych volaní nástrojov.
- Pridať **lokálny RAG** (Chroma) alebo **lokálny MCP server**.
- Navrhnúť **hybridnú** stratégiu smerovania lokálne/vo cloude.

## Základný mentálny model

SLM vymieňa šírku poznania za súkromie, náklady a offline prevádzku. Víťazná stratégia:
**nechať SLM orchestráciu a nechať nástroje odviesť ťažkú prácu.** Model nemusí *poznať*
kódovú základňu — potrebuje vedieť, kedy volať `read_file` a `search_docs`. To využíva
silu SLM (obmedzené rozhodnutia ako výber nástroja) a vyhýba sa jeho slabine (široké znalosti,
dlhé viacstupňové uvažovanie).


## Prečo práve tieto časti

- **Foundry Local** sprístupňuje **OpenAI-kompatibilný HTTP endpoint**, takže kód cloudového agenta sa prenáša len zmenou `base_url` (a použitím lokálneho dočasného API kľúča). Tiež automaticky vyberá najlepší build (CPU/GPU/NPU) pre zariadenie.
- Modely **Qwen** sú trénované na volanie funkcií a konzistentne generujú správne volania nástrojov — tým sa lokálny *chat* model mení na lokálneho *agenta*.
- **Chroma** beží v procese a ukladá vektory na disk, takže celý RAG pipeline (embedding → ukladanie → vyhľadávanie → uvažovanie) zostáva lokálny.
- **MCP** je transport, nie cloudová služba: MCP server môže bežať lokálne cez `stdio`.

## Základné nastavenie

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokálna zástupná značka
```

~8 GB RAM je realistické minimum; GPU/NPU pomáha, ale nie je povinné.

## Kľúčové vzory na reprodukciu

Nasmerujte študenta na notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Izolované nástroje**: každý súborový nástroj rieši cesty a odmieta čokoľvek mimo jednej koreňovej zložky projektu — aj lokálne nástroj beží s oprávneniami používateľa.
- **Cyklické volanie nástrojov**: zaregistrujte nástroje podľa OpenAI nástrojovej schémy, vykonávajte požadované nástroje lokálne, vráťte výsledky a opakujte, kým nedostanete konečnú odpoveď.
- **Lokálny RAG**: vložte dokumenty do Chroma kolekcie; `search_docs` vráti najlepších k prvých fragmentov.
- **Lokálny MCP**: pripojte sa k lokálnemu serveru cez `stdio`; ohraničte ho na adresár projektu a validujte jeho výstupy.

## Hybridné smerovanie (lokálne ako jeden z modelov)

| Situácia | Kde beží |
|-----------|---------------|
| Citlivé dáta / offline | Lokálny SLM |
| Jednoduchá, obmedzená úloha | Lokálny SLM (lacný, rýchly) |
| Náročné viacstupňové uvažovanie na necitlivých dátach | Cloudový model |
| Výpadok cloudu | Lokálny SLM (plynulý pokles kvality) |

Toto odráža myšlienku smerovania modelov z Lekcie 16, pričom pracovná stanica je jedna
z ciest. Preferujte dizajny, ktoré sa vracajú k lokálnemu, aby agent degradoval vo
kvalite namiesto úplného zlyhania.

## Ochranné opatrenia pre asistenta

- Každá operácia so súbormi/nástrojmi musí byť ohraničená v izolovanom adresári projektu.
- Neodosielajte kód ani dáta do cloudu, ak je cieľom študenta súkromie/offline režim — udržiavajte celú linku lokálnu.
- Nastavte realistické očakávania pre kvalitu SLM; spoliehajte sa na nástroje a RAG skôr než na zapamätané vedomosti modelu.
- Všimnite si, že Lekcia 17 nemá žiadny Foundry Responses endpoint, takže cloudový smoke-test nie je použiteľný — overujte spustením notebooku lokálne.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->