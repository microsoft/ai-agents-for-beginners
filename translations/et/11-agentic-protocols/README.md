# Agentide protokollide kasutamine (MCP, A2A ja NLWeb)

[![Agentide protokollid](../../../translated_images/et/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klõpsa ülal olevale pildile, et vaadata selle loengu videot)_

AI agentide kasutamise kasvades suureneb ka vajadus protokollide järele, mis tagavad standardimise, turvalisuse ja toetavad avatud innovatsiooni. Selles loengus käsitleme kolme protokolli, mis püüavad neid vajadusi rahuldada - Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Sissejuhatus

Selles loengus käsitleme:

• Kuidas **MCP** võimaldab AI agentidel pääseda ligi välistele tööriistadele ja andmetele, et täita kasutaja ülesandeid.

• Kuidas **A2A** võimaldab eri AI agentide vahel suhtlemist ja koostööd.

• Kuidas **NLWeb** toob loomuliku keele liidesed ükskõik millisele veebisaidile, võimaldades AI agentidel avastada ja suhelda selle sisuga.

## Õpieesmärgid

• **Tuletada** MCP, A2A ja NLWebi põhiline eesmärk ja kasu AI agentide kontekstis.

• **Selgitada**, kuidas iga protokoll hõlbustab suhtlust ja interaktsiooni LLMide, tööriistade ja teiste agentide vahel.

• **Tuvastada** iga protokolli erinevad rollid keerukate agentide süsteemide ehitamisel.

## Model Context Protocol

**Model Context Protocol (MCP)** on avatud standard, mis pakub standardiseeritud viisi rakendustele pakkuda konteksti ja tööriistu LLMidele. See võimaldab "universaalset adapterit" erinevatele andmeallikatele ja tööriistadele, millega AI agentidel on võimalik ühenduda ühtsel viisil.

Vaatame MCP komponente, eeliseid võrreldes otse API kasutamisega ning näite, kuidas AI agent võib MCP serverit kasutada.

### MCP põhikomponendid

MCP toimib **klient-server arhitektuuril** ning põhikomponendid on:

• **Hostid** on LLM rakendused (näiteks koodiredaktor nagu VSCode), mis alustavad ühendusi MCP serveriga.

• **Kliendid** on hostrakenduse komponendid, mis hoiavad välja üks-ühele ühendusi serveritega.

• **Serverid** on kergekaalulised programmid, mis pakuvad konkreetseid võimeid.

Protokolli hulka kuuluvad kolm põhialust, mis on MCP serveri võimed:

• **Tööriistad**: Need on eraldi toimingud või funktsioonid, mida AI agent saab kutsuda toimingu tegemiseks. Näiteks ilmaprognoosi teenus võib pakkuda "saada ilm" tööriista või e-kaubanduse server võib pakkuda "toote ostmise" tööriista. MCP serverid kuulutavad iga tööriista nime, kirjelduse ja sisendi/väljundi skeemi oma võimete nimekirjas.

• **Ressursid**: Need on ainult lugemiseks mõeldud andmeelemendid või dokumendid, mida MCP server saab pakkuda ning mida kliendid saavad nõudmisel pärida. Näiteks failisisud, andmebaasi kirjed või logifailid. Ressursid võivad olla tekstid (nagu kood või JSON) või binaarsed (nagu pildid või PDF-dokumendid).

• **Viited**: Need on eelmääratletud mallid, mis pakuvad soovitatud sisendeid, võimaldades keerukamaid töövooge.

### MCP eelised

MCP pakub AI agentidele märkimisväärseid eeliseid:

• **Dünaamiline tööriistade avastamine**: Agentidel on võimalik dünaamiliselt saada nimekiri serveris saadaval olevatest tööriistadest koos nende kirjeldustega. See erineb traditsioonilistest API-dest, mis sageli nõuavad integreerimiseks staatilist kodeerimist ning iga API muudatus eeldab koodi uuendamist. MCP pakub "ühekordset integreerimist", mis viib suurema kohanemisvõimeni.

• **Ühilduvus erinevate LLMidega**: MCP töötab erinevate LLMidega, andes paindlikkuse põhimudelid välja vahetada parema jõudluse saavutamiseks.

• **Standardiseeritud turvalisus**: MCP sisaldab standardset autentimisviisi, mis parandab skaleeritavust lisades juurdepääsu täiendavatele MCP serveritele. See on lihtsam kui hallata erinevaid võtmeid ja autentimismeetodeid erinevate traditsiooniliste APIde jaoks.

### MCP näide

![MCP skeem](../../../translated_images/et/mcp-diagram.e4ca1cbd551444a1.webp)

Kujutame ette, et kasutaja soovib broneerida lendu AI assistendi abil, mida toetab MCP.

1. **Ühendus**: AI assistent (MCP klient) ühendub lennufirma poolt pakutava MCP serveriga.

2. **Tööriistade avastamine**: Klient küsib lennufirma MCP serverilt: „Millised tööriistad teil saadaval on?“ Server vastab tööriistadega nagu "lendude otsing" ja "lendude broneerimine".

3. **Tööriista kutsumine**: Seejärel küsid AI assistendilt: „Palun otsi lendu Portlandist Honolulusse.“ AI assistent, kasutades oma LLMi, tuvastab, et peab kutsuma tööriista "lendude otsing" ja edastab MCP serverile asjakohased parameetrid (lähtkoht, sihtkoht).

4. **Täideviimine ja vastus**: MCP server, tegutsedes vahendajana, teeb tegeliku kõne lennufirma sisemaisele broneerimis-API-le. Seejärel saab lendude info (nt JSON-andmed) ja saadab selle tagasi AI assistendile.

5. **Edasine suhtlus**: AI assistent esitab lennuvalikud. Kui valid lennu, võib assistent kutsuda sama MCP serveri tööriista "lendude broneerimine" ja lõpule viia broneerimise.

## Agent-to-Agent protokoll (A2A)

MCP keskendub LLMide ühendamisele tööriistadega, kuid **Agent-to-Agent (A2A) protokoll** läheb sammu kaugemale, võimaldades erinevate AI agentide vahel suhtlust ja koostööd. A2A ühendab AI agendid erinevate organisatsioonide, keskkondade ja tehnoloogiliste platvormide vahel ühise ülesande täitmiseks.

Vaatleme A2A komponente ja eeliseid ning ka näidet, kuidas seda võiks rakendada meie reisis rakenduses.

### A2A põhikomponendid

A2A keskendub agentide vahelise suhtluse võimaldamisele ja koostööle kasutaja alamülesande täitmisel. Iga protokolli komponent aitab seda saavutada:

#### Agendi kaart

Nii nagu MCP server jagab tööriistade nimekirja, sisaldab Agendi kaart:
- Agendi nimi.
- Üldiste ülesannete kirjeldus, mida agent täidab.
- Spetsiifiliste oskuste nimekiri kirjeldustega, et aidata teistel agentidel (või isegi inimkasutajatel) mõista, millal ja miks seda agenti kutsuda.
- Agendi **praegune lõpp-punkti URL**.
- Agendi **versioon** ja **võimed**, nagu voogedastuse vastused ja push-teavitused.

#### Agendi täideviija

Agendi täideviija vastutab **kasutajavestluse konteksti edastamise eest kaugagendile**, mida viimane vajab ülesande mõistmiseks ja täitmiseks. A2A serveris kasutab agent oma LLMi, et analüüsida saabuvat päringut ja täita ülesandeid oma sisemiste tööriistade abil.

#### Artefakt

Kui kaugagent on palutud ülesande lõpetanud, luuakse selle töö tulemusena artefakt. Artefakt **sisaldab agendi töö tulemust**, **valmimise kirjeldust** ja **teksti konteksti**, mis saadetakse protokolli kaudu. Pärast artefakti saatmist suletakse ühendus kaugagendiga, kuni seda uuesti vajatakse.

#### Sündmuste järjekord

See komponent hoolitseb **uuenduste haldamise ja sõnumite edastamise eest**. See on tootmiskeskkonnas eriti oluline agentidesüsteemide jaoks, et vältida ühenduse sulgemist agentide vahel enne ülesande lõpetamist, eriti kui ülesande täitmine võtab aega.

### A2A eelised

• **Tõhustatud koostöö**: See võimaldab erinevate müüjate ja platvormide agentidel suhelda, jagada konteksti ja töötada koos, toetades sujuvat automatiseerimist traditsiooniliselt jagamata süsteemide vahel.

• **Mudeli valiku paindlikkus**: Iga A2A agent saab otsustada, millist LLMi ta kasutab, võimaldades optimeeritud või täpsustatud mudeleid iga agendi jaoks, erinevalt mõnest MCP kasutusjuhtumist, kus on üks LLM ühendus.

• **Sisseehitatud autentimine**: Autentimine on otseselt integreeritud A2A protokolli, pakkudes tugevat turvafraamistikku agentide vahelistes interaktsioonides.

### A2A näide

![A2A skeem](../../../translated_images/et/A2A-Diagram.8666928d648acc26.webp)

Laiendame oma reisi broneerimise stsenaariumi, kasutades seekord A2A protokolli.

1. **Kasutaja päring mitme agendi süsteemile**: Kasutaja suhtleb "Reisiagent" A2A kliendi/agendiga, näiteks ütleb: "Palun broneeri terve reis Honolulusse järgmiseks nädalaks, lennud, hotell ja rendiauto."

2. **Reisiagendi orkestreerimine**: Reisiagent saab selle keerulise päringu, kasutab oma LLMi, et ülesannet hinnata ja otsustab suhelda teiste spetsialiseerunud agentidega.

3. **Agentidevaheline suhtlus**: Reisiagent kasutab A2A protokolli, et võtta ühendust alluva tasandi agentidega, nagu "Lennufirma agent," "Hotelli agent" ja "Autorendi agent," kes töötavad erinevates ettevõtetes.

4. **Ülesannete delegeerimine**: Reisiagent saadab spetsiifilised ülesanded neile spetsialiseerunud agentidele (nt „Leia lennud Honolulusse,“ „Broneeri hotell,“ „Rendi auto“). Iga agent kasutab oma LLMi ja tööriistu (mis võivad ise olla MCP serverid) ja täidab oma osa broneerimisest.

5. **Konsolideeritud vastus**: Kui kõik alluvad agentid on oma ülesanded lõpetanud, koostab Reisiagent tulemused (lendude andmed, hotelli kinnitus, autorendi broneering) ja saadab kasutajale kokkuvõtliku vestlusstiilis vastuse.

## Loomuliku keele veebi protokoll (NLWeb)

Veebisaidid on juba pikka aega olnud peamine viis kasutajate jaoks internetis teabe ja andmete juurde pääsemiseks.

Vaatame NLWebi erinevaid komponente, NLWebi eeliseid ja kuidas meie NLWeb töötab, vaadates meie reisi rakendust.

### NLWebi komponendid

- **NLWeb rakendus (põhiteenuse kood)**: Süsteem, mis töötleb loomuliku keele küsimusi. See ühendab platvormi erinevad osad vastuste loomiseks. Seda saab mõelda kui **mootorit, mis toidab veebisaidi loomuliku keele funktsioone**.

- **NLWeb protokoll**: See on **põhiline reeglistik loomuliku keele suhtluseks** veebisaidiga. See saadab vastused JSON-formaadis (tavaliselt kasutades Schema.org). Selle eesmärk on luua lihtne alus "AI veebile", samamoodi nagu HTML võimaldas dokumentide jagamist veebis.

- **MCP server (Model Context Protocol lõpp-punkt)**: Iga NLWeb setup töötab ka kui **MCP server**. See tähendab, et see suudab **jagada tööriistu (nt „küsi“ meetod) ja andmeid** teiste AI süsteemidega. Praktikas teeb see veebisaidi sisu ja võimeid AI agendile kasutatavaks, võimaldades saidil saada osaks laiemast "agendi ökosüsteemist".

- **Manustamismudelid**: Neid mudeleid kasutatakse, et **kujundada veebisaidi sisu numbrilisteks esindusteks ehk vektoriteks (manustusteks)**. Need vektorid haaravad tähenduse viisil, mida arvutid suudavad võrrelda ja otsida. Need salvestatakse spetsiaalsesse andmebaasi, kus kasutajad saavad valida, millist manustusmudelit nad soovivad kasutada.

- **Vektoriandmebaas (päringumehhanism)**: See andmebaas **salvestab veebisaidi sisu manustused**. Kui keegi esitab küsimuse, kontrollib NLWeb kiiresti vektoriandmebaasi, et leida kõige asjakohasem info. See annab kiire nimekirja võimalikest vastustest, mis on järjestatud sarnasuse alusel. NLWeb töötab erinevate vektori salvestussüsteemidega nagu Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb näide

![NLWeb](../../../translated_images/et/nlweb-diagram.c1e2390b310e5fe4.webp)

Võtame taas meie reisi broneerimise veebisaidi, kuid seekord on see toetatud NLWebi poolt.

1. **Andmete vastuvõtt**: Reisi veebisaidi olemasolevad tootekataloogid (nt lennu pakkumised, hotelli kirjelduse, tuuripakettide info) on vormindatud Schema.org vormingus või laaditud RSS voogude kaudu. NLWebi tööriistad vastuvõtavad seda struktureeritud andmestikku, loovad manustused ja salvestavad need kohalikku või kaugvektoriandmebaasi.

2. **Loomuliku keele päring (inimene)**: Kasutaja külastab veebisaiti ja selle asemel, et menüüs navigeerida, kirjutab vestlusliidesesse: „Leia mulle peresõbralik hotell Honolulus koos basseiniga järgmiseks nädalaks“.

3. **NLWebi töötlemine**: NLWebi rakendus saab selle päringu. Saadab selle LLMile mõistmiseks ja samal ajal otsib kiiresti vektoriandmebaasist asjakohaseid hotelli pakkumisi.

4. **Täpsed tulemused**: LLM aitab tõlgendada andmebaasi otsingutulemusi, tuvastab parimad sobivad pakkumised tingimustele „peresõbralik“, „bassein“ ja „Honolulu“ ning vormindab loomulikus keeles vastuse. Oluline on, et vastus viitab tegelikele hotellidele veebisaidi kataloogist, vältides väljamõeldud infot.

5. **AI agendi interaktsioon**: Kuna NLWeb toimib MCP serverina, võiks ka väline AI reisibüroo agent ühendada selle veebisaidi NLWebi instantsiga. AI agent võiks siis kasutada `ask` MCP meetodit, et veebisaidilt otse küsida: `ask("Kas hotell soovitab vegan-sõbralikke restorane Honolulu piirkonnas?")`. NLWeb töödeldes kasutab selle restorani infokogumit (kui see on laetud) ja saadab struktuurse JSON vastuse.

### Kas sul on rohkem küsimusi MCP/A2A/NLWeb kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda virtuaalsel lahtistel tundidel ja saada vastuseid AI agentide küsimustele.

## Ressursid

- [MCP algajatele](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentatsioon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWebi hoidla](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Eelmine loeng

[AI agendid tootmises](../10-ai-agents-production/README.md)

## Järgmine loeng

[Konteksti inseneriteadus AI agentidele](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->