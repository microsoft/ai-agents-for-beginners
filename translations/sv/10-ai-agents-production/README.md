# AI-agenter i produktion: Observabilitet och utvärdering

[![AI Agents in Production](../../../translated_images/sv/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

När AI-agenter går från experimentella prototyper till verkliga tillämpningar blir förmågan att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat viktig.

## Läromål

Efter att ha genomgått denna lektion kommer du att kunna/förstå:
- Grundläggande begrepp inom agentobservabilitet och utvärdering
- Tekniker för att förbättra agenters prestanda, kostnader och effektivitet
- Vad och hur du systematiskt utvärderar dina AI-agenter
- Hur du kontrollerar kostnader när du driftsätter AI-agenter i produktion
- Hur du instrumenterar agenter byggda med Microsoft Agent Framework

Målet är att förse dig med kunskap för att omvandla dina "svarta lådor"-agenter till transparenta, hanterbara och tillförlitliga system.

_**Notera:** Det är viktigt att driftsätta AI-agenter som är säkra och pålitliga. Kolla in lektionen [Bygga pålitliga AI-agenter](../06-building-trustworthy-agents/README.md) också._

## Spår (Traces) och Steg (Spans)

Observabilitetsverktyg som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar vanligtvis agentkörningar som spår och steg.

- **Spår (Trace)** representerar en komplett agentuppgift från början till slut (som att hantera en användarfråga).
- **Steg (Spans)** är individuella steg inom spåret (som att anropa en språklig modell eller hämta data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Utan observabilitet kan en AI-agent kännas som en "svart låda" – dess interna tillstånd och resonemang är ogenomskinliga, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observabilitet blir agenter "glaslådor" som erbjuder transparens, vilket är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett.

## Varför observabilitet är viktigt i produktionsmiljöer

Att flytta AI-agenter till produktionsmiljöer medför nya utmaningar och krav. Observabilitet är inte längre något "bra att ha" utan en kritisk kapacitet:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller ger oväntade resultat ger observabilitetsverktyg de spår som behövs för att lokalisera felkällan. Detta är särskilt viktigt i komplexa agenter som kan innefatta flera LLM-anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens- och kostnadshantering**: AI-agenter är ofta beroende av LLM:er och andra externa API:er som debiteras per token eller per anrop. Observabilitet möjliggör exakt spårning av dessa anrop vilket hjälper till att identifiera operationer som är ovanligt långsamma eller dyra. Detta gör det möjligt för team att optimera prompts, välja effektivare modeller eller omforma arbetsflöden för att hantera operativa kostnader och säkra en bra användarupplevelse.
*   **Förtroende, säkerhet och efterlevnad**: I många tillämpningar är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observabilitet ger en revisionskedja för agentens handlingar och beslut. Detta kan användas för att upptäcka och mildra problem som promptinjektion, generering av skadligt innehåll eller felhantering av personligt identifierbar information (PII). Till exempel kan du granska spår för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringsloopar**: Observabilitetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i verkliga världen kan team identifiera förbättringsområden, samla data för finjustering av modeller och validera effekten av förändringar. Detta skapar en återkopplingsloop där insikter från onlineutvärdering i produktion informerar offline-experiment och förfining, vilket leder till successivt bättre agentprestanda.

## Viktiga mått att spåra

För att övervaka och förstå agentbeteende bör en rad mätvärden och signaler följas upp. Även om specifika mått kan variera beroende på agentens syfte är vissa universellt viktiga.

Här är några vanliga mätvärden som observabilitetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och enskilda steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modellanrop snabbbas upp genom att använda en snabbare modell eller köra modellanrop parallellt.

**Kostnader:** Vad kostar en agentkörning? AI-agenter är beroende av LLM-anrop debiterade per token eller externa API:er. Frekvent verktygsanvändning eller flera prompts kan snabbt öka kostnaderna. Om en agent t.ex. anropar en LLM fem gånger för marginell kvalitetsförbättring måste du bedöma om kostnaden är motiverad eller om du kan minska anropen eller använda en billigare modell. Realtidsövervakning kan också hjälpa till att identifiera oväntade skutt (t.ex. buggar som orsakar överdrivna API-loopar).

**Begäransfel:** Hur många begäranden misslyckades agenten med? Detta kan inkludera API-fel eller misslyckade verktygsanrop. För att göra din agent mer robust i produktion kan du då sätta upp fallback-lösningar eller retries. T.ex. om LLM-leverantör A är nere, byter du till LLM-leverantör B som backup.

**Användarfeedback:** Att implementera direkta användarutvärderingar ger värdefulla insikter. Detta kan inkludera explicita betyg (👍tummen upp/👎ner, ⭐1-5 stjärnor) eller textkommentarer. Konsekvent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat.

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan explicita betyg. Detta kan inkludera omedelbar omformulering av frågor, upprepade frågor eller klick på en retry-knapp. T.ex. om du ser att användare upprepade gånger frågar samma fråga är det ett tecken på att agenten inte fungerar som förväntat.

**Noggrannhet:** Hur ofta producerar agenten korrekta eller önskade resultat? Definitionen av noggrannhet varierar (t.ex. korrekt problemlösning, informationshämtningens träffsäkerhet, användarnöjdhet). Första steget är att definiera vad framgång innebär för din agent. Du kan följa noggrannhet via automatiska kontroller, utvärderingspoäng eller markeringar av uppgiftsfullföljande. Till exempel att märka spår som "lyckades" eller "misslyckades".

**Automatiserade utvärderingsmått:** Du kan också sätta upp automatiska utvärderingar. T.ex. kan du använda en LLM för att poängsätta agentens output, t.ex. om den är hjälpsam, korrekt eller inte. Det finns även flera öppen källkods-bibliotek som hjälper dig att bedöma olika aspekter av agenten, t.ex. [RAGAS](https://docs.ragas.io/) för RAG-agenter eller [LLM Guard](https://llm-guard.com/) för att upptäcka skadligt språk eller promptinjektion.

I praktiken ger en kombination av dessa mått bäst täckning av en AI-agents hälsa. I detta kapitel [exempelnätbok](./code_samples/10-expense_claim-demo.ipynb) visar vi hur dessa mått ser ut i riktiga exempel, men först lär vi oss hur ett typiskt utvärderingsarbetsflöde ser ut.

## Instrumentera din agent

För att samla in spårningsdata behöver du instrumentera din kod. Målet är att instrumentera agentkoden så att den genererar spår och mätvärden som kan fångas, bearbetas och visualiseras av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blivit en industristandard för observabilitet hos LLM. Det erbjuder ett set av API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata.

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry-spans till ett observabilitetsverktyg. Microsoft Agent Framework integreras med OpenTelemetry nativt. Nedan är ett exempel på att instrumentera en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens körning spåras automatiskt
    pass
```

[Exempelnätboken](./code_samples/10-expense_claim-demo.ipynb) i detta kapitel demonstrerar hur du instrumenterar din MAF-agent.

**Manuell skapelse av spans:** Medan instrumenteringsbibliotek ger en bra grund finns ofta fall där mer detaljerad eller anpassad information behövs. Du kan manuellt skapa spans för att lägga till egen applikationslogik. Viktigare är att de kan berika automatiskt eller manuellt skapade spans med egna attribut (även kända som taggar eller metadata). Dessa attribut kan inkludera affärsspecifik data, mellanberäkningar eller annan kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id` eller `model_version`.

Exempel på att skapa spår och spans manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentutvärdering

Observabilitet ger oss mätvärden, men utvärdering är processen att analysera dessa data (och utföra tester) för att bestämma hur väl en AI-agent presterar och hur den kan förbättras. Med andra ord, när du har dessa spår och mätvärden, hur använder du dem för att bedöma agenten och fatta beslut?

Regelbunden utvärdering är viktigt eftersom AI-agenter ofta är icke-deterministiska och kan utvecklas (genom uppdateringar eller driftsförskjutning i modellbeteende) – utan utvärdering skulle du inte veta om din "smarta agent" faktiskt gör sitt jobb väl eller om den har försämrats.

Det finns två kategorier av utvärderingar för AI-agenter: **onlineutvärdering** och **offlineutvärdering**. Båda är värdefulla och kompletterar varandra. Vanligtvis börjar vi med offlineutvärdering, eftersom detta är det minimala nödvändiga steget innan en agent kan driftsättas.

### Offlineutvärdering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med testdatasätt och inte levande användarfrågor. Du använder kurerade dataset där du vet vad förväntat resultat eller korrekt beteende är, och kör sedan agenten på dessa.

Till exempel, om du byggt en agent för matematiska ordproblem kan du ha ett [testdataset](https://huggingface.co/datasets/gsm8k) med 100 problem och kända svar. Offlineutvärdering görs ofta under utveckling (och kan ingå i CI/CD-pipelines) för att kontrollera förbättringar eller skydda mot regressioner. Fördelen är att det är **upprepbart och du kan få tydliga noggrannhetsmått eftersom du har sanningsdata**. Du kan också simulera användarfrågor och mäta agentens svar mot ideala svar eller använda automatiska mått som beskrivits ovan.

Den stora utmaningen med offlineutvärdering är att säkerställa att ditt testdataset är heltäckande och håller sig relevant – agenten kan prestera bra på ett fast testset men möta mycket olika frågor i produktion. Därför bör testset uppdateras med nya kantfall och exempel som speglar verkliga scenarion​. En mix av små ”röktest” och större utvärderingsset är användbart: små set för snabba kontroller och större för bredare prestandamått​.

### Onlineutvärdering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en levande, verklig miljö, alltså under faktisk användning i produktion. Onlineutvärdering innebär att övervaka agentens prestanda på verkliga användarinteraktioner och analysera resultat löpande.

Till exempel kan du spåra framgångsfrekvenser, användartillfredsställelse eller andra mått på levande trafik. Fördelen med onlineutvärdering är att det **fångar saker som du inte kan förutse i en labsituation** – du kan observera modellförskjutning över tid (om agentens effektivitet försämras när inmatningsmönster förändras) och upptäcka oväntade frågor eller situationer som inte fanns i testdatan​. Det ger en sann bild av hur agenten beter sig "i det vilda".

Onlineutvärdering omfattar ofta insamling av implicit och explicit användarfeedback, som diskuterats, och eventuellt skuggetester eller A/B-tester (där en ny version av agenten kör parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få pålitliga etiketter eller poäng för levande interaktioner – du kanske förlitar dig på användarfeedback eller efterföljande mått (som om användaren klickade på resultatet).

### Att kombinera de två

Online- och offlineutvärderingar är inte ömsesidigt uteslutande; de kompletterar varandra väl. Insikter från onlineövervakning (t.ex. nya typer av användarfrågor där agenten presterar dåligt) kan användas för att förstärka och förbättra offline testdataset. Omvänt kan agenter som presterar bra i offline-tester då med större förtroende driftsättas och övervakas online.

Faktum är att många team antar en loop:

_utvärdera offline -> driftsätta -> övervaka online -> samla in nya fall av fel -> lägg till i offline-dataset -> förfina agent -> upprepa_.

## Vanliga problem

När du driftsätter AI-agenter i produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras potentiella lösningar:

| **Problem**    | **Potentiell lösning**   |
| ------------- | ------------------ |
| AI-agenten utför inte uppgifter konsekvent | - Förfina den prompt som ges till AI-agenten; var tydlig med målen.<br>- Identifiera om det hjälper att dela upp uppgifterna i deluppgifter som hanteras av flera agenter. |
| AI-agent fastnar i oändliga loopar  | - Säkerställ att du har tydliga villkor för när processen ska avslutas så att agenten vet när den ska stoppa.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell specialiserad för resonemangsuppgifter. |
| AI-agentens verktygsanrop fungerar inte bra   | - Testa och validera verktygets output utanför agentsystemet.<br>- Förfina definierade parametrar, prompts och namngivning av verktyg.  |
| Multi-agent system presterar inte konsekvent | - Förfina promptar till varje agent för att säkerställa att de är specifika och distinkta.<br>- Bygg ett hierarkiskt system med en "routing" eller styrare-agent för att avgöra vilken agent som är rätt. |

Många av dessa problem kan identifieras mer effektivt med observabilitet på plats. De spår och mätvärden vi diskuterade tidigare hjälper till att exakt peka ut var i agentens arbetsflöde problem uppstår, vilket gör felsökning och optimering mycket mer effektivt.

## Hantera kostnader
Här är några strategier för att hantera kostnaderna för att distribuera AI-agenter i produktion:

**Använda Mindre Modeller:** Små språkmodeller (SLM) kan prestera bra på vissa agentrelaterade användningsområden och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur väl en SLM kommer att prestera på ditt användningsområde att bygga ett utvärderingssystem för att bestämma och jämföra prestanda mot större modeller. Överväg att använda SLM för enklare uppgifter som intentsklassificering eller parameterutvinning, samtidigt som du reserverar större modeller för komplexa resonemang.

**Använda en Routermodell:** En liknande strategi är att använda en mångfald av modeller och storlekar. Du kan använda en LLM/SLM eller serverless-funktion för att dirigera förfrågningar baserat på komplexitet till de bäst lämpade modellerna. Detta hjälper också till att minska kostnader samtidigt som det säkerställer prestanda för rätt uppgifter. Till exempel, dirigera enkla frågor till mindre, snabbare modeller, och använd endast dyra stora modeller för komplexa resonansuppgifter.

**Caching av Svar:** Att identifiera vanliga förfrågningar och uppgifter och tillhandahålla svaren innan de går igenom ditt agentbaserade system är ett bra sätt att minska volymen av likartade förfrågningar. Du kan till och med implementera ett flöde för att identifiera hur lik en förfrågan är dina cachade förfrågningar med hjälp av mer grundläggande AI-modeller. Denna strategi kan avsevärt minska kostnader för ofta ställda frågor eller vanliga arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempelnotebooken för detta avsnitt](./code_samples/10-expense_claim-demo.ipynb) kommer vi att se exempel på hur vi kan använda observabilitetsverktyg för att övervaka och utvärdera vår agent.


### Fler frågor om AI-agenter i produktion?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra inlärare, delta i kontorstid och få dina frågor om AI-agenter besvarade.

## Föregående Lektion

[Metakognition Designmönster](../09-metacognition/README.md)

## Nästa Lektion

[Agentiska Protokoll](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->