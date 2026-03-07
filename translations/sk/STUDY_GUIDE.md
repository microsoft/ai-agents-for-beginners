# AI Agenti pre Začiatočníkov - Študijný Sprievodca a Súhrn Kurzu

Tento sprievodca poskytuje zhrnutie kurzu "AI Agenti pre Začiatočníkov" a vysvetľuje kľúčové koncepty, rámce a návrhové vzory na tvorbu AI Agentov.

## 1. Úvod do AI Agentov

**Čo sú AI Agenti?**
AI Agenti sú systémy, ktoré rozširujú schopnosti Veľkých Jazykových Modelov (LLM) tým, že im dávajú prístup k **nástrojom**, **vedomostiam** a **pamäti**. Na rozdiel od štandardného chatbotu založeného na LLM, ktorý iba generuje text na základe tréningových dát, AI Agent môže:
- **Vnímať** svoje prostredie (cez senzory alebo vstupy).
- **Rozmýšľať** o tom, ako vyriešiť problém.
- **Konať** na zmenu prostredia (cez aktuátory alebo vykonávanie nástrojov).

**Kľúčové komponenty agenta:**
- **Prostredie**: Priestor, kde agent pôsobí (napr. rezervačný systém).
- **Senzory**: Mechanizmy na získavanie informácií (napr. čítanie API).
- **Aktuátory**: Mechanizmy na vykonávanie akcií (napr. odoslanie emailu).
- **Mozog (LLM)**: Rozhodovací engine, ktorý plánuje a rozhoduje, aké akcie vykonať.

## 2. Agentové Rámce

Kurz používa **Microsoft Agent Framework (MAF)** s **Azure AI Foundry Agent Service V2** na tvorbu agentov:

| Komponent | Zameranie | Najvhodnejšie pre |
|-----------|-----------|-------------------|
| **Microsoft Agent Framework** | Unified Python/C# SDK pre agentov, nástroje a workflowy | Tvorbu agentov s nástrojmi, multi-agentné workflowy a produkčné vzory. |
| **Azure AI Foundry Agent Service** | Spravovaná cloudová runtime | Bezpečné, škálovateľné nasadenie s zabudovaným manažmentom stavu, observabilitou a dôverou. |

## 3. Agentové Návrhové Vzory

Návrhové vzory pomáhajú štruktúrovať, ako agenti fungujú na spoľahlivé riešenie problémov.

### **Vzorec Použitia Nástroja** (Lekcia 4)
Tento vzorec umožňuje agentom komunikovať s vonkajším svetom.
- **Koncept**: Agent má k dispozícii "schému" (zoznam dostupných funkcií a ich parametrov). LLM sa rozhoduje, *ktorý* nástroj zavolať a *s akými* argumentami na základe požiadavky používateľa.
- **Priebeh**: Požiadavka používateľa -> LLM -> **Výber nástroja** -> **Vykonanie nástroja** -> LLM (s výstupom nástroja) -> Konečná odpoveď.
- **Použitia**: Získavanie reálnych dát (počasie, ceny akcií), vykonávanie výpočtov, spúšťanie kódu.

### **Vzorec Plánovania** (Lekcia 7)
Tento vzorec umožňuje agentom riešiť komplexné, viacstupňové úlohy.
- **Koncept**: Agent rozkladá vysokú úlohu na postupnosť menších podúloh.
- **Prístupy**:
  - **Decompozícia úloh**: Rozdelenie "Naplánuj výlet" na "Zarezervuj let", "Zarezervuj hotel", "Požičiavanie auta".
  - **Iteratívne plánovanie**: Prehodnocovanie plánu podľa výsledkov predchádzajúcich krokov (napr. ak je let plný, vybrať iný dátum).
- **Implementácia**: Často zahŕňa "Planner" agenta, ktorý generuje štruktúrovaný plán (napr. JSON), ktorý je potom vykonaný inými agentmi.

## 4. Návrhové princípy

Pri návrhu agentov zvážte tri dimenzie:
- **Priestor**: Agenti by mali spájať ľudí a vedomosti, byť prístupní ale nenápadní.
- **Čas**: Agenti by sa mali učiť z *minulosti*, poskytovať relevantné podnety *teraz* a prispôsobovať sa *budúcnosti*.
- **Jadro**: Prijmite neistotu, ale budujte dôveru cez transparentnosť a kontrolu používateľa.

## 5. Súhrn Kľúčových Lekcií

- **Lekcia 1**: Agenti sú systémy, nie len modely. Vnímajú, rozmýšľajú a konajú.
- **Lekcia 2**: Microsoft Agent Framework abstrahuje komplexnosť volania nástrojov a manažmentu stavu.
- **Lekcia 3**: Navrhujte s transparentnosťou a kontrolou používateľa na mysli.
- **Lekcia 4**: Nástroje sú "ruky" agenta. Definícia schémy je kľúčová, aby LLM vedel, ako ich používať.
- **Lekcia 7**: Plánovanie je "výkonná funkcia" agenta, ktorá mu umožňuje zvládať komplexné workflowy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím vezmite na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->