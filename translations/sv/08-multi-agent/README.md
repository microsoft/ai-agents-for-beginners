<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T15:24:46+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "sv"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.sv.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Mönster för multi-agentdesign

Så snart du börjar arbeta med ett projekt som involverar flera agenter, behöver du överväga mönstret för multi-agentdesign. Det är dock inte alltid självklart när man ska byta till multi-agenter och vilka fördelarna är.

## Introduktion

I denna lektion försöker vi besvara följande frågor:

- Vilka scenarier är lämpliga för multi-agenter?
- Vilka är fördelarna med att använda multi-agenter istället för en enda agent som utför flera uppgifter?
- Vilka är byggstenarna för att implementera mönstret för multi-agentdesign?
- Hur kan vi få insyn i hur flera agenter interagerar med varandra?

## Lärandemål

Efter denna lektion ska du kunna:

- Identifiera scenarier där multi-agenter är tillämpliga.
- Känna igen fördelarna med att använda multi-agenter jämfört med en enda agent.
- Förstå byggstenarna för att implementera mönstret för multi-agentdesign.

Vad är den större bilden?

*Multi-agenter är ett designmönster som gör det möjligt för flera agenter att samarbeta för att uppnå ett gemensamt mål.*

Detta mönster används flitigt inom olika områden, inklusive robotik, autonoma system och distribuerad databehandling.

## Scenarier där multi-agenter är tillämpliga

Så vilka scenarier är lämpliga för att använda multi-agenter? Svaret är att det finns många scenarier där det är fördelaktigt att använda flera agenter, särskilt i följande fall:

- **Stora arbetsbelastningar**: Stora arbetsbelastningar kan delas upp i mindre uppgifter och tilldelas olika agenter, vilket möjliggör parallell bearbetning och snabbare slutförande. Ett exempel på detta är vid bearbetning av stora datamängder.
- **Komplexa uppgifter**: Komplexa uppgifter, precis som stora arbetsbelastningar, kan delas upp i mindre deluppgifter och tilldelas olika agenter som är specialiserade på specifika aspekter av uppgiften. Ett bra exempel är autonoma fordon där olika agenter hanterar navigation, hinderdetektion och kommunikation med andra fordon.
- **Mångsidig expertis**: Olika agenter kan ha olika expertis, vilket gör att de kan hantera olika aspekter av en uppgift mer effektivt än en enda agent. Ett bra exempel är inom sjukvården där agenter kan hantera diagnostik, behandlingsplaner och patientövervakning.

## Fördelar med att använda multi-agenter jämfört med en enda agent

Ett system med en enda agent kan fungera bra för enkla uppgifter, men för mer komplexa uppgifter kan användningen av flera agenter ge flera fördelar:

- **Specialisering**: Varje agent kan specialiseras för en specifik uppgift. Brist på specialisering i en enda agent innebär att du har en agent som kan göra allt men som kan bli förvirrad när den ställs inför en komplex uppgift. Den kan till exempel utföra en uppgift som den inte är bäst lämpad för.
- **Skalbarhet**: Det är enklare att skala system genom att lägga till fler agenter istället för att överbelasta en enda agent.
- **Feltolerans**: Om en agent misslyckas kan andra fortsätta att fungera, vilket säkerställer systemets tillförlitlighet.

Låt oss ta ett exempel: låt oss boka en resa för en användare. Ett system med en enda agent skulle behöva hantera alla aspekter av bokningsprocessen, från att hitta flyg till att boka hotell och hyrbilar. För att uppnå detta med en enda agent skulle agenten behöva ha verktyg för att hantera alla dessa uppgifter. Detta skulle kunna leda till ett komplext och monolitiskt system som är svårt att underhålla och skala. Ett system med flera agenter, å andra sidan, skulle kunna ha olika agenter specialiserade på att hitta flyg, boka hotell och hyrbilar. Detta skulle göra systemet mer modulärt, lättare att underhålla och skalbart.

