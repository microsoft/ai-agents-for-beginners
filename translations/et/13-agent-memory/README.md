# Mälu tehisintellekti agentidele 
[![Agent Mälu](../../../translated_images/et/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kui räägitakse unikaalsetest eelistest AI agentide loomisel, arutatakse peamiselt kaht asja: tööriistade kutsumise võime ülesannete täitmiseks ja võime aja jooksul pareneda. Mälu on eneseparaneva agendi loomise alus, mis suudab meie kasutajatele luua paremaid kogemusi.

Selles õppetükis vaatleme, mis on mälu AI agentide jaoks ja kuidas saame seda hallata ning kasutada oma rakenduste hüvanguks.

## Sissejuhatus

See õppetükk hõlmab:

• **AI agendi mälu mõistmine**: mis on mälu ja miks see on agentide jaoks oluline.

• **Mälu rakendamine ja salvestamine**: praktilised meetodid mälu võimete lisamiseks oma AI agentidele, keskendudes lühiajalisele ja pikaajalisele mälule.

• **AI agentide eneseparandamine**: kuidas mälu võimaldab agentidel õppida varasematest interaktsioonidest ja aja jooksul paremaks saada.

## Saadaval olevad rakendused

See õppetükk sisaldab kahte põhjalikku sülearvuti juhendit:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: rakendab mälu Mem0 ja Azure AI Search abil Microsoft Agent Frameworkiga

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: rakendab struktureeritud mälu kasutades Cognee'd, automaatselt ehitades teadmiste graafi, mida toetavad embed'd, graafi visualiseerimine ja intelligentne otsing

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad:

• **Eraldada erinevaid AI agendi mälutüüpe**, sealhulgas töömälu, lühiajalist ja pikaajalist mälu, samuti spetsialiseeritud vorme nagu persona ja episoodiline mälu.

• **Rakendada ja hallata lühiajalist ja pikaajalist mälu AI agentidele** kasutades Microsoft Agent Frameworki, rakendades tööriistu nagu Mem0, Cognee, Whiteboard mäluga ja integreerides Azure AI Searchiga.

• **Mõista eneseparandavate AI agentide põhimõtteid** ja kuidas robustsed mäluhaldussüsteemid toetavad pidevat õppimist ja kohanemist.

## AI Agendi Mälu Mõistmine

Põhimõtteliselt tähendab **mälu AI agentide jaoks mehhanisme, mis võimaldavad neil säilitada ja meenutada informatsiooni**. See info võib olla konkreetseid detaile vestlusest, kasutaja eelistusi, varasemaid tegevusi või isegi õpitud mustreid.

Ilma mäluta on AI rakendused sageli olukorrast sõltumatud, mis tähendab, et iga interaktsioon algab nullist. See tekitab korduva ja frustreeriva kasutajakogemuse, kus agent "unustab" eelneva konteksti või eelistused.

### Miks on mälu oluline?

Agendi intelligentsus on tihedalt seotud võimega meenutada ja kasutada varasemat infot. Mälu võimaldab agentidel olla:

• **Peegelduvad**: õpivad varasematest tegudest ja tulemustest.

• **Interaktiivsed**: hoiavad vestluse konteksti jooksvalt.

• **Etteteadlikud ja reageerivad**: ennustavad vajadusi või vastavad sobivalt ajaloolistele andmetele.

• **Autonoomsed**: tegutsevad sõltumatumalt, tuginedes salvestatud teadmistele.

Mälu rakendamise eesmärk on muuta agendid **usaldusväärsemaks ja võimekamaks**.

### Mälu tüübid

#### Töömälu

Mõtle sellele kui märkmele, mida agent kasutab ühes, jooksvas ülesandes või mõtlemisprotsessis. See sisaldab kohest informatsiooni järgmise sammu arvutamiseks.

AI agentide puhul hõlmab töömälu tavaliselt kõige olulisemat infot vestlusest, isegi kui kogu vestluse ajalugu on pikk või lühendatud. Keskendutakse võtmeelementide nagu nõudmised, ettepanekud, otsused ja tegevused eraldamisele.

**Töömälu näide**

Reisibroneerimise agendi puhul võib töömälu haarata kasutaja praeguse soovinõude, näiteks "Ma tahan broneerida reisi Pariisi". See konkreetne soov hoitakse agendi vahetus kontekstis, et juhendada praegust suhtlust.

#### Lühiajaline mälu

See mälu tüüp hoiab infot ühe vestluse või seansi jooksul. See on praeguse vestluse kontekst, mis võimaldab agendil viidata eelnevatele dialoogi vahetustele.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK näidetes vastab see töösessioonile `AgentSession`, mis luuakse `agent.create_session()` abil. See sessioon on raamistikus sisseehitatud lühiajaline mälu: hoiab vestluse konteksti alles seni, kuni sama seanssi kasutatakse, kuid konteksti ei säilitata pärast sessiooni lõppu või rakenduse taaskäivitust. Kasuta pikaajalist mälu faktide ja eelistuste salvestamiseks, mis peavad seansside vahel püsima, tavaliselt läbi andmebaasi, vektoriindeksi või muu püsiva salvestuse.

**Lühiajalise mälu näide**

Kui kasutaja küsib "Kui palju maksab lend Pariisi?" ja järgneb küsimus "Ent majutus seal?", tagab lühiajaline mälu, et agent teab, et "seal" viitab sama vestluse raames "Pariisile".

#### Pikaajaline mälu

See on info, mis säilib mitmete vestluste või seansside jooksul. Võimaldab agentidel meeles pidada kasutaja eelistusi, ajaloolisi interaktsioone või üldteadmisi pika aja jooksul. See on oluline personaliseerimiseks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et "Ben naudib suusatamist ja välitegevusi, eelistab kohvi mägivaatega ja soovib vältida keerukaid suusaradu varasema vigastuse tõttu". See info, mis on õpitud varasematest interaktsioonidest, mõjutab soovitusi tulevastes reisiplaneerimise seanssides, muutes need väga personaalseks.

#### Persona mälu

See spetsialiseerunud mälu tüüp aitab agendil arendada järjepidevat "isiksust" või "persona". Võimaldab agendil meeles pidada detailid iseendast või oma kavandatud rollist, muutes suhtlused sujuvamaks ja keskendunumaks.

**Persona mälu näide**
Kui reisibüroo agent on loodud olema "ekspert suusareiside planeerija," võib persona mälu seda rolli tugevdada, mõjutades vastuseid, et need vastaksid eksperdi toonile ja teadmistele.

#### Töövoo/Episoodiline mälu

See mälu salvestab agenti kompleksse ülesande käigus tehtud sammude järjekorra, sealhulgas edukuse ja ebaõnnestumised. See on nagu konkreetsete "episoodide" või varasemate kogemuste meenutamine, et neist õppida.

**Episoodilise mälu näide**

Kui agent üritas broneerida kindlat lendu, kuid see ebaõnnestus selle kättesaamatuse tõttu, võiks episoodiline mälu sellise ebaõnnestumise salvestada, võimaldades agendil proovida alternatiivseid lende või teavitada kasutajat probleemist paremini järgmisel katsel.

#### Objektimälu

See hõlmab konkreetsete objektide (nagu inimesed, kohad või asjad) ja sündmuste väljavõtmist ning meeldejätmist vestlustest. Võimaldab agendil luua struktuurset arusaama arutatud võtmeelementidest.

**Objektimälu näide**

Vestlusest möödunud reisist võib agent välja võtta "Pariisi", "Eiffeli torni" ja "õhtu Le Chat Noir restoranis" objektidena. Järgmises suhtluses võiks agent meenutada "Le Chat Noir" ja pakkuda seal uue broneeringu tegemist.

#### Struktureeritud RAG (Retrieval Augmented Generation)

Kuigi RAG on laiem tehnika, siis "Struktureeritud RAG" on esile toodud kui võimas mälutehnoloogia. See võtab tiheda, struktureeritud info eri allikatest (vestlustest, e-kirjadest, piltidest) ja kasutab seda vastuste täpsuse, meeldejätmise ja kiiruse parandamiseks. Erinevalt klassikalisest RAGist, mis tugineb ainult semantilisele sarnasusele, töötab Struktureeritud RAG info omadusest lähtuvalt.

**Struktureeritud RAG näide**

Selle asemel, et ainult märksõnu sobitada, võiks Struktureeritud RAG parsida lennuandmed (sihtkoht, kuupäev, kellaaeg, lennufirma) e-kirjast ja salvestada need struktureeritud vormis. See võimaldaks täpseid päringuid nagu "Millise lennu ma broneerisin teisipäeval Pariisi?"

## Mälu rakendamine ja salvestamine

Mälu rakendamine AI agentidele hõlmab süsteemset protsessi nimega **mälu haldamine**, mis sisaldab info genereerimist, salvestamist, otsimist, integreerimist, uuendamist ja isegi unustamist (või kustutamist). Otsing on eriti oluline aspekt.

### Spetsialiseeritud mälutööriistad

#### Mem0

Üks viis agendi mälu talletamiseks ja haldamiseks on kasutada spetsialiseeritud tööriistu nagu Mem0. Mem0 töötab püsiva mälukihina, võimaldades agentidel meenutada olulisi suhtlusi, salvestada kasutaja eelistusi ja faktipõhist konteksti ning õppida õnnestumistest ja ebaõnnestumistest aja jooksul. Idee on muuta olukorrast sõltumatud agendid olekupiirangutega agentideks.

See toimib **kahefaasilise mälu torujuhtme kaudu: väljavõtmine ja uuendamine**. Esiteks saadetakse agendi lõimesse lisatud sõnumid Mem0 teenusele, mis kasutab suurt keelemudelit (LLM) vestluse ajaloo kokkusurumiseks ja uute mälestuste väljavõtmiseks. Seejärel määrab LLM-põhine uuendusfaas, kas neid mälestusi lisada, muuta või kustutada, salvestades need hübriidandmehoidlasse, mis võib sisaldada vektori-, graafi- ja võtme-väärtuse andmebaase. See süsteem toetab ka erinevaid mälutüüpe ning võib kaasata graafimälu objektidevaheliste suhete haldamiseks.

#### Cognee

Teine võimas lähenemine on kasutada **Cogneed**, avatud lähtekoodiga semantilist mälu AI agentidele, mis muudab struktureeritud ja struktureerimata andmed päritavaks teadmiste graafile, mida toetavad embed'd. Cognee pakub **kahesalvestuse arhitektuuri**, ühendades vektori sarnasusotsingu graafisuhetega, mis võimaldab agentidel mõista mitte ainult seda, milline info on sarnane, vaid ka kuidas mõisted omavahel seotud on.

See paistab silma **hübriidotsingus**, mis ühendab vektori sarnasuse, graafistruktuuri ja LLM-põhise mõtlemise - alates toorest lõiguotsingust kuni graafitundliku küsimustele vastamiseni. Süsteem säilitab **elava mälu**, mis areneb ja kasvab jäädes samaaegselt päritavaks kui üks ühendatud graafik, toetades nii lühiajalise seansi konteksti kui ka pikaajalist püsivat mälu.

Cognee sülearvutijuhend ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreerib selle ühtse mälukihi ehitamist, praktiliste näidetega erinevate andmeallikate süstimiseks, teadmiste graafi visualiseerimiseks ja erinevate otsingustrateegiate kasutamiseks spetsiifiliste agentide vajaduste rahuldamiseks.

### Mälu salvestamine RAG abil

Lisaks spetsialiseeritud mälutööriistadele nagu Mem0 saad kasutada tugevaid otsinguteenuseid nagu **Azure AI Search mälu salvestamiseks ja pärimiseks**, eriti struktureeritud RAGi jaoks.

See võimaldab põhjalikult toetada agendi vastuseid omaenda andmetega, tagades asjakohasemaid ja täpsemaid vastuseid. Azure AI Search saab kasutada kasutajaspetsiifiliste reisimälestuste, tooteloendite või muude domeenispetsiifiliste teadmiste salvestamiseks.

Azure AI Search toetab võimalusi nagu **Struktureeritud RAG**, mis paistab silma tiheda, struktureeritud info väljavõtmisel ja pärimisel suurtest andmekogumitest, nagu vestluste ajaloost, e-kirjadest või isegi piltidest. See pakub võrreldes traditsioonilise tekstilõikude ja embed'imise lähenemisega "ülimuslikku täpsust ja meeldejätmist".

## AI Agentide eneseparandamine

Eneseparanduvate agentide üldine muster hõlmab **"teadmusagendi"** sisseviimist. See eraldi agent jälgib peamist vestlust kasutaja ja põhiagendi vahel. Selle ülesanne on:

1. **Tuvastada väärtuslikku infot**: otsustada, kas mõni vestluse osa väärib salvestamist üldise teadmisena või konkreetse kasutaja eelistusena.

2. **Väljavõtte tegemine ja kokkuvõtete koostamine**: ekstraktida vestlusest oluline õppetund või eelistus.

3. **Teadmistebaasi salvestamine**: säilitada see väljavõetud info tihti vektorandmebaasis, et seda hiljem pärida.

4. **Tulevaste päringute rikastamine**: kui kasutaja esitab uue päringu, pärib teadmusagent vastava salvestatud info ja lisab selle kasutaja küsimusele, pakkudes põhiagendile olulist konteksti (sarnaselt RAGile).

### Mälu optimeerimised

• **Latentsuse juhtimine**: et vältida kasutajaliidese aeglustamist, võib alguses kasutada odavamat ja kiirem mudelit, mis kiiresti kontrollib, kas info on salvestamist või taasalvestamist väärt, kutsudes keerukama ekstraktsiooni/otsingu protsessi sisse vaid vajadusel.

• **Teadmistebaasi hooldus**: kasvava teadmistebaasi puhul saab vähem kasutatava info viia "külma hoiustamise" ehk odavama arhiveerimise alla kulude haldamiseks.

## Kas sul on veel küsimusi agendi mälu kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda õppetundides ja saada vastused oma AI agentide küsimustele.
## Eelmine õppetükk

[Konteksti inseneritöö AI agentide jaoks](../12-context-engineering/README.md)

## Järgmine õppetükk

[Microsoft Agent Frameworki uurimine](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->