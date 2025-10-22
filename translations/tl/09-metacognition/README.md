<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T09:41:53+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "tl"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.tl.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_
# Metakognisyon sa mga AI Agent

## Panimula

Maligayang pagdating sa aralin tungkol sa metakognisyon sa mga AI agent! Ang kabanatang ito ay idinisenyo para sa mga baguhan na interesado kung paano nag-iisip ang mga AI agent tungkol sa kanilang sariling proseso ng pag-iisip. Sa pagtatapos ng araling ito, mauunawaan mo ang mga pangunahing konsepto at magkakaroon ka ng mga praktikal na halimbawa upang magamit ang metakognisyon sa disenyo ng AI agent.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, magagawa mong:

1. Maunawaan ang mga implikasyon ng reasoning loops sa mga depinisyon ng agent.
2. Gumamit ng mga teknik sa pagpaplano at pagsusuri upang matulungan ang mga self-correcting agent.
3. Gumawa ng sarili mong mga agent na kayang manipulahin ang code upang maisakatuparan ang mga gawain.

## Panimula sa Metakognisyon

Ang metakognisyon ay tumutukoy sa mas mataas na antas ng proseso ng pag-iisip na kinabibilangan ng pag-iisip tungkol sa sariling pag-iisip. Para sa mga AI agent, nangangahulugan ito ng kakayahang suriin at ayusin ang kanilang mga aksyon batay sa kamalayan sa sarili at mga nakaraang karanasan. Ang metakognisyon, o "pag-iisip tungkol sa pag-iisip," ay isang mahalagang konsepto sa pagbuo ng mga agentic AI system. Kasama rito ang pagiging mulat ng mga AI system sa kanilang sariling mga internal na proseso at ang kakayahang subaybayan, i-regulate, at iakma ang kanilang pag-uugali nang naaayon. Katulad ng ginagawa natin kapag nagbabasa ng sitwasyon o humaharap sa isang problema. Ang kamalayang ito sa sarili ay makakatulong sa mga AI system na gumawa ng mas mahusay na desisyon, tukuyin ang mga pagkakamali, at mapabuti ang kanilang pagganap sa paglipas ng panahon—na muling nag-uugnay sa Turing test at sa debate kung ang AI ay magtatagumpay sa tao.

Sa konteksto ng mga agentic AI system, ang metakognisyon ay makakatulong sa pagtugon sa ilang mga hamon, tulad ng:
- Transparency: Tiyakin na ang mga AI system ay kayang ipaliwanag ang kanilang pangangatwiran at mga desisyon.
- Reasoning: Pagpapahusay ng kakayahan ng mga AI system na mag-synthesize ng impormasyon at gumawa ng matalinong desisyon.
- Adaptation: Pagbibigay-daan sa mga AI system na umangkop sa mga bagong kapaligiran at nagbabagong kondisyon.
- Perception: Pagpapabuti ng katumpakan ng mga AI system sa pagkilala at interpretasyon ng data mula sa kanilang kapaligiran.

### Ano ang Metakognisyon?

Ang metakognisyon, o "pag-iisip tungkol sa pag-iisip," ay isang mas mataas na antas ng proseso ng pag-iisip na kinabibilangan ng kamalayan sa sarili at regulasyon ng sariling mga proseso ng pag-iisip. Sa larangan ng AI, binibigyan ng metakognisyon ang mga agent ng kakayahang suriin at iakma ang kanilang mga estratehiya at aksyon, na nagreresulta sa mas mahusay na kakayahan sa paglutas ng problema at paggawa ng desisyon. Sa pamamagitan ng pag-unawa sa metakognisyon, maaari kang magdisenyo ng mga AI agent na hindi lamang mas matalino kundi mas adaptable at epektibo rin. Sa tunay na metakognisyon, makikita mong ang AI ay tahasang nagrereason tungkol sa sarili nitong pangangatwiran.

Halimbawa: “Pinili ko ang mas murang mga flight dahil… maaaring hindi ko napansin ang mga direktang flight, kaya’t kailangan kong muling suriin.”
Pag-track kung paano o bakit ito pumili ng isang partikular na ruta.
- Napansin na nagkamali ito dahil masyado itong umasa sa mga kagustuhan ng user mula sa nakaraan, kaya binabago nito ang estratehiya sa paggawa ng desisyon, hindi lamang ang huling rekomendasyon.
- Pagsusuri ng mga pattern tulad ng, “Tuwing binabanggit ng user ang ‘masyadong masikip,’ hindi ko lamang dapat alisin ang ilang atraksyon kundi dapat ding suriin kung ang paraan ko ng pagpili ng ‘mga pangunahing atraksyon’ ay mali kung palagi akong nagra-rank batay sa kasikatan.”

### Kahalagahan ng Metakognisyon sa mga AI Agent

Ang metakognisyon ay may mahalagang papel sa disenyo ng mga AI agent para sa ilang mga dahilan:

![Kahalagahan ng Metakognisyon](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.tl.png)