Jämför detta med en resebyrå som drivs som en liten familjefirma kontra en resebyrå som drivs som en franchise. Familjefirman skulle ha en enda agent som hanterar alla aspekter av bokningsprocessen, medan franchisen skulle ha olika agenter som hanterar olika aspekter av bokningsprocessen.

## Byggstenar för att implementera mönstret för multi-agentdesign

Innan du kan implementera mönstret för multi-agentdesign behöver du förstå byggstenarna som utgör mönstret.

Låt oss göra detta mer konkret genom att återigen titta på exemplet med att boka en resa för en användare. I detta fall skulle byggstenarna inkludera:

- **Agentkommunikation**: Agenter för att hitta flyg, boka hotell och hyrbilar behöver kommunicera och dela information om användarens preferenser och begränsningar. Du behöver bestämma protokoll och metoder för denna kommunikation. Konkret innebär detta att agenten för att hitta flyg behöver kommunicera med agenten för att boka hotell för att säkerställa att hotellet är bokat för samma datum som flyget. Det innebär att agenterna behöver dela information om användarens resedatum, vilket innebär att du behöver bestämma *vilka agenter som delar information och hur de delar information*.
- **Koordineringsmekanismer**: Agenter behöver koordinera sina handlingar för att säkerställa att användarens preferenser och begränsningar uppfylls. En användarpreferens kan vara att de vill ha ett hotell nära flygplatsen, medan en begränsning kan vara att hyrbilar endast är tillgängliga vid flygplatsen. Detta innebär att agenten för att boka hotell behöver koordinera med agenten för att boka hyrbilar för att säkerställa att användarens preferenser och begränsningar uppfylls. Detta innebär att du behöver bestämma *hur agenterna koordinerar sina handlingar*.
- **Agentarkitektur**: Agenter behöver ha en intern struktur för att fatta beslut och lära sig av sina interaktioner med användaren. Detta innebär att agenten för att hitta flyg behöver ha en intern struktur för att fatta beslut om vilka flyg som ska rekommenderas till användaren. Detta innebär att du behöver bestämma *hur agenterna fattar beslut och lär sig av sina interaktioner med användaren*. Exempel på hur en agent lär sig och förbättras kan vara att agenten för att hitta flyg använder en maskininlärningsmodell för att rekommendera flyg till användaren baserat på deras tidigare preferenser.
- **Insyn i multi-agentinteraktioner**: Du behöver ha insyn i hur flera agenter interagerar med varandra. Detta innebär att du behöver ha verktyg och tekniker för att spåra agenters aktiviteter och interaktioner. Detta kan vara i form av loggnings- och övervakningsverktyg, visualiseringsverktyg och prestationsmått.
- **Multi-agentmönster**: Det finns olika mönster för att implementera multi-agentsystem, såsom centraliserade, decentraliserade och hybrida arkitekturer. Du behöver bestämma vilket mönster som bäst passar ditt användningsfall.
- **Människa i loopen**: I de flesta fall kommer du att ha en människa i loopen och du behöver instruera agenterna när de ska be om mänsklig intervention. Detta kan vara i form av att en användare ber om ett specifikt hotell eller flyg som agenterna inte har rekommenderat eller ber om bekräftelse innan de bokar ett flyg eller hotell.

## Insyn i multi-agentinteraktioner

Det är viktigt att du har insyn i hur flera agenter interagerar med varandra. Denna insyn är avgörande för felsökning, optimering och för att säkerställa systemets övergripande effektivitet. För att uppnå detta behöver du ha verktyg och tekniker för att spåra agenters aktiviteter och interaktioner. Detta kan vara i form av loggnings- och övervakningsverktyg, visualiseringsverktyg och prestationsmått.

Till exempel, i fallet med att boka en resa för en användare, kan du ha en instrumentpanel som visar statusen för varje agent, användarens preferenser och begränsningar samt interaktionerna mellan agenter. Denna instrumentpanel kan visa användarens resedatum, flyg som rekommenderas av flygagenten, hotell som rekommenderas av hotellagenten och hyrbilar som rekommenderas av hyrbilsagenten. Detta skulle ge dig en tydlig bild av hur agenterna interagerar med varandra och om användarens preferenser och begränsningar uppfylls.

