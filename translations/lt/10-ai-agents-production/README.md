# DI agentai gamyboje: matomumas ir vertinimas

[![DI agentai gamyboje](../../../translated_images/lt/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kai DI agentai pereina nuo eksperimentinių prototipų prie realių taikymų, tampa svarbu gebėti suprasti jų elgseną, stebėti našumą ir sistemingai įvertinti jų rezultatus.

## Mokymosi tikslai

Baigę šią pamoką, jūs sužinosite arba suprasite:
- Pagrindines agentų matomumo ir vertinimo sąvokas
- Technikas, kaip pagerinti agentų našumą, kaštus ir veiksmingumą
- Ką ir kaip sistemingai įvertinti savo DI agentus
- Kaip valdyti kaštus diegiant DI agentus gamyboje
- Kaip instrumentuoti agentus, sukurtus naudojant Microsoft Agent Framework

Tikslas – suteikti žinių, kad jūsų „juodosios dėžės“ agentai taptų skaidrūs, valdomi ir patikimi sistemos komponentai.

_**Pastaba:** Svarbu diegti saugius ir patikimus DI agentus. Taip pat peržiūrėkite pamoką [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces ir Spans

Stebėjimo įrankiai, tokie kaip [Langfuse](https://langfuse.com/) arba [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), paprastai atvaizduoja agentų vykdymus kaip traces ir spans.

- **Trace** reiškia užduotį, kurią agentas atlieka nuo pradžios iki pabaigos (pvz., vartotojo užklausos apdorojimas).
- **Spans** yra atskiros žingsnių dalys trace viduje (pvz., kalbos modelio iškvietimas arba duomenų gavimas).

![Trace medis Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Be matomumo DI agentas gali atrodyti kaip „juodoji dėžė“ – jo vidinė būsena ir samprotavimai yra neaiškūs, todėl sunku nustatyti gedimus ar optimizuoti veikimą. Turint matomumą, agentai tampa „stiklinėmis dėžėmis“, suteikiančiomis skaidrumą, kuris yra būtinas pasitikėjimui kurti ir užtikrinti, kad jie veiktų taip, kaip numatyta.

## Kodėl matomumas svarbus gamybos aplinkose

Pereinant DI agentams į gamybos aplinkas atsiranda naujų iššūkių ir reikalavimų. Matomumas nebėra „naudingas priedas“, o kritinė galimybė:

*   **Debug‘inimas ir pagrindinės priežasties analizė**: Kai agentas sugenda arba pateikia netikėtą rezultatą, stebėjimo įrankiai pateikia traces, reikalingas klaidos šaltiniui nustatyti. Tai ypač svarbu sudėtinguose agentuose, kuriuose gali būti keli LLM iškvietimai, įrankių sąveikos ir sąlyginė logika.
*   **Latencijos ir kaštų valdymas**: DI agentai dažnai remiasi LLM ir kitais išoriniais API, kuriems taikomas apmokėjimas už token’us ar už iškvietimą. Matomumas leidžia tiksliai sekti šiuos iškvietimus, padedant identifikuoti operacijas, kurios yra per lėtos arba brangios. Tai suteikia galimybę optimizuoti prompt’us, pasirinkti efektyvesnius modelius arba pertvarkyti darbo eigas, siekiant valdyti veiklos kaštus ir užtikrinti gerą vartotojo patirtį.
*   **Pasitikėjimas, sauga ir atitiktis**: Daugelyje taikymų svarbu užtikrinti, kad agentai elgtųsi saugiai ir etiškai. Matomumas suteikia audito pėdsaką apie agento veiksmus ir sprendimus. Tai galima naudoti aptikti ir sušvelninti tokias problemas kaip promptų injekcija, kenksmingo turinio generavimas arba asmens duomenų (PII) netinkamas tvarkymas. Pavyzdžiui, galite peržiūrėti traces, kad suprastumėte, kodėl agentas pateikė tam tikrą atsakymą arba panaudojo konkretų įrankį.
*   **Nuolatinio tobulinimo ciklai**: Matomumo duomenys yra iteratyvaus vystymo proceso pagrindas. Stebint, kaip agentai veikia realiame pasaulyje, komandos gali nustatyti tobulintinas sritis, surinkti duomenis modelių tobulinimui ir patikrinti pakeitimų poveikį. Tai sukuria atgalinio ryšio lauką, kuriame gamybiniai įžvalgos iš online vertinimo informuoja offline eksperimentus ir patobulinimus, vedančius prie nuosekliai gerėjančio agento veikimo.

## Pagrindiniai rodikliai, kuriuos verta sekti

Norint stebėti ir suprasti agento elgseną, reikėtų sekti įvairius rodiklius ir signalus. Konkrečios metrikos gali skirtis priklausomai nuo agento paskirties, tačiau kai kurios yra universaliai svarbios.

Čia pateikiami dažniausiai stebimi rodikliai:

**Vėlavimas (Latency):** Kaip greitai agentas atsako? Ilgi laukimo laikai neigiamai veikia vartotojo patirtį. Jūs turėtumėte matuoti vėlavimą užduotims ir atskiriems žingsniams tracindami agentų vykdymus. Pvz., agentas, kuriam visiems modelio iškvietimams reikia 20 sekundžių, gali būti pagreitintas naudojant greitesnį modelį arba vykdant modelio iškvietimus lygiagrečiai.

**Kaštai:** Kiek kainuoja vienas agento vykdymas? DI agentai remiasi LLM iškvietimais, apmokestinamais už token’us, arba išoriniais API. Dažnas įrankių naudojimas arba keli prompt’ai gali greitai padidinti kaštus. Pavyzdžiui, jeigu agentas penkis kartus kviečia LLM dėl menkos kokybės pagerinimo, reikia įvertinti, ar tai pateisina kaštus, ar galima sumažinti iškvietimų skaičių arba naudoti pigesnį modelį. Realiojo laiko stebėjimas taip pat padeda pastebėti netikėtus šuolius (pvz., klaidos, sukeliančios perteklines API kilpas).

**Užklausų klaidos (Request Errors):** Kiek užklausų agentas nepavyko įvykdyti? Tai gali apimti API klaidas arba nepavykusius įrankių iškvietimus. Kad jūsų agentas būtų atsparesnis gamyboje, galite nustatyti atsargines parinktis arba bandymus iš naujo. Pvz., jei LLM tiekėjas A neveikia, pereiti prie LLM tiekėjo B kaip atsarginio varianto.

**Vartotojo atsiliepimai:** Tiesioginiai vartotojų vertinimai suteikia vertingų įžvalgų. Tai gali apimti aiškius įvertinimus (👍thumbs-up/👎down, ⭐1–5 žvaigždutės) arba tekstinius komentarus. Nuolatiniai neigiami atsiliepimai turėtų įspėti, nes tai ženklas, kad agentas neveikia pagal lūkesčius.

**Netiesioginiai vartotojo atsiliepimai (Implicit User Feedback):** Vartotojų elgsena suteikia netiesioginį atsiliepimą net be aiškių įvertinimų. Tai gali apimti klausimų perrašymą iš karto, pasikartojančias užklausas arba spaudimą mygtuko „bando dar kartą“. Pvz., jeigu matote, kad vartotojai kartoja tą patį klausimą, tai ženklas, kad agentas neveikia kaip tikėtasi.

**Tikslumas (Accuracy):** Kaip dažnai agentas generuoja teisingus arba pageidaujamus rezultatus? Tikslumo apibrėžimai skiriasi (pvz., užduoties sprendimo teisingumas, informacijos gavimo tikslumas, vartotojo pasitenkinimas). Pirmas žingsnis yra apibrėžti, ką jūsų agentui reiškia sėkmė. Tikslumą galite stebėti per automatinius patikrinimus, vertinimo balus arba užduoties atlikimo žymes. Pavyzdžiui, pažymint traces kaip „succeeded“ arba „failed“.

**Automatinio vertinimo metrikos:** Taip pat galite nustatyti automatinius vertinimus. Pavyzdžiui, galite naudoti LLM, kad įvertintumėte agento išvestį pagal naudingumą, tikslumą ar panašiai. Yra keletas atviro kodo bibliotekų, kurios padeda įvertinti skirtingus agento aspektus. Pvz., [RAGAS](https://docs.ragas.io/) RAG agentams arba [LLM Guard](https://llm-guard.com/) kenksmingos kalbos ar promptų injekcijos aptikimui.

Praktikoje šių metrikų derinys suteikia geriausią DI agento sveikatos aprėptį. Šio skyriaus [pavyzdiniame užrašų knygoje](./code_samples/10-expense_claim-demo.ipynb) parodysime, kaip šios metrikos atrodo realiuose pavyzdžiuose, tačiau pirmiausia sužinosime, kaip atrodo tipinis vertinimo darbo eigos procesas.

## Instrumentuokite savo agentą

Norint surinkti tracing duomenis, reikės instrumentuoti jūsų kodą. Tikslas – instrumentuoti agento kodą taip, kad jis išmestų traces ir metrikas, kurias galėtų fiksuoti, apdoroti ir vizualizuoti stebėjimo platforma.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) išsivystė kaip pramonės standartas LLM matomumui. Jis suteikia API, SDK ir įrankius telemetrijos duomenų generavimui, rinkimui ir eksportavimui.

Yra daug instrumentavimo bibliotekų, kurios apgaubia esamus agentų framework’us ir palengvina OpenTelemetry span’ų eksportavimą į stebėjimo įrankį. Microsoft Agent Framework natūraliai integruojasi su OpenTelemetry. Žemiau pateikiamas pavyzdys, kaip instrumentuoti MAF agentą:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agento vykdymas automatiškai sekamas.
    pass
```

Šio skyriaus [pavyzdiniame užrašų knygoje](./code_samples/10-expense_claim-demo.ipynb) bus parodyta, kaip instrumentuoti savo MAF agentą.

**Rankinis Span’ų kūrimas:** Nors instrumentavimo bibliotekos suteikia gerą pradinį lygį, dažnai reikia detalesnės arba pritaikytos informacijos. Galite rankiniu būdu kurti spans, kad pridėtumėte pasirinktą programos logiką. Dar svarbiau, galite praturtinti automatiškai arba rankiniu būdu sukurtus spans pasirinktinėmis atributikomis (dar žinomomis kaip žymos arba metaduomenys). Šie atributai gali apimti verslui specifinius duomenis, tarpiniai skaičiavimai ar bet koks kontekstas, kuris gali būti naudingas derinimui ar analizei, pvz., `user_id`, `session_id` arba `model_version`.

Pavyzdys, kaip rankiniu būdu sukurti traces ir spans naudojant [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentų vertinimas

Matomumas suteikia mums metrikas, tačiau vertinimas yra procesas, kuriuo analizuojami tie duomenys (ir atliekami testai), siekiant nustatyti, kaip gerai DI agentas veikia ir kaip jį galima pagerinti. Kitaip tariant, turėdami traces ir metrikas, kaip jas panaudoti agento įvertinimui ir sprendimų priėmimui?

Reguliarus vertinimas yra svarbus, nes DI agentai dažnai yra nedeterministiniai ir gali keistis (per atnaujinimus arba modelio elgsenos nuokrypius) – be vertinimo negalėtumėte žinoti, ar jūsų „išmanusis agentas“ iš tikrųjų gerai atlieka savo darbą, ar įvyko regresija.

Yra dvi agentų vertinimo kategorijos: **online vertinimas** ir **offline vertinimas**. Abu yra naudingi ir papildo vienas kitą. Paprastai pradedame nuo offline vertinimo, nes tai yra minimalus būtinas žingsnis prieš diegiant bet kokį agentą.

### Offline vertinimas

![Duomenų rinkinio elementai Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tai reiškia agento vertinimą kontroliuojamoje aplinkoje, paprastai naudojant testinius duomenų rinkinius, o ne tiesiogines vartotojų užklausas. Naudojate kuruotus duomenų rinkinius, kuriuose žinote, koks yra tikėtinasis rezultatas arba teisinga elgsena, ir tada paleidžiate agentą su tais duomenimis.

Pavyzdžiui, jei sukūrėte matematikos žodinių uždavinių agentą, galite turėti [testinį duomenų rinkinį](https://huggingface.co/datasets/gsm8k) su 100 uždavinių ir žinomais atsakymais. Offline vertinimas dažnai atliekamas kūrimo metu (ir gali būti CI/CD vamzdžio dalis), siekiant patikrinti patobulinimus ar apsaugoti nuo regresijų. Privalumas yra tas, kad tai yra **pakartojama ir galite gauti aiškias tikslumo metrikas, nes turite realią teisybę**. Taip pat galite simuliuoti vartotojų užklausas ir palyginti agento atsakymus su idealiais atsakymais arba naudoti automatines metrikas, aprašytas aukščiau.

Pagrindinis iššūkis su offline vertinimu yra užtikrinti, kad jūsų testų duomenų rinkinys būtų išsamus ir išliktų aktualus – agentas gali gerai pasirodyti fiksuotame testų rinkinyje, bet gamyboje susidurti su visiškai kitokio pobūdžio užklausomis. Todėl turėtumėte atnaujinti testų rinkinius naujais ribiniais atvejais ir pavyzdžiais, atspindinčiais realius scenarijus​. Naudinga turėti ir nedidelius „smoke test“ rinkinius greitiems patikrinimams, ir didesnius rinkinius platesnėms našumo metrikoms​.

### Online vertinimas

![Matomumo metrikų apžvalga](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tai reiškia agento vertinimą gyvoje, realioje aplinkoje, t. y. per faktinį naudojimą gamyboje. Online vertinimas apima agento veikimo stebėjimą realių vartotojų sąveikų metu ir rezultatų nuolatinę analizę.

Pavyzdžiui, galite sekti sėkmės rodiklius, vartotojų pasitenkinimo balus arba kitus metrikus realiame sraute. Online vertinimo privalumas yra tas, kad jis **fiksuoja dalykus, kurių galite neįvardyti laboratorinėje aplinkoje** – galite stebėti modelio nuokrypį laikui bėgant (jei agento veiksmingumas pablogėja keičiantis įvesties modeliams) ir užfiksuoti netikėtas užklausas ar situacijas, kurių nebuvo jūsų testų duomenyse​. Tai suteikia tikrą vaizdą, kaip agentas elgiasi realiame pasaulyje.

Online vertinimas dažnai apima netiesioginių ir tiesioginių vartotojų atsiliepimų rinkimą, kaip buvo aptarta, ir gali apimti shadow testus arba A/B testus (kai nauja agento versija veikia lygiagrečiai, kad palygintumėte su sena). Iššūkis yra tai, kad gali būti sudėtinga gauti patikimas etiketes ar balus už gyvas sąveikas – gali tekti remtis vartotojų atsiliepimais arba žemynine analitika (pvz., ar vartotojas paspaudė rezultatą).

### Šių dviejų derinimas

Online ir offline vertinimai nėra vienas kitam prieštaraujantys; jie yra labai papildantys. Online stebėjimo įžvalgos (pvz., nauji vartotojų užklausų tipai, kuriuose agentas pasirodo blogai) gali būti naudojamos offline testų rinkinių papildymui ir patobulinimui. Atvirkščiai, agentai, kurie gerai pasirodo offline testuose, gali būti su didesne pasitikėjimo nuostata diegiami ir stebimi online.

Iš tiesų daugelis komandų priima ciklą:

_ivertinti offline -> diegti -> stebėti online -> surinkti naujus klaidų atvejus -> pridėti prie offline rinkinio -> tobulinti agentą -> kartoti_.

## Dažnos problemos

Diegiant DI agentus į gamybą galite susidurti su įvairiais iššūkiais. Čia pateikiamos dažnos problemos ir galimi sprendimai:

| **Problema**    | **Galimas sprendimas**   |
| ------------- | ------------------ |
| DI agentas neatlieka užduočių nuosekliai | - Patikslinkite agentui duodamą prompt’ą; aiškiai apibrėžkite tikslus.<br>- Nustatykite, kur padalijus užduotį į potaskas ir paskyrus ją keliems agentams tai gali padėti. |
| DI agentas pakliūna į nuolatines kilpas  | - Užtikrinkite aiškias termino pabaigos sąlygas, kad agentas žinotų, kada nutraukti procesą.<br>- Sudėtingoms užduotims, reikalaujančioms samprotavimo ir planavimo, naudokite didesnį, šiems uždaviniams specializuotą modelį. |
| DI agento įrankių iškvietimai neveikia gerai   | - Išbandykite ir patvirtinkite įrankio išvestį už agento sistemos ribų.<br>- Patikslinkite parametrus, prompt’us ir įrankių pavadinimus.  |
| Daugiaagentė sistema neveikia nuosekliai | - Patikslinkite kiekvienam agentui duodamus prompt’us, kad jie būtų konkretūs ir tarpusavyje skirtingi.<br>- Sukurkite hierarchinę sistemą, naudodami „maršrutizavimo“ arba valdymo agentą, kuris nuspręstų, kuris agentas yra tinkamiausias. |

Daugelį šių problemų galima efektyviau identifikuoti turint įdiegtą matomumą. Anksčiau aptartos traces ir metrikos padeda tiksliai nustatyti, kurioje agento darbo eigoje kyla problemos, todėl derinimas ir optimizavimas tampa daug veiksmingesni.

## Kaštų valdymas
Štai keletas strategijų, kaip valdyti kaštus diegiant DI agentus į gamybą:

**Using Smaller Models:** Maži kalbos modeliai (SLM) gali gerai veiktį tam tikruose agentiniuose naudojimo atvejuose ir reikšmingai sumažinti kaštus. Kaip minėta anksčiau, sukurti vertinimo sistemą, kad nustatytumėte ir palygintumėte našumą su didesniais modeliais, yra geriausias būdas suprasti, kaip gerai SLM veiks jūsų naudojimo atveju. Apsvarstykite SLM naudojimą paprastesnėms užduotims, tokioms kaip intencijų klasifikavimas arba parametrų išgavimas, o sudėtingam samprotavimui rezervuokite didesnius modelius.

**Using a Router Model:** Panaši strategija yra naudoti įvairius modelius ir dydžius. Galite naudoti LLM/SLM arba serverless funkciją užklausoms nukreipti pagal sudėtingumą į geriausiai tinkamus modelius. Tai taip pat padės sumažinti kaštus ir užtikrinti našumą tinkamoms užduotims. Pavyzdžiui, nukreipkite paprastas užklausas į mažesnius, greitesnius modelius ir naudokite brangius didelius modelius tik sudėtingoms samprotavimo užduotims.

**Caching Responses:** Identifikuodami dažnas užklausas ir užduotis bei pateikdami atsakymus prieš jiems pereinant per jūsų agentinę sistemą, galite sumažinti panašių užklausų kiekį. Netgi galite įdiegti procesą, naudojant paprastesnius DI modelius, kad nustatytumėte, kiek užklausa panaši į jūsų talpykloje saugomas užklausas. Ši strategija gali reikšmingai sumažinti išlaidas dažnai užduodamiems klausimams arba įprastoms darbo eigoms.

## Pažiūrėkime, kaip tai veikia praktikoje

Šio skyriaus [pavyzdiniame užrašų knygelės faile](./code_samples/10-expense_claim-demo.ipynb) pamatysime pavyzdžių, kaip galime naudoti stebėjimo (observability) įrankius mūsų agentui prižiūrėti ir vertinti.


### Ar turite daugiau klausimų apie DI agentus gamyboje?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiaisiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo DI agentų klausimus.

## Ankstesnė pamoka

[Metakognicijos dizaino modelis](../09-metacognition/README.md)

## Kita pamoka

[Agentiniai protokolai](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojama kreiptis į profesionalų vertėją. Mes neatsakome už jokius nesusipratimus ar klaidingas interpretacijas, kilusias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->