- Pagninilay sa Sarili: Ang mga agent ay maaaring suriin ang kanilang sariling pagganap at tukuyin ang mga lugar na kailangang pagbutihin.
- Kakayahang Umangkop: Ang mga agent ay maaaring baguhin ang kanilang mga estratehiya batay sa mga nakaraang karanasan at nagbabagong kapaligiran.
- Pagwawasto ng Pagkakamali: Ang mga agent ay maaaring awtomatikong tukuyin at itama ang mga pagkakamali, na nagreresulta sa mas tumpak na mga resulta.
- Pamamahala ng Mga Mapagkukunan: Ang mga agent ay maaaring i-optimize ang paggamit ng mga mapagkukunan, tulad ng oras at computational power, sa pamamagitan ng pagpaplano at pagsusuri ng kanilang mga aksyon.

## Mga Komponent ng isang AI Agent

Bago sumisid sa mga proseso ng metakognisyon, mahalagang maunawaan ang mga pangunahing komponent ng isang AI agent. Karaniwang binubuo ang isang AI agent ng:

- Persona: Ang personalidad at mga katangian ng agent, na tumutukoy kung paano ito nakikipag-ugnayan sa mga user.
- Mga Tool: Ang mga kakayahan at tungkulin na kayang gampanan ng agent.
- Mga Kasanayan: Ang kaalaman at kadalubhasaan na taglay ng agent.

Ang mga komponent na ito ay nagtutulungan upang makabuo ng isang "yunit ng kadalubhasaan" na kayang gampanan ang mga partikular na gawain.

**Halimbawa**:
Isipin ang isang travel agent, isang serbisyo ng agent na hindi lamang nagpaplano ng iyong bakasyon kundi ina-adjust din ang ruta nito batay sa real-time na data at mga nakaraang karanasan ng customer.

### Halimbawa: Metakognisyon sa isang Travel Agent Service

Isipin na nagdidisenyo ka ng isang travel agent service na pinapagana ng AI. Ang agent na ito, "Travel Agent," ay tumutulong sa mga user sa pagpaplano ng kanilang mga bakasyon. Upang maisama ang metakognisyon, kailangang suriin at ayusin ng Travel Agent ang mga aksyon nito batay sa kamalayan sa sarili at mga nakaraang karanasan. Narito kung paano maaaring gumanap ang metakognisyon:

#### Kasalukuyang Gawain

Ang kasalukuyang gawain ay tulungan ang isang user na magplano ng biyahe sa Paris.

#### Mga Hakbang upang Kumpletuhin ang Gawain

1. **Kunin ang Mga Kagustuhan ng User**: Tanungin ang user tungkol sa kanilang mga petsa ng paglalakbay, badyet, interes (hal., museo, pagkain, pamimili), at anumang partikular na kinakailangan.
2. **Kunin ang Impormasyon**: Maghanap ng mga opsyon sa flight, tirahan, atraksyon, at mga restawran na tumutugma sa mga kagustuhan ng user.
3. **Gumawa ng Mga Rekomendasyon**: Magbigay ng isang personalized na itinerary na may mga detalye ng flight, reserbasyon sa hotel, at mga iminungkahing aktibidad.
4. **Ayusin Batay sa Feedback**: Humingi ng feedback mula sa user sa mga rekomendasyon at gumawa ng kinakailangang mga pagsasaayos.

#### Mga Kinakailangang Mapagkukunan

- Access sa mga database ng flight at hotel booking.
- Impormasyon tungkol sa mga atraksyon at restawran sa Paris.
- Data ng feedback ng user mula sa mga nakaraang interaksyon.

#### Karanasan at Pagninilay sa Sarili

Ginagamit ng Travel Agent ang metakognisyon upang suriin ang pagganap nito at matuto mula sa mga nakaraang karanasan. Halimbawa:

1. **Pagsusuri ng Feedback ng User**: Sinusuri ng Travel Agent ang feedback ng user upang matukoy kung aling mga rekomendasyon ang nagustuhan at alin ang hindi. Ina-adjust nito ang mga susunod na mungkahi nang naaayon.
2. **Kakayahang Umangkop**: Kung ang isang user ay dati nang nagpahayag ng hindi pagkagusto sa masisikip na lugar, iiwasan ng Travel Agent na magrekomenda ng mga sikat na lugar ng turista sa mga oras ng kasagsagan sa hinaharap.
3. **Pagwawasto ng Pagkakamali**: Kung nagkamali ang Travel Agent sa isang nakaraang booking, tulad ng pagrekomenda ng isang hotel na fully booked na, natututo itong mas masusing suriin ang availability bago magbigay ng mga rekomendasyon.

#### Praktikal na Halimbawa para sa Developer

Narito ang isang pinasimpleng halimbawa ng code ng Travel Agent na nagsasama ng metakognisyon:

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

#### Bakit Mahalaga ang Metakognisyon

- **Pagninilay sa Sarili**: Ang mga agent ay maaaring suriin ang kanilang pagganap at tukuyin ang mga lugar na kailangang pagbutihin.
- **Kakayahang Umangkop**: Ang mga agent ay maaaring baguhin ang mga estratehiya batay sa feedback at nagbabagong kondisyon.
- **Pagwawasto ng Pagkakamali**: Ang mga agent ay maaaring awtomatikong tukuyin at itama ang mga pagkakamali.
- **Pamamahala ng Mga Mapagkukunan**: Ang mga agent ay maaaring i-optimize ang paggamit ng mga mapagkukunan, tulad ng oras at computational power.

