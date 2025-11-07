<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:18:05+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🤝 Mfumo wa Kazi wa Wakala wa Wingi wa Biashara (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inaonyesha jinsi ya kujenga mifumo ya wakala wa wingi ya kiwango cha biashara kwa kutumia Microsoft Agent Framework katika .NET na GitHub Models. Utajifunza jinsi ya kuratibu mawakala maalum wanaofanya kazi pamoja kupitia mifumo ya kazi iliyopangwa, ukitumia vipengele vya biashara vya .NET kwa suluhisho tayari kwa uzalishaji.

**Uwezo wa Wakala wa Wingi wa Biashara Utakaoujenga:**
- 👥 **Ushirikiano wa Mawakala**: Uratibu wa wakala salama kwa aina na uthibitisho wa wakati wa kuandaa
- 🔄 **Uratibu wa Mfumo wa Kazi**: Ufafanuzi wa mfumo wa kazi kwa njia ya tamko ukitumia mifumo ya async ya .NET
- 🎭 **Utaalamu wa Majukumu**: Utu wa wakala ulio na aina kali na maeneo ya utaalamu
- 🏢 **Ujumuishaji wa Biashara**: Mifumo tayari kwa uzalishaji yenye ufuatiliaji na utunzaji wa makosa

## ⚙️ Mahitaji ya Awali na Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#
- Usajili wa Azure (kwa mawakala wa kudumu)

**Paket Zinazohitajika za NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Mfano wa Msimbo

Msimbo kamili wa kazi kwa somo hili unapatikana katika faili ya C# inayotolewa: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Ili kuendesha mfano:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Au kwa kutumia .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Kile Mfano Huu Unaonyesha

Mfumo huu wa kazi wa wakala wa wingi unaunda huduma ya mapendekezo ya kusafiri kwa hoteli na mawakala wawili maalum:

1. **Wakala wa FrontDesk**: Wakala wa kusafiri anayetoa mapendekezo ya shughuli na maeneo
2. **Wakala wa Concierge**: Anapitia mapendekezo ili kuhakikisha uzoefu halisi, usio wa kitalii

Mawakala hufanya kazi pamoja katika mfumo wa kazi ambapo:
- Wakala wa FrontDesk hupokea ombi la awali la kusafiri
- Wakala wa Concierge hupitia na kuboresha pendekezo
- Mfumo wa kazi hutiririsha majibu kwa wakati halisi

## Dhana Muhimu

### Uratibu wa Mawakala
Mfano unaonyesha uratibu wa wakala salama kwa aina ukitumia Microsoft Agent Framework na uthibitisho wa wakati wa kuandaa.

### Uratibu wa Mfumo wa Kazi
Unatumia ufafanuzi wa mfumo wa kazi kwa njia ya tamko ukitumia mifumo ya async ya .NET kuunganisha mawakala wengi katika bomba.

### Majibu ya Kutiririka
Unatekeleza utiririshaji wa majibu ya wakala kwa wakati halisi ukitumia async enumerables na usanifu unaoendeshwa na matukio.

### Ujumuishaji wa Biashara
Unaonyesha mifumo tayari kwa uzalishaji ikijumuisha:
- Usanidi wa vigezo vya mazingira
- Usimamizi salama wa hati za siri
- Utunzaji wa makosa
- Usindikaji wa matukio kwa njia ya async

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.