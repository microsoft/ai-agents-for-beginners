<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d71524fe83a23829ae7a23b4031aaac8",
  "translation_date": "2025-11-13T12:55:04+00:00",
  "source_file": "03-agentic-design-patterns/README.md",
  "language_code": "no"
}
-->
[![Hvordan designe gode AI-agenter](../../../translated_images/lesson-3-thumbnail.1092dd7a8f1074a5b26e35aa8f810814e05a22fed1765c20c14b2b508c7ae379.no.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_
# Prinsipper for design av AI-agenter

## Introduksjon

Det finnes mange måter å tenke på når det gjelder å bygge AI-agentiske systemer. Siden tvetydighet er en funksjon og ikke en feil i design av generativ AI, kan det noen ganger være vanskelig for ingeniører å vite hvor de skal begynne. Vi har laget et sett med menneskesentrerte UX-designprinsipper for å gjøre det mulig for utviklere å bygge kundesentrerte agentiske systemer som løser deres forretningsbehov. Disse designprinsippene er ikke en foreskrevet arkitektur, men snarere et utgangspunkt for team som definerer og bygger agentopplevelser.

Generelt bør agenter:

- Utvide og skalere menneskelige evner (idémyldring, problemløsning, automatisering, osv.)
- Fylle kunnskapshull (gi meg en rask innføring i kunnskapsområder, oversettelse, osv.)
- Legge til rette for og støtte samarbeid på måter vi som individer foretrekker å jobbe med andre
- Gjøre oss til bedre versjoner av oss selv (f.eks. livscoach/oppgavemester, hjelpe oss med å lære emosjonell regulering og mindfulness-ferdigheter, bygge motstandskraft, osv.)

## Denne leksjonen vil dekke

- Hva er de agentiske designprinsippene
- Hvilke retningslinjer bør følges når man implementerer disse designprinsippene
- Eksempler på bruk av designprinsippene

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

1. Forklare hva de agentiske designprinsippene er
2. Forklare retningslinjene for bruk av de agentiske designprinsippene
3. Forstå hvordan man bygger en agent ved hjelp av de agentiske designprinsippene

## De agentiske designprinsippene

![Agentiske designprinsipper](../../../translated_images/agentic-design-principles.1cfdf8b6d3cc73c2b738951ee7b2043e224441d98babcf654be69d866120f93a.no.png)

### Agent (Rom)

Dette er miljøet der agenten opererer. Disse prinsippene informerer hvordan vi designer agenter for å engasjere seg i fysiske og digitale verdener.

- **Koble sammen, ikke bryte ned** – hjelp til med å koble mennesker til andre mennesker, hendelser og handlingsbar kunnskap for å muliggjøre samarbeid og tilknytning.
- Agenter hjelper til med å koble hendelser, kunnskap og mennesker.
- Agenter bringer mennesker nærmere hverandre. De er ikke designet for å erstatte eller nedvurdere mennesker.
- **Lett tilgjengelig, men av og til usynlig** – agenten opererer stort sett i bakgrunnen og gir oss bare et dytt når det er relevant og passende.
  - Agenten er lett å oppdage og tilgjengelig for autoriserte brukere på alle enheter eller plattformer.
  - Agenten støtter multimodale inn- og utganger (lyd, stemme, tekst, osv.).
  - Agenten kan sømløst skifte mellom forgrunn og bakgrunn; mellom proaktiv og reaktiv, avhengig av brukerens behov.
  - Agenten kan operere i usynlig form, men dens bakgrunnsprosess og samarbeid med andre agenter er transparente og kontrollerbare for brukeren.

### Agent (Tid)

Dette er hvordan agenten opererer over tid. Disse prinsippene informerer hvordan vi designer agenter som interagerer på tvers av fortid, nåtid og fremtid.

- **Fortid**: Reflektere over historien som inkluderer både tilstand og kontekst.
  - Agenten gir mer relevante resultater basert på analyse av rikere historiske data utover bare hendelsen, mennesker eller tilstander.
  - Agenten skaper forbindelser fra tidligere hendelser og reflekterer aktivt over minne for å engasjere seg i nåværende situasjoner.
- **Nå**: Gi et dytt mer enn en varsling.
  - Agenten har en helhetlig tilnærming til å interagere med mennesker. Når en hendelse skjer, går agenten utover statisk varsling eller annen statisk formalitet. Agenten kan forenkle prosesser eller dynamisk generere signaler for å rette brukerens oppmerksomhet på riktig tidspunkt.
  - Agenten leverer informasjon basert på kontekstuell miljø, sosiale og kulturelle endringer og tilpasset brukerens intensjon.
  - Agentens interaksjon kan være gradvis, utvikle seg i kompleksitet for å styrke brukeren over tid.
- **Fremtid**: Tilpasse seg og utvikle seg.
  - Agenten tilpasser seg ulike enheter, plattformer og modaliteter.
  - Agenten tilpasser seg brukerens atferd, tilgjengelighetsbehov og er fritt tilpassbar.
  - Agenten formes av og utvikler seg gjennom kontinuerlig brukerinteraksjon.

### Agent (Kjerne)

Dette er de sentrale elementene i kjernen av en agents design.

- **Omfavn usikkerhet, men etabler tillit**.
  - Et visst nivå av usikkerhet hos agenten er forventet. Usikkerhet er et nøkkelaspekt ved agentdesign.
  - Tillit og transparens er grunnleggende lag i agentdesign.
  - Mennesker har kontroll over når agenten er på/av, og agentens status er alltid tydelig synlig.

## Retningslinjer for implementering av disse prinsippene

Når du bruker de tidligere designprinsippene, følg disse retningslinjene:

1. **Transparens**: Informer brukeren om at AI er involvert, hvordan det fungerer (inkludert tidligere handlinger), og hvordan man kan gi tilbakemelding og endre systemet.
2. **Kontroll**: Gi brukeren mulighet til å tilpasse, spesifisere preferanser og personalisere, og ha kontroll over systemet og dets attributter (inkludert muligheten til å glemme).
3. **Konsistens**: Sikt mot konsistente, multimodale opplevelser på tvers av enheter og endepunkter. Bruk kjente UI/UX-elementer der det er mulig (f.eks. mikrofonikon for stemmeinteraksjon) og reduser brukerens kognitive belastning så mye som mulig (f.eks. sikt mot korte svar, visuelle hjelpemidler og ‘Lær mer’-innhold).

## Hvordan designe en reiseagent ved hjelp av disse prinsippene og retningslinjene

Tenk deg at du designer en reiseagent, her er hvordan du kan bruke designprinsippene og retningslinjene:

1. **Transparens** – La brukeren vite at reiseagenten er en AI-drevet agent. Gi noen grunnleggende instruksjoner om hvordan man kommer i gang (f.eks. en “Hei”-melding, eksempelforespørsler). Dokumenter dette tydelig på produktsiden. Vis listen over forespørsler en bruker har stilt tidligere. Gjør det klart hvordan man gir tilbakemelding (tommel opp og ned, Send tilbakemelding-knapp, osv.). Klargjør om agenten har bruks- eller emnebegrensninger.
2. **Kontroll** – Sørg for at det er tydelig hvordan brukeren kan endre agenten etter at den er opprettet, med ting som systemprompt. Gi brukeren mulighet til å velge hvor detaljert agenten skal være, dens skrivestil, og eventuelle forbehold om hva agenten ikke skal snakke om. Tillat brukeren å se og slette tilknyttede filer eller data, forespørsler og tidligere samtaler.
3. **Konsistens** – Sørg for at ikonene for Del forespørsel, legg til en fil eller et bilde og tagge noen eller noe er standard og gjenkjennelige. Bruk bindersikonet for å indikere filopplasting/deling med agenten, og et bildeikon for å indikere opplasting av grafikk.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)

## Har du flere spørsmål om agentiske designmønstre for AI?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre elever, delta på kontortid og få svar på spørsmålene dine om AI-agenter.

## Tilleggsressurser

- <a href="https://openai.com" target="_blank">Praksis for styring av agentiske AI-systemer | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">HAX Toolkit-prosjektet - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Forrige leksjon

[Utforske agentiske rammeverk](../02-explore-agentic-frameworks/README.md)

## Neste leksjon

[Designmønster for verktøybruk](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->