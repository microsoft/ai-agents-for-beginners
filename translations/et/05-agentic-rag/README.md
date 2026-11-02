[![Agentic RAG](../../../translated_images/et/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Agentic RAG

See õppetund annab põhjaliku ülevaate Agentic Retrieval-Augmented Generationist (Agentic RAG), uusst AI paradigmas, kus suured keelemudelid (LLMid) planeerivad autonoomselt oma järgmisi samme, samal ajal otsides infot väliste allikate hulgast. Erinevalt staatilistest meetoditest, kus esmalt otsitakse ja siis loetakse, kaasab Agentic RAG iteratiivseid LLMi väljakutseid, vaheldudes tööriistade või funktsioonide kutsumisega ning struktureeritud väljunditega. Süsteem hindab tulemusi, täpsustab päringuid, kutsub vajadusel lisatööriistu ja jätkab seda tsüklit, kuni saavutatakse rahuldav lahendus.

## Sissejuhatus

See õppetund käsitleb

- **Agentic RAG mõistmine:** Õppige tundma AI uusim paradigma, kus suured keelemudelid (LLMid) planeerivad autonoomselt järgmised sammud ja otsivad infot välisest andmeallikast.
- **Iteratiivse Maker-Checker stiili haaramine:** Mõistke iteratiivsete LLMi väljakutsete tsüklit, kus vahelduvad tööriistade või funktsioonide kutsed ja struktureeritud väljundid, eesmärgiga parandada täpsust ja käsitleda vigaseid päringuid.
- **Praktiliste kasutusjuhtude uurimine:** Tuvastage olukorrad, kus Agentic RAG paistab silma, näiteks täpsuspõhistes keskkondades, keerukate andmebaasidega tegelemisel ja pikendatud töövoogudes.

## Õpieesmärgid

Pärast selle õppetunni läbimist te:

- **Agentic RAG mõistmine:** Saate teada, kuidas suured keelemudelid (LLMid) autonoomselt planeerivad järgmisi samme, otsides infot välisest allikast.
- **Iteratiivse Maker-Checker stiili mõistmine:** Mõistke LLMi korduvate väljakutsete tsüklit vaheldumisi tööriistade või funktsioonide kutsumise ja struktureeritud väljunditega.
- **Arutluse protsessi omamine:** Saate aru süsteemi võimest omada oma arutluse protsessi, tehes otsuseid probleemide lahendamise kohta ilma eelmääratletud radadeta.
- **Töövoog:** Mõistate, kuidas agenti mudel iseseisvalt otsustab hankida turusuundumuste aruandeid, tuvastada konkurentide andmeid, korreleerida sisemisi müüginäitajaid, sünteesida leide ja hinnata strateegiat.
- **Iteratiivsed tsüklid, tööriistade integratsioon ja mälu:** Õpite süsteemi sõltuvusest korduvast interaktsioonimustrist, mis hoiab olekut ja mälu sammude jooksul, vältides korduvaid tsükleid ja tehes informeeritud otsuseid.
- **Vigade käsitsemine ja enesekorrektsioon:** Avastate süsteemi tugeva enesekorrektsiooni mehhanismi, sealhulgas kordusi ja uuesti päringuid, diagnostikavahendite kasutamist ning inimjärelevalve tagasilangemist.
- **Agentuuri piirid:** Mõistate Agentic RAG piiranguid, keskendudes domeenipõhisele autonoomiale, infrastruktuuri sõltuvusele ja piirangute austamisele.
- **Praktilised kasutusjuhtumid ja väärtus:** Tuvastate olukorrad, kus Agentic RAG paistab silma, näiteks täpsuspõhistes keskkondades, keerukate andmebaasidega suhtlemisel ja pikendatud töövoogudes.
- **Juhtimine, läbipaistvus ja usaldus:** Õpite juhtimise ja läbipaistvuse olulisust, sealhulgas selgitavat arutlust, kallutuste kontrolli ja inimjärelevalvet.

## Mis on Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) on uus AI paradigma, kus suured keelemudelid (LLMid) planeerivad autonoomselt oma järgmisi samme, otsides infot välisallikatest. Erinevalt staatilisest otsi- ja loe mustrist hõlmab Agentic RAG LLMi iteratiivseid väljakutseid, mille vahele jäävad tööriista või funktsiooni kutsed ja struktureeritud väljundid. Süsteem hindab tulemusi, täpsustab päringuid, kutsub vajadusel lisatööriistu ja jätkab tsüklit, kuni leitakse rahuldav lahendus. See iteratiivne "maker-checker" stiil parandab täpsust, käsitleb vigased päringud ja tagab kvaliteetsed tulemused.

Süsteem juhib aktiivselt oma arutlusprotsessi, kirjutades ebaõnnestunud päringuid ümber, valides erinevaid otsimismeetodeid ja integreerides mitmeid tööriistu — nagu vektorotsing Azure AI Searchis, SQL andmebaasid või kohandatud API-d — enne vastuse lõpetamist. Agentse süsteemi määravaks tunnuseks on võime omada oma arutlusprotsessi. Traditsioonilised RAG lahendused tuginevad eelmääratletud radadele, aga agentne süsteem määrab sammude järjekorra info kvaliteedi põhjal iseseisvalt.

## Agentic Retrieval-Augmented Generationi (Agentic RAG) määratlus

Agentic Retrieval-Augmented Generation (Agentic RAG) on AI arendusparadigma, kus LLMid mitte ainult ei otsi infot välisest andmebaasist, vaid planeerivad autonoomselt järgmised sammud. Erinevalt staatilistest otsi- ja loe mustritest või hoolikalt kirjutatud päringute järjestusest, hõlmab Agentic RAG LLMi iteratiivseid väljakutseid, mille vahele jäävad tööriistade või funktsioonide kutsed ja struktureeritud väljundid. Süsteem hindab iga kord saadud tulemusi, otsustab päringuid täpsustada, kutsub vajadusel lisa tööriistu ja jätkab seda tsüklit, kuni leitakse rahuldav lahendus.

See iteratiivne "maker-checker" tööstiil on loodud täpsuse parandamiseks, vigaste päringute käsitlemiseks struktureeritud andmebaasidele (näiteks NL2SQL) ja kõrgkvaliteetsete tasakaalustatud tulemuste tagamiseks. Selle asemel, et ainult tugineda hoolikalt üldseadistatud päringa keti skriptile, juhib süsteem aktiivselt oma arutluse protsessi. See võib ümber kirjutada ebaõnnestunud päringuid, valida erinevaid otsimismeetodeid ja kombineerida mitmeid tööriistu — nagu vektorotsing Azure AI Searchis, SQL andmebaasid või kohandatud API-d — enne lõpliku vastuse koostamist. See kõrvaldab vajaduse keerukate orkestreerimismustrite järele. Selle asemel võib suhteliselt lihtne tsükkel "LLMi kõne → tööriista kasutus → LLMi kõne → ..." anda keerukaid ja hästi põhjendatud väljundeid.

![Agentic RAG Core Loop](../../../translated_images/et/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Arutlusprotsessi omamine

Agentse süsteemi määrav omadus on võime omada oma arutlusprotsessi. Traditsioonilised RAG rakendused sõltuvad sageli inimeste poolt eelmääratletud stsenaariumist: mõttekett, mis määrab, mida ja millal tuleb otsida.
Kuid kui süsteem on tõeliselt agentne, otsustab ta sisemiselt, kuidas probleemi lahendada. See ei täida lihtsalt skripti, vaid määrab autonoomselt sammude järjekorra põhinedes leitud info kvaliteedil.
Näiteks kui palutakse luua tooteturu lansseerimise strateegia, ei tugine ta ainult päringule, mis määratleb kogu uurimis- ja otsustusprotsessi. Selle asemel otsustab agentne mudel iseseisvalt:

1. Hankida praegused turutrendide raportid Bing Web Groundingu abil
2. Tuvastada asjakohased konkurentide andmed Azure AI Searchiga.
3. Korrelleerida ajaloolised sisemised müüginäitajad Azure SQL andmebaasis.
4. Sünteesida leiud ühtseks strateegiaks, koordineerituna Azure OpenAI teenuse kaudu.
5. Hinnata strateegiat puuduste või ebakõlade suhtes, vajadusel käivitades uue uurimisvooru.
Kõik need sammud — päringute täpsustamine, allikate valik, vastuse rahuldavuseni iteratsioon — otsustab mudel, mitte inimene eelnevalt skriptitud viisil.

## Iteratiivsed tsüklid, tööriistade integreerimine ja mälu

![Tool Integration Architecture](../../../translated_images/et/tool-integration.0f569710b5c17c10.webp)

Agentne süsteem tugineb iteratiivsele interaktsioonimustrile:

- **Algne väljakutse:** Kasutaja eesmärk (ehk kasutajapäring) antakse LLMile.
- **Tööriista kutsumine:** Kui mudel tuvastab info puudumise või ebamäärased juhised, valib ta tööriista või otsingumeetodi — näiteks vektorandmebaasi päringu (nt Azure AI Search hübriidotsing privaatandmetel) või struktureeritud SQL-kutse — lisakonteksti kogumiseks.
- **Hindamine ja täpsustamine:** Tagastatud andmeid üle vaadates otsustab mudel, kas info on piisav. Kui ei ole, parendab päringut, proovib teist tööriista või kohandab lähenemist.
- **Korda kuni rahuloluni:** Tsükkel jätkub, kuni mudel leiab, et tal on piisav selgus ja tõendus, et anda lõplik ja hästi põhjendatud vastus.
- **Mälu ja olek:** Süsteem hoiab sammude vahel olekut ja mälu, meenutades varasemaid katseid ja nende tulemusi, vältides korduvaid tsükleid ja tehes paremaid otsuseid protsessi käigus.

Aja jooksul loob see areneva mõistmise tunde, võimaldades mudelil navigeerida keerukates, mitmeastmelistes ülesannetes ilma inimese pideva sekkumiseta või päringu ümberkujundamiseta.

## Vigade käsitlemine ja enesekorrektsioon

Agentic RAG autonoomia hõlmab ka tugevaid enesekorrektsiooni mehhanisme. Kui süsteem satub ummikusse — näiteks tagastab ebaolulisi dokumente või puutub kokku vigaste päringutega — siis võib see:

- **Itereerida ja uuesti pärida:** Selle asemel, et tagasi anda madala väärtusega vastuseid, proovib mudel uusi otsingustrateegiaid, kirjutab andmebaasipäringud ümber või vaatab alternatiivseid andmekogumeid.
- **Kasutada diagnostikavahendeid:** Süsteem võib kutsuda lisafunktsioone, mis aitavad siluda arutluse samme või kinnitada tagastatud andmete õigsust. Sellised tööriistad nagu Azure AI Tracing on olulised robustse jälgitavuse ja monitooringu võimaldamiseks.
- **Kallutuda inimjärelevalve poole:** Kõrge riskiga või korduvalt ebaõnnestuvate stsenaariumide puhul võib mudel märgistada ebakindluse ja paluda inimjuhendust. Kui inimene annab korrektsioonipala, suudab mudel seda edaspidi arvestada.

See iteratiivne ja dünaamiline lähenemine võimaldab mudelil pidevalt areneda, tagades, et see pole mitte ühe korraga töötav süsteem, vaid õpib vigadest antud sessiooni jooksul.

![Self Correction Mechanism](../../../translated_images/et/self-correction.da87f3783b7f174b.webp)

## Agentuuri piirid

Hoolimata autonoomiast ülesande täitmisel pole Agentic RAG samaväärne tehisüldintellektiga. Selle agentuuri võimed piirduvad tööriistade, andmeallikate ja inimestest arendajate poolt seatud poliitikatega. See ei suuda leiutada enda tööriistu ega astuda välja mõistatuspiiridest, mis on seatud. Selle asemel paistab see silma ressursse dünaamiliselt koordineerides.
Peamised erinevused võrreldes keerukamate AI vormidega on:

1. **Domeenipõhine autonoomia:** Agentic RAG süsteemid keskenduvad kasutaja määratletud eesmärkide täitmisele teadaolevas domeenis, kasutades selliseid strateegiaid nagu päringute ümberkirjutamine või tööriista valik tulemuste parandamiseks.
2. **Infrastruktuuri sõltuvus:** Süsteemi võimed sõltuvad arendajate integreeritud tööriistadest ja andmetest. Ilma inimsekkumiseta ei saa ta neid piire ületada.
3. **Piirangute austamine:** Eetilised juhised, vastavusreeglid ja äri poliitikad on jätkuvalt väga olulised. Agendi vabadus on alati piiratud ohutusmeetmete ja järelevalve mehhanismidega (loodetavasti).

## Praktilised kasutusjuhud ja väärtus

Agentic RAG paistab silma olukordades, mis nõuavad iteratiivset täpsustamist ja täpsust:

1. **Täpsuse prioriteediga keskkonnad:** Vastavuse kontrollides, regulatiivsel analüüsil või õigusuuringutes saab agentne mudel korduvalt kontrollida fakte, konsulteerida mitmete allikatega ja ümber kirjutada päringuid kuni täielikult kontrollitud vastuse saamiseni.
2. **Keerukad andmebaasidega suhtlused:** Kui tegeletakse struktureeritud andmetega päringutega, mis võivad tihti ebaõnnestuda või vajada täpsustamist, saab süsteem iseseisvalt täiustada päringuid kasutades Azure SQL või Microsoft Fabric OneLake, tagades lõpliku päringu vastavuse kasutaja eesmärgile.
3. **Pikendatud töövood:** Pikkema kestusega sessioonid võivad areneda uue info ilmnemisel. Agentic RAG saab pidevalt uusi andmeid integreerida, muutes strateegiaid vastavalt probleemivaldkonna tundmisele.

## Juhtimine, läbipaistvus ja usaldus

Kuna need süsteemid muutuvad oma arutluses autonoomsemaks, on juhtimine ja läbipaistvus olulised:

- **Selgitav arutlus:** Mudel suudab anda auditeeritava jälje oma päringutest, allikatest ja arutlusetappidest, mis viisid järelduseni. Sellised tööriistad nagu Azure AI Content Safety ja Azure AI Tracing / GenAIOps aitavad säilitada läbipaistvust ja maandada riske.
- **Eelarvutuse kontroll ja tasakaalustatud otsing:** Arendajad saavad häälestada otsingustrateegiaid tagamaks tasakaalustatud ja esinduslike andmeallikate arvestamist ning regulaarselt auditeerida väljundeid kallutatuse või ebaõnnestumiste avastamiseks kasutades kohandatud mudeleid edasijõudnutele, näiteks Azure Machine Learningu kaudu.
- **Inimjärelevalve ja vastavus:** Tundlike ülesannete puhul on inimkontroll jätkuvalt hädavajalik. Agentic RAG ei asenda inimotsust kõrgete panustega otsustes vaid täiendab seda põhjalikumalt kontrollitud võimalustega.

On oluline omada tööriistu, mis dokumenteerivad tehtud tegevused selgelt. Ilma selleta võib mitmest sammust koosneva protsessi silumine olla väga keeruline. Järgnevalt on näide Literal AI-st (ettevõte Chainliti taga) agendi töö käigust:

![AgentRunExample](../../../translated_images/et/AgentRunExample.471a94bc40cbdc0c.webp)

## Kokkuvõte

Agentic RAG kujutab endast loomulikku arengut AI süsteemide võimes käsitleda keerukaid ja andmerikkaid ülesandeid. Adopteerides iteratiivse interaktsioonimustri, valides autonoomselt tööriistu ja täiustades päringuid kuni kõrgekvaliteedilise tulemuse saavutamiseni, liigub süsteem kaugemale staatilisest päringute järgimisest kohanemisvõimelise ja kontekstiteadliku otsustajana. Kuigi see on ikkagi piiratud inimestest määratletud infrastruktuuride ja eetiliste juhistega, võimaldavad need agentse võimed rikkalikumaid, dünaamilisemaid ja lõppkokkuvõttes kasulikumaid AI interaktsioone nii ettevõtetele kui lõppkasutajatele.

### Kas teil on Agentic RAG kohta veel küsimusi?

Liituge [Microsoft Foundry Discordi](https://discord.com/invite/ATgtXmAS5D) kanaliga, et kohtuda teiste õppuritega, osaleda konsultatsioonitundides ja saada vastuseid oma AI agentidega seotud küsimustele.

## Täiendavad ressursid

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Rakenda Retrieval Augmented Generation (RAG) Azure OpenAI teenusega: Õpi, kuidas kasutada oma andmeid Azure OpenAI teenusega. See Microsoft Learni moodul pakub kõikehõlmavat juhendit RAG rakendamiseks</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivse AI rakenduste hindamine Microsoft Foundry abil: Artikkel käsitleb mudelite hindamist ja võrdlust avalikult kättesaadavate andmestike peal, sealhulgas Agentic AI rakendused ja RAG arhitektuurid</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mis on Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Täielik juhend agendipõhisele Retrieval Augmented Generationile – Uudised generatiivse RAG kohta</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: kiirendage oma RAG päringu ümberkirjutamise ja enese-päringu abil! Hugging Face avatud lähtekoodiga tehisintellekti kokaraamat</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentikihtide lisamine RAG-ile</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Teadmusassistendi tulevik: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kuidas ehitada agentseid RAG-süsteeme</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Microsoft Foundry agenditeenuse kasutamine oma tehisintellekti agentide laiendamiseks</a>

### Akadeemilised artiklid

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: iteratiivne täiustamine enesetagasiside abil</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: keeleagentidel põhinev verbaalne tugevdatud õppimine</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: suured keelemudelid saavad ise oma tööriistadega interaktiivselt parandada</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentne päringu-kujutusega loomine: ülevaade agentsetest RAG-dest</a>

## Selle agendi esmase toimimise kontroll (valikuline)

Pärast seda, kui olete õppinud agente juurutama [õppetükk 16-s](../16-deploying-scalable-agents/README.md), saate seda õppetüki `TravelRAGAgent`-i esmalt kontrollida — veendumaks, et tema vastused jäävad teadmusbaasis põhinevaks — failiga [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Vaadake käivitamiseks juhiseid failist [`tests/README.md`](../tests/README.md).

## Eelmine õppetükk

[Tööriistade kasutamise disainimuster](../04-tool-use/README.md)

## Järgmine õppetükk

[Usaldusväärsete tehisintellekti agentide loomine](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->