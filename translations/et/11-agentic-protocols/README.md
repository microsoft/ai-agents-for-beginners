# Agendi protokollide kasutamine (MCP, A2A ja NLWeb)

[![Agentic Protocols](../../../translated_images/et/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klõpsa ülaloleval pildil, et vaadata selle tunni videot)_

Nagu AI agentide kasutamine kasvab, suureneb ka vajadus protokollide järele, mis tagavad standardiseerimise, turvalisuse ja toetavad avatud innovatsiooni. Selles tunnis käsitleme kolme protokolli, mis püüavad seda vajadust rahuldada – Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Sissejuhatus

Selles tunnis käsitleme:

• Kuidas **MCP** võimaldab AI agentidel ligipääsu välistele tööriistadele ja andmetele kasutaja ülesannete täitmiseks.

• Kuidas **A2A** võimaldab erinevate AI agentide vahel suhtlust ja koostööd.

• Kuidas **NLWeb** toob loomuliku keele liidesed igale veebisaidile, võimaldades AI agentidel sisu avastada ja sellega suhelda.

## Õpieesmärgid

• **Tuvastada** MCP, A2A ja NLWeb põhieesmärgid ja eelised AI agentide kontekstis.

• **Selgitada**, kuidas iga protokoll hõlbustab suhtlust ja koostööd LLM-ide, tööriistade ja teiste agentide vahel.

• **Tunda ära** iga protokolli erinevad rollid keeruliste agentide süsteemide loomisel.

## Model Context Protocol

**Model Context Protocol (MCP)** on avatud standard, mis pakub standardiseeritud viisi, kuidas rakendused saavad anda konteksti ja tööriistu LLM-idele. See võimaldab "universaalset adapterit" erinevatele andmeallikatele ja tööriistadele, millega AI agentid saavad järjepidevalt ühendada.

Vaadakem MCP komponente, eeliseid võrreldes otsese API kasutamisega ning näidet, kuidas AI agentid MCP serverit kasutavad.

### MCP põhikomponendid

MCP töötab **klient-serveri arhitektuuril** ning põhikomponendid on:

• **Hostid** on LLM-rakendused (näiteks koodiredaktor nagu VSCode), mis alustavad ühendusi MCP serveriga.

• **Kliendid** on komponendid host-rakenduses, mis hoiavad ühe-ühele ühendusi serveritega.

• **Serverid** on kerged programmid, mis pakuvad kindlaid võimekusi.

Protokolli kuuluvad kolm põhialust, mis on MCP serveri võimekused:

• **Tööriistad**: Need on üksikud tegevused või funktsioonid, mida AI agent saab kutsuda mingi toimingu tegemiseks. Näiteks ilmateenus võib pakkuda "saada ilm" tööriista või e-kaubanduse server "osta toode" tööriista. MCP serverid reklaamivad iga tööriista nime, kirjeldust ja sisendi/väljundi skeemi oma võimekuste nimekirjas.

• **Ressursid**: Need on ainult lugemiseks mõeldud andmeobjektid või dokumendid, mida MCP server saab pakkuda ja kliendid saavad neid vajadusel pärida. Näideteks on failide sisu, andmebaasi kirjed või logifailid. Ressursid võivad olla tekstipõhised (näiteks kood või JSON) või binaarsed (näiteks pildid või PDF-id).

• **Juhised**: Need on ette määratud mallid, mis pakuvad soovitatud juhiseid, võimaldades keerukamaid töövooge.

### MCP eelised

MCP pakub AI agentidele olulisi eeliseid:

• **Dünaamiline tööriistade avastamine**: Agentidel on võimalik dünaamiliselt saada serverilt nimekiri kättesaadavatest tööriistadest koos nende kirjeldustega. See erineb traditsioonilistest API-dest, mis sageli nõuavad staatilist kodeerimist integratsioonide loomiseks ja iga API muudatus nõuab koodi uuendamist. MCP pakub "integreeri üks kord" lähenemist, mis toob kaasa suurema kohanemisvõime.

• **Ühilduvus erinevate LLM-idega**: MCP töötab erinevate LLM-idega, pakkudes paindlikkust vahetada põhimudeleid parema jõudluse saavutamiseks.

• **Standardiseeritud turvalisus**: MCP sisaldab standardset autentimismeetodit, mis parandab võrreldavust uute MCP serverite juurdevõtmisel. See on lihtsam kui erinevate traditsiooniliste API-de jaoks erinevate võtmete ja autentimistüüpide haldamine.

### MCP näide

![MCP Diagram](../../../translated_images/et/mcp-diagram.e4ca1cbd551444a1.webp)

Kujutleme kasutajat, kes soovib MCP toel töötava AI assistendi abil lennupileti broneerida.

1. **Ühendus**: AI assistent (MCP klient) ühendub lennufirma MCP serveriga.

2. **Tööriistade avastamine**: Klient küsib lennufirma MCP serverilt: "Milliseid tööriistu teil on?" Server vastab tööriistadega nagu "otsi lende" ja "broneeri lend".

3. **Tööriista kutsumine**: Kasutaja ütleb AI assistendile: "Palun otsi lendu Portlandist Honolulu." AI assistent kasutab oma LLM-i ja tuvastab, et peab kutsuma "otsi lende" tööriista ning edastab MCP serverile vastavad parameetrid (lähtekoht, sihtkoht).

4. **Täitmine ja vastus**: MCP server, toimides ümbrisena, teeb tegeliku kutsumise lennufirma sise-broneerimis-API-le. Samuti saab ta lennuinfo (näiteks JSON-formaadis) ja edastab selle AI assistendile.

5. **Edasine suhtlus**: AI assistent esitab lennuvalikud. Kui kasutaja valib lennu, võib assistent kutsuda sama MCP serveri "broneeri lend" tööriista, lõpetades broneeringu.

## Agent-to-Agent protokoll (A2A)

Kui MCP keskendub LLM-ide ühendamisele tööriistadega, siis **Agent-to-Agent (A2A) protokoll** läheb samm edasi, võimaldades erinevate AI agentide vahelist suhtlust ja koostööd. A2A ühendab AI agendid erinevatest organisatsioonidest, keskkondadest ja tehnoloogiatest, et koos täita ühine ülesanne.

Vaadeldakse A2A komponente ja eeliseid ning näidet, kuidas seda meie reisirakenduses rakendada.

### A2A põhikomponendid

A2A võimaldab agentidevahelist suhtlust ja koostööd, et täita kasutaja alamosa. Iga protokolli komponent aitab selles:

#### Agentkaart

Sarnaselt MCP serveri tööriistade nimekirjale sisaldab Agentkaart:

- Agendi nimi.

- **üldiste ülesannete kirjeldus**, mida ta täidab.

- **spetsiifiliste oskuste nimekiri** koos kirjeldustega, mis aitab teistel agentidel (või isegi inimestel) mõista, millal ja miks seda agenti kutsuda.

- Agendi **praegune lõpp-punkti URL**.

- Agendi **versioon** ja **võimekused** nagu näiteks voogedastus vastustele ja push-teavitused.

#### Agentijooksutaja

Agentijooksutaja vastutab **kasutaja vestluse konteksti edastamise eest kaugarendile**, kes vajab seda ülesande mõistmiseks. A2A serveris kasutab agent oma suurt keelemudelit (LLM) sissetulevate taotluste analüüsimiseks ja ülesannete täitmiseks oma sisemiste tööriistadega.

#### Artefakt

Kui kaugarend on soovitud ülesande lõpetanud, luuakse tema töö tulemusena artefakt. Artefakt **sisaldab agendi töö tulemust**, **täidetud töö kirjeldust** ja **tekstikonteksti**, mis saadetakse protokolli kaudu edasi. Pärast artefakti saatmist suletakse ühendus kaugarendiga kuni järgmise vajaduseni.

#### Sündmuste järjekord

See komponent haldab **uuendusi ja sõnumite edastamist**. See on eriti oluline tootmiskeskkonnale agentide süsteemides, et vältida ühenduse sulgumist ülesande lõpetamise ajal, eriti kui ülesande täitmine võib võtta aega.

### A2A eelised

• **Tõhustatud koostöö**: Võimaldab erinevate tootjate ja platvormide agendid suhelda, jagada konteksti ja töötada koos, hõlbustades sujuvat automatiseerimist traditsiooniliselt lahusolevate süsteemide vahel.

• **Mudeli valiku paindlikkus**: Iga A2A agent otsustab ise, millist LLM-i oma teenuste pakkumiseks kasutada, võimaldades optimeeritud või peenhäälestatud mudeleid iga agendi jaoks, erinevalt ühest LLM-ühendusest MCP olukordades.

• **Integreeritud autentimine**: Autentimine on otse A2A protokolli integreeritud, pakkudes tugevat turvafraami agentide suhtluseks.

### A2A näide

![A2A Diagram](../../../translated_images/et/A2A-Diagram.8666928d648acc26.webp)

Laiendame meie reisibroneerimise stsenaariumi A2A-ga.

1. **Kasutaja taotlus mitme agendi poole**: Kasutaja suhtleb "Reisiagendi" A2A kliendi/agendiga, näiteks paludes: "Palun broneeri kogu reis Honolulusse järgmiseks nädalaks, kaasa arvatud lennud, hotell ja rendiauto."

2. **Reisiagendi korraldus**: Reisiagent saab selle keeruka taotluse, kasutab oma LLM-i ülesande analüüsimiseks ja otsustab, et peab suhtlema teiste spetsialiseeritud agentidega.

3. **Agentidevaheline suhtlus**: Reisiagent kasutab A2A protokolli ühendamiseks järgmiste agentidega, näiteks "Lennufirma agent", "Hotelli agent" ja "Autolennu agent", mis on loodud erinevate firmade poolt.

4. **Delegeeritud töö täitmine**: Reisiagent saadab konkreetseid ülesandeid spetsialiseeritud agentidele (nt "Leia lennud Honolulusse", "Broneeri hotell", "Rendi auto"). Iga agent, oma LLM-iga ja oma tööriistu kasutades (milleks võivad olla ka MCP serverid), täidab oma osa broneeringust.

5. **Koondatud vastus**: Kui kõik allagentsed on ülesanded lõpetanud, koondab Reisiagent tulemused (lennuandmed, hotelli kinnitus, auto broneering) ja edastab kasutajale vestluse stiilis vastuse.

## Loomuliku keele veeb (NLWeb)

Veebisaidid on juba pikka aega olnud peamine viis kasutajate ligipääsuks internetis olevatele andmetele ja teabele.

Vaatame NLWeb erinevaid komponente, NLWeb eeliseid ja näidet meie reisirakenduse põhjal.

### NLWeb komponendid

- **NLWeb rakendus (põhiteenus)**: Süsteem, mis töötleb loomuliku keele küsimusi. See ühendab platvormi erinevad osad, et vastuseid luua. Seda võib pidada veebisaidi loomuliku keele funktsioonide **mootoriks**.

- **NLWeb protokoll**: On **lihtsate reeglite kogum loomuliku keele suhtluseks** veebisaidiga. Tagastab vastused JSON-formaadis (tihti kasutades Schema.org). Selle eesmärk on luua lihtne alus "AI veebile", samamoodi nagu HTML tegi võimalikuks dokumentide jagamise veebis.

- **MCP server (Model Context Protocol lõpp-punkt)**: Iga NLWeb seade töötab ka **MCP serverina**. See tähendab, et ta saab **jagada tööriistu (nt "küsige" meetod) ja andmeid** teiste AI süsteemidega. See teeb veebisaidi sisu ja võimekused AI agentide jaoks kasutatavaks, võimaldades saidil saada osaks laiemast "agendisüsteemist".

- **Embedingu mudelid**: Need mudelid teisendavad veebisisu numbrilisteks esitluseks ehk vektoriteks (embeddinguteks). Need vektorid haaravad tähenduse viisil, mida arvutid saavad võrrelda ja otsida. Need salvestatakse spetsiaalsesse andmebaasi ning kasutajad saavad valida, millist embedingu mudelit kasutada.

- **Vektori andmebaas (otsingumehhanism)**: See andmebaas **salvestab veebisaidi sisu embeddinguid**. Kui keegi esitab küsimuse, otsib NLWeb kiiresti vektoriandmebaasist kõige asjakohasemaid vastuseid. See pakub kiiret võimalikust vastusest koos vastavushinnanguga. NLWeb töötab erinevate vektoriandmebaasidega nagu Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb näide

![NLWeb](../../../translated_images/et/nlweb-diagram.c1e2390b310e5fe4.webp)

Võtame taas meie reisibroneerimise veebilehe, mis on seekord NLWeb-i toega.

1. **Andmete sissetoomine**: Reisiveebisaidi olemasolevaid tootekatalooge (nt lennunimekirjad, hotellikirjeldused, ekskursioonipaketid) vormistatakse Schema.org abil või tuuakse sisendina RSS-voogudena. NLWeb tööriistad töötlevad neid struktuurandmeid, loovad embeddingud ja salvestavad need lokaalsesse või kaugvektorandmebaasi.

2. **Loomuliku keele päring (inimene)**: Kasutaja külastab veebilehte ja menüüde üles otsimise asemel tippib vestluse liidesesse: "Leia mulle peresõbralik hotell Honolulus basseiniga järgmiseks nädalaks".

3. **NLWeb töötlemine**: NLWeb rakendus saab päringu, saadab selle mõistmiseks LLM-ile ja otsib samal ajal oma vektoriandmebaasist asjakohaseid hotellipakkumisi.

4. **Täpne tulemus**: LLM aitab tõlgendada andmebaasist otsitud tulemusi, valida parimad vastavused kriteeriumite "peresõbralik", "bassein" ja "Honolulu" alusel ning vormistab loomulikus keeles vastuse. Väga oluline on see, et vastus viitab tegelikele hotellidele veebisaidi kataloogist, vältides väljamõeldud infot.

5. **AI agendi interaktsioon**: Kuna NLWeb toimib MCP serverina, võib välise AI reisagent ühenduda selle veebilehe NLWeb eksemplariga. AI agent saab seejärel kasutada MCP meetodit `ask`, et otse veebilehte küsitleda: `ask("Kas hotelli poolt soovitatakse vegan-sõbralikke restorane Honolulu piirkonnas?")`. NLWeb töötleb selle, kasutades oma restoraniandmebaasi (kui see on laetud) ja tagastab struktureeritud JSON-vastuse.

### Kas on veel küsimusi MCP/A2A/NLWeb kohta?

Liitu [Microsoft Foundry Discordiga](https://aka.ms/ai-agents/discord), et kohtuda teiste õppijatega, osaleda küsitundides ja saada vastused AI agentide teemal.

## Ressursid

- [MCP algajatele](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentatsioon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb hoidla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud AI-tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüdleme täpsuse poole, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleb pidada autoriteetseks allikaks. Tähtsa info puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste ega eksituste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->