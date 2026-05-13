[![Intro to AI Agents](../../../translated_images/hr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na sliku iznad da pogledate video za ovu lekciju)_

# Uvod u AI agente i primjene agenata

Dobrodošli na tečaj **AI Agent za početnike**! Ovaj tečaj pruža vam temeljnija znanja — i stvarni radni kod — za početak izrade AI agenata od nule.

Dođite pozdraviti se u <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord zajednicu</a> — puna je učenika i graditelja AI-ja koji rado odgovaraju na pitanja.

Prije nego što počnemo graditi, pobrinimo se da stvarno razumijemo što je AI agent *i* kada ima smisla koristiti ga.

---

## Uvod

Ova lekcija pokriva:

- Što su AI agenti i koje vrste postoje
- Za koje vrste zadataka su AI agenti najprikladniji
- Osnovne gradivne blokove koje ćete koristiti pri dizajniranju Agentnog rješenja

## Ciljevi učenja

Do kraja ove lekcije trebali biste biti u mogućnosti:

- Objasniti što je AI agent i kako se razlikuje od običnog AI rješenja
- Znati kada posegnuti za AI agentom (a kada ne)
- Nacrtati osnovni dizajn Agentnog rješenja za stvarni problem

---

## Definiranje AI agenata i vrste AI agenata

### Što su AI agenti?

Evo jednostavan način da to shvatite:

> **AI agenti su sustavi koji omogućuju velikim jezičnim modelima (LLM-ovima) da zapravo *rade stvari* — dajući im alate i znanje za djelovanje u svijetu, a ne samo za odgovaranje na upite.**

Razložimo to malo:

- **Sustav** — AI agent nije samo jedna stvar. To je skup dijelova koji rade zajedno. U svojoj srži, svaki agent ima tri elementa:
  - **Okruženje** — prostor u kojem agent djeluje. Za agenta za rezervaciju putovanja, to bi bila sama platforma za rezervaciju.
  - **Senzori** — kako agent čita trenutačno stanje okruženja. Naš agent za putovanja mogao bi provjeravati dostupnost hotela ili cijene letova.
  - **Aktuatori** — kako agent poduzima akciju. Agent za putovanja mogao bi rezervirati sobu, poslati potvrdu ili otkazati rezervaciju.

![Što su AI agenti?](../../../translated_images/hr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veliki jezični modeli** — Agenti su postojali i prije LLM-ova, ali LLM-ovi su ono što današnje agente čini moćnima. Mogu razumjeti prirodni jezik, rezonirati o kontekstu i pretvoriti nejasan korisnički zahtjev u konkretan plan djelovanja.

- **Izvršavanje radnji** — Bez agentnog sustava, LLM samo generira tekst. Unutar agentnog sustava, LLM zapravo može *izvršavati* korake — pretraživati bazu podataka, pozivati API, slati poruke.

- **Pristup alatima** — Koje alate agent može koristiti ovisi o (1) okruženju u kojem radi i (2) što mu programer odluči dati. Agent za putovanja može moći tražiti letove, ali ne uređivati zapise o kupcima — sve ovisi o povezivanju.

- **Memorija + Znanje** — Agent može imati kratkoročnu memoriju (trenutni razgovor) i dugoročnu memoriju (bazu podataka kupaca, prošle interakcije). Agent za putovanja može "zapamtiti" da preferirate sjedala uz prozor.

---

### Različite vrste AI agenata

Nisu svi agenti građeni isto. Evo podjela glavnih vrsta, koristeći agenta za rezervaciju putovanja kao primjernog agenta:

| **Vrsta agenta** | **Što radi** | **Primjer agenta za putovanja** |
|---|---|---|
| **Jednostavni refleksni agenti** | Prate unaprijed zadana pravila — bez memorije, bez planiranja. | Vidjet će žalbu u e-mailu → proslijedit će je službi za korisnike. To je to. |
| **Model-temeljeni refleksni agenti** | Drže unutarnji model svijeta i ažuriraju ga kad se stvari mijenjaju. | Prate povijesne cijene letova i označavaju rute koje su iznenada skupe. |
| **Agent s ciljem** | Ima cilj i korak po korak pronalazi kako ga postići. | Rezervira cijelo putovanje (letove, auto, hotel) od vaše trenutačne lokacije do cilja. |
| **Agent s korisničkom funkcijom** | Ne pronalazi samo *rješenje* — pronalazi *najbolje* rješenje balansirajući kompromise. | Uravnotežuje troškove i praktičnost da pronađe putovanje koje najviše odgovara vašim preferencijama. |
| **Agent za učenje** | Poboljšava se s vremenom učeći iz povratnih informacija. | Prilagođava buduće preporuke za rezervacije na temelju rezultata anketa nakon putovanja. |
| **Hijerarhijski agenti** | Visoki agent dijeli posao na podzadatke i delegira ih agentima nižeg nivoa. | Zahtjev za "otkazivanje putovanja" dijeli se na: otkazivanje leta, otkazivanje hotela, otkazivanje najma auta — svaki dodiijeljen pod-agentu. |
| **Sustavi s više agenata (MAS)** | Više neovisnih agenata koji surađuju (ili konkuriraju). | Kooperativno: zasebni agenti upravljaju hotelima, letovima i zabavom. Konkurentski: više agenata natječe se za popunjavanje hotelskih soba po najboljoj cijeni. |

---

## Kada koristiti AI agente

Samo zato što *možete* koristiti AI agenta, ne znači da biste uvijek *trebali*. Evo situacija u kojima agenti zaista dolaze do izražaja:

![Kada koristiti AI agente?](../../../translated_images/hr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvoreni problemi** — Kad se koraci za rješavanje problema ne mogu unaprijed programirati. Trebate da LLM sam dinamički pronađe put.
- **Višestepeni procesi** — Zadatci koji zahtijevaju korištenje alata kroz više koraka, a ne samo jedno pretraživanje ili generiranje.
- **Poboljšanje kroz vrijeme** — Kad želite da sustav postaje pametniji na temelju povratnih informacija korisnika ili signala iz okoline.

Detaljnije ćemo razmotriti kada (i kada *ne*) koristiti AI agente u lekciji **Izgradnja pouzdanih AI agenata** kasnije u tečaju.

---

## Osnove agentnih rješenja

### Razvoj agenta

Prvo što radite pri izradi agenta je definirati *što može raditi* — njegove alate, radnje i ponašanja.

U ovom tečaju koristimo **Azure AI Agent Service** kao našu glavnu platformu. Podržava:

- Modele od pružatelja kao što su OpenAI, Mistral i Meta (Llama)
- Licencirane podatke od pružatelja kao što je Tripadvisor
- Standardizirane OpenAPI 3.0 definicije alata

### Agentni obrasci

Komunicirate s LLM-ovima pomoću upita (prompta). Kod agenata ne možete uvijek ručno izrađivati svaki upit — agent treba poduzimati akcije kroz mnoge korake. Tu dolaze **Agentni obrasci**. To su ponovo iskoristive strategije za promptanje i usklađivanje LLM-ova na skalabilniji i pouzdaniji način.

Ovaj tečaj je strukturiran oko najčešćih i najkorisnijih agentnih obrazaca.

### Agentni okviri

Agentni okviri daju programerima gotove predloške, alate i infrastrukturu za izgradnju agenata. Olakšavaju:

- Povezivanje alata i mogućnosti
- Promatranje što agent radi (i otklanjanje pogrešaka kad nešto pođe po zlu)
- Suradnju među više agenata

U ovom tečaju fokusiramo se na **Microsoft Agent Framework (MAF)** za izradu agenata spremnih za produkciju.

---

## Primjeri koda

Spremni vidjeti to u praksi? Evo primjera koda za ovu lekciju:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate pitanja?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) da se povežete s drugim učenicima, sudjelujete u uredskim satima i dobijete odgovore na pitanja o AI agentima iz zajednice.

---

## Prethodna lekcija

[Course Setup](../00-course-setup/README.md)

## Sljedeća lekcija

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->