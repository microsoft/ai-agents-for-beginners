# 🔍 Enterprise RAG s Microsoft Foundry (.NET)

## 📋 Ciljevi učenja

Ovaj bilježnik prikazuje kako izgraditi sustave za generiranje s dodatnim pretraživanjem (Retrieval-Augmented Generation, RAG) razine enterprise koristeći Microsoft Agent Framework u .NET-u s Microsoft Foundry. Naučit ćete kako stvoriti agente spremne za produkciju koji mogu pretraživati kroz dokumente i pružati točne, kontekstualno osviještene odgovore s enterprise sigurnošću i skalabilnošću.

**Enterprise RAG mogućnosti koje ćete izgraditi:**
- 📚 **Inteligencija dokumenata**: Napredna obrada dokumenata koristeći Azure AI servise
- 🔍 **Semantičko pretraživanje**: Visoko učinkovito vektorsko pretraživanje s enterprise značajkama
- 🛡️ **Integracija sigurnosti**: Kontrola pristupa temeljena na ulogama i obrasci zaštite podataka
- 🏢 **Skalabilna arhitektura**: Sistemi RAG spremni za produkciju s nadzorom

## 🎯 Enterprise RAG arhitektura

### Ključne enterprise komponente
- **Microsoft Foundry**: Upravljačka AI platforma za poduzeća s sigurnošću i usklađenošću
- **Persistent Agents**: Stanja svijesni agenti s poviješću razgovora i upravljanjem kontekstom
- **Upravljanje vektorskom pohranom**: Indeksiranje i dohvat dokumenata enterprise razine
- **Integracija identiteta**: Azure AD autentikacija i kontrola pristupa temeljena na ulogama

### .NET enterprise prednosti
- **Sigurnost tipova**: Provjera u vrijeme kompilacije za RAG operacije i podatkovne strukture
- **Asinkrona izvedba**: Neblokirajuća obrada dokumenata i operacije pretraživanja
- **Upravljanje memorijom**: Učinkovito korištenje resursa za velike zbirke dokumenata
- **Integracijski obrasci**: Izvorna integracija Azure servisa s ubrizgavanjem ovisnosti

## 🏗️ Tehnička arhitektura

### Enterprise RAG pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Ključne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje agentima enterprise razine s očuvanjem stanja
- **Azure.Identity**: Integrirana autentikacija za siguran pristup Azure servisima
- **Microsoft.Agents.AI.AzureAI**: Azure-optimizirana implementacija agent frameworka
- **System.Linq.Async**: Visoko učinkovite asinkrone LINQ operacije

## 🔧 Enterprise značajke i prednosti

### Sigurnost i usklađenost
- **Integracija Azure AD-a**: Upravljanje identitetom i autentikacija na enterprise razini
- **Kontrola pristupa temeljena na ulogama**: Precizna prava pristupa dokumentima i operacijama
- **Zaštita podataka**: Šifriranje u mirovanju i prijenosu za osjetljive dokumente
- **Evidencija revizije**: Sveobuhvatno praćenje aktivnosti radi usklađenosti

### Izvedba i skalabilnost
- **Povezivanje u pool**: Učinkovito upravljanje vezama prema Azure servisima
- **Asinkrona obrada**: Neblokirajuće operacije za scenarije velike propusnosti
- **Strategije cacheiranja**: Inteligentno keširanje često korištenih dokumenata
- **Balansiranje opterećenja**: Raspodijeljena obrada za velike implementacije

