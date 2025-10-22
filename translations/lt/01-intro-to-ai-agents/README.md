<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-30T14:32:28+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "lt"
}
-->
[![Intro to AI Agents](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.lt.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Spustelėkite paveikslėlį aukščiau, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Įvadas į AI agentus ir jų panaudojimo atvejus

Sveiki atvykę į kursą „AI agentai pradedantiesiems“! Šis kursas suteikia pagrindines žinias ir praktinius pavyzdžius, kaip kurti AI agentus.

Prisijunkite prie bendruomenės, kad susipažintumėte su kitais mokiniais ir AI agentų kūrėjais bei užduotumėte klausimus, susijusius su šiuo kursu.

Pradėdami kursą, pirmiausia geriau suprasime, kas yra AI agentai ir kaip juos galime panaudoti kuriant programas bei darbo eigas.

## Įvadas

Šioje pamokoje aptariama:

- Kas yra AI agentai ir kokie yra jų tipai?
- Kokie panaudojimo atvejai geriausiai tinka AI agentams ir kaip jie gali mums padėti?
- Kokie yra pagrindiniai elementai, kuriant agentinius sprendimus?

## Mokymosi tikslai
Baigę šią pamoką, turėtumėte:

- Suprasti AI agentų koncepcijas ir kuo jie skiriasi nuo kitų AI sprendimų.
- Efektyviai taikyti AI agentus.
- Produktyviai kurti agentinius sprendimus tiek vartotojams, tiek klientams.

## AI agentų apibrėžimas ir tipai

### Kas yra AI agentai?

AI agentai yra **sistemos**, kurios leidžia **dideliems kalbos modeliams (LLMs)** **atlikti veiksmus**, išplečiant jų galimybes suteikiant jiems **prieigą prie įrankių** ir **žinių**.

Išskaidykime šį apibrėžimą į mažesnes dalis:

- **Sistema** – Svarbu galvoti apie agentus ne kaip apie vieną komponentą, o kaip apie daugelio komponentų sistemą. Pagrindiniai AI agento komponentai yra:
  - **Aplinka** – Apibrėžta erdvė, kurioje veikia AI agentas. Pavyzdžiui, jei turėtume kelionių rezervavimo AI agentą, aplinka galėtų būti kelionių rezervavimo sistema, kurią agentas naudoja užduotims atlikti.
  - **Jutikliai** – Aplinka turi informaciją ir teikia grįžtamąjį ryšį. AI agentai naudoja jutiklius, kad surinktų ir interpretuotų informaciją apie dabartinę aplinkos būseną. Kelionių rezervavimo agento pavyzdyje sistema gali pateikti informaciją, pvz., viešbučių prieinamumą ar skrydžių kainas.
  - **Aktuatoriai** – Gavęs dabartinę aplinkos būseną, agentas nustato, kokį veiksmą atlikti, kad pakeistų aplinką. Kelionių rezervavimo agento atveju tai galėtų būti viešbučio kambario rezervavimas vartotojui.

![Kas yra AI agentai?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.lt.png)

**Dideli kalbos modeliai** – Agentų koncepcija egzistavo dar prieš LLM sukūrimą. AI agentų kūrimo su LLM privalumas yra jų gebėjimas interpretuoti žmogaus kalbą ir duomenis. Šis gebėjimas leidžia LLM interpretuoti aplinkos informaciją ir apibrėžti planą, kaip pakeisti aplinką.

**Veiksmų atlikimas** – Už AI agentų sistemų ribų LLM yra riboti situacijose, kur veiksmas yra turinio ar informacijos generavimas pagal vartotojo užklausą. AI agentų sistemose LLM gali atlikti užduotis interpretuodami vartotojo prašymą ir naudodami įrankius, prieinamus jų aplinkoje.

**Prieiga prie įrankių** – Kokius įrankius LLM turi, priklauso nuo 1) aplinkos, kurioje jis veikia, ir 2) AI agento kūrėjo. Mūsų kelionių agento pavyzdyje agento įrankiai yra riboti pagal rezervavimo sistemos operacijas, o kūrėjas gali apriboti agento prieigą prie skrydžių.

**Atmintis + žinios** – Atmintis gali būti trumpalaikė, susijusi su pokalbio kontekstu tarp vartotojo ir agento. Ilgalaikėje perspektyvoje, be aplinkos teikiamos informacijos, AI agentai gali gauti žinių iš kitų sistemų, paslaugų, įrankių ir net kitų agentų. Kelionių agento pavyzdyje tai galėtų būti informacija apie vartotojo kelionių pageidavimus, esanti klientų duomenų bazėje.

### Skirtingi agentų tipai

Dabar, kai turime bendrą AI agentų apibrėžimą, pažvelkime į konkrečius agentų tipus ir kaip jie būtų taikomi kelionių rezervavimo AI agentui.

| **Agentų tipas**              | **Aprašymas**                                                                                                                        | **Pavyzdys**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Paprasti refleksiniai agentai** | Atlieka tiesioginius veiksmus pagal iš anksto nustatytas taisykles.                                                                 | Kelionių agentas interpretuoja el. laiško kontekstą ir persiunčia kelionių skundus klientų aptarnavimo skyriui.                                                                                                                |
| **Modeliu pagrįsti refleksiniai agentai** | Atlieka veiksmus remdamiesi pasaulio modeliu ir jo pokyčiais.                                                                      | Kelionių agentas teikia pirmenybę maršrutams, kuriuose pastebimi reikšmingi kainų pokyčiai, remdamasis prieiga prie istorinių kainų duomenų.                                                                                   |
| **Tikslų siekiantys agentai** | Sudaro planus, kaip pasiekti konkrečius tikslus, interpretuodami tikslą ir nustatydami veiksmus, reikalingus jam pasiekti.             | Kelionių agentas rezervuoja kelionę, nustatydamas reikalingus kelionės elementus (automobilį, viešąjį transportą, skrydžius) nuo dabartinės vietos iki kelionės tikslo.                                                         |
| **Naudingumo pagrindu veikiantys agentai** | Atsižvelgia į pageidavimus ir skaičiuoja kompromisus, kad nustatytų, kaip pasiekti tikslus.                                       | Kelionių agentas maksimaliai padidina naudingumą, vertindamas patogumą ir kainą, kai rezervuoja kelionę.                                                                                                                       |
| **Mokymosi agentai**          | Tobulėja laikui bėgant, reaguodami į grįžtamąjį ryšį ir atitinkamai koreguodami veiksmus.                                              | Kelionių agentas tobulėja, naudodamas klientų atsiliepimus iš apklausų po kelionės, kad atliktų korekcijas būsimuose rezervavimuose.                                                                                           |
| **Hierarchiniai agentai**     | Naudoja kelis agentus hierarchinėje sistemoje, kur aukštesnio lygio agentai suskaido užduotis į smulkesnes, kurias atlieka žemesnio lygio agentai. | Kelionių agentas atšaukia kelionę, suskaidydamas užduotį į smulkesnes (pvz., atšaukiant konkrečius rezervavimus) ir leisdamas žemesnio lygio agentams jas atlikti, pranešant aukštesnio lygio agentui.                             |
| **Daugiagentės sistemos (MAS)** | Agentai savarankiškai atlieka užduotis, bendradarbiaudami arba konkuruodami tarpusavyje.                                              | Bendradarbiavimas: keli agentai rezervuoja konkrečias kelionių paslaugas, tokias kaip viešbučiai, skrydžiai ir pramogos. Konkurencija: keli agentai valdo ir konkuruoja dėl bendro viešbučio rezervavimo kalendoriaus, kad užsakytų klientus į viešbutį. |

## Kada naudoti AI agentus

Ankstesniame skyriuje mes naudojome kelionių agento panaudojimo atvejį, kad paaiškintume, kaip skirtingi agentų tipai gali būti naudojami įvairiose kelionių rezervavimo scenarijose. Šį pavyzdį naudosime viso kurso metu.

Pažvelkime į panaudojimo atvejus, kuriems AI agentai yra geriausiai pritaikyti:

![Kada naudoti AI agentus?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.lt.png)

- **Atviri klausimai** – leidžiant LLM nustatyti reikalingus veiksmus užduočiai atlikti, nes jų ne visada galima iš anksto užkoduoti darbo eigoje.
- **Daugiapakopiai procesai** – užduotys, kurioms reikia tam tikro sudėtingumo lygio, kai AI agentas turi naudoti įrankius ar informaciją per kelis žingsnius, o ne vienkartinį duomenų gavimą.
- **Tobulėjimas laikui bėgant** – užduotys, kuriose agentas gali tobulėti laikui bėgant, gaudamas grįžtamąjį ryšį iš aplinkos ar vartotojų, kad suteiktų didesnę naudą.

Daugiau apie AI agentų naudojimo aspektus aptarsime pamokoje „Patikimų AI agentų kūrimas“.

## Agentinių sprendimų pagrindai

### Agentų kūrimas

Pirmasis žingsnis kuriant AI agentų sistemą yra apibrėžti įrankius, veiksmus ir elgesį. Šiame kurse mes sutelkiame dėmesį į **Azure AI Agent Service** naudojimą, kad apibrėžtume savo agentus. Ši paslauga siūlo tokias funkcijas kaip:

- Atvirų modelių, tokių kaip OpenAI, Mistral ir Llama, pasirinkimas
- Licencijuotų duomenų naudojimas per tiekėjus, tokius kaip Tripadvisor
- Standartizuotų OpenAPI 3.0 įrankių naudojimas

### Agentiniai šablonai

Bendravimas su LLM vyksta per užklausas. Atsižvelgiant į pusiau autonominį AI agentų pobūdį, ne visada įmanoma ar būtina rankiniu būdu pakartotinai užklausti LLM po aplinkos pokyčio. Naudojame **agentinius šablonus**, kurie leidžia užklausti LLM per kelis žingsnius labiau masteliniu būdu.

Šis kursas suskirstytas į kai kuriuos populiarius agentinius šablonus.

### Agentinės sistemos

Agentinės sistemos leidžia kūrėjams įgyvendinti agentinius šablonus per kodą. Šios sistemos siūlo šablonus, įskiepius ir įrankius geresniam AI agentų bendradarbiavimui. Šie privalumai suteikia galimybes geresniam AI agentų sistemų stebėjimui ir trikčių šalinimui.

Šiame kurse mes nagrinėsime moksliniais tyrimais pagrįstą AutoGen sistemą ir gamybai paruoštą Agent sistemą iš Semantic Kernel.

### Turite daugiau klausimų apie AI agentus?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susipažintumėte su kitais mokiniais, dalyvautumėte konsultacijų valandose ir gautumėte atsakymus į savo klausimus apie AI agentus.

## Ankstesnė pamoka

[Kurso nustatymas](../00-course-setup/README.md)

## Kita pamoka

[Agentinių sistemų tyrinėjimas](../02-explore-agentic-frameworks/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.