Låt oss titta närmare på dessa aspekter.

- **Loggnings- och övervakningsverktyg**: Du vill ha loggning för varje åtgärd som en agent utför. En loggpost kan innehålla information om vilken agent som utförde åtgärden, vilken åtgärd som utfördes, tidpunkten för åtgärden och resultatet av åtgärden. Denna information kan sedan användas för felsökning, optimering och mer.

- **Visualiseringsverktyg**: Visualiseringsverktyg kan hjälpa dig att se interaktionerna mellan agenter på ett mer intuitivt sätt. Till exempel kan du ha en graf som visar informationsflödet mellan agenter. Detta kan hjälpa dig att identifiera flaskhalsar, ineffektivitet och andra problem i systemet.

- **Prestationsmått**: Prestationsmått kan hjälpa dig att spåra effektiviteten hos multi-agentsystemet. Till exempel kan du spåra tiden det tar att slutföra en uppgift, antalet uppgifter som slutförs per tidsenhet och noggrannheten i de rekommendationer som agenterna ger. Denna information kan hjälpa dig att identifiera förbättringsområden och optimera systemet.

## Multi-agentmönster

Låt oss dyka in i några konkreta mönster vi kan använda för att skapa multi-agentapplikationer. Här är några intressanta mönster värda att överväga:

### Gruppchatt

Detta mönster är användbart när du vill skapa en gruppchattapplikation där flera agenter kan kommunicera med varandra. Typiska användningsfall för detta mönster inkluderar teamarbete, kundsupport och sociala nätverk.

I detta mönster representerar varje agent en användare i gruppchatten, och meddelanden utbyts mellan agenter med hjälp av ett meddelandeprotokoll. Agenterna kan skicka meddelanden till gruppchatten, ta emot meddelanden från gruppchatten och svara på meddelanden från andra agenter.

Detta mönster kan implementeras med en centraliserad arkitektur där alla meddelanden dirigeras genom en central server, eller en decentraliserad arkitektur där meddelanden utbyts direkt.

![Gruppchatt](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.sv.png)

### Överlämning

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan överlämna uppgifter till varandra.

Typiska användningsfall för detta mönster inkluderar kundsupport, uppgiftshantering och arbetsflödesautomation.

I detta mönster representerar varje agent en uppgift eller ett steg i ett arbetsflöde, och agenter kan överlämna uppgifter till andra agenter baserat på fördefinierade regler.

![Överlämning](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.sv.png)

### Samarbetsfiltrering

Detta mönster är användbart när du vill skapa en applikation där flera agenter kan samarbeta för att ge rekommendationer till användare.

Varför du skulle vilja att flera agenter samarbetar är för att varje agent kan ha olika expertis och kan bidra till rekommendationsprocessen på olika sätt.

Låt oss ta ett exempel där en användare vill ha en rekommendation om den bästa aktien att köpa på aktiemarknaden.

- **Branschexpert**: En agent kan vara expert inom en specifik bransch.
- **Teknisk analys**: En annan agent kan vara expert på teknisk analys.
- **Fundamental analys**: Och en annan agent kan vara expert på fundamental analys. Genom att samarbeta kan dessa agenter ge en mer omfattande rekommendation till användaren.

![Rekommendation](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.sv.png)

## Scenario: Återbetalningsprocess

Tänk på ett scenario där en kund försöker få en återbetalning för en produkt. Det kan finnas ganska många agenter involverade i denna process, men låt oss dela upp det mellan agenter som är specifika för denna process och generella agenter som kan användas i andra processer.

**Agenter specifika för återbetalningsprocessen**:

Följande är några agenter som kan vara involverade i återbetalningsprocessen:

- **Kundagent**: Denna agent representerar kunden och är ansvarig för att initiera återbetalningsprocessen.
- **Säljaragent**: Denna agent representerar säljaren och är ansvarig för att behandla återbetalningen.
- **Betalningsagent**: Denna agent representerar betalningsprocessen och är ansvarig för att återbetala kundens betalning.
- **Lösningsagent**: Denna agent representerar lösningsprocessen och är ansvarig för att lösa eventuella problem som uppstår under återbetalningsprocessen.
- **Efterlevnadsagent**: Denna agent representerar efterlevnadsprocessen och är ansvarig för att säkerställa att återbetalningsprocessen följer regler och policyer.

