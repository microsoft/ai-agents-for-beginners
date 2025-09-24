<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T23:04:19+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "hr"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.hr.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

# Agentic RAG

Ova lekcija pruža sveobuhvatan pregled Agentic Retrieval-Augmented Generation (Agentic RAG), novog AI pristupa u kojem veliki jezični modeli (LLM-ovi) autonomno planiraju svoje sljedeće korake dok prikupljaju informacije iz vanjskih izvora. Za razliku od statičnih obrazaca "pronađi pa pročitaj", Agentic RAG uključuje iterativne pozive LLM-u, izmjenjujući se s pozivima alata ili funkcija i strukturiranim izlazima. Sustav procjenjuje rezultate, usavršava upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok ne postigne zadovoljavajuće rješenje.

## Uvod

Ova lekcija obuhvaća:

- **Razumijevanje Agentic RAG-a:** Upoznajte se s novim pristupom u AI-u gdje veliki jezični modeli (LLM-ovi) autonomno planiraju svoje sljedeće korake dok prikupljaju informacije iz vanjskih izvora podataka.
- **Iterativni Maker-Checker stil:** Shvatite petlju iterativnih poziva LLM-u, izmjenjujući se s pozivima alata ili funkcija i strukturiranim izlazima, osmišljenim za poboljšanje točnosti i rješavanje neispravnih upita.
- **Istraživanje praktičnih primjena:** Identificirajte scenarije u kojima Agentic RAG briljira, poput okruženja gdje je točnost prioritet, složenih interakcija s bazama podataka i produženih radnih tijekova.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako/razumjeti:

- **Razumijevanje Agentic RAG-a:** Upoznajte se s novim pristupom u AI-u gdje veliki jezični modeli (LLM-ovi) autonomno planiraju svoje sljedeće korake dok prikupljaju informacije iz vanjskih izvora podataka.
- **Iterativni Maker-Checker stil:** Shvatite koncept petlje iterativnih poziva LLM-u, izmjenjujući se s pozivima alata ili funkcija i strukturiranim izlazima, osmišljenim za poboljšanje točnosti i rješavanje neispravnih upita.
- **Vlasništvo nad procesom zaključivanja:** Shvatite sposobnost sustava da preuzme odgovornost za svoj proces zaključivanja, donoseći odluke o pristupu problemima bez oslanjanja na unaprijed definirane putanje.
- **Radni tijek:** Razumjeti kako agentički model samostalno odlučuje dohvatiti izvještaje o tržišnim trendovima, identificirati podatke o konkurenciji, povezati interne prodajne metrike, sintetizirati nalaze i procijeniti strategiju.
- **Iterativne petlje, integracija alata i memorija:** Naučite o oslanjanju sustava na uzorak interakcije u petlji, održavajući stanje i memoriju kroz korake kako bi se izbjegle ponavljajuće petlje i donosile informirane odluke.
- **Rukovanje neuspjesima i samoispravljanje:** Istražite robusne mehanizme samoispravljanja sustava, uključujući iteraciju i ponovne upite, korištenje dijagnostičkih alata i oslanjanje na ljudski nadzor.
- **Granice agentičnosti:** Razumjeti ograničenja Agentic RAG-a, s fokusom na autonomiju specifičnu za domenu, ovisnost o infrastrukturi i poštivanje sigurnosnih ograda.
- **Praktični slučajevi upotrebe i vrijednost:** Identificirajte scenarije u kojima Agentic RAG briljira, poput okruženja gdje je točnost prioritet, složenih interakcija s bazama podataka i produženih radnih tijekova.
- **Upravljanje, transparentnost i povjerenje:** Naučite o važnosti upravljanja i transparentnosti, uključujući objašnjivo zaključivanje, kontrolu pristranosti i ljudski nadzor.

## Što je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je novi AI pristup u kojem veliki jezični modeli (LLM-ovi) autonomno planiraju svoje sljedeće korake dok prikupljaju informacije iz vanjskih izvora. Za razliku od statičnih obrazaca "pronađi pa pročitaj", Agentic RAG uključuje iterativne pozive LLM-u, izmjenjujući se s pozivima alata ili funkcija i strukturiranim izlazima. Sustav procjenjuje rezultate, usavršava upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok ne postigne zadovoljavajuće rješenje. Ovaj iterativni stil "maker-checker" poboljšava točnost, rješava neispravne upite i osigurava visokokvalitetne rezultate.

