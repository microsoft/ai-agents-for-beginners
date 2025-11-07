<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:07:17+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🔍 RAG ya Biashara na Azure AI Foundry (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inaonyesha jinsi ya kujenga mifumo ya Retrieval-Augmented Generation (RAG) ya kiwango cha biashara kwa kutumia Microsoft Agent Framework katika .NET na Azure AI Foundry. Utajifunza kuunda mawakala wa kiwango cha uzalishaji wanaoweza kutafuta kupitia nyaraka na kutoa majibu sahihi, yenye muktadha, huku wakizingatia usalama na upanuzi wa biashara.

**Uwezo wa RAG ya Biashara Utakaounda:**
- 📚 **Ujasusi wa Nyaraka**: Usindikaji wa nyaraka wa hali ya juu kwa huduma za Azure AI
- 🔍 **Utafutaji wa Semantiki**: Utafutaji wa vector wa utendaji wa juu na vipengele vya biashara
- 🛡️ **Ujumuishaji wa Usalama**: Udhibiti wa ufikiaji kulingana na majukumu na mifumo ya ulinzi wa data
- 🏢 **Usanifu Unaoweza Kupanuka**: Mifumo ya RAG ya kiwango cha uzalishaji yenye ufuatiliaji

## 🎯 Usanifu wa RAG ya Biashara

### Vipengele Vikuu vya Biashara
- **Azure AI Foundry**: Jukwaa la AI la biashara linalosimamiwa na usalama na uzingatiaji
- **Mawakala wa Kudumu**: Mawakala wenye hali ya mazungumzo na usimamizi wa muktadha
- **Usimamizi wa Duka la Vector**: Uorodheshaji wa nyaraka za kiwango cha biashara na urejeshaji
- **Ujumuishaji wa Utambulisho**: Uthibitishaji wa Azure AD na udhibiti wa ufikiaji kulingana na majukumu

### Faida za Biashara za .NET
- **Usalama wa Aina**: Uthibitishaji wa wakati wa kuunganisha kwa operesheni za RAG na miundo ya data
- **Utendaji wa Async**: Usindikaji wa nyaraka usiozuia na operesheni za utafutaji
- **Usimamizi wa Kumbukumbu**: Matumizi bora ya rasilimali kwa makusanyo makubwa ya nyaraka
- **Mifumo ya Ujumuishaji**: Ujumuishaji wa asili wa huduma za Azure na sindikizo la utegemezi

## 🏗️ Usanifu wa Kiufundi

### Njia ya RAG ya Biashara
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Vipengele Vikuu vya .NET
- **Azure.AI.Agents.Persistent**: Usimamizi wa mawakala wa biashara wenye uhifadhi wa hali
- **Azure.Identity**: Uthibitishaji uliounganishwa kwa ufikiaji salama wa huduma za Azure
- **Microsoft.Agents.AI.AzureAI**: Utekelezaji wa mfumo wa mawakala ulioboreshwa kwa Azure
- **System.Linq.Async**: Operesheni za LINQ za utendaji wa juu zisizo na vizuizi

## 🔧 Vipengele na Faida za Biashara

### Usalama na Uzingatiaji
- **Ujumuishaji wa Azure AD**: Usimamizi wa utambulisho wa biashara na uthibitishaji
- **Ufikiaji Kulingana na Majukumu**: Ruhusa za kina kwa ufikiaji wa nyaraka na operesheni
- **Ulinzi wa Data**: Usimbaji wa data wakati wa kuhifadhi na kusafirisha kwa nyaraka nyeti
- **Kumbukumbu za Ukaguzi**: Ufuatiliaji wa shughuli wa kina kwa mahitaji ya uzingatiaji

### Utendaji na Upanuzi
- **Ujumuishaji wa Muunganisho**: Usimamizi bora wa muunganisho wa huduma za Azure
- **Usindikaji wa Async**: Operesheni zisizo na vizuizi kwa hali za utendaji wa juu
- **Mikakati ya Akiba**: Akiba ya akili kwa nyaraka zinazofikiwa mara kwa mara
- **Usawazishaji wa Mizigo**: Usindikaji uliosambazwa kwa utekelezaji wa kiwango kikubwa

### Usimamizi na Ufuatiliaji
- **Ukaguzi wa Afya**: Ufuatiliaji wa ndani kwa vipengele vya mfumo wa RAG
- **Vipimo vya Utendaji**: Takwimu za kina kuhusu ubora wa utafutaji na nyakati za majibu
- **Usimamizi wa Makosa**: Usimamizi wa hali ya kipekee wa kina na sera za kurudia
- **Usimamizi wa Usanidi**: Mipangilio maalum ya mazingira yenye uthibitishaji

## ⚙️ Mahitaji ya Awali na Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#
- Usajili wa Azure wenye ufikiaji wa AI Foundry

**Paket Zinazohitajika za NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Uthibitishaji wa Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Usanidi wa Mazingira:**
* Usanidi wa Azure AI Foundry (unashughulikiwa kiotomatiki kupitia Azure CLI)
* Hakikisha umeidhinishwa kwa usajili sahihi wa Azure

## 📊 Mifumo ya RAG ya Biashara

### Mifumo ya Usimamizi wa Nyaraka
- **Upakiaji wa Wingi**: Usindikaji bora wa makusanyo makubwa ya nyaraka
- **Sasisho za Kiongezi**: Ongezeko la nyaraka na marekebisho kwa wakati halisi
- **Udhibiti wa Toleo**: Utoaji wa toleo la nyaraka na ufuatiliaji wa mabadiliko
- **Usimamizi wa Metadata**: Sifa tajiri za nyaraka na mfumo wa taksonomia

### Mifumo ya Utafutaji na Urejeshaji
- **Utafutaji Mseto**: Kuchanganya utafutaji wa semantiki na maneno muhimu kwa matokeo bora
- **Utafutaji wa Vipengele**: Uchujaji wa vipengele vingi na uainishaji
- **Urekebishaji wa Umuhimu**: Algorithimu za alama maalum kwa mahitaji ya kikoa
- **Upangaji wa Matokeo**: Upangaji wa hali ya juu wenye ujumuishaji wa mantiki ya biashara

### Mifumo ya Usalama
- **Usalama wa Kiwango cha Nyaraka**: Udhibiti wa ufikiaji wa kina kwa kila nyaraka
- **Uainishaji wa Data**: Uwekaji wa lebo ya unyeti kiotomatiki na ulinzi
- **Njia za Ukaguzi**: Kumbukumbu za kina za operesheni zote za RAG
- **Ulinzi wa Faragha**: Ufuatiliaji wa PII na uwezo wa kufuta

## 🔒 Vipengele vya Usalama vya Biashara

### Uthibitishaji na Uidhinishaji
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

### Ulinzi wa Data
- **Usimbaji**: Usimbaji wa mwisho hadi mwisho kwa nyaraka na faharasa za utafutaji
- **Udhibiti wa Ufikiaji**: Ujumuishaji na Azure AD kwa ruhusa za watumiaji na vikundi
- **Makazi ya Data**: Udhibiti wa eneo la data kijiografia kwa uzingatiaji
- **Hifadhi Nakala na Urejeshaji**: Uwezo wa hifadhi nakala kiotomatiki na urejeshaji wa maafa

## 📈 Uboreshaji wa Utendaji

### Mifumo ya Usindikaji wa Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Usimamizi wa Kumbukumbu
- **Usindikaji wa Kutiririsha**: Kushughulikia nyaraka kubwa bila matatizo ya kumbukumbu
- **Ujumuishaji wa Rasilimali**: Matumizi bora ya rasilimali ghali
- **Ukusanyaji wa Takataka**: Mifumo ya ugawaji wa kumbukumbu iliyoboreshwa
- **Usimamizi wa Muunganisho**: Mzunguko sahihi wa muunganisho wa huduma za Azure

### Mikakati ya Akiba
- **Akiba ya Maswali**: Akiba ya utafutaji unaotekelezwa mara kwa mara
- **Akiba ya Nyaraka**: Akiba ya kumbukumbu kwa nyaraka zinazotumika mara kwa mara
- **Akiba ya Faharasa**: Akiba ya faharasa ya vector iliyoboreshwa
- **Akiba ya Matokeo**: Akiba ya akili ya majibu yaliyotengenezwa

## 📊 Matumizi ya Biashara

### Usimamizi wa Maarifa
- **Wiki ya Kampuni**: Utafutaji wa akili katika hifadhidata za maarifa za kampuni
- **Sera na Taratibu**: Mwongozo wa uzingatiaji na taratibu kiotomatiki
- **Vifaa vya Mafunzo**: Msaada wa kujifunza na maendeleo ya akili
- **Hifadhidata za Utafiti**: Mifumo ya uchambuzi wa karatasi za kitaaluma na utafiti

### Msaada kwa Wateja
- **Hifadhidata ya Maarifa ya Msaada**: Majibu ya huduma kwa wateja kiotomatiki
- **Nyaraka za Bidhaa**: Urejeshaji wa taarifa za bidhaa kwa akili
- **Mwongozo wa Utatuzi wa Matatizo**: Msaada wa kutatua matatizo kwa muktadha
- **Mifumo ya Maswali Yanayoulizwa Mara kwa Mara**: Uundaji wa maswali yanayoulizwa mara kwa mara kutoka kwa makusanyo ya nyaraka

### Uzingatiaji wa Kanuni
- **Uchambuzi wa Nyaraka za Kisheria**: Ujasusi wa mikataba na nyaraka za kisheria
- **Ufuatiliaji wa Uzingatiaji**: Ukaguzi wa uzingatiaji wa kanuni kiotomatiki
- **Tathmini ya Hatari**: Uchambuzi wa hatari unaotegemea nyaraka na kuripoti
- **Msaada wa Ukaguzi**: Ugunduzi wa nyaraka za akili kwa ukaguzi

## 🚀 Utekelezaji wa Uzalishaji

### Ufuatiliaji na Uangalizi
- **Application Insights**: Telemetry ya kina na ufuatiliaji wa utendaji
- **Vipimo Maalum**: Ufuatiliaji wa KPI maalum za biashara na tahadhari
- **Ufuatiliaji Ulioenea**: Ufuatiliaji wa maombi kutoka mwanzo hadi mwisho katika huduma
- **Dashibodi za Afya**: Uonyeshaji wa afya ya mfumo na utendaji kwa wakati halisi

### Upanuzi na Uaminifu
- **Upanuzi wa Kiotomatiki**: Upanuzi wa kiotomatiki kulingana na mzigo na vipimo vya utendaji
- **Upatikanaji wa Juu**: Utekelezaji wa maeneo mengi na uwezo wa kushindwa
- **Upimaji wa Mizigo**: Uthibitishaji wa utendaji chini ya hali ya mzigo wa biashara
- **Urejeshaji wa Maafa**: Taratibu za hifadhi nakala na urejeshaji kiotomatiki

Tayari kujenga mifumo ya RAG ya kiwango cha biashara inayoweza kushughulikia nyaraka nyeti kwa kiwango kikubwa? Hebu tusanifu mifumo ya maarifa ya akili kwa biashara! 🏢📖✨

## Utekelezaji wa Msimbo

Mfano wa msimbo kamili wa somo hili unapatikana katika `05-dotnet-agent-framework.cs`. 

Kuendesha mfano:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Au tumia `dotnet run` moja kwa moja:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Msimbo unaonyesha:

1. **Usakinishaji wa Paket**: Kusakinisha paket zinazohitajika za NuGet kwa Mawakala wa Azure AI
2. **Usanidi wa Mazingira**: Kupakia mipangilio ya mwisho wa Azure AI Foundry na modeli
3. **Upakiaji wa Nyaraka**: Kupakia nyaraka kwa usindikaji wa RAG
4. **Uundaji wa Duka la Vector**: Kuunda duka la vector kwa utafutaji wa semantiki
5. **Usanidi wa Mawakala**: Kuweka wakala wa AI wenye uwezo wa utafutaji wa faili
6. **Utekelezaji wa Maswali**: Kuendesha maswali dhidi ya nyaraka zilizopakiwa

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.