[![Agentic RAG](../../../translated_images/sl/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Agentic RAG

Ta lekcija ponuja celovit pregled Agentic Retrieval-Augmented Generation (Agentic RAG), nastajajočega AI paradigma, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov. V nasprotju s statičnimi vzorci pridobivanja in nato branja, Agentic RAG vključuje iterativne klice LLM, prekinjene z uporabo orodij ali funkcij in strukturiranih izhodov. Sistem ocenjuje rezultate, izboljšuje poizvedbe, po potrebi kliče dodatna orodja in ta cikel ponavlja, dokler ne doseže zadovoljive rešitve.

## Uvod

Ta lekcija bo obravnavala

- **Razumevanje Agentic RAG:** Spoznajte nastajajoči AI paradigme, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih podatkovnih virov.
- **Razumevanje iterativnega maker-checker sloga:** Spoznajte zanko iterativnih klicev LLM, prekinjenih z orodji ali funkcijami in strukturiranimi izhodi, ki so namenjeni izboljšanju pravilnosti in obravnavi neustreznih poizvedb.
- **Raziskovanje praktičnih aplikacij:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, usmerjena k pravilnosti, kompleksne interakcije z bazami podatkov in razširjeni delovni tokovi.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:

- **Razumevanje Agentic RAG:** Spoznajte nastajajoči AI paradigme, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih podatkovnih virov.
- **Iterativni maker-checker slog:** Razumite koncept zanke iterativnih klicev LLM, prekinjenih z orodji ali funkcijami in strukturiranimi izhodi, namenjenih izboljšanju pravilnosti in obravnavi neustreznih poizvedb.
- **Obvladovanje procesa razmišljanja:** Razumite sistemsko zmožnost prevzema nadzora nad lastnim procesom razmišljanja, sprejemanja odločitev o pristopu k težavam brez odvisnosti od vnaprej določenih poti.
- **Delovni tok:** Razumite, kako agentni model samostojno odloča o pridobivanju poročil o tržnih trendih, prepoznavanju podatkov konkurentov, korelaciji notranjih prodajnih metrik, sintezi ugotovitev in ocenjevanju strategije.
- **Iterativne zanke, integracija orodij in pomnilnik:** Spoznajte sistem, ki temelji na vzorcu zanke, ki ohranja stanje in pomnilnik skozi korake, da prepreči ponavljajoče se zanke in omogoči premišljeno odločanje.
- **Obravnava načinov napak in samopopravki:** Raziščite robustne mehanizme samopopravka sistema, vključno z iteracijami in ponovnimi poizvedbami, uporabo diagnostičnih orodij in oporo človeškemu nadzoru.
- **Meje agencije:** Razumite omejitve Agentic RAG, osredotočene na domensko specifiko avtonomije, odvisnost od infrastrukture in spoštovanje varnostnih omejitev.
- **Praktični primeri uporabe in vrednost:** Prepoznajte scenarije, kjer Agentic RAG izstopa, kot so okolja, usmerjena k pravilnosti, kompleksne interakcije z bazami podatkov in razširjeni delovni tokovi.
- **Upravljanje, preglednost in zaupanje:** Spoznajte pomen upravljanja in preglednosti, vključno z razložljivim razmišljanjem, nadzorom pristranskosti in človeškim nadzorom.

## Kaj je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nastajajoči AI paradigma, kjer veliki jezikovni modeli (LLM) samostojno načrtujejo svoje naslednje korake, medtem ko pridobivajo informacije iz zunanjih virov. V nasprotju s statičnimi vzorci pridobivanja in nato branja, Agentic RAG vključuje iterativne klice LLM, prekinjene z uporabo orodij ali funkcij in strukturiranih izhodov. Sistem ocenjuje rezultate, izboljšuje poizvedbe, po potrebi kliče dodatna orodja in ta cikel ponavlja, dokler ne doseže zadovoljive rešitve. Ta iterativni “maker-checker” slog izboljšuje pravilnost, obravnava neustrezne poizvedbe in zagotavlja rezultate visoke kakovosti.

Sistem aktivno prevzema nadzor nad svojim procesom razmišljanja, prepisuje neuspešne poizvedbe, izbira različne načine pridobivanja informacij in vključuje več orodij—kot so vektorsko iskanje v Azure AI Search, SQL baze podatkov ali lastni API-ji—preden dokončno odgovori. Značilnost agentnega sistema je zmožnost prevzema nadzora nad lastnim procesom razmišljanja. Tradicionalne RAG implementacije zaupajo vnaprej določenim potem, medtem ko agentni sistem samostojno določi zaporedje korakov glede na kakovost najdenih informacij.

## Opredelitev Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nastajajoči razvojni AI paradigma, kjer LLM ne zgolj pridobivajo informacije iz zunanjih podatkovnih virov, ampak tudi samostojno načrtujejo svoje naslednje korake. V nasprotju s statičnimi vzorci pridobivanja in nato branja ali skrbno napisanim zaporedjem pozivov, Agentic RAG vključuje zanko iterativnih klicev LLM, prekinjenih z uporabo orodij ali funkcij in strukturiranih izhodov. Ob vsakem koraku sistem ocenjuje pridobljene rezultate, odloča, ali naj izboljša poizvedbe, po potrebi kliče dodatna orodja in ta cikel ponavlja, dokler ne doseže zadovoljive rešitve.

Ta iterativni “maker-checker” slog delovanja je namenjen izboljšanju pravilnosti, obravnavi neustreznih poizvedb do strukturiranih baz podatkov (npr. NL2SQL) in zagotavljanju uravnoteženih, kakovostnih rezultatov. Namesto da bi se zanašal zgolj na skrbno zasnovane verige pozivov, sistem aktivno prevzema nadzor nad procesom razmišljanja. Lahko prepiše neuspele poizvedbe, izbere različne metode pridobivanja in vključi več orodij—kot so vektorsko iskanje v Azure AI Search, SQL baze podatkov ali lastni API-ji—preden dokončno odgovori. To odpravlja potrebo po pretirano zapletenih orkestracijskih okvirjih. Namesto tega lahko razmeroma preprosta zanka “klic LLM → uporaba orodja → klic LLM → …” prinese sofisticirane in dobro utemeljene izhode.

![Agentic RAG Core Loop](../../../translated_images/sl/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Prevzem nadzora nad procesom razmišljanja

Značilna lastnost, ki sistem naredi “agentnega”, je njegova zmožnost prevzema nadzora nad lastnim procesom razmišljanja. Tradicionalne RAG implementacije pogosto zanašajo na ljudi, ki vnaprej določijo pot za model: verigo misli, ki določa, kaj pridobiti in kdaj.
Toda ko je sistem resnično agenten, interno odloča, kako pristopiti k problemu. Ne izvaja zgolj skripta; samostojno določi zaporedje korakov na podlagi kakovosti informacij, ki jih najde.
Na primer, če ga vprašajo, naj ustvari strategijo lansiranja izdelka, se ne zanaša zgolj na poziv, ki opiše celoten proces raziskav in odločanja. Namesto tega agentni model samostojno odloča, da bo:

1. Pridobil aktualna poročila o tržnih trendih z uporabo Bing Web Grounding
2. Prepoznal ustrezne podatke o konkurenci z uporabo Azure AI Search.
3. Koreliral zgodovinske notranje prodajne metrike z uporabo Azure SQL Database.
4. Sintetiziral ugotovitve v kohezivno strategijo, orkestrirano preko Azure OpenAI Service.
5. Ocenil strategijo glede vrzeli ali nedoslednosti, po potrebi sprožil nov krog pridobivanja informacij.
Vse te korake—izboljševanje poizvedb, izbira virov, ponavljanje dokler ni “zadovoljen” z odgovorom—odloči model, ne človek, ki je vnaprej pripravil skript.

## Iterativne zanke, integracija orodij in pomnilnik

![Tool Integration Architecture](../../../translated_images/sl/tool-integration.0f569710b5c17c10.webp)

Agentni sistem temelji na vzorcu zanke interakcij:

- **Začetni klic:** Cilj uporabnika (t.j. uporabniški poziv) se predstavi LLM.
- **Klic orodja:** Če model zazna manjkajoče informacije ali nejasna navodila, izbere orodje ali metodo pridobivanja—kot je poizvedba v vektorski bazi (npr. Azure AI Search Hibridno iskanje po zasebnih podatkih) ali strukturiran klic SQL, da zbere več konteksta.
- **Ocenjevanje in izboljševanje:** Po pregledu vrnjenih podatkov model odloči, ali je informacija zadostna. Če ne, izboljša poizvedbo, preizkusi drugo orodje ali prilagodi svoj pristop.
- **Ponovi dokler ni zadovoljen:** Ta cikel traja, dokler model ne ugotovi, da ima dovolj jasnosti in dokazov za podajanje končnega, dobro utemeljenega odgovora.
- **Pomnilnik in stanje:** Ker sistem ohranja stanje in pomnilnik skozi korake, se lahko spomni preteklih poskusov in njihovih rezultatov, kar preprečuje ponavljajoče se zanke in omogoča bolj premišljene odločitve med napredovanjem.

S časom to ustvarja občutek razvijajočega se razumevanja, kar omogoča modelu, da brez stalnega poseganja človeka ali preoblikovanja pozivov upravlja kompleksne, večstopenjske naloge.

## Obravnava načinov napak in samopopravki

Avtonomija Agentic RAG vključuje tudi robustne mehanizme samopopravka. Ko sistem naleti na slepe ulice—kot so pridobivanje nepomembnih dokumentov ali naleti na neustrezne poizvedbe—lahko:

- **Iterira in ponovi poizvedbo:** Namesto da bi vrnil nizko kakovosten odgovor, model poskuša nove iskalne strategije, prepiše poizvedbe baz podatkov ali razišče alternativne podatkovne nize.
- **Uporablja diagnostična orodja:** Sistem lahko pokliče dodatne funkcije, namenjene pomaganju pri odpravljanju napak v njegovih korakih razmišljanja ali potrditvi pravilnosti pridobljenih podatkov. Orodja, kot je Azure AI Tracing, bodo pomembna za omogočanje robustnega opazovanja in nadzora.
- **Se opira na človeški nadzor:** Pri visoko tveganih ali večkrat neuspešnih scenarijih lahko model označi negotovost in zahteva človeško usmerjanje. Ko človeški uporabnik poda korektivno povratno informacijo, jo model lahko vključi za nadaljnje delovanje.

Ta iterativni in dinamični pristop modelu omogoča stalno izboljševanje, pri čemer ni zgolj enkratni sistem, ampak tak, ki se uči iz napak med samo sejo.

![Self Correction Mechanism](../../../translated_images/sl/self-correction.da87f3783b7f174b.webp)

## Meje agencije

Kljub svoji avtonomiji znotraj naloge Agentic RAG ni enakovreden umetni splošni inteligenci. Njegove “agentne” sposobnosti so omejene na orodja, podatkovne vire in politike, ki jih zagotovijo človeški razvijalci. Ne more si izmisliti lastnih orodij ali stopiti izven domenskih meja, ki so bile postavljene. Raje izstopa v dinamični orkestraciji razpoložljivih virov.
Ključne razlike v primerjavi z bolj naprednimi oblikami AI vključujejo:

1. **Domensko specifična avtonomija:** Agentni RAG sistemi so osredotočeni na doseganje ciljev, ki jih določi uporabnik znotraj znane domene, pri čemer uporabljajo strategije kot so prepisovanje poizvedb ali izbira orodij za izboljšanje rezultatov.
2. **Odvisnost od infrastrukture:** Zmožnosti sistema so odvisne od orodij in podatkov, ki jih vključijo razvijalci. Brez človeškega posega ne more preseči teh meja.
3. **Spoštovanje varnostnih omejitev:** Etična pravila, norme skladnosti in poslovne politike ostajajo zelo pomembne. Svoboda agenta je vedno omejena z varnostnimi ukrepi in mehanizmi nadzora (upajmo).

## Praktični primeri uporabe in vrednost

Agentic RAG izstopa v scenarijih, ki zahtevajo iterativno izboljševanje in natančnost:

1. **Okolja, usmerjena k pravilnosti:** Pri preverjanju skladnosti, regulativnih analizah ali pravnih raziskavah lahko agentni model večkrat preveri dejstva, se posvetuje z več viri in prepiše poizvedbe, dokler ne ustvari temeljito preverjenega odgovora.
2. **Kompleksne interakcije z bazami podatkov:** Ko deluje z strukturiranimi podatki, kjer poizvedbe pogosto ne uspele ali jih je treba prilagoditi, sistem lahko samostojno izboljša poizvedbe z uporabo Azure SQL ali Microsoft Fabric OneLake, s čimer zagotavlja, da pridobivanje ustreza namenu uporabnika.
3. **Razširjeni delovni tokovi:** Daljše seje se lahko razvijajo, ko se pojavljajo novi podatki. Agentic RAG lahko stalno vključuje nove informacije in prilagaja strategije, ko se dozdeva več o problemu.

## Upravljanje, preglednost in zaupanje

Ko sistemi postajajo bolj avtonomni v svojem razmišljanju, sta upravljanje in preglednost ključnega pomena:

- **Razložljivo razmišljanje:** Model lahko zagotovi revizijsko sled poizvedb, ki jih je naredil, virov, ki jih je uporabil, in korakov razmišljanja, ki jih je naredil, da pride do zaključka. Orodja, kot sta Azure AI Content Safety in Azure AI Tracing / GenAIOps, pomagajo ohranjati preglednost in zmanjševati tveganja.
- **Nadzor pristranskosti in uravnoteženo pridobivanje:** Razvijalci lahko prilagodijo strategije pridobivanja, da zagotovijo upoštevanje uravnoteženih, reprezentativnih virov podatkov, in redno pregledujejo izhode za odkrivanje pristranskosti ali izkrivljenih vzorcev z uporabo prilagojenih modelov za napredne znanstvene organizacije, ki uporabljajo Azure Machine Learning.
- **Človeški nadzor in skladnost:** Pri občutljivih nalogah ostaja človeški pregled ključnega pomena. Agentic RAG ne nadomešča človeškega odločanja pri visokotveganih odločitvah—temveč ga dopolnjuje z zagotavljanjem bolj temeljito preverjenih možnosti.

Pomembno je imeti orodja, ki zagotavljajo jasen zapis dejanj. Brez njih je odpravljanje napak v večstopenjskem procesu zelo težavno. Glejte naslednji primer iz Literal AI (podjetja za Chainlit) za zagon agenta:

![AgentRunExample](../../../translated_images/sl/AgentRunExample.471a94bc40cbdc0c.webp)

## Zaključek

Agentic RAG predstavlja naravni razvoj v načinu, kako AI sistemi obravnavajo kompleksne, podatkovno intenzivne naloge. Z uporabo vzorca zanke interakcij, samostojnim izborom orodij in izboljševanjem poizvedb dokler ne dosežejo kakovostnega rezultata, sistem presega statično sledenje pozivom in postane bolj prilagodljiv, kontekstno zavedajoč se odločevalec. Čeprav je še vedno omejen z infrastrukturo, ki jo določijo ljudje, in etičnimi smernicami, te agentne zmožnosti omogočajo bogatejše, bolj dinamične in na koncu bolj uporabne AI interakcije tako za podjetja kot končne uporabnike.

### Imate več vprašanj o Agentic RAG?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, sodelujete na urah pisarne in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementacija Retrieval Augmented Generation (RAG) z Azure OpenAI storitvijo: Naučite se uporabljati svoje lastne podatke z Azure OpenAI storitvijo. Ta modul Microsoft Learn nudi celovit vodič o implementaciji RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Vrednotenje generativnih AI aplikacij z Microsoft Foundry: Članek zajema vrednotenje in primerjavo modelov na javno dostopnih podatkovnih zbirkah, vključno z agentnimi AI aplikacijami in RAG arhitekturami</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Kaj je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Popoln vodič za agentno osnovano Retrieval Augmented Generation – Novice iz generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: pospešite svoj RAG z reformulacijo poizvedb in samopoizvedbo! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodajanje agentnih plasti RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Prihodnost pomočnikov za znanje: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako zgraditi agentne RAG sisteme</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Uporaba Microsoft Foundry Agent Service za razširitev vaših AI agentov</a>

### Akademski članki

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno izboljševanje s samopovratno informacijo</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezikovni agenti z verbalnim krepitvenim učenjem</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezikovni modeli se lahko samopopravljajo z orodjem interaktivne kritike</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Pregled agentnega RAG</a>

## Prejšnja lekcija

[Vzorec uporabe orodja](../04-tool-use/README.md)

## Naslednja lekcija

[Gradnja zaupanja vrednih AI agentov](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->