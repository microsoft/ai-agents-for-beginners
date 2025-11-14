<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T15:20:53+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "sv"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.sv.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klicka på bilden ovan för att se videon till denna lektion)_
# Metakognition i AI-agenter

## Introduktion

Välkommen till lektionen om metakognition i AI-agenter! Detta kapitel är utformat för nybörjare som är nyfikna på hur AI-agenter kan reflektera över sina egna tankemönster. I slutet av denna lektion kommer du att förstå nyckelkoncept och ha praktiska exempel för att tillämpa metakognition i designen av AI-agenter.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

1. Förstå konsekvenserna av resonansslingor i agentdefinitioner.
2. Använda planerings- och utvärderingstekniker för att hjälpa självkorrigerande agenter.
3. Skapa egna agenter som kan manipulera kod för att utföra uppgifter.

## Introduktion till metakognition

Metakognition avser de högre kognitiva processer som innebär att tänka på sitt eget tänkande. För AI-agenter innebär detta att kunna utvärdera och justera sina handlingar baserat på självmedvetenhet och tidigare erfarenheter. Metakognition, eller "att tänka på tänkande", är ett viktigt koncept i utvecklingen av agentiska AI-system. Det handlar om att AI-system är medvetna om sina egna interna processer och kan övervaka, reglera och anpassa sitt beteende därefter. Precis som vi gör när vi "läser av rummet" eller analyserar ett problem. Denna självmedvetenhet kan hjälpa AI-system att fatta bättre beslut, identifiera fel och förbättra sin prestanda över tid – vilket återkopplar till Turing-testet och debatten om huruvida AI kommer att ta över.

I sammanhanget av agentiska AI-system kan metakognition hjälpa till att hantera flera utmaningar, såsom:
- Transparens: Säkerställa att AI-system kan förklara sitt resonemang och sina beslut.
- Resonemang: Förbättra AI-systemens förmåga att syntetisera information och fatta välgrundade beslut.
- Anpassning: Möjliggöra för AI-system att anpassa sig till nya miljöer och förändrade förhållanden.
- Perception: Förbättra AI-systemens noggrannhet i att känna igen och tolka data från sin omgivning.

### Vad är metakognition?

Metakognition, eller "att tänka på tänkande", är en högre kognitiv process som innefattar självmedvetenhet och självreglering av sina kognitiva processer. Inom AI ger metakognition agenter möjlighet att utvärdera och anpassa sina strategier och handlingar, vilket leder till förbättrade problemlösnings- och beslutsförmågor. Genom att förstå metakognition kan du designa AI-agenter som inte bara är mer intelligenta utan också mer anpassningsbara och effektiva. I sann metakognition skulle AI:n uttryckligen resonera om sitt eget resonemang.

Exempel: "Jag prioriterade billigare flyg eftersom... jag kanske missar direktflyg, så låt mig dubbelkolla."
Hålla koll på hur eller varför den valde en viss rutt.
- Notera att den gjorde misstag eftersom den överbetonade användarens tidigare preferenser, och därför ändrar sin beslutsstrategi, inte bara den slutliga rekommendationen.
- Diagnostisera mönster som: "När jag ser att användaren nämner 'för trångt', bör jag inte bara ta bort vissa attraktioner utan också reflektera över att min metod att välja 'toppattraktioner' är bristfällig om jag alltid rankar efter popularitet."

### Vikten av metakognition i AI-agenter

Metakognition spelar en avgörande roll i designen av AI-agenter av flera skäl:

![Vikten av metakognition](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.sv.png)

- Självreflektion: Agenter kan utvärdera sin egen prestanda och identifiera förbättringsområden.
- Anpassningsförmåga: Agenter kan ändra sina strategier baserat på tidigare erfarenheter och förändrade miljöer.
- Felkorrigering: Agenter kan upptäcka och korrigera fel autonomt, vilket leder till mer exakta resultat.
- Resurshantering: Agenter kan optimera användningen av resurser, såsom tid och beräkningskraft, genom att planera och utvärdera sina handlingar.

## Komponenter i en AI-agent

Innan vi dyker in i metakognitiva processer är det viktigt att förstå de grundläggande komponenterna i en AI-agent. En AI-agent består vanligtvis av:

- Persona: Agentens personlighet och egenskaper, som definierar hur den interagerar med användare.
- Verktyg: De funktioner och förmågor som agenten kan utföra.
- Färdigheter: Den kunskap och expertis som agenten besitter.

