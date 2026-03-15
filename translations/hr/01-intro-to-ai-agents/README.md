[![Uvod u AI agente](../../../translated_images/hr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na gornju sliku za prikaz videa ovog poglavlja)_


# Uvod u AI agente i primjere upotrebe agenata

Dobrodošli na tečaj "AI agenti za početnike"! Ovaj tečaj pruža osnovno znanje i primjere primjene za izgradnju AI agenata.

Pridružite se <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord zajednici</a> da biste upoznali druge polaznike i kreatore AI agenata i postavili sva pitanja vezana uz ovaj tečaj.

Za početak ovog tečaja, započinjemo s boljim razumijevanjem što su AI agenti i kako ih možemo koristiti u aplikacijama i radnim tokovima koje gradimo.

## Uvod

Ovo poglavlje obuhvaća:

- Što su AI agenti i koje su različite vrste agenata?
- Koje su najbolje primjene za AI agente i kako nam oni mogu pomoći?
- Koji su neki osnovni blokovi pri dizajniranju agentnih rješenja?

## Ciljevi učenja
Nakon dovršetka ovog poglavlja, trebali biste biti sposobni:

- Razumjeti koncepte AI agenata i kako se oni razlikuju od drugih AI rješenja.
- Najefikasnije primijeniti AI agente.
- Produktivno dizajnirati agentna rješenja za korisnike i kupce.

## Definiranje AI agenata i vrste AI agenata

### Što su AI agenti?

AI agenti su **sustavi** koji omogućuju **velikim jezičnim modelima (LLM-ovima)** da **izvršavaju radnje** proširujući njihove sposobnosti tako što omogućuju LLM-ovima **pristup alatima** i **znanju**.

Razložimo ovu definiciju na manje dijelove:

- **Sustav** – važno je misliti o agentima ne samo kao o jednoj komponenti, nego kao o sustavu mnogih komponenti. Na osnovnoj razini, komponente AI agenta su:
  - **Okruženje** – definirani prostor u kojem AI agent djeluje. Na primjer, ako imamo AI agenta za rezervaciju putovanja, okruženje može biti sustav za rezervaciju putovanja koji agent koristi za izvršavanje zadataka.
  - **Senzori** – okruženja imaju informacije i pružaju povratne informacije. AI agenti koriste senzore za prikupljanje i tumačenje ovih informacija o trenutnom stanju okruženja. U primjeru AI agenta za rezervaciju putovanja, sustav za rezervaciju može pružiti informacije kao što su dostupnost hotela ili cijene letova.
  - **Aktuatori** – nakon što AI agent dobije trenutno stanje okruženja, za trenutni zadatak agent određuje koju akciju treba izvršiti da promijeni okruženje. Za AI agenta za rezervaciju putovanja to može biti rezervacija dostupne sobe za korisnika.

![Što su AI agenti?](../../../translated_images/hr/what-are-ai-agents.1ec8c4d548af601a.webp)

**Veliki jezični modeli** – koncept agenata postojao je i prije nastanka LLM-ova. Prednost izgradnje AI agenata s LLM-ovima jest njihova sposobnost razumijevanja ljudskog jezika i podataka. Ova sposobnost omogućuje LLM-ovima tumačenje informacija iz okruženja i definiranje plana za promjenu okruženja.

**Izvršavanje radnji** – izvan sustava AI agenata, LLM-ovi su ograničeni na situacije u kojima je radnja generiranje sadržaja ili informacija na temelju korisničkog upita. Unutar sustava AI agenata, LLM-ovi mogu obavljati zadatke tumačenjem zahtjeva korisnika i korištenjem alata dostupnih u njihovom okruženju.

**Pristup alatima** – koji alati su dostupni LLM-u definira 1) okruženje u kojem djeluje i 2) programer AI agenta. U našem primjeru sa agentom za putovanja alati su ograničeni na operacije dostupne u sustavu za rezervaciju, a/ili programer može ograničiti pristup alata za letove.

**Memorija i znanje** – Memorija može biti kratkoročna u kontekstu razgovora između korisnika i agenta. Dugoročno, osim informacija koje okruženje pruža, AI agenti mogu pribavljati znanja iz drugih sustava, usluga, alata, pa čak i drugih agenata. U primjeru s agentom za putovanja, to znanje može biti informacija o korisnikovim putnim preferencijama pohranjenim u korisničkoj bazi podataka.

### Različite vrste agenata

Sad kada imamo opću definiciju AI agenata, pogledajmo neke specifične vrste agenata i kako bi se primijenili u agentu za rezervaciju putovanja.

