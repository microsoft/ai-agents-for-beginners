<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:27:12+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🛠️ Matumizi ya Zana za Juu na Miundo ya GitHub (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inaonyesha mifumo ya ujumuishaji wa zana za kiwango cha biashara kwa kutumia Microsoft Agent Framework katika .NET na Miundo ya GitHub. Utajifunza jinsi ya kujenga mawakala wa hali ya juu wenye zana nyingi maalum, ukitumia nguvu ya C# na vipengele vya biashara vya .NET.

**Uwezo wa Zana za Juu Utakaomasteri:**
- 🔧 **Usanifu wa Zana Nyingi**: Kujenga mawakala wenye uwezo maalum mbalimbali
- 🎯 **Utekelezaji wa Zana Salama kwa Aina**: Kutumia uthibitishaji wa wakati wa kuandaa wa C#
- 📊 **Mifumo ya Zana za Biashara**: Ubunifu wa zana tayari kwa uzalishaji na usimamizi wa makosa
- 🔗 **Muundo wa Zana**: Kuchanganya zana kwa mtiririko wa kazi za biashara ngumu

## 🎯 Faida za Usanifu wa Zana za .NET

### Vipengele vya Zana za Biashara
- **Uthibitishaji wa Wakati wa Kuandaa**: Uandishi wenye nguvu unahakikisha usahihi wa vigezo vya zana
- **Uingizaji wa Utegemezi**: Ujumuishaji wa kontena la IoC kwa usimamizi wa zana
- **Mifumo ya Async/Await**: Utekelezaji wa zana bila kuzuia na usimamizi sahihi wa rasilimali
- **Kumbukumbu Iliyopangiliwa**: Ujumuishaji wa kumbukumbu kwa ufuatiliaji wa utekelezaji wa zana

### Mifumo Tayari kwa Uzalishaji
- **Usimamizi wa Makosa**: Usimamizi wa makosa wa kina na makosa yaliyoainishwa
- **Usimamizi wa Rasilimali**: Mifumo sahihi ya utupaji na usimamizi wa kumbukumbu
- **Ufuatiliaji wa Utendaji**: Vipimo vilivyojengwa ndani na kaunta za utendaji
- **Usimamizi wa Usanidi**: Usanidi salama kwa aina na uthibitishaji

## 🔧 Usanifu wa Kiufundi

### Vipengele vya Msingi vya Zana za .NET
- **Microsoft.Extensions.AI**: Tabaka la muhtasari wa zana lililounganishwa
- **Microsoft.Agents.AI**: Usanifu wa zana wa kiwango cha biashara
- **Ujumuishaji wa Miundo ya GitHub**: Mteja wa API wa utendaji wa juu na upunguzaji wa muunganisho

### Njia ya Utekelezaji wa Zana
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Aina za Zana & Mifumo

### 1. **Zana za Usindikaji wa Data**
- **Uthibitishaji wa Ingizo**: Uandishi wenye nguvu na maelezo ya data
- **Operesheni za Ubadilishaji**: Ubadilishaji wa data salama kwa aina na uundaji
- **Mantiki ya Biashara**: Zana za hesabu maalum za kikoa na uchambuzi
- **Uundaji wa Matokeo**: Uzalishaji wa majibu yaliyopangiliwa

### 2. **Zana za Ujumuishaji**
- **Viunganishi vya API**: Ujumuishaji wa huduma za RESTful na HttpClient
- **Zana za Hifadhidata**: Ujumuishaji wa Entity Framework kwa ufikiaji wa data
- **Operesheni za Faili**: Operesheni salama za mfumo wa faili na uthibitishaji
- **Huduma za Nje**: Mifumo ya ujumuishaji wa huduma za watu wengine

### 3. **Zana za Kazi**
- **Usindikaji wa Maandishi**: Manipulasi ya maandishi na zana za uundaji
- **Operesheni za Tarehe/Muda**: Hesabu za tarehe/muda zinazojali utamaduni
- **Zana za Hisabati**: Hesabu za usahihi na operesheni za takwimu
- **Zana za Uthibitishaji**: Uthibitishaji wa sheria za biashara na uhakiki wa data

## ⚙️ Mahitaji & Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#
- Ufikiaji wa API ya Miundo ya GitHub

**Pakiti za NuGet Zinazohitajika:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Mazingira (faili ya .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Uko tayari kujenga mawakala wa kiwango cha biashara wenye uwezo wa zana salama kwa aina katika .NET? Hebu tuunde suluhisho za kiwango cha kitaalamu! 🏢⚡

## 💻 Utekelezaji wa Msimbo

Utekelezaji kamili wa C# unapatikana katika faili ya kuandamana `04-dotnet-agent-framework.cs`. Programu hii ya Faili Moja ya .NET inaonyesha:

- Kupakia vigezo vya mazingira kwa usanidi wa Miundo ya GitHub
- Kufafanua zana maalum kwa kutumia mbinu za C# na sifa
- Kuunda wakala wa AI na ujumuishaji wa zana
- Kusimamia nyuzi za mazungumzo
- Kutekeleza maombi ya wakala na mwito wa zana

Ili kuendesha mfano:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Au kwa kutumia .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.