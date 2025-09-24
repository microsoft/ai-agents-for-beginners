<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T23:17:31+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "sl"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.sl.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na zgornjo sliko za ogled videoposnetka te lekcije)_

# Agentic RAG

Ta lekcija ponuja celovit pregled paradigme Agentic Retrieval-Augmented Generation (Agentic RAG), novega pristopa v umetni inteligenci, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov. Za razliko od statičnih vzorcev "pridobi nato preberi" Agentic RAG vključuje iterativne klice LLM, prepletene z uporabo orodij ali funkcij in strukturiranimi izhodi. Sistem ocenjuje rezultate, izpopolnjuje poizvedbe, po potrebi uporablja dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve.

## Uvod

Ta lekcija bo obravnavala:

- **Razumevanje Agentic RAG:** Spoznajte novo paradigmo v umetni inteligenci, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov podatkov.
- **Iterativni pristop Maker-Checker:** Razumite zanko iterativnih klicev LLM, prepletenih z uporabo orodij ali funkcij in strukturiranimi izhodi, zasnovano za izboljšanje pravilnosti in obravnavo napačnih poizvedb.
- **Raziskovanje praktičnih aplikacij:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, kjer je pravilnost na prvem mestu, kompleksne interakcije z bazami podatkov in razširjeni delovni tokovi.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:

- **Razumevanje Agentic RAG:** Spoznajte novo paradigmo v umetni inteligenci, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov podatkov.
- **Iterativni pristop Maker-Checker:** Razumite koncept zanke iterativnih klicev LLM, prepletenih z uporabo orodij ali funkcij in strukturiranimi izhodi, zasnovano za izboljšanje pravilnosti in obravnavo napačnih poizvedb.
- **Prevzemanje odgovornosti za proces razmišljanja:** Razumite sposobnost sistema, da prevzame odgovornost za svoj proces razmišljanja, sprejema odločitve o pristopu k problemom brez zanašanja na vnaprej določene poti.
- **Delovni tok:** Razumite, kako agentični model samostojno odloča o pridobivanju poročil o tržnih trendih, prepoznavanju podatkov o konkurentih, povezovanju notranjih prodajnih metrik, sintezi ugotovitev in ocenjevanju strategije.
- **Iterativne zanke, integracija orodij in spomin:** Spoznajte zanašanje sistema na vzorec interakcije v zanki, ohranjanje stanja in spomina skozi korake za preprečevanje ponavljajočih se zank in sprejemanje informiranih odločitev.
- **Obravnavanje načinov neuspeha in samopopravljanje:** Raziskujte robustne mehanizme samopopravljanja sistema, vključno z iteracijo in ponovnim poizvedovanjem, uporabo diagnostičnih orodij in zanašanjem na človeški nadzor.
- **Meje agentnosti:** Razumite omejitve Agentic RAG, s poudarkom na avtonomiji, specifični za domeno, odvisnosti od infrastrukture in spoštovanju varoval.
- **Praktični primeri uporabe in vrednost:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, kjer je pravilnost na prvem mestu, kompleksne interakcije z bazami podatkov in razširjeni delovni tokovi.
- **Upravljanje, preglednost in zaupanje:** Spoznajte pomen upravljanja in preglednosti, vključno z razložljivim razmišljanjem, nadzorom pristranskosti in človeškim nadzorom.

## Kaj je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova paradigma v umetni inteligenci, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov. Za razliko od statičnih vzorcev "pridobi nato preberi" Agentic RAG vključuje iterativne klice LLM, prepletene z uporabo orodij ali funkcij in strukturiranimi izhodi. Sistem ocenjuje rezultate, izpopolnjuje poizvedbe, po potrebi uporablja dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve. Ta iterativni pristop "maker-checker" izboljšuje pravilnost, obravnava napačne poizvedbe in zagotavlja visokokakovostne rezultate.

Sistem aktivno prevzema odgovornost za svoj proces razmišljanja, prepisuje neuspele poizvedbe, izbira različne metode pridobivanja in integrira več orodij—kot so iskanje vektorjev v Azure AI Search, SQL baze podatkov ali prilagojeni API-ji—preden dokonča svoj odgovor. Ključna značilnost agentičnega sistema je njegova sposobnost, da prevzame odgovornost za svoj proces razmišljanja. Tradicionalne implementacije RAG se zanašajo na vnaprej določene poti, medtem ko agentični sistem samostojno določa zaporedje korakov na podlagi kakovosti najdenih informacij.