Sa pamamagitan ng pagsasama ng metakognisyon, ang Travel Agent ay maaaring magbigay ng mas personalized at tumpak na mga rekomendasyon sa paglalakbay, na nagpapahusay sa kabuuang karanasan ng user.

---

## 2. Pagpaplano sa mga Agent

Ang pagpaplano ay isang mahalagang bahagi ng pag-uugali ng AI agent. Kasama rito ang pag-outline ng mga hakbang na kinakailangan upang makamit ang isang layunin, isinasaalang-alang ang kasalukuyang estado, mga mapagkukunan, at posibleng mga hadlang.

### Mga Elemento ng Pagpaplano

- **Kasalukuyang Gawain**: Malinaw na tukuyin ang gawain.
- **Mga Hakbang upang Kumpletuhin ang Gawain**: Hatiin ang gawain sa mga hakbang na madaling pamahalaan.
- **Mga Kinakailangang Mapagkukunan**: Tukuyin ang mga kinakailangang mapagkukunan.
- **Karanasan**: Gamitin ang mga nakaraang karanasan upang gabayan ang pagpaplano.

**Halimbawa**:
Narito ang mga hakbang na kailangang gawin ng Travel Agent upang epektibong matulungan ang isang user sa pagpaplano ng kanilang biyahe:

### Mga Hakbang para sa Travel Agent

1. **Kunin ang Mga Kagustuhan ng User**
   - Tanungin ang user tungkol sa mga detalye ng kanilang mga petsa ng paglalakbay, badyet, interes, at anumang partikular na kinakailangan.
   - Mga Halimbawa: "Kailan ka balak maglakbay?" "Ano ang saklaw ng iyong badyet?" "Anong mga aktibidad ang gusto mo sa bakasyon?"

2. **Kunin ang Impormasyon**
   - Maghanap ng mga kaugnay na opsyon sa paglalakbay batay sa mga kagustuhan ng user.
   - **Mga Flight**: Maghanap ng mga available na flight na pasok sa badyet at mga gustong petsa ng paglalakbay ng user.
   - **Mga Tirahan**: Maghanap ng mga hotel o rental property na tumutugma sa mga kagustuhan ng user para sa lokasyon, presyo, at amenities.
   - **Mga Atraksyon at Restawran**: Tukuyin ang mga sikat na atraksyon, aktibidad, at opsyon sa kainan na naaayon sa mga interes ng user.

3. **Gumawa ng Mga Rekomendasyon**
   - I-compile ang nakuhang impormasyon sa isang personalized na itinerary.
   - Magbigay ng mga detalye tulad ng mga opsyon sa flight, reserbasyon sa hotel, at mga iminungkahing aktibidad, na tinitiyak na iniangkop ang mga rekomendasyon sa mga kagustuhan ng user.

4. **Ipakita ang Itinerary sa User**
   - Ibahagi ang iminungkahing itinerary sa user para sa kanilang pagsusuri.
   - Halimbawa: "Narito ang isang iminungkahing itinerary para sa iyong biyahe sa Paris. Kasama rito ang mga detalye ng flight, mga reserbasyon sa hotel, at isang listahan ng mga inirerekomendang aktibidad at restawran. Ano ang iyong opinyon?"

5. **Kolektahin ang Feedback**
   - Humingi ng feedback mula sa user tungkol sa iminungkahing itinerary.
   - Mga Halimbawa: "Gusto mo ba ang mga opsyon sa flight?" "Angkop ba ang hotel para sa iyong mga pangangailangan?" "Mayroon bang mga aktibidad na nais mong idagdag o alisin?"

6. **Ayusin Batay sa Feedback**
   - Baguhin ang itinerary batay sa feedback ng user.
   - Gumawa ng mga kinakailangang pagbabago sa mga rekomendasyon sa flight, tirahan, at aktibidad upang mas tumugma sa mga kagustuhan ng user.

7. **Panghuling Kumpirmasyon**
   - Ipakita ang na-update na itinerary sa user para sa panghuling kumpirmasyon.
   - Halimbawa: "Ginawa ko na ang mga pagsasaayos batay sa iyong feedback. Narito ang na-update na itinerary. Ayos ba ang lahat para sa iyo?"

8. **Mag-book at Kumpirmahin ang mga Reserbasyon**
   - Kapag inaprubahan ng user ang itinerary, magpatuloy sa pag-book ng mga flight, tirahan, at anumang pre-planned na aktibidad.
   - Ipadala ang mga detalye ng kumpirmasyon sa user.

9. **Magbigay ng Patuloy na Suporta**
   - Manatiling available upang tumulong sa user sa anumang pagbabago o karagdagang kahilingan bago at habang nasa biyahe.
   - Halimbawa: "Kung kailangan mo ng karagdagang tulong habang nasa biyahe, huwag kang mag-atubiling makipag-ugnayan sa akin anumang oras!"

### Halimbawa ng Interaksyon

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

