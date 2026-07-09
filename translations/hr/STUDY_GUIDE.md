# AI agenti za početnike - studijski vodič

Koristite ovaj vodič kao praktičnog pratitelja dok prolazite kroz tečaj. Nije
namijenjen za zamjenu lekcija. Pomaže vam odlučiti gdje početi, što
tražiti u svakoj lekciji i kako povezati ideje u mali radni agent
demo.

Ako ste ovdje prvi put, započnite jednostavno:

1. Pročitajte [Postavljanje tečaja](./00-course-setup/README.md).
2. Dovršite Lekcije 01-06 redoslijedom.
3. Držite u mislima jednu malu ideju demo agenta dok učite.
4. Nakon svake lekcije, zapitajte se: "Što moj agent sada može učiniti što prije nije mogao?"


## Jednostavan demo za imati na umu

Dobar način za učenje agenata je slijediti jednu ideju demoa kroz cijeli tečaj.

Primjer demoa: **agent pomagač za tečaj**.

Korisnik pita:

> "Želim naučiti kako agenti koriste alate. Pronađi prave lekcije, sažmi što
> trebam prvo pročitati i daj mi kratki zadatak za vježbu."

Običan chatbot može odgovoriti na temelju onoga što već zna. Agent može više:

1. **Čita ili pretražuje datoteke tečaja** da pronađe prave lekcije.
2. **Koristi alate** za dohvat poveznica na lekcije, primjera ili dodatnog materijala.
3. **Planira** kratak put učenja umjesto da daje jedan dug odgovor.
4. **Koristi kontekst** iz trenutnog razgovora kako bi ostao usredotočen na cilj učenika.

5. **Pamti korisne preferencije** ako aplikacija podržava memoriju.
6. **Prikazuje tragove, citate ili dnevnike** kako bi korisnik razumio što se dogodilo.
7. **Primjenjuje sigurnosne mjere** prije poduzimanja rizičnih radnji ili korištenja osjetljivih podataka.

Dok proučavate svaku lekciju, vraćajte se ovom demou i pitajte: koju novu
sposobnost bi ova lekcija dodala?

## Prema čemu gradite

Do kraja tečaja trebali biste moći objasniti i izgraditi agentske sustave
koji kombiniraju ove dijelove:

| Dio | Značenje običnim jezikom | U demou |
|------|------------------------|-------------|
| Model | Mehanizam rezoniranja koji tumači zahtjev korisnika | Razumije da učenik želi lekcije o korištenju alata |
| Alati | Funkcije, API-ji, datoteke, preglednici ili usluge koje agent može koristiti | Pretražuje repozitorij ili dohvaća sadržaj lekcija |
| Znanje | Dokumenti ili podaci koji služe kao osnova za odgovor | README datoteke tečaja i materijal lekcija |
| Kontekst | Informacije uključene u sljedeći poziv modela | Cilj korisnika i rezultati alata |
| Memorija | Informacije spremljene za kasniju upotrebu | Učenik preferira praktične primjere u Pythonu |
| Planiranje | Razbijanje većeg cilja na manje korake | Pronađi lekcije, sažmi ih, predloži vježbu |
| Orkestracija | Usmjeravanje rada kroz alate, korake ili agente | Planer poziva alat za pretraživanje, zatim sažimatelj |
| Povjerenje | Sigurnost, zaštita, evaluacija i primjetljivost | Bilježi pozive alatu i pita prije radnji velikog utjecaja |

## Modeli i pružatelji

Primjeri koda u tečaju koriste **Microsoft Agent Framework (MAF)** i ciljaju na **Azure OpenAI Responses API** — preporučeni API za budućnost koji kombinira nadopune chata, pozivanje alata, multimodalni unos i državne razgovore u jedinstvenom API-ju. Povezujete se ili putem **Microsoft Foundry** projekta (s `FoundryChatClient`) ili izravno na Azure OpenAI (s `OpenAIChatClient`).


Dok prolazite kroz lekcije, imate nekoliko opcija davatelja usluga:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — glavni put koji se koristi kroz lekcije. Prijavite se s `az login` za autentifikaciju bez ključeva putem Entra ID-a.
- **Foundry Local** — pokrenite modele u potpunosti na uređaju putem OpenAI-kompatibilnog API-ja (nema oblaka, nema API ključeva). Idealno za eksperimentiranje offline ili bez troškova. Pogledajte [Postavljanje tečaja](./00-course-setup/README.md).
- **MiniMax** — OpenAI-kompatibilni davatelj s modelima velikog konteksta, upotrebljiv kao izravna alternativa.

> **Napomena:** GitHub Models je zastario (ukida se u srpnju 2026.) i ne podržava Responses API. Primjeri su ažurirani da koriste Azure OpenAI / Microsoft Foundry umjesto toga.

