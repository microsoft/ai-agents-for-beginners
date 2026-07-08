[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_
# AI-agentiske designprinsipper

## Introduksjon

Det finnes mange måter å tenke på når man bygger AI-agentiske systemer. Siden tvetydighet er en funksjon og ikke en feil i Generativ AI-design, er det noen ganger vanskelig for ingeniører å finne ut hvor de skal begynne. Vi har laget et sett med menneskesentrerte UX-designprinsipper for å gjøre det mulig for utviklere å bygge kundesentrerte agentiske systemer for å løse deres forretningsbehov. Disse designprinsippene er ikke en forskrevet arkitektur, men snarere et utgangspunkt for team som definerer og bygger ut agentopplevelser.

Generelt bør agenter:

- Utvide og skalere menneskelige kapasiteter (idémyldring, problemløsning, automatisering, osv.)
- Fylle kunnskapshull (få meg oppdatert på kunnskapsdomener, oversettelse, osv.)
- Legge til rette for og støtte samarbeid på de måtene vi som individer foretrekker å jobbe med andre
- Gjøre oss til bedre versjoner av oss selv (f.eks. livscoach/oppgaveleder, hjelpe oss å lære følelsesregulering og oppmerksomhetstrening, bygge motstandskraft, osv.)

## Denne leksjonen vil dekke

- Hva Agentiske designprinsipper er
- Noen retningslinjer for implementering av disse designprinsippene
- Noen eksempler på bruk av designprinsippene

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

1. Forklare hva de agentiske designprinsippene er
2. Forklare retningslinjene for bruk av de agentiske designprinsippene
3. Forstå hvordan man bygger en agent ved hjelp av de agentiske designprinsippene

## De agentiske designprinsippene

![Agentiske designprinsipper](../../../translated_images/no/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Rom)

Dette er miljøet agenten opererer i. Disse prinsippene veileder hvordan vi designer agenter for å engasjere seg i fysiske og digitale verdener.

- **Koble sammen, ikke kollapse** – hjelpe til med å koble mennesker til andre mennesker, hendelser og handlingsrettet kunnskap for å muliggjøre samarbeid og tilknytning.
- Agenter hjelper til med å koble hendelser, kunnskap og mennesker.
- Agenter bringer mennesker nærmere hverandre. De er ikke designet for å erstatte eller nedvurdere mennesker.
- **Lett tilgjengelig, men noen ganger usynlig** – agenten opererer i stor grad i bakgrunnen og gir bare et puff når det er relevant og passende.
  - Agenten er lett å oppdage og tilgjengelig for autoriserte brukere på enhver enhet eller plattform.
  - Agenten støtter multimodale inn- og utdata (lyd, tale, tekst, osv.).
  - Agenten kan sømløst bytte mellom forgrunn og bakgrunn; mellom proaktiv og reaktiv, avhengig av hvordan den oppfatter brukerens behov.
  - Agenten kan operere i usynlig form, men dens bakgrunnsprosessbane og samarbeid med andre agenter er transparente for og kan kontrolleres av brukeren.

### Agent (Tid)

Dette er hvordan agenten opererer over tid. Disse prinsippene veileder hvordan vi designer agenter som interagerer på tvers av fortid, nåtid og fremtid.

- **Fortid**: Reflekterer over historien som inkluderer både tilstand og kontekst.
  - Agenten gir mer relevante resultater basert på analyse av rikere historiske data utover bare hendelsen, folkene eller tilstandene.
  - Agenten skaper forbindelser fra tidligere hendelser og reflekterer aktivt over minnet for å engasjere seg i nåværende situasjoner.
- **Nå**: Puffe mer enn bare varsle.
  - Agenten legemliggjør en helhetlig tilnærming til å interagere med mennesker. Når en hendelse skjer, går agenten ut over statisk varsling eller andre statiske formaliteter. Agenten kan forenkle flyter eller dynamisk generere signaler for å rette brukerens oppmerksomhet på riktig tidspunkt.
  - Agenten leverer informasjon basert på kontekstuell miljø, sosiale og kulturelle endringer, og tilpasset brukerens intensjon.
  - Agentinteraksjonen kan være gradvis, evolusjonerende/i økende kompleksitet for å styrke brukere over lang tid.
- **Fremtid**: Tilpasning og utvikling.
  - Agenten tilpasser seg ulike enheter, plattformer og modaliteter.
  - Agenten tilpasser seg brukeradferd, tilgjengelighetsbehov, og er fritt tilpassbar.
  - Agenten formes av og utvikler seg gjennom kontinuerlig brukerinteraksjon.

### Agent (Kjerne)

Dette er nøkkel-elementene i kjernen av en agents design.

- **Omfavne usikkerhet, men etablere tillit**.
  - Et visst nivå av agent-usikkerhet forventes. Usikkerhet er et nøkkelelement i agentdesign.
  - Tillit og åpenhet er grunnleggende lag i agentdesign.
  - Mennesker styrer når agenten er på/av, og agentens status er tydelig synlig til enhver tid.

## Retningslinjer for implementering av disse prinsippene

Når du bruker de forrige designprinsippene, bruk følgende retningslinjer:

1. **Åpenhet**: Informer brukeren om at AI er involvert, hvordan det fungerer (inkludert tidligere handlinger), og hvordan man kan gi tilbakemelding og endre systemet.
2. **Kontroll**: Gi brukeren mulighet til å tilpasse, spesifisere preferanser og personalisere, og ha kontroll over systemet og dets attributter (inkludert muligheten til å glemme).
3. **Konsistens**: Sikt etter konsistente, multimodale opplevelser på tvers av enheter og endepunkter. Bruk kjente UI/UX-elementer der det er mulig (f.eks. mikrofonikon for taleinteraksjon) og reduser brukerens kognitive belastning så mye som mulig (f.eks. sikt etter konsise svar, visuelle hjelpemidler og 'Lær mer'-innhold).

## Hvordan designe en reiseagent ved bruk av disse prinsippene og retningslinjene

Forestill deg at du designer en reiseagent, her er hvordan du kan tenke om bruk av designprinsippene og retningslinjene:

1. **Åpenhet** – La brukeren vite at reiseagenten er en AI-aktivert agent. Gi noen grunnleggende instruksjoner om hvordan man kommer i gang (f.eks. en «Hei»-melding, eksempelhjelp). Dokumenter dette tydelig på produktsiden. Vis listen over forespørsler brukeren har gjort tidligere. Gjør det klart hvordan man gir tilbakemelding (tommelen opp og ned, Send tilbakemelding-knapp, osv.). Presiser tydelig om agenten har bruks- eller temaforskrifter.
2. **Kontroll** – Sørg for at det er klart hvordan brukeren kan endre agenten etter at den er opprettet med ting som systemprompt. Gi brukeren mulighet til å velge hvor pratsom agenten skal være, skrivestil, og eventuelle forbehold om hva agenten ikke skal snakke om. Tillat brukeren å se og slette tilknyttede filer eller data, spørsmål og tidligere samtaler.
3. **Konsistens** – Sørg for at ikonene for Del spørsmål, legg til fil eller bilde og tagg noen eller noe er standard og gjenkjennelige. Bruk bindersikonet for å indikere filopplasting/deling med agenten, og et bildeikon for å indikere bildeopplasting.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Har du flere spørsmål om AI-agentiske designmønstre?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på spørsmål om AI-agenter.

## Tilleggsressurser

- <a href="https://openai.com" target="_blank">Praksis for styring av agentiske AI-systemer | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">The HAX Toolkit Project - Microsoft Research</a>
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