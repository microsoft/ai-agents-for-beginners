# Bygga datoranvändaragenter (CUA)

Datoranvändaragenter kan interagera med webbplatser på samma sätt som en person: genom att öppna en webbläsare, inspektera sidan och ta nästa bästa åtgärd utifrån vad de ser. I denna lektion bygger du en webbläsarautomationsagent som söker på Airbnb, extraherar strukturerad listningsdata och identifierar det billigaste boendet i Stockholm.

Lektionen kombinerar Browser-Use för AI-driven navigering, Playwright och Chrome DevTools Protocol (CDP) för webbläsarkontroll, Azure OpenAI för synbaserad resonemang och Pydantic för strukturerad extraktion.

## Introduktion

Denna lektion täcker:

- Förstå när datoranvändaragenter är bättre än enbart API-automatisering
- Kombinera Browser-Use med Playwright och CDP för pålitlig hantering av webbläsarlivscykeln
- Använda Azure OpenAI vision och strukturerad Pydantic-utmatning för att extrahera listningsdata från dynamiska webbsidor
- Avgöra när man ska använda ett agent-först-, aktör-först- eller hybridwebbläsarautomationsarbetsflöde

## Lärandemål

Efter att ha slutfört denna lektion kommer du att veta hur du:

- Konfigurerar Browser-Use med Azure OpenAI och Playwright
- Bygger ett automatiserat arbetsflöde som navigerar på en riktig webbplats och hanterar dynamiska UI-element
- Extraherar typade resultat från synligt sidinnehåll och omvandlar dem till efterföljande affärslogik
- Väljer mellan agent- och aktörsmönster baserat på hur förutsägbar webbläsaruppgiften är

## Kodexempel

Denna lektion innehåller en Jupyter-notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Startar en Chrome-session via CDP, söker Airbnb efter listningar i Stockholm, extraherar priser med Browser-Use vision och returnerar det billigaste alternativet som strukturerad data.

## Förutsättningar

- Python 3.12+
- Azure OpenAI-distribution konfigurerad i din miljö
- Chrome eller Chromium installerat lokalt
- Playwright-beroenden installerade
- Grundläggande kunskap om asynkron Python

## Installation

Installera paketen som används i notebooken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Ställ in miljövariabler för Azure OpenAI som notebooken använder:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valfritt: standard är den senaste API-versionen när det utelämnas
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturöversikt

Notebooken visar ett hybrid-webbläsarautomationsarbetsflöde:

1. Chrome startar med CDP aktiverat så att både Playwright och Browser-Use kan dela samma webbläsarsession.
2. En Browser-Use-agent hanterar öppna navigeringsuppgifter som att öppna Airbnb, bortse från popup-fönster och söka efter Stockholm.
3. Den aktiva sidan inspekteras med ett strukturerat Pydantic-schema för att extrahera listningstitlar, nattpriser, betyg och URL:er.
4. Python- logik jämför de extraherade listningarna och lyfter fram det billigaste resultatet.

Detta tillvägagångssätt bevarar den flexibla, synbaserade resonemangsförmågan som Browser-Use är bra på samtidigt som du får deterministisk kontroll över webbläsaren när du behöver det.

## Viktiga slutsatser och bästa praxis

### När ska man använda Agent vs Aktör

| Scenario | Använd Agent | Använd Aktör |
|----------|--------------|--------------|
| Dynamiska layouter | Ja, AI kan anpassa sig till sidändringar | Nej, spröda selektorer kan gå sönder |
| Känd struktur | Nej, en agent är långsammare än direkt kontroll | Ja, snabbt och precist |
| Hitta element | Ja, naturligt språk fungerar bra | Nej, exakta selektorer krävs |
| Tidskontroll | Nej, mindre förutsägbar | Ja, full kontroll över väntetider och försök |
| Komplexa arbetsflöden | Ja, hanterar oväntade UI-tillstånd | Nej, kräver explicit grenhantering |

### Browser-Use bästa praxis

1. Börja med en agent för utforskning och dynamisk navigering.
2. Byt till direkt sidkontroll när interaktionen blir förutsägbar.
3. Använd strukturerade utdata modeller så att extraherad data valideras och är typ-säker.
4. Lägg till fördröjningar strategiskt efter åtgärder som triggar synliga UI-förändringar.
5. Ta skärmbilder under iteration så att fel är lättare att felsöka.
6. Förvänta dig att webbplatser ändras och designa reservstrategier för popup-fönster och layoutskiften.
7. Kombinera agent- och aktörsmönster för att få både flexibilitet och precision.

### Tillämpningar i verkliga världen

- Resebokning och prisövervakning
- Jämförelse av priser och tillgänglighet e-handel
- Strukturerad extraktion från dynamiska webbplatser
- Synmedveten UI-testning och verifiering
- Webbplatsövervakning och larm
- Intelligent formulärifyllning över flerstegsflöden

## Exempel från verkligheten: Microsoft Project Opal

Agenten du bygger i denna lektion är en liten, lokal version av en **datoranvändaragent (CUA)** — ett program som styr en webbläsare som en människa. Microsoft för detta koncept till företagsvärlden med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en uppgift och agenten arbetar åt dig med **datoranvändning på en säker Windows 365 Cloud PC**, och verkar över organisationens webbläsarbaserade appar, sajter och data. Den arbetar **asynkront i bakgrunden**, och du kan styra arbetet eller ta kontroll när som helst. Exempeluppgifter inkluderar:

- Hantering av medlemsförfrågningar för säkerhetsgrupper
- Insamling och validering av revisionsbevis för compliance-granskningar
- Triage av IT-incidenter (uppdatera ärendestatus, tilldela ansvariga, avsluta dubbletter)
- Sammanställning av Excel-data till en finansiell rapport

Opal är en användbar referens för hur en **produktionsklar, pålitlig** datoranvändaragent ser ut — och förstärker koncept från tidigare lektioner:

| Begrepp i denna kurs | Hur Project Opal tillämpar det |
|----------------------|--------------------------------|
| **Human-in-the-loop** (Lektion 06) | Opal pausar för inloggningsuppgifter, känslig data eller otydliga instruktioner, och matar aldrig in lösenord eller skickar formulär utan tydlig bekräftelse. Du kan *Ta kontroll* och *Återlämna kontroll* mitt i en uppgift. |
| **Pålitliga och säkra agenter** (Lektioner 06 & 18) | Körs i en isolerad Windows 365 Cloud PC, är webbläsarbaserad som standard (annan datoråtkomst blockeras och styrs via Intune), använder *din* identitet så att den bara kommer åt det du är behörig för, och loggar varje åtgärd för revision. |
| **Planering & metakognition** (Lektioner 07 & 09) | Opal generar en plan för uppgiften först och övervakar sedan sitt eget resonemang i varje steg och pausar vid misstänkt aktivitet. |
| **Återanvändbara kapabiliteter / verktyg** (Lektion 04) | **Kompetenser** låter dig skriva instruktioner för upprepbara jobb (importerade från en `.md`-fil eller skapade med Opal) och återanvända dem över flera samtal. |

> **Tillgänglighet:** Project Opal är för närvarande tillgängligt för användare i [Frontier tidig tillgångsprogram](https://adoption.microsoft.com/copilot/frontier-program/) med Microsoft 365 Copilot-prenumeration, och din administratör måste slutföra installationen. Eftersom det är en experimentell Frontier-funktion kan kapabiliteter förändras över tid.

## Ytterligare resurser

- [Kom igång med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrationsmall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktörparametrar och innehållsextraktion](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursinstallation](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->