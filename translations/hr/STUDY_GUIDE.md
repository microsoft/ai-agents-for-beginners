# AI agenti za početnike - vodič za učenje

Koristite ovaj vodič kao praktičnog pratitelja dok prolazite kroz tečaj. Nije
namijenjen zamjeni lekcija. Pomaže vam da odlučite gdje početi, na što obratiti
pažnju u svakoj lekciji i kako povezati ideje u mali radni demo agenta.

Ako ste ovdje prvi put, počnite jednostavno:

1. Pročitajte [Postavljanje tečaja](./00-course-setup/README.md).
2. Završite lekcije 01-06 redom.
3. Držite na umu jednu malu ideju za demo dok učite.
4. Nakon svake lekcije, pitajte se: "Što moj agent sada može što prije nije mogao?"

## Jednostavan demo za imati na umu

Dobar način za učenje agenata je pratiti jednu ideju za demo kroz tečaj.

Primjer demo-a: **agent pomagač za tečaj**.

Korisnik pita:

> "Želim naučiti kako agenti koriste alate. Pronađi prave lekcije, sažmi što bih 
> prvo trebao pročitati i daj mi kratki zadatak za vježbu."

Obični chatbot može odgovoriti na temelju onoga što već zna. Agent može više:

1. **Pročitati ili pretražiti datoteke tečaja** da pronađe prave lekcije.
2. **Koristiti alate** za dohvat linkova lekcija, primjera ili pomoćnog materijala.
3. **Planirati** kratak put učenja umjesto davanja jednog dugog odgovora.
4. **Koristiti kontekst** iz trenutnog razgovora da ostane fokusiran na cilj učenika.
5. **Pamćenje korisnih preferencija** ako aplikacija podržava memoriju.
6. **Prikazati tragove, citate ili zapise** da korisnik razumije što se dogodilo.
7. **Primijeniti zaštitne mjere** prije poduzimanja rizičnih radnji ili korištenja osjetljivih podataka.

Dok proučavate svaku lekciju, vratite se ovom demu i pitajte: koju novu mogućnost
bi ova lekcija dodala?

## Toward što gradite

Do kraja tečaja trebali biste moći objasniti i izgraditi agentske sustave koji
kombiniraju ove dijelove:

| Dio | Značenje običnim jezikom | U demu |
|------|------------------------|-------------|
| Model | Mehanizam rezoniranja koji interpretira zahtjev korisnika | Razumije da učenik želi lekcije o korištenju alata |
| Alati | Funkcije, API-jevi, datoteke, preglednici ili servisi koje agent može koristiti | Pretražuje repozitorij ili dohvaća sadržaj lekcije |
| Znanje | Dokumenti ili podaci koji podupiru odgovor | README datoteke i materijali lekcija tečaja |
| Kontekst | Informacije uključene u sljedeći poziv modela | Cilj korisnika i rezultati alata |
| Memorija | Informacije spremljene za kasniju upotrebu | Učenik preferira praktične Python primjere |
| Planiranje | Razbijanje većeg cilja u manje korake | Pronaći lekcije, sažeti ih, predložiti vježbu |
| Orkestracija | Usmjeravanje posla preko alata, koraka ili agenata | Planer poziva alat za pretraživanje, zatim sažima |
| Povjerenje | Sigurnost, evaluacija i promatranje | Zabilježava pozive alata i pita prije akcija velikog utjecaja |

## Odaberite svoj put učenja

Možete uzeti cijeli tečaj po redu ili skočiti na put temeljen na onome što želite
izgraditi.

| Ako vam je cilj... | Počnite s | Zatim proučite |
|--------------------|-----------|----------------|
| Razumjeti što su agenti | 01, 02, 03 | 04, 05, 06 |
| Izgraditi agenta koji koristi alate | 04 | 05, 07, 14 |
| Izgraditi agenta baziranog na RAG-u | 05 | 04, 06, 12 |
| Dizajnirati višestupanjske tijekove rada | 07 | 08, 09, 14 |
| Razumjeti višestruke agentske sustave | 08 | 07, 09, 11 |
| Pripremiti agente za produkciju | 06, 10 | 12, 13, 18 |
| Istražiti protokole i automatizaciju preglednika | 11, 15 | 10, 18 |

Savjet: ako ste novi u agentima, nemojte preskakati lekcije 01-06. One vam daju
rečnik potreban za ostatak tečaja.

## Vodič lekcija po lekcija

| Lekcija | Što učite | Pokušajte nakon lekcije |
|--------|----------------|-------------------------|
| [01 - Uvod u AI agente](./01-intro-to-ai-agents/README.md) | Što agenta razlikuje od osnovnog chatbota. | Objasnite ideju vašeg demo agenta, ne samo chat aplikacije. |
| [02 - Agentni okviri](./02-explore-agentic-frameworks/README.md) | Kako okviri pomažu s modelima, alatima, stanjem i tijekovima rada. | Identificirajte koje dijelove vašeg demo-a bi upravljao okvir. |
| [03 - Agentni dizajnerski obrasci](./03-agentic-design-patterns/README.md) | Uobičajeni obrasci za dizajniranje ponašanja agenta. | Skicirajte korisnički put prije pisanja koda. |
| [04 - Korištenje alata](./04-tool-use/README.md) | Kako agenti pozivaju alate za dobivanje podataka ili poduzimanje radnji. | Definirajte jedan alat koji bi vaš demo agent trebao. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako dohvat podataka temelji odgovore agenta u dokumentima ili podacima. | Odlučite koji izvor znanja vaš demo treba pretražiti. |
| [06 - Pouzdani agenti](./06-building-trustworthy-agents/README.md) | Kako dodati zaštitne mjere, nadzor i sigurnije ponašanje. | Dodajte jedno pravilo kada agent treba prvo pitati korisnika. |
| [07 - Dizajn planiranja](./07-planning-design/README.md) | Kako agenti razbijaju veće ciljeve u manje korake. | Napišite plan od tri koraka za vaš zahtjev demo-a. |
| [08 - Multi-agentni dizajn](./08-multi-agent/README.md) | Kada raspodijeliti rad između specijaliziranih agenata. | Odlučite treba li vaš demo jednog agenta ili više njih. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako agenti mogu pregledati i poboljšati vlastiti izlaz. | Dodajte završnu samoprovjeru prije nego agent odgovori. |
| [10 - AI agenti u produkciji](./10-ai-agents-production/README.md) | Što se mijenja kad agent prelazi iz demo u produkciju. | Nabrojite što biste pratili: kvalitetu, troškove, latenciju, greške. |
| [11 - Agentički protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezuju agente s alatima i drugim agentima. | Identificirajte gdje bi standardni protokol mogao pojednostaviti integraciju. |
| [12 - Inženjering konteksta](./12-context-engineering/README.md) | Kako odabrati, skratiti, izolirati i upravljati s kontekstom. | Odlučite što treba ući u prompt, a što treba ostati van. |
| [13 - Memorija agenta](./13-agent-memory/README.md) | Kako agenti mogu spremiti korisne informacije kroz interakcije. | Odaberite jednu sigurnu preferenciju koju bi vaš demo mogao zapamtiti. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Okvir-specifične gradivne cjeline za agente i tijekove rada. | Preslikajte korake vašeg demo-a na koncepte okvira. |
| [15 - Agent za korištenje računala](./15-browser-use/README.md) | Kako agenti mogu komunicirati s preglednikom ili UI sučeljima. | Odaberite jedan zadatak preglednika koji i dalje treba potvrdu korisnika. |
| [18 - Sigurnost AI agenata](./18-securing-ai-agents/README.md) | Kako učiniti radnje agenta auditabilnijima i otpornijima na manipulaciju. | Odlučite koje radnje u vašem demo-u treba bilježiti ili potvrđivati. |

Lekcije 16 i 17 navedene su u glavnom README kao "uskoro dostupno". Dodajte ih
u svoj plan učenja kad sadržaj lekcije postane dostupan.

## Ključne ideje jednostavnim jezikom

### Alati

Alat je nešto što agent može pozvati da obavi rad izvan modela. Dobar alat ima
jasan naziv, uski zadatak, tipizirane ulaze, predvidivi izlaz i siguran način
kada ne uspije.

Za pomagača u tečaju, alat može biti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG i znanje

RAG pomaže agentu da odgovara iz izvornog materijala umjesto nagađanja. U ovom
tečaju, izvornu materiju mogu činiti README datoteke lekcija, primjeri koda ili
vanjski resursi povezani u lekcijama.

Koristite RAG kada odgovor treba biti utemeljen u dokumentima, podacima ili
trenutnim datotekama projekta.

### Planiranje

Planiranje je korisno kada zahtjev ima više koraka. Držite planove kratkim i
dovoljno vidljivim da ih programer ili korisnik mogu pregledati.

Za demo, plan može biti:

1. Pronaći lekcije povezane s korištenjem alata.
2. Sažeti najrelevantnije lekcije.
3. Preporučiti jedan zadatak za vježbu.

### Kontekst

Kontekst je ono što model trenutno vidi. Premalo konteksta može učiniti da agent
propusti važne detalje. Previše konteksta može učiniti agenta sporijim, skupljim
ili lakšim za zbunjivanje.

Dobar inženjering konteksta znači odabrati prave informacije za sljedeći poziv
modela.

### Memorija

Memorija je informacija spremljena za kasniju upotrebu. Nemojte spremati sve.
Spremite informacije samo kada su korisne, sigurne i lako ih je ažurirati ili
izbrisati.

Na primjer, pamćenje "učenik preferira Python primjere" može biti korisno.
Pamćenje osjetljivih osobnih podataka obično nije.

### Evaluacija i promatranje

Evaluacija pita: je li agent učinio pravu stvar?

Promatranje pita: možemo li vidjeti kako se to dogodilo?

Za produkcijske agente, pratite pozive modela, pozive alata, dohvaćeni kontekst,
latenciju, troškove, greške i povratne informacije korisnika.

### Povjerenje i sigurnost

Pouzdani agenti trebaju više od korisnog prompta. Koristite alate s minimalnim
privilegijama, ljudsko odobrenje za radnje velikog utjecaja, maskiranje podataka
gdje je potrebno i zapise ili potvrde za radnje koje se moraju nadzirati.

## Rutina pregleda od 15 minuta

Koristite ovu rutinu nakon svake lekcije:

1. **Sažmite lekciju u jednoj rečenici.**
2. **Nazovite novu sposobnost agenta.** Na primjer: korištenje alata, dohvat,
   planiranje, memorija, promatranje ili sigurnost.
3. **Dodajte je u demo pomagača tečaja.** Što se sada promijenilo u demu?
4. **Pronađite rizik.** Što bi moglo poći po zlu ako se ova sposobnost zloupotrijebi?
5. **Napišite jedno testno pitanje.** Kako biste provjerili da se agent dobro ponaša?

## Brza samoprovjera

Prije nego nastavite, pokušajte odgovoriti na ova pitanja:

1. Što agent može što obični chatbot sam ne može?
2. Koji alat bi vaš agent prvo trebao i zašto?
3. Koji izvor znanja treba poduprijeti odgovor agenta?
4. Koji kontekst treba uklopiti u sljedeći poziv modela?
5. Što bi agent trebao pamtiti, a što treba izbjegavati spremati?
6. Kada agent treba tražiti ljudsko odobrenje?
7. Koje zapise, tragove ili potvrde bi vam pomogle za kasniji debug ili reviziju agenta?

## Predložena završna vježba

Na kraju tečaja, izgradite malog agenta koji pomaže učeniku da se snađe u ovom
repozitoriju.

Minimalna verzija:

- Prihvatite temu od korisnika.
- Pronađite najrelevantnije lekcije.
- Sažmite što prvo treba pročitati.
- Predložite jedan praktični zadatak.
- Prikažite koje su lekcijske datoteke ili linkovi korišteni.

Produžena verzija:

- Zapamtite preferirani programski jezik učenika.
- Upotrijebite jednostavan plan prije davanja odgovora.
- Dodajte korak samoprovjere prije konačnog odgovora.
- Zabilježite pozive alata i dohvaćene izvore.
- Zatražite potvrdu prije otvaranja preglednika ili zadataka automatizacije UI.

Ovo vam daje mali, ali realan način da vježbate alate, RAG, planiranje,
kontekst, memoriju, promatranje i povjerenje u jednom projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->