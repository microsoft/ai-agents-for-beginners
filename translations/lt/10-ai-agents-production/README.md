# Dirbtinio intelekto agentai produkcijoje: stebėjimas ir vertinimas

[![Dirbtinio intelekto agentai produkcijoje](../../../translated_images/lt/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kai DI agentai pereina nuo eksperimentinių prototipų prie realių taikymų, svarbu suprasti jų elgseną, stebėti jų veikimą ir sistemingai vertinti jų rezultatus.

## Mokymosi tikslai

Baigę šią pamoką, žinosite/įsisavinsite:
- Pagrindines agentų stebėjimo ir vertinimo sąvokas
- Metodas agentų veikimui, sąnaudoms ir efektyvumui gerinti
- Kaip sistemingai vertinti savo DI agentus
- Kaip kontroliuoti sąnaudas diegiant DI agentus produkcijoje
- Kaip instrumentuoti agentus, sukurtus naudojant Microsoft Agent Framework

Tikslas – suteikti jums žinių, kaip paversti savo „juodosios dėžės“ agentus skaidriomis, valdomomis ir patikimomis sistemomis.

_**Pastaba:** labai svarbu diegti saugius ir patikimus DI agentus. Peržiūrėkite ir pamoką [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Sekos ir segmentai

Stebėjimo įrankiai, tokie kaip [Langfuse](https://langfuse.com/) arba [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), dažniausiai agentų veikimą vaizduoja kaip sekas ir segmentus.

- **Seka** atspindi pilną agento užduotį nuo pradžios iki pabaigos (pvz., vartotojo užklausos apdorojimą).
- **Segmentai** yra atskiri žingsniai sekoje (pvz., kalbos modelio iškvietimas arba duomenų gavimas).

![Sekos medis Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Be stebėjimo, DI agentas gali jaustis kaip „juodoji dėžė“ – jo vidinė būsena ir sprendimai yra neaiškūs, todėl sunku diagnozuoti problemas ar optimizuoti veikimą. Su stebėjimu agentai tampa „stiklinėmis dėžėmis“, teikiančiomis skaidrumą, kuris yra būtinas pasitikėjimui kurti ir užtikrinti tinkamą veikimą.

## Kodėl stebėjimas svarbus produkcijos aplinkose

Perkėlimas DI agentų į produkcijos aplinką atneša naujų iššūkių ir reikalavimų. Stebėjimas nebėra „pageidautina“ funkcija, o kritinė galimybė:

*   **Klaidų nuodugnioji analizė ir šakninių priežasčių nustatymas**: kai agentas nepavyksta arba pateikia netikėtą rezultatą, stebėjimo įrankiai suteikia sekas, leidžiančias tiksliai nustatyti klaidos šaltinį. Tai ypač svarbu sudėtinguose agentuose, kuriuose gali būti daug LLM iškvietimų, įrankių bei sąlyginių logikos elementų.
*   **Vėlavimų ir sąnaudų valdymas**: DI agentai dažnai naudoja LLM ir kitus išorinius API, kurie apmokestinami už simbolį arba iškvietimą. Stebėjimas leidžia tiksliai sekti šiuos iškvietimus, padedant identifikuoti per lėtus arba brangius veiksmus. Tai suteikia galimybę optimizuoti užklausas, pasirinkti efektyvesnius modelius arba pertvarkyti darbo eigas siekiant suvaldyti sąnaudas ir užtikrinti gerą vartotojo patirtį.
*   **Pasitikėjimas, saugumas ir atitiktis**: daugelyje taikymų svarbu užtikrinti, kad agentai veiktų saugiai ir etiškai. Stebėjimas suteikia agento veiksmų ir sprendimų auditavimo seką. Tai gali padėti aptikti ir sumažinti problemas, tokias kaip užklausų injekcija, žalingo turinio generavimas ar asmens identifikavimo duomenų netinkamas tvarkymas. Pavyzdžiui, galima peržiūrėti sekas, kad suprastumėte, kodėl agentas pateikė tam tikrą atsakymą ar naudojo konkretų įrankį.
*   **Nuolatinis tobulinimas**: stebėjimo duomenys yra pagrindas iteraciniam vystymosi procesui. Stebėdami agentų veikimą realiame pasaulyje, komandos gali nustatyti tobulinimo sritis, rinkti duomenis modeliui tobulinti ir vertinti pokyčių poveikį. Tai sukuria atsiliepimų ciklą, kai produkcijos įžvalgos iš internetinio vertinimo informuoja neprisijungusio eksperimentavimo ir patobulinimų procesą, vedantį prie nuolat gerėjančių agentų rezultatų.

## Svarbūs rodikliai stebėti

Norint stebėti ir suprasti agento elgesį, reikėtų sekti įvairius rodiklius ir signalus. Nors konkretūs rodikliai gali skirtis priklausomai nuo agento paskirties, kai kurie yra universaliai svarbūs.

Štai kai kurie dažniausi rodikliai, kuriuos stebėjimo įrankiai fiksuoja:

**Vėlavimas:** Kaip greitai agentas atsako? Ilgų laukimo laikų vartotojo patirtis blogėja. Reikėtų matuoti vėlavimą užduotis ir atskirus žingsnius, sekant agento veikimą. Pavyzdžiui, jei agentui visi modelio iškvietimai užtrunka 20 sekundžių, galima paspartinti naudojant greitesnį modelį arba vykdant kvietimus lygiagrečiai.

**Sąnaudos:** Kokia kaina už vieną agento veikimą? DI agentai naudoja LLM iškvietimus, apmokestinamus už simbolį, arba išorinius API. Dažnas įrankių naudojimas ar daug užklausų gali greitai padidinti išlaidas. Pavyzdžiui, jei agentas penkis kartus iškviečia LLM siekdamas nedidelio kokybės pagerėjimo, turite įvertinti, ar kaina pateisinama, arba ar galima sumažinti iškvietimų skaičių ar naudoti pigesnį modelį. Realaus laiko stebėjimas taip pat padeda identifikuoti netikėtus šuolius (pvz., klaidas, sukeliančias per daug API ciklų).

**Užklausų klaidos:** Kiek agento užklausų nepavyko? Tai gali apimti API klaidas arba nepavykusius įrankių iškvietimus. Norint padaryti agentą atsparų tokiems atvejams produkcijoje, galima nustatyti atsarginius variantus ar bandymus pakartoti. Pvz., jei LLM tiekėjas A neveikia, pereinate prie tiekėjo B kaip atsarginio.

**Vartotojo atsiliepimai:** Tiesioginis vartotojų vertinimas suteikia vertingos informacijos. Tai gali būti aiškūs įvertinimai (👍patinka/👎nepatinka, ⭐1-5 žvaigždutės) arba tekstiniai komentarai. Nuolatiniai neigiami atsiliepimai turėtų įspėti, nes tai ženklas, kad agentas neveikia kaip tikėtasi.

**Netiesioginiai vartotojo atsiliepimai:** Vartotojų elgsena suteikia netiesioginių atsiliepimų net be aiškių įvertinimų. Tai gali būti vietinis klausimo perrašymas, pakartotinės užklausos ar mygtuko „bandyti dar kartą“ paspaudimas. Pvz., jei matote, kad vartotojai pakartotinai užduoda tą patį klausimą, tai yra ženklas, kad agentas neveikia kaip tikėtasi.

**Tikslumas:** Kaip dažnai agentas pateikia teisingus ar pageidaujamus rezultatus? Tikslumo apibrėžimai gali skirtis (pvz., teisingumas sprendžiant uždavinius, informacijos gavimo tikslumas, vartotojo pasitenkinimas). Pirmas žingsnis – apibrėžti, ką reiškia sėkmė jūsų agentui. Tikslumą galite sekti automatizuotais patikrinimais, vertinimo balais ar užduoties užbaigimo žymomis. Pavyzdžiui, pažymint sekas kaip „pavyko“ arba „nepavyko“.

**Automatizuoti vertinimo rodikliai:** Taip pat galite nustatyti automatinius vertinimus. Pvz., naudoti LLM agento rezultatui įvertinti, ar jis yra naudingas, tikslus ar ne. Yra keletas atvirojo kodo bibliotekų, kurios padeda vertinti skirtingus agento aspektus. Pvz., [RAGAS](https://docs.ragas.io/) RAG agentams arba [LLM Guard](https://llm-guard.com/) žalingos kalbos ar užklausų injekcijos aptikimui.

Praktikoje geriausią DI agento sveikatos apžvalgą suteikia šių rodiklių derinys. Šios pamokos [pavyzdiniame užrašų knygutėje](./code_samples/10-expense_claim-demo.ipynb) parodysime, kaip šie rodikliai atrodo realiuose pavyzdžiuose, bet pirmiausia išmokysime, kaip atrodo tipinis vertinimo darbo procesas.

## Instrumentuokite savo agentą

Norint rinkti sekimo duomenis, reikia instrumentuoti savo kodą. Tikslas – instrumentuoti agento kodą taip, kad jis generuotų sekas ir rodiklius, kuriuos galėtų fiksuoti, apdoroti ir vizualizuoti stebėjimo platforma.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) tapo pramonės standartu LLM stebėjimui. Jis siūlo API, SDK ir įrankių rinkinį telemetrijos duomenims generuoti, rinkti ir eksportuoti.

Yra daug instrumentavimo bibliotekų, kurios apgaubia esamus agentų pagrindus ir leidžia lengvai eksportuoti OpenTelemetry segmentus į stebėjimo įrankį. Microsoft Agent Framework natūraliai integruojasi su OpenTelemetry. Žemiau pateiktas pavyzdys, kaip instrumentuoti MAF agentą:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentų vykdymas stebimas automatiškai
    pass
```

Šiame skyriuje pateiktas [pavyzdinis užrašų knygutė](./code_samples/10-expense_claim-demo.ipynb) parodys, kaip instrumentuoti savo MAF agentą.

**Rankinis segmento kūrimas:** nors instrumentavimo bibliotekos suteikia gerą pagrindą, dažnai reikia detalesnės ar individualios informacijos. Galite rankiniu būdu kurti segmentus, kad pridėtumėte pasirinktą programos logiką. Dar svarbiau, galite praturtinti automatiškai arba rankiniu būdu sukurtus segmentus pasirinktinais atributais (dar vadinamais žymomis arba metaduomenimis). Šie atributai gali apimti verslo specifinius duomenis, tarpinį skaičiavimą ar bet kokį kontekstą, svarbų klaidų taisymui ar analizei, pvz., `user_id`, `session_id` ar `model_version`.

Pavyzdys, kaip rankiniu būdu kurti sekas ir segmentus naudojant [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentų vertinimas

Stebėjimas suteikia mums rodiklius, tačiau vertinimas yra procesas, kuriame analizuojami tie duomenys (ir atliekami testai), siekiant nustatyti, kaip gerai DI agentas veikia ir kaip jį pagerinti. Kitaip tariant, kai turite sekas ir rodiklius, kaip juos panaudoti agentui vertinti ir sprendimams priimti?

Reguliarus vertinimas yra svarbus, nes DI agentai dažnai yra nežymiai deterministiniai ir gali keistis (per atnaujinimus ar modelio elgsenos pasislinkimą) – be vertinimo negalėtumėte žinoti, ar jūsų „protingas agentas“ iš tiesų gerai atlieka savo darbą ar sukėlė regresiją.

Yra dvi agentų vertinimo kategorijos: **interneto vertinimas** ir **neinterneto vertinimas**. Abi yra vertingos ir viena kitą papildo. Dažniausiai pradedama nuo neinterneto vertinimo, nes tai minimalus būtinas žingsnis prieš diegiant bet kurį agentą.

### Neinternetinis vertinimas

![Duomenų rinkinys Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Tai reiškia agento vertinimą kontroliuojamoje aplinkoje, paprastai naudojant testinius duomenų rinkinius, o ne tiesiogines vartotojų užklausas. Naudojate kruopščiai parinktus duomenų rinkinius, kuriuose žinote laukiamą rezultatą ar teisingą elgesį, ir tada vykdote agentą šiuose rinkiniuose.

Pavyzdžiui, jei sukūrėte matematinių žodinių uždavinių agentą, galite turėti [testinį duomenų rinkinį](https://huggingface.co/datasets/gsm8k) su 100 užduočių, kurių atsakymai žinomi. Neinternetinis vertinimas dažnai atliekamas vystymosi metu (gali būti CI/CD pipeline'e), tikrinant patobulinimus ar saugant nuo regresijų. Privalumas yra tas, kad jis yra **pakartojamas ir galite gauti aiškius tikslumo rodiklius, nes turite tikrą bazę**. Taip pat galite simuliuoti vartotojų užklausas ir vertinti agento atsakymus pagal idealias atsakymų aibes ar naudoti automatinius rodiklius, kaip aprašyta anksčiau.

Pagrindinė problema su neinternetu vertinimu yra užtikrinti, kad jūsų testinis duomenų rinkinys yra išsamus ir išlieka aktualus – agentas gali gerai veikti fiksuotame rinkinyje, bet susidurti su visiškai kitokiais užklausimais produkcijoje. Todėl testinius rinkinius turėtumėte nuolat atnaujinti naujais ribiniais atvejais ir pavyzdžiais, atspindinčiais realius scenarijus. Naudinga turėti nedidelius „bakaus“ testų rinkinius greitiems patikrinimams ir didesnius vertinimo rinkinius platesniems veikimo rodikliams.

### Internetinis vertinimas

![Stebėjimo rodiklių apžvalga](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Tai reiškia agento vertinimą tiesioginėje, realiojo pasaulio aplinkoje, t.y. faktiniame naudojime produkcijoje. Internetinis vertinimas apima agento našumo stebėjimą realiuoju laiku atliekant tikras vartotojų sąveikas ir nuolatinę rezultatų analizę.

Pavyzdžiui, galite stebėti sėkmės rodiklius, vartotojų pasitenkinimo balus ar kitus rodiklius realioje sraute. Internetinio vertinimo privalumas yra tas, jog jis **fiksuoja dalykus, kurių laboratorijoje gali nepastebėti** – galite stebėti modelio elgsenos pasikeitimus laikui bėgant (jei agento efektyvumas mažėja, nes keičiasi įvesties modeliai) ir užfiksuoti netikėtas užklausas ar situacijas, kurių nebuvo testiniuose duomenyse. Tai pateikia tikrą agento elgesio vaizdą laukinėje aplinkoje.

Internetinis vertinimas dažnai apima ir netiesioginių bei tiesioginių vartotojų atsiliepimų rinkimą, kaip aptarta anksčiau, bei galbūt šešėlinio arba A/B testavimo vykdymą (kai nauja agento versija veikia lygiagrečiai senajai, lyginant rezultatus). Problema ta, kad gali būti sudėtinga gauti patikimus vertinius ar balus tiesioginėms sąveikoms – galite remtis vartotojų atsiliepimais arba tolimesniais rodikliais (pvz., ar vartotojas paspaudė rezultatą).

### Abiejų derinimas

Internetinis ir neinternetinis vertinimas nėra tarpusavyje prieštaraujantys; jie yra labai papildantys. Internetinio stebėjimo įžvalgos (pvz., nauji vartotojų užklausų tipai, kur agentas veikia prastai) gali būti naudojamos papildyti ir patobulinti neintelektinius testinius rinkinius. Atvirkščiai, agentai, geri neintelektiniuose testuose, gali būti labiau pasitikint diegiami ir stebimi internete.

Iš tiesų, dauguma komandų praktikose naudoja ciklą:

_vertinti neintelektiniu būdu -> diegti -> stebėti internete -> rinkti naujus klaidų atvejus -> pridėti į neintelektinį rinkinį -> tobulinti agentą -> kartoti_.

## Dažnos problemos

Diegiant DI agentus produkcijoje, galite susidurti su įvairiais iššūkiais. Štai keletas dažnų problemų ir jų galimų sprendimų:

| **Problema**    | **Galimas sprendimas**   |
| ------------- | ------------------ |
| DI agentas neatlieka užduočių nuosekliai | - Tobulinkite agentui pateiktą užklausą; aiškiai apibrėžkite tikslus.<br>- Nustatykite, kur užduotis galima suskaidyti į posritis ir patikėti kelis agentus. |
| DI agentas patenka į nuolatinius ciklus  | - Užtikrinkite aiškias proceso nutraukimo sąlygas, kad agentas žinotų, kada sustoti.<br>- Sudėtingoms užduotims, reikalaujančioms mąstymo ir planavimo, naudokite didesnį specializuotą modelį. |
| DI agentas blogai naudoja įrankių kvietimus   | - Testuokite ir patikrinkite įrankio rezultatus ne agento sistemoje.<br>- Tobulinkite apibrėžtus parametrus, užklausas ir įrankių pavadinimus.  |
| Multiagentinė sistema veikia prieštaringai | - Tobulinkite kiekvienam agentui skirtas užklausas, kad jos būtų aiškios ir skirtingos.<br>- Sukurkite hierarchinę sistemą su „maršruto“ arba valdymo agentu, kuris nustatytų, kuris agentas tinkamiausias. |

Daugelį šių problemų galima efektyviau nustatyti turint įgyvendintą stebėjimą. Anksčiau aptartos sekos ir rodikliai padeda tiksliai nustatyti, kur agentų darbo procese kyla problemos, kas žymiai palengvina klaidų taisymą ir optimizavimą.

## Sąnaudų valdymas


Štai keletas strategijų, kaip valdyti dirbtinio intelekto agentų diegimo į gamybą kaštus:

**Naudojant mažesnius modelius:** Maži kalbos modeliai (SLM) gali gerai veikti tam tikruose agentiniuose naudojimo atvejuose ir reikšmingai sumažinti kaštus. Kaip minėta ankstesniame skyriuje, geriausias būdas suprasti, kaip gerai SLM veiks jūsų panaudojimo atveju, yra sukurti vertinimo sistemą, leidžiančią nustatyti ir palyginti našumą su didesniais modeliais. Apsvarstykite galimybę naudoti SLM paprastesnėms užduotims, tokioms kaip ketinimų klasifikavimas ar parametrų išgavimas, o didesnius modelius skirkite sudėtingam mąstymui.

**Naudojant maršrutizatoriaus modelį:** Panaši strategija yra naudoti įvairius modelius ir dydžius. Galite naudoti LLM/SLM arba serverless funkciją, kad nukreiptumėte užklausas pagal sudėtingumą į geriausiai tinkamus modelius. Tai taip pat padės sumažinti kaštus ir užtikrinti našumą tinkamose užduotyse. Pavyzdžiui, nukreipkite paprastas užklausas į mažesnius ir greitesnius modelius, o brangius didelius modelius naudokite tik sudėtingoms mąstymo užduotims.

**Atsakymų talpinimas (caching):** Nustatyti dažnas užklausas ir užduotis bei pateikti atsakymus prieš jiems patekiant į jūsų agentinę sistemą yra geras būdas sumažinti panašių užklausų kiekį. Galite netgi įgyvendinti srautą, kuris nustato, kiek užklausa panaši į jūsų talpinamas užklausas, naudojant paprastesnius DI modelius. Ši strategija gali reikšmingai sumažinti kaštus dažnai užduodamiems klausimams ar įprastiems darbo eigoms.

## Pažiūrėkime, kaip tai veikia praktikoje

[Šio skyriaus pavyzdiniame užrašyne](./code_samples/10-expense_claim-demo.ipynb) pamatysime, kaip galime naudoti stebėjimo įrankius, kad stebėtume ir vertintume savo agentą.


### Turite daugiau klausimų apie DI agentus gamyboje?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susipažintumėte su kitais besimokančiaisiais, dalyvautumėte aptarimų valandomis ir gautumėte atsakymus į savo klausimus apie DI agentus.

## Ankstesnė pamoka

[Metakognicijos dizaino šablonas](../09-metacognition/README.md)

## Kita pamoka

[Agentiniai protokolai](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->