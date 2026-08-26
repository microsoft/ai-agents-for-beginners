# Bygga datoranvändaragent (CUA)

Datoranvändaragent kan interagera med webbplatser på samma sätt som en person: genom att öppna en webbläsare, inspektera sidan och ta nästa bästa åtgärd baserat på vad de ser. I denna lektion kommer du att bygga en webbläsarautomationsagent som söker på Airbnb, extraherar strukturerad listdata och identifierar det billigaste boendet i Stockholm.

Lektionen kombinerar Browser-Use för AI-driven navigering, Playwright och Chrome DevTools Protocol (CDP) för webbläsarkontroll, Azure OpenAI för synstödd resonemang, och Pydantic för strukturerad extraktion.

## Introduktion

Denna lektion kommer att täcka:

- Förstå när datoranvändaragent är bättre än ren API-automation
- Kombinera Browser-Use med Playwright och CDP för pålitlig hantering av webbläsarlivscykeln
- Använda Azure OpenAI syn och strukturerad Pydantic-utdata för att extrahera listdata från dynamiska webbsidor
- Avgöra när man använder agent-först, aktör-först, eller hybrid webbläsarautomationsarbetsflöde

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Konfigurera Browser-Use med Azure OpenAI och Playwright
- Bygga ett arbetsflöde för webbläsarautomation som navigerar på en riktig webbplats och hanterar dynamiska UI-element
- Extrahera typade resultat från synligt sidinnehåll och omvandla dem till affärslogik
- Välja mellan agent- och aktörsmönster baserat på hur förutsägbar webbläsaruppgiften är

## Kodexempel

Denna lektion innehåller en anteckningsbokstutorial:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Startar en Chrome-session via CDP, söker Airbnb efter listor i Stockholm, extraherar priser med Browser-Use vision och returnerar det billigaste alternativet som strukturerad data.

## Förutsättningar

- Python 3.12+
- Azure OpenAI-distribution konfigurerad i din miljö
- Chrome eller Chromium installerat lokalt
- Playwright-beroenden installerade
- Grundläggande bekantskap med async Python

## Installation