Dessa komponenter samverkar för att skapa en "expertisenhet" som kan utföra specifika uppgifter.

**Exempel**:
Tänk dig en reseagent, en agenttjänst som inte bara planerar din semester utan också justerar sin planering baserat på realtidsdata och tidigare kundupplevelser.

### Exempel: Metakognition i en reseagenttjänst

Föreställ dig att du designar en reseagenttjänst som drivs av AI. Denna agent, "Reseagenten", hjälper användare att planera sina semestrar. För att inkludera metakognition behöver Reseagenten utvärdera och justera sina handlingar baserat på självmedvetenhet och tidigare erfarenheter. Så här kan metakognition spela en roll:

#### Aktuell uppgift

Den aktuella uppgiften är att hjälpa en användare att planera en resa till Paris.

#### Steg för att slutföra uppgiften

1. **Samla användarpreferenser**: Fråga användaren om deras resedatum, budget, intressen (t.ex. museer, mat, shopping) och eventuella specifika krav.
2. **Hämta information**: Sök efter flygalternativ, boenden, attraktioner och restauranger som matchar användarens preferenser.
3. **Generera rekommendationer**: Ge en personlig resplan med flygdetaljer, hotellbokningar och föreslagna aktiviteter.
4. **Justera baserat på feedback**: Be användaren om feedback på rekommendationerna och gör nödvändiga justeringar.

#### Nödvändiga resurser

- Tillgång till databaser för flyg- och hotellbokningar.
- Information om attraktioner och restauranger i Paris.
- Användarfeedbackdata från tidigare interaktioner.

#### Erfarenhet och självreflektion

Reseagenten använder metakognition för att utvärdera sin prestanda och lära sig av tidigare erfarenheter. Till exempel:

1. **Analysera användarfeedback**: Reseagenten granskar användarens feedback för att avgöra vilka rekommendationer som uppskattades och vilka som inte gjorde det. Den justerar sina framtida förslag därefter.
2. **Anpassningsförmåga**: Om en användare tidigare har nämnt att de ogillar trånga platser, undviker Reseagenten att rekommendera populära turistmål under rusningstid i framtiden.
3. **Felkorrigering**: Om Reseagenten gjorde ett fel i en tidigare bokning, som att föreslå ett hotell som var fullbokat, lär den sig att kontrollera tillgänglighet noggrannare innan den ger rekommendationer.

#### Praktiskt utvecklarexempel

Här är ett förenklat exempel på hur Reseagentens kod kan se ut när den inkluderar metakognition:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Varför metakognition är viktig

- **Självreflektion**: Agenter kan analysera sin prestanda och identifiera förbättringsområden.
- **Anpassningsförmåga**: Agenter kan ändra strategier baserat på feedback och förändrade förhållanden.
- **Felkorrigering**: Agenter kan autonomt upptäcka och korrigera misstag.
- **Resurshantering**: Agenter kan optimera resursanvändning, såsom tid och beräkningskraft.

Genom att inkludera metakognition kan Reseagenten ge mer personliga och exakta reseförslag, vilket förbättrar den övergripande användarupplevelsen.

---

## 2. Planering i agenter

Planering är en kritisk komponent i AI-agenters beteende. Det innebär att skissera de steg som behövs för att uppnå ett mål, med hänsyn till den aktuella situationen, resurser och möjliga hinder.

### Element av planering

- **Aktuell uppgift**: Definiera uppgiften tydligt.
- **Steg för att slutföra uppgiften**: Dela upp uppgiften i hanterbara steg.
- **Nödvändiga resurser**: Identifiera nödvändiga resurser.
- **Erfarenhet**: Använd tidigare erfarenheter för att informera planeringen.

**Exempel**:
Här är stegen som Reseagenten behöver ta för att effektivt hjälpa en användare att planera sin resa:

### Steg för Reseagenten

1. **Samla användarpreferenser**
   - Fråga användaren om detaljer kring resedatum, budget, intressen och eventuella specifika krav.
   - Exempel: "När planerar du att resa?" "Vad är din budget?" "Vilka aktiviteter tycker du om på semestern?"

2. **Hämta information**
   - Sök efter relevanta resealternativ baserat på användarens preferenser.
   - **Flyg**: Leta efter tillgängliga flyg inom användarens budget och föredragna resedatum.
   - **Boenden**: Hitta hotell eller hyresbostäder som matchar användarens preferenser för plats, pris och bekvämligheter.
   - **Attraktioner och restauranger**: Identifiera populära attraktioner, aktiviteter och matställen som passar användarens intressen.

