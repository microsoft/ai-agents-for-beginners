[![Uvod v AI agente](../../../translated_images/sl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite sliko zgoraj, da si ogledate video za to lekcijo)_

# Uvod v AI agente in primere uporabe agentov

Dobrodošli na tečaju **AI agenti za začetnike**! Ta tečaj vam daje osnovno znanje — in pravo delujočo kodo — za začetek gradnje AI agentov iz nič.

Pridružite se v <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord skupnosti</a> — polni je učencev in AI razvijalcev, ki z veseljem odgovorijo na vprašanja.

Preden začnemo z gradnjo, se prepričajmo, da dejansko razumemo, kaj AI agent *je* in kdaj je smiselno uporabiti enega.

---

## Uvod

Ta lekcija zajema:

- Kaj so AI agenti in različne vrste, ki obstajajo
- Za katere vrste nalog so AI agenti najbolj primerni
- Temeljne gradnike, ki jih boste uporabili pri oblikovanju agentne rešitve

## Cilji učenja

Na koncu te lekcije bi morali biti sposobni:

- Pojasniti, kaj je AI agent in kako se razlikuje od običajne AI rešitve
- Vedeti, kdaj je primerno uporabiti AI agenta (in kdaj ne)
- Načrtovati osnovno zasnovo agentne rešitve za resničen problem

---

## Definiranje AI agentov in vrst AI agentov

### Kaj so AI agenti?

Tukaj je enostaven način za razmišljanje o tem:

> **AI agenti so sistemi, ki Large Language Models (LLM) dejansko *omogočajo dejanja* — z dajanjem orodij in znanja za vplivanje na svet, ne le za odgovarjanje na ukaze.**

Razložimo malce podrobneje:

- **Sistem** — AI agent ni le ena stvar. Je zbirka delov, ki skupaj delujejo. V jedru ima vsak agent tri dele:
  - **Okolje** — Prostor, v katerem agent deluje. Za agenta za rezervacijo potovanj bi to bila sama platforma za rezervacije.
  - **Senzorji** — Kako agent bere trenutni položaj svojega okolja. Naš agent za potovanja bi lahko preverjal razpoložljivost hotelov ali cene letov.
  - **Aktuatorji** — Kako agent izvaja dejanja. Agent za potovanje bi lahko rezerviral sobo, poslal potrditev ali odpovedal rezervacijo.

![Kaj so AI agenti?](../../../translated_images/sl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agenti so obstajali pred LLM, a LLM naredijo sodobne agente tako močne. Razumejo naravni jezik, razmišljajo o kontekstu in spremenijo nejasno uporabniško zahtevo v konkreten načrt.

- **Izvajanje dejanj** — Brez sistema agenta LLM samo ustvari besedilo. Znotraj agentskega sistema lahko LLM dejansko *izvede* korake — išče v podatkovni bazi, kliče API, pošilja sporočila.

- **Dostop do orodij** — Katere orodja lahko agent uporablja, je odvisno od (1) okolja, v katerem deluje, in (2) kaj je razvijalec odločil, da mu da. Agent za potovanja lahko išče lete, a ne ureja podatkov strank — vse je odvisno od tega, kako ga povežete.

- **Spomin + Znanje** — Agenti imajo lahko kratkoročni spomin (trenutni pogovor) in dolgoročni spomin (baza strank, pretekle interakcije). Agent za potovanja se bo "spomnil", da imate raje sedeže ob oknu.

---

### Različne vrste AI agentov

Niso vsi agenti enaki. Tukaj je razčlenitev glavnih vrst, z agentom za rezervacijo potovanj kot tekočim primerom:

| **Vrsta agenta** | **Kaj počne** | **Primer agenta za potovanja** |
|---|---|---|
| **Enostavni refleksni agenti** | Sledijo trdo kodiranim pravilom — brez spomina, brez načrtovanja. | Prejme pritožbeno e-pošto → posreduje ga službi za stranke. To je vse. |
| **Modelno osnovani refleksni agenti** | Ohranjajo notranji model sveta in ga posodabljajo, ko se stvari spremenijo. | Spremlja zgodovinske cene letov in označi poti, ki so nenadoma drage. |
| **Agent z ciljem** | Ima zastavljen cilj in ugotavlja, kako ga korak za korakom doseči. | Rezervira celotno potovanje (leti, avto, hotel) od vaše trenutne lokacije do cilja. |
| **Agent, ki temelji na koristnosti** | Ne najde le *rešitve* — najde *najboljšo* z uravnoteženjem kompromisov. | Uravnava stroške proti udobju, da najde potovanje, ki najbolje ustreza vašim željam. |
| **Učeči agenti** | Se sčasoma izboljšajo z učenjem iz povratnih informacij. | Prilagodi prihodnja priporočila za rezervacije glede na rezultate ankete po poti. |
| **Hierarhični agenti** | Visoko raven agent razdeli delo na podnaloge in ga delegira nižjim agentom. | Zahtevek "prekliči potovanje" se razdeli na: odpoved leta, odpoved hotela, odpoved najema avtomobila — vsak upravlja pod-agent. |
| **Sistemi z več agenti (MAS)** | Več neodvisnih agentov, ki delajo skupaj (ali tekmujejo). | Sodelovanje: ločeni agenti skrbijo za hotele, lete in zabavo. Tekmovanje: več agentov tekmuje za zapolnitev hotelskih sob po najboljši ceni. |

---

## Kdaj uporabiti AI agente

Samo zato, ker lahko uporabite AI agenta, še ne pomeni, da ga morate vedno uporabljati. Tukaj so situacije, kjer agenti resnično izstopajo:

![Kdaj uporabiti AI agente?](../../../translated_images/sl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Odprte zadeve** — Ko koraki za rešitev problema ne morejo biti vnaprej programirani. Potrebujete, da LLM dinamično najde pot.
- **Večstopenjski procesi** — Naloge, ki zahtevajo uporabo orodij čez več korakov, ne le enega iskanja ali generiranja.
- **Izboljšave skozi čas** — Ko želite, da sistem postane pametnejši na podlagi uporabniških povratnih informacij ali signalov iz okolja.

Podrobneje bomo raziskali, kdaj (in kdaj *ne*) uporabljati AI agente v lekciji **Gradnja zaupanja vrednih AI agentov** kasneje v tečaju.

---

## Osnove agentnih rešitev

### Razvoj agenta

Prvo, kar naredite pri gradnji agenta, je določiti *kaj lahko počne* — njegova orodja, dejanja in vedenja.

V tem tečaju uporabljamo **Microsoft Foundry Agent Service** kot našo glavno platformo. Podpira:

- Modele od ponudnikov, kot so OpenAI, Mistral in Meta (Llama)
- Licencirane podatke od ponudnikov, kot je Tripadvisor
- Standardizirane definicije orodij OpenAPI 3.0

### Agentni vzorci

Komunicirate z LLM-ji preko pozivov (prompts). Pri agentih ne morete vedno ročno izdelati vsakega poziva — agent mora lahko delovati skozi več korakov. Tu pridejo na vrsto **agentni vzorci**. To so ponovno uporabne strategije za pozivanje in usklajevanje LLM-jev na bolj razširljiv in zanesljiv način.

Ta tečaj je zgrajen okoli najpogostejših in najbolj uporabnih agentnih vzorcev.

### Agentni okviri

Agentni okviri razvijalcem nudijo pripravljene predloge, orodja in infrastrukturo za gradnjo agentov. Poenostavljajo:

- Povezovanje orodij in zmogljivosti
- Opazovanje, kaj agent počne (in odpravljanje napak, ko gre kaj narobe)
- Sodelovanje med več agenti

V tem tečaju se osredotočamo na **Microsoft Agent Framework (MAF)** za gradnjo produkcijsko pripravljenih agentov.

---

## Primeri kode

Ste pripravljeni videti delovanje? Tukaj so primeri kode za to lekcijo:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate vprašanja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, obiščete uradne ure in dobite odgovore na vprašanja o AI agentih iz skupnosti.


---

## Preizkušanje tega agenta (neobvezno)

Ko se naučite nameščati agente v [Lekcija 16](../16-deploying-scalable-agents/README.md), lahko dodate hitro zdravstveno preverjanje po namestitvi za agent `TravelAgent` iz te lekcije s pripravljeno zbirko [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Oglejte si [`tests/README.md`](../tests/README.md) za navodila, kako ga zagnati.

---

## Prejšnja lekcija

[Nastavitev tečaja](../00-course-setup/README.md)

## Naslednja lekcija

[Raziskovanje agentnih okvirov](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->