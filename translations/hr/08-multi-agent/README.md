[![Dizajn višestrukih agenata](../../../translated_images/hr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Obrasci dizajna višestrukih agenata

Čim počnete raditi na projektu koji uključuje više agenata, morat ćete razmotriti obrazac dizajna višestrukih agenata. Međutim, možda neće biti odmah jasno kada preći na višestruke agente i koje su prednosti.

## Uvod

U ovoj lekciji pokušavamo odgovoriti na sljedeća pitanja:

- Koje su situacije u kojima se višestruki agenti mogu primijeniti?
- Koje su prednosti korištenja višestrukih agenata u odnosu na samo jednog agenta koji obavlja više zadataka?
- Koji su gradivni blokovi implementacije obrasca dizajna višestrukih agenata?
- Kako imamo uvid u to kako višestruki agenti međusobno komuniciraju?

## Ciljevi učenja

Nakon ove lekcije trebali biste biti u stanju:

- Prepoznati situacije u kojima se višestruki agenti mogu primijeniti
- Uočiti prednosti korištenja višestrukih agenata u odnosu na pojedinačnog agenta.
- Razumjeti gradivne blokove implementacije obrasca dizajna višestrukih agenata.

Koja je šira slika?

*Višestruki agenti su obrazac dizajna koji omogućuje da više agenata surađuje kako bi ostvarilo zajednički cilj*.

Ovaj obrazac se široko koristi u raznim područjima, uključujući robotiku, autonomne sustave i distribuirano računarstvo.

## Situacije u kojima su višestruki agenti primjenjivi

Koje situacije su dobar slučaj za korištenje višestrukih agenata? Odgovor je da postoji mnogo situacija u kojima je korisno angažirati više agenata, naročito u sljedećim slučajevima:

- **Veliki poslovi**: Veliki poslovi se mogu podijeliti na manje zadatke i dodijeliti različitim agentima, što omogućava paralelnu obradu i brže izvršenje. Primjer ovoga je u slučaju velikog zadatka obrade podataka.
- **Složeni zadaci**: Složeni zadaci, slično velikim poslovima, mogu se razbiti u manje podzadatke i dodijeliti različitim agentima, od kojih se svaki specijalizira za određeni dio zadatka. Dobar primjer ovoga su autonomna vozila gdje različiti agenti upravljaju navigacijom, detekcijom prepreka i komunikacijom s drugim vozilima.
- **Raznolika ekspertiza**: Različiti agenti mogu imati različite stručnosti, što im omogućuje učinkovitije upravljanje različitim aspektima zadatka nego pojedinačni agent. Za ovaj slučaj dobar je primjer zdravstvena skrb, gdje agenti mogu upravljati dijagnostikom, planovima liječenja i praćenjem pacijenta.

## Prednosti korištenja višestrukih agenata u odnosu na pojedinačnog agenta

Sustav s jednim agentom može dobro funkcionirati za jednostavne zadatke, ali za složenije zadatke korištenje više agenata može imati nekoliko prednosti:

- **Specijalizacija**: Svaki agent može biti specijaliziran za određeni zadatak. Nedostatak specijalizacije kod pojedinačnog agenta znači da imate agenta koji može raditi sve, ali se može zbuniti kada se suoči sa složenim zadatkom. Na primjer, mogao bi završiti obavljajući zadatak za koji nije najbolje kvalificiran.
- **Skalabilnost**: Lakše je skalirati sustave dodavanjem više agenata nego opterećivanjem jednog agenta.
- **Otpornost na greške**: Ako jedan agent zakaže, drugi mogu nastaviti funkcionirati, osiguravajući pouzdanost sustava.

Uzmimo primjer, rezervirajmo putovanje za korisnika. Sustav s jednim agentom morao bi upravljati svim aspektima procesa rezervacije putovanja, od pronalaska letova do rezervacije hotela i najma automobila. Da bi to postigao, agent bi morao imati alate za sve te zadatke. To bi moglo dovesti do složenog i monolitnog sustava koji je teško održavati i skalirati. Sustav s višestrukim agentima, s druge strane, mogao bi imati različite agente specijalizirane za pronalazak letova, rezervaciju hotela i najam automobila. To bi sustav učinilo modularnijim, lakšim za održavanje i skalabilnim.

Usporedite to s putničkom agencijom vođenom kao obiteljski posao u usporedbi s franšizom. Obiteljski posao imao bi jednog agenta koji upravlja svim aspektima procesa rezervacije putovanja, dok franšiza ima različite agente koji upravljaju različitim aspektima procesa rezervacije.

## Gradivni blokovi implementacije obrasca dizajna višestrukih agenata

Prije nego što možete implementirati obrazac dizajna višestrukih agenata, morate razumjeti gradivne blokove koji tvorе obrazac.

Učinit ćemo to konkretnijim ponovno gledajući primjer rezervacije putovanja za korisnika. U ovom slučaju gradivni blokovi bi uključivali:

- **Komunikacija agenata**: Agenti za pronalazak letova, rezervaciju hotela i najam automobila trebaju komunicirati i dijeliti informacije o preferencijama i ograničenjima korisnika. Morate odlučiti o protokolima i metodama za tu komunikaciju. Konkretno, agent za pronalazak letova treba komunicirati s agentom za rezervaciju hotela kako bi osigurao da je hotel rezerviran za iste datume kao i let. To znači da agenti moraju dijeliti informacije o datumima putovanja korisnika, što znači da morate odlučiti *koji agenti dijele informacije i kako dijele informacije*.
- **Mehanizmi koordinacije**: Agenti moraju koordinirati svoje akcije kako bi osigurali da su preferencije i ograničenja korisnika zadovoljeni. Preferencija korisnika može biti da želi hotel blizu zračne luke, dok ograničenje može biti da su automobili za najam dostupni samo na zračnoj luci. To znači da agent za rezervaciju hotela mora koordinirati s agentom za najam automobila kako bi osigurao da su preferencije i ograničenja korisnika zadovoljeni. To znači da morate odlučiti *kako agenti koordiniraju svoje akcije*.
- **Arhitektura agenata**: Agenti trebaju imati unutarnju strukturu za donošenje odluka i učenje iz interakcija s korisnikom. To znači da agent za pronalazak letova mora imati unutarnju strukturu za donošenje odluka o tome koje letove preporučiti korisniku. To znači da morate odlučiti *kako agenti donose odluke i uče iz interakcija s korisnikom*. Primjeri kako agent uči i poboljšava se mogu biti da agent za pronalazak letova koristi model strojnog učenja za preporuke letova korisniku na temelju njihovih prethodnih preferencija.
- **Uvid u interakcije višestrukih agenata**: Morate imati uvid u to kako višestruki agenti međusobno komuniciraju. To znači da morate imati alate i tehnike za praćenje aktivnosti i interakcija agenata. To može biti u obliku alata za zapisivanje i nadzor, vizualizacijskih alata i metrike performansi.
- **Obrasci višestrukih agenata**: Postoje različiti obrasci za implementaciju sustava višestrukih agenata, poput centralizirane, decentralizirane i hibridne arhitekture. Morate odlučiti o obrascu koji najbolje odgovara vašem slučaju uporabe.
- **Čovjek u petlji**: U većini slučajeva imat ćete čovjeka u petlji i trebate uputiti agente kada tražiti ljudsku intervenciju. To može biti u obliku korisnika koji traži određeni hotel ili let koji agenti nisu preporučili ili traži potvrdu prije rezervacije leta ili hotela.

## Uvid u interakcije višestrukih agenata

Važno je da imate uvid u to kako višestruki agenti međusobno komuniciraju. Taj uvid je ključan za otklanjanje pogrešaka, optimizaciju i osiguravanje učinkovitosti cijelog sustava. Da biste to postigli, morate imati alate i tehnike za praćenje aktivnosti i interakcija agenata. To može biti u obliku alata za zapisivanje i nadzor, vizualizacijskih alata i metrike performansi.

Na primjer, u slučaju rezervacije putovanja za korisnika, mogli biste imati kontrolnu ploču koja prikazuje status svakog agenta, korisničke preferencije i ograničenja te interakcije među agentima. Ova kontrolna ploča može prikazivati datume putovanja korisnika, letove koje je preporučio agent za letove, hotele koje je preporučio agent za hotele te najam automobilа kojeg je preporučio agent za najam. To bi vam dalo jasan pregled kako agenti međusobno komuniciraju i ispunjavaju li korisničke preferencije i ograničenja.

Pogledajmo svaki od ovih aspekata detaljnije.

- **Alati za zapisivanje i nadzor**: Želite bilježiti svaku akciju koju agent poduzme. Zapis u dnevnik može čuvati informacije o agentu koji je poduzeo akciju, akciji koja je poduzeta, vremenu kada je akcija poduzeta i ishodu akcije. Ove informacije tada se mogu koristiti za otklanjanje pogrešaka, optimizaciju i drugo.

- **Vizualizacijski alati**: Vizualizacijski alati mogu vam pomoći da vidite interakcije među agentima na intuitivniji način. Na primjer, mogli biste imati graf koji prikazuje protok informacija između agenata. To može pomoći u identifikaciji uskih grla, neučinkovitosti i drugih problema u sustavu.

- **Metrički pokazatelji performansi**: Metrički pokazatelji mogu vam pomoći pratiti učinkovitost sustava višestrukih agenata. Na primjer, mogli biste pratiti vrijeme potrebno za izvršenje zadatka, broj zadataka završenih u jedinici vremena i točnost preporuka koje daju agenti. Te informacije pomažu u pronalaženju područja za poboljšanje i optimizaciji sustava.

## Obrasci višestrukih agenata

Idemo se upoznati s konkretnim obrascima koje možemo koristiti za stvaranje aplikacija s višestrukim agentima. Evo nekoliko zanimljivih obrazaca vrijednih razmatranja:

### Grupni chat

Ovaj obrazac je koristan kada želite stvoriti aplikaciju za grupni chat u kojoj se više agenata mogu međusobno komunicirati. Tipični slučajevi uporabe ovog obrasca uključuju timsku suradnju, korisničku podršku i društveno umrežavanje.

U ovom obrascu, svaki agent predstavlja korisnika u grupnom chatu, a poruke se razmjenjuju između agenata koristeći protokol poruka. Agenti mogu slati poruke u grupni chat, primati poruke iz grupnog chata i odgovarati na poruke drugih agenata.

Ovaj se obrazac može implementirati koristeći centraliziranu arhitekturu gdje se sve poruke usmjeravaju putem središnjeg poslužitelja, ili decentraliziranu arhitekturu gdje se poruke razmjenjuju izravno.

![Grupni chat](../../../translated_images/hr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Predaja zadataka

Ovaj obrazac je koristan kada želite stvoriti aplikaciju gdje više agenata može predavati zadatke jedan drugome.

Tipični slučajevi uporabe ovog obrasca uključuju korisničku podršku, upravljanje zadacima i automatizaciju tijeka rada.

U ovom obrascu, svaki agent predstavlja zadatak ili korak u tijeku rada, a agenti mogu predavati zadatke drugim agentima na osnovi unaprijed definiranih pravila.

![Predaja zadataka](../../../translated_images/hr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Suradničko filtriranje

Ovaj obrazac je koristan kada želite stvoriti aplikaciju u kojoj više agenata može surađivati kako bi dali preporuke korisnicima.

Zašto biste željeli da više agenata surađuje? Zato što svaki agent može imati različitu stručnost i može na različite načine doprinositi procesu preporuke.

Uzmimo primjer gdje korisnik želi preporuku za najbolju dionicu za kupnju na burzi.

- **Stručnjak za industriju**: Jedan agent mogao bi biti stručnjak za određenu industriju.
- **Tehnička analiza**: Drugi agent mogao bi biti stručnjak za tehničku analizu.
- **Fundamentalna analiza**: a treći agent mogao bi biti stručnjak za fundamentalnu analizu. Suradnjom ovi agenti mogu pružiti potpuniju preporuku korisniku.

![Preporuka](../../../translated_images/hr/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarij: Proces povrata novca

Razmotrite scenarij u kojem kupac pokušava dobiti povrat novca za proizvod, u tom je procesu uključeno dosta agenata, ali podijelit ćemo ih na agente specifične za taj proces i opće agente koji se mogu koristiti u drugim procesima.

**Agenti specifični za proces povrata novca**:

Slijede neki agenti koji bi mogli biti uključeni u proces povrata novca:

- **Agent kupca**: Ovaj agent predstavlja kupca i odgovoran je za pokretanje procesa povrata novca.
- **Agent prodavača**: Ovaj agent predstavlja prodavača i odgovoran je za obradu povrata novca.
- **Agent plaćanja**: Ovaj agent predstavlja proces plaćanja i odgovoran je za vraćanje novca kupcu.
- **Agent za rješavanje problema**: Ovaj agent predstavlja proces rješavanja problema i odgovoran je za rješavanje svih problema koji nastanu tijekom procesa povrata novca.
- **Agent usklađenosti**: Ovaj agent predstavlja proces usklađenosti i osigurava da proces povrata novca zadovoljava propise i pravila.

**Opći agenti**:

Ovi agenti se mogu koristiti i u drugim dijelovima vašeg poslovanja.

- **Agent dostave**: Ovaj agent predstavlja proces dostave i odgovoran je za vraćanje proizvoda prodavaču. Ovaj agent se može koristiti i u procesu povrata i za opću dostavu proizvoda prilikom kupovine npr.
- **Agent feedbacka**: Ovaj agent predstavlja proces prikupljanja povratnih informacija od kupca. Povratne informacije se mogu prikupljati u bilo kojem trenutku, a ne samo tijekom procesa povrata novca.
- **Agent eskalacije**: Ovaj agent je odgovoran za eskalaciju problema na višu razinu podrške. Ovakav se agent može koristiti u bilo kojem procesu kod kojeg je potrebna eskalacija problema.
- **Agent obavijesti**: Ovaj agent je odgovoran za slanje obavijesti kupcu u različitim fazama procesa povrata novca.
- **Agent analitike**: Ovaj agent je odgovoran za analizu podataka vezanih uz proces povrata novca.
- **Agent revizije**: Ovaj agent je odgovoran za reviziju procesa povrata novca kako bi se osiguralo da se provodi ispravno.
- **Agent izvještavanja**: Ovaj agent je odgovoran za generiranje izvještaja o procesu povrata novca.
- **Agent znanja**: Ovaj agent upravlja bazom znanja vezanom za proces povrata novca. Ovaj agent može biti stručan i za povrate i za druge dijelove vašeg poslovanja.
- **Agent sigurnosti**: Ovaj agent je odgovoran za osiguravanje sigurnosti procesa povrata novca.
- **Agent kvalitete**: Ovaj agent je odgovoran za osiguravanje kvalitete procesa povrata novca.

Puno je agenata nabrojano, kako specifičnih za proces povrata, tako i općih agenata koji se mogu koristiti u drugim dijelovima poslovanja. Nadamo se da vam to daje ideju kako možete odlučiti koje agente koristiti u sustavu višestrukih agenata.

## Zadatak

Dizajnirajte sustav višestrukih agenata za proces korisničke podrške. Identificirajte agente uključene u proces, njihove uloge i odgovornosti te kako međusobno komuniciraju. Uzmite u obzir kako agente specifične za korisničku podršku tako i opće agente koji se mogu koristiti u drugim dijelovima vašeg poslovanja.


> Razmislite prije nego što pročitate sljedeće rješenje, možda će vam trebati više agenata nego što mislite.

> SAVJET: Razmislite o različitim fazama procesa korisničke podrške i također uzmite u obzir agente potrebne za bilo koji sustav.

## Rješenje

[Rješenje](./solution/solution.md)

## Provjere znanja

### Pitanje 1

Koji je scenarij najsnažniji za sustav s više agenata?

- [ ] A1: Bot za podršku odgovara na često postavljana pitanja koristeći jednu bazu znanja i mali skup alata.
- [ ] A2: Radni tok za povrat novca zahtijeva odvojene uloge za prijevaru, plaćanje i usklađenost, svaka sa svojim alatima, a njihovi rezultati se moraju koordinirati.
- [ ] A3: Isti jednostavan zahtjev za klasifikacijom stiže tisućama puta na sat.

### Pitanje 2

Kada je pojedinačni agent obično bolji izbor?

- [ ] A1: Zadatak se može obaviti s jednim skupom uputa i alata, bez prepuštanja specijalistima.
- [ ] A2: Agent ima pristup više od jednog alata.
- [ ] A3: Radni tok zahtijeva odvojene uloge s različitim dopuštenjima i neovisnim revizijskim tragovima.

[Rješenje kviza](./solution/solution-quiz.md)

## Sažetak

U ovoj lekciji pogledali smo obrazac dizajna s više agenata, uključujući scenarije u kojima se više agenata može primijeniti, prednosti korištenja više agenata u odnosu na jednog agenta, gradivne blokove za implementaciju obrasca dizajna s više agenata i kako imati pregled nad interakcijama između više agenata.

### Imate li dodatnih pitanja o obrascu dizajna s više agenata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se upoznali s drugim polaznicima, sudjelovali na radnim satima i dobili odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacija Microsoft Agent Frameworka</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentni obrasci dizajna</a>


## Prethodna lekcija

[Planiranje dizajna](../07-planning-design/README.md)

## Sljedeća lekcija

[Metakognicija u AI agentima](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->