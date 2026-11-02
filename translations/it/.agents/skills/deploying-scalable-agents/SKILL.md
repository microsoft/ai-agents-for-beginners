---
name: deploying-scalable-agents
license: MIT
---
# Distribuire agenti scalabili con Microsoft Foundry

> Abilità di supporto per [Lezione 16 – Distribuire agenti scalabili](../../../16-deploying-scalable-agents/README.md).
> Usala per aiutare un apprendista a spostare un agente dal prototipo a una distribuzione
> di produzione scalabile e osservabile. Basa ogni raccomandazione sul contenuto della lezione e
> sul notebook eseguibile; non inventare API di Foundry.

## Inneschi

Attiva questa abilità quando un apprendista vuole:
- Distribuire un agente su Microsoft Foundry come **agente ospitato** e renderlo versionato/osservabile.
- Scegliere tra i modelli di distribuzione **client-hosted, hosted-agent e agent-workflow**.
- Aggiungere **instradamento del modello**, **memorizzazione nella cache delle risposte** o **concorrenza limitata** per controllare latenza e costi.
- Aggiungere un **cancello di valutazione** così da impedire che una versione di un agente scadente venga distribuita.
- Aggiungere un passaggio di **approvazione human-in-the-loop** per azioni ad alto rischio.
- Strumentare un agente con tracciamento **OpenTelemetry** per l’osservabilità in produzione.
- **Smoke-test** di un agente distribuito come controllore rapido post-distribuzione.

## Modello mentale centrale

Un agente di produzione è per lo più lo scheletro operativo *attorno* al modello (~80%),
non il modello stesso. Mappa ogni raccomandazione a una di queste preoccupazioni:

| Preoccupazione | Prototipo → Produzione |
|---------|------------------------|
| Hosting | notebook → servizio ospitato versionato |
| Identità | il tuo `az login` → identità gestita + RBAC con ambito |
| Stato | in memoria → archivio esterno di thread/memoria |
| Fallimento | traceback → ritentativi, soluzioni alternative, avvisi |
| Costo | "pochi centesimi" → tracciati, instradati, memorizzati in cache, budgettati |
| Qualità | controllo a occhio → cancello di valutazione automatizzato |
| Fiducia | approvi tu → policy + human-in-the-loop |

## Modelli di distribuzione (scegli uno o combina)

1. **Client-hosted** — il ciclo di ragionamento gira nel tuo processo. Massimo controllo; possiedi scalabilità/stato.
2. **Hosted agent (Foundry Agent Service)** — Foundry ospita il ciclo, memorizza thread, applica RBAC/sicurezza contenuti, mostra l’agente nel portale. Meno controllo, molto meno superficie operativa.
3. **Agent workflow** — più agenti/strumenti composti in un grafo con diramazioni, nodi di approvazione e checkpoint durevoli.

## Ciclo di vita (il loop che distribuisce un agente)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**La valutazione offline è un cancello, non un ripensamento** — una versione non viene distribuita
a meno che non superi la soglia. L’osservabilità online rimanda i veri fallimenti
nel set di test offline.

## Leve di scalabilità e costo (in ordine di priorità)

1. **Dimensiona correttamente il modello** — usa il modello più piccolo che supera il cancello di valutazione.
2. **Instrada per complessità** — modello piccolo/veloce per richieste semplici, modello grande per vero ragionamento (classificatore DIY o Foundry Model Router).
3. **Cache** — servi richieste quasi duplicate senza una chiamata al modello.
4. **Design senza stato + concorrenza limitata** — esternalizza lo stato; ritenta con backoff.

## Modelli chiave da riprodurre

Indirizza l’apprendista a questi dal notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Gestore richieste**: cache → instrada per complessità → traccia span → esegui → cache.
- **Cancello di valutazione**: valuta un set di test offline; ritorna `pass_rate >= threshold` e distribuisci solo se vero.
- **Approvazione umana**: `@tool(approval_mode="always_require")` per azioni come grossi rimborsi.
- **Tracciamento**: avvolgi ogni richiesta in `tracer.start_as_current_span(...)` e imposta attributi come `routed.model`, `customer.id`.

## Smoke-test di un agente distribuito

Dopo la distribuzione, verifica che l’endpoint risponda davvero (una distribuzione verde può
essere silenziosa). Usa l’azione [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
tramite [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
con il catalogo in [`tests/`](../../../tests/README.md). Il runner invia in POST ogni
prompt a `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
e verifica il testo della risposta. L’identità ha bisogno del ruolo **Azure AI User** a
livello di progetto Foundry; l’audience del token deve essere `https://ai.azure.com/`.

Sovrapponi i cancelli: **smoke test** (raggiungibile/risponde, ad ogni distribuzione) → **valutazione offline** (abbastanza buono per distribuire, prima della promozione) → **valutazione online** (come va nel mondo, continua).



## Controlli enterprise

- **RBAC**: assegna a ogni agente ospitato un’identità gestita con privilegi minimi.
- **MCP in produzione**: tratta ogni server MCP come un confine non fidato — fissa la versione, limita l’identità, valida gli output, limita la frequenza, non esporre mai segreti.

## Guardrail per l’assistente

- Preferisci il modello canonico `FoundryChatClient(...)` + `provider.as_agent(...)` usato in tutto il corso.
- Non promettere risultati live-Azure non verificati; raccomanda il workflow smoke-test per confermare una distribuzione.
- Tieni insieme valutazione e consigli sui costi: la valutazione fissa il livello di qualità, instradamento/cache tengono i costi vicino a quel livello.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->