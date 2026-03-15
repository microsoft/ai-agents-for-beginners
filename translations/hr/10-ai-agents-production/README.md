# AI agenti u produkciji: Promatranje i evaluacija

[![AI Agents in Production](../../../translated_images/hr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Kako AI agenti prelaze iz eksperimentalnih prototipova u stvarne primjene, sposobnost razumijevanja njihovog ponašanja, praćenja njihove izvedbe i sustavne evaluacije njihovih ishoda postaje važna.

## Ciljevi učenja

Nakon završetka ovog poglavlja, znat ćete kako/razumjet ćete:
- Osnovne pojmove promatranja i evaluacije agenata
- Tehnike za poboljšanje izvedbe, troškova i učinkovitosti agenata
- Što i kako sustavno evaluirati svoje AI agente
- Kako kontrolirati troškove pri implementaciji AI agenata u produkciju
- Kako instrumentirati agente izgrađene s Microsoft Agent Frameworkom

Cilj je opremiti vas znanjem za transformaciju vaših "crnih kutija" agenata u transparentne, upravljive i pouzdane sustave.

_**Napomena:** Važno je implementirati AI agente koji su sigurni i pouzdani. Pogledajte i lekciju [Izgradnja pouzdanih AI agenata](./06-building-trustworthy-agents/README.md)._

## Tragovi i segmenti

Alati za promatranje poput [Langfuse](https://langfuse.com/) ili [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) obično predstavljaju izvođenja agenata kao tragove i segmente.

- **Trag** predstavlja cjelokupan zadatak agenta od početka do kraja (npr. obrada korisničkog upita).
- **Segmenti** su pojedinačni koraci unutar traga (npr. pozivanje jezičnog modela ili dohvaćanje podataka).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez promatranja, AI agent može izgledati kao „crna kutija“ – njegov unutarnji status i rezoniranje su nejasni, što otežava dijagnostiku problema ili optimizaciju izvedbe. S promatranjem, agenti postaju „staklene kutije“, nudeći transparentnost koja je ključna za izgradnju povjerenja i osiguravanje da rade kako je predviđeno.

## Zašto je promatranje važno u produkcijskim okruženjima

Prijelaz AI agenata u produkcijska okruženja donosi novi niz izazova i zahtjeva. Promatranje više nije „luksuz“, već ključna sposobnost:

*   **Otklanjanje pogrešaka i analiza uzroka:** Kad agent zakaže ili proizvede neočekivani ishod, alati za promatranje pružaju tragove potrebne za određivanje izvora pogreške. Ovo je posebno važno kod složenih agenata koji mogu uključivati više poziva LLM-a, interakcija s alatima i uvjetne logike.
*   **Upravljanje latencijom i troškovima:** AI agenti često ovise o LLM-ovima i drugim vanjskim API-jima koji se naplaćuju po tokenu ili pozivu. Promatranje omogućava precizno praćenje tih poziva, pomažući identificirati operacije koje su prespore ili preskupe. Time se omogućuje optimizacija upita, odabir učinkovitijih modela ili redizajn radnih tokova radi upravljanja troškovima i osiguravanja dobre korisničke iskustva.
*   **Povjerenje, sigurnost i usklađenost:** U mnogim primjenama važno je osigurati da se agenti ponašaju sigurno i etično. Promatranje pruža revizijski zapis radnji i odluka agenata. Može se koristiti za otkrivanje i ublažavanje problema kao što su injektiranje upita, generiranje štetnog sadržaja ili nepravilno rukovanje osobnim podacima (PII). Na primjer, možete pregledavati tragove da biste razumjeli zašto je agent dao određeni odgovor ili koristio određeni alat.
*   **Kontinuirani ciklusi poboljšanja:** Podaci iz promatranja su osnova iterativnog procesa razvoja. Praćenjem kako agenti rade u stvarnom svijetu, timovi mogu identificirati područja za poboljšanja, prikupiti podatke za fino podešavanje modela i potvrditi utjecaj promjena. Ovo stvara povratnu petlju gdje produkcijski uvidi iz online evaluacije informiraju offline eksperimentiranje i doradu, vodeći do postupnog poboljšanja izvedbe agenata.

## Ključni metrički pokazatelji za praćenje

Da biste pratili i razumjeli ponašanje agenta, treba pratiti niz metričkih pokazatelja i signala. Iako se specifične metrike mogu razlikovati ovisno o svrsi agenta, neke su univerzalno važne.

Evo nekih od najčešćih metričkih pokazatelja koje alati za promatranje prate:

**Latencija:** Koliko brzo agent odgovara? Dugo čekanje negativno utječe na korisničko iskustvo. Trebali biste mjeriti latenciju za zadatke i pojedinačne korake prateći izvođenje agenta. Na primjer, agent koji za sve pozive modela treba 20 sekundi može se ubrzati korištenjem bržeg modela ili pokretanjem poziva paralelno.

**Troškovi:** Koliki je trošak po izvođenju agenta? AI agenti se oslanjaju na LLM pozive koji se naplaćuju po tokenu ili vanjske API-je. Česta upotreba alata ili višestruki upiti mogu brzo povećati troškove. Na primjer, ako agent poziva LLM pet puta za minimalno poboljšanje kvalitete, morate procijeniti je li trošak opravdan ili biste mogli smanjiti broj poziva ili koristiti jeftiniji model. Praćenje u stvarnom vremenu može također pomoći u otkrivanju neočekivanih skokova (npr. bugovi koji uzrokuju prekomjerne petlje API-ja).

**Pogreške zahtjeva:** Koliko je zahtjeva agent neuspješno obradio? To može uključivati API pogreške ili neuspjele pozive alata. Da bi vaš agent bio otporniji na ove probleme u produkciji, možete postaviti rezervne opcije ili ponovne pokušaje. Npr. ako je LLM pružatelj A nedostupan, prebacite se na LLM pružatelja B kao rezervu.

**Povratne informacije korisnika:** Implementacija izravnih korisničkih evaluacija daje vrijedne uvide. To može uključivati eksplicitne ocjene (👍lajk/👎dislajk, ⭐1-5 zvjezdica) ili tekstualne komentare. Konzistentno negativne povratne informacije trebale bi vas upozoriti kao znak da agent ne radi kako se očekuje.

**Implicitne povratne informacije korisnika:** Ponašanje korisnika daje neizravne povratne informacije čak i bez eksplicitnih ocjena. To može uključivati trenutačno preformuliranje pitanja, ponovljene upite ili klik na tipku za ponovni pokušaj. Npr. ako primijetite da korisnici stalno postavljaju isto pitanje, to je znak da agent ne radi kako se očekuje.

**Točnost:** Koliko često agent proizvodi ispravne ili poželjne rezultate? Definicije točnosti variraju (npr. točnost rješavanja problema, točnost dohvaćanja informacija, zadovoljstvo korisnika). Prvi korak je definirati što za vašeg agenta znači uspjeh. Točnost možete pratiti automatiziranim provjerama, ocjenama evaluacije ili oznakama dovršenosti zadataka. Na primjer, označavanjem tragova kao „uspješno“ ili „neuspješno“.

**Automatizirane evaluacijske metrike:** Također možete postaviti automatizirane evaluacije. Npr. možete koristiti LLM za ocjenu izlaza agenta je li koristan, točan ili ne. Postoji i nekoliko otvorenih biblioteka koje pomažu u ocjenjivanju različitih aspekata agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ili [LLM Guard](https://llm-guard.com/) za otkrivanje štetnog jezika ili injektiranja upita.

U praksi, kombinacija ovih metričkih pokazatelja daje najbolji uvid u zdravlje AI agenta. U primjeru bilježnice ovog poglavlja [example notebook](./code_samples/10-expense_claim-demo.ipynb) pokazat ćemo vam kako ove metrike izgledaju u stvarnim primjerima, ali prvo ćemo naučiti kako izgleda tipični tijek evaluacije.

## Instrumentirajte svog agenta

Za prikupljanje podataka o traganju, trebate instrumentirati svoj kod. Cilj je instrumentirati kod agenta da emitira tragove i metrike koje može uhvatiti, obraditi i vizualizirati platforma za promatranje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) postao je industrijski standard za promatranje LLM-ova. Pruža skup API-ja, SDK-ova i alata za generiranje, prikupljanje i izvoz telemetrijskih podataka.

Postoji mnogo biblioteka za instrumentaciju koje obavijaju postojeće okvire agenata i olakšavaju izvoz OpenTelemetry segmenata u alat za promatranje. Microsoft Agent Framework izvorno integrira OpenTelemetry. Ispod je primjer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvršenje agenta se automatski prati
    pass
```

Primjer bilježnice [example notebook](./code_samples/10-expense_claim-demo.ipynb) u ovom poglavlju demonstrirat će kako instrumentirati vaš MAF agent.

**Ručno stvaranje segmenata:** Iako biblioteke za instrumentaciju pružaju dobru osnovu, često postoje slučajevi kada su potrebne detaljnije ili prilagođene informacije. Možete ručno stvarati segmente za dodavanje prilagođene logike aplikacije. Još važnije, mogu obogatiti automatski ili ručno stvorene segmente s prilagođenim atributima (poznatim i kao oznake ili metapodaci). Ti atributi mogu sadržavati poslovno specifične podatke, privremene izračune ili bilo koji kontekst koji može biti koristan za otklanjanje pogrešaka ili analizu, poput `user_id`, `session_id` ili `model_version`.

Primjer ručnog stvaranja tragova i segmenata s [Langfuse Python SDK-om](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluacija agenta

Promatranje nam daje metrike, ali evaluacija je proces analize tih podataka (i izvođenja testova) kako bismo odredili koliko dobro AI agent radi i kako se može poboljšati. Drugim riječima, kada imate te tragove i metrike, kako ih koristite za ocjenjivanje agenta i donošenje odluka?

Redovita evaluacija je važna jer su AI agenti često nedeterministički i mogu se mijenjati (kroz nadogradnje ili promjenu ponašanja modela) – bez evaluacije ne biste znali radi li vaš „pametni agent“ zapravo dobro ili je došlo do regresije.

Postoje dvije kategorije evaluacija za AI agente: **online evaluacija** i **offline evaluacija**. Obje su vrijedne i nadopunjuju se. Obično započinjemo s offline evaluacijom, jer je to minimalni potrebni korak prije implementacije bilo kojeg agenta.

### Offline evaluacija

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ona uključuje evaluaciju agenta u kontroliranim uvjetima, obično korištenjem testnih skupova podataka, a ne korisničkih upita uživo. Koristite kurirane skupove podataka gdje znate očekivani ishod ili ispravno ponašanje, a zatim pokrećete agenta na njima.

Na primjer, ako ste izgradili agenta za rješavanje matematičkih riječi-problema, mogli biste imati [testni skup podataka](https://huggingface.co/datasets/gsm8k) od 100 problema sa poznatim odgovorima. Offline evaluacija se često provodi tijekom razvoja (i može biti dio CI/CD procesa) da provjeri poboljšanja ili spriječi regresije. Prednost je što je **ponovljiva i možete dobiti jasne metrike točnosti jer imate referentnu istinu**. Također možete simulirati korisničke upite i mjeriti odgovore agenta prema idealnim odgovorima ili koristiti automatizirane metrike opisane gore.

Ključni izazov offline evaluacije je osigurati da vaš testni skup podataka bude sveobuhvatan i ostane relevantan – agent može dobro funkcionirati na fiksnom testnom skupu, ali susresti vrlo različite upite u produkciji. Zato biste trebali redovito ažurirati testne skupove novim rubnim slučajevima i primjerima koji odražavaju stvarne scenarije​. Korisna je kombinacija malih „smoke test“ slučajeva i većih evaluacijskih setova: mali su za brze provjere, veliki za šire metrike izvedbe​.

### Online evaluacija

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se odnosi na evaluaciju agenta u živom, stvarnom okruženju, tj. tijekom stvarne upotrebe u produkciji. Online evaluacija podrazumijeva praćenje izvedbe agenta u stvarnim korisničkim interakcijama i kontinuiranu analizu ishoda.

Na primjer, možete pratiti uspješnost, ocjene zadovoljstva korisnika ili druge metrike na stvarnom prometu. Prednost online evaluacije je što **hvata stvari koje možda ne možete predvidjeti u laboratorijskom okruženju** – možete promatrati drift modela tijekom vremena (ako efikasnost agenta opada dok se ulazni obrasci mijenjaju) i detektirati neočekivane upite ili situacije koje nisu bile u vašim testnim podacima​. Ona pruža stvarnu sliku o tome kako se agent ponaša u stvarnom svijetu.

Online evaluacija često uključuje prikupljanje implicitnih i eksplicitnih povratnih informacija korisnika, kao i mogućnost vođenja testova u sjeni ili A/B testova (gdje nova verzija agenta radi paralelno za usporedbu sa starom). Izazov je što može biti teško dobiti pouzdane oznake ili ocjene za žive interakcije – možda ćete se oslanjati na povratne informacije korisnika ili metričke pokazatelje iz lančanih procesa (npr. je li korisnik kliknuo na rezultat).

### Kombiniranje dvaju pristupa

Online i offline evaluacije nisu međusobno isključive; one su vrlo komplementarne. Uvidi iz online praćenja (npr. novi tipovi korisničkih upita na kojima agent loše radi) mogu se koristiti za obogaćivanje i poboljšanje offline testnih skupova. Suprotno, agenti koji dobro prolaze offline testove mogu se s većim povjerenjem implementirati i pratiti online.

Zapravo, mnogi timovi usvajaju petlju:

_evaluiraj offline -> implementiraj -> prati online -> prikupi nove slučajeve neuspjeha -> dodaj u offline skup podataka -> doradi agenta -> ponovi_.

## Uobičajeni problemi

Kako implementirate AI agente u produkciju, možete se susresti s raznim izazovima. Evo nekih uobičajenih problema i njihovih mogućih rješenja:

| **Problem**    | **Moguće rješenje**   |
| ------------- | ------------------ |
| AI agent ne izvršava zadatke dosljedno | - Doradite upit postavljen AI agentu; budite jasni u ciljevima.<br>- Identificirajte mjesta gdje podjela zadataka na pod-zadatke i rukovanje njima s više agenata može pomoći. |
| AI agent ulazi u kontinuirane petlje  | - Osigurajte jasne uvjete zaustavljanja kako bi agent znao kada zaustaviti proces.<br>- Za složene zadatke koji zahtijevaju rezoniranje i planiranje, koristite veći model specijaliziran za rezonacijske zadatke. |
| Pozivi alata AI agenta ne funkcioniraju dobro   | - Testirajte i validirajte izlaz alata izvan sustava agenta.<br>- Doradite definirane parametre, upite i imenovanje alata.  |
| Multi-agentni sustav ne radi dosljedno | - Doradite upite za svakog agenta da budu specifični i različiti.<br>- Izgradite hijerarhijski sustav koristeći „usmjeravajućeg“ ili kontrolnog agenta za određivanje koji je agent ispravan. |

Mnoge od ovih problema moguće je učinkovitije identificirati uz postavljenu promatranost. Tragovi i metrike o kojima smo govorili ranije pomažu pinpointirati točno gdje u tijeku rada agenta nastaju problemi, što čini otklanjanje grešaka i optimizaciju puno učinkovitijima.

## Upravljanje troškovima
Evo nekoliko strategija za upravljanje troškovima implementacije AI agenata u produkciju:

**Korištenje manjih modela:** Mali jezični modeli (SLM) mogu dobro funkcionirati za određene agencijske slučajeve korištenja i značajno smanjiti troškove. Kao što je ranije spomenuto, izgradnja sustava za evaluaciju kako bi se odredila i usporedila izvedba u odnosu na veće modele najbolji je način da se razumije koliko će dobro SLM raditi na vašem slučaju korištenja. Razmotrite korištenje SLM-ova za jednostavnije zadatke kao što su klasifikacija namjere ili ekstrakcija parametara, dok veće modele rezervirajte za složeno razmišljanje.

**Korištenje router modela:** Slična strategija je korištenje različitosti modela i veličina. Možete koristiti LLM/SLM ili serverless funkciju za usmjeravanje zahtjeva na temelju složenosti prema najprikladnijim modelima. To će također pomoći u smanjenju troškova, a istovremeno osigurati izvedbu na pravim zadacima. Na primjer, usmjerite jednostavne upite prema manjim, bržim modelima, a skupe velike modele koristite samo za složene zadatke razmišljanja.

**Keširanje odgovora:** Identificiranje čestih zahtjeva i zadataka te pružanje odgovora prije nego što prođu kroz vaš agencijski sustav dobar je način za smanjenje količine sličnih zahtjeva. Možete čak implementirati tok za identifikaciju koliko je zahtjev sličan vašim keširanim zahtjevima koristeći osnovnije AI modele. Ova strategija može značajno smanjiti troškove za često postavljana pitanja ili uobičajene radne tokove.

## Pogledajmo kako ovo funkcionira u praksi

U [primjernom bilježniku ovog dijela](./code_samples/10-expense_claim-demo.ipynb) vidjet ćemo primjere kako možemo koristiti alate za opažanje za nadzor i evaluaciju našeg agenta.


### Imate još pitanja o AI agentima u produkciji?

Pridružite se [Microsoft Foundry Discordu](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, sudjelovali na konzultacijama i dobili odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Metakognitivni dizajnerski uzorak](../09-metacognition/README.md)

## Sljedeća lekcija

[Agencijski protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI alata za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim. Za važne informacije preporuča se angažiranje profesionalnog ljudskog prevoditelja. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->