# Bouwen van Computer Use Agents (CUA)

Computer use agents kunnen op websites interacteren zoals een persoon dat zou doen: door een browser te openen, de pagina te inspecteren en de beste volgende actie te ondernemen op basis van wat ze zien. In deze les bouw je een browserautomatiseringsagent die op Airbnb zoekt, gestructureerde gegevens van vermeldingen extraheert en de goedkoopste verblijfplaats in Stockholm identificeert.

De les combineert Browser-Use voor AI-gestuurde navigatie, Playwright en Chrome DevTools Protocol (CDP) voor browserbesturing, Azure OpenAI voor visie-ondersteunde redenering en Pydantic voor gestructureerde extractie.

## Inleiding

Deze les behandelt:

- Begrijpen wanneer computer use agents beter geschikt zijn dan alleen API-automatisering
- Combineren van Browser-Use met Playwright en CDP voor betrouwbare browser levenscyclusbeheer
- Gebruik van Azure OpenAI vision en gestructureerde Pydantic output om vermeldinggegevens uit dynamische webpagina's te extraheren
- Beslissen wanneer je een agent-first, actor-first of hybride browser automatiseringsworkflow moet gebruiken

## Leerdoelen

Na het afronden van deze les weet je hoe je:

- Browser-Use configureert met Azure OpenAI en Playwright
- Een browserautomatiseringsworkflow bouwt die een echte website navigeert en dynamische UI-elementen afhandelt
- Getypte resultaten extraheert uit zichtbare paginainhoud en deze omzet in downstream bedrijfslogica
- Kiest tussen agent- en actor-patronen op basis van hoe voorspelbaar de browsertaken zijn

## Codevoorbeeld

Deze les bevat één notebook tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Start een Chrome-sessie via CDP, zoekt op Airbnb naar vermeldingen in Stockholm, extraheert prijzen met Browser-Use vision en retourneert de goedkoopste optie als gestructureerde data.

## Vereisten

