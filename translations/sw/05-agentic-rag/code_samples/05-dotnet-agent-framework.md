# 🔍 Enterprise RAG na Microsoft Foundry (.NET)

## 📋 Malengo ya Kujifunza

Daftari hili linaonyesha jinsi ya kujenga mifumo ya kizazi ya RAG ya kiwango cha biashara kwa kutumia Microsoft Agent Framework katika .NET na Microsoft Foundry. Utajifunza jinsi ya kuunda maajenti tayari kwa uzalishaji ambayo yanaweza kutafuta kupitia nyaraka na kutoa majibu sahihi, yanayojua muktadha na usalama pamoja na ukuzaji wa biashara.

**Uwezo wa Enterprise RAG Utakaoujenga:**
- 📚 **Akili ya Nyaraka**: Usindikaji wa hali ya juu wa nyaraka kwa huduma za AI za Azure
- 🔍 **Utafutaji wa Semantiki**: Utafutaji bora wa vector wenye vipengele vya biashara
- 🛡️ **Uunganishaji wa Usalama**: Upatikanaji wa msingi wa majukumu na mifumo ya ulinzi data
- 🏢 **Mimaaruba Inayoweza Kuongezeka**: Mifumo ya RAG tayari kwa uzalishaji yenye ufuatiliaji

## 🎯 Mimarisha ya Enterprise RAG

### Sehemu Muhimu za Enterprise
- **Microsoft Foundry**: Jukwaa la AI la biashara linalosimamiwa lenye usalama na ufuataji sheria
- **Maajenti Walio Hifadhiwa**: Maajenti wenye hali na usimamizi wa muktadha wa mazungumzo
- **Usimamizi wa Hifadhi ya Vector**: Kuweka alama na upokeaji wa nyaraka kwa kiwango cha biashara
- **Uunganishaji wa Utambulisho**: Uthibitishaji wa Azure AD na udhibiti wa upatikanaji wa majukumu

### Manufaa ya .NET Enterprise
- **Usalama wa Aina**: Uthibitishaji wakati wa kuunganisha kwa kazi za RAG na miundo ya data
- **Ufanisi wa Kazi za Async**: Usindikaji wa nyaraka na utafutaji usiozuia kazi nyingine
- **Usimamizi wa Kumbukumbu**: Matumizi bora ya rasilimali kwa makusanyo makubwa ya nyaraka
- **Mifumo ya Uunganishaji**: Uunganishaji wa huduma za Azure asilia kwa kutumia injection ya utegemezi

## 🏗️ Mimarisha ya Kiufundi

### Mlolongo wa Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Sehemu Muhimu za .NET
- **Azure.AI.Agents.Persistent**: Usimamizi wa maajenti wa biashara wenye uhifadhi wa hali
- **Azure.Identity**: Uthibitishaji uliounganishwa kwa upatikanaji salama wa huduma za Azure
- **Microsoft.Agents.AI.AzureAI**: Utekelezaji wa mfumo wa maajenti ulioboreshwa kwa Azure
- **System.Linq.Async**: Kazi za LINQ zisizo za kusimamisha kwa ufanisi mkubwa

## 🔧 Vipengele na Manufaa ya Enterprise

### Usalama na Uzingatiaji Sheria
- **Uunganishaji wa Azure AD**: Usimamizi wa utambulisho wa biashara na uthibitishaji
- **Udhibiti wa Upatikanaji kwa Majukumu**: Ruhusa za kina kwa upatikanaji na operesheni za nyaraka
- **Ulinzi wa Data**: Usimbaji fiche wa nyaraka pale zinapohifadhiwa na zinaposafirishwa
- **Kufuatilia Ukaguzi**: Ufuatiliaji mpana wa shughuli kwa mahitaji ya uzingatiaji

### Ufanisi na Ukuzaji
- **Usimamizi wa Pool ya Muunganisho**: Usimamizi wa muunganisho wa huduma za Azure wa ufanisi
- **Usindikaji wa Async**: Operesheni zisizozuia kwa hali za mtiririko wa juu
- **Mikakati ya Kuhifadhi Cache**: Kuhifadhi akili kwa nyaraka zinazotembelewa mara kwa mara
- **Usawazishaji Wa Mzigo**: Usindikaji uliosambazwa kwa usambazaji mkubwa

