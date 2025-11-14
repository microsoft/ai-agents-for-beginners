<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T20:04:07+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "hu"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.hu.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_
# Metakogníció az AI ügynökökben

## Bevezetés

Üdvözlünk a metakognícióval foglalkozó leckében! Ez a fejezet kezdőknek készült, akik kíváncsiak arra, hogyan képesek az AI ügynökök gondolkodni saját gondolkodási folyamataikról. A lecke végére megérted a kulcsfogalmakat, és gyakorlati példákkal leszel felvértezve, hogy alkalmazd a metakogníciót az AI ügynökök tervezésében.

## Tanulási célok

A lecke elvégzése után képes leszel:

1. Megérteni az ügynökdefiníciókban előforduló gondolkodási hurkok következményeit.
2. Tervezési és értékelési technikákat alkalmazni az önjavító ügynökök segítésére.
3. Saját ügynököket létrehozni, amelyek képesek kódot manipulálni a feladatok elvégzéséhez.

## Bevezetés a metakognícióba

A metakogníció olyan magasabb szintű kognitív folyamatokra utal, amelyek magukban foglalják a saját gondolkodásról való gondolkodást. Az AI ügynökök esetében ez azt jelenti, hogy képesek értékelni és módosítani cselekedeteiket önismeret és korábbi tapasztalatok alapján. A metakogníció, vagyis a "gondolkodás a gondolkodásról," kulcsfontosságú az ügynöki AI rendszerek fejlesztésében. Ez magában foglalja, hogy az AI rendszerek tisztában vannak saját belső folyamataikkal, és képesek monitorozni, szabályozni, valamint adaptálni viselkedésüket. Hasonlóan ahhoz, ahogy mi "olvassuk a szobát" vagy megközelítünk egy problémát. Ez az önismeret segíthet az AI rendszereknek jobb döntéseket hozni, hibákat azonosítani és idővel javítani teljesítményüket – ismét visszautalva a Turing-tesztre és az AI jövőjéről szóló vitára.

Az ügynöki AI rendszerek kontextusában a metakogníció segíthet számos kihívás kezelésében, például:
- Átláthatóság: Biztosítja, hogy az AI rendszerek meg tudják magyarázni érvelésüket és döntéseiket.
- Érvelés: Javítja az AI rendszerek képességét az információ szintetizálására és megalapozott döntések meghozatalára.
- Alkalmazkodás: Lehetővé teszi az AI rendszerek számára, hogy új környezetekhez és változó körülményekhez igazodjanak.
- Észlelés: Növeli az AI rendszerek pontosságát a környezetükből származó adatok felismerésében és értelmezésében.

### Mi az a metakogníció?

A metakogníció, vagyis a "gondolkodás a gondolkodásról," egy magasabb szintű kognitív folyamat, amely magában foglalja a saját gondolkodási folyamatok önismeretét és önszabályozását. Az AI területén a metakogníció lehetővé teszi az ügynökök számára, hogy értékeljék és módosítsák stratégiáikat és cselekedeteiket, ami jobb problémamegoldási és döntéshozatali képességekhez vezet. A metakogníció megértésével olyan AI ügynököket tervezhetsz, amelyek nemcsak intelligensebbek, hanem alkalmazkodóbbak és hatékonyabbak is. Valódi metakogníció esetén az AI kifejezetten érvelne saját érveléséről.

Példa: „Az olcsóbb repülőjáratokat részesítettem előnyben, mert... Lehet, hogy kihagyom a közvetlen járatokat, ezért újra ellenőriznem kellene.”
Nyomon követi, hogyan vagy miért választott egy bizonyos útvonalat.
- Megjegyzi, hogy hibázott, mert túlságosan támaszkodott a korábbi felhasználói preferenciákra, ezért nemcsak a végső ajánlást, hanem a döntéshozatali stratégiáját is módosítja.
- Mintázatokat diagnosztizál, például: „Valahányszor a felhasználó említi, hogy 'túl zsúfolt,' nemcsak bizonyos látványosságokat kell eltávolítanom, hanem azt is fel kell ismernem, hogy a 'legnépszerűbb látványosságok' rangsorolási módszerem hibás, ha mindig népszerűség alapján rangsorolok.”

