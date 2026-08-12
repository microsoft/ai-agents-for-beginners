# Dirbtinio intelekto agentai gamyboje: stebėjimas ir vertinimas

[![Dirbtinio intelekto agentai gamyboje](../../../translated_images/lt/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kai dirbtinio intelekto agentai pereina nuo eksperimentinių prototipų prie realių pasaulio taikymų, būtina suprasti jų elgesį, stebėti jų veikimą ir sistemingai vertinti jų rezultatus.

## Mokymosi tikslai

Baigę šią pamoką, jūs sužinosite kaip / suprasite:
- Pagrindines agentų stebėjimo ir vertinimo sąvokas
- Technikas agentų našumui, kaštams ir efektyvumui gerinti
- Kaip sistemingai vertinti savo dirbtinio intelekto agentus
- Kaip valdyti kaštus diegiant dirbtinio intelekto agentus gamyboje
- Kaip instrumentuoti agentus, sukurtus naudojant Microsoft Agent Framework

Tikslas – suteikti jums žinių, kad savo „juodosios dėžės“ agentus paverstumėte skaidriomis, valdomomis ir patikimomis sistemomis.

_**Pastaba:** Svarbu diegti saugius ir patikimus dirbtinio intelekto agentus. Taip pat peržiūrėkite pamoką [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Sekos ir apimtys

Stebėjimo įrankiai, tokie kaip [Langfuse](https://langfuse.com/) arba [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), dažniausiai vaizduoja agento paleidimus kaip sekas ir apimtis.

- **Sekos** atspindi visą agento užduotį nuo pradžios iki pabaigos (pvz., vartotojo užklausos apdorojimą).
- **Apimtys** yra atskiri sekos žingsniai (pvz., kalbos modelio kvietimas ar duomenų gavimas).

![Sekos medis Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Be stebėjimo dirbtinio intelekto agentas gali jaustis kaip „juodoji dėžė“ – jo vidinė būsena ir argumentacija yra neaiškios, todėl sunku diagnozuoti problemas ar optimizuoti veikimą. Turint stebėjimą agentai tampa „stiklinėmis dėžėmis“, kurios siūlo skaidrumą, būtina pasitikėjimui kurti ir užtikrinti, kad jie veikia numatytu būdu.

## Kodėl stebėjimas yra svarbus gamybos aplinkoje

Pereinant dirbtinio intelekto agentams į gamybos aplinką atsiranda naujų iššūkių ir reikalavimų. Stebėjimas nėra tik „gražus priedas“, o kritinė funkcija:

*   **Klaidų taisymas ir pagrindinės priežasties analizė**: kai agentas nepavyksta arba pateikia netikėtą rezultatą, stebėjimo įrankiai suteikia sekas, reikalingas klaidos šaltiniui nustatyti. Tai ypač svarbu sudėtinguose agentuose, kuriuose gali būti keli LLM kvietimai, įrankių sąveikos ir sąlyginė logika.
*   **Vėlinimo ir kaštų valdymas**: dirbtinio intelekto agentai dažnai naudoja LLM ir kitas išorines API, kurios apmokestinamos už žodį ar kvietimą. Stebėjimas leidžia tiksliai sekti šiuos kvietimus, padedant nustatyti operacijas, kurios yra pernelyg lėtos arba brangios. Tai leidžia komandai optimizuoti užklausas, pasirinkti efektyvesnius modelius arba pertvarkyti darbo eigas, kad valdyti operacines išlaidas ir užtikrinti gerą vartotojo patirtį.
*   **Pasitikėjimas, saugumas ir atitiktis**: daugelyje taikymų svarbu užtikrinti, kad agentai elgtųsi saugiai ir etiškai. Stebėjimas suteikia agentų veiksmų ir sprendimų audito įrašą. Tai gali būti naudojama atpažinti ir pašalinti problemas, tokias kaip užklausų inžinerija, žalingo turinio generavimas ar netinkamas asmeninės informacijos tvarkymas. Pavyzdžiui, galite peržiūrėti sekas, kad suprastumėte, kodėl agentas pateikė tam tikrą atsakymą arba panaudojo konkretų įrankį.
*   **Nuolatinio tobulinimo ciklai**: stebėjimo duomenys yra iteratyvaus kūrimo proceso pagrindas. Stebėdami agentų veikimą realiame pasaulyje, komandos gali nustatyti tobulinimo sritis, rinkti duomenis modelių tobulinimui ir patvirtinti pakeitimų poveikį. Tai sukuria grįžtamojo ryšio ciklą, kuriame gamybos įžvalgos iš online vertinimo informuoja offline eksperimentavimą ir tobulinimą, vedantį prie vis geresnio agento veikimo.

## Svarbiausi metrikų rodikliai

Norint stebėti ir suprasti agento elgesį, reikia sekti įvairias metrikas ir signalus. Nors konkretūs rodikliai gali skirtis priklausomai nuo agento paskirties, kai kurie yra universaliai svarbūs.

Čia pateikiami kai kurie dažniausiai stebimi metrikų pavyzdžiai:

**Vėlinimas:** Kaip greitai agentas reaguoja? Ilgi laukimo laikai neigiamai veikia vartotojo patirtį. Reikėtų matuoti vėlinimą užduotims ir atskiriems žingsniams sekant agento paleidimus. Pavyzdžiui, agentą, kuris visiems modeliavimo kvietimams skiria 20 sekundžių, galima paspartinti naudojant greitesnį modelį arba vykdant kvietimus lygiagrečiai.

**Kaštai:** Kokia bėgimo kaina vienam agento paleidimui? Dirbtinio intelekto agentai remiasi LLM kvietimais, kurie apmokestinami už žodį, arba išorinėmis API. Dažnas įrankių naudojimas ar keli užklausos kartojimai gali greitai padidinti kaštus. Pavyzdžiui, jei agentas penkis kartus kviečia LLM, kad nežymiai pagerintų kokybę, būtina įvertinti, ar kaštai yra pateisinami arba ar galima sumažinti kvietimų skaičių arba naudoti pigesnį modelį. Realaus laiko stebėjimas taip pat gali padėti atpažinti netikėtus šuolius (pvz., klaidas, sukylančias per daug API kvietimų ciklų).

**Užklausų klaidos:** Kiek užklausų agentas neįvykdė? Tai gali būti API klaidos arba nepavykę įrankių kvietimai. Kad agentas taptų atsparesnis tokiems atvejams gamyboje, galite nustatyti atsarginį variantą arba pakartojimus, pvz., jei LLM tiekėjas A neveikia, pereiti prie LLM tiekėjo B kaip atsarginio.

**Vartotojo atsiliepimai:** Tiesioginių vartotojo vertinimų įdiegimas teikia vertingas įžvalgas. Tai gali būti aiškūs įvertinimai (👍patinka/👎nepatinka, ⭐1-5 žvaigždutės) arba tekstiniai komentarai. Nuolatiniai neigiami atsiliepimai turi įspėti, nes tai ženklas, kad agentas neveikia kaip tikėtasi.

**Netiesioginiai vartotojo atsiliepimai:** Vartotojo elgesys suteikia netiesioginį atsiliepimą, net jei nėra aiškių įvertinimų. Tai gali būti greitas klausimo pertvarkymas, pasikartojančios užklausos arba mygtuko „bandyti dar kartą“ paspaudimai. Pavyzdžiui, jei matote, kad vartotojai kartoja tą patį klausimą, tai rodo, kad agentas neveikia tinkamai.

**Tikslumas:** Kaip dažnai agentas pateikia teisingus ar pageidaujamus rezultatus? Tikslumo apibrėžimai skiriasi (pvz., problemų sprendimo teisingumas, informacijos gavimo tikslumas, vartotojo pasitenkinimas). Pirmas žingsnis – apibrėžti, ką reiškia sėkmė jūsų agentui. Tikslumą galite stebėti automatizuotų patikrų, vertinimo rezultatų ar užduočių įvykdymo žymių būdu. Pavyzdžiui, žymint sekas kaip „pavyko“ arba „nepavyko“.

**Automatizuotos vertinimo metrikos:** Taip pat galite nustatyti automatinius vertinimus. Pavyzdžiui, naudoti LLM agento rezultatui įvertinti, ar jis naudingas, tikslus ar ne. Yra keletas atvirojo kodo bibliotekų, kurios padeda įvertinti skirtingus agento aspektus, pvz., [RAGAS](https://docs.ragas.io/) RAG agentams arba [LLM Guard](https://llm-guard.com/), skirtą aptikti žalingą kalbą ar užklausų injekcijas.

Praktikoje šių metrikų derinys suteikia geriausią dirbtinio intelekto agento būklės apžvalgą. Šio skyriaus [pavyzdinėje užrašų knygelėje](./code_samples/10-expense_claim-demo.ipynb) parodysime, kaip šios metrikos atrodo realiuose pavyzdžiuose, tačiau pirmiausia išmoksime, kaip atrodo tipinis vertinimo darbo procesas.

## Instrumentuokite savo agentą

Kad surinktumėte sekimo duomenis, turėsite instrumentuoti savo kodą. Tikslas – instrumentuoti agento kodą taip, kad jis transliuotų sekas ir metrikas, kurias galėtų fiksuoti, apdoroti ir vizualizuoti stebėjimo platforma.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) tapo pramonės standartu LLM stebėjimui. Jis suteikia API, SDK ir įrankių rinkinį telemetrijos duomenų generavimui, kaupimui ir eksportui.

Yra daug instrumentavimo bibliotekų, kurios supakuoja esamus agentų karkasus ir palengvina OpenTelemetry apimčių eksportą į stebėjimo įrankį. Microsoft Agent Framework natūraliai integruojasi su OpenTelemetry. Žemiau pateiktas pavyzdys apie MAF agento instrumentaciją:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentas vykdomas automatiškai ir yra fiksuojamas
    pass
```

Šio skyriaus [pavyzdinė užrašų knygelė](./code_samples/10-expense_claim-demo.ipynb) parodys, kaip instrumentuoti savo MAF agentą.

**Rankinis apimčių kūrimas:** nors instrumentavimo bibliotekos suteikia gerą pagrindą, dažnai reikalinga detalesnė ar pasirinktinė informacija. Galite rankiniu būdu kurti apimtis, kad pridėtumėte pasirinktą programos logiką. Svarbiausia, kad galima papildyti automatiškai arba rankiniu būdu sukurtas apimtis pasirinktiniais atributais (dar vadinamais žymomis arba meta duomenimis). Šie atributai gali apimti verslo specifinius duomenis, tarpinį skaičiavimą arba bet kokį kontekstą, naudingą derinimui ar analizei, pvz., `user_id`, `session_id` ar `model_version`.

Pavyzdys, kaip rankiniu būdu kurti sekas ir apimtis naudojant [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentų vertinimas

Stebėjimas suteikia metrikas, bet vertinimas yra procesas, kurio metu analizuojame tuos duomenis (ir atliekame testus), kad nustatytume, kaip gerai veikia dirbtinio intelekto agentas ir kaip jį galima patobulinti. Kitaip tariant, kai turite sekas ir metrikas, kaip jas naudoti, kad įvertintumėte agentą ir priimtumėte sprendimus?

Reguliarus vertinimas yra svarbus, nes dirbtinio intelekto agentai dažnai būna nedeterministiniai ir gali vystytis (per atnaujinimus ar modelio elgesio pokyčius) – be vertinimo nežinotumėte, ar jūsų „išmanusis agentas“ iš tiesų gerai atlieka savo darbą arba jei jis sugedo.

Yra dvi ekspertų agentų vertinimo kategorijos: **online vertinimas** ir **offline vertinimas**. Abu yra vertingi ir papildomi. Dažniausiai pradedame nuo offline vertinimo, nes tai yra minimalus būtinas žingsnis prieš bet kokį agento diegimą.

### Offline vertinimas

![Duomenų rinkinys Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tai reiškia agento vertinimą kontroliuojamoje aplinkoje, paprastai naudojant testinius duomenų rinkinius, o ne tiesiogines vartotojų užklausas. Jūs naudojate atrinktus duomenų rinkinius, kur žinote, koks yra numatomas rezultatas ar teisingas elgesys, ir tuomet paleidžiate agentą su jais.

Pavyzdžiui, jei sukūrėte matematikos žodinių uždavinių agentą, galite turėti [testinį duomenų rinkinį](https://huggingface.co/datasets/gsm8k) su 100 problemų ir žinomais atsakymais. Offline vertinimas dažnai atliekamas vystymo metu (ir gali būti CI/CD procesuose), norint patikrinti patobulinimus arba apsaugoti nuo regresijos. Privalumas yra tas, kad tai **pavyzdinga ir jūs galite gauti aiškius tikslumo rodiklius, nes turite realius atsakymus**. Taip pat galite simuliuoti vartotojų užklausas ir matuoti agento atsakymus, palyginant su idealiais atsakymais, arba naudoti automatizuotas metrikas, kaip aprašyta anksčiau.

Pagrindinė offline vertinimo problema yra užtikrinti, kad jūsų testinis duomenų rinkinys būtų išsamus ir reikalingas – agentas gali gerai veikti fiksuotame rinkinyje, tačiau gamyboje susidurti su labai skirtingomis užklausomis. Todėl turėtumėte reguliariai atnaujinti testinius rinkinius naujais kraštutiniais atvejais ir pavyzdžiais, atspindinčiais realius scenarijus. Naudinga naudoti mažus „smoke test“ atvejus greitam patikrinimui ir didesnius vertinimo rinkinius platesnėms metrikoms.

### Online vertinimas

![Stebėjimo metrikų apžvalga](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tai reiškia agento vertinimą gyvoje, realioje aplinkoje, t. y. tikroje gamybos aplinkoje naudojant. Online vertinimas reiškia agento veikimo stebėjimą tikrose vartotojų sąveikose ir nuolatinę rezultatų analizę.

Pavyzdžiui, galite stebėti sėkmės rodiklius, vartotojų pasitenkinimo balus ar kitas metrikas gyvame sraute. Online vertinimo pranašumas yra tas, kad jis **fiksuoja dalykus, kurių galbūt nepastebėtumėte laboratorijoje** – galite stebėti modelio pakitimą laikui bėgant (jei agento efektyvumas blogėja, kai keičiami įvesties modeliai) ir užfiksuoti netikėtas užklausas ar situacijas, kurios nebuvo testų duomenyse. Tai suteikia tikrą vaizdą, kaip agentas veikia realiame pasaulyje.

Online vertinimas dažnai apima netiesioginių ir tiesioginių vartotojų atsiliepimų rinkimą, kaip aprašyta, ir galbūt šešėlinių testų arba A/B testų vykdymą (kur naujoji agento versija veikia šalia senojo palyginimo). Iššūkis yra tai gauti patikimus žymėjimus ar balus gyvoms sąveikoms – gali tekti remtis vartotojų atsiliepimais arba posistemiais rodikliais (pvz., ar vartotojas paspaudė rezultatą).

### Abiejų derinimas

Online ir offline vertinimai nėra vienas kitam prieštaraujantys; jie yra labai papildantys. Įžvalgos iš online stebėjimo (pvz., naujų vartotojų užklausų tipai, kuriuose agentas veikia blogai) gali būti naudojamos offline testų duomenų rinkinių papildymui ir gerinimui. Atvirkščiai, agentai, kurie gerai veikia offline testuose, gali būti užtikrintai diegiami ir stebimi online režimu.

Iš tiesų, daugelis komandų naudoja ciklą:

_vertinti offline -> diegti -> stebėti online -> rinkti naujas nepavykusias atvejus -> pridėti į offline duomenų rinkinį -> tobulinti agentą -> kartoti_.

## Dažnos problemos

Diegiant dirbtinio intelekto agentus gamyboje galite susidurti su įvairiais iššūkiais. Štai keletas dažnų problemų ir galimi sprendimai:

| **Problema**    | **Galimas sprendimas**   |
| ------------- | ------------------ |
| Dirbtinio intelekto agentas nesukuria užduočių nuosekliai | - Patikslinkite agentui skirtus užklausimus; aiškiai apibrėžkite tikslus.<br>- Nustatykite, kur užduotis galima suskirstyti į dalines užduotis ir jas vykdyti keliems agentams. |
| Dirbtinio intelekto agentas įstringa nuolatiniuose cikluose  | - Užtikrinkite aiškias pabaigos sąlygas, kad agentas žinotų, kada sustabdyti procesą.<br>- Sudėtingoms užduotims, reikalaujančioms argumentavimo ir planavimo, naudokite didesnį modelį, sukurtą būtent tokioms užduotims. |
| Dirbtinio intelekto agento įrankių kvietimai neveikia gerai   | - Išbandykite ir patvirtinkite įrankių išvestis už agento sistemos ribų.<br>- Patikslinkite parametrus, užklausimus ir įrankių pavadinimus.  |
| Daugiagentinė sistema neveikia nuosekliai | - Patikslinkite užklausimus, skiriamus kiekvienam agentui, kad jie būtų aiškūs ir skirtingi.<br>- Sukurkite hierarchinę sistemą su „maršruto“ arba valdymo agentu, kuris nuspręstų, kuris agentas yra tinkamiausias. |

Daugelį šių problemų galima nustatyti efektyviau įdiegus stebėjimą. Anksčiau minėtos sekos ir metrikos padeda tiksliai nustatyti, kur agente vykstančioje darbo eigoje kyla problemos, todėl klaidų taisymas ir optimizavimas tampa daug efektyvesni.

## Kaštų valdymas


Štai keletas strategijų, kaip valdyti dirbtinio intelekto agentų diegimo į gamybą sąnaudas:

**Naudojant mažesnius modelius:** Maži kalbos modeliai (SLM) gali gerai veikti tam tikruose agenturos atvejais ir reikšmingai sumažins sąnaudas. Kaip minėta anksčiau, geriausias būdas suprasti, kaip gerai SLM veiks jūsų atveju – tai sukurti vertinimo sistemą, kuri nustatytų ir palygintų našumą su didesniais modeliais. Apsvarstykite galimybę naudoti SLM paprastesnėms užduotims, tokioms kaip ketinimų klasifikavimas arba parametrų išgavimas, o sudėtingam samprotavimui rezervuokite didesnius modelius.

**Naudojant maršrutizatoriaus modelį:** Panaši strategija yra naudoti įvairius modelius ir dydžius. Galite naudoti LLM/SLM arba serverless funkciją, kad maršrutizuotumėte užklausas pagal sudėtingumą į geriausiai tinkamus modelius. Tai taip pat padės sumažinti sąnaudas ir užtikrins našumą tinkamoms užduotims. Pavyzdžiui, maršrutizuokite paprastas užklausas į mažesnius, greitesnius modelius, o brangius didelius modelius naudokite tik sudėtingiems samprotavimo uždaviniams.

**Atsakymų kešavimas:** Nustatyti dažnas užklausas ir užduotis bei pateikti atsakymus prieš jie pasiekia jūsų agentūros sistemą yra geras būdas sumažinti panašių užklausų apimtį. Galite net įgyvendinti srautą, nustatantį, kiek užklausa panaši į jūsų kešuotas užklausas, naudojant paprastesnius DI modelius. Ši strategija gali reikšmingai sumažinti sąnaudas dažnai užduodamiems klausimams arba įprastiems darbo eigų procesams.

## Pažiūrėkime, kaip tai veikia praktikoje

[Šio skyriaus pavyzdiniame užrašyne](./code_samples/10-expense_claim-demo.ipynb) pamatysime pavyzdžių, kaip galime naudoti stebėjimo įrankius mūsų agentui stebėti ir vertinti.


### Turite daugiau klausimų apie DI agentus gamyboje?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susipažinkite su kitais besimokančiais, dalyvaukite konsultačiuose ir gaukite atsakymus į savo DI agentų klausimus.

## Ankstesnė pamoka

[Metakognicijos dizaino šablonas](../09-metacognition/README.md)

## Kitoji pamoka

[Agentūros protokolai](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->