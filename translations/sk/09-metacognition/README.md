<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T20:33:13+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "sk"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.sk.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na obrázok vyššie, aby ste si pozreli video k tejto lekcii)_
# Metakognícia v AI agentoch

## Úvod

Vitajte v lekcii o metakognícii v AI agentoch! Táto kapitola je určená pre začiatočníkov, ktorí sa zaujímajú o to, ako môžu AI agenti premýšľať o svojich vlastných myšlienkových procesoch. Na konci tejto lekcie pochopíte kľúčové koncepty a získate praktické príklady, ako aplikovať metakogníciu pri návrhu AI agentov.

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

1. Pochopiť dôsledky cyklov uvažovania v definíciách agentov.
2. Používať techniky plánovania a hodnotenia na podporu samokorigujúcich agentov.
3. Vytvoriť vlastných agentov schopných manipulovať s kódom na splnenie úloh.

## Úvod do metakognície

Metakognícia sa týka vyšších kognitívnych procesov, ktoré zahŕňajú premýšľanie o vlastnom myslení. Pre AI agentov to znamená schopnosť hodnotiť a upravovať svoje činnosti na základe sebauvedomenia a minulých skúseností. Metakognícia, alebo „myslenie o myslení“, je dôležitý koncept pri vývoji agentických AI systémov. Zahŕňa to, že AI systémy si uvedomujú svoje vlastné vnútorné procesy a dokážu monitorovať, regulovať a prispôsobovať svoje správanie. Podobne ako my, keď „čítame miestnosť“ alebo analyzujeme problém. Toto sebauvedomenie môže pomôcť AI systémom robiť lepšie rozhodnutia, identifikovať chyby a zlepšovať svoj výkon v priebehu času – opäť sa vraciame k Turingovmu testu a debate o tom, či AI prevezme kontrolu.

V kontexte agentických AI systémov môže metakognícia pomôcť riešiť niekoľko výziev, ako napríklad:
- Transparentnosť: Zabezpečenie, že AI systémy dokážu vysvetliť svoje uvažovanie a rozhodnutia.
- Uvažovanie: Zlepšenie schopnosti AI systémov syntetizovať informácie a robiť rozumné rozhodnutia.
- Adaptácia: Umožnenie AI systémom prispôsobiť sa novým prostrediam a meniacim sa podmienkam.
- Vnímanie: Zlepšenie presnosti AI systémov pri rozpoznávaní a interpretácii údajov z ich prostredia.

### Čo je metakognícia?

Metakognícia, alebo „myslenie o myslení“, je vyšší kognitívny proces, ktorý zahŕňa sebauvedomenie a sebareguláciu vlastných kognitívnych procesov. V oblasti AI metakognícia umožňuje agentom hodnotiť a prispôsobovať svoje stratégie a činnosti, čo vedie k zlepšeným schopnostiam riešenia problémov a rozhodovania. Pochopením metakognície môžete navrhovať AI agentov, ktorí sú nielen inteligentnejší, ale aj prispôsobivejší a efektívnejší. Pri skutočnej metakognícii by AI explicitne uvažovala o svojom vlastnom uvažovaní.

Príklad: „Uprednostnil som lacnejšie lety, pretože... Možno mi unikajú priame lety, takže to skontrolujem znova.“
Sledovanie toho, ako alebo prečo si vybral určitú trasu.
- Uvedomenie si, že urobil chyby, pretože sa príliš spoliehal na preferencie používateľa z minula, a preto mení svoju stratégiu rozhodovania, nielen konečné odporúčanie.
- Diagnostikovanie vzorcov, ako napríklad: „Kedykoľvek používateľ spomenie ‚príliš preplnené‘, nemal by som len odstrániť určité atrakcie, ale aj prehodnotiť, či môj spôsob výberu ‚top atrakcií‘ nie je chybný, ak vždy hodnotím podľa popularity.“

### Dôležitosť metakognície v AI agentoch

Metakognícia zohráva kľúčovú úlohu pri návrhu AI agentov z viacerých dôvodov:

![Dôležitosť metakognície](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.sk.png)

