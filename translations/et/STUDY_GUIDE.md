# AI Agendid Algajatele - Õpi juhend

Kasuta seda juhendit praktilise kaaslasena kursuse läbimisel. See ei ole
mõeldud tundide asendamiseks. See aitab sul otsustada, kust alustada, mida
iga tunni juures otsida ja kuidas ideid ühendada väikese töötava agendi
demonstratsiooniks.

Kui see on su esimene kord siin, alusta lihtsast:

1. Loe [Kursuse seadistamine](./00-course-setup/README.md).
2. Täida õppetunnid 01–06 järjekorras.
3. Hoia meeles üht väikest demoideed õppetöö ajal.
4. Pärast iga õppetundi küsi: "Mida saab mu agent nüüd teha, mida ta enne teha ei saanud?"
   

## Lihtne demo, mida meeles pidada

Hea viis agentide õppimiseks on läbida ühe demoidee kogu kursuse vältel.

Näite demo: **kursuse abistaja agent**.

Kasutaja küsib:

> "Ma tahan õppida, kuidas agendid kasutavad tööriistu. Leia õiged õppetunnid, tee kokkuvõte, mida peaksin esmalt lugema, ja anna mulle lühike praktikaülesanne."




2. **Kasuta tööriistu**, et saada õppetundide linke, näiteid või toetavat materjali.
3. **Planeeri** lühike õppeteekond, selle asemel et anda pikk vastus.
4. **Kasuta konteksti** praegusest vestlusest, et keskenduda õppija eesmärgile.
5. **Mäleta kasulikke eelistusi**, kui rakendus toetab mälu.
6. **Näita jälgi, viiteid või logisid**, et kasutaja saaks aru, mis toimus.
7. **Rakenda piiranguid** enne riskantsete tegude tegemist või tundlike andmete kasutamist.

Kui õpid iga õppetunni, tule tagasi selle demoni juurde ja küsi: mida uut see õppetund lisaks?

## Mille poole sa ehitad




|------|------------------------|-------------|
mis kombineerivad need osad:

| Osa | Lihtsustus keeles | Demo puhul |
|------|------------------------|-------------|
| Mudel | Mõtlemismootor, mis tõlgendab kasutaja soovi | Mõistab, et õppija soovib tööriistade kasutamist käsitlevaid tunde |
| Tööriistad | Funktsioonid, API-d, failid, brauserid või teenused, mida agent saab kasutada | Otsib repositoorset või hangib tundide sisu |
| Teadmised | Dokumendid või andmed vastuse alusena | Kursuse README-failid ja tunnimaterjal |
| Kontekst | Teave, mis kaasatakse järgmisse mudelikõnesse | Kasutaja eesmärk ja tööriista tulemused |
| Mälu | Hilisemaks kasutamiseks salvestatud teave | Õppija eelistab praktilisi Python näiteid |
| Planeerimine | Suurema eesmärgi jaotamine väiksemateks sammudeks | Leia tunnid, tee neist kokkuvõte, paku harjutust |
| Orkestreerimine | Töö suunamine tööriistade, sammude või agentide vahel | Planeerija kutsub otsingutööriista ja siis kokkuvõtjat |
| Usaldus | Turvalisus, läbipaistvus, hindamine ja jälgitavus | Logib tööriistakõned ja küsib enne olulisi toiminguid |

## Mudelid ja pakkujad

Kursuse koodinäited kasutavad **Microsoft Agent Frameworki (MAF)** ja sihivad **Azure OpenAI Responses API-d** — eesolevaks soovitatud API-d, mis ühendab vestluste täiendused, tööriistakutsed, multimodaalse sisendi ja staatilised vestlused ühe API-pinnal. Ühendute kas **Microsoft Foundry** projektiga (kasutades `FoundryChatClient`) või Azure OpenAI-ga otse (kasutades `OpenAIChatClient`).

