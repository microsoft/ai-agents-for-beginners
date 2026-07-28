[![Hvordan man designer gode AI-agenter](../../../translated_images/da/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_
# AI Agentiske Designprincipper

## Introduktion

Der er mange måder at tænke på, når man bygger AI Agentiske Systemer. Da tvetydighed er en funktion og ikke en fejl i Generativ AI design, kan det nogle gange være svært for ingeniører at finde ud af, hvor de overhovedet skal starte. Vi har skabt et sæt menneskecentrerede UX Designprincipper for at gøre det muligt for udviklere at bygge kundecentrerede agentiske systemer, som løser deres forretningsbehov. Disse designprincipper er ikke en foreskrivende arkitektur, men snarere et udgangspunkt for teams, der definerer og udvikler agentoplevelser.

Generelt bør agenter:

- Udvide og skalere menneskelige kapaciteter (idéudvikling, problemløsning, automatisering osv.)
- Udfylde videnshuller (give mig opdateret indsigt i vidensdomæner, oversættelse osv.)
- Lettere og understøtte samarbejde på de måder, vi som individer foretrækker at arbejde med andre på
- Gøre os til bedre versioner af os selv (f.eks. livscoach/opgaveleder, hjælpe os med at lære følelsesmæssig regulering og mindfulness færdigheder, opbygge modstandskraft osv.)

## Denne lektion vil dække

- Hvad de Agentiske Designprincipper er
- Hvilke retningslinjer der bør følges ved implementering af disse designprincipper
- Eksempler på brug af designprincipperne

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

1. Forklare, hvad de Agentiske Designprincipper er
2. Forklare retningslinjerne for brug af de Agentiske Designprincipper
3. Forstå hvordan man bygger en agent ved hjælp af de Agentiske Designprincipper

## De Agentiske Designprincipper

![Agentiske Designprincipper](../../../translated_images/da/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Rum)

Dette er det miljø, hvor agenten opererer. Disse principper vejleder, hvordan vi designer agenter til at engagere sig i fysiske og digitale verdener.

- **Forbindelse, ikke sammenbrud** – hjælp med at forbinde mennesker med andre mennesker, begivenheder og håndterbar viden for at muliggøre samarbejde og forbindelse.
- Agenter hjælper med at forbinde begivenheder, viden og mennesker.
- Agenter bringer mennesker tættere sammen. De er ikke designet til at erstatte eller nedgøre mennesker.
- **Let tilgængelig men til tider usynlig** – agenten opererer stort set i baggrunden og skubber kun til os, når det er relevant og passende.
  - Agenten er let at finde og tilgå for autoriserede brugere på enhver enhed eller platform.
  - Agenten understøtter multimodale input og output (lyd, stemme, tekst osv.).
  - Agenten kan sømløst skifte mellem forgrund og baggrund; mellem proaktiv og reaktiv, afhængigt af dens vurdering af brugerens behov.
  - Agenten kan operere i en usynlig form, men dens baggrundsprocesbane og samarbejde med andre agenter er gennemsigtig og kontrollerbar af brugeren.

### Agent (Tid)

Sådan opererer agenten over tid. Disse principper vejleder, hvordan vi designer agenter, der interagerer på tværs af fortid, nutid og fremtid.

- **Fortid**: Reflekterer over historie, der inkluderer både tilstand og kontekst.
  - Agenten leverer mere relevante resultater baseret på analyse af rigere historiske data ud over kun begivenheden, personer eller tilstande.
  - Agenten skaber forbindelser fra tidligere begivenheder og reflekterer aktivt over hukommelsen for at engagere sig i aktuelle situationer.
- **Nu**: Skubber mere end bare notifikation.
  - Agenten indkapsler en omfattende tilgang til interaktion med mennesker. Når en begivenhed sker, går agenten videre end statisk notifikation eller anden statisk formalitet. Agenten kan forenkle flow eller dynamisk generere cues for at rette brugerens opmærksomhed på det rette tidspunkt.
  - Agenten leverer information baseret på kontekstuel omgivelse, sociale og kulturelle ændringer og tilpasset brugerens intention.
  - Agentinteraktion kan være gradvis, udviklende/voksende i kompleksitet for at styrke brugerne på længere sigt.
- **Fremtid**: Tilpasning og udvikling.
  - Agenten tilpasser sig forskellige enheder, platforme og modaliteter.
  - Agenten tilpasser sig brugeradfærd, tilgængelighedsbehov og er frit tilpasselig.
  - Agenten formes af og udvikler sig gennem kontinuerlig brugerinteraktion.

### Agent (Kerner)

Disse er nøgleelementerne i kernen i en agents design.

- **Omfavne usikkerhed men etablere tillid**.
  - Et vist niveau af agent-usikkerhed forventes. Usikkerhed er et nøgleelement i agentdesign.
  - Tillid og gennemsigtighed er grundlæggende lag i agentdesign.
  - Mennesker har kontrol over, hvornår agenten er tændt/slukket, og agentens status er klart synlig til enhver tid.

## Retningslinjer for at implementere disse principper

Når du bruger de tidligere designprincipper, skal du følge disse retningslinjer:

1. **Gennemsigtighed**: Informer brugeren om, at AI er involveret, hvordan den fungerer (inklusive tidligere handlinger), og hvordan der kan gives feedback og ændres på systemet.
2. **Kontrol**: Gør det muligt for brugeren at tilpasse, specificere præferencer og personificere samt have kontrol over systemet og dets egenskaber (inklusive muligheden for at glemme).
3. **Konsistens**: Sigter efter konsistente, multimodale oplevelser på tværs af enheder og endpoints. Brug velkendte UI/UX-elementer hvor muligt (f.eks. mikrofon-ikon til stemmeinteraktion) og reducer brugerens kognitive belastning så meget som muligt (f.eks. sigt efter korte svar, visuelle hjælpemidler og 'Lær mere'-indhold).

## Hvordan man designer en Rejseagent ved brug af disse principper og retningslinjer

Forestil dig, at du designer en Rejseagent, her er hvordan du kan tænke på at bruge Designprincipperne og retningslinjerne:

1. **Gennemsigtighed** – Lad brugeren vide, at Rejseagenten er en AI-aktiveret agent. Giv nogle grundlæggende instruktioner om, hvordan man kommer i gang (f.eks. en "Hej" besked, eksempler på prompts). Dokumenter dette tydeligt på produktsiden. Vis listen over prompts, som brugeren har stillet tidligere. Gør det klart, hvordan man kan give feedback (tommel op og ned, Send feedback-knap osv.). Angiv klart, om agenten har begrænsninger i brug eller emner.
2. **Kontrol** – Sørg for, at det er klart, hvordan brugeren kan ændre agenten efter den er oprettet med ting som System-prompten. Gør det muligt for brugeren at vælge, hvor detaljeret agenten skal være, dens skriftstil og eventuelle forbehold om, hvad agenten ikke bør tale om. Tillad brugeren at se og slette eventuelle tilknyttede filer eller data, prompts og tidligere samtaler.
3. **Konsistens** – Sørg for, at ikonerne for Del prompt, tilføj en fil eller foto og tag nogen eller noget er standardiserede og genkendelige. Brug papirclipsikonet til at indikere filupload/deling med agenten, og et billedeikon til at indikere grafikupload.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Flere spørgsmål om AI Agentiske Designmønstre?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://openai.com" target="_blank">Praksis for styring af agentiske AI-systemer | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">HAX Toolkit-projektet - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Ansvarlig AI-værktøjskasse</a>

## Forrige lektion

[Udforskning af agentiske frameworks](../02-explore-agentic-frameworks/README.md)

## Næste lektion

[Designmønster for værktøjsbrug](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->