<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T20:18:38+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "cs"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.cs.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_
# Metakognice u AI agentů

## Úvod

Vítejte v lekci o metakognici u AI agentů! Tato kapitola je určena pro začátečníky, kteří se zajímají o to, jak mohou AI agenti přemýšlet o svých vlastních myšlenkových procesech. Na konci této lekce pochopíte klíčové koncepty a získáte praktické příklady, jak aplikovat metakognici při návrhu AI agentů.

## Cíle učení

Po dokončení této lekce budete schopni:

1. Pochopit důsledky smyček uvažování v definicích agentů.
2. Používat plánovací a hodnotící techniky k podpoře agentů, kteří se sami opravují.
3. Vytvořit vlastní agenty schopné manipulovat s kódem k dosažení úkolů.

## Úvod do metakognice

Metakognice označuje vyšší kognitivní procesy, které zahrnují přemýšlení o vlastním myšlení. U AI agentů to znamená schopnost hodnotit a upravovat své akce na základě sebeuvědomění a minulých zkušeností. Metakognice, neboli „přemýšlení o přemýšlení“, je důležitým konceptem při vývoji agentních AI systémů. Zahrnuje schopnost AI systémů být si vědomi svých vlastních interních procesů a schopnost monitorovat, regulovat a přizpůsobovat své chování. Podobně jako my, když „čteme situaci“ nebo řešíme problém. Toto sebeuvědomění může pomoci AI systémům dělat lepší rozhodnutí, identifikovat chyby a zlepšovat svůj výkon v průběhu času – což opět souvisí s Turingovým testem a debatou o tom, zda AI převezme kontrolu.

V kontextu agentních AI systémů může metakognice pomoci řešit několik výzev, jako jsou:
- Transparentnost: Zajištění, že AI systémy dokážou vysvětlit své uvažování a rozhodnutí.
- Uvažování: Zlepšení schopnosti AI systémů syntetizovat informace a činit správná rozhodnutí.
- Adaptace: Umožnění AI systémům přizpůsobit se novým prostředím a měnícím se podmínkám.
- Vnímání: Zlepšení přesnosti AI systémů při rozpoznávání a interpretaci dat z jejich prostředí.

### Co je metakognice?

Metakognice, neboli „přemýšlení o přemýšlení“, je vyšší kognitivní proces, který zahrnuje sebeuvědomění a seberegulaci vlastních kognitivních procesů. V oblasti AI metakognice umožňuje agentům hodnotit a přizpůsobovat své strategie a akce, což vede ke zlepšení schopností řešení problémů a rozhodování. Pochopením metakognice můžete navrhnout AI agenty, kteří jsou nejen inteligentnější, ale také přizpůsobivější a efektivnější. U skutečné metakognice by AI explicitně uvažovala o svém vlastním uvažování.

Příklad: „Upřednostnil jsem levnější lety, protože… možná mi unikají přímé lety, takže to znovu zkontroluji.“
Sledování, jak nebo proč si zvolila určitou trasu.
- Poznání, že udělala chybu, protože se příliš spoléhala na uživatelské preference z minula, a proto upravuje svou strategii rozhodování, nejen konečné doporučení.
- Diagnostika vzorců, jako například: „Kdykoli uživatel zmíní ‚příliš přeplněné‘, neměl bych jen odstranit určité atrakce, ale také přehodnotit svou metodu výběru ‚nejlepších atrakcí‘, pokud vždy řadím podle popularity.“

### Důležitost metakognice u AI agentů

Metakognice hraje klíčovou roli při návrhu AI agentů z několika důvodů:

![Důležitost metakognice](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.cs.png)

- Sebereflexe: Agenti mohou hodnotit svůj vlastní výkon a identifikovat oblasti ke zlepšení.
- Přizpůsobivost: Agenti mohou upravovat své strategie na základě minulých zkušeností a měnících se podmínek.
- Oprava chyb: Agenti mohou autonomně detekovat a opravovat chyby, což vede k přesnějším výsledkům.
- Správa zdrojů: Agenti mohou optimalizovat využití zdrojů, jako je čas a výpočetní výkon, plánováním a hodnocením svých akcí.

## Komponenty AI agenta

Než se ponoříme do metakognitivních procesů, je důležité pochopit základní komponenty AI agenta. AI agent se obvykle skládá z:

- Persona: Osobnost a charakteristiky agenta, které definují, jak interaguje s uživateli.
- Nástroje: Schopnosti a funkce, které agent může vykonávat.
- Dovednosti: Znalosti a odborné schopnosti, které agent má.

Tyto komponenty spolupracují na vytvoření „jednotky odbornosti“, která dokáže vykonávat specifické úkoly.

**Příklad**:
Představte si cestovního agenta, který nejen plánuje vaši dovolenou, ale také upravuje svůj postup na základě dat v reálném čase a zkušeností z předchozích zákaznických cest.