### Upravljanje i nadzor
- **Provjere zdravlja**: Ugrađeni nadzor komponenti RAG sustava
- **Mjerenje izvedbe**: Detaljne analitike kvalitete pretraživanja i vremena odziva
- **Rukovanje greškama**: Sveobuhvatno upravljanje iznimkama s politikama ponovnog pokušaja
- **Upravljanje konfiguracijom**: Okolišno specifične postavke s validacijom

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Pretplata na Azure s pristupom Microsoft Foundry

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Postavljanje Azure autentikacije:**
```bash
# Instalirajte Azure CLI i prijavite se
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracija okoline:**
* Konfiguracija Microsoft Foundry (automatski preko Azure CLI)
* Provjerite jeste li autentificirani na ispravnu Azure pretplatu

## 📊 Enterprise RAG obrasci

### Obrasci upravljanja dokumentima
- **Masovno učitavanje**: Učinkovita obrada velikih zbirki dokumenata
- **Inkrementalna ažuriranja**: Dodavanje i izmjena dokumenata u stvarnom vremenu
- **Kontrola verzija**: Verzije dokumenata i praćenje promjena
- **Upravljanje metapodacima**: Bogata svojstva dokumenata i taksonomija

### Obrasci pretraživanja i dohvaćanja
- **Hibridno pretraživanje**: Kombinacija semantičkog i pretraživanja po ključnim riječima za optimalne rezultate
- **Fasetirano pretraživanje**: Višedimenzionalno filtriranje i kategorizacija
- **Podešavanje relevantnosti**: Prilagođeni algoritmi ocjenjivanja za domen-specifične potrebe
- **Rangiranje rezultata**: Napredno rangiranje s integracijom poslovne logike

### Obrasci sigurnosti
- **Sigurnost na razini dokumenata**: Precizna kontrola pristupa za svaki dokument
- **Klasifikacija podataka**: Automatsko označavanje osjetljivosti i zaštita
- **Revizijski tragovi**: Sveobuhvatno evidentiranje svih RAG operacija
- **Zaštita privatnosti**: Detekcija i zamjena PII podataka

## 🔒 Enterprise značajke sigurnosti

### Autentikacija i autorizacija
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
- **Šifriranje**: Krajnje do krajnjeg šifriranje dokumenata i indeksa za pretraživanje
- **Kontrola pristupa**: Integracija s Azure AD za prava korisnika i grupa
- **Geografski smještaj podataka**: Kontrole lokacije podataka radi usklađenosti
- **Sigurnosne kopije i oporavak**: Automatizirano sigurnosno kopiranje i kapaciteti oporavka

## 📈 Optimizacija izvedbe

### Obrasci asinkrone obrade
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje memorijom
- **Obrada streamanjem**: Rukovanje velikim dokumentima bez problema s memorijom
- **Pooling resursa**: Učinkovito ponovno korištenje skupih resursa
- **Garbage Collection**: Optimizirani obrasci alokacije memorije
- **Upravljanje vezama**: Ispravan životni ciklus veza prema Azure servisima

### Strategije cacheiranja
- **Cacheiranje upita**: Keširanje često izvršavanih pretraživanja
- **Cacheiranje dokumenata**: Cacheiranje u memoriji za „vruće“ dokumente
- **Cacheiranje indeksa**: Optimizirano cacheiranje vektorskih indeksa
- **Cacheiranje rezultata**: Inteligentno keširanje generiranih odgovora

## 📊 Enterprise primjeri uporabe

### Upravljanje znanjem
- **Korporativna wiki**: Inteligentno pretraživanje kroz baze znanja tvrtke
- **Politike i procedure**: Automatizirana usklađenost i smjernice za procedure
- **Materijali za obuku**: Inteligentna pomoć za učenje i razvoj
- **Baze istraživanja**: Analiza akademskih i istraživačkih radova

### Korisnička podrška
- **Baza znanja za podršku**: Automatizirani korisnički odgovori
- **Dokumentacija proizvoda**: Inteligentno dohvaćanje podataka o proizvodu
- **Vodiči za rješavanje problema**: Kontekstualna pomoć u rješavanju problema
- **Sustavi često postavljanih pitanja (FAQ)**: Dinamičko generiranje FAQ-a iz zbirki dokumenata

### Usklađenost s regulativama
- **Analiza pravnih dokumenata**: Inteligencija ugovora i pravnih dokumenata
- **Praćenje usklađenosti**: Automatizirana provjera regulativne usklađenosti
- **Procjena rizika**: Analiza i izvještavanje rizika na bazi dokumenata
- **Podrška za reviziju**: Inteligentno pronalaženje dokumenata za revizije

## 🚀 Produkcijska implementacija

### Nadziranje i preglednost
- **Application Insights**: Detaljna telemetrija i nadzor izvedbe
- **Prilagođeni metrički podaci**: Praćenje i upozorenja specifičnih poslovnih KPI-jeva
- **Distribuirano praćenje**: Praćenje zahtjeva od početka do kraja kroz servise
- **Nadzorne ploče zdravlja sustava**: Vizualizacija zdravstvenog stanja i performansi u stvarnom vremenu

### Skalabilnost i pouzdanost
- **Automatsko skaliranje**: Automatsko skaliranje temeljem opterećenja i metrike izvedbe
- **Visoka dostupnost**: Implementacija u više regija s mogućnostima preuzimanja u slučaju pogreške
- **Testiranje opterećenja**: Validacija izvedbe pod enterprise opterećenjem
- **Postupci oporavka od katastrofe**: Automatizirano sigurnosno kopiranje i oporavak

Spremni za izgradnju enterprise RAG sustava koji mogu obrađivati osjetljive dokumente u velikom opsegu? Krenimo s arhitekturom inteligentnih sustava znanja za poduzeća! 🏢📖✨

## Implementacija koda

Potpuni radni uzorak koda za ovu lekciju dostupan je u `05-dotnet-agent-framework.cs`. 

Za pokretanje primjera:

```bash
# Napravite skriptu izvršnom (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Pokreni .NET aplikaciju jedne datoteke
./05-dotnet-agent-framework.cs
```

Ili upotrijebite `dotnet run` izravno:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod demonstrira:

1. **Instalaciju paketa**: Instalacija potrebnih NuGet paketa za Azure AI agente
2. **Konfiguraciju okruženja**: Učitavanje Microsoft Foundry krajnjih točaka i postavki modela
3. **Učitavanje dokumenta**: Učitavanje dokumenta za RAG obradu
4. **Stvaranje vektorske pohrane**: Izrada vektorske pohrane za semantičko pretraživanje
5. **Konfiguraciju agenta**: Postavka AI agenta s mogućnostima pretraživanja datoteka
6. **Izvršavanje upita**: Pokretanje upita prema učitanom dokumentu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->