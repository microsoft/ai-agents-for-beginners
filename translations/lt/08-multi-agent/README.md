<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-30T15:01:34+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "lt"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.lt.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Spustelėkite paveikslėlį aukščiau, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Daugiaveiksnių sistemų dizaino šablonai

Kai tik pradėsite dirbti su projektu, kuriame dalyvauja keli agentai, turėsite apsvarstyti daugiaveiksnių sistemų dizaino šabloną. Tačiau gali būti ne iš karto aišku, kada pereiti prie daugiaveiksnių sistemų ir kokie yra jų privalumai.

## Įvadas

Šioje pamokoje siekiame atsakyti į šiuos klausimus:

- Kokiose situacijose daugiaveiksnės sistemos yra tinkamos?
- Kokie yra daugiaveiksnių sistemų privalumai, palyginti su vienu agentu, atliekančiu kelias užduotis?
- Kokie yra pagrindiniai elementai, reikalingi įgyvendinant daugiaveiksnių sistemų dizaino šabloną?
- Kaip užtikrinti matomumą, kaip keli agentai sąveikauja tarpusavyje?

## Mokymosi tikslai

Po šios pamokos turėtumėte gebėti:

- Nustatyti situacijas, kuriose daugiaveiksnės sistemos yra tinkamos.
- Atpažinti daugiaveiksnių sistemų privalumus, palyginti su vienu agentu.
- Suprasti pagrindinius elementus, reikalingus įgyvendinant daugiaveiksnių sistemų dizaino šabloną.

Koks yra platesnis kontekstas?

*Daugiaveiksnės sistemos yra dizaino šablonas, leidžiantis keliems agentams dirbti kartu siekiant bendro tikslo.*

Šis šablonas plačiai naudojamas įvairiose srityse, įskaitant robotiką, autonomines sistemas ir paskirstytąjį skaičiavimą.

## Situacijos, kuriose daugiaveiksnės sistemos yra tinkamos

Taigi, kokios situacijos yra tinkamos daugiaveiksnių sistemų naudojimui? Atsakymas yra tas, kad daugiaveiksnės sistemos yra naudingos daugelyje situacijų, ypač šiais atvejais:

- **Didelės darbo apimtys**: Didelės darbo apimtys gali būti suskaidytos į mažesnes užduotis ir paskirstytos skirtingiems agentams, leidžiant vykdyti užduotis lygiagrečiai ir greičiau jas užbaigti. Pavyzdys galėtų būti didelės apimties duomenų apdorojimo užduotis.
- **Sudėtingos užduotys**: Sudėtingos užduotys, kaip ir didelės darbo apimtys, gali būti suskaidytos į mažesnius subtikslus ir paskirstytos skirtingiems agentams, kiekvienam specializuojantis tam tikroje užduoties dalyje. Geras pavyzdys galėtų būti autonominiai automobiliai, kur skirtingi agentai valdo navigaciją, kliūčių aptikimą ir komunikaciją su kitais automobiliais.
- **Įvairi ekspertizė**: Skirtingi agentai gali turėti įvairią ekspertizę, leidžiančią jiems efektyviau spręsti skirtingus užduoties aspektus nei vienas agentas. Pavyzdys galėtų būti sveikatos priežiūros srityje, kur agentai valdo diagnostiką, gydymo planus ir pacientų stebėjimą.

## Daugiaveiksnių sistemų privalumai, palyginti su vienu agentu

Vieno agento sistema gali gerai veikti paprastoms užduotims, tačiau sudėtingesnėms užduotims daugiaveiksnės sistemos gali suteikti keletą privalumų:

- **Specializacija**: Kiekvienas agentas gali būti specializuotas tam tikrai užduočiai. Vieno agento sistema, neturinti specializacijos, gali susidurti su sunkumais atliekant sudėtingas užduotis, nes agentas gali atlikti užduotį, kuriai jis nėra geriausiai pritaikytas.
- **Skalavimas**: Sistemos skalavimas yra lengvesnis pridedant daugiau agentų, o ne perkraunant vieną agentą.
- **Gedimų tolerancija**: Jei vienas agentas sugenda, kiti gali toliau veikti, užtikrindami sistemos patikimumą.