3. **Generera rekommendationer**
   - Sammanställ den hämtade informationen till en personlig resplan.
   - Ge detaljer som flygalternativ, hotellbokningar och föreslagna aktiviteter, anpassade efter användarens preferenser.

4. **Presentera resplan för användaren**
   - Dela den föreslagna resplanen med användaren för granskning.
   - Exempel: "Här är en föreslagen resplan för din resa till Paris. Den inkluderar flygdetaljer, hotellbokningar och en lista över rekommenderade aktiviteter och restauranger. Vad tycker du?"

5. **Samla feedback**
   - Be användaren om feedback på den föreslagna resplanen.
   - Exempel: "Gillar du flygalternativen?" "Är hotellet lämpligt för dina behov?" "Finns det några aktiviteter du vill lägga till eller ta bort?"

6. **Justera baserat på feedback**
   - Ändra resplanen baserat på användarens feedback.
   - Gör nödvändiga ändringar i flyg-, boende- och aktivitetsrekommendationer för att bättre matcha användarens preferenser.

7. **Slutgiltig bekräftelse**
   - Presentera den uppdaterade resplanen för användaren för slutgiltig bekräftelse.
   - Exempel: "Jag har gjort justeringarna baserat på din feedback. Här är den uppdaterade resplanen. Ser allt bra ut för dig?"

8. **Boka och bekräfta reservationer**
   - När användaren godkänner resplanen, fortsätt med att boka flyg, boenden och eventuella förplanerade aktiviteter.
   - Skicka bekräftelsedetaljer till användaren.

9. **Ge löpande support**
   - Var tillgänglig för att hjälpa användaren med eventuella ändringar eller ytterligare förfrågningar före och under resan.
   - Exempel: "Om du behöver ytterligare hjälp under din resa, tveka inte att kontakta mig när som helst!"

### Exempel på interaktion

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korrigerande RAG-system

Låt oss först förstå skillnaden mellan RAG-verktyg och förhandsladdning av kontext.

![RAG vs Kontextladdning](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.sv.png)

### Retrieval-Augmented Generation (RAG)

RAG kombinerar ett återvinningssystem med en generativ modell. När en fråga ställs hämtar återvinningssystemet relevanta dokument eller data från en extern källa, och denna hämtade information används för att förstärka inmatningen till den generativa modellen. Detta hjälper modellen att generera mer exakta och kontextuellt relevanta svar.

I ett RAG-system hämtar agenten relevant information från en kunskapsbas och använder den för att generera lämpliga svar eller handlingar.

### Korrigerande RAG-ansats

Den korrigerande RAG-ansatsen fokuserar på att använda RAG-tekniker för att korrigera fel och förbättra AI-agenters noggrannhet. Detta innebär:

1. **Promptteknik**: Använda specifika prompts för att vägleda agenten i att hämta relevant information.
2. **Verktyg**: Implementera algoritmer och mekanismer som gör det möjligt för agenten att utvärdera relevansen av den hämtade informationen och generera korrekta svar.
3. **Utvärdering**: Kontinuerligt bedöma agentens prestanda och göra justeringar för att förbättra dess noggrannhet och effektivitet.

#### Exempel: Korrigerande RAG i en sökagent

Tänk dig en sökagent som hämtar information från webben för att besvara användarfrågor. Den korrigerande RAG-ansatsen kan innebära:

1. **Promptteknik**: Formulera sökfrågor baserat på användarens inmatning.
2. **Verktyg**: Använda naturlig språkbehandling och maskininlärningsalgoritmer för att rangordna och filtrera sökresultat.
3. **Utvärdering**: Analysera användarfeedback för att identifiera och korrigera felaktigheter i den hämtade informationen.

### Korrigerande RAG i Reseagenten

Korrigerande RAG (Retrieval-Augmented Generation) förbättrar en AI:s förmåga att hämta och generera information samtidigt som den korrigerar eventuella felaktigheter. Låt oss se hur Reseagenten kan använda den korrigerande RAG-ansatsen för att ge mer exakta och relevanta reseförslag.

Detta innebär:

- **Promptteknik:** Använda specifika prompts för att vägleda agenten i att hämta relevant information.
- **Verktyg:** Implementera algoritmer och mekanismer som gör det möjligt för agenten att utvärdera relevansen av den hämtade informationen och generera korrekta svar.
- **Utvärdering:** Kontinuerligt bedöma agentens prestanda och göra justeringar för att förbättra dess noggrannhet och effektivitet.

