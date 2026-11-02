# AI agenti za začetnike - študijski vodič

Ta vodič uporabite kot praktičnega spremljevalca med tečajem. Ni
namen nadomestiti lekcij. Pomaga vam odločiti, kje začeti, kaj
iskati v posamezni lekciji in kako ideje povezati v majhen delujoč agent
demonstracijo.

Če ste tukaj prvič, začnite preprosto:

1. Preberite [nastavitev tečaja](./00-course-setup/README.md).
2. Dokončajte lekcije 01-06 po vrsti.
3. Med učenjem imejte v mislih eno majhno idejo za demo.
4. Po vsaki lekciji vprašajte: "Kaj lahko moj agent zdaj naredi, česar prej ni
   zmogel?"

## Preprosta demo ideja za spominjanje

Dober način za učenje agentov je, da sledite eni demo ideji skozi tečaj.

Primer demoja: **agent pomočnik za tečaj**.

Uporabnik vpraša:

> "Želim se naučiti, kako agenti uporabljajo orodja. Najdi prave lekcije, povzem
> kaj naj najprej preberem in mi daj kratek praktični izziv."

Navaden klepetalni robot lahko odgovori iz tega, kar že ve. Agent lahko naredi več:

1. **Prebere ali poišče datoteke tečaja** za iskanje pravih lekcij.
2. **Uporabi orodja** za pridobitev povezav do lekcij, primerov ali gradiva.
3. **Načrtuje** kratek učni načrt namesto enega dolgega odgovora.
4. **Uporabi kontekst** trenutnega pogovora, da ostane osredotočen na cilj učenca.
5. **Se spomni uporabnih nastavitev**, če aplikacija podpira shranjevanje.
6. **Prikaže sledi, navedbe ali dnevnike**, da uporabnik razume, kaj se je zgodilo.
7. **Uporabi zaščitne ukrepe** pred tveganimi dejanji ali uporabo občutljivih podatkov.


zmožnost bi ta lekcija dodala?


## K čemu stremite

Do konca tečaja bi morali znati razložiti in zgraditi agentske sisteme,
ki združujejo te dele:

| Del | Pomen v običajnem jeziku | V demoju |
|------|------------------------|-------------|
| Model | Razumski motor, ki interpretira zahtevo uporabnika | Razume, da učenec želi lekcije o uporabi orodij |
| Orodja | Funkcije, API-ji, datoteke, brskalniki ali storitve, ki jih agent lahko uporablja | Iskanje po repozitoriju ali pridobivanje vsebin lekcij |
| Znanje | Dokumenti ali podatki uporabljeni za utemeljitev odgovora | README datoteke in gradivo tečaja |
| Kontekst | Informacije vključene v naslednji klic modela | Cilj uporabnika in rezultati orodij |
| Spomin | Informacije shranjene za kasnejšo uporabo | Učenčeve preference glede praktičnih primerov v Pythonu |
| Načrtovanje | Razbijanje večjega cilja na manjše korake | Iskanje lekcij, povzemanje, predlaganje vaje |
| Orkestracija | Usmerjanje dela med orodja, korake ali agente | Načrtovalec pokliče iskalno orodje, nato povzemalnik |
| Zaupanje | Varnost, zaščita, ocenjevanje in opazovanje | Beleženje klicev orodij in vprašanje pred tveganimi dejanji |

## Modeli in ponudniki

Kode vzorcih v tečaju uporabljajo **Microsoft Agent Framework (MAF)** in ciljajo na **Azure OpenAI Responses API** — priporočeni API za prihodnost, ki združuje klepetalne dokončave, klice orodij, multimodalni vhod in ohranjene pogovore v enem vmesniku API. Povežete se bodisi prek **Microsoft Foundry** projekta (z `FoundryChatClient`), bodisi neposredno do Azure OpenAI (z `OpenAIChatClient`).

