# 🔍 Poslovni RAG z Microsoft Foundry (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje, kako zgraditi sistema za generiranje z obogatitvijo iskanja (RAG) na poslovni ravni z uporabo Microsoft Agent Framework v .NET z Microsoft Foundry. Naučili se boste ustvariti produkte pripravljene agente, ki lahko preiskujejo dokumente in zagotavljajo natančne, v kontekst umeščene odzive z varnostjo in razširljivostjo za podjetja.

**Poslovne zmožnosti RAG, ki jih boste zgradili:**
- 📚 **Inteligenca dokumentov**: Napredna obdelava dokumentov z Azure AI storitvami
- 🔍 **Semantično iskanje**: Visoko zmogljivo iskanje po vektorskih podatkih s poslovnimi funkcijami
- 🛡️ **Integracija varnosti**: Dostop na osnovi vlog in vzorci zaščite podatkov
- 🏢 **Razširljiva arhitektura**: Sistemi RAG pripravljeni za produkcijo z nadzorom

## 🎯 Poslovna arhitektura RAG

### Glavne poslovne komponente
- **Microsoft Foundry**: Upravljana poslovna AI platforma z varnostjo in skladnostjo
- **Vztrajni agenti**: Zastavek stanja agenta z zgodovino pogovorov in upravljanjem konteksta
- **Upravljanje skladišča vektorjev**: Indeksiranje in pridobivanje poslovnih dokumentov
- **Integracija identitete**: Avtentikacija Azure AD in nadzor dostopa na osnovi vlog

### Prednosti .NET za podjetja
- **Varnost tipov**: Preverjanje ob času prevajanja za operacije RAG in podatkovne strukture
- **Asinhrona zmogljivost**: Neblokirajoča obdelava dokumentov in iskalne operacije
- **Upravljanje pomnilnika**: Učinkovita raba virov za velike zbirke dokumentov
- **Integracijski vzorci**: Naravna integracija Azure storitev z injekcijo odvisnosti

## 🏗️ Tehnična arhitektura

### Poslovna RAG cevovod
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Osnovne .NET komponente
- **Azure.AI.Agents.Persistent**: Upravljanje poslovnih agentov z vztrajanjem stanja
- **Azure.Identity**: Integrirana avtentikacija za varen dostop do Azure storitev
- **Microsoft.Agents.AI.AzureAI**: Okvir za agente optimiziran za Azure
- **System.Linq.Async**: Visoko zmogljive asinhrone LINQ operacije

## 🔧 Poslovne funkcije in prednosti

### Varnost in skladnost
- **Integracija Azure AD**: Upravljanje identitete in avtentikacija za podjetja
- **Dostop na osnovi vlog**: Detajlne pravice za dostop do dokumentov in operacij
- **Zaščita podatkov**: Šifriranje v mirovanju in med prenosom za občutljive dokumente
- **Revizijsko beleženje**: Celostno sledenje dejavnosti za zahteve skladnosti

### Zmogljivost in razširljivost
- **Povezovalni bazeni**: Učinkovito upravljanje povezav do Azure storitev
- **Asinhrona obdelava**: Neblokirajoče operacije za scenarije z visokim tokom
- **Strategije predpomnjenja**: Inteligentno predpomnjenje pogosto uporabljenih dokumentov
- **Uravnoteženje obremenitev**: Razdeljena obdelava za velike razporeditve

### Upravljanje in nadzor
- **Preverjanje zdravja**: Vgrajeno spremljanje komponent RAG sistema
- **Meritve zmogljivosti**: Podrobna analitika kakovosti iskanja in časov odziva
- **Obravnava napak**: Celovito upravljanje izjem z možnostmi poskusov ponovnega izvajanja
- **Upravljanje konfiguracije**: Nastavitve za okolja s preverjanjem veljavnosti

## ⚙️ Predpogoji in namestitev

**Razvojno okolje:**
- SDK .NET 9.0 ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo C#
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
* Konfiguracija Microsoft Foundry (samodejno upravljana preko Azure CLI)
* Zagotovite, da ste prijavljeni na pravilno Azure naročnino

## 📊 Poslovni vzorci RAG

### Vzorci upravljanja dokumentov
- **Masovni prenos**: Učinkovita obdelava velikih zbirk dokumentov
- **Postopne posodobitve**: Dodajanje in spreminjanje dokumentov v realnem času
- **Nadzor različic**: Verzijsko vodenje dokumentov in sledenje sprememb
- **Upravljanje metapodatkov**: Bogati atributi dokumentov in taksonomija

### Vzorci iskanja in pridobivanja
- **Hibridno iskanje**: Združevanje semantičnega in ključnega iskanja za optimalne rezultate
- **Fasetno iskanje**: Večdimenzionalno filtriranje in kategorizacija
- **Usklajevanje relevantnosti**: Prilagojeni algoritmi ocenjevanja za specifične domene
- **Razvrščanje rezultatov**: Napredno razvrščanje z integracijo poslovne logike

