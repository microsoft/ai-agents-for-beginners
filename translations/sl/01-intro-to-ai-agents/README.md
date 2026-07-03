[![Uvod v AI agente](../../../translated_images/sl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite zgornjo sliko za ogled videoposnetka te lekcije)_

# Uvod v AI agente in primere uporabe agentov

Dobrodošli v tečaju **AI agenti za začetnike**! Ta tečaj vam daje osnovno znanje — in dejansko delujočo kodo — za začetek ustvarjanja AI agentov iz nič.

Pridružite se pozdravu v <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord skupnosti</a> — polni je učencev in ustvarjalcev AI, ki z veseljem odgovarjajo na vprašanja.

Preden začnemo z gradnjo, se prepričajmo, da zares razumemo, kaj AI agent *je* in kdaj je smiselno uporabiti enega.

---

## Uvod

Ta lekcija pokriva:

- Kaj so AI agenti in različne vrste, ki obstajajo
- Za kakšne vrste nalog so AI agenti najbolje primerni
- Osnovni gradniki, ki jih boste uporabljali pri oblikovanju agentne rešitve

## Cilji učenja

Do konca te lekcije boste morali znati:

- Razložiti, kaj je AI agent in kako se razlikuje od običajne AI rešitve
- Vedeti, kdaj se poslužiti AI agenta (in kdaj ne)
- Na skici izdelati osnovno zasnovo agentne rešitve za resničen problem

---

## Definicija AI agentov in vrste AI agentov

### Kaj so AI agenti?

Tu je preprost način, kako o tem razmišljati:

> **AI agenti so sistemi, ki omogočajo Velikim jezikovnim modelom (LLM), da dejansko *ukrepajo* — s tem, da jim ponujajo orodja in znanje za delovanje v svetu, ne le odgovarjanje na ukaze.**

Poglejmo malo podrobneje:

- **Sistem** — AI agent ni le ena stvar. Je zbirka delov, ki delujejo skupaj. Vsak agent ima v svoji osnovi tri dele:
  - **Okolje** — prostor, v katerem agent deluje. Za potovalnega agenta bi to bila sama platforma za rezervacije.
  - **Senzorji** — kako agent bere trenutno stanje svojega okolja. Naš potovalni agent lahko preverja razpoložljivost hotelov ali cene letov.
  - **Aktuatorji** — kako agent izvaja dejanja. Potovalni agent lahko rezervira sobo, pošlje potrditev ali prekliče rezervacijo.

![Kaj so AI agenti?](../../../translated_images/sl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veliki jezikovni modeli** — agenti so obstajali tudi pred LLM, a LLM naredijo sodobne agente tako močne. Razumejo naravni jezik, razmišljajo o kontekstu in nejasno uporabniško zahtevo spremenijo v konkreten akcijski načrt.

- **Izvajanje dejanj** — brez agentskega sistema LLM samo generira besedilo. V agentskem sistemu pa lahko LLM dejansko *izvaja* korake — išče po podatkovni bazi, kliče API, pošilja sporočila.

- **Dostop do orodij** — katera orodja agent lahko uporablja, je odvisno (1) od okolja, v katerem teče, in (2) kaj je razvijalec izbral, da mu jih ponudi. Potovalni agent lahko išče po letih, a ne ureja podatkov strank — vse je odvisno, kaj povežete.

- **Spomin + znanje** — agenti imajo lahko kratkoročni spomin (trenutni pogovor) in dolgoročni spomin (baza strank, pretekli stiki). Potovalni agent si lahko "zapomni", da imate raje sedeže ob oknu.

---

### Različne vrste AI agentov

Niso vsi agenti izdelani enako. Tukaj je pregled glavnih vrst, z uporabo potovalnega agenta kot tekočega primera:

| **Vrsta agenta** | **Kaj počne** | **Primer potovalnega agenta** |
|---|---|---|
| **Preprosti refleksni agenti** | Sledijo trdo kodiranim pravilom — brez spomina, brez načrtovanja. | Vidijo pritožbo po e-pošti → posredujejo jo službi za podporo. To je vse. |
| **Modelno temelječi refleksni agenti** | Ohranjajo notranji model sveta in ga posodabljajo, ko se stvari spreminjajo. | Spremljajo zgodovinske cene letov in označujejo poti, ki so nenadoma drage. |
| **Agenti z cilji** | Imajo cilj in postopoma ugotavljajo, kako ga doseči korak za korakom. | Rezervira celotno potovanje (leti, avto, hotel) od vaše trenutne lokacije do cilja. |
| **Agenti, ki temeljijo na uporabnosti** | Ne najdejo le *kakšne* rešitve — najdejo *najboljšo* z ovrednotenjem kompromisov. | Uravnavajo stroške proti udobju in najdejo potovanje, ki najbolje ustreza vašim željam. |
| **Učeči se agenti** | Postajajo boljši s časom na podlagi povratnih informacij. | Prilagajajo prihodnja priporočila za rezervacije na podlagi rezultatov anket po potovanju. |
| **Hierarhični agenti** | Agent na visoki ravni razdeli delo na podnaloge in jih delegira agentom na nižjih ravneh. | Zahtevek "prekliči potovanje" se razdeli na: preklic leta, preklic hotela, preklic najema avtomobila — vsak dela podagent. |
| **Večagentni sistemi (MAS)** | Več neodvisnih agentov, ki delujejo skupaj (ali tekmujejo). | Sodelovanje: ločeni agenti upravljajo hotele, lete in zabavo. Tekmovalno: več agentov tekmuje za polnjenje hotelskih sob po najboljših cenah. |

---

## Kdaj uporabljati AI agente

Le zato, ker *lahko* uporabite AI agenta, ne pomeni, da ga vedno *morate*. Tukaj so situacije, kjer agenti resnično izstopajo:

![Kdaj uporabljati AI agente?](../../../translated_images/sl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Odprti problemi** — ko korakov za rešitev problema ni mogoče vnaprej programirati. LLM mora dinamično ugotoviti pot.
- **Večstopenjski procesi** — naloge, ki zahtevajo uporabo orodij skozi več korakov, ne le en sam ogled ali generiranje.
- **Izboljšave skozi čas** — ko želite, da sistem postaja pametnejši na podlagi povratnih informacij uporabnikov ali signalov iz okolja.

Kasneje v tečaju bomo podrobneje raziskali, kdaj (in kdaj *ne*) uporabljati AI agente, v lekciji **Gradnja zaupanja vrednih AI agentov**.

---

## Osnove agentnih rešitev

### Razvoj agentov

Prva stvar, ki jo naredite pri gradnji agenta, je določiti *kaj lahko počne* — njegova orodja, dejanja in vedenja.

V tem tečaju uporabljamo **Azure AI Agent Service** kot glavno platformo. Podpira:

- Modele od ponudnikov, kot so OpenAI, Mistral in Meta (Llama)
- Licencirane podatke od ponudnikov, kot je Tripadvisor
- Standardizirane definicije orodij OpenAPI 3.0

### Agentni vzorci

Z LLM komunicirate preko pozivov. Pri agentih ne morete vedno ročno izdelati vsak poziv — agent mora ukrepati preko več korakov. Tu pridejo v poštev **agentni vzorci**. So ponovno uporabne strategije za pozivanje in orkestriranje LLM na bolj razširljiv in zanesljiv način.

Ta tečaj je strukturiran okoli najpogostejših in najbolj uporabnih agentnih vzorcev.

### Agentni ogrodji

Agentna ogrodja razvijalcem ponujajo že pripravljene predloge, orodja in infrastrukturo za gradnjo agentov. Olajšajo:

- Povezovanje orodij in zmogljivosti
- Opazovanje, kaj agent počne (in iskanje napak, ko stvari ne delujejo)
- Sodelovanje med več agenti

V tem tečaju se osredotočamo na **Microsoft Agent Framework (MAF)** za gradnjo agentov, pripravljenih za proizvodnjo.

---

## Primeri kode

Ste pripravljeni, da to vidite v akciji? Tukaj so vzorci kode za to lekcijo:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate vprašanja?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) za povezovanje z drugimi učenci, udeležbo na urah odprtih vrat in dobite odgovore na vprašanja o AI agentih skupnosti.


---

## Prejšnja lekcija

[Nastavitev tečaja](../00-course-setup/README.md)

## Naslednja lekcija

[Raziskovanje agentnih ogrodij](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->