## 3. Corrective RAG System

Una, unawain natin ang pagkakaiba ng RAG Tool at Pre-emptive Context Load.

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.tl.png)

### Retrieval-Augmented Generation (RAG)

Ang RAG ay pinagsasama ang isang retrieval system sa isang generative model. Kapag may query, ang retrieval system ay kumukuha ng mga kaugnay na dokumento o data mula sa isang external na source, at ang nakuhang impormasyong ito ay ginagamit upang palakasin ang input sa generative model. Nakakatulong ito sa model na makabuo ng mas tumpak at kontekstwal na mga tugon.

Sa isang RAG system, ang agent ay kumukuha ng kaugnay na impormasyon mula sa isang knowledge base at ginagamit ito upang makabuo ng angkop na mga tugon o aksyon.

### Corrective RAG Approach

Ang Corrective RAG approach ay nakatuon sa paggamit ng mga teknik ng RAG upang itama ang mga pagkakamali at mapabuti ang katumpakan ng mga AI agent. Kasama rito ang:

1. **Prompting Technique**: Paggamit ng mga partikular na prompt upang gabayan ang agent sa pagkuha ng kaugnay na impormasyon.
2. **Tool**: Pagpapatupad ng mga algorithm at mekanismo na nagbibigay-daan sa agent na suriin ang kaugnayan ng nakuhang impormasyon at makabuo ng tumpak na mga tugon.
3. **Evaluation**: Patuloy na pagsusuri sa pagganap ng agent at paggawa ng mga pagsasaayos upang mapabuti ang katumpakan at kahusayan nito.

#### Halimbawa: Corrective RAG sa isang Search Agent

Isipin ang isang search agent na kumukuha ng impormasyon mula sa web upang sagutin ang mga query ng user. Ang Corrective RAG approach ay maaaring kasangkutan ng:

1. **Prompting Technique**: Pagbuo ng mga query sa paghahanap batay sa input ng user.
2. **Tool**: Paggamit ng natural language processing at machine learning algorithms upang i-rank at i-filter ang mga resulta ng paghahanap.
3. **Evaluation**: Pagsusuri ng feedback ng user upang tukuyin at itama ang mga hindi tumpak na impormasyon na nakuha.

### Corrective RAG sa Travel Agent

Ang Corrective RAG (Retrieval-Augmented Generation) ay nagpapahusay sa kakayahan ng AI na kumuha at bumuo ng impormasyon habang itinatama ang anumang hindi tumpak na datos. Tingnan natin kung paano magagamit ng Travel Agent ang Corrective RAG approach upang magbigay ng mas tumpak at kaugnay na mga rekomendasyon sa paglalakbay.

Kasama rito ang:

- **Prompting Technique:** Paggamit ng mga partikular na prompt upang gabayan ang agent sa pagkuha ng kaugnay na impormasyon.
- **Tool:** Pagpapatupad ng mga algorithm at mekanismo na nagbibigay-daan sa agent na suriin ang kaugnayan ng nakuhang impormasyon at makabuo ng tumpak na mga tugon.
- **Evaluation:** Patuloy na pagsusuri sa pagganap ng agent at paggawa ng mga pagsasaayos upang mapabuti ang katumpakan at kahusayan nito.


### Pre-emptive Context Load

Ang Pre-emptive Context Load ay tumutukoy sa paglo-load ng kaugnay na konteksto o impormasyon bago pa man iproseso ang isang query. Nangangahulugan ito na may access na ang modelo sa impormasyong ito mula sa simula, na makakatulong upang makabuo ng mas may kaalaman na sagot nang hindi na kailangang mag-retrieve ng karagdagang data habang nasa proseso.

Narito ang isang simpleng halimbawa kung paano maaaring magmukha ang pre-emptive context load para sa isang travel agent application sa Python:

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

#### Paliwanag

1. **Initialization (`__init__` method)**: Ang `TravelAgent` class ay naglo-load ng isang dictionary na naglalaman ng impormasyon tungkol sa mga sikat na destinasyon tulad ng Paris, Tokyo, New York, at Sydney. Kasama sa dictionary ang mga detalye tulad ng bansa, pera, wika, at mga pangunahing atraksyon para sa bawat destinasyon.

2. **Pagkuha ng Impormasyon (`get_destination_info` method)**: Kapag nagtanong ang isang user tungkol sa isang partikular na destinasyon, kinukuha ng `get_destination_info` method ang kaugnay na impormasyon mula sa pre-loaded na context dictionary.

Sa pamamagitan ng pre-loading ng konteksto, ang travel agent application ay maaaring mabilis na tumugon sa mga tanong ng user nang hindi na kailangang mag-retrieve ng impormasyon mula sa isang external na source sa real-time. Ginagawa nitong mas epektibo at responsive ang application.

### Bootstrapping ng Plano gamit ang Layunin Bago Mag-Iterate

Ang bootstrapping ng plano gamit ang layunin ay tumutukoy sa pagsisimula ng isang proseso na may malinaw na layunin o target na resulta. Sa pamamagitan ng pagtukoy sa layuning ito mula sa simula, magagamit ito ng modelo bilang gabay sa buong proseso ng pag-iterate. Nakakatulong ito upang masigurado na ang bawat iteration ay papalapit sa inaasahang resulta, na ginagawang mas epektibo at nakatuon ang proseso.

