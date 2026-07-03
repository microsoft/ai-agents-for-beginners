# Memorija za AI agente 
[![Agent Memory](../../../translated_images/hr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Prilikom rasprave o jedinstvenim prednostima stvaranja AI agenata, uglavnom se ističu dvije stvari: sposobnost pozivanja alata za izvršavanje zadataka i sposobnost poboljšanja tijekom vremena. Memorija je temelj za stvaranje samopoboljšavajućeg agenta koji može stvoriti bolje iskustvo za naše korisnike.

U ovoj lekciji pogledat ćemo što je memorija za AI agente te kako je možemo upravljati i koristiti za dobrobit naših aplikacija.

## Uvod

Ova će lekcija obuhvatiti:

• **Razumijevanje memorije AI agenata**: Što je memorija i zašto je bitna za agente.

• **Implementacija i pohrana memorije**: Praktične metode dodavanja mogućnosti memorije vašim AI agentima, s fokusom na kratkoročnu i dugoročnu memoriju.

• **Samopoboljšavajući AI agenti**: Kako memorija omogućuje agentima da uče iz prošlih interakcija i s vremenom se poboljšavaju.

## Dostupne implementacije

Ova lekcija uključuje dva sveobuhvatna tutorijala u obliku bilježnice (notebook):

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira memoriju koristeći Mem0 i Azure AI Search s Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiranu memoriju koristeći Cognee, automatski gradi graf znanja potkrijepljen embeddingsima, vizualizira graf i omogućuje inteligentno dohvaćanje

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

• **Razlikovati različite vrste memorije AI agenata**, uključujući radnu, kratkoročnu i dugoročnu memoriju, kao i specijalizirane oblike poput persona i epizodične memorije.

• **Implementirati i upravljati kratkoročnom i dugoročnom memorijom za AI agente** koristeći Microsoft Agent Framework, iskorištavajući alate poput Mem0, Cognee, Whiteboard memorije i integraciju s Azure AI Searchom.

• **Razumjeti principe samopoboljšavajućih AI agenata** i kako robusni sustavi upravljanja memorijom doprinose kontinuiranom učenju i prilagodbi.

## Razumijevanje memorije AI agenata

Suštinski, **memorija za AI agente odnosi se na mehanizme koji im omogućuju zadržavanje i prisjećanje informacija**. Te informacije mogu biti specifični detalji o razgovoru, korisničke preferencije, prošle radnje ili čak naučeni obrasci.

Bez memorije, AI aplikacije često nemaju stanje, što znači da svaka interakcija počinje od početka. To vodi do ponavljajućeg i frustrirajućeg iskustva za korisnika gdje agent "zaboravlja" prethodni kontekst ili preferencije.

### Zašto je memorija važna?

Inteligencija agenta duboko je povezana s njegovom sposobnošću prisjećanja i korištenja prošlih informacija. Memorija agentima omogućuje da budu:

• **Refleksivni**: Uče iz prošlih radnji i rezultata.

• **Interaktivni**: Održavaju kontekst trajnog razgovora.

• **Proaktivni i reaktivni**: Predviđaju potrebe ili odgovaraju prikladno na temelju povijesnih podataka.

• **Autonomni**: Djeluju samostalnije oslanjajući se na pohranjeno znanje.

Cilj implementacije memorije je učiniti agente **pouzdanijima i sposobnijima**.

### Vrste memorije

#### Radna memorija

Smatrajte to papirom za bilješke koji agent koristi tijekom jednog, tekućeg zadatka ili misaonog procesa. Ona sadržava neposredne informacije potrebne za računanje sljedećeg koraka.

Za AI agente, radna memorija često hvata najrelevantnije informacije iz razgovora, čak i ako je cijela povijest chata duga ili skraćena. Fokusira se na izdvajanje ključnih elemenata poput zahtjeva, prijedloga, odluka i akcija.

**Primjer radne memorije**

U agentu za rezervaciju putovanja, radna memorija može sadržavati trenutni zahtjev korisnika, poput "Želim rezervirati putovanje u Pariz". Taj specifični zahtjev držan je u neposrednom kontekstu agenta kako bi vodio trenutnu interakciju.

#### Kratkoročna memorija

Ova vrsta memorije zadržava informacije tijekom trajanja jednog razgovora ili sesije. To je kontekst trenutnog razgovora, koji agentu omogućuje vraćanje na prethodne dijelove dijaloga.

U [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK primjerima, ovo se mapira na `AgentSession`, kreiranu pomoću `agent.create_session()`. Sesija je ugrađena kratkoročna memorija frameworka: drži kontekst razgovora dostupan dok se ista sesija koristi, no taj se kontekst ne čuva kada sesija završi ili se aplikacija ponovno pokrene. Za činjenice i preferencije koje trebaju preživjeti preko sesija koristi se dugoročna memorija, obično putem baze podataka, vektorskog indeksa ili drugog trajnog spremišta.

**Primjer kratkoročne memorije**

Ako korisnik pita: "Koliko bi koštao let za Pariz?" a zatim nastavi s "A što je s smještajem tamo?", kratkoročna memorija osigurava da agent razumije da se "tamo" odnosi na "Pariz" u istom razgovoru.

#### Dugoročna memorija

To su informacije koje traju kroz više razgovora ili sesija. Omogućuje agentima da pamte korisničke preferencije, povijesne interakcije ili opće znanje tijekom duljeg razdoblja. Važno je za personalizaciju.

**Primjer dugoročne memorije**

Dugoročna memorija može pohraniti da "Ben voli skijanje i aktivnosti u prirodi, voli kavu s pogledom na planine i želi izbjeći zahtjevne skijaške staze zbog ranije ozljede". Te informacije, naučene iz prethodnih interakcija, utječu na preporuke u budućim planovima putovanja, čineći ih vrlo personaliziranim.

#### Persona memorija

Ova specijalizirana vrsta memorije pomaže agentu da razvije dosljednu "osobnost" ili "personu". Omogućuje agentu da pamti detalje o sebi ili svojoj namijenjenoj ulozi, čineći interakcije fluidnijima i fokusiranijima.

**Primjer persona memorije**

Ako je putni agent dizajniran kao "ekspert za planiranje skijanja", persona memorija može pojačati tu ulogu, utječući na njegove odgovore da budu u skladu sa stručnim tonom i znanjem.

#### Workflow/Epizodična memorija

Ova memorija pohranjuje slijed koraka koje agent poduzima tijekom složenog zadatka, uključujući uspjehe i neuspjehe. To je poput pamćenja specifičnih "epizoda" ili prošlih iskustava kako bi iz njih učio.

**Primjer epizodične memorije**

Ako je agent pokušao rezervirati određeni let, ali to nije uspjelo zbog nedostupnosti, epizodična memorija može zabilježiti taj neuspjeh, omogućujući agentu da pokuša alternativne letove ili informira korisnika o problemu na informiraniji način tijekom sljedećeg pokušaja.

#### Memorija entiteta

Ovo uključuje izdvajanje i pamćenje specifičnih entiteta (poput ljudi, mjesta ili stvari) i događaja iz razgovora. Omogućuje agentu da gradi strukturirano razumijevanje ključnih elemenata o kojima se raspravljalo.

**Primjer memorije entiteta**

Iz razgovora o prošlom putovanju agent može izdvojiti "Pariz", "Eiffelov toranj" i "večera u restoranu Le Chat Noir" kao entitete. U budućoj interakciji, agent može prisjetiti "Le Chat Noira" i ponuditi novu rezervaciju tamo.

#### Strukturirani RAG (Retrieval Augmented Generation)

Iako je RAG šira tehnika, "Strukturirani RAG" istaknut je kao moćna tehnologija memorije. Ona izdvaja guste, strukturirane informacije iz različitih izvora (razgovori, emailovi, slike) i koristi ih za poboljšanje preciznosti, pokrivenosti i brzine odgovora. Za razliku od klasičnog RAG-a koji se oslanja isključivo na semantičku sličnost, Strukturirani RAG koristi inherentnu strukturu informacija.

**Primjer Strukturiranog RAG-a**

Umjesto da se samo podudaraju ključne riječi, Strukturirani RAG može parsirati detalje leta (odredište, datum, vrijeme, aviokompanija) iz emaila i pohraniti ih na strukturiran način. To omogućuje precizna pitanja poput "Koji sam let rezervirao za Pariz u utorak?"

## Implementacija i pohrana memorije

Implementacija memorije za AI agente uključuje sustavan proces **upravljanja memorijom**, koji uključuje generiranje, pohranu, dohvaćanje, integraciju, ažuriranje i čak "zaboravljanje" (ili brisanje) informacija. Dohvaćanje je posebno ključan aspekt.

### Specijalizirani alati za memoriju

#### Mem0

Jedan od načina za pohranu i upravljanje memorijom agenta je korištenje specijaliziranih alata poput Mem0. Mem0 radi kao sloj trajne memorije, omogućujući agentima da se prisjećaju relevantnih interakcija, pohranjuju korisničke preferencije i faktualni kontekst te uče iz uspjeha i neuspjeha tijekom vremena. Ideja je da stateless agenti postanu stateful.

Rad je kroz **dvofazni memorijski proces: ekstrakciju i ažuriranje**. Prvo se poruke dodane u agentov thread šalju Mem0 servisu koji koristi Veliki jezični model (LLM) za sažimanje povijesti razgovora i izvlačenje novih memorija. Nakon toga, faza ažuriranja upravljana LLM-om odlučuje hoće li te memorije dodati, izmijeniti ili izbrisati, pohranjujući ih u hibridno spremište podataka koje može uključivati vektorske, graf i key-value baze. Sustav podržava razne vrste memorije i može uključiti graf memoriju za upravljanje odnosima između entiteta.

#### Cognee

Drugi snažan pristup je korištenje **Cognee-a**, open-source semantičke memorije za AI agente koja transformira strukturirane i nestrukturirane podatke u upitne grafikone znanja podržane embeddingima. Cognee pruža **arhitekturu s dva spremišta** koja kombinira vektorsko pretraživanje po sličnosti s grafičkim odnosima, omogućujući agentima da razumiju ne samo što je slično, nego i kako su koncepti povezani.

Izvrsno funkcionira u **hibridnom dohvaćanju** koje kombinira vektorsku sličnost, graf strukturu i LLM rezoniranje - od osnovnog pregleda dijelova podataka do odgovaranja na pitanja svjesna grafa. Sustav održava **živu memoriju** koja se razvija i raste, dok ostaje upitna kao jedan povezani graf, podržavajući kratkoročni kontekst sesije i dugoročnu trajnu memoriju.

Cognee tutorijal bilježnice ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrira izgradnju ovog ujedinjenog memorijskog sloja, s praktičnim primjerima unošenja različitih izvora podataka, vizualizacije grafa znanja i upita s različitim strategijama pretraživanja prilagođenim specifičnim potrebama agenata.

### Pohrana memorije s RAG-om

Osim specijaliziranih alata za memoriju poput Mem0, možete iskoristiti robusne usluge pretraživanja poput **Azure AI Search kao backend za pohranu i dohvaćanje memorija**, posebno za strukturirani RAG.

To vam omogućuje da utemeljite odgovore vašeg agenta na vlastitim podacima, osiguravajući relevantnije i točnije odgovore. Azure AI Search može se koristiti za pohranu korisničkih memorija putovanja, kataloga proizvoda ili bilo kojeg drugog domenskog znanja.

Azure AI Search podržava funkcionalnosti poput **Strukturiranog RAG-a**, koji je izvrsan u izdvajanja i dohvaćanju gustih, strukturiranih informacija iz velikih skupova podataka poput povijesti razgovora, emailova ili čak slika. Ovo pruža "superljudsku preciznost i pokrivenost" u usporedbi s tradicionalnim pristupima dijeljenja teksta i embeddinga.

## Kako učiniti AI agente samopoboljšavajućima

Uobičajeni obrazac za samopoboljšavajuće agente uključuje uvođenje **"agenta znanja"**. Taj poseban agent promatra glavni razgovor između korisnika i primarnog agenta. Njegova uloga je:

1. **Identificirati vrijedne informacije**: Odrediti je li neki dio razgovora vrijedan za spremanje kao opće znanje ili specifična korisnička preferencija.

2. **Izvući i sažeti**: Destilirati bitnu lekciju ili preferenciju iz razgovora.

3. **Pohraniti u bazu znanja**: Trajno pohraniti ove informacije, često u vektorskoj bazi podataka, kako bi se mogle kasnije dohvatiti.

4. **Obogatiti buduće upite**: Kad korisnik pokrene novi upit, agent znanja dohvaća relevantne pohranjene informacije i dodaje ih korisnikovom unosu, pružajući ključni kontekst primarnom agentu (slično RAG-u).

### Optimizacije za memoriju

• **Upravljanje latencijom**: Da bi se izbjeglo usporavanje korisničkih interakcija, može se isprva koristiti jeftiniji, brži model za brzo provjeravanje je li informacija vrijedna za pohranu ili dohvat, a složeniji proces ekstrakcije/dohvata poziva se samo po potrebi.

• **Održavanje baze znanja**: Za rastuću bazu znanja, rjeđe korištene informacije mogu se premjestiti u "hladno spremište" radi upravljanja troškovima.

## Imate li dodatnih pitanja o memoriji agenata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se susreli s drugim učenicima, sudjelovali u uredskim satima i dobili odgovore na vaša pitanja o AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->