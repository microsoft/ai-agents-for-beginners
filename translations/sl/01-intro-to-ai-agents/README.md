[![Uvod v AI agente](../../../translated_images/sl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na zgornjo sliko, da si ogledate video za to lekcijo)_

# Uvod v AI agente in primere uporabe agentov

Dobrodošli v tečaj **AI agenti za začetnike**! Ta tečaj vam nudi osnovno znanje — in delujočo kodo — za začetek gradnje AI agentov iz nič.

Pridite in se pozdravite v <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord skupnosti</a> — polni je učencev in graditeljev AI, ki z veseljem odgovarjajo na vprašanja.

Preden začnemo z gradnjo, se prepričajmo, da res razumemo, kaj AI agent *je* in kdaj je smiselno uporabiti enega.

---

## Uvod

Ta lekcija obravnava:

- Kaj so AI agenti in različne vrste, ki obstajajo
- Za katere vrste nalog so AI agenti najbolj primerni
- Osnovni gradniki, ki jih boste uporabili pri oblikovanju agentne rešitve

## Cilji učenja

Na koncu te lekcije bi morali biti sposobni:

- Razložiti, kaj je AI agent in kako se razlikuje od običajne AI rešitve
- Vedeti, kdaj uporabiti AI agenta (in kdaj ne)
- Načrtovati osnovno zasnovo agentne rešitve za resničen problem

---

## Definiranje AI agentov in vrst AI agentov

### Kaj so AI agenti?

Tukaj je enostaven način za razumevanje:

> **AI agenti so sistemi, ki Large Language Models (LLM) dejansko *naredijo stvari* — tako, da jim ponudijo orodja in znanje za delovanje v svetu, ne samo za odgovarjanje na pozive.**

Poglejmo si to podrobneje:

- **Sistem** — AI agent ni samo ena stvar. Je zbirka delov, ki delujejo skupaj. Vsak agent ima v jedru tri dele:
  - **Okolje** — Prostor, v katerem agent deluje. Pri agentu za rezervacijo potovanj je to sama platforma za rezervacije.
  - **Senzorji** — Kako agent bere trenutno stanje svojega okolja. Naš potovalni agent lahko preverja razpoložljivost hotelov ali cene letov.
  - **Aktuatorji** — Kako agent ukrepa. Potovalni agent lahko rezervira sobo, pošlje potrditev ali prekliče rezervacijo.

![Kaj so AI agenti?](../../../translated_images/sl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agenti so obstajali že pred LLM, a LLM so tisti, ki moderne agente naredijo tako močne. Razumejo naravni jezik, razmišljajo o kontekstu in nejasno uporabniško zahtevo spremenijo v konkreten načrt dejanj.

- **Izvajanje dejanj** — Brez agentskega sistema LLM zgolj ustvarja besedilo. Znotraj agentnega sistema lahko LLM dejansko *izvede* korake — išče v bazi podatkov, kliče API, pošlje sporočilo.

- **Dostop do orodij** — Katera orodja lahko agent uporablja, je odvisno od (1) okolja v katerem deluje in (2) kaj mu je razvijalec omogočil. Potovalni agent lahko morda išče lete, vendar ne ureja strankinih zapisov — vse je stvar povezav.

- **Spomin + Znanje** — Agenti lahko imajo kratkoročni spomin (trenutni pogovor) in dolgoročni spomin (baza strank, pretekle interakcije). Potovalni agent si lahko "zapomni", da imate raje sedeže ob oknu.

---

### Različne vrste AI agentov

Niso vsi agenti zgrajeni enako. Tukaj je razčlenitev glavnih vrst, pri čemer kot primer uporabljamo potovalnega agenta:

| **Vrsta agenta** | **Kaj počne** | **Primer potovalnega agenta** |
|---|---|---|
| **Preprosti refleksni agenti** | Sledijo strogo določenim pravilom — brez spomina, brez načrtovanja. | Prejme reklamacijo po elektronski pošti → jo posreduje storitvi za stranke. To je vse. |
| **Modelno osnovani refleksni agenti** | Ohranjajo notranji model sveta in ga posodabljajo, ko se stvari spremenijo. | Spremlja zgodovinske cene letov in opozarja na poti, ki so nenadoma drage. |
| **Agenti z vnaprejšnjim ciljem** | Imajo cilj in ugotavljajo, kako ga doseči korak za korakom. | Rezervira celoten izlet (lete, avto, hotel) od vaše trenutne lokacije do cilja. |
| **Agenti na osnovi uporabnosti** | Ne najdejo samo *neke* rešitve — poiščejo *najboljšo* z tehtanjem kompromisov. | Uravnoveša ceno in udobje, da najde potovanje, ki najbolje ustreza vašim željam. |
| **Učeči agenti** | Sčasoma se izboljšujejo z učenjem iz povratnih informacij. | Prilagaja prihodnja priporočila za rezervacije glede na rezultate anket po potovanju. |
| **Hierarhični agenti** | Zgornji agent razdeli delo na podnaloge in jih delegira nižjim agentom. | Zahtevek "prekliči potovanje" se razdeli v: prekliči let, prekliči hotel, prekliči najem avta — vsak obravnava podagent. |
| **Sistemi več agentov (MAS)** | Več neodvisnih agentov, ki delajo skupaj (ali tekmujejo). | Sodelovanje: ločeni agenti skrbijo za hotele, lete in zabavo. Tekmovalno: več agentov tekmuje za najem hotelskih sob po najboljši ceni. |

---

## Kdaj uporabljati AI agente

Samo zato, ker lahko uporabite AI agenta, še ne pomeni, da bi ga vedno morali. Tukaj so situacije, kjer agenti res izstopajo:

![Kdaj uporabljati AI agente?](../../../translated_images/sl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Odprti problemi** — Ko koraki za rešitev problema ne morejo biti vnaprej programirani. Potreben je dinamičen pristop LLM za iskanje poti.
- **Večstopenjski procesi** — Naloge, ki zahtevajo uporabo orodij skozi več korakov, ne samo en sam pogled ali generacijo.
- **Izboljšave s časom** — Ko želite, da sistem postaja pametnejši na podlagi povratnih informacij uporabnikov ali okoljskih signalov.

V lekciji **Gradnja zaupanja vrednih AI agentov** pozneje v tečaju bomo podrobneje raziskali, kdaj (in kdaj *ne*) uporabljati AI agente.

---

## Osnove agentnih rešitev

### Razvoj agenta

Prvo, kar naredite pri gradnji agenta, je definirati *kaj lahko počne* — njegova orodja, dejanja in vedenja.

V tem tečaju uporabljamo **Azure AI Agent Service** kot glavno platformo. Podpira:

- Odprte modele kot so OpenAI, Mistral in Llama
- Licencirane podatke od ponudnikov, kot je Tripadvisor
- Standardizirane definicije orodij OpenAPI 3.0

### Agentni vzorci

Komunicirate z LLM prek pozivov. Pri agentih ne morete vedno ročno izdelati vsakega poziva — agent mora ukrepati skozi več korakov. Tu pridejo na vrsto **agentni vzorci**. To so ponovno uporabne strategije za pozivanje in orkestracijo LLM na bolj skalabilen in zanesljiv način.

Ta tečaj je strukturiran okoli najpogostejših in najbolj uporabnih agentnih vzorcev.

### Agentni okviri

Agentni okviri razvijalcem ponujajo vnaprej pripravljene predloge, orodja in infrastrukturo za gradnjo agentov. Olajšajo:

- Povezovanje orodij in zmogljivosti
- Opazovanje, kaj agent počne (in odpravljanje napak, če gre kaj narobe)
- Sodelovanje med več agenti

V tem tečaju se osredotočamo na **Microsoft Agent Framework (MAF)** za gradnjo agentov pripravljenih za produkcijo.

---

## Primeri kode

Pripravljeni za ogled v praksi? Tukaj so koda primeri za to lekcijo:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate vprašanja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, udeležite pisarnkih ur in dobite odgovore na vprašanja o AI agentih od skupnosti.

---

## Prejšnja lekcija

[Postavitev tečaja](../00-course-setup/README.md)

## Naslednja lekcija

[Raziskovanje agentnih okvirjev](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorno jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->