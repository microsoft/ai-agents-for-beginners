<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:23:11+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ro"
}
-->
# Exemplu de Server MCP Github

## Descriere

Acesta este un demo creat pentru Hackathon-ul AI Agents găzduit de Microsoft Reactor.

Instrumentul este utilizat pentru a recomanda proiecte de hackathon pe baza repo-urilor unui utilizator de pe Github. Acest lucru se realizează prin:

1. **Agentul Github** - Folosind Serverul MCP Github pentru a prelua repo-uri și informații despre acestea.
2. **Agentul Hackathon** - Preia datele de la Agentul Github și generează idei creative de proiecte pentru hackathon, bazate pe proiectele utilizatorului, limbajele utilizate și temele hackathon-ului AI Agents.
3. **Agentul Evenimente** - Pe baza sugestiilor agentului hackathon, agentul evenimente va recomanda evenimente relevante din seria Hackathon-ului AI Agents.

## Rularea codului

### Variabile de mediu

Acest demo utilizează Azure Open AI Service, Semantic Kernel, Serverul MCP Github și Azure AI Search.

Asigură-te că ai setat corect variabilele de mediu necesare pentru a utiliza aceste instrumente:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Rularea Serverului Chainlit

Pentru a te conecta la serverul MCP, acest demo folosește Chainlit ca interfață de chat.

Pentru a rula serverul, folosește următoarea comandă în terminalul tău:

```bash
chainlit run app.py -w
```

Aceasta ar trebui să pornească serverul Chainlit pe `localhost:8000` și să populeze Indexul Azure AI Search cu conținutul din `event-descriptions.md`.

## Conectarea la Serverul MCP

Pentru a te conecta la Serverul MCP Github, selectează pictograma „plug” de sub caseta de chat „Type your message here..”:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ro.png)

De acolo, poți face clic pe „Connect an MCP” pentru a adăuga comanda de conectare la Serverul MCP Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Înlocuiește "[YOUR PERSONAL ACCESS TOKEN]" cu propriul tău Personal Access Token.

După conectare, ar trebui să vezi un (1) lângă pictograma plug pentru a confirma că este conectat. Dacă nu, încearcă să repornești serverul Chainlit cu `chainlit run app.py -w`.

## Utilizarea Demo-ului

Pentru a începe fluxul de lucru al agentului pentru recomandarea proiectelor de hackathon, poți introduce un mesaj precum:

"Recomandă proiecte de hackathon pentru utilizatorul Github koreyspace"

Agentul Router va analiza cererea ta și va determina ce combinație de agenți (GitHub, Hackathon și Evenimente) este cea mai potrivită pentru a răspunde solicitării tale. Agenții lucrează împreună pentru a oferi recomandări complete bazate pe analiza repo-urilor Github, generarea de idei de proiecte și evenimente tehnologice relevante.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.