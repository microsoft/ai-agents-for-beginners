# Uporaba agentnih protokolov (MCP, A2A in NLWeb)

[![Agentni protokoli](../../../translated_images/sl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na sliko zgoraj za ogled videa te lekcije)_

Z naraščajočo uporabo AI agentov se povečuje tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprte inovacije. V tej lekciji bomo obravnavali 3 protokole, ki želijo zadovoljiti to potrebo - Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za dokončanje uporabniških opravil.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša naravno jezikovne vmesnike na katero koli spletno stran, kar omogoča AI agentom odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in koristi MCP, A2A in NLWeb v kontekstu AI agentov.

• **Razložiti**, kako vsak protokol omogoča komunikacijo in interakcijo med LLM, orodji in drugimi agenti.

• **Prepoznati** različne vloge, ki jih vsak protokol igra pri gradnji zapletenih agentnih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprt standard, ki omogoča standardiziran način, kako aplikacije zagotavljajo kontekst in orodja LLM-jem. To omogoča "univerzalni adapter" za različne zbirke podatkov in orodja, na katere se AI agenti lahko dosledno povežejo.

Oglejmo si sestavne dele MCP, koristi v primerjavi z neposredno uporabo API-jev ter primer, kako lahko AI agenti uporabljajo MCP strežnik.

### Osnovne komponente MCP

MCP deluje na arhitekturi **strežnik-stranka** in osnovne komponente so:

• **Gostitelji** so LLM aplikacije (na primer urejevalnik kode, kot je VSCode), ki vzpostavijo povezave do MCP strežnika.

• **Stranke** so komponente znotraj gostiteljske aplikacije, ki vzdržujejo ena-na-ena povezave s strežniki.

• **Strežniki** so lahke programe, ki razkrivajo določene zmožnosti.

Protokol vključuje tri osnovne primitive, ki predstavljajo zmožnosti MCP strežnika:

• **Orodja**: To so diskretna dejanja ali funkcije, ki jih AI agent lahko kliče za izvedbo dejanja. Na primer, vremenska služba lahko ponudi orodje "pridobi vreme" ali pa e-trgovina strežnik orodje "nakup izdelka". MCP strežniki oglašujejo ime orodja, opis in shemo vhodnih/izhodnih podatkov v seznamu zmožnosti.

• **Viri**: To so podatkovni elementi ali dokumenti, do katerih strežnik MCP zagotavlja dostop v načinu samo-za-branje, stranke jih lahko dobijo po potrebi. Primeri vključujejo vsebino datotek, zapise v bazi podatkov ali dnevniške datoteke. Viri so lahko besedilni (kot koda ali JSON) ali binarni (kot slike ali PDF).

• **Pozivi**: To so vnaprej določene predloge, ki nudijo predlagane pozive, kar omogoča bolj zapletene delovne tokove.

### Koristi MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij s strežnika skupaj z opisom njihove funkcije. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API-ja zahteva posodobitev kode. MCP ponuja pristop "integriraj enkrat", kar vodi do večje prilagodljivosti.

• **Medsebojna združljivost med LLM**: MCP deluje z različnimi LLM, kar omogoča prilagodljivost, da se zamenjajo osnovni modeli za boljše zmogljivosti.

• **Standardizirana varnost**: MCP vključuje standardizirano metodo preverjanja pristnosti, kar izboljšuje skalabilnost pri dodajanju dostopa do dodatnih MCP strežnikov. To je preprosteje kot upravljanje različnih ključev in načinov preverjanja za različne tradicionalne API-je.

### Primer MCP

![Diagram MCP](../../../translated_images/sl/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislite si uporabnika, ki želi rezervirati let z AI pomočnikom, ki ga poganja MCP.

1. **Povezava**: AI pomočnik (MCP stranka) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkritje orodij**: Stranka vpraša MCP strežnik letalske družbe: "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot so "iskanje letov" in "rezervacija letov".

3. **Klic orodja**: Nato uporabnik vpraša AI pomočnika: "Prosim, poišči let iz Portlanda v Honolulu." AI pomočnik, z uporabo svojega LLM, ugotovi, da mora poklicati orodje "iskanje letov" in posreduje ustrezne parametre (izvor, cilj) MCP strežniku.

4. **Izvedba in odgovor**: MCP strežnik, kot ovitek, izvede dejanski klic notranjega API-ja letalske družbe za rezervacije. Nato prejme informacije o letu (npr. JSON podatke) in jih pošlje nazaj AI pomočniku.

5. **Nadaljnja interakcija**: AI pomočnik predstavi možnosti letenja. Ko uporabnik izbere let, pomočnik lahko pokliče orodje "rezerviraj let" na istem MCP strežniku, s čimer dokonča rezervacijo.

## Agent-to-Agent Protocol (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM z orodji, **Agent-to-Agent (A2A) protokol** naredi korak naprej z omogočanjem komunikacije in sodelovanja med različnimi AI agenti. A2A povezuje AI agente med različnimi organizacijami, okolji in tehnološkimi skladki za dokončanje skupnega opravila.

Pregledali bomo sestavne dele in koristi A2A ter primer, kako se lahko uporabi v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A se osredotoča na omogočanje komunikacije med agenti in njihovo sodelovanje pri dokončanju podnaloge za uporabnika. Vsaka komponenta protokola k temu prispeva:

#### Agentova kartica

Podobno kot MCP strežnik deli seznam orodij, ima Agentova kartica:
- Ime agenta.
- **opis splošnih opravil**, ki jih opravlja.
- **seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo ljudskim uporabnikom) razumeti, kdaj in zakaj bi želeli klicati tega agenta.
- **trenutni URL končne točke** agenta.
- **različico** in **zmožnosti** agenta, kot so pretakanje odgovorov in potisna obvestila.

#### Izvrševalec agenta

Izvrševalec agenta je odgovoren za **posredovanje konteksta pogovora z uporabnikom oddaljenemu agentu**, saj ta potrebuje ta kontekst za razumevanje opravila, ki ga je treba dokončati. V A2A strežniku agent uporablja svoj lasten velik jezikovni model (LLM) za razčlenitev dohodnih zahtev in izvedbo nalog z lastnimi notranjimi orodji.

#### Artefakt

Ko oddaljeni agent opravi zahtevano nalogo, se njegov rezultat ustvari kot artefakt. Artefakt **vsebuje rezultat dela agenta**, **opis opravljenega dela** in **besedilni kontekst**, ki se pošlje skozi protokol. Po pošiljanju artefakta se povezava z oddaljenim agentom zapre, dokler ni spet potrebna.

#### Vrsta dogodkov

Ta komponenta se uporablja za **obdelavo posodobitev in prenos sporočil**. Še posebej je pomembna v produkciji agentnih sistemov, da prepreči zaprtje povezave med agenti pred dokončanjem naloge, še posebej, ko dokončanje naloge lahko traja dlje časa.

### Koristi A2A

• **Izboljšano sodelovanje**: Omogoča agentom iz različnih prodajalcev in platform, da medsebojno komunicirajo, delijo kontekst in sodelujejo, s čimer omogoča nemoteno avtomatizacijo med prej nepovezanimi sistemi.

• **Prilagodljivost izbire modela**: Vsak A2A agent lahko odloča, kateri LLM uporablja za obdelavo svojih zahtev, kar omogoča optimizirane ali fino nastavljene modele za posameznega agenta, v nasprotju z enim samim LLM v nekaterih MCP scenarijih.

• **Vgrajena preverjanja pristnosti**: Preverjanje pristnosti je neposredno vključeno v A2A protokol, kar nudi robusten varnostni okvir za interakcije agentov.

### Primer A2A

![Diagram A2A](../../../translated_images/sl/A2A-Diagram.8666928d648acc26.webp)

Razširimo naš scenarij rezervacije potovanja, vendar tokrat z uporabo A2A.

1. **Uporabnikova zahteva multi-agentu**: Uporabnik komunicira z A2A stranko/agenta "Potovalni agent", morda z besedami: "Prosim, rezerviraj celotno potovanje v Honolulu za naslednji teden, vključno z leti, hotelom in najemom avtomobila."

2. **Orkestracija s strani potovalnega agenta**: Potovalni agent prejme to kompleksno zahtevo. S svojim LLM presoja nalogo in ugotovi, da mora komunicirati z drugimi specializiranimi agenti.

3. **Medagentna komunikacija**: Potovalni agent se nato s pomočjo protokola A2A poveže z nižjimi agenti, kot so "Agent letalske družbe", "Agent hotela" in "Agent za najem avtomobila", ki jih ustvarjajo različna podjetja.

4. **Delegirana izvedba naloge**: Potovalni agent pošlje specifična opravila tem specializiranim agentom (npr. "Poišči lete do Honeolulu", "Rezerviraj hotel", "Najem avtomobila"). Vsak od teh agentov, ki uporablja svoj LLM in lastna orodja (lahko so tudi MCP strežniki), izvede svojo specifično nalogo.

5. **Združeni odgovor**: Ko vsi nižji agenti dokončajo svoje naloge, potovalni agent zbira rezultate (podatke o letu, potrditev hotela, rezervacijo avtomobila) in pošlje uporabniku celovit odgovor v obliki klepeta.

## Natural Language Web (NLWeb)

Spletne strani so že dolgo primarni način, kako uporabniki dostopajo do informacij in podatkov po internetu.

Oglejmo si različne sestavne dele NLWeb, njegove koristi ter primer, kako NLWeb deluje v naši aplikaciji za potovanja.

### Sestavni deli NLWeb

- **NLWeb aplikacija (osnovna storitvena koda)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko jo razumete kot **motor, ki poganja naravno jezikovne funkcije** spletne strani.

- **NLWeb protokol**: Osnovni nabor pravil za interakcijo v naravnem jeziku s spletno stranjo. V odgovoru pošilja podatke v JSON formatu (pogosto uporablja Schema.org). Namenjen je ustvarjanju preproste osnove za "AI splet", podobno kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (končna točka Model Context Protokola)**: Vsaka NLWeb namestitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja** (kot metoda “ask”) in podatke z drugimi AI sistemi. V praksi to omogoča, da je vsebina spletne strani in njene zmožnosti uporabne za AI agente, kar strani omogoča, da postane del širšega “agentnega ekosistema.”

- **Vdelani modeli (Embedding models)**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v številčne predstavitve, imenovane vektorji (embeddingi)**. Ti vektorji zajemajo pomen na način, ki ga računalniki lahko primerjajo in iščejo. Shranjeni so v posebni zbirki podatkov, uporabniki pa lahko izberejo kateri embedding model želijo uporabiti.

- **Vektorska baza podatkov (mehanizem za iskanje)**: Ta baza **shranjuje embeddinge vsebine spletne strani**. Ko nekdo postavi vprašanje, NLWeb pregleda vektorsko bazo in hitro najde najbolj relevantne informacije. Ponudi hiter seznam možnih odgovorov, razvrščenih po podobnosti. NLWeb deluje z različnimi sistemi shranjevanja vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb na primeru

![NLWeb](../../../translated_images/sl/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno si oglejmo našo spletno stran za rezervacijo potovanj, a tokrat jo poganja NLWeb.

1. **Vnos podatkov**: Obstoječi produktni katalogi spletne strani o potovanjih (npr. seznam letov, opisi hotelov, turistične ponudbe) so formatirani z uporabo Schema.org ali naloženi prek RSS virov. Orodja NLWeba zajemajo te strukturirane podatke, ustvarjajo embeddinge in jih shranjujejo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Poizvedba v naravnem jeziku (človek)**: Uporabnik obišče spletno stran in namesto navigacije po menijih vpiše v klepetni vmesnik: "Poišči družinam prijazen hotel v Honolulu z bazenom za naslednji teden".

3. **Obdelava NLWeba**: NLWeb aplikacija prejme to poizvedbo, jo pošlje LLM za razumevanje in hkrati išče v vektorski bazi ustrezne seznam hotelov.

4. **Natančni rezultati**: LLM pomaga interpretirati iskalne rezultate iz baze, prepoznati najboljše zadetke glede na kriterije "družinam prijazen", "bazen" in "Honolulu", nato pa oblikuje odgovor v naravnem jeziku. Ključno je, da se odgovor nanaša na dejanske hotele iz kataloga spletne strani in ne vsebuje izmišljenih podatkov.

5. **Interakcija AI agenta**: Ker NLWeb deluje kot MCP strežnik, se lahko zunanji AI potovalni agent poveže tudi na to NLWeb instanco spletne strani. AI agent lahko nato uporabi MCP metodo `ask` za neposredno poizvedbo spletne strani: `ask("Ali v območju Honolulu hotelsko priporočate veganske restavracije?")`. NLWeb bo to obdelal in izkoristil svojo bazo informacij o restavracijah (če je naložena) ter vrnil strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z drugimi učenjaki, udeležite pisarnskih ur in dobite odgovore na vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->