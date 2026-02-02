# AI Agenti pro začátečníky - studie a shrnutí kurzu

Tato příručka poskytuje shrnutí kurzu „AI Agenti pro začátečníky“ a vysvětluje klíčové pojmy, rámce a návrhové vzory pro vytváření AI Agentů.

## 1. Úvod do AI Agentů

**Co jsou AI Agenti?**  
AI Agenti jsou systémy, které rozšiřují schopnosti Velkých jazykových modelů (LLM) tím, že jim poskytují přístup k **nástrojům**, **znalostem** a **paměti**. Na rozdíl od standardního chatbotu založeného na LLM, který pouze generuje text na základě tréninkových dat, AI Agent může:  
- **Vnímat** své prostředí (prostřednictvím senzorů nebo vstupů).  
- **Uvažovat** o tom, jak vyřešit problém.  
- **Jednat** za účelem změny prostředí (pomocí aktivátorů nebo provádění nástrojů).

**Klíčové složky agenta:**  
- **Prostředí**: Prostor, ve kterém agent operuje (např. rezervační systém).  
- **Senzory**: Mechanismy pro sběr informací (např. čtení API).  
- **Aktivátory**: Mechanismy pro vykonávání akcí (např. odesílání e-mailu).  
- **Mozek (LLM)**: Motor uvažování, který plánuje a rozhoduje o tom, jaké akce provést.

## 2. Agentické rámce

Kurz pokrývá tři hlavní rámce pro tvorbu agentů:

| Rámec | Zaměření | Nejlepší pro |
|-------|----------|-------------|
| **Semantic Kernel** | Produkčně připravené SDK pro .NET/Python | Podnikové aplikace, integrace AI s existujícím kódem. |
| **AutoGen** | Spolupráce více agentů | Složité scénáře vyžadující více specializovaných agentů komunikujících mezi sebou. |
| **Azure AI Agent Service** | Spravovaná cloudová služba | Bezpečné, škálovatelné nasazení s vestavěnou správou stavu. |

## 3. Agentické návrhové vzory

Návrhové vzory pomáhají strukturovat, jak agenti fungují, aby spolehlivě řešili problémy.

### **Vzor používání nástrojů** (Lekce 4)  
Tento vzor umožňuje agentům interakci s vnějším světem.  
- **Koncept**: Agentovi je poskytnut „schéma“ (seznam dostupných funkcí a jejich parametrů). LLM rozhoduje, *který* nástroj zavolat a s *jakými* argumenty na základě uživatelského požadavku.  
- **Průběh**: Uživatelský požadavek -> LLM -> **Výběr nástroje** -> **Spuštění nástroje** -> LLM (s výstupem nástroje) -> Konečná odpověď.  
- **Použití**: Získávání aktuálních dat (počasí, ceny akcií), provádění výpočtů, spouštění kódu.

### **Vzor plánování** (Lekce 7)  
Tento vzor umožňuje agentům řešit složité, vícestupňové úkoly.  
- **Koncept**: Agent rozdělí cíl vysoké úrovně na posloupnost menších dílčích úkolů.  
- **Přístupy**:  
  - **Rozklad úkolu**: Rozdělení „Naplánuj cestu“ na „Rezervuj let“, „Rezervuj hotel“, „Půjč auto“.  
  - **Iterativní plánování**: Opakované přehodnocování plánu na základě výstupů předchozích kroků (např. pokud je let plný, vybrat jiný termín).  
- **Implementace**: Často zahrnuje agenta „Plánovače“, který generuje strukturovaný plán (např. JSON), který pak vykonávají další agenti.

## 4. Návrhové principy

Při návrhu agentů zvažte tři dimenze:  
- **Prostor**: Agent by měl spojovat lidi a znalosti, být přístupný, ale nenápadný.  
- **Čas**: Agent by se měl učit z *minulosti*, poskytovat relevantní pobídky *nyní* a přizpůsobovat se *budoucnosti*.  
- **Jádro**: Přijměte nejistotu, ale budujte důvěru pomocí transparentnosti a uživatelské kontroly.

## 5. Shrnutí klíčových lekcí

- **Lekce 1**: Agent jsou systémy, ne jen modely. Vnímají, uvažují a jednají.  
- **Lekce 2**: Rámce jako Semantic Kernel a AutoGen abstraktně vyřizují složitost volání nástrojů a správu stavu.  
- **Lekce 3**: Návrh s důrazem na transparentnost a uživatelskou kontrolu.  
- **Lekce 4**: Nástroje jsou „ruce“ agenta. Definice schématu je klíčová pro porozumění, jak je LLM použije.  
- **Lekce 7**: Plánování je „výkonná funkce“ agenta, která mu umožňuje řešit složité postupy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->