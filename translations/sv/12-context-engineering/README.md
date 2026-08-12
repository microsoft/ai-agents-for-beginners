# Kontektsengineering för AI-agenter

[![Kontektsengineering](../../../translated_images/sv/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

Att förstå komplexiteten i den applikation du bygger en AI-agent för är viktigt för att skapa en pålitlig sådan. Vi behöver bygga AI-agenter som effektivt hanterar information för att möta komplexa behov bortom promptengineering.

I denna lektion kommer vi att titta på vad kontektsengineering är och dess roll i att bygga AI-agenter.

## Introduktion

Denna lektion kommer att täcka:

• **Vad kontektsengineering är** och varför det skiljer sig från promptengineering.

• **Strategier för effektiv kontektsengineering**, inklusive hur man skriver, väljer, komprimerar och isolerar information.

• **Vanliga kontextfel** som kan spåra ur din AI-agent och hur man åtgärdar dem.

## Läromål

Efter att ha genomfört denna lektion kommer du att förstå hur du:

• **Definierar kontektsengineering** och skiljer det från promptengineering.

• **Identifierar de viktigaste komponenterna av kontext** i applikationer för Large Language Models (LLM).

• **Tillämpa strategier för att skriva, välja, komprimera och isolera kontext** för att förbättra agentens prestanda.

• **Känna igen vanliga kontextfel** såsom förgiftning, distraktion, förvirring och krockar, och implementera tekniker för att mildra dem.

## Vad är kontektsengineering?

För AI-agenter är kontext det som styr planeringen för att AI-agenten ska utföra vissa handlingar. Kontektsengineering är praktiken att säkerställa att AI-agenten har rätt information för att slutföra nästa steg i uppgiften. Kontextfönstret är begränsat i storlek, så som agentbyggare måste vi skapa system och processer för att hantera tillägg, borttagning och kondensering av information i kontextfönstret.

### Promptengineering vs kontektsengineering

Promptengineering fokuserar på en enda uppsättning statiska instruktioner för att effektivt styra AI-agenter med ett regelverk. Kontektsengineering handlar om att hantera en dynamisk informationsuppsättning, inklusive den initiala prompten, för att säkerställa att AI-agenten har vad den behöver över tid. Huvudidén med kontektsengineering är att göra denna process upprepbar och pålitlig.

### Typer av kontext

[![Typer av kontext](../../../translated_images/sv/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Det är viktigt att komma ihåg att kontext inte är bara en sak. Informationen som AI-agenten behöver kan komma från olika källor och det är upp till oss att säkerställa att agenten har tillgång till dessa källor:

De typer av kontext som en AI-agent kan behöva hantera inkluderar:

• **Instruktioner:** Dessa är som agentens "regler" – prompts, systemmeddelanden, få-skott-exempel (som visar AI hur man gör något) och beskrivningar av verktyg den kan använda. Här kombineras fokus för promptengineering med kontektsengineering.

• **Kunskap:** Detta omfattar fakta, information hämtad från databaser eller långtidsminnen som agenten samlat på sig. Detta inkluderar integration av ett Retrieval Augmented Generation (RAG)-system om en agent behöver tillgång till olika kunskapslager och databaser.

• **Verktyg:** Dessa är definitioner av externa funktioner, API:er och MCP-servrar som agenten kan anropa, samt den feedback (resultat) den får från att använda dem.

• **Konversationshistorik:** Den pågående dialogen med en användare. Med tiden blir dessa samtal längre och mer komplexa, vilket innebär att de tar upp plats i kontextfönstret.

• **Användarpreferenser:** Information som lärs in om en användares tycken eller dislike över tid. Dessa kan lagras och anropas vid nyckelbeslut för att hjälpa användaren.

## Strategier för effektiv kontektsengineering

### Planeringsstrategier

[![Bästa praxis för kontektsengineering](../../../translated_images/sv/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

God kontektsengineering börjar med god planering. Här är ett tillvägagångssätt som hjälper dig att börja tänka på hur du kan tillämpa konceptet kontektsengineering:

1. **Definiera tydliga resultat** - Resultatet av de uppgifter som AI-agenterna ska tilldelas bör definieras tydligt. Svara på frågan - "Hur kommer världen att se ut när AI-agenten är klar med sin uppgift?" Med andra ord, vilken förändring, information eller respons bör användaren ha efter interaktionen med AI-agenten.
2. **Kartlägg kontexten** - När du väl definierat resultaten för AI-agenten behöver du svara på frågan "Vilken information behöver AI-agenten för att slutföra denna uppgift?". På så sätt kan du börja kartlägga kontexten för var den informationen kan hittas.
3. **Skapa kontextpipelines** - Nu när du vet var informationen finns behöver du svara på frågan "Hur kommer agenten att få denna information?". Detta kan göras på flera sätt inklusive RAG, användning av MCP-servrar och andra verktyg.

### Praktiska strategier

Planering är viktigt men när informationen börjar flöda in i vår agents kontextfönster behöver vi praktiska strategier för att hantera det:

#### Hantera kontext

Medan viss information läggs till i kontextfönstret automatiskt handlar kontektsengineering om att ta en mer aktiv roll i denna information, vilket kan göras med några strategier:

 1. **Agentens anteckningsfält**
 Detta möjliggör för en AI-agent att anteckna relevant information om pågående uppgifter och användarinteraktioner under en enskild session. Detta bör finnas utanför kontextfönstret i en fil eller runtime-objekt som agenten senare kan hämta under denna session om det behövs.

 2. **Minnen**
 Anteckningsfälten är bra för att hantera information utanför kontextfönstret för en enskild session. Minnen möjliggör för agenter att lagra och hämta relevant information över flera sessioner. Detta kan inkludera sammanfattningar, användarpreferenser och feedback för framtida förbättringar.

 3. **Komprimering av kontext**
  När kontextfönstret växer och närmar sig sin gräns kan tekniker som summering och beskärning användas. Det innebär att man antingen behåller endast den mest relevanta informationen eller tar bort äldre meddelanden.
  
 4. **Multi-agent system**
  Att utveckla multi-agent system är en form av kontektsengineering eftersom varje agent har sitt eget kontextfönster. Hur den kontexten delas och överförs till olika agenter är en annan sak att planera när man bygger dessa system.
  
 5. **Sandbox-miljöer**
  Om en agent behöver köra en kod eller bearbeta stora mängder information i ett dokument kan detta kräva många tokens för att bearbeta resultaten. Istället för att ha allt detta lagrat i kontextfönstret kan agenten använda en sandbox-miljö som kan köra denna kod och endast läsa resultaten och annan relevant information.
  
 6. **Runtime state-objekt**
   Detta görs genom att skapa informationsbehållare för att hantera situationer när agenten behöver ha tillgång till viss information. För en komplex uppgift möjliggör detta att agenten lagrar resultaten för varje deluppgift steg för steg, vilket låter kontexten förbli kopplad endast till just den specifika deluppgiften.

#### Inspektera kontext

Efter att du tillämpat en av dessa strategier är det värt att kontrollera vad nästa modellanrop faktiskt mottog. En användbar felsökningsfråga är:

> Laddade agenten för mycket kontext, fel kontext eller saknade den kontext den behövde?

Du behöver inte logga råa prompts, verktygsutdata eller minnesinnehåll för att svara på den frågan. I produktion föredrar du små kontextinspektionsposter som fångar antal, id:n, hashar och policyrubriker:

- **Urval:** Spåra hur många potentiella delar, verktyg eller minnen som övervägdes, hur många som valdes ut och vilken regel eller poäng som orsakade att övriga filtrerades bort.
- **Komprimering:** Registrera källområdet eller spår-id, sammanfattningsid, uppskattat antal tokens före och efter komprimering samt om det råa innehållet exkluderades från nästa anrop.
- **Isolering:** Notera vilken deluppgift som kördes i en separat agent, session eller sandbox, vilken begränsad sammanfattning som returnerades och om stora verktygsresultat hölls utanför föräldragents kontext.
- **Minne och RAG:** Spara hämtade dokument-id:n, minnes-id:n, poäng, valda id:n och redigeringsstatus istället för full text.
- **Säkerhet och integritet:** Föredra hashar, id:n, tokenhinkar och policyrubriker framför känslig prompttext, verktygsargument, verktygsresultat eller användarminnesinnehåll.

Målet är inte att behålla mer kontext. Det är att lämna tillräckligt med bevis så att en utvecklare kan avgöra vilken kontextstrategi som kördes och om den ändrade nästa modellanrop på avsett sätt.

### Exempel på kontektsengineering

Låt oss säga att vi vill att en AI-agent ska **"Boka en resa till Paris åt mig."**

• En enkel agent som bara använder promptengineering kan bara svara: **"Okej, när vill du åka till Paris?**". Den bearbetade bara din direkta fråga vid den tidpunkt användaren ställde den.

• En agent som använder kontektsengineeringstrategierna som behandlats skulle göra mycket mer. Innan den ens svarar kan dess system:

  ◦ **Kontrollera din kalender** för lediga datum (hämta realtidsdata).

 ◦ **Minnas tidigare resepreferenser** (från långtidsminnet) som ditt föredragna flygbolag, budget eller om du föredrar direktflyg.

 ◦ **Identifiera tillgängliga verktyg** för flyg- och hotellbokning.

- Sedan kan ett exempel på svar vara: "Hej [Ditt namn]! Jag ser att du är ledig första veckan i oktober. Ska jag leta efter direktflyg till Paris med [föredraget flygbolag] inom din vanliga budget på [budget]?". Detta rikare, kontextmedvetna svar visar kraften i kontektsengineering.

## Vanliga kontextfel

### Kontekstförgiftning

**Vad det är:** När en hallucination (felaktig information genererad av LLM) eller ett fel kommer in i kontexten och refereras till upprepade gånger, vilket gör att agenten strävar efter omöjliga mål eller utvecklar nonsensstrategier.

**Vad man ska göra:** Implementera **kontextvalidering** och **karantän**. Validera information innan den läggs till i långtidsminnet. Om potentiell förgiftning upptäcks, starta nya kontexttrådar för att förhindra att den dåliga informationen sprids.

**Exempel på resebokning:** Din agent hallucinerar ett **direktflyg från en liten lokal flygplats till en avlägsen internationell stad** som faktiskt inte erbjuder internationella flyg. Denna icke-existerande flyginformation sparas i kontexten. Senare, när du ber agenten boka, fortsätter den att försöka hitta biljetter för denna omöjliga rutt, vilket leder till upprepade fel.

**Lösning:** Implementera ett steg som **validerar flygningarnas existens och rutter med ett realtids-API** _innan_ flyginformationen läggs till i agentens arbetskontext. Om valideringen misslyckas sätts den felaktiga informationen i "karantän" och används inte vidare.

### Kontextdistraktion

**Vad det är:** När kontexten blir så stor att modellen fokuserar för mycket på det ackumulerade historiken istället för att använda det den lärt sig under träning, vilket leder till repetitiva eller oanvändbara handlingar. Modeller kan börja göra misstag även innan kontextfönstret är fullt.

**Vad man ska göra:** Använd **kontextsummering**. Komprimera periodvis ackumulerad information till kortare sammanfattningar, behåll viktiga detaljer medan redundanta historik tas bort. Detta hjälper till att "återställa" fokus.

**Exempel på resebokning:** Du har diskuterat olika drömresmål länge, inklusive en detaljerad berättelse om din backpackingresa för två år sedan. När du slutligen säger **"hitta mig ett billigt flyg för nästa månad,"** fastnar agenten i gamla, irrelevanta detaljer och fortsätter fråga om din backpackingutrustning eller tidigare resplaner, medan den ignorerar din aktuella begäran.

**Lösning:** Efter ett visst antal turer eller när kontexten blir för stor bör agenten **sammanfatta de senaste och mest relevanta delarna av samtalet** – med fokus på dina aktuella resdatum och resmål – och använda den kondenserade sammanfattningen för nästa LLM-anrop, samtidigt som mindre relevant historik slängs.

### Kontextförvirring

**Vad det är:** När onödig kontext, ofta i form av för många tillgängliga verktyg, gör att modellen genererar dåliga svar eller anropar irrelevanta verktyg. Mindre modeller är särskilt utsatta för detta.

**Vad man ska göra:** Implementera **verktygshantering** med hjälp av RAG-tekniker. Spara verktygsbeskrivningar i en vektordatabas och välj _endast_ de mest relevanta verktygen för varje specifik uppgift. Forskning visar att begränsa verktyg till färre än 30 är effektivt.

**Exempel på resebokning:** Din agent har tillgång till dussintals verktyg: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` osv. Du frågar, **"Vad är bästa sättet att ta sig runt i Paris?"** På grund av det stora antalet verktyg blir agenten förvirrad och försöker anropa `book_flight` _inom_ Paris, eller `rent_car` trots att du föredrar kollektivtrafik, eftersom verktygsbeskrivningarna kan överlappa eller modellen helt enkelt inte kan avgöra det bästa.

**Lösning:** Använd **RAG över verktygsbeskrivningarna**. När du frågar om att ta sig runt i Paris hämtar systemet dynamiskt _endast_ de mest relevanta verktygen som `rent_car` eller `public_transport_info` baserat på din fråga, och presenterar en fokuserad "loadout" av verktyg till LLM.

### Kontektskrock

**Vad det är:** När motstridig information finns inom kontexten, vilket leder till inkonsekvent resonemang eller dåliga slutliga svar. Detta händer ofta när information kommer i omgångar och tidiga felaktiga antaganden kvarstår i kontexten.

**Vad man ska göra:** Använd **kontextbeskärning** och **avlastning**. Beskärning innebär att ta bort föråldrad eller motstridig information när nya detaljer anländer. Avlastning ger modellen en separat "anteckningsyta" för att bearbeta information utan att störa huvudkontexten.


**Exempel på resebokning:** Du berättar initialt för din agent, **"Jag vill flyga ekonomiklass."** Senare i samtalet ändrar du dig och säger, **"Egentligen, för denna resa, låt oss ta business class."** Om båda instruktionerna finns kvar i kontexten kan agenten få motstridiga sökresultat eller bli förvirrad om vilken preferens som ska prioriteras.

**Lösning:** Implementera **kontextbeskärning**. När en ny instruktion motsäger en gammal, tas den äldre instruktionen bort eller skrivs uttryckligen över i kontexten. Alternativt kan agenten använda en **anteckningsbok** för att förena motstridiga preferenser innan beslut fattas, vilket säkerställer att endast den slutliga, konsekventa instruktionen styr dess handlingar.

## Har du fler frågor om kontextteknik?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstid och få svar på dina AI Agents-frågor.
## Föregående lektion

[Agentic Protocols](../11-agentic-protocols/README.md)

## Nästa lektion

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->