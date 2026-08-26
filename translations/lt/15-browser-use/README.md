# Kompiuterio naudojimo agentų (CUA) kūrimas

Kompiuterio naudojimo agentai gali sąveikauti su svetainėmis taip pat, kaip ir žmogus: atidarant naršyklę, tikrinant puslapį ir imantis geriausio tolimesnio veiksmo pagal tai, ką jie mato. Šiame pamokoje sukursite naršyklės automatizavimo agentą, kuris ieško Airbnb, ištraukia struktūrizuotus skelbimų duomenis ir nustato pigiausią viešnagę Stokholme.

Pamoka sujungia Browser-Use AI valdomam naršymui, Playwright ir Chrome DevTools protokolą (CDP) naršyklės valdymui, Azure OpenAI vaizdu pagrįstam samprotavimui ir Pydantic struktūrizuotam duomenų gavimui.

## Įvadas

Šioje pamokoje bus aptarta:

- Kada kompiuterio naudojimo agentai yra geresnis pasirinkimas nei tik API automatizavimas
- Browser-Use su Playwright ir CDP derinimas patikimam naršyklės veikimo ciklo valdymui
- Azure OpenAI vaizdo ir struktūriškai Pydantic išvesties naudojimas skelbimų duomenų išgavimui iš dinamiškų svetainių
- Sprendimas, kada naudoti agento, aktoriaus ar hibridinį naršyklės automatizavimo darbo eigą

## Mokymosi tikslai

Baigę šią pamoką, žinosite, kaip:

- Konfigūruoti Browser-Use su Azure OpenAI ir Playwright
- Sukurti naršyklės automatizavimo darbo eigą, kuri naršo tikroje svetainėje ir valdo dinamiškus UI elementus
- Išgauti tipuotas išvestis iš matomo puslapio turinio ir paversti jas verslo logika
- Pasirinkti agento arba aktoriaus modelį priklausomai nuo naršyklės užduoties nuspėjamumo

## Kodo pavyzdys

Šioje pamokoje rasite vieną užrašų bloką:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Paleidžia Chrome seansą per CDP, ieško Airbnb Stokholmo skelbimų, ištraukia kainas naudodamas Browser-Use vaizdą ir pateikia pigiausią variantą struktūrizuotais duomenimis.

## Reikalavimai

- Python 3.12+
- Jūsų aplinkoje sukonfigūruotas Azure OpenAI diegimas
- Vietoje įdiegta Chrome arba Chromium naršyklė
- Įdiegti Playwright priklausomybes
- Pagrindinės žinios apie asinchroninį Python

## Diegimas

