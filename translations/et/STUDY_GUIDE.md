# AI Agendid Algajatele - Õppejuhend ja Kursuse Kokkuvõte

See juhend annab ülevaate kursusest "AI Agendid Algajatele" ja selgitab põhikontseptsioone, raamistikke ja disainimustreid AI agentide ehitamiseks.

## 1. Sissejuhatus AI Agentidesse

**Mis on AI Agendid?**
AI agendid on süsteemid, mis laiendavad Suurte Keelemudelite (LLM-ide) võimalusi, andes neile juurdepääsu **tööriistadele**, **teadmistele** ja **mälule**. Erinevalt tavalisest LLM-i vestlusrobotist, mis ainult genereerib teksti treeningandmete põhjal, saab AI agent:
- **Tajuda** oma keskkonda (sensorite või sisendite kaudu).
- **Arutleda** selle üle, kuidas probleemi lahendada.
- **Teha** tegevusi keskkonna muutmiseks (hädavalt tööriistade või tegevuste abil).

**Agendi Põhikomponendid:**
- **Keskkond**: Ruumi, kus agent tegutseb (nt broneerimissüsteem).
- **Sensorid**: Mehhanismid info kogumiseks (nt API lugemine).
- **Tegutsejad**: Mehhanismid tegevuste sooritamiseks (nt e-kirja saatmine).
- **Aju (LLM)**: Mõtlemisosa, mis planeerib ja otsustab, milliseid tegevusi teha.

## 2. Agentseadme Raamistikud

Kursus käsitleb kolme peamist agentide loomise raamistikku:

| Raamistik | Fookus | Parim Kasutuseks |
|-----------|---------|------------------|
| **Semantic Kernel** | Tootmiskõlblik SDK .NET/Python jaoks | Ettevõtte rakendused, AI integreerimine olemasoleva koodiga. |
| **AutoGen** | Mitme agendi koostöö | Keerulised olukorrad, kus mitu spetsialiseerunud agenti omavahel suhtlevad. |
| **Azure AI Agent Service** | Haldatud pilveteenus | Turvaline, skaleeritav juurutus koos sisseehitatud olekuhaldusega. |

## 3. Agentseadme Disainimustrid

Disainimustrid aitavad struktuureerida agentide tööd, et lahendada probleeme usaldusväärselt.

### **Tööriistade Kasutamise Muster** (Õppetund 4)
See muster võimaldab agentidel suhelda välismaailmaga.
- **Kontseptsioon**: Agendile antakse "skeem" (järjestus saadavalolevatest funktsioonidest ja nende parameetritest). LLM otsustab, *millist* tööriista valida ja *milliste* argumentidega vastavalt kasutaja päringule.
- **Voog**: Kasutaja Päring -> LLM -> **Tööriista Valik** -> **Tööriista Käivitamine** -> LLM (tööriista väljundiga) -> Lõplik Vastus.
- **Kasutusjuhtumid**: Reaalajas andmete (ilm, aktsiakulud) hankimine, arvutuste tegemine, koodi käivitamine.

### **Planeerimise Muster** (Õppetund 7)
See muster võimaldab agentidel lahendada keerukaid, mitmeastmelisi ülesandeid.
- **Kontseptsioon**: Agent jagab kõrgetasemelise eesmärgi väiksemateks osülesanneteks.
- **Lähenemised**:
  - **Ülesannete Lahutamine**: Jagades "Reisi planeerimise" "Lennu broneerimiseks", "Hotelli broneerimiseks", "Autoliisi jaoks".
  - **Iteratiivne Planeerimine**: Plaani uuesti hindamine varasemate sammude väljundi põhjal (nt kui lend on täis, valida teine kuupäev).
- **Rakendamine**: Sageli kasutatakse "Planeerija" agenti, mis genereerib struktureeritud plaani (nt JSON), mida siis teised agendid täidavad.

## 4. Disainipõhimõtted

Agentide loomisel tuleks arvestada kolme mõõtmega:
- **Ruum**: Agendid peaksid ühendama inimesi ja teadmisi, olema ligipääsetavad, aga mitte pealetükkivad.
- **Aeg**: Agendid peaksid õppima *minevikust*, pakkuma asjakohaseid viiteid *praeguses* ning kohanema *tuleviku* jaoks.
- **Tuumik**: Võtta omaks ebakindlus, kuid rajada usaldus läbipaistvuse ja kasutajapoolse kontrolli kaudu.

## 5. Peamiste Õppetundide Kokkuvõte

- **Õppetund 1**: Agendid on süsteemid, mitte ainult mudelid. Nad tajuvad, arutlevad ja tegutsevad.
- **Õppetund 2**: Raamistikud nagu Semantic Kernel ja AutoGen varjavad tööriistakutsumise ja olekuhalduse keerukust.
- **Õppetund 3**: Disaini läbipaistvust ja kasutajakontrolli silmas pidades.
- **Õppetund 4**: Tööriistad on agendi "käed". Skeemi määratlus on LLM-ile hädavajalik tööriistade kasutamise mõistmiseks.
- **Õppetund 7**: Planeerimine on agendi "juhtimisfunktsioon", mis võimaldab toime tulla keerukate töövoogudega.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun pidage meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->