Med prehodom skozi lekcije imate nekaj možnosti ponudnikov:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — glavni način, uporabljen v lekcijah. Prijavite se z `az login` za prijavo z Entra ID brez ključev.
- **Foundry Local** — modeli tečejo povsem lokalno prek OpenAI združljivega API-ja (brez oblaka, brez ključev API). Idealno za offline ali brezplačne eksperimente. Glej [nastavitev tečaja](./00-course-setup/README.md).
- **MiniMax** — združljiv ponudnik OpenAI z modeli z velikim kontekstom, uporaben kot nadomestek za vstavitev.

> **Opomba:** GitHub modeli so zastareli (upokojeni julija 2026) in ne podpirajo Responses API. Vzorci so bili posodobljeni za uporabo Azure OpenAI / Microsoft Foundry.

## Izberite svojo učno pot

Lahko opravite celoten tečaj po vrsti ali skočite na pot glede na to, kaj želite
zgraditi.

| Če želite... | Začnite z | Nato študirajte |
|-----------------------|------------|------------|
| Razumeti, kaj so agenti | 01, 02, 03 | 04, 05, 06 |
| Zgraditi agenta, ki uporablja orodja | 04 | 05, 07, 14 |
| Zgraditi agenta na osnovi RAG | 05 | 04, 06, 12 |
| Oblikovati večstopenjske delovne tokove | 07 | 08, 09, 14 |
| Razumeti večagentske sisteme | 08 | 07, 09, 11 |
| Pripraviti agente za produkcijo | 06, 10 | 12, 13, 16, 18 |
| Namestiti in skalirati agente na Foundry | 10, 16 | 06, 13, 18 |
| Zgraditi lokalne / offline-first agente | 17 | 04, 05, 11 |
| Raziskati protokole in avtomatizacijo brskalnika | 11, 15 | 10, 18 |

Namig: če ste novi pri agentih, ne preskakujte lekcij 01-06. Dajo vam
besedišče, ki ga boste potrebovali za preostanek tečaja.

## Vodnik po lekcijah

