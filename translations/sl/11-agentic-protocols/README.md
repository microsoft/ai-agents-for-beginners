# Uporaba agentnih protokolov (MCP, A2A in NLWeb)

[![Agentni protokoli](../../../translated_images/sl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

Kako se uporaba AI agentov povečuje, se povečuje tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in spodbujajo odprto inovacijo. V tej lekciji bomo predstavili 3 protokole, ki želijo zadovoljiti to potrebo - Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za dokončanje nalog uporabnika.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša naravne jezikovne vmesnike na katerokoli spletno stran in omogoča AI agentom, da odkrijejo in komunicirajo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in koristi MCP, A2A in NLWeb v okviru AI agentov.

• **Pojasniti** kako vsak protokol omogoča komunikacijo in interakcijo med LLM, orodji in drugimi agenti.

• **Prepoznati** različne vloge, ki jih vsak protokol igra pri gradnji zapletenih agentnih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprt standard, ki zagotavlja standardiziran način, da aplikacije omogočajo kontekst in orodja LLM-jem. To omogoča "univerzalni adapter" za različne podatkovne vire in orodja, na katere se AI agenti lahko povežejo na dosleden način.

Poglejmo sestavne dele MCP, prednosti v primerjavi z neposredno uporabo API-jev in primer, kako lahko AI agenti uporabljajo MCP strežnik.

### Osnovne komponente MCP

MCP deluje na **stranka-strežnik arhitekturi** in osnovne komponente so:

• **Gostitelji (Hosts)** so LLM aplikacije (na primer urejevalnik kode kot je VSCode), ki vzpostavijo povezave z MCP strežnikom.

• **Odjemalci (Clients)** so sestavni deli znotraj gostiteljske aplikacije, ki vzdržujejo enon-nene povezave s strežniki.

• **Strežniki (Servers)** so lahki programi, ki razkrivajo specifične zmogljivosti.

V protokolu so vključene tri osnovne primitivne funkcije, ki predstavljajo zmogljivosti MCP strežnika:

• **Orodja (Tools)**: To so diskretna dejanja ali funkcije, ki jih AI agent lahko pokliče za izvedbo dejavnosti. Na primer, vremenska storitev lahko razkrije orodje "pridobi vreme", ali pa e-trgovinski strežnik orodje "nakup izdelka". MCP strežniki oglašujejo ime orodja, opis in shemo vnosa/izhoda v seznamu zmogljivosti.

• **Viri (Resources)**: To so podatkovni elementi ali dokumenti samo za branje, ki jih MCP strežnik lahko zagotovi, odjemalci pa jih lahko pridobijo na zahtevo. Primeri vključujejo vsebine datotek, podatkovne zapise ali dnevniške datoteke. Viri so lahko besedilni (kot koda ali JSON) ali binarni (kot slike ali PDF-ji).

• **Sprožilci (Prompts)**: To so prednastavljene predloge, ki nudijo predlagane poizvedbe, kar omogoča kompleksnejše delovne tokove.

### Prednosti MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij s strežnika skupaj z opisi njihove funkcionalnosti. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API-ja zahteva posodobitve kode. MCP omogoča pristop "integriraj enkrat", kar vodi do večje prilagodljivosti.

• **Medsebojna združljivost med LLM-ji**: MCP deluje med različnimi LLM-ji, kar omogoča prilagodljivost pri zamenjavi osnovnih modelov za boljše delovanje.

• **Standardizirana varnost**: MCP vključuje standardno metodo preverjanja pristnosti, kar izboljšuje razširljivost pri dodajanju dostopa do dodatnih MCP strežnikov. To je preprosteje kot upravljanje različnih ključev in vrst overitev za različne tradicionalne API-je.

### Primer MCP

![Shema MCP](../../../translated_images/sl/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavljajte si, da uporabnik želi rezervirati let z uporabo AI pomočnika, ki ga poganja MCP.

1. **Povezava**: AI pomočnik (MCP odjemalec) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkritje orodij**: Odjemalec vpraša MCP strežnik letalske družbe: "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot so "iskanje letov" in "rezervacija letov".

3. **Klicanje orodja**: Nato uporabnik prosi AI pomočnika: "Prosim, poišči let iz Portlanda v Honolulu." AI pomočnik, z uporabo svojega LLM, ugotovi, da mora poklicati orodje "iskanje letov" in posreduje ustrezne parametre (izvor, cilj) MCP strežniku.

4. **Izvedba in odgovor**: MCP strežnik, ki deluje kot ovojnica, izvede dejanski klic notranjemu sistemu za rezervacijo letalske družbe. Nato prejme podatke o letu (npr. JSON podatke) in jih pošlje nazaj AI pomočniku.

5. **Nadaljnja interakcija**: AI pomočnik prikaže možnosti letov. Ko izberete let, pomočnik lahko pokliče orodje "rezervacija leta" na istem MCP strežniku in zaključi rezervacijo.

## Protokol agent-do-agenta (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM-jev z orodji, protokol **Agent-to-Agent (A2A)** naredi korak dlje tako, da omogoči komunikacijo in sodelovanje med različnimi AI agenti. A2A povezuje AI agente med različnimi organizacijami, okolji in tehnološkimi skladi za dokončanje skupnega opravila.

Pregledali bomo komponente in koristi A2A ter primer, kako bi ga lahko uporabili v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A omogoča komunikacijo med agenti in njihovo sodelovanje za dokončanje podnaloge uporabnika. Vsaka komponenta protokola prispeva k temu:

#### Kartica agenta

Podobno kot MCP strežnik deli seznam orodij, kartica agenta vsebuje:
- Ime agenta.
- **opis splošnih opravil**, ki jih dokonča.
- **seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo človeškim uporabnikom) razumeti, kdaj in zakaj bi želeli klicati tega agenta.
- **trenutni URL končne točke** agenta
- **različico** in **zmogljivosti** agenta, kot so pretakanje odgovorov in potisna obvestila.

#### Izvrševalec agenta

Izvrševalec agenta je odgovoren za **posredovanje konteksta uporabniškega klepeta oddaljenemu agentu**, ki potrebuje ta kontekst za razumevanje naloge, ki jo mora dokončati. V A2A strežniku agent uporabi svoj lasten velik jezikovni model (LLM), da analizira dohodne zahteve in izvaja naloge z uporabo svojih notranjih orodij.

#### Artefakt

Ko oddaljeni agent dokonča zahtevano nalogo, nastane produkt dela kot artefakt. Artefakt **vsebuje rezultat agentovega dela**, **opis opravljenega** in **besedilni kontekst**, ki se pošlje skozi protokol. Po pošiljanju artefakta se povezava z oddaljenim agentom prekine, dokler ni ponovno potrebna.

#### Vrsta dogodkov

Ta komponenta se uporablja za **upravljanje posodobitev in prenašanje sporočil**. V produkciji je še posebej pomembna, da prepreči zaprtje povezave med agenti, preden je naloga dokončana, še posebej ko lahko dokončanje naloge traja dalj časa.

### Prednosti A2A

• **Izboljšano sodelovanje**: Omogoča interakcijo, deljenje konteksta in sodelovanje agentov različnih ponudnikov in platform, kar omogoča brezhibno avtomatizacijo preko prej nepovezanih sistemov.

• **Fleksibilnost izbire modelov**: Vsak A2A agent se lahko odloči, kateri LLM uporablja za obdelavo svojih zahtev, kar omogoča optimizirane ali prilagojene modele na agenta, v nasprotju z enim LLM povezavo v nekaterih primerih MCP.

• **Vgrajena overitev**: Overitev je integrirana neposredno v A2A protokol, kar nudi robusten varnostni okvir za interakcije agentov.

### Primer A2A

![Shema A2A](../../../translated_images/sl/A2A-Diagram.8666928d648acc26.webp)

Nadaljujmo naš primer rezervacije potovanja, vendar tokrat uporabimo A2A.

1. **Uporabnik pošlje zahtevo multi-agentu**: Uporabnik komunicira z "Potovalnim agentom" kot A2A odjemalcem/agentom, morda z izjavo: "Prosim, rezerviraj celotno potovanje v Honolulu za prihodnji teden, vključno z leti, hotelom in najemom avtomobila".

2. **Orkestracija s strani potovalnega agenta**: Potovalni agent prejme to zapleteno zahtevo. Uporabi svoj LLM za razmišljanje o nalogi in ugotovi, da mora komunicirati z drugimi specializiranimi agenti.

3. **Med-agentna komunikacija**: Potovalni agent z A2A protokolom poveže v nižje sosede agente, kot so "Agent letalske družbe," "Agent hotela" in "Agent za najem avtomobila," ki so ustvarjeni s strani različnih podjetij.

4. **Delegirana izvedba nalog**: Potovalni agent pošlje specifične naloge tem specializiranim agentom (npr. "Poišči lete v Honolulu," "Rezerviraj hotel," "Najem avtomobila"). Vsak od teh agentov, ki poganjajo svoje LLM-je in uporabljajo svoja orodja (lahko tudi MCP strežnike), opravi svoj del rezervacije.

5. **Združeni odgovor**: Ko vsi nižji agenti dokončajo svoje naloge, potovalni agent združi rezultate (podatke o letu, potrditev hotela, rezervacijo avtomobila) in pošlje obsežen, klepetu podoben odgovor nazaj uporabniku.

## Naravni jezikovni splet (NLWeb)

Spletne strani so že dolgo glavni način, kako uporabniki dostopajo do informacij in podatkov na internetu.

Poglejmo različne komponente NLWeb, njegove prednosti in primer, kako NLWeb deluje na naši potovalni aplikaciji.

### Komponente NLWeb

- **NLWeb aplikacija (osnovna koda storitve)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko si ga predstavljate kot **motor, ki poganja funkcije naravnega jezika** spletne strani.

- **NLWeb protokol**: To je **osnovni komplet pravil za interakcijo z naravnim jezikom** s spletno stranjo. Vračanje odgovorov je v obliki JSON (pogosto uporablja Schema.org). Namen je ustvariti preprosto osnovo za "AI splet", tako kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (Model Context Protocol konec)**: Vsaka NLWeb nastavitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda 'ask') in podatke** z drugimi AI sistemi. V praksi to omogoča, da vsebina in zmogljivosti spletne strani postanejo uporabne AI agentom, s čimer splet postane del širšega "agentnega ekosistema".

- **Modeli vdelave (Embedding models)**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v številčne prikaze imenovane vektorji** (vdelave). Ti vektorji zajamejo pomen na način, ki ga računalniki lahko primerjajo in iščejo. Shranjeni so v posebni podatkovni bazi, uporabniki pa lahko izberejo, kateri model vdelave želijo uporabiti.

- **Vektorska baza podatkov (mehanizem za iskanje)**: Ta baza podatkov **shrani vdelave vsebine spletne strani**. Ko nekdo postavi vprašanje, NLWeb preveri vektorsko bazo, da hitro najde najbolj relevantne informacije. Daje hiter seznam možnih odgovorov, razvrščen po podobnosti. NLWeb dela z različnimi sistemi za shranjevanje vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb na primeru

![NLWeb](../../../translated_images/sl/nlweb-diagram.c1e2390b310e5fe4.webp)

Spet upoštevajmo našo spletno stran za rezervacijo potovanj, vendar tokrat z NLWeb.

1. **Vnos podatkov**: Obstoječi produktni katalogi na spletni strani za potovanja (npr. seznam letov, opisi hotelov, turistični paketi) so formatirani z uporabo Schema.org ali naloženi prek RSS virov. Orodja NLWeb zajamejo te strukturirane podatke, ustvarijo vdelave in jih shranijo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Povpraševanje v naravnem jeziku (človek)**: Uporabnik obišče spletno stran in namesto da bi brskal po menijih, vpiše v klepet: "Poišči mi družinam prijazen hotel v Honolulu z bazenom za prihodnji teden."

3. **Obdelava NLWeb**: NLWeb aplikacija prejme to poizvedbo. Pošlje jo LLM za razumevanje in hkrati išče v svoji vektorski bazi relevantne hotelske sezname.

4. **Natančni rezultati**: LLM pomaga interpretirati rezultate iskanja iz baze, prepoznati najboljše ujemanje glede na kriterije "prijazno družinam," "bazen" in "Honolulu," nato pa oblikuje naravno jezikovni odgovor. Pomembno je, da se odgovor nanaša na dejanske hotele iz kataloga spletne strani in ne na izmišljene podatke.

5. **Interakcija AI agenta**: Ker NLWeb deluje kot MCP strežnik, se lahko z zunanjim AI potovalnim agentom poveže NLWeb instanca te spletne strani. AI agent lahko uporabi MCP metodo `ask` za neposredno poizvedbo spletne strani: `ask("Ali obstajajo vegansko prijazne restavracije na območju Honolulu, ki jih priporoča hotel?")`. NLWeb bo to obdelal, uporabil svojo bazo podatkov o restavracijah (če je naložena) in vrnil strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, se udeležite uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [Dokumentacija MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Prejšnja lekcija

[AI agenti v produkciji](../10-ai-agents-production/README.md)

## Naslednja lekcija

[Kontekstualno inženirstvo za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->