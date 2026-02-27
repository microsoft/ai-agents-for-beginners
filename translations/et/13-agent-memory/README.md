# Mälu tehisintellekti agentidele  
[![Agendi mälu](../../../translated_images/et/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kui arutletakse tehisintellekti agendide loomise erilise kasu üle, käsitletakse peamiselt kahte asja: võimet kasutada tööriistu ülesannete täitmiseks ja võimet aja jooksul paremaks saada. Mälu on aluseks eneseparaneva agendi loomisel, mis suudab meie kasutajatele paremaid kogemusi pakkuda.

Selles õppetükis vaatleme, mis on mälu tehisintellekti agentidele ning kuidas seda hallata ja kasutada meie rakenduste kasuks.

## Sissejuhatus

See õppetükk hõlmab:

• **Tehisintellekti agendi mälu mõistmine**: Mis on mälu ja miks see agentidele oluline on.

• **Mälu rakendamine ja salvestamine**: Praktilised meetodid agendile mälu võimete lisamiseks, keskendudes lühiajalisele ja pikaajalisele mälule.

• **Tehisintellekti agendi eneseparandamine**: Kuidas mälu võimaldab agentidel õppida varasematest tegevustest ja aja jooksul paremaks saada.

## Saadavad rakendused

See õppetükk sisaldab kahte põhjalikku märkmiku juhendit:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mälu rakendamine Mem0 ja Azure AI Search abil Microsoft Agent Frameworkis

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Struktureeritud mälu rakendamine Cognee abil, mis automaatselt koostab teadmiste graafi tagatisega sisestustest, visualiseerib graafi ja teostab intelligentset päringut

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad:

• **Erinevaid tehisintellekti agendi mälutüüpe eristada**, sealhulgas töömälu, lühiajaline ja pikaajaline mälu ning spetsialiseeritud vormid nagu isikupära (persona) ja episoodiline mälu.

• **Rakendada ja hallata lühiajalist ja pikaajalist mälu tehisintellekti agentidele** kasutades Microsoft Agent Frameworki ja tööriistu nagu Mem0, Cognee, Whiteboard-mälu ning integreerides Azure AI Searchiga.

• **Mõista eneseparanduvate tehisintellekti agendi põhimõtteid** ja kuidas tugevad mäluhaldussüsteemid aitavad kaasa pidevale õppimisele ja kohanemisele.

## Tehisintellekti agendi mälu mõistmine

Põhimõtteliselt tähendab **mälu tehisintellekti agentidele mehhanisme, mis võimaldavad neil säilitada ja meenutada teavet**. See teave võib olla detailid vestlusest, kasutaja eelistused, varasemad tegevused või isegi õpitud mustrid.

Ilma mäluta on tehisintellekti rakendused sageli olekuta, st iga suhtlus algab nullist. See toob kaasa korduva ja frustratsiooni tekitava kasutajakogemuse, kus agent "unustab" eelneva konteksti või eelistused.

### Miks mälu on oluline?

Agendi intellekt on tihedalt seotud selle võimega meenutada ja kasutada varasemat teavet. Mälu võimaldab agentidel olla:

• **Mõtisklev**: Õppida varasematest tegevustest ja tulemustest.

• **Interaktiivne**: Säilitada konteksti jooksva vestluse jooksul.

• **Proaktiivne ja reaktiivne**: Eeldada vajadusi või vastata asjakohaselt ajaloolise info põhjal.

• **Autonoomne**: Tegutseda iseseisvamalt tuginedes salvestatud teadmistel.

Mälu rakendamise eesmärk on muuta agendid usaldusväärsemaks ja võimekamaks.

### Mälu tüübid

#### Töömälu

Mõtle sellele kui visandpaberile, mida agent kasutab ühe jätkuva ülesande või mõttekäigu ajal. See hoiab kohest informatsiooni järgmise sammu arvutamiseks.

Tehisintellekti agentide puhul hõlmab töömälu sageli enim asjakohast infot vestlusest, isegi kui kogu vestluse ajalugu on pikk või kärbitud. See keskendub võtmeelementide nagu nõuded, ettepanekud, otsused ja tegevused väljavõtmisele.

**Töömälu näide**

Reisibroneerimise agendi puhul võib töömälu hoida jooksva kasutajasoovi, näiteks "Ma tahan broneerida reisi Pariisi". See konkreetne nõue hoitakse agendi koheses kontekstis, et juhendada praegust suhtlust.

#### Lühiajaline mälu

See mälu tüüp säilitab infot ühe vestluse või sessiooni jooksul. See on praeguse vestluse kontekst, mis võimaldab agendil viidata varasematele dialoogi voorudele.

**Lühiajalise mälu näide**

Kui kasutaja küsib "Kui palju maksaks lend Pariisi?" ja siis lisab "Ent kuidas on seal majutusega?", tagab lühiajaline mälu, et agent teab, et "seal" tähendab "Pariisi" selles samas vestluses.

#### Pikaajaline mälu

See on info, mis püsib üle mitme vestluse või sessiooni. See võimaldab agentidel mäletada kasutaja eelistusi, ajaloolisi suhtlusi või üldteadmisi pikema aja jooksul. See on oluline personaliseerimiseks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et "Ben naudib suusatamist ja välitegevusi, talle meeldib kohv mägivaatega ning ta soovib vältida keerulisi suusaradu varasema vigastuse tõttu". See info, õpitud eelnevate suhtluste käigus, mõjutab tulevasi reisiplaani soovitusi, muutes need väga isikupäraseks.

#### Isikupära mälu (Persona Memory)

See spetsialiseeritud mälu tüüp aitab agendil kujundada järjepideva "isikupära" või "persona". See võimaldab agentidel mäletada detaile enda või oma rolli kohta, muutes suhtluse sujuvamaks ja fokusseeritumaks.

**Isikupära mälu näide**  
Kui reisibroneerimise agent on loodud kui "ekspert suusaplaneerija", võib isikupära mälu seda rolli tugevdada, mõjutades vastuseid vastavalt eksperdi toonile ja teadmistele.

#### Töövoo/Episoodiline mälu

See mälu salvestab sammude järjekorra, mille agent võtab keerulise ülesande täitmisel, sealhulgas õnnestumised ja ebaõnnestumised. See on nagu meenutada konkreetseid "episoodid" või varasemaid kogemusi, et neist õppida.

**Episoodilise mälu näide**

Kui agent üritas broneerida kindlat lendu, kuid see ebaõnnestus kättesaadavuse puudumise tõttu, võib episoodiline mälu selle ebaõnnestumise salvestada, võimaldades agendil proovida alternatiivseid lende või teavitada kasutajat probleemist paremini järgmisel katsel.

#### Olemise mälu (Entity Memory)

See hõlmab konkreetsete üksuste (nagu inimesed, kohad või asjad) ja sündmuste väljavõtmist ja meeldejätmist vestlustest. See võimaldab agendil luua struktureeritud arusaama olulistest käsitletud elementidest.

**Olemise mälu näide**

Vestlusest eelmise reisi kohta võib agent välja võtta üksused nagu "Pariis", "Eiffeli torn" ja "õhtusöök restoranis Le Chat Noir". Tulevases suhtluses võiks agent meenutada "Le Chat Noir'i" ja pakkuda seal uut broneeringut teha.

#### Struktureeritud RAG (Retrieval Augmented Generation)

Kuigi RAG on laiem tehnika, on "Struktureeritud RAG" esile toodud kui võimas mälutehnoloogia. See võtab tihedat, struktureeritud infot erinevatest allikatest (vestlustest, meilidest, piltidest) ja kasutab seda täpsuse, meenutamise ja kiiruse parandamiseks vastustes. Erinevalt klassikalisest RAG-st, mis tugineb ainult semantilisele sarnasusele, töötab Struktureeritud RAG info loomuliku struktuuriga.

**Struktureeritud RAG näide**

Selle asemel, et lihtsalt märksõnu sobitada, võiks Struktureeritud RAG parsida lennuandmed (sihtkoht, kuupäev, kellaaeg, lennufirma) meililt ja salvestada need struktureeritud vormis. See võimaldab täpseid päringuid nagu "Millise lennu broneerisin Pariisi teisipäeval?"

## Mälu rakendamine ja salvestamine

Mälu rakendamine tehisintellekti agentidele hõlmab süsteemset protsessi nimega **mäluhaldus**, mis sisaldab info genereerimist, salvestamist, päringut, integreerimist, uuendamist ja isegi "unustamist" (või kustutamist). Päring on eriti oluline osa.

### Spetsialiseeritud mälutööriistad

#### Mem0

Üks viis agendi mälu salvestamiseks ja haldamiseks on kasutada spetsialiseeritud tööriistu nagu Mem0. Mem0 töötab püsiva mälukihtina, võimaldades agentidel meenutada asjakohaseid vestlusi, salvestada kasutaja eelistusi ja faktide konteksti ning õppida edukusest ja ebaõnnestumistest aja jooksul. Mõte on, et olekuta agendid muutuvad olekuhaldavateks.

See toimib **kahefaasilise mälupipeline'i kaudu: väljavõte ja uuendus**. Esiteks saadetakse agenti vestlusele lisatud sõnumid Mem0 teenusele, mis kasutab suurt keelemudelit (LLM) vestluse ajaloo kokkuvõtmiseks ja uute mälude väljavõtmiseks. Järgmiseks määrab LLM-käitatud uuendusfaas, kas need mälud lisada, muuta või kustutada, salvestades need hübriidandmebaasi, mis võib hõlmata vektor-, graafi- ja võtme-väärtuse andmebaase. See süsteem toetab ka erinevaid mälutüüpe ning võib integreerida graafimälu, et hallata suhete omavahelisi seoseid.

#### Cognee

Teine võimas lähenemine on kasutada **Cogneed**, avatud lähtekoodiga semantilist mälu tehisintellekti agentidele, mis muudab struktureeritud ja struktureerimata andmed päringuteks mõeldud teadmiste graafideks, millele toetuvad sisestused. Cognee pakub **kahepoodilist arhitektuuri**, mis ühendab vektorite sarnasuse otsingu graafisuhetega, võimaldades agentidel mõista mitte ainult sarnasust, vaid ka kontseptsioonide omavahelisi suhteid.

See on võimas **hübriidpäring**, mis segab vektorite sarnasust, graafistruktuuri ja LLM-i mõtlemist – alates tükipõhisest otsingust kuni graafiteadliku küsimustele vastamiseni. Süsteem säilitab **elava mälu**, mis areneb ja kasvab, kuid jääb samas ühtseks päringuks ühendatud graafina, toetades nii lühiajalist sessiooni konteksti kui ka pikaajalist püsivat mälu.

Cognee märkmiku juhend ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreerib selle ühtse mälukihi ehitamist praktiliste näidetega erinevate andmeallikate sissepaigutamisest, teadmiste graafi visualiseerimisest ja erinevate otsingustrateegiate kasutamisest vastavalt konkreetse agendi vajadustele.

### Mälu salvestamine RAG-i abil

Lisaks spetsialiseeritud muistööriistadele nagu Mem0, võid kasutada usaldusväärseid otsinguteenuseid nagu **Azure AI Search mälu salvestamiseks ja pärimiseks**, eriti struktureeritud RAG puhul.

See võimaldab sul maandada agendi vastuseid oma andmetega, tagades asjakohasemad ja täpsemad vastused. Azure AI Searchi saab kasutada kasutajapõhiste reisimälude, tooteloendite või muu domeenispetsiifilise teadmise hoidmiseks.

Azure AI Search toetab funktsioone nagu **Struktureeritud RAG**, mis on osav tiheda, struktureeritud info väljavõtmisel ja pärimisel suurtest andmekogumitest nagu vestluse ajalugu, meilid või isegi pildid. See võimaldab "üliinimlikku täpsust ja meenutamist" võrreldes traditsioonilise tekstitükkide ja sisestuste kasutamisega.

## Tehisintellekti agendi eneseparandamine

Levinud eneseparanduvate agentide muster hõlmab **"teadmiste agendi"** lisamist. See eraldiseisev agent jälgib kasutaja ja peamise agendi vahelist vestlust. Selle ülesandeks on:

1. **Tuvastada väärtuslik info**: Mõista, kas mõni vestluse osa tasub salvestada üldiseks teadmiseks või konkreetseks kasutaja eelistuseks.

2. **Väljavõte ja kokkuvõte**: Tuletada vestlusest oluline õppetund või eelistus.

3. **Salvestamine teadmiste baasi**: Säilitada see info, sageli vektoriandmebaasis, et seda hiljem pärida.

4. **Tulevaste päringute täiendamine**: Kui kasutaja algatab uue päringu, pärib teadmiste agent asjakohase info ja lisab selle kasutaja sisendile, pakkudes peamisele agendile olulist konteksti (sarnaselt RAG-ile).

### Mälu optimeerimine

• **Latentsuse haldamine**: Kasutajasuhtluse aeglustumise vältimiseks saab alguses kasutada odavamat, kiiremat mudelit, mis kiiresti kontrollib, kas info on salvestamist või pärimist väärt, kutsudes keerukama väljavõtte-/päringuprotsessi esile vaid vajadusel.

• **Teadmiste baasi hooldus**: Kasvava teadmiste baasi puhul saab harvem kasutatava info üle viia "külma hoiustamisse", et kulusid hallata.

## Kas sul on rohkem küsimusi agendi mälu kohta?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda nõuandmistundides ja saada vastuseid oma tehisintellekti agentide küsimustele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtikirjutus**:
See dokument on tõlgitud kasutades tehisintellekti tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse või valesti mõistmise eest, mis võib tekkida selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->