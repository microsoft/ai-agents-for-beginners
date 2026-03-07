[![Intro to AI Agents](../../../translated_images/et/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klõpsake ülal oleval pildil, et vaadata selle tunni videot)_


# Sissejuhatus AI agentidesse ja nende kasutusjuhtudesse

Tere tulemast kursusele "AI agentide algajatele"! See kursus pakub põhilisi teadmisi ja rakendusnäiteid AI agentide loomiseks.

Liituge <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discordi kogukonnaga</a>, et kohtuda teiste õppijate ja AI agentide arendajatega ning esitada kõik oma küsimused selle kursuse kohta.

Kursuse alustamiseks vaatleme esmalt paremini, mis on AI agendid ja kuidas me saame neid kasutada rakendustes ja töövoogudes, mida me loome.

## Sissejuhatus

See tund hõlmab:

- Mis on AI agendid ja millised on erinevat tüüpi agendid?
- Millised kasutusjuhtumid sobivad kõige paremini AI agentidele ja kuidas nad saavad meid aidata?
- Millised on mõned põhilised ehitusplokid, kui disainime agentipõhiseid lahendusi?

## Õpieesmärgid
Pärast selle tunni lõpetamist peaksid oskama:

- Mõista AI agentide mõisteid ja seda, kuidas nad erinevad teistest AI lahendustest.
- Rakendada AI agente kõige tõhusamalt.
- Kujundada agentipõhiseid lahendusi produktiivselt nii kasutajate kui ka klientide jaoks.

## AI agentide määratlus ja agentide tüübid

### Mis on AI agendid?

AI agendid on **süsteemid**, mis võimaldavad **suurtel keelemudelitel (LLM-del)** **tegevusi sooritada**, laiendades nende võimeid, andes LLM-idele **ligipääsu tööriistadele** ja **teadmistele**.

Lahutame selle definitsiooni väiksemateks osadeks:

- **Süsteem** – oluline on mõista agente mitte ainult kui üht komponenti, vaid kui mitmest komponendist koosnevat süsteemi. Põhilisel tasemel on AI agendi komponendid:
  - **Keskkond** – määratletud ruum, kus AI agent tegutseb. Näiteks kui meil oleks reisibroneerimise AI agent, oleks keskkond reisibroneerimissüsteem, mida AI agent kasutab ülesannete täitmiseks.
  - **Sensorid** – keskkond omab informatsiooni ja annab tagasisidet. AI agendid kasutavad sensoreid selle teabe kogumiseks ja tõlgendamiseks keskkonna praeguse seisundi kohta. Reisibroneerimisagentide näites võib broneerimissüsteem anda infot näiteks hotellide saadavuse või lennuhindade kohta.
  - **Aktuaatorid** – kui AI agent on saanud keskkonna hetkeseisundi, määrab agent ülesande raames, mis tegevus tuleb keskkonna muutmiseks sooritada. Reisibroneerimisagent võib näiteks broneerida kasutajale saadaoleva toa.

![Mis on AI agendid?](../../../translated_images/et/what-are-ai-agents.1ec8c4d548af601a.webp)

**Suured keelemudelid (LLM-id)** – agendi kontseptsioon eksisteeris juba enne LLM-ide loomist. LLM-idega AI agentide ehitamise eeliseks on nende võime tõlgendada inimkeelt ja andmeid. See võime võimaldab LLM-idel tõlgendada keskkonna teavet ja määratleda plaani keskkonna muutmiseks.

**Tegevuste sooritamine** – väljaspool AI agendi süsteeme on LLM-id piiratud olukordadega, kus tegevus on sisu või info genereerimine kasutaja sisendi põhjal. AI agendi süsteemides saavad LLM-id täita ülesandeid, tõlgendades kasutaja päringut ja kasutades tööriistu, mis on nende keskkonnas saadaval.

**Ligipääs tööriistadele** – millistele tööriistadele LLM-il ligipääs on, määrab 1) keskkond, kus see tegutseb, ja 2) AI agendi arendaja. Meie reisibroneerimisagentide näites on agendi tööriistad piiratud broneerimissüsteemi funktsioonidega ning/ või saab arendaja piirata agendi tööriistade ligipääsu ainult lendudele.

**Mälu + Teadmised** – mälu võib olla lühiajaline kasutaja ja agendi vahelise vestluse kontekstis. Pikaajaline mälu, keskkonna poolt pakutava info kõrval, võimaldab AI agentidel ka teadmisi pärida teistest süsteemidest, teenustest, tööriistadest ja isegi teistest agentidest. Näiteks reisibroneerimisagent võib saada teadmisi kasutaja reisieelistuste kohta kliendibaasist.

### Erinevad agentide tüübid

Nüüd, kui meil on üldine definitsioon AI agentidele, vaatleme mõningaid konkreetseid agentide tüüpe ja kuidas neid saaks rakendada reisibroneerimisagentide puhul.

