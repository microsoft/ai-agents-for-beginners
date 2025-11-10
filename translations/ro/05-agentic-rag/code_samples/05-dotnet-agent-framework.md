<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:08:58+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "ro"
}
-->
# 🔍 RAG pentru Enterprise cu Azure AI Foundry (.NET)

## 📋 Obiective de Învățare

Acest notebook demonstrează cum să construiești sisteme RAG (Retrieval-Augmented Generation) de nivel enterprise folosind Microsoft Agent Framework în .NET cu Azure AI Foundry. Vei învăța să creezi agenți pregătiți pentru producție care pot căuta în documente și oferi răspunsuri precise, conștiente de context, cu securitate și scalabilitate pentru enterprise.

**Capabilități RAG pentru Enterprise pe care le vei construi:**
- 📚 **Inteligența Documentelor**: Procesare avansată a documentelor cu serviciile Azure AI
- 🔍 **Căutare Semantică**: Căutare vectorială de înaltă performanță cu funcții enterprise
- 🛡️ **Integrare Securitate**: Acces bazat pe roluri și modele de protecție a datelor
- 🏢 **Arhitectură Scalabilă**: Sisteme RAG pregătite pentru producție cu monitorizare

## 🎯 Arhitectura RAG pentru Enterprise

### Componentele de Bază pentru Enterprise
- **Azure AI Foundry**: Platformă AI gestionată pentru enterprise, cu securitate și conformitate
- **Agenți Persistenți**: Agenți cu stare, istoric conversațional și gestionare a contextului
- **Managementul Magazinului de Vectori**: Indexare și recuperare de documente la nivel enterprise
- **Integrare Identitate**: Autentificare Azure AD și control de acces bazat pe roluri

### Beneficii .NET pentru Enterprise
- **Siguranța Tipurilor**: Validare la compilare pentru operațiuni RAG și structuri de date
- **Performanță Async**: Procesare de documente și operațiuni de căutare non-blocante
- **Managementul Memoriei**: Utilizare eficientă a resurselor pentru colecții mari de documente
- **Modele de Integrare**: Integrare nativă cu serviciile Azure prin injecție de dependențe

## 🏗️ Arhitectura Tehnică

### Fluxul RAG pentru Enterprise
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Componentele de Bază .NET
- **Azure.AI.Agents.Persistent**: Managementul agenților enterprise cu persistența stării
- **Azure.Identity**: Autentificare integrată pentru acces securizat la serviciile Azure
- **Microsoft.Agents.AI.AzureAI**: Implementare optimizată pentru agenți în Azure
- **System.Linq.Async**: Operațiuni LINQ asincrone de înaltă performanță

## 🔧 Funcționalități și Beneficii pentru Enterprise

### Securitate și Conformitate
- **Integrare Azure AD**: Managementul identității și autentificării pentru enterprise
- **Acces Bazat pe Roluri**: Permisiuni detaliate pentru accesul la documente și operațiuni
- **Protecția Datelor**: Criptare la repaus și în tranzit pentru documente sensibile
- **Jurnalizare Audit**: Urmărire detaliată a activităților pentru cerințele de conformitate

### Performanță și Scalabilitate
- **Pooling de Conexiuni**: Management eficient al conexiunilor la serviciile Azure
- **Procesare Async**: Operațiuni non-blocante pentru scenarii de debit ridicat
- **Strategii de Caching**: Caching inteligent pentru documentele accesate frecvent
- **Balansare de Sarcină**: Procesare distribuită pentru implementări la scară largă

### Management și Monitorizare
- **Verificări de Sănătate**: Monitorizare integrată pentru componentele sistemului RAG
- **Metrice de Performanță**: Analize detaliate ale calității căutării și timpilor de răspuns
- **Gestionarea Erorilor**: Management cuprinzător al excepțiilor cu politici de retry
- **Managementul Configurației**: Setări specifice mediului cu validare

## ⚙️ Cerințe Prealabile și Configurare

**Mediu de Dezvoltare:**
- SDK .NET 9.0 sau mai recent
- Visual Studio 2022 sau VS Code cu extensia C#
- Abonament Azure cu acces la AI Foundry

**Pachete NuGet Necesare:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurare Autentificare Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Configurare Mediu:**
* Configurarea Azure AI Foundry (gestionată automat prin Azure CLI)
* Asigură-te că ești autentificat la abonamentul Azure corect

## 📊 Modele RAG pentru Enterprise

### Modele de Management al Documentelor
- **Încărcare în Masă**: Procesare eficientă a colecțiilor mari de documente
- **Actualizări Incrementale**: Adăugare și modificare de documente în timp real
- **Controlul Versiunilor**: Versiuni ale documentelor și urmărirea modificărilor
- **Managementul Metadatelor**: Atribute bogate ale documentelor și taxonomie

