# Kompiuterinių naudojimo agentų (CUA) kūrimas

Kompiuterinės naudojimo agentūros gali sąveikauti su svetainėmis taip pat, kaip tai darytų žmogus: atidarant naršyklę, tikrinant puslapį ir imantis geriausio veiksmo pagal matomą informaciją. Šioje pamokoje jūs sukursite naršyklės automatizavimo agentą, kuris ieško Airbnb, ištraukia struktūruotus skelbimų duomenis ir nustato pigiausią nakvynę Stokholme.

Pamoka sujungia Browser-Use dirbtinio intelekto valdomą navigaciją, Playwright ir Chrome DevTools protokolą (CDP) naršyklės valdymui, Azure OpenAI su vizijos funkcijomis loginėms išvadoms ir Pydantic struktūruotam duomenų išgavimui.

## Įvadas

Šioje pamokoje apžvelgsime:

- Kada kompiuterinių naudojimo agentų sprendimas tinka geriau nei vien API automatizavimas
- Kaip sujungti Browser-Use su Playwright ir CDP, užtikrinant patikimą naršyklės gyvavimo ciklo valdymą
- Kaip naudoti Azure OpenAI viziją ir struktūruotą Pydantic išvestį norint išgauti skelbimų duomenis iš dinamiškų tinklalapių
- Kada naudoti agento pirmumo, veiksmo pirmumo ar hibridinį naršyklės automatizavimo darbo srautą

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Suvesti Browser-Use su Azure OpenAI ir Playwright
- Sukurti naršyklės automatizavimo darbo srautą, kuris naršytų realią svetainę ir valdytų dinamiškus UI elementus
- Išgauti tipizuotus rezultatus iš matomos puslapio turinio ir paversti juos tolimesne verslo logika
- Pasirinkti tarp agento ir veiksmo modelių, atsižvelgiant į naršyklės užduoties numatymą

## Kodo pavyzdys

Šioje pamokoje pateikiamas vienas užrašų knygutės vadovas:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Paleidžia Chrome sesiją per CDP, ieško Airbnb Stokholmo skelbimų, ištraukia kainas naudojant Browser-Use viziją ir grąžina pigiausią variantą struktūruotais duomenimis.

## Prieš sąlygos

- Python 3.12+
- Azure OpenAI paskyros konfigūracija jūsų aplinkoje
- Vietinis Chrome arba Chromium įdiegimas
- Playwright priklausomybių įdiegimas
- Pagrindinės asynchrininės Python pažintys

## Nustatymas

