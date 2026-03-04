# DI agentai gamyboje: stebėjimas ir vertinimas

[![DI agentai gamyboje](../../../translated_images/lt/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kai DI agentai pereina nuo eksperimentinių prototipų prie realių taikymų, tampa svarbu suprasti jų elgseną, stebėti jų našumą ir sistemingai vertinti jų rezultatus.

## Mokymosi tikslai

Baigę šią pamoką, jūs sužinosite / suprasite:
- Pagrindines agentų stebėjimo ir vertinimo sąvokas
- Technikas agentų veikimui, kaštams ir efektyvumui gerinti
- Ką ir kaip sistemingai įvertinti savo DI agentus
- Kaip valdyti kaštus diegiant DI agentus gamyboje
- Kaip instrumentuoti agentus, sukurtus su AutoGen

Tikslas – suteikti jums žinių, kad paverstumėte savo „juodosios dėžės“ agentus skaidriais, valdomais ir patikimais sistemomis.

_**Pastaba:** Svarbu diegti saugius ir patikimus DI agentus. Taip pat peržiūrėkite pamoką apie [Saugūs ir patikimi DI agentai](../06-building-trustworthy-agents/README.md)._

## Trasos ir span'ai

Stebėjimo įrankiai, tokie kaip [Langfuse](https://langfuse.com/) arba [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), paprastai agentų vykdymus vaizduoja kaip trasas ir span'us.

- **Trasa** reiškia pilną agento užduotį nuo pradžios iki pabaigos (pvz., vartotojo užklausos apdorojimas).
- **Span'ai** yra atskiri žingsniai trasoje (pvz., kalbos modelio kvietimas arba duomenų gavimas).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Be stebėjimo DI agentas gali jaustis kaip „juodoji dėžė“ – jo vidinė būsena ir samprotavimai yra neaiškūs, todėl sunku diagnozuoti klaidas ar optimizuoti veikimą. Su stebėjimu agentai tampa „stiklinėmis dėžėmis“, suteikiančiomis skaidrumą, kuris yra būtinas pasitikėjimui kurti ir užtikrinti, kad jie veiktų taip, kaip tikėtasi.

## Kodėl stebėjimas yra svarbus gamybos aplinkose

Perkėlimas DI agentų į gamybos aplinką sukuria naujų iššūkių ir reikalavimų. Stebėjimas nebėra „malonu turėti“, o tapo kritine galimybe:

*   **Derinimas ir šakninių priežasčių analizė:** Kai agentas sugenda arba pateikia netikėtą atsakymą, stebėjimo įrankiai suteikia trasas, reikalingas tiksliai nustatyti klaidos šaltinį. Tai ypač svarbu sudėtingiems agentams, kuriuose gali būti keli LLM kvietimai, įrankių sąveikos ir sąlyginė logika.
*   **Latencijos ir kaštų valdymas:** DI agentai dažnai remiasi LLM ir kitais išoriniais API, kurių sąskaitos skaičiuojamos už simbolį arba už kvietimą. Stebėjimas leidžia tiksliai sekti šiuos kvietimus, padedant identifikuoti veiksmus, kurie yra per lėti arba brangūs. Tai leidžia komandoms optimizuoti užklausas, pasirinkti efektyvesnius modelius arba pertvarkyti darbo eigas, kad valdytų veiklos kaštus ir užtikrintų gerą vartotojo patirtį.
*   **Pasitikėjimas, sauga ir atitiktis:** Daugelyje taikymų svarbu užtikrinti, kad agentai elgtųsi saugiai ir etiškai. Stebėjimas suteikia agento veiksmų ir sprendimų audito pėdsaką. Tai galima naudoti aptikti ir sušvelninti problemas, tokias kaip užklausų injekcija, kenksmingo turinio generavimas ar netinkamas asmens identifikuojamos informacijos (PII) tvarkymas. Pavyzdžiui, galite peržiūrėti trasas, kad suprastumėte, kodėl agentas pateikė tam tikrą atsakymą arba panaudojo konkretų įrankį.
*   **Nuolatinio tobulinimo ciklai:** Stebėjimo duomenys yra iteracinio vystymo proceso pagrindas. Stebėdami, kaip agentai veikia realiame pasaulyje, komandos gali nustatyti tobulintinas sritis, rinkti duomenis modelių tobulinimui ir patvirtinti pakeitimų poveikį. Tai sukuria atsiliepimų kilpą, kurioje įžvalgos iš gamybos online vertinimo informuoja offline eksperimentus ir patobulinimus, vedančius prie nuolat gerėjančio agentų veikimo.

## Pagrindiniai rodikliai, kuriuos verta sekti

Norint stebėti ir suprasti agento elgseną, reikia sekti įvairius rodiklius ir signalus. Konkretūs rodikliai gali skirtis priklausomai nuo agento paskirties, bet kai kurie yra universaliai svarbūs.

Štai keletas dažniausiai stebimų rodiklių:

**Latencija:** Kaip greitai agentas atsako? Ilgas laukimo laikas neigiamai veikia vartotojo patirtį. Turėtumėte matuoti latenciją užduotims ir atskiriems žingsniams, trasuojant agento vykdymus. Pavyzdžiui, agentą, kuriam visiems modelio kvietimams prireikia 20 sekundžių, galima pagreitinti naudojant greitesnį modelį arba vykdant modelio kvietimus lygiagrečiai.

**Kaštai:** Kiek kainuoja vienas agento vykdymas? DI agentai remiasi LLM kvietimais, apmokestinamais už simbolį, arba išoriniais API. Dažnas įrankių naudojimas arba keli užklausimai gali greitai išauginti kaštus. Pavyzdžiui, jei agentas penkis kartus kviečia LLM dėl menko kokybės pagerėjimo, turite įvertinti, ar tai pateisina kaštus, ar galite sumažinti kvietimų skaičių arba naudoti pigesnį modelį. Realaus laiko stebėjimas taip pat gali padėti nustatyti netikėtus šuolius (pvz., klaidos, sukėliančios per daug API ciklų).

**Užklausų klaidos:** Kiek užklausų agentas nepavyko apdoroti? Tai gali apimti API klaidas arba nepavykusius įrankių kvietimus. Kad agentas būtų atsparesnis šiems atvejams gamyboje, galite sukonfigūruoti atsarginius sprendimus arba pakartojimus. Pvz., jei LLM tiekėjas A neveikia, pereikite prie LLM tiekėjo B kaip atsarginio varianto.

**Vartotojo atsiliepimai:** Tiesioginiai vartotojų įvertinimai suteikia vertingų įžvalgų. Tai gali būti aiškūs reitingai (👍patinka/👎nepatinka, ⭐1-5 žvaigždutės) arba tekstiniai komentarai. Nuolatiniai neigiami atsiliepimai turėtų jus įspėti, nes tai ženklas, kad agentas neveikia taip, kaip tikėtasi.

**Netiesioginiai vartotojo atsiliepimai:** Vartotojų elgsena teikia netiesioginį grįžtamąjį ryšį net be aiškių įvertinimų. Tai gali būti greitas klausimo perrašymas, pasikartojančios užklausos arba paspaudimas mygtuko „bandyti dar kartą“. Pvz., jei matote, kad vartotojai nuolat užduoda tą patį klausimą, tai yra ženklas, kad agentas neveikia kaip tikėtasi.

**Tikslumas:** Kaip dažnai agentas generuoja teisingus arba pageidaujamus rezultatus? Tikslumo apibrėžimai skiriasi (pvz., problemų sprendimo teisingumas, informacijos paieškos tikslumas, vartotojo pasitenkinimas). Pirmas žingsnis yra apibrėžti, ką jūsų agentui reiškia sėkmė. Tikslumą galite sekti automatizuotais patikrinimais, vertinimo balais arba užduoties užbaigimo žymomis. Pavyzdžiui, žymėti trasas kaip „sėkmingas“ arba „nepavyko“.

**Automatizuoti vertinimo rodikliai:** Taip pat galite sukurti automatizuotus vertinimus. Pvz., galite naudoti LLM, kad įvertintumėte agento išvestį — ar ji naudinga, tiksli ar ne. Taip pat yra kelios atviro kodo bibliotekos, kurios padeda vertinti skirtingus agento aspektus. Pvz. [RAGAS](https://docs.ragas.io/) RAG agentams arba [LLM Guard](https://llm-guard.com/) kenksmingai kalbai ar užklausų injekcijai aptikti.

Praktikoje šių rodiklių derinys suteikia geriausią DI agento sveikatos aprėptį. Šio skyriaus [pavyzdiniame užrašų knygelėje](./code_samples/10_autogen_evaluation.ipynb) parodysime, kaip šie rodikliai atrodo realiuose pavyzdžiuose, bet pirmiausia išmokysime, kaip atrodo tipinė vertinimo darbo eiga.

## Instrumentuokite savo agentą

Norėdami surinkti trasavimo duomenis, turėsite instrumentuoti savo kodą. Tikslas yra instrumentuoti agento kodą taip, kad jis siųstų trasas ir rodiklius, kuriuos galėtų užfiksuoti, apdoroti ir vizualizuoti stebėjimo platforma.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) tapo pramonės standartu LLM stebėjimui. Ji teikia API, SDK ir įrankius telemetrijos duomenų generavimui, rinkimui ir eksportavimui.

Yra daug instrumentavimo bibliotekų, kurios supakuoja esamas agentų sistemas ir palengvina OpenTelemetry span'ų eksportavimą į stebėjimo įrankį. Žemiau pateiktas pavyzdys, kaip instrumentuoti AutoGen agentą su [OpenLit instrumentavimo biblioteka](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Šio skyriaus [pavyzdinė užrašų knygelė](./code_samples/10_autogen_evaluation.ipynb) demonstruos, kaip instrumentuoti jūsų AutoGen agentą.

**Rankinis span'ų kūrimas:** Nors instrumentavimo bibliotekos suteikia gerą pradžią, dažnai reikia detalesnės arba pritaikytos informacijos. Galite rankiniu būdu kurti span'us, kad pridėtumėte pritaikytą programos logiką. Svarbiau, kad galite praturtinti automatiškai arba rankiniu būdu sukurtus span'us pritaikytais atributais (dar vadinamais žymėmis arba metaduomenimis). Šie atributai gali apimti verslui specifinius duomenis, tarpinį skaičiavimą arba bet kokį kontekstą, kuris gali būti naudingas derinimui arba analizei, pavyzdžiui, `user_id`, `session_id` arba `model_version`.

Pavyzdys, kaip rankiniu būdu kurti trasas ir span'us su [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentų vertinimas

Stebėjimas suteikia rodiklius, tačiau vertinimas yra tas procesas, kai analizuojami tie duomenys (ir atliekami testai), siekiant nustatyti, kaip gerai veikia DI agentas ir kaip jį galima patobulinti. Kitaip tariant, kai turite trasas ir rodiklius, kaip juos naudoti agentui įvertinti ir priimti sprendimus?

Reguliarus vertinimas yra svarbus, nes DI agentai dažnai nėra determinuojami ir gali kisti (per atnaujinimus arba modelio elgsenos pasislinkimą) – be vertinimo nežinotumėte, ar jūsų „protingas agentas“ iš tikrųjų atlieka savo darbą gerai arba ar neatsirado regresija.

Yra dvi agentų vertinimo kategorijos: **online vertinimas** ir **offline vertinimas**. Abu yra vertingi ir papildo vienas kitą. Paprastai pradedame nuo offline vertinimo, nes tai yra minimalus būtinas žingsnis prieš diegiant bet kurį agentą.

### Offline vertinimas

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tai apima agento vertinimą kontroliuojamoje aplinkoje, paprastai naudojant testinius duomenų rinkinius, o ne gyvas vartotojų užklausas. Naudojate atrinktus duomenų rinkinius, kuriuose žinote, koks yra tikėtinas atsakas arba teisingas elgesys, ir tada paleidžiate agentą su tais duomenimis.

Pavyzdžiui, jei sukūrėte matematikos žodinių uždavinių agentą, galite turėti [testinį duomenų rinkinį](https://huggingface.co/datasets/gsm8k) su 100 uždavinių, kurių atsakymai yra žinomi. Offline vertinimas dažnai atliekamas vystymo metu (ir gali būti CI/CD eigos dalis), kad būtų patikrinti patobulinimai arba apsaugota nuo regresijų. Privalumas tas, kad tai yra **pakartojama ir galite gauti aiškius tikslumo rodiklius, nes turite pagrindinę tiesą**. Taip pat galite simuliuoti vartotojų užklausas ir palyginti agento atsakymus su idealiais atsakymais arba naudoti automatizuotus rodiklius, kaip aprašyta aukščiau.

Pagrindinis offline vertinimo iššūkis – užtikrinti, kad jūsų testinis duomenų rinkinys būtų išsamus ir liktų aktualus – agentas gali gerai pasirodyti fiksuotame testų rinkinyje, bet gamyboje susidurti su labai skirtingomis užklausomis. Todėl turėtumėte nuolat atnaujinti testų rinkinius naujais ribiniais atvejais ir pavyzdžiais, atspindinčiais realaus pasaulio scenarijus. Naudinga derinti mažas „dūmų bandymo“ bylas ir didesnius vertinimo rinkinius: mažesni rinkiniai greitiems patikrinimams, didesni – platesniems našumo rodikliams.

### Online vertinimas

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tai reiškia agento vertinimą gyvoje, realioje aplinkoje, t. y. faktinio naudojimo gamyboje metu. Online vertinimas apima agento našumo stebėjimą realių vartotojų sąveikose ir nuolatinę rezultatų analizę.

Pavyzdžiui, galite stebėti sėkmingumo rodiklius, vartotojų pasitenkinimo balus ar kitus rodiklius gyvam srautui. Online vertinimo privalumas yra tas, kad jis **fiksuoja dalykus, kurių laboratorijoje galite neprognozuoti** – galite stebėti modelio elgsenos poslinkį laikui bėgant (jei agento efektyvumas mažėja, kai keičiasi įvesties modeliai) ir aptikti netikėtas užklausas ar situacijas, kurių nebuvo jūsų testų duomenyse. Tai suteikia tikrą vaizdą, kaip agentas elgiasi realiame pasaulyje.

Online vertinimas dažnai apima netiesioginio ir tiesioginio vartotojo grįžtamojo ryšio rinkimą, kaip aptarta anksčiau, ir galbūt vykdo šešėlinius testus arba A/B testus (kai nauja agento versija veikia lygiagrečiai, kad būtų palyginta su sena). Iššūkis tas, kad gali būti sunku gauti patikimas etiketes arba balus gyvoms sąveikoms – galite remtis vartotojų atsiliepimais arba žemutinių grandžių rodikliais (pvz., ar vartotojas paspaudė rezultatą).

### Abiejų derinimas

Online ir offline vertinimai nėra vienas kitam prieštaraujantys; jie labai papildo vienas kitą. Įžvalgos iš online monitoring'o (pvz., nauji vartotojų užklausų tipai, kuriuose agentas blogai pasirodo) gali būti naudojamos papildyti ir patobulinti offline testų rinkinius. Atvirkščiai, agentai, kurie gerai pasirodo offline testuose, gali būti drąsiau diegiami ir stebimi online.

Iš tikrųjų daug komandos taiko kilpą:

_įvertinkite offline -> diegkite -> stebėkite online -> surinkite naujus klaidų atvejus -> pridėkite prie offline rinkinio -> patobulinkite agentą -> pakartokite_.

## Dažnos problemos

Diegdami DI agentus gamyboje galite susidurti su įvairiais iššūkiais. Čia pateikiamos kelios dažnos problemos ir galimi sprendimai:

| **Problema**    | **Galimas sprendimas**   |
| ------------- | ------------------ |
| DI agentas nekonsistentiškai atlieka užduotis | - Patikslinkite agentui duodamą užklausą; aiškiai nurodykite tikslus.<br>- Nustatykite, ar užduoties suskirstymas į poskyrius ir jų vykdymas kelių agentų gali padėti. |
| DI agentas patekęs į nuolatines ciklas  | - Įsitikinkite, kad turite aiškias proceso nutraukimo sąlygas, kad agentas žinotų, kada sustoti.<br>- Sudėtingoms užduotims, reikalaujančioms samprotavimo ir planavimo, naudokite didesnį modelį, specializuotą samprotavimui. |
| DI agento įrankių kvietimai veikia prastai   | - Išbandykite ir patikrinkite įrankio išvestį už agento sistemos ribų.<br>- Patikslinkite apibrėžtus parametrus, užklausas ir įrankių pavadinimus.  |
| Daugiagentė sistema nekonsistiškai veikia | - Patikslinkite kiekvienam agentui duodamas užklausas, kad jos būtų specifinės ir skirtingos.<br>- Sukurkite hierarchinę sistemą, naudodami „routingo“ arba valdymo agentą, kad nustatytumėte, kuris agentas yra tinkamiausias. |

Daugelis šių problemų gali būti geriau identifikuotos turint stebėjimą. Anksčiau aptartos trasos ir rodikliai padeda tiksliai nustatyti, kur agentų darbo eigoje kyla problemos, todėl derinimas ir optimizavimas tampa daug efektyvesni.

## Kaštų valdymas
Štai keletas strategijų, kaip valdyti dirbtinio intelekto agentų diegimo į gamybą kaštus:

**Using Smaller Models:** Maži kalbos modeliai (SLMs) gali gerai veikti tam tikrais agentiškais atvejais ir žymiai sumažins kaštus. Kaip minėta anksčiau, geriausias būdas suprasti, kaip gerai SLM veiks jūsų naudojimo atveju, yra sukurti vertinimo sistemą, skirtą nustatyti ir palyginti našumą su didesniais modeliais. Apsvarstykite galimybę naudoti SLM paprastesnėms užduotims, tokioms kaip ketinimų klasifikacija ar parametrų išgavimas, o sudėtingam samprotavimui palikite didesnius modelius.

**Using a Router Model:** Panaši strategija yra naudoti skirtingus modelius ir jų dydžius. Galite naudoti LLM/SLM arba serverless funkciją, kad maršrutizuotumėte užklausas pagal sudėtingumą į geriausiai tinkamus modelius. Tai taip pat padės sumažinti kaštus ir užtikrinti našumą tinkamoms užduotims. Pavyzdžiui, maršrutizuokite paprastas užklausas į mažesnius, greitesnius modelius ir naudokite brangius, didelius modelius tik sudėtingoms samprotavimo užduotims.

**Caching Responses:** Nustatant dažniausias užklausas ir užduotis bei pateikiant atsakymus prieš jiems pereinant per jūsų agentinę sistemą, galima sumažinti panašių užklausų kiekį. Netgi galite įdiegti srautą, kad nustatytumėte, kiek užklausa panaši į jūsų talpykloje esančias užklausas, naudodami paprastesnius DI modelius. Ši strategija gali žymiai sumažinti kaštus dažnai užduodamiems klausimams arba įprastiems darbo procesams.

## Pažiūrėkime, kaip tai veikia praktiškai

Šiame [skyriaus pavyzdiniame užrašų knygelyje](./code_samples/10_autogen_evaluation.ipynb) pamatysime pavyzdžių, kaip galime naudoti stebėjimo įrankius mūsų agentui stebėti ir vertinti.

### Ar turite daugiau klausimų apie dirbtinio intelekto agentus gamyboje?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susipažintumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo klausimus apie dirbtinio intelekto agentus.

## Ankstesnė pamoka

[Metakognicijos dizaino šablonas](../09-metacognition/README.md)

## Kita pamoka

[Agentiniai protokolai](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą Co-op Translator (https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Jei informacija yra kritinė, rekomenduojame kreiptis į profesionalų vertėją. Mes neatsakome už jokių nesusipratimų ar neteisingų aiškinimų, kylančių dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->