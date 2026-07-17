# AI agenti v produkciji: opazovanje in ocenjevanje

[![AI agenti v produkciji](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v aplikacije v resničnem svetu, postane pomembno razumeti njihovo vedenje, spremljati njihovo učinkovitost in sistematično ocenjevati njihove rezultate.

## Cilji učenja

Po končanem tem se boste naučili/razumeli:
- Osnovne koncepte opazovanja agentov in ocenjevanja
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično ocenjevati svoje AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente zgrajene z Microsoft Agent Framework

Cilj je opremiti vas z znanjem, da svoje "črne skrinjice" agente spremenite v pregledne, upravljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zaupanja vredni. Oglejte si tudi lekcijo [Gradnja zaupanja vrednih AI agentov](../06-building-trustworthy-agents/README.md)._

## Sledi in razpone

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno prikazujejo izvajanje agentov kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (npr. obravnava uporabniške zahteve).
- **Razponi** so posamezni koraki znotraj sledi (npr. klic jezikovnega modela ali pridobivanje podatkov).

![Drevo sledi v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez opazovanja lahko AI agent deluje kot "črna skrinjica" - njegovo notranje stanje in razmišljanje sta nejasna, kar otežuje diagnosticiranje težav ali optimizacijo zmogljivosti. Z opazovanjem postanejo agenti "steklene škatle", ki nudijo preglednost, ki je ključna za gradnjo zaupanja in zagotavljanje, da delujejo kot je bilo načrtovano.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nov niz izzivov in zahtev. Opazovanje ni več "zaželeno", ampak kritična funkcionalnost:

*   **Razhroščevanje in analiza vzroka:** Ko agent ne uspe ali proizvede nepričakovan izhod, orodja za opazovanje nudijo sledi, potrebne za določitev izvora napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcij z orodji in pogojne logike.
*   **Upravljanje zakasnitev in stroškov:** AI agenti pogosto uporabljajo LLM in druge zunanje API-je, ki se zaračunavajo na token ali klic. Opazovanje omogoča natančno spremljanje teh klicev, kar pomaga prepoznati operacije, ki so pretirano počasne ali drage. To omogoča ekipam optimizacijo pozivov, izbiro učinkovitejših modelov ali preoblikovanje delovnih tokov za upravljanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** V mnogih primerih je pomembno zagotoviti, da agenti delujejo varno in etično. Opazovanje zagotavlja revizijsko sled agentovih dejanj in odločitev. To se lahko uporablja za odkrivanje in ublažitev težav, kot so vbrizgavanje pozivov, generiranje škodljive vsebine ali nepravilno ravnanje z osebnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent dal določen odgovor ali uporabil določen pripomoček.
*   **Zanke za stalno izboljševanje:** Podatki opazovanja so osnova za iterativni razvojni proces. Z nadzorovanjem uspešnosti agentov v resničnem svetu lahko ekipe prepoznajo področja za izboljšave, zberejo podatke za fino nastavitev modelov in potrdijo vpliv sprememb. To ustvarja povratno zanko, kjer vpogledi iz produkcije prek spletnega ocenjevanja obveščajo poskuse in izboljšave brez povezave, kar vodi do postopnega izboljševanja uspešnosti agenta.

## Ključni metrični podatki za sledenje

Za spremljanje in razumevanje vedenja agenta je treba slediti različnim metrikam in signalom. Čeprav se lahko specifične metrike razlikujejo glede na namen agenta, so nekatere univerzalno pomembne.

Tukaj je nekaj najpogostejših metrik, ki jih spremljajo orodja za opazovanje:

**Zakasnitev:** Kako hitro agent odgovori? Dolgi časi čakanja negativno vplivajo na uporabniško izkušnjo. Meriti je treba zakasnitev za naloge in posamezne korake z beleženjem izvajanja agentov. Na primer, agent, ki za vse klice modelov potrebuje 20 sekund, se lahko pospeši z uporabo hitrejšega modela ali z izvajanjem klicev modelov vzporedno.

**Stroški:** Kakšni so stroški na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na token ali zunanje API-je. Pogosta uporaba orodij ali več kratnih pozivov lahko hitro poveča stroške. Na primer, če agent kliče LLM petkrat za minimalno izboljšanje kakovosti, je treba oceniti, ali so stroški upravičeni ali pa bi bilo mogoče zmanjšati število klicev ali uporabiti cenejši model. Spremljanje v realnem času lahko tudi pomaga prepoznati nepričakovane vrhove (npr. napake, ki povzročajo prekomerne zanke API).

**Napake zahtevkov:** Koliko zahtevkov je agent neuspešno izvedel? To lahko vključuje API napake ali neuspešne klice orodij. Da bi naredili svojega agenta bolj robustnega v produkciji, lahko nastavite rezervne možnosti ali ponovitve. Npr. če ponudnik LLM A ni dosegljiv, preklopite na ponudnika LLM B kot rezervnega.

**Napotki uporabnikov:** Uvajanje neposrednih ocen uporabnikov prinaša dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍za/👎proti, ⭐1-5 zvezdic) ali besedilne komentarje. Dosledne negativne povratne informacije so znak, da agent ne deluje kot pričakovano.

**Implicitne povratne informacije uporabnikov:** Vedenje uporabnikov zagotavlja posredne povratne informacije tudi brez eksplicitnih ocen. To lahko vključuje takojšnje ponavljanje vprašanj, ponavljajoče se poizvedbe ali klik na gumb za ponovni poskus. Npr. če opazite, da uporabniki večkrat zastavljajo isto vprašanje, je to znak, da agent ne deluje kot pričakovano.

**Natančnost:** Kako pogosto agent proizvaja pravilne ali zaželene rezultate? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost pridobivanja informacij, zadovoljstvo uporabnikov). Prvi korak je opredeliti, kaj pomeni uspeh za vašega agenta. Natančnost lahko spremljate z avtomatiziranimi pregledi, ocenjevalnimi točkami ali oznakami dokončanosti nalog. Na primer, označevanje sledi kot "uspešne" ali "neuspešne".

**Avtomatizirane ocenjevalne metrike:** Prav tako lahko nastavite avtomatske ocene. Na primer, lahko uporabite LLM za oceno izhoda agenta, npr. ali je uporaben, natančen ali ne. Obstaja tudi več odprtokodnih knjižnic, ki pomagajo oceniti različne vidike agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali vbrizgavanja pozivov.

V praksi kombinacija teh metrik daje najboljši pregled nad zdravjem AI agenta. V [primerih zapiska](./code_samples/10-expense_claim-demo.ipynb) v tem poglavju bomo prikazali, kako te metrike izgledajo v resničnih primerih, a najprej se bomo naučili, kako izgleda tipični delovni tok ocenjevanja.

## Instrumentirajte svojega agenta

Za zbiranje podatkov o sledenju boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta, da oddaja sledi in metrike, ki jih lahko zajame, obdela in vizualizira platforma za opazovanje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) je postal industrijski standard za opazovanje LLM-jev. Zagotavlja nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvažanje telemetričnih podatkov.

