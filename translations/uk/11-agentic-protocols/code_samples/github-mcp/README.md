<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T00:19:25+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "uk"
}
-->
# Github MCP Server Example

## Опис

Це демонстраційний проект, створений для хакатону AI Agents, організованого Microsoft Reactor.

Інструмент використовується для рекомендації хакатон-проектів на основі репозиторіїв користувача на Github. Це здійснюється за допомогою:

1. **Github Agent** - Використання Github MCP Server для отримання репозиторіїв та інформації про них.
2. **Hackathon Agent** - Аналіз даних від Github Agent і створення креативних ідей для хакатон-проектів на основі існуючих проектів, мов програмування, які використовує користувач, та напрямків хакатону AI Agents.
3. **Events Agent** - На основі рекомендацій Hackathon Agent, Events Agent пропонує відповідні заходи з серії хакатонів AI Agents.

## Запуск коду 

### Змінні середовища

Цей демонстраційний проект використовує Azure Open AI Service, Semantic Kernel, Github MCP Server та Azure AI Search.

Переконайтеся, що у вас налаштовані відповідні змінні середовища для використання цих інструментів:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Запуск Chainlit Server

Для підключення до MCP Server цей демонстраційний проект використовує Chainlit як інтерфейс чату.

Щоб запустити сервер, використовуйте наступну команду в терміналі:

```bash
chainlit run app.py -w
```

Це має запустити ваш Chainlit сервер на `localhost:8000`, а також заповнити ваш Azure AI Search Index контентом з файлу `event-descriptions.md`.

## Підключення до MCP Server

Щоб підключитися до Github MCP Server, натисніть на іконку "штекер" під полем "Type your message here.." у чаті:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.uk.png)

Після цього ви можете натиснути "Connect an MCP", щоб додати команду для підключення до Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Замініть "[YOUR PERSONAL ACCESS TOKEN]" на ваш реальний персональний токен доступу.

Після підключення ви повинні побачити (1) поруч із іконкою штекера, що підтверджує успішне підключення. Якщо ні, спробуйте перезапустити Chainlit сервер за допомогою `chainlit run app.py -w`.

## Використання демонстрації 

Щоб розпочати роботу агентів з рекомендації хакатон-проектів, ви можете написати повідомлення, наприклад:

"Рекомендуй хакатон-проекти для користувача Github koreyspace"

Router Agent проаналізує ваш запит і визначить, яка комбінація агентів (GitHub, Hackathon та Events) найкраще підходить для обробки вашого запиту. Агенти працюють разом, щоб надати комплексні рекомендації на основі аналізу репозиторіїв Github, генерації ідей для проектів та відповідних технічних заходів.

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.