---
name: local-ai-agents
description: Build local-first AI agents that run entirely on a developer workstation with Microsoft Foundry Local and Qwen function-calling models. Covers sandboxed local tools, local RAG with Chroma, local MCP servers, hybrid cloud/local routing, and privacy, cost, and offline trade-offs.
license: MIT
---
# Kreiranje lokalnih AI agenata s Foundry Local i Qwen

> Dopunska vještina za [Lekciju 17 – Kreiranje lokalnih AI agenata](../../../17-creating-local-ai-agents/README.md).
> Koristite je za pomoć učeniku u izgradnji agenta koji razmišlja, poziva alate i pretražuje
> dokumentaciju u potpunosti na vlastitom računalu — bez cloud izvođenja. Svaku
> preporuku utemeljite na sadržaju lekcije i izvršivoj bilježnici.

## Okidači

Aktivirajte ovu vještinu kada učenik želi:
- Pokrenuti agenta **potpuno na uređaju** iz privatnosti, troškova ili offline razloga.
- Poslužiti model lokalno s **Foundry Local** i povezati se putem OpenAI-kompatibilnog endpointa.
- Koristiti **Qwen model s pozivanjem funkcija** za pouzdane lokalne pozive alata.
- Dodati **lokalni RAG** (Chroma) ili **lokalni MCP poslužitelj**.
- Osmišljavati **hibridnu** strategiju usmjeravanja lokalno/cloud.

## Osnovni mentalni model

SLM mijenja širinu pokrivenosti za privatnost, troškove i offline rad. Pobjednička
strategija: **dopustiti SLM-u da orkestrira, a alatima da obavljaju glavni posao.** 
Model ne mora *znati* kodnu bazu — treba znati kada pozvati
`read_file` i `search_docs`. Ovo igra u korist snage SLM-a (ograničene odluke
poput odabira alata) i izbjegava njegovu slabost (široko znanje, dugi višestupanjski
rezoniranje).

## Zašto baš ovi dijelovi

- **Foundry Local** pruža **OpenAI-kompatibilni HTTP endpoint**, pa se cloud kod agenta prenosi promjenom samo `base_url` (i korištenjem lokalnog privremenog API ključa). Također automatski bira najbolju verziju (CPU/GPU/NPU) za računalo.
- **Qwen** modeli su trenirani za pozivanje funkcija i dosljedno ispisuju pravilno oblikovane pozive alata — to pretvara lokalni *chat* model u lokalnog *agenta*.
- **Chroma** radi unutar procesa i pohranjuje vektore na disk, tako da cijeli RAG proces (ugrađivanje → pohrana → dohvati → rezoniranje) ostaje lokalno.
- **MCP** je transport, ne cloud usluga: MCP poslužitelj može raditi lokalno preko `stdio`.

## Osnove postavljanja

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```

~8 GB RAM-a je realan minimum; GPU/NPU pomaže ali nije obavezan.

## Ključni obrasci za reprodukciju

Usmjerite učenika na bilježnicu
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Alati u pješčaniku**: svaki alat za datoteke rješava putove i odbacuje sve izvan jednog korijenskog direktorija projekta — čak i lokalno alat radi s korisničkim dozvolama.
- **Petlja poziva alata**: registrirajte alate s OpenAI shemom alata, izvršavajte tražene alate lokalno, vraćajte rezultate, ponavljajte dok ne dođete do konačnog odgovora.
- **Lokalni RAG**: ubacite dokumente u Chroma kolekciju; `search_docs` vraća top-k dijelove.
- **Lokalni MCP**: spojite se na lokalni poslužitelj preko `stdio`; ograničite ga na direktorij projekta i potvrdite njegove izlaze.

## Hibridno usmjeravanje (lokalno kao jedan od modela)

| Situacija | Gdje se izvršava |
|-----------|---------------|
| Osjetljivi podaci / offline | Lokalni SLM |
| Jednostavan, ograničen zadatak | Lokalni SLM (jeftino, brzo) |
| Teško višestupanjsko rezoniranje na neosjetljivim podacima | Cloud model |
| Prekid cloud usluge | Lokalni SLM (nježno degradiranje) |

Ovo odražava ideju usmjeravanja modela iz Lekcije 16, s radnom stanicom kao jednim
od pravaca. Preferirajte dizajne koji se vraćaju na lokalno tako da agent degradira u
kvaliteti umjesto da potpuno zakaže.

## Sigurnosne mjere za asistenta

- Ograničite svaku operaciju datoteka/alata na pješčanik direktorij projekta.
- Ne šaljite kod ili podatke u cloud kada je cilj učenika privatnost/offline — cijeli proces držite lokalnim.
- Postavite realna očekivanja za kvalitetu SLM-a; oslanjajte se na alate i RAG umjesto na memorirano znanje modela.
- Imajte na umu da Lekcija 17 nema **niti jedan** Foundry Responses endpoint, pa cloud test radnje nisu primjenjive — provjerite pokretanjem bilježnice lokalno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->