# AI agenti za začetnike - študijski vodnik

Ta vodič uporabite kot praktični spremljevalec med potekom tečaja. Ni
namenjen nadomeščanju lekcij. Pomoči vam določiti, kje začeti, kaj
iskati v vsaki lekciji in kako povezati ideje v majhen delujoč agent
demo.

Če ste tukaj prvič, začnite preprosto:

1. Preberite [Nastavitev tečaja](./00-course-setup/README.md).
2. Dokončajte lekcije 01-06 po vrsti.
3. Med učenjem imejte v mislih eno majhno idejo za demo.
4. Po vsaki lekciji vprašajte: "Kaj lahko moj agent zdaj naredi, česar prej ni
   zmogel?"

## Preprost demo, ki ga imejte v mislih

Dober način za učenje agentov je, da skozi tečaj sledite eni demo ideji.

Primer demoa: **agent pomočnik pri tečaju**.

Uporabnik vpraša:

> "Želim se naučiti, kako agenti uporabljajo orodja. Poišči prave lekcije, povzem',
> kaj naj najprej preberem, in mi daj kratek praktični nalogo."

Navaden klepetalni robot odgovori na podlagi tega, kar že ve. Agent zmore več:

1. **Preberi ali poišči datoteke tečaja**, da najdeš prave lekcije.
2. **Uporabi orodja** za pridobivanje povezav do lekcij, primerov ali gradiv.
3. **Načrtuj** kratek učni načrt namesto da podaš en dolg odgovor.
4. **Uporabi kontekst** trenutnega pogovora za osredotočenost na cilj učenca.
5. **Zapomni si uporabne preference**, če aplikacija podpira pomnenje.
6. **Pokaži sledove, navedke ali zapise**, da uporabnik razume, kaj se je zgodilo.
7. **Uporabi zaščitne ukrepe** pred tveganimi dejanji ali uporabo občutljivih podatkov.


zmožnost bi jo ta lekcija dodala?


## Kaj gradite

Ob koncu tečaja bi morali znati razložiti in zgraditi agentske sisteme,
ki združujejo te dele:

| Del | Pomen v preprostem jeziku | V demu |
|------|------------------------|-------------|
| Model | Mehanizem za razmišljanje, ki interpretira uporabnikovo zahtevo | Razume, da učenec želi lekcije o uporabi orodij |
| Orodja | Funkcije, API-ji, datoteke, brskalniki ali storitve, ki jih agent lahko uporablja | Išče v repozitoriju ali pridobiva vsebino lekcij |
| Znanje | Dokumenti ali podatki, ki podpirajo odgovor | Datoteke README tečaja in gradivo lekcij |
| Kontekst | Informacije, vključene v naslednji klic modela | Cilj uporabnika in rezultati orodij |
| Pomnilnik | Informacije, shranjene za kasnejšo uporabo | Učenec ima raje praktične primere v Python |
| Načrtovanje | Razbijanje večjega cilja na manjše korake | Poišči lekcije, povzemaj jih, predlagaj vaje |
| Usklajevanje | Usmerjanje dela med orodji, koraki ali agenti | Načrtovalec pokliče iskalno orodje, nato povzemač |
| Zaupanje | Varnost, zaščita, ocenjevanje in opazovanje | Zabeleži klice orodij in vpraša pred pomembnimi dejanji |

## Modeli in ponudniki

Vzorce kode tečaja uporabljajo **Microsoft Agent Framework (MAF)** in ciljajo na **Azure OpenAI Responses API** — priporočen API za naprej, ki združuje klepetalne zaključke, klicanje orodij, multimodalne vnose in pogovore s stanjem v enotnem API-ju. Povežete se bodisi preko projekta **Microsoft Foundry** (z `FoundryChatClient`) ali neposredno v Azure OpenAI (z `OpenAIChatClient`).

Ko delate skozi lekcije, imate nekaj možnosti ponudnikov:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — glavni potek, uporabljen v lekcijah. Prijavite se z `az login` za preverjanje pristnosti Entra ID brez ključev.
- **Foundry Local** — zaženite modele povsem lokalno preko OpenAI združljivega API-ja (brez oblaka, brez API ključev). Idealen za delo brez povezave ali brezplačno eksperimentiranje. Oglejte si [Nastavitev tečaja](./00-course-setup/README.md).
- **MiniMax** — OpenAI združljiv ponudnik z modeli za velik kontekst, uporaben kot zamenjava brez sprememb.

> **Opomba:** GitHub Models je zastarel (upad do julija 2026) in ne podpira Responses API. Vzorci so posodobljeni za uporabo Azure OpenAI / Microsoft Foundry.

## Izberite svojo učni pot

Lahko opravite celoten tečaj po vrsti ali skočite na pot glede na to,
kaj želite zgraditi.