Pavyzdžiui, tarkime, kad reikia užsakyti kelionę vartotojui. Vieno agento sistema turėtų tvarkyti visus kelionės užsakymo proceso aspektus – nuo skrydžių paieškos iki viešbučių ir automobilių nuomos užsakymo. Tai galėtų sukurti sudėtingą ir monolitinę sistemą, kurią sunku prižiūrėti ir skalauti. Daugiaveiksnių sistemų atveju skirtingi agentai galėtų specializuotis skrydžių paieškoje, viešbučių užsakymuose ir automobilių nuomoje. Tai padarytų sistemą moduliarią, lengviau prižiūrimą ir skalaujamą.

Palyginkime tai su kelionių biuru, kuris veikia kaip šeimos verslas, ir kelionių biuru, kuris veikia kaip franšizė. Šeimos verslas turėtų vieną agentą, tvarkantį visus kelionės užsakymo proceso aspektus, o franšizė turėtų skirtingus agentus, tvarkančius skirtingus kelionės užsakymo proceso aspektus.

## Pagrindiniai elementai, reikalingi įgyvendinant daugiaveiksnių sistemų dizaino šabloną

Prieš įgyvendinant daugiaveiksnių sistemų dizaino šabloną, reikia suprasti pagrindinius elementus, sudarančius šį šabloną.

Grįžkime prie kelionės užsakymo vartotojui pavyzdžio. Šiuo atveju pagrindiniai elementai būtų:

- **Agentų komunikacija**: Agentai, atsakingi už skrydžių paiešką, viešbučių užsakymus ir automobilių nuomą, turi komunikuoti ir dalintis informacija apie vartotojo pageidavimus ir apribojimus. Reikia nuspręsti, kokie bus šios komunikacijos protokolai ir metodai. Pavyzdžiui, skrydžių paieškos agentas turi komunikuoti su viešbučių užsakymo agentu, kad užtikrintų, jog viešbutis būtų užsakytas toms pačioms datoms kaip ir skrydis.
- **Koordinavimo mechanizmai**: Agentai turi koordinuoti savo veiksmus, kad užtikrintų vartotojo pageidavimų ir apribojimų įgyvendinimą. Pavyzdžiui, vartotojas gali norėti viešbučio netoli oro uosto, o apribojimas gali būti tas, kad automobilių nuoma galima tik oro uoste.
- **Agentų architektūra**: Agentai turi turėti vidinę struktūrą, leidžiančią priimti sprendimus ir mokytis iš sąveikos su vartotoju. Pavyzdžiui, skrydžių paieškos agentas turi turėti vidinę struktūrą, leidžiančią priimti sprendimus, kokius skrydžius rekomenduoti vartotojui.
- **Matomumas į daugiaveiksnių sistemų sąveiką**: Reikia turėti matomumą, kaip keli agentai sąveikauja tarpusavyje. Tai gali būti pasiekta naudojant registravimo ir stebėjimo įrankius, vizualizacijos įrankius ir našumo metrikas.
- **Daugiaveiksnių sistemų šablonai**: Yra įvairių šablonų, skirtų daugiaveiksnių sistemų įgyvendinimui, tokių kaip centralizuotos, decentralizuotos ir hibridinės architektūros. Reikia nuspręsti, kuris šablonas geriausiai tinka jūsų atvejui.
- **Žmogaus įsitraukimas**: Daugeliu atvejų sistemoje dalyvaus žmogus, ir reikia nurodyti agentams, kada prašyti žmogaus įsikišimo. Pavyzdžiui, vartotojas gali paprašyti konkretaus viešbučio ar skrydžio, kurio agentai nerekomendavo, arba prašyti patvirtinimo prieš užsakant skrydį ar viešbutį.

## Matomumas į daugiaveiksnių sistemų sąveiką

Svarbu turėti matomumą, kaip keli agentai sąveikauja tarpusavyje. Šis matomumas yra būtinas derinimui, optimizavimui ir bendram sistemos efektyvumui užtikrinti. Norint tai pasiekti, reikia turėti įrankius ir technikas agentų veikloms ir sąveikoms stebėti. Tai gali būti registravimo ir stebėjimo įrankiai, vizualizacijos įrankiai ir našumo metrikos.

Pavyzdžiui, kelionės užsakymo vartotojui atveju galėtumėte turėti prietaisų skydelį, kuriame būtų rodomas kiekvieno agento statusas, vartotojo pageidavimai ir apribojimai bei agentų sąveikos. Šis prietaisų skydelis galėtų rodyti vartotojo kelionės datas, skrydžius, kuriuos rekomendavo skrydžių agentas, viešbučius, kuriuos rekomendavo viešbučių agentas, ir automobilius, kuriuos rekomendavo automobilių nuomos agentas. Tai suteiktų aiškų vaizdą, kaip agentai sąveikauja tarpusavyje ir ar vartotojo pageidavimai bei apribojimai yra įgyvendinami.