- Sebareflexia: Agenti môžu hodnotiť svoj vlastný výkon a identifikovať oblasti na zlepšenie.
- Adaptabilita: Agenti môžu meniť svoje stratégie na základe minulých skúseností a meniacich sa prostredí.
- Korekcia chýb: Agenti môžu autonómne detegovať a opravovať chyby, čo vedie k presnejším výsledkom.
- Riadenie zdrojov: Agenti môžu optimalizovať využívanie zdrojov, ako je čas a výpočtový výkon, plánovaním a hodnotením svojich činností.

## Komponenty AI agenta

Predtým, než sa ponoríme do metakognitívnych procesov, je dôležité pochopiť základné komponenty AI agenta. AI agent sa zvyčajne skladá z:

- Persona: Osobnosť a charakteristiky agenta, ktoré definujú, ako komunikuje s používateľmi.
- Nástroje: Schopnosti a funkcie, ktoré agent dokáže vykonávať.
- Zručnosti: Vedomosti a odborné znalosti, ktoré agent vlastní.

Tieto komponenty spolupracujú na vytvorení „jednotky odbornosti“, ktorá dokáže vykonávať špecifické úlohy.

**Príklad**:
Predstavte si cestovného agenta, ktorý nielen plánuje vašu dovolenku, ale aj upravuje svoju trasu na základe údajov v reálnom čase a minulých skúseností zákazníkov.

### Príklad: Metakognícia v službe cestovného agenta

Predstavte si, že navrhujete službu cestovného agenta poháňanú AI. Tento agent, „Cestovný agent“, pomáha používateľom plánovať ich dovolenky. Na začlenenie metakognície musí Cestovný agent hodnotiť a upravovať svoje činnosti na základe sebauvedomenia a minulých skúseností. Tu je, ako by mohla metakognícia zohrávať úlohu:

#### Aktuálna úloha

Aktuálnou úlohou je pomôcť používateľovi naplánovať výlet do Paríža.

#### Kroky na splnenie úlohy

1. **Zhromaždiť preferencie používateľa**: Opýtať sa používateľa na jeho cestovné dátumy, rozpočet, záujmy (napr. múzeá, kuchyňa, nakupovanie) a akékoľvek špecifické požiadavky.
2. **Získať informácie**: Vyhľadať možnosti letov, ubytovania, atrakcií a reštaurácií, ktoré zodpovedajú preferenciám používateľa.
3. **Vytvoriť odporúčania**: Poskytnúť personalizovaný itinerár s podrobnosťami o letoch, rezerváciách hotelov a navrhovaných aktivitách.
4. **Upraviť na základe spätnej väzby**: Požiadať používateľa o spätnú väzbu na odporúčania a vykonať potrebné úpravy.

#### Požadované zdroje

- Prístup k databázam rezervácií letov a hotelov.
- Informácie o parížskych atrakciách a reštauráciách.
- Údaje o spätnej väzbe od používateľov z predchádzajúcich interakcií.

#### Skúsenosti a sebareflexia

Cestovný agent využíva metakogníciu na hodnotenie svojho výkonu a učenie sa z minulých skúseností. Napríklad:

1. **Analýza spätnej väzby používateľa**: Cestovný agent preskúma spätnú väzbu používateľa, aby zistil, ktoré odporúčania boli dobre prijaté a ktoré nie. Podľa toho upraví svoje budúce návrhy.
2. **Adaptabilita**: Ak používateľ predtým spomenul, že nemá rád preplnené miesta, Cestovný agent sa v budúcnosti vyhne odporúčaniu populárnych turistických miest počas špičkových hodín.
3. **Korekcia chýb**: Ak Cestovný agent urobil chybu v minulom plánovaní, napríklad navrhol hotel, ktorý bol plne obsadený, naučí sa dôkladnejšie kontrolovať dostupnosť predtým, než urobí odporúčania.

#### Praktický príklad pre vývojárov

Tu je zjednodušený príklad kódu, ako by mohol vyzerať kód Cestovného agenta pri začlenení metakognície:

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

#### Prečo je metakognícia dôležitá

- **Sebareflexia**: Agenti môžu analyzovať svoj výkon a identifikovať oblasti na zlepšenie.
- **Adaptabilita**: Agenti môžu meniť stratégie na základe spätnej väzby a meniacich sa podmienok.
- **Korekcia chýb**: Agenti môžu autonómne detegovať a opravovať chyby.
- **Riadenie zdrojov**: Agenti môžu optimalizovať využívanie zdrojov, ako je čas a výpočtový výkon.

