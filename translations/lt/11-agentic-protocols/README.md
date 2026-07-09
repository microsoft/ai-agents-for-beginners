# Agentinių protokolų naudojimas (MCP, A2A ir NLWeb)

[![Agentic Protocols](../../../translated_images/lt/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Spustelėkite aukščiau esantį paveikslėlį norėdami peržiūrėti šios pamokos vaizdo įrašą)_

Didėjant dirbtinio intelekto agentų naudojimui, didėja ir protokolų, užtikrinančių standartizaciją, saugumą ir atvirą inovacijų palaikymą, poreikis. Šioje pamokoje apžvelgsime 3 protokolus, siekiančius patenkinti šį poreikį – Modelio konteksto protokolą (MCP), Agentų bendravimą (A2A) ir Natūralios kalbos tinklą (NLWeb).

## Įvadas

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia dirbtinio intelekto agentams pasiekti išorines priemones ir duomenis, kad atliktų vartotojo užduotis.

• Kaip **A2A** suteikia galimybę bendrauti ir bendradarbiauti tarp skirtingų DI agentų.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriai svetainei, leidžiant DI agentams atrasti ir sąveikauti su jos turiniu.

## Mokymosi tikslai

• **Nustatyti** pagrindinį MCP, A2A ir NLWeb tikslą ir naudą DI agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina bendravimą ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Atpažinti** kiekvieno protokolo unikalią rolę sudėtingų agentinių sistemų kūrime.

## Modelio konteksto protokolas

**Modelio konteksto protokolas (MCP)** yra atviras standartas, suteikiantis standartizuotą būdą programoms teikti kontekstą ir priemones LLM. Tai leidžia sukurti "universalų adapterį" prie skirtingų duomenų šaltinių ir įrankių, prie kurių DI agentai gali prisijungti nuosekliu būdu.

Pažvelkime į MCP komponentus, privalumus lyginant su tiesioginiu API naudojimu ir pavyzdį, kaip DI agentai galėtų naudoti MCP serverį.

### MCP pagrindiniai komponentai

MCP veikia **kliento-serverio architektūroje** ir pagrindiniai komponentai yra:

• **Hostai** yra LLM programos (pavyzdžiui, kodo redaktorius VSCode), kurios pradeda ryšius su MCP serveriu.

• **Klientai** yra komponentai hosto programoje, palaikantys vienas prie vieno ryšius su serveriais.

• **Serveriai** yra lengvos programos, atveriančios specifines galimybes.

Protokole yra trys pagrindiniai primityvai, kurie yra MCP serverio galimybės:

• **Įrankiai**: tai atskiros veiksmai ar funkcijos, kurias DI agentas gali iškviesti atlikti veiksmui. Pavyzdžiui, orų paslauga gali atverti "gauti orą" įrankį, ar el. prekybos serveris gali siūlyti "įsigyti produktą" įrankį. MCP serveriai reklamuoja kiekvieno įrankio pavadinimą, aprašymą ir įvesties/išvesties schemą savo galimybių sąraše.

• **Ištekliai**: tai tik skaitymui skirti duomenų elementai ar dokumentai, kuriuos MCP serveris gali pateikti, o klientai gali juos gauti pagal poreikį. Pavyzdžiai: failų turinys, duomenų bazės įrašai ar žurnalo failai. Ištekliai gali būti tekstiniai (kaip kodas ar JSON) arba dvejetainiai (kaip paveikslėliai ar PDF).

• **Skatinimai (Prompts)**: tai iš anksto apibrėžti šablonai, teikiantys siūlomus skatinimus, leidžiančius vykdyti sudėtingesnius darbo procesus.

### MCP privalumai

MCP suteikia ženklių privalumų DI agentams:

• **Dinaminis įrankių atradimas**: agentai gali dinamiškai gauti serverio pateiktą galimų įrankių sąrašą su jų aprašymais. Tai skiriasi nuo tradicinių API, kurioms dažnai reikalinga statinė integracijos kodavimo konfigūracija, todėl bet kokie API pakeitimai reikalauja kodo atnaujinimų. MCP siūlo "vieną integravimą" strategiją, leidžiančią didesnį prisitaikomumą.

• **Tarp LLM sąveika**: MCP veikia su skirtingais LLM, suteikdamas lankstumą keisti pagrindinius modelius geresniam našumui įvertinti.

• **Standardizuotas saugumas**: MCP apima standartinį autentifikavimo metodą, palengvinantį mastelį, kai pridedama prieigos prie kito MCP serverio. Tai paprasčiau nei tvarkyti skirtingus raktus ir autentifikavimo tipus tradiciniams API.

### MCP pavyzdys

![MCP Diagram](../../../translated_images/lt/mcp-diagram.e4ca1cbd551444a1.webp)

Įsivaizduokime, kad vartotojas nori užsisakyti skrydį naudodamas DI asistentą, pagrįstą MCP.

1. **Prisijungimas**: DI asistentas (MCP klientas) jungiasi prie MCP serverio, kurį teikia oro linijos.

2. **Įrankių atradimas**: klientas klausia oro linijų MCP serverio: „Kokius įrankius turite?“ Serveris atsako su įrankiais, pavyzdžiui, „ieškoti skrydžių“ ir „užsisakyti skrydį“.

3. **Įrankio iškvietimas**: jūs tuomet paprašote DI asistento: „Prašau surask skrydį iš Portlando į Honolulį.“ DI asistentas, naudodamasis savo LLM, nustato, kad turi iškviesti „ieškoti skrydžių“ įrankį ir perduoda atitinkamus parametrus (kilmės ir paskirties vietas) MCP serveriui.

4. **Įvykdymas ir atsakymas**: MCP serveris, veikiantis kaip apvyniojimas, atlieka faktinį skambutį oro linijų vidiniam užsakymų API. Tada gauna skrydžio informaciją (pvz., JSON duomenis) ir atsiunčia ją atgal DI asistentui.

5. **Tolesnė sąveika**: DI asistentas pateikia skrydžių variantus. Kai pasirinksite skrydį, asistentas gali iškviesti „užsisakyti skrydį“ įrankį tame pačiame MCP serveryje ir užbaigti užsakymą.

## Agentas-agentui protokolas (A2A)

Tuo tarpu, kai MCP koncentruojasi į LLM sujungimą su įrankiais, **Agentas-agentui (A2A) protokolas** žengia dar toliau, leidžiant skirtingų DI agentų bendravimą ir bendradarbiavimą. A2A jungia DI agentus per skirtingas organizacijas, aplinkas ir technologijų krūvas, kad būtų įvykdyta bendra užduotis.

Pažvelgsime į A2A komponentus ir naudą, kartu su pavyzdžiu, kaip tai būtų galima pritaikyti mūsų kelionių programėlėje.

### A2A pagrindiniai komponentai

A2A orientuotas į agentų bendravimo ir jų bendro darbo galimybes užbaigti vartotojo dalinę užduotį. Kiekvienas protokolo komponentas prisideda prie to:

#### Agentų kortelė

Panašiai kaip MCP serveris dalinasi įrankių sąrašu, Agentų kortelėje yra:
- Agento pavadinimas.
- **aprašymas apie bendras užduotis**, kurias agentas atlieka.
- **konkretų įgūdžių sąrašas** su aprašymais, padedančiais kitiems agentams (ar net žmonėms) suprasti, kada ir kodėl vertėtų kviesti tą agentą.
- Agento **dabartinis Endpoint URL**.
- Agento **versija** ir **galimybės**, pavyzdžiui, srautinė reakcija ir pranešimai.

#### Agentų vykdytojas

Agentų vykdytojas atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, nes nuotolinis agentas turi suprasti, kokia užduotis turi būti atlikta. A2A serveryje agentas naudoja savo Didelį kalbos modelį (LLM), kad analizuotų gaunamas užklausas ir vykdytų užduotis naudodamas savo vidinius įrankius.

#### Artefaktas

Baigus užduotį, nuotolinio agente sukurtas darbo produktas vadinamas artefaktu. Artefaktas **apima agento darbo rezultatą**, **aprašymą, kas buvo atlikta**, ir **tekstinį kontekstą**, kuris perduodamas per protokolą. Po artefakto siuntimo ryšys su nuotoliniu agentu uždaromas iki kito panaudojimo.

#### Įvykių eilė

Šis komponentas naudojamas **atnaujinimams tvarkyti ir žinutėms perduoti**. Tai ypač svarbu gamybinėse agentinėse sistemose, kad būtų išvengta ryšio uždarymo tarp agentų prieš užduoties užbaigimą, ypač kai užduočių vykdymas užtrunka ilgiau.

### A2A privalumai

• **Pagerintas bendradarbiavimas**: suteikia galimybę agentams iš įvairių tiekėjų ir platformų bendrauti, dalytis kontekstu ir bendradarbiauti, palengvinant sklandžią automatizaciją tarp įprastai nesujungtų sistemų.

• **Lankstus modelių pasirinkimas**: kiekvienas A2A agentas gali pasirinkti, kokį LLM naudoja savo užklausų aptarnavimui, leidžiant optimizuotus ar koreguotus modelius kiekvienam agentui, skirtingai nei kai kuriose MCP situacijose, kai jungiamasi prie vieno LLM.

• **Įmontuotas autentifikavimas**: autentifikavimas integruotas tiesiogiai į A2A protokolą, suteikiant stiprią saugumo sistemą agentų sąveikai.

### A2A pavyzdys

![A2A Diagram](../../../translated_images/lt/A2A-Diagram.8666928d648acc26.webp)

Išplėsime mūsų kelionių užsakymo scenarijų, tačiau šį kartą naudodami A2A.

1. **Vartotojo užklausa daugiaagentiniam sistemai**: vartotojas sąveikauja su „Kelionių agentu“ – A2A klientu/agento, galbūt sakydamas: „Prašau užsisakyti visą kelionę į Honolulį kitai savaitei, įskaitant skrydžius, viešbutį ir automobilio nuomą“.

2. **Kelionių agente vykdoma koordinacija**: Kelionių agentas gauna šią sudėtingą užklausą. Jis naudoja savo LLM užduočiai apmąstyti ir nustato, kad reikia sąveikauti su kitais specializuotais agentais.

3. **Agentų tarpusavio komunikacija**: Kelionių agentas naudoja A2A protokolą, kad prisijungtų prie kelių agentų, pavyzdžiui, „Oro linijų agento“, „Viešbučio agento“ ir „Automobilio nuomos agento“, sukurtų skirtingų bendrovių.

4. **Užduočių perdavimas**: Kelionių agentas siunčia konkrečias užduotis šiems specializuotiems agentams (pvz., „Raskite skrydžius į Honolulį“, „Užsisakykite viešbutį“, „Išsinuomokite automobilį“). Kiekvienas specializuotas agentas, naudodamas savo LLM ir vidinius įrankius (kurie patys gali būti MCP serveriai), atlieka savo užsakymo dalį.

5. **Sujungtas atsakymas**: kai visi agentai baigia savo užduotis, Kelionių agentas sujungia rezultatus (skrydžio duomenis, viešbučio patvirtinimą, automobilio nuomos užsakymą) ir pateikia išsamų, pokalbio stiliaus atsakymą vartotojui.

## Natūralios kalbos tinklas (NLWeb)

Svetainės jau ilgą laiką yra pagrindinis būdas vartotojams pasiekti informaciją ir duomenis internete.

Pažvelkime į skirtingus NLWeb komponentus, NLWeb privalumus ir pavyzdį, kaip mūsų kelionių programėlė veikia su NLWeb.

### NLWeb komponentai

- **NLWeb programėlė (Pagrindinis paslaugos kodas)**: sistema, apdorojanti natūralios kalbos klausimus. Ji jungia platformos dalis, kad sukurtų atsakymus. Tai galima įsivaizduoti kaip **variklį, kurio dėka svetainės turi natūralios kalbos funkcijas**.

- **NLWeb protokolas**: tai **pagrindinių taisyklių rinkinys natūralios kalbos sąveikai** su svetaine. Jis grąžina atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pamatus „DI tinklui“, taip, kaip HTML leido dalytis dokumentais internete.

- **MCP serveris (Modelio konteksto protokolo galas)**: kiekvienas NLWeb diegimas taip pat veikia kaip **MCP serveris**. Tai reiškia, kad gali **dalytis įrankiais (pvz., „ask“ metodu) ir duomenimis** su kitomis DI sistemomis. Praktikoje tai leidžia svetainės turinį ir galimybes naudoti DI agentams, todėl svetainė tampa platesnės „agentų ekosistemos“ dalimi.

- **Įterpimo modeliai**: šie modeliai naudojami **paversti svetainės turinį į skaitines reprezentacijas, vadinamas vektoriais (embeddingais)**. Šie vektoriai užfiksuoja reikšmes taip, kad kompiuteriai galėtų jas palyginti ir ieškoti. Jie saugomi specialioje duomenų bazėje, o vartotojai gali pasirinkti, kurį įterpimo modelį nori naudoti.

- **Vektorinė duomenų bazė (paieškos mechanizmas)**: ši duomenų bazė **saugo svetainės turinio embeddingus**. Kai kas nors užduoda klausimą, NLWeb patikrina vektorinę duomenų bazę, kad greitai surastų aktualiausią informaciją. Ji pateikia greitą galimų atsakymų sąrašą, reitinguotą pagal artimumą. NLWeb veikia su įvairiomis vektorinėmis saugyklomis, tokiomis kaip Qdrant, Snowflake, Milvus, Azure AI Search ir Elasticsearch.

### NLWeb pagal pavyzdį

![NLWeb](../../../translated_images/lt/nlweb-diagram.c1e2390b310e5fe4.webp)

Vėl pažvelkime į mūsų kelionių užsakymo svetainę, tačiau šį kartą ji veikia su NLWeb.

1. **Duomenų įkėlimas**: kelionių svetainės esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, kelionių paketai) yra suformatuoti naudojant Schema.org arba įkelti per RSS srautus. NLWeb įrankiai įrašo šiuos struktūruotus duomenis, sukuria embeddingus ir saugo juos vietinėje arba nuotolinėje vektorinėje duomenų bazėje.

2. **Natūralios kalbos užklausa (žmogaus)**: vartotojas apsilanko svetainėje ir, vietoj naršymo meniu, rašo pokalbio sąsajoje: „Rask man šeimoms tinkamą viešbutį Honolulyje su baseinu kitai savaitei“.

3. **NLWeb apdorojimas**: NLWeb programėlė gauna šią užklausą. Ji siunčia užklausą LLM supratimui ir tuo pačiu ieško savo vektorinėje duomenų bazėje atitinkančių viešbučių sąrašų.

4. **Tikslūs rezultatai**: LLM padeda interpretuoti paieškos rezultatus iš duomenų bazės, nustatyti geriausius atitikmenis pagal kriterijus „šeimoms tinkamas“, „baseinas“ ir „Honolulu“ ir tada suformuluoti natūralios kalbos atsakymą. Svarbu, kad atsakymas remiasi tikrais viešbučiais iš svetainės katalogo, vengiant išgalvotos informacijos.

5. **DI agento sąveika**: kadangi NLWeb veikia kaip MCP serveris, išorinis DI kelionių agentas taip pat galėtų prisijungti prie šios svetainės NLWeb instancijos. DI agentas tuomet galėtų naudoti `ask` MCP metodą tiesiogiai užduoti klausimą svetainei: `ask("Ar viešbutis rekomenduoja veganišką restoraną Honolulio rajone?")`. NLWeb instancija apdorotų šį užklausą, pasitelkdama savo restoranų duomenų bazę (jei ta duomenų bazė yra įkelta) ir pateiktų struktūruotą JSON atsakymą.

### Turite daugiau klausimų apie MCP/A2A/NLWeb?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiaisiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo DI agentų klausimus.

## Ištekliai

- [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb saugykla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft agentų karkasas](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->