Sustav aktivno preuzima odgovornost za svoj proces zaključivanja, prepravljajući neuspjele upite, birajući različite metode dohvaćanja i integrirajući više alata—poput vektorskog pretraživanja u Azure AI Search, SQL baza podataka ili prilagođenih API-ja—prije nego što finalizira svoj odgovor. Ono što razlikuje agentički sustav je njegova sposobnost da preuzme odgovornost za svoj proces zaključivanja. Tradicionalne RAG implementacije oslanjaju se na unaprijed definirane putanje, dok agentički sustav autonomno određuje slijed koraka na temelju kvalitete pronađenih informacija.

## Definiranje Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je novi pristup u razvoju AI-a gdje LLM-ovi ne samo da prikupljaju informacije iz vanjskih izvora podataka već i autonomno planiraju svoje sljedeće korake. Za razliku od statičnih obrazaca "pronađi pa pročitaj" ili pažljivo skriptiranih nizova upita, Agentic RAG uključuje petlju iterativnih poziva LLM-u, izmjenjujući se s pozivima alata ili funkcija i strukturiranim izlazima. Na svakom koraku sustav procjenjuje dobivene rezultate, odlučuje hoće li usavršiti svoje upite, poziva dodatne alate ako je potrebno i nastavlja ovaj ciklus dok ne postigne zadovoljavajuće rješenje.

Ovaj iterativni stil rada "maker-checker" osmišljen je za poboljšanje točnosti, rješavanje neispravnih upita prema strukturiranim bazama podataka (npr. NL2SQL) i osiguravanje uravnoteženih, visokokvalitetnih rezultata. Umjesto da se oslanja isključivo na pažljivo osmišljene nizove upita, sustav aktivno preuzima odgovornost za svoj proces zaključivanja. Može prepravljati neuspjele upite, birati različite metode dohvaćanja i integrirati više alata—poput vektorskog pretraživanja u Azure AI Search, SQL baza podataka ili prilagođenih API-ja—prije nego što finalizira svoj odgovor. To uklanja potrebu za prekompliciranim orkestracijskim okvirima. Umjesto toga, relativno jednostavna petlja "LLM poziv → korištenje alata → LLM poziv → ..." može rezultirati sofisticiranim i dobro utemeljenim izlazima.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.hr.png)

## Preuzimanje odgovornosti za proces zaključivanja

Ono što sustav čini "agentičkim" je njegova sposobnost da preuzme odgovornost za svoj proces zaključivanja. Tradicionalne RAG implementacije često ovise o ljudima koji unaprijed definiraju putanju za model: lanac razmišljanja koji određuje što dohvatiti i kada.  
Ali kada je sustav zaista agentički, on interno odlučuje kako pristupiti problemu. Ne izvršava samo skriptu; autonomno određuje slijed koraka na temelju kvalitete pronađenih informacija.  
Na primjer, ako se od njega zatraži da kreira strategiju lansiranja proizvoda, ne oslanja se samo na upit koji detaljno opisuje cijeli tijek istraživanja i donošenja odluka. Umjesto toga, agentički model samostalno odlučuje:

1. Dohvatiti trenutne izvještaje o tržišnim trendovima koristeći Bing Web Grounding.  
2. Identificirati relevantne podatke o konkurenciji koristeći Azure AI Search.  
3. Povezati povijesne interne prodajne metrike koristeći Azure SQL Database.  
4. Sintetizirati nalaze u kohezivnu strategiju orkestriranu putem Azure OpenAI Service.  
5. Procijeniti strategiju za praznine ili nedosljednosti, pokrećući još jedan krug dohvaćanja ako je potrebno.  

Svi ovi koraci—usavršavanje upita, odabir izvora, iteracija dok ne bude "zadovoljan" odgovorom—odlučuje model, a ne unaprijed skriptirani ljudski koraci.

## Iterativne petlje, integracija alata i memorija

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.hr.png)

Agentički sustav oslanja se na uzorak interakcije u petlji:

- **Početni poziv:** Cilj korisnika (tj. korisnički upit) predstavlja se LLM-u.  
- **Poziv alata:** Ako model identificira nedostatak informacija ili nejasne upute, odabire alat ili metodu dohvaćanja—poput upita vektorske baze podataka (npr. Azure AI Search Hybrid pretraživanje privatnih podataka) ili strukturiranog SQL poziva—za prikupljanje više konteksta.  
- **Procjena i usavršavanje:** Nakon pregleda vraćenih podataka, model odlučuje jesu li informacije dovoljne. Ako nisu, usavršava upit, isprobava drugi alat ili prilagođava svoj pristup.  
- **Ponavljanje dok nije zadovoljan:** Ovaj ciklus se nastavlja dok model ne zaključi da ima dovoljno jasnoće i dokaza za isporuku konačnog, dobro utemeljenog odgovora.  
- **Memorija i stanje:** Budući da sustav održava stanje i memoriju kroz korake, može se prisjetiti prethodnih pokušaja i njihovih ishoda, izbjegavajući ponavljajuće petlje i donoseći informiranije odluke kako napreduje.  

S vremenom, ovo stvara osjećaj evoluirajućeg razumijevanja, omogućujući modelu da navigira složenim, višestupanjskim zadacima bez potrebe za stalnom ljudskom intervencijom ili preoblikovanjem upita.

## Rukovanje neuspjesima i samoispravljanje

Autonomija Agentic RAG-a također uključuje robusne mehanizme samoispravljanja. Kada sustav naiđe na slijepu ulicu—poput dohvaćanja irelevantnih dokumenata ili nailaska na neispravne upite—može:

- **Iterirati i ponovno upitati:** Umjesto da vrati odgovore niske vrijednosti, model pokušava nove strategije pretraživanja, prepravlja upite baze podataka ili pregledava alternativne skupove podataka.  
- **Koristiti dijagnostičke alate:** Sustav može pozvati dodatne funkcije osmišljene za pomoć u otklanjanju pogrešaka u koracima zaključivanja ili potvrđivanju točnosti dohvaćenih podataka. Alati poput Azure AI Tracing bit će važni za omogućavanje robusne promatrivosti i praćenja.  
- **Osloniti se na ljudski nadzor:** Za scenarije visokog rizika ili one koji se ponavljano ne uspijevaju riješiti, model može označiti nesigurnost i zatražiti ljudsko vođenje. Nakon što ljudski korisnik pruži korektivne povratne informacije, model može uključiti tu lekciju u budućem radu.  

Ovaj iterativni i dinamični pristup omogućuje modelu kontinuirano poboljšanje, osiguravajući da nije samo sustav za jednokratnu upotrebu, već onaj koji uči iz svojih pogrešaka tijekom određene sesije.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.hr.png)

## Granice agentičnosti

Unatoč svojoj autonomiji unutar zadatka, Agentic RAG nije analogan umjetnoj općoj inteligenciji. Njegove "agentičke" sposobnosti ograničene su na alate, izvore podataka i politike koje su osigurali ljudski programeri. Ne može izmišljati vlastite alate niti izlaziti izvan granica domena koje su postavljene. Umjesto toga, briljira u dinamičnom orkestriranju dostupnih resursa.  
Ključne razlike u odnosu na naprednije AI oblike uključuju:

1. **Autonomija specifična za domenu:** Agentic RAG sustavi fokusirani su na postizanje ciljeva koje definira korisnik unutar poznate domene, koristeći strategije poput prepravljanja upita ili odabira alata za poboljšanje rezultata.  
2. **Ovisnost o infrastrukturi:** Sposobnosti sustava ovise o alatima i podacima koje su integrirali programeri. Ne može nadmašiti te granice bez ljudske intervencije.  
3. **Poštivanje sigurnosnih ograda:** Etičke smjernice, pravila usklađenosti i poslovne politike ostaju vrlo važne. Sloboda agenta uvijek je ograničena sigurnosnim mjerama i mehanizmima nadzora (nadamo se?).  

## Praktični slučajevi upotrebe i vrijednost

Agentic RAG briljira u scenarijima koji zahtijevaju iterativno usavršavanje i preciznost:

1. **Okruženja gdje je točnost prioritet:** U provjerama usklađenosti, regulatornim analizama ili pravnim istraživanjima, agentički model može ponavljano provjeravati činjenice, konzultirati više izvora i prepravljati upite dok ne proizvede temeljito provjeren odgovor.  
2. **Složene interakcije s bazama podataka:** Kada se radi o strukturiranim podacima gdje upiti često mogu ne uspjeti ili trebaju prilagodbu, sustav može autonomno usavršavati svoje upite koristeći Azure SQL ili Microsoft Fabric OneLake, osiguravajući da konačno dohvaćanje odgovara korisnikovoj namjeri.  
3. **Produženi radni tijekovi:** Duže sesije mogu se razvijati kako se pojavljuju nove informacije. Agentic RAG može kontinuirano uključivati nove podatke, mijenjajući strategije kako saznaje više o problemu.  

## Upravljanje, transparentnost i povjerenje

Kako ovi sustavi postaju autonomniji u svom zaključivanju, upravljanje i transparentnost su ključni:

- **Objašnjivo zaključivanje:** Model može pružiti trag audita upita koje je napravio, izvora koje je konzultirao i koraka zaključivanja koje je poduzeo kako bi došao do zaključka. Alati poput Azure AI Content Safety i Azure AI Tracing / GenAIOps mogu pomoći u održavanju transparentnosti i smanjenju rizika.  
- **Kontrola pristranosti i uravnoteženo dohvaćanje:** Programeri mogu prilagoditi strategije dohvaćanja kako bi osigurali da se uzimaju u obzir uravnoteženi, reprezentativni izvori podataka, te redovito provjeravati izlaze kako bi otkrili pristranost ili iskrivljene obrasce koristeći prilagođene modele za napredne organizacije za podatkovnu znanost koristeći Azure Machine Learning.  
- **Ljudski nadzor i usklađenost:** Za osjetljive zadatke, ljudska revizija ostaje ključna. Agentic RAG ne zamjenjuje ljudsku prosudbu u odlukama visokog rizika—on je nadopunjuje pružanjem temeljito provjerenih opcija.  

Imati alate koji pružaju jasan zapis radnji je ključno. Bez njih, otklanjanje pogrešaka u višestupanjskom procesu može biti vrlo teško. Pogledajte sljedeći primjer iz Literal AI (tvrtka iza Chainlit-a) za Agent run:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.hr.png)

## Zaključak

Agentic RAG predstavlja prirodnu evoluciju u načinu na koji AI sustavi rješavaju složene, podatkovno intenzivne zadatke. Usvajanjem uzorka interakcije u petlji, autonomnim odabirom alata i usavršavanjem upita dok ne postigne visokokvalitetan rezultat, sustav prelazi granice statičnog praćenja upita u adaptivnijeg, kontekstualno svjesnog donositelja odluka. Iako je još uvijek ograničen ljudski definiranim infrastrukturama i etičkim smjernicama, ove agentičke sposobnosti omogućuju bogatije, dinamičnije i na kraju korisnije AI interakcije za poduzeća i krajnje korisnike.

### Imate još pitanja o Agentic RAG-u?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima,
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementacija Retrieval Augmented Generation (RAG) s Azure OpenAI Service: Naučite kako koristiti vlastite podatke s Azure OpenAI Service. Ovaj Microsoft Learn modul pruža sveobuhvatan vodič za implementaciju RAG-a  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluacija generativnih AI aplikacija s Azure AI Foundry: Ovaj članak pokriva evaluaciju i usporedbu modela na javno dostupnim skupovima podataka, uključujući Agentic AI aplikacije i RAG arhitekture</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Što je Agentic RAG | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Potpuni vodič za generaciju uz pomoć agenata – Novosti iz generacije RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: ubrzajte svoj RAG s reformulacijom upita i samostalnim upitima! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodavanje agentnih slojeva RAG-u</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budućnost asistenata za znanje: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kako izgraditi Agentic RAG sustave</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Korištenje Azure AI Foundry Agent Service za skaliranje vaših AI agenata</a>  

### Akademski radovi  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativno usavršavanje uz povratne informacije</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jezični agenti s verbalnim učenjem pojačanja</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veliki jezični modeli mogu se samostalno ispravljati uz interaktivno kritiziranje alata</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Pregled Agentic RAG-a</a>  

## Prethodna lekcija  

[Tool Use Design Pattern](../04-tool-use/README.md)  

## Sljedeća lekcija  

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)  

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.