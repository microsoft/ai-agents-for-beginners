# Uporaba agentnih protokolov (MCP, A2A in NLWeb)

[![Agentni protokoli](../../../translated_images/sl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na sliko zgoraj za ogled videoposnetka te lekcije)_

V rasti uporabe AI agentov raste tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprte inovacije. V tej lekciji bomo obravnavali 3 protokole, ki želijo zadostiti tej potrebi - Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za dokončanje uporabnikovih nalog.

•  Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša vmesnike v naravnem jeziku na katero koli spletno mesto ter omogoča AI agentom odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** glavni namen in prednosti MCP, A2A in NLWeb v kontekstu AI agentov.

• **Razložiti** kako vsak protokol olajša komunikacijo in interakcijo med LLM-ji, orodji in drugimi agenti.

• **Prepoznati** različne vloge, ki jih vsak protokol igra pri gradnji kompleksnih agentnih sistemov.

## Model Context Protocol

The **Model Context Protocol (MCP)** je odprt standard, ki zagotavlja standardiziran način, da aplikacije zagotovijo kontekst in orodja LLM-jem. To omogoča "universal adaptor" do različnih virov podatkov in orodij, na katere se lahko AI agenti dosledno povežejo.

Poglejmo sestavine MCP, prednosti v primerjavi z neposredno uporabo API-jev in primer, kako bi AI agenti morda uporabili MCP strežnik.

### Osnovne sestavine MCP

MCP deluje na **arhitekturi odjemalec-strežnik** in osnovne sestavine so:

• **Hosts** so LLM aplikacije (na primer urejevalnik kode, kot je VSCode), ki vzpostavijo povezave do MCP strežnika.

• **Clients** so komponente znotraj gostiteljske aplikacije, ki vzdržujejo ena-na-ena povezave s strežniki.

• **Servers** so lahki programi, ki ponujajo določene zmogljivosti.

V protokolu so trije osnovni elementi, ki so zmožnosti MCP strežnika:

• **Tools**: To so ločena dejanja ali funkcije, ki jih lahko AI agent pokliče za izvedbo dejanja. Na primer, vremenska storitev bi lahko ponudila orodje "get weather", ali pa e-trgovina orodje "purchase product". MCP strežniki oglašujejo ime vsakega orodja, opis in vhodno/izhodno shemo v seznamu zmožnosti.

• **Resources**: To so podatkovni elementi ali dokumenti samo za branje, ki jih lahko MCP strežnik zagotovi, odjemalci pa jih lahko pridobijo na zahtevo. Primeri vključujejo vsebino datotek, zapise v podatkovni bazi ali dnevniške datoteke. Resources so lahko besedilo (na primer koda ali JSON) ali binarni podatki (na primer slike ali PDF-ji).

• **Prompts**: To so vnaprej določeni predlogi, ki zagotavljajo predlagane pozive, kar omogoča bolj kompleksne delovne tokove.

### Prednosti MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dynamic Tool Discovery**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij s strežnika skupaj z opisi, kaj ta orodja počnejo. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje integracij, kar pomeni, da vsaka sprememba API-ja zahteva posodobitve kode. MCP ponuja pristop "integrate once", ki vodi do večje prilagodljivosti.

• **Interoperability Across LLMs**: MCP deluje z različnimi LLM-ji, kar omogoča prilagodljivost pri zamenjavi osnovnih modelov za boljšo zmogljivost.

• **Standardized Security**: MCP vključuje standardno metodo preverjanja pristnosti, kar izboljšuje skalabilnost pri dodajanju dostopa do dodatnih MCP strežnikov. To je preprostejše kot upravljanje različnih ključev in vrst preverjanja pristnosti za različne tradicionalne API-je.

### Primer MCP

![Diagram MCP](../../../translated_images/sl/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine a user wants to book a flight using an AI assistant powered by MCP.

1. **Connection**: Pomočnik AI (the MCP client) se poveže z MCP strežnikom, ki ga nudi letalska družba.

2. **Tool Discovery**: Odjemalec vpraša MCP strežnik letalske družbe: "Katere orodja imate na voljo?" Strežnik odgovori z orodji, kot so "search flights" in "book flights".

3. **Tool Invocation**: Nato prosite AI asistenta: "Prosimo poišči let iz Portlanda v Honolulu." AI asistent, z uporabo svojega LLM, ugotovi, da mora poklicati orodje "search flights" in posredovati ustrezne parametre (origin, destination) MCP strežniku.

4. **Execution and Response**: MCP strežnik, delujoč kot vmesnik, izvede dejanski klic na notranji rezervacijski API letalske družbe. Nato prejme informacije o letih (npr. JSON podatki) in jih pošlje nazaj AI asistentu.

5. **Further Interaction**: AI asistent predstavi možnosti letov. Ko izberete let, asistent lahko pokliče orodje "book flight" na istem MCP strežniku in dokonča rezervacijo.

## Agent-to-Agent Protocol (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM-jev z orodji, **Agent-to-Agent (A2A) protokol** naredi korak dlje tako, da omogoča komunikacijo in sodelovanje med različnimi AI agenti. A2A povezuje AI agente med različnimi organizacijami, okolji in tehnološkimi skladovnicami, da bi dokončali skupno nalogo.

Pregledali bomo sestavine in prednosti A2A ter primer, kako bi ga lahko uporabili v naši potovalni aplikaciji.

### Osnovne sestavine A2A

A2A se osredotoča na omogočanje komunikacije med agenti in na to, da skupaj delajo za dokončanje podnaloge uporabnika. Vsaka sestavina protokola prispeva k temu:

#### Agentova kartica

Podobno kot MCP strežnik deli seznam orodij, Agentova kartica vsebuje:
- Ime agenta .
- A **opis splošnih nalog** ki jih opravlja.
- A **seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo človeškim uporabnikom) razumeti, kdaj in zakaj bi želeli poklicati tega agenta.
- Trenutni **Endpoint URL** agenta
- **verzija** in **zmožnosti** agenta, kot so pretočni odgovori in potisna obvestila.

#### Izvajalec agenta

Izvajalec agenta je odgovoren za **posredovanje konteksta pogovora z uporabnikom do oddaljenega agenta**, saj oddaljeni agent potrebuje to, da razume nalogo, ki jo je treba izpolniti. Na A2A strežniku agent uporablja svoj Large Language Model (LLM) za razčlenjevanje dohodnih zahtev in izvajanje nalog z uporabo svojih notranjih orodij.

#### Artefakt

Ko oddaljeni agent zaključi zahtevano nalogo, se njegov izdelek zabeleži kot artefakt. Artefakt **vsebuje rezultat agentovega dela**, **opis opravljenega** in **besedilni kontekst**, ki se pošlje skozi protokol. Po pošiljanju artefakta se povezava z oddaljenim agentom zapre, dokler ni spet potrebna.

#### Čakalna vrsta dogodkov

Ta komponenta se uporablja za **ravnanje z posodobitvami in prenašanje sporočil**. V produkcijskem okolju je še posebej pomembna za agentne sisteme, da se prepreči zaprtje povezave med agenti preden je naloga zaključena, zlasti kadar dokončanje naloge lahko traja dlje časa.

### Prednosti A2A

• **Enhanced Collaboration**: Omogoča agentom iz različnih ponudnikov in platform, da medsebojno sodelujejo, delijo kontekst in delajo skupaj, kar olajša brezhibno avtomatizacijo prek tradicionalno nepovezanih sistemov.

• **Model Selection Flexibility**: Vsak A2A agent se lahko odloči, kateri LLM bo uporabljal za obdelavo svojih zahtev, kar omogoča optimizirane ali prilagojene modele za posameznega agenta, v nasprotju z eno samo LLM povezavo v nekaterih MCP scenarijih.

• **Built-in Authentication**: Avtorizacija je integrirana neposredno v A2A protokol, kar zagotavlja robusten varnostni okvir za interakcije med agenti.

### Primer A2A

![A2A diagram](../../../translated_images/sl/A2A-Diagram.8666928d648acc26.webp)

Razširimo naš scenarij rezervacije potovanja, tokrat z uporabo A2A.

1. **User Request to Multi-Agent**: Uporabnik komunicira z A2A odjemalcem/agenta "Travel Agent", morda s prošnjo: "Prosimo rezervirajte celoten izlet v Honolulu za naslednji teden, vključno z leti, hotelom in najemom avtomobila".

2. **Orchestration by Travel Agent**: Travel Agent prejme to kompleksno zahtevo. Uporabi svoj LLM za razmislek o nalogi in ugotovi, da mora sodelovati z drugimi specializiranimi agenti.

3. **Inter-Agent Communication**: Travel Agent nato uporabi A2A protokol za povezavo z downstream agenti, kot so "Airline Agent", "Hotel Agent" in "Car Rental Agent", ki jih ustvarijo različna podjetja.

4. **Delegated Task Execution**: Travel Agent pošlje specifične naloge tem specializiranim agentom (npr. "Find flights to Honolulu", "Book a hotel", "Rent a car"). Vsak od teh specializiranih agentov, ki poganja svoj LLM in uporablja svoja orodja (ki so lahko sami MCP strežniki), opravi svoj del rezervacije.

5. **Consolidated Response**: Ko vsi downstream agenti zaključijo svoje naloge, Travel Agent združi rezultate (podrobnosti o letu, potrdilo o hotelu, rezervacijo najema avtomobila) in pošlje celovit, v slogu klepeta oblikovan odgovor nazaj uporabniku.

## Naravni jezikovni splet (NLWeb)

Spletna mesta so že dolgo glavni način, kako uporabniki dostopajo do informacij in podatkov po internetu.

Poglejmo različne sestavine NLWeb, prednosti NLWeb in primer, kako NLWeb deluje na naši potovalni aplikaciji.

### Komponente NLWeb

- **NLWeb Application (Core Service Code)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko ga razumete kot **stroj, ki poganja funkcije v naravnem jeziku** spletnega mesta.

- **NLWeb Protocol**: To je **osnovni nabor pravil za interakcijo v naravnem jeziku** s spletnim mestom. Vrača odgovore v formatu JSON (pogosto z uporabo Schema.org). Njegov namen je ustvariti preprosto osnovo za "AI Web", na enak način kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP Server (Model Context Protocol Endpoint)**: Vsaka NLWeb namestitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda "ask") in podatke** z drugimi AI sistemi. V praksi to naredi vsebino in zmogljivosti spletnega mesta uporabne za AI agente, kar omogoča, da splet postane del širšega "ekosistema agentov".

- **Embedding Models**: Ti modeli se uporabljajo za **pretvorbo vsebine spletnega mesta v številčne predstavitve, imenovane vektorji** (embeddings). Ti vektorji zajamejo pomen na način, ki ga računalniki lahko primerjajo in iščejo. Shranjeni so v posebni podatkovni bazi, uporabniki pa lahko izberejo, kateri embedding model želijo uporabljati.

- **Vector Database (Retrieval Mechanism)**: Ta baza podatkov **shranjuje vektorje vsebine spletnega mesta**. Ko nekdo postavi vprašanje, NLWeb preveri vektorsko bazo, da hitro najde najbolj relevantne informacije. Dobi hiter seznam možnih odgovorov, razvrščenih po podobnosti. NLWeb deluje z različnimi sistemi za shranjevanje vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### Primer NLWeb

![NLWeb](../../../translated_images/sl/nlweb-diagram.c1e2390b310e5fe4.webp)

Razmislimo znova o našem spletnem mestu za rezervacijo potovanj, tokrat, ko ga poganja NLWeb.

1. **Data Ingestion**: Obstoječi katalogi izdelkov na spletnem mestu za potovanja (npr. seznam letov, opisi hotelov, turistični paketi) so formatirani z uporabo Schema.org ali naloženi prek RSS virov. Orodja NLWeb uvozijo te strukturirane podatke, ustvarijo embeddings in jih shranijo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Natural Language Query (Human)**: Uporabnik obišče spletno mesto in namesto brskanja po menijih vpiše v klepetalni vmesnik: "Najdi mi družinam prijazen hotel v Honolulu z bazenom za naslednji teden".

3. **NLWeb Processing**: NLWeb aplikacija prejme to poizvedbo. Pošlje poizvedbo LLM-ju za razumevanje in hkrati išče v svoji vektorski bazi podatkov ustrezne sezname hotelov.

4. **Accurate Results**: LLM pomaga interpretirati rezultate iskanja iz baze, prepoznati najboljše ujemanje na podlagi meril "prijazen družinam", "bazen" in "Honolulu" ter nato oblikuje odgovor v naravnem jeziku. Ključno je, da se odgovor nanaša na dejanske hotele iz kataloga spletnega mesta in se izogne izmišljenim informacijam.

5. **AI Agent Interaction**: Ker NLWeb deluje kot MCP strežnik, se lahko zunanji AI potovalni agent poveže z NLWeb instanco tega spletnega mesta. AI agent bi lahko nato uporabil MCP metodo `ask` za neposredno poizvedovanje spletnega mesta: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb instanca bi to obdelala, izkoriščajoč svojo bazo podatkov z informacijami o restavracijah (če je naložena), in vrnila strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) za srečanje z drugimi učenci, udeležbo v urah za vprašanja in odgovore ter da dobite odgovore na vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repozitorij NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->