Začlenením metakognície môže Cestovný agent poskytovať personalizovanejšie a presnejšie odporúčania na cestovanie, čím zlepší celkový používateľský zážitok.

---

## 2. Plánovanie v agentoch

Plánovanie je kľúčovou súčasťou správania AI agenta. Zahŕňa načrtnutie krokov potrebných na dosiahnutie cieľa, pričom sa zohľadňuje aktuálny stav, zdroje a možné prekážky.

### Prvky plánovania

- **Aktuálna úloha**: Jasne definovať úlohu.
- **Kroky na splnenie úlohy**: Rozdeliť úlohu na zvládnuteľné kroky.
- **Požadované zdroje**: Identifikovať potrebné zdroje.
- **Skúsenosti**: Využiť minulé skúsenosti na informovanie plánovania.

**Príklad**:
Tu sú kroky, ktoré musí Cestovný agent podniknúť, aby efektívne pomohol používateľovi naplánovať jeho cestu:

### Kroky pre Cestovného agenta

1. **Zhromaždiť preferencie používateľa**
   - Opýtať sa používateľa na podrobnosti o jeho cestovných dátumoch, rozpočte, záujmoch a akýchkoľvek špecifických požiadavkách.
   - Príklady: „Kedy plánujete cestovať?“ „Aký je váš rozpočtový rozsah?“ „Aké aktivity si užívate na dovolenke?“

2. **Získať informácie**
   - Vyhľadať relevantné možnosti cestovania na základe preferencií používateľa.
   - **Lety**: Vyhľadať dostupné lety v rámci rozpočtu a preferovaných dátumov používateľa.
   - **Ubytovanie**: Nájsť hotely alebo prenájmy, ktoré zodpovedajú preferenciám používateľa pre lokalitu, cenu a vybavenie.
   - **Atrakcie a reštaurácie**: Identifikovať populárne atrakcie, aktivity a možnosti stravovania, ktoré zodpovedajú záujmom používateľa.

3. **Vytvoriť odporúčania**
   - Zostaviť získané informácie do personalizovaného itinerára.
   - Poskytnúť podrobnosti, ako sú možnosti letov, rezervácie hotelov a navrhované aktivity, pričom odporúčania prispôsobiť preferenciám používateľa.

4. **Predstaviť itinerár používateľovi**
   - Zdieľať navrhovaný itinerár s používateľom na jeho preskúmanie.
   - Príklad: „Tu je navrhovaný itinerár pre váš výlet do Paríža. Zahŕňa podrobnosti o letoch, rezerváciách hotelov a zoznam odporúčaných aktivít a reštaurácií. Dajte mi vedieť, čo si o tom myslíte!“

5. **Zhromaždiť spätnú väzbu**
   - Požiadať používateľa o spätnú väzbu na navrhovaný itinerár.
   - Príklady: „Páčia sa vám možnosti letov?“ „Je hotel vhodný pre vaše potreby?“ „Sú nejaké aktivity, ktoré by ste chceli pridať alebo odstrániť?“

6. **Upraviť na základe spätnej väzby**
   - Upraviť itinerár na základe spätnej väzby používateľa.
   - Urobiť potrebné zmeny v odporúčaniach na lety, ubytovanie a aktivity, aby lepšie zodpovedali preferenciám používateľa.

7. **Konečné potvrdenie**
   - Predstaviť aktualizovaný itinerár používateľovi na konečné potvrdenie.
   - Príklad: „Urobil som úpravy na základe vašej spätnej väzby. Tu je aktualizovaný itinerár. Vyzerá všetko v poriadku?“

8. **Rezervovať a potvrdiť rezervácie**
   - Po schválení itinerára používateľom pokračovať v rezervácii letov, ubytovania a akýchkoľvek predplánovaných aktivít.
   - Poslať používateľovi podrobnosti o potvrdení.

9. **Poskytnúť priebežnú podporu**
   - Zostať k dispozícii na pomoc používateľovi s akýmikoľvek zmenami alebo dodatočnými požiadavkami pred a počas jeho cesty.
   - Príklad: „Ak budete počas svojej cesty potrebovať ďalšiu pomoc, neváhajte ma kedykoľvek kontaktovať!“

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

