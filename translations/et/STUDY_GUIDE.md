# AI-agensid algajatele - õppematerjal ja kursuse kokkuvõte

See juhend annab kokkuvõtte "AI Agents for Beginners" kursusest ning selgitab peamisi kontseptsioone, raamistikke ja disainimustreid AI-agenside ehitamiseks.

## 1. Sissejuhatus AI-agensitesse

**Mis on AI-agensid?**
AI-agensid on süsteemid, mis laiendavad suurte keelemudelite (LLMs) võimekust, andes neile juurdepääsu **tööriistadele**, **teadmistele** ja **mälule**. Erinevalt tavalise LLM-chatbot'ist, mis ainult genereerib teksti treeningandmete põhjal, võib AI-agens:
- **Taju** oma keskkonda (andurite või sisendite kaudu).
- **Mõtleb** selle üle, kuidas probleemi lahendada.
- **Tegutseb** keskkonna muutmiseks (aktuaatorite või tööriistade käivitamise kaudu).

**Agendi põhikomponendid:**
- **Keskkond**: Ruum, kus agent tegutseb (nt broneerimissüsteem).
- **Sensorid**: Mehhanismid info kogumiseks (nt API lugemine).
- **Aktuaatorid**: Mehhanismid tegevuste sooritamiseks (nt e-kirja saatmine).
- **Aju (LLM)**: Järeldamismootor, mis planeerib ja otsustab, milliseid toiminguid teha.

## 2. Agentide raamistikud

Kursus kasutab **Microsoft Agent Framework (MAF)** koos **Azure AI Foundry Agent Service V2** agentide ehitamiseks:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Ühendatud Python/C# SDK agentide, tööriistade ja töövoogude jaoks | Agentide loomine tööriistadega, mitmeagendiliste töövoogude ja tootmistavade jaoks. |
| **Azure AI Foundry Agent Service** | Hallatud pilve käituskeskkond | Turvaline, skaleeritav juurutus koos sisseehitatud oleku halduse, jälgitavuse ja usaldusega. |

## 3. Agentide disainimustrid

Disainimustrid aitavad struktureerida, kuidas agendid toimivad, et lahendada probleeme usaldusväärselt.

### **Tööriistade kasutamise muster** (Õppetund 4)
See muster võimaldab agentidel suhelda välismaailmaga.
- **Kontseptsioon**: Agendile antakse "skeem" (loetelu saadaolevatest funktsioonidest ja nende parameetritest). LLM otsustab *millist* tööriista kutsuda ja *milliste* argumentidega, lähtudes kasutaja taotlusest.
- **Töövoog**: User Request -> LLM -> **Tööriista valik** -> **Tööriista täitmine** -> LLM (tööriista väljundiga) -> Lõplik vastus.
- **Kasutusjuhtumid**: Reaalajas andmete hankimine (ilm, aktsiahinnad), arvutuste tegemine, koodi täitmine.

### **Planeerimise muster** (Õppetund 7)
See muster võimaldab agentidel lahendada keerukaid, mitmeastmelisi ülesandeid.
- **Kontseptsioon**: Agent jagab kõrgetasemelise eesmärgi järjestikusteks väiksemateks alamülesanneteks.
- **Lähenemised**:
  - **Ülesande dekompositsioon**: Jagades "Reisi planeerimine" osadeks "Broneeri lend", "Broneeri hotell", "Üüri auto".
  - **Iteratiivne planeerimine**: Plaani uuesti hindamine varasemate sammude väljundi põhjal (nt kui lend on täis, vali teine kuupäev).
- **Rakendus**: Sageli hõlmab see "Planeerija" agenti, mis genereerib struktureeritud plaani (nt JSON), mida seejärel täidavad teised agendid.

## 4. Disainipõhimõtted

Agentide disainimisel arvestage kolme dimensiooniga:
- **Ruum**: Agendid peaksid ühendama inimesi ja teadmisi, olema ligipääsetavad, kuid mitte pealetükkivad.
- **Aeg**: Agendid peaksid õppima *minevikust*, pakkuma asjakohaseid vihjeid *praegusel hetkel* ja kohanema *tuleviku jaoks*.
- **Tuum**: Aktsepteeri ebakindlust, kuid loo usaldus läbipaistvuse ja kasutaja kontrolli kaudu.

## 5. Oluliste õppetundide kokkuvõte

- **Õppetund 1**: Agendid on süsteemid, mitte ainult mudelid. Nad tajuvad, teevad järeldusi ja tegutsevad.
- **Õppetund 2**: Microsoft Agent Framework abstraheerib tööriistakõnede ja oleku haldamise keerukuse.
- **Õppetund 3**: Disaini, silmas pidades läbipaistvust ja kasutaja kontrolli.
- **Õppetund 4**: Tööriistad on agendi "käed". Skeemi defineerimine on LLM-ile ülioluline, et mõista, kuidas neid kasutada.
- **Õppetund 7**: Planeerimine on agendi "juhtfunktsioon", mis võimaldab tal käsitleda keerukaid töövooge.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Lahtiütlus:
Seda dokumenti on tõlgitud tehisintellekti-põhise tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, võivad automaatsed tõlked sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleb pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega väärtõlgete eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->