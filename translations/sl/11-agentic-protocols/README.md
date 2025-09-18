<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:48:31+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sl"
}
-->
# Uporaba agentnih protokolov (MCP, A2A in NLWeb)

[![Agentni protokoli](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sl.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

Z naraščajočo uporabo AI agentov se povečuje potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprte inovacije. V tej lekciji bomo obravnavali tri protokole, ki si prizadevajo za izpolnitev teh potreb - Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za izvedbo uporabniških nalog.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša vmesnike v naravnem jeziku na katero koli spletno stran, kar omogoča AI agentom odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in prednosti MCP, A2A in NLWeb v kontekstu AI agentov.

• **Razložiti**, kako vsak protokol olajša komunikacijo in interakcijo med LLM-ji, orodji in drugimi agenti.

• **Razumeti** različne vloge, ki jih ima vsak protokol pri gradnji kompleksnih agentnih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprti standard, ki zagotavlja standardiziran način, kako aplikacije nudijo kontekst in orodja LLM-jem. To omogoča "univerzalni adapter" za različne vire podatkov in orodja, ki se lahko povežejo z AI agenti na dosleden način.

Poglejmo si komponente MCP, prednosti v primerjavi z neposredno uporabo API-jev in primer, kako bi AI agenti lahko uporabili MCP strežnik.

### Osnovne komponente MCP

MCP deluje na **odjemalec-strežnik arhitekturi**, njegove osnovne komponente pa so:

• **Gostitelji** so aplikacije LLM (na primer urejevalnik kode, kot je VSCode), ki vzpostavijo povezave z MCP strežnikom.

• **Odjemalci** so komponente znotraj gostiteljske aplikacije, ki vzdržujejo povezave ena-na-ena s strežniki.

• **Strežniki** so lahki programi, ki omogočajo specifične zmogljivosti.

Protokol vključuje tri osnovne primitivne elemente, ki predstavljajo zmogljivosti MCP strežnika:

• **Orodja**: To so posamezna dejanja ali funkcije, ki jih AI agent lahko pokliče za izvedbo naloge. Na primer, vremenska storitev lahko ponudi orodje "pridobi vreme", ali pa e-trgovinski strežnik orodje "kupite izdelek". MCP strežniki oglašujejo ime, opis in shemo vhodov/izhodov vsakega orodja v svojem seznamu zmogljivosti.

• **Viri**: To so podatkovni elementi ali dokumenti, ki jih MCP strežnik lahko zagotovi, odjemalci pa jih lahko pridobijo po potrebi. Primeri vključujejo vsebino datotek, zapise v podatkovnih bazah ali dnevniške datoteke. Viri so lahko besedilni (kot koda ali JSON) ali binarni (kot slike ali PDF-ji).

• **Predloge**: To so vnaprej določene predloge, ki ponujajo predlagane pozive, kar omogoča bolj kompleksne delovne tokove.

### Prednosti MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij od strežnika skupaj z opisi njihove funkcionalnosti. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API-ja zahteva posodobitve kode. MCP ponuja pristop "enkratna integracija", kar vodi do večje prilagodljivosti.

• **Interoperabilnost med LLM-ji**: MCP deluje z različnimi LLM-ji, kar omogoča fleksibilnost pri preklapljanju osnovnih modelov za oceno boljše zmogljivosti.

• **Standardizirana varnost**: MCP vključuje standardizirano metodo avtentikacije, kar izboljša skalabilnost pri dodajanju dostopa do dodatnih MCP strežnikov. To je preprostejše kot upravljanje različnih ključev in vrst avtentikacije za različne tradicionalne API-je.

### Primer MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sl.png)

Predstavljajte si, da uporabnik želi rezervirati let z uporabo AI asistenta, ki temelji na MCP.

1. **Povezava**: AI asistent (MCP odjemalec) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkrivanje orodij**: Odjemalec vpraša MCP strežnik letalske družbe: "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot sta "iskanje letov" in "rezervacija letov".

3. **Uporaba orodja**: Nato uporabnik vpraša AI asistenta: "Prosim, poišči let iz Portlanda v Honolulu." AI asistent, ki uporablja svoj LLM, ugotovi, da mora poklicati orodje "iskanje letov" in posreduje ustrezne parametre (izvor, destinacija) MCP strežniku.

4. **Izvedba in odgovor**: MCP strežnik, ki deluje kot ovojnica, izvede dejanski klic na notranji API za rezervacije letalske družbe. Nato prejme informacije o letu (npr. podatke v JSON obliki) in jih pošlje nazaj AI asistentu.

5. **Nadaljnja interakcija**: AI asistent predstavi možnosti letov. Ko uporabnik izbere let, asistent morda pokliče orodje "rezervacija letov" na istem MCP strežniku in zaključi rezervacijo.

## Agent-to-Agent Protocol (A2A)

Medtem ko MCP omogoča povezovanje LLM-jev z orodji, **Agent-to-Agent (A2A) protokol** gre korak dlje, saj omogoča komunikacijo in sodelovanje med različnimi AI agenti. A2A povezuje AI agente med različnimi organizacijami, okolji in tehnološkimi skladami za izvedbo skupne naloge.

Preučili bomo komponente in prednosti A2A ter primer, kako bi ga lahko uporabili v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A se osredotoča na omogočanje komunikacije med agenti in njihovo sodelovanje pri izvedbi podnaloge uporabnika. Vsaka komponenta protokola prispeva k temu:

#### Kartica agenta

Podobno kot MCP strežnik deli seznam orodij, kartica agenta vsebuje:
- Ime agenta.
- **Opis splošnih nalog**, ki jih opravlja.
- **Seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo človeškim uporabnikom) razumeti, kdaj in zakaj bi želeli poklicati tega agenta.
- **Trenutni URL končne točke** agenta.
- **Različico** in **zmogljivosti** agenta, kot so pretočni odgovori in potisna obvestila.

#### Izvajalec agenta

Izvajalec agenta je odgovoren za **posredovanje konteksta uporabniškega pogovora oddaljenemu agentu**, ki potrebuje ta kontekst za razumevanje naloge, ki jo je treba opraviti. V A2A strežniku agent uporablja svoj LLM za razčlenjevanje dohodnih zahtev in izvajanje nalog z uporabo svojih notranjih orodij.

#### Artefakt

Ko oddaljeni agent zaključi zahtevano nalogo, se njegov izdelek ustvari kot artefakt. Artefakt **vsebuje rezultat dela agenta**, **opis opravljenega dela** in **besedilni kontekst**, ki se pošlje prek protokola. Ko je artefakt poslan, se povezava z oddaljenim agentom zapre, dokler ni ponovno potrebna.

#### Čakalna vrsta dogodkov

Ta komponenta se uporablja za **upravljanje posodobitev in posredovanje sporočil**. To je še posebej pomembno v produkciji za agentne sisteme, da se prepreči zaprtje povezave med agenti pred dokončanjem naloge, zlasti kadar lahko čas dokončanja naloge traja dlje.

### Prednosti A2A

• **Izboljšano sodelovanje**: Omogoča agentom različnih ponudnikov in platform interakcijo, deljenje konteksta in sodelovanje, kar olajša avtomatizacijo med tradicionalno nepovezanimi sistemi.

• **Fleksibilnost pri izbiri modela**: Vsak A2A agent lahko odloči, kateri LLM bo uporabil za obdelavo svojih zahtev, kar omogoča optimizirane ali prilagojene modele za posameznega agenta, za razliko od povezave z enim samim LLM-jem v nekaterih scenarijih MCP.

• **Vgrajena avtentikacija**: Avtentikacija je neposredno vključena v A2A protokol, kar zagotavlja robusten varnostni okvir za interakcije med agenti.

### Primer A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sl.png)

Razširimo naš scenarij rezervacije potovanja, tokrat z uporabo A2A.

1. **Uporabniška zahteva večagentnemu sistemu**: Uporabnik komunicira z "Potovalnim agentom" A2A odjemalcem/agentom, morda z besedami: "Prosim, rezerviraj celotno potovanje v Honolulu za naslednji teden, vključno z leti, hotelom in najemom avtomobila."

2. **Orkestracija s strani potovalnega agenta**: Potovalni agent prejme to kompleksno zahtevo. Uporabi svoj LLM za razmišljanje o nalogi in ugotovi, da mora komunicirati z drugimi specializiranimi agenti.

3. **Komunikacija med agenti**: Potovalni agent nato uporabi A2A protokol za povezavo z agenti, kot so "Letalski agent", "Hotelski agent" in "Agent za najem avtomobilov", ki jih ustvarijo različna podjetja.

4. **Izvedba delegiranih nalog**: Potovalni agent pošlje specifične naloge tem specializiranim agentom (npr. "Poišči lete v Honolulu," "Rezerviraj hotel," "Najemi avto"). Vsak od teh specializiranih agentov, ki uporablja svoje LLM-je in svoja orodja (ki so lahko MCP strežniki sami), opravi svoj specifični del rezervacije.

5. **Konsolidiran odgovor**: Ko vsi specializirani agenti zaključijo svoje naloge, potovalni agent združi rezultate (podrobnosti o letu, potrditev hotela, rezervacija avtomobila) in pošlje celovit, pogovorni odgovor nazaj uporabniku.

## Natural Language Web (NLWeb)

Spletne strani so že dolgo primarni način za dostop do informacij in podatkov prek interneta.

Poglejmo si različne komponente NLWeb, prednosti NLWeb in primer, kako NLWeb deluje v naši aplikaciji za potovanja.

### Komponente NLWeb

- **NLWeb aplikacija (osnovna storitvena koda)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko si ga predstavljate kot **motor, ki poganja funkcije naravnega jezika** na spletni strani.

- **NLWeb protokol**: To je **osnovni nabor pravil za interakcijo v naravnem jeziku** s spletno stranjo. Odgovore pošilja v JSON formatu (pogosto z uporabo Schema.org). Njegov namen je ustvariti preprosto osnovo za "AI splet", podobno kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (Model Context Protocol končna točka)**: Vsaka NLWeb nastavitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda "vprašaj") in podatke** z drugimi AI sistemi. V praksi to omogoča, da vsebina in zmogljivosti spletne strani postanejo del širšega "ekosistema agentov."

