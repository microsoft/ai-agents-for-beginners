<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:23:22+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "bg"
}
-->
# Github MCP Server Пример

## Описание

Това е демонстрация, създадена за хакатона AI Agents, организиран от Microsoft Reactor.

Инструментът се използва за препоръчване на хакатон проекти въз основа на Github репозиториите на потребителя. Това се постига чрез:

1. **Github Agent** - Използване на Github MCP Server за извличане на репозитории и информация за тях.
2. **Hackathon Agent** - Взема данните от Github Agent и предлага креативни идеи за хакатон проекти, базирани на проектите, езиците, използвани от потребителя, и темите на хакатона AI Agents.
3. **Events Agent** - Въз основа на предложението на Hackathon Agent, Events Agent препоръчва подходящи събития от серията AI Agent Hackathon.

## Стартиране на кода

### Променливи на средата

Тази демонстрация използва Azure Open AI Service, Semantic Kernel, Github MCP Server и Azure AI Search.

Уверете се, че сте задали правилните променливи на средата, за да използвате тези инструменти:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Стартиране на Chainlit Server

За да се свърже с MCP сървъра, тази демонстрация използва Chainlit като интерфейс за чат.

За да стартирате сървъра, използвайте следната команда в терминала:

```bash
chainlit run app.py -w
```

Това трябва да стартира вашия Chainlit сървър на `localhost:8000`, както и да попълни вашия Azure AI Search Index със съдържанието на `event-descriptions.md`.

## Свързване с MCP Server

За да се свържете с Github MCP Server, изберете иконата "щепсел" под полето "Type your message here.." в чата:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.bg.png)

Оттам можете да кликнете върху "Connect an MCP", за да добавите командата за свързване с Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Заменете "[YOUR PERSONAL ACCESS TOKEN]" с вашия реален Personal Access Token.

След като се свържете, трябва да видите (1) до иконата на щепсела, което потвърждава, че връзката е успешна. Ако не, опитайте да рестартирате Chainlit сървъра с `chainlit run app.py -w`.

## Използване на демонстрацията

За да стартирате работния процес на агентите за препоръчване на хакатон проекти, можете да напишете съобщение като:

"Препоръчайте хакатон проекти за Github потребителя koreyspace"

Router Agent ще анализира вашата заявка и ще определи коя комбинация от агенти (GitHub, Hackathon и Events) е най-подходяща за обработка на вашето запитване. Агенти работят заедно, за да предоставят цялостни препоръки, базирани на анализ на Github репозитории, генериране на идеи за проекти и подходящи технологични събития.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.