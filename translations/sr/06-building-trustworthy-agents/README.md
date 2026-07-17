[![Поуздани AI агенти](../../../translated_images/sr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликните на слику изнад да бисте погледали видео овог часа)_

# Изградња поузданих AI агената

## Увод

Овај час ће обухватити:

- Како изградити и имплементирати безбедне и ефикасне AI агенте
- Важне безбедносне аспекте приликом развоја AI агената.
- Како одржавати приватност података и корисника током развоја AI агената.

## Циљеви учења

Након завршетка овог часа знаћете како да:

- Идентификујете и ублажите ризике приликом креирања AI агената.
- Спроведете безбедносне мере како бисте осигурали правилно управљање подацима и приступом.
- Креирате AI агенте који одржавају приватност података и пружају квалитетно корисничко искуство.

## Безбедност

Прво ћемо погледати изградњу безбедних агентских апликација. Безбедност значи да AI агент функционише онако како је дизајниран. Као творци агентских апликација, имамо методе и алате за максимизирање безбедности:

### Изградња система порука

Ако сте икада правили AI апликацију користећи Велике језичке моделе (LLM), знате колико је важно дизајнирати робусан системски упит или системску поруку. Ови упити постављају мета правила, инструкције и смернице како ће LLM комуницирати са корисником и подацима.

За AI агенте, системски упит је још важнији јер ће AI агенти требати врло специфичне инструкције да би завршили задатке које смо им дизајнирали.

Да бисмо креирали скалабилне системске упите, можемо користити оквир система порука за изградњу једног или више агената у нашој апликацији:

![Изградња система порука](../../../translated_images/sr/system-message-framework.3a97368c92d11d68.webp)

#### Корак 1: Креирање мета системске поруке

Мета упит ће LLM-у служити за генерисање системских упита за агенте које креирамо. Дизајнирамо га као шаблон како бисмо ефикасно могли направити више агената ако буде потребно.

Ево примера мета системске поруке коју бисмо дали LLM-у:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Корак 2: Креирање основног упита

Следећи корак је да направите основни упит који описује AI агента. Треба да укључите улогу агента, задатке које агент треба да заврши и све друге одговорности агента.

Ево примера:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Корак 3: Пружање основне системске поруке LLM-у

Сада можемо оптимизовати ову системску поруку тако што ћемо пружити мета системску поруку као системску поруку и нашу основну системску поруку.

Ово ће произвести системску поруку боље дизајнирану за вођење наших AI агената:

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

#### Корак 4: Итерација и побољшање

Вредност овог оквира система порука је у томе што омогућава лакше скалабилно креирање системских порука за више агената као и побољшање вашим системским порукама током времена. Ретко ће системска порука радити савршено од првог пута за цео случај употребе. Могућност малих измена и побољшања променом основне системске поруке и покретањем кроз систем омогућиће вам да упоредите и процените резултате.

## Разумевање претњи

Да бисте изградили поуздане AI агенте, важно је разумети и ублажити ризике и претње вашег AI агента. Погледајмо само неке од различитих претњи AI агентима и како боље планирати и припремити се за њих.

![Разумевање претњи](../../../translated_images/sr/understanding-threats.89edeada8a97fc0f.webp)

### Задатак и упутство

**Опис:** Нападачи покушавају да промене упутства или циљеве AI агента кроз упите или манипулисањем уносима.

**Ублажавање**: Извршите валидационе провере и филтре уноса да бисте открили потенцијално опасне упите пре него што их AI агент обради. Пошто овакви напади обично захтевају честу интеракцију са агентом, ограничавање броја разговора у разговору je додатни начин за спречавање ових напада.

### Приступ критичним системима

**Опис**: Ако AI агент има приступ системима и сервисима који чувају осетљиве податке, нападачи могу угрозити комуникацију између агента и тих сервиса. Ово могу бити директни напади или индиректни покушаји да се преко агента сазнају информације о тим системима.

**Ублажавање**: AI агенти треба да имају приступ системима само када је то неопходно да би се спречили овакви напади. Комуникација између агента и система такође мора бити безбедна. Спровођење аутентификације и контроле приступа још је један начин да се заштите ове информације.

### Превелико оптерећење ресурса и сервиса

**Опис:** AI агенти могу приступити различитим алатима и сервисима да заврше задатке. Нападачи могу злоупотребити ову способност тако што ће слати велики број захтева преко AI агента, што може довести до отказа система или високих трошкова.

**Ублажавање:** Успоставите политике које ограничавају број захтева које AI агент може упутити сервису. Ограничење броја разговора и захтева AI агенту је још један начин спречавања оваквих напада.

### Тровање базе знања

**Опис:** Овај тип напада не циља директно AI агента већ циља базу знања и друге сервисе које ће AI агент користити. То може обухватати корупцију података или информација које AI агент користи за извршавање задатка, што доводи до пристрасних или нежељених одговора кориснику.

**Ублажавање:** Редовно вршите проверу података које ће AI агент користити у својим процесима. Осигурајте да приступ овим подацима буде безбедан и да их могу мењати само поуздане особе како бисте избегли овакве нападе.

### Каскадне грешке

**Опис:** AI агенти приступају разним алатима и сервисима да би завршили задатке. Грешке изазване нападачима могу проузроковати отказе других система повезаних са AI агентом, што чини напад све распрострањенијим и теже решивим.

**Ублажавање**: Један начин да се ово избегне је да AI агент ради у ограниченом окружењу, као што је извођење задатака у Docker контејнеру, да би се спречили директни напади на систем. Креирање резервних механизама и логике за поновну покретање када одређени системи дају грешку је још један начин да се спрече већи откази система.

## Човек у петљи

Још један ефикасан начин изградње поузданих AI агентских система је коришћење концепта човек у петљи. Ово ствара ток у коме корисници могу пружити повратне информације агентима током извршавања. Корисници у суштини делују као агенти у мулти-агентском систему и дају одобрење или заустављају процес.

![Човек у петљи](../../../translated_images/sr/human-in-the-loop.5f0068a678f62f4f.webp)

Ево примера кода који користи Microsoft Agent Framework да покаже како се овај концепт имплементира:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Креирајте провајдера са одобрењем човека у циклусу
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Креирајте агента са кораком одобрења човека
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

Изградња поузданих AI агената захтева пажљив дизајн, робусне безбедносне мере и континуирано усавршавање. Спровођењем структурираних система мета упита, разумијевањем потенцијалних претњи и применом стратегија ублажавања, програмери могу креирати AI агенте који су безбедни и ефикасни. Додавање приступа човек у петљи осигурава да AI агенти остану усаглашени са потребама корисника уз минимизирање ризика. Kako AI наставља да се развија, одржавање проактивног става према безбедности, приватности и етичким разматрањима биће кључно за неговање поверења и поузданости у системима који покрећу AI.

## Примери кода

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Демонстрација корак по корак система мета упита.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Врата одобрења пре акције, класификација ризика и евиденција ревизија за поуздане агенте.

### Имате још питања о изградњи поузданих AI агената?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да упознате друге ученике, посетите канцеларијско време и добијете одговоре на ваша питања о AI агентима.

## Додатни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед одговорне употребе AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Евалуација генеративних AI модела и AI апликација</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Поруке безбедносног система</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Образац процене ризика</a>

## Претходни час

[Agentic RAG](../05-agentic-rag/README.md)

## Следећи час

[Дизајн шаблона планирања](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->