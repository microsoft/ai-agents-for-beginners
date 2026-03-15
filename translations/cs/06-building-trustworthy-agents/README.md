[![Důvěryhodní AI agenti](../../../translated_images/cs/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Tvorba důvěryhodných AI agentů

## Úvod

Tato lekce pokryje:

- Jak vytvořit a nasadit bezpečné a efektivní AI agenty
- Důležitá bezpečnostní hlediska při vývoji AI agentů
- Jak zachovat ochranu dat a soukromí uživatelů při vývoji AI agentů

## Cíle učení

Po dokončení této lekce budete vědět, jak:

- Identifikovat a zmírnit rizika při vytváření AI agentů
- Implementovat bezpečnostní opatření k zajištění správné správy dat a přístupu
- Vytvořit AI agenty, kteří zachovávají soukromí dat a poskytují kvalitní uživatelský zážitek

## Bezpečnost

Nejprve se podívejme na tvorbu bezpečných agentních aplikací. Bezpečnost znamená, že AI agent funguje podle návrhu. Jako tvůrci agentních aplikací máme metody a nástroje k maximalizaci bezpečnosti:

### Vytvoření Frameworku pro systémové zprávy

Pokud jste někdy vytvářeli AI aplikaci pomocí velkých jazykových modelů (LLM), víte, jak důležité je navrhnout robustní systémový prompt nebo systémovou zprávu. Tyto prompty stanovují meta pravidla, instrukce a pokyny, jak bude LLM interagovat s uživatelem a daty.

Pro AI agenty je systémový prompt ještě důležitější, protože AI agenti budou potřebovat velmi specifické instrukce k dokončení úkolů, které jsme pro ně navrhli.

Pro vytvoření škálovatelných systémových promptů můžeme použít framework systémových zpráv k vytvoření jednoho nebo více agentů v naší aplikaci:

![Vytvoření Frameworku pro systémové zprávy](../../../translated_images/cs/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvoření meta systémové zprávy

Meta prompt bude použit LLM k generování systémových promptů pro agenty, které vytvoříme. Navrhneme ji jako šablonu, abychom mohli efektivně vytvářet více agentů podle potřeby.

Zde je příklad meta systémové zprávy, kterou bychom dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvoření základního promptu

Dalším krokem je vytvořit základní prompt, který popíše AI agenta. Měli byste zahrnout roli agenta, úkoly, které agent dokončí, a jakékoli jiné odpovědnosti agenta.

Zde je příklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnutí základní systémové zprávy LLM

Nyní můžeme tento systémový prompt optimalizovat tím, že poskytneme meta systémovou zprávu jako systémovou zprávu a naši základní systémovou zprávu.

To vytvoří systémovou zprávu, která je lépe navržena pro vedení našich AI agentů:

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

#### Krok 4: Iterace a zlepšení

Hodnota tohoto frameworku systémových zpráv spočívá v tom, že umožňuje lépe škálovat vytváření systémových zpráv pro více agentů a zároveň zlepšovat vaše systémové zprávy v průběhu času. Je vzácné, že budete mít systémovou zprávu, která funguje dokonale napoprvé pro váš kompletní použitý případ. Možnost provádět malé úpravy a zlepšení změnou základní systémové zprávy a jejím opakovaným spuštěním v systému vám umožní porovnat a vyhodnotit výsledky.

## Porozumění hrozbám

Pro vytvoření důvěryhodných AI agentů je důležité rozumět a zmírnit rizika a hrozby, kterým váš AI agent čelí. Podívejme se na několik různých hrozeb AI agentů a jak se na ně lépe připravit.

![Porozumění hrozbám](../../../translated_images/cs/understanding-threats.89edeada8a97fc0f.webp)

### Úkol a instrukce

**Popis:** Útočníci se snaží změnit instrukce nebo cíle AI agenta pomocí promptů nebo manipulace vstupů.

**Zmírnění:** Provádějte validační kontroly a filtry vstupů k detekci potenciálně nebezpečných promptů před tím, než jsou zpracovány AI agentem. Protože tyto útoky obvykle vyžadují častou interakci s agentem, omezení počtu kol v konverzaci je další způsob, jak tyto útoky zabránit.

### Přístup ke kritickým systémům

**Popis:** Pokud má AI agent přístup k systémům a službám, které uchovávají citlivá data, útočníci mohou ohrozit komunikaci mezi agentem a těmito službami. Mohou to být přímé útoky nebo nepřímé pokusy získat informace o těchto systémech prostřednictvím agenta.

**Zmírnění:** AI agenti by měli mít přístup k systémům pouze podle potřeby, aby se předešlo těmto útokům. Komunikace mezi agentem a systémem by měla být také zabezpečená. Implementace autentizace a řízení přístupu je dalším způsobem, jak tyto informace ochránit.

### Přetížení zdrojů a služeb

**Popis:** AI agenti mohou přistupovat k různým nástrojům a službám pro dokončení úkolů. Útočníci mohou tuto schopnost zneužít zasíláním velkého množství požadavků přes AI agenta, což může vést k selhání systému nebo vysokým nákladům.

**Zmírnění:** Zavádějte politiky omezení počtu požadavků, které může AI agent směřovat na službu. Omezení počtu kol konverzace a požadavků na AI agenta je dalším způsobem, jak těmto útokům zabránit.

### Otrava znalostní báze

**Popis:** Tento typ útoku není zaměřen přímo na AI agenta, ale na znalostní bázi a další služby, které AI agent používá. Může jít o poškození dat nebo informací, které AI agent použije k dokončení úkolu, což vede k zaujatým nebo nechtěným odpovědím uživateli.

**Zmírnění:** Provádějte pravidelné ověřování dat, která AI agent používá ve svých pracovních postupech. Zajistěte, aby přístup k těmto datům byl zabezpečený a aby je měnily pouze důvěryhodné osoby, což pomůže předejít tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti přistupují k různým nástrojům a službám k dokončení úkolů. Chyby způsobené útočníky mohou vést k selháním dalších systémů, ke kterým je AI agent připojen, což způsobí, že útok se rozšíří a je obtížnější jej řešit.

**Zmírnění:** Jednou z metod, jak tomu zabránit, je provozovat AI agenta v omezeném prostředí, například vykonávat úkoly v Docker kontejneru, aby se zabránilo přímým útokům na systém. Vytvoření záložních mechanismů a logiky opakování při chybové odpovědi některých systémů je dalším způsobem, jak zabránit větším selháním systému.

## Člověk v procesu

Dalším efektivním způsobem, jak vytvořit důvěryhodné AI agentní systémy, je použití přístupu Člověk v procesu. To vytvoří tok, kde uživatelé mohou během běhu poskytovat zpětnou vazbu agentům. Uživatelé v podstatě fungují jako agenti v multiagentním systému a poskytují schválení nebo ukončení běžícího procesu.

![Člověk v procesu](../../../translated_images/cs/human-in-the-loop.5f0068a678f62f4f.webp)

Zde je ukázka kódu pomocí Microsoft Agent Framework, který ukazuje, jak je tento koncept implementován:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvořte poskytovatele s lidským schvalovacím krokem
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Vytvořte agenta s krokem lidského schválení
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Uživatel může zkontrolovat a schválit odpověď
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Závěr

Vytváření důvěryhodných AI agentů vyžaduje pečlivý návrh, robustní bezpečnostní opatření a kontinuální iterace. Implementací strukturovaných systémů meta-promptu, porozuměním potenciálním hrozbám a aplikací strategií zmírnění mohou vývojáři vytvářet AI agenty, kteří jsou bezpeční i efektivní. Navíc začlenění přístupu s člověkem v procesu zajišťuje, že AI agenti zůstávají sladěni s potřebami uživatelů a zároveň minimalizují rizika. Jak se AI dále vyvíjí, udržování proaktivního postoje k bezpečnosti, ochraně soukromí a etickým otázkám bude klíčové pro podporu důvěryhodnosti a spolehlivosti systémů řízených AI.

### Máte další otázky ohledně tvorby důvěryhodných AI agentů?

Připojte se na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se setkáte s ostatními studenty, zúčastníte se konzultačních hodin a získáte odpovědi na své otázky o AI agentech.

## Další zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Přehled odpovědného používání AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnocení generativních AI modelů a AI aplikací</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostní systémové zprávy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablona posouzení rizik</a>

## Předchozí lekce

[Agentic RAG](../05-agentic-rag/README.md)

## Další lekce

[Vzory plánování](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nejsme odpovědní za jakákoliv nedorozumění nebo špatné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->