# Izgradnja agenata za korištenje računala (CUA)

Agenti za korištenje računala mogu komunicirati s web stranicama na isti način kao i osoba: otvaranjem preglednika, pregledavanjem stranice i poduzimanjem sljedeće najbolje radnje na temelju onoga što vide. U ovoj lekciji, izgradit ćete agenta za automatizaciju preglednika koji pretražuje Airbnb, izvlači strukturirane podatke o ponudama i identificira najjeftiniji smještaj u Stockholmu.

Lekcija kombinira Browser-Use za navigaciju vođenu umjetnom inteligencijom, Playwright i Chrome DevTools Protocol (CDP) za upravljanje preglednikom, Azure OpenAI za rezoniranje omogućeno vidom, te Pydantic za strukturirano izvlačenje.

## Uvod

Ova lekcija će obuhvatiti:

- Razumijevanje kada su agenti za korištenje računala bolji izbor od automatizacije koja koristi samo API
- Kombiniranje Browser-Use s Playwrightom i CDP-om za pouzdano upravljanje životnim ciklusom preglednika
- Korištenje Azure OpenAI vida i strukturiranog Pydantic izlaza za izvlačenje podataka o ponudama s dinamičnih web stranica
- Odlučivanje kada koristiti agent-prvi, actor-prvi ili hibridni tijek rada automatizacije preglednika

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Konfigurirati Browser-Use s Azure OpenAI i Playwrightom
- Izgraditi tijek rada automatizacije preglednika koji pretražuje stvarnu web stranicu i upravlja dinamičkim UI elementima
- Izvući tipizirane rezultate iz vidljivog sadržaja stranice i pretvoriti ih u poslovnu logiku
- Odabrati između agenata i glumaca na temelju predvidivosti zadatka u pregledniku

## Primjer koda

Ova lekcija uključuje jedan notebook tutorijal:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Pokreće Chrome sesiju preko CDP-a, pretražuje Airbnb za ponude u Stockholmu, izvlači cijene koristeći Browser-Use vid i vraća najjeftiniju opciju kao strukturirane podatke.

## Preduvjeti

- Python 3.12+
- Konfigurirana Azure OpenAI implementacija u vašem okruženju
- Lokalno instalirani Chrome ili Chromium
- Instalirane Playwright ovisnosti
- Osnovno poznavanje async Python-a

## Postavljanje

Instalirajte pakete korištene u notebooku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Postavite Azure OpenAI varijable okruženja koje koristi notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcionalno: zadano na najnoviju verziju API-ja kada se izostavi
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Notebook demonstrira hibridni tijek rada automatizacije preglednika:

1. Chrome se pokreće s omogućenim CDP-om kako bi Playwright i Browser-Use mogli dijeliti istu sesiju preglednika.
2. Agent Browser-Use upravlja zadacima otvorene navigacije poput otvaranja Airbnba, odbacivanja iskačućih prozora i pretraživanja Stockholma.
3. Aktivna stranica se pregledava pomoću strukturirane Pydantic šeme za izvlačenje naslova ponuda, cijena po noćenju, ocjena i URL-ova.
4. Python logika uspoređuje izvučene ponude i ističe najjeftiniji rezultat.

Ovaj pristup zadržava fleksibilnost rezoniranja temeljenog na vidu koju Browser-Use dobro vrši, istovremeno dajući determinističku kontrolu nad preglednikom kada vam je potrebna.

## Ključni zaključci i najbolje prakse

### Kada koristiti agenta, a kada glumca

| Scenarij | Koristi agenta | Koristi glumca |
|----------|---------------|-------------|
| Dinamični rasporedi | Da, AI se može prilagoditi promjenama stranice | Ne, krhki selektori se mogu pokvariti |
| Poznata struktura | Ne, agent je sporiji od direktne kontrole | Da, brzo i precizno |
| Pronalaženje elemenata | Da, prirodni jezik dobro funkcionira | Ne, potrebni su točni selektori |
| Kontrola vremena | Ne, manje predvidljivo | Da, potpuna kontrola nad čekanjima i ponovnim pokušajima |
| Složeni tijekovi rada | Da, rukuje neočekivanim UI stanjima | Ne, zahtijeva eksplicitno grananje |

### Najbolje prakse Browser-Use-a

