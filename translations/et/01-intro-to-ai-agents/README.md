[![Sissejuhatus tehisintellekti agentidesse](../../../translated_images/et/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Vajuta ülalolevale pildile, et vaadata selle õppetunni videot)_

# Sissejuhatus tehisintellekti agentidesse ja agentide kasutusjuhtumitesse

Tere tulemast **Tehisintellekti agentide algajate kursusele**! See kursus annab sulle põhiteadmised — ja päris töötava koodi — et alustada tehisintellekti agentide loomist nullist.

Tule ja ütle tere <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discordi kogukonnas</a> — seal on palju õppijaid ja AI arendajaid, kes on rõõmsad küsimustele vastamiseks.

Enne ehitusega alustamist veendume, et me tegelikult mõistame, mis asi AI agent *on* ja millal on mõistlik seda kasutada.

---

## Sissejuhatus

See õppetund hõlmab:

- Mis on AI agentid ja millised erinevad tüübid eksisteerivad
- Milliste ülesannete jaoks on AI agentid kõige paremini sobivad
- Peamised koostisosad, mida kasutad agentpõhise lahenduse kavandamisel

## Õpieesmärgid

Selle õppetunni lõpuks peaksid suutma:

- Selgitada, mis on AI agent ja kuidas see erineb tavalisest AI lahendusest
- Teada, millal kasutada AI agenti (ja millal mitte)
- Kavandada põhjalik agentpõhine lahendus reaalsele probleemile

---

## AI agentide määratlemine ja AI agentide tüübid

### Mis on AI agentid?

Siin on lihtne viis sellele mõelda:

> **AI agentid on süsteemid, mis võimaldavad suurte keelemudelite (LLMide) *tegutsema* hakata — andes neile tööriistad ja teadmised maailma mõjutamiseks, mitte ainult vastamiseks avaldustele.**

Lahtipakkides see veidi:

- **Süsteem** — AI agent ei ole lihtsalt üks asi. See on mitme osa kooslus, mis töötab koos. Iga agendi põhiosas on kolm osa:
  - **Keskkond** — Ruumi, milles agent töötab. Reisiagentuuri puhul oleks see broneerimisplatvorm ise.
  - **SENSORID** — Kuidas agent loeb oma keskkonna praegust seisundit. Meie reisiagent võib kontrollida hotelli saadavust või lennupileti hindu.
  - **AKTUAATORID** — Kuidas agent tegutseb. Reisiagent võib broneerida toa, saata kinnitusmeili või tühistada broneeringu.

![Mis on AI agentid?](../../../translated_images/et/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suured keelemudelid** — Agentid eksisteerisid juba enne LLM-e, kuid LLM-id teevad moodsaid agente nii võimsaks. Nad mõistavad loomulikku keelt, arutlevad konteksti üle ja muudavad ebamäärase kasutajapäringu konkreetseks tegevuskavaks.

- **Tegevuste sooritamine** — Ilma agent-süsteemita genereerib LLM ainult teksti. Agent-süsteemi sees saab LLM tegelikult samme *teostada* — otsida andmebaasist, kutsuda API-d, saata sõnumit.

- **Ligipääs tööriistadele** — Milliseid tööriistu agent saab kasutada sõltub (1) keskkonnast, kus see töötab, ja (2) mida arendaja on talle andnud. Reisiagent võib otsida lende, kuid mitte muuta kliendiandmeid — kõik sõltub sellest, mida ühendad.

- **Mälu ja teadmised** — Agentidel võib olla lühiajalist mälu (praegune vestlus) ja pikaajalist mälu (klientide andmebaas, varasemad interaktsioonid). Reisiagent võib „meeles pidada“, et sulle meeldivad aknaäärsed kohad.

---

### AI agentide erinevad tüübid

Kõik agentid pole ehitatud ühtemoodi. Siin on põhitüüpide jaotus, kasutades jooksva näitena reisiagentuuri:

| **Agendi tüüp** | **Mida ta teeb** | **Reisiagendi näide** |
|---|---|---|
| **Lihtsad refleksagentid** | Järgib kõvasti kodeeritud reegleid — pole mälu ega planeerimist. | Näeb kaebuse meili → suunab klienditeenindusse. Sellega on kõik. |
| **Mudelpõhised refleksagentid** | Hoidab sisemist maailma mudelit ja uuendab seda, kui asjad muutuvad. | Jälgib ajaloolisi lennuhindu ja märgib marsruute, mis on äkki kalliks läinud. |
| **Eesmärgipõhised agentid** | Omab eesmärki ja leiab samm-sammult, kuidas selle saavutada. | Broneerib kogu reisi (lennud, auto, hotell) sinu asukohast sihtkohta jõudmiseks. |
| **Tarakogupõhised agentid** | Ei leia ainult *üht* lahendust, vaid *parimat*, kaaludes erinevaid tegureid. | Tasakaalustab kulu ja mugavuse, et leida sinu eelistuste kohaselt parim reis. |
| **Õppivad agentid** | Parandab end aja jooksul tagasiside põhjal. | Kohandab tulevasi broneerimissoovitusi pärast reisi tehtud küsitluste põhjal. |
| **Hierarhilised agentid** | Kõrgema taseme agent jagab töö alamülesanneteks ja delegeerib madalama taseme agentidele. | „Tühista reis“ päring jaguneb: tühista lend, tühista hotell, tühista autorent — igaüht käsitleb alamagent. |
| **Mitme agendi süsteemid (MAS)** | Mitmed iseseisvad agentid töötavad koos (või konkureerivad). | Koostöö: eraldi agentid tegelevad hotellide, lendude ja meelelahutusega. Konkurents: mitmed agentid võistlevad hotellitubade pakkumisega parima hinnaga. |

---

## Millal kasutada AI agente

See, et saad kasutada AI agenti, ei tähenda, et peaksid seda alati tegema. Siin on olukorrad, kus agentid tõeliselt säravad:

![Millal kasutada AI agente?](../../../translated_images/et/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avatud lõpptulemustega probleemid** — Kui probleemi lahendamiseks samme ei saa eelprogrammeerida. Sul on vaja, et LLM leiaks tee dünaamiliselt.
- **Mitmesammulised protsessid** — Ülesanded, mis vajavad mitmel korral tööriistade kasutamist, mitte lihtsalt ühekordset otsingut või genereerimist.
- **Paranemine aja jooksul** — Kui soovid, et süsteem muutuks targemaks kasutajate tagasiside või keskkonnasignaalide põhjal.

Lisame selle teemasse sügavust kursuse edaspidises õppetunnis **Usaldusväärsete AI agentide loomine**.

---

## Agendipõhiste lahenduste alused

### Agendi arendus

Esimene asi agendi loomisel on määratleda *mida ta teha saab* — tema tööriistad, tegevused ja käitumised.

Selles kursuses kasutame põhiplatvormina **Azure AI Agent Service'i**. See toetab:

- Modelle pakkujatelt nagu OpenAI, Mistral ja Meta (Llama)
- Lusendatud andmeid pakkujatelt nagu Tripadvisor
- Standardiseeritud OpenAPI 3.0 tööriistade määratlusi

### Agendipõhised mustrid

Suhelda LLMidega saad läbi promptside. Agentide puhul ei saa alati igat prompti käsitsi meisterdada — agent peab tegutsema mitme sammu vältel. Siin tulevad mängu **agendipõhised mustrid**. Need on korduvkasutatavad strateegiad, kuidas LLMidega suhelda ja neid juhendada skaleeritaval ja usaldusväärsel moel.

Kursus on üles ehitatud kõige tavalisemate ja kasulikumate agendipõhiste mustrite ümber.

### Agendipõhised raamistikkud

Agendipõhised raamistikkud annavad arendajatele valmis mallid, tööriistad ja taristu agentide loomiseks. Need lihtsustavad:

- Tööriistade ja võimekuste ühendamist
- Agentide tegevuse jälgimist (ja silumist vigade korral)
- Koostööd paljude agentide vahel

Selles kursuses keskendume **Microsoft Agent Framework'ile (MAF)**, et luua tootmisvalmis agente.

---

## Koodinäited

Valmis nägema seda tegutsemas? Siin on selle õppetunni koodinäited:

- 🐍 Python: [Agentide raamistiku näide](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agentide raamistiku näide](./code_samples/01-dotnet-agent-framework.md)

---

## Küsimusi?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et suhelda teiste õppijatega, osaleda kontoritundides ja saada AI agentide küsimustele vastused kogukonnalt.

---

## Eelmine õppetund

[Kursuse seadistamine](../00-course-setup/README.md)

## Järgmine õppetund

[Agendipõhiste raamistike uurimine](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->