## 3. Korekčný RAG systém

Najprv začnime pochopením rozdielu medzi nástrojom RAG a prediktívnym načítaním kontextu.

![RAG vs načítanie kontextu](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.sk.png)

### Retrieval-Augmented Generation (RAG)

RAG kombinuje systém vyhľadávania s generatívnym modelom. Keď sa zadá dopyt, systém vyhľadávania načíta relevantné dokumenty alebo údaje z externého zdroja a tieto získané informácie sa použijú na doplnenie vstupu do generatívneho modelu. To pomáha modelu generovať presnejšie a kontextovo relevantné odpovede.

V systéme RAG agent načíta relevantné informácie z databázy znalostí a použije ich na generovanie vhodných odpovedí alebo činností.

### Korekčný prístup RAG

Korekčný prístup RAG sa zameriava na použitie techník RAG na opravu chýb a zlepšenie presnosti AI agentov. To zahŕňa:

1. **Technika podnetov**: Použitie špecifických podnetov na usmernenie agenta pri načítavaní relevantných informácií.
2. **Nástroj**: Implementácia algoritmov a mechanizmov, ktoré umožňujú agentovi hodnotiť relevantnosť načítaných informácií a generovať presné odpovede.
3. **Hodnotenie**: Neustále hodnotenie výkonu agenta a vykonávanie úprav na zlepšenie jeho presnosti a efektívnosti.

#### Príklad: Korekčný RAG v agentovi vyhľadávania

Zvážte agenta vyhľadávania, ktorý načítava informácie z webu na zodpovedanie otázok používateľov. Korekčný prístup RAG môže zahŕňať:

1. **Technika podnetov**: Formulovanie vyhľadávacích dopytov na základe vstupu používateľa.
2. **Nástroj**: Použitie algoritmov spracovania prirodzeného jazyka a strojového učenia na hodnotenie a filtrovanie výsledkov vyhľadávania.
3. **Hodnotenie**: Analýza spätnej väzby používateľa na identifikáciu a opravu nepresností v načítaných informáciách.

### Korekčný RAG v Cestovnom agentovi

Korekčný RAG (Retrieval-Augmented Generation) zlepšuje schopnosť AI načítavať a generovať informácie pri opravovaní akýchkoľvek nepresností. Pozrime sa, ako môže Cestovný agent využiť korekčný prístup RAG na poskytovanie presnejších a relevantnejších odporúčaní na cestovanie.

To zahŕňa:

- **Technika podnetov:** Použitie špecifických podnetov na usmernen
### Predbežné načítanie kontextu

Predbežné načítanie kontextu zahŕňa načítanie relevantných informácií alebo pozadia do modelu ešte pred spracovaním dotazu. To znamená, že model má od začiatku prístup k týmto informáciám, čo mu umožňuje generovať informovanejšie odpovede bez potreby získavania ďalších údajov počas procesu.

Tu je zjednodušený príklad, ako by mohlo vyzerať predbežné načítanie kontextu pre aplikáciu cestovnej agentúry v Pythone:

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

#### Vysvetlenie

1. **Inicializácia (`__init__` metóda)**: Trieda `TravelAgent` predbežne načíta slovník obsahujúci informácie o populárnych destináciách, ako sú Paríž, Tokio, New York a Sydney. Tento slovník zahŕňa detaily ako krajina, mena, jazyk a hlavné atrakcie pre každú destináciu.

2. **Získavanie informácií (`get_destination_info` metóda)**: Keď sa používateľ pýta na konkrétnu destináciu, metóda `get_destination_info` vyhľadá relevantné informácie z predbežne načítaného slovníka.

Predbežným načítaním kontextu môže aplikácia cestovnej agentúry rýchlo reagovať na dotazy používateľov bez potreby získavania týchto informácií z externého zdroja v reálnom čase. To robí aplikáciu efektívnejšou a pohotovejšou.

### Bootstrapovanie plánu s cieľom pred iteráciou

