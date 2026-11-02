# 🤝 Mifumo ya Wafanyakazi Wengi wa Biashara (.NET)

## 📋 Malengo ya Kujifunza

Daftari hili linaonyesha jinsi ya kujenga mifumo tata ya wafanyakazi wengi wa daraja la biashara kutumia Mfumo wa Wakala wa Microsoft katika .NET na Azure OpenAI (API za Majibu). Utajifunza kuandaa wakala wengi maalum wanaofanya kazi pamoja kupitia michakato iliyopangwa, ukitumia sifa za biashara za .NET kwa suluhisho zinazostahili uzalishaji.

**Uwezo wa Wafanyakazi Wengi wa Biashara Utakaojenga:**
- 👥 **Ushirikiano wa Wakala**: Usawazishaji wa wakala wenye aina salama na uthibitisho wakati wa kuandika programu
- 🔄 **Usimamizi wa Michakato**: Ufafanuzi wa michakato ya kazi kwa utaratibu na mifumo ya async ya .NET
- 🎭 **Utaalam wa Majukumu**: Wakala wenye tabia zenye aina imara na maeneo ya utaalam
- 🏢 **Muungano wa Biashara**: Mifumo inayostahili uzalishaji ikiwa na ufuatiliaji na usimamizi wa makosa

## ⚙️ Mahitaji na Mipangilio

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#
- Usajili wa Azure (kwa wakala wa kudumu)

**Pakiti za NuGet Zinazohitajika:**
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

## Mfano wa Msimbo

Msimbo mzima unaofanya kazi kwa somo hili upo katika faili la C# linaloambatana: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Ili kuendesha mfano huu:

```bash
# Fanya faili iwe ya utekelezaji (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Endesha sampuli
./08-dotnet-agent-framework.cs
```

Au ukitumia .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Hiki Mfano Kinaonyesha Nini

Mfumo huu wa mchakato wa wafanyakazi wengi hutengeneza huduma ya mapendekezo ya usafiri wa hoteli na wakala maalum wawili:

1. **Wakala wa FrontDesk**: Mwakala wa usafiri anayetoa mapendekezo ya shughuli na maeneo
2. **Wakala wa Concierge**: Hukagua mapendekezo ili kuhakikisha uzoefu halisi, usio wa watalii

Wakala hao hufanya kazi pamoja katika mchakato ambapo:
- Wakala wa FrontDesk anapokea ombi la usafiri la awali
- Wakala wa Concierge hukagua na kuboresha pendekezo
- Mchakato hupelekwa majibu papo hapo kwa mtiririko wa moja kwa moja

## Dhana Muhimu

### Usawazishaji wa Wakala
Mfano unaonyesha usawazishaji wa wakala wenye aina salama ukitumia Mfumo wa Wakala wa Microsoft na uthibitisho wakati wa kuandika programu.

### Usimamizi wa Michakato
Hutumia uainishaji wa michakato kwa utaratibu na mifumo ya async ya .NET kuunganisha wakala wengi katika mfululizo.

### Kupelekwa kwa Majibu Moja kwa Moja
Hutatua mtiririko wa papo hapo wa majibu ya wakala kwa kutumia orodha za async na usanifu wa tukio unaoendeshwa.

### Muungano wa Biashara
Inaonyesha mifumo inayostahili uzalishaji ikiwemo:
- Mipangilio ya variable ya mazingira
- Usimamizi salama wa nywila
- Usimamizi wa makosa
- Usindikaji wa tukio usio na ufuatiliaji

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->