### Příklad: Metakognice u služby cestovního agenta

Představte si, že navrhujete službu cestovního agenta poháněnou AI. Tento agent, „Cestovní agent“, pomáhá uživatelům s plánováním jejich dovolené. Aby zahrnoval metakognici, Cestovní agent musí hodnotit a upravovat své akce na základě sebeuvědomění a minulých zkušeností. Zde je, jak by mohla metakognice hrát roli:

#### Aktuální úkol

Aktuálním úkolem je pomoci uživateli naplánovat výlet do Paříže.

#### Kroky k dokončení úkolu

1. **Shromáždění uživatelských preferencí**: Zeptat se uživatele na jeho cestovní data, rozpočet, zájmy (např. muzea, kuchyně, nakupování) a jakékoli specifické požadavky.
2. **Získání informací**: Vyhledat možnosti letů, ubytování, atrakcí a restaurací, které odpovídají uživatelským preferencím.
3. **Generování doporučení**: Poskytnout personalizovaný itinerář s detaily letů, rezervacemi hotelů a navrhovanými aktivitami.
4. **Úprava na základě zpětné vazby**: Požádat uživatele o zpětnou vazbu k doporučením a provést potřebné úpravy.

#### Požadované zdroje

- Přístup k databázím letů a hotelů.
- Informace o pařížských atrakcích a restauracích.
- Data o zpětné vazbě od uživatelů z předchozích interakcí.

#### Zkušenosti a sebereflexe

Cestovní agent využívá metakognici k hodnocení svého výkonu a učení se z minulých zkušeností. Například:

1. **Analýza zpětné vazby uživatelů**: Cestovní agent přezkoumává zpětnou vazbu uživatelů, aby zjistil, která doporučení byla dobře přijata a která ne. Podle toho upravuje svá budoucí doporučení.
2. **Přizpůsobivost**: Pokud uživatel dříve zmínil, že nemá rád přeplněná místa, Cestovní agent se v budoucnu vyhne doporučování populárních turistických míst během špičky.
3. **Oprava chyb**: Pokud Cestovní agent v minulosti udělal chybu, například doporučil hotel, který byl plně obsazen, naučí se důkladněji kontrolovat dostupnost před doporučením.

#### Praktický příklad pro vývojáře

Zde je zjednodušený příklad, jak by mohl vypadat kód Cestovního agenta při zahrnutí metakognice:

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

#### Proč je metakognice důležitá

- **Sebereflexe**: Agenti mohou analyzovat svůj výkon a identifikovat oblasti ke zlepšení.
- **Přizpůsobivost**: Agenti mohou upravovat strategie na základě zpětné vazby a měnících se podmínek.
- **Oprava chyb**: Agenti mohou autonomně detekovat a opravovat chyby.
- **Správa zdrojů**: Agenti mohou optimalizovat využití zdrojů, jako je čas a výpočetní výkon.

Zahrnutím metakognice může Cestovní agent poskytovat personalizovanější a přesnější cestovní doporučení, čímž zlepšuje celkový uživatelský zážitek.

---

## 2. Plánování u agentů

Plánování je klíčovou součástí chování AI agentů. Zahrnuje stanovení kroků potřebných k dosažení cíle s ohledem na aktuální stav, zdroje a možné překážky.

### Prvky plánování

- **Aktuální úkol**: Jasně definovat úkol.
- **Kroky k dokončení úkolu**: Rozdělit úkol na zvládnutelné kroky.
- **Požadované zdroje**: Identifikovat potřebné zdroje.
- **Zkušenosti**: Využít minulé zkušenosti k informování plánování.

**Příklad**:
Zde jsou kroky, které musí Cestovní agent podniknout, aby efektivně pomohl uživateli naplánovat jeho cestu:

### Kroky pro Cestovního agenta

1. **Shromáždění uživatelských preferencí**
   - Zeptat se uživatele na detaily o jeho cestovních datech, rozpočtu, zájmech a jakýchkoli specifických požadavcích.
   - Příklady: „Kdy plánujete cestovat?“ „Jaký je váš rozpočtový rozsah?“ „Jaké aktivity si na dovolené užíváte?“

2. **Získání informací**
   - Vyhledat relevantní cestovní možnosti na základě uživatelských preferencí.
   - **Lety**: Vyhledat dostupné lety v rámci uživatelova rozpočtu a preferovaných cestovních dat.
   - **Ubytování**: Najít hotely nebo pronájmy, které odpovídají uživatelským preferencím ohledně lokality, ceny a vybavení.
   - **Atrakce a restaurace**: Identifikovat populární atrakce, aktivity a možnosti stravování, které odpovídají uživatelským zájmům.

3. **Generování doporučení**
   - Sestavit získané informace do personalizovaného itineráře.
   - Poskytnout detaily, jako jsou možnosti letů, rezervace hotelů a navrhované aktivity, přičemž doporučení přizpůsobit uživatelským preferencím.

