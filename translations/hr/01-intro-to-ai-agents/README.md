<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T22:56:42+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "hr"
}
-->
[![Uvod u AI agente](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.hr.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na sliku iznad za video ovog predavanja)_

# Uvod u AI agente i njihove primjene

Dobrodošli u tečaj "AI Agenti za početnike"! Ovaj tečaj pruža osnovno znanje i primjere za izradu AI agenata.

Pridružite se kako biste upoznali druge polaznike i graditelje AI agenata te postavili sva pitanja koja imate o ovom tečaju.

Za početak tečaja, prvo ćemo bolje razumjeti što su AI agenti i kako ih možemo koristiti u aplikacijama i radnim procesima koje gradimo.

## Uvod

Ova lekcija pokriva:

- Što su AI agenti i koje vrste agenata postoje?
- Koje su najbolje primjene za AI agente i kako nam mogu pomoći?
- Koji su osnovni elementi pri dizajniranju rješenja temeljenih na agentima?

## Ciljevi učenja
Nakon završetka ove lekcije, trebali biste moći:

- Razumjeti koncepte AI agenata i kako se razlikuju od drugih AI rješenja.
- Učinkovito primjenjivati AI agente.
- Produktivno dizajnirati rješenja temeljena na agentima za korisnike i klijente.

## Definiranje AI agenata i vrste AI agenata

### Što su AI agenti?

AI agenti su **sustavi** koji omogućuju **velikim jezičnim modelima (LLM-ovima)** da **izvršavaju radnje** proširujući njihove mogućnosti davanjem pristupa **alatima** i **znanju**.

Razložimo ovu definiciju na manje dijelove:

- **Sustav** - Važno je razmišljati o agentima ne kao o jednom komponentu, već kao o sustavu mnogih komponenti. Na osnovnoj razini, komponente AI agenta su:
  - **Okruženje** - Definirani prostor u kojem AI agent djeluje. Na primjer, ako imamo AI agenta za rezervaciju putovanja, okruženje bi moglo biti sustav za rezervaciju putovanja koji agent koristi za obavljanje zadataka.
  - **Senzori** - Okruženja imaju informacije i pružaju povratne informacije. AI agenti koriste senzore za prikupljanje i tumačenje tih informacija o trenutnom stanju okruženja. U primjeru agenta za rezervaciju putovanja, sustav za rezervaciju može pružiti informacije poput dostupnosti hotela ili cijena letova.
  - **Aktuatori** - Nakon što AI agent primi informacije o trenutnom stanju okruženja, određuje koju radnju treba poduzeti kako bi promijenio okruženje. Za agenta za rezervaciju putovanja, to bi moglo biti rezerviranje dostupne sobe za korisnika.

![Što su AI agenti?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.hr.png)

**Veliki jezični modeli** - Koncept agenata postojao je i prije stvaranja LLM-ova. Prednost izgradnje AI agenata s LLM-ovima je njihova sposobnost tumačenja ljudskog jezika i podataka. Ta sposobnost omogućuje LLM-ovima da tumače informacije iz okruženja i definiraju plan za promjenu okruženja.

**Izvršavanje radnji** - Izvan sustava AI agenata, LLM-ovi su ograničeni na situacije u kojima je radnja generiranje sadržaja ili informacija na temelju korisničkog upita. Unutar sustava AI agenata, LLM-ovi mogu izvršavati zadatke tumačenjem korisničkog zahtjeva i korištenjem alata dostupnih u njihovom okruženju.

**Pristup alatima** - Koji alati su dostupni LLM-u definirano je 1) okruženjem u kojem djeluje i 2) programerom AI agenta. U našem primjeru agenta za putovanja, alati agenta ograničeni su operacijama dostupnim u sustavu za rezervaciju, a/ili programer može ograničiti pristup alata na letove.

**Memorija + Znanje** - Memorija može biti kratkoročna u kontekstu razgovora između korisnika i agenta. Dugoročno, izvan informacija koje pruža okruženje, AI agenti mogu također dohvaćati znanje iz drugih sustava, usluga, alata, pa čak i drugih agenata. U primjeru agenta za putovanja, to znanje može biti informacija o korisnikovim preferencijama putovanja pohranjenim u bazi podataka klijenata.

### Različite vrste agenata

Sada kada imamo opću definiciju AI agenata, pogledajmo neke specifične vrste agenata i kako bi se primijenili na AI agenta za rezervaciju putovanja.

