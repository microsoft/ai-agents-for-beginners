# AI agentai pradedantiesiems – studijų vadovas ir kurso santrauka

Šis vadovas pateikia „AI agentai pradedantiesiems“ kurso santrauką ir paaiškina pagrindines sąvokas, sistemas bei dizaino modelius AI agentų kūrimui.

## 1. Įvadas į AI agentus

**Kas yra AI agentai?**  
AI agentai yra sistemos, kurios plečia didelių kalbos modelių (LLM) galimybes suteikdamos jiems prieigą prie **įrankių**, **žinių** ir **atminties**. Skirtingai nuo standartinio LLM pokalbių roboto, kuris tik generuoja tekstą remdamasis mokymo duomenimis, AI agentas gali:  
- **Suvokti** savo aplinką (per jutiklius ar įėjimus).  
- **Mąstyti**, kaip išspręsti problemą.  
- **Veikti**, kad pakeistų aplinką (per veikėjus arba įrankių vykdymą).

**Pagrindinės agento sudedamosios dalys:**  
- **Aplinka**: vieta, kurioje agentas veikia (pvz., rezervavimo sistema).  
- **Jutikliai**: mechanizmai informacijos rinkimui (pvz., API skaitymas).  
- **Veikėjai**: mechanizmai veiksmams atlikti (pvz., el. laiško siuntimas).  
- **Smegenys (LLM)**: loginis variklis, kuris planuoja ir sprendžia, kokius veiksmus atlikti.

## 2. Agentų sistemos

Kursas naudoja **Microsoft Agent Framework (MAF)** kartu su **Azure AI Foundry Agent Service V2** agentų kūrimui:

| Komponentas                  | Dėmesys                                | Geriausiai tinka                                                     |
|-----------------------------|--------------------------------------|--------------------------------------------------------------------|
| **Microsoft Agent Framework** | Vieningas Python/C# SDK agentams, įrankiams ir darbo eigoms | Agentams su įrankiais, daugiagentėms darbo eigoms ir gamybos modeliams. |
| **Azure AI Foundry Agent Service** | Valdomas debesų vykdymas              | Saugi, plečiama diegimo aplinka su įmontuota būsenos valdymu, stebėjimu ir patikimumu. |

## 3. Agentų dizaino modeliai

Dizaino modeliai padeda struktūrizuoti agentų veikimą, kad jie patikimai spręstų problemas.

### **Įrankių naudojimo modelis** (4 pamoka)  
Šis modelis leidžia agentams sąveikauti su išoriniu pasauliu.  
- **Sąvoka**: agentui pateikiamas „schema“ (galimų funkcijų ir jų parametrų sąrašas). LLM nusprendžia, *kurį* įrankį iškviesti ir su *kokiais* argumentais pagal vartotojo užklausą.  
- **Srautas**: Vartotojo užklausa -> LLM -> **įrankio pasirinkimas** -> **įrankio vykdymas** -> LLM (su įrankio rezultatu) -> galutinis atsakymas.  
- **Panaudojimo atvejai**: realaus laiko duomenų gavimas (oras, akcijų kainos), skaičiavimų atlikimas, kodo vykdymas.

### **Planavimo modelis** (7 pamoka)  
Šis modelis leidžia agentams spręsti sudėtingas, daugiasluoksnes užduotis.  
- **Sąvoka**: agentas skaido aukšto lygio tikslą į mažesnių užduočių seką.  
- **Požiūriai**:  
  - **Užduočių suskaidymas**: „Suplanuoti kelionę“ į „nupirkti lėktuvo bilietą“, „užsakyti viešbutį“, „išsinuomoti automobilį“.  
  - **Iteratyvus planavimas**: plano peržiūra ir koregavimas pagal ankstesnių veiksmų rezultatus (pvz., jei lėktuvas pilnas, pasirinkti kitą datą).  
- **Įgyvendinimas**: dažnai naudojamas „planuotojo“ agentas, kuris generuoja struktūrizuotą planą (pavyzdžiui, JSON formatu), kurį vykdo kiti agentai.

## 4. Dizaino principai

Kuriant agentus, verta atsižvelgti į tris dimensijas:  
- **Erdvė**: agentai turi sujungti žmones ir žinias, būti prieinami, bet nepastebimi.  
- **Laikas**: agentai turi mokytis iš *praeities*, teikti tinkamus paskatinimus *dabar* ir prisitaikyti prie *ateities*.  
- **Branduolys**: priimti neapibrėžtumą, bet užtikrinti pasitikėjimą per skaidrumą ir vartotojo kontrolę.

## 5. Pagrindinių pamokų santrauka

- **1 pamoka**: Agentai yra sistemos, ne tik modeliai. Jie suvokia, mąsto ir veikia.  
- **2 pamoka**: Microsoft Agent Framework supaprastina įrankių iškvietimo ir būsenos valdymo sudėtingumą.  
- **3 pamoka**: Dizainas turi būti skaidrus ir suteikti vartotojui kontrolę.  
- **4 pamoka**: Įrankiai – agento „rankos“. Schema svarbi, kad LLM suprastų, kaip juos naudoti.  
- **7 pamoka**: Planavimas yra agento „vykdomoji funkcija“, leidžianti tvarkyti sudėtingas darbo eigas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turi būti laikomas pagrindiniu šaltiniu. Kritiniais atvejais rekomenduojamas profesionalus žmogiškasis vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->