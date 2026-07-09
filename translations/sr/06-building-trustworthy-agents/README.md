[![Поверење вредни AI агенти](../../../translated_images/sr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликните на слику изнад да бисте погледали видео о овом лекцији)_

# Изградња поверења вредних AI агената

## Увод

Ова лекција ће обухватити:

- Како направити и имплементирати безбедне и ефективне AI агенте
- Важне безбедносне аспекте приликом развоја AI агената.
- Како одржавати приватност података и корисника приликом развоја AI агената.

## Циљеви учења

Након завршетка ове лекције, знаћете како да:

- Идентификујете и смањите ризике приликом креирања AI агената.
- Имплементирате мере безбедности да бисте осигурали да се подаци и приступ правилно управљају.
- Креирате AI агенте који одржавају приватност података и пружају квалитетно корисничко искуство.

## Безбедност

Прво ћемо погледати како изградити безбедне агенцки апликације. Безбедност значи да AI агент функционише како је дизајнирано. Као градитељи агенцки апликација, имамо методе и алате да максимализујемо безбедност:

### Изградња система порука оквира

Ако сте икада правили AI апликацију користећи Велике језичке моделе (LLM), знате колико је важно дизајнирати робусан системски промпт или системску поруку. Ови промпти успостављају мета правила, упутства и смернице о томе како ће LLM комуницирати са корисником и подацима.

За AI агенте, системски промпт је још важнији јер AI агенти требају врло специфична упутства да заврше задатке које смо им дизајнирали.

За креирање скалабилних системских промпта, можемо користити системску поруку оквара за изградњу једног или више агената у нашој апликацији:

![Изградња система порука оквира](../../../translated_images/sr/system-message-framework.3a97368c92d11d68.webp)

#### Корак 1: Креирање мета системске поруке

Мета промпт ће користити LLM да генерише системске промпте за агенте које креирамо. Дизајнирамо га као шаблон тако да можемо ефикасно креирати више агената ако је потребно.

Ево примера мета системске поруке коју бисмо дали LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Корак 2: Креирање основног промпта

Следећи корак је да направите основни промпт који описује AI агента. Требало би да укључите улогу агента, задатке које агенат мора завршити, као и друге одговорности агента.

Ево примера:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Корак 3: Обезбедити основну системску поруку LLM-у

Сада можемо оптимизовати ову системску поруку тако што ћемо послати мета системску поруку као системску поруку, заједно са нашем основном системском поруком.

Ово ће генерисати системску поруку бољег дизајна која ће усмерити наше AI агенте:

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

Вредност овог система порука оквира је у могућности лакшег скалирања креирања системских порука за више агената као и побољшања система порука временом. Ретко ћете имати системску поруку која одмах одговара вашем комплетном случају употребе. Могућност прављења малих корекција и побољшања мењањем основне системске поруке и покретањем кроз систем омогућиће вам да упоредите и процените резултате.

## Разумевање претњи

Да бисмо изградили поуздане AI агенте, важно је разумети и ублажити ризике и претње према вашем AI агенту. Погледајмо само неке од различитих претњи AI агенатима и како боље да се планирате и припремите за њих.

![Разумевање претњи](../../../translated_images/sr/understanding-threats.89edeada8a97fc0f.webp)

### Задатак и упутство

**Опис:** Нападачи покушавају да промене инструкције или циљеве AI агента путем промптовања или манипулације улазима.

**Ублажавање**: Извршите валидационе провере и филтре улаза да бисте открили потенцијално опасне промпт-ове пре него што их AI агент обради. Пошто ови напади обично захтевају честу интеракцију са агентом, ограничавање броја корака у разговору је још један начин спречавања ових врста напада.

### Приступ критичним системима

**Опис**: Ако AI агент има приступ системима и услугама које чувају осетљиве податке, нападачи могу компромитовати комуникацију између агента и ових услуга. Ово могу бити директни напади или индиректни покушаји да се путем агента добију информације о тим системима.

**Ублажавање**: AI агенти треба да имају приступ системима само по потреби да се спрече овакве врсте напада. Комуникација између агента и система такође мора бити безбедна. Имплементација аутентификације и контроле приступа је други начин заштите ових информација.

### Преоптерећење ресурса и услуга

**Опис:** AI агенти могу приступити различитим алатима и услугама да би завршили задатке. Нападачи могу злоупотребити ову могућност тако што шаљу велики број захтева преко AI агента, што може довести до кварова система или високих трошкова.

**Ублажавање:** Имплементирајте политике које ограничавају број захтева које AI агент може упутити услузи. Ограничење броја корака у разговору и захтева вашем AI агенту је још један начин спречавања ових типова напада.

### Тровање базе знања

**Опис:** Ова врста напада не циља директно AI агента, већ базу знања и друге услуге које ће AI агент користити. Ово може укључивати корупцију података или информација које AI агент користи за завршавање задатка, што доводи до пристрасних или нежелених одговора кориснику.

**Ублажавање:** Редовно проверавајте податке које AI агент користи у својим радним токовима. Осигурајте да је приступ овим подацима безбедан и да их могу мењати само поуздане особе како бисте избегли ову врсту напада.

### Серијске грешке

**Опис:** AI агенти приступају разним алатима и услугама за обављање задатака. Грешке изазване нападачима могу довести до отказа других система повезаних са AI агентом, што чини напад ширим и тежим за решавање.

**Ублажавање**: Једна метода да се избегне ово је да AI агент ради у ограниченом окружењу, као што је обављање задатака у Docker контејнеру, како би се спречили директни напади на систем. Креирање механизама резервне копије и логике поновног покушаја када неки системи одговоре са грешком је још један начин за спречавање већих кварова система.

## Човек у петљи

Још један ефикасан начин да се изграде поуздани AI системи је коришћење човека у петљи. Ово ствара ток у коме корисници могу пружати повратне информације агентима у току рада. Корисници у суштини делују као агенти у мулти-агентном систему пружајући одобрење или прекид извршавања процеса.

![Човек у петљи](../../../translated_images/sr/human-in-the-loop.5f0068a678f62f4f.webp)

Ево пример кода који користи Microsoft Agent Framework да покаже како је овај концепт имплементиран:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Креирајте провајдера са људским одобрењем у процесу
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Креирајте агента са кораком људског одобрења
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

Изградња поверења вредних AI агената захтева пажљив дизајн, робусне безбедносне мере и континуирано унапређење. Имплементирањем структурираних система мета промптовања, разумевањем потенцијалних претњи и применом стратегија ублажавања, програмери могу креирати AI агенте који су и безбедни и ефективни. Додатно, укључивање човека у петљи осигурава да AI агенти остану усклађени са потребама корисника уз минимизирање ризика. Како AI наставља да се развија, одржавање проактивног става према безбедности, приватности и етичким разматрањима биће кључ за изградњу поверења и поузданости у системима покретаним AI-јем.

## Примери кода

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Детаљна демонстрација система мета-промптовања системских порука.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Прелиминарна одобрења, рангирање ризика и вођење ревизије за поверење вредне агенте.

### Имате ли још питања о изградњи поверења вредних AI агената?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) и упознајте друге ученике, посетите канцеларијско време и добијте одговоре на ваша питања о AI агентима.

## Додатни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Преглед одговорне употребе AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Евалуација генеративних AI модела и AI апликација</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системске поруке за безбедност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Образац процене ризика</a>

## Претходна лекција

[Agentic RAG](../05-agentic-rag/README.md)

## Следећа лекција

[Образац планирања](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->