Įdiekite paketus, naudojamus užrašų bloke:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Nustatykite Azure OpenAI aplinkos kintamuosius, kuriuos naudoja užrašų blokas:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Neprivaloma: pagal numatytuosius nustatymus naudojama naujausia API versija, kai paliekama tuščia
AZURE_OPENAI_API_VERSION=...
```

## Architektūros apžvalga

Užrašų blokas demonstruoja hibridinę naršyklės automatizavimo darbo eigą:

1. Chrome paleidžiamas su įjungtu CDP, tad tiek Playwright, tiek Browser-Use gali naudoti tą pačią naršyklės sesiją.
2. Browser-Use agentas tvarko atvirus navigacijos uždavinius, tokius kaip Airbnb atidarymas, iškylančių langų atmetimas ir paieška Stokholme.
3. Aktyvus puslapis tikrinamas pagal struktūrizuotą Pydantic schemą, kad būtų ištraukti skelbimų pavadinimai, kainos už naktį, įvertinimai ir URL.
4. Python logika palygina išgautus skelbimus ir paryškina pigiausią rezultatą.

Šis požiūris išlaiko lankstų, vaizdu pagrįstą samprotavimą, kuriame Browser-Use yra stiprus, kartu suteikdamas deterministinį naršyklės valdymą, kai to reikia.

## Pagrindinės įžvalgos ir gerosios praktikos

### Kada naudoti agentą ar aktorių

| Scenarijus | Naudoti agentą | Naudoti aktorių |
|----------|-----------|-----------|
| Dinamiški maketai | Taip, AI gali prisitaikyti prie puslapio pokyčių | Ne, trapūs selektoriai gali sugesti |
| Žinoma struktūra | Ne, agentas veikia lėčiau nei tiesioginė kontrolė | Taip, greita ir tiksli |
| Elementų radimas | Taip, natūrali kalba veikia gerai | Ne, reikalingi tikslūs selektoriai |
| Laiko valdymas | Ne, mažiau nuspėjama | Taip, visiškas laukimo ir bandymų kontroliavimas |
| Sudėtingos darbo eigų | Taip, tvarko netikėtas UI būsenas | Ne, reikalauja aiškaus šakojimo |

### Browser-Use geriausios praktikos

1. Pradėkite nuo agento tyrinėjimui ir dinamiškai navigacijai.
2. Pereikite prie tiesioginės puslapio kontrolės, kai sąveika tampa nuspėjama.
3. Naudokite struktūrizuotos išvesties modelius, kad išgauti duomenys būtų patikrinti ir tipų saugūs.
4. Strategiškai pridėkite vėlavimus po veiksmų, kurie sukelia matomus UI pokyčius.
5. Fiksuokite ekrano kopijas iteracijos metu, kad gedimus būtų lengviau analizuoti.
6. Tikėkitės, kad svetainės keisis, ir sukurkite atsarginius planus iškylantiems langams ir maketų pasikeitimams.
7. Derinkite agento ir aktoriaus modelius, kad gautumėte ir lankstumą, ir tikslumą.

### Saugumo gairės naršyklės agentams

Naršyklės agentai veikia tiesiogiai svetainėse, tad jiems reikia griežtesnių ribų nei skriptui, kuris tik kviečia žinomą API. Prieš pereinant nuo užrašų bloko demonstravimo prie realios darbo eigos, apibrėžkite, ką agentas gali matyti, spausti ir siųsti.

1. **Apribokite naršymo aplinką.** Vykdykite agentą specialiame naršyklės profilyje ar smėlio dėžėje ir ribokite prie užduočiai reikalingų domenų.
2. **Atskirkite stebėjimą nuo veiksmų.** Leiskite agentui pirmiausia ieškoti, skaityti ir išgauti duomenis; reikalaukite aiškaus patvirtinimo, prieš siunčiant formas, žinutes, užsakant keliones, atlikus pirkimus, trinant įrašus ar keičiant paskyros nustatymus.
3. **Neįtraukite slaptų duomenų į užklausas ir pėdsakus.** Neskelbkite slaptažodžių, mokėjimo duomenų, sesijų slapukų ar asmeninių duomenų atvirame modelio kontekste. Leiskite naudotojui autentifikuotis ir ištrinti jautrius laukus iš žurnalų.
4. **Vertinkite puslapio turinį kaip nepatikimą įvestį.** Svetainėje gali būti instrukcijų agentui, ne naudotojui. Agentas turėtų ignoruoti teksto dalis, kurios verčia keisti tikslus, atskleisti duomenis, išjungti apsaugas ar lankytis nesusijusiose svetainėse.
5. **Naudokite determinuotus patikrinimus dėl rizikingų veiksmų.** Patikrinkite dabartinį URL, puslapio pavadinimą, pasirinktą elementą, kainą, gavėją ir veiksmų santrauką su kodu prieš prašant naudotojo patvirtinimo galutiniam veiksmui.
6. **Nustatykite biudžetus ir sustabdymo sąlygas.** Apribokite agento veiksmų, pakartojimų, skirtukų ir laiko kiekį. Sustabdykite darbą, kai puslapio būsena netiksli, vietoje tęsiamo spustelėjimo.
7. **Fiksuokite naudotą įrodymą, o ne viską.** Saugojimo santraukas, laiko žymes, URL, pasirinktų elementų aprašymus, ekrano kopijų nuorodas, kad būtų galima peržiūrėti klaidas, ne saugant nereikalingą jautrų puslapio turinį.

Airbnb pavyzdyje saugus numatytasis veiksmas yra ieškoti skelbimų ir išgauti kainas. Prisijungimas, susisiekimas su šeimininku ar užsakymo atlikimas turi būti atskiri naudotojo patvirtinti veiksmai.

### Tikri panaudojimo atvejai

- Kelionių užsakymų ir kainų stebėjimas
- Elektroninės prekybos kainų palyginimas ir prieinamumo patikrinimai
- Struktūrizuotas duomenų išgavimas iš dinamiškų svetainių
- Vaizdu pagrįstas UI testavimas ir patikra
- Svetainių stebėjimas ir perspėjimai
- Protingas formų pildymas kelių žingsnių procesuose

## Tikras pavyzdys: Microsoft Project Opal

Šiame pamokoje kuriamas agentas yra nedidelė, vietinė **kompiuterio naudojimo agente (CUA)** versija — programa, kuri valdo naršyklę taip, kaip tai darytų žmogus. Microsoft diegia šią idėją verslui per **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** — funkciją Microsoft 365 Copilot.

Su Project Opal apibūdinate užduotį, o agentas veikia jūsų vardu naudodamas **kompiuterio naudojimą saugiame Windows 365 Cloud PC**, operuodamas jūsų organizacijos naršyklės programose, svetainėse ir duomenyse. Jis veikia **asinchroniškai fone**, o jūs galite bet kada nukreipti darbą arba perimti kontrolę. Pavyzdiniai darbai apima:

- Saugumo grupių narystės užklausų valdymą
- Audito įrodymų rinkimą ir patvirtinimą atitikčiai
- IT incidentų tvarkymą (bilieto būsenos atnaujinimą, savininkų paskyrimą, dublikatus uždarant)
- Excel duomenų apibendrinimą finansiniam uždarymui

Opal yra naudingas pavyzdys, kaip atrodo **gamybinės klasės, patikimas** kompiuterio naudojimo agentas — ir jis sustiprina ankstesnių pamokų konceptus:

| Koncepcija šiame kurse | Kaip Project Opal ją įgyvendina |
|------------------------|-----------------------------|
| **Žmogus procese** (Pamoka 06) | Opal laukia prisijungimo duomenų, jautrios informacijos ar neaiškių nurodymų, niekada neįveda slaptažodžių ar neišsiunčia formų be aiškaus patvirtinimo. Galite *Perimti kontrolę* ir *Grąžinti kontrolę* proceso viduryje. |
| **Patikimi ir saugūs agentai** (Pamokos 06 ir 18) | Veikia izoliuotame Windows 365 Cloud PC, pagal nutylėjimą tik naršyklė (kitokie kompiuterio pasiekiamumai blokuojami per Intune), naudoja *jūsų* tapatybę, tad pasiekia tik tai, ką leidžiama, ir registruoja kiekvieną veiksmą audito tikslams. |
| **Planavimas & metakognicija** (Pamokos 07 ir 09) | Opal pirmiausia sudaro darbo planą, tada prižiūri savo samprotavimą kiekviename žingsnyje ir sustoja, jei aptinka įtartiną veiklą. |
| **Pakartotinai naudojamos galimybės / įrankiai** (Pamoka 04) | **Įgūdžiai** leidžia rašyti instrukcijas kartotinams darbams (importuojamus iš `.md` failo ar kuriamus Opal aplinkoje) ir naudoti juos pokalbiuose. |

> **Prieinamumas:** Project Opal šiuo metu pasiekiamas vartotojams [Frontier ankstyvos prieigos programoje](https://adoption.microsoft.com/copilot/frontier-program/) turint Microsoft 365 Copilot prenumeratą, ir administratoriui būtina atlikti nustatymus. Kadangi tai eksperimentinė Frontier funkcija, galimybės gali keistis.

## Žinių tikrinimas

Patikrinkite savo supratimą prieš pereidami prie kitos pamokos.

**1. Kada naršyklėje veikiantis kompiuterio naudojimo agentas yra geresnis už API ar užduoties darbo eigą?**

<details>
<summary>Atsakymas</summary>

Naudokite naršyklės agentą, kai užduotis priklauso nuo to, kas matoma interneto vartotojo sąsajoje, svetainė neteikia reikiamos API, arba puslapis keičiasi pakankamai dažnai, kad fiksuota API ar selektorių logika būtų trapūs. Jei egzistuoja stabili API tais pačiais tikslais, pirmenybę teikite API, nes ji paprastai yra greitesnė, lengviau testuojama ir saugesnė.
</details>

**2. Hibridinėje darbo eigoje, kokias dalis turėtų valdyti agentas ir kokias tiesioginis Playwright kodas?**

<details>
<summary>Atsakymas</summary>

Tegul agentas tvarko atvirus navigacijos ir dinamiškų UI būsenų uždavinius, tokius kaip tinkamo puslapio radimas arba netikėtų iškylančių langų uždarymas. Pereikite prie tiesioginio Playwright valdymo, kai puslapio struktūra žinoma ir veiksmui reikalingas tikslumas, pakartojimai, laukimai ar determinuotas patikrinimas.
</details>

**3. Airbnb pavyzdyje randamas skelbimas, kurį naudotojas galbūt norės užsakyti. Kas turėtų įvykti prieš darbo eigai prisijungiant, susisiekus su šeimininku ar užbaigiant užsakymą?**

<details>
<summary>Atsakymas</summary>

Darbo eiga turėtų sustoti ir paprašyti aiškaus naudotojo patvirtinimo. Prieš tai parodykite aiškią pasirinktą skelbimą, esamą URL, kainą, datas ir numatomą veiksmą. Ieškojimas ir kainų išgavimas gali būti autonomiški; paskyros prieiga, žinutės, pirkimai ir užsakymai turi būti patvirtinti naudotojo.
</details>

**4. Internetinis puslapis nurodo agentui ignoruoti originalias instrukcijas, lankytis kitoje svetainėje ir atskleisti išsaugotus prisijungimo duomenis. Kaip agentas turėtų traktuoti tą tekstą?**

<details>
<summary>Atsakymas</summary>

Traktuokite jį kaip nepatikimą puslapio turinį, o ne kaip kūrėjo ar naudotojo nurodymą. Agentas turėtų likti leidžiamoje domene ir užduoties ribose, atsisakyti atskleisti paslaptis ir vengti sekti puslapio teksto, kuris keičia tikslą, išjungia apsaugas ar nukreipia į nesusijusias svetaines.
</details>

**5. Kokius įrodymus verta išsaugoti agentui veikimo metu, o ko reiktų vengti?**

<details>
<summary>Atsakymas</summary>

Saugokite veiksmų santraukas, laiko žymes, URL, pasirinktų elementų aprašymus, patikrinimų rezultatus ir ekrano kopijų nuorodas, kad būtų galima peržiūrėti veikimą. Venkite saugoti slaptažodžius, mokėjimo duomenis, sesijų slapukus, neapdorotus asmeninius duomenis ar visą puslapio turinį be aiškios pagrįstos poreikio dėl saugojimo ir privatumo.
</details>

## Papildomi šaltiniai

- [Pradžia su Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integracijos šablonas](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktoriaus parametrai ir turinio išgavimas](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurso diegimas](../00-course-setup/README.md)

## Ankstesnė pamoka

[Microsoft agentų sistemos tyrinėjimas](../14-microsoft-agent-framework/README.md)

## Kitoji pamoka

[Mastelio keitimo agentų išdėstymas](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->