[![Uvod v AI agente](../../../translated_images/sl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na zgornjo sliko za ogled videoposnetka te lekcije)_


# Uvod v AI agente in primere uporabe agentov

Dobrodošli v tečaju "AI agenti za začetnike"! Ta tečaj nudi temeljno znanje in praktične primere za izdelavo AI agentov.

Pridružite se <a href="https://discord.gg/kzRShWzttr" target="_blank">skupnosti Azure AI na Discordu</a>, da spoznate druge učeče se in razvijalce AI agentov ter postavite vprašanja o tem tečaju.

Za začetek tega tečaja si najprej pridobimo boljše razumevanje, kaj so AI agenti in kako jih lahko uporabimo v aplikacijah in potekih dela, ki jih izdelujemo.

## Uvod

Ta lekcija zajema:

- Kaj so AI agenti in katere so različne vrste agentov?
- Za katere primere uporabe so AI agenti najbolj primerni in kako nam lahko pomagajo?
- Kateri so nekateri osnovni gradniki pri oblikovanju agentnih rešitev?

## Cilji učenja
Po zaključku te lekcije boste morali biti sposobni:

- Razumeti koncepte AI agentov in kako se razlikujejo od drugih AI rešitev.
- Uporabiti AI agente kar se da učinkovito.
- Produktivno zasnovati agentne rešitve tako za uporabnike kot za stranke.

## Opredelitev AI agentov in vrste AI agentov

### Kaj so AI agenti?

AI agenti so **sistemi**, ki omogočajo **Large Language Models(LLMs)**, da **izvedejo dejanja** tako, da razširijo svoje zmogljivosti z dajanjem LLM-jem **dostopa do orodij** in **znanja**.

Razdelimo to definicijo na manjše dele:

- **Sistem** - Pomembno je razmišljati o agentih ne le kot o posamezni komponenti, temveč kot o sistemu mnogih komponent. Na osnovni ravni so komponente AI agenta:
  - **Okolje** - Določeni prostor, v katerem agent deluje. Na primer, če bi imeli potovalnega agenta za rezervacije, bi lahko okolje predstavljal sistem za rezervacijo potovanj, ki ga agent uporablja za dokončanje nalog.
  - **Senzorji** - Okolja imajo informacije in zagotavljajo povratne informacije. AI agenti uporabljajo senzorje za zbiranje in interpretacijo teh informacij o trenutnem stanju okolja. V primeru potovalnega agenta lahko sistem za rezervacije zagotavlja informacije, kot so razpoložljivost hotelov ali cene letov.
  - **Aktuatorji** - Ko AI agent prejme trenutno stanje okolja, za tekočo nalogo določi, katero dejanje izvesti, da spremeni okolje. Pri potovalnem agentu bi to lahko bilo rezerviranje razpoložljive sobe za uporabnika.

![Kaj so AI agenti?](../../../translated_images/sl/what-are-ai-agents.1ec8c4d548af601a.webp)

**Large Language Models** - Koncept agentov je obstajal že pred nastankom LLM-jev. Prednost gradnje AI agentov z LLM-ji je njihova sposobnost interpretacije človeškega jezika in podatkov. Ta sposobnost omogoča LLM-jem, da interpretirajo informacije iz okolja in določijo načrt za spreminjanje okolja.

**Izvajanje dejanj** - Izven sistemov AI agentov so LLM-ji omejeni na situacije, kjer je dejanje generiranje vsebine ali informacij na podlagi poziva uporabnika. Znotraj sistemov AI agentov lahko LLM-ji opravijo naloge tako, da interpretirajo zahtevo uporabnika in uporabijo orodja, ki so na voljo v njihovem okolju.

**Dostop do orodij** - Katera orodja ima LLM na voljo, je določeno 1) z okoljem, v katerem deluje, in 2) z razvijalcem AI agenta. V primeru našega potovalnega agenta so orodja agenta omejena z operacijami, ki so na voljo v rezervacijskem sistemu, in/ali jih lahko razvijalec omeji le na letalske storitve.

**Spomin in znanje** - Spomin je lahko kratkotrajen v kontekstu pogovora med uporabnikom in agentom. Na dolgi rok, zunaj informacij, ki jih zagotavlja okolje, lahko AI agenti pridobivajo znanje iz drugih sistemov, storitev, orodij in celo drugih agentov. V primeru potovalnega agenta bi to znanje lahko predstavljale informacije o uporabnikovih potovalnih preferencah, shranjene v bazi strank.

### Različne vrste agentov

Zdaj, ko imamo splošno definicijo AI agentov, si poglejmo nekaj specifičnih vrst agentov in kako bi jih uporabili v primeru potovalnega agenta.