### A metakogníció fontossága az AI ügynökökben

A metakogníció több okból is kulcsfontosságú az AI ügynökök tervezésében:

![A metakogníció fontossága](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.hu.png)

- Önelemzés: Az ügynökök értékelhetik saját teljesítményüket, és azonosíthatják a fejlesztendő területeket.
- Alkalmazkodóképesség: Az ügynökök módosíthatják stratégiáikat a korábbi tapasztalatok és változó környezetek alapján.
- Hibajavítás: Az ügynökök önállóan észlelhetik és javíthatják a hibákat, ami pontosabb eredményekhez vezet.
- Erőforrás-kezelés: Az ügynökök optimalizálhatják az erőforrások, például az idő és a számítási kapacitás felhasználását a cselekvéseik tervezésével és értékelésével.

## Az AI ügynökök összetevői

Mielőtt belemélyednénk a metakognitív folyamatokba, fontos megérteni az AI ügynökök alapvető összetevőit. Egy AI ügynök általában a következőkből áll:

- Persona: Az ügynök személyisége és jellemzői, amelyek meghatározzák, hogyan lép kapcsolatba a felhasználókkal.
- Eszközök: Az ügynök által végrehajtható képességek és funkciók.
- Készségek: Az ügynök által birtokolt tudás és szakértelem.

Ezek az összetevők együtt alkotnak egy "szakértői egységet," amely képes konkrét feladatok elvégzésére.

**Példa**:
Gondolj egy utazási ügynökre, amely nemcsak megtervezi a nyaralásodat, hanem valós idejű adatok és korábbi ügyfélélmények alapján módosítja az útvonalát.

### Példa: Metakogníció egy utazási ügynökségi szolgáltatásban

Képzeld el, hogy egy AI által működtetett utazási ügynökségi szolgáltatást tervezel. Ez az ügynök, "Travel Agent," segíti a felhasználókat nyaralásuk megtervezésében. A metakogníció beépítéséhez a Travel Agentnek önismeret és korábbi tapasztalatok alapján kell értékelnie és módosítania cselekedeteit. Így játszhat szerepet a metakogníció:

#### Jelenlegi feladat

A jelenlegi feladat egy párizsi utazás megtervezése a felhasználó számára.

#### A feladat elvégzésének lépései

1. **Felhasználói preferenciák összegyűjtése**: Kérdezd meg a felhasználót utazási dátumairól, költségvetéséről, érdeklődési köreiről (pl. múzeumok, konyha, vásárlás), és bármilyen konkrét igényéről.
2. **Információk lekérése**: Keress repülőjáratokat, szállásokat, látványosságokat és éttermeket, amelyek megfelelnek a felhasználó preferenciáinak.
3. **Ajánlások generálása**: Készíts személyre szabott útitervet repülőjárat részletekkel, szállásfoglalásokkal és javasolt tevékenységekkel.
4. **Visszajelzés alapján módosítás**: Kérj visszajelzést a felhasználótól az ajánlásokról, és végezd el a szükséges módosításokat.

#### Szükséges erőforrások

- Hozzáférés repülőjárat- és szállásfoglalási adatbázisokhoz.
- Információ párizsi látványosságokról és éttermekről.
- Korábbi interakciókból származó felhasználói visszajelzések.

#### Tapasztalat és önelemzés

A Travel Agent metakogníciót használ teljesítményének értékelésére és korábbi tapasztalatokból való tanulásra. Például:

1. **Felhasználói visszajelzés elemzése**: A Travel Agent áttekinti a felhasználói visszajelzéseket, hogy megállapítsa, mely ajánlások voltak sikeresek, és melyek nem. Ennek megfelelően módosítja jövőbeli javaslatait.
2. **Alkalmazkodóképesség**: Ha egy felhasználó korábban nem kedvelte a zsúfolt helyeket, a Travel Agent a jövőben elkerüli a népszerű turisztikai helyek ajánlását csúcsidőben.
3. **Hibajavítás**: Ha a Travel Agent korábban hibát követett el egy foglalásban, például egy teltházas szálloda ajánlásával, megtanulja, hogy a jövőben alaposabban ellenőrizze a rendelkezésre állást, mielőtt ajánlásokat tesz.

#### Gyakorlati fejlesztői példa

