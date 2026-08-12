# Kompiuterio naudojimo agentų (CUA) kūrimas

Kompiuterio naudojimo agentai gali sąveikauti su svetainėmis taip pat kaip žmogus: atverdami naršyklę, tikrindami puslapį ir imdamiesi geriausio kito veiksmo pagal tai, ką mato. Šioje pamokoje jūs sukursite naršyklės automatikos agentą, kuris ieško Airbnb, ištraukia struktūrizuotus skelbimų duomenis ir nustato pigiausią nakvynę Stokholme.

Pamoka apjungia Browser-Use AI valdomą navigaciją, Playwright ir Chrome DevTools protokolą (CDP) naršyklės valdymui, Azure OpenAI regos pagrindu veikiančiai logikai ir Pydantic struktūrizuotam duomenų išgavimui.

## Įvadas

Šioje pamokoje bus aptarta:

- Kada kompiuterio naudojimo agentai yra tinkamesni nei tik API automatizavimas
- Kaip apjungti Browser-Use su Playwright ir CDP patikimam naršyklės gyvenimo ciklo valdymui
- Kaip naudoti Azure OpenAI regą ir struktūrizuotą Pydantic išvestį norint išgauti sąrašų duomenis iš dinamiškų tinklalapių
- Kada pasirinkti agento pirmumo, aktoriaus pirmumo ar mišrią naršyklės automatikos darbo eigą

## Mokymosi tikslai

Baigę šią pamoką žinosite, kaip:

- Konfigūruoti Browser-Use su Azure OpenAI ir Playwright
- Sukurti naršyklės automatikos darbo eigą, kuri naršo realią svetainę ir tvarko dinamiškus UI elementus
- Išgauti tipizuotus rezultatus iš matomo puslapio turinio ir paversti juos verslo logika
- Pasirinkti tarp agento ir aktoriaus modelių, priklausomai nuo naršyklės užduoties nuspėjamumo

## Kodo pavyzdys

Ši pamoka apima vieną užrašų knygelės (notebook) pamoką:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Paleidžia Chrome sesiją per CDP, ieško Airbnb Stokholmo skelbimų, ištraukia kainas su Browser-Use rega ir grąžina pigiausią variantą kaip struktūrizuotą duomenį.

## Priešistorė

- Python 3.12+
- Azure OpenAI diegimas sukonfigūruotas jūsų aplinkoje
- Vietoje įdiegta Chrome arba Chromium naršyklė
- Įdiegti Playwright priklausomybės
- Pagrindinis susipažinimas su asinchroniniu Python

## Nustatymas

