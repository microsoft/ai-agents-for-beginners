# 🔍 Enterprise RAG na Microsoft Foundry (.NET)

## 📋 Malengo ya Kujifunza

Daftari hili linaonyesha jinsi ya kujenga mifumo ya Utoaji wa Maoni Iliyoimarishwa (RAG) ya daraja la biashara kwa kutumia Mfumo wa Wakala wa Microsoft katika .NET na Microsoft Foundry. Utafanya kujifunza kuunda mawakala tayari kwa uzalishaji ambao wanaweza kutafuta kupitia nyaraka na kutoa majibu sahihi, yanayojua muktadha na yenye usalama na uwezo wa kupanuka vya kiutawala.

**Uwezo wa Enterprise RAG Utakaoujenga:**
- 📚 **Uelewa wa Nyaraka**: Usindikaji wa nyaraka wa hali ya juu kwa huduma za AI za Azure
- 🔍 **Utafutaji wa Semantiki**: Utafutaji wa vector wenye utendaji wa juu na sifa za biashara
- 🛡️ **Muunganisho wa Usalama**: Upatikanaji wa msingi wa majukumu na mifumo ya ulinzi wa data
- 🏢 **Mimaariko Inayopanuka**: Mifumo ya RAG tayari kwa uzalishaji yenye usimamizi

## 🎯 Mimariko ya Enterprise RAG

### Vipengele Vikuu vya Biashara
- **Microsoft Foundry**: Jukwaa la AI la biashara lililodhibitiwa na usalama na uzingatiaji
- **Mawakala wa Kudumu**: Mawakala wenye hali na historia ya mazungumzo na usimamizi wa muktadha
- **Usimamizi wa Uhifadhi wa Vector**: Uorodhesaji na upataji wa nyaraka za daraja la biashara
- **Muunganisho wa Utambulisho**: Uthibitishaji wa Azure AD na udhibiti wa upatikanaji wa majukumu

### Manufaa ya .NET kwa Biashara
- **Usalama wa Aina**: Uthibitishaji wakati wa compilation kwa operesheni za RAG na muundo wa data
- **Utendaji wa Async**: Usindikaji wa nyaraka na utafutaji usiozuia
- **Usimamizi wa Kumbukumbu**: Matumizi madhubuti ya rasilimali kwa makusanyo makubwa ya nyaraka
- **Mifumo ya Muunganisho**: Muunganisho wa huduma za Azure kwa kutumia injection ya utegemezi

## 🏗️ Mimariko ya Kiufundi

### Mhimili wa Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Vipengele Vikuu vya .NET
- **Azure.AI.Agents.Persistent**: Usimamizi wa mawakala wa biashara wenye uhifadhi wa hali
- **Azure.Identity**: Uthibitishaji uliounganishwa kwa upatikanaji salama wa huduma za Azure
- **Microsoft.Agents.AI.AzureAI**: Utekelezaji wa mfumo wa wakala ulioboreshwa kwa Azure
- **System.Linq.Async**: Operesheni za LINQ zisizozuia zenye utendaji wa juu

## 🔧 Sifa na Manufaa ya Enterprise

### Usalama na Uzingatiaji
- **Muunganisho wa Azure AD**: Usimamizi wa utambulisho wa biashara na uthibitishaji
- **Upatikanaji wa Msingi wa Majukumu**: Ruhusa za kina kwa upatikanaji wa nyaraka na operesheni
- **Ulinzi wa Data**: Ufungaji wa data wakati wa kutosha na wakati wa usafiri kwa nyaraka nyeti
- **Ufuatiliaji wa Ukaguzi**: Ufuatiliaji wa shughuli kwa mahitaji ya uzingatiaji

### Utendaji na Uwezo wa Kupanuka
- **Pooli ya Muunganisho**: Usimamizi madhubuti wa muunganisho wa huduma za Azure
- **Usindikaji wa Async**: Operesheni zisizozuia kwa hali za mtiririko mkubwa
- **Mikakati ya Kuweka kwa Cache**: Kuweka smart kwa nyaraka zinazotafutwa sana
- **Ugawaji wa Mzigo**: Usindikaji uliogawanyika kwa usambazaji mkubwa