Íme egy egyszerűsített példa arra, hogyan nézhet ki a Travel Agent kódja, amikor metakogníciót alkalmaz:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
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
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
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

#### Miért fontos a metakogníció?

- **Önelemzés**: Az ügynökök elemezhetik teljesítményüket, és azonosíthatják a fejlesztendő területeket.
- **Alkalmazkodóképesség**: Az ügynökök módosíthatják stratégiáikat a visszajelzések és változó körülmények alapján.
- **Hibajavítás**: Az ügynökök önállóan észlelhetik és javíthatják a hibákat.
- **Erőforrás-kezelés**: Az ügynökök optimalizálhatják az erőforrások felhasználását, például az időt és a számítási kapacitást.

A metakogníció beépítésével a Travel Agent személyre szabottabb és pontosabb utazási ajánlásokat nyújthat, javítva a felhasználói élményt.

---

## 2. Tervezés az ügynökökben

A tervezés az AI ügynökök viselkedésének kritikus eleme. Magában foglalja a cél eléréséhez szükséges lépések körvonalazását, figyelembe véve a jelenlegi állapotot, erőforrásokat és lehetséges akadályokat.

### A tervezés elemei

- **Jelenlegi feladat**: A feladat egyértelmű meghatározása.
- **A feladat elvégzésének lépései**: A feladat kezelhető lépésekre bontása.
- **Szükséges erőforrások**: A szükséges erőforrások azonosítása.
- **Tapasztalat**: A korábbi tapasztalatok felhasználása a tervezéshez.

**Példa**:
Íme a lépések, amelyeket a Travel Agentnek meg kell tennie, hogy hatékonyan segítse a felhasználót az utazás megtervezésében:

### A Travel Agent lépései

1. **Felhasználói preferenciák összegyűjtése**
   - Kérdezd meg a felhasználót utazási dátumairól, költségvetéséről, érdeklődési köreiről és bármilyen konkrét igényéről.
   - Példák: „Mikor tervez utazni?” „Mi az Ön költségvetési kerete?” „Milyen tevékenységeket élvez nyaraláskor?”

2. **Információk lekérése**
   - Keress releváns utazási lehetőségeket a felhasználói preferenciák alapján.
   - **Repülőjáratok**: Keress elérhető járatokat a felhasználó költségvetésén és preferált utazási dátumain belül.
   - **Szállások**: Találj szállodákat vagy bérleményeket, amelyek megfelelnek a felhasználó helyszínre, árra és szolgáltatásokra vonatkozó preferenciáinak.
   - **Látványosságok és éttermek**: Azonosíts népszerű látványosságokat, tevékenységeket és étkezési lehetőségeket, amelyek összhangban vannak a felhasználó érdeklődési köreivel.

3. **Ajánlások generálása**
   - Az összegyűjtött információkat személyre szabott útitervvé állítsd össze.
   - Nyújts részleteket, például repülőjáratokat, szállásfoglalásokat és javasolt tevékenységeket, ügyelve arra, hogy az ajánlások megfeleljenek a felhasználó preferenciáinak.

4. **Útiterv bemutatása a felhasználónak**
   - Oszd meg a javasolt útitervet a felhasználóval átnézésre.
   - Példa: „Íme egy javasolt útiterv párizsi utazásához. Tartalmazza a repülőjárat részleteit, szállásfoglalásokat, valamint ajánlott tevékenységek és éttermek listáját. Kérem, ossza meg véleményét!”

5. **Visszajelzés gyűjtése**
   - Kérj visszajelzést a felhasználótól a javasolt útitervről.
   - Példák: „Tetszenek a repülőjárat lehetőségek?” „Megfelel a szálloda az igényeinek?” „Van olyan tevékenység, amit hozzáadna vagy eltávolítana?”

6. **Visszajelzés alapján módosítás**
   - Módosítsd az útitervet a felhasználói visszajelzések alapján.
   - Végezd el a szükséges változtatásokat a repülőjárat, szállás és tevékenység ajánlásokban, hogy jobban megfeleljenek a felhasználó preferenciáinak.

7. **Végső megerősítés**
   - Mutasd be a frissített útitervet a felhasználónak végső megerősítésre.
   - Példa: „Elvégeztem a módosításokat a visszajelzései alapján. Íme a frissített útiterv. Minden rendben van így?”