4. **Předložení itineráře uživateli**
   - Sdílet navrhovaný itinerář s uživatelem k jeho přezkoumání.
   - Příklad: „Zde je navrhovaný itinerář pro vaši cestu do Paříže. Obsahuje detaily letů, rezervace hotelů a seznam doporučených aktivit a restaurací. Dejte mi vědět, co si o tom myslíte!“

5. **Shromáždění zpětné vazby**
   - Požádat uživatele o zpětnou vazbu k navrhovanému itineráři.
   - Příklady: „Líbí se vám možnosti letů?“ „Je hotel vhodný pro vaše potřeby?“ „Jsou zde nějaké aktivity, které byste chtěli přidat nebo odstranit?“

6. **Úprava na základě zpětné vazby**
   - Upravit itinerář na základě uživatelské zpětné vazby.
   - Provést potřebné změny v doporučeních letů, ubytování a aktivit, aby lépe odpovídaly uživatelským preferencím.

7. **Konečné potvrzení**
   - Předložit aktualizovaný itinerář uživateli k finálnímu potvrzení.
   - Příklad: „Provedl jsem úpravy na základě vaší zpětné vazby. Zde je aktualizovaný itinerář. Vypadá vše v pořádku?“

8. **Rezervace a potvrzení**
   - Jakmile uživatel schválí itinerář, pokračovat s rezervací letů, ubytování a jakýchkoli předem plánovaných aktivit.
   - Odeslat uživateli detaily potvrzení.

9. **Poskytování průběžné podpory**
   - Zůstat k dispozici pro pomoc uživateli s jakýmikoli změnami nebo dodatečnými požadavky před a během jeho cesty.
   - Příklad: „Pokud budete během své cesty potřebovat další pomoc, neváhejte se na mě kdykoli obrátit!“

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

## 3. Korektivní RAG systém

Nejprve si vysvětleme rozdíl mezi nástrojem RAG a předběžným načítáním kontextu.

![RAG vs načítání kontextu](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.cs.png)

### Retrieval-Augmented Generation (RAG)

RAG kombinuje systém vyhledávání s generativním modelem. Když je zadán dotaz, vyhledávací systém načte relevantní dokumenty nebo data z externího zdroje a tato načtená informace se použije k rozšíření vstupu generativního modelu. To pomáhá modelu generovat přesnější a kontextově relevantní odpovědi.

V systému RAG agent načítá relevantní informace z databáze znalostí a používá je k vytváření vhodných odpovědí nebo akcí.

### Korektivní přístup RAG

Korektivní přístup RAG se zaměřuje na využití technik RAG k opravě chyb a zlepšení přesnosti AI agentů. To zahrnuje:

1. **Technika promptů**: Použití specifických promptů k vedení agenta při načítání relevantních informací.
2. **Nástroj**: Implementace algoritmů a mechanismů, které umožňují agentovi hodnotit relevanci načtených informací a generovat přesné odpovědi.
3. **Hodnocení**: Neustálé hodnocení výkonu agenta a provádění úprav ke zlepšení jeho přesnosti a efektivity.

#### Příklad: Korektivní RAG u vyhledávacího agenta

Představte si vyhledávacího agenta, který načítá informace z webu, aby odpověděl na dotazy uživatelů. Korektivní přístup RAG by mohl zahrnovat:

1. **Technika promptů**: Formulování vyhledávacích dotazů na základě vstupu uživatele.
2. **Nástroj**: Použití algoritmů zpracování přirozeného jazyka a strojového učení k hodnocení a filtrování výsledků vyhledávání.
3. **Hodnocení**: Analýza zpětné vazby uživatelů k identifikaci a opravě nepřesností v načtených informacích.

### Korektivní RAG u Cestovního agenta

Korektivní RAG (Retrieval-Augmented Generation) zlepšuje schopnost AI načítat a generovat informace při opravě nepřesností. Podívejme se, jak může Cestovní agent využít korektivní přístup RAG k poskytování přesnějších a relevantnějších cestovních doporučení.

To zahrnuje:

- **Technika promptů:** Použití specifických promptů k vedení agenta při načítání relevantních informací.
- **Nástroj:** Implementace algoritmů a mechanismů, které umožňují agentovi hodnotit relevanci načtených informací a generovat přesné odpovědi.
- **Hodnocení:** Neustálé hodnocení výkonu agenta a provádění úprav ke zlepšení jeho přesnosti a efektivity.

#### Kroky pro implementaci korektivního RAG u Cestovního agenta

