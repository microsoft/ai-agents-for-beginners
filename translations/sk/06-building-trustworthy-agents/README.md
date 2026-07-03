[![Dôveryhodní AI agenti](../../../translated_images/sk/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Budovanie dôveryhodných AI agentov

## Úvod

Táto lekcia pokryje:

- Ako vytvárať a nasadzovať bezpečných a efektívnych AI agentov
- Dôležité bezpečnostné aspekty pri vývoji AI agentov.
- Ako udržiavať ochranu údajov a súkromia používateľov pri vývoji AI agentov.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Identifikovať a zmierniť riziká pri tvorbe AI agentov.
- Implementovať bezpečnostné opatrenia na zabezpečenie správnej správy údajov a prístupu.
- Vytvárať AI agentov, ktorí zachovávajú ochranu údajov a poskytujú kvalitný používateľský zážitok.

## Bezpečnosť

Najprv sa pozrime na budovanie bezpečných agentových aplikácií. Bezpečnosť znamená, že AI agent funguje podľa navrhnutého účelu. Ako tvorcovia agentových aplikácií máme metódy a nástroje na maximalizáciu bezpečnosti:

### Vytvorenie rámca systémovej správy (system message framework)

Ak ste už niekedy vytvárali AI aplikáciu používajúcu veľké jazykové modely (LLM), viete, aké dôležité je navrhnúť robustný systémový prompt alebo systémovú správu. Tieto prompty stanovujú meta pravidlá, inštrukcie a smernice, ako bude LLM komunikovať s používateľom a s údajmi.

Pre AI agentov je systémový prompt ešte dôležitejší, pretože AI agenti potrebujú veľmi špecifické inštrukcie na dokončenie úloh, ktoré sme pre nich navrhli.

Na vytváranie škálovateľných systémových promptov môžeme použiť rámec systémovej správy na tvorbu jedného alebo viacerých agentov v našej aplikácii:

![Building a System Message Framework](../../../translated_images/sk/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Vytvorte meta systémovú správu

Meta prompt bude použitý LLM na generovanie systémových promptov pre agentov, ktorých vytvoríme. Navrhujeme ho ako šablónu, aby sme mohli efektívne vytvoriť viac agentov podľa potreby.

Tu je príklad meta systémovej správy, ktorú by sme dali LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Vytvorte základný prompt

Ďalším krokom je vytvoriť základný prompt, ktorý popisuje AI agenta. Mali by ste zahrnúť úlohu agenta, úlohy, ktoré agent vykoná, a všetky ďalšie zodpovednosti agenta.

Tu je príklad:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Poskytnite základnú systémovú správu LLM

Teraz môžeme optimalizovať túto systémovú správu tým, že meta systémovú správu poskytneme ako systémovú správu spolu s našou základnou systémovou správou.

Tým vznikne systémová správa lepšie navrhnutá na usmerňovanie našich AI agentov:

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

#### Krok 4: Iterujte a vylepšujte

Hodnota tohto rámca systémovej správy spočíva v tom, že umožňuje jednoduchšie škálovanie tvorby systémových správ pre viacerých agentov a zároveň umožňuje časom vylepšovať vaše systémové správy. Je zriedkavé, že systémová správa na prvýkrát dokonale funguje pre váš celý prípad použitia. Možnosť robiť malé úpravy a vylepšenia zmenou základnej systémovej správy a jej prechodom cez systém vám umožní porovnávať a hodnotiť výsledky.

## Pochopenie hrozieb

Na vybudovanie dôveryhodných AI agentov je dôležité pochopiť a zmierniť riziká a hrozby voči vášmu AI agentovi. Pozrime sa na niektoré z rôznych hrozieb pre AI agentov a ako sa na ne lepšie pripraviť a plánovať ich zvládanie.

![Understanding Threats](../../../translated_images/sk/understanding-threats.89edeada8a97fc0f.webp)

### Úloha a inštrukcie

**Popis:** Útočníci sa pokúšajú zmeniť inštrukcie alebo ciele AI agenta prostredníctvom promptov alebo manipulácie vstupov.

**Zmierenie:** Vykonajte validačné kontroly a filtre vstupov, aby ste odhalili potenciálne nebezpečné prompty predtým, než ich AI agent spracuje. Keďže tieto útoky vyžadujú častú interakciu s agentom, obmedzenie počtu ťahov v konverzácii je ďalším spôsobom, ako takéto útoky zabrániť.

### Prístup ku kritickým systémom

**Popis:** Ak AI agent má prístup k systémom a službám, ktoré ukladajú citlivé údaje, útočníci môžu kompromitovať komunikáciu medzi agentom a týmito službami. Môžu to byť priame útoky alebo nepriame pokusy získať informácie o týchto systémoch cez agenta.

**Zmierenie:** AI agenti by mali mať prístup k systémom len na báze potreby, aby sa predišlo týmto útokom. Komunikácia medzi agentom a systémom by mala byť tiež zabezpečená. Implementácia autentifikácie a kontroly prístupu je ďalšou ochranou.

### Preťaženie zdrojov a služieb

**Popis:** AI agenti môžu pristupovať k rôznym nástrojom a službám na vykonávanie úloh. Útočníci môžu túto schopnosť zneužiť na útoky proti týmto službám zaslaním veľkého množstva požiadaviek cez AI agenta, čo môže spôsobiť zlyhania systému alebo vysoké náklady.

**Zmierenie:** Implementujte politiky na obmedzenie počtu požiadaviek, ktoré môže AI agent smerovať na službu. Obmedzenie počtu ťahov a požiadaviek na vášho AI agenta je ďalším spôsobom, ako takéto útoky zabrániť.

### Otrava znalostnej bázy

**Popis:** Tento typ útoku sa nepriamo zameriava na AI agenta, ale na jeho znalostnú bázu a iné služby, ktoré AI agent používa. Môže to znamenať poškodenie údajov alebo informácií, ktoré AI agent používa na vykonanie úlohy, čo môže viesť k zaujatým alebo nežiaducim odpovediam používateľovi.

**Zmierenie:** Pravidelne overujte údaje, ktoré AI agent používa vo svojich pracovných postupoch. Zabezpečte, aby k týmto údajom mal prístup len dôveryhodný personál a aby neboli neoprávnene menené, aby ste zabránili tomuto typu útoku.

### Kaskádové chyby

**Popis:** AI agenti pristupujú k rôznym nástrojom a službám na vykonanie úloh. Chyby spôsobené útočníkmi môžu viesť k zlyhaniu ďalších systémov, ku ktorým je AI agent pripojený, čo spôsobí, že útok sa rozšíri a je ťažšie ho odstrániť.

**Zmierenie:** Jednou z metód, ako tomu predísť, je prevádzka AI agenta v obmedzenom prostredí, napríklad vykonávanie úloh v Docker kontejnery, aby sa zabránilo priamym útokom na systém. Vytváranie záložných mechanizmov a logiky opakovania pri odpovedi systému s chybou je ďalšou ochranou proti väčším zlyhaniam systému.

## Človek v slučke (Human-in-the-Loop)

Ďalším efektívnym spôsobom, ako vytvárať dôveryhodné AI agentné systémy, je použitie konceptu Človek v slučke. Tento prístup vytvára tok, kde používatelia môžu poskytovať spätnú väzbu agentom počas behu. Používatelia v podstate pôsobia ako agenti v multi-agentnom systéme a poskytujú schválenie alebo ukončenie bežiaceho procesu.

![Human in The Loop](../../../translated_images/sk/human-in-the-loop.5f0068a678f62f4f.webp)

Tu je ukážka kódu využívajúca Microsoft Agent Framework, ktorá demonštruje implementáciu tohto konceptu:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvorte poskytovateľa so schválením človekom v procese
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Vytvorte agenta s krokem schválenia človekom
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

Budovanie dôveryhodných AI agentov si vyžaduje dôkladný návrh, robustné bezpečnostné opatrenia a neustále iterácie. Implementáciou štruktúrovaných systémov meta promptov, porozumením potenciálnych hrozieb a aplikovaním mitigácií môžu vývojári vytvoriť AI agentov, ktorí sú bezpeční a efektívni. Okrem toho, začlenenie človeka v slučke zabezpečuje, že AI agenti zostávajú zosúladení s potrebami používateľa a zároveň minimalizujú riziká. Ako sa AI naďalej vyvíja, udržiavanie proaktívneho prístupu k bezpečnosti, súkromiu a etickým otázkam bude kľúčom k budovaniu dôvery a spoľahlivosti AI systémov.

## Ukážky kódu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonštrácia krok za krokom rámca meta-prompt systémovej správy.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Brány schválenia pred akciou, segmentácia rizika a auditné logovanie pre dôveryhodných agentov.

### Máte ďalšie otázky o budovaní dôveryhodných AI agentov?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), stretnite sa s ďalšími študentmi, navštevujte konzultačné hodiny a získajte odpovede na svoje otázky týkajúce sa AI agentov.

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->