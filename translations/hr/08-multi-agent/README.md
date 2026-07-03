[![Višestruki agenti dizajna](../../../translated_images/hr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite gornju sliku za pregled video lekcije)_

# Dizajnerski obrasci za više agenata

Čim započnete rad na projektu koji uključuje više agenata, morat ćete razmotriti obrazac dizajna za više agenata. Međutim, možda neće biti odmah jasno kada preći na višestruke agente i koje su prednosti.

## Uvod

U ovoj lekciji nastojimo odgovoriti na sljedeća pitanja:

- Koji su scenariji u kojima su višestruki agenti primjenjivi?
- Koje su prednosti korištenja višestrukih agenata u odnosu na samo jednog agenta koji obavlja više zadataka?
- Koji su gradivni blokovi implementacije obrasca dizajna za više agenata?
- Kako imamo uvid u to kako se višestruki agenti međusobno međusobno povezuju?

## Ciljevi učenja

Nakon ove lekcije trebali biste moći:

- Prepoznati scenarije gdje su višestruki agenti primjenjivi
- Prepoznati prednosti korištenja višestrukih agenata u odnosu na jednog agenta.
- Razumjeti gradivne blokove implementacije obrasca dizajna za više agenata.

Što je šira slika?

*Višestruki agenti su obrazac dizajna koji omogućava da više agenata zajednički radi na postizanju zajedničkog cilja*.

Ovaj obrazac se široko koristi u različitim područjima, uključujući robotiku, autonomne sustave i distribuirano računarstvo.

## Scenariji u kojima su višestruki agenti primjenjivi

Dakle, koji su scenariji dobar slučaj za korištenje višestrukih agenata? Odgovor je da postoji mnogo scenarija u kojima je upotreba više agenata korisna, osobito u sljedećim slučajevima:

- **Veliki radni opterećenji**: Veliki radni zadaci mogu se podijeliti na manje zadatke i dodijeliti različitim agentima, što omogućava paralelnu obradu i brže dovršenje. Primjer toga je kod velikog zadatka obrade podataka.
- **Složeni zadaci**: Složeni zadaci, poput velikih radnih opterećenja, mogu se razložiti na manje podzadatke i dodijeliti različitim agentima, od kojih svaki specijalizira u određenom aspektu zadatka. Dobar primjer je kod autonomnih vozila gdje različiti agenti upravljaju navigacijom, otkrivanjem prepreka i komunikacijom s drugim vozilima.
- **Raznolika stručnost**: Različiti agenti mogu imati različite stručnosti, što im omogućuje učinkovitije rješavanje različitih aspekata zadatka nego što bi to mogao jedan agent. Za ovaj slučaj, dobar primjer je u zdravstvu gdje agenti mogu upravljati dijagnostikom, planovima liječenja i nadzorom pacijenata.

## Prednosti korištenja višestrukih agenata u odnosu na jednog agenta

Sustav s jednim agentom može dobro raditi za jednostavne zadatke, ali za složenije zadatke korištenje višestrukih agenata može pružiti nekoliko prednosti:

- **Specijalizacija**: Svaki agent može biti specijaliziran za određeni zadatak. Nedostatak specijalizacije u jednom agentu znači da imate agenta koji može raditi sve, ali može se zbuniti što učiniti kad se suoči sa složenim zadatkom. Na primjer, mogao bi završiti radeći zadatak za koji nije najbolje kvalificiran.
- **Skalabilnost**: Lakše je skalirati sustave dodavanjem više agenata nego preopterećivanjem jednog agenta.
- **Otpornost na pogreške**: Ako jedan agent zakaže, ostali mogu nastaviti funkcionirati, osiguravajući pouzdanost sustava.

Uzmimo primjer, rezervirati putovanje za korisnika. Sustav s jednim agentom morao bi se baviti svim aspektima procesa rezervacije putovanja, od pronalaska letova do rezervacije hotela i najma automobila. Da bi se to postiglo jednim agentom, agent bi morao imati alate za rješavanje svih tih zadataka. To bi moglo dovesti do složenog i monolitnog sustava koji je težak za održavanje i skaliranje. Sustav s višestrukim agentima, s druge strane, mogao bi imati različite agente specijalizirane za pronalaženje letova, rezervaciju hotela i najam automobila. To bi sustav učinilo modularnijim, lakšim za održavanje i skalabilnim.

Usporedite to s putničkom agencijom vođenom kao obiteljska trgovina nasuprot putničkoj agenciji vođenoj kao franšiza. Obiteljska trgovina imala bi jednog agenta koji se bavi svim aspektima procesa rezervacije putovanja, dok bi franšiza imala različite agente koji se bave različitim aspektima procesa rezervacije.

## Gradivni blokovi implementacije obrasca dizajna za više agenata

Prije nego što počnete implementirati obrazac dizajna za više agenata, trebate razumjeti gradivne blokove koji čine obrazac.

Učinit ćemo to konkretnijim opet gledajući primjer rezervacije putovanja za korisnika. U ovom slučaju, gradivni blokovi uključuju:

- **Komunikacija među agentima**: Agenti za pronalazak letova, rezervaciju hotela i najam automobila trebaju komunicirati i dijeliti informacije o korisnikovim preferencijama i ograničenjima. Morate odlučiti o protokolima i metodama za tu komunikaciju. Konkretno, agent za pronalazak letova mora komunicirati s agentom za rezervaciju hotela kako bi se osiguralo da je hotel rezerviran za iste datume kao let. To znači da agenti moraju dijeliti informacije o datumima putovanja korisnika, što znači da morate odlučiti *koji agenti dijele informacije i kako ih dijele*.
- **Mehanizmi koordinacije**: Agenti trebaju koordinirati svoje akcije kako bi se zadovoljile korisničke preferencije i ograničenja. Korisnička preferencija može biti da žele hotel blizu aerodroma dok je ograničenje da su rent-a-car vozila dostupna samo na aerodromu. To znači da agent za rezervaciju hotela mora koordinirati s agentom za najam automobila kako bi se zadovoljile korisničke preferencije i ograničenja. Dakle, morate odlučiti *kako agenti koordiniraju svoje akcije*.
- **Arhitektura agenta**: Agenti trebaju imati internu strukturu za donošenje odluka i učenje iz interakcija s korisnikom. To znači da agent za pronalazak letova treba imati strukturu za odlučivanje o tome koje letove preporučiti korisniku. To znači da trebate odlučiti *kako agenti donose odluke i uče iz interakcija s korisnikom*. Primjeri učenja i poboljšanja agenta mogu biti da agent za pronalazak letova koristi model strojnog učenja za preporuku letova na temelju prethodnih preferencija korisnika.
- **Uvid u interakcije među višestrukim agentima**: Trebate imati uvid u to kako se višestruki agenti međusobno povezuju. To znači da trebate alate i tehnike za praćenje aktivnosti i interakcija agenata. To može biti u obliku alata za bilježenje i nadzor, vizualizacijske alate i metrike performansi.
- **Obrasci za više agenata**: Postoje različiti obrasci za implementaciju sustava s više agenata, poput centralizirane, decentralizirane i hibridne arhitekture. Morate odlučiti koji obrazac najbolje odgovara vašem slučaju uporabe.
- **Čovjek u petlji**: U većini slučajeva imat ćete čovjeka u petlji te morate uputiti agente kada tražiti ljudsku intervenciju. To može biti u obliku korisnika koji traži određeni hotel ili let koji agenti nisu preporučili ili traženja potvrde prije rezervacije leta ili hotela.

## Uvid u interakcije među višestrukim agentima

Važno je imati uvid u to kako se višestruki agenti međusobno povezuju. Ovaj uvid je bitan za otklanjanje pogrešaka, optimizaciju i osiguravanje ukupne učinkovitosti sustava. Da biste to postigli, trebate alate i tehnike za praćenje aktivnosti i interakcija agenata. To može biti u obliku alata za bilježenje i nadzor, vizualizacijskih alata i mjera izvedbe.

Na primjer, u slučaju rezervacije putovanja za korisnika, mogli biste imati nadzornu ploču koja prikazuje status svakog agenta, korisničke preferencije i ograničenja te interakcije među agentima. Ta nadzorna ploča mogla bi prikazivati datume putovanja korisnika, letove koje je preporučio agent za letove, hotele koje je preporučio agent za hotele te rent-a-car vozila koje je preporučio agent za najam automobila. To bi vam pružilo jasan uvid u to kako se agenti međusobno povezuju i zadovoljavaju li se korisničke preferencije i ograničenja.

Pogledajmo svaki od ovih aspekata detaljnije.

- **Alati za bilježenje i nadzor**: Želite imati bilježenje za svaku akciju koju agent poduzme. Zapis u dnevniku može pohraniti informacije o agentu koji je poduzeo akciju, poduzetoj akciji, vremenu kada je akcija poduzeta i rezultatu akcije. Te informacije mogu se koristiti za otklanjanje pogrešaka, optimizaciju i drugo.

- **Vizualizacijski alati**: Vizualizacijski alati mogu vam pomoći da intuitivnije vidite interakcije među agentima. Na primjer, mogli biste imati graf koji prikazuje protok informacija među agentima. To bi vam moglo pomoći u prepoznavanju uskih grla, neučinkovitosti i drugih problema u sustavu.

- **Metrike izvedbe**: Metrike izvedbe mogu vam pomoći u praćenju učinkovitosti sustava s više agenata. Na primjer, mogli biste pratiti vrijeme potrebno za dovršetak zadatka, broj dovršenih zadataka po jedinici vremena i točnost preporuka koje daju agenti. Te informacije mogu vam pomoći u prepoznavanju područja za poboljšanje i optimizaciji sustava.

## Obrasci za više agenata

Zaronimo u neke konkretne obrasce koje možemo koristiti za stvaranje aplikacija s više agenata. Evo nekoliko zanimljivih obrazaca vrijednih razmatranja:

### Grupni chat

Ovaj obrazac je koristan kada želite stvoriti aplikaciju grupnog chata u kojoj više agenata može međusobno komunicirati. Tipične primjene ovog obrasca uključuju timsku suradnju, korisničku podršku i društvene mreže.

U ovom obrascu svaki agent predstavlja korisnika u grupnom chatu, a poruke se razmjenjuju među agentima koristeći protokol za razmjenu poruka. Agenti mogu slati poruke u grupni chat, primati poruke iz grupnog chata i odgovarati na poruke drugih agenata.

Ovaj se obrazac može implementirati koristeći centraliziranu arhitekturu gdje su sve poruke usmjerene kroz središnji poslužitelj ili decentraliziranu arhitekturu gdje se poruke razmjenjuju izravno.

![Grupni chat](../../../translated_images/hr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Predaja zadataka

Ovaj obrazac je koristan kada želite stvoriti aplikaciju u kojoj višestruki agenti mogu međusobno predavati zadatke.

Tipične primjene ovog obrasca uključuju korisničku podršku, upravljanje zadacima i automatizaciju radnih tijekova.

U ovom obrascu svaki agent predstavlja zadatak ili korak u tijeku rada, a agenti mogu predavati zadatke drugim agentima na temelju unaprijed definiranih pravila.

![Predaja zadatka](../../../translated_images/hr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Suradnički filtriranje

Ovaj obrazac je koristan kada želite stvoriti aplikaciju u kojoj višestruki agenti mogu surađivati u davanju preporuka korisnicima.

Zašto bi višestruki agenti surađivali? Zato što svaki agent može imati različitu stručnost i može pridonijeti procesu preporuke na različite načine.

Uzmimo za primjer korisnika koji želi preporuku najboljih dionica za kupnju na burzi.

- **Stručnjak za industriju**: Jedan agent može biti stručnjak za određenu industriju.
- **Tehnička analiza**: Drugi agent može biti stručnjak za tehničku analizu.
- **Fundamentalna analiza**: I treći agent može biti stručnjak za fundamentalnu analizu. Suradnjom, ovi agenti mogu pružiti sveobuhvatniju preporuku korisniku.

![Preporuka](../../../translated_images/hr/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarij: Proces povrata novca

Razmotrite scenarij u kojem kupac pokušava dobiti povrat novca za proizvod, u tom procesu može biti uključeno prilično puno agenata, ali podijelit ćemo ih na agente specifične za taj proces i opće agente koji se mogu koristiti u drugim procesima.

**Agenti specifični za proces povrata novca**:

Slijede neki agenti koji bi mogli biti uključeni u proces povrata novca:

- **Agent kupca**: Ovaj agent predstavlja kupca i odgovoran je za pokretanje procesa povrata novca.
- **Agent prodavača**: Ovaj agent predstavlja prodavača i odgovoran je za obradu povrata novca.
- **Agent plaćanja**: Ovaj agent predstavlja proces plaćanja i odgovoran je za povrat novca kupcu.
- **Agent za rješavanje problema**: Ovaj agent predstavlja proces rješavanja problema i odgovoran je za rješavanje bilo kakvih problema koji se pojave tijekom procesa povrata novca.
- **Agent za usklađenost**: Ovaj agent predstavlja proces usklađenosti i odgovoran je za osiguranje da proces povrata novca zadovoljava propise i pravila.

**Opći agenti**:

Ovi agenti mogu se koristiti u drugim dijelovima vašeg poslovanja.

- **Agent dostave**: Ovaj agent predstavlja proces dostave i odgovoran je za slanje proizvoda natrag prodavaču. Ovaj se agent može koristiti i za proces povrata i za opću dostavu proizvoda putem kupnje, na primjer.
- **Agent za povratne informacije**: Ovaj agent predstavlja proces prikupljanja povratnih informacija i odgovoran je za prikupljanje povratnih informacija od kupca. Povratne informacije mogu se uzimati u bilo kojem trenutku, ne samo tijekom procesa povrata.
- **Agent za eskalaciju**: Ovaj agent predstavlja proces eskalacije i odgovoran je za eskalaciju problema na višu razinu podrške. Ovaj tip agenta možete koristiti za bilo koji proces gdje je potrebna eskalacija problema.
- **Agent za obavijesti**: Ovaj agent predstavlja proces obavještavanja i odgovoran je za slanje obavijesti kupcu u različitim fazama procesa povrata novca.
- **Agent za analitiku**: Ovaj agent predstavlja proces analize podataka vezanih uz proces povrata novca.
- **Agent za reviziju**: Ovaj agent predstavlja proces revizije i odgovoran je za provjeru ispravne provedbe procesa povrata.
- **Agent za izvještavanje**: Ovaj agent predstavlja proces izvještavanja i odgovoran je za generiranje izvještaja o procesu povrata novca.
- **Agent za znanje**: Ovaj agent predstavlja proces upravljanja znanjem i odgovoran je za održavanje baze znanja informacija vezanih uz proces povrata novca. Ovaj agent može biti dobro upućen i u povrate i u druge dijelove vašeg poslovanja.
- **Agent za sigurnost**: Ovaj agent predstavlja proces sigurnosti i odgovoran je za osiguranje sigurnosti procesa povrata novca.
- **Agent za kvalitetu**: Ovaj agent predstavlja proces kontrole kvalitete i odgovoran je za osiguranje kvalitete procesa povrata novca.

Postoji priličan broj agenata navedenih ranije, kako za specifični proces povrata novca, tako i za opće agente koji se mogu koristiti u drugim dijelovima vašeg poslovanja. Nadamo se da vam ovo daje ideju kako odlučiti koje agente koristiti u vašem sustavu s više agenata.

## Zadatak

Dizajnirajte sustav s više agenata za proces korisničke podrške. Identificirajte agente uključene u proces, njihove uloge i odgovornosti te kako međusobno djeluju. Razmotrite i agente specifične za proces korisničke podrške i opće agente koji se mogu koristiti u drugim dijelovima vašeg poslovanja.
> Razmislite prije nego što pročitate sljedeće rješenje, možda će vam trebati više agenata nego što mislite.

> SAVJET: Razmislite o različitim fazama procesa korisničke podrške i također uzmite u obzir agente potrebne za bilo koji sustav.

## Rješenje

[Rješenje](./solution/solution.md)

## Provjere znanja

Pitanje: Kada biste trebali razmotriti korištenje više agenata?

- [ ] A1: Kada imate mali opseg posla i jednostavan zadatak.
- [ ] A2: Kada imate velik opseg posla
- [ ] A3: Kada imate jednostavan zadatak.

[Rješenje kviza](./solution/solution-quiz.md)

## Sažetak

U ovoj lekciji smo pogledali dizajnerski obrazac više agenata, uključujući scenarije u kojima su višestruki agenti primjenjivi, prednosti korištenja više agenata u odnosu na jednog agenta, osnovne elemente implementacije dizajnerskog obrasca više agenata te kako imati uvid u način na koji višestruki agenti međusobno komuniciraju.

### Imate li dodatnih pitanja o dizajnerskom obrascu više agenata?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) kako biste se upoznali s drugim učenicima, sudjelovali na radnom vremenu i dobili odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacija Microsoft Agent Frameworka</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentni dizajnerski obrasci</a>


## Prethodna lekcija

[Planiranje dizajna](../07-planning-design/README.md)

## Sljedeća lekcija

[Metakognicija u AI agentima](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->