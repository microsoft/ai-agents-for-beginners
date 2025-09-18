<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:26:20+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "lt"
}
-->
# Atmintis dirbtinio intelekto agentams

Kalbant apie unikalius dirbtinio intelekto agentų privalumus, dažniausiai aptariami du dalykai: gebėjimas naudoti įrankius užduotims atlikti ir gebėjimas tobulėti laikui bėgant. Atmintis yra pagrindas kuriant savarankiškai tobulėjančius agentus, kurie gali suteikti geresnę patirtį mūsų vartotojams.

Šioje pamokoje aptarsime, kas yra atmintis dirbtinio intelekto agentams, kaip ją valdyti ir panaudoti mūsų programų naudai.

## Įvadas

Šioje pamokoje aptarsime:

• **Dirbtinio intelekto agentų atminties supratimą**: kas yra atmintis ir kodėl ji būtina agentams.

• **Atminties įgyvendinimą ir saugojimą**: praktinius metodus, kaip pridėti atminties funkcijas dirbtinio intelekto agentams, akcentuojant trumpalaikę ir ilgalaikę atmintį.

• **Dirbtinio intelekto agentų savarankišką tobulėjimą**: kaip atmintis leidžia agentams mokytis iš ankstesnių sąveikų ir tobulėti laikui bėgant.

## Mokymosi tikslai

Baigę šią pamoką, jūs sužinosite, kaip:

• **Atskirti skirtingus dirbtinio intelekto agentų atminties tipus**, įskaitant darbinę, trumpalaikę ir ilgalaikę atmintį, taip pat specializuotas formas, tokias kaip asmenybės ir epizodinė atmintis.

• **Įgyvendinti ir valdyti trumpalaikę ir ilgalaikę atmintį dirbtinio intelekto agentams**, naudojant Semantic Kernel sistemą, pasitelkiant įrankius, tokius kaip Mem0 ir Whiteboard atmintis, bei integruojant su Azure AI Search.

• **Suprasti savarankiškai tobulėjančių dirbtinio intelekto agentų principus** ir kaip tvirtos atminties valdymo sistemos prisideda prie nuolatinio mokymosi ir prisitaikymo.

## Dirbtinio intelekto agentų atminties supratimas

Iš esmės, **dirbtinio intelekto agentų atmintis reiškia mechanizmus, leidžiančius jiems išsaugoti ir prisiminti informaciją**. Ši informacija gali būti specifinės detalės apie pokalbį, vartotojo pageidavimus, ankstesnius veiksmus ar net išmokti modeliai.

Be atminties dirbtinio intelekto programos dažnai yra be būsenos, tai reiškia, kad kiekviena sąveika prasideda nuo nulio. Tai sukelia pasikartojančią ir varginančią vartotojo patirtį, kai agentas „pamiršta“ ankstesnį kontekstą ar pageidavimus.

### Kodėl atmintis svarbi?

Agentų intelektas yra glaudžiai susijęs su jų gebėjimu prisiminti ir panaudoti ankstesnę informaciją. Atmintis leidžia agentams būti:

• **Refleksyviems**: Mokytis iš ankstesnių veiksmų ir rezultatų.

• **Interaktyviems**: Išlaikyti kontekstą per vykstantį pokalbį.

• **Proaktyviems ir reaktyviems**: Nuspėti poreikius arba tinkamai reaguoti remiantis istorine informacija.

• **Autonomiškiems**: Veikti savarankiškiau, remiantis sukauptomis žiniomis.

Atminties įgyvendinimo tikslas yra padaryti agentus **patikimesnius ir pajėgesnius**.

### Atminties tipai

#### Darbinė atmintis

Tai tarsi užrašų lapelis, kurį agentas naudoja vykdydamas vieną užduotį ar minties procesą. Ji saugo tiesioginę informaciją, reikalingą kitam žingsniui atlikti.

Dirbtinio intelekto agentams darbinė atmintis dažnai fiksuoja svarbiausią informaciją iš pokalbio, net jei visas pokalbio istorija yra ilga ar sutrumpinta. Ji sutelkia dėmesį į pagrindinių elementų, tokių kaip reikalavimai, pasiūlymai, sprendimai ir veiksmai, išskyrimą.

**Darbinės atminties pavyzdys**

Kelionių rezervavimo agentui darbinė atmintis gali užfiksuoti vartotojo dabartinį prašymą, pavyzdžiui, „Noriu užsisakyti kelionę į Paryžių“. Šis konkretus reikalavimas laikomas agento tiesioginiame kontekste, kad būtų galima vadovautis dabartine sąveika.

