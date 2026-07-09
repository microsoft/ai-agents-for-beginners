# 🔍 Enterprise RAG s Microsoft Foundry (.NET)

## 📋 Ciljevi učenja

Ovaj bilježnik prikazuje kako izgraditi Enterprise-grade Retrieval-Augmented Generation (RAG) sustave koristeći Microsoft Agent Framework u .NET-u s Microsoft Foundryjem. Naučit ćete kako kreirati agente spremne za produkciju koji mogu pretraživati dokumente i pružati točne, kontekstualno svjesne odgovore s enterprise sigurnošću i skalabilnošću.

**Enterprise RAG mogućnosti koje ćete izgraditi:**
- 📚 **Inteligencija dokumenata**: Napredno procesiranje dokumenata s Azure AI servisima
- 🔍 **Semantičko pretraživanje**: Visokoučinkovito vektorsko pretraživanje s enterprise značajkama
- 🛡️ **Integracija sigurnosti**: Pristup baziran na ulogama i obrasci zaštite podataka
- 🏢 **Skalabilna arhitektura**: RAG sustavi spremni za produkciju s nadzorom

## 🎯 Enterprise RAG arhitektura

### Osnovne enterprise komponente
- **Microsoft Foundry**: Upravljana enterprise AI platforma sa sigurnošću i usklađenošću
- **Persistent Agents**: Državni agenti s poviješću razgovora i upravljanjem kontekstom
- **Upravljanje vektorskim spremištem**: Enterprise razina indeksiranja i dohvaćanja dokumenata
- **Integracija identiteta**: Azure AD autentifikacija i kontrola pristupa bazirana na ulogama

### .NET enterprise prednosti
- **Tipna sigurnost**: Validacija u vrijeme kompilacije za RAG operacije i podatkovne strukture
- **Async performanse**: Neblokirajuće procesiranje dokumenata i operacije pretraživanja
- **Upravljanje memorijom**: Učinkovito korištenje resursa za velike kolekcije dokumenata
- **Integracijski obrasci**: Izvorna integracija Azure servisa s dependency injection

## 🏗️ Tehnička arhitektura

### Enterprise RAG pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Osnovne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje enterprise agentima s perzistentnošću stanja
- **Azure.Identity**: Integrirana autentifikacija za siguran pristup Azure servisima
- **Microsoft.Agents.AI.AzureAI**: Implementacija agent frameworka optimizirana za Azure
- **System.Linq.Async**: Visokoučinkovite asinkrone LINQ operacije

## 🔧 Enterprise značajke i prednosti

### Sigurnost i usklađenost
- **Integracija Azure AD**: Enterprise upravljanje identitetom i autentifikacija
- **Pristup baziran na ulogama**: Fino granulirane dozvole za pristup dokumentima i operacijama
- **Zaštita podataka**: Šifriranje u mirovanju i u prijenosu za osjetljive dokumente
- **Audit zapisivanje**: Sveobuhvatno praćenje aktivnosti za usklađenost

### Performanse i skalabilnost
- **Spajanje konekcija**: Učinkovito upravljanje Azure servisnim konekcijama
- **Async procesiranje**: Neblokirajuće operacije za scenarije visokog protoka
- **Strategije keširanja**: Inteligentno keširanje često pristupanih dokumenata
- **Ravnomjerno opterećenje**: Distribuirano procesiranje za velike implementacije

