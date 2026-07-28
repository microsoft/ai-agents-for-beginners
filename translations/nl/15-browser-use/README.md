# Computergebruikagenten (CUA) bouwen

Computergebruikagenten kunnen met websites interageren zoals een persoon dat zou doen: door een browser te openen, de pagina te inspecteren en de volgende beste actie te ondernemen op basis van wat ze zien. In deze les bouw je een browserautomatiseringsagent die Airbnb doorzoekt, gestructureerde gegevens van aanbiedingen haalt en het goedkoopste verblijf in Stockholm identificeert.

De les combineert Browser-Use voor AI-gedreven navigatie, Playwright en Chrome DevTools Protocol (CDP) voor browserbesturing, Azure OpenAI voor zicht-ondersteunde redenering, en Pydantic voor gestructureerde extractie.

## Introductie

Deze les behandelt:

- Begrijpen wanneer computergebruikagenten beter geschikt zijn dan alleen API-automatisering
- Browser-Use combineren met Playwright en CDP voor betrouwbare browser levenscyclusbeheer
- Azure OpenAI-vision en gestructureerde Pydantic output gebruiken om aanbiedingsgegevens van dynamische webpagina’s te extraheren
- Beslissen wanneer een agent-first, actor-first, of hybride browserautomatiseringsworkflow te gebruiken

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

- Browser-Use configureert met Azure OpenAI en Playwright
- Een browserautomatiseringsworkflow bouwt die een echte website navigeert en dynamische UI-elementen afhandelt
- Getypeerde resultaten extraheert van zichtbare pagina-inhoud en die omzet in downstream bedrijfslogica
- Kiest tussen agent- en actorpatronen op basis van hoe voorspelbaar de browsertaken zijn

## Codevoorbeeld

Deze les bevat één notebooktutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Start een Chrome-sessie via CDP, doorzoekt Airbnb voor aanbiedingen in Stockholm, extraheert prijzen met Browser-Use vision en retourneert de goedkoopste optie als gestructureerde data.

## Vereisten

- Python 3.12+
- Azure OpenAI-implementatie geconfigureerd in je omgeving
- Chrome of Chromium lokaal geïnstalleerd
- Vereisten van Playwright geïnstalleerd
- Basiskennis van async Python

## Setup