8. **Foglalások és megerősítések végrehajtása**
   - Miután a felhasználó jóváhagyta az útitervet, folytasd a repülőjáratok, szállások és előre tervezett tevékenységek foglalásával.
   - Küldj megerősítési részleteket a felhasználónak.

9. **Folyamatos támogatás nyújtása**
   - Maradj elérhető, hogy segítséget nyújts a felhasználónak bármilyen változtatás vagy további kérés esetén az utazás előtt és alatt.
   - Példa: „Ha bármilyen további segítségre van szüksége az utazása során, bármikor forduljon hozzám bizalommal!”

### Példa interakció

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

# Example usage within a booing request
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

## 3. Javító RAG rendszer

Először értsük meg a különbséget a RAG eszköz és az előzetes kontextus betöltése között.

![RAG vs Kontextus betöltése](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.hu.png)

### Retrieval-Augmented Generation (RAG)

A RAG egy lek
### Előzetes Kontextus Betöltése

Az előzetes kontextus betöltése azt jelenti, hogy a releváns kontextust vagy háttérinformációt előre betöltjük a modellbe, mielőtt az feldolgozná a lekérdezést. Ez biztosítja, hogy a modell már a kezdetektől hozzáférjen ezekhez az információkhoz, ami segíthet abban, hogy tájékozottabb válaszokat generáljon anélkül, hogy további adatokat kellene lekérnie a folyamat során.

Íme egy egyszerű példa arra, hogyan nézhet ki az előzetes kontextus betöltése egy utazási ügynök alkalmazásban Pythonban:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Magyarázat

1. **Inicializálás (`__init__` metódus)**: A `TravelAgent` osztály előre betölt egy szótárt, amely népszerű úti célokról tartalmaz információkat, például Párizsról, Tokióról, New Yorkról és Sydney-ről. Ez a szótár olyan részleteket tartalmaz, mint az ország, pénznem, nyelv és főbb látványosságok az egyes úti célokhoz.

2. **Információk lekérése (`get_destination_info` metódus)**: Amikor egy felhasználó egy konkrét úti célról érdeklődik, a `get_destination_info` metódus lekéri a releváns információkat az előre betöltött kontextus szótárból.

Az előzetes kontextus betöltésével az utazási ügynök alkalmazás gyorsan tud válaszolni a felhasználói lekérdezésekre anélkül, hogy valós időben kellene külső forrásból információt lekérnie. Ez hatékonyabbá és gyorsabbá teszi az alkalmazást.

### A terv indítása egy céllal, mielőtt iterálnánk

Egy terv indítása egy céllal azt jelenti, hogy egyértelmű célkitűzéssel vagy kívánt eredménnyel kezdjük. Ha ezt a célt előre meghatározzuk, a modell irányelvként használhatja az iterációs folyamat során. Ez segít abban, hogy minden iteráció közelebb vigyen a kívánt eredmény eléréséhez, így a folyamat hatékonyabb és fókuszáltabb lesz.

Íme egy példa arra, hogyan lehet egy utazási tervet egy céllal elindítani, mielőtt iterálnánk egy utazási ügynök alkalmazásban Pythonban:

### Szcenárió

Egy utazási ügynök személyre szabott nyaralást szeretne tervezni egy ügyfél számára. A cél egy olyan utazási terv létrehozása, amely maximalizálja az ügyfél elégedettségét az ő preferenciái és költségvetése alapján.

### Lépések

1. Határozzuk meg az ügyfél preferenciáit és költségvetését.
2. Indítsuk el az alap tervet ezek alapján.
3. Iteráljunk a terv finomítása érdekében, optimalizálva az ügyfél elégedettségét.

#### Python kód

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

# Example usage
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

#### Kódmagyarázat

1. **Inicializálás (`__init__` metódus)**: A `TravelAgent` osztály inicializálva van egy potenciális úti célok listájával, amelyek olyan attribútumokat tartalmaznak, mint név, költség és tevékenységtípus.

2. **Terv indítása (`bootstrap_plan` metódus)**: Ez a metódus létrehoz egy kezdeti utazási tervet az ügyfél preferenciái és költségvetése alapján. Végigmegy az úti célok listáján, és hozzáadja őket a tervhez, ha megfelelnek az ügyfél preferenciáinak és beleférnek a költségvetésbe.

