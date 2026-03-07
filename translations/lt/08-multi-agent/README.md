[![Daugiagentės dizaino šablonai](../../../translated_images/lt/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Spustelėkite aukščiau esantį paveikslėlį, norėdami peržiūrėti šios pamokos vaizdo įrašą)_

# Daugiagentės dizaino šablonai

Kai tik pradedate dirbti su projektu, kuriame dalyvauja keli agentai, turėsite apsvarstyti daugiagentės dizaino šabloną. Tačiau gali būti ne iš karto aišku, kada pereiti prie daugiagentės sistemos ir kokie yra jos pranašumai.

## Įvadas

Šioje pamokoje siekiame atsakyti į šiuos klausimus:

- Kokios situacijos tinka daugiagentėms sistemoms?
- Kokie pranašumai naudojant daugiagentę sistemą, palyginti su vienu agentu, kuris atlieka kelias užduotis?
- Kokie yra daugiagentės dizaino šablono įgyvendinimo blokai?
- Kaip mes galime matyti, kaip tarpusavyje sąveikauja keli agentai?

## Mokymosi tikslai

Po šios pamokos turėtumėte gebėti:

- Nustatyti situacijas, kuriose tinka naudoti daugiagentę sistemą
- Suprasti daugiagentės sistemos pranašumus, palyginti su vienu agentu
- Suprasti daugiagentės dizaino šablono įgyvendinimo blokų esmę

Koks didesnis vaizdas?

*Daugiagentės sistemos yra dizaino šablonas, leidžiantis keliems agentams dirbti kartu siekiant bendro tikslo.*

Šis šablonas plačiai naudojamas įvairiose srityse, įskaitant robotiką, autonomines sistemas ir paskirstytą kompiuteriją.

## Situacijos, kuriose tinka naudoti daugiagentę sistemą

Kokios situacijos yra tinkamos naudoti daugiagentę sistemą? Atsakymas yra, kad daugelyje situacijų naudinga naudoti kelis agentus, ypač šiais atvejais:

- **Didelės darbo apimtys**: Dideles darbo apimtis galima suskaidyti į mažesnes užduotis ir paskirstyti skirtingiems agentams, leidžiant lygiagrečiai apdoroti ir greičiau baigti. Pavyzdys — didelės duomenų apdorojimo užduoties atvejis.
- **Sudėtingos užduotys**: Sudėtingas užduotis, kaip ir dideles darbo apimtis, galima suskaidyti į mažesnes dalines užduotis ir paskirti skirtingiems agentams, kurių kiekvienas specializuojasi konkrečioje užduoties dalyje. Pavyzdys — autonominių transporto priemonių atvejis, kur skirtingi agentai valdo navigaciją, kliūčių aptikimą ir bendravimą su kitais automobiliais.
- **Įvairiapusė ekspertizė**: Skirtingi agentai gali turėti įvairiapusę ekspertizę, leidžiančią jiems veiksmingiau spręsti skirtingas užduoties dalis nei vienam agentui. Pavyzdys čia būtų sveikatos priežiūra, kur agentai gali dirbti su diagnostika, gydymo planais ir paciento stebėjimu.

## Privalumai naudojant daugiagentę sistemą, palyginti su vienu agentu

Vieno agento sistema galėtų tinkamai veikti paprastoms užduotims, tačiau sudėtingesnėms užduotims naudojant kelis agentus galima pasiekti kelis privalumus:

- **Specializacija**: Kiekvienas agentas gali būti specializuotas konkrečiai užduočiai. Vieno agento trūkumas yra tas, kad agentas, bandantis viską atlikti, gali sutrikti susidūręs su sudėtinga užduotimi. Jis gali, pavyzdžiui, imtis užduoties, kuriai jis nėra geriausiai pritaikytas.
- **Mastelio keitimas**: Lengviau plečiama sistema pridedant daugiau agentų, nei apkraunant vieną agentą per daug.
- **Atsparumas gedimams**: Jei vienas agentas sugenda, kiti gali tęsti darbą, užtikrinant sistemos patikimumą.

Pažiūrėkime pavyzdį — užsisakykime kelionę vartotojui. Vieno agento sistema turėtų rūpintis visais kelionės užsakymo aspektais — nuo skrydžių paieškos iki viešbučių ir automobilių nuomos užsakymo. Norint tai įgyvendinti su vienu agentu, jis turėtų turėti įrankius visoms šiems užduotims atlikti. Tai gali sukurti sudėtingą ir sunkiai prižiūrimą, monolitinę sistemą. Tuo tarpu daugiagentė sistema galėtų turėti skirtingus agentus, specializuotus skrydžių paieškai, viešbučių ir automobilių nuomos užsakymui. Tai padarytų sistemą modularią, lengviau prižiūrimą ir išplečiamą.

Palyginkime tai su kelionių agentūra, kuri veikia kaip mažas šeimos verslas, ir kelionių agentūra-franšizė. Mažas šeimos verslas turėtų vieną agentą, kuris rūpinasi visais kelionės užsakymo aspektais, o franšizė turėtų skirtingus agentus, kurie atlieka skirtingas užduotis.

## Daugiagentės dizaino šablono įgyvendinimo blokai

Prieš pradėdami įgyvendinti daugiagentės dizaino šabloną, turite suprasti jo sudedamąsias dalis.

Padarykime tai konkretesnį, vėl pasižiūrėdami į vartotojo kelionės užsakymo pavyzdį. Šiuo atveju įgyvendinimo blokai būtų:

- **Agentų komunikacija**: Agentai, atsakingi už skrydžių paiešką, viešbučių ir automobilių nuomą, turi bendrauti ir dalintis informacija apie vartotojo pageidavimus ir apribojimus. Turite nuspręsti, kokie bus šios komunikacijos protokolai ir metodai. Konkrečiai tai reiškia, kad skrydžių agentas turi bendrauti su viešbučių agentu, kad viešbutis būtų užsakytas tomis pačiomis datomis kaip ir skrydis. Tai reiškia, kad agentai turi dalintis informacija apie vartotojo kelionės datas, ir jums reikia nuspręsti, *kuriuos agentus ir kaip jie dalinsis informacija*.
- **Koordinavimo mechanizmai**: Agentai turi koordinuoti savo veiksmus, kad atitiktų vartotojo pageidavimus ir apribojimus. Pavyzdžiui, vartotojas gali norėti viešbučio šalia oro uosto, o apribojimas gali būti toks, kad automobilių nuoma yra tik oro uoste. Tai reiškia, kad viešbučių agentas turi koordinuotis su automobilių nuomos agentu, kad vartotojo pageidavimai ir apribojimai būtų įgyvendinti. Jūs turite nuspręsti, *kaip agentai koordinuoja savo veiksmus*.
- **Agentų architektūra**: Agentai turi turėti vidinę struktūrą, leidžiančią priimti sprendimus ir mokytis iš sąveikos su vartotoju. Tai reiškia, kad skrydžių agentas turi turėti vidinę struktūrą sprendimams, kokius skrydžius pasiūlyti vartotojui. Jūs turite nuspręsti, *kaip agentai priima sprendimus ir mokosi iš sąveikos su vartotoju*. Pavyzdžiui, skrydžių agentas gali naudoti mašininio mokymosi modelį, kad remdamasis praeities vartotojo pageidavimais rekomenduotų skrydžius.
- **Matomumas apie daugiagentę sąveiką**: Turite turėti galimybę matyti, kaip keli agentai sąveikauja tarpusavyje. Tam reikia turėti įrankius ir technikas agentų veiklos ir sąveikų stebėjimui — pavyzdžiui, registravimo, stebėjimo įrankius, vizualizacijas ir našumo metrikas.
- **Daugiagentės sistemos šablonai**: Yra įvairūs šablonai daugiagentėms sistemoms įgyvendinti, tokie kaip centralizuotos, decentralizuotos ir hibridinės architektūros. Turite pasirinkti, kuris šablonas geriausiai tinka jūsų atvejui.
- **Žmogus grandinėje**: Dažnai bus žmogus, dalyvaujantis procese, ir reikia nustatyti, kada agentai turi prašyti žmogaus įsikišimo. Tai gali būti, pavyzdžiui, kai vartotojas prašo konkretaus viešbučio ar skrydžio, kurio agentai nesiūlė, arba kai reikia patvirtinimo prieš užsakant skrydį ar viešbutį.

## Matomumas apie daugiagentę sąveiką

Svarbu turėti galimybę matyti, kaip keli agentai sąveikauja tarpusavyje. Šis matomumas yra būtinas trikčių šalinimui, optimizavimui ir bendro sistemos efektyvumo užtikrinimui. Norint tai pasiekti, reikia turėti įrankius ir technikas agentų veiklos ir sąveikos sekimui. Tai gali būti registravimo, stebėjimo įrankiai, vizualizacijos ir našumo metrikos.

Pavyzdžiui, vartotojo kelionės užsakymo atveju galėtumėte turėti informacinę skydelį, rodantį kiekvieno agente būseną, vartotojo pageidavimus ir apribojimus, bei agentų sąveiką. Šis skydelis galėtų rodyti vartotojo kelionės datas, skrydžių, kuriuos rekomenduoja skrydžių agentas, viešbučius, kuriuos siūlo viešbučių agentas, ir automobilių nuomą, kurią rekomenduoja automobilių nuomos agentas. Tai suteiktų aiškų vaizdą, kaip agentai sąveikauja ir ar vartotojo pageidavimai bei apribojimai yra tenkinami.

Aptarkime kiekvieną iš šių aspektų detaliau.

- **Registravimo ir stebėjimo įrankiai**: Norite užfiksuoti kiekvieną agento atliktą veiksmą. Registracijos įrašas gali saugoti informaciją apie agentą, kuris atliko veiksmą, veiksmą, jo atlikimo laiką ir rezultatą. Ši informacija gali būti naudojama trikčių šalinimui, optimizavimui ir pan.
- **Vizualizacijos įrankiai**: Jie leidžia matyti agentų sąveiką intuityvesniu būdu. Pavyzdžiui, galėtumėte turėti grafą, rodantį informacijos srautą tarp agentų. Tai padeda identifikuoti perkrovos taškus, neefektyvumą ir kitas problemas.
- **Našumo metrikos**: Padeda sekti daugiagentės sistemos efektyvumą. Pavyzdžiui, galite stebėti užduoties atlikimo laiką, vienetui laiko atliktų užduočių skaičių ir agentų rekomendacijų tikslumą. Ši informacija leidžia nustatyti tobulinimo sritis ir optimizuoti sistemą.

## Daugiagentės sistemos šablonai

Pažvelkime į konkretų šablonų rinkinį, kuriuos galima naudoti kuriant daugiagentines programas. Štai keli įdomūs šablonai, kuriuos verta apsvarstyti:

### Grupinis pokalbis

Šis šablonas naudingas, kai siekiate sukurti grupinio pokalbio programą, kur keli agentai gali bendrauti tarpusavyje. Tipinės panaudojimo sritys: komandinis bendradarbiavimas, klientų aptarnavimas, socialiniai tinklai.

Šiame šablone kiekvienas agentas atstovauja vartotoją grupiniame pokalbyje, o žinutės keičiasi tarp agentų naudojant susirašinėjimo protokolą. Agentai gali siųsti žinutes į grupę, gauti žinutes iš grupės ir atsakyti į kitų agentų žinutes.

Šis šablonas gali būti įgyvendinamas naudojant centralizuotą architektūrą, kur visos žinutės keliauja per centrinį serverį, arba decentralizuotą, kur žinutės keičiasi tiesiogiai.

![Grupinis pokalbis](../../../translated_images/lt/multi-agent-group-chat.ec10f4cde556babd.webp)

### Perdavimas (Hand-off)

Šis šablonas naudingas, kai norite sukurti programą, kurioje keli agentai gali perduoti vienas kitam užduotis.

Tipinės panaudojimo sritys: klientų aptarnavimas, užduočių valdymas, darbo eigos automatizavimas.

Šiame šablone kiekvienas agentas reprezentuoja užduotį arba žingsnį darbo eigoje, o agentai perduoda užduotis vienas kitam pagal iš anksto nustatytas taisykles.

![Perdavimas](../../../translated_images/lt/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Bendradarbiaujantis filtravimas

Šis šablonas naudingas, kai norite sukurti programą, kurioje keli agentai bendradarbiauja, kad pateiktų rekomendacijas vartotojams.

Kodėl verta, kad agentai bendradarbiautų? Nes kiekvienas agentas gali turėti skirtingą ekspertizę ir skirtingai prisidėti prie rekomendacijų teikimo proceso.

Paimkime pavyzdį, kai vartotojas nori rekomendacijos, kokias geriausias akcijas įsigyti.

- **Pramonės ekspertas**: Vienas agentas gali būti pramonės srities ekspertas.
- **Techninė analizė**: Kitas agentas gali būti techninės analizės ekspertas.
- **Fundamentali analizė**: Trečias agentas gali būti fundamentali analizės ekspertas. Bendradarbiaudami šie agentai gali pateikti vartotojui išsamesnę rekomendaciją.

![Rekomendacijos](../../../translated_images/lt/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenarijus: pinigų grąžinimo procesas

Aptarkime scenarijų, kai klientas bando gauti pinigų grąžinimą už produktą. Šiame procese gali būti daug agentų, bet suskirstykime juos į konkrečius šiam procesui skirtus agentus ir bendrus agentus, kurie gali būti naudojami ir kituose procesuose.

**Agentai, skirti pinigų grąžinimo procesui**:

Šie agentai gali dalyvauti pinigų grąžinimo procese:

- **Kliento agentas**: Atstovauja klientui ir atsakingas už pinigų grąžinimo proceso pradžią.
- **Pardavėjo agentas**: Atstovauja pardavėjui ir atsakingas už grąžinimo apdorojimą.
- **Mokėjimo agentas**: Atsakingas už vartotojo mokėjimo grąžinimą.
- **Išsprendimo agentas**: Atsakingas už problemų sprendimą, kilusių per grąžinimo procesą.
- **Atitikties agentas**: Užtikrina, kad grąžinimo procesas atitiktų taisykles ir politikas.

**Bendri agentai**:

Šie agentai gali būti naudojami kitose jūsų verslo srityse.

- **Siuntimo agentas**: Atsakingas už prekės siuntimą atgal pardavėjui. Gali būti naudojamas tiek grąžinimo procese, tiek bendram produktų siuntimui pavyzdžiui per pirkimą.
- **Atsiliepimų agentas**: Rinkti atsiliepimus iš kliento. Atsiliepimus galima gauti bet kuriuo metu, ne tik grąžinimo proceso metu.
- **Eskalavimo agentas**: Atsakingas už problemų eskalavimą aukštesnio lygio palaikymui. Galima naudoti bet kuriame procese, kur reikia eskaluoti problemą.
- **Pranešimų agentas**: Atsakingas už klientų informavimą įvairiuose grąžinimo proceso etapuose.
- **Analitikos agentas**: Analizuoja duomenis, susijusius su grąžinimo procesu.
- **Auditavimo agentas**: Atlieka grąžinimo proceso auditą, kad įsitikintų, jog jis vykdomas teisingai.
- **Ataskaitų agentas**: Rengia ataskaitas apie grąžinimo procesą.
- **Žinių agentas**: Palaiko žinių bazę apie grąžinimo procesą ir kitas verslo sritis.
- **Saugumo agentas**: Užtikrina grąžinimo proceso saugumą.
- **Kokybės agentas**: Užtikrina grąžinimo proceso kokybę.

Išvardinti agentai apima tiek specifinius grąžinimo proceso agentus, tiek bendruosius agentus, naudojamus kituose verslo segmentuose. Tikimės, jog tai suteikia jums supratimą, kaip spręsti klausimą, kokius agentus naudoti daugiagentėje sistemoje.

## Užduotis

Sukurkite daugiagentę sistemą klientų aptarnavimo procesui. Nustatykite procese dalyvaujančius agentus, jų roles ir atsakomybes bei kaip jie sąveikauja tarpusavyje. Apsvarstykite tiek klientų aptarnavimo procesui specifinius agentus, tiek bendruosius agentus, kurie gali būti naudojami kitose jūsų verslo srityse.
> Pagalvokite prieš skaitydami toliau pateiktą sprendimą, gali prireikti daugiau agentų nei manote.

> PATARIMAS: Apsvarstykite skirtingus klientų aptarnavimo proceso etapus ir taip pat pamąstykite apie agentus, reikalingus bet kuriai sistemai.

## Sprendimas

[Sprendimas](./solution/solution.md)

## Žinių patikrinimai

Klausimas: Kada reikėtų svarstyti apie daugelio agentų naudojimą?

- [ ] A1: Kai turite mažą darbo krūvį ir paprastą užduotį.
- [ ] A2: Kai turite didelį darbo krūvį
- [ ] A3: Kai turite paprastą užduotį.

[Sprendimo testas](./solution/solution-quiz.md)

## Santrauka

Šiame pamokoje aptarėme daugelio agentų dizaino šabloną, įskaitant atvejus, kai tinkama naudoti kelis agentus, privalumus, palyginti su vienu agentu, daugelio agentų dizaino šablono įgyvendinimo pagrindinius elementus ir kaip stebėti, kaip keli agentai sąveikauja tarpusavyje.

### Turite daugiau klausimų apie daugelio agentų dizaino šabloną?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kur galite susitikti su kitais besimokančiais, dalyvauti konsultacijose ir gauti atsakymus į savo klausimus apie dirbtinio intelekto agentus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft agentų sistemos dokumentacija</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentų dizaino šablonai</a>


## Ankstesnė pamoka

[Planavimo dizainas](../07-planning-design/README.md)

## Kitoji pamoka

[Metakognicija dirbtinio intelekto agentuose](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Autentišku ir tiksliausiu šaltiniu laikomas originalus dokumentas jo gimtąja kalba. Kritinės informacijos atveju rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingą interpretavimą, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->