[![Multiagentný dizajn](../../../translated_images/sk/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_
# Metakognícia v AI agentoch

## Úvod

Vitajte v lekcii o metakognícii v AI agentoch! Táto kapitola je určená pre začiatočníkov, ktorí sa zaujímajú o to, ako môžu AI agenti premýšľať o svojich vlastných procesoch myslenia. Na konci tejto lekcie pochopíte kľúčové pojmy a budete vybavení praktickými príkladmi na uplatnenie metakognície v dizajne AI agentov.

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

1. Pochopiť dôsledky slučiek rozprávania v definíciách agentov.
2. Používať plánovacie a hodnotiace techniky na pomoc samokorigujúcim agentom.
3. Vytvoriť si vlastných agentov schopných manipulovať s kódom na dosiahnutie úloh.

## Úvod do metakognície

Metakognícia označuje vyššie kognitívne procesy, ktoré zahŕňajú myslenie o vlastnom myslení. Pre AI agentov to znamená schopnosť hodnotiť a upravovať svoje akcie na základe sebavedomia a minulých skúseností. Metakognícia, alebo "myslenie o myslení," je dôležitý koncept vo vývoji agentných AI systémov. Zahŕňa, že AI systémy sú si vedomé svojich vnútorných procesov a dokážu monitorovať, regulovať a prispôsobovať svoje správanie podľa toho. Podobne ako my, keď čítame miestnosť alebo sa pozeráme na problém. Toto sebauvedomenie môže pomôcť AI systémom robiť lepšie rozhodnutia, identifikovať chyby a časom zlepšovať svoj výkon – znova to súvisí s Turingovým testom a debatou o tom, či AI prevezme nadvládu.

V kontexte agentných AI systémov môže metakognícia pomôcť riešiť niekoľko výziev, ako napríklad:
- Transparentnosť: Zaistenie toho, že AI systémy dokážu vysvetliť svoje rozprávanie a rozhodnutia.
- Uvažovanie: Zvýšenie schopnosti AI systémov syntetizovať informácie a robiť rozumné rozhodnutia.
- Adaptácia: Umožniť AI systémom prispôsobiť sa novým prostrediam a meniacim podmienkam.
- Vnímanie: Zlepšenie presnosti AI systémov pri rozpoznávaní a interpretácii dát zo svojho prostredia.

### Čo je metakognícia?

Metakognícia, alebo "myslenie o myslení," je vyšší kognitívny proces, ktorý zahŕňa sebavedomie a sebareguláciu vlastných kognitívnych procesov. V oblasti AI umožňuje metakognícia agentom hodnotiť a prispôsobovať svoje stratégie a činnosti, čo vedie k zlepšeniu riešenia problémov a schopnosti rozhodovania. Pochopením metakognície môžete navrhnúť AI agentov, ktorí sú nielen inteligentnejší, ale aj viac prispôsobiví a efektívni. V skutočnej metakognícii by ste videli, že AI explicitne uvažuje o svojom vlastnom uvažovaní.

Príklad: „Uprednostnil som lacnejšie lety, pretože... Mohol by som však prehliadať priame lety, preto si to znova overím.“
Sledovanie, ako alebo prečo si vybral určitú trasu.
- Uvedomenie si, že spravil chyby, pretože príliš dôveroval preferenciám používateľa z posledného razu, takže modifikuje svoju stratégiu rozhodovania, nie len finálne odporúčanie.
- Diagnostikovanie vzorcov ako: „Kedykoľvek používateľ spomenie ‚príliš preplnené,‘ nemal by som len odstrániť určité atrakcie, ale tiež zvážiť, že moja metóda výberu ‚najlepších atrakcií‘ je chybná, ak vždy radím podľa popularity.“

### Význam metakognície v AI agentoch

Metakognícia zohráva kľúčovú úlohu v dizajne AI agentov z niekoľkých dôvodov:

![Význam metakognície](../../../translated_images/sk/importance-of-metacognition.b381afe9aae352f7.webp)

- Sebareflexia: Agenti môžu zhodnotiť svoj vlastný výkon a identifikovať oblasti na zlepšenie.
- Prispôsobivosť: Agenti môžu meniť svoje stratégie na základe minulých skúseností a meniacich sa prostredí.
- Oprava chýb: Agenti môžu samostatne odhaliť a opraviť chyby, čo vedie k presnejším výsledkom.
- Správa zdrojov: Agenti môžu optimalizovať využívanie zdrojov, ako čas a výpočtový výkon, plánovaním a hodnotením svojich akcií.

## Komponenty AI agenta

Predtým, než sa pustíme do metakognitívnych procesov, je dôležité pochopiť základné komponenty AI agenta. AI agent zvyčajne pozostáva z:

- Persona: Osobnosť a charakteristiky agenta, ktoré definujú, ako komunikuje s používateľmi.
- Nástroje: Schopnosti a funkcie, ktoré agent dokáže vykonávať.
- Zručnosti: Vedomosti a expertíza, ktoré agent vlastní.

Tieto komponenty spolupracujú na vytvorení „jednotky odbornosti,“ ktorá vie vykonávať konkrétne úlohy.

**Príklad**:
Predstavte si cestovného agenta, ktorý nielen plánuje vašu dovolenku, ale aj upravuje svoju cestu na základe údajov v reálnom čase a minulých skúseností zákazníkov.

### Príklad: Metakognícia v cestovnej agentúre

Predstavte si, že navrhujete službu cestovného agenta poháňanú AI. Tento agent, „Cestovný agent,“ pomáha používateľom plánovať ich dovolenky. Na začlenenie metakognície potrebuje Cestovný agent hodnotiť a upravovať svoje akcie na základe sebavedomia a minulých skúseností. Tu je, ako by metakognícia mohla hrať úlohu:

#### Aktuálna úloha

Aktuálnou úlohou je pomôcť používateľovi naplánovať cestu do Paríža.

#### Kroky na dokončenie úlohy

1. **Získať používateľské preferencie**: Spýtať sa používateľa na termíny cesty, rozpočet, záujmy (napr. múzeá, kuchyňa, nakupovanie) a akékoľvek špecifické požiadavky.
2. **Získať informácie**: Vyhľadať možnosti letov, ubytovania, atrakcií a reštaurácií, ktoré zodpovedajú preferenciám používateľa.
3. **Vytvoriť odporúčania**: Poskytnúť personalizovaný itinerár s detailmi o letoch, rezerváciách hotelov a navrhovaných aktivitách.
4. **Upraviť na základe spätnej väzby**: Požiadať používateľa o spätnú väzbu k odporúčaniam a vykonať potrebné úpravy.

#### Potrebné zdroje

- Prístup do databáz letov a hotelových rezervácií.
- Informácie o parížskych atrakciách a reštauráciách.
- Dáta spätnej väzby používateľov z predchádzajúcich interakcií.

#### Skúsenosť a sebareflexia

Cestovný agent používa metakogníciu na hodnotenie svojho výkonu a učenie sa z minulých skúseností. Napríklad:

1. **Analýza spätnej väzby používateľa**: Cestovný agent prezerá spätnú väzbu používateľa, aby zistil, ktoré odporúčania boli prijaté pozitívne a ktoré nie. Podľa toho upravuje svoje budúce návrhy.
2. **Prispôsobivosť**: Ak používateľ predtým uviedol, že nemá rád preplnené miesta, Cestovný agent v budúcnosti neodporučí populárne turistické lokality počas rušných hodín.
3. **Oprava chýb**: Ak Cestovný agent spravil chybu v minulej rezervácii, napríklad navrhol hotel, ktorý bol plne obsadený, naučí sa overovať dostupnosť dôkladnejšie pred podaním odporúčania.

#### Praktický príklad pre vývojára

Tu je zjednodušený príklad kódu Cestovného agenta, ktorý začleňuje metakogníciu:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Vyhľadávanie letov, hotelov a atrakcií podľa preferencií
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
        # Analyzovať spätnú väzbu a prispôsobiť budúce odporúčania
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
- **Prispôsobivosť**: Agenti môžu meniť stratégie na základe spätnej väzby a meniacich sa podmienok.
- **Oprava chýb**: Agenti môžu autonómne odhaľovať a opravovať chyby.
- **Správa zdrojov**: Agenti môžu optimalizovať využívanie zdrojov, ako čas a výpočtový výkon.

Začlenením metakognície môže Cestovný agent poskytovať personalizovanejšie a presnejšie odporúčania na cestovanie, čím sa zlepší celkový zážitok používateľa.

---

## 2. Plánovanie v agentoch

Plánovanie je kľúčovou súčasťou správania AI agenta. Zahŕňa načrtnutie krokov potrebných na dosiahnutie cieľa, pričom zohľadňuje aktuálny stav, zdroje a možné prekážky.

### Prvky plánovania

- **Aktuálna úloha**: Jasne definovať úlohu.
- **Kroky na dokončenie úlohy**: Rozložiť úlohu na zvládnuteľné kroky.
- **Potrebné zdroje**: Identifikovať potrebné zdroje.
- **Skúsenosť**: Využiť minulé skúsenosti na informovanie plánovania.

**Príklad**:
Tu sú kroky, ktoré musí Cestovný agent vykonať, aby efektívne pomohol používateľovi s plánovaním cesty:

### Kroky pre Cestovného agenta

1. **Získať používateľské preferencie**
   - Spýtať sa používateľa na detaily o termínoch cesty, rozpočte, záujmoch a akýchkoľvek špecifických požiadavkách.
   - Príklady: „Kedy plánujete cestovať?“ „Aký máte rozpočtový rámec?“ „Aké aktivity vás voľný čas bavia?“

2. **Získať informácie**
   - Vyhľadať relevantné možnosti cestovania na základe preferencií používateľa.
   - **Lety**: Vyhľadať dostupné lety v rámci rozpočtu a preferovaných dátumov.
   - **Ubytovanie**: Nájsť hotely alebo prenájmy, ktoré vyhovujú preferenciám používateľa ohľadom lokality, ceny a vybavenia.
   - **Atrakcie a reštaurácie**: Určiť populárne atrakcie, aktivity a reštauračné možnosti, ktoré zodpovedajú záujmom používateľa.

3. **Vytvoriť odporúčania**
   - Zostaviť získané informácie do personalizovaného itinerára.
   - Poskytnúť detaily ako možnosti letov, rezervácie hotelov a odporúčané aktivity, dbajúc na prispôsobenie odporúčaní preferenciám používateľa.

4. **Predložiť itinerár používateľovi**
   - Zdieľať navrhovaný itinerár s používateľom na jeho preštudovanie.
   - Príklad: „Tu je navrhovaný itinerár pre vašu cestu do Paríža. Obsahuje detaily o letoch, hotelových rezerváciách a zoznam odporúčaných aktivít a reštaurácií. Dajte mi vedieť svoj názor!“

5. **Získanie spätnej väzby**
   - Požiadať používateľa o spätnú väzbu k navrhnutému itineráru.
   - Príklady: „Páčia sa vám možnosti letov?“ „Je hotel vhodný pre vaše potreby?“ „Chceli by ste pridať alebo odstrániť nejaké aktivity?“

6. **Úprava na základe spätnej väzby**
   - Upraviť itinerár podľa spätnej väzby používateľa.
   - Vykonať potrebné zmeny u letov, ubytovania a odporúčaní aktivít tak, aby lepšie vyhovovali preferenciám používateľa.

7. **Konečné potvrdenie**
   - Predložiť aktualizovaný itinerár používateľovi na konečné potvrdenie.
   - Príklad: „Úpravy podľa vašej spätnej väzby som vykonal. Tu je aktualizovaný itinerár. Vyzerá to všetko dobre?“

8. **Rezervovať a potvrdiť rezervácie**
   - Po schválení itinerára používateľom pokračovať v rezervácii letov, ubytovania a predplánovaných aktivít.
   - Poslať používateľovi potvrdenie.

9. **Poskytnúť priebežnú podporu**
   - Byť k dispozícii na pomoc s akýmikoľvek zmenami alebo ďalšími požiadavkami pred a počas cesty.
   - Príklad: „Ak budete počas cesty potrebovať ďalšiu pomoc, neváhajte ma kedykoľvek kontaktovať!“

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

# Príklad použitia v rámci požiadavky na rezerváciu
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

Najprv začnime pochopením rozdielu medzi RAG nástrojom a predbežným načítaním kontextu.

![RAG vs načítanie kontextu](../../../translated_images/sk/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinuje systém vyhľadávania s generatívnym modelom. Keď sa položí otázka, systém vyhľadá vhodné dokumenty alebo dáta z externého zdroja a tieto získané informácie sa použijú na rozšírenie vstupu pre generatívny model. To pomáha modelu generovať presnejšie a kontextovo relevantnejšie odpovede.

V RAG systéme agent vyhľadáva relevantné informácie z databázy znalostí a používa ich na generovanie vhodných odpovedí alebo akcií.

### Korektívny prístup RAG

Korektívny RAG prístup sa zameriava na použitie metód RAG na opravu chýb a zlepšenie presnosti AI agentov. To zahŕňa:

1. **Techniku promptovania**: Použitie špecifických promptov na nasmerovanie agenta pri vyhľadávaní relevantných informácií.
2. **Nástroj**: Implementáciu algoritmov a mechanizmov umožňujúcich agentovi hodnotiť relevantnosť získaných informácií a generovať presné odpovede.
3. **Hodnotenie**: Neustále posudzovanie výkonu agenta a vykonávanie úprav na zlepšenie presnosti a efektivity.

#### Príklad: Korektívny RAG v search agentovi

Uvažujme search agenta, ktorý vyhľadáva informácie z webu na odpovedanie otázok používateľov. Korektívny RAG prístup môže zahŕňať:

1. **Techniku promptovania**: Formuláciu vyhľadávacích dopytov na základe vstupu používateľa.
2. **Nástroj**: Použitie spracovania prirodzeného jazyka a strojového učenia na triedenie a filtrovanie výsledkov vyhľadávania.
3. **Hodnotenie**: Analýzu spätnej väzby používateľa na identifikáciu a opravu nepresností v získaných informáciách.

### Korektívny RAG v Cestovnom agentovi

Korektívny RAG (Retrieval-Augmented Generation) zvyšuje schopnosť AI získavať a generovať informácie a zároveň opravovať akékoľvek nepresnosti. Pozrime sa, ako môže Cestovný agent použiť korektívny RAG prístup na poskytovanie presnejších a relevantnejších odporúčaní pre cestovanie.

Toto zahŕňa:

- **Techniku promptovania:** Použitie konkrétnych promptov na nasmerovanie agenta pri vyhľadávaní relevantných informácií.
- **Nástroj:** Implementáciu algoritmov a mechanizmov, ktoré umožňujú agentovi hodnotiť relevantnosť získaných informácií a generovať presné odpovede.
- **Hodnotenie:** Neustále hodnotenie výkonu agenta a vykonávanie úprav na zlepšenie presnosti a efektivity.

#### Kroky na implementáciu korektívneho RAG v Cestovnom agentovi

1. **Počiatočná interakcia s používateľom**
   - Cestovný agent zhromažďuje počiatočné preferencie od používateľa, ako sú cieľová destinácia, termíny cesty, rozpočet a záujmy.
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
   - Cestovný agent získava informácie o letoch, ubytovaní, atrakciách a reštauráciách na základe používateľských preferencií.
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
   - Cestovný agent žiada používateľa o spätnú väzbu k počiatočným odporúčaniam.
   - Príklad:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces korektívneho RAG**
   - **Technika promptovania**: Cestovný agent formulujem nové vyhľadávacie dotazy na základe spätnej väzby používateľa.
     - Príklad:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Nástroj**: Cestovný agent používa algoritmy na triedenie a filtrovanie nových výsledkov vyhľadávania s dôrazom na relevantnosť podľa spätnej väzby používateľa.
     - Príklad:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Hodnotenie**: Cestovný agent neustále vyhodnocuje relevantnosť a presnosť svojich odporúčaní analyzovaním spätnej väzby a vykonáva potrebné úpravy.
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

Tu je zjednodušený príklad Python kódu začleňujúci korektívny RAG prístup v Cestovnom agentovi:

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

### Predbežné načítanie kontextu
Predbežné načítanie kontextu znamená načítanie relevantného kontextu alebo základných informácií do modelu pred spracovaním dotazu. To znamená, že model má k týmto informáciám prístup od začiatku, čo mu môže pomôcť generovať lepšie informované odpovede bez potreby vyhľadávania ďalších údajov počas procesu.

Tu je zjednodušený príklad, ako môže vyzerať predbežné načítanie kontextu pre aplikáciu cestovného agenta v Pythone:

```python
class TravelAgent:
    def __init__(self):
        # Prednačítanie populárnych destinácií a ich informácií
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

1. **Inicializácia (`__init__` metóda)**: Trieda `TravelAgent` prednačíta slovník obsahujúci informácie o populárnych destináciách ako Paríž, Tokio, New York a Sydney. Tento slovník obsahuje detaily ako krajina, mena, jazyk a hlavné atrakcie každej destinácie.

2. **Získavanie informácií (`get_destination_info` metóda)**: Keď používateľ zadá dotaz ohľadne konkrétnej destinácie, metóda `get_destination_info` načíta relevantné informácie zo slovníka, ktorý bol predom načítaný.

Prednačítaním kontextu môže aplikácia cestovného agenta rýchlo reagovať na dotazy používateľov bez potreby vyhľadávania týchto informácií z externého zdroja v reálnom čase. To robí aplikáciu efektívnejšou a rýchlejšou.

### Naštartovanie plánu s cieľom pred iteráciou

Naštartovanie plánu s cieľom znamená začať so jasne definovaným cieľom alebo požadovaným výsledkom na mysli. Definovaním tohto cieľa vopred model môže použiť tento cieľ ako vodítko počas celého iteratívneho procesu. To pomáha zabezpečiť, že každá iterácia sa priblíži k dosiahnutiu požadovaného výsledku, čím je proces efektívnejší a zameraný.

Tu je príklad, ako môžete naštartovať plán cesty s cieľom pred iteráciou pre cestovného agenta v Pythone:

### Scenár

Cestovný agent chce naplánovať prispôsobenú dovolenku pre klienta. Cieľom je vytvoriť cestovný itinerár, ktorý maximalizuje spokojnosť klienta na základe jeho preferencií a rozpočtu.

### Kroky

1. Definovať preferencie a rozpočet klienta.
2. Naštartovať počiatočný plán na základe týchto preferencií.
3. Iterovať a vylepšovať plán s optimalizáciou pre spokojnosť klienta.

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

1. **Inicializácia (`__init__` metóda)**: Trieda `TravelAgent` je inicializovaná zoznamom potenciálnych destinácií, kde každá má atribúty ako názov, cena a typ aktivity.

2. **Naštartovanie plánu (`bootstrap_plan` metóda)**: Táto metóda vytvorí počiatočný plán cesty na základe preferencií klienta a rozpočtu. Prechádza zoznam destinácií a pridáva ich do plánu, ak vyhovujú preferenciám klienta a zmestia sa do rozpočtu.

3. **Porovnávanie preferencií (`match_preferences` metóda)**: Táto metóda kontroluje, či destinácia zodpovedá preferenciám klienta.

4. **Iterovanie plánu (`iterate_plan` metóda)**: Táto metóda vylepšuje počiatočný plán snahou nahradiť každú destináciu v pláne lepšou zhodou, pričom zohľadňuje preferencie a rozpočtové obmedzenia klienta.

5. **Výpočet nákladov (`calculate_cost` metóda)**: Táto metóda počíta celkové náklady aktuálneho plánu vrátane potenciálnej novej destinácie.

#### Príklad použitia

- **Počiatočný plán**: Cestovný agent vytvorí počiatočný plán podľa preferencií klienta zameraných na prehliadky pamiatok a rozpočtu 2000 dolárov.
- **Vylepšený plán**: Cestovný agent iteruje plán, optimalizujúc pre preferencie a rozpočet klienta.

Naštartovaním plánu so zreteľným cieľom (napr. maximalizáciou spokojnosti klienta) a iterovaním na vylepšenie plánu môže cestovný agent vytvoriť prispôsobený a optimalizovaný cestovný itinerár pre klienta. Tento prístup zabezpečuje, že plán cesty je od začiatku v súlade s preferenciami a rozpočtom klienta a s každou iteráciou sa zlepšuje.

### Využitie LLM pre znovu-zaradenie a skórovanie

Veľké jazykové modely (LLM) môžu byť použité na znovu-zaradenie a skórovanie hodnotením relevantnosti a kvality získaných dokumentov alebo generovaných odpovedí. Funguje to nasledovne:

**Získavanie:** Počiatočný krok získania vyhľadá súbor kandidátskych dokumentov alebo odpovedí na základe dotazu.

**Znovu-zaradenie:** LLM hodnotí týchto kandidátov a znovu ich radí podľa ich relevantnosti a kvality. Tento krok zabezpečuje, že najrelevantnejšie a najkvalitnejšie informácie sú zobrazené na prvom mieste.

**Skórovanie:** LLM priraďuje skóre každému kandidátovi, reflektujúce jeho relevantnosť a kvalitu. To pomáha vybrať najlepšiu odpoveď alebo dokument pre používateľa.

Využitím LLM na znovu-zaradenie a skórovanie môže systém poskytovať presnejšie a kontextovo relevantnejšie informácie, čím sa zlepší celková používateľská skúsenosť.

Tu je príklad, ako by cestovný agent mohol použiť veľký jazykový model (LLM) na znovu-zaradenie a skórovanie cestovných destinácií na základe preferencií používateľa v Pythone:

#### Scenár - Cestovanie podľa preferencií

Cestovný agent chce odporučiť najlepšie cestovné destinácie klientovi na základe jeho preferencií. LLM pomôže znovu-zaradiť a skórovať destinácie, aby sa zabezpečilo, že najrelevantnejšie možnosti budú predstavené.

#### Kroky:

1. Zhromaždiť preferencie používateľa.
2. Získať zoznam potenciálnych cestovných destinácií.
3. Použiť LLM na znovu-zaradenie a skórovanie destinácií na základe preferencií.

Tu je aktualizácia predchádzajúceho príkladu na použitie Azure OpenAI služieb:

#### Požiadavky

1. Potrebujete mať Azure predplatné.
2. Vytvorte Azure OpenAI zdroj a získajte svoj API kľúč.

#### Príklad Python kódu

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Vygenerujte požiadavku pre Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definujte hlavičky a obsah pre požiadavku
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Zavolajte API Azure OpenAI, aby ste získali pretriedené a ohodnotené destinácie
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

#### Vysvetlenie kódu - Preference Booker

1. **Inicializácia**: Trieda `TravelAgent` je inicializovaná zoznamom potenciálnych cestovných destinácií, každá s atribútmi ako názov a popis.

2. **Získavanie odporúčaní (`get_recommendations` metóda)**: Táto metóda generuje prompt pre Azure OpenAI službu na základe preferencií používateľa a vykonáva HTTP POST požiadavku na Azure OpenAI API, aby získala znovu-zaradené a skórované destinácie.

3. **Generovanie promptu (`generate_prompt` metóda)**: Táto metóda konštruuje prompt pre Azure OpenAI, vrátane preferencií používateľa a zoznamu destinácií. Prompt vedie model, aby destinácie znovu zoradil a ohodnotil podľa daných preferencií.

4. **API volanie**: Knižnica `requests` je použitá na vykonanie HTTP POST požiadavky na Azure OpenAI API endpoint. Odpoveď obsahuje znovu-zaradené a skórované destinácie.

5. **Príklad použitia**: Cestovný agent zhromaždí preferencie používateľa (napr. záujem o prehliadky pamiatok a rôznorodú kultúru) a použije Azure OpenAI službu, aby získal znovu-zaradené a skórované odporúčania cestovných destinácií.

Nezabudnite nahradiť `your_azure_openai_api_key` svojím skutočným API kľúčom Azure OpenAI a `https://your-endpoint.com/...` skutočnou URL adresou endpointu vášho Azure OpenAI nasadenia.

Využitím LLM na znovu-zaradenie a skórovanie môže cestovný agent poskytovať personalizovanejšie a relevantnejšie cestovné odporúčania klientom, čím zlepší ich celkovú skúsenosť.

### RAG: Technika promptovania vs Nástroj

Retrieval-Augmented Generation (RAG) môže byť zároveň technika promptovania a nástroj vo vývoji AI agentov. Pochopenie rozdielu medzi nimi vám môže pomôcť lepšie využiť RAG vo vašich projektoch.

#### RAG ako technika promptovania

**Čo to je?**

- Ako technika promptovania RAG zahŕňa formulovanie špecifických dotazov alebo promptov na vedenie získania relevantných informácií z veľkého korpusu alebo databázy. Tieto informácie sa potom používajú na generovanie odpovedí alebo akcií.

**Ako to funguje:**

1. **Formulovanie promptov**: Vytvorte dobre štruktúrované prompty alebo dotazy na základe úlohy alebo vstupu používateľa.
2. **Získavanie informácií**: Použite prompty na vyhľadanie relevantných údajov zo existujúcej bázy poznatkov alebo dátovej množiny.
3. **Generovanie odpovede**: Kombinujte získané informácie s generatívnymi AI modelmi na vytvorenie komplexnej a súdržnej odpovede.

**Príklad v cestovnom agentovi**:

- Vstup používateľa: "Chcem navštíviť múzeá v Paríži."
- Prompt: "Nájdi najlepšie múzeá v Paríži."
- Získané informácie: Detaily o Louvri, Musée d'Orsay atď.
- Generovaná odpoveď: "Tu sú niektoré najlepšie múzeá v Paríži: Louvre, Musée d'Orsay a Centre Pompidou."

#### RAG ako nástroj

**Čo to je?**

- Ako nástroj je RAG integrovaný systém, ktorý automatizuje proces získavania a generovania, čím uľahčuje vývojárom implementovať komplexné AI funkcie bez potreby manuálneho vytvárania promptov pre každý dotaz.

**Ako to funguje:**

1. **Integrácia**: Zapojiť RAG priamo do architektúry AI agenta, čo mu umožní automaticky spracovávať získavanie a generovanie.
2. **Automatizácia**: Nástroj riadi celý proces od prijatia vstupu používateľa až po generovanie finálnej odpovede bez potreby explicitných promptov pre každý krok.
3. **Efektivita**: Zvyšuje výkon agenta zjednodušením procesu získavania a generovania, čo umožňuje rýchlejšie a presnejšie odpovede.

**Príklad v cestovnom agentovi**:

- Vstup používateľa: "Chcem navštíviť múzeá v Paríži."
- RAG nástroj: Automaticky získa informácie o múzeách a vygeneruje odpoveď.
- Generovaná odpoveď: "Tu sú niektoré najlepšie múzeá v Paríži: Louvre, Musée d'Orsay a Centre Pompidou."

### Porovnanie

| Aspekt                 | Technika promptovania                                     | Nástroj                                               |
|------------------------|------------------------------------------------------------|-------------------------------------------------------|
| **Manuálne vs Automatické** | Manuálne vytváranie promptov pre každý dotaz.          | Automatizovaný proces získavania a generovania.        |
| **Kontrola**            | Poskytuje väčšiu kontrolu nad procesom získavania.        | Zjednodušuje a automatizuje proces získavania a generovania. |
| **Flexibilita**         | Umožňuje prispôsobené prompty podľa potrieb.              | Efektívnejšie pre rozsiahle implementácie.            |
| **Zložitosť**           | Vyžaduje tvorbu a dolaďovanie promptov.                    | Ľahšie integrovať do architektúry AI agenta.          |

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

### Hodnotenie relevancie

Hodnotenie relevancie je kľúčovým aspektom výkonu AI agenta. Zabezpečuje, že informácie získané a generované agentom sú vhodné, presné a užitočné pre používateľa. Pozrime sa, ako hodnotiť relevanciu v AI agentoch vrátane praktických príkladov a techník.

#### Kľúčové koncepty hodnotenia relevancie

1. **Spoznanie kontextu**:
   - Agent musí rozumieť kontextu používateľovho dotazu, aby načítal a generoval relevantné informácie.
   - Príklad: Ak používateľ žiada o "najlepšie reštaurácie v Paríži", agent by mal zohľadniť jeho preferencie, ako typ kuchyne či rozpočet.

2. **Presnosť**:
   - Informácie poskytované agentom by mali byť fakticky správne a aktuálne.
   - Príklad: Odporučiť aktuálne otvorené reštaurácie s dobrými recenziami, nie zastaralé alebo zatvorené miesta.

3. **Úmysel používateľa**:
   - Agent by mal vyvodiť úmysel používateľa za dotazom, aby poskytol najrelevantnejšie informácie.
   - Príklad: Ak používateľ hľadá "lacné hotely", agent by mal uprednostniť dostupné možnosti.

4. **Spätná väzba**:
   - Neustále zbieranie a analyzovanie spätnej väzby používateľov pomáha agentovi zlepšovať proces hodnotenia relevancie.
   - Príklad: Začleniť hodnotenia a spätnú väzbu na predchádzajúce odporúčania pre lepšie budúce odpovede.

#### Praktické techniky hodnotenia relevancie

1. **Skórovanie relevancie**:
   - Priraďte každej položke získanej na základe dotazu skóre relevancie podľa zhody s dotazom a preferenciami používateľa.
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

2. **Filtrovanie a radenie**:
   - Vyfiltrujte nerelevantné položky a zoradte zostávajúce podľa ich skóre relevancie.
   - Príklad:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrátiť 10 najrelevantnejších položiek
     ```

3. **Spracovanie prirodzeného jazyka (NLP)**:
   - Použite NLP techniky na porozumenie dotazu používateľa a získanie relevantných informácií.
   - Príklad:

     ```python
     def process_query(query):
         # Použite NLP na extrahovanie kľúčových informácií z dopytu používateľa
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrácia spätnej väzby používateľa**:
   - Zbierajte spätnú väzbu na poskytnuté odporúčania a používajte ju na úpravu budúceho hodnotenia relevancie.
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

#### Príklad: Hodnotenie relevancie v Travel Agentovi

Tu je praktický príklad, ako môže Travel Agent hodnotiť relevanciu cestovných odporúčaní:

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
        return ranked_items[:10]  # Vrátiť 10 najrelevantnejších položiek

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

### Vyhľadávanie s úmyslom

Vyhľadávanie s úmyslom znamená pochopenie a interpretáciu základného účelu alebo cieľa za dotazom používateľa na získanie a generovanie najrelevantnejších a najpoužiteľnejších informácií. Tento prístup ide nad rámec jednoduchého zhody kľúčových slov a sústreďuje sa na pochopenie skutočných potrieb a kontextu používateľa.

#### Kľúčové koncepty vyhľadávania s úmyslom

1. **Pochopenie úmyslu používateľa**:
   - Úmysel používateľa možno rozdeliť do troch hlavných typov: informačný, navigačný a transakčný.
     - **Informačný úmysel**: Používateľ hľadá informácie o téme (napr. "Aké sú najlepšie múzeá v Paríži?").
     - **Navigačný úmysel**: Používateľ chce prejsť na konkrétnu webovú stránku alebo stránku (napr. "Oficiálna stránka Louvru").
     - **Transakčný úmysel**: Používateľ chce vykonať transakciu, ako rezervovať let alebo nakúpiť (napr. "Rezervuj letenku do Paríža").

2. **Spoznanie kontextu**:
   - Analýza kontextu dotazu používateľa pomáha presnejšie identifikovať jeho úmysel. To zahŕňa zváženie predchádzajúcich interakcií, preferencií používateľa a konkrétne detaily aktuálneho dotazu.

3. **Spracovanie prirodzeného jazyka (NLP)**:
   - NLP techniky sa používajú na rozpoznanie a interpretáciu prirodzených jazykových dotazov používateľov. To zahŕňa úlohy ako rozpoznávanie entít, analýzu sentimentu a parsovanie dotazu.

4. **Personalizácia**:
   - Personalizácia výsledkov vyhľadávania podľa histórie, preferencií a spätnej väzby používateľa zvyšuje relevanciu získaných informácií.

#### Praktický príklad: Vyhľadávanie s úmyslom v Travel Agentovi

Pozrime sa na Travel Agent ako príklad, ako možno implementovať vyhľadávanie s úmyslom.

1. **Zhromažďovanie preferencií používateľa**

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

3. **Spoznanie kontextu**
   ```python
   def analyze_context(query, user_history):
       # Kombinovať aktuálny dopyt s históriou používateľa, aby sme pochopili kontext
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
       # Príklad vyhľadávacej logiky pre informačný úmysel
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Príklad vyhľadávacej logiky pre navigačný úmysel
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Príklad vyhľadávacej logiky pre transakčný úmysel
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

Agenti generujúci kód používajú modely AI na písanie a vykonávanie kódu, riešenie zložitých problémov a automatizáciu úloh.

### Agenti generujúci kód

Agenti generujúci kód používajú generatívne AI modely na písanie a vykonávanie kódu. Títo agenti dokážu riešiť zložité problémy, automatizovať úlohy a poskytovať cenné poznatky generovaním a spustením kódu v rôznych programovacích jazykoch.

#### Praktické aplikácie

1. **Automatizované generovanie kódu**: Generovanie kódových útržkov pre špecifické úlohy, ako je analýza dát, web scraping alebo strojové učenie.
2. **SQL ako RAG**: Použitie SQL dotazov na získavanie a manipuláciu s údajmi z databáz.
3. **Riešenie problémov**: Vytváranie a vykonávanie kódu na riešenie konkrétnych problémov, ako je optimalizácia algoritmov alebo analýza dát.

#### Príklad: Agent generujúci kód na analýzu dát

Predstavte si, že navrhujete agenta generujúceho kód. Tu je, ako by mohol fungovať:

1. **Úloha**: Analyzovať dataset a identifikovať trendy a vzory.
2. **Kroky**:
   - Načítať dataset do nástroja na analýzu dát.
   - Vygenerovať SQL dotazy na filtrovanie a agregáciu dát.
   - Vykonať dotazy a získať výsledky.
   - Použiť výsledky na generovanie vizualizácií a poznatkov.
3. **Potrebné zdroje**: Prístup k datasetu, nástroje na analýzu dát a SQL schopnosti.
4. **Zkušenosti**: Použiť výsledky z minulých analýz na zlepšenie presnosti a relevantnosti budúcich analýz.

### Príklad: Agent generujúci kód pre cestovnú agentúru

V tomto príklade navrhneme agenta generujúceho kód, Cestovnú agentúru, ktorý pomôže používateľom plánovať ich cestovanie generovaním a vykonávaním kódu. Tento agent môže spracovať úlohy ako načítanie možností cestovania, filtrovanie výsledkov a zostavenie itinerára pomocou generatívnej AI.

#### Prehľad agenta generujúceho kód

1. **Zhromažďovanie používateľských preferencií**: Zhromažďuje vstupy používateľa ako cieľ cesty, dátumy, rozpočet a záujmy.
2. **Generovanie kódu na získanie dát**: Generuje kódové útržky na získanie dát o letoch, hoteloch a atrakciách.
3. **Vykonávanie vygenerovaného kódu**: Spúšťa vygenerovaný kód na získanie aktuálnych informácií.
4. **Generovanie itinerára**: Kompiluje získané údaje do personalizovaného cestovného plánu.
5. **Úprava na základe spätnej väzby**: Prijíma spätnú väzbu od používateľa a podľa potreby regeneruje kód na vylepšenie výsledkov.

#### Implementácia krok za krokom

1. **Zhromažďovanie používateľských preferencií**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generovanie kódu na získanie dát**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Príklad: Vygenerujte kód na vyhľadávanie letov podľa preferencií používateľa
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

3. **Vykonávanie vygenerovaného kódu**

   ```python
   def execute_code(code):
       # Spustiť vygenerovaný kód pomocou exec
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
       # Upravte preferencie na základe spätnej väzby od používateľa
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Znovu vygenerujte a vykonajte kód s aktualizovanými preferenciami
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Využitie environmentálneho povedomia a uvažovania

Na základe schémy tabuľky možno skutočne vylepšiť proces generovania dotazov využitím environmentálneho povedomia a uvažovania.

Tu je príklad, ako sa to dá urobiť:

1. **Pochopenie schémy**: Systém pochopí schému tabuľky a použije túto informáciu na podloženie generovania dotazov.
2. **Úprava na základe spätnej väzby**: Systém upraví používateľské preferencie na základe spätnej väzby a uvažuje o tom, ktoré polia v schéme treba aktualizovať.
3. **Generovanie a vykonávanie dotazov**: Systém vygeneruje a vykoná dotazy na získanie aktualizovaných údajov o letoch a hoteloch na základe nových preferencií.

Tu je aktualizovaný príklad Python kódu, ktorý tieto koncepty obsahuje:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Prispôsobiť preferencie na základe spätnej väzby používateľa
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
    # Vygenerovať kód na získanie údajov o letoch na základe aktualizovaných preferencií
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Vygenerovať kód na získanie údajov o hoteloch na základe aktualizovaných preferencií
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulovať vykonanie kódu a vrátiť falošné údaje
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Vytvoriť itinerár na základe letov, hotelov a atrakcií
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

# Znova vygenerovať a vykonať kód s aktualizovanými preferenciami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Vysvetlenie – Rezervácia na základe spätnej väzby

1. **Povedomie o schéme**: Slovník `schema` definuje, ako majú byť preferencie upravené na základe spätnej väzby. Obsahuje polia ako `favorites` a `avoid` s príslušnými úpravami.
2. **Úprava preferencií (metóda `adjust_based_on_feedback`)**: Táto metóda upravuje preferencie na základe spätnej väzby používateľa a schémy.
3. **Úpravy založené na prostredí (metóda `adjust_based_on_environment`)**: Táto metóda prispôsobuje úpravy na základe schémy a spätnej väzby.
4. **Generovanie a vykonávanie dotazov**: Systém generuje kód na získanie aktualizovaných údajov o letoch a hoteloch na základe upravených preferencií a simuluje vykonanie týchto dotazov.
5. **Generovanie itinerára**: Systém vytvorí aktualizovaný itinerár na základe nových informácií o letoch, hoteloch a atrakciách.

Vďaka tomu, že systém je environmentálne uvedomelý a uvažuje na základe schémy, dokáže generovať presnejšie a relevantnejšie dotazy, čo vedie k lepším cestovným odporúčaniam a personalizovanejšiemu užívateľskému zážitku.

### Použitie SQL ako Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) je výkonný nástroj na interakciu s databázami. Keď sa používa ako súčasť prístupu Retrieval-Augmented Generation (RAG), SQL môže načítať relevantné dáta z databáz na informovanie a generovanie odpovedí alebo akcií v AI agentoch. Pozrime sa, ako možno SQL využiť ako RAG techniku v kontexte Cestovnej agentúry.

#### Kľúčové koncepty

1. **Interakcia s databázou**:
   - SQL sa používa na dotazovanie databáz, získavanie relevantných informácií a manipuláciu s dátami.
   - Príklad: Získavanie detailov letov, informácií o hoteloch a atrakciách v databáze o cestovaní.

2. **Integrácia s RAG**:
   - SQL dotazy sú generované na základe vstupov a preferencií používateľa.
   - Načítané dáta sa následne používajú na generovanie personalizovaných odporúčaní alebo akcií.

3. **Dynamické generovanie dotazov**:
   - AI agent generuje dynamické SQL dotazy na základe kontextu a potrieb používateľa.
   - Príklad: Prispôsobovanie SQL dotazov na filtrovanie výsledkov podľa rozpočtu, dátumov a záujmov.

#### Aplikácie

- **Automatizované generovanie kódu**: Generovanie kódových útržkov pre konkrétne úlohy.
- **SQL ako RAG**: Použitie SQL dotazov na manipuláciu s dátami.
- **Riešenie problémov**: Vytváranie a vykonávanie kódu na riešenie problémov.

**Príklad**:
Agent na analýzu dát:

1. **Úloha**: Analyzovať dataset a nájsť trendy.
2. **Kroky**:
   - Načítať dataset.
   - Generovať SQL dotazy na filtrovanie dát.
   - Vykonať dotazy a získať výsledky.
   - Generovať vizualizácie a poznatky.
3. **Zdroje**: Prístup k datasetu, SQL schopnosti.
4. **Zkušenosti**: Použiť predchádzajúce výsledky na zlepšenie budúcich analýz.

#### Praktický príklad: Použitie SQL v Cestovnej agentúre

1. **Zhromažďovanie používateľských preferencií**

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

Vďaka využitiu SQL ako súčasti Retrieval-Augmented Generation (RAG) techniky môžu AI agenti ako Cestovná agentúra dynamicky získavať a využívať relevantné dáta na poskytovanie presných a personalizovaných odporúčaní.

### Príklad metakognície

Aby sme demonštrovali implementáciu metakognície, vytvorme jednoduchého agenta, ktorý *reflektuje svoj proces rozhodovania* pri riešení problému. V tomto príklade postavíme systém, kde agent skúša optimalizovať výber hotela, ale potom vyhodnocuje vlastné uvažovanie a upravuje stratégiu, keď robí chyby alebo suboptimálne rozhodnutia.

Simulujeme to na jednoduchom príklade, kde agent vyberá hotely na základe kombinácie ceny a kvality, ale „reflektuje“ svoje rozhodnutia a podľa toho sa upravuje.

#### Ako to ilustruje metakogníciu:

1. **Počiatočné rozhodnutie**: Agent vyberie najlacnejší hotel bez pochopenia vplyvu kvality.
2. **Reflexia a vyhodnotenie**: Po počiatočnom výbere agent skontroluje, či hotel bol „zlou“ voľbou pomocou spätnej väzby používateľa. Ak zistí, že kvalita hotela bola príliš nízka, reflektuje nad svojím rozhodovaním.
3. **Úprava stratégie**: Agent upraví svoju stratégiu na základe reflexie a prejde z výberu „najracionálnejšieho“ na „najkvalitnejší“, čím zlepší svoj rozhodovací proces v budúcich iteráciách.

Tu je príklad:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Uchováva predtým vybrané hotely
        self.corrected_choices = []  # Uchováva opravené voľby
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
        # Predpokladajme, že máme spätnú väzbu od používateľa, ktorá nám hovorí, či bola posledná voľba dobrá alebo nie
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Uprav stratégiu, ak bola predchádzajúca voľba neuspokojivá
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

# Simuluj zoznam hotelov (cena a kvalita)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Vytvor agenta
agent = HotelRecommendationAgent()

# Krok 1: Agent odporučí hotel pomocou stratégie "najlacnejší"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Krok 2: Agent zhodnotí voľbu a v prípade potreby upraví stratégiu
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Krok 3: Agent opäť odporučí, tentokrát pomocou upravenej stratégie
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Schopnosti metakognície agentov

Kľúčové je tu schopnosť agenta:
- Vyhodnocovať svoje predchádzajúce voľby a rozhodovací proces.
- Upraviť svoju stratégiu na základe tejto reflexie, teda metakognícia v praxi.

Ide o jednoduchú formu metakognície, kde systém dokáže prispôsobiť svoje uvažovanie na základe internej spätnej väzby.

### Záver

Metakognícia je silný nástroj, ktorý môže významne vylepšiť schopnosti AI agentov. Vďaka začleneniu metakognitívnych procesov môžete navrhnúť agentov, ktorí sú inteligentnejší, prispôsobivejší a efektívnejší. Použite dodatočné zdroje na ďalšie preskúmanie fascinujúceho sveta metakognície v AI agentoch.

### Máte ďalšie otázky o návrhovom vzore metakognície?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa office hours a získať odpovede na svoje otázky o AI agentoch.

## Predchádzajúca lekcia

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Nasledujúca lekcia

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->