3. **Preferenciák egyeztetése (`match_preferences` metódus)**: Ez a metódus ellenőrzi, hogy egy úti cél megfelel-e az ügyfél preferenciáinak.

4. **Terv iterálása (`iterate_plan` metódus)**: Ez a metódus finomítja a kezdeti tervet azáltal, hogy megpróbálja minden úti célt egy jobb alternatívára cserélni, figyelembe véve az ügyfél preferenciáit és költségvetési korlátait.

5. **Költség kiszámítása (`calculate_cost` metódus)**: Ez a metódus kiszámítja az aktuális terv teljes költségét, beleértve egy potenciális új úti célt is.

#### Példa használat

- **Kezdeti terv**: Az utazási ügynök létrehoz egy kezdeti tervet az ügyfél preferenciái alapján, például városnézés iránti érdeklődés és 2000 dolláros költségvetés.
- **Finomított terv**: Az utazási ügynök iterálja a tervet, optimalizálva az ügyfél preferenciái és költségvetése alapján.

Ha egyértelmű céllal indítjuk a tervet (például az ügyfél elégedettségének maximalizálása), és iterálunk a terv finomítása érdekében, az utazási ügynök személyre szabott és optimalizált utazási tervet hozhat létre az ügyfél számára. Ez a megközelítés biztosítja, hogy az utazási terv már a kezdetektől igazodjon az ügyfél preferenciáihoz és költségvetéséhez, és minden iterációval javuljon.

### Az LLM előnyeinek kihasználása újrarangsorolásra és pontozásra

A Nagy Nyelvi Modellek (LLM-ek) használhatók újrarangsorolásra és pontozásra azáltal, hogy értékelik a lekért dokumentumok vagy generált válaszok relevanciáját és minőségét. Így működik:

**Lekérés:** Az első lépésben a rendszer egy sor jelölt dokumentumot vagy választ keres ki a lekérdezés alapján.

**Újrarangsorolás:** Az LLM értékeli ezeket a jelölteket, és újrarangsorolja őket relevanciájuk és minőségük alapján. Ez a lépés biztosítja, hogy a legrelevánsabb és legjobb minőségű információ kerüljön előre.

**Pontozás:** Az LLM pontszámokat rendel minden jelölthöz, amelyek tükrözik azok relevanciáját és minőségét. Ez segít kiválasztani a legjobb választ vagy dokumentumot a felhasználó számára.

Az LLM-ek újrarangsorolásra és pontozásra való használatával a rendszer pontosabb és kontextusban releváns információt tud nyújtani, javítva a felhasználói élményt.

Íme egy példa arra, hogyan használhat egy utazási ügynök Nagy Nyelvi Modellt (LLM) az úti célok újrarangsorolására és pontozására a felhasználói preferenciák alapján Pythonban:

#### Szcenárió - Utazás preferenciák alapján

Egy utazási ügynök szeretné ajánlani a legjobb úti célokat egy ügyfélnek az ő preferenciái alapján. Az LLM segít újrarangsorolni és pontozni az úti célokat, hogy a legrelevánsabb opciók kerüljenek előtérbe.

#### Lépések:

1. Gyűjtsük össze a felhasználói preferenciákat.
2. Kérjünk le egy listát a potenciális úti célokról.
3. Használjuk az LLM-et az úti célok újrarangsorolására és pontozására a felhasználói preferenciák alapján.

#### Hogyan frissítsük a korábbi példát az Azure OpenAI Services használatával:

#### Követelmények

1. Szükség van egy Azure előfizetésre.
2. Hozzon létre egy Azure OpenAI erőforrást, és szerezze meg az API kulcsát.

#### Példa Python kód

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
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

# Example usage
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

#### Kódmagyarázat - Preferencia alapú ajánló

1. **Inicializálás**: A `TravelAgent` osztály inicializálva van egy potenciális úti célok listájával, amelyek olyan attribútumokat tartalmaznak, mint név és leírás.

