---
name: deploying-scalable-agents
license: MIT
---
# Implementarea agenților scalabili cu Microsoft Foundry

> Competență complementară pentru [Lecția 16 – Implementarea agenților scalabili](../../../16-deploying-scalable-agents/README.md).
> Folosește-o pentru a ajuta un cursant să treacă un agent de la prototip la o implementare de producție scalabilă, observabilă.
> Fundamentează fiecare recomandare pe conținutul lecției și
> pe notebook-ul executabil; nu inventa API-uri Foundry.

## Declanșatoare

Activează această competență când un cursant dorește să:
- Implementeze un agent în Microsoft Foundry ca **agent găzduit** și să-l facă versionat/observabil.
- Aleagă între modele de implementare **client-hosted, hosted-agent și agent-workflow**.
- Adauge **routare de model**, **stocare în cache a răspunsurilor**, sau **concurență limitată** pentru a controla latența și costul.
- Adauge o **poartă de evaluare** pentru ca o versiune proastă a agentului să nu fie livrată.
- Adauge un pas de **aprobarea umană în buclă** pentru acțiuni cu risc ridicat.
- Instrumentează un agent cu trasare **OpenTelemetry** pentru observabilitate în producție.
- **Testare rapidă** (smoke-test) a unui agent implementat ca o poartă post-implementare rapidă.

## Model mental de bază

Un agent de producție este în cea mai mare parte scheletul operațional *în jurul* modelului (~80%),
nu modelul în sine. Mapează fiecare recomandare la unul dintre aceste aspecte:

| Aspect | Prototip → Producție |
|---------|------------------------|
| Găzduire | notebook → serviciu găzduit versionat |
| Identitate | `az login` → identitate gestionată + RBAC cu scop limitat |
| Stare | în memorie → depozit de fire/memorie externalizat |
| Eșec | traceback → retrieri, fallback-uri, alerte |
| Cost | „câțiva cenți” → urmărit, rutat, cache-uit, bugetat |
| Calitate | evaluare vizuală → poartă de evaluare automată |
| Încredere | aprobare manuală → politică + om în buclă |

## Modele de implementare (alege unul sau combină)

1. **Client-hosted** — bucla de raționament rulează în procesul tău. Control maxim; deții scalarea/gestionarea stării.
2. **Agent găzduit (Foundry Agent Service)** — Foundry găzduiește bucla, stochează firele, impune RBAC/siguranța conținutului, afișează agentul în portal. Mai puțin control, suprafață operațională mult mai mică.
3. **Flux de lucru agent** — mai mulți agenți/unelte compuse într-un graf cu ramificații, noduri de aprobare și puncte de verificare durabile.

## Ciclu de viață (bucla care livrează un agent)

`creare → versionare → evaluare (poartă) → implementare găzduită → observare online → colectare eșecuri → repetare`.
**Evaluarea offline este o poartă, nu o idee secundară** — o versiune nu se livrează
decât dacă trece pragul. Observabilitatea online alimentează eșecurile reale
în setul de teste offline.

## Pârghii de scalare și cost (în ordine de prioritate)

1. **Dimensionează corect modelul** — folosește cel mai mic model care trece poarta de evaluare.
2. **Rutează după complexitate** — model mic/rapid pentru cereri simple, model mare pentru raționament real (clasificator DIY sau Foundry Model Router).
3. **Cache-uiește** — servește cererile aproape duplicate fără apel la model.
4. **Design fără stare + concurență limitată** — externalizează starea; încearcă retrieri cu backoff.

## Modele cheie de reprodus

Indică cursantului acestea din notebook-ul
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Handler-ul de cereri**: cache → rutare după complexitate → span de trasare → rulare → cache.
- **Poarta de evaluare**: acordă un scor unui set de teste offline; returnează `pass_rate >= threshold` și implementează doar dacă este adevărat.
- **Aprobare umană**: `@tool(approval_mode="always_require")` pentru acțiuni precum rambursări mari.
- **Trasare**: învelește fiecare cerere în `tracer.start_as_current_span(...)` și setează atribute precum `routed.model`, `customer.id`.

## Testare rapidă a unui agent implementat

După implementare, verifică dacă endpointul răspunde efectiv (o implementare verde poate fi încă
tăcută). Folosește acțiunea [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
prin [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
cu catalogul din [`tests/`](../../../tests/README.md). Runner-ul face POST la fiecare
prompt către `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
și verifică textul răspunsului. Identitatea are nevoie de rolul **Azure AI User** la
nivelul proiectului Foundry; audiența token-ului trebuie să fie `https://ai.azure.com/`.

Stratifică porțile: **smoke test** (accesibil/răspunzător, la fiecare implementare) → **evaluare offline**
(suficient de bun pentru a fi livrat, înainte de promovare) → **evaluare online** (cum
se comportă în mediul real, continuu).

## Controale în întreprinderi

- **RBAC**: oferă fiecărui agent găzduit o identitate gestionată cu cele mai mici privilegii.
- **MCP în producție**: tratează fiecare server MCP ca o limită neîncredere — fixează versiunea, limitează identitatea, validează rezultatele, limitează rata, nu expune niciodată secrete.

## Bariere de siguranță pentru asistent

- Preferă modelul canonic `FoundryChatClient(...)` + `provider.as_agent(...)` folosit în tot cursul.
- Nu promite rezultate live Azure pe care nu le-ai verificat; recomandă workflow-ul de testare rapidă pentru confirmarea unei implementări.
- Păstrează sfatul privind evaluarea și costurile legate împreună: evaluarea stabilește nivelul de calitate, rutarea/cache-ul mențin costul aproape de acel nivel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->