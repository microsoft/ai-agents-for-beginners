<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-30T14:49:51+00:00",
  "source_file": "11-agentic-protocols/code_samples/mcp-agents/README.md",
  "language_code": "lt"
}
-->
# Agentų tarpusavio komunikacijos sistemų kūrimas su MCP

> TL;DR - Ar galite sukurti Agent2Agent komunikaciją naudojant MCP? Taip!

MCP gerokai išsivystė nuo savo pradinio tikslo „suteikti kontekstą LLM“. Su naujausiais patobulinimais, tokiais kaip [atnaujinamos srautai](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) ir pranešimai ([progresas](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) ir [ištekliai](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)), MCP dabar suteikia tvirtą pagrindą sudėtingų agentų tarpusavio komunikacijos sistemų kūrimui.

## Agentas/Įrankis klaidinga samprata

Kai vis daugiau kūrėjų tyrinėja įrankius su agentiniais elgesiais (veikia ilgą laiką, gali prireikti papildomos informacijos vykdymo metu ir pan.), dažnai klaidingai manoma, kad MCP netinkamas, nes ankstyvieji jo įrankių pavyzdžiai buvo orientuoti į paprastus užklausos-atsakymo modelius.

Šis suvokimas yra pasenęs. MCP specifikacija per pastaruosius kelis mėnesius buvo žymiai patobulinta, kad užpildytų spragas, leidžiančias kurti ilgalaikį agentinį elgesį:

- **Srautai ir daliniai rezultatai**: realaus laiko progreso atnaujinimai vykdymo metu
- **Atnaujinamumas**: klientai gali prisijungti iš naujo ir tęsti po atsijungimo
- **Patvarumas**: rezultatai išlieka po serverio perkrovimo (pvz., per išteklių nuorodas)
- **Daugkartiniai posūkiai**: interaktyvus įvestis vykdymo metu per elicitation ir sampling

Šios funkcijos gali būti suderintos, kad būtų galima kurti sudėtingas agentines ir daugiagentines programas, visas diegiamas MCP protokole.

Šiame kontekste agentą vadinsime „įrankiu“, kuris yra prieinamas MCP serveryje. Tai reiškia, kad egzistuoja pagrindinė programa, kuri įgyvendina MCP klientą, užmezga sesiją su MCP serveriu ir gali iškviesti agentą.

## Kas daro MCP įrankį „agentiniu“?

Prieš pereinant prie įgyvendinimo, apibrėžkime, kokių infrastruktūros galimybių reikia, kad būtų palaikomi ilgalaikiai agentai.

> Agentą apibrėšime kaip subjektą, kuris gali veikti savarankiškai ilgą laiką, gebantį atlikti sudėtingas užduotis, kurioms gali prireikti kelių sąveikų ar korekcijų, remiantis realaus laiko grįžtamuoju ryšiu.

### 1. Srautai ir daliniai rezultatai

Tradiciniai užklausos-atsakymo modeliai neveikia ilgalaikėms užduotims. Agentai turi teikti:

- Realiojo laiko progreso atnaujinimus
- Tarpinius rezultatus

**MCP palaikymas**: Išteklių atnaujinimo pranešimai leidžia srautinius dalinius rezultatus, nors tai reikalauja kruopštaus dizaino, kad būtų išvengta konfliktų su JSON-RPC 1:1 užklausos/atsakymo modeliu.

| Funkcija                  | Naudojimo atvejis                                                                                                                                                                       | MCP palaikymas                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Realiojo laiko progreso atnaujinimai | Vartotojas prašo kodų bazės migracijos užduoties. Agentas srautiniu būdu teikia progresą: „10% - Analizuojamos priklausomybės... 25% - Konvertuojami TypeScript failai... 50% - Atnaujinami importai...“          | ✅ Progreso pranešimai                                                                  |
| Daliniai rezultatai            | „Sukurti knygą“ užduotis srautiniu būdu teikia dalinius rezultatus, pvz., 1) Istorijos arkos kontūras, 2) Skyrių sąrašas, 3) Kiekvienas skyrius, kai baigtas. Pagrindinė programa gali peržiūrėti, atšaukti ar nukreipti bet kuriame etape. | ✅ Pranešimai gali būti „išplėsti“, kad apimtų dalinius rezultatus, žr. pasiūlymus PR 383, 776 |

