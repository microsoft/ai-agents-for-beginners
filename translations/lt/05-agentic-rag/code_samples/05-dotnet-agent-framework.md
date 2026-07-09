# 🔍 Įmonių RAG su Microsoft Foundry (.NET)

## 📋 Mokymosi tikslai

Šiame užrašuose parodyta, kaip sukurti įmonių klasės Retrieval-Augmented Generation (RAG) sistemas naudojant Microsoft Agent Framework .NET su Microsoft Foundry. Išmoksite kurti produkcijai paruoštus agentus, kurie gali ieškoti dokumentuose ir pateikti tikslius, kontekstui pritaikytus atsakymus, užtikrinant įmonės saugumą ir mastelį.

**Įmonių RAG galimybės, kurias kursite:**
- 📚 **Dokumentų intelektas**: Pažangus dokumentų apdorojimas su Azure AI paslaugomis
- 🔍 **Semantinis paieška**: Aukšto našumo vektorinė paieška su įmonių funkcijomis
- 🛡️ **Saugumo integracija**: Pagal vaidmenis pagrįsta prieiga ir duomenų apsaugos modeliai
- 🏢 **Mastelio architektūra**: Produkcijai paruoštos RAG sistemos su stebėjimu

## 🎯 Įmonių RAG architektūra

### Pagrindinės įmonių sudedamosios dalys
- **Microsoft Foundry**: Valdoma įmonių AI platforma su saugumu ir atitiktimi
- **Nuolatiniai agentai**: Būseną išlaikantys agentai su pokalbių istorija ir konteksto valdymu
- **Vektorinės saugyklos valdymas**: Įmonių lygio dokumentų indeksavimas ir paieška
- **Tapatybės integracija**: Azure AD autentifikacija ir pagal vaidmenis pagrįsta prieigos kontrolė

### .NET įmonių privalumai
- **Tipų saugumas**: Kompiliacijos metu tikrinamos RAG operacijos ir duomenų struktūros
- **Asinchroninis našumas**: Blokavimo nesukeliantis dokumentų apdorojimas ir paieškos operacijos
- **Atminties valdymas**: Efektyvus didelių dokumentų kolekcijų išteklių naudojimas
- **Integracijos modeliai**: Natūrali Azure paslaugų integracija su priklausomybių injekcija

## 🏗️ Techninė architektūra

### Įmonių RAG kanalas
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Pagrindinės .NET sudedamosios dalys
- **Azure.AI.Agents.Persistent**: Įmonių agentų valdymas su būsenos išsaugojimu
- **Azure.Identity**: Integruota autentifikacija saugiai prieigai prie Azure paslaugų
- **Microsoft.Agents.AI.AzureAI**: Azure pritaikytos agentų sistemos įgyvendinimas
- **System.Linq.Async**: Aukšto našumo asinchroninės LINQ operacijos

## 🔧 Įmonių funkcijos ir privalumai

### Saugumas ir atitiktis
- **Azure AD integracija**: Įmonių tapatybės valdymas ir autentifikacija
- **Pagal vaidmenis pagrįsta prieiga**: Smulkiai valdomos teisės dokumentų prieigai ir operacijoms
- **Duomenų apsauga**: Šifravimas ramybėje ir perdavimo metu jautriems dokumentams
- **Auditų žurnalas**: Išsamus veiklos sekimas atitikties reikalavimams

### Našumas ir mastelį
- **Ryšių telkimas**: Efektyvus Azure paslaugų ryšių valdymas
- **Asinchroninis apdorojimas**: Blokavimo nesukeliantys veiksmai didelio pralaidumo scenarijuose
- **Talpinimo strategijos**: Išmani talpykla dažnai naudojamiems dokumentams
- **Krovio balansavimas**: Paskirstytas apdorojimas didelės apimties diegimuose

### Valdymas ir stebėjimas
- **Būklės patikrinimai**: Įmontuotas RAG sistemos komponentų stebėjimas
- **Veiklos metrika**: Išsamios analizės apie paieškos kokybę ir atsakymų laiką
- **Klaidų valdymas**: Išplėstinis išimčių tvarkymas su pakartotinių bandymų politika
- **Konfigūracijos valdymas**: Aplinkai pritaikomi nustatymai su patikra

## ⚙️ Priešpriešos ir konfigūracijos

**Kūrimo aplinka:**
- .NET 9.0 SDK ar naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su prieiga prie Microsoft Foundry

**Būtini NuGet paketai:**
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
* Įsitikinkite, kad esate prisijungę prie teisingos Azure prenumeratos

## 📊 Įmonių RAG modeliai

### Dokumentų valdymo modeliai
- **Daugiapakopis įkėlimas**: Efektyvus didelių dokumentų kolekcijų apdorojimas
- **Inkrementiniai atnaujinimai**: Realaus laiko dokumentų įtraukimas ir modifikavimas
- **Versijų valdymas**: Dokumentų versijavimo ir pakeitimų sekimas
- **Meta duomenų valdymas**: Išsamūs dokumentų atributai ir taksonomija

### Paieškos ir gavimo modeliai
- **Hibridinė paieška**: Semantinės ir raktinių žodžių paieškos derinimas optimaliai rezultatams
- **Facetuota paieška**: Daugiadimensinis filtravimas ir kategorizavimas
- **Relevancijos derinimas**: Pasirinktinių vertinimo algoritmų pritaikymas specifiniams poreikiams
- **Rezultatų reitingavimas**: Pažangus reitingavimas su verslo logikos integracija

