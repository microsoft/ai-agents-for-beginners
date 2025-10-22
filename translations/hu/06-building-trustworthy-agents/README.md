<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T20:07:35+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "hu"
}
-->
[![Megbízható MI Ügynökök](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.hu.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

# Megbízható MI Ügynökök Létrehozása

## Bevezetés

Ebben a leckében az alábbiakat tárgyaljuk:

- Hogyan építsünk és telepítsünk biztonságos és hatékony MI ügynököket.
- Fontos biztonsági szempontok az MI ügynökök fejlesztése során.
- Hogyan biztosítsuk az adatok és a felhasználók magánéletének védelmét az MI ügynökök fejlesztésekor.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Azonosítani és mérsékelni a kockázatokat az MI ügynökök létrehozása során.
- Biztonsági intézkedéseket bevezetni az adatok és hozzáférések megfelelő kezelésének biztosítására.
- Olyan MI ügynököket létrehozni, amelyek megőrzik az adatok bizalmasságát és minőségi felhasználói élményt nyújtanak.

## Biztonság

Először nézzük meg, hogyan építhetünk biztonságos ügynöki alkalmazásokat. A biztonság azt jelenti, hogy az MI ügynök az elvárásoknak megfelelően működik. Az ügynöki alkalmazások fejlesztőiként rendelkezésünkre állnak módszerek és eszközök a biztonság maximalizálására:

### Rendszerüzenet-keretrendszer létrehozása

Ha valaha építettél MI alkalmazást Nagy Nyelvi Modellek (LLM-ek) használatával, tudod, milyen fontos egy robusztus rendszerprompt vagy rendszerüzenet megtervezése. Ezek az üzenetek határozzák meg a meta szabályokat, utasításokat és irányelveket arra vonatkozóan, hogyan lépjen kapcsolatba az LLM a felhasználóval és az adatokkal.

Az MI ügynökök esetében a rendszerprompt még fontosabb, mivel az ügynököknek rendkívül specifikus utasításokra van szükségük a számukra kijelölt feladatok elvégzéséhez.

A skálázható rendszerpromtok létrehozásához használhatunk egy rendszerüzenet-keretrendszert, amely lehetővé teszi egy vagy több ügynök létrehozását az alkalmazásunkban:

![Rendszerüzenet-keretrendszer létrehozása](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.hu.png)

#### 1. lépés: Meta rendszerüzenet létrehozása

A meta promptot egy LLM használja az általunk létrehozott ügynökök rendszerpromtjainak generálására. Ezt sablonként tervezzük meg, hogy szükség esetén hatékonyan hozhassunk létre több ügynököt.

Íme egy példa egy meta rendszerüzenetre, amelyet az LLM-nek adnánk:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2. lépés: Alapvető prompt létrehozása

A következő lépés egy alapvető prompt létrehozása az MI ügynök leírására. Ebben szerepelnie kell az ügynök szerepének, az elvégzendő feladatoknak és az ügynök egyéb felelősségeinek.

Íme egy példa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3. lépés: Alapvető rendszerüzenet megadása az LLM-nek

Most optimalizálhatjuk ezt a rendszerüzenetet azáltal, hogy a meta rendszerüzenetet rendszerüzenetként, az alapvető rendszerüzenetet pedig bemenetként adjuk meg.

Ez egy olyan rendszerüzenetet eredményez, amely jobban irányítja az MI ügynököket:

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

Ennek a rendszerüzenet-keretrendszernek az értéke abban rejlik, hogy megkönnyíti több ügynök rendszerüzenetének létrehozását, valamint lehetővé teszi a rendszerüzenetek időbeli javítását. Ritka, hogy egy rendszerüzenet az első próbálkozásra teljes mértékben megfelel az adott felhasználási esetnek. Az alapvető rendszerüzenet apró módosításai és a rendszer újrafuttatása lehetővé teszi az eredmények összehasonlítását és értékelését.

## Fenyegetések megértése

Ahhoz, hogy megbízható MI ügynököket építsünk, fontos megérteni és mérsékelni az ügynököket érintő kockázatokat és fenyegetéseket. Nézzünk meg néhányat az MI ügynököket érintő különböző fenyegetések közül, és hogyan tervezhetünk és készülhetünk fel ezekre.

![Fenyegetések megértése](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.hu.png)

### Feladatok és utasítások

**Leírás:** A támadók megpróbálják megváltoztatni az MI ügynök utasításait vagy céljait promptok vagy bemenetek manipulálásával.

**Megelőzés:** Végezzen validációs ellenőrzéseket és bemeneti szűréseket, hogy azonosítsa a potenciálisan veszélyes promptokat, mielőtt azokat az MI ügynök feldolgozná. Mivel ezek a támadások általában gyakori interakciót igényelnek az ügynökkel, a beszélgetések fordulóinak korlátozása egy másik módja az ilyen támadások megelőzésének.

### Hozzáférés kritikus rendszerekhez

**Leírás:** Ha egy MI ügynök hozzáfér olyan rendszerekhez és szolgáltatásokhoz, amelyek érzékeny adatokat tárolnak, a támadók kompromittálhatják az ügynök és ezek között a szolgáltatások között zajló kommunikációt. Ezek lehetnek közvetlen támadások vagy közvetett kísérletek információk megszerzésére az ügynökön keresztül.

**Megelőzés:** Az MI ügynököknek csak szükség esetén legyen hozzáférésük a rendszerekhez, hogy megelőzzük az ilyen támadásokat. Az ügynök és a rendszer közötti kommunikációnak biztonságosnak kell lennie. Az autentikáció és a hozzáférés-vezérlés bevezetése szintén segíthet az információk védelmében.

### Erőforrások és szolgáltatások túlterhelése

**Leírás:** Az MI ügynökök különböző eszközökhöz és szolgáltatásokhoz férhetnek hozzá a feladatok elvégzéséhez. A támadók kihasználhatják ezt a képességet, hogy nagy mennyiségű kérést küldjenek az ügynökön keresztül, ami rendszerhibákhoz vagy magas költségekhez vezethet.

**Megelőzés:** Vezessen be szabályokat az MI ügynök által egy szolgáltatás felé küldhető kérések számának korlátozására. A beszélgetések fordulóinak és az ügynök által küldött kérések számának korlátozása szintén segíthet az ilyen támadások megelőzésében.

### Tudásbázis mérgezése

**Leírás:** Ez a támadástípus nem közvetlenül az MI ügynököt célozza, hanem a tudásbázist és más szolgáltatásokat, amelyeket az ügynök használ. Ez magában foglalhatja az adatok vagy információk korrumpálását, amelyeket az ügynök a feladatok elvégzéséhez használ, ami elfogult vagy nem kívánt válaszokat eredményezhet a felhasználó számára.

**Megelőzés:** Végezzen rendszeres ellenőrzéseket az adatokon, amelyeket az ügynök a munkafolyamataiban használ. Biztosítsa, hogy az adatokhoz való hozzáférés biztonságos legyen, és csak megbízható személyek módosíthassák azokat, hogy elkerülje az ilyen támadásokat.

### Hibák láncolata

**Leírás:** Az MI ügynökök különböző eszközökhöz és szolgáltatásokhoz férnek hozzá a feladatok elvégzéséhez. A támadók által okozott hibák más rendszerek meghibásodásához vezethetnek, amelyekhez az ügynök kapcsolódik, így a támadás szélesebb körűvé és nehezebben elháríthatóvá válik.

**Megelőzés:** Az egyik módszer ennek elkerülésére az, hogy az MI ügynök korlátozott környezetben működik, például feladatokat végez egy Docker-konténerben, hogy elkerülje a közvetlen rendszer támadásokat. Tartalék mechanizmusok és újrapróbálkozási logika létrehozása, amikor bizonyos rendszerek hibával válaszolnak, szintén segíthet a nagyobb rendszerhibák megelőzésében.

## Ember a folyamatban

Egy másik hatékony módja a megbízható MI ügynökrendszerek létrehozásának az ember a folyamatban megközelítés alkalmazása. Ez egy olyan folyamatot hoz létre, amelyben a felhasználók visszajelzést adhatnak az ügynököknek a futás során. A felhasználók lényegében ügynökökként működnek egy több ügynökből álló rendszerben, és jóváhagyhatják vagy megszakíthatják a futó folyamatot.

![Ember a folyamatban](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.hu.png)

Íme egy kódrészlet az AutoGen használatával, amely bemutatja, hogyan valósítható meg ez a koncepció:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Összefoglalás

A megbízható MI ügynökök létrehozása gondos tervezést, robusztus biztonsági intézkedéseket és folyamatos iterációt igényel. Strukturált meta prompt rendszerek alkalmazásával, a potenciális fenyegetések megértésével és mérséklési stratégiák alkalmazásával a fejlesztők biztonságos és hatékony MI ügynököket hozhatnak létre. Ezenkívül az ember a folyamatban megközelítés alkalmazása biztosítja, hogy az MI ügynökök a felhasználói igényekhez igazodjanak, miközben minimalizálják a kockázatokat. Ahogy az MI tovább fejlődik, a biztonság, az adatvédelem és az etikai szempontok proaktív kezelése kulcsfontosságú lesz a bizalom és a megbízhatóság fenntartásában az MI-alapú rendszerekben.

### További kérdéseid vannak a megbízható MI ügynökök létrehozásáról?

Csatlakozz az [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozz más tanulókkal, részt vegyél konzultációkon, és választ kapj az MI ügynökökkel kapcsolatos kérdéseidre.

## További források

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Felelős MI áttekintés</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatív MI modellek és alkalmazások értékelése</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Biztonsági rendszerüzenetek</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kockázatértékelési sablon</a>

## Előző lecke

[Agentic RAG](../05-agentic-rag/README.md)

## Következő lecke

[Tervezési minta](../07-planning-design/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.