<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T20:37:54+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "sk"
}
-->
[![Dôveryhodní AI agenti](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.sk.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

# Budovanie dôveryhodných AI agentov

## Úvod

Táto lekcia pokryje:

- Ako vytvoriť a nasadiť bezpečných a efektívnych AI agentov.
- Dôležité bezpečnostné aspekty pri vývoji AI agentov.
- Ako zachovať ochranu údajov a súkromie používateľov pri vývoji AI agentov.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Identifikovať a zmierniť riziká pri vytváraní AI agentov.
- Implementovať bezpečnostné opatrenia na zabezpečenie správneho spravovania údajov a prístupu.
- Vytvoriť AI agentov, ktorí zachovávajú ochranu údajov a poskytujú kvalitný používateľský zážitok.

## Bezpečnosť

Najprv sa pozrime na budovanie bezpečných agentických aplikácií. Bezpečnosť znamená, že AI agent vykonáva úlohy tak, ako bolo navrhnuté. Ako tvorcovia agentických aplikácií máme metódy a nástroje na maximalizáciu bezpečnosti:

### Budovanie rámca systémových správ

Ak ste niekedy vytvárali AI aplikáciu pomocou veľkých jazykových modelov (LLMs), viete, aké dôležité je navrhnúť robustný systémový prompt alebo systémovú správu. Tieto prompty stanovujú meta pravidlá, pokyny a usmernenia pre interakciu LLM s používateľom a údajmi.

Pre AI agentov je systémový prompt ešte dôležitejší, pretože AI agenti potrebujú veľmi špecifické pokyny na splnenie úloh, ktoré sme pre nich navrhli.

Na vytvorenie škálovateľných systémových promptov môžeme použiť rámec systémových správ na budovanie jedného alebo viacerých agentov v našej aplikácii:

![Budovanie rámca systémových správ](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.sk.png)

#### Krok 1: Vytvorte meta systémovú správu

Meta prompt bude použitý LLM na generovanie systémových promptov pre agentov, ktorých vytvárame. Navrhujeme ho ako šablónu, aby sme mohli efektívne vytvoriť viacero agentov, ak je to potrebné.

Tu je príklad meta systémovej správy, ktorú by sme dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvorte základný prompt

Ďalším krokom je vytvorenie základného promptu na opísanie AI agenta. Mali by ste zahrnúť úlohu agenta, úlohy, ktoré agent vykoná, a akékoľvek ďalšie zodpovednosti agenta.

Tu je príklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnite základnú systémovú správu LLM

Teraz môžeme optimalizovať túto systémovú správu poskytnutím meta systémovej správy ako systémovej správy a našej základnej systémovej správy.

Tým sa vytvorí systémová správa, ktorá je lepšie navrhnutá na vedenie našich AI agentov:

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

#### Krok 4: Iterácia a zlepšenie

Hodnota tohto rámca systémových správ spočíva v tom, že umožňuje jednoduchšie škálovanie vytvárania systémových správ pre viacerých agentov, ako aj zlepšovanie vašich systémových správ v priebehu času. Je zriedkavé, že systémová správa funguje na prvýkrát pre celý váš prípad použitia. Možnosť vykonávať malé úpravy a zlepšenia zmenou základnej systémovej správy a jej spustením cez systém vám umožní porovnávať a hodnotiť výsledky.

## Pochopenie hrozieb

Na vytvorenie dôveryhodných AI agentov je dôležité pochopiť a zmierniť riziká a hrozby pre vášho AI agenta. Pozrime sa na niektoré z rôznych hrozieb pre AI agentov a ako sa na ne lepšie pripraviť.

![Pochopenie hrozieb](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.sk.png)

### Úloha a pokyny

**Popis:** Útočníci sa pokúšajú zmeniť pokyny alebo ciele AI agenta prostredníctvom promptov alebo manipulácie vstupov.

**Zmiernenie:** Vykonávajte validačné kontroly a filtre vstupov na detekciu potenciálne nebezpečných promptov pred ich spracovaním AI agentom. Keďže tieto útoky zvyčajne vyžadujú častú interakciu s agentom, obmedzenie počtu krokov v konverzácii je ďalším spôsobom, ako zabrániť týmto typom útokov.

### Prístup k kritickým systémom

**Popis:** Ak má AI agent prístup k systémom a službám, ktoré uchovávajú citlivé údaje, útočníci môžu kompromitovať komunikáciu medzi agentom a týmito službami. Môže ísť o priame útoky alebo nepriame pokusy získať informácie o týchto systémoch prostredníctvom agenta.

**Zmiernenie:** AI agenti by mali mať prístup k systémom iba na základe potreby, aby sa zabránilo týmto typom útokov. Komunikácia medzi agentom a systémom by mala byť tiež zabezpečená. Implementácia autentifikácie a kontroly prístupu je ďalším spôsobom ochrany týchto informácií.

### Preťaženie zdrojov a služieb

**Popis:** AI agenti môžu pristupovať k rôznym nástrojom a službám na splnenie úloh. Útočníci môžu využiť túto schopnosť na útok na tieto služby zaslaním veľkého množstva požiadaviek prostredníctvom AI agenta, čo môže viesť k zlyhaniu systému alebo vysokým nákladom.

**Zmiernenie:** Implementujte politiky na obmedzenie počtu požiadaviek, ktoré môže AI agent poslať službe. Obmedzenie počtu krokov v konverzácii a požiadaviek na vášho AI agenta je ďalším spôsobom, ako zabrániť týmto typom útokov.

### Otrava znalostnej bázy

**Popis:** Tento typ útoku nezasahuje priamo AI agenta, ale zameriava sa na znalostnú bázu a ďalšie služby, ktoré AI agent používa. Môže ísť o poškodenie údajov alebo informácií, ktoré AI agent používa na splnenie úlohy, čo vedie k zaujatým alebo neúmyselným odpovediam používateľovi.

**Zmiernenie:** Pravidelne overujte údaje, ktoré AI agent používa vo svojich pracovných postupoch. Zabezpečte, aby prístup k týmto údajom bol bezpečný a aby ich mohli meniť iba dôveryhodné osoby, aby sa zabránilo tomuto typu útoku.

### Reťazové chyby

**Popis:** AI agenti pristupujú k rôznym nástrojom a službám na splnenie úloh. Chyby spôsobené útočníkmi môžu viesť k zlyhaniu iných systémov, ku ktorým je AI agent pripojený, čo spôsobí, že útok sa stane rozsiahlejším a ťažšie riešiteľným.

**Zmiernenie:** Jednou z metód, ako sa tomu vyhnúť, je nechať AI agenta pracovať v obmedzenom prostredí, napríklad vykonávať úlohy v Docker kontejnere, aby sa zabránilo priamym útokom na systém. Vytvorenie záložných mechanizmov a logiky opakovania pri odpovedi určitých systémov chybou je ďalším spôsobom, ako zabrániť väčším zlyhaniam systému.

## Človek v procese

Ďalším efektívnym spôsobom, ako budovať dôveryhodné systémy AI agentov, je použitie človeka v procese. To vytvára tok, kde používatelia môžu poskytovať spätnú väzbu agentom počas ich činnosti. Používatelia v podstate pôsobia ako agenti v systéme s viacerými agentmi tým, že poskytujú schválenie alebo ukončenie bežiaceho procesu.

![Človek v procese](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.sk.png)

Tu je ukážka kódu pomocou AutoGen na ilustráciu, ako je tento koncept implementovaný:

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

## Záver

Budovanie dôveryhodných AI agentov si vyžaduje starostlivý dizajn, robustné bezpečnostné opatrenia a neustálu iteráciu. Implementáciou štruktúrovaných systémov meta promptov, pochopením potenciálnych hrozieb a aplikovaním stratégií zmiernenia môžu vývojári vytvárať AI agentov, ktorí sú bezpeční a efektívni. Navyše, začlenenie človeka do procesu zabezpečuje, že AI agenti zostávajú v súlade s potrebami používateľov a zároveň minimalizujú riziká. Ako sa AI ďalej vyvíja, udržiavanie proaktívneho prístupu k bezpečnosti, ochrane súkromia a etickým aspektom bude kľúčové pre podporu dôvery a spoľahlivosti v systémoch poháňaných AI.

### Máte ďalšie otázky o budovaní dôveryhodných AI agentov?

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ostatnými študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

## Dodatočné zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prehľad zodpovedného používania AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI modelov a AI aplikácií</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostné systémové správy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablóna hodnotenia rizík</a>

## Predchádzajúca lekcia

[Agentic RAG](../05-agentic-rag/README.md)

## Nasledujúca lekcia

[Plánovací dizajnový vzor](../07-planning-design/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.