2. **Ajánlások lekérése (`get_recommendations` metódus)**: Ez a metódus generál egy promptot az Azure OpenAI szolgáltatáshoz a felhasználói preferenciák alapján, és HTTP POST kérést küld az Azure OpenAI API-nak, hogy újrarangsorolt és pontozott úti célokat kapjon.

3. **Prompt generálása (`generate_prompt` metódus)**: Ez a metódus létrehoz egy promptot az Azure OpenAI számára, amely tartalmazza a felhasználói preferenciákat és az úti célok listáját. A prompt irányítja a modellt az úti célok újrarangsorolására és pontozására a megadott preferenciák alapján.

4. **API hívás**: A `requests` könyvtárat használjuk HTTP POST kérés küldésére az Azure OpenAI API végpontjára. A válasz tartalmazza az újrarangsorolt és pontozott úti célokat.

5. **Példa használat**: Az utazási ügynök összegyűjti a felhasználói preferenciákat (például érdeklődés városnézés és változatos kultúra iránt), és az Azure OpenAI szolgáltatást használja, hogy újrarangsorolt és pontozott ajánlásokat kapjon az úti célokról.

Ne felejtse el lecserélni a `your_azure_openai_api_key` értéket az aktuális Azure OpenAI API kulcsára, és a `https://your-endpoint.com/...` értéket az Azure OpenAI telepítésének tényleges végpont URL-jére.

Az LLM újrarangsorolásra és pontozásra való használatával az utazási ügynök személyre szabottabb és relevánsabb utazási ajánlásokat tud nyújtani az ügyfeleknek, javítva ezzel az általános élményt.
#### Gyakorlati példa: Keresés szándékkal az Utazási Ügynökben

Vegyük példának az Utazási Ügynököt, hogy lássuk, hogyan valósítható meg a keresés szándékkal.

1. **Felhasználói preferenciák összegyűjtése**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Felhasználói szándék megértése**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Környezet tudatosság**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Keresés és eredmények személyre szabása**

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
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Példa használat**

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

## 4. Kód generálása mint eszköz

A kódgeneráló ügynökök AI modelleket használnak kód írására és futtatására, komplex problémák megoldására és feladatok automatizálására.

### Kódgeneráló ügynökök

A kódgeneráló ügynökök generatív AI modelleket használnak kód írására és futtatására. Ezek az ügynökök képesek komplex problémák megoldására, feladatok automatizálására, és értékes betekintéseket nyújtanak különböző programozási nyelveken írt kód generálásával és futtatásával.

#### Gyakorlati alkalmazások

1. **Automatikus kódgenerálás**: Kódrészletek generálása specifikus feladatokhoz, például adat-elemzéshez, webes adatgyűjtéshez vagy gépi tanuláshoz.
2. **SQL mint RAG**: SQL lekérdezések használata adatbázisokból történő adatok lekérésére és manipulálására.
3. **Problémamegoldás**: Kód létrehozása és futtatása specifikus problémák megoldására, például algoritmusok optimalizálására vagy adatok elemzésére.

#### Példa: Kódgeneráló ügynök adat-elemzéshez

Képzeljük el, hogy egy kódgeneráló ügynököt tervezünk. Így működhet:

1. **Feladat**: Egy adatállomány elemzése trendek és minták azonosítására.
2. **Lépések**:
   - Az adatállomány betöltése egy adat-elemző eszközbe.
   - SQL lekérdezések generálása az adatok szűrésére és összesítésére.
   - A lekérdezések futtatása és az eredmények lekérése.
   - Az eredmények felhasználása vizualizációk és betekintések generálására.
3. **Szükséges erőforrások**: Hozzáférés az adatállományhoz, adat-elemző eszközök és SQL képességek.
4. **Tapasztalat**: Korábbi elemzési eredmények felhasználása a jövőbeli elemzések pontosságának és relevanciájának javítására.

### Példa: Kódgeneráló ügynök az Utazási Ügynök számára

Ebben a példában egy kódgeneráló ügynököt tervezünk, az Utazási Ügynököt, amely segíti a felhasználókat az utazásuk megtervezésében kód generálásával és futtatásával. Ez az ügynök olyan feladatokat képes kezelni, mint utazási lehetőségek lekérése, eredmények szűrése és egy útiterv összeállítása generatív AI segítségével.

#### A kódgeneráló ügynök áttekintése