### Vzorci varnosti
- **Varnost na ravni dokumentov**: Detajlni nadzor dostopa za vsak dokument
- **Klasifikacija podatkov**: Samodejno označevanje občutljivosti in zaščita
- **Revizijske sledi**: Celovito beleženje vseh RAG operacij
- **Zaščita zasebnosti**: Zmožnosti zaznavanja in prerazporejanja osebnih podatkov

## 🔒 Poslovne varnostne funkcije

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
- **Šifriranje**: Popolna šifriranost dokumentov in indeksov iskanja
- **Kontrole dostopa**: Integracija z Azure AD za uporabniške in skupinske pravice
- **Lokacija podatkov**: Geografski nadzor nad lokacijo podatkov za skladnost
- **Varnostno kopiranje in obnova**: Avtomatizirane zmožnosti varnostnega kopiranja in obnove ob izgubi

## 📈 Optimizacija zmogljivosti

### Vzorci asinhrone obdelave
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Upravljanje pomnilnika
- **Pretakajoča obdelava**: Obravnava velikih dokumentov brez težav s pomnilnikom
- **Skupki virov**: Učinkovita ponovna uporaba dragocenih virov
- **Garbage Collection**: Optimizirani vzorci dodeljevanja pomnilnika
- **Upravljanje povezav**: Pravilno upravljanje življenjskega cikla povezav do Azure storitev

### Strategije predpomnjenja
- **Predpomnjenje poizvedb**: Predpomnjenje pogosto izvajanja iskanj
- **Predpomnjenje dokumentov**: Predpomnjenje v pomnilniku za vroče dokumente
- **Predpomnjenje indeksov**: Optimizirano predpomnjenje vektorskih indeksov
- **Predpomnjenje rezultatov**: Inteligentno predpomnjenje generiranih odgovorov

## 📊 Poslovni primeri uporabe

### Upravljanje znanja
- **Podjetniška wiki**: Inteligentno iskanje po podjetniških bazah znanja
- **Politike in postopki**: Samodejno usmerjanje po skladnosti in postopkih
- **Učni materiali**: Inteligentna pomoč pri učenju in razvoju
- **Raziskovalne baze**: Sistemi za analizo akademskih in raziskovalnih člankov

### Podpora strankam
- **Baza znanja za podporo**: Samodejni odgovori za podporo strankam
- **Dokumentacija izdelkov**: Inteligentno pridobivanje informacij o izdelku
- **Vodiči za odpravljanje težav**: Pomoč pri reševanju težav v kontekstu
- **Sistemi FAQ**: Dinamična generacija pogostih vprašanj iz zbirk dokumentov

### Skladnost z regulativo
- **Analiza pravnih dokumentov**: Inteligenca pogodb in pravnih dokumentov
- **Nadzor skladnosti**: Samodejno preverjanje skladnosti z regulativami
- **Ocenjevanje tveganj**: Analiza tveganj na osnovi dokumentov in poročanje
- **Podpora reviziji**: Inteligentno odkrivanje dokumentov za revizije

## 🚀 Produkcijska implementacija

### Nadzor in opazovanje
- **Application Insights**: Podrobna telemetrija in spremljanje zmogljivosti
- **Lastne meritve**: Spremljanje KPI po meri in opozorila
- **Distribuirano sledenje**: Sledenje zahtev od začetka do konca v storitvah
- **Nadzorne nadzorne plošče**: Vizualizacija zdravja in zmogljivosti sistema v realnem času

### Razširljivost in zanesljivost
- **Samodejno skaliranje**: Samodejno prilagajanje glede na obremenitev in meritve zmogljivosti
- **Visoka razpoložljivost**: Razporeditev v več regijah z možnostjo preklopa ob napaki
- **Preizkušanje obremenitve**: Preverjanje zmogljivosti pod podjetniškimi pogoji obremenitve
- **Obnova po nesrečah**: Avtomatizirani postopki varnostnega kopiranja in obnove

Ste pripravljeni graditi sisteme RAG na poslovni ravni, ki lahko upravljajo občutljive dokumente v velikem obsegu? Zasnovimo inteligentne sisteme znanja za podjetja! 🏢📖✨

## Implementacija kode

Celoten delujoči vzorec kode za to lekcijo je na voljo v `05-dotnet-agent-framework.cs`.

Za zagon primera:

```bash
# Nastavite skripto kot izvršljivo (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Zaženite .NET aplikacijo z eno datoteko
./05-dotnet-agent-framework.cs
```

Ali uporabite `dotnet run` neposredno:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koda prikazuje:

1. **Namestitev paketov**: Namestitev potrebnih paketi NuGet za Azure AI agente
2. **Konfiguracija okolja**: Nalaganje nastavitev Microsoft Foundry vtični točke in modelov
3. **Nalaganje dokumenta**: Nalaganje dokumenta za obdelavo RAG
4. **Ustvarjanje skladišča vektorjev**: Ustvarjanje vektorskega skladišča za semantično iskanje
5. **Konfiguracija agenta**: Nastavitev AI agenta z zmogljivostmi iskanja po datotekah
6. **Izvajanje poizvedb**: Izvajanje poizvedb nad naloženim dokumentom

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->