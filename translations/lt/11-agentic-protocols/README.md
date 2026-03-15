# Using Agentic Protocols (MCP, A2A and NLWeb)

[![Agentic Protocols](../../../translated_images/lt/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Kadangi AI agentų naudojimas auga, auga ir poreikis protokolams, kurie užtikrina standartizavimą, saugumą ir palaiko atvirą inovaciją. Šioje pamokoje aptarsime 3 protokolus, siekiančius tenkinti šį poreikį – Model Context Protocol (MCP), Agent to Agent (A2A) ir Natural Language Web (NLWeb).

## Introduction

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia AI agentams pasiekti išorinius įrankius ir duomenis, kad atliktų vartotojo užduotis.

• Kaip **A2A** leidžia skirtingiems AI agentams bendrauti ir bendradarbiauti.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriam tinklalapiui, leidžiant AI agentams atrasti ir sąveikauti su turiniu.

## Learning Goals

• **Nustatyti** pagrindinį MCP, A2A ir NLWeb tikslą ir naudą AI agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina ryšį ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Atpažinti** skirtingas kiekvieno protokolo roles kuriant sudėtingas agentines sistemas.

## Model Context Protocol

The **Model Context Protocol (MCP)** yra atviras standartas, kuris suteikia standartizuotą būdą programoms pateikti kontekstą ir įrankius LLM. Tai leidžia „universalų adapterį“ skirtingiems duomenų šaltiniams ir įrankiams, prie kurių AI agentai gali prisijungti nuosekliai.

Pažiūrėkime į MCP komponentus, privalumus, palyginti su tiesioginiu API naudojimu, ir pavyzdį, kaip AI agentai gali naudoti MCP serverį.

### MCP Core Components

MCP veikia pagal **klientas-serveris architektūrą** ir pagrindiniai komponentai yra:

• **Hosts** yra LLM programos (pavyzdžiui, kodo redaktorius kaip VSCode), kurios inicijuoja ryšius su MCP serveriu.

• **Clients** yra komponentai host programoje, kurie palaiko vienas-prie-vieno ryšius su serveriais.

• **Servers** yra lengvos programos, kurios atskleidžia specifines galimybes.

Protokole įtraukti trys pagrindiniai primityvai, kurie yra MCP serverio galimybės:

• **Tools**: tai atskiros operacijos ar funkcijos, kurias AI agentas gali iškviesti, kad atliktų veiksmą. Pavyzdžiui, orų tarnyba gali atskleisti įrankį „get weather“, arba el. prekybos serveris gali atskleisti įrankį „purchase product“. MCP serveriai savo galimybių sąraše reklamuoja kiekvieno įrankio pavadinimą, aprašymą ir įėjimo/išėjimo schemą.

• **Resources**: tai skaitymui skirtos duomenų vienetai arba dokumentai, kuriuos MCP serveris gali suteikti, o klientai gali juos gauti pagal poreikį. Pavyzdžiai: failų turinys, duomenų bazės įrašai arba žurnalo failai. Resursai gali būti tekstiniai (pvz., kodas arba JSON) arba dvejetainiai (pvz., vaizdai arba PDF).

• **Prompts**: tai iš anksto apibrėžti šablonai, kurie teikia siūlomus užklausas, leidžiančius sudėtingesnes darbo eigas.

### Benefits of MCP

MCP siūlo ženklių privalumų AI agentams:

• **Dynamic Tool Discovery**: Agentai gali dinamiškai gauti iš serverio prieinamų įrankių sąrašą kartu su aprašymais, ką jie atlieka. Tai skiriasi nuo tradicinių API, kurios dažnai reikalauja statinio kodavimo integracijoms, t. y. bet koks API pasikeitimas reikalauja kodo atnaujinimų. MCP siūlo „integruok vieną kartą“ požiūrį, suteikiantį didesnį prisitaikymą.

• **Interoperability Across LLMs**: MCP veikia su skirtingais LLM, suteikdamas lankstumo pakeisti pagrindinius modelius siekiant geresnių rezultatų.

• **Standardized Security**: MCP apima standartinį autentifikacijos metodą, pagerindamas mastelį pridedant prieigą prie papildomų MCP serverių. Tai paprasčiau nei valdyti skirtingus raktus ir autentifikacijos tipus įvairiems tradiciniams API.

### MCP Example

![MCP Diagram](../../../translated_images/lt/mcp-diagram.e4ca1cbd551444a1.webp)

Įsivaizduokite, kad vartotojas nori užsakyti skrydį naudodamasis AI asistentu, kuris naudoja MCP.

1. **Connection**: AI asistentas (MCP klientas) prisijungia prie oro linijų pateikto MCP serverio.

2. **Tool Discovery**: Klientas paklausia oro linijų MCP serverio: „Kokius įrankius turite?“ Serveris atsako su įrankiais, tokiais kaip „search flights“ ir „book flights“.

3. **Tool Invocation**: Jūs tada paprašote AI asistento: „Prašau suraskite skrydį iš Portland į Honolulu.“ AI asistentas, naudodamas savo LLM, nustato, kad reikia iškviesti įrankį „search flights“ ir perduoda atitinkamus parametrus (išvykimo vieta, paskirties vieta) MCP serveriui.

4. **Execution and Response**: MCP serveris, veikiantis kaip apvalkalas, atlieka faktinį skambutį į oro linijų vidinį rezervavimo API. Jis gauna skrydžių informaciją (pvz., JSON duomenis) ir siunčia ją atgal AI asistentui.

5. **Further Interaction**: AI asistentas pateikia skrydžių parinktis. Kai pasirinksite skrydį, asistentas gali iškviesti tą patį MCP serverį skirtą įrankį „book flight“, baigdamas užsakymą.

## Agent-to-Agent Protocol (A2A)

Kol MCP orientuojasi į LLM prisijungimą prie įrankių, **Agent-to-Agent (A2A) protokolas** žengia žingsnį toliau, įgalindamas skirtingų AI agentų tarpusavio komunikaciją ir bendradarbiavimą. A2A jungia AI agentus iš skirtingų organizacijų, aplinkų ir technologijų komplektų, kad bendradarbiautų atliekant bendrą užduotį.

Aptarsime A2A komponentus ir privalumus bei pavyzdį, kaip tai galėtų būti pritaikyta mūsų kelionių programoje.

### A2A Core Components

A2A orientuojasi į agentų tarpusavio komunikacijos įgalinimą ir jų darbą kartu, kad būtų atlikta vartotojo sub-užduotis. Kiekvienas protokolo komponentas prisideda prie to:

#### Agent Card

Panašiai kaip MCP serveris dalijasi įrankių sąrašu, Agent Card turi:
- Agento pavadinimą.
- **bendrą užduočių aprašymą**, kurias jis atlieka.
- **konkrečių įgūdžių sąrašą** su aprašymais, kurie padeda kitiems agentams (arba net žmonėms) suprasti, kada ir kodėl verta kviesti tą agentą.
- **dabartinį Endpoint URL** agento
- Agento **versiją** ir **galimybes**, tokias kaip transliavimo atsakymai ir push pranešimai.

#### Agent Executor

Agent Executor atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, nes nuotoliniam agentui to reikia, kad suprastų, kokią užduotį reikia atlikti. A2A serveryje agentas naudoja savo didelį kalbos modelį (LLM) gaunčių užklausų analizavimui ir užduočių vykdymui naudodamas savo vidinius įrankius.

#### Artifact

Kai nuotolinis agentas atliko prašomą užduotį, jo darbo produktas sukuriamas kaip artefaktas. Artefaktas **turi agento darbo rezultatą**, **aprašymą, kas buvo atlikta**, ir **teksto kontekstą**, kuris siunčiamas per protokolą. Po artefakto siuntimo ryšys su nuotoliniu agentu uždaromas iki kito poreikio.

#### Event Queue

Šis komponentas naudojamas **atnaujinimams tvarkyti ir žinutėms perduoti**. Jis ypač svarbus gamybiniame agentiniame sistemos kontekste, kad būtų užkirstas kelias ryšio uždarymui tarp agentų prieš užduočiai pilnai užbaigiant, ypač kai užduočių vykdymas gali užtrukti ilgesnį laiką.

### Benefits of A2A

• **Enhanced Collaboration**: Leidžia agentams iš skirtingų tiekėjų ir platformų bendrauti, dalintis kontekstu ir dirbti kartu, palengvindamas sklandžią automatizaciją tarp tradiciškai atskirtų sistemų.

• **Model Selection Flexibility**: Kiekvienas A2A agentas gali pasirinkti, kurį LLM jis naudoja savo užklausoms aptarnauti, leidžiant optimizuotus arba smulkintus modelius kiekvienam agentui, skirtingai nei vienas LLM ryšys kai kuriuose MCP scenarijuose.

• **Built-in Authentication**: Autentifikacija yra integruota tiesiogiai į A2A protokolą, suteikiant tvirtą saugumo pagrindą agentų sąveikai.

### A2A Example

![A2A Diagram](../../../translated_images/lt/A2A-Diagram.8666928d648acc26.webp)

Išplėskime mūsų kelionių užsakymo scenarijų, bet šį kartą naudodami A2A.

1. **User Request to Multi-Agent**: Vartotojas bendrauja su „Travel Agent“ A2A klientu/agento, pavyzdžiui, sakydamas: „Prašau užsakyti visą kelionę į Honolulu kitai savaitei, įskaitant skrydžius, viešbutį ir nuomojamą automobilį“.

2. **Orchestration by Travel Agent**: Travel Agent gauna šį sudėtingą prašymą. Jis naudoja savo LLM, kad apgalvotų užduotį ir nustatytų, jog reikia bendrauti su kitais specializuotais agentais.

3. **Inter-Agent Communication**: Travel Agent tada naudoja A2A protokolą, kad prisijungtų prie tolimesnių agentų, tokių kaip „Airline Agent“, „Hotel Agent“ ir „Car Rental Agent“, kuriuos kuria skirtingos įmonės.

4. **Delegated Task Execution**: Travel Agent siunčia konkrečias užduotis šiems specializuotiems agentams (pvz., „Raskite skrydžius į Honolulu,“ „Užsakyti viešbutį,“ „Išsinuomoti automobilį“). Kiekvienas iš šių specializuotų agentų, naudodamas savo LLM ir savo įrankius (kurie patys gali būti MCP serveriai), atlieka savo dalį rezervavimo proceso.

5. **Consolidated Response**: Kai visi tolimesni agentai baigia užduotis, Travel Agent sujungia rezultatus (skrydžio duomenis, viešbučio patvirtinimą, automobilių nuomos užsakymą) ir siunčia išsamią, pokalbio stiliaus atsakymą atgal vartotojui.

## Natural Language Web (NLWeb)

Tinklalapiai ilgą laiką buvo pagrindinis būdas vartotojams pasiekti informaciją ir duomenis internete.

Pažiūrėkime į skirtingus NLWeb komponentus, NLWeb privalumus ir pavyzdį, kaip mūsų NLWeb veikia, žiūrint į mūsų kelionių programą.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Sistema, kuri apdoroja natūralios kalbos užklausas. Ji sujungia skirtingas platformos dalis, kad sukurtų atsakymus. Galite galvoti apie ją kaip apie **variklį, kuris palaiko natūralios kalbos funkcijas** tinklalapyje.

- **NLWeb Protocol**: Tai **pagrindinių taisyklių rinkinys natūralios kalbos sąveikai** su tinklalapiu. Jis grąžina atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pagrindą „AI Web“, panašiai kaip HTML padarė įmanomą dokumentų dalinimąsi internete.

- **MCP Server (Model Context Protocol Endpoint)**: Kiekvienas NLWeb nustatymas taip pat veikia kaip **MCP serveris**. Tai reiškia, kad jis gali **dalintis įrankiais (pvz., „ask“ metodu) ir duomenimis** su kitomis AI sistemomis. Praktikoje tai leidžia tinklalapio turinį ir galimybes naudoti AI agentams, todėl svetainė tampa platesnės „agentų ekosistemos“ dalimi.

- **Embedding Models**: Šie modeliai naudojami **paversti tinklalapio turinį į skaitines reprezentacijas, vadinamas vektoriais** (embedding). Šie vektoriai fiksuoja reikšmę taip, kad kompiuteriai gali palyginti ir ieškoti. Jie saugomi specialioje duomenų bazėje, ir vartotojai gali pasirinkti, kurį embedding modelį nori naudoti.

- **Vector Database (Retrieval Mechanism)**: Ši duomenų bazė **saugo tinklalapio turinio embedding'us**. Kai kas nors pateikia užklausą, NLWeb patikrina vektorinę duomenų bazę, kad greitai rastų aktualiausią informaciją. Ji pateikia greitą galimų atsakymų sąrašą, surūšiuotą pagal panašumą. NLWeb veikia su skirtingomis vektorių saugojimo sistemomis, tokiomis kaip Qdrant, Snowflake, Milvus, Azure AI Search ir Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/lt/nlweb-diagram.c1e2390b310e5fe4.webp)

Apsvarstykime vėl mūsų kelionių rezervavimo svetainę, bet šį kartą ji veikia su NLWeb.

1. **Data Ingestion**: Kelionių svetainės esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, kelionių paketai) yra suformatuoti naudojant Schema.org arba įkelti per RSS srautus. NLWeb įrankiai importuoja šiuos struktūruotus duomenis, sukuria embedding'us ir saugo juos vietinėje arba nuotolinėje vektorinėje duomenų bazėje.

2. **Natural Language Query (Human)**: Vartotojas aplanko svetainę ir, vietoj naršymo meniu, įrašo į pokalbio sąsają: „Raskite man šeimai tinkamą viešbutį Honolulu su baseinu kitai savaitei“.

3. **NLWeb Processing**: NLWeb programa gauna šią užklausą. Ji siunčia užklausą LLM supratimui ir tuo pačiu ieško savo vektorinėje duomenų bazėje tinkamų viešbučių sąrašų.

4. **Accurate Results**: LLM padeda interpretuoti paieškos rezultatus iš duomenų bazės, identifikuoti geriausius atitikimus pagal kriterijus „šeimai tinkamas“, „baseinas“ ir „Honolulu“, ir tuomet suformatuoti natūralios kalbos atsakymą. Svarbu, kad atsakymas remiasi faktiniais viešbučiais iš svetainės katalogo, vengiant išgalvotos informacijos.

5. **AI Agent Interaction**: Kadangi NLWeb veikia kaip MCP serveris, išorinis AI kelionių agentas taip pat galėtų prisijungti prie šios svetainės NLWeb egzemplioriaus. AI agentas tada galėtų naudoti `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb egzempliorius suprocesuotų tai, pasinaudodamas savo restoranų informacijos duomenų baze (jei ji įkelta), ir grąžintų struktūruotą JSON atsakymą.

### Got More Questions about MCP/A2A/NLWeb?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo klausimus apie AI agentus.

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojama kreiptis į profesionalų vertėją. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingą aiškinimą, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->