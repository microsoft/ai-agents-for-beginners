<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:29:13+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sv"
}
-->
# AI-agenter i produktion: Observabilitet och utvärdering

När AI-agenter går från experimentella prototyper till verkliga applikationer blir det viktigt att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat.

## Lärandemål

Efter att ha genomfört denna lektion kommer du att veta hur man/ha förståelse för:
- Grundläggande koncept kring observabilitet och utvärdering av agenter
- Tekniker för att förbättra prestanda, kostnader och effektivitet hos agenter
- Vad och hur du systematiskt utvärderar dina AI-agenter
- Hur du kontrollerar kostnader vid implementering av AI-agenter i produktion
- Hur du instrumenterar agenter byggda med AutoGen

Målet är att ge dig kunskap för att omvandla dina "svarta lådor" till transparenta, hanterbara och pålitliga system.

_**Obs:** Det är viktigt att implementera AI-agenter som är säkra och pålitliga. Kolla in lektionen [Bygga pålitliga AI-agenter](./06-building-trustworthy-agents/README.md) också._

## Traces och Spans

Observabilitetsverktyg som [Langfuse](https://langfuse.com/) eller [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar vanligtvis agentkörningar som traces och spans.

- **Trace** representerar en komplett agentuppgift från början till slut (som att hantera en användarfråga).
- **Spans** är individuella steg inom trace (som att anropa en språkmodell eller hämta data).

![Trace-träd i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Utan observabilitet kan en AI-agent kännas som en "svart låda" – dess interna tillstånd och resonemang är otydliga, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observabilitet blir agenter "glaslådor" och erbjuder den transparens som är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett.

## Varför observabilitet är viktigt i produktionsmiljöer

Att överföra AI-agenter till produktionsmiljöer innebär nya utmaningar och krav. Observabilitet är inte längre en "trevlig att ha"-funktion utan en kritisk förmåga:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller ger ett oväntat resultat ger observabilitetsverktyg traces som behövs för att identifiera källan till felet. Detta är särskilt viktigt i komplexa agenter som kan involvera flera LLM-anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens- och kostnadshantering**: AI-agenter förlitar sig ofta på LLM:er och andra externa API:er som debiteras per token eller anrop. Observabilitet möjliggör exakt spårning av dessa anrop, vilket hjälper till att identifiera operationer som är onödigt långsamma eller dyra. Detta gör det möjligt för team att optimera prompts, välja mer effektiva modeller eller omdesigna arbetsflöden för att hantera driftskostnader och säkerställa en bra användarupplevelse.
*   **Förtroende, säkerhet och efterlevnad**: I många applikationer är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observabilitet ger en granskningsspår av agentens handlingar och beslut. Detta kan användas för att upptäcka och åtgärda problem som promptinjektion, generering av skadligt innehåll eller felhantering av personligt identifierbar information (PII). Till exempel kan du granska traces för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringsloopar**: Observabilitetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i verkligheten kan team identifiera förbättringsområden, samla in data för att finjustera modeller och validera effekten av förändringar. Detta skapar en feedbackloop där produktionsinsikter från onlineutvärdering informerar offlineexperiment och förfining, vilket leder till successivt bättre agentprestanda.

## Viktiga mätvärden att spåra

För att övervaka och förstå agentbeteende bör en rad mätvärden och signaler spåras. Även om de specifika mätvärdena kan variera beroende på agentens syfte, är vissa universellt viktiga.

Här är några av de vanligaste mätvärdena som observabilitetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och individuella steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modellanrop accelereras genom att använda en snabbare modell eller genom att köra modellanrop parallellt.

**Kostnader:** Vad är kostnaden per agentkörning? AI-agenter förlitar sig på LLM-anrop som debiteras per token eller externa API:er. Frekvent verktygsanvändning eller flera prompts kan snabbt öka kostnaderna. Till exempel, om en agent anropar en LLM fem gånger för marginell kvalitetsförbättring, måste du bedöma om kostnaden är motiverad eller om du kan minska antalet anrop eller använda en billigare modell. Realtidsövervakning kan också hjälpa till att identifiera oväntade toppar (t.ex. buggar som orsakar överdrivna API-loopar).

**Begäransfel:** Hur många begäranden misslyckades agenten med? Detta kan inkludera API-fel eller misslyckade verktygsanrop. För att göra din agent mer robust mot dessa i produktion kan du sedan ställa in fallback-lösningar eller omförsök. T.ex. om LLM-leverantör A är nere, byter du till LLM-leverantör B som backup.

**Användarfeedback:** Implementering av direkta användarutvärderingar ger värdefulla insikter. Detta kan inkludera explicita betyg (👍tumme upp/👎ner, ⭐1-5 stjärnor) eller textkommentarer. Konsekvent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat.

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan explicita betyg. Detta kan inkludera omedelbar omformulering av frågor, upprepade frågor eller att klicka på en omförsöksknapp. T.ex. om du ser att användare upprepade gånger ställer samma fråga är detta ett tecken på att agenten inte fungerar som förväntat.

**Noggrannhet:** Hur ofta producerar agenten korrekta eller önskvärda resultat? Definitioner av noggrannhet varierar (t.ex. korrekthet i problemlösning, noggrannhet vid informationshämtning, användarnöjdhet). Det första steget är att definiera vad framgång innebär för din agent. Du kan spåra noggrannhet via automatiska kontroller, utvärderingspoäng eller etiketter för uppgiftsfullbordande. Till exempel, markera traces som "lyckades" eller "misslyckades".

**Automatiserade utvärderingsmätvärden:** Du kan också ställa in automatiserade utvärderingar. Till exempel kan du använda en LLM för att betygsätta agentens output, t.ex. om den är hjälpsam, korrekt eller inte. Det finns också flera open source-bibliotek som hjälper dig att betygsätta olika aspekter av agenten. T.ex. [RAGAS](https://docs.ragas.io/) för RAG-agenter eller [LLM Guard](https://llm-guard.com/) för att upptäcka skadligt språk eller promptinjektion.

I praktiken ger en kombination av dessa mätvärden den bästa täckningen av en AI-agents hälsa. I detta kapitels [exempeldokument](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) visar vi hur dessa mätvärden ser ut i verkliga exempel, men först ska vi lära oss hur ett typiskt utvärderingsarbetsflöde ser ut.

## Instrumentera din agent

För att samla in tracing-data måste du instrumentera din kod. Målet är att instrumentera agentkoden för att generera traces och mätvärden som kan fångas, bearbetas och visualiseras av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blivit en industristandard för observabilitet av LLM. Det erbjuder en uppsättning API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata.

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry-spans till ett observabilitetsverktyg. Nedan är ett exempel på att instrumentera en AutoGen-agent med [OpenLit-instrumenteringsbiblioteket](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Exempeldokumentet](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) i detta kapitel kommer att demonstrera hur du instrumenterar din AutoGen-agent.

**Manuell skapande av spans:** Även om instrumenteringsbibliotek ger en bra grund finns det ofta fall där mer detaljerad eller anpassad information behövs. Du kan manuellt skapa spans för att lägga till anpassad applikationslogik. Ännu viktigare är att de kan berika automatiskt eller manuellt skapade spans med anpassade attribut (även kända som taggar eller metadata). Dessa attribut kan inkludera affärsspecifik data, mellanliggande beräkningar eller någon kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id` eller `model_version`.

Exempel på att skapa traces och spans manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Utvärdering av agenter

Observabilitet ger oss mätvärden, men utvärdering är processen att analysera dessa data (och utföra tester) för att avgöra hur väl en AI-agent presterar och hur den kan förbättras. Med andra ord, när du har dessa traces och mätvärden, hur använder du dem för att bedöma agenten och fatta beslut?

Regelbunden utvärdering är viktig eftersom AI-agenter ofta är icke-deterministiska och kan utvecklas (genom uppdateringar eller förändrat modellbeteende) – utan utvärdering skulle du inte veta om din "smarta agent" faktiskt gör sitt jobb bra eller om den har försämrats.

Det finns två kategorier av utvärderingar för AI-agenter: **onlineutvärdering** och **offlineutvärdering**. Båda är värdefulla och kompletterar varandra. Vi börjar vanligtvis med offlineutvärdering, eftersom detta är det minsta nödvändiga steget innan någon agent implementeras.

### Offlineutvärdering

![Datasetobjekt i Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med testdatamängder, inte live-användarfrågor. Du använder kuraterade datamängder där du vet vad det förväntade resultatet eller korrekta beteendet är och kör sedan din agent på dessa.

Till exempel, om du byggde en agent för matematiska ordproblem, kan du ha en [testdatamängd](https://huggingface.co/datasets/gsm8k) med 100 problem med kända svar. Offlineutvärdering görs ofta under utveckling (och kan vara en del av CI/CD-pipelines) för att kontrollera förbättringar eller skydda mot försämringar. Fördelen är att det är **upprepbart och du kan få tydliga noggrannhetsmätvärden eftersom du har facit**. Du kan också simulera användarfrågor och mäta agentens svar mot ideala svar eller använda automatiserade mätvärden som beskrivs ovan.

Den största utmaningen med offlineutvärdering är att säkerställa att din testdatamängd är omfattande och förblir relevant – agenten kan prestera bra på en fast testmängd men stöta på helt andra frågor i produktion. Därför bör du hålla testmängder uppdaterade med nya edge cases och exempel som speglar verkliga scenarier​. En blandning av små "röktest"-fall och större utvärderingsmängder är användbar: små mängder för snabba kontroller och större för bredare prestandamätningar​.

### Onlineutvärdering

![Översikt över observabilitetsmätvärden](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en live, verklig miljö, dvs. under faktisk användning i produktion. Onlineutvärdering innebär att kontinuerligt övervaka agentens prestanda på verkliga användarinteraktioner och analysera resultat.

Till exempel kan du spåra framgångsfrekvenser, användarnöjdhetspoäng eller andra mätvärden på live-trafik. Fördelen med onlineutvärdering är att det **fångar saker du kanske inte förutser i en labbmiljö** – du kan observera modellförändringar över tid (om agentens effektivitet försämras när inmatningsmönster förändras) och fånga oväntade frågor eller situationer som inte fanns i din testdata​. Det ger en sann bild av hur agenten beter sig i verkligheten.

Onlineutvärdering innebär ofta att samla in implicit och explicit användarfeedback, som diskuterats, och eventuellt köra skuggtester eller A/B-tester (där en ny version av agenten körs parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få tillförlitliga etiketter eller poäng för live-interaktioner – du kan behöva förlita dig på användarfeedback eller nedströmsmätvärden (som om användaren klickade på resultatet).

### Kombinera de två

Online- och offlineutvärderingar utesluter inte varandra; de kompletterar varandra starkt. Insikter från onlineövervakning (t.ex. nya typer av användarfrågor där agenten presterar dåligt) kan användas för att förstärka och förbättra offline-testdatamängder. Omvänt kan agenter som presterar bra i offline-tester sedan implementeras med större självförtroende och övervakas online.

Faktum är att många team antar en loop:

_utvärdera offline -> implementera -> övervaka online -> samla in nya felaktiga fall -> lägg till i offline-datamängd -> förfina agent -> upprepa_.

## Vanliga problem

När du implementerar AI-agenter i produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras möjliga lösningar:

| **Problem**    | **Möjlig lösning**   |
| ------------- | ------------------ |
| AI-agenten utför inte uppgifter konsekvent | - Förfina prompten som ges till AI-agenten; var tydlig med målen.<br>- Identifiera om det kan hjälpa att dela upp uppgifterna i deluppgifter och hantera dem med flera agenter. |
| AI-agenten hamnar i kontinuerliga loopar  | - Säkerställ att du har tydliga avslutningsvillkor så att agenten vet när processen ska avslutas.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell som är specialiserad för resonemangsuppgifter. |
| AI-agentens verktygsanrop fungerar inte bra   | - Testa och validera verktygets output utanför agentsystemet. |

- Förfina de definierade parametrarna, uppmaningarna och namngivningen av verktyg.  |
| Multi-Agent-systemet fungerar inte konsekvent | - Förfina uppmaningarna som ges till varje agent för att säkerställa att de är specifika och skiljer sig från varandra.<br>- Bygg ett hierarkiskt system med hjälp av en "routing"- eller kontrollagent för att avgöra vilken agent som är den rätta. |

Många av dessa problem kan identifieras mer effektivt med observabilitet på plats. De spår och mätvärden vi diskuterade tidigare hjälper till att exakt identifiera var i agentens arbetsflöde problemen uppstår, vilket gör felsökning och optimering mycket mer effektivt.

## Hantering av kostnader

Här är några strategier för att hantera kostnaderna för att implementera AI-agenter i produktion:

**Använda mindre modeller:** Små språkmodeller (SLM) kan fungera bra för vissa agentbaserade användningsområden och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur väl en SLM kommer att fungera för ditt användningsområde att bygga ett utvärderingssystem för att avgöra och jämföra prestanda med större modeller. Överväg att använda SLM för enklare uppgifter som avsiktsklassificering eller parameterutvinning, och reservera större modeller för komplexa resonemangsuppgifter.

**Använda en routermodell:** En liknande strategi är att använda en mångfald av modeller och storlekar. Du kan använda en LLM/SLM eller serverlös funktion för att dirigera förfrågningar baserat på komplexitet till de mest lämpliga modellerna. Detta kommer också att hjälpa till att minska kostnaderna samtidigt som det säkerställer prestanda för rätt uppgifter. Till exempel, dirigera enkla frågor till mindre, snabbare modeller och använd endast dyra stora modeller för komplexa resonemangsuppgifter.

**Cacha svar:** Identifiera vanliga förfrågningar och uppgifter och tillhandahåll svaren innan de går igenom ditt agentbaserade system. Du kan till och med implementera ett flöde för att identifiera hur lik en förfrågan är dina cachade förfrågningar med hjälp av mer grundläggande AI-modeller. Denna strategi kan avsevärt minska kostnaderna för vanliga frågor eller återkommande arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempeldagboken för denna sektion](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) kommer vi att se exempel på hur vi kan använda observabilitetsverktyg för att övervaka och utvärdera vår agent.

## Föregående lektion

[Metakognitionsdesignmönster](../09-metacognition/README.md)

## Nästa lektion

[MCP](../11-mcp/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.