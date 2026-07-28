# Bygga datoranvändar-agenter (CUA)

Datoranvändar-agenter kan interagera med webbplatser på samma sätt som en person: genom att öppna en webbläsare, inspektera sidan och ta nästa bästa åtgärd utifrån vad de ser. I denna lektion bygger du en webbläsarautomationsagent som söker på Airbnb, extraherar strukturerad listdata och identifierar det billigaste boendet i Stockholm.

Lektionen kombinerar Browser-Use för AI-driven navigering, Playwright och Chrome DevTools Protocol (CDP) för webbläsarkontroll, Azure OpenAI för synbaserad resonemang och Pydantic för strukturerad extraktion.

## Introduktion

Denna lektion kommer att täcka:

- Förstå när datoranvändar-agenter är bättre än API-endast automatisering
- Kombinera Browser-Use med Playwright och CDP för pålitlig hantering av webbläsarlivscykeln
- Använda Azure OpenAI vision och strukturerad Pydantic-utmatning för att extrahera listdata från dynamiska webbsidor
- Besluta när man ska använda en agent-först, aktör-först eller hybrid webbläsarautomationsarbetsflöde

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Konfigurera Browser-Use med Azure OpenAI och Playwright
- Bygga ett webbläsarautomationsarbetsflöde som navigerar på en riktigt webbplats och hanterar dynamiska UI-element
- Extrahera typade resultat från synligt sidinnehåll och omvandla dem till vidare affärslogik
- Välja mellan agent- och aktörsmönster baserat på hur förutsägbar webbläsaruppgiften är

## Kodexempel

Den här lektionen innehåller en notebook-tutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Startar en Chrome-session över CDP, söker på Airbnb efter boenden i Stockholm, extraherar priser med Browser-Use vision och returnerar det billigaste alternativet som strukturerad data.

## Förutsättningar

- Python 3.12+
- Azure OpenAI-distribution konfigurerad i din miljö
- Chrome eller Chromium installerat lokalt
- Playwright-beroenden installerade
- Grundläggande kännedom om asynkron Python

## Installation

Installera paketen som används i notebooken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Sätt Azure OpenAI-miljövariablerna som används av notebooken:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valfritt: standard är den senaste API-versionen när det utelämnas
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturöversikt

Notebooks demonstrerar ett hybrid arbetsflöde för webbläsarautomation:

1. Chrome startar med CDP aktiverat så både Playwright och Browser-Use kan dela samma webbläsarsession.
2. En Browser-Use-agent hanterar öppna navigationsuppgifter såsom att öppna Airbnb, avvisa popup-fönster och söka efter Stockholm.
3. Den aktiva sidan inspekteras med ett strukturerat Pydantic-schema för att extrahera listtitrar, nattliga priser, betyg och URL:er.
4. Python-logik jämför de extraherade listorna och markerar det billigaste resultatet.

Detta tillvägagångssätt behåller den flexibla, synbaserade resonemangsförmågan som Browser-Use är bra på samtidigt som du får deterministisk webbläsarkontroll när du behöver den.

## Viktiga Slutsatser och Bästa Praxis

### När man ska använda Agent vs Aktör

| Scenario | Använd Agent | Använd Aktör |
|----------|--------------|-------------|
| Dynamiska layouter | Ja, AI kan anpassa sig till sidändringar | Nej, sköra selektorer kan gå sönder |
| Känd struktur | Nej, en agent är långsammare än direkt kontroll | Ja, snabbt och precist |
| Hitta element | Ja, naturligt språk fungerar bra | Nej, exakta selektorer krävs |
| Tidstyrning | Nej, mindre förutsägbart | Ja, full kontroll över väntetider och omförsök |
| Komplexa arbetsflöden | Ja, hanterar oväntade UI-tillstånd | Nej, kräver explicit förgrening |

### Browser-Use Bästa Praxis

1. Börja med en agent för utforskning och dynamisk navigering.
2. Byt till direkt sidkontroll när interaktionen blir förutsägbar.
3. Använd strukturerade utdata modeller så att extraherad data är validerad och typ-säker.
4. Lägg till fördröjningar strategiskt efter åtgärder som triggar synliga UI-förändringar.
5. Ta skärmdumpar under iterationer så att fel blir lättare att felsöka.
6. Förvänta dig att webbplatser förändras och designa fallback-strategier för popup-fönster och layoutskiften.
7. Blanda agent- och aktörsmönster för att få både flexibilitet och precision.

### Säkerhetsåtgärder för Webbläsaragenter

Webbläsaragenter arbetar på levande webbplatser, så de behöver snävare gränser än ett skript som bara anropar ett känt API. Innan du går från en notebook-demo till ett verkligt arbetsflöde, definiera kontrollerna kring vad agenten kan se, klicka på och skicka in.

