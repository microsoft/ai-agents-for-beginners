# Izrada agenata za korištenje računala (CUA)

Agenti za korištenje računala mogu komunicirati s web stranicama na isti način kao i osoba: otvaranjem preglednika, pregledavanjem stranice i poduzimanjem najboljeg sljedećeg koraka prema onome što vide. U ovoj lekciji izradit ćete agenta za automatizaciju preglednika koji pretražuje Airbnb, izvlači strukturirane podatke o ponudama i identificira najjeftiniji boravak u Stockholmu.

Lekcija kombinira Browser-Use za navigaciju vođenu AI, Playwright i Chrome DevTools Protocol (CDP) za kontrolu preglednika, Azure OpenAI za zaključivanje omogućeno vizijom i Pydantic za strukturirano izvlačenje podataka.

## Uvod

Ova lekcija pokriva:

- Razumijevanje kada su agenti za korištenje računala bolji od isključive automatizacije putem API-ja
- Kombiniranje Browser-Use s Playwrightom i CDP-om za pouzdano upravljanje životnim ciklusom preglednika
- Korištenje Azure OpenAI vizije i strukturiranog Pydantic izlaza za izvlačenje podataka o ponudama s dinamičnih web stranica
- Odlučivanje kada koristiti pristup vođen agentom, izvođačem ili hibridni tijek rada automatizacije preglednika

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete kako:

- Konfigurirati Browser-Use s Azure OpenAI i Playwrightom
- Izraditi tijek rada automatizacije preglednika koji navigira stvarnom web stranicom i upravlja dinamičkim UI elementima
- Izvući tipizirane rezultate iz vidljivog sadržaja stranice i pretvoriti ih u poslovnu logiku
- Izabrati između obrazaca agenta i izvođača na temelju predvidljivosti zadatka u pregledniku

## Primjer koda

Ova lekcija uključuje jedan tutorial u notebooku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Pokreće Chrome sesiju preko CDP-a, pretražuje Airbnb za ponude u Stockholmu, izvlači cijene uz pomoć Browser-Use vizije i vraća najjeftiniju opciju kao strukturirane podatke.

## Preduvjeti

- Python 3.12+
- Konfigurirana Azure OpenAI implementacija u vašem okruženju
- Chrome ili Chromium instaliran lokalno
- Instalirane Playwright ovisnosti
- Osnovno poznavanje async Pythona

## Postavljanje

Instalirajte pakete koje koristi notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Postavite Azure OpenAI varijable okruženja koje koristi notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcionalno: ako se izostavi, koristi se zadnja verzija API-ja
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Notebook prikazuje hibridni tijek automatizacije preglednika:

1. Chrome se pokreće s omogućenim CDP-om kako bi Playwright i Browser-Use mogli dijeliti istu sesiju preglednika.
2. Agent Browser-Use upravlja otvorenim zadacima navigacije kao što su otvaranje Airbnb-a, zatvaranje iskačućih prozora i pretraživanje Stockholma.
3. Aktivna stranica se pregledava uz pomoć strukturirane Pydantic sheme za izvlačenje naslova ponuda, noćnih cijena, ocjena i URL-ova.
4. Python logika uspoređuje izdvojene ponude i ističe najjeftiniji rezultat.

Ovaj pristup zadržava fleksibilno zaključivanje temeljeno na viziji po kojem je Browser-Use dobar, a istovremeno pruža determinističku kontrolu preglednika kad je to potrebno.

## Glavne spoznaje i najbolje prakse

### Kada koristiti agenta, a kada izvođača

| Scenarij | Koristite agenta | Koristite izvođača |
|----------|-----------------|------------------|
| Dinamični rasporedi | Da, AI se može prilagoditi promjenama stranice | Ne, lomljivi selektori mogu zakazati |
| Poznata struktura | Ne, agent je sporiji od direktne kontrole | Da, brz i precizan |
| Pronalaženje elemenata | Da, prirodni jezik dobro funkcionira | Ne, potrebni su točni selektori |
| Kontrola vremena | Ne, manje je predvidivo | Da, potpuna kontrola čekanja i ponavljanja |
| Kompleksni tijekovi rada | Da, rukuje neočekivanim stanjima UI | Ne, zahtijeva eksplicitno grananje |

### Najbolje prakse Browser-Use-a

