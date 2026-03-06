# AI agenti v produkciji: opazljivost in ocenjevanje

[![AI agenti v produkciji](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v resnične aplikacije, postaja sposobnost razumevanja njihovega vedenja, spremljanja njihove zmogljivosti in sistematičnega ocenjevanja njihovih izhodov pomembna.

## Cilji učenja

Po končani lekciji boste znali/razumeli:
- Osnovne koncepte opazljivosti in ocenjevanja agentov
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično ocenjevati svoje AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente zgrajene z Microsoft Agent Framework

Cilj je opremiti vas z znanjem, da svoje "črne skrinjice" agente spremenite v pregledne, upravljljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zanesljivi. Oglejte si tudi lekcijo [Gradnja zaupanja vrednih AI agentov](./06-building-trustworthy-agents/README.md)._

## Sledi in razponi

Orodja za opazljivost, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo izvajanja agentov kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (kot je obravnava uporabniškega poizvedbe).
- **Razponi (spans)** so posamezni koraki znotraj sledu (kot je klic modela jezika ali pridobivanje podatkov).

![Drevo sledi v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez opazljivosti se lahko AI agent zdi kot "črna skrinjica" - njegovo notranje stanje in razmišljanje sta neprozorna, kar otežuje diagnosticiranje težav ali optimizacijo zmogljivosti. Z opazljivostjo postanejo agenti "steklene skrinjice", ki nudijo preglednost, kar je bistveno za gradnjo zaupanja in zagotovitev, da delujejo kot je predvideno.

## Zakaj je opazljivost pomembna v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nov nabor izzivov in zahtev. Opazljivost ni več "le lepo-to-imeti", temveč kritična sposobnost:

*   **Razhroščevanje in analize vzrokov**: Ko agent odpove ali proizvede nepričakovan izhod, orodja za opazljivost zagotovijo sledi, potrebne za natančno ugotovitev vira napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcij z orodji in pogojne logike.
*   **Upravljanje latence in stroškov**: AI agenti pogosto uporabljajo LLM in druge zunanje API-je, ki se zaračunavajo na token ali na klic. Opazljivost omogoča natančno sledenje teh klicev, kar pomaga prepoznati operacije, ki so pretirano počasne ali drage. To ekipam omogoča optimizacijo pozivov, izbiro učinkovitejših modelov ali prenovo delovnih tokov za upravljanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost**: V mnogih aplikacijah je pomembno zagotoviti, da se agenti obnašajo varno in etično. Opazljivost zagotavlja revizijsko sled agentovih dejanj in odločitev. To se lahko uporabi za odkrivanje in blaženje težav, kot so prompt injection, ustvarjanje škodljive vsebine ali nepravilno ravnanje z osebno prepoznavnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent podal določen odgovor ali uporabil določeno orodje.
*   **Zanke za neprekinjeno izboljševanje**: Podatki opazljivosti so temelj iterativnega razvojnega procesa. Z nadzorovanjem, kako agenti delujejo v resničnem svetu, lahko ekipe prepoznajo področja za izboljšave, zberejo podatke za fino nastavljanje modelov in potrdijo vpliv sprememb. To ustvarja povratno zanko, kjer produkcijski vpogledi iz spletnega ocenjevanja informirajo offline eksperimentiranje in izboljšave, kar vodi k postopnemu izboljšanju zmogljivosti agenta.

## Ključne metrike za sledenje

Za spremljanje in razumevanje vedenja agenta je treba spremljati vrsto metrik in signalov. Konkretne metrike se lahko razlikujejo glede na namen agenta, vendar so nekatere univerzalno pomembne.

Tukaj so nekatere najpogostejše metrike, ki jih spremljajo orodja za opazljivost:

**Latenca:** Kako hitro agent odgovori? Dolgi časi čakanja negativno vplivajo na uporabniško izkušnjo. Latenco bi morali meriti za naloge in posamezne korake z beleženjem sledu izvajanj agenta. Na primer, agent, ki za vse klice modela potrebuje 20 sekund, bi lahko pospešili z uporabo hitrejšega modela ali izvajanjem klicev modela vzporedno.

**Stroški:** Kolikšen je strošek na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na token ali zunanje API-je. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent pokliče LLM petkrat za minimalno izboljšanje kakovosti, morate oceniti, ali so stroški upravičeni ali pa bi lahko zmanjšali število klicev ali uporabili cenejši model. Spremljanje v realnem času lahko tudi pomaga odkriti nepričakovane skoke (npr. napake, ki povzročajo prekomerne zanke API klicev).

**Napake zahtevkov:** Koliko zahtevkov je agent neuspel izvesti? To lahko vključuje napake API ali neuspešne klice orodij. Da bi bil vaš agent v produkciji bolj robusten proti tem, lahko nastavite nadomestila ali ponovitve. Npr. če LLM ponudnik A ne deluje, preklopite na LLM ponudnika B kot rezervnega.

**Povratne informacije uporabnikov:** Neposredne uporabniške ocene zagotavljajo dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍thumbs-up/👎down, ⭐1-5 zvezdic) ali besedilne komentarje. Konstantno negativne povratne informacije bi vam morale signalizirati, da agent ne deluje, kot je pričakovano.

**Implicitne povratne informacije uporabnikov:** Uporabniško vedenje nudi posredne povratne informacije tudi brez eksplicitnih ocen. To lahko vključuje takojšnje preoblikovanje vprašanja, ponavljajoče se poizvedbe ali klik na gumb za ponovni poskus. Npr. če opazite, da uporabniki večkrat zastavljajo isto vprašanje, je to znak, da agent ne deluje pričakovano.

**Natančnost:** Kako pogosto agent proizvede pravilne ali zaželjene izhode? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost iskanja informacij, zadovoljstvo uporabnika). Prvi korak je definirati, kako izgleda uspeh za vašega agenta. Natančnost lahko spremljate z avtomatiziranimi preverjanji, evalvacijskimi ocenami ali oznakami dokončanosti naloge. Na primer, označevanje sledi kot "uspešno" ali "neuspešno".

**Avtomatizirane evalvacijske metrike:** Prav tako lahko nastavite avtomatizirane evalvacije. Na primer, lahko uporabite LLM za ocenjevanje izhoda agenta, npr. ali je bil koristni, natančen ali ne. Obstaja tudi več odprtokodnih knjižnic, ki pomagajo ocenjevati različne vidike agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali prompt injection.

V praksi kombinacija teh metrik nudi najboljši pregled zdravja AI agenta. V tem poglavju v [primerjalnem zvezku](./code_samples/10-expense_claim-demo.ipynb) bomo pokazali, kako te metrike izgledajo v resničnih primerih, a najprej se naučimo, kako izgleda tipičen delovni tok ocenjevanja.

## Instrumentirajte svojega agenta

Da zberete podatke sledenja, boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta tako, da sprošča sledi in metrike, ki jih lahko prestreže, obdela in vizualizira platforma za opazljivost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se je uveljavil kot industrijski standard za opazljivost LLM. Ponuja nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetričnih podatkov.

Obstaja veliko knjižnic za instrumentacijo, ki ovijejo obstoječe ogrodja agentov in olajšajo izvoz OpenTelemetry razponov v orodje za opazljivost. Microsoft Agent Framework se nativno integrira z OpenTelemetry. Spodaj je primer o instrumentiranju MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvajanje agenta se samodejno sledi.
    pass
```

V tem poglavju bo [primer zvezka](./code_samples/10-expense_claim-demo.ipynb) prikazal, kako instrumentirati vaš MAF agent.

**Ročno ustvarjanje razponov (spans):** Čeprav knjižnice za instrumentacijo nudijo dobro osnovo, obstajajo primeri, kjer so potrebne bolj podrobne ali prilagojene informacije. Razpone lahko ročno ustvarjate, da dodate prilagojeno aplikacijsko logiko. Še pomembneje pa je, da lahko avtomatsko ali ročno ustvarjenim razponom dodate prilagojene atribute (znane tudi kot oznake ali metadata). Ti atributi lahko vključujejo poslovno-specifične podatke, vmesne izračune ali kateri koli kontekst, ki je lahko uporaben za razhroščevanje ali analizo, kot so `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledi in razponov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agenta

Opazljivost nam daje metrike, vendar je ocenjevanje proces analize teh podatkov (in izvedbe testov) za ugotovitev, kako dobro AI agent deluje in kako ga je mogoče izboljšati. Z drugimi besedami, ko imate sledove in metrike, kako jih uporabite za presojanje agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko razvijajo (z nadgradnjami ali spreminjanjem obnašanja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pameten agent" dejansko opravlja svoje delo dobro ali pa je regressiral.

Obstajata dve kategoriji ocenjevanj za AI agente: **spletno ocenjevanje (online)** in **offline ocenjevanje**. Obe sta dragoceni in se dopolnjujeta. Običajno začnemo z offline ocenjevanjem, saj je to najmanjši potreben korak pred uvajanjem katerega koli agenta.

### Offline ocenjevanje

![Elementi nabora podatkov v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje ocenjevanje agenta v nadzorovanem okolju, običajno z uporabo testnih naborov podatkov, ne z dejanskimi uporabniškimi poizvedbami. Uporabljate skrbno pripravljene nabore podatkov, kjer veste, kakšen je pričakovani izhod ali pravilno vedenje, in nato izvajate svojega agenta na teh podatkih.

Na primer, če ste zgradili agenta za reševanje matematičnih besedilnih nalog, bi lahko imeli [testni nabor](https://huggingface.co/datasets/gsm8k) 100 problemov z znanimi odgovori. Offline ocenjevanje se pogosto izvaja med razvojem (in je lahko del CI/CD cevovodov), da se preveri izboljšave ali zaščiti pred regresijami. Prednost je, da je **ponovljivo in dobite jasne metrike natančnosti, saj imate referenčne odgovore**. Prav tako lahko simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane metrike kot je opisano zgoraj.

Ključni izziv offline ocenjevanja je zagotoviti, da je vaš testni nabor obsežen in ostane relevanten – agent se lahko dobro obnese na fiksnem testnem naboru, a naleti na zelo različne poizvedbe v produkciji. Zato bi morali testne nabore posodabljati z novimi robnimi primeri in primeri, ki odražajo realne scenarije​. Uporaben je miks majhnih "smoke test" primerov in večjih evalvacijskih nizov: majhne za hitre preglede in večje za širše metrike zmogljivosti​.

### Online ocenjevanje

![Pregled metrik opazljivosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se nanaša na ocenjevanje agenta v živo, v resničnem okolju, tj. med dejansko uporabo v produkciji. Online ocenjevanje vključuje spremljanje zmogljivosti agenta na dejanskih uporabniških interakcijah in stalno analizo izidov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrike na živem prometu. Prednost online ocenjevanja je, da **zajame stvari, ki jih morda ne pričakujete v laboratorijskih pogojih** – lahko opazite drift modela skozi čas (če učinkovitost agenta upada zaradi spremembe vzorcev vhodnih podatkov) in ujamete nepričakovane poizvedbe ali situacije, ki niso bile v vaših testnih podatkih​. To daje resnično sliko, kako se agent obnaša v naravnem okolju.

Online ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo omenjeno, in morda izvajanje shadow testov ali A/B testov (kjer nova različica agenta deluje vzporedno z obstoječo za primerjavo). Izziv je v tem, da je lahko težko pridobiti zanesljive oznake ali ocene za žive interakcije – lahko se zanašate na povratne informacije uporabnikov ali na spodnje metrike (npr. ali je uporabnik kliknil rezultat).

### Združevanje obeh

Online in offline ocenjevanja se ne izključujeta; sta zelo dopolnjujoča. Vpogledu iz spletnega spremljanja (npr. nove vrste uporabniških poizvedb, kjer se agent slabo obnese) lahko uporabite za dopolnitev in izboljšanje offline testnih nizov podatkov. Nasprotno pa agenti, ki se dobro obnesejo v offline testih, lahko z večjo gotovostjo uvajate in spremljate v produkciji.

Dejansko mnoge ekipe sprejmejo zanko:

_evaluerajte offline -> razporedite -> spremljajte online -> zberite nove primere napak -> dodajte v offline nabor podatkov -> izpopolnite agenta -> ponovite_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj je nekaj pogostih težav in morebitnih rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| Agent AI ne izvaja nalog dosledno | - Izboljšajte prompt, ki ga daste AI agentu; bodite jasni glede ciljev.<br>- Ugotovite, kje lahko razdelitev nalog na podnaloge in obravnava z več agenti pomaga. |
| Agent AI se ujame v nenehne zanke  | - Zagotovite jasna merila in pogoje za prekinitev, da agent ve, kdaj naj ustavi postopek.<br>- Za kompleksne naloge, ki zahtevajo sklepanje in načrtovanje, uporabite večji model, ki je specializiran za naloge sklepanja. |
| Klici orodij AI agenta ne delujejo dobro   | - Preizkusite in preverite izhod orodja zunaj sistema agenta.<br>- Izboljšajte definirane parametre, promte in poimenovanje orodij.  |
| Sistem z več agenti ne deluje dosledno | - Izboljšajte promte, dane vsakemu agentu, da bodo specifični in različni med seboj.<br>- Zgradite hierarhični sistem z "routing" ali kontrolnim agentom, ki določi, kateri agent je pravi. |

Veliko teh težav se lahko učinkoviteje identificira z vzpostavljeno opazljivostjo. Sledi in meritve, ki smo jih omenili prej, pomagajo natančno določiti, kje v delovnem toku agenta se pojavljajo problemi, kar naredi razhroščevanje in optimizacijo bistveno učinkovitejše.

## Upravljanje stroškov
Tukaj je nekaj strategij za upravljanje stroškov uvajanja AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLMs) se lahko dobro obnesejo v določenih agentnih primerih uporabe in bodo znatno znižali stroške. Kot je bilo omenjeno prej, je izgradnja ocenjevalnega sistema za določanje in primerjavo zmogljivosti v primerjavi z večjimi modeli najboljši način, da razumete, kako dobro se bo SLM obnesel za vaš primer uporabe. Razmislite o uporabi SLMs za preprostejše naloge, kot so razvrščanje namenov ali izluščanje parametrov, medtem ko rezervirate večje modele za zahtevno sklepanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba raznolikosti modelov in velikosti. Uporabite lahko LLM/SLM ali serverless function za usmerjanje zahtev glede na kompleksnost do najbolj primernih modelov. To bo prav tako pomagalo zmanjšati stroške in zagotoviti zmogljivost pri pravih nalogah. Na primer, usmerite preprosta poizvedovanja k manjšim, hitrejšim modelom, in drage velike modele uporabite le za zahtevne naloge sklepanja.

**Predpomnjenje odgovorov:** Prepoznavanje pogostih zahtev in nalog ter zagotavljanje odgovorov, preden gredo skozi vaš agentski sistem, je dober način za zmanjšanje količine podobnih zahtev. Lahko celo uvedete potek, ki ugotovi, kako podoben je zahtevek vašim predpomnjenim zahtevam z uporabo bolj osnovnih AI modelov. Ta strategija lahko bistveno zniža stroške za pogosto zastavljena vprašanja ali običajne delovne tokove.

## Poglejmo, kako to deluje v praksi

V [primer zvezka te sekcije](./code_samples/10-expense_claim-demo.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazljivost za spremljanje in ocenjevanje našega agenta.


### Imate še več vprašanj glede AI agentov v produkciji?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) za srečanje z drugimi učečimi se, udeležbo uradnih ur in pridobitev odgovorov na vprašanja o AI agentih.

## Prejšnja lekcija

[Oblikovni vzorec metakognicije](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Za avtoritativni vir velja izvirni dokument v njegovem izvirnem jeziku. Za pomembne informacije priporočamo strokovni prevod, opravljen s strani človeškega prevajalca. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->