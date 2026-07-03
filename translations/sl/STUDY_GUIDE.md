# AI Agenti za začetnike - učni vodič

Uporabite ta vodič kot praktičnega sopotnika med potovanjem skozi tečaj. Ni
namišljen kot nadomestilo za lekcije. Pomaga vam odločiti, kje začeti, kaj iskati v
vsaki lekciji in kako povezati ideje v majhen delujoč demo agenta.

Če ste tukaj prvič, začnite preprosto:

1. Preberite [Nastavitev tečaja](./00-course-setup/README.md).
2. Izvedite lekcije 01-06 po vrsti.
3. Med učenjem imejte v mislih eno majhno idejo za demo.
4. Po vsaki lekciji vprašajte: "Kaj lahko moj agent zdaj naredi, kar prej ni mogel?"

## Enostaven demo, ki ga imejte v mislih

Dober način za učenje agentov je, da eno demo idejo spremljate skozi tečaj.

Primer demoja: **agent pomočnik za tečaj**.

Uporabnik vpraša:

> "Želim se naučiti, kako agenti uporabljajo orodja. Poišči prave lekcije,
> povzemi, kaj naj najprej preberem, in daj mi kratek prakso nalogo."

Navaden klepetalni bot lahko odgovori iz tega, kar že ve. Agent pa lahko naredi več:

1. **Prebere ali poišče datoteke tečaja**, da najde prave lekcije.
2. **Uporabi orodja** za iskanje povezav do lekcij, primerov ali pomožnega gradiva.
3. **Načrtuje** kratek učni načrt namesto enega dolgega odgovora.
4. **Uporabi kontekst** trenutnega pogovora, da ostane osredotočen na cilj učenca.
5. **Zapomni si uporabne preference**, če aplikacija podpira shranjevanje spomina.
6. **Prikaže sledi, navedbe ali zapise**, da uporabnik razume, kaj se je zgodilo.
7. **Uporabi varovalke** pred tveganimi dejanji ali uporabo občutljivih podatkov.

Med učenjem vsake lekcije se vrnite k temu demoju in vprašajte: katero novo
zmogljivost bi ta lekcija dodala?

## K čemu stremite

Do konca tečaja bi morali znati razložiti in zgraditi agentske sisteme, ki združujejo
te dele:

| Del | Pomen v vsakdanjem jeziku | V demoju |
|------|------------------------|-------------|
| Model | Upravlja razumevanje uporabnikove zahteve | Razume, da učenec želi lekcije o uporabi orodij |
| Orodja | Funkcije, API-ji, datoteke, brskalniki ali storitve, ki jih agent lahko uporablja | Išče po repozitoriju ali pridobi vsebino lekcij |
| Znanje | Dokumenti ali podatki, na katerih temelji odgovor | Datoteke README ter gradivo lekcij |
| Kontekst | Informacije vključene v naslednji poziv modelu | Cilj uporabnika in rezultati orodij |
| Spomin | Informacije shranjene za kasnejšo uporabo | Učenec ima raje praktične Python primere |
| Načrtovanje | Razdelitev večjega cilja na manjše korake | Poišči lekcije, povzem, predlagaj prakso |
| Orkestracija | Usmerjanje dela preko orodij, korakov ali agentov | Načrtovalec kliče iskalno orodje, nato povzema |
| Zaupanje | Varnost, zaščita, ocenjevanje in opazovanje | Zabeleži klice orodij in vpraša pred tveganimi dejanji |

## Izberite svojo učno pot

Lahko sledite celotnemu tečaju po vrsti ali skočite na pot glede na to, kaj želite
izgraditi.

| Če je vaš cilj... | Začnite z | Nato študirajte |
|-----------------------|------------|------------|
| Razumeti, kaj agenti so | 01, 02, 03 | 04, 05, 06 |
| Zgraditi agenta, ki uporablja orodja | 04 | 05, 07, 14 |
| Zgraditi RAG-agenta | 05 | 04, 06, 12 |
| Načrtovati večstopenjske delovne tokove | 07 | 08, 09, 14 |
| Razumeti sisteme z več agenti | 08 | 07, 09, 11 |
| Pripraviti agente za produkcijo | 06, 10 | 12, 13, 18 |
| Raziščite protokole in avtomatizacijo brskalnika | 11, 15 | 10, 18 |