### Saugumo modeliai
- **Dokumentų lygio saugumas**: Smulkiai valdoma prieiga prie atskirų dokumentų
- **Duomenų klasifikacija**: Automatinis jautrumo žymėjimas ir apsauga
- **Auditų takai**: Išsamus visų RAG operacijų žurnalas
- **Privatumo apsauga**: Asmens duomenų aptikimo ir slėpimo galimybės

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
- **Šifravimas**: Galutinis galutiniam šifravimas dokumentams ir paieškos indeksams
- **Prieigos valdymas**: Integracija su Azure AD vartotojų ir grupių teisėms
- **Duomenų buvimo vieta**: Geografinė duomenų vieta atitikties užtikrinimui
- **Atsarginė kopija ir atkūrimas**: Automatizuota atsarginių kopijų kūrimo ir gedimų atstatymo galimybės

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
- **Srautinio apdorojimo**: Darbas su dideliais dokumentais be atminties problemų
- **Išteklių telkimas**: Efektyvus brangių išteklių pakartotinis naudojimas
- **Atliekų surinkimas**: Optimizuoti atminties paskirstymo modeliai
- **Ryšių valdymas**: Korektinis Azure paslaugų ryšių ciklas

### Talpinimo strategijos
- **Užklausų talpyklos**: Talpinkite dažnai vykdomas paieškas
- **Dokumentų talpykla**: Atmintyje laikoma karštų dokumentų talpykla
- **Indeksų talpykla**: Optimizuota vektorinio indekso talpykla
- **Rezultatų talpykla**: Išmanus sugeneruotų atsakymų talpinimas

## 📊 Įmonių naudojimo atvejai

### Žinių valdymas
- **Įmonių žinynas**: Išmanioji paieška įmonės žinių bazėse
- **Politikos ir procedūros**: Automatizuota atitikties ir procedūrų pateikimo pagalba
- **Mokymo medžiagos**: Išmanioji mokymo ir plėtros pagalba
- **Tyrimų duomenų bazės**: Akademinių ir tyrimų straipsnių analizės sistemos

### Klientų aptarnavimas
- **Pagalbos žinių bazė**: Automatizuoti klientų aptarnavimo atsakymai
- **Produkto dokumentacija**: Išmani produkto informacijos paieška
- **Gedimų šalinimo vadovai**: Kontekstinė problemų sprendimo pagalba
- **DUK sistemos**: Dinamiškas DUK generavimas iš dokumentų rinkinų

### Reguliacinė atitiktis
- **Teisinių dokumentų analizė**: Sutarčių ir teisinių dokumentų intelektas
- **Atitikties stebėjimas**: Automatizuotas reguliacinės atitikties tikrinimas
- **Rizikos vertinimas**: Dokumentų pagrįsta rizikos analizė ir ataskaitos
- **Auditų palaikymas**: Išmani dokumentų paieška auditams

## 🚀 Produkcijos diegimas

### Stebėjimas ir matomumas
- **Application Insights**: Išsamus telemetrijos ir našumo stebėjimas
- **Vartotojiška metrika**: Verslui svarbių KPI sekimas ir įspėjimai
- **Išplėstinė sekimo sistema**: Galinių užklausų sekimas per visą paslaugų grandinę
- **Būklės valdymo skydeliai**: Realaus laiko sistemos būklės ir našumo vizualizacija

### Mastelio didinimas ir patikimumas
- **Automatinis mastelio didinimas**: Automatinis reguliavimas pagal apkrovą ir našumo metrikas
- **Aukštas prieinamumas**: Diegimas keliuose regionuose su atsarginio veikimo galimybėmis
- **Krovio testavimas**: Produkcijos apkrovos sąlygų našumo patikrinimas
- **Nelaimių atkūrimas**: Automatizuotos atsarginės kopijos ir atkūrimo procedūros

Pasiruošę kurti įmonių klasės RAG sistemas, kurios gali valdyti jautrius dokumentus dideliu mastu? Sukurkime išmanias žinių sistemas įmonėms! 🏢📖✨

## Kodo įgyvendinimas

Šio pamokos įgyvendinimo pilnas veikiantis kodo pavyzdys pateiktas faile `05-dotnet-agent-framework.cs`. 

Norėdami paleisti pavyzdį:

```bash
# Padarykite scenarijų paleidžiamu (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Paleiskite .NET vieno failo programą
./05-dotnet-agent-framework.cs
```

Arba tiesiogiai naudokite komandą `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kode parodyta:

1. **Paketų įdiegimas**: Būtini NuGet paketai Azure AI Agentams
2. **Aplinkos konfigūracija**: Microsoft Foundry galo ir modelio nustatymai
3. **Dokumento įkėlimas**: Dokumento įkėlimas RAG apdorojimui
4. **Vektorinės saugyklos kūrimas**: Vektorinės saugyklos sukūrimas semantinei paieškai
5. **Agentų konfigūracija**: AI agento nustatymas su failų paieškos galimybėmis
6. **Užklausų vykdymas**: Užklausų vykdymas prieš įkeltą dokumentą

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->