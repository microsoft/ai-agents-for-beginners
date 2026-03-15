[![Dôveryhodní AI agenti](../../../translated_images/sk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

# Budovanie dôveryhodných AI agentov

## Úvod

Táto lekcia pokryje:

- Ako vytvoriť a nasadiť bezpečných a efektívnych AI agentov
- Dôležité bezpečnostné úvahy pri vývoji AI agentov.
- Ako udržiavať ochranu údajov a súkromia používateľov pri vývoji AI agentov.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Identifikovať a zmierňovať riziká pri vytváraní AI agentov.
- Implementovať bezpečnostné opatrenia na zabezpečenie správneho spravovania údajov a prístupu.
- Vytvárať AI agentov, ktorí zachovávajú ochranu údajov a poskytujú kvalitný používateľský zážitok.

## Bezpečnosť

Najprv sa pozrime na budovanie bezpečných agentových aplikácií. Bezpečnosť znamená, že AI agent funguje podľa návrhu. Ako tvorcovia agentových aplikácií máme metódy a nástroje, ako maximalizovať bezpečnosť:

### Budovanie rámca systémovej správy

Ak ste už niekedy vytvárali AI aplikáciu využívajúcu veľké jazykové modely (LLM), viete, aký je dôležitý návrh robustného systémového príkazu alebo systémovej správy. Tieto príkazy ustanovujú meta pravidlá, inštrukcie a usmernenia pre to, ako bude LLM komunikovať s používateľom a údajmi.

Pre AI agentov je systémový príkaz ešte dôležitejší, pretože AI agenti budú potrebovať veľmi špecifické pokyny na dokončenie úloh, ktoré sme pre nich navrhli.

Na vytváranie škálovateľných systémových príkazov môžeme použiť rámec systémovej správy pre budovanie jedného alebo viacerých agentov v našej aplikácii:

![Budovanie rámca systémovej správy](../../../translated_images/sk/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvorte meta systémovú správu

Meta príkaz bude použitý LLM na generovanie systémových príkazov pre agentov, ktorých vytvárame. Navrhneme ho ako šablónu, aby sme mohli efektívne vytvárať viacerých agentov podľa potreby.

Tu je príklad meta systémovej správy, ktorú by sme zadali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvorte základný príkaz

Ďalším krokom je vytvoriť základný príkaz, ktorý popisuje AI agenta. Mali by ste zahrnúť úlohu agenta, úlohy, ktoré agent splní, a akékoľvek ďalšie zodpovednosti agenta.

Tu je príklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnite základnú systémovú správu LLM

Teraz môžeme tento systémový príkaz optimalizovať tak, že poskytneme meta systémovú správu ako systémovú správu spolu s našou základnou systémovou správou.

Toto vytvorí systémovú správu, ktorá je lepšie navrhnutá pre vedenie našich AI agentov:

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

#### Krok 4: Opakujte a zlepšujte

Hodnota tohto rámca systémovej správy spočíva v tom, že umožňuje ľahšie škálovanie vytvárania systémových príkazov od viacerých agentov, ako aj zlepšovanie systémových príkazov v priebehu času. Je zriedkavé, že budete mať systémovú správu, ktorá funguje hneď na prvýkrát pre váš kompletný prípad použitia. Možnosť robiť malé úpravy a vylepšenia zmenou základnej systémovej správy a jej prebehnutím cez systém vám umožní porovnávať a hodnotiť výsledky.

## Pochopenie hrozieb

Aby ste mohli vytvárať dôveryhodných AI agentov, je dôležité pochopiť a zmierniť riziká a hrozby pre váš AI agent. Pozrime sa na niektoré z rôznych hrozieb pre AI agentov a ako sa na ne lepšie pripraviť a plánovať ich zvládanie.

![Pochopenie hrozieb](../../../translated_images/sk/understanding-threats.89edeada8a97fc0f.webp)

### Úloha a inštrukcia

**Popis:** Útočníci sa snažia zmeniť inštrukcie alebo ciele AI agenta prostredníctvom promptovania alebo manipulácie so vstupmi.

**Zmiernenie:** Vykonávajte validačné kontroly a filtre vstupov na detekciu potenciálne nebezpečných promptov predtým, než sú spracované AI agentom. Pretože tieto útoky obyčajne vyžadujú častú interakciu s agentom, obmedzenie počtu koliesok v rozhovore je ďalším spôsobom, ako predísť týmto typom útokov.

### Prístup ku kritickým systémom

**Popis:** Ak má AI agent prístup k systémom a službám, ktoré ukladajú citlivé údaje, útočníci môžu kompromitovať komunikáciu medzi agentom a týmito službami. Môže ísť o priamy útok alebo nepriamy pokus získať informácie o týchto systémoch cez agenta.

**Zmiernenie:** AI agenti by mali mať prístup k systémom len na nevyhnutný účel, aby sa zabránilo týmto typom útokov. Komunikácia medzi agentom a systémom by tiež mala byť zabezpečená. Implementácia overovania a kontroly prístupu je ďalší spôsob, ako ochrániť tieto údaje.

### Preťaženie zdrojov a služieb

**Popis:** AI agenti môžu pristupovať k rôznym nástrojom a službám na dokončenie úloh. Útočníci môžu využiť túto schopnosť na útok na tieto služby tým, že cez AI agenta pošlú veľké množstvo žiadostí, čo môže viesť k zlyhaniu systému alebo vysokým nákladom.

**Zmiernenie:** Implementujte politiky na obmedzenie počtu požiadaviek, ktoré môže AI agent smerovať na službu. Obmedzenie počtu koliesok v rozhovore a žiadostí smerovaných na váš AI agent je ďalší spôsob, ako zabrániť týmto útokom.

### Otrava znalostnej databázy

**Popis:** Tento typ útoku cieli nie priamo na AI agenta, ale na znalostnú databázu a ďalšie služby, ktoré AI agent využíva. Môže to zahŕňať poškodenie údajov alebo informácií, ktoré AI agent použije na splnenie úlohy, čo vedie k zaujatým alebo neúmyselným odpovediam používateľovi.

**Zmiernenie:** Pravidelne overujte údaje, ktoré AI agent používa vo svojich pracovných postupoch. Zabezpečte, aby bol prístup k týmto údajom zabezpečený a aby ich menili len dôveryhodné osoby, aby ste sa vyhli tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti pristupujú k rôznym nástrojom a službám na vykonanie úloh. Chyby spôsobené útočníkmi môžu viesť k zlyhaniu ďalších systémov, ku ktorým je AI agent pripojený, čo spôsobuje, že útok sa rozšíri a je ťažšie ho vyriešiť.

**Zmiernenie:** Jednou z metód, ako sa tomu vyhnúť, je mať AI agenta fungujúceho v obmedzenom prostredí, napríklad vykonávanie úloh v Docker kontajneri, aby sa zabránilo priamym útokom na systém. Vytváranie záložných mechanizmov a logiky opakovaných pokusov, keď určité systémy odpovedia chybou, je ďalší spôsob, ako predísť rozsiahlejším zlyhaniam systému.

## Human-in-the-Loop

Ďalším efektívnym spôsobom, ako vytvárať dôveryhodné systémy AI agentov, je použitie konceptu Human-in-the-loop. To vytvára tok, kde používatelia môžu poskytovať spätnú väzbu agentom počas behu. Používatelia v podstate fungujú ako agenti v multiagentovom systéme a tým, že schvaľujú alebo ukončujú bežiaci proces.

![Human in The Loop](../../../translated_images/sk/human-in-the-loop.5f0068a678f62f4f.webp)

Tu je ukážka kódu využívajúca Microsoft Agent Framework, ktorá demonštruje, ako je tento koncept implementovaný:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvorte poskytovateľa so schválením človekom v slučke
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Vytvorte agenta s krokom schválenia človekom
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Používateľ môže odpoveď skontrolovať a schváliť
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Záver

Budovanie dôveryhodných AI agentov vyžaduje starostlivý návrh, robustné bezpečnostné opatrenia a neustálu iteráciu. Implementáciou štruktúrovaných systémov meta promptovania, pochopením potenciálnych hrozieb a aplikovaním stratégií zmierňovania rizík môžu vývojári vytvárať AI agentov, ktorí sú zároveň bezpeční a efektívni. Okrem toho začlenenie prístupu human-in-the-loop zabezpečuje, že AI agenti zostávajú v súlade s potrebami používateľov a zároveň minimalizujú riziká. Ako sa AI ďalej vyvíja, udržiavanie proaktívneho prístupu k bezpečnosti, ochrane súkromia a etickým úvahám bude kľúčom k budovaniu dôvery a spoľahlivosti v systémoch poháňaných AI.

### Máte ďalšie otázky o budovaní dôveryhodných AI agentov?

Pripojte sa k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na svoje otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Prehľad zodpovedného používania AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI modelov a AI aplikácií</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Bezpečnostné systémové správy</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Šablóna hodnotenia rizík</a>

## Predchádzajúca lekcia

[Agentický RAG](../05-agentic-rag/README.md)

## Nasledujúca lekcia

[Návrhový vzor plánovania](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->