Pažvelkime į kiekvieną iš šių aspektų išsamiau.

- **Registravimo ir stebėjimo įrankiai**: Norite registruoti kiekvieną agento atliktą veiksmą. Registracijos įrašas galėtų saugoti informaciją apie agentą, kuris atliko veiksmą, veiksmą, laiką, kada veiksmas buvo atliktas, ir veiksmo rezultatą. Ši informacija gali būti naudojama derinimui, optimizavimui ir kt.
- **Vizualizacijos įrankiai**: Vizualizacijos įrankiai gali padėti matyti agentų sąveikas intuityvesniu būdu. Pavyzdžiui, galėtumėte turėti grafiką, kuris rodo informacijos srautą tarp agentų. Tai galėtų padėti identifikuoti kliūtis, neefektyvumą ir kitas sistemos problemas.
- **Našumo metrikos**: Našumo metrikos gali padėti stebėti daugiaveiksnių sistemų efektyvumą. Pavyzdžiui, galėtumėte stebėti užduoties atlikimo laiką, užduočių skaičių per laiko vienetą ir agentų rekomendacijų tikslumą. Ši informacija gali padėti identifikuoti tobulinimo sritis ir optimizuoti sistemą.

## Daugiaveiksnių sistemų šablonai

Pažvelkime į keletą konkrečių šablonų, kuriuos galime naudoti kuriant daugiaveiksnių programas. Štai keletas įdomių šablonų, kuriuos verta apsvarstyti:

### Grupinis pokalbis

Šis šablonas naudingas, kai norite sukurti grupinio pokalbio programą, kurioje keli agentai gali komunikuoti tarpusavyje. Tipiniai šio šablono naudojimo atvejai apima komandinį bendradarbiavimą, klientų aptarnavimą ir socialinius tinklus.

Šiame šablone kiekvienas agentas atstovauja vartotoją grupiniame pokalbyje, o žinutės keičiasi tarp agentų naudojant žinučių protokolą. Agentai gali siųsti žinutes į grupinį pokalbį, gauti žinutes iš grupinio pokalbio ir atsakyti į kitų agentų žinutes.

Šis šablonas gali būti įgyvendintas naudojant centralizuotą architektūrą, kur visos žinutės nukreipiamos per centrinį serverį, arba decentralizuotą architektūrą, kur žinutės keičiasi tiesiogiai.

![Grupinis pokalbis](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.lt.png)

### Perdavimas

Šis šablonas naudingas, kai norite sukurti programą, kurioje keli agentai gali perduoti užduotis vienas kitam.

Tipiniai šio šablono naudojimo atvejai apima klientų aptarnavimą, užduočių valdymą ir darbo srautų automatizavimą.

Šiame šablone kiekvienas agentas atstovauja užduotį arba žingsnį darbo sraute, o agentai gali perduoti užduotis kitiems agentams pagal iš anksto nustatytas taisykles.

![Perdavimas](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.lt.png)

### Bendradarbiavimo filtravimas

Šis šablonas naudingas, kai norite sukurti programą, kurioje keli agentai gali bendradarbiauti, kad pateiktų rekomendacijas vartotojams.

Kodėl verta, kad keli agentai bendradarbiautų? Todėl, kad kiekvienas agentas gali turėti skirtingą ekspertizę ir prisidėti prie rekomendacijų proceso skirtingais būdais.

Pavyzdžiui, vartotojas nori rekomendacijos dėl geriausios akcijos, kurią galima įsigyti akcijų rinkoje.

- **Pramonės ekspertas**: Vienas agentas galėtų būti pramonės ekspertas.
- **Techninė analizė**: Kitas agentas galėtų būti techninės analizės ekspertas.
- **Fundamentinė analizė**: Ir dar vienas agentas galėtų būti fundamentinės analizės ekspertas. Bendradarbiaudami šie agentai galėtų pateikti vartotojui išsamesnę rekomendaciją.

![Rekomendacija](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.lt.png)

## Scenarijus: Grąžinimo procesas

Apsvarstykime scenarijų, kai klientas bando gauti grąžinimą už produktą. Šiame procese gali dalyvauti nemažai agentų, tačiau suskirstykime juos į agentus, specifinius šiam procesui, ir bendruosius agentus, kurie gali būti naudojami kituose procesuose.

