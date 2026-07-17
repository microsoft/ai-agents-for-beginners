# Gradnja agentov za uporabo računalnika (CUA)

Agenti za uporabo računalnika lahko sodelujejo z spletnimi mesti na enak način kot oseba: z odpiranjem brskalnika, pregledom strani in izvajanjem naslednjega najboljšega dejanja glede na to, kar vidijo. V tej lekciji boste ustvarili avtomatiziranega agenta brskalnika, ki išče na Airbnb, izvleče strukturirane podatke o ponudbah in določi najcenejše bivanje v Stockholmu.

Lekcija združuje Browser-Use za vodeno navigacijo z umetno inteligenco, Playwright in Chrome DevTools Protocol (CDP) za nadzor brskalnika, Azure OpenAI za vidno omogočeno sklepanje in Pydantic za strukturirano ekstrakcijo.

## Uvod

Ta lekcija bo zajemala:

- Razumevanje, kdaj so agenti za uporabo računalnika bolj primerni od avtomatizacije samo z API-jem
- Združevanje Browser-Use s Playwrightom in CDP za zanesljivo upravljanje življenjskega cikla brskalnika
- Uporaba Azure OpenAI vida in strukturiranega Pydantic izhoda za ekstrakcijo podatkov o ponudbah s dinamičnih spletnih strani
- Odločanje, kdaj uporabiti delovni tok avtomatizacije brskalnika, ki je usmerjen na agenta, igralca ali hibrid

## Cilji učenja

Po zaključku te lekcije boste znali:

- Konfigurirati Browser-Use z Azure OpenAI in Playwrightom
- Ustvariti avtomatiziran delovni tok brskalnika, ki brskа po pravem spletnem mestu in obvladuje dinamične elemente UI
- Izvleči tipizirane rezultate iz vidne vsebine strani in jih pretvoriti v poslovno logiko
- Izbrati med vzorci agenta in igralca glede na to, kako predvidljivo je opravilo v brskalniku

## Primer kode

Ta lekcija vključuje en vodič v zvezku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Zažene sejo Chrome prek CDP, išče ponudbe na Airbnb za Stockholm, izvleče cene z Browser-Use vidom in vrne najcenejšo možnost kot strukturirane podatke.

## Predpogoji

- Python 3.12+
- Azure OpenAI nameščena in konfigurirana v vašem okolju
- Lokalno nameščen Chrome ali Chromium
- Nameščene odvisnosti Playwrighta
- Osnovno poznavanje asinhronega Python-a

## Namestitev

Namestite pakete, uporabljene v zvezku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavite okoljske spremenljivke Azure OpenAI, ki jih zvezek uporablja:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Neobvezno: privzeto uporabi najnovejšo različico API, če je izpuščeno
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Zvezek prikazuje hibridni delovni tok avtomatizacije brskalnika:

1. Chrome se zažene z omogočenim CDP, tako da sta Playwright in Browser-Use v isti seji brskalnika.
2. Agent Browser-Use upravlja odprta opravila navigacije, kot so odpiranje Airbnb, zapiranje pojavnih oken in iskanje Stockholma.
3. Trenutna stran se pregleda s strukturirano shemo Pydantic za ekstrakcijo naslovov ponudb, nočnih cen, ocen in URL-jev.
4. Python logika primerja izvlečene ponudbe in označi najcenejši rezultat.

Ta pristop ohranja prilagodljivo, vidno podprto sklepanje, ki ga Browser-Use odlično izvaja, hkrati pa vam daje determinističen nadzor brskalnika, kadar ga potrebujete.

## Ključne ugotovitve in dobre prakse

### Kdaj uporabiti agenta v primerjavi z igralcem

| Scenarij | Uporabi agenta | Uporabi igralca |
|----------|-----------|-----------|
| Dinamični postavitve | Da, UI se lahko prilagodi spremembam strani | Ne, krhki selektorji se lahko zlomijo |
| Znana struktura | Ne, agent je počasnejši od neposrednega nadzora | Da, hiter in natančen |
| Iskanje elementov | Da, naravni jezik deluje dobro | Ne, potrebni so točni selektorji |
| Nadzor časov | Ne, manj predvidljivo | Da, popoln nadzor nad čakanji in poskusi |
| Kompleksni delovni tokovi | Da, obvladuje nepričakovane UI stanje | Ne, zahteva eksplicitno vejitev |

### Dobre prakse Browser-Use

1. Začnite z agentom za raziskovanje in dinamično navigacijo.
2. Preklopite na neposredni nadzor strani, ko postane interakcija predvidljiva.
3. Uporabite strukturirane izhodne modele, tako da so izvlečeni podatki preverjeni in varni glede tipa.
4. Dodajte zamude strateško po dejanjih, ki sprožijo vidne spremembe UI.
5. Posnemajte zaslonske slike med iteracijami, da je lažje odpraviti napake.
6. Pričakujte spremembe spletnih mest in zasnujte rezervne strategije za pojavna okna in premike postavitve.
7. Združite vzorce agenta in igralca, da pridobite tako prilagodljivost kot natančnost.

### Varnostna zaščita za browser agente

Agent brskalnika deluje na živih spletnih mestih, zato potrebuje strožje omejitve kot skripta, ki kliče le znan API. Preden preidete iz primere zvezka v pravi delovni tok, opredelite nadzore glede tega, kaj agent lahko vidi, klikne in pošlje.

