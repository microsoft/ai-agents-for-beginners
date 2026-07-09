# Gradnja agentov za uporabo računalnika (CUA)

Agent za uporabo računalnika lahko komunicira s spletnimi stranmi na enak način kot človek: z odpiranjem brskalnika, pregledovanjem strani in izvajanjem naslednjega najboljšega ukrepa glede na ugotovljeno. V tej lekciji boste zgradili agenta za avtomatizacijo brskalnika, ki išče po Airbnb, izvleče strukturirane podatke o namestitvah in identificira najcenejši bivanj v Stockholmu.

Lekcija združuje Browser-Use za AI-podprto navigacijo, Playwright in Chrome DevTools Protocol (CDP) za nadzor brskalnika, Azure OpenAI za vidno omogočeno sklepanje in Pydantic za strukturirano ekstrakcijo.

## Uvod

Ta lekcija bo zajemala:

- Razumevanje, kdaj so agenti za uporabo računalnika bolj primerni kot avtomatizacija samo preko API
- Združevanje Browser-Use s Playwright in CDP za zanesljivo upravljanje življenjskega cikla brskalnika
- Uporaba Azure OpenAI vida in strukturiranega Pydantic izhoda za ekstrakcijo podatkov o namestitvah s dinamičnih spletnih strani
- Odločanje, kdaj uporabiti potek dela avtomatizacije brskalnika, ki temelji na agentu, igralcu ali hibridu

## Cilji učenja

Po zaključku te lekcije boste znali:

- Konfigurirati Browser-Use z Azure OpenAI in Playwright
- Zgraditi potek avtomatizacije brskalnika, ki navigira po resnični spletni strani in obvladuje dinamične elemente uporabniškega vmesnika
- Izvleči tipizirane rezultate iz vidne vsebine strani in jih pretvoriti v nadaljnjo poslovno logiko
- Izbirati med vzorci agenta in igralca glede na to, kako predvidljivo je opravilo v brskalniku

## Primer kode

Ta lekcija vključuje en noteboksko navodilo:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Zažene seja Chroma preko CDP, poišče sezname na Airbnb za Stockholm, izvleče cene z vidom Browser-Use in vrne najcenejšo možnost kot strukturirane podatke.

## Predpogoji

- Python 3.12+
- Konfigurirana Azure OpenAI namestitev v vašem okolju
- Namestitev Chrome ali Chromium lokalno
- Namestitvene odvisnosti Playwright
- Osnovno poznavanje asinhronega Pythona

## Namestitev

