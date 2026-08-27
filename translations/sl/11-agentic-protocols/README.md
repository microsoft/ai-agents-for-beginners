# Uporaba agentskih protokolov (MCP, A2A in NLWeb)

[![Agentic Protocols](../../../translated_images/sl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite zgornjo sliko za ogled videoposnetka te lekcije)_

Z rastjo uporabe AI agentov narašča tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprte inovacije. V tej lekciji bomo obravnavali 3 protokole, ki želijo zadovoljiti to potrebo – Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za dokončanje nalog uporabnika.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša naravno jezikovno vmesnike na katerokoli spletno stran, kar AI agentom omogoča odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in koristi MCP, A2A in NLWeb v kontekstu AI agentov.

• **Pojasniti**, kako vsak protokol omogoča komunikacijo in interakcijo med LLM-ji, orodji in drugimi agenti.

• **Prepoznati** različne vloge, ki jih ima vsak protokol pri gradnji kompleksnih agentskih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprt standard, ki zagotavlja standardiziran način, kako aplikacije zagotavljajo kontekst in orodja LLM-jem. To omogoča "univerzalni priključek" na različne podatkovne vire in orodja, na katere se AI agenti lahko povezujejo na enoten način.

Oglejmo si komponente MCP, koristi v primerjavi z neposredno uporabo API-jev in primer, kako bi AI agenti lahko uporabljali MCP strežnik.

### Osnovne komponente MCP

MCP deluje na **arhitekturi klient-strežnik**, osnovne komponente pa so:

• **Gostitelji (Hosts)** so LLM aplikacije (npr. urejevalnik kode, kot je VSCode), ki vzpostavijo povezavo z MCP strežnikom.

• **Klienti (Clients)** so komponente znotraj gostiteljske aplikacije, ki ohranjajo enonapetostne povezave s strežniki.

• **Strežniki (Servers)** so lahki programi, ki razkrivajo določene zmogljivosti.

Protokol vključuje tri osnovne primitive, ki so zmogljivosti MCP strežnika:

• **Orodja (Tools)**: To so posamezni ukrepi ali funkcije, ki jih lahko AI agent sproži za izvedbo akcije. Na primer, vremenska služba lahko ponudi orodje "pridobi vreme", ali pa strežnik spletne trgovine orodje "nakup izdelka". MCP strežniki oglašujejo ime, opis in shemo vnos/izhod vsakega orodja v seznamu zmogljivosti.

• **Viri (Resources)**: To so bralno-zapisljivi podatkovni elementi ali dokumenti, ki jih MCP strežnik lahko zagotovi, klienti pa jih lahko pridobijo po potrebi. Primeri vključujejo vsebino datotek, zapise iz podatkovnih baz ali dnevniške datoteke. Viri so lahko besedilni (kot koda ali JSON) ali binarni (kot slike ali PDF-ji).

• **Napotki (Prompts)**: To so vnaprej določeni predlogi, ki nudijo predlagane napotke za omogočanje bolj kompleksnih delovnih tokov.

### Koristi MCP

MCP prinaša pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij s strežnika skupaj z opisi njihove funkcionalnosti. To kontrastira s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API-ja zahteva posodobitve kode. MCP ponuja pristop "integriraj enkrat", kar vodi do večje prilagodljivosti.

• **Medsebojna združljivost med LLM-ji**: MCP deluje preko različnih LLM-jev, kar omogoča fleksibilnost zamenjave osnovnih modelov za boljšo učinkovitost.

• **Standardizirana varnost**: MCP vključuje standardno metodo avtentikacije, ki izboljšuje skalabilnost pri dodajanju dostopa do dodatnih MCP strežnikov. To je enostavneje kot upravljanje različnih ključev in vrst avtentikacije za različne tradicionalne API-je.

### Primer MCP

![MCP Diagram](../../../translated_images/sl/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavljajte si uporabnika, ki želi rezervirati let z AI asistentom, ki deluje preko MCP.

1. **Povezava**: AI asistent (MCP klient) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkritje orodij**: Klient vpraša MCP strežnik letalske družbe, "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot so "iskanje letov" in "rezervacija letov".

3. **Uporaba orodja**: Uporabnik nato vpraša AI asistenta: "Prosim, poišči let iz Portlanda v Honolulu." AI asistent s svojim LLM prepozna, da mora poklicati orodje "iskanje letov" in posreduje ustrezne parametre (izvor, cilj) MCP strežniku.

4. **Izvedba in odgovor**: MCP strežnik, ki deluje kot vmesnik, naredi dejanski klic notranjemu API-ju letalske družbe za rezervacije. Nato prejme podatke o letu (npr. JSON podatke) in jih pošlje nazaj AI asistentu.

5. **Nadaljnja interakcija**: AI asistent predstavi možnosti letenja. Ko uporabnik izbere let, asistent lahko sproži orodje "rezervacija leta" na istem MCP strežniku in dokonča rezervacijo.

## Protokol Agent-to-Agent (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM-jev z orodji, **Agent-to-Agent (A2A) protokol** gre korak dlje in omogoča komunikacijo ter sodelovanje med različnimi AI agenti. A2A povezuje AI agente preko različnih organizacij, okolij in tehnoloških skladov za dokončanje skupne naloge.

Pregledali bomo komponente in koristi A2A ter primer njegove uporabe v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A se osredotoča na omogočanje komunikacije med agenti in njihovo sodelovanje pri dokončanju podnaloge uporabnika. Vsaka komponenta protokola prispeva k temu:

#### Agent Card

Podobno kot MCP strežnik deli seznam orodij, Agent Card vsebuje:
- Ime agenta.
- **Opis splošnih nalog**, ki jih agent opravlja.
- **Seznam specifičnih veščin** z opisi, ki drugim agentom (ali celo uporabnikom) pomagajo razumeti, kdaj in zakaj naj pokličejo tega agenta.
- **Trenutni URL končne točke** agenta.
- **Različico** in **zmogljivosti** agenta, kot so pretočni odgovori in potisna obvestila.

#### Agent Executor

Agent Executor je odgovoren za **posredovanje konteksta pogovora uporabnika oddaljenemu agentu**, saj ta potrebuje ta kontekst za razumevanje naloge, ki jo je treba dokončati. V A2A strežniku agent uporablja lasten Large Language Model (LLM) za razčlenjevanje dohodnih zahtevkov in izvajanje nalog z uporabo lastnih notranjih orodij.

#### Artifact

Ko oddaljeni agent dokonča zahtevano nalogo, je njegov rezultat ustvarjen kot artefakt. Artefakt **vsebuje rezultat agentovega dela**, **opis dokončane naloge** in **besedilni kontekst**, ki se pošlje prek protokola. Po pošiljanju artefakta se povezava z oddaljenim agentom zapre, dokler ni ponovno potrebna.

#### Event Queue

Ta komponenta se uporablja za **obdelavo posodobitev in prenos sporočil**. Pomembna je predvsem v produkciji agentskih sistemov, da prepreči zapiranje povezave med agenti pred dokončanjem naloge, zlasti če lahko dokončanje naloge traja dlje časa.

### Koristi A2A

• **Izboljšano sodelovanje**: Omogoča, da agenti različnih ponudnikov in platform medsebojno komunicirajo, delijo kontekst in sodelujejo ter tako omogočajo nemoteno avtomatizacijo prek prej nepovezanih sistemov.

• **Fleksibilnost izbire modela**: Vsak A2A agent lahko izbere, kateri LLM uporablja za obravnavo svojih zahtev, kar omogoča optimizirane ali prilagojene modele po agentih, za razliko od enotne povezave LLM v nekaterih primerih MCP.

• **Vgrajena avtentikacija**: Avtentikacija je neposredno integrirana v A2A protokol, kar zagotavlja robusten varnostni okvir za interakcije agentov.

### Primer A2A

![A2A Diagram](../../../translated_images/sl/A2A-Diagram.8666928d648acc26.webp)

Razširimo naš scenarij rezervacije potovanja, tokrat z uporabo A2A.

1. **Uporabnikova zahteva večagentnemu sistemu**: Uporabnik komunicira z A2A klientom/agenta "Potovalni agent", na primer z ukazom: "Prosim, rezerviraj celoten potovalni paket v Honolulu za naslednji teden, vključno z leti, hotelom in najemom avtomobila."

2. **Orkestracija potovalnega agenta**: Potovalni agent prejme to kompleksno zahtevo. Uporabi svoj LLM za presojo naloge in ugotovi, da mora komunicirati z drugimi specializiranimi agenti.

3. **Medagentna komunikacija**: Potovalni agent uporablja A2A protokol za povezavo z nižjimi agenti, kot so "Agent letalske družbe", "Agent hotela" in "Agent za najem avtomobila", ki so ustvarjeni s strani različnih podjetij.

4. **Delegirana izvedba nalog**: Potovalni agent pošlje specifične naloge tem specializiranim agentom (npr. "Najdi lete za Honolulu", "Rezerviraj hotel", "Najemi avto"). Vsak izmed teh agentov, ki uporablja svoj LLM in lastna orodja (lahko so celo MCP strežniki sami), opravi svoj del rezervacije.

5. **Konsolidirani odgovor**: Ko vsi nižji agenti dokončajo svoje naloge, potovalni agent združi rezultate (podrobnosti o letu, potrditev hotela, rezervacijo najema avtomobila) in pošlje obsežen, klepetu podoben odgovor uporabniku.

## Naravni jezikovni splet (NLWeb)

Spletne strani so že dolgo glavni način, kako uporabniki dostopajo do informacij in podatkov prek interneta.

Oglejmo si različne komponente NLWeb, koristi NLWeb in primer, kako deluje NLWeb skozi našo potovalno aplikacijo.

### Komponente NLWeb

- **NLWeb aplikacija (osnovna koda storitve)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko ga razumete kot **motor, ki poganja naravno jezikovne funkcije** spletne strani.

- **NLWeb protokol**: Osnovni nabor pravil za naravno jezikovno interakcijo s spletno stranjo. Odgovore vrača v formatu JSON (pogosto uporablja Schema.org). Namenjen je ustvarjanju preproste osnove za “AI splet”, tako kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (končna točka Model Context Protocol)**: Vsaka NLWeb postavitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda “ask”) in podatke** z drugimi AI sistemi. V praksi to omogoča, da so vsebine in zmogljivosti spletne strani uporabne AI agentom, kar strani omogoča vključitev v širši “agentski ekosistem.”

- **Modeli za vdelavo (Embedding Models)**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v numerične predstavitve, imenovane vektorji** (embedings). Ti vektorji zajamejo pomen tako, da jih računalniki lahko primerjajo in iščejo. Shranjeni so v posebni bazi podatkov, uporabniki pa lahko izberejo, kateri model vdelave želijo uporabiti.

- **Vektorska baza podatkov (mehanizem iskanja)**: Ta baza shranjuje embedinge vsebine spletne strani. Ko nekdo zastavi vprašanje, NLWeb pregleda to bazo, da hitro najde najbolj relevantne informacije. Daje hiter seznam možnih odgovorov, rangiranih po podobnosti. NLWeb deluje z različnimi sistemi za shranjevanje vektorjev kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb na primeru

![NLWeb](../../../translated_images/sl/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno vzemimo našo spletno stran za rezervacijo potovanj, a tokrat poganjano z NLWeb.

1. **Zajem podatkov**: Obstoječi katalogi izdelkov na spletni strani za potovanja (npr. seznami letov, opis hotela, paketne ture) so formatirani z uporabo Schema.org ali naloženi preko RSS virov. Orodja NLWeb tehnično zajamejo te strukturirane podatke, ustvarijo embedinge in jih shranijo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Naravno jezikovno vprašanje (človek)**: Uporabnik obišče spletno stran in namesto navigacije po menijih vtipka v klepetni vmesnik: "Poišči mi družinam prijazen hotel v Honolulu z bazenom za naslednji teden."

3. **Obdelava NLWeb**: NLWeb aplikacija prejme vprašanje. Pošlje ga LLM-ju za razumevanje in hkrati pregleda svojo vektorsko bazo za relevantne ponudbe hotelov.

4. **Natančni rezultati**: LLM pomaga interpretirati iskalne rezultate iz baze podatkov, prepozna najboljše zadetke glede na kriterije "družinam prijazen", "bazen" in "Honolulu", nato oblikuje odgovor v naravnem jeziku. Pomembno je, da odgovor vključuje dejanske hotele iz kataloga spletne strani in ne izmišljene informacije.

5. **Interakcija AI agenta**: Ker NLWeb deluje kot MCP strežnik, se lahko z zunanjim AI potovalnim agentom poveže instanca NLWeb na tej spletni strani. AI agent lahko uporabi MCP metodo `ask` za neposredno poizvedbo po spletni strani: `ask("Ali so v bližini hotela priporočene veganske restavracije?")`. NLWeb bo to obdelal, uporabil podatkovno bazo z informacijami o restavracijah (če je naložena) in vrnil strukturiran JSON odgovor.

### Imate še vprašanja o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) za srečanja z drugimi učenci, udeležbo na urah pisarne in odgovore na vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Prejšnja lekcija

[AI agenti v produkciji](../10-ai-agents-production/README.md)

## Naslednja lekcija

[Inženiring konteksta za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->