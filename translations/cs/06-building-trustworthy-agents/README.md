[![Důvěryhodní AI agenti](../../../translated_images/cs/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Tvorba důvěryhodných AI agentů

## Úvod

Tato lekce pokryje:

- Jak vytvořit a nasadit bezpečné a efektivní AI agenty
- Důležité bezpečnostní aspekty při vývoji AI agentů
- Jak udržovat ochranu dat a soukromí uživatelů při vývoji AI agentů

## Cíle učení

Po dokončení této lekce budete umět:

- Identifikovat a zmírnit rizika při vytváření AI agentů
- Implementovat bezpečnostní opatření k zajištění správné správy dat a přístupu
- Vytvářet AI agenty, kteří zachovávají ochranu dat a zajišťují kvalitní uživatelský zážitek

## Bezpečnost

Nejprve se podívejme na tvorbu bezpečných agentních aplikací. Bezpečnost znamená, že AI agent funguje tak, jak je navržený. Jako tvůrci agentních aplikací máme metody a nástroje pro maximalizaci bezpečnosti:

### Vytvoření rámce systémové zprávy

Pokud jste někdy vytvářeli AI aplikaci s použitím velkých jazykových modelů (LLM), znáte důležitost navržení robustního systémového promptu nebo systémové zprávy. Tyto promptové zprávy stanovují metapravidla, instrukce a pokyny, jak bude LLM komunikovat s uživatelem a daty.

Pro AI agenty je systémový prompt ještě důležitější, protože AI agenti budou potřebovat velmi specifické instrukce k dokončení úkolů, které jsme pro ně navrhli.

K vytvoření škálovatelných systémových promptů můžeme použít rámec systémové zprávy pro tvorbu jednoho či více agentů v naší aplikaci:

![Vytvoření rámce systémové zprávy](../../../translated_images/cs/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvoření metasytemové zprávy

Metaprompt bude použit LLM k generování systémových promptů pro agenty, které vytváříme. Navrhujeme ho jako šablonu, abychom mohli efektivně vytvořit více agentů, pokud je potřeba.

Zde je příklad metasytemové zprávy, kterou bychom dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvoření základního promptu

Dalším krokem je vytvoření základního promptu, který popisuje AI agenta. Měli byste uvést roli agenta, úkoly, které agent splní, a další odpovědnosti agenta.

Zde je příklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnutí základní systémové zprávy LLM

Nyní můžeme optimalizovat tuto systémovou zprávu tak, že poskytneme metasytemovou zprávu jako systémovou zprávu spolu s naší základní systémovou zprávou.

To vytvoří systémovou zprávu, která je lépe navržena pro řízení našich AI agentů:

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

#### Krok 4: Iterace a zlepšování

Hodnota tohoto rámce systémové zprávy je v možnosti snadněji škálovat tvorbu systémových zpráv z více agentů a také zlepšovat vaše systémové zprávy v čase. Je vzácné, že systémová zpráva poprvé perfektně vyhoví vašemu kompletnímu případu použití. Možnost provádět malé úpravy a vylepšení změnou základní systémové zprávy a její opětovné spuštění vám umožní porovnávat a vyhodnocovat výsledky.

## Porozumění hrozbám

Pro vytvoření důvěryhodných AI agentů je důležité rozumět a zmírňovat rizika a hrozby vůči vašemu AI agentovi. Podívejme se alespoň na některé z různých hrozeb AI agentům a jak se na ně lépe připravit.

![Porozumění hrozbám](../../../translated_images/cs/understanding-threats.89edeada8a97fc0f.webp)

### Úkol a instrukce

**Popis:** Útočníci se snaží změnit instrukce nebo cíle AI agenta pomocí promptování nebo manipulace s vstupy.

**Zmírnění:** Proveďte validační kontroly a filtry vstupů, abyste odhalili potenciálně nebezpečné promptové požadavky dříve, než je AI agent zpracuje. Jelikož tyto útoky obvykle vyžadují častou interakci s agentem, omezení počtu kol konverzace je dalším způsobem, jak zabránit těmto útokům.

### Přístup ke kritickým systémům

**Popis:** Pokud má AI agent přístup k systémům a službám, které ukládají citlivá data, útočníci mohou narušit komunikaci mezi agentem a těmito službami. Mohou jít o přímé útoky nebo nepřímé pokusy získat informace o těchto systémech prostřednictvím agenta.

**Zmírnění:** AI agenti by měli mít přístup k systémům jen na základě nezbytné potřeby, aby se zabránilo těmto typům útoků. Komunikace mezi agentem a systémem by měla být bezpečná. Implementace autentizace a řízení přístupu je dalším způsobem ochrany těchto informací.

### Přetížení zdrojů a služeb

**Popis:** AI agenti mohou používat různé nástroje a služby k dokončení úkolů. Útočníci mohou tuto schopnost využít k útoku na tyto služby posíláním vysokého objemu požadavků přes AI agenta, což může vést k selhání systémů nebo vysokým nákladům.

**Zmírnění:** Implementujte pravidla omezující počet požadavků, které může AI agent směrovat na službu. Omezení počtu kol konverzace a požadavků na AI agenta je také cestou, jak předejít těmto útokům.

### Kontaminace znalostní báze

**Popis:** Tento typ útoku není přímo zaměřen na AI agenta, ale na znalostní bázi a další služby, které AI agent využívá. Může jít o poškození dat nebo informace, které AI agent používá k dokončení úkolu, což vede k zaujatým nebo nechtěným odpovědím uživateli.

**Zmírnění:** Provádějte pravidelné ověřování dat, která AI agent používá ve svých pracovních postupech. Zajistěte, aby přístup k těmto datům byl bezpečný a měnili je pouze důvěryhodní jedinci, abyste předešli tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti používají různé nástroje a služby k dokončení úkolů. Chyby způsobené útočníky mohou vést k selhání dalším systémům, ke kterým je AI agent připojen, čímž se útok rozšíří a ztíží řešení problémů.

**Zmírnění:** Jednou z metod, jak tomu předejít, je provozovat AI agenta ve vymezeném prostředí, například v Docker kontejneru, aby se zabránilo přímým útokům na systém. Vytvoření záložních mechanismů a opakování pokusů, když některý systém oznámí chybu, je dalším způsobem, jak zabránit větším selháním.

## Člověk v procesu

Dalším účinným způsobem, jak vytvořit důvěryhodné AI agentní systémy, je použití člověka v procesu (Human-in-the-loop). To vytváří tok, kde uživatelé mohou během běhu poskytovat agentům zpětnou vazbu. Uživatelé vlastně fungují jako agenti v multiagentním systému a mohou schvalovat nebo ukončovat probíhající procesy.

![Člověk v procesu](../../../translated_images/cs/human-in-the-loop.5f0068a678f62f4f.webp)

Zde je ukázka kódu využívající Microsoft Agent Framework, která ukazuje, jak je tento koncept implementován:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Vytvořte poskytovatele s lidským schvalovacím krokem
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Vytvořte agenta se schvalovacím krokem člověka
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

Vytvoření důvěryhodných AI agentů vyžaduje pečlivý návrh, robustní bezpečnostní opatření a neustálé zlepšování. Implementací strukturovaných meta promptových systémů, porozuměním možným hrozbám a aplikací zmírňujících strategií mohou vývojáři vytvořit AI agenty, kteří jsou bezpeční i efektivní. Navíc začlenění člověka v procesu zajišťuje, že AI agenti zůstanou v souladu s potřebami uživatelů a zároveň minimalizují rizika. Jak AI pokračuje ve svém vývoji, udržování proaktivního přístupu k bezpečnosti, ochraně soukromí a etickým aspektům bude klíčem k budování důvěry a spolehlivosti v systémech řízených AI.

## Ukázky kódu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Podrobná ukázka rámce metapromptových systémových zpráv.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Schvalování před akcí, členění rizik a auditní záznamy pro důvěryhodné agenty.

### Máte další otázky ohledně tvorby důvěryhodných AI agentů?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), abyste se potkali s dalšími studenty, navštívili konzultační hodiny a získali odpovědi na své otázky o AI agentech.

## Další zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Přehled odpovědného využití AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnocení generativních AI modelů a AI aplikací</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostní systémové zprávy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablona hodnocení rizik</a>

## Předchozí lekce

[Agentní RAG](../05-agentic-rag/README.md)

## Další lekce

[Vzorový plánovací návrh](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->