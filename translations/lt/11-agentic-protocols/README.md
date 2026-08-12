# Agentinių protokolų naudojimas (MCP, A2A ir NLWeb)

[![Agentic Protocols](../../../translated_images/lt/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad pamatytumėte šios pamokos vaizdo įrašą)_

Didėjant DI agentų naudojimui, taip pat auga poreikis protokolams, užtikrinantiems standartizavimą, saugumą ir palaikantiems atvirą inovaciją. Šioje pamokoje aptarsime 3 protokolus, kurie siekia patenkinti šį poreikį – Modelio konteksto protokolą (MCP), Agentas agentui (A2A) ir Natūralios kalbos internetą (NLWeb).

## Įvadas

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia DI agentams naudotis išoriniais įrankiais ir duomenimis, kad įvykdytų vartotojo užduotis.

• Kaip **A2A** leidžia skirtingiems DI agentams bendrauti ir bendradarbiauti.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriame tinklalapyje, leidžiant DI agentams atrasti ir sąveikauti su turiniu.

## Mokymosi tikslai

• **Nustatyti** pagrindinį MCP, A2A ir NLWeb tikslą ir privalumus DI agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina komunikaciją ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Atpažinti** skirtingas roles, kurias kiekvienas protokolas atlieka kuriant sudėtingas agentines sistemas.

## Modelio konteksto protokolas

**Modelio konteksto protokolas (MCP)** yra atviras standartas, suteikiantis standartizuotą būdą programoms pateikti kontekstą ir įrankius LLM. Tai leidžia „universalų adapterį“ prie skirtingų duomenų šaltinių ir įrankių, prie kurių DI agentai gali prisijungti nuosekliai.

Pažvelkime į MCP komponentus, privalumus lyginant su tiesioginiu API naudojimu ir pavyzdį, kaip DI agentai gali naudoti MCP serverį.

### MCP pagrindiniai komponentai

MCP veikia pagal **klientų-serverių architektūrą**, o pagrindiniai komponentai yra:

• **Šalys (Hosts)** yra LLM programos (pvz., kodo redaktorius kaip VSCode), kurios inicijuoja ryšius su MCP serveriu.

• **Klientai (Clients)** yra komponentai šalies programoje, palaikantys vienas prie vieno ryšius su serveriais.

• **Serveriai (Servers)** yra lengvos programos, suteikiančios tam tikras galimybes.

Protokole yra trys pagrindinės primityvios funkcijos, kurios yra MCP serverio galimybės:

• **Įrankiai (Tools)**: Tai yra atskiros funkcijos ar veiksmai, kuriuos DI agentas gali iškviesti atlikti veiksmą. Pavyzdžiui, orų tarnyba gali pateikti „gauti orą“ įrankį, arba el. prekybos serveris gali pateikti „įsigyti produktą“ įrankį. MCP serveriai skelbia kiekvieno įrankio pavadinimą, aprašymą ir įvesties/išvesties schemą savo galimybių sąraše.

• **Ištekliai (Resources)**: Tai yra skaitymui skirti duomenų elementai ar dokumentai, kuriuos MCP serveris gali pateikti, o klientai gali juos gauti pagal poreikį. Pavyzdžiai – failų turinys, duomenų bazės įrašai ar žurnalo failai. Ištekliai gali būti tekstiniai (pvz., kodas arba JSON) arba dvejetainiai (pvz., paveikslėliai ar PDF).

• **Užklausos (Prompts)**: Tai yra iš anksto paruoštos šablonų formos, suteikiančios siūlomų užklausų, leidžiančių sudėtingesnes darbo eigas.

### MCP privalumai

MCP suteikia svarbių privalumų DI agentams:

• **Dinaminis įrankių aptikimas**: Agentai gali dinamiškai gauti iš serverio prieinamų įrankių sąrašą kartu su aprašymais, ką jie daro. Tai skiriasi nuo tradicinių API, kurie dažnai reikalauja statinio kodavimo integracijoms, o tai reiškia, kad bet koks API pakeitimas reikalauja kodo atnaujinimų. MCP siūlo „integruoti vieną kartą“ požiūrį, leidžiantį būti labiau prisitaikantiems.

• **Bendradarbiavimas tarp įvairių LLM**: MCP veikia per skirtingus LLM, suteikdamas lankstumą pereiti tarp pagrindinių modelių ir vertinti geresniam našumui.

• **Standartizuotas saugumas**: MCP apima standartinį autentifikavimo metodą, palengvinantį mastelį plečiant prieigą prie papildomų MCP serverių. Tai yra paprasčiau nei tvarkyti skirtingus raktus ir autentifikavimo tipus įvairiems tradiciniams API.

### MCP pavyzdys

![MCP Diagram](../../../translated_images/lt/mcp-diagram.e4ca1cbd551444a1.webp)

Įsivaizduokite, kad vartotojas nori užsisakyti skrydį naudodamasis MCP pagrįstu DI asistentu.

1. **Ryšys**: DI asistentas (MCP klientas) prisijungia prie MCP serverio, kurį pateikia aviakompanija.

2. **Įrankių aptikimas**: Klientas klausia aviakompanijos MCP serverio: „Kokius įrankius turite?“ Serveris atsako su įrankiais, tokiais kaip „ieskoti skrydžių“ ir „užsakyti skrydį“.

3. **Įrankio iškvietimas**: Tada jūs prašote DI asistento: „Prašau, ieškok skrydžio iš Porterlando į Honolulu.“ DI asistentas, naudodamasis savo LLM, nustato, kad reikia iškviesti „ieskoti skrydžių“ įrankį ir perduoda atitinkamus parametrus (išvykimo vieta, atvykimo vieta) MCP serveriui.

4. **Vykdymas ir atsakymas**: MCP serveris, veikiantis kaip apvalkalas, tikrąjį kvietimą perduoda aviakompanijos vidaus užsakymų API. Jis gauna skrydžio informaciją (pvz., JSON duomenis) ir nusiunčia ją atgal DI asistentui.

5. **Tolimesnė sąveika**: DI asistentas pateikia skrydžio pasirinkimus. Kai pasirenkate skrydį, asistentas gali iškviesti „užsakyti skrydį“ įrankį tame pačiame MCP serveryje ir užbaigti užsakymą.

## Agentas agentui protokolas (A2A)

Nors MCP orientuotas į LLM ir įrankių sujungimą, **Agentas agentui (A2A) protokolas** žengia žingsnį toliau, leidžiant DI agentams bendrauti ir bendradarbiauti tarpusavyje. A2A sujungia DI agentus įvairiose organizacijose, aplinkose ir technologijose, kad įvykdytų bendrą užduotį.

Patikrinkime A2A komponentus ir privalumus bei pavyzdį, kaip tai galėtų būti pritaikyta mūsų kelionių programoje.

### A2A pagrindiniai komponentai

A2A orientuotas į agentų komunikaciją ir jų bendrą darbą siekiant įvykdyti vartotojo užduoties dalį. Kiekvienas protokolo komponentas prisideda prie šio tikslo:

#### Agentų kortelė

Panašiai kaip MCP serveris dalijasi įrankių sąrašu, Agentų kortelėje yra:
- Agento pavadinimas.
- **aprašymas apie bendras užduotis**, kurias jis atlieka.
- **konkrečių įgūdžių sąrašas** su aprašymais, padedančiais kitiems agentams (ar net žmonėms) suprasti, kada ir kodėl reikėtų kreiptis į tą agentą.
- Agento **dabartinis galinio taško URL**.
- Agento **versija** ir **galimybės**, tokios kaip srautinis atsakas ir išstumiamos žinutės.

#### Agento vykdytojas

Agento vykdytojas atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, nes nuotolinis agentas turi suprasti, kokia užduotis turi būti atlikta. A2A serveryje agentas naudoja savo LLM priimti užklausoms ir vykdyti užduotis naudodamas savo vidinius įrankius.

#### Artefaktas

Kai nuotolinis agentas baigia užduotį, sukuriamas jo darbo rezultatas – artefaktas. Artefaktas **saugo agento darbo rezultatą**, **aprašymą, kas buvo atlikta** ir **teksto kontekstą**, kuris siunčiamas per protokolą. Po artefakto nusiuntimo ryšys su nuotoliniu agentu uždaromas, kol vėl prireikia.

#### Įvykių eilė

Šis komponentas naudojamas **atnaujinimams valdyti ir pranešimams perduoti**. Jis ypač svarbus produkcijoje agentinėms sistemoms, kad būtų išvengta ryšio tarp agentų uždarymo prieš užduoties atlikimą, ypač kai užduoties vykdymas užtrunka ilgiau.

### A2A privalumai

• **Pagerintas bendradarbiavimas**: leidžia agentams iš skirtingų tiekėjų ir platformų bendrauti, dalintis kontekstu ir dirbti kartu, palengvindamas sklandų automatizavimą tarp tradiciškai atskirtų sistemų.

• **Modelio pasirinkimo lankstumas**: kiekvienas A2A agentas gali pasirinkti, kurį LLM naudoti užklausoms aptarnauti, leidžiant optimizuoti ar pritaikyti modelius pagal agentą, skirtingai nei vienas LLM ryšys kai kuriuose MCP scenarijuose.

• **Integruota autentifikacija**: autentifikacija tiesiogiai įtraukta į A2A protokolą, suteikiant stiprią saugumo sistemą agentų sąveikai.

### A2A pavyzdys

![A2A Diagram](../../../translated_images/lt/A2A-Diagram.8666928d648acc26.webp)

Išplėskime mūsų kelionių užsakymo scenarijų, bet šį kartą naudodami A2A.

1. **Vartotojo užklausa daugiaagentinei sistemai**: vartotojas sąveikauja su „Kelionių agentu“ A2A klientu/agentu, pvz., sakydamas: „Prašau užsakyti visą kelionę į Honolulu kitai savaitei, įskaitant skrydžius, viešbutį ir automobilio nuomą“.

2. **Kelionių agento organizavimas**: Kelionių agentas gauna šią sudėtingą užklausą. Naudodamas savo LLM jis įvertina užduotį ir nusprendžia, kad reikia sąveikauti su kitais specializuotais agentais.

3. **Agentų tarpusavio komunikacija**: Kelionių agentas tada naudoja A2A protokolą, kad prisijungtų prie žemyninių agentų, tokių kaip „Aviakompanijos agentas“, „Viešbučio agentas“ ir „Automobilių nuomos agentas“, kuriuos kūrė skirtingos kompanijos.

4. **Deleguotas užduočių vykdymas**: Kelionių agentas siunčia konkrečias užduotis šiems specializuotiems agentams (pvz., „Rasti skrydžius į Honolulu“, „Užsakyti viešbutį“, „Išsinuomoti automobilį“). Kiekvienas iš šių specializuotų agentų, naudodamas savo LLM ir įrankius (kurie gali būti patys MCP serveriai), atlieka savo užsakymo dalį.

5. **Sujungtas atsakas**: kai visi žemyniniai agentai baigia užduotis, Kelionių agentas suveda rezultatus (skrydžio duomenis, viešbučio patvirtinimą, automobilio nuomą) ir pateikia išsamų, pokalbio stiliaus atsakymą vartotojui.

## Natūralios kalbos tinklas (NLWeb)

Tinklalapiai jau ilgą laiką buvo pagrindinė vartotojų priemonė prieigai prie informacijos ir duomenų internete.

Pažiūrėkime į skirtingus NLWeb komponentus, NLWeb naudą ir pavyzdį, kaip veikia mūsų kelionių programa.

### NLWeb komponentai

- **NLWeb programa (pagrindinis paslaugos kodas)**: sistema, kuri apdoroja natūralios kalbos klausimus. Ji jungia platformos dalis, kad sukurtų atsakymus. Galima ją laikyti kaip **variklį, kuris veikia natūralios kalbos funkcijas** tinklalapyje.

- **NLWeb protokolas**: tai **vieningas taisyklių rinkinys natūralios kalbos sąveikai** su tinklalapiu. Jis grąžina atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pagrindą „DI tinklui“, taip kaip HTML leido dalytis dokumentais internete.

- **MCP serveris (Modelio konteksto protokolo galinis taškas)**: Kiekviena NLWeb sistema taip pat veikia kaip **MCP serveris**. Tai reiškia, kad ji gali **dalintis įrankiais (pvz., „klausk“ metodu) ir duomenimis** su kitomis DI sistemomis. Praktikoje tai leidžia tinklalapio turinį ir galimybes naudoti DI agentams, taip versdama svetainę tapti platesnės „agentų ekosistemos“ dalimi.

- **Įterpimo (Embedding) modeliai**: šie modeliai skirti **paversti tinklalapio turinį į skaitines atvaizdavimo formas, vadinamas vektoriais** (embeddingais). Šie vektoriai užfiksuoja prasmę taip, kad kompiuteriai gali juos palyginti ir ieškoti. Jie saugomi specialioje duomenų bazėje, o vartotojai gali pasirinkti, kurį įterpimo modelį naudoti.

- **Vektorinė duomenų bazė (paieškos mechanizmas)**: ši duomenų bazė **saugo tinklalapio turinio embeddingus**. Kai kas nors pateikia klausimą, NLWeb patikrina vektorinę duomenų bazę, kad greitai rastų aktualiausią informaciją. Ji pateikia greitą galimų atsakymų sąrašą, surikiuotą pagal panašumą. NLWeb palaiko įvairias vektorinės saugyklos sistemas, tokias kaip Qdrant, Snowflake, Milvus, Azure AI Search ir Elasticsearch.

### NLWeb pavyzdys

![NLWeb](../../../translated_images/lt/nlweb-diagram.c1e2390b310e5fe4.webp)

Vėl pažiūrėkime į mūsų kelionių užsakymo tinklalapį, bet šį kartą – jis pagrįstas NLWeb.

1. **Duomenų įterpimas**: kelionių tinklalapio esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, turų paketai) suformatuoti naudojant Schema.org arba įkelti per RSS kanalus. NLWeb įrankiai gauna šiuos struktūruotus duomenis, sukuria embeddingus ir saugo juos vietinėje ar nuotolinėje vektorinėje duomenų bazėje.

2. **Natūralios kalbos užklausa (Žmogus)**: vartotojas apsilanko tinklalapyje ir vietoje naršymo meniu įveda į pokalbių sąsają: „Rask man šeimai tinkamą viešbutį Honolulu su baseinu kitai savaitei“.

3. **NLWeb apdorojimas**: NLWeb programa gauna šią užklausą. Ji perduoda ją į LLM supratimui ir tuo pačiu ieško savo vektorinėje duomenų bazėje aktualių viešbučių sąrašų.

4. **Tikslūs rezultatai**: LLM padeda interpretuoti paieškos rezultatus iš duomenų bazės, nustatyti geriausius atitikmenis pagal kriterijus „šeimai tinkamas“, „baseinas“ ir „Honolulu“ ir suformuluoti natūralios kalbos atsakymą. Svarbu, kad atsakymas remiasi tikrais tinklalapio katalogo viešbučiais, vengiant išgalvotos informacijos.

5. **DI agentų sąveika**: kadangi NLWeb veikia kaip MCP serveris, išorinis DI kelionių agentas taip pat galėtų prisijungti prie šio tinklalapio NLWeb instancijos. DI agentas galėtų naudoti `ask` MCP metodą užklausai: `ask("Ar viešbutis rekomenduoja veganiškus restoranus Honolulu rajone?")`. NLWeb apdorotų užklausą, pasinaudodamas restoranų informacijos baze (jei ji įkelta) ir pateiktų struktūruotą JSON atsakymą.

### Turite daugiau klausimų apie MCP/A2A/NLWeb?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitikti su kitais besimokančiais, dalyvauti konsultacijose ir gauti atsakymus į savo DI agentų klausimus.

## Ištekliai

- [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb saugykla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft agentų karkasas](https://aka.ms/ai-agents-beginners/agent-framework)

## Ankstesnė pamoka

[DI agentai produkcijoje](../10-ai-agents-production/README.md)

## Kitoji pamoka

[Konteksto inžinerija DI agentams](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->