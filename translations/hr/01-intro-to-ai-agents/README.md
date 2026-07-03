[![Uvod u AI agente](../../../translated_images/hr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na sliku iznad da pogledate video za ovu lekciju)_

# Uvod u AI agente i primjere upotrebe agenata

Dobrodošli na tečaj **AI agenti za početnike**! Ovaj tečaj pruža vam osnovno znanje — i stvarni radni kod — za početak izgradnje AI agenata od nule.

Posjetite nas i pozdravite se u <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord zajednici</a> — puna je učenika i graditelja AI koji rado odgovaraju na pitanja.

Prije nego skočimo u izgradnju, uvjerimo se da zapravo razumijemo što je AI agent i kada ima smisla koristiti ga.

---

## Uvod

Ova lekcija pokriva:

- Što su AI agenti i različite vrste koje postoje
- Koje vrste zadataka su najbolje za AI agente
- Temeljne gradivne blokove koje ćete koristiti pri dizajniranju Agentnog rješenja

## Ciljevi učenja

Do kraja ove lekcije trebali biste moći:

- Objasniti što je AI agent i kako se razlikuje od uobičajenog AI rješenja
- Znati kada koristiti AI agenta (a kada ne)
- Skicirati osnovni dizajn Agentnog rješenja za stvarni problem

---

## Definiranje AI agenata i vrste AI agenata

### Što su AI agenti?

Evo jednostavan način za razmišljanje o tome:

> **AI agenti su sustavi koji omogućuju velikim jezičnim modelima (LLM-ovima) da zapravo *činje* nešto — dajući im alate i znanje da djeluju na svijetu, a ne samo odgovaraju na upite.**

Razjasnimo to malo:

- **Sustav** — AI agent nije samo jedna stvar. To je skup dijelova koji rade zajedno. U svojoj suštini, svaki agent ima tri dijela:
  - **Okruženje** — Prostor u kojem agent djeluje. Za turističkog agenta to bi bila sama platforma za rezervacije.
  - **Senzori** — Kako agent očitava trenutačno stanje svog okruženja. Naš turistički agent može provjeravati dostupnost hotela ili cijene letova.
  - **Aktuatori** — Kako agent poduzima radnje. Turistički agent može rezervirati sobu, poslati potvrdu ili otkazati rezervaciju.

![Što su AI agenti?](../../../translated_images/hr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veliki jezični modeli** — Agenti su postojali prije LLM-ova, ali LLM-ovi su ono što čini moderne agente tako moćnima. Oni mogu razumjeti prirodni jezik, razmišljati o kontekstu i pretvoriti nejasan korisnički zahtjev u konkretan plan djelovanja.

- **Izvođenje radnji** — Bez sustava agenta, LLM samo generira tekst. U sklopu sustava agenta, LLM može zapravo *izvršavati* korake — pretraživati bazu podataka, pozivati API, slati poruku.

- **Pristup alatima** — Koje alate agent može koristiti ovisi o (1) okruženju u kojem se izvršava i (2) što je programer odlučio dati. Turistički agent može moći pretraživati letove, ali ne i uređivati podatke o korisnicima — sve ovisi o tome što ste spojili.

- **Memorija + Znanje** — Agenti mogu imati kratkoročnu memoriju (trenutačni razgovor) i dugoročnu memoriju (baza podataka korisnika, prošle interakcije). Turistički agent može „zapamtiti“ da preferirate sjedala pokraj prozora.

---

### Različite vrste AI agenata

Nisu svi agenti jednako građeni. Evo pregleda glavnih vrsta, koristeći turističkog agenta kao primjer:

| **Vrsta agenta** | **Što radi** | **Primjer turističkog agenta** |
|---|---|---|
| **Jednostavni refleksni agenti** | Prate unaprijed definirana pravila — nema memorije, nema planiranja. | Vidio je pritužbu putem e-pošte → prosljeđuje je službi za korisnike. To je to. |
| **Model-temeljeni refleksni agenti** | Čuva unutarnji model svijeta i ažurira ga kako se stvari mijenjaju. | Prati povijesne cijene letova i označava rute koje su odjednom skupe. |
| **Agenti usmjereni na ciljeve** | Ima cilj i korak po korak pronalazi način kako ga ostvariti. | Rezervira cijelo putovanje (letove, automobil, hotel) počevši s vašeg mjesta kako bi vas odveo do odredišta. |
| **Agenti temeljeni na korisnosti** | Ne pronalazi samo *rješenje* — već *najbolje* rješenje procjenjujući kompromis. | Uravnotežuje cijenu i pogodnost kako bi pronašao putovanje koje najviše odgovara vašim preferencijama. |
| **Agenti za učenje** | Vremenom se poboljšava učenjem iz povratnih informacija. | Podešava buduće preporuke za rezervacije na temelju rezultata anketa nakon putovanja. |
| **Hijerarhijski agenti** | Agent visokog nivoa razbija posao na podzadatke i delegira nižerazrednim agentima. | Zahtjev „otkaži putovanje“ razdijeli se na: otkaži let, otkaži hotel, otkaži najam auta — svaki rješava pod-agent. |
| **Sustavi višestrukih agenata (MAS)** | Više neovisnih agenata rade zajedno (ili se natječu). | Suradnički: zasebni agenti se bave hotelima, letovima i zabavom. Natjecateljski: više agenata se natječe za popunjavanje hotelskih soba po najboljoj cijeni. |

---

## Kada koristiti AI agente

Samo zato što *možete* koristiti AI agenta, ne znači da uvijek *trebate*. Evo situacija u kojima agenti stvarno briljiraju:

![Kada koristiti AI agente?](../../../translated_images/hr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemi otvorenog tipa** — Kada se koraci za rješavanje problema ne mogu unaprijed programirati. Potreban je LLM da dinamički pronađe put.
- **Višekoraci procesi** — Zadatci koji zahtijevaju korištenje alata kroz više koraka, a ne samo jedno pretraživanje ili generiranje.
- **Poboljšanje tijekom vremena** — Kada želite da sustav postane pametniji na temelju povratnih informacija korisnika ili signala iz okoline.

Detaljnije ćemo obraditi kada (i kada *ne*) koristiti AI agente u lekciji **Izgradnja pouzdanih AI agenata** kasnije u tečaju.

---

## Osnove Agentnih rješenja

### Razvoj agenata

Prva stvar koju radite pri izgradnji agenta je definirati *što može raditi* — njegove alate, radnje i ponašanja.

U ovom tečaju koristimo **Azure AI Agent Service** kao našu glavnu platformu. Podržava:

- Modele od pružatelja kao što su OpenAI, Mistral i Meta (Llama)
- Licencirane podatke od pružatelja poput Tripadvisor
- Standardizirane definicije alata OpenAPI 3.0

### Agentni obrasci

Komunicirate s LLM-ovima pomoću upita. Kod agenata ne možete uvijek ručno izrađivati svaki upit — agent mora djelovati kroz mnoge korake. Tu dolaze **Agentni obrasci**. To su ponovo iskoristive strategije za promptiranje i orkestraciju LLM-ova na skalabilniji i pouzdaniji način.

Ovaj tečaj je strukturiran oko najčešćih i najkorisnijih agentnih obrazaca.

### Agentni okviri

Agentni okviri daju programerima gotove predloške, alate i infrastrukturu za izgradnju agenata. Olakšavaju:

- Povezivanje alata i mogućnosti
- Promatranje što agent radi (i otklanjanje pogrešaka kada nešto krene po zlu)
- Suradnju između više agenata

U ovom tečaju fokusiramo se na **Microsoft Agent Framework (MAF)** za izgradnju produkcijski spremnih agenata.

---

## Primjeri koda

Spremni za akciju? Evo primjera koda za ovu lekciju:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Imate pitanja?

Pridružite se [Microsoft Foundry Discordu](https://discord.com/invite/ATgtXmAS5D) za povezivanje s drugim učenicima, sudjelovanje u radnim satima i odgovore na pitanja o AI agentima od zajednice.


---

## Prethodna lekcija

[Postavljanje tečaja](../00-course-setup/README.md)

## Slijedeća lekcija

[Istraživanje agentnih okvira](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->