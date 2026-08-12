# Github MCP Server Example

## Опис

Це була демонстрація, створена для AI Agents Hackathon, проведеного через Microsoft Reactor.

Інструмент використовується для рекомендації проектів хакатону на основі репозиторіїв користувача на Github.
Це робиться за допомогою:

1. **Github Agent** - Використання Github MCP Server для отримання репозиторіїв та інформації про ці репозиторії.
2. **Hackathon Agent** - Отримує дані від Github Agent і пропонує креативні ідеї проектів для хакатону на основі проектів, мов програмування, які використовує користувач, і напрямків проектів для AI Agents hackathon.
3. **Events Agent** - На основі пропозицій hackathon agent, events agent рекомендує відповідні події з серії AI Agent Hackathon.
## Запуск коду 

### Змінні середовища

Ця демонстрація використовує Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server та Azure AI Search.

Переконайтеся, що у вас встановлені правильні змінні середовища для використання цих інструментів:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Запуск Chainlit Server

Щоб підключитися до MCP сервера, ця демонстрація використовує Chainlit як інтерфейс чат.

Щоб запустити сервер, використовуйте наступну команду у вашому терміналі:

```bash
chainlit run app.py -w
```

Це має запустити ваш Chainlit сервер на `localhost:8000`, а також заповнити ваш індекс Azure AI Search вмістом файлу `event-descriptions.md`.

## Підключення до MCP Server

Щоб підключитися до Github MCP Server, оберіть іконку "штекера" під полем чату "Type your message here..":

![MCP Connect](../../../../../translated_images/uk/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Потім можете натиснути на "Connect an MCP", щоб додати команду підключення до Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Замініть "[YOUR PERSONAL ACCESS TOKEN]" на ваш реальний персональний токен доступу.

Після підключення ви повинні побачити (1) поруч із іконкою штекера, що підтверджує підключення. Якщо ні, спробуйте перезапустити chainlit сервер за допомогою `chainlit run app.py -w`.

## Використання демонстрації

Щоб почати роботу агента з рекомендаціями проектів хакатону, ви можете написати повідомлення типу:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent проаналізує ваш запит і визначить, яка комбінація агентів (GitHub, Hackathon і Events) найкраще підійде для обробки вашого запиту. Агенти працюють разом, щоб надати комплексні рекомендації на основі аналізу репозиторіїв GitHub, ідей проектів та відповідних технічних подій.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою має вважатися авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->