## Definicija Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova paradigma v razvoju umetne inteligence, kjer LLM ne le pridobivajo informacije iz zunanjih virov podatkov, temveč tudi samostojno načrtujejo svoje naslednje korake. Za razliko od statičnih vzorcev "pridobi nato preberi" ali skrbno skriptiranih zaporedij pozivov Agentic RAG vključuje zanko iterativnih klicev LLM, prepletenih z uporabo orodij ali funkcij in strukturiranimi izhodi. Na vsakem koraku sistem ocenjuje pridobljene rezultate, se odloča, ali bo izpopolnil poizvedbe, po potrebi uporablja dodatna orodja in nadaljuje ta cikel, dokler ne doseže zadovoljive rešitve.

Ta iterativni pristop "maker-checker" je zasnovan za izboljšanje pravilnosti, obravnavo napačnih poizvedb v strukturirane baze podatkov (npr. NL2SQL) in zagotavljanje uravnoteženih, visokokakovostnih rezultatov. Namesto da bi se zanašal zgolj na skrbno zasnovane verige pozivov, sistem aktivno prevzema odgovornost za svoj proces razmišljanja. Lahko prepiše neuspele poizvedbe, izbere različne metode pridobivanja in integrira več orodij—kot so iskanje vektorjev v Azure AI Search, SQL baze podatkov ali prilagojeni API-ji—preden dokonča svoj odgovor. To odpravlja potrebo po preveč zapletenih orkestracijskih okvirih. Namesto tega lahko relativno preprosta zanka "klic LLM → uporaba orodja → klic LLM → ..." prinese prefinjene in dobro utemeljene rezultate.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.sl.png)

## Prevzemanje odgovornosti za proces razmišljanja

Ključna značilnost, ki naredi sistem "agentičen", je njegova sposobnost, da prevzame odgovornost za svoj proces razmišljanja. Tradicionalne implementacije RAG se pogosto zanašajo na ljudi, da vnaprej določijo pot za model: verigo misli, ki določa, kaj pridobiti in kdaj.
Ko pa je sistem resnično agentičen, se sam odloča, kako pristopiti k problemu. Ne izvaja le skripta; samostojno določa zaporedje korakov na podlagi kakovosti najdenih informacij.
Na primer, če je sistemu naročeno, naj ustvari strategijo lansiranja izdelka, se ne zanaša zgolj na poziv, ki natančno določa celoten raziskovalni in odločitveni delovni tok. Namesto tega agentični model samostojno odloča:

1. Pridobiti trenutna poročila o tržnih trendih z uporabo Bing Web Grounding.
2. Prepoznati ustrezne podatke o konkurentih z uporabo Azure AI Search.
3. Povezati zgodovinske notranje prodajne metrike z uporabo Azure SQL Database.
4. Sintetizirati ugotovitve v kohezivno strategijo, orkestrirano prek Azure OpenAI Service.
5. Oceniti strategijo glede vrzeli ali neskladnosti in po potrebi sprožiti nov krog pridobivanja.
Vsi ti koraki—izpopolnjevanje poizvedb, izbira virov, iteracija, dokler ni "zadovoljen" z odgovorom—so odločitve modela, ne vnaprej skriptirane odločitve človeka.

## Iterativne zanke, integracija orodij in spomin

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.sl.png)

Agentični sistem se zanaša na vzorec interakcije v zanki:

- **Začetni klic:** Cilj uporabnika (tj. uporabniški poziv) je predstavljen LLM.
- **Uporaba orodij:** Če model zazna manjkajoče informacije ali dvoumna navodila, izbere orodje ali metodo pridobivanja—na primer poizvedbo vektorske baze podatkov (npr. Azure AI Search Hybrid search nad zasebnimi podatki) ali strukturiran SQL klic—za pridobitev več konteksta.
- **Ocena in izpopolnjevanje:** Po pregledu vrnjenih podatkov model odloči, ali so informacije zadostne. Če ne, izpopolni poizvedbo, poskusi drugo orodje ali prilagodi svoj pristop.
- **Ponavljanje, dokler ni zadovoljen:** Ta cikel se nadaljuje, dokler model ne ugotovi, da ima dovolj jasnosti in dokazov za podajo končnega, dobro utemeljenega odgovora.
- **Spomin in stanje:** Ker sistem ohranja stanje in spomin skozi korake, se lahko spomni prejšnjih poskusov in njihovih rezultatov, s čimer se izogne ponavljajočim se zankam in sprejema bolj informirane odločitve, ko napreduje.

Sčasoma to ustvari občutek razvijajočega se razumevanja, kar omogoča modelu, da se spopada s kompleksnimi, večstopenjskimi nalogami brez potrebe po stalnem človeškem posredovanju ali preoblikovanju poziva.

## Obravnavanje načinov neuspeha in samopopravljanje

Avtonomija Agentic RAG vključuje tudi robustne mehanizme samopopravljanja. Ko sistem naleti na slepe ulice—na primer pridobivanje nepomembnih dokumentov ali nalet na napačne poizvedbe—lahko:

- **Iterira in ponovno poizveduje:** Namesto da bi vrnil nizkovredne odgovore, model poskusi nove strategije iskanja, prepiše poizvedbe v bazo podatkov ali pregleda alternativne nize podatkov.
- **Uporablja diagnostična orodja:** Sistem lahko uporabi dodatne funkcije, zasnovane za pomoč pri odpravljanju napak v korakih razmišljanja ali potrjevanju pravilnosti pridobljenih podatkov. Orodja, kot je Azure AI Tracing, bodo pomembna za omogočanje robustne opazljivosti in spremljanja.
- **Zanaša se na človeški nadzor:** Za scenarije z visokim tveganjem ali ponavljajoče se neuspehe lahko model označi negotovost in zahteva človeško usmerjanje. Ko človek poda korektivne povratne informacije, lahko model to lekcijo vključi v prihodnje.

Ta iterativen in dinamičen pristop omogoča modelu, da se nenehno izboljšuje, kar zagotavlja, da ni le sistem za enkratno uporabo, temveč tak, ki se uči iz svojih napak med posamezno sejo.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.sl.png)

## Meje agentnosti

Kljub svoji avtonomiji znotraj naloge Agentic RAG ni enakovreden splošni umetni inteligenci. Njegove "agentične" sposobnosti so omejene na orodja, vire podatkov in politike, ki jih določijo človeški razvijalci. Ne more si izmisliti lastnih orodij ali preseči meja domen, ki so bile določene. Namesto tega odlično obvladuje dinamično orkestracijo razpoložljivih virov.
Ključne razlike od bolj naprednih oblik umetne inteligence vključujejo:

1. **Avtonomija, specifična za domeno:** Sistemi Agentic RAG so osredotočeni na doseganje ciljev, ki jih določi uporabnik, znotraj znane domene, pri čemer uporabljajo strategije, kot sta prepisovanje poizvedb ali izbira orodij za izboljšanje rezultatov.
2. **Odvisnost od infrastrukture:** Zmožnosti sistema so odvisne od orodij in podatkov, ki jih integrirajo razvijalci. Brez človeškega posredovanja ne more preseči teh meja.
3. **Spoštovanje varoval:** Etične smernice, pravila skladnosti in poslovne politike ostajajo zelo pomembne. Svoboda agenta je vedno omejena z varnostnimi ukrepi in mehanizmi nadzora (upajmo?).

## Praktični primeri uporabe in vrednost

Agentic RAG izstopa v scenarijih, ki zahtevajo iterativno izpopolnjevanje in natančnost:

1. **Okolja, kjer je pravilnost na prvem mestu:** Pri preverjanju skladnosti, regulativnih analizah ali pravnih raziskavah lahko agentični model večkrat preveri dejstva, se posvetuje z več viri in prepiše poizvedbe, dokler ne poda temeljito preverjenega odgovora.
2. **Kompleksne interakcije z bazami podatkov:** Pri delu s strukturiranimi podatki, kjer poizvedbe pogosto ne uspejo ali potrebujejo prilagoditev, lahko sistem samostojno izpopolni svoje poizvedbe z uporabo Azure SQL ali Microsoft Fabric OneLake, kar zagotavlja, da končno pridobivanje ustreza uporabnikovemu namenu.
3. **Razširjeni delovni tokovi:** Daljše seje se lahko razvijajo, ko se pojavijo nove informacije. Agentic RAG lahko nenehno vključuje nove podatke in spreminja strategije, ko se več nauči o problematičnem prostoru.