Bootstrapovanie plánu s cieľom zahŕňa začatie s jasne definovaným cieľom alebo požadovaným výsledkom. Definovaním tohto cieľa na začiatku môže model použiť tento cieľ ako vodítko počas celého iteratívneho procesu. To pomáha zabezpečiť, že každá iterácia sa približuje k dosiahnutiu požadovaného výsledku, čím sa proces stáva efektívnejším a zameranejším.

Tu je príklad, ako by ste mohli bootstrapovať cestovný plán s cieľom pred iteráciou pre cestovnú agentúru v Pythone:

### Scenár

Cestovná agentúra chce naplánovať prispôsobenú dovolenku pre klienta. Cieľom je vytvoriť cestovný itinerár, ktorý maximalizuje spokojnosť klienta na základe jeho preferencií a rozpočtu.

### Kroky

1. Definujte preferencie a rozpočet klienta.
2. Bootstrapujte počiatočný plán na základe týchto preferencií.
3. Iterujte, aby ste plán zdokonalili a optimalizovali spokojnosť klienta.

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

#### Vysvetlenie kódu

1. **Inicializácia (`__init__` metóda)**: Trieda `TravelAgent` je inicializovaná zoznamom potenciálnych destinácií, z ktorých každá má atribúty ako názov, cena a typ aktivity.

2. **Bootstrapovanie plánu (`bootstrap_plan` metóda)**: Táto metóda vytvára počiatočný cestovný plán na základe preferencií klienta a rozpočtu. Iteruje cez zoznam destinácií a pridáva ich do plánu, ak zodpovedajú preferenciám klienta a zmestia sa do rozpočtu.

3. **Porovnávanie preferencií (`match_preferences` metóda)**: Táto metóda kontroluje, či destinácia zodpovedá preferenciám klienta.

4. **Iterovanie plánu (`iterate_plan` metóda)**: Táto metóda zdokonaľuje počiatočný plán tým, že sa snaží nahradiť každú destináciu v pláne lepšou alternatívou, pričom zohľadňuje preferencie klienta a rozpočtové obmedzenia.

5. **Výpočet nákladov (`calculate_cost` metóda)**: Táto metóda vypočíta celkové náklady aktuálneho plánu vrátane potenciálnej novej destinácie.

#### Príklad použitia

- **Počiatočný plán**: Cestovná agentúra vytvorí počiatočný plán na základe preferencií klienta pre prehliadky a rozpočet 2000 dolárov.
- **Zdokonalený plán**: Cestovná agentúra iteruje plán, optimalizuje ho podľa preferencií klienta a rozpočtu.

Bootstrapovaním plánu s jasným cieľom (napr. maximalizácia spokojnosti klienta) a iterovaním na jeho zdokonalenie môže cestovná agentúra vytvoriť prispôsobený a optimalizovaný cestovný itinerár pre klienta. Tento prístup zabezpečuje, že cestovný plán od začiatku zodpovedá preferenciám a rozpočtu klienta a zlepšuje sa s každou iteráciou.

### Využitie LLM na prehodnocovanie a skórovanie

Veľké jazykové modely (LLM) môžu byť použité na prehodnocovanie a skórovanie hodnotením relevantnosti a kvality získaných dokumentov alebo generovaných odpovedí. Tu je, ako to funguje:

**Získavanie informácií:** Počiatočný krok získavania informácií vyhľadá súbor kandidátskych dokumentov alebo odpovedí na základe dotazu.

**Prehodnocovanie:** LLM hodnotí týchto kandidátov a prehodnocuje ich na základe ich relevantnosti a kvality. Tento krok zabezpečuje, že najrelevantnejšie a najkvalitnejšie informácie sú prezentované ako prvé.

**Skórovanie:** LLM priraďuje skóre každému kandidátovi, ktoré odráža ich relevantnosť a kvalitu. To pomáha pri výbere najlepšej odpovede alebo dokumentu pre používateľa.

Využitím LLM na prehodnocovanie a skórovanie môže systém poskytovať presnejšie a kontextovo relevantné informácie, čím zlepšuje celkový používateľský zážitok.

Tu je príklad, ako by cestovná agentúra mohla použiť veľký jazykový model (LLM) na prehodnocovanie a skórovanie cestovných destinácií na základe preferencií používateľa v Pythone:

#### Scenár - Cestovanie podľa preferencií

