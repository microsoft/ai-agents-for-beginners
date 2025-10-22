<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-11T11:12:39+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "et"
}
-->
# Mälu AI-agentide jaoks
[![Agent Memory](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.et.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

AI-agentide loomise unikaalsete eeliste arutamisel keskendutakse peamiselt kahele asjale: tööriistade kasutamisele ülesannete täitmiseks ja võimele aja jooksul paremaks muutuda. Mälu on aluseks isetäieneva agendi loomisele, mis suudab pakkuda meie kasutajatele paremaid kogemusi.

Selles õppetükis vaatame, mis on mälu AI-agentide jaoks ning kuidas seda hallata ja rakendada meie rakenduste kasuks.

## Sissejuhatus

Selles õppetükis käsitletakse:

• **AI-agentide mälu mõistmine**: Mis on mälu ja miks see agentide jaoks oluline on.

• **Mälu rakendamine ja salvestamine**: Praktilised meetodid, kuidas lisada AI-agentidele mälufunktsioone, keskendudes lühi- ja pikaajalisele mälule.

• **AI-agentide isetäiendamine**: Kuidas mälu võimaldab agentidel õppida varasematest interaktsioonidest ja aja jooksul paremaks muutuda.

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad:

• **Eristada erinevaid AI-agentide mälutüüpe**, sealhulgas töömälu, lühiajalist ja pikaajalist mälu, samuti spetsialiseeritud vorme nagu persona- ja episoodiline mälu.

• **Rakendada ja hallata AI-agentide lühi- ja pikaajalist mälu** kasutades Semantic Kernel raamistikku, tööriistu nagu Mem0 ja Whiteboard memory ning integreerides Azure AI Searchiga.

• **Mõista isetäiendavate AI-agentide põhimõtteid** ja kuidas tugevad mäluhaldussüsteemid aitavad kaasa pidevale õppimisele ja kohanemisele.

## AI-agentide mälu mõistmine

Põhimõtteliselt viitab **mälu AI-agentide jaoks mehhanismidele, mis võimaldavad neil säilitada ja meenutada teavet**. See teave võib hõlmata konkreetseid detaile vestlusest, kasutaja eelistusi, varasemaid tegevusi või isegi õpitud mustreid.

Ilma mäluta on AI-rakendused sageli olekuta, mis tähendab, et iga interaktsioon algab nullist. See viib korduva ja frustreeriva kasutajakogemuseni, kus agent "unustab" varasema konteksti või eelistused.

### Miks on mälu oluline?

Agendi intelligentsus on tihedalt seotud tema võimega meenutada ja kasutada varasemat teavet. Mälu võimaldab agentidel olla:

• **Reflektiivne**: Õppida varasematest tegevustest ja tulemustest.

• **Interaktiivne**: Säilitada konteksti käimasoleva vestluse ajal.

• **Proaktiivne ja reaktiivne**: Ennustada vajadusi või reageerida sobivalt ajalooliste andmete põhjal.

• **Autonoomne**: Tegutseda iseseisvamalt, tuginedes salvestatud teadmistele.

Mälu rakendamise eesmärk on muuta agendid **usaldusväärsemaks ja võimekamaks**.

### Mälutüübid

#### Töömälu

Mõtle sellele kui agendi "märkmepaberile", mida ta kasutab ühe käimasoleva ülesande või mõtteprotsessi ajal. See hoiab kohest teavet, mis on vajalik järgmise sammu arvutamiseks.

AI-agentide puhul salvestab töömälu sageli vestluse kõige olulisema teabe, isegi kui kogu vestluse ajalugu on pikk või kärbitud. See keskendub võtmeelementide, nagu nõuded, ettepanekud, otsused ja tegevused, väljavõtmisele.

**Töömälu näide**

Reisi broneerimise agent võib töömälu abil salvestada kasutaja praeguse soovi, näiteks "Ma tahan broneerida reisi Pariisi". See konkreetne nõue hoitakse agendi vahetus kontekstis, et suunata käimasolevat interaktsiooni.

#### Lühiajaline mälu

See mälutüüp säilitab teavet ühe vestluse või sessiooni jooksul. See on praeguse vestluse kontekst, mis võimaldab agendil viidata vestluse varasematele pöördumistele.

**Lühiajalise mälu näide**

Kui kasutaja küsib: "Kui palju maksaks lend Pariisi?" ja seejärel jätkab: "Aga majutus seal?", tagab lühiajaline mälu, et agent teab, et "seal" viitab "Pariisile" sama vestluse raames.

#### Pikaajaline mälu

See on teave, mis püsib mitme vestluse või sessiooni jooksul. See võimaldab agentidel meeles pidada kasutaja eelistusi, ajaloolisi interaktsioone või üldisi teadmisi pikema aja jooksul. See on oluline personaliseerimise jaoks.

**Pikaajalise mälu näide**

Pikaajaline mälu võib salvestada, et "Ben naudib suusatamist ja välitegevusi, eelistab kohvi mäevaatega ning soovib vältida keerulisi suusaradu varasema vigastuse tõttu". See teave, mis on õpitud varasematest interaktsioonidest, mõjutab tulevaste reisiplaanide soovitusi, muutes need väga isikupäraseks.

#### Persona mälu

See spetsialiseeritud mälutüüp aitab agendil arendada järjepidevat "isiksust" või "rolli". See võimaldab agendil meeles pidada detaile enda kohta või oma kavandatud rolli, muutes interaktsioonid sujuvamaks ja keskendunumaks.

**Persona mälu näide**

Kui reisiplaneerimise agent on loodud olema "ekspert suusareiside planeerimisel", võib persona mälu tugevdada seda rolli, mõjutades vastuseid, et need vastaksid eksperdi toonile ja teadmistele.

#### Töövoo/episoodiline mälu

See mälu salvestab agendi tehtud sammude järjestuse keeruka ülesande ajal, sealhulgas õnnestumised ja ebaõnnestumised. See on nagu konkreetsete "episoodide" või varasemate kogemuste meelespidamine, et neist õppida.

**Episoodilise mälu näide**

Kui agent üritas broneerida konkreetset lendu, kuid see ebaõnnestus saadavuse puudumise tõttu, võiks episoodiline mälu salvestada selle ebaõnnestumise, võimaldades agendil proovida alternatiivseid lende või teavitada kasutajat probleemist informeeritumalt järgmisel katsel.

#### Entiteedi mälu

See hõlmab konkreetsete entiteetide (nagu inimesed, kohad või asjad) ja sündmuste väljavõtmist ja meelespidamist vestlustest. See võimaldab agendil luua struktureeritud arusaama arutatud võtmeelementidest.

**Entiteedi mälu näide**

Vestlusest varasema reisi kohta võib agent välja võtta "Pariis", "Eiffeli torn" ja "õhtusöök restoranis Le Chat Noir". Tulevases interaktsioonis võiks agent meenutada "Le Chat Noir" ja pakkuda seal uut broneeringut.

#### Struktureeritud RAG (Retrieval Augmented Generation)

Kuigi RAG on laiem tehnika, tõstetakse "Struktureeritud RAG" esile kui võimsat mälutehnoloogiat. See eraldab tihedalt struktureeritud teavet erinevatest allikatest (vestlused, e-kirjad, pildid) ja kasutab seda täpsuse, meenutamise ja kiiruse parandamiseks vastustes. Erinevalt klassikalisest RAG-st, mis tugineb ainult semantilisele sarnasusele, töötab Struktureeritud RAG teabe sisemise struktuuriga.

**Struktureeritud RAG näide**

Selle asemel, et lihtsalt märksõnu sobitada, võiks Struktureeritud RAG e-kirjast välja võtta lennuandmed (sihtkoht, kuupäev, kellaaeg, lennufirma) ja salvestada need struktureeritud viisil. See võimaldab täpseid päringuid, nagu "Millise lennu ma Pariisi teisipäeval broneerisin?"

## Mälu rakendamine ja salvestamine

AI-agentide mälu rakendamine hõlmab **mäluhalduse** süstemaatilist protsessi, mis sisaldab teabe genereerimist, salvestamist, meenutamist, integreerimist, uuendamist ja isegi "unustamist" (või kustutamist). Meenutamine on eriti oluline aspekt.

### Spetsialiseeritud mälutööriistad

Üks viis agendi mälu salvestamiseks ja haldamiseks on kasutada spetsialiseeritud tööriistu nagu Mem0. Mem0 toimib püsiva mälukihina, võimaldades agentidel meenutada asjakohaseid interaktsioone, salvestada kasutaja eelistusi ja faktilist konteksti ning õppida aja jooksul õnnestumistest ja ebaõnnestumistest. Idee seisneb selles, et olekuta agendid muutuvad olekuga agentideks.

See töötab **kahefaasilise mälutoru kaudu: väljavõtmine ja uuendamine**. Esiteks saadetakse agendi lõime lisatud sõnumid Mem0 teenusesse, mis kasutab suurt keelemudelit (LLM), et kokku võtta vestluse ajalugu ja välja võtta uued mälud. Seejärel määrab LLM-põhine uuendusfaas, kas need mälud lisada, muuta või kustutada, salvestades need hübriidandmehoidlasse, mis võib hõlmata vektorit, graafi ja võtme-väärtuse andmebaase. See süsteem toetab ka erinevaid mälutüüpe ja võib sisaldada graafimälu, et hallata entiteetide vahelisi suhteid.

### Mälu salvestamine RAG-ga

Lisaks spetsialiseeritud mälutööriistadele nagu Mem0, saab kasutada tugevaid otsinguteenuseid, nagu **Azure AI Search, mälude salvestamiseks ja meenutamiseks**, eriti struktureeritud RAG jaoks.

See võimaldab agendi vastuseid siduda oma andmetega, tagades asjakohasemad ja täpsemad vastused. Azure AI Searchi saab kasutada kasutajaspetsiifiliste reiside mälude, tootekataloogide või mis tahes muu valdkonnaspetsiifilise teadmise salvestamiseks.

Azure AI Search toetab funktsioone nagu **Struktureeritud RAG**, mis paistab silma tihedalt struktureeritud teabe eraldamise ja meenutamisega suurtest andmekogumitest, nagu vestluste ajalugu, e-kirjad või isegi pildid. See pakub "üliinimlikku täpsust ja meenutamist" võrreldes traditsiooniliste tekstitükeldamise ja sisestamise lähenemisviisidega.

## AI-agentide isetäiendamine

Isetäiendavate agentide tavaline muster hõlmab **"teadmiste agendi"** kasutuselevõttu. See eraldi agent jälgib peamist vestlust kasutaja ja põhivahendi vahel. Selle roll on:

1. **Väärtusliku teabe tuvastamine**: Määrata, kas vestluse mõni osa on väärt salvestamist üldteadmiste või konkreetse kasutaja eelistusena.

2. **Väljavõtmine ja kokkuvõte**: Destilleerida vestlusest olulised õppetunnid või eelistused.

3. **Salvestamine teadmistebaasi**: Säilitada see väljavõetud teave, sageli vektorandmebaasis, et seda hiljem meenutada.

4. **Tulevaste päringute täiendamine**: Kui kasutaja algatab uue päringu, otsib teadmiste agent asjakohast salvestatud teavet ja lisab selle kasutaja päringule, pakkudes põhivahendile olulist konteksti (sarnaselt RAG-le).

### Mälu optimeerimine

• **Latentsuse haldamine**: Kasutajainteraktsioonide aeglustumise vältimiseks saab algselt kasutada odavamat ja kiiremat mudelit, et kiiresti kontrollida, kas teave on väärt salvestamist või meenutamist, kutsudes keerukama väljavõtmise/meenutamise protsessi ainult vajadusel.

• **Teadmistebaasi hooldus**: Kasvava teadmistebaasi jaoks saab harvemini kasutatavat teavet viia "külmsäilitusse", et hallata kulusid.

## Kas sul on rohkem küsimusi agendi mälu kohta?

Liitu [Azure AI Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda vastuvõtuaegadel ja saada vastuseid oma AI-agentide küsimustele.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.