Tundide läbimisel on teil mõned pakkuja valikud:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — peamine tee, mida tundides kasutatakse. Logi sisse ilma võtmeta Entra ID autentimiseks `az login` abil.
- **Foundry Local** — käivita mudeleid täielikult seadmes OpenAI-ühilduva API kaudu (ilma pilveta, ilma API võtmeteta). Ideaalne offline- või tasuta katsetusteks. Vaata [Kursuse seadistust](./00-course-setup/README.md).
- **MiniMax** — OpenAI-ühilduv pakkuja suure kontekstiga mudelitega, kasutatav otseasendajana.

> **Märkus:** GitHub Models on vananenud (väljajäämine juulis 2026) ja ei toeta Responses API-d. Näiteid on uuendatud kasutama Azure OpenAI / Microsoft Foundry-d.

## Valige oma õppeteekond

Võite võtta kogu kursuse järjest või hüpata tee peale vastavalt sellele, mida soovite
ehitada.

| Kui teie eesmärk on... | Alustage | Siis õppige |
|-----------------------|------------|------------|
| Mõista, mis on agendid | 01, 02, 03 | 04, 05, 06 |
| Ehita agent, kes kasutab tööriistu | 04 | 05, 07, 14 |
| Ehita RAG-põhine agent | 05 | 04, 06, 12 |
| Kujunda mitmeastmelisi töövooge | 07 | 08, 09, 14 |
| Mõista mitmeagendilisi süsteeme | 08 | 07, 09, 11 |
| Valmista agendid tootmiseks ette | 06, 10 | 12, 13, 16, 18 |
| Külasta ja skaleeri agente Foundryl | 10, 16 | 06, 13, 18 |
| Ehita lokaalseid / offline-esimesi agente | 17 | 04, 05, 11 |
| Uuri protokolle ja brauseri automatiseerimist | 11, 15 | 10, 18 |

Nipp: kui oled agentide vallas uus, ära jäta vahele õppetunde 01-06. Need annavad sulle
selleks vajalikud mõisted kogu ülejäänud kursuse jaoks.

## Õppetundide juhend