| **Vrsta agenta**               | **Opis**                                                                                                                            | **Primjer**                                                                                                                                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Jednostavni refleksni agenti** | Izvršavaju trenutne radnje na temelju unaprijed definiranim pravilima.                                                             | Agent za putovanja interpretira kontekst e-pošte i prosljeđuje pritužbe o putovanjima službi za korisnike.                                                                                        |
| **Refleksni agenti temeljeni na modelu** | Izvršavaju radnje na temelju modela svijeta i promjena u tom modelu.                                                            | Agent za putovanja prioritizira rute s velikim promjenama cijena temeljem dostupnih povijesnih podataka o cijenama.                                                                             |
| **Agent za ciljeve**             | Kreira planove za ostvarenje specifičnih ciljeva tumačenjem cilja i određivanjem radnji za njegovo ostvarenje.                 | Agent za putovanja rezervira putovanje određujući potrebne aranžmane (auto, javni prijevoz, letovi) od trenutne lokacije do odredišta.                                                          |
| **Agent s utilitarnim pristupom** | Razmatra preferencije i numerički procjenjuje kompromise kako bi odredio kako ostvariti ciljeve.                                   | Agent za putovanja maksimizira korisnost procjenjujući pogodnost u odnosu na cijenu prilikom rezervacije putovanja.                                                                             |
| **Učeći agenti**                | Poboljšavaju se tijekom vremena odgovarajući na povratne informacije i prilagođavajući radnje prema tome.                        | Agent za putovanja se poboljšava koristeći povratne informacije korisnika iz anketa nakon putovanja kako bi prilagodio buduće rezervacije.                                                     |
| **Hijerarhijski agenti**        | Sastoje se od više agenata u slojevitom sustavu, gdje viši agenti razlažu zadatke na podzadace za niže agente koji ih izvršavaju. | Agent za putovanja otkazuje putovanje dijeleći zadatak na podzadace (npr. otkazivanje određenih rezervacija) koje izvršavaju niži agenti te izvještavaju višeg agenta.                            |
| **Sustavi više agenata (MAS)**  | Agenti neovisno izvršavaju zadatke, bilo kooperativno ili natjecateljski.                                                          | Kooperativno: Više agenata rezervira različite usluge poput hotela, letova i zabave. Natjecateljski: Više agenata upravlja i natječe se za zajednički kalendar rezervacija hotela za korisnike. |

## Kada koristiti AI agente

U ranijem dijelu koristili smo primjer AI agenta za putovanja da objasnimo kako se različite vrste agenata mogu koristiti u različitim scenarijima rezervacije putovanja. Nastavit ćemo koristiti ovu aplikaciju kroz cijeli tečaj.

Pogledajmo vrste primjena za koje su AI agenti najprikladniji:

![Kada koristiti AI agente?](../../../translated_images/hr/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemi otvorenog tipa** – dopuštaju LLM-u da odredi potrebne korake za izvršenje zadatka jer se ne mogu uvijek unaprijed definirati u radnom toku.
- **Višekorakni procesi** – zadaci koji zahtijevaju razinu složenosti pri kojoj AI agent treba koristiti alate ili informacije tijekom više koraka umjesto jednokratnog dohvaćanja.  
- **Poboljšavanje tijekom vremena** – zadaci gdje se agent može poboljšavati primajući povratne informacije iz okruženja ili od korisnika kako bi pružio veću korisnost.

Više razmatranja o korištenju AI agenata obrađujemo u lekciji Izgradnja pouzdanih AI agenata.

## Osnove agentnih rješenja

### Razvoj agenta

Prvi korak u dizajniranju sustava AI agenta je definirati alate, radnje i ponašanja. U ovom tečaju fokusiramo se na korištenje **Azure AI Agent Service** za definiranje naših agenata. On nudi značajke poput:

- Izbor popularnih otvorenih modela kao što su OpenAI, Mistral i Llama
- Korištenje licenciranih podataka preko pružatelja poput Tripadvisor
- Korištenje standardiziranih OpenAPI 3.0 alata

### Agentni obrasci

Komunikacija s LLM-ovima se odvija putem upita (prompta). S obzirom na poluautonomnu prirodu AI agenata, nije uvijek moguće ili potrebno ručno ponovo slati upite LLM-u kad dođe do promjena u okruženju. Koristimo **agentne obrasce** koji nam omogućuju slanje upita LLM-u u više koraka na skalabilniji način.

Ovaj tečaj podijeljen je po nekim od trenutno popularnih agentnih obrazaca.

### Agentni okviri

Agentni okviri omogućuju programerima implementaciju agentnih obrazaca putem koda. Ti okviri nude predloške, dodatke i alate za bolju suradnju AI agenata. Ove prednosti pružaju mogućnosti za bolje nadgledanje i otklanjanje poteškoća u AI agentnim sustavima.

U ovom tečaju istraživat ćemo Microsoft Agent Framework (MAF) za izgradnju AI agenata spremnih za produkciju.

## Primjeri koda

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Imate dodatnih pitanja o AI agentima?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) da biste se povezali s drugim polaznicima, sudjelovali na uredskim satima i dobili odgovore na pitanja o AI agentima.

## Prethodna lekcija

[Postavljanje tečaja](../00-course-setup/README.md)

## Sljedeća lekcija

[Istraživanje agentnih okvira](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI prevoditeljske usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalan ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz uporabe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->