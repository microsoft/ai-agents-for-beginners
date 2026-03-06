# Korištenje Agentnih protokola (MCP, A2A i NLWeb)

[![Agentic Protocols](../../../translated_images/hr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite gornju sliku za pregled videa ovog časa)_

Kako se korištenje AI agenata povećava, tako raste i potreba za protokolima koji osiguravaju standardizaciju, sigurnost i podržavaju otvorenu inovaciju. U ovom času razmotrit ćemo 3 protokola koji nastoje odgovoriti na ovu potrebu - Model Context Protocol (MCP), Agent to Agent (A2A) i Natural Language Web (NLWeb).

## Uvod

U ovom času ćemo obraditi:

• Kako **MCP** omogućava AI agentima pristup vanjskim alatima i podacima za izvršavanje zadataka korisnika.

• Kako **A2A** omogućava komunikaciju i suradnju između različitih AI agenata.

• Kako **NLWeb** donosi sučelja prirodnog jezika na bilo koju web stranicu, omogućujući AI agentima da otkriju i komuniciraju s sadržajem.

## Ciljevi učenja

• **Prepoznati** osnovnu svrhu i prednosti MCP, A2A i NLWeb u kontekstu AI agenata.

• **Objasniti** kako svaki protokol olakšava komunikaciju i interakciju između LLM-ova, alata i drugih agenata.

• **Prepoznati** različite uloge koje svaki protokol ima u izgradnji složenih agentnih sustava.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvoreni standard koji pruža standardizirani način da aplikacije pruže kontekst i alate LLM-ovima. To omogućava "univerzalni adaptor" za različite izvore podataka i alate kojima se AI agenti mogu dosljedno povezivati.

Pogledajmo komponente MCP-a, prednosti u odnosu na direktno korištenje API-ja i primjer kako bi AI agenti mogli koristiti MCP server.

### Osnovne komponente MCP-a

MCP radi na osnovi **klijent-server arhitekture**, a osnovne komponente su:

• **Hostovi** su LLM aplikacije (na primjer uređivač koda poput VSCodea) koje započinju veze s MCP serverom.

• **Klijenti** su komponente unutar host aplikacije koje održavaju jedan-na-jedan veze sa serverima.

• **Serveri** su lagani programi koji izlažu specifične mogućnosti.

U protokolu su uključena tri primarna elementa koja predstavljaju mogućnosti MCP servera:

• **Alati**: To su diskretne akcije ili funkcije koje AI agent može pozvati za izvršenje radnje. Na primjer, vremenska usluga može izložiti alat "dohvati vremensku prognozu", ili e-trgovina može izložiti alat "kupi proizvod". MCP serveri oglašavaju naziv, opis i shemu unosa/izlaza svakog alata u popisu njihovih mogućnosti.

• **Resursi**: To su podaci ili dokumenti samo za čitanje koje MCP server može pružiti, a klijenti ih mogu dohvatiti po potrebi. Primjeri uključuju sadržaj datoteka, zapise baza podataka ili log datoteke. Resursi mogu biti tekstualni (kao kod ili JSON) ili binarni (kao slike ili PDF-ovi).

• **Upiti (Prompts)**: To su unaprijed definirane predloške koje pružaju predložene upite, omogućujući složenije radne tokove.

### Prednosti MCP-a

MCP nudi značajne prednosti za AI agente:

• **Dinamično otkrivanje alata**: Agenti mogu dinamički primiti popis dostupnih alata sa servera zajedno s opisima njihovih funkcionalnosti. Ovo je suprotno tradicionalnim API-jima, koji često zahtijevaju statičko kodiranje za integracije, što znači da svaka promjena API-ja zahtijeva izmjene koda. MCP nudi pristup "integriraj jednom", što vodi do veće prilagodljivosti.

• **Interoperabilnost između LLM-ova**: MCP radi preko različitih LLM-ova, pružajući fleksibilnost u promjeni osnovnih modela radi boljeg performansa.

• **Standardizirana sigurnost**: MCP uključuje standardizirani način autentikacije, što poboljšava skalabilnost kod dodavanja pristupa dodatnim MCP serverima. To je jednostavnije od upravljanja različitim ključevima i tipovima autentikacije za različite tradicionalne API-je.

### MCP primjer

![MCP Diagram](../../../translated_images/hr/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislimo da korisnik želi rezervirati let koristeći AI asistenta pokretanog MCP-om.

1. **Veza**: AI asistent (MCP klijent) se povezuje na MCP server koji pruža zrakoplovna kompanija.

2. **Otkrivanje alata**: Klijent pita MCP server zrakoplovne kompanije: "Koje alate imate dostupne?" Server odgovara alatima poput "pretraži letove" i "rezerviraj letove".

3. **Pozivanje alata**: Zatim korisnik pita AI asistenta: "Molim te, pretraži let od Portlanda do Honolulua." AI asistent, koristeći svoj LLM, identificira da treba pozvati alat "pretraži letove" te šalje relevantne parametre (polazište, odredište) MCP serveru.

4. **Izvršenje i odgovor**: MCP server, djelujući kao omotač, poziva stvarni interni API zrakoplovne kompanije. Primjerice, prima informacije o letu (npr. JSON podatke) i vraća ih natrag AI asistentu.

5. **Daljnja interakcija**: AI asistent prikazuje opcije leta. Nakon što korisnik odabere let, asistent može pozvati alat "rezerviraj let" na istom MCP serveru te dovršiti rezervaciju.

## Agent-to-Agent protokol (A2A)

Dok se MCP fokusira na povezivanje LLM-ova s alatima, **Agent-to-Agent (A2A) protokol** ide korak dalje omogućavajući komunikaciju i suradnju između različitih AI agenata. A2A povezuje AI agente iz različitih organizacija, okruženja i tehnoloških sklopova radi zajedničkog izvršavanja zadatka.

Ispitat ćemo komponente i prednosti A2A, zajedno s primjerom kako se može primijeniti u našoj aplikaciji za putovanja.

### Osnovne komponente A2A

A2A se fokusira na omogućavanje komunikacije između agenata i njihovu suradnju u izvršavanju podzadatka korisnika. Svaka komponenta protokola doprinosi tome:

#### Kartica agenta (Agent Card)

Slično kao što MCP server dijeli popis alata, Agent Card sadrži:
- Ime agenta.
- **opis općih zadataka** koje agent izvršava.
- **popis specifičnih vještina** s opisima koji pomažu drugim agentima (ili čak ljudskim korisnicima) razumjeti kada i zašto bi trebali pozvati tog agenta.
- **trenutni URL krajnje točke** agenta.
- **verziju** i **mogućnosti** agenta, poput strujanja odgovora i push obavijesti.

#### Izvršitelj agenta (Agent Executor)

Izvršitelj agenta je odgovoran za **prosljeđivanje konteksta korisničkog razgovora udaljenom agentu**; udaljeni agent to treba da razumije zadatak koji treba izvršiti. U A2A serveru, agent koristi vlastiti veliki jezični model (LLM) za parsiranje dolaznih zahtjeva i izvršavanje zadataka koristeći vlastite interne alate.

#### Artefakt

Nakon što udaljeni agent izvrši traženi zadatak, njegov proizvod rada kreira se kao artefakt. Artefakt **sadrži rezultat rada agenta**, **opis onoga što je izvršeno** i **tekstualni kontekst** koji se prenosi protokolom. Nakon slanja artefakta, veza s udaljenim agentom se zatvara dok ponovno ne bude potrebna.

#### Red događaja (Event Queue)

Ova komponenta se koristi za **rukovanje ažuriranjima i prijenos poruka**. Posebno je važna u produkciji agentnih sustava kako bi se spriječilo zatvaranje veze između agenata prije završetka zadatka, osobito kada izvršavanje zadataka može trajati dulje.

### Prednosti A2A

• **Poboljšana suradnja**: Omogućuje agentima različitih dobavljača i platformi da međusobno komuniciraju, dijele kontekst i rade zajedno, olakšavajući besprijekornu automatizaciju među tradicionalno odvojenim sustavima.

• **Fleksibilnost odabira modela**: Svaki A2A agent može odlučiti koji LLM koristi za svoje zahtjeve, što omogućuje optimizirane ili prilagođene modele po agentu, za razliku od jedne LLM veze u nekim MCP scenarijima.

• **Ugrađena autentikacija**: Autentikacija je integrirana izravno u A2A protokol, pružajući robustan sigurnosni okvir za interakcije agenata.

### A2A primjer

![A2A Diagram](../../../translated_images/hr/A2A-Diagram.8666928d648acc26.webp)

Proširimo naš scenarij rezervacije putovanja, ali ovaj put koristeći A2A.

1. **Korisnički zahtjev multi-agentu**: Korisnik komunicira s "Putničkim agentom" preko A2A klijenta/agenta, recimo: "Molim te rezerviraj cijelo putovanje za Honolulu idući tjedan, uključujući letove, hotel i unajmljivanje automobila".

2. **Orkestracija Putničkog agenta**: Putnički agent prima ovaj složeni zahtjev. Koristi svoj LLM da razmotri zadatak i utvrdi da treba komunicirati s drugim specijaliziranim agentima.

3. **Međusobna komunikacija agenata**: Putnički agent koristi A2A protokol za povezivanje s podređenim agentima, poput "Agenta zrakoplovne kompanije," "Hotel agenta" i "Agenta za najam automobila" koje su kreirale različite tvrtke.

4. **Delegirano izvršavanje zadataka**: Putnički agent šalje specifične zadatke ovim specijaliziranim agentima (npr. "Pronađi letove za Honolulu," "Rezerviraj hotel," "Unajmi automobil"). Svaki od njih koristi vlastiti LLM i koristi svoje alate (koji mogu biti MCP serveri) da izvrši svoj dio rezervacije.

5. **Konsolidirani odgovor**: Kad svi podređeni agenti dovrše svoje zadatke, Putnički agent sastavlja rezultate (detalje leta, potvrdu hotela, rezervaciju auta) i šalje korisniku sveobuhvatan odgovor u formatu razgovora.

## Natural Language Web (NLWeb)

Web stranice su dugo bile primarni način na koji korisnici pristupaju informacijama i podacima putem interneta.

Pogledajmo različite komponente NLWeb-a, prednosti NLWeb-a i primjer kako naš NLWeb funkcionira kroz našu aplikaciju za putovanja.

### Komponente NLWeb-a

- **NLWeb aplikacija (kôd osnovne usluge)**: Sustav koji obrađuje upite na prirodnom jeziku. Povezuje različite dijelove platforme za stvaranje odgovora. Možete ga zamisliti kao **motor koji pokreće značajke prirodnog jezika** web stranice.

- **NLWeb protokol**: To je **osnovni skup pravila za interakciju prirodnim jezikom** s web stranicom. Vraća odgovore u JSON formatu (često koristeći Schema.org). Njegova namjena je da stvori jednostavnu osnovu za "AI web", na isti način kako je HTML omogućio dijeljenje dokumenata online.

- **MCP server (Model Context Protocol krajnja točka)**: Svaka NLWeb instalacija također radi kao **MCP server**. To znači da može **dijeliti alate (kao što je metoda „ask“) i podatke** s drugim AI sustavima. U praksi to znači da su sadržaj i mogućnosti web stranice dostupni AI agentima, čineći web dio šire "agentne ekosustava".

- **Modeli ugradnje (Embedding Models)**: Ovi modeli se koriste za **pretvorbu sadržaja web stranice u numeričke reprezentacije zvane vektori** (embedding). Ovi vektori hvataju značenje na način koji računala mogu uspoređivati i pretraživati. Pohranjuju se u posebnu bazu podataka, a korisnici mogu birati koji model ugradnje žele koristiti.

- **Vektorska baza podataka (mehanizam pretraživanja)**: Ova baza **pohranjuje embeddinge sadržaja web stranice**. Kada netko postavi pitanje, NLWeb koristi vektorsku bazu da brzo pronađe najrelevantnije informacije. Daje brzi popis mogućih odgovora, rangiran po sličnosti. NLWeb radi s različitim sustavima za pohranu vektora kao što su Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb na primjeru

![NLWeb](../../../translated_images/hr/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno razmotrimo našu web stranicu za rezervaciju putovanja, ali ovaj put s NLWeb podrškom.

1. **Unos podataka**: Postojeći katalog proizvoda web stranice za putovanja (npr. popisi letova, opisi hotela, paket ture) formatira se korištenjem Schema.org ili se učitava putem RSS feedova. Alati NLWeb-a unose te strukturirane podatke, stvaraju embeddinge i pohranjuju ih u lokalnu ili udaljenu vektorsku bazu podataka.

2. **Upit prirodnim jezikom (čovjek)**: Korisnik posjećuje web stranicu i umjesto navigacije kroz izbornike, u chat sučelje upisuje: "Pronađi mi obiteljski hotel u Honoluluu s bazenom za idući tjedan".

3. **Obrada NLWeb-a**: NLWeb aplikacija prima upit. Šalje upit LLM-u za razumijevanje i istodobno pretražuje svoju vektorsku bazu za relevantne hotel liste.

4. **Točni rezultati**: LLM pomaže tumačiti rezultate pretraživanja iz baze podataka, identificira najbolje podudarnosti po kriterijima "prikladno za obitelji", "bazen" i "Honolulu" te formatira odgovor na prirodnom jeziku. Ključno je da odgovor upućuje na stvarne hotele iz kataloga web stranice, izbjegavajući izmišljene informacije.

5. **Interakcija AI agenta**: Budući da NLWeb djeluje kao MCP server, vanjski AI agent za putovanja također se može povezati s ovom NLWeb instancom web stranice. AI agent tada može koristiti MCP metodu `ask` za upit web stranice: `ask("Postoje li neki veganski restorani u području Honolulu koje hotel preporučuje?")`. NLWeb instanca obrađuje upit koristeći svoju bazu podataka o restoranima (ako je učitana) i vraća strukturirani JSON odgovor.

### Imate li još pitanja o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) zajednici da se upoznate s drugim učenicima, sudjelujete na radnim satima i dobijete odgovore na svoja pitanja o AI agentima.

## Resursi

- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati ovlaštenim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->