| Õppetund | Mida õpid | Proovi peale õppetundi |
|--------|----------------|---------------------------|
| [01 - Sissejuhatus AI agentidesse](./01-intro-to-ai-agents/README.md) | Mis teeb agendi tavalisest juturobotist erinevaks. | Selgita oma demo ideed kui agenti, mitte ainult vestlusrakendust. |
| [02 - Agentide raamistikud](./02-explore-agentic-frameworks/README.md) | Kuidas raamistikud aitavad mudelite, tööriistade, oleku ja töövoogudega. | Määra, milliseid demo osi raamistik haldaks. |
| [03 - Agentide disainimustrid](./03-agentic-design-patterns/README.md) | Levinud mustrid agentide käitumise disainiks. | Joonista kasutajateekond enne koodi kirjutamist. |
| [04 - Tööriistade kasutamine](./04-tool-use/README.md) | Kuidas agendid kutsuvad tööriistu info saamiseks või tegevuse võtmeks. | Määra üks tööriist, mida sinu demo agent vajaks. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Kuidas päring tagab agentide vastused dokumentide või andmete põhjal. | Otsusta, millist teadmusallikat sinu demo peaks otsima. |
| [06 - Usaldusväärsed agendid](./06-building-trustworthy-agents/README.md) | Kuidas lisada turvapiirded, järelevalve ja ohutum käitumine. | Lisa reegel, millal agent peaks kasutajalt esmalt küsima. |
| [07 - Plaanimise disain](./07-planning-design/README.md) | Kuidas agendid jagavad suuremad eesmärgid väiksemateks sammudeks. | Kirjuta kolmeastmeline plaan oma demo päringule. |
| [08 - Mitmeagendiline disain](./08-multi-agent/README.md) | Millal töö jaotada spetsialiseeritud agentide vahel. | Otsusta, kas demo vajab ühte või mitut agenti. |
| [09 - Metakognitsioon](./09-metacognition/README.md) | Kuidas agendid saavad oma väljundit analüüsida ja parandada. | Lisa lõplik enesekontroll enne agenti vastust. |
| [10 - AI agendid tootmises](./10-ai-agents-production/README.md) | Mis muutub, kui agent läheb demost tootmisse. | Kirjuta üles, mida sa jälgiksid: kvaliteet, hind, latentsus, vead. |
| [11 - Agentide protokollid](./11-agentic-protocols/README.md) | Kuidas protokollid ühendavad agente tööriistade ja teiste agentidega. | Määra koht, kus standardprotokoll võiks lihtsustada integratsiooni. |
| [12 - Konteksti inseneritöö](./12-context-engineering/README.md) | Kuidas valida, kärpida, isoleerida ja hallata konteksti. | Otsusta, mis kuulub PROMPT-ile ja mis peaks välja jääma. |
| [13 - Agendi mälu](./13-agent-memory/README.md) | Kuidas agendid saavad säilitada kasulikku infot suhtluste vahel. | Vali üks ohutu eelistus, mida demo võiks meelde jätta. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Raamistiku spetsiifilised moodulid agentidele ja töövoogudele, koos LangChain/LangGraph agentide majutamisega Microsoft Foundryl. | Kaarda oma demo sammud raamistiku mõistetega. |
| [15 - Arvuti kasutamise agendid](./15-browser-use/README.md) | Kuidas agendid saavad suhelda brauseri või kasutajaliidesega, sh tõelised näited nagu Microsoft Project Opal. | Vali üks brauseri ülesanne, mis nõuab endiselt kasutaja kinnitust. |
| [16 - Skaleeritavate agentide juurutamine](./16-deploying-scalable-agents/README.md) | Kuidas viia agent prototüübist skaleeritava ja jälgitava tootmisjuurutuseni Microsoft Foundryl (majutatud agendid, mudelite marsruutimine, vahemälu, hindamise väravad, suitsutestid). | Pane kirja tootmismured, mida su demo veel vajab: majutus, marsruutimine, kulud, hindamine. |
| [17 - Kohalike AI agentide loomine](./17-creating-local-ai-agents/README.md) | Kuidas ehitada lokaalseid esimesi agente, kes töötavad täielikult sinu masinas Foundry Local ja Qweniga (kohalikud tööriistad, kohalik RAG, kohalik MCP). | Otsusta, millised demo osad peaksid jääma privaatselt kohalikuks. |
| [18 - AI agentide turvamine](./18-securing-ai-agents/README.md) | Kuidas muuta agendi toimingud paremini auditeeritavaks ja muutustõenduseks. | Otsusta, milliseid toiminguid su demo peaks logima või vastu võtma. |

## Juurutatud agentide valideerimine suitsutestidega