**Agentai, specifiniai grąžinimo procesui**:

Štai keletas agentų, kurie galėtų dalyvauti grąžinimo procese:

- **Kliento agentas**: Šis agentas atstovauja klientą ir yra atsakingas už grąžinimo proceso inicijavimą.
- **Pardavėjo agentas**: Šis agentas atstovauja pardavėją ir yra atsakingas už grąžinimo apdorojimą.
- **Mokėjimo agentas**: Šis agentas atstovauja mokėjimo procesą ir yra atsakingas už kliento mokėjimo grąžinimą.
- **Sprendimo agentas**: Šis agentas atstovauja sprendimo procesą ir yra atsakingas už bet kokių problemų, kylančių grąžinimo proceso metu, sprendimą.
- **Atitikties agentas**: Šis agentas atstovauja atitikties procesą ir yra atsakingas už tai, kad grąžinimo procesas atitiktų reglamentus ir politiką.

**Bendrieji agentai**:

Šie agentai gali būti naudojami kitose jūsų verslo dalyse.

- **Siuntimo agentas**: Šis agentas atstovauja siuntimo procesą ir yra atsakingas už produkto siuntimą atgal pardavėjui. Šis agentas gali būti naudojamas tiek grąžinimo procese, tiek bendrame produkto siuntime, pavyzdžiui, pirkimo metu.
- **Atsiliepimų agentas**: Šis agentas atstovauja atsiliepimų procesą ir yra atsakingas už klientų atsiliepimų rinkimą. Atsiliepimai gali būti renkami bet kuriuo metu, ne tik grąžinimo proceso metu.
- **Eskalavimo agentas**: Šis agentas atstovauja eskalavimo procesą ir yra atsakingas už problemų eskalavimą į aukštesnį palaikymo lygį. Šio tipo agentą galima naudoti bet kuriame procese, kuriame reikia eskaluoti problemą.
- **Pranešimų agentas**: Šis agentas atstovauja pranešimų procesą ir yra atsakingas už pranešimų siuntimą klientui įvairiais grąžinimo proceso etapais.
- **Analizės agentas**: Šis agentas atstovauja analizės procesą ir yra atsakingas už duomenų, susijusių su grąžinimo procesu, analizę.
- **Audito agentas**: Šis agentas atstovauja audito procesą ir
## Sprendimas

Sukurkite daugiaveikį sistemą klientų aptarnavimo procesui. Nustatykite procese dalyvaujančius agentus, jų vaidmenis ir atsakomybes bei kaip jie sąveikauja tarpusavyje. Apsvarstykite tiek agentus, skirtus konkrečiai klientų aptarnavimo procesui, tiek bendruosius agentus, kurie gali būti naudojami kitose jūsų verslo srityse.

> Pagalvokite prieš skaitydami pateiktą sprendimą, jums gali prireikti daugiau agentų, nei manote.

> PATARIMAS: Pagalvokite apie skirtingus klientų aptarnavimo proceso etapus ir taip pat apsvarstykite agentus, reikalingus bet kuriai sistemai.

## Sprendimas

[Sprendimas](./solution/solution.md)

## Žinių patikrinimas

Klausimas: Kada reikėtų apsvarstyti daugiaveikių agentų naudojimą?

- [ ] A1: Kai turite mažą darbo krūvį ir paprastą užduotį.
- [ ] A2: Kai turite didelį darbo krūvį.
- [ ] A3: Kai turite paprastą užduotį.

[Sprendimo testas](./solution/solution-quiz.md)

## Santrauka

Šioje pamokoje aptarėme daugiaveikių agentų dizaino modelį, įskaitant scenarijus, kuriuose daugiaveikiai agentai yra tinkami, daugiaveikių agentų pranašumus prieš vieną agentą, pagrindinius daugiaveikių agentų dizaino modelio įgyvendinimo elementus ir kaip stebėti, kaip keli agentai sąveikauja tarpusavyje.

### Turite daugiau klausimų apie daugiaveikių agentų dizaino modelį?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiaisiais, dalyvautumėte konsultacijų valandose ir gautumėte atsakymus į savo klausimus apie AI agentus.

## Papildomi ištekliai

- 

## Ankstesnė pamoka

[Planavimo dizainas](../07-planning-design/README.md)

## Kita pamoka

[Metakognicija AI agentuose](../09-metacognition/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.