## Upravljanje, preglednost in zaupanje

Ker ti sistemi postajajo bolj avtonomni v svojem razmišljanju, so upravljanje in preglednost ključnega pomena:

- **Razložljivo razmišljanje:** Model lahko zagotovi revizijsko sled poizvedb, ki jih je izvedel, virov, ki jih je uporabil, in korakov razmišljanja, ki jih je sprejel za dosego zaključka. Orodja, kot sta Azure AI Content Safety in Azure AI Tracing / GenAIOps, lahko pomagajo ohranjati preglednost in zmanjševati tveganja.
- **Nadzor pristranskosti in uravnoteženo pridobivanje:** Razvijalci lahko prilagodijo strategije pridobivanja, da zagotovijo, da so upoštevani uravnoteženi, reprezentativni viri podatkov, in redno preverjajo rezultate, da zaznajo pristranskost ali pristranske vzorce z uporabo prilagojenih modelov za napredne organizacije za podatkovne znanosti z uporabo Azure Machine Learning.
- **Človeški nadzor in skladnost:** Pri občutljivih nalogah ostaja človeški pregled bistven. Agentic RAG ne nadomešča človeške presoje pri odločitvah z visokim tveganjem—jo dopolnjuje z zagotavljanjem bolj temeljito preverjenih možnosti.

Imeti orodja, ki zagotavljajo jasen zapis dejanj, je bistveno. Brez njih je odpravljanje napak v večstopenjskem procesu lahko zelo težavno. Oglejte si naslednji primer iz podjetja Literal AI (podjetje za Chainlit) za zagon agenta:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.sl.png)

## Zaključek

Agentic RAG predstavlja naravno evolucijo v tem, kako sistemi umetne inteligence obravnavajo kompleksne, podatkovno intenzivne naloge. S sprejetjem vzorca interakcije v zanki, samostojno izbiro orodij in izpopolnjevanjem poizvedb, dokler ne doseže visokokakovostnega rezultata, sistem presega statično sledenje pozivom in postane bolj prilagodljiv, kontekstno zavedajoč se odločevalec. Čeprav je še vedno omejen z infrastrukturo, ki jo določijo ljudje, in etičnimi smernicami, te agentične sposobnosti omogočajo bogatejše, bolj din
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementacija pridobivanja z izboljšano generacijo (RAG) z Azure OpenAI Service: Naučite se uporabljati svoje podatke z Azure OpenAI Service. Ta modul Microsoft Learn ponuja celovit vodnik za implementacijo RAG  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Vrednotenje aplikacij generativne umetne inteligence z Azure AI Foundry: Ta članek obravnava vrednotenje in primerjavo modelov na javno dostopnih podatkovnih zbirkah, vključno z aplikacijami Agentic AI in arhitekturami RAG</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Kaj je Agentic RAG | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Celovit vodnik za pridobivanje z izboljšano generacijo na osnovi agentov – Novice iz generacije RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: pospešite svoj RAG z reformulacijo poizvedb in samopoizvedovanjem! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodajanje agentnih slojev v RAG</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Prihodnost asistentov za znanje: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako zgraditi sisteme Agentic RAG</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Uporaba Azure AI Foundry Agent Service za skaliranje vaših AI agentov</a>  

### Akademski članki  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno izboljševanje s samopovratnimi informacijami</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezikovni agenti z verbalnim krepitvenim učenjem</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezikovni modeli se lahko sami popravijo z orodji za interaktivno kritiko</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Pregled o Agentic RAG</a>  

## Prejšnja lekcija  

[Vzorec oblikovanja uporabe orodij](../04-tool-use/README.md)  

## Naslednja lekcija  

[Gradnja zaupanja vrednih AI agentov](../06-building-trustworthy-agents/README.md)  

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.