<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:52:13+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🎨 Agentni dizajnerski obrasci s GitHub modelima (.NET)

## 📋 Ciljevi učenja

Ovaj priručnik prikazuje dizajnerske obrasce na razini poduzeća za izradu inteligentnih agenata koristeći Microsoft Agent Framework u .NET-u s integracijom GitHub modela. Naučit ćete profesionalne obrasce i arhitektonske pristupe koji čine agente spremnima za produkciju, održivima i skalabilnima.

**Dizajnerski obrasci za poduzeća:**
- 🏭 **Obrazac tvornice**: Standardizirano stvaranje agenata uz injekciju ovisnosti
- 🔧 **Obrazac graditelja**: Fluentna konfiguracija i postavljanje agenata
- 🧵 **Obrasci sigurni za niti**: Upravljanje razgovorima u više niti
- 📋 **Obrazac repozitorija**: Organizirano upravljanje alatima i sposobnostima

## 🎯 Arhitektonske prednosti specifične za .NET

### Značajke za poduzeća
- **Jako tipiziranje**: Provjera valjanosti u vrijeme kompilacije i podrška za IntelliSense
- **Injekcija ovisnosti**: Integracija ugrađenog DI spremnika
- **Upravljanje konfiguracijom**: Obrasci IConfiguration i Options
- **Async/Await**: Prvoklasna podrška za asinkrono programiranje

### Obrasci spremni za produkciju
- **Integracija zapisivanja**: Podrška za ILogger i strukturirano zapisivanje
- **Provjere zdravlja**: Ugrađeno praćenje i dijagnostika
- **Provjera konfiguracije**: Jako tipiziranje s validacijom podataka
- **Upravljanje pogreškama**: Strukturirano upravljanje iznimkama

## 🔧 Tehnička arhitektura

### Osnovne .NET komponente
- **Microsoft.Extensions.AI**: Ujednačene apstrakcije AI usluga
- **Microsoft.Agents.AI**: Okvir za orkestraciju agenata na razini poduzeća
- **Integracija GitHub modela**: Obrasci klijenata visokih performansi za API
- **Sustav konfiguracije**: Integracija appsettings.json i okruženja

### Implementacija dizajnerskih obrazaca
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Prikazani obrasci za poduzeća

### 1. **Obrasci stvaranja**
- **Tvornica agenata**: Centralizirano stvaranje agenata s dosljednom konfiguracijom
- **Obrazac graditelja**: Fluentni API za složenu konfiguraciju agenata
- **Obrazac singletona**: Upravljanje zajedničkim resursima i konfiguracijom
- **Injekcija ovisnosti**: Slabo povezivanje i testabilnost

### 2. **Obrasci ponašanja**
- **Obrazac strategije**: Zamjenjive strategije izvršavanja alata
- **Obrazac naredbe**: Inkapsulirane operacije agenata s undo/redo funkcionalnošću
- **Obrazac promatrača**: Upravljanje životnim ciklusom agenata vođeno događajima
- **Obrazac metode predloška**: Standardizirani tijekovi izvršavanja agenata

### 3. **Strukturni obrasci**
- **Obrazac adaptera**: Integracijski sloj za GitHub Models API
- **Obrazac dekoratora**: Poboljšanje sposobnosti agenata
- **Obrazac fasade**: Pojednostavljeni sučelji za interakciju s agentima
- **Obrazac proxyja**: Lijeno učitavanje i predmemoriranje za performanse

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Pristup GitHub Models API-ju

**NuGet ovisnosti:**
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

## 📚 Dizajnerska načela za .NET

### SOLID načela
- **Jedinstvena odgovornost**: Svaka komponenta ima jednu jasnu svrhu
- **Otvoreno/Zatvoreno**: Proširivo bez modifikacije
- **Liskovljeva zamjena**: Implementacije alata temeljene na sučeljima
- **Segregacija sučelja**: Fokusirana, kohezivna sučelja
- **Inverzija ovisnosti**: Oslanjanje na apstrakcije, ne na konkretne implementacije

### Čista arhitektura
- **Sloj domene**: Osnovne apstrakcije agenata i alata
- **Sloj aplikacije**: Orkestracija agenata i tijekovi rada
- **Sloj infrastrukture**: Integracija GitHub modela i vanjskih usluga
- **Sloj prezentacije**: Interakcija s korisnicima i formatiranje odgovora

## 🔒 Razmatranja za poduzeća

### Sigurnost
- **Upravljanje vjerodajnicama**: Sigurno rukovanje API ključevima uz IConfiguration
- **Validacija unosa**: Jako tipiziranje i validacija podataka
- **Sanitizacija izlaza**: Sigurno procesiranje i filtriranje odgovora
- **Zapisivanje revizije**: Sveobuhvatno praćenje operacija

### Performanse
- **Asinkroni obrasci**: Operacije bez blokiranja I/O-a
- **Pooliranje veza**: Učinkovito upravljanje HTTP klijentima
- **Predmemoriranje**: Predmemoriranje odgovora za poboljšane performanse
- **Upravljanje resursima**: Pravilno odlaganje i obrasci čišćenja

### Skalabilnost
- **Sigurnost za niti**: Podrška za istovremeno izvršavanje agenata
- **Pooliranje resursa**: Učinkovito korištenje resursa
- **Upravljanje opterećenjem**: Ograničavanje brzine i rukovanje povratnim pritiskom
- **Praćenje**: Metrike performansi i provjere zdravlja

## 🚀 Produkcijsko postavljanje

- **Upravljanje konfiguracijom**: Postavke specifične za okruženje
- **Strategija zapisivanja**: Strukturirano zapisivanje s ID-ovima za korelaciju
- **Upravljanje pogreškama**: Globalno upravljanje iznimkama s pravilnim oporavkom
- **Praćenje**: Application Insights i brojači performansi
- **Testiranje**: Obrasci za jedinične testove, integracijske testove i testove opterećenja

Spremni za izradu inteligentnih agenata na razini poduzeća s .NET-om? Idemo arhitektirati nešto robusno! 🏢✨

## Primjer koda

Za kompletan radni primjer, pogledajte [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.