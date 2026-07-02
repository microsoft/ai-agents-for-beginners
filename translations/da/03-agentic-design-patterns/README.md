[![Hvordan man designer gode AI-agenter](../../../translated_images/da/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_
# Principper for AI Agentisk Design

## Introduktion

Der er mange måder at tænke på opbygning af AI Agentiske Systemer. Da tvetydighed er en funktion og ikke en fejl i design af Generativ AI, kan det nogle gange være svært for ingeniører at finde ud af, hvor de overhovedet skal starte. Vi har skabt et sæt menneskecentrerede UX designprincipper for at gøre det muligt for udviklere at bygge kundecentrerede agentiske systemer, som løser deres forretningsbehov. Disse designprincipper er ikke en forskriftsmæssig arkitektur, men snarere et udgangspunkt for teams, der definerer og bygger agentoplevelser.

Generelt bør agenter:

- Udvide og skalere menneskelige kapaciteter (brainstorming, problemløsning, automatisering osv.)
- Udfylde videnshuller (bring mig op i fart inden for vidensdomæner, oversættelse osv.)
- Muliggøre og støtte samarbejde på den måde, vi som individer foretrækker at arbejde med andre på
- Gøre os til bedre versioner af os selv (fx livscoach/opgavemester, hjælpe os med at lære følelsesregulering og mindfulness færdigheder, opbygge modstandsdygtighed osv.)

## Denne lektion vil dække

- Hvad Agentiske Designprincipper er
- Hvad nogle retningslinjer er, som man skal følge under implementering af disse designprincipper
- Hvad nogle eksempler på brug af designprincipperne er

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

1. Forklare hvad Agentiske Designprincipper er
2. Forklare retningslinjerne for brug af Agentiske Designprincipper
3. Forstå hvordan man bygger en agent ved hjælp af Agentiske Designprincipper

## De Agentiske Designprincipper

![Agentiske Designprincipper](../../../translated_images/da/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Rum)

Dette er det miljø, hvor agenten opererer. Disse principper informerer om, hvordan vi designer agenter til at engagere sig i fysiske og digitale verdener.

- **At forbinde, ikke at ophæve** – hjælp med at forbinde mennesker til andre mennesker, begivenheder og handlingsrettet viden for at muliggøre samarbejde og forbindelse.
- Agenter hjælper med at forbinde begivenheder, viden og mennesker.
- Agenter bringer mennesker tættere sammen. De er ikke designet til at erstatte eller nedgøre mennesker.
- **Let tilgængelig, men undertiden usynlig** – agenten opererer stort set i baggrunden og skubber kun til os, når det er relevant og passende.
  - Agenten er let at finde og tilgå for autoriserede brugere på enhver enhed eller platform.
  - Agenten understøtter multimodale input og output (lyd, stemme, tekst osv.).
  - Agenten kan problemfrit skifte mellem forgrund og baggrund; mellem proaktiv og reaktiv, afhængigt af dens sansning af brugerens behov.
  - Agenten kan operere i usynlig form, men dens baggrundsprocessti og samarbejde med andre agenter er gennemsigtigt for og kontrollerbart af brugeren.

### Agent (Tid)

Sådan opererer agenten over tid. Disse principper informerer, hvordan vi designer agenter, der interagerer på tværs af fortid, nutid og fremtid.

- **Fortid**: Reflektere over historie som inkluderer både tilstand og kontekst.
  - Agenten giver mere relevante resultater baseret på analyse af rigere historiske data udover kun begivenheden, mennesker eller tilstande.
  - Agenten skaber forbindelser fra tidligere begivenheder og reflekterer aktivt over hukommelsen for at engagere sig i aktuelle situationer.
- **Nu**: At skubbe mere end at underrette.
  - Agenten legemliggør en helhedsorienteret tilgang til interaktion med mennesker. Når en begivenhed sker, går agenten ud over statisk notifikation eller anden statisk formalitet. Agenten kan forenkle flows eller dynamisk generere signaler til at rette brugerens opmærksomhed på det rette tidspunkt.
  - Agenten leverer information baseret på kontekstuel omgivelse, sociale og kulturelle forandringer og tilpasses brugerens intention.
  - Agentens interaktion kan være gradvis og udviklende/voksende i kompleksitet for at styrke brugerne på lang sigt.
- **Fremtid**: Tilpasse sig og udvikle sig.
  - Agenten tilpasser sig forskellige enheder, platforme og modaliteter.
  - Agenten tilpasser sig brugeradfærd, tilgængelighedsbehov og er frit tilpasselig.
  - Agenten formes af og udvikles gennem løbende brugerinteraktion.

### Agent (Kernen)

Dette er nøgleelementerne i kernen af en agents design.

- **Omfavn usikkerhed, men etabler tillid**.
  - Et vist niveau af agentusikkerhed forventes. Usikkerhed er et nøgleelement i agentdesign.
  - Tillid og gennemsigtighed er fundamentale lag i agentdesign.
  - Mennesker har kontrollen over, hvornår agenten er tændt/slukket, og agentstatus er klart synlig til enhver tid.

## Retningslinjerne for at implementere disse principper

Når du bruger de tidligere nævnte designprincipper, skal du bruge følgende retningslinjer:

1. **Gennemsigtighed**: Informer brugeren om, at AI er involveret, hvordan den fungerer (inklusive tidligere handlinger), og hvordan man giver feedback og ændrer systemet.
2. **Kontrol**: Giv brugeren mulighed for at tilpasse, specificere præferencer og personificere samt have kontrol over systemet og dets attributter (inklusive muligheden for at glemme).
3. **Konsistens**: Sigte efter konsistente, multimodale oplevelser på tværs af enheder og endepunkter. Brug velkendte UI/UX-elementer hvor det er muligt (fx mikrofonikon til stemmeinteraktion) og reducer kundens kognitive belastning så meget som muligt (fx sigt efter korte svar, visuelle hjælpemidler og 'Læs mere'-indhold).

## Hvordan man designer en rejseagent ved at bruge disse principper og retningslinjer

Forestil dig, at du designer en rejseagent, her er hvordan du kunne tænke på brugen af designprincipper og retningslinjer:

1. **Gennemsigtighed** – Lad brugeren vide, at rejseagenten er en AI-aktiveret agent. Giv nogle grundlæggende instruktioner om, hvordan man kommer i gang (fx en “Hej” besked, eksempel-prompt). Dokumentér dette tydeligt på produktsiden. Vis listen over prompts, brugeren har stillet tidligere. Gør det klart, hvordan man giver feedback (thumbs up og down, Send Feedback-knap osv.). Angiv tydeligt, hvis agenten har brug eller emnebegrænsninger.
2. **Kontrol** – Sørg for, at det er klart, hvordan brugeren kan ændre agenten, efter den er oprettet med ting som System Prompt. Giv brugeren mulighed for at vælge, hvor detaljeret agenten skal være, dens skrivestil og eventuelle forbehold om, hvad agenten ikke bør tale om. Lad brugeren se og slette alle tilknyttede filer eller data, prompts og tidligere samtaler.
3. **Konsistens** – Sørg for, at ikonerne til deling af prompt, tilføjelse af en fil eller foto og tagge nogen eller noget er standard og genkendelige. Brug clipsikonet til at indikere filupload/-deling med agenten og et billedeikon til at indikere grafik-upload.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI Agentiske Designmønstre?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i åbningstider og få besvaret dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://openai.com" target="_blank">Praksis for styring af agentiske AI-systemer | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">The HAX Toolkit Project - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Forrige lektion

[Udforskning af agentiske frameworks](../02-explore-agentic-frameworks/README.md)

## Næste lektion

[Designtema for værktøjsbrug](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->