Cestovná agentúra chce odporučiť najlepšie cestovné destinácie klientovi na základe jeho preferencií. LLM pomôže prehodnotiť a skórovať destinácie, aby zabezpečil, že najrelevantnejšie možnosti budú prezentované.

#### Kroky:

1. Získajte preferencie používateľa.
2. Získajte zoznam potenciálnych cestovných destinácií.
3. Použite LLM na prehodnocovanie a skórovanie destinácií na základe preferencií používateľa.

Tu je, ako môžete aktualizovať predchádzajúci príklad na použitie Azure OpenAI Services:

#### Požiadavky

1. Potrebujete mať predplatné Azure.
2. Vytvorte zdroj Azure OpenAI a získajte svoj API kľúč.

#### Príklad Python kódu

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

#### Vysvetlenie kódu - Preference Booker

1. **Inicializácia**: Trieda `TravelAgent` je inicializovaná zoznamom potenciálnych cestovných destinácií, z ktorých každá má atribúty ako názov a popis.

2. **Získavanie odporúčaní (`get_recommendations` metóda)**: Táto metóda generuje prompt pre službu Azure OpenAI na základe preferencií používateľa a vykoná HTTP POST požiadavku na API Azure OpenAI, aby získala prehodnotené a skórované destinácie.

3. **Generovanie promptu (`generate_prompt` metóda)**: Táto metóda konštruuje prompt pre Azure OpenAI, vrátane preferencií používateľa a zoznamu destinácií. Prompt usmerňuje model, aby prehodnotil a skóroval destinácie na základe poskytnutých preferencií.

4. **API volanie**: Knižnica `requests` sa používa na vykonanie HTTP POST požiadavky na API endpoint Azure OpenAI. Odpoveď obsahuje prehodnotené a skórované destinácie.

5. **Príklad použitia**: Cestovná agentúra zhromažďuje preferencie používateľa (napr. záujem o prehliadky a rozmanitú kultúru) a používa službu Azure OpenAI na získanie prehodnotených a skórovaných odporúčaní pre cestovné destinácie.

Uistite sa, že nahradíte `your_azure_openai_api_key` svojím skutočným API kľúčom Azure OpenAI a `https://your-endpoint.com/...` skutočnou URL endpointu vášho nasadenia Azure OpenAI.

Využitím LLM na prehodnocovanie a skórovanie môže cestovná agentúra poskytovať personalizovanejšie a relevantnejšie cestovné odporúčania klientom, čím zlepšuje ich celkový zážitok.
#### Praktický príklad: Vyhľadávanie s úmyslom v cestovnej agentúre

Pozrime sa na príklad cestovnej agentúry, aby sme videli, ako môže byť implementované vyhľadávanie s úmyslom.

1. **Zhromažďovanie preferencií používateľa**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Porozumenie úmyslu používateľa**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Vedomie kontextu**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
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

Agenti na generovanie kódu využívajú AI modely na písanie a vykonávanie kódu, riešenie zložitých problémov a automatizáciu úloh.

### Agenti na generovanie kódu

Agenti na generovanie kódu využívajú generatívne AI modely na písanie a vykonávanie kódu. Títo agenti dokážu riešiť zložité problémy, automatizovať úlohy a poskytovať cenné poznatky generovaním a spúšťaním kódu v rôznych programovacích jazykoch.

#### Praktické aplikácie

1. **Automatizované generovanie kódu**: Generovanie úryvkov kódu pre konkrétne úlohy, ako je analýza dát, web scraping alebo strojové učenie.
2. **SQL ako RAG**: Použitie SQL dotazov na získavanie a manipuláciu s dátami z databáz.
3. **Riešenie problémov**: Tvorba a vykonávanie kódu na riešenie konkrétnych problémov, ako je optimalizácia algoritmov alebo analýza dát.

#### Príklad: Agent na generovanie kódu pre analýzu dát

Predstavte si, že navrhujete agenta na generovanie kódu. Takto by to mohlo fungovať:

1. **Úloha**: Analyzovať dataset na identifikáciu trendov a vzorcov.
2. **Kroky**:
   - Načítať dataset do nástroja na analýzu dát.
   - Generovať SQL dotazy na filtrovanie a agregáciu dát.
   - Spustiť dotazy a získať výsledky.
   - Použiť výsledky na vytvorenie vizualizácií a poznatkov.