| **Agendi tüüp**               | **Kirjeldus**                                                                                                                        | **Näide**                                                                                                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lihtsad refleksagentid**    | Teevad koheseid tegevusi eelmääratletud reeglite põhjal.                                                                              | Reisibroneerimisagent tõlgendab e-kirja konteksti ja suunab reisikaebused klienditeenindusse.                                                                                                                                   |
| **Mudeli põhised refleksagentid** | Tegevused tuginevad maailma mudelil ja selle mudeli muutustel.                                                                       | Reisibroneerimisagent annab prioriteedi marsruutidele, kus on märkimisväärsed hinnamuutused, tuginedes ajaloolisele hinnainfole.                                                                                               |
| **Eesmärgipõhised agentid**    | Koostavad plaane kindlate eesmärkide saavutamiseks, tõlgendades eesmärki ja määrates tegevusi selle täitmiseks.                     | Reisibroneerimisagent broneerib reisi, määrates vajalikud reisikorraldused (auto, ühistransport, lennud) praegusest asukohast sihtkohta.                                                                                      |
| **Kasulikkuspõhised agentid**  | Võtavad arvesse eelistusi ja kaaluvad kompromisse numbriliselt, et määrata, kuidas eesmärke kõige paremini saavutada.               | Reisibroneerimisagent maksimeerib kasulikkust, kaaludes mugavust võrreldes kuludega reisi broneerimisel.                                                                                                                      |
| **Õppivad agentid**            | Paranevad aja jooksul, reageerides tagasisidele ja kohandades tegevusi vastavalt.                                                    | Reisibroneerimisagent parendab oma toimimist, kasutades klientide tagasisidet reisijärgsest ankeetidest, et teha tulevaste broneeringute jaoks parandusi.                                                                    |
| **Hierarhilised agentid**      | Sisaldavad mitut agenti kihilises süsteemis, kus kõrgemase taseme agendid jagavad ülesanded väiksemateks aluseks madalamatele agentidele. | Reisibroneerimisagent tühistab reisi, jagades ülesande alamosadeks (näiteks konkreetsete broneeringute tühistamine) ning madalamad agendid täidavad neid ja annavad tagasisidet kõrgema taseme agendile.                       |
| **Mitmeagendilised süsteemid (MAS)** | Agendid täidavad ülesandeid iseseisvalt, kas koostööd tehes või konkurentsis olles.                                                  | Koostöös: Mitmed agendid broneerivad konkreetseid reisiteenuseid nagu hotellid, lennud ja meelelahutus. Konkurentsis: Mitmed agendid haldavad ja konkureerivad ühise hotelli broneerimiskalendri üle, et broneerida kliente hotelli. |

## Millal kasutada AI agente

Eelnevas osas kasutasime näitena reisibroneerimisagentuuri kasutusjuhtu, et selgitada, kuidas eri tüüpi agendid sobivad erinevatesse reisibroneerimise stsenaariumitesse. Jätkame selle rakenduse kasutamist kogu kursuse jooksul.

Vaatame, milliseid kasutusjuhtumeid AI agentide jaoks kõige paremini sobib:

![Millal kasutada AI agente?](../../../translated_images/et/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Avatud lõpp-päringud** – võimaldades LLM-il määrata vajalikud sammud ülesande täitmiseks, sest kõiki protsesse ei saa alati töösse kõvasti kodeerida.
- **Mitmetasemelised protsessid** – ülesanded, mille puhul on vajalik teatud keerukuse tase, kus AI agent peab kasutama tööriistu või infot mitme sammuna, mitte ühekordse päringuga.  
- **Aja jooksul parendamine** – ülesanded, kus agent saab aja jooksul parandada oma võimeid, saades tagasisidet kas oma keskkonnast või kasutajatelt, et pakkuda paremat kasulikkust.

Me käsitleme täpsemaid kaalutlusi AI agentide kasutamisel usaldusväärsete AI agentide loomise tunnis.

## Agentipõhiste lahenduste alused

### Agendi arendamine

Esimene samm AI agendi süsteemi kujundamisel on määratleda tööriistad, tegevused ja käitumised. Selles kursuses keskendume **Azure AI Agent Service** kasutamisele agentide määratlemiseks. See teenus pakub funktsioone nagu:

- Valik avatud mudeleid nagu OpenAI, Mistral ja Llama
- Litsentseeritud andmete kasutamine pakkujate kaudu nagu Tripadvisor
- Standardiseeritud OpenAPI 3.0 tööriistade kasutamine

### Agentipõhised mustrid

Suhtlus LLM-idega toimub päringute kaudu. Arvestades AI agentide poolautonoomset olemust, ei ole alati võimalik ega vajalik käsitsi LLM-i uuesti pärida pärast keskkonna muutumist. Kasutame **agentipõhiseid mustreid**, mis võimaldavad LLM-i pärida mitme sammu jooksul skaleeritaval viisil.

Kursus on jagatud mõneks praegu populaarseks agentipõhiseks mustriks.

### Agentipõhised raamistikud

Agentipõhised raamistikud võimaldavad arendajatel rakendada agentipõhiseid mustreid koodi kaudu. Need raamistikud pakuvad malle, pistikprogramme ja tööriistu parema AI agentide koostöö jaoks. Need eelised võimaldavad paremat jälgitavust ja tõrkeotsingut AI agendi süsteemides.

Selles kursuses uurime Microsoft Agent Frameworki (MAF) põhitootmisvalmiste AI agentide loomiseks.

## Näidiskoodid

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Kas sul on AI agentide kohta rohkem küsimusi?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda konsultatsioonitundides ja saada vastused oma AI agentide küsimustele.

## Eelmine tund

[Kursuse seadistus](../00-course-setup/README.md)

## Järgmine tund

[Agentipõhiste raamistikute uurimine](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun pidage meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või väärtõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->