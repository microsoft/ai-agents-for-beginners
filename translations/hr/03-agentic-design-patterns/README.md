[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite na gornju sliku za pogledati video ovog poglavlja)_
# Principi dizajna AI agenata

## Uvod

Postoji mnogo načina za razmišljanje o izgradnji AI agentnih sustava. Budući da je dvosmislenost značajka, a ne greška u dizajnu generativne AI, ponekad je inženjerima teško odrediti gdje uopće početi. Stvorili smo skup principa dizajna usmjerenih na korisnika kako bismo omogućili developerima da grade agentne sustave usmjerene na korisnika za rješavanje njihovih poslovnih potreba. Ovi principi dizajna nisu propisna arhitektura, već početna točka za timove koji definiraju i razvijaju agentna iskustva.

Općenito, agenti bi trebali:

- Proširiti i skalirati ljudske sposobnosti (razmišljanje, rješavanje problema, automatizacija, itd.)
- Popuniti praznine u znanju (dovesti me do razine znanja o domenama, prijevod, itd.)
- Omogućiti i podržavati suradnju na načinima na koje kao pojedinci volimo raditi s drugima
- Učiniti nas boljim verzijama sebe samih (npr. životni trener/vođa zadataka, pomažući nam naučiti emocionalnu regulaciju i vještine pažljivosti, gradnju otpornosti, itd.)

## Ovo poglavlje pokriva

- Što su principi agentnog dizajna
- Koje smjernice slijediti prilikom implementacije ovih principa dizajna
- Neki primjeri korištenja principa dizajna

## Ciljevi učenja

Nakon dovršetka ovog poglavlja moći ćete:

1. Objasniti što su principi agentnog dizajna
2. Objasniti smjernice za korištenje principa agentnog dizajna
3. Razumjeti kako izgraditi agenta koristeći principe agentnog dizajna

## Principi agentnog dizajna

![Principi agentnog dizajna](../../../translated_images/hr/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Prostorni)

Ovo je okruženje u kojem agent djeluje. Ovi principi informiraju kako dizajniramo agente za interakciju u fizičkim i digitalnim svjetovima.

- **Povezivanje, a ne kolapsiranje** – pomažu povezati ljude s drugim ljudima, događajima i djelotvornim znanjem za omogućavanje suradnje i povezanosti.
- Agentima pomažu povezati događaje, znanje i ljude.
- Agent približava ljude jedne drugima. Nisu dizajnirani za zamjenu ili omalovažavanje ljudi.
- **Lako dostupni, a povremeno nevidljivi** – agent uglavnom djeluje u pozadini i lagano nas potiče kada je to relevantno i prikladno.
  - Agent je lako otkriven i dostupan ovlaštenim korisnicima na bilo kojem uređaju ili platformi.
  - Agent podržava višemodalne unose i izlaze (zvuk, glas, tekst, itd.).
  - Agent može neprimjetno prelaziti između prvog i drugog plana; između proaktivnog i reaktivnog, ovisno o procjeni korisničkih potreba.
  - Agent može djelovati nevidljivo, ali procesi u pozadini i suradnja s drugim agentima su pregledni i kontrolirani od strane korisnika.

### Agent (Vremenski)

Ovo je način na koji agent djeluje tijekom vremena. Ovi principi informiraju kako dizajniramo agente koji komuniciraju preko prošlosti, sadašnjosti i budućnosti.

- **Prošlost**: Promišljanje povijesti koja uključuje stanje i kontekst.
  - Agent pruža relevantnije rezultate na temelju analize bogatijih povijesnih podataka, osim samog događaja, ljudi ili stanja.
  - Agent stvara veze iz prošlih događaja i aktivno se oslanja na memoriju za angažman u trenutačnim situacijama.
- **Sadašnjost**: Poticaj više nego obavještavanje.
  - Agent utjelovljuje sveobuhvatan pristup interakciji s ljudima. Kad se dogodi događaj, agent nadilazi statičnu obavijest ili druge statične formalnosti. Agent može pojednostaviti tokove ili dinamički generirati signale za usmjeravanje pažnje korisnika u pravom trenutku.
  - Agent prenosi informacije na temelju kontekstualnog okruženja, društvenih i kulturnih promjena te ih prilagođava korisničkoj namjeri.
  - Interakcija s agentom može biti postepena, razvijajuća se/rastuća u složenosti kako bi osnažila korisnike na duži rok.
