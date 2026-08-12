[![Multi-agent design](../../../translated_images/sv/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klicka på bilden ovan för att se video av denna lektion)_

# Multi-agent designmönster

Så snart du börjar arbeta med ett projekt som involverar flera agenter behöver du överväga multi-agent designmönster. Det kan dock inte vara omedelbart tydligt när man ska övergå till multi-agenter och vilka fördelarna är.

## Introduktion

I denna lektion försöker vi besvara följande frågor:

- Vilka scenarier är multi-agenter tillämpliga för?
- Vilka är fördelarna med att använda multi-agenter jämfört med en enskild agent som utför flera uppgifter?
- Vilka är byggstenarna för att implementera multi-agent designmönstret?
- Hur får vi insyn i hur flera agenter interagerar med varandra?

## Inlärningsmål

Efter denna lektion bör du kunna:

- Identifiera scenarier där multi-agenter är tillämpliga
- Känna igen fördelarna med att använda multi-agenter jämfört med en enskild agent.
- Förstå byggstenarna för att implementera multi-agent designmönstret.

Vad är den större bilden?

*Multi-agenter är ett designmönster som tillåter flera agenter att arbeta tillsammans för att uppnå ett gemensamt mål*.

Detta mönster används i stor utsträckning inom olika områden, inklusive robotik, autonoma system och distribuerad databehandling.

## Scenarier där multi-agenter är tillämpliga

Så vilka scenarier är ett bra användningsfall för att använda multi-agenter? Svaret är att det finns många scenarier där användning av flera agenter är fördelaktigt, särskilt i följande fall:

- **Stora arbetsbelastningar**: Stora arbetsbelastningar kan delas upp i mindre uppgifter och tilldelas olika agenter, vilket möjliggör parallell bearbetning och snabbare avslut. Ett exempel på detta är vid en stor datahanteringsuppgift.
- **Komplexa uppgifter**: Komplexa uppgifter, likt stora arbetsbelastningar, kan brytas ner i mindre deluppgifter och tilldelas olika agenter, som var och en specialiserar sig på en specifik del av uppgiften. Ett bra exempel är autonoma fordon där olika agenter hanterar navigation, hinderupptäckt och kommunikation med andra fordon.
- **Mångsidig expertis**: Olika agenter kan ha olika expertis, vilket gör att de effektivare kan hantera olika aspekter av en uppgift jämfört med en enda agent. Ett bra exempel för detta är inom vården där agenter kan hantera diagnostik, behandlingsplaner och patientövervakning.

## Fördelar med att använda multi-agenter jämfört med en enskild agent

Ett system med en enskild agent kan fungera bra för enkla uppgifter, men för mer komplexa uppgifter kan användning av flera agenter erbjuda flera fördelar:

- **Specialisering**: Varje agent kan vara specialiserad på en specifik uppgift. Brist på specialisering i en enda agent innebär att agenten kan göra allt men kan bli förvirrad över vad den ska göra när den ställs inför en komplex uppgift. Den kan till exempel sluta med att utföra en uppgift den inte är bäst lämpad för.
- **Skalbarhet**: Det är lättare att skala system genom att lägga till fler agenter än att överbelasta en enda agent.
- **Felförtålighet**: Om en agent misslyckas kan de andra fortsätta fungera och säkerställa systemets tillförlitlighet.

Låt oss ta ett exempel: boka en resa för en användare. Ett system med en enda agent skulle behöva hantera alla aspekter av resebokningsprocessen, från att hitta flyg till att boka hotell och hyrbilar. För att uppnå detta med en enda agent skulle agenten behöva ha verktyg för att hantera alla dessa uppgifter. Detta kan leda till ett komplext och monolitiskt system som är svårt att underhålla och skala. Ett multi-agent system, å andra sidan, kan ha olika agenter specialiserade på att hitta flyg, boka hotell och hyrbilar. Detta skulle göra systemet mer modulärt, lättare att underhålla och skalbart.

Jämför detta med en resebyrå som drivs som en småskalig butik jämfört med en resebyrå som drivs som en franchise. Småbutiken skulle ha en enda agent som hanterar alla aspekter av resebokningsprocessen, medan franchisen skulle ha olika agenter som hanterar olika delar av processen.

## Byggstenar för att implementera multi-agent designmönstret

Innan du kan implementera multi-agent designmönstret behöver du förstå byggstenarna som utgör mönstret.

Låt oss göra detta mer konkret genom att återigen titta på exemplet att boka en resa för en användare. I detta fall skulle byggstenarna inkludera:

- **Agentkommunikation**: Agenter för att hitta flyg, boka hotell och hyrbilar behöver kommunicera och dela information om användarens preferenser och begränsningar. Du behöver bestämma protokoll och metoder för denna kommunikation. Konkret betyder detta att agenten för att hitta flyg behöver kommunicera med agenten för hotellbokning för att säkerställa att hotellet bokas för samma datum som flyget. Det innebär att agenterna behöver dela information om användarens resedatum, vilket betyder att du behöver bestämma *vilka agenter som delar information och hur de delar den*.
- **Koordinationsmekanismer**: Agenter behöver koordinera sina handlingar för att säkerställa att användarens preferenser och begränsningar uppfylls. En användarpreferens kan vara att de vill ha ett hotell nära flygplatsen medan en begränsning kan vara att hyrbilar bara finns tillgängliga på flygplatsen. Detta innebär att agenten för hotellbokning behöver koordinera med agenten för hyrbilar för att säkerställa att användarens preferenser och begränsningar uppfylls. Det innebär att du behöver bestämma *hur agenterna koordinerar sina handlingar*.
- **Agentarkitektur**: Agenter behöver ha intern struktur för att fatta beslut och lära sig från sina interaktioner med användaren. Detta betyder att agenten för att hitta flyg behöver ha en intern struktur för att fatta beslut om vilka flyg som ska rekommenderas till användaren. Det betyder att du behöver bestämma *hur agenterna fattar beslut och lär sig av sina interaktioner med användaren*. Exempel på hur en agent lär sig och förbättras kan vara att agenten för att hitta flyg använder en maskininlärningsmodell för att rekommendera flyg baserat på användarens tidigare preferenser.
- **Insyn i multi-agent-interaktioner**: Du behöver ha insyn i hur flera agenter interagerar med varandra. Detta betyder att du behöver verktyg och tekniker för att spåra agentaktiviteter och interaktioner. Detta kan vara i form av loggning och övervakningsverktyg, visualiseringsverktyg och prestationsmått.
- **Multi-agent-mönster**: Det finns olika mönster för att implementera multi-agent system, såsom centraliserad, decentraliserad och hybridarkitektur. Du behöver bestämma vilket mönster som passar bäst för ditt användningsfall.
- **Människa i loopen**: I de flesta fall kommer du ha en människa i loopen och du behöver instruera agenterna när de ska be om mänsklig intervention. Detta kan vara i form av att en användare efterfrågar ett specifikt hotell eller flyg som agenterna inte rekommenderat eller begär bekräftelse innan en flyg- eller hotellbokning görs.

## Insyn i multi-agent-interaktioner

Det är viktigt att du har insyn i hur flera agenter interagerar med varandra. Denna insyn är avgörande för felsökning, optimering och att säkerställa systemets övergripande effektivitet. För att uppnå detta behöver du verktyg och tekniker för att spåra agenters aktiviteter och interaktioner. Detta kan vara i form av loggnings- och övervakningsverktyg, visualiseringsverktyg och prestationsmått.

Till exempel, vid bokning av en resa för en användare, kan du ha en instrumentbräda som visar status för varje agent, användarens preferenser och begränsningar samt interaktionerna mellan agenter. Denna instrumentbräda kan visa användarens resedatum, de flyg som rekommenderas av flygagenten, de hotell som rekommenderas av hotellagenten och hyrbilar som rekommenderas av hyrbilsagenten. Detta skulle ge dig en tydlig bild av hur agenterna interagerar med varandra och om användarens preferenser och begränsningar uppfylls.

Låt oss titta närmare på varje aspekt.

- **Logg- och övervakningsverktyg**: Du vill logga varje åtgärd som en agent utför. En loggpost kan lagra information om agenten som utförde åtgärden, vilken åtgärd som utfördes, när den utfördes och resultatet av åtgärden. Denna information kan sedan användas för felsökning, optimering och mer.

- **Visualiseringsverktyg**: Visualiseringsverktyg kan hjälpa dig att se interaktionerna mellan agenter på ett mer intuitivt sätt. Till exempel kan du ha en graf som visar informationsflödet mellan agenter. Detta kan hjälpa dig att identifiera flaskhalsar, ineffektivitet och andra problem i systemet.

- **Prestationsmått**: Prestationsmått kan hjälpa dig att följa effektiviteten i multi-agent systemet. Till exempel kan du följa tiden det tar att slutföra en uppgift, antalet uppgifter som slutförs per tidsenhet och noggrannheten i de rekommendationer som agenterna ger. Denna information kan hjälpa dig att identifiera förbättringsområden och optimera systemet.

## Multi-agent-mönster

Låt oss dyka in i några konkreta mönster vi kan använda för att skapa multi-agent-appar. Här är några intressanta mönster värda att överväga:

### Gruppchatt

Detta mönster är användbart när du vill skapa en gruppchattapplikation där flera agenter kan kommunicera med varandra. Typiska användningsfall för detta mönster inkluderar teamarbete, kundsupport och sociala nätverk.

I detta mönster representerar varje agent en användare i gruppchatten, och meddelanden utbyts mellan agenter med hjälp av ett meddelandeprotokoll. Agenterna kan skicka meddelanden till gruppchatten, ta emot meddelanden från gruppchatten och svara på meddelanden från andra agenter.

Detta mönster kan implementeras med en centraliserad arkitektur där alla meddelanden går via en central server, eller en decentraliserad arkitektur där meddelanden utbyts direkt.

![Group chat](../../../translated_images/sv/multi-agent-group-chat.ec10f4cde556babd.webp)

### Överlämning

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan överlämna uppgifter till varandra.

Typiska användningsfall för detta mönster inkluderar kundsupport, uppgiftshantering och arbetsflödesautomatisering.

I detta mönster representerar varje agent en uppgift eller ett steg i ett arbetsflöde, och agenter kan överlämna uppgifter till andra agenter baserat på fördefinierade regler.

![Hand off](../../../translated_images/sv/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbetsfiltrering

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan samarbeta för att ge rekommendationer till användare.

Anledningen till att man vill att flera agenter ska samarbeta är att varje agent kan ha olika expertis och kan bidra till rekommendationsprocessen på olika sätt.

Låt oss ta ett exempel där en användare vill ha en rekommendation på den bästa aktien att köpa på börsen.

- **Branchexpert**: En agent kan vara expert inom en specifik bransch.
- **Teknisk analys**: En annan agent kan vara expert på teknisk analys.
- **Fundamental analys**: och en annan agent kan vara expert på fundamental analys. Genom att samarbeta kan dessa agenter ge en mer heltäckande rekommendation till användaren.

![Recommendation](../../../translated_images/sv/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Återbetalningsprocess

Tänk på ett scenario där en kund försöker få en återbetalning för en produkt. Det kan finnas ganska många agenter involverade i denna process, men låt oss dela upp det mellan agenter specifika för denna process och generella agenter som kan användas i andra processer.

**Agenter specifika för återbetalningsprocessen**:

Följande är några agenter som kan vara involverade i återbetalningsprocessen:

- **Kundagent**: Denna agent representerar kunden och ansvarar för att initiera återbetalningsprocessen.
- **Säljagent**: Denna agent representerar säljaren och ansvarar för att behandla återbetalningen.
- **Betalningsagent**: Denna agent representerar betalningsprocessen och ansvarar för att återbetala kundens betalning.
- **Lösningsagent**: Denna agent representerar lösningsprocessen och ansvarar för att lösa eventuella problem som uppstår under återbetalningsprocessen.
- **Efterlevnadsagent**: Denna agent representerar efterlevnadsprocessen och ansvarar för att säkerställa att återbetalningsprocessen följer regler och riktlinjer.

**Generella agenter**:

Dessa agenter kan användas av andra delar av din verksamhet.

- **Fraktagent**: Denna agent representerar fraktprocessen och ansvarar för att skicka tillbaka produkten till säljaren. Denna agent kan användas både för återbetalningsprocessen och för generell frakt av en produkt vid köp, till exempel.
- **Feedbackagent**: Denna agent representerar feedbackprocessen och ansvarar för att samla in feedback från kunden. Feedback kan samlas in när som helst och inte bara under återbetalningsprocessen.
- **Eskaleringsagent**: Denna agent representerar eskaleringsprocessen och ansvarar för att eskalera problem till en högre supportnivå. Denna typ av agent kan användas för vilken process som helst där du behöver eskalera ett problem.
- **Notifikationsagent**: Denna agent representerar notifieringsprocessen och ansvarar för att skicka aviseringar till kunden vid olika steg i återbetalningsprocessen.
- **Analysagent**: Denna agent representerar analysprocessen och ansvarar för att analysera data relaterad till återbetalningsprocessen.
- **Revisionsagent**: Denna agent representerar revisionsprocessen och ansvarar för att revidera återbetalningsprocessen för att säkerställa att den utförs korrekt.
- **Rapporteringsagent**: Denna agent representerar rapporteringsprocessen och ansvarar för att generera rapporter om återbetalningsprocessen.
- **Kunskapsagent**: Denna agent representerar kunskapsprocessen och ansvarar för att underhålla en kunskapsdatabas med information relaterad till återbetalningsprocessen. Denna agent kan vara kunnig både om återbetalningar och andra delar av din verksamhet.
- **Säkerhetsagent**: Denna agent representerar säkerhetsprocessen och ansvarar för att säkerställa säkerheten i återbetalningsprocessen.
- **Kvalitetsagent**: Denna agent representerar kvalitetsprocessen och ansvarar för att säkerställa kvaliteten i återbetalningsprocessen.

Det finns ganska många agenter listade tidigare, både för den specifika återbetalningsprocessen och för de generella agenterna som kan användas i andra delar av din verksamhet. Förhoppningsvis ger detta dig en idé om hur du kan bestämma vilka agenter du ska använda i ditt multi-agent system.

## Uppgift

Designa ett multi-agent system för en kundsupportprocess. Identifiera vilka agenter som ingår i processen, deras roller och ansvar, samt hur de interagerar med varandra. Tänk på både agenter specifika för kundsupportprocessen och generella agenter som kan användas i andra delar av din verksamhet.


> Tänk efter innan du läser följande lösning, du kan behöva fler agenter än du tror.

> TIP: Tänk på de olika stegen i kundsupportprocessen och överväg också agenter som behövs för något system.

## Lösning

[Lösning](./solution/solution.md)

## Kunskapskontroller

### Fråga 1

Vilket scenario passar bäst för ett multi-agent-system?

- [ ] A1: En supportbot svarar på vanliga frågor med en kunskapsbas och en liten uppsättning verktyg.
- [ ] A2: Ett återbetalningsflöde kräver separata roller för bedrägeri, betalning och efterlevnad, var och en med sina egna verktyg, och deras resultat måste samordnas.
- [ ] A3: Samma enkla klassificeringsförfrågan kommer tusentals gånger i timmen.

### Fråga 2

När är en enskild agent vanligtvis det bättre valet?

- [ ] A1: Uppgiften kan hanteras med en uppsättning instruktioner och verktyg, utan specialistöverföringar.
- [ ] A2: Agenten har tillgång till mer än ett verktyg.
- [ ] A3: Arbetsflödet kräver separata roller med olika behörigheter och oberoende revisionsspår.

[Lösningsquiz](./solution/solution-quiz.md)

## Sammanfattning

I denna lektion har vi tittat på multi-agent-designmönstret, inklusive scenarier där multi-agenter är tillämpliga, fördelarna med att använda multi-agenter jämfört med en enskild agent, byggstenarna för att implementera multi-agent-designmönstret samt hur man kan få insyn i hur de flera agenterna interagerar med varandra.

### Fler frågor om Multi-Agent Designmönstret?

Anslut till [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att möta andra elever, delta i kontorstider och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework-dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiska designmönster</a>


## Föregående lektion

[Planeringsdesign](../07-planning-design/README.md)

## Nästa lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->