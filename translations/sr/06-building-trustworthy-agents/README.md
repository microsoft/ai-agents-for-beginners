[![Поуздани AI агенти](../../../translated_images/sr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Изградња поузданих AI агената

## Увод

Ова лекција ће обухватити:

- Како изградити и поставити безбедне и ефикасне AI агенте
- Важне безбедносне аспекте приликом развоја AI агената.
- Како одржати приватност података и корисника приликом развоја AI агената.

## Циљеви учења

Након завршетка ове лекције, бићете у стању да:

- Идентификујете и ублажите ризике приликом креирања AI агената.
- Имплементирате безбедносне мере како бисте осигурали да су подаци и приступ правилно управљани.
- Креирате AI агенте који одржавају приватност података и пружају квалитетно корисничко искуство.

## Безбедност

Прво ћемо погледати изградњу безбедних агентних апликација. Безбедност значи да AI агент функционише како је осмишљено. Као творци агентних апликација, имамо методе и алате који максимизирају безбедност:

### Изградња оквира за системске поруке

Ако сте икада изградили AI апликацију користећи велике језичке моделе (LLMs), знате колико је важно дизајнирати робустан системски упит или системску поруку. Ови упити успостављају мета правила, инструкције и смернице за интеракцију LLM-а са корисником и подацима.

За AI агенте, системски упит је још важнији јер ће AI агенти требати врло специфичне инструкције како би завршили задатке које смо им дизајнирали.

Да бисмо креирали скалабилне системске упите, можемо користити оквир за системске поруке за изградњу једног или више агената у нашој апликацији:

![Изградња оквира за системске поруке](../../../translated_images/sr/system-message-framework.3a97368c92d11d68.webp)

#### Корак 1: Креирајте мета системску поруку

Мета упит ће користити LLM за генерисање системских упита за агенте које креирамо. Дизајнирамо га као шаблон како бисмо ефикасно могли креирати више агената по потреби.

Ево примера мета системске поруке коју бисмо дали LLM-у:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Корак 2: Креирајте основни упит

Следећи корак је креирање основног упита који описује AI агента. Треба да укључите улогу агента, задатке које ће агент извршити и све друге одговорности агента.

Ево примера:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Корак 3: Обезбедите основну системску поруку LLM-у

Сада можемо оптимизовати ову системску поруку тако што ћемо дати мета системску поруку као системску поруку и нашу основну системску поруку.

Ово ће произвести системску поруку која је боље осмишљена за вођење наших AI агената:

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

#### Корак 4: Понављајте и унапређујте

Вредност овог оквира системске поруке је у томе што је могуће лакше скалирати креирање системских порука од више агената као и унапређивати ваше системске поруке током времена. Ретко када ћете имати системску поруку која одмах ради за цео случај употребе. Могућност прављења малих подешавања и побољшања мењањем основне системске поруке и покретањем кроз систем омогућава вам поређење и процену резултата.

## Разумевање претњи

Да бисте изградили поуздане AI агенте, важно је разумети и ублажити ризике и претње вашим AI агентом. Погледајмо само неке од различитих претњи AI агенатима и како боље планирати и припремити се за њих.

![Разумевање претњи](../../../translated_images/sr/understanding-threats.89edeada8a97fc0f.webp)

### Задатак и инструкција

**Опис:** Нападачи покушавају да промене инструкције или циљеве AI агента преко упита или манипулације улазима.

**Ублажавање**: Извршавајте валидационе провере и филтере улаза да бисте детектовали потенцијално опасне упите пре него што их AI агент обради. Пошто ови напади обично захтевају честу интеракцију са агентом, ограничавање броја окрета у разговору још један је начин да се спрече ове врсте напада.

### Приступ критичним системима

**Опис**: Ако AI агент има приступ системима и сервисима који чувају осетљиве податке, нападачи могу компромитовати комуникацију између агента и ових сервиса. Ово могу бити директни напади или индиректни покушаји стицања информација о овим системима преко агента.

**Ублажавање**: AI агенти треба да имају приступ системима само по потреби да би се спречиле ове врсте напада. Комуникација између агента и система треба такође да буде безбедна. Имплементација аутентикације и контроле приступа је још један начин да се заштите ове информације.

### Преоптерећење ресурса и услуга

**Опис:** AI агенти могу приступати различитим алатима и услугама да обављају задатке. Нападачи могу искористити ову способност да нападну те сервисе слањем великог броја захтева преко AI агента, што може резултирати кваровима система или високим трошковима.

**Ублажавање:** Имплементирајте политике које ограничавају број захтева које AI агент може упутити сервису. Ограничавање броја окрета у разговору и захтева вашем AI агенту још је један начин да се спрече ове врсте напада.

### Тровање базе знања

**Опис:** Ова врста напада не циља директно AI агента већ базу знања и друге сервисе које ће AI агент користити. Ово може укључивати корумпирање података или информација које ће AI агент користити да обави задатак, што доводи до пристрасних или нежељених одговора кориснику.

**Ублажавање:** Редовно проверавајте податке које ће AI агент користити у својим токовима рада. Осигурајте да је приступ овим подацима безбедан и да их могу мењати само поуздане особе како бисте избегли ову врсту напада.

### Ланчане грешке

**Опис:** AI агенти приступају различитим алатима и сервисима да би завршили задатке. Грешке изазване нападачима могу довести до квара других система са којима је AI агент повезан, чиме напад постаје шире распрострањен и тежи за решавање.

**Ублажавање**: Један начин да се ово избегне је да AI агент ради у ограниченом окружењу, као што је извођење задатака у Docker контејнеру, како би се спречили директни напади на систем. Креирање резервних механизама и логике поновних покушаја када неки системи одговоре са грешком је још један начин заштите од већих кварова система.

## Човек у петљи

Један од ефикасних начина да се изграде поуздани AI агентни системи јесте коришћење човека у петљи (Human-in-the-Loop). Ово ствара ток у којем корисници могу да дају повратне информације агентима током извршавања. Корисници у суштини делују као агенти у мулти-агентном систему и пружају одобрење или прекид процеса у реалном времену.

![Човек у петљи](../../../translated_images/sr/human-in-the-loop.5f0068a678f62f4f.webp)

Ево и фрагмента кода који користи Microsoft Agent Framework да покаже како се овај концепт имплементира:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Креирајте провајдера са одобрењем човека у петљи
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Креирајте агента са кораком одобрења од стране човека
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

Изградња поузданих AI агената захтева пажљив дизајн, робусне безбедносне мере и континуиране итерације. Имплементацијом структуираних мета упитних система, разумевањем потенцијалних претњи и применом стратегија ублажавања, програмери могу креирати AI агенте који су безбедни и ефикасни. Поред тога, коришћење човека у петљи обезбеђује да AI агенти остану у складу са потребама корисника уз минимизирање ризика. Како AI наставља да се развија, одржавање проактивног става према безбедности, приватности и етичким аспектима биће кључно за изградњу поверења и поузданости у системима вођеним вештачком интелигенцијом.

### Имате још питања о изградњи поузданих AI агената?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) да упознате друге учеснике, присуствујете сатовима консултација и добијете одговоре на питања о AI агентима.

## Додатни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед одговорне употребе AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Процена генеративних AI модела и AI апликација</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системске поруке за безбедност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Обрасци за процену ризика</a>

## Претходна лекција

[Agentic RAG](../05-agentic-rag/README.md)

## Следећа лекција

[Обрасци планирања](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем АИ услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматски преводи могу да садрже грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати званичним и обавезујућим извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->