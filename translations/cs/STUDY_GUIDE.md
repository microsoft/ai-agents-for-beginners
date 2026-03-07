# AI Agent pro začátečníky – studie a shrnutí kurzu

Tato příručka poskytuje shrnutí kurzu „AI Agent pro začátečníky“ a vysvětluje klíčové koncepty, rámce a návrhové šablony pro tvorbu AI Agentů.

## 1. Úvod do AI Agentů

**Co jsou AI Agenti?**  
AI Agenti jsou systémy, které rozšiřují schopnosti velkých jazykových modelů (LLM) tím, že jim poskytují přístup k **nástrojům**, **znalostem** a **paměti**. Na rozdíl od standardního chatbotu založeného na LLM, který pouze generuje text na základě tréninkových dat, AI Agent dokáže:  
- **Vnímat** své prostředí (pomocí senzorů nebo vstupů).  
- **Uvažovat** o tom, jak vyřešit problém.  
- **Jednat** tak, aby změnil prostředí (pomocí aktuátorů nebo vykonávání nástrojů).

**Klíčové součásti agenta:**  
- **Prostředí**: Prostor, ve kterém agent operuje (např. rezervační systém).  
- **Senzory**: Mechanismy pro získávání informací (např. čtení API).  
- **Aktuátory**: Mechanismy pro provádění akcí (např. odesílání e-mailu).  
- **Mozek (LLM)**: Rozumová jednotka, která plánuje a rozhoduje, jaké akce provést.

## 2. Agentní rámce

Kurz využívá **Microsoft Agent Framework (MAF)** s **Azure AI Foundry Agent Service V2** pro tvorbu agentů:

| Komponenta | Zaměření | Nejvhodnější pro |
|------------|----------|------------------|
| **Microsoft Agent Framework** | Jednotné Python/C# SDK pro agenty, nástroje a workflow | Tvorbu agentů s nástroji, multiagentní workflow a produkční vzory. |
| **Azure AI Foundry Agent Service** | Spravované cloudové runtime | Bezpečné, škálovatelné nasazení s vestavěnou správou stavu, observabilitou a důvěrou. |

## 3. Agentní návrhové vzory

Návrhové vzory pomáhají strukturovat fungování agentů tak, aby spolehlivě řešili problémy.

### **Vzor použití nástroje** (Lekce 4)  
Tento vzor umožňuje agentům interagovat s vnějším světem.  
- **Koncept**: Agent má k dispozici „schéma“ (seznam dostupných funkcí a jejich parametrů). LLM rozhoduje, *který* nástroj zavolat a s *jakými* argumenty podle požadavku uživatele.  
- **Tok**: Uživatelský požadavek -> LLM -> **Výběr nástroje** -> **Provedení nástroje** -> LLM (se vstupem z nástroje) -> Konečná odpověď.  
- **Případy použití**: Získávání aktuálních dat (počasí, ceny akcií), provádění výpočtů, spouštění kódu.

### **Vzor plánování** (Lekce 7)  
Tento vzor umožňuje agentům řešit složité, vícestupňové úkoly.  
- **Koncept**: Agent rozkládá vysokou úroveň cíle do sekvence menších dílčích úkolů.  
- **Přístupy**:  
  - **Decompozice úkolu**: Rozdělení „Naplánuj výlet“ na „Rezervuj let“, „Rezervuj hotel“, „Půjč auto“.  
  - **Iterativní plánování**: Přehodnocování plánu na základě výsledků předchozích kroků (např. pokud je let plný, zvol jiný datum).  
- **Implementace**: Často zahrnuje „Plánovač“ agenta, který generuje strukturovaný plán (např. JSON), jenž pak provádějí ostatní agenti.

## 4. Návrhové principy

Při návrhu agentů zvažte tři dimenze:  
- **Prostor**: Agenti by měli propojit lidi a znalosti, být přístupní, ale nenápadní.  
- **Čas**: Agenti se učí z *minulosti*, poskytují relevantní podněty v *přítomnosti* a přizpůsobují se pro *budoucnost*.  
- **Jádro**: Přijměte nejistotu, ale vybudujte důvěru prostřednictvím transparentnosti a kontroly uživatele.

## 5. Shrnutí klíčových lekcí

- **Lekce 1**: Agenti jsou systémy, ne jen modely. Vnímají, uvažují a jednají.  
- **Lekce 2**: Microsoft Agent Framework zjednodušuje volání nástrojů a správu stavu.  
- **Lekce 3**: Navrhujte s transparentností a kontrolou ze strany uživatele.  
- **Lekce 4**: Nástroje jsou „ruce“ agenta. Definice schématu je klíčová pro porozumění LLM, jak je používat.  
- **Lekce 7**: Plánování je „výkonná funkce“ agenta, která mu umožňuje řešit složité workflow.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->