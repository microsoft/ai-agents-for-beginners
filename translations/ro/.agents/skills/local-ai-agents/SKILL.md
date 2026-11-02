---
name: local-ai-agents
license: MIT
---
# Crearea agenților AI locali cu Foundry Local și Qwen

> Competență companion pentru [Lecția 17 – Crearea agenților AI locali](../../../17-creating-local-ai-agents/README.md).
> Folosește-o pentru a ajuta un cursant să construiască un agent care raționează, apelează instrumente și caută
> documentație complet pe propriul său calculator — fără inferență în cloud. Fundamentează fiecare
> recomandare pe conținutul lecției și pe caietul rulabil.

## Declanșatoare

Activează această competență când un cursant dorește să:
- Ruleze un agent **complet pe dispozitiv** pentru motive de confidențialitate, cost sau offline.
- Servească un model local cu **Foundry Local** și se conecteze prin endpoint-ul compatibil OpenAI.
- Folosească un model de **apelare a funcțiilor Qwen** pentru a genera apeluri de instrumente locale fiabile.
- Adauge **RAG local** (Chroma) sau un **server MCP local**.
- Proiecteze o strategie **hibridă** de rutare local/cloud.

## Model mental de bază

Un SLM face compromis între amploare și confidențialitate, cost și operare offline. Strategia câștigătoare:
**lasă SLM-ul să orchestreze și lasă instrumentele să facă munca grea.** Modelul
nu trebuie să *cunoască* codul — trebuie să știe când să apeleze
`read_file` și `search_docs`. Aceasta valorifică punctul forte al unui SLM (decizii limitate
precum selecția instrumentelor) și evită punctul său slab (cunoștințe largi, raționament multi-hop lung).


## De ce aceste elemente specifice

- **Foundry Local** expune un **endpoint HTTP compatibil OpenAI**, astfel încât codul agentului cloud se transferă schimbând doar `base_url` (și folosind o cheie API locală fictivă). De asemenea, selectează automat cea mai bună variantă (CPU/GPU/NPU) pentru mașină.
- Modelele **Qwen** sunt antrenate pentru apelarea funcțiilor și emit apeluri de instrumente bine formate constant — acesta este ceea ce transformă un model *chat* local într-un *agent* local.
- **Chroma** rulează în proces și stochează vectori pe disc, astfel întregul flux RAG (embed → stocare → regăsire → raționament) rămâne local.
- **MCP** este un transport, nu un serviciu cloud: un server MCP poate rula local peste `stdio`.

## Elemente esențiale pentru configurare

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # substituent local
```

~8 GB RAM este un minim realist; un GPU/NPU ajută, dar nu este necesar.

## Modele cheie de replicat

Indică cursantului caietul
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Instrumente izolate**: fiecare instrument de fișiere rezolvă căile și respinge orice este în afara unui singur director rădăcină de proiect — chiar și local, un instrument rulează cu permisiunile utilizatorului.
- **Bucle de apelare a instrumentelor**: înregistrează instrumentele conform schemei OpenAI, execută instrumentele solicitate local, introduce rezultatele înapoi, repetă până la un răspuns final.
- **RAG local**: inserează documente într-o colecție Chroma; `search_docs` returnează fragmente top-k.
- **MCP local**: conectează-te la un server local peste `stdio`; limitează-l la un director de proiect și validează ieșirile.

## Rutare hibridă (local ca unul dintre modele)

| Situație | Unde rulează |
|-----------|---------------|
| Date sensibile / offline | SLM local |
| Sarcină simplă, limitată | SLM local (ieftin, rapid) |
| Raționament multi-hop dificil pe date nesensibile | Model cloud |
| Pană în cloud | SLM local (degradare grațioasă) |

Aceasta reflectă ideea de rutare a modelelor din Lecția 16, cu stația de lucru ca una
dintre rutele disponibile. Preferă proiecte care cad înapoi pe local astfel încât agentul degradează
calitatea în loc să eșueze complet.

## Măsuri de siguranță pentru asistent

- Menține fiecare operație de fișier/instrument limitată la un director de proiect izolat.
- Nu trimite cod sau date în cloud când scopul declarat al cursantului este confidențialitate/offline — păstrează tot fluxul local.
- Stabilește așteptări realiste pentru calitatea SLM; bazează-te pe instrumente și RAG mai degrabă decât pe cunoștințele memorate ale modelului.
- Observă că Lecția 17 nu are endpoint Foundry Responses, așa că acțiunea de testare rapidă în cloud nu se aplică — validează rulând caietul local.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->