- **Modeli vdelave**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v numerične predstavitve, imenovane vektorji** (vdelave). Ti vektorji zajemajo pomen na način, ki ga računalniki lahko primerjajo in iščejo. Shranjeni so v posebni podatkovni bazi, uporabniki pa lahko izberejo, kateri model vdelave želijo uporabiti.

- **Vektorska podatkovna baza (mehanizem za iskanje)**: Ta podatkovna baza **shrani vdelave vsebine spletne strani**. Ko nekdo postavi vprašanje, NLWeb preveri vektorsko podatkovno bazo, da hitro najde najbolj relevantne informacije. Ponuja hiter seznam možnih odgovorov, razvrščenih po podobnosti. NLWeb deluje z različnimi sistemi za shranjevanje vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb po primeru

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sl.png)

Razmislimo o naši spletni strani za rezervacijo potovanj, tokrat pa jo poganja NLWeb.

1. **Vnos podatkov**: Obstoječi katalogi izdelkov spletne strani (npr. seznam letov, opisi hotelov, turistični paketi) so oblikovani z uporabo Schema.org ali naloženi prek RSS virov. Orodja NLWeb vnesejo te strukturirane podatke, ustvarijo vdelave in jih shranijo v lokalno ali oddaljeno vektorsko podatkovno bazo.

2. **Vprašanje v naravnem jeziku (človek)**: Uporabnik obišče spletno stran in namesto navigacije po menijih vpiše v pogovorni vmesnik: "Poišči mi družinam prijazen hotel v Honoluluju z bazenom za naslednji teden."

3. **Obdelava NLWeb**: NLWeb aplikacija prejme to vprašanje. Pošlje vprašanje LLM-ju za razumevanje in hkrati išče v svoji vektorski podatkovni bazi za relevantne opise hotelov.

4. **Natančni rezultati**: LLM pomaga interpretirati rezultate iskanja iz podatkovne baze, identificira najboljše ujemanje glede na kriterije "družinam prijazen," "bazen" in "Honolulu" ter oblikuje odgovor v naravnem jeziku. Ključno je, da se odgovor nanaša na dejanske hotele iz kataloga spletne strani, s čimer se izogne izmišljenim informacijam.

5. **Interakcija z AI agentom**: Ker NLWeb deluje kot MCP strežnik, se lahko z NLWeb instanco te spletne strani poveže tudi zunanji AI potovalni agent. AI agent lahko nato uporabi metodo `ask` MCP za neposredno poizvedbo na spletni strani: `ask("Ali obstajajo veganske restavracije v Honoluluju, ki jih priporoča hotel?")`. NLWeb instanca to obdela, izkoristi svojo podatkovno bazo informacij o restavracijah (če je naložena) in vrne strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kjer se lahko srečate z drugimi učenci, udeležite uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Vodiči za Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.