**Generella agenter**:

Dessa agenter kan användas av andra delar av din verksamhet.

- **Fraktagent**: Denna agent representerar fraktprocessen och är ansvarig för att skicka tillbaka produkten till säljaren. Denna agent kan användas både för återbetalningsprocessen och för generell frakt av en produkt, till exempel vid ett köp.
- **Feedbackagent**: Denna agent representerar feedbackprocessen och är ansvarig för att samla in feedback från kunden. Feedback kan samlas in när som helst och inte bara under återbetalningsprocessen.
- **Eskaleringsagent**: Denna agent representerar eskaleringsprocessen och är ansvarig för att eskalera problem till en högre supportnivå. Du kan använda denna typ av agent för vilken process som helst där du behöver eskalera ett problem.
- **Notifieringsagent**: Denna agent representerar notifieringsprocessen och är ansvarig för att skicka notifieringar till kunden vid olika stadier av återbetalningsprocessen.
- **Analysagent**: Denna agent representerar analysprocessen och är ansvarig för att analysera data relaterad till återbetalningsprocessen.
- **Revisionsagent**: Denna agent representerar revisionsprocessen och är ansvarig för att granska återbetalningsprocessen för att säkerställa att den genomförs korrekt.
- **Rapporteringsagent**: Denna agent representerar rapporteringsprocessen och är ansvarig för att generera rapporter om återbetalningsprocessen.
- **Kunskapsagent**: Denna agent representerar kunskapsprocessen och är ansvarig för att underhålla en kunskapsbas med information relaterad till återbetalningsprocessen. Denna agent kan vara kunnig både om återbetalningar och andra delar av din verksamhet.
- **Säkerhetsagent**: Denna agent representerar säkerhetsprocessen och är ansvarig för att säkerställa säkerheten i återbetalningsprocessen.
- **Kvalitetsagent**: Denna agent representerar kvalitetsprocessen och är ansvarig för att säkerställa kvaliteten i återbetalningsprocessen.

Det finns ganska många agenter listade ovan, både för den specifika återbetalningsprocessen och för de generella agenter som kan användas i andra delar av din verksamhet. Förhoppningsvis ger detta dig en idé om hur du kan bestämma vilka agenter som ska användas i ditt multi-agentsystem.

## Uppgift
## Designa ett multi-agent-system för en kundsupportprocess. Identifiera de agenter som är involverade i processen, deras roller och ansvar, samt hur de interagerar med varandra. Tänk på både agenter som är specifika för kundsupportprocessen och generella agenter som kan användas i andra delar av verksamheten.

> Fundera innan du läser lösningen nedan, du kanske behöver fler agenter än du tror.

> TIP: Tänk på de olika stegen i kundsupportprocessen och överväg också agenter som behövs för något system.

## Lösning

[Lösning](./solution/solution.md)

## Kunskapskontroller

Fråga: När bör du överväga att använda multi-agenter?

- [ ] A1: När du har en liten arbetsbelastning och en enkel uppgift.
- [ ] A2: När du har en stor arbetsbelastning.
- [ ] A3: När du har en enkel uppgift.

[Lösning quiz](./solution/solution-quiz.md)

## Sammanfattning

I den här lektionen har vi tittat på multi-agent-designmönstret, inklusive de scenarier där multi-agenter är tillämpliga, fördelarna med att använda multi-agenter jämfört med en enskild agent, byggstenarna för att implementera multi-agent-designmönstret och hur man får insyn i hur de olika agenterna interagerar med varandra.

### Har du fler frågor om Multi-Agent Designmönstret?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra elever, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- 

## Föregående lektion

[Planeringsdesign](../07-planning-design/README.md)

## Nästa lektion

[Metakognition i AI-agenter](../09-metacognition/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.