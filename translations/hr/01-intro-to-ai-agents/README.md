[![Uvod u AI agente](../../../translated_images/hr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite sliku gore za gledanje videa za ovu lekciju)_

# Uvod u AI agente i primjene agenata

Dobrodošli u tečaj **AI Agenti za početnike**! Ovaj tečaj pruža vam osnovno znanje — i stvarni radni kod — da biste počeli graditi AI agente ispočetka.

Dođite pozdraviti se u <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord zajednicu</a> — puna je učenika i tvoraca AI-ja koji rado odgovaraju na pitanja.

Prije nego što počnemo graditi, hajdemo se uvjeriti da zaista razumijemo što je AI agent *i* kada ima smisla koristiti ga.

---

## Uvod

Ova lekcija obuhvaća:

- Što su AI agenti, i koji različiti tipovi postoje
- Koje vrste zadataka su AI agentima najbolje za izvršavanje
- Osnovne gradivne blokove koje ćete koristiti prilikom dizajniranja agentskog rješenja

## Ciljevi učenja

Na kraju ove lekcije, trebali biste moći:

- Objasniti što je AI agent i kako se razlikuje od običnog AI rješenja
- Znati kada se treba osloniti na AI agenta (a kada ne)
- Nacrtati osnovni dizajn agentskog rješenja za stvarni problem

---

## Definiranje AI agenata i tipovi AI agenata

### Što su AI agenti?

Evo jednostavan način razmišljanja o tome:

> **AI agenti su sustavi koji omogućuju velikim jezičnim modelima (LLM-ovima) da zapravo *nešto rade* — daju im alate i znanje za djelovanje u svijetu, a ne samo odgovaranje na upite.**

Razložimo to malo:

- **Sustav** — AI agent nije samo jedna stvar. To je skup dijelova koji rade zajedno. U svojoj srži, svaki agent ima tri dijela:
  - **Okruženje** — Prostor u kojem agent radi. Za agenta za rezervaciju putovanja to bi bila sama platforma za rezervacije.
  - **Senzori** — Kako agent čita trenutačno stanje svog okruženja. Naš agent za putovanja može provjeravati dostupnost hotela ili cijene letova.
  - **Aktuatori** — Kako agent poduzima radnje. Agent za putovanja može rezervirati sobu, poslati potvrdu ili otkazati rezervaciju.

![Što su AI agenti?](../../../translated_images/hr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veliki jezični modeli** — Agentima su postojali prije LLM-ova, ali LLM-ovi su ono što današnje agente čini tako moćnima. Oni mogu razumjeti prirodni jezik, rasuđivati o kontekstu i pretvoriti nejasan korisnički zahtjev u konkretan plan djelovanja.

- **Izvršavaju radnje** — Bez agentskog sustava, LLM samo generira tekst. Unutar agentskog sustava, LLM zapravo može *izvesti* korake — pretražiti bazu podataka, pozvati API, poslati poruku.

- **Pristup alatima** — Koje alate agent može koristiti ovisi o (1) okruženju u kojem radi i (2) što mu je developer odlučio dati. Agent za putovanja može moći tražiti letove, ali ne i uređivati podatke o kupcima — sve ovisi o tome što povežete.

- **Memorija + znanje** — Agenti mogu imati kratkoročnu memoriju (trenutni razgovor) i dugoročnu memoriju (baza podataka kupaca, prošle interakcije). Agent za putovanja može "zapamtiti" da preferirate sjedala uz prozor.

---

### Različite vrste AI agenata

Nisu svi agenti izgrađeni na isti način. Evo pregleda glavnih vrsta, koristeći agenta za rezervaciju putovanja kao primjer:

| **Vrsta agenta** | **Što radi** | **Primjer agenta za putovanja** |
|---|---|---|
| **Jednostavni refleksni agenti** | Slijede unaprijed zadana pravila — nema memorije, nema planiranja. | Vidi žalbu u e-pošti → prosljeđuje je službi za korisnike. To je to. |
| **Agenti zasnovani na modelu** | Drže unutarnji model svijeta i ažuriraju ga kako se stvari mijenjaju. | Prati povijesne cijene letova i označava rute koje su odjednom skupe. |
| **Agenti s ciljem** | Imaju cilj i korak po korak pronalaze način da ga postignu. | Rezervira cijelo putovanje (letove, auto, hotel) počevši od vaše trenutne lokacije do odredišta. |
| **Agenti usmjereni na korisnost** | Ne pronalaze samo *neko* rješenje — pronalaze *najbolje* uz vaganje kompromisa. | Izbalansira troškove i pogodnost da bi našao putovanje koje najbolje odgovara vašim željama. |
| **Učeći agenti** | Postaju bolji s vremenom učeći iz povratnih informacija. | Prilagođava buduće preporuke za rezervacije bazirane na anketama nakon putovanja. |
| **Hijerarhijski agenti** | Visokorazinski agent razbija posao na podzadatke i delegira nižerazinskim agentima. | Zahtjev "otkaži putovanje" dijeli se na: otkaži let, otkaži hotel, otkaži najam auta — svaki obavlja pod-agent. |
| **Sustavi s više agenata (MAS)** | Više neovisnih agenata koji rade zajedno (ili se natječu). | Suradnički: zasebni agenti upravljaju hotelima, letovima i zabavom. Natjecateljski: više agenata se natječu za popunjavanje hotelskih soba po najboljoj cijeni. |

---

## Kada koristiti AI agente

Samo zato što *možete* koristiti AI agenta, ne znači da biste to uvijek *trebali*. Evo situacija u kojima agenti doista briljiraju:

![Kada koristiti AI agente?](../../../translated_images/hr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemi bez jasno definiranih koraka** — Kad se koraci za rješavanje problema ne mogu unaprijed programirati. Trebate da LLM dinamički pronađe put.
- **Višekorakni procesi** — Zadatci koji zahtijevaju korištenje alata kroz više koraka, a ne samo jednostavno pretraživanje ili generiranje.
- **Poboljšanje tijekom vremena** — Kad želite da sustav postane pametniji na temelju povratnih informacija korisnika ili signala iz okoline.

Detaljnije ćemo istražiti kada (a kada *ne*) koristiti AI agente u lekciji **Izgradnja pouzdanih AI agenata** kasnije u tečaju.

---

## Osnove agentskih rješenja

### Razvoj agenta

Prvo što radite kod izrade agenta jest definirati *što može raditi* — njegove alate, radnje i ponašanja.

U ovom tečaju koristimo **Microsoft Foundry Agent Service** kao našu glavnu platformu. Ona podržava:

- Modele od pružatelja poput OpenAI, Mistral i Meta (Llama)
- Licencirane podatke od pružatelja poput Tripadvisor
- Standardizirane OpenAPI 3.0 definicije alata

### Agentski obrasci

Komunicirate s LLM-ovima putem upita (promptova). S agentima ne možete uvijek ručno izrađivati svaki upit — agent mora djelovati kroz više koraka. Tu na scenu stupaju **agentski obrasci**. To su višekratno upotrebljive strategije za promptanje i usklađivanje LLM-ova na skalabilniji, pouzdaniji način.

Ovaj je tečaj strukturiran oko najčešćih i najkorisnijih agentskih obrazaca.

### Agentski okviri

Agentski okviri daju developerima gotove predloške, alate i infrastrukturu za izgradnju agenata. Olakšavaju:

- Povezivanje alata i sposobnosti
- Praćenje što agent radi (i otklanjanje grešaka kad nešto pođe po zlu)
- Suradnju između više agenata

U ovom tečaju fokusiramo se na **Microsoft Agent Framework (MAF)** za izgradnju agenata spremnih za produkciju.

---

## Primjeri koda

Spremni za vidjeti to u akciji? Evo primjera koda za ovu lekciju:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate pitanja?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) kako biste se povezali s drugim učenicima, sudjelovali u radnim satima i dobili odgovore na pitanja o AI agentima od zajednice.


---

## Testiranje agenta (neobavezno)

Nakon što naučite kako implementirati agente u [Lekcija 16](../16-deploying-scalable-agents/README.md), možete dodati brzu provjeru ispravnosti nakon implementacije za ovogodišnji `TravelAgent` koristeći gotovu katalog datoteku [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Pogledajte [`tests/README.md`](../tests/README.md) za upute kako pokrenuti test.

---

## Prethodna lekcija

[Postavljanje tečaja](../00-course-setup/README.md)

## Sljedeća lekcija

[Istraživanje agentskih okvira](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->