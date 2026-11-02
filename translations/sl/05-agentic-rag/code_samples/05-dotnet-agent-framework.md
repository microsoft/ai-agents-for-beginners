# 🔍 Enterprise RAG z Microsoft Foundry (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje, kako zgraditi sisteme za generiranje z opozarjanjem na pridobivanje podatkov (RAG) na ravni podjetja z uporabo Microsoft Agent Framework v .NET z Microsoft Foundry. Naučili se boste ustvarjati agente, pripravljene za proizvodnjo, ki lahko iščejo po dokumentih in zagotavljajo natančne, kontekstno ozaveščene odgovore z varnostjo in skalabilnostjo na ravni podjetja.

**Sposobnosti Enterprise RAG, ki jih boste zgradili:**
- 📚 **Inteligenca dokumentov**: Napredno procesiranje dokumentov z Azure AI storitvami
- 🔍 **Semantično iskanje**: Visokozmogljivo vektorsko iskanje z značilnostmi podjetja
- 🛡️ **Varnostna integracija**: Nadzor dostopa na podlagi vlog in vzorci zaščite podatkov
- 🏢 **Skalabilna arhitektura**: Sistem RAG, pripravljen za proizvodnjo z nadzorom

## 🎯 Arhitektura Enterprise RAG

### Osnovne komponente podjetja
- **Microsoft Foundry**: Upravljana AI platforma podjetja z varnostjo in skladnostjo
- **Vztrajno upravljanje agentov**: Agent z zgodovino pogovorov in upravljanjem konteksta
- **Upravljanje vektorskih shramb**: Indeksiranje in pridobivanje dokumentov na ravni podjetja
- **Identitetna integracija**: Avtentikacija Azure AD in nadzor dostopa na podlagi vlog

### Prednosti .NET za podjetja
- **Tipna varnost**: Preverjanje napak med prevajanjem za operacije RAG in podatkovne strukture
- **Asinhrona zmogljivost**: Nezaustavljajoče procesiranje in iskanje dokumentov
- **Upravljanje pomnilnika**: Učinkovita raba virov za velike zbirke dokumentov
- **Integracijski vzorci**: Nativna integracija Azure storitev z uporabe DI (odvisnostne injekcije)

## 🏗️ Tehnična arhitektura

### Pipeline za Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Osnovne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje agentov z vztrajnim stanjem
- **Azure.Identity**: Integrirana avtentikacija za varni dostop do storitev Azure
- **Microsoft.Agents.AI.AzureAI**: Okvir za agente optimiziran za Azure
- **System.Linq.Async**: Visokozmogljive asinhrone LINQ operacije

## 🔧 Lastnosti in koristi za podjetja

### Varnost in skladnost
- **Integracija Azure AD**: Upravljanje identitet podjetja in avtentikacija
- **Dostop na osnovi vlog**: Natančne pravice dostopa do dokumentov in operacij
- **Zaščita podatkov**: Šifriranje pri mirovanju in prenosu za občutljive dokumente
- **Revizijsko beleženje**: Celovito spremljanje aktivnosti za zahteve skladnosti

### Zmogljivost in skalabilnost
- **Upravljanje povezav (Connection Pooling)**: Učinkovito upravljanje povezav do Azure storitev
- **Asinhrono procesiranje**: Nezaustavljajoče operacije za scenarije z visokim pretokom
- **Strategije predpomnjenja**: Inteligentno predpomnjenje pogosto dostopanih dokumentov
- **Uravnoteženje obremenitev**: Porazdeljeno procesiranje za obsežne implementacije

### Upravljanje in nadzor
- **Preverjanje zdravja**: Vgrajeni nadzor komponent RAG sistema
- **Meritve zmogljivosti**: Podrobna analitika kakovosti iskanja in časov odziva
- **Ravnanje z napakami**: Celovito upravljanje napak s politiko ponavljanja
- **Upravljanje nastavitev**: Specifične nastavitve okolja z validacijo

## ⚙️ Predpogoji in namestitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code s C# razširitvijo
- Azure naročnina z dostopom do Microsoft Foundry

**Zahtevani NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavitev Azure avtentikacije:**
```bash
# Namestite Azure CLI in se prijavite
az login
az account set --subscription "your-subscription-id"
```

**Konfiguracija okolja:**
* Konfiguracija Microsoft Foundry (samodejno upravljano preko Azure CLI)
* Prepričajte se, da ste avtenticirani v pravilni Azure naročnini

## 📊 Vzorce Enterprise RAG

### Vzorce upravljanja dokumentov
- **Serijski nalaganje**: Učinkovita obdelava velikih zbirk dokumentov
- **Inkrementalne posodobitve**: Dodajanje in spreminjanje dokumentov v realnem času
- **Nadzor različic**: Različice dokumentov in sledenje sprememb
- **Upravljanje metapodatkov**: Bogati atributi dokumentov in taksonomija

### Vzorce iskanja in pridobivanja
- **Hibridno iskanje**: Združevanje semantičnega in ključnoločnega iskanja za optimalne rezultate
- **Večdimenzionalno filtriranje**: Večplasten filter in kategorizacija
- **Prilagoditev relevantnosti**: Prilagojeni algoritmi točkovanja za domensko specifične potrebe
- **Razvrščanje rezultatov**: Napredno razvrščanje z integracijo poslovne logike

