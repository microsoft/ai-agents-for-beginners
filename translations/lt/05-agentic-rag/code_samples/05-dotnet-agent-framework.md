# 🔍 Įmonių RAG su Microsoft Foundry (.NET)

## 📋 Mokymosi tikslai

Šis užrašų blokas demonstruoja, kaip sukurti įmonėms skirtas Retrieval-Augmented Generation (RAG) sistemas, naudojant Microsoft Agent Framework .NET su Microsoft Foundry. Išmoksite kurti gamybai pasiruošusius agentus, kurie gali ieškoti dokumentuose ir pateikti tikslius, kontekstinius atsakymus su įmonių saugumu ir mastu.

**Įgysite šias įmonių RAG galimybes:**
- 📚 **Dokumentų intelektas**: Pažangus dokumentų apdorojimas naudojant Azure AI paslaugas
- 🔍 **Semantinis paieška**: Aukšto našumo vektorinė paieška su įmonių funkcijomis
- 🛡️ **Saugumo integracija**: Rolės pagrindu veikiantis prieigos valdymas ir duomenų apsaugos modeliai
- 🏢 **Mastelio architektūra**: Gamybai paruoštos RAG sistemos su stebėsena

## 🎯 Įmonių RAG architektūra

### Pagrindinės įmonių sudedamosios dalys
- **Microsoft Foundry**: Valdoma įmonių AI platforma su saugumu ir atitiktimi
- **Nuolatiniai agentai**: Būsenoje esančių agentų, turinčių pokalbių istoriją ir konteksto valdymą
- **Vektorinės saugyklos valdymas**: Įmonių lygio dokumentų indeksavimas ir gavimas
- **Tapatybės integracija**: Azure AD autentifikacija ir rolės pagrindu veikiantis prieigos kontrolė

### .NET įmonių privalumai
- **Tipų saugumas**: Kompiliavimo metu vykdoma RAG operacijų ir duomenų struktūrų patikra
- **Asinchroninis veikimas**: Netrukdantis dokumentų apdorojimas ir paieškos operacijos
- **Atminties valdymas**: Efektyvus išteklių naudojimas didelėms dokumentų kolekcijoms
- **Integracijos modeliai**: Natūrali Azure paslaugų integracija su priklausomybių injekcija

## 🏗️ Techninė architektūra

### Įmonių RAG srautas
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Pagrindinės .NET sudedamosios dalys
- **Azure.AI.Agents.Persistent**: Įmonių agentų valdymas su būsenos išsaugojimu
- **Azure.Identity**: Integruota autentifikacija saugiam Azure paslaugų pasiekiamumui
- **Microsoft.Agents.AI.AzureAI**: Azure optimizuota agentų platformos įgyvendinimas
- **System.Linq.Async**: Aukšto našumo asinchroninės LINQ operacijos

## 🔧 Įmonių funkcijos ir privalumai

### Saugumas ir atitiktis
- **Azure AD integracija**: Įmonių tapatybės valdymas ir autentifikacija
- **Rolės pagrindu veikianti prieiga**: Tikslinės teisės prieigai prie dokumentų ir veiksmų
- **Duomenų apsauga**: Duomenų šifravimas saugojimo ir perkėlimo metu jautriems dokumentams
- **Audito žurnalavimas**: Išsamus veiklos stebėjimas atitikties reikalavimams

### Našumas ir masto keitimas
- **Prisijungimų grupavimas**: Efektyvus Azure paslaugų ryšių valdymas
- **Asinchroninis apdorojimas**: Netrukdančios operacijos didelio pralaidumo scenarijams
- **Talpyklos strategijos**: Protinga talpyklų sistema dažnai naudojamiems dokumentams
- **Krovos balansavimas**: Paskirstytas apdorojimas didelio masto diegimams

### Valdymas ir stebėsena
- **Sveikatos patikrinimai**: Įmontuota RAG sistemos komponentų stebėsena
- **Našumo metrika**: Išsamios analizės apie paieškos kokybę ir atsakymų laiką
- **Klaidų valdymas**: Išsamus išimčių valdymas su pakartotinės bandymo politika
- **Konfigūracijos valdymas**: Aplinkos nustatymai su validacija

## ⚙️ Reikalavimai ir diegimas

**Kūrimo aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su Microsoft Foundry prieiga

**Būtinos NuGet paketai:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure autentifikacijos nustatymai:**
```bash
# Įdiekite Azure CLI ir autentifikuokitės
az login
az account set --subscription "your-subscription-id"
```

**Aplinkos konfigūracija:**
* Microsoft Foundry konfigūracija (automatiškai valdoma per Azure CLI)
* Įsitikinkite, kad esate autentifikuotas su teisinga Azure prenumerata

## 📊 Įmonių RAG modeliai

### Dokumentų valdymo modeliai
- **Didelis įkėlimas**: Efektyvus didelių dokumentų kolekcijų apdorojimas
- **Inkrementiniai atnaujinimai**: Realiojo laiko dokumentų pridėjimas ir keitimas
- **Versijų valdymas**: Dokumentų versijavimas ir pakeitimų sekimas
- **Metaduomenų valdymas**: Turtingi dokumentų atributai ir taksonomija

### Paieškos ir gavimo modeliai
- **Hibridinė paieška**: Semantinės ir raktažodžių paieškos derinys optimaliesiems rezultatams
- **Fasuota paieška**: Daugiamačio filtravimo ir kategorizavimo galimybės
- **Reikšmingumo derinimas**: Tinkintos vertinimo algoritmai domeno poreikiams
- **Rezultatų reitingavimas**: Pažangus reitingavimas su verslo logikos integracija

