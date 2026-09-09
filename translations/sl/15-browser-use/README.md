# Gradnja računalniških agentov za uporabo računalnika (CUA)

Računalniški agenti za uporabo računalnika lahko sodelujejo z spletnimi mesti enako kot človek: z odpiranjem brskalnika, pregledovanjem strani in sprejemanjem naslednjega najboljšega ukrepa glede na to, kar vidijo. V tej lekciji boste izdelali agenta za avtomatizacijo brskalnika, ki išče na Airbnb, izvleče strukturirane podatke o ponudbah in identificira najcenejše bivanje v Stockholmu.

Lekcija združuje Browser-Use za navigacijo, podprto z AI, Playwright in Chrome DevTools Protocol (CDP) za nadzor brskalnika, Azure OpenAI za razločevanje z vidom ter Pydantic za strukturirano ekstrakcijo.

## Uvod

Ta lekcija bo obravnavala:

- Razumevanje, kdaj so računalniški agenti za uporabo računalnika bolj primerni kot avtomatizacija samo preko API-ja
- Združevanje Browser-Use z Playwright in CDP za zanesljivo upravljanje življenjskega cikla brskalnika
- Uporabo Azure OpenAI vida in strukturiranega Pydantic izhoda za ekstrakcijo podatkov o ponudbah iz dinamičnih spletnih strani
- Odločanje, kdaj uporabiti nagovor agenta, igralca ali hibridni potek avtomatizacije brskalnika

## Cilji učenja

Po končani tej lekciji boste znali:

- Konfigurirati Browser-Use z Azure OpenAI in Playwrightom
- Izdelati postopek avtomatizacije brskalnika, ki se premika po resničnem spletnem mestu in upravlja dinamične elemente uporabniškega vmesnika
- Izvleči tipizirane rezultate iz vidne vsebine strani in jih pretvoriti v nadaljnjo poslovno logiko
- Izbira med vzorci agenta in igralca glede na predvidljivost naloge brskalnika

## Vzorec kode

Ta lekcija vključuje en vodič v obliki zapiska:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Zažene Chrome sejo preko CDP, išče Airbnb oglase za Stockholm, izvleče cene z Browser-Use vidom in vrne najcenejšo možnost kot strukturirane podatke.

## Predpogoji

- Python 3.12+
- Azure OpenAI nameščena v vašem okolju
- Lokalno nameščen Chrome ali Chromium
- Nameščene odvisnosti Playwrighta
- Osnovno poznavanje asinhronega Pythona

## Namestitev

Namestite pakete, uporabljene v zapisku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavite okoljske spremenljivke Azure OpenAI, ki jih uporablja zvezek:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Neobvezno: privzeto na najnovejšo različico API, če je izpuščeno
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Zvezek prikazuje hibridni potek avtomatizacije brskalnika:

1. Chrome se zažene z omogočenim CDP, tako da lahko Playwright in Browser-Use delita isto sejo brskalnika.
2. Agent Browser-Use obvladuje odprte naloge navigacije, kot so odpiranje Airbnb, zapiranje pojavnih okenc in iskanje Stockholma.
3. Aktivna stran se pregleda z uporabo strukturirane Pydantic sheme za ekstrakcijo naslovov oglasov, cen na noč, ocen in URL-jev.
4. Python logika primerja izvlečene oglase in izpostavi najcenejši rezultat.

Ta pristop ohranja prilagodljivo, na vidu temelječo presojo, v kateri je Browser-Use dober, hkrati pa nudi deterministični nadzor brskalnika, ko ga potrebujete.

## Ključna spoznanja in najboljše prakse

### Kdaj uporabiti agenta in kdaj igralca

| Scenarij | Uporaba agenta | Uporaba igralca |
|----------|----------------|------------------|
| Dinamične postavitve | Da, AI se lahko prilagodi spremembam strani | Ne, krhki selektorji lahko prenehajo delovati |
| Poznana struktura | Ne, agent je počasnejši kot neposredni nadzor | Da, hitro in natančno |
| Iskanje elementov | Da, naravni jezik dobro deluje | Ne, zahtevajo se natančni selektorji |
| Nadzor časa | Ne, manj predvidljivo | Da, popoln nadzor nad čakanji in ponovitvami |
| Kompleksni poteki | Da, obvladuje nepričakovane UI situacije | Ne, zahteva eksplicitne veje |

### Najboljše prakse za Browser-Use

