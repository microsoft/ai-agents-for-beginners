# Github MCP Server Example

## Опис

Це була демонстрація, створена для хакатону AI Agents, проведеного через Microsoft Reactor.

Інструмент використовується для рекомендації проєктів хакатону на основі репозиторіїв користувача на Github.
Це робиться за допомогою:

1. **Github Agent** - Використання Github MCP Server для отримання репозиторіїв та інформації про ці репозиторії.
2. **Hackathon Agent** - Отримує дані від Github Agent і пропонує креативні ідеї проєктів для хакатону на основі проєктів, мов програмування, які використовує користувач, та треків проєктів для хакатону AI Agents.
3. **Events Agent** - На основі пропозиції hackathon agent, events agent рекомендує релевантні події з серії AI Agent Hackathon.

## Запуск коду

### Змінні оточення

Ця демонстрація використовує Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server та Azure AI Search.

Переконайтеся, що у вас встановлено правильні змінні оточення для використання цих інструментів:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Запуск Chainlit Server

Для підключення до MCP серверу ця демонстрація використовує Chainlit як чат-інтерфейс.

Для запуску сервера використайте наступну команду у вашому терміналі:

```bash
chainlit run app.py -w
```


Це має запустити ваш Chainlit сервер на `localhost:8000`, а також заповнити ваш індекс Azure AI Search вмістом з файлу `event-descriptions.md`.

## Підключення до MCP Server

Щоб підключитися до Github MCP Server, оберіть іконку "штекера" під полем вводу чату "Type your message here..":

![MCP Connect](../../../../../translated_images/uk/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Там ви можете натиснути на "Connect an MCP", щоб додати команду підключення до Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Замість "[YOUR PERSONAL ACCESS TOKEN]" вставте свій фактичний персональний токен доступу.

Після підключення біля іконки штекера має зʼявитися (1), що підтверджує зʼєднання. Якщо ні, спробуйте перезапустити chainlit сервер за допомогою `chainlit run app.py -w`.

## Використання демонстрації

Щоб почати роботу агента з рекомендації проєктів хакатону, ви можете написати повідомлення, наприклад:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent проаналізує ваш запит і визначить, яка комбінація агентів (GitHub, Hackathon та Events) найкраще підходить для обробки вашого запиту. Агенти працюють разом, щоб надати всебічні рекомендації на основі аналізу репозиторіїв GitHub, генерації ідей для проєктів і відповідних технічних подій.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми і прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->