| **Vrsta agenta**            | **Opis**                                                                                                                             | **Primer**                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preprosti refleksni agenti**      | Izvedejo takojšnje ukrepe na podlagi vnaprej določenih pravil.                                                                                  | Potovalni agent interpretira kontekst e-pošte in posreduje pritožbe glede potovanj službi za pomoč strankam.                                                                                                                          |
| **Refleksni agenti na osnovi modela** | Izvedejo dejanja na podlagi modela sveta in sprememb tega modela.                                                              | Potovalni agent daje prednost premestitvam poti z znatnimi spremembami cen na podlagi dostopa do zgodovinskih podatkov o cenah.                                                                                                             |
| **Agenti, ki temeljijo na ciljih**         | Ustvarijo načrte za dosego specifičnih ciljev z interpretacijo cilja in določanjem dejanj za njegovo dosego.                                  | Potovalni agent rezervira potovanje z določanjem potrebnih potovalnih ureditev (avto, javni prevoz, leti) od trenutne lokacije do cilja.                                                                                |
| **Agenti, ki temeljijo na koristnosti**      | Upoštevajo preference in tehtajo kompromise numerično, da določijo, kako doseči cilje.                                               | Potovalni agent maksimira korist s tehtanjem udobja proti stroškom pri rezervaciji potovanja.                                                                                                                                          |
| **Učeči se agenti**           | Izboljšujejo se skozi čas z odzivanjem na povratne informacije in prilagajanjem dejanj.                                                        | Potovalni agent se izboljša z uporabo povratnih informacij strank iz anket po potovanju, da prilagodi prihodnje rezervacije.                                                                                                               |
| **Hierarhični agenti**       | Vključujejo več agentov v večnivojskem sistemu, pri čemer višjenivojski agent razbije naloge na podnaloge, ki jih dokončajo nižjenivojski agenti. | Potovalni agent prekliče potovanje tako, da nalogo razdeli na podnaloge (na primer preklic posameznih rezervacij) in dovoli nižjenivojskim agentom, da jih dokončajo ter poročajo višjenivojskemu agentu.                                     |
| **Sistemi več agentov (MAS)** | Agenti dokončajo naloge neodvisno, bodisi sodelovalno ali tekmovalno.                                                           | Kooperativno: Več agentov rezervira specifične potovalne storitve, kot so hoteli, leti in zabava. Tekmovalno: Več agentov upravlja in tekmuje za skupni koledar hotelskih rezervacij, da stranke namesti v hotel. |

## Kdaj uporabiti AI agente

V prejšnjem razdelku smo uporabili primer potovalnega agenta, da pojasnimo, kako se različne vrste agentov uporabljajo v različnih scenarijih rezervacij potovanj. Ta aplikacija bo spremljala skozi celoten tečaj.

Poglejmo vrste primerov uporabe, za katere so AI agenti najbolj primerni:

![Kdaj uporabiti AI agente?](../../../translated_images/sl/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Odprte naloge** - omogočanje LLM-ju, da določi potrebne korake za dokončanje naloge, saj jih ni vedno mogoče vnaprej kodirati v potek dela.
- **Večstopenjski procesi** - naloge, ki zahtevajo določeno raven kompleksnosti, pri katerih mora AI agent uporabljati orodja ali informacije skozi več korakov namesto enkratnega pridobivanja.  
- **Izboljševanje skozi čas** - naloge, kjer se agent lahko izboljša skozi čas z zbiranjem povratnih informacij iz okolja ali od uporabnikov, da zagotovi večjo koristnost.

Več premislekov o uporabi AI agentov obravnavamo v lekciji Building Trustworthy AI Agents.

## Osnove agentnih rešitev

### Razvoj agentov

Prvi korak pri oblikovanju sistema AI agenta je opredeliti orodja, dejanja in vedenja. V tem tečaju se osredotočamo na uporabo **Azure AI Agent Service** za opredelitev naših agentov. Ponuja funkcije, kot so:

- Izbira odprtih modelov, kot so OpenAI, Mistral in Llama
- Uporaba licenciranih podatkov prek ponudnikov, kot je Tripadvisor
- Uporaba standardiziranih orodij OpenAPI 3.0

### Agentni vzorci

Komunikacija z LLM-ji poteka prek pozivov (prompts). Glede na deloma avtonomno naravo AI agentov ni vedno mogoče ali potrebno ročno ponovno sprožiti LLM po spremembi v okolju. Uporabljamo **agentne vzorce**, ki nam omogočajo, da LLM nagovorimo skozi več korakov na bolj skalabilen način.

Ta tečaj je razdeljen na nekatere trenutno priljubljene agentne vzorce.

### Agentna ogrodja

Agentna ogrodja razvijalcem omogočajo implementacijo agentnih vzorcev prek kode. Ta ogrodja ponujajo predloge, vtičnike in orodja za boljše sodelovanje agentov. Te koristi zagotavljajo možnosti za boljšo opazljivost in odpravljanje težav v sistemih AI agentov.

V tem tečaju bomo raziskali Microsoft Agent Framework (MAF) za gradnjo proizvodno pripravljenih AI agentov.

## Primeri kode

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Imate še več vprašanj o AI agentih?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učečimi se, obiščete uradne ure in dobite odgovore na vprašanja o AI agentih.

## Prejšnja lekcija

[Nastavitev tečaja](../00-course-setup/README.md)

## Naslednja lekcija

[Raziščite agentna ogrodja](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->