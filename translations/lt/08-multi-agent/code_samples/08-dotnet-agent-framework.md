<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:19:52+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🤝 Įmonių daugiaveiksnių darbo eigos sistemos (.NET)

## 📋 Mokymosi tikslai

Šiame užrašų knygelėje parodoma, kaip sukurti sudėtingas įmonių lygio daugiaveiksnių sistemas naudojant Microsoft Agent Framework .NET ir GitHub modelius. Išmoksite koordinuoti kelių specializuotų agentų darbą per struktūrizuotas darbo eigas, pasinaudodami .NET įmonių funkcijomis, kad sukurtumėte sprendimus, paruoštus gamybai.

**Įmonių daugiaveiksnių galimybės, kurias sukursite:**
- 👥 **Agentų bendradarbiavimas**: Tipų saugi agentų koordinacija su kompiliavimo laiko patvirtinimu
- 🔄 **Darbo eigos orkestracija**: Deklaratyvus darbo eigos apibrėžimas naudojant .NET asinchroninius modelius
- 🎭 **Rolės specializacija**: Stipriai tipizuotos agentų asmenybės ir ekspertizės sritys
- 🏢 **Įmonių integracija**: Gamybai paruošti modeliai su stebėjimu ir klaidų tvarkymu

## ⚙️ Reikalavimai ir nustatymas

**Kūrimo aplinka:**
- .NET 9.0 SDK ar naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata (nuolatiniams agentams)

**Reikalingos NuGet paketai:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Kodo pavyzdys

Visas veikiančio kodo pavyzdys pateiktas pridedamame C# faile: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Norėdami paleisti pavyzdį:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Arba naudojant .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ką demonstruoja šis pavyzdys

Ši daugiaveiksnių darbo eigos sistema sukuria viešbučio kelionių rekomendacijų paslaugą su dviem specializuotais agentais:

1. **FrontDesk Agentas**: Kelionių agentas, teikiantis veiklos ir vietos rekomendacijas
2. **Concierge Agentas**: Peržiūri rekomendacijas, kad užtikrintų autentiškas, ne turistines patirtis

Agentai dirba kartu darbo eigoje, kur:
- FrontDesk agentas gauna pradinį kelionės prašymą
- Concierge agentas peržiūri ir patobulina rekomendaciją
- Darbo eiga realiu laiku transliuoja atsakymus

## Pagrindinės sąvokos

### Agentų koordinacija
Pavyzdyje demonstruojama tipų saugi agentų koordinacija naudojant Microsoft Agent Framework su kompiliavimo laiko patvirtinimu.

### Darbo eigos orkestracija
Naudojamas deklaratyvus darbo eigos apibrėžimas su .NET asinchroniniais modeliais, siekiant sujungti kelis agentus į vieną procesą.

### Atsakymų transliavimas
Įgyvendinamas realaus laiko agentų atsakymų transliavimas naudojant asinchroninius išvardijimus ir įvykių valdomą architektūrą.

### Įmonių integracija
Parodomi gamybai paruošti modeliai, įskaitant:
- Konfigūraciją naudojant aplinkos kintamuosius
- Saugų kredencialų valdymą
- Klaidų tvarkymą
- Asinchroninį įvykių apdorojimą

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.