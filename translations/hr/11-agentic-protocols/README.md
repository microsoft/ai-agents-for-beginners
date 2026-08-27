# Korištenje agentskih protokola (MCP, A2A i NLWeb)

[![Agentski protokoli](../../../translated_images/hr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na gornju sliku da biste pogledali video ove lekcije)_

Kako raste upotreba AI agenata, tako raste i potreba za protokolima koji osiguravaju standardizaciju, sigurnost i podržavaju otvorene inovacije. U ovoj lekciji, pokrit ćemo 3 protokola koja nastoje zadovoljiti ovu potrebu - Model Context Protocol (MCP), Agent to Agent (A2A) i Natural Language Web (NLWeb).

## Uvod

U ovoj lekciji ćemo pokriti:

• Kako **MCP** omogućuje AI agentima pristup vanjskim alatima i podacima za dovršavanje korisničkih zadataka.

• Kako **A2A** omogućuje komunikaciju i suradnju između različitih AI agenata.

• Kako **NLWeb** donosi sučelja prirodnog jezika na bilo koju web stranicu omogućavajući AI agentima da otkriju i komuniciraju s sadržajem.

## Ciljevi učenja

• **Prepoznati** osnovnu svrhu i prednosti MCP-a, A2A i NLWeb-a u kontekstu AI agenata.

• **Objasniti** kako svaki protokol olakšava komunikaciju i interakciju između LLM-ova, alata i drugih agenata.

• **Prepoznati** različite uloge koje svaki protokol ima u izgradnji složenih agentskih sustava.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvoreni standard koji pruža standardizirani način da aplikacije pružaju kontekst i alate LLM-ovima. Ovo omogućuje "univerzalni prilagodnik" za različite izvore podataka i alate na koje se AI agenti mogu povezati na dosljedan način.

Pogledajmo komponente MCP-a, prednosti u usporedbi s direktnim korištenjem API-ja i primjer kako bi AI agenti mogli koristiti MCP poslužitelj.

### Osnovne komponente MCP-a

MCP radi na **klijent-poslužitelj arhitekturi**, a osnovne komponente su:

• **Domaćini (Hosts)** su LLM aplikacije (na primjer uređivač koda poput VSCode) koje uspostavljaju veze s MCP poslužiteljem.

• **Klijenti (Clients)** su komponente unutar domaćinske aplikacije koje održavaju veze jedan-na-jedan s poslužiteljima.

• **Poslužitelji (Servers)** su lagani programi koji izlažu određene mogućnosti.

U protokolu su uključene tri osnovne primitivne funkcije koje su sposobnosti MCP poslužitelja:

• **Alati**: To su pojedinačne radnje ili funkcije koje AI agent može pozvati za izvršavanje zadatka. Na primjer, vremenska služba može izložiti alat "dohvati vremensku prognozu", ili e-trgovina može izložiti alat "kupi proizvod". MCP poslužitelji oglašavaju ime alata, opis i ulazno/izlaznu shemu u svom popisu mogućnosti.

• **Resursi**: To su podatci ili dokumenti samo za čitanje koje MCP poslužitelj može pružiti, a klijenti ih mogu preuzeti po potrebi. Primjeri uključuju sadržaj datoteka, zapise u bazi podataka ili zapisničke datoteke. Resursi mogu biti tekstualni (poput koda ili JSON-a) ili binarni (poput slika ili PDF-ova).

• **Upute (Prompts)**: To su unaprijed definirani predlošci koji pružaju predložene upite, dopuštajući složenije tijekove rada.

### Prednosti MCP-a

MCP nudi značajne prednosti za AI agente:

• **Dinamično otkrivanje alata**: Agenti mogu dinamički primiti popis dostupnih alata od poslužitelja zajedno s opisima što ti alati rade. Ovo se razlikuje od tradicionalnih API-ja koji često zahtijevaju statički kod za integracije, što znači da svaka promjena API-ja zahtijeva ažuriranje koda. MCP nudi pristup "integriraj jednom", što vodi većoj prilagodljivosti.

• **Interoperabilnost između različitih LLM-ova**: MCP radi preko različitih LLM-ova, pružajući fleksibilnost za promjenu osnovnih modela radi bolje izvedbe.

• **Standardizirana sigurnost**: MCP uključuje standardiziranu metodu autentikacije, poboljšavajući skalabilnost prilikom dodavanja pristupa dodatnim MCP poslužiteljima. To je jednostavnije nego upravljanje različitim ključevima i vrstama autentikacije za različite tradicionalne API-je.

### Primjer MCP-a

![MCP dijagram](../../../translated_images/hr/mcp-diagram.e4ca1cbd551444a1.webp)

Zamislimo da korisnik želi rezervirati let koristeći AI asistenta koji koristi MCP.

1. **Povezivanje**: AI asistent (MCP klijent) povezuje se na MCP poslužitelj aviokompanije.

2. **Otkrivanje alata**: Klijent pita MCP poslužitelj aviokompanije: "Koje alate imate dostupne?" Poslužitelj odgovara alatima poput "pretraži letove" i "rezerviraj letove".

3. **Pozivanje alata**: Zatim korisnik pita AI asistenta: "Molim te pretraži let iz Portlanda za Honolulu." AI asistent, koristeći svoj LLM, identificira da treba pozvati alat "pretraži letove" i prosljeđuje relevantne parametre (polazište, odredište) MCP poslužitelju.

4. **Izvršenje i odgovor**: MCP poslužitelj, koji djeluje kao omotač, poziva internu rezervacijsku API aviokompanije. Zatim prima informacije o letu (npr. JSON podatke) i vraća ih AI asistentu.

5. **Daljnja interakcija**: AI asistent prikazuje opcije leta. Kada korisnik odabere let, asistent može pozvati alat "rezerviraj let" na istom MCP poslužitelju i time dovršiti rezervaciju.

## Protokol agent-agent (A2A)

Dok se MCP fokusira na povezivanje LLM-a s alatima, **Agent-to-Agent (A2A) protokol** ide korak dalje omogućujući komunikaciju i suradnju između različitih AI agenata. A2A povezuje AI agente preko različitih organizacija, okruženja i tehnoloških stogova kako bi dovršili zajednički zadatak.

Pregledat ćemo komponente i prednosti A2A te primjer kako se može primijeniti u našoj aplikaciji za putovanja.

### Osnovne komponente A2A

A2A se fokusira na omogućavanje komunikacije između agenata i njihovu suradnju na dovršavanju dijela korisničkog zadatka. Svaka komponenta protokola doprinosi tome:

#### Kartica agenta (Agent Card)

Slično kao što MCP poslužitelj dijeli popis alata, Kartica agenta sadrži:
- Ime agenta.
- **opis općih zadataka** koje obavlja.
- **popis specifičnih vještina** s opisima koji pomažu drugim agentima (ili čak ljudskim korisnicima) da razumiju kada i zašto bi željeli pozvati tog agenta.
- **trenutni URL krajnje točke** agenta.
- **verziju** i **mogućnosti** agenta poput streaming odgovora i push obavijesti.

#### Izvršitelj agenta (Agent Executor)

Izvršitelj agenta odgovoran je za **prosljeđivanje konteksta korisničkog chata udaljenom agentu**, koji to treba za razumijevanje zadatka koji treba biti dovršen. U A2A poslužitelju, agent koristi vlastiti Large Language Model (LLM) za parsiranje dolaznih zahtjeva i izvršavanje zadataka koristeći svoje interne alate.

#### Artefakt

Nakon što udaljeni agent dovrši traženi zadatak, njegov izlaz nastaje kao artefakt. Artefakt **sadrži rezultat rada agenta**, **opis onoga što je dovršeno** i **tekstualni kontekst** koji se šalje kroz protokol. Nakon slanja artefakta, veza s udaljenim agentom se zatvara dok se ponovno ne zatreba.

#### Red čekanja događaja (Event Queue)

Ova komponenta se koristi za **rukovanje ažuriranjima i prosljeđivanje poruka**. Posebno je važna u produkciji agentskih sustava kako bi se spriječilo zatvaranje veze između agenata prije završetka zadatka, osobito jer završetak zadatka može trajati dulje vrijeme.

### Prednosti A2A

• **Poboljšana suradnja**: Omogućuje agentima različitih dobavljača i platformi da međusobno komuniciraju, dijele kontekst i surađuju, olakšavajući besprijekornu automatizaciju preko tradicionalno nepovezanih sustava.

• **Fleksibilnost odabira modela**: Svaki A2A agent može odlučiti koji LLM koristi za usluživanje svojih zahtjeva, omogućujući optimizirane ili prilagođene modele po agentu, za razliku od jednog LLM-a u nekim MCP scenarijima.

• **Integrirana autentikacija**: Autentikacija je izravno integrirana u A2A protokol, pružajući robusni sigurnosni okvir za interakcije agenata.

### Primjer A2A

![A2A dijagram](../../../translated_images/hr/A2A-Diagram.8666928d648acc26.webp)

Proširimo naš scenarij rezervacije putovanja, ali ovoga puta koristeći A2A.

1. **Korisnički zahtjev prema multi-agentu**: Korisnik komunicira s "Agentom za putovanja" A2A klijentom/agentom, primjerice govoreći: "Molim te rezerviraj čitavo putovanje u Honolulu za sljedeći tjedan, uključujući letove, hotel i najam automobila".

2. **Orkestracija od strane agenta za putovanja**: Agent za putovanja prima ovaj složeni zahtjev. Koristi svoj LLM da razmisli o zadatku i utvrdi da mora komunicirati s drugim specijaliziranim agentima.

3. **Komunikacija između agenata**: Agent za putovanja koristi A2A protokol za povezivanje s nižim agentima, poput "Agenta aviokompanije", "Agenta hotela" i "Agenta za najam automobila" koje su kreirale različite tvrtke.

4. **Delegirano izvršavanje zadataka**: Agent za putovanja šalje specifične zadatke tim specijaliziranim agentima (npr. "Pronađi letove za Honolulu", "Rezerviraj hotel", "Iznajmi automobil"). Svaki od tih specijaliziranih agenata, koristeći vlastite LLM-ove i vlastite alate (koji također mogu biti MCP poslužitelji), obavlja svoj specifični dio rezervacije.

5. **Konsolidirani odgovor**: Kada svi niži agenti dovrše svoje zadatke, Agent za putovanja sastavlja rezultate (detalji leta, potvrda hotela, rezervacija automobila) i šalje sveobuhvatan, chat-stil odgovor korisniku.

## Natural Language Web (NLWeb)

Web stranice već dugo vremena su primarni način na koji korisnici pristupaju informacijama i podacima na internetu.

Pogledajmo različite komponente NLWeb-a, njegove prednosti i primjer kako naš NLWeb funkcionira na primjeru naše aplikacije za putovanja.

### Komponente NLWeb-a

- **NLWeb aplikacija (Core Service Code)**: Sustav koji obrađuje pitanja prirodnog jezika. Povezuje različite dijelove platforme za stvaranje odgovora. Možete ga smatrati **motorom koji pokreće značajke prirodnog jezika** web stranice.

- **NLWeb protokol**: Osnovni skup pravila za interakciju prirodnim jezikom sa web stranicom. Vraća odgovore u JSON formatu (često koristeći Schema.org). Njegova svrha je stvoriti jednostavnu osnovu za "AI Web", na isti način na koji je HTML omogućio dijeljenje dokumenata online.

- **MCP poslužitelj (Model Context Protocol endpoint)**: Svaka NLWeb instalacija također radi kao **MCP poslužitelj**. To znači da može **dijeliti alate (poput metode "ask") i podatke** s drugim AI sustavima. U praksi, to omogućava da sadržaj i mogućnosti web stranice budu korisni AI agentima, čime stranica postaje dio šire "agentske ekosfere".

- **Embedding modeli**: Ti modeli se koriste za **pretvaranje sadržaja web stranice u numeričke prikaze zvane vektori** (embeddingi). Ti vektori hvataju značenje na način koji računala mogu uspoređivati i pretraživati. Spremaju se u posebnu bazu podataka, a korisnici mogu odabrati koji embedding model žele koristiti.

- **Vektorska baza podataka (mehanizam za dohvat)**: Ova baza podataka **pohranjuje embeddinge sadržaja web stranice**. Kada netko postavi pitanje, NLWeb provjerava vektorsku bazu podataka kako bi brzo pronašao najrelevantnije informacije. Daje brz popis mogućih odgovora, rangiranih prema sličnosti. NLWeb radi s različitim sustavima za pohranu vektora kao što su Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb po primjeru

![NLWeb](../../../translated_images/hr/nlweb-diagram.c1e2390b310e5fe4.webp)

Ponovo razmotrimo naš web za rezervaciju putovanja, ali ovoga puta pokreće ga NLWeb.

1. **Unos podataka**: Postojeći katalozi proizvoda na web stranici za putovanja (npr. popisi letova, opisi hotela, paketi tura) formatirani su pomoću Schema.org ili učitani putem RSS feedova. Alati NLWeb-a unose te strukturirane podatke, stvaraju embeddinge i pohranjuju ih u lokalnu ili udaljenu vektorsku bazu podataka.

2. **Upit prirodnim jezikom (osoba)**: Korisnik posjećuje web stranicu i umjesto da pretražuje izbornike, upisuje u chat sučelje: "Nađi mi obiteljski hotel u Honoluluu s bazenom za sljedeći tjedan".

3. **Obrada NLWeb-a**: NLWeb aplikacija prima ovaj upit. Šalje upit LLM-u za razumijevanje i istovremeno pretražuje svoju vektorsku bazu podataka za relevantne ponude hotela.

4. **Točni rezultati**: LLM pomaže interpretirati rezultate pretrage iz baze podataka, identificirati najbolje podudarnosti na temelju kriterija "prikladan za obitelji", "bazena" i "Honolulu", a zatim oblikuje odgovor na prirodnom jeziku. Ključno je da odgovor referira stvarne hotele iz kataloga web stranice, izbjegavajući izmišljene informacije.

5. **Interakcija AI agenta**: Budući da NLWeb djeluje kao MCP poslužitelj, vanjski AI agent za putovanja također bi se mogao povezati s ovom NLWeb instancom web stranice. AI agent bi tada mogao koristiti MCP metodu `ask` za ostvarenje izravnog upita web stranici: `ask("Postoje li u području Honolulua bilo kakvi restorani prilagođeni veganima koje hotel preporučuje?")`. NLWeb instanca bi to obradila iskorištavajući svoju bazu podataka o restoranima (ako je učitana) i vratila strukturirani JSON odgovor.

### Imate li još pitanja o MCP/A2A/NLWeb?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici gdje možete upoznati druge učenike, sudjelovati na radnim satima i dobiti odgovore na pitanja o AI agentima.

## Resursi

- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitorij](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Prethodna lekcija

[AI agenti u produkciji](../10-ai-agents-production/README.md)

## Sljedeća lekcija

[Kontekstualno inženjerstvo za AI agente](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->