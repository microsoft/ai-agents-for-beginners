<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6600bebb86f72f3f62a9163fcce9566",
  "translation_date": "2025-08-30T10:10:05+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sl"
}
-->
# Uporaba agentnih protokolov (MCP, A2A in NLWeb)

[![Agentni protokoli](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sl.png)](https://youtu.be/X-Dh9R3Opn8)

Z rastjo uporabe AI agentov narašča tudi potreba po protokolih, ki zagotavljajo standardizacijo, varnost in podpirajo odprte inovacije. V tej lekciji bomo obravnavali tri protokole, ki poskušajo zadovoljiti to potrebo – Model Context Protocol (MCP), Agent to Agent (A2A) in Natural Language Web (NLWeb).

## Uvod

V tej lekciji bomo obravnavali:

• Kako **MCP** omogoča AI agentom dostop do zunanjih orodij in podatkov za izpolnjevanje uporabniških nalog.

• Kako **A2A** omogoča komunikacijo in sodelovanje med različnimi AI agenti.

• Kako **NLWeb** prinaša vmesnike v naravnem jeziku na katero koli spletno stran, kar omogoča AI agentom odkrivanje in interakcijo z vsebino.

## Cilji učenja

• **Prepoznati** osnovni namen in prednosti MCP, A2A in NLWeb v kontekstu AI agentov.

• **Razložiti**, kako vsak protokol omogoča komunikacijo in interakcijo med LLM-ji, orodji in drugimi agenti.

• **Razumeti** različne vloge, ki jih ima vsak protokol pri gradnji kompleksnih agentnih sistemov.

## Model Context Protocol

**Model Context Protocol (MCP)** je odprti standard, ki zagotavlja standardiziran način, kako aplikacije zagotavljajo kontekst in orodja za LLM-je. To omogoča "univerzalni adapter" za različne vire podatkov in orodja, s katerimi se AI agenti lahko povežejo na dosleden način.

Poglejmo komponente MCP, prednosti v primerjavi z neposredno uporabo API-jev in primer, kako AI agenti uporabljajo MCP strežnik.

### Osnovne komponente MCP

MCP deluje na **odjemalec-strežnik arhitekturi**, osnovne komponente pa so:

• **Gostitelji** so LLM aplikacije (na primer urejevalnik kode, kot je VSCode), ki vzpostavijo povezave z MCP strežnikom.

• **Odjemalci** so komponente znotraj gostiteljske aplikacije, ki vzdržujejo eno-na-eno povezave s strežniki.

• **Strežniki** so lahki programi, ki omogočajo specifične zmožnosti.

Protokol vključuje tri osnovne gradnike, ki predstavljajo zmožnosti MCP strežnika:

• **Orodja**: To so posamezna dejanja ali funkcije, ki jih AI agent lahko pokliče za izvedbo naloge. Na primer, vremenska storitev lahko ponudi orodje "pridobi vreme", ali pa e-trgovinski strežnik ponudi orodje "kupi izdelek". MCP strežniki oglašujejo ime, opis in shemo vhodov/izhodov za vsako orodje v svojem seznamu zmožnosti.

• **Viri**: To so podatkovni elementi ali dokumenti samo za branje, ki jih MCP strežnik lahko zagotovi, odjemalci pa jih lahko pridobijo na zahtevo. Primeri vključujejo vsebino datotek, zapise v podatkovnih bazah ali dnevniške datoteke. Viri so lahko besedilni (kot koda ali JSON) ali binarni (kot slike ali PDF-ji).

• **Predloge**: To so vnaprej določene predloge, ki ponujajo predlagane pozive, kar omogoča bolj zapletene delovne tokove.

### Prednosti MCP

MCP ponuja pomembne prednosti za AI agente:

• **Dinamično odkrivanje orodij**: Agenti lahko dinamično prejmejo seznam razpoložljivih orodij s strežnika skupaj z opisi njihove funkcionalnosti. To je v nasprotju s tradicionalnimi API-ji, ki pogosto zahtevajo statično kodiranje za integracije, kar pomeni, da vsaka sprememba API zahteva posodobitve kode. MCP ponuja pristop "enkrat integriraj", kar vodi do večje prilagodljivosti.

• **Interoperabilnost med LLM-ji**: MCP deluje z različnimi LLM-ji, kar omogoča fleksibilnost pri preklapljanju osnovnih modelov za boljšo zmogljivost.

• **Standardizirana varnost**: MCP vključuje standardno metodo avtentikacije, kar izboljša skalabilnost pri dodajanju dostopa do dodatnih MCP strežnikov. To je enostavnejše kot upravljanje različnih ključev in vrst avtentikacije za različne tradicionalne API-je.

### Primer MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sl.png)

Predstavljajte si, da uporabnik želi rezervirati let s pomočjo AI asistenta, ki uporablja MCP.

1. **Povezava**: AI asistent (MCP odjemalec) se poveže z MCP strežnikom, ki ga zagotavlja letalska družba.

2. **Odkrivanje orodij**: Odjemalec vpraša MCP strežnik letalske družbe: "Katera orodja imate na voljo?" Strežnik odgovori z orodji, kot sta "iskanje letov" in "rezervacija letov".

3. **Klic orodja**: Nato uporabnik vpraša AI asistenta: "Prosim, poišči let iz Portlanda v Honolulu." AI asistent s pomočjo svojega LLM prepozna, da mora poklicati orodje "iskanje letov" in posreduje ustrezne parametre (izvor, cilj) MCP strežniku.

4. **Izvedba in odgovor**: MCP strežnik, ki deluje kot vmesnik, izvede dejanski klic na notranji API za rezervacije letalske družbe. Nato prejme informacije o letu (npr. podatke v JSON obliki) in jih pošlje nazaj AI asistentu.

5. **Nadaljnja interakcija**: AI asistent predstavi možnosti letov. Ko uporabnik izbere let, lahko asistent pokliče orodje "rezervacija letov" na istem MCP strežniku in dokonča rezervacijo.

## Protokol Agent-to-Agent (A2A)

Medtem ko se MCP osredotoča na povezovanje LLM-jev z orodji, **Agent-to-Agent (A2A) protokol** naredi korak naprej, saj omogoča komunikacijo in sodelovanje med različnimi AI agenti. A2A povezuje AI agente različnih organizacij, okolij in tehnoloških skladov za izpolnitev skupne naloge.

Raziskali bomo komponente in prednosti A2A ter primer, kako bi ga lahko uporabili v naši aplikaciji za potovanja.

### Osnovne komponente A2A

A2A omogoča komunikacijo med agenti in njihovo sodelovanje pri izpolnjevanju podnalog uporabnika. Vsaka komponenta protokola prispeva k temu:

#### Kartica agenta

Podobno kot MCP strežnik deli seznam orodij, kartica agenta vsebuje:
    ◦ Ime agenta.  
    ◦ **Opis splošnih nalog**, ki jih opravlja.  
    ◦ **Seznam specifičnih veščin** z opisi, ki pomagajo drugim agentom (ali celo človeškim uporabnikom) razumeti, kdaj in zakaj bi želeli poklicati tega agenta.  
    ◦ **Trenutni URL končne točke** agenta.  
    ◦ **Različico** in **zmožnosti** agenta, kot so pretočni odgovori in potisna obvestila.  

#### Izvajalec agenta

Izvajalec agenta je odgovoren za **posredovanje konteksta uporabniškega pogovora oddaljenemu agentu**, ki potrebuje ta kontekst za razumevanje naloge, ki jo mora izpolniti. V A2A strežniku agent uporablja svoj LLM za razčlenitev dohodnih zahtev in izvedbo nalog z uporabo svojih notranjih orodij.

#### Artefakt

Ko oddaljeni agent zaključi zahtevano nalogo, ustvari artefakt. Artefakt **vsebuje rezultat dela agenta**, **opis opravljenega dela** in **besedilni kontekst**, ki se pošlje prek protokola. Pošiljanje artefakta zapre povezavo z oddaljenim agentom, dokler ni ponovno potreben.

#### Vrsta dogodkov

Ta komponenta se uporablja za **upravljanje posodobitev in posredovanje sporočil**. To je še posebej pomembno v produkciji za agentne sisteme, da se prepreči zapiranje povezave med agenti, preden je naloga dokončana, še posebej, ko lahko dokončanje naloge traja dlje časa.

### Prednosti A2A

• **Izboljšano sodelovanje**: Omogoča agentom različnih ponudnikov in platform interakcijo, deljenje konteksta in sodelovanje, kar omogoča brezhibno avtomatizacijo med tradicionalno nepovezanimi sistemi.

• **Fleksibilnost pri izbiri modela**: Vsak A2A agent se lahko sam odloči, kateri LLM bo uporabil za obdelavo svojih zahtev, kar omogoča optimizirane ali prilagojene modele za posameznega agenta, za razliko od ene same LLM povezave v nekaterih MCP scenarijih.

• **Vgrajena avtentikacija**: Avtentikacija je neposredno vključena v A2A protokol, kar zagotavlja robusten varnostni okvir za interakcije med agenti.

### Primer A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sl.png)

Razširimo naš scenarij rezervacije potovanja, tokrat z uporabo A2A.

1. **Uporabniška zahteva večagentnemu sistemu**: Uporabnik komunicira z "Potovalnim agentom" A2A odjemalcem/agentom, na primer z besedami: "Prosim, rezerviraj celotno potovanje v Honolulu za naslednji teden, vključno z letom, hotelom in najemom avtomobila."

2. **Orkestracija s strani potovalnega agenta**: Potovalni agent prejme to kompleksno zahtevo. Uporabi svoj LLM za razumevanje naloge in določi, da mora komunicirati z drugimi specializiranimi agenti.

3. **Komunikacija med agenti**: Potovalni agent nato uporabi A2A protokol za povezavo z drugimi agenti, kot so "Letalski agent", "Hotelski agent" in "Agent za najem avtomobilov", ki jih ustvarijo različna podjetja.

4. **Izvedba delegiranih nalog**: Potovalni agent pošlje specifične naloge tem specializiranim agentom (npr. "Najdi lete v Honolulu", "Rezerviraj hotel", "Najemi avto"). Vsak od teh specializiranih agentov, ki uporablja svoje LLM-je in svoja orodja (ki so lahko tudi MCP strežniki), izvede svoj specifični del rezervacije.

5. **Konsolidiran odgovor**: Ko vsi podrejeni agenti dokončajo svoje naloge, potovalni agent združi rezultate (podrobnosti o letu, potrditev hotela, rezervacija avtomobila) in pošlje celovit, pogovorni odgovor nazaj uporabniku.

## Natural Language Web (NLWeb)

Spletne strani so že dolgo primarni način za dostop uporabnikov do informacij in podatkov na internetu.

Poglejmo različne komponente NLWeb, prednosti NLWeb in primer, kako NLWeb deluje v naši aplikaciji za potovanja.

### Komponente NLWeb

- **NLWeb aplikacija (osnovna storitvena koda)**: Sistem, ki obdeluje vprašanja v naravnem jeziku. Povezuje različne dele platforme za ustvarjanje odgovorov. Lahko si ga predstavljate kot **motor, ki poganja funkcije naravnega jezika** na spletni strani.

- **NLWeb protokol**: To je **osnovni nabor pravil za interakcijo v naravnem jeziku** s spletno stranjo. Odgovore pošilja v JSON formatu (pogosto z uporabo Schema.org). Njegov namen je ustvariti preprosto osnovo za "AI splet", podobno kot je HTML omogočil deljenje dokumentov na spletu.

- **MCP strežnik (Model Context Protocol končna točka)**: Vsaka NLWeb nastavitev deluje tudi kot **MCP strežnik**. To pomeni, da lahko **deli orodja (kot je metoda "ask") in podatke** z drugimi AI sistemi. V praksi to omogoča, da vsebina in zmožnosti spletne strani postanejo uporabne za AI agente, kar omogoča, da spletna stran postane del širšega "ekosistema agentov".

- **Modeli vdelav**: Ti modeli se uporabljajo za **pretvorbo vsebine spletne strani v numerične predstavitve, imenovane vektorji** (vdelave). Ti vektorji zajamejo pomen na način, ki ga računalniki lahko primerjajo in iščejo. Shranjeni so v posebni bazi podatkov, uporabniki pa lahko izberejo, kateri model vdelav želijo uporabiti.

- **Vektorska baza podatkov (mehanizem za iskanje)**: Ta baza podatkov **shrani vdelave vsebine spletne strani**. Ko nekdo postavi vprašanje, NLWeb preveri vektorsko bazo podatkov, da hitro najde najbolj relevantne informacije. Ponuja hiter seznam možnih odgovorov, razvrščenih po podobnosti. NLWeb deluje z različnimi sistemi za shranjevanje vektorjev, kot so Qdrant, Snowflake, Milvus, Azure AI Search in Elasticsearch.

### NLWeb po primeru

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sl.png)

Razmislimo o naši spletni strani za rezervacijo potovanj, tokrat z uporabo NLWeb.

1. **Vnos podatkov**: Obstoječi katalogi izdelkov spletne strani (npr. seznami letov, opisi hotelov, turistični paketi) so oblikovani z uporabo Schema.org ali naloženi prek RSS virov. Orodja NLWeb vnesejo te strukturirane podatke, ustvarijo vdelave in jih shranijo v lokalno ali oddaljeno vektorsko bazo podatkov.

2. **Vprašanje v naravnem jeziku (človek)**: Uporabnik obišče spletno stran in namesto navigacije po menijih vpiše v pogovorni vmesnik: "Najdi mi družinam prijazen hotel v Honoluluju z bazenom za naslednji teden."

3. **Obdelava NLWeb**: NLWeb aplikacija prejme to vprašanje. Pošlje vprašanje LLM-ju za razumevanje in hkrati preišče svojo vektorsko bazo podatkov za ustrezne hotelske sezname.

4. **Natančni rezultati**: LLM pomaga interpretirati rezultate iskanja iz baze podatkov, identificira najboljše zadetke glede na kriterije "družinam prijazen", "bazen" in "Honolulu" ter oblikuje odgovor v naravnem jeziku. Ključno je, da se odgovor nanaša na dejanske hotele iz kataloga spletne strani, s čimer se izogne izmišljenim informacijam.

5. **Interakcija z AI agentom**: Ker NLWeb deluje kot MCP strežnik, se lahko z instanco NLWeb te spletne strani poveže tudi zunanji AI potovalni agent. AI agent lahko nato uporabi metodo `ask` MCP za neposredno poizvedbo spletne strani: `ask("Ali obstajajo veganske restavracije v Honoluluju, ki jih priporoča hotel?")`. NLWeb instanca to obdela, izkoristi svojo bazo podatkov z informacijami o restavracijah (če so naložene) in vrne strukturiran JSON odgovor.

### Imate več vprašanj o MCP/A2A/NLWeb?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Viri

- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)  
- [Vodiči za Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.