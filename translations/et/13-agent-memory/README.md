# Mälu tehisintellekti agentidele
[![Agent Memory](../../../translated_images/et/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kui räägitakse tehisintellekti agentide loomise ainulaadsetest eelistest, käsitletakse peamiselt kahte asja: tööriistade kasutamise võime ülesannete täitmiseks ja aja jooksul paremaks muutumise võime. Mälu on iseparaneva agendi loomise aluseks, mis suudab luua paremaid kasutajakogemusi.

Selles õppetükis vaatleme, mis on mälu tehisintellekti agentidele ja kuidas seda hallata ning kasutada oma rakenduste kasuks.

## Sissejuhatus

Selles õppetükis käsitletakse:

• **Tehisintellekti agendi mälu mõistmine**: mis on mälu ja miks see agentidele oluline on.

• **Mälu rakendamine ja salvestamine**: praktilised meetodid mäluvõime lisamiseks tehisintellekti agentidele, keskendudes lühiajalisele ja pikaajalisele mälule.

• **Tehisintellekti agentide iseparandamine**: kuidas mälu võimaldab agentidel õppida varasematest suhetest ja aja jooksul paraneda.

## Saadaval olevad rakendused

See õppetükk sisaldab kahte põhjalikku märkmikuõpetust:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: rakendab mälu Mem0 ja Azure AI Search abil Microsoft Agent Frameworkis

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: rakendab struktureeritud mälu Cognee abil, luues automaatselt teadmiste graafi, mis tugineb manustele, visualiseerides graafi ja pakkudes intelligentset otsingut

## Õpieesmärgid

Pärast selle õppetüki lõpetamist teate, kuidas:

• **Erinevaid tehisintellekti agendi mälutüüpe eristada**, sealhulgas töötav mälu, lühiajaline ja pikaajaline mälu, samuti spetsialiseeritud vormid nagu persona ja episoodiline mälu.

• **Rakendada ja hallata lühiajalist ja pikaajalist mälu** tehisintellekti agentide jaoks, kasutades Microsoft Agent Frameworki, Mem0, Cognee, Whiteboardi mälu ja Azure AI Searchi integreerimist.

• **Mõista iseparanevate tehisintellekti agentide põhimõtteid** ja seda, kuidas tugevad mäluhaldussüsteemid aitavad kaasa pidevale õppimisele ja kohanemisele.

## Tehisintellekti agendi mälu mõistmine

Põhimõtteliselt viitab **mälu tehisintellekti agentidele mehhanismidele, mis võimaldavad neil säilitada ja meenutada teavet**. See teave võib olla spetsiifilised detailid vestluse kohta, kasutaja eelistused, varasemad tegevused või isegi õpitud mustrid.

Ilma mäluta on tehisintellekti rakendused sageli olekuta, mis tähendab, et iga suhtlus algab nullist. See viib korduva ja frustreeriva kasutajakogemuseni, kus agent "unustab" varasema konteksti või eelistused.

### Miks on mälu tähtis?

agendi intelligentsus on tihedalt seotud tema võimega meenutada ja kasutada varasemat teavet. Mälu võimaldab agentidel olla:

• **Reflektiivne**: õppides varasematest tegudest ja tulemustest.

• **Interaktiivne**: säilitades konteksti jooksva vestluse jooksul.

• **Etteaimav ja reageeriv**: eeldades vajadusi või vastates sobivalt ajaloolistele andmetele.

• **Autonoomne**: toimides iseseisvamalt, tuginedes salvestatud teadmistele.

Mälu rakendamise eesmärk on muuta agendid **usaldusväärsemaks ja võimekamaks**.

### Mälutüübid

#### Töötav mälu

Mõelge sellele nagu visandpaberile, mida agent kasutab ühe jooksva ülesande või mõttekäigu ajal. See sisaldab kohest teavet, mis on vajalik järgmise sammu arvutamiseks.

Tehisintellekti agentide puhul salvestab töötav mälu sageli vestluse kõige olulisemat teavet, isegi kui kogu vestluse ajalugu on pikk või kärbitud. See keskendub võtmeelementide nagu nõuded, ettepanekud, otsused ja tegevused eraldamisele.

**Töötava mälu näide**

Reisibroneerimisagendis võib töötav mälu salvestada kasutaja praeguse soovi, nagu „Ma tahan broneerida reisi Pariisi“. See konkreetne nõue hoitakse agendi vahetus kontekstis, et juhtida praegust suhtlust.

#### Lühiajaline mälu

See mälu tüüp hoiab teavet ühe vestluse või seansi vältel. See on praeguse vestluse kontekst, mis võimaldab agendil viidata varasematele dialoogide pööretele.

[Microsoft Agent Frameworki](https://github.com/microsoft/agent-framework) Python SDK näidetes vastab see `AgentSession`-ile, mis luuakse `agent.create_session()` abil. Seanss on raamistikus sisseehitatud lühiajaline mälu: see hoiab vestluse konteksti saadaval sama seansi kasutamise ajal, kuid see kontekst ei püsi, kui seanss lõpeb või rakendus taaskäivitub. Faktide ja eelistuste jaoks, mis peavad kestma seansside vahel, kasutage pikaajalist mälu, tavaliselt andmebaasi, vektoriindeksi või muu püsiva hoidlaga.

**Lühiajalise mälu näide**

Kui kasutaja küsib: „Kui palju maksab lend Pariisi?“ ja järgneb küsimus „Ent majutus seal?“, tagab lühiajaline mälu, et agent teab, et "seal" viitab samas vestluses "Pariisile".

#### Pikaajaline mälu

See on teave, mis kestab mitme vestluse või seansi vältel. See võimaldab agentidel meeles pidada kasutaja eelistusi, ajaloolisi suhtlusi või üldteadmisi pikema aja jooksul. See on oluline isikupärastamiseks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et „Benile meeldivad suusatamine ja õues tegevused, talle meeldib kohv mägivaatega ja ta soovib vältida keerulisi suusaradu varasema vigastuse tõttu“. See teave, mis on õpitud varasematest suhtlustest, mõjutab soovitusi tulevastel reisiplaanide sessioonidel, muutes need väga isikupärastatuks.

#### Persona mälu

See spetsialiseerunud mälutüüp aitab agendil välja arendada järjepideva "isiksuse" või "persona". See võimaldab agendil meeles pidada üksikasju enda või tema taotletud rolli kohta, muutes suhtlused sujuvamaks ja fokusseeritumaks.

**Persona mälu näide**
Kui reisibüroo agent on loodud olema „ekspert suusareiside planeerimisel“, siis persona mälu võib seda rolli tugevdada, mõjutades tema vastuseid vastavalt eksperdi toonile ja teadmistele.

#### Töövoo/Episoodiline mälu

See mälu salvestab sammude järjekorra, mille kaudu agent keerulise ülesande täidab, sealhulgas edukused ja ebaõnnestumised. See on nagu konkreetsete „episoodide“ või varasemate kogemuste meenutamine, et neist õppida.

**Episoodilise mälu näide**

Kui agent proovib broneerida konkreetset lendu, kuid see ei õnnestu ebakättesaadavuse tõttu, võib episoodiline mälu selle ebaõnnestumise salvestada. See võimaldab agendil proovida alternatiivseid lende või teavitada kasutajat probleemist teadlikumal viisil järgmisel katsel.

#### Objektimälu

See hõlmab konkreetsete üksuste (nagu inimesed, kohad või asjad) ja sündmuste väljaselgitamist ja meeldejätmist vestlustest. See võimaldab agendil üles ehitada struktureeritud arusaama peamistest arutletud elementidest.

**Objektimälu näide**

Vestlusest möödunud reisi kohta võib agent tuvastada üksused „Pariis“, „Eiffeli torn“ ja „õhtusöök restoranis Le Chat Noir“. Tulevases suhtluses võib agent meenutada „Le Chat Noiri“ ja pakkuda uut broneeringut seal.

#### Struktureeritud RAG (otsingupõhine täiendatud genereerimine)

Kuigi RAG on laiem tehnika, tõstetakse esile "struktureeritud RAG" kui võimsat maimul tehnoloogiat. See võtab tihedaid, struktureeritud andmeid erinevatest allikatest (vestlused, e-kirjad, pildid) ja kasutab neid täpsuse, meenutuse ja kiiruse parandamiseks vastustes. Erinevalt klassikalisest RAG-ist, mis tugineb vaid semantilisele sarnasusele, töötab Struktureeritud RAG andmete loomuliku struktuuriga.

**Struktureeritud RAGi näide**

Selle asemel, et lihtsalt vasteid märksõnadele otsida, suudab Struktureeritud RAG töödelda lennuandmeid (sihtkoht, kuupäev, kellaaeg, lennufirma) e-kirjast ja salvestada need struktureeritud kujul. See võimaldab täpseid päringuid nagu „Millise lennu broneerisin teisipäeval Pariisi?“

## Mälu rakendamine ja salvestamine

Mälu rakendamine tehisintellekti agentidele hõlmab süsteemset protsessi, mida nimetatakse **mäluhalduseks**, mis sisaldab teabe genereerimist, salvestamist, otsimist, integreerimist, uuendamist ja isegi "unustamist" (või kustutamist). Otsimine on eriti oluline aspekt.

### Spetsialiseerunud mälutööriistad

#### Mem0

Üks viis agendi mälu salvestamiseks ja haldamiseks on kasutada spetsiaalseid tööriistu nagu Mem0. Mem0 toimib püsiva mälukihina, võimaldades agentidel meenutada asjakohaseid suhtlusi, salvestada kasutaja eelistusi ja faktipõhist konteksti ning õppida edu ja ebaõnnestumiste põhjal aja jooksul. Idee on muuta olekuta agendid olekuga agentideks.

See töötab **kahefaasilise mälupipelini kaudu: andmete väljavõtmine ja uuendamine**. Esiteks saadetakse agendi lõimel lisatud sõnumid Mem0 teenusele, mis kasutab suurt keelemudelit (LLM) vestluse ajaloo kokkuvõtmiseks ja uute mälestuste väljavõtmiseks. Seejärel määrab LLM-põhine uuendusfaas, kas neid mälestusi lisada, muuta või kustutada, salvestades need hübriidandmebaasi, mis võib sisaldada vektori-, graafi- ja võtme-väärtuse andmebaase. See süsteem toetab ka erinevaid mälutüüpe ning võib kasutada graafimälu suhete haldamiseks üksuste vahel.

#### Cognee

Teine võimas lähenemine on kasutada **Cognee**, avatud lähtekoodiga semantilist mälu tehisintellekti agentidele, mis teisendab struktureeritud ja struktureerimata andmed päringuteks sobivateks teadmiste graafideks, mis tuginevad manustele. Cognee pakub **kahepüsivat arhitektuuri**, mis ühendab vektorsarnase otsingu graafisuhetega, võimaldades agentidel mõista mitte ainult, mis info on sarnane, vaid ka kuidas mõisted omavahel seotud on.

See on suurepärane **hübriidotsingus**, mis ühildab vektorsarnasuse, graafistruktuuri ja LLM-i arutluse – alates toorest andmeosa otsingust kuni graafitundliku küsimuste vastamiseni. Süsteem säilitab **elava mälu**, mis areneb ja kasvab, olles samal ajal päringutes ühendatud graafina kättesaadav, toetades nii lühiajalist sessioonikonteksti kui ka pikaajalist püsivat mälu.

Cognee märkmikuõpetus ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreerib selle ühtse mälukihi loomist praktiliste näidetega erinevate andmeallikate tarbimiseks, teadmiste graafi visualiseerimiseks ja päringuteks erinevate otsingustrateegiatega, mis on kohandatud spetsiifiliste agentide vajadustele.

### Mälu salvestamine RAG abil

Lisaks spetsialiseerunud mälutööriistadele nagu Mem0 saate kasutada tugevaid otsinguteenuseid nagu **Azure AI Search ainult mälu salvestamiseks ja otsimiseks**, eriti struktureeritud RAG jaoks.

See võimaldab teil kinnistada agendi vastused oma andmetega, tagades asjakohasemad ja täpsemad vastused. Azure AI Searchi saab kasutada kasutajapõhise reisimälu, tootekataloogide või mis tahes muu valdkonnapõhise teadmise salvestamiseks.

Azure AI Search toetab funktsioone nagu **Structured RAG**, mis paistab silma tihedate, struktureeritud andmete väljatõstmise ja otsingu osas suurtes andmekogudes nagu vestlusajalugu, e-kirjad või isegi pildid. See pakub "üliinimlikku täpsust ja meenutust" võrreldes traditsiooniliste tekstilõikude ja manuste lähenemisviisidega.

## Tehisintellekti agentide iseparandamine

Iseparandavate agentide laialt levinud muster hõlmab **"teadmiste agenti"** kasutuselevõttu. See eraldi agent jälgib peamist vestlust kasutaja ja tähtsa agendi vahel. Selle roll on:

1. **Määratleda väärtuslik teave**: tuvastada, kas mõni vestluse osa on väärt salvestamist üldiste teadmistena või konkreetse kasutaja eelistusena.

2. **Väljavõtmine ja kokkuvõte**: välja selgitada vestluse olulisim õpe või eelistus.

3. **Salvestamine teadmistebaasi**: see välja võetud teave salvestatakse sageli vektorandmebaasi, et seda hiljem otsida.

4. **Tulevaste päringute täiendamine**: kui kasutaja algatab uue päringu, otsib teadmiste agent asjakohase salvestatud teabe ja lisab selle kasutaja sisendile, pakkudes peamisele agendile olulist konteksti (sarnaselt RAG-ile).

### Mälu optimeerimine

• **Latentsuse haldamine**: kasutajaliidese aeglustamise vältimiseks võib alguses kasutada odavamat ja kiirem mudelit, mis kontrollib kiiresti, kas teavet on väärt salvestada või otsida, tõmmates keerukama väljavõtte/otsi protsessi esile ainult vajadusel.

• **Teadmistebaasi hooldus**: kasvava teadmistebaasi puhul saab harvemini kasutatava teabe viia „külma hoiule“, et hoida kulud kontrolli all.

## Kas teil on rohkem küsimusi agendi mälu kohta?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda konsultatsioonidel ja saada vastuseid oma tehisintellekti agentide küsimustele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->