#### Steg för att implementera korrigerande RAG i Reseagenten

1. **Inledande användarinteraktion**
   - Reseagenten samlar inledande preferenser från användaren, såsom destination, resedatum, budget och intressen.
   - Exempel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Hämtning av information**
   - Reseagenten hämtar information om flyg, boenden, attraktioner och restauranger baserat på användarens preferenser.
   - Exempel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generera inledande rekommendationer**
   - Reseagenten använder den hämtade informationen för att generera en personlig resplan.
   - Exempel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Samla användarfeedback**
   - Reseagenten ber användaren om feedback på de inledande rekommendationerna.
   - Exempel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrigerande RAG-process**
   - **Promptteknik**: Reseagenten formulerar nya sökfrågor baserat på användarens feedback.
     - Exempel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Verktyg**: Reseagenten använder algoritmer för att rangordna och filtrera nya sökresultat, med fokus på relevans baserat på användarens feedback.
     - Exempel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Utvärdering**: Reseagenten bedömer kontinuerligt relevansen och noggrannheten i sina rekommendationer genom att analysera användarfeedback och göra nödvändiga justeringar.
     - Exempel:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktiskt exempel

Här är ett förenklat Python-kodexempel som inkluderar den korrigerande RAG-ansatsen i Reseagenten:
### Förhandsladdning av kontext

Förhandsladdning av kontext innebär att relevant bakgrundsinformation laddas in i modellen innan en fråga behandlas. Detta gör att modellen har tillgång till informationen från början, vilket kan hjälpa den att generera mer informerade svar utan att behöva hämta ytterligare data under processen.

Här är ett förenklat exempel på hur en förhandsladdning av kontext kan se ut för en reseagentapplikation i Python:

#### Förklaring

1. **Initialisering (`__init__`-metoden)**: Klassen `TravelAgent` laddar förhandsin en ordbok med information om populära destinationer som Paris, Tokyo, New York och Sydney. Ordboken innehåller detaljer som land, valuta, språk och stora sevärdheter för varje destination.

2. **Hämta information (`get_destination_info`-metoden)**: När en användare frågar om en specifik destination hämtar metoden `get_destination_info` relevant information från den förhandsladdade kontextordboken.

Genom att förhandsladda kontexten kan reseagentapplikationen snabbt svara på användarfrågor utan att behöva hämta information från en extern källa i realtid. Detta gör applikationen mer effektiv och responsiv.

### Starta planen med ett mål innan iteration

Att starta en plan med ett mål innebär att börja med ett tydligt definierat syfte eller önskat resultat. Genom att definiera detta mål i förväg kan modellen använda det som en vägledande princip under hela den iterativa processen. Detta hjälper till att säkerställa att varje iteration närmar sig det önskade resultatet, vilket gör processen mer effektiv och fokuserad.

Här är ett exempel på hur man kan starta en reseplan med ett mål innan iteration för en reseagent i Python:

### Scenario

En reseagent vill planera en skräddarsydd semester för en klient. Målet är att skapa en reseplan som maximerar klientens nöjdhet baserat på deras preferenser och budget.

### Steg

1. Definiera klientens preferenser och budget.
2. Starta den initiala planen baserat på dessa preferenser.
3. Iterera för att förfina planen och optimera för klientens nöjdhet.

#### Kodförklaring

1. **Initialisering (`__init__`-metoden)**: Klassen `TravelAgent` initialiseras med en lista över potentiella destinationer, där varje destination har attribut som namn, kostnad och aktivitetstyp.

2. **Starta planen (`bootstrap_plan`-metoden)**: Denna metod skapar en initial reseplan baserat på klientens preferenser och budget. Den går igenom listan över destinationer och lägger till dem i planen om de matchar klientens preferenser och passar inom budgeten.

3. **Matcha preferenser (`match_preferences`-metoden)**: Denna metod kontrollerar om en destination matchar klientens preferenser.

4. **Iterera planen (`iterate_plan`-metoden)**: Denna metod förfinar den initiala planen genom att försöka ersätta varje destination i planen med ett bättre alternativ, med hänsyn till klientens preferenser och budgetbegränsningar.

5. **Beräkna kostnad (`calculate_cost`-metoden)**: Denna metod beräknar den totala kostnaden för den aktuella planen, inklusive en potentiell ny destination.

#### Exempel på användning

