[![Uvod u AI agente](../../../translated_images/hr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite gornju sliku za pregled videa za ovu lekciju)_

# Uvod u AI agente i primjenu agenata

Dobrodošli u tečaj **AI agenti za početnike**! Ovaj tečaj daje vam temeljno znanje — i pravi radni kod — za početak izgradnje AI agenata od nule.

Dođite i pozdravite se u <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord zajednici</a> — puna je učenika i AI kreatora koji rado odgovaraju na pitanja.

Prije nego što krenemo s izgradnjom, hajde da se uvjerimo da zaista razumijemo što je AI agent i kada ima smisla koristiti ga.

---

## Uvod

Ova lekcija obuhvaća:

- Što su AI agenti i koje vrste postoje
- Za kakve vrste zadataka su AI agenti najbolje prilagođeni
- Temeljne gradivne blokove koje ćete koristiti pri dizajniranju agencijskog rješenja

## Ciljevi učenja

Na kraju ove lekcije, trebali biste moći:

- Objasniti što je AI agent i kako se razlikuje od običnog AI rješenja
- Znati kada posegnuti za AI agentom (a kada ne)
- Skicirati osnovni dizajn agencijskog rješenja za stvarni problem

---

## Definiranje AI agenata i vrste AI agenata

### Što su AI agenti?

Evo jednostavan način razmišljanja o tome:

> **AI agenti su sustavi koji omogućuju Velikim jezičnim modelima (LLM-ovima) da zapravo *čine stvari* — daju im alate i znanje da djeluju na svijet, a ne samo da odgovaraju na upite.**

Razmotrimo to detaljnije:

- **Sustav** — AI agent nije samo jedna stvar. To je skup dijelova koji rade zajedno. U svojoj osnovi, svaki agent ima tri dijela:
  - **Okruženje** — Prostor u kojem agent djeluje. Za agenta za rezervaciju putovanja, to bi bila sama platforma za rezervacije.
  - **Senzori** — Kako agent čita trenutačno stanje svog okruženja. Naš agent za putovanja može provjeravati dostupnost hotela ili cijene leta.
  - **Aktuatori** — Kako agent poduzima radnje. Agent za putovanja može rezervirati sobu, poslati potvrdu ili otkazati rezervaciju.

![Što su AI agenti?](../../../translated_images/hr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veliki jezični modeli** — Agenti su postojali i prije LLM-ova, ali LLM-ovi su ono što moderne agente čini tako moćnima. Oni razumiju prirodni jezik, rezoniraju o kontekstu i pretvaraju nejasan korisnički zahtjev u konkretan plan djelovanja.

- **Izvođenje akcija** — Bez sustava agenata, LLM samo generira tekst. Unutar sustava agenata, LLM može zapravo *izvesti* korake — pretraživati bazu podataka, pozvati API, poslati poruku.

- **Pristup alatima** — Koje alate agent može koristiti ovisi o (1) okruženju u kojem radi i (2) što mu je razvojni inženjer omogućio. Agent za putovanja možda može pretraživati letove, ali ne može uređivati zapise korisnika — sve ovisi o tome kako ga povežete.

- **Memorija + znanje** — Agenti mogu imati kratkotrajnu memoriju (trenutni razgovor) i dugotrajnu memoriju (baza podataka korisnika, prošle interakcije). Agent za putovanja može "pamtiti" da preferirate sjedala uz prozor.

---

### Različite vrste AI agenata

Nisu svi agenti jednako građeni. Evo prikaza glavnih vrsta, koristeći agenta za rezervaciju putovanja kao primjer:

| **Vrsta agenta** | **Što radi** | **Primjer agenta za putovanja** |
|---|---|---|
| **Agenti sa jednostavnim refleksom** | Prate unaprijed definirana pravila — bez memorije, bez planiranja. | Vidi pritužbu u e-mailu → prosljeđuje je službi za korisnike. To je to. |
| **Refleksni agenti s modelom** | Drže internu mapu svijeta i ažuriraju ju kako se stvari mijenjaju. | Prate povijesne cijene letova i označavaju rute koje su iznenada skupe. |
| **Agenti usmjereni na cilj** | Imaju cilj i otkrivaju kako ga korak po korak dostići. | Rezerviraju kompletno putovanje (letove, auto, hotel) od vaše trenutne lokacije do odredišta. |
| **Agenti usmjereni na korisnost** | Ne pronalaze samo *rješenje* — pronalaze *najbolje* rješenje procjenjujući kompromise. | Ponderira cijenu i praktičnost kako bi pronašao putovanje koje najbolje odgovara vašim preferencijama. |
| **Agent učenja** | Postaje bolji tijekom vremena učeći iz povratnih informacija. | Prilagođava buduće preporuke za rezervaciju temeljem ankete nakon putovanja. |
| **Hijerarhijski agenti** | Visoko rangirani agent dijeli posao na podzadatke i delegira ih nižim agentima. | Zahtjev "otkaži putovanje" dijeli se na: otkazivanje leta, hotela, najma auta — svaki dio obrađuje pod-agent. |
| **Sustavi više agenata (MAS)** | Više neovisnih agenata koji rade zajedno (ili se natječu). | Kooperativno: zasebni agenti upravljaju hotelima, letovima i zabavom. Natjecateljski: više agenata natječu se za popunjavanje hotelskih soba po najboljoj cijeni. |

---

## Kada koristiti AI agente

Samo zato što *možete* koristiti AI agenta ne znači da uvijek *trebate*. Evo situacija u kojima agenti zaista briljiraju:

![Kada koristiti AI agente?](../../../translated_images/hr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvoreni problemi** — Kada koraci za rješavanje problema ne mogu biti unaprijed programirani. Potreban vam je LLM da dinamički utvrdi put.
- **Višekoračni procesi** — Zadatci koji zahtijevaju korištenje alata kroz više faza, ne samo jednokratno pretraživanje ili generiranje.
- **Poboljšanje tijekom vremena** — Kada želite da sustav postaje pametniji na temelju povratnih informacija korisnika ili signala iz okruženja.

Detaljnije ćemo istražiti kada (i kada *ne*) koristiti AI agente u lekciji **Izgradnja pouzdanih AI agenata** kasnije tijekom tečaja.

---

## Osnove agencijskih rješenja

### Razvoj agenta

Prvi korak u izgradnji agenta je definirati *što može raditi* — njegove alate, radnje i ponašanja.

U ovom tečaju koristimo **Azure AI Agent Service** kao našu glavnu platformu. Podržava:

- Otvorene modele poput OpenAI, Mistral i Llama
- Licencirane podatke od pružatelja poput Tripadvisor-a
- Standardizirane definicije alata OpenAPI 3.0

### Agencijski obrasci

Komunicirate s LLM-ovima putem upita (promptova). S agentima ne možete uvijek ručno izrađivati svaki prompt — agent mora poduzimati radnje u više koraka. Tu dolaze **agencijski obrasci**. To su ponovo upotrebljive strategije za promptanje i orkestraciju LLM-ova na skalabilniji i pouzdaniji način.

Ovaj tečaj je strukturiran oko najčešćih i najkorisnijih agencijskih obrazaca.

### Agencijski okviri

Agencijski okviri daju programerima gotove predloške, alate i infrastrukturu za izgradnju agenata. Olakšavaju:

- Povezivanje alata i mogućnosti
- Praćenje što agent radi (i otklanjanje pogrešaka kada nešto ne radi)
- Suradnju među više agenata

U ovom tečaju fokusiramo se na **Microsoft Agent Framework (MAF)** za izgradnju agenata spremnih za produkciju.

---

## Primjeri koda

Spremni vidjeti kako to funkcionira? Evo primjera koda za ovu lekciju:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate pitanja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) zajednici kako biste se povezali s drugim učenicima, sudjelovali na konzultacijama i dobili odgovore na pitanja o AI agentima od zajednice.

---

## Prethodna lekcija

[Postavljanje tečaja](../00-course-setup/README.md)

## Sljedeća lekcija

[Istraživanje agencijskih okvira](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->