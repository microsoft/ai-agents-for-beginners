[![Pristatymas apie AI agentus](../../../translated_images/lt/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Spustelkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šio pamokos vaizdo įrašą)_

# Įvadas į AI agentus ir jų panaudojimo atvejus

Sveiki atvykę į **AI agentų pradedantiesiems** kursą! Šis kursas suteikia jums pagrindines žinias — ir dirbančio kodo pavyzdžius — kad galėtumėte pradėti kurti AI agentus nuo nulio.

Ateikite pasisveikinti <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord bendruomenėje</a> — joje pilna mokinių ir AI kūrėjų, kurie mielai atsakys į jūsų klausimus.

Prieš pradėdami kurti, įsitikinkime, kad iš tiesų suprantame, kas yra AI agentas ir kada verta juo naudotis.

---

## Įvadas

Šioje pamokoje aptarsime:

- Kas yra AI agentai ir kokie jų tipai egzistuoja
- Kokiems uždaviniams AI agentai tinka geriausiai
- Pagrindines dalis, kurias naudosite projektuodami agentinį sprendimą

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Paaiškinti, kas yra AI agentas ir kuo jis skiriasi nuo įprasto AI sprendimo
- Suprasti, kada verta naudoti AI agentą (ir kada ne)
- Apibrėžti paprastą agentinio sprendimo projektą realiam pasaulio uždaviniui

---

## AI agentų apibrėžimas ir tipai

### Kas yra AI agentai?

Štai paprastas paaiškinimas:

> **AI agentai yra sistemos, kurios leidžia Didiesiems kalbos modeliams (LLM) iš tiesų *daryti veiksmus* — suteikiant jiems įrankių ir žinių veikti pasaulyje, ne tik atsakyti į užklausas.**

Išsamiau apie tai:

- **Sistema** — AI agentas nėra vienas dalykas. Tai dalių rinkinys, veikiančios kartu. Kiekvienas agentas iš esmės turi tris dalis:
  - **Aplinka** — erdvė, kurioje agentas veikia. Kelionių užsakymo agentui tai būtų pati užsakymo platforma.
  - **Jutikliai** — kaip agentas skaito esamą aplinkos būseną. Mūsų kelionių agentas gali tikrinti viešbučių užimtumą ar skrydžių kainas.
  - **Veiksmo įtaisai** — kaip agentas imasi veiksmų. Kelionių agentas gali užsakyti kambarį, siųsti patvirtinimą arba atšaukti rezervaciją.

![Kas yra AI agentai?](../../../translated_images/lt/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Didieji kalbos modeliai** — Agentai egzistavo ir be LLM, bet LLM daro šiuolaikinius agentus tokiais galingais. Jie supranta natūralią kalbą, gali spręsti kontekstą ir paversti neaiškų naudotojo prašymą konkrečiu veiksmų planu.

- **Vykdo veiksmus** — be agento sistemos LLM tiesiog generuoja tekstą. Agentų sistemoje LLM gali iš tikrųjų *vykdyti* veiksmus — ieškoti duomenų bazėje, kviesti API, siųsti žinutę.

- **Priėjimas prie įrankių** — kokius įrankius agentas gali naudoti, priklauso nuo (1) aplinkos, kurioje jis veikia, ir (2) ką kūrėjas jam suteikė. Kelionių agentas gali ieškoti skrydžių, bet negali redaguoti klientų įrašų — svarbu kokius sujungiate įrankius.

- **Atmintis ir žinios** — Agentai gali turėti trumpalaikę atmintį (esamą pokalbį) ir ilgalaikę atmintį (klientų duomenų bazę, ankstesnius sąveikas). Kelionių agentas gali „prisiminti“, kad jums patinka vietos prie lango.

---

### Skirtingi AI agentų tipai

Ne visi agentai kuriami vienodai. Štai pagrindinių tipų apžvalga, naudojant kelionių užsakymo agentą kaip pavyzdį:

| **Agentų tipas** | **Ką jie daro** | **Kelionių agento pavyzdys** |
|---|---|---|
| **Paprasti refleksiniai agentai** | Laikosi griežtai užkoduotų taisyklių — neturi atminties, neplanuoja. | Pamato skundo el. laišką → persiunčia klientų aptarnavimui. Viskas. |
| **Modelio pagrindu veikiantys refleksiniai agentai** | Laiko vidaus pasaulio modelį ir atnaujina jį keičiantis situacijai. | Stebi istorinės skrydžių kainos ir pažymi staigiai pabrangusias kryptis. |
| **Tikslą turintys agentai** | Turi tikslą ir žingsnis po žingsnio planuoja, kaip jį pasiekti. | Užsako visą kelionę (skrydžius, automobilį, viešbutį) nuo jūsų vietos iki tikslo. |
| **Naudingumo pagrindu veikiantys agentai** | Ne tik randa *bet kokį* sprendimą — ieško *geriausio* svarstydami kompromisus. | Balansuoja kainą ir patogumą, kad rastų geriausiai jūsų pageidavimus atitinkančią kelionę. |
| **Mokymosi agentai** | Tobulėja laikui bėgant mokydamiesi iš atsiliepimų. | Tolių rekomendacijas koreguoja pagal apklausas po kelionės. |
| **Hierarchiniai agentai** | Aukšto lygio agentas suskaido darbą į potaskius ir paskirsto juos žemesnio lygio agentams. | „Atšaukti kelionę“ užklausa suskirstoma: atšaukti skrydį, atšaukti viešbutį, atšaukti automobilių nuomą — kiekvieną atlieka potagentas. |
| **Daugiagentinės sistemos (MAS)** | Keli nepriklausomi agentai dirba kartu (arba konkuruoja). | Bendradarbiaujantys: atskiri agentai rūpinasi viešbučiais, skrydžiais ir pramogomis. Konkuruojantys: keli agentai varžosi užpildyti viešbučių kambarius už geriausią kainą. |

---

## Kada naudoti AI agentus

Ne visada, kai galite naudoti AI agentą, verta tai daryti. Štai situacijos, kai agentai iš tikrųjų pranašauja:

![Kada naudoti AI agentus?](../../../translated_images/lt/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Atviri problemų sprendimai** — kai problemos sprendimo žingsnių neįmanoma iš anksto užprogramuoti. LLM turi dinamiškai nustatyti kelią.
- **Daugiažingsniai procesai** — užduotys, kur reikia naudoti įrankius per kelis etapus, ne tik vienkartinį duomenų ieškojimą ar generavimą.
- **Tobulėjimas laikui bėgant** — kai sistema turi tapti protingesnė pagal naudotojo atsiliepimus ar aplinkos signalus.

Išsamiau nagrinėsime, kada (ir kada *ne*) vertėtų naudoti AI agentus pamokoje **Patikimų AI agentų kūrimas** vėlesniuose kurso moduliuose.

---

## Agentinių sprendimų pagrindai

### Agentų kūrimas

Pirmas žingsnis kuriant agentą yra apibrėžti *ką jis gali daryti* — jo įrankius, veiksmus ir elgesį.

Šiame kurse pagrindine platforma naudojame **Azure AI Agent Service**. Ji palaiko:

- Atvirus modelius kaip OpenAI, Mistral ir Llama
- Licencijuotus duomenis iš tiekėjų kaip Tripadvisor
- Standartizuotus OpenAPI 3.0 įrankių aprašymus

### Agentinės schemos

Bendravimas su LLM vyksta per užklausas (promptus). Su agentais ne visuomet įmanoma rankiniu būdu parengti kiekvieną užklausą — agentas turi imtis veiksmų daugelyje žingsnių. Štai kur pasitelkiamos **agentinės schemos**. Tai pakartotinai naudojamos strategijos LLM paskatinimui ir koordinavimui, leidžiančios kurti patikimesnius ir lengviau plečiamus sprendimus.

Šis kursas sukurtas remiantis dažniausiai naudojamomis ir naudingiausiomis agentinėmis schemomis.

### Agentinės sistemos karkasai

Agentinės sistemos karkasai suteikia kūrėjams paruoštus šablonus, įrankius ir infrastruktūrą agentų kūrimui. Jie palengvina:

- Įrankių ir funkcijų sujungimą
- Stebėjimą, ką agentas daro (ir gedimų diagnozę)
- Dalyvavimą keliems agentams kartu dirbant

Šiame kurse daugiausia dėmesio skiriama **Microsoft Agent Framework (MAF)**, skirtam pramonės standartų agentų kūrimui.

---

## Kodo pavyzdžiai

Norite pamatyti veikimą? Štai šios pamokos kodo pavyzdžiai:

- 🐍 Python: [Agent framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent framework](./code_samples/01-dotnet-agent-framework.md)

---

## Turite klausimų?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), bendraukite su kitais mokiniais, dalyvaukite konsultacijose ir gaukite atsakymus apie AI agentus iš bendruomenės.

---

## Ankstesnė pamoka

[Kurso pradžia](../00-course-setup/README.md)

## Kitas pamoka

[Agentinių sistemų apžvalga](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas gimtąja kalba laikomas autoritetingu šaltiniu. Kritiniais atvejais rekomenduojamas profesionalus žmogaus atliktas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->