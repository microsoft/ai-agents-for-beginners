# AI agenti u produkciji: Promatranje i evaluacija

[![AI Agents in Production](../../../translated_images/hr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kako AI agenti prelaze sa eksperimentalnih prototipova na stvarne primjene, sposobnost razumijevanja njihovog ponašanja, praćenja njihove izvedbe i sustavne evaluacije njihovih rezultata postaje važna.

## Ciljevi učenja

Nakon što završite ovaj lekciju, znat ćete kako razumjeti/sljedeće:
- Osnovni pojmovi promatranja i evaluacije agenata
- Tehnike za poboljšanje izvedbe, troškova i učinkovitosti agenata
- Što i kako sustavno evaluirati svoje AI agente
- Kako kontrolirati troškove prilikom postavljanja AI agenata u produkciju
- Kako instrumentirati agente izgrađene s Microsoft Agent Frameworkom

Cilj je opremiti vas znanjem da svoje "crne kutije" agente pretvorite u transparentne, upravljive i pouzdane sustave.

_**Napomena:** Važno je postavljati AI agente koji su sigurni i pouzdani. Pogledajte i lekciju [Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)._

## Traci i spanovi

Alati za promatranje poput [Langfuse](https://langfuse.com/) ili [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) obično predstavljaju izvođenje agenata kao trake i spanove.

- **Traka** predstavlja cjelokupni zadatak agenta od početka do kraja (kao što je obrada korisničkog upita).
- **Spanovi** su pojedinačni koraci unutar trake (kao što je pozivanje jezičnog modela ili dohvat podataka).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez promatranja, AI agent može djelovati kao "crna kutija" – njegovo unutarnje stanje i razmišljanje su neprozirni, što otežava dijagnosticiranje problema ili optimizaciju izvedbe. S promatranjem, agenti postaju "staklene kutije", nudeći transparentnost koja je ključna za izgradnju povjerenja i osiguravanje da rade kako je zamišljeno.

## Zašto promatranje ima važnost u produkcijskim okruženjima

Prijelaz AI agenata u produkcijska okruženja uvodi nove izazove i zahtjeve. Promatranje više nije samo "lijepo imati", već kritična sposobnost:

*   **Debugging i analiza uzroka:** Kad agent zakaže ili proizvede neočekivani rezultat, alati za promatranje pružaju trake potrebne za precizno utvrđivanje izvora pogreške. Ovo je osobito važno u složenim agentima koji mogu uključivati više poziva LLM-a, interakcije s alatima i uvjetnu logiku.
*   **Upravljanje latencijom i troškovima:** AI agenti često ovise o LLM-ovima i drugim vanjskim API-jima koji se naplaćuju po tokenu ili po pozivu. Promatranje omogućava precizno praćenje tih poziva, pomažući u identificiranju operacija koje su pretjerano spore ili skupe. To omogućava timovima optimizaciju promptova, odabir učinkovitijih modela ili redizajn radnih tijekova za upravljanje operativnim troškovima i osiguranje dobrog korisničkog iskustva.
*   **Povjerenje, sigurnost i usklađenost:** U mnogim aplikacijama važno je osigurati da agenti djeluju sigurno i etično. Promatranje pruža revizijski trag akcija i odluka agenata. To se može koristiti za otkrivanje i ublažavanje problema poput prompt injekcija, generiranja štetnog sadržaja ili nepravilnog rukovanja osobnim podacima (PII). Na primjer, možete pregledati trake da razumijete zašto je agent dao određeni odgovor ili koristio specifičan alat.
*   **Petlje kontinuiranog poboljšanja:** Podaci promatranja temelj su iterativnog procesa razvoja. Praćenjem izvedbe agenata u stvarnom svijetu, timovi mogu identificirati područja za poboljšanje, prikupiti podatke za fino podešavanje modela i potvrditi utjecaj promjena. To stvara povratnu petlju gdje uvidi iz produkcijskog online praćenja informiraju offline eksperimentiranje i doradu, što vodi do progresivno bolje izvedbe agenata.

## Ključni metrički pokazatelji za praćenje

Za praćenje i razumijevanje ponašanja agenata treba pratiti niz metrika i signala. Iako se specifični metrički pokazatelji mogu razlikovati ovisno o svrsi agenta, neki su univerzalno važni.

Evo nekih od najčešćih metrika koje alati za promatranje prate:

**Latencija:** Koliko brzo agent odgovara? Dugo čekanje negativno utječe na korisničko iskustvo. Trebali biste mjeriti latenciju za zadatke i pojedinačne korake prateći izvođenja agenata. Na primjer, agent koji traje 20 sekundi za sve pozive modela može se ubrzati korištenjem bržeg modela ili paralelnim izvođenjem poziva modela.

**Troškovi:** Koliki je trošak po izvođenju agenta? AI agenti ovise o pozivima LLM-a koji se naplaćuju po tokenu ili vanjskim API-jima. Česta upotreba alata ili više promptova može brzo povećati troškove. Na primjer, ako agent pet puta pozove LLM radi marginalnog poboljšanja kvalitete, morate procijeniti je li trošak opravdan ili možete smanjiti broj poziva ili koristiti jeftiniji model. Praćenje u stvarnom vremenu može pomoći i u otkrivanju neočekivanih skokova (npr. greške koje uzrokuju višestruke petlje API-ja).

**Pogreške zahtjeva:** Koliko zahtjeva je agent propustio? Ovo može uključivati API pogreške ili neuspjele pozive alata. Da biste učinili agenta otpornijim u produkciji, možete postaviti zamjene ili ponovne pokušaje. Npr. ako je LLM davatelj A nedostupan, možete prebaciti na LLM davatelja B kao rezervu.

**Povratne informacije korisnika:** Implementacija izravnih korisničkih evaluacija pruža vrijedne uvide. To može uključivati eksplicitne ocjene (👍palac gore/👎dolje, ⭐1-5 zvjezdica) ili tekstualne komentare. Dosljedne negativne povratne informacije trebaju vas upozoriti jer su znak da agent ne radi kako je očekivano.

**Implicitne povratne informacije korisnika:** Ponašanja korisnika pružaju neizravnu povratnu informaciju čak i bez eksplicitnih ocjena. To može uključivati trenutnu izmjenu pitanja, ponovljene upite ili klikanje na gumb za ponovni pokušaj. Npr. ako vidite da korisnici stalno postavljaju isto pitanje, to je znak da agent ne radi kako je očekivano.

**Točnost:** Koliko često agent proizvodi točne ili poželjne rezultate? Definicije točnosti variraju (npr. točnost rješavanja problema, točnost dohvaćanja informacija, zadovoljstvo korisnika). Prvi korak je definirati što za vašeg agenta znači uspjeh. Možete pratiti točnost putem automatiziranih provjera, ocjena evaluacije ili oznaka dovršenosti zadataka. Na primjer, označiti trake kao "uspješne" ili "neuspješne".

**Automatizirane metrike evaluacije:** Također možete postaviti automatizirane evaluacije. Na primjer, možete koristiti LLM za ocjenu izlaza agenta, npr. da li je koristan, točan ili nije. Postoji i nekoliko open source biblioteka koje pomažu ocijeniti različite aspekte agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ili [LLM Guard](https://llm-guard.com/) za otkrivanje štetnog jezika ili prompt injekcija.

U praksi, kombinacija ovih metrika daje najbolji pregled zdravlja AI agenta. U [primjeru bilježnice](./code_samples/10-expense_claim-demo.ipynb) u ovom poglavlju pokazat ćemo vam kako te metrike izgledaju na stvarnim primjerima, ali najprije ćemo naučiti kako izgleda tipični postupak evaluacije.

## Instrumentirajte svoj agent

Da biste prikupili podatke o praćenju, trebate instrumentirati svoj kod. Cilj je instrumentirati kod agenta tako da emitira trake i metrike koje može uhvatiti, obraditi i vizualizirati platforma za promatranje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se nametnuo kao industrijski standard za promatranje LLM-ova. Pruža skup API-ja, SDK-a i alata za generiranje, prikupljanje i izvoz telemetrijskih podataka.

Postoji mnogo biblioteka za instrumentaciju koje omotavaju postojeće okvire agenata i olakšavaju izvoz OpenTelemetry spanova u alat za promatranje. Microsoft Agent Framework se nativno integrira s OpenTelemetryjem. Ispod je primjer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvršavanje agenta se automatski prati
    pass
```

Primjer bilježnice [example notebook](./code_samples/10-expense_claim-demo.ipynb) u ovom poglavlju pokazat će vam kako instrumentirati svoj MAF agent.

**Ručno kreiranje spanova:** Iako biblioteke za instrumentaciju pružaju dobru osnovu, često postoje slučajevi kada su potrebne detaljnije ili prilagođene informacije. Možete ručno kreirati spanove za dodavanje prilagođene logike aplikacije. Još važnije, mogu obogatiti automatski ili ručno kreirane spanove prilagođenim atributima (poznatim i kao oznake ili metapodaci). Ti atributi mogu uključivati poslovne podatke, međurezultate ili bilo koji kontekst koristan za debugiranje ili analizu, poput `user_id`, `session_id` ili `model_version`.

Primjer ručnog kreiranja traka i spanova pomoću [Langfuse Python SDK-a](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluacija agenta

Promatranje nam daje metrike, ali evaluacija je proces analize tih podataka (i izvođenja testova) kako bismo utvrdili koliko dobro agent radi i kako ga možemo poboljšati. Drugim riječima, kad imate te trake i metrike, kako ih koristiti za ocjenu agenta i donošenje odluka?

Redovita evaluacija je važna jer su AI agenti često nedeterministički i mogu se mijenjati (kroz nadogradnje ili promjene u ponašanju modela) – bez evaluacije ne biste znali radi li vaš "pametni agent" zapravo dobro ili je nazadovao.

Postoje dvije kategorije evaluacija za AI agente: **online evaluacija** i **offline evaluacija**. Obje su vrijedne i nadopunjuju se. Obično se započinje s offline evaluacijom, jer je to minimalni korak prije postavljanja bilo kojeg agenta.

### Offline evaluacija

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To podrazumijeva evaluaciju agenta u kontroliranim uvjetima, obično koristeći testne skupove podataka, a ne upite stvarnih korisnika. Koristite kurirane skupove podataka gdje znate što je očekivani izlaz ili ispravno ponašanje, a zatim na njima pokrećete agenta.

Na primjer, ako ste izgradili agenta za riješavanje matematičkih zadataka s riječima, mogli biste imati [testni skup podataka](https://huggingface.co/datasets/gsm8k) od 100 problema s poznatim odgovorima. Offline evaluacija se često radi tijekom razvoja (i može biti dio CI/CD procesa) za provjeru poboljšanja ili sprječavanje nazadovanja. Prednost je u tome što je **ponovljivo i možete dobiti jasne metrike točnosti budući da imate osnovnu istinu**. Možete također simulirati korisničke upite i mjeriti odgovore agenta naspram idealnih odgovora ili koristiti automatizirane metrike kao što je gore opisano.

Ključni izazov kod offline evaluacije je osigurati da je vaš testni skup podataka sveobuhvatan i relevantan – agent može dobro raditi na fiksnom testnom skupu, ali naići na vrlo različite upite u produkciji. Stoga biste trebali redovito ažurirati testne skupove novim rubnim slučajevima i primjerima koji odražavaju stvarne scenarije. Korisna je kombinacija malih "smoke test" slučajeva i većih evaluacijskih skupova: mali skupovi za brze provjere, a veći za širu evaluaciju izvedbe.

### Online evaluacija

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi se na evaluaciju agenta u stvarnom, produkcijskom okruženju, tj. tijekom stvarne uporabe. Online evaluacija uključuje praćenje izvedbe agenta na stvarnim korisničkim interakcijama i kontinuiranu analizu ishoda.

Na primjer, mogli biste pratiti stopu uspjeha, ocjene zadovoljstva korisnika ili druge metrike na stvarnom prometu. Prednost online evaluacije je što **uhvati stvari koje ne biste mogli predvidjeti u laboratorijskim uvjetima** – možete uočiti model drift tijekom vremena (ako učinkovitost agenta opada kako se mijenjaju obrasci unosa) i uhvatiti neočekivane upite ili situacije koje nisu bile u testnim podacima. Pruža realnu sliku kako agent funkcionira u stvarnom svijetu.

Online evaluacija često uključuje prikupljanje implicitnih i eksplicitnih povratnih informacija korisnika, kao što je već raspravljeno, i moguće provođenje shadow testova ili A/B testova (gdje nova verzija agenta radi paralelno kako bi se usporedila sa starom). Izazov je što može biti teško dobiti pouzdane oznake ili ocjene za žive interakcije – možda se oslanjate na povratne informacije korisnika ili metrike kasnijeg toka (npr. je li korisnik kliknuo rezultat).

### Kombiniranje dvije vrste evaluacije

Online i offline evaluacije nisu međusobno isključive; one su vrlo komplementarne. Uvidi iz online praćenja (npr. novi tipovi korisničkih upita gdje agent loše radi) mogu se koristiti za proširenje i poboljšanje offline testnih skupova podataka. Suprotno tome, agenti koji dobro rade na offline testovima mogu se tada s većim povjerenjem postaviti i pratiti online.

Zapravo, mnogi timovi usvajaju petlju:

_evaluirati offline -> postaviti u produkciju -> pratiti online -> prikupiti nove slučajeve neuspjeha -> dodati u offline skup -> usavršavati agenta -> ponoviti_.

## Uobičajeni problemi

Dok postavljate AI agente u produkciju, možete naići na različite izazove. Evo nekih uobičajenih problema i mogućih rješenja:

| **Problem**    | **Moguće rješenje**   |
| ------------- | ------------------ |
| AI agent ne izvodi zadatke dosljedno | - Precizirajte prompt dan agentu; budite jasni u ciljevima.<br>- Identificirajte gdje podjela zadataka u podzadataka i njihovo izvođenje višestrukim agentima može pomoći. |
| AI agent zapinje u beskonačnim petljama  | - Osigurajte jasne uvjete za završetak kako bi agent znao kad zaustaviti proces.<br>- Za složene zadatke koji zahtijevaju rezoniranje i planiranje, koristite veći model specijaliziran za rezonacijske zadatke. |
| Pozivi alata AI agenta ne rade dobro   | - Testirajte i provjerite izlaz alata izvan agenta.<br>- Poboljšajte definirane parametre, promptove i imenovanje alata.  |
| Sustav s više agenata ne radi dosljedno | - Precizirajte promptove svakom agentu da budu specifični i različiti.<br>- Izgradite hijerarhijski sustav koristeći "ruting" ili kontrolni agent da odredi koji je agent ispravan. |

Mnogi od ovih problema mogu se učinkovitije identificirati s promatranjem na mjestu. Trake i metrike o kojima smo ranije govorili pomažu točno odrediti gdje u tijeku rada agenta nastaju problemi, čineći debugging i optimizaciju mnogo učinkovitijom.

## Upravljanje troškovima


Evo nekoliko strategija za upravljanje troškovima implementacije AI agenata u produkciju:

**Korištenje manjih modela:** Mali jezični modeli (SLM) mogu dobro raditi za određene agentne slučajeve korištenja i značajno će smanjiti troškove. Kao što je ranije spomenuto, izgradnja sustava za evaluaciju u svrhu određivanja i usporedbe performansi u odnosu na veće modele najbolji je način da se razumije koliko će se SLM dobro ponašati u vašem slučaju korištenja. Razmotrite korištenje SLM-ova za jednostavnije zadatke poput klasifikacije namjere ili ekstrakcije parametara, dok veće modele rezervirajte za složeno rezoniranje.

**Korištenje usmjerivačkog modela:** Slična strategija je korištenje raznolikosti modela i veličina. Možete koristiti LLM/SLM ili serverless funkciju za usmjeravanje zahtjeva prema složenosti na najprikladnije modele. To će također pomoći smanjiti troškove, a istovremeno osigurati performanse na pravim zadacima. Na primjer, usmjerite jednostavne upite prema manjim, bržim modelima, a skupe velike modele koristite samo za složene zadatke rezoniranja.

**Predmemoriranje odgovora:** Identificiranje uobičajenih zahtjeva i zadataka te pružanje odgovora prije nego što prođu kroz vaš agentski sustav dobar je način za smanjenje broja sličnih zahtjeva. Možete čak implementirati tok za određivanje koliko je zahtjev sličan vašim predmemoriranim zahtjevima koristeći osnovnije AI modele. Ova strategija može značajno smanjiti troškove za često postavljana pitanja ili uobičajene radne tokove.

## Pogledajmo kako ovo funkcionira u praksi

U [primjernom bilježničkom dokumentu ovog poglavlja](./code_samples/10-expense_claim-demo.ipynb), vidjet ćemo primjere kako možemo koristiti alate za promatranje za praćenje i evaluaciju našeg agenta.


### Imate li još pitanja o AI agentima u produkciji?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) kako biste upoznali druge učenike, sudjelovali u radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Metacognition Design Pattern](../09-metacognition/README.md)

## Sljedeća lekcija

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->