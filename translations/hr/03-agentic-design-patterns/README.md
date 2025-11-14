<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c46e4ff9e349c521e2b0b17f51afa64",
  "translation_date": "2025-08-29T23:07:23+00:00",
  "source_file": "03-agentic-design-patterns/README.md",
  "language_code": "hr"
}
-->
[![Kako dizajnirati dobre AI agente](../../../translated_images/lesson-3-thumbnail.1092dd7a8f1074a5b26e35aa8f810814e05a22fed1765c20c14b2b508c7ae379.hr.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite na sliku iznad za video lekcije)_
# Principi dizajna AI agenata

## Uvod

Postoji mnogo načina razmišljanja o izgradnji sustava AI agenata. S obzirom na to da je nejasnoća značajka, a ne greška u dizajnu generativne umjetne inteligencije, inženjerima je ponekad teško odrediti odakle početi. Stvorili smo skup principa dizajna usmjerenih na korisnika kako bismo omogućili programerima da izgrade sustave agenata usmjerene na korisnike za rješavanje njihovih poslovnih potreba. Ovi principi dizajna nisu propisana arhitektura, već početna točka za timove koji definiraju i razvijaju iskustva s agentima.

Općenito, agenti bi trebali:

- Proširiti i povećati ljudske sposobnosti (brainstorming, rješavanje problema, automatizacija itd.)
- Popuniti praznine u znanju (upoznavanje s novim područjima znanja, prijevod itd.)
- Omogućiti i podržati suradnju na način na koji pojedinci preferiraju raditi s drugima
- Učiniti nas boljim verzijama sebe (npr. životni trener/organizator zadataka, pomoć u učenju emocionalne regulacije i vještina svjesnosti, izgradnja otpornosti itd.)

## Ova lekcija obuhvaća

- Što su principi dizajna agenata
- Koje smjernice slijediti prilikom implementacije ovih principa dizajna
- Primjere korištenja principa dizajna

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

1. Objasniti što su principi dizajna agenata
2. Objasniti smjernice za korištenje principa dizajna agenata
3. Razumjeti kako izgraditi agenta koristeći principe dizajna agenata

## Principi dizajna agenata

![Principi dizajna agenata](../../../translated_images/agentic-design-principles.1cfdf8b6d3cc73c2b738951ee7b2043e224441d98babcf654be69d866120f93a.hr.png)

### Agent (Prostor)

Ovo je okruženje u kojem agent djeluje. Ovi principi informiraju kako dizajniramo agente za interakciju u fizičkim i digitalnim svjetovima.

- **Povezivanje, ne zamjena** – pomoći povezati ljude s drugim ljudima, događajima i korisnim znanjem kako bi se omogućila suradnja i povezivanje.
- Agenti pomažu povezati događaje, znanje i ljude.
- Agenti približavaju ljude jedne drugima. Nisu dizajnirani da zamijene ili umanje ljude.
- **Lako dostupni, ali povremeno nevidljivi** – agent uglavnom djeluje u pozadini i samo nas potiče kada je to relevantno i prikladno.
  - Agent je lako otkriti i dostupan je ovlaštenim korisnicima na bilo kojem uređaju ili platformi.
  - Agent podržava multimodalne ulaze i izlaze (zvuk, glas, tekst itd.).
  - Agent može neprimjetno prelaziti između prednjeg i stražnjeg plana; između proaktivnog i reaktivnog, ovisno o potrebama korisnika.
  - Agent može djelovati u nevidljivom obliku, ali njegov proces u pozadini i suradnja s drugim agentima su transparentni i pod kontrolom korisnika.

### Agent (Vrijeme)

Ovo je način na koji agent djeluje tijekom vremena. Ovi principi informiraju kako dizajniramo agente koji interagiraju kroz prošlost, sadašnjost i budućnost.

- **Prošlost**: Refleksija na povijest koja uključuje stanje i kontekst.
  - Agent pruža relevantnije rezultate na temelju analize bogatijih povijesnih podataka, ne samo događaja, ljudi ili stanja.
  - Agent stvara poveznice iz prošlih događaja i aktivno reflektira na memoriju kako bi se angažirao u trenutnim situacijama.
- **Sadašnjost**: Poticaj više nego obavijest.
  - Agent utjelovljuje sveobuhvatan pristup interakciji s ljudima. Kada se dogodi događaj, agent ide dalje od statične obavijesti ili druge statične formalnosti. Agent može pojednostaviti tokove ili dinamički generirati znakove za usmjeravanje korisnikove pažnje u pravom trenutku.
  - Agent pruža informacije na temelju kontekstualnog okruženja, društvenih i kulturnih promjena te prilagođene korisničkoj namjeri.
  - Interakcija s agentom može biti postupna, evoluirajući/rastući u složenosti kako bi osnažila korisnike dugoročno.
- **Budućnost**: Prilagodba i evolucija.
  - Agent se prilagođava različitim uređajima, platformama i modalitetima.
  - Agent se prilagođava ponašanju korisnika, potrebama pristupačnosti i slobodno je prilagodljiv.
  - Agent se oblikuje i evoluira kroz kontinuiranu interakciju s korisnikom.

### Agent (Jezgra)

Ovo su ključni elementi u jezgri dizajna agenta.

- **Prihvatite neizvjesnost, ali uspostavite povjerenje**.
  - Određena razina neizvjesnosti agenta je očekivana. Neizvjesnost je ključni element dizajna agenta.
  - Povjerenje i transparentnost su temeljni slojevi dizajna agenta.
  - Ljudi kontroliraju kada je agent uključen/isključen, a status agenta je jasno vidljiv u svakom trenutku.

## Smjernice za implementaciju ovih principa

Kada koristite prethodne principe dizajna, koristite sljedeće smjernice:

1. **Transparentnost**: Informirajte korisnika da je AI uključen, kako funkcionira (uključujući prošle radnje) i kako dati povratne informacije te modificirati sustav.
2. **Kontrola**: Omogućite korisniku da prilagodi, specificira preferencije i personalizira te ima kontrolu nad sustavom i njegovim atributima (uključujući mogućnost zaborava).
3. **Dosljednost**: Ciljajte na dosljedna, multimodalna iskustva na različitim uređajima i krajnjim točkama. Koristite poznate UI/UX elemente gdje je to moguće (npr. ikona mikrofona za glasovnu interakciju) i smanjite kognitivno opterećenje korisnika što je više moguće (npr. ciljate na sažete odgovore, vizualne pomoći i sadržaj "Saznajte više").

## Kako dizajnirati putničkog agenta koristeći ove principe i smjernice

Zamislite da dizajnirate putničkog agenta, evo kako biste mogli razmišljati o korištenju principa dizajna i smjernica:

1. **Transparentnost** – Obavijestite korisnika da je putnički agent AI-enabled agent. Pružite osnovne upute o tome kako započeti (npr. poruka "Pozdrav", uzorci upita). Jasno dokumentirajte ovo na stranici proizvoda. Prikažite popis upita koje je korisnik postavio u prošlosti. Jasno naznačite kako dati povratne informacije (palac gore i dolje, gumb Pošalji povratne informacije itd.). Jasno artikulirajte ima li agent ograničenja u korištenju ili temama.
2. **Kontrola** – Pobrinite se da je jasno kako korisnik može modificirati agenta nakon što je stvoren, s opcijama poput sistemskog upita. Omogućite korisniku da odabere koliko će agent biti opširan, njegov stil pisanja i sve ograničenja o čemu agent ne bi trebao govoriti. Dopustite korisniku da pregleda i izbriše sve povezane datoteke ili podatke, upite i prošle razgovore.
3. **Dosljednost** – Pobrinite se da su ikone za dijeljenje upita, dodavanje datoteke ili fotografije te označavanje nekoga ili nečega standardne i prepoznatljive. Koristite ikonu spajalice za označavanje prijenosa/dijeljenja datoteka s agentom, te ikonu slike za označavanje prijenosa grafike.

### Imate li još pitanja o uzorcima dizajna AI agenata?

Pridružite se [Azure AI Foundry Discordu](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

## Prethodna lekcija

[Istrazivanje okvira za agente](../02-explore-agentic-frameworks/README.md)

## Sljedeća lekcija

[Uzorak dizajna za korištenje alata](../04-tool-use/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.