<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:10:04+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🔍 Enterprise RAG s Azure AI Foundry (.NET)

## 📋 Ciljevi učenja

Ovaj notebook pokazuje kako izgraditi sustave za dohvat uz proširenu generaciju (RAG) na razini poduzeća koristeći Microsoft Agent Framework u .NET-u s Azure AI Foundry. Naučit ćete kako kreirati agente spremne za produkciju koji mogu pretraživati dokumente i pružati točne, kontekstualno svjesne odgovore uz sigurnost i skalabilnost na razini poduzeća.

**Mogućnosti Enterprise RAG sustava koje ćete izgraditi:**
- 📚 **Inteligencija dokumenata**: Napredno procesiranje dokumenata s Azure AI uslugama
- 🔍 **Semantičko pretraživanje**: Visokoučinkovito pretraživanje vektora s funkcijama za poduzeća
- 🛡️ **Integracija sigurnosti**: Pristup temeljen na ulogama i obrasci zaštite podataka
- 🏢 **Skalabilna arhitektura**: RAG sustavi spremni za produkciju s praćenjem

## 🎯 Arhitektura Enterprise RAG-a

### Ključne komponente za poduzeća
- **Azure AI Foundry**: Upravljana AI platforma za poduzeća sa sigurnošću i usklađenošću
- **Persistentni agenti**: Agenti sa stanjem koji čuvaju povijest razgovora i upravljanje kontekstom
- **Upravljanje vektorskom pohranom**: Indeksiranje i dohvat dokumenata na razini poduzeća
- **Integracija identiteta**: Autentifikacija putem Azure AD-a i kontrola pristupa temeljenog na ulogama

### Prednosti .NET-a za poduzeća
- **Sigurnost tipova**: Validacija u vrijeme kompilacije za RAG operacije i strukture podataka
- **Asinkrona izvedba**: Ne-blokirajuće procesiranje dokumenata i operacije pretraživanja
- **Upravljanje memorijom**: Učinkovito korištenje resursa za velike kolekcije dokumenata
- **Integracijski obrasci**: Nativna integracija Azure usluga s ubrizgavanjem ovisnosti

## 🏗️ Tehnička arhitektura

### Enterprise RAG cjevovod
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Ključne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje agentima za poduzeća s trajnim stanjem
- **Azure.Identity**: Integrirana autentifikacija za siguran pristup Azure uslugama
- **Microsoft.Agents.AI.AzureAI**: Implementacija optimiziranog okvira za agente u Azureu
- **System.Linq.Async**: Visokoučinkovite asinkrone LINQ operacije

## 🔧 Značajke i prednosti za poduzeća

### Sigurnost i usklađenost
- **Integracija s Azure AD-om**: Upravljanje identitetima i autentifikacija za poduzeća
- **Pristup temeljen na ulogama**: Fino podešene dozvole za pristup dokumentima i operacijama
- **Zaštita podataka**: Šifriranje u mirovanju i tijekom prijenosa za osjetljive dokumente
- **Dnevnik aktivnosti**: Sveobuhvatno praćenje aktivnosti za zahtjeve usklađenosti

### Izvedba i skalabilnost
- **Upravljanje vezama**: Učinkovito upravljanje vezama s Azure uslugama
- **Asinkrono procesiranje**: Ne-blokirajuće operacije za scenarije visokog kapaciteta
- **Strategije predmemoriranja**: Inteligentno predmemoriranje često pristupanih dokumenata
- **Ravnoteža opterećenja**: Distribuirano procesiranje za implementacije velikih razmjera

### Upravljanje i praćenje
- **Provjere zdravlja**: Ugrađeno praćenje komponenti RAG sustava
- **Metričke izvedbe**: Detaljna analitika kvalitete pretraživanja i vremena odgovora
- **Upravljanje greškama**: Sveobuhvatno upravljanje iznimkama s politikama ponovnog pokušaja
- **Upravljanje konfiguracijom**: Postavke specifične za okruženje s validacijom

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Azure pretplata s pristupom AI Foundry

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Postavljanje autentifikacije za Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracija okruženja:**
* Konfiguracija Azure AI Foundry (automatski se postavlja putem Azure CLI-ja)
* Provjerite jeste li autentificirani na ispravnu Azure pretplatu

## 📊 Obrasci Enterprise RAG-a

### Obrasci upravljanja dokumentima
- **Masovno učitavanje**: Učinkovito procesiranje velikih kolekcija dokumenata
- **Inkrementalna ažuriranja**: Dodavanje i izmjena dokumenata u stvarnom vremenu
- **Kontrola verzija**: Verzioniranje dokumenata i praćenje promjena
- **Upravljanje metapodacima**: Bogati atributi dokumenata i taksonomija

### Obrasci pretraživanja i dohvaćanja
- **Hibridno pretraživanje**: Kombiniranje semantičkog i ključnog pretraživanja za optimalne rezultate
- **Pretraživanje s fasetama**: Višedimenzionalno filtriranje i kategorizacija
- **Podešavanje relevantnosti**: Prilagođeni algoritmi bodovanja za specifične domene
- **Rangiranje rezultata**: Napredno rangiranje s integracijom poslovne logike