- **Initial plan**: Reseagenten skapar en initial plan baserat på klientens preferenser för sightseeing och en budget på $2000.
- **Förfinad plan**: Reseagenten itererar planen och optimerar för klientens preferenser och budget.

Genom att starta planen med ett tydligt mål (t.ex. att maximera klientens nöjdhet) och iterera för att förfina planen kan reseagenten skapa en skräddarsydd och optimerad reseplan för klienten. Denna metod säkerställer att reseplanen är anpassad till klientens preferenser och budget från början och förbättras med varje iteration.

### Utnyttja LLM för omrankning och poängsättning

Stora språkmodeller (LLM) kan användas för omrankning och poängsättning genom att utvärdera relevansen och kvaliteten på hämtade dokument eller genererade svar. Så här fungerar det:

**Hämtning:** Det första steget hämtar en uppsättning kandidater (dokument eller svar) baserat på frågan.

**Omrankning:** LLM utvärderar dessa kandidater och omrankar dem baserat på deras relevans och kvalitet. Detta steg säkerställer att den mest relevanta och högkvalitativa informationen presenteras först.

**Poängsättning:** LLM tilldelar poäng till varje kandidat som reflekterar deras relevans och kvalitet. Detta hjälper till att välja det bästa svaret eller dokumentet för användaren.

Genom att utnyttja LLM för omrankning och poängsättning kan systemet ge mer exakt och kontextuellt relevant information, vilket förbättrar den övergripande användarupplevelsen.

#### Scenario - Resor baserat på preferenser

En reseagent vill rekommendera de bästa resmålen till en klient baserat på deras preferenser. LLM kommer att hjälpa till att omrankera och poängsätta destinationerna för att säkerställa att de mest relevanta alternativen presenteras.

#### Steg:

1. Samla in användarens preferenser.
2. Hämta en lista över potentiella resmål.
3. Använd LLM för att omrankera och poängsätta destinationerna baserat på användarens preferenser.

#### Kodförklaring - Preference Booker

1. **Initialisering**: Klassen `TravelAgent` initialiseras med en lista över potentiella resmål, där varje resmål har attribut som namn och beskrivning.

2. **Hämta rekommendationer (`get_recommendations`-metoden)**: Denna metod genererar en prompt för Azure OpenAI-tjänsten baserat på användarens preferenser och gör en HTTP POST-förfrågan till Azure OpenAI API för att få omrankerade och poängsatta destinationer.

3. **Generera prompt (`generate_prompt`-metoden)**: Denna metod konstruerar en prompt för Azure OpenAI, inklusive användarens preferenser och listan över destinationer. Prompten guidar modellen att omrankera och poängsätta destinationerna baserat på de angivna preferenserna.

4. **API-anrop**: Biblioteket `requests` används för att göra en HTTP POST-förfrågan till Azure OpenAI API-slutpunkten. Svaret innehåller de omrankade och poängsatta destinationerna.

5. **Exempel på användning**: Reseagenten samlar in användarens preferenser (t.ex. intresse för sightseeing och mångkulturell upplevelse) och använder Azure OpenAI-tjänsten för att få omrankade och poängsatta rekommendationer för resmål.

Genom att utnyttja LLM för omrankning och poängsättning kan reseagenten ge mer personliga och relevanta reseförslag till klienter, vilket förbättrar deras övergripande upplevelse.

### RAG: Promptteknik vs Verktyg

Retrieval-Augmented Generation (RAG) kan vara både en promptteknik och ett verktyg vid utveckling av AI-agenter. Att förstå skillnaden mellan de två kan hjälpa dig att utnyttja RAG mer effektivt i dina projekt.

#### RAG som promptteknik

**Vad är det?**

- Som en promptteknik innebär RAG att formulera specifika frågor eller prompts för att styra hämtningen av relevant information från en stor databas eller corpus. Denna information används sedan för att generera svar eller åtgärder.

#### RAG som verktyg

**Vad är det?**

- Som ett verktyg är RAG ett integrerat system som automatiserar hämtning och generering, vilket gör det enklare för utvecklare att implementera komplexa AI-funktioner utan att manuellt skapa prompts för varje fråga.

### Jämförelse

