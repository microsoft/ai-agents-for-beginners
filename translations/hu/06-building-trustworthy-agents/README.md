[![Megbízható AI ügynökök](../../../translated_images/hu/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

# Megbízható AI ügynökök építése

## Bevezetés

Ez a lecke a következőket tárgyalja:

- Hogyan építsünk és telepítsünk biztonságos és hatékony AI ügynököket
- Fontos biztonsági szempontok AI ügynökök fejlesztésekor.
- Hogyan tartsuk meg az adat- és felhasználói adatvédelmet AI ügynökök fejlesztése során.

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

- Azonosítsd és csökkentsd a kockázatokat AI ügynökök létrehozásakor.
- Biztonsági intézkedéseket valósíts meg az adatok és hozzáférések megfelelő kezeléséhez.
- Olyan AI ügynököket hozz létre, amelyek megőrzik az adatvédelmet és minőségi felhasználói élményt nyújtanak.

## Biztonság

Először nézzük meg, hogyan építsünk biztonságos ügynök alapú alkalmazásokat. A biztonság azt jelenti, hogy az AI ügynök a tervek szerint működik. Az ügynök alapú alkalmazások építőiként rendelkezünk módszerekkel és eszközökkel a biztonság maximalizálásához:

### Rendszerüzenet Keretrendszer építése

Ha valaha építettél már AI alkalmazást nagy nyelvi modellek (LLM-ek) használatával, tudod, mennyire fontos egy robusztus rendszerüzenet vagy rendszerprompt tervezése. Ezek a promptok megteremtik a meta szabályokat, utasításokat és irányelveket arra, hogy az LLM hogyan lép interakcióba a felhasználóval és az adatokkal.

AI ügynökök esetében a rendszerprompt még fontosabb, mivel az AI ügynököknek nagyon specifikus utasításokra lesz szükségük a számukra tervezett feladatok elvégzéséhez.

Skálázható rendszerpromptok létrehozásához használhatunk egy rendszerüzenet keretrendszert, amely segítségével egy vagy több ügynököt építhetünk az alkalmazásunkban:

![Rendszerüzenet Keretrendszer építése](../../../translated_images/hu/system-message-framework.3a97368c92d11d68.webp)

#### 1. lépés: Meta rendszerüzenet létrehozása

A meta promptot egy LLM használja majd az ügynökeink rendszerpromptjainak generálására. Úgy tervezzük, mint egy sablont, hogy hatékonyan tudjunk több ügynököt is létrehozni, ha szükséges.

Íme egy példa egy meta rendszerüzenetre, amit egy LLM-nek adnánk:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2. lépés: Alap prompt létrehozása

A következő lépés egy alap prompt létrehozása az AI ügynök leírására. Tartalmaznia kell az ügynök szerepét, az általa elvégzendő feladatokat és egyéb felelősségeket.

Íme egy példa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3. lépés: Alap rendszerüzenet átadása az LLM-nek

Most optimalizálhatjuk ezt a rendszerüzenetet azzal, hogy a meta rendszerüzenetet és az alap rendszerüzenetet adjuk meg rendszerüzenetként.

Ez egy olyan rendszerüzenetet eredményez, amely jobban irányítja az AI ügynökeinket:

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

#### 4. lépés: Iteráció és fejlesztés

Ennek a rendszerüzenet keretrendszernek az értéke abban rejlik, hogy könnyebbé teszi több ügynök rendszerüzeneteinek skálázható létrehozását, valamint a rendszerüzenetek időbeli fejlesztését. Ritka, hogy egy rendszerüzenet az első alkalommal tökéletesen működjön a teljes felhasználási esethez. A kis módosítások és fejlesztések lehetővé tétele az alap rendszerüzenet megváltoztatásával és újrafuttatásával lehetőséget ad az eredmények összehasonlítására és értékelésére.

## A fenyegetések megértése

Ahhoz, hogy megbízható AI ügynököket építsünk, fontos megérteni és csökkenteni az AI ügynököt érő kockázatokat és fenyegetéseket. Nézzük meg csak néhány különböző fenyegetést az AI ügynökökre, és hogyan tudsz jobban tervezni és felkészülni rájuk.

![A fenyegetések megértése](../../../translated_images/hu/understanding-threats.89edeada8a97fc0f.webp)

### Feladat és utasítás

**Leírás:** A támadók megpróbálják megváltoztatni az AI ügynök utasításait vagy céljait promptolással vagy bemenetek manipulálásával.

**Megelőzés:** Ellenőrzéseket és bemeneti szűrőket kell alkalmazni annak felismerésére, hogy potenciálisan veszélyes promptok érkeznek-e az AI ügynökhöz. Mivel ezek a támadások általában többszöri interakciót igényelnek az ügynökkel, a beszélgetések körszámának korlátozása is segít megelőzni ezeket a támadásokat.

### Kritikus rendszerekhez való hozzáférés

**Leírás:** Ha egy AI ügynök hozzáféréssel rendelkezik olyan rendszerekhez és szolgáltatásokhoz, amelyek érzékeny adatokat tárolnak, a támadók kompromittálhatják az ügynök és ezek a szolgáltatások közti kommunikációt. Ezek lehetnek közvetlen támadások vagy közvetett próbálkozások információk megszerzésére az ügynökön keresztül.

**Megelőzés:** AI ügynökök csak szükséges esetben férjenek hozzá rendszerekhez az ilyen típusú támadások elkerülése érdekében. Az ügynök és a rendszer közötti kommunikációnak is biztonságosnak kell lennie. Hitelesítés és hozzáférés-vezérlés bevezetése további védelmet nyújt az ilyen információkhoz.

### Erőforrás- és szolgáltatás túlterhelés

**Leírás:** Az AI ügynökök különböző eszközökhöz és szolgáltatásokhoz férhetnek hozzá feladatok elvégzéséhez. A támadók ezt a képességet kihasználva nagyszámú kérést küldhetnek az AI ügynökön keresztül, ami rendszerleálláshoz vagy magas költségekhez vezethet.

**Megelőzés:** Olyan szabályzatokat kell bevezetni, amelyek korlátozzák, hogy az AI ügynök mennyi kérést küldhet egy szolgáltatásnak. A beszélgetési körök és kérések számának korlátozása az AI ügynökhöz szintén megakadályozza az ilyen típusú támadásokat.

### Tudásbázis megmérgezése

**Leírás:** Ez a támadástípus nem közvetlenül az AI ügynökre irányul, hanem a tudásbázisra és más szolgáltatásokra, amelyeket az AI ügynök fog használni. Ez magában foglalhatja az adatok vagy információk meghamisítását, amelyeket az AI ügynök felhasznál a feladatok elvégzéséhez, és ami torz vagy nem kívánt válaszokat eredményezhet a felhasználónak.

**Megelőzés:** Rendszeres adatellenőrzést kell végezni az AI ügynök munkafolyamataiban használt adatokon. Biztosítani kell, hogy az adatokhoz való hozzáférés biztonságos legyen, és csak megbízható személyek módosíthassák azokat az ilyen támadások elkerülése érdekében.

### Láncreakciós hibák

**Leírás:** AI ügynökök különböző eszközökhöz és szolgáltatásokhoz férnek hozzá a feladatok elvégzéséhez. A támadó által okozott hibák más rendszerek meghibásodásához vezethetnek, amelyekhez az AI ügynök csatlakozik, így a támadás szélesebb körűvé és nehezebben kezelhetővé válik.

**Megelőzés:** Egy módja ennek elkerülésére, ha az AI ügynök korlátozott környezetben működik, például Docker konténerben végzi a feladatokat, megakadályozva a közvetlen rendszer-támadásokat. Biztonsági mechanizmusok és újrapróbálkozás beiktatása, ha bizonyos rendszerek hibát jeleznek, szintén megakadályozza a nagyobb rendszerek meghibásodását.

## Ember a folyamatban

Egy másik hatékony módszer a megbízható AI ügynökrendszerek építésére az ember bevonása a folyamatba (Human-in-the-loop). Ez létrehoz egy folyamatot, amelyben a felhasználók visszajelzéseket tudnak adni az ügynökök futása közben. A felhasználók lényegében az ügynökök utasítóivá válnak a többügynökös rendszerben, jóváhagyásokat vagy a folyamat lezárását végezve.

![Ember a folyamatban](../../../translated_images/hu/human-in-the-loop.5f0068a678f62f4f.webp)

Íme egy kódrészlet a Microsoft Agent Framework használatával, amely bemutatja ennek a fogalomnak az alkalmazását:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Hozd létre a szolgáltatót emberi jóváhagyással
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Hozd létre az ügynököt emberi jóváhagyási lépéssel
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# A felhasználó átnézheti és jóváhagyhatja a választ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Összegzés

Megbízható AI ügynökök építéséhez alapos tervezésre, erős biztonsági intézkedésekre és folyamatos iterációra van szükség. Strukturált meta prompt rendszer alkalmazásával, a lehetséges fenyegetések megértésével és megfékező stratégiák alkalmazásával a fejlesztők olyan AI ügynököket hozhatnak létre, amelyek egyszerre biztonságosak és hatékonyak. Emellett az ember bevonása a folyamatban biztosítja, hogy az AI ügynökök összhangban maradjanak a felhasználók igényeivel miközben minimalizálják a kockázatokat. Amint az AI fejlődik, a biztonság, adatvédelem és etikai szempontok proaktív szemléletű fenntartása kulcsfontosságú lesz az AI-alapú rendszerek iránti bizalom és megbízhatóság építésében.

## Kód példák

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Lépésenkénti bemutató a meta-prompt rendszerüzenet keretrendszerről.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Előzetes jóváhagyási kapuk, kockázati szintek és audit naplózás megbízható ügynökök számára.

### Több kérdésed van a megbízható AI ügynökök építésével kapcsolatban?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél konzultációkon és választ kapj AI ügynökeiddel kapcsolatos kérdéseidre.

## További források

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Felelős AI áttekintés</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatív AI modellek és AI alkalmazások értékelése</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Biztonsági rendszerüzenetek</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kockázatértékelési sablon</a>

## Előző lecke

[Agentic RAG](../05-agentic-rag/README.md)

## Következő lecke

[Tervezési mintázat](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->