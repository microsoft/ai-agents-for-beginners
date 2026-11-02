[![Daugelio agentų dizainas](../../../translated_images/lt/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Spustelėkite aukščiau esantį paveikslėlį norėdami peržiūrėti šio pamokos vaizdo įrašą)_

# Daugelio agentų dizaino šablonai

Kai tik pradėsite dirbti su projektu, kuriame dalyvauja keli agentai, reikės apsvarstyti daugiaagentinį dizaino modelį. Tačiau iš karto gali būti neaišku, kada pereiti prie daugelio agentų ir kokie yra privalumai.

## Įvadas

Šioje pamokoje mes siekiame atsakyti į šiuos klausimus:

- Kokios situacijos yra tinkamos naudoti daugelio agentų sistemą?
- Kokie yra daugelio agentų naudojimo pranašumai, palyginti su vienu agentu, atliekant kelių užduočių vykdymą?
- Kokios yra pagrindinės daugelio agentų dizaino modelio realizavimo sudedamosios dalys?
- Kaip galime turėti matomumą, kaip keli agentai sąveikauja tarpusavyje?

## Mokymosi tikslai

Po šios pamokos turėtumėte sugebėti:

- Nustatyti situacijas, kuriose tinka naudoti daugelio agentų sistemą
- Pripažinti daugelio agentų naudojimo pranašumus, palyginti su vienu agentu.
- Suprasti daugelio agentų dizaino modelio realizavimo sudedamąsias dalis.

Kokia yra platesnė prasmė?

*Daugelio agentų modelis yra dizaino šablonas, leidžiantis keliems agentams dirbti kartu siekiant bendro tikslo*.

Šis modelis plačiai naudojamas įvairiose srityse, įskaitant robotiką, autonomines sistemas ir paskirstytą skaičiavimą.

## Situacijos, kuriose tinka naudoti daugelio agentų sistemas

Kokios situacijos yra geras daugelio agentų naudojimo pavyzdys? Atsakymas yra toks, kad yra daug situacijų, kuriomis naudinga naudoti kelis agentus, ypač šiais atvejais:

- **Didelės apimties darbai**: Dideles užduotis galima suskaidyti į mažesnes ir paskirti skirtingiems agentams, leidžiant atlikti veiksmus lygiagrečiai ir greičiau užbaigti. Pavyzdys būtų didelis duomenų apdorojimo uždavinys.
- **Sudėtingos užduotys**: Sudėtingas užduotis, kaip ir didelės apimties darbus, galima skaidyti į mažesnes užduočių dalis ir paskirti skirtingiems agentams, kurių kiekvienas specializuojasi konkrečioje užduoties dalyje. Geras pavyzdys yra autonominiai automobiliai, kur skirtingi agentai valdo navigaciją, kliūčių aptikimą ir komunikaciją su kitais automobiliais.
- **Įvairi ekspertizė**: Skirtingi agentai gali turėti skirtingų žinių, leidžiančių jiems efektyviau tvarkyti skirtingus užduoties aspektus nei vienas agentas. Šiuo atveju geras pavyzdys yra sveikatos priežiūra, kur agentai gali valdyti diagnostiką, gydymo planus ir pacientų stebėseną.

## Daugelio agentų naudojimo pranašumai prieš vieną agentą

Vieno agente sistemos gali tinkamai veikti paprastoms užduotims, tačiau sudėtingesnėms užduotims daugelio agentų naudojimas suteikia keletą pranašumų:

- **Specializacija**: Kiekvienas agentas gali būti specializuotas konkrečiai užduočiai. Vieno agento nespecializavimas reiškia, kad agentas bando atlikti viską, bet gali susipainioti sudėtingos užduoties metu. Jis gali, pavyzdžiui, atlikti užduotį, kuriai nėra geriausiai pritaikytas.
- **Išplečiamumas**: Sistemą lengviau išplėsti tiesiog pridėjus daugiau agentų, o ne apkraunant vieną agentą.
- **Atsparumas klaidoms**: Jei vienas agentas sugestų, kiti gali tęsti darbą, užtikrindami sistemos patikimumą.

Paimkime pavyzdį - užsakyti kelionę vartotojui. Vieno agento sistema turėtų tvarkyti visas kelionės užsakymo dalis – nuo skrydžių paieškos iki viešbučių ir automobilių nuomos užsakymo. Tai reikštų, kad agentas turėtų turėti įrankius visoms šioms užduotims atlikti. Tai gali sukurti sudėtingą, monolitinę sistemą, kurią sunku prižiūrėti ir plečiant. Daugelio agentų sistema galėtų turėti skirtingus agentus, specializuotus skrydžių ieškojimo, viešbučių ir automobilių nuomos užsakymų srityse. Tai padarytų sistemą moduline, lengviau prižiūrimą ir plečiamą.

Palyginkite tai su kelionių biuru, veikiančiu kaip mažas šeimos verslas, ir kelionių biuru kaip franšizės. Mažas šeimos verslas turėtų vieną agentą, kuris tvarko visus kelionės užsakymo aspektus, o franšizėje skirtingi agentai tvarko skirtingas užsakymo dalis.

## Daugelio agentų dizaino modelio realizavimo sudedamosios dalys

Prieš pradėdami realizuoti daugelio agentų dizaino modelį, turite suprasti jo sudedamąsias dalis.

Pavyzdžiui, vėl pažiūrėkime į kelionės užsakymo vartotojui pavyzdį. Šiuo atveju sudedamosios dalys būtų:

- **Agentų komunikacija**: Agentai, ieškantys skrydžių, užsakantys viešbučius ir automobilių nuomą, turi tarpusavyje bendrauti ir dalytis informacija apie vartotojo pageidavimus ir apribojimus. Reikia nuspręsti, kokias protokolus ir metodus naudoti komunikacijai. Tai konkrečiai reiškia, kad skrydžių ieškojimo agentas turi bendrauti su viešbučių užsakymo agentu, kad viešbutis būtų užsakytas tuo pačiu laikotarpiu kaip ir skrydis. Tai reiškia, kad agentai turi dalytis informacija apie vartotojo kelionės datas, o jūs turite nuspręsti, *kokie agentai dalijasi informacija ir kaip tai vyksta*.
- **Koordinacijos mechanizmai**: Agentai turi suderinti savo veiksmus, kad būtų patenkinti vartotojo pageidavimai ir apribojimai. Pavyzdžiui, vartotojas gali norėti viešbučio netoli oro uosto, o apribojimas gali būti, kad automobilių nuoma prieinama tik oro uoste. Tai reiškia, kad viešbučių užsakymo agentas turi derinti veiksmus su automobilių nuomos agentu, kad būtų įgyvendinti vartotojo pageidavimai ir apribojimai. Reikia nuspręsti, *kaip agentai koordinuoja savo veiksmus*.
- **Agentų architektūra**: Agentai turi turėti vidinę struktūrą, leidžiančią priimti sprendimus ir mokytis iš sąveikos su vartotoju. Tai reiškia, kad skrydžių ieškojimo agentas turi turėti vidinę struktūrą sprendimų priėmimui apie rekomenduojamus skrydžius vartotojui. Reikia nuspręsti, *kaip agentai priima sprendimus ir mokosi iš sąveikos su vartotoju*. Pavyzdžiui, skrydžių ieškojimo agentas galėtų naudoti mašininio mokymosi modelį, kad rekomenduotų skrydžius pagal vartotojo ankstesnius pageidavimus.
- **Matomumas daugiaagentinėje sąveikoje**: Turite matyti, kaip keli agentai sąveikauja tarpusavyje. Tam reikia turėti įrankius ir metodikas agentų veiksmų ir sąveikos sekimui. Tai gali būti žurnalai ir stebėjimo įrankiai, vizualizacijos priemonės ir našumo metrikos.
- **Daugelio agentų šablonai**: Yra skirtingi daugelio agentų sistemų kūrimo šablonai, tokie kaip centralizuota, decentralizuota ir mišri architektūros. Reikia pasirinkti tinkamiausią jūsų naudojimo atvejui.
- **Žmogus grandinėje**: Daugeliu atvejų yra žmogus grandinėje, ir reikia nurodyti agentams, kada prašyti žmogaus įsikišimo. Tai gali būti vartotojo užklausa dėl konkretaus viešbučio ar skrydžio, kurio agentai nerekomendavo, arba patvirtinimo prašymas prieš užsakant skrydį ar viešbutį.

## Matomumas daugiaagentinėje sąveikoje

Svarbu turėti matomumą, kaip keli agentai sąveikauja tarpusavyje. Šis matomumas yra būtinas klaidų taisymui, optimizavimui ir bendram sistemos efektyvumui užtikrinti. Norint sukurti tokį matomumą, reikia naudoti įrankius ir metodikas agentų veiksmams ir sąveikai stebėti. Tai gali apimti žurnalų įrašymo ir stebėjimo įrankius, vizualizavimo įrankius bei našumo rodiklius.

Pavyzdžiui, užsakant kelionę vartotojui, galėtumėte turėti informacijos suvestinę, rodytų kiekvieno agente būseną, vartotojo pageidavimus ir apribojimus bei agentų sąveiką. Ši suvestinė galėtų rodyti vartotojo kelionės datas, skrydžių rekomendacijas iš skrydžių agento, viešbučius iš viešbučių agento ir automobilių nuomą iš atitinkamo agento. Tai suteiktų aiškų vaizdą, kaip agentai bendrauja ir ar vartotojo pageidavimai bei apribojimai yra įgyvendinami.

Pažvelkime į kiekvieną iš šių aspektų detaliau.

- **Žurnalo įrašymo ir stebėjimo įrankiai**: Norite užfiksuoti kiekvieną agento atliekamą veiksmą. Žurnalo įrašas gali saugoti informaciją apie agentą, kuris atliko veiksmą, veiksmą, laiką, kada veiksmas buvo atliktas, ir jo rezultatą. Šią informaciją galima naudoti klaidų taisymui, optimizavimui ir kitais tikslais.

- **Vizualizacijos įrankiai**: Vizualizacijos įrankiai gali padėti kur kas intuityviau matyti agentų sąveikas. Pavyzdžiui, galite turėti grafiką, rodančią informacijos srautą tarp agentų. Tai gali padėti nustatyti sistemos „kamuoliukus“, neefektyvumą ir kitas problemas.

- **Našumo rodikliai**: Našumo rodikliai leidžia stebėti daugelio agentų sistemos efektyvumą. Pavyzdžiui, galite sekti užduoties įvykdymo laiką, užduočių skaičių per vienetą laiko ir agentų pateiktų rekomendacijų tikslumą. Tai padeda nustatyti tobulinimo sritis ir optimizuoti sistemą.

## Daugelio agentų šablonai

Pažvelkime į konkrečius šablonus, kuriuos galime naudoti kuriant daugelio agentų programas. Štai keli įdomūs modeliai, kuriuos verta apsvarstyti:

### Grupės pokalbis

Šis modelis naudingas, kai norite sukurti grupės pokalbių programą, kurioje keli agentai gali bendrauti tarpusavyje. Tipiniai šio modelio panaudojimo atvejai apima komandų bendradarbiavimą, klientų aptarnavimą ir socialinius tinklus.

Šiame modelyje kiekvienas agentas atstovauja grupės pokalbio vartotoją, o žinutės keičiasi tarp agentų naudojant pranešimų protokolą. Agentai gali siųsti žinutes į grupės pokalbį, gauti žinutes iš jo ir reaguoti į kitų agentų žinutes.

Šį modelį galima įgyvendinti naudojant centralizuotą architektūrą, kai visos žinutės nukreipiamos per centrinį serverį, arba decentralizuotą architektūrą, kai žinutės keičiasi tiesiogiai.

![Grupės pokalbis](../../../translated_images/lt/multi-agent-group-chat.ec10f4cde556babd.webp)

### Užduoties perdavimas (Hand-off)

Šis modelis naudingas, kai norite sukurti programą, kurioje keli agentai gali perduoti užduotis vienas kitam.

Tipiniai šio modelio panaudojimo atvejai yra klientų aptarnavimas, užduočių valdymas ir darbo srautų automatizavimas.

Šiame modelyje kiekvienas agentas atstovauja užduotį arba darbo srauto žingsnį, o agentai gali perduoti užduotis kitiems agentams pagal iš anksto nustatytas taisykles.

![Užduoties perdavimas](../../../translated_images/lt/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Bendradarbiavimas rekomendacijoms (Collaborative filtering)

Šis modelis naudingas, kai norite sukurti programą, kurioje keli agentai bendradarbiauja teikdami rekomendacijas vartotojams.

Kodėl verta keliems agentams bendradarbiauti? Nes kiekvienas agentas gali turėti skirtingų žinių ir skirtingai prisidėti prie rekomendacijų proceso.

Paimkime pavyzdį, kai vartotojas nori rekomendacijos dėl geriausios akcijos pirkti akcijų rinkoje.

- **Pramonės ekspertas**: Vienas agentas gali būti konkrečios pramonės srities ekspertas.
- **Techninė analizė**: Kitas agentas gali būti techninės analizės ekspertas.
- **Fundamentali analizė**: O dar kitas agentas gali būti fundamentali analizės ekspertas. Bendradarbiaudami šie agentai gali suteikti vartotojui platesnę ir išsamesnę rekomendaciją.

![Rekomendacijos](../../../translated_images/lt/multi-agent-filtering.d959cb129dc9f608.webp)

## Situacija: grąžinimo procesas

Apsvarstykite situaciją, kai klientas bando gauti prekių grąžinimą; šiame procese gali dalyvauti nemažai agentų, tačiau padalinkime juos į konkrečius agentus šiam procesui ir bendruosius agentus, naudojamus kitose veiklose.

**Agentai, skirti grąžinimo procesui**:

Toliau pateikti kai kurie agentai, galintys dalyvauti grąžinimo procese:

- **Kliento agentas**: Šis agentas atstovauja klientui ir yra atsakingas už grąžinimo proceso inicijavimą.
- **Pardavėjo agentas**: Šis agentas atstovauja pardavėjui ir yra atsakingas už grąžinimo tvarkymą.
- **Mokėjimo agentas**: Šis agentas atstovauja mokėjimo procesą ir yra atsakingas už kliento pinigų grąžinimą.
- **Sprendimų agentas**: Šis agentas tvarko problemų sprendimus, kilusius grąžinimo metu.
- **Atitikties agentas**: Šis agentas užtikrina, kad grąžinimo procesas atitiktų reglamentus ir politiką.

**Bendrieji agentai**:

Šie agentai gali būti naudojami ir kitose jūsų verslo srityse.

- **Siuntimo agentas**: Atsakingas už prekės grąžinimą pardavėjui. Gali būti naudojamas ir grąžinimo procese, ir bendrai prekių siuntimui, pvz., pirkimams.
- **Atsiliepimų agentas**: Rinkti klientų atsiliepimus. Atsiliepimus galima rinkti bet kuriuo metu, ne tik grąžinimo metu.
- **Eskaltacijos agentas**: Atsakingas už problemų eskalavimą aukštesniam klientų aptarnavimo lygiui. Gali būti naudojamas bet kuriame procese, kur reikia eskalacijos.
- **Pranešimų agentas**: Atsakingas už pranešimų siuntimą klientui įvairiais grąžinimo proceso etapais.
- **Analitikos agentas**: Analizuoja su grąžinimo procesu susijusius duomenis.
- **Audito agentas**: Atlieka grąžinimo proceso auditą, užtikrindamas jo teisingumą.
- **Ataskaitų agentas**: Rengia ataskaitas apie grąžinimo procesą.
- **Žinių agentas**: Palaiko žinių bazę apie grąžinimų procesą. Gali turėti žinių tiek apie grąžinimus, tiek apie kitas verslo sritis.
- **Saugumo agentas**: Užtikrina grąžinimo proceso saugumą.
- **Kokybės agentas**: Užtikrina grąžinimo proceso kokybę.

Ankstesniame sąraše yra nemažai agentų, tiek specifinių grąžinimo procesui, tiek bendrųjų, naudojamų kitose verslo srityse. Tikimės, kad tai padeda susidaryti vaizdą apie tai, kaip galite pasirinkti agentus savo daugelio agentų sistemoje.

## Užduotis

Sukurkite daugelio agentų sistemą klientų aptarnavimo procesui. Nustatykite procese dalyvaujančius agentus, jų vaidmenis ir atsakomybes bei kaip jie tarpusavyje sąveikauja. Apsvarstykite tiek agentus, specifinius klientų aptarnavimo procesui, tiek bendruosius agentus, naudojamus kitose verslo srityse.


> Pagalvokite prieš skaitydami toliau pateiktą sprendimą, jums gali prireikti daugiau agentų nei galvojate.

> PATARIMAS: Pagalvokite apie skirtingus klientų aptarnavimo proceso etapus ir taip pat apsvarstykite agentus, reikalingus bet kuriai sistemai.

## Sprendimas

[Sprendimas](./solution/solution.md)

## Žinių patikrinimai

### Klausimas 1

Kuris scenarijus geriausiai tinka daugiaagentinei sistemai?

- [ ] A1: Pagalbai skirtas botas atsako į įprastus klausimus naudodamas vieną žinių bazę ir nedidelį įrankių rinkinį.
- [ ] A2: Pinigų grąžinimo procesui reikalingos atskiros sukčiavimo, mokėjimų ir atitikties funkcijos, kiekviena su savo įrankiais, o jų rezultatai turi būti koordinuojami.
- [ ] A3: Ta pati paprasta klasifikavimo užklausa pasikartoja tūkstančius kartų per valandą.

### Klausimas 2

Kada vienas agentas paprastai yra geresnis pasirinkimas?

- [ ] A1: Užduotį galima atlikti naudojant vieną instrukcijų ir įrankių rinkinį, be specialistų perdavimo.
- [ ] A2: Agentas turi prieigą prie daugiau nei vieno įrankio.
- [ ] A3: Darbo eiga reikalauja atskirų vaidmenų su skirtingais leidimais ir nepriklausomais audito įrašais.

[Quiz sprendimas](./solution/solution-quiz.md)

## Santrauka

Šiame pamokų cikle apžvelgėme daugiaagentės architektūros šabloną, įskaitant scenarijus, kur daugiaagentinės sistemos yra tinkamos, daugiaagentinės sistemos pranašumus palyginti su vienu agentu, daugiaagentės architektūros įgyvendinimo pagrindus ir kaip stebėti agentų tarpusavio sąveiką.

### Turite daugiau klausimų apie daugiaagentės architektūros šabloną?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į klausimus apie AI agentus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentacija</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentų architektūros šablonai</a>


## Ankstesnė pamoka

[Dizaino planavimas](../07-planning-design/README.md)

## Kita pamoka

[Metakognicija AI agentuose](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->