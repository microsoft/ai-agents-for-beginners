# Atmintis AI Agentams 
[![Agentų atmintis](../../../translated_images/lt/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kalbant apie unikalius AI Agentų kūrimo privalumus dažniausiai minimos dvi pagrindinės savybės: galimybė iškviesti įrankius užduotims atlikti ir gebėjimas tobulėti laikui bėgant. Atmintis yra saviugdos agento, kuris gali kurti geresnes patirtis mūsų vartotojams, pagrindas.

Šiame pamokoje apžvelgsime, kas yra atmintis AI agentams, kaip ją valdyti ir kaip ją panaudoti mūsų programų naudai.

## Įvadas

Ši pamoka apims:

• **AI agentų atminties supratimą**: Kas yra atmintis ir kodėl ji svarbi agentams.

• **Atminties įgyvendinimą ir saugojimą**: Praktinius metodus, kaip pridėti atminties funkcijas jūsų AI agentams, sutelkiant dėmesį į trumpalaikę ir ilgalaikę atmintį.

• **Kaip padaryti AI agentus savitobulinančius**: Kaip atmintis leidžia agentams mokytis iš ankstesnių sąveikų ir tobulėti laikui bėgant.

## Galimi įgyvendinimai

Ši pamoka apima du išsamius užrašų knygelių vadovus:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Atminties įgyvendinimas naudojant Mem0 ir Azure AI Search su Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Įgyvendina struktūruotą atmintį naudojant Cognee, automatiškai kuriant žinių grafą, pagrįstą įterpimais, vizualizuojant grafą ir intelektualų paiešką

## Mokymosi tikslai

Baigę šią pamoką, žinosite, kaip:

• **Atskirti įvairius AI agentų atminties tipus**, įskaitant darbo, trumpalaikę ir ilgalaikę atmintį, taip pat specializuotas formas, tokias kaip persona ir epizodinė atmintis.

• **Įgyvendinti ir valdyti trumpalaikę bei ilgalaikę atmintį AI agentams** naudojant Microsoft Agent Framework, pasitelkiant įrankius kaip Mem0, Cognee, Whiteboard atmintį ir integruojant su Azure AI Search.

• **Suprasti savitobulinančių AI agentų principus** ir kaip patikimos atminties valdymo sistemos prisideda prie nuolatinio mokymosi ir prisitaikymo.

## AI agentų atminties supratimas

Iš esmės **atmintis AI agentams reiškia mechanizmus, leidžiančius jiems išlaikyti ir prisiminti informaciją**. Ši informacija gali būti specifinės ištraukos apie pokalbį, vartotojo pageidavimus, ankstesnius veiksmus ar net išmoktus modelius.

Be atminties, AI programos dažnai yra bevalstės, t. y. kiekviena sąveika prasideda nuo nulio. Tai sukelia pasikartojančią ir erzinančią vartotojo patirtį, kur agentas „pamiršta“ ankstesnį kontekstą arba pageidavimus.

### Kodėl atmintis yra svarbi?

Agento intelektas glaudžiai susijęs su jo gebėjimu prisiminti ir panaudoti ankstesnę informaciją. Atmintis leidžia agentams būti:

• **Reflektuojančiais**: Mokantis iš ankstesnių veiksmų ir rezultatų.

• **Interaktyviais**: Išlaikyti kontekstą vykstančio pokalbio metu.

• **Proaktyviais ir reaktyviais**: Numatyti poreikius arba tinkamai reaguoti remiantis istorine informacija.

• **Autonomiškais**: Veikti savarankiškiau remiantis saugoma informacija.

Atminties įgyvendinimo tikslas – padaryti agentus **patikimesniais ir pajėgesniais**.

### Atminties tipai

#### Darbo atmintis

Galvokite apie tai kaip apie užrašų lapą, kurį agentas naudoja vienos einamos užduoties ar minties proceso metu. Ji laiko būtiną informaciją, reikalingą kitam žingsniui apskaičiuoti.

AI agentams darbo atmintis dažnai kaupia svarbiausią informaciją iš pokalbio, net jei visas pokalbio istorijos ilgis yra ilgas arba sutrumpintas. Jos dėmesys sutelktas į pagrindinių elementų išgavimą, tokių kaip reikalavimai, pasiūlymai, sprendimai ir veiksmai.

**Darbo atminties pavyzdys**

Kelionių užsakymo agentui darbo atmintis gali užfiksuoti dabartinį vartotojo užklausą, pavyzdžiui, „Noriu užsakyti kelionę į Paryžių“. Šis konkretus reikalavimas saugomas agente esamame kontekste, kad nukreiptų dabartinę sąveiką.

#### Trumpalaikė atmintis

Šis atminties tipas saugo informaciją viso vieno pokalbio ar sesijos metu. Tai dabartinio pokalbio kontekstas, leidžiantis agentui prisiminti ankstesnius dialogo posūkius.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK pavyzdžiuose tai atitinka `AgentSession`, sukurtą su `agent.create_session()`. Sesija yra karkaso įmontuota trumpalaikė atmintis: ji laiko pokalbio kontekstą, kol ta pati sesija naudojama, bet šis kontekstas nesaugomas, kai sesija baigiasi arba programa paleidžiama iš naujo. Naudokite ilgalaikę atmintį faktams ir pageidavimams, kurių reikia išlaikyti per kelias sesijas, paprastai per duomenų bazę, vektorinį indeksą arba kitą nuolatinę saugyklą.

**Trumpalaikės atminties pavyzdys**

Jei vartotojas klausia: „Kiek kainuotų skrydis į Paryžių?“ ir vėliau klausia „O kaip dėl apgyvendinimo ten?“, trumpalaikė atmintis užtikrina, kad agentas supranta, kad „ten“ reiškia „Paryžių“ tame pačiame pokalbyje.

#### Ilgalaikė atmintis

Tai informacija, kuri išlieka per kelis pokalbius ar sesijas. Ji leidžia agentams prisiminti vartotojo pageidavimus, istorines sąveikas arba bendrą žinių bagažą ilgesnį laiką. Tai svarbu personalizacijai.

**Ilgalaikės atminties pavyzdys**

Ilgalaikė atmintis gali saugoti, kad „Benas mėgsta slidinėjimą ir lauko veiklas, mėgsta kavą su kalnų vaizdu ir nori vengti pažangių slidinėjimo trasų dėl ankstesnės traumos“. Ši informacija, išmokta iš ankstesnių sąveikų, veikia rekomendacijas būsimose kelionių planavimo sesijose, darant jas labai personalizuotas.

#### Personos atmintis

Šis specializuotas atminties tipas padeda agentui sukurti nuoseklią „asmenybę“ arba „personą“. Tai leidžia agentui prisiminti detales apie save ar savo numatytą vaidmenį, darant sąveikas sklandesnes ir tikslingesnes.

**Personos atminties pavyzdys**
Jei kelionių agentas suprogramuotas būti „ekspertu slidinėjimo planuotoju“, personos atmintis gali sustiprinti šį vaidmenį, lemiančią atsakymus, kurie atitinka eksperto toną ir žinias.

#### Darbo eigos/Epizodinė atmintis

Ši atmintis saugo agento žingsnių seką sudėtingos užduoties metu, įskaitant sėkmes ir nesėkmes. Tai tarsi prisiminimas apie konkrečius „epizodus“ ar praeities patirtis, iš kurių mokomasi.

**Epizodinės atminties pavyzdys**

Jei agentas bandė užsakyti konkretų skrydį, bet tai nepavyko dėl neprieinamumo, epizodinė atmintis gali užfiksuoti šią nesėkmę, leidžianti agentui bandyti kitus skrydžius ar labiau informuotai pranešti naudotojui apie problemą kito bandymo metu.

#### Objektų (Entity) atmintis

Tai apima specifinių objektų (pvz., žmonių, vietų ar daiktų) ir įvykių ištraukimą bei įsimintį iš pokalbių. Leidžia agentui kurti struktūruotą supratimą apie svarbiausias aptartas temas.

**Objektų atminties pavyzdys**

Iš pokalbio apie praeitą kelionę agentas gali išgauti „Paryžių“, „Eifelio bokštą“ ir „vakarienę Le Chat Noir restorane“ kaip objektus. Ateityje agentas galėtų prisiminti „Le Chat Noir“ ir pasiūlyti padaryti naują rezervaciją ten.

#### Struktūrizuotas RAG (Retrieval Augmented Generation)

Nors RAG yra platesnė technika, "Struktūrizuotas RAG" išskiriamas kaip galinga atminties technologija. Ji ištraukia tankią, struktūruotą informaciją iš įvairių šaltinių (pokalbių, el. laiškų, paveikslėlių) ir naudoja ją tikslumui, atkūrimui ir greičiui gerinti atsakymuose. Skirtingai nuo klasikinio RAG, kuris remiasi tik semantiniu panašumu, Struktūrizuotas RAG dirba su informacijos struktūra.

**Struktūrizuoto RAG pavyzdys**

Vietoje vien tik raktinių žodžių sutapimo, Struktūrizuotas RAG galėtų ištirti skrydžio duomenis (tikslą, datą, laiką, oro linijas) iš el. laiško ir saugoti juos struktūrizuotu formatu. Tai leidžia tikslinius užklausimus, pvz., „Kokį skrydį į Paryžių užsakiau antradienį?“

## Atminties įgyvendinimas ir saugojimas

Atminties įgyvendinimas AI agentams apima sistemingą procesą – **atminties valdymą**, kuris apima informacijos generavimą, saugojimą, paiešką, integravimą, atnaujinimą ir netgi „pamiršimą“ (arba ištrynimą). Paieška yra ypač svarbus aspektas.

### Specializuoti atminties įrankiai

#### Mem0

Vienas iš būdų saugoti ir valdyti agentų atmintį yra naudoti specializuotus įrankius, kaip Mem0. Mem0 veikia kaip nuolatinės atminties sluoksnis, leidžiantis agentams prisiminti svarbias sąveikas, saugoti vartotojo pageidavimus ir faktinį kontekstą, ir mokytis iš sėkmių bei nesėkmių laikui bėgant. Idėja yra, kad bevalstės agentūros virsta būsenos turinčiomis.

Tai veikia per **dviejų etapų atminties procesą: išgavimą ir atnaujinimą**. Pirma, agentui pridėtos žinutės siunčiamos Mem0 paslaugai, kuri naudoja Didelį kalbos modelį (LLM) pokalbio istorijai santraukai ir naujų atmintinių išgavimui. Vėliau, LLM vedamas atnaujinimo etapas nusprendžia, ar pridėti, modifikuoti ar ištrinti šias atmintis, saugodamas jas hibridinėje duomenų saugykloje, galinčioje apimti vektorinę, grafų ir raktų-reikšmių duomenų bazes. Ši sistema palaiko įvairius atminties tipus ir gali įtraukti grafų atmintį valdyti santykiams tarp objektų.

#### Cognee

Kitas galingas požiūris yra naudoti **Cognee**, atvirojo kodo semantinę atmintį AI agentams, kuri paverčia struktūruotus ir nestruktūruotus duomenis į užklausomis pasiekiamus žinių grafus, pagrįstus įterpimais. Cognee teikia **dvipusę saugyklos architektūrą**, derindama vektorinę panašumo paiešką su grafų santykiais, leidžiančią agentams suprasti ne tik panašumas informacijos, bet ir kaip sąvokos susijusios.

Ji pasižymi **hibridine paieška**, kuri sujungia vektorinius panašumus, grafų struktūrą ir LLM sprendimą – nuo žalių fragmentų paieškos iki klausimų atsakymo, žinant grafą. Sistema palaiko **gyvą atmintį**, kuri vystosi ir auga, tuo pačiu lieka užklausomis pasiekiama kaip vienas susietas grafas, palaikydama trumpalaikį sesijos kontekstą ir ilgalaikę nuolatinę atmintį.

Cognee užrašų knygelės vadovas ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruoja, kaip kurti vieningą atminties sluoksnį, su praktiniais pavyzdžiais, kaip priimti įvairius duomenų šaltinius, vizualizuoti žinių grafą ir užduoti klausimus naudojant skirtingas paieškos strategijas, pritaikytas specifiniams agentų poreikiams.

### Atminties saugojimas su RAG

Be specializuotų atminties įrankių kaip Mem0, galima naudoti patikimas paieškos paslaugas, tokias kaip **Azure AI Search, kaip pagrindinę atminties saugojimo ir atgaivinimo sistemą**, ypač struktūrizuotam RAG.

Tai leidžia paremti agentų atsakymus jūsų pačių duomenimis, užtikrinant daug tinkamesnius ir tikslesnius atsakymus. Azure AI Search gali būti panaudotas saugoti vartotojo kelionių atminties, produktų katalogus ar bet kokias kitas srities žinias.

Azure AI Search palaiko galimybes, tokias kaip **Struktūrizuotas RAG**, kuris išsiskiria gebėjimu išgauti ir atgaivinti tankią, struktūruotą informaciją iš didelių duomenų rinkinių kaip pokalbių istorijos, el. laiškai ar net paveikslėliai. Tai suteikia „žmogišką tikslumą ir atkūrimą“ palyginus su tradiciniais teksto fragmentų ir įterpimų metodais.

## Kaip padaryti AI agentus savitobulinančiais

Bendras savitobulinančių agentų modelis apima **„žinių agento“** įvedimą. Šis atskiras agentas stebi pagrindinį vartotojo ir pirminio agente pokalbį. Jo vaidmuo yra:

1. **Nustatyti vertingą informaciją**: Nustatyti, ar bet kuri pokalbio dalis verta būti išsaugota kaip bendros žinios arba specifinis vartotojo pageidavimas.

2. **Ištraukti ir santraukinti**: Išskirti esminį mokymąsi ar pageidavimą iš pokalbio.

3. **Saugojimas žinių bazėje**: Išsaugoti šią informaciją dažnai vektorinėje duomenų bazėje, kad ją būtų galima atkurti vėliau.

4. **Papildyti būsimus užklausimus**: Kai vartotojas inicijuoja naują užklausą, žinių agentas suranda susijusią saugomą informaciją ir priduria ją prie vartotojo prašymo, suteikdamas pagrindinį kontekstą pirminiam agentui (panašiai kaip RAG).

### Atminties optimizacijos

• **Vėlinimo valdymas**: Siekiant išvengti vartotojo sąveikos sulėtėjimo, iš pradžių galima naudoti pigesnį, greitesnį modelį, kad greitai patikrintų, ar informacija verta saugojimo ar paieškos, o sudėtingesnį išgavimą/paiešką įjungti tik prireikus.

• **Žinių bazės priežiūra**: Augančiai žinių bazei mažiau naudojama informacija gali būti perkeliama į „šaltąją saugyklą“ siekiant valdyti kaštus.

## Turite daugiau klausimų apie agentų atmintį?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) susitikti su kitais besimokančiais, dalyvauti konsultacijose ir gauti atsakymus į savo AI agentų klausimus.
## Ankstesnė pamoka

[AI agentų konteksto inžinerija](../12-context-engineering/README.md)

## Kitoji pamoka

[Microsoft Agent Framework tyrinėjimas](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->