3. **Požadované zdroje**: Prístup k datasetu, nástroje na analýzu dát a SQL schopnosti.
4. **Skúsenosti**: Použitie minulých výsledkov analýz na zlepšenie presnosti a relevantnosti budúcich analýz.

### Príklad: Agent na generovanie kódu pre cestovnú agentúru

V tomto príklade navrhneme agenta na generovanie kódu, Travel Agent, ktorý pomáha používateľom plánovať cestovanie generovaním a vykonávaním kódu. Tento agent dokáže zvládnuť úlohy, ako je získavanie cestovných možností, filtrovanie výsledkov a zostavovanie itinerára pomocou generatívnej AI.

#### Prehľad agenta na generovanie kódu

1. **Zhromažďovanie preferencií používateľa**: Zbiera vstupy používateľa, ako sú destinácia, dátumy cestovania, rozpočet a záujmy.
2. **Generovanie kódu na získavanie dát**: Generuje úryvky kódu na získavanie dát o letoch, hoteloch a atrakciách.
3. **Vykonávanie generovaného kódu**: Spúšťa generovaný kód na získanie aktuálnych informácií.
4. **Generovanie itinerára**: Zostavuje získané dáta do personalizovaného cestovného plánu.
5. **Úprava na základe spätnej väzby**: Prijíma spätnú väzbu od používateľa a regeneruje kód, ak je to potrebné, na spresnenie výsledkov.

#### Implementácia krok za krokom

1. **Zhromažďovanie preferencií používateľa**

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

3. **Vykonávanie generovaného kódu**

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

5. **Úprava na základe spätnej väzby**

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

### Využitie environmentálneho povedomia a uvažovania

Na základe schémy tabuľky je možné zlepšiť proces generovania dotazov využitím environmentálneho povedomia a uvažovania.

Tu je príklad, ako to môže byť realizované:

1. **Porozumenie schéme**: Systém porozumie schéme tabuľky a použije tieto informácie na ukotvenie generovania dotazov.
2. **Úprava na základe spätnej väzby**: Systém upraví preferencie používateľa na základe spätnej väzby a uvažuje o tom, ktoré polia v schéme je potrebné aktualizovať.
3. **Generovanie a vykonávanie dotazov**: Systém generuje a vykonáva dotazy na získanie aktualizovaných dát o letoch a hoteloch na základe nových preferencií.

Tu je aktualizovaný príklad Python kódu, ktorý zahŕňa tieto koncepty:

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

#### Vysvetlenie - Rezervácia na základe spätnej väzby

1. **Povedomie o schéme**: Slovník `schema` definuje, ako by sa mali preferencie upravovať na základe spätnej väzby. Zahŕňa polia ako `favorites` a `avoid` s príslušnými úpravami.
2. **Úprava preferencií (metóda `adjust_based_on_feedback`)**: Táto metóda upravuje preferencie na základe spätnej väzby používateľa a schémy.
3. **Úpravy na základe prostredia (metóda `adjust_based_on_environment`)**: Táto metóda prispôsobuje úpravy na základe schémy a spätnej väzby.
4. **Generovanie a vykonávanie dotazov**: Systém generuje kód na získanie aktualizovaných dát o letoch a hoteloch na základe upravených preferencií a simuluje vykonávanie týchto dotazov.
5. **Generovanie itinerára**: Systém vytvára aktualizovaný itinerár na základe nových dát o letoch, hoteloch a atrakciách.

Vďaka tomu, že je systém environmentálne uvedomelý a uvažuje na základe schémy, dokáže generovať presnejšie a relevantnejšie dotazy, čo vedie k lepším cestovným odporúčaniam a personalizovanejšiemu zážitku používateľa.

### Použitie SQL ako Retrieval-Augmented Generation (RAG) techniky

SQL (Structured Query Language) je výkonný nástroj na interakciu s databázami. Keď sa používa ako súčasť prístupu Retrieval-Augmented Generation (RAG), SQL dokáže získať relevantné dáta z databáz na informovanie a generovanie odpovedí alebo akcií v AI agentoch. Pozrime sa, ako môže byť SQL použité ako RAG technika v kontexte cestovnej agentúry.