### 2. Atnaujinamumas

Agentai turi tvarkyti tinklo pertraukimus be problemų:

- Prisijungti iš naujo po (kliento) atsijungimo
- Tęsti nuo ten, kur buvo sustota (pranešimų pakartotinis pristatymas)

**MCP palaikymas**: MCP StreamableHTTP transportas šiandien palaiko sesijos atnaujinimą ir pranešimų pakartotinį pristatymą naudojant sesijos ID ir paskutinių įvykių ID. Svarbu pažymėti, kad serveris turi įgyvendinti EventStore, kuris leidžia pakartoti įvykius klientui prisijungus iš naujo.  
Atkreipkite dėmesį, kad yra bendruomenės pasiūlymas (PR #975), kuris tiria transportui nepriklausomus atnaujinamus srautus.

| Funkcija      | Naudojimo atvejis                                                                                                                                                   | MCP palaikymas                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Atnaujinamumas | Klientas atsijungia vykdant ilgalaikę užduotį. Prisijungus iš naujo, sesija atnaujinama su praleistais įvykiais, tęsiant sklandžiai nuo ten, kur buvo sustota. | ✅ StreamableHTTP transportas su sesijos ID, įvykių pakartojimu ir EventStore |

### 3. Patvarumas

Ilgalaikiai agentai turi turėti nuolatinę būseną:

- Rezultatai išlieka po serverio perkrovimo
- Būseną galima gauti neprisijungus
- Progreso stebėjimas tarp sesijų

**MCP palaikymas**: MCP dabar palaiko Išteklių nuorodų grąžinimo tipą įrankių iškvietimams. Šiandien galimas modelis yra sukurti įrankį, kuris sukuria išteklių ir iškart grąžina išteklių nuorodą. Įrankis gali toliau spręsti užduotį fone ir atnaujinti išteklių. Klientas gali pasirinkti tikrinti šio ištekliaus būseną, kad gautų dalinius ar pilnus rezultatus (remiantis tuo, kokius išteklių atnaujinimus serveris teikia) arba prenumeruoti išteklių atnaujinimo pranešimus.

### 4. Daugkartinės sąveikos

Agentams dažnai reikia papildomos informacijos vykdymo metu:

- Žmogaus patikslinimo ar patvirtinimo
- AI pagalbos sudėtingiems sprendimams
- Dinaminio parametrų koregavimo

**MCP palaikymas**: Pilnai palaikoma per sampling (AI įvestis) ir elicitation (žmogaus įvestis).

## Ilgalaikių agentų įgyvendinimas MCP - kodo apžvalga

Šiame straipsnyje pateikiame [kodo saugyklą](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents), kurioje yra pilnas ilgalaikių agentų įgyvendinimas naudojant MCP Python SDK su StreamableHTTP transportu sesijos atnaujinimui ir pranešimų pakartotiniam pristatymui. 

## Išvada

MCP patobulintos galimybės - išteklių pranešimai, elicitation/sampling, atnaujinami srautai ir nuolatiniai ištekliai - leidžia sudėtingas agentų tarpusavio sąveikas, išlaikant protokolo paprastumą.

## Pradžia

Pasiruošę kurti savo agent2agent sistemą? Sekite šiuos žingsnius:

### 1. Paleiskite demonstraciją

### 2. Išbandykite atnaujinimo galimybes

### 3. Tyrinėkite ir plėskite

Tai parodo, kaip MCP leidžia intelektualų agentų elgesį, išlaikant įrankių paprastumą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.