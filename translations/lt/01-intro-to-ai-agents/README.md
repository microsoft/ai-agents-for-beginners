[![Įvadas į DI agentus](../../../translated_images/lt/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šio pamokos vaizdo įrašą)_

# Įvadas į DI agentus ir agentų naudojimo atvejus

Sveiki atvykę į kursą **DI agentai pradedantiesiems**! Šis kursas suteikia jums pagrindines žinias — ir veikiantį kodą — kad pradėtumėte kurti DI agentus nuo nulio.

Ateikite pasisveikinti į <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure DI Discord bendruomenę</a> — joje daug besimokančių ir DI kūrėjų, kurie mielai atsako į klausimus.

Prieš pradėdami kurti, įsitikinkime, kad iš tikrųjų suprantame, kas yra DI agentas ir kada verta jį naudoti.

---

## Įvadas

Ši pamoka apima:

- Kas yra DI agentai ir kokie skirtingi jų tipai egzistuoja
- Kokie uždaviniai geriausiai tinka DI agentams
- Pagrindiniai komponentai, kuriuos naudosite projektuodami agentinį sprendimą

## Mokymosi tikslai

Šios pamokos pabaigoje turėtumėte sugebėti:

- Paaiškinti, kas yra DI agentas ir kuo jis skiriasi nuo įprasto DI sprendimo
- Žinoti, kada verta naudoti DI agentą (ir kada ne)
- Apibrėžti pagrindinį agentinio sprendimo projektą realiam pasaulio problemos sprendimui

---

## DI agentų apibrėžimas ir DI agentų tipai

### Kas yra DI agentai?

Čia pateikiamas paprastas paaiškinimas:

> **DI agentai yra sistemos, kurios leidžia dideliems kalbų modeliams (LLM) iš tiesų *daryti veiksmus* — suteikdamos jiems įrankius ir žinias veikti pasaulyje, o ne tik atsakyti į užklausas.**

Paaiškinkime tai plačiau:

- **Sistema** — DI agentas nėra tik viena dalis. Tai kelių dalių rinkinys, dirbantis kartu. Kiekvienas agentas turi tris pagrindines dalis:
  - **Aplinka** — erdvė, kurioje agentas veikia. Pavyzdžiui, kelionių užsakymų agentas veikia užsakymų platformoje.
  - **Jutikliai** — kaip agentas skaito savo aplinkos būseną. Mūsų kelionių agentas gali tikrinti viešbučių užimtumą ar skrydžių kainas.
  - **Veikimo įtaisai** — kaip agentas imasi veiksmų. Kelionių agentas gali užsakyti kambarį, siųsti patvirtinimą arba atšaukti rezervaciją.

![Kas yra DI agentai?](../../../translated_images/lt/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Dideli kalbų modeliai** — agentai egzistavo ir prieš LLM, bet būtent LLM suteikia šiuolaikiniams agentams didelę galią. Jie supranta natūralią kalbą, sugeba kontekstualiai mąstyti ir paversti neaiškų vartotojo prašymą į konkretų veiksmų planą.

- **Atlikti veiksmus** — be agentų sistemos, LLM tik generuoja tekstą. Agentų sistemoje LLM iš tiesų gali *vykdyti* veiksmų žingsnius — ieškoti duomenų bazėje, kviesti API, siųsti žinutę.

- **Priėjimas prie įrankių** — kokius įrankius agentas gali naudoti, priklauso nuo (1) aplinkos, kurioje veikia, ir (2) ką kūrėjas jam suteikė. Kelionių agentas gali ieškoti skrydžių, bet negali redaguoti klientų įrašų — tai priklauso nuo sujungtos sistemos.

- **Atmintis + žinios** — agentai gali turėti trumpalaikę atmintį (dabartinę pokalbio eigą) ir ilgalaikę atmintį (klientų duomenų bazę, ankstesnius sąveikus). Kelionių agentas „prisimena“, kad jums labiau patinka vietos prie lango.

---

### Skirtingi DI agentų tipai

Ne visi agentai yra sukurti vienodai. Štai pagrindinių tipų apžvalga, naudojant kelionių užsakymų agentą kaip pavyzdį:

| **Agento tipas** | **Ką jis daro** | **Kelionių agento pavyzdys** |
|---|---|---|
| **Paprasti refleksiniai agentai** | Laikosi griežtai nustatytų taisyklių — nėra atminties, nėra planavimo. | Pastebi skundo laišką → persiunčia klientų aptarnavimui. Viskas. |
| **Modeliu pagrįsti refleksiniai agentai** | Turi vidinį pasaulio modelį ir jį atnaujina, kai kas keičiasi. | Stebi istorinį skrydžių kainų pokytį ir pažymi maršrutus, kurių kainos smarkiai pakilo. |
| **Tikslo siekiantys agentai** | Turi tikslą ir žingsnis po žingsnio randa, kaip jį pasiekti. | Užsako visą kelionę (skrydžius, automobilį, viešbutį) nuo jūsų buvimo vietos iki kelionės tikslo. |
| **Naudingumo pagrindu agentai** | Ne tik randa *sprendimą*, bet *geriausią* sprendimą, vertindami kompromisus. | Derina kainos ir patogumo santykį, kad rastų kelionę, labiausiai atitinkančią jūsų pageidavimus. |
| **Mokymosi agentai** | Tobulėja bėgant laikui mokydamiesi iš grįžtamojo ryšio. | Pritaiko būsimus užsakymų pasiūlymus pagal po kelionės apklausos rezultatus. |
| **Hierarchiniai agentai** | Aukšto lygio agentas darbus suskaido į potaskis ir deleguoja žemesnio lygio agentams. | Paskyra „atšaukti kelionę“ suskaidoma į: atšaukti skrydį, viešbutį, automobilio nuomą — kiekvieną užduotį atlieka sub-agentas. |
| **Daugiagentinės sistemos (MAS)** | Kelni nepriklausomi agentai dirba kartu (arba konkuruoja). | Bendradarbiavimas: atskiri agentai rūpinasi viešbučiais, skrydžiais ir pramogomis. Konkurencija: keli agentai konkuruoja užpildyti viešbučių kambarius geriausia kaina. |

---

## Kada naudoti DI agentus

Tik todėl, kad *galite* naudoti DI agentą, nereiškia, kad visada *reikia*. Štai situacijos, kai agentai iš tiesų atsiskleidžia:

![Kada naudoti DI agentus?](../../../translated_images/lt/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Atviri sprendimai** — kai žingsniai problemai išspręsti negali būti iš anksto užprogramuoti. Reikia, kad LLM dinamiškai rastų sprendimo kelią.
- **Daug žingsnių turinčios procedūros** — užduotys, kurios reikalauja naudotis įrankiais keliais etapais, o ne vienu paieškos ar teksto generavimo žingsniu.
- **Tobulėjimas laikui bėgant** — kai norite, kad sistema taptų protingesnė remdamasi vartotojų grįžtamuoju ryšiu arba aplinkos signalais.

Vėliau šiame kurse pamokoje **Patikimų DI agentų kūrimas** išsamiau panagrinėsime, kada naudoti (ir kada *neverta*) DI agentus.

---

## Agentinių sprendimų pagrindai

### Agentų kūrimas

Pirmasis žingsnis kuriant agentą yra apibrėžti *ką jis gali daryti* — jo įrankius, veiksmus ir elgesį.

Šiame kurse pagrindinė platforma yra **Microsoft Foundry Agent Service**. Ji palaiko:

- Modelius iš tiekėjų, tokių kaip OpenAI, Mistral ir Meta (Llama)
- Licencijuotus duomenis iš tiekėjų, tokių kaip Tripadvisor
- Standartizuotas OpenAPI 3.0 įrankių apibrėžtis

### Agentinės schemos

Su LLM bendraujate per užklausas. Su agentais ne visada galima rankomis kurti kiekvieną užklausą — agentas turi imtis veiksmų keliais žingsniais. Čia į pagalbą ateina **agentinės schemos**. Tai pakartotinai naudojamos strategijos, kaip efektyviau ir patikimiau pasitelkti ir koordinuoti LLM.

Šis kursas pagrįstas pačiomis dažniausiomis ir naudingiausiomis agentinėmis schemomis.

### Agentinės sistemos karkasai

Agentiniai karkasai suteikia kūrėjams paruoštas šablonus, įrankius ir infrastruktūrą agentams kurti. Jie palengvina:

- Įrankių ir galimybių sujungimą
- Stebėjimą, ką agentas daro (ir klaidų taisymą, jei kas nepasiseka)
- Bendradarbiavimą tarp kelių agentų

Šiame kurse daugiausia dėmesio skiriame **Microsoft Agent Framework (MAF)**, skirtam profesionaliems agentams kurti.

---

## Kodo pavyzdžiai

Pasiruošę pamatyti veikimą? Štai šios pamokos kodo pavyzdžiai:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Turite klausimų?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susisiektumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo DI agentų klausimus bendruomenės pagalba.


---

## Šio agente dūmų testas (pasirinktinai)

Kai išmoksite diegti agentus [16 pamokoje](../16-deploying-scalable-agents/README.md), galėsite pridėti greitą po diegimo sveikatos patikrinimą šiam pamokos `TravelAgent` agentui su paruoštu katalogu [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Žr. [`tests/README.md`](../tests/README.md) kaip jį paleisti.

---

## Ankstesnė pamoka

[Kurso paruošimas](../00-course-setup/README.md)

## Kitoji pamoka

[Agentinės sistemos karkasų tyrimas](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->