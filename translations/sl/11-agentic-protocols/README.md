# Uporaba agentskih protokolov (MCP, A2A in NLWeb)

[![Agentic Protocols](../../../translated_images/sl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite zgornjo sliko za ogled videoposnetka te lekcije)_

Z rastjo uporabe AI agentov raste tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprto inovacijo. V tej lekciji bomo obdelali 3 protokole, ki želijo zadostiti tej potrebi - Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za izvedbo uporabniških nalog.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša naravne jezikovne vmesnike na katerokoli spletno stran in omogoča AI agentom odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in koristi MCP, A2A in NLWeb v kontekstu AI agentov.

• **Pojasniti** kako vsak protokol omogoča komunikacijo in interakcijo med LLM, orodji in drugimi agenti.

• **Prepoznati** različne vloge, ki jih ima vsak protokol pri gradnji kompleksnih agentskih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprti standard, ki zagotavlja standardiziran način za aplikacije, da zagotovijo kontekst in orodja LLM-jem. To omogoča "univerzalni adapter" za različne podatkovne vire in orodja, na katera se lahko AI agenti povezujejo na dosleden način.

Poglejmo si komponente MCP, prednosti v primerjavi z neposredno uporabo API-jev in primer, kako bi AI agenti lahko uporabljali MCP strežnik.

### Osnovne komponente MCP

MCP deluje na **odjemalsko-strežniški arhitekturi** in osnovne komponente so:

• **Gostitelji** so LLM aplikacije (na primer urejevalnik kode kot je VSCode), ki vzpostavijo povezave do MCP strežnika.

• **Odjemalci** so komponente znotraj gostiteljske aplikacije, ki vzdržujejo enopovezavo s strežniki.

• **Strežniki** so lahki programi, ki izpostavljajo specifične zmogljivosti.

V protokolu so vključeni trije osnovni primitivni elementi, ki so zmogljivosti MCP strežnika:

• **Orodja**: To so posamezna dejanja ali funkcije, ki jih lahko AI agent pokliče za izvedbo akcije. Na primer, vremenska storitev lahko izpostavi orodje "pridobi vreme", ali pa strežnik e-trgovine izpostavi orodje "nakup izdelka". MCP strežniki oglašujejo ime, opis in shemo vhodnih/izhodnih podatkov za vsako orodje v svojem seznamu zmogljivosti.

• **Viri**: To so podatkovni predmeti ali dokumenti samo za branje, ki jih MCP strežnik lahko zagotovi in jih odjemalci lahko zahtevajo po potrebi. Primeri vključujejo vsebino datotek, zapise baze podatkov ali datoteke dnevnikov. Viri so lahko besedilo (kot koda ali JSON) ali binarni podatki (kot slike ali PDF-ji).

• **Pozivi**: To so vnaprej pripravljene predloge, ki nudijo predlagane pozive, kar omogoča bolj kompleksne poteke dela.

### Koristi MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij z opisi, kaj počnejo. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API-ja zahteva posodobitev kode. MCP omogoča pristop "integriraj enkrat", kar vodi k večji prilagodljivosti.

• **Medsebojna združljivost med LLM-ji**: MCP deluje z različnimi LLM-ji in omogoča fleksibilnost preklapljanja med osnovnimi modeli za boljšo zmogljivost.

• **Standardizirana varnost**: MCP vključuje standardni način avtentikacije, kar izboljša razširljivost pri dodajanju dostopa do dodatnih MCP strežnikov. To je enostavneje kot upravljanje različnih ključev in vrst avtentikacije za različne tradicionalne API-je.

### Primer MCP

![MCP Diagram](../../../translated_images/sl/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavljajte si uporabnika, ki želi z AI pomočnikom, ki poganja MCP, rezervirati let.

1. **Povezava**: AI pomočnik (MCP odjemalec) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkritje orodij**: Odjemalec vpraša MCP strežnik letalske družbe: "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot so "iskanje letov" in "rezervacija letov".

3. **Uporaba orodja**: Nato poveste AI pomočniku: "Prosim, poišči let iz Portlanda do Honoluluja." AI pomočnik, z uporabo svojega LLM-ja, prepozna, da mora poklicati orodje "iskanje letov" in preda ustrezne parametre (izvor, cilj) MCP strežniku.

4. **Izvedba in odziv**: MCP strežnik, ki deluje kot ovojnica, opravi dejanski klic do notranjega API-ja za rezervacije letalske družbe. Nato prejme podatke o letu (npr. v JSON formatu) in jih pošlje nazaj AI pomočniku.

5. **Nadaljnja interakcija**: AI pomočnik predstavi možnosti letov. Ko izberete let, lahko pomočnik pokliče orodje "rezerviraj let" na istem MCP strežniku in zaključi rezervacijo.

## Protokol Agent to Agent (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM-jev z orodji, **Agent to Agent (A2A) protokol** naredi korak dalje in omogoča komunikacijo ter sodelovanje med različnimi AI agenti. A2A povezuje AI agente med različnimi organizacijami, okolji in tehnološkimi kupi za dokončanje skupne naloge.

Ogledali si bomo komponente in prednosti A2A skupaj s primerom, kako bi se lahko uporabil v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A je usmerjen v omogočanje komunikacije med agenti in sodelovanje pri izvedbi podnaloge uporabnika. Vsaka komponenta protokola prispeva k temu:

#### Agentova kartica

Podobno kot MCP strežnik deli seznam orodij, ima Agentova kartica:
- Ime agenta.
- **Opis splošnih nalog**, ki jih opravlja.
- **Seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo ljudem) razumeti, kdaj in zakaj bi želeli poklicati tega agenta.
- **Trenutni URL končne točke** agenta.
- **Različica** in **zmogljivosti** agenta, kot so tokovni odgovori in push obvestila.

#### Izvajalec agenta

Izvajalec agenta je odgovoren za **posredovanje konteksta pogovora uporabnika oddaljenemu agentu**, ta ga potrebuje za razumevanje naloge, ki jo je treba opraviti. V A2A strežniku agent uporablja svoj lasten LLM za razumevanje dohodnih zahtev in izvajanje nalog z uporabo lastnih notranjih orodij.

#### Artefakt

Ko oddaljeni agent dokonča zahtevano nalogo, nastane artefakt. Artefakt **vsebuje rezultat agencovega dela**, **opis opravljenega dela** in **besedilni kontekst**, ki je poslan prek protokola. Po pošiljanju artefakta se povezava z oddaljenim agentom zaključi, dokler ne bo spet potrebna.

#### Vrsta dogodkov

Ta komponenta se uporablja za **upravljanje posodobitev in prenos sporočil**. Je še posebej pomembna v produkciji agentskih sistemov, da prepreči, da bi povezava med agenti bila zaprta pred dokončanjem naloge, še posebej, ko lahko čas dokončanja naloge traja dlje.

### Koristi A2A

• **Izboljšano sodelovanje**: Omogoča agentom različnih ponudnikov in platform, da komunicirajo, delijo kontekst in sodelujejo, kar omogoča nemoteno avtomatizacijo med tradicionalno nepovezanimi sistemi.

• **Fleksibilnost izbire modela**: Vsak A2A agent se lahko odloči, kateri LLM uporablja za servisiranje svojih zahtev, kar omogoča optimizirane ali posebej prilagojene modele za vsakega agenta, v nasprotju z eno samo LLM povezavo v nekaterih MCP scenarijih.

• **Vgrajena avtentikacija**: Avtentikacija je neposredno integrirana v A2A protokol, kar zagotavlja robustno varnostno ogrodje za interakcije agentov.

### Primer A2A

![A2A Diagram](../../../translated_images/sl/A2A-Diagram.8666928d648acc26.webp)

Razširimo naš scenarij rezervacije potovanj, tokrat z uporabo A2A.

1. **Uporabniška zahteva multi-agentu**: Uporabnik komunicira z A2A odjemalcem/agenta "Potovalni agent", morda z besedami: "Prosim, rezerviraj celotno potovanje v Honolulu za naslednji teden, vključno z leti, hotelom in najemom avtomobila".

2. **Orkestracija Potovalnega agenta**: Potovalni agent prejme to kompleksno zahtevo. Z LLM-jem razmisli o nalogi in ugotovi, da mora sodelovati z drugimi specializiranimi agenti.

3. **Med-agentna komunikacija**: Potovalni agent nato uporabi A2A protokol za povezavo z nižjimi agenti, kot so "Letalski agent", "Hotelski agent" in "Agent za najem avtomobila", ki jih ustvarjajo različna podjetja.

4. **Delegirano izvajanje nalog**: Potovalni agent pošlje specifične naloge tem specializiranim agentom (npr. "Najdi polete do Honoluluja", "Rezerviraj hotel", "Najemi avto"). Vsak od teh agentov, ki poganjajo svoje LLM-je in uporabljajo lastna orodja (ki so lahko tudi MCP strežniki), opravi svoj specifični del rezervacije.

5. **Konsolidiran odgovor**: Ko vsi nižji agenti opravijo svoje naloge, Potovalni agent sestavi rezultate (podatke o letu, potrdilo o hotelu, rezervacijo avtomobila) in pošlje uporabniku obsežen odgovor v klepetalnem slogu.

## Naravni jezikovni splet (NLWeb)

Spletne strani že dolgo predstavljajo glavni način za uporabnike, da dostopajo do informacij in podatkov po internetu.

Oglejmo si različne komponente NLWeb, koristi NLWeb in primer, kako NLWeb deluje v naši aplikaciji za potovanja.

### Komponente NLWeb

- **NLWeb aplikacija (glavna storitev kode)**: Sistem, ki obdeluje naravna jezikovna vprašanja. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko ga razumemo kot **motor, ki poganja zmožnosti naravnega jezika** na spletni strani.

- **NLWeb protokol**: Osnovni nabor pravil za naravno jezikovno interakcijo s spletno stranjo. V odgovoru pošilja podatke v JSON formatu (pogosto s Schema.org). Namen je ustvariti enostavno osnovo za "AI splet", podobno kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (končna točka Model Context Protocol)**: Vsaka NLWeb postavitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda "ask") in podatke** z drugimi AI sistemi. V praksi to omogoča, da vsebina in zmogljivosti spletne strani postanejo uporabne AI agentom, saj se stran vključi v širši "agentski ekosistem."

- **Vdelani modeli**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v numerične predstavitve, imenovane vektorji (embeddingi)**. Vektorji zajamejo pomen tako, da jih računalniki lahko primerjajo in iščejo. Hranijo se v posebni podatkovni zbirki in uporabniki lahko izberejo, kateri vdelani model želijo uporabiti.

- **Vektorska baza podatkov (mehanizem za pridobivanje)**: Ta baza shranjuje embeddinge vsebine spletne strani. Ko nekdo postavi vprašanje, NLWeb pregleda to bazo, da hitro najde najbolj relevantne informacije. Ponudi seznam možnih odgovorov, razvrščenih po podobnosti. NLWeb deluje z različnimi sistemi za shranjevanje vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb na primeru

![NLWeb](../../../translated_images/sl/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno si oglejmo naš spletni portal za rezervacije potovanj, tokrat pa ga poganja NLWeb.

1. **Zajem podatkov**: Obstoječi katalogi izdelkov na portalu za potovanja (npr. sezname letov, opise hotelov, turistične pakete) so formatirani z Schema.org ali naloženi preko RSS virov. Orodja NLWeb te strukturirane podatke prevzamejo, ustvarijo embeddinge in jih shranijo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Poizvedba v naravnem jeziku (človek)**: Uporabnik obišče spletno stran in namesto navigacije po menijih vtipka v klepetalni vmesnik: "Najdi mi družinam prijazen hotel na Honoluluju z bazenom za naslednji teden."

3. **Obdelava NLWeb**: NLWeb aplikacija prejme to poizvedbo. Pošlje jo LLM-ju za razumevanje in hkrati pregleda svojo vektorsko bazo za ustrezne hotelske ponudbe.

4. **Natančni rezultati**: LLM pomaga interpretirati rezultate iskanja iz baze, prepoznati najboljše ujemanje glede na kriterije "družinam prijazen", "bazen" in "Honolulu" ter nato oblikuje odgovor v naravnem jeziku. Pomembno je, da odgovor vsebuje referenco na dejanske hotele iz kataloga spletne strani, s čimer se izogne izmišljenim informacijam.

5. **Interakcija AI agenta**: Ker NLWeb deluje kot MCP strežnik, se lahko zunanji AI potovalni agent poveže s to NLWeb instanco spletne strani. AI agent lahko nato uporabi MCP metodo `ask` in neposredno povpraša spletno stran: `ask("Ali priporočate veganske restavracije v območju Honoluluja, ki jih priporoča hotel?")`. NLWeb instanca bi obdelala to vprašanje, uporabila svojo bazo podatkov o restavracijah (če je naložena) in vrnila strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, udeležite ur za vprašanja in dobite odgovore na vaša vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Prejšnja lekcija

[AI Agentje v produkciji](../10-ai-agents-production/README.md)

## Naslednja lekcija

[Inženiring konteksta za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->