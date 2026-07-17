[![Agentic RAG](../../../translated_images/sl/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na sliko zgoraj za ogled videa tega učnega gradiva)_

# Agentic RAG

To učno gradivo ponuja celovit pregled Agentic Retrieval-Augmented Generation (Agentic RAG), novega paradigme umetne inteligence, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, hkrati pa pridobivajo informacije iz zunanjih virov. V nasprotju s statičnimi vzorci pridobivanja in nato branja, vključuje Agentic RAG iterativne klice LLM, prekinjene z orodji ali funkcijskimi klici in strukturiranimi izhodi. Sistem ocenjuje rezultate, izboljšuje poizvedbe, po potrebi kliče dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve.

## Uvod

To učno gradivo bo zajemalo

- **Razumevanje Agentic RAG:** Spoznajte nastajajoči paradigm umetne inteligence, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, hkrati pa pridobivajo informacije iz zunanjih podatkovnih virov.
- **Razumevanje iterativnega Maker-Checker sloga:** Razumite zanko iterativnih klicev LLM, prekinjenih z orodji ali funkcijskimi klici in strukturiranimi izhodi, namenjenimi izboljšanju pravilnosti in obravnavi nepravilen poizvedb.
- **Raziskovanje praktičnih aplikacij:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, fokusirana na pravilnost, kompleksne interakcije z bazami podatkov in razširjeni delovni procesi.

## Cilji učenja

Po zaključku tega učnega gradiva boste znali/razumeli:

- **Razumevanje Agentic RAG:** Spoznajte nastajajoči paradigm umetne inteligence, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, hkrati pa pridobivajo informacije iz zunanjih podatkovnih virov.
- **Iterativni Maker-Checker slog:** Razumite koncept zanke iterativnih klicev LLM, prekinjenih z orodji ali funkcijskimi klici in strukturiranimi izhodi, namenjenih izboljšanju pravilnosti in obravnavi nepravilen poizvedb.
- **Obvladovanje procesa razmišljanja:** Razumite sistemovo sposobnost obvladovanja procesa razmišljanja, sprejemati odločitve o pristopu k problemom brez odvisnosti od vnaprej določenih poti.
- **Delovni tok:** Razumite, kako agentni model neodvisno odloča za pridobivanje poročil o trendih na trgu, prepoznavanje podatkov konkurentov, korelacijo notranjih prodajnih metrik, sintezo ugotovitev in ocenjevanje strategije.
- **Iterativne zanke, integracija orodij in pomnilnik:** Spoznajte, kako sistem temelji na vzorcu interakcije z zanko, vzdržuje stanje in pomnilnik skozi korake, da se izogne ponavljajočim zankam in sprejema informirane odločitve.
- **Obvladovanje načinov napak in samopopravljanje:** Raziskujte robustne mehanizme samopopravkov sistema, vključno z iteriranjem in ponovnim poizvedovanjem, uporabo diagnostičnih orodij in prehodi na človeški nadzor.
- **Meje avtonomije:** Razumite omejitve Agentic RAG, osredotočene na avtonomijo znotraj domen, odvisnost od infrastrukture in spoštovanje varnostnih omejitev.
- **Praktični primeri uporabe in vrednost:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, osredotočena na pravilnost, kompleksne interakcije z bazami podatkov in daljši delovni procesi.
- **Upravljanje, transparentnost in zaupanje:** Spoznajte pomen upravljanja in transparentnosti, vključno z razložljivim razmišljanjem, nadzorom pristranskosti in človeškim nadzorom.

## Kaj je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nastajajoči paradigm umetne inteligence, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, hkrati pa pridobivajo informacije iz zunanjih virov. V nasprotju s statičnimi vzorci pridobivanja in nato branja vključuje Agentic RAG iterativne klice LLM, prekinjene z orodji ali funkcijskimi klici in strukturiranimi izhodi. Sistem ocenjuje rezultate, izboljšuje poizvedbe, po potrebi kliče dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve. Ta iterativni "maker-checker" slog izboljšuje pravilnost, obvladuje napačne poizvedbe in zagotavlja visokokakovostne rezultate.

Sistem aktivno upravlja svoj proces razmišljanja, prepisuje neuspešne poizvedbe, izbira različne metode pridobivanja informacij in združuje več orodij—kot so iskanje po vektorjih v Azure AI Search, SQL baze podatkov ali lastni API-ji—preden dokončno poda odgovor. Značilna kakovost agentnega sistema je njegova sposobnost upravljanja svojega razmišljanja. Tradicionalne implementacije RAG se zanašajo na vnaprej določene poti, medtem ko agentni sistem samostojno določa zaporedje korakov na podlagi kakovosti najdenih informacij.

## Določanje Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nastajajoči paradigme v razvoju umetne inteligence, kjer LLM ne le pridobivajo informacije iz zunanjih podatkovnih virov, ampak tudi samostojno načrtujejo svoje naslednje korake. V nasprotju s statičnimi vzorci pridobivanja in nato branja ali skrbno načrtovanimi nizi pozivov, vključuje Agentic RAG zanko iterativnih klicev LLM, prekinjenih z orodji ali funkcijskimi klici in strukturiranimi izhodi. Ob vsakem koraku sistem ocenjuje pridobljene rezultate, odloča, ali je treba izboljšati poizvedbe, po potrebi kliče dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve.

Ta iterativni "maker-checker" slog delovanja je zasnovan za izboljšanje pravilnosti, obravnavo napačnih poizvedb do strukturiranih baz podatkov (npr. NL2SQL) in zagotavljanje uravnoteženih, visokokakovostnih rezultatov. Namesto da bi se zanašal samo na natančno zasnovane verige pozivov, sistem aktivno upravlja svoj proces razmišljanja. Lahko prepiše neuspešne poizvedbe, izbere različne metode pridobivanja in združi več orodij—kot so iskanje po vektorjih v Azure AI Search, SQL baze podatkov ali lastni API-ji—preden dokončno poda odgovor. S tem odstrani potrebo po preveč zapletenih okvirih orkestracije. Namesto tega lahko razmeroma preprosta zanka "klic LLM → uporaba orodja → klic LLM → ..." prinese sofisticirane in dobro utemeljene izhode.

![Agentic RAG Core Loop](../../../translated_images/sl/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Upravljanje procesa razmišljanja

Značilna lastnost, ki sistem naredi "agentnega", je njegova sposobnost upravljanja lastnega procesa razmišljanja. Tradicionalne implementacije RAG pogosto temeljijo na vnaprej določenih poteh, ki jih ljudje pripravijo za model: verigi misli, ki opisuje, kaj pridobiti in kdaj.
Vendar, ko je sistem resnično agenten, interno odloča, kako se lotiti problema. Ne izvaja samo scenarij; samostojno določa zaporedje korakov na podlagi kakovosti najdenih informacij.
Na primer, če ga prosijo za izdelavo strategije lansiranja izdelka, se ne zanese samo na poziv, ki v celoti opiše raziskovalni in odločilni proces. Namesto tega agentni model samostojno odloča, da:

1. Pridobi trenutna poročila o trendih na trgu z uporabo Bing Web Grounding
2. Identificira ustrezne podatke o konkurentih z uporabo Azure AI Search.
3. Korelira zgodovinske notranje prodajne metrike z uporabo Azure SQL Database.
4. Sintesizira ugotovitve v skladno strategijo, orkestrirano prek Azure OpenAI Service.
5. Ocenjuje strategijo za vrzeli ali neskladnosti, če je potrebno sproži nov krog pridobivanja.
Vsi ti koraki—izboljševanje poizvedb, izbira virov, iteriranje dokler ni "zadovoljen" z odgovorom—so odločitve modela, ne pa vnaprej določene s strani človeka.

## Iterativne zanke, integracija orodij in pomnilnik

![Tool Integration Architecture](../../../translated_images/sl/tool-integration.0f569710b5c17c10.webp)

Agentni sistem se zanaša na vzorec interakcije z zanko:

- **Začetni klic:** Cilj uporabnika (tudi uporabniški poziv) se predstavi LLM.
- **Klic orodja:** Če model ugotovi, da manjkajo informacije ali so navodila nejasna, izbere orodje ali metodo pridobivanja—kot je poizvedba v vektorski bazi podatkov (npr. Azure AI Search Hybrid iskanje po zasebnih podatkih) ali strukturiran SQL klic—za zbiranje več konteksta.
- **Ocena in izboljšava:** Po pregledu vrnjenih podatkov model odloča, ali so informacije zadostne. Če ne, izboljša poizvedbo, preizkusi drugo orodje ali prilagodi pristop.
- **Ponovi dokler ni zadovoljen:** Ta cikel se nadaljuje, dokler model ne ugotovi, da ima dovolj jasnosti in dokazov za podajo končnega, dobro premišljenega odgovora.
- **Pomnilnik in stanje:** Ker sistem vzdržuje stanje in pomnilnik skozi korake, se lahko spomni prejšnjih poskusov in njihovih izidov, s čimer se izogne ponavljajočim zankam in sprejema bolj informirane odločitve med postopkom.

Sčasoma to ustvarja občutek razvijajočega se razumevanja, ki omogoča modelu navigacijo skozi kompleksne, večkorakne naloge brez potrebe po stalnem človekovem vpletanju ali spreminjanju pozivov.

## Obvladovanje načinov napak in samopopravljanje

Avtonomija Agentic RAG vključuje tudi robustne mehanizme samopopravkov. Ko sistem naleti na mrtve točke—kot so pridobivanje nepomembnih dokumentov ali soočanje z napačnimi poizvedbami—lahko:

- **Iterira in ponovi poizvedbo:** Namesto da bi vrnil nizkocenovne odgovore, model poskuša nove strategije iskanja, prepiše poizvedbe v bazi podatkov ali pregleda alternativne nize podatkov.
- **Uporaba diagnostičnih orodij:** Sistem lahko kliče dodatne funkcije, zasnovane za pomoč pri razhroščevanju korakov razmišljanja ali potrditvi pravilnosti pridobljenih podatkov. Orodja, kot je Azure AI Tracing, bodo pomembna za omogočanje robustne opaznosti in nadzora.
- **Prehod na človeški nadzor:** Za situacije z visokim tveganjem ali ponavljajoče neuspešne primere lahko model označi negotovost in zahteva človeško usmeritev. Ko človek poda popravljive povratne informacije, jih model lahko upošteva v prihodnosti.

Ta iterativni in dinamični pristop omogoča modelu nenehno izboljševanje, zagotavljajoč, da ni le enkratni sistem, ampak tak, ki se uči iz svojih napak med posamezno seanso.

![Self Correction Mechanism](../../../translated_images/sl/self-correction.da87f3783b7f174b.webp)

## Meje avtonomije

Kljub svoji avtonomiji znotraj naloge Agentic RAG ni primerljiv z umetno splošno inteligenco (AGI). Njegove "agentne" zmogljivosti so omejene na orodja, podatkovne vire in politike, ki jih zagotavljajo človeški razvijalci. Ne more si izumiti lastnih orodij ali stopiti izven omejitev domene, ki so bile določene. Namesto tega izstopa pri dinamični orkestraciji razpoložljivih virov.
Ključne razlike od bolj naprednih oblik umetne inteligence vključujejo:

1. **Avtonomija, specifična za domeno:** Agentni sistemi RAG so osredotočeni na doseganje ciljev, ki jih določi uporabnik znotraj znane domene, pri tem uporabljajo strategije, kot so prepisovanje poizvedb ali izbira orodij za izboljšanje rezultatov.
2. **Odvisnost od infrastrukture:** Zmožnosti sistema so odvisne od orodij in podatkov, ki jih integrirajo razvijalci. Ne more preseči teh meja brez človeškega posega.
3. **Spoštovanje varnostnih omejitev:** Etična pravila, pravila skladnosti in poslovne politike ostajajo zelo pomembni. Svoboda agenta je vedno omejena z varnostnimi ukrepi in nadzornimi mehanizmi (upamo?).

## Praktični primeri uporabe in vrednost

Agentic RAG izstopa v scenarijih, ki zahtevajo iterativno izboljšavo in natančnost:

1. **Okolja, ki dajejo prednost pravilnosti:** Pri preverjanju skladnosti, regulativnih analizah ali pravnih raziskavah lahko agentni model večkrat preveri dejstva, se posvetuje z več viri in prepiše poizvedbe, dokler ne ustvari popolnoma preverjenega odgovora.
2. **Kompleksne interakcije z bazami podatkov:** Pri delu s strukturiranimi podatki, kjer poizvedbe pogosto spodletijo ali jih je treba prilagoditi, lahko sistem samostojno izboljša poizvedbe z uporabo Azure SQL ali Microsoft Fabric OneLake, s čimer zagotovi, da je končno pridobljeno skladno z uporabniškimi nameni.
3. **Razširjeni delovni procesi:** Dolgotrajne seje se lahko razvijajo z novimi informacijami. Agentic RAG lahko nenehno vključuje nove podatke in spreminja strategije, ko se uči več o problematiki.

## Upravljanje, transparentnost in zaupanje

Ko sistemi postajajo bolj avtonomni v svojem razmišljanju, sta upravljanje in preglednost ključna:

- **Razložljivo razmišljanje:** Model lahko zagotovi revizijsko sled poizvedb, ki jih je izvedel, virov, ki jih je pregledal, in korakov razmišljanja, ki jih je uporabil za dosego zaključka. Orodja, kot sta Azure AI Content Safety in Azure AI Tracing / GenAIOps, lahko pomagajo ohranjati preglednost in ublažiti tveganja.
- **Nadzor pristranskosti in uravnoteženo pridobivanje:** Razvijalci lahko prilagajajo strategije pridobivanja informacij, da zagotovijo upoštevanje uravnoteženih in reprezentativnih podatkovnih virov, ter redno pregledujejo izhode, da zaznajo pristranskost ali izkrivljene vzorce z uporabo prilagojenih modelov za napredne organizacije podatkovnih znanosti, ki uporabljajo Azure Machine Learning.
- **Človeški nadzor in skladnost:** Za občutljive naloge ostaja človeški pregled bistven. Agentic RAG ne zamenjuje človeške presoje pri odločanju z visokimi vložki—namesto tega jo dopolnjuje z zagotavljanjem podrobneje preverjenih možnosti.

Imati orodja, ki nudijo jasno evidenco o opravilih, je bistveno. Brez njih je razhroščevanje večkoraknega procesa zelo zahtevno. Oglejte si naslednji primer iz Literal AI (podjetje za Chainlit) za primer delovanja agenta:

![AgentRunExample](../../../translated_images/sl/AgentRunExample.471a94bc40cbdc0c.webp)

## Zaključek

Agentic RAG predstavlja naravno evolucijo v načinu, kako sistemi umetne inteligence obravnavajo kompleksne, podatkovno intenzivne naloge. Z uporabo vzorca interakcije z zanko, samostojno izbiro orodij in izboljševanjem poizvedb, dokler ne doseže visokokakovostnega rezultata, sistem presega statično izvajanje pozivov in postane bolj prilagodljiv, kontekstualno zavesten odločevalec. Čeprav je še vedno omejen z infrastrukturo in etičnimi smernicami, ki jih določajo ljudje, te agentne zmogljivosti omogočajo bogatejše, bolj dinamične in na koncu bolj uporabne interakcije z AI tako za podjetja kot končne uporabnike.

### Imate več vprašanj o Agentic RAG?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Izvedba Retrieval Augmented Generation (RAG) z Azure OpenAI Service: Naučite se uporabljati lastne podatke z Azure OpenAI Service. Ta modul Microsoft Learn ponuja celovit vodič o implementaciji RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena aplikacij generativne AI z Microsoft Foundry: Ta članek pokriva ocenjevanje in primerjavo modelov na javno dostopnih podatkovnih nizih, vključno z agentnimi AI aplikacijami in RAG arhitekturami</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Kaj je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: celovit vodič po agentno osnovani Retrieval Augmented Generation – novice iz generacije RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: pospešite svoj RAG z reformulacijo poizvedb in samopovpraševanjem! Hugging Face odprtokodna kuharska knjiga AI</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodajanje agentnih plasti k RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Prihodnost znanstvenih pomočnikov: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako zgraditi agentne RAG sisteme</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Uporaba Microsoft Foundry Agent Service za razširitev vaših AI agentov</a>

### Akademski članki

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno izboljševanje s samopovratno zvezo</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezikovni agenti z verbalnim okrepljenim učenjem</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezikovni modeli se lahko samopopravljajo z orodjno interaktivno kritiko</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentna generacija z izboljšanim iskanjem: Pregled agentnega RAG</a>

## Preizkus delovanja tega agenta (neobvezno)

Ko se naučite nameščati agente v [Lekcija 16](../16-deploying-scalable-agents/README.md), lahko preizkusite delovanje `TravelRAGAgent` iz te lekcije — preverite, da njegovi odgovori ostanejo utemeljeni v bazi znanja — z [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Ogledate si lahko [`tests/README.md`](../tests/README.md) za navodila, kako ga zagnati.

## Predhodna lekcija

[Vzorec uporabe orodij](../04-tool-use/README.md)

## Naslednja lekcija

[Gradnja zanesljivih AI agentov](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->