# AI-agenter i produktion: Observerbarhet och utvärdering

[![AI Agents in Production](../../../translated_images/sv/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

När AI-agenter går från experimentella prototyper till verkliga tillämpningar blir förmågan att förstå deras beteende, övervaka deras prestanda och systematiskt utvärdera deras resultat viktig.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna/veta:
- Kärnbegrepp för agentobserverbarhet och utvärdering
- Tekniker för att förbättra agenters prestanda, kostnader och effektivitet
- Vad och hur du systematiskt utvärderar dina AI-agenter
- Hur du styr kostnader vid produktionstillämpning av AI-agenter
- Hur du instrumenterar agenter byggda med Microsoft Agent Framework

Målet är att ge dig kunskap för att omvandla dina "svarta låda"-agenter till transparenta, hanterbara och pålitliga system.

_**Notera:** Det är viktigt att distribuera AI-agenter som är säkra och pålitliga. Ta även en titt på lektionen [Bygga pålitliga AI-agenter](../06-building-trustworthy-agents/README.md)._

## Spår och Spännvidder

Observerbarhetsverktyg som [Langfuse](https://langfuse.com/) eller [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representerar vanligtvis agentkörningar som spår och spännvidder.

- **Spår** representerar en komplett agentuppgift från början till slut (som att hantera en användarförfrågan).
- **Spännvidder** är individuella steg inom spåret (som att anropa en språkmodell eller hämta data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Utan observerbarhet kan en AI-agent kännas som en "svart låda" – dess interna tillstånd och resonemang är ogenomskinliga, vilket gör det svårt att diagnostisera problem eller optimera prestanda. Med observerbarhet blir agenter "glaslådor", vilket erbjuder transparens som är avgörande för att bygga förtroende och säkerställa att de fungerar som avsett.

## Varför observerbarhet är viktig i produktionsmiljöer

Att överföra AI-agenter till produktionsmiljöer innebär nya utmaningar och krav. Observerbarhet är inte längre en "trevlig att ha" utan en kritisk förmåga:

*   **Felsökning och rotorsaksanalys**: När en agent misslyckas eller ger ett oväntat resultat ger observerbarhetsverktyg de spår som behövs för att identifiera felkällan. Detta är särskilt viktigt i komplexa agenter som kan involvera flera LLM-anrop, verktygsinteraktioner och villkorlig logik.
*   **Latens- och kostnadshantering**: AI-agenter förlitar sig ofta på LLM:er och andra externa API:er som debiteras per token eller per anrop. Observerbarhet möjliggör exakt spårning av dessa anrop, vilket hjälper till att identifiera operationer som är alltför långsamma eller kostsamma. Detta gör det möjligt för team att optimera prompts, välja mer effektiva modeller eller omdesigna arbetsflöden för att hantera driftskostnader och säkerställa en god användarupplevelse.
*   **Förtroende, säkerhet och efterlevnad**: I många tillämpningar är det viktigt att säkerställa att agenter beter sig säkert och etiskt. Observerbarhet tillhandahåller en revisionskedja av agentens handlingar och beslut. Detta kan användas för att upptäcka och mildra problem som prompt-injektion, generering av skadligt innehåll eller hantering av personligt identifierbar information (PII). Till exempel kan du granska spår för att förstå varför en agent gav ett visst svar eller använde ett specifikt verktyg.
*   **Kontinuerliga förbättringsslingor**: Observerbarhetsdata är grunden för en iterativ utvecklingsprocess. Genom att övervaka hur agenter presterar i den verkliga världen kan team identifiera förbättringsområden, samla data för finjustering av modeller och validera effekten av förändringar. Detta skapar en återkopplingsslinga där produktionsinsikter från online-utvärdering informerar offline-experiment och förfining, vilket leder till successivt bättre agentprestanda.

## Nyckelmått att följa

För att övervaka och förstå agentens beteende bör en rad mätvärden och signaler följas. Även om specifika mått kan variera beroende på agentens syfte, är vissa universellt viktiga.

Här är några av de vanligaste mätvärden som observerbarhetsverktyg övervakar:

**Latens:** Hur snabbt svarar agenten? Långa väntetider påverkar användarupplevelsen negativt. Du bör mäta latens för uppgifter och individuella steg genom att spåra agentkörningar. Till exempel kan en agent som tar 20 sekunder för alla modell-anrop accelereras genom att använda en snabbare modell eller genom att köra modell-anrop parallellt.

**Kostnader:** Vad kostar varje agentkörning? AI-agenter använder LLM-anrop som debiteras per token eller externa API:er. Frekvent verktygsanvändning eller flera prompts kan snabbt öka kostnaderna. Till exempel, om en agent anropar en LLM fem gånger för att förbättra marginal kvalitet, måste du bedöma om kostnaden är motiverad eller om antalet anrop kan minskas eller en billigare modell användas. Realtidsövervakning kan också hjälpa dig att identifiera oväntade toppar (t.ex. buggar som orsakar överdrivna API-loopar).

**Förfrågningsfel:** Hur många förfrågningar misslyckades agenten med? Detta kan inkludera API-fel eller misslyckade verktygsanrop. För att göra din agent mer robust mot dessa i produktion kan du då sätta upp fallback-mekanismer eller omförsök. T.ex. om LLM-leverantör A är nere, byter du till LLM-leverantör B som backup.

**Användarfeedback:** Implementering av direkt användarvärdering ger värdefulla insikter. Detta kan inkludera explicita betyg (👍tummen upp/👎ner, ⭐1-5 stjärnor) eller textkommentarer. Konsistent negativ feedback bör varna dig eftersom det är ett tecken på att agenten inte fungerar som förväntat.

**Implicit användarfeedback:** Användarbeteenden ger indirekt feedback även utan explicita betyg. Detta kan inkludera omedelbar omformulering av frågor, upprepade frågor eller klick på en retry-knapp. T.ex. om du ser att användare upprepade gånger ställer samma fråga är detta ett tecken på att agenten inte fungerar som förväntat.

**Precision:** Hur ofta producerar agenten korrekta eller önskvärda resultat? Definitionen av precision varierar (t.ex. korrekta problemlösningar, träffsäkerhet vid informationshämtning, användartillfredsställelse). Det första steget är att definiera vad framgång innebär för din agent. Du kan följa precision genom automatiska kontroller, utvärderingspoäng eller märka uppgiftsfullföljanden. Till exempel att märka spår som ”lyckade” eller ”misslyckade”.

**Automatiserade utvärderingsmått:** Du kan också sätta upp automatiserade utvärderingar. Till exempel kan du använda en LLM för att poängsätta agentens utdata, t.ex. om den är hjälpsam, korrekt eller inte. Det finns också flera open source-bibliotek som hjälper dig att poängsätta olika aspekter av agenten. T.ex. [RAGAS](https://docs.ragas.io/) för RAG-agenter eller [LLM Guard](https://github.com/protectai/llm-guard) för att upptäcka skadligt språk eller prompt-injektion.

I praktiken ger en kombination av dessa mått bäst täckning av en AI-agents hälsa. I detta kapitel [exempelnötebok](./code_samples/10-expense_claim-demo.ipynb) visar vi hur dessa mått ser ut i riktiga exempel, men först lär vi oss hur en typisk utvärderingsarbetsflöde ser ut.

## Instrumentera din agent

För att samla in spårningsdata behöver du instrumentera din kod. Målet är att instrumentera agentkoden för att sända ut spår och mätvärden som kan fångas, bearbetas och visualiseras av en observerbarhetsplattform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) har blivit en industristandard för LLM-observerbarhet. Det erbjuder ett sett API:er, SDK:er och verktyg för att generera, samla in och exportera telemetridata.

Det finns många instrumenteringsbibliotek som omsluter befintliga agentramverk och gör det enkelt att exportera OpenTelemetry-spännvidder till ett observerbarhetsverktyg. Microsoft Agent Framework integreras med OpenTelemetry inbyggt. Nedan är ett exempel på hur man instrumenterar en MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

[Exempelnöteboken](./code_samples/10-expense_claim-demo.ipynb) i detta kapitel kommer att visa hur du instrumenterar din MAF-agent.

**Manuell spännviddsskapande:** Även om instrumenteringsbibliotek ger en bra utgångspunkt finns det ofta fall där mer detaljerad eller anpassad information behövs. Du kan manuellt skapa spännvidder för att lägga till anpassad applikationslogik. Viktigare är att de kan berika automatiskt eller manuellt skapade spännvidder med egna attribut (även kallade taggar eller metadata). Dessa attribut kan inkludera affärsspecifik data, mellanliggande beräkningar eller annan kontext som kan vara användbar för felsökning eller analys, såsom `user_id`, `session_id` eller `model_version`.

Exempel på att skapa spår och spännvidder manuellt med [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentutvärdering

Observerbarhet ger oss mätvärden, men utvärdering är processen att analysera dessa data (och utföra tester) för att avgöra hur väl en AI-agent presterar och hur den kan förbättras. Med andra ord, när du har dessa spår och mätvärden, hur använder du dem för att bedöma agenten och fatta beslut?

Regelbunden utvärdering är viktigt eftersom AI-agenter ofta är icke-deterministiska och kan förändras (genom uppdateringar eller förskjutning i modellbeteende) – utan utvärdering skulle du inte veta om din "smarta agent" faktiskt gör sitt jobb bra eller om den har försämrats.

Det finns två kategorier av utvärderingar för AI-agenter: **online-utvärdering** och **offline-utvärdering**. Båda är värdefulla och kompletterar varandra. Vi börjar vanligtvis med offline-utvärdering, eftersom detta är det minsta nödvändiga steget innan en agent distribueras.

### Offline-utvärdering

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Detta innebär att utvärdera agenten i en kontrollerad miljö, vanligtvis med hjälp av testdatasätt, inte levande användarförfrågningar. Du använder kurerade datasätt där du vet vad det förväntade resultatet eller rätta beteendet är och kör sedan din agent på dessa.

Till exempel, om du byggt en agent för matteordproblem kan du ha ett [testdatasätt](https://huggingface.co/datasets/openai/gsm8k) med 100 problem och kända svar. Offline-utvärdering görs ofta under utveckling (och kan vara del av CI/CD-pipelines) för att kontrollera förbättringar eller förhindra regression. Fördelen är att det är **upprepbart och du kan få tydliga precision mått eftersom du har grundfakta**. Du kan också simulera användarfrågor och mäta agentens svar mot idealiska svar eller använda automatiserade mått som beskrivits ovan.

Den största utmaningen med offline-utvärdering är att säkerställa att ditt testdatasätt är omfattande och håller sig relevant – agenten kan prestera bra på en fast testuppsättning men stöta på mycket annorlunda förfrågningar i produktion. Därför bör du kontinuerligt uppdatera testsatser med nya gränsfall och exempel som speglar verkliga scenarier​. En mix av små ”rökprov” och större utvärderingssatser är användbart: små set för snabba kontroller och större för bredare prestandamått​.

### Online-utvärdering

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Detta avser att utvärdera agenten i en levande, verklig miljö, dvs. under faktisk användning i produktion. Online-utvärdering innebär att övervaka agentens prestanda på verkliga användarinteraktioner och kontinuerligt analysera resultat.

Till exempel kan du följa framgångsfrekvenser, användartillfredsställelsepoäng eller andra mått på levande trafik. Fördelen med online-utvärdering är att den **fångar upp saker du kanske inte förutser i ett labb** – du kan observera modellförskjutningar över tid (om agentens effektivitet minskar när inmatningsmönster förändras) och fånga oväntade förfrågningar eller situationer som inte finns i ditt testdata​. Den ger en sann bild av hur agenten beter sig i det vilda.

Online-utvärdering inkluderar ofta insamling av implicit och explicit användarfeedback, som diskuterats, och eventuellt körning av shadow-tester eller A/B-tester (där en ny version av agenten kör parallellt för att jämföras med den gamla). Utmaningen är att det kan vara svårt att få tillförlitliga etiketter eller poäng för levande interaktioner – du kan behöva förlita dig på användarfeedback eller nedströms-mått (t.ex. om användaren klickade på resultatet).

### Kombinera de två

Online- och offline-utvärderingar utesluter inte varandra; de kompletterar varandra mycket väl. Insikter från online-övervakning (t.ex. nya typer av användarförfrågningar där agenten presterar dåligt) kan användas för att utöka och förbättra offline-testdatasätt. Omvänt kan agenter som presterar bra i offline-tester med större tillförsikt distribueras och övervakas online.

Många team arbetar faktiskt i en slinga:

_utvärdera offline -> distribuera -> övervaka online -> samla nya felaktiga fall -> lägg till i offline-datasättet -> förfina agent -> upprepa_.

## Vanliga problem

När du distribuerar AI-agenter till produktion kan du stöta på olika utmaningar. Här är några vanliga problem och deras potentiella lösningar:

| **Problem**    | **Potentiell lösning**   |
| ------------- | ------------------ |
| AI-agenten utför inte uppgifter konsekvent | - Förfina prompten till AI-agenten; var tydlig med målen.<br>- Identifiera var uppgifter kan delas upp i deluppgifter och hanteras av flera agenter. |
| AI-agent fastnar i oändliga loopar | - Säkerställ tydliga avslutsvillkor så att agenten vet när processen ska stoppas.<br>- För komplexa uppgifter som kräver resonemang och planering, använd en större modell som är specialiserad för sådana uppgifter. |
| AI-agentens verktygsanrop fungerar inte bra | - Testa och validera verktygets utdata utanför agentsystemet.<br>- Förfina definierade parametrar, prompts och namngivning av verktyg. |
| Multi-agent-system presterar inkonsekvent | - Förfina prompts till varje agent för att säkerställa att de är specifika och distinkta.<br>- Bygg ett hierarkiskt system med en "routing"- eller controller-agent som avgör vilken agent som är rätt. |

Många av dessa problem kan identifieras mer effektivt med observerbarhet på plats. De spår och mätvärden vi diskuterade tidigare hjälper till att precis identifiera var i agentarbetsflödet problem uppstår, vilket gör felsökning och optimering mycket effektivare.

## Hantering av kostnader

Här är några strategier för att hantera kostnader vid produktion av AI-agenter:

**Använda mindre modeller:** Små språkmodeller (SLM) kan prestera bra på vissa agentiska användningsfall och kommer att minska kostnaderna avsevärt. Som nämnts tidigare är det bästa sättet att förstå hur bra en SLM kommer att prestera för ditt användningsfall att bygga ett utvärderingssystem för att bestämma och jämföra prestanda mot större modeller. Överväg att använda SLM för enklare uppgifter som intentsklassificering eller parameterutvinning, medan större modeller reserveras för komplex resonemang.

**Använda en routermodell:** En liknande strategi är att använda en variation av modeller och storlekar. Du kan använda en LLM/SLM eller serverlös funktion för att routa förfrågningar baserat på komplexitet till de modeller som passar bäst. Detta hjälper också att minska kostnader samtidigt som prestanda för rätt uppgifter säkerställs. Till exempel, rutta enkla frågor till mindre, snabbare modeller och använd bara dyra stora modeller för komplexa resonemangsuppgifter.

**Caching av svar:** Att identifiera vanliga förfrågningar och uppgifter och tillhandahålla svaren innan de går igenom ditt agentiska system är ett bra sätt att minska volymen av liknande förfrågningar. Du kan till och med implementera ett flöde för att avgöra hur lik en förfrågan är dina cachade förfrågningar med hjälp av enklare AI-modeller. Denna strategi kan avsevärt minska kostnader för ofta ställda frågor eller vanliga arbetsflöden.

## Låt oss se hur detta fungerar i praktiken

I [exempeln i den här sektionens anteckningsbok](./code_samples/10-expense_claim-demo.ipynb) kommer vi att se exempel på hur vi kan använda observabilitetsverktyg för att övervaka och utvärdera vår agent.


### Fler frågor om AI-agenter i produktion?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstid och få svar på dina frågor om AI-agenter.

## Föregående lektion

[Metacognition Design Pattern](../09-metacognition/README.md)

## Nästa lektion

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->