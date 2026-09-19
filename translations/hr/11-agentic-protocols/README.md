# Korištenje agentičkih protokola (MCP, A2A i NLWeb)

[![Agentic Protocols](../../../translated_images/hr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

Kako raste upotreba AI agenata, raste i potreba za protokolima koji osiguravaju standardizaciju, sigurnost i podržavaju otvorenu inovaciju. U ovoj lekciji ćemo pokriti 3 protokola usmjerena na ispunjavanje ove potrebe - Model Context Protocol (MCP), Agent to Agent (A2A) i Natural Language Web (NLWeb).

## Uvod

U ovoj lekciji ćemo obraditi:

• Kako **MCP** omogućuje AI agentima pristup vanjskim alatima i podacima za dovršavanje korisničkih zadataka.

• Kako **A2A** omogućuje komunikaciju i suradnju između različitih AI agenata.

• Kako **NLWeb** donosi prirodni jezični sučelje na bilo koju web stranicu, omogućujući AI agentima da otkriju i komuniciraju s sadržajem.

## Ciljevi učenja

• **Prepoznati** glavnu svrhu i prednosti MCP, A2A i NLWeb u kontekstu AI agenata.

• **Objasniti** kako svaki protokol olakšava komunikaciju i interakciju između LLM-ova, alata i drugih agenata.

• **Prepoznati** različite uloge koje svaki protokol ima u izgradnji složenih agentičkih sustava.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvoreni standard koji pruža standardizirani način za aplikacije da pruže kontekst i alate LLM-ovima. To omogućuje "univerzalni prilagodnik" za različite izvore podataka i alate na koje se AI agenti mogu dosljedno povezati.

Pogledajmo komponente MCP-a, prednosti u odnosu na izravan rad s API-jem i primjer kako AI agenti mogu koristiti MCP poslužitelj.

### Osnovne komponente MCP-a

MCP djeluje na **klijent-poslužitelj arhitekturi** i osnovne komponente su:

• **Hostovi** su LLM aplikacije (npr. uređivač koda poput VSCode-a) koje pokreću veze prema MCP poslužitelju.

• **Klijenti** su komponente unutar host aplikacije koje održavaju veze jedan-na-jedan s poslužiteljima.

• **Poslužitelji** su lagani programi koji izlažu određene mogućnosti.

U protokolu su uključena tri osnovna primitiva koja su kapaciteti MCP poslužitelja:

• **Alati**: To su diskretne radnje ili funkcije koje AI agent može pozvati za obavljanje zadatka. Na primjer, vremenska služba može izložiti alat "dohvati vremensku prognozu", ili e-trgovina alat "kupi proizvod". MCP poslužitelji oglašavaju ime, opis i shemu ulaza/izlaza svakog alata u svojoj listi mogućnosti.

• **Resursi**: To su samo za čitanje podaci ili dokumenti koje MCP poslužitelj može pružiti, a klijenti ih mogu dohvatiti po zahtjevu. Primjeri uključuju sadržaj datoteka, zapise u bazama ili zapisnike. Resursi mogu biti tekstualni (poput koda ili JSON-a) ili binarni (poput slika ili PDF-ova).

• **Upiti (Prompts)**: To su unaprijed definirani predlošci koji nude predložene upite, omogućujući složenije radne tokove.

### Prednosti MCP-a

MCP nudi značajne prednosti za AI agente:

• **Dinamično otkrivanje alata**: Agenti mogu dinamički primiti popis dostupnih alata s poslužitelja zajedno s opisima njihove funkcije. Ovo je suprotno tradicionalnim API-jima koji često zahtijevaju statičko kodiranje integracija, što znači da svaka promjena API-ja traži ažuriranja koda. MCP nudi pristup "integriraj jednom", što omogućuje veću prilagodljivost.

• **Međuprocesna interoperabilnost LLM-ova**: MCP radi preko različitih LLM-ova, pružajući fleksibilnost za prebacivanje glavnih modela radi boljih performansi.

• **Standardizirana sigurnost**: MCP uključuje standardizirani način autentifikacije, poboljšavajući skalabilnost prilikom dodavanja pristupa dodatnim MCP poslužiteljima. To je jednostavnije nego upravljanje različitim ključevima i vrstama autentifikacije za različite tradicionalne API-je.

### Primjer MCP-a

![MCP Diagram](../../../translated_images/hr/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislimo korisnika koji želi rezervirati let koristeći AI asistenta vođenog MCP-om.

1. **Veza**: AI asistent (MCP klijent) se povezuje s MCP poslužiteljem koji pruža aviokompanija.

2. **Otkriće alata**: Klijent pita MCP poslužitelj aviokompanije: "Koje alate imate dostupne?" Poslužitelj odgovara alatima kao što su "pretraži letove" i "rezerviraj letove".

3. **Pozivanje alata**: Zatim korisnik traži od AI asistenta: "Molim te pronađi let od Portlanda do Honolulu." AI asistent, koristeći svoj LLM, prepoznaje da treba pozvati alat "pretraži letove" i prosljeđuje potrebne parametre (polazište, odredište) MCP poslužitelju.

4. **Izvršenje i odgovor**: MCP poslužitelj, djelujući kao omot, pravi stvarni poziv prema internom sustavu rezervacija aviokompanije. Zatim prima informacije o letu (npr. JSON podatke) i šalje ih natrag AI asistentu.

5. **Daljnja interakcija**: AI asistent prikazuje opcije letova. Kad korisnik odabere let, asistent može pozvati alat "rezerviraj let" na istom MCP poslužitelju i dovršiti rezervaciju.

## Agent-to-Agent protokol (A2A)

Dok MCP fokus stavlja na povezivanje LLM-ova s alatima, **Agent-to-Agent (A2A) protokol** ide korak dalje omogućujući komunikaciju i suradnju između različitih AI agenata. A2A povezuje AI agente preko različitih organizacija, okruženja i tehnoloških platformi da zajednički izvrše zadatak.

Pogledat ćemo komponente i prednosti A2A, kao i primjer kako se može primijeniti u našoj aplikaciji za putovanja.

### Osnovne komponente A2A

A2A se fokusira na omogućavanje komunikacije između agenata i njihov rad zajedno na izvršavanju podzadatka korisnika. Svaka komponenta protokola doprinosi ovome:

#### Kartica agenta

Slično kao što MCP poslužitelj dijeli popis alata, Agent Card ima:
- Ime agenta.
- **opis općih zadataka** koje ispunjava.
- **popis specifičnih vještina** s opisima koji pomažu drugim agentima (ili čak ljudskim korisnicima) razumjeti kada i zašto bi željeli pozvati tog agenta.
- **trenutni URL krajnje točke** agenta
- **verziju** i **sposobnosti** agenta kao što su odgovori u streamingu i push notifikacije.

#### Izvršitelj agenta

Izvršitelj agenta odgovoran je za **prenošenje konteksta korisničkog razgovora udaljenom agentu**, jer udaljeni agent treba to za razumijevanje zadatka koji treba izvršiti. U A2A poslužitelju agent koristi vlastiti Large Language Model (LLM) za parsiranje dolaznih zahtjeva i izvršavanje zadataka koristeći vlastite interne alate.

#### Artefakt

Kad udaljeni agent dovrši traženi zadatak, njegov rezultat se stvara kao artefakt. Artefakt **sadrži rezultat rada agenta**, **opis onoga što je dovršeno** i **tekstualni kontekst** koji se šalje kroz protokol. Nakon slanja artefakta, veza s udaljenim agentom se zatvara dok ponovno ne bude potrebna.

#### Red događaja

Ova komponenta se koristi za **upravljanje ažuriranjima i slanjem poruka**. Posebno je važna u produkciji agentičkih sustava kako bi se spriječilo zatvaranje veze između agenata prije nego što se zadatak dovrši, što je bitno kod zadataka s duljim trajanjem.

### Prednosti A2A

• **Poboljšana suradnja**: Omogućuje agentima iz različitih dobavljača i platformi da međusobno komuniciraju, dijele kontekst i rade zajedno, što olakšava besprijekornu automatizaciju preko tradicionalno nepovezanih sustava.

• **Fleksibilnost izbora modela**: Svaki A2A agent može odlučiti koji LLM koristi za obradu zahtjeva, dopuštajući optimizirane ili fino podešene modele po agentu, za razliku od jedne LLM veze u nekim MCP scenarijima.

• **Ugrađena autentifikacija**: Autentifikacija je integrirana izravno u A2A protokol, pružajući robustan sigurnosni okvir za interakcije agenata.

### Primjer A2A

![A2A Diagram](../../../translated_images/hr/A2A-Diagram.8666928d648acc26.webp)

Proširimo naš scenarij rezervacije putovanja, ali ovaj put koristeći A2A.

1. **Korisnički zahtjev Multi-agentu**: Korisnik komunicira s A2A klijentom/agenta "Putnički agent", možda rekavši: "Molim te rezerviraj cjelokupno putovanje u Honolulu za sljedeći tjedan, uključujući letove, hotel i najam auta."

2. **Orkestracija od strane putničkog agenta**: Putnički agent prima ovaj složeni zahtjev. Koristi svoj LLM da razmotri zadatak i utvrdi da treba komunicirati s drugim specijaliziranim agentima.

3. **Međusobna komunikacija agenata**: Putnički agent koristi A2A protokol za povezivanje s downstream agentima, kao što su "Agent aviokompanije", "Hotel agent" i "Agent za najam auta" koje su kreirale različite tvrtke.

4. **Delegiranje izvršenja zadatka**: Putnički agent šalje specifične zadatke tim specijaliziranim agentima (npr. "Pronađi letove za Honolulu," "Rezerviraj hotel," "Iznajmi auto"). Svaki od tih specijaliziranih agenata, koristeći vlastite LLM-ove i alate (koji sami mogu biti MCP poslužitelji), izvršava svoj dio rezervacije.

5. **Konsolidirani odgovor**: Kad svi downstream agenti završavaju svoje zadatke, Putnički agent sastavlja rezultate (detalje leta, potvrdu hotela, rezervaciju auta) i šalje opširan odgovor u chat stilu korisniku.

## Prirodni jezični web (NLWeb)

Web stranice su već dugo glavni način za korisnike da pristupe informacijama i podacima preko interneta.

Pogledajmo različite komponente NLWeba, njegove prednosti i primjer kako naš NLWeb radi kroz našu aplikaciju za putovanja.

### Komponente NLWeba

- **NLWeb aplikacija (jezgra servisnog koda)**: Sustav koji obrađuje pitanja na prirodnom jeziku. Povezuje različite dijelove platforme za kreiranje odgovora. Možemo ga smatrati **motorom koji pokreće funkcije prirodnog jezika** web stranice.

- **NLWeb protokol**: To je **osnovni skup pravila za interakciju prirodnim jezikom** sa web stranicom. Vraća odgovore u JSON formatu (često koristeći Schema.org). Njegova svrha je stvoriti osnovu za "AI web", slično kao što je HTML omogućio dijeljenje dokumenata online.

- **MCP poslužitelj (Model Context Protocol endpoint)**: Svaka NLWeb instalacija također radi kao **MCP poslužitelj**. To znači da može **dijeliti alate (poput metode "ask") i podatke** s drugim AI sustavima. U praksi, to omogućuje AI agentima korištenje sadržaja i sposobnosti web stranice, čineći stranicu dijelom šire "agent ekosustava."

- **Embedding modeli**: Ovi modeli se koriste za **pretvorbu sadržaja web stranice u numeričke reprezentacije zvane vektori** (embeddinge). Ti vektori hvataju značenje na način koji računala mogu uspoređivati i pretraživati. Spremaju se u posebnu bazu podataka, a korisnici mogu izabrati koji embedding model žele koristiti.

- **Vektorska baza podataka (mehanizam pretraživanja)**: Ova baza pohranjuje embedinge sadržaja web stranice. Kad netko postavi pitanje, NLWeb provjerava vektorsku bazu kako bi brzo našao najrelevantnije informacije. Daje brzi popis mogućih odgovora, rangiranih prema sličnosti. NLWeb radi s različitim sustavima za pohranu vektora kao što su Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb na primjeru

![NLWeb](../../../translated_images/hr/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovno razmotrimo našu web stranicu za rezervacije putovanja, ali ovaj put pokreće ju NLWeb.

1. **Unos podataka**: Postojeći katalozi proizvoda na stranici (npr. popisi letova, opisi hotela, ponude tura) formatirani su korištenjem Schema.org ili učitani putem RSS feedova. NLWeb alati obrađuju ove strukturirane podatke, stvaraju embeddinge i spremaju ih u lokalnu ili udaljenu vektorsku bazu.

2. **Upit na prirodnom jeziku (čovjek)**: Korisnik posjeti web stranicu i umjesto da navigira izbornicima, upisuje u chat sučelje: "Pronađi mi hotel prilagođen obiteljima u Honoluluu s bazenom za sljedeći tjedan."

3. **Obrada NLWeba**: NLWeb aplikacija prima taj upit. Šalje upit LLM-u za razumijevanje i istovremeno pretražuje svoju vektorsku bazu za relevantne ponude hotela.

4. **Točni rezultati**: LLM pomaže interpretirati rezultate pretraživanja iz baze, identificira najbolje podudarnosti temeljene na kriterijima "prilagođen obiteljima", "bazen" i "Honolulu", te zatim formatira odgovor na prirodnom jeziku. Bitno je da odgovor upućuje na stvarne hotele iz kataloga stranice, izbjegavajući izmišljene podatke.

5. **Interakcija AI agenta**: Budući da NLWeb djeluje kao MCP poslužitelj, vanjski AI agent za putovanja mogao bi se spojiti na ovu NLWeb instancu web stranice. AI agent bi onda mogao koristiti MCP metodu `ask` za direktno postavljanje pitanja web stranici: `ask("Postoje li veganske preporučene restorane u području Honolulu koje hotel preporučuje?")`. NLWeb instanca bi to obradila, koristeći bazu podataka o restoranima (ako je učitana), i vratila strukturirani JSON odgovor.

### Imate li dodatnih pitanja o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici za susrete s drugim učenicima, prisustvovanje satima za konzultacije i dobivanje odgovora na pitanja o AI agentima.

## Resursi

- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Prethodna lekcija

[AI agenti u produkciji](../10-ai-agents-production/README.md)

## Sljedeća lekcija

[Inženjerstvo konteksta za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->