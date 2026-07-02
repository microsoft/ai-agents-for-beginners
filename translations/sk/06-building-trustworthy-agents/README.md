[![Dôveryhodní AI agenti](../../../translated_images/sk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Tvorba dôveryhodných AI agentov

## Úvod

V tejto lekcii sa dozviete:

- Ako vytvárať a nasadzovať bezpečných a efektívnych AI agentov
- Dôležité bezpečnostné úvahy pri vývoji AI agentov
- Ako zabezpečiť ochranu údajov a súkromie používateľov pri vývoji AI agentov

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Identifikovať a zmierniť riziká pri vytváraní AI agentov
- Implementovať bezpečnostné opatrenia na správu údajov a prístupu
- Vytvárať AI agentov, ktorí zachovávajú súkromie údajov a poskytujú kvalitný používateľský zážitok

## Bezpečnosť

Najskôr sa pozrime na budovanie bezpečných agentných aplikácií. Bezpečnosť znamená, že AI agent funguje podľa návrhu. Ako tvorcovia agentných aplikácií máme metódy a nástroje na maximalizáciu bezpečnosti:

### Vytvorenie rámca systémovej správy

Ak ste už niekedy vytvárali AI aplikáciu pomocou veľkých jazykových modelov (LLM), viete, aké je dôležité navrhnúť robustný systémový prompt alebo systémovú správu. Tieto prompty stanovujú meta pravidlá, inštrukcie a usmernenia, ako bude LLM komunikovať s používateľom a údajmi.

Pre AI agentov je systémový prompt ešte dôležitejší, pretože AI agenti budú potrebovať veľmi špecifické inštrukcie na dokončenie úloh, ktoré sme pre nich navrhli.

Na vytvorenie škálovateľných systémových promptov môžeme použiť rámec systémovej správy na vytváranie jedného alebo viacerých agentov v našej aplikácii:

![Vytvorenie rámca systémovej správy](../../../translated_images/sk/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvorte meta systémovú správu

Meta prompt bude použitý LLM na generovanie systémových promptov pre agentov, ktorých vytvoríme. Navrhujeme ho ako šablónu, aby sme mohli efektívne vytvárať viac agentov podľa potreby.

Tu je príklad meta systémovej správy, ktorú by sme dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvorte základný prompt

Ďalším krokom je vytvoriť základný prompt na popis AI agenta. Mali by ste zahrnúť úlohu agenta, úlohy, ktoré agent vykoná, a akékoľvek ďalšie zodpovednosti agenta.

Tu je príklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnite základnú systémovú správu LLM

Teraz môžeme optimalizovať túto systémovú správu tým, že poskytneme meta systémovú správu ako systémovú správu a náš základný systémový prompt.

Výsledkom bude systémová správa, ktorá je lepšie navrhnutá na riadenie našich AI agentov:

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

Hodnota tohto rámca systémových správ spočíva v možnosti ľahšie škálovať vytváranie systémových správ pre viac agentov a tiež v priebežnom zlepšovaní vašich správ. Zriedkavo máte systémovú správu, ktorá funguje hneď na prvýkrát pre váš kompletný prípad použitia. Možnosť robiť malé úpravy a zlepšenia zmenou základnej systémovej správy a ich spracovaním cez systém vám umožní porovnávať a vyhodnocovať výsledky.

## Pochopenie hrozieb

Na vytvorenie dôveryhodných AI agentov je dôležité pochopiť a zmierniť riziká a hrozby pre váš AI agent. Pozrime sa na niektoré rôzne hrozby pre AI agentov a ako sa na ne môžete lepšie pripraviť.

![Pochopenie hrozieb](../../../translated_images/sk/understanding-threats.89edeada8a97fc0f.webp)

### Úlohy a inštrukcie

**Popis:** Útočníci sa snažia zmeniť inštrukcie alebo ciele AI agenta pomocou promptovania alebo manipulácie vstupov.

**Zmiernenie:** Vykonávajte overovacie kontroly a filtre vstupov na detekciu potenciálne nebezpečných promptov pred ich spracovaním AI agentom. Keďže tieto útoky zvyčajne vyžadujú častú interakciu s agentom, obmedzenie počtu ťahov v konverzácii je ďalším spôsobom, ako tomuto typu útokov predchádzať.

### Prístup k kritickým systémom

**Popis:** Ak AI agent má prístup k systémom a službám, ktoré uchovávajú citlivé údaje, útočníci môžu kompromitovať komunikáciu medzi agentom a týmito službami. Môže ísť o priame útoky alebo nepriame pokusy získať informácie o týchto systémoch cez agenta.

**Zmiernenie:** AI agenti by mali mať prístup k systémom iba na základe potreby, aby sa zabránilo týmto typom útokov. Komunikácia medzi agentom a systémom by mala byť tiež zabezpečená. Implementácia autentifikácie a kontroly prístupu je ďalším spôsobom ochrany týchto údajov.

### Preťaženie zdrojov a služieb

**Popis:** AI agenti môžu pristupovať k rôznym nástrojom a službám na vykonávanie úloh. Útočníci môžu využiť túto schopnosť na útok na tieto služby zasielaním vysokého počtu požiadaviek prostredníctvom AI agenta, čo môže viesť k zlyhaniam systémov alebo vysokým nákladom.

**Zmiernenie:** Implementujte pravidlá na obmedzenie počtu požiadaviek, ktoré môže AI agent zaslať službe. Obmedzenie počtu ťahov v konverzácii a požiadaviek na váš AI agent je ďalším spôsobom prevencie týchto útokov.

### Otrava vedomostnej databázy

**Popis:** Tento typ útoku nemieri priamo na AI agenta, ale na vedomostnú databázu a ďalšie služby, ktoré AI agent používa. Môže ísť o korupciu dát alebo informácií, ktoré AI agent použije na vykonanie úlohy, čo vedie k zaujatým alebo neželaným odpovediam používateľovi.

**Zmiernenie:** Pravidelne overujte údaje, ktoré AI agent používa vo svojich pracovných postupoch. Zabezpečte, aby bol prístup k týmto údajom bezpečný a menili ich iba dôveryhodné osoby, aby ste predišli tomuto typu útokov.

### Kaskádové chyby

**Popis:** AI agenti pristupujú k rôznym nástrojom a službám na vykonávanie úloh. Chyby spôsobené útočníkmi môžu viesť k zlyhaniu iných systémov, ku ktorým je AI agent pripojený, čím sa útok rozšíri a ťažšie diagnostikuje.

**Zmiernenie:** Jednou z metód je nechať AI agenta pracovať v obmedzenom prostredí, napríklad vykonávať úlohy v Docker kontejnery, aby sa zabránilo priamym útokom na systém. Vytvorenie záložných mechanizmov a logiky opätovného pokusu, keď určité systémy odpovedia chybou, je ďalším spôsobom, ako predísť vážnejším zlyhaniam systému.

## Človek v procese

Ďalším účinným spôsobom, ako vytvoriť dôveryhodné AI agentné systémy, je použitie prístupu Človek v procese (Human-in-the-loop). Tento prístup vytvára tok, kde môžu používatelia počas behu poskytovať spätnú väzbu agentom. Používatelia v podstate pôsobia ako agenti v multi-agentnom systéme a poskytujú schválenie alebo ukončenie bežiaceho procesu.

![Človek v procese](../../../translated_images/sk/human-in-the-loop.5f0068a678f62f4f.webp)

Tu je ukážka kódu používajúceho Microsoft Agent Framework, ktorá ukazuje, ako je tento koncept implementovaný:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvorte poskytovateľa so schválením človekom v procese
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Vytvorte agenta s krokom schválenia človekom
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Používateľ môže preskúmať a schváliť odpoveď
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Záver

Tvorba dôveryhodných AI agentov vyžaduje dôkladný návrh, robustné bezpečnostné opatrenia a neustálu iteráciu. Implementáciou štruktúrovaných meta-prompt systémov, pochopením potenciálnych hrozieb a aplikáciou zmierňujúcich stratégií môžu vývojári vytvárať AI agentov, ktorí sú bezpeční a efektívni. Okrem toho začlenenie prístupu človek v procese zabezpečuje, že AI agenti zostanú v súlade s potrebami používateľov a zároveň minimalizujú riziká. Ako sa AI ďalej vyvíja, udržiavanie proaktívneho prístupu k bezpečnosti, ochrane súkromia a etickým otázkam bude kľúčom k budovaniu dôvery a spoľahlivosti v systémoch riadených AI.

## Ukážky kódu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Krok za krokom demonštrácia rámca meta-prompt systémových správ.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Schvaľovacie brány pred akciou, rizikové úrovne a auditné protokolovanie pre dôveryhodných agentov.

### Máte ďalšie otázky o tvorbe dôveryhodných AI agentov?

Pripojte sa k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde sa stretnete s ďalšími študentmi, zúčastnite sa konzultácií a získajte odpovede na vaše otázky o AI agentoch.

## Dodatočné zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prehľad zodpovedného používania AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI modelov a AI aplikácií</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostné systémové správy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablóna hodnotenia rizík</a>

## Predchádzajúca lekcia

[Agentic RAG](../05-agentic-rag/README.md)

## Nasledujúca lekcia

[Plánovací vzor návrhu](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->