Namig: če ste novi v svet agentov, ne preskakujte lekcij 01-06. Dajo vam
besedišče, ki ga boste potrebovali za preostanek tečaja.

## Vodnik lekcija po lekcija

| Lekcija | Kaj se naučite | Poskusite po lekciji |
|--------|----------------|---------------------------|
| [01 - Uvod v AI agente](./01-intro-to-ai-agents/README.md) | Kaj razlikuje agenta od osnovnega klepetalnega bota. | Razložite idejo svojega demo agenta, ne le kot aplikacijo za klepet. |
| [02 - Agentna ogrodja](./02-explore-agentic-frameworks/README.md) | Kako ogrodja pomagajo pri modelih, orodjih, stanju in delovnih tokovih. | Prepoznajte, katere dele vašega demoja bi obvladovalo ogrodje. |
| [03 - Agentni oblikovni vzorci](./03-agentic-design-patterns/README.md) | Pogosti vzorci za načrtovanje vedenja agentov. | Skicirajte uporabniško pot pred pisanjem kode. |
| [04 - Uporaba orodij](./04-tool-use/README.md) | Kako agenti kličejo orodja za pridobivanje podatkov ali izvajanje dejanj. | Določite eno orodje, ki bi ga vaš demo agent potreboval. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako pridobivanje temelji odgovore agenta na dokumentih ali podatkih. | Odločite, kateri vir znanja naj vaš demo pregleda. |
| [06 - Zanesljivi agenti](./06-building-trustworthy-agents/README.md) | Kako dodati varovalke, nadzor in varnejše vedenje. | Dodajte eno pravilo, kdaj naj agent najprej vpraša uporabnika. |
| [07 - Oblikovanje načrtovanja](./07-planning-design/README.md) | Kako agenti razdelijo večje cilje na manjše korake. | Napišite trikorakni načrt za zahtevo vašega demoja. |
| [08 - Oblikovanje večagentnega sistema](./08-multi-agent/README.md) | Kdaj delo razdeliti med specializirane agente. | Odločite, ali vaš demo potrebuje enega ali več agentov. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako agenti pregledujejo in izboljšajo svoj izhod. | Dodajte končni samopregled pred agentovim odgovorom. |
| [10 - AI agenti v produkciji](./10-ai-agents-production/README.md) | Kaj se spremeni, ko agent preide iz demoja v produkcijo. | Naštejte, kaj bi spremljali: kakovost, stroške, zakasnitev, napake. |
| [11 - Agentni protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezujejo agente z orodji in drugimi agenti. | Prepoznajte, kje bi standardni protokol poenostavil integracijo. |
| [12 - Inženiring konteksta](./12-context-engineering/README.md) | Kako izbrati, obrezati, izolirati in upravljati kontekst. | Odločite, kaj spada v poziv in kaj naj ostane zunaj. |
| [13 - Agentni spomin](./13-agent-memory/README.md) | Kako agenti shranjujejo uporabne informacije med interakcijami. | Izberite eno varno preferenco, ki si jo vaš demo lahko zapomni. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Gradniki specifični za ogrodje za agente in delovne tokove. | Preslikajte korake demoja v pojme ogrodja. |
| [15 - Agenti za uporabo računalnika](./15-browser-use/README.md) | Kako agenti komunicirajo z brskalnikom ali UI površinami. | Izberite eno brskalniško nalogo, ki naj še zahteva potrditev uporabnika. |
| [18 - Zavarovanje AI agentov](./18-securing-ai-agents/README.md) | Kako narediti agentove ukrepe bolj sledljive in zaščitene pred posegi. | Odločite, katera dejanja v vašem demoju naj bodo zabeležena ali potrjena. |

Lekciji 16 in 17 sta navedeni v glavnem README kot kmalu na voljo.
Dodajte ju v svoj učni načrt, ko bo vsebina lekcij na voljo.

## Ključne ideje v prijaznem jeziku za začetnike

### Orodja

Orodje je nekaj, kar agent lahko pokliče za delo izven modela. Dobro orodje ima
jasno ime, ozek namen, tipizirane vhodne podatke, predvidljiv izhod in varen način
napake.

Za demo pomočnika pri tečaju so npr.:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG in Znanje

RAG pomaga agentu odgovarjati na podlagi izvornega gradiva namesto ugibanja.
V tem tečaju je to lahko gradivo lekcijskih README datotek, vzorčne kode ali zunanji
viri, povezani iz lekcij.

Uporabite RAG, ko mora biti odgovor utemeljen na dokumentih, podatkih ali trenutnih
datotekah projekta.

### Načrtovanje

Načrtovanje je uporabno, ko ima zahteva več kot en korak. Načrte naj bodo kratki
in dovolj vidni, da jih razvijalec ali uporabnik lahko pregleda.

Za demo je načrt lahko:

1. Poišči lekcije povezane z uporabo orodij.
2. Povzemi najbolj relevantne lekcije.
3. Priporoči eno prakso nalogo.

### Kontekst

Kontekst je tisto, kar model vidi v trenutku. Premajhen kontekst lahko
pomoti agente pri pomembnih podrobnostih. Preveč konteksta lahko upočasni agenta,
poviša stroške ali ga zmede.

Dobro inženiranje konteksta pomeni izbrati prave informacije za naslednji poziv
modelu.

### Spomin

Spomin so informacije shranjene za pozneje. Ne shranjujte vsega. Shranjujte
informacije samo, kadar so uporabne, varne in jih je lahko posodobiti ali izbrisati.

Na primer, zapomniti si "učenec ima raje Python primere" je lahko koristno.
Zapomnitev občutljivih osebnih podatkov ponavadi ni.

### Evalvacija in opazovanje

Evalvacija se sprašuje: ali je agent naredil prav?

Opazovanje se sprašuje: ali lahko vidimo, kako se je to zgodilo?

Za produkcijske agente spremljajte klice modela, klice orodij, pridobljeni kontekst,
zakasnitev, stroške, napake in povratne informacije uporabnikov.

### Zaupanje in varnost

Zanesljivi agenti potrebujejo več kot le koristen poziv. Uporabljajte orodja z
najmanj privilegiji, človeško odobritev za dejanja z visokim vplivom, rdečenje
podatkov kjer je potrebno, ter zapise ali potrdila za dejanja, ki morajo biti
revidirana.

## 15-minutna rutina pregleda

Uporabite to rutino po vsaki lekciji:

1. **Povzemite lekcijo v eni povedi.**
2. **Poimenujte novo zmogljivost agenta.** Na primer: uporaba orodij, pridobivanje,
   načrtovanje, spomin, opazovanje ali varnost.
3. **Dodajte jo demo pomočniku tečaja.** Kaj se zdaj spremeni v demoju?
4. **Poiščite tveganje.** Kaj bi lahko šlo narobe, če se ta zmogljivost zlorabi?
5. **Napišite eno testno vprašanje.** Kako bi preverili, da se agent vede pravilno?

## Hiter samopregled

Pred nadaljevanjem poskusite odgovoriti na ta vprašanja:

1. Kaj agent lahko naredi, česar redni klepetalni bot sam ne more?
2. Katero orodje bi agent potreboval najprej in zakaj?
3. Kateri vir znanja naj utemelji agentov odgovor?
4. Kakšen kontekst naj bo vključen v naslednji poziv modelu?
5. Kaj naj si agent zapomni, in kaj naj se izogiba hranjenju?
6. Kdaj naj agent zahteva človeško odobritev?
7. Katere zapise, sledi ali potrdila bi vam pomagali kasneje za odpravljanje napak ali revizijo?

## Predlagana zaključna vaja

Na koncu tečaja zgradite majhnega agenta, ki pomaga učencu krmariti po tem
repositoriju.

Minimalna različica:

- Sprejme temo od uporabnika.
- Najde najbolj relevantne lekcije.
- Povzame, kaj naj najprej prebere.
- Predlaga eno praktično nalogo.
- Prikaže, katere lekcijske datoteke ali povezave je uporabil.

Razširjena različica:

- Zapomni si jezik programiranja, ki ga učenec raje uporablja.
- Pred odgovorom uporabi preprost načrt.
- Dodajte korak samopregleda pred končnim odgovorom.
- Zabeleži klice orodij in uporabljene vire.
- Pred odpiranjem brskalnika ali avtomatizacijo UI zahteva potrditev.

To vam daje majhen a realističen način za prakso orodij, RAG, načrtovanja,
konteksta, spomina, opazovanja in zaupanja v enem projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->