Įdiekite užrašų knygelėje naudojamas bibliotekas:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nustatykite Azure OpenAI aplinkos kintamuosius, kuriuos naudoja užrašų knygelė:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Pasirinktinai: praleidus, naudojama naujausia API versija
AZURE_OPENAI_API_VERSION=...
```

## Architektūros apžvalga

Užrašų knygelė demonstruoja hibridinę naršyklės automatikos darbo eigą:

1. Chrome paleidžiamas su įjungtu CDP, todėl tiek Playwright, tiek Browser-Use gali naudoti tą pačią naršyklės sesiją.
2. Browser-Use agentas atlieka atviras navigacijos užduotis, tokias kaip Airbnb atidarymas, iššokančių langų atmetimas ir Stokholmo paieška.
3. Aktyvus puslapis tikrinamas pagal struktūrizuotą Pydantic schemą, siekiant išgauti skelbimų pavadinimus, nakvynės kainas, įvertinimus ir URL.
4. Python logika palygina išgautus skelbimus ir paryškina pigiausią variantą.

Šis požiūris palaiko lanksčią, rega pagrįstą logiką, kurioje Browser-Use yra stiprus, tuo pat metu suteikiant deterministinį naršyklės valdymą tada, kai reikia.

## Pagrindinės išvados ir gerosios praktikos

### Kada naudoti agentą ir kada aktorių

| Scenarijus | Naudoti agentą | Naudoti aktorių |
|----------|-----------------|-------------|
| Dinamiški išdėstymai | Taip, AI gali prisitaikyti prie puslapio pokyčių | Ne, trapūs selektoriai gali gesti |
| Žinoma struktūra | Ne, agentas yra lėtesnis nei tiesioginis valdymas | Taip, greitas ir tikslus |
| Elementų radimas | Taip, natūralios kalbos reikšmės puikiai veikia | Ne, reikalingi tikslūs selektoriai |
| Laiko valdymas | Ne, mažiau nuspėjamas | Taip, pilnas laukimų ir bandymų kontrolė |
| Kompleksinės darbo eigos | Taip, tvarko netikėtas UI būsenas | Ne, reikia explicit šakų |

### Browser-Use gerosios praktikos

1. Pradėkite nuo agento tyrinėjimui ir dinamiškai navigacijai.
2. Pereikite prie tiesioginio puslapio valdymo, kai sąveika tampa nuspėjama.
3. Naudokite struktūrizuotus išvesties modelius, kad išgauti duomenys būtų patikrinti ir tipizuoti.
4. Strategiškai pridėkite uždelsimus po veiksmų, kurie sukelia matomus UI pokyčius.
5. Fiksuokite ekrano nuotraukas iteracijų metu, kad būtų lengviau identifikuoti klaidas.
6. Tikėkitės, kad svetainės keisis ir sukurkite atsargines strategijas iššokančioms langų ir išdėstymo pokyčiams.
7. Derinkite agento ir aktoriaus modelius, kad gautumėte tiek lankstumą, tiek tikslumą.

### Saugumo gairės naršyklės agentams

Naršyklės agentai veikia gyvose svetainėse, todėl jiems reikia griežtesnių ribojimų nei scenarijui, kuris tik kviečia žinomą API. Prieš pereinant nuo užrašų knygelės demonstracijos prie realios darbo eigos, apibrėžkite kontrolę, ką agentas gali matyti, spausti ir pateikti.

1. **Apribokite naršyklės aplinką.** Paleiskite agentą skirtingoje naršyklės profilyje arba izoliuotoje aplinkoje ir apribokite jį tik užduočiai reikalingiems domenams.
2. **Atskirkite stebėjimą nuo veiksmų.** Leiskite agentui pirmiausia ieškoti, skaityti ir išgauti duomenis; reikalaukite aiškios patvirtinimo žingsnio prieš pateikiant formas, siuntinėjant žinutes, užsakant keliones, perkant, trinant įrašus ar keičiant paskyros nustatymus.
3. **Nelaikykite slaptažodžių ir konfidencialių duomenų užklausose ir žurnaluose.** Neskelbkite modelio kontekste slaptažodžių, mokėjimo detalių, sesijos slapukų ar asmens duomenų. Leiskite naudotojui atlikti autentifikaciją ir šalinimą iš žurnalų.
4. **Traktuokite puslapio turinį kaip nepatikimą įvestį.** Svetainėje gali būti instrukcijos agentui, o ne naudotojui. Agentas turėtų ignoruoti tekstą, kuris prašo pakeisti tikslą, atskleisti duomenis, išjungti saugiklius ar lankytis nesusijusiose svetainėse.
5. **Naudokite deterministines patikras rizikingose vietose.** Prieš prašant naudotojo patvirtinimo, patikrinkite dabartinį URL, puslapio pavadinimą, pasirinktą elementą, kainą, gavėją ir veiksmo santrauką su kodu.
6. **Nustatykite biudžetus ir stabdymo sąlygas.** Apribokite veiksmų, pakartojimų, skirtukų ir minučių skaičių, kuriuos agentas gali naudoti. Sustabdykite veiklą, kai puslapio būsena neaiški, vietoje to, kad tęstumėte spustelėjimus.
7. **Fiksuokite naudingus įrodymus, o ne viską.** Laikykite veiksmų santraukas, laiko žymes, URL, pasirinktų elementų aprašymus ir ekrano nuotraukų nuorodas, kad būtų galima peržiūrėti klaidas nesaugant nereikalingo jautraus turinio.

Airbnb pavyzdyje saugiausia numatytoji veiksena yra ieškoti skelbimų ir išgauti kainas. Prisijungimas, kontakto užmezgimas su šeimininku ar užsakymo užbaigimas turėtų būti atskira naudotojo patvirtinta operacija.

### Realūs pritaikymai

- Kelionių užsakymas ir kainų stebėjimas
- Elektroninės prekybos kainų palyginimas ir prieinamumo patikra
- Struktūrizuotas duomenų išgavimo iš dinamiškų svetainių procesas
- Regos pagrindu UI testavimas ir tikrinimas
- Svetainių stebėjimas ir perspėjimai
- Išmanus formų užpildymas daugiapakopiuose procesuose

## Realus pavyzdys: Microsoft Project Opal

Šiame pamokoje kuriamas agentas yra mažoji vietinė **kompiuterio naudojimo agento (CUA)** versija — programa, kuri valdo naršyklę taip, lyg ją naudotų žmogus. Microsoft diegia tą pačią idėją verslui su **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, galimybe Microsoft 365 Copilot platformoje.

Naudodami Project Opal, jūs aprašote užduotį, o agentas veikia jūsų vardu naudodamas **kompiuterio naudojimą saugioje Windows 365 Cloud PC aplinkoje**, dirbdamas su jūsų organizacijos naršyklės pagrindu veikiančiomis programomis, svetainėmis ir duomenimis. Jis veikia **asinchroniškai fone**, ir jūs galite bet kada vadovauti ar perimti kontrolę. Pavyzdinės užduotys:

- Valdyti saugumo grupių narių užklausas
- Rinkti ir tikrinti auditui skirtus įrodymus atitikties patikrinimams
- IT incidentų skirstymas (bilietų būsenos atnaujinimas, savininkų paskyrimas, dublikatų uždarymas)
- Apjungti Excel duomenis į finansinių uždarymų pristatymus

Opal yra naudingas pavyzdys, ką reiškia **gamybai tinkamas, patikimas** kompiuterio naudojimo agentas — ir jis sustiprina ankstesnių pamokų koncepcijas:

| Šios pamokos konceptas | Kaip jį įgyvendina Project Opal |
|------------------------|-----------------------------|
| **Žmogus grandyje** (pamoka 06) | Opal sustoja prisijungimo duomenims, jautriai informacijai ar neaiškioms instrukcijoms ir niekada nepateikia slaptažodžių ar nepateikia formų be aiškaus patvirtinimo. Galite *Perimti kontrolę* ir *Grąžinti kontrolę* vykdant užduotį. |
| **Patikimi ir saugūs agentai** (pamokos 06 ir 18) | Veikia izoliuotoje Windows 365 Cloud PC aplinkoje, pagal nutylėjimą tik naršyklėje (kitas kompiuterio prieigas blokuoja Intune), naudoja *jūsų* tapatybę, todėl pasiekia tik tai, kam esate įgaliotas, ir fiksuoja kiekvieną veiksmą audito tikslais. |
| **Planavimas ir metakognicija** (pamokos 07 ir 09) | Opal pirmiausia generuoja veiksmų planą, po to stebi savo logiką kiekviename žingsnyje ir sustoja, jei aptinka įtartiną veiklą. |
| **Pakartotinai naudojamos galimybės / įrankiai** (pamoka 04) | **Įgūdžiai** leidžia rašyti instrukcijas kartotinoms užduotims (importuojamas iš `.md` failo arba kuriamas su Opal) ir pakartotinai naudoti jas pokalbiuose. |

> **Pasiekiamumas:** Project Opal šiuo metu yra prieinamas vartotojams per [Frontier ankstyvojo prieigos programą](https://adoption.microsoft.com/copilot/frontier-program/) su Microsoft 365 Copilot prenumerata, ir jūsų administratorius turi atlikti nustatymus. Kadangi tai eksperimentinė Frontier funkcija, galimybės gali keistis laikui bėgant.

## Papildomi ištekliai

- [Pradžia su Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integracijos šablonas](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktorių parametrai ir turinio išgavimas](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurso nustatymas](../00-course-setup/README.md)

## Ankstesnė pamoka

[Microsoft Agent Framework tyrinėjimas](../14-microsoft-agent-framework/README.md)

## Kitoji pamoka

[Mastelio didinimas agentams](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->