### Usimamizi na Ufuatiliaji
- **Ukaguzi wa Afya**: Ufuatiliaji uliomo kwa vipengele vya mfumo wa RAG
- **Vipimo vya Utendaji**: Uchambuzi wa kina juu ya ubora wa utafutaji na muda wa majibu
- **Ushughulikiaji wa Makosa**: Usimamizi wa makosa kwa sehemu na sera za jaribio tena
- **Usimamizi wa Mipangilio**: Mipangilio maalum ya mazingira yenye uthibitishaji

## ⚙️ Mahitaji ya Awali na Usanidi

**Mazingira ya Maendeleo:**
- SDK ya .NET 9.0 au juu zaidi
- Visual Studio 2022 au VS Code na ugani wa C#
- Usajili wa Azure wenye upatikanaji wa Microsoft Foundry

**Packages za NuGet Zinazohitajika:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Uthibitishaji wa Azure:**
```bash
# Weka Azure CLI na thibitisha utambulisho
az login
az account set --subscription "your-subscription-id"
```

**Usanidi wa Mazingira:**
* Usanidi wa Microsoft Foundry (huendeshwa moja kwa moja kupitia Azure CLI)
* Hakikisha umeingia kwa usajili sahihi wa Azure

## 📊 Mifumo ya Enterprise RAG

### Mifumo ya Usimamizi wa Nyaraka
- **Upakiaji wa Wingi**: Usindikaji madhubuti wa makusanyo makubwa ya nyaraka
- **Mabadiliko ya Hatua kwa Hatua**: Kuongeza na kubadilisha nyaraka kwa wakati halisi
- **Udhibiti wa Toleo**: Utoleo wa nyaraka na ufuatiliaji wa mabadiliko
- **Usimamizi wa Metadata**: Sifa tajiri za nyaraka na taksonomia

### Mifumo ya Utafutaji na Upataji
- **Utafutaji Mseto**: Kuunganisha utafutaji wa semantiki na maneno muhimu kwa matokeo bora
- **Utafutaji wa Vigenge**: Kuchuja na kupanga kwa vipimo vingi
- **Urekebishaji wa Uhusiano**: Algoriti za alama maalum kwa mahitaji maalum ya eneo
- **Upangaji wa Matokeo**: Upangaji wa hali ya juu na muunganisho wa mantiki ya biashara

### Mifumo ya Usalama
- **Usalama wa Ngazi ya Nyaraka**: Udhibiti wa upatikanaji kwa nyaraka moja moja
- **Uainishaji wa Data**: Uwekaji lebo wa kiotomatiki wa unyeti na ulinzi
- **Fuatiliaji wa Ukaguzi**: Kuandika kumbukumbu kamili za operesheni zote za RAG
- **Ulinzi wa Faragha**: Kugundua na kuficha Taarifa Binafsi za Mtumiaji (PII)

## 🔒 Sifa za Usalama wa Enterprise

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
- **Ufungaji**: Ufungaji kamili kwa nyaraka na faharasa za utafutaji
- **Udhibiti wa Upatikanaji**: Muunganisho na Azure AD kwa ruhusa za watumiaji na makundi
- **Makazi ya Data**: Udhibiti wa eneo la data kwa uzingatiaji
- **Nakili na Ufufuaji**: Nakili za automatiki na uwezo wa kupona majanga

## 📈 Uboreshaji wa Utendaji

### Mifumo ya Usindikaji Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Usimamizi wa Kumbukumbu
- **Usindikaji wa Mtiririko**: Hudumia nyaraka kubwa bila matatizo ya kumbukumbu
- **Pooli ya Rasilimali**: Matumizi ya rasilimali ghali kwa ufanisi
- **Ukusanyaji wa Takataka**: Mifumo iliyoboreshwa ya ugawaji wa kumbukumbu
- **Usimamizi wa Muunganisho**: Mzunguko sahihi wa muunganisho wa huduma za Azure

### Mikakati ya Kuweka kwa Cache
- **Kuweka kwa Cache kwa Maswali**: Kuweka kwa cache utafutaji unaofanywa mara kwa mara
- **Kuweka kwa Cache kwa Nyaraka**: Kuweka kwa cache kwa kumbukumbu wa nyaraka moto
- **Kuweka kwa Cache kwa Faharasa**: Kuweka kwa cache faharasa za vector zilizo boreshwa
- **Kuweka kwa Cache Matokeo**: Kuweka madhubuti kwa cache majibu yaliyozalishwa

