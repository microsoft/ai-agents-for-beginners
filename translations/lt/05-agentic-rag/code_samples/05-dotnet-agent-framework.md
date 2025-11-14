<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:11:43+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🔍 Įmonės RAG su Azure AI Foundry (.NET)

## 📋 Mokymosi tikslai

Šiame užrašų knygelėje parodoma, kaip sukurti įmonės lygio Retrieval-Augmented Generation (RAG) sistemas naudojant Microsoft Agent Framework .NET su Azure AI Foundry. Išmoksite kurti gamybai paruoštus agentus, kurie gali ieškoti dokumentuose ir pateikti tikslius, kontekstinius atsakymus su įmonės saugumu ir mastelio keitimu.

**Įmonės RAG galimybės, kurias sukursite:**
- 📚 **Dokumentų intelektas**: Pažangus dokumentų apdorojimas su Azure AI paslaugomis
- 🔍 **Semantinė paieška**: Aukštos kokybės vektorinė paieška su įmonės funkcijomis
- 🛡️ **Saugumo integracija**: Prieigos kontrolė pagal vaidmenis ir duomenų apsaugos modeliai
- 🏢 **Mastelio keitimo architektūra**: Gamybai paruoštos RAG sistemos su stebėjimu

## 🎯 Įmonės RAG architektūra

### Pagrindiniai įmonės komponentai
- **Azure AI Foundry**: Valdoma įmonės AI platforma su saugumu ir atitiktimi
- **Nuolatiniai agentai**: Agentai su pokalbių istorija ir konteksto valdymu
- **Vektorinės saugyklos valdymas**: Įmonės lygio dokumentų indeksavimas ir paieška
- **Tapatybės integracija**: Azure AD autentifikacija ir prieigos kontrolė pagal vaidmenis

### .NET įmonės privalumai
- **Tipų saugumas**: Kompiliavimo metu tikrinamos RAG operacijos ir duomenų struktūros
- **Asinchroninis našumas**: Neužblokuojantis dokumentų apdorojimas ir paieškos operacijos
- **Atminties valdymas**: Efektyvus išteklių naudojimas dideliems dokumentų rinkiniams
- **Integracijos modeliai**: Natūrali Azure paslaugų integracija su priklausomybių injekcija

## 🏗️ Techninė architektūra

### Įmonės RAG procesas
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Pagrindiniai .NET komponentai
- **Azure.AI.Agents.Persistent**: Įmonės agentų valdymas su būsenos išsaugojimu
- **Azure.Identity**: Integruota autentifikacija saugiam Azure paslaugų naudojimui
- **Microsoft.Agents.AI.AzureAI**: Optimizuotas Azure agentų sistemos įgyvendinimas
- **System.Linq.Async**: Aukštos kokybės asinchroninės LINQ operacijos

## 🔧 Įmonės funkcijos ir privalumai

### Saugumas ir atitiktis
- **Azure AD integracija**: Įmonės tapatybės valdymas ir autentifikacija
- **Prieiga pagal vaidmenis**: Detali leidimų kontrolė dokumentų prieigai ir operacijoms
- **Duomenų apsauga**: Šifravimas saugojimo metu ir perduodant jautrius dokumentus
- **Audito žurnalai**: Išsamus veiklos stebėjimas atitikties reikalavimams

### Našumas ir mastelio keitimas
- **Jungčių telkiniai**: Efektyvus Azure paslaugų jungčių valdymas
- **Asinchroninis apdorojimas**: Neužblokuojančios operacijos didelio našumo scenarijams
- **Talpyklos strategijos**: Protingas dažnai pasiekiamų dokumentų talpyklavimas
- **Krovos balansavimas**: Paskirstytas apdorojimas didelio masto diegimams

### Valdymas ir stebėjimas
- **Sveikatos patikrinimai**: Įmontuotas RAG sistemos komponentų stebėjimas
- **Našumo metrika**: Išsami paieškos kokybės ir atsako laiko analizė
- **Klaidų valdymas**: Išsamus išimčių valdymas su pakartojimo politikomis
- **Konfigūracijos valdymas**: Aplinkai pritaikyti nustatymai su validacija

## ⚙️ Reikalavimai ir nustatymai

**Kūrimo aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su AI Foundry prieiga

**Reikalingi NuGet paketai:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure autentifikacijos nustatymai:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Aplinkos konfigūracija:**
* Azure AI Foundry konfigūracija (automatiškai tvarkoma per Azure CLI)
* Įsitikinkite, kad esate autentifikuotas tinkamoje Azure prenumeratoje

## 📊 Įmonės RAG modeliai

### Dokumentų valdymo modeliai
- **Masinis įkėlimas**: Efektyvus didelių dokumentų rinkinių apdorojimas
- **Inkrementiniai atnaujinimai**: Dokumentų pridėjimas ir keitimas realiu laiku
- **Versijų kontrolė**: Dokumentų versijų valdymas ir pakeitimų stebėjimas
- **Metaduomenų valdymas**: Turtingi dokumentų atributai ir taksonomija

