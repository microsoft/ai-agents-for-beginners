[![Agentic RAG](../../../translated_images/hr/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Agentic RAG

Ova lekcija pruža sveobuhvatan pregled Agentic Retrieval-Augmented Generation (Agentic RAG), novog AI paradigme u kojoj veliki jezični modeli (LLM-ovi) samostalno planiraju svoje sljedeće korake dok povlače informacije iz vanjskih izvora. Za razliku od statičnih obrazaca preuzimanja pa čitanja, Agentic RAG uključuje iterativne pozive LLM-u, isprekidane pozivima alata ili funkcija i strukturiranim izlazima. Sustav evaluira rezultate, poboljšava upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok se ne postigne zadovoljavajuće rješenje.

## Uvod

Ova lekcija će pokriti

- **Razumijevanje Agentic RAG:** Naučite o novoj paradigmi u AI-u u kojoj veliki jezični modeli (LLM-ovi) samostalno planiraju svoje sljedeće korake dok povlače informacije iz vanjskih izvora podataka.
- **Razumijevanje iterativnog Maker-Checker stila:** Savladajte petlju iterativnih poziva LLM-u, isprekidanu pozivima alata ili funkcija i strukturiranim izlazima, dizajniranom za poboljšanje ispravnosti i obrađivanje neispravnih upita.
- **Istraživanje praktičnih primjena:** Identificirajte scenarije u kojima Agentic RAG dolazi do izražaja, poput okruženja koja zahtijevaju ispravnost, kompleksnih interakcija s bazama podataka i proširenih tijekova rada.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako/razumjeti:

- **Razumijevanje Agentic RAG:** Naučiti o novoj paradigmi u AI-u u kojoj veliki jezični modeli (LLM-ovi) samostalno planiraju svoje sljedeće korake dok povlače informacije iz vanjskih izvora podataka.
- **Iterativni Maker-Checker stil:** Razumjeti koncept petlje iterativnih poziva LLM-u, isprekidanu pozivima alata ili funkcija i strukturiranim izlazima, dizajniranom za poboljšanje ispravnosti i rukovanje neispravnim upitima.
- **Vlastiti proces rezoniranja:** Shvatiti sustavsku sposobnost da posjeduje vlastiti proces rezoniranja, donoseći odluke o načinu pristupa problemima bez oslanjanja na prethodno definirane putanje.
- **Tijek rada:** Razumjeti kako agentni model samostalno odlučuje preuzeti izveštaje o tržišnim trendovima, identificirati podatke o konkurenciji, povezati unutarnje prodajne metrike, sintetizirati nalaze i evaluirati strategiju.
- **Iterativne petlje, integracija alata i memorija:** Naučiti o oslanjanju sustava na obrasce interakcije u petlji, održavajući stanje i memoriju kroz korake kako bi izbjegao repetitivne petlje i donosio informirane odluke.
- **Rukovanje načinima neuspjeha i samokorekcija:** Istražiti robusne mehanizme samokorekcije sustava, uključujući iteracije i ponovno upite, korištenje dijagnostičkih alata i oslanjanje na ljudski nadzor.
- **Granice agentnosti:** Razumjeti ograničenja Agentic RAG-a, fokusirajući se na autonomiju specifičnu za domenu, ovisnost o infrastrukturi i poštivanje sigurnosnih ograda.
- **Praktične primjene i vrijednost:** Identificirati scenarije u kojima Agentic RAG doista briljira, poput okruženja koja zahtijevaju ispravnost, kompleksnih interakcija s bazama podataka i proširenih tijekova rada.
- **Upravljanje, transparentnost i povjerenje:** Naučiti o važnosti upravljanja i transparentnosti, uključujući objašnjivo rezoniranje, kontrolu pristranosti i ljudski nadzor.

## Što je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova AI paradigma u kojoj veliki jezični modeli (LLM-ovi) samostalno planiraju svoje sljedeće korake dok povlače informacije iz vanjskih izvora. Za razliku od statičnih obrazaca preuzimanja zatim čitanja, Agentic RAG uključuje iterativne pozive LLM-u, isprekidane pozivima alata ili funkcija i strukturiranim izlazima. Sustav evaluira rezultate, poboljšava upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok ne postigne zadovoljavajuće rješenje. Ovaj iterativni “maker-checker” stil poboljšava ispravnost, obrađuje neispravne upite i osigurava visokokvalitetne rezultate.

Sustav aktivno posjeduje svoj proces rezoniranja, prepisujući neuspjele upite, birajući različite metode dohvaćanja i integrirajući više alata – poput pretraživanja vektora u Azure AI Search, SQL baza podataka ili prilagođenih API-ja – prije nego što finalizira svoj odgovor. Karakteristična osobina agentnog sustava je njegova sposobnost posjedovanja procesa rezoniranja. Tradicionalne RAG implementacije se oslanjaju na prethodno definirane putanje, dok agentni sustav samostalno određuje redoslijed koraka na temelju kvalitete pronalaženih informacija.

## Definiranje Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova paradigma u razvoju AI-a gdje LLM-ovi ne samo povlače informacije iz vanjskih izvora podataka, nego i samostalno planiraju svoje sljedeće korake. Za razliku od statičnih obrazaca preuzimanja pa čitanja ili pažljivo skriptiranih nizova promptova, Agentic RAG uključuje petlju iterativnih poziva LLM-u, isprekidanu pozivima alata ili funkcija i strukturiranim izlazima. Svakim korakom sustav procjenjuje dobivene rezultate, odlučuje hoće li poboljšati upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok se ne postigne zadovoljavajuće rješenje.

Ovaj iterativni “maker-checker” stil rada dizajniran je za poboljšanje ispravnosti, obradu neispravnih upita u strukturiranim bazama podataka (npr. NL2SQL) i osiguranje uravnoteženih, visokokvalitetnih rezultata. Umjesto oslanjanja isključivo na pažljivo inženjerski izrađene lance promptova, sustav aktivno posjeduje svoj proces rezoniranja. Može prepisati upite koji ne uspiju, odabrati drugačije metode dohvaćanja i integrirati više alata – kao što su pretraživanje vektora u Azure AI Search, SQL baze podataka ili prilagođeni API-ji – prije finalizacije odgovora. Ovo uklanja potrebu za previše složenim okvirima orkestracije. Umjesto toga, relativno jednostavna petlja “poziv LLM-a → korištenje alata → poziv LLM-a → …” može proizvesti sofisticirane i dobro utemeljene ishode.

![Agentic RAG Core Loop](../../../translated_images/hr/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Posjedovanje procesa rezoniranja

Karakteristična kvaliteta koja sustav čini “agentnim” je njegova sposobnost posjedovanja vlastitog procesa rezoniranja. Tradicionalne RAG implementacije često ovise o ljudima koji unaprijed definiraju put za model: lanac razmišljanja koji opisuje što dohvatiti i kada.
Ali kada je sustav zaista agentan, on interno odlučuje kako pristupiti problemu. Ne izvodi samo skriptu; samostalno određuje redoslijed koraka temeljen na kvaliteti pronađenih informacija.
Na primjer, ako ga se traži da kreira strategiju lansiranja proizvoda, ne oslanja se isključivo na prompt koji opisuje cijeli istraživački i proces donošenja odluka. Umjesto toga, agentni model samostalno odlučuje:

1. Preuzeti aktualne izvještaje o tržišnim trendovima koristeći Bing Web Grounding
2. Identificirati relevantne podatke o konkurenciji koristeći Azure AI Search.
3.	Povezati povijesne interne prodajne metrike koristeći Azure SQL bazu podataka.
4. Sintetizirati nalaze u koherentnu strategiju orkestriranu putem Azure OpenAI servisa.
5.	Evaluirati strategiju za praznine ili nekonzistentnosti, te po potrebi učiniti još jedan krug dohvaćanja podataka.
Svi ovi koraci—poboljšavanje upita, odabir izvora, iteracija dok nije “zadovoljno” odgovorom—odlučuje model, a ne unaprijed skriptirani čovjek.

## Iterativne petlje, integracija alata i memorija

![Tool Integration Architecture](../../../translated_images/hr/tool-integration.0f569710b5c17c10.webp)

Agentni sustav se oslanja na obrazac interakcije u petlji:

- **Početni poziv:** Korisnički cilj (tj. korisnički prompt) se prezentira LLM-u.
- **Poziv alata:** Ako model identificira nedostajuće informacije ili nejasne upute, odabire alat ili metodu dohvaćanja – poput upita u vektorsku bazu podataka (npr. Azure AI Search hibridno pretraživanje preko privatnih podataka) ili strukturiranog SQL poziva – kako bi prikupio dodatni kontekst.
- **Procjena i poboljšavanje:** Nakon pregleda vraćenih podataka, model odlučuje zadovoljavaju li informacije. Ako ne, poboljšava upit, pokušava s drugim alatom ili prilagođava pristup.
- **Ponavljanje dok nije zadovoljan:** Ovaj ciklus se nastavlja dok model ne procijeni da ima dovoljnu jasnoću i dokaze za konačni, dobro obrazloženi odgovor.
- **Memorija i stanje:** Budući da sustav održava stanje i memoriju kroz korake, može se prisjetiti prethodnih pokušaja i njihovih ishoda, izbjegavajući repetitivne petlje i donoseći informirane odluke tijekom procesa.

S vremenom, ovo stvara osjećaj evoluirajućeg razumijevanja, omogućujući modelu da navigira složenim zadacima s više koraka bez potrebe da čovjek stalno intervenira ili mijenja prompt.

## Rukovanje načinima neuspjeha i samokorekcija

Autonomija Agentic RAG-a uključuje i robusne mehanizme samokorekcije. Kada sustav naiđe na slijepa crijeva – poput povlačenja nerelevantnih dokumenata ili susreta s neispravnim upitima – može:

- **Iterirati i ponovno postaviti upite:** Umjesto vraćanja odgovora niske vrijednosti, model pokušava nove strategije pretraživanja, prepisuje upite baze podataka ili pregleda alternativne skupove podataka.
- **Koristiti dijagnostičke alate:** Sustav može pozvati dodatne funkcije dizajnirane za pomoć u debugiranju koraka rezoniranja ili potvrdu ispravnosti dohvaćenih podataka. Alati poput Azure AI Tracing bit će važni za omogućavanje robusne vidljivosti i praćenja.
- **Osloniti se na ljudski nadzor:** Za scenarije visokog rizika ili ponavljajućih neuspjeha, model može označiti nesigurnost i zatražiti ljudsko vodstvo. Nakon što čovjek da korektivne povratne informacije, model može uključiti to iskustvo u daljnji rad.

Ovaj iterativni i dinamični pristup omogućuje modelu kontinuirano poboljšanje, osiguravajući da nije samo sustav koji puca u jednom potezu, već onaj koji uči iz svojih pogrešaka tijekom sesije.

![Self Correction Mechanism](../../../translated_images/hr/self-correction.da87f3783b7f174b.webp)

## Granice agentnosti

Unatoč svojoj autonomiji unutar zadatka, Agentic RAG nije analogon umjetnoj općoj inteligenciji. Njegove “agentne” sposobnosti ograničene su na alate, izvore podataka i politike koje pružaju ljudski programeri. Ne može sam osmisliti vlastite alate ili izaći izvan granica domene koje su postavljene. Umjesto toga, izvrsno je u dinamičkom orkestriranju dostupnih resursa.
Ključne razlike u odnosu na naprednije oblike AI uključuju:

1. **Autonomija specifična za domenu:** Agentni RAG sustavi su usmjereni na postizanje korisnički definiranih ciljeva unutar poznate domene, koristeći strategije poput preformulacije upita ili izbora alata za poboljšanje ishoda.
2. **Ovisnost o infrastrukturi:** Sposobnosti sustava ovise o alatima i podacima koje integriraju programeri. Ne može prijeći ove granice bez ljudske intervencije.
3. **Poštivanje sigurnosnih ograda:** Etičke smjernice, pravila usklađenosti i poslovne politike ostaju vrlo važne. Sloboda agenta je uvijek ograničena sigurnosnim mjerama i mehanizmima nadzora (nadamo se).

## Praktične primjene i vrijednost

Agentic RAG briljira u scenarijima koji zahtijevaju iterativno usavršavanje i preciznost:

1. **Okruženja s naglaskom na ispravnost:** U provjerama usklađenosti, regulatornim analizama ili pravnim istraživanjima, agentni model može višekratno provjeravati činjenice, konzultirati više izvora i prepisivati upite dok ne proizvede temeljito provjereni odgovor.
2. **Složene interakcije s bazama podataka:** Kada se radi sa strukturiranim podacima gdje upiti često ne uspijevaju ili zahtijevaju prilagodbu, sustav može samostalno poboljšavati upite koristeći Azure SQL ili Microsoft Fabric OneLake, osiguravajući da konačan dohvat bude u skladu s korisničkom namjerom.
3. **Produženi tijekovi rada:** Duže sesije mogu evoluirati kako se pojavljuju nove informacije. Agentic RAG može kontinuirano uključivati nove podatke, mijenjajući strategije dok uči više o prostoru problema.

## Upravljanje, transparentnost i povjerenje

Kako ovi sustavi postaju autonomniji u rezoniranju, upravljanje i transparentnost su ključni:

- **Objašnjivo rezoniranje:** Model može pružiti zapisnik upita koje je napravio, izvora koje je konzultirao i koraka rezoniranja koje je proveo do svog zaključka. Alati poput Azure AI Content Safety i Azure AI Tracing / GenAIOps mogu pomoći u održavanju transparentnosti i smanjenju rizika.
- **Kontrola pristranosti i uravnotežen dohvat:** Programeri mogu podešavati strategije dohvaćanja kako bi osigurali da se uzimaju u obzir uravnoteženi, reprezentativni izvori podataka, te redovito auditirati izlaze na otkrivanje pristranosti ili iskrivljenih obrazaca koristeći prilagođene modele za napredne organizacije za podatkovnu znanost koristeći Azure Machine Learning.
- **Ljudski nadzor i usklađenost:** Za osjetljive zadatke, ljudski pregled ostaje ključan. Agentic RAG ne zamjenjuje ljudsku prosudbu u odlukama visokog rizika – nego je podržava pružanjem temeljitije provjerenih opcija.

Imajući alate koji pružaju jasan zapis akcija je esencijalno. Bez njih, debugiranje višekorakog procesa može biti vrlo teško. Pogledajte sljedeći primjer iz Literal AI (tvrtke iza Chainlit) za Agent-run:

![AgentRunExample](../../../translated_images/hr/AgentRunExample.471a94bc40cbdc0c.webp)

## Zaključak

Agentic RAG predstavlja prirodnu evoluciju u načinu na koji AI sustavi pristupaju složenim, podatcima intenzivnim zadacima. Usvajanjem obrasca interakcije u petlji, samostalnim odabirom alata i poboljšavanjem upita dok ne postigne visokokvalitetni rezultat, sustav nadilazi statičko praćenje promptova u prilagodljivijeg, kontekstualno svjesnog donositelja odluka. Iako još uvijek ograničen ljudski definiranim infrastrukturama i etičkim smjernicama, ove agentne sposobnosti omogućuju bogatije, dinamičnije i na kraju korisnije interakcije AI-a kako za tvrtke tako i za krajnje korisnike.

### Imate još pitanja o Agentic RAG-u?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici gdje možete upoznati druge polaznike, prisustvovati uredu za pitanja i dobiti odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementacija Retrieval Augmented Generation (RAG) s Azure OpenAI servisom: Naučite kako koristiti vlastite podatke uz Azure OpenAI servis. Ovaj Microsoft Learn modul pruža sveobuhvatan vodič o implementaciji RAG-a</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI aplikacija s Microsoft Foundry: Ovaj članak pokriva evaluaciju i usporedbu modela na javno dostupnim skupovima podataka, uključujući Agentic AI aplikacije i RAG arhitekture</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Što je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Potpuni vodič za agentno baziranu Retrieval Augmented Generaciju – Vijesti iz generacije RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: ubrzajte svoj RAG reformulacijom upita i samostalnim upitima! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodavanje agentnih slojeva u RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budućnost pomoćnika za znanje: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako izgraditi agentne RAG sustave</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Korištenje Microsoft Foundry Agent Service za skaliranje vaših AI agenata</a>

### Akademski radovi

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno usavršavanje sa samopovratnom informacijom</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezični agenti s verbalnim učenjem pojačanjem</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezični modeli mogu se samopopraviti pomoću interaktivne kritike alatom</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Pregled agentnog RAG-a</a>

## Prethodna lekcija

[Tool Use Design Pattern](../04-tool-use/README.md)

## Sljedeća lekcija

[Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->