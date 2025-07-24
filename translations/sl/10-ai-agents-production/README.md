<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T09:11:33+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sl"
}
-->
# AI agenti v produkciji: Opazovanje in vrednotenje

Ko AI agenti prehajajo iz eksperimentalnih prototipov v resnične aplikacije, postaja sposobnost razumevanja njihovega vedenja, spremljanja njihovega delovanja in sistematičnega vrednotenja njihovih rezultatov ključnega pomena.

## Cilji učenja

Po zaključku te lekcije boste znali/razumeli:
- Osnovne koncepte opazovanja in vrednotenja agentov
- Tehnike za izboljšanje delovanja, stroškov in učinkovitosti agentov
- Kaj in kako sistematično vrednotiti pri AI agentih
- Kako nadzorovati stroške pri uvajanju AI agentov v produkcijo
- Kako instrumentirati agente, zgrajene z AutoGen

Cilj je, da pridobite znanje za preoblikovanje svojih "črnih škatel" v pregledne, obvladljive in zanesljive sisteme.

_**Opomba:** Pomembno je uvajati AI agente, ki so varni in vredni zaupanja. Oglejte si lekcijo [Gradnja zaupanja vrednih AI agentov](./06-building-trustworthy-agents/README.md)._

## Sledi in razponi

Orodja za opazovanje, kot sta [Langfuse](https://langfuse.com/) ali [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), običajno predstavljajo izvajanje agentov kot sledi in razpone.

- **Sled** predstavlja celotno nalogo agenta od začetka do konca (npr. obravnava uporabniškega vprašanja).
- **Razponi** so posamezni koraki znotraj sledi (npr. klic jezikovnega modela ali pridobivanje podatkov).

![Drevo sledi v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Brez opazovanja se AI agent lahko zdi kot "črna škatla" – njegovo notranje stanje in razmišljanje sta nejasna, kar otežuje diagnosticiranje težav ali optimizacijo delovanja. Z opazovanjem pa agenti postanejo "steklene škatle", kar omogoča preglednost, ki je ključna za gradnjo zaupanja in zagotavljanje, da delujejo po pričakovanjih.

## Zakaj je opazovanje pomembno v produkcijskih okoljih

Prehod AI agentov v produkcijska okolja prinaša nove izzive in zahteve. Opazovanje ni več "lepa lastnost", temveč ključna sposobnost:

*   **Odpravljanje napak in analiza vzrokov:** Ko agent odpove ali ustvari nepričakovani rezultat, orodja za opazovanje zagotovijo sledi, potrebne za določitev vira napake. To je še posebej pomembno pri kompleksnih agentih, ki lahko vključujejo več klicev LLM, interakcij z orodji in pogojno logiko.
*   **Upravljanje zakasnitev in stroškov:** AI agenti se pogosto zanašajo na LLM-je in druge zunanje API-je, ki se zaračunavajo na žeton ali klic. Opazovanje omogoča natančno sledenje tem klicem, kar pomaga prepoznati operacije, ki so prepočasne ali predrage. To omogoča ekipam optimizacijo pozivov, izbiro učinkovitejših modelov ali preoblikovanje delovnih tokov za upravljanje operativnih stroškov in zagotavljanje dobre uporabniške izkušnje.
*   **Zaupanje, varnost in skladnost:** V mnogih aplikacijah je pomembno zagotoviti, da agenti delujejo varno in etično. Opazovanje zagotavlja revizijsko sled dejanj in odločitev agenta. To se lahko uporabi za zaznavanje in odpravljanje težav, kot so vbrizgavanje pozivov, generiranje škodljive vsebine ali nepravilno ravnanje z osebnimi podatki (PII). Na primer, lahko pregledate sledi, da razumete, zakaj je agent podal določen odgovor ali uporabil določeno orodje.
*   **Neprekinjene izboljšave:** Podatki o opazovanju so temelj iterativnega razvojnega procesa. Z opazovanjem, kako agenti delujejo v resničnem svetu, lahko ekipe prepoznajo področja za izboljšave, zberejo podatke za fino nastavitev modelov in preverijo vpliv sprememb. To ustvarja povratno zanko, kjer vpogledi iz produkcijskega okolja informirajo eksperimentiranje in izboljšave, kar vodi do postopno boljšega delovanja agentov.

## Ključne metrike za spremljanje

Za spremljanje in razumevanje vedenja agenta je treba slediti različnim metrikam in signalom. Čeprav se specifične metrike lahko razlikujejo glede na namen agenta, so nekatere univerzalno pomembne.

Tukaj je nekaj najpogostejših metrik, ki jih spremljajo orodja za opazovanje:

**Zakasnitev:** Kako hitro agent odgovori? Dolgi časi čakanja negativno vplivajo na uporabniško izkušnjo. Meriti bi morali zakasnitev za naloge in posamezne korake s sledenjem izvajanja agenta. Na primer, agenta, ki za vse klice modela potrebuje 20 sekund, bi lahko pospešili z uporabo hitrejšega modela ali vzporednim izvajanjem klicev modela.

**Stroški:** Kakšni so stroški na izvajanje agenta? AI agenti se zanašajo na klice LLM, ki se zaračunavajo na žeton, ali zunanje API-je. Pogosta uporaba orodij ali več pozivov lahko hitro poveča stroške. Na primer, če agent petkrat pokliče LLM za minimalno izboljšanje kakovosti, morate oceniti, ali so stroški upravičeni, ali pa zmanjšati število klicev ali uporabiti cenejši model. Spremljanje v realnem času lahko pomaga tudi pri prepoznavanju nepričakovanih konic (npr. napake, ki povzročajo prekomerne zanke API).

**Napake pri zahtevah:** Koliko zahtev je agentu spodletelo? To lahko vključuje napake API ali neuspešne klice orodij. Da bi bil vaš agent bolj robusten v produkciji, lahko nastavite nadomestne rešitve ali ponovne poskuse. Na primer, če je ponudnik LLM A nedosegljiv, preklopite na ponudnika LLM B kot rezervno možnost.

**Povratne informacije uporabnikov:** Neposredne ocene uporabnikov zagotavljajo dragocene vpoglede. To lahko vključuje eksplicitne ocene (👍/👎, ⭐1-5 zvezdic) ali besedilne komentarje. Dosledno negativne povratne informacije vas morajo opozoriti, saj to pomeni, da agent ne deluje po pričakovanjih.

**Implicitne povratne informacije uporabnikov:** Vedenje uporabnikov zagotavlja posredne povratne informacije, tudi brez eksplicitnih ocen. To lahko vključuje takojšnje preoblikovanje vprašanj, ponavljajoče se poizvedbe ali klikanje gumba za ponovni poskus. Na primer, če opazite, da uporabniki večkrat postavljajo isto vprašanje, je to znak, da agent ne deluje po pričakovanjih.

**Natančnost:** Kako pogosto agent ustvari pravilne ali zaželene rezultate? Definicije natančnosti se razlikujejo (npr. pravilnost reševanja problemov, natančnost pridobivanja informacij, zadovoljstvo uporabnikov). Prvi korak je določiti, kaj pomeni uspeh za vašega agenta. Natančnost lahko spremljate z avtomatiziranimi preverjanji, ocenjevalnimi točkami ali oznakami dokončanja nalog. Na primer, označevanje sledi kot "uspešno" ali "neuspešno".

**Avtomatizirane ocenjevalne metrike:** Lahko nastavite tudi avtomatizirane ocene. Na primer, uporabite LLM za ocenjevanje izhodov agenta glede na to, ali so koristni, natančni ali ne. Obstajajo tudi številne odprtokodne knjižnice, ki pomagajo oceniti različne vidike agenta. Na primer, [RAGAS](https://docs.ragas.io/) za RAG agente ali [LLM Guard](https://llm-guard.com/) za zaznavanje škodljivega jezika ali vbrizgavanja pozivov.

V praksi kombinacija teh metrik zagotavlja najboljši vpogled v zdravje AI agenta. V [primeru zvezka](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) v tem poglavju bomo prikazali, kako te metrike izgledajo v resničnih primerih, vendar se bomo najprej naučili, kako izgleda tipičen potek vrednotenja.

## Instrumentiranje vašega agenta

Za zbiranje podatkov o sledenju boste morali instrumentirati svojo kodo. Cilj je instrumentirati kodo agenta tako, da oddaja sledi in metrike, ki jih lahko platforma za opazovanje zajame, obdela in vizualizira.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se je uveljavil kot industrijski standard za opazovanje LLM. Ponuja nabor API-jev, SDK-jev in orodij za generiranje, zbiranje in izvoz telemetrijskih podatkov.

Obstajajo številne knjižnice za instrumentiranje, ki ovijejo obstoječe ogrodja agentov in omogočajo enostaven izvoz razponov OpenTelemetry v orodje za opazovanje. Spodaj je primer instrumentiranja agenta AutoGen z uporabo knjižnice [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Primer zvezka](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) v tem poglavju bo prikazal, kako instrumentirati vašega agenta AutoGen.

**Ročno ustvarjanje razponov:** Čeprav knjižnice za instrumentiranje zagotavljajo dobro osnovo, obstajajo primeri, ko so potrebne podrobnejše ali prilagojene informacije. Razpone lahko ustvarite ročno, da dodate prilagojeno logiko aplikacije. Še pomembneje je, da lahko obogatite samodejno ali ročno ustvarjene razpone s prilagojenimi atributi (znanimi tudi kot oznake ali metapodatki). Ti atributi lahko vključujejo poslovno specifične podatke, vmesne izračune ali kateri koli kontekst, ki bi bil uporaben za odpravljanje napak ali analizo, kot so `user_id`, `session_id` ali `model_version`.

Primer ustvarjanja sledi in razponov ročno z uporabo [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Vrednotenje agenta

Opazovanje nam daje metrike, vendar je vrednotenje proces analiziranja teh podatkov (in izvajanja testov), da ugotovimo, kako dobro AI agent deluje in kako ga lahko izboljšamo. Z drugimi besedami, ko imate sledi in metrike, kako jih uporabiti za oceno agenta in sprejemanje odločitev?

Redno vrednotenje je pomembno, ker so AI agenti pogosto nedeterministični in se lahko razvijajo (prek posodobitev ali spreminjajočega vedenja modela) – brez vrednotenja ne bi vedeli, ali vaš "pametni agent" dejansko dobro opravlja svoje delo ali je nazadoval.

Obstajata dve kategoriji vrednotenj za AI agente: **offline vrednotenje** in **online vrednotenje**. Obe sta dragoceni in se dopolnjujeta. Običajno začnemo z offline vrednotenjem, saj je to minimalni potrebni korak pred uvajanjem agenta.

### Offline vrednotenje

![Elementi podatkovne zbirke v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To vključuje vrednotenje agenta v nadzorovanem okolju, običajno z uporabo testnih podatkovnih zbirk, ne pa živih uporabniških poizvedb. Uporabite kurirane podatkovne zbirke, kjer poznate pričakovani izhod ali pravilno vedenje, in nato zaženete agenta na teh podatkih.

Na primer, če ste ustvarili agenta za matematične besedilne naloge, bi lahko imeli [testno podatkovno zbirko](https://huggingface.co/datasets/gsm8k) s 100 nalogami z znanimi odgovori. Offline vrednotenje se pogosto izvaja med razvojem (in je lahko del CI/CD procesov), da preverite izboljšave ali preprečite nazadovanja. Prednost je, da je **ponovljivo in lahko dobite jasne metrike natančnosti, saj imate resnico na voljo**. Lahko tudi simulirate uporabniške poizvedbe in merite odzive agenta glede na idealne odgovore ali uporabite avtomatizirane metrike, kot je opisano zgoraj.

Ključni izziv pri offline vrednotenju je zagotoviti, da je vaša testna podatkovna zbirka celovita in ostaja relevantna – agent se lahko dobro obnese na fiksnem testnem naboru, vendar naleti na zelo različne poizvedbe v produkciji. Zato bi morali testne nabore posodabljati z novimi mejami in primeri, ki odražajo resnične scenarije. Uporabna je kombinacija majhnih "dimnih testov" in večjih evalvacijskih naborov: majhni nabori za hitre preglede in večji za širše metrike delovanja.

### Online vrednotenje

![Pregled metrik opazovanja](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se nanaša na vrednotenje agenta v živem, resničnem okolju, tj. med dejansko uporabo v produkciji. Online vrednotenje vključuje spremljanje delovanja agenta na resničnih interakcijah z uporabniki in neprekinjeno analizo rezultatov.

Na primer, lahko spremljate stopnje uspešnosti, ocene zadovoljstva uporabnikov ali druge metrike na živem prometu. Prednost online vrednotenja je, da **zajame stvari, ki jih v laboratorijskem okolju morda ne bi predvideli** – lahko opazujete odmik modela skozi čas (če se učinkovitost agenta poslabša, ko se vzorci vhodov spremenijo) in zaznate nepričakovane poizvedbe ali situacije, ki niso bile v vaših testnih podatkih. Zagotavlja resnično sliko, kako se agent obnaša v praksi.

Online vrednotenje pogosto vključuje zbiranje implicitnih in eksplicitnih povratnih informacij uporabnikov, kot je bilo omenjeno, in morda izvajanje senčnih testov ali A/B testov (kjer nova različica agenta deluje vzporedno za primerjavo s staro). Izziv je, da je lahko težko pridobiti zanesljive oznake ali ocene za žive interakcije – morda se zanašate na povratne informacije uporabnikov ali metrike navzdol (npr. ali je uporabnik kliknil rezultat).

### Kombinacija obeh

Online in offline vrednotenja se ne izključujeta; sta zelo komplementarna. Vpogledi iz online spremljanja (npr. nove vrste uporabniških poizvedb, kjer agent deluje slabo) se lahko uporabijo za dopolnitev in izboljšanje offline testnih podatkovnih zbirk. Nasprotno pa se agenti, ki se dobro obnesejo v offline testih, lahko bolj samozavestno uvedejo in spremljajo online.

Dejansko mnoge ekipe sprejmejo zanko:

_vrednotenje offline -> uvedba -> spremljanje online -> zbiranje novih primerov napak -> dodajanje v offline podatkovno zbirko -> izboljšanje agenta -> ponovitev_.

## Pogoste težave

Ko uvajate AI agente v produkcijo, se lahko srečate z različnimi izzivi. Tukaj je nekaj pogostih težav in njihovih možnih rešitev:

| **Težava**    | **Možna rešitev**   |
| ------------- | ------------------ |
| AI agent ne izvaja nalog dosledno | - Izboljšajte poziv, ki ga dajete AI agentu; bodite jasni glede ciljev.<br>- Prepoznajte, kje lahko razdelitev nalog na podnaloge in njihovo obravnavanje z več agenti pomaga. |
| AI agent se ujame v neskončne zanke  | - Poskrbite, da imate jasne pogoje za prekinitev, da agent ve, kdaj ustaviti proces.<br>- Za kompleksne naloge, ki zahtevajo razmišljanje in načrtovanje, uporabite večji model, specializiran za naloge razmišljanja. |
| Klici orodij AI agenta ne delujejo dobro   | - Preizkusite in preverite izhod orodja zunaj sistema agenta. |

- Izboljšajte določene parametre, pozive in poimenovanje orodij.  |
| Večagentni sistem ne deluje dosledno | - Izboljšajte pozive, ki jih prejme vsak agent, da bodo specifični in jasno ločeni drug od drugega.<br>- Zgradite hierarhični sistem z uporabo "usmerjevalnega" ali kontrolnega agenta, ki določi, kateri agent je pravi za določeno nalogo. |

Veliko teh težav je mogoče učinkoviteje prepoznati, če je vzpostavljena opazljivost. Sledi in meritve, o katerih smo govorili prej, pomagajo natančno določiti, kje v poteku dela agenta se pojavijo težave, kar omogoča veliko bolj učinkovito odpravljanje napak in optimizacijo.

## Upravljanje stroškov

Tukaj je nekaj strategij za upravljanje stroškov pri uvajanju AI agentov v produkcijo:

**Uporaba manjših modelov:** Majhni jezikovni modeli (SLM) se lahko dobro obnesejo pri določenih agentnih primerih uporabe in znatno zmanjšajo stroške. Kot smo že omenili, je najboljši način za razumevanje, kako dobro bo SLM deloval za vaš primer uporabe, vzpostavitev evalvacijskega sistema za določanje in primerjavo zmogljivosti v primerjavi z večjimi modeli. Razmislite o uporabi SLM za enostavnejše naloge, kot so razvrščanje namenov ali pridobivanje parametrov, večje modele pa rezervirajte za kompleksno sklepanje.

**Uporaba usmerjevalnega modela:** Podobna strategija je uporaba raznolikih modelov različnih velikosti. LLM/SLM ali strežniško funkcijo lahko uporabite za usmerjanje zahtev glede na njihovo kompleksnost k najbolj ustreznim modelom. To bo pomagalo zmanjšati stroške in hkrati zagotoviti ustrezno zmogljivost za določene naloge. Na primer, preprosta vprašanja usmerite k manjšim, hitrejšim modelom, drage velike modele pa uporabite le za naloge, ki zahtevajo kompleksno sklepanje.

**Predpomnjenje odgovorov:** Prepoznavanje pogostih zahtev in nalog ter zagotavljanje odgovorov, preden gredo skozi vaš agentni sistem, je dober način za zmanjšanje obsega podobnih zahtev. Lahko celo uvedete postopek za določanje, kako podobna je zahteva že predpomnjenim zahtevam, z uporabo bolj osnovnih AI modelov. Ta strategija lahko znatno zmanjša stroške za pogosto zastavljena vprašanja ali običajne poteke dela.

## Poglejmo, kako to deluje v praksi

V [primerjalni beležnici tega poglavja](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) bomo videli primere, kako lahko uporabimo orodja za opazljivost za spremljanje in evalvacijo našega agenta.

## Prejšnja lekcija

[Metakognitivni vzorec oblikovanja](../09-metacognition/README.md)

## Naslednja lekcija

[MCP](../11-mcp/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.