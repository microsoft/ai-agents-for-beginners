<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:23:51+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "hr"
}
-->
# Memorija za AI agente

Kada se raspravlja o jedinstvenim prednostima stvaranja AI agenata, najčešće se spominju dvije stvari: sposobnost pozivanja alata za obavljanje zadataka i sposobnost poboljšanja tijekom vremena. Memorija je temelj stvaranja samopoboljšavajućih agenata koji mogu pružiti bolje iskustvo našim korisnicima.

U ovoj lekciji, razmotrit ćemo što je memorija za AI agente, kako je možemo upravljati i koristiti za dobrobit naših aplikacija.

## Uvod

Ova lekcija obuhvaća:

• **Razumijevanje memorije AI agenata**: Što je memorija i zašto je ključna za agente.

• **Implementacija i pohrana memorije**: Praktične metode za dodavanje sposobnosti memorije vašim AI agentima, s naglaskom na kratkoročnu i dugoročnu memoriju.

• **Stvaranje samopoboljšavajućih AI agenata**: Kako memorija omogućuje agentima da uče iz prošlih interakcija i poboljšavaju se tijekom vremena.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

• **Razlikovati različite vrste memorije AI agenata**, uključujući radnu, kratkoročnu i dugoročnu memoriju, kao i specijalizirane oblike poput memorije osobnosti i epizodne memorije.

• **Implementirati i upravljati kratkoročnom i dugoročnom memorijom za AI agente** koristeći Semantic Kernel framework, alate poput Mem0 i Whiteboard memorije te integraciju s Azure AI Search.

• **Razumjeti principe iza samopoboljšavajućih AI agenata** i kako robusni sustavi upravljanja memorijom doprinose kontinuiranom učenju i prilagodbi.

## Razumijevanje memorije AI agenata

U svojoj srži, **memorija za AI agente odnosi se na mehanizme koji im omogućuju zadržavanje i prisjećanje informacija**. Te informacije mogu uključivati specifične detalje o razgovoru, korisničke preferencije, prošle radnje ili čak naučene obrasce.

Bez memorije, AI aplikacije često su bez stanja, što znači da svaka interakcija počinje od nule. To dovodi do ponavljajućeg i frustrirajućeg korisničkog iskustva gdje agent "zaboravlja" prethodni kontekst ili preferencije.

### Zašto je memorija važna?

Inteligencija agenta usko je povezana s njegovom sposobnošću prisjećanja i korištenja prošlih informacija. Memorija omogućuje agentima da budu:

• **Refleksivni**: Uče iz prošlih radnji i ishoda.

• **Interaktivni**: Održavaju kontekst tijekom trajanja razgovora.

• **Proaktivni i reaktivni**: Predviđaju potrebe ili odgovaraju prikladno na temelju povijesnih podataka.

• **Autonomni**: Djeluju samostalnije koristeći pohranjeno znanje.

Cilj implementacije memorije je učiniti agente **pouzdanijima i sposobnijima**.

### Vrste memorije

#### Radna memorija

Zamislite ovo kao komad papira za bilješke koji agent koristi tijekom jednog zadatka ili misaonog procesa. Ona drži neposredne informacije potrebne za sljedeći korak.

Za AI agente, radna memorija često bilježi najrelevantnije informacije iz razgovora, čak i ako je cijela povijest chata duga ili skraćena. Fokusira se na izdvajanje ključnih elemenata poput zahtjeva, prijedloga, odluka i radnji.

**Primjer radne memorije**

Kod agenta za rezervaciju putovanja, radna memorija može zabilježiti trenutni zahtjev korisnika, poput "Želim rezervirati putovanje u Pariz". Ovaj specifični zahtjev drži se u neposrednom kontekstu agenta kako bi vodio trenutnu interakciju.

#### Kratkoročna memorija

Ova vrsta memorije zadržava informacije tijekom trajanja jednog razgovora ili sesije. To je kontekst trenutnog chata, omogućujući agentu da se referira na prethodne korake u dijalogu.

**Primjer kratkoročne memorije**

Ako korisnik pita, "Koliko bi koštala karta za Pariz?" i zatim nastavi s "Što je s smještajem tamo?", kratkoročna memorija osigurava da agent zna da se "tamo" odnosi na "Pariz" unutar istog razgovora.

#### Dugoročna memorija

Ovo su informacije koje traju kroz više razgovora ili sesija. Omogućuje agentima da pamte korisničke preferencije, povijesne interakcije ili opće znanje tijekom duljih vremenskih razdoblja. To je važno za personalizaciju.

**Primjer dugoročne memorije**

Dugoročna memorija može pohraniti da "Ben uživa u skijanju i aktivnostima na otvorenom, voli kavu s pogledom na planine i želi izbjeći napredne skijaške staze zbog prošle ozljede". Ove informacije, naučene iz prethodnih interakcija, utječu na preporuke u budućim sesijama planiranja putovanja, čineći ih visoko personaliziranima.

#### Memorija osobnosti

Ova specijalizirana vrsta memorije pomaže agentu da razvije dosljednu "osobnost" ili "personu". Omogućuje agentu da pamti detalje o sebi ili svojoj namijenjenoj ulozi, čineći interakcije tečnijima i fokusiranijima.

**Primjer memorije osobnosti**

Ako je agent za putovanja dizajniran da bude "stručnjak za planiranje skijanja", memorija osobnosti može učvrstiti ovu ulogu, utječući na njegove odgovore kako bi se uskladili s tonom i znanjem stručnjaka.

#### Memorija tijeka rada/epizodna memorija

Ova memorija pohranjuje slijed koraka koje agent poduzima tijekom složenog zadatka, uključujući uspjehe i neuspjehe. To je poput pamćenja specifičnih "epizoda" ili prošlih iskustava kako bi se učilo iz njih.

**Primjer epizodne memorije**

Ako je agent pokušao rezervirati određeni let, ali nije uspio zbog nedostupnosti, epizodna memorija može zabilježiti taj neuspjeh, omogućujući agentu da pokuša alternativne letove ili informira korisnika o problemu na informiraniji način tijekom sljedećeg pokušaja.

#### Memorija entiteta

Ovo uključuje izdvajanje i pamćenje specifičnih entiteta (poput ljudi, mjesta ili stvari) i događaja iz razgovora. Omogućuje agentu da izgradi strukturirano razumijevanje ključnih elemenata o kojima se raspravlja.

**Primjer memorije entiteta**

Iz razgovora o prošlom putovanju, agent može izdvojiti "Pariz", "Eiffelov toranj" i "večera u restoranu Le Chat Noir" kao entitete. U budućoj interakciji, agent bi se mogao prisjetiti "Le Chat Noir" i ponuditi da tamo napravi novu rezervaciju.

#### Strukturirani RAG (Retrieval Augmented Generation)

Dok je RAG šira tehnika, "Strukturirani RAG" ističe se kao moćna tehnologija memorije. Izvlači gustu, strukturiranu informaciju iz različitih izvora (razgovora, e-mailova, slika) i koristi je za poboljšanje preciznosti, prisjećanja i brzine odgovora. Za razliku od klasičnog RAG-a koji se oslanja isključivo na semantičku sličnost, Strukturirani RAG radi s inherentnom strukturom informacija.

**Primjer strukturiranog RAG-a**

Umjesto da samo podudara ključne riječi, Strukturirani RAG može analizirati detalje leta (odredište, datum, vrijeme, aviokompanija) iz e-maila i pohraniti ih na strukturiran način. To omogućuje precizne upite poput "Koji let sam rezervirao za Pariz u utorak?"

## Implementacija i pohrana memorije

Implementacija memorije za AI agente uključuje sustavni proces **upravljanja memorijom**, koji uključuje generiranje, pohranu, dohvaćanje, integraciju, ažuriranje, pa čak i "zaboravljanje" (ili brisanje) informacija. Dohvaćanje je posebno ključan aspekt.

### Specijalizirani alati za memoriju

Jedan od načina za pohranu i upravljanje memorijom agenta je korištenje specijaliziranih alata poput Mem0. Mem0 djeluje kao sloj trajne memorije, omogućujući agentima da se prisjete relevantnih interakcija, pohrane korisničke preferencije i kontekstualne činjenice te uče iz uspjeha i neuspjeha tijekom vremena. Ideja je da se agenti bez stanja pretvore u agente sa stanjem.

Funkcionira kroz **dvostupanjski proces memorije: ekstrakcija i ažuriranje**. Prvo, poruke dodane u nit agenta šalju se Mem0 servisu, koji koristi Large Language Model (LLM) za sažimanje povijesti razgovora i izdvajanje novih memorija. Nakon toga, faza ažuriranja vođena LLM-om određuje hoće li te memorije dodati, izmijeniti ili izbrisati, pohranjujući ih u hibridnu bazu podataka koja može uključivati vektorske, grafičke i ključ-vrijednost baze podataka. Ovaj sustav također podržava različite vrste memorije i može uključiti grafičku memoriju za upravljanje odnosima između entiteta.

### Pohrana memorije s RAG-om

Osim specijaliziranih alata za memoriju poput Mem0, možete koristiti robusne usluge pretraživanja poput **Azure AI Search kao pozadinu za pohranu i dohvaćanje memorija**, posebno za strukturirani RAG.

To omogućuje da odgovori vašeg agenta budu utemeljeni na vašim vlastitim podacima, osiguravajući relevantnije i točnije odgovore. Azure AI Search može se koristiti za pohranu korisničkih putnih memorija, kataloga proizvoda ili bilo kojeg drugog znanja specifičnog za domenu.

Azure AI Search podržava mogućnosti poput **strukturiranog RAG-a**, koji se ističe u izvlačenju i dohvaćanju guste, strukturirane informacije iz velikih skupova podataka poput povijesti razgovora, e-mailova ili čak slika. To pruža "nadljudsku preciznost i prisjećanje" u usporedbi s tradicionalnim pristupima segmentiranju teksta i ugrađivanju.

## Stvaranje samopoboljšavajućih AI agenata

Uobičajeni obrazac za samopoboljšavajuće agente uključuje uvođenje **"agenta za znanje"**. Ovaj zasebni agent promatra glavni razgovor između korisnika i primarnog agenta. Njegova uloga je:

1. **Identificirati vrijedne informacije**: Odrediti je li neki dio razgovora vrijedan pohrane kao opće znanje ili specifična korisnička preferencija.

2. **Izvući i sažeti**: Destilirati bitno učenje ili preferenciju iz razgovora.

3. **Pohraniti u bazu znanja**: Pohraniti izdvojene informacije, često u vektorsku bazu podataka, kako bi se kasnije mogle dohvatiti.

4. **Povećati buduće upite**: Kada korisnik pokrene novi upit, agent za znanje dohvaća relevantne pohranjene informacije i dodaje ih korisničkom upitu, pružajući ključni kontekst primarnom agentu (slično RAG-u).

### Optimizacije za memoriju

• **Upravljanje latencijom**: Kako bi se izbjeglo usporavanje korisničkih interakcija, jeftiniji, brži model može se koristiti inicijalno za brzo provjeravanje je li informacija vrijedna pohrane ili dohvaćanja, a složeniji proces ekstrakcije/dohvaćanja se pokreće samo kada je potrebno.

• **Održavanje baze znanja**: Za rastuću bazu znanja, informacije koje se rjeđe koriste mogu se premjestiti u "hladnu pohranu" radi upravljanja troškovima.

## Imate li još pitanja o inženjeringu konteksta?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, sudjelovali u uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.