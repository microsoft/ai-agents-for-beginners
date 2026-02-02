# AI agenti pre začiatočníkov - študijný sprievodca a súhrn kurzu

Tento sprievodca poskytuje súhrn kurzu "AI agenti pre začiatočníkov" a vysvetľuje kľúčové koncepty, rámce a návrhové vzory pre budovanie AI agentov.

## 1. Úvod do AI agentov

**Čo sú AI agenti?**
AI agenti sú systémy, ktoré rozširujú schopnosti veľkých jazykových modelov (LLM) tým, že im umožňujú prístup k **nástrojom**, **znalostiam** a **pamäti**. Na rozdiel od bežného chatbotu založeného na LLM, ktorý len generuje text na základe tréningových dát, AI agent dokáže:
- **Vnímať** svoje prostredie (pomocou senzorov alebo vstupov).
- **Rozmýšľať** nad tým, ako vyriešiť problém.
- **Konať**, aby zmenil prostredie (pomocou akčných členov alebo vykonávania nástrojov).

**Kľúčové komponenty agenta:**
- **Prostredie**: Priestor, kde agent pôsobí (napr. rezervačný systém).
- **Senzory**: Mechanizmy na zbieranie informácií (napr. čítanie API).
- **Akčné členy**: Mechanizmy na vykonávanie akcií (napr. odosielanie e-mailu).
- **Mozog (LLM)**: Rozhodovací motor, ktorý plánuje a rozhoduje, aké akcie vykonať.

## 2. Agentné rámce

Kurz pokrýva tri hlavné rámce na budovanie agentov:

| Rámec | Zameranie | Najvhodnejšie pre |
|-----------|-------|----------|
| **Semantic Kernel** | Produkčne pripravené SDK pre .NET/Python | Podnikové aplikácie, integrácia AI s existujúcim kódom. |
| **AutoGen** | Spolupráca viacerých agentov | Zložité scenáre vyžadujúce viacerých špecializovaných agentov komunikujúcich medzi sebou. |
| **Azure AI Agent Service** | Spravovaná cloud služba | Bezpečné, škálovateľné nasadenie so zabudovaným manažmentom stavu. |

## 3. Agentné návrhové vzory

Návrhové vzory pomáhajú štruktúrovať fungovanie agentov tak, aby spoľahlivo riešili problémy.

### **Návrhový vzor použitia nástrojov** (Lekcia 4)
Tento vzor umožňuje agentom interagovať s vonkajším svetom.
- **Koncept**: Agent dostane "schému" (zoznam dostupných funkcií a ich parametrov). LLM rozhoduje, *ktorý* nástroj použiť a s *akými* argumentmi na základe požiadavky používateľa.
- **Tok**: Požiadavka používateľa -> LLM -> **Výber nástroja** -> **Vykonanie nástroja** -> LLM (s výstupom z nástroja) -> Konečná odpoveď.
- **Použitie**: Získavanie aktuálnych dát (počasie, ceny akcií), vykonávanie výpočtov, spúšťanie kódu.

### **Návrhový vzor plánovania** (Lekcia 7)
Tento vzor umožňuje agentom riešiť zložité, viacstupňové úlohy.
- **Koncept**: Agent rozkladá všeobecný cieľ na postupnosť menších podúloh.
- **Prístupy**:
  - **Dezaggregácia úlohy**: Rozdelenie "Naplánuj cestu" na "Rezervuj let", "Rezervuj hotel", "Požičiavka auta".
  - **Iteratívne plánovanie**: Prehodnocovanie plánu na základe výstupov predchádzajúcich krokov (napr. ak je let plný, vybrať iný dátum).
- **Implementácia**: Často zahŕňa "planner" agenta, ktorý generuje štruktúrovaný plán (napr. JSON), ktorý následne vykonávajú ostatní agenti.

## 4. Návrhové princípy

Pri návrhu agentov zvážte tri dimenzie:
- **Priestor**: Agenti by mali prepájať ľudí so znalosťami, byť prístupní, ale nenápadní.
- **Čas**: Agenti by sa mali učiť z *minulosti*, poskytovať vhodné podnety *teraz* a prispôsobovať sa pre *budúcnosť*.
- **Jadro**: Prijmite neistotu, ale vybudujte dôveru prostredníctvom transparentnosti a kontroly používateľa.

## 5. Súhrn kľúčových lekcií

- **Lekcia 1**: Agenti sú systémy, nielen modely. Vnímajú, rozmýšľajú a konajú.
- **Lekcia 2**: Rámce ako Semantic Kernel a AutoGen zjednodušujú volanie nástrojov a manažment stavu.
- **Lekcia 3**: Navrhujte s ohľadom na transparentnosť a kontrolu používateľa.
- **Lekcia 4**: Nástroje sú "ruky" agenta. Definícia schémy je kľúčová, aby LLM vedel, ako ich používať.
- **Lekcia 7**: Plánovanie je "výkonná funkcia" agenta, ktorá mu umožňuje riešiť zložité pracovné toky.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->