1. **Počáteční interakce s uživatelem**
   - Cestovní agent shromažďuje počáteční preference uživatele, jako je destinace, data cestování, rozpočet a zájmy.
   - Příklad:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Načítání informací**
   - Cestovní agent načítá informace o letech, ubytování, atrakcích a restauracích na základě uživatelských preferencí.
   - Příklad:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generování počátečních doporučení**
   - Cestovní agent používá načtené informace k
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
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Předběžné načtení kontextu

Předběžné načtení kontextu zahrnuje načtení relevantních informací nebo pozadí do modelu ještě před zpracováním dotazu. To znamená, že model má od začátku přístup k těmto informacím, což mu může pomoci generovat informovanější odpovědi, aniž by během procesu musel získávat další data.

Zde je zjednodušený příklad, jak by mohlo vypadat předběžné načtení kontextu pro aplikaci cestovní kanceláře v Pythonu:

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

#### Vysvětlení

1. **Inicializace (metoda `__init__`)**: Třída `TravelAgent` předem načte slovník obsahující informace o oblíbených destinacích, jako jsou Paříž, Tokio, New York a Sydney. Tento slovník zahrnuje detaily, jako je země, měna, jazyk a hlavní atrakce pro každou destinaci.

2. **Získávání informací (metoda `get_destination_info`)**: Když uživatel zadá dotaz na konkrétní destinaci, metoda `get_destination_info` vyhledá relevantní informace z předem načteného slovníku kontextu.

Díky předběžnému načtení kontextu může aplikace cestovní kanceláře rychle reagovat na dotazy uživatelů, aniž by musela v reálném čase získávat tyto informace z externího zdroje. To činí aplikaci efektivnější a pohotovější.

### Zahájení plánu s cílem před iterací

Zahájení plánu s cílem zahrnuje začátek s jasně definovaným cílem nebo požadovaným výsledkem. Definováním tohoto cíle předem může model použít tento cíl jako vodítko během celého iterativního procesu. To pomáhá zajistit, že každá iterace se přibližuje k dosažení požadovaného výsledku, což činí proces efektivnějším a zaměřeným.

Zde je příklad, jak by cestovní kancelář mohla zahájit plánování dovolené s cílem před iterací v Pythonu:

### Scénář

Cestovní kancelář chce naplánovat klientovi dovolenou na míru. Cílem je vytvořit cestovní itinerář, který maximalizuje spokojenost klienta na základě jeho preferencí a rozpočtu.

### Kroky

1. Definujte klientovy preference a rozpočet.
2. Zahajte počáteční plán na základě těchto preferencí.
3. Iterujte a upravujte plán, optimalizujte spokojenost klienta.

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

#### Vysvětlení kódu

1. **Inicializace (metoda `__init__`)**: Třída `TravelAgent` je inicializována seznamem potenciálních destinací, z nichž každá má atributy jako název, cena a typ aktivity.

2. **Zahájení plánu (metoda `bootstrap_plan`)**: Tato metoda vytvoří počáteční cestovní plán na základě klientových preferencí a rozpočtu. Prochází seznam destinací a přidává je do plánu, pokud odpovídají preferencím klienta a vejdou se do rozpočtu.

3. **Porovnání preferencí (metoda `match_preferences`)**: Tato metoda kontroluje, zda destinace odpovídá preferencím klienta.

4. **Iterace plánu (metoda `iterate_plan`)**: Tato metoda upravuje počáteční plán tím, že se snaží nahradit každou destinaci v plánu lepší volbou, s ohledem na klientovy preference a rozpočtová omezení.

5. **Výpočet nákladů (metoda `calculate_cost`)**: Tato metoda vypočítává celkové náklady aktuálního plánu, včetně potenciální nové destinace.

#### Příklad použití

- **Počáteční plán**: Cestovní kancelář vytvoří počáteční plán na základě klientových preferencí pro památky a rozpočet 2000 USD.
- **Upravený plán**: Cestovní kancelář iteruje plán, optimalizuje ho podle preferencí a rozpočtu klienta.

Zahájením plánu s jasným cílem (např. maximalizace spokojenosti klienta) a iterací za účelem jeho úpravy může cestovní kancelář vytvořit přizpůsobený a optimalizovaný cestovní itinerář pro klienta. Tento přístup zajišťuje, že cestovní plán odpovídá preferencím a rozpočtu klienta od začátku a zlepšuje se s každou iterací.

### Využití LLM pro přeřazování a hodnocení

Velké jazykové modely (LLM) lze využít pro přeřazování a hodnocení tím, že hodnotí relevanci a kvalitu získaných dokumentů nebo generovaných odpovědí. Jak to funguje:

**Získávání informací:** Prvním krokem je získání sady kandidátních dokumentů nebo odpovědí na základě dotazu.

**Přeřazování:** LLM vyhodnotí tyto kandidáty a přeřadí je na základě jejich relevance a kvality. Tento krok zajišťuje, že nejrelevantnější a nejkvalitnější informace jsou prezentovány jako první.

