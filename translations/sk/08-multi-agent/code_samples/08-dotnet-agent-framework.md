# 🤝 Podnikové multi-agentné pracovné systémy (.NET)

## 📋 Ciele učenia

Tento notebook ukazuje, ako vytvoriť sofistikované podnikové multi-agentné systémy pomocou Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte sa orchestráciu viacerých špecializovaných agentov, ktorí pracujú spolu prostredníctvom štruktúrovaných pracovných tokov, pričom využijete podnikové funkcie .NET pre produkčne pripravené riešenia.

**Podnikové multi-agentné schopnosti, ktoré si vybudujete:**
- 👥 **Spolupráca agentov**: Typovo bezpečná koordinácia agentov s kontrolou počas kompilácie
- 🔄 **Orchestrace pracovného toku**: Deklaratívna definícia pracovného toku s asynchrónnymi vzormi .NET
- 🎭 **Špecializácia rolí**: Silne typované osobnosti agentov a domény odbornosti
- 🏢 **Podniková integrácia**: Produkčne pripravené vzory s monitorovaním a spracovaním chýb

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo novší
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Predplatné Azure (pre perzistentných agentov)

**Povinné NuGet balíčky:**
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

## Ukážka kódu

Kompletný funkčný kód pre túto lekciu je dostupný v doplnkovom súbore C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Ako spustiť ukážku:

```bash
# Urobte súbor spustiteľným (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Spustite príklad
./08-dotnet-agent-framework.cs
```

Alebo pomocou .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Čo táto ukážka demonštruje

Tento multi-agentný pracovný systém vytvára odporúčací servis pre hotelové cestovanie so dvoma špecializovanými agentmi:

1. **Agent FrontDesk**: Cestovný agent poskytujúci odporúčania aktivít a lokalít
2. **Agent Concierge**: Skúma odporúčania, aby zabezpečil autentické, neturistické zážitky

Agenti spolupracujú v pracovnom toku, kde:
- Agent FrontDesk prijíma počiatočnú cestovnú požiadavku
- Agent Concierge kontroluje a vylepšuje odporúčanie
- Pracovný tok v reálnom čase streamuje odpovede

## Kľúčové koncepty

### Koordinácia agentov
Ukážka demonštruje typovo bezpečnú koordináciu agentov pomocou Microsoft Agent Framework s kontrolou počas kompilácie.

### Orchestrace pracovného toku
Používa deklaratívnu definíciu pracovného toku s asynchrónnymi vzormi .NET na prepojenie viacerých agentov v pipeline.

### Streamovanie odpovedí
Implementuje streamovanie odpovedí agentov v reálnom čase použitím asynchrónnych enumerables a event-driven architektúry.

### Podniková integrácia
Ukazuje produkčne pripravené vzory vrátane:
- Konfigurácie prostredia cez premenné
- Bezpečného spravovania poverení
- Spracovania chýb
- Asynchrónneho spracovania udalostí

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->