# AI agenti v produkciji: Opazovanje in ocenjevanje

[![AI agenti v produkciji](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v aplikacije v resničnem svetu, postane pomembna sposobnost razumevanja njihovega vedenja, spremljanja njihove uspešnosti in sistematičnega ocenjevanja njihovih izhodov.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:
- Temeljne koncepte opazovanja (observability) in ocenjevanja agentov
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično ocenjevati svoje AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente zgrajene z Microsoft Agent Framework

Cilj je opremiti vas z znanjem, da boste svoje "črne skrinjice" agente spremenili v pregledne, obvladljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zaupanja vredni. Oglejte si tudi lekcijo [Gradnja zanesljivih AI agentov](./06-building-trustworthy-agents/README.md)._

## Sledi in segmenti

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavijo izvajanja agentov kot sledi in segmente.

- **Sled** predstavlja celotno opravilo agenta od začetka do konca (npr. obdelava uporabnikove poizvedbe).
- **Segmenti** so posamezni koraki znotraj sledi (npr. klic jezikovnega modela ali pridobivanje podatkov).

![Drevo sledi v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez opazovanja lahko AI agent deluje kot "črna skrinjica" - njegovo notranje stanje in sklepanje sta neprozorna, kar otežuje diagnosticiranje težav ali optimizacijo zmogljivosti. Z opazovanjem agent postane "steklena skrinjica", ki nudi preglednost, kar je bistveno za gradnjo zaupanja in zagotavljanje delovanja v skladu s pričakovanji.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nov nabor izzivov in zahtev. Opazovanje ni več "prijeten dodatok", temveč kritična sposobnost:

*   **Razhroščevanje in analiza vzrokov (Root-Cause Analysis):** Ko agent odpove ali proizvede nepričakovan izhod, orodja za opazovanje nudijo sledi, potrebne za natančno določitev vira napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcije z orodji in pogojno logiko.
*   **Upravljanje latence in stroškov:** AI agenti pogosto temeljijo na LLM in drugih zunanjih API-jih, ki se zaračunavajo na token ali na klic. Opazovanje omogoča natančno sledenje teh klicev in pomaga odkriti operacije, ki so pretirano počasne ali drage. To ekipam omogoča optimizacijo pozivov (promptov), izbiro učinkovitejših modelov ali preoblikovanje delovnih tokov za obvladovanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** V mnogih aplikacijah je pomembno zagotoviti, da se agenti obnašajo varno in etično. Opazovanje zagotavlja revizijsko sled akcij in odločitev agenta. To lahko uporabite za odkrivanje in ublažitev težav, kot so prompt injection, generiranje škodljive vsebine ali nepravilno ravnanje z osebno prepoznatljivimi informacijami (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent dal določen odgovor ali uporabil določeno orodje.
*   **Nenehni zanke izboljševanja:** Podatki iz opazovanja so temelj iterativnega razvojnega procesa. S spremljanjem, kako agenti delujejo v resničnem svetu, ekipe lahko identificirajo področja za izboljšave, zberejo podatke za fino nastavljanje modelov in potrdijo vpliv sprememb. To ustvari povratno zanko, kjer proizvodne ugotovitve iz spletnega ocenjevanja informirajo offline eksperimentiranje in izpopolnjevanje, kar vodi do postopnega izboljševanja zmogljivosti agenta.

## Ključni kazalniki, ki jih je treba spremljati

Za spremljanje in razumevanje vedenja agenta je treba spremljati vrsto metrik in signalov. Specifične metrike se lahko razlikujejo glede na namen agenta, a nekaj je univerzalno pomembnih.

Tukaj je nekaj najpogostejših metrike, ki jih orodja za opazovanje spremljajo:

**Latenca:** Kako hitro agent odgovori? Dolgi časi čakanja negativno vplivajo na uporabniško izkušnjo. Latenco morate meriti za naloge in posamezne korake s sledenjem izvajanja agentov. Na primer, agent, ki za vse klice modela potrebuje 20 sekund, bi lahko pohitrili z uporabo hitrejšega modela ali z vzporednim izvajanjem klicev modela.

**Stroški:** Kolikšen je strošek na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na token ali zunanje API-je. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent petkrat pokliče LLM za marginalno izboljšanje kakovosti, morate oceniti, ali je strošek upravičen ali pa lahko zmanjšate število klicev ali uporabite cenejši model. Tudi spremljanje v realnem času pomaga odkriti nepričakovane skoke (npr. napake, ki povzročajo pretirane API zanke).

**Napake zahtevkov:** Koliko zahtevkov je agent neuspešno izvedel? To lahko vključuje API napake ali neuspešne klice orodij. Da bi agent v produkciji postal bolj robusten proti tem težavam, lahko nastavite povratne mehanizme ali ponovitve. Npr. če je ponudnik LLM A nedosegljiv, preklopite na ponudnika LLM B kot rezervno možnost.

**Povratne informacije uporabnikov:** Implementacija neposrednih ocen uporabnikov nudi dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍všeč/👎ne, ⭐1-5 zvezdic) ali besedne komentarje. Stalno negativno povratno informiranje naj vas opozori, saj je to znak, da agent ne deluje po pričakovanjih.

**Implicitne povratne informacije uporabnikov:** Uporabniško vedenje daje posredno povratno informacijo tudi brez eksplicitnih ocen. To lahko vključuje takojšnje preoblikovanje vprašanja, ponavljajoče se poizvedbe ali klik na gumb za ponovni poskus. Npr. če vidite, da uporabniki večkrat zastavijo isto vprašanje, je to znak, da agent ne deluje po pričakovanjih.

**Natančnost:** Kako pogosto agent proizvede pravilne ali zaželene izhode? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost iskanja informacij, zadovoljstvo uporabnikov). Prvi korak je opredeliti, kako izgleda uspeh za vašega agenta. Natančnost lahko spremljate preko avtomatiziranih preverjanj, ocenjevalnih točk ali oznak dokončanja naloge. Na primer označevanje sledi kot "uspešna" ali "neuspešna".

**Samodejni metri ocenjevanja:** Prav tako lahko nastavite samodejne ocene. Na primer, lahko uporabite LLM za ocenjevanje izhoda agenta, npr. ali je koristen, natančen ali ne. Obstaja tudi več odprtokodnih knjižnic, ki pomagajo oceniti različne vidike agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za odkrivanje škodljivega jezika ali prompt injection.

V praksi kombinacija teh metrik nudi najboljši pregled nad zdravjem AI agenta. V tem poglavju v [primeru zvezka](./code_samples/10-expense_claim-demo.ipynb) bomo prikazali, kako te metrike izgledajo na resničnih primerih, a najprej se naučimo, kako običajno poteka evalvacijski delovni proces.

## Instrumentirajte svojega agenta

Za zbiranje podatkov o sledenju boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta, da oddaja sledi in metrike, ki jih lahko zajame, obdela in vizualizira platforma za opazovanje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se je uveljavil kot industrijski standard za opazovanje LLM. Ponuja niz API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetričnih podatkov.

Obstaja veliko knjižnic za instrumentacijo, ki ovijejo obstoječe ogrodje agentov in olajšajo izvoz OpenTelemetry segmentov v orodje za opazovanje. Microsoft Agent Framework se naravno integrira z OpenTelemetry. Spodaj je primer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvajanje agenta se samodejno spremlja.
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Ročno ustvarjanje segmentov:** Čeprav knjižnice za instrumentacijo nudijo dobro izhodišče, pogosto obstajajo primeri, kjer so potrebne bolj podrobne ali prilagojene informacije. Lahko ročno ustvarite segmente, da dodate prilagojeno aplikacijsko logiko. Še pomembneje je, da lahko obogatite avtomatsko ali ročno ustvarjene segmente s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo poslovno-specifične podatke, vmesne izračune ali kateri koli kontekst, ki bi bil uporaben za razhroščevanje ali analizo, kot so `user_id`, `session_id`, ali `model_version`.

Primer ročnega ustvarjanja sledi in segmentov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agenta

Opazovanje nam daje metrike, vendar je ocenjevanje proces analiziranja teh podatkov (in izvajanja testov), da določimo, kako dobro AI agent deluje in kako ga je mogoče izboljšati. Z drugimi besedami, ko imate sledi in metrike, kako jih uporabite za presojo agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko spreminjajo (s posodobitvami ali drifitngom vedenja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pametni agent" dejansko opravlja svoje delo dobro ali pa je prišlo do regresije.

Obstajata dve kategoriji ocenjevanj za AI agente: **spletno ocenjevanje** in **offline ocenjevanje**. Obe sta dragoceni in se medsebojno dopolnjujeta. Običajno začnemo z offline ocenjevanjem, saj je to najmanjši potreben korak pred uvajanjem katerega koli agenta.

### Offline ocenjevanje

![Elementi podatkovnega nabora v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje ocenjevanje agenta v nadzorovanem okolju, običajno z uporabo testnih naborov podatkov, ne z živimi uporabniškimi poizvedbami. Uporabite kurirane nabore podatkov, kjer veste, kakšen je pričakovani izhod ali pravilno vedenje, in nato zaženete svojega agenta na teh podatkih.

Na primer, če ste ustvarili agenta za reševanje besedilnih matematičnih nalog, lahko imate [testni nabor](https://huggingface.co/datasets/gsm8k) 100 problemov z znanimi odgovori. Offline ocenjevanje se pogosto izvaja med razvojem (in je lahko del CI/CD cevovodov) za preverjanje izboljšav ali varovanja pred regresijami. Prednost je v tem, da je **ponovljivo in dobite jasne metrike natančnosti, saj imate osnovno resnico**. Prav tako lahko simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane metrike, kot je opisano zgoraj.

Ključni izziv pri offline ocenjevanju je zagotoviti, da je vaš testni nabor celovit in ostaja relevanten – agent se lahko dobro obnese na fiksnem testnem naboru, vendar v produkciji naleti na zelo različne poizvedbe. Zato je treba testne nize posodabljati z novimi robnimi primeri in primeri, ki odražajo resnične scenarije​. Uporaben je mešan pristop majhnih "smoke testov" in večjih evalvacijskih nizov: majhni se za hitro preverjanje in večji za širše metrike zmogljivosti​.

### Spletno ocenjevanje

![Pregled metrik opazovanja](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se nanaša na ocenjevanje agenta v živem, resničnem okolju, tj. med dejansko uporabo v produkciji. Spletno ocenjevanje vključuje spremljanje zmogljivosti agenta na resničnih interakcijah uporabnikov in kontinuirano analizo izidov.

Na primer, morda spremljate stopnje uspeha, ocene zadovoljstva uporabnikov ali druge metrike na žičnem prometu. Prednost spletnega ocenjevanja je, da **ujame stvari, na katere morda ne pomislite v laboratoriju** – lahko opazite drifitng modela skozi čas (če se učinkovitost agenta poslabša, ko se vzorci vhodov spremenijo) in ujamete nepričakovane poizvedbe ali situacije, ki niso bile v vaših testnih podatkih​. Ponuja resnično sliko, kako se agent obnaša v naravi.

Spletno ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo omenjeno, in morebiti izvajanje shadow testov ali A/B testov (kjer nova različica agenta deluje vzporedno za primerjavo s staro). Izziv je v tem, da je pridobivanje zanesljivih oznak ali ocen za žive interakcije lahko težavno – lahko se zanašate na povratne informacije uporabnikov ali na vzporedne metrike (npr. ali je uporabnik kliknil rezultat).

### Združevanje obeh

Spletno in offline ocenjevanje nista nasprotji; sta zelo dopolnjujoča. Ugotovitve iz spletnega spremljanja (npr. nove vrste uporabniških poizvedb, kjer se agent slabo obnese) lahko uporabite za dopolnitev in izboljšanje offline testnih podatkov. Nasprotno pa lahko agenti, ki se dobro obnesejo v offline testih, bolj samozavestno uvedete in spremljate v živo.

Dejansko mnoge ekipe sprejmejo zanko:

_oceni offline -> razporedi -> spremljaj online -> zberi nove primere napak -> dodaj v offline nabor -> izpopolni agenta -> ponovi_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko pojavijo različni izzivi. Tukaj je nekaj pogostih težav in njihovih možnih rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent ne izvaja nalog dosledno | - Izboljšajte navodila (prompt) dani AI agentu; bodite jasni glede ciljev.<br>- Določite, kje lahko razdelitev nalog na podnaloge in obdelava s strani več agentov pomaga. |
| AI agent se zatika v neskončne zanke  | - Poskrbite za jasna merila za zaključek, da agent ve, kdaj naj prekine postopek.<br>- Za kompleksne naloge, ki zahtevajo sklepanja in načrtovanje, uporabite večji model, specializiran za reševanje takih nalog. |
| Klici orodij AI agenta niso učinkoviti   | - Preizkusite in preverite izhod orodja zunaj sistema agenta.<br>- Izboljšajte definirane parametre, navodila (prompt) in poimenovanje orodij.  |
| Sistem več agentov ne deluje dosledno | - Izboljšajte navodila, dane vsakemu agentu, da zagotovite, da so specifična in različna med seboj.<br>- Zgradite hierarhični sistem z uporabo "routing" ali kontrolnega agenta, ki določi, kateri agent je pravi. |

Številne od teh težav je mogoče učinkoviteje odkriti z vzpostavljenim opazovanjem. Sledi in metrike, ki smo jih prej omenili, pomagajo natančno določiti, kje v delovnem toku agenta se pojavijo težave, kar naredi razhroščevanje in optimizacijo veliko bolj učinkovito.

## Upravljanje stroškov
Tukaj je nekaj strategij za obvladovanje stroškov uvajanja AI agentov v produkcijo:

**Using Smaller Models:** Small Language Models (SLMs) can perform well on certain agentic use-cases and will reduce costs significantly. As mentioned earlier, building an evaluation system to determine and compare performance vs larger models is the best way to understand how well an SLM will perform on your use case. Consider using SLMs for simpler tasks like intent classification or parameter extraction, while reserving larger models for complex reasoning.

**Using a Router Model:** Podoben pristop je uporaba različnih modelov in velikosti. Uporabite lahko LLM/SLM ali brezstrežniško funkcijo, da usmerjate zahteve glede na kompleksnost do najbolj primernih modelov. To bo prav tako pomagalo znižati stroške in hkrati zagotavljalo ustrezno zmogljivost za prave naloge. Na primer, enostavne poizvedbe usmerite na manjše, hitrejše modele in drage velike modele uporabite le za naloge zahtevnega sklepanja.

**Caching Responses:** Identificiranje pogostih zahtev in opravil ter priprava odgovorov, preden gredo skozi vaš agentni sistem, je dober način za zmanjšanje števila podobnih zahtev. Lahko celo izvedete tok, ki oceni, kako podobna je zahteva vašim predpomnjenim zahtevam, z uporabo bolj osnovnih AI modelov. Ta strategija lahko znatno zniža stroške za pogosto zastavljena vprašanja ali pogoste delovne tokove.

## Poglejmo, kako to deluje v praksi

V [primeru zvezka tega razdelka](./code_samples/10-expense_claim-demo.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazovanje za spremljanje in ocenjevanje našega agenta.


### Imate več vprašanj glede AI agentov v produkciji?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi udeleženci, udeležite ur za vprašanja in dobite odgovore na svoja vprašanja o AI agentih.

## Prejšnja lekcija

[Oblikovni vzorec metakognicije](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco Co-op Translator (https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor­nem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->