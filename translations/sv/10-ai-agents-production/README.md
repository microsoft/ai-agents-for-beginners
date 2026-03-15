# AI-agenter i produktion: Observabilitet & utvärdering

[![AI-agenter i produktion](../../../translated_images/sv/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

När AI-agenter går från experimentella prototyper till verkliga tillämpningar blir förmågan att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat viktig.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna/förstå:
- Kärnkoncept för agenters observabilitet och utvärdering
- Tekniker för att förbättra agenternas prestanda, kostnader och effektivitet
- Vad och hur du systematiskt utvärderar dina AI-agenter
- Hur du kontrollerar kostnader vid driftsättning av AI-agenter i produktion
- Hur man instrumenterar agenter byggda med Microsoft Agent Framework

Målet är att ge dig kunskapen för att förvandla dina 'svarta lådor'-agenter till transparenta, hanterbara och tillförlitliga system.

_**Note:** Det är viktigt att driftsätta AI-agenter som är säkra och pålitliga. Kolla även in lektionen [Bygga tillförlitliga AI-agenter](./06-building-trustworthy-agents/README.md)._ 

## Traces and Spans

Observabilitetsverktyg såsom [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar vanligtvis agentkörningar som traces och spans.

- **Trace** representerar en fullständig agentuppgift från start till mål (t.ex. hantering av en användarförfrågan).
- **Spans** är individuella steg inom tracen (t.ex. anrop till en språkmodell eller hämtning av data).

![Trace-träd i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Utan observabilitet kan en AI-agent kännas som en "black box" – dess interna tillstånd och resonemang är ogenomskinliga, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observabilitet blir agenterna "glassboxar" som erbjuder insyn som är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett. 

## Varför observabilitet är viktig i produktionsmiljöer

Att flytta AI-agenter till produktionsmiljöer inför nya utmaningar och krav. Observabilitet är inte längre något "trevligt att ha" utan en kritisk förmåga:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller ger ett oväntat resultat ger observabilitetsverktyg de spår som behövs för att lokalisera felets källa. Detta är särskilt viktigt i komplexa agenter som kan involvera flera LLM-anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens- och kostnadshantering**: AI-agenter förlitar sig ofta på LLM:er och andra externa API:er som debiteras per token eller per anrop. Observabilitet möjliggör noggrann spårning av dessa anrop och hjälper till att identifiera operationer som är överdrivet långsamma eller dyra. Detta gör det möjligt för team att optimera prompts, välja mer effektiva modeller eller designa om arbetsflöden för att hantera driftkostnader och säkerställa en bra användarupplevelse.
*   **Förtroende, säkerhet och efterlevnad**: I många tillämpningar är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observabilitet ger ett revisionsspår av agentens åtgärder och beslut. Detta kan användas för att upptäcka och mildra problem som prompt-injektion, generering av skadligt innehåll eller felaktig hantering av personligt identifierbar information (PII). Till exempel kan du granska spår för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringsslöjor**: Observabilitetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i verkliga världen kan team identifiera förbättringsområden, samla data för finjustering av modeller och validera effekten av förändringar. Detta skapar en återkopplingsslinga där produktionsinsikter från onlineutvärdering informerar offline-experiment och förfining, vilket leder till successivt bättre agentprestanda.

## Viktiga mätvärden att spåra

För att övervaka och förstå agenters beteende bör en rad mätvärden och signaler spåras. Specifika mätvärden kan variera beroende på agentens syfte, men några är universellt viktiga.

Här är några av de vanligaste mätvärden som observabilitetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och individuella steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modellanrop snabba upp genom att använda en snabbare modell eller genom att köra modellanrop parallellt.

**Kostnader:** Vad är kostnaden per agentkörning? AI-agenter förlitar sig på LLM-anrop som debiteras per token eller externa API:er. Frekvent verktygsanvändning eller flera prompts kan snabbt öka kostnaderna. Till exempel, om en agent anropar en LLM fem gånger för marginell kvalitetsförbättring måste du bedöma om kostnaden är motiverad eller om du kan minska antalet anrop eller använda en billigare modell. Realtidsövervakning kan också hjälpa till att identifiera oväntade toppar (t.ex. buggar som orsakar överdrivna API-loopar).

**Begäranfel:** Hur många förfrågningar misslyckades agenten med? Detta kan inkludera API-fel eller misslyckade verktygsanrop. För att göra din agent mer robust i produktion kan du då ställa in fallback-lösningar eller återförsök. T.ex. om LLM-leverantör A är nere, växlar du till LLM-leverantör B som backup.

**Användarfeedback:** Implementering av direkta användarutvärderingar ger värdefulla insikter. Detta kan inkludera explicita betyg (👍thumbs-up/👎down, ⭐1-5 stjärnor) eller textkommentarer. Konsekvent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat. 

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan explicita betyg. Detta kan inkludera omformulering av frågor direkt, upprepade förfrågningar eller att klicka på en försök-igen-knapp. T.ex. om du ser att användare upprepade gånger ställer samma fråga är detta ett tecken på att agenten inte fungerar som förväntat.

**Noggrannhet:** Hur ofta producerar agenten korrekta eller önskvärda resultat? Definitionen av noggrannhet varierar (t.ex. korrekt problemlösning, informationshämtningens precision, användarnöjdhet). Det första steget är att definiera vad framgång innebär för din agent. Du kan spåra noggrannhet via automatiska kontroller, utvärderingspoäng eller etiketter för uppgiftsgenomförande. Till exempel att markera spår som "succeeded" eller "failed". 

**Automatiserade utvärderingsmått:** Du kan också ställa in automatiska utvärderingar. Till exempel kan du använda en LLM för att poängsätta agentens output, t.ex. om den är hjälpsam, korrekt eller inte. Det finns även flera open source-bibliotek som hjälper dig att poängsätta olika aspekter av agenten. T.ex. [RAGAS](https://docs.ragas.io/) för RAG-agenter eller [LLM Guard](https://llm-guard.com/) för att upptäcka skadligt språk eller prompt-injektion. 

I praktiken ger en kombination av dessa mätvärden bäst täckning av en AI-agents hälsa. I detta kapitel kommer [exempel-notebooken](./code_samples/10-expense_claim-demo.ipynb) att visa hur dessa mätvärden ser ut i verkliga exempel men först ska vi lära oss hur ett typiskt utvärderingsflöde ser ut.

## Instrumentera din agent

För att samla spårningsdata måste du instrumentera din kod. Målet är att instrumentera agentkoden så att den skickar ut traces och mätvärden som kan fångas, bearbetas och visualiseras av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blivit en industristandard för LLM-observabilitet. Det tillhandahåller ett sett med API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata. 

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry-spans till ett observabilitetsverktyg. Microsoft Agent Framework integreras med OpenTelemetry inbyggt. Nedan är ett exempel på hur man instrumenterar en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens exekvering spåras automatiskt
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manuell skapande av spans:** Medan instrumenteringsbibliotek ger en bra grund finns det ofta fall där mer detaljerad eller anpassad information behövs. Du kan manuellt skapa spans för att lägga till anpassad applikationslogik. Viktigare är att de kan berika automatiskt eller manuellt skapade spans med egna attribut (även kända som taggar eller metadata). Dessa attribut kan inkludera affärsspecifik data, mellanliggande beräkningar eller annan kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id`, eller `model_version`.

Exempel på att skapa traces och spans manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentutvärdering

Observabilitet ger oss mätvärden, men utvärdering är processen att analysera den datan (och utföra tester) för att avgöra hur väl en AI-agent presterar och hur den kan förbättras. Med andra ord, när du har dessa traces och mätvärden, hur använder du dem för att bedöma agenten och fatta beslut? 

Regelbunden utvärdering är viktig eftersom AI-agenter ofta är icke-deterministiska och kan utvecklas (genom uppdateringar eller drift i modellbeteende) – utan utvärdering skulle du inte veta om din "smarta agent" faktiskt gör sitt jobb bra eller om den har försämrats.

Det finns två kategorier av utvärderingar för AI-agenter: **onlineutvärdering** och **offlineutvärdering**. Båda är värdefulla och kompletterar varandra. Vi börjar vanligtvis med offlineutvärdering, eftersom detta är det minsta nödvändiga steget innan man driftsätter en agent.

### Offlineutvärdering

![Datasetposter i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med testdataset, inte levande användarförfrågningar. Du använder kuraterade dataset där du vet vad det förväntade resultatet eller korrekt beteende är, och kör sedan din agent på dessa. 

Till exempel, om du byggt en agent för matematiska uppgiftsordproblem kan du ha ett [testdataset](https://huggingface.co/datasets/gsm8k) med 100 problem med kända svar. Offlineutvärdering görs ofta under utveckling (och kan vara en del av CI/CD-pipelines) för att kontrollera förbättringar eller skydda mot regressioner. Fördelen är att det är **reproducerbart och att du kan få tydliga noggrannhetsmått eftersom du har en sanningskälla**. Du kan också simulera användarförfrågningar och mäta agentens svar mot ideala svar eller använda automatiska mått som beskrivits ovan. 

Den största utmaningen med offlineutvärdering är att säkerställa att ditt testdataset är omfattande och förblir relevant – agenten kan prestera bra på en fast testsats men möta mycket annorlunda förfrågningar i produktion. Därför bör du hålla testset uppdaterade med nya edge cases och exempel som speglar verkliga scenarier. En blandning av små "smoke test"-fall och större utvärderingsset är användbart: små set för snabba kontroller och större för bredare prestandamått.

### Onlineutvärdering 

![Översikt över observabilitetsmetrik](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en levande, verklig miljö, dvs. under faktisk användning i produktion. Onlineutvärdering innebär att övervaka agentens prestanda i riktiga användarinteraktioner och kontinuerligt analysera resultat. 

Till exempel kan du spåra framgångsfrekvenser, användarnöjdhetspoäng eller andra mått på live-trafik. Fördelen med onlineutvärdering är att det **upptäcker saker du kanske inte förutser i en laboratoriemiljö** – du kan observera modelldriftsförändringar över tid (om agentens effektivitet försämras när indata mönster skiftar) och fånga oväntade frågor eller situationer som inte fanns i ditt testdata. Det ger en sann bild av hur agenten beter sig i fält. 

Onlineutvärdering innebär ofta insamling av implicit och explicit användarfeedback, som diskuterats, och eventuellt körning av shadowtesten eller A/B-tester (där en ny version av agenten körs parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få tillförlitliga etiketter eller poäng för live-interaktioner – du kan vara beroende av användarfeedback eller nedströmsmått (som om användaren klickade på resultatet).

### Att kombinera de två

Online- och offlineutvärderingar utesluter inte varandra; de kompletterar varandra väl. Insikter från onlineövervakning (t.ex. nya typer av användarförfrågningar där agenten presterar dåligt) kan användas för att utöka och förbättra offline-testdataset. Omvänt kan agenter som presterar väl i offline-test driftsättas med större självförtroende och övervakas online. 

Faktum är att många team antar en loop: 

_utvärdera offline -> driftsätt -> övervaka online -> samla nya felfall -> lägg till i offline-dataset -> förfina agent -> upprepa_.

## Vanliga problem

När du driftsätter AI-agenter i produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras möjliga lösningar:

| **Problem**    | **Föreslagen lösning**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Förfina prompten som ges till AI-agenten; var tydlig med målen.<br>- Identifiera var det hjälper att dela upp uppgiften i deluppgifter och låta flera agenter hantera dem. |
| AI Agent running into continuous loops  | - Se till att du har tydliga avslutsvillkor så att agenten vet när processen ska avbrytas.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell som är specialiserad för resonemangsuppgifter. |
| AI Agent tool calls are not performing well   | - Testa och validera verktygets output utanför agentsystemet.<br>- Förfina definierade parametrar, prompts och namngivningen av verktygen.  |
| Multi-Agent system not performing consistently | - Förfina prompts som ges till varje agent för att säkerställa att de är specifika och skilda från varandra.<br>- Bygg ett hierarkiskt system med en "routing" eller kontrollagent för att avgöra vilken agent som är den rätta. |

Många av dessa problem kan identifieras mer effektivt med observabilitet på plats. De spår och mätvärden vi diskuterade tidigare hjälper till att exakt lokalisera var i agentens arbetsflöde problem uppstår, vilket gör felsökning och optimering mycket effektivare.

## Hantera kostnader
Här är några strategier för att hantera kostnaderna för att driftsätta AI-agenter i produktion:

**Använd mindre modeller:** Små språkmodeller (SLMs) kan prestera väl i vissa agentrelaterade användningsfall och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur väl en SLM kommer att fungera för ditt användningsfall att bygga ett utvärderingssystem för att fastställa och jämföra prestanda mot större modeller. Överväg att använda SLMs för enklare uppgifter som avsiktsklassificering eller parameterutvinning, samtidigt som du reserverar större modeller för komplext resonerande.

**Använd en routermodell:** En liknande strategi är att använda en variation av modeller och storlekar. Du kan använda en LLM/SLM eller en serverlös funktion för att skicka förfrågningar vidare baserat på komplexitet till de mest lämpliga modellerna. Detta hjälper också till att sänka kostnaderna samtidigt som det säkerställer prestanda för rätt uppgifter. Till exempel, skicka enkla frågor till mindre, snabbare modeller och använd endast dyra stora modeller för komplexa resoneringsuppgifter.

**Cachelagring av svar:** Att identifiera vanliga förfrågningar och uppgifter och att tillhandahålla svaren innan de går igenom ditt agentiska system är ett bra sätt att minska volymen av liknande förfrågningar. Du kan till och med implementera ett flöde för att identifiera hur lik en förfrågan är dina cachelagrade förfrågningar med hjälp av mer grundläggande AI-modeller. Denna strategi kan avsevärt minska kostnaderna för ofta ställda frågor eller vanliga arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempelnotebooken för detta avsnitt](./code_samples/10-expense_claim-demo.ipynb) kommer vi att se exempel på hur vi kan använda verktyg för observabilitet för att övervaka och utvärdera vår agent.


### Har du fler frågor om AI-agenter i produktion?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra deltagare, delta i öppna frågestunder och få dina frågor om AI-agenter besvarade.

## Föregående lektion

[Designmönster för metakognition](../09-metacognition/README.md)

## Nästa lektion

[Agentiska protokoll](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på originalspråket ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->