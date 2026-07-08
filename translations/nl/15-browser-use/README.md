# Computergebruikagenten (CUA) bouwen

Computergebruikagenten kunnen met websites omgaan op dezelfde manier als een persoon: door een browser te openen, de pagina te inspecteren en de beste volgende actie te ondernemen op basis van wat ze zien. In deze les bouw je een browserautomatiseringsagent die Airbnb doorzoekt, gestructureerde gegevens van aanbiedingen extraheert en het goedkoopste verblijf in Stockholm identificeert.

De les combineert Browser-Use voor door AI aangestuurde navigatie, Playwright en Chrome DevTools Protocol (CDP) voor browserbeheer, Azure OpenAI voor vision-enabled redeneren, en Pydantic voor gestructureerde extractie.

## Inleiding

Deze les behandelt:

- Begrijpen wanneer computergebruikagenten beter geschikt zijn dan alleen API-automatisering
- Het combineren van Browser-Use met Playwright en CDP voor betrouwbare browser lifecycle management
- Het gebruik van Azure OpenAI vision en gestructureerde Pydantic-output om aanbiedinggegevens van dynamische webpagina's te extraheren
- Beslissen wanneer je een agent-first, actor-first of hybride browserautomatiseringsworkflow moet gebruiken

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Browser-Use configureert met Azure OpenAI en Playwright
- Een browserautomatiseringsworkflow bouwt die een echte website navigeert en omgaat met dynamische UI-elementen
- Getypeerde resultaten extraheert uit zichtbare paginainhoud en deze omzet in downstream businesslogica
- Kiest tussen agent- en actorpatronen op basis van hoe voorspelbaar de browsertaken zijn

## Codesample

Deze les bevat één notebooktutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Start een Chrome-sessie via CDP, zoekt op Airbnb naar aanbiedingen in Stockholm, extraheert prijzen met Browser-Use vision, en retourneert de goedkoopste optie als gestructureerde data.

## Vereisten

- Python 3.12+
- Azure OpenAI deployment geconfigureerd in je omgeving
- Chrome of Chromium lokaal geïnstalleerd
- Playwright-afhankelijkheden geïnstalleerd
- Basiskennis van async Python

## Installatie