| Aspekt                 | Promptteknik                                              | Verktyg                                                |
|------------------------|-----------------------------------------------------------|-------------------------------------------------------|
| **Manuell vs Automatisk**| Manuell formulering av prompts för varje fråga.           | Automatiserad process för hämtning och generering.    |
| **Kontroll**            | Ger mer kontroll över hämtningen.                         | Strömlinjeformar och automatiserar processen.         |
| **Flexibilitet**        | Möjliggör anpassade prompts baserat på specifika behov.   | Mer effektivt för storskaliga implementationer.       |
| **Komplexitet**         | Kräver skapande och justering av prompts.                 | Lättare att integrera i en AI-agents arkitektur.      |

### Utvärdera relevans

Att utvärdera relevans är en viktig aspekt av AI-agentens prestanda. Det säkerställer att informationen som hämtas och genereras av agenten är lämplig, korrekt och användbar för användaren. Låt oss utforska hur man utvärderar relevans i AI-agenter, inklusive praktiska exempel och tekniker.

#### Viktiga koncept för att utvärdera relevans

1. **Kontextmedvetenhet**:
   - Agenten måste förstå kontexten för användarens fråga för att hämta och generera relevant information.
   - Exempel: Om en användare frågar efter "bästa restauranger i Paris" bör agenten ta hänsyn till användarens preferenser, såsom typ av mat och budget.

2. **Noggrannhet**:
   - Informationen som tillhandahålls av agenten bör vara faktamässigt korrekt och aktuell.
   - Exempel: Rekommendera restauranger som är öppna och har bra recensioner istället för föråldrade eller stängda alternativ.

3. **Användarens avsikt**:
   - Agenten bör tolka användarens avsikt bakom frågan för att ge den mest relevanta informationen.
   - Exempel: Om en användare frågar efter "prisvärda hotell" bör agenten prioritera prisvärda alternativ.

4. **Feedbackloop**:
   - Kontinuerlig insamling och analys av användarfeedback hjälper agenten att förbättra sin process för att utvärdera relevans.
   - Exempel: Inkludera användarbetyg och feedback på tidigare rekommendationer för att förbättra framtida svar.

#### Praktiska tekniker för att utvärdera relevans

1. **Relevanspoäng**:
   - Tilldela en relevanspoäng till varje hämtat objekt baserat på hur väl det matchar användarens fråga och preferenser.

2. **Filtrering och rankning**:
   - Filtrera bort irrelevanta objekt och rangordna de återstående baserat på deras relevanspoäng.

3. **NLP (Natural Language Processing)**:
   - Använd NLP-tekniker för att förstå användarens fråga och hämta relevant information.

4. **Integrering av användarfeedback**:
   - Samla in användarfeedback om de tillhandahållna rekommendationerna och använd den för att justera framtida relevansutvärderingar.

#### Exempel: Utvärdera relevans i reseagent

Här är ett praktiskt exempel på hur en reseagent kan utvärdera relevansen av reseförslag:

### Sökning med avsikt

Att söka med avsikt innebär att förstå och tolka det underliggande syftet eller målet bakom en användares fråga för att hämta och generera den mest relevanta och användbara informationen. Denna metod går bortom att bara matcha nyckelord och fokuserar på att förstå användarens faktiska behov och kontext.

#### Viktiga koncept för sökning med avsikt

1. **Förstå användarens avsikt**:
   - Användarens avsikt kan kategoriseras i tre huvudtyper: informativ, navigerande och transaktionell.
     - **Informativ avsikt**: Användaren söker information om ett ämne (t.ex. "Vilka är de bästa museerna i Paris?").
     - **Navigerande avsikt**: Användaren vill navigera till en specifik webbplats eller sida (t.ex. "Louvren officiella webbplats").
     - **Transaktionell avsikt**: Användaren vill utföra en transaktion, såsom att boka en flygresa eller göra ett köp (t.ex. "Boka en flygresa till Paris").

2. **Kontextmedvetenhet**:
   - Att analysera kontexten för användarens fråga hjälper till att identifiera deras avsikt korrekt. Detta inkluderar att ta hänsyn till tidigare interaktioner, användarpreferenser och specifika detaljer i den aktuella frågan.

3. **NLP (Natural Language Processing)**:
   - NLP-tekniker används för att förstå och tolka de naturliga språkfrågor som användare tillhandahåller. Detta inkluderar uppgifter som entitetsigenkänning, sentimentanalys och frågeparsing.

4. **Personalisering**:
   - Att anpassa sökresultaten baserat på användarens historik, preferenser och feedback förbättrar relevansen av den information som hämtas.
#### Praktiskt Exempel: Söka med Avsikt i Resebyrå

Låt oss ta Resebyrå som ett exempel för att se hur sökning med avsikt kan implementeras.

