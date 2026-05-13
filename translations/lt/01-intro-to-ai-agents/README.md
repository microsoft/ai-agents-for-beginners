[![Intro to AI Agents](../../../translated_images/lt/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Spustelėkite aukščiau esantį paveikslėlį, jei norite peržiūrėti šios pamokos vaizdo įrašą)_

# Įvadas į DI agentus ir agentų naudojimo atvejus

Sveiki atvykę į **DI agentų pradedantiesiems** kursą! Šiame kurse gausite pagrindines žinias — ir realų veikiančio kodo — kad galėtumėte pradėti kurti DI agentus nuo nulio.

Ateikite pasisveikinti <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure DI Discord bendruomenėje</a> — čia pilna besimokančių ir DI kūrėjų, kurie mielai atsakys į jūsų klausimus.

Prieš pradedant kurti, įsitikinkime, kad tikrai suprantame, kas yra DI agentas ir kada prasminga jį naudoti.

---

## Įvadas

Ši pamoka apima:

- Kas yra DI agentai ir kokie yra jų skirtingi tipai
- Kokiems uždaviniams DI agentai tinka geriausiai
- Pagrindiniai elementai, kuriuos naudosite kurdami agentinį sprendimą

## Mokymosi tikslai

Pamokos pabaigoje turėtumėte sugebėti:

- Paaiškinti, kas yra DI agentas ir kuo jis skiriasi nuo įprasto DI sprendimo
- Žinoti, kada verta naudoti DI agentą (ir kada ne)
- Nubrėžti pagrindinį agentinio sprendimo dizainą realaus pasaulio problemai

---

## DI agentų apibrėžimas ir agentų tipai

### Kas yra DI agentai?

Štai paprastas būdas tai suprasti:

> **DI agentai yra sistemos, leidžiančios Didiesiems kalbos modeliams (LLM) iš tikrųjų *daryti veiksmus* — suteikiant jiems įrankius ir žinias veikti pasaulyje, o ne tik atsakyti į užklausas.**

Paaiškinkime tai plačiau:

- **Sistema** — DI agentas nėra tik viena dalis. Tai dalių rinkinys, veikiančių kartu. Pagrinde kiekvienas agentas turi tris dalis:
  - **Aplinka** — erdvė, kurioje agentas veikia. Kelionių rezervavimo agento atveju tai būtų pati rezervavimo platforma.
  - **Jutikliai** — kaip agentas skaito savo aplinkos dabartinę būseną. Mūsų kelionių agentas galėtų tikrinti viešbučių prieinamumą ar skrydžių kainas.
  - **Veikėjai** — kaip agentas imasi veiksmų. Kelionių agentas gali užsakyti kambarį, siųsti patvirtinimą ar atšaukti rezervaciją.

![What Are AI Agents?](../../../translated_images/lt/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Didieji kalbos modeliai** — agentai egzistavo ir prieš LLM, bet LLM padaro šiuolaikinius agentus tokiais galingais. Jie supranta natūralią kalbą, įvertina kontekstą ir iš neaiškios vartotojo užklausos sukuria konkretų veiksmų planą.

- **Atlikti veiksmus** — be agento sistemos LLM tik generuoja tekstą. Agentų sistemoje LLM gali iš tiesų *įvykdyti* veiksmus — ieškoti duomenų bazėje, kreiptis į API, siųsti žinutę.

- **Įrankių prieiga** — kokiais įrankiais agentas gali naudotis priklauso nuo (1) aplinkos, kurioje jis veikia, ir (2) ko kūrėjas jam suteikia. Kelionių agentas gali ieškoti skrydžių, bet negali keisti klientų įrašų — viskas priklauso nuo to, ką sujungi.

- **Atmintis + Žinios** — agentai gali turėti trumpalaikę atmintį (dabartinę pokalbio eigą) ir ilgalaikę atmintį (klientų duomenų bazę, praeitus pokalbius). Kelionių agentas gali „prisiminti“, kad jums patinka vietos prie lango.

---

### Skirtingi DI agentų tipai

Ne visi agentai sukurti vienodai. Štai pagrindinių tipų suskirstymas, naudojant kelionių agentą kaip pavyzdį:

| **Agento tipas** | **Ką jis daro** | **Kelionių agento pavyzdys** |
|---|---|---|
| **Paprasti refleksiniai agentai** | Laikosi iš anksto užkoduotų taisyklių — be atminties, be planavimo. | Pamato skundo el. laišką → perduoda klientų aptarnavimui. Viskas. |
| **Modeliu grįsti refleksiniai agentai** | Turi vidinį pasaulio modelį ir jį atnaujina, kai viskas keičiasi. | Stebi istorines skrydžių kainas ir pabrangusias maršrutus pažymi. |
| **Tikslų pagrindu veikiantys agentai** | Turi tikslą ir žingsnis po žingsnio sprendžia, kaip jo pasiekti. | Užsako visą kelionę (skrydžius, automobilį, viešbutį) nuo jūsų vietos iki kelionės tikslo. |
| **Naudų pagrindu veikiantys agentai** | Neranda tiesiog *sprendimo* — randa *geriausią* sprendimą, vertindami kompromisus. | Subalansuoja kainą ir patogumą, kad rastų kelionę, geriausiai atitinkančią jūsų pageidavimus. |
| **Mokymosi agentai** | Tobulėja laikui bėgant, mokydamiesi iš atsiliepimų. | Koreguoja būsimus užsakymų pasiūlymus pagal po kelionės surinktą apklausą. |
| **Hierarchiniai agentai** | Aukšto lygio agentas darbus skirsto į potaisykles ir deleguoja žemesnio lygio agentams. | Užklausa „atšaukti kelionę“ padalijama į: atšaukti skrydį, atšaukti viešbutį, atšaukti automobilio nuomą — kiekvieną tvarko subagentas. |
| **Daugiagentės sistemos (MAS)** | Kelios nepriklausomos agentų grupės dirba kartu (arba konkuruoja). | Bendradarbiaujantys: atskiri agentai tvarko viešbučius, skrydžius ir pramogas. Konkurencingi: keli agentai varžosi dėl geriausių viešbučių kainų. |

---

## Kada naudoti DI agentus

Tik todėl, kad galite naudoti DI agentą, nereiškia, kad visada turėtumėte. Štai situacijos, kur agentai iš tikrųjų pasiekia geriausių rezultatų:

![When to use AI Agents?](../../../translated_images/lt/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Atviros pabaigos problemos** — kai problemos sprendimo žingsnių negalima iš anksto programuoti. LLM turi dinamiškai surasti kelią.
- **Daugiapakopiai procesai** — užduotys, kurioms reikia naudoti įrankius per kelis žingsnius, ne tik vieną užklausą ar sugeneravimą.
- **Tobulėjimas laikui bėgant** — kai norite, kad sistema būtų protingesnė remdamasi naudotojų atsiliepimais ar aplinkos signalais.

Daugiau nagrinėsime, kada (ir kada *ne*) naudoti DI agentus pamokoje **Patikimų DI agentų kūrimas** vėliau kurso metu.

---

## Agentinių sprendimų pagrindai

### Agento kūrimas

Pirmas dalykas, kurį darote kurdami agentą, yra apibrėžti *ką jis gali daryti* — jo įrankius, veiksmus ir elgseną.

Šiame kurse mes naudojame **Azure DI agentų tarnybą** kaip pagrindinę platformą. Ji palaiko:

- Modelius iš tiekėjų, tokių kaip OpenAI, Mistral ir Meta (Llama)
- Licencijuotus duomenis iš tiekėjų, tokių kaip Tripadvisor
- Standartizuotus OpenAPI 3.0 įrankių apibrėžimus

### Agentinės struktūros

Bendraujate su LLM per užklausas. Su agentais ne visada įmanoma rankiniu būdu sukurti kiekvieną užklausą — agentas turi imtis veiksmų per kelis žingsnius. Čia praverčia **agentinės struktūros**. Tai daugkartinio naudojimo strategijos, skirtos užklausoms ir LLM koordinavimui patikimesniu ir labiau pritaikomu būdu.

Šis kursas grįstas dažniausiai pasitaikančiomis ir naudingiausiomis agentinėmis struktūromis.

### Agentinės platformos

Agentinės platformos suteikia kūrėjams paruoštus šablonus, įrankius ir infrastruktūrą agentų kūrimui. Jos palengvina:

- Įrankių ir gebėjimų sujungimą
- Stebėjimą, ką agentas veikia (ir klaidų taisymą, kai kas nors nepavyksta)
- Bendradarbiavimą keliose agentų grupėse

Šiame kurse daugiausia dėmesio skiriame **Microsoft Agent Framework (MAF)** kuriant gamybinės kokybės agentus.

---

## Kodo pavyzdžiai

Norite pamatyti veikimą? Štai šios pamokos kodo pavyzdžiai:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Turite klausimų?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susisiektumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus iš bendruomenės į savo DI agentų klausimus.

---

## Ankstesnė pamoka

[Kurso pradžia](../00-course-setup/README.md)

## Kita pamoka

[Agentinių platformų tyrinėjimas](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->