#### Kľúčové koncepty

1. **Interakcia s databázou**:
   - SQL sa používa na dotazovanie databáz, získavanie relevantných informácií a manipuláciu s dátami.
   - Príklad: Získavanie detailov o letoch, informácií o hoteloch a atrakciách z cestovnej databázy.

2. **Integrácia s RAG**:
   - SQL dotazy sú generované na základe vstupov a preferencií používateľa.
   - Získané dáta sa potom používajú na generovanie personalizovaných odporúčaní alebo akcií.

3. **Dynamické generovanie dotazov**:
   - AI agent generuje dynamické SQL dotazy na základe kontextu a potrieb používateľa.
   - Príklad: Prispôsobenie SQL dotazov na filtrovanie výsledkov podľa rozpočtu, dátumov a záujmov.

#### Aplikácie

- **Automatizované generovanie kódu**: Generovanie úryvkov kódu pre konkrétne úlohy.
- **SQL ako RAG**: Použitie SQL dotazov na manipuláciu s dátami.
- **Riešenie problémov**: Tvorba a vykonávanie kódu na riešenie problémov.

**Príklad**:
Agent na analýzu dát:

1. **Úloha**: Analyzovať dataset na nájdenie trendov.
2. **Kroky**:
   - Načítať dataset.
   - Generovať SQL dotazy na filtrovanie dát.
   - Spustiť dotazy a získať výsledky.
   - Generovať vizualizácie a poznatky.
3. **Zdroje**: Prístup k datasetu, SQL schopnosti.
4. **Skúsenosti**: Použitie minulých výsledkov na zlepšenie budúcich analýz.

#### Praktický príklad: Použitie SQL v cestovnej agentúre

1. **Zhromažďovanie preferencií používateľa**

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

#### Príklady SQL dotazov

1. **Dotaz na lety**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Dotaz na hotely**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Dotaz na atrakcie**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Využitím SQL ako súčasti Retrieval-Augmented Generation (RAG) techniky môžu AI agenti, ako je Travel Agent, dynamicky získavať a využívať relevantné dáta na poskytovanie presných a personalizovaných odporúčaní.

### Príklad metakognície

Na demonštráciu implementácie metakognície vytvorme jednoduchého agenta, ktorý *reflektuje svoj proces rozhodovania* pri riešení problému. V tomto príklade vytvoríme systém, kde agent optimalizuje výber hotela, ale následne hodnotí svoje vlastné rozhodovanie a upravuje svoju stratégiu, keď urobí chyby alebo suboptimálne rozhodnutia.

#### Ako to ilustruje metakogníciu:

1. **Počiatočné rozhodnutie**: Agent vyberie najlacnejší hotel bez ohľadu na kvalitu.
2. **Reflexia a hodnotenie**: Po počiatočnom výbere agent skontroluje, či bol hotel "zlou" voľbou na základe spätnej väzby používateľa. Ak zistí, že kvalita hotela bola príliš nízka, reflektuje svoje rozhodovanie.
3. **Úprava stratégie**: Agent upraví svoju stratégiu na základe reflexie a prejde z "najlacnejšieho" na "najkvalitnejší", čím zlepší svoj proces rozhodovania v budúcich iteráciách.

Tu je príklad:

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

#### Metakognitívne schopnosti agenta

Kľúčom je schopnosť agenta:
- Vyhodnotiť svoje predchádzajúce rozhodnutia a proces rozhodovania.
- Upraviť svoju stratégiu na základe tejto reflexie, teda metakognícia v praxi.

Toto je jednoduchá forma metakognície, kde je systém schopný upraviť svoj proces uvažovania na základe internej spätnej väzby.

### Záver

Metakognícia je mocný nástroj, ktorý môže výrazne zlepšiť schopnosti AI agentov. Vďaka začleneniu metakognitívnych procesov môžete navrhnúť agentov, ktorí sú inteligentnejší, prispôsobivejší a efektívnejší. Využite ďalšie zdroje na hlbšie preskúmanie fascinujúceho sveta metakognície v AI agentoch.

### Máte ďalšie otázky o dizajnovom vzore metakognície?

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Nasledujúca lekcia

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.