Įdiekite užrašų knygutėje naudojamus paketus:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nustatykite Azure OpenAI aplinkos kintamuosius, kuriuos naudoja užrašų knygutė:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Pasirinktinai: pagal numatytuosius nustatymus naudojama naujausia API versija, jei nenurodyta
AZURE_OPENAI_API_VERSION=...
```

## Architektūros apžvalga

Užrašų knygutė demonstruoja hibridinį naršyklės automatizavimo darbo srautą:

1. Chrome startuoja su įjungtu CDP, todėl tiek Playwright, tiek Browser-Use gali naudoti tą pačią naršyklės sesiją.
2. Browser-Use agentas sprendžia atvirus navigacijos uždavinius, tokius kaip Airbnb atidarymas, iškylančių langų uždarymas ir Stokholmo paieška.
3. Aktyvus puslapis tikrinamas pagal struktūruotą Pydantic schemą, ištraukiami skelbimų pavadinimai, naktinės kainos, įvertinimai ir URL.
4. Python logika palygina ištrauktus skelbimus ir paryškina pigiausią rezultatą.

Toks požiūris išlaiko lankstų, vizijos pagrindu veikiančią loginę sistemą, kurioje Browser-Use ir sekant, tačiau suteikia determinuojamą naršyklės valdymą, kai to reikia.

## Svarbiausios išvados ir gerosios praktikos

### Kada naudoti agentą, o kada aktorių

| Situacija | Naudoti agentą | Naudoti aktorių |
|----------|----------------|-----------------|
| Dinamiški maketai | Taip, DI gali prisitaikyti prie puslapio pokyčių | Ne, trapūs selektoriai gali neveikti |
| Žinoma struktūra | Ne, agentas yra lėtesnis už tiesioginį valdymą | Taip, greita ir tiksli |
| Elementų radimas | Taip, natūrali kalba veikia gerai | Ne, reikalingi tikslūs selektoriai |
| Laiko valdymas | Ne, mažiau nuspėjama | Taip, pilnas laukimų ir pakartojimų valdymas |
| Sudėtingi darbo srautai | Taip, valdo netikėtas UI būsenas | Ne, reikalauja aiškių šakų |

### Browser-Use geros praktikos

1. Pradėkite agentą tyrimams ir dinamiškai navigacijai.
2. Perjunkite į tiesioginį puslapio valdymą, kai sąveika tampa nuspėjama.
3. Naudokite struktūruotus išvesties modelius, kad išgauti duomenys būtų patikrinti ir tipų saugūs.
4. Pridėkite strategiškus laukimo laikus po veiksmų, sukeliančių matomus UI pokyčius.
5. Fiksuokite ekrano kopijas atliekant iteracijas, kad klaidos būtų lengviau aptinkamos.
6. Tikėkitės svetainių pokyčių ir numatykite atsargines strategijas iškylantiems langams ir maketų poslinkiams.
7. Derinkite agento ir aktoriaus modelius, kad gautumėte lankstumą ir tikslumą.

### Realūs panaudojimo atvejai

- Kelionių rezervavimas ir kainų stebėjimas
- Elektroninės prekybos kainų palyginimas ir prieinamumo tikrinimas
- Struktūruotas duomenų išgavimas iš dinamiškų svetainių
- Viziją suvokiantis UI testavimas ir patikra
- Svetainių stebėjimas ir perspėjimas
- Protingas formų pildymas daugiapakopėse procedūrose

## Realus pavyzdys: Microsoft Project Opal

Šioje pamokoje sukurtas agentas yra nedidelė, vietinė **kompiuterinio naudojimo agento (CUA)** versija – programa, kuri valdo naršyklę taip, kaip tai darytų žmogus. Microsoft šią idėją taiko įmonėms su **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkcija, įtraukta į Microsoft 365 Copilot.

Su Project Opal aprašote užduotį, o agentas veikia jūsų vardu naudodamas **kompiuterinio naudojimo funkcijas saugioje Windows 365 Cloud PC aplinkoje**, dirba jūsų organizacijos naršyklės pagrindu veikiančių programų, svetainių ir duomenų atžvilgiu. Agentas veikia **asinchroniškai fone**, o jūs galite bet kada perimti arba nurodyti darbą. Pavyzdiniai darbai yra:

- Tvarkyti saugumo grupių narystės prašymus
- Rinkti ir patvirtinti audito įrodymus atitikties peržiūroms
- IT incidentų prioritetų nustatymas (bilieto statuso atnaujinimas, savininkų priskyrimas, dublių uždarymas)
- Excel duomenų sudarymas finansiniam uždarymui

Opal yra gera nuoroda, kaip atrodo **gamybinės klasės, patikimas** kompiuterinio naudojimo agentas – ir sustiprina ankstesnių pamokų konceptus:

| Koncepcija šiame kurse | Kaip Project Opal ją taiko |
|---------------------|--------------------------------|
| **Žmogus procese** (Pamoka 06) | Opal sustoja prisijungimo duomenims, jautriems duomenims ar neaiškioms instrukcijoms, ir niekada neįveda slaptažodžių ar nepateikia formų be aiškaus patvirtinimo. Galite *Perimti valdymą* ir *Grąžinti valdymą* vykdant užduotį. |
| **Patikimi ir saugūs agentai** (Pamokos 06 ir 18) | Veikia izoliuotoje Windows 365 Cloud PC aplinkoje, iš pradžių veikia tik naršyklėje (kitas kompiuterio prieigas blokuoja Intune), naudoja *jūsų* identitetą, todėl pasiekia tik tai, kam turite leidimą, ir fiksuoja visas veiklas audito tikslais. |
| **Planavimas ir metakognicija** (Pamokos 07 ir 09) | Opal pirmiausia generuoja darbo planą, tada prižiūri savo loginį procesą kiekviename žingsnyje ir sustoja, jei aptinka įtartiną veiklą. |
| **Pakartotinai naudojamos galimybės / įrankiai** (Pamoka 04) | **Įgūdžiai** leidžia rašyti instrukcijas kartojamiems darbams (importuojamus iš `.md` failo arba sukurtus su Opal) ir panaudoti juos pokalbiuose. |

> **Prieinamumas:** Project Opal šiuo metu prieinamas [Frontier ankstyvos prieigos programos](https://adoption.microsoft.com/copilot/frontier-program/) naudotojams su Microsoft 365 Copilot prenumerata, o jūsų administratorius turi užbaigti konfigūraciją. Kadangi tai eksperimentinė Frontier funkcija, galimybės gali keistis laikui bėgant.

## Papildomi šaltiniai

- [Pradėkite su Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integracijos šablonas](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktoriaus parametrai ir turinio išgavimas](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurso nustatymas](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->