1. **Felhasználói preferenciák összegyűjtése**: Felhasználói adatok gyűjtése, mint például úti cél, utazási dátumok, költségvetés és érdeklődési körök.
2. **Kód generálása adatok lekérésére**: Kódrészletek generálása repülőjáratok, szállodák és látnivalók adatainak lekérésére.
3. **Generált kód futtatása**: A generált kód futtatása valós idejű információk lekérésére.
4. **Útiterv generálása**: Az összegyűjtött adatokból személyre szabott utazási terv összeállítása.
5. **Visszajelzés alapján történő módosítás**: Felhasználói visszajelzések fogadása és szükség esetén a kód újragenerálása az eredmények finomításához.

#### Lépésről lépésre történő megvalósítás

1. **Felhasználói preferenciák összegyűjtése**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Kód generálása adatok lekérésére**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Generált kód futtatása**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
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

4. **Útiterv generálása**

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

5. **Visszajelzés alapján történő módosítás**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Környezeti tudatosság és érvelés kihasználása

A táblázat séma alapján történő lekérdezés-generálás folyamata jelentősen javítható környezeti tudatosság és érvelés alkalmazásával.

Íme egy példa arra, hogyan valósítható ez meg:

1. **Séma megértése**: A rendszer megérti a táblázat sémáját, és ezt az információt használja a lekérdezés-generálás alapjaként.
2. **Visszajelzés alapján történő módosítás**: A rendszer a felhasználói visszajelzések alapján módosítja a preferenciákat, és érvel arról, hogy mely mezőket kell frissíteni a sémában.
3. **Lekérdezések generálása és futtatása**: A rendszer lekérdezéseket generál és futtat, hogy frissített repülőjárat- és szállodai adatokat kérjen le az új preferenciák alapján.

Íme egy frissített Python kód példa, amely ezeket a koncepciókat tartalmazza:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Magyarázat - Foglalás visszajelzés alapján

1. **Séma tudatosság**: A `schema` szótár meghatározza, hogyan kell a preferenciákat módosítani a visszajelzések alapján. Olyan mezőket tartalmaz, mint `favorites` és `avoid`, a megfelelő módosításokkal.
2. **Preferenciák módosítása (`adjust_based_on_feedback` metódus)**: Ez a metódus a preferenciákat módosítja a felhasználói visszajelzések és a séma alapján.
3. **Környezeti alapú módosítások (`adjust_based_on_environment` metódus)**: Ez a metódus testre szabja a módosításokat a séma és a visszajelzések alapján.
4. **Lekérdezések generálása és futtatása**: A rendszer kódot generál, hogy frissített repülőjárat- és szállodai adatokat kérjen le a módosított preferenciák alapján, és szimulálja ezeknek a lekérdezéseknek a futtatását.
5. **Útiterv generálása**: A rendszer frissített útitervet hoz létre az új repülőjárat-, szálloda- és látnivaló-adatok alapján.

A rendszer környezeti tudatosságának és a séma alapján történő érvelésének köszönhetően pontosabb és relevánsabb lekérdezéseket generálhat, ami jobb utazási ajánlásokat és személyre szabottabb felhasználói élményt eredményez.

### SQL használata Retrieval-Augmented Generation (RAG) technikaként

Az SQL (Structured Query Language) egy hatékony eszköz az adatbázisokkal való interakcióhoz. Ha a Retrieval-Augmented Generation (RAG) megközelítés részeként használjuk, az SQL képes releváns adatokat lekérni az adatbázisokból, hogy információt nyújtson és válaszokat vagy műveleteket generáljon AI ügynökökben. Nézzük meg, hogyan használható az SQL RAG technikaként az Utazási Ügynök kontextusában.

#### Kulcskoncepciók

1. **Adatbázis interakció**:
   - Az SQL-t adatbázisok lekérdezésére, releváns információk lekérésére és adatok manipulálására használják.
   - Példa: Repülőjáratok, szállodák és látnivalók adatainak lekérése egy utazási adatbázisból.

2. **Integráció a RAG-gal**:
   - Az SQL lekérdezéseket a felhasználói bemenetek és preferenciák alapján generálják.
   - A lekért adatokat személyre szabott ajánlások vagy műveletek generálására használják.