**Hodnocení:** LLM přiřadí skóre každému kandidátovi, které odráží jeho relevanci a kvalitu. To pomáhá vybrat nejlepší odpověď nebo dokument pro uživatele.

Využitím LLM pro přeřazování a hodnocení může systém poskytovat přesnější a kontextově relevantní informace, čímž zlepšuje celkovou uživatelskou zkušenost.

Zde je příklad, jak by cestovní kancelář mohla využít velký jazykový model (LLM) pro přeřazování a hodnocení cestovních destinací na základě preferencí uživatele v Pythonu:

#### Scénář - Cestování podle preferencí

Cestovní kancelář chce doporučit klientovi nejlepší cestovní destinace na základě jeho preferencí. LLM pomůže přeřadit a ohodnotit destinace, aby byly prezentovány nejrelevantnější možnosti.

#### Kroky:

1. Shromážděte uživatelské preference.
2. Získejte seznam potenciálních cestovních destinací.
3. Použijte LLM k přeřazení a ohodnocení destinací na základě uživatelských preferencí.

Zde je aktualizovaný příklad použití Azure OpenAI Services:

#### Požadavky

1. Musíte mít předplatné Azure.
2. Vytvořte zdroj Azure OpenAI a získejte svůj API klíč.

#### Příklad Python kódu

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

#### Vysvětlení kódu - Preference Booker

1. **Inicializace**: Třída `TravelAgent` je inicializována seznamem potenciálních cestovních destinací, z nichž každá má atributy jako název a popis.

2. **Získávání doporučení (metoda `get_recommendations`)**: Tato metoda generuje prompt pro službu Azure OpenAI na základě uživatelských preferencí a provádí HTTP POST požadavek na API Azure OpenAI, aby získala přeřazené a ohodnocené destinace.

3. **Generování promptu (metoda `generate_prompt`)**: Tato metoda sestavuje prompt pro Azure OpenAI, který zahrnuje uživatelské preference a seznam destinací. Prompt vede model k přeřazení a ohodnocení destinací na základě poskytnutých preferencí.

4. **API volání**: Knihovna `requests` se používá k provedení HTTP POST požadavku na koncový bod API Azure OpenAI. Odpověď obsahuje přeřazené a ohodnocené destinace.

5. **Příklad použití**: Cestovní kancelář shromáždí uživatelské preference (např. zájem o památky a rozmanitou kulturu) a použije službu Azure OpenAI k získání přeřazených a ohodnocených doporučení pro cestovní destinace.

Nezapomeňte nahradit `your_azure_openai_api_key` svým skutečným API klíčem Azure OpenAI a `https://your-endpoint.com/...` skutečnou URL koncového bodu vašeho nasazení Azure OpenAI.

Využitím LLM pro přeřazování a hodnocení může cestovní kancelář poskytovat personalizovanější a relevantnější cestovní doporučení klientům, čímž zlepšuje jejich celkovou zkušenost.

### RAG: Technika promptování vs nástroj

Retrieval-Augmented Generation (RAG) může být jak technikou promptování, tak nástrojem při vývoji AI agentů. Porozumění rozdílu mezi těmito dvěma přístupy vám může pomoci efektivněji využít RAG ve vašich projektech.

#### RAG jako technika promptování

**Co to je?**

- Jako technika promptování RAG zahrnuje formulaci specifických dotazů nebo promptů k získání relevantních informací z rozsáhlého korpusu nebo databáze. Tyto informace se pak používají k generování odpovědí nebo akcí.

**Jak to funguje:**

1. **Formulace promptů**: Vytvořte dobře strukturované prompty nebo dotazy na základě daného úkolu nebo vstupu uživatele.
2. **Získávání informací**: Použijte prompty k vyhledání relevantních dat z předem existující znalostní báze nebo datové sady.
3. **Generování odpovědi**: Kombinujte získané informace s generativními AI modely k vytvoření komplexní a koherentní odpovědi.

**Příklad v cestovní kanceláři**:

- Uživatelský vstup: "Chci navštívit muzea v Paříži."
- Prompt: "Najdi nejlepší muzea v Paříži."
- Získané informace: Detaily o Louvre, Musée d'Orsay atd.
- Generovaná odpověď: "Zde jsou nejlepší muzea v Paříži: Louvre, Musée d'Orsay a Centre Pompidou."

#### RAG jako nástroj

**Co to je?**

- Jako nástroj je RAG integrovaný systém, který automatizuje proces získávání a generování, což usnadňuje vývojářům implementaci složitých AI funkcí bez nutnosti ručně vytvářet prompty pro každý dotaz.

**Jak to funguje:**

1. **Integrace**: Vložte RAG do architektury AI agenta, což mu umožní automaticky zpracovávat úkoly získávání a generování.
2. **Automatizace**: Nástroj spravuje celý proces, od přijetí uživatelského vstupu po generování konečné odpovědi, bez nutnosti explicitních promptů pro každý krok.
3. **Efektivita**: Zvyšuje výkon agenta tím, že zjednodušuje proces získávání a generování, což umožňuje rychlejší a přesnější odpovědi.