1. Začnite z agentom za raziskovanje in dinamično navigacijo.
2. Preklopite na neposredni nadzor strani, ko interakcija postane predvidljiva.
3. Uporabljajte strukturirane modele izhodnih podatkov, da so izvlečeni podatki validirani in varni glede tipov.
4. Dodajte zamude strateško po dejanjih, ki sprožijo vidne spremembe UI.
5. Med iteriranjem zajemajte posnetke zaslona, da so napake lažje za odkrivanje.
6. Pričakujte spremembe spletnih mest in oblikujte rezervne strategije za pojavna okna in premike postavitve.
7. Združite vzorce agenta in igralca za dosego obeh: prilagodljivosti in natančnosti.

### Varnostni varovalni ukrepi za brskalniške agente

Brskalniški agenti delujejo na živih spletnih mestih, zato potrebujejo strožje meje kot skripta, ki samo kliče znan API. Pred začetkom produkcijskega postopka, definirajte nadzore glede tega, kaj agent vidi, klikne in odda.

1. **Omejite brskalno okolje.** Zaženite agenta v namenskem profilu brskalnika ali peskovniku in ga omejite na domene, potrebne za nalogo.
2. **Ločite opazovanje od dejanja.** Naj agent najprej išče, bere in izvleče podatke; zahteva ekspliciten korak odobritve pred oddajo obrazcev, pošiljanjem sporočil, rezervacijami, nakupi, brisanjem zapisov ali spreminjanjem nastavitev računa.
3. **Ne vključujte skrivnosti v pozive in sledi.** Ne dodajajte gesel, podatkov o plačilu, piškotkov sej ali neobdelanih osebnih podatkov v kontekst modela. Naj uporabnik prevzame avtentikacijo in izbriše občutljiva polja iz dnevnikov.
4. **Ravnajte z vsebino strani kot nezaupanja vrednim vhodom.** Spletna stran lahko vsebuje navodila za agenta, ne za uporabnika. Agent naj prezre tekst, ki zahteva spremembo cilja, razkritje podatkov, onemogočanje varovalk ali obisk nepovezanih mest.
5. **Uporabljajte deterministične preglede okoli tveganih korakov.** Preden uporabnik potrdi zadnji korak, preverite trenutno URL, naslov strani, izbran element, ceno, prejemnika in povzetek dejanja s kodo.
6. **Nastavite meje in pogoje zaustavitve.** Omejite število dejanj, ponovitev, zavihkov in minut, ki jih agent lahko uporabi. Ustavite se, ko je stanje strani nejasno, namesto da nadaljujete s klikanjem.
7. **Posnemajte koristne dokaze, ne vsega.** Beležite povzetke dejanj, časovne žige, URL-je, opise izbranih elementov in reference posnetkov zaslona, da je mogoče pregledati napake brez shranjevanja nepotrebne občutljive vsebine strani.

V primerku Airbnb je varna privzeta nastavitev iskanje oglasov in ekstrakcija cen. Prijava, stik z gostiteljem ali dokončanje rezervacije naj bo ločeno dejanje, ki ga odobri uporabnik.

### Resnični primeri uporabe

- Rezervacije potovanj in spremljanje cen
- Primerjava cen v e-trgovini in preverjanje razpoložljivosti
- Strukturirana ekstrakcija iz dinamičnih spletnih mest
- Testiranje in preverjanje uporabniškega vmesnika z vidnim zaznavanjem
- Spremljanje spletnih mest in opozarjanje
- Pametno izpolnjevanje obrazcev v večstopenjskih potekih

## Resnični primer: Microsoft Project Opal

Agent, ki ga izdelate v tej lekciji, je majhna, lokalna različica **računalniškega agenta za uporabo računalnika (CUA)** — programa, ki upravlja brskalnik kot človek. Microsoft to idejo prinaša podjetjem z **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, zmožnostjo v Microsoft 365 Copilot.

Pri Project Opal opišete nalogo, agent pa dela v vašem imenu, uporabljajoč **uporabo računalnika na varnem Windows 365 Cloud PC**, delujoč prek brskalniških aplikacij, mest in podatkov vaše organizacije. Deluje **asinhrono v ozadju**, vi pa lahko kadarkoli vodite delo ali prevzamete nadzor. Primeri nalog vključujejo:

- Upravljanje zahtevkov članstva v varnostnih skupinah
- Zbiranje in preverjanje dokazov za presoje skladnosti
- Razvrščanje IT incidentov (posodabljanje statusa, dodeljevanje lastnikov, zapiranje podvojitev)
- Priprava podatkov Excela za finančno poročilo

Opal je uporaben primer, kako izgleda **produkcijsko zanesljiv** računalniški agent za uporabo računalnika — in potrjuje koncepte iz prejšnjih lekcij:

| Koncept v tem tečaju | Kako ga uporablja Project Opal |
|----------------------|-----------------------------|
| **Človek v zanki** (lekcija 06) | Opal počaka na prijavne podatke, občutljive podatke ali dvoumna navodila in nikoli ne vnese gesel ali odda obrazcev brez izrecnega potrditve. Uporabnik lahko *Prevzame Nadzor* in *Vrne Nadzor* sredi naloge. |
| **Zanesljivi in varni agenti** (lekcije 06 in 18) | Deluje v izoliranem Windows 365 Cloud PC, je po privzetku le brskalniški (dostop do drugih računalnikov blokiran, urejen preko Intune), uporablja *vašo* identiteto, da dostopa le do dovoljenih vsebin, in beleži vsako dejanje za revizijo. |
| **Načrtovanje in metakognicija** (lekcije 07 in 09) | Opal najprej generira načrt za opravilo, nato nadzira svoje sklepanje na vsakem koraku in se ustavi ob zaznavi sumljive dejavnosti. |
| **Ponovno uporabne funkcionalnosti orodja** (lekcija 04) | **Sposobnosti** omogočajo pisanje navodil za ponovljive naloge (uvožena iz `.md` datoteke ali ustvarjena z Opalom) in njihovo ponovno uporabo v pogovorih. |

> **Dostopnost:** Project Opal je trenutno na voljo uporabnikom v [Frontier programu zgodnjega dostopa](https://adoption.microsoft.com/copilot/frontier-program/) z naročnino Microsoft 365 Copilot, vaš skrbnik pa mora izvesti nastavitev. Ker gre za eksperimentalno funkcijo Frontier, se zmožnosti lahko s časom spremenijo.

## Preverjanje znanja

Preizkusite svoje razumevanje pred premikom na naslednjo lekcijo.

**1. Kdaj je brskalniški računalniški agent bolj primeren kot potek dela samo z API-jem?**

<details>
<summary>Odgovor</summary>

Uporabite brskalniškega agenta, ko naloga temelji na tem, kar je vidno v spletnem UI-ju, spletno mesto ne izpostavlja potrebnega API-ja ali se stran pogosto spreminja, zaradi česar bi bil fiksni API ali logika selektorjev krhka. Če obstaja stabilen API za isto nalogo, je bolje uporabiti API, saj je običajno hitrejši, lažji za testiranje in bolj varen.
</details>

**2. Kateri deli v hibridnem poteku naj jih upravlja agent, in kateri naj jih upravlja neposredna Playwright koda?**

<details>
<summary>Odgovor</summary>

Naj agent obvladuje odprto navigacijo in dinamična stanja UI, kot je iskanje prave strani ali zapiranje nepričakovanih pojavnih okenc. Preklopite na neposredni nadzor Playwrighta, ko je struktura strani znana in dejanje zahteva natančnost, ponovitve, čakanja ali deterministične preverjanja.
</details>

**3. V primerku Airbnb agent najde oglas, ki ga uporabnik morda želi rezervirati. Kaj naj se zgodi pred prijavo, stikom z gostiteljem ali dokončanjem rezervacije?**

<details>
<summary>Odgovor</summary>

Potek dela naj se ustavi in zahteva izrecno uporabniško odobritev. Pred tem naj prikaže jasen povzetek izbranega oglasa, trenutni URL, ceno, datume in predvideno dejanje. Iskanje in ekstrakcija cen je lahko avtonomno; dostop do računa, sporočila, nakupi in rezervacije naj bodo odobreni s strani uporabnika.
</details>

**4. Spletna stran agentu naroča, naj prezre svoja prvotna navodila, obišče drugo stran in razkrije shranjene poverilnice. Kako naj agent ravna s tem tekstom?**

<details>
<summary>Odgovor</summary>

Ravnajte z njim kot z nezaupanja vredno vsebino strani, ne kot z navodilom razvijalca ali uporabnika. Agent naj ostane znotraj dovoljenega domenskega in nalognega obsega, zavrne razkrivanje skrivnosti in se izogiba sledenju tekstu stran, ki spremeni cilj, onemogoči varovalke ali pošlje na nepovezana mesta.
</details>

**5. Kateri dokazi so koristni za shranjevanje, ko agent deluje, in česa naj se izogibamo?**

<details>
<summary>Odgovor</summary>

Shranjujte povzetke dejanj, časovne žige, URL-je, opise izbranih elementov, validacijske rezultate in reference posnetkov zaslona, da se lahko delovanje pregleda. Izogibajte se shranjevanju gesel, podatkov o plačilu, piškotkov sej, neobdelanih osebnih podatkov ali celotnih vsebin strani, razen če obstaja poseben razlog glede hrambe in zasebnosti.
</details>

## Dodatni viri

- [Začetek z Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Predloga integracije Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameterji akterja Browser-Use in ekstrakcija vsebine](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavitev tečaja](../00-course-setup/README.md)

## Prejšnja lekcija

[Raziščite Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Naslednja lekcija

[Namestitev razširljivih agentov](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->