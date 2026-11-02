[![Intro to AI Agents](../../../translated_images/et/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klõpsake videokursuse video vaatamiseks ülaloleval pildil)_

# Sissejuhatus tehisintellekti agentidesse ja nende kasutusjuhtudesse

Tere tulemast **AI Agents for Beginners** kursusele! See kursus annab teile põhilised teadmised — ja tegeliku töötava koodi — et hakata AI agente nullist looma.

Tule ja tere tulemast <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discordi kogukonda</a> — see on täis õppijaid ja tehisintellekti loojad, kes vastavad hea meelega küsimustele.

Enne kui asume ehitama, veendume, et mõistame tegelikult, mis on AI agent ja millal on mõistlik seda kasutada.

---

## Sissejuhatus

Selles loos käsitleme:

- Mis on AI agentid ja erinevad tüübid, mis eksisteerivad
- Milliste ülesannete jaoks AI agentid kõige paremini sobivad
- Põhitükid, mida kasutate agentide lahenduste kujundamisel

## Õpieesmärgid

Selle õppetüki lõpuks peaksid olema võimeline:

- Selgitama, mis on AI agent ja kuidas see erineb tavapärasest AI lahendusest
- Teadma, millal kasutada AI agenti (ja millal mitte)
- Joonistama välja lihtsa agentse lahenduse disaini reaalse maailma probleemile

---

## AI agentide määratlus ja tüübid

### Mis on AI agentid?

Siin on lihtne viis sellele mõelda:

> **AI agentid on süsteemid, mis lasevad suurtel keelemudelitel (LLM) tegelikult *tegutseda* — andes neile tööriistad ja teadmised maailma mõjutamiseks, mitte ainult vastata päringutele.**

Vaatame seda lähemalt:

- **Süsteem** — AI agent ei ole ainult üks asi. See on koos töötavate osade kogum. Iga agent koosneb põhiliselt kolmest osast:
  - **Keskkond** — Ruumi, milles agent töötab. Reisibroneerimisagent puhul on see broneerimisplatvorm ise.
  - **Sensorid** — Kuidas agent loeb oma keskkonna praegust seisu. Meie reisibroneerimisagent võiks kontrollida hotellide saadavust või lennuhindu.
  - **Toimingud** — Kuidas agent tegutseb. Reisibroneerimisagent võiks broneerida toa, saata kinnitus- või tühistada broneeringu.

![Mis on AI agentid?](../../../translated_images/et/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suured keelemudelid** — Agentid eksisteerisid enne LLM-e, kuid LLM-id teevad tänapäeva agentid väga võimsaks. Nad mõistavad loomulikku keelt, arutlevad konteksti üle ja muudavad ebamäärased kasutajasoovid konkreetseteks tegutsemisplaanideks.

- **Tegevuste täitmine** — Ilma agendita genereerib LLM lihtsalt teksti. Agendi süsteemis saab LLM tegelikult *teha samme* — otsida andmebaasist, helistada API-le, saata sõnumeid.

- **Juurdepääs tööriistadele** — Milliseid tööriistu agent saab kasutada sõltub (1) keskkonnast, milles see töötab, ja (2) arendaja valikutest, mida talle anda. Reisibroneerimisagent võib osata lennuotsi teha, kuid mitte muuta kliendi andmeid — kõik sõltub sellest, kuidas selle ühendad.

- **Mälu + Teadmised** — Agentidel võib olla lühiajaline mälu (praegune vestlus) ja pikaajaline mälu (kliendi andmebaas, varasemad suhtlused). Reisibroneerimisagent võib "mäletada", et eelistad aknaäärseid istekohti.

---

### Erinevad AI agentide tüübid

Kõik agentid ei ole ehitatud samamoodi. Siin on põhiliigid, kasutades reisibroneerimisagenti näidet:

| **Agendi tüüp** | **Mida ta teeb** | **Reisibroneerimisagendi näide** |
|---|---|---|
| **Lihtsad refleksagentid** | Järgivad rangelt kodeeritud reegleid — pole mälu ega planeerimist. | Näeb kaebuskirja → edastab klienditeenindusele. Täpselt nii. |
| **Mudeli-põhised refleksagentid** | Hoidavad sisemist maailma mudelit ja uuendavad seda muutuste korral. | Jälgib lennuhindade ajaloolisi andmeid ja märgib marsruudid, mis äkitselt kalliks muutuvad. |
| **Eesmärgipõhised agentid** | Omab eesmärki ja plaanib samm-sammult selle saavutamist. | Broneerib kogu reisi (lennud, auto, hotell), alustades sinu praegusest asukohast sihtkohta jõudmiseks. |
| **Kasulikkuspõhised agentid** | Ei leia lihtsalt *üht* lahendust — leiab *parima* kaaludes kompromisse. | Tasakaalustab kulu ja mugavust, et leida reisi, mis vastab kõige paremini su eelistustele. |
| **Õpivad agentid** | Paranevad aja jooksul, õppides tagasisidest. | Kohandab tulevasi broneerimissoovitusi tuginedes pärast reisi tehtud küsimustikele. |
| **Hierarhilised agentid** | Kõrgema taseme agent jagab töö alamülesanneteks ja delegeerib need madalama taseme agentidele. | "Tühista reis" päringu puhul jagatakse ülesanded: tühista lend, tühista hotell, tühista autorent — igaüht tegeleb alamagent. |
| **Mitmeagent-süsteemid (MAS)** | Mitu sõltumatut agenti töötavad koos (või võistlevad). | Koostöö: eri agentidel vastutus hotellide, lendude ja meelelahutuse haldamisel. Võistlus: mitmed agentid võistlevad hotellitubade täitmise eest parima hinnaga. |

---

## Millal kasutada AI agente

Fakt, et *võid* AI agenti kasutada, ei tähenda, et peaksid seda alati tegema. Siin on olukorrad, kus agentid tõeliselt silma paistavad:

![Millal kasutada AI agente?](../../../translated_images/et/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avatud lõpp-punktiga probleemid** — Kui probleemi lahendamise samme ei saa ette programmeerida. LLM peab ise teed dünaamiliselt leidma.
- **Mitmeetapilised protsessid** — Ülesanded, mis nõuavad tööriistade kasutamist mitmel sammul, mitte ainult ühe otsingu või generaatori tegemist.
- **Ajapikku paranemine** — Kui soovid, et süsteem muutuks targemaks kasutaja tagasiside või keskkonna signaalide põhjal.

Süvatsi uurime, millal on sobilik (ja millal mitte) AI agente kasutada hiljem kursuse õppetükis **Usaldusväärsete AI agentide loomine**.

---

## Agentsete lahenduste põhialused

### Agendi arendamine

Esimene asi, mida agendi loomisel teha, on määratleda *mida ta saab teha* — selle tööriistad, tegevused ja käitumised.

Selles kursuses kasutame põhiliselt **Microsoft Foundry Agent Service** platvormi. See toetab:

- Modelle teenusepakkujatelt nagu OpenAI, Mistral ja Meta (Llama)
- Litsentseeritud andmeid teenusepakkujatelt, näiteks Tripadvisor
- Standardiseeritud OpenAPI 3.0 tööriista definitsioone

### Agendsed mustrid

Suheldes LLM-idega kasutad päringuid. Agentide puhul ei saa alati kõiki päringuid käsitsi valmistada — agent peab võtma meetmeid mitmel sammul. Siin tulevad mängu **agendsed mustrid**. Need on korduvkasutatavad strateegiad LLM-ide kutsumiseks ja korraldamiseks skaleeritaval ja usaldusväärsel moel.

Selle kursuse ülesehitus tugineb kõige tavalisematele ja kasulikumatele agendsetele mustritele.

### Agendsed raamistikud

Agendsed raamistikud annavad arendajatele valmis mallid, tööriistad ja infrastruktuuri agentide ehitamiseks. Need muudavad lihtsamaks:

- Tööriistade ja võimaluste ühendamise
- Agendi tegevuse jälgimise (ja veaotsingu, kui midagi läheb valesti)
- Koostöö mitme agendi vahel

Selles kursuses keskendume **Microsoft Agent Framework (MAF)** kasutamisele tootmiseks valmis agentide ehitamiseks.

---

## Koodinäited

Oled valmis nägema, kuidas see toimib? Siin on selle õppetüki koodinäited:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Kas on küsimusi?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et suhelda teiste õppijatega, osaleda töötubades ja saada AI agentide küsimustele kogukonna vastused.


---

## Agendi põhitestimine (valikuline)

Kui oled õppinud agentide käivitamist [õppest 16](../16-deploying-scalable-agents/README.md), saad lisada selle õppetüki `TravelAgent` jaoks kiire tervisekontrolli pärast käivitust kasutades valmis kataloogi [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Vaata, kuidas seda käivitada, failist [`tests/README.md`](../tests/README.md).

---

## Eelmine õppetükk

[Kursuse käivitamine](../00-course-setup/README.md)

## Järgmine õppetükk

[Agentsete raamistikude uurimine](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->