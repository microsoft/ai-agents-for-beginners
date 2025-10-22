<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-08-29T23:14:07+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sl"
}
-->
# AI agenti v produkciji: opazovanje in ocenjevanje

[![AI agenti v produkciji](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.sl.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ko AI agenti prehajajo iz eksperimentalnih prototipov v resnične aplikacije, postane ključnega pomena razumevanje njihovega vedenja, spremljanje njihovega delovanja in sistematično ocenjevanje njihovih rezultatov.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:
- Osnovne koncepte opazovanja in ocenjevanja agentov
- Tehnike za izboljšanje zmogljivosti, stroškov in učinkovitosti agentov
- Kaj in kako sistematično oceniti svoje AI agente
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente, zgrajene z AutoGen

Cilj je, da pridobite znanje za preoblikovanje svojih "črnih škatel" agentov v pregledne, obvladljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in vredni zaupanja. Oglejte si lekcijo [Gradnja zaupanja vrednih AI agentov](./06-building-trustworthy-agents/README.md)._

## Sledi in razponi

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo izvajanje agentov kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (na primer obravnavanje uporabniškega vprašanja).
- **Razponi** so posamezni koraki znotraj sledi (na primer klic jezikovnega modela ali pridobivanje podatkov).

![Drevo sledi v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Brez opazovanja se AI agent lahko zdi kot "črna škatla" – njegovo notranje stanje in razmišljanje sta nejasna, kar otežuje diagnosticiranje težav ali optimizacijo delovanja. Z opazovanjem pa agenti postanejo "steklene škatle", kar omogoča preglednost, ki je ključna za gradnjo zaupanja in zagotavljanje, da delujejo po pričakovanjih.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nove izzive in zahteve. Opazovanje ni več "lepa lastnost", ampak ključna sposobnost:

*   **Odpravljanje napak in analiza vzrokov**: Ko agent odpove ali ustvari nepričakovan rezultat, orodja za opazovanje zagotovijo sledi, potrebne za določitev izvora napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcije z orodji in pogojno logiko.
*   **Upravljanje zakasnitve in stroškov**: AI agenti se pogosto zanašajo na LLM-je in druge zunanje API-je, ki se zaračunavajo na klic ali na število tokenov. Opazovanje omogoča natančno spremljanje teh klicev, kar pomaga prepoznati operacije, ki so prepočasne ali predrage. To ekipam omogoča optimizacijo pozivov, izbiro bolj učinkovitih modelov ali preoblikovanje delovnih tokov za upravljanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost**: V mnogih aplikacijah je pomembno zagotoviti, da se agenti obnašajo varno in etično. Opazovanje zagotavlja revizijsko sled dejanj in odločitev agenta. To se lahko uporabi za odkrivanje in odpravljanje težav, kot so vbrizgavanje pozivov, generiranje škodljive vsebine ali nepravilno ravnanje z osebnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent podal določen odgovor ali uporabil določeno orodje.
*   **Neprekinjeni izboljševalni cikli**: Podatki o opazovanju so temelj iterativnega razvojnega procesa. Z opazovanjem, kako agenti delujejo v resničnem svetu, lahko ekipe prepoznajo področja za izboljšave, zberejo podatke za fino nastavitev modelov in preverijo učinek sprememb. To ustvari povratno zanko, kjer vpogledi iz produkcijskega okolja informirajo eksperimentiranje in izboljšave, kar vodi do postopno boljšega delovanja agentov.

## Ključne metrike za spremljanje

Za spremljanje in razumevanje vedenja agenta je treba spremljati vrsto metrik in signalov. Čeprav se specifične metrike lahko razlikujejo glede na namen agenta, so nekatere univerzalno pomembne.

Tukaj je nekaj najpogostejših metrik, ki jih orodja za opazovanje spremljajo:

**Zakasnitev:** Kako hitro agent odgovori? Dolgi čakalni časi negativno vplivajo na uporabniško izkušnjo. Meriti morate zakasnitev za naloge in posamezne korake s sledenjem izvajanja agenta. Na primer, agent, ki za vse klice modela potrebuje 20 sekund, bi lahko pospešili z uporabo hitrejšega modela ali vzporednim izvajanjem klicev modela.

**Stroški:** Kakšni so stroški na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na token ali na zunanje API-je. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent petkrat pokliče LLM za marginalno izboljšanje kakovosti, morate oceniti, ali so stroški upravičeni ali pa zmanjšati število klicev ali uporabiti cenejši model. Spremljanje v realnem času lahko pomaga prepoznati nepričakovane konice (npr. napake, ki povzročajo prekomerne zanke API).

**Napake pri zahtevah:** Koliko zahtev je agentu spodletelo? To lahko vključuje napake API ali neuspele klice orodij. Da bi vaš agent postal bolj robusten v produkciji, lahko nastavite rezervne možnosti ali ponovne poskuse. Na primer, če je ponudnik LLM A nedosegljiv, preklopite na ponudnika LLM B kot rezervno možnost.

**Povratne informacije uporabnikov:** Neposredne ocene uporabnikov zagotavljajo dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍thumbs-up/👎down, ⭐1-5 zvezdic) ali besedilne komentarje. Dosledne negativne povratne informacije bi vas morale opozoriti, saj to pomeni, da agent ne deluje po pričakovanjih.

**Implicitne povratne informacije uporabnikov:** Vedenje uporabnikov zagotavlja posredne povratne informacije, tudi brez eksplicitnih ocen. To lahko vključuje takojšnje preoblikovanje vprašanja, ponavljajoče se poizvedbe ali klik na gumb za ponovni poskus. Na primer, če opazite, da uporabniki večkrat postavljajo isto vprašanje, je to znak, da agent ne deluje po pričakovanjih.

**Točnost:** Kako pogosto agent ustvari pravilne ali zaželene rezultate? Definicije točnosti se razlikujejo (npr. pravilnost reševanja problemov, točnost pridobivanja informacij, zadovoljstvo uporabnikov). Prvi korak je opredeliti, kaj pomeni uspeh za vašega agenta. Točnost lahko spremljate prek avtomatiziranih preverjanj, ocenjevalnih točk ali oznak dokončanja nalog. Na primer, označevanje sledi kot "uspešno" ali "neuspešno".

**Avtomatizirane ocenjevalne metrike:** Lahko nastavite tudi avtomatizirane ocene. Na primer, lahko uporabite LLM za ocenjevanje izhoda agenta, npr. ali je koristen, točen ali ne. Obstajajo tudi številne odprtokodne knjižnice, ki pomagajo oceniti različne vidike agenta. Na primer, [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali vbrizgavanja pozivov.

V praksi kombinacija teh metrik zagotavlja najboljši pregled nad zdravjem AI agenta. V [primeru zvezka](./code_samples/10_autogen_evaluation.ipynb) v tem poglavju vam bomo pokazali, kako te metrike izgledajo v resničnih primerih, vendar se najprej naučimo, kako izgleda tipičen potek ocenjevanja.

## Instrumentiranje vašega agenta

Za zbiranje podatkov o sledenju boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta, da oddaja sledi in metrike, ki jih lahko opazovalna platforma zajame, obdela in vizualizira.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se je uveljavil kot industrijski standard za opazovanje LLM. Ponuja nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetrijskih podatkov.

Obstajajo številne knjižnice za instrumentiranje, ki ovijejo obstoječe okvirje agentov in omogočajo enostaven izvoz razponov OpenTelemetry v orodje za opazovanje. Spodaj je primer instrumentiranja agenta AutoGen z [OpenLit knjižnico za instrumentiranje](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Primer zvezka](./code_samples/10_autogen_evaluation.ipynb) v tem poglavju bo pokazal, kako instrumentirati vašega agenta AutoGen.

**Ročno ustvarjanje razponov:** Čeprav knjižnice za instrumentiranje zagotavljajo dobro osnovo, pogosto obstajajo primeri, ko so potrebne podrobnejše ali prilagojene informacije. Razpone lahko ročno ustvarite za dodajanje prilagojene logike aplikacije. Še pomembneje, lahko obogatite samodejno ali ročno ustvarjene razpone s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo poslovno specifične podatke, vmesne izračune ali katero koli kontekstualno informacijo, ki bi lahko bila koristna za odpravljanje napak ali analizo, kot so `user_id`, `session_id` ali `model_version`.

Primer ročnega ustvarjanja sledi in razponov z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocenjevanje agenta

Opazovanje nam daje metrike, vendar je ocenjevanje proces analiziranja teh podatkov (in izvajanja testov), da ugotovimo, kako dobro AI agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate te sledi in metrike, kako jih uporabiti za oceno agenta in sprejemanje odločitev?

Redno ocenjevanje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko razvijajo (prek posodobitev ali spreminjajočega vedenja modela) – brez ocenjevanja ne bi vedeli, ali vaš "pametni agent" dejansko dobro opravlja svoje delo ali pa je nazadoval.

Obstajata dve kategoriji ocenjevanja AI agentov: **spletno ocenjevanje** in **nespletno ocenjevanje**. Obe sta dragoceni in se medsebojno dopolnjujeta. Običajno začnemo z nespletnim ocenjevanjem, saj je to minimalni potrebni korak pred uvajanjem agenta.

### Nespletno ocenjevanje

![Elementi podatkovne zbirke v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje ocenjevanje agenta v nadzorovanem okolju, običajno z uporabo testnih podatkovnih zbirk, ne pa živih uporabniških poizvedb. Uporabljate kurirane podatkovne zbirke, kjer veste, kakšen je pričakovani rezultat ali pravilno vedenje, in nato preizkusite agenta na teh podatkih.

Na primer, če ste zgradili agenta za matematične besedilne probleme, bi lahko imeli [testno podatkovno zbirko](https://huggingface.co/datasets/gsm8k) s 100 problemi z znanimi odgovori. Nespletno ocenjevanje se pogosto izvaja med razvojem (in je lahko del CI/CD procesov), da preverite izboljšave ali preprečite nazadovanja. Prednost je, da je **ponovljivo in lahko dobite jasne metrike točnosti, saj imate resnico**. Lahko tudi simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane metrike, kot je opisano zgoraj.

Ključni izziv pri nespletnem ocenjevanju je zagotoviti, da je vaša testna podatkovna zbirka celovita in ostaja relevantna – agent lahko dobro deluje na fiksnem testnem naboru, vendar naleti na zelo različne poizvedbe v produkciji. Zato morate testne nabore posodabljati z novimi mejami in primeri, ki odražajo resnične scenarije​. Mešanica majhnih "dimnih testov" in večjih ocenjevalnih naborov je koristna: majhni nabori za hitre preveritve in večji za širše metrike delovanja​.

### Spletno ocenjevanje

![Pregled metrik opazovanja](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se nanaša na ocenjevanje agenta v živem, resničnem okolju, tj. med dejansko uporabo v produkciji. Spletno ocenjevanje vključuje spremljanje delovanja agenta na resničnih interakcijah uporabnikov in neprekinjeno analiziranje rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrike na živem prometu. Prednost spletnega ocenjevanja je, da **zajame stvari, ki jih morda ne bi predvideli v laboratorijskem okolju** – lahko opazujete odmik modela skozi čas (če se učinkovitost agenta poslabša, ko se vzorci vhodnih podatkov spremenijo) in zaznate nepričakovane poizvedbe ali situacije, ki niso bile v vaših testnih podatkih​. Ponuja resnično sliko, kako se agent obnaša v naravi.

Spletno ocenjevanje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo že omenjeno, in morda izvajanje senčnih testov ali A/B testov (kjer nova različica agenta deluje vzporedno za primerjavo s staro). Izziv je, da je lahko težko pridobiti zanesljive oznake ali ocene za žive interakcije – morda se zanašate na povratne informacije uporabnikov ali metrike navzdol (na primer, ali je uporabnik kliknil rezultat).

### Kombinacija obeh

Spletno in nespletno ocenjevanje se ne izključujeta; močno se dopolnjujeta. Vpogledi iz spletnega spremljanja (npr. nove vrste uporabniških poizvedb, kjer agent slabo deluje) se lahko uporabijo za dopolnitev in izboljšanje nespletnih testnih podatkovnih zbirk. Nasprotno pa se agenti, ki dobro delujejo v nespletnih testih, lahko bolj samozavestno uvedejo in spremljajo spletno.

Pravzaprav mnoge ekipe sprejmejo zanko:

_oceni nespletno -> uvedi -> spremljaj spletno -> zberi nove primere neuspehov -> dodaj v nespletni nabor podatkov -> izboljšaj agenta -> ponovi_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj je nekaj pogostih težav in njihovih možnih rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent ne izvaja nalog dosledno | - Izboljšajte poziv, ki ga dajete AI agentu; bodite jasni glede ciljev.<br>- Ugotovite, kje bi razdelitev nalog na podnaloge in njihovo obravnavanje s strani več agentov lahko pomagala. |
| AI agent zaide v neprekinjene zanke  | - Poskrbite, da imate jasne pogoje za zaključek, da agent ve, kdaj ustaviti proces. |

## Uvod

Ko se AI agenti premaknejo iz faze razvoja v produkcijo, se pogosto pojavijo izzivi. Tukaj je nekaj pogostih težav, ki jih lahko srečate, skupaj s predlogi za njihovo reševanje.

## Pogoste težave in rešitve

| **Težava**                                   | **Rešitev**                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------|
| Agent ne daje pričakovanih rezultatov       | - Preverite, ali so podatki za usposabljanje ustrezni za vaš primer uporabe.<br>- Preverite, ali so parametri in pozivi pravilno nastavljeni. |
| Agent ne razume kompleksnih nalog           | - Uporabite večji model, ki je specializiran za naloge, ki zahtevajo kompleksno razmišljanje. |
| Orodja AI agenta ne delujejo dobro          | - Testirajte in preverite rezultate orodij zunaj sistema agenta.<br>- Izboljšajte definirane parametre, pozive in poimenovanje orodij. |
| Sistem z več agenti ne deluje dosledno      | - Izboljšajte pozive, ki jih prejme vsak agent, da zagotovite, da so specifični in se med seboj razlikujejo.<br>- Zgradite hierarhični sistem z "usmerjevalnim" ali kontrolnim agentom, ki določi, kateri agent je pravi za nalogo. |

Veliko teh težav je mogoče učinkoviteje prepoznati z ustrezno opazljivostjo. Sledi in metrike, o katerih smo govorili prej, pomagajo natančno določiti, kje v delovnem toku agenta se pojavijo težave, kar omogoča hitrejše odpravljanje napak in optimizacijo.

## Upravljanje stroškov

Tukaj je nekaj strategij za upravljanje stroškov pri uvajanju AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) lahko dobro delujejo pri določenih primerih uporabe agentov in znatno zmanjšajo stroške. Kot smo že omenili, je najboljši način za razumevanje, kako dobro bo SLM deloval za vaš primer uporabe, vzpostavitev sistema za ocenjevanje, ki primerja zmogljivost manjših modelov z večjimi. Razmislite o uporabi SLM za enostavnejše naloge, kot so klasifikacija namena ali ekstrakcija parametrov, medtem ko večje modele rezervirate za kompleksno razmišljanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba raznolikosti modelov in velikosti. Uporabite LLM/SLM ali strežniško funkcijo za usmerjanje zahtev glede na kompleksnost k najbolj ustreznim modelom. To bo pomagalo zmanjšati stroške, hkrati pa zagotovilo zmogljivost za prave naloge. Na primer, preusmerite enostavna vprašanja k manjšim, hitrejšim modelom, medtem ko za kompleksne naloge uporabite dražje velike modele.

**Predpomnjenje odgovorov:** Prepoznavanje pogostih zahtev in nalog ter zagotavljanje odgovorov, preden gredo skozi vaš sistem agentov, je dober način za zmanjšanje obsega podobnih zahtev. Lahko celo implementirate proces za ugotavljanje, kako podobna je zahteva vašim predpomnjenim zahtevam, z uporabo bolj osnovnih AI modelov. Ta strategija lahko znatno zmanjša stroške za pogosto zastavljena vprašanja ali običajne delovne tokove.

## Poglejmo, kako to deluje v praksi

V [primerjalni beležki tega razdelka](./code_samples/10_autogen_evaluation.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazljivost za spremljanje in ocenjevanje našega agenta.

### Imate več vprašanj o AI agentih v produkciji?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kjer se lahko povežete z drugimi učenci, udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Prejšnja lekcija

[Metakognitivni vzorec oblikovanja](../09-metacognition/README.md)

## Naslednja lekcija

[Agentni protokoli](../11-agentic-protocols/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.