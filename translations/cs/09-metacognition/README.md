[![Návrh vícero agentů](../../../translated_images/cs/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_
# Metakognice u AI agentů

## Úvod

Vítejte v lekci o metakognici u AI agentů! Tato kapitola je určena pro začátečníky, kteří se zajímají o to, jak mohou agenti AI přemýšlet o vlastních procesech myšlení. Na konci této lekce budete rozumět klíčovým konceptům a budete vybaveni praktickými příklady, jak metakognici aplikovat při návrhu AI agentů.

## Cíle učení

Po dokončení této lekce budete umět:

1. Pochopit důsledky smyček uvažování v definicích agentů.
2. Použít techniky plánování a vyhodnocování k podpoře samoopravných agentů.
3. Vytvořit vlastní agenty schopné manipulovat s kódem k plnění úkolů.

## Úvod do metakognice

Metakognice odkazuje na kognitivní procesy vyššího řádu, které zahrnují přemýšlení o vlastním myšlení. Pro AI agenty to znamená schopnost hodnotit a upravovat své akce na základě sebeuvědomění a minulých zkušeností. Metakognice, neboli "přemýšlení o přemýšlení," je důležitý koncept při vývoji agentních AI systémů. Zahrnuje, že AI systémy si uvědomují své vlastní vnitřní procesy a jsou schopné monitorovat, regulovat a přizpůsobovat své chování odpovídajícím způsobem. Podobně jako když my „čteme“ situaci v místnosti nebo se díváme na problém. Toto sebeuvědomění může AI systémům pomoci učinit lepší rozhodnutí, odhalit chyby a zlepšit svůj výkon v průběhu času – opět se tak spojuje s Turingovým testem a debatou o tom, zda AI převezme kontrolu.

V kontextu agentních AI systémů může metakognice pomoci řešit několik výzev, jako jsou:
- Transparentnost: Zajištění toho, aby AI systémy dokázaly vysvětlit své uvažování a rozhodnutí.
- Uvažování: Zvýšení schopnosti AI systémů syntetizovat informace a učinit opodstatněná rozhodnutí.
- Adaptace: Umožnění AI systémům přizpůsobovat se novým prostředím a měnícím se podmínkám.
- Vnímání: Zlepšení přesnosti AI systémů při rozpoznávání a interpretaci dat ze svého prostředí.

### Co je metakognice?

Metakognice, neboli „přemýšlení o přemýšlení,“ je kognitivní proces vyššího řádu, který zahrnuje sebeuvědomění a seberegulaci vlastních kognitivních procesů. V oblasti AI umožňuje metakognice agentům hodnotit a přizpůsobovat své strategie a akce, což vede ke zlepšení schopnosti řešit problémy a rozhodovat se. Pochopením metakognice můžete navrhovat AI agenty, kteří jsou nejen chytřejší, ale také více adaptabilní a efektivní. Ve skutečné metakognici by AI explicite uvažovala o svém vlastním uvažování.

Příklad: „Upřednostnil jsem levnější lety, protože… mohl bych tak propásnout přímé lety, takže si to znovu ověřím.“
Sledování toho, jak nebo proč zvolila určitou trasu.
- Uvědomění si, že udělala chyby, protože příliš spoléhala na uživatelské preference z minulého času, takže modifikuje svou strategii rozhodování, nejen finální doporučení.
- Diagnostikuje vzorce jako: „Kdykoliv uživatel zmíní 'příliš přeplněno,' neměl bych jen odebrat některé atrakce, ale také reflektovat, že moje metoda výběru ‚nejlepších atrakcí‘ je chybná, pokud je vždy řadím podle popularity.“

### Význam metakognice u AI agentů

Metakognice hraje zásadní roli v návrhu AI agentů z několika důvodů:

![Význam metakognice](../../../translated_images/cs/importance-of-metacognition.b381afe9aae352f7.webp)

- Sebereflexe: Agenti mohou hodnotit svůj vlastní výkon a identifikovat oblasti ke zlepšení.
- Adaptabilita: Agenti mohou měnit své strategie na základě minulých zkušeností a měnících se podmínek.
- Oprava chyb: Agenti mohou autonomně odhalovat a opravovat chyby, což vede k přesnějším výsledkům.
- Řízení zdrojů: Agenti mohou optimalizovat využití zdrojů, jako je čas a výpočetní výkon, plánováním a vyhodnocováním svých akcí.

## Komponenty AI agenta

Než se ponoříme do metakognitivních procesů, je důležité pochopit základní komponenty AI agenta. AI agent obvykle obsahuje:

- Persona: Osobnost a charakteristiky agenta, které definují, jak komunikuje s uživateli.
- Nástroje: Schopnosti a funkce, které agent může vykonávat.
- Dovednosti: Znalosti a expertízu, kterou agent vlastní.

Tyto komponenty spolupracují při vytváření „jednotky odbornosti“, která dokáže vykonávat specifické úkoly.

**Příklad**:
Uvažujte o cestovním agentovi, což jsou služby agenta, které nejen plánují vaši dovolenou, ale také upravují plán na základě dat v reálném čase a minulých zkušeností uživatelů.

### Příklad: Metakognice v cestovní agentuře

Představte si, že navrhujete službu cestovního agenta řízenou AI. Tento agent, „Cestovní agent,“ pomáhá uživatelům plánovat dovolené. Aby mohl inkorporovat metakognici, musí Cestovní agent hodnotit a upravovat své akce na základě sebeuvědomění a minulých zkušeností. Zde je, jak by metakognice mohla hrát roli:

#### Aktuální úkol

Aktuální úkol je pomoci uživateli naplánovat cestu do Paříže.

#### Kroky k dokončení úkolu

1. **Shromáždit uživatelské preference**: Zeptat se uživatele na data cesty, rozpočet, zájmy (např. muzea, kuchyně, nakupování) a jakékoli specifické požadavky.
2. **Získat informace**: Vyhledat možnosti letů, ubytování, atrakcí a restaurací, které odpovídají preferencím uživatele.
3. **Vygenerovat doporučení**: Poskytnout personalizovaný itinerář s detaily o letech, rezervacích hotelů a navrhovaných aktivitách.
4. **Upravit na základě zpětné vazby**: Zeptat se uživatele na zpětnou vazbu ohledně doporučení a provést potřebné úpravy.

#### Potřebné zdroje

- Přístup k databázím letů a hotelových rezervací.
- Informace o pařížských atrakcích a restauracích.
- Data o zpětné vazbě uživatelů z předchozích interakcí.

#### Zkušenosti a sebereflexe

Cestovní agent využívá metakognici k hodnocení svého výkonu a učení se z minulých zkušeností. Například:

1. **Analýza zpětné vazby uživatelů**: Cestovní agent zkoumá zpětnou vazbu uživatelů, aby zjistil, která doporučení byla dobře přijata a která ne. Podle toho upravuje svá budoucí doporučení.
2. **Adaptabilita**: Pokud uživatel dříve zmínil nesympatii k přeplněným místům, Cestovní agent se v budoucnu vyhne doporučování populárních turistických míst během špičky.
3. **Oprava chyb**: Pokud Cestovní agent v minulosti udělal chybu, například doporučil hotel, který byl plně obsazen, naučí se důkladněji kontrolovat dostupnost před poskytnutím doporučení.

#### Praktický příklad pro vývojáře

Zde je zjednodušený příklad, jak by mohl vypadat kód Cestovního agenta, který začleňuje metakognici:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Vyhledávejte lety, hotely a atrakce na základě preferencí
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
        # Analyzujte zpětnou vazbu a upravte budoucí doporučení
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Příklad použití
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

#### Proč je metakognice důležitá

- **Sebereflexe**: Agenti mohou analyzovat svůj výkon a identifikovat oblasti ke zlepšení.
- **Adaptabilita**: Agenti mohou upravovat strategie na základě zpětné vazby a měnících se podmínek.
- **Oprava chyb**: Agenti mohou autonomně odhalovat a opravovat chyby.
- **Řízení zdrojů**: Agenti mohou optimalizovat využití zdrojů, jako je čas a výpočetní výkon.

Začleněním metakognice může Cestovní agent poskytovat personalizovanější a přesnější doporučení na cesty, čímž se zlepší celkový uživatelský zážitek.

---

## 2. Plánování u agentů

Plánování je klíčová součást chování AI agenta. Zahrnuje vymezení kroků potřebných k dosažení cíle s ohledem na aktuální stav, zdroje a možné překážky.

### Prvky plánování

- **Aktuální úkol**: Jasně definovat úkol.
- **Kroky k dokončení úkolu**: Rozdělit úkol na zvládnutelné kroky.
- **Potřebné zdroje**: Identifikovat potřebné zdroje.
- **Zkušenosti**: Využít minulé zkušenosti k informování plánování.

**Příklad**:
Zde jsou kroky, které musí Cestovní agent podniknout, aby účinně pomohl uživateli při plánování jeho cesty:

### Kroky pro Cestovního agenta

1. **Shromáždit uživatelské preference**
   - Zeptat se uživatele na detaily o termínech cestování, rozpočtu, zájmech a jakékoli specifické požadavky.
   - Příklady: "Kdy plánujete cestovat?" "Jaký je váš rozpočtový rámec?" "Jaké aktivity si užíváte na dovolené?"

2. **Získat informace**
   - Vyhledat relevantní možnosti cestování na základě uživatelských preferencí.
   - **Letenky**: Hledat dostupné lety v rámci rozpočtu a preferovaných termínů uživatele.
   - **Ubytování**: Najít hotely nebo pronájmy odpovídající preferencím uživatele ohledně lokality, ceny a vybavení.
   - **Atrakce a restaurace**: Identifikovat populární atrakce, aktivity a jídelny, které odpovídají zájmům uživatele.

3. **Vygenerovat doporučení**
   - Sestavit získané informace do personalizovaného itineráře.
   - Poskytnout detaily jako možnosti letů, rezervace hotelů a navrhované aktivity, přičemž doporučení doladit podle uživatelských preferencí.

4. **Předložit itinerář uživateli**
   - Sdílet navržený itinerář s uživatelem k jeho přezkoumání.
   - Příklad: "Zde je navržený itinerář pro vaši cestu do Paříže. Obsahuje detaily o letech, rezervacích hotelů a seznam doporučených aktivit a restaurací. Dejte mi vědět svůj názor!"

5. **Sbírat zpětnou vazbu**
   - Zeptat se uživatele na zpětnou vazbu k navrženému itineráři.
   - Příklady: "Líbí se vám možnosti letů?" "Vyhovuje hotel vašim potřebám?" "Jsou nějaké aktivity, které byste chtěli přidat nebo odebrat?"

6. **Upravit na základě zpětné vazby**
   - Modifikovat itinerář podle uživatelské zpětné vazby.
   - Učinit potřebné změny v doporučeních letů, ubytování a aktivit, aby lépe odpovídala preferencím uživatele.

7. **Konečné potvrzení**
   - Předložit aktualizovaný itinerář uživateli k finálnímu potvrzení.
   - Příklad: "Provedl jsem úpravy na základě vaší zpětné vazby. Zde je aktualizovaný itinerář. Vypadá to podle vás dobře?"

8. **Rezervace a potvrzení**
   - Jakmile uživatel itinerář schválí, pokračovat s rezervacemi letů, ubytování a předem naplánovaných aktivit.
   - Poslat podrobnosti o potvrzení uživateli.

9. **Poskytovat průběžnou podporu**
   - Být k dispozici k pomoci uživateli s případnými změnami nebo doplňujícími žádostmi před i během cesty.
   - Příklad: "Pokud budete potřebovat další pomoc během vaší cesty, neváhejte se na mě kdykoliv obrátit!"

### Příklad interakce

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

# Příklad použití v rámci žádosti o hostování
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

## 3. Korektivní RAG systém

Nejprve si pojďme vysvětlit rozdíl mezi RAG nástrojem a pre-emptivním načítáním kontextu

![RAG vs načítání kontextu](../../../translated_images/cs/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombinuje retrieval systém s generativním modelem. Když je zadán dotaz, retrieval systém vyhledá relevantní dokumenty nebo data z externího zdroje a tyto získané informace slouží k obohacení vstupu generativního modelu. To pomáhá modelu generovat přesnější a kontextově relevantní odpovědi.

V RAG systému agent získává relevantní informace z báze znalostí a používá je k vytváření vhodných odpovědí nebo akcí.

### Korektivní RAG přístup

Korektivní RAG přístup se zaměřuje na využití RAG technik k opravám chyb a zlepšení přesnosti AI agentů. To zahrnuje:

1. **Technika vyvolávání**: Použití specifických promptů k navádění agenta při získávání relevantních informací.
2. **Nástroj**: Implementace algoritmů a mechanismů, které umožňují agentovi hodnotit relevanci získaných informací a generovat přesné odpovědi.
3. **Vyhodnocení**: Neustálé hodnocení výkonu agenta a provádění úprav ke zvýšení přesnosti a efektivity.

#### Příklad: Korektivní RAG u vyhledávacího agenta

Představme si vyhledávacího agenta, který získává informace z webu pro odpovědi na uživatelské dotazy. Korektivní RAG přístupy mohou zahrnovat:

1. **Technika vyvolávání**: Formulování vyhledávacích dotazů na základě vstupu uživatele.
2. **Nástroj**: Použití zpracování přirozeného jazyka a algoritmů strojového učení k řazení a filtrování výsledků vyhledávání.
3. **Vyhodnocení**: Analyzování zpětné vazby uživatelů s cílem identifikovat a opravit nepřesnosti ve získaných informacích.

### Korektivní RAG v Cestovním agentovi

Korektivní RAG (Retrieval-Augmented Generation) zvyšuje schopnost AI získávat a generovat informace a zároveň opravovat případné nepřesnosti. Podívejme se, jak může Cestovní agent využít korektivní RAG přístup, aby poskytoval přesnější a relevantnější doporučení na cestování.

To zahrnuje:

- **Technika vyvolávání:** Použití specifických promptů k navádění agenta při získávání relevantních informací.
- **Nástroj:** Implementaci algoritmů a mechanismů, které agentovi umožní hodnotit relevanci získaných informací a generovat přesné odpovědi.
- **Vyhodnocení:** Neustálé hodnocení výkonu agenta a provádění úprav ke zvýšení přesnosti a efektivity.

#### Kroky pro implementaci Korektivního RAG v Cestovním agentovi

1. **Počáteční interakce s uživatelem**
   - Cestovní agent získává počáteční preference od uživatele, jako jsou destinace, data cesty, rozpočet a zájmy.
   - Příklad:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Získávání informací**
   - Cestovní agent získává informace o letech, ubytování, atrakcích a restauracích na základě uživatelských preferencí.
   - Příklad:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generování počátečních doporučení**
   - Cestovní agent využívá získané informace k vytvoření personalizovaného itineráře.
   - Příklad:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Sbírání zpětné vazby od uživatele**
   - Cestovní agent žádá uživatele o zpětnou vazbu k počátečním doporučením.
   - Příklad:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korektivní RAG proces**
   - **Technika vyvolávání:** Cestovní agent formuluje nové vyhledávací dotazy na základě zpětné vazby uživatele.
     - Příklad:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Nástroj:** Cestovní agent používá algoritmy k řazení a filtrování nových výsledků vyhledávání s důrazem na relevanci podle zpětné vazby uživatele.
     - Příklad:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Vyhodnocení:** Cestovní agent průběžně hodnotí relevanci a přesnost svých doporučení analýzou zpětné vazby uživatele a provádí potřebné úpravy.
     - Příklad:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktický příklad

Zde je zjednodušený příklad Python kódu začleňujícího korektivní RAG přístup v Cestovním agentovi:

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

# Příklad použití
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

### Pre-emptivní načítání kontextu


Pre-emptive Context Load zahrnuje načtení relevantního kontextu nebo pozadí do modelu před zpracováním dotazu. To znamená, že model má k této informaci přístup od začátku, což mu může pomoci generovat informovanější odpovědi, aniž by během procesu musel získávat další data.

Zde je zjednodušený příklad, jak by mohlo vypadat pre-emptivní načtení kontextu pro aplikaci cestovní kanceláře v Pythonu:

```python
class TravelAgent:
    def __init__(self):
        # Přednačíst oblíbené destinace a jejich informace
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Získat informace o destinaci z přednačteného kontextu
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Příklad použití
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Vysvětlení

1. **Inicializace (metoda `__init__`)**: Třída `TravelAgent` přednačítá slovník obsahující informace o populárních destinacích, jako jsou Paříž, Tokio, New York a Sydney. Tento slovník obsahuje detaily jako země, měna, jazyk a hlavní atrakce pro každou destinaci.

2. **Získávání informací (metoda `get_destination_info`)**: Když uživatel dotazuje informace o konkrétní destinaci, metoda `get_destination_info` načte relevantní informace ze přednačteného slovníku kontextu.

Přednačtením kontextu může aplikace cestovní kanceláře rychle reagovat na uživatelské dotazy bez nutnosti získávat tyto informace z externího zdroje v reálném čase. To činí aplikaci efektivnější a responzivnější.

### Inicializace plánu s cílem před iterací

Inicializace plánu s cílem zahrnuje nastartování s jasným cílem nebo požadovaným výsledkem na mysli. Definováním tohoto cíle předem může model používat tento cíl jako vodítko během celého iterativního procesu. To pomáhá zajistit, že každá iterace vede blíže k dosažení požadovaného výsledku, čímž se proces stává efektivnější a zaměřenější.

Zde je příklad, jak můžete inicializovat cestovní plán s cílem před iterací pro cestovní kancelář v Pythonu:

### Scénář

Cestovní agent chce naplánovat na míru šitou dovolenou pro klienta. Cílem je vytvořit itinerář cestování, který maximalizuje spokojenost klienta na základě jeho preferencí a rozpočtu.

### Kroky

1. Definujte preference a rozpočet klienta.
2. Inicializujte počáteční plán na základě těchto preferencí.
3. Iterujte, abyste plán upřesnili a optimalizovali spokojenost klienta.

#### Pythonový kód

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

# Příklad použití
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

#### Vysvětlení kódu

1. **Inicializace (metoda `__init__`)**: Třída `TravelAgent` je inicializována s listem potenciálních destinací, z nichž každá má atributy jako název, cena a typ aktivity.

2. **Inicializace plánu (metoda `bootstrap_plan`)**: Tato metoda vytvoří počáteční cestovní plán na základě preferencí a rozpočtu klienta. Prochází seznam destinací a přidává je do plánu, pokud odpovídají preferencím klienta a zapadají do rozpočtu.

3. **Kontrola shody preferencí (metoda `match_preferences`)**: Tato metoda kontroluje, zda destinace odpovídá preferencím klienta.

4. **Iterace plánu (metoda `iterate_plan`)**: Tato metoda upřesňuje počáteční plán tím, že se snaží nahradit každou destinaci v plánu lepší volbou s ohledem na preference klienta a omezení rozpočtu.

5. **Výpočet nákladů (metoda `calculate_cost`)**: Tato metoda vypočítá celkové náklady aktuálního plánu včetně potenciálně nové destinace.

#### Ukázkové použití

- **Počáteční plán**: Cestovní agent vytvoří počáteční plán na základě klientových preferencí pro prohlídky památek a rozpočtu 2000 dolarů.
- **Upřesněný plán**: Cestovní agent iteruje plán a optimalizuje ho podle preferencí a rozpočtu klienta.

Inicializací plánu s jasným cílem (např. maximalizace spokojenosti klienta) a iterací pro jeho upřesnění může cestovní agent vytvořit na míru šitý a optimalizovaný cestovní itinerář pro klienta. Tento přístup zajišťuje, že cestovní plán odpovídá klientovým preferencím a rozpočtu od začátku a s každou iterací se zlepšuje.

### Využití LLM pro přeřazování a skórování

Velké jazykové modely (LLM) lze použít pro přeřazování a skórování hodnocením relevance a kvality získaných dokumentů nebo generovaných odpovědí. Funguje to takto:

**Získání:** Počáteční krok získá sadu kandidátních dokumentů nebo odpovědí na základě dotazu.

**Přeřazování:** LLM hodnotí tyto kandidáty a přeřadí je podle jejich relevance a kvality. Tento krok zajišťuje, že nejvíce relevantní a kvalitní informace jsou prezentovány první.

**Skórování:** LLM přiděluje skóre každému kandidátovi, které odráží jejich relevanci a kvalitu. To pomáhá vybrat nejlepší odpověď nebo dokument pro uživatele.

Využitím LLM pro přeřazování a skórování může systém poskytovat přesnější a kontextově relevantnější informace, čímž se zlepšuje celkový uživatelský zážitek.

Zde je příklad, jak může cestovní agent použít velký jazykový model (LLM) k přeřazování a skórování cestovních destinací na základě preferencí uživatele v Pythonu:

#### Scénář – Cestování na základě preferencí

Cestovní agent chce doporučit nejlepší cestovní destinace klientovi na základě jeho preferencí. LLM pomůže přeřadit a ohodnotit destinace, aby se zajistilo předložení nejrelevantnějších možností.

#### Kroky:

1. Shromáždit uživatelské preference.
2. Získat seznam potenciálních cestovních destinací.
3. Použít LLM k přeřazení a skórování destinací podle uživatelských preferencí.

Zde je, jak můžete aktualizovat předchozí příklad na využití služeb Azure OpenAI:

#### Požadavky

1. Musíte mít předplatné Azure.
2. Vytvořit Azure OpenAI zdroj a získat svůj API klíč.

#### Ukázkový Python kód

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Vygenerujte prompt pro Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definujte hlavičky a obsah požadavku
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Zavolejte Azure OpenAI API pro získání přeřazených a ohodnocených destinací
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extrahujte a vraťte doporučení
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

# Příklad použití
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

#### Vysvětlení kódu – Preference Booker

1. **Inicializace**: Třída `TravelAgent` je inicializována s listem potenciálních cestovních destinací, z nichž každá má atributy jako název a popis.

2. **Získání doporučení (metoda `get_recommendations`)**: Tato metoda generuje prompt pro službu Azure OpenAI na základě uživatelských preferencí a provádí HTTP POST požadavek na Azure OpenAI API, aby získala přeřazené a ohodnocené destinace.

3. **Generování promptu (metoda `generate_prompt`)**: Tato metoda sestavuje prompt pro Azure OpenAI, včetně uživatelských preferencí a seznamu destinací. Prompt vede model k přeřazení a skórování destinací na základě poskytnutých preferencí.

4. **Volání API**: Knihovna `requests` je použita k provedení HTTP POST požadavku na koncový bod Azure OpenAI API. Odpověď obsahuje přeřazené a ohodnocené destinace.

5. **Ukázkové použití**: Cestovní agent shromažďuje uživatelské preference (např. zájem o památky a rozmanitou kulturu) a používá službu Azure OpenAI k získání přeřazených a ohodnocených doporučení pro cestovní destinace.

Ujistěte se, že nahradíte `your_azure_openai_api_key` skutečným API klíčem Azure OpenAI a `https://your-endpoint.com/...` skutečnou URL adresou end-pointu vaší Azure OpenAI služby.

Využitím LLM pro přeřazování a skórování může cestovní agent poskytovat personalizovanější a relevantnější cestovní doporučení klientům, čímž zlepší jejich celkový zážitek.

### RAG: technika promptování vs nástroj

Retrieval-Augmented Generation (RAG) může být jak technikou promptování, tak nástrojem při vývoji AI agentů. Pochopení rozdílu mezi nimi vám pomůže efektivněji využívat RAG ve vašich projektech.

#### RAG jako technika promptování

**Co to je?**

- Jako technika promptování RAG zahrnuje formulování specifických dotazů nebo promptů k usměrnění získávání relevantních informací z velkého korpusu nebo databáze. Tyto informace se pak používají k vytváření odpovědí nebo akcí.

**Jak to funguje:**

1. **Formulace promptů**: Vytvořit dobře strukturované prompty nebo dotazy na základě aktuální úlohy nebo vstupu uživatele.
2. **Získávání informací**: Použít prompty k vyhledávání relevantních dat z předem existující znalostní databáze nebo datasetu.
3. **Generování odpovědi**: Kombinovat získané informace s generativními AI modely k vytvoření komplexní a koherentní odpovědi.

**Příklad v cestovní agentuře**:

- Uživatelský vstup: "Chci navštívit muzea v Paříži."
- Prompt: "Najdi nejlepší muzea v Paříži."
- Získané informace: Detaily o Louvru, Musée d'Orsay atd.
- Vygenerovaná odpověď: "Zde jsou některá nejlepší muzea v Paříži: Louvre, Musée d'Orsay a Centre Pompidou."

#### RAG jako nástroj

**Co to je?**

- Jako nástroj je RAG integrovaný systém, který automatizuje proces získávání a generování, což vývojářům usnadňuje implementaci složitých AI funkcionalit bez nutnosti ručně vytvářet prompty pro každý dotaz.

**Jak to funguje:**

1. **Integrace**: RAG je zabudován do architektury AI agenta a umožňuje automaticky zvládat úlohy získávání a generování.
2. **Automatizace**: Nástroj řídí celý proces, od příjmu uživatelského vstupu po vytvoření konečné odpovědi, bez nutnosti explicitních promptů pro každý krok.
3. **Efektivita**: Zlepšuje výkon agenta tím, že zjednodušuje proces získávání a generování, což umožňuje rychlejší a přesnější odpovědi.

**Příklad v cestovní agentuře**:

- Uživatelský vstup: "Chci navštívit muzea v Paříži."
- Nástroj RAG: Automaticky vyhledá informace o muzeích a vytvoří odpověď.
- Vygenerovaná odpověď: "Zde jsou některá nejlepší muzea v Paříži: Louvre, Musée d'Orsay a Centre Pompidou."

### Porovnání

| Aspekt                 | Technika promptování                                        | Nástroj                                                |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Manuální vs Automatické**| Manuální formulace promptů pro každý dotaz.              | Automatizovaný proces získávání a generování.          |
| **Kontrola**            | Nabízí větší kontrolu nad procesem získávání.               | Zjednodušuje a automatizuje získávání a generování.    |
| **Flexibilita**         | Umožňuje přizpůsobené prompty podle specifických potřeb.    | Efektivnější pro velké implementace.                   |
| **Složitost**            | Vyžaduje tvorbu a ladění promptů.                          | Snazší integrace do architektury AI agenta.            |

### Praktické příklady

**Příklad techniky promptování:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Příklad nástroje:**

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

### Hodnocení relevance

Hodnocení relevance je klíčovým aspektem výkonu AI agenta. Zajišťuje, že informace získané a generované agentem jsou vhodné, přesné a užitečné pro uživatele. Pojďme prozkoumat, jak hodnotit relevanci u AI agentů, včetně praktických příkladů a technik.

#### Klíčové koncepty hodnocení relevance

1. **Povědomí o kontextu**:
   - Agent musí rozumět kontextu uživatelského dotazu, aby získal a generoval relevantní informace.
   - Příklad: Pokud uživatel žádá o "nejlepší restaurace v Paříži", agent by měl vzít v úvahu uživatelské preference, například typ kuchyně a rozpočet.

2. **Přesnost**:
   - Informace poskytnuté agentem by měly být fakticky správné a aktuální.
   - Příklad: Doporučit aktuálně otevřené restaurace s dobrými recenzemi namísto zastaralých nebo zavřených možností.

3. **Záměr uživatele**:
   - Agent by měl odhadnout záměr uživatele za dotazem, aby poskytl co nejrelevantnější informace.
   - Příklad: Pokud uživatel žádá o "hotely s příznivou cenou", agent by měl upřednostnit cenově dostupné možnosti.

4. **Smyčka zpětné vazby**:
   - Neustálé sbírání a analýza uživatelské zpětné vazby pomáhá agentu zlepšovat proces hodnocení relevance.
   - Příklad: Zahrnuj uživatelská hodnocení a zpětnou vazbu k předchozím doporučením pro zlepšení budoucích odpovědí.

#### Praktické techniky hodnocení relevance

1. **Skórování relevance**:
   - Přidělit skóre relevance každé získané položce na základě toho, jak dobře odpovídá uživatelskému dotazu a preferencím.
   - Příklad:

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

2. **Filtrování a řazení**:
   - Odfiltrovat nerelevantní položky a seřadit zbývající podle jejich skóre relevance.
   - Příklad:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Vrátit 10 nejrelevantnějších položek
     ```

3. **Zpracování přirozeného jazyka (NLP)**:
   - Použít NLP techniky k pochopení uživatelského dotazu a získání relevantních informací.
   - Příklad:

     ```python
     def process_query(query):
         # Použijte NLP pro extrakci klíčových informací z dotazu uživatele
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrace uživatelské zpětné vazby**:
   - Sbírat zpětnou vazbu od uživatelů o poskytnutých doporučeních a využívat ji k úpravě budoucího hodnocení relevance.
   - Příklad:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Příklad: Hodnocení relevance v cestovní agentuře

Zde je praktický příklad, jak může cestovní agent hodnotit relevanci cestovních doporučení:

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
        return ranked_items[:10]  # Vrátit 10 nejrelevantnějších položek

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

# Příklad použití
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

### Vyhledávání se záměrem

Vyhledávání se záměrem zahrnuje pochopení a interpretaci základního účelu nebo cíle uživatelova dotazu k získání a generování co nejrelevantnějších a nejužitečnějších informací. Tento přístup jde nad rámec pouhého porovnávání klíčových slov a zaměřuje se na pochopení skutečných potřeb a kontextu uživatele.

#### Klíčové koncepty vyhledávání se záměrem

1. **Pochopení záměru uživatele**:
   - Záměr uživatele lze rozdělit do tří hlavních typů: informační, navigační a transakční.
     - **Informační záměr**: Uživatel hledá informace o nějakém tématu (např. "Jaká jsou nejlepší muzea v Paříži?").
     - **Navigační záměr**: Uživatel chce přejít na konkrétní web nebo stránku (např. "Oficiální web Louvre").
     - **Transakční záměr**: Uživatel chce provést nějakou transakci, například rezervovat let nebo uskutečnit nákup (např. "Rezervovat letenku do Paříže").

2. **Povědomí o kontextu**:
   - Analýza kontextu uživatelského dotazu pomáhá přesně identifikovat jeho záměr. Zahrnuje zohlednění předchozích interakcí, uživatelských preferencí a konkrétních detailů aktuálního dotazu.

3. **Zpracování přirozeného jazyka (NLP)**:
   - NLP techniky se používají k pochopení a interpretaci přirozených jazykových dotazů uživatelů. Zahrnuje úlohy jako rozpoznávání entit, analýzu sentimentu a parsování dotazů.

4. **Personalizace**:
   - Personalizace výsledků vyhledávání na základě historie uživatele, preferencí a zpětné vazby zvyšuje relevanci získaných informací.

#### Praktický příklad: Vyhledávání se záměrem v cestovní agentuře

Podívejme se na cestovního agenta jako příklad, jak může být vyhledávání se záměrem implementováno.

1. **Shromáždění uživatelských preferencí**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Pochopení záměru uživatele**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Povědomí o kontextu**


   ```python
   def analyze_context(query, user_history):
       # Kombinujte aktuální dotaz s historií uživatele pro pochopení kontextu
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Vyhledávání a personalizace výsledků**

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
       # Příklad vyhledávací logiky pro informační záměr
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Příklad vyhledávací logiky pro navigační záměr
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Příklad vyhledávací logiky pro transakční záměr
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Příklad personalizační logiky
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Vrátit 10 nejlepších personalizovaných výsledků
   ```

5. **Příklad použití**

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

## 4. Generování kódu jako nástroje

Agenti generující kód používají AI modely k psaní a vykonávání kódu, řeší složité problémy a automatizují úkoly.

### Agenti generující kód

Agenti generující kód používají generativní AI modely k psaní a vykonávání kódu. Tito agenti mohou řešit složité problémy, automatizovat úkoly a poskytovat cenné poznatky generováním a spouštěním kódu v různých programovacích jazycích.

#### Praktické aplikace

1. **Automatizované generování kódu**: Generování útržků kódu pro specifické úkoly, jako je analýza dat, web scraping nebo strojové učení.
2. **SQL jako RAG**: Použití SQL dotazů k načítání a manipulaci s daty z databází.
3. **Řešení problémů**: Vytváření a spouštění kódu k řešení konkrétních problémů, například optimalizace algoritmů nebo analýzy dat.

#### Příklad: Agent generující kód pro analýzu dat

Představte si, že navrhujete agenta generujícího kód. Takto by mohl fungovat:

1. **Úkol**: Analyzovat dataset k identifikaci trendů a vzorců.
2. **Kroky**:
   - Načíst dataset do nástroje pro analýzu dat.
   - Generovat SQL dotazy pro filtrování a agregaci dat.
   - Spustit dotazy a získat výsledky.
   - Použít výsledky k vytvoření vizualizací a poznatků.
3. **Potřebné zdroje**: Přístup k datasetu, nástroje pro analýzu dat a možnosti SQL.
4. **Zkušenosti**: Použít výsledky předchozích analýz ke zlepšení přesnosti a relevance budoucích analýz.

### Příklad: Agent generující kód pro cestovní kancelář

V tomto příkladu navrhneme agenta generujícího kód, Cestovní kancelář, který pomůže uživatelům plánovat jejich cestu generováním a spouštěním kódu. Tento agent může řešit úkoly, jako je vyhledávání cestovních možností, filtrování výsledků a sestavování itineráře pomocí generativní AI.

#### Přehled agenta generujícího kód

1. **Sbírání uživatelských preferencí**: Shromažďuje vstupy uživatele, jako jsou cílová destinace, data cesty, rozpočet a zájmy.
2. **Generování kódu pro získání dat**: Generuje útržky kódu pro získání dat o letech, hotelech a atrakcích.
3. **Spouštění generovaného kódu**: Spouští generovaný kód pro získání aktuálních informací.
4. **Generování itineráře**: Sestavuje získaná data do personalizovaného cestovního plánu.
5. **Úpravy na základě zpětné vazby**: Přijímá uživatelskou zpětnou vazbu a podle potřeby znovu generuje kód, aby zpřesnil výsledky.

#### Krok za krokem implementace

1. **Sbírání uživatelských preferencí**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generování kódu pro získání dat**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Příklad: Vygenerujte kód pro hledání letů na základě uživatelských preferencí
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Příklad: Vygenerujte kód pro hledání hotelů
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Spouštění generovaného kódu**

   ```python
   def execute_code(code):
       # Spusťte vygenerovaný kód pomocí exec
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

4. **Generování itineráře**

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

5. **Úpravy na základě zpětné vazby**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Upravte preference na základě zpětné vazby uživatele
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Znovu vygenerujte a spusťte kód s aktualizovanými preferencemi
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Využití povědomí o prostředí a uvažování

Založení na schématu tabulky může skutečně zlepšit proces generování dotazů použitím povědomí o prostředí a uvažování.

Zde je příklad, jak lze toto provést:

1. **Porozumění schématu**: Systém porozumí schématu tabulky a použije tyto informace k zakotvení generování dotazů.
2. **Úprava na základě zpětné vazby**: Systém upraví uživatelské preference na základě zpětné vazby a zváží, která pole ve schématu je třeba aktualizovat.
3. **Generování a spouštění dotazů**: Systém vygeneruje a spustí dotazy k získání aktuálních dat o letech a hotelech na základě nových preferencí.

Zde je aktualizovaný příklad kódu v Pythonu, který tyto koncepty zahrnuje:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Upravit předvolby na základě zpětné vazby uživatele
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Odůvodnění založené na schématu pro úpravu dalších souvisejících předvoleb
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Vlastní logika pro úpravu předvoleb na základě schématu a zpětné vazby
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generovat kód pro získání dat o letech na základě aktualizovaných předvoleb
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generovat kód pro získání dat o hotelech na základě aktualizovaných předvoleb
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulovat spuštění kódu a vrátit ukázková data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Vygenerovat itinerář na základě letů, hotelů a atrakcí
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Příklad schématu
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Příklad použití
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Znovu vygenerovat a spustit kód s aktualizovanými předvolbami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Vysvětlení - Rezervace na základě zpětné vazby

1. **Povědomí o schématu**: Slovník `schema` definuje, jak by měly být preference upraveny na základě zpětné vazby. Zahrnuje pole jako `favorites` a `avoid` s odpovídajícími úpravami.
2. **Úprava preferencí (`adjust_based_on_feedback` metoda)**: Tato metoda upravuje preference na základě uživatelské zpětné vazby a schématu.
3. **Úpravy na základě prostředí (`adjust_based_on_environment` metoda)**: Tato metoda přizpůsobuje úpravy na základě schématu a zpětné vazby.
4. **Generování a spouštění dotazů**: Systém generuje kód k získání aktualizovaných dat o letech a hotelech na základě upravených preferencí a simuluje spuštění těchto dotazů.
5. **Generování itineráře**: Systém vytváří aktualizovaný itinerář na základě nových dat o letech, hotelu a atrakcích.

Tím, že je systém povědomý o prostředí a uvažuje podle schématu, může generovat přesnější a relevantnější dotazy, což vede k lepším doporučením pro cestování a více personalizovanému uživatelskému zážitku.

### Použití SQL jako techniky Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) je výkonný nástroj pro interakci s databázemi. Když je použit jako součást přístupu Retrieval-Augmented Generation (RAG), SQL může načítat relevantní data z databází pro informování a generování odpovědí nebo akcí v AI agentech. Pojďme prozkoumat, jak lze SQL používat jako techniku RAG v kontextu Cestovního agenta.

#### Klíčové koncepty

1. **Interakce s databází**:
   - SQL se používá k dotazování databází, načítání relevantních informací a manipulaci s daty.
   - Příklad: Získání údajů o letech, hotelech a atrakcích z cestovní databáze.

2. **Integrace s RAG**:
   - SQL dotazy jsou generovány na základě vstupu a preferencí uživatele.
   - Načtená data jsou pak využita k vytváření personalizovaných doporučení nebo akcí.

3. **Dynamické generování dotazů**:
   - AI agent generuje dynamické SQL dotazy na základě kontextu a potřeb uživatele.
   - Příklad: Přizpůsobení SQL dotazů pro filtrování výsledků na základě rozpočtu, dat a zájmů.

#### Aplikace

- **Automatizované generování kódu**: Generování útržků kódu pro specifické úkoly.
- **SQL jako RAG**: Použití SQL dotazů k manipulaci s daty.
- **Řešení problémů**: Vytváření a spouštění kódu k řešení problémů.

**Příklad**:
Agent pro analýzu dat:

1. **Úkol**: Analyzovat dataset pro nalezení trendů.
2. **Kroky**:
   - Načíst dataset.
   - Generovat SQL dotazy pro filtrování dat.
   - Spustit dotazy a získat výsledky.
   - Generovat vizualizace a poznatky.
3. **Zdroje**: Přístup k datasetu, možnosti SQL.
4. **Zkušenosti**: Použít předchozí výsledky ke zlepšení budoucích analýz.

#### Praktický příklad: Použití SQL v Cestovním agentovi

1. **Sbírání uživatelských preferencí**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generování SQL dotazů**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Spouštění SQL dotazů**

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

4. **Generování doporučení**

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

#### Příklad SQL dotazů

1. **Dotaz na lety**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Dotaz na hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Dotaz na atrakce**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Využitím SQL jako části techniky Retrieval-Augmented Generation (RAG) mohou AI agenti jako Cestovní agent dynamicky načítat a využívat relevantní data k poskytování přesných a personalizovaných doporučení.

### Příklad metakognice

Pro demonstraci implementace metakognice vytvořme jednoduchého agenta, který *reflektuje svůj proces rozhodování* při řešení problému. Pro tento příklad sestavíme systém, kde se agent snaží optimalizovat výběr hotelu, ale následně vyhodnotí své vlastní uvažování a upraví strategii, když dělá chyby nebo suboptimální volby.

Tento proces simulujeme na základním příkladu, kde agent vybírá hotely na základě kombinace ceny a kvality, ale "reflektuje" svá rozhodnutí a podle toho se přizpůsobuje.

#### Jak toto ilustruje metakognici:

1. **Počáteční rozhodnutí**: Agent vybere nejlevnější hotel, aniž by chápal dopad kvality.
2. **Reflexe a vyhodnocení**: Po počáteční volbě agent zkontroluje, zda hotel nebyl "špatná" volba pomocí zpětné vazby uživatele. Pokud zjistí, že kvalita hotelu byla příliš nízká, reflektuje své uvažování.
3. **Úprava strategie**: Agent upraví strategii na základě reflexe a přepne se z "nejlevnějšího" na "nejkvalitnějšího", čímž zlepšuje svůj proces rozhodování v budoucích iteracích.

Zde je příklad:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Ukládá dříve vybrané hotely
        self.corrected_choices = []  # Ukládá opravené volby
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Dostupné strategie

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
        # Předpokládejme, že máme zpětnou vazbu od uživatele, která nám říká, zda byla poslední volba dobrá nebo ne
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Upravte strategii, pokud byla předchozí volba neuspokojivá
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

# Simulujte seznam hotelů (cena a kvalita)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Vytvořte agenta
agent = HotelRecommendationAgent()

# Krok 1: Agent doporučí hotel pomocí strategie "nejlevnější"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Krok 2: Agent zhodnotí volbu a případně upraví strategii
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Krok 3: Agent opět doporučí, tentokrát pomocí upravené strategie
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Schopnosti metakognice agentů

Klíčové je zde, že agent:
- Vyhodnocuje svá předchozí rozhodnutí a proces rozhodování.
- Přizpůsobuje strategii na základě této reflexe, tedy metakognice v akci.

Toto je jednoduchá forma metakognice, kdy je systém schopen upravovat svůj proces uvažování na základě interní zpětné vazby.

### Závěr

Metakognice je silný nástroj, který může výrazně zlepšit schopnosti AI agentů. Začleněním metakognitivních procesů můžete navrhnout agenty, kteří jsou inteligentnější, adaptabilnější a efektivnější. Využijte další zdroje k dalšímu poznání fascinujícího světa metakognice v AI agentech.

### Máte další otázky týkající se návrhového vzoru metakognice?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde potkáte další studenty, můžete navštívit konzultační hodiny a získat odpovědi na své otázky o AI agentech.

## Předchozí lekce

[Návrhový vzor vícero agentů](../08-multi-agent/README.md)

## Následující lekce

[AI agenti v produkci](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->