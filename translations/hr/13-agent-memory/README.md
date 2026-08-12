# Memorija za AI agente 
[![Agent Memory](../../../translated_images/hr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kada govorimo o jedinstvenim prednostima stvaranja AI agenata, uglavnom su dvije stvari u fokusu: sposobnost pozivanja alata za izvršavanje zadataka i sposobnost poboljšavanja tijekom vremena. Memorija je temelj za stvaranje samopoboljšavajućeg agenta koji može stvarati bolje korisničke doživljaje.

U ovoj lekciji istražit ćemo što je memorija za AI agente i kako je možemo upravljati i koristiti za dobrobit naših aplikacija.

## Uvod

Ova lekcija će obuhvatiti:

• **Razumijevanje memorije AI agenata**: Što je memorija i zašto je važna za agente.

• **Implementacija i spremanje memorije**: Praktične metode dodavanja memorijskih sposobnosti vašim AI agentima, fokusirajući se na kratkotrajnu i dugotrajnu memoriju.

• **Kako AI agenti postaju samopoboljšavajući**: Kako memorija omogućuje agentima učenje iz prošlih interakcija i napredovanje tijekom vremena.

## Dostupne implementacije

Ova lekcija uključuje dva sveobuhvatna tutoriala u bilježnici:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira memoriju koristeći Mem0 i Azure AI Search s Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiranu memoriju koristeći Cognee, automatski gradeći graf znanja podržan embeddingima, vizualizirajući graf i inteligentno dohvaćanje

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete kako:

• **Razlikovati različite vrste memorije AI agenata**, uključujući radnu, kratkotrajnu i dugotrajnu memoriju, kao i specijalizirane oblike poput memorije ličnosti i epizodne memorije.

• **Implementirati i upravljati kratkoročnom i dugoročnom memorijom za AI agente** koristeći Microsoft Agent Framework, koristeći alate poput Mem0, Cognee, memoriju bijele ploče i integraciju s Azure AI Searchom.

• **Razumjeti principe iza samopoboljšavajućih AI agenata** i kako robusni sustavi upravljanja memorijom doprinose kontinuiranom učenju i prilagodbi.

## Razumijevanje memorije AI agenata

U svojoj biti, **memorija za AI agente odnosi se na mehanizme koji im omogućuju zadržavanje i prisjećanje informacija**. Te informacije mogu biti specifični detalji o razgovoru, korisničke preferencije, prošle radnje ili čak naučeni obrasci.

Bez memorije, AI aplikacije često su bezstanja, što znači da svaka interakcija započinje od nule. To dovodi do ponavljajućeg i frustrirajućeg korisničkog iskustva gdje agent "zaboravlja" prethodni kontekst ili preferencije.

### Zašto je memorija važna?

Inteligencija agenta duboko je povezana s njegovom sposobnošću prisjećanja i korištenja prošlih informacija. Memorija omogućuje agentima da budu:

• **Refleksivni**: Učenje iz prošlih radnji i ishoda.

• **Interaktivni**: Održavanje konteksta tijekom tekućeg razgovora.

• **Proaktivni i reaktivni**: Predviđanje potreba ili odgovaranje prikladno temeljem povijesnih podataka.

• **Autonomni**: Samostalnije djelovanje crpeći iz pohranjena znanja.

Cilj implementacije memorije je učiniti agente pouzdanijima i sposobnijima.

### Vrste memorije

#### Radna memorija

Zamislite je kao komad papira za bilješke kojeg agent koristi tijekom jedne, tekuće zadaće ili misaonog procesa. Drži neposredne informacije potrebne za izračun sljedećeg koraka.

Za AI agente, radna memorija često bilježi najrelevantnije informacije iz razgovora, čak i ako je cijela povijest chata dugačka ili skraćena. Fokusira se na izdvajanje ključnih elemenata poput zahtjeva, prijedloga, odluka i radnji.

**Primjer radne memorije**

U agentu za rezervaciju putovanja, radna memorija može bilježiti trenutni zahtjev korisnika, poput "Želim rezervirati putovanje u Pariz". Taj specifični zahtjev se drži u neposrednom kontekstu agenta kako bi vodio trenutnu interakciju.

#### Kratkoročna memorija

Ova vrsta memorije zadržava informacije tijekom trajanja pojedinačnog razgovora ili sesije. To je kontekst trenutnog chata, što omogućuje agentu da se pozove na prethodne dijelove dijaloga.

U primjerima [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-a, to se mapira na `AgentSession`, koji se kreira s `agent.create_session()`. Sesija je ugrađena kratkoročna memorija frameworka: čuva kontekst razgovora dostupan dok se ista sesija ponovno koristi, ali taj kontekst se ne pohranjuje kada sesija završi ili se aplikacija ponovno pokrene. Za činjenice i preferencije koje trebaju preživjeti više sesija, koristite dugoročnu memoriju, obično putem baze podataka, vektorskog indeksa ili drugog trajnog spremišta.

**Primjer kratkoročne memorije**

Ako korisnik pita, "Koliko bi koštao let za Pariz?" i potom nastavi s "A što je s smještajem tamo?", kratkoročna memorija osigurava da agent zna da se "tamo" odnosi na "Pariz" unutar istog razgovora.

#### Dugoročna memorija

Ovo su informacije koje traju kroz više razgovora ili sesija. Omogućuje agentima da pamte korisničke preferencije, povijesne interakcije ili općenito znanje tijekom dužeg vremena. Važno je za personalizaciju.

**Primjer dugoročne memorije**

Dugoročna memorija može pohraniti da "Ben uživa u skijanju i aktivnostima na otvorenom, voli kavu s pogledom na planinu i želi izbjegavati napredne skijaške staze zbog prošle ozljede". Te informacije, naučene iz prethodnih interakcija, utječu na preporuke u budućim sesijama planiranja putovanja čineći ih izrazito personaliziranima.

#### Memorija ličnosti (Persona)

Ova specijalizirana vrsta memorije pomaže agentu razviti dosljednu "osobnost" ili "personu". Omogućuje agentu da pamti detalje o sebi ili svojoj namijenjenoj ulozi, čineći interakcije fluidnijima i usmjerenijima.

**Primjer memorije ličnosti**
Ako je agent za putovanja dizajniran kao "stručni planer za skijanje", memorija ličnosti može pojačati ovu ulogu, utječući na njegove odgovore da budu u skladu s tonom i znanjem stručnjaka.

#### Radni tok/Epizodna memorija

Ova memorija pohranjuje niz koraka koje agent poduzima tijekom složenog zadatka, uključujući uspjehe i neuspjehe. To je kao sjećanje na određene "epizode" ili prošla iskustva kako bi se iz njih učilo.

**Primjer epizodne memorije**

Ako je agent pokušao rezervirati određeni let, ali je to propalo zbog nedostupnosti, epizodna memorija može zabilježiti ovaj neuspjeh, dopuštajući agentu da pokuša alternativne letove ili obavijesti korisnika o problemu na informiraniji način pri sljedećem pokušaju.

#### Memorija entiteta

Ovo uključuje izdvajanje i pamćenje specifičnih entiteta (poput ljudi, mjesta ili stvari) i događaja iz razgovora. Omogućuje agentu da izgradi strukturirano razumijevanje ključnih elemenata o kojima se raspravljalo.

**Primjer memorije entiteta**

Iz razgovora o prošlom putovanju, agent može izdvojiti "Pariz," "Eiffelov toranj" i "večera u restoranu Le Chat Noir" kao entitete. U budućoj interakciji, agent može zapamtiti "Le Chat Noir" i ponuditi da napravi novu rezervaciju tamo.

#### Strukturirani RAG (Retrieval Augmented Generation)

Iako je RAG šira tehnika, "Strukturirani RAG" je istaknut kao moćna memorijska tehnologija. Izvlači gusto, strukturirano znanje iz raznih izvora (razgovora, e-pošte, slika) i koristi ga za poboljšanje preciznosti, prisjećanja i brzine u odgovorima. Za razliku od klasičnog RAG-a koji se oslanja isključivo na semantičku sličnost, Strukturirani RAG radi s unutarnjom strukturom informacija.

**Primjer strukturiranog RAG-a**

Umjesto samo podudaranja ključnih riječi, Strukturirani RAG može rastaviti detalje leta (odredište, datum, vrijeme, aviokompanija) iz e-pošte i pohraniti ih na strukturiran način. To omogućava precizna upite poput "Koji let sam rezervirao za Pariz u utorak?"

## Implementacija i pohrana memorije

Implementacija memorije za AI agente uključuje sustavni proces **upravljanja memorijom**, koji uključuje generiranje, pohranu, dohvaćanje, integraciju, ažuriranje i čak "zaboravljanje" (ili brisanje) informacija. Dohvaćanje je osobito važan aspekt.

### Specijalizirani memorijski alati

#### Mem0

Jedan od načina za pohranu i upravljanje memorijom agenta je korištenje specijaliziranih alata poput Mem0. Mem0 funkcionira kao sloj trajne memorije, omogućujući agentima da se prisjete relevantnih interakcija, pohranjuju korisničke preferencije i činjenice, te uče iz uspjeha i neuspjeha tijekom vremena. Ideja je pretvoriti agente bez stanja u one sa stanjem.

Radi kroz **dvofazni memorijski proces: ekstrakciju i ažuriranje**. Prvo, poruke dodane u nit agenta šalju se Mem0 servisu, koji koristi Veliki jezični model (LLM) za sažimanje povijesti razgovora i izdvajanje novih memorija. Nakon toga, faza ažuriranja vođena LLM-om odlučuje hoće li se te memorije dodati, izmijeniti ili izbrisati, pohranjujući ih u hibridni podatkovni spremnik koji može uključivati vektorske, grafičke i baze s ključem-vrijednošću. Ovaj sustav također podržava različite vrste memorije i može uključiti graf memoriju za upravljanje odnosima između entiteta.

#### Cognee

Drugi moćan pristup je korištenje **Cognee**, otvorenog izvora semantičke memorije za AI agente koji pretvara strukturirane i nestrukturirane podatke u upitne grafove znanja podržane embeddingima. Cognee pruža **dvoslojnu arhitekturu** koja kombinira pretraživanje vektorske sličnosti s grafičkim odnosima, omogućujući agentima da razumiju ne samo koje su informacije slične, već i kako su koncepti povezani.

Izvrsno je u **hibridnom dohvaćanju** koje kombinira vektorsku sličnost, grafičku strukturu i LLM rezoniranje – od sirovog pretraživanja fragmenta do odgovaranja na pitanja svjesnog grafa. Sustav održava **živu memoriju** koja se razvija i raste dok ostaje upitna kao jedan povezani graf, podupirući kako kratkoročni kontekst sesije, tako i dugoročnu trajnu memoriju.

Tutorijal u bilježnici Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrira izgradnju ovog jedinstvenog sloja memorije, s praktičnim primjerima unos različitih izvora podataka, vizualizacije grafa znanja i upita s različitim strategijama pretraživanja prilagođenima potrebama agenta.

### Pohrana memorije s RAG-om

Osim specijaliziranih memorijskih alata poput Mem0, možete iskoristiti robusne usluge pretraživanja poput **Azure AI Search kao pozadinu za pohranu i dohvat memorija**, osobito za strukturirani RAG.

To vam omogućuje da ukorijenite odgovore svog agenta u vlastite podatke, osiguravajući relevantnije i točnije odgovore. Azure AI Search može se koristiti za pohranu korisničkih memorija o putovanjima, kataloge proizvoda ili bilo koje drugo domensko znanje.

Azure AI Search podržava mogućnosti poput **Strukturiranog RAG-a**, koji izvrsno izvlači i dohvaća gusto, strukturirano znanje iz velikih skupova podataka kao što su povijesti razgovora, e-pošte ili čak slike. To pruža "superljudsku preciznost i prisjećanje" u usporedbi s tradicionalnim pristupima razlaganju teksta i embeddingom.

## Kako AI agenti postaju samopoboljšavajući

Uobičajeni obrazac za samopoboljšavajuće agente uključuje uvođenje **"agenta znanja"**. Ovaj zasebni agent promatra glavni razgovor između korisnika i primarnog agenta. Njegova uloga je:

1. **Identificirati vrijedne informacije**: Odlučiti je li dio razgovora vrijedan spremanja kao opće znanje ili specifična korisnička preferencija.

2. **Izvlačenje i sažimanje**: Destilirati bitno učenje ili preferenciju iz razgovora.

3. **Spremanje u bazu znanja**: Trajno pohraniti izdvojene informacije, često u vektorsku bazu podataka, kako bi se mogle kasnije dohvatiti.

4. **Nadopuna budućih upita**: Kada korisnik pokrene novi upit, agent znanja dohvaća relevantne pohranjene informacije i dodaje ih u korisnički upit, pružajući ključni kontekst primarnom agentu (slično RAG-u).

### Optimizacije za memoriju

• **Upravljanje latencijom**: Kako ne bi usporavali korisničke interakcije, može se koristiti jeftiniji, brži model za početnu brzu provjeru je li informacija vrijedna za spremanje ili dohvat, pri čemu se složeniji proces ekstrakcije/dohvata aktivira samo po potrebi.

• **Održavanje baze znanja**: Za rastuću bazu znanja, rjeđe korištene informacije mogu se premjestiti u "hladnu pohranu" radi upravljanja troškovima.

## Imate li dodatnih pitanja o memoriji agenata?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, sudjelujete na radnim satima i dobijete odgovore na svoja pitanja o AI agentima.
## Prethodna lekcija

[Inženjering konteksta za AI agente](../12-context-engineering/README.md)

## Sljedeća lekcija

[Istraživanje Microsoft Agent Frameworka](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->