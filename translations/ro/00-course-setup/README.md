<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:57:04+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ro"
}
-->
ar trebui să ai acum propria ta versiune fork-uită a acestui curs la următorul link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ro.png)

## Rularea Codului

Acest curs oferă o serie de Jupyter Notebooks pe care le poți rula pentru a obține experiență practică în construirea Agenților AI.

Exemplele de cod utilizează fie:

**Necesită Cont GitHub - Gratuit**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Etichetat ca (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Etichetat ca (autogen.ipynb)

**Necesită Abonament Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Etichetat ca (azureaiagent.ipynb)

Te încurajăm să încerci toate cele trei tipuri de exemple pentru a vedea care funcționează cel mai bine pentru tine.

Oricare opțiune alegi, aceasta va determina pașii de configurare pe care trebuie să îi urmezi mai jos:

## Cerințe

- Python 3.12+
  - **NOTE**: Dacă nu ai instalat Python3.12, asigură-te că îl instalezi. Apoi creează venv-ul folosind python3.12 pentru a te asigura că versiunile corecte sunt instalate din fișierul requirements.txt.
- Un Cont GitHub - Pentru acces la GitHub Models Marketplace
- Abonament Azure - Pentru acces la Azure AI Foundry
- Cont Azure AI Foundry - Pentru acces la Azure AI Agent Service

Am inclus un fișier `requirements.txt` în rădăcina acestui repository care conține toate pachetele Python necesare pentru a rula exemplele de cod.

Le poți instala rulând următoarea comandă în terminalul tău, la rădăcina repository-ului:

```bash
pip install -r requirements.txt
```
Recomandăm crearea unui mediu virtual Python pentru a evita conflictele și problemele.

## Configurarea VSCode
Asigură-te că folosești versiunea corectă de Python în VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurare pentru Exemplele care folosesc GitHub Models

### Pasul 1: Obține Token-ul Personal de Acces GitHub (PAT)

În prezent, acest curs folosește GitHub Models Marketplace pentru a oferi acces gratuit la Modele de Limbaj Mari (LLMs) care vor fi folosite pentru a crea Agenți AI.

Acest lucru poate fi realizat accesând contul tău GitHub.

Te rugăm să urmezi [Principiul Privilegiului Minim](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) atunci când creezi token-ul. Acest lucru înseamnă că ar trebui să oferi token-ului doar permisiunile necesare pentru a rula exemplele de cod din acest curs.

1. Selectează opțiunea `Fine-grained tokens` din partea stângă a ecranului.

    Apoi selectează `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.ro.png)

1. Introdu un nume descriptiv pentru token care reflectă scopul său, făcându-l ușor de identificat mai târziu. Setează o dată de expirare (recomandat: 30 de zile; poți alege o perioadă mai scurtă, cum ar fi 7 zile, dacă preferi o postură mai sigură).

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ro.png)

1. Limitează domeniul token-ului la fork-ul acestui repository.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.ro.png)

1. Restricționează permisiunile token-ului: Sub **Permissions**, activează **Account Permissions**, navighează la **Models** și activează doar accesul de citire necesar pentru Modelele GitHub.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.ro.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.ro.png)

Copiază noul token pe care tocmai l-ai creat. Acum îl vei adăuga în fișierul `.env` inclus în acest curs.

### Pasul 2: Creează Fișierul `.env`

Pentru a crea fișierul `.env`, rulează următoarea comandă în terminalul tău.

```bash
cp .env.example .env
```

Aceasta va copia fișierul exemplu și va crea un `.env` în directorul tău, unde vei completa valorile pentru variabilele de mediu.

Cu token-ul copiat, deschide fișierul `.env` în editorul tău de text preferat și lipește token-ul în câmpul `GITHUB_TOKEN`.

Ar trebui să poți rula acum exemplele de cod din acest curs.

## Configurare pentru Exemple folosind Azure AI Foundry și Azure AI Agent Service

### Pasul 1: Obține Endpoint-ul Proiectului Azure

Urmează pașii pentru crearea unui hub și proiect în Azure AI Foundry găsiți aici: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

După ce ai creat proiectul, va trebui să obții string-ul de conexiune pentru proiectul tău.

Acest lucru poate fi realizat accesând pagina **Overview** a proiectului tău în portalul Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ro.png)

### Pasul 2: Creează Fișierul `.env`

Pentru a crea fișierul `.env`, rulează următoarea comandă în terminalul tău.

```bash
cp .env.example .env
```

Aceasta va copia fișierul exemplu și va crea un `.env` în directorul tău, unde vei completa valorile pentru variabilele de mediu.

Cu token-ul copiat, deschide fișierul `.env` în editorul tău de text preferat și lipește token-ul în câmpul `PROJECT_ENDPOINT`.

### Pasul 3: Autentificare în Azure

Ca o bună practică de securitate, vom folosi [autentificarea fără cheie](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) pentru a ne autentifica în Azure OpenAI cu Microsoft Entra ID.

Apoi, deschide un terminal și rulează `az login --use-device-code` pentru a te autentifica în contul tău Azure.

După ce te-ai autentificat, selectează abonamentul tău în terminal.

## Variabile de Mediu Adiționale - Azure Search și Azure OpenAI 

Pentru Lecția Agentic RAG - Lecția 5 - există exemple care utilizează Azure Search și Azure OpenAI.

Dacă dorești să rulezi aceste exemple, va trebui să adaugi următoarele variabile de mediu în fișierul `.env`:

### Pagina Overview (Proiect)

- `AZURE_SUBSCRIPTION_ID` - Verifică **Project details** pe pagina **Overview** a proiectului tău.

- `AZURE_AI_PROJECT_NAME` - Uită-te în partea de sus a paginii **Overview** pentru proiectul tău.

- `AZURE_OPENAI_SERVICE` - Găsește acest lucru în fila **Included capabilities** pentru **Azure OpenAI Service** pe pagina **Overview**.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Accesează **Project properties** pe pagina **Overview** a **Management Center**.

- `GLOBAL_LLM_SERVICE` - Sub **Connected resources**, găsește numele conexiunii **Azure AI Services**. Dacă nu este listat, verifică **Azure portal** sub grupul tău de resurse pentru numele resursei AI Services.

### Pagina Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selectează modelul tău de embedding (ex. `text-embedding-ada-002`) și notează **Deployment name** din detaliile modelului.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selectează modelul tău de chat (ex. `gpt-4o-mini`) și notează **Deployment name** din detaliile modelului.

### Portalul Azure

- `AZURE_OPENAI_ENDPOINT` - Caută **Azure AI services**, fă clic pe el, apoi accesează **Resource Management**, **Keys and Endpoint**, derulează în jos la "Azure OpenAI endpoints" și copiază cel care spune "Language APIs".

- `AZURE_OPENAI_API_KEY` - De pe același ecran, copiază KEY 1 sau KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Găsește resursa ta **Azure AI Search**, fă clic pe ea și vezi **Overview**.

- `AZURE_SEARCH_API_KEY` - Apoi accesează **Settings** și apoi **Keys** pentru a copia cheia principală sau secundară de administrare.

### Pagina Externă

- `AZURE_OPENAI_API_VERSION` - Vizitează pagina [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sub **Latest GA API release**.

### Configurare autentificare fără cheie

În loc să codificăm credențialele, vom folosi o conexiune fără cheie cu Azure OpenAI. Pentru a face acest lucru, vom importa `DefaultAzureCredential` și mai târziu vom apela funcția `DefaultAzureCredential` pentru a obține credențialul.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Probleme?

Dacă întâmpini probleme în rularea acestei configurări, intră în

## Lecția Următoare

Acum ești gata să rulezi codul pentru acest curs. Spor la învățat mai multe despre lumea Agenților AI!

[Introducere în Agenți AI și Cazuri de Utilizare](../01-intro-to-ai-agents/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.