<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:28:57+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🛠️ Napredno uporabo orodij z modeli GitHub (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje vzorce integracije orodij na ravni podjetja z uporabo Microsoft Agent Framework v .NET z modeli GitHub. Naučili se boste graditi napredne agente z več specializiranimi orodji, pri čemer boste izkoristili močno tipizacijo jezika C# in funkcije za podjetja v .NET.

**Napredne zmogljivosti orodij, ki jih boste obvladali:**
- 🔧 **Arhitektura več orodij**: Gradnja agentov z več specializiranimi zmogljivostmi
- 🎯 **Varno izvajanje orodij glede na tipe**: Izkoristite preverjanje pravilnosti med prevajanjem v C#
- 📊 **Vzorce orodij za podjetja**: Oblikovanje orodij, pripravljeno za produkcijo, in obravnavanje napak
- 🔗 **Sestavljanje orodij**: Kombiniranje orodij za kompleksne poslovne delovne tokove

## 🎯 Prednosti arhitekture orodij v .NET

### Funkcije orodij za podjetja
- **Preverjanje pravilnosti med prevajanjem**: Močna tipizacija zagotavlja pravilnost parametrov orodij
- **Vbrizgavanje odvisnosti**: Integracija IoC kontejnerja za upravljanje orodij
- **Vzorec Async/Await**: Nezastojno izvajanje orodij z ustreznim upravljanjem virov
- **Strukturirano beleženje**: Vgrajena integracija beleženja za spremljanje izvajanja orodij

### Vzorci, pripravljeni za produkcijo
- **Obravnavanje izjem**: Celovito upravljanje napak s tipiziranimi izjemami
- **Upravljanje virov**: Ustrezni vzorci za odstranjevanje in upravljanje pomnilnika
- **Spremljanje zmogljivosti**: Vgrajene metrike in števci zmogljivosti
- **Upravljanje konfiguracije**: Tipizirana konfiguracija z validacijo

## 🔧 Tehnična arhitektura

### Osnovne komponente orodij v .NET
- **Microsoft.Extensions.AI**: Poenotena plast abstrakcije orodij
- **Microsoft.Agents.AI**: Orkestracija orodij na ravni podjetja
- **Integracija modelov GitHub**: Visoko zmogljiv API odjemalec z združevanjem povezav

### Cevovod za izvajanje orodij
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategorije orodij in vzorci

### 1. **Orodja za obdelavo podatkov**
- **Validacija vhodnih podatkov**: Močna tipizacija z anotacijami podatkov
- **Operacije pretvorbe**: Tipizirana pretvorba in formatiranje podatkov
- **Poslovna logika**: Orodja za izračune in analize, specifične za domeno
- **Formatiranje izhodnih podatkov**: Generiranje strukturiranih odgovorov

### 2. **Integracijska orodja**
- **API konektorji**: Integracija RESTful storitev z HttpClient
- **Orodja za baze podatkov**: Integracija Entity Framework za dostop do podatkov
- **Operacije z datotekami**: Varne operacije datotečnega sistema z validacijo
- **Zunanje storitve**: Vzorci integracije storitev tretjih oseb

### 3. **Orodja za pripomočke**
- **Obdelava besedila**: Pripomočki za manipulacijo in formatiranje nizov
- **Operacije z datumi/časi**: Kulturno ozaveščeni izračuni datumov/časov
- **Matematična orodja**: Natančni izračuni in statistične operacije
- **Orodja za validacijo**: Validacija poslovnih pravil in preverjanje podatkov

## ⚙️ Predpogoji in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Dostop do API-ja modelov GitHub

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okolja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Pripravljeni za gradnjo agentov na ravni podjetja z zmogljivimi, tipiziranimi zmogljivostmi orodij v .NET? Zasnujmo profesionalne rešitve! 🏢⚡

## 💻 Implementacija kode

Celotna implementacija v C# je na voljo v spremljevalni datoteki `04-dotnet-agent-framework.cs`. Ta .NET aplikacija v eni datoteki prikazuje:

- Nalaganje spremenljivk okolja za konfiguracijo modelov GitHub
- Definiranje prilagojenih orodij z uporabo metod C# z atributi
- Ustvarjanje AI agenta z integracijo orodij
- Upravljanje niti pogovora
- Izvajanje zahtev agenta z uporabo orodij

Za zagon primera:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ali z uporabo .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.