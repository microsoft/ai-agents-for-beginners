<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:10:26+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🔍 Enterprise RAG z Azure AI Foundry (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje, kako zgraditi sisteme za pridobivanje informacij z izboljšano generacijo (RAG) na ravni podjetja z uporabo Microsoft Agent Framework v .NET z Azure AI Foundry. Naučili se boste ustvariti agente, pripravljene za produkcijo, ki lahko iščejo po dokumentih in zagotavljajo natančne, kontekstualno ustrezne odgovore z varnostjo in skalabilnostjo na ravni podjetja.

**Zmožnosti Enterprise RAG, ki jih boste razvili:**
- 📚 **Inteligenca dokumentov**: Napredno procesiranje dokumentov z Azure AI storitvami
- 🔍 **Semantično iskanje**: Visoko zmogljivo iskanje vektorjev z funkcijami za podjetja
- 🛡️ **Integracija varnosti**: Dostop na podlagi vlog in vzorci zaščite podatkov
- 🏢 **Skalabilna arhitektura**: Sistemi RAG, pripravljeni za produkcijo, z nadzorom

## 🎯 Arhitektura Enterprise RAG

### Osnovne komponente za podjetja
- **Azure AI Foundry**: Upravljana platforma za umetno inteligenco z varnostjo in skladnostjo
- **Persistentni agenti**: Agenti s stanjem, zgodovino pogovorov in upravljanjem konteksta
- **Upravljanje vektorskih baz**: Indeksiranje in pridobivanje dokumentov na ravni podjetja
- **Integracija identitete**: Avtentikacija Azure AD in nadzor dostopa na podlagi vlog

### Prednosti .NET za podjetja
- **Tipna varnost**: Validacija operacij RAG in podatkovnih struktur med prevajanjem
- **Asinhrona zmogljivost**: Nezastojno procesiranje dokumentov in operacije iskanja
- **Upravljanje pomnilnika**: Učinkovita uporaba virov za velike zbirke dokumentov
- **Vzorce integracije**: Naravna integracija Azure storitev z vbrizgavanjem odvisnosti

## 🏗️ Tehnična arhitektura

### Enterprise RAG cevovod
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Osnovne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje agentov na ravni podjetja z ohranjanjem stanja
- **Azure.Identity**: Integrirana avtentikacija za varni dostop do Azure storitev
- **Microsoft.Agents.AI.AzureAI**: Implementacija agentnega okvira, optimizirana za Azure
- **System.Linq.Async**: Visoko zmogljive asinhrone operacije LINQ

## 🔧 Funkcije in prednosti za podjetja

### Varnost in skladnost
- **Integracija Azure AD**: Upravljanje identitete in avtentikacije na ravni podjetja
- **Dostop na podlagi vlog**: Natančno določene pravice za dostop do dokumentov in operacij
- **Zaščita podatkov**: Šifriranje v mirovanju in med prenosom za občutljive dokumente
- **Dnevnik revizij**: Celovito sledenje dejavnostim za zahteve skladnosti

### Zmogljivost in skalabilnost
- **Upravljanje povezav**: Učinkovito upravljanje povezav do Azure storitev
- **Asinhrono procesiranje**: Nezastojne operacije za scenarije z visokim pretokom
- **Strategije predpomnjenja**: Inteligentno predpomnjenje pogosto dostopnih dokumentov
- **Uravnavanje obremenitve**: Porazdeljeno procesiranje za velike implementacije

### Upravljanje in nadzor
- **Preverjanje zdravja**: Vgrajen nadzor komponent sistema RAG
- **Meritve zmogljivosti**: Podrobna analitika kakovosti iskanja in časov odziva
- **Upravljanje napak**: Celovito upravljanje izjem z politikami ponovnega poskusa
- **Upravljanje konfiguracije**: Nastavitve specifične za okolje z validacijo

## ⚙️ Predpogoji in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Azure naročnina z dostopom do AI Foundry

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavitev avtentikacije Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracija okolja:**
* Konfiguracija Azure AI Foundry (samodejno upravljana prek Azure CLI)
* Prepričajte se, da ste avtenticirani v pravilno Azure naročnino

## 📊 Vzorci Enterprise RAG

### Vzorci upravljanja dokumentov
- **Masovni prenos**: Učinkovito procesiranje velikih zbirk dokumentov
- **Postopne posodobitve**: Dodajanje in spreminjanje dokumentov v realnem času
- **Upravljanje različic**: Različice dokumentov in sledenje spremembam
- **Upravljanje metapodatkov**: Bogati atributi dokumentov in taksonomija

### Vzorci iskanja in pridobivanja
- **Hibridno iskanje**: Kombinacija semantičnega in ključnega iskanja za optimalne rezultate
- **Fasetno iskanje**: Večdimenzionalno filtriranje in kategorizacija
- **Prilagoditev ustreznosti**: Prilagojeni algoritmi za točkovanje za specifične domene
- **Razvrščanje rezultatov**: Napredno razvrščanje z integracijo poslovne logike

### Varnostni vzorci
- **Varnost na ravni dokumentov**: Natančen nadzor dostopa za vsak dokument
- **Razvrščanje podatkov**: Samodejno označevanje občutljivosti in zaščita
- **Revizijske sledi**: Celovito beleženje vseh operacij RAG
- **Zaščita zasebnosti**: Zaznavanje in redakcija osebnih podatkov (PII)

## 🔒 Funkcije varnosti za podjetja

### Avtentikacija in avtorizacija
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

### Zaščita podatkov
- **Šifriranje**: Šifriranje od konca do konca za dokumente in indekse iskanja
- **Nadzor dostopa**: Integracija z Azure AD za pravice uporabnikov in skupin
- **Lokacija podatkov**: Geografski nadzor lokacije podatkov za skladnost
- **Varnostno kopiranje in obnovitev**: Samodejno varnostno kopiranje in postopki za obnovitev

## 📈 Optimizacija zmogljivosti

### Vzorci asinhronega procesiranja
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje pomnilnika
- **Procesiranje pretoka**: Obdelava velikih dokumentov brez težav s pomnilnikom
- **Upravljanje virov**: Učinkovita ponovna uporaba dragih virov
- **Zbiranje smeti**: Optimizirani vzorci dodeljevanja pomnilnika
- **Upravljanje povezav**: Pravilno upravljanje življenjskega cikla povezav do Azure storitev

### Strategije predpomnjenja
- **Predpomnjenje poizvedb**: Predpomnjenje pogosto izvedenih iskanj
- **Predpomnjenje dokumentov**: Predpomnjenje v pomnilniku za priljubljene dokumente
- **Predpomnjenje indeksov**: Optimizirano predpomnjenje vektorskih indeksov
- **Predpomnjenje rezultatov**: Inteligentno predpomnjenje generiranih odgovorov

## 📊 Uporabni primeri za podjetja

### Upravljanje znanja
- **Korporativna Wiki**: Inteligentno iskanje po bazah znanja podjetja
- **Politike in postopki**: Samodejno vodenje skladnosti in postopkov
- **Učni materiali**: Inteligentna pomoč pri učenju in razvoju
- **Raziskovalne baze**: Sistemi za analizo akademskih in raziskovalnih člankov

### Podpora strankam
- **Baza znanja za podporo**: Samodejni odgovori za storitve za stranke
- **Dokumentacija izdelkov**: Inteligentno pridobivanje informacij o izdelkih
- **Vodniki za odpravljanje težav**: Kontekstualna pomoč pri reševanju težav
- **Sistemi FAQ**: Dinamično generiranje pogostih vprašanj iz zbirk dokumentov

### Skladnost z regulativami
- **Analiza pravnih dokumentov**: Inteligenca za pogodbe in pravne dokumente
- **Nadzor skladnosti**: Samodejno preverjanje skladnosti z regulativami
- **Ocena tveganja**: Analiza tveganj na podlagi dokumentov in poročanje
- **Podpora pri revizijah**: Inteligentno odkrivanje dokumentov za revizije

## 🚀 Produkcijska implementacija

### Nadzor in opazovanje
- **Application Insights**: Podrobna telemetrija in nadzor zmogljivosti
- **Prilagojene meritve**: Sledenje in opozarjanje na poslovno specifične KPI-je
- **Porazdeljeno sledenje**: Sledenje zahtevkom od začetka do konca med storitvami
- **Nadzorne plošče zdravja**: Vizualizacija zdravja sistema in zmogljivosti v realnem času

### Skalabilnost in zanesljivost
- **Samodejno skaliranje**: Samodejno prilagajanje na podlagi obremenitve in zmogljivosti
- **Visoka razpoložljivost**: Implementacija v več regijah z možnostjo preklopa ob okvari
- **Testiranje obremenitve**: Validacija zmogljivosti pod obremenitvijo na ravni podjetja
- **Obnova po katastrofi**: Samodejno varnostno kopiranje in postopki za obnovitev

Pripravljeni na gradnjo sistemov RAG na ravni podjetja, ki lahko obdelujejo občutljive dokumente v velikem obsegu? Zasnovimo inteligentne sisteme znanja za podjetja! 🏢📖✨

## Implementacija kode

Celoten delujoč vzorec kode za to lekcijo je na voljo v `05-dotnet-agent-framework.cs`. 

Za zagon primera:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Ali uporabite `dotnet run` neposredno:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koda prikazuje:

1. **Namestitev paketov**: Namestitev potrebnih NuGet paketov za Azure AI agente
2. **Konfiguracija okolja**: Nalaganje nastavitev končne točke in modela Azure AI Foundry
3. **Prenos dokumenta**: Prenos dokumenta za procesiranje RAG
4. **Ustvarjanje vektorske baze**: Ustvarjanje vektorske baze za semantično iskanje
5. **Konfiguracija agenta**: Nastavitev AI agenta z zmožnostmi iskanja po datotekah
6. **Izvajanje poizvedb**: Izvajanje poizvedb na prenesenem dokumentu

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.