### Saugumo modeliai
- **Dokumentų lygio saugumas**: Tikslinė prieigos kontrolė kiekvienam dokumentui
- **Duomenų klasifikacija**: Automatinis jautrumo žymėjimas ir apsauga
- **Audito pėdsakai**: Išsamus visų RAG operacijų žurnalavimas
- **Privatumo apsauga**: Asmens identifikuojamos informacijos aptikimas ir pašalinimas

## 🔒 Įmonių saugumo funkcijos

### Autentifikacija ir autorizacija
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

### Duomenų apsauga
- **Šifravimas**: End-to-end šifravimas dokumentams ir paieškos indeksams
- **Prieigos kontrolė**: Azure AD integracija vartotojų ir grupių leidimams
- **Duomenų lokalizacija**: Geografinės duomenų vietos kontrolė atitikties užtikrinimui
- **Atsarginės kopijos ir atkūrimas**: Automatizuotos atsarginės kopijos ir katastrofų atkūrimo galimybės

## 📈 Našumo optimizavimas

### Asinchroninio apdorojimo modeliai
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Atminties valdymas
- **Srautinė apdorojimas**: Tvarkyti didelius dokumentus be atminties problemų
- **Išteklų grupavimas**: Efektyvus brangių išteklių pakartotinis naudojimas
- **Atminties valymas**: Optimizuoti atminties paskirstymo modeliai
- **Prisijungimų valdymas**: Tinkamas Azure paslaugų ryšių gyvavimo ciklas

### Talpyklos strategijos
- **Užklausų talpykla**: Talpyklos kūrimas dažnai vykdomoms paieškoms
- **Dokumentų talpykla**: Atminties talpykla aktyviems dokumentams
- **Indeksų talpykla**: Optimizuota vektorinės rodyklės talpykla
- **Rezultatų talpykla**: Išmanus atsakymų generavimo talpinimas

## 📊 Įmonių naudojimo scenarijai

### Žinių valdymas
- **Įmonių žinių bazė**: Intelektuali paieška per įmonės žinių bazes
- **Politikos ir procedūros**: Automatizuota atitiktis ir veiklos gairės
- **Mokymo medžiaga**: Intelektualus mokymosi ir vystymosi pagalbininkas
- **Tyrimų duomenų bazės**: Akademinių ir mokslinių darbų analizės sistemos

### Klientų palaikymas
- **Palaikymo žinių bazė**: Automatizuoti klientų aptarnavimo atsakymai
- **Produkto dokumentacija**: Intelektualus produkto informacijos gavimas
- **Trikčių šalinimo vadovai**: Kontekstinė problemų sprendimo pagalba
- **DUK sistemos**: Dinamiškas DUK generavimas iš dokumentų kolekcijų

### Reguliacinė atitiktis
- **Teisinių dokumentų analizė**: Sutarčių ir teisinių dokumentų intelektas
- **Atitikties stebėsena**: Automatizuotas reguliacinės atitikties tikrinimas
- **Rizikos vertinimas**: Dokumentais pagrįsta rizikos analizė ir ataskaitos
- **Audito palaikymas**: Intelektuali dokumentų paieška auditams

## 🚀 Gamybinis diegimas

### Stebėsena ir matomumas
- **Application Insights**: Išsami telemetrija ir našumo stebėjimas
- **Individuali metrika**: Verslo KPI sekimas ir įspėjimai
- **Paskirstytas sekimas**: Užklausų sekimas per visas paslaugas
- **Sveikatos prietaisų skydeliai**: Realiojo laiko sistemos būklės ir našumo vizualizacija

### Mastelio keitimas ir patikimumas
- **Automatinis mastelio keitimas**: Automatinis skalavimas pagal apkrovą ir našumo metrikas
- **Didelis prieinamumas**: Diegimas keliuose regionuose su gedimų perėmimo galimybėmis
- **Krovos testavimas**: Našumo validacija įmonių apkrovos sąlygomis
- **Katastrofų atkūrimas**: Automatizuoti atsarginės kopijos ir atkūrimo procesai

Pasiruošę kurti įmonių lygio RAG sistemas, kurios galėtų saugiai tvarkyti jautrius dokumentus dideliu mastu? Sukurkime intelektualias žinių sistemas verslui! 🏢📖✨

## Kodo įgyvendinimas

Pilną šios pamokos veikiančio kodo pavyzdį rasite faile `05-dotnet-agent-framework.cs`. 

Norėdami paleisti pavyzdį:

```bash
# Padarykite scenarijų vykdomą (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Paleiskite .NET vieno failo programą
./05-dotnet-agent-framework.cs
```

Arba naudokite tiesiogiai `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kodas demonstruoja:

1. **Paketo įdiegimas**: Reikalingų NuGet paketų Azure AI Agentams diegimas
2. **Aplinkos nustatymai**: Microsoft Foundry taško ir modelio nustatymų įkėlimas
3. **Dokumento įkėlimas**: Dokumento įkėlimas RAG apdorojimui
4. **Vektorinės saugyklos kūrimas**: Vektorinės saugyklos sukūrimas semantinei paieškai
5. **Agento konfigūracija**: AI agento sukūrimas su failų paieškos galimybėmis
6. **Užklausų vykdymas**: Užklausų vykdymas atsižvelgiant į įkeltą dokumentą

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->