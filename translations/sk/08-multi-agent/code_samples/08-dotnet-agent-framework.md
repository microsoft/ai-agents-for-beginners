<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:18:34+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🤝 Podnikové systémy pracovných postupov s viacerými agentmi (.NET)

## 📋 Ciele učenia

Tento notebook ukazuje, ako vytvoriť sofistikované podnikové systémy s viacerými agentmi pomocou Microsoft Agent Framework v .NET s modelmi GitHub. Naučíte sa orchestráciu viacerých špecializovaných agentov, ktorí spolupracujú prostredníctvom štruktúrovaných pracovných postupov, využívajúc podnikové funkcie .NET pre riešenia pripravené na produkciu.

**Podnikové schopnosti s viacerými agentmi, ktoré si osvojíte:**
- 👥 **Spolupráca agentov**: Typovo bezpečná koordinácia agentov s validáciou počas kompilácie
- 🔄 **Orchestrácia pracovných postupov**: Deklaratívna definícia pracovných postupov s asynchrónnymi vzormi .NET
- 🎭 **Špecializácia rolí**: Silne typované osobnosti agentov a oblasti odbornosti
- 🏢 **Podniková integrácia**: Vzory pripravené na produkciu s monitorovaním a spracovaním chýb

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Azure predplatné (pre perzistentných agentov)

**Požadované balíčky NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Ukážka kódu

Kompletný funkčný kód pre túto lekciu je dostupný v priloženom súbore C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Na spustenie ukážky:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Alebo pomocou .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Čo táto ukážka demonštruje

Tento systém pracovných postupov s viacerými agentmi vytvára odporúčaciu službu pre hotelové cestovanie s dvoma špecializovanými agentmi:

1. **Agent recepcie**: Cestovný agent, ktorý poskytuje odporúčania na aktivity a lokality
2. **Agent concierge**: Prehodnocuje odporúčania, aby zabezpečil autentické, neturistické zážitky

Agentí spolupracujú v pracovnom postupe, kde:
- Agent recepcie prijíma počiatočnú požiadavku na cestovanie
- Agent concierge prehodnocuje a zdokonaľuje odporúčanie
- Pracovný postup streamuje odpovede v reálnom čase

## Kľúčové koncepty

### Koordinácia agentov
Ukážka demonštruje typovo bezpečnú koordináciu agentov pomocou Microsoft Agent Framework s validáciou počas kompilácie.

### Orchestrácia pracovných postupov
Používa deklaratívnu definíciu pracovných postupov s asynchrónnymi vzormi .NET na prepojenie viacerých agentov v pipeline.

### Streamovanie odpovedí
Implementuje streamovanie odpovedí agentov v reálnom čase pomocou asynchrónnych enumerácií a architektúry riadenej udalosťami.

### Podniková integrácia
Ukazuje vzory pripravené na produkciu vrátane:
- Konfigurácie prostredníctvom environmentálnych premenných
- Bezpečného spravovania poverení
- Spracovania chýb
- Asynchrónneho spracovania udalostí

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.