1. **Samla Användarpreferenser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Förstå Användarens Avsikt**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kontekstkännedom**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Sök och Anpassa Resultat**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Exempel på Användning**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Generera Kod som ett Verktyg

Kodgenererande agenter använder AI-modeller för att skriva och köra kod, lösa komplexa problem och automatisera uppgifter.

### Kodgenererande Agenter

Kodgenererande agenter använder generativa AI-modeller för att skriva och köra kod. Dessa agenter kan lösa komplexa problem, automatisera uppgifter och ge värdefulla insikter genom att generera och köra kod på olika programmeringsspråk.

#### Praktiska Användningsområden

1. **Automatisk Kodgenerering**: Generera kodsnuttar för specifika uppgifter, som dataanalys, webbsökning eller maskininlärning.
2. **SQL som en RAG**: Använd SQL-frågor för att hämta och manipulera data från databaser.
3. **Problemlösning**: Skapa och köra kod för att lösa specifika problem, som att optimera algoritmer eller analysera data.

#### Exempel: Kodgenererande Agent för Dataanalys

Föreställ dig att du designar en kodgenererande agent. Så här kan det fungera:

1. **Uppgift**: Analysera en dataset för att identifiera trender och mönster.
2. **Steg**:
   - Ladda datasetet i ett dataanalysverktyg.
   - Generera SQL-frågor för att filtrera och aggregera data.
   - Kör frågorna och hämta resultaten.
   - Använd resultaten för att skapa visualiseringar och insikter.
3. **Nödvändiga Resurser**: Tillgång till datasetet, dataanalysverktyg och SQL-funktioner.
4. **Erfarenhet**: Använd tidigare analysresultat för att förbättra noggrannheten och relevansen i framtida analyser.

### Exempel: Kodgenererande Agent för Resebyrå

I detta exempel designar vi en kodgenererande agent, Resebyrå, för att hjälpa användare att planera sina resor genom att generera och köra kod. Denna agent kan hantera uppgifter som att hämta resealternativ, filtrera resultat och skapa en resplan med hjälp av generativ AI.

#### Översikt av den Kodgenererande Agenten

1. **Samla Användarpreferenser**: Samlar in användarens input som destination, resedatum, budget och intressen.
2. **Generera Kod för att Hämta Data**: Genererar kodsnuttar för att hämta data om flyg, hotell och sevärdheter.
3. **Köra Genererad Kod**: Kör den genererade koden för att hämta information i realtid.
4. **Generera Resplan**: Sammanställer den hämtade datan till en personlig resplan.
5. **Justera Baserat på Feedback**: Tar emot användarfeedback och genererar om koden vid behov för att förbättra resultaten.

#### Steg-för-Steg Implementering

1. **Samla Användarpreferenser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generera Kod för att Hämta Data**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Köra Genererad Kod**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Generera Resplan**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Justera Baserat på Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Utnyttja Miljömedvetenhet och Resonemang

Att basera frågegenereringsprocessen på tabellens schema kan förbättra processen genom att utnyttja miljömedvetenhet och resonemang.

Här är ett exempel på hur detta kan göras:

1. **Förstå Schemat**: Systemet förstår tabellens schema och använder denna information för att grunda frågegenereringen.
2. **Justera Baserat på Feedback**: Systemet justerar användarpreferenser baserat på feedback och resonerar kring vilka fält i schemat som behöver uppdateras.
3. **Generera och Köra Frågor**: Systemet genererar och kör frågor för att hämta uppdaterad flyg- och hotellinformation baserat på de nya preferenserna.

Här är ett uppdaterat Python-exempel som inkluderar dessa koncept:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Förklaring - Bokning Baserad på Feedback

1. **Schema Medvetenhet**: `schema`-ordlistan definierar hur preferenser ska justeras baserat på feedback. Den inkluderar fält som `favorites` och `avoid` med motsvarande justeringar.
2. **Justera Preferenser (`adjust_based_on_feedback`-metod)**: Denna metod justerar preferenser baserat på användarfeedback och schemat.
3. **Miljöbaserade Justeringar (`adjust_based_on_environment`-metod)**: Denna metod anpassar justeringarna baserat på schemat och feedback.
4. **Generera och Köra Frågor**: Systemet genererar kod för att hämta uppdaterad flyg- och hotellinformation baserat på de justerade preferenserna och simulerar körningen av dessa frågor.
5. **Generera Resplan**: Systemet skapar en uppdaterad resplan baserat på den nya flyg-, hotell- och sevärdhetsinformationen.

