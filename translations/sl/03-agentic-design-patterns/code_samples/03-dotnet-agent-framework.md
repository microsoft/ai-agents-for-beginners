<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:52:27+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🎨 Agentni vzorci oblikovanja z modeli GitHub (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje vzorce oblikovanja na ravni podjetja za gradnjo inteligentnih agentov z uporabo Microsoftovega okvira Agent Framework v .NET z integracijo modelov GitHub. Naučili se boste profesionalne vzorce in arhitekturne pristope, ki omogočajo, da so agenti pripravljeni za produkcijo, vzdržljivi in skalabilni.

**Vzorci oblikovanja na ravni podjetja:**
- 🏭 **Tovarniški vzorec**: Standardizirano ustvarjanje agentov z vbrizgavanjem odvisnosti
- 🔧 **Graditeljski vzorec**: Fluentna konfiguracija in nastavitev agentov
- 🧵 **Vzorci za varnost niti**: Upravljanje sočasnih pogovorov
- 📋 **Vzorci repozitorija**: Organizirano upravljanje orodij in zmogljivosti

## 🎯 Arhitekturne prednosti .NET

### Funkcije na ravni podjetja
- **Močna tipizacija**: Validacija med prevajanjem in podpora IntelliSense
- **Vbrizgavanje odvisnosti**: Integracija vgrajenega DI kontejnerja
- **Upravljanje konfiguracije**: Vzorci IConfiguration in Options
- **Async/Await**: Prvovrstna podpora za asinhrono programiranje

### Vzorci pripravljeni za produkcijo
- **Integracija beleženja**: Podpora za ILogger in strukturirano beleženje
- **Preverjanje zdravja**: Vgrajeno spremljanje in diagnostika
- **Validacija konfiguracije**: Močna tipizacija z anotacijami podatkov
- **Upravljanje napak**: Strukturirano upravljanje izjem

## 🔧 Tehnična arhitektura

### Osnovne komponente .NET
- **Microsoft.Extensions.AI**: Poenotene abstrakcije AI storitev
- **Microsoft.Agents.AI**: Okvir za orkestracijo agentov na ravni podjetja
- **Integracija modelov GitHub**: Vzorci API odjemalcev z visoko zmogljivostjo
- **Sistem konfiguracije**: Integracija appsettings.json in okolja

### Implementacija vzorcev oblikovanja
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Prikazani vzorci na ravni podjetja

### 1. **Ustvarjalni vzorci**
- **Tovarna agentov**: Centralizirano ustvarjanje agentov z dosledno konfiguracijo
- **Graditeljski vzorec**: Fluentni API za kompleksno konfiguracijo agentov
- **Vzorec Singleton**: Upravljanje skupnih virov in konfiguracije
- **Vbrizgavanje odvisnosti**: Ohlapna povezanost in testabilnost

### 2. **Vedenjski vzorci**
- **Vzorec strategije**: Zamenljive strategije izvajanja orodij
- **Vzorec ukaza**: Inkapsulirane operacije agentov z razveljavitvijo/ponovitvijo
- **Vzorec opazovalca**: Upravljanje življenjskega cikla agentov, ki temelji na dogodkih
- **Vzorec predloge metode**: Standardizirani poteki izvajanja agentov

### 3. **Strukturni vzorci**
- **Vzorec adapterja**: Integracijski sloj API modelov GitHub
- **Vzorec dekoratorja**: Izboljšanje zmogljivosti agentov
- **Vzorec fasade**: Poenostavljeni vmesniki za interakcijo z agenti
- **Vzorec proxyja**: Lenobno nalaganje in predpomnjenje za zmogljivost

## ⚙️ Predpogoji in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Dostop do API modelov GitHub

**Odvisnosti NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Načela oblikovanja v .NET

### Načela SOLID
- **Enotna odgovornost**: Vsaka komponenta ima en jasen namen
- **Odprto/Zaprto**: Razširljivo brez spreminjanja
- **Liskov substitucija**: Implementacije orodij, ki temeljijo na vmesnikih
- **Ločitev vmesnikov**: Osredotočeni, kohezivni vmesniki
- **Inverzija odvisnosti**: Odvisnost od abstrakcij, ne konkretnih implementacij

### Čista arhitektura
- **Plast domene**: Osnovne abstrakcije agentov in orodij
- **Plast aplikacije**: Orkestracija agentov in poteki dela
- **Plast infrastrukture**: Integracija modelov GitHub in zunanjih storitev
- **Plast predstavitve**: Interakcija z uporabnikom in formatiranje odgovorov

## 🔒 Premisleki na ravni podjetja

### Varnost
- **Upravljanje poverilnic**: Varno ravnanje z API ključi z uporabo IConfiguration
- **Validacija vnosa**: Močna tipizacija in validacija z anotacijami podatkov
- **Sanitacija izhoda**: Varna obdelava in filtriranje odgovorov
- **Beleženje revizij**: Celovito sledenje operacijam

### Zmogljivost
- **Asinhroni vzorci**: Neblokirajoče I/O operacije
- **Upravljanje povezav**: Učinkovito upravljanje HTTP odjemalcev
- **Predpomnjenje**: Predpomnjenje odgovorov za izboljšano zmogljivost
- **Upravljanje virov**: Pravilno odstranjevanje in vzorci čiščenja

### Skalabilnost
- **Varnost niti**: Podpora za sočasno izvajanje agentov
- **Upravljanje virov**: Učinkovita uporaba virov
- **Upravljanje obremenitve**: Omejevanje hitrosti in obravnavanje povratnega pritiska
- **Spremljanje**: Meritve zmogljivosti in preverjanje zdravja

## 🚀 Produkcijska uvedba

- **Upravljanje konfiguracije**: Nastavitve, specifične za okolje
- **Strategija beleženja**: Strukturirano beleženje z ID-ji korelacije
- **Upravljanje napak**: Globalno upravljanje izjem z ustreznim okrevanjem
- **Spremljanje**: Application Insights in števci zmogljivosti
- **Testiranje**: Vzorci enotnih testov, integracijskih testov in testov obremenitve

Pripravljeni na gradnjo inteligentnih agentov na ravni podjetja z .NET? Arhitektirajmo nekaj robustnega! 🏢✨

## Vzorec kode

Za popoln delujoč primer si oglejte [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.