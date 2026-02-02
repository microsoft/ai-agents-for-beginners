# AI Agentai pradedantiesiems – studijų vadovas ir kurso santrauka

Šis vadovas pateikia „AI Agentai pradedantiesiems“ kurso santrauką ir paaiškina pagrindines sąvokas, sistemas bei dizaino šablonus, skirtus AI Agentų kūrimui.

## 1. Įvadas į AI Agentus

**Kas yra AI Agentai?**  
AI Agentai yra sistemos, kurios išplečia Didelių Kalbos Modelių (DKM) galimybes suteikdamos jiems prieigą prie **įrankių**, **žinių** ir **atminties**. Skirtingai nei standartinis DKM pokalbių robotas, kuris tik generuoja tekstą remdamasis mokymosi duomenimis, AI Agentas gali:
- **Suvokti** savo aplinką (per jutiklius arba įvestis).
- **Mąstyti**, kaip išspręsti problemą.
- **Veikti**, kad pakeistų aplinką (per aktuliatorius arba įrankių vykdymą).

**Pagrindinės Agentų sudedamosios dalys:**  
- **Aplinka**: erdvė, kurioje agentas veikia (pvz., rezervavimo sistema).  
- **Jutikliai**: mechanizmai informacijos rinkimui (pvz., API skaitymas).  
- **Aktuliatoriai**: mechanizmai veiksmams atlikti (pvz., el. laiško siuntimas).  
- **Smegenys (DKM)**: mąstymo variklis, kuris planuoja ir nusprendžia, kokius veiksmus atlikti.

## 2. Agentų sistemos

Kursas apima tris pagrindines agentų kūrimo sistemas:

| Sistema | Fokusas | Geriausia skirta |
|---------|---------|------------------|
| **Semantic Kernel** | Produkcijai paruoštas SDK .NET/Python | Įmonių programoms, AI integracijai su esamu kodu. |
| **AutoGen** | Daugiaagentinė bendradarbiavimas | Sudėtingoms situacijoms, reikalaujančioms kelių specializuotų agentų bendravimo. |
| **Azure AI Agent Service** | Valdoma debesų paslauga | Saugiam, masteliui pritaikytam diegimui su įdiegtu būsenos valdymu. |

## 3. Agentų dizaino šablonai

Dizaino šablonai padeda struktūruoti agentų veikimą, kad problemos būtų patikimai sprendžiamos.

### **Įrankių naudojimo šablonas** (4 pamoka)  
Šis šablonas leidžia agentams bendrauti su išoriniu pasauliu.  
- **Sąvoka**: agentui pateikiama „schema“ (sąrašas prieinamų funkcijų ir jų parametrų). DKM nusprendžia, *kurį* įrankį iškviesti ir su *kokiais* argumentais pagal vartotojo užklausą.  
- **Srautas**: Vartotojo užklausa -> DKM -> **Įrankio pasirinkimas** -> **Įrankio vykdymas** -> DKM (su įrankio rezultatu) -> Galutinis atsakymas.  
- **Naudojimo atvejai**: realaus laiko duomenų gavimas (oras, akcijų kainos), skaičiavimų atlikimas, kodo vykdymas.

### **Planavimo šablonas** (7 pamoka)  
Šis šablonas leidžia agentams spręsti sudėtingas, daug žingsnių turinčias užduotis.  
- **Sąvoka**: agentas suskaido aukšto lygio tikslą į mažesnių užduočių seką.  
- **Požiūriai**:  
  - **Užduočių suskaidymas**: „Planuoti kelionę“ į „Rezervuoti skrydį“, „Rezervuoti viešbutį“, „Išsinuomoti automobilį“.  
  - **Iteratyvus planavimas**: plano peržiūra pagal ankstesnių žingsnių rezultatus (pvz., jei skrydis pilnas, pasirinkti kitą datą).  
- **Įgyvendinimas**: dažnai įtraukiamas „Planner“ agentas, kuris generuoja struktūruotą planą (pvz., JSON), kurį vėliau vykdo kiti agentai.

## 4. Dizaino principai

Kuriant agentus, svarbu atsižvelgti į tris dimensijas:  
- **Erdvė**: agentai turėtų jungti žmones ir žinias, būti prieinami, bet neįkyrūs.  
- **Laikas**: agentai turėtų mokytis iš *praeities*, suteikti aktualius paskatinimus *dabartyje*, ir prisitaikyti *ateičiai*.  
- **Branduolys**: priimti neapibrėžtumą, bet kurti pasitikėjimą per skaidrumą ir vartotojo kontrolę.

## 5. Pagrindinių pamokų santrauka

- **1 pamoka**: Agentai yra sistemos, ne tik modeliai. Jie suvokia, mąsto ir veikia.  
- **2 pamoka**: Tokios sistemos kaip Semantic Kernel ir AutoGen abstrahuoja įrankių kvietimų bei būsenos valdymo sudėtingumą.  
- **3 pamoka**: Kurkite su skaidrumu ir vartotojo kontrole mintyje.  
- **4 pamoka**: Įrankiai yra agento „rankos“. Schemos apibrėžimas yra esminis, kad DKM suprastų, kaip jais naudotis.  
- **7 pamoka**: Planavimas yra agento „vykdomoji funkcija“, leidžianti spręsti sudėtingus darbo srautus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome suprasti, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminė dokumento versija gimtąja kalba turėtų būti laikoma autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama kreiptis į profesionalius vertėjus. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->