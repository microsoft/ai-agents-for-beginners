# Konteksti inseneritöö AI agentidele

[![Context Engineering](../../../translated_images/et/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klõpsa ülaloleval pildil, et vaadata selle tunni videot)_

Rakenduse keerukuse mõistmine, mille jaoks AI agenti ehitad, on oluline usaldusväärse agenti loomisel. Me peame looma AI agente, kes haldavad efektiivselt informatsiooni, et lahendada keerukaid vajadusi, mis ületavad pelga promptide inseneritöö.

Selles õppetükis vaatame, mis on konteksti inseneritöö ja selle roll AI agentide loomisel.

## Sissejuhatus

See õppetund käsitleb:

• **Mis on konteksti inseneritöö** ja miks see erineb promptide inseneritööst.

• **Efektiivse konteksti inseneritöö strateegiaid**, sealhulgas kuidas kirjutada, valida, tihendada ja isoleerida infot.

• **Tavalisi konteksti tõrkeid**, mis võivad AI agenti rikkuda, ja kuidas neid parandada.

## Õpieesmärgid

Pärast selle tunni lõpetamist tead, kuidas:

• **Määratleda konteksti inseneritöö** ja eristada seda promptide inseneritööst.

• **Tuvastada konteksti põhikomponendid** suurte keelemudelite rakendustes.

• **Rakendada strateegiaid kontekti kirjutamiseks, valimiseks, tihendamiseks ja isoleerimiseks** agentide jõudluse parandamiseks.

• **Tuvastada tavalisi kontekstitõrkeid** nagu mürgitamine, tähelepanu hajumine, segadus ja vastuolu, ning rakendada leevendusmeetodeid.

## Mis on konteksti inseneritöö?

AI agentide kontekst juhib AI agendi planeerimist teatud toimingute tegemiseks. Konteksti inseneritöö on praktika tagada, et AI agentil on õige info, et täita järgmine ülesande samm. Konteksti aken on piiratud suurusega, seepärast peame agendi looja rollis üles ehitama süsteeme ja protsesse, et hallata info lisamist, eemaldamist ja kokkusurumist konteksti aknas.

### Promptide inseneritöö vs konteksti inseneritöö

Promptide inseneritöö keskendub ühele komplektile staatilisi juhiseid, mis juhivad AI agente efektiivselt reeglite kogumiga. Konteksti inseneritöö käsitleb dünaamilise infokogumi haldamist, kaasa arvatud esialgne prompt, et tagada AI agendil vajalik informatsioon aja jooksul. Põhimõte on muuta see protsess korduvaks ja usaldusväärseks.

### Konteksti tüübid

[![Types of Context](../../../translated_images/et/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Oluline on meeles pidada, et kontekst ei ole vaid üks asi. AI agendi jaoks vajalik info võib tulla erinevatest allikatest ja meie ülesanne on tagada agendi ligipääs neile allikatele:

Konteksti tüübid, mida AI agent võib vajada haldamiseks, hõlmavad:

• **Juhised:** Need on agenti "reeglid" – promptid, süsteemisõnumid, mõne näite kasutamine (näitamaks, kuidas midagi teha) ja tööriistade kirjeldused, mida agent saab kasutada. Siin kattub promptide inseneritöö fookus konteksti inseneritööga.

• **Teadmised:** See hõlmab fakte, andmeid andmebaasidest või pikaajalisi mälestusi, mida agent on kogunud. Siia kuulub ka Retrieval Augmented Generation (RAG) süsteemi integreerimine, kui agent vajab ligipääsu erinevatele teadmusbaasidele ja andmebaasidele.

• **Tööriistad:** Need on väliste funktsioonide, API-de ja MCP serverite määratlused, mida agent saab kutsuda, koos tagasisidega (tulemustega), mida ta nende kasutamisest saab.

• **Vestluse ajalugu:** Jooksev dialoog kasutajaga. Aja jooksul pikenevad ja keerukamaks muutuvad need vestlused, võtavad ruumi konteksti aknas.

• **Kasutaja eelistused:** Infot, mida on kasutaja eelistuste kohta aja jooksul kogutud. Seda võib salvestada ja kasutada oluliste otsuste tegemisel kasutaja abistamiseks.

## Efektiivse konteksti inseneritöö strateegiad

### Planeerimisstrateegiad

[![Context Engineering Best Practices](../../../translated_images/et/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Hea konteksti inseneritöö algab heast planeerimisest. Siin on lähenemine, mis aitab alustada mõtlemist, kuidas rakendada konteksti inseneritöö mõistet:

1. **Määra selged tulemused** - AI agentidele määratavate ülesannete tulemused peaksid olema selgelt sõnastatud. Vasta küsimusele - "Milline näeb maailm välja, kui AI agent on oma ülesande lõpetanud?" Teisisõnu, milline muutus, info või vastus peaks kasutajal olema pärast AI agendiga suhtlemist.
2. **Kaardista kontekst** - Kui oled tulemused määratlenud, pead vastama küsimusele "Millist infot vajab AI agent selle ülesande täitmiseks?". Nii saad hakata kaardistama, kus see info asub.
3. **Loo konteksti vood** - Kui tead, kus info on, pead vastama küsimusele "Kuidas saab agent selle info kätte?". Seda saab teha mitmel moel, sh RAG süsteemi, MCP serverite ja muude tööriistade kasutamise kaudu.

### Praktilised strateegiad

Planeerimine on tähtis, kuid kui info hakkab voolama meie agendi konteksti aknasse, vajame praktilisi strateegiaid selle haldamiseks:

#### Konteksti haldamine

Kuigi osa infot lisatakse konteksti aknasse automaatselt, on konteksti inseneritöö aktiivsema rolli võtmine selles infosisus võimalik mitme strateegiaga:

 1. **Agendi märkmeleht**
 See võimaldab AI agendil teha märkmeid asjakohase info kohta jooksva ülesande ja kasutajategevuste kohta ühe seansi jooksul. See peaks asuma konteksti aknast väljas, failis või tööajal objekti kujul, mida agent saab vajadusel selle seansi jooksul hiljem kasutada.

 2. **Mälestused**
 Märkmelehed sobivad info haldamiseks ühe seansi konteksti aknast väljaspool. Mälestused võimaldavad agentidel salvestada ja taastada asjakohast infot mitme seansi jooksul. Sellesse võib kuuluda kokkuvõtteid, kasutaja eelistusi ja tagasisidet tulevikuks paremuse saavutamiseks.

 3. **Konteksti tihendamine**
  Kui konteksti aken tuleb suureks ja hakkab oma piiri lähedale jõudma, saab kasutada selliseid tehnikaid nagu kokkuvõtete tegemine ja kärpimine. See hõlmab ainult kõige asjakohasema info hoidmist või vanemate sõnumite eemaldamist.
  
 4. **Mitme agendi süsteemid**
  Mitme agendi süsteemi arendamine on konteksti inseneritöö vorm, kuna iga agendil on oma konteksti aken. Kuidas seda konteksti jagatakse ja erinevatele agentidele edasi antakse, on midagi, mida tuleb nende süsteemide ehitamisel planeerida.
  
 5. **Liivakasti keskkonnad**
  Kui agent peab käivitama koodi või töötlema suuri infokoguseid dokumendis, võib see võtta palju token'e tulemuste töötlemiseks. Selle asemel, et see kõik jääks konteksti aknasse salvestatuks, saab agent kasutada liivakasti keskkonda, mis suudab koodi käivitada ning lugeda ainult tulemusi ja muud asjakohast infot.
  
 6. **Tööaja oleku objektid**
   Seda tehakse info konteinerite loomisega, et hallata olukordi, kus agendil on vaja teatud infole ligi pääseda. Kompleksi ülesande puhul võimaldab see agentidel salvestada iga alamülesande tulemusi samm-sammult, hoides konteksti seotud ainult selle konkreetse alamülesandega.

#### Konteksti kontrollimine

Pärast ühe sellise strateegia rakendamist tasub kontrollida, mida järgmise mudelikõne ajal tegelikult vastu võeti. Kasulik silumiseks küsimus on:

> Kas agent laadis liiga palju konteksti, vale konteksti või jäi kontekst puudu, mida ta vajas?

Selle küsimuse vastamiseks ei pea logima tooreid promte, tööriistade väljundeid ega mälu sisu. Tootmises eelista väikseid konteksti kontrollikirjeid, mis sisaldavad loendusi, ID-sid, räsi ja poliitikamärke:

- **Valik:** Jälgi, kui palju kandidaatkilde, tööriistu või mälestusi kaaluti, kui palju neist valiti ja milline reegel või skoor põhjustas teiste filtreerimise.
- **Tihendamine:** Salvestage allika vahemik või jälgimis-ID, kokkuvõtte ID, hinnanguline tokenite arv enne ja pärast tihendamist ning kas tooraine sisu jäeti järgmise kõne juurest välja.
- **Isoleerimine:** Märgi, milline alamülesanne käis teises agendis, seansis või liivakastis, milline piiritletud kokkuvõte tagastati ja kas mahukas tööriista väljund jäi emateenuse agendi kontekstist väljapoole.
- **Mälu ja RAG:** Salvesta taastatud dokumendi ID-d, mälu ID-d, skoorid, valitud ID-d ja redigeerimise olek täistekstide asemel.
- **Turvalisus ja privaatsus:** Eelista räside, ID-de, tokenite korvide ja poliitikamärkide kasutamist tundlike promptide teksti, tööriista argumentide, tööriista tulemuste või kasutaja mälu sisu asemel.

Eesmärk ei ole hoida rohkem konteksti, vaid jätta piisavalt tõendeid, et arendaja saaks tuvastada, millisest konteksti strateegiast oli jutt ja kas see mõjutas järgmist mudelikõnet soovitud viisil.

### Näide konteksti inseneritööst

Oletame, et tahame AI agendilt **"Broneeri mulle reis Pariisi."**

• Lihtne agent, mis kasutab ainult promptide inseneritööd, vastaks näiteks: **"Olgu, millal soovid Pariisi sõita?"** See töötles ainult sinu otsest küsimust sellel ajal, kui kasutaja seda küsis.

• Agent, kes kasutab siin käsitletud konteksti inseneritöö strateegiaid, teeks palju enamat. Enne vastamist võib tema süsteem näiteks:

  ◦ **Kontrollida sinu kalendrit** saadaolevate kuupäevade jaoks (saades reaalajas andmeid).

 ◦ **Meenutada varasemaid reisieelistusi** (pikaajaline mälu), näiteks eelistatud lennufirma, eelarve või kas eelistad otselende.

 ◦ **Tuua välja saadaolevad tööriistad** lennupiletite ja hotellibroneeringu tegemiseks.

- Siis võiks näidisvastus olla: "Hei [Sinu nimi]! Märkan, et oled vaba oktoobri esimesel nädalal. Kas otsin otse lende Pariisi [Eelistatud lennufirma]ga tavapärase [eelarve] piires?" See rikkalik, kontekstitundlik vastus demonstreerib konteksti inseneritöö võimu.

## Levinud kontekstitõrked

### Konteksti mürgitamine

**Mis see on:** Kui hallutsinatsioon (LLMi poolt genereeritud valeinfo) või viga jõuab konteksti ja sellele viidatakse korduvalt, põhjustades agendi võimatute eesmärkide ja mitte­tõsiste strateegiate tekkimist.

**Mida teha:** Rakenda **konteksti valideerimist** ja **karantiini**. Kontrolli infot enne selle lisamist pikaajalisse mällu. Kui avastatakse võimalik mürgitamine, alusta uut konteksti lõime, et takistada halbade andmete levikut.

**Reisibroneeringu näide:** Agent hallutsineerib **otse lennu väiksel kohalikul lennujaamal kaugesse rahvusvahelisse linna**, kuhu tegelikult ei lenda rahvusvahelisi lende. See mittetegutsev lennuinfo salvestatakse konteksti. Hiljem, kui küsid agentilt broneerimist, üritab see kogu aeg leida pileteid sellele võimatule marsruudile, põhjustades korduvaid vigu.

**Lahendus:** Rakenda samm, mis **valideerib lennu olemasolu ja marsruudid reaalajas API abil** _enne_ lennuinfo lisamist agendi töökonteksti. Kui valideerimine ebaõnnestub, pannakse valeinfo "karantiini" ega kasutata edasi.

### Konteksti tähelepanu hajumine

**Mis see on:** Kui kontekst muutub nii suureks, et mudel keskendub liiga palju kogunenud ajaloole ja unustab kasutada treeningu käigus õpitut, põhjustades korduvaid või ebaotstarbekaid tegevusi. Mudelid hakkavad vigu tegema isegi enne, kui konteksti aken on täis.

**Mida teha:** Kasuta **konteksti kokkusurumist**. Aeg-ajalt tihenda kogutud infot lühemateks kokkuvõteteks, hoides olulisi detaile ja eemaldades liigse ajaloo. See aitab "lähtestada" fookuse.

**Reisibroneeringu näide:** Oled kauem arutanud mitmeid reisunumbreid, sh detailselt rääkinud oma kahe aasta tagusest matkapäevikus. Kui lõpuks palud **"Leia odav lend järgmisel kuul"**, muutub agent vanade, ebaoluliste detailide tõttu segadusse ja küsib korduvalt sinu matkapakki või varasemaid marsruute, ignoreerides sinu praegust küsimust.

**Lahendus:** Pärast teatavat arvu küsimusi või kui kontekst liiga suureks läheb, peaks agent **kokku võtma vestluse kõige uuemad ja asjakohasemad osad** – keskendudes sinu hetke reisikuupäevadele ja sihtkohale – ning kasutama seda tihendatud kokkuvõtet järgmiseks LLM kõneks, visates vähem olulise ajaloo kõrvale.

### Konteksti segadus

**Mis see on:** Kui mittevajalik kontekst, sageli liiga paljude saadaolevate tööriistade kujul, paneb mudeli genereerima halbu vastuseid või kutsuma sobimatuid tööriistu. Väiksemad mudelid on sellele eriti vastuvõtlikud.

**Mida teha:** Rakenda **tööriistade valiku haldamist** RAG tehnikate abil. Salvestage tööriistade kirjeldused vektoriandmebaasi ja vali iga ülesande jaoks _ainult_ kõige asjakohasemad tööriistad. Uuringud näitavad, et tööriistade valik tuleks piirata alla 30.

**Reisibroneeringu näide:** Sinu agendil on ligipääs kümnetele tööriistadele: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` jne. Küsimus on, **"Mis on parim viis Pariisis ringi liikumiseks?"** Paljude tööriistade hulgast võib agent segadusse sattuda ja proovida kutsuda näiteks `book_flight` Pariisi sees või `rent_car`, kuigi eelistad ühistransporti, sest tööriistade kirjeldused võivad kattuda või ta ei suuda valida parimat.

**Lahendus:** Kasuta **RAG-i üle tööriistade kirjelduste**. Kui küsid Pariisis ringiliikumise kohta, saab süsteem dünaamiliselt tuua välja _ainult_ kõige asjakohasemad tööriistad nagu `rent_car` või `public_transport_info` vastavalt sinu päringule, esitades LLM-ile fokuseeritud tööriistade komplekti.

### Konteksti vastuolu

**Mis see on:** Kui konfliktne info eksisteerib kontekstis, põhjustades ebajärjekindlat mõtlemist või halbu lõppvastuseid. Seda juhtub tihti, kui info saabub etapiti ja varasemad, valed eeldused jäävad konteksti.

**Mida teha:** Kasuta **konteksti kärpimist** ja **väljavahetamist**. Kärpimine tähendab aegunud või vastuolulise info eemaldamist uute andmete saabudes. Väljavahetamine annab mudelile eraldi "märkmelehe" tööruumi, kus infot töödelda ilma peamist konteksti ülekoormamata.


**Reisibroneerimise näide:** Sa ütled oma agendile algselt, **"Ma tahan lennata majandusklassis."** Hiljem vestluse käigus muudad meelt ja ütled, **"Tegelikult, selle reisi jaoks valime äriklassi."** Kui mõlemad juhised jäävad konteksti alles, võib agent saada vastuolulisi otsingutulemusi või jääda segadusse, millist eelistust eelistada.

**Lahendus:** Rakenda **konteksti kärpimist**. Kui uus juhis on vastuolus vana juhisega, eemaldatakse vanem juhis või asendatakse see kontekstis selgelt. Alternatiivselt võib agent kasutada **märkmelehte**, et lepitada vastuolulisi eelistusi enne otsuse tegemist, tagades, et ainult lõplik ja ühtne juhis juhib selle toiminguid.

## Kas sul on veel küsimusi konteksti insenertehnika kohta?

Liitu [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)-iga, et kohtuda teiste õppijatega, osaleda konsultatsioonides ja saada vastused oma AI agentide küsimustele.
## Eelmine õppetund

[Agentic Protocols](../11-agentic-protocols/README.md)

## Järgmine õppetund

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->