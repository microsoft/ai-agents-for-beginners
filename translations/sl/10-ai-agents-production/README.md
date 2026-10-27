# AI agenti v produkciji: opazovanje in ocenjevanje

[![AI Agents in Production](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v realne uporabe, postaja pomembno razumeti njihovo vedenje, spremljati njihovo učinkovitost in sistematično vrednotiti njihove rezultate.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:
- Osnovne pojme opazovanja in ocenjevanja agentov
- Tehnike za izboljšanje učinkovitosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično ocenjevati svoje AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente, zgrajene z Microsoft Agent Frameworkom

Cilj je opremiti vas z znanjem, kako pretvoriti svoje "črne skrinjice" agente v pregledne, obvladljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zaupanja vredni. Oglejte si tudi lekcijo [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Sledi in razponi

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo zagone agentov kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (na primer obdelava uporabniškega poizvedovanja).
- **Razponi** so posamezni koraki znotraj sledi (na primer klic jezikovnega modela ali pridobivanje podatkov).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez opazovanja se AI agent lahko zdi kot "črna skrinjica" - njegovo notranje stanje in razmišljanje sta neprozorna, zaradi česar je težko diagnosticirati težave ali optimizirati delovanje. Z opazovanjem agent postane "steklena skrinjica", ki nudi preglednost, pomembno za gradnjo zaupanja in zagotavljanje, da deluje kot je bilo predvideno.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nov nabor izzivov in zahtev. Opazovanje ni več "lep dodatek", temveč ključna zmogljivost:

*   **Razhroščevanje in analiza osnovnega vzroka:** Ko agent ne uspe ali ustvari nepričakovan rezultat, orodja za opazovanje zagotovijo sledi, potrebne za natančno določitev izvora napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcije z orodji in pogojno logiko.
*   **Upravljanje latence in stroškov:** AI agenti pogosto temeljijo na LLM-jih in drugih zunanjih API-jih, ki se zaračunavajo na token ali klic. Opazovanje omogoča natančno sledenje tem klicem, kar pomaga prepoznati operacije, ki so prepočasi ali predrage. To ekipam omogoča optimizacijo pozivov, izbiro učinkovitejših modelov ali prenovo delovnih tokov za obvladovanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** Pri mnogih aplikacijah je pomembno zagotoviti, da agenti delujejo varno in etično. Opazovanje zagotavlja revizijsko sled delovanja in odločitev agenta. To se lahko uporabi za zaznavanje in ublažitev težav, kot so injekcija pozivov, ustvarjanje škodljive vsebine ali neustrezno ravnanje z osebnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent podal določen odgovor ali uporabil določeno orodje.
*   **Zanke nenehnega izboljševanja:** Podatki o opazovanju so osnova iterativnega razvojnega procesa. Z spremljanjem, kako agenti delujejo v resničnem svetu, lahko ekipe prepoznajo področja za izboljšave, zberejo podatke za natančno prilagajanje modelov in potrdijo učinek sprememb. To ustvarja povratno zanko, kjer produkcijski vpogledi iz spletne ocene vplivajo na eksperimentiranje in izboljšave brez povezave, kar vodi do postopoma boljše učinkovitosti agentov.

## Ključni merljivi podatki za sledenje

Za spremljanje in razumevanje vedenja agenta bi morali slediti različnim meritvam in signalom. Čeprav se lahko specifične meritve razlikujejo glede na namen agenta, so nekatere univerzalno pomembne.

Tukaj je nekaj najpogostejših meritev, ki jih orodja za opazovanje spremljajo:

**Latenca:** Kako hitro agent odgovori? Dolge čakalne dobe negativno vplivajo na uporabniško izkušnjo. Latenco za naloge in posamezne korake morate meriti s sledenjem zagonom agenta. Na primer, agent, ki za vse klice modela potrebuje 20 sekund, bi lahko pohitrili z uporabo hitrejšega modela ali s paralelnim izvajanjem klicev modela.

**Stroški:** Kakšni so stroški na posamezen zagon agenta? AI agenti temeljijo na klicih LLM, ki se zaračunavajo na token ali zunanji API-ji. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent LLM kliče petkrat za manjšo izboljšavo kakovosti, morate oceniti, ali so stroški upravičeni ali bi lahko zmanjšali število klicev ali uporabili cenejši model. Spremljanje v realnem času lahko pomaga tudi pri odkrivanju nepričakovanih skokov (npr. napake, ki povzročajo pretirano število klicev API).

**Napake zahtevkov:** Koliko zahtevkov je agent neuspešno obdelal? To lahko vključuje napake API ali neuspešne klice orodij. Da naredite svojega agenta bolj robustnega proti tem težavam v produkciji, lahko nastavite rezervne možnosti ali ponovitve. Npr. če LLM ponudnik A ne deluje, preklopite na LLM ponudnika B kot rezervno možnost.

**Povratne informacije uporabnikov:** Direktne ocene uporabnikov nudijo dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍všeč/👎ne, ⭐1-5 zvezdic) ali besedilne komentarje. Konsistentne negativne povratne informacije naj bi vas opozorile, saj je to znak, da agent ne deluje po pričakovanjih.

**Implicitne povratne informacije uporabnikov:** Vedenje uporabnikov zagotavlja neposredne povratne informacije tudi brez eksplicitnih ocen. To lahko vključuje takojšnje ponovne formulacije vprašanj, ponavljajoče se poizvedbe ali klik na gumb za ponovni poskus. Npr. če opazite, da uporabniki večkrat zastavljajo isto vprašanje, je to znak, da agent ne deluje po pričakovanjih.

**Natančnost:** Kako pogosto agent proizvaja pravilne ali zaželene rezultate? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost pridobivanja informacij, zadovoljstvo uporabnikov). Prvi korak je definirati, kaj pomeni uspeh za vašega agenta. Natančnost lahko spremljate preko avtomatiziranih preverjanj, ocen evalvacije ali oznak dokončanih nalog. Na primer, označevanje sledi kot "uspešno" ali "neuspešno".

**Avtomatizirane metrike ocenjevanja:** Lahko nastavite tudi avtomatizirane ocene. Na primer, lahko uporabite LLM za oceno izhoda agenta, npr. ali je koristen, natančen ali ne. Na voljo je tudi več odprtokodnih knjižnic, ki vam pomagajo oceniti različne vidike agenta. Na primer [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://github.com/protectai/llm-guard) za zaznavanje škodljivega jezika ali injekcije pozivov.

V praksi kombinacija teh meritev nudi najboljši pregled nad stanjem AI agenta. V tem poglavju vas bomo s pomočjo [primernega zvezka](./code_samples/10-expense_claim-demo.ipynb) vodili, kako te meritve izgledajo v resničnih primerih, najprej pa se bomo naučili, kako poteka tipičen proces ocenjevanja.

## Instrumentirajte svojega agenta

Za zbiranje podatkov sledenja boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta, da oddaja sledi in meritve, ki jih lahko zajema, obdela in vizualizira platforma za opazovanje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) je postal industrijski standard za opazovanje LLM. Nudi nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetričnih podatkov.

Obstaja veliko instrumentacijskih knjižnic, ki ovijejo obstoječe agentne okvire in olajšajo izvoz OpenTelemetry razponov v orodje za opazovanje. Microsoft Agent Framework se nativno integrira z OpenTelemetry. Spodaj je primer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

V [primerju zvezka](./code_samples/10-expense_claim-demo.ipynb) v tem poglavju bomo prikazali, kako instrumentirati vaš MAF agent.

**Ročno ustvarjanje razponov:** Čeprav instrumentacijske knjižnice nudijo dobro osnovo, so pogosto potrebni bolj podrobni ali prilagojeni podatki. Lahko ročno ustvarite razpone za dodajanje prilagojene aplikativne logike. Pomembneje je, da lahko avtomatsko ali ročno ustvarjeni razponi bogatijo lastnosti (znane tudi kot oznake ali metapodatki). Te lastnosti lahko vključujejo podatke specifične za poslovanje, vmesne izračune ali kateri koli kontekst, ki je lahko uporaben pri razhroščevanju ali analizi, kot so `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledi in razponov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agenta

Opazovanje nam daje meritve, ocenjevanje pa je proces analize teh podatkov (in izvajanja testov), da določimo, kako dobro agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate te sledi in meritve, kako jih uporabite za presojo agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko razvijajo (prek posodobitev ali spreminjanja vedenja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pameten agent" dejansko opravlja svoje delo dobro ali se je poslabšal.

Obstajata dve kategoriji ocenjevanj za AI agente: **spletno ocenjevanje** in **brez povezave ocenjevanje**. Obe sta dragoceni in se dopolnjujeta. Običajno začnemo z ocenjevanjem brez povezave, saj je to minimalni potrebni korak pred uvajanjem katerega koli agenta.

### Ocenjevanje brez povezave

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje ocenjevanje agenta v kontroliranem okolju, običajno z uporabo testnih podatkovnih nizov, ne z živimi uporabniškimi poizvedbami. Uporabite skrbno izbrane podatke, kjer veste, kakšen je pričakovani izhod ali pravilno vedenje, nato pa na njih zaženete agenta.

Na primer, če ste zgradili matematičnega agenta za besedilne probleme, imate morda [testni podatkovni niz](https://huggingface.co/datasets/openai/gsm8k) s 100 problemi z znanimi odgovori. Ocenjevanje brez povezave se pogosto izvaja med razvojem (in je lahko del CI/CD procesov) za preverjanje izboljšav ali zaščito pred poslabšanji. Prednost je, da je **ponovljivo in lahko dobite jasne meritve natančnosti, saj imate osnovno resnico**. Prav tako lahko simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane meritve, kot je opisano zgoraj.

Glavni izziv pri ocenjevanju brez povezave je zagotoviti, da je vaš testni podatkovni niz celovit in ostaja relevanten – agent morda dobro deluje na fiksnem testnem naboru, a se v produkciji srečuje z zelo drugačnimi poizvedbami. Zato bi morali testne nize redno posodabljati z novimi robnimi primeri in primeri, ki odražajo scenarije iz resničnega sveta. Koristna je kombinacija majhnih "hitrih testov" in večjih ocenjevalnih nizov: majhnih za hitre preverbe in večjih za širše metrike učinkovitosti.

### Spletno ocenjevanje

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To pomeni ocenjevanje agenta v živo, v realnem okolju, torej med dejansko uporabo v produkciji. Spletno ocenjevanje vključuje spremljanje učinkovitosti agenta na dejanskih uporabniških interakcijah in stalno analizo rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge meritve na živi prometni obremenitvi. Prednost spletnega ocenjevanja je, da **ujame stvari, ki jih v laboratorijskem okolju ne bi pričakovali** – lahko opazite drsenje modela skozi čas (če učinkovitost agenta upada zaradi sprememb vzorcev vhodnih podatkov) in zaznate nepričakovane poizvedbe ali situacije, ki jih v testnih podatkih ni bilo. Zagotavlja resnično sliko, kako agent deluje v naravnem okolju.

Spletno ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot smo že omenili, in morda izvajanje sence testov ali A/B testov (kjer nova verzija agenta deluje vzporedno s staro za primerjavo). Izziv je, da je lahko težko pridobiti zanesljive etikete ali ocene za žive interakcije – lahko se zanesete na povratne informacije uporabnikov ali spodnje meritve (npr. ali je uporabnik kliknil rezultat).

### Združevanje obeh

Spletna in brez povezave ocenjevanja nista izključujoči se; sta zelo dopolnjujoči. Vpoglede iz spletnega spremljanja (npr. nove vrste uporabniških poizvedb, kjer agent slabo deluje) je mogoče uporabiti za izboljšanje in nadgradnjo testnih nizov brez povezave. Nasprotno pa lahko agente, ki dobro delujejo v testih brez povezave, z večjim zaupanjem uvajamo in spremljamo v spletu.

Pravzaprav mnoge ekipe sprejmejo zanko:

_oceni brez povezave -> uvajaj -> spremljaj spletno -> zbiraj nove primere napak -> dodaj v testni niz brez povezave -> izpopolni agenta -> ponovi_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj so nekatere pogoste težave in njihove potencialne rešitve:

| **Težava**    | **Potencialna rešitev**   |
| ------------- | ------------------ |
| AI agent naloge ne izvaja dosledno | - Izpopolnite poziv, dan AI agentu; bodite jasni glede ciljev.<br>- Prepoznajte, kje razdelitev nalog na podnaloge, ki jih obravnava več agentov, lahko pomaga. |
| AI agent ujame nenehne zanke  | - Poskrbite za jasne pogoje za prekinitev, da agent ve, kdaj ustaviti proces.<br>- Za kompleksne naloge, ki zahtevajo razumevanje in načrtovanje, uporabite večji model, specializiran za te naloge. |
| Klici orodij AI agenta ne delujejo dobro   | - Testirajte in preverite izhod orodja izven sistema agenta.<br>- Izboljšajte definirane parametre, pozive in poimenovanja orodij.  |
| Sistem z več agenti ne deluje dosledno | - Izpopolnite pozive za vsak agent, da bodo specifični in različni med seboj.<br>- Zgradite hierarhični sistem z "usmerjevalnim" ali krmilnim agentom, ki določi, kateri agent je pravi. |

Veliko teh težav je mogoče bolje prepoznati z vzpostavljenim opazovanjem. Sledi in meritve, o katerih smo govorili, pomagajo natančno določiti, kje v delovnem toku agenta se težave pojavljajo, kar bistveno olajša razhroščevanje in optimizacijo.

## Upravljanje stroškov

Tukaj je nekaj strategij za obvladovanje stroškov uvajanja AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) lahko dobro delujejo pri določenih agentskih primerih uporabe in bodo znatno znižali stroške. Kot smo že omenili, je gradnja evaluacijskega sistema za določanje in primerjavo zmogljivosti v primerjavi z večjimi modeli najboljši način, da razumete, kako dobro bo SLM deloval za vaš primer uporabe. Razmislite o uporabi SLM za preprostejše naloge, kot so klasifikacija namenov ali izvleček parametrov, medtem ko večje modele rezervirajte za kompleksno razmišljanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba različnih modelov in velikosti. Za usmerjanje zahtev na modele, ki so najprimernejši glede na zahtevnost, lahko uporabite LLM/SLM ali funkcijo brez strežnika. To bo prav tako pomagalo zmanjšati stroške, hkrati pa zagotoviti zmogljivost pri pravih nalogah. Na primer, preproste poizvedbe usmerite na manjše, hitrejše modele, drage velike modele pa uporabite le za zahtevnejše naloge razmišljanja.

**Predpomnjenje odzivov:** Prepoznavanje pogostih zahtev in nalog ter zagotavljanje odgovorov, še preden gredo skozi vaš agentski sistem, je dober način za zmanjšanje količine podobnih zahtev. Lahko celo izvedete potek za ugotavljanje, kako podobna je zahteva vašim predpomnjenim zahtevam, z uporabo osnovnejših modelov AI. Ta strategija lahko znatno zmanjša stroške pri pogosto zastavljenih vprašanjih ali pogostih potekih dela.

## Poglejmo, kako to deluje v praksi

V [primerku zapiskov tega razdelka](./code_samples/10-expense_claim-demo.ipynb) si bomo ogledali primere, kako lahko uporabimo orodja za opazovanje za spremljanje in ocenjevanje našega agenta.


### Imate še več vprašanj o AI agentih v produkciji?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge udeležence, obiskujete uradne ure in dobite odgovore na svoja vprašanja o AI agentih.

## Prejšnja lekcija

[Vzorec načrtovanja metakognicije](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->