# Izgradnja agenata za korištenje računala (CUA)

Agenti za korištenje računala mogu komunicirati s web stranicama na isti način kao i osoba: otvaranjem preglednika, pregledavanjem stranice i poduzimanjem najbolje sljedeće akcije na temelju onoga što vide. U ovoj lekciji izgradit ćete agenta za automatizaciju preglednika koji traži na Airbnbu, izvlači strukturirane podatke o oglasima i identificira najjeftiniji smještaj u Stockholmu.

Lekcija kombinira Browser-Use za navigaciju vođenu umjetnom inteligencijom, Playwright i Chrome DevTools Protocol (CDP) za upravljanje preglednikom, Azure OpenAI za rezoniranje s podrškom vida te Pydantic za strukturirano izvlačenje.

## Uvod

Ova lekcija će obuhvatiti:

- Razumijevanje kada su agenti za korištenje računala prikladniji od same API automatizacije
- Kombiniranje Browser-Use s Playwrightom i CDP za pouzdano upravljanje životnim ciklusom preglednika
- Korištenje Azure OpenAI vida i strukturiranog Pydantic izlaza za izvlačenje podataka o oglasima sa dinamičnih web stranica
- Odlučivanje kada koristiti agent-prvi, actor-prvi ili hibridni tijek rada za automatizaciju preglednika

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete kako:

- Konfigurirati Browser-Use s Azure OpenAI i Playwrightom
- Izgraditi tijek rada za automatizaciju preglednika koji navigira pravom web stranicom i rukuje dinamičkim elementima korisničkog sučelja
- Izvući tipizirane rezultate iz vidljivog sadržaja stranice i pretvoriti ih u poslovnu logiku
- Odabrati između agent i actor obrazaca na temelju predvidivosti zadatka preglednika

## Primjer koda

Ova lekcija uključuje jedan tutorial u bilježnici:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Pokreće Chrome sesiju preko CDP-a, pretražuje Airbnb za oglase u Stockholmu, izdvaja cijene koristeći Browser-Use vid, i vraća najjeftiniju opciju kao strukturirane podatke.

## Preduvjeti

- Python 3.12+
- Konfigurirani Azure OpenAI deployment u vašem okruženju
- Lokalno instalirani Chrome ili Chromium
- Instalirane Playwright ovisnosti
- Osnovno poznavanje asinhronog Python-a

## Postavljanje

Instalirajte pakete korištene u bilježnici:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Postavite Azure OpenAI varijable okruženja koje bilježnica koristi:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcionalno: zadana vrijednost je najnovija verzija API-ja ako je izostavljeno
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Bilježnica demonstrira hibridni tijek rada automatizacije preglednika:

1. Chrome se pokreće s omogućenim CDP-om kako bi Playwright i Browser-Use dijelili istu sesiju preglednika.
2. Agent Browser-Use upravlja zadacima otvorene navigacije poput otvaranja Airbnba, zatvaranja iskačućih prozora i pretraživanja Stockholma.
3. Aktivna stranica se pregledava pomoću strukturirane Pydantic sheme za izvlačenje naslova oglasa, cijena po noći, ocjena i URL-ova.
4. Python logika uspoređuje izvučene oglase i ističe najjeftiniji rezultat.

Ovaj pristup zadržava fleksibilno rezoniranje temeljeno na viđenom koje Browser-Use dobro radi, dok vam istovremeno daje determinističku kontrolu nad preglednikom kad vam zatreba.

## Ključne spoznaje i najbolje prakse

### Kada koristiti agenta u odnosu na glumca (actor)

| Scenarij | Koristi agenta | Koristi glumca |
|----------|-----------|-----------|
| Dinamični rasporedi | Da, AI se može prilagoditi promjenama stranice | Ne, lomljivi selektori mogu prestati raditi |
| Poznata struktura | Ne, agent je sporiji od izravne kontrole | Da, brzo i precizno |
| Pronalaženje elemenata | Da, prirodni jezik dobro funkcionira | Ne, potrebni su točni selektori |
| Kontrola vremena | Ne, manje predvidivo | Da, potpuna kontrola nad čekanjima i pokušajima |
| Složeni tijekovi rada | Da, rukuje neočekivanim stanjima sučelja | Ne, zahtijeva eksplicitno grananje |

### Najbolje prakse za Browser-Use

1. Započnite s agentom za istraživanje i dinamičnu navigaciju.
2. Prebacite se na izravnu kontrolu stranice kada interakcija postane predvidiva.
3. Koristite modele za strukturirani izlaz kako bi izvlačeni podaci bili verificirani i tipizirani.
4. Dodajte kašnjenja strateški nakon akcija koje pokreću vidljive promjene u sučelju.
5. Snimajte zaslone tijekom iteracija kako bi se kvarovi lakše dijagnosticirali.
6. Očekujte promjene na web stranicama i dizajnirajte rezervne strategije za iskačuće prozore i pomake u rasporedu.
7. Kombinirajte agent i actor obrasce za dobivanje fleksibilnosti i preciznosti.

### Sigurnosne mjere za agente preglednika

Agenti preglednika rade na živim web stranicama, pa im trebaju stroža ograničenja od skripte koja samo poziva poznati API. Prije nego što prijeđete s demo bilježnice na stvarni tijek rada, definirajte kontrole oko toga što agent može vidjeti, kliknuti i poslati.

