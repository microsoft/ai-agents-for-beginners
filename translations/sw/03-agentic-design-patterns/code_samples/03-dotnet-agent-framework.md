<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:50:19+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🎨 Miundo ya Ubunifu wa Wakala kwa kutumia GitHub Models (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inaonyesha miundo ya ubunifu ya kiwango cha biashara kwa ajili ya kujenga mawakala wenye akili kwa kutumia Microsoft Agent Framework katika .NET na ujumuishaji wa GitHub Models. Utajifunza miundo ya kitaalamu na mbinu za usanifu zinazofanya mawakala kuwa tayari kwa uzalishaji, rahisi kudumisha, na kupanuka.

**Miundo ya Ubunifu ya Biashara:**
- 🏭 **Factory Pattern**: Uundaji wa wakala uliosanifishwa kwa kutumia dependency injection
- 🔧 **Builder Pattern**: Usanidi wa wakala kwa njia ya fluent
- 🧵 **Thread-Safe Patterns**: Usimamizi wa mazungumzo ya wakati mmoja
- 📋 **Repository Pattern**: Usimamizi wa zana na uwezo ulioandaliwa

## 🎯 Faida za Usanifu wa .NET

### Vipengele vya Biashara
- **Strong Typing**: Uthibitishaji wa wakati wa kuandaa na msaada wa IntelliSense
- **Dependency Injection**: Ujumuishaji wa kontena la DI lililojengwa ndani
- **Configuration Management**: Mifumo ya IConfiguration na Options
- **Async/Await**: Msaada wa programu ya asynchronous ya daraja la kwanza

### Miundo Tayari kwa Uzalishaji
- **Logging Integration**: Msaada wa ILogger na logging iliyoundwa
- **Health Checks**: Ufuatiliaji na uchunguzi uliojengwa ndani
- **Configuration Validation**: Strong typing na annotations za data
- **Error Handling**: Usimamizi wa makosa ulioandaliwa

## 🔧 Usanifu wa Kiufundi

### Vipengele vya Msingi vya .NET
- **Microsoft.Extensions.AI**: Abstractions za huduma za AI zilizounganishwa
- **Microsoft.Agents.AI**: Mfumo wa uratibu wa wakala wa biashara
- **GitHub Models Integration**: Miundo ya mteja wa API yenye utendaji wa juu
- **Configuration System**: Ujumuishaji wa appsettings.json na mazingira

### Utekelezaji wa Miundo ya Ubunifu
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Miundo ya Biashara Iliyodhihirishwa

### 1. **Miundo ya Uundaji**
- **Agent Factory**: Uundaji wa wakala ulio katikati na usanidi thabiti
- **Builder Pattern**: API ya fluent kwa usanidi wa wakala wa hali ngumu
- **Singleton Pattern**: Usimamizi wa rasilimali na usanidi wa pamoja
- **Dependency Injection**: Uunganishaji usio wa moja kwa moja na uwezo wa kupimwa

### 2. **Miundo ya Tabia**
- **Strategy Pattern**: Mikakati ya utekelezaji wa zana inayoweza kubadilishwa
- **Command Pattern**: Operesheni za wakala zilizofungwa na undo/redo
- **Observer Pattern**: Usimamizi wa mzunguko wa maisha wa wakala unaoendeshwa na matukio
- **Template Method**: Mifumo ya utekelezaji wa wakala iliyosanifishwa

### 3. **Miundo ya Kimuundo**
- **Adapter Pattern**: Tabaka la ujumuishaji wa API ya GitHub Models
- **Decorator Pattern**: Uboreshaji wa uwezo wa wakala
- **Facade Pattern**: Mienendo rahisi ya mwingiliano wa wakala
- **Proxy Pattern**: Upakiaji wa polepole na caching kwa utendaji

## ⚙️ Mahitaji ya Awali na Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na extension ya C#
- Ufikiaji wa API ya GitHub Models

**Dependencies za NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Kanuni za Ubunifu wa .NET

### Kanuni za SOLID
- **Single Responsibility**: Kila kipengele kina kusudi moja wazi
- **Open/Closed**: Kinapanuka bila mabadiliko
- **Liskov Substitution**: Utekelezaji wa zana unaotegemea interface
- **Interface Segregation**: Interfaces zilizoelekezwa na zenye mshikamano
- **Dependency Inversion**: Kutegemea abstractions, si concretions

### Usanifu Safi
- **Domain Layer**: Abstractions za msingi za wakala na zana
- **Application Layer**: Uratibu wa wakala na workflows
- **Infrastructure Layer**: Ujumuishaji wa GitHub Models na huduma za nje
- **Presentation Layer**: Mwingiliano wa mtumiaji na muundo wa majibu

## 🔒 Mazingatio ya Biashara

### Usalama
- **Credential Management**: Ushughulikiaji salama wa funguo za API kwa kutumia IConfiguration
- **Input Validation**: Strong typing na uthibitishaji wa annotations za data
- **Output Sanitization**: Usindikaji salama wa majibu na uchujaji
- **Audit Logging**: Ufuatiliaji wa operesheni kwa kina

### Utendaji
- **Async Patterns**: Operesheni za I/O zisizo na vizuizi
- **Connection Pooling**: Usimamizi mzuri wa mteja wa HTTP
- **Caching**: Caching ya majibu kwa utendaji bora
- **Resource Management**: Mifumo sahihi ya usafishaji na utupaji

### Uwezo wa Kupanuka
- **Thread Safety**: Msaada wa utekelezaji wa wakala wa wakati mmoja
- **Resource Pooling**: Matumizi bora ya rasilimali
- **Load Management**: Kuweka mipaka ya kiwango na kushughulikia shinikizo
- **Monitoring**: Vipimo vya utendaji na ukaguzi wa afya

## 🚀 Utekelezaji wa Uzalishaji

- **Configuration Management**: Usanidi maalum wa mazingira
- **Logging Strategy**: Logging iliyoundwa na vitambulisho vya uhusiano
- **Error Handling**: Ushughulikiaji wa makosa ya kimataifa na urejeshaji sahihi
- **Monitoring**: Uelewa wa programu na counters za utendaji
- **Testing**: Mifumo ya majaribio ya kitengo, ujumuishaji, na mzigo

Uko tayari kujenga mawakala wenye akili wa kiwango cha biashara kwa kutumia .NET? Hebu tusanifu kitu imara! 🏢✨

## Mfano wa Msimbo

Kwa mfano kamili unaofanya kazi, angalia [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.