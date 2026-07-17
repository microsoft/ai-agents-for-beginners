[![Mitmeagendi disain](../../../translated_images/et/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

# Mitmeagendi disainimustrid

Niipea kui hakkad töötama projektiga, mis hõlmab mitut agenti, pead kaaluma mitmeagendi disainimustrit. Kuid võib-olla ei ole kohe selge, millal üle minna mitmeagentidele ja millised on selle eelised.

## Sissejuhatus

Selles õppetunnis püüame vastata järgmistele küsimustele:

- Millistes olukordades on mitmeagentide kasutamine asjakohane?
- Millised on mitmeagentide kasutamise eelised võrreldes üheainsa agendiga, kes teeb mitut ülesannet?
- Millised on mitmeagendi disainimustri rakendamise põhielemendid?
- Kuidas meil on ülevaade sellest, kuidas mitmed agendid omavahel suhtlevad?

## Õpieesmärgid

Pärast seda õppetundi peaksid suutma:

- Tuvastada olukorrad, kus mitmeagendid on asjakohased
- Tunda ära mitmeagentide kasutamise eelised võrreldes üheainsa agendiga.
- Mõista mitmeagendi disainimustri rakendamise põhielemente.

Milline on suurem pilt?

*Mitmeagendid on disainimuster, mis võimaldab mitmel agendil koos töötada ühise eesmärgi saavutamiseks*.

Seda mustrit kasutatakse laialdaselt erinevates valdkondades, sealhulgas robootikas, isesõitvates süsteemides ja hajutatud arvutusteaduses.

## Olukorrad, kus mitmeagendid on asjakohased

Millised olukorrad on siis head näited mitmeagentide kasutamisest? Vastus on, et on palju olukordi, kus mitme agenti kasutamine on kasulik, eriti järgmistes juhtudel:

- **Suured töökoormused**: Suured tööde hulgad saab jaotada väiksemateks ülesanneteks ja määrata erinevatele agentidele, võimaldades paralleelprotsessimist ja kiiremat lõpetamist. Näiteks suurandmete töötlemise ülesanne.
- **Keerukad ülesanded**: Keerukaid ülesandeid, nagu suured töökoormad, saab jagada väiksemateks aluseksanneteks ja määrata erinevatele agentidele, kes on spetsialiseerunud teatud ülesande aspektile. Näiteks isesõitvad sõidukid, kus erinevad agendid haldavad navigeerimist, takistuste tuvastamist ja suhtlust teiste sõidukitega.
- **Mitmekesine asjatundlikkus**: Erinevatel agentidel võib olla mitmekesine oskusteave, mis võimaldab neil käsitleda eri ülesandeid efektiivsemalt kui üks agent. Näiteks tervishoiu valdkonnas, kus agendid haldavad diagnostikat, raviplaane ja patsiendi jälgimist.

## Mitmeagentide kasutamise eelised võrreldes üheainsa agendiga

Üksikagentne süsteem võiks hästi töötada lihtsate ülesannete puhul, kuid keerukamate ülesannete puhul toob mitmeagentide kasutamine mitmeid eeliseid:

- **Spetsialiseerumine**: Iga agent võib olla spetsialiseerunud konkreetsele ülesandele. Üheainsa agendi mittespetsialiseerumine tähendab, et agent võib teha kõike, aga võib keeruka ülesande ees segadusse sattuda ja teha ülesande, mille jaoks ta pole kõige sobivam.
- **Mastaapsus**: Süsteemi on kergem skaleerida, lisades rohkem agente, kui üle koormata üht agenti.
- **Rikkekindlus**: Kui üks agent ebaõnnestub, saavad teised edasi töötada, tagades süsteemi töökindluse.

Võtame näiteks reisi broneerimise kasutaja jaoks. Üksikagentne süsteem peaks haldama kõiki reisi broneerimise protsessi aspekte, alates lendude leidmisest kuni hotellide ja autorendi broneerimiseni. Selle saavutamiseks peaks agendil olema tööriistad kõigi nende ülesannete haldamiseks. See võib viia keeruka ja monoliitse süsteemini, mida on raske hooldada ja skaleerida. Mitmeagentne süsteem võiks seevastu omada erinevaid agente – lennupiletite leidmiseks, hotellide broneerimiseks ja autorendi haldamiseks. See muudaks süsteemi modulaarsemaks, kergemini hallatavaks ja skaleeritavaks.

Võrreldes reisibürooga, mida juhib pereettevõte, ja reisibürooga, mida juhib frantsiis. Pereettevõtte puhul haldab kogu reisi broneerimist üks agent, samas kui frantsiis kasutab erinevaid agente, kes vastutavad reisi erinevate aspektide eest.

## Mitmeagendi disainimustri rakendamise põhielemendid

Enne kui saad mitmeagendi disainimustrit rakendada, pead mõistma selle mustri põhielemente.

Teeme selle konkreetsemaks, vaadates taas näidet reisi broneerimisest kasutaja jaoks. Selles stsenaariumis kuuluvad põhielemendid järgmised:

- **Agentide kommunikatsioon**: Lennuotsimisagent, hotelli- ja autorendibroneeringute agent peavad suhtlema ja jagama teavet kasutaja eelistuste ja piirangute kohta. Pead otsustama selle kommunikatsiooni protokollide ja meetodite üle. Konkreetsemalt tähendab see, et lennuotsimisagent peab suhtlema hotelli broneerimise agendiga, et veenduda, et hotell on broneeritud sama kuupäeva jaoks kui lend. See tähendab, et agendid peavad jagama teavet kasutaja reisi kuupäevade kohta, ehk pead otsustama *millised agendid infot jagavad ja kuidas*.
- **Koordineerimise mehhanismid**: Agendid peavad koordineerima oma tegevusi, et tagada kasutaja eelistuste ja piirangute täitmine. Näiteks võib kasutajal olla eelistus hotellile, mis asub lennujaama lähedal, samas kui piirang võib olla, et autorent on saadaval ainult lennujaamas. See tähendab, et hotelli broneerimise agent peab koordineerima tegevusi autorent agentiga, et tagada kasutaja eelistuste ja piirangute täitmine. Seega pead otsustama *kuidas agendid oma tegevusi koordineerivad*.
- **Agentide arhitektuur**: Agendil peab olema sisemine struktuur otsuste tegemiseks ja õppimiseks kasutajaga suhtlemisest. Näiteks lennuotsimisagent peaks suutma otsustada, milliseid lende kasutajale soovitada. See tähendab, et pead otsustama *kuidas agendid otsuseid teevad ja kasutajakogemustest õpivad*. Näiteks võib lennuotsimisagent kasutada masinõppemudelit, et soovitada lende vastavalt kasutaja varasematele eelistustele.
- **Ülevaade mitmeagendi interaktsioonidest**: Pead omama ülevaadet, kuidas eri agendid omavahel suhtlevad. See tähendab, et vajatakse tööriistu ja tehnikaid agentide tegevuse ja suhtluse jälgimiseks. See võib olla logimis- ja monitooringutööriistad, visualiseerimistööriistad ja jõudlusmõõdikud.
- **Mitmeagendi mustrid**: Mitmeagendisüsteeme saab rakendada erinevate mustritega, näiteks keskne, hajutatud ja hübriid arhitektuur. Pead valima mustri, mis sobib kõige paremini sinu kasutusjuhtumiga.
- **Inimene tsüklis**: Enamikul juhtudel on süsteemis inimene tsüklis ning pead õpetama agentidele, millal inimsekkumist küsida. See võib olla vormis, kus kasutaja palub konkreetset hotelli või lendu, mida agendid ei soovitanud, või küsib kinnitust enne lennu või hotelli broneerimist.

## Ülevaade mitmeagendi interaktsioonidest

Oluline on, et sul oleks ülevaade sellest, kuidas mitmed agendid omavahel suhtlevad. See ülevaade on hädavajalik silumiseks, optimeerimiseks ja süsteemi üldise tõhususe tagamiseks. Selle saavutamiseks vajad tööriistu ja tehnikaid agentide tegevuse ja suhtluse jälgimiseks. Need võivad olla logimis- ja monitooringutööriistad, visualiseerimisvahendid ja jõudlusmõõdikud.

Näiteks reisi broneerimisel kasutaja jaoks võiks olla armatuurlaud, mis kuvab iga agendi staatust, kasutaja eelistusi ja piiranguid ning agentide vahelist suhtlust. See armatuurlaud võiks näidata kasutaja reisi kuupäevi, lendude soovitusi lennuagentidelt, hotellisoovitusi hotelliagentidelt ja autorendisoovitusi autorent agentidelt. See annaks selge pildi, kuidas agendid omavahel suhtlevad ja kas kasutaja eelistused ja piirangud täidetakse.

Vaatame iga neist aspektidest lähemalt.

- **Logimis- ja monitooringutööriistad**: Tahad salvestada logisid iga agendi tegevuse kohta. Logikirje sisaldab infot agendi kohta, kes tegevuse tegi, tegevuse aja ja tulemuse kohta. Seda teavet saab kasutada silumiseks, optimeerimiseks ja muuks.

- **Visualiseerimistööriistad**: Need aitavad näha agentidevahelisi suhtlusi visuaalselt arusaadaval viisil. Näiteks graaf, mis kuvab infovoogu agentide vahel. See võib aidata tuvastada kitsaskohti, ebatõhususi ja muid probleeme süsteemis.

- **Jõudlusmõõdikud**: Need aitavad jälgida mitmeagendisüsteemi tõhusust. Näiteks ülesande täitmise aega, täidetud ülesannete hulka ajaühikus ja agentide soovituste täpsust. See info aitab leida parandamisvõimalusi ja süsteemi optimeerida.

## Mitmeagentide mustrid

Sukeldume mõnda konkreetset mustrisse, mida saab kasutada mitmeagentsete rakenduste loomiseks. Siin on mõned huvitavad mustrid, mida tasub kaaluda:

### Grupivestlus

See muster on kasulik, kui soovid luua grupivestluse rakenduse, kus mitmed agendid saavad omavahel suhelda. Tavapärased kasutusjuhud hõlmavad meeskonnatööd, kliendituge ja sotsiaalvõrgustikke.

Selles mustris esindab iga agent grupivestluse kasutajat ning sõnumeid vahetatakse agendi ja sõnumiprotokolli abil. Agendid saavad saata sõnumeid grupivestlusesse, vastu võtta sõnumeid ja vastata teiste agentide sõnumitele.

See muster võib olla rakendatud kas tsentraliseeritud arhitektuuris, kus kõik sõnumid lähevad läbi keskserveri, või detsentraliseeritud arhitektuuris, kus sõnumeid vahetatakse otse.

![Grupivestlus](../../../translated_images/et/multi-agent-group-chat.ec10f4cde556babd.webp)

### Ülesannete üleandmine

See muster on kasulik, kui soovid luua rakenduse, kus erinevad agendid saavad ülesandeid omavahel üle anda.

Tüüpilised kasutusjuhud hõlmavad kliendituge, ülesannete haldust ja töövoo automatiseerimist.

Selles mustris esindab iga agent ülesannet või töövoo sammu ning agendid saavad maagide alusel ülesandeid teistele agentidele üle anda.

![Ülesannete üleandmine](../../../translated_images/et/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Koostööfiltreerimine

See muster on kasulik, kui soovid luua rakenduse, kus erinevad agendid teevad koostööd, et kasutajatele soovitusi teha.

Miks tahta, et mitmed agendid teeksid koostööd? Sest iga agent võib olla erinevas asjatundlikkusvaldkonnas ja panustada soovitusprotsessi erineval moel.

Võtame näiteks olukorra, kus kasutaja tahab soovitust, millist aktsiat börsil osta.

- **Tööstusharu ekspert**: Üks agent võib olla konkreetse tööstusharu ekspert.
- **Tehniline analüüs**: Teine agent võib olla tehnilise analüüsi ekspert.
- **Fundamentaalne analüüs**: Kolmas agent võib olla fundamentaalse analüüsi ekspert. Koostöös saavad need agendid pakkuda kasutajale põhjalikumat soovitust.

![Soovitused](../../../translated_images/et/multi-agent-filtering.d959cb129dc9f608.webp)

## Stsenaarium: Tagasimakse protsess

Mõtle olukorda, kus klient üritab saada tagasimakset toote eest, sellesse protsessi võib olla kaasatud üsna palju agente, kuid jagame need konkreetseteks protsessi agentideks ning üldisteks agentideks, mida saab kasutada ka teistes protsessides.

**Tagasimakse protsessile spetsiaalsed agendid**:

Järgnevad on mõned agendid, kes võivad tagasimakse protsessis osaleda:

- **Kliendi agent**: Esindab klienti ja käivitab tagasimakse protsessi.
- **Müüja agent**: Esindab müüjat ja haldab tagasimaksete töötlemist.
- **Makse agent**: Esindab makseprotsessi ja vastutab kliendi makse tagastamise eest.
- **Lahendamise agent**: Haldab probleemide lahendamist tagasimakse protsessi käigus.
- **Järgimise agent**: Tagab, et tagasimakse protsess vastab regulatsioonidele ja poliitikatele.

**Üldised agendid**:

Neid agente saab kasutada ka mujal sinu äriprotsessides.

- **Saatmise agent**: Haldab toote tagasisaatmiste protsessi ja saadab toote müüjale. Seda agenti saab kasutada nii tagasimaksete korral kui ka muu kaupade saatmise puhul, näiteks ostmisel.
- **Tagasiside agent**: Kogub klientide tagasisidet. Tagasisidet võib küsida igal ajal, mitte ainult tagasimakse protsessi ajal.
- **Eskalatsiooni agent**: Vastutab probleemide eskaleerimise eest kõrgemale tasemele klienditoes. Seda tüüpi agenti saab kasutada igas protsessis, kus on vaja eskaleerida küsimusi.
- **Teavituse agent**: Saadab klientidele teavitusi tagasimakse erinevates etappides.
- **Analüüsiaagent**: Analüüsib tagasimakse protsessiga seotud andmeid.
- **Audit agent**: Kontrollib tagasimakse protsessi õigsust ja korrektsust.
- **Aruandlus agent**: Koostab aruandeid tagasimakse protsessi kohta.
- **Teadmiste agent**: Halda teadmistebaasi tagasimaksete protsessist. See agent võib olla teadlik nii tagasimaksetest kui ka muudest sinu äriprotsessi osadest.
- **Turvalisuse agent**: Tagab tagasimakse protsessi turvalisuse.
- **Kvaliteedi agent**: Tagab tagasimakse protsessi kvaliteedi.

Eelnevalt on nimetud päris palju agente nii spetsiifiliselt tagasimakse protsessi jaoks kui ka üldiseid agente, mida saab kasutada muudes äriprotsessides. Loodetavasti annab see sulle ülevaate, kuidas otsustada, milliseid agente oma mitmeagendi süsteemis kasutada.

## Ülesanne

Kavanda mitmeagendi süsteem klienditoe protsessi jaoks. Tuvasta protsessis osalevad agendid, nende rollid ja vastutusalad ning kuidas nad omavahel suhtlevad. Kaasa nii klienditoe protsessile spetsiifilised agendid kui ka üldised agendid, keda saab kasutada ka teistes ärivaldkondades.


> Mõtle enne järgmise lahenduse lugemist järele, sul võib vaja minna rohkem agente, kui arvad.

> NÕUANNE: Mõtle klienditoe protsessi erinevatele etappidele ning ka selle peale, milliseid agente on vaja süsteemi jaoks.

## Lahendus

[Lahendus](./solution/solution.md)

## Teadmiste kontroll

### Küsimus 1

Milline stsenaarium sobib kõige paremini mitmeagendi süsteemile?

- [ ] A1: Tugibot vastab korduvatele küsimustele, kasutades ühte teadmistebaasi ja väikest tööriistakomplekti.
- [ ] A2: Tagasimakse töövoog vajab eraldi pettuse, maksete ja nõuetele vastavuse rolle, igaühel oma tööriistad, ja nende tulemused tuleb koordineerida.
- [ ] A3: Sama lihtsat klassifikatsioonipäringut tuleb tunnis tuhandeid kordi.

### Küsimus 2

Millal on tavaliselt parem valida üks agent?

- [ ] A1: Ülesannet saab lahendada ühe juhiste ja tööriistakomplektiga, ilma spetsiaalsete üleandmisteta.
- [ ] A2: Agendil on ligipääs rohkem kui ühele tööriistale.
- [ ] A3: Töövoog nõuab eraldi rolle, millel on erinevad õigused ja iseseisvad auditeerimisteed.

[Lahenduse viktoriin](./solution/solution-quiz.md)

## Kokkuvõte

Selles õppetükis vaatasime mitmeagendilise disainimusteri, sealhulgas olukordi, kus mitmeagendilised süsteemid sobivad, mitmeagendiliste süsteemide eeliseid võrreldes ühe agendiga, mitmeagendilise disainimustri rakendamise põhielemente ja seda, kuidas saada ülevaadet mitme agendi omavahelisest koostööst.

### Kas sul on mitmeagendilise disainimustri kohta rohkem küsimusi?

Liitu [Microsoft Foundry Discord'iga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada vastused oma AI agentide küsimustele.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Frameworki dokumentatsioon</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentliku disainimustri mustrid</a>


## Eelmine õppetükk

[Planeerimise disain](../07-planning-design/README.md)

## Järgmine õppetükk

[Metakognitsioon AI agentides](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->