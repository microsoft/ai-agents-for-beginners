[![Megbízható AI-ügynökök](../../../translated_images/hu/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

# Megbízható AI-ügynökök létrehozása

## Bevezetés

Ebben a leckében a következőkről lesz szó:

- Hogyan építsünk és telepítsünk biztonságos és hatékony AI-ügynököket
- Fontos biztonsági szempontok AI-ügynökök fejlesztésekor.
- Hogyan biztosítsuk az adatok és a felhasználók magánéletének védelmét AI-ügynökök fejlesztésekor.

## Tanulási célok

A lecke elvégzése után képes leszel a következőkre:

- Azonosítani és mérsékelni a kockázatokat AI-ügynökök létrehozásakor.
- Biztonsági intézkedéseket bevezetni annak érdekében, hogy az adatok és a hozzáférések megfelelően legyenek kezelve.
- Olyan AI-ügynököket készíteni, amelyek megőrzik az adatvédelmet és minőségi felhasználói élményt nyújtanak.

## Biztonság

Először nézzük meg, hogyan építhetünk biztonságos ügynökalapú alkalmazásokat. A biztonság azt jelenti, hogy az AI-ügynök úgy működik, ahogy tervezték. Ügynökalapú alkalmazások készítőjeként rendelkezünk módszerekkel és eszközökkel a biztonság maximalizálására:

### Rendszerüzenet-keretrendszer létrehozása

Ha valaha építettél már AI-alkalmazást nagy nyelvi modellek (LLM-ek) használatával, akkor tudod, milyen fontos egy robusztus rendszerprompt vagy rendszerüzenet megtervezése. Ezek a promptok állítják fel a meta-szabályokat, utasításokat és iránymutatásokat arra vonatkozóan, hogyan lépjen kapcsolatba az LLM a felhasználóval és az adatokkal.

Az AI-ügynökök esetében a rendszerprompt még fontosabb, mivel az AI-ügynököknek nagyon konkrét utasításokra lesz szükségük a számukra tervezett feladatok elvégzéséhez.

Skálázható rendszerpromptok létrehozásához rendszerüzenet-keretrendszert használhatunk egy vagy több ügynök felépítéséhez az alkalmazásunkban:

![Rendszerüzenet-keretrendszer létrehozása](../../../translated_images/hu/system-message-framework.3a97368c92d11d68.webp)

#### 1. lépés: Meta rendszerüzenet létrehozása

A meta promptot egy LLM fogja használni arra, hogy létrehozza az általunk készített ügynökök számára szánt rendszerpromptokat. Sablonként tervezzük meg, hogy hatékonyan tudjunk több ügynököt is létrehozni, ha szükséges.

Íme egy példa egy meta rendszerüzenetre, amelyet a LLM-nek adnánk:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2. lépés: Alap prompt létrehozása

A következő lépés egy alap prompt létrehozása az AI-ügynök leírásához. Tartalmaznia kell az ügynök szerepét, azokat a feladatokat, amelyeket az ügynök elvégez, valamint minden egyéb felelősséget.

Íme egy példa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3. lépés: Alap rendszerüzenet átadása a LLM-nek

Most optimalizálhatjuk ezt a rendszerüzenetet úgy, hogy a meta rendszerüzenetet használjuk rendszerüzenetként, és mellé tesszük az alap rendszerüzenetet.

Ez olyan rendszerüzenetet eredményez, amely jobban alkalmas az AI-ügynökök irányítására:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### 4. lépés: Iterálás és fejlesztés

Ennek a rendszerüzenet-keretrendszernek az értéke abban rejlik, hogy könnyebbé teszi több ügynök rendszerüzeneteinek skálázását, valamint idővel a rendszerüzenetek fejlesztését. Ritka, hogy egy rendszerüzenet az első próbálkozásra tökéletesen működjön az egész használati esetnél. Az, hogy képesek vagyunk apró módosításokat és fejlesztéseket végrehajtani az alap rendszerüzenet megváltoztatásával és annak rendszeren történő lefuttatásával, lehetővé teszi az eredmények összehasonlítását és értékelését.

## A fenyegetések megértése

A megbízható AI-ügynökök építéséhez fontos megérteni és mérsékelni az AI-ügynökre leselkedő kockázatokat és fenyegetéseket. Nézzünk meg néhány különböző fenyegetést, és hogyan tervezhetsz és készülhetsz fel jobban rájuk.

![Fenyegetések megértése](../../../translated_images/hu/understanding-threats.89edeada8a97fc0f.webp)

### Feladat és utasítás

**Leírás:** A támadók megpróbálják megváltoztatni az AI-ügynök utasításait vagy céljait promptokkal vagy a bemenetek manipulálásával.

**Megelőzés**: Végrehajtási érvényesítési ellenőrzéseket és bemeneti szűrőket alkalmazz, hogy észleld a potenciálisan veszélyes promptokat még az AI-ügynök által történő feldolgozás előtt. Mivel ezek a támadások általában gyakori interakciót igényelnek az ügynökkel, a beszélgetés fordulóinak számának korlátozása szintén módot ad ezen típusú támadások megelőzésére.

### Kritikus rendszerekhez való hozzáférés

**Leírás:** Ha egy AI-ügynök hozzáfér olyan rendszerekhez és szolgáltatásokhoz, amelyek érzékeny adatokat tárolnak, a támadók kompromittálhatják a kommunikációt az ügynök és ezek a szolgáltatások között. Ez történhet közvetlen támadásként vagy közvetett próbálkozásként, hogy információt szerezzenek ezekről a rendszerekről az ügynökön keresztül.

**Megelőzés:** Az AI-ügynököknek csak szükség szerinti hozzáférést kell adni a rendszerekhez ezen típusú támadások megelőzése érdekében. Az ügynök és a rendszer közötti kommunikációnak is biztonságosnak kell lennie. A hitelesítés és a hozzáférés-vezérlés bevezetése további mód a védelemre.

### Erőforrás- és szolgáltatás-túlterhelés

**Leírás:** Az AI-ügynökök különböző eszközökhöz és szolgáltatásokhoz férhetnek hozzá a feladatok elvégzéséhez. A támadók ezt a képességet kihasználhatják úgy, hogy nagy mennyiségű kérést küldenek az AI-ügynökön keresztül ezeknek a szolgáltatásoknak, ami rendszerhibákhoz vagy magas költségekhez vezethet.

**Megelőzés:** Alkalmazz irányelveket az AI-ügynök által egy szolgáltatásnak küldhető kérések számának korlátozására. A beszélgetési fordulók és a kérések számának korlátozása az AI-ügynök felé szintén módot ad ezen típusú támadások megelőzésére.

### Tudásbázis megmérgezése

**Leírás:** Ez a támadástípus nem közvetlenül az AI-ügynököt célozza, hanem azt a tudásbázist és egyéb szolgáltatásokat, amelyeket az AI-ügynök használni fog. Ez magában foglalhatja az adatok vagy információk megsérülését vagy korrupttá tételét, amelyeket az AI-ügynök egy feladat elvégzéséhez használ, ami elfogult vagy váratlan válaszokhoz vezethet a felhasználó felé.

**Megelőzés:** Végezzen rendszeres ellenőrzést azon az adaton, amelyet az AI-ügynök a munkafolyamataiban fog használni. Biztosítsa, hogy az adatokhoz való hozzáférés biztonságos legyen, és csak megbízható személyek módosíthassák azokat, hogy elkerülje ezt a típusú támadást.

### Láncolt hibák

**Leírás:** Az AI-ügynökök különböző eszközökhöz és szolgáltatásokhoz férnek hozzá a feladatok elvégzéséhez. A támadók által okozott hibák más, az AI-ügynökhöz kapcsolódó rendszerek meghibásodásához vezethetnek, így a támadás kiterjedtebbé válhat és nehezebb lesz elhárítani.

**Megelőzés**: Ennek elkerülésére egyik módszer, ha az AI-ügynök korlátozott környezetben működik, például feladatokat végez Docker-konténerben, hogy megakadályozzuk a közvetlen rendszerellenes támadásokat. Tartalékmechanizmusok és újrapróbálkozási logika létrehozása, ha bizonyos rendszerek hibával válaszolnak, szintén módja a nagyobb rendszerhibák megelőzésének.

## Ember a hurkon

Egy másik hatékony módja a megbízható AI-ügynök rendszerek létrehozásának az ember a hurkon megközelítés használata. Ez egy olyan folyamatot hoz létre, ahol a felhasználók a futás során visszajelzést adhatnak az ügynököknek. A felhasználók lényegében ügynökként viselkednek egy többügynökös rendszerben, és jóváhagyással vagy a futó folyamat megszakításával befolyásolhatják azt.

![Ember a hurkon](../../../translated_images/hu/human-in-the-loop.5f0068a678f62f4f.webp)

Íme egy kódrészlet a Microsoft Agent Framework használatával, amely bemutatja, hogyan valósítják meg ezt a koncepciót:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Hozza létre a szolgáltatót emberi felügyeletű jóváhagyással
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Hozza létre az ügynököt emberi jóváhagyási lépéssel
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# A felhasználó felülvizsgálhatja és jóváhagyhatja a választ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Következtetés

A megbízható AI-ügynökök létrehozása alapos tervezést, robusztus biztonsági intézkedéseket és folyamatos iterációt igényel. Strukturált meta-prompt rendszerek alkalmazásával, a lehetséges fenyegetések megértésével és megelőző stratégiák alkalmazásával a fejlesztők olyan AI-ügynököket hozhatnak létre, amelyek egyszerre biztonságosak és hatékonyak. Emellett az ember a hurkon megközelítés beépítése biztosítja, hogy az AI-ügynökök összhangban maradjanak a felhasználói igényekkel, miközben csökkentik a kockázatokat. Ahogy az AI fejlődik, a biztonság, a magánélet és az etikai szempontok proaktív kezelése kulcsfontosságú lesz a bizalom és a megbízhatóság előmozdításában az AI-vezérelt rendszerekben.

### További kérdéseid vannak a megbízható AI-ügynökök létrehozásával kapcsolatban?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozz más tanulókkal, részt vehess konzultációs órákon, és választ kapj AI-ügynökeiddel kapcsolatos kérdéseidre.

## További források

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Felelős AI áttekintése</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatív AI modellek és AI-alkalmazások értékelése</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Biztonsági rendszerüzenetek</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kockázatértékelési sablon</a>

## Előző lecke

[Agentic RAG](../05-agentic-rag/README.md)

## Következő lecke

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) mesterséges intelligencia alapú fordítószolgáltatásával készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum eredeti nyelven készült változata tekintendő irányadónak. Kritikus fontosságú információk esetén javasolt profi, emberi fordító igénybevétele. Nem vállalunk felelősséget a jelen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->