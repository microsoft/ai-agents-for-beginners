# AI agentai pradedantiesiems – mokymosi vadovas ir kurso santrauka

Šis vadovas pateikia „AI agentai pradedantiesiems“ kurso santrauką ir paaiškina pagrindines sąvokas, sistemas ir dizaino šablonus, skirtus AI agentų kūrimui.

## 1. Įvadas į AI agentus

**Kas yra AI agentai?**
AI agentai yra sistemos, kurios išplečia Didžiųjų kalbos modelių (LLM) galimybes suteikdamos jiems prieigą prie **įrankių**, **žinių** ir **atminties**. Skirtingai nei standartinis LLM pokalbių robotas, kuris tik generuoja tekstą remdamasis mokymo duomenimis, AI agentas gali:
- **Suvokti** savo aplinką (per jutiklius ar įvestį).
- **Mąstyti** apie tai, kaip išspręsti problemą.
- **Veikti**, kad pakeistų aplinką (per aktyvatorius ar įrankių vykdymą).

**Pagrindinės agente sudedamosios dalys:**
- **Aplinka**: erdvė, kurioje agentas veikia (pvz., užsakymų sistema).
- **Jutikliai**: mechanizmai informacijos rinkimui (pvz., API skaitymas).
- **Aktyvatoriai**: mechanizmai veiksmams atlikti (pvz., el. pašto siuntimas).
- **Smegenys (LLM)**: mąstymo variklis, kuris planuoja ir nusprendžia, kokius veiksmus atlikti.

## 2. Agentų sistemos

Kursas naudoja **Microsoft Agent Framework (MAF)** su **Azure AI Foundry Agent Service V2**, skirtą agentams kurti:

| Sudedamoji dalis | Dėmesys | Geriausia |
|------------------|---------|-----------|
| **Microsoft Agent Framework** | Vieningas Python/C# SDK agentams, įrankiams ir darbų srautams | Agentų kūrimui su įrankiais, daugiagentinių darbų srautų valdymui ir gamybos šablonams. |
| **Azure AI Foundry Agent Service** | Valdomoji debesijos vykdymo aplinka | Saugiam, masteliu pritaikomam diegimui su integruotu būsenos valdymu, stebėjimu ir patikimumu. |

## 3. Agentų dizaino šablonai

Dizaino šablonai padeda struktūruoti, kaip agentai veikia, kad patikimai spręstų problemas.

### **Įrankių naudojimo šablonas** (4 pamoka)
Šis šablonas leidžia agentams bendrauti su išoriniu pasauliu.
- **Sąvoka**: agentui suteikiamas „schema“ (galimų funkcijų ir jų parametrų sąrašas). LLM nusprendžia, *kurį* įrankį kviesti ir su *kokiais* argumentais, atsižvelgdamas į vartotojo užklausą.
- **Procesas**: Vartotojo užklausa -> LLM -> **Įrankio pasirinkimas** -> **Įrankio vykdymas** -> LLM (su įrankio išvestimi) -> Galutinis atsakymas.
- **Panaudojimo atvejai**: realaus laiko duomenų gavimas (oras, akcijų kainos), skaičiavimų atlikimas, kodo vykdymas.

### **Planavimo šablonas** (7 pamoka)
Šis šablonas leidžia agentams spręsti sudėtingas, daugiasluoksnes užduotis.
- **Sąvoka**: agentas suskaido aukšto lygio tikslą į mažesnes tarpines užduotis.
- **Požiūriai**:
  - **Užduoties skaidymas**: pvz., „Suplanuoti kelionę“ į „Užsakyti skrydį“, „Užsakyti viešbutį“, „Išsinuomoti automobilį“.
  - **Iteratyvus planavimas**: planas peržiūrimas pagal ankstesnių žingsnių rezultatus (pvz., jei skrydis pilnas, pasirenkama kita data).
- **Įgyvendinimas**: dažnai ūkinis agentas „Planuotojas“, kuris generuoja struktūruotą planą (pvz., JSON), kuris vėliau vykdomas kitų agentų.

## 4. Dizaino principai

Kuriant agentus, atsižvelkite į tris dimensijas:
- **Erdvė**: agentai turėtų jungti žmones ir žinias, būti prieinami, bet nepastebimi.
- **Laikas**: agentai turėtų mokytis iš *praeities*, pateikti tinkamus paskatinimus *dabar* ir prisitaikyti prie *ateities*.
- **Branduolys**: priimti neapibrėžtumą, bet užtikrinti pasitikėjimą per skaidrumą ir vartotojo kontrolę.

## 5. Pagrindinių pamokų santrauka

- **1 pamoka**: Agentai yra sistemos, ne tik modeliai. Jie suvokia, mąsto ir veikia.
- **2 pamoka**: Microsoft Agent Framework abstrahuoja sudėtingumą skambinant įrankiams ir valdyti būseną.
- **3 pamoka**: Kuriant reikėtų galvoti apie skaidrumą ir vartotojo kontrolę.
- **4 pamoka**: Įrankiai yra agento „rankos“. Schema yra būtina, kad LLM suprastų, kaip juos naudoti.
- **7 pamoka**: Planavimas yra agento „vykdomoji funkcija“, leidžianti jiems spręsti sudėtingus darbų srautus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai rekomenduojama pasitelkti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->