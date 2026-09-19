# Agentsete protokollide kasutamine (MCP, A2A ja NLWeb)

[![Agentsete protokollide](../../../translated_images/et/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

Kuna AI agente kasutatakse järjest enam, suureneb ka vajadus protokollide järele, mis tagavad standardimise, turvalisuse ning toetavad avatud innovatsiooni. Selles õppetunnis käsitleme kolme protokolli, mis püüavad sellele vajadusele vastata – Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Sissejuhatus

Selles õppetunnis käsitleme:

• Kuidas **MCP** võimaldab AI agentidel ligi pääseda välistele tööriistadele ja andmetele, et täita kasutaja ülesandeid.

• Kuidas **A2A** võimaldab erinevate AI agentide omavahelist suhtlust ja koostööd.

• Kuidas **NLWeb** toob loomuliku keele liidesed mis tahes veebisaidile, võimaldades AI agentidel sisu avastada ja sellega suhelda.

## Õpieesmärgid

• **Tuletada meelde** MCP, A2A ja NLWeb põhieesmärk ja eelised AI agentide kontekstis.

• **Selgitada**, kuidas iga protokoll hõlbustab kommunikatsiooni ja suhtlust LLM-ide, tööriistade ja teiste agentide vahel.

• **Tuvastada** iga protokolli eraldi rollid keerukate agentsete süsteemide ülesehitamisel.

## Model Context Protocol

**Model Context Protocol (MCP)** on avatud standard, mis pakub rakendustele standardiseeritud viisi pakkuda konteksti ja tööriistu LLM-idele. See võimaldab „universaalset adapterit“ erinevatele andmeallikatele ja tööriistadele, millesse AI agentidel on võimalik järjepidevalt ühendada.

Vaatleme MCP komponente, eeliseid võrreldes otse API kasutamisega ja näidet, kuidas AI agent võib MCP serverit kasutada.

### MCP põhikomponendid

MCP töötab **kliendi-serveri arhitektuuril** ja põhikomponendid on:

• **Hostid** on LLM rakendused (näiteks koodiredaktor nagu VSCode), mis alustavad ühendusi MCP serveriga.

• **Kliendid** on komponendid hostrakenduse sees, mis hoiavad ühe-ühe ühendust serveritega.

• **Serverid** on kergekaalulised programmid, mis avaldavad spetsiifilisi võimeid.

Protokolli kuuluvad kolm põhialgatust, mis on MCP serveri võimed:

• **Tööriistad**: Need on eraldiseisvad toimingud või funktsioonid, mida AI agent saab kutsuda mingi tegevuse sooritamiseks. Näiteks võib ilmapalvel teenus pakkuda „saada ilm“ tööriista või e-kaubanduse server „osta toode“ tööriista. MCP serverid reklaamivad iga tööriista nime, kirjeldust ja sisend-/väljundskeemi oma võimete nimekirjas.

• **Ressursid**: Need on ainult-lugemisandmed või dokumendid, mida MCP server saab pakkuda ja mida kliendid saavad nõudmisel kätte saada. Näiteks faili sisu, andmebaasi kirjed või logifailid. Ressursid võivad olla tekstilised (nt kood või JSON) või binaarsed (nt pildid või PDF-id).

• **Sissutõmbed**: Need on ette määratud mallid, mis pakuvad ettepanekutena sisutõmbeid, võimaldades keerukamaid töövooge.

### MCP eelised

MCP pakub AI agentidele märkimisväärseid eeliseid:

• **Dünaamiline tööriistade avastamine**: Agendid saavad dünaamiliselt serverilt kätte nimekirja saadaolevatest tööriistadest koos nende tegevuste kirjeldustega. See erineb traditsioonilistest API-dest, mille integreerimiseks on sageli vaja staatilist kodeerimist, mis tähendab, et iga API muutus nõuab koodi uuendusi. MCP pakub „integreeri üks kord“ lähenemist, mis võimaldab suuremat kohanemisvõimet.

• **Ühenduvus eri LLM-idega**: MCP töötab erinevate LLM-idega, pakkudes paindlikkust tuumamodelleid vahetada parema jõudluse saavutamiseks.

• **Standardiseeritud turvalisus**: MCP sisaldab standardset autentimismeetodit, mis parandab skaleeritavust, kui lisatakse ligipääsu täiendavatele MCP serveritele. See on lihtsam kui erinevate traditsiooniliste API-de võtmete ja autentimistüüpide haldamine.

### MCP näide

![MCP Diagram](../../../translated_images/et/mcp-diagram.e4ca1cbd551444a1.webp)

Kujutame ette, et kasutaja soovib lennukipileti broneerida AI assistendi kaudu, mida juhib MCP.

1. **Ühendus**: AI assistent (MCP klient) loob ühenduse lennufirma pakutava MCP serveriga.

2. **Tööriistade avastamine**: Klient küsib lennufirma MCP serverilt: „Millised tööriistad teil olemas on?“ Server vastab tööriistadega nagu „lennupiletite otsimine“ ja „lennupiletite broneerimine“.

3. **Tööriista kutsumine**: Seejärel palud AI assistendil „Palun otsi lendu Portlandist Honolulu suunas“. AI assistent, kasutades oma LLM-i, tuvastab, et tuleb kutsuda tööriist „lennupiletite otsimine“ ja edastab asjakohased parameetrid (lähtesta, sihtkoht) MCP serverile.

4. **Täideviimine ja vastus**: MCP server, tegutsedes kui „ümbris“, teeb tegeliku kõne lennufirma siseühendusele API-le. Seejärel saab lennuinformatsiooni (nt JSON-andmed) ja saadab selle AI assistendile tagasi.

5. **Järgmine suhtlus**: AI assistent esitab lennuvõimalused. Kui kasutaja valib lennu, kutsub assistent võib-olla sama MCP serveri „lennupileti broneerimise“ tööriista, lõpetades broneerimise.

## Agent-to-Agent protokoll (A2A)

Kui MCP keskendub LLM-ide ühendamisele tööriistadega, siis **Agent-to-Agent (A2A) protokoll** läheb samm edasi, võimaldades suhtlust ja koostööd erinevate AI agentide vahel. A2A ühendab AI agendid erinevate organisatsioonide, keskkondade ja tehnoloogiastiikrite vahel ühise ülesande täitmiseks.

Uurime A2A komponente ja eeliseid ning näidet, kuidas seda võiks rakendada meie reisis rakenduses.

### A2A põhikomponendid

A2A keskendub agentide omavahelise kommunikatsiooni võimaldamisele ja nende koostööle kasutaja alamülesande täitmiseks. Iga protokolli komponent panustab sellesse:

#### Agentkaart

Sarnaselt MCP serveri tööriistade loendiga sisaldab Agentkaart järgmist:
- Agendi nimi.
- **Kirjeldus üldistest ülesannetest**, mida agent täidab.
- **Spetsiifiliste oskuste loend** koos kirjeldustega, mis aitavad teistel agentidel (või isegi inimestel) mõista, millal ja miks nad agenti kutsuda sooviksid.
- Agendi **praegune Endpoint URL**.
- Agendi **versioon** ja **võimekus**, näiteks voogedastuse vastused ja push-teavitused.

#### Agendikäitaja

Agendikäitaja vastutab **kasutaja vestluse konteksti edastamise eest kaugagentile**, kuna kaugagent vajab seda ülesande mõistmiseks. A2A serveris kasutab agent oma suurt keelemudelit (LLM), et analüüsida saabunud taotlusi ja täita ülesandeid oma sisemiste tööriistade abil.

#### Artefakt

Kui kaugagent on taotletud ülesande lõpetanud, luuakse tema töö tulemusena artefakt. Artefakt **sisaldab agendi töö tulemust**, **kirjeldust täidetud ülesandest** ja **tekstikonteksti**, mis on protokolli kaudu saadetud. Pärast artefakti saatmist suletakse ühendus kaugagentiga, kuni seda uuesti vajatakse.

#### Sündmustejada

See komponent kasutatakse **uuenduste haldamiseks ja sõnumite edastamiseks**. See on tootmises agentsete süsteemide puhul eriti oluline, et takistada agentide vahelise ühenduse sulgumist enne, kui ülesanne on lõpetatud, eriti kui ülesande täitmine võib võtta kauem aega.

### A2A eelised

• **Täiustatud koostöö**: See võimaldab agentidel erinevatelt müüjatelt ja platvormidelt suhelda, jagada konteksti ja koos töötada, võimaldades sujuvat automatiseerimist tavaühenduste vahel.

• **Mudelite valiku paindlikkus**: Iga A2A agent saab valida, millist LLM-i ta kasutab oma päringute teenindamiseks, võimaldades optimeeritud või häälestatud mudeleid iga agendi jaoks, erinevalt mõnest MCP stsenaariumist, kus on ainult üks LLM ühendus.

• **Sisseehitatud autentimine**: Autentimine on otse integreeritud A2A protokolli, pakkudes tugevat turvafraami agentide interaktsiooniks.

### A2A näide

![A2A Diagram](../../../translated_images/et/A2A-Diagram.8666928d648acc26.webp)

Täiendame meie reisibroneerimise stsenaariumi, kuid sel korral kasutades A2A-d.

1. **Kasutaja taotlus mitmeagendile**: Kasutaja suhtleb „Reisiagendi“ A2A kliendi/agendiga, näiteks öeldes: „Palun broneeri kogu reis Honolulu järgmisele nädalale, sealhulgas lennud, hotell ja autorent“.

2. **Reisiagendi orkestreerimine**: Reisiagent saab selle keeruka taotluse. Ta kasutab oma LLM-i, et ülesannet analüüsida ja teha kindlaks, et peab suhtlema teiste spetsialiseerunud agentidega.

3. **Agendid vaheline suhtlus**: Reisiagent kasutab siis A2A protokolli, et ühenduda alamagentidega, nagu „Lennufirma agent“, „Hotelli agent“ ja „Autorendi agent“, mille on loonud erinevad ettevõtted.

4. **Ülesannete delegeerimine**: Reisiagent saadab spetsialiseerunud agentidele konkreetsed ülesanded (nt „Leia lennud Honolulu“, „Broneeri hotell“, „Võta autorent“). Iga spetsialiseerunud agent, kasutades oma LLM-i ja oma tööriistu (mis võivad olla ise MCP serverid), täidab oma osa broneerimisest.

5. **Koondatud vastus**: Kui kõik alamagendid on oma ülesanded lõpule viinud, koostab Reisiagent tulemused (lennu andmed, hotelli kinnitus, autorendi broneering) ja saadab kasutajale täieliku vestlusstiilis vastuse.

## Natural Language Web (NLWeb)

Veebilehed on juba kaua olnud peamine viis kasutajate jaoks internetis info ja andmeteni ligipääsuks.

Vaatleme NLWebi erinevaid komponente, selle eeliseid ja näidet, kuidas meie NLWeb töötab, vaadates tolle reisiaplikatsiooni.

### NLWeb komponendid

- **NLWeb rakendus (tuumteenuse kood)**: Süsteem, mis töötleb loomulikus keeles esitatud küsimusi. See ühendab platvormi erinevad osad vastuste loomiseks. Seda võib mõelda kui **mootorit, mis jõustab veebisaidi loomuliku keele funktsioonid**.

- **NLWeb protokoll**: See on **loomuliku keele suhtluse põhireeglistik** veebisaidiga. See saadab vastuseid tagasi JSON formaadis (tihti kasutades Schema.org-i). Selle eesmärk on luua lihtne alus „AI-veebile“, samamoodi nagu HTML võimaldas dokumentide jagamist veebis.

- **MCP server (Model Context Protocoli lõpp-punkt)**: Iga NLWeb seadistus töötab ka MCP serverina. See tähendab, et see võib **jagada tööriistu (näiteks „küsida“ meetod) ja andmeid** teiste AI süsteemidega. Tegelikkuses teeb see veebisaidi sisu ja võimed AI agentide jaoks kasutatavaks, võimaldades saidist saada osa laiemast „agendisüsteemist“.

- **Embedimise mudelid**: Need mudelid teisendavad **veebisaidi sisu arvulisteks esituskujunditeks ehk vektoriteks** (embeddingudeks). Need vektorid kannavad tähendust, mida arvutid saavad omavahel võrrelda ja otsida. Need salvestatakse spetsiaalsesse andmebaasi ning kasutajad saavad valida, millist embedimise mudelit nad soovivad kasutada.

- **Vektorandmebaas (tagastamismehhanism)**: See andmebaas **salvestab veebisaidi sisu embeddingud**. Kui keegi esitab küsimuse, kontrollib NLWeb kiiresti vektorandmebaasi, et leida kõige asjakohasem info. Ta annab kiire nimekirja võimalikest vastustest, järjestatult sarnasuse järgi. NLWeb töötab koos erinevate vektorite salvestussüsteemidega nagu Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb näide

![NLWeb](../../../translated_images/et/nlweb-diagram.c1e2390b310e5fe4.webp)

Võtame uuesti meie reisibroneerimise veebisaidi, kuid seekord seda juhib NLWeb.

1. **Andmete omistamine**: Reisi veebisaidi olemasolevad tootekataloogid (nt lennu nimekirjad, hotelli kirjeldused, ekskursioonipaketid) on vormistatud Schema.org abil või laetud RSS voo kaudu. NLWeb tööriistad loevad need struktureeritud andmed sisse, loovad embeddingud ja salvestavad need kohalikku või kaugvektorandmebaasi.

2. **Loomuliku keele päring (inimene)**: Kasutaja külastab veebisaidi ja selle asemel, et menüüsid sirvida, sisestab vestlusliidesesse: „Leia Honolulu peresõbralik hotell koos basseiniga järgmiseks nädalaks“.

3. **NLWeb töötlemine**: NLWeb rakendus saab selle päringu. See saadab päringu mõistmiseks LLM-ile ning otsib samal ajal oma vektorandmebaasist sobivaid hotelli nimekirju.

4. **Täpsed tulemused**: LLM aitab tõlgendada andmebaasi otsingutulemusi, tuvastada parimad vasted kriteeriumite „peresõbralik“, „bassein“ ja „Honolulu“ põhjal ning vormistab loomulikus keeles vastuse. Oluline on, et vastuses viidatakse tegelikele hotellidele veebisaidi kataloogist, vältides leiutatud infot.

5. **AI agente interaktsioon**: Kuna NLWeb toimib MCP serverina, võib väline AI reisagent ka ühenduda selle veebisaidi NLWeb instantsiga. AI agent saab siis kasutada `ask` MCP meetodit, et veebisaidilt otse pärida: `ask("Kas hotell soovitab vegansõbralikke restorane Honolulu piirkonnas?")`. NLWeb instants töötleb selle, kasutades oma restoraniandmete andmebaasi (kui see on laetud) ja tagastab struktureeritud JSON-vastuse.

### Kas on veel küsimusi MCP/A2A/NLWeb kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada oma AI agentide küsimustele vastused.

## Ressursid

- [MCP algajatele](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentatsioon](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent raamistik](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Eelmine õppetund

[AI agendid tootmises](../10-ai-agents-production/README.md)

## Järgmine õppetund

[Kontekstitöö AI agentidele](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->