# Mälu AI agentidele 
[![Agent Memory](../../../translated_images/et/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kui arutatakse AI agentide loomise unikaalsete eeliste üle, räägitakse peamiselt kahest asjast: võimest kutsuda tööriistu ülesannete täitmiseks ja võimest aja jooksul paraneda. Mälu on iseparaneva agendi loomise alus, mis suudab meie kasutajatele paremaid kogemusi pakkuda.

Selles õppetükis vaatleme, mis on mälu AI agentide jaoks ja kuidas me seda hallata ning oma rakenduste kasuks kasutada saame.

## Sissejuhatus

See õppetükk katab:

• **AI agendi mälu mõistmine**: Mis on mälu ja miks see agentidele oluline on.

• **Mälu rakendamine ja salvestamine**: Praktilised meetodid mäluvõimaluste lisamiseks oma AI agentidele, keskendudes lühiajalisele ja pikaajalisele mälule.

• **AI agentide iseparandamine**: Kuidas mälu võimaldab agentidel õppida varasematest suhtlustest ja aja jooksul paremaks saada.

## Saadaval rakendused

See õppetükk sisaldab kahte põhjalikku märkmikujuhendit:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mälu rakendamine Mem0 ja Azure AI Search abil Microsoft Agent Frameworkis

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Struktureeritud mälu rakendamine Cognee abil, mis ehitab automaatselt teadmiste graafi põhinevalt manustel, visualiseerib graafi ja võimaldab nutikat päringut

## Õpieesmärgid

Pärast selle õppetüki lõpetamist tead, kuidas:

• **Erinevaid AI agendi mälutüüpe eristada**, sealhulgas töömälu, lühiajalist ja pikaajalist mälu ning spetsialiseeritud vorme nagu isiku- ja episoodimälu.

• **Rakendada ja hallata lühiajalist ja pikaajalist mälu AI agentidele** Microsoft Agent Frameworki abil, kasutades tööriistu nagu Mem0, Cognee, Whiteboard mälu ning integreerides Azure AI Searchiga.

• **Mõista iseparanevate AI agentide põhimõtteid** ja kuidas tugevad mäluhaldussüsteemid aitavad kaasa pidevale õppimisele ja kohanemisele.

## AI agendi mälu mõistmine

Põhimõtteliselt tähendab **mälu AI agentide jaoks mehhanisme, mis võimaldavad neil infot salvestada ja meenutada**. See info võib olla konkreetseid detaile vestlusest, kasutaja eelistusi, varasemaid tegevusi või isegi õpitud mustreid.

Ilma mäluta on AI rakendused sageli olekuta, mis tähendab, et iga suhtlus algab nullist. See viib korduva ja pettumust valmistava kasutajakogemuseni, kus agent "unustab" varasema konteksti või eelistused.

### Miks mälu on oluline?

Agendi intelligentsus on sügavalt seotud tema võimega meenutada ja kasutada varasemat informatsiooni. Mälu võimaldab agentidel olla:

• **Peegelduv**: Õppida varasematest tegevustest ja tulemustest.

• **Interaktiivne**: Säilitada konteksti kestva vestluse vältel.

• **Proaktiivne ja reaktiivne**: Ennustada vajadusi või reageerida ajalooliste andmete põhjal sobivalt.

• **Sõltumatu**: Tegutseda iseseisvamalt, tuginedes salvestatud teadmistele.

Mälu rakendamise eesmärk on muuta agendid rohkem **usaldusväärseks ja võimekaks**.

### Mälu tüübid

#### Töömälu

Seda võib mõelda kui märkmepaberit, mida agent kasutab ühe käimasoleva ülesande või mõttekäigu ajal. See hoiab käesolevast hetkest vajalikku infot järgmise sammu arvutamiseks.

AI agentide puhul haarab töömälu sageli vestluse kõige olulisema info, isegi kui kogu vestluse ajalugu on pikk või kärbitud. Keskendutakse võtmeelementide nagu nõuded, ettepanekud, otsused ja tegevused väljavõtmisele.

**Töömälu näide**

Reisibroneerimise agendi puhul võib töömälu haarata kasutaja praeguse taotluse, nagu "Ma tahan broneerida reisi Pariisi". See konkreetne nõue hoitakse agendi otseses kontekstis, et juhendada käimasolevat suhtlust.

#### Lühiajaline mälu

See mälu tüüp säilitab infot ühe vestluse või seansi kestel. See on praeguse vestluse kontekst, mis võimaldab agenti tagasi viidata varasematele dialoogi vahetustele.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK näidetes vastab see `AgentSession`-ile, mis luuakse käsuga `agent.create_session()`. Seanss on raamistikus sisseehitatud lühiajaline mälu: see hoiab vestluse konteksti kättesaadavana seni, kuni sama seanssi kasutatakse, kuid see kontekst ei säili, kui seanss lõpeb või rakendus taaskäivitub. Faktiliste ja eelistuste säilitamiseks, mis peavad püsima seansside vahel, kasutatakse pikaajalist mälu, tavaliselt andmebaasi, vektoriindeksi või muu püsiva hoidla kaudu.

**Lühiajalise mälu näide**

Kui kasutaja küsib: "Kui palju maksab lend Pariisi?" ja seejärel lisab "Mis saab majutuse kohta seal?", siis lühiajaline mälu tagab, et agent teab, et "seal" viitab samas vestluses "Pariisi".

#### Pikaajaline mälu

See on info, mis püsib üle mitme vestluse või seansi. See võimaldab agentidel meeles pidada kasutaja eelistusi, ajaloolisi suhtlusi või üldteadmisi pikema aja vältel. See on oluline personaliseerimise jaoks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et "Ben naudib suusatamist ja õues tegevusi, meeldib kohvi joosta mäenägudega ja tahab vältida keerukaid suusaradu varasema vigastuse tõttu". See info, mis on saadud varasematest suhtlustest, mõjutab soovitusi tulevastes reisi planeerimise sessioonides ja teeb need kõrgelt personaliseerituks.

#### Isikumälu

See spetsialiseeritud mälutüüp aitab agendil arendada järjekindlat "isiksust" või "persona". See võimaldab agenti end meenutada üksikasju iseenda või oma kavandatud rolli kohta, muutes suhtluse sujuvamaks ja keskendunumaks.

**Isikumälu näide**

Kui reisibüroo agent on kujundatud kui "ekspert suusareiside planeerija", siis isikumälu võib tugevdada seda rolli, mõjutades vastuseid vastavalt eksperdi toonile ja teadmistele.

#### Töötöötlus-/episoodimälu

See mälu salvestab sündmuste jada, mida agent teeb keeruka ülesande täitmisel, kaasa arvatud õnnestumised ja ebaõnnestumised. See on nagu konkreetsete "episoodide" või varasemate kogemuste meenutamine, et neist õppida.

**Episoodimälu näide**

Kui agent proovis broneerida konkreetset lendu, kuid see ebaõnnestus kättesaamatuse tõttu, võib episoodimälu selle ebaõnnestumise salvestada, võimaldades agendil proovida alternatiivseid lende või teavitada kasutajat probleemist teadlikumal viisil järgmisel katsel.

#### Üksuse mälu

See hõlmab konkreetsete üksuste (näiteks inimeste, kohtade või asjade) ja sündmuste tuvastamist ja meelde jätmist vestlustest. See võimaldab agendil luua struktureeritud arusaama arutatud võtmetest.

**Üksuse mälu näide**

Vestlusest möödunud reisist võib agent välja tõmmata üksused nagu "Pariis", "Eiffeli torn" ja "õhtusöök restoranis Le Chat Noir". Tulevases suhtluses võib agent meeles pidada "Le Chat Noir'i" ja pakkuda teha seal uue broneeringu.

#### Struktureeritud RAG (Retrieval Augmented Generation)

Kuigi RAG on laiem tehnika, on "Struktureeritud RAG" esile tõstetud kui võimas mälutehnoloogia. See ekstraheerib tihedat, struktureeritud informatsiooni erinevatest allikatest (vestlused, e-kirjad, pildid) ja kasutab seda vastuste täpsuse, meenutuse ja kiiruse parandamiseks. Erinevalt klassikalisest RAG-ist, mis tugineb vaid semantilisele sarnasusele, töötab Struktureeritud RAG info loomuliku struktuuriga.

**Struktureeritud RAG näide**

Sõnade sobitamise asemel võib Struktureeritud RAG töödelda lennuandmeid (sihtkoht, kuupäev, kellaaeg, lennufirma) e-kirjast ja salvestada need struktureeritud kujul. See võimaldab täpseid päringuid nagu "Millise lennu ma teisipäeval Pariisi broneerisin?"

## Mälu rakendamine ja salvestamine

AI agentide mälu rakendamine nõuab süsteemset protsessi, mida nimetatakse **mäluhalduseks**, mis hõlmab info genereerimist, salvestamist, päringut, integreerimist, uuendamist ja isegi unustamist (kustutamist). Päring on eriti oluline osa.

### Spetsialiseeritud mälutööriistad

#### Mem0

Üks viis agentide mälu salvestamiseks ja haldamiseks on kasutada spetsiaalseid tööriistu nagu Mem0. Mem0 toimib püsiva mälukihtina, võimaldades agentidel meenutada asjakohaseid suhtlusi, salvestada kasutaja eelistusi ja faktilist konteksti ning õppida aja jooksul õnnestumistest ja ebaõnnestumistest. Idee on muuta olekuta agendid olekuga agentideks.

See töötab läbi **kahefaasilise mälutöötluse: ekstraheerimise ja uuendamise**. Esiteks saadetakse agendi vestluslõimele lisatud sõnumid Mem0 teenusele, mis kasutab suure keelemudelit (LLM) vestluse ajaloo kokkuvõtmiseks ja uute mälestuste ekstraheerimiseks. Järgneb LLM-põhine uuendusfaas, mis otsustab, kas neid mälestusi lisada, muuta või kustutada, salvestades need hübriidandmebaasi, mis võib hõlmata vektoreid, graafi ja võtme-väärtuse andmebaase. See süsteem toetab erinevaid mälutüüpe ja võib kaasata graafimälu üksustevaheliste suhete haldamiseks.

#### Cognee

Teine võimas lähenemine on **Cognee**, avatud lähtekoodiga semantiline mälu AI agentidele, mis teisendab struktureeritud ja struktureerimata andmed päritavateks teadmiste graafideks, mida toetavad manused. Cognee pakub **kaksikhoidla arhitektuuri**, mis ühendab vektorsarnuse otsingu graafisuhetega, võimaldades agentidel mõista mitte ainult, milline info on sarnane, vaid ka kuidas kontseptsioonid omavahel seotud on.

See paistab silma **hübriidse päringu** poolest, mis segab vektorisarnasust, graafistruktuuri ja LLM-i põhjendamist – alates algandmete otsingust kuni graafiteadliku küsimuste vastamiseni. Süsteem säilitab **elava mälu**, mis areneb ja kasvab, jäädes päringuteks kättesaadavaks ühe ühendatud graafina, toetades nii lühiajalist seansikonteksti kui ka pikaajalist püsivat mälu.

Cognee märkmiku juhend ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreerib selle ühtse mälukihti ehitamist, praktiliste näidetega mitmesuguste andmeallikate sissetoomisest, teadmiste graafi visualiseerimisest ja päringutest erinevate otsingustrateegiatega, mis on kohandatud konkreetsete agentide vajadustele.

### Mälu salvestamine RAG-iga

Lisaks spetsialiseeritud mälutööriistadele nagu mem0 saate kasutada tugevaid otsinguteenuseid nagu **Azure AI Search mälu salvestamise ja päringu taustana**, eriti struktureeritud RAG jaoks.

See võimaldab teil juurutada agendi vastused oma andmete põhjal, tagades asjakohasemad ja täpsemad vastused. Azure AI Searchi saab kasutada kasutajapõhiste reisimälestuste, tootekataloogide või muu domeenispetsiifilise teadmiste salvestamiseks.

Azure AI Search toetab võimeid nagu **Struktureeritud RAG**, mis on suurepärane tiheda, struktureeritud info ekstraheerimisel ja päringul suurtest andmekogudest nagu vestlused, e-kirjad või isegi pildid. See pakub "inimeseülese" täpsust ja meenutust võrreldes traditsiooniliste tekstilõikude ja manuste lähenemistega.

## AI agentide iseparanduse võimaldamine

Iseparanevate agentide tavapärane muster hõlmab **"teadmiste agendi"** lisamist. See eraldi agent jälgib peamist kasutajaga vestlust. Selle ülesanne on:

1. **Tuvastada väärtuslik info**: Otsustada, kas vestluse mõni osa on väärt säilitada üldiste teadmistena või konkreetse kasutaja eelistusena.

2. **Ekstraheerida ja kokku võtta**: Välja tuua olulise õppetunni või eelistuse vestlusest.

3. **Salvestada teadmistebaasi**: Salvestada see teave, sageli vektorandmebaasi, et seda saaks hiljem kasutada.

4. **Täiendada tulevasi päringuid**: Kui kasutaja algatab uue päringu, hangib teadmiste agent asjakohase salvestatud info ja lisab selle kasutaja küsimusele, pakkudes olulist konteksti põhiagentile (nagu RAG).

### Mälu optimeerimised

• **Lõtku juhtimine**: Et vältida kasutajaliidese aeglustumist, saab alguses kasutada odavamat ja kiiremat mudelit, mis kontrollib kiiresti, kas info on väärt salvestamist või päringut, kutsudes keerukama ekstraheerimise/päringu protsessi esile vaid vajadusel.

• **Teadmistebaasi hooldus**: Kasvava teadmistebaasi korral saab harvem kasutatava info viia "külma hoiule", et kulusid kontrolli all hoida.

## Kas sul on AI agentide mälu kohta rohkem küsimusi?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), kohtumiseks teiste õppuritega, osalemaks nõuandmetundides ja saades vastused oma AI agentide küsimustele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->