1. Počnite s agentom za istraživanje i dinamičnu navigaciju.
2. Prebacite se na direktnu kontrolu stranice kada interakcija postane predvidiva.
3. Koristite strukturirane modele izlaza kako bi izvučeni podaci bili validirani i tipizirani.
4. Dodajte odgode strateški nakon radnji koje pokreću vidljive UI promjene.
5. Snimajte zaslone dok iterirate kako bi kvarovi bili lakši za ispravljanje.
6. Očekujte promjene na web stranicama i razvijajte rezervne strategije za iskačuće prozore i promjene izgleda.
7. Kombinirajte obrasce agenta i glumca za dobivanje fleksibilnosti i preciznosti.

### Primjene u stvarnom svijetu

- Rezervacije putovanja i praćenje cijena
- Usporedba cijena u e-trgovini i provjere dostupnosti
- Strukturirano izvlačenje s dinamičnih web stranica
- Testiranje i provjera UI-a uz svijest o vidu
- Praćenje web stranica i upozorenja
- Pametno ispunjavanje obrazaca u više koraka

## Primjer iz stvarnog svijeta: Microsoft Project Opal

Agent kojeg pravite u ovoj lekciji je mala, lokalna verzija **agenta za korištenje računala (CUA)** — programa koji upravlja preglednikom na način kao što bi to radila osoba. Microsoft donosi ovu istu ideju u poduzeća s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mogućnošću u Microsoft 365 Copilot-u.

S Project Opalom opisujete zadatak, a agent radi u vaše ime koristeći **korištenje računala na sigurnom Windows 365 Cloud PC-u**, operirajući preko pregledničkih aplikacija, stranica i podataka vaše organizacije. Radi **asinhrono u pozadini**, a vi možete usmjeravati rad ili preuzeti kontrolu u bilo kojem trenutku. Primjeri poslova uključuju:

- Upravljanje zahtjevima za članstvo u sigurnosnoj grupi
- Prikupljanje i validaciju dokaza za revizijske preglede usklađenosti
- Klasificiranje IT incidenata (ažuriranje statusa tiketa, dodjela vlasnika, zatvaranje duplikata)
- Sastavljanje Excel podataka u financijsku prezentaciju

Opal je koristan primjer kako izgleda **agent za korištenje računala spreman za produkciju i s povjerenjem** — i jača koncepte iz ranijih lekcija:

| Koncept u ovom tečaju | Kako Project Opal to primjenjuje |
|------------------------|-----------------------------|
| **Čovjek u petlji** (Lekcija 06) | Opal pauzira za prijavne podatke, osjetljive podatke ili nejasne upute, i nikada ne unosi lozinke niti ne podnosi obrasce bez eksplicitne potvrde. Možete *preuzeti kontrolu* i *vratiti kontrolu* usred zadatka. |
| **Pouzdani i sigurni agenti** (Lekcije 06 i 18) | Radi u izoliranom Windows 365 Cloud PC-u, prema zadanim postavkama je isključivo preglednik (drugi pristupi računalu blokirani, provođeno putem Intune), koristi *vaš* identitet pa pristupa samo onome za što ste ovlašteni, i zapisuje svaku radnju radi revizije. |
| **Planiranje i metakognicija** (Lekcije 07 i 09) | Opal prvo generira plan za posao, zatim nadzire vlastito rezoniranje u svakom koraku i pauzira ako detektira sumnjivu aktivnost. |
| **Ponovno upotrebljive sposobnosti / alati** (Lekcija 04) | **Vještine** vam omogućuju pisanje uputa za ponovljive zadatke (uvoz iz `.md` datoteke ili kreirano s Opalom) i njihovu ponovnu upotrebu kroz razgovore. |

> **Dostupnost:** Project Opal je trenutno dostupan korisnicima u [Frontier programu ranog pristupa](https://adoption.microsoft.com/copilot/frontier-program/) s pretplatom na Microsoft 365 Copilot, a vaš administrator mora završiti postavljanje. Budući da je eksperimentalna Frontier značajka, mogućnosti se mogu mijenjati tijekom vremena.

## Dodatni resursi

- [Početak rada s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Predložak integracije Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use parametri glumca i izvlačenje sadržaja](https://docs.browser-use.com/customize/actor/all-parameters)
- [Postavljanje tečaja](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->