#### Trumpalaikė atmintis

Ši atmintis saugo informaciją vieno pokalbio ar sesijos metu. Tai yra dabartinio pokalbio kontekstas, leidžiantis agentui grįžti prie ankstesnių dialogo posūkių.

**Trumpalaikės atminties pavyzdys**

Jei vartotojas klausia: „Kiek kainuotų skrydis į Paryžių?“ ir vėliau priduria: „O kaip dėl apgyvendinimo ten?“, trumpalaikė atmintis užtikrina, kad agentas žinotų, jog „ten“ reiškia „Paryžių“ tame pačiame pokalbyje.

#### Ilgalaikė atmintis

Tai informacija, kuri išlieka per kelis pokalbius ar sesijas. Ji leidžia agentams prisiminti vartotojo pageidavimus, istorines sąveikas ar bendras žinias per ilgesnį laikotarpį. Tai svarbu personalizacijai.

**Ilgalaikės atminties pavyzdys**

Ilgalaikė atmintis gali saugoti informaciją, kad „Benui patinka slidinėjimas ir lauko veikla, mėgsta kavą su kalnų vaizdu ir vengia sudėtingų slidinėjimo trasų dėl ankstesnės traumos“. Ši informacija, išmokta iš ankstesnių sąveikų, daro būsimus kelionių planavimo pasiūlymus labai personalizuotus.

#### Asmenybės atmintis

Ši specializuota atmintis padeda agentui sukurti nuoseklią „asmenybę“ ar „vaidmenį“. Ji leidžia agentui prisiminti detales apie save ar savo numatytą vaidmenį, kad sąveika būtų sklandesnė ir labiau orientuota.

**Ilgalaikės atminties pavyzdys**

Jei kelionių agentas yra sukurtas kaip „ekspertas slidinėjimo planuotojas“, asmenybės atmintis gali sustiprinti šį vaidmenį, paveikdama jo atsakymus, kad jie atitiktų eksperto toną ir žinias.

#### Darbo eiga/Epizodinė atmintis

Ši atmintis saugo veiksmų seką, kurią agentas atlieka vykdydamas sudėtingą užduotį, įskaitant sėkmes ir nesėkmes. Tai tarsi prisiminimas apie konkrečius „epizodus“ ar ankstesnes patirtis, kad iš jų būtų galima mokytis.

**Epizodinės atminties pavyzdys**

Jei agentas bandė užsisakyti konkretų skrydį, bet nepavyko dėl vietų trūkumo, epizodinė atmintis galėtų užfiksuoti šią nesėkmę, leidžiant agentui bandyti alternatyvius skrydžius arba informuoti vartotoją apie problemą labiau informuotu būdu per kitą bandymą.

#### Subjekto atmintis

Tai apima specifinių subjektų (pvz., žmonių, vietų ar daiktų) ir įvykių iš pokalbių išskyrimą ir prisiminimą. Tai leidžia agentui sukurti struktūruotą supratimą apie pagrindinius aptartus elementus.

**Subjekto atminties pavyzdys**

Iš pokalbio apie ankstesnę kelionę agentas galėtų išskirti „Paryžių“, „Eifelio bokštą“ ir „vakarienę restorane Le Chat Noir“. Per būsimą sąveiką agentas galėtų prisiminti „Le Chat Noir“ ir pasiūlyti ten rezervuoti naują vakarienę.

#### Struktūruotas RAG (Retrieval Augmented Generation)

Nors RAG yra platesnė technika, „Struktūruotas RAG“ išskiriamas kaip galinga atminties technologija. Jis ištraukia tankią, struktūruotą informaciją iš įvairių šaltinių (pokalbių, el. laiškų, vaizdų) ir naudoja ją tikslumui, prisiminimui ir greičiui atsakymuose pagerinti. Skirtingai nuo klasikinio RAG, kuris remiasi vien semantiniu panašumu, Struktūruotas RAG dirba su informacijos vidine struktūra.

**Struktūruoto RAG pavyzdys**

Užuot tik atitikęs raktinius žodžius, Struktūruotas RAG galėtų analizuoti skrydžio detales (kelionės tikslą, datą, laiką, oro linijas) iš el. laiško ir saugoti jas struktūruotu būdu. Tai leidžia tiksliai užklausti, pvz., „Kokį skrydį užsisakiau į Paryžių antradienį?“

## Atminties įgyvendinimas ir saugojimas

