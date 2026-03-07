[![Įvadas į DI agentus](../../../translated_images/lt/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_


# Įvadas į DI agentus ir agentų naudojimo atvejus

Sveiki atvykę į kursą "AI Agents for Beginners"! Šis kursas suteikia pagrindines žinias ir praktinius pavyzdžius DI agentų kūrimui.

Prisijunkite prie <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a>, kad susipažintumėte su kitais besimokančiaisiais ir DI agentų kūrėjais bei užduotumėte bet kokius klausimus apie šį kursą.

Norėdami pradėti šį kursą, pradėsime nuo geresnio supratimo, kas yra DI agentai ir kaip juos galime naudoti kuriamuose taikymuose ir darbo srautuose.

## Įžanga

Ši pamoka apima:

- Kas yra DI agentai ir kokie yra skirtingi agentų tipai?
- Kokie naudojimo atvejai yra tinkamiausi DI agentams ir kaip jie gali mums padėti?
- Kokie yra pagrindiniai komponentai projektuojant agentinius sprendimus?

## Mokymosi tikslai
Baigę šią pamoką, turėtumėte sugebėti:

- Suprasti DI agentų koncepcijas ir kaip jos skiriasi nuo kitų DI sprendimų.
- Efektyviai taikyti DI agentus.
- Produktiškai projektuoti agentinius sprendimus tiek vartotojams, tiek klientams.

## DI agentų apibrėžimas ir DI agentų tipai

### Kas yra DI agentai?

DI agentai yra **sistemos**, kurios leidžia **Dideliems kalbos modeliams(LLMs)** **atlikti veiksmus**, išplečiant jų galimybes suteikiant LLMs **prieigą prie įrankių** ir **žinių**.

Suskaldykime šį apibrėžimą į mažesnes dalis:

- **Sistema** - Svarbu galvoti apie agentus ne tik kaip apie vieną komponentą, bet kaip apie daugelio komponentų sistemą. Pagrindiniu lygiu DI agente komponentai yra:
  - **Aplinka** - Apibrėžta erdvė, kurioje veikia DI agentas. Pavyzdžiui, jei turėtume kelionių rezervavimo DI agentą, aplinka galėtų būti kelionių rezervavimo sistema, kurią agentas naudoja užduotims atlikti.
  - **Jutikliai** - Aplinkoje yra informacija ir ji teikia atsiliepimus. DI agentai naudoja jutiklius rinkti ir interpretuoti informaciją apie dabartinę aplinkos būseną. Kelionių rezervavimo agente, rezervavimo sistema gali suteikti duomenis, tokius kaip viešbučio prieinamumas arba skrydžių kainos.
  - **Aktuatorių** - Kai DI agentas gauna dabartinę aplinkos būseną, už konkrečią užduotį agentas nustato, kokį veiksmą atlikti, kad pakeistų aplinką. Kelionių rezervavimo agentui tai gali būti prieinamo kambario rezervavimas vartotojui.

![Kas yra DI agentai?](../../../translated_images/lt/what-are-ai-agents.1ec8c4d548af601a.webp)

**Dideli kalbos modeliai** - Agentų koncepcija egzistavo dar prieš sukuriant LLM. Privalumas kuriant DI agentus su LLM yra jų gebėjimas interpretuoti žmogaus kalbą ir duomenis. Šis gebėjimas leidžia LLM interpretuoti aplinkos informaciją ir suformuluoti planą aplinkos pakeitimui.

**Veiksmų atlikimas** - Už agentinių sistemų ribų LLM yra riboti situacijose, kai veiksmas yra turinio ar informacijos generavimas pagal vartotojo užklausą. Agentinių sistemų viduje LLM gali įvykdyti užduotis interpretuodami vartotojo prašymą ir naudodami aplinkoje prieinamus įrankius.

**Prieiga prie įrankių** - Kokius įrankius LLM turi, nusako 1) aplinka, kurioje jis veikia, ir 2) DI agento kūrėjas. Mūsų kelionių agente, agento įrankiai yra ribojami rezervavimo sistemoje prieinamų operacijų, ir/arba kūrėjas gali apriboti agento prieigą prie konkrečių skrydžių.

**Atmintis + Žinios** - Atmintis gali būti trumpalaikė vartotojo ir agente vykstančios pokalbio kontekste. Ilgalaikėje perspektyvoje, nepriklausomai nuo aplinkos pateiktos informacijos, DI agentai taip pat gali gauti žinių iš kitų sistemų, paslaugų, įrankių ir net kitų agentų. Kelionių agente šiomis žiniomis gali būti vartotojo kelionių pageidavimų informacija, saugoma klientų duomenų bazėje.

### Skirtingi agentų tipai

Dabar, kai turime bendrą DI agentų apibrėžimą, pažvelkime į konkrečius agentų tipus ir kaip jie būtų pritaikyti kelionių rezervavimo DI agentui.

