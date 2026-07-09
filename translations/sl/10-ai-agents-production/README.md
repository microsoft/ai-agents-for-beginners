# AI agenti v produkciji: Opazovanje in evalvacija

[![AI agenti v produkciji](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v aplikacije v realnem svetu, postaja pomembna sposobnost razumevanja njihovega vedenja, spremljanja njihove uspešnosti in sistematične evalvacije njihovih izhodov.

## Cilji učenja

Po končanem učenju boste znali/razumeli:
- Osnovne koncepte opazovanja in evalvacije agentov
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično evalvirati vaše AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente zgrajene z Microsoft Agent Framework

Cilj je opremiti vas z znanjem, da vaše »črne skrinjice« agentov spremenite v transparentne, obvladljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zaupanja vredni. Preverite tudi lekcijo [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Sledi in odseki

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo izvajanje agenta kot sledi in odseke.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (npr. obdelava uporabnikovega poizvedka).
- **Odseki** so posamezni koraki znotraj sledi (npr. klic jezikovnega modela ali pridobivanje podatkov).

![Sled drevesa v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez možnosti opazovanja je AI agent lahko videti kot »črna skrinjica« – njegovo notranje stanje in razmišljanje sta nejasna, kar otežuje diagnosticiranje težav ali optimizacijo uspešnosti. Z opazovanjem agent postane »steklena skrinjica«, ki ponuja preglednost, pomembno za gradnjo zaupanja in zagotavljanje pravilnega delovanja.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nov sklop izzivov in zahtev. Opazovanje ni več »prijeten dodatek«, ampak ključna sposobnost:

*   **Razhroščevanje in analiza vzrokov:** Ko agent odpove ali ustvari nepričakovan izhod, orodja za opazovanje zagotovijo sledi za natančno določitev izvora napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcije z orodji in pogojno logiko.
*   **Upravljanje latence in stroškov:** AI agenti pogosto uporabljajo LLM in druge zunanje API-je, ki se zaračunavajo na token ali klic. Opazovanje omogoča natančno sledenje tem klicem, pomaga prepoznati operacije, ki so prepočasi ali predrage. To ekipam omogoča optimizacijo pozivov, izbiro učinkovitejših modelov ali prenovo potekov dela za upravljanje stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** V mnogih aplikacijah je pomembno zagotoviti, da agenti delujejo varno in etično. Opazovanje zagotavlja revizijsko sled dejanj in odločitev agenta. To se lahko uporabi za odkrivanje in ublažitev težav, kot so injekcije pozivov, generiranje škodljive vsebine ali nepravilno ravnanje z osebnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent podal določen odgovor ali uporabil specifično orodje.
*   **Zanke za nenehno izboljševanje:** Podatki opazovanja so osnova iterativnega razvojnega procesa. S spremljanjem, kako agenti delujejo v resničnem svetu, ekipe prepoznajo področja za izboljšave, zbirajo podatke za fino nastavljanje modelov in potrjujejo vpliv sprememb. To ustvarja povratno zanko, kjer produkcijski vpogledi iz spletne evalvacije usmerjajo eksperimentiranje in izboljšave v offlinu, kar vodi do postopoma boljše uspešnosti agentov.

## Ključni metrični kazalniki za spremljanje

Za spremljanje in razumevanje vedenja agenta je treba slediti več metričnim kazalnikom in signalom. Čeprav se specifični metrični kazalniki lahko razlikujejo glede na namen agenta, so nekateri univerzalno pomembni.

Tu so nekateri najpogostejši metrični kazalniki, ki jih spremljajo orodja za opazovanje:

**Latenca:** Kako hitro agent odgovori? Dolge čakalne dobe negativno vplivajo na uporabniško izkušnjo. Merite latenco za naloge in posamezne korake z analiziranjem izvajanja agentov. Na primer, agent, ki za vse klice modela porabi 20 sekund, se lahko pospeši z uporabo hitrejšega modela ali z izvajanjem klicev modela vzporedno.

**Stroški:** Kakšen je strošek na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na token ali zunanje API-je. Pogosta uporaba orodij ali več pozivov hitro poveča stroške. Na primer, če agent petkrat kliče LLM za minimalno izboljšanje kakovosti, morate oceniti, ali je strošek upravičen ali ali lahko zmanjšate število klicev ali uporabite cenejši model. Spremljanje v realnem času lahko pomaga tudi pri zaznavanju nepričakovanih skokov (npr. hrošči, ki povzročajo prekomerne zanke API).

**Napake zahtev:** Koliko zahtev je agent zatajil? To lahko vključuje napake API ali neuspešne klice orodij. Da bi bil agent bolj odporen proti tem v produkciji, lahko nastavite nadomestne poti ali ponovitve. Npr., če LLM ponudnik A odpove, preklopite na LLM ponudnika B kot rezervno možnost.

**Uporabniški odziv:** Implementacija neposrednih uporabniških evalvacij prinaša dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍všeč/👎ne, ⭐1-5 zvezdic) ali besedilne komentarje. Konstantno negativni odziv naj vas opozori, saj je to znak, da agent ne deluje po pričakovanjih.

**Implicitni uporabniški odziv:** Uporabniško vedenje zagotavlja posredno povratno informacijo tudi brez eksplicitnih ocen. To lahko vključuje takojšnje ponovne formulacije vprašanj, ponavljajoče poizvedbe ali klik na gumb za ponovni poskus. Npr., če vidite, da uporabniki večkrat zastavljajo isto vprašanje, je to znak, da agent ne deluje po pričakovanjih.

**Natančnost:** Kako pogosto agent proizvaja pravilne ali zaželene izhode? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost pridobivanja informacij, zadovoljstvo uporabnikov). Prvi korak je definirati, kako uspeh izgleda za vašega agenta. Lahko spremljate natančnost preko avtomatiziranih preverjanj, evalvacijskih ocen ali oznak za dokončanje nalog. Na primer označevanje sledov kot »uspešno« ali »neuspešno«.

**Avtomatizirani evalvacijski metrični kazalniki:** Prav tako lahko nastavite avtomatizirane evalvacije. Na primer, lahko uporabite LLM za ocenjevanje izhoda agenta, npr. ali je uporaben, natančen ali ne. Obstaja tudi več odprtokodnih knjižnic, ki pomagajo ocenjevati različne vidike agenta. Npr. [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali injekcije pozivov.

V praksi kombinacija teh metričnih kazalnikov zagotavlja najbolj celosten vpogled v stanje AI agenta. V [primerku zvezka](./code_samples/10-expense_claim-demo.ipynb) v tem poglavju vam bomo prikazali, kako ti metrični kazalniki izgledajo v resničnih primerih, a najprej se bomo naučili, kako tipičen postopek evalvacije poteka.

## Instrumentirajte svojega agenta

Za zbiranje podatkov sledilnika boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta tako, da oddaja sledi in metrične kazalnike, ki jih lahko prestreže, obdela in vizualizira platforma za opazovanje.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) je postal industrijski standard za opazovanje LLM. Nudi nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetričnih podatkov.

Obstaja veliko knjižnic za instrumentacijo, ki obdajajo obstoječe okvire agentov in olajšajo izvoz OpenTelemetry odsekov v orodje za opazovanje. Microsoft Agent Framework se nativno povezuje z OpenTelemetry. Spodaj je primer instrumentacije MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvedba agenta se samodejno sledi
    pass
```

V [primerku zvezka](./code_samples/10-expense_claim-demo.ipynb) tega poglavja bomo pokazali, kako instrumentirati vašega MAF agenta.

**Ročno ustvarjanje odsekov:** Čeprav knjižnice za instrumentacijo zagotavljajo dobro osnovo, so pogosto potrebni bolj podrobni ali prilagojeni podatki. Lahko ročno ustvarite odseke za dodajanje prilagojene logike aplikacije. Še pomembneje, lahko obogatite samodejno ali ročno ustvarjene odseke s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo podatke specifične za poslovanje, vmesne izračune ali kakršen koli kontekst, uporaben za razhroščevanje ali analizo, kot so `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledi in odsekov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evalvacija agenta

Opazovanje nam daje metrične kazalnike, vendar je evalvacija proces analiziranja teh podatkov (ter izvajanja testov), da določimo, kako dobro AI agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate te sledi in metrične kazalnike, kako jih uporabite za presojo agenta in sprejemanje odločitev?

Redna evalvacija je pomembna, saj so AI agenti pogosto nedeterministični in se lahko razvijajo (skozi posodobitve ali pojemanje vedenja modela) – brez evalvacije ne bi vedeli, ali vaš »pametni agent« dejansko dobro opravlja svoje delo ali je nazadoval.

Evalvacije AI agentov delimo v dve kategoriji: **spletna evalvacija** in **offline evalvacija**. Obe vrednoti, dopolnjujeta se. Pogosto začnemo z offline evalvacijo, saj je to minimalni potreben korak pred uvajanjem agenta.

### Offline evalvacija

![Postavke nabora podatkov v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje evalvacijo agenta v nadzorovanem okolju, običajno z uporabo testnih podatkovnih nizov, ne uporabniških poizvedb v živo. Uporabite skrbno izbrane podatkovne nize, za katere veste, kakšen je pričakovani izhod ali pravilno vedenje, in nato izvedete vašega agenta.

Na primer, če ste zgradili agenta za reševanje matematičnih besedilnih nalog, lahko imate [testni podatkovni niz](https://huggingface.co/datasets/gsm8k) 100 problemov z znanimi odgovori. Offline evalvacija se pogosto izvaja med razvojem (in je lahko del CI/CD procesov) za preverjanje izboljšav ali zaščito pred regresijami. Prednost je, da je **ponovljiva in pridobite jasne metrične kazalnike natančnosti, saj imate osnovno resnico**. Lahko tudi simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane metrične kazalnike, kot je opisano zgoraj.

Ključni izziv pri offline evalvaciji je zagotavljanje, da je vaš testni podatkovni niz celovit in aktualen – agent se lahko dobro obnese na fiksnem testnem naboru, vendar v produkciji naleti na zelo različne poizvedbe. Zato morate testne nize redno posodabljati z novimi robnimi primeri in primeri, ki odražajo realne scenarije. Koristna je mešanica majhnih »testov dima« in večjih evalvacijskih nizov: majhni za hitre kontrole, večji za širše metrične kazalnike uspešnosti.

### Online evalvacija

![Pregled metričnih kazalnikov opazovanja](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se nanaša na evalvacijo agenta v živo, v realnem okolju, tj. med dejansko uporabo v produkciji. Online evalvacija vključuje spremljanje uspešnosti agenta pri resničnih uporabniških interakcijah in kontinuirano analizo rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrične kazalnike za promet v živo. Prednost online evalvacije je, da **ujame stvari, ki jih ne bi pričakovali v laboratorijskem okolju** – lahko opazujete pojemanje modela skozi čas (če učinkovitost agenta upada, ko se vzorci vhodnih podatkov spreminjajo) in zaznate nepričakovane poizvedbe ali situacije, ki niso bile v testnih podatkih. Zagotavlja resnično sliko, kako agent deluje v praksi.

Online evalvacija pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo omenjeno, in morda izvajanje sencnih testov ali A/B testov (kjer nova različica agenta teče vzporedno za primerjavo s staro). Izziv je v tem, da je težko pridobiti zanesljive oznake ali ocene za interakcije v živo – lahko se zanašate na povratne informacije uporabnikov ali metrične kazalnike v nadaljnjem toku (npr. ali je uporabnik kliknil rezultat).

### Kombiniranje obeh

Online in offline evalvacije se ne izključujeta; sta zelo dopolnjujoči se. Ugotovitve iz spletnega spremljanja (npr. nove vrste uporabniških poizvedb, kjer agent deluje slabo) se lahko uporabijo za dopolnitev in izboljšanje offline testnih nizov. Obratno, agenti, ki se dobro obnesejo v offline testih, se lahko nato bolj samozavestno uvajajo in spremljajo v živo.

Pravzaprav številne ekipe uporabljajo zanko:

_offline evalvacija -> uvajanje -> spletno spremljanje -> zbiranje novih primerov napak -> dodajanje v offline podatkovni niz -> izboljšava agenta -> ponavljanje_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj so nekaj pogostih težav in njihovih možnih rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent naloge ne izvaja dosledno | - Izboljšajte pozive, ki jih dajete AI agentu; bodite jasni glede ciljev.<br>- Ugotovite, ali lahko razdelitev nalog na podnaloge in njihovo obdelavo z več agenti pomaga. |
| AI agent se uvrsti v neskončne zanke | - Zagotovite jasne pogoje za zaključek, da agent ve, kdaj ustaviti proces.<br>- Za kompleksne naloge, ki zahtevajo razmišljanje in načrtovanje, uporabite večji model, specializiran za razmislek. |
| Klici orodij AI agenta se ne obnesejo dobro | - Testirajte in preverite izhod orodja zunaj sistema agenta.<br>- Izboljšajte definirane parametre, pozive in poimenovanje orodij. |
| Multii-agentni sistem ne deluje dosledno | - Izboljšajte pozive, ki jih dajete vsakemu agentu, da bodo specifični in različni drug od drugega.<br>- Zgradite hierarhični sistem z »usmerjevalnim« ali krmilnim agentom, ki določi, kateri agent je pravi. |

Veliko teh težav je mogoče učinkoviteje zaznati z vključenim opazovanjem. Sledi in metrični kazalniki, o katerih smo govorili, pomagajo natančno določiti, kje v poteku dela agenta nastajajo težave, kar bistveno izboljša razhroščevanje in optimizacijo.

## Upravljanje stroškov


Tukaj je nekaj strategij za upravljanje stroškov uvedbe AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) lahko dobro delujejo pri določenih agentnih primerih uporabe in bodo stroške znatno zmanjšali. Kot smo že omenili, je najboljši način za razumevanje, kako dobro bo SLM deloval za vaš primer uporabe, izgradnja ocenjevalnega sistema za določanje in primerjavo zmogljivosti v primerjavi z večjimi modeli. Uporabite SLM za preprostejše naloge, kot so klasifikacija namena ali izvlek parametrov, medtem ko rezervirate večje modele za kompleksno sklepanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba raznolikosti modelov in velikosti. Za usmerjanje zahtev glede na kompleksnost na najbolj primerne modele lahko uporabite LLM/SLM ali strežniško funkcijo brez strežnika. To bo prav tako pomagalo zmanjšati stroške, obenem pa zagotovilo zmogljivost pri pravih nalogah. Na primer, preproste poizvedbe preusmerite na manjše, hitrejše modele in drage velike modele uporabite le za kompleksne naloge sklepanja.

**Predpomnjenje odgovorov:** Identificiranje pogostih zahtev in nalog ter zagotavljanje odgovorov, preden zanje zaprosite vaš agentni sistem, je dober način za zmanjšanje obsega podobnih zahtev. Lahko celo implementirate tok za določanje, kako podobna je zahteva tistim v predpomnilniku, z uporabo osnovnejših AI modelov. Ta strategija lahko znatno zmanjša stroške za pogosto zastavljena vprašanja ali pogoste delovne tokove.

## Poglejmo, kako to deluje v praksi

V [primerku zvezka tega razdelka](./code_samples/10-expense_claim-demo.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazovanje za nadzor in ocenjevanje našega agenta.


### Imate več vprašanj o AI agentih v produkciji?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, obiskujete uradne ure in dobite odgovore na vaša vprašanja o AI agentih.

## Prejšnja lekcija

[Vzorec načrtovanja metakognicije](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->