### Usimamizi na Ufuatiliaji
- **Ukaguzi wa Afya**: Ufuatiliaji uliojengwa kwa vipengele vya mfumo wa RAG
- **Vipimo vya Ufanisi**: Uchambuzi wa kina juu ya ubora wa utafutaji na nyakati za majibu
- **Udhibiti wa Makosa**: Usimamizi mpana wa makosa with sera za jaribio upya
- **Usimamizi wa Mipangilio**: Mipangilio ya mazingira fulani yenye uthibitishaji

## ⚙️ Yanayohitajika na Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na ugani wa C#
- Usajili wa Azure kwa upatikanaji wa Microsoft Foundry

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
# Sakinisha Azure CLI na thibitisha utambulisho
az login
az account set --subscription "your-subscription-id"
```

**Usanidi wa Mazingira:**
* Usanidi wa Microsoft Foundry (huendeshwa kiotomatiki kupitia Azure CLI)
* Hakikisha umeingia kwenye usajili sahihi wa Azure

## 📊 Mifumo ya Enterprise RAG

### Mifumo ya Usimamizi wa Nyaraka
- **Kupakia kwa Wingi**: Usindikaji wa makusanyo makubwa ya nyaraka kwa ufanisi
- **Mabadiliko ya Hatua kwa Hatua**: Kuongeza na kubadilisha nyaraka kwa wakati halisi
- **Udhibiti wa Toleo**: Kufuatilia matoleo ya nyaraka na mabadiliko
- **Usimamizi wa Metadata**: Sifa tajiri za nyaraka na utaratibu wa aina

### Mifumo ya Utafutaji na Upokeaji
- **Utafutaji Mchanganyiko**: Kuchanganya utafutaji wa semantiki na maneno muhimu kwa matokeo bora
- **Utafutaji kwa Mipangilio**: Kuchuja na kupanga kwa vipimo vingi
- **Urekebishaji wa Uhusiano**: Algoriti za alama maalum kwa mahitaji ya kipekee ya sekta
- **Upangaji wa Matokeo**: Upangaji wa hali ya juu ukiwa na uunganishaji wa mantiki za biashara

### Mifumo ya Usalama
- **Usalama wa Ngazi ya Nyaraka**: Udhibiti wa upatikanaji wa kina kwa kila nyaraka
- **Uainishaji wa Data**: Uwekaji alama wa moja kwa moja wa ugumu na ulinzi
- **Marekodi ya Ukaguzi**: Kurekodi kwa kina operesheni zote za RAG
- **Ulinzi wa Faragha**: Kugundua na kufuta taarifa za PII

## 🔒 Vipengele vya Usalama vya Enterprise

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
- **Usimbaji fiche**: Usimbaji fiche wa mwisho kwa mwisho kwa nyaraka na faharasa za utafutaji
- **Udhibiti wa Upatikanaji**: Uunganisho na Azure AD kwa ruhusa za watumiaji na makundi
- **Makazi ya Data**: Udhibiti wa eneo la kijiografia la data kwa uzingatiaji sheria
- **Hifadhi na Urejeshaji**: Urahisi wa hifadhi ya nakala na urejeshaji wa majanga

## 📈 Uboreshaji wa Ufanisi

### Mifumo ya Usindikaji wa Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Usimamizi wa Kumbukumbu
- **Usindikaji wa Mtiririko**: Kusimamia nyaraka kubwa bila matatizo ya kumbukumbu
- **Malisho ya Rasilimali**: Matumizi bora ya rasilimali ghali
- **Ukusanyaji Takataka**: Mifumo ya ugawaji kumbukumbu kwa ufanisi
- **Usimamizi wa Muunganisho**: Mzunguko sahihi wa muunganisho wa huduma za Azure

### Mikakati ya Kuhifadhi Cache
- **Kuhifadhi Cache za Maulizo**: Kuhifadhi kwa akili utafutaji unaofanywa mara kwa mara
- **Kuhifadhi Cache za Nyaraka**: Kuhifadhi ndani ya kumbukumbu kwa nyaraka moto
- **Kuhifadhi Cache za Faharasa**: Kuhifadhi faharasa za vector kwa ufanisi
- **Kuhifadhi Cache za Majibu**: Kuhifadhi kwa akili majibu yaliyotengenezwa

## 📊 Matumizi ya Enterprise

### Usimamizi wa Maarifa
- **Wiki ya Kampuni**: Utafutaji wa akili kwenye hifadhidata za maarifa ya kampuni
- **Sera na Taratibu**: Ufuataji wa kiotomatiki wa uzingatiaji na mwongozo wa taratibu
- **Vifaa vya Mafunzo**: Usaidizi wa kujifunza na maendeleo wa akili
- **Hifadhidata za Utafiti**: Mifumo ya uchambuzi wa karatasi za kitaaluma na utafiti

### Huduma kwa Wateja
- **Hifadhidata ya Maarifa ya Msaada**: Majibu ya huduma kwa wateja yaliyotozwa kiotomatiki
- **Nyaraka za Bidhaa**: Upokeaji wa habari za bidhaa kwa akili
- **Mwongozo wa Kutatua Matatizo**: Usaidizi wa kutatua matatizo kwa muktadha
- **Mifumo ya Maswali yanayoulizwa Mara kwa Mara (FAQ)**: Uzazi wa maswali ya FAQ kwa muktadha ya makala

### Uzingatiaji wa Sheria
- **Uchambuzi wa Nyaraka za Kisheria**: Akili ya mikataba na nyaraka za kisheria
- **Ufuatiliaji wa Uzingatiaji**: Ukaguzi wa uzingatiaji wa sheria kwa njia ya kiotomatiki
- **Tathmini ya Hatari**: Uchambuzi wa hatari na uwasilishaji wa ripoti kulingana na nyaraka
- **Msaada wa Ukaguzi**: Ugunduzi wa nyaraka kwa ajili ya ukaguzi kwa akili

## 🚀 Uwasilishaji wa Uzalishaji

### Ufuatiliaji na Uwezekano wa Kuona
- **Application Insights**: Telemetri ya kina na ufuatiliaji wa ufanisi
- **Vipimo Maalum**: Ufuatiliaji na onyo la KPI za biashara
- **Ufuatiliaji wa Maombi Yaliyosambazwa**: Ufuatiliaji wa maombi kutoka mwanzo hadi mwisho kwenye huduma
- **Dashibodi za Afya**: Uonyesho wa hali ya afya ya mfumo na ufanisi kwa wakati halisi

### Ukuzaji na Uthabiti
- **Kuongeza Kwa Kiotomatiki**: Kuongeza skalp kama inavyohitajika kulingana na mzigo na vipimo vya ufanisi
- **Upatikanaji Mkuu**: Uwekezaji wa maeneo mengi yenye uwezo wa kukabiliana na kushindwa
- **Upimaji wa Mzigo**: Uthibitisho wa ufanisi chini ya mzigo wa biashara
- **Urejeshaji wa Majanga**: Taratibu za kuhifadhi nakala na kurejesha kiotomatiki

Tayari kujenga mifumo ya RAG ya kiwango cha biashara inayoweza kushughulikia nyaraka nyeti kwa kiwango? Hebu tufanye usanifu wa mifumo ya maarifa yenye akili kwa biashara! 🏢📖✨

## Utekelezaji wa Msimbo

Sampuli kamili ya msimbo wa kazi kwa somo hili inapatikana katika `05-dotnet-agent-framework.cs`.

Ili kuendesha mfano:

```bash
# Fanya skripti iwe inatekelezeka (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Endesha Programu ya Faili Moja ya .NET
./05-dotnet-agent-framework.cs
```

Au tumia `dotnet run` moja kwa moja:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Msimbo unaonyesha:

1. **Usakinishaji wa Pakiti**: Kusakinisha vifurushi vinavyohitajika vya NuGet kwa maajenti wa Azure AI
2. **Usanidi wa Mazingira**: Kupakia usanidi wa kivuko na modeli za Microsoft Foundry
3. **Uchaji wa Nyaraka**: Kupakia nyaraka kwa usindikaji wa RAG
4. **Uundaji wa Hifadhi ya Vector**: Kuunda hifadhi ya vector kwa utafutaji wa semantiki
5. **Usanidi wa Maajenti**: Kuweka maajenti wa AI na uwezo wa kutafuta faili
6. **Utekelezaji wa Maswali**: Kuendesha maswali dhidi ya nyaraka zilizopakiwa

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->