Kui sa juurutad agendi (Ōppetund 16), on **suitsutest** odavaim esimene
kontroll, kas juurutus tegelikult reageerib. See repoo sisaldab käivitamiseks valmis
katalooge kaustas [tests/](./tests/README.md) juurutatavate agentide jaoks õppetundides
01, 04, 05 ja 16, ühendatuna
[AI suitsutestiga](https://github.com/marketplace/actions/ai-smoke-test) GitHubi
tegevusega. Käivita need **Tegevuste** vahekaardilt peale õppetunni agendi juurutamist.
Suitsutestid on esimene värav — offline- ja online-hindamine (Õppetunnid 10 ja 16)
ütlevad sulle, kui *hea* agent on.

## Põhimõisted algajale arusaadavalt

### Tööriistad

Tööriist on midagi, mida agent saab kutsuda töö tegemiseks väljaspool mudelit. Heal tööriistal
on selge nimi, kitsas ülesanne, tüpiseeritud sisendid, prognoositav väljund ja ohutu viis
ebaõnnestumiseks.

Kursuse abistava demo jaoks võiks tööriist olla:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG ja Teadmus

RAG aitab agendil vastata lähteallikast, mitte oletada. Selles
kursuses võivad selleks allikaks olla õppetundide README-d, koodinäited või välised
ressursid, mis on õppetundidega lingitud.

Kasuta RAG-i, kui vastus peaks olema dokumentide, andmete või hetkeliste
projekti failide põhjal.

### Planeerimine

Planeerimine on kasulik, kui päringul on rohkem kui üks samm. Hoia plaanid lühikesed ja
nähtavad nii, et arendaja või kasutaja saaks neid vaadata.

Demo puhul võiks plaan olla:

1. Leia õppetunnid, mis on seotud tööriistade kasutamisega.
2. Võta kokku kõige olulisemad õppetunnid.
3. Soovita üks harjutusülesanne.

### Kontext

Kontext on see, mida mudel praegu näeb. Liiga vähe konteksti võib panna
agendi olulisi detaile ignoreerima. Liiga palju konteksti võib muuta agendi aeglasemaks, kallimaks
või kergemini eksitavaks.

Hea konteksti inseneritöö tähendab õigete andmete valikut järgmise mudelikõne jaoks.




ainult siis, kui see on kasulik, ohutu ja kerge uuendada või kustutada.


Isikuandmeid ei tohiks tavaliselt salvestada.


### Hindamine ja jälgitavus

Hindamine vastab küsimusele: kas agent tegi õiget asja?

Jälgitavus vastab küsimusele: kas me näeme, kuidas see juhtus?

Tootmisagentide puhul jälgi mudelikõnesid, tööriistade kutsumisi, hangitud konteksti,
latentsust, kulusid, rikkeid ja kasutajate tagasisidet.

### Usaldus ja turvalisus

Usaldusväärsed agendid vajavad rohkem kui kasulikku prompti. Kasuta vähima privileegiga tööriistu,
inimese kinnitust tõsiste tegevuste jaoks, vajadusel andmete punaseerimist ning logisid või
kviitungeid tegevustele, mida tuleb auditeerida.

## 15-minutiline ülevaaterutiin

Kasuta seda rutiini peale iga õppetundi:

1. **Võta õppetund kokku ühe lausega.**
2. **Nimeta uus agendi võimekus.** Näiteks: tööriistade kasutamine, päring,
   planeerimine, mälu, jälgitavus või turve.
3. **Lisa see kursuse abi demosse.** Mis muutub demos nüüd?
4. **Leia risk.** Mis võiks valesti minna, kui seda võimekust kasutatakse valesti?
5. **Kirjuta üks testküsimus.** Kuidas sa kontrolliksid, et agent käitub hästi?

## Kiire enesekontroll

Enne edasi liikumist proovi vastata järgmistele küsimustele:

1. Mida saab agent teha, mida tavaline juturobot iseseisvalt teha ei suuda?
2. Millist tööriista su agent esmalt vajab ja miks?
3. Milline teadmusallikas peaks agendi vastuse aluseks olema?
4. Mis kontekst peaks kaasnema järgmise mudelikõnega?
5. Mida peaks agent meeles pidama ja mida peaks vältima salvestamast?
6. Millal peaks agent küsima inimese kinnitust?
7. Millised logid, jäljed või kviitungid aitaksid sul agenti hiljem siluda või auditeerida?

## Soovitatud lõputööülesanne

Kursuse lõpus loo väike agent, mis aitab õppijal selles
hoidlas navigeerida.

Vähemalt versioon:

- Võta kasutajalt teema.
- Leia kõige asjakohasemad õppetunnid.
- Võta kokku, mida lugeda kõigepealt.
- Soovita üht praktilist ülesannet.
- Näita, milliseid õppetundi faile või linke kasutati.

Lisavõimaluste versioon:

- Mäleta õppija eelistatud programmeerimiskeelt.
- Kasuta enne vastamist lihtsat plaani.
- Lisa enne lõplikku vastust enesekontrolli samm.
- Logi tööriistakõned ja leitud allikad.
- Küsi kinnitust enne brauseri või kasutajaliidese automatiseerimise ülesannete avamist.

See annab sulle väikese, kuid realistliku võimaluse harjutada tööriistu, RAGi, planeerimist,
konteksti, mälu, jälgitavust ja usaldust ühes projektis.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->