Narito ang isang halimbawa kung paano maaaring mag-bootstrap ng travel plan gamit ang layunin bago mag-iterate para sa isang travel agent sa Python:

### Scenario

Isang travel agent ang nais magplano ng customized na bakasyon para sa isang kliyente. Ang layunin ay lumikha ng travel itinerary na magbibigay ng pinakamataas na kasiyahan sa kliyente batay sa kanilang mga kagustuhan at budget.

### Mga Hakbang

1. Tukuyin ang mga kagustuhan at budget ng kliyente.
2. I-bootstrap ang paunang plano batay sa mga kagustuhan.
3. Mag-iterate upang i-refine ang plano, na-optimize para sa kasiyahan ng kliyente.

#### Python Code

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

#### Paliwanag ng Code

1. **Initialization (`__init__` method)**: Ang `TravelAgent` class ay ini-initialize gamit ang listahan ng mga potensyal na destinasyon, bawat isa ay may mga attribute tulad ng pangalan, gastos, at uri ng aktibidad.

2. **Bootstrapping ng Plano (`bootstrap_plan` method)**: Ang method na ito ay lumilikha ng paunang travel plan batay sa mga kagustuhan at budget ng kliyente. Ini-iterate nito ang listahan ng mga destinasyon at idinadagdag ang mga ito sa plano kung tumutugma ang mga ito sa mga kagustuhan ng kliyente at pasok sa budget.

3. **Pag-match ng Kagustuhan (`match_preferences` method)**: Ang method na ito ay nagche-check kung ang isang destinasyon ay tumutugma sa mga kagustuhan ng kliyente.

4. **Pag-iterate ng Plano (`iterate_plan` method)**: Ang method na ito ay nagre-refine ng paunang plano sa pamamagitan ng pagsubok na palitan ang bawat destinasyon sa plano ng mas angkop na destinasyon, isinasaalang-alang ang mga kagustuhan at limitasyon sa budget ng kliyente.

5. **Pagkalkula ng Gastos (`calculate_cost` method)**: Ang method na ito ay kinakalkula ang kabuuang gastos ng kasalukuyang plano, kabilang ang potensyal na bagong destinasyon.

#### Halimbawa ng Paggamit

- **Paunang Plano**: Lumilikha ang travel agent ng paunang plano batay sa kagustuhan ng kliyente para sa sightseeing at budget na $2000.
- **Refined Plan**: Ang travel agent ay nag-iiterate ng plano, na-optimize para sa mga kagustuhan at budget ng kliyente.

Sa pamamagitan ng pag-bootstrap ng plano gamit ang malinaw na layunin (hal., pag-maximize ng kasiyahan ng kliyente) at pag-iterate upang i-refine ang plano, maaaring lumikha ang travel agent ng customized at optimized na travel itinerary para sa kliyente. Ang approach na ito ay nagsisiguro na ang travel plan ay naaayon sa mga kagustuhan at budget ng kliyente mula sa simula at patuloy na bumubuti sa bawat iteration.

### Paggamit ng LLM para sa Re-ranking at Scoring

Ang Large Language Models (LLMs) ay maaaring gamitin para sa re-ranking at scoring sa pamamagitan ng pagsusuri sa kaugnayan at kalidad ng mga na-retrieve na dokumento o mga generated na sagot. Narito kung paano ito gumagana:

**Retrieval:** Ang unang hakbang sa retrieval ay ang pagkuha ng set ng mga kandidato na dokumento o sagot batay sa query.

**Re-ranking:** Ang LLM ay sinusuri ang mga kandidatong ito at nire-re-rank ang mga ito batay sa kanilang kaugnayan at kalidad. Ang hakbang na ito ay nagsisiguro na ang pinaka-kaugnay at mataas na kalidad na impormasyon ang unang ipinapakita.

**Scoring:** Ang LLM ay nag-aassign ng scores sa bawat kandidato, na nagpapakita ng kanilang kaugnayan at kalidad. Nakakatulong ito sa pagpili ng pinakamahusay na sagot o dokumento para sa user.

Sa pamamagitan ng paggamit ng LLMs para sa re-ranking at scoring, maaaring magbigay ang sistema ng mas tumpak at kontekstwal na kaugnay na impormasyon, na nagpapabuti sa kabuuang karanasan ng user.

Narito ang isang halimbawa kung paano maaaring gamitin ng isang travel agent ang Large Language Model (LLM) para sa re-ranking at scoring ng mga travel destinations batay sa mga kagustuhan ng user sa Python:

#### Scenario - Paglalakbay batay sa Kagustuhan

Isang travel agent ang nais magrekomenda ng pinakamahusay na travel destinations sa isang kliyente batay sa kanilang mga kagustuhan. Ang LLM ang tutulong sa pag-re-rank at pag-score ng mga destinasyon upang masigurado na ang pinaka-kaugnay na mga opsyon ang maipapakita.

#### Mga Hakbang:

1. Kolektahin ang mga kagustuhan ng user.
2. Mag-retrieve ng listahan ng mga potensyal na travel destinations.
3. Gamitin ang LLM upang mag-re-rank at mag-score ng mga destinasyon batay sa mga kagustuhan ng user.

Narito kung paano mo maaaring i-update ang naunang halimbawa upang gamitin ang Azure OpenAI Services:

#### Mga Kinakailangan

1. Kailangan mo ng Azure subscription.
2. Gumawa ng Azure OpenAI resource at kunin ang iyong API key.

#### Halimbawa ng Python Code

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

#### Paliwanag ng Code - Preference Booker

1. **Initialization**: Ang `TravelAgent` class ay ini-initialize gamit ang listahan ng mga potensyal na travel destinations, bawat isa ay may mga attribute tulad ng pangalan at deskripsyon.

2. **Pagkuha ng Rekomendasyon (`get_recommendations` method)**: Ang method na ito ay bumubuo ng prompt para sa Azure OpenAI service batay sa mga kagustuhan ng user at gumagawa ng HTTP POST request sa Azure OpenAI API upang makuha ang re-ranked at scored na mga destinasyon.

3. **Pagbuo ng Prompt (`generate_prompt` method)**: Ang method na ito ay nagko-construct ng prompt para sa Azure OpenAI, kabilang ang mga kagustuhan ng user at ang listahan ng mga destinasyon. Ang prompt ay gumagabay sa modelo upang mag-re-rank at mag-score ng mga destinasyon batay sa ibinigay na mga kagustuhan.

4. **API Call**: Ang `requests` library ay ginagamit upang gumawa ng HTTP POST request sa Azure OpenAI API endpoint. Ang response ay naglalaman ng re-ranked at scored na mga destinasyon.

5. **Halimbawa ng Paggamit**: Kinokolekta ng travel agent ang mga kagustuhan ng user (hal., interes sa sightseeing at diverse culture) at ginagamit ang Azure OpenAI service upang makuha ang re-ranked at scored na mga rekomendasyon para sa travel destinations.

Siguraduhing palitan ang `your_azure_openai_api_key` ng iyong aktwal na Azure OpenAI API key at ang `https://your-endpoint.com/...` ng aktwal na endpoint URL ng iyong Azure OpenAI deployment.

Sa pamamagitan ng paggamit ng LLM para sa re-ranking at scoring, maaaring magbigay ang travel agent ng mas personalized at kaugnay na travel recommendations sa mga kliyente, na nagpapahusay sa kanilang kabuuang karanasan.
#### Praktikal na Halimbawa: Paghahanap na may Layunin sa Travel Agent

Gamitin natin ang Travel Agent bilang halimbawa upang makita kung paano maipapatupad ang paghahanap na may layunin.

1. **Pagkuha ng Mga Kagustuhan ng Gumagamit**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Pag-unawa sa Layunin ng Gumagamit**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Pagiging Malaman sa Konteksto**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Paghahanap at Pag-personalize ng Mga Resulta**

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

5. **Halimbawa ng Paggamit**

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

## 4. Pagbuo ng Code bilang Isang Kasangkapan

Ang mga ahenteng bumubuo ng code ay gumagamit ng mga AI model upang magsulat at magpatakbo ng code, na nagreresolba ng mga komplikadong problema at nag-a-automate ng mga gawain.

### Mga Ahenteng Bumubuo ng Code

Ang mga ahenteng bumubuo ng code ay gumagamit ng generative AI models upang magsulat at magpatakbo ng code. Ang mga ahenteng ito ay maaaring magresolba ng mga komplikadong problema, mag-automate ng mga gawain, at magbigay ng mahalagang kaalaman sa pamamagitan ng pagbuo at pagpapatakbo ng code sa iba't ibang programming languages.

#### Praktikal na Aplikasyon

1. **Awtomatikong Pagbuo ng Code**: Bumuo ng mga code snippet para sa mga partikular na gawain, tulad ng data analysis, web scraping, o machine learning.
2. **SQL bilang RAG**: Gumamit ng SQL queries upang kumuha at magmanipula ng data mula sa mga database.
3. **Pagresolba ng Problema**: Gumawa at magpatakbo ng code upang magresolba ng mga partikular na problema, tulad ng pag-optimize ng mga algorithm o pagsusuri ng data.

#### Halimbawa: Ahenteng Bumubuo ng Code para sa Data Analysis

Isipin na ikaw ay nagdidisenyo ng isang ahenteng bumubuo ng code. Ganito ito maaaring gumana:

1. **Gawain**: Suriin ang isang dataset upang matukoy ang mga trend at pattern.
2. **Mga Hakbang**:
   - I-load ang dataset sa isang data analysis tool.
   - Bumuo ng mga SQL query upang i-filter at i-aggregate ang data.
   - Patakbuhin ang mga query at kunin ang mga resulta.
   - Gamitin ang mga resulta upang bumuo ng mga visualization at kaalaman.
3. **Mga Kinakailangang Resource**: Access sa dataset, mga tool sa data analysis, at kakayahan sa SQL.
4. **Karanasan**: Gamitin ang mga nakaraang resulta ng pagsusuri upang mapabuti ang katumpakan at kaugnayan ng mga susunod na pagsusuri.

