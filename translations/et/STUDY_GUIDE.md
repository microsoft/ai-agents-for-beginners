# AI agendid algajatele - õppejuhend ja kursuse kokkuvõte

See juhend annab ülevaate kursusest "AI Agents for Beginners" ning selgitab peamisi mõisteid, raamistikke ja disainimustreid AI-agentide loomisel.

## 1. Sissejuhatus AI-agentidesse

**Mis on AI-agentid?**
AI-agentid on süsteemid, mis laiendavad suurte keelemudelite (LLM-ide) võimeid, andes neile juurdepääsu **tööriistadele**, **teadmistele** ja **mälule**. Erinevalt tavalisest LLM-chatbotist, mis genereerib teksti ainult treeningandmete põhjal, suudab AI-agent:
- **Tajuda** oma keskkonda (sensorite või sisendite kaudu).
- **Mõelda**, kuidas probleemi lahendada.
- **Tegutseda**, et keskkonda muuta (aktuaatorite või tööriistade käivitamise kaudu).

**Agendi põhikomponendid:**
- **Keskkond**: Ruum, kus agent tegutseb (nt. broneerimissüsteem).
- **Sensorid**: Mehhanismid info kogumiseks (nt. API lugemine).
- **Aktuaatorid**: Mehhanismid tegevuste sooritamiseks (nt. e-kirja saatmine).
- **Aju (LLM)**: Mõtlemise ja otsustamise mootor, mis planeerib ja otsustab, milliseid toiminguid ette võtta.

## 2. Agendiraamistikud

Kursus kasutab **Microsoft Agent Framework (MAF)** koos **Azure AI Foundry Agent Service V2** agentide ehitamiseks:

| Komponent | Fookus | Parim kasutus |
|-----------|--------|---------------|
| **Microsoft Agent Framework** | Ühtne Python/C# SDK agentide, tööriistade ja töövoogude jaoks | Agentide ehitamine, mis kasutavad tööriistu, mitmeagendi töövoogusid ja tootmismustreid. |
| **Azure AI Foundry Agent Service** | Haldatud pilve käituskeskkond | Turvaline, skaleeritav juurutus koos sisseehitatud olekuhalduse, jälgitavuse ja usaldusfunktsioonidega. |

## 3. Agentide disainimustrid

Disainimustrid aitavad struktureerida, kuidas agendid tegutsevad, et probleeme usaldusväärselt lahendada.

### **Tööriistakasutuse muster** (Õppetund 4)
See muster võimaldab agentidel suhelda välismaailmaga.
- **Kontseptsioon**: Agendile antakse "skeem" (loend saadaolevatest funktsioonidest ja nende parameetritest). LLM otsustab *millist* tööriista kutsuda ja *milliste* argumentidega vastavalt kasutaja päringule.
- **Töövoog**: Kasutaja päring -> LLM -> **Tööriista valik** -> **Tööriista täitmine** -> LLM (tööriista väljundiga) -> Lõplik vastus.
- **Kasutusjuhtumid**: Reaalajas andmete pärimine (ilm, aktsiahinnad), arvutuste tegemine, koodi käivitamine.

### **Planeerimismuster** (Õppetund 7)
See muster võimaldab agentidel lahendada keerukaid, mitmeastmelisi ülesandeid.
- **Kontseptsioon**: Agent jagab kõrgetasemelise eesmärgi järjestikuseks väiksemateks alamülesanneteks.
- **Lähenemised**:
  - **Ülesande lagundamine**: "Planeeri reis" jagamine "Broneeri lend", "Broneeri hotell", "Üüri auto".
  - **Iteratiivne planeerimine**: Plaani ülevaatamine eelnevate sammude väljundi põhjal (nt. kui lend on täis, valida teine kuupäev).
- **Rakendamine**: Sageli hõlmab see "Planeerija" agenti, mis genereerib struktureeritud plaani (nt. JSON), mida seejärel täidavad teised agendid.

## 4. Disainipõhimõtted

Agendeid disainides tuleks arvestada kolme mõõdet:
- **Ruumi**: Agendid peaksid ühendama inimesi ja teadmisi, olema ligipääsetavad, kuid mitte pealetükkivad.
- **Aeg**: Agendid peaksid õppima *Minevikust*, pakkuma asjakohaseid vihjeid *Praegu* ja kohanduma *Tuleviku* jaoks.
- **Tuumik**: Võtke ebakindlus omaks, kuid looge usaldus läbipaistvuse ja kasutaja kontrolli kaudu.

## 5. Peamiste õppetundide kokkuvõte

- **Õppetund 1**: Agendid on süsteemid, mitte ainult mudelid. Nad tajuvad, mõtlevad ja tegutsevad.
- **Õppetund 2**: Microsoft Agent Framework abstraktiseerib tööriistade kutsumise ja oleku haldamise keerukust.
- **Õppetund 3**: Disaini, arvestades läbipaistvust ja kasutaja kontrolli.
- **Õppetund 4**: Tööriistad on agendi "käed". Skeemi määratlus on LLM-i jaoks kriitilise tähtsusega, et mõista, kuidas neid kasutada.
- **Õppetund 7**: Planeerimine on agendi "täitevfunktsioon", mis võimaldab tal tegeleda keerukate töövoogudega.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
See dokument on tõlgitud tehisintellekti tõlketeenuse Co‑op Translator (https://github.com/Azure/co-op-translator) abil. Kuigi me püüdleme täpsuse poole, palun pidage meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algset dokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse või väärtõlgenduse eest, mis võib tuleneda selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->