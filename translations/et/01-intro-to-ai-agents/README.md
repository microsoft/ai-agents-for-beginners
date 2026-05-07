[![Sissejuhatus AI agentidesse](../../../translated_images/et/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

# Sissejuhatus AI agentidesse ja agentide kasutusjuhtumitesse

Tere tulemast kursusele **AI agentidele algajatele**! See kursus annab teile baasteadmised — ning tõelise töö koodi — AI agentide nullist ülesehitamiseks.

Tule ja tere ütle <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discordi kogukonnas</a> — see on täis õppijaid ja AI loojaid, kes on valmis küsimustele vastama.

Enne kui ehitamisele asume, veendume, et mõistame tegelikult, mis on AI agent *ja* millal on mõistlik seda kasutada.

---

## Sissejuhatus

See õppetund käsitleb:

- Mis on AI agentid ja millised erinevad tüübid eksisteerivad
- Milliste ülesannete jaoks AI agentid kõige paremini sobivad
- Peamised koostisplokid, mida kasutate agentliku lahenduse kujundamisel

## Õpieesmärgid

Selle õppetunni lõpus peaksite suutma:

- Selgitada, mis on AI agent ja kuidas see erineb tavalisest AI lahendusest
- Teada, millal kasutada AI agenti (ja millal mitte)
- Joonistada välja lihtne agentliku lahenduse kavand reaalsele probleemile

---

## AI agentide määratlemine ja AI agentide tüübid

### Mis on AI agentid?

Siin on lihtne viis selle kohta mõelda:

> **AI agentid on süsteemid, mis võimaldavad suurte keelemudelitel (LLMidel) tegelikult *tegutseda* — andes neile tööriistad ja teadmised tegutsemiseks maailmas, mitte ainult vastamiseks käsklustele.**

Võtame selle veidi lahti:

- **Süsteem** — AI agent ei ole lihtsalt üks asi. See on mitme osa kogum, mis töötab koos. Iga agendi keskmes on kolm osa:
  - **Keskkond** — Ruumi tükk, kus agent tegutseb. Reisibroneerimise agendi puhul oleks see broneerimisplatvorm ise.
  - **Sensorid** — Kuidas agent loeb oma keskkonna praegust seisundit. Meie reisibotti puhul võiks see olla hotellide saadavuse või lennupiletite hindade kontrollimine.
  - **Toimevõtjad** — Kuidas agent tegutseb. Reisibott võiks ruumi broneerida, kinnitust saata või tühistust teha.

![Mis on AI agentid?](../../../translated_images/et/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suured keelemudelid** — Agentid eksisteerisid juba enne LLM-e, kuid LLM-id muudavad kaasaegsed agentid võimsaks. Nad mõistavad loomulikku keelt, suudavad konteksti analüüsida ning muuta ebamäärase kasutajasoovi konkreetseks tegevuskavaks.

- **Tegutsema hakkamine** — Ilma agendisüsteemita genereerib LLM ainult teksti. Agendisüsteemis saab LLM tegelikult *teostada* samme — andmebaasi otsida, API-d kutsuda, sõnumit saata.

- **Juurdepääs tööriistadele** — Milliseid tööriistu agent saab kasutada sõltub (1) keskkonnast, kus ta töötab, ja (2) mida arendaja talle anda otsustas. Reisiboti puhul võib tal olla võimalus otsida lende, kuid ta ei saa kliendiandmeid muuta — kõik sõltub, mida teil ühendatud on.

- **Mälu + Teadmised** — Agentidel võib olla lühiajaline mälu (praegune vestlus) ja pikaajaline mälu (kliendiandmebaas, varasemad suhtlused). Reisibott võib „mäletada“, et eelistate aknaäärseid kohti.

---

### AI agentide erinevad tüübid

Kõik agentid ei ole ehitatud ühtemoodi. Siin on põhiliigid, kasutades näitena reisibroneerija agendi:

| **Agendi tüüp** | **Mida see teeb** | **Reisibroneerija näide** |
|---|---|---|
| **Lihtsad refleksagentid** | Järgivad kindlaksmääratud reegleid — ei mälu ega planeerimist. | Näeb kaebuskirja → suunab klienditeenindusse. Sellega kõik. |
| **Mudelpõhised refleksagentid** | Hoidavad sisemist maailma mudelit ja uuendavad seda muutuste korral. | Jälgib lennuhindade ajalugu ja märgib marsruudid, mis on ootamatult kallid. |
| **Eesmärgipõhised agentid** | Omavad eesmärki ja leiavad samm-sammult tee selle saavutamiseks. | Broneerib kogu reisi (lennud, auto, hotell) alates hetkeasukohast sihtkohta jõudmiseks. |
| **Tulu-põhised agentid** | Ei leia lihtsalt *üht* lahendust — otsib *parimat* lahendust tasakaalustades kompromisse. | Võrdleb hinda ja mugavust, et leida teie eelistustele kõige paremini sobiv reis. |
| **Õppivad agentid** | Paranevad aja jooksul tagasiside põhjal. | Kohandab tulevasi broneerimissoovitusi pärast reisi tagasiside põhjal. |
| **Hierarhilised agentid** | Kõrgetasemeline agent jagab töö alamülesanneteks ja delegeerib madalama taseme agentidele. | „Tühista reis“ palve jagatakse: lennu tühistamine, hotelli tühistamine, auto rentimise tühistamine — igaüht haldab alamagendi komponent. |
| **Mitmeagentsüsteemid (MAS)** | Mitmed sõltumatud agentid töötavad koos (või konkureerivad). | Koostöö: eraldi agentid haldavad hotelle, lende ja meelelahutust. Konkurents: mitu agenti võistlevad hotellitubade müümisel parima hinnaga. |

---

## Millal kasutada AI agente

See, et te *saate* kasutada AI agenti, ei tähenda, et peaksite alati seda tegema. Siin on olukorrad, kus agentid tõeliselt säravad:

![Millal kasutada AI agente?](../../../translated_images/et/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avatud lõpp-punktiga probleemid** — Kui sammu, kuidas probleemi lahendada, ei saa eelprogrammeerida. LLM peab suuta dünaamiliselt marsruuti määrata.
- **Mitme-sammu protsessid** — Ülesanded, mis vajavad tööriistade kasutamist mitme sammu vältel, mitte lihtsalt ühe otsingu või genereerimise korral.
- **Paranemine aja jooksul** — Kui soovite, et süsteem muutuks targemaks kasutajate tagasiside või keskkonna signaalide põhjal.

Räägime “## Usaldusväärsete AI agentide loomine” õppetunnis kursuse hilisemas osas põhjalikumalt, millal agenti kasutada (ja millal mitte).

---

## Agentlike lahenduste alused

### Agendi arendus

Esimene asi, mida agendi ehitamisel teha, on defineerida *mida ta suudab teha* — tema tööriistad, tegevused ja käitumine.

Selles kursuses kasutame peamise platvormina **Azure AI Agent Service** teenust. See toetab:

- Avatud mudeleid nagu OpenAI, Mistral ja Llama
- Litsentseeritud andmeid pakkujatelt nagu Tripadvisor
- Standardiseeritud OpenAPI 3.0 tööriistade definitsioone

### Agentlikud mustrid

Suhtlete LLM-idega käsuridade kaudu. Agendi puhul ei saa alati kõiki käsuridasid käsitsi valmistada — agent peab tegutsema mitme sammu ulatuses. Siin tulevad mängu **agentlikud mustrid**. Need on korduvkasutatavad strateegiad LLM-ide käivitamiseks ja töökorralduseks skaleeritaval ja usaldusväärsel moel.

Seda kursust juhivad kõige levinumad ja kasulikumad agentlikud mustrid.

### Agentlikud raamistikud

Agentlikud raamistikud annavad arendajatele valmis mallid, tööriistad ja infrastruktuuri agentide ehitamiseks. Need teevad lihtsamaks:

- Töötamise ühendamise tööriistadega ja võimete lisamise
- Agentide tegevuse jälgimise (ja vigade leidmise)
- Koostöö mitme agendiga

Selles kursuses keskendume **Microsoft Agent Framework’ile (MAF)** tootmisvalmis agentide loomiseks.

---

## Koodi näited

Valmis näha seda päriselus? Siin on selle õppetunni koodinäited:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Küsimused?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et suhelda teiste õppijatega, osaleda konsultatsioonitundides ja saada kogukonnalt AI agentide küsimustele vastuseid.

---

## Eelmine õppetund

[Kursuse seadistamine](../00-course-setup/README.md)

## Järgmine õppetund

[Agentlike raamistikute uurimine](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades AI tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument tema emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->