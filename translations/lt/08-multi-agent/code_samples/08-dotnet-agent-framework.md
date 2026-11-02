# 🤝 Įmonių daugiaagentės darbo eigos sistemos (.NET)

## 📋 Mokymosi tikslai

Šiame užraše parodyta, kaip sukurti pažangias įmonėms skirtas daugiaagentės sistemas, naudojant Microsoft Agent Framework .NET aplinkoje kartu su Azure OpenAI (Responses API). Išmoksite organizuoti kelis specializuotus agentus, veikiančius kartu struktūrizuotose darbo eigos srautose, pasinaudodami .NET įmoninėmis funkcijomis kuriant gamybinio lygio sprendimus.

**Įmonių daugiaagentės galimybės, kurias išmoksite kurti:**
- 👥 **Agentų bendradarbiavimas**: Tipiškai saugi agentų koordinacija su kompiliavimo metu atliekama tikrinimu
- 🔄 **Darbo eigos srauto valdymas**: Deklaratyvus darbo eigos apibrėžimas naudojant .NET asinchroninius šablonus
- 🎭 **Rolės specializacija**: Griežtai tipizuotos agentų asmenybės ir ekspertų sritys
- 🏢 **Įmonių integracija**: Gamybiniai šablonai su stebėsena ir klaidų valdymu

## ⚙️ Reikalavimai ir įrengimas

**Vystymo aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata (nuolatiniams agentams)

**Reikalingos NuGet bibliotekos:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Kodo pavyzdys

Pilnas veikiančio kodo pavyzdys pateiktas kartu su C# failu: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Norėdami paleisti pavyzdį:

```bash
# Padarykite failą vykdomu (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Vykdyti pavyzdį
./08-dotnet-agent-framework.cs
```

Arba naudodami .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ką šis pavyzdys iliustruoja

Ši daugiaagentė darbo eigos sistema sukuria viešbučio kelionių rekomendacijų paslaugą su dviem specializuotais agentais:

1. **FrontDesk agentas**: kelionių agentas, teikiantis pasiūlymus apie užsiėmimus ir vietas
2. **Concierge agentas**: peržiūri rekomendacijas, užtikrindamas autentiškas, ne turistines patirtis

Agentai bendradarbiauja darbo eigoje, kur:
- FrontDesk agentas gauna pradinį kelionės užklausimą
- Concierge agentas peržiūri ir patobulina rekomendaciją
- Darbo eiga tiesiogiai transliuoja atsakymus realiuoju laiku

## Pagrindinės sąvokos

### Agentų koordinavimas
Pavyzdyje demonstruojama tipiškai saugi agentų koordinacija naudojant Microsoft Agent Framework ir kompiliavimo metu atliekamą tikrinimą.

### Darbo eigos valdymas
Naudojamas deklaratyvus darbo eigos apibrėžimas su .NET asinchroniniais šablonais, jungiant kelis agentus į srautą.

### Atsakymų transliacija
Įgyvendina agentų atsakymų realaus laiko transliaciją naudojant asinchroninius skaitinius ir įvykių pagrindu veikiančią architektūrą.

### Įmonių integracija
Parodo gamybinius šablonus, tokius kaip:
- Aplinkos kintamųjų konfigūracija
- Saugus įgaliojimų valdymas
- Klaidų valdymas
- Asinchroninis įvykių apdorojimas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->