### Obrasci sigurnosti
- **Sigurnost na razini dokumenta**: Fino podešena kontrola pristupa po dokumentu
- **Klasifikacija podataka**: Automatsko označavanje osjetljivosti i zaštita
- **Dnevnici aktivnosti**: Sveobuhvatno bilježenje svih RAG operacija
- **Zaštita privatnosti**: Otkrivanje i redakcija osobnih podataka (PII)

## 🔒 Značajke sigurnosti za poduzeća

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
- **Šifriranje**: Šifriranje od kraja do kraja za dokumente i indekse pretraživanja
- **Kontrole pristupa**: Integracija s Azure AD-om za dozvole korisnika i grupa
- **Rezidencija podataka**: Kontrole lokacije podataka za usklađenost
- **Sigurnosne kopije i oporavak**: Automatizirane sigurnosne kopije i postupci oporavka

## 📈 Optimizacija izvedbe

### Obrasci asinkronog procesiranja
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje memorijom
- **Procesiranje u streamu**: Obrada velikih dokumenata bez problema s memorijom
- **Upravljanje resursima**: Učinkovito ponovno korištenje skupih resursa
- **Sakupljanje smeća**: Optimizirani obrasci dodjele memorije
- **Upravljanje vezama**: Pravilno upravljanje životnim ciklusom veze s Azure uslugama

### Strategije predmemoriranja
- **Predmemoriranje upita**: Predmemoriranje često izvršenih pretraživanja
- **Predmemoriranje dokumenata**: Predmemoriranje u memoriji za "vruće" dokumente
- **Predmemoriranje indeksa**: Optimizirano predmemoriranje vektorskih indeksa
- **Predmemoriranje rezultata**: Inteligentno predmemoriranje generiranih odgovora

## 📊 Primjene za poduzeća

### Upravljanje znanjem
- **Korporativni Wiki**: Inteligentno pretraživanje kroz baze znanja tvrtke
- **Politike i procedure**: Automatizirano usklađivanje i smjernice za procedure
- **Materijali za obuku**: Inteligentna pomoć u učenju i razvoju
- **Baze podataka za istraživanje**: Sustavi za analizu akademskih i istraživačkih radova

### Korisnička podrška
- **Baza znanja za podršku**: Automatizirani odgovori za korisničku podršku
- **Dokumentacija proizvoda**: Inteligentno dohvaćanje informacija o proizvodima
- **Vodiči za rješavanje problema**: Kontekstualna pomoć u rješavanju problema
- **Sustavi FAQ-a**: Dinamičko generiranje FAQ-a iz kolekcija dokumenata

### Usklađenost s regulativama
- **Analiza pravnih dokumenata**: Inteligencija za ugovore i pravne dokumente
- **Praćenje usklađenosti**: Automatizirano provjeravanje usklađenosti s regulativama
- **Procjena rizika**: Analiza i izvještavanje o rizicima temeljenim na dokumentima
- **Podrška za revizije**: Inteligentno otkrivanje dokumenata za revizije

## 🚀 Produkcijska implementacija

### Praćenje i preglednost
- **Application Insights**: Detaljna telemetrija i praćenje izvedbe
- **Prilagođene metrike**: Praćenje i upozorenja za poslovno specifične KPI-jeve
- **Distribuirano praćenje**: Praćenje zahtjeva od kraja do kraja kroz usluge
- **Nadzorne ploče zdravlja**: Vizualizacija zdravlja i izvedbe sustava u stvarnom vremenu

### Skalabilnost i pouzdanost
- **Automatsko skaliranje**: Automatsko skaliranje na temelju opterećenja i metričkih izvedbi
- **Visoka dostupnost**: Implementacija u više regija s mogućnostima prebacivanja
- **Testiranje opterećenja**: Validacija izvedbe pod opterećenjem na razini poduzeća
- **Oporavak od katastrofe**: Automatizirane sigurnosne kopije i postupci oporavka

Spremni za izgradnju RAG sustava na razini poduzeća koji mogu rukovati osjetljivim dokumentima u velikom opsegu? Idemo arhitektirati inteligentne sustave znanja za poduzeća! 🏢📖✨

## Implementacija koda

Potpuni radni primjer koda za ovu lekciju dostupan je u `05-dotnet-agent-framework.cs`. 

Za pokretanje primjera:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Ili koristite `dotnet run` direktno:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod demonstrira:

1. **Instalacija paketa**: Instalacija potrebnih NuGet paketa za Azure AI agente
2. **Konfiguracija okruženja**: Učitavanje postavki za Azure AI Foundry endpoint i model
3. **Učitavanje dokumenata**: Učitavanje dokumenta za RAG procesiranje
4. **Kreiranje vektorske pohrane**: Kreiranje vektorske pohrane za semantičko pretraživanje
5. **Konfiguracija agenta**: Postavljanje AI agenta s mogućnostima pretraživanja datoteka
6. **Izvršavanje upita**: Pokretanje upita na učitanom dokumentu

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.