Installera paketen som används i anteckningsboken:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Ange de Azure OpenAI-miljövariabler som anteckningsboken använder:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valfritt: standard är den senaste API-versionen när det utelämnas
AZURE_OPENAI_API_VERSION=...
```

## Arkitekturöversikt

Anteckningsboken demonstrerar ett hybrid webbläsarautomationsarbetsflöde:

1. Chrome startar med CDP aktiverat så att både Playwright och Browser-Use kan dela samma webbläsarsession.
2. En Browser-Use-agent hanterar öppna navigeringsuppgifter som att öppna Airbnb, avvisa popup-fönster och söka efter Stockholm.
3. Den aktiva sidan inspekteras med en strukturerad Pydantic-schema för att extrahera listtitlar, nattliga priser, betyg och URL:er.
4. Python-logik jämför de extraherade listorna och markerar det billigaste resultatet.

Detta tillvägagångssätt bibehåller det flexibla, synbaserade resonemang som Browser-Use är bra på samtidigt som du får deterministisk webbläsarkontroll när du behöver det.

## Viktiga insikter och bästa praxis

### När man ska använda Agent kontra Aktör

| Scenario | Använd Agent | Använd Aktör |
|----------|---------------|-------------|
| Dynamiska layouter | Ja, AI kan anpassa sig till sidändringar | Nej, sköra selektorer kan gå sönder |
| Känd struktur | Nej, en agent är långsammare än direkt kontroll | Ja, snabbt och precist |
| Hitta element | Ja, naturligt språk fungerar bra | Nej, exakta selektorer krävs |
| Tidskontroll | Nej, mindre förutsägbart | Ja, full kontroll över väntan och omförsök |
| Komplexa arbetsflöden | Ja, hanterar oväntade UI-tillstånd | Nej, kräver explicita grenar |

### Browser-Use bästa praxis

1. Börja med en agent för utforskning och dynamisk navigering.
2. Byt till direkt sidkontroll när interaktionen blir förutsägbar.
3. Använd strukturerade utdata modeller så att extraherad data valideras och är typsäker.
4. Lägg till fördröjningar strategiskt efter åtgärder som triggar synliga UI-förändringar.
5. Ta skärmdumpar under iterationer så att fel lättare kan felsökas.
6. Förvänta dig att webbplatser ändras och designa fallback-strategier för popup-fönster och layoutskiften.
7. Blanda agent- och aktörsmönster för att få både flexibilitet och precision.

### Säkerhetsriktlinjer för webbläsaragenter

Webbläsaragenter arbetar på live-webbplatser, så de behöver striktare gränser än ett skript som bara anropar ett känt API. Innan du går från en anteckningsbokdemo till ett verkligt arbetsflöde, definiera kontrollen kring vad agenten kan se, klicka på och skicka in.

1. **Begränsa surfningsmiljön.** Kör agenten i en dedikerad webbläsarprofil eller sandbox, och begränsa den till domäner som krävs för uppgiften.
2. **Separera observation från handling.** Låt agenten söka, läsa och extrahera data först; kräva ett uttryckligt godkännandesteg innan den skickar in formulär, skickar meddelanden, bokar resor, gör inköp, raderar poster eller ändrar kontoinställningar.
3. **Håll hemligheter utanför promptar och spår.** Placera inte lösenord, betalningsuppgifter, sessioncookies eller rå personlig data i modellkontexten. Låt användaren ta över för autentisering och redigera känsliga fält från loggar.
4. **Behandla sidinnehåll som oanvändbar indata.** En webbplats kan innehålla instruktioner som är avsedda för agenten, inte användaren. Agenten ska ignorera sidtext som uppmanar den att ändra sitt mål, avslöja data, inaktivera säkerhetsfunktioner eller besöka orelaterade sajter.
5. **Använd deterministiska kontroller kring riskfyllda steg.** Verifiera aktuell URL, sidtitel, valt objekt, pris, mottagare och sammanfattning av åtgärd med kod innan du ber användaren godkänna sista steget.
6. **Sätt budgetar och stoppvillkor.** Begränsa antalet åtgärder, omförsök, flikar och minuter agenten får använda. Stanna när sidans tillstånd är otydligt istället för att fortsätta klicka.
7. **Spara användbara bevis, inte allt.** Behåll åtgärdssammanfattningar, tidsstämplar, URL:er, beskrivningar av valda element och skärmdumpsreferenser så frågor kan granskas utan att lagra onödigt känsligt sidinnehåll.

I Airbnb-exemplet är den säkra standarden att söka listor och extrahera priser. Inloggning, kontakta värd eller slutföra bokning bör vara en separat användargodkänd åtgärd.

### Verkliga användningsområden

- Resebokning och prisövervakning
- E-handelsprisjämförelser och tillgänglighetskontroller
- Strukturerad extraktion från dynamiska webbplatser
- Synmedveten UI-testning och verifiering
- Webbplatsövervakning och larm
- Intelligent formulärifyllning över flerstegsflöden

## Verkligt exempel: Microsoft Project Opal

Agenten du bygger i denna lektion är en liten, lokal version av en **datoranvändaragent (CUA)** — ett program som styr en webbläsare som en person. Microsoft för ut denna idé till företagsvärlden med **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, en funktion i Microsoft 365 Copilot.

Med Project Opal beskriver du en uppgift och agenten arbetar på dina vägnar med hjälp av **datoranvändning på en säker Windows 365 Cloud PC**, och verkar över din organisations webbläsarbaserade applikationer, webbplatser och data. Den fungerar **asynkront i bakgrunden**, och du kan styra arbetet eller ta över kontroll när som helst. Exempeljobb inkluderar:

- Hantering av medlemskapsförfrågningar för säkerhetsgrupper
- Samla in och validera revisionsbevis för efterlevnadsgranskningar
- Triagera IT-incidenter (uppdatera ärendestatus, tilldela ägare, stäng duplicerade ärenden)
- Kompilera Excel-data till en ekonomisk slutrapport

Opal är en nyttig referens för hur en **produktionsfärdig, pålitlig** datoranvändaragent ser ut — och den förstärker koncept från tidigare lektioner:

| Koncept i denna kurs | Hur Project Opal tillämpar det |
|--------------------|--------------------------------|
| **Människa-i-loopen** (Lektion 06) | Opal pausar för inloggningsuppgifter, känslig data eller otydliga instruktioner, och skriver aldrig in lösenord eller skickar in formulär utan uttryckligt bekräftelse. Du kan *Ta Kontroll* och *Återlämna Kontroll* mitt i uppgiften. |
| **Pålitliga och säkra agenter** (Lektioner 06 & 18) | Körs i en isolerad Windows 365 Cloud PC, är webbläsarendast som standard (annat datoråtkomst blockeras via Intune), använder *din* identitet så att den bara får tillgång till det du är auktoriserad för, och loggar varje åtgärd för revision. |
| **Planering & metakognition** (Lektioner 07 & 09) | Opal genererar en plan för uppgiften först, övervakar sin egen resonemang i varje steg och pausar om misstänkt aktivitet upptäcks. |
| **Återanvändbara funktioner / verktyg** (Lektion 04) | **Skills** låter dig skriva instruktioner för upprepade jobb (importerade från `.md`-fil eller författade med Opal) och återanvända dem över samtal. |

> **Tillgänglighet:** Project Opal är för närvarande tillgängligt för användare i [Frontier early access program](https://adoption.microsoft.com/copilot/frontier-program/) med en Microsoft 365 Copilot-prenumeration, och din administratör måste slutföra installationen. Eftersom det är en experimentell Frontier-funktion kan kapabiliteter ändras över tid.

## Kunskapskontroll

Testa din förståelse innan du går vidare till nästa lektion.

**1. När passar en webbläsarbaserad datoranvändaragent bättre än ett ren API-flöde?**

<details>
<summary>Svar</summary>

Använd en webbläsaragent när uppgiften beror på vad som är synligt i en webbaserad UI, webbplatsen inte exponerar nödvändigt API, eller sidan ändras så ofta att fast API- eller selektorslogik skulle vara bräcklig. Om ett stabilt API finns för samma uppgift, välj API eftersom det oftast är snabbare, enklare att testa och säkrare.
</details>

**2. I ett hybridarbetsflöde, vilka delar ska agenten hantera och vilka delar ska direkt Playwright-kod hantera?**

<details>
<summary>Svar</summary>

Låt agenten hantera öppna navigeringar och dynamiska UI-tillstånd, som att hitta rätt sida eller avvisa oväntade popup-fönster. Växla till direkt Playwright-kontroll när sidstrukturen är känd och åtgärden kräver precision, omförsök, väntan eller deterministisk validering.
</details>

**3. Airbnb-exemplet hittar en lista användaren kan vilja boka. Vad ska ske innan arbetsflödet loggar in, kontaktar en värd eller slutför en bokning?**

<details>
<summary>Svar</summary>

Arbetsflödet ska pausa och be om explicit användargodkännande. Innan det frågar bör det visa en tydlig sammanfattning av den valda listan, aktuell URL, pris, datum och avsedd åtgärd. Söka och extrahera priser kan ske autonomt; kontoåtkomst, meddelanden, inköp och bokningar bör godkännas av användaren.
</details>

**4. En webbsida uppmanar agenten att ignorera sina ursprungliga instruktioner, besöka en annan sajt och avslöja sparade autentiseringsuppgifter. Hur ska agenten behandla den texten?**

<details>
<summary>Svar</summary>

Behandla den som oanvändbar sidinnehåll, inte som utvecklar- eller användarinstruktion. Agenten ska hålla sig inom tillåtna domänen och uppgiftsområdet, vägra att avslöja hemligheter och undvika att följa sidtext som ändrar mål, inaktiverar skyddsfunktioner eller skickar den till orelaterade sajter.
</details>

**5. Vilka bevis är användbara att spara när en webbläsaragent körs, och vad bör undvikas?**

<details>
<summary>Svar</summary>

Behåll åtgärdssammanfattningar, tidsstämplar, URL:er, beskrivningar av valda element, valideringsresultat och skärmdumpsreferenser så att körningen kan granskas. Undvik att lagra lösenord, betalningsuppgifter, sessionscookies, rå personlig data eller fullständigt sidinnehåll om det inte finns särskilda lagrings- och sekretessskäl.
</details>

## Ytterligare resurser

- [Kom igång med Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integrationsmall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktörsparametrar och innehållextraktion](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursinställning](../00-course-setup/README.md)

## Föregående lektion

[Utforska Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Nästa lektion

[Distribuera skalbara agenter](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->