- **Budućnost**: Prilagodba i evolucija.
  - Agent se prilagođava različitim uređajima, platformama i modalitetima.
  - Agent se prilagođava korisničkom ponašanju, potrebama pristupačnosti i slobodno je prilagodljiv.
  - Agent je oblikovan i evoluira kroz kontinuiranu interakciju s korisnikom.

### Agent (Jezgra)

Ovo su ključni elementi u jezgru dizajna agenta.

- **Prigrliti nesigurnost, ali uspostaviti povjerenje**.
  - Očekuje se određena razina nesigurnosti kod agenta. Nesigurnost je ključni element dizajna agenta.
  - Povjerenje i transparentnost su temeljni slojevi dizajna agenta.
  - Ljudi kontroliraju kad je agent uključen/isključen i status agenta je u svakom trenutku jasno vidljiv.

## Smjernice za implementaciju ovih principa

Kada koristite prethodne principe dizajna, koristite sljedeće smjernice:

1. **Transparentnost**: Informirajte korisnika da AI sudjeluje, kako funkcionira (uključujući prošle akcije) i kako dati povratnu informaciju te mijenjati sustav.
2. **Kontrola**: Omogućite korisniku prilagodbu, specificiranje preferencija i personalizaciju, te kontrolu nad sustavom i njegovim atributima (uključujući mogućnost zaboravljanja).
3. **Dosljednost**: Ciljajte na dosljedna, višemodalna iskustva na uređajima i krajnjim točkama. Koristite poznate UI/UX elemente gdje je moguće (npr. ikona mikrofona za glasovnu interakciju) i smanjite kognitivno opterećenje korisnika što je više moguće (npr. ciljanje na sažete odgovore, vizualna pomagala i sadržaje "Saznaj više").

## Kako dizajnirati putničkog agenta koristeći ove principe i smjernice

Zamislite da dizajnirate Putničkog agenta, evo kako biste mogli razmišljati o korištenju principa dizajna i smjernica:

1. **Transparentnost** – Obavijestite korisnika da je Putnički agent AI-om omogućeni agent. Osigurajte osnovne upute o početku rada (npr. poruka "Pozdrav", primjeri upita). Jasno dokumentirajte ovo na stranici proizvoda. Prikažite popis upita koje je korisnik postavio u prošlosti. Jasno objasnite kako dati povratnu informaciju (palac gore/dolje, gumb Pošalji povratnu informaciju itd.). Jasno navedite ako agent ima ograničenja u korištenju ili temama.
2. **Kontrola** – Pobrinite se da je jasno kako korisnik može mijenjati agenta nakon što je stvoren, s stvarima kao što je Sistemski upit. Omogućite korisniku da odabere koliko opširan agent treba biti, njegov stil pisanja i bilo koje rezerve o temama o kojima agent ne bi trebao razgovarati. Dopustite korisniku pregled i brisanje bilo kojih pridruženih datoteka ili podataka, upita i prethodnih razgovora.
3. **Dosljednost** – Osigurajte da ikone za Dijeljenje upita, dodavanje datoteke ili fotografije te označavanje nekoga ili nečega budu standardne i prepoznatljive. Koristite ikonu spajalice za označavanje prijenosa/dijeljenja datoteke s agentom, a ikonu slike za prijenos grafike.

## Primjerni kodovi

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Imate li dodatna pitanja o AI agentnim dizajnerskim obrascima?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da biste se susreli s drugim učenicima, sudjelovali na radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

- <a href="https://openai.com" target="_blank">Prakse za upravljanje agentnim AI sustavima | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Prethodno poglavlje

[Istraživanje agentnih okvira](../02-explore-agentic-frameworks/README.md)

## Sljedeće poglavlje

[Obrazac dizajna za korištenje alata](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->