Namestite pakete, uporabljene v zvezku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nastavite okoljske spremenljivke Azure OpenAI, ki jih uporablja zvezek:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Izbirno: privzeto uporabi najnovejšo različico API, če ni podano
AZURE_OPENAI_API_VERSION=...
```

## Pregled arhitekture

Zvezek prikazuje hibridni potek avtomatizacije brskalnika:

1. Chrome se zažene z omogočenim CDP, tako da si Playwright in Browser-Use delita isto sejanje brskalnika.
2. Agent Browser-Use upravlja z opravili odprte navigacije, kot so odpiranje Airbnb, zapiranje pojavnih oken in iskanje po Stockholmu.
3. Aktivna stran je pregledana z uporabo strukturirane Pydantic sheme za izvleček naslovov namestitev, nočnih cen, ocen in URL-jev.
4. Python logika primerja izvlečene sezname in poudari najcenejši rezultat.

Ta pristop ohranja prilagodljivo sklepanje na osnovi vida, v čemer je Browser-Use odličen, hkrati pa zagotavlja deterministični nadzor brskalnika, kadar ga potrebujete.

## Ključni poudarki in dobre prakse

### Kdaj uporabiti agenta v primerjavi z igralcem

| Scenarij | Uporabi agenta | Uporabi igralca |
|----------|----------------|--------------|
| Dinamične postavitve | Da, AI se lahko prilagodi spremembam strani | Ne, krhki izbirniki lahko odpovejo |
| Znana struktura | Ne, agent je počasnejši od neposrednega nadzora | Da, hitro in natančno |
| Iskanje elementov | Da, naravni jezik deluje dobro | Ne, potrebni so natančni izbirniki |
| Nadzor časa | Ne, manj predvidljivo | Da, popoln nadzor nad čakanji in ponovitvami |
| Kompleksni poteki | Da, obvladuje nepričakovane UI stanje | Ne, zahteva eksplicitno razvejanje |

### Najboljše prakse za Browser-Use

1. Začnite z agentom za raziskovanje in dinamično navigacijo.
2. Preklopite na neposredno upravljanje strani, ko interakcija postane predvidljiva.
3. Uporabljajte strukturirane modele izhoda, da so podatki, ki jih izvlečete, preverjeni in tipno varni.
4. Dodajte zamike strateško po dejanjih, ki sprožijo vidne spremembe UI.
5. Zajemajte posnetke zaslona med iteracijami, da je napake lažje odpravljati.
6. Pričakujte spremembe na spletnih straneh in oblikujte rezervne strategije za pojavna okna in premike postavitve.
7. Združite vzorce agenta in igralca, da združite fleksibilnost in natančnost.

### Prave svetovne uporabe

- Rezervacije potovanj in spremljanje cen
- Primerjava cen v e-trgovini in preverjanje razpoložljivosti
- Strukturirana ekstrakcija s dinamičnih spletnih strani
- Preverjanje uporabniškega vmesnika, ki upošteva vidne elemente
- Spremljanje spletnih strani in obveščanje
- Pametno izpolnjevanje obrazcev skozi večstopenjske tokove

## Primer iz prakse: Microsoft Project Opal

Agent, ki ga zgradite v tej lekciji, je majhna lokalna različica **agenta za uporabo računalnika (CUA)** — programa, ki upravlja brskalnik tako kot človek. Microsoft to isto idejo prinaša podjetjem z **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, zmogljivostjo v Microsoft 365 Copilot.

Z Project Opal opišete nalogo in agent dela v vašem imenu z uporabo **uporabe računalnika na varnem Windows 365 Cloud PC-ju**, ki deluje po brskalniških aplikacijah, spletnih mestih in podatkih vaše organizacije. Deluje **asinhrono v ozadju**, vi pa lahko delo usmerjate ali kadarkoli prevzamete nadzor. Primeri nalog vključujejo:

- Upravljanje zahtev za članstvo v varnostnih skupinah
- Zbiranje in preverjanje revizijskih dokazov za preglede skladnosti
- Razvrščanje IT incidentov (posodabljanje statusa tiketov, dodeljevanje lastnikov, zapiranje podvojenih)
- Združevanje podatkov Excela v finančni zaključni spisek

Opal je uporaben vzorčni primer, kakšen je **proizvodno zanesljiv agent za uporabo računalnika** — in krepi koncepte iz prejšnjih lekcij:

| Koncept v tem tečaju | Kako ga izvaja Project Opal |
|---------------------|-------------------------------|
| **Človek-v-zanki** (Lekcija 06) | Opal ustavi za vnos prijavnih podatkov, občutljivih informacij ali dvoumnih navodil in nikoli ne vnese gesel ali odda obrazcev brez izrecnega potrditve. Lahko *prevzamete nadzor* in *vrnete nadzor* med nalogo. |
| **Zanesljivi in varni agenti** (Lekcije 06 in 18) | Deluje v izoliranem Windows 365 Cloud PC-ju, privzeto je samo za brskalnik (dostop do ostalih računalnikov je blokiran, nadzorovan preko Intune), uporablja *vašo* identiteto, tako da dostopa le do pooblaščenega, in beleži vsak ukrep za revizijsko sledljivost. |
| **Načrtovanje in metakognicija** (Lekcije 07 in 09) | Opal najprej ustvari načrt za opravilo, nato nadzira lastno sklepanje na vsakem koraku in se ustavi, če zazna sumljivo dejavnost. |
| **Ponovno uporabne zmogljivosti / orodja** (Lekcija 04) | **Veščine** vam omogočajo pisanje navodil za ponovljive naloge (uvožene iz `.md` datoteke ali ustvarjene neposredno z Opal) in njihovo ponovno uporabo skozi pogovore. |

> **Razpoložljivost:** Project Opal je trenutno na voljo uporabnikom v [Frontier programu zgodnjega dostopa](https://adoption.microsoft.com/copilot/frontier-program/) z naročnino Microsoft 365 Copilot, vaš skrbnik pa mora dokončati nastavitev. Ker gre za eksperimentalno funkcijo Frontier, se zmogljivosti lahko s časom spremenijo.

## Dodatni viri

- [Začetek z Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Predloga integracije Browser-Use in Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri igralcev in ekstrakcija vsebine v Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Nastavitev tečaja](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->