[![Hur man utformar bra AI-agenter](../../../translated_images/sv/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klicka på bilden ovan för att se videon för denna lektion)_
# Principer för AI Agentisk Design

## Introduktion

Det finns många sätt att tänka kring att bygga AI Agentiska System. Eftersom tvetydighet är en egenskap och inte en brist i Generativ AI-design, kan det ibland vara svårt för ingenjörer att ens veta var man ska börja. Vi har skapat ett uppsättning människocentrerade UX-designprinciper för att möjliggöra för utvecklare att bygga kundcentrerade agentiska system för att möta deras affärsbehov. Dessa designprinciper är inte en föreskriven arkitektur utan snarare en startpunkt för team som definierar och bygger ut agentupplevelser.

Generellt bör agenter:

- Bredda och skala mänskliga kapaciteter (idékläckning, problemlösning, automatisering etc.)
- Fyll i kunskapsluckor (få mig uppdaterad inom kunskapsdomäner, översättning etc.)
- Underlätta och stödja samarbete på de sätt som vi som individer föredrar att arbeta med andra
- Göra oss till bättre versioner av oss själva (t.ex. livscoach/uppgiftsansvarig, hjälpa oss att lära oss känsloreglering och mindfulness-färdigheter, bygga resiliens etc.)

## Denna lektion kommer att täcka

- Vad Agentiska Designprinciper är
- Vilka riktlinjer som bör följas vid implementering av dessa designprinciper
- Exempel på användning av designprinciperna

## Lärandemål

Efter att ha genomgått denna lektion kommer du att kunna:

1. Förklara vad Agentiska Designprinciper är
2. Förklara riktlinjerna för att använda Agentiska Designprinciper
3. Förstå hur man bygger en agent med hjälp av Agentiska Designprinciper

## Agentiska Designprinciper

![Agentiska Designprinciper](../../../translated_images/sv/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Plats)

Detta är miljön som agenten verkar i. Dessa principer styr hur vi designar agenter för att verka i fysiska och digitala världar.

- **Koppla samman, inte kollapsa** – hjälp till att koppla människor till andra människor, händelser och handlingsbar kunskap för att möjliggöra samarbete och kontakt.
- Agenter hjälper till att koppla samman händelser, kunskap och människor.
- Agenter för människor närmare varandra. De är inte designade för att ersätta eller förminska människor.
- **Lättillgänglig men ibland osynlig** – agenten verkar till stor del i bakgrunden och påminner oss bara när det är relevant och lämpligt.
  - Agenten är lätt att upptäcka och komma åt för auktoriserade användare på vilken enhet eller plattform som helst.
  - Agenten stödjer multimodala in- och utgångar (ljud, röst, text etc.).
  - Agenten kan sömlöst växla mellan förgrund och bakgrund; mellan proaktiv och reaktiv, beroende på dess uppfattning av användarens behov.
  - Agenten kan verka osynligt, men dess bakgrundsprocessväg och samarbete med andra agenter är transparenta och kontrollerbara för användaren.

### Agent (Tid)

Så här verkar agenten över tid. Dessa principer styr hur vi designar agenter som interagerar över dåtid, nutid och framtid.

- **Dåtid**: Reflekterande över historia som inkluderar både tillstånd och kontext.
  - Agenten levererar mer relevanta resultat baserat på analys av rikare historiska data bortom endast händelsen, personerna eller tillstånden.
  - Agenten skapar kopplingar från tidigare händelser och reflekterar aktivt över minnet för att engagera sig med aktuella situationer.
- **Nu**: Uppmuntrar mer än notifierar.
  - Agenten innefattar ett helhetsgrepp för att interagera med människor. När en händelse inträffar går agenten utöver statisk notifikation eller annan statisk formalitet. Agenten kan förenkla flöden eller dynamiskt generera signaler för att rikta användarens uppmärksamhet vid rätt ögonblick.
  - Agenten levererar information baserad på kontextuell miljö, sociala och kulturella förändringar samt anpassad efter användarens avsikt.
  - Agentens interaktion kan vara gradvis, utvecklas/komplexifieras för att stärka användare på lång sikt.
- **Framtid**: Anpassa och utvecklas.
  - Agenten anpassar sig till olika enheter, plattformar och modaliteter.
  - Agenten anpassar sig till användarbeteende, tillgänglighetsbehov och är fritt anpassningsbar.
  - Agenten formas av och utvecklas genom kontinuerlig användarinteraktion.

### Agent (Kärna)

Dessa är de nyckelelement som finns i kärnan av agentens design.

- **Omfamna osäkerhet men etablera förtroende**.
  - En viss nivå av agentosäkerhet förväntas. Osäkerhet är ett nyckelelement i agentdesign.
  - Förtroende och transparens är grundläggande lager i agentdesign.
  - Människor kontrollerar när agenten är på/av och agentens status är tydligt synlig hela tiden.

## Riktlinjer för att implementera dessa principer

När du använder de föregående designprinciperna, använd följande riktlinjer:

1. **Transparens**: Informera användaren om att AI är inblandat, hur det fungerar (inklusive tidigare handlingar) och hur man ger feedback och ändrar systemet.
2. **Kontroll**: Ge användaren möjlighet att anpassa, specificera preferenser och personalisera samt ha kontroll över systemet och dess attribut (inklusive möjligheten att glömma).
3. **Konsistens**: Sträva efter konsekventa, multimodala upplevelser över enheter och ändpunkter. Använd välkända UI/UX-element där det är möjligt (t.ex. mikrofonikon för röstinteraktion) och minska användarens kognitiva belastning så mycket som möjligt (t.ex. sträva efter kortfattade svar, visuella hjälpmedel och 'Lär dig mer'-innehåll).

## Hur man utformar en reseagent med dessa principer och riktlinjer

Föreställ dig att du designar en reseagent, här är hur du kan tänka kring användningen av designprinciper och riktlinjer:

1. **Transparens** – Låt användaren veta att reseagenten är en AI-driven agent. Ge grundläggande instruktioner för att komma igång (t.ex. ett “Hej”-meddelande, exempel på uppmaningar). Dokumentera detta tydligt på produktsidan. Visa listan över uppmaningar som användaren har ställt tidigare. Gör det klart hur man ger feedback (tumme upp och ner, knapp för att skicka feedback etc.). Förtydliga om agenten har användnings- eller ämnesbegränsningar.
2. **Kontroll** – Se till att det är tydligt hur användaren kan ändra agenten efter att den skapats med saker som systemuppmaningen. Ge användaren möjlighet att välja hur utförlig agenten är, dess skrivstil och eventuella begränsningar kring vad agenten inte bör diskutera. Tillåt användaren att se och radera eventuella associerade filer, data, uppmaningar och tidigare konversationer.
3. **Konsistens** – Se till att ikoner för Dela Uppmaning, lägga till en fil eller bild och tagga någon eller något är standardiserade och igenkännbara. Använd gemikonen för att indikera filuppladdning/delning med agenten, och en bildikon för grafikuppladdning.

## Exempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Fler frågor om AI Agentiska Designmönster?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstider och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://openai.com" target="_blank">Praxis för styrning av Agentiska AI-system | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">The HAX Toolkit Project - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Ansvarsfull AI Toolbox</a>

## Föregående lektion

[Utforska Agentiska Ramverk](../02-explore-agentic-frameworks/README.md)

## Nästa lektion

[Verktygsanvändningsdesignmönster](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->