| **Vrsta agenta**              | **Opis**                                                                                                                             | **Primjer**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agenti s jednostavnim refleksom** | Izvršavaju trenutne radnje na temelju unaprijed definiranih pravila.                                                                 | Agent za putovanja tumači kontekst e-pošte i prosljeđuje pritužbe na putovanja korisničkoj službi.                                                                                                                          |
| **Agenti s modelom refleksa** | Izvršavaju radnje na temelju modela svijeta i promjena tog modela.                                                                     | Agent za putovanja daje prioritet rutama s značajnim promjenama cijena na temelju pristupa povijesnim podacima o cijenama.                                                                                                   |
| **Agenti temeljeni na ciljevima** | Kreiraju planove za postizanje specifičnih ciljeva tumačenjem cilja i određivanjem radnji za njegovo postizanje.                     | Agent za putovanja rezervira putovanje određivanjem potrebnih aranžmana (auto, javni prijevoz, letovi) od trenutne lokacije do odredišta.                                                                                     |
| **Agenti temeljeni na korisnosti** | Razmatraju preferencije i numerički vagaju kompromise kako bi odredili kako postići ciljeve.                                         | Agent za putovanja maksimizira korisnost vaganjem praktičnosti naspram troškova prilikom rezervacije putovanja.                                                                                                              |
| **Agenti koji uče**           | Poboljšavaju se s vremenom odgovarajući na povratne informacije i prilagođavajući radnje.                                              | Agent za putovanja poboljšava se koristeći povratne informacije korisnika iz anketa nakon putovanja kako bi prilagodio buduće rezervacije.                                                                                   |
| **Hijerarhijski agenti**      | Imaju više agenata u sustavu s više razina, pri čemu agenti viših razina dijele zadatke na podzadatke koje izvršavaju agenti nižih razina. | Agent za putovanja otkazuje putovanje dijeleći zadatak na podzadatke (npr. otkazivanje specifičnih rezervacija) koje izvršavaju agenti nižih razina, a zatim izvještavaju agenta više razine.                                   |
| **Sustavi s više agenata (MAS)** | Agenti samostalno izvršavaju zadatke, bilo suradnički ili natjecateljski.                                                             | Suradnički: Više agenata rezervira specifične usluge putovanja poput hotela, letova i zabave. Natjecateljski: Više agenata upravlja i natječe se za zajednički kalendar rezervacija hotela kako bi rezervirali goste u hotelu. |

## Kada koristiti AI agente

U prethodnom dijelu koristili smo primjer agenta za putovanja kako bismo objasnili kako se različite vrste agenata mogu koristiti u različitim scenarijima rezervacije putovanja. Nastavit ćemo koristiti ovu aplikaciju tijekom tečaja.

Pogledajmo vrste slučajeva upotrebe za koje su AI agenti najprikladniji:

![Kada koristiti AI agente?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.hr.png)

- **Problemi otvorenog tipa** - omogućavanje LLM-u da odredi potrebne korake za dovršavanje zadatka jer se oni ne mogu uvijek unaprijed definirati u radnom procesu.
- **Procesi s više koraka** - zadaci koji zahtijevaju određenu razinu složenosti pri kojoj AI agent mora koristiti alate ili informacije tijekom više koraka, a ne samo u jednom pokušaju.
- **Poboljšanje s vremenom** - zadaci kod kojih se agent može poboljšati s vremenom primajući povratne informacije iz okruženja ili od korisnika kako bi pružio bolju korisnost.

Više o razmatranjima korištenja AI agenata pokrivamo u lekciji o izgradnji pouzdanih AI agenata.

## Osnove rješenja temeljenih na agentima

### Razvoj agenata

Prvi korak u dizajniranju sustava AI agenta je definiranje alata, radnji i ponašanja. U ovom tečaju fokusiramo se na korištenje **Azure AI Agent Service** za definiranje naših agenata. Nudi značajke poput:

- Odabira otvorenih modela poput OpenAI, Mistral i Llama
- Korištenja licenciranih podataka putem pružatelja poput Tripadvisora
- Korištenja standardiziranih OpenAPI 3.0 alata

### Obrasci temeljeni na agentima

Komunikacija s LLM-ovima odvija se putem upita. S obzirom na poluautonomnu prirodu AI agenata, nije uvijek moguće ili potrebno ručno ponovno postavljati upit LLM-u nakon promjene u okruženju. Koristimo **obrasce temeljene na agentima** koji nam omogućuju postavljanje upita LLM-u tijekom više koraka na skalabilniji način.

Ovaj tečaj podijeljen je na neke od trenutno popularnih obrazaca temeljenih na agentima.

### Okviri temeljeni na agentima

Okviri temeljeni na agentima omogućuju programerima implementaciju obrazaca temeljenih na agentima putem koda. Ovi okviri nude predloške, dodatke i alate za bolju suradnju AI agenata. Ove prednosti omogućuju bolju preglednost i otklanjanje poteškoća u sustavima AI agenata.

U ovom tečaju istražit ćemo istraživački vođen AutoGen okvir i produkcijski spreman Agent okvir iz Semantic Kernel-a.

### Imate još pitanja o AI agentima?

Pridružite se [Azure AI Foundry Discordu](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim polaznicima, sudjelovali u uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Prethodna lekcija

[Postavljanje tečaja](../00-course-setup/README.md)

## Sljedeća lekcija

[Istraživanje okvira temeljenih na agentima](../02-explore-agentic-frameworks/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje mogu proizaći iz korištenja ovog prijevoda.