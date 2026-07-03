[![Kako Dizajnirati Dobre AI Agente](../../../translated_images/hr/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknite gornju sliku za pregled videozapisa ove lekcije)_
# Principi Dizajna AI Agenta

## Uvod

Postoji mnogo načina razmišljanja o izgradnji AI agentnih sustava. Budući da je nejasnoća značajka, a ne greška u dizajnu generativne AI, inženjerima zna ponekad biti teško shvatiti odakle uopće početi. Stvorili smo skup ljudski usmjerenih principa dizajna korisničkog iskustva kako bismo programerima omogućili izgradnju agentnih sustava usmjerenih na korisnike za rješavanje njihovih poslovnih potreba. Ovi principi dizajna nisu propisna arhitektura, već polazna točka za timove koji definiraju i razvijaju agentna iskustva.

Općenito, agenti bi trebali:

- Proširiti i skalirati ljudske sposobnosti (protu-stavno razmišljanje, rješavanje problema, automatizacija itd.)
- Popuniti praznine u znanju (dovesti me u tijek domena znanja, prijevod itd.)
- Olakšati i podržati suradnju na načine na koje kao pojedinci preferiramo raditi s drugima
- Učiniti nas boljim verzijama sebe (npr., životni trener/zadatkovni gospodar, pomažući nam naučiti emocionalnu regulaciju i vještine mindfulnessa, izgradnju otpornosti itd.)

## Ova Lekcija Će Pokriti

- Što su principi dizajna agentnog sustava
- Koje smjernice slijediti prilikom implementacije ovih principa dizajna
- Primjere korištenja principa dizajna

## Ciljevi Učenja

Nakon završetka ove lekcije, moći ćete:

1. Objasniti što su principi dizajna agentnog sustava
2. Objasniti smjernice za korištenje principa dizajna agentnog sustava
3. Razumjeti kako izgraditi agenta koristeći principe dizajna agentnog sustava

## Principi Dizajna Agentnog Sustava

![Principi Dizajna Agentnog Sustava](../../../translated_images/hr/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Prostor)

Ovo je okruženje u kojem agent djeluje. Ovi principi informiraju kako dizajniramo agente za angažman u fizičkim i digitalnim svjetovima.

- **Povezivanje, a ne zamjena** – pomaže povezati ljude s drugim ljudima, događajima i primjenjivim znanjem za omogućavanje suradnje i povezivanja.
- Agenti pomažu povezati događaje, znanje i ljude.
- Agenti dovode ljude bliže jedne drugima. Nisu dizajnirani da zamijene ili umanjuju ljude.
- **Lako dostupno, a povremeno nevidljivo** – agent uglavnom djeluje u pozadini i samo nas potakne kad je relevantno i prikladno.
  - Agent je lako pronaći i dostupan ovlaštenim korisnicima na bilo kojem uređaju ili platformi.
  - Agent podržava multimodalne ulaze i izlaze (zvuk, glas, tekst itd.).
  - Agent može besprijekorno prelaziti između prednjeg i stražnjeg plana; između proaktivnog i reaktivnog, ovisno o prepoznavanju potreba korisnika.
  - Agent može djelovati nevidljivo, ali njegov pozadinski proces i suradnja s drugim agentima su transparentni i kontrolirani od strane korisnika.

### Agent (Vrijeme)

Ovo je kako agent djeluje tijekom vremena. Ovi principi informiraju kako dizajniramo agente koji komuniciraju preko prošlosti, sadašnjosti i budućnosti.

- **Prošlost**: Razmišljanje o povijesti koja uključuje i stanje i kontekst.
  - Agent pruža relevantnije rezultate na temelju analize bogatijih povijesnih podataka, ne samo događaja, ljudi ili stanja.
  - Agent stvara veze iz prošlih događaja i aktivno razmišlja o sjećanju kako bi se uključio u trenutne situacije.
- **Sadašnjost**: Poticanje više nego samo obavještavanje.
  - Agent utjelovljuje sveobuhvatan pristup interakciji s ljudima. Kada se dogodi događaj, agent prelazi statično obavještavanje ili drugu statičnu formalnost. Agent može pojednostaviti procese ili dinamički generirati signale za usmjeravanje pažnje korisnika u pravom trenutku.
  - Agent isporučuje informacije temeljem kontekstualnog okruženja, društvenih i kulturnih promjena i prilagođeno namjeri korisnika.
  - Interakcija s agentom može biti postepena, razvijajuća se/raste u složenosti kako bi osnažila korisnike na dulji rok.
- **Budućnost**: Prilagođavanje i razvoj.
  - Agent se prilagođava raznim uređajima, platformama i modalitetima.
  - Agent se prilagođava ponašanju korisnika, potrebama pristupačnosti te je slobodno prilagodljiv.
  - Agent je oblikovan i razvija se kontinuiranom interakcijom s korisnikom.

### Agent (Jezgra)

Ovo su ključni elementi u središtu dizajna agenta.

- **Prihvatiti nesigurnost, ali uspostaviti povjerenje**.
  - Očekuje se određena razina nesigurnosti agenta. Nesigurnost je ključni element dizajna agenta.
  - Povjerenje i transparentnost su temeljni slojevi dizajna agenta.
  - Ljudi kontroliraju kada je agent uključen/isključen i status agenta je jasno vidljiv u svakom trenutku.

## Smjernice za Implementaciju Ovih Principa

Kada koristite prethodne principe dizajna, primijenite sljedeće smjernice:

1. **Transparentnost**: Obavijestite korisnika da je uključena AI, kako ona funkcionira (uključujući prošle radnje) i kako dati povratne informacije i mijenjati sustav.
2. **Kontrola**: Omogućite korisniku prilagodbu, specificiranje preferencija i personalizaciju te kontrolu nad sustavom i njegovim atributima (uključujući mogućnost zaborava).
3. **Dosljednost**: Ciljajte na dosljedna, multimodalna iskustva preko uređaja i krajnjih točaka. Koristite poznate UI/UX elemente gdje je moguće (npr., ikona mikrofona za glasovnu interakciju) i smanjite kognitivno opterećenje korisnika koliko je moguće (npr., težite sažetim odgovorima, vizualnim pomagalima i sadržaju „Saznaj više“).

## Kako Dizajnirati Putničkog Agenta koristeći Ove Principa i Smjernice

Zamislite da dizajnirate Putničkog Agenta, ovako biste mogli razmišljati o korištenju principa dizajna i smjernica:

1. **Transparentnost** – Obavijestite korisnika da je Putnički Agent AI-agenta. Pružite osnovne upute kako započeti (npr., poruka „Bok“, primjeri upita). Jasno dokumentirajte to na stranici proizvoda. Prikažite popis upita koje je korisnik postavio u prošlosti. Jasno navedite kako dati povratne informacije (palac gore/dolje, gumb Pošalji povratnu informaciju itd.). Javno navesti postoje li ograničenja u korištenju ili temama o kojima agent smije razgovarati.
2. **Kontrola** – Neka bude jasno na koji način korisnik može modificirati agenta nakon što je stvoren, npr. putem sustavnog upita. Omogućite korisniku da izabere koliko je agent rječito, njegov stil pisanja i eventualne zabrane tema o kojima agent ne smije govoriti. Dopustite korisniku pregled i brisanje povezanih datoteka, podataka, upita i prošlih razgovora.
3. **Dosljednost** – Pobrinite se da su ikone za Dijeli upit, dodavanje datoteke ili fotografije te označavanje nekoga/nečega standardne i prepoznatljive. Koristite ikonu spajalice za prijenos/dijeljenje datoteka s agentom te ikonu slike za prijenos grafika.

## Primjeri Kôdova

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Imate Više Pitanja o AI Agentnim Dizajnerskim Obrasima?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se upoznali s drugim učenicima, sudjelovali u radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni Resursi

- <a href="https://openai.com" target="_blank">Prakse za upravljanje agentnim AI sustavima | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Kutija za alate odgovorne AI</a>

## Prethodna Lekcija

[Pregled Agentnih Okvira](../02-explore-agentic-frameworks/README.md)

## Sljedeća Lekcija

[Obrazac dizajna za upotrebu alata](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->