1. **Avgränsa surfningsmiljön.** Kör agenten i en dedikerad webbläsarprofil eller sandlåda, och begränsa den till de domäner som krävs för uppgiften.
2. **Separera observation från handling.** Låt agenten söka, läsa och extrahera data först; kräva ett uttryckligt godkännande steg innan den skickar in formulär, skickar meddelanden, bokar resor, genomför köp, raderar poster eller ändrar kontoinställningar.
3. **Håll hemligheter utanför prompts och spår.** Placera inte lösenord, betalningsuppgifter, sessionscookies eller rå personlig data i modellkontexten. Låt användaren ta över för autentisering och censurera känsliga fält från loggar.
4. **Behandla sidinnehåll som opålitlig indata.** En webbplats kan innehålla instruktioner som är avsedda för agenten, inte användaren. Agenten ska ignorera sidtext som ber den att ändra sitt mål, avslöja data, inaktivera säkerhetsåtgärder eller besöka orelaterade sidor.
5. **Använd deterministiska kontroller kring riskfyllda steg.** Verifiera den aktuella URL:en, sidrubriken, vald artikel, pris, mottagare och sammanfattning av åtgärden med kod innan du ber användaren godkänna slutsteget.
6. **Sätt budgetar och stoppvillkor.** Begränsa antalet åtgärder, omförsök, flikar och minuter agenten kan använda. Stoppa när sidans tillstånd är oklart istället för att fortsätta klicka.
7. **Spela in användbara bevis, inte allt.** Behåll åtgärdssammanfattningar, tidsstämplar, URL:er, beskrivningar av valda element och referenser till skärmdumpar så att fel kan granskas utan att lagra onödigt känsligt sidinnehåll.

I Airbnb-exemplet är standard att söka listor och extrahera priser säkert. Inloggning, kontakta en värd eller slutföra en bokning bör vara en separat användargodkänd åtgärd.

### Tillämpningar i verkliga världen

- Resebokning och prisövervakning
- E-handel prisjämförelse och tillgänglighetskontroller
- Strukturerad extraktion från dynamiska webbplatser
- Synmedveten UI-testning och verifiering
- Webbplatsövervakning och larm
- Intelligenta formulärifyllningar i flerstegsflöden

## Verkligt exempel: Microsoft Project Opal

Agenten du bygger i denna lektion är en liten, lokal version av en **datoranvändar-agent (CUA)** — ett program som styr en webbläsare på samma sätt som en person skulle göra. Microsoft för denna idé till företagsvärlden med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en uppgift och agenten arbetar å dina vägnar genom **datoranvändning på en säker Windows 365 Cloud PC**, som opererar över din organisations webbläsarbaserade applikationer, webbplatser och data. Den arbetar **asynkront i bakgrunden**, och du kan styra arbetet eller ta kontroll när som helst. Exempel på jobb inkluderar:

- Hantering av medlemförfrågningar i säkerhetsgrupper
- Samla och validera revisionsbevis för efterlevnadsgranskningar
- Hantera IT-incidenter (uppdatera ärendestatus, tilldela ägare, stänga dubletter)
- Sammanställa Excel-data i en finansiell slutlig presentation

Opal är en användbar referens för hur en **produktionsklar, pålitlig** datoranvändar-agent ser ut — och förstärker koncept från tidigare lektioner:

| Koncept i denna kurs | Hur Project Opal tillämpar det |
|-----------------------|---------------------------|
| **Människa-i-loopen** (Lektion 06) | Opal pausar för inloggningsuppgifter, känslig data eller tvetydiga instruktioner och anger aldrig lösenord eller skickar formulär utan uttryckligt bekräftelse. Du kan *Ta kontroll* och *Återlämna kontroll* mitt i uppgiften. |
| **Pålitliga och säkra agenter** (Lektioner 06 & 18) | Körs i en isolerad Windows 365 Cloud PC, är webbläsarbaserad som standard (annat datoråtkomst blockerat, handhållet via Intune), använder *din* identitet så att den bara får tillgång till det du är auktoriserad för, och loggar varje åtgärd för revisionsbarhet. |
| **Planering & metakognition** (Lektioner 07 & 09) | Opal genererar en plan för jobbet först, övervakar sedan sitt eget resonemang vid varje steg och pausar om misstänkt aktivitet upptäcks. |
| **Återanvändbara kapabiliteter / verktyg** (Lektion 04) | **Färdigheter** låter dig skriva instruktioner för upprepbara jobb (importerade från en `.md` fil eller skrivna med Opal) och återanvända dem i flera konversationer. |

> **Tillgänglighet:** Project Opal är för närvarande tillgängligt för användare i [Frontier Early Access-programmet](https://adoption.microsoft.com/copilot/frontier-program/) med en Microsoft 365 Copilot-prenumeration, och din administratör måste slutföra konfigurationen. Eftersom det är en experimentell Frontier-funktion kan kapabiliteter förändras över tid.

## Ytterligare resurser

- [Kom igång med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrationsmall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktörsparametrar och content-extraktion](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursinstallation](../00-course-setup/README.md)

## Föregående lektion

[Utforska Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Nästa lektion

[Distribuera skalbara agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->