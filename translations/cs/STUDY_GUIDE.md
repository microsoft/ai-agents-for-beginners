# AI Agentů pro Začátečníky - Studijní Průvodce a Shrnutí Kurzu

Tento průvodce poskytuje shrnutí kurzu „AI Agentů pro Začátečníky“ a vysvětluje klíčové koncepty, rámce a návrhové vzory pro vytváření AI Agentů.

## 1. Úvod do AI Agentů

**Co jsou AI Agenti?**
AI Agenti jsou systémy, které rozšiřují schopnosti Velkých Jazykových Modelů (LLM) tím, že jim poskytují přístup k **nástrojům**, **znalostem** a **paměti**. Na rozdíl od standardního chatbotu s LLM, který pouze generuje text na základě tréninkových dat, AI Agent může:
- **Vnímat** své prostředí (pomocí senzorů nebo vstupů).
- **Uvažovat** o tom, jak vyřešit problém.
- **Jednat**, aby změnil prostředí (pomocí aktorů nebo vykonávání nástrojů).

**Klíčové součásti Agenta:**
- **Prostředí**: Prostor, kde agent působí (např. rezervační systém).
- **Senzory**: Mechanismy pro sběr informací (např. čtení API).
- **Aktory**: Mechanismy pro provádění akcí (např. odeslání emailu).
- **Mozek (LLM)**: Rozumový modul, který plánuje a rozhoduje, jaké akce provést.

## 2. Agentní Rámce

Kurz používá **Microsoft Agent Framework (MAF)** spolu s **Azure AI Foundry Agent Service V2** pro vytváření agentů:

| Komponenta | Zaměření | Nejvhodnější pro |
|------------|----------|------------------|
| **Microsoft Agent Framework** | Jednotné Python/C# SDK pro agenty, nástroje a pracovní toky | Vytváření agentů s nástroji, workflow multi-agentů a produkčních vzorů. |
| **Azure AI Foundry Agent Service** | Spravovaný cloudový runtime | Bezpečné, škálovatelné nasazení s vestavěnou správou stavu, dohledatelností a důvěrou. |

## 3. Agentní Návrhové Vzory

Návrhové vzory pomáhají strukturovat způsob, jakým agenti fungují k spolehlivému řešení problémů.

### **Vzorec Použití Nástroje** (Lekce 4)
Tento vzor umožňuje agentům interakci s vnějším světem.
- **Koncept**: Agent má k dispozici „schéma“ (seznam dostupných funkcí a jejich parametrů). LLM rozhoduje, *který* nástroj zavolat a s *jakými* argumenty na základě uživatelského požadavku.
- **Průběh**: Uživatelský požadavek -> LLM -> **Výběr nástroje** -> **Provedení nástroje** -> LLM (s výstupem nástroje) -> Konečná odpověď.
- **Případy použití**: Získávání aktuálních dat (počasí, ceny akcií), provádění výpočtů, spouštění kódu.

### **Plánovací Vzor** (Lekce 7)
Tento vzor umožňuje agentům řešit složité úkoly ve více krocích.
- **Koncept**: Agent rozloží vysoce úroveň cíl na posloupnost menších dílčích úkolů.
- **Přístupy**:
  - **Dekompozice úkolu**: Rozdělení „Naplánuj cestu“ na „Rezervuj let“, „Rezervuj hotel“, „Půjč auto“.
  - **Iterativní plánování**: Přehodnocení plánu na základě výsledků předchozích kroků (např. pokud je let plný, vyber jiný termín).
- **Implementace**: Často zahrnuje „Plánovacího“ agenta, který generuje strukturovaný plán (např. JSON), který pak vykonávají ostatní agenti.

## 4. Principy Návrhu

Při navrhování agentů zvažte tři rozměry:
- **Prostor**: Agenti by měli propojit lidi a znalosti, být přístupní, ale nenápadní.
- **Čas**: Agenti by se měli učit z *minulosti*, poskytovat relevantní pobídky *teď* a přizpůsobovat se pro *budoucnost*.
- **Jádro**: Přijměte nejistotu, ale budujte důvěru skrze transparentnost a kontrolu uživatele.

## 5. Shrnutí Klíčových Lekcí

- **Lekce 1**: Agenti jsou systémy, ne jen modely. Vnímají, uvažují a jednají.
- **Lekce 2**: Microsoft Agent Framework abstrahuje složitost volání nástrojů a správy stavu.
- **Lekce 3**: Navrhujte s důrazem na transparentnost a kontrolu uživatele.
- **Lekce 4**: Nástroje jsou „ruce“ agenta. Definice schématu je klíčová, aby LLM pochopil, jak je používat.
- **Lekce 7**: Plánování je „výkonná funkce“ agenta, která mu umožňuje řešit složité pracovní toky.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, uvědomte si prosím, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->