## 📊 Matumizi ya Enterprise

### Usimamizi wa Maarifa
- **Wiki ya Kampuni**: Utafutaji mwenye akili katika misingi ya maarifa ya kampuni
- **Sera na Taratibu**: Uzingatiaji na mwongozo wa taratibu wa moja kwa moja
- **Vifaa vya Mafunzo**: Msaada wa kujifunza na maendeleo wenye akili
- **Maktaba za Utafiti**: Mifumo ya uchambuzi wa makala za kitaaluma na utafiti

### Msaada kwa Wateja
- **Msingi wa Maarifa ya Msaada**: Majibu ya huduma kwa wateja ya moja kwa moja
- **Nyaraka za Bidhaa**: Upataji wa taarifa za bidhaa kwa akili
- **Viongozi vya Utatuzi wa Matatizo**: Msaada wa kutatua matatizo kwa muktadha
- **Mifumo ya Maswali Yanayoulizwa Mara kwa Mara (FAQ)**: Uundaji wa FAQ kwa nyaraka zilizokusanywa

### Uzingatiaji wa Sheria
- **Uchambuzi wa Nyaraka za Kisheria**: Uelewa wa mikataba na nyaraka za kisheria
- **Ufuatiliaji wa Uzingatiaji**: Ukaguzi wa uzingatiaji wa kanuni kwa njia ya kiotomatiki
- **Tathmini ya Hatari**: Uchambuzi wa hatari na utoaji ripoti kwa nyaraka
- **Msaada wa Ukaguzi**: Ugunduzi wa nyaraka wenye akili kwa ukaguzi

## 🚀 Utekelezaji wa Uzalishaji

### Ufuatiliaji na Uhitajika Kuonekana
- **Application Insights**: Telemetri ya kina na ufuatiliaji wa utendaji
- **Vipimo Maalum**: Ufuatiliaji na onyo la KPI za biashara maalum
- **Ufuatiliaji Uliogawanywa**: Ufuatiliaji wa maombi kuanzia mwanzo hadi mwisho kupitia huduma
- **Dashibodi za Afya**: Uonyesho wa afya na utendaji wa mfumo kwa wakati halisi

### Uwezo wa Kupanuka na Uthabiti
- **Kupanua Kiotomatiki**: Kupanua kiotomatiki kulingana na mzigo na vipimo vya utendaji
- **Upatikanaji wa Juu**: Utekelezaji wa maeneo mengi yenye uwezo wa kuhamia kwenye zana nyingine
- **Upimaji wa Mzigo**: Uthibitishaji wa utendaji chini ya hali za mzigo wa biashara
- **Ufufuaji wa Ajali**: Taratibu za nakala na kupona ajali kwa njia ya kiotomatiki

Tayari kujenga mifumo ya RAG ya daraja la biashara inayoweza kushughulikia nyaraka nyeti kwa wingi? Hebu tuitengeneze mifumo yenye akili ya maarifa kwa biashara! 🏢📖✨

## Utekelezaji wa Msimbo

Mfano kamili wa msimbo unaofanya kazi kwa somo hili upatikana katika `05-dotnet-agent-framework.cs`. 

Kuendesha mfano:

```bash
# Fanya hati ya maandishi iweze kutekelezwa (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Endesha Programu ya Faili Moja ya .NET
./05-dotnet-agent-framework.cs
```

Au tumia `dotnet run` moja kwa moja:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Msimbo unaonyesha:

1. **Usakinishaji wa Paket**: Kusakinisha packages za NuGet zinazohitajika kwa Wakala wa Azure AI
2. **Usanidi wa Mazingira**: Kupakia mipangilio ya mwisho wa Microsoft Foundry na modeli
3. **Upakiaji wa Nyaraka**: Kupakia nyaraka kwa usindikaji wa RAG
4. **Uundaji wa Uhifadhi wa Vector**: Kuunda duka la vector kwa utafutaji wa semantiki
5. **Usanidi wa Wakala**: Kuanzisha wakala wa AI wenye uwezo wa kutafuta faili
6. **Utekelezaji wa Maswali**: Kuendesha maswali dhidi ya nyaraka zilizo pakwa

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->