Obstaja veliko knjižnic za instrumentiranje, ki ovijejo obstoječe agentske ogrodja in olajšajo izvoz OpenTelemetry razponov v orodje za opazovanje. Microsoft Agent Framework se nativno integrira z OpenTelemetry. Spodaj je primer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvajanje agenta je samodejno sledeno
    pass
```

[Primer zapiska](./code_samples/10-expense_claim-demo.ipynb) v tem poglavju bo prikazal, kako instrumentirati svojega MAF agenta.

**Ročno ustvarjanje razponov:** Čeprav knjižnice za instrumentiranje zagotavljajo dobro osnovo, so pogosto potrebni bolj podrobni ali prilagojeni podatki. Ročno lahko ustvarite razpone za dodajanje prilagojene aplikacijske logike. Še pomembneje je, da lahko obogatite samodejno ali ročno ustvarjene razpone s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo poslovno specifične podatke, vmesne izračune ali kateri koli kontekst, ki je uporaben za razhroščevanje ali analizo, na primer `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledi in razponov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agentov

Opazovanje nam daje metrike, a ocenjevanje je proces analize teh podatkov (in izvajanja testov), da določimo, kako dobro AI agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate te sledi in metrike, kako jih uporabite za presojanje agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker AI agenti pogosto niso deterministični in se lahko razvijajo (z nadgradnjami ali odmikom vedenja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pameten agent" dejansko opravlja svoje delo dobro ali je nazadoval.

Obstajata dve kategoriji ocenjevanj AI agentov: **spletno ocenjevanje** in **brez povezave ocenjevanje**. Obe sta dragoceni in se dopolnjujeta. Običajno začnemo z ocenjevanjem brez povezave, saj je to minimalni potreben korak pred uvajanjem kateregakoli agenta.

### Ocenjevanje brez povezave

![Elementi podatkovnega nabora v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Gre za ocenjevanje agenta v nadzorovanem okolju, običajno z uporabo testnih podatkovnih množic, ne pa z živimi uporabniškimi vprašanji. Uporabite kurirane podatkovne množice, kjer veste, kakšen je pričakovani izhod ali pravilno vedenje, nato pa svojega agenta preizkusite na teh.

Na primer, če ste zgradili agenta za reševanje matematičnih problemov iz besedila, lahko imate [testni podatkovni niz](https://huggingface.co/datasets/gsm8k) s 100 problemi z znanimi odgovori. Ocenjevanje brez povezave se pogosto izvaja med razvojem (in je lahko del CI/CD procesov) za preverjanje izboljšav ali zaščito pred nazadovanjem. Prednost je, da je **ponovljivo in da lahko dobite jasne metrike natančnosti, saj imate osnovni resnični podatki**. Prav tako lahko simulirate uporabniška vprašanja in merite agentove odgovore glede na idealne odgovore ali uporabite avtomatizirane metrike, kot je opisano zgoraj.

Glavni izziv pri ocenjevanju brez povezave je zagotoviti, da je vaš testni podatkovni niz obsežen in ostaja relevanten – agent se lahko dobro obnese na fiksnem testnem naboru, a v produkciji naleti na zelo različna vprašanja. Zato naj bi testne množice obnavljali z novimi primernimi primeri in primeri, ki odražajo resnične situacije. Mešanica majhnih "preizkusov dima" in večjih ocenjevalnih nizov je uporabna: majhni za hitre preglede in večji za širše metrike učinkovitosti.

### Spletno ocenjevanje

![Pregled metrik opazovanja](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Nanaša se na ocenjevanje agenta v živo, v realnem okolju, tj. med dejansko uporabo v produkciji. Spletno ocenjevanje vključuje spremljanje uspešnosti agenta pri resničnih uporabniških interakcijah in stalno analizo rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrike za živi promet. Prednost spletnega ocenjevanja je, da **zajema stvari, ki jih morda ne pričakujete v laboratorijskem okolju** – lahko opazite odmik modela skozi čas (če učinkovitost agenta upada zaradi spremembe vhodnih vzorcev) in zaznate nepričakovana vprašanja ali situacije, ki jih ni bilo v vaših testnih podatkih. Zagotavlja resnično sliko o vedenju agenta v naravi.

Spletno ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo opisano, in morda izvajanje sencnih testov ali A/B testov (kjer nova različica agenta teče vzporedno za primerjavo s staro). Izziv je, da je lahko težko pridobiti zanesljive oznake ali ocene za žive interakcije – morda se zanašate na povratne informacije uporabnikov ali naslednje metrike (npr. ali je uporabnik kliknil rezultat).

### Združevanje obeh

Spletna in brez povezave ocenjevanja se ne izključujeta, temveč se močno dopolnjujeta. Vpogledi iz spletnega spremljanja (npr. novi tipi uporabniških poizvedb, kjer agent slabo deluje) se lahko uporabijo za dopolnjevanje in izboljšanje množic testnih podatkov brez povezave. Nasprotno pa se agenti, ki se dobro obnesejo v brezžičnih testih, lahko z večjo samozavestjo uvajajo in spremljajo v spletu.

Pravzaprav številne ekipe sledijo zanki:

_oceni brez povezave -> uvedi -> spremljaj v spletu -> zbierz nove primere napak -> dodaj v brezžični nabor -> izboljšaj agenta -> ponovi_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj so nekateri pogosti problemi in njihova možna rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent ne izvaja nalog dosledno | - Izboljšajte poziv, ki ga dajete AI agentu; bodite jasni glede ciljev.<br>- Ugotovite, kje lahko naloge razdelite na podnaloge in jih obravnavate z več agenti. |
| AI agent se zatakne v nenehnih zankah | - Zagotovite jasna pravila za zaključek, da agent ve, kdaj naj ustavi proces.<br>- Za kompleksne naloge, ki zahtevajo razmišljanje in načrtovanje, uporabite večji model, specializiran za takšne naloge. |
| Klici orodij AI agenta ne delujejo dobro | - Preizkusite in potrdite izhod orodja zunaj sistema agenta.<br>- Izboljšajte definirane parametre, pozive in poimenovanja orodij. |
| Sistem z več agenti ne deluje dosledno | - Izboljšajte pozive za vsakega agenta, da so specifični in različni med seboj.<br>- Zgradite hierarhični sistem z "usmerjevalnim" ali kontrolnim agentom, ki določa, kateri agent je pravi. |

Veliko teh težav je mogoče učinkoviteje odkriti z vzpostavljenim opazovanjem. Sledi in metrike, o katerih smo prej govorili, pomagajo natančno določiti, kje v delovnem toku agenta pride do težav, kar naredi razhroščevanje in optimizacijo veliko učinkovitejšo.

## Upravljanje stroškov


Tukaj je nekaj strategij za upravljanje stroškov uvajanja AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) se lahko dobro obnesejo pri določenih agentskih primerih uporabe in bodo znatno zmanjšali stroške. Kot je bilo omenjeno prej, je najboljši način za razumevanje, kako dobro se bo SLM obnesel za vaš primer uporabe, vzpostavitev ocenjevalnega sistema za določanje in primerjavo učinkovitosti glede na večje modele. Razmislite o uporabi SLM za preprostejše naloge, kot so klasifikacija namer ali izvleček parametrov, medtem ko večje modele rezervirajte za kompleksno sklepanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba različnih modelov in velikosti. Lahko uporabite LLM/SLM ali strežniško brez funkcijo za usmerjanje zahtevkov glede na zapletenost do najbolj primernih modelov. To bo prav tako pomagalo zmanjšati stroške in hkrati zagotoviti zmogljivost pri pravih nalogah. Na primer, preproste poizvedbe usmerite na manjše, hitrejše modele, in drage velike modele uporabite samo za kompleksne naloge sklepanje.

**Predpomnjenje odgovorov:** Prepoznavanje pogostih zahtev in nalog ter zagotavljanje odgovorov, preden gredo skozi vaš agentski sistem, je dober način za zmanjšanje količine podobnih zahtev. Lahko celo implementirate tok, ki ugotavlja, kako zelo je zahteva podobna vašim predpomnjenim zahtevam z uporabo bolj osnovnih AI modelov. Ta strategija lahko znatno zmanjša stroške za pogosto zastavljena vprašanja ali pogoste delovne tokove.

## Poglejmo, kako to deluje v praksi

V [primerku zvezka tega razdelka](./code_samples/10-expense_claim-demo.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazovanje za spremljanje in ocenjevanje našega agenta.


### Imate več vprašanj o AI agentih v produkciji?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učečimi, sodelujete na urah pisarne in dobite odgovore na svoja vprašanja o AI agentih.

## Prejšnja lekcija

[Vzorec oblikovanja metacogniacije](../09-metacognition/README.md)

## Naslednja lekcija

[Agentski protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->