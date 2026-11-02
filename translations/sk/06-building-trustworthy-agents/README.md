[![Dôveryhodní AI agenti](../../../translated_images/sk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

# Budovanie dôveryhodných AI agentov

## Úvod

Táto lekcia bude obsahovať:

- Ako vytvárať a nasadzovať bezpečných a efektívnych AI agentov
- Dôležité bezpečnostné aspekty pri vývoji AI agentov.
- Ako zachovať súkromie dát a používateľov pri vývoji AI agentov.

## Výučbové ciele

Po absolvovaní tejto lekcie budete vedieť:

- Identifikovať a zmierňovať riziká pri tvorbe AI agentov.
- Implementovať bezpečnostné opatrenia na správu dát a prístupov.
- Vytvárať AI agentov, ktorí zachovávajú súkromie dát a poskytujú kvalitný používateľský zážitok.

## Bezpečnosť

Najprv sa pozrime na budovanie bezpečných agentických aplikácií. Bezpečnosť znamená, že AI agent funguje podľa návrhu. Ako tvorcovia agentických aplikácií máme metódy a nástroje na maximalizáciu bezpečnosti:

### Budovanie rámca systémových správ

Ak ste už niekedy vytvárali AI aplikáciu využívajúcu veľké jazykové modely (LLM), viete, aký dôležitý je robustný systémový prompt alebo systémová správa. Tieto prompty stanovujú meta pravidlá, pokyny a usmernenia, ako bude LLM komunikovať s používateľom a dátami.

Pre AI agentov je systémový prompt ešte dôležitejší, pretože agenti potrebujú veľmi špecifické inštrukcie na vykonanie navrhnutých úloh.

Na vytváranie škálovateľných systémových promptov môžeme použiť rámec systémových správ na tvorbu jedného alebo viacerých agentov v našej aplikácii:

![Budovanie rámca systémových správ](../../../translated_images/sk/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvorte meta systémovú správu

Meta prompt bude použitý LLM na generovanie systémových promptov pre vytvárané agenty. Navrhujeme ho ako šablónu, aby sme mohli efektívne vytvárať viacerých agentov podľa potreby.

Tu je príklad meta systémovej správy, ktorú by sme poskytli LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvorte základný prompt

Ďalším krokom je vytvoriť základný prompt na opísanie AI agenta. Mali by ste uviesť rolu agenta, úlohy, ktoré agent vykoná, a ďalšie zodpovednosti agenta.

Tu je príklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnite základnú systémovú správu LLM

Teraz môžeme optimalizovať túto systémovú správu tým, že poskytneme meta systémovú správu a našu základnú systémovú správu.

Výsledkom bude systémová správa lepšie navrhnutá na usmerňovanie našich AI agentov:

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

Hodnota tohto rámca systémových správ spočíva v možnosti jednoduchšie škálovať tvorbu systémových správ pre viacerých agentov, ako aj zlepšovať systémové správy postupne v čase. Zriedka máte systémovú správu, ktorá funguje perfektne hneď na prvý raz pre celý váš prípad použitia. Možnosť robiť malé úpravy a zlepšenia tým, že zmeníte základnú systémovú správu a prebehnete ju systémom, vám umožní porovnať a vyhodnotiť výsledky.

## Pochopenie hrozieb

Na vytvorenie dôveryhodných AI agentov je dôležité pochopiť a zmierniť riziká a hrozby pre vášho AI agenta. Pozrime sa na niektoré z rôznych hrozieb voči AI agentom a ako sa na ne lepšie pripraviť.

![Pochopenie hrozieb](../../../translated_images/sk/understanding-threats.89edeada8a97fc0f.webp)

### Úloha a inštrukcie

**Popis:** Útočníci sa snažia zmeniť pokyny alebo ciele AI agenta prostredníctvom promptov alebo manipulácie vstupov.

**Zmiernenie:** Vykonávajte validačné kontroly a filtre vstupov na detekciu potenciálne nebezpečných promptov ešte pred ich spracovaním AI agentom. Pretože tieto útoky zvyčajne vyžadujú častú interakciu s agentom, obmedzenie počtu ťahov v konverzácii je ďalším spôsobom, ako tieto útoky zabrániť.

### Prístup ku kritickým systémom

**Popis:** Ak má AI agent prístup k systémom a službám, ktoré uchovávajú citlivé dáta, útočníci môžu ohroziť komunikáciu medzi agentom a týmito službami. Môžu to byť priame útoky alebo nepriame pokusy získať informácie o týchto systémoch cez agenta.

**Zmiernenie:** AI agenti by mali mať prístup k systémom len na báze potreby, aby sa zabránilo týmto typom útokov. Komunikácia medzi agentom a systémom by mala byť tiež zabezpečená. Implementácia autentifikácie a kontroly prístupov je ďalší spôsob ochrany týchto informácií.

### Preťaženie zdrojov a služieb

**Popis:** AI agenti môžu využívať rôzne nástroje a služby na plnenie úloh. Útočníci môžu využiť túto schopnosť na útok na tieto služby zasielaním vysokého objemu požiadaviek cez AI agenta, čo môže spôsobiť zlyhanie systému alebo vysoké náklady.

**Zmiernenie:** Implementujte pravidlá na obmedzenie počtu požiadaviek, ktoré môže AI agent smerovať na jednu službu. Obmedzenie počtu ťahov konverzácie a požiadaviek na AI agenta je ďalší spôsob, ako predchádzať týmto útokom.

### Otrava databázy znalostí

**Popis:** Tento typ útoku nie je cielene na AI agenta, ale na databázu znalostí a ďalšie služby, ktoré AI agent využíva. Môže ísť o poškodenie dát alebo informácií, ktoré AI agent použije na dokončenie úlohy, čo vedie k zaujatým alebo neúmyselným odpovediam používateľovi.

**Zmiernenie:** Pravidelne overujte dáta, ktoré AI agent používa vo svojich pracovných postupoch. Zabezpečte, že prístup k týmto dátam je bezpečný a menia ich iba dôveryhodné osoby, aby sa predišlo tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti majú prístup k rôznym nástrojom a službám na plnenie úloh. Chyby spôsobené útočníkmi môžu viesť k zlyhaniu ďalších systémov pripojených k AI agentovi, čo spôsobí rozšírenie útoku a sťaženie riešenia problémov.

**Zmiernenie:** Jednou z metód ako tomu zabrániť je, aby AI agent fungoval v obmedzenom prostredí, napríklad vykonávaním úloh v docker kontejnere, aby sa predišlo priamym útokom na systém. Vytvorenie záložných mechanizmov a opakovanie pokusov pri chybových odpovediach systémov je ďalší spôsob, ako predchádzať väčším zlyhaniam systému.

## Človek v slučke (Human-in-the-Loop)

Ďalším efektívnym spôsobom budovania dôveryhodných AI agentov je použitie konceptu človeka v slučke. To vytvára tok, kde môžu používatelia poskytovať spätnú väzbu agentom počas ich spúšťania. Používatelia v podstate pôsobia ako agenti v multi-agentnom systéme a poskytujú schválenie alebo ukončenie bežiaceho procesu.

![Človek v slučke](../../../translated_images/sk/human-in-the-loop.5f0068a678f62f4f.webp)

Tu je ukážka kódu využívajúca Microsoft Agent Framework, ktorá ukazuje implementáciu tohto konceptu:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Vytvorte poskytovateľa s ľudským schválením v procese
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Vytvorte agenta s krokom ľudského schválenia
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Používateľ môže skontrolovať a schváliť odpoveď
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Záver

Budovanie dôveryhodných AI agentov vyžaduje dôkladný dizajn, robustné bezpečnostné opatrenia a kontinuálne iterácie. Implementáciou štruktúrovaných meta-prompt systémov, pochopením potenciálnych hrozieb a nastavením zmierňujúcich stratégií môžu vývojári vytvoriť AI agentov, ktorí sú bezpeční a efektívni. Zahrnutie prístupu človeka v slučke zároveň zabezpečuje, že AI agenti zostanú v súlade s potrebami používateľov a minimalizujú riziká. Ako sa AI naďalej vyvíja, bude kľúčové udržiavať proaktívny prístup k bezpečnosti, súkromiu a etickým otázkam na podporu dôvery a spoľahlivosti AI poháňaných systémov.

## Ukážky kódu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Krok za krokom ukážka rámca meta-prompt systémových správ.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Schvaľovacie brány pred akciou, hodnotenie rizík a auditovanie pre dôveryhodných agentov.

### Máte ďalšie otázky o budovaní dôveryhodných AI agentov?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prehľad zodpovedného využívania AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI modelov a aplikácií</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostné systémové správy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablóna hodnotenia rizík</a>

## Predchádzajúca lekcia

[Agentický RAG](../05-agentic-rag/README.md)

## Nasledujúca lekcia

[Návrhový vzor plánovania](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->