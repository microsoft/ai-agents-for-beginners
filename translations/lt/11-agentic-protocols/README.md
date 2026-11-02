# Agentinių protokolų naudojimas (MCP, A2A ir NLWeb)

[![Agentinių protokolų vaizdas](../../../translated_images/lt/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Paspauskite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Didėjant DI agentų naudojimui, auga ir poreikis protokolams, užtikrinantiems standartizaciją, saugumą ir palaikantiems atvirą inovaciją. Šioje pamokoje aptarsime 3 protokolus, siekiančius patenkinti šį poreikį – Modelio konteksto protokolą (MCP), Agentas-agentui (A2A) ir Natūralios kalbos tinklą (NLWeb).

## Įvadas

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia DI agentams pasiekti išorinius įrankius ir duomenis, kad atliktų vartotojo užduotis.

• Kaip **A2A** leidžia komunikaciją ir bendradarbiavimą tarp skirtingų DI agentų.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriai svetainei, leidžiančias DI agentams rasti ir bendrauti su turiniu.

## Mokymosi tikslai

• **Nustatyti** pagrindinę MCP, A2A ir NLWeb paskirtį ir naudą DI agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina komunikaciją ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Atpažinti** skirtingas kiekvieno protokolo vaidmenis sudarant sudėtingas agentines sistemas.

## Modelio konteksto protokolas

**Modelio konteksto protokolas (MCP)** yra atviras standartas, suteikiantis standartizuotą būdą programoms pateikti kontekstą ir įrankius LLM. Tai leidžia "universalią jungtį" skirtingiems duomenų šaltiniams ir įrankiams, prie kurių DI agentai gali prisijungti nuosekliai.

Pažiūrėkime į MCP komponentus, privalumus palyginti su tiesioginiu API naudojimu ir pavyzdį, kaip DI agentai gali naudoti MCP serverį.

### Pagrindiniai MCP komponentai

MCP veikia pagal **kliento-serverio architektūrą**, o pagrindiniai komponentai yra:

• **Šeimininkai (Hosts)** – LLM programėlės (pavyzdžiui, VSCode kodo redaktorius), kurios inicijuoja ryšius su MCP serveriu.

• **Klientai** – komponentai šeimininko programoje, palaikantys vienas prie vieno ryšius su serveriais.

• **Serveriai** – lengvos programos, kurios teikia konkrečias galimybes.

Protokole įtraukti trys pagrindiniai primityvai, kurie yra MCP serverio galimybės:

• **Įrankiai**: Tai atskiros veiksmo funkcijos, kurias DI agentas gali kviesti. Pavyzdžiui, orų tarnyba gali siūlyti "gauti orus" įrankį, o e-komercijos serveris – "įsigyti produktą". MCP serveriai reklamuoja kiekvieno įrankio pavadinimą, aprašymą ir įvesties/išvesties schemą savo galimybių sąraše.

• **Ištekliai**: Tai yra tekstiniai ar binariniai duomenys ar dokumentai, kuriuos MCP serveris gali suteikti, ir klientai juos gali gauti pagal poreikį. Pavyzdžiai – failų turinys, duomenų bazių įrašai ar žurnalo failai. Ištekliai gali būti tekstiniai (kaip kodas arba JSON) arba binariniai (kaip paveikslėliai ar PDF).

• **Užklausos**: Tai iš anksto paruošti šablonai su pasiūlytais užklausų pavyzdžiais, leidžiantys sudėtingesniems darbo procesams.

### MCP privalumai

MCP suteikia svarbių privalumų DI agentams:

• **Dinamiškas įrankių atradimas**: Agentai gali dinamiškai gauti serverio pateiktą galimų įrankių sąrašą su jų aprašymais. Tai skiriasi nuo tradicinių API, kuriems dažnai reikia statinio integravimo kodavimo – bet koks API pakeitimas reikalauja kodo atnaujinimo. MCP siūlo "integruoti vieną kartą" požiūrį, didinantį pritaikomumą.

• **Suderinamumas tarp LLM**: MCP veikia su įvairiais LLM, suteikdamas lankstumo keisti pagrindinius modelius aukštesnei veiklai įvertinti.

• **Standartizuotas saugumas**: MCP apima standartinį autentifikavimo metodą, palengvinantį mastelio didinimą prijungiant papildomus MCP serverius. Tai paprasčiau nei tvarkyti skirtingus raktus ir autentifikavimo tipus įvairioms tradicinėms API.

### MCP pavyzdys

![MCP schema](../../../translated_images/lt/mcp-diagram.e4ca1cbd551444a1.webp)

Įsivaizduokite, kad vartotojas nori užsakyti skrydį naudodamasis MCP varomu DI asistentu.

1. **Prisijungimas**: DI asistentas (MCP klientas) jungiasi prie oro linijų suteikto MCP serverio.

2. **Įrankių atradimas**: Klientas klausia oro linijų MCP serverio: "Kokie įrankiai yra prieinami?" Serveris atsako su įrankiais kaip "skrydžių paieška" ir "skrydžių užsakymas".

3. **Įrankio kvietimas**: Tuomet vartotojas sako DI asistentui: "Prašau ieškoti skrydžio iš Portlando į Honolulu." DI asistentas, naudodamas savo LLM, nustato, kad reikia kviesti "skrydžių paieškos" įrankį ir perduoda susijusius parametrus (išvykimo vietą, tikslą) MCP serveriui.

4. **Vykdymas ir atsakymas**: MCP serveris, veikiantis kaip tarpininkas, atlieka faktinį kvietimą vidinei oro linijų užsakymų API. Tada gauna skrydžių informaciją (pvz., JSON duomenis) ir siunčia ją DI asistentui.

5. **Tolimesnė sąveika**: DI asistentas pateikia skrydžių variantus. Pasirinkus skrydį, asistentas gali iškviesti "skrydžio užsakymo" įrankį tame pačiame MCP serveryje, užbaigiant užsakymą.

## Agentas-agentui protokolas (A2A)

Šiame MCP kontekste **Agentas-agentui (A2A) protokolas** dar labiau žengia į priekį, leidžiant bendravimą ir bendradarbiavimą tarp skirtingų DI agentų. A2A jungia DI agentus skirtingų organizacijų, aplinkų ir technologijų sistemų ribose, kad įvykdytų bendrą užduotį.

Aptarsime A2A komponentus ir privalumus bei pavyzdį, kaip tai galėtų būti pritaikyta mūsų kelionių programėlėje.

### A2A pagrindiniai komponentai

A2A siekia sudaryti ryšį tarp agentų ir skatinti juos dirbti kartu, atlikti vartotojo užduoties dalį. Kiekvienas protokolo komponentas prisideda prie to:

#### Agentų kortelė

Panašiai kaip MCP serveris dalinasi įrankių sąrašu, Agentų kortelė apima:
- Agentų pavadinimą.
- **Bendrą užduočių aprašymą**, kurias agentas atlieka.
- **Specifinių įgūdžių sąrašą** su aprašymais, kurie padeda kitiems agentams (ar net žmonių vartotojams) suprasti, kada ir kodėl verta iškviesti tą agentą.
- Agentų **dabartinį Endpoint URL**.
- Agentų **versiją** ir **galimybes**, tokias kaip tiesioginis atsakymų srautas ir pranešimai.

#### Agentų vykdytojas

Agentų vykdytojas atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, kuris to reikia, kad suprastų vykdomą užduotį. A2A serveryje agentas naudoja savo LLM, kad analizuotų gaunamus užklausimus ir vykdytų užduotis su savo vidiniais įrankiais.

#### Artefaktas

Baigus užduotį, nuotolinio agento darbo rezultatas sukuriamas kaip artefaktas. Artefaktas **apima agento darbo rezultatą**, **ką atlikta aprašymą** ir **teksto kontekstą**, perduodamą protokolu. Po artefakto išsiuntimo ryšys su nuotoliniu agentu uždaromas, kol vėl bus reikalingas.

#### Įvykių eilė

Ši dalis naudojama **atnaujinimams tvarkyti ir pranešimams perduoti**. Ji ypač svarbi gamybai, kad užkirstų kelią agentų ryšio uždarymui dar neatlikus užduoties, ypač kai užduotys gali užtrukti ilgiau.

### A2A privalumai

• **Išplėtotas bendradarbiavimas**: Leidžia agentams iš skirtingų tiekėjų ir platformų bendrauti, dalytis kontekstu ir dirbti kartu, užtikrinant sklandžią automatizaciją tarp tradiciškai atsiskyrusių sistemų.

• **Modelio pasirinkimo lankstumas**: Kiekvienas A2A agentas gali pasirinkti, kokį LLM naudoja užklausų aptarnavimui, leidžiant optimizuotus ar specialiai pritaikytus modelius, skirtingai nei MCP, kur neretai naudojamas vienas LLM ryšys.

• **Integruotas autentifikavimas**: Autentifikavimas tiesiogiai įtrauktas į A2A protokolą, užtikrindamas stiprų saugumo pagrindą agentų sąveikoms.

### A2A pavyzdys

![A2A schema](../../../translated_images/lt/A2A-Diagram.8666928d648acc26.webp)

Išplėskime kelionių užsakymo scenarijų, bet šįkart naudodami A2A.

1. **Vartotojo užklausa keliems agentams**: Vartotojas bendrauja su "Kelionių agento" A2A klientu/agentu, pavyzdžiui, sakydamas: "Prašau užsakyti visą kelionę į Honolulu kitai savaitei, įskaitant skrydžius, viešbutį ir automobilio nuomą".

2. **Kelionių agento orkestracija**: Kelionių agentas gauna sudėtingą užklausą. Jis naudoja savo LLM, kad apmąstytų užduotį ir nuspręstų, kad reikia bendrauti su kitais specializuotais agentais.

3. **Agentų tarpusavio komunikacija**: Tada Kelionių agentas naudoja A2A protokolą prisijungti prie antrinių agentų, tokių kaip „Oro linijų agentas“, „Viešbučių agentas“ ir „Automobilių nuomos agentas“, kuriuos sukūrė skirtingos įmonės.

4. **Užduočių delegavimas**: Kelionių agentas siunčia specifines užduotis šiems specializuotiems agentams (pvz., „Raskite skrydžius į Honolulu“, „Užsisakykite viešbutį“, „Išsinuomokite automobilį“). Kiekvienas šių agentų, naudodamas savo LLM ir savus įrankius (kurių kai kurie gali būti MCP serveriai), atlieka savo užsakymo dalį.

5. **Sujungtas atsakymas**: Kai visi antriniai agentai atlieka savo užduotis, Kelionių agentas surenka rezultatus (skrydžio duomenis, viešbučio patvirtinimą, automobilio nuomos užsakymą) ir pateikia vartotojui išsamų, pokalbio stiliaus atsakymą.

## Natūralios kalbos tinklas (NLWeb)

Svetainės jau ilgą laiką yra pagrindinis būdas vartotojams pasiekti informaciją ir duomenis internete.

Pažiūrėkime į NLWeb skirtingus komponentus, NLWeb naudą ir kaip mūsų kelionių programėlė veikia su NLWeb pavyzdžiu.

### NLWeb komponentai

- **NLWeb programėlė (pagrindinis paslaugos kodas)**: Sistema, apdorojanti natūralios kalbos klausimus. Ji jungia platformos dalis, kad sukurtų atsakymus. Galima įsivaizduoti ją kaip **variklį, kuris palaiko natūralios kalbos funkcijas** svetainėje.

- **NLWeb protokolas**: Tai yra **pagrindinių taisyklių rinkinys natūralios kalbos sąveikai su svetaine**. Jis siunčia atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pagrindą „DI tinklui“, kaip HTML padarė galimą dalytis dokumentais internete.

- **MCP serveris (Modelio konteksto protokolo galutinis taškas)**: Kiekviena NLWeb sistema taip pat veikia kaip **MCP serveris**. Tai reiškia, kad ji gali **dalintis įrankiais (pvz., „klausk“ metodu) ir duomenimis** su kitomis DI sistemomis. Praktikoje tai leidžia svetainės turiniui ir gebėjimams būti naudojamiems DI agentų, leidžiant svetainei tapti platesnio „agentų ekosistemos“ dalimi.

- **Įterpimo modeliai**: Šie modeliai naudojami **paversti svetainės turinį į skaitines reprezentacijas, vadinamas vektoriais** (embeddingais). Šie vektoriai fiksuoja prasmę taip, kad kompiuteriai gali juos palyginti ir ieškoti. Jie saugomi specialioje duomenų bazėje, o vartotojai gali rinktis, kurį įterpimo modelį naudoti.

- **Vektorinė duomenų bazė (paieškos mechanizmas)**: Ši duomenų bazė **saugo svetainės turinio embeddingus**. Kai kas nors užduoda klausimą, NLWeb ieško vektorinėje duomenų bazėje, kad greitai surastų aktualiausią informaciją. Ji pateikia greitą galimų atsakymų sąrašą, reitinguotą pagal panašumą. NLWeb veikia su skirtingomis vektorių saugojimo sistemomis, tokiomis kaip Qdrant, Snowflake, Milvus, Azure AI Search ir Elasticsearch.

### NLWeb pavyzdys

![NLWeb schema](../../../translated_images/lt/nlweb-diagram.c1e2390b310e5fe4.webp)

Vėlgi pažiūrėkime į mūsų kelionių užsakymo svetainę, bet šį kartą, ją veikia NLWeb.

1. **Duomenų įkėlimas**: Kelionių svetainės esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, turų paketai) suformatuoti naudojant Schema.org arba įkrauti per RSS srautus. NLWeb įrankiai apdoroja šiuos struktūruotus duomenis, kuria embeddingus ir saugo juos vietinėje ar nuotolinėje vektorinėje duomenų bazėje.

2. **Natūralios kalbos užklausa (žmogus)**: Vartotojas aplanko svetainę ir vietoje meniu naršymo įveda į pokalbio langą: „Raskite man šeimai draugišką viešbutį Honolulu su baseinu kitai savaitei“.

3. **NLWeb apdorojimas**: NLWeb programėlė gauna užklausą. Ji siunčia užklausą LLM supratimui ir tuo pačiu metu ieško vektorinėje duomenų bazėje aktualių viešbučių sąrašų.

4. **Tikslūs rezultatai**: LLM padeda iššifruoti duomenų bazės paieškos rezultatus, identifikuoja geriausius atitikmenis pagal kriterijus „šeimai draugiškas“, „baseinas“ ir „Honolulu“, tada pateikia natūralios kalbos atsakymą. Svarbiausia – atsakyme pateikiami tikri viešbučiai iš svetainės katalogo, vengiant sugalvotos informacijos.

5. **DI agento sąveika**: Kadangi NLWeb veikia kaip MCP serveris, išorinis DI kelionių agentas taip pat galėtų jungtis prie šios svetainės NLWeb sąsajos. DI agentas galėtų naudoti `ask` MCP metodą tiesiogiai užklausti svetainę: `ask("Ar yra veganiškų restoranų Honolulu rajone, kuriuos rekomenduoja viešbutis?")`. NLWeb apdorotų užklausą, naudodamas restoranų duomenų bazę (jei ji įkelta), ir grąžintų struktūruotą JSON atsakymą.

### Turite daugiau klausimų apie MCP/A2A/NLWeb?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitikti su kitais besimokančiais, dalyvauti darbo valandose ir gauti atsakymus į DI agentų klausimus.

## Ištekliai

- [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb saugykla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Ankstesnė pamoka

[DI agentai gamyboje](../10-ai-agents-production/README.md)

## Kita pamoka

[Konteksto inžinerija DI agentams](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->