**Příklad v cestovní kanceláři**:

- Uživatelský vstup: "Chci navštívit muzea v Paříži."
- Nástroj RAG: Automaticky získá informace o muzeích a vygeneruje odpověď.
- Generovaná odpověď: "Zde jsou nejlepší muzea v Paříži: Louvre, Musée d'Orsay a Centre Pompidou."

### Porovnání

| Aspekt                 | Technika promptování                                       | Nástroj                                                  |
|------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| **Ruční vs automatické**| Ruční formulace promptů pro každý dotaz.                   | Automatizovaný proces získávání a generování.             |
| **Kontrola**            | Nabízí větší kontrolu nad procesem získávání.               | Zjednodušuje a automatizuje proces získávání a generování.|
| **Flexibilita**         | Umožňuje přizpůsobené prompty na základě specifických potřeb.| Efektivnější pro implementace ve velkém měřítku.         |
| **Složitost**           | Vyžaduje tvorbu a úpravu promptů.                          | Snadnější integrace do architektury AI agenta.           |

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

Hodnocení relevance je klíčovým aspektem výkonu AI agenta. Zajišťuje, že informace získané a generované agentem jsou vhodné, přesné a užitečné pro uživatele. Pojďme prozkoumat, jak hodnotit relevanci v AI agentech, včetně praktických příkladů a technik.

#### Klíčové koncepty hodnocení relevance

1. **Vědomí kontextu**:
   - Agent musí rozumět kontextu uživatelského dotazu, aby získal a generoval relevantní informace.
   - Příklad: Pokud se uživatel ptá na "nejlepší restaurace v Paříži," agent by měl zohlednit uživatelské preference, jako typ kuchyně a rozpočet.

2. **Přesnost**:
   - Informace poskytované agentem by měly být fakticky správné a aktuální.
   - Příklad: Doporučení aktuálně otevřených restaurací s dobrými recenzemi místo zastaralých nebo zavřených možností.

3. **Záměr uživatele**:
   - Agent by měl odvodit záměr uživatele za dotazem, aby poskytl nejrelevantnější informace.
   - Příklad: Pokud se uživatel ptá na "cenově dostupné hotely," agent by měl upřednostnit dostupné možnosti.

4. **Zpětná vazba**:
   - Nepřetržité shromažďování a analýza zpětné vazby od uživatelů pomáhá agentovi zdokonalovat proces hodnocení relevance.
   - Příklad: Zahrnutí uživatelských hodnocení a zpětné vazby na předchozí doporučení ke zlepšení budoucích odpovědí.

#### Praktické techniky hodnocení relevance

1. **Skórování relevance**:
   - Přiřaďte skóre relevance každé získané položce na základě toho, jak dobře odpovídá uživatelskému dotazu a preferencím.
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
   - Odstraňte nerelevantní položky a seřaďte zbývající na základě jejich skóre relevance.
   - Příklad:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Zpracování přirozeného jazyka (NLP)**:
   - Použijte NLP techniky k pochopení uživatelského dotazu a získání relevantních informací.
   - Příklad:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrace zpětné vazby od uživatelů**:
   - Shromažďujte zpětnou vazbu od uživatelů na poskytnutá doporučení a použijte ji k úpravě budoucího hodnocení relevance.
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

#### Příklad: Hodnocení relevance v cestovní kanceláři

Zde je praktický příklad, jak může cestovní kancelář hodnotit relevanci cestovních doporučení:

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
        return ranked_items[:10]  # Return top 10 relevant items

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Vyhledávání podle záměru

Vyhledávání podle záměru zahrnuje pochopení a interpretaci základního účelu nebo cíle za uživatelským dotazem, aby bylo možné získat a generovat nejrelevantnější a nejužitečnější informace. Tento přístup jde nad rámec pouhého shody klíčových slov a zaměřuje se na pochopení skutečných potřeb a kontextu uživatele.

#### Klíčové koncepty vyhledávání podle záměru

1. **Porozumění záměru uživatele**:
   - Záměr uživatele lze rozdělit do tří hlavních typů: informační, navigační a transakční.
     - **Informační záměr**: Uživatel hledá informace o tématu (např. "Jaká jsou nejlepší muzea v Paříži?").
     - **Navigační záměr**: Uživatel chce přejít na konkrétní web nebo stránku (např. "Oficiální web Louvre").
     - **Transakční záměr**: Uživatel chce provést transakci, jako je rezervace letu nebo nákup (např. "Rezervovat let do Paříže").

2. **Vědomí kontextu**:
   - Analýza kontextu uživatelského dotazu pomáhá přesně identifikovat jeho záměr. To zahrnuje zohlednění předchozích interakcí, uživatelských preferencí a specifických detailů aktuálního dotazu.