### Modele de Căutare și Recuperare
- **Căutare Hibridă**: Combinarea căutării semantice și pe cuvinte cheie pentru rezultate optime
- **Căutare Facetată**: Filtrare și categorisire multidimensională
- **Ajustarea Relevanței**: Algoritmi de scor personalizați pentru nevoi specifice domeniului
- **Clasificarea Rezultatelor**: Clasificare avansată cu integrarea logicii de afaceri

### Modele de Securitate
- **Securitate la Nivel de Document**: Control detaliat al accesului pentru fiecare document
- **Clasificarea Datelor**: Etichetare automată a sensibilității și protecție
- **Urme de Audit**: Jurnalizare cuprinzătoare a tuturor operațiunilor RAG
- **Protecția Confidențialității**: Detectarea și redactarea automată a informațiilor personale

## 🔒 Funcționalități de Securitate pentru Enterprise

### Autentificare și Autorizare
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Protecția Datelor
- **Criptare**: Criptare end-to-end pentru documente și indici de căutare
- **Controale de Acces**: Integrare cu Azure AD pentru permisiuni utilizator și grup
- **Rezidența Datelor**: Controale geografice ale locației datelor pentru conformitate
- **Backup și Recuperare**: Capacități automate de backup și recuperare în caz de dezastru

## 📈 Optimizarea Performanței

### Modele de Procesare Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Managementul Memoriei
- **Procesare Streaming**: Gestionarea documentelor mari fără probleme de memorie
- **Pooling de Resurse**: Reutilizarea eficientă a resurselor costisitoare
- **Colectare de Gunoi**: Modele optimizate de alocare a memoriei
- **Managementul Conexiunilor**: Ciclu de viață corect al conexiunilor la serviciile Azure

### Strategii de Caching
- **Caching Interogări**: Cache pentru căutările executate frecvent
- **Caching Documente**: Caching în memorie pentru documentele accesate frecvent
- **Caching Indici**: Caching optimizat al indicilor vectoriali
- **Caching Rezultate**: Caching inteligent al răspunsurilor generate

## 📊 Utilizări pentru Enterprise

### Managementul Cunoștințelor
- **Wiki Corporativ**: Căutare inteligentă în bazele de cunoștințe ale companiei
- **Politici și Proceduri**: Ghid automatizat pentru conformitate și proceduri
- **Materiale de Training**: Asistență inteligentă pentru învățare și dezvoltare
- **Baze de Date de Cercetare**: Sisteme de analiză a lucrărilor academice și de cercetare

### Suport pentru Clienți
- **Bază de Cunoștințe pentru Suport**: Răspunsuri automate pentru serviciul clienți
- **Documentație Produs**: Recuperare inteligentă a informațiilor despre produse
- **Ghiduri de Depanare**: Asistență contextuală pentru rezolvarea problemelor
- **Sisteme FAQ**: Generare dinamică de FAQ din colecții de documente

### Conformitate Regulatorie
- **Analiza Documentelor Legale**: Inteligență pentru contracte și documente legale
- **Monitorizare Conformitate**: Verificare automată a conformității reglementare
- **Evaluarea Riscurilor**: Analiză și raportare a riscurilor bazate pe documente
- **Suport pentru Audit**: Descoperire inteligentă de documente pentru audituri

## 🚀 Implementare în Producție

### Monitorizare și Observabilitate
- **Application Insights**: Telemetrie detaliată și monitorizare a performanței
- **Metrice Personalizate**: Urmărirea KPI-urilor specifice afacerii și alerte
- **Trasare Distribuită**: Urmărirea cererilor de la un capăt la altul între servicii
- **Tablouri de Bord pentru Sănătate**: Vizualizare în timp real a sănătății și performanței sistemului

### Scalabilitate și Fiabilitate
- **Auto-Scaling**: Scalare automată bazată pe sarcină și metrice de performanță
- **Disponibilitate Ridicată**: Implementare multi-regională cu capacități de failover
- **Testare de Sarcină**: Validarea performanței sub condiții de sarcină enterprise
- **Recuperare în Caz de Dezastru**: Proceduri automate de backup și recuperare

Ești pregătit să construiești sisteme RAG de nivel enterprise care pot gestiona documente sensibile la scară? Hai să arhitectăm sisteme inteligente de cunoștințe pentru enterprise! 🏢📖✨

## Implementare Cod

Exemplul complet de cod funcțional pentru această lecție este disponibil în `05-dotnet-agent-framework.cs`. 

Pentru a rula exemplul:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Sau folosește `dotnet run` direct:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Codul demonstrează:

1. **Instalarea Pachetelor**: Instalarea pachetelor NuGet necesare pentru Azure AI Agents
2. **Configurarea Mediului**: Încărcarea punctului final și setărilor modelului Azure AI Foundry
3. **Încărcarea Documentelor**: Încărcarea unui document pentru procesarea RAG
4. **Crearea Magazinului de Vectori**: Crearea unui magazin de vectori pentru căutare semantică
5. **Configurarea Agentului**: Configurarea unui agent AI cu capacități de căutare în fișiere
6. **Executarea Interogărilor**: Rularea interogărilor pe documentul încărcat

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.