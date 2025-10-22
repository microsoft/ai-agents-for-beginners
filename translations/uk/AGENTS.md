<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5f54aa3f419865e5d58bcfddb1d3198",
  "translation_date": "2025-10-03T15:58:57+00:00",
  "source_file": "AGENTS.md",
  "language_code": "uk"
}
-->
# AGENTS.md

## Огляд проєкту

Цей репозиторій містить курс "AI Agents for Beginners" — комплексний освітній матеріал, який навчає всього необхідного для створення AI-агентів. Курс складається з понад 15 уроків, що охоплюють основи, шаблони проєктування, фреймворки та розгортання AI-агентів у виробництві.

**Основні технології:**
- Python 3.12+
- Jupyter Notebooks для інтерактивного навчання
- AI-фреймворки: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Сервіси Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (доступний безкоштовний рівень)

**Архітектура:**
- Структура на основі уроків (каталоги 00-15+)
- Кожен урок містить: документацію README, приклади коду (Jupyter Notebooks) та зображення
- Підтримка багатомовності через автоматизовану систему перекладу
- Кілька варіантів фреймворків для кожного уроку (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Команди для налаштування

### Попередні вимоги
- Python 3.12 або новіший
- Обліковий запис GitHub (для GitHub Models — безкоштовний рівень)
- Підписка на Azure (опціонально, для сервісів Azure AI)

### Початкове налаштування

1. **Клонування або форк репозиторію:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Створення та активація віртуального середовища Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Встановлення залежностей:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Налаштування змінних середовища:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Необхідні змінні середовища

Для **GitHub Models (безкоштовно)**:
- `GITHUB_TOKEN` — персональний токен доступу з GitHub

Для **Azure AI Services** (опціонально):
- `PROJECT_ENDPOINT` — кінцева точка проєкту Azure AI Foundry
- `AZURE_OPENAI_API_KEY` — ключ API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` — URL кінцевої точки Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` — назва розгортання для моделі чату
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` — назва розгортання для вбудовувань
- Додаткова конфігурація Azure, як показано у `.env.example`

## Робочий процес розробки

### Запуск Jupyter Notebooks

Кожен урок містить кілька Jupyter Notebooks для різних фреймворків:

1. **Запустіть Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Перейдіть до каталогу уроку** (наприклад, `01-intro-to-ai-agents/code_samples/`)

3. **Відкрийте та виконайте ноутбуки:**
   - `*-semantic-kernel.ipynb` — використання фреймворку Semantic Kernel
   - `*-autogen.ipynb` — використання фреймворку AutoGen
   - `*-python-agent-framework.ipynb` — використання Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` — використання Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` — використання Azure AI Agent Service

### Робота з різними фреймворками

**Semantic Kernel + GitHub Models:**
- Доступний безкоштовний рівень з обліковим записом GitHub
- Підходить для навчання та експериментів
- Шаблон файлу: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Доступний безкоштовний рівень з обліковим записом GitHub
- Можливості оркестрації мультиагентних систем
- Шаблон файлу: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Найновіший фреймворк від Microsoft
- Доступний у Python та .NET
- Шаблон файлу: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Вимагає підписки на Azure
- Функції, готові до виробництва
- Шаблон файлу: `*-azureaiagent.ipynb`

## Інструкції з тестування

Це освітній репозиторій з прикладним кодом, а не виробничим кодом з автоматизованими тестами. Для перевірки налаштувань і змін:

### Ручне тестування

1. **Перевірте середовище Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Перевірте виконання ноутбуків:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Перевірте змінні середовища:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Запуск окремих ноутбуків

Відкрийте ноутбуки в Jupyter і виконуйте клітинки послідовно. Кожен ноутбук є самодостатнім і включає:
- Імпорт бібліотек
- Завантаження конфігурації
- Приклади реалізації агентів
- Очікувані результати в клітинках Markdown

## Стиль коду

### Конвенції Python

- **Версія Python**: 3.12+
- **Стиль коду**: Дотримуйтесь стандартів PEP 8
- **Ноутбуки**: Використовуйте зрозумілі клітинки Markdown для пояснення концепцій
- **Імпорти**: Групуйте за стандартною бібліотекою, сторонніми та локальними імпортами

### Конвенції Jupyter Notebook

- Додавайте описові клітинки Markdown перед клітинками з кодом
- Додавайте приклади результатів у ноутбуках для довідки
- Використовуйте зрозумілі назви змінних, які відповідають концепціям уроку
- Зберігайте лінійний порядок виконання ноутбука (клітинка 1 → 2 → 3...)

### Організація файлів

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Збірка та розгортання

### Створення документації

Цей репозиторій використовує Markdown для документації:
- Файли README.md у кожній папці уроку
- Головний README.md у корені репозиторію
- Автоматизована система перекладу через GitHub Actions

### CI/CD Пайплайн

Розташований у `.github/workflows/`:

1. **co-op-translator.yml** — автоматичний переклад на 50+ мов
2. **welcome-issue.yml** — привітання для авторів нових запитів
3. **welcome-pr.yml** — привітання для авторів нових pull request

### Розгортання

Це освітній репозиторій — процес розгортання відсутній. Користувачі:
1. Форкують або клонують репозиторій
2. Запускають ноутбуки локально або в GitHub Codespaces
3. Навчаються, змінюючи та експериментуючи з прикладами

## Правила для Pull Request

### Перед поданням

1. **Перевірте свої зміни:**
   - Повністю виконайте змінені ноутбуки
   - Переконайтеся, що всі клітинки виконуються без помилок
   - Перевірте, чи результати відповідають очікуванням

2. **Оновлення документації:**
   - Оновіть README.md, якщо додаєте нові концепції
   - Додайте коментарі в ноутбуках для складного коду
   - Переконайтеся, що клітинки Markdown пояснюють мету

3. **Зміни у файлах:**
   - Уникайте коміту файлів `.env` (використовуйте `.env.example`)
   - Не комітьте каталоги `venv/` або `__pycache__/`
   - Залишайте результати ноутбуків, якщо вони демонструють концепції
   - Видаляйте тимчасові файли та резервні ноутбуки (`*-backup.ipynb`)

### Формат заголовка PR

Використовуйте описові заголовки:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Обов'язкові перевірки

- Ноутбуки повинні виконуватися без помилок
- Файли README повинні бути зрозумілими та точними
- Дотримуйтесь існуючих шаблонів коду в репозиторії
- Зберігайте узгодженість з іншими уроками

## Додаткові примітки

### Поширені проблеми

1. **Невідповідність версії Python:**
   - Переконайтеся, що використовується Python 3.12+
   - Деякі пакети можуть не працювати зі старими версіями
   - Використовуйте `python3 -m venv`, щоб явно вказати версію Python

2. **Змінні середовища:**
   - Завжди створюйте `.env` з `.env.example`
   - Не комітьте файл `.env` (він у `.gitignore`)
   - Токен GitHub потребує відповідних дозволів

3. **Конфлікти пакетів:**
   - Використовуйте нове віртуальне середовище
   - Встановлюйте залежності з `requirements.txt`, а не окремі пакети
   - Деякі ноутбуки можуть вимагати додаткових пакетів, зазначених у їх клітинках Markdown

4. **Сервіси Azure:**
   - Сервіси Azure AI вимагають активної підписки
   - Деякі функції доступні лише в певних регіонах
   - Обмеження безкоштовного рівня застосовуються до GitHub Models

### Шлях навчання

Рекомендована послідовність проходження уроків:
1. **00-course-setup** — Почніть тут для налаштування середовища
2. **01-intro-to-ai-agents** — Зрозумійте основи AI-агентів
3. **02-explore-agentic-frameworks** — Вивчіть різні фреймворки
4. **03-agentic-design-patterns** — Основні шаблони проєктування
5. Продовжуйте через пронумеровані уроки послідовно

### Вибір фреймворку

Вибирайте фреймворк залежно від ваших цілей:
- **Навчання/Прототипування**: Semantic Kernel + GitHub Models (безкоштовно)
- **Мультиагентні системи**: AutoGen
- **Останні функції**: Microsoft Agent Framework (MAF)
- **Розгортання у виробництві**: Azure AI Agent Service

### Отримання допомоги

- Приєднуйтесь до [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Переглядайте README файли уроків для конкретних рекомендацій
- Перевіряйте головний [README.md](./README.md) для огляду курсу
- Звертайтеся до [Course Setup](./00-course-setup/README.md) для детальних інструкцій з налаштування

### Внесок

Це відкритий освітній проєкт. Внески вітаються:
- Покращуйте приклади коду
- Виправляйте помилки або друкарські помилки
- Додавайте пояснювальні коментарі
- Пропонуйте нові теми уроків
- Перекладайте на додаткові мови

Дивіться [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) для актуальних потреб.

## Контекст проєкту

### Підтримка багатомовності

Цей репозиторій використовує автоматизовану систему перекладу:
- Підтримка понад 50 мов
- Переклади у каталогах `/translations/<lang-code>/`
- Оновлення перекладів обробляються через GitHub Actions
- Джерельні файли англійською мовою знаходяться в корені репозиторію

### Структура уроків

Кожен урок дотримується послідовного шаблону:
1. Зображення відео з посиланням
2. Письмовий контент уроку (README.md)
3. Приклади коду в різних фреймворках
4. Навчальні цілі та попередні вимоги
5. Додаткові навчальні ресурси з посиланнями

### Іменування прикладів коду

Формат: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` — Урок 4, Semantic Kernel
- `07-autogen.ipynb` — Урок 7, AutoGen
- `14-python-agent-framework.ipynb` — Урок 14, MAF Python
- `14-dotnet-agent-framework.ipynb` — Урок 14, MAF .NET

### Спеціальні каталоги

- `translated_images/` — Локалізовані зображення для перекладів
- `images/` — Оригінальні зображення для контенту англійською мовою
- `.devcontainer/` — Конфігурація контейнера розробки для VS Code
- `.github/` — Шаблони та робочі процеси GitHub Actions

### Залежності

Основні пакети з `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` — фреймворк AutoGen
- `semantic-kernel` — фреймворк Semantic Kernel
- `agent-framework` — Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` — сервіси Azure AI
- `azure-search-documents` — інтеграція Azure AI Search
- `chromadb` — векторна база даних для прикладів RAG
- `chainlit` — фреймворк для UI чату
- `browser_use` — автоматизація браузера для агентів
- `mcp[cli]` — підтримка Model Context Protocol
- `mem0ai` — управління пам'яттю для агентів

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.