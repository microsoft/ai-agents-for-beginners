[![Agentic RAG](../../../translated_images/lt/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Agentic RAG

Ši pamoka suteikia išsamų Agentic Retrieval-Augmented Generation (Agentic RAG) apžvalgą – naują AI paradigmą, kurioje dideli kalbos modeliai (LLM) savarankiškai planuoja savo kitus veiksmus, tuo pačiu traukdami informaciją iš išorinių šaltinių. Skirtingai nei statiniai paieškos-tada-skaitymo modeliai, Agentic RAG apima iteratyvius LLM kvietimus, pertraukiamus įrankių ar funkcijų kvietimais ir struktūrizuotais rezultatais. Sistema vertina rezultatus, tobulina užklausas, jei reikia – iškviečia papildomus įrankius ir tęsia šį ciklą, kol pasiekia patenkinamą sprendimą.

## Įvadas

Ši pamoka apims

- **Suprasti Agentic RAG:** Sužinokite apie naują AI paradigmą, kurioje dideli kalbos modeliai (LLM) savarankiškai planuoja savo kitus veiksmus, traukdami informaciją iš išorinių duomenų šaltinių.
- **Įsisavinti Iteratyvų Maker-Checker stilių:** Suprasti iteratyvių LLM kvietimų ciklą, pertraukiamą įrankių ar funkcijų kvietimais ir struktūrizuotais rezultatais, skirtą tikslumo gerinimui ir klaidų užklausose tvarkymui.
- **Ištirti praktines taikymo sritis:** Nustatyti scenarijus, kuriuose Agentic RAG ypač efektyvus, kaip taisyklių pirmumo aplinkos, sudėtingos duomenų bazės interakcijos ir išplėstiniai darbo procesai.

## Mokymosi tikslai

Baigę šią pamoką, jūs sugebėsite / suprasite:

- **Agentic RAG supratimas:** Sužinoti apie naują AI paradigmą, kurioje dideli kalbos modeliai (LLM) savarankiškai planuoja savo kitus veiksmus, traukdami informaciją iš išorinių duomenų šaltinių.
- **Iteratyvus Maker-Checker stilius:** Suprasti iteratyvių LLM kvietimų ciklo koncepciją, pertraukiamą įrankių ar funkcijų kvietimais ir struktūrizuotais rezultatais, skirtą tikslumo gerinimui ir klaidų užklausose tvarkymui.
- **Mąstymo proceso valdymas:** Suprasti sistemos gebėjimą valdyti savo mąstymo procesą, savarankiškai spręsti, kaip spręsti problemas, nenaudojant iš anksto apibrėžtų kelių.
- **Darbo eiga:** Suprasti, kaip agentinis modelis savarankiškai nusprendžia gauti rinkos tendencijų ataskaitas, identifikuoti konkurentų duomenis, susieti vidinius pardavimų rodiklius, sintetinti išvadas ir įvertinti strategiją.
- **Iteratyvūs ciklai, įrankių integracija ir atmintis:** Sužinoti apie sistemos priklausomybę nuo ciklinio sąveikos modelio su būsena ir atmintimi, vengiant kartojimosi ir priimant pagrįstus sprendimus.
- **Gedimų valdymas ir savikorekcija:** Ištirti sistemos tvirtas savikorekcijos priemones, įskaitant iteracijas ir pakartotinį užklausų siuntimą, diagnostinių įrankių naudojimą bei žmonių priežiūrą.
- **Agentūros ribos:** Suprasti Agentic RAG apribojimus, sutelkiant dėmesį į srities specifinę autonomiją, infrastruktūros priklausomybę ir apsaugos priemonių laikymąsi.
- **Praktinės taikymo sritys ir vertė:** Nustatyti scenarijus, kuriuose Agentic RAG išsiskiria, kaip tikslumo pirmumo aplinkos, sudėtingos duomenų bazės interakcijos ir ilgalaikiai darbo procesai.
- **Valdymas, skaidrumas ir pasitikėjimas:** Sužinoti apie valdymo ir skaidrumo svarbą, įskaitant paaiškinamą mąstymą, šališkumo kontrolę ir žmonių priežiūrą.

## Kas yra Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) yra nauja AI paradigma, kurioje dideli kalbos modeliai (LLM) savarankiškai planuoja savo žingsnius, tuo pat metu traukdami informaciją iš išorinių šaltinių. Skirtingai nuo statinių paieškos-tada-skaitymo modelių, Agentic RAG apima iteratyvius LLM kvietimus, pertraukiamus įrankių ar funkcijų kvietimais ir struktūrizuotais rezultatais. Sistema vertina rezultatus, tobulina užklausas, iškviečia papildomus įrankius, jei reikia, ir tęsia šį ciklą tol, kol pasiekia patenkinamą sprendimą. Šis iteratyvus “maker-checker” stilius gerina tikslumą, tvarko klaidingas užklausas ir užtikrina aukštos kokybės rezultatus.

Sistema aktyviai valdo savo mąstymo procesą, perrašo nepavykusias užklausas, pasirenka skirtingus paieškos metodus ir integruoja kelis įrankius – tokius kaip vektorinė paieška Azure AI Search, SQL duomenų bazės ar pasirinktinius API, prieš pabaigdama atsakymą. Agentinės sistemos išskirtinumas yra gebėjimas valdyti savo mąstymo procesą. Tradiciniai RAG įgyvendinimai remiasi iš anksto apibrėžtais keliais, o agentinė sistema savarankiškai nustato veiksmų seką pagal rastos informacijos kokybę.

## Agentic Retrieval-Augmented Generation (Agentic RAG) apibrėžimas

Agentic Retrieval-Augmented Generation (Agentic RAG) yra nauja AI kūrimo paradigma, kurioje LLM ne tik traukia informaciją iš išorinių duomenų šaltinių, bet ir savarankiškai planuoja savo kitus veiksmus. Skirtingai nuo statinių paieškos-tada-skaitymo modelių ar kruopščiai suplanuotų užklausų sekų, Agentic RAG apima iteratyvių LLM kvietimų ciklą, pertraukiamą įrankių ar funkcijų kvietimais bei struktūrizuotais rezultatais. Kiekviename žingsnyje sistema įvertina gautus rezultatus, nusprendžia, ar reikalinga tobulinti užklausas, iškviečia papildomus įrankius, jei reikia, ir tęsia šį ciklą, kol pasiekia patenkinamą sprendimą.

Šis iteratyvus “maker-checker” veikimo stilius skirtas gerinti tikslumą, tvarkyti klaidingas užklausas į struktūrizuotas duomenų bazes (pvz., NL2SQL) ir užtikrinti subalansuotus, aukštos kokybės rezultatus. Vietoj to, kad remtųsi vien tik kruopščiai sukurtomis užklausų grandinėmis, sistema aktyviai valdo savo mąstymo procesą. Ji gali perrašyti nepavykusias užklausas, pasirinkti kitus paieškos metodus ir integruoti kelis įrankius – tokius kaip vektorinė paieška Azure AI Search, SQL duomenų bazės ar pasirinktinius API – prieš galutinai pateikdama atsakymą. Tai pašalina pernelyg sudėtingų sąrankos sistemų poreikį. Vietoje to, paprastas “LLM kvietimas → įrankio naudojimas → LLM kvietimas → …” ciklas gali duoti pažangius ir gerai pagrįstus rezultatus.

![Agentic RAG Core Loop](../../../translated_images/lt/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Mąstymo proceso valdymas

Unikali savybė, daranti sistemą „agentine“, yra jos gebėjimas valdyti savo mąstymo procesą. Tradiciniai RAG įgyvendinimai dažnai priklauso nuo žmonių, iš anksto apibrėžiančių modelio veiksmų seką: mąstymo grandinę, kuri nurodo, ką ir kada traukti.
Tačiau kai sistema iš tikrųjų yra agentinė, ji viduje savarankiškai nusprendžia, kaip spręsti problemą. Ji ne tik vykdo scenarijų, bet savarankiškai nustato tavo žingsnių seką pagal rastos informacijos kokybę.
Pavyzdžiui, jei jos prašoma sukurti produkto paleidimo strategiją, ji neapsiriboja vien tik užklausa, kurioje aprašomas visas tyrimo ir sprendimų priėmimo procesas. Vietoje to agentinis modelis savarankiškai nusprendžia:

1. Gautis dabartines rinkos tendencijų ataskaitas naudojant Bing Web Grounding
2. Identifikuoti aktualius konkurentų duomenis naudojant Azure AI Search.
3. Susieti istorinius vidinius pardavimų rodiklius, naudodamas Azure SQL duomenų bazę.
4. Sintetinti išvadas į vieningą strategiją, kurią organizuoja Azure OpenAI Service.
5. Įvertinti strategiją dėl spragų ar neatitikimų ir, jei reikia, atlikti dar vieną paieškos etapą.
Visi šie žingsniai – užklausų tobulinimas, šaltinių pasirinkimas, iteravimas tol, kol modelis „džiaugiasi“ atsakymu – yra modelio sprendžiami, o ne iš anksto žmogaus užrašyti.

## Iteratyvūs ciklai, įrankių integracija ir atmintis

![Tool Integration Architecture](../../../translated_images/lt/tool-integration.0f569710b5c17c10.webp)

Agentinė sistema remiasi cikline sąveikos schema:

- **Pradinis kvietimas:** Naudotojo tikslas (naudotojo užklausa) pateikiamas LLM.
- **Įrankių iškvietimas:** Jei modelis nustato trūkstamą informaciją ar neaiškias instrukcijas, jis pasirenka įrankį arba paieškos metodą – pvz., vektorinės duomenų bazės užklausą (pvz., Azure AI Search hibridinę paiešką per privačius duomenis) arba struktūrizuotą SQL užklausą – kad surinktų daugiau konteksto.
- **Vertinimas ir tobulinimas:** Peržiūrėjęs gautus duomenis modelis nusprendžia, ar informacijos pakanka. Jei ne, jis tobulina užklausą, bando kitą įrankį arba keičia požiūrį.
- **Kartojimas, kol patenkinama:** Šis ciklas tęsiasi tol, kol modelis nustato, kad turi pakankamai aiškumo ir įrodymų galutiniam, gerai pagrįstam atsakymui pateikti.
- **Atmintis ir būsena:** Kadangi sistema palaiko būseną ir atmintį žingsnių metu, ji gali prisiminti ankstesnius bandymus ir jų rezultatus, vengdama pasikartojančių ciklų ir priimdama pagrįstus sprendimus, vykdydama užduotį.

Bėgant laikui tai sukuria nuolatinio supratimo jausmą, leidžiant modeliui naviguoti sudėtingas, daugžingsnes užduotis be nuolatinės žmogaus intervencijos ar užklausos pertvarkymo.

## Gedimų valdymas ir savikorekcija

Agentic RAG autonomija taip pat apima tvirtas savikorekcijos mechanizmus. Kai sistema susiduria su aklavietėmis – pavyzdžiui, grąžina nereikšmingus dokumentus arba gauna klaidingas užklausas – ji gali:

- **Iteruoti ir pakartotinai užklausti:** Vietoje žemos vertės atsakymų modelis bando naujas paieškos strategijas, perrašo duomenų bazės užklausas arba ieško alternatyvių duomenų rinkinių.
- **Naudoti diagnostinius įrankius:** Sistema gali iškviesti papildomas funkcijas, skirtas padėti tikrinti mąstymo žingsnius arba patvirtinti surinktų duomenų teisingumą. Įrankiai, tokie kaip Azure AI Tracing, bus svarbūs užtikrinant tvirtą stebimą priežiūrą ir monitoringo galimybes.
- **Pasileisti žmogaus priežiūrą:** Aukštos svarbos arba kartojančiai nesėkmingose situacijose modelis gali pažymėti neaiškumą ir prašyti žmogaus nurodymų. Kai žmogus pateikia korekcinį grįžtamąjį ryšį, modelis gali įtraukti šią pamoką į savo veikimą ateityje.

Šis iteratyvus ir dinamiškas požiūris leidžia modeliui nuolat tobulėti, užtikrindamas, kad tai nėra vienkartinis sprendimas, bet sistema, mokanti iš savo klaidų per sesiją.

![Self Correction Mechanism](../../../translated_images/lt/self-correction.da87f3783b7f174b.webp)

## Agentūros ribos

Nepaisant savarankiškumo užduotyje, Agentic RAG nėra analogiškas Dirbtiniam Bendrajam Intelektui. Jo „agentinės“ galimybės ribojasi įrankiais, duomenų šaltiniais ir politika, kurias teikia žmonių kūrėjai. Sistema negali sugalvoti savo įrankių ar išeiti už nustatytų sričių ribų. Vietoje to, ji puikiai organizuoja turimus išteklius dinamiškai.
Pagrindiniai skirtumai nuo pažangesnių AI formų yra:

1. **Srities specializuotas savarankiškumas:** Agentic RAG sistemos koncentruojasi į naudotojo apibrėžtų tikslų pasiekimą žinomoje srityje, naudojant strategijas, tokias kaip užklausų perrašymas ar įrankių pasirinkimas tikslui gerinti.
2. **Priklausomybė nuo infrastruktūros:** Sistemos galimybės priklauso nuo kūrėjų integruotų įrankių ir duomenų. Ji negali peržengti šių ribų be žmogaus intervencijos.
3. **Pagarba taisyklių riboms:** Etikos gairės, atitikties taisyklės ir verslo politika išlieka labai svarbios. Agenčio laisvė visada yra ribojama saugumo priemonių ir priežiūros mechanizmų (tikimės?).

## Praktinės taikymo sritys ir vertė

Agentic RAG ypač vertingas scenarijuose, kuriems reikalingas iteratyvus tobulinimas ir tikslumas:

1. **Tikslumo pirmumo aplinkos:** Atitikties patikrinimuose, reguliavimo analizėje ar teisės tyrimuose agentinis modelis gali pakartotinai tikrinti faktus, konsultuotis su keliais šaltiniais ir perrašinėti užklausas, kol pateikia kruopščiai patikrintą atsakymą.
2. **Sudėtingos duomenų bazės interakcijos:** Dirbant su struktūrizuotais duomenimis, kur užklausos dažnai nepavyksta arba jas reikia koreguoti, sistema gali savarankiškai tikslinti užklausas naudodama Azure SQL arba Microsoft Fabric OneLake, užtikrindama, kad galutinis rezultatas atitinka naudotojo tikslą.
3. **Išplėstiniai darbo procesai:** Ilgesnės sesijos gali vystytis, kai atsiranda naujos informacijos. Agentic RAG nuolat įtraukia naujus duomenis, keičia strategijas, kai mokosi daugiau apie problemos sritį.

## Valdymas, skaidrumas ir pasitikėjimas

Kadangi šios sistemos tampa vis savarankiškesnės savo mąstyme, valdymas ir skaidrumas yra labai svarbūs:

- **Paaiškinamas mąstymas:** Modelis gali pateikti audito kelią, nurodydamas, kokias užklausas jis atliko, kokius šaltinius konsultavosi ir kokius mąstymo žingsnius atliko, kad pasiektų išvadą. Įrankiai, tokie kaip Azure AI Content Safety ir Azure AI Tracing / GenAIOps, padeda palaikyti skaidrumą ir mažinti rizikas.
- **Šališkumo kontrolė ir subalansuota paieška:** Kūrėjai gali reguliuoti paieškos strategijas, kad būtų užtikrintas subalansuotų, reprezentatyvių duomenų šaltinių svarstymas, taip pat reguliariai tikrinti rezultatus, siekiant aptikti šališkumą ar iškreiptas tendencijas, naudojant pasirinktuosius modelius pažangiems duomenų mokslo organizacijoms, naudojančioms Azure Machine Learning.
- **Žmonių priežiūra ir atitiktis:** Jautriems uždaviniams būtina žmogaus apžvalga. Agentic RAG nepakeičia žmogaus sprendimo aukštos svarbos situacijose – jis jį papildo, pateikdamas kruopštų patikrintų variantų.

Turėti įrankius, kurie suteikia aiškią veiksmų įrašo seką, yra esminis dalykas. Be jų, daugžingsnio proceso derinimas gali būti labai sudėtingas. Žr. šį Literal AI pavyzdį (įmonės, kuri sukūrė Chainlit) apie Agentų vykdymą:

![AgentRunExample](../../../translated_images/lt/AgentRunExample.471a94bc40cbdc0c.webp)

## Išvada

Agentic RAG reiškia natūralią evoliuciją, kaip AI sistemos tvarko sudėtingas, duomenų intensyvumo užduotis. Priimdama ciklinio sąveikos modelio principą, savarankiškai pasirinkdama įrankius ir iteratyviai tobulindama užklausas, kol pasiekia aukštos kokybės rezultatą, sistema žengia už statinio užklausų vykdymo ribų į labiau adaptyvų, kontekstu pagrįstą sprendimų priėmėją. Nors vis dar ribojamą žmogaus apibrėžtų infrastruktūrų ir etikos gairių, šios agentinės galimybės leidžia sukurti turtingesnę, dinamiškesnę ir galiausiai naudingesnę AI sąveiką tiek įmonėms, tiek galutiniams vartotojams.

### Turite daugiau klausimų apie Agentic RAG?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ir susipažinkite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į klausimus apie savo AI agentus.

## Papildomi ištekliai

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Agentinės Retrieval-Augmented Generation (RAG) įgyvendinimas su Azure OpenAI Service: sužinokite, kaip naudoti savo duomenis su Azure OpenAI Service. Šis Microsoft Learn modulis suteikia išsamų vadovą apie RAG įgyvendinimą</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatyvivės AI taikomųjų programų vertinimas su Microsoft Foundry: straipsnyje aptariamas modelių vertinimas ir palyginimas su viešai prieinamais duomenų rinkiniais, įskaitant Agentic AI taikymus ir RAG architektūras</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Kas yra Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: išsamus vadovas apie agentais pagrįstą Retrieval-Augmented Generation – Naujienos iš generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentinis RAG: pagreitinkite savo RAG naudodami užklausų pertvarkymą ir savęs užklausimą! Hugging Face atvirojo kodo AI receptų knyga</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentinių sluoksnių pridėjimas prie RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Žinių Asistentų ateitis: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kaip sukurti agentinius RAG sistemus</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Kaip naudoti Microsoft Foundry Agent Service, kad mastelizuotumėte savo AI agentus</a>

### Akademiniai straipsniai

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratyvus tobulinimas su savistabos grįžtamuoju ryšiu</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Kalbos agentai su žodžiu pagrįstu stiprinamuoju mokymusi</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Didieji kalbos modeliai gali savikoreguotis naudodami įrankiais pagrįstą kritikos metodą</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentinė ieškomoji generacija: apžvalga apie agentinį RAG</a>

## Šio agento dūmų testavimas (pasirinktinai)

Kai išmoksite diegti agentus [16 pamokoje](../16-deploying-scalable-agents/README.md), galite atlikti šioje pamokoje aptariamo `TravelRAGAgent` dūmų testą — patikrinti, ar jo atsakymai lieka pagrįsti žinių baze — naudodami [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Peržiūrėkite [`tests/README.md`](../tests/README.md), kaip jį paleisti.

## Ankstesnė pamoka

[Įrankių naudojimo dizaino šablonas](../04-tool-use/README.md)

## Kitas pamoka

[Patikimų AI agentų kūrimas](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->