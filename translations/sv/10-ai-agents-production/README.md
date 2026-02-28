# AI‑agenter i produktion: Observabilitet & utvärdering

[![AI‑agenter i produktion](../../../translated_images/sv/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

När AI‑agenter går från experimentella prototyper till verkliga tillämpningar blir förmågan att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat viktig.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna/förstå:
- Grundläggande begrepp för agentobservabilitet och utvärdering
- Tekniker för att förbättra agenters prestanda, kostnader och effektivitet
- Vad och hur du systematiskt utvärderar dina AI‑agenter
- Hur du kontrollerar kostnader vid produktsättning av AI‑agenter
- Hur du instrumenterar agenter byggda med Microsoft Agent Framework

Målet är att utrusta dig med kunskap för att förvandla dina "svarta låda"-agenter till transparenta, hanterbara och pålitliga system.

_**Obs:** Det är viktigt att distribuera AI‑agenter som är säkra och förtroendeingivande. Kolla också in lektionen [Bygga förtroendefulla AI‑agenter](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Observabilitetsverktyg som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar vanligtvis agentkörningar som traces och spans.

- **Trace** representerar en komplett agentuppgift från början till slut (som att hantera en användarfråga).
- **Spans** är individuella steg inom trace:en (som att anropa en språkmodell eller hämta data).

![Trace-träd i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Utan observabilitet kan en AI‑agent kännas som en "svart låda" – dess interna tillstånd och resonemang är ogenomskinliga, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observabilitet blir agenterna "glaslådor", vilket erbjuder transparens som är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett. 

## Varför observabilitet är viktigt i produktionsmiljöer

Att överföra AI‑agenter till produktionsmiljöer introducerar en ny uppsättning utmaningar och krav. Observabilitet är inte längre ett "trevligt att ha" utan en kritisk förmåga:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller producerar ett oväntat resultat ger observabilitetsverktyg de spår som behövs för att lokalisera felets källa. Detta är särskilt viktigt i komplexa agenter som kan involvera flera LLM‑anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens- och kostnadshantering**: AI‑agenter förlitar sig ofta på LLM:er och andra externa API:er som debiteras per token eller per anrop. Observabilitet möjliggör exakt spårning av dessa anrop och hjälper till att identifiera operationer som är onödigt långsamma eller dyra. Detta gör det möjligt för team att optimera prompts, välja effektivare modeller eller omdesigna arbetsflöden för att hantera driftkostnader och säkerställa en bra användarupplevelse.
*   **Förtroende, säkerhet och efterlevnad**: I många tillämpningar är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observabilitet tillhandahåller en revisionslogg över agentens handlingar och beslut. Detta kan användas för att upptäcka och mildra problem som prompt‑injektion, generering av skadligt innehåll eller felhantering av personligt identifierbar information (PII). Du kan till exempel granska traces för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringscykler**: Observabilitetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i verkliga världen kan team identifiera förbättringsområden, samla data för finjustering av modeller och validera effekten av förändringar. Detta skapar en återkopplingsslinga där produktionsinsikter från onlineutvärdering informerar offline‑experiment och förfining, vilket leder till successivt bättre agentprestanda.

## Viktiga mätvärden att övervaka

För att övervaka och förstå agentbeteende bör en rad mätvärden och signaler följas. De specifika mätvärdena kan variera beroende på agentens syfte, men vissa är universellt viktiga.

Här är några av de vanligaste mätvärdena som observabilitetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och individuella steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modellanrop snabba upp genom att använda en snabbare modell eller genom att köra modellanrop parallellt.

**Kostnader:** Vad kostar en agentkörning? AI‑agenter förlitar sig på LLM‑anrop som debiteras per token eller externa API:er. Frekvent verktygsanvändning eller flera prompts kan snabbt öka kostnaderna. Om en agent till exempel anropar en LLM fem gånger för marginell kvalitetsförbättring måste du bedöma om kostnaden är motiverad eller om du kan minska antalet anrop eller använda en billigare modell. Realtidsövervakning kan också hjälpa till att identifiera oväntade toppar (t.ex. buggar som orsakar överdrivna API‑loopar).

**Begäransfel:** Hur många förfrågningar misslyckades agenten med? Detta kan inkludera API‑fel eller misslyckade verktygsanrop. För att göra din agent mer robust i produktion kan du sedan sätta upp fallback‑lösningar eller retries. T.ex. om LLM‑leverantör A ligger nere kan du byta till LLM‑leverantör B som backup.

**Användarfeedback:** Implementering av direkt användarutvärdering ger värdefulla insikter. Detta kan inkludera explicita betyg (👍tummen upp/👎ner, ⭐1–5 stjärnor) eller textkommentarer. Konsekvent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat. 

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan explicita betyg. Detta kan inkludera omedelbar omformulering av frågor, upprepade förfrågningar eller att klicka på en försök‑igen‑knapp. T.ex. om du ser att användare upprepade gånger ställer samma fråga är det ett tecken på att agenten inte fungerar som förväntat.

**Noggrannhet:** Hur ofta producerar agenten korrekta eller önskvärda resultat? Definitionen av noggrannhet varierar (t.ex. korrekt problemlösning, informationsåtervinningens träffsäkerhet, användarnöjdhet). Det första steget är att definiera vad framgång ser ut som för din agent. Du kan spåra noggrannhet via automatiska kontroller, utvärderingspoäng eller etiketter för uppgiftsfullföljande. Till exempel markera traces som "succeeded" eller "failed". 

**Automatiserade utvärderingsmetoder:** Du kan också ställa in automatiska evals. Till exempel kan du använda en LLM för att poängsätta agentens output, t.ex. om den är hjälpsam, korrekt eller inte. Det finns även flera öppna källkods‑bibliotek som hjälper dig att poängsätta olika aspekter av agenten. T.ex. [RAGAS](https://docs.ragas.io/) för RAG‑agenter eller [LLM Guard](https://llm-guard.com/) för att upptäcka skadligt språk eller prompt‑injektion. 

I praktiken ger en kombination av dessa mätvärden bäst täckning för en AI‑agents hälsa. I detta kapitels [exempelnätbok](./code_samples/10-expense_claim-demo.ipynb) visar vi hur dessa mätvärden ser ut i verkliga exempel men först lär vi oss hur ett typiskt utvärderingsarbetsflöde ser ut.

## Instrumentera din agent

För att samla spårningsdata behöver du instrumentera din kod. Målet är att instrumentera agentkoden för att sända traces och mätvärden som kan fångas, bearbetas och visualiseras av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har vuxit fram som en industristandard för LLM‑observabilitet. Det tillhandahåller ett set API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata. 

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry‑spans till ett observabilitetsverktyg. Microsoft Agent Framework integrerar med OpenTelemetry inbyggt. Nedan är ett exempel på hur man instrumenterar en MAF‑agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens körning spåras automatiskt
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manuell span‑skapande:** Medan instrumenteringsbibliotek ger en bra grundlinje finns det ofta fall där mer detaljerad eller anpassad information behövs. Du kan skapa spans manuellt för att lägga till anpassad applikationslogik. Mer viktigt, de kan berika automatiskt eller manuellt skapade spans med anpassade attribut (även kända som taggar eller metadata). Dessa attribut kan inkludera verksamhetsspecifik data, mellanliggande beräkningar eller annan kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id` eller `model_version`.

Exempel på att skapa traces och spans manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentutvärdering

Observabilitet ger oss mätvärden, men utvärdering är processen att analysera dessa data (och utföra tester) för att avgöra hur väl en AI‑agent presterar och hur den kan förbättras. Med andra ord, när du har de där traces och mätvärdena, hur använder du dem för att bedöma agenten och fatta beslut? 

Regelbunden utvärdering är viktig eftersom AI‑agenter ofta är icke‑deterministiska och kan utvecklas (genom uppdateringar eller modellens drift) – utan utvärdering skulle du inte veta om din "smarta agent" faktiskt gör sitt jobb väl eller om den har regressat.

Det finns två kategorier av utvärderingar för AI‑agenter: **onlineutvärdering** och **offline‑utvärdering**. Båda är värdefulla och kompletterar varandra. Vi börjar vanligtvis med offline‑utvärdering, eftersom detta är minimisteget som krävs innan man distribuerar någon agent.

### Offline‑utvärdering

![Dataposter i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med hjälp av testdataset, inte levande användarförfrågningar. Du använder kurerade dataset där du vet vad det förväntade resultatet eller korrekt beteende är, och kör sedan din agent på dessa. 

Till exempel, om du byggt en agent för matematiska textproblem kanske du har ett [testdataset](https://huggingface.co/datasets/gsm8k) med 100 problem med kända svar. Offline‑utvärdering görs ofta under utveckling (och kan vara del av CI/CD‑pipelines) för att kontrollera förbättringar eller skydda mot regressioner. Fördelen är att det är **reproducerbart och du kan få tydliga noggrannhetsmått eftersom du har sanning på marken**. Du kan också simulera användarförfrågningar och mäta agentens svar mot idealiska svar eller använda automatiserade mätvärden som beskrivits ovan. 

Den största utmaningen med offline‑utvärdering är att säkerställa att ditt testdataset är omfattande och förblir relevant – agenten kan prestera bra på en fast testsats men stöta på mycket olika frågor i produktion. Därför bör du hålla testsatser uppdaterade med nya kantfall och exempel som speglar verkliga scenarier​. En blandning av små "smoke test"-fall och större utvärderingssatsningar är användbar: små satser för snabba kontroller och större för bredare prestandamått​.

### Online‑utvärdering 

![Översikt över observabilitetsmått](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en levande, verklig miljö, dvs. under faktisk användning i produktion. Online‑utvärdering innebär att övervaka agentens prestanda på verkliga användarinteraktioner och analysera utfall kontinuerligt. 

Till exempel kan du spåra framgångsgrader, användarnöjdhetspoäng eller andra mätvärden på live‑trafik. Fördelen med online‑utvärdering är att den **fångar saker du kanske inte förutser i en labbmiljö** – du kan observera modellens drift över tid (om agentens effektivitet försämras när indatafördelningar förändras) och fånga oväntade frågor eller situationer som inte fanns i ditt testdata​. Det ger en sann bild av hur agenten beter sig i verkligheten. 

Online‑utvärdering innebär ofta insamling av implicit och explicit användarfeedback, som diskuterats, och eventuellt körning av skuggtester eller A/B‑tester (där en ny version av agenten körs parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få tillförlitliga etiketter eller poäng för live‑interaktioner – du kan behöva förlita dig på användarfeedback eller downstream‑mått (som om användaren klickade på resultatet). 

### Kombinera de båda

Online‑ och offline‑utvärderingar utesluter inte varandra; de kompletterar varandra väl. Insikter från online‑övervakning (t.ex. nya typer av användarfrågor där agenten presterar dåligt) kan användas för att utöka och förbättra offline‑testdataset. Omvänt kan agenter som presterar bra i offline‑tester sedan mer förtroendefullt sättas i produktion och övervakas online. 

Faktum är att många team antar en loop: 

_utvärdera offline -> distribuera -> övervaka online -> samla nya felfall -> lägg till i offlinedatasetet -> förbättra agenten -> upprepa_.

## Vanliga problem

När du distribuerar AI‑agenter till produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras potentiella lösningar:

| **Problem**    | **Potentiell lösning**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Förfina prompten som ges till AI‑agenten; var tydlig med målen.<br>- Identifiera var det kan hjälpa att dela upp uppgifterna i deluppgifter och hantera dem med flera agenter. |
| AI Agent running into continuous loops  | - Se till att du har tydliga avslutningsvillkor så agenten vet när den ska avbryta processen.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell som är specialiserad för resonemangsuppgifter. |
| AI Agent tool calls are not performing well   | - Testa och validera verktygets output utanför agentsystemet.<br>- Förfina de definierade parametrarna, prompts och namngivningen av verktygen.  |
| Multi-Agent system not performing consistently | - Förfina prompts som ges till varje agent för att säkerställa att de är specifika och skiljer sig från varandra.<br>- Bygg ett hierarkiskt system med en "routing" eller controller‑agent för att avgöra vilken agent som är den korrekta. |

Många av dessa problem kan identifieras mer effektivt med observabilitet på plats. De traces och mätvärden vi diskuterat tidigare hjälper till att exakt lokalisera var i agentens arbetsflöde problemen uppstår, vilket gör felsökning och optimering mycket mer effektivt.

## Hantera kostnader
Här är några strategier för att hantera kostnaderna för att driftsätta AI-agenter i produktion:

**Använd mindre modeller:** Små Language Models (SLMs) kan prestera väl i vissa agentiska användningsfall och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur väl en SLM kommer att fungera i ditt användningsfall att bygga ett utvärderingssystem för att bestämma och jämföra prestanda mot större modeller. Överväg att använda SLMs för enklare uppgifter som avsiktsklassificering eller parameterextraktion, medan du reserverar större modeller för komplexare resonemang.

**Använda en routermodell:** En liknande strategi är att använda en mångfald av modeller och storlekar. Du kan använda en LLM/SLM eller en serverlös funktion för att dirigera förfrågningar baserat på komplexitet till de modeller som passar bäst. Detta hjälper också till att minska kostnader samtidigt som prestanda säkerställs för rätt uppgifter. Till exempel, dirigera enkla frågor till mindre, snabbare modeller, och använd endast dyra stora modeller för komplexa resonemangsuppgifter.

**Cachelagring av svar:** Att identifiera vanliga förfrågningar och uppgifter och tillhandahålla svaren innan de går igenom ditt agentiska system är ett bra sätt att minska volymen av liknande förfrågningar. Du kan till och med implementera ett flöde för att avgöra hur lik en förfrågan är dina cachelagrade förfrågningar genom att använda mer grundläggande AI-modeller. Denna strategi kan avsevärt minska kostnaderna för ofta ställda frågor eller vanliga arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempelnotebooken för detta avsnitt](./code_samples/10-expense_claim-demo.ipynb) kommer vi att se exempel på hur vi kan använda observability-verktyg för att övervaka och utvärdera vår agent.


### Har du fler frågor om AI-agenter i produktion?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra deltagare, delta i kontorstider och få dina frågor om AI-agenter besvarade.

## Föregående lektion

[Designmönster för metakognition](../09-metacognition/README.md)

## Nästa lektion

[Agentiska protokoll](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->