### Paieškos ir gavimo modeliai
- **Hibridinė paieška**: Semantinės ir raktažodžių paieškos derinimas optimaliems rezultatams
- **Fasuota paieška**: Daugiamatė filtracija ir kategorijų nustatymas
- **Relevancijos derinimas**: Individualizuoti vertinimo algoritmai specifiniams poreikiams
- **Rezultatų reitingavimas**: Pažangus reitingavimas su verslo logikos integracija

### Saugumo modeliai
- **Dokumentų lygio saugumas**: Detali prieigos kontrolė kiekvienam dokumentui
- **Duomenų klasifikacija**: Automatinis jautrumo žymėjimas ir apsauga
- **Audito pėdsakai**: Išsamus visų RAG operacijų žurnalavimas
- **Privatumo apsauga**: PII aptikimas ir redagavimas

## 🔒 Įmonės saugumo funkcijos

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
- **Šifravimas**: Pilnas dokumentų ir paieškos indeksų šifravimas
- **Prieigos kontrolė**: Integracija su Azure AD vartotojų ir grupių leidimams
- **Duomenų buvimo vieta**: Geografinė duomenų vietos kontrolė atitikties reikalavimams
- **Atsarginės kopijos ir atkūrimas**: Automatinės atsarginės kopijos ir atkūrimo galimybės

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
- **Srautinio apdorojimo**: Didelių dokumentų apdorojimas be atminties problemų
- **Išteklių telkiniai**: Efektyvus brangių išteklių pakartotinis naudojimas
- **Šiukšlių surinkimas**: Optimizuoti atminties paskirstymo modeliai
- **Jungčių valdymas**: Tinkamas Azure paslaugų jungčių gyvavimo ciklas

### Talpyklos strategijos
- **Užklausų talpyklavimas**: Dažnai vykdomų paieškų talpyklavimas
- **Dokumentų talpyklavimas**: Atminties talpyklavimas populiariems dokumentams
- **Indeksų talpyklavimas**: Optimizuotas vektorinių indeksų talpyklavimas
- **Rezultatų talpyklavimas**: Protingas sugeneruotų atsakymų talpyklavimas

## 📊 Įmonės naudojimo atvejai

### Žinių valdymas
- **Įmonės wiki**: Išmanioji paieška per įmonės žinių bazes
- **Politikos ir procedūros**: Automatinė atitikties ir procedūrų pagalba
- **Mokymo medžiaga**: Išmanioji mokymosi ir tobulėjimo pagalba
- **Tyrimų duomenų bazės**: Akademinių ir mokslinių straipsnių analizės sistemos

### Klientų aptarnavimas
- **Pagalbos žinių bazė**: Automatiniai klientų aptarnavimo atsakymai
- **Produkto dokumentacija**: Išmanioji produkto informacijos paieška
- **Trikčių šalinimo vadovai**: Kontekstinė problemų sprendimo pagalba
- **DUK sistemos**: Dinaminis DUK generavimas iš dokumentų rinkinių

### Reguliavimo atitiktis
- **Teisinių dokumentų analizė**: Sutarčių ir teisinių dokumentų intelektas
- **Atitikties stebėjimas**: Automatinis reguliavimo atitikties tikrinimas
- **Rizikos vertinimas**: Dokumentais pagrįsta rizikos analizė ir ataskaitos
- **Audito pagalba**: Išmanioji dokumentų paieška auditams

## 🚀 Gamybos diegimas

### Stebėjimas ir stebimumas
- **Application Insights**: Išsami telemetrija ir našumo stebėjimas
- **Individuali metrika**: Verslo specifinių KPI stebėjimas ir įspėjimai
- **Paskirstytas sekimas**: Pilnas užklausų sekimas per paslaugas
- **Sveikatos skydeliai**: Realaus laiko sistemos sveikatos ir našumo vizualizacija

### Mastelio keitimas ir patikimumas
- **Automatinis mastelio keitimas**: Automatinis mastelio keitimas pagal apkrovą ir našumo metriką
- **Didelis prieinamumas**: Daugiaregioninis diegimas su perjungimo galimybėmis
- **Krovos testavimas**: Našumo patvirtinimas esant įmonės apkrovai
- **Avarinis atkūrimas**: Automatinės atsarginės kopijos ir atkūrimo procedūros

Pasiruošę kurti įmonės lygio RAG sistemas, kurios gali tvarkyti jautrius dokumentus dideliu mastu? Sukurkime išmaniąsias žinių sistemas įmonei! 🏢📖✨

## Kodo įgyvendinimas

Pilnas veikiančio kodo pavyzdys šiai pamokai yra `05-dotnet-agent-framework.cs`.

Norėdami paleisti pavyzdį:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Arba naudokite `dotnet run` tiesiogiai:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kodas demonstruoja:

1. **Paketų diegimas**: Reikalingų NuGet paketų diegimas Azure AI agentams
2. **Aplinkos konfigūracija**: Azure AI Foundry galinių taškų ir modelio nustatymų įkėlimas
3. **Dokumentų įkėlimas**: Dokumento įkėlimas RAG apdorojimui
4. **Vektorinės saugyklos kūrimas**: Vektorinės saugyklos kūrimas semantinei paieškai
5. **Agentų konfigūracija**: AI agento nustatymas su failų paieškos galimybėmis
6. **Užklausų vykdymas**: Užklausų vykdymas prieš įkeltą dokumentą

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.