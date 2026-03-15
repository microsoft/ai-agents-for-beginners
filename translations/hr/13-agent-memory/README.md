# Memorija za AI agente  
[![Agent Memory](../../../translated_images/hr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kada se raspravlja o jedinstvenim prednostima stvaranja AI agenata, najčešće se raspravlja o dvije stvari: sposobnosti pozivanja alata za dovršavanje zadataka i sposobnosti poboljšavanja tijekom vremena. Memorija je temelj za stvaranje samopoboljšavajućeg agenta koji može stvarati bolje iskustvo za naše korisnike.

U ovoj lekciji proučit ćemo što je memorija za AI agente i kako je možemo upravljati i koristiti u korist naših aplikacija.

## Uvod

Ova lekcija pokriva:

• **Razumijevanje memorije AI agenata**: Što je memorija i zašto je ključna za agente.

• **Implementacija i pohrana memorije**: Praktične metode za dodavanje memorijskih sposobnosti vašim AI agentima, fokusirajući se na kratkoročnu i dugoročnu memoriju.

• **Samopoboljšavanje AI agenata**: Kako memorija omogućava agentima da uče iz prošlih interakcija i poboljšavaju se tijekom vremena.

## Dostupne implementacije

Ova lekcija uključuje dva sveobuhvatna bilježničarska vodiča:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementira memoriju koristeći Mem0 i Azure AI Search s Microsoft Agent Frameworkom

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementira strukturiranu memoriju koristeći Cognee, automatski gradi graf znanja podržan embeddingsima, vizualizira graf i omogućava inteligentno dohvaćanje

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

• **Razlikovati različite vrste memorije AI agenata**, uključujući radnu, kratkoročnu i dugoročnu memoriju, kao i specijalizirane oblike poput persona i epizodne memorije.

• **Implementirati i upravljati kratkoročnom i dugoročnom memorijom za AI agente** koristeći Microsoft Agent Framework, iskorištavajući alate poput Mem0, Cognee, Whiteboard memoriju i integraciju s Azure AI Search.

• **Razumjeti principe samopoboljšavajućih AI agenata** i kako robusni sustavi upravljanja memorijom doprinose kontinuiranom učenju i prilagodbi.

## Razumijevanje memorije AI agenata

U svojoj biti, **memorija za AI agente odnosi se na mehanizme koji im omogućuju zadržavanje i prisjećanje informacija**. Te informacije mogu biti specifični detalji o razgovoru, korisničke preferencije, prošle radnje ili čak naučeni obrasci.

Bez memorije, AI aplikacije često su bezstanja, što znači da svaka interakcija započinje ispočetka. To dovodi do ponavljajućeg i frustrirajućeg korisničkog iskustva gdje agent "zaboravlja" prethodni kontekst ili preferencije.

### Zašto je memorija važna?

Inteligencija agenta duboko je povezana sa sposobnošću prisjećanja i korištenja prošlih informacija. Memorija omogućava agentima da budu:

• **Reflektivni**: Učenje iz prošlih radnji i rezultata.

• **Interaktivni**: Održavanje konteksta tijekom trajanja razgovora.

• **Proaktivni i reaktivni**: Predviđanje potreba ili odgovaranje na odgovarajući način na temelju povijesnih podataka.

• **Autonomni**: Samostalnije djelovanje oslanjajući se na pohranjeno znanje.

Cilj implementacije memorije je učiniti agente **pouzdanijima i sposobnijima**.

### Vrste memorije

#### Radna memorija

Zamislite ovo kao komad bilježnice koji agent koristi tijekom jednog tekućeg zadatka ili misaonog procesa. Drži neposredne informacije potrebne za izračun sljedećeg koraka.

Za AI agente, radna memorija često hvata najrelevantnije informacije iz razgovora, čak i ako je cijela povijest chata duga ili skraćena. Fokusira se na izvlačenje ključnih elemenata poput zahtjeva, prijedloga, odluka i radnji.

**Primjer radne memorije**

U agentu za rezervaciju putovanja, radna memorija može zabilježiti trenutni zahtjev korisnika, poput "Želim rezervirati putovanje u Pariz". Taj specifični zahtjev držan je u neposrednom kontekstu agenta za vođenje trenutačne interakcije.

#### Kratkoročna memorija

Ova vrsta memorije zadržava informacije tijekom trajanja jednoga razgovora ili sesije. To je kontekst trenutačnog chata koji agentu omogućuje da se referira natrag na prethodne korake u dijalogu.

**Primjer kratkoročne memorije**

Ako korisnik pita, "Koliko bi koštao let do Pariza?" a zatim nastavlja sa "A što je s smještajem tamo?", kratkoročna memorija osigurava da agent zna da "tamo" odnosi se na "Pariz" unutar istog razgovora.

#### Dugoročna memorija

Ovo su informacije koje traju kroz više razgovora ili sesija. Omogućuje agentima da se sjećaju korisničkih preferencija, povijesnih interakcija ili općeg znanja kroz duže vremensko razdoblje. To je važno za personalizaciju.

**Primjer dugoročne memorije**

Dugoročna memorija može pohraniti da "Ben uživa u skijanju i aktivnostima na otvorenom, voli kavu s pogledom na planine i želi izbjeći zahtjevne skijaške staze zbog prošle ozljede". Te informacije, naučene iz prethodnih interakcija, utječu na preporuke u budućim sesijama planiranja putovanja, čineći ih vrlo personaliziranim.

#### Persona memorija

Ova specijalizirana vrsta memorije pomaže agentu razviti dosljednu "osobnost" ili "personu". Omogućava agentu da pamti detalje o sebi ili svojoj predviđenoj ulozi, čineći interakcije fluidnijima i fokusiranijima.

**Primjer persona memorije**  
Ako je agent za putovanja dizajniran kao "stručni planera skijanja", persona memorija može pojačati tu ulogu, utječući na njegove odgovore da budu u skladu s tonom i znanjem stručnjaka.

#### Radni tijek/Epizodna memorija

Ova memorija pohranjuje redoslijed koraka koje agent poduzima tijekom složenog zadatka, uključujući uspjehe i neuspjehe. Kao da pamtite konkretne "epizode" ili prošla iskustva kako biste iz njih učili.

**Primjer epizodne memorije**

Ako je agent pokušao rezervirati određeni let, ali je to propalo zbog nedostupnosti, epizodna memorija može zabilježiti ovaj neuspjeh, dopuštajući agentu da pokuša alternativne letove ili na informiraniji način obavijesti korisnika o problemu tijekom narednog pokušaja.

#### Memorija entiteta

Ovo uključuje izdvajanje i pamćenje specifičnih entiteta (poput osoba, mjesta ili stvari) i događaja iz razgovora. Omogućuje agentu da gradi strukturirano razumijevanje ključnih elemenata o kojima se raspravljalo.

**Primjer memorije entiteta**

Iz razgovora o prošlom putovanju, agent može izvući "Pariz", "Eiffelov toranj" i "večera u restoranu Le Chat Noir" kao entitete. U budućoj interakciji agent može prisjetiti "Le Chat Noir" i ponuditi da tamo napravi novu rezervaciju.

#### Strukturirani RAG (retrieval augmented generation)

Iako je RAG šira tehnika, "strukturirani RAG" istaknut je kao moćna memorijska tehnologija. Izvlači guste, strukturirane informacije iz različitih izvora (razgovora, emailova, slika) i koristi ih za poboljšanje preciznosti, dohvata i brzine odgovora. Za razliku od klasičnog RAG-a koji se oslanja samo na semantičku sličnost, Strukturirani RAG radi s inherentnom strukturom informacija.

**Primjer strukturiranog RAG-a**

Umjesto da samo podudara ključne riječi, Strukturirani RAG može rastaviti detalje leta (odredište, datum, vrijeme, aviokompaniju) iz emaila i pohraniti ih na strukturiran način. To omogućuje precizna pitanja poput "Koji sam let rezervirao za Pariz u utorak?"

## Implementacija i pohrana memorije

Implementacija memorije za AI agente uključuje sustavan proces **upravljanja memorijom**, što uključuje generiranje, pohranu, dohvaćanje, integraciju, ažuriranje i čak "zaboravljanje" (odnosno brisanje) informacija. Dohvaćanje informacije je osobito ključan aspekt.

### Specijalizirani alati za memoriju

#### Mem0

Jedan od načina za pohranu i upravljanje memorijom agenta je korištenje specijaliziranih alata poput Mem0. Mem0 funkcionira kao sloj trajne memorije koji omogućava agentima prisjećanje relevantnih interakcija, pohranu korisničkih preferencija i činjeničnog konteksta te učenje iz uspjeha i neuspjeha tijekom vremena. Ideja je da agenti bez stanja postanu agenti sa stanjem.

Radi kroz **dvofazni memorijski proces: ekstrakcija i ažuriranje**. Prvo se poruke dodane u agentovu temu šalju Mem0 servisu, koji koristi Veliki jezični model (LLM) za sažimanje povijesti razgovora i izdvajanje novih sjećanja. Zatim, faza ažuriranja pokretana LLM-om određuje hoće li se ta sjećanja dodati, izmijeniti ili izbrisati te ih pohranjuje u hibridnu bazu podataka koja može uključivati vektorske, grafičke i key-value baze. Taj sustav podržava različite tipove memorije i može uključiti graf memoriju za upravljanje odnosima između entiteta.

#### Cognee

Drugi moćan pristup je korištenje **Cognee**, open-source semantičke memorije za AI agente koja pretvara strukturirane i nestrukturirane podatke u upitne grafikone znanja podržane embeddingsima. Cognee pruža **dvoskladišnu arhitekturu** koja kombinira pretraživanje po sličnosti vektora s grafičkim odnosima, omogućujući agentima da razumiju ne samo što je slično, nego i kako su koncepti međusobno povezani.

Izvrsno je u **hibridnom dohvaćanju** koje spaja vektorsku sličnost, strukturu grafa i LLM rezoniranje - od osnovnog pronalaženja podataka do odgovaranja na pitanja svjesna grafa. Sustav održava **živu memoriju** koja se razvija i raste, a pritom ostaje upitna kao jedan povezani graf, podržavajući i kratkoročni kontekst sesije i dugoročnu trajnu memoriju.

Cognee bilježničarski vodič ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrira izgradnju ovog jedinstvenog memorijskog sloja, s praktičnim primjerima unošenja raznovrsnih izvora podataka, vizualizacije grafa znanja i upita s različitim strategijama pretraživanja prilagođenim posebnim potrebama agenata.

### Pohrana memorije s RAG

Osim specijaliziranih memorijskih alata poput mem0, možete iskoristiti robusne servise pretraživanja poput **Azure AI Search kao backend za pohranu i dohvaćanje memorije**, osobito za strukturirani RAG.

Ovo vam omogućuje da utemeljite odgovore vašeg agenta na vlastitim podacima, osiguravajući relevantnije i točnije odgovore. Azure AI Search može se koristiti za pohranu korisničkih memorija o putovanjima, proizvoda ili bilo kojeg drugog domen-specifičnog znanja.

Azure AI Search podržava mogućnosti poput **strukturiranog RAG-a**, koji izvrsno izvlači i dohvaća guste, strukturirane informacije iz velikih skupova podataka kao što su povijesti razgovora, emailovi ili čak slike. To pruža "nadljudsku preciznost i dohvata" u usporedbi s tradicionalnim pristupima razbijanju teksta i embeddinga.

## Samopoboljšavanje AI agenata

Uobičajeni obrazac za samopoboljavajuće agente uključuje uvođenje **"agenta znanja"**. Taj poseban agent promatra glavni razgovor između korisnika i primarnog agenta. Njegova uloga je:

1. **Identificirati vrijedne informacije**: Odrediti je li bilo koji dio razgovora vrijedan pohrane kao opće znanje ili specifična korisnička preferencija.

2. **Izvući i sažeti**: Destilirati ključnu lekciju ili preferenciju iz razgovora.

3. **Pohraniti u bazu znanja**: Sačuvati ove izdvojene informacije, često u vektorsku bazu podataka, kako bi se kasnije mogle dohvatiti.

4. **Obogatiti buduće upite**: Kada korisnik pokrene novi upit, agent znanja dohvaća relevantne pohranjene informacije i dodaje ih korisničkom upitu, pružajući ključni kontekst primarnom agentu (slično RAG-u).

### Optimizacije za memoriju

• **Upravljanje latencijom**: Kako se ne bi usporile korisničke interakcije, može se koristiti jeftiniji, brži model za početnu provjeru je li informacija vrijedna pohrane ili dohvaćanja, a složeniji proces ekstrakcije/dohvaćanja poziva se samo kad je potrebno.

• **Održavanje baze znanja**: Za rastuću bazu znanja, rjeđe korištene informacije mogu se premjestiti u "hladnu pohranu" radi upravljanja troškovima.

## Imate li dodatnih pitanja o memoriji agenata?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se susreli s drugim učenicima, sudjelovali na uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazume ili kriva tumačenja koja proizlaze iz uporabe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->