### Halimbawa: Ahenteng Bumubuo ng Code para sa Travel Agent

Sa halimbawang ito, magdidisenyo tayo ng isang ahenteng bumubuo ng code, ang Travel Agent, upang tulungan ang mga gumagamit sa pagpaplano ng kanilang paglalakbay sa pamamagitan ng pagbuo at pagpapatakbo ng code. Ang ahenteng ito ay maaaring humawak ng mga gawain tulad ng pagkuha ng mga opsyon sa paglalakbay, pag-filter ng mga resulta, at pagbuo ng itinerary gamit ang generative AI.

#### Pangkalahatang-ideya ng Ahenteng Bumubuo ng Code

1. **Pagkuha ng Mga Kagustuhan ng Gumagamit**: Kinokolekta ang input ng gumagamit tulad ng destinasyon, mga petsa ng paglalakbay, badyet, at interes.
2. **Pagbuo ng Code upang Kumuha ng Data**: Bumubuo ng mga code snippet upang kumuha ng data tungkol sa mga flight, hotel, at atraksyon.
3. **Pagpapatakbo ng Nabuo na Code**: Pinapatakbo ang nabuo na code upang kumuha ng real-time na impormasyon.
4. **Pagbuo ng Itinerary**: Binubuo ang nakuhang data sa isang personalized na plano sa paglalakbay.
5. **Pag-aayos Batay sa Feedback**: Tumanggap ng feedback mula sa gumagamit at muling bumuo ng code kung kinakailangan upang pinuhin ang mga resulta.

#### Hakbang-hakbang na Pagpapatupad

1. **Pagkuha ng Mga Kagustuhan ng Gumagamit**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Pagbuo ng Code upang Kumuha ng Data**

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

3. **Pagpapatakbo ng Nabuo na Code**

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

4. **Pagbuo ng Itinerary**

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

5. **Pag-aayos Batay sa Feedback**

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

### Paggamit ng Kamalayan sa Kapaligiran at Pangangatwiran

Ang paggamit ng schema ng table ay maaaring mapahusay ang proseso ng pagbuo ng query sa pamamagitan ng paggamit ng kamalayan sa kapaligiran at pangangatwiran.

Narito ang isang halimbawa kung paano ito magagawa:

1. **Pag-unawa sa Schema**: Mauunawaan ng sistema ang schema ng table at gagamitin ang impormasyong ito upang i-ground ang pagbuo ng query.
2. **Pag-aayos Batay sa Feedback**: Ia-adjust ng sistema ang mga kagustuhan ng gumagamit batay sa feedback at magpapasya kung aling mga field sa schema ang kailangang i-update.
3. **Pagbuo at Pagpapatakbo ng Mga Query**: Bubuo at magpapatakbo ang sistema ng mga query upang kumuha ng na-update na data ng flight at hotel batay sa mga bagong kagustuhan.

Narito ang isang na-update na halimbawa ng Python code na nagsasama ng mga konseptong ito:

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

#### Paliwanag - Pag-book Batay sa Feedback

1. **Kamalayan sa Schema**: Ang `schema` dictionary ay nagde-define kung paano dapat i-adjust ang mga kagustuhan batay sa feedback. Kasama rito ang mga field tulad ng `favorites` at `avoid`, na may kaukulang mga adjustment.
2. **Pag-aayos ng Mga Kagustuhan (`adjust_based_on_feedback` method)**: Ina-adjust ng method na ito ang mga kagustuhan batay sa feedback ng gumagamit at sa schema.
3. **Mga Pag-aayos Batay sa Kapaligiran (`adjust_based_on_environment` method)**: Ina-customize ng method na ito ang mga adjustment batay sa schema at feedback.
4. **Pagbuo at Pagpapatakbo ng Mga Query**: Bumubuo ang sistema ng code upang kumuha ng na-update na data ng flight at hotel batay sa mga na-adjust na kagustuhan at sinisimulate ang pagpapatakbo ng mga query na ito.
5. **Pagbuo ng Itinerary**: Lumilikha ang sistema ng na-update na itinerary batay sa bagong data ng flight, hotel, at atraksyon.

Sa pamamagitan ng paggawa ng sistema na may kamalayan sa kapaligiran at pangangatwiran batay sa schema, makakabuo ito ng mas tumpak at kaugnay na mga query, na nagreresulta sa mas mahusay na mga rekomendasyon sa paglalakbay at mas personalized na karanasan ng gumagamit.

### Paggamit ng SQL bilang Retrieval-Augmented Generation (RAG) Technique

Ang SQL (Structured Query Language) ay isang makapangyarihang kasangkapan para sa pakikipag-ugnayan sa mga database. Kapag ginamit bilang bahagi ng Retrieval-Augmented Generation (RAG) approach, maaaring kumuha ang SQL ng kaugnay na data mula sa mga database upang magbigay ng impormasyon at bumuo ng mga tugon o aksyon sa mga AI agent. Tuklasin natin kung paano magagamit ang SQL bilang RAG technique sa konteksto ng Travel Agent.

#### Mga Pangunahing Konsepto

