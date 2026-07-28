# AI-agenter i produktion: Observabilitet & Utvärdering

[![AI Agents in Production](../../../translated_images/sv/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

När AI-agenter går från experimentella prototyper till verkliga tillämpningar blir förmågan att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat viktig.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att veta hur man/förstå:
- Kärnbegrepp för agentobservabilitet och utvärdering
- Tekniker för att förbättra agenters prestanda, kostnader och effektivitet
- Vad och hur du systematiskt utvärderar dina AI-agenter
- Hur du kontrollerar kostnader vid produktsättning av AI-agenter
- Hur du instrumenterar agenter byggda med Microsoft Agent Framework

Målet är att utrusta dig med kunskapen för att förvandla dina "svarta låda"-agenter till transparenta, hanterbara och pålitliga system.

_**Notera:** Det är viktigt att distribuera AI-agenter som är säkra och pålitliga. Kolla även in lektionen [Bygga pålitliga AI-agenter](../06-building-trustworthy-agents/README.md)._

## Traces och Spans

Observabilitetsverktyg som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar oftast agentkörningar som traces och spans.

- **Trace** representerar en komplett agentuppgift från start till slut (som att hantera en användarfråga).
- **Spans** är individuella steg inom trace (som att anropa en språkmodell eller hämta data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Utan observabilitet kan en AI-agent kännas som en "svart låda" - dess interna tillstånd och resonemang är opaka, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observabilitet blir agenter "glaslådor," som erbjuder transparens som är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett.

## Varför observabilitet är viktigt i produktionsmiljöer

Övergången av AI-agenter till produktionsmiljöer introducerar en ny uppsättning utmaningar och krav. Observabilitet är inte längre ett "trevligt att ha" utan en kritisk kapacitet:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller ger ett oväntat resultat ger observabilitetsverktyg traces som behövs för att identifiera felkällan. Detta är särskilt viktigt i komplexa agenter som kan involvera flera LLM-anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens och kostnadshantering**: AI-agenter förlitar sig ofta på LLM:er och andra externa API:er som faktureras per token eller anrop. Observabilitet möjliggör exakt spårning av dessa anrop, vilket hjälper till att identifiera operationer som är överdrivet långsamma eller dyra. Detta gör det möjligt för team att optimera prompts, välja effektivare modeller eller omdesigna arbetsflöden för att hantera driftkostnader och garantera en god användarupplevelse.
*   **Förtroende, säkerhet och regelefterlevnad**: I många tillämpningar är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observabilitet tillhandahåller en granskningskedja av agentens handlingar och beslut. Detta kan användas för att upptäcka och mildra problem som promptinjektion, generering av skadligt innehåll eller felhantering av personligt identifierbar information (PII). Till exempel kan du granska traces för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringsloopar**: Observabilitetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i verkliga världen kan team identifiera förbättringsområden, samla data för finjustering av modeller och verifiera effekterna av förändringar. Detta skapar en återkopplingsloop där produktionsinsikter från onlineutvärdering informerar offline-experiment och förfining, vilket leder till successivt bättre agentprestanda.

## Nyckelmetrik att följa

För att övervaka och förstå agentens beteende bör en rad metrik och signaler följas. Även om specifika mätvärden kan variera beroende på agentens syfte är några universellt viktiga.

Här är några av de vanligaste metrik som observabilitetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och individuella steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modellkallningar accelereras genom att använda en snabbare modell eller genom att köra modellkallningar parallellt.

**Kostnader:** Vad är kostnaden per agentkörning? AI-agenter förlitar sig på LLM-anrop som faktureras per token eller externa API:er. Frekvent verktygsanvändning eller många prompts kan snabbt öka kostnaderna. Om en agent exempelvis anropar en LLM fem gånger för marginella kvalitetsförbättringar måste du bedöma om kostnaden är motiverad eller om du kan minska antalet anrop eller använda en billigare modell. Realtidssövervakning kan också hjälpa till att identifiera oväntade toppar (t.ex. buggar som orsakar överdrivna API-loopar).

**Begäranfel:** Hur många förfrågningar misslyckades agenten med? Detta kan inkludera API-fel eller misslyckade verktygsanrop. För att göra din agent mer robust mot detta i produktion kan du sedan sätta upp fallback-mekanismer eller omförsök. T.ex. om LLM-leverantör A är nere kan du byta till LLM-leverantör B som backup.

**Användarfeedback:** Att implementera direkt användarutvärdering ger värdefulla insikter. Detta kan inkludera uttryckliga betyg (👍tummen upp/👎ner, ⭐1-5 stjärnor) eller textkommentarer. Konsekvent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat.

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan uttryckliga betyg. Det kan inkludera omformulering av fråga direkt, upprepade frågor eller klick på en försök-igen-knapp. T.ex. om du ser att användare upprepade gånger ställer samma fråga är detta ett tecken på att agenten inte fungerar som förväntat.

**Noggrannhet:** Hur ofta producerar agenten korrekta eller önskvärda resultat? Definitioner av noggrannhet varierar (t.ex. korrekt problemlösning, informationssökningens noggrannhet, användartillfredsställelse). Det första steget är att definiera vad framgång ser ut som för din agent. Du kan spåra noggrannhet via automatiska kontroller, utvärderingspoäng eller etiketter för uppgiftsfullföljande. Till exempel att markera traces som "lyckad" eller "misslyckad".

**Automatiserade utvärderingsmetoder:** Du kan också sätta upp automatiserade utvärderingar. Till exempel kan du använda en LLM för att poängsätta agentens output, t.ex. om den är hjälpsam, korrekt eller ej. Det finns även flera open source-bibliotek som hjälper dig att poängsätta olika aspekter av agenten. T.ex. [RAGAS](https://docs.ragas.io/) för RAG-agenter eller [LLM Guard](https://llm-guard.com/) för att upptäcka skadligt språk eller promptinjektion.

I praktiken ger en kombination av dessa metrik bäst täckning av en AI-agents hälsa. I detta kapitels [exempelnätbok](./code_samples/10-expense_claim-demo.ipynb) visar vi hur dessa metrik ser ut i verkliga exempel, men först lär vi oss hur ett typiskt utvärderingsarbetsflöde ser ut.

## Instrumentera din agent

För att samla in spårdata behöver du instrumentera din kod. Målet är att instrumentera agentkoden för att sända traces och metrik som kan fångas, bearbetas och visualiseras av en observabilitetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blivit en industristandard för LLM-observabilitet. Det tillhandahåller API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata.

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry spans till ett observabilitetsverktyg. Microsoft Agent Framework integreras med OpenTelemetry nativt. Nedan är ett exempel på instrumentering av en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentens körning spåras automatiskt
    pass
```

Exempelnätboken ([example notebook](./code_samples/10-expense_claim-demo.ipynb)) i detta kapitel kommer att visa hur du instrumenterar din MAF-agent.

**Manuell span-skapning:** Även om instrumenteringsbibliotek ger en bra baslinje finns det ofta fall där mer detaljerad eller anpassad information behövs. Du kan manuellt skapa spans för att lägga till anpassad applikationslogik. Viktigare är att de kan berika automatiskt eller manuellt skapade spans med anpassade attribut (även kända som taggar eller metadata). Dessa attribut kan inkludera affärsspecifik data, mellanberäkningar eller annan kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id` eller `model_version`.

Exempel på att skapa traces och spans manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentutvärdering

Observabilitet ger oss metrik, men utvärdering är processen att analysera dessa data (och utföra tester) för att avgöra hur väl en AI-agent presterar och hur den kan förbättras. Med andra ord, när du har de där traces och metrikerna, hur använder du dem för att bedöma agenten och fatta beslut?

Regelbunden utvärdering är viktig eftersom AI-agenter ofta är icke-deterministiska och kan utvecklas (genom uppdateringar eller drifttendens i modellbeteende) – utan utvärdering skulle du inte veta om din "smarta agent" verkligen gör sitt jobb bra eller om den har försämrats.

Det finns två kategorier av utvärderingar för AI-agenter: **onlineutvärdering** och **offlineutvärdering**. Båda är värdefulla och kompletterar varandra. Vi börjar vanligtvis med offlineutvärdering, eftersom detta är det minimala nödvändiga steget innan någon agent distribueras.

### Offlineutvärdering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med testdatamängder, inte liveanvändarfrågor. Du använder noggrant utvalda datamängder där du vet vad det förväntade resultatet eller korrekt beteende är, och kör sedan agenten på dessa.

Om du t.ex. byggt en agent för matematiska ordproblem kan du ha en [testdatamängd](https://huggingface.co/datasets/gsm8k) med 100 problem med kända svar. Offlineutvärdering görs ofta under utveckling (och kan vara en del av CI/CD-pipelines) för att kontrollera förbättringar eller skydda mot regression. Fördelen är att det är **upprepbart och du kan få tydliga noggrannhetsmetrik eftersom du har grunddata**. Du kan också simulera användarfrågor och mäta agentens svar mot idealiska svar eller använda automatiserade metrik som tidigare beskrivits.

Den centrala utmaningen med offlineutvärdering är att säkerställa att din testdatamängd är omfattande och förblir relevant – agenten kan prestera väl på en fast testuppsättning men möta mycket olika frågor i produktion. Därför bör du hålla testuppsättningar uppdaterade med nya kantfall och exempel som speglar verkliga scenarier. En blandning av små "skumtest"-fall och större utvärderingsuppsättningar är användbar: små uppsättningar för snabba kontroller och större för bredare prestandamått.

### Onlineutvärdering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en levande, verklig miljö, dvs under faktisk användning i produktion. Onlineutvärdering innebär att övervaka agentens prestanda på riktiga användarinteraktioner och kontinuerligt analysera resultat.

Till exempel kan du följa framgångsfrekvenser, användartillfredsställelsepoäng eller andra mätvärden på live-trafik. Fördelen med onlineutvärdering är att den **fångar saker du kanske inte förutser i en labbmiljö** – du kan observera modellavdrift över tid (om agentens effektivitet försämras när inmatningsmönster skiftar) och fånga oväntade frågor eller situationer som inte fanns i din testdata. Den ger en sann bild av hur agenten beter sig i verkligheten.

Onlineutvärdering involverar ofta insamling av implicit och explicit användarfeedback, som diskuterats, och eventuellt körning av skuggtester eller A/Btester (där en ny version av agenten körs parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få tillförlitliga etiketter eller poäng för live-interaktioner – du kan behöva förlita dig på användarfeedback eller efterföljande mätvärden (som om användaren klickade på resultatet).

### Kombinera de två

Online- och offlineutvärderingar är inte ömsesidigt uteslutande; de kompletterar varandra väl. Insikter från onlineövervakning (t.ex. nya typer av användarfrågor där agenten presterar dåligt) kan användas för att komplettera och förbättra offline-testdatamängder. Omvänt kan agenter som presterar väl i offline-tester mer självsäkert distribueras och övervakas online.

Faktum är att många team använder en loop:

_utvärdera offline -> distributera -> övervaka online -> samla nya felaktiga fall -> lägg till i offline-datamängden -> förfina agent -> upprepa_.

## Vanliga problem

När du distribuerar AI-agenter till produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras potentiella lösningar:

| **Problem**    | **Potentiell lösning**   |
| ------------- | ------------------ |
| AI-agenten utför inte uppgifter konsekvent | - Förfina prompten som ges till AI-agenten; var tydlig med mål.<br>- Identifiera var det kan hjälpa att dela upp uppgifter i deluppgifter och låta flera agenter hantera dem. |
| AI-agenten fastnar i oändliga loopar  | - Säkerställ att tydliga termineringsvillkor finns så agenten vet när processen ska stoppas.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell specialiserad på resonemangsuppgifter. |
| Verktygsanrop från AI-agenten fungerar inte bra   | - Testa och validera verktygets output utanför agentsystemet.<br>- Förfina definierade parametrar, prompts och namn på verktyg.  |
| Multi-agent-system fungerar inte konsekvent | - Förfina prompts till varje agent så att de är specifika och tydligt skilda från varandra.<br>- Bygg ett hierarkiskt system med en "routing"- eller kontrollagent som bestämmer vilken agent som är rätt. |

Många av dessa problem kan identifieras mer effektivt med observabilitet på plats. De traces och metriker vi diskuterade tidigare hjälper till att exakt lokalisera var i agentens arbetsflöde problem uppstår, vilket gör felsökning och optimering mycket mer effektivt.

## Hantera kostnader


Här är några strategier för att hantera kostnaderna för att driftsätta AI-agenter:

**Använda mindre modeller:** Små språkmodeller (SLMs) kan fungera bra för vissa agentliknande användningsfall och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur bra en SLM kommer att prestera i ditt användningsfall att bygga ett utvärderingssystem för att bestämma och jämföra prestanda mot större modeller. Överväg att använda SLM:er för enklare uppgifter som intentsklassificering eller parameterutvinning, medan du reserverar större modeller för komplexa resonemang.

**Använda en routermodell:** En liknande strategi är att använda en mångfald av modeller och storlekar. Du kan använda en LLM/SLM eller serverlös funktion för att dirigera förfrågningar baserat på komplexitet till de modeller som passar bäst. Detta hjälper också till att minska kostnader samtidigt som prestanda säkerställs för rätt uppgifter. Till exempel, dirigera enkla frågor till mindre, snabbare modeller och använd endast dyra stora modeller för komplexa resonemangsuppgifter.

**Cachelagring av svar:** Att identifiera vanliga förfrågningar och uppgifter och tillhandahålla svaren innan de går igenom ditt agentliknande system är ett bra sätt att minska volymen av liknande förfrågningar. Du kan till och med implementera ett flöde för att identifiera hur lik en förfrågan är dina cachelagrade förfrågningar med hjälp av mer grundläggande AI-modeller. Denna strategi kan avsevärt minska kostnader för ofta ställda frågor eller vanliga arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempelnotebooken för detta avsnitt](./code_samples/10-expense_claim-demo.ipynb) ska vi se exempel på hur vi kan använda observabilitetsverktyg för att övervaka och utvärdera vår agent.


### Fler frågor om AI-agenter i produktion?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstid och få dina frågor om AI-agenter besvarade.

## Föregående lektion

[Metakognitionsdesignmönster](../09-metacognition/README.md)

## Nästa lektion

[Agentiska protokoll](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->