## Odaberite svoj put učenja

Možete proći cijeli tečaj redom ili skočiti na put na temelju onoga što želite
izgraditi.

| Ako vam je cilj... | Počnite s | Zatim proučite |
|-----------------------|------------|------------|
| Razumjeti što su agenti | 01, 02, 03 | 04, 05, 06 |
| Izgraditi agenta koji koristi alate | 04 | 05, 07, 14 |
| Izgraditi agenta temeljenog na RAG-u | 05 | 04, 06, 12 |
| Dizajnirati višekorake tijekove rada | 07 | 08, 09, 14 |
| Razumjeti sustave s više agenata | 08 | 07, 09, 11 |
| Pripremiti agente za produkciju | 06, 10 | 12, 13, 18 |
| Istražiti protokole i automatizaciju preglednika | 11, 15 | 10, 18 |

Savjet: ako ste novi u agentima, nemojte preskakati lekcije 01-06. One vam daju
vokabular koji će vam trebati za ostatak tečaja.

## Vodič lekcija po lekcija

| Lekcija | Što učite | Isprobajte nakon lekcije |
|--------|----------------|---------------------------|
| [01 - Uvod u AI agente](./01-intro-to-ai-agents/README.md) | Što čini agenta drugačijim od osnovnog chatbot-a. | Objasnite svoju ideju demo agenta, ne samo chat aplikacije. |
| [02 - Agentni okviri](./02-explore-agentic-frameworks/README.md) | Kako okviri pomažu s modelima, alatima, stanjem i tijekovima rada. | Identificirajte koje dijelove vaše demo aplikacije bi upravljao okvir. |
| [03 - Agentni dizajnerski obrasci](./03-agentic-design-patterns/README.md) | Uobičajeni obrasci za dizajn ponašanja agenata. | Skicirajte put korisnika prije pisanja koda. |
| [04 - Korištenje alata](./04-tool-use/README.md) | Kako agenti pozivaju alate za dobivanje podataka ili poduzimanje akcija. | Definirajte jedan alat koji bi vaš demo agent trebao. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako dohvaćanje temelji odgovore agenata na dokumentima ili podacima. | Odlučite koji izvor znanja vaš demo treba pretraživati. |
| [06 - Pouzdani agenti](./06-building-trustworthy-agents/README.md) | Kako dodati zaštitne mjere, nadzor i sigurnije ponašanje. | Dodajte jedno pravilo za kada agent treba prvo pitati korisnika. |

| [07 - Planiranje dizajna](./07-planning-design/README.md) | Kako agenti razlažu veće ciljeve na manje korake. | Napišite trostupanjski plan za vaš zahtjev za demonstraciju. |