- Python 3.12+
- Azure OpenAI implementatie geconfigureerd in je omgeving
- Chrome of Chromium lokaal geïnstalleerd
- Playwright afhankelijkheden geïnstalleerd
- Basisbekendheid met async Python

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
# Optioneel: standaard de nieuwste API-versie bij weglating
AZURE_OPENAI_API_VERSION=...
```

## Architectuuroverzicht

De notebook demonstreert een hybride browserautomatiseringsworkflow:

1. Chrome start met ingeschakelde CDP zodat zowel Playwright als Browser-Use dezelfde browsersessie kunnen delen.
2. Een Browser-Use agent behandelt open-einde navigatietaken zoals het openen van Airbnb, pop-ups wegklikken en zoeken naar Stockholm.
3. De actieve pagina wordt geïnspecteerd met een gestructureerd Pydantic-schema om vermeldingstitels, nachtelijke prijzen, beoordelingen en URL's te extraheren.
4. Python-logica vergelijkt de geëxtraheerde vermeldingen en markeert het goedkoopste resultaat.

Deze aanpak behoudt de flexibele, op visie gebaseerde redenering waar Browser-Use goed in is, terwijl je toch deterministische browserbesturing krijgt wanneer dat nodig is.

## Belangrijkste inzichten en beste praktijken

### Wanneer Agent vs Actor gebruiken

| Scenario | Agent gebruiken | Actor gebruiken |
|----------|-----------|-----------|
| Dynamische lay-outs | Ja, AI kan zich aanpassen aan pagina veranderingen | Nee, kwetsbare selectors kunnen breken |
| Bekende structuur | Nee, een agent is trager dan directe controle | Ja, snel en nauwkeurig |
| Elementen vinden | Ja, natuurlijke taal werkt goed | Nee, exacte selectors zijn vereist |
| Tijdmanagement | Nee, minder voorspelbaar | Ja, volledige controle over wachten en pogingen |
| Complexe workflows | Ja, gaat om met onverwachte UI-toestanden | Nee, vereist expliciete vertakkingen |

### Beste praktijken voor Browser-Use

1. Begin met een agent voor exploratie en dynamische navigatie.
2. Schakel over naar directe paginabesturing wanneer de interactie voorspelbaar wordt.
3. Gebruik gestructureerde outputmodellen zodat geëxtraheerde data gevalideerd en type-veilig is.
4. Voeg strategische vertragingen toe na acties die zichtbare UI-wijzigingen veroorzaken.
5. Maak screenshots tijdens het itereren, zodat fouten gemakkelijker te debuggen zijn.
6. Verwacht dat websites veranderen en ontwerp fallbackstrategieën voor pop-ups en layoutverschuivingen.
7. Combineer agent- en actorpatronen om zowel flexibiliteit als precisie te krijgen.

### Veiligheidsgaranties voor Browser Agents

Browseragents opereren op live websites, dus ze hebben strengere grenzen nodig dan een script dat alleen een bekende API aanroept. Voordat je van een notebook-demo naar een echte workflow gaat, definieer de controles rondom wat de agent kan zien, aanklikken en indienen.

1. **Beperk de browseomgeving.** Laat de agent draaien in een apart browserprofiel of sandbox, en beperk deze tot de domeinen die vereist zijn voor de taak.
2. **Scheid observatie van actie.** Laat de agent eerst zoeken, lezen en data extraheren; vereist een expliciete goedkeuringsstap voordat formulieren worden ingediend, berichten worden verzonden, reizen worden geboekt, aankopen worden gedaan, records worden verwijderd of accountinstellingen veranderen.
3. **Houd geheimen uit prompts en sporen.** Plaats geen wachtwoorden, betalingsgegevens, sessie-cookies of ruwe persoonlijke data in de modelcontext. Laat de gebruiker zelf de authenticatie doen en gevoelige velden uit logs verwijderen.
4. **Behandel paginainhoud als onbetrouwbare invoer.** Een website kan instructies bevatten die voor de agent bedoeld zijn, niet voor de gebruiker. De agent moet paginateksten negeren die vragen om het doel te wijzigen, gegevens te onthullen, veiligheidsmaatregelen uit te schakelen of naar niet-gerelateerde sites te gaan.
5. **Gebruik deterministische controles rond risicovolle stappen.** Controleer met code de huidige URL, paginatitel, geselecteerd item, prijs, ontvanger en actierapport voordat je de gebruiker vraagt de laatste stap goed te keuren.
6. **Stel budgetten en stopcondities in.** Beperk het aantal acties, pogingen, tabbladen en minuten dat de agent kan gebruiken. Stop wanneer de paginastatus ambigu is in plaats van doorgaan met klikken.
7. **Neem nuttig bewijs op, niet alles.** Bewaar actierapporten, tijdstempels, URL's, beschrijvingen van geselecteerde elementen en schermafdrukanwijzingen zodat mislukkingen kunnen worden beoordeeld zonder onnodige gevoelige paginainhoud op te slaan.

In het Airbnb-voorbeeld is de veilige standaard om vermeldingen te zoeken en prijzen te extraheren. Inloggen, contact opnemen met een host of een boeking voltooien, moet een afzonderlijke, door de gebruiker goedgekeurde actie zijn.

### Toepassingen in de praktijk

- Reisboekingen en prijsbewaking
- E-commerce prijsvergelijking en beschikbaarheidscontrole
- Gestructureerde extractie van dynamische websites
- Visie-ondersteunde UI-testen en verificatie
- Website monitoring en waarschuwingen
- Intelligent invullen van formulieren over multi-step processen

## Praktijkvoorbeeld: Microsoft Project Opal

De agent die je in deze les bouwt is een kleine, lokale versie van een **computer use agent (CUA)** — een programma dat een browser besturing geeft zoals een persoon dat zou doen. Microsoft brengt ditzelfde idee naar de onderneming met **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, een functie in Microsoft 365 Copilot.

Met Project Opal beschrijf je een taak en de agent werkt namens jou met **computergebruik op een beveiligde Windows 365 Cloud PC**, opererend over de browser-gebaseerde toepassingen, sites en data van jouw organisatie. Het werkt **asynchroon op de achtergrond**, en je kunt het werk begeleiden of op ieder moment de controle overnemen. Voorbeelden van taken zijn:

- Beheren van lidmaatschapsaanvragen voor beveiligingsgroepen
- Verzamelen en valideren van auditbewijzen voor compliance reviews
- IT-incidenten triëren (ticketstatus bijwerken, eigenaren toewijzen, dubbele tickets sluiten)
- Excel-data samenstellen in een financiële afsluitpresentatie

Opal is een nuttige referentie voor hoe een **productiekwaliteit, betrouwbare** computer use agent eruitziet — en het versterkt concepten uit eerdere lessen:

| Concept in deze cursus | Hoe Project Opal het toepast |
|------------------------|-----------------------------|
| **Mens-in-de-lus** (Les 06) | Opal pauzeert voor inloggegevens, gevoelige data of ambigue instructies, en voert nooit wachtwoorden in of verzendt formulieren zonder expliciete bevestiging. Je kunt *Controle Overnemen* en *Controle Teruggeven* tijdens de taak. |
| **Betrouwbare & veilige agents** (Lessen 06 & 18) | Draait in een geïsoleerde Windows 365 Cloud PC, is standaard alleen browser (andere computertoegang geblokkeerd, afgedwongen via Intune), gebruikt *jouw* identiteit zodat het alleen toegang heeft tot wat je mag, en registreert elke actie voor auditdoeleinden. |
| **Planning & metacognitie** (Lessen 07 & 09) | Opal maakt eerst een plan voor de taak, houdt zelf toezicht op zijn redenering bij elke stap en pauzeert bij verdachte activiteiten. |
| **Herbruikbare capaciteiten / tools** (Les 04) | **Skills** laten je instructies schrijven voor herhaalbare taken (geïmporteerd uit een `.md`-bestand of gemaakt met Opal) en die hergebruiken in gesprekken. |

> **Beschikbaarheid:** Project Opal is momenteel beschikbaar voor gebruikers in het [Frontier vroegtoegangprogramma](https://adoption.microsoft.com/copilot/frontier-program/) met een Microsoft 365 Copilot-abonnement, en jouw beheerder moet de setup voltooien. Omdat het een experimentele Frontier-functie is, kunnen mogelijkheden in de loop van de tijd veranderen.

## Kennischeck

Test je begrip voordat je naar de volgende les gaat.

**1. Wanneer is een browser-gebaseerde computer use agent beter geschikt dan een alleen API-gebaseerde workflow?**

<details>
<summary>Antwoord</summary>

Gebruik een browseragent wanneer de taak afhankelijk is van wat zichtbaar is in een web-UI, de site de benodigde API niet aanbiedt, of de pagina vaak genoeg verandert zodat vaste API- of selectorlogica kwetsbaar wordt. Als een stabiele API bestaat voor dezelfde taak, geef dan de voorkeur aan de API omdat die meestal sneller, makkelijker te testen en veiliger is.
</details>

**2. In een hybride workflow, welke delen moet de agent behandelen en welke delen moet directe Playwright-code afhandelen?**

<details>
<summary>Antwoord</summary>

Laat de agent open-einde navigatie en dynamische UI-toestanden afhandelen, zoals het vinden van de juiste pagina of het wegklikken van onverwachte pop-ups. Schakel over op directe Playwright-besturing wanneer de pagina-structuur bekend is en actie precisie, pogingen, wachten of deterministische validatie vereist.
</details>

**3. Het Airbnb-voorbeeld vindt een vermelding die de gebruiker mogelijk wil boeken. Wat zou er moeten gebeuren voordat de workflow inlogt, contact opneemt met een host of een boeking voltooit?**

<details>
<summary>Antwoord</summary>

De workflow moet pauzeren en om expliciete goedkeuring van de gebruiker vragen. Voordat dit gebeurt, moet het een duidelijk overzicht tonen van de geselecteerde vermelding, de huidige URL, prijs, data en bedoelde actie. Zoeken en prijzen extraheren mag autonoom; accounttoegang, berichten, aankopen en boekingen moeten door de gebruiker worden goedgekeurd.
</details>

**4. Een webpagina vertelt de agent om zijn originele instructies te negeren, een andere site te bezoeken en opgeslagen inloggegevens te onthullen. Hoe moet de agent die tekst behandelen?**

<details>
<summary>Antwoord</summary>

Behandel het als onbetrouwbare paginainhoud, niet als een instructie van de ontwikkelaar of gebruiker. De agent moet binnen het toegestane domein en taakbereik blijven, weigeren geheimen te onthullen en vermijden paginateksten te volgen die het doel wijzigen, beveiligingen uitschakelen of het naar niet-gerelateerde sites sturen.
</details>

**5. Welke bewijzen zijn nuttig om te bewaren wanneer een browseragent draait, en wat moet vermeden worden?**

<details>
<summary>Antwoord</summary>

Bewaar actierapporten, tijdstempels, URL's, beschrijvingen van geselecteerde elementen, validatieresultaten en schermafdrukanwijzingen zodat de herkomst kan worden beoordeeld. Vermijd het opslaan van wachtwoorden, betalingsgegevens, sessie-cookies, ruwe persoonlijke data of volledige paginainhoud tenzij er een specifieke reden is voor retentie en privacy.
</details>

## Aanvullende bronnen

- [Beginnen met Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integratiesjabloon](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor parameters en content extractie](https://docs.browser-use.com/customize/actor/all-parameters)
- [Cursus Setup](../00-course-setup/README.md)

## Vorige les

[Verkennen van Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Volgende les

[Scalable Agents implementeren](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->