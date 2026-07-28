[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klikk på bildet over for å se video av denne leksjonen)_
# Prinsipper for AI-agentisk design

## Introduksjon

Det finnes mange måter å tenke på når man bygger AI-agentiske systemer. Siden tvetydighet er en egenskap og ikke en feil i generativ AI-design, kan det noen ganger være vanskelig for ingeniører å finne ut hvor de skal begynne. Vi har laget et sett med menneskesentrerte UX-designprinsipper for å hjelpe utviklere med å bygge kundeorienterte agentiske systemer som løser deres forretningsbehov. Disse designprinsippene er ikke en forskriftsmessig arkitektur, men snarere et utgangspunkt for team som definerer og bygger ut agentopplevelser.

Generelt bør agenter:

- Utvide og skalere menneskelige evner (idémyldring, problemløsning, automatisering osv.)
- Fylle inn kunnskapshull (gjøre meg oppdatert på kunnskapsdomener, oversettelse osv.)
- Legge til rette for og støtte samarbeid på de måtene vi som individer foretrekker å jobbe med andre
- Gjøre oss til bedre versjoner av oss selv (f.eks. livscoach/oppgaveleder, hjelpe oss å lære emosjonell regulering og mindfulness-ferdigheter, bygge motstandskraft osv.)

## Denne leksjonen vil dekke

- Hva agentiske designprinsipper er
- Noen retningslinjer for implementering av disse designprinsippene
- Eksempler på bruk av designprinsippene

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

1. Forklare hva agentiske designprinsipper er
2. Forklare retningslinjene for bruk av agentiske designprinsipper
3. Forstå hvordan man bygger en agent ved å bruke agentiske designprinsipper

## Agentiske designprinsipper

![Agentiske designprinsipper](../../../translated_images/no/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Rom)

Dette er miljøet agenten opererer i. Disse prinsippene veileder hvordan vi designer agenter for å delta i fysiske og digitale verdener.

- **Koble sammen, ikke kollapse** – hjelp til med å koble mennesker til andre mennesker, hendelser og handlingsrettet kunnskap for å muliggjøre samarbeid og tilknytning.
- Agenter hjelper med å koble hendelser, kunnskap og mennesker.
- Agenter bringer folk nærmere hverandre. De er ikke designet for å erstatte eller nedvurdere mennesker.
- **Lett tilgjengelig, men av og til usynlig** – agenten opererer stort sett i bakgrunnen og guider oss bare når det er relevant og passende.
  - Agenten er lett å finne og tilgjengelig for autoriserte brukere på alle enheter eller plattformer.
  - Agenten støtter multimodale inn- og utdata (lyd, tale, tekst osv.).
  - Agenten kan sømløst veksle mellom forgrunn og bakgrunn; mellom proaktiv og reaktiv, avhengig av hvordan den oppfatter brukerbehov.
  - Agenten kan operere i usynlig form, men dens bakgrunnsprosess og samarbeid med andre agenter er transparente og styrbare for brukeren.

### Agent (Tid)

Dette beskriver hvordan agenten opererer over tid. Disse prinsippene veileder hvordan vi designer agenter som samhandler på tvers av fortid, nåtid og fremtid.

- **Fortid**: Reflektere over historie som inkluderer både tilstand og kontekst.
  - Agenten gir mer relevante resultater basert på analyse av rikere historiske data utover bare hendelsen, menneskene eller tilstandene.
  - Agenten skaper forbindelser fra tidligere hendelser og reflekterer aktivt over minnet for å engasjere seg i nåværende situasjoner.
- **Nå**: Veilede mer enn å varsle.
  - Agenten embodies en omfattende tilnærming til samhandling med mennesker. Når en hendelse skjer, går agenten utover statisk varsling eller annen statisk formalitet. Agenten kan forenkle prosesser eller dynamisk generere signaler for å rette brukerens oppmerksomhet til rett tid.
  - Agenten leverer informasjon basert på kontekstuell miljø, sosiale og kulturelle endringer og tilpasset brukerens intensjon.
  - Agentens interaksjon kan være gradvis, utvikle/vokse i kompleksitet for å styrke brukerne over tid.
- **Fremtid**: Tilpasse og utvikle seg.
  - Agenten tilpasser seg ulike enheter, plattformer og modaliteter.
  - Agenten tilpasser seg brukeradferd, tilgjengelighetsbehov og er fritt tilpassbar.
  - Agenten formes av og utvikler seg gjennom kontinuerlig brukerinteraksjon.

### Agent (Kjerne)

Dette er nøkkel elementene i kjernen av agentens design.

- **Omfavn usikkerhet, men etabler tillit**.
  - Et visst nivå av usikkerhet hos agenten er forventet. Usikkerhet er et sentralt element i agentdesign.
  - Tillit og åpenhet er grunnleggende lag i agentdesign.
  - Mennesker har kontroll over når agenten er på/av og agentens status er tydelig synlig til enhver tid.

## Retningslinjer for å implementere disse prinsippene

Når du bruker de foregående designprinsippene, følg disse retningslinjene:

1. **Åpenhet**: Informer brukeren om at AI er involvert, hvordan den fungerer (inkludert tidligere handlinger) og hvordan gi tilbakemeldinger og endre systemet.
2. **Kontroll**: Gi brukeren mulighet til å tilpasse, spesifisere preferanser og personalisere, samt ha kontroll over systemet og dets egenskaper (inkludert mulighet til å glemme).
3. **Konsistens**: Sikre konsistente, multimodale opplevelser på tvers av enheter og endepunkter. Bruk kjente UI/UX-elementer der det er mulig (f.eks. mikrofonikon for taleinteraksjon) og reduser brukerens kognitive belastning så mye som mulig (f.eks. kortfattede svar, visuelle hjelpemidler og 'Lær mer'-innhold).

## Hvordan designe en reiseagent ved å bruke disse prinsippene og retningslinjene

Tenk deg at du designer en reiseagent, her er hvordan du kan tenke om bruk av designprinsippene og retningslinjene:

1. **Åpenhet** – La brukeren vite at reiseagenten er en AI-aktivert agent. Gi noen grunnleggende instruksjoner om hvordan komme i gang (f.eks. en "Hei"-melding, eksempelspørsmål). Dokumenter dette tydelig på produktsiden. Vis listen over spørsmål brukeren har stilt tidligere. Gjør det klart hvordan man gir tilbakemeldinger (tommel opp og ned, Send tilbakemeldingsknapp osv.). Klargjør eventuelle bruks- eller tema-restriksjoner for agenten.
2. **Kontroll** – Sørg for at det er klart hvordan brukeren kan endre agenten etter at den er opprettet, med ting som System Prompt. La brukeren velge hvor detaljert agenten skal være, dens skrivestil og eventuelle forbehold om hva agenten ikke skal snakke om. La brukeren se og slette tilknyttede filer eller data, spørsmål og tidligere samtaler.
3. **Konsistens** – Sørg for at ikonene for Del spørsmål, legge til fil eller bilde og merke noen eller noe er standard og lett gjenkjennelige. Bruk bindersikonet for å indikere filopplasting/deling med agenten, og et bildeikon for å indikere grafikkopplasting.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Har du flere spørsmål om AI-agentiske designmønstre?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine AI-agentspørsmål.

## Ekstra ressurser

- <a href="https://openai.com" target="_blank">Praksiser for styring av agentiske AI-systemer | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">HAX Toolkit Project - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Forrige leksjon

[Utforske agentiske rammeverk](../02-explore-agentic-frameworks/README.md)

## Neste leksjon

[Designmønster for verktøybruk](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->