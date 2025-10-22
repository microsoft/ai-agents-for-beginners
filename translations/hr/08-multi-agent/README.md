<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T23:01:37+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "hr"
}
-->
[![Višestruki dizajn agenata](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.hr.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

# Obrasci dizajna višestrukih agenata

Čim počnete raditi na projektu koji uključuje više agenata, morat ćete razmotriti obrazac dizajna višestrukih agenata. Međutim, možda neće biti odmah jasno kada prijeći na višestruke agente i koje su prednosti.

## Uvod

U ovoj lekciji nastojimo odgovoriti na sljedeća pitanja:

- Koji su scenariji u kojima su višestruki agenti primjenjivi?
- Koje su prednosti korištenja višestrukih agenata u odnosu na jednog agenta koji obavlja više zadataka?
- Koji su osnovni elementi za implementaciju obrasca dizajna višestrukih agenata?
- Kako možemo imati pregled nad interakcijama između višestrukih agenata?

## Ciljevi učenja

Nakon ove lekcije trebali biste moći:

- Identificirati scenarije u kojima su višestruki agenti primjenjivi.
- Prepoznati prednosti korištenja višestrukih agenata u odnosu na jednog agenta.
- Razumjeti osnovne elemente za implementaciju obrasca dizajna višestrukih agenata.

Šira slika?

*Višestruki agenti su obrazac dizajna koji omogućuje da više agenata surađuje kako bi postigli zajednički cilj.*

Ovaj obrazac se široko koristi u raznim područjima, uključujući robotiku, autonomne sustave i distribuirano računalstvo.

## Scenariji u kojima su višestruki agenti primjenjivi

Koji su to scenariji u kojima je korisno koristiti višestruke agente? Odgovor je da postoji mnogo scenarija u kojima je primjena višestrukih agenata korisna, posebno u sljedećim slučajevima:

- **Veliki radni zadaci**: Veliki radni zadaci mogu se podijeliti na manje zadatke i dodijeliti različitim agentima, omogućujući paralelnu obradu i brže dovršavanje. Primjer za to je obrada velike količine podataka.
- **Složeni zadaci**: Složeni zadaci, poput velikih radnih zadataka, mogu se razložiti na manje podzadatke i dodijeliti različitim agentima, od kojih svaki specijalizira određeni aspekt zadatka. Dobar primjer za to su autonomna vozila gdje različiti agenti upravljaju navigacijom, otkrivanjem prepreka i komunikacijom s drugim vozilima.
- **Raznolika stručnost**: Različiti agenti mogu imati raznoliku stručnost, omogućujući im da se učinkovitije bave različitim aspektima zadatka nego jedan agent. Primjer za to je zdravstvena skrb gdje agenti mogu upravljati dijagnostikom, planovima liječenja i praćenjem pacijenata.

## Prednosti korištenja višestrukih agenata u odnosu na jednog agenta

Sustav s jednim agentom može dobro funkcionirati za jednostavne zadatke, ali za složenije zadatke korištenje višestrukih agenata može donijeti nekoliko prednosti:

- **Specijalizacija**: Svaki agent može biti specijaliziran za određeni zadatak. Nedostatak specijalizacije kod jednog agenta znači da imate agenta koji može raditi sve, ali se može zbuniti kada se suoči sa složenim zadatkom. Na primjer, može završiti radeći zadatak za koji nije najbolje prilagođen.
- **Skalabilnost**: Lakše je skalirati sustave dodavanjem više agenata nego preopterećivanjem jednog agenta.
- **Otpornost na greške**: Ako jedan agent zakaže, drugi mogu nastaviti funkcionirati, osiguravajući pouzdanost sustava.

Uzmimo primjer: rezervacija putovanja za korisnika. Sustav s jednim agentom morao bi upravljati svim aspektima procesa rezervacije putovanja, od pronalaženja letova do rezervacije hotela i iznajmljivanja automobila. Da bi to postigao, agent bi morao imati alate za upravljanje svim tim zadacima. To bi moglo dovesti do složenog i monolitnog sustava koji je teško održavati i skalirati. Sustav s višestrukim agentima, s druge strane, mogao bi imati različite agente specijalizirane za pronalaženje letova, rezervaciju hotela i iznajmljivanje automobila. To bi sustav učinilo modularnijim, lakšim za održavanje i skalabilnim.

Usporedimo to s turističkom agencijom vođenom kao obiteljski posao naspram turističke agencije vođene kao franšiza. Obiteljski posao imao bi jednog agenta koji upravlja svim aspektima procesa rezervacije putovanja, dok bi franšiza imala različite agente koji upravljaju različitim aspektima procesa rezervacije putovanja.

## Osnovni elementi za implementaciju obrasca dizajna višestrukih agenata

Prije nego što možete implementirati obrazac dizajna višestrukih agenata, morate razumjeti osnovne elemente koji čine taj obrazac.

Uzmimo konkretan primjer rezervacije putovanja za korisnika. U ovom slučaju, osnovni elementi uključuju:

- **Komunikacija agenata**: Agenti za pronalaženje letova, rezervaciju hotela i iznajmljivanje automobila moraju komunicirati i dijeliti informacije o korisnikovim preferencijama i ograničenjima. Morate odlučiti o protokolima i metodama za ovu komunikaciju. Konkretno, to znači da agent za pronalaženje letova mora komunicirati s agentom za rezervaciju hotela kako bi osigurao da je hotel rezerviran za iste datume kao i let. To znači da agenti moraju dijeliti informacije o korisnikovim datumima putovanja, što znači da morate odlučiti *koji agenti dijele informacije i kako ih dijele*.
- **Mehanizmi koordinacije**: Agenti moraju koordinirati svoje radnje kako bi osigurali da su korisnikove preferencije i ograničenja ispunjeni. Korisnička preferencija mogla bi biti da žele hotel blizu zračne luke, dok bi ograničenje moglo biti da su automobili za iznajmljivanje dostupni samo na zračnoj luci. To znači da agent za rezervaciju hotela mora koordinirati s agentom za rezervaciju automobila kako bi osigurao da su korisnikove preferencije i ograničenja ispunjeni. To znači da morate odlučiti *kako agenti koordiniraju svoje radnje*.
- **Arhitektura agenata**: Agenti moraju imati unutarnju strukturu za donošenje odluka i učenje iz svojih interakcija s korisnikom. To znači da agent za pronalaženje letova mora imati unutarnju strukturu za donošenje odluka o tome koje letove preporučiti korisniku. To znači da morate odlučiti *kako agenti donose odluke i uče iz svojih interakcija s korisnikom*. Primjeri kako agent uči i poboljšava se mogli bi biti da agent za pronalaženje letova koristi model strojnog učenja za preporuku letova korisniku na temelju njihovih prošlih preferencija.
- **Pregled interakcija višestrukih agenata**: Morate imati pregled nad interakcijama između višestrukih agenata. To znači da morate imati alate i tehnike za praćenje aktivnosti i interakcija agenata. To bi moglo biti u obliku alata za zapisivanje i praćenje, alata za vizualizaciju i mjernih podataka o izvedbi.
- **Obrasci višestrukih agenata**: Postoje različiti obrasci za implementaciju sustava višestrukih agenata, poput centraliziranih, decentraliziranih i hibridnih arhitektura. Morate odlučiti o obrascu koji najbolje odgovara vašem slučaju.
- **Čovjek u petlji**: U većini slučajeva imat ćete čovjeka u petlji i morate uputiti agente kada tražiti ljudsku intervenciju. To bi moglo biti u obliku korisnika koji traži određeni hotel ili let koji agenti nisu preporučili ili traži potvrdu prije rezervacije leta ili hotela.

## Pregled interakcija višestrukih agenata

Važno je da imate pregled nad interakcijama između višestrukih agenata. Ovaj pregled je ključan za otklanjanje grešaka, optimizaciju i osiguranje učinkovitosti cjelokupnog sustava. Da biste to postigli, morate imati alate i tehnike za praćenje aktivnosti i interakcija agenata. To bi moglo biti u obliku alata za zapisivanje i praćenje, alata za vizualizaciju i mjernih podataka o izvedbi.

Na primjer, u slučaju rezervacije putovanja za korisnika, mogli biste imati nadzornu ploču koja prikazuje status svakog agenta, korisnikove preferencije i ograničenja te interakcije između agenata. Ova nadzorna ploča mogla bi prikazivati korisnikove datume putovanja, letove koje preporučuje agent za letove, hotele koje preporučuje agent za hotele i automobile koje preporučuje agent za iznajmljivanje automobila. To bi vam dalo jasan pregled kako agenti međusobno djeluju i jesu li korisnikove preferencije i ograničenja ispunjeni.

Pogledajmo detaljnije svaki od ovih aspekata.

- **Alati za zapisivanje i praćenje**: Želite zapisivati svaku radnju koju poduzme agent. Unos zapisa mogao bi sadržavati informacije o agentu koji je poduzeo radnju, poduzetoj radnji, vremenu kada je radnja poduzeta i ishodu radnje. Ove informacije mogu se koristiti za otklanjanje grešaka, optimizaciju i više.
- **Alati za vizualizaciju**: Alati za vizualizaciju mogu vam pomoći da vidite interakcije između agenata na intuitivniji način. Na primjer, mogli biste imati grafikon koji prikazuje tok informacija između agenata. To bi vam moglo pomoći da identificirate uska grla, neučinkovitosti i druge probleme u sustavu.
- **Mjerni podaci o izvedbi**: Mjerni podaci o izvedbi mogu vam pomoći da pratite učinkovitost sustava višestrukih agenata. Na primjer, mogli biste pratiti vrijeme potrebno za dovršavanje zadatka, broj dovršenih zadataka po jedinici vremena i točnost preporuka koje daju agenti. Ove informacije mogu vam pomoći da identificirate područja za poboljšanje i optimizirate sustav.

## Obrasci višestrukih agenata

Pogledajmo konkretne obrasce koje možemo koristiti za stvaranje aplikacija s višestrukim agentima. Evo nekoliko zanimljivih obrazaca koje vrijedi razmotriti:

### Grupni chat

Ovaj obrazac je koristan kada želite stvoriti aplikaciju za grupni chat u kojoj više agenata može međusobno komunicirati. Tipični slučajevi upotrebe za ovaj obrazac uključuju timsku suradnju, korisničku podršku i društvene mreže.

U ovom obrascu, svaki agent predstavlja korisnika u grupnom chatu, a poruke se razmjenjuju između agenata koristeći protokol za razmjenu poruka. Agenti mogu slati poruke u grupni chat, primati poruke iz grupnog chata i odgovarati na poruke drugih agenata.

Ovaj obrazac može se implementirati koristeći centraliziranu arhitekturu gdje se sve poruke usmjeravaju kroz centralni poslužitelj ili decentraliziranu arhitekturu gdje se poruke razmjenjuju izravno.

![Grupni chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.hr.png)

### Predaja zadatka

Ovaj obrazac je koristan kada želite stvoriti aplikaciju u kojoj više agenata može predavati zadatke jedni drugima.

Tipični slučajevi upotrebe za ovaj obrazac uključuju korisničku podršku, upravljanje zadacima i automatizaciju tijeka rada.

U ovom obrascu, svaki agent predstavlja zadatak ili korak u tijeku rada, a agenti mogu predavati zadatke drugim agentima na temelju unaprijed definiranih pravila.

![Predaja zadatka](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.hr.png)

### Kolaborativno filtriranje

Ovaj obrazac je koristan kada želite stvoriti aplikaciju u kojoj više agenata može surađivati kako bi korisnicima dali preporuke.

Zašto biste željeli da više agenata surađuje? Zato što svaki agent može imati različitu stručnost i može doprinijeti procesu preporuka na različite načine.

Uzmimo primjer gdje korisnik želi preporuku za najbolju dionicu za kupnju na burzi.

- **Industrijski stručnjak**: Jedan agent mogao bi biti stručnjak za određenu industriju.
- **Tehnička analiza**: Drugi agent mogao bi biti stručnjak za tehničku analizu.
- **Fundamentalna analiza**: Treći agent mogao bi biti stručnjak za fundamentalnu analizu. Suradnjom, ovi agenti mogu korisniku pružiti sveobuhvatniju preporuku.

![Preporuka](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.hr.png)

## Scenarij: Proces povrata novca

Razmotrimo scenarij u kojem korisnik pokušava dobiti povrat novca za proizvod. U ovom procesu može biti uključeno dosta agenata, ali podijelimo ih na agente specifične za ovaj proces i opće agente koji se mogu koristiti u drugim procesima.

**Agenti specifični za proces povrata novca**:

Slijede neki agenti koji bi mogli biti uključeni u proces povrata novca:

- **Agent korisnika**: Ovaj agent predstavlja korisnika i odgovoran je za pokretanje procesa povrata novca.
- **Agent prodavatelja**: Ovaj agent predstavlja prodavatelja i odgovoran je za obradu povrata novca.
- **Agent plaćanja**: Ovaj agent predstavlja proces plaćanja i odgovoran je za povrat korisnikove uplate.
- **Agent za rješavanje problema**: Ovaj agent predstavlja proces rješavanja problema i odgovoran je za rješavanje svih problema koji se pojave tijekom procesa povrata novca.
- **Agent za usklađenost**: Ovaj agent predstavlja proces usklađenosti i odgovoran je za osiguranje da proces povrata novca bude u skladu s propisima i politikama.

**Opći agenti**:

Ovi agenti mogu se koristiti u drugim dijelovima vašeg poslovanja.

- **Agent za dostavu**: Ovaj agent predstavlja proces dostave i odgovoran je za dostavu proizvoda natrag prodavatelju. Ovaj agent može se koristiti i za proces povrata novca i za opću dostavu proizvoda, primjerice nakon kupnje.
- **Agent za povratne informacije**: Ovaj agent predstavlja proces povratnih informacija i odgovoran je za prikupljanje povratnih informacija od korisnika. Povratne informacije mogu se prikupljati u bilo kojem trenutku, ne samo tijekom procesa povrata novca.
- **Agent za eskalaciju**: Ovaj agent predstavlja proces eskalacije i odgovoran je za eskalaciju problema na višu razinu podrške. Ova vrsta agenta može se koristiti u bilo kojem procesu gdje je potrebno eskalirati problem.
- **Agent za obavijesti**: Ovaj agent predstavlja proces obavijesti i odgovoran je za slanje obavijesti korisniku u različitim fazama procesa povrata novca.
- **Agent za analitiku**: Ovaj agent predstavlja proces analitike i odgovoran je za analizu podataka povezanih s procesom povrata novca.
- **Agent za reviziju**: Ovaj agent predstavlja proces revizije i odgovoran je za reviziju procesa povrata novca kako bi se osiguralo da se provodi ispravno.
- **Agent za izvještavanje**: Ovaj agent predstavlja proces izvještavanja i odgovoran je za generiranje izvještaja o procesu povrata novca.
- **Agent za znanje**: Ovaj agent predstavlja proces znanja i odgovoran je za održavanje baze znanja informacija povezanih s procesom povrata novca. Ovaj agent može biti informiran i o povratima i o drugim dijelovima vašeg poslovanja.
- **Agent za sigurnost**: Ovaj agent predstavlja proces sigurnosti i odgovoran je za osiguranje sigurnosti procesa povrata novca.
- **Agent za kvalitetu**: Ovaj agent predstavlja proces kvalitete i odgovoran je za osiguranje kvalitete procesa povrata novca.

Naveden je priličan broj agenata, kako specifičnih za proces povrata novca, tako i općih agenata koji se mogu koristiti u drugim dijelovima vašeg poslovanja. Nadamo se da vam ovo daje ideju kako možete odlučiti koje agente koristiti u svom sustavu višestrukih agenata.

## Zadatak
Dizajnirajte sustav s više agenata za proces korisničke podrške. Identificirajte agente uključene u proces, njihove uloge i odgovornosti te kako međusobno komuniciraju. Razmotrite i specifične agente za proces korisničke podrške i opće agente koji se mogu koristiti u drugim dijelovima vašeg poslovanja.

> Razmislite prije nego što pročitate sljedeće rješenje, možda će vam trebati više agenata nego što mislite.

> TIP: Razmislite o različitim fazama procesa korisničke podrške i također uzmite u obzir agente potrebne za bilo koji sustav.

## Rješenje

[Rješenje](./solution/solution.md)

## Provjera znanja

Pitanje: Kada biste trebali razmotriti korištenje sustava s više agenata?

- [ ] A1: Kada imate mali opseg posla i jednostavan zadatak.
- [ ] A2: Kada imate veliki opseg posla.
- [ ] A3: Kada imate jednostavan zadatak.

[Kviz rješenja](./solution/solution-quiz.md)

## Sažetak

U ovoj lekciji smo razmotrili dizajnerski obrazac s više agenata, uključujući scenarije u kojima su primjenjivi, prednosti korištenja više agenata u odnosu na jednog agenta, osnovne elemente implementacije dizajnerskog obrasca s više agenata te kako imati uvid u međusobnu interakciju više agenata.

### Imate li dodatnih pitanja o dizajnerskom obrascu s više agenata?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, sudjelovali u uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

## Prethodna lekcija

[Dizajn planiranja](../07-planning-design/README.md)

## Sljedeća lekcija

[Metakognicija u AI agentima](../09-metacognition/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.