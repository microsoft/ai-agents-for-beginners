<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:53:12+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🎨 Agentiniai dizaino šablonai su GitHub modeliais (.NET)

## 📋 Mokymosi tikslai

Šiame užrašų knygelėje pateikiami įmonės lygio dizaino šablonai, skirti kurti intelektualius agentus naudojant Microsoft Agent Framework .NET aplinkoje su GitHub modelių integracija. Sužinosite profesionalius šablonus ir architektūrinius metodus, kurie padaro agentus paruoštus gamybai, lengvai prižiūrimus ir plečiamus.

**Įmonės dizaino šablonai:**
- 🏭 **Gamyklos šablonas**: Standartizuotas agentų kūrimas su priklausomybių injekcija
- 🔧 **Kūrėjo šablonas**: Sklandus agentų konfigūravimas ir nustatymas
- 🧵 **Siūlų saugumo šablonai**: Lygiagretus pokalbių valdymas
- 📋 **Saugyklos šablonas**: Tvarkingas įrankių ir galimybių valdymas

## 🎯 .NET specifiniai architektūriniai privalumai

### Įmonės funkcijos
- **Stiprus tipavimas**: Patikra kompiliavimo metu ir IntelliSense palaikymas
- **Priklausomybių injekcija**: Integruotas DI konteineris
- **Konfigūracijos valdymas**: IConfiguration ir Options šablonai
- **Async/Await**: Pirmo lygio asinchroninio programavimo palaikymas

### Paruošti gamybai šablonai
- **Žurnalų integracija**: ILogger ir struktūrizuoto žurnalų palaikymas
- **Sveikatos patikrinimai**: Integruotas stebėjimas ir diagnostika
- **Konfigūracijos patikra**: Stiprus tipavimas su duomenų anotacijomis
- **Klaidų valdymas**: Struktūrizuotas išimčių valdymas

## 🔧 Techninė architektūra

### Pagrindiniai .NET komponentai
- **Microsoft.Extensions.AI**: Vieninga AI paslaugų abstrakcija
- **Microsoft.Agents.AI**: Įmonės agentų orkestravimo sistema
- **GitHub modelių integracija**: Aukštos kokybės API klientų šablonai
- **Konfigūracijos sistema**: appsettings.json ir aplinkos integracija

### Dizaino šablonų įgyvendinimas
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonstruoti įmonės šablonai

### 1. **Kūrimo šablonai**
- **Agentų gamykla**: Centralizuotas agentų kūrimas su nuoseklia konfigūracija
- **Kūrėjo šablonas**: Sklandus API sudėtingam agentų konfigūravimui
- **Singleton šablonas**: Bendrų išteklių ir konfigūracijos valdymas
- **Priklausomybių injekcija**: Laisvas susiejimas ir testavimas

### 2. **Elgsenos šablonai**
- **Strategijos šablonas**: Keičiamų įrankių vykdymo strategijos
- **Komandos šablonas**: Inkapsuliuotos agentų operacijos su atšaukimu/atstatymu
- **Stebėtojo šablonas**: Įvykių pagrindu veikiantis agentų gyvavimo ciklo valdymas
- **Šabloninis metodas**: Standartizuoti agentų vykdymo darbo srautai

### 3. **Struktūriniai šablonai**
- **Adapterio šablonas**: GitHub modelių API integracijos sluoksnis
- **Dekoratoriaus šablonas**: Agentų galimybių plėtra
- **Fasado šablonas**: Supaprastintos agentų sąsajos
- **Proxy šablonas**: Lėtas įkrovimas ir talpyklos naudojimas našumui

## ⚙️ Reikalavimai ir nustatymas

**Kūrimo aplinka:**
- .NET 9.0 SDK ar naujesnė
- Visual Studio 2022 arba VS Code su C# plėtiniu
- GitHub modelių API prieiga

**NuGet priklausomybės:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigūracija (.env failas):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET dizaino principai

### SOLID principai
- **Vienos atsakomybės**: Kiekvienas komponentas turi aiškų tikslą
- **Atviras/Uždarytas**: Plečiamas be modifikacijų
- **Liskovo pakeitimas**: Įrankių įgyvendinimas pagal sąsajas
- **Sąsajos segregacija**: Koncentruotos, darnios sąsajos
- **Priklausomybių inversija**: Priklausomybė nuo abstrakcijų, o ne konkrečių įgyvendinimų

### Švari architektūra
- **Domeno sluoksnis**: Pagrindinės agentų ir įrankių abstrakcijos
- **Programos sluoksnis**: Agentų orkestracija ir darbo srautai
- **Infrastruktūros sluoksnis**: GitHub modelių integracija ir išorinės paslaugos
- **Pateikimo sluoksnis**: Vartotojo sąveika ir atsakymų formatavimas

## 🔒 Įmonės svarstymai

### Saugumas
- **Kredencialų valdymas**: Saugus API raktų tvarkymas su IConfiguration
- **Įvesties patikra**: Stiprus tipavimas ir duomenų anotacijų patikra
- **Išvesties valymas**: Saugus atsakymų apdorojimas ir filtravimas
- **Audito žurnalai**: Išsamus operacijų stebėjimas

### Našumas
- **Asinchroniniai šablonai**: Neužblokuojančios I/O operacijos
- **Jungčių telkinys**: Efektyvus HTTP klientų valdymas
- **Talpyklos naudojimas**: Atsakymų talpyklos našumo gerinimui
- **Išteklių valdymas**: Tinkamas išteklių atlaisvinimas ir valymas

### Skalavimas
- **Siūlų saugumas**: Lygiagretus agentų vykdymo palaikymas
- **Išteklių telkinys**: Efektyvus išteklių naudojimas
- **Krovos valdymas**: Greičio ribojimas ir spaudimo valdymas
- **Stebėjimas**: Našumo metrikos ir sveikatos patikrinimai

## 🚀 Gamybinis diegimas

- **Konfigūracijos valdymas**: Aplinkai specifiniai nustatymai
- **Žurnalų strategija**: Struktūrizuoti žurnalai su koreliacijos ID
- **Klaidų valdymas**: Bendras išimčių valdymas su tinkamu atkūrimu
- **Stebėjimas**: Programos įžvalgos ir našumo skaitikliai
- **Testavimas**: Vienetų testai, integracijos testai ir apkrovos testavimo šablonai

Pasiruošę kurti įmonės lygio intelektualius agentus su .NET? Sukurkime kažką tvirto! 🏢✨

## Kodo pavyzdys

Visą veikiančio pavyzdžio kodą rasite [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.