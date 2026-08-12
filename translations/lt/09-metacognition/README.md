[![Multi-Agent Design](../../../translated_images/lt/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_
# Metakognicija DI agentuose

## Įvadas

Sveiki atvykę į pamoką apie metakogniciją DI agentuose! Šis skyrius skirtas pradedantiesiems, kurie domisi, kaip DI agentai gali mąstyti apie savo pačių mąstymo procesus. Pamokos pabaigoje suprasite pagrindines sąvokas ir būsite aprūpinti praktiniais pavyzdžiais, kaip pritaikyti metakogniciją DI agentų kūrime.

## Mokymosi tikslai

Baigę šią pamoką galėsite:

1. Suprasti apribojimus ir pasekmes, susijusias su samprotavimo ciklais agentų apibrėžimuose.
2. Naudoti planavimo ir vertinimo technikas, kad padėtumėte agentams savarankiškai taisyti klaidas.
3. Kurti savo agentus, gebančius manipuliuoti kodu užduotims atlikti.

## Įvadas į metakogniciją

Metakognicija reiškia aukštesnio rango pažinimo procesus, kurie apima mąstymą apie savo paties mąstymą. DI agentams tai reiškia gebėjimą įvertinti ir koreguoti savo veiksmus remiantis savimonėmis ir praeities patirtimi. Metakognicija, arba „mąstymas apie mąstymą“, yra svarbi sąvoka agentinių DI sistemų kūrime. Tai reiškia, kad DI sistemos sąmoningos apie savo vidinius procesus ir gali stebėti, reguliuoti bei pritaikyti savo elgesį atitinkamai. Kaip mes darome, kai jaučiame aplinką ar nagrinėjame problemą. Ši savimonė gali padėti DI sistemoms priimti geresnius sprendimus, atpažinti klaidas ir gerinti savo veikimą laikui bėgant – tai vėl susiję su Turingo testu ir diskusijomis, ar DI perims kontrolę.

Agentinių DI sistemų kontekste metakognicija gali padėti spręsti kelis iššūkius, pavyzdžiui:
- Skaidrumas: Užtikrinti, kad DI sistemos galėtų paaiškinti savo samprotavimus ir sprendimus.
- Samprotavimas: Pagerinti DI sistemų gebėjimą apjungti informaciją ir priimti pagrįstus sprendimus.
- Prisitaikymas: Leisti DI sistemoms prisitaikyti prie naujų aplinkų ir kintančių sąlygų.
- Suvokimas: Pagerinti DI sistemų tikslumą atpažįstant ir interpretuojant aplinkos duomenis.

### Kas yra metakognicija?

Metakognicija, arba „mąstymas apie mąstymą“, yra aukštesnio rango pažinimo procesas, kuris apima savimonę ir savo pažinimo procesų savireguliaciją. DI srityje metakognicija suteikia agentams galimybę įvertinti ir pritaikyti savo strategijas bei veiksmus, kas lemia pagerintą problemų sprendimą ir sprendimų priėmimo gebėjimus. Suprasdami metakogniciją, galite kurti DI agentus, kurie yra ne tik išmanesni, bet ir labiau prisitaikantys bei efektyvūs. Tikroje metakognicijoje DI aiškiai samprotauja apie savo pačios samprotavimus.

Pavyzdys: „Aš pasirinkau pigesnius skrydžius, nes… galbūt praleidau tiesioginius skrydžius, todėl dar kartą peržiūrėsiu.“.
Stebi, kaip ir kodėl pasirinko tam tikrą maršrutą.
- Atkreipia dėmesį, kad padarė klaidų, nes pernelyg pasitikėjo vartotojo pageidavimais iš praėjusio karto, tad keičia savo sprendimų priėmimo strategiją, ne tik galutinį pasiūlymą.
- Diagnostikuoja modelius, pavyzdžiui: „Kiekvieną kartą, kai vartotojas mini ‘per daug žmonių’, turėčiau ne tik pašalinti tam tikras lankytinas vietas, bet ir įvertinti, kad mano metodas rinktis ‘populiariausias lankytinas vietas’ yra klaidingas, jei visada reitinguoju pagal populiarumą.“

### Metakognicijos svarba DI agentams

Metakognicija atlieka lemiamą vaidmenį DI agentų kūrime dėl kelių priežasčių:

![Metakognicijos svarba](../../../translated_images/lt/importance-of-metacognition.b381afe9aae352f7.webp)

- Savianalizė: Agentai gali įvertinti savo veiklą ir nustatyti tobulintinas sritis.
- Prisitaikomumas: Agentai gali keisti savo strategijas remdamiesi praeities patirtimi ir kintančiomis aplinkybėmis.
- Klaidų taisymas: Agentai gali savarankiškai aptikti ir taisyti klaidas, kas leidžia pasiekti tikslesnių rezultatų.
- Išteklių valdymas: Agentai gali optimizuoti išteklių, tokių kaip laikas ir skaičiavimo galia, naudojimą, planuodami ir vertindami savo veiksmus.

## DI agento komponentai

Prieš gilindamiesi į metakognityvinius procesus, svarbu suprasti pagrindinius DI agento komponentus. DI agentas paprastai susideda iš:

- Asmenybės: Agento asmenybė ir charakteristikos, apibrėžiančios, kaip jis sąveikauja su vartotojais.
- Įrankių: Gebėjimai ir funkcijos, kurias agentas gali atlikti.
- Įgūdžių: Žinios ir ekspertizė, kurias agentas turi.

Šie komponentai veikia kartu, sukurdami „ekspertizės vienetą“, galintį atlikti specifines užduotis.

**Pavyzdys**:
Įsivaizduokite kelionių agentą, agento paslaugas, kurios ne tik planuoja jūsų atostogas, bet ir koreguoja savo veiksmus pagal realaus laiko duomenis ir praeities klientų kelionių patirtis.

### Pavyzdys: metakognicija kelionių agento paslaugoje

Įsivaizduokite, kad kuriate DI varomą kelionių agento paslaugą. Šis agentas, „Kelionių agentas“, padeda vartotojams planuoti atostogas. Norint įtraukti metakogniciją, „Kelionių agentas“ turi įvertinti ir koreguoti savo veiksmus remdamasis savimonėmis ir praeities patirtimi. Štai kaip metakognicija galėtų pasireikšti:

#### Dabartinė užduotis

Dabartinė užduotis – padėti vartotojui suplanuoti kelionę į Paryžių.

#### Žingsniai užduočiai atlikti

1. **Surinkti vartotojo pageidavimus:** Paklauskite vartotojo apie kelionės datas, biudžetą, pomėgius (pvz., muziejus, virtuvė, apsipirkimas) ir bet kokius specifinius reikalavimus.
2. **Gauti informaciją:** Ieškokite skrydžių, apgyvendinimo vietų, lankytinų vietų ir restoranų, atitinkančių vartotojo pageidavimus.
3. **Generuoti rekomendacijas:** Pateikite suasmenintą maršrutą su skrydžių detalėmis, viešbučių rezervacijomis ir siūlomomis veiklomis.
4. **Koreguoti pagal atsiliepimus:** Paprašykite vartotojo atsiliepimų apie rekomendacijas ir atlikite būtinus pakeitimus.

#### Reikalingi ištekliai

- Prieiga prie skrydžių ir viešbučių rezervavimo duomenų bazių.
- Informacija apie Paryžiaus lankytinas vietas ir restoranus.
- Vartotojo atsiliepimų duomenys iš ankstesnių sąveikų.

#### Patirtis ir savianalizė

„Kelionių agentas“ naudoja metakogniciją, kad įvertintų savo veiklą ir mokytųsi iš patirties. Pavyzdžiui:

1. **Analizuojant vartotojo atsiliepimus:** „Kelionių agentas“ peržiūri atsiliepimus, kad nustatytų, kurios rekomendacijos buvo gerai įvertintos, o kurios – ne, ir atitinkamai koreguoja ateities pasiūlymus.
2. **Prisitaikomumas:** Jei vartotojas anksčiau minėjo nemėgstąs perpildytų vietų, „Kelionių agentas“ ateityje vengs siūlyti populiarias turistų vietas piko metu.
3. **Klaidų taisymas:** Jei „Kelionių agentas“ padarė klaidą ankstesnėje rezervacijoje, pvz., pasiūlė visiškai užsakytą viešbutį, jis išmoksta kruopščiau tikrinti prieinamumą prieš siūlydamas.

#### Praktinis kūrėjo pavyzdys

Štai supaprastintas pavyzdys, kaip „Kelionių agento“ kodas gali atrodyti įtraukiant metakogniciją:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Ieškokite skrydžių, viešbučių ir lankytinų vietų pagal pageidavimus
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analizuokite atsiliepimus ir koreguokite būsimus pasiūlymus
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Pavyzdinis naudojimas
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Kodėl svarbi metakognicija

- **Savianalizė:** Agentai gali įvertinti savo veiklą ir nustatyti gerintinas sritis.
- **Prisitaikomumas:** Agentai gali modifikuoti strategijas pagal gautus atsiliepimus ir kintančias sąlygas.
- **Klaidų taisymas:** Agentai gali savarankiškai aptikti ir taisyti klaidas.
- **Išteklių valdymas:** Agentai gali optimizuoti išteklių, tokių kaip laikas ir skaičiavimo galia, naudojimą.

Įtraukdami metakogniciją, „Kelionių agentas“ gali suteikti asmeniškesnes ir tikslesnes kelionių rekomendacijas, gerindamas bendrą vartotojo patirtį.

---

## 2. Planavimas agentuose

Planavimas yra svarbi DI agentų elgesio sudedamoji dalis. Tai apima žingsnių, reikalingų pasiekti tikslą, apibrėžimą atsižvelgiant į esamą būseną, išteklius ir galimus kliuvinius.

### Planavimo elementai

- **Dabartinė užduotis:** Aiškiai apibrėžkite užduotį.
- **Žingsniai užduočiai atlikti:** Suskaidykite užduotį į valdomus etapus.
- **Reikalingi ištekliai:** Nustatykite reikalingus išteklius.
- **Patirtis:** Naudokite praeities patirtį planavimui paremti.

**Pavyzdys**:
Čia pateikti žingsniai, kurių „Kelionių agentas“ turi imtis, kad veiksmingai padėtų vartotojui suplanuoti kelionę:

### „Kelionių agento“ žingsniai

1. **Surinkti vartotojo pageidavimus**
   - Paklauskite vartotojo apie kelionės datas, biudžetą, pomėgius ir specifinius reikalavimus.
   - Pavyzdžiai: „Kada planuojate keliauti?“ „Koks jūsų biudžetas?“ „Kokias veiklas mėgstate atostogų metu?“

2. **Gauti informaciją**
   - Ieškokite kelionės variantų pagal vartotojo pageidavimus.
   - **Skrydžiai:** Raskite prieinamus skrydžius pagal vartotojo biudžetą ir kelionės datas.
   - **Apgyvendinimas:** Raskite viešbučius ar nuomojamus būstus, atitinkančius vartotojo pageidavimus dėl vietos, kainos ir patogumų.
   - **Lankytinos vietos ir restoranai:** Nustatykite populiarias lankytinas vietas, veiklas ir maitinimosi galimybes pagal vartotojo pomėgius.

3. **Generuoti rekomendacijas**
   - Sudarykite surinktą informaciją į suasmenintą maršrutą.
   - Pateikite detales, tokias kaip skrydžių pasirinkimai, viešbučių rezervacijos ir siūlomos veiklos, pritaikytas vartotojo pageidavimams.

4. **Pateikti maršrutą vartotojui**
   - Perduokite pasiūlytą maršrutą vartotojui peržiūrai.
   - Pavyzdys: „Čia yra pasiūlytas maršrutas jūsų kelionei į Paryžių. Jame yra skrydžių informacija, viešbučių rezervacijos bei siūlomų veiklų ir restoranų sąrašas. Prašau, pasakykite savo nuomonę!“

5. **Surinkti atsiliepimus**
   - Paklauskite vartotojo atsiliepimų apie pasiūlytą maršrutą.
   - Pavyzdžiai: „Ar jums patinka skrydžių variantai?“ „Ar viešbutis tinkamas jūsų poreikiams?“ „Ar yra veiklų, kurias norėtumėte pridėti ar pašalinti?“

6. **Koreguoti pagal atsiliepimus**
   - Modifikuokite maršrutą remdamiesi vartotojo atsiliepimais.
   - Atlikite reikiamus pakeitimus dėl skrydžių, apgyvendinimo ir veiklų rekomendacijų, kad jos geriau atitiktų vartotojo pageidavimus.

7. **Galutinis patvirtinimas**
   - Pateikite atnaujintą maršrutą vartotojui galutiniam patvirtinimui.
   - Pavyzdys: „Atlikau pakeitimus pagal jūsų atsiliepimus. Štai atnaujintas maršrutas. Ar viskas atrodo gerai?“

8. **Rezervacijų užsakymas ir patvirtinimas**
   - Kai vartotojas patvirtina maršrutą, tęskite skrydžių, apgyvendinimo ir iš anksto suplanuotų veiklų rezervacijas.
   - Siųskite patvirtinimo duomenis vartotojui.

9. **Teikti nuolatinę pagalbą**
   - Likite pasiekiamas, kad padėtumėte vartotojui keitimų ar papildomų prašymų atveju prieš kelionę ir jos metu.
   - Pavyzdys: „Jei kelionės metu reikės papildomos pagalbos, drąsiai kreipkitės bet kada!“

### Pavyzdinė sąveika

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Pavyzdinis naudojimas užsakymo užklausos metu
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korekcinė RAG sistema

Pirmiausia pradėkime nuo supratimo, kuo skiriasi RAG įrankis ir pre-emptive konteksto krovimas.

![RAG vs Konteksto krovimas](../../../translated_images/lt/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG derina informacijos gavimo sistemą su generatyviniu modeliu. Užklausai pateikus, gavimo sistema išorinėje šaltinyje surenka susijusius dokumentus ar duomenis, kurie tada pridedami prie įėjimo generatyviniam modeliui. Tai padeda modeliui sugeneruoti tikslesnius ir kontekstualiai svarbesnius atsakymus.

RAG sistemoje agentas gauna susijusią informaciją iš žinių bazės ir naudoja ją tinkamiems atsakymams ar veiksmams generuoti.

### Korekcinis RAG požiūris

Korekcinis RAG požiūris orientuojasi į RAG technikų naudojimą klaidoms taisyti ir DI agentų tikslumo gerinimui. Tai apima:

1. **Skatinimo technika:** Naudojant specifinius užuominas, kad agentas galėtų gauti aktualią informaciją.
2. **Įrankis:** Įgyvendinant algoritmus ir mechanizmus, leidžiančius agentui įvertinti gautos informacijos svarbą ir sugeneruoti tikslius atsakymus.
3. **Vertinimas:** Nuolatinis agento veiklos vertinimas ir koregavimas tikslo gerinti tikslumą ir efektyvumą.

#### Pavyzdys: Korekcinis RAG paieškos agentui

Įsivaizduokite paieškos agentą, kuris surenka informaciją iš interneto atsakant į vartotojo užklausas. Korekcinis RAG požiūris gali apimti:

1. **Skatinimo technika:** Formuluoti paieškos užklausas pagal vartotojo įvestį.
2. **Įrankis:** Naudoti natūralios kalbos apdorojimo ir mašininio mokymosi algoritmus paieškos rezultatams rikiuoti ir filtruoti.
3. **Vertinimas:** Analizuoti vartotojo atsiliepimus, kad identifikuotų ir ištaisytų netikslumus surinktoje informacijoje.

### Korekcinis RAG kelionių agentui

Korekcinis RAG (Retrieval-Augmented Generation) pagerina DI gebėjimą gauti ir generuoti informaciją, taisant bet kokius netikslumus. Pažiūrėkime, kaip „Kelionių agentas“ gali naudoti korekcinį RAG požiūrį, kad suteiktų tikslesnes ir aktualias kelionių rekomendacijas.

Tai apima:

- **Skatinimo technika:** Naudojant specifines užuominas, kad agentas galėtų gauti aktualią informaciją.
- **Įrankis:** Įgyvendinant algoritmus ir mechanizmus, leidžiančius agentui įvertinti gautos informacijos svarbą ir generuoti tikslius atsakymus.
- **Vertinimas:** Nuolat vertinant agento veiklą ir koreguojant ją, siekiant gerinti tikslumą ir efektyvumą.

#### Žingsniai korekciniam RAG įgyvendinimui „Kelionių agento“ sistemoje

1. **Pirmoji vartotojo sąveika**
   - „Kelionių agentas“ surenka pradinius vartotojo pageidavimus, tokius kaip kelionės tikslas, datos, biudžetas ir pomėgiai.
   - Pavyzdys:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Informacijos gavimas**
   - „Kelionių agentas“ gauna informaciją apie skrydžius, apgyvendinimą, lankytinas vietas ir restoranus pagal vartotojo pageidavimus.
   - Pavyzdys:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Pirminių rekomendacijų generavimas**
   - „Kelionių agentas“ naudoja gautą informaciją suasmenintam maršrutui generuoti.
   - Pavyzdys:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Vartotojo atsiliepimų rinkimas**
   - „Kelionių agentas“ prašo vartotojo atsiliepimų apie pirmines rekomendacijas.
   - Pavyzdys:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korekcinis RAG procesas**
   - **Skatinimo technika:** „Kelionių agentas“ formuluoja naujas paieškos užklausas pagal vartotojo atsiliepimus.
     - Pavyzdys:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Įrankis:** „Kelionių agentas“ naudoja algoritmus naujiems paieškos rezultatams rikiuoti ir filtruoti, pabrėždamas aktualumą pagal vartotojo atsiliepimus.
     - Pavyzdys:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Vertinimas:** „Kelionių agentas“ nuolat vertina savo rekomendacijų aktualumą ir tikslumą, analizuodamas vartotojo atsiliepimus ir atlikdamas būtinus pakeitimus.
     - Pavyzdys:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktinis pavyzdys

Štai supaprastintas Python kodo pavyzdys, įtraukiantis korekcinį RAG požiūrį „Kelionių agento“ sistemoje:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Pavyzdinis naudojimas
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Pre-emptive konteksto krovimas


Išankstinis konteksto įkėlimas reiškia, kad modelis prieš apdorojant užklausą gauna atitinkamą kontekstą ar fono informaciją. Tai leidžia modeliui turėti šią informaciją nuo pat pradžios, kas padeda sugeneruoti labiau pagrįstus atsakymus be poreikio rinkti papildomus duomenis proceso metu.

Štai supaprastintas pavyzdys, kaip išankstinis konteksto įkėlimas galėtų atrodyti kelionių agento programoje Python kalba:

```python
class TravelAgent:
    def __init__(self):
        # Iš anksto įkelti populiarias kelionės vietas ir jų informaciją
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Gauti kelionės vietos informaciją iš iš anksto įkelto konteksto
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Naudojimo pavyzdys
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Paaiškinimas

1. **Inicializacija (`__init__` metodas)**: `TravelAgent` klasė iš anksto įkelia žodyną, kuriame yra informacija apie populiarias kelionės vietas, tokias kaip Paryžius, Tokijas, Niujorkas ir Sidnėjus. Šiame žodyne yra tokia informacija kaip šalis, valiuta, kalba ir pagrindinės lankytinos vietos kiekvienai vietai.

2. **Informacijos gavimas (`get_destination_info` metodas)**: Kai vartotojas užduoda klausimą apie tam tikrą kelionės vietą, `get_destination_info` metodas paima reikiamą informaciją iš išankstinio konteksto žodyno.

Iš anksto įkėlus kontekstą, kelionių agento programa gali greitai atsakyti į vartotojo užklausas nereikalaujant rinkti šios informacijos iš išorinio šaltinio realiu laiku. Tai daro programą efektyvesnę ir jautresnę.

### Plano inicijavimas su tikslu prieš iteraciją

Plano inicijavimas su tikslu reiškia aiškaus tikslo ar norimo rezultato apibrėžimą iš karto. Apibrėždama šį tikslą iš anksto, modelis gali jį naudoti kaip vadovaujančią principą per visą iteracinį procesą. Tai padeda užtikrinti, kad kiekviena iteracija priartina prie norimo rezultato, todėl procesas tampa efektyvesnis ir labiau susitelkęs.

Štai pavyzdys, kaip galėtumėte inicijuoti kelionės planą su tikslu prieš iteruojant kelionių agento programoje Python kalba:

### Scenarijus

Kelionių agentas nori suplanuoti klientui individualizuotas atostogas. Tikslas – sukurti kelionės maršrutą, kuris maksimaliai atitiktų kliento pageidavimus ir biudžetą.

### Veiksmai

1. Apibrėžti kliento pageidavimus ir biudžetą.
2. Inicijuoti pradinį planą, remiantis šiais pageidavimais.
3. Iteruoti, tobulinti planą, optimizuojant pagal kliento pasitenkinimą.

#### Python kodas

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Pavyzdinis naudojimas
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Kodo paaiškinimas

1. **Inicializacija (`__init__` metodas)**: `TravelAgent` klasė yra inicializuojama su sąrašu potencialių kelionės vietų, kurių kiekviena turi atributus kaip pavadinimas, kaina ir veiklos tipas.

2. **Plano inicijavimas (`bootstrap_plan` metodas)**: Šis metodas sukuria pradinis kelionės planą remiantis kliento pageidavimais ir biudžetu. Jis iteruoja per vietų sąrašą ir prideda jas prie plano, jei jos atitinka kliento pageidavimus ir atitinka biudžetą.

3. **Pageidavimų atitikimas (`match_preferences` metodas)**: Šis metodas tikrina, ar vieta atitinka kliento pageidavimus.

4. **Plano iteracija (`iterate_plan` metodas)**: Šis metodas tobulina pirminį planą, bandydamas pakeisti kiekvieną vietą plane geresniu variantu, atsižvelgiant į kliento pageidavimus ir biudžeto apribojimus.

5. **Sąnaudų skaičiavimas (`calculate_cost` metodas)**: Šis metodas apskaičiuoja bendrą dabartinio plano kainą, įskaitant galimą naują vietą.

#### Pavyzdinis naudojimas

- **Pradinis planas**: Kelionių agentas sukuria pradinį planą pagal kliento pageidavimus aplankyti lankytinas vietas ir biudžetą $2000.
- **Patobulintas planas**: Kelionių agentas iteruoja planą, optimizuodamas pagal kliento pageidavimus ir biudžetą.

Inicijuodamas planą su aiškiu tikslu (pvz., maksimalizuoti kliento pasitenkinimą) ir iteruodamas, kad tobulintų planą, kelionių agentas gali sukurti individualizuotą ir optimizuotą kelionės maršrutą klientui. Šis metodas užtikrina, kad kelionės planas nuo pat pradžių atitiks kliento pageidavimus ir biudžetą bei gerės su kiekviena iteracija.

### LLM naudojimas perskirstymui ir vertinimui

Didieji kalbos modeliai (LLM) gali būti naudojami perskirstymui ir vertinimui, įvertinant gautų dokumentų ar sugeneruotų atsakymų aktualumą ir kokybę. Štai kaip tai veikia:

**Gavimas:** Pradinis gavimo etapas paima kandidatų dokumentų arba atsakymų rinkinį, remiantis užklausa.

**Perskirstymas:** LLM įvertina šiuos kandidatus ir perskirsto juos pagal aktualumą ir kokybę. Šis žingsnis užtikrina, kad pirmiausia būtų pateikta pati aktualiausia ir aukščiausios kokybės informacija.

**Vertinimas:** LLM priskiria balus kiekvienam kandidatui, atspindinčius jų aktualumą ir kokybę. Tai padeda pasirinkti geriausią atsakymą ar dokumentą vartotojui.

Naudodami LLM perskirstymui ir vertinimui, sistema gali pateikti tikslesnę ir kontekstualiai svarbesnę informaciją, gerindama bendrą vartotojo patirtį.

Štai pavyzdys, kaip kelionių agentas gali naudoti Didįjį kalbos modelį (LLM) perskirstymui ir vertinimui pagal vartotojo pageidavimus Python kalba:

#### Scenarijus – kelionės pagal pageidavimus

Kelionių agentas nori rekomenduoti geriausias kelionės vietas klientui pagal jo pageidavimus. LLM padės perskirstyti ir įvertinti vietas, kad būtų pateikta pati aktualiausia pasirinktis.

#### Veiksmai:

1. Surinkti vartotojo pageidavimus.
2. Gauti potencialių kelionės vietų sąrašą.
3. Naudoti LLM perskirstymui ir vertinimui pagal vartotojo pageidavimus.

Štai kaip galite atnaujinti ankstesnį pavyzdį, naudodami Azure OpenAI paslaugas:

#### Reikalavimai

1. Turėti Azure prenumeratą.
2. Sukurti Azure OpenAI išteklių ir gauti savo API raktą.

#### Pavyzdinis Python kodas

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Sugeneruoti užklausą Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Apibrėžti antraštes ir užklausos duomenis
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Iškvieti Azure OpenAI API, kad gauti perrikiuotas ir įvertintas paskirties vietas
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Išskirti ir grąžinti rekomendacijas
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Naudojimo pavyzdys
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Kodo paaiškinimas – pageidavimų pateikėjas

1. **Inicializacija**: `TravelAgent` klasė yra inicializuojama su potencialių kelionės vietų sąrašu, kurių kiekviena turi atributus, tokius kaip pavadinimas ir aprašymas.

2. **Rekomendacijų gavimas (`get_recommendations` metodas)**: Šis metodas generuoja užklausą Azure OpenAI paslaugai pagal vartotojo pageidavimus ir siunčia HTTP POST užklausą Azure OpenAI API, kad gautų perskirstytas ir įvertintas vietas.

3. **Užklausos generavimas (`generate_prompt` metodas)**: Šis metodas sudaro užklausą Azure OpenAI, įtraukiant vartotojo pageidavimus ir vietų sąrašą. Užklausa nukreipia modelį perskirstyti ir įvertinti vietas pagal pateiktus pageidavimus.

4. **API kvietimas**: `requests` biblioteka naudojama siųsti HTTP POST užklausą į Azure OpenAI API galutinį tašką. Atsakymas turi perskirstytas ir įvertintas vietas.

5. **Pavyzdinis naudojimas**: Kelionių agentas surenka vartotojo pageidavimus (pvz., susidomėjimą lankytinomis vietomis ir įvairią kultūrą) ir naudoja Azure OpenAI paslaugą, kad gautų perskirstytas ir įvertintas kelionės vietų rekomendacijas.

Būtinai pakeiskite `your_azure_openai_api_key` į savo tikrąjį Azure OpenAI API raktą ir `https://your-endpoint.com/...` į tikrąjį Azure OpenAI diegimo galutinį URL.

Naudodamasis LLM perskirstymui ir vertinimui, kelionių agentas gali pateikti labiau suasmenintas ir aktualias kelionės rekomendacijas klientams, pagerindamas jų bendrą patirtį.

### RAG: užklausos metodas prieš įrankį

Retrieval-Augmented Generation (RAG) gali būti tiek užklausos metodas, tiek įrankis AI agentų kūrime. Supratimas apie skirtumus gali padėti jums efektyviau naudoti RAG savo projektuose.

#### RAG kaip užklausos metodas

**Kas tai yra?**

- Kaip užklausos metodas, RAG reiškia specifinių užklausų ar užklausų formavimą, kuris nukreipia informacijos paiešką dideliame korpuse ar duomenų bazėje. Ši informacija tada naudojama atsakymams arba veiksmams generuoti.

**Kaip tai veikia:**

1. **Užklausų formavimas**: Sukurkite gerai struktūruotas užklausas arba prompts, remdamiesi užduotimi ar vartotojo įvestimi.
2. **Informacijos paieška**: Naudokite užklausas, kad surastumėte aktualius duomenis iš iš anksto egzistuojančios žinių bazės ar duomenų rinkinio.
3. **Atsakymo generavimas**: Sujunkite surinktą informaciją kartu su generatyviniais AI modeliais, kad sukurtumėte išsamų ir nuoseklų atsakymą.

**Pavyzdys kelionių agentui:**

- Vartotojo įvestis: "Noriu aplankyti muziejus Paryžiuje."
- Užklausa: "Raskite geriausius muziejus Paryžiuje."
- Surinkta informacija: Informacija apie Luvro muziejų, Orsė muziejų ir pan.
- Sugeneruotas atsakymas: "Štai keletas geriausių muziejų Paryžiuje: Luvro muziejus, Orsė muziejus ir Pompidu centras."

#### RAG kaip įrankis

**Kas tai yra?**

- Kaip įrankis, RAG yra integruota sistema, kuri automatizuoja informacijos gavimo ir generavimo procesus, leidžianti kūrėjams lengviau įgyvendinti sudėtingas AI funkcijas be rankinio užklausų kūrimo kiekvienai užklausai.

**Kaip tai veikia:**

1. **Integracija**: Įdiegti RAG AI agento architektūroje, leidžiant jam automatiškai tvarkyti informacijos gavimo ir generavimo užduotis.
2. **Automatizavimas**: Įrankis valdo visą procesą nuo vartotojo įvesties iki galutinio atsakymo generavimo, nereikalaujant aiškių užklausų kiekvienam žingsniui.
3. **Efektyvumas**: Pagerina agento veikimą supaprastindamas gavimo ir generavimo procesą, leidžiant greičiau ir tiksliau atsakyti.

**Pavyzdys kelionių agentui:**

- Vartotojo įvestis: "Noriu aplankyti muziejus Paryžiuje."
- RAG įrankis: Automatiškai surenka informaciją apie muziejus ir sugeneruoja atsakymą.
- Sugeneruotas atsakymas: "Štai keletas geriausių muziejų Paryžiuje: Luvro muziejus, Orsė muziejus ir Pompidu centras."

### Palyginimas

| Aspektas               | Užklausos metodas                                         | Įrankis                                               |
|------------------------|------------------------------------------------------------|-------------------------------------------------------|
| **Rankinis vs Automatinis** | Rankiniu būdu formuluojamos užklausos kiekvienai užklausai. | Automatizuotas gavimo ir generavimo procesas.        |
| **Kontrolė**            | Teikia didesnę kontrolę gavimo procesui.                  | Supaprastina ir automatizuoja gavimo ir generavimo procesą.|
| **Lankstumas**          | Leidžia suasmenintas užklausas pagal specifinius poreikius.| Efektyvesnis didelio masto įgyvendinimams.           |
| **Sudėtingumas**        | Reikalauja užklausų kūrimo ir tobulinimo.                   | Lengviau integruoti AI agento architektūroje.         |

### Praktiniai pavyzdžiai

**Užklausos metodo pavyzdys:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Įrankio pavyzdys:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Aktualumo vertinimas

Aktualumo vertinimas yra svarbus AI agento veiklos aspektas. Tai užtikrina, kad agento surinkta ir sugeneruota informacija būtų tinkama, tiksli ir naudinga vartotojui. Pažvelkime, kaip vertinti aktualumą AI agentuose, pateikiant praktinius pavyzdžius ir metodikas.

#### Pagrindinės aktualumo vertinimo sąvokos

1. **Konteksto suvokimas**:
   - Agentas turi suprasti vartotojo užklausos kontekstą, kad surinktų ir generuotų aktualią informaciją.
   - Pavyzdys: Jei vartotojas klausia „geriausi restoranai Paryžiuje“, agentas turėtų atsižvelgti į vartotojo pageidavimus, tokius kaip maisto rūšis ir biudžetas.

2. **Tikslumas**:
   - Agentas turi pateikti faktiškai teisingą ir atnaujintą informaciją.
   - Pavyzdys: Rekomenduoti šiuo metu veikiančius restoranus su geromis apžvalgomis, o ne pasenusias ar uždarytas vietas.

3. **Vartotojo ketinimas**:
   - Agentas turi atspėti vartotojo ketinimą už užklausos, kad pateiktų pačią aktualiausią informaciją.
   - Pavyzdys: Jei vartotojas prašo „biudžetui tinkami viešbučiai“, agentas turėtų prioritetizuoti prieinamas vietas.

4. **Grįžtamojo ryšio ciklas**:
   - Nuolatinis vartotojo atsiliepimų rinkimas ir analizavimas padeda agentui tobulinti aktualumo vertinimo procesą.
   - Pavyzdys: Įtraukti vartotojų įvertinimus ir atsiliepimus apie ankstesnes rekomendacijas, kad pagerėtų ateities atsakymai.

#### Praktinės aktualumo vertinimo technikos

1. **Aktualumo balų skyrimas**:
   - Priskirti aktualumo balą kiekvienam gautam elementui, vertinant, kaip gerai jis atitinka vartotojo užklausą ir pageidavimus.
   - Pavyzdys:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtravimas ir rūšiavimas**:
   - Išfiltruoti neaktualius elementus ir surūšiuoti likusius pagal aktualumo balą.
   - Pavyzdys:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Grąžina 10 svarbiausių elementų
     ```

3. **Natūralios kalbos apdorojimas (NLP)**:
   - Naudoti NLP metodus, kad suprastumėte vartotojo užklausą ir surinktumėte aktualią informaciją.
   - Pavyzdys:

     ```python
     def process_query(query):
         # Naudokite NLP, kad išgautumėte pagrindinę informaciją iš vartotojo užklausos
         processed_query = nlp(query)
         return processed_query
     ```

4. **Vartotojo atsiliepimų integravimas**:
   - Rinkti vartotojo atsiliepimus apie pateiktas rekomendacijas ir naudoti juos būsimoms aktualumo vertinimo korekcijoms.
   - Pavyzdys:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Pavyzdys: Aktualumo vertinimas kelionių agentui

Štai praktinis pavyzdys, kaip Kelionių agentas gali vertinti kelionės rekomendacijų aktualumą:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Grąžinti 10 svarbiausių elementų

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Naudojimo pavyzdys
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Paieška pagal ketinimą

Paieška pagal ketinimą reiškia vartotojo užklausos pagrindinio tikslo ar poreikio supratimą ir interpretavimą, kad būtų surinkta ir sugeneruota pati aktualiausia ir naudingiausia informacija. Šis požiūris eina toliau nei tik raktinių žodžių atitikimas ir orientuojasi į vartotojo tikrąsias reikmes bei kontekstą.

#### Pagrindinės sąvokos ieškant pagal ketinimą

1. **Vartotojo ketinimo supratimas**:
   - Vartotojo ketinimą galima suskirstyti į tris pagrindines rūšis: informacinis, navigacinis ir sandorio.
     - **Informacinis ketinimas**: Vartotojas ieško informacijos apie temą (pvz., „Kokie yra geriausi muziejai Paryžiuje?“).
     - **Navigacinis ketinimas**: Vartotojas nori nukeliauti į tam tikrą svetainę ar puslapį (pvz., „Luvro muziejaus oficiali svetainė“).
     - **Sandorio ketinimas**: Vartotojas siekia atlikti sandorį, pavyzdžiui, užsakyti skrydį arba pirkti (pvz., „Užsakyti skrydį į Paryžių“).

2. **Konteksto suvokimas**:
   - Vartotojo užklausos konteksto analizė padeda tiksliai nustatyti ketinimą. Tai apima ankstesnes sąveikas, vartotojo pageidavimus ir specifines dabartinės užklausos detales.

3. **Natūralios kalbos apdorojimas (NLP)**:
   - Naudojamos NLP technikos, skirtos suprasti ir interpretuoti vartotojo natūralias užklausas. Tai apima objektų atpažinimą, nuotaikų analizę ir užklausų skaidymą.

4. **Personalizavimas**:
   - Paieškos rezultatų personalizavimas remiantis vartotojo istorija, pageidavimais ir atsiliepimais pagerina surinktos informacijos aktualumą.

#### Praktinis pavyzdys: paieška pagal ketinimą kelionių agentui

Pažvelkime į Travel Agent kaip pavyzdį, kaip galėtų būti įgyvendinta paieška pagal ketinimą.

1. **Vartotojo pageidavimų rinkimas**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Vartotojo ketinimo supratimas**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Konteksto suvokimas**


   ```python
   def analyze_context(query, user_history):
       # Sujunkite esamą užklausą su vartotojo istorija, kad suprastumėte kontekstą
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Ieškoti ir personalizuoti rezultatus**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Pavyzdinė paieškos logika informaciniam tikslui
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Pavyzdinė paieškos logika navigaciniam tikslui
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Pavyzdinė paieškos logika transakciniam tikslui
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Pavyzdinė personalizavimo logika
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Grąžinti 10 geriausių suasmenintų rezultatų
   ```

5. **Naudojimo pavyzdys**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Kodo generavimas kaip įrankis

Kodo generavimo agentai naudoja DI modelius kodui rašyti ir vykdyti, sprendžiant sudėtingas problemas ir automatizuojant užduotis.

### Kodo generavimo agentai

Kodo generavimo agentai naudoja generatyvius DI modelius kodo rašymui ir vykdymui. Šie agentai gali spręsti sudėtingas problemas, automatizuoti užduotis ir suteikti vertingos informacijos generuodami ir vykdydami kodą įvairiomis programavimo kalbomis.

#### Praktinės taikymai

1. **Automatizuotas kodo generavimas**: Generuoti kodo fragmentus konkrečioms užduotims, pvz., duomenų analizei, interneto duomenų rinkimui ar mašininio mokymosi užduotims.
2. **SQL kaip RAG**: Naudoti SQL užklausas duomenų gavimui ir manipuliavimui iš duomenų bazių.
3. **Problemų sprendimas**: Kurti ir vykdyti kodą specifinėms problemoms spręsti, pvz., algoritmų optimizavimui arba duomenų analizei.

#### Pavyzdys: kodo generavimo agentas duomenų analizei

Įsivaizduokite, kad kuriate kodo generavimo agentą. Štai kaip jis galėtų veikti:

1. **Užduotis**: Išanalizuoti duomenų rinkinį, kad būtų identifikuotos tendencijos ir modeliai.
2. **Veiksmai**:
   - Įkelti duomenų rinkinį į duomenų analizės įrankį.
   - Generuoti SQL užklausas duomenų filtravimui ir suvestinėms gauti.
   - Vykdyti užklausas ir gauti rezultatus.
   - Naudoti rezultatus vizualizacijoms ir įžvalgoms generuoti.
3. **Reikalingi ištekliai**: Prieiga prie duomenų rinkinio, duomenų analizės įrankių ir SQL galimybės.
4. **Patirtis**: Naudoti ankstesnių analizės rezultatų patirtį siekiant pagerinti būsimų analizų tikslumą ir aktualumą.

### Pavyzdys: kodo generavimo agentas kelionių agentui

Šiame pavyzdyje sukursime kodo generavimo agentą, Pavyzdžiui, Kelionių agentą, kuris padėtų vartotojams planuoti keliones generuodamas ir vykdydamas kodą. Šis agentas galės atlikti užduotis, tokias kaip kelionių parinkčių paieška, rezultatų filtravimas ir maršruto sudarymas, naudodamas generatyvią DI.

#### Kodo generavimo agente apžvalga

1. **Vartotojo pageidavimų rinkimas**: Surenka vartotojo įvestį, pvz., kelionės tikslą, datas, biudžetą ir pomėgius.
2. **Kodo generavimas duomenų gavimui**: Generuoja kodo fragmentus, skirtus gauti informaciją apie skrydžius, viešbučius ir lankytinas vietas.
3. **Generuoto kodo vykdymas**: Vykdo sugeneruotą kodą, kad gautų realaus laiko informaciją.
4. **Maršruto sudarymas**: Apjungia gautus duomenis į personalizuotą kelionės planą.
5. **Rezultatų patikslinimas pagal atsiliepimus**: Priima vartotojo atsiliepimus ir prireikus iš naujo generuoja kodą, kad patobulintų rezultatus.

#### Įgyvendinimas žingsnis po žingsnio

1. **Vartotojo pageidavimų rinkimas**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Kodo generavimas duomenims gauti**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Pavyzdys: Generuoti kodą skrydžių paieškai pagal naudotojo pageidavimus
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Pavyzdys: Generuoti kodą viešbučių paieškai
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Generuoto kodo vykdymas**

   ```python
   def execute_code(code):
       # Vykdykite sugeneruotą kodą naudodami exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Maršruto sudarymas**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Rezultatų patikslinimas pagal atsiliepimus**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Koreguoti nustatymus pagal vartotojo atsiliepimus
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Atkurti ir vykdyti kodą su atnaujintais nustatymais
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Panaudojant aplinkos suvokimą ir samprotavimą

Atsižvelgiant į lentelės schemą, tikrai galima pagerinti užklausų generavimo procesą, pasitelkiant aplinkos suvokimą ir samprotavimą.

Štai pavyzdys, kaip tai galima atlikti:

1. **Schemų supratimas**: Sistema supranta lentelės schemą ir naudoja šią informaciją užklausų generavimo pagrindui.
2. **Rezultatų patikslinimas pagal atsiliepimus**: Sistema koreguoja vartotojo pageidavimus pagal atsiliepimus ir logiškai apsvarsto, kurios lentelės sritys turi būti atnaujintos.
3. **Užklausų generavimas ir vykdymas**: Sistema generuoja ir vykdo užklausas, kad gautų atnaujintus skrydžių ir viešbučių duomenis pagal naujus pageidavimus.

Žemiau pateiktas atnaujinto Python kodo pavyzdys, kuris taiko šias koncepcijas:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Koreguoti nuostatas pagal vartotojo atsiliepimus
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Logika pagrįsta schema, skirta koreguoti kitas susijusias nuostatas
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Vietinė logika nuostatų koregavimui pagal schemą ir atsiliepimus
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generuoti kodą skrydžių duomenims gauti pagal atnaujintas nuostatas
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generuoti kodą viešbučių duomenims gauti pagal atnaujintas nuostatas
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuliuoti kodo vykdymą ir grąžinti pavyzdinius duomenis
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Sugeneruoti maršrutą pagal skrydžius, viešbučius ir lankytinas vietas
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Pavyzdinė schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Pavyzdinis naudojimas
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Perkurti ir vykdyti kodą su atnaujintomis nuostatomis
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Paaiškinimas – užsakymas pagal atsiliepimus

1. **Schemų suvokimas**: `schema` žodynas apibrėžia, kaip pageidavimai turėtų būti koreguojami pagal atsiliepimus. Jame yra laukai, tokie kaip `favorites` ir `avoid`, su atitinkamomis korekcijomis.
2. **Pageidavimų koregavimas (`adjust_based_on_feedback` metodas)**: Šis metodas keičia pageidavimus pagal vartotojo atsiliepimus ir schemą.
3. **Aplinkos pagrindu atliekami koregavimai (`adjust_based_on_environment` metodas)**: Šis metodas koreguoja pakeitimus pagal schemą ir atsiliepimus.
4. **Užklausų generavimas ir vykdymas**: Sistema generuoja kodą, kad gautų atnaujintus skrydžių ir viešbučių duomenis pagal koreguotus pageidavimus ir imituoja šių užklausų vykdymą.
5. **Maršruto generavimas**: Sistema sudaro atnaujintą kelionės maršrutą remdamasi naujais skrydžių, viešbučių ir lankytinų vietų duomenimis.

Sistemai suteikus galimybę suvokti aplinką ir samprotauti pagal schemą, ji gali generuoti tikslesnes ir svarbesnes užklausas, kas veda prie geresnių kelionių rekomendacijų ir labiau suasmenintos vartotojo patirties.

### SQL kaip papildymo duomenų gavimų generavimo (RAG) metodas

SQL (struktūruotų užklausų kalba) yra galingas įrankis darbui su duomenų bazėmis. Naudojant ją kaip dalį papildymo duomenų gavimų generavimo (RAG) požiūrio, SQL gali gauti svarbią informaciją iš duomenų bazių, kuri leistų DI agentams kurti ir vykdyti atsakymus ar veiksmus. Pažiūrėkime, kaip SQL gali būti panaudotas kaip RAG metodas kelionių agento kontekste.

#### Pagrindinės sąvokos

1. **Duomenų bazės sąveika**:
   - SQL naudojama duomenų bazėms užklausti, gauti svarbią informaciją ir manipuliuoti duomenimis.
   - Pavyzdys: skrydžių detalių, viešbučių ir lankytinų vietų gavimas iš kelionių duomenų bazės.

2. **Integracija su RAG**:
   - SQL užklausos yra generuojamos atsižvelgiant į vartotojo įvestį ir pageidavimus.
   - Gautus duomenis vėliau naudoja personalizuotoms rekomendacijoms ar veiksmams generuoti.

3. **Dinaminis užklausų generavimas**:
   - DI agentas generuoja dinamiškas SQL užklausas pagal kontekstą ir vartotojo poreikius.
   - Pavyzdys: SQL užklausų pritaikymas rezultatų filtravimui pagal biudžetą, datas ir pomėgius.

#### Taikymai

- **Automatizuotas kodo generavimas**: Generuoti kodo fragmentus konkrečioms užduotims.
- **SQL kaip RAG metodas**: Naudoti SQL užklausas duomenų manipuliavimui.
- **Problemų sprendimas**: Kurti ir vykdyti kodą problemoms spręsti.

**Pavyzdys**:
Duomenų analizės agentas:

1. **Užduotis**: Išanalizuoti duomenų rinkinį, kad nustatytų tendencijas.
2. **Žingsniai**:
   - Įkelti duomenų rinkinį.
   - Generuoti SQL užklausas duomenų filtravimui.
   - Vykdyti užklausas ir gauti rezultatus.
   - Generuoti vizualizacijas ir įžvalgas.
3. **Ištekliai**: Prieiga prie duomenų rinkinio, SQL galimybės.
4. **Patirtis**: Naudoti ankstesnių rezultatų patirtį, kad pagerintų būsimų analizių tikslumą.

#### Praktinis pavyzdys: SQL naudojimas kelionių agente

1. **Vartotojo pageidavimų rinkimas**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL užklausų generavimas**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL užklausų vykdymas**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Rekomendacijų generavimas**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Pavyzdinės SQL užklausos

1. **Skrydžių užklausa**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Viešbučių užklausa**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Lankytinų vietų užklausa**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Naudodamiesi SQL kaip dalimi papildymo duomenų gavimų generavimo (RAG) metodo, DI agentai, tokie kaip Kelionių agentas, gali dinamiškai gauti ir naudoti aktualius duomenis, kad suteiktų tikslias ir suasmenintas rekomendacijas.

### Metakognicijos pavyzdys

Norėdami parodyti metakognicijos įgyvendinimą, sukursime paprastą agentą, kuris *atsispindi savo sprendimų priėmimo procese* spręsdamas problemą. Šiame pavyzdyje sukursime sistemą, kur agentas bando optimizuoti viešbučio pasirinkimą, bet vėliau įvertina savo samprotavimą ir koreguoja strategiją, kai padaro klaidų ar neoptimalų sprendimą.

Tai simuliuosime paprastu pavyzdžiu, kuriame agentas renkasi viešbučius pagal kainos ir kokybės derinį, tačiau jis „atsispindi“ savo sprendimuose ir atitinkamai koreguoja savo elgesį.

#### Kaip tai iliustruoja metakogniciją:

1. **Pradinis sprendimas**: Agentas pasirinks pigiausią viešbutį, nesuprasdamas kokybės įtakos.
2. **Atsispindėjimas ir vertinimas**: Po pirminio pasirinkimo agentas patikrina, ar viešbutis buvo blogas pasirinkimas pagal vartotojo atsiliepimus. Jei kokybė buvo per žema, jis reflektuoja savo samprotavimus.
3. **Strategijos koregavimas**: Agentas koreguoja savo strategiją pagal refleksiją ir pereina nuo „pigiausias“ prie „aukščiausia kokybė“, taip gerindamas sprendimų priėmimo procesą ateityje.

Štai pavyzdys:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Saugo anksčiau pasirinktus viešbučius
        self.corrected_choices = []  # Saugo pataisytus pasirinkimus
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Galimos strategijos

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Tarkime, turime vartotojo atsiliepimą, kuris mums sako, ar paskutinis pasirinkimas buvo geras ar ne
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Koreguoja strategiją, jei ankstesnis pasirinkimas buvo nepasitenkinimą keliantis
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simuliuoja viešbučių sąrašą (kaina ir kokybė)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Sukuria agentą
agent = HotelRecommendationAgent()

# 1 žingsnis: agentas rekomenduoja viešbutį, naudodamas „pigesnės“ strategiją
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 2 žingsnis: agentas apmąsto pasirinkimą ir prireikus koreguoja strategiją
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 3 žingsnis: agentas vėl rekomenduoja, šį kartą naudodamas pakoreguotą strategiją
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agento metakognicijos gebėjimai

Svarbiausia šiame pavyzdyje yra agente gebėjimas:
- Įvertinti ankstesnius sprendimus ir sprendimų priėmimo procesą.
- Koreguoti strategiją remiantis tuo atsispindėjimu, tai yra metakognicija veiksme.

Tai paprasta metakognicijos forma, kai sistema gali koreguoti savo samprotavimų procesą gavus vidinį atsiliepimą.

### Išvados

Metakognicija yra galingas įrankis, kuris gali žymiai pagerinti DI agentų galimybes. Įtraukdami metakognicinius procesus, galite kurti protingesnius, prisitaikančius ir efektyvesnius agentus. Naudokitės papildomais ištekliais, kad toliau tyrinėtumėte įdomų metakognicijos pasaulį DI agentuose.

### Ar turite daugiau klausimų apie metakognicijos dizaino modelį?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo klausimus apie DI agentus.

## Ankstesnis pamokas

[Daugiagentinis dizaino modelis](../08-multi-agent/README.md)

## Kitas pamoka

[DI agentai gamyboje](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->