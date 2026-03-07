# Mälu tehisintellekti agentidele
[![Agent Memory](../../../translated_images/et/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Tehisintellekti agentide loomise ainulaadsete eeliste arutamisel käsitletakse peamiselt kahte asja: tööriistade kutsumise võimalust ülesannete täitmiseks ja aja jooksul paranemise võimet. Mälu on aluseks iseparaneva agendi loomisele, kes suudab luua meie kasutajatele paremaid kogemusi.

Selles õppetükis vaatleme, mis on mälu tehisintellekti agentidele ning kuidas me saame seda hallata ja kasutada oma rakenduste kasuks.

## Sissejuhatus

See õppetükk hõlmab:

• **Tehisintellekti agendi mälude mõistmine**: Mis on mälu ja miks see agentidele oluline on.

• **Mälu rakendamine ja salvestamine**: Praktilised meetodid, kuidas lisada mäluvõimekus oma tehisintellekti agentidele, keskendudes lühiajalisele ja pikaajalisele mälule.

• **Tehisintellekti agentide iseparandumine**: Kuidas võimaldab mälu agentidel õppida varasematest suhtlustest ja aja jooksul areneda.

## Saadaval olevad rakendused

Selles õppetükis on kaks põhjalikku märkmikututoriaali:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Rakendab mälu kasutades Mem0 ja Azure AI Searchi Microsoft Agent Frameworkiga

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Rakendab struktureeritud mälu, kasutades Cogneet, mis ehitab automaatselt teadmiste graafi, toetatud embedingutega, graafi visualiseerimise ja intelligentse otsingu

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad:

• **Erinevaid tehisintellekti agendi mälu tüüpe eristada**, sealhulgas töömälu, lühiajalist ja pikaajalist mälu ning spetsialiseerunud vorme nagu persona- ja episoodiline mälu.

• **Rakendada ja hallata lühiajalist ja pikaajalist mälu tehisintellekti agentidele**, kasutades Microsoft Agent Frameworki, tööriistu nagu Mem0, Cognee, Whiteboard Memory ja integreerides Azure AI Searchiga.

• **Mõista iseparanevate tehisintellekti agentide põhimõtteid** ja kuidas tugevad mäluhaldussüsteemid toetavad pidevat õppimist ja kohanemist.

## Tehisintellekti agendi mälu mõistmine

Põhimõtteliselt **viitab mälu tehisintellekti agentidele mehhanismidele, mis võimaldavad neil säilitada ja meenutada teavet**. See võib olla spetsiifilised üksikasjad vestluse kohta, kasutaja eelistused, varasemad tegevused või isegi õpitud mustrid.

Ilma mäluta on tehisintellekti rakendused sageli seisundita (stateless), mis tähendab, et iga suhtlus algab nullist. See põhjustab korduvat ja frustreerivat kasutajakogemust, kus agent "unustab" varasema konteksti või eelistused.

### Miks mälu on oluline?

Agendi intelligentsus on sügavalt seotud tema võimega meenutada ja kasutada varasemat teavet. Mälu võimaldab agentidel olla:

• **Reflektiivsed**: Õppida varasemate tegevuste ja tulemustest.

• **Interaktiivsed**: Säilitada konteksti käimasoleva vestluse jooksul.

• **Etteteadlikud ja reagatiivsed**: Ennustada vajadusi või reageerida õigesti ajaloo põhjal.

• **Autonoomsed**: Tegutseda iseseisvamalt, tuginedes salvestatud teadmistele.

Mälu rakendamise eesmärk on muuta agendid usaldusväärsemaks ja võimekamaks.

### Mälu tüübid

#### Töömälu

Mõtle sellele kui paberi tüki peale, mida agent kasutab ühe jooksva ülesande või mõttekäigu jooksul. See hoiab vahetut teavet, mis on vajalik järgmise sammu arvutamiseks.

Tehisintellekti agentide puhul haarab töömälu sageli kõige asjakohasema teabe vestlusest, isegi kui kogu vestluslugu on pikk või kärbitud. See keskendub võtmeelementide nagu nõuded, ettepanekud, otsused ja tegevused väljavõtmisele.

**Töömälu näide**

Reisibroneerimise agendi puhul võib töömälu haarata kasutaja hetke päringu, näiteks "Ma tahan broneerida reisi Pariisi". See konkreetne nõue hoitakse agendi vahetus kontekstis, et juhendada praegust suhtlust.

#### Lühiajaline mälu

See mälu tüüp säilitab teavet ühe vestluse või sessiooni jooksul. See on vestluse praeguse vestluse kontekst, mis võimaldab agentil viidata varasematele dialoogi pöördele.

**Lühiajalise mälu näide**

Kui kasutaja küsib: "Kui palju maksab lend Pariisi?" ja seejärel küsib: "Aga majutus seal?", tagab lühiajaline mälu, et agent teab, et "seal" viitab sama vestluse jooksul "Pariisi".

#### Pikaajaline mälu

See on teave, mis säilib mitme vestluse või sessiooni vahel. See võimaldab agentidel meeles pidada kasutaja eelistusi, ajaloolisi suhtlusi või üldteadmisi pikema aja jooksul. See on oluline isikupärastamiseks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et "Ben armastab suusatamist ja vabaõhutegevusi, meeldib kohv vaatega mägedele ja soovib vältida edasijõudnud suusaradu varasema vigastuse tõttu". See teave, mis on õpitud varasematest suhtlustest, mõjutab soovitusi tulevaste reisiplaanide koostamisel, muutes need väga isikupäraseks.

#### Persona mälu

See spetsialiseerunud mälu tüüp aitab agendil arendada järjepidevat "isiksust" või "persona". See võimaldab agendil meeles pidada üksikasju enda või oma kavandatud rolli kohta, muutes suhtlused sujuvamaks ja sihitud.

**Persona mälu näide**

Kui reisagent on kujundatud "eksperdi suusareiside planeerijana", võib persona mälu tugevdada seda rolli, mõjutades vastuseid vastavalt eksperdi toonile ja teadmistele.

#### Tööpõhine/Episoodiline mälu

See mälu salvestab järjestuse samme, mida agent kasutab keeruka ülesande täitmisel, sealhulgas edu ja ebaõnnestumisi. See on nagu mäletada konkreetseid "episoodid" või varasemad kogemused, et neist õppida.

**Episoodilise mälu näide**

Kui agent püüdis broneerida konkreetset lendu, kuid see ebaõnnestus kättesaamatuse tõttu, võiks episoodiline mälu selle ebaõnnestumise salvestada, võimaldades agendil proovida alternatiivseid lende või teavitada kasutajat probleemist teadlikumalt järgmisel katsel.

#### Entiteedi mälu

See hõlmab spetsiifiliste entiteetide (nagu inimesed, kohad või asjad) ja sündmuste eraldamist ja meeles pidamist vestlustest. See võimaldab agendil luua struktureeritud arusaama arutatud võtmeelementidest.

**Entiteedi mälu näide**

Vestlusest mineviku reisi kohta võib agent eraldada entiteetidena "Pariis", "Eiffeli torn" ja "õhtusöök restoranis Le Chat Noir". Tulevikus võiks agent meenutada "Le Chat Noir" ning pakkuda broneeringut seal.

#### Struktureeritud RAG (Retrieval Augmented Generation)

Kuigi RAG on laiem tehnik, on "Struktureeritud RAG" esile tõstetud kui võimas mälu tehnoloogia. See eraldab tihedat, struktureeritud teavet erinevatest allikatest (vestlused, e-kirjad, pildid) ja kasutab seda täpsuse, meenutamise ja kiiruse parandamiseks vastustes. Erinevalt klassikalisest RAG-st, mis tugineb ainult semantilisele sarnasusele, töötab Struktureeritud RAG informatsiooni loomuliku struktuuriga.

**Struktureeritud RAG näide**

Selle asemel, et lihtsalt märksõnu sobitada, võiks Struktureeritud RAG analüüsida lennu üksikasju (sihtkoht, kuupäev, kellaaeg, lennufirma) e-kirjast ja salvestada need struktureeritud kujul. See võimaldab täpseid päringuid, näiteks "Millise lennu ma broneerisin Pariisi teisipäeval?"

## Mälu rakendamine ja salvestamine

Mälu rakendamine tehisintellekti agentidele hõlmab süsteemset protsessi **mäluhalduse** kaudu, mis sisaldab teabe genereerimist, salvestamist, toomist, integreerimist, uuendamist ja isegi "unustamist" (või kustutamist). Eriti oluline on teabe toomine.

### Spetsialiseerunud mälutööriistad

#### Mem0

Üks viis agendi mälu salvestamiseks ja haldamiseks on kasutada spetsialiseerunud tööriistu nagu Mem0. Mem0 toimib püsiva mälukihina, võimaldades agentidel meenutada asjakohaseid suhtlusi, salvestada kasutaja eelistusi ja faktipõhist konteksti ning õppida edu ja ebaõnnestumiste põhjal aja jooksul. Idee on see, et seisundita agendid muutuvad seisunditundlikeks.

See toimib kahefaasilise mälupipeline'i kaudu: eraldamine ja uuendamine. Esiteks saadetakse agendi lõimele lisatud sõnumid Mem0 teenusele, mis kasutab suurt keelemudelit (LLM), et kokku võtta vestluse ajalugu ja eraldada uusi mälusid. Järgnev LLM-põhine uuendusfaas otsustab, kas neid mälusid lisada, muuta või kustutada, salvestades need hübriidandmebaasi, mis võib sisaldada vektori-, graafi- ja võtme-väärtusbaase. See süsteem toetab ka mitmesuguseid mälutüüpe ning võib kaasata graafimälu, et hallata entiteetide vahelisi suhteid.

#### Cognee

Teine võimas lähenemine on kasutada **Cogneet**, avatud lähtekoodiga semantilist mälu tehisintellekti agentidele, mis muundab struktureeritud ja struktureerimata andmeid päringuvõimelisteks teadmiste graafideks, mida toetavad embedingud. Cognee pakub **topeltsalvestuse arhitektuuri**, mis ühendab vektorsarnasuse otsingu graafisuhetega, võimaldades agentidel mõista mitte ainult seda, milline teave on sarnane, vaid kuidas mõisted on omavahel seotud.

See on tipptasemel **hübriidse toomise poolest**, mis segab vektorsarnasust, graafi struktuuri ja LLM-i põhjendamist - alates toorandmete otsimisest kuni graafiteadliku küsimustele vastamiseni. Süsteem säilitab **elava mälu**, mis areneb ja kasvab ning jääb samal ajal päringuvõimeliseks kui üks ühendatud graaf, toetades nii lühiajalist sessiooni konteksti kui ka pikaajalist püsivat mälu.

Cognee märkmikuõpetus ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreerib selle ühtse mälukihi loomist, praktiliste näidetega erinevate andmeallikate sissevõtmisest, teadmiste graafi visualiseerimisest ja päringutest erinevate otsingustrateegiatega, mis on kohandatud konkreetsete agendi vajadustega.

### Mälu salvestamine RAG-i abil

Lisaks spetsialiseerunud mälutööriistadele nagu Mem0 võite kasutada võimsaid otsimisteenuseid nagu **Azure AI Search** mälude salvestamiseks ja toomiseks, eriti struktureeritud RAG jaoks.

See võimaldab teil oma agendi vastuseid oma andmetega siduda, tagades asjakohasemad ja täpsemad vastused. Azure AI Searchi saab kasutada kasutajaspetsiifiliste reisimälude, tooteloendite või muu domeenispetsiifilise teadmise salvestamiseks.

Azure AI Search toetab funktsioone nagu **Struktureeritud RAG**, mis on suurepärane tiheda, struktureeritud teabe eraldamisel ja toomisel suurtest andmekogudest nagu vestluste ajalugu, e-kirjad või isegi pildid. See pakub "ülimat täpsust ja meenutamist" võrreldes traditsiooniliste tekstiparandamise ja embedingu lähenemistega.

## Tehisintellekti agentide iseparandamine

Iseparanevate agentide tavaline muster hõlmab **"teadmiste agendi"** loomist. See eraldi agent jälgib põhikasutaja ja põhiedendi vahelist vestlust. Selle roll on:

1. **Tuua esile väärtuslikku teavet**: Otsustada, kas vestluse mõni osa on väärt salvestamist üldise teadmise või konkreetse kasutaja eelistusena.

2. **Eraldada ja kokku võtta**: Viia vestlusest välja olulisem õppimine või eelistus.

3. **Salvestada teadmistebaasi**: Püsivalt salvestada see eraldatud teave, sageli vektordatabaasi, et seda hiljem tuua.

4. **Täiendada tulevasi päringuid**: Kui kasutaja alustab uut päringut, toob teadmiste agent asjakohaseid salvestatud andmeid ja lisab need kasutaja päringule, pakkudes põhiedendile olulist konteksti (sarnaselt RAG-ile).

### Mälu optimeerimised

• **Latentsuse haldamine**: Et vältida kasutajate suhtluse aeglustumist, võib alguses kasutada odavamat ja kiiremat mudelit, mis kontrollib kiiresti, kas teave on väärt salvestamist või toomist, kutsudes keerulisemat eraldus-/toomisprotsessi välja alles vajadusel.

• **Teadmistebaasi hooldus**: Kasvava teadmistebaasi puhul saab harvemini kasutatava teabe viia "külma hoiuruumi", et kulusid hallata.

## Kas sul on rohkem küsimusi agentide mälu kohta?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada oma tehisintellekti agentide küsimustele vastuseid.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe korral soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või väärinterpreteerimiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->