| Če želite... | Začnite s | Potem se učite |
|-----------------------|------------|------------|
| Razumeti, kaj agenti so | 01, 02, 03 | 04, 05, 06 |
| Zgraditi agenta, ki uporablja orodja | 04 | 05, 07, 14 |
| Zgraditi agenta na osnovi RAG | 05 | 04, 06, 12 |
| Oblikovati večstopenjske delovne tokove | 07 | 08, 09, 14 |
| Razumeti sisteme z več agenti | 08 | 07, 09, 11 |
| Pripraviti agente za produkcijo | 06, 10 | 12, 13, 18 |
| Raziščite protokole in avtomatizacijo brskalnika | 11, 15 | 10, 18 |

Nasvet: če ste novi pri agentih, ne preskočite lekcij 01-06. Dajo vam
besedišče, ki ga boste potrebovali za preostanek tečaja.

## Vodnik lekcija za lekcijo

| Lekcija | Kaj se naučite | Poizkusite to po lekciji |
|--------|----------------|---------------------------|
| [01 - Uvod v AI agente](./01-intro-to-ai-agents/README.md) | Kaj razlikuje agenta od osnovnega klepetalnega robota. | Razložite svojo idejo za demo kot agent, ne le kot klepetalno aplikacijo. |
| [02 - Agentni okviri](./02-explore-agentic-frameworks/README.md) | Kako okviri pomagajo z modeli, orodji, stanjem in delovnimi tokovi. | Določite, katere dele demo bi upravljal okvir. |
| [03 - Agentni oblikovni vzorci](./03-agentic-design-patterns/README.md) | Pogosti vzorci za oblikovanje vedenja agentov. | Narišite uporabniško pot pred pisanjem kode. |
| [04 - Uporaba orodij](./04-tool-use/README.md) | Kako agenti kličejo orodja za pridobivanje podatkov ali sprejemanje ukrepov. | Določite eno orodje, ki bi ga vaš agent pri demo potreboval. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako pridobivanje podpira agentove odgovore v dokumentih ali podatkih. | Odločite, kateri vir znanja naj demo išče. |
| [06 - Zanesljivi agenti](./06-building-trustworthy-agents/README.md) | Kako dodati zaščite, nadzor in varnejše vedenje. | Dodajte eno pravilo, kdaj naj agent najprej vpraša uporabnika. |
| [07 - Oblikovanje načrtovanja](./07-planning-design/README.md) | Kako agenti razbijejo večje cilje na manjše korake. | Napišite tri-stopenjski načrt za zahtevo v demo. |
| [08 - Večagentno oblikovanje](./08-multi-agent/README.md) | Kdaj razdeliti delo med specializirane agente. | Odločite, ali vaš demo potrebuje enega ali več agentov. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako lahko agenti pregledajo in izboljšajo svoj rezultat. | Dodajte zaključni samopregled pred odgovorom agenta. |
| [10 - AI agenti v produkciji](./10-ai-agents-production/README.md) | Kaj se spremeni, ko agent preide iz demoa v produkcijo. | Navedite, kaj bi nadzirali: kakovost, stroške, zakasnitve, napake. |
| [11 - Agentni protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezujejo agente z orodji in drugimi agenti. | Določite, kje bi standardni protokol poenostavil integracijo. |
| [12 - Inženiring konteksta](./12-context-engineering/README.md) | Kako izbrati, obrezati, izolirati in upravljati kontekst. | Odločite, kaj naj bo v pozivu in kaj naj ostane zunaj. |
| [13 - Pomnilnik agenta](./13-agent-memory/README.md) | Kako agenti shranjujejo uporabne informacije med interakcijami. | Izberite eno varno prednost, ki bi jo demo lahko zapomnil. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Okvirno-specifične gradnike za agente in delovne tokove ter gostovanje LangChain/LangGraph agentov na Microsoft Foundry. | Povežite korake svojega demoa s koncepti okvirja. |
| [15 - Agentni za uporabo računalnika](./15-browser-use/README.md) | Kako agenti lahko upravljajo brskalnik ali uporabniški vmesnik, vključno z resničnimi primeri kot Microsoft Project Opal. | Izberite eno opravilo v brskalniku, ki še vedno zahteva potrditev uporabnika. |
| [18 - Zavarovanje AI agentov](./18-securing-ai-agents/README.md) | Kako narediti agentna dejanja bolj revidirana in odporna na manipulacije. | Odločite, katera dejanja v demo naj se beležijo ali potrdijo. |

Lekcije 16 in 17 so omenjene v glavnem README kot kmalu na voljo. Dodajte jih v svoj
študijski načrt, ko bo vsebina lekcij na voljo.

## Ključne ideje v prijaznih izrazih za začetnike

### Orodja

Orodje je nekaj, kar agent lahko pokliče za delo zunaj modela. Dobro orodje
ima jasno ime, ozko nalogo, tipizirane vhode, predvidljiv izhod in varen način
za neuspeh.

Za demo pomočnika tečaja bi orodje lahko bilo:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG in Znanje

RAG agentu pomaga odgovarjati iz izvornega materiala namesto ugibanja. V tem
tečaju je ta izvorni material lahko lekcijski README-ji, vzorčne kode ali zunanji
viri povezani iz lekcij.

Uporabite RAG, kadar naj bo odgovor podprt z dokumenti, podatki ali trenutnimi
datotekami projekta.

### Načrtovanje

Načrtovanje je koristno, kadar zahteva zahteva več korakov. Načrte naj bodo kratki in
dovolj vidni za razvijalca ali uporabnika za pregled.

Za demo bi načrt lahko bil:

1. Poišči lekcije povezane z uporabo orodij.
2. Povzemi najbolj relevantne lekcije.
3. Priporoči eno praktično nalogo.

### Kontekst

Kontekst je tisto, kar model vidí zdaj. Premajhen kontekst lahko agentu
zamegli pomembne podrobnosti. Prevelik kontekst lahko pojemi agenta, naredi ga
počasnejšega, dražjega ali lažje zmede.

Dobro inženirstvo konteksta pomeni izbrati prave informacije za naslednji
klic modela.

### Pomnilnik

Pomnilnik so informacije, shranjene za kasnejšo uporabo. Ne shranjujte vsega.
Shranjujte informacije samo, kadar so uporabne, varne in jih je lahko posodobiti ali izbrisati.

Na primer, zapomniti si "učenec ima raje primere v Pythonu" je lahko koristno.
Shranjevanje občutljivih osebnih podatkov običajno ni.

### Ocenjevanje in opazovanje

Ocenjevanje se sprašuje: ali je agent naredil prav?

Opazovanje se sprašuje: ali lahko vidimo, kako se je zgodilo?

Za agente v produkciji spremljajte klice modela, klice orodij, pridobljeni kontekst,
zakasnitev, stroške, napake in povratne informacije uporabnikov.

### Zaupanje in varnost

Zanesljivi agenti potrebujejo več kot le koristno spodbudo. Uporabite orodja z minimalnimi privilegiji,
človeško odobritev za dejanja z velikim vplivom, redakcijo podatkov tam, kjer je potrebno, ter zapise ali
potrdila za dejanja, ki jih je treba pregledovati.

## 15-minutna rutina pregleda

Po vsaki lekciji uporabite to rutino:

1. **Povzemite lekcijo v eni povedi.**
2. **Poimenujte novo zmožnost agenta.** Na primer: uporaba orodja, pridobivanje,
   načrtovanje, pomnilnik, opazovanje ali varnost.
3. **Dodajte jo v demo pomočnika tečaja.** Kaj se zdaj spremeni v demu?
4. **Poiščite tveganje.** Kaj bi lahko šlo narobe, če se ta zmožnost zlorabi?
5. **Napišite eno testno vprašanje.** Kako bi preverili, da agent ravna pravilno?

## Hiter samopregled

Preden nadaljujete, poskusite odgovoriti na ta vprašanja:

1. Kaj agent lahko naredi, česa navaden klepetalni robot ne zmore sam?
2. Katero orodje bi vaš agent potreboval najprej in zakaj?
3. Katerega vira znanja naj podpira odgovor agenta?
4. Kateri kontekst vključiti v naslednji klic modela?
5. Kaj naj agent zapomni in česa naj ne shrani?
6. Kdaj naj agent zaprosi za človeško odobritev?
7. Kateri zapisi, sledovi ali potrdila bi vam kasneje pomagali pri odpravljanju ali reviziji agenta?

## Predlagana zaključna vaja

Ob koncu tečaja zgradite majhnega agenta, ki pomaga učencu poiskati pot v tem
repozitoriju.

Minimalna verzija:

- Sprejme temo od uporabnika.
- Poišče najbolj relevantne lekcije.
- Povzame, kaj naj prebere najprej.
- Predlaga eno praktično nalogo.
- Prikaže katere lekcijske datoteke ali povezave so bile uporabljene.

Razširjena verzija:

- Zapomni si izbrani programski jezik učenca.
- Pred odgovorom uporabi preprost načrt.
- Dodaj korak samopregleda pred končnim odgovorom.
- Beleži klice orodij in pridobljene vire.
- Pred odpiranjem brskalnika ali avtomatizacijo UI zahteva potrditev uporabnika.

To vam daje majhen, a realističen način za vadbo orodij, RAG, načrtovanja,
konteksta, pomnilnika, opazovanja in zaupanja v enem projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->