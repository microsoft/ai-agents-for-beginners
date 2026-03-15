# Atmintis DI agentams 
[![Agentų atmintis](../../../translated_images/lt/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kalbant apie unikalius DI agentų kūrimo privalumus, dažniausiai minimos dvi pagrindinės savybės: gebėjimas kviesti įrankius užduotims atlikti ir gebėjimas gerėti laikui bėgant. Atmintis yra pagrindas kuriant savi-tobulėjančius agentus, kurie gali kurti geresnę patirtį mūsų vartotojams.

Šiame pamokyme apžvelgsime, kas yra atmintis DI agentams, kaip ją valdyti ir panaudoti savo programų naudai.

## Įvadas

Ši pamoka apims:

• **DI agentų atminties supratimas**: Kas yra atmintis ir kodėl ji svarbi agentams.

• **Atminties įgyvendinimas ir saugojimas**: Praktiniai būdai pridėti atminties galimybes jūsų DI agentams, orientuojantis į trumpalaikę ir ilgalaikę atmintį.

• **DI agentų savi-tobulinimas**: Kaip atmintis leidžia agentams mokytis iš ankstesnių sąveikų ir gerėti laikui bėgant.

## Galimos diegimo priemonės

Ši pamoka apima dvi išsamius užrašų knygų (notebook) pamokas:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Diegia atmintį naudojant Mem0 ir Azure AI Search su Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Diegia struktūruotą atmintį naudojant Cognee, automatiškai kuria žinių grafą, paremta embedding’ais, vizualizuoja grafą ir atlieka intelektualų traukimą

## Mokymosi tikslai

Baigę šią pamoką, žinosite, kaip:

• **Atskirti įvairius DI agentų atminties tipus**, įskaitant darbo, trumpalaikę ir ilgalaikę atmintį, taip pat specializuotas formas, tokias kaip persona ir epizodinė atmintis.

• **Įgyvendinti ir valdyti trumpalaikę bei ilgalaikę atmintį DI agentams** naudojant Microsoft Agent Framework, pasinaudojant įrankiais kaip Mem0, Cognee, Whiteboard memory ir integruojant su Azure AI Search.

• **Suprasti principus, lemiamus savi-tobulėjantiems DI agentams**, ir kaip tvirtos atminties valdymo sistemos prisideda prie nuolatinio mokymosi ir prisitaikymo.

## DI agentų atminties supratimas

Sutinku, pagrinde, **atmintis DI agentams reiškia mechanizmus, kurie leidžia jiems išsaugoti ir atgaivinti informaciją**. Ši informacija gali būti specifinės detalės apie pokalbį, vartotojo nuostatos, ankstesni veiksmai arba net išmokti modeliai.

Be atminties DI programos dažnai yra bevalstės (stateless), tai reiškia, kad kiekviena sąveika prasideda nuo nulio. Tai sukelia pasikartojančią ir varginančią vartotojo patirtį, kai agentas „pamiršta“ ankstesnį kontekstą ar nuostatas.

### Kodėl atmintis yra svarbi?

Agento intelektas yra glaudžiai susijęs su jo gebėjimu prisiminti ir panaudoti ankstesnę informaciją. Atmintis leidžia agentams būti:

• **Apmąstančiais**: Mokytis iš ankstesnių veiksmų ir rezultatų.

• **Interaktyviais**: Išlaikyti kontekstą vykstančio pokalbio metu.

• **Proaktyviais ir reagavimo gebančiais**: Numatyti poreikius arba tinkamai reaguoti remiantis istoriniais duomenimis.

• **Autonomiškais**: Veikti savarankiškiau, remiantis saugoma informacija.

Įgyvendinimo tikslas yra padaryti agentus labiau **patikimus ir pajėgius**.

### Atminties tipai

#### Darbinė atmintis

Galvokite apie tai kaip užrašų lapelį, kurį agentas naudoja vienos, einamosios užduoties ar mąstymo proceso metu. Ji laiko momentinę informaciją, reikalingą sekančiam žingsniui apskaičiuoti.

DI agentams darbinė atmintis dažnai fiksuoja svarbiausią informaciją iš pokalbio, net jei visas pokalbio istorija yra ilga arba sutrumpinta. Ji orientuojasi į raktinius elementus, tokius kaip reikalavimai, pasiūlymai, sprendimai ir veiksmai.

**Darbinės atminties pavyzdys**

Kelionių užsakymo agente darbinė atmintis gali laikyti vartotojo dabartinį prašymą, pvz., „Noriu užsakyti kelionę į Paryžių“. Šis konkretus reikalavimas laikomas agentei momentiniame kontekste, kad vadovautųsi dabartine sąveika.

#### Trumpalaikė atmintis

Šio tipo atmintis išlaiko informaciją per vieną pokalbį arba sesiją. Tai yra einamojo pokalbio kontekstas, leidžiantis agentui grįžti prie ankstesnių dialogo posūkių.

**Trumpalaikės atminties pavyzdys**

Jei vartotojas klausia: „Kiek kainuotų skrydis į Paryžių?“ ir vėliau klausia „O kaip dėl apgyvendinimo ten?“, trumpalaikė atmintis užtikrina, kad agentas žino, jog „ten“ reiškia „Paryžių“ tame pačiame pokalbyje.

#### Ilgalaikė atmintis

Tai informacija, kuri išlieka per kelis pokalbius ar sesijas. Ji leidžia agentams prisiminti vartotojo nuostatas, istorines sąveikas ar bendras žinias per ilgą laikotarpį. Tai svarbu personalizavimo atžvilgiu.

**Ilgalaikės atminties pavyzdys**

Ilgalaikė atmintis gali saugoti, kad „Benas mėgsta slidinėti ir lauko veiklas, mėgsta kavą su kalnų vaizdu ir nori vengti sudėtingų slidinėjimo trasų dėl ankstesnės traumos“. Iš ankstesnių sąveikų išmokta informacija veiktų rekomendacijas būsimose kelionių planavimo sesijose, darant jas labai suasmenintas.

#### Personos atmintis

Šis specializuotas atminties tipas padeda agentui suformuoti nuoseklią „asmenybę“ arba „personą“. Ji leidžia agentui prisiminti detales apie save arba jo numatytą vaidmenį, todėl sąveikos tampa sklandesnės ir labiau susitelkusios.

**Personos atminties pavyzdys**
Jei kelionių agentas sukurtas kaip „ekspertas slidinėjimo planavime“, personos atmintis gali stiprinti šį vaidmenį ir daryti įtaką jo atsakymams, kad jie atitiktų eksperto toną ir žinias.

#### Veiklos/Epizodinė atmintis

Ši atmintis saugo žingsnių seką, kurių agentas imasi sudėtingos užduoties metu, įskaitant sėkmes ir nesėkmes. Tai panašu į konkrečių „epizodų“ ar praeities patirčių prisiminimą, kad būtų galima išmokti iš jų.

**Epizodinės atminties pavyzdys**

Jei agentas bandė užsakyti konkretų skrydį, bet tai nepavyko dėl nepasiekiamumo, epizodinė atmintis galėtų užfiksuoti šią nesėkmę, leidžiant agentui bandyti alternatyvius skrydžius arba informuoti vartotoją apie problemą labiau informuotai kitą kartą.

#### Entitetų atmintis

Tai apima konkrečių entitetų (pvz., žmonių, vietų ar daiktų) ir įvykių ištraukimą ir prisiminimą iš pokalbių. Tai leidžia agentui suformuoti struktūruotą supratimą apie aptartus svarbiausius elementus.

**Entitetų atminties pavyzdys**

Iš pokalbio apie praeitą kelionę agentas gali išskirti „Paryžių“, „Eifelio bokštą“ ir „vakarienę restorane Le Chat Noir“ kaip entitetus. Būsimame pokalbyje agentas galėtų prisiminti „Le Chat Noir“ ir pasiūlyti užsakyti naują rezervaciją ten.

#### Struktūruota RAG (Retrieval Augmented Generation)

Nors RAG yra platesnė technika, „Struktūruota RAG“ pabrėžiama kaip galinga atminties technologija. Ji ištraukia tankią, struktūruotą informaciją iš įvairių šaltinių (pokalbių, el. laiškų, vaizdų) ir naudoja ją tikslumui, atgaminimui ir atsakymų greičiui didinti. Skirtingai nei klasikinis RAG, kuris remiasi vien semantiniu panašumu, Struktūruota RAG dirba su informacijos įgimta struktūra.

**Struktūruotos RAG pavyzdys**

Užuot tik derinus raktinius žodžius, Struktūruota RAG galėtų išgauti skrydžio duomenis (paskirties vieta, data, laikas, aviakompanija) iš el. laiško ir saugoti juos struktūrizuotu būdu. Tai leidžia atlikti tikslius užklausimus, pvz., „Kokį skrydį užsakiau į Paryžių antradienį?“

## Atminties įgyvendinimas ir saugojimas

Atminties įgyvendinimas DI agentams apima sisteminį procesą — **atminties valdymą**, kuris susideda iš generavimo, saugojimo, gavimo, integravimo, atnaujinimo ir net „pamiršimo“ (arba ištrynimo) informacijos. Traukimas (retrieval) yra ypač svarbi dalis.

### Specializuoti atminties įrankiai

#### Mem0

Viena iš būdų saugoti ir valdyti agento atmintį yra naudoti specializuotus įrankius, tokius kaip Mem0. Mem0 veikia kaip nuolatinio saugojimo atminties sluoksnis, leidžiantis agentams atgaivinti susijusias sąveikas, saugoti vartotojo nuostatas ir faktinį kontekstą bei mokytis iš sėkmių ir nesėkmių laikui bėgant. Idėja yra ta, kad bevalstiai agentai tampa būseną palaikančiais.

Tai veikia per **dviejų fazių atminties vamzdelį: ištraukimas ir atnaujinimas**. Pirma, pranešimai, pridėti prie agente esančio siūlo, siunčiami į Mem0 paslaugą, kuri naudoja Didelį Kalbų Modelį (LLM) pokalbio istorijai santrumpinti ir naujus prisiminimus ištraukti. Vėliau LLM varoma atnaujinimo fazė nusprendžia, ar pridėti, pakeisti ar ištrinti šiuos prisiminimus, saugodama juos hibridiniame duomenų saugykloje, kuri gali apimti vektorių, grafų ir raktas-reikšmė duomenų bazes. Ši sistema taip pat palaiko įvairius atminties tipus ir gali įtraukti grafų atmintį valdyti santykiams tarp entitetų.

#### Cognee

Kitas galingas požiūris yra naudoti **Cognee**, atviro kodo semantinę atmintį DI agentams, kuri transformuoja struktūruotus ir nestruktūruotus duomenis į užklausomus žinių grafus, paremtus embedding’ais. Cognee suteikia **dvigubos saugyklos architektūrą**, jungiančią vektorių panašumo paiešką su grafų santykiais, leidžiančią agentams suprasti ne tik tai, kas yra panašu, bet ir kaip sąvokos tarpusavyje susijusios.

Jis puikiai tinka **hibridiniam traukimo būdui**, kuris maišo vektorių panašumą, grafinę struktūrą ir LLM samprotavimą — nuo žaliųjų dalelių paieškos iki grafams jautraus klausimų-atsakymų. Sistema palaiko **gyvą atmintį**, kuri vystosi ir auga, likdama užklausoma kaip vienas susietas grafas, palaikantis tiek trumpalaikį sesijos kontekstą, tiek ilgalaikę nuolatinę atmintį.

Cognee užrašų knygos pamoka ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruoja šio vieningo atminties sluoksnio kūrimą, pateikdama praktinius pavyzdžius, kaip įtraukti įvairius duomenų šaltinius, vizualizuoti žinių grafą ir užklausti naudojant skirtingas paieškos strategijas, pritaikytas konkretiems agentų poreikiams.

### Atminties saugojimas naudojant RAG

Be specializuotų atminties įrankių, tokių kaip Mem0, galite pasinaudoti patikimomis paieškos paslaugomis, tokiomis kaip **Azure AI Search**, kaip fonu atminties saugojimui ir traukimui, ypač struktūruotai RAG.

Tai leidžia pagrįsti agento atsakymus jūsų duomenimis, užtikrinant tikslesnius ir aktualius atsakymus. Azure AI Search gali būti naudojama saugoti vartotojui specifines kelionių atmintis, produktų katalogus ar bet kokias kitas domeno specifines žinias.

Azure AI Search palaiko galimybes, tokias kaip **Struktūruota RAG**, kuri puikiai tinka tankios, struktūruotos informacijos išgavimui ir traukimui iš didelių duomenų rinkinių, tokių kaip pokalbių istorijos, el. laiškai ar net vaizdai. Tai suteikia „žmogiškus pranokstantį“ tikslumą ir atgaivinimą, palyginti su tradiciniais teksto gabalų ir embedding’ų požiūriais.

## DI agentų savi-tobulinimas

Dažnas savi-tobulėjančių agentų modelis apima atskirą **„žinių agentą“**. Šis atskiras agentas stebi pagrindinį pokalbį tarp vartotojo ir pirminio agento. Jo rolė yra:

1. **Nustatyti vertingą informaciją**: Nuspręsti, ar bet kuri pokalbio dalis verta išsaugojimo kaip bendros žinios ar specifinė vartotojo nuostata.

2. **Išgauti ir apibendrinti**: Išfiltruoti esminį išmokimą arba nuostatą iš pokalbio.

3. **Saugojimas žinių bazėje**: Išsaugoti ištraukta informaciją, dažnai vektorių duomenų bazėje, kad ją būtų galima vėliau atkurti.

4. **Papildyti būsimus užklausimus**: Kai vartotojas inicijuoja naują užklausą, žinių agentas atkuria susijusią saugomą informaciją ir prideda ją prie vartotojo užklausos, suteikdamas pagrindinį kontekstą pirminiam agentui (panašiai kaip RAG).

### Atminties optimizacijos

• **Vėlinimo (latency) valdymas**: Kad nesulėtintumėte vartotojo sąveikų, pradžioje galima naudoti pigesnį, greitesnį modelį, kad greitai patikrintų, ar informacija verta saugoti arba atkurti, o sudėtingesnį ištraukimo/traukimo procesą kvieti tik esant būtinybei.

• **Žinių bazės priežiūra**: Augant žinių bazei, rečiau naudojama informacija gali būti perkelta į „šaltą saugyklą“, siekiant valdyti kaštus.

## Turite daugiau klausimų apie agentų atmintį?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) — susitikite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo DI agentų klausimus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas patikimu šaltiniu. Jei informacija yra kritiškai svarbi, rekomenduojame pasitelkti profesionalų žmogaus vertimą. Už bet kokius nesusipratimus ar neteisingą interpretaciją, kylančius dėl šio vertimo naudojimo, mes neatsakome.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->