1. **Pakikipag-ugnayan sa Database**:
   - Ginagamit ang SQL upang mag-query sa mga database, kumuha ng kaugnay na impormasyon, at magmanipula ng data.
   - Halimbawa: Pagkuha ng mga detalye ng flight, impormasyon ng hotel, at mga atraksyon mula sa isang travel database.

2. **Integrasyon sa RAG**:
   - Ang mga SQL query ay nabubuo batay sa input at kagustuhan ng gumagamit.
   - Ang nakuhang data ay ginagamit upang bumuo ng mga personalized na rekomendasyon o aksyon.

3. **Dynamic Query Generation**:
   - Ang AI agent ay bumubuo ng dynamic SQL queries batay sa konteksto at pangangailangan ng gumagamit.
   - Halimbawa: Pag-customize ng SQL queries upang i-filter ang mga resulta batay sa badyet, mga petsa, at interes.

#### Mga Aplikasyon

- **Awtomatikong Pagbuo ng Code**: Bumuo ng mga code snippet para sa mga partikular na gawain.
- **SQL bilang RAG**: Gumamit ng SQL queries upang magmanipula ng data.
- **Pagresolba ng Problema**: Gumawa at magpatakbo ng code upang magresolba ng mga problema.

**Halimbawa**:
Isang data analysis agent:

1. **Gawain**: Suriin ang isang dataset upang makahanap ng mga trend.
2. **Mga Hakbang**:
   - I-load ang dataset.
   - Bumuo ng mga SQL query upang i-filter ang data.
   - Patakbuhin ang mga query at kunin ang mga resulta.
   - Bumuo ng mga visualization at kaalaman.
3. **Mga Resource**: Access sa dataset, kakayahan sa SQL.
4. **Karanasan**: Gamitin ang mga nakaraang resulta upang mapabuti ang mga susunod na pagsusuri.

#### Praktikal na Halimbawa: Paggamit ng SQL sa Travel Agent

1. **Pagkuha ng Mga Kagustuhan ng Gumagamit**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Pagbuo ng SQL Queries**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Pagpapatakbo ng SQL Queries**

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

4. **Pagbuo ng Mga Rekomendasyon**

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

#### Halimbawa ng SQL Queries

1. **Flight Query**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotel Query**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraction Query**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Sa pamamagitan ng paggamit ng SQL bilang bahagi ng Retrieval-Augmented Generation (RAG) technique, ang mga AI agent tulad ng Travel Agent ay maaaring dynamic na kumuha at gumamit ng kaugnay na data upang magbigay ng tumpak at personalized na mga rekomendasyon.

### Halimbawa ng Metacognition

Upang maipakita ang isang implementasyon ng metacognition, gagawa tayo ng isang simpleng ahente na *nagpapakita ng proseso ng pagninilay sa sarili* habang nilulutas ang isang problema. Sa halimbawang ito, gagawa tayo ng sistema kung saan sinusubukan ng ahente na i-optimize ang pagpili ng hotel, ngunit sinusuri nito ang sariling proseso ng pagdedesisyon at ina-adjust ang estratehiya kapag may mga pagkakamali o hindi magandang pagpili.

#### Paano ito nagpapakita ng metacognition:

1. **Paunang Desisyon**: Pipiliin ng ahente ang pinakamurang hotel, nang hindi isinasaalang-alang ang kalidad.
2. **Pagninilay at Pagsusuri**: Pagkatapos ng paunang pagpili, susuriin ng ahente kung ang hotel ay isang "masamang" pagpili gamit ang feedback ng gumagamit. Kapag natukoy na mababa ang kalidad ng hotel, magmumuni-muni ito sa sariling pangangatwiran.
3. **Pag-aayos ng Estratehiya**: Ia-adjust ng ahente ang estratehiya batay sa pagninilay at lilipat mula sa "pinakamura" patungo sa "pinakamataas na kalidad," kaya pinapabuti ang proseso ng pagdedesisyon sa mga susunod na pagkakataon.

Narito ang isang halimbawa:

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

#### Kakayahan ng Metacognition ng Ahente

Ang mahalaga dito ay ang kakayahan ng ahente na:
- Suriin ang mga naunang pagpili at proseso ng pagdedesisyon.
- Ia-adjust ang estratehiya batay sa pagninilay, na nagpapakita ng metacognition sa aksyon.

Ito ay isang simpleng anyo ng metacognition kung saan ang sistema ay may kakayahang i-adjust ang proseso ng pangangatwiran batay sa internal na feedback.

### Konklusyon

Ang metacognition ay isang makapangyarihang kasangkapan na maaaring lubos na mapahusay ang kakayahan ng mga AI agent. Sa pamamagitan ng pagsasama ng mga proseso ng metacognition, maaari kang magdisenyo ng mga ahente na mas matalino, adaptable, at mahusay. Gamitin ang mga karagdagang resource upang higit pang tuklasin ang kamangha-manghang mundo ng metacognition sa mga AI agent.

### May Higit Pang Katanungan Tungkol sa Metacognition Design Pattern?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at makuha ang mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Nakaraang Aralin

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Susunod na Aralin

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.