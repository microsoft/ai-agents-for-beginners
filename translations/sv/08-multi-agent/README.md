[![Multi-Agent Design](../../../translated_images/sv/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

# Multi-agent designmönster

Så fort du börjar arbeta på ett projekt som involverar flera agenter behöver du överväga multi-agent designmönster. Det kanske dock inte är omedelbart tydligt när man ska byta till multi-agenter och vilka fördelarna är.

## Introduktion

I denna lektion försöker vi besvara följande frågor:

- Vilka scenarier är multi-agenter tillämpliga på?
- Vilka är fördelarna med att använda multi-agenter jämfört med att ha en enda agent som utför flera uppgifter?
- Vilka är byggstenarna för att implementera multi-agent designmönster?
- Hur får vi insyn i hur de flera agenterna interagerar med varandra?

## Lärandemål

Efter denna lektion bör du kunna:

- Identifiera scenarier där multi-agenter är tillämpliga
- Känna igen fördelarna med att använda multi-agenter jämfört med en enda agent.
- Förstå byggstenarna för att implementera multi-agent designmönster.

Vad är den större bilden?

*Multi-agenter är ett designmönster som tillåter flera agenter att arbeta tillsammans för att uppnå ett gemensamt mål*.

Detta mönster används i stor utsträckning inom olika områden, inklusive robotik, autonoma system och distribuerad databehandling.

## Scenarier där multi-agenter är tillämpliga

Så vilka scenarier är en bra användning för multi-agenter? Svaret är att det finns många scenarier där det är fördelaktigt att använda flera agenter, särskilt i följande fall:

- **Stora arbetsbelastningar**: Stora arbetsbelastningar kan delas upp i mindre uppgifter och tilldelas olika agenter, vilket möjliggör parallell bearbetning och snabbare slutförande. Ett exempel på detta är vid en stor databehandlingsuppgift.
- **Komplexa uppgifter**: Komplexa uppgifter, likt stora arbetsbelastningar, kan brytas ned i mindre deluppgifter och tilldelas olika agenter, där varje agent är specialiserad på en specifik aspekt av uppgiften. Ett bra exempel är i autonoma fordon där olika agenter hanterar navigation, hinderupptäckt och kommunikation med andra fordon.
- **Mångsidig expertis**: Olika agenter kan ha mångsidig expertis, vilket gör att de kan hantera olika aspekter av en uppgift mer effektivt än en enda agent. För detta är ett bra exempel inom sjukvård där agenter kan hantera diagnostik, behandlingsplaner och patientövervakning.

## Fördelar med att använda multi-agenter jämfört med en enda agent

Ett system med en enda agent kan fungera väl för enkla uppgifter, men för mer komplexa uppgifter kan användningen av flera agenter ge flera fördelar:

- **Specialisering**: Varje agent kan vara specialiserad på en specifik uppgift. Brist på specialisering i en enda agent innebär att du har en agent som kan göra allt men som kan bli förvirrad om vad den ska göra när den möter en komplex uppgift. Den kan till exempel sluta med att göra en uppgift som den inte är bäst lämpad för.
- **Skalbarhet**: Det är lättare att skala system genom att lägga till fler agenter snarare än att överbelasta en enda agent.
- **Fel tolerans**: Om en agent misslyckas kan andra fortsätta fungera, vilket säkerställer systemets tillförlitlighet.

Låt oss ta ett exempel, låt oss boka en resa för en användare. Ett system med en enda agent skulle behöva hantera alla aspekter av resebokningsprocessen, från att hitta flyg till att boka hotell och hyrbilar. För att uppnå detta med en enda agent skulle agenten behöva ha verktyg för att hantera alla dessa uppgifter. Detta kan leda till ett komplext och monolitiskt system som är svårt att underhålla och skala. Ett multi-agent system, å andra sidan, kan ha olika agenter specialiserade på att hitta flyg, boka hotell och hyrbilar. Detta skulle göra systemet mer modulärt, lättare att underhålla och skalbart.

Jämför detta med en resebyrå som drivs som en kvartersbutik kontra en resebyrå som drivs som en franchise. Kvartersbutiken skulle ha en enda agent som hanterar alla aspekter av resebokningsprocessen, medan franchisen skulle ha olika agenter som hanterar olika delar av processen.

## Byggstenar för att implementera multi-agent designmönster

Innan du kan implementera multi-agent designmönster behöver du förstå byggstenarna som utgör mönstret.

Låt oss göra detta mer konkret genom att återigen titta på exemplet att boka en resa för en användare. I detta fall skulle byggstenarna inkludera:

- **Agentkommunikation**: Agenter för att hitta flyg, boka hotell och hyrbilar måste kommunicera och dela information om användarens preferenser och begränsningar. Du behöver bestämma protokoll och metoder för denna kommunikation. Vad detta konkret betyder är att agenten för att hitta flyg måste kommunicera med agenten för att boka hotell för att säkerställa att hotellet bokas för samma datum som flyget. Det innebär att agenterna behöver dela information om användarens resdatum, vilket betyder att du behöver bestämma *vilka agenter som delar information och hur de delar information*.
- **Koordinationsmekanismer**: Agenter måste koordinera sina handlingar för att säkerställa att användarens preferenser och begränsningar uppfylls. En användarpreferens kan vara att de vill ha ett hotell nära flygplatsen medan en begränsning kan vara att hyrbilar endast är tillgängliga på flygplatsen. Det betyder att agenten för att boka hotell måste koordinera med agenten för att boka hyrbil för att säkerställa att användarens preferenser och begränsningar uppfylls. Detta innebär att du behöver bestämma *hur agenterna koordinerar sina handlingar*.
- **Agentarkitektur**: Agenter måste ha en intern struktur för att fatta beslut och lära sig från sina interaktioner med användaren. Detta betyder att agenten för att hitta flyg måste ha en intern struktur för att fatta beslut om vilka flyg som ska rekommenderas till användaren. Detta innebär att du behöver bestämma *hur agenterna fattar beslut och lär sig från sina interaktioner med användaren*. Exempel på hur en agent lär sig och förbättras kan vara att agenten för att hitta flyg kan använda en maskininlärningsmodell för att rekommendera flyg till användaren baserat på deras tidigare preferenser.
- **Insyn i multi-agent interaktioner**: Du behöver ha insyn i hur flera agenter interagerar med varandra. Detta betyder att du behöver ha verktyg och tekniker för att spåra agenters aktiviteter och interaktioner. Detta kan vara i form av logg- och övervakningsverktyg, visualiseringsverktyg och prestandamått.
- **Multi-agentmönster**: Det finns olika mönster för att implementera multi-agent system, såsom centraliserade, decentraliserade och hybrida arkitekturer. Du behöver bestämma det mönster som bäst passar ditt användningsfall.
- **Människa i loopen**: I de flesta fallen kommer du att ha en människa i loopen och du behöver instruera agenterna när de ska be om mänsklig intervention. Detta kan ske i form av att en användare efterfrågar ett specifikt hotell eller flyg som agenterna inte har rekommenderat eller att be om bekräftelse innan bokning av flyg eller hotell.

## Insyn i multi-agent interaktioner

Det är viktigt att du har insyn i hur flera agenter interagerar med varandra. Denna insyn är avgörande för felsökning, optimering och för att säkerställa systemets övergripande effektivitet. För att uppnå detta behöver du ha verktyg och tekniker för att spåra agenters aktiviteter och interaktioner. Detta kan vara i form av logg- och övervakningsverktyg, visualiseringsverktyg och prestandamått.

Till exempel, vid bokning av en resa för en användare, kan du ha en instrumentpanel som visar statusen för varje agent, användarens preferenser och begränsningar samt interaktionerna mellan agenterna. Denna instrumentpanel kan visa användarens resedatum, flygen som rekommenderas av flygagenten, hotellen som rekommenderas av hotelagenten och hyrbilarna som rekommenderas av hyrbilsagenten. Detta skulle ge dig en tydlig bild av hur agenterna interagerar med varandra och om användarens preferenser och begränsningar uppfylls.

Låt oss titta närmare på var och en av dessa aspekter.

- **Logg- och övervakningsverktyg**: Du vill ha loggning för varje åtgärd som en agent utför. En loggpost kan lagra information om agenten som utförde åtgärden, åtgärden som utfördes, tiden för åtgärden och resultatet av åtgärden. Denna information kan sedan användas för felsökning, optimering och mer.

- **Visualiseringsverktyg**: Visualiseringsverktyg kan hjälpa dig att se interaktionerna mellan agenter på ett mer intuitivt sätt. Till exempel kan du ha en graf som visar informationsflödet mellan agenter. Detta kan hjälpa dig att identifiera flaskhalsar, ineffektivitet och andra problem i systemet.

- **Prestandamått**: Prestandamått kan hjälpa dig att följa effektiviteten hos multi-agent systemet. Till exempel kan du spåra tiden som krävs för att slutföra en uppgift, antalet uppgifter slutförda per tidsenhet och noggrannheten i rekommendationerna som görs av agenterna. Denna information kan hjälpa dig att identifiera förbättringsområden och optimera systemet.

## Multi-agentmönster

Låt oss dyka in i några konkreta mönster som vi kan använda för att skapa multi-agent-appar. Här är några intressanta mönster värda att överväga:

### Gruppchatt

Detta mönster är användbart när du vill skapa en gruppchattapplikation där flera agenter kan kommunicera med varandra. Typiska användningsområden för detta mönster inkluderar teamarbete, kundsupport och sociala nätverk.

I detta mönster representerar varje agent en användare i gruppchatten, och meddelanden utbyts mellan agenter med hjälp av ett meddelandeprotokoll. Agenterna kan skicka meddelanden till gruppchatten, ta emot meddelanden från gruppchatten och svara på meddelanden från andra agenter.

Detta mönster kan implementeras med en centraliserad arkitektur där alla meddelanden dirigeras genom en central server, eller en decentraliserad arkitektur där meddelanden utbyts direkt.

![Group chat](../../../translated_images/sv/multi-agent-group-chat.ec10f4cde556babd.webp)

### Överlämning

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan överlämna uppgifter till varandra.

Typiska användningsområden för detta mönster inkluderar kundsupport, uppgiftshantering och automatisering av arbetsflöden.

I detta mönster representerar varje agent en uppgift eller ett steg i ett arbetsflöde, och agenter kan överlämna uppgifter till andra agenter baserat på fördefinierade regler.

![Hand off](../../../translated_images/sv/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbetsfiltrering

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan samarbeta för att göra rekommendationer till användare.

Varför du vill att flera agenter ska samarbeta är för att varje agent kan ha olika expertis och kan bidra till rekommendationsprocessen på olika sätt.

Låt oss ta ett exempel där en användare vill ha rekommendation på den bästa aktien att köpa på aktiemarknaden.

- **Branschexpert**: En agent kan vara expert inom en specifik bransch.
- **Teknisk analys**: En annan agent kan vara expert på teknisk analys.
- **Fundamental analys**: och en annan agent kan vara expert på fundamental analys. Genom att samarbeta kan dessa agenter ge en mer heltäckande rekommendation till användaren.

![Recommendation](../../../translated_images/sv/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Återbetalningsprocess

Tänk på ett scenario där en kund försöker få återbetalning för en produkt, det kan finnas ganska många agenter involverade i denna process men låt oss dela upp dem mellan agenter som är specifika för denna process och generella agenter som kan användas i andra processer.

**Agenter specifika för återbetalningsprocessen**:

Följande är några agenter som kan vara inblandade i återbetalningsprocessen:

- **Kundagent**: Denna agent representerar kunden och är ansvarig för att initiera återbetalningsprocessen.
- **Säljaragent**: Denna agent representerar säljaren och är ansvarig för att behandla återbetalningen.
- **Betalningsagent**: Denna agent representerar betalningsprocessen och är ansvarig för att återbetala kundens betalning.
- **Lösningsagent**: Denna agent representerar lösningsprocessen och är ansvarig för att lösa eventuella problem som uppstår under återbetalningsprocessen.
- **Efterlevnadsagent**: Denna agent representerar efterlevnadsprocessen och är ansvarig för att säkerställa att återbetalningsprocessen följer regler och policyer.

**Generella agenter**:

Dessa agenter kan användas av andra delar av din verksamhet.

- **Fraktagent**: Denna agent representerar fraktprocessen och är ansvarig för att skicka produkten tillbaka till säljaren. Denna agent kan användas både för återbetalningsprocessen och för allmän frakt av en produkt via ett köp till exempel.
- **Feedbackagent**: Denna agent representerar feedbackprocessen och är ansvarig för att samla in feedback från kunden. Feedback kan ges när som helst och inte bara under återbetalningsprocessen.
- **Eskaleringsagent**: Denna agent representerar eskaleringsprocessen och är ansvarig för att eskalera problem till en högre supportnivå. Du kan använda denna typ av agent för vilken process som helst där du behöver eskalera ett problem.
- **Notifieringsagent**: Denna agent representerar notifieringsprocessen och är ansvarig för att skicka aviseringar till kunden vid olika stadier av återbetalningsprocessen.
- **Analyseragent**: Denna agent representerar analysprocessen och är ansvarig för att analysera data relaterad till återbetalningsprocessen.
- **Revisionsagent**: Denna agent representerar revisionsprocessen och är ansvarig för att granska återbetalningsprocessen för att säkerställa att den genomförs korrekt.
- **Rapporteringsagent**: Denna agent representerar rapporteringsprocessen och är ansvarig för att skapa rapporter om återbetalningsprocessen.
- **Kunskapsagent**: Denna agent representerar kunskapsprocessen och är ansvarig för att underhålla en kunskapsbas med information relaterad till återbetalningsprocessen. Denna agent kan vara kunnig både om återbetalningar och andra delar av din verksamhet.
- **Säkerhetsagent**: Denna agent representerar säkerhetsprocessen och är ansvarig för att säkerställa säkerheten i återbetalningsprocessen.
- **Kvalitetsagent**: Denna agent representerar kvalitetsprocessen och är ansvarig för att säkerställa kvaliteten i återbetalningsprocessen.

Det finns ganska många agenter listade ovan både för den specifika återbetalningsprocessen men också för de generella agenter som kan användas i andra delar av din verksamhet. Förhoppningsvis ger detta dig en idé om hur du kan bestämma vilka agenter du ska använda i ditt multi-agent system.

## Uppgift

Designa ett multi-agent system för en kundsupportprocess. Identifiera agenterna som är involverade i processen, deras roller och ansvar, och hur de interagerar med varandra. Överväg både agenter som är specifika för kundsupportprocessen och generella agenter som kan användas i andra delar av din verksamhet.
> Tänk efter innan du läser följande lösning, du kan behöva fler agenter än du tror.

> TIPS: Tänk på de olika etapperna i kundsupportprocessen och fundera också på agenter som behövs för något system.

## Lösning

[Lösning](./solution/solution.md)

## Kunskapskontroller

Fråga: När bör du överväga att använda flera agenter?

- [ ] A1: När du har en liten arbetsbelastning och en enkel uppgift.
- [ ] A2: När du har en stor arbetsbelastning
- [ ] A3: När du har en enkel uppgift.

[Lösningsquiz](./solution/solution-quiz.md)

## Sammanfattning

I denna lektion har vi tittat på mönstret för flera agenter, inklusive de scenarier där flera agenter är tillämpliga, fördelarna med att använda flera agenter istället för en enskild agent, byggstenarna för att implementera mönstret för flera agenter och hur man får insyn i hur de flera agenterna interagerar med varandra.

### Fler frågor om mönstret för flera agenter?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra lärande, delta i kontorstider och få dina frågor om AI-agenter besvarade.

## Ytterligare resurser

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiska designmönster</a>

## Föregående lektion

[Planeringsdesign](../07-planning-design/README.md)

## Nästa lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->