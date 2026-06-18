[![Поверљиви AI агенти](../../../translated_images/sr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликните на слику изнад за гледање видео снимка овој лекцији)_

# Изградња поверљивих AI агената

## Увод

Ова лекција ће обухватити:

- Како изградити и применити безбедне и ефективне AI агенте
- Важна безбедносна разматрања приликом развоја AI агената.
- Како одржавати приватност података и корисника приликом развоја AI агената.

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Идентификујете и ублажите ризике приликом креирања AI агената.
- Имплементирате мере безбедности како бисте осигурали правилно управљање подацима и приступом.
- Креирате AI агенте који одржавају приватност података и пружају квалитетно корисничко искуство.

## Безбедност

Прво погледајмо изградњу безбедних агентских апликација. Безбедност значи да AI агент функционише онако како је замишљено. Као творци агентских апликација, имамо методе и алате за макармирање безбедности:

### Изградња оквира системске поруке

Ако сте икада изградили AI апликацију користећи велике језичке моделе (LLM), знате важност дизајнирања робусног системског упита или системске поруке. Ови упити успостављају мета правила, инструкције и смернице за начин на који ће се LLM повезивати са корисником и подацима.

За AI агенте, системски упит је још важнији јер ће AI агенти морати да имају врло специфичне инструкције за завршетак задатака које смо им задали.

Да бисмо направили скалабилне системске упите, можемо користити оквир системске поруке за изградњу једног или више агената у нашој апликацији:

![Изградња оквира системске поруке](../../../translated_images/sr/system-message-framework.3a97368c92d11d68.webp)

#### Корак 1: Креирајте мета системску поруку

Мета упит ће користити LLM за генерисање системских упита за агенте које креирамо. Дизајнирамо га као шаблон тако да можемо ефикасно креирати више агената по потреби.

Ево примера мета системске поруке коју бисмо дали LLM-у:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Корак 2: Направите основни упит

Следећи корак је да направите основни упит који описује AI агента. Требало би да укључује улогу агента, задатке које ће агент обављати и било које друге одговорности агента.

Ево примера:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Корак 3: Пружите основну системску поруку LLM-у

Сада можемо оптимизовати ову системску поруку тако што ћемо мета системску поруку користити као системску поруку и нашу основну системску поруку.

Ово ће произвести системску поруку боље дизајнирану за усмеравање наших AI агената:

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

#### Корак 4: Итерација и унапређење

Вредност овог оквира системске поруке је у томе што олакшава скалирање креирања системских порука више агената као и побољшање ваших системских порука током времена. Ретко када ћете имати системску поруку која од првог пута одговара вашем потпуном случају коришћења. Могућност да направите мале измене и побољшања мењањем основне системске поруке и његовим вођењем кроз систем омогућиће вам да упоредите и процените резултате.

## Разумевање претњи

Да бисте изградили поверљиве AI агенте, важно је разумети и ублажити ризике и претње вашем AI агенту. Погледајмо само неке од различитих претњи AI агентима и како можете боље планирати и припремити се за њих.

![Разумевање претњи](../../../translated_images/sr/understanding-threats.89edeada8a97fc0f.webp)

### Задатак и инструкције

**Опис:** Нападачи покушавају да промене инструкције или циљеве AI агента путем упита или манипулацијом улазних података.

**Ублажавање**: Извршите валидацијске провере и филтере улаза како бисте открили потенцијално опасне упите пре него што их AI агент обради. Пошто ови напади обично захтевају често интеракцију са агентом, ограничавање броја кругова у разговору је други начин да се спрече ове врсте напада.

### Приступ критичним системима

**Опис**: Ако AI агент има приступ системима и услугама које чувају поверљиве податке, нападачи могу компромитовати комуникацију између агента и тих услуга. Ово могу бити директни напади или индиректни покушаји да се преко агента добију информације о тим системима.

**Ублажавање**: AI агенти треба да имају приступ системима само по потреби да би се спречиле овакве врсте напада. Комуникација између агента и система такође треба бити безбедна. Имплементација аутентификације и контроле приступа је други начин да се заштите ове информације.

### Претерано оптерећење ресурса и услуга

**Опис:** AI агенти могу приступати различитим алатима и услугама како би обавили задатке. Нападачи могу искористити ову могућност да нападну те услуге слањем великог броја захтева преко AI агента, што може резултирати отказима система или високим трошковима.

**Ублажавање:** Имплементирајте политике које ограничавају број захтева које AI агент може упутити услузи. Ограничење броја кругова разговора и броја захтева ка вашем AI агенту је други начин да се спрече ове врсте напада.

### Зараза базе знања

**Опис:** Ова врста напада не циља директно AI агента већ базу знања и друге услуге које ће AI агент користити. Ово може укључивати корупцију података или информација које ће AI агент користити за обављање задатка, што доводи до пристрасних или нежељених одговора кориснику.

**Ублажавање:** Обављајте редовне провере података које ће AI агент користити у својим токовима рада. Осигурајте да приступ тим подацима буде безбедан и да могу бити мијењани само од стране поузданих особа како би се избегла ова врста напада.

### Каскадне грешке

**Опис:** AI агенти приступају разним алатима и услугама да би обавили задатке. Грешке изазване нападима могу довести до отказа других система на које је AI агент повезан, што узрокује да напад постане шире распрострањен и теже решив.

**Ублажавање**: Једна метода за избегавање овога је да AI агент ради у ограниченом окружењу, као што је извођење задатака у Docker контејнеру, да би се спречили директни напади на систем. Такође, стварање механизама за резервне опције и логике поновног покушаја када одређени системи одговоре грешком је други начин да се спрече већи откази система.

## Човек у петљи

Још један ефикасан начин за изградњу поверљивих система AI агената је коришћење приступа човек у петљи. Ово ствара ток у којем корисници могу пружити повратне информације агентима током њиховог рада. Корисници у суштини делују као агенти у мулти-агентском систему и пружају одобрење или прекид покренутог процеса.

![Човек у петљи](../../../translated_images/sr/human-in-the-loop.5f0068a678f62f4f.webp)

Ево пример кода који користи Microsoft Agent Framework да покаже како је овај концепт имплементиран:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Креирај провајдера са одобрењем човека у току процеса
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Креирај агента са кораком одобрења од стране човека
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Корисник може прегледати и одобрити одговор
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Закључак

Изградња поверљивих AI агената захтева пажљив дизајн, јаке безбедносне мере и континуирану итерацију. Имплементацијом структуираних мета упит система, разумевањем потенцијалних претњи и применом стратегија ублажавања, програмери могу створити AI агенте који су и безбедни и ефективни. Додатно, укључивање приступа човек у петљи осигурава да AI агенти остају усклађени са потребама корисника уз минимизирање ризика. Како AI наставља да се развија, одржавање проактивног става према безбедности, приватности и етичким аспектима биће кључно за изградњу поверења и поузданости у системима заснованим на AI.

## Примери кода

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Демонстрација корак по корак мета-система упита и системских порука.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Преглед празних капија за одобрење пре акције, нивоа ризика и дневника провере за поверљиве агенте.

### Имате још питања о изградњи поверљивих AI агената?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) за сусрет са другим студентима, учествовање у канцеларијским сатима и добијање одговора на питања о вашим AI агентима.

## Додатни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед одговорног коришћења AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Евалуација генеративних AI модела и AI апликација</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Безбедносне системске поруке</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Образац за процену ризика</a>

## Претходна лекција

[Agentic RAG](../05-agentic-rag/README.md)

## Следећа лекција

[Патерн планирања](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->