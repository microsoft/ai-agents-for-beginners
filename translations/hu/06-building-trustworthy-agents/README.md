[![Megbízható MI ágensek](../../../translated_images/hu/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

# Megbízható MI ügynökök létrehozása

## Bevezetés

Ez a lecke a következőket fogja lefedni:

- Hogyan lehet biztonságos és hatékony MI ügynököket létrehozni és telepíteni
- Fontos biztonsági megfontolások az MI ügynökök fejlesztése során.
- Hogyan őrizhetjük meg az adatok és a felhasználók magánéletét az MI ügynökök fejlesztésekor.

## Tanulási célok

A lecke elvégzése után tudni fogja, hogyan:

- Azonosítsa és mérsékelje a kockázatokat MI ügynökök létrehozásakor.
- Biztonsági intézkedéseket vezessen be az adatok és a hozzáférés megfelelő kezelése érdekében.
- Olyan MI ügynököket hozzon létre, amelyek megőrzik az adatvédelmet és minőségi felhasználói élményt nyújtanak.

## Biztonság

Először nézzük meg, hogyan lehet biztonságos ügynöki alkalmazásokat építeni. A biztonság azt jelenti, hogy az MI ügynök a terveinek megfelelően működik. Ügynöki alkalmazások építőiként rendelkezünk módszerekkel és eszközökkel a biztonság maximalizálására:

### Rendszerüzenet keretrendszer építése

Ha valaha is épített már MI alkalmazást Nagy Nyelvi Modellek (LLM-ek) használatával, akkor tudja, milyen fontos egy robusztus rendszerüzenet vagy rendszer parancs létrehozása. Ezek az üzenetek megállapítják a meta szabályokat, utasításokat és irányelveket arra, hogy az LLM hogyan fog kommunikálni a felhasználóval és az adatokkal.

Az MI ügynökök esetében a rendszerüzenet még fontosabb, mivel az ügynököknek rendkívül specifikus utasításokra lesz szükségük a feladatok elvégzéséhez, amelyeket számukra terveztünk.

Skálázható rendszerüzenetek létrehozásához használhatunk egy rendszerüzenet-keretrendszert az alkalmazásunkban egy vagy több ügynök építéséhez:

![Rendszerüzenet keretrendszer építése](../../../translated_images/hu/system-message-framework.3a97368c92d11d68.webp)

#### 1. lépés: Meta rendszerüzenet létrehozása

A meta parancsot egy LLM fogja használni az általunk létrehozott ügynökök rendszerüzeneteinek generálásához. Ezt sablonként tervezzük, hogy hatékonyan tudjunk több ügynököt létrehozni, ha szükséges.

Íme egy példa egy meta rendszerüzenetre, amelyet az LLM-nek adnánk:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 2. lépés: Alap parancs létrehozása

A következő lépés egy alap parancs létrehozása az MI ügynök leírására. Tartalmaznia kell az ügynök szerepét, a teljesítendő feladatokat és az ügynök egyéb felelősségeit.

Íme egy példa:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 3. lépés: Alap rendszerüzenet megadása az LLM-nek

Most optimalizálhatjuk ezt a rendszerüzenetet azáltal, hogy a meta rendszerüzenetet adjuk meg rendszerüzenetként az alap rendszerüzenet mellett.

Ez egy jobb tervezésű rendszerüzenetet fog eredményezni, amely irányítja MI ügynökeinket:

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

#### 4. lépés: Ismétlés és fejlesztés

Ennek a rendszerüzenet-keretrendszernek az értéke abban rejlik, hogy könnyebbé teszi a rendszerüzenetek létrehozását több ügynökhöz és idővel javítható a rendszerüzenet. Ritka, hogy egy rendszerüzenet elsőre tökéletesen működjön a teljes felhasználási esethez. Az alap rendszerüzenet kismértékű módosítása és a rendszer futtatása lehetővé teszi az eredmények összehasonlítását és értékelését.

## A fenyegetések megértése

Ahhoz, hogy megbízható MI ügynököket építsünk, fontos megérteni és csökkenteni az MI ügynököt fenyegető kockázatokat és veszélyeket. Nézzünk meg néhány fenyegetést az MI ügynökökkel szemben, és hogyan lehet jobban tervezni és felkészülni ezekre.

![A fenyegetések megértése](../../../translated_images/hu/understanding-threats.89edeada8a97fc0f.webp)

### Feladat és utasítás

**Leírás:** A támadók megpróbálják megváltoztatni az MI ügynök utasításait vagy céljait promptolás vagy bemenetek manipulálása révén.

**Mérséklés:** Érvényesítési ellenőrzéseket és bemeneti szűrőket kell alkalmazni a potenciálisan veszélyes promptok felismerésére, mielőtt azokat az MI ügynök feldolgozná. Mivel ezek a támadások általában gyakori interakciót igényelnek az ügynökkel, a beszélgetések fordulóinak korlátozása is segíthet megelőzni ezeket a támadásokat.

### Kritikus rendszerekhez való hozzáférés

**Leírás:** Ha egy MI ügynök hozzáfér rendszerekhez és szolgáltatásokhoz, amelyek érzékeny adatokat tárolnak, a támadók megszerezhetik az ügynök és a rendszerek közötti kommunikációt. Ezek lehetnek közvetlen támadások vagy közvetett információszerzési próbálkozások az ügynökön keresztül.

**Mérséklés:** Az MI ügynökök csak szükség szerinti hozzáféréssel rendelkezzenek a rendszerekhez, hogy megelőzzék az ilyen támadásokat. Az ügynök és a rendszer közötti kommunikációnak is biztonságosnak kell lennie. Hitelesítés és hozzáférés-szabályozás bevezetése az információ védelmére.

### Erőforrás- és szolgáltatás túlterhelése

**Leírás:** Az MI ügynökök különböző eszközökhöz és szolgáltatásokhoz férhetnek hozzá a feladatok elvégzéséhez. A támadók ezt kihasználva nagy mennyiségű kérelmet küldhetnek az MI ügynökön keresztül, ami rendszerleállásokhoz vagy magas költségekhez vezethet.

**Mérséklés:** Szabályzatokat kell bevezetni a szolgáltatásokhoz történő kérelmek számának korlátozására. A beszélgetések fordulóinak és a kérelmek számának korlátozása az MI ügynök esetében is hatékony módszer az ilyen támadások megelőzésére.

### Tudásbázis szennyezése

**Leírás:** Ez a típusú támadás nem közvetlenül az MI ügynökre irányul, hanem a tudásbázisra és egyéb szolgáltatásokra, amelyeket az MI ügynök használ majd. Ez magában foglalhatja az adatok vagy információk megsértését, amelyeket az MI ügynök a feladat elvégzéséhez használ, ami elfogult vagy nem kívánt válaszokat eredményezhet a felhasználónak.

**Mérséklés:** Rendszeres adatellenőrzéseket kell végezni azokon az adatokon, amelyeket az MI ügynök a munkafolyamataiban használ. Biztosítani kell, hogy ezekhez az adatokhoz csak megbízható személyek férjenek hozzá, és csak ők módosíthassák azokat az ilyen támadások elkerülése érdekében.

### Végeláthatatlan hibák

**Leírás:** Az MI ügynök különféle eszközökhöz és szolgáltatásokhoz fér hozzá a feladatok elvégzéséhez. A támadók által okozott hibák más rendszerek hibáihoz vezethetnek, amelyekhez az MI ügynök kapcsolódik, így a támadás szélesebb körűvé és nehezebben kezelhetővé válhat.

**Mérséklés:** Egy módszer ennek elkerülésére, ha az MI ügynök korlátozott környezetben működik, például Docker konténerben végez feladatokat, ezzel megakadályozva a közvetlen rendszer támadásokat. Vészhívó mechanizmusok és újbóli próbálkozási logika kialakítása, ha bizonyos rendszerek hibával válaszolnak, szintén segít megelőzni a nagyobb rendszerhibákat.

## Ember a folyamatban

Egy másik hatékony módja megbízható MI ügynökrendszerek létrehozásának az ember bevonása a folyamatba. Ez egy olyan folyamatot hoz létre, ahol a felhasználók visszajelzést adhatnak az ügynököknek a működés közben. A felhasználók lényegében ügynökként működnek egy több ügynökös rendszerben, és jóváhagyást vagy a folyamat megszakítását biztosítják.

![Ember a folyamatban](../../../translated_images/hu/human-in-the-loop.5f0068a678f62f4f.webp)

Íme egy kódrészlet a Microsoft Agent Framework használatával, amely bemutatja, hogyan valósul meg ez a koncepció:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Hozd létre a szolgáltatót emberi jóváhagyással
provider = AzureAIProjectAgentProvider(
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

Megbízható MI ügynökök építése gondos tervezést, robusztus biztonsági intézkedéseket és folyamatos ismétlést igényel. A strukturált meta prompt rendszerek megvalósításával, a potenciális fenyegetések megértésével és a mérséklési stratégiák alkalmazásával a fejlesztők biztonságos és hatékony MI ügynököket hozhatnak létre. Emellett az ember bevonása a folyamatba biztosítja, hogy az MI ügynökök összhangban maradjanak a felhasználói igényekkel, miközben minimalizálják a kockázatokat. Ahogy az MI tovább fejlődik, a proaktív hozzáállás a biztonsághoz, adatvédelemhez és etikai kérdésekhez kulcsfontosságú lesz a bizalom és megbízhatóság előmozdításához az MI-alapú rendszerekben.

## Példakódok

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Meta-prompt rendszerüzenet-keretrendszer lépésről lépésre.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Jóváhagyási kapuk előzetes műveletekhez, kockázati szintezés és audit naplózás megbízható ügynökök számára.

### Van még kérdése a megbízható MI ügynökök építéséről?

Csatlakozzon a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozzon más tanulókkal, részt vegyen konzultációkon, és válaszokat kapjon MI ügynökökkel kapcsolatos kérdéseire.

## További források

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Felelős MI áttekintés</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatív MI modellek és MI alkalmazások értékelése</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Biztonsági rendszerüzenetek</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Kockázatértékelési sablon</a>

## Előző lecke

[Ügynöki RAG](../05-agentic-rag/README.md)

## Következő lecke

[Tervtervezési mintázat](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->