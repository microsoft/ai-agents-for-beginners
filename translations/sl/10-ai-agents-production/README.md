# AI Agentje v proizvodnji: Opazljivost in ocenjevanje

[![AI Agentje v proizvodnji](../../../translated_images/sl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agentje prehajajo iz eksperimentalnih prototipov v aplikacije v resničnem svetu, postaja pomembna sposobnost razumevanja njihovega vedenja, spremljanja njihove zmogljivosti in sistematičnega ocenjevanja njihovih izhodov.

## Cilji učenja

Po končani tej lekciji boste razumeli/znali:
- Osnovne koncepte opazljivosti in ocenjevanja agentov
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično ocenjevati vaše AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v proizvodnjo
- Kako instrumentirati agente, zgrajene z Microsoft Agent Framework

Cilj je, da vas opremimo z znanjem za preoblikovanje vaših "črnih skrinjic" agentov v pregledne, upravljalne in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in zaupanja vredni. Prav tako si oglejte lekcijo [Gradnja zaupanja vrednih AI agentov](./06-building-trustworthy-agents/README.md)._

## Sledi in razponi

Orodja za opazljivost, kot sta [Langfuse](https://langfuse.com/) ali [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo izvajanje agenta kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (npr. obravnava uporabniške zahteve).
- **Razponi** so posamezni koraki znotraj sledi (npr. klic jezikovnega modela ali pridobivanje podatkov).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Brez opazljivosti se AI agent lahko zdi kot "črna skrinjica" – njegovo notranje stanje in razmišljanje sta neprosojna, kar otežuje diagnozo težav ali optimizacijo zmogljivosti. Z opazljivostjo agenti postanejo "steklene skrinjice", ki nudijo preglednost, ki je bistvena za gradnjo zaupanja in zagotavljanje pravilnega delovanja.

## Zakaj je opazljivost pomembna v proizvodnih okoljih

Prehod AI agentov v proizvodna okolja prinaša nov nabor izzivov in zahtev. Opazljivost ni več "prijetna lastnost", ampak ključna zmogljivost:

*   **Razhroščevanje in analiza vzrokov:** Ko agent odpove ali ustvari nepričakovan izhod, orodja za opazljivost zagotovijo sledi, potrebne za določitev izvora napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcije z orodji in pogojno logiko.
*   **Upravljanje latence in stroškov:** AI agenti pogosto temeljijo na LLM-jih in drugih zunanjih API-jih, ki se zaračunavajo na osnovi števila tokenov ali klicev. Opazljivost omogoča natančno sledenje tem klicem, kar pomaga identificirati operacije, ki so prepočasi ali predrage. To ekipam omogoča optimizacijo pozivov, izbiro učinkovitejših modelov ali prenovo potekov dela za obvladovanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** V številnih aplikacijah je pomembno zagotoviti, da se agenti obnašajo varno in etično. Opazljivost ponuja revizijsko sled agentovih dejanj in odločitev. To lahko uporabimo za zaznavanje in ublažitev težav, kot so vbrizgavanje pozivov, generiranje škodljive vsebine ali nepravilno ravnanje z osebno prepoznavnimi informacijami (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent dal določen odgovor ali uporabil specifično orodje.
*   **Nenehni procesi izboljšav:** Podatki opazljivosti so temelj iterativnega razvojnega procesa. Z nadzorovanjem, kako agenti delujejo v resničnem svetu, lahko ekipe identificirajo področja za izboljšave, zbirajo podatke za finotuning modelov in potrjujejo učinke sprememb. To ustvarja povratno zanko, kjer produkcijski vpogledi iz spletnega ocenjevanja obveščajo offline eksperimentiranje in izpopolnjevanje, kar vodi do postopoma boljših zmogljivosti agentov.

## Ključni merljivi kazalniki za spremljanje

Za spremljanje in razumevanje vedenja agenta je treba spremljati različne metrike in signale. Specifične metrike se lahko razlikujejo glede na namen agenta, vendar so nekatere univerzalno pomembne.

Tukaj je nekaj najpogostejših metrik, ki jih orodja za opazljivost spremljajo:

**Latenca:** Kako hitro agent odgovori? Dolge čakalne dobe negativno vplivajo na uporabniško izkušnjo. Merite latenco za naloge in posamezne korake z zatakanjem izvedb agenta. Na primer, agent, ki za vse klice modela porabi 20 sekund, se lahko pohitri z uporabo hitrejšega modela ali z izvajanjem klicev modela vzporedno.

**Stroški:** Kakšni so stroški na zagon agenta? AI agenti temeljijo na LLM klicih, ki se zaračunavajo na token ali zunanji API klicih. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent za majhno izboljšavo kakovosti kliče LLM petkrat, je treba oceniti, ali so stroški upravičeni ali jih je mogoče zmanjšati z manjšim številom klicev ali cenejšim modelom. Spremljanje v realnem času pomaga tudi prepoznati nepričakovane skoke (npr. napake, ki povzročajo prekomerne API zanke).

**Napake zahtev:** Koliko zahtev je agent izgubil? To vključuje API napake ali neuspešne klice orodij. Da naredite vašega agenta bolj robustnega v proizvodnji, lahko nastavite rezervne poti ali ponovno poizkušanje. Npr. če ponudnik LLM A ni na voljo, preklopite na ponudnika LLM B kot rezervno možnost.

**Uporabniška povratna informacija:** Uvedba neposrednega ocenjevanja uporabnikov prinaša dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍všeč/👎ni všeč, ⭐1-5 zvezdic) ali besedilne komentarje. Konsistentno negativne povratne informacije vas morajo opozoriti, saj je to znak, da agent ne deluje po pričakovanjih.

**Implicitna uporabniška povratna informacija:** Uporabniško vedenje zagotavlja posredno povratno informacijo tudi brez eksplicitnih ocen. Vključuje takojšnje preoblikovanje vprašanja, ponavljajoče se poizvedbe ali klik na gumb za ponovno poskus. Npr. če opazite, da uporabniki večkrat zastavijo isto vprašanje, je to znak, da agent ne deluje pričakovano.

**Natančnost:** Kako pogosto agent ustvari pravilne ali zaželene izhode? Definicije natančnosti so različne (npr. pravilnost reševanja problemov, natančnost iskanja informacij, zadovoljstvo uporabnikov). Prvi korak je definirati, kaj pomeni uspeh za vašega agenta. Natančnost lahko spremljate prek avtomatskih preverjanj, ocenjevalnih rezultatov ali oznak dokončanosti nalog. Na primer, označevanje sledov kot "uspešen" ali "neuspešen".

**Avtomatizirane metrike ocenjevanja:** Prav tako lahko uvedete avtomatizirane evalvacije. Na primer, lahko uporabite LLM za oceno izhoda agenta, npr. ali je koristen, natančen ali ni. Obstaja več odprtokodnih knjižnic, ki pomagajo oceniti različne vidike agenta, npr. [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali vbrizgavanja poziva.

V praksi kombinacija teh metrik najbolj pokriva zdravje AI agenta. V [primerjalnem zvezku](./code_samples/10-expense_claim-demo.ipynb) tega poglavja vam bomo pokazali, kako te metrike izgledajo v resničnih primerih, najprej pa si bomo ogledali tipičen potek dela ocenjevanja.

## Instrumentirajte svojega agenta

Za zbiranje podatkov o sledenju boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta, da oddaja sledi in metrike, ki jih lahko ujamejo, obdelajo in vizualizirajo platforme za opazljivost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) je postal industrijski standard za opazljivost LLM. Ponuja nabor API-jev, SDK-jev in orodij za ustvarjanje, zbiranje in izvoz telemetrijskih podatkov.

Obstaja veliko knjižnic za instrumentiranje, ki zavijejo obstoječe agentne okvirje in olajšajo izvoz OpenTelemetry razponov v orodje za opazljivost. Microsoft Agent Framework se samodejno povezuje z OpenTelemetry. Spodaj je primer instrumentiranja MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Izvedba agenta se samodejno sledi
    pass
```

V [primerjalnem zvezku](./code_samples/10-expense_claim-demo.ipynb) tega poglavja je prikazano, kako instrumentirati svojega MAF agenta.

**Ročna kreacija razponov:** Čeprav knjižnice za instrumentiranje ponujajo dobro osnovo, so pogosto potrebni bolj podrobni ali prilagojeni podatki. Ročno lahko ustvarite razpone za dodajanje prilagojene aplikativne logike. Pomembneje je, da lahko avtomatsko ali ročno ustvarjene razpone obogatite s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo poslovne podatke, vmesne izračune ali katerikoli kontekst, ki je koristen za razhroščevanje ali analizo, npr. `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledov in razponov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agentov

Opazljivost nam daje metrike, a ocenjevanje je proces analize teh podatkov (in izvajanja testov) za ugotavljanje, kako dobro AI agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate sledi in metrike, kako jih uporabite za presojo agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko razvijajo (prek posodobitev ali sprememb vedenja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pameten agent" dejansko opravlja svoje delo dobro ali se je poslabšal.

Obstajata dve kategoriji ocenjevanja AI agentov: **spletno ocenjevanje** in **offline ocenjevanje**. Oba sta dragocena in se dopolnjujeta. Običajno začnemo z offline ocenjevanjem, saj je to najmanjši potreben korak pred uvajanjem kateregakoli agenta.

### Offline ocenjevanje

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Vključuje ocenjevanje agenta v kontroliranem okolju, običajno z uporabo testnih zbirk podatkov, ne z živimi uporabniškimi poizvedbami. Uporabite kurirane zbirke podatkov, kjer veste, kakšen je pričakovani izhod ali pravilno vedenje, in nato zaženete svojega agenta na teh podatkih.

Na primer, če ste zgradili agenta za matematične besedilne naloge, boste morda imeli [testno zbirko](https://huggingface.co/datasets/gsm8k) 100 problemov z znanimi rešitvami. Offline ocenjevanje se pogosto izvaja med razvojem (in je lahko del CI/CD procesov) za preverjanje izboljšav ali zaščito pred regresijami. Prednost je, da je **ponovljivo in lahko dobite jasne metrike natančnosti, saj imate resnične vrednosti (ground truth)**. Lahko tudi simulirate uporabniške poizvedbe in merite odzive agenta proti idealnim odgovorom ali uporabite avtomatske metrike, kot je opisano zgoraj.

Glavni izziv offline ocenjevanja je zagotoviti, da je vaša testna zbirka podatkov obsežna in ostaja relevantna – agent lahko dobro deluje na fiksni testni množici, a v proizvodnji naleti na zelo različne poizvedbe. Zato morate testne množice posodabljati z novimi eksotičnimi primeri in primeri, ki odražajo realne scenarije. Koristna je kombinacija majhnih "hitrih testov" in večjih evalvacijskih zbirk: majhne za hitre preverbe in večje za širše metrike učinkovitosti.

### Spletno ocenjevanje

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Nanaša se na ocenjevanje agenta v živem, resničnem okolju, tj. med dejansko uporabo v proizvodnji. Spletno ocenjevanje vključuje spremljanje zmogljivosti agenta na pravih uporabniških interakcijah in neprekinjeno analizo rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrike na živem prometu. Prednost spletnega ocenjevanja je, da **zajame stvari, ki jih v laboratorijskih pogojih ne bi predvideli** – lahko opazujete drsenje modela skozi čas (če se učinkovitost agenta slabša z morebitnimi spremembami vzorcev vhodnih podatkov) in ujame nepričakovane poizvedbe ali situacije, ki niso bile v testnih podatkih. Ponudi resnično sliko o vedenju agenta v naravi.

Spletno ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih uporabniških povratnih informacij, kot je bilo omenjeno, ter možno izvajanje senčnih testov ali A/B testov (kjer nova različica agenta teče vzporedno za primerjavo s staro). Izziv je, da je lahko pridobivanje zanesljivih oznak ali ocen za žive interakcije zahtevno – morda se zanašate na uporabniške povratne informacije ali kasnejše metrike (npr. ali je uporabnik kliknil rezultat).

### Združevanje obeh

Spletno in offline ocenjevanje nista izključujoči se; sta zelo komplementarna. Vpogledi iz spletnega spremljanja (npr. novi tipi uporabniških poizvedb, kjer agent slabo deluje) se lahko uporabijo za dopolnitev in izboljšanje offline testnih zbirk. Nasprotno, agenti, ki dobro delujejo v offline testih, so lahko nato z večjim zaupanjem uvedeni in spremljani online.

Dejansko mnoge ekipe uporabljajo zanko:

_ocenjuj offline -> uvajaj -> spremljaj online -> zbiri nove primere napak -> dodaj v offline bazo -> izpopolni agenta -> ponovi_.

## Pogoste težave

Ob uvajanju AI agentov v produkcijo se lahko soočite z različnimi izzivi. Tukaj je nekaj pogostih težav in njihove morebitne rešitve:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent ne izvaja nalog konsistentno | - Izboljšajte poziv, ki ga dajete AI agentu; bodite jasni glede ciljev.<br>- Prepoznajte, kje lahko razdelitev nalog na podnaloge in obravnava z več agenti pomaga. |
| AI agent se znajde v neskončnih zankah | - Poskrbite, da imate jasne pogoje zaustavitve, da agent ve, kdaj ustaviti postopek.<br>- Pri zapletenih nalogah, ki zahtevajo razmišljanje in načrtovanje, uporabite večji model, specializiran za razumske naloge. |
| AI agentovi klici orodij ne delujejo dobro | - Testirajte in validirajte izhod orodja zunaj sistema agenta.<br>- Izboljšajte definirane parametre, pozive in poimenovanje orodij.  |
| Sistem z več agenti ne deluje konsistentno | - Izboljšajte pozive, dane vsakemu agentu, da bodo specifični in različni.<br>- Zgradite hierarhični sistem z "usmerjevalnim" ali krmilnim agentom, ki določi, kateri agent je pravi. |

Veliko teh težav je mogoče bolj učinkovito odkriti z vzpostavljeno opazljivostjo. Sledi in metrike, o katerih smo prej govorili, pomagajo natančno določiti, kje v poteku dela agenta se pojavljajo težave, kar naredi razhroščevanje in optimizacijo bistveno učinkovitejše.

## Upravljanje stroškov
Tukaj je nekaj strategij za upravljanje stroškov uvajanja AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) se lahko dobro obnesejo pri določenih primerih uporabe agentov in bodo znatno znižali stroške. Kot je omenjeno zgoraj, je izdelava ocenjevalnega sistema za določanje in primerjavo uspešnosti v primerjavi z večjimi modeli najboljši način, da razumete, kako dobro se bo SLM izkazal za vaš primer uporabe. Razmislite o uporabi SLM za enostavnejše naloge, kot so klasifikacija namena ali izvleček parametrov, medtem ko rezervirate večje modele za zapleteno sklepanje.

**Uporaba modela za usmerjanje:** Podobna strategija je uporaba različnih modelov in velikosti. Lahko uporabite LLM/SLM ali brezstrežniško funkcijo za usmerjanje zahtev na podlagi zapletenosti do modelov, ki najbolj ustrezajo. To bo prav tako pomagalo znižati stroške, hkrati pa zagotavljalo uspešnost pri pravih nalogah. Na primer, preusmerite enostavna vprašanja k manjšim, hitrejšim modelom in uporabljajte drage velike modele le za zahtevne naloge sklepanja.

**Predpomnjenje odgovorov:** Prepoznavanje pogostih zahtevkov in nalog ter zagotavljanje odgovorov pred njihovim prehodom skozi vaš agentski sistem je dober način za zmanjšanje količine podobnih zahtev. Lahko celo izvedete tok, ki določa, kako podoben je zahtevek tistim, shranjenim v predpomnilnik, z uporabo bolj osnovnih AI modelov. Ta strategija lahko znatno zmanjša stroške za pogosto zastavljena vprašanja ali pogoste delovne postopke.

## Poglejmo, kako to deluje v praksi

V [primerku zvezka tega poglavja](./code_samples/10-expense_claim-demo.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazovanje in ocenjevanje našega agenta.


### Imate še več vprašanj o AI agentih v produkciji?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učeče, se udeležite uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.

## Prejšnja lekcija

[Metakognitivni oblikovni vzorec](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->