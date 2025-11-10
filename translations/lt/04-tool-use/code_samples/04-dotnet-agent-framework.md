<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:29:37+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🛠️ Pažangus Įrankių Naudojimas su GitHub Modeliais (.NET)

## 📋 Mokymosi Tikslai

Šiame užrašų knygelėje demonstruojami įmonės lygio įrankių integracijos modeliai naudojant Microsoft Agent Framework .NET aplinkoje su GitHub modeliais. Išmoksite kurti sudėtingus agentus su keliais specializuotais įrankiais, pasinaudodami C# stipriu tipavimu ir .NET įmonės funkcijomis.

**Pažangūs Įrankių Gebėjimai, Kuriuos Įvaldysite:**
- 🔧 **Daugiainstrumentinė Architektūra**: Agentų kūrimas su keliomis specializuotomis galimybėmis
- 🎯 **Tipų Saugus Įrankių Vykdymas**: Pasinaudojimas C# kompiliavimo laiko patikra
- 📊 **Įmonės Įrankių Modeliai**: Gamybai paruoštas įrankių dizainas ir klaidų valdymas
- 🔗 **Įrankių Kompozicija**: Įrankių derinimas sudėtingiems verslo procesams

## 🎯 .NET Įrankių Architektūros Privalumai

### Įmonės Įrankių Funkcijos
- **Kompiliavimo Laiko Patikra**: Stiprus tipavimas užtikrina įrankių parametrų teisingumą
- **Priklausomybių Įpurškimas**: IoC konteinerio integracija įrankių valdymui
- **Async/Await Modeliai**: Neužblokuojantis įrankių vykdymas su tinkamu resursų valdymu
- **Struktūrizuotas Logavimas**: Integruotas logavimas įrankių vykdymo stebėjimui

### Gamybai Paruošti Modeliai
- **Išimčių Valdymas**: Išsamus klaidų valdymas su tipizuotomis išimtimis
- **Resursų Valdymas**: Tinkami šalinimo modeliai ir atminties valdymas
- **Našumo Stebėjimas**: Integruoti metrikos ir našumo skaitikliai
- **Konfigūracijos Valdymas**: Tipų saugi konfigūracija su patikra

## 🔧 Techninė Architektūra

### Pagrindiniai .NET Įrankių Komponentai
- **Microsoft.Extensions.AI**: Vieninga įrankių abstrakcijos sluoksnis
- **Microsoft.Agents.AI**: Įmonės lygio įrankių orkestracija
- **GitHub Modelių Integracija**: Aukštos našumo API klientas su ryšio telkimu

### Įrankių Vykdymo Vamzdynas
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Įrankių Kategorijos ir Modeliai

### 1. **Duomenų Apdorojimo Įrankiai**
- **Įvesties Patikra**: Stiprus tipavimas su duomenų anotacijomis
- **Transformacijos Operacijos**: Tipų saugus duomenų konvertavimas ir formatavimas
- **Verslo Logika**: Specifiniai skaičiavimo ir analizės įrankiai
- **Išvesties Formatavimas**: Struktūrizuotas atsakymų generavimas

### 2. **Integracijos Įrankiai** 
- **API Jungtys**: RESTful paslaugų integracija su HttpClient
- **Duomenų Bazės Įrankiai**: Entity Framework integracija duomenų prieigai
- **Failų Operacijos**: Saugios failų sistemos operacijos su patikra
- **Išorinės Paslaugos**: Trečiųjų šalių paslaugų integracijos modeliai

### 3. **Naudingumo Įrankiai**
- **Teksto Apdorojimas**: Teksto manipuliavimo ir formatavimo įrankiai
- **Datos/Laiko Operacijos**: Kultūrai jautrūs datos/laiko skaičiavimai
- **Matematiniai Įrankiai**: Tikslūs skaičiavimai ir statistinės operacijos
- **Patikros Įrankiai**: Verslo taisyklių patikra ir duomenų tikrinimas

## ⚙️ Reikalavimai ir Nustatymai

**Kūrimo Aplinka:**
- .NET 9.0 SDK ar naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- GitHub Modelių API prieiga

**Reikalingi NuGet Paketai:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Aplinkos Konfigūracija (.env failas):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Pasiruošę kurti įmonės lygio agentus su galingomis, tipų saugiomis įrankių galimybėmis .NET aplinkoje? Sukurkime profesionalaus lygio sprendimus! 🏢⚡

## 💻 Kodo Įgyvendinimas

Pilnas C# įgyvendinimas pateiktas pridedamame faile `04-dotnet-agent-framework.cs`. Ši .NET vieno failo programa demonstruoja:

- Aplinkos kintamųjų įkrovimą GitHub Modelių konfigūracijai
- Individualių įrankių apibrėžimą naudojant C# metodus su atributais
- AI agento kūrimą su įrankių integracija
- Pokalbių gijų valdymą
- Agentų užklausų vykdymą su įrankių iškvietimu

Norėdami paleisti pavyzdį:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Arba naudojant .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.