| Lekcija | Kaj se naučite | Poskusite po lekciji |
|--------|----------------|---------------------------|
| [01 - Uvod v AI agente](./01-intro-to-ai-agents/README.md) | Kaj naredi agenta drugačnega od osnovnega klepetalnega robota. | Pojasnite svojo demo idejo kot agent, ne le kot klepetalno aplikacijo. |
| [02 - Agentni okvirji](./02-explore-agentic-frameworks/README.md) | Kako okvirji pomagajo pri modelih, orodjih, stanju in delovnih tokovih. | Določite, katere dele vaše demo bi upravljal okvir. |
| [03 - Agentni oblikovalski vzorci](./03-agentic-design-patterns/README.md) | Pogosti vzorci za oblikovanje agentskega vedenja. | Narišite uporabnikovo pot pred pisanjem kode. |
| [04 - Uporaba orodij](./04-tool-use/README.md) | Kako agenti kličejo orodja za pridobivanje podatkov ali izvajanje dejanj. | Določite eno orodje, ki ga vaš demo agent potrebuje. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako pridobivanje utemeljuje agentove odgovore v dokumentih ali podatkih. | Odločite, kateri vir znanja naj vaš demo išče. |
| [06 - Zanesljivi agenti](./06-building-trustworthy-agents/README.md) | Kako dodati zaščitne ukrepe, nadzor in varnejše vedenje. | Dodajte eno pravilo, kdaj naj agent najprej vpraša uporabnika. |
| [07 - Načrtovanje oblikovanja](./07-planning-design/README.md) | Kako agenti razbijejo večje cilje na manjše korake. | Napišite trikorakni načrt za vaš demo zahtevek. |
| [08 - Večagentno oblikovanje](./08-multi-agent/README.md) | Kdaj razdeliti delo med specializirane agente. | Odločite se, ali vaš demo potrebuje enega ali več agentov. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako lahko agenti pregledajo in izboljšajo svoj izhod. | Dodajte končno samopreverjanje pred agentovim odgovorom. |
| [10 - AI agenti v produkciji](./10-ai-agents-production/README.md) | Kaj se spremeni, ko agent preide iz demo faze v produkcijo. | Naštejte, kaj bi spremljali: kakovost, stroške, zamude, napake. |
| [11 - Agentni protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezujejo agente z orodji in drugimi agenti. | Določite, kje bi standardni protokol olajšal integracijo. |
| [12 - Inženiring konteksta](./12-context-engineering/README.md) | Kako izbrati, skrajšati, izolirati in upravljati kontekst. | Odločite, kaj spada v poziv in kaj naj ostane zunaj. |
| [13 - Spomin agenta](./13-agent-memory/README.md) | Kako lahko agenti shranjujejo uporabne informacije med interakcijami. | Izberite eno varno nastavitev, ki si jo lahko vaš demo zapomni. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Posebni gradniki okvirja za agente in delovne tokove, plus gostovanje LangChain/LangGraph agentov na Microsoft Foundry. | Preslikajte korake vašega demoja na koncepte okvirja. |
| [15 - Agentni za uporabo računalnika](./15-browser-use/README.md) | Kako agenti lahko sodelujejo z brskalniki ali uporabniškimi vmesniki, vključno s primeri iz resničnega sveta, kot je Microsoft Project Opal. | Izberite eno brskalniško nalogo, ki bi še vedno zahtevala potrditev uporabnika. |
| [16 - Namestitev skalabilnih agentov](./16-deploying-scalable-agents/README.md) | Kako agenta od prototipa pripeljati do skalabilne, opazne produkcijske namestitve na Microsoft Foundry (gostujoči agenti, usmerjanje modelov, predpomnjenje, nadzorni mehanizmi, testi delovanja). | Naštejte produkcijske skrbi, ki jih vaš demo še potrebuje: gostovanje, usmerjanje, stroške, ocenjevanje. |
| [17 - Ustvarjanje lokalnih AI agentov](./17-creating-local-ai-agents/README.md) | Kako narediti lokalno-primerne agente, ki tečejo popolnoma na vašem računalniku z Foundry Local in Qwen (lokalna orodja, lokalni RAG, lokalni MCP). | Odločite, kateri deli vašega demoja naj ostanejo zasebni in tečejo lokalno. |
| [18 - Varnost AI agentov](./18-securing-ai-agents/README.md) | Kako narediti dejanja agenta bolj pregledna in odporna proti manipulacijam. | Odločite, katera dejanja v vašem demoju naj se beležijo ali prejmejo potrdila. |

## Validacija nameščenih agentov z dima testi

Ko namestite agenta (lekcija 16), je **dimni test** najcenejša prva
preverba, ali namestitev dejansko odgovarja. Ta repozitorij vsebuje pripravljene
kataloge pod [tests/](./tests/README.md) za nameščene agente v lekcijah
01, 04, 05 in 16, povezane z
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
dejanjem. Zaženite jih iz zavihka **Dejanja** po namestitvi lekcijskega agenta.
Dimni testi so prvi filter — offline in online vrednotenje (lekciji 10 in 16)
povedo, kako *dober* je agent.

## Ključne ideje v jezik prijazen začetnikom

### Orodja

Orodje je nekaj, kar agent lahko pokliče za delo zunaj modela. Dobro orodje
ima jasno ime, ozko nalogo, tipizirane vhode, predvidljiv izhod in varen način
za neuspeh.

Za demo pomočnika tečaja je orodje lahko:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG in znanje

RAG agentu pomaga odgovarjati iz vira, namesto da bi ugibal. V tem
tečaju so lahko viri README datoteke lekcij, vzorci kode ali zunanji
viri povezani z lekcijami.

Uporabite RAG, ko mora biti odgovor utemeljen v dokumentih, podatkih ali trenutnih
datotekah projekta.

### Načrtovanje

Načrtovanje je koristno, ko zahtevek vsebuje več korakov. Naj bodo načrti kratki in
dovolj vidni, da jih lahko pregleda razvijalec ali uporabnik.

Za demo bi bil načrt lahko:

1. Najdi lekcije povezane z uporabo orodij.
2. Povzemi najbolj relevantne lekcije.
3. Priporoči eno praktično nalogo.

### Kontekst

Kontekst je, kar model vidi v tem trenutku. Premajhen kontekst lahko agentu
prepreči opaziti pomembne podrobnosti. Preveč konteksta lahko agenta naredi počasnejšega,
dražjega ali lažje zmedenega.

Dobro inženirstvo konteksta pomeni izbrati prave informacije za naslednji klic modela.




Shranjujte informacije le, ko so koristne, varne in jih je enostavno posodobiti ali izbrisati.


Na primer, spominjanje "učenec raje praktične primere v Pythonu" je lahko koristno.
Spominjanje občutljivih osebnih podatkov običajno ni.

### Ocenjevanje in opazovanje

Ocenjevanje sprašuje: ali je agent naredil prav?

Opazovanje sprašuje: ali lahko vidimo, kako se je to zgodilo?

Za produkcijske agente beležite klice modela, klice orodij, pridobljeni kontekst,
zamude, stroške, napake in povratne informacije uporabnikov.

### Zaupanje in varnost

Zanesljivi agenti potrebujejo več od prijaznega poziva. Uporabljajte orodja z najmanjšimi privilegiji,
človeško odobritev za tvegana dejanja, maskiranje podatkov tam, kjer je potrebno, in dnevnike ali
potrdila za dejanja, ki jih je treba pregledovati.

## 15-minutna pregledna rutina

Uporabite to rutino po vsaki lekciji:

1. **Povzemite lekcijo v eni povedi.**
2. **Poimenujte novo agentno zmožnost.** Na primer: uporaba orodij, pridobivanje,
   načrtovanje, spomin, opazovanje ali varnost.
3. **Dodajte jo demo pomoči za tečaj.** Kaj se zdaj spremeni v demoju?
4. **Poiščite tveganje.** Kaj bi lahko šlo narobe, če se ta zmožnost zlorabi?
5. **Napišite eno testno vprašanje.** Kako bi preverili, da agent dobro deluje?

## Hiter samopregled

Pred nadaljevanjem poskusite odgovoriti na ta vprašanja:

1. Kaj agent lahko naredi, česar osnovni klepetalni robot sam ne zmore?
2. Katero orodje bi vaš agent potreboval najprej in zakaj?
3. Kateri vir znanja bi moral utemeljiti agentov odgovor?
4. Kakšen kontekst naj bo vključen v naslednji klic modela?
5. Kaj naj si agent zapomni in česa naj ne shranjuje?
6. Kdaj naj agent zahteva človeško odobritev?
7. Kateri dnevniki, sledovi ali potrdila bi vam pomagali kasneje odpraviti težave ali pregledati agenta?


## Predlagana zaključna vaja

Na koncu tečaja zgradite majhnega agenta, ki pomaga učenčku premikati se po tem
repozitoriju.

Minimalna različica:

- Sprejme temo od uporabnika.
- Poišče najbolj relevantne lekcije.
- Povzame, kaj je treba prebrati najprej.
- Predlaga eno praktično nalogo.
- Pokaže, katere datoteke lekcije ali povezave so bile uporabljene.

Razširjena različica:

- Zapomni si učenčev izbrani programski jezik.
- Pred odgovorom uporabi preprost načrt.
- Dodaj korak samopregleda pred končnim odgovorom.
- Beleži klice orodij in pridobljene vire.
- Pred odpiranjem brskalnika ali nalog avtomatizacije UI zahteva potrditev.

To vam daje majhen, a realističen način za vadbo orodij, RAG, načrtovanja,
konteksta, spomina, opazovanja in zaupanja v enem projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->