3. **Zpracování přirozeného jazyka (NLP)**:
   - NLP techniky se používají k pochopení a interpretaci dotazů v přirozeném jazyce od uživatelů. To zahrnuje úkoly jako rozpoznávání entit, analýza sentimentu a parsování dotazů.

4. **Personalizace**:
   - Personalizace
#### Praktický příklad: Hledání s úmyslem v cestovní agentuře

Podívejme se na příklad cestovní agentury, abychom zjistili, jak lze implementovat hledání s úmyslem.

1. **Shromažďování preferencí uživatele**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Porozumění úmyslu uživatele**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Vědomí kontextu**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Hledání a personalizace výsledků**

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

## 4. Generování kódu jako nástroj

Agenti generující kód využívají AI modely k psaní a spouštění kódu, čímž řeší složité problémy a automatizují úkoly.

### Agenti generující kód

Agenti generující kód využívají generativní AI modely k psaní a spouštění kódu. Tito agenti dokážou řešit složité problémy, automatizovat úkoly a poskytovat cenné poznatky generováním a spouštěním kódu v různých programovacích jazycích.

#### Praktické aplikace

1. **Automatické generování kódu**: Generování úryvků kódu pro specifické úkoly, jako je analýza dat, web scraping nebo strojové učení.
2. **SQL jako RAG**: Použití SQL dotazů k získávání a manipulaci s daty z databází.
3. **Řešení problémů**: Vytváření a spouštění kódu pro řešení konkrétních problémů, jako je optimalizace algoritmů nebo analýza dat.

#### Příklad: Agent generující kód pro analýzu dat

Představte si, že navrhujete agenta generujícího kód. Takto by mohl fungovat:

1. **Úkol**: Analyzovat dataset za účelem identifikace trendů a vzorců.
2. **Kroky**:
   - Načtení datasetu do nástroje pro analýzu dat.
   - Generování SQL dotazů pro filtrování a agregaci dat.
   - Spuštění dotazů a získání výsledků.
   - Použití výsledků k vytvoření vizualizací a poznatků.
3. **Požadované zdroje**: Přístup k datasetu, nástroje pro analýzu dat a schopnosti SQL.
4. **Zkušenosti**: Použití výsledků z předchozích analýz ke zlepšení přesnosti a relevance budoucích analýz.

### Příklad: Agent generující kód pro cestovní agenturu

V tomto příkladu navrhneme agenta generujícího kód, Travel Agent, který pomáhá uživatelům plánovat cestování generováním a spouštěním kódu. Tento agent zvládne úkoly, jako je získávání cestovních možností, filtrování výsledků a sestavování itineráře pomocí generativní AI.

#### Přehled agenta generujícího kód

1. **Shromažďování preferencí uživatele**: Sbírá vstupy uživatele, jako je destinace, data cestování, rozpočet a zájmy.
2. **Generování kódu pro získání dat**: Generuje úryvky kódu pro získání informací o letech, hotelech a atrakcích.
3. **Spouštění generovaného kódu**: Spouští generovaný kód pro získání aktuálních informací.
4. **Generování itineráře**: Sestavuje získaná data do personalizovaného cestovního plánu.
5. **Úpravy na základě zpětné vazby**: Přijímá zpětnou vazbu od uživatele a regeneruje kód, pokud je to nutné, pro zpřesnění výsledků.

#### Implementace krok za krokem

1. **Shromažďování preferencí uživatele**

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

3. **Spouštění generovaného kódu**

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

### Využití povědomí o prostředí a uvažování

Zohlednění schématu tabulky může skutečně zlepšit proces generování dotazů díky využití povědomí o prostředí a uvažování.

Zde je příklad, jak to lze provést:

1. **Porozumění schématu**: Systém porozumí schématu tabulky a použije tyto informace k ukotvení generování dotazů.
2. **Úpravy na základě zpětné vazby**: Systém upraví uživatelské preference na základě zpětné vazby a zváží, které pole ve schématu je třeba aktualizovat.
3. **Generování a spouštění dotazů**: Systém vygeneruje a spustí dotazy pro získání aktualizovaných dat o letech a hotelech na základě nových preferencí.

Zde je aktualizovaný příklad Python kódu, který tyto koncepty zahrnuje:

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

#### Vysvětlení - Rezervace na základě zpětné vazby

