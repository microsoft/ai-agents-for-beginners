<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:28:44+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🛠️ Napredno korištenje alata s GitHub modelima (.NET)

## 📋 Ciljevi učenja

Ovaj notebook prikazuje obrasce integracije alata na razini poduzeća koristeći Microsoft Agent Framework u .NET-u s GitHub modelima. Naučit ćete kako izgraditi sofisticirane agente s više specijaliziranih alata, koristeći snažno tipiziranje C# jezika i značajke .NET-a za poduzeća.

**Napredne mogućnosti alata koje ćete savladati:**
- 🔧 **Arhitektura s više alata**: Izgradnja agenata s više specijaliziranih funkcionalnosti
- 🎯 **Izvršavanje alata uz sigurnost tipova**: Iskorištavanje C# provjere u vrijeme kompilacije
- 📊 **Obrasci alata za poduzeća**: Dizajn alata spreman za produkciju i upravljanje greškama
- 🔗 **Kompozicija alata**: Kombiniranje alata za složene poslovne procese

## 🎯 Prednosti arhitekture alata u .NET-u

### Značajke alata za poduzeća
- **Provjera u vrijeme kompilacije**: Snažno tipiziranje osigurava ispravnost parametara alata
- **Ubrizgavanje ovisnosti**: Integracija IoC spremnika za upravljanje alatima
- **Async/Await obrasci**: Izvršavanje alata bez blokiranja uz pravilno upravljanje resursima
- **Strukturirano logiranje**: Ugrađena integracija za praćenje izvršavanja alata

### Obrasci spremni za produkciju
- **Upravljanje iznimkama**: Sveobuhvatno upravljanje greškama uz tipizirane iznimke
- **Upravljanje resursima**: Pravilni obrasci za oslobađanje resursa i upravljanje memorijom
- **Praćenje performansi**: Ugrađene metrike i brojači performansi
- **Upravljanje konfiguracijom**: Sigurna konfiguracija uz provjeru valjanosti

## 🔧 Tehnička arhitektura

### Osnovne komponente alata u .NET-u
- **Microsoft.Extensions.AI**: Jedinstveni sloj apstrakcije alata
- **Microsoft.Agents.AI**: Orkestracija alata na razini poduzeća
- **Integracija GitHub modela**: Klijent visokih performansi za API s bazenom veza

### Cjevovod za izvršavanje alata
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategorije alata i obrasci

### 1. **Alati za obradu podataka**
- **Provjera unosa**: Snažno tipiziranje uz podatkovne anotacije
- **Operacije transformacije**: Sigurna konverzija i formatiranje podataka
- **Poslovna logika**: Alati za domensko specifične izračune i analize
- **Formatiranje izlaza**: Generiranje strukturiranih odgovora

### 2. **Alati za integraciju**
- **API konektori**: Integracija RESTful servisa s HttpClient-om
- **Alati za baze podataka**: Integracija Entity Frameworka za pristup podacima
- **Operacije s datotekama**: Sigurne operacije datotečnog sustava uz provjeru valjanosti
- **Vanjske usluge**: Obrasci za integraciju usluga trećih strana

### 3. **Alati za pomoćne funkcije**
- **Obrada teksta**: Manipulacija i formatiranje stringova
- **Operacije s datumima/vremenom**: Izračuni datuma/vremena uz kulturološku svijest
- **Matematički alati**: Precizni izračuni i statističke operacije
- **Alati za provjeru**: Provjera poslovnih pravila i validacija podataka

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Pristup GitHub Models API-ju

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okruženja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Spremni za izgradnju agenata na razini poduzeća s moćnim, sigurnim alatima u .NET-u? Idemo arhitektirati profesionalna rješenja! 🏢⚡

## 💻 Implementacija koda

Kompletna implementacija u C# dostupna je u pratećoj datoteci `04-dotnet-agent-framework.cs`. Ova .NET aplikacija u jednoj datoteci demonstrira:

- Učitavanje varijabli okruženja za konfiguraciju GitHub modela
- Definiranje prilagođenih alata koristeći C# metode s atributima
- Kreiranje AI agenta s integracijom alata
- Upravljanje nitima razgovora
- Izvršavanje zahtjeva agenta uz pozivanje alata

Za pokretanje primjera:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ili koristeći .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.