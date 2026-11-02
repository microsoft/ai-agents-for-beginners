[![Agentic RAG](../../../translated_images/hr/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na gornju sliku za prikaz videa ove lekcije)_

# Agentic RAG

Ova lekcija pruža sveobuhvatan pregled Agentic Retrieval-Augmented Generation (Agentic RAG), novog AI paradigme u kojoj veliki jezični modeli (LLM) autonomno planiraju svoje sljedeće korake dok izvlače informacije iz vanjskih izvora. Za razliku od statičnih obrazaca dohvaćanja pa čitanja, Agentic RAG uključuje iterativne pozive LLM-u, isprekidane pozivima alata ili funkcija i strukturiranim izlazima. Sustav procjenjuje rezultate, usavršava upite, poziva dodatne alate po potrebi i nastavlja ovaj ciklus dok se ne postigne zadovoljavajuće rješenje.

## Uvod

Ova lekcija će pokriti

- **Razumijevanje Agentic RAG:** Upoznajte se s novom paradigmom u AI-u gdje veliki jezični modeli (LLM) autonomno planiraju svoje sljedeće korake dok izvlače informacije iz vanjskih izvora podataka.
- **Razumijevanje iterativnog Maker-Checker stila:** Razumjeti petlju iterativnih poziva LLM-u, isprekidanih pozivima alata ili funkcija i strukturiranim izlazima, dizajniranu za poboljšanje točnosti i rukovanje neispravnim upitima.
- **Istraživanje praktičnih primjena:** Identificirajte scenarije u kojima Agentic RAG briljira, kao što su okruženja s prioritetom na točnost, kompleksne interakcije s bazama podataka i prošireni radni tokovi.

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete kako/razumjeti:

- **Razumijevanje Agentic RAG:** Upoznajte se s novom paradigmom u AI-u gdje veliki jezični modeli (LLM) autonomno planiraju svoje sljedeće korake dok izvlače informacije iz vanjskih izvora podataka.
- **Iterativni Maker-Checker stil:** Razumite koncept petlje iterativnih poziva LLM-u, isprekidanih pozivima alata ili funkcija i strukturiranim izlazima, dizajniranom za poboljšanje točnosti i rukovanje neispravnim upitima.
- **Vlasništvo nad procesom razmišljanja:** Razumjeti sposobnost sustava da preuzme vlasništvo nad svojim procesom razmišljanja, donoseći odluke kako pristupiti problemima bez oslanjanja na unaprijed definirane puteve.
- **Radni tok:** Razumjeti kako agentni model samostalno odlučuje dohvatiti izvještaje o tržišnim trendovima, identificirati podatke o konkurentima, povezati unutarnje prodajne metrike, sintetizirati nalaze i evaluirati strategiju.
- **Iterativne petlje, integracija alata i memorija:** Naučiti o oslanjanju sustava na obrazac petljaste interakcije, održavajući stanje i memoriju kroz korake kako bi se izbjegle ponavljajuće petlje i donosile informirane odluke.
- **Rukovanje načinima neuspjeha i samo-ispravljanje:** Istražiti robusne mehanizme samo-ispravljanja sustava, uključujući iteriranje i ponovni upit, korištenje dijagnostičkih alata i oslanjanje na ljudski nadzor.
- **Granice agentnosti:** Razumjeti ograničenja Agentic RAG-a, fokusirano na autonomiju specifičnu za domenu, ovisnost o infrastrukturi i poštivanje pravila.
- **Praktični slučajevi korištenja i vrijednost:** Identificirati scenarije u kojima Agentic RAG briljira, kao što su okruženja s prioritetom na točnost, kompleksne interakcije s bazama podataka i prošireni radni tokovi.
- **Upravljanje, transparentnost i povjerenje:** Naučiti o važnosti upravljanja i transparentnosti, uključujući objašnjivo razmišljanje, kontrolu pristranosti i ljudski nadzor.

## Što je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova AI paradigma u kojoj veliki jezični modeli (LLM) autonomno planiraju svoje sljedeće korake dok izvlače informacije iz vanjskih izvora. Za razliku od statičnih obrazaca dohvaćanja pa čitanja, Agentic RAG uključuje iterativne pozive LLM-u, isprekidane pozivima alata ili funkcija i strukturiranim izlazima. Sustav procjenjuje rezultate, usavršava upite, poziva dodatne alate po potrebi i nastavlja ovaj ciklus dok se ne postigne zadovoljavajuće rješenje. Ovaj iterativni “maker-checker” stil poboljšava točnost, rukuje neispravnim upitima i osigurava visokokvalitetne rezultate.

Sustav aktivno preuzima vlasništvo nad svojim procesom razmišljanja, prepisuje neuspjele upite, bira različite metode dohvaćanja i integrira više alata—kao što su pretraživanje vektora u Azure AI Search, SQL baze podataka ili prilagođeni API-jevi—prije nego što finalizira svoj odgovor. Prepoznatljiva kvaliteta agentnog sustava je njegova sposobnost da preuzme vlasništvo nad svojim procesom razmišljanja. Tradicionalne implementacije RAG oslanjaju se na unaprijed definirane putove, dok agentni sustav autonomno određuje redoslijed koraka na temelju kvalitete informacija koje pronađe.

## Definiranje Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nova paradigma u razvoju AI-a gdje LLM-ovi ne samo da izvlače informacije iz vanjskih izvora podataka, već i autonomno planiraju svoje sljedeće korake. Za razliku od statičnih obrazaca dohvaćanja pa čitanja ili pažljivo skriptiranih nizova upita, Agentic RAG uključuje petlju iterativnih poziva LLM-u, isprekidanu pozivima alata ili funkcija i strukturiranim izlazima. Na svakom koraku sustav procjenjuje rezultate koje je dobio, odlučuje treba li usavršiti upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok ne postigne zadovoljavajuće rješenje.

Ovaj iterativni “maker-checker” stil rada dizajniran je za poboljšanje točnosti, rukovanje neispravnim upitima prema strukturiranim bazama podataka (npr. NL2SQL) i osiguranje izbalansiranih, visokokvalitetnih rezultata. Umjesto da se oslanja isključivo na pažljivo izrađene lance upita, sustav aktivno preuzima vlasništvo nad svojim procesom razmišljanja. Može prepisivati neuspjele upite, odabrati različite metode dohvaćanja i integrirati više alata—kao što su pretraživanje vektora u Azure AI Search, SQL baze podataka ili prilagođene API-jeve—prije finalizacije odgovora. To uklanja potrebu za previše složenim orkestracijskim okvirima. Umjesto toga, relativno jednostavna petlja “poziv LLM-u → korištenje alata → poziv LLM-u → …” može proizvesti sofisticirane i dobro utemeljene izlaze.

![Agentic RAG Core Loop](../../../translated_images/hr/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Preuzimanje vlasništva nad procesom razmišljanja

Prepoznatljiva kvaliteta koja čini sustav “agentnim” je njegova sposobnost da preuzme vlasništvo nad svojim procesom razmišljanja. Tradicionalne implementacije RAG često ovise o ljudima koji unaprijed definiraju put za model: lanac razmišljanja koji iznosi što treba dohvatiti i kada.
Ali kada je sustav stvarno agentan, on interno odlučuje kako pristupiti problemu. Ne izvršava samo skriptu; autonomno određuje redoslijed koraka na temelju kvalitete informacija koje pronađe.
Na primjer, ako ga se pita da kreira strategiju lansiranja proizvoda, ne oslanja se samo na upit koji specificira cijeli istraživački i proces donošenja odluka. Umjesto toga, agentni model samostalno odlučuje:

1. Dohvatiti trenutne izvještaje o tržišnim trendovima koristeći Bing Web Grounding
2. Identificirati relevantne podatke o konkurenciji koristeći Azure AI Search.
3. Povezati povijesne unutarnje prodajne metrike koristeći Azure SQL Database.
4. Sintetizirati nalaze u kohezivnu strategiju orkestriranu putem Azure OpenAI Servisa.
5. Evaluirati strategiju na praznine ili nedosljednosti, aktivirajući još jedan krug dohvaćanja ako je potrebno.
Sve ove korake—usavršavanje upita, odabir izvora, iteriranje dok ne bude “zadovoljan” odgovorom—odlučuje model, a ne unaprijed je skriptirao čovjek.

## Iterativne petlje, integracija alata i memorija

![Tool Integration Architecture](../../../translated_images/hr/tool-integration.0f569710b5c17c10.webp)

Agentni sustav se oslanja na obrazac petljaste interakcije:

- **Početni poziv:** Cilj korisnika (tj. korisnički upit) se predstavlja LLM-u.
- **Poziv alata:** Ako model identificira nedostatak informacija ili nejasne upute, odabire alat ili metodu dohvata—kao što je upit prema vektorskoj bazi podataka (npr. Azure AI Search Hybrid pretraživanje privatnih podataka) ili strukturirani SQL poziv—za prikupljanje više konteksta.
- **Procjena i usavršavanje:** Nakon pregleda vraćenih podataka, model odlučuje jesu li informacije dovoljne. Ako nisu, usavršava upit, pokušava s drugim alatom ili prilagođava pristup.
- **Ponavljanje dok nije zadovoljan:** Ovaj ciklus se nastavlja dok model ne zaključi da ima dovoljno jasnoće i dokaza da isporuči konačni, dobro rezonirani odgovor.
- **Memorija i stanje:** Budući da sustav održava stanje i memoriju kroz korake, može se prisjetiti prethodnih pokušaja i njihovih ishoda, izbjegavajući ponavljajuće petlje i donoseći informiranije odluke tijekom procesa.

Vremenom to stvara osjećaj evoluirajućeg razumijevanja, omogućujući modelu da navigira složenim, višekoracnim zadacima bez potrebe za stalnom ljudskom intervencijom ili preoblikovanjem upita.

## Rukovanje načinima neuspjeha i samo-ispravljanje

Autonomija Agentic RAG-a također uključuje robusne mehanizme samo-ispravljanja. Kada sustav naiđe na mrtve točke—poput dohvaćanja irelevantnih dokumenata ili susretanja s neispravnim upitima—može:

- **Iterirati i ponovno upitavati:** Umjesto da vraća niske vrijednosti odgovore, model pokušava nove strategije pretraživanja, prepisuje upite prema bazi podataka ili gleda alternativne skupove podataka.
- **Koristiti dijagnostičke alate:** Sustav može pozvati dodatne funkcije dizajnirane da mu pomognu otkloniti pogreške u koracima zaključivanja ili potvrditi točnost dohvaćenih podataka. Alati poput Azure AI Tracing bit će važni za omogućavanje robusne promatranja i nadzora.
- **Oslanjanje na ljudski nadzor:** Za zadatke visokog rizika ili ponavljajuće neuspješne scenarije, model može signalizirati nesigurnost i zatražiti ljudsku pomoć. Nakon što čovjek pruži korektivnu povratnu informaciju, model može uključiti taj nauk za dalje.

Ovaj iterativni i dinamični pristup omogućava modelu kontinuirano poboljšavanje, osiguravajući da nije samo sustav jedne prilike, već onaj koji uči iz svojih pogrešaka tijekom zadane sesije.

![Self Correction Mechanism](../../../translated_images/hr/self-correction.da87f3783b7f174b.webp)

## Granice agentnosti

Unatoč svojoj autonomiji unutar zadatka, Agentic RAG nije analogija umjetnoj općoj inteligenciji. Njegove “agentne” sposobnosti ograničene su na alate, izvore podataka i politike koje su dali ljudski programeri. Ne može izumiti vlastite alate ili izaći izvan granica domene koje su postavljene. Umjesto toga, odlično upravlja resursima pri ruci.
Ključne razlike u odnosu na naprednije oblike AI uključuju:

1. **Autonomija specifična za domen:** Agentic RAG sustavi su fokusirani na postizanje ciljeva definiranih od strane korisnika unutar poznate domene, koristeći strategije poput prepisivanja upita ili odabira alata za poboljšanje ishoda.
2. **Ovisnost o infrastrukturi:** Sposobnosti sustava ovise o alatima i podacima integriranim od strane programera. Ne može prijeći te granice bez ljudske intervencije.
3. **Poštivanje pravila:** Etičke smjernice, pravila usklađenosti i poslovne politike ostaju vrlo važni. Sloboda agenta uvijek je ograničena sigurnosnim mjerama i mehanizmima nadzora (nadamo se).

## Praktični slučajevi korištenja i vrijednost

Agentic RAG briljira u scenarijima koji zahtijevaju iterativno usavršavanje i preciznost:

1. **Okruženja s prioritetom na točnost:** U provjerama usklađenosti, regulatornoj analizi ili pravnim istraživanjima, agentni model može višestruko provjeravati činjenice, konzultirati više izvora i prepisivati upite dok ne proizvede temeljito provjeren odgovor.
2. **Složene interakcije s bazama podataka:** Kada se radi o strukturiranim podacima gdje upiti često mogu zakazati ili trebaju prilagodbu, sustav može autonomno usavršavati svoje upite koristeći Azure SQL ili Microsoft Fabric OneLake, osiguravajući da konačni dohvati odgovaraju namjeri korisnika.
3. **Prošireni radni tokovi:** Dulje sesije mogu se razvijati kako se pojavljuju novi podaci. Agentic RAG može kontinuirano uključivati nove podatke i mijenjati strategije kako saznaje više o problemu.

## Upravljanje, transparentnost i povjerenje

Kako ovi sustavi postaju autonomniji u svom razmišljanju, upravljanje i transparentnost su ključni:

- **Objašnjivo razmišljanje:** Model može pružiti zapisnik upita koje je napravio, izvora koje je konzultirao i koraka razmišljanja koje je poduzeo da bi došao do zaključka. Alati poput Azure AI Content Safety i Azure AI Tracing / GenAIOps mogu pomoći u održavanju transparentnosti i smanjenju rizika.
- **Kontrola pristranosti i izbalansirani dohvat:** Programeri mogu prilagoditi strategije dohvaćanja kako bi osigurali uzimanje u obzir izbalansiranih, reprezentativnih izvora podataka i redovito pregledavati izlaze za otkrivanje pristranosti ili iskrivljenih obrazaca koristeći prilagođene modele za napredne organizacije za znanost o podacima koristeći Azure Machine Learning.
- **Ljudski nadzor i usklađenost:** Za osjetljive zadatke ljudski pregled ostaje ključan. Agentic RAG ne zamjenjuje ljudsku prosudbu u visokorizičnim odlukama—on ju proširuje pružajući temeljito provjerene opcije.

Imati alate koji pružaju jasan zapis radnji je presudno. Bez njih je vrlo teško otkloniti pogreške u višekorakom procesu. Pogledajte sljedeći primjer iz Literal AI (tvrtka iza Chainlit) za pokretanje agenta:

![AgentRunExample](../../../translated_images/hr/AgentRunExample.471a94bc40cbdc0c.webp)

## Zaključak

Agentic RAG predstavlja prirodnu evoluciju u načinu na koji AI sustavi rješavaju složene, podatkovno intenzivne zadatke. Usvajanjem petljastog obrasca interakcije, autonomnim odabirom alata i usavršavanjem upita dok ne postignu visokokvalitetan rezultat, sustav prelazi granicu statičnog praćenja upita u prilagodljivijeg, kontekstualno svjesnog donositelja odluka. Iako je i dalje ograničen infrastrukturom i etičkim smjernicama definiranim od strane ljudi, ove agentne sposobnosti omogućuju bogatije, dinamičnije i u konačnici korisnije AI interakcije za poduzeća i krajnje korisnike.

### Imate li dodatnih pitanja o Agentic RAG-u?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se susreli s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementacija Retrieval Augmented Generation (RAG) uz Azure OpenAI Service: Naučite kako koristiti vlastite podatke sa servisom Azure OpenAI. Ovaj Microsoft Learn modul pruža sveobuhvatan vodič za implementaciju RAG-a</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI aplikacija uz Microsoft Foundry: Ovaj članak pokriva evaluaciju i usporedbu modela na javno dostupnim skupovima podataka, uključujući agentne AI aplikacije i RAG arhitekture</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Što je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Potpuni vodič za agentno Retrieval Augmented Generation – Vijesti iz generacije RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: pojačajte svoj RAG reformulacijom upita i samopitanjem! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodavanje agentnih slojeva RAG-u</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budućnost pomoćnika za znanje: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako izraditi agentne RAG sustave</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Korištenje Microsoft Foundry Agent Service za skaliranje vaših AI agenata</a>

### Akademski radovi

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno usavršavanje s samopovratnom informacijom</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezični agenti s verbalnim učenjem pojačanjem</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezični modeli mogu se samostalno ispravljati interaktivnim kritiziranjem pomoću alata</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agent-based Retrieval-Augmented Generation: Pregled Agentic RAG</a>

## Dimsko testiranje ovog agenta (opcionalno)

Nakon što naučite kako postaviti agente u [Lekcija 16](../16-deploying-scalable-agents/README.md), možete dimski testirati `TravelRAGAgent` iz ove lekcije — provjeravajući da njegovi odgovori ostaju utemeljeni u bazi znanja — s [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Pogledajte [`tests/README.md`](../tests/README.md) kako ga pokrenuti.

## Prethodna lekcija

[Dizajnerski obrazac korištenja alata](../04-tool-use/README.md)

## Sljedeća lekcija

[Izgradnja pouzdanih AI agenata](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->