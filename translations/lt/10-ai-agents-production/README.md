# AI Agentai gamyboje: stebimumas & vertinimas

[![AI agentai gamyboje](../../../translated_images/lt/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kai AI agentai pereina nuo eksperimentinių prototipų prie realių taikymų, svarbu sugebėti suprasti jų elgseną, stebėti jų veikimą ir sistemingai vertinti jų rezultatus.

## Mokymosi tikslai

Baigę šią pamoką, jūs sužinosite/ suprasite:
- Agentų stebimumo ir vertinimo pagrindines sąvokas
- Technikas agentų našumui, sąnaudoms ir efektyvumui gerinti
- Ką ir kaip sistemingai vertinti savo AI agentams
- Kaip valdyti sąnaudas diegiant AI agentus gamyboje
- Kaip instrumentuoti agentus, sukurtus su Microsoft Agent Framework

Tikslas yra suteikti jums žinių, kad galėtumėte paversti savo „juodosios dėžės“ agentus skaidriais, valdomais ir patikimais sistemos komponentais.

_**Pastaba:** Svarbu diegti saugius ir patikimus AI agentus. Taip pat peržiūrėkite pamoką apie [Kuriant patikimus AI agentus](./06-building-trustworthy-agents/README.md)._

## Sekos ir spanai

Stebimumo įrankiai, tokie kaip [Langfuse](https://langfuse.com/) ar [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), paprastai agentų vykdymus vaizduoja kaip sekas (traces) ir spanus (spans).

- **Trace** reiškia pilną agento užduotį nuo pradžios iki pabaigos (pvz., vartotojo užklausos apdorojimą).
- **Spans** yra atskiri žingsniai sekoje (pvz., kalbos modelio kvietimas arba duomenų gavimas).

![Sekos medis Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Be stebimumo AI agentas gali pasirodyti kaip „juodoji dėžė“ – jo vidinė būklė ir samprotavimai yra nepermatomi, todėl sunku diagnozuoti problemas ar optimizuoti veikimą. Su stebimumu agentai tampa „stiklinėmis dėžėmis“, suteikiančiomis skaidrumą, kuris yra būtinas pasitikėjimui kurti ir užtikrinti, kad jie veikia kaip numatyta.

## Kodėl stebimumas svarbus gamybinėse aplinkose

Perkėlimas AI agentų į gamybines aplinkas atneša naujų iššūkių ir reikalavimų. Stebimumas nebėra „malonu turėti“, jis tampa kritine galimybe:

*   **Triktis ir priežasties nustatymas:** Kai agentas sugenda arba pateikia netikėtą rezultatą, stebimumo įrankiai suteikia sekas, reikalingas klaidos šaltiniui nustatyti. Tai ypač svarbu sudėtinguose agentuose, kuriuose gali būti keli LLM kvietimai, įrankių sąveikos ir sąlyginė logika.
*   **Vėlavimo ir sąnaudų valdymas:** AI agentai dažnai remiasi LLM ir kitais išoriniais API, kurie apmokestinami už simbolį arba už kvietimą. Stebimumas leidžia tiksliai sekti šiuos kvietimus, padedant nustatyti operacijas, kurios yra pernelyg lėtos ar brangios. Tai leidžia komandai optimizuoti promptus, pasirinkti efektyvesnius modelius arba pertvarkyti darbo eigas siekiant valdyti veiklos sąnaudas ir užtikrinti gerą vartotojo patirtį.
*   **Pasitikėjimas, saugumas ir atitiktis:** Daugelyje taikymų svarbu užtikrinti, kad agentai elgiasi saugiai ir etiškai. Stebimumas suteikia agento veiksmų ir sprendimų auditą. Tai gali būti naudojama aptikti ir švelninti problemas, tokias kaip prompt injekcija, žalingo turinio generavimas arba asmens atpažįstamos informacijos (PII) netinkamas tvarkymas. Pavyzdžiui, galite peržiūrėti sekas, kad suprastumėte, kodėl agentas pateikė tam tikrą atsakymą arba naudojo konkretų įrankį.
*   **Nuolatinio tobulinimo ciklai:** Stebimumo duomenys yra iteracinio vystymo proceso pagrindas. Stebėdami, kaip agentai veikia realiame pasaulyje, komandos gali nustatyti tobulintinas sritis, surinkti duomenis modeliui smulkinti ir įvertinti pokyčių poveikį. Tai sukuria atsiliepimų kilpą, kurioje gamybiniai įžvalgos iš online vertinimo informuoja offline eksperimentavimą ir tobulinimą, vedantį prie nuosekliai gerėjančio agento veikimo.

## Pagrindiniai stebimi rodikliai

Norint stebėti ir suprasti agento elgseną, reikia sekti įvairius rodiklius ir signalus. Konkretūs rodikliai gali skirtis priklausomai nuo agento paskirties, tačiau kai kurie yra universaliai svarbūs.

Čia pateikti dažniausiai stebimi rodikliai:

**Vėlavimas:** Kokiu greičiu agentas atsako? Ilgas laukimas neigiamai veikia vartotojo patirtį. Turėtumėte matuoti vėlavimą užduotims ir atskiriems žingsniams, sekdami agentų vykdymą. Pavyzdžiui, agentui, kuriam visiems modelio kvietimams reikia 20 sekundžių, galima pagreitinti naudojant greitesnį modelį arba vykdant modelio kvietimus lygiagrečiai.

**Sąnaudos:** Kiek kainuoja vienas agento vykdymas? AI agentai remiasi LLM kvietimais, apmokestinamais už simbolį, arba išoriniais API. Dažnas įrankių naudojimas ar keli promptai gali greitai padidinti sąnaudas. Pavyzdžiui, jei agentas penkis kartus kviečia LLM dėl menko kokybės pagerinimo, turite įvertinti, ar sąnaudos pateisinamos, ar galima sumažinti kvietimų skaičių arba naudoti pigesnį modelį. Realaus laiko stebėjimas taip pat gali padėti aptikti netikėtus šuolius (pvz., klaidas, sukeliančias perteklinius API ciklus).

**Užklausų klaidos:** Kiek užklausų agentas nepavyko įvykdyti? Tai gali apimti API klaidas arba nesėkmingus įrankių kvietimus. Norėdami padaryti agentą atsparesnį tokioje gamybinėje aplinkoje, galite nustatyti atsargines galimybes arba pakartojimus. Pvz., jei LLM tiekėjas A neveikia, perjungiate į LLM tiekėją B kaip atsarginį.

**Vartotojų atsiliepimai:** Tiesioginiai vartotojų vertinimai suteikia vertingų įžvalgų. Tai gali būti aiškūs įvertinimai (👍patinka/👎nepatinka, ⭐1–5 žvaigždutės) arba tekstiniai komentarai. Nuolatiniai neigiami atsiliepimai turėtų įspėti, kad agentas neveikia taip, kaip tikėtasi.

**Netiesioginiai vartotojų signalai:** Vartotojų elgesys suteikia netiesioginių atsiliepimų net be aiškių vertinimų. Tai gali apimti klausimų perrašymą iš karto, pasikartojančias užklausas arba mygtuko „išbandyti dar kartą“ paspaudimus. Pvz., jei matote, kad vartotojai pakartotinai užduoda tą patį klausimą, tai ženklas, kad agentas neveikia kaip tikėtasi.

**Tikslumas:** Kaip dažnai agentas generuoja teisingus arba pageidaujamus rezultatus? Tikslumo apibrėžimai skiriasi (pvz., sprendimo teisingumas, informacijos gavimo tikslumas, vartotojo pasitenkinimas). Pirmas žingsnis yra apibrėžti, koks yra sėkmės kriterijus jūsų agentui. Galite sekti tikslumą per automatinius patikrinimus, vertinimo balus arba užduoties užbaigimo žymes. Pavyzdžiui, žymint sekas kaip „sėkminga“ arba „nesėkminga“.

**Automatizuoti vertinimo rodikliai:** Taip pat galite nustatyti automatizuotus vertinimus. Pavyzdžiui, galite naudoti LLM, kad įvertintumėte agento išvestį, pvz., ar ji naudinga, tiksli ar ne. Yra keli atvirojo kodo bibliotekos, kurios padeda įvertinti skirtingus agento aspektus. Pvz., [RAGAS](https://docs.ragas.io/) RAG agentams arba [LLM Guard](https://llm-guard.com/) žalingai kalbai ar prompt injekcijai aptikti.

Praktikoje šių rodiklių derinys suteikia geriausią AI agento būklės aprėptį. Šio skyriaus [pavyzdiniame užrašyne](./code_samples/10-expense_claim-demo.ipynb) parodysime, kaip šie rodikliai atrodo realiuose pavyzdžiuose, tačiau pirmiausia sužinosime, kaip atrodo tipinis vertinimo darbo srautas.

## Instrumentuokite savo agentą

Norėdami surinkti sekų duomenis, turėsite instrumentuoti savo kodą. Tikslas – instrumentuoti agento kodą taip, kad jis emituotų sekas ir rodiklius, kuriuos gali užfiksuoti, apdoroti ir vizualizuoti stebimumo platforma.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) tapo pramonės standartu LLM stebimumui. Ji suteikia API, SDK ir įrankius telemetrijos duomenims generuoti, rinkti ir eksportuoti.

Yra daug instrumentavimo bibliotekų, kurios apgaubia esamus agentų rinkinius ir palengvina OpenTelemetry spanų eksportavimą į stebimumo įrankį. Microsoft Agent Framework natūraliai integruojasi su OpenTelemetry. Toliau pateiktas pavyzdys, kaip instrumentuoti MAF agentą:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentų vykdymas automatiškai fiksuojamas
    pass
```

Šio skyriaus [pavyzdiniame užrašyne](./code_samples/10-expense_claim-demo.ipynb) bus parodyta, kaip instrumentuoti savo MAF agentą.

**Rankinis spanų kūrimas:** Nors instrumentavimo bibliotekos suteikia gerą pradžią, dažnai yra atvejų, kai reikia išsamesnės ar pritaikytos informacijos. Galite rankiniu būdu kurti spanus, kad pridėtumėte vartotojo logiką. Svarbiau, kad jie gali praturtinti automatiškai arba rankiniu būdu sukurtus spanus su pritaikytomis atributų reikšmėmis (dar vadinamomis žymomis arba metaduomenimis). Šie atributai gali apimti verslo specifinius duomenis, tarpinio apdorojimo rezultatus ar bet kokį kontekstą, kuris gali būti naudingas derinimui ar analizei, pvz., `user_id`, `session_id` arba `model_version`.

Pavyzdys, kaip rankiniu būdu sukurti sekas ir spanus su [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentų vertinimas

Stebimumas suteikia mums rodiklius, tačiau vertinimas yra procesas, kai analizuojami tie duomenys (ir atliekami testai), kad būtų nustatyta, kaip gerai veikia AI agentas ir kaip jį galima pagerinti. Kitaip tariant, turėdami sekas ir rodiklius, kaip juos panaudoti agento vertinimui ir sprendimams priimti?

Reguliarus vertinimas yra svarbus, nes AI agentai dažnai yra nedeterministiniai ir gali kisti (per atnaujinimus arba modelio elgsenos poslinkį) – be vertinimo nežinotumėte, ar jūsų „išmanusis agentas“ iš tikrųjų atlieka savo darbą gerai arba ar jis regresavo.

Yra dvi agentų vertinimo kategorijos: **online vertinimas** ir **offline vertinimas**. Abu yra vertingi ir papildo vienas kitą. Paprastai pradedame nuo offline vertinimo, nes tai yra minimalus būtinas žingsnis prieš diegiant bet kurį agentą.

### Offline vertinimas

![Duomenų rinkinio elementai Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tai reiškia agento vertinimą kontroliuojamoje aplinkoje, paprastai naudojant testinius duomenų rinkinius, o ne tiesiogines vartotojų užklausas. Naudojate kruopščiai parengtus duomenų rinkinius, kuriuose žinote, koks yra tikimasis išvestis arba teisingas elgesys, ir tada paleidžiate agentą ant jų.

Pavyzdžiui, jei sukūrėte agentą, sprendžiantį matematikos žodinius uždavinius, galite turėti [testinį duomenų rinkinį](https://huggingface.co/datasets/gsm8k) su 100 uždavinių ir žinomais atsakymais. Offline vertinimas dažnai atliekamas vystymo metu (ir gali būti CI/CD grandinių dalis), kad patikrintumėte patobulinimus arba apsisaugotumėte nuo regresijų. Privalumas yra tas, kad tai yra **kartojama ir galite gauti aiškius tikslumo rodiklius, nes turite kontrolinę tiesą**. Taip pat galite sukurti vartotojų užklausų simuliacijas ir palyginti agento atsakymus su idealiais atsakymais arba naudoti automatinius rodiklius, kaip aprašyta aukščiau.

Pagrindinis iššūkis su offline vertinimu yra užtikrinti, kad jūsų testinis duomenų rinkinys būtų išsamus ir išliktų aktualus – agentas gali gerai veikti fiksuotame testiniame rinkinyje, bet gamyboje susidurti su labai skirtingomis užklausomis. Todėl turėtumėte atnaujinti testų rinkinius su naujais kraštutiniais atvejais ir pavyzdžiais, atspindinčiais realias situacijas. Naudinga turėti mažų „smoke test“ atvejų ir didesnių vertinimo rinkinių: mažesni rinkiniai greitiems patikrinimams, didesni – platesniems našumo rodikliams.

### Online vertinimas

![Stebimumo rodiklių apžvalga](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tai reiškia agento vertinimą tiesioginėje, realioje aplinkoje, t. y. naudojimo metu gamyboje. Online vertinimas apima agento našumo stebėjimą realiose vartotojų sąveikose ir rezultatų nuolatinę analizę.

Pavyzdžiui, galite sekti sėkmės rodiklius, vartotojų pasitenkinimo įvertinimus arba kitus rodiklius tiesioginiame sraute. Online vertinimo privalumas yra tas, kad jis **fiksuoja dalykus, kurių laboratorinėje aplinkoje galėjote neprognozuoti** – galite stebėti modelio elgsenos poslinkį laikui bėgant (jei agento veiksmingumas mažėja, kai keičiasi įvesties modeliai) ir užfiksuoti netikėtas užklausas ar situacijas, kurios nebuvo jūsų testiniuose duomenyse. Tai suteikia tikrą vaizdą, kaip agentas elgiasi gamtoje.

Online vertinimas dažnai apima netiesioginių ir aiškių vartotojų atsiliepimų rinkimą, kaip aptarta anksčiau, ir galbūt vykdymą šešėlinio testo arba A/B testų (kai nauja agento versija veikia lygiagrečiai senajai, kad būtų galima palyginti). Iššūkis yra tas, kad sunku gauti patikimus etikečių ar įvertinimų duomenis tiesioginėms sąveikoms – gali tekti remtis vartotojų atsiliepimais arba antrinėmis metrikomis (pvz., ar vartotojas paspaudė rezultatus).

### Abu derinami kartu

Online ir offline vertinimai nėra vienas kito alternatyvos; jie labai papildo vienas kitą. Online stebėjimo įžvalgos (pvz., naujos užklausų rūšys, kur agentas vykdo prasčiau) gali būti naudojamos offline testinių rinkinių papildymui ir tobulinimui. Atvirkščiai, agentai, kurie gerai pasirodo offline testuose, gali būti saugiau diegiami ir stebimi online.

Iš tiesų daug komandos diegia kilpą:

_vertinti offline -> diegti -> stebėti online -> surinkti naujus gedimo atvejus -> pridėti prie offline duomenų rinkinio -> tobulinti agentą -> kartoti_.

## Dažnos problemos

Diegdami AI agentus gamyboje galite susidurti su įvairiais iššūkiais. Čia pateikiamos kelios dažnos problemos ir galimi sprendimai:

| **Problema**    | **Galimas sprendimas**   |
| ------------- | ------------------ |
| AI Agentas neatlieka užduočių nuosekliai | - Patikslinkite agentui duodamą promptą; aiškiai nurodykite tikslus.<br>- Nustatykite, ar užduotis verta suskaidyti į subužduotis ir paskirstyti keliems agentams. |
| AI Agentas patenka į nuolatinius ciklus  | - Užtikrinkite aiškias nutraukimo sąlygas, kad agentas žinotų, kada sustoti.<br>- Sudėtingoms užduotims, reikalaujančioms samprotavimo ir planavimo, naudokite didesnį modelį, specializuotą tokiems uždaviniams. |
| AI agento įrankių kvietimai neveikia gerai   | - Išbandykite ir patikrinkite įrankio išvestį nepriklausomai nuo agento sistemos.<br>- Patobulinkite parametrus, promptus ir įrankių pavadinimus.  |
| Daugiagentinė sistema neveikia nuosekliai | - Patikslinkite kiekvienam agentui skirtus promptus, kad jie būtų konkretūs ir skirtingi vienas nuo kito.<br>- Sukurkite hierarchinę sistemą, naudojant maršruto (routing) arba valdymo agentą, kuris nuspręstų, kuris agentas yra tinkamiausias. |

Daugelis šių problemų gali būti nustatytos efektyviau, kai yra įdiegtas stebimumas. Anksčiau aptartos sekos ir rodikliai padeda tiksliai nustatyti, kurioje agento darbo eigoje atsiranda problemos, todėl derinimas ir optimizavimas tampa daug efektyvesni.

## Sąnaudų valdymas
Štai kelios strategijos, kaip valdyti dirbtinio intelekto agentų diegimo į gamybinę aplinką kaštus:

**Using Smaller Models:** Maži kalbos modeliai (SLMs) tam tikrais agentiniais naudojimo atvejais gali veikti gerai ir žymiai sumažinti išlaidas. Kaip minėta anksčiau, įvertinimų sistemos sukūrimas, leidžiantis nustatyti ir palyginti našumą su didesniais modeliais, yra geriausias būdas suprasti, kaip gerai SLM veiks jūsų atveju. Apsvarstykite galimybę naudoti SLM paprastesnėms užduotims, tokioms kaip ketinimų klasifikavimas ar parametrų išgavimas, o sudėtingesniam samprotavimui skirkite didesnius modelius.

**Using a Router Model:** Panaši strategija yra naudoti įvairių modelių ir dydžių derinį. Galite naudoti LLM/SLM arba serverless funkciją, kad maršrutizuotumėte užklausas pagal sudėtingumą į tinkamiausius modelius. Tai taip pat padės sumažinti išlaidas ir užtikrinti našumą tinkamose užduotyse. Pavyzdžiui, nukreipkite paprastas užklausas į mažesnius, greitesnius modelius ir brangius didelius modelius naudokite tik sudėtingiems samprotavimo uždaviniams.

**Caching Responses:** Bendrų užklausų ir užduočių identifikavimas ir atsakymų pateikimas prieš jiems pereinant per jūsų agentinę sistemą yra geras būdas sumažinti panašių užklausų kiekį. Netgi galite įgyvendinti procesą, kad nustatytumėte, kiek užklausa panaši į talpykloje saugomas užklausas, naudodami paprastesnius DI modelius. Ši strategija gali žymiai sumažinti išlaidas dažnai užduodamiems klausimams arba įprastiems darbo eigoms.

## Pažiūrėkime, kaip tai veikia praktikoje

In the [šio skyriaus pavyzdiniame užrašų knygoje](./code_samples/10-expense_claim-demo.ipynb), pamatysime pavyzdžių, kaip galime naudoti stebėjimo įrankius, kad stebėtume ir vertintume savo agentą.


### Turite daugiau klausimų apie AI agentus gamybinėje aplinkoje?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), susipažinkite su kitais besimokančiaisiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Ankstesnė pamoka

[Metakognicijos dizaino šablonas](../09-metacognition/README.md)

## Kita pamoka

[Agentiniai protokolai](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą Co‑op Translator (https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas pirminiu (autoritetiniu) šaltiniu. Kritiniais atvejais rekomenduojame pasinaudoti profesionalaus žmogaus vertėjo paslaugomis. Mes neatsakome už jokius nesusipratimus ar neteisingas interpretacijas, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->