1. Počnite s agentom za istraživanje i dinamičku navigaciju.
2. Prebacite se na izravnu kontrolu stranice kada interakcija postane predvidiva.
3. Koristite strukturirane modele izlaza da bi izdvojeni podaci bili validirani i tipizirani.
4. Strategijski dodajte odgode nakon radnji koje pokreću vidljive promjene sučelja.
5. Snimajte zaslonske slike tijekom iteracija kako bi otklanjanje pogrešaka bilo lakše.
6. Očekujte promjene web stranica i dizajnirajte rezervne strategije za iskačuće prozore i pomake u rasporedu.
7. Kombinirajte obrasce agenta i izvođača za dobivanje fleksibilnosti i preciznosti.

### Sigurnosne mjere za agente preglednika

Agenti preglednika rade na živim web stranicama, stoga im trebaju stroža ograničenja nego skripti koje samo pozivaju poznati API. Prije prelaska s demonstracije u notebooku na stvarni tijek rada, definirajte kontrole oko onoga što agent može vidjeti, kliknuti i poslati.

1. **Ograničite pregledničko okruženje.** Pokrenite agenta u namjenskom profilu preglednika ili sandboxu i ograničite domene potrebne zadatku.
2. **Odvojite promatranje od akcije.** Dopustite agentu da prvo pretražuje, čita i izvlači podatke; zahtijevajte eksplicitnu potvrdu prije slanja obrazaca, slanja poruka, rezervacija, kupnji, brisanja zapisa ili promjene postavki računa.
3. **Čuvajte tajne izvan upita i zapisa.** Nemojte stavljati lozinke, podatke o plaćanju, kolačiće sesije ili sirove osobne podatke u kontekst modela. Neka korisnik preuzme autentikaciju i ukloni osjetljiva polja iz zapisa.
4. **Tretirajte sadržaj stranice kao nepouzdani unos.** Web stranica može sadržavati upute namijenjene agentu, a ne korisniku. Agent bi trebao ignorirati tekst koji traži da promijeni cilj, otkrije podatke, onemogući mjere zaštite ili posjeti nesrodne stranice.
5. **Koristite determinističke provjere oko rizičnih koraka.** Provjerite trenutni URL, naslov stranice, odabrani element, cijenu, primatelja i sažetak radnje pomoću koda prije traženja od korisnika da odobri završni korak.
6. **Postavite limite i uvjete zaustavljanja.** Ograničite broj radnji, ponavljanja, tabova i minuta koje agent može koristiti. Zaustavite se kada je stanje stranice nejasno umjesto da nastavite klikati.
7. **Bilježite korisne dokaze, ne sve.** Čuvajte sažetke radnji, vremenske oznake, URL-ove, opise odabranih elemenata i reference na snimke zaslona kako bi se pogreške mogle pregledati bez pohrane nepotrebnog osjetljivog sadržaja stranice.

U Airbnb primjeru, siguran zadani izbor je pretraživanje ponuda i izvlačenje cijena. Prijava, kontaktiranje domaćina ili dovršavanje rezervacije trebaju biti odvojene radnje koje potvrđuje korisnik.

### Primjena u stvarnom svijetu

- Rezervacija putovanja i praćenje cijena
- Usporedba cijena i provjera dostupnosti u e-trgovini
- Strukturirano izvlačenje s dinamičnih web stranica
- Testiranje i verifikacija korisničkog sučelja osviještenog o vidu
- Praćenje web stranica i slanje upozorenja
- Inteligentno popunjavanje obrazaca kroz višestepene tijekove

## Stvarni primjer: Microsoft Project Opal

Agent koji izrađujete u ovoj lekciji je mala, lokalna verzija **agenta za korištenje računala (CUA)** — programa koji upravlja preglednikom kao osoba. Microsoft ovu istu ideju donosi u poduzeća s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mogućnošću u Microsoft 365 Copilot.

S Project Opalom opisujete zadatak, a agent radi za vas koristeći **korištenje računala na sigurnom Windows 365 Cloud PC-u**, radeći preko pregledničkih aplikacija, stranica i podataka vaše organizacije. Radi **asinkrono u pozadini**, a vi možete voditi rad ili preuzeti kontrolu u bilo kojem trenutku. Primjeri poslova uključuju:

- Upravljanje zahtjevima za članstvo u sigurnosnim grupama
- Prikupljanje i validaciju dokaza za reviziju usklađenosti
- Rješavanje IT incidenata (ažuriranje statusa ticket-a, dodjeljivanje vlasnika, zatvaranje duplikata)
- Sastavljanje Excel podataka u financijski izvještaj

Opal je koristan primjer kako izgleda **produkcijski, pouzdan** agent za korištenje računala — i potvrđuje koncepte iz ranijih lekcija:

