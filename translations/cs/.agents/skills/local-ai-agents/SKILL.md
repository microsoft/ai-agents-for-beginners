---
name: local-ai-agents
license: MIT
---
# Vytváření lokálních AI agentů s Foundry Local a Qwen

> Doprovodná dovednost pro [Lekci 17 – Vytváření lokálních AI agentů](../../../17-creating-local-ai-agents/README.md).
> Použijte ji k tomu, aby si učenec vytvořil agenta, který uvažuje, volá nástroje a hledá
> dokumentaci kompletně na svém vlastním počítači — bez využití cloudu. Všechny
> doporučení zakotvěte v obsahu lekce a spustitelném notebooku.

## Spouštěče

Aktivujte tuto dovednost, když učenec chce:
- Spustit agenta **zcela na zařízení** kvůli ochraně soukromí, nákladům nebo offline provozu.
- Poskytovat model lokálně pomocí **Foundry Local** a připojit se přes OpenAI-kompatibilní endpoint.
- Použít model **Qwen s voláním funkcí** k spolehlivému lokálnímu volání nástrojů.
- Přidat **lokální RAG** (Chroma) nebo **lokální MCP server**.
- Navrhnout **hybridní** strategii směrování mezi lokálním a cloudovým modelem.

## Základní mentální model

SLM vyměňuje rozsah za soukromí, nízké náklady a offline provoz. Vítězná
strategie: **nechte SLM orchestraci a nástroje nechte dělat těžkou práci.** Model
nemusí *znát* kódovou základnu — musí vědět, kdy zavolat
`read_file` a `search_docs`. To hraje na silné stránky SLM (omezena rozhodnutí
jako výběr nástroje) a vyhýbá se jeho slabině (široké znalosti, dlouhé multi-hop
uvažování).

## Proč právě tyto komponenty

- **Foundry Local** zpřístupňuje **OpenAI-kompatibilní HTTP endpoint**, takže kód cloudového agenta se přenáší pouhou změnou `base_url` (a využitím místního placeholder API klíče). Navíc automaticky vybírá nejlepší build (CPU/GPU/NPU) pro počítač.
- Modely **Qwen** jsou trénovány pro volání funkcí a konzistentně generují dobře formátované volání nástrojů — to mění lokální *chat* model na lokální *agenta*.
- **Chroma** běží v rámci procesu a ukládá vektory na disk, takže celý RAG pipeline (embed → store → retrieve → reason) zůstává lokální.
- **MCP** je transport, nikoliv cloudová služba: MCP server může běžet lokálně přes `stdio`.

## Základy nastavení

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # místní zástupný symbol
```

~8 GB RAM je realistické minimum; GPU/NPU pomůže, ale není nutná.

## Klíčové vzory k reprodukci

Odkazujte učenče na notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxované nástroje**: každý nástroj pro práci se soubory řeší cesty a odmítá vše mimo kořenový adresář jednoho projektu — i lokálně nástroj běží s oprávněními uživatele.
- **Smyčka volání nástrojů**: zaregistrujte nástroje pomocí OpenAI schématu nástrojů, spouštějte požadované nástroje lokálně, předávejte výsledky zpět, opakujte až do konečné odpovědi.
- **Lokální RAG**: vložte dokumenty do Chroma kolekce; `search_docs` vrací top-k bloků.
- **Lokální MCP**: připojte se k lokálnímu serveru přes `stdio`; omezte ho na adresář projektu a validujte jeho výstupy.

## Hybridní směrování (lokální jako jeden z modelů)

| Situace | Kde běží |
|-----------|---------------|
| Citlivá data / offline | Lokální SLM |
| Jednoduchý, omezený úkol | Lokální SLM (levný, rychlý) |
| Náročné multi-hop uvažování nad necitlivými daty | Cloudový model |
| Výpadek cloudu | Lokální SLM (plynulá degradace) |

Toto odráží myšlenku směrování modelu z Lekce 16, kdy pracovní stanice je jedna
z cest. Upřednostňujte návrhy, které v případě potřeby přecházejí na lokální, aby agent degradoval v
kvalitě, místo aby selhal úplně.

## Ochranná opatření pro asistenta

- Každou operaci se soubory/nástroji omezte na sandboxovaný adresář projektu.
- Nezasílejte kód ani data do cloudu, pokud je cílem uživatele soukromí/offline provoz — udržujte celý pipeline lokální.
- Nastavte realistická očekávání ohledně kvality SLM; spoléhajte na nástroje a RAG spíše než na zapamatované znalosti modelu.
- Všimněte si, že Lekce 17 **nemá** endpoint Foundry Responses, takže testovací akce na cloud neplatí — ověřte spuštěním notebooku lokálně.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->