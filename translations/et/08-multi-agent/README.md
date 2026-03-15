[![Mitmeagendi kujundus](../../../translated_images/et/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klõpsa ülaloleval pildil, et vaadata selle tunni videot)_

# Mitmeagendi kujundusmustrid

Niipea kui hakkate töötama projektiga, mis hõlmab mitut agenti, peate kaaluma mitmeagendi kujundusmustrit. Kuid ei pruugi olla kohe selge, millal üle minna mitme agenti kasutamisele ja millised on selle eelised.

## Sissejuhatus

Selles tunnis püüame vastata järgmistele küsimustele:

- Millistes olukordades on mitmeagente mõistlik kasutada?
- Millised on mitmeagentide kasutamise eelised võrreldes üheainsa agendiga, kes teeb mitut ülesannet?
- Millised on mitmeagendi kujundusmustri rakendamise komponendid?
- Kuidas omada nähtavust selle üle, kuidas mitmed agendid omavahel suhtlevad?

## Õpieesmärgid

Pärast seda tundi peaksite olema võimeline:

- Tuvastama olukordi, kus mitmeagente on mõistlik kasutada
- Tuvastama mitmeagentide kasutamise eeliseid võrreldes üheainsa agendiga
- Mõistma mitmeagendi kujundusmustri rakendamise põhikomponente

Mis on suurem pilt?

*Mitmeagentne kujundusmuster võimaldab mitmel agendil töötada koos ühise eesmärgi saavutamiseks*.

Seda mustrit kasutatakse laialdaselt erinevates valdkondades, kaasa arvatud robotitehnika, autonoomsed süsteemid ja hajutatud arvutustehnika.

## Situatsioonid, kus mitmeagente on mõistlik kasutada

Millised olukorrad on hea kasutada mitmeagente? Vastus on, et on palju olukordi, kus mitmeagentide kasutamine on kasulik, eriti järgmistes juhtumites:

- **Suured töömahud**: Suured töömahud saab jagada väiksemateks ülesanneteks ja määrata erinevatele agentidele, võimaldades paralleelset töötlemist ja kiiremat lõpetamist. Hea näide on suurandmete töötlemise ülesanne.
- **Kompleksed ülesanded**: Nagu suurte töömahude puhul, saab ka keerukad ülesanded jagada väiksemateks alaupustusteks ja määrata erinevatele agentidele, kellest igaüks spetsialiseerub ülesande konkreetsele aspektile. Hea näide on autonoomsete sõidukite puhul, kus erinevad agendid haldavad navigeerimist, takistuste tuvastamist ja suhtlust teiste sõidukitega.
- **Mitmekesine erialane oskus**: Erinevatel agentidel võib olla erinev ekspertteadmiste pagas, mis võimaldab neil töödelda ülesande erinevaid aspekte tõhusamalt kui üks agent. Näiteks tervishoius võivad agendid hallata diagnostikat, raviplaane ja patsientide jälgimist.

## Mitmeagentide kasutamise eelised võrreldes üheainsa agendiga

Üksikagentne süsteem võib toimida hästi lihtsate ülesannete puhul, kuid keerukamate ülesannete puhul võib mitmeagentne lähenemine anda mitmeid eeliseid:

- **Spetsialiseerumine**: Iga agent võib olla spetsialiseerunud konkreetsele ülesandele. Kui ühes agendis puudub spetsialiseerumine, võib teil olla agent, kes oskab kõike, kuid võib keerulise ülesande korral segadusse sattuda. Näiteks võib ta lõpuks teha ülesande, milleks ta ei ole kõige paremini sobitatud.
- **Skaleeritavus**: Süsteemi on lihtsam skaleerida, lisades rohkem agente, kui koormata üht agenti üle.
- **Veakindlus**: Kui üks agent ebaõnnestub, võivad teised jätkata, tagades süsteemi usaldusväärsuse.

Vaatame ühte näidet: broneerime kasutajale reisi. Üksikagentne süsteem peaks tegelema kõigi reisi broneerimise protsesside aspektidega — alates lendude leidmisest kuni hotellide ja rendiautode broneerimiseni. Selle saavutamiseks peaks agendil olema tööriistad kõigi nende ülesannete käsitlemiseks. See võib viia keeruka ja monoliitse süsteemi tekkeni, mida on raske hooldada ja skaleerida. Mitmeagentne süsteem seevastu võiks omada erinevaid agente, kes on spetsialiseerunud lendude leidmisele, hotellide broneerimisele ja rendiautodele. See muudaks süsteemi modulaarsemaks, hooldatavamaks ja skaleeritavamaks.

Võrrelge seda reisibürooga, mida haldab väike pereettevõte, ja frantsiisiga. Pereettevõttes tegeleb üks agent kõigi reisi broneerimise aspektidega, samas kui frantsiisis oleks erinevaid agente, kes tegelevad reisi erinevate aspektidega.

## Mitmeagendi kujundusmustri rakendamise põhikomponendid

Enne kui saate rakendada mitmeagendi kujundusmustri, peate mõistma, millest see muster koosneb.

Teeme selle konkreetsemaks, vaadates taas näidet kasutajale reisi broneerimisest. Sellisel juhul hõlmavad põhikomponendid järgmist:

- **Agentidevaheline suhtlus**: Agentidel, kes tegelevad lendude leidmise, hotellide ja rendiautode broneerimisega, tuleb suhelda ja jagada teavet kasutaja eelistuste ja piirangute kohta. Peate otsustama suhtlusprotokollide ja -meetodite üle. Konkreetsemalt tähendab see seda, et lendude leidmise agent peab suhtlema hotellide broneerimise agendiga, et tagada hotelli broneerimine samadel kuupäevadel kui lend. See tähendab, et agentide vahel tuleb jagada teavet kasutaja reisi kuupäevade kohta — peate otsustama *millised agendid infot jagavad ja kuidas nad infot jagavad*.
- **Koordineerimismehhanismid**: Agendid peavad koordineerima oma tegevusi, et tagada kasutaja eelistuste ja piirangute täitmine. Näiteks võib kasutaja eelistada hotelli, mis asub lennujaama lähedal, samas kui piiranguks võib olla, et rendiautod on saadaval ainult lennujaamas. See tähendab, et hotellide broneerimise agent peab koordineerima rendiautode broneerimise agendiga, et tagada kasutaja eelistuste ja piirangute täitmine. See tähendab, et peate otsustama *kuidas agendid oma tegevusi koordineerivad*.
- **Agendi arhitektuur**: Agentidel peab olema sisemine struktuur otsuste tegemiseks ja õppimiseks oma interaktsioonidest kasutajaga. See tähendab, et lendude leidmise agendil peab olema sisemine struktuur otsustamiseks, milliseid lende kasutajale soovitada. See tähendab, et peate otsustama *kuidas agendid otsuseid teevad ja õpivad oma interaktsioonidest kasutajaga*. Näiteks võib lendude leidmise agent kasutada masinaõppemudelit, et soovitada lende kasutaja varasemate eelistuste alusel.
- **Nähtavus mitmeagendi interaktsioonides**: Peate omama ülevaadet sellest, kuidas mitmed agendid omavahel suhtlevad. See tähendab, et teil peavad olema tööriistad ja tehnikad agentide tegevuste ja interaktsioonide jälgimiseks. See võib olla logimise ja jälgimise tööriistade, visualiseerimistööriistade ja jõudlusmõõdikute kujul.
- **Mitmeagendi mustrid**: Mitmeagendisüsteemide rakendamiseks on erinevaid mustreid, näiteks tsentraliseeritud, detsentraliseeritud ja hübriidarhitektuurid. Peate otsustama mustri, mis sobib kõige paremini teie kasutusjuhtumile.
- **Inimene tsüklis**: Enamiku juhtude puhul on inimesel roll protsessis ja peate määrama, millal agendid peaksid küsima inimsekkumist. See võib olla näiteks siis, kui kasutaja soovib konkreetset hotelli või lendu, mida agendid ei ole soovitanud, või kui kasutaja soovib kinnitust enne lennu või hotelli broneerimist.

## Nähtavus mitmeagendi interaktsioonides

On oluline, et teil oleks nähtavus selle üle, kuidas mitmed agendid omavahel suhtlevad. See nähtavus on oluline veaotsinguks, optimeerimiseks ja kogu süsteemi tõhususe tagamiseks. Selle saavutamiseks vajate tööriistu ja tehnikaid agentide tegevuste ja interaktsioonide jälgimiseks. See võib väljenduda logimise ja jälgimise tööriistade, visualiseerimistööriistade ja jõudlusmõõdikute kaudu.

Näiteks reisi broneerimise puhul võiksite omada juhtpaneeli, mis näitab iga agendi staatust, kasutaja eelistusi ja piiranguid ning agentidevahelisi interaktsioone. See juhtpaneel võiks kuvada kasutaja reisi kuupäevad, lendude soovitused lendude agendilt, hotellisoovitused hotellide agendilt ja rendiautode soovitused rendiautode agendilt. See annaks selge ülevaate sellest, kuidas agendid omavahel suhtlevad ja kas kasutaja eelistusi ning piiranguid täidetakse.

Vaatame neid aspekte üksikasjalikumalt.

- **Logimise ja jälgimise tööriistad**: Tahate, et iga agendi tehtud tegevus oleks logitud. Logikirje võib salvestada teavet selle agendi kohta, kes tegevuse tegi, tehtud tegevuse, tegevuse aja ja tegevuse tulemuse kohta. Seda teavet saab seejärel kasutada veaotsinguks, optimeerimiseks ja muuks.
- **Visualiseerimistööriistad**: Visualiseerimistööriistad võivad aidata teil agentide vahelisi interaktsioone intuitiivsemalt näha. Näiteks võiksite omada graafikut, mis näitab informatsiooni voogu agentide vahel. See võib aidata tuvastada kitsaskohti, ebatõhususi ja muid probleeme süsteemis.
- **Tulemuslikkuse mõõdikud**: Tulemuslikkuse mõõdikud aitavad jälgida mitmeagendisüsteemi tõhusust. Näiteks võite jälgida ülesande täitmiseks kulunud aega, ühe ajaühiku kohta lõpetatud ülesannete arvu ning agentide soovituste täpsust. See teave võib aidata tuvastada parenduskohti ja süsteemi optimeerida.

## Mitmeagendi mustrid

Uurime mõningaid konkreetseid mustreid, mida saab kasutada mitmeagendi rakenduste loomiseks. Siin on mõned huvitavad mustrid, mida tasub kaaluda:

### Rühmavestlus

See muster on kasulik, kui soovite luua rühma vestluse rakendust, kus mitu agenti saavad omavahel suhelda. Selle mustri tüüpilised kasutusjuhtumid hõlmavad meeskonnatööd, kliendituge ja sotsiaalvõrgustikke.

Selles mustris esindab iga agent rühma vestluse kasutajat ning sõnumeid vahetatakse agentide vahel sõnumiprotoooli abil. Agendid saavad saata sõnumeid rühma vestlusele, vastu võtta sõnumeid rühma vestlusest ja vastata teiste agentide sõnumitele.

Seda mustrit saab rakendada tsentraliseeritud arhitektuuri abil, kus kõik sõnumid suunatakse läbi keskse serveri, või detsentraliseeritud arhitektuuri abil, kus sõnumeid vahetatakse otse.

![Group chat](../../../translated_images/et/multi-agent-group-chat.ec10f4cde556babd.webp)

### Üleandmine

See muster on kasulik, kui soovite luua rakenduse, kus mitu agenti saavad omavahel ülesandeid üle anda.

Selle mustri tüüpilised kasutusjuhtumid hõlmavad kliendituge, ülesannete haldust ja töövoo automatiseerimist.

Selles mustris esindab iga agent ülesannet või sammu töövoos ning agendid saavad eeldefineeritud reeglite alusel ülesandeid teistele agentidele üle anda.

![Hand off](../../../translated_images/et/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Koostööpõhine filtreerimine

See muster on kasulik, kui soovite luua rakenduse, kus mitu agenti saavad koostööd teha, et teha kasutajatele soovitusi.

Miks soovite mitme agenti koostööd teha? Sest iga agent võib omada erinevat ekspertteadmiste valdkonda ja panustada soovitusprotsessi erinevatel viisidel.

Võtame näiteks olukorra, kus kasutaja soovib soovitust parima aktsia kohta, mida börsil osta.

- **Tööstuse ekspert**:. Üks agent võib olla konkreetse tööstusharu ekspert.
- **Tehniline analüüs**: Teine agent võib olla tehnilise analüüsi ekspert.
- **Fundamentaalne analüüs**: Ja kolmas agent võib olla fundamentaalse analüüsi ekspert. Koostöös suudavad need agendid anda kasutajale põhjalikuma soovituse.

![Recommendation](../../../translated_images/et/multi-agent-filtering.d959cb129dc9f608.webp)

## Stsenaarium: tagasimakse protsess

Võtame olukorra, kus klient proovib saada toote eest tagasimakset — selles protsessis võib osaleda üsna palju agente, kuid jagame need agentideks, mis on spetsiifilised sellele protsessile, ja üldisteks agentideks, mida saab kasutada ka teistes protsessides.

**Tagasimakseprotsessile spetsiifilised agendid**:

Järgnevad on mõned agendid, kes võiksid osaleda tagasimakse protsessis:

- **Kliendiagent**: See agent esindab klienti ja vastutab tagasimakse protsessi algatamise eest.
- **Müüjaagent**: See agent esindab müüjat ja vastutab tagasimakse töötlemise eest.
- **Makseagent**: See agent esindab makseprotsessi ja vastutab kliendi makse tagasimaksmise eest.
- **Lahendusagent**: See agent esindab lahenduse protsessi ja vastutab tagasimakse protsessi käigus tekkivate probleemide lahendamise eest.
- **Vastavusagent**: See agent esindab vastavuse protsessi ja vastutab selle eest, et tagasimakse protsess vastab regulatsioonidele ja poliitikatele.

**Üldised agendid**:

Neid agente saab kasutada teie ettevõtte muudes osades.

- **Saatmisagent**: See agent esindab saatmisprotsessi ja vastutab toote tagasisaatmise eest müüjale. Seda agenti saab kasutada nii tagasimakse protsessis kui ka toote üldises saatmises ostu puhul.
- **Tagasisideagent**: See agent esindab tagasiside protsessi ja vastutab kliendi tagasiside kogumise eest. Tagasisidet võidakse küsida igal ajal, mitte ainult tagasimakse protsessi ajal.
- **Eskalatsiooniagent**: See agent esindab eskalatsiooni protsessi ja vastutab probleemide tõstmise eest kõrgemale tasemele. Seda tüüpi agenti saab kasutada igas protsessis, kus on vaja probleemi eskaleerida.
- **Teavituseagent**: See agent esindab teavituste protsessi ja vastutab kliendi teavitamise eest tagasimakse erinevates etappides.
- **Analüütikaagent**: See agent esindab analüütika protsessi ja vastutab tagasimakse protsessiga seotud andmete analüüsi eest.
- **Auditagent**: See agent esindab auditeerimise protsessi ja vastutab tagasimakse protsessi auditeerimise eest, et tagada protsessi nõuetekohasus.
- **Aruandlusagent**: See agent esindab aruandluse protsessi ja vastutab aruannete genereerimise eest tagasimakse protsessi kohta.
- **Teadmusagent**: See agent esindab teadmisteprotsessi ja vastutab tagasimakse protsessiga seotud teadmistebaasi haldamise eest. See agent võib olla kursis nii tagasimaksete kui ka teie äri muude osadega.
- **Turvaagent**: See agent esindab turvaprotsessi ja vastutab tagasimakse protsessi turvalisuse tagamise eest.
- **Kvaliteediagent**: See agent esindab kvaliteediprotsessi ja vastutab tagasimakse protsessi kvaliteedi tagamise eest.

Eelnevalt loetlesime üsna palju agente — nii tagasimakse protsessi spetsiifilisi agente kui ka üldisi agente, keda saab kasutada teie äri muudes osades. Loodetavasti annab see teile ettekujutuse selle kohta, kuidas otsustada, milliseid agente kasutada teie mitmeagendilise süsteemi puhul.

## Ülesanne

Disainige mitmeagendiline süsteem klienditoe protsessi jaoks. Tuvastage protsessis osalevad agendid, nende rollid ja vastutused ning kuidas nad omavahel suhtlevad. Kaasake nii klienditoega seotud spetsiifilised agendid kui ka üldised agendid, keda saab kasutada teie äri muudes osades.
> Mõtle enne, kui loed järgmist lahendust — sul võib vaja minna rohkem agente, kui arvad.
> VIHJE: Mõtle klienditoe protsessi erinevatele etappidele ning ka süsteemis vajalikele agentidele.

## Lahendus

[Lahendus](./solution/solution.md)

## Teadmiste kontroll

Küsimus: Millal tuleks kaaluda mitme agendi kasutamist?

- [ ] A1: Kui sul on väike töökoormus ja lihtne ülesanne.
- [ ] A2: Kui sul on suur töökoormus.
- [ ] A3: Kui sul on lihtne ülesanne.

[Lahenduse viktoriin](./solution/solution-quiz.md)

## Kokkuvõte

Selles õppetükis vaatlesime mitme agendi disainimustrit, sealhulgas olukordi, kus mitme agendi kasutamine on sobiv, mitme agendi eeliseid võrreldes ühe agendiga, mitme agendi disainimustri rakendamise põhielemente ning seda, kuidas saavutada ülevaade sellest, kuidas mitmed agendid omavahel suhtlevad.

### Kas sul on veel küsimusi mitme agendi disainimustri kohta?

Liitu [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), et kohtuda teiste õppuritega, osaleda konsultatsioonitundidel ning saada vastuseid oma AI agentide küsimustele.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Frameworki dokumentatsioon</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentsete disainimustrid</a>


## Eelmine õppetund

[Planeerimise disain](../07-planning-design/README.md)

## Järgmine õppetund

[Metakognitsioon AI agentides](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsust, palun pange tähele, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või väärtõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->