| Koncept u ovom tečaju | Kako ga Project Opal primjenjuje |
|------------------------|-----------------------------|
| **Čovjek u petlji** (Lekcija 06) | Opal se zaustavlja za prijavu, osjetljive podatke ili dvosmislene upute i nikada ne unosi lozinke niti šalje obrasce bez eksplicitne potvrde. Možete *preuzeti kontrolu* i *vratiti kontrolu* usred zadatka. |
| **Pouzdani i sigurni agenti** (Lekcije 06 & 18) | Radi u izoliranom Windows 365 Cloud PC-u, po zadanim postavkama samo preglednik (drugi pristupi računalu blokirani, provedeno putem Intunea), koristi *vaš* identitet tako da pristupa samo onome za što ste ovlašteni i bilježi svaku akciju radi revizije. |
| **Planiranje i metakognicija** (Lekcije 07 & 09) | Opal prvo generira plan za posao, zatim nadzire vlastito zaključivanje u svakom koraku i zaustavlja se ako detektira sumnjive aktivnosti. |
| **Ponovno upotrebljive sposobnosti / alati** (Lekcija 04) | **Vještine** vam omogućuju pisanje uputa za ponovljive zadatke (uvozeni iz `.md` datoteke ili izrađeni u Opalu) i njihovu ponovnu upotrebu kroz razgovore. |

> **Dostupnost:** Project Opal je trenutno dostupan korisnicima u [Frontier programu ranog pristupa](https://adoption.microsoft.com/copilot/frontier-program/) uz pretplatu na Microsoft 365 Copilot, a vaš administrator mora završiti postavljanje. Budući da je eksperimentalna Frontier značajka, mogućnosti se mogu mijenjati s vremenom.

## Provjera znanja

Provjerite svoje razumijevanje prije prelaska na sljedeću lekciju.

**1. Kada je agent za korištenje preglednika bolji izbor od tijeka rada koji koristi samo API?**

<details>
<summary>Odgovor</summary>

Koristite agenta preglednika kad zadatak ovisi o onome što je vidljivo u web korisničkom sučelju, ako stranica ne izlaže potreban API ili ako se stranica često mijenja toliko da bi fiksna API ili selektorska logika bila nestabilna. Ako postoji stabilan API za isti zadatak, preferirajte API jer je obično brži, lakši za testiranje i sigurniji.
</details>

**2. Koje dijelove tijeka rada u hibridnom modelu treba upravljati agent, a koje izravni Playwright kod?**

<details>
<summary>Odgovor</summary>

Dopustite agentu da upravlja otvorenom navigacijom i dinamičkim UI stanjima, kao što je pronalazak prave stranice ili zatvaranje neočekivanih iskačućih prozora. Prebacite se na izravnu kontrolu Playwrighta kada je struktura stranice poznata i akcija zahtijeva preciznost, ponavljanja, čekanja ili determinističku validaciju.
</details>

**3. Airbnb primjer pronalazi ponudu koju korisnik možda želi rezervirati. Što treba dogoditi prije nego što tijek rada izvrši prijavu, kontaktira domaćina ili dovrši rezervaciju?**

<details>
<summary>Odgovor</summary>

Tijek rada treba stati i zatražiti eksplicitnu korisničku suglasnost. Prije zahtjeva treba prikazati jasan sažetak odabrane ponude, trenutnog URL-a, cijene, datuma i namjeravane radnje. Pretraživanje i izvlačenje cijena može biti autonomno; pristup računu, poruke, kupnje i rezervacije trebaju biti odobreni od strane korisnika.
</details>

**4. Web stranica agentu nalaže da ignorira svoje izvorne upute, posjeti drugu stranicu i otkrije spremljene vjerodajnice. Kako bi agent trebao tretirati taj tekst?**

<details>
<summary>Odgovor</summary>

Tretirajte ga kao nepouzdani sadržaj stranice, a ne kao uputu programera ili korisnika. Agent bi trebao ostati unutar dopuštene domene i opsega zadatka, odbiti otkrivanje tajni i izbjegavati slijediti tekst koji mijenja cilj, onemogućuje zaštitne mjere ili ga šalje na nesrodne stranice.
</details>

**5. Koji su korisni dokazi za pohranu tijekom rada agenta preglednika, a što treba izbjegavati?**

<details>
<summary>Odgovor</summary>

Čuvajte sažetke radnji, vremenske oznake, URL-ove, opise odabranih elemenata, rezultate validacije i reference na snimke zaslona kako bi se rad mogao pregledati. Izbjegavajte pohranu lozinki, podataka o plaćanju, kolačića sesije, sirovih osobnih podataka ili punog sadržaja stranice osim ako postoji specifičan razlog za zadržavanje i privatnost.
</details>

## Dodatni resursi

- [Početak rada s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Predložak integracije Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri izvođača i izvlačenje sadržaja u Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
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