3. **Dinamikus lekérdezés-generálás**:
   - Az AI ügynök dinamikus SQL lekérdezéseket generál a kontextus és a felhasználói igények alapján.
   - Példa: SQL lekérdezések testreszabása az eredmények szűrésére költségvetés, dátumok és érdeklődési körök alapján.

#### Alkalmazások

- **Automatikus kódgenerálás**: Kódrészletek generálása specifikus feladatokhoz.
- **SQL mint RAG**: SQL lekérdezések használata adatok manipulálására.
- **Problémamegoldás**: Kód létrehozása és futtatása problémák megoldására.

**Példa**:
Egy adat-elemző ügynök:

1. **Feladat**: Egy adatállomány elemzése trendek azonosítására.
2. **Lépések**:
   - Az adatállomány betöltése.
   - SQL lekérdezések generálása az adatok szűrésére.
   - Lekérdezések futtatása és eredmények lekérése.
   - Vizualizációk és betekintések generálása.
3. **Erőforrások**: Adatállomány hozzáférés, SQL képességek.
4. **Tapasztalat**: Korábbi eredmények felhasználása a jövőbeli elemzések javítására.

#### Gyakorlati példa: SQL használata az Utazási Ügynökben

1. **Felhasználói preferenciák összegyűjtése**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL lekérdezések generálása**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL lekérdezések futtatása**

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

4. **Ajánlások generálása**

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

#### Példa SQL lekérdezések

1. **Repülőjárat lekérdezés**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Szálloda lekérdezés**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Látnivaló lekérdezés**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Az SQL Retrieval-Augmented Generation (RAG) technika részeként történő alkalmazásával az AI ügynökök, mint az Utazási Ügynök, dinamikusan lekérhetik és felhasználhatják a releváns adatokat, hogy pontos és személyre szabott ajánlásokat nyújtsanak.

### Metakogníció példája

A metakogníció megvalósításának bemutatására hozzunk létre egy egyszerű ügynököt, amely *reflektál a döntéshozatali folyamatára* probléma megoldása közben. Ebben a példában egy rendszert építünk, ahol az ügynök megpróbálja optimalizálni egy szálloda kiválasztását, majd értékeli saját érvelését, és módosítja stratégiáját, ha hibát vagy nem optimális választást tesz.

Egy alapvető példát szimulálunk, ahol az ügynök szállodákat választ ár és minőség kombinációja alapján, de "reflektál" a döntéseire, és ennek megfelelően módosít.

#### Hogyan illusztrálja ez a metakogníciót:

1. **Kezdeti döntés**: Az ügynök a legolcsóbb szállodát választja, anélkül hogy megértené a minőség hatását.
2. **Reflexió és értékelés**: Az első választás után az ügynök ellenőrzi, hogy a szálloda "rossz" választás volt-e a felhasználói visszajelzések alapján. Ha azt találja, hogy a szálloda minősége túl alacsony volt, reflektál az érvelésére.
3. **Stratégia módosítása**: Az ügynök módosítja stratégiáját a reflexió alapján, és a "legolcsóbb" helyett a "legjobb minőségű" opciót választja, így javítva a döntéshozatali folyamatot a jövőben.

Íme egy példa:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

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
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
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

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Az ügynök metakognitív képességei

A kulcs itt az ügynök képessége:
- Értékelni korábbi választásait és döntéshozatali folyamatát.
- Stratégiáját módosítani a reflexió alapján, azaz metakogníciót alkalmazni.

Ez egy egyszerű formája a metakogníciónak, ahol a rendszer képes módosítani érvelési folyamatát belső visszajelzések alapján.

### Összegzés

A metakogníció egy erőteljes eszköz, amely jelentősen növelheti az AI ügynökök képességeit. A metakognitív folyamatok beépítésével intelligensebb, alkalmazkodóbb és hatékonyabb ügynököket tervezhetünk. Használja a további forrásokat, hogy mélyebben felfedezze a metakogníció lenyűgöző világát az AI ügynökökben.

### További kérdése van a metakogníció tervezési mintájával kapcsolatban?

Csatlakozzon az [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozzon más tanulókkal, részt vegyen konzultációkon, és választ kapjon AI ügynökökkel kapcsolatos kérdéseire.

## Előző lecke

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Következő lecke

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.