Installeer de pakketten die in de notebook worden gebruikt:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Stel de Azure OpenAI-omgevingsvariabelen in die door de notebook worden gebruikt:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optioneel: standaard wordt de nieuwste API-versie gebruikt wanneer weggelaten
AZURE_OPENAI_API_VERSION=...
```

## Architectuuroverzicht

De notebook demonstreert een hybride browserautomatiseringsworkflow:

1. Chrome start met CDP ingeschakeld zodat zowel Playwright als Browser-Use dezelfde browsersessie kunnen delen.
2. Een Browser-Use agent handelt open-eind navigatietaken af zoals Airbnb openen, pop-ups wegklikken en zoeken naar Stockholm.
3. De actieve pagina wordt geïnspecteerd met een gestructureerd Pydantic-schema om titels van aanbiedingen, nachtprijzen, beoordelingen en URL's te extraheren.
4. Python-logica vergelijkt de geëxtraheerde aanbiedingen en markeert het goedkoopste resultaat.

Deze aanpak behoudt de flexibele, op visie gebaseerde redenering waar Browser-Use goed in is, terwijl je toch deterministische browserversturing krijgt wanneer dat nodig is.

## Belangrijkste inzichten en best practices

### Wanneer Agent versus Actor gebruiken

| Scenario | Agent gebruiken | Actor gebruiken |
|----------|-----------------|-----------------|
| Dynamische lay-outs | Ja, AI kan zich aanpassen aan paginawijzigingen | Nee, breekbare selectors kunnen falen |
| Bekende structuur | Nee, een agent is trager dan directe besturing | Ja, snel en nauwkeurig |
| Elementen vinden | Ja, natuurlijke taal werkt goed | Nee, exacte selectors zijn vereist |
| Tijdregeling | Nee, minder voorspelbaar | Ja, volledige controle over wachten en herhalingen |
| Complexe workflows | Ja, behandelt onverwachte UI-toestanden | Nee, vereist expliciete vertakkingen |

### Browser-Use Best Practices

1. Begin met een agent voor verkenning en dynamische navigatie.
2. Schakel over naar directe besturing van de pagina wanneer de interactie voorspelbaar wordt.
3. Gebruik gestructureerde outputmodellen zodat geëxtraheerde data gevalideerd en typsafe is.
4. Voeg strategisch vertragingen toe na acties die zichtbare UI-veranderingen veroorzaken.
5. Maak screenshots tijdens het itereren zodat fouten makkelijker te debuggen zijn.
6. Verwacht dat websites veranderen en ontwerp fallback-strategieën voor pop-ups en layoutverschuivingen.
7. Combineer agent- en actorpatronen om zowel flexibiliteit als precisie te krijgen.

### Veiligheidsmaatregelen voor Browser Agents

Browseragents opereren op live websites, dus hebben ze strengere grenzen nodig dan een script dat alleen een bekende API aanroept. Definieer voordat je overgaat van een notebook-demo naar een echte workflow de controles over wat de agent mag zien, klikken en versturen.

1. **Beperk de browseromgeving.** Laat de agent draaien in een toegewijd browserprofiel of sandbox, en beperk hem tot de domeinen die voor de taak nodig zijn.
2. **Scheid observatie van actie.** Laat de agent eerst zoeken, lezen en data extraheren; vereist een expliciete goedkeuringsstap voordat hij formulieren verstuurt, berichten verzendt, reizen boekt, aankopen doet, records verwijdert of accountinstellingen wijzigt.
3. **Houd geheimen buiten prompts en sporen.** Plaats geen wachtwoorden, betaalgegevens, sessiecookies of ruwe persoonlijke data in de modelcontext. Laat de gebruiker de authenticatie overnemen en verwijder gevoelige velden uit logs.
4. **Behandel paginainhoud als niet-vertrouwde input.** Een website kan instructies bevatten die bedoeld zijn voor de agent, niet voor de gebruiker. De agent moet pagina-tekst negeren die vraagt om het doel te veranderen, data te onthullen, beveiligingen uit te schakelen of niet-gerelateerde sites te bezoeken.
5. **Gebruik deterministische controles rond risicovolle stappen.** Verifieer de huidige URL, paginatitel, geselecteerd item, prijs, ontvanger en actieresumé met code voordat je de gebruiker vraagt de laatste stap goed te keuren.
6. **Stel budgetten en stopcondities in.** Beperk het aantal acties, herhalingen, tabs en minuten dat de agent mag gebruiken. Stop als de paginastatus onduidelijk is in plaats van door te klikken.
7. **Neem bruikbaar bewijs op, niet alles.** Bewaar actieresumés, tijdstempels, URL's, beschrijvingen van geselecteerde elementen en screenshotverwijzingen zodat fouten kunnen worden nagekeken zonder onnodige gevoelige paginainhoud op te slaan.

In het Airbnb-voorbeeld is de veilige standaard om aanbiedingen te zoeken en prijzen te extraheren. Inloggen, contact opnemen met een host of een boeking afronden moet een aparte door de gebruiker goedgekeurde actie zijn.

### Toepassingen in de praktijk

- Reisboekingen en prijsbewaking
- Prijsvergelijkingen en beschikbaarheidscontroles in e-commerce
- Gestructureerde extractie van dynamische websites
- Visie-gebaseerde UI testen en verificatie
- Websitebewaking en alarmen
- Intelligente formulierinvoer over multi-step processen

## Praktijkvoorbeeld: Microsoft Project Opal

De agent die je in deze les bouwt is een kleine, lokale versie van een **computergebruikagent (CUA)** — een programma dat een browser bestuurt zoals een persoon dat zou doen. Microsoft brengt ditzelfde idee naar de onderneming met **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, een functie in Microsoft 365 Copilot.

Met Project Opal beschrijf je een taak en werkt de agent namens jou gebruikmakend van **computergebruik op een beveiligde Windows 365 Cloud PC**, die over de browsergebaseerde applicaties, sites, en data van je organisatie opereert. Het werkt **asynchroon op de achtergrond**, en je kunt het werk begeleiden of te allen tijde overnemen. Voorbeeldtaken omvatten:

- Beheer van verzoeken tot lidmaatschap van beveiligingsgroepen
- Verzamelen en valideren van auditbewijs voor compliance controles
- Afhandelen van IT-incidenten (bijwerken ticketstatus, eigenaars toewijzen, duplicaten sluiten)
- Excel-gegevens samenstellen in een financiële afsluitpresentatie

Opal is een bruikbare referentie voor hoe een **productieklaar, betrouwbaar** computergebruikagent eruitziet — en het versterkt concepten uit eerdere lessen:

| Concept in deze cursus | Hoe Project Opal dit toepast |
|------------------------|-----------------------------|
| **Mens-in-de-lus** (Les 06) | Opal pauzeert voor inloggegevens, gevoelige data of onduidelijke instructies, en voert nooit wachtwoorden in of verstuurt formulieren zonder expliciete bevestiging. Je kunt *Overnemen* en *Teruggeven* midden in een taak. |
| **Betrouwbare & veilige agents** (Lessen 06 & 18) | Draait in een geïsoleerde Windows 365 Cloud PC, is standaard alleen-browser (toegang tot andere computerfuncties geblokkeerd via Intune), gebruikt *jouw* identity zodat het alleen toegang heeft tot wat je mag, en logt elke actie voor controleerbaarheid. |
| **Planning & metacognitie** (Lessen 07 & 09) | Opal genereert eerst een plan voor de taak, houdt toezicht op zijn eigen redenering bij elke stap, en pauzeert als het verdachte activiteit detecteert. |
| **Herbruikbare vaardigheden / tools** (Les 04) | **Skills** laten je instructies schrijven voor herhaalbare taken (geïmporteerd uit een `.md` bestand of gemaakt met Opal) en ze hergebruiken in gesprekken. |

> **Beschikbaarheid:** Project Opal is momenteel beschikbaar voor gebruikers in het [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) met een Microsoft 365 Copilot-abonnement, en je beheerder moet de setup voltooien. Omdat het een experimentele Frontier-functie is, kunnen mogelijkheden in de loop van de tijd veranderen.

## Aanvullende bronnen

- [Aan de slag met Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integratiesjabloon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actorparameters en inhoudsextractie](https://docs.browser-use.com/customize/actor/all-parameters)
- [Cursus Setup](../00-course-setup/README.md)

## Vorige les

[Verkennen van Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Volgende les

[Schaalbare agents implementeren](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->