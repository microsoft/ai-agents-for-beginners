[![Multi-Agent Design](../../../translated_images/sk/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_
# Metakognícia v AI agentoch

## Úvod

Vitajte v lekcii o metakognícii v AI agentoch! Táto kapitola je určená pre začiatočníkov, ktorí sa zaujímajú o to, ako môžu AI agenti premýšľať o vlastných procesoch myslenia. Na konci tejto lekcie porozumiete kľúčovým konceptom a budete vybavení praktickými príkladmi na aplikáciu metakognície v dizajne AI agentov.

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

1. Pochopiť dôsledky slučiek uvažovania v definíciách agentov.
2. Použiť plánovacie a hodnotiace techniky na pomoc samokorigujúcim agentom.
3. Vytvoriť vlastných agentov schopných manipulovať s kódom na splnenie úloh.

## Úvod do metakognície

Metakognícia sa vzťahuje na vyššie poradie kognitívnych procesov, ktoré zahŕňajú premýšľanie o vlastnom myslení. Pre AI agentov to znamená schopnosť vyhodnotiť a upraviť svoje konanie na základe seba-vedomia a minulých skúseností. Metakognícia, alebo „premýšľanie o myslení“, je dôležitý koncept vo vývoji agentných AI systémov. Zahŕňa AI systémy, ktoré si uvedomujú svoje vlastné vnútorné procesy a sú schopné monitorovať, regulovať a prispôsobovať svoje správanie podľa toho. Podobne ako keď my vyhodnocujeme situáciu alebo riešime problém. Toto sebauvedomenie môže pomôcť AI systémom robiť lepšie rozhodnutia, identifikovať chyby a zlepšovať svoj výkon v priebehu času – opäť sa odkazujúce na Turingov test a diskusiu o tom, či AI prevezme kontrolu.

V kontexte agentných AI systémov môže metakognícia pomôcť riešiť niekoľko výziev, ako sú:
- Transparentnosť: Zabezpečenie, že AI systémy dokážu vysvetliť svoje uvažovanie a rozhodnutia.
- Uvažovanie: Zlepšenie schopnosti AI systémov syntetizovať informácie a robiť správne rozhodnutia.
- Adaptácia: Umožnenie AI systémom prispôsobiť sa novým prostrediam a meniacim sa podmienkam.
- Vnímanie: Zlepšenie presnosti AI systémov pri rozpoznávaní a interpretácii údajov zo svojho okolia.

### Čo je metakognícia?

Metakognícia, alebo „premýšľanie o myslení“, je vyšší kognitívny proces, ktorý zahŕňa sebauvedomenie a samoreguláciu vlastných kognitívnych procesov. V oblasti AI umožňuje metakognícia agentom vyhodnocovať a prispôsobovať svoje stratégie a činnosti, čo vedie k lepším schopnostiam riešenia problémov a rozhodovania. Pochopením metakognície môžete navrhovať AI agentov, ktorí nie sú len inteligentnejší, ale aj adaptabilnejší a efektívnejší. Pri skutočnej metakognícii by ste videli, ako AI explicitne uvažuje o svojom vlastnom uvažovaní.

Príklad: „Uprednostnil som lacnejšie lety, pretože... Môžem prehliadať priame lety, takže si to znova skontrolujem.“.
Sledovanie, ako alebo prečo si vybral určitú trasu.
- Uvedomenie si, že urobil chyby, pretože príliš spolahl na používateľské preferencie z minulosti, a tak modifikuje svoju stratégiu rozhodovania, nie len konečné odporúčanie.
- Diagnostikovanie vzorcov ako: „Kedykoľvek používateľ spomenie ‚príliš preplnené‘, nemal by som len odstrániť určité atrakcie, ale aj zvážiť, že moja metóda vyberania ‚najlepších atrakcií‘ je chybná, ak vždy hodnotím podľa popularity.“

### Význam metakognície v AI agentoch

Metakognícia zohráva kľúčovú úlohu v dizajne AI agentov z niekoľkých dôvodov:

![Importance of Metacognition](../../../translated_images/sk/importance-of-metacognition.b381afe9aae352f7.webp)

- Sebareflexia: Agenti môžu hodnotiť svoj výkon a identifikovať oblasti na zlepšenie.
- Adaptabilita: Agenti môžu upravovať svoje stratégie na základe minulých skúseností a meniaceho sa prostredia.
- Oprava chýb: Agenti môžu samostatne odhaľovať a korigovať chyby, čo vedie k presnejším výsledkom.
- Správa zdrojov: Agenti môžu optimalizovať využitie zdrojov, ako je čas a výpočtový výkon, plánovaním a hodnotením svojich akcií.

## Komponenty AI agenta

Predtým, než sa pustíme do metakognitívnych procesov, je nevyhnutné pochopiť základné komponenty AI agenta. AI agent obvykle pozostáva z:

- Persona: Osobnosť a charakteristiky agenta, ktoré definujú, ako komunikuje s používateľmi.
- Nástroje: Schopnosti a funkcie, ktoré agent dokáže vykonávať.
- Zručnosti: Vedomosti a odborné znalosti, ktoré agent vlastní.

Tieto komponenty spolupracujú na vytvorenie „jednotky odbornosti“, ktorá môže vykonávať konkrétne úlohy.

**Príklad**:
Predstavte si cestovného agenta, ktorý nielen plánuje vašu dovolenku, ale aj prispôsobuje trasu na základe údajov v reálnom čase a skúseností z predchádzajúcich zákazníckych ciest.

### Príklad: Metakognícia v službe cestovného agenta

Predstavte si, že navrhujete službu cestovného agenta poháňanú AI. Tento agent, „Cestovný agent“, pomáha používateľom plánovať dovolenky. Aby ste začlenili metakogníciu, Cestovný agent potrebuje vyhodnocovať a upravovať svoje akcie na základe sebauvedomenia a minulých skúseností. Tu je, ako by metakognícia mohla hrať úlohu:

#### Aktuálna úloha

Aktuálnou úlohou je pomôcť používateľovi naplánovať cestu do Paríža.

#### Kroky na dokončenie úlohy

1. **Zber používateľských preferencií**: Opýtajte sa používateľa na dátumy cesty, rozpočet, záujmy (napr. múzeá, kuchyňa, nakupovanie) a akékoľvek špecifické požiadavky.
2. **Získanie informácií**: Vyhľadajte možnosti letov, ubytovania, atrakcií a reštaurácií, ktoré zodpovedajú preferenciám používateľa.
3. **Generovanie odporúčaní**: Poskytnite personalizovaný itinerár s detailmi letov, rezerváciami hotelov a navrhovanými aktivitami.
4. **Úprava na základe spätnej väzby**: Požiadajte používateľa o spätnú väzbu na odporúčania a vykonajte potrebné úpravy.

#### Potrebné zdroje

- Prístup k databázam rezervácií letov a hotelov.
- Informácie o parížskych atrakciách a reštauráciách.
- Dáta spätnej väzby od používateľov z predchádzajúcich interakcií.

#### Skúsenosti a sebareflexia

Cestovný agent používa metakogníciu na vyhodnocovanie svojho výkonu a učenie sa z minulých skúseností. Napríklad:

1. **Analýza spätnej väzby používateľa**: Cestovný agent prehodnocuje spätnú väzbu, aby zistil, ktoré odporúčania boli dobre prijaté a ktoré nie. Podľa toho upravuje svoje budúce návrhy.
2. **Adaptabilita**: Ak používateľ predtým spomenul, že nemá rád preplnené miesta, Cestovný agent sa v budúcnosti vyhne odporúčaniu populárnych turistických miest v najvyťaženejších časoch.
3. **Oprava chýb**: Ak Cestovný agent urobil chybu pri rezervácii, napríklad navrhol hotel, ktorý bol plne obsadený, naučí sa dôkladnejšie kontrolovať dostupnosť pred podaním odporúčaní.

#### Praktický príklad pre vývojára

Tu je zjednodušený príklad kódu Cestovného agenta, ktorý zahŕňa metakogníciu:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Vyhľadávanie letov, hotelov a atrakcií na základe preferencií
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
        # Analyzovať spätnú väzbu a upraviť budúce odporúčania
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Príklad použitia
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

#### Prečo je metakognícia dôležitá

- **Sebareflexia**: Agenti môžu analyzovať svoj výkon a identifikovať oblasti na zlepšenie.
- **Adaptabilita**: Agenti môžu upravovať stratégie na základe spätnej väzby a meniacich sa podmienok.
- **Oprava chýb**: Agenti môžu autonómne odhaľovať a opravovať chyby.
- **Správa zdrojov**: Agenti môžu optimalizovať využívanie zdrojov, ako je čas a výpočtový výkon.

Začlenením metakognície môže Cestovný agent poskytovať personalizovanejšie a presnejšie cestovné odporúčania, čím zlepšuje celkový používateľský zážitok.

---

## 2. Plánovanie v agentoch

Plánovanie je kľúčovou súčasťou správania AI agenta. Zahŕňa načrtnutie krokov potrebných na dosiahnutie cieľa, zohľadňujúc aktuálny stav, zdroje a možné prekážky.

### Prvky plánovania

- **Aktuálna úloha**: Jasne definovať úlohu.
- **Kroky na dokončenie úlohy**: Rozložiť úlohu na spravovateľné kroky.
- **Potrebné zdroje**: Identifikovať potrebné zdroje.
- **Skúsenosti**: Využiť minulé skúsenosti na podporu plánovania.

**Príklad**:
Tu sú kroky, ktoré musí Cestovný agent vykonať, aby účinne pomohol používateľovi plánovať jeho cestu:

### Kroky pre Cestovného agenta

1. **Zber používateľských preferencií**
   - Opýtajte sa používateľa na detaily o dátumoch cesty, rozpočte, záujmoch a akýchkoľvek špecifických požiadavkách.
   - Príklady: „Kedy plánujete cestovať?“ „Aký je váš rozpočtový rozsah?“ „Aké aktivity si užívate na dovolenke?“

2. **Získanie informácií**
   - Vyhľadajte relevantné možnosti cestovania na základe preferencií používateľa.
   - **Lety**: Nájdite dostupné lety v rámci rozpočtu a preferovaných dátumov.
   - **Ubytovanie**: Nájdite hotely alebo prenájmy, ktoré zodpovedajú preferenciám používateľa čo sa týka lokality, ceny a vybavenia.
   - **Atrakcie a reštaurácie**: Identifikujte populárne atrakcie, aktivity a možnosti stravovania, ktoré sú v súlade so záujmami používateľa.

3. **Generovanie odporúčaní**
   - Zostavte získané informácie do personalizovaného itinerára.
   - Poskytnite detaily, ako sú možnosti letov, rezervácie hotelov a navrhované aktivity, pričom sa uistite, že odporúčania zodpovedajú preferenciám používateľa.

4. **Predstavenie itinerára používateľovi**
   - Zdieľajte navrhovaný itinerár na posúdenie používateľom.
   - Príklad: „Tu je navrhovaný itinerár pre vašu cestu do Paríža. Obsahuje detaily letov, rezervácie hotelov a zoznam odporúčaných aktivít a reštaurácií. Dajte mi vedieť vaše názory!“

5. **Zber spätnej väzby**
   - Požiadajte používateľa o spätnú väzbu na navrhovaný itinerár.
   - Príklady: „Páčia sa vám možnosti letov?“ „Je hotel vhodný pre vaše potreby?“ „Chceli by ste niečo pridať alebo odstrániť?“

6. **Úprava podľa spätnej väzby**
   - Upraviť itinerár na základe spätnej väzby používateľa.
   - Vykonať potrebné zmeny v odporúčaniach týkajúcich sa letu, ubytovania a aktivít, aby lepšie zodpovedali preferenciám používateľa.

7. **Konečné potvrdenie**
   - Predložiť aktualizovaný itinerár používateľovi na finálne potvrdenie.
   - Príklad: „Urobil som úpravy podľa vašej spätnej väzby. Tu je upravený itinerár. Vyzerá všetko v poriadku?“

8. **Rezervácia a potvrdenie**
   - Po schválení itinerára používateľom pokračujte s rezerváciou letov, ubytovania a predpripravených aktivít.
   - Pošlite používateľovi potvrdenie.

9. **Poskytovanie priebežnej podpory**
   - Buďte k dispozícii na pomoc používateľovi so zmenami alebo ďalšími požiadavkami pred cestou a počas nej.
   - Príklad: „Ak budete počas cesty potrebovať ďalšiu pomoc, neváhajte sa na mňa kedykoľvek obrátiť!“

### Príklad interakcie

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

# Príklad použitia v rámci požiadavky na bookovanie
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

## 3. Korektívny RAG systém

Najskôr si poďme vysvetliť rozdiel medzi RAG nástrojom a preemptívnym načítaním kontextu.

![RAG vs Context Loading](../../../translated_images/sk/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinuje systém vyhľadávania s generatívnym modelom. Keď je zadaný dopyt, vyhľadávací systém získava relevantné dokumenty alebo dáta z externého zdroja a tieto získané informácie sa používajú na rozšírenie vstupu generatívneho modelu. To pomáha modelu vytvárať presnejšie a kontextovo relevantnejšie odpovede.

V RAG systéme agent získava relevantné informácie z databázy znalostí a používa ich na generovanie vhodných odpovedí alebo akcií.

### Korektívny RAG prístup

Korektívny RAG prístup sa zameriava na použitie RAG techník na opravu chýb a zlepšenie presnosti AI agentov. To zahŕňa:

1. **Technika podnetov**: Použitie špecifických podnetov na riadenie agenta pri vyhľadávaní relevantných informácií.
2. **Nástroj**: Implementácia algoritmov a mechanizmov umožňujúcich agentovi vyhodnocovať relevantnosť získaných informácií a generovať presné odpovede.
3. **Hodnotenie**: Neustále hodnotenie výkonu agenta a vykonávanie úprav na zlepšenie jeho presnosti a efektivity.

#### Príklad: Korektívny RAG v agentovi na vyhľadávanie

Predstavte si agenta na vyhľadávanie, ktorý získava informácie z webu na odpovedanie na otázky používateľov. Korektívny RAG prístup by mohol zahŕňať:

1. **Technika podnetov**: Formulovanie vyhľadávacích dopytov na základe vstupu používateľa.
2. **Nástroj**: Použitie spracovania prirodzeného jazyka a algoritmov strojového učenia na hodnotenie a filtrovanie výsledkov vyhľadávania.
3. **Hodnotenie**: Analýza spätnej väzby používateľov na identifikáciu a opravu nepresností vo získaných informáciách.

### Korektívny RAG v Cestovnom agentovi

Korektívny RAG (Retrieval-Augmented Generation) zvyšuje schopnosť AI získavať a generovať informácie, pričom opravuje akékoľvek nepresnosti. Pozrime sa, ako môže Cestovný agent využiť korektívny RAG prístup na poskytovanie presnejších a relevantnejších cestovných odporúčaní.

To zahŕňa:

- **Technika podnetov:** Použitie špecifických podnetov na riadenie agenta pri vyhľadávaní relevantných informácií.
- **Nástroj:** Implementácia algoritmov a mechanizmov, ktoré umožňujú agentovi vyhodnocovať relevantnosť získaných informácií a generovať presné odpovede.
- **Hodnotenie:** Neustále hodnotenie výkonu agenta a vykonávanie úprav na zlepšenie jeho presnosti a efektivity.

#### Kroky implementácie korektívneho RAG v Cestovnom agentovi

1. **Počiatočná interakcia s používateľom**
   - Cestovný agent zhromažďuje počiatočné preferencie od používateľa, ako sú cieľ, dátumy cesty, rozpočet a záujmy.
   - Príklad:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Získavanie informácií**
   - Cestovný agent získava informácie o letoch, ubytovaní, atrakciách a reštauráciách na základe preferencií používateľa.
   - Príklad:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generovanie počiatočných odporúčaní**
   - Cestovný agent používa získané informácie na vytvorenie personalizovaného itinerára.
   - Príklad:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Zber spätnej väzby od používateľa**
   - Cestovný agent žiada používateľa o spätnú väzbu na počiatočné odporúčania.
   - Príklad:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces korektívneho RAG**
   - **Technika podnetov**: Cestovný agent formuluje nové vyhľadávacie dopyty na základe spätnej väzby používateľa.
     - Príklad:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Nástroj**: Cestovný agent využíva algoritmy na hodnotenie a filtrovanie nových výsledkov vyhľadávania, pričom zdôrazňuje relevanciu na základe spätnej väzby.
     - Príklad:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Hodnotenie**: Cestovný agent neustále vyhodnocuje relevantnosť a presnosť svojich odporúčaní analýzou spätnej väzby používateľa a vykonáva potrebné úpravy.
     - Príklad:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktický príklad

Tu je zjednodušený príklad kódu v Pythone, ktorý zahrňuje korektívny RAG prístup v Cestovnom agentovi:

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

# Príklad použitia
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

### Preemptívne načítanie kontextu


Pre-emptívne načítanie kontextu zahŕňa načítanie relevantného kontextu alebo základných informácií do modelu pred spracovaním dotazu. To znamená, že model má prístup k týmto informáciám od začiatku, čo mu môže pomôcť generovať lepšie informované odpovede bez potreby získavania ďalších údajov počas procesu.

Tu je zjednodušený príklad, ako by mohlo vyzerať pre-emptívne načítanie kontextu pre aplikáciu cestovnej kancelárie v Pythone:

```python
class TravelAgent:
    def __init__(self):
        # Prednačítanie obľúbených destinácií a ich informácií
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Získanie informácií o destinácii z prednačítaného kontextu
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Príklad použitia
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Vysvetlenie

1. **Inicializácia (metóda `__init__`)**: Trieda `TravelAgent` prednačítava slovník obsahujúci informácie o populárnych destináciách, ako sú Paríž, Tokio, New York a Sydney. Tento slovník zahŕňa detaily ako krajina, mena, jazyk a hlavné atrakcie každej destinácie.

2. **Získavanie informácií (metóda `get_destination_info`)**: Keď používateľ položí otázku o konkrétnej destinácii, metóda `get_destination_info` načíta relevantné informácie zo prednačítaného slovníka kontextu.

Prednačítavaním kontextu môže aplikácia cestovnej kancelárie rýchlo odpovedať na používateľské otázky bez nutnosti v reálnom čase získavať tieto informácie z externého zdroja. Toto robí aplikáciu efektívnejšou a responzívnejšou.

### Inicializácia plánu s cieľom pred iteráciou

Inicializácia plánu s cieľom znamená začať s jasným cieľom alebo želaným výsledkom na mysli. Definovaním tohto cieľa od začiatku môže model používať tento cieľ ako vodítko počas celého iteratívneho procesu. Pomáha to zabezpečiť, že každá iterácia sa približuje k dosiahnutiu požadovaného výsledku, čím sa proces stáva efektívnejším a zameraným.

Tu je príklad, ako môžete inicializovať cestovný plán s cieľom pred iteráciou pre cestovnú kanceláriu v Pythone:

### Scenár

Cestovná kancelária chce naplánovať zákaznícku dovolenku na mieru. Cieľom je vytvoriť cestovný itinerár, ktorý maximalizuje spokojnosť klienta na základe jeho preferencií a rozpočtu.

### Kroky

1. Definovať preferencie a rozpočet klienta.
2. Inicializovať počiatočný plán na základe týchto preferencií.
3. Iterovať a zdokonaľovať plán, optimalizujúc pre spokojnosť klienta.

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

# Príklad použitia
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

#### Vysvetlenie kódu

1. **Inicializácia (metóda `__init__`)**: Trieda `TravelAgent` je inicializovaná s zoznamom potenciálnych destinácií, z ktorých každá má atribúty ako názov, cena a typ aktivity.

2. **Inicializácia plánu (metóda `bootstrap_plan`)**: Táto metóda vytvorí počiatočný cestovný plán na základe preferencií a rozpočtu klienta. Prechádza zoznam destinácií a pridáva ich do plánu, ak zodpovedajú preferenciám klienta a zmestia sa do rozpočtu.

3. **Zhodnotenie preferencií (metóda `match_preferences`)**: Táto metóda kontroluje, či destinácia zodpovedá preferenciám klienta.

4. **Iterácia plánu (metóda `iterate_plan`)**: Táto metóda zdokonaľuje počiatočný plán tým, že sa snaží nahradiť každú destináciu v pláne lepšou voľbou, zohľadňujúc preferencie klienta a rozpočtové obmedzenia.

5. **Výpočet ceny (metóda `calculate_cost`)**: Táto metóda vypočíta celkové náklady aktuálneho plánu vrátane potenciálnej novej destinácie.

#### Príklad použitia

- **Počiatočný plán**: cestovná kancelária vytvorí počiatočný plán na základe preferencií klienta pre poznávanie pamiatok a rozpočtu 2000 $.
- **Zdokonalený plán**: cestovná kancelária iteruje plán a optimalizuje ho podľa preferencií a rozpočtu klienta.

Inicializáciou plánu s jasným cieľom (napr. maximalizovať spokojnosť klienta) a iteráciou na jeho zdokonalenie môže cestovná kancelária vytvoriť prispôsobený a optimalizovaný cestovný itinerár pre klienta. Tento prístup zabezpečuje, že cestovný plán od začiatku zodpovedá preferenciám a rozpočtu klienta a postupne sa zlepšuje.

### Využitie LLM na pretriedenie a skórovanie

Veľké jazykové modely (LLM) je možné použiť na pretriedenie a skórovanie vyhľadaných dokumentov alebo generovaných odpovedí hodnotením ich relevantnosti a kvality. Funguje to takto:

**Vyhľadávanie:** Počiatočný krok vyhľadávania získa sadu kandidátskych dokumentov alebo odpovedí na základe dotazu.

**Pretriedenie:** LLM vyhodnotí týchto kandidátov a usporiada ich podľa relevantnosti a kvality. Tento krok zabezpečuje, že na začiatku sú prezentované najrelevantnejšie a najkvalitnejšie informácie.

**Skórovanie:** LLM pridá každému kandidátovi skóre, ktoré odráža jeho relevantnosť a kvalitu. To pomáha vybrať najlepšiu odpoveď alebo dokument pre používateľa.

Využitím LLM na pretriedenie a skórovanie môže systém poskytovať presnejšie a kontextovo relevantné informácie, čím zlepšuje celkový používateľský zážitok.

Tu je príklad, ako by cestovná kancelária mohla použiť veľký jazykový model (LLM) na pretriedenie a skórovanie cestovných destinácií na základe preferencií používateľa v Pythone:

#### Scenár - Cestovanie na základe preferencií

Cestovná kancelária chce klientovi odporučiť najlepšie cestovné destinácie na základe jeho preferencií. LLM pomôže pretriediť a skórovať destinácie tak, aby sa prezentovali tie najrelevantnejšie možnosti.

#### Kroky:

1. Získať používateľské preferencie.
2. Získať zoznam potenciálnych cestovných destinácií.
3. Použiť LLM na pretriedenie a skórovanie destinácií na základe používateľských preferencií.

Tu je návod, ako môžete aktualizovať predošlý príklad na použitie Azure OpenAI služieb:

#### Požiadavky

1. Musíte mať Azure predplatné.
2. Vytvoriť Azure OpenAI zdroj a získať svoj API kľúč.

#### Príklad Python kódu

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Vygenerujte prompt pre Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definujte hlavičky a obsah požiadavky
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Zavolajte Azure OpenAI API, aby ste získali opätovne zoradené a ohodnotené destinácie
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extrahujte a vráťte odporúčania
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

# Príklad použitia
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

#### Vysvetlenie kódu - Rezervátor preferencií

1. **Inicializácia**: Trieda `TravelAgent` je inicializovaná so zoznamom potenciálnych cestovných destinácií, z ktorých každá má atribúty ako názov a popis.

2. **Získavanie odporúčaní (metóda `get_recommendations`)**: Táto metóda generuje prompt pre službu Azure OpenAI na základe preferencií používateľa a vykonáva HTTP POST požiadavku na API Azure OpenAI, aby získala pretriedené a skórované destinácie.

3. **Generovanie promptu (metóda `generate_prompt`)**: Táto metóda vytvára prompt pre Azure OpenAI, vrátane používateľských preferencií a zoznamu destinácií. Prompt vedie model k pretriedeniu a skórovaniu destinácií na základe poskytnutých preferencií.

4. **Volanie API**: Na vykonanie HTTP POST požiadavky na endpoint Azure OpenAI API sa používa knižnica `requests`. Odpoveď obsahuje pretriedené a skórované destinácie.

5. **Príklad použitia**: Cestovná kancelária zhromažďuje používateľské preferencie (napr. záujem o poznávanie pamiatok a rôznorodú kultúru) a používa službu Azure OpenAI, aby získala pretriedené a skórované odporúčania cestovných destinácií.

Nezabudnite nahradiť `your_azure_openai_api_key` vaším skutočným API kľúčom Azure OpenAI a `https://your-endpoint.com/...` skutočnou URL adresou endpointu vašej Azure OpenAI implementácie.

Využitím LLM na pretriedenie a skórovanie môže cestovná kancelária poskytnúť osobnejšie a relevantnejšie cestovné odporúčania klientom, čím zlepší ich celkový zážitok.

### RAG: Technika promptovania vs. nástroj

Retrieval-Augmented Generation (RAG) môže byť zároveň technikou promptovania aj nástrojom pri vývoji AI agentov. Pochopenie rozdielu medzi nimi vám pomôže efektívnejšie využiť RAG vo vašich projektoch.

#### RAG ako technika promptovania

**Čo to je?**

- Ako technika promptovania RAG zahŕňa formuláciu špecifických dotazov alebo promptov na usmernenie vyhľadávania relevantných informácií z veľkého korpusu alebo databázy. Tieto informácie sa potom používajú na generovanie odpovedí alebo akcií.

**Ako to funguje:**

1. **Formulácia promptov**: Vytvorte dobre štruktúrované prompt alebo dotazy na základe zadania alebo vstupu používateľa.
2. **Získavanie informácií**: Pomocou prompt vyhľadávajte relevantné údaje z existujúcej databázy poznatkov alebo datasetu.
3. **Generovanie odpovede**: Kombinujte získané informácie s generatívnymi AI modelmi na vytvorenie komplexnej a zrozumiteľnej odpovede.

**Príklad v cestovnej kancelárii**:

- Vstup používateľa: "Chcem navštíviť múzeá v Paríži."
- Prompt: "Nájdite najlepšie múzeá v Paríži."
- Získané informácie: Detaily o múzeu Louvre, Musée d'Orsay atď.
- Generovaná odpoveď: "Tu sú top múzeá v Paríži: múzeum Louvre, Musée d'Orsay a Centre Pompidou."

#### RAG ako nástroj

**Čo to je?**

- Ako nástroj je RAG integrovaný systém, ktorý automatizuje proces vyhľadávania a generovania, čo uľahčuje vývojárom implementovať komplexné AI funkcionality bez nutnosti manuálne vytvárať prompt pre každý dotaz.

**Ako to funguje:**

1. **Integrácia**: Zaintegrovať RAG v rámci architektúry AI agenta, čo mu umožní automaticky spracovávať úlohy vyhľadávania a generovania.
2. **Automatizácia**: Nástroj riadi celý proces od prijatia vstupu používateľa až po generovanie konečnej odpovede bez potreby explicitných promptov pre každý krok.
3. **Efektivita**: Zlepšuje výkon agenta tým, že zjednodušuje proces vyhľadávania a generovania, čo umožňuje rýchlejšie a presnejšie odpovede.

**Príklad v cestovnej kancelárii**:

- Vstup používateľa: "Chcem navštíviť múzeá v Paríži."
- RAG nástroj: Automaticky získa informácie o múzeách a generuje odpoveď.
- Generovaná odpoveď: "Tu sú top múzeá v Paríži: múzeum Louvre, Musée d'Orsay a Centre Pompidou."

### Porovnanie

| Aspekt                  | Technika promptovania                                      | Nástroj                                               |
|-------------------------|-----------------------------------------------------------|-------------------------------------------------------|
| **Manuálne vs Automatické** | Manuálna tvorba promptov pre každý dotaz.                 | Automatizovaný proces vyhľadávania a generovania.      |
| **Kontrola**             | Ponúka väčšiu kontrolu nad procesom vyhľadávania.         | Zjednodušuje a automatizuje vyhľadávanie a generovanie.|
| **Flexibilita**          | Umožňuje prispôsobené prompty podľa špecifických potrieb. | Efektívnejšie pre veľkoskalové implementácie.          |
| **Komplexnosť**          | Vyžaduje tvorbu a ladenie promptov.                        | Jednoduchšie na integráciu v rámci architektúry AI agenta.|

### Praktické príklady

**Príklad techniky promptovania:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Príklad nástroja:**

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

### Hodnotenie relevantnosti

Hodnotenie relevantnosti je kľúčový aspekt výkonnosti AI agenta. Zabezpečuje, že informácie získané a generované agentom sú vhodné, presné a užitočné pre používateľa. Pozrime sa, ako hodnotiť relevantnosť v AI agentoch vrátane praktických príkladov a techník.

#### Kľúčové koncepty hodnotenia relevantnosti

1. **Povedomie o kontexte**:
   - Agent musí rozumieť kontextu používateľovho dotazu, aby získal a generoval relevantné informácie.
   - Príklad: Ak používateľ pýta "najlepšie reštaurácie v Paríži," agent by mal brať do úvahy preferencie používateľa, ako typ kuchyne a rozpočet.

2. **Presnosť**:
   - Informácie poskytované agentom by mali byť fakticky správne a aktuálne.
   - Príklad: Odporúčanie reštaurácií, ktoré sú otvorené a majú dobré recenzie, namiesto zastaralých alebo zatvorených možností.

3. **Úmysel používateľa**:
   - Agent by mal odhadnúť úmysel používateľa za dotazom, aby poskytol najrelevantnejšie informácie.
   - Príklad: Ak používateľ hľadá "lacné hotely," agent by mal uprednostniť cenovo dostupné možnosti.

4. **Spätná väzba**:
   - Neustále zhromažďovanie a analyzovanie spätnej väzby od používateľov pomáha agentovi zlepšovať proces hodnotenia relevantnosti.
   - Príklad: Zahrnutie hodnotení a spätnej väzby na predchádzajúce odporúčania na zlepšenie budúcich odpovedí.

#### Praktické techniky hodnotenia relevantnosti

1. **Scoring relevance**:
   - Priraďte každému získanému prvku skóre relevantnosti na základe toho, ako dobre zodpovedá používateľovmu dotazu a preferenciám.
   - Príklad:

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

2. **Filtrovanie a zoradenie**:
   - Odstráňte nerelevantné položky a zoradte zostávajúce podľa skóre relevantnosti.
   - Príklad:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrátiť top 10 relevantných položiek
     ```

3. **Spracovanie prirodzeného jazyka (NLP)**:
   - Použite NLP techniky na pochopenie dotazu používateľa a získanie relevantných informácií.
   - Príklad:

     ```python
     def process_query(query):
         # Použite NLP na extrahovanie kľúčových informácií z dotazu používateľa
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrácia spätnej väzby používateľa**:
   - Zhromažďujte spätnú väzbu používateľov na poskytnuté odporúčania a využívajte ju na prispôsobenie budúcich hodnotení relevantnosti.
   - Príklad:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Príklad: Hodnotenie relevantnosti v cestovnej kancelárii

Tu je praktický príklad, ako môže cestovná kancelária hodnotiť relevantnosť cestovných odporúčaní:

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
        return ranked_items[:10]  # Vrátiť top 10 relevantných položiek

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

# Príklad použitia
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

### Hľadanie s úmyslom

Hľadanie s úmyslom znamená pochopenie a interpretáciu skrytého cieľa alebo zámeru za používateľovým dotazom s cieľom získať a generovať tie najrelevantnejšie a najpraktickejšie informácie. Tento prístup ide ďalej než len jednoduché vyhľadávanie kľúčových slov a zameriava sa na pochopenie skutočných potrieb a kontextu používateľa.

#### Kľúčové koncepty hľadania s úmyslom

1. **Pochopenie úmyslu používateľa**:
   - Úmysel používateľa možno klasifikovať do troch hlavných typov: informačný, navigačný a transakčný.
     - **Informačný úmysel**: Používateľ hľadá informácie o téme (napr. "Aké sú najlepšie múzeá v Paríži?").
     - **Navigačný úmysel**: Používateľ chce prejsť na konkrétnu webovú stránku alebo stránku (napr. "Oficiálna stránka múzea Louvre").
     - **Transakčný úmysel**: Používateľ chce vykonať transakciu, napríklad rezervovať let alebo uskutočniť nákup (napr. "Rezervovať let do Paríža").

2. **Povedomie o kontexte**:
   - Analýza kontextu dotazu používateľa pomáha presne identifikovať jeho úmysel. Zahŕňa to zohľadnenie predchádzajúcich interakcií, preferencií používateľa a konkrétnych detailov aktuálneho dotazu.

3. **Spracovanie prirodzeného jazyka (NLP)**:
   - NLP techniky sa využívajú na pochopenie a interpretáciu prirodzených jazykových dotazov používateľov. Zahŕňa úlohy ako rozpoznávanie entít, analýzu sentimentu a parsovanie dotazu.

4. **Personalizácia**:
   - Personalizácia výsledkov vyhľadávania na základe histórie, preferencií a spätnej väzby používateľa zvyšuje relevantnosť získaných informácií.

#### Praktický príklad: Hľadanie s úmyslom v cestovnej kancelárii

Pozrime sa na príklad cestovnej kancelárie, ako môže byť hľadanie s úmyslom implementované.

1. **Zhromažďovanie používateľských preferencií**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Pochopenie úmyslu používateľa**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Povedomie o kontexte**


   ```python
   def analyze_context(query, user_history):
       # Skombinujte aktuálny dopyt s históriou používateľa, aby ste porozumeli kontextu
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Vyhľadávanie a personalizácia výsledkov**

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
       # Príklad vyhľadávacej logiky pre informačný zámer
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Príklad vyhľadávacej logiky pre navigačný zámer
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Príklad vyhľadávacej logiky pre transakčný zámer
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Príklad personalizačnej logiky
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Vrátiť top 10 personalizovaných výsledkov
   ```

5. **Príklad použitia**

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

## 4. Generovanie kódu ako nástroj

Agentmi generátora kódu sú modely AI, ktoré píšu a vykonávajú kód na riešenie zložitých problémov a automatizáciu úloh.

### Agent generátora kódu

Agentmi generátora kódu používajú generatívne AI modely na písanie a vykonávanie kódu. Títo agenti môžu riešiť zložité problémy, automatizovať úlohy a poskytovať hodnotné poznatky generovaním a spúšťaním kódu v rôznych programovacích jazykoch.

#### Praktické použitia

1. **Automatizovaná generácia kódu**: Generovanie kódových útržkov pre konkrétne úlohy, napríklad analýzu dát, web scraping alebo strojové učenie.
2. **SQL ako RAG**: Použitie SQL dotazov na získavanie a manipuláciu s dátami z databáz.
3. **Riešenie problémov**: Vytváranie a vykonávanie kódu na riešenie špecifických problémov, napríklad optimalizácia algoritmov alebo analýza dát.

#### Príklad: agent generátora kódu pre analýzu dát

Predstavte si, že navrhujete agenta generátora kódu. Tu je, ako by mohol fungovať:

1. **Úloha**: Analyzovať dátovú množinu na identifikáciu trendov a vzorov.
2. **Kroky**:
   - Načítať dátovú množinu do nástroja na analýzu dát.
   - Generovať SQL dotazy na filtrovanie a agregáciu dát.
   - Vykonať dotazy a získať výsledky.
   - Použiť výsledky na generovanie vizualizácií a poznatkov.
3. **Potrebné zdroje**: Prístup k dátovej množine, nástroje na analýzu dát a SQL schopnosti.
4. **Skúsenosti**: Použiť minulé výsledky analýz na zlepšenie presnosti a relevancie budúcich analýz.

### Príklad: agent generátora kódu pre cestovnú kanceláriu

V tomto príklade navrhneme agenta generátora kódu, Cestovnú kanceláriu, ktorý pomáha užívateľom plánovať ich cestovanie generovaním a vykonávaním kódu. Tento agent dokáže riešiť úlohy, ako je získavanie možností cestovania, filtrovanie výsledkov a zostavovanie itinerára pomocou generatívnej AI.

#### Prehľad agenta generátora kódu

1. **Zbieranie preferencií užívateľa**: Zhromažďuje vstupy užívateľa, ako sú destinácia, dátumy cesty, rozpočet a záujmy.
2. **Generovanie kódu na získavanie dát**: Generuje útržky kódu na získanie informácií o letoch, hoteloch a atrakciách.
3. **Vykonávanie generovaného kódu**: Spúšťa generovaný kód na získanie aktuálnych informácií.
4. **Generovanie itinerára**: Zostavuje získané dáta do personalizovaného cestovného plánu.
5. **Úpravy na základe spätnej väzby**: Prijíma spätnú väzbu od užívateľa a podľa potreby znovu generuje kód na doladenie výsledkov.

#### Implementácia krok za krokom

1. **Zbieranie preferencií užívateľa**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generovanie kódu na získavanie dát**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Príklad: Vygenerujte kód na vyhľadávanie letov podľa používateľských preferencií
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Príklad: Vygenerujte kód na vyhľadávanie hotelov
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Vykonávanie generovaného kódu**

   ```python
   def execute_code(code):
       # Spustite vygenerovaný kód pomocou exec
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

4. **Generovanie itinerára**

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

5. **Úpravy na základe spätnej väzby**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Upravte preferencie na základe spätnej väzby od používateľa
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Znovu vygenerujte a spustite kód s aktualizovanými preferenciami
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Využitie environmentálneho povedomia a uvažovania

Založenie na schéme tabuľky môže skutočne zlepšiť proces generovania dotazov využitím environmentálneho povedomia a uvažovania.

Tu je príklad, ako sa to dá urobiť:

1. **Pochopenie schémy**: Systém pochopí schému tabuľky a použije tieto informácie na zakotvenie generovania dotazov.
2. **Úprava na základe spätnej väzby**: Systém upraví užívateľské preferencie na základe spätnej väzby a uvažuje o tom, ktoré polia v schéme je potrebné aktualizovať.
3. **Generovanie a vykonávanie dotazov**: Systém vygeneruje a vykoná dotazy na získanie aktualizovaných údajov o letoch a hoteloch na základe nových preferencií.

Tu je aktualizovaný príklad kódu v Pythone, ktorý tieto koncepty začleňuje:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Upravte preferencie na základe spätnej väzby používateľa
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Odôvodnenie založené na schéme na úpravu ďalších súvisiacich preferencií
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Vlastná logika na úpravu preferencií na základe schémy a spätnej väzby
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Vygenerujte kód na získanie údajov o letoch na základe aktualizovaných preferencií
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Vygenerujte kód na získanie údajov o hoteloch na základe aktualizovaných preferencií
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulujte vykonanie kódu a vráťte skúšobné údaje
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Vygenerujte itinerár na základe letov, hotelov a atrakcií
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Príklad schémy
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Príklad použitia
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Znovu vygenerujte a vykonajte kód s aktualizovanými preferenciami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Vysvetlenie - rezervácia na základe spätnej väzby

1. **Povedomie o schéme**: Slovník `schema` definuje, ako by sa mali preferencie upravovať na základe spätnej väzby. Obsahuje polia ako `favorites` a `avoid` s príslušnými úpravami.
2. **Úprava preferencií (metóda `adjust_based_on_feedback`)**: Táto metóda upravuje preferencie na základe spätnej väzby užívateľa a schémy.
3. **Úpravy založené na prostredí (metóda `adjust_based_on_environment`)**: Táto metóda prispôsobuje úpravy na základe schémy a spätnej väzby.
4. **Generovanie a vykonávanie dotazov**: Systém generuje kód na získanie aktualizovaných údajov o letoch a hoteloch na základe upravených preferencií a simuluje vykonávanie týchto dotazov.
5. **Generovanie itinerára**: Systém vytvorí aktualizovaný itinerár na základe nových údajov o letoch, hoteloch a atrakciách.

Tým, že je systém vedomý prostredia a uvažuje na základe schémy, môže generovať presnejšie a relevantnejšie dotazy, čo vedie k lepším odporúčaniam pre cestovanie a personalizovanejšiemu užívateľskému zážitku.

### Použitie SQL ako techniky Retrieval-Augmented Generation (RAG)

SQL (Structurovaný dotazovací jazyk) je mocný nástroj na interakciu s databázami. Keď sa používa ako súčasť prístupu Retrieval-Augmented Generation (RAG), SQL dokáže získať relevantné dáta z databáz na informovanie a generovanie odpovedí alebo činností v AI agentoch. Preskúmajme, ako môže byť SQL použité ako technika RAG v kontexte Cestovnej kancelárie.

#### Kľúčové koncepty

1. **Interakcia s databázou**:
   - SQL sa používa na dotazovanie databáz, získavanie relevantných informácií a manipuláciu s dátami.
   - Príklad: Získavanie detailov letov, informácií o hoteloch a atrakciách z cestovnej databázy.

2. **Integrácia s RAG**:
   - SQL dotazy sa generujú na základe vstupu a preferencií užívateľa.
   - Získané údaje sa následne používajú na generovanie personalizovaných odporúčaní alebo činností.

3. **Dynamická generácia dotazov**:
   - AI agent generuje dynamické SQL dotazy na základe kontextu a potrieb užívateľa.
   - Príklad: Prispôsobovanie SQL dotazov na filtrovanie výsledkov podľa rozpočtu, dátumov a záujmov.

#### Použitia

- **Automatizovaná generácia kódu**: Generovanie kódových útržkov pre konkrétne úlohy.
- **SQL ako RAG**: Použitie SQL dotazov na manipuláciu s dátami.
- **Riešenie problémov**: Vytváranie a vykonávanie kódu na riešenie problémov.

**Príklad**:
Agent na analýzu dát:

1. **Úloha**: Analyzovať dátovú množinu na zistenie trendov.
2. **Kroky**:
   - Načítať dátovú množinu.
   - Generovať SQL dotazy na filtrovanie dát.
   - Vykonať dotazy a získať výsledky.
   - Generovať vizualizácie a poznatky.
3. **Zdroje**: Prístup k dátovej množine, schopnosti SQL.
4. **Skúsenosti**: Použiť minulé výsledky na zlepšenie budúcich analýz.

#### Praktický príklad: použitie SQL v Cestovnej kancelárii

1. **Zbieranie preferencií užívateľa**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generovanie SQL dotazov**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Vykonávanie SQL dotazov**

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

4. **Generovanie odporúčaní**

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

#### Príklad SQL dotazov

1. **Dotaz na let**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Dotaz na hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Dotaz na atrakciu**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Využitím SQL ako súčasti techniky Retrieval-Augmented Generation (RAG) môžu AI agenti ako Cestovná kancelária dynamicky získavať a využívať relevantné dáta na poskytovanie presných a personalizovaných odporúčaní.

### Príklad metakognície

Aby sme demonštrovali implementáciu metakognície, vytvorme jednoduchého agenta, ktorý *reflektuje svoj proces rozhodovania* počas riešenia problému. V tomto príklade postavíme systém, kde agent sa snaží optimalizovať výber hotela, no následne vyhodnocuje svoje odôvodnenie a upravuje stratégiu, keď robí chyby alebo neoptimálne výbery.

Tento proces nasimulujeme na jednoduchom príklade, kde agent vyberá hotely na základe kombinácie ceny a kvality, no bude „reflektovať“ svoje rozhodnutia a podľa toho sa upraví.

#### Ako to ilustruje metakogníciu:

1. **Počiatočné rozhodnutie**: Agent vyberie najlacnejší hotel bez pochopenia vplyvu kvality.
2. **Reflexia a vyhodnotenie**: Po prvotnom výbere agent skontroluje, či hotel nebol „zlou“ voľbou pomocou spätnej väzby od užívateľa. Ak zistí, že kvalita hotela bola príliš nízka, reflexne vyhodnotí svoje odôvodnenie.
3. **Úprava stratégie**: Agent upraví stratégiu na základe svojej reflexie a prejde z „najlacnejšieho“ na „najvyššiu kvalitu“, čím vylepší svoj rozhodovací proces pri budúcich iteráciách.

Tu je príklad:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Ukladá predtým vybrané hotely
        self.corrected_choices = []  # Ukladá opravené výbery
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Dostupné stratégie

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
        # Predpokladajme, že máme spätnú väzbu od používateľa, ktorá nám povedz, či posledný výber bol dobrý alebo nie
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Upravte stratégiu, ak bol predchádzajúci výber neuspokojivý
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

# Simulujte zoznam hotelov (cena a kvalita)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Vytvorte agenta
agent = HotelRecommendationAgent()

# Krok 1: Agent odporúča hotel pomocou stratégie „najlacnejší“
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Krok 2: Agent reflektuje na výber a podľa potreby upraví stratégiu
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Krok 3: Agent opäť odporúča, tentoraz s použitím upravenej stratégie
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Schopnosti metakognície agenta

Kľúčové je, že agent dokáže:
- Vyhodnocovať svoje predchádzajúce výbery a proces rozhodovania.
- Upraviť svoju stratégiu na základe tejto reflexie, teda metakogníciu v praxi.

Toto je jednoduchá forma metakognície, kde systém vie upravovať svoj uvažovací proces na základe vnútorných spätných väzieb.

### Záver

Metakognícia je mocný nástroj, ktorý môže výrazne zlepšiť schopnosti AI agentov. Začlenením metakognitívnych procesov môžete navrhnúť agentov, ktorí sú inteligentnejší, prispôsobivejší a efektívnejší. Použite ďalšie zdroje na hlbšie preskúmanie fascinujúceho sveta metakognície v AI agentoch.

### Máte ďalšie otázky ohľadom návrhového vzoru metakognície?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na vaše otázky týkajúce sa AI agentov.

## Predchádzajúca lekcia

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Nasledujúca lekcia

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->