1. **Povědomí o schématu**: Slovník `schema` definuje, jak by měly být preference upraveny na základě zpětné vazby. Obsahuje pole jako `favorites` a `avoid` s odpovídajícími úpravami.
2. **Úprava preferencí (metoda `adjust_based_on_feedback`)**: Tato metoda upravuje preference na základě zpětné vazby uživatele a schématu.
3. **Úpravy na základě prostředí (metoda `adjust_based_on_environment`)**: Tato metoda přizpůsobuje úpravy na základě schématu a zpětné vazby.
4. **Generování a spouštění dotazů**: Systém generuje kód pro získání aktualizovaných dat o letech a hotelech na základě upravených preferencí a simuluje provedení těchto dotazů.
5. **Generování itineráře**: Systém vytváří aktualizovaný itinerář na základě nových dat o letech, hotelech a atrakcích.

Díky tomu, že je systém povědomý o prostředí a uvažuje na základě schématu, dokáže generovat přesnější a relevantnější dotazy, což vede k lepším cestovním doporučením a personalizovanějšímu uživatelskému zážitku.

### Použití SQL jako techniky Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) je výkonný nástroj pro práci s databázemi. Pokud je použit jako součást přístupu Retrieval-Augmented Generation (RAG), SQL může získávat relevantní data z databází, aby informoval a generoval odpovědi nebo akce v AI agentech. Podívejme se, jak lze SQL použít jako techniku RAG v kontextu cestovní agentury.

#### Klíčové koncepty

1. **Interakce s databází**:
   - SQL se používá k dotazování databází, získávání relevantních informací a manipulaci s daty.
   - Příklad: Získávání detailů o letech, informací o hotelech a atrakcích z cestovní databáze.

2. **Integrace s RAG**:
   - SQL dotazy jsou generovány na základě vstupů a preferencí uživatele.
   - Získaná data jsou poté použita k vytvoření personalizovaných doporučení nebo akcí.

3. **Dynamické generování dotazů**:
   - AI agent generuje dynamické SQL dotazy na základě kontextu a potřeb uživatele.
   - Příklad: Přizpůsobení SQL dotazů pro filtrování výsledků na základě rozpočtu, dat a zájmů.

#### Aplikace

- **Automatické generování kódu**: Generování úryvků kódu pro specifické úkoly.
- **SQL jako RAG**: Použití SQL dotazů k manipulaci s daty.
- **Řešení problémů**: Vytváření a spouštění kódu pro řešení problémů.

**Příklad**:
Agent pro analýzu dat:

1. **Úkol**: Analyzovat dataset za účelem nalezení trendů.
2. **Kroky**:
   - Načtení datasetu.
   - Generování SQL dotazů pro filtrování dat.
   - Spuštění dotazů a získání výsledků.
   - Generování vizualizací a poznatků.
3. **Zdroje**: Přístup k datasetu, schopnosti SQL.
4. **Zkušenosti**: Použití minulých výsledků ke zlepšení budoucích analýz.

#### Praktický příklad: Použití SQL v cestovní agentuře

1. **Shromažďování preferencí uživatele**

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

2. **Dotaz na hotely**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Dotaz na atrakce**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Využitím SQL jako součásti techniky Retrieval-Augmented Generation (RAG) mohou AI agenti, jako je Travel Agent, dynamicky získávat a využívat relevantní data k poskytování přesných a personalizovaných doporučení.

### Příklad metakognice

Pro demonstraci implementace metakognice vytvoříme jednoduchého agenta, který *reflektuje svůj rozhodovací proces* při řešení problému. V tomto příkladu vytvoříme systém, kde agent optimalizuje výběr hotelu, ale poté vyhodnocuje své vlastní uvažování a upravuje svou strategii, pokud udělá chyby nebo suboptimální volby.

#### Jak to ilustruje metakognici:

1. **Počáteční rozhodnutí**: Agent vybere nejlevnější hotel, aniž by zohlednil kvalitu.
2. **Reflexe a vyhodnocení**: Po počáteční volbě agent zkontroluje, zda byl hotel "špatnou" volbou na základě zpětné vazby uživatele. Pokud zjistí, že kvalita hotelu byla příliš nízká, reflektuje své uvažování.
3. **Úprava strategie**: Agent upraví svou strategii na základě reflexe a přejde z "nejlevnějšího" na "nejkvalitnější", čímž zlepší svůj rozhodovací proces v budoucích iteracích.

Zde je příklad:

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

#### Schopnosti metakognice agenta

Klíčové zde je schopnost agenta:
- Vyhodnotit své předchozí volby a rozhodovací proces.
- Upravit svou strategii na základě této reflexe, tj. metakognice v praxi.

Toto je jednoduchá forma metakognice, kde je systém schopen upravit svůj proces uvažování na základě interní zpětné vazby.

### Závěr

Metakognice je mocný nástroj, který může významně zlepšit schopnosti AI agentů. Začleněním metakognitivních procesů můžete navrhnout agenty, kteří jsou inteligentnější, přizpůsobivější a efektivnější. Využijte další zdroje k dalšímu prozkoumání fascinujícího světa metakognice v AI agentech.

### Máte další otázky ohledně návrhového vzoru metakognice?

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Předchozí lekce

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Další lekce

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.