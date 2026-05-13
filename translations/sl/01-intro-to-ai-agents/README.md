[![Uvod v AI agente](../../../translated_images/sl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na sliko zgoraj, da si ogledate video tega gradiva)_

# Uvod v AI agente in primere uporabe agentov

Dobrodošli v tečaju **AI agenti za začetnike**! Ta tečaj vam zagotavlja temeljno znanje — in dejansko delujočo kodo — za začetek gradnje AI agentov od začetka.

Pridružite se nam in pozdravite v <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord skupnosti</a> — polni je učencev in graditeljev AI, ki z veseljem odgovorijo na vprašanja.

Preden začnemo graditi, poskrbimo, da v resnici razumemo, kaj AI agent *je* in kdaj ima smisel uporabiti ga.

---

## Uvod

Ta lekcija zajema:

- Kaj so AI agenti in vrste agentov, ki obstajajo
- Za katere vrste nalog so AI agenti najbolj primerni
- Osnovne gradnike, ki jih boste uporabili pri načrtovanju agentne rešitve

## Cilji učenja

Do konca te lekcije bi morali znati:

- Razložiti, kaj je AI agent in kako se razlikuje od običajne AI rešitve
- Prepoznati, kdaj poseči po AI agentu (in kdaj ne)
- Narisati osnovni načrt agentne rešitve za problem iz resničnega sveta

---

## Definicija AI agentov in vrste AI agentov

### Kaj so AI agenti?

Tu je preprost način razmišljanja:

> **AI agenti so sistemi, ki Large Language Models (LLM) dejansko *dovolijo, da nekaj počnejo* — tako, da jim dajo orodja in znanje za delovanje na svetu, ne le za odgovarjanje na pozive.**

Poglejmo to podrobneje:

- **Sistem** — AI agent ni samo ena stvar. Je zbirka delov, ki delujejo skupaj. Osnovno ima vsak agent tri dele:
  - **Okolje** — prostor, v katerem agent deluje. Za turističnega agenta je to sama platforma za rezervacije.
  - **Senzorji** — kako agent bere trenutno stanje svojega okolja. Naš turistični agent lahko preveri razpoložljivost hotelov ali cene letov.
  - **Aktuatorji** — kako agent ukrepa. Turistični agent lahko rezervira sobo, pošlje potrditev ali prekliče rezervacijo.

![Kaj so AI agenti?](../../../translated_images/sl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agentje so obstajali pred LLM, vendar so LLM tisti, ki sodobne agente naredijo tako zmogljive. Razumejo naravni jezik, razmišljajo o kontekstu in nejasno uporabniško zahtevo spremenijo v konkreten načrt.

- **Izvajanje dejanj** — Brez sistema agenta LLM zgolj generira besedilo. V sistemu agenta pa LLM dejansko *izvede* korake — išče v podatkovni bazi, kliče API, pošilja sporočila.

- **Dostop do orodij** — Katere orodja agent lahko uporablja, je odvisno od (1) okolja, v katerem deluje, in (2) kaj mu je razvijalec omogočil. Turistični agent lahko išče lete, a ne ureja podatkov o strankah — vse je odvisno od povezav.

- **Spomin + Znanje** — Agent ima lahko kratkoročni spomin (trenutni pogovor) in dolgoročni spomin (bazo strank, pretekle interakcije). Turistični agent si lahko "zapomni", da imate raje sedeže ob oknu.

---

### Različne vrste AI agentov

Niso vsi agenti narejeni enako. Tu je razčlenitev glavnih vrst, z uporabo turističnega agenta kot primera:

| **Vrsta agenta** | **Kaj počne** | **Primer turističnega agenta** |
|---|---|---|
| **Preprosti refleksni agenti** | Sledi vnaprej napisanih pravilom — brez spomina, brez načrtovanja. | Prebere pritožbeno e-pošto → posreduje jo službi za pomoč strankam. To je vse. |
| **Modelno osnovani refleksni agenti** | Ohranja notranji model sveta in ga posodablja ob spremembah. | Sledi zgodovinskim cenam letov in označi nenadno drage poti. |
| **Agent s ciljem** | Ima določen cilj in postopoma izračuna, kako ga doseči. | Rezervira celotno potovanje (leti, avto, hotel) iz vaše trenutne lokacije do cilja. |
| **Agent z uporabnostjo** | Ne najde le *neke* rešitve — najde *najboljšo* z tehtanjem kompromisov. | Uravnava stroške proti udobju, da najde potovanje, ki najbolj ustreza vašim željam. |
| **Učeči agenti** | Postanejo boljši skozi čas z učenjem iz povratnih informacij. | Prilagaja prihodnja priporočila za rezervacije glede na rezultate anket po potovanju. |
| **Hierarhični agenti** | Višji agent razdeli delo na podnaloge in jih delegira nižjim agentom. | Zahteva "preklic potovanja" razdeli na: prekini let, prekini hotel, prekini najem avta — vsak od tega ureja podagent. |
| **Sistemi z več agenti (MAS)** | Več samostojnih agentov dela skupaj (ali tekmuje). | Sodelovanje: ločeni agenti urejajo hotele, lete in zabavo. Tekmovanje: več agentov tekmuje za rezervacijo hotelskih sob po najboljših cenah. |

---

## Kdaj uporabljati AI agente

Samo zato, ker lahko uporabite AI agenta, še ne pomeni, da vedno morate. Tukaj so situacije, kjer se agenti res najbolje izkažejo:

![Kdaj uporabljati AI agente?](../../../translated_images/sl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Odprti problemi** — ko koraki za rešitev problema ne morejo biti vnaprej programirani. LLM mora dinamično izračunati pot.
- **Večstopenjski postopki** — naloge, ki zahtevajo uporabo orodij skozi več korakov, ne le en sam klic ali generiranje.
- **Izboljševanje skozi čas** — ko želite, da sistem postane pametnejši na podlagi povratnih informacij uporabnikov ali signalov iz okolja.

Več bomo raziskali o tem, kdaj (in kdaj *ne*) uporabiti AI agente v lekciji **Gradnja zaupanja vrednih AI agentov** pozneje v tečaju.

---

## Osnove agentnih rešitev

### Razvoj agenta

Prva stvar, ki jo naredite pri gradnji agenta, je definirati *kaj lahko počne* — njegova orodja, dejanja in vedenja.

V tem tečaju uporabljamo **Azure AI Agent Service** kot glavno platformo. Podpira:

- Modele ponudnikov kot so OpenAI, Mistral in Meta (Llama)
- Licencirane podatke od ponudnikov kot je Tripadvisor
- Standardizirane definicije orodij OpenAPI 3.0

### Agentni vzorci

S LLM komunicirate preko pozivov. Pri agentih ne morete vsak poziv ročno izdelati — agent mora ukrepati skozi več korakov. Tu pridejo na vrsto **agentni vzorci**. So ponovno uporabne strategije za spodbujanje in usklajevanje LLM v bolj razširljiv in zanesljiv način.

Ta tečaj je strukturiran okoli najpogostejših in najbolj uporabnih agentnih vzorcev.

### Agentni ogrodji

Agentni ogrodji razvijalcem nudijo vnaprej pripravljene predloge, orodja in infrastrukturo za gradnjo agentov. Omogočajo lažje:

- Povezovanje orodij in zmožnosti
- Opazovanje, kaj agent počne (in odpravljanje napak, ko kaj ne deluje)
- Sodelovanje med več agenti

V tem tečaju se osredotočamo na **Microsoft Agent Framework (MAF)** za izdelavo agentov, pripravljenih za produkcijo.

---

## Primeri kode

Pripravljeni, da vidite to v praksi? Tukaj so primeri kode za to lekcijo:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate vprašanja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, sodelujete na urah pomoči in dobite odgovore na vprašanja o AI agentih od skupnosti.

---

## Prejšnja lekcija

[Priprava tečaja](../00-course-setup/README.md)

## Naslednja lekcija

[Raziskovanje agentnih ogrodij](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->