Installeer de pakketten die in de notebook worden gebruikt:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Stel de Azure OpenAI omgevingsvariabelen in die door de notebook worden gebruikt:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optioneel: standaard naar de nieuwste API-versie als deze wordt weggelaten
AZURE_OPENAI_API_VERSION=...
```

## Architectuuroverzicht

De notebook demonstreert een hybride browserautomatiseringsworkflow:

1. Chrome start met CDP ingeschakeld zodat zowel Playwright als Browser-Use dezelfde browsersessie kunnen delen.
2. Een Browser-Use agent handelt open-eind navigatietaken af zoals Airbnb openen, pop-ups wegklikken, en zoeken naar Stockholm.
3. De actieve pagina wordt geïnspecteerd met een gestructureerd Pydantic-schema om de titels van aanbiedingen, nachtprijzen, beoordelingen en URL's te extraheren.
4. Python logica vergelijkt de geëxtraheerde aanbiedingen en markeert het goedkoopste resultaat.

Deze aanpak behoudt het flexibele, vision-based redeneren waar Browser-Use goed in is, terwijl je toch deterministisch browserbeheer krijgt wanneer je het nodig hebt.

## Belangrijkste lessen en best practices

### Wanneer Agent vs Actor te gebruiken

| Scenario | Agent gebruiken | Actor gebruiken |
|----------|-----------------|------------------|
| Dynamische lay-outs | Ja, AI kan zich aanpassen aan paginawijzigingen | Nee, fragile selectors kunnen breken |
| Bekende structuur | Nee, een agent is trager dan directe controle | Ja, snel en precies |
| Elementen vinden | Ja, natuurlijke taal werkt goed | Nee, exacte selectors zijn vereist |
| Timing-controle | Nee, minder voorspelbaar | Ja, volledige controle over wachten en pogingen |
| Complexe workflows | Ja, handelt onverwachte UI-toestanden af | Nee, vereist expliciete vertakkingen |

### Browser-Use best practices

1. Begin met een agent voor verkenning en dynamische navigatie.
2. Schakel over naar directe paginabesturing wanneer de interactie voorspelbaar wordt.
3. Gebruik gestructureerde outputmodellen zodat geëxtraheerde data gevalideerd en typeveilig is.
4. Voeg strategisch vertragingen toe na acties die zichtbare UI-wijzigingen veroorzaken.
5. Maak screenshots tijdens het itereren zodat fouten makkelijker te debuggen zijn.
6. Verwacht dat websites veranderen en ontwerp fallback-strategieën voor pop-ups en lay-outverschuivingen.
7. Combineer agent- en actorpatronen om zowel flexibiliteit als precisie te bereiken.

### Toepassingen in de praktijk

- Reisboekingen en prijsmonitoring
- E-commerce prijsvergelijking en beschikbaarheidscontroles
- Gestructureerde extractie van dynamische websites
- Vision-gebaseerde UI-testen en verificatie
- Website monitoring en waarschuwingen
- Intelligente formulierinvoer over multi-step flows

## Praktijkvoorbeeld: Microsoft Project Opal

De agent die je bouwt in deze les is een kleine, lokale versie van een **computergebruikagent (CUA)** — een programma dat een browser aanstuurt zoals een persoon dat zou doen. Microsoft brengt ditzelfde idee naar de onderneming met **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, een functie in Microsoft 365 Copilot.

Met Project Opal beschrijf je een taak en werkt de agent namens jou via **computergebruik op een beveiligde Windows 365 Cloud-pc**, opererend over de browsergebaseerde applicaties, sites en gegevens van je organisatie. Het werkt **asynchroon op de achtergrond**, en je kunt het werk begeleiden of op elk moment de controle overnemen. Voorbeelden van taken zijn:

- Beheren van lidmaatschapsverzoeken voor beveiligingsgroepen
- Verzamelen en valideren van auditbewijs voor compliance beoordelingen
- IT-incidenten triëren (bijwerken ticketstatus, toewijzen eigenaren, duplicaten sluiten)
- Excel-gegevens compileren in een financieel afsluitingsrapport

Opal is een nuttige referentie voor hoe een **productiereife, betrouwbare** computergebruikagent eruitziet — en het versterkt concepten uit eerdere lessen:

| Concept in deze cursus | Hoe Project Opal het toepast |
|------------------------|-----------------------------|
| **Mens-in-de-lus** (Les 06) | Opal pauzeert voor inloggegevens, gevoelige data of onduidelijke instructies, en voert nooit wachtwoorden in of verstuurt formulieren zonder expliciete bevestiging. Je kunt *Controle overnemen* en *Controle teruggeven* halverwege de taak. |
| **Betrouwbare & veilige agenten** (Lessen 06 & 18) | Draait in een geïsoleerde Windows 365 Cloud-pc, is standaard alleen browsergebaseerd (andere computertoegang geblokkeerd, afgedwongen via Intune), gebruikt *jouw* identiteit zodat het alleen toegang heeft tot wat jij mag, en logt elke actie voor auditdoeleinden. |
| **Planning & metacognitie** (Lessen 07 & 09) | Opal maakt eerst een plan voor de taak, houdt toezicht op zijn eigen redenering bij elke stap en pauzeert als het verdachte activiteiten detecteert. |
| **Herbruikbare mogelijkheden / tools** (Les 04) | **Skills** laten je instructies schrijven voor herhaalbare taken (geïmporteerd vanuit een `.md`-bestand of gemaakt met Opal) en hergebruiken in gesprekken. |

> **Beschikbaarheid:** Project Opal is momenteel beschikbaar voor gebruikers in het [Frontier vroege toegang programma](https://adoption.microsoft.com/copilot/frontier-program/) met een Microsoft 365 Copilot-abonnement, en je beheerder moet de setup voltooien. Omdat het een experimentele Frontier-functie is, kunnen functionaliteiten in de loop der tijd veranderen.

## Aanvullende bronnen

- [Aan de slag met Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integratiesjabloon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters en content extractie](https://docs.browser-use.com/customize/actor/all-parameters)
- [Cursus Setup](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->