### Vzorce varnosti
- **Varnost na ravni dokumenta**: Natančen nadzor dostopa za posamezne dokumente
- **Klasifikacija podatkov**: Avtomatsko označevanje občutljivosti in zaščita
- **Revizijski sledovi**: Celovito beleženje vseh RAG operacij
- **Zaščita zasebnosti**: Možnosti zaznavanja in prekrivanja osebnih podatkov (PII)

## 🔒 Lastnosti varnosti za podjetja

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
- **Šifriranje**: Končna do končne šifriranje za dokumente in indeks iskanja
- **Kontrola dostopa**: Integracija z Azure AD za pravice uporabnikov in skupin
- **Lokacija podatkov**: Geografska lokacija podatkov za skladnost
- **Varnostno kopiranje in obnovitev**: Avtomatizirane možnosti varnostnega kopiranja in obnovitve po nesrečah

## 📈 Optimizacija zmogljivosti

### Vzorce asinhrone obdelave
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje pomnilnika
- **Pretakanje obdelave**: Obdelava velikih dokumentov brez težav s pomnilnikom
- **Združevanje virov**: Učinkovita ponovno uporaba dragocenih virov
- **Zbirka odpadkov**: Optimizirani vzorci dodeljevanja pomnilnika
- **Upravljanje povezav**: Pravilno upravljanje življenjskega cikla povezave do Azure storitev

### Strategije predpomnjenja
- **Predpomnjenje poizvedb**: Predpomnjenje pogosto izvajajočih se iskanj
- **Predpomnjenje dokumentov**: Predpomnjenje v pomnilniku za pogosto dostopane dokumente
- **Predpomnjenje indeksov**: Optimizirano predpomnjenje vektorskih indeksov
- **Predpomnjenje rezultatov**: Inteligentno predpomnjenje generiranih odgovorov

## 📊 Primeri uporabe za podjetja

### Upravljanje znanja
- **Podjetniški wiki**: Inteligentno iskanje po korporativnih zbirkah znanja
- **Pravila in postopki**: Avtomatizirano usmerjanje za skladnost in postopke
- **Učni materiali**: Inteligentna pomoč pri učenju in razvoju
- **Raziskovalne baze podatkov**: Sistemi za analizo akademskih in raziskovalnih dokumentov

### Podpora strankam
- **Baza znanja za podporo**: Avtomatizirani odgovori za stranko
- **Dokumentacija izdelkov**: Inteligentno pridobivanje informacij o izdelku
- **Vodniki za odpravljanje težav**: Kontekstualna pomoč pri reševanju problemov
- **Sistemi pogostih vprašanj (FAQ)**: Dinamična generacija FAQ iz zbirk dokumentov

### Regulatorna skladnost
- **Analiza pravnih dokumentov**: Inteligenca pogodb in pravnih dokumentov
- **Nadzor skladnosti**: Avtomatizirano preverjanje skladnosti z regulativami
- **Ocenjevanje tveganj**: Analiza tveganj na osnovi dokumentov in poročanje
- **Podpora reviziji**: Inteligentno odkrivanje dokumentov za revizije

## 🚀 Implementacija v produkciji

### Nadzor in opazovanje
- **Application Insights**: Podrobna telemetrija in nadzor zmogljivosti
- **Prilagojene meritve**: Sledenje in obveščanje poslovno specifičnih KPI-jev
- **Porazdeljeno sledenje**: Celovito sledenje zahtevkom preko storitev
- **Nadzorne plošče zdravja**: Vizualizacija zdravja in zmogljivosti sistema v realnem času

### Skalabilnost in zanesljivost
- **Samodejno skaliranje**: Samodejno prilagajanje glede na obremenitev in metrike zmogljivosti
- **Visoka razpoložljivost**: Večregijska razmestitev z možnostmi preklopa v sili
- **Testiranje obremenitve**: Validacija zmogljivosti pod pogoji obremenitve podjetja
- **Obnova po nesreči**: Avtomatizirani postopki varnostnega kopiranja in obnove

Ste pripravljeni zgraditi sisteme RAG na ravni podjetja, ki lahko obvladujejo občutljive dokumente v velikem obsegu? Začnimo z načrtovanjem inteligentnih sistemov znanja za podjetja! 🏢📖✨

## Implementacija kode

Celoten delujoči vzorec kode za to lekcijo je na voljo v `05-dotnet-agent-framework.cs`.

Za zagon primera:

```bash
# Nastavite skripto kot izvršljivo (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Zaženite .NET aplikacijo v eni datoteki
./05-dotnet-agent-framework.cs
```

Ali pa uporabite neposredno `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koda prikazuje:

1. **Namestitev paketov**: Namestitev zahtevanih NuGet paketov za Azure AI agente
2. **Konfiguracija okolja**: Nalaganje Microsoft Foundry končnega točke in nastavitev modela
3. **Nalaganje dokumenta**: Nalaganje dokumenta za RAG obdelavo
4. **Ustvarjanje vektorske shramba**: Ustvarjanje vektorske shrambe za semantično iskanje
5. **Konfiguracija agenta**: Nastavitev AI agenta z zmožnostjo iskanja datotek
6. **Izvajanje poizvedb**: Izvajanje poizvedb na naloženem dokumentu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->