1. **Omejite okolje brskanja.** Zaženite agenta v namenskem profilu brskalnika ali peskovniku in ga omejite na domene, potrebne za opravilo.
2. **Ločite opazovanje od dejanja.** Naj agent najprej išče, bere in izvleče podatke; zahtevajte eksplicitno odobritev, preden pošilja obrazce, sporočila, rezervacije, nakupuje, briše zapise ali spreminja nastavitve računa.
3. **Skrivnosti naj bodo zunaj pozivov in sledi.** Ne dodajajte gesel, podatkov o plačilu, piškotkov seje ali surovih osebnih podatkov v kontekst modela. Naj uporabnik prevzame avtentikacijo in cenzurira občutljiva polja iz dnevnikov.
4. **Obravnavajte vsebino strani kot nezanesljiv vhod.** Spletna stran lahko vsebuje navodila, namenjena agentu, ne uporabniku. Agent naj prezre besedilo strani, ki ga poziva k spremembi cilja, razkritju podatkov, onemogočitvi varovalk ali obisku nepovezanih strani.
5. **Uporabljajte deterministične preveritve pri tveganih korakih.** Preverite trenutni URL, naslov strani, izbrani element, ceno, prejemnika in povzetek dejanj s pomočjo kode, preden uporabniku zahtevate potrditev končnega koraka.
6. **Določite proračune in pogoje za zaustavitev.** Omejite število dejanj, ponovitev, zavihkov in minut, ki jih agent lahko uporabi. Ustavite se, ko je stanje strani nejasno, namesto da nadaljujete s klikanjem.
7. **Zapisujte koristne dokaze, ne vsega.** Shranjujte povzetke dejanj, časovne žige, URL-je, opise izbranih elementov in reference posnetkov zaslona, da je mogoče napake pregledati brez shranjevanja nepotrebne občutljive vsebine strani.

V Airbnb vzorcu je varna privzeta nastavitev iskanje ponudb in izvlek cen. Prijava, stik z gostiteljem ali dokončanje rezervacije naj bo ločeno dejanje, potrjeno s strani uporabnika.

### Praktične uporabe v resničnem svetu

- Rezervacija potovanj in spremljanje cen
- Primerjava cen in preverjanje razpoložljivosti v e-trgovini
- Strukturirana ekstrakcija s dinamičnih spletnih mest
- Preizkušanje in preverjanje UI z uporabo vida
- Spremljanje spletnih mest in obveščanje
- Inteligentno izpolnjevanje obrazcev v večkorakih

## Primer iz resničnega sveta: Microsoft Project Opal

Agent, ki ga zgradite v tej lekciji, je majhna, lokalna različica **agenta za uporabo računalnika (CUA)** — programa, ki upravlja brskalnik kot oseba. Microsoft to isto idejo uvaja v podjetja s **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, zmogljivostjo v Microsoft 365 Copilot.

Z Project Opal opisujete opravilo, agent pa dela v vašem imenu z uporabo **uporabe računalnika na varnem Windows 365 Cloud PC**, ki deluje preko brskalniških aplikacij, spletnih mest in podatkov vaše organizacije. Deluje **asinhrono v ozadju** in delo lahko kadar koli usmerjate ali prevzamete nadzor. Primeri opravil vključujejo:

- Upravljanje zahtevkov za članstvo v varnostnih skupinah
- Zbiranje in preverjanje dokazov za revizijske preglede skladnosti
- Reševanje IT incidentov (posodabljanje statusa kartice, dodeljevanje lastnikov, zapiranje podvojitev)
- Sestavljanje Excel podatkov v finančno poročilo

Opal je koristna referenca, kako izgleda **proizvodno zanesljiv in zaupanja vreden** agent za uporabo računalnika — in utrjuje koncepte iz prejšnjih lekcij:

| Koncept v tem tečaju | Kako ga Project Opal uporablja |
|------------------------|-----------------------------|
| **Človek v zanki** (Lekcija 06) | Opal počaka na prijavne podatke, občutljive informacije ali nejasna navodila in nikoli ne vnaša gesel ali ne pošilja obrazcev brez izrecnega potrditve. Lahko *prevzamete nadzor* in ga *vrnete* v poljubnem trenutku med opravili. |
| **Zanesljivi in varni agenti** (Lekcije 06 in 18) | Deluje v izoliranem Windows 365 Cloud PC, privzeto le brskalnik (dostop do drugih računalnikov blokiran, izvršeno preko Intune), uporablja *vašo* identiteto, da dostopa le do avtenticiranih podatkov in beleži vsako dejanje za revizijo. |
| **Načrtovanje in metakognicija** (Lekcije 07 in 09) | Opal najprej ustvari načrt za opravilo, nato nadzoruje lastno sklepanje v vsakem koraku in se ustavi, če zazna sumljivo aktivnost. |
| **Večkratna uporaba zmogljivosti/opravil** (Lekcija 04) | **Veščine** omogočajo pisanje navodil za ponovljiva opravila (uvožena iz `.md` datoteke ali napisana z Opalom) in njihovo ponovno uporabo v pogovorih. |

> **Razpoložljivost:** Project Opal je trenutno na voljo uporabnikom v [Frontier zgodnjem dostopu](https://adoption.microsoft.com/copilot/frontier-program/) z naročnino Microsoft 365 Copilot, administrator pa mora dokončati nastavitev. Ker gre za eksperimentalno funkcijo Frontier, se zmogljivosti lahko s časom spremenijo.

## Dodatni viri

- [Začnite s Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Predloga za integracijo Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri igralca Browser-Use in ekstrakcija vsebine](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavitev tečaja](../00-course-setup/README.md)

## Prejšnja lekcija

[Raziskovanje Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Naslednja lekcija

[Implementacija skalabilnih agentov](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->