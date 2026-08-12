---
name: local-ai-agents
license: MIT
---
# Ustvarjanje lokalnih AI agentov s Foundry Local in Qwen

> Spremljevalna veščina za [Lekcija 17 – Ustvarjanje lokalnih AI agentov](../../../17-creating-local-ai-agents/README.md).
> Uporabi jo, da pomaga učencu zgraditi agenta, ki samostojno razmišlja, kliče orodja in išče
> dokumentacijo povsem na lastnem računalniku — brez oblačnega sklepanja. Vsako
> priporočilo poveži z vsebino lekcije in izvedljivim zvezkom.

## Sprožilci

Aktiviraj to veščino, ko učenec želi:
- Zagnati agenta **popolnoma na napravi** zaradi zasebnosti, stroškov ali brez povezave.
- Postreči model lokalno z **Foundry Local** in se povezati prek OpenAI združljivega konektorja.
- Uporabiti model **Qwen za klicanje funkcij** za zanesljive lokalne klice orodij.
- Dodati **lokalni RAG** (Chroma) ali **lokalni MCP strežnik**.
- Oblikovati **hibridno** usmerjevalno strategijo lokalno/oblak.

## Osnovni mentalni model

SLM zamenja širino za zasebnost, stroške in delovanje brez povezave. Zmagovalna
strategija: **dovoli, da SLM usmerja in naj orodja opravijo težko delo.** Model
ne potrebuje, da *pozna* kodo — mora vedeti, kdaj poklicati
`read_file` in `search_docs`. To izkorišča prednosti SLM (omejene odločitve,
kot je izbira orodij) in se izogiba njegovim slabostim (široko znanje, dolgoročno večstopenjsko
sklepanje).

## Zakaj prav ti deli

- **Foundry Local** izpostavlja **OpenAI združljiv HTTP konektor**, tako se koda oblaka prenese samo z zamenjavo `base_url` (in uporabo lokalnega nadomestnega API ključa). Prav tako samodejno izbere najboljšo gradnjo (CPU/GPU/NPU) za napravo.
- Modeli **Qwen** so usposobljeni za klic funkcij in dosledno ustvarjajo dobro oblikovane klice orodij — to spremeni lokalni *klepetalni* model v lokalnega *agenta*.
- **Chroma** deluje znotraj procesa in shranjuje vektorje na disku, tako celoten RAG cevovod (vstavljanje → shranjevanje → pridobivanje → sklepanje) ostane lokalni.
- **MCP** je prenos, ne oblačna storitev: MCP strežnik lahko teče lokalno preko `stdio`.

## Osnove nastavitve

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokalni rezervni prostor
```

~8 GB RAM je realna minimum; GPU/NPU pomaga, vendar ni nujen.

## Ključni vzorci za ponovitev

Usmeri učenca na zvezek
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Orodja v peskovniku**: vsako orodje za datoteke rešuje poti in zavrne vse zunaj enega projekta — tudi lokalno orodje teče z uporabnikovimi dovoljenji.
- **Zanka za klic orodij**: registriraj orodja po OpenAI shemi orodij, lokalno izvedi zahtevana orodja, vrni rezultate in ponovi, dokler ni končnega odgovora.
- **Lokalni RAG**: vstavi dokumente v Chroma zbirko; `search_docs` vrne najboljše kose.
- **Lokalni MCP**: poveži se na lokalni strežnik preko `stdio`; omeji na projektno mapo in preveri njegove izhode.

## Hibridno usmerjanje (lokalno kot en izmed modelov)

| Situacija | Kje teče |
|-----------|---------------|
| Zaupni podatki / brez povezave | Lokalni SLM |
| Enostavna, omejena naloga | Lokalni SLM (ceneje, hitreje) |
| Zahtevno večstopenjsko sklepanje na nezaupnih podatkih | Model v oblaku |
| Izpad oblaka | Lokalni SLM (vljudno degradiranje) |

To zrcali idejo usmerjanja modela iz Lekcije 16, kjer je delovna postaja ena
od poti. Prednost daj zasnovam, ki se priklenejo nazaj na lokalno, da agent upada v
kakovosti namesto da popolnoma odpove.

## Zaščitne ograje za asistenta

- Večino operacij z datotekami/orodji omeji na peskovniško projektno mapo.
- Ne pošiljaj kode ali podatkov v oblak, ko je cilj učenca zasebnost/brez povezave — naj celoten cevovod ostane lokalni.
- Nastavi realna pričakovanja za kakovost SLM; opiraj se na orodja in RAG namesto na modelovo zapomnjeno znanje.
- Upoštevaj, da Lekcija 17 nima **Foundry Responses** konektorja, zato oblačni test ni uporaben — preveri z zagonom zvezka lokalno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->