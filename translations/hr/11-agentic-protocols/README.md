# Korištenje Agentnih Protokola (MCP, A2A i NLWeb)

[![Agentic Protocols](../../../translated_images/hr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na gornju sliku za pregled videozapisa ove lekcije)_

Kako raste upotreba AI agenata, tako raste i potreba za protokolima koji osiguravaju standardizaciju, sigurnost i podržavaju otvorenu inovaciju. U ovoj lekciji obradit ćemo 3 protokola koji nastoje zadovoljiti ovu potrebu - Model Context Protocol (MCP), Agent to Agent (A2A) i Natural Language Web (NLWeb).

## Uvod

U ovoj lekciji ćemo pokriti:

• Kako **MCP** omogućuje AI agentima pristup vanjskim alatima i podacima za dovršavanje korisničkih zadataka.

• Kako **A2A** omogućuje komunikaciju i suradnju između različitih AI agenata.

• Kako **NLWeb** donosi prirodne jezične sučelja na bilo koju web stranicu omogućujući AI agentima da otkrivaju i međudjeluju s sadržajem.

## Ciljevi učenja

• **Prepoznati** osnovnu svrhu i prednosti MCP-a, A2A i NLWeb-a u kontekstu AI agenata.

• **Objasniti** kako svaki protokol olakšava komunikaciju i interakciju između LLM-ova, alata i drugih agenata.

• **Prepoznati** različite uloge koje svaki protokol ima u izgradnji složenih agentnih sustava.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvoreni standard koji pruža standardiziran način za aplikacije da pruže kontekst i alate LLM-ovima. To omogućuje "univerzalni adapter" za različite izvore podataka i alate na koje se AI agenti mogu konzistentno povezati.

Pogledajmo komponente MCP-a, prednosti u odnosu na direktnu upotrebu API-ja i primjer kako bi AI agenti mogli koristiti MCP server.

### Osnovne komponente MCP-a

MCP radi na **klijent-server arhitekturi** i osnovne komponente su:

• **Hostovi** su LLM aplikacije (na primjer uređivač koda poput VSCode-a) koji pokreću veze prema MCP serveru.

• **Klijenti** su komponente unutar host aplikacije koje održavaju jedan-na-jedan veze sa serverima.

• **Serveri** su lagani programi koji izlažu određene funkcionalnosti.

U protokolu su uključene tri osnovne primitiva koja su sposobnosti MCP servera:

• **Alati**: To su zasebne akcije ili funkcije koje AI agent može pozvati za obavljanje radnje. Na primjer, vremenska služba može izložiti alat "dohvati vremensku prognozu", ili e-trgovina može izložiti alat "kupi proizvod". MCP serveri oglašavaju ime alata, opis i shemu ulaza/izlaza u svom popisu sposobnosti.

• **Resursi**: To su podaci ili dokumenti samo za čitanje koje MCP server može pružiti, a klijenti ih mogu dohvatiti po potrebi. Primjeri uključuju sadržaj datoteka, zapise u bazi podataka ili datoteke dnevnika. Resursi mogu biti tekstualni (poput koda ili JSON-a) ili binarni (poput slika ili PDF-ova).

• **Upute**: To su unaprijed definirane predloške koji pružaju predložene upite, omogućujući složenije tijekove rada.

### Prednosti MCP-a

MCP nudi značajne prednosti za AI Agente:

• **Dinamičko otkrivanje alata**: Agenti mogu dinamički primati popis dostupnih alata sa servera zajedno s opisima što ti alati rade. Ovo je u kontrastu s tradicionalnim API-jima koji često zahtijevaju statički kod za integracije, što znači da bilo kakva promjena API-ja zahtijeva ažuriranje koda. MCP nudi pristup "integriraj jednom", što dovodi do veće prilagodljivosti.

• **Interoperabilnost između LLM-ova**: MCP radi preko različitih LLM-ova, pružajući fleksibilnost za mijenjanje osnovnih modela radi bolje izvedbe.

• **Standardizirana sigurnost**: MCP uključuje standardiziranu metodu autentikacije, poboljšavajući skalabilnost prilikom dodavanja pristupa dodatnim MCP serverima. Ovo je jednostavnije od upravljanja različitim ključevima i vrstama autentikacije za razne tradicionalne API-je.

### Primjer MCP-a

![MCP Diagram](../../../translated_images/hr/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislite da korisnik želi rezervirati let koristeći AI asistenta pokretanog MCP-om.

1. **Veza**: AI asistent (MCP klijent) se povezuje na MCP server kojeg pruža zrakoplovna kompanija.

2. **Otkrivanje alata**: Klijent pita MCP server zrakoplovne kompanije: "Koje alate imate dostupne?" Server odgovara alatima kao što su "pretraži letove" i "rezerviraj letove".

3. **Poziv alata**: Zatim tražite od AI asistenta: "Molim te, potraži let od Portlanda do Honolulua." AI asistent, koristeći svoj LLM, identificira potrebu za pozivom alata "pretraži letove" i prosljeđuje relevantne parametre (polazište, odredište) MCP serveru.

4. **Izvršenje i odgovor**: MCP server, djelujući kao omotač, izvršava stvarni poziv internog API-ja za rezervacije zrakoplovne kompanije. Zatim prima informacije o letu (npr. JSON podatke) i šalje ih natrag AI asistentu.

5. **Daljnja interakcija**: AI asistent prikazuje opcije letova. Kad odaberete let, asistent može pozvati alat "rezerviraj let" na istom MCP serveru, čime dovršava rezervaciju.

## Agent-to-Agent Protokol (A2A)

Dok se MCP fokusira na povezivanje LLM-ova s alatima, **Agent-to-Agent (A2A) protokol** ide korak dalje omogućujući komunikaciju i suradnju između različitih AI agenata. A2A povezuje AI agente preko različitih organizacija, okruženja i tehnoloških slojeva za dovršavanje zajedničkog zadatka.

Pogledat ćemo komponente i prednosti A2A te primjer kako se može primijeniti u našoj aplikaciji za putovanja.

### Osnovne komponente A2A

A2A se fokusira na omogućavanje komunikacije između agenata i njihovu suradnju na dovršavanju dijela korisničkog zadatka. Svaka komponenta protokola doprinosi tome:

#### Agent Card

Slično kao što MCP server dijeli popis alata, Agent Card ima:
- Ime agenta.
- **opis općih zadataka** koje agent obavlja.
- **popis specifičnih vještina** s opisima koji pomažu drugim agentima (ili čak ljudskim korisnicima) da razumiju kada i zašto žele pozvati tog agenta.
- **trenutni URL endpointa** agenta.
- **verziju** i **sposobnosti** agenta kao što su streaming odgovora i push notifikacije.

#### Agent Executor

Agent Executor je zadužen za **prenošenje konteksta korisničkog razgovora do udaljenog agenta**, jer udaljeni agent treba razumjeti zadatak koji treba dovršiti. U A2A serveru, agent koristi svoj vlastiti Large Language Model (LLM) za obradu dolaznih zahtjeva i izvršavanje zadataka koristeći svoje interne alate.

#### Artifact

Kada udaljeni agent završi traženi zadatak, njegov radni proizvod nastaje kao artefakt. Artefakt **sadrži rezultat rada agenta**, **opis što je dovršeno** i **tekstualni kontekst** koji se šalje kroz protokol. Nakon slanja artefakta, veza s udaljenim agentom se zatvara dok ponovno nije potrebna.

#### Event Queue

Ova komponenta se koristi za **rukovanje ažuriranjima i prijenos poruka**. Posebno je važna u proizvodnim agentnim sustavima kako bi se spriječilo zatvaranje veze između agenata prije nego što zadatak bude dovršen, osobito kada dovršavanje zadatka može potrajati dulje.

### Prednosti A2A

• **Poboljšana suradnja**: Omogućuje agentima različitih dobavljača i platformi da međusobno komuniciraju, dijele kontekst i rade zajedno, olakšavajući besprijekornu automatizaciju preko tradicionalno nepovezanih sustava.

• **Fleksibilnost odabira modela**: Svaki A2A agent može odlučiti koji LLM koristi za obradu svojih zahtjeva, omogućujući optimizirane ili fino podešene modele po agentu, za razliku od jedne LLM veze u nekim MCP scenarijima.

• **Ugrađena autentikacija**: Autentikacija je integrirana direktno u A2A protokol, pružajući snažan sigurnosni okvir za interakciju agenata.

### Primjer A2A

![A2A Diagram](../../../translated_images/hr/A2A-Diagram.8666928d648acc26.webp)

Proširimo naš scenarij rezervacije putovanja, ali ovaj put koristeći A2A.

1. **Korisnički zahtjev za multi-agent**: Korisnik komunicira s "Travel Agent" A2A klijentom/agentom, možda rekavši: "Molim te rezerviraj cijelo putovanje u Honolulu za sljedeći tjedan, uključujući letove, hotel i najam automobila."

2. **Orijentacija od strane Travel Agenta**: Travel Agent prima ovaj složeni zahtjev. Koristi svoj LLM za razmišljanje o zadatku i odlučuje da mora komunicirati s drugim specijaliziranim agentima.

3. **Komunikacija među agentima**: Travel Agent zatim koristi A2A protokol za povezivanje s nizom agenata, kao što su "Airline Agent," "Hotel Agent" i "Car Rental Agent" koje su kreirale različite kompanije.

4. **Delegirano izvršenje zadataka**: Travel Agent šalje specifične zadatke tim specijaliziranim agentima (npr. "Pronađi letove za Honolulu," "Rezerviraj hotel," "Iznajmi automobil"). Svaki od tih specijaliziranih agenata, koristeći svoj vlastiti LLM i svoje alate (koji bi također mogli biti MCP serveri), obavlja svoj dio rezervacije.

5. **Konsolidirani odgovor**: Kad svi niži agenti završe svoje zadatke, Travel Agent sastavlja rezultate (detalji leta, potvrda hotela, rezervacija automobila) i šalje sveobuhvatan, razgovorni odgovor korisniku.

## Natural Language Web (NLWeb)

Web stranice su dugo bile primarni način korisnicima za pristup informacijama i podacima preko interneta.

Pogledajmo različite komponente NLWeb-a, prednosti NLWeb-a i primjer kako naš NLWeb funkcionira gledajući našu aplikaciju za putovanja.

### Komponente NLWeb-a

- **NLWeb aplikacija (primarni servisni kod)**: Sustav koji obrađuje pitanja na prirodnom jeziku. Povezuje različite dijelove platforme za stvaranje odgovora. Možete je zamisliti kao **motor koji pokreće prirodnojezične značajke** web stranice.

- **NLWeb protokol**: Osnovni skup pravila za prirodnu jezičnu interakciju s web stranicom. Vraća odgovore u JSON formatu (često koristi Schema.org). Svrha mu je stvoriti jednostavnu osnovu za “AI web” na isti način kako je HTML omogućio dijeljenje dokumenata online.

- **MCP server (Model Context Protocol endpoint)**: Svaka NLWeb konfiguracija također radi kao **MCP server**. To znači da može **dijeliti alate (kao što je metoda ‘ask’) i podatke** s drugim AI sustavima. U praksi, to čini sadržaj i mogućnosti web stranice dostupnima AI agentima, čime stranica postaje dio šire “agentne ekosustava.”

- **Embedding modeli**: Ti modeli služe za **pretvaranje sadržaja web stranice u numeričke reprezentacije zvane vektori** (embeddings). Ti vektori hvataju značenje na način koji računala mogu uspoređivati i pretraživati. Spremni su u posebnu bazu podataka, a korisnici mogu odabrati koji embedding model žele koristiti.

- **Vektorska baza podataka (mehanizam dohvaćanja)**: Ova baza podataka **sprema embeddings sadržaja web stranice**. Kada netko postavi pitanje, NLWeb provjerava vektorsku bazu kako bi brzo pronašao najrelevantnije informacije. Daje brzi popis mogućih odgovora, rangiranih po sličnosti. NLWeb radi s različitim sustavima za pohranu vektora kao što su Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb na primjeru

![NLWeb](../../../translated_images/hr/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno razmotrite našu web stranicu za rezervaciju putovanja, ali ovaj put, pokreće je NLWeb.

1. **Unos podataka**: Postojeći katalozi proizvoda na web stranici (npr. ponude letova, opisi hotela, paket ture) su formatirani korištenjem Schema.org ili učitani putem RSS feedova. Alati NLWeb-a unose ove strukturirane podatke, stvaraju embeddings i pohranjuju ih u lokalnu ili udaljenu vektorsku bazu.

2. **Prirodnojezični upit (čovjek)**: Korisnik posjećuje web stranicu i, umjesto navigacije kroz izbornike, tipka u chat sučelju: "Pronađi mi hotel prilagođen obiteljima u Honoluluu s bazenom za sljedeći tjedan".

3. **Obrada NLWeb-a**: NLWeb aplikacija prima upit. Šalje upit LLM-u radi razumijevanja i istovremeno pretražuje svoju vektorsku bazu za relevantne ponude hotela.

4. **Točni rezultati**: LLM pomaže interpretirati rezultate pretraživanja iz baze podataka, identificirati najbolje podudarnosti temeljene na kriterijima "prilagođen obiteljima," "bazen" i "Honolulu," te zatim formatira odgovor na prirodnom jeziku. Ključno je da odgovor referira stvarne hotele iz kataloga stranice, izbjegavajući izmišljene informacije.

5. **Interakcija AI agenta**: Kako NLWeb služi kao MCP server, vanjski AI agent za putovanja također se može povezati s ovom NLWeb instancom web stranice. AI agent može koristiti MCP metodu `ask` za direktno upitavanje web stranice: `ask("Postoje li veganski restorani u području Honolulua koje preporučuje hotel?")`. NLWeb instanca bi obradila to, koristeći svoj bazu podataka informacija o restoranima (ako je učitana), i vratila strukturirani JSON odgovor.

### Imate još pitanja o MCP/A2A/NLWeb-u?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, pohađate office hours i dobijete odgovore na pitanja o AI agentima.

## Resursi

- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Prethodna lekcija

[AI Agenti u produkciji](../10-ai-agents-production/README.md)

## Sljedeća lekcija

[Inženjering konteksta za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->