1. **Ograničite pregledno okruženje.** Pokrenite agenta u posvećenom profilu preglednika ili pješčaniku i ograničite ga na domene potrebne za zadatak.
2. **Odvojite promatranje od akcije.** Neka agent prvo pretražuje, čita i izvlači podatke; zahtijevajte eksplicitni korak odobrenja prije nego što šalje obrasce, poruke, rezervacije putovanja, kupnje, briše zapise ili mijenja postavke računa.
3. **Držite tajne izvan upita i zapisa.** Ne stavljajte lozinke, podatke o plaćanju, kolačiće sesije ili sirove osobne podatke u kontekst modela. Neka korisnik preuzme autentifikaciju i ukloni osjetljiva polja iz dnevnika.
4. **Tretirajte sadržaj stranice kao nepouzdani ulaz.** Web stranica može sadržavati upute namijenjene agentu, a ne korisniku. Agent bi trebao ignorirati tekst stranice koji traži promjenu cilja, otkrivanje podataka, onemogućavanje zaštita ili posjet nepovezanim stranicama.
5. **Koristite determinističke provjere oko rizičnih koraka.** Provjerite trenutnu URL adresu, naslov stranice, odabrani element, cijenu, primatelja i sažetak akcije kodom prije nego što tražite od korisnika da odobri završni korak.
6. **Postavite proračune i uvjete zaustavljanja.** Ograničite broj akcija, pokušaja, kartica i minuta koje agent može koristiti. Zaustavite se kada je stanje stranice nejasno umjesto da nastavite klikati.
7. **Snimate korisne dokaze, ne sve.** Čuvajte sažetke radnji, vremenske oznake, URL-ove, opise odabranih elemenata i reference zaslona kako bi se kvarovi mogli pregledati bez pohrane nepotrebnog osjetljivog sadržaja stranice.

U primjeru Airbnba, sigurna zadana opcija je pretraživanje oglasa i izvlačenje cijena. Prijava, kontaktiranje domaćina ili završavanje rezervacije trebali bi biti zasebna radnja odobrena od korisnika.

### Primjene u stvarnom svijetu

- Rezervacija putovanja i praćenje cijena
- Usporedba cijena e-trgovine i provjere dostupnosti
- Strukturirano izvlačenje sa dinamičnih web stranica
- Testiranje i provjera korisničkog sučelja s obzirom na vid
- Praćenje web stranica i upozorenja
- Inteligentno popunjavanje obrazaca u višestupanjskim procesima

## Primjer iz stvarnog svijeta: Microsoft Project Opal

Agent koji gradite u ovoj lekciji mali je, lokalni primjerak **agenta za korištenje računala (CUA)** — programa koji pokreće preglednik na način kao osoba. Microsoft donosi ovu istu ideju u poslovne svrhe s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mogućnošću u Microsoft 365 Copilot.

Projekt Opal radi tako da opišete zadatak, a agent radi u vaše ime koristeći **korištenje računala na sigurnom Windows 365 Cloud PC-u**, djelujući preko pregledničkih aplikacija, web stranica i podataka vaše organizacije. Radi **asinhrono u pozadini**, a možete usmjeravati rad ili preuzeti kontrolu u bilo kojem trenutku. Primjeri poslova uključuju:

- Upravljanje zahtjevima za članstvo u sigurnosnim grupama
- Prikupljanje i provjere dokaza za nadzor usklađenosti
- Rukovanje IT incidentima (ažuriranje statusa tiketa, dodjela vlasnika, zatvaranje duplikata)
- Kompilacija podataka u Excelu u financijski završni dokument

Opal je koristan primjer kako izgleda **agent za korištenje računala u produkciji, kojem se može vjerovati** — i potvrđuje koncepte iz ranijih lekcija:

| Koncept u ovom tečaju | Kako ga Project Opal primjenjuje |
|------------------------|-----------------------------|
| **Čovjek u petlji** (Lekcija 06) | Opal se zaustavlja za prijavu, osjetljive podatke ili nejasne upute i nikad ne unosi lozinke niti šalje obrasce bez eksplicitne potvrde. Možete *preuzeti kontrolu* i *vratiti kontrolu* usred zadatka. |
| **Pouzdani i sigurni agenti** (Lekcije 06 & 18) | Radi u izoliranom Windows 365 Cloud PC-u, prema zadanim postavkama je samo preglednik (drugi pristupi računalu blokirani, provodi se putem Intunea), koristi *vaš* identitet pa pristupa samo onome za što ste ovlašteni, i bilježi svaku akciju radi revizije. |
| **Planiranje i metakognicija** (Lekcije 07 & 09) | Opal prvo generira plan za posao, zatim nadzire vlastito rezoniranje na svakom koraku i zaustavlja se ako otkrije sumnjive aktivnosti. |
| **Ponovno upotrebljive sposobnosti / alati** (Lekcija 04) | **Vještine** vam omogućuju da pišete upute za ponovljive zadatke (uvoz iz `.md` datoteke ili stvaranje unutar Opala) i koristite ih u različitim razgovorima. |

> **Dostupnost:** Project Opal trenutno je dostupan korisnicima u [Frontier programu ranog pristupa](https://adoption.microsoft.com/copilot/frontier-program/) s Microsoft 365 Copilot pretplatom, a vaš administrator mora izvršiti postavljanje. Budući da je eksperimentalna značajka Frontiera, mogućnosti se mogu mijenjati tijekom vremena.

## Dodatni resursi

- [Početak rada s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integracijski predložak](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use parametri djelatnika i izvlačenje sadržaja](https://docs.browser-use.com/customize/actor/all-parameters)
- [Postavljanje tečaja](../00-course-setup/README.md)

## Prethodna lekcija

[Istraživanje Microsoft Agent Frameworka](../14-microsoft-agent-framework/README.md)

## Sljedeća lekcija

[Implementacija skalabilnih agenata](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->