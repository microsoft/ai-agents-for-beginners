# AI agenti pre začiatočníkov - študijný sprievodca a zhrnutie kurzu

Tento sprievodca poskytuje zhrnutie kurzu „AI agenti pre začiatočníkov“ a vysvetľuje kľúčové koncepty, rámce a návrhové vzory na tvorbu AI agentov.

## 1. Úvod do AI agentov

**Čo sú AI agenti?**
AI agenti sú systémy, ktoré rozširujú schopnosti veľkých jazykových modelov (LLM) tým, že im poskytujú prístup k **nástrojom**, **vedomostiam** a **pamäti**. Na rozdiel od štandardného chatbotu založeného na LLM, ktorý iba generuje text na základe tréningových dát, AI agent môže:
- **Vnímať** svoje prostredie (prostredníctvom senzorov alebo vstupov).
- **Uvažovať** o tom, ako vyriešiť problém.
- **Konat’** na zmenu prostredia (prostredníctvom aktivátorov alebo vykonávania nástrojov).

**Kľúčové komponenty agenta:**
- **Prostredie**: Priestor, kde agent pôsobí (napr. rezervačný systém).
- **Senzory**: Mechanizmy na získavanie informácií (napr. čítanie API).
- **Aktivátory**: Mechanizmy na vykonávanie akcií (napr. odoslanie e-mailu).
- **Mozog (LLM)**: Logický engine, ktorý plánuje a rozhoduje, ktoré akcie vykonať.

## 2. Agentné rámce

Kurz používa **Microsoft Agent Framework (MAF)** s **Azure AI Foundry Agent Service V2** na tvorbu agentov:

| Komponent | Zameranie | Najlepšie pre |
|-----------|-----------|---------------|
| **Microsoft Agent Framework** | Jednotné Python/C# SDK pre agentov, nástroje a pracovné postupy | Tvorbu agentov s nástrojmi, viacagentné workflow a produkčné vzory. |
| **Azure AI Foundry Agent Service** | Spravované cloudové runtime | Bezpečné, škálovateľné nasadenie s vstavaným manažmentom stavu, sledovateľnosťou a dôverou. |

## 3. Návrhové vzory pre agentov

Návrhové vzory pomáhajú štrukturovať spôsob, akým agenti spoľahlivo riešia problémy.

### **Vzorec použitia nástroja** (Lekcia 4)
Tento vzorec umožňuje agentom komunikovať s vonkajším svetom.
- **Koncept**: Agent dostane „schému“ (zoznam dostupných funkcií a ich parametrov). LLM rozhoduje, *ktorý* nástroj zavolať a s *akými* argumentmi na základe požiadavky používateľa.
- **Proces**: Požiadavka používateľa -> LLM -> **Výber nástroja** -> **Vykonanie nástroja** -> LLM (s výstupom nástroja) -> Konečná odpoveď.
- **Použitie**: Získavanie aktuálnych dát (počasie, ceny akcií), vykonávanie výpočtov, spúšťanie kódu.

### **Vzorec plánovania** (Lekcia 7)
Tento vzorec umožňuje agentom riešiť komplexné, viacstupňové úlohy.
- **Koncept**: Agent rozkladá cieľ na sekvenciu menších podúloh.
- **Prístupy**:
  - **Rozklad úlohy**: Rozdelenie „Naplánuj výlet“ na „Rezervuj let“, „Rezervuj hotel“, „Požičiavanie auta“.
  - **Iteratívne plánovanie**: Prehodnocovanie plánu na základe výstupov predchádzajúcich krokov (napr. ak je let plný, vybrať iný dátum).
- **Implementácia**: Často zahŕňa agenta „plánovača“, ktorý generuje štruktúrovaný plán (napr. JSON), ktorý potom vykonávajú iní agenti.

## 4. Návrhové princípy

Pri navrhovaní agentov zvážte tri dimenzie:
- **Priestor**: Agenti by mali prepájať ľudí a vedomosti, byť prístupní, ale nenápadní.
- **Čas**: Agenti by sa mali učiť z *minulosti*, poskytovať relevantné podnety v *prítomnosti* a prispôsobovať sa pre *budúcnosť*.
- **Jadro**: Prijmite neistotu, ale budujte dôveru prostredníctvom transparentnosti a kontroly používateľa.

## 5. Zhrnutie kľúčových lekcií

- **Lekcia 1**: Agenti sú systémy, nie len modely. Vnímajú, uvažujú a konajú.
- **Lekcia 2**: Microsoft Agent Framework abstrahuje zložitosť volania nástrojov a správy stavu.
- **Lekcia 3**: Navrhujte so zameraním na transparentnosť a používateľskú kontrolu.
- **Lekcia 4**: Nástroje sú „ruky“ agenta. Definícia schémy je zásadná, aby LLM rozumelo, ako ich používať.
- **Lekcia 7**: Plánovanie je „výkonná funkcia“ agenta, ktorá mu umožňuje zvládať zložité pracovné postupy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho materinskom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->