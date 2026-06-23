[![Důvěryhodní AI agenti](../../../translated_images/cs/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Vytváření důvěryhodných AI agentů

## Úvod

Tato lekce pokryje:

- Jak vytvořit a nasadit bezpečné a efektivní AI agenty
- Důležitá bezpečnostní opatření při vývoji AI agentů.
- Jak zachovat soukromí dat a uživatelů při vývoji AI agentů.

## Cíle učení

Po dokončení této lekce budete vědět, jak:

- Identifikovat a zmírnit rizika při tvorbě AI agentů.
- Implementovat bezpečnostní opatření pro správu dat a přístupů.
- Vytvářet AI agenty, kteří zachovávají soukromí dat a poskytují kvalitní uživatelský zážitek.

## Bezpečnost

Nejprve se podívejme na vytváření bezpečných agentních aplikací. Bezpečnost znamená, že AI agent funguje podle návrhu. Jako tvůrci agentních aplikací máme metody a nástroje, jak maximalizovat bezpečnost:

### Vytvoření rámce systémových zpráv

Pokud jste někdy vytvářeli AI aplikaci využívající Velké Jazykové Modely (LLM), víte, jak důležité je navrhnout robustní systémový prompt nebo systémovou zprávu. Tyto prompty stanovují meta pravidla, instrukce a pokyny, jak bude LLM komunikovat s uživatelem a daty.

U AI agentů je systémový prompt ještě důležitější, protože AI agenti potřebují velmi specifické instrukce k dokončení úkolů, které jsme pro ně navrhli.

Pro vytvoření škálovatelných systémových promptů můžeme použít rámec systémových zpráv pro tvorbu jednoho nebo více agentů v naší aplikaci:

![Vytvoření rámce systémových zpráv](../../../translated_images/cs/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvořte meta systémovou zprávu

Meta prompt bude použit LLM k vytvoření systémových promptů pro agenty, které vytváříme. Navrhneme ho jako šablonu, abychom mohli efektivně vytvářet více agentů podle potřeby.

Zde je příklad meta systémové zprávy, kterou dáme LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvořte základní prompt

Dalším krokem je vytvořit základní prompt, který popisuje AI agenta. Měli byste zahrnout roli agenta, úkoly, které agent bude plnit, a další odpovědnosti agenta.

Zde je příklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytněte základní systémovou zprávu LLM

Nyní můžeme tuto systémovou zprávu optimalizovat tím, že jako systémovou zprávu poskytneme meta systémovou zprávu a naši základní systémovou zprávu.

To vytvoří systémovou zprávu lépe navrženou pro vedení našich AI agentů:

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

#### Krok 4: Iterujte a zlepšujte

Hodnota tohoto rámce systémových zpráv spočívá v možnosti snadněji škálovat tvorbu systémových zpráv od více agentů, stejně jako vylepšovat vaše systémové zprávy v čase. Je vzácné, že budete mít systémovou zprávu, která funguje napoprvé pro váš kompletní případ použití. Možnost provádět malé úpravy a vylepšení změnou základní systémové zprávy a jejím zpracováním systémem vám umožní porovnat a vyhodnotit výsledky.

## Pochopení hrozeb

K vytvoření důvěryhodných AI agentů je důležité rozumět rizikům a hrozbám vůči vašemu AI agentovi a umět je zmírnit. Podívejme se jen na některé z různých hrozeb AI agentům a jak se na ně lépe připravit.

![Pochopení hrozeb](../../../translated_images/cs/understanding-threats.89edeada8a97fc0f.webp)

### Úkol a instrukce

**Popis:** Útočníci se snaží změnit instrukce nebo cíle AI agenta pomocí promptování nebo manipulace s vstupy.

**Zmírnění:** Provádějte validační kontroly a filtry vstupů k detekci potenciálně nebezpečných promptů před jejich zpracováním AI agentem. Protože tyto útoky obvykle vyžadují častou interakci s agentem, omezení počtu kol v konverzaci je dalším způsobem, jak těmto útokům předcházet.

### Přístup ke kritickým systémům

**Popis:** Pokud má AI agent přístup k systémům a službám, které ukládají citlivá data, útočníci mohou kompromitovat komunikaci mezi agentem a těmito službami. Mohou to být přímé útoky nebo nepřímé pokusy získat informace o těchto systémech skrze agenta.

**Zmírnění:** AI agenti by měli mít přístup k systémům pouze na základě potřeby, aby se těmto útokům zabránilo. Komunikace mezi agentem a systémem by měla být také zabezpečená. Implementace autentizace a kontroly přístupu je dalším způsobem, jak chránit tyto informace.

### Přetížení zdrojů a služeb

**Popis:** AI agenti mohou přistupovat k různým nástrojům a službám, aby vykonali úkoly. Útočníci mohou tuto schopnost zneužít k útokům na tyto služby tím, že prostřednictvím AI agenta pošlou velký objem požadavků, což může vést k selhání systému nebo vysokým nákladům.

**Zmírnění:** Implementujte politiky, které omezí počet požadavků, které může AI agent poslat službě. Omezení počtu konverzačních kol a požadavků na vašeho AI agenta je dalším způsobem, jak těmto útokům předcházet.

### Otrava znalostní báze

**Popis:** Tento typ útoku není zaměřen přímo na AI agenta, ale na znalostní bázi a další služby, které AI agent využívá. Může se jednat o korumpování dat nebo informací, které AI agent použije k vykonání úkolu, což vede ke zkresleným nebo nechtěným odpovědím uživateli.

**Zmírnění:** Provádějte pravidelnou verifikaci dat, která AI agent používá ve svých pracovních postupech. Zajistěte, aby přístup k těmto datům byl zabezpečený a měnili je pouze důvěryhodní lidé, aby se předešlo tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti přistupují k různým nástrojům a službám, aby vykonali úkoly. Chyby způsobené útočníky mohou vést k selhání dalším systémům, ke kterým je AI agent připojen, což způsobí rozsáhlejší útok a obtížnější řešení problémů.

**Zmírnění:** Jednou z možností, jak tomu předejít, je nechat AI agenta pracovat v omezeném prostředí, například vykonávat úkoly v Docker kontejneru, aby se zabránilo přímým útokům na systém. Vytvoření záložních mechanismů a logiky opakování, když určité systémy odpoví chybou, je dalším způsobem, jak zabránit větším systémovým poruchám.

## Člověk-v-cepě

Dalším účinným způsobem, jak vytvořit důvěryhodné systémy AI agentů, je použití člověka-v-cepě (Human-in-the-loop). To zajišťuje tok, kde uživatelé mohou poskytovat zpětnou vazbu agentům během běhu. Uživatelé v podstatě fungují jako agenti v multiagentním systému a schvalují nebo ukončují probíhající proces.

![Člověk-v-cepě](../../../translated_images/cs/human-in-the-loop.5f0068a678f62f4f.webp)

Zde je ukázka kódu používajícího Microsoft Agent Framework, která ukazuje, jak je tento koncept implementován:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvořte poskytovatele s lidským schvalováním
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Vytvořte agenta s krokem schválení člověkem
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Uživatel může odpověď zkontrolovat a schválit
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Závěr

Vytvoření důvěryhodných AI agentů vyžaduje pečlivý návrh, robustní bezpečnostní opatření a kontinuální iterace. Implementací strukturovaných systémů meta promptů, porozuměním potenciálním hrozbám a aplikací strategií zmírnění mohou vývojáři vytvářet AI agenty, kteří jsou zároveň bezpeční i efektivní. Navíc začlenění přístupu člověka-v-cepě zajišťuje, že AI agenti zůstávají v souladu s potřebami uživatelů při minimalizaci rizik. Jak AI pokračuje ve svém vývoji, zachování proaktivního přístupu k bezpečnosti, ochraně soukromí a etickým otázkám bude klíčové pro budování důvěry a spolehlivosti v systémech řízených AI.

## Ukázky kódu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Podrobná ukázka rámce systémových zpráv meta-promptu.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Předběžná schválení akcí, stanovení úrovně rizika a auditní protokolování pro důvěryhodné agenty.

### Máte více otázek ohledně vytváření důvěryhodných AI agentů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), abyste se setkali s dalšími studenty, zúčastnili se konzultačních hodin a získali odpovědi na vaše otázky ohledně AI agentů.

## Další zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Přehled odpovědného používání AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnocení generativních AI modelů a AI aplikací</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostní systémové zprávy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablona hodnocení rizik</a>

## Předchozí lekce

[Agentic RAG](../05-agentic-rag/README.md)

## Další lekce

[Vzory plánování](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->