### Upravljanje i nadzor
- **Provjere zdravlja**: Ugrađeni nadzor komponenti RAG sustava
- **Metrike performansi**: Detaljna analitika kvalitete pretraživanja i vremena odgovora
- **Rukovanje pogreškama**: Sveobuhvatno upravljanje iznimkama s politikama ponovnog pokušaja
- **Upravljanje konfiguracijom**: Postavke specifične za okruženje s validacijom

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Azure pretplata s pristupom Microsoft Foundryju

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure autentifikacija postavljanje:**
```bash
# Instalirajte Azure CLI i prijavite se
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracija okruženja:**
* Microsoft Foundry konfiguracija (automatski upravljana preko Azure CLI)
* Provjerite jeste li autentificirani na ispravnu Azure pretplatu

## 📊 Enterprise RAG obrasci

### Obrasci upravljanja dokumentima
- **Masovno učitavanje**: Učinkovito procesiranje velikih kolekcija dokumenata
- **Inkrementalna ažuriranja**: Dodavanje i mijenjanje dokumenata u stvarnom vremenu
- **Kontrola verzija**: Verzije dokumenata i praćenje promjena
- **Upravljanje metapodacima**: Bogati atributi dokumenata i taksonomija

### Obrasci pretraživanja i dohvaćanja
- **Hibridno pretraživanje**: Kombiniranje semantičkog i ključnog pretraživanja za optimalne rezultate
- **Faceted pretraživanje**: Višedimenzionalno filtriranje i kategorizacija
- **Podešavanje relevantnosti**: Prilagođeni algoritmi bodovanja za specifične domene
- **Rangiranje rezultata**: Napredno rangiranje s integracijom poslovne logike

### Sigurnosni obrasci
- **Sigurnost na razini dokumenata**: Fino granulirana kontrola pristupa po dokumentu
- **Klasifikacija podataka**: Automatsko označavanje osjetljivosti i zaštita
- **Audit tragovi**: Sveobuhvatno evidentiranje svih RAG operacija
- **Zaštita privatnosti**: Detekcija i uređivanje PII podataka

## 🔒 Enterprise sigurnosne značajke

### Autentifikacija i autorizacija
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

### Zaštita podataka
- **Šifriranje**: Krajnje do krajnjeg šifriranje dokumenata i indeksa pretraživanja
- **Kontrola pristupa**: Integracija s Azure AD za dopuštenja korisnika i grupa
- **Rezidencija podataka**: Kontrola geografske lokacije podataka za usklađenost
- **Sigurnosna kopija i oporavak**: Automatizirane mogućnosti sigurnosnih kopija i oporavka od katastrofa

## 📈 Optimizacija performansi

### Obrasci asinhronog procesiranja
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje memorijom
- **Streaming procesiranje**: Obrada velikih dokumenata bez problema s memorijom
- **Ponovna upotreba resursa**: Učinkovito ponovno korištenje skupih resursa
- **Garbage collection**: Optimizirani obrasci alokacije memorije
- **Upravljanje vezama**: Ispravan životni ciklus vezan za Azure servise

### Strategije keširanja
- **Keširanje upita**: Keširanje često izvršenih pretraživanja
- **Keširanje dokumenata**: Keširanje u memoriji za vruće dokumente
- **Keširanje indeksa**: Optimizirano keširanje vektorskih indeksa
- **Keširanje rezultata**: Inteligentno keširanje generiranih odgovora

## 📊 Enterprise primjeri korištenja

### Upravljanje znanjem
- **Korporativna wiki**: Inteligentno pretraživanje kroz baze znanja tvrtke
- **Pravila i procedure**: Automatizirani vodiči za usklađenost i procedure
- **Materijali za obuku**: Inteligentna pomoć za učenje i razvoj
- **Istraživačke baze podataka**: Sustavi za analizu akademskih i istraživačkih radova

### Korisnička podrška
- **Baza znanja za podršku**: Automatizirani odgovori korisničke službe
- **Dokumentacija proizvoda**: Inteligentno dohvaćanje informacija o proizvodu
- **Vodiči za rješavanje problema**: Kontekstualna pomoć u rješavanju problema
- **Sustavi FAQ**: Dinamičko generiranje često postavljanih pitanja iz dokumenata

### Regulativna usklađenost
- **Analiza pravnih dokumenata**: Inteligencija ugovora i pravnih dokumenata
- **Praćenje usklađenosti**: Automatizirana provjera usklađenosti s propisima
- **Procjena rizika**: Analiza rizika i izvještavanje temeljeno na dokumentima
- **Podrška za reviziju**: Inteligentno pronalaženje dokumenata za revizije

## 🚀 Produkcijsko postavljanje

### Nadzor i preglednost
- **Application Insights**: Detaljna telemetrija i nadzor performansi
- **Prilagođene metrike**: Praćenje i upozoravanje KPI-a specifičnih za posao
- **Distribuirano praćenje**: Praćenje zahtjeva od kraja do kraja kroz servise
- **Nadzorne ploče za zdravlje**: Vizualizacija zdravlja i performansi sustava u stvarnom vremenu

### Skalabilnost i pouzdanost
- **Automatsko skaliranje**: Automatsko skaliranje temeljem opterećenja i metrika performansi
- **Visoka dostupnost**: Višeregionalno postavljanje s mogućnostima preuzimanja u slučaju pada
- **Testiranje opterećenja**: Validacija performansi pod enterprise opterećenjem
- **Obnova od katastrofe**: Automatizirani postupci sigurnosnih kopija i oporavka

Spremni za izgradnju enterprise-grade RAG sustava koji mogu rukovati osjetljivim dokumentima u velikom opsegu? Dizajnirajmo inteligentne sustave znanja za poduzeća! 🏢📖✨

## Implementacija koda

Potpuni radni uzorak koda za ovu lekciju dostupan je u `05-dotnet-agent-framework.cs`.

Za pokretanje primjera:

```bash
# Napravite skriptu izvršnom (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Pokrenite .NET aplikaciju s jedinstvenom datotekom
./05-dotnet-agent-framework.cs
```

Ili koristite `dotnet run` direktno:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod demonstrira:

1. **Instalaciju paketa**: Instalacija potrebnih NuGet paketa za Azure AI agente
2. **Konfiguraciju okruženja**: Učitavanje Microsoft Foundry endpointa i postavki modela
3. **Učitavanje dokumenata**: Učitavanje dokumenta za RAG procesiranje
4. **Kreiranje vektorskog spremišta**: Izrada vektorskog spremišta za semantičko pretraživanje
5. **Konfiguracija agenta**: Postavljanje AI agenta s mogućnostima pretraživanja datoteka
6. **Izvršavanje upita**: Pokretanje upita nad učitanim dokumentom

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->