| [08 - Dizajn s Više Agenta](./08-multi-agent/README.md) | Kada podijeliti posao među specijaliziranim agentima. | Odlučite treba li vašem demo-u jedan agent ili nekoliko. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako agenti mogu pregledavati i poboljšavati vlastiti izlaz. | Dodajte završnu samoprovjeru prije nego agent odgovori. |
| [10 - AI Agenti u Produkciji](./10-ai-agents-production/README.md) | Što se mijenja kada agent prelazi iz demo faze u produkciju. | Nabrojite što biste pratili: kvalitetu, trošak, latenciju, kvarove. |
| [11 - Agentni Protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezuju agente s alatima i drugim agentima. | Identificirajte gdje bi standardni protokol mogao pojednostaviti integraciju. |
| [12 - Inženjering Konteksta](./12-context-engineering/README.md) | Kako odabrati, obrezati, izolirati i upravljati kontekstom. | Odlučite što treba biti u upitu, a što izvan njega. |
| [13 - Memorija Agenta](./13-agent-memory/README.md) | Kako agenti mogu spremati korisne informacije kroz interakcije. | Odaberite jednu sigurnu preferenciju koju bi vaš demo mogao pamtiti. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Specifični sučelni blokovi za agente i tijekove rada, plus hostanje LangChain/LangGraph agenata na Microsoft Foundry. | Povežite korake vašeg demo-a sa konceptima okvira. |
| [15 - Agenti za Korištenje Računala](./15-browser-use/README.md) | Kako agenti mogu komunicirati s preglednikom ili korisničkim sučeljem, uključujući stvarne primjere poput Microsoft Project Opal. | Izaberite jedan zadatak u pregledniku koji i dalje zahtijeva potvrdu korisnika. |
| [18 - Osiguranje AI Agenata](./18-securing-ai-agents/README.md) | Kako učiniti akcije agenata više auditabilnima i evidentiranima na manipulacije. | Odlučite koje akcije u vašem demo-u treba bilježiti ili potvrditi. |

Lekcije 16 i 17 navedene su u glavnom README kao uskoro dostupne. Dodajte ih u svoj
plan učenja kad sadržaj lekcija bude dostupan.

## Ključne Ideje u Terminima Prikladnim Početnicima

### Alati

Alat je nešto što agent može pozvati da obavi posao izvan modela. Dobar alat
ima jasno ime, usku zadaću, tipizirane ulaze, predvidiv izlaz i siguran način
za neuspjeh.

Za pomoćnog demo agenta tečaja, alat bi mogao biti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG i Znanje

RAG pomaže agentu da odgovori na temelju izvornog materijala umjesto da pogađa. U ovom
tečaju, taj izvorni materijal može biti README lekcija, primjeri koda ili vanjski
resursi povezani u lekcijama.

Koristite RAG kada odgovor treba biti utemeljen na dokumentima, podacima ili
trenutno dostupnim datotekama projekta.

### Planiranje

Planiranje je korisno kada zahtjev ima više od jednog koraka. Čuvajte planove kratkima i
dovoljno preglednima da ih programer ili korisnik može provjeriti.

Za demo, plan bi mogao biti:

1. Pronađi lekcije vezane uz upotrebu alata.
2. Sažmi najrelevantnije lekcije.
3. Preporuči jedan zadatak za vježbu.

### Kontekst

Kontekst je ono što model trenutno vidi. Premalo konteksta može učiniti da agent
propusti važne detalje. Previše konteksta može učiniti agenta sporijim, skupljim,
ili lakše zbunjenim.

Dobro inženjerstvo konteksta znači odabrati prave informacije za sljedeći model

poziv.

### Memorija

Memorija je informacija sačuvana za kasnije. Nemojte spremati sve. Spremite informacije
samo kada su korisne, sigurne i lako se mogu ažurirati ili izbrisati.

Na primjer, može biti korisno zapamtiti "učenik preferira Python primjere".
Obično nije korisno pamtiti osjetljive osobne podatke.

### Evaluacija i promatranje

Evaluacija pita: je li agent učinio pravu stvar?

Promatranje pita: možemo li vidjeti kako se to dogodilo?

Za produkcijske agente, pratite pozive modela, pozive alata, dohvaćeni kontekst,
latenciju, troškove, pogreške i povratne informacije korisnika.

### Povjerenje i sigurnost

Pouzdani agenti trebaju više od korisnog upita. Koristite alate s minimalnim privilegijama,
ljudsko odobrenje za akcije velikog utjecaja, skrivanje podataka gdje je potrebno i zapise ili
potvrde za radnje koje se moraju revidirati.

## Rutina pregleda od 15 minuta

Upotrijebite ovu rutinu nakon svake lekcije:

1. **Sažmite lekciju u jednoj rečenici.**
2. **Nazovite novu sposobnost agenta.** Na primjer: korištenje alata, dohvaćanje,
   planiranje, memorija, promatranje ili sigurnost.
3. **Dodajte je demonstraciji pomoćnika tečaja.** Što se sada mijenja u demonstraciji?
4. **Pronađite rizik.** Što bi moglo poći po zlu ako se ta sposobnost zloupotrijebi?
5. **Napišite jedno ispitno pitanje.** Kako biste provjerili da se agent ponaša ispravno?

## Brza samoprovjera

Prije nego što nastavite, pokušajte odgovoriti na ova pitanja:

1. Što agent može napraviti što običan chatbot ne može sam od sebe?
2. Koji bi alat vaš agent najprije trebao imati i zašto?
3. Koji bi izvor znanja trebao biti osnova za odgovor agenta?
4. Koji kontekst treba biti uključen u sljedeći poziv modela?
5. Što bi agent trebao zapamtiti, a što bi trebao izbjegavati spremati?
6. Kada bi agent trebao tražiti ljudsko odobrenje?
7. Koji bi zapisi, tragovi ili potvrde pomogli u otklanjanju pogrešaka ili reviziji agenta kasnije?

## Predložena završna vježba

Na kraju tečaja, izgradite malog agenta koji pomaže učeniku navigirati ovim
repozitorijem.

Minimalna verzija:

- Prihvati temu od korisnika.
- Pronađi najrelevantnije lekcije.
- Sažmi što se prvo treba pročitati.
- Predloži jedan praktični zadatak.
- Prikaži koje su lekcijske datoteke ili poveznice korištene.

Proširena verzija:

- Zapamti programski jezik koji učenik preferira.
- Koristi jednostavan plan prije odgovora.
- Dodaj korak samoprovjere prije konačnog odgovora.
- Bilježi pozive alata i dohvaćene izvore.
- Traži potvrdu prije otvaranja preglednika ili zadataka za automatizaciju UI-ja.

Ovo vam daje mali, ali realan način za vježbanje alata, RAG-a, planiranja,
konteksta, memorije, promatranja i povjerenja u jednom projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->