<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:56:28+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "lt"
}
-->
# Naudojant Agentinius Protokolus (MCP, A2A ir NLWeb)

[![Agentiniai Protokolai](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.lt.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Spustelėkite paveikslėlį aukščiau, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Didėjant dirbtinio intelekto agentų naudojimui, auga ir poreikis protokolams, kurie užtikrintų standartizaciją, saugumą ir palaikytų atvirą inovaciją. Šioje pamokoje aptarsime 3 protokolus, kurie siekia patenkinti šį poreikį – Modelio Konteksto Protokolas (MCP), Agentas Agentui (A2A) ir Natūralios Kalbos Tinklas (NLWeb).

## Įvadas

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia dirbtinio intelekto agentams pasiekti išorinius įrankius ir duomenis, kad atliktų vartotojo užduotis.

• Kaip **A2A** suteikia galimybę skirtingiems dirbtinio intelekto agentams bendrauti ir bendradarbiauti.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriai svetainei, leidžiant dirbtinio intelekto agentams atrasti ir sąveikauti su turiniu.

## Mokymosi tikslai

• **Identifikuoti** pagrindinę MCP, A2A ir NLWeb paskirtį bei naudą dirbtinio intelekto agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina komunikaciją ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Atpažinti** skirtingus vaidmenis, kuriuos kiekvienas protokolas atlieka kuriant sudėtingas agentines sistemas.

## Modelio Konteksto Protokolas

**Modelio Konteksto Protokolas (MCP)** yra atviras standartas, kuris suteikia standartizuotą būdą programoms pateikti kontekstą ir įrankius LLM. Tai leidžia sukurti „universalią jungtį“ skirtingiems duomenų šaltiniams ir įrankiams, prie kurių dirbtinio intelekto agentai gali prisijungti nuosekliai.

Pažvelkime į MCP komponentus, privalumus, palyginti su tiesioginiu API naudojimu, ir pavyzdį, kaip dirbtinio intelekto agentai gali naudoti MCP serverį.

### MCP Pagrindiniai Komponentai

MCP veikia pagal **kliento-serverio architektūrą**, o pagrindiniai komponentai yra:

• **Hostai** – tai LLM programos (pvz., kodų redaktorius kaip VSCode), kurios inicijuoja ryšius su MCP serveriu.

• **Klientai** – tai komponentai hosto programoje, kurie palaiko vienas su vienu ryšius su serveriais.

• **Serveriai** – tai lengvos programos, kurios atskleidžia specifinius pajėgumus.

Protokole yra trys pagrindiniai primityvai, kurie apibrėžia MCP serverio pajėgumus:

• **Įrankiai**: Tai atskiros funkcijos ar veiksmai, kuriuos dirbtinio intelekto agentas gali iškviesti, kad atliktų veiksmą. Pavyzdžiui, orų tarnyba gali pateikti „gauti orus“ įrankį, o e. prekybos serveris – „pirkti produktą“ įrankį. MCP serveriai reklamuoja kiekvieno įrankio pavadinimą, aprašymą ir įvesties/išvesties schemą savo pajėgumų sąraše.

• **Ištekliai**: Tai tik skaitymui skirti duomenų elementai ar dokumentai, kuriuos MCP serveris gali pateikti, o klientai gali juos gauti pagal poreikį. Pavyzdžiai: failų turinys, duomenų bazės įrašai ar žurnalų failai. Ištekliai gali būti tekstiniai (pvz., kodas ar JSON) arba dvejetainiai (pvz., vaizdai ar PDF).

• **Šablonai**: Tai iš anksto apibrėžti šablonai, kurie pateikia siūlomus raginimus, leidžiantys sudėtingesnius darbo procesus.

### MCP Privalumai

MCP suteikia reikšmingų privalumų dirbtinio intelekto agentams:

• **Dinaminis Įrankių Atradimas**: Agentai gali dinamiškai gauti serverio siūlomų įrankių sąrašą kartu su jų aprašymais. Tai skiriasi nuo tradicinių API, kurios dažnai reikalauja statinio kodavimo integracijoms, o bet kokie API pakeitimai reikalauja kodo atnaujinimų. MCP siūlo „integruoti vieną kartą“ metodą, kuris suteikia didesnį prisitaikymą.

• **Suderinamumas Tarp LLM**: MCP veikia su skirtingais LLM, suteikdamas lankstumą keisti pagrindinius modelius, kad būtų galima įvertinti geresnį našumą.

• **Standartizuotas Saugumas**: MCP apima standartinį autentifikavimo metodą, kuris palengvina mastelio didinimą, kai pridedama prieiga prie papildomų MCP serverių. Tai paprasčiau nei valdyti skirtingus raktus ir autentifikavimo tipus įvairiems tradiciniams API.

### MCP Pavyzdys

![MCP Diagrama](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.lt.png)

Įsivaizduokite, kad vartotojas nori užsisakyti skrydį naudodamas dirbtinio intelekto asistentą, kuris naudoja MCP.

1. **Ryšys**: Dirbtinio intelekto asistentas (MCP klientas) prisijungia prie MCP serverio, kurį teikia oro linijos.

2. **Įrankių Atradimas**: Klientas klausia oro linijų MCP serverio: „Kokius įrankius turite?“ Serveris atsako su tokiais įrankiais kaip „ieškoti skrydžių“ ir „užsakyti skrydžius“.

3. **Įrankio Iškvietimas**: Tada jūs paprašote dirbtinio intelekto asistento: „Prašau surasti skrydį iš Portlando į Honolulu.“ Dirbtinio intelekto asistentas, naudodamas savo LLM, nustato, kad reikia iškviesti „ieškoti skrydžių“ įrankį ir perduoda atitinkamus parametrus (išvykimo vieta, kelionės tikslas) MCP serveriui.

4. **Vykdymas ir Atsakymas**: MCP serveris, veikiantis kaip apvalkalas, atlieka faktinį skambutį į oro linijų vidinį užsakymo API. Tada jis gauna skrydžio informaciją (pvz., JSON duomenis) ir siunčia ją atgal dirbtinio intelekto asistentui.

5. **Tolimesnė Sąveika**: Dirbtinio intelekto asistentas pateikia skrydžio pasirinkimus. Kai pasirinksite skrydį, asistentas gali iškviesti „užsakyti skrydį“ įrankį tame pačiame MCP serveryje, užbaigdamas užsakymą.

## Agentas Agentui Protokolas (A2A)

Nors MCP orientuojasi į LLM ryšį su įrankiais, **Agentas Agentui (A2A) protokolas** žengia dar toliau, suteikdamas galimybę skirtingiems dirbtinio intelekto agentams bendrauti ir bendradarbiauti. A2A jungia dirbtinio intelekto agentus iš skirtingų organizacijų, aplinkų ir technologijų, kad atliktų bendrą užduotį.

Aptarsime A2A komponentus ir privalumus, kartu su pavyzdžiu, kaip jis galėtų būti pritaikytas mūsų kelionių programoje.

### A2A Pagrindiniai Komponentai

A2A orientuojasi į agentų komunikacijos galimybes ir jų bendradarbiavimą atliekant vartotojo užduotį. Kiekvienas protokolo komponentas prisideda prie šio proceso:

#### Agentų Kortelė

Panašiai kaip MCP serveris dalijasi įrankių sąrašu, Agentų Kortelė turi:
- Agentų pavadinimą.
- **Bendro pobūdžio užduočių aprašymą**, kurias jis atlieka.
- **Specifinių įgūdžių sąrašą** su aprašymais, kad kiti agentai (ar net žmonės) suprastų, kada ir kodėl jie norėtų iškviesti tą agentą.
- **Dabartinį agento URL adresą**.
- **Versiją** ir **pajėgumus**, tokius kaip srautinių atsakymų ir pranešimų siuntimas.

#### Agentų Vykdytojas

Agentų Vykdytojas yra atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, kad šis suprastų, kokią užduotį reikia atlikti. A2A serveryje agentas naudoja savo LLM, kad analizuotų gaunamus prašymus ir vykdytų užduotis naudodamas savo vidinius įrankius.

#### Artefaktas

Kai nuotolinis agentas užbaigia prašomą užduotį, jo darbo produktas sukuriamas kaip artefaktas. Artefaktas **turi agento atlikto darbo rezultatą**, **aprašymą, kas buvo atlikta**, ir **tekstinį kontekstą**, kuris perduodamas per protokolą. Po artefakto perdavimo ryšys su nuotoliniu agentu uždaromas, kol jo vėl prireiks.

#### Įvykių Eilė

Šis komponentas naudojamas **atnaujinimų valdymui ir pranešimų perdavimui**. Tai ypač svarbu gamyboje, kad agentų sistemos ryšys nebūtų uždaromas prieš užduoties užbaigimą, ypač kai užduočių atlikimo laikas gali būti ilgesnis.

### A2A Privalumai

• **Pagerintas Bendradarbiavimas**: Leidžia agentams iš skirtingų tiekėjų ir platformų bendrauti, dalintis kontekstu ir dirbti kartu, palengvinant automatizaciją tarp tradiciškai nesusijusių sistemų.

• **Modelio Pasirinkimo Lankstumas**: Kiekvienas A2A agentas gali nuspręsti, kurį LLM naudoti savo prašymams aptarnauti, leidžiant optimizuoti ar pritaikyti modelius pagal agentą, skirtingai nei vieno LLM ryšys kai kuriose MCP situacijose.

• **Integruotas Autentifikavimas**: Autentifikavimas tiesiogiai integruotas į A2A protokolą, suteikiant tvirtą saugumo sistemą agentų sąveikai.

### A2A Pavyzdys

![A2A Diagrama](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.lt.png)

Išplėskime mūsų kelionių užsakymo scenarijų, bet šį kartą naudodami A2A.

1. **Vartotojo Prašymas Multi-Agentui**: Vartotojas bendrauja su „Kelionių Agentu“ A2A klientu/agentu, galbūt sakydamas: „Prašau užsakyti visą kelionę į Honolulu kitai savaitei, įskaitant skrydžius, viešbutį ir automobilio nuomą.“

2. **Kelionių Agentas Orkestruoja**: Kelionių Agentas gauna šį sudėtingą prašymą. Jis naudoja savo LLM, kad suprastų užduotį ir nustatytų, jog reikia bendrauti su kitais specializuotais agentais.

3. **Tarpagentinė Komunikacija**: Kelionių Agentas tada naudoja A2A protokolą, kad prisijungtų prie žemyninių agentų, tokių kaip „Oro Linijų Agentas“, „Viešbučių Agentas“ ir „Automobilių Nuomos Agentas“, kurie sukurti skirtingų kompanijų.

4. **Deleguotas Užduočių Vykdymas**: Kelionių Agentas siunčia specifines užduotis šiems specializuotiems agentams (pvz., „Raskite skrydžius į Honolulu“, „Užsakykite viešbutį“, „Išnuomokite automobilį“). Kiekvienas iš šių specializuotų agentų, naudodamas savo LLM ir vidinius įrankius (kurie gali būti MCP serveriai), atlieka savo specifinę užsakymo dalį.

5. **Sujungtas Atsakymas**: Kai visi žemyniniai agentai užbaigia savo užduotis, Kelionių Agentas sujungia rezultatus (skrydžio detales, viešbučio patvirtinimą, automobilio nuomos užsakymą) ir pateikia išsamų, pokalbio stiliaus atsakymą vartotojui.

## Natūralios Kalbos Tinklas (NLWeb)

Svetainės jau seniai yra pagrindinis būdas vartotojams pasiekti informaciją ir duomenis internete.

Pažvelkime į skirtingus NLWeb komponentus, NLWeb privalumus ir pavyzdį, kaip NLWeb veikia mūsų kelionių programoje.

### NLWeb Komponentai

- **NLWeb Programėlė (Pagrindinis Paslaugos Kodas)**: Sistema, kuri apdoroja natūralios kalbos klausimus. Ji jungia skirtingas platformos dalis, kad sukurtų atsakymus. Galite ją laikyti **varikliu, kuris maitina natūralios kalbos funkcijas** svetainėje.

- **NLWeb Protokolas**: Tai **pagrindinis taisyklių rinkinys natūralios kalbos sąveikai** su svetaine. Jis grąžina atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pagrindą „AI Tinklui“, taip kaip HTML padarė įmanomą dokumentų dalijimąsi internete.

- **MCP Serveris (Modelio Konteksto Protokolo Galinis Taškas)**: Kiekviena NLWeb konfigūracija taip pat veikia kaip **MCP serveris**. Tai reiškia, kad ji gali **dalintis įrankiais (pvz., „klausti“ metodu) ir duomenimis** su kitomis dirbtinio intelekto sistemomis. Praktikoje tai leidžia svetainės turinį ir galimybes naudoti dirbtinio intelekto agentams, leidžiant svetainei tapti platesnės „agentų ekosistemos“ dalimi.

- **Įterpimo Modeliai**: Šie modeliai naudojami **konvertuoti svetainės turinį į skaitines reprezentacijas, vadinamas vektoriais** (įterpimais). Šie vektoriai užfiksuoja prasmę taip, kad kompiuteriai galėtų palyginti ir ieškoti. Jie saugomi specialioje duomenų bazėje, o vartotojai gali pasirinkti, kurį įterpimo modelį naudoti.

- **Vektorinė Duomenų Bazė (Paieškos Mechanizmas)**: Ši duomenų bazė **saugo svetainės turinio įterpimus**. Kai kas nors užduoda klausimą, NLWeb patikrina vektorinę duomenų bazę, kad greitai rastų tinkamiausią informaciją. Ji pateikia greitą galimų atsakymų sąrašą, surūšiuotą pagal panašumą. NLWeb veikia su skirtingomis vektorinėmis saugojimo sistemomis, tokiomis kaip Qdrant, Snowflake, Milvus, Azure AI Search ir Elasticsearch.

### NLWeb Pavyzdys

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.lt.png)

Apsvarstykime mūsų kelionių užsakymo svetainę, bet šį kartą ji veikia su NLWeb.

1. **Duomenų Įkėlimas**: Kelionių svetainės esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, kelionių paketai) yra formatuojami naudojant Schema.org arba įkeliami per RSS srautus. NLWeb įrankiai įkelia šiuos struktūrizuotus duomenis, sukuria įterpimus ir saugo juos vietinėje arba nuotolinėje vektorinėje duomenų bazėje.

2. **Natūralios Kalbos Užklausa (Žmogus)**: Vartotojas apsilanko svetainėje ir, užuot naršęs meniu, įveda į pokalbio sąsają: „Raskite šeimai draugišką viešbutį Honolulu su baseinu kitai savaitei“.

3. **NLWeb Apdorojimas**: NLWeb programėlė gauna šią užklausą. Ji siunčia užklausą LLM, kad suprastų, ir tuo pačiu metu ieško savo vektorinėje duomenų bazėje tinkamų viešbučių sąrašų.

4. **Tikslūs Rezultatai**:

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.