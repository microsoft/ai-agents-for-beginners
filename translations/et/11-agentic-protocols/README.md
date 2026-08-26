# Agentsete protokollide kasutamine (MCP, A2A ja NLWeb)

[![Agentsete protokollide](../../../translated_images/et/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

Kuna tehisintellekti agentide kasutamine kasvab, suureneb ka vajadus protokollide järele, mis tagavad standardiseerimise, turvalisuse ja toetavad avatud innovatsiooni. Selles õppetunnis käsitleme kolme protokolli, mis püüavad seda vajadust täita – Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Sissejuhatus

Selles õppetunnis käsitleme:

• Kuidas **MCP** võimaldab tehisintellekti agentidel juurde pääseda välistele tööriistadele ja andmetele kasutaja ülesannete täitmiseks.

• Kuidas **A2A** võimaldab eri tehisintellekti agentidel suhelda ja koostööd teha.

• Kuidas **NLWeb** toob loomuliku keele liidestused igale veebisaidile, võimaldades tehisintellekti agentidel sisu avastada ja sellega suhelda.

## Õpieesmärgid

• **Määratlema** MCP, A2A ja NLWebi põhieesmärgid ja eelised tehisintellekti agentide kontekstis.

• **Selgitama**, kuidas iga protokoll hõlbustab LLM-ide, tööriistade ja teiste agentide vahelist suhtlust ja suhtlust.

• **Tuvastama** iga protokolli erinevad rollid keerukate agentsete süsteemide loomisel.

## Model Context Protocol

**Model Context Protocol (MCP)** on avatud standard, mis tagab rakendustele standardiseeritud viisi konteksti ja tööriistade pakkumiseks LLM-idele. See võimaldab "universaalse adapteri" erinevatele andmeallikatele ja tööriistadele, millega tehisintellekti agentidel on võimalik järjekindlalt ühenduda.

Vaatame MCP komponente, eeliseid võrreldes otsepõhise API kasutamisega ja näidet, kuidas tehisintellekti agent võiks MCP serverit kasutada.

### MCP põhikomponendid

MCP töötab **klient-serveri arhitektuuril** ja põhikomponendid on:

• **Hostid** on LLM-rakendused (näiteks koodiredaktor nagu VSCode), mis alustavad ühendusi MCP serveriga.

• **Kliendid** on hostrakenduse komponendid, mis hoiavad ühetahulisi ühendusi serveritega.

• **Serverid** on kerged programmid, mis avaldavad konkreetseid võimalusi.

Protokoll sisaldab kolme põhifunktsiooni, mis on MCP serveri võimed:

• **Tööriistad**: Need on eraldiseisvad toimingud või funktsioonid, mida tehisintellekti agent saab teha. Näiteks võib ilmaportaal avaldada "saada ilm" tööriista või e-kaubanduse server "osta toode" tööriista. MCP serverid reklaamivad iga tööriista nime, kirjelduse ja sisendi/väljundi skeemi oma võimete nimekirjas.

• **Ressursid**: Need on ainult lugemiseks mõeldud andmeüksused või dokumendid, mida MCP server saab pakkuda ning kliendid neid nõudmisel kätte saada. Näideteks on failide sisu, andmebaasi kirjed või logifailid. Ressursid võivad olla tekst (näiteks kood või JSON) või binaarfailid (näiteks pildid või PDF-id).

• **Päringumallid**: Need on eelmääratud mallid, mis pakuvad soovitatud päringuid keerulisemate töövoogude loomiseks.

### MCP eelised

MCP pakub tehisintellekti agentidele märkimisväärseid eeliseid:

• **Dünaamiline tööriistade avastamine**: Agentidel on võimalik serverist dünaamiliselt saada nimekiri saadaolevatest tööriistadest koos seletustega, mida need teevad. See erineb traditsioonilistest API-dest, mis tihti nõuavad staatilist kodeerimist integratsioonide jaoks ja iga API muutus nõuab koodi uuendamist. MCP pakub "integreeri üks kord" lähenemisviisi, mis suurendab kohanemisvõimet.

• **Koostalitlusvõime eri LLM-idega**: MCP töötab erinevate LLM-idega, andes paindlikkuse vahetada põhimalle parema jõudluse saavutamiseks.

• **Standardiseeritud turvalisus**: MCP sisaldab standardset autentimismeetodit, mis parandab skaleeritavust uute MCP serverite ligipääsu lisamisel. See on lihtsam kui hallata erinevaid võtmeid ja autentimistüüpe traditsiooniliste API-de puhul.

### MCP näide

![MCP Diagram](../../../translated_images/et/mcp-diagram.e4ca1cbd551444a1.webp)

Kujutame ette, et kasutaja soovib lennupiletit broneerida tehisintellekti assistendi abil, mis töötab MCP toel.

1. **Ühendus**: Tehisintellekti assistent (MCP klient) ühendub lennufirma pakutava MCP serveriga.

2. **Tööriistade avastamine**: Klient küsib lennufirma MCP serverilt: "Millised tööriistad teil saadaval on?" Server vastab tööriistadega nagu "otsi lende" ja "broneeri lend".

3. **Tööriista kutsumine**: Seejärel ütled tehisintellekti assistendile: "Palun otsi lendu Portlandist Honolulu suunas." AI assistent, kasutades oma LLM-i, tuvastab, et peab kutsuma "otsi lende" tööriista ja edastab vastavad parameetrid (lähtekoht, sihtkoht) MCP serverile.

4. **Täitmine ja vastus**: MCP server, toimides kui ümbris, teeb päris API-kutse lennufirma sisemisele broneerimissüsteemile. Seejärel saab lennuinfo (nt JSON-andmed) ja saadab selle tagasi AI assistendile.

5. **Edasine suhtlus**: AI assistent esitab lennuvalikud. Kui valid lennu, võib assistent kutsuda sama MCP serveri "broneeri lend" tööriista, lõpetades broneeringu.

## Agent Agentile protokoll (A2A)

Kui MCP keskendub LLM-ide ühendamisele tööriistadega, siis **Agent Agentile (A2A) protokoll** viib selle samm edasi, võimaldades eri tehisintellekti agentide vahel suhtlust ja koostööd. A2A ühendab tehisintellekti agente eri organisatsioonide, keskkondade ja tehnoloogiliste platvormide vahel ühisülesande täitmiseks.

Vaatame A2A komponente ja eeliseid ning näidet, kuidas seda võiks rakendada meie reisiäpiga.

### A2A põhikomponendid

A2A võimaldab agentide vahel suhelda ja teha koostööd kasutaja alamülesande täitmiseks. Protokolli iga komponent aitab selles kaasa:

#### Agendi kaart

Nagu MCP server jagab tööriistade nimekirja, sisaldab Agendi kaart:
- Agendi nime.
- **üldiste ülesannete kirjeldus**, mida see täidab.
- **spetsiifiliste oskuste nimekiri** koos kirjeldustega, et aidata teisi agente (või isegi inimesi) mõista, millal ja miks seda agenti kutsuda.
- Agendi **praegune lõpp-punkti URL**.
- Agendi **versioon** ja **võimalused**, näiteks voogedastusega vastused ja push-teavitused.

#### Agendi täitja

Agendi täitja vastutab **kasutaja vestluse konteksti edastamise eest kaugagentile**, kuna kaugagent vajab seda ülesande mõistmiseks. A2A serveris kasutab agent oma enda suuri keelemudeleid (LLM) saabuvate päringute analüüsimiseks ja ülesannete täitmiseks oma sisemiste tööriistade abil.

#### Artefakt

Kui kaugagent on soovitud ülesande täitnud, luuakse tema töö tulemusena artefakt. Artefakt **sisaldab agendi töö tulemust**, **kinnitust, mis täideti**, ja **teksti konteksti**, mis saadetakse protokolli kaudu. Pärast artefakti saatmist suletakse ühendus kaugagentiga kuni järgmise korrani.

#### Sündmuste järjekord

Seda komponenti kasutatakse **uuenduste haldamiseks ja sõnumite edastamiseks**. See on eriti oluline agentsete süsteemide tootmiskeskkonnas, et vältida ühenduse sulgumist enne, kui ülesanne on täielikult lõpetatud, eriti kui ülesande täitmine võib võtta kauem aega.

### A2A eelised

• **Täiustatud koostöö**: Võimaldab eri tarnijate ja platvormide agente suhelda, jagada konteksti ja töötada koos, hõlbustades sujuvat automatiseerimist traditsiooniliselt eraldatud süsteemide vahel.

• **Mudeli valiku paindlikkus**: Iga A2A agent saab valida, millist LLM-i ta oma päringute teenindamiseks kasutab, võimaldades optimeeritud või peenhäälestatud mudeleid iga agendi jaoks, erinevalt ühest LLM ühendusest mõnes MCP stsenaariumis.

• **Sisseehitatud autentimine**: Autentimine on otse A2A protokolli integreeritud, pakkudes tugevat turvafraami agendisuhtlusteks.

### A2A näide

![A2A Diagram](../../../translated_images/et/A2A-Diagram.8666928d648acc26.webp)

Laiendame oma reisibroneerimise stsenaariumi, kuid seekord kasutades A2A-d.

1. **Kasutaja päring mitme agendile**: Kasutaja suhtleb "reisibüroo" A2A kliendi/agendiga, näiteks ütlevalt: "Palun broneeri terve reis Honolulu järgmiseks nädalaks, kaasa arvatud lennud, hotell ja rendiauto".

2. **Reisibüroo orkestreerimine**: Reisibüroo saab selle keeruka päringu. See kasutab oma LLM-i ülesande mõistmiseks ja otsustab, et peab suhtlema teiste spetsialiseeritud agentidega.

3. **Agentidevaheline suhtlus**: Reisibüroo kasutab A2A protokolli ühenduseks alluvate agentidega, näiteks "lennufirma agent", "hotelli agent" ja "rendiautode agent", kes on loodud erinevate ettevõtete poolt.

4. **Delegeeritud ülesande täitmine**: Reisibüroo saadab konkreetseid ülesandeid neile spetsialiseeritud agentidele (nt "Leia lennud Honolulu", "Broneeri hotell", "Renta auto"). Iga neist spetsialiseerunud agentidest, kasutades oma LLM-i ja enda tööriistu (mis võivad ise olla MCP serverid), täidab oma osa broneeringust.

5. **Konsolideeritud vastus**: Kui kõik alluvas olekus agentid saavad ülesanded täidetud, koostab Reisibüroo tulemused (lennuandmed, hotelli kinnitus, rendiauto broneering) ja saadab kasutajale põhjaliku vestlusstiilis vastuse.

## Natural Language Web (NLWeb)

Veebisaidid on kaua olnud peamine viis, kuidas kasutajad pääsevad internetis teabele ja andmetele ligi.

Vaatame NLWeb erinevaid komponente, selle eeliseid ja näidet, kuidas meie NLWeb töötab, vaadates meie reisiäppi.

### NLWeb komponendid

- **NLWeb rakendus (tuumikteenuse kood)**: Süsteem, mis töötleb loomulikus keeles esitatud küsimusi. See ühendab platvormi eri osad vastuste loomiseks. Seda võib mõelda kui **mootorina, mis juhib veebisaidi loomuliku keele funktsioone**.

- **NLWeb protokoll**: See on **aluspõhimõtete kogum loomuliku keele interaktsiooniks** veebisaidiga. See saadab vastused tagasi JSON-formaadis (tihti kasutades Schema.org-i). Selle eesmärk on luua lihtne alus "tehisintellekti veebile", samamoodi nagu HTML võimaldas dokumente veebis jagada.

- **MCP server (Model Context Protocol lõpp-punkt)**: Iga NLWeb seadistus töötab ka kui **MCP server**. See tähendab, et see suudab **jagada tööriistu (näiteks "küsi" meetod) ja andmeid** teiste tehisintellekti süsteemidega. Praktikas muudab see veebisaidi sisu ja võimed tehisintellekti agentidele kasutatavaks, võimaldades saidil saada osa laiemast "agentide ökosüsteemist".

- **Embedding mudelid**: Neid mudeleid kasutatakse, et **muuta veebisaidi sisu arvulisteks esitluseks ehk vektoriteks (embeddinguteks)**. Need vektorid võtab tähenduse viisil, mida arvutid saavad võrrelda ja otsida. Need salvestatakse spetsiaalsesse andmebaasi ning kasutajad saavad valida, millist embedding mudelit nad soovivad kasutada.

- **Vektorandmebaas (otsingumehhanism)**: See andmebaas **salvestab veebisaidi sisu embeddingud**. Kui keegi küsib küsimust, kontrollib NLWeb vektorandmebaasi, et kiiresti leida kõige asjakohasem teave. See annab kiire nimekirja võimalikest vastustest, järjestades need sarnasuse alusel. NLWeb töötab erinevate vektorandmebaaside süsteemidega nagu Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb näide

![NLWeb](../../../translated_images/et/nlweb-diagram.c1e2390b310e5fe4.webp)

Mõtleme veelkord meie reisi broneerimise veebisaidile, kuid seekord, kui see töötab NLWebi toel.

1. **Andmete sisestamine**: reisiveebisaidi olemasolevad tootekataloogid (nt lendude nimekirjad, hotelli kirjeldused, tuuripaketid) vormindatakse Schema.org abil või laaditakse RSS voogude kaudu. NLWebi tööriistad võtavad selle struktureeritud andmestiku vastu, loovad embeddingud ja salvestavad need kohalikku või kaugvektorandmebaasi.

2. **Loomuliku keele päring (inimene)**: Kasutaja külastab veebisaiti ning menüüde asemel tippib vestlusliidesesse: "Leia mulle peresõbralik hotell Honolulu lähedal basseiniga järgmiseks nädalaks."

3. **NLWeb töötlemine**: NLWebi rakendus võtab selle päringu vastu. Ta saadab päringu LLM-ile mõistmiseks ja samaaegselt otsib oma vektorandmebaasist asjakohaseid hotelli kirjeid.

4. **Täpsemad tulemused**: LLM aitab tõlgendada andmebaasi otsingutulemusi, tuvastada parimad vasteid "peresõbralik", "bassein" ja "Honolulu" tingimuste järgi ning vormindada loomulikus keeles vastust. Oluline on, et vastus viitab veebisaidi kataloogis olevatele tõelistele hotellidele, vältides väljamõeldud infot.

5. **AI agendi interaktsioon**: Kuna NLWeb toimib MCP serverina, võib ka väline tehisintellekti reisibüroo agent ühenduda selle veebisaidi NLWebi instantsiga. AI agent saab siis direktiivselt pärida veebilehte MCP `ask` meetodi kaudu: `ask("Kas hotell soovitab mõnda vegansõbralikku restorani Honolulu piirkonnas?")`. NLWeb töötleb selle, kasutades oma restoraniinfoga andmebaasi (kui see on laetud), ja tagastab struktureeritud JSON vastuse.

### Kas sul on rohkem küsimusi MCP/A2A/NLWeb kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda konsultatsioonitundides ja saada vastuseid oma tehisintellekti agentide küsimustele.

## Ressursid

- [MCP algajatele](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentatsioon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb hoidla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Eelmine õppetund

[Tehisintellekti agendid tootmises](../10-ai-agents-production/README.md)

## Järgmine õppetund

[Konteksti inseneriteadus tehisintellekti agentide jaoks](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->