Genom att göra systemet miljömedvetet och resonera baserat på schemat kan det generera mer exakta och relevanta frågor, vilket leder till bättre reseförslag och en mer personlig användarupplevelse.

### Använda SQL som en Retrieval-Augmented Generation (RAG)-Teknik

SQL (Structured Query Language) är ett kraftfullt verktyg för att interagera med databaser. När det används som en del av en Retrieval-Augmented Generation (RAG)-metod kan SQL hämta relevant data från databaser för att informera och generera svar eller åtgärder i AI-agenter. Låt oss utforska hur SQL kan användas som en RAG-teknik i kontexten av Resebyrå.

#### Nyckelkoncept

1. **Databasinteraktion**:
   - SQL används för att fråga databaser, hämta relevant information och manipulera data.
   - Exempel: Hämta flyginformation, hotelluppgifter och sevärdheter från en resedatabas.

2. **Integration med RAG**:
   - SQL-frågor genereras baserat på användarinput och preferenser.
   - Den hämtade datan används sedan för att generera personliga rekommendationer eller åtgärder.

3. **Dynamisk Frågegenerering**:
   - AI-agenten genererar dynamiska SQL-frågor baserat på kontext och användarbehov.
   - Exempel: Anpassa SQL-frågor för att filtrera resultat baserat på budget, datum och intressen.

#### Användningsområden

- **Automatisk Kodgenerering**: Generera kodsnuttar för specifika uppgifter.
- **SQL som en RAG**: Använd SQL-frågor för att manipulera data.
- **Problemlösning**: Skapa och köra kod för att lösa problem.

**Exempel**:
En dataanalysagent:

1. **Uppgift**: Analysera en dataset för att hitta trender.
2. **Steg**:
   - Ladda datasetet.
   - Generera SQL-frågor för att filtrera data.
   - Kör frågorna och hämta resultaten.
   - Generera visualiseringar och insikter.
3. **Resurser**: Datasetåtkomst, SQL-funktioner.
4. **Erfarenhet**: Använd tidigare resultat för att förbättra framtida analyser.

#### Praktiskt Exempel: Använda SQL i Resebyrå

1. **Samla Användarpreferenser**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generera SQL-frågor**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Köra SQL-frågor**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Generera Rekommendationer**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Exempel på SQL-frågor

1. **Flygfråga**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotellfråga**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Sevärdhetsfråga**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Genom att använda SQL som en del av Retrieval-Augmented Generation (RAG)-tekniken kan AI-agenter som Resebyrå dynamiskt hämta och använda relevant data för att ge exakta och personliga rekommendationer.

### Exempel på Metakognition

För att demonstrera en implementering av metakognition, låt oss skapa en enkel agent som *reflekterar över sin beslutsprocess* medan den löser ett problem. I detta exempel bygger vi ett system där en agent försöker optimera valet av hotell, men sedan utvärderar sitt eget resonemang och justerar sin strategi när den gör fel eller suboptimala val.

#### Hur detta illustrerar metakognition:

1. **Initialt Beslut**: Agenten väljer det billigaste hotellet utan att förstå kvalitetsaspekten.
2. **Reflektion och Utvärdering**: Efter det initiala valet kontrollerar agenten om hotellet är ett "dåligt" val baserat på användarfeedback. Om kvaliteten är för låg reflekterar den över sitt resonemang.
3. **Justera Strategi**: Agenten justerar sin strategi baserat på reflektionen och byter från "billigast" till "högsta kvalitet", vilket förbättrar dess beslutsprocess i framtida iterationer.

Här är ett exempel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agentens Metakognitiva Förmågor

Nyckeln här är agentens förmåga att:
- Utvärdera sina tidigare val och beslutsprocess.
- Justera sin strategi baserat på den reflektionen, dvs. metakognition i praktiken.

Detta är en enkel form av metakognition där systemet kan justera sitt resonemang baserat på intern feedback.

### Slutsats

Metakognition är ett kraftfullt verktyg som kan förbättra AI-agenters kapacitet avsevärt. Genom att inkludera metakognitiva processer kan du designa agenter som är mer intelligenta, anpassningsbara och effektiva. Använd de ytterligare resurserna för att utforska den fascinerande världen av metakognition i AI-agenter.

### Har du Fler Frågor om Metakognitionsdesignmönstret?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Föregående Lektion

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Nästa Lektion

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.