| **Agento tipas**                | **Aprašymas**                                                                                                                       | **Pavyzdys**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Paprasti refleksiniai agentai**      | Atlieka tiesioginius veiksmus pagal iš anksto apibrėžtas taisykles.                                                                                  | Kelionių agentas interpretuoja el. laiško kontekstą ir persiunčia kelionių skundus klientų aptarnavimo skyriui.                                                                                                                          |
| **Modeliuoti refleksiniai agentai** | Atlieka veiksmus remdamiesi pasaulio modeliu ir pokyčiais tame modelyje.                                                              | Kelionių agentas prioritetizuoja maršrutus su reikšmingais kainų pokyčiais, remdamasis prieiga prie istorinės kainų informacijos.                                                                                                             |
| **Tiksliniai agentai**         | Sudaro planus, kaip pasiekti konkrečius tikslus, interpretuodami tikslą ir nustatydami veiksmus jam pasiekti.                                  | Kelionių agentas rezervuoja kelionę nustatydamas reikalingus kelionės organizavimo veiksmus (automobilis, viešasis transportas, skrydžiai) iš dabartinės vietos iki kelionės tikslo.                                                                                |
| **Agentai, pagrįsti naudingumu**      | Apsvarsto nuostatas ir skaičiuoja kompromisus, kad nustatytų, kaip geriausiai pasiekti tikslus.                                               | Kelionių agentas maksimizuoja naudingumą, sverdamas patogumą prieš kainą rezervuodamas kelionę.                                                                                                                                          |
| **Mokymosi agentai**           | Tobulėja laikui bėgant reaguodami į atsiliepimus ir atitinkamai koreguodami veiksmus.                                                        | Kelionių agentas tobulėja naudodamas klientų atsiliepimus po kelionės iš apklausų, kad atliktų pakeitimus būsimose rezervacijose.                                                                                                               |
| **Hierarchiniai agentai**       | Turi kelis agentus sluoksniuotoje sistemoje, kur aukštesnio lygio agentai suskaido užduotis į potaskes, kurias vykdo žemesnio lygio agentai. | Kelionių agentas atšaukia kelionę suskaidydamas užduotį į potaskes (pavyzdžiui, atšaukti konkrečias rezervacijas) ir leisdamas žemesnio lygio agentams jas įvykdyti bei ataskaitą grąžinti aukštesnio lygio agentui.                                     |
| **Daugelio agentų sistemos (MAS)** | Agentai atlieka užduotis nepriklausomai, bendradarbiaudami arba konkuruodami.                                                           | Bendradarbiavimas: keli agentai rezervuoja konkrečias kelionės paslaugas, tokias kaip viešbučiai, skrydžiai ir pramogos. Konkurencija: keli agentai valdo ir konkuruoja dėl bendros viešbučio rezervacijų kalendoriaus, kad priskirtų klientus viešbučiui. |

## Kada naudoti DI agentus

Ankstesniame skyriuje mes naudojome kelionių agento naudojimo atvejį, kad paaiškintume, kaip skirtingi agentų tipai gali būti taikomi skirtinguose kelionių rezervavimo scenarijuose. Šį taikymą naudosime ir toliau per visą kursą.

Pažiūrėkime, kokiems naudojimo atvejams DI agentai tinka labiausiai:

![Kada naudoti DI agentus?](../../../translated_images/lt/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Atviros problemos** - leidžiant LLM nustatyti reikalingus žingsnius užduočiai atlikti, nes tai ne visada galima pilnai užkodinti į darbo srautą.
- **Daugiapakopiai procesai** - užduotys, reikalaujančios tam tikro sudėtingumo, kai DI agentui reikia naudoti įrankius arba informaciją per kelis etapus, o ne vienkartinį gavimą.  
- **Tobulėjimas laikui bėgant** - užduotys, kur agentas gali tobulėti laiko eigoje gaudamas atsiliepimus iš aplinkos ar vartotojų, kad suteiktų didesnę naudą.

Daugiau svarstymų apie DI agentų naudojimą aptariame pamokoje "Kuriant patikimus DI agentus".

## Agentinių sprendimų pagrindai

### Agentų kūrimas

Pirmasis žingsnis projektuojant DI agentų sistemą yra apibrėžti įrankius, veiksmus ir elgesį. Šiame kurse mes sutelkiame dėmesį į **Azure AI Agent Service** naudojimą agentų apibrėžimui. Jis siūlo funkcijas, tokias kaip:

- Atvirų modelių pasirinkimas, tokių kaip OpenAI, Mistral ir Llama
- Licencijuotų duomenų naudojimas per tiekėjus, tokius kaip Tripadvisor
- Standartizuotų OpenAPI 3.0 įrankių naudojimas

### Agentiniai šablonai

Bendravimas su LLM vyksta per užklausas (prompts). Atsižvelgiant į pusiau autonominę DI agentų prigimtį, ne visada yra įmanoma ar būtina rankiniu būdu pakartotinai užduoti užklausą LLM po aplinkos pasikeitimo. Naudojame **agentinius šablonus**, leidžiančius užklausti LLM per kelis etapus labiau išplečiamu būdu.

Šis kursas padalintas į kai kuriuos šiuo metu populiarius agentinius šablonus.

### Agentiniai karkasai

Agentiniai karkasai leidžia kūrėjams įgyvendinti agentinius šablonus per kodą. Šie karkasai siūlo šablonus, papildinius ir įrankius geresniam DI agentų bendradarbiavimui. Šios naudos suteikia galimybes geresnei stebėsenai ir trikčių šalinimui DI agentų sistemose.

Šiame kurse mes nagrinėsime Microsoft Agent Framework (MAF) skirtą produkcijai paruoštų DI agentų kūrimui.

## Kodo pavyzdžiai

- Python: [Agentų karkasas](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agentų karkasas](./code_samples/01-dotnet-agent-framework.md)

## Turite daugiau klausimų apie DI agentus?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitikti su kitais besimokančiaisiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į klausimus apie DI agentus.

## Ankstesnė pamoka

[Kurso nustatymai](../00-course-setup/README.md)

## Kita pamoka

[Agentinių karkasų tyrinėjimas](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas savo originalia kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl kritinės svarbos informacijos rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingas interpretacijas, atsiradusias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->