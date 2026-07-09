# AI agenti u produkciji: promatranje i evaluacija

[![AI Agents in Production](../../../translated_images/hr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kako AI agenti prelaze iz eksperimentalnih prototipova u stvarne primjene, sposobnost razumijevanja njihovog ponašanja, praćenja njihove izvedbe i sustavnog vrednovanja njihovih rezultata postaje važna.

## Ciljevi učenja

Nakon završetka ovog poglavlja znat ćete kako/razumjeti:
- Temeljne koncepte promatranja i evaluacije agenata
- Tehnike za poboljšanje izvedbe, troškova i učinkovitosti agenata
- Što i kako sustavno evaluirati svoje AI agente
- Kako kontrolirati troškove prilikom postavljanja AI agenata u produkciju
- Kako instrumentirati agente izgrađene s Microsoft Agent Frameworkom

Cilj je opremiti vas znanjem za pretvaranje vaših "crnih kutija" agenata u transparentne, upravljive i pouzdane sustave.

_**Napomena:** Važno je postaviti AI agente koji su sigurni i pouzdani. Pogledajte i lekciju [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Tragovi i opsezi

Alati za promatranje poput [Langfuse](https://langfuse.com/) ili [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) obično predstavljaju izvođenje agenata kao tragove i opsege.

- **Trag** predstavlja cjelovit zadatak agenata od početka do kraja (npr. obrada upita korisnika).
- **Opsezi** su pojedinačni koraci unutar traga (npr. pozivanje jezičnog modela ili dohvaćanje podataka).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez promatranja, AI agent može se doimati kao "crna kutija" – njegovo unutarnje stanje i razlozi su neprozirni, što otežava dijagnosticiranje problema ili optimizaciju izvedbe. S promatranjem, agenti postaju "staklene kutije", pružajući transparentnost koja je ključna za izgradnju povjerenja i osiguranje da rade kako je zamišljeno.

## Zašto promatranje ima važnost u produkcijskim okruženjima

Prijelaz AI agenata u produkcijska okruženja uvodi novi niz izazova i zahtjeva. Promatranje više nije "lijepo imati", već ključna sposobnost:

*   **Otklanjanje pogrešaka i analiza uzroka:** Kada agent zakaže ili proizvede neočekivan rezultat, alati za promatranje pružaju tragove potrebne za precizno utvrđivanje izvora pogreške. Ovo je posebno važno kod složenih agenata koji mogu uključivati višestruke pozive LLM-a, interakcije s alatima i uvjetnu logiku.
*   **Upravljanje latencijom i troškovima:** AI agenti često se oslanjaju na LLM-ove i druge vanjske API-je koje se naplaćuju po tokenu ili pozivu. Promatranje omogućava precizno praćenje tih poziva, pomažući u identifikaciji operacija koje su previše spore ili skupe. To omogućuje timovima optimizaciju upita, odabir učinkovitijih modela ili redizajn tijekova rada za upravljanje operativnim troškovima i osiguravanje dobre korisničke iskustva.
*   **Povjerenje, sigurnost i usklađenost:** U mnogim aplikacijama važno je osigurati da se agenti ponašaju sigurno i etički. Promatranje pruža zapisnik o radnjama i odlukama agenata. To se može koristiti za otkrivanje i ublažavanje problema poput unošenja promptova, generiranja štetnog sadržaja ili nepravilnog rukovanja osobnim podacima. Na primjer, možete pregledavati tragove da biste razumjeli zašto je agent dao određeni odgovor ili koristio određeni alat.
*   **Kontinuirane petlje poboljšanja:** Podaci promatranja temelj su iterativnog procesa razvoja. Praćenjem kako agenti rade u stvarnom svijetu, timovi mogu identificirati područja za poboljšanje, prikupiti podatke za fino podešavanje modela i potvrditi utjecaj promjena. To stvara povratnu petlju u kojoj uvide iz produkcije preko online evaluacije informiraju offline eksperimentiranje i usavršavanje, dovodeći do postupno boljih rezultata agenata.

## Ključne metrike za praćenje

Za praćenje i razumijevanje ponašanja agenata, treba pratiti niz metrika i signala. Specifične metrike mogu varirati ovisno o namjeni agenta, ali neke su univerzalno važne.

Evo nekoliko najčešćih metrika koje alati za promatranje prate:

**Latencija:** Koliko brzo agent reagira? Dugo čekanje negativno utječe na korisničko iskustvo. Trebalo bi mjeriti latenciju za zadatke i pojedinačne korake praćenjem izvođenja agenata. Na primjer, agent koji treba 20 sekundi za sve pozive modela mogao bi se ubrzati korištenjem bržeg modela ili paralelnim pozivima modela.

**Troškovi:** Koliki je trošak po izvođenju agenta? AI agenti oslanjaju se na LLM pozive naplaćivane po tokenu ili vanjske API-je. Često korištenje alata ili višestruki upiti mogu brzo povećati troškove. Na primjer, ako agent poziva LLM pet puta za marginalno poboljšanje kvalitete, morate procijeniti opravdanost troška ili razmotriti smanjenje broja poziva ili korištenje jeftinijeg modela. Praćenje u stvarnom vremenu također može pomoći u otkrivanju neočekivanih skokova (npr. bugovi uzrokujući pretjerane petlje API-ja).

**Pogreške u zahtjevima:** Koliko zahtjeva agent nije uspio obraditi? To može uključivati pogreške API-ja ili neuspjele pozive alata. Da bi agent bio otporniji u produkciji, možete postaviti alternative ili ponovne pokušaje. Npr. ako je LLM pružatelj A nedostupan, prebacite se na LLM pružatelja B kao rezervu.

**Povratne informacije korisnika:** Implementacija izravnih evaluacija korisnika pruža vrijedne uvide. To može uključivati eksplicitne ocjene (👍palac gore/👎dolje, ⭐1-5 zvjezdica) ili tekstualne komentare. Dosljedno negativne povratne informacije trebale bi vas upozoriti jer su znak da agent ne radi kako se očekuje.

**Implicitne povratne informacije korisnika:** Ponašanja korisnika pružaju neizravne povratne informacije čak i bez eksplicitnih ocjena. To može uključivati trenutno preformuliranje pitanja, ponovljene upite ili klikanje gumba za ponovni pokušaj. Na primjer, ako vidite da korisnici stalno postavljaju isto pitanje, to je znak da agent ne radi kako se očekuje.

**Točnost:** Koliko često agent proizvodi točne ili poželjne rezultate? Definicije točnosti variraju (npr. točnost rješavanja problema, točnost dohvaćanja informacija, zadovoljstvo korisnika). Prvi korak je definirati kako za vašeg agenta izgleda uspjeh. Točnost možete pratiti putem automatiziranih provjera, ocjena evaluacije ili oznaka dovršenosti zadataka. Na primjer, označavanje tragova kao "uspješno" ili "neuspješno".

**Automatizirane metrike evaluacije:** Također možete postaviti automatizirane evaluacije. Na primjer, možete koristiti LLM za ocjenjivanje izlaza agenta, npr. je li koristan, točan ili ne. Postoje i razne open source biblioteke koje pomažu ocijeniti različite aspekte agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ili [LLM Guard](https://llm-guard.com/) za otkrivanje štetnog jezika ili unošenja promptova.

U praksi kombinacija ovih metrika daje najbolji pregled zdravlja AI agenta. U ovom poglavlju [primjer bilježnice](./code_samples/10-expense_claim-demo.ipynb) pokazat ćemo kako ove metrike izgledaju u stvarnim primjerima, ali prvo ćemo naučiti kako izgleda tipični tijek rada evaluacije.

## Instrumentirajte svog agenta

Za prikupljanje podataka o tragovima potrebno je instrumentirati svoj kod. Cilj je instrumentirati kod agenata tako da emitira tragove i metrike koje može zabilježiti, obraditi i vizualizirati platforma za promatranje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se etablirao kao industrijski standard za promatranje LLM-a. Pruža skup API-ja, SDK-ova i alata za generiranje, prikupljanje i izvoz telemetrijskih podataka.

Postoji mnogo biblioteka za instrumentaciju koje obavijaju postojeće okvire agenata i olakšavaju izvoz OpenTelemetry opsega u alat za promatranje. Microsoft Agent Framework se nativno integrira s OpenTelemetry-jem. Ispod je primjer instrumentacije MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvršavanje agenta se automatski prati
    pass
```

[Primjer bilježnice](./code_samples/10-expense_claim-demo.ipynb) u ovom poglavlju pokazat će kako instrumentirati vašeg MAF agenta.

**Ručno stvaranje opsega:** Iako biblioteke za instrumentaciju pružaju dobru osnovu, često su potrebne detaljnije ili prilagođene informacije. Možete ručno stvarati opsege za dodavanje prilagođene logike aplikacije. Još važnije, mogu obogatiti automatski ili ručno kreirane opsege prilagođenim atributima (poznatima i kao oznake ili metapodaci). Ti atributi mogu uključivati poslovno specifične podatke, međurezultate ili bilo koji kontekst koristan za otklanjanje pogrešaka ili analizu, kao što su `user_id`, `session_id` ili `model_version`.

Primjer ručnog stvaranja tragova i opsega s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluacija agenta

Promatranje nam daje metrike, ali evaluacija je proces analiziranja tih podataka (i izvođenja testova) kako bismo odredili koliko dobro AI agent radi i kako se može poboljšati. Drugim riječima, kad imate te tragove i metrike, kako ih koristite da prosudite agenta i donesete odluke?

Redovita evaluacija je važna jer AI agenti često nisu deterministički i mogu evoluirati (kroz ažuriranja ili promjenu ponašanja modela) – bez evaluacije ne biste znali radi li vaš „pametni agent“ stvarno dobro ili je nazadovao.

Postoje dvije kategorije evaluacija za AI agente: **online evaluacija** i **offline evaluacija**. Obje su vrijedne i nadopunjuju se. Obično počinjemo s offline evaluacijom jer je to minimalni potrebni korak prije postavljanja bilo kojeg agenta.

### Offline evaluacija

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To uključuje evaluaciju agenta u kontroliranim uvjetima, obično korištenjem testnih podataka, a ne stvarnih korisničkih upita. Koristite kurirane skupove podataka gdje znate očekivani izlaz ili točno ponašanje, i onda pokrećete agenta na njima.

Na primjer, ako ste izgradili agenta za rješavanje matematičkih zadataka, možda imate [testni skup podataka](https://huggingface.co/datasets/gsm8k) od 100 problema s poznatim odgovorima. Offline evaluacija se često provodi tijekom razvoja (i može biti dio CI/CD procesa) kako bi se provjerila poboljšanja ili spriječile regresije. Prednost je što je **ponovljiva i možete dobiti jasne metrike točnosti jer imate stvarnu istinu**. Također možete simulirati korisničke upite i mjeriti odgovore agenta u odnosu na idealne odgovore ili koristiti automatizirane metrike kao što je opisano gore.

Glavni izazov kod offline evaluacije je osigurati da je vaš testni skup sveobuhvatan i ostaje relevantan – agent može dobro funkcionirati na fiksnom testnom skupu, ali naići na vrlo različite upite u produkciji. Stoga biste trebali redovito ažurirati testne skupove novim rubnim slučajevima i primjerima koji odražavaju stvarne scenarije. Korisna je kombinacija malih „smoke test“ slučajeva i većih evaluacijskih skupova: mali skupovi za brze provjere i veći za šire metrike izvedbe.

### Online evaluacija

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se odnosi na evaluaciju agenta u stvarnom, produkcijskom okruženju, tj. tijekom stvarne uporabe. Online evaluacija uključuje praćenje izvedbe agenta u stvarnim korisničkim interakcijama i kontinuiranu analizu rezultata.

Na primjer, mogli biste pratiti stope uspjeha, ocjene zadovoljstva korisnika ili druge metrike na stvarnom prometu. Prednost online evaluacije je što **uhvati stvari koje možda ne očekujete u laboratorijskom okruženju** – možete primijetiti promjenu modela tijekom vremena (ako učinkovitost agenta opada kako se mijenjaju obrasci ulaza) i uočiti neočekivane upite ili situacije koje nisu bile u vašim testnim podacima. To pruža stvarnu sliku kako se agent ponaša u stvarnom svijetu.

Online evaluacija često uključuje prikupljanje implicitnih i eksplicitnih povratnih informacija korisnika, kako je ranije opisano, i moguće izvođenje shadow testova ili A/B testova (gdje nova verzija agenta radi paralelno za usporedbu sa starom). Izazov je u dobivanju pouzdanih oznaka ili ocjena za stvarne interakcije – možda se oslanjate na povratne informacije korisnika ili metrike nižeg sloja (npr. je li korisnik kliknuo rezultat).

### Kombiniranje dvaju pristupa

Online i offline evaluacije nisu međusobno isključive; vrlo su komplementarne. Uvidi iz online praćenja (npr. novi tipovi korisničkih upita gdje agent ne radi dobro) mogu se koristiti za proširenje i poboljšanje offline testnih skupova podataka. Suprotno, agenti koji dobro prolaze offline testove mogu se s većim povjerenjem postaviti i pratiti online.

Zapravo, mnogi timovi primjenjuju petlju:

_evaluiraj offline -> deploy -> prati online -> skupljaj nove slučajeve neuspjeha -> dodaj u offline set -> fino podešavaj agenta -> ponovi_.

## Uobičajeni problemi

Prilikom postavljanja AI agenata u produkciju, možete naići na različite izazove. Evo nekoliko uobičajenih problema i potencijalnih rješenja:

| **Problem**    | **Potencijalno rješenje**   |
| ------------- | ------------------ |
| AI agent ne izvršava zadatke dosljedno | - Doradite prompt koji dajete AI agentu; budite jasni u ciljevima.<br>- Identificirajte gdje dijeljenje zadataka na podzadatke i njihovo izvođenje od strane više agenata može pomoći. |
| AI agent ulazi u neprekidne petlje  | - Osigurajte jasne uvjete prekida da agent zna kada zaustaviti proces.<br>- Za složene zadatke koji zahtijevaju rezoniranje i planiranje, koristite veći model specijaliziran za takve zadatke. |
| Pozivi alata AI agenta nisu učinkoviti   | - Testirajte i validirajte izlaz alata izvan sustava agenta.<br>- Doradite definirane parametre, upite i imenovanje alata.  |
| Višeagentni sustav ne radi dosljedno | - Doradite upite za svakog agenta kako biste osigurali da su specifični i različiti jedan od drugoga.<br>- Izgradite hijerarhijski sustav koristeći "rutirajućeg" ili kontrolnog agenta koji određuje koji je agent ispravan. |

Mnoge od ovih poteškoća mogu se učinkovitije uočiti ako postoji promatranje. Tragovi i metrike o kojima smo ranije govorili pomažu precizno odrediti gdje u tijeku rada agenta nastaju problemi, što olakšava otklanjanje pogrešaka i optimizaciju.

## Upravljanje troškovima


Evo nekoliko strategija za upravljanje troškovima implementacije AI agenata u produkciju:

**Korištenje manjih modela:** Mali jezični modeli (SLM) mogu dobro raditi na određenim agentnim slučajevima upotrebe i značajno će smanjiti troškove. Kao što je ranije spomenuto, izrada evaluacijskog sustava za određivanje i usporedbu performansi u odnosu na veće modele najbolji je način da se razumije koliko će SLM dobro raditi na vašem slučaju upotrebe. Razmislite o korištenju SLM-ova za jednostavnije zadatke poput klasifikacije namjere ili ekstrakcije parametara, dok zadržavate veće modele za složeno rezoniranje.

**Korištenje modela usmjerivača:** Slična strategija je korištenje raznolikosti modela i veličina. Možete koristiti LLM/SLM ili serverless funkciju za usmjeravanje zahtjeva prema složenosti na najbolje odgovarajuće modele. Ovo će također pomoći u smanjenju troškova uz osiguranje performansi na pravim zadacima. Na primjer, usmjerite jednostavne upite prema manjim, bržim modelima, a skupe velike modele koristite samo za složene zadatke rezoniranja.

**Keširanje odgovora:** Identificiranje uobičajenih zahtjeva i zadataka te pružanje odgovora prije nego što prođu kroz vaš agentni sustav dobar je način za smanjenje volumena sličnih zahtjeva. Možete čak implementirati tok za određivanje koliko je zahtjev sličan vašim keširanim zahtjevima koristeći osnovnije AI modele. Ova strategija može značajno smanjiti troškove za često postavljana pitanja ili uobičajene radne tokove.

## Pogledajmo kako to funkcionira u praksi

U [primjer bilježnice ovog poglavlja](./code_samples/10-expense_claim-demo.ipynb) vidjet ćemo primjere kako možemo koristiti alate za promatranje i evaluaciju našeg agenta.


### Imate li dodatnih pitanja o AI agentima u produkciji?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) kako biste susreli druge učenike, sudjelovali u radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Metakognitivni dizajnerski obrazac](../09-metacognition/README.md)

## Sljedeća lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->