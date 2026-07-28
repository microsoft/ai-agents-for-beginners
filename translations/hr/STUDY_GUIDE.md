# AI agenti za početnike – vodič za učenje

Koristite ovaj vodič kao praktičnog pratitelja dok prolazite kroz tečaj. Nije
zamišljen kao zamjena za lekcije. Pomaže vam odlučiti gdje započeti, na što
obratiti pažnju u svakoj lekciji i kako povezati ideje u mali radni demo
agenta.

Ako ste ovdje prvi put, krenite jednostavno:

1. Pročitajte [Course Setup](./00-course-setup/README.md).
2. Završite lekcije 01-06 redom.
3. Imajte na umu jednu malu ideju za demo dok učite.
4. Nakon svake lekcije, zapitajte se: "Što moj agent sada može što nije mogao
   prije?"

## Jednostavan demo za imati na umu

Dobar način za učenje agenata je pratiti jednu ideju demo projekta kroz tečaj.

Primjer demo projekta: **agent pomagač za tečaj**.

Korisnik pita:

> "Želim naučiti kako agenti koriste alate. Nađi prave lekcije, sažmi što bih
> prvo trebao pročitati i daj mi kratak zadatak za vježbu."

Obični chatbot može odgovarati na temelju onoga što već zna. Agent može više:

1. **Pročitaj ili pretraži datoteke tečaja** da pronađe prave lekcije.
2. **Koristi alate** za dohvat poveznica lekcija, primjera ili pratećeg materijala.
3. **Planiraj** kratak put učenja umjesto davanja jednog dugačkog odgovora.
4. **Koristi kontekst** iz trenutnog razgovora da ostaneš fokusiran na cilj učenika.
5. **Pamti korisne preferencije** ako aplikacija podržava memoriju.
6. **Prikaži tragove, citate ili zapise** kako bi korisnik mogao razumjeti što se
   dogodilo.
7. **Primijeni zaštitne mjere** prije poduzimanja rizičnih radnji ili korištenja


Dok učiš svaku lekciju, vraćaj se ovom demo projektu i zapitaj se: koju novu




Do kraja tečaja trebao bi moći objasniti i izgraditi sustave agenata koji kombiniraju


| Dio | Značenje običnim jezikom | U demo projektu |
|------|------------------------|-------------|
| Model | Sklop za rezoniranje koji tumači zahtjev korisnika | Razumije da učenik želi lekcije o korištenju alata |
| Alati | Funkcije, API-jevi, datoteke, preglednici ili usluge koje agent može koristiti | Pretražuje repozitorij ili dohvaća sadržaj lekcija |
| Znanje | Dokumenti ili podaci koji služe za utemeljenje odgovora | README datoteke tečaja i materijal lekcija |
| Kontekst | Informacije uključene u sljedeći poziv modela | Cilj korisnika i rezultati alata |
| Memorija | Informacije spremljene za kasniju uporabu | Učenik preferira praktične primjere u Pythonu |
| Planiranje | Razbijanje većeg cilja na manje korake | Pronađi lekcije, sažmi ih, predloži vježbu |
| Orkestracija | Usmjeravanje posla između alata, koraka ili agenata | Planer poziva alat za pretraživanje, pa zatim sažimatelja |






Kako prolazite kroz lekcije, imate nekoliko ponuđenih providera:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — primarni put koji se koristi kroz lekcije. Prijavite se pomoću `az login` za autentikaciju bez ključeva preko Entra ID.
- **Foundry Local** — pokreće modele u potpunosti na uređaju putem API-ja kompatibilnog s OpenAI (bez oblaka, bez API ključeva). Idealno za offline ili besplatno eksperimentiranje. Pogledajte [Course Setup](./00-course-setup/README.md).
- **MiniMax** — provider kompatibilan s OpenAI-jem s modelima velikog konteksta, upotrebljiv kao zamjena.

> **Napomena:** GitHub Models je zastario (ukida se u srpnju 2026.) i ne podržava Responses API. Primjeri su ažurirani da koriste Azure OpenAI / Microsoft Foundry umjesto toga.

## Odaberite svoj put učenja

Možete pohađati cijeli tečaj redom ili preskočiti na put ovisno o onome što želite
izgraditi.

| Ako vam je cilj... | Započnite s | Zatim proučite |
|-----------------------|------------|------------|
| Razumjeti što su agenti | 01, 02, 03 | 04, 05, 06 |
| Izgraditi agenta koji koristi alate | 04 | 05, 07, 14 |
| Izgraditi agenta temeljenog na RAG-u | 05 | 04, 06, 12 |
| Dizajnirati višekorakove tijekove rada | 07 | 08, 09, 14 |
| Razumjeti sustave s više agenata | 08 | 07, 09, 11 |
| Pripremiti agente za produkciju | 06, 10 | 12, 13, 16, 18 |
| Implementirati i skalirati agente na Foundry-u | 10, 16 | 06, 13, 18 |
| Izgraditi lokalne / offline-prvo agente | 17 | 04, 05, 11 |
| Istražiti protokole i automatizaciju preglednika | 11, 15 | 10, 18 |

Savjet: ako ste novi u agentima, ne preskačite Lekcije 01-06. One vam daju
vokabular koji će vam trebati za ostatak tečaja.

## Vodič po lekcijama

| Lekcija | Što naučite | Isprobajte ovo poslije lekcije |
|--------|----------------|---------------------------|
| [01 - Uvod u AI agente](./01-intro-to-ai-agents/README.md) | Što razlikuje agenta od osnovnog chatbota. | Objasnite svoju ideju za demo kao agenta, ne samo kao chat aplikaciju. |
| [02 - Agentni okviri](./02-explore-agentic-frameworks/README.md) | Kako okviri pomažu s modelima, alatima, stanjem i tokovima rada. | Identificirajte koji dijelovi vaše demo aplikacije bi bili upravljani okvirom. |
| [03 - Agentni dizajnerski obrasci](./03-agentic-design-patterns/README.md) | Uobičajeni obrasci za dizajn ponašanja agenta. | Nacrtajte korisnički put prije nego što napišete kod. |
| [04 - Korištenje alata](./04-tool-use/README.md) | Kako agenti pozivaju alate za dohvat podataka ili poduzimanje akcija. | Definirajte jedan alat koji bi vaš demo agent trebao. |
| [05 - Agentni RAG](./05-agentic-rag/README.md) | Kako dohvat uspostavlja temelje agentovim odgovorima u dokumentima ili podacima. | Odlučite koji izvor znanja bi vaš demo trebao pretraživati. |

| [06 - Pouzdani agenti](./06-building-trustworthy-agents/README.md) | Kako dodati zaštitne mjere, nadzor i sigurnije ponašanje. | Dodajte jedno pravilo kada agent treba prvo pitati korisnika. |
| [07 - Dizajn planiranja](./07-planning-design/README.md) | Kako agenti razlažu veće ciljeve na manje korake. | Napišite plan u tri koraka za vaš zahtjev za demonstraciju. |
| [08 - Dizajn više agenata](./08-multi-agent/README.md) | Kada raspodijeliti posao među specijaliziranim agentima. | Odlučite treba li vašoj demonstraciji jedan agent ili nekoliko. |
| [09 - Metakognicija](./09-metacognition/README.md) | Kako agenti mogu pregledati i poboljšati vlastiti rezultat. | Dodajte završnu samoprovjeru prije nego agent odgovori. |
| [10 - AI agenti u produkciji](./10-ai-agents-production/README.md) | Što se mijenja kada agent prelazi iz demonstracije u produkciju. | Nabrojite što biste nadzirali: kvalitetu, troškove, kašnjenje, neuspjehe. |
| [11 - Agentni protokoli](./11-agentic-protocols/README.md) | Kako protokoli povezuju agente s alatima i drugim agentima. | Identificirajte gdje bi standardni protokol mogao pojednostaviti integraciju. |
| [12 - Inženjering konteksta](./12-context-engineering/README.md) | Kako odabrati, skratiti, izolirati i upravljati kontekstom. | Odlučite što pripada u prompt, a što treba ostaviti izvan njega. |
| [13 - Memorija agenata](./13-agent-memory/README.md) | Kako agenti mogu spremiti korisne informacije kroz interakcije. | Izaberite jednu sigurnu preferenciju koju bi vaša demonstracija mogla pamtiti. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Specifični blokovi za gradnju agenata i tijekova rada, plus hostanje LangChain/LangGraph agenata na Microsoft Foundry. | Preslikajte korake vaše demonstracije na koncepte okvira. |
| [15 - Agentni korištenje računala](./15-browser-use/README.md) | Kako agenti mogu komunicirati s browserom ili UI sučeljima, uključujući stvarne primjere poput Microsoft Project Opal. | Odaberite jedan zadatak u browseru koji i dalje treba potvrdu korisnika. |
| [16 - Implementacija skalabilnih agenata](./16-deploying-scalable-agents/README.md) | Kako dovesti agenta od prototipa do skalabilne, promatrane produkcijske implementacije na Microsoft Foundry (hostani agenti, usmjeravanje modela, keširanje, evaluacijski pragovi, ispitivanja dima). | Nabrojite produkcijske brige koje vaša demonstracija još treba: hostanje, usmjeravanje, troškovi, evaluacija. |
| [17 - Kreiranje lokalnih AI agenata](./17-creating-local-ai-agents/README.md) | Kako izgraditi agente s prioritetom lokalnog rada koji se potpuno izvršavaju na vašem računalu s Foundry Local i Qwen (lokalni alati, lokalni RAG, lokalni MCP). | Odlučite koji dijelovi vaše demonstracije trebaju ostati privatni i raditi lokalno. |
| [18 - Sigurnost AI agenata](./18-securing-ai-agents/README.md) | Kako učiniti radnje agenata auditabilnijima i otkrivajućima manipulacije. | Odlučite koje radnje u vašoj demonstraciji trebaju biti zabilježene ili potvrđene primitkom. |

## Validacija implementiranih agenata pomoću ispitivanja dima

Kad implementirate agenta (Lekcija 16), **ispitivanje dima** je najjeftinija prva
provjera da implementacija doista odgovara. Ovaj repozitorij isporučuje spremne kataloge za pokretanje
pod [tests/](./tests/README.md) za implementirane agente iz lekcija
01, 04, 05 i 16, povezane s

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
radnja. Pokrenite ih sa kartice **Actions** nakon implementacije agenta lekcije.
Smoke testovi su prva prepreka — offline i online evaluacija (Lekcije 10 i 16)
govore vam koliko je agent *dobar*.

## Ključne ideje jednostavnim riječima

### Alati

Alat je nešto što agent može pozvati da obavi posao izvan modela. Dobar alat
ima jasno ime, usko područje rada, tipizirane ulaze, predvidiv izlaz i siguran način
neuspjeha.

Za demo pomoćnika tečaja, alat može biti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG i znanje

RAG pomaže agentu da odgovori iz izvornog materijala umjesto da nagađa. U ovom
tečaju, izvorni materijal može biti README lekcija, uzorci koda ili vanjski
resursi povezani s lekcijama.

Koristite RAG kada odgovor treba biti utemeljen na dokumentima, podacima ili trenutnim
datotekama projekta.

### Planiranje

Planiranje je korisno kada zahtjev ima više koraka. Držite planove kratkima i
dovoljno vidljivima za programera ili korisnika da ih može pregledati.

Za demo plan može biti:

1. Pronađi lekcije vezane uz upotrebu alata.
2. Sažmi najrelevantnije lekcije.
3. Preporuči jedan zadatak za vježbu.

### Kontekst

Kontekst je ono što model trenutno vidi. Premalo konteksta može učiniti da agent
propusti važne detalje. Previše konteksta može usporiti agenta, povećati troškove,
ili ga učiniti lakšim za zbunjivanje.

Dobra inženjerska praksa konteksta znači odabir pravih informacija za sljedeći
poziv modela.

### Memorija

Memorija je informacija spremljena za kasnije. Ne pohranjujte sve. Spremajte informacije
samo kada su korisne, sigurne i jednostavne za ažuriranje ili brisanje.

Na primjer, pamćenje da "učenik preferira primjere u Pythonu" može biti korisno.
Pamćenje osjetljivih osobnih podataka obično nije.

### Evaluacija i promatranje

Evaluacija postavlja pitanje: je li agent učinio pravu stvar?

Promatranje postavlja pitanje: možemo li vidjeti kako se to dogodilo?

Za produkcijske agente, pratite pozive modela, pozive alata, dohvaćeni kontekst,
kašnjenje, troškove, neuspjehe i povratne informacije korisnika.

### Povjerenje i sigurnost

Pouzdani agenti trebaju više od korisnog prompta. Koristite alate s najmanjim potrebnim
ovlastima, ljudsko odobrenje za radnje velikog utjecaja, redakciju podataka gdje je potrebno,
i zapise ili potvrde za radnje koje se moraju revidirati.

## Rutina pregleda od 15 minuta

Koristite ovu rutinu nakon svake lekcije:

1. **Sažeti lekciju u jednu rečenicu.**
2. **Imenujte novu sposobnost agenta.** Na primjer: upotreba alata, dohvat,
   planiranje, memorija, promatranje ili sigurnost.
3. **Dodajte je u demo pomoćnika tečaja.** Što se sada mijenja u demo verziji?
4. **Pronađite rizik.** Što bi moglo poći po zlu ako se ova sposobnost zloupotrijebi?
5. **Napišite jedno test pitanje.** Kako biste provjerili da se agent ponaša ispravno?

## Brza samoprovjera

Prije nego što nastavite, pokušajte odgovoriti na ova pitanja:

1. Što agent može učiniti, a obični chatbot ne može samostalno?
2. Koji alat bi vaš agent prvo trebao, i zašto?
3. Koji izvor znanja treba utemeljiti odgovor agenta?
4. Koji bi kontekst trebao biti uključen u sljedeći poziv modela?

5. Što bi agent trebao pamtiti, a što bi trebao izbjegavati spremati?
6. Kada bi agent trebao tražiti ljudsko odobrenje?
7. Koji bi zapisi, tragovi ili potvrde pomogli u kasnijem otklanjanju pogrešaka ili reviziji agenta?


## Predložena završna vježba

Na kraju tečaja, izgradite malog agenta koji pomaže učeniku da se snađe u ovom
spremištu.

Minimalna verzija:

- Prihvati temu od korisnika.
- Pronađi najrelevantnije lekcije.
- Sažmi što treba prvo pročitati.
- Predloži jedan praktični zadatak.
- Prikaži koje su lekcije ili poveznice korištene.

Proširena verzija:

- Zapamti preferirani programski jezik učenika.
- Upotrijebi jednostavan plan prije odgovora.
- Dodaj korak samoprovjere prije konačnog odgovora.
- Zabilježi pozive alata i dohvaćene izvore.
- Zatraži potvrdu prije otvaranja preglednika ili zadataka automatskog korisničkog sučelja.

Ovo ti daje mali, ali realan način za vježbanje alata, RAG-a, planiranja,
konteksta, memorije, uočljivosti i povjerenja u jednom projektu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->