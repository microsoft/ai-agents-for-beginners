# Memorija za AI agente  
[![Agent Memory](../../../translated_images/hr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kada se raspravlja o jedinstvenim koristima stvaranja AI agenata, uglavnom se raspravlja o dvije stvari: sposobnosti pozivanja alata za izvršenje zadataka i sposobnosti poboljšavanja tijekom vremena. Memorija je temelj stvaranja samopoboljšavajućeg agenta koji može kreirati bolje doživljaje za naše korisnike.

U ovom ćemo se poglavlju osvrnuti na to što je memorija za AI agente i kako je možemo upravljati i koristiti u korist naših aplikacija.

## Uvod

Ovo poglavlje pokriva:

• **Razumijevanje memorije AI agenta**: Što je memorija i zašto je važna za agente.

• **Implementacija i pohrana memorije**: Praktične metode za dodavanje sposobnosti memorije vašim AI agentima, s naglaskom na kratkoročnu i dugoročnu memoriju.

• **Samopoboljšavajući se AI agenti**: Kako memorija omogućuje agentima učenje iz prošlih interakcija i poboljšavanje tijekom vremena.

## Dostupne implementacije

Ovo poglavlje uključuje dva opsežna vodiča u bilježnicama:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira memoriju koristeći Mem0 i Azure AI Search s Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiranu memoriju koristeći Cognee, automatski gradi graf znanja potpomognut ugrađivanjima, vizualizira graf i inteligentno dohvaća informacije

## Ciljevi učenja

Nakon završetka ovog poglavlja, znat ćete kako:

• **Razlikovati različite vrste memorije AI agenta**, uključujući radnu, kratkoročnu i dugoročnu memoriju, kao i specijalizirane oblike poput osobe i epizodne memorije.

• **Implementirati i upravljati kratkoročnom i dugoročnom memorijom za AI agente** koristeći Microsoft Agent Framework, koristeći alate poput Mem0, Cognee, Whiteboard memorije i integraciju s Azure AI Search.

• **Razumjeti principe iza samopoboljšavajućih AI agenata** i kako robusni sustavi upravljanja memorijom doprinose kontinuiranom učenju i prilagodbi.

## Razumijevanje memorije AI agenta

U svojoj srži, **memorija za AI agente odnosi se na mehanizme koji im omogućuju zadržavanje i prisjećanje informacija**. Te informacije mogu biti specifični detalji o razgovoru, korisničkim preferencijama, prošlim radnjama ili čak naučenim obrascima.

Bez memorije, AI aplikacije često su bezstanja, što znači da svaka interakcija započinje od početka. To vodi u ponavljajuće i frustrirajuće korisničko iskustvo u kojem agent "zaboravlja" prethodni kontekst ili preferencije.

### Zašto je memorija važna?

Inteligencija agenta duboko je povezana s njegovom sposobnošću da se prisjeti i iskoristi prošle informacije. Memorija omogućuje agentima da budu:

• **Refleksivni**: Učeći iz prošlih akcija i ishoda.

• **Interaktivni**: Održavajući kontekst tijekom trajanja razgovora.

• **Proaktivni i reaktivni**: Predviđajući potrebe ili primjereno reagirajući na temelju povijesnih podataka.

• **Autonomni**: Djelujući samostalnije oslanjajući se na pohranjeno znanje.

Cilj implementacije memorije je učiniti agente **pouzdanijima i sposobnijima**.

### Vrste memorije

#### Radna memorija

Zamislite to kao komad papira za bilješke koji agent koristi tijekom jednog, tekućeg zadatka ili misaonog procesa. Čuva neposredne informacije potrebne za izračun sljedećeg koraka.

Za AI agente, radna memorija često hvata najvažnije informacije iz razgovora, čak i ako je puna povijest chata dugačka ili skraćena. Fokusira se na izdvajanje ključnih elemenata poput zahtjeva, prijedloga, odluka i radnji.

**Primjer radne memorije**

U agentu za rezervaciju putovanja, radna memorija može zabilježiti trenutni zahtjev korisnika, poput "Želim rezervirati putovanje u Pariz". Ovaj specifični zahtjev se čuva u neposrednom kontekstu agenta da usmjeri trenutnu interakciju.

#### Kratkoročna memorija

Ova vrsta memorije zadržava informacije tijekom trajanja jednog razgovora ili sesije. To je kontekst trenutnog chata, koji omogućuje agentu da se osvrne na prethodne korake u dijalogu.

U uzorcima iz [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK-a, ovo odgovara `AgentSession`, kreiranom s `agent.create_session()`. Sesija je ugrađena kratkoročna memorija okvira: čuva kontekst razgovora dok se ista sesija ponovo koristi, ali taj se kontekst ne sprema kada sesija završi ili aplikacija ponovno pokrene. Za činjenice i preferencije koje trebaju preživjeti preko sesija koristite dugoročnu memoriju, obično putem baze podataka, vektorskog indeksa ili drugog trajnog spremišta.

**Primjer kratkoročne memorije**

Ako korisnik pita: "Koliko košta let do Pariza?" a zatim nastavi s "A što je s smještajem tamo?", kratkoročna memorija osigurava da agent zna da se "tamo" odnosi na "Pariz" u istom razgovoru.

#### Dugoročna memorija

To su informacije koje traju preko više razgovora ili sesija. Omogućuje agentima da se sjećaju korisničkih preferencija, povijesnih interakcija ili općeg znanja tijekom duljeg razdoblja. To je važno za personalizaciju.

**Primjer dugoročne memorije**

Dugoročna memorija može pohraniti da "Ben voli skijanje i aktivnosti na otvorenom, voli kavu s pogledom na planinu i želi izbjeći napredne skijaške staze zbog prošle ozljede". Te informacije, naučene iz prošlih interakcija, utječu na preporuke u budućim planiranjima putovanja, čineći ih vrlo personaliziranim.

#### Memorija osobe (Persona Memory)

Ova specijalizirana vrsta memorije pomaže agentu razviti dosljednu "osobnost" ili "ulogu". Omogućuje agentu da zapamti detalje o sebi ili svojoj namjeri, čineći interakcije fluidnijima i fokusiranijima.

**Primjer memorije osobe**

Ako je agent za putovanja dizajniran da bude "stručni planer skijanja", memorija osobe može ojačati ovu ulogu, utječući na njegove odgovore da odgovaraju tonu i znanju eksperta.

#### Memorija tijeka rada / epizodna memorija

Ova memorija pohranjuje slijed koraka koje agent poduzima tijekom složenog zadatka, uključujući uspjehe i neuspjehe. Kao da se sjeća specifičnih "epizoda" ili prošlih iskustava iz kojih uči.

**Primjer epizodne memorije**

Ako je agent pokušao rezervirati određeni let ali je to propalo zbog nedostupnosti, epizodna memorija može zabilježiti ovaj neuspjeh, dopuštajući agentu da pokuša alternativne letove ili obavijesti korisnika o problemu na informiraniji način prilikom sljedećeg pokušaja.

#### Memorija entiteta

Ovo uključuje izdvajanje i pamćenje specifičnih entiteta (kao ljudi, mjesta ili stvari) i događaja iz razgovora. Omogućuje agentu da izgradi strukturirano razumijevanje ključnih elemenata koji su diskutirani.

**Primjer memorije entiteta**

Iz razgovora o prošlom putovanju, agent može izdvojiti "Pariz", "Eiffelov toranj" i "večera u restoranu Le Chat Noir" kao entitete. U budućoj interakciji agent bi mogao prisjetiti se "Le Chat Noir" i ponuditi novu rezervaciju tamo.

#### Strukturirani RAG (Retrieval Augmented Generation)

Dok je RAG šira tehnika, "Strukturirani RAG" istaknut je kao moćna tehnologija memorije. Izvlači gusto, strukturirano znanje iz različitih izvora (razgovora, e-pošte, slika) i koristi ga za poboljšanje preciznosti, povrata i brzine u odgovorima. Za razliku od klasičnog RAG-a koji se oslanja samo na semantičku sličnost, Strukturirani RAG radi s inherentnom strukturom informacija.

**Primjer strukturiranog RAG-a**

Umjesto da samo podudara ključne riječi, Strukturirani RAG može razložiti detalje leta (odredište, datum, vrijeme, zrakoplovnu tvrtku) iz e-pošte i pohraniti ih na strukturirani način. To omogućuje precizna pitanja poput "Koji let sam rezervirao za Pariz u utorak?"

## Implementacija i pohrana memorije

Implementacija memorije za AI agente uključuje sustavan proces **upravljanja memorijom**, koji uključuje generiranje, pohranu, dohvat, integraciju, ažuriranje i čak "zaboravljanje" (ili brisanje) informacija. Dohvat je posebno važan aspekt.

### Specijalizirani alati za memoriju

#### Mem0

Jedan od načina za pohranu i upravljanje memorijom agenta je korištenje specijaliziranih alata poput Mem0. Mem0 djeluje kao sloj trajne memorije, omogućujući agentima da se prisjećaju relevantnih interakcija, pohranjuju korisničke preferencije i faktualni kontekst te uče iz uspjeha i neuspjeha tijekom vremena. Ideja je da agentski sistemi bez stanja postanu oni sa stanjem.

Radi kroz **dvostupanjski proces memorijskog postupka: izvlačenje i ažuriranje**. Prvo se poruke dodane u nit agenta šalju Mem0 servisu, koji koristi Large Language Model (LLM) za sažimanje povijesti razgovora i izvlačenje novih memorija. Nakon toga, faza ažuriranja koju pokreće LLM određuje treba li dodati, izmijeniti ili izbrisati te memorije, pohranjujući ih u hibridnoj bazi podataka koja može uključivati vektorsku, grafičku i bazu ključ-vrijednost. Sustav također podržava različite vrste memorije i može uključivati graf memorije za upravljanje odnosima između entiteta.

#### Cognee

Drugi moćan pristup je korištenje **Cognee**, open-source semantičke memorije za AI agente koja pretvara strukturirane i nestrukturirane podatke u upitne grafove znanja potpomognute ugradnjama (embeddings). Cognee pruža **dvostruku arhitekturu pohrane** koja kombinira pretraživanje vektorske sličnosti s grafičkim odnosima, omogućujući agentima da razumiju ne samo što je informacija slična, nego i kako su koncepti povezani.

Izvrsno je u **hibridnom pretraživanju** koje spaja vektorsku sličnost, graf strukturu i rezoniranje LLM-om – od sirovog pretraživanja do upita koji su svjesni grafa. Sustav održava **živu memoriju** koja se razvija i raste dok ostaje upitna kao jedan povezani graf, podržavajući i kratkoročni kontekst sesije i dugoročnu trajnu memoriju.

Vodič u Cognee bilježnici ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) pokazuje kako graditi ovaj objedinjeni sloj memorije, s praktičnim primjerima unošenja različitih izvora podataka, vizualizacije grafa znanja i upita s različitim strategijama pretraživanja prilagođenim potrebama agenta.

### Pohrana memorije pomoću RAG-a

Osim specijaliziranih alata poput Mem0, možete koristiti snažne usluge pretraživanja poput **Azure AI Search kao backend za pohranu i dohvat memorija**, osobito za strukturirani RAG.

To vam omogućuje da utemeljite odgovore vašeg agenta na vlastitim podacima, osiguravajući relevantnije i točnije odgovore. Azure AI Search može se koristiti za pohranu korisničkih memorija o putovanjima, katalozima proizvoda ili bilo kojem drugom specifičnom domenskom znanju.

Azure AI Search podržava mogućnosti poput **Strukturiranog RAG-a**, koji izvrsno izvlači i dohvaća gusto, strukturirano znanje iz velikih skupova podataka poput povijesti razgovora, e-pošte ili čak slika. To pruža "natčovječansku preciznost i povrat" u usporedbi s tradicionalnim pristupima dijeljenju teksta i ugradnjama.

## Samopoboljšavanje AI agenata

Uobičajeni obrazac za samopoboljšavajuće agente uključuje uvođenje **"agenta znanja"**. Ovaj odvojeni agent prati glavni razgovor između korisnika i primarnog agenta. Njegova uloga je:

1. **Identificirati vrijedne informacije**: Odrediti je li dio razgovora vrijedan spremanja kao opće znanje ili specifična korisnička preferencija.

2. **Izvući i sažeti**: Pročistiti ključnu lekciju ili preferenciju iz razgovora.

3. **Pohraniti u bazu znanja**: Sačuvati ove informacije, često u vektorsku bazu podataka, kako bi se mogle kasnije dohvatiti.

4. **Nadograditi buduće upite**: Kada korisnik počne novi upit, agent znanja dohvaća relevantne pohranjene informacije i prilaže ih korisnikovom upitu, pružajući ključni kontekst primarnom agentu (slično RAG-u).

### Optimizacije za memoriju

• **Upravljanje kašnjenjem**: Kako se ne bi usporile korisničke interakcije, može se početno koristiti jeftiniji i brži model za brz inspekcijski pregled ima li informacija vrijednost za pohranu ili dohvat, a složeniji proces ekstrakcije/dohvata koristi se samo kada je to potrebno.

• **Održavanje baze znanja**: Za rastuću bazu znanja, rjeđe korištene informacije mogu se premjestiti u "hladnu pohranu" radi upravljanja troškovima.

## Imate li još pitanja o memoriji agenta?

Pridružite se [Microsoft Foundry Discordu](https://aka.ms/ai-agents/discord) da upoznate druge učenike, prisustvujete radnim satima i dobijete odgovore na vaša pitanja o AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->