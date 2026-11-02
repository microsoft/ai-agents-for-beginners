# Exemplu server Github MCP

## Descriere

Acesta a fost un demo creat pentru Hackathon-ul AI Agents găzduit prin intermediul Microsoft Reactor.

Instrumentul este utilizat pentru a recomanda proiecte de hackathon bazate pe repo-urile Github ale unui utilizator.
Acest lucru se realizează prin:

1. **Agent Github** - Folosind serverul Github MCP pentru a prelua repo-uri și informații despre acestea.
2. **Agent Hackathon** - Preia datele de la Agentul Github și generează idei creative de proiecte pentru hackathon bazate pe proiectele, limbajele folosite de utilizator și categoriile proiectului pentru hackathon-ul AI Agents.
3. **Agent Evenimente** - Pe baza sugestiei agentului hackathon, agentul de evenimente va recomanda evenimente relevante din seria Hackathon AI Agent.

## Rularea codului 

### Variabile de mediu

Acest demo utilizează Microsoft Agent Framework, Azure OpenAI Service, serverul Github MCP și Azure AI Search.

Asigurați-vă că aveți setate corect variabilele de mediu pentru a folosi aceste instrumente:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Pornirea serverului Chainlit

Pentru a vă conecta la serverul MCP, acest demo folosește Chainlit ca interfață de chat.

Pentru a porni serverul, folosiți următoarea comandă în terminal:

```bash
chainlit run app.py -w
```


Aceasta va porni serverul Chainlit pe `localhost:8000` și va popula indexul de căutare Azure AI cu conținutul din `event-descriptions.md`.

## Conectarea la serverul MCP

Pentru a vă conecta la serverul Github MCP, selectați pictograma „fișă” sub caseta de chat „Type your message here..”:

![MCP Connect](../../../../../translated_images/ro/mcp-chainlit-1.7ed66d648e3cfb28.webp)

De acolo puteți face clic pe „Connect an MCP” pentru a adăuga comanda de conectare la serverul Github MCP:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Înlocuiți „[YOUR PERSONAL ACCESS TOKEN]” cu tokenul dvs. personal de acces.

După conectare, ar trebui să vedeți un (1) lângă pictograma fișei pentru a confirma că este conectat. Dacă nu, încercați să reporniți serverul chainlit cu `chainlit run app.py -w`.

## Utilizarea Demo-ului

Pentru a începe fluxul agentului de recomandare a proiectelor de hackathon, puteți scrie un mesaj de genul:

"Recomandă proiecte de hackathon pentru utilizatorul Github koreyspace"

Agentul Router va analiza cererea dvs. și va determina ce combinație de agenți (GitHub, Hackathon și Evenimente) este cea mai potrivită pentru a răspunde la întrebarea dvs. Agenții lucrează împreună pentru a oferi recomandări cuprinzătoare bazate pe analiza depozitelor GitHub, generarea de idei de proiect și evenimente tehnologice relevante.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->