Atminties įgyvendinimas dirbtinio intelekto agentams apima sistemingą **atminties valdymo** procesą, kuris apima informacijos generavimą, saugojimą, išgavimą, integravimą, atnaujinimą ir net „pamiršimą“ (arba ištrynimą). Išgavimas yra ypač svarbus aspektas.

### Specializuoti atminties įrankiai

Vienas iš būdų saugoti ir valdyti agento atmintį yra naudoti specializuotus įrankius, tokius kaip Mem0. Mem0 veikia kaip nuolatinis atminties sluoksnis, leidžiantis agentams prisiminti svarbias sąveikas, saugoti vartotojo pageidavimus ir faktinį kontekstą bei mokytis iš sėkmių ir nesėkmių laikui bėgant. Idėja yra ta, kad be būsenos agentai tampa būseniniais.

Jis veikia per **dviejų etapų atminties vamzdyną: ištraukimas ir atnaujinimas**. Pirma, pranešimai, pridėti prie agento gijos, siunčiami į Mem0 paslaugą, kuri naudoja didelį kalbos modelį (LLM), kad apibendrintų pokalbio istoriją ir ištrauktų naujas atmintis. Vėliau LLM valdomas atnaujinimo etapas nustato, ar pridėti, modifikuoti ar ištrinti šias atmintis, saugant jas hibridiniame duomenų saugykloje, kuri gali apimti vektorių, grafų ir raktų-reikšmių duomenų bazes. Ši sistema taip pat palaiko įvairius atminties tipus ir gali įtraukti grafų atmintį, skirtą valdyti ryšius tarp subjektų.

### Atminties saugojimas naudojant RAG

Be specializuotų atminties įrankių, tokių kaip Mem0, galite pasinaudoti patikimomis paieškos paslaugomis, tokiomis kaip **Azure AI Search**, kaip pagrindu atmintims saugoti ir išgauti, ypač struktūruotam RAG.

Tai leidžia pagrįsti agento atsakymus savo duomenimis, užtikrinant aktualesnius ir tikslesnius atsakymus. Azure AI Search gali būti naudojamas vartotojo specifinėms kelionių atmintims, produktų katalogams ar bet kokioms kitoms specifinėms žinioms saugoti.

Azure AI Search palaiko tokias funkcijas kaip **Struktūruotas RAG**, kuris puikiai ištraukia ir išgauna tankią, struktūruotą informaciją iš didelių duomenų rinkinių, tokių kaip pokalbių istorijos, el. laiškai ar net vaizdai. Tai suteikia „antžmogišką tikslumą ir prisiminimą“, palyginti su tradiciniais teksto skaidymo ir įterpimo metodais.

## Dirbtinio intelekto agentų savarankiškas tobulėjimas

Dažnas savarankiškai tobulėjančių agentų modelis apima **„žinių agento“** įvedimą. Šis atskiras agentas stebi pagrindinį pokalbį tarp vartotojo ir pagrindinio agento. Jo vaidmuo yra:

1. **Identifikuoti vertingą informaciją**: Nustatyti, ar kuri nors pokalbio dalis verta išsaugoti kaip bendras žinias ar specifinį vartotojo pageidavimą.

2. **Ištraukti ir apibendrinti**: Išskirti esminę mokymosi ar pageidavimo informaciją iš pokalbio.

3. **Saugojimas žinių bazėje**: Išsaugoti šią ištrauktą informaciją, dažnai vektorinėje duomenų bazėje, kad ją būtų galima išgauti vėliau.

4. **Papildyti būsimus užklausimus**: Kai vartotojas inicijuoja naują užklausą, žinių agentas ištraukia susijusią saugomą informaciją ir prideda ją prie vartotojo užklausos, suteikdamas svarbų kontekstą pagrindiniam agentui (panašiai kaip RAG).

### Atminties optimizavimas

• **Vėlavimo valdymas**: Kad vartotojo sąveika nebūtų sulėtinta, iš pradžių galima naudoti pigesnį, greitesnį modelį, kuris greitai patikrina, ar informacija verta saugoti ar išgauti, sudėtingesnį ištraukimo/išgavimo procesą įjungiant tik tada, kai būtina.

• **Žinių bazės priežiūra**: Augančiai žinių bazei rečiau naudojama informacija gali būti perkelta į „šaltą saugyklą“, kad būtų valdomos išlaidos.

## Turite daugiau klausimų apie konteksto inžineriją?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susipažintumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo klausimus apie dirbtinio intelekto agentus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.