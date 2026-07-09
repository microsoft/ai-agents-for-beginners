# Korištenje Agentnih Protokola (MCP, A2A i NLWeb)

[![Agentic Protocols](../../../translated_images/hr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na gornju sliku za pogledati video ovog lekcije)_

Kako rastuća upotreba AI agenata napreduje, tako raste i potreba za protokolima koji osiguravaju standardizaciju, sigurnost i potiču otvorene inovacije. U ovom ćemo lekciji pokriti 3 protokola koja nastoje zadovoljiti ovu potrebu — Model Context Protocol (MCP), Agent to Agent (A2A) i Natural Language Web (NLWeb).

## Uvod

U ovoj lekciji ćemo obraditi:

• Kako **MCP** omogućava AI agentima pristup vanjskim alatima i podacima za izvršenje korisničkih zadataka.

• Kako **A2A** omogućava komunikaciju i suradnju između različitih AI agenata.

• Kako **NLWeb** donosi jezike prirodnog govora na bilo koju web stranicu, omogućavajući AI agentima da otkrivaju i komuniciraju s sadržajem.

## Ciljevi učenja

• **Prepoznati** osnovnu svrhu i prednosti MCP, A2A i NLWeb u kontekstu AI agenata.

• **Objasniti** kako svaki protokol olakšava komunikaciju i interakciju između LLM-ova, alata i drugih agenata.

• **Prepoznati** različite uloge koje svaki protokol ima u izgradnji složenih agentnih sustava.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvoreni standard koji pruža standardizirani način aplikacijama da pruže kontekst i alate LLM-ovima. Ovo omogućava "univerzalni adapter" za različite izvore podataka i alate na koje se AI agenti mogu povezati na dosljedan način.

Pogledajmo komponente MCP-a, prednosti u odnosu na izravnu API upotrebu i primjer kako bi AI agenti mogli koristiti MCP server.

### Osnovne komponente MCP-a

MCP radi na **klijent-poslužitelj arhitekturi**, a osnovne komponente su:

• **Hostovi** su LLM aplikacije (na primjer uređivač koda poput VSCode-a) koje uspostavljaju veze sa MCP serverom.

• **Klijenti** su komponente unutar host aplikacije koje održavaju veza jedan-na-jedan sa serverima.

• **Serveri** su lagani programi koji izlažu specifične mogućnosti.

U protokolu su uključene tri osnovne primitivne funkcije koje su mogućnosti MCP servera:

• **Alati**: To su pojedinačne radnje ili funkcije koje AI agent može pozvati radi izvršenja zadatka. Na primjer, servis za vremensku prognozu može izložiti alat "dohvati vremensku prognozu", ili e-trgovina može izložiti alat "kupi proizvod". MCP serveri oglašavaju ime alata, opis i shemu ulaza/izlaza u njihovoj listi mogućnosti.

• **Resursi**: To su podaci samo za čitanje ili dokumenti koje MCP server može pružiti, a klijenti ih mogu dohvatiti na zahtjev. Primjeri uključuju sadržaj datoteka, zapise u bazi podataka ili datoteke zapisnika. Resursi mogu biti tekstualni (kao kod ili JSON) ili binarni (poput slika ili PDF-a).

• **Upiti (Prompts)**: To su unaprijed definirane predloške koje pružaju predložene upite, dopuštajući složenije radne tokove.

### Prednosti MCP-a

MCP nudi značajne prednosti za AI agente:

• **Dinamično otkrivanje alata**: Agenti mogu dinamički primati popis dostupnih alata sa servera zajedno s opisima što ti alati rade. Ovo je suprotno tradicionalnim API-jima, koji često zahtijevaju statički kod za integracije, što znači da svaka promjena API-ja zahtijeva ažuriranje koda. MCP pruža pristup "integriraj jednom", što vodi ka većoj prilagodljivosti.

• **Interoperabilnost među LLM-ovima**: MCP funkcionira preko različitih LLM-ova, pružajući fleksibilnost za promjenu osnovnih modela radi bolje izvedbe.

• **Standardizirana sigurnost**: MCP uključuje standardiziranu metodu autentifikacije, poboljšavajući skalabilnost pri dodavanju pristupa dodatnim MCP serverima. To je jednostavnije od upravljanja različitim ključevima i vrstama autentifikacije za različite tradicionalne API-je.

### Primjer MCP-a

![MCP Diagram](../../../translated_images/hr/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislite korisnika koji želi rezervirati let koristeći AI asistenta pokretanog MCP-om.

1. **Povezivanje**: AI asistent (MCP klijent) se povezuje s MCP serverom kojeg pruža aviokompanija.

2. **Otkrivanje alata**: Klijent pita MCP server aviokompanije: "Koje alate imate dostupne?" Server odgovara alatima poput "pretraži letove" i "rezerviraj letove".

3. **Pozivanje alata**: Zatim kažete AI asistentu: "Molim te, potraži let iz Portlanda za Honolulu." AI asistent, koristeći svoj LLM, identificira da treba pozvati alat "pretraži letove" i prosljeđuje odgovarajuće parametre (polazište, odredište) MCP serveru.

4. **Izvršenje i odgovor**: MCP server, djelujući kao omot, izvršava stvarni poziv internom API-ju aviokompanije. Zatim prima podatke o letu (npr. JSON) i šalje ih natrag AI asistentu.

5. **Daljnja interakcija**: AI asistent prikazuje opcije leta. Kada odaberete let, asistent može pozvati alat "rezerviraj let" na istom MCP serveru, dovršavajući rezervaciju.

## Protokol Agent-to-Agent (A2A)

Dok se MCP fokusira na povezivanje LLM-ova s alatima, **Agent-to-Agent (A2A) protokol** ide korak dalje omogućujući komunikaciju i suradnju između različitih AI agenata. A2A povezuje AI agente preko različitih organizacija, okruženja i tehnoloških sustava za izvršavanje zajedničkih zadataka.

Pregledat ćemo komponente i prednosti A2A, zajedno s primjerom kako se može primijeniti u našoj aplikaciji za putovanja.

### Osnovne komponente A2A

A2A se fokusira na omogućavanje komunikacije između agenata i njihovu suradnju za dovršetak korisnikovih dijelovnih zadataka. Svaka komponenta protokola doprinosi tome:

#### Agentova kartica

Slično kao što MCP server dijeli popis alata, Agentova kartica sadrži:
- Ime agenta.
- **opis općih zadataka** koje agent obavlja.
- **popis specifičnih vještina** s opisima, koji pomažu drugim agentima (ili čak ljudskim korisnicima) razumjeti kada i zašto bi trebali pozvati tog agenta.
- **trenutni URL krajnje točke** agenta.
- **verziju** i **mogućnosti** agenta kao što su streaming odgovori i push obavijesti.

#### Izvršitelj agenta

Izvršitelj agenta je odgovoran za **prijenos konteksta korisničkog razgovora udaljenom agentu**, udaljeni agent to treba kako bi razumio zadatak koji treba obaviti. U A2A serveru, agent koristi vlastiti veliki jezični model (LLM) za analiziranje dolaznih zahtjeva i izvršavanje zadataka koristeći vlastite interne alate.

#### Artefakt

Kada udaljeni agent završi zadani zadatak, njegov radni proizvod se kreira kao artefakt. Artefakt **sadrži rezultat agentovog rada**, **opis što je obavljeno** i **tekstualni kontekst** koji se šalje kroz protokol. Nakon slanja artefakta, veza s udaljenim agentom se zatvara dok ponovno ne zatreba.

#### Red događaja

Ova komponenta se koristi za **rukovanje ažuriranjima i prijenos poruka**. Izuzetno je važna u produkciji agentnih sustava kako bi se spriječilo zatvaranje veze između agenata prije dovršetka zadatka, posebno kada može potrajati dulje vrijeme za završetak zadatka.

### Prednosti A2A

• **Poboljšana suradnja**: Omogućava agentima iz različitih prodavača i platformi interakciju, dijeljenje konteksta i zajednički rad, olakšavajući besprijekornu automatizaciju kroz tradicionalno nepovezane sustave.

• **Fleksibilnost odabira modela**: Svaki A2A agent može sam odlučiti koji LLM koristi za obradu svojih zahtjeva, dopuštajući optimizirane ili ugađane modele po agentu, za razliku od jedne LLM veze u nekim MCP scenarijima.

• **Ugrađena autentifikacija**: Autentifikacija je integrirana direktno u A2A protokol, pružajući robusni sigurnosni okvir za interakcije agenata.

### Primjer A2A

![A2A Diagram](../../../translated_images/hr/A2A-Diagram.8666928d648acc26.webp)

Proširimo naš scenarij rezervacije putovanja, ali ovaj put koristeći A2A.

1. **Korisnički zahtjev višestrukim agentima**: Korisnik komunicira s "Putničkim agentom" A2A klijentom/agentom, možda rečima: "Molim te, rezerviraj cijelo putovanje za Honolulu idući tjedan, uključujući letove, hotel i najam auta".

2. **Orkestracija od strane Putničkog agenta**: Putnički agent prima ovaj složeni zahtjev. Koristi svoj LLM da razmotri zadatak i utvrdi da treba komunicirati s drugim specijaliziranim agentima.

3. **Komunikacija između agenata**: Putnički agent zatim koristi A2A protokol za povezivanje s nižim agentima, poput "Agent aviokompanije", "Agent hotela" i "Agent najma auta" koje su kreirale različite tvrtke.

4. **Delegirano izvršenje zadataka**: Putnički agent šalje specifične zadatke ovim specijaliziranim agentima (npr. "Pronađi letove za Honolulu", "Rezerviraj hotel", "Iznajmi auto"). Svaki od tih specijaliziranih agenata, koristeći vlastite LLM-ove i vlastite alate (koji sami mogu biti MCP serveri), obavlja svoj dio rezervacije.

5. **Konsolidirani odgovor**: Kada svi niži agenti završe svoje zadatke, Putnički agent sastavi rezultate (detalje leta, potvrdu hotela, rezervaciju auta) i šalje sveobuhvatan, chat-stil odgovor korisniku.

## Natural Language Web (NLWeb)

Web stranice dugo su bile glavni način za korisnike da pristupe informacijama i podacima diljem interneta.

Pogledajmo različite komponente NLWeb-a, prednosti NLWeb-a i primjer kako naš NLWeb radi promatrajući našu aplikaciju za putovanja.

### Komponente NLWeb-a

- **NLWeb aplikacija (Glavni servisni kod)**: Sustav koji obrađuje pitanja na prirodnom jeziku. Povezuje različite dijelove platforme za kreiranje odgovora. Možete ga zamisliti kao **motor koji pokreće prirodnojezične mogućnosti web stranice**.

- **NLWeb protokol**: To je **osnovni skup pravila za interakciju prirodnim jezikom** sa web stranicom. Vraća odgovore u JSON formatu (često koristeći Schema.org). Njegova svrha je stvoriti jednostavnu osnovu za "AI web", na isti način na koji je HTML omogućio dijeljenje dokumenata online.

- **MCP server (Krajnja točka Model Context Protokola)**: Svaka NLWeb konfiguracija također radi kao **MCP server**. To znači da može **dijeliti alate (poput metode “ask”) i podatke** s drugim AI sustavima. U praksi, to znači da web stranica čini sadržaj i mogućnosti dostupnim AI agentima, dopuštajući stranici da postane dio šire “agenske ekosustave.”

- **Embedding modeli**: Ti modeli se koriste za **pretvaranje sadržaja web stranice u numeričke prikaze zvane vektori** (embeddinge). Ti vektori hvataju značenje na način koji računala mogu uspoređivati i pretraživati. Pohranjuju se u posebnu bazu podataka, a korisnici mogu odabrati koji embedding model žele koristiti.

- **Vektorska baza podataka (mehanizam pronalaska)**: Ova baza podataka **pohranjuje embeddinge sadržaja web stranice**. Kad netko postavi pitanje, NLWeb provjerava vektorsku bazu podataka kako bi brzo pronašao najrelevantnije informacije. Daje brzi popis mogućih odgovora, rangiranih prema sličnosti. NLWeb radi s različitim sustavima za pohranu vektora kao što su Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### Primjer NLWeb-a

![NLWeb](../../../translated_images/hr/nlweb-diagram.c1e2390b310e5fe4.webp)

Razmotrite ponovno našu web stranicu za rezervaciju putovanja, ali ovaj put pokreće ju NLWeb.

1. **Unos podataka**: Postojeći katalog proizvoda web stranice za putovanja (npr. popisi letova, opisi hotela, paketi tura) formatirani su putem Schema.org ili učitani putem RSS feedova. Alati NLWeb-a unose te strukturirane podatke, stvaraju embeddinge i pohranjuju ih u lokalnu ili udaljenu vektorsku bazu podataka.

2. **Prirodnojezični upit (čovjek)**: Korisnik posjećuje web stranicu i umjesto korištenja izbornika, upisuje u chat sučelje: "Pronađi mi obiteljski hotel u Honoluluu s bazenom za idući tjedan".

3. **Obrada NLWeb-a**: NLWeb aplikacija prima ovaj upit. Šalje ga LLM-u za razumijevanje i istovremeno pretražuje svoju vektorsku bazu podataka za relevantne hotelske ponude.

4. **Točni rezultati**: LLM pomaže u tumačenju rezultata pretraživanja iz baze, identificira najbolje podudarnosti na temelju kriterija "prikladno za obitelj", "bazen" i "Honolulu", te potom formatira odgovor na prirodnom jeziku. Važno je da se odgovor odnosi na stvarne hotele iz kataloga web stranice, izbjegavajući izmišljene informacije.

5. **Interakcija AI agenta**: Budući da NLWeb također djeluje kao MCP server, vanjski AI turistički agent može se povezati na ovu NLWeb instancu web stranice. AI agent može koristiti MCP metodu `ask` za izravni upit web stranice: `ask("Ima li veganskih restorana u području Honolulu koje hotel preporučuje?")`. NLWeb instanca će to obraditi, koristeći svoju bazu podataka restorana (ako je učitana), i vratiti strukturirani JSON odgovor.

### Imate li još pitanja o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, sudjelujete na uredskim satima i dobijete odgovore na svoja pitanja o AI agentima.

## Resursi

- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [Dokumentacija za MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoftov Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->