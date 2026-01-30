# AGENTS.md

## Преглед на проекта

Този репозиторий съдържа "AI агенти за начинаещи" - цялостен образователен курс, който учи всичко необходимо за създаване на AI агенти. Курсът включва над 15 урока, обхващащи основи, дизайнерски модели, рамки и внедряване на AI агенти в продукция.

**Основни технологии:**
- Python 3.12+
- Jupyter Notebooks за интерактивно обучение
- AI рамки: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI услуги: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (наличен безплатен план)

**Архитектура:**
- Структура, базирана на уроци (директории 00-15+)
- Всеки урок съдържа: документация README, примерен код (Jupyter notebooks) и изображения
- Поддръжка на много езици чрез автоматизирана система за превод
- Опции за множество рамки за всеки урок (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Команди за настройка

### Предварителни изисквания
- Python 3.12 или по-нова версия
- GitHub акаунт (за GitHub Models - безплатен план)
- Azure абонамент (по избор, за Azure AI услуги)

### Първоначална настройка

1. **Клониране или форкване на репозитория:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Създаване и активиране на Python виртуална среда:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Инсталиране на зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка на променливи на средата:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Необходими променливи на средата

За **GitHub Models (безплатно):**
- `GITHUB_TOKEN` - Личен токен за достъп от GitHub

За **Azure AI услуги** (по избор):
- `PROJECT_ENDPOINT` - Крайна точка на проект в Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - API ключ за Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL на крайна точка за Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Име на внедряване за чат модел
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Име на внедряване за embeddings
- Допълнителна конфигурация за Azure, както е показано в `.env.example`

## Работен процес за разработка

### Стартиране на Jupyter Notebooks

Всеки урок съдържа множество Jupyter notebooks за различни рамки:

1. **Стартиране на Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Навигиране до директория на урок** (например, `01-intro-to-ai-agents/code_samples/`)

3. **Отваряне и изпълнение на notebooks:**
   - `*-semantic-kernel.ipynb` - Използване на рамката Semantic Kernel
   - `*-autogen.ipynb` - Използване на рамката AutoGen
   - `*-python-agent-framework.ipynb` - Използване на Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Използване на Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Използване на Azure AI Agent Service

### Работа с различни рамки

**Semantic Kernel + GitHub Models:**
- Наличен безплатен план с GitHub акаунт
- Подходящ за обучение и експериментиране
- Модел на файлове: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Наличен безплатен план с GitHub акаунт
- Възможности за оркестрация на множество агенти
- Модел на файлове: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Най-новата рамка от Microsoft
- Налична в Python и .NET
- Модел на файлове: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Изисква Azure абонамент
- Функции, готови за продукция
- Модел на файлове: `*-azureaiagent.ipynb`

## Инструкции за тестване

Това е образователен репозиторий с примерен код, а не продукционен код с автоматизирани тестове. За да проверите настройката и промените си:

### Ръчно тестване

1. **Тестване на Python среда:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Тестване на изпълнение на notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Проверка на променливи на средата:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Изпълнение на отделни notebooks

Отворете notebooks в Jupyter и изпълнявайте клетките последователно. Всеки notebook е самостоятелен и включва:
- Импорт на библиотеки
- Зареждане на конфигурация
- Примерни реализации на агенти
- Очаквани изходи в markdown клетки

## Стил на код

### Конвенции за Python

- **Версия на Python**: 3.12+
- **Стил на код**: Следвайте стандартните конвенции на Python PEP 8
- **Notebooks**: Използвайте ясни markdown клетки за обяснение на концепции
- **Импорти**: Групирайте по стандартна библиотека, трети страни, локални импорти

### Конвенции за Jupyter Notebook

- Включвайте описателни markdown клетки преди клетки с код
- Добавяйте примери за изходи в notebooks за справка
- Използвайте ясни имена на променливи, които съответстват на концепциите на урока
- Поддържайте линейна последователност на изпълнение на notebook (клетка 1 → 2 → 3...)

### Организация на файлове

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

## Създаване и внедряване

### Създаване на документация

Този репозиторий използва Markdown за документация:
- README.md файлове във всяка папка на урок
- Основен README.md в корена на репозитория
- Автоматизирана система за превод чрез GitHub Actions

### CI/CD Пайплайн

Намира се в `.github/workflows/`:

1. **co-op-translator.yml** - Автоматичен превод на над 50 езика
2. **welcome-issue.yml** - Приветства създателите на нови проблеми
3. **welcome-pr.yml** - Приветства новите сътрудници на pull request

### Внедряване

Това е образователен репозиторий - няма процес на внедряване. Потребителите:
1. Форкват или клонират репозитория
2. Стартират notebooks локално или в GitHub Codespaces
3. Учете чрез модифициране и експериментиране с примери

## Насоки за Pull Request

### Преди изпращане

1. **Тествайте промените си:**
   - Изпълнете напълно засегнатите notebooks
   - Уверете се, че всички клетки се изпълняват без грешки
   - Проверете дали изходите са подходящи

2. **Актуализации на документацията:**
   - Актуализирайте README.md, ако добавяте нови концепции
   - Добавете коментари в notebooks за сложен код
   - Уверете се, че markdown клетките обясняват целта

3. **Промени във файлове:**
   - Избягвайте да комитирате `.env` файлове (използвайте `.env.example`)
   - Не комитвайте директории `venv/` или `__pycache__/`
   - Запазете изходите на notebooks, когато демонстрират концепции
   - Премахнете временни файлове и резервни notebooks (`*-backup.ipynb`)

### Формат на заглавие на PR

Използвайте описателни заглавия:
- `[Lesson-XX] Добавяне на нов пример за <концепция>`
- `[Fix] Корекция на грешка в README на урок-XX`
- `[Update] Подобряване на примерен код в урок-XX`
- `[Docs] Актуализация на инструкции за настройка`

### Необходими проверки

- Notebooks трябва да се изпълняват без грешки
- README файловете трябва да са ясни и точни
- Следвайте съществуващите модели на код в репозитория
- Поддържайте последователност с други уроци

## Допълнителни бележки

### Често срещани проблеми

1. **Несъответствие на версията на Python:**
   - Уверете се, че използвате Python 3.12+
   - Някои пакети може да не работят с по-стари версии
   - Използвайте `python3 -m venv`, за да зададете версията на Python изрично

2. **Променливи на средата:**
   - Винаги създавайте `.env` от `.env.example`
   - Не комитвайте `.env` файл (той е в `.gitignore`)
   - GitHub токенът трябва да има подходящи разрешения

3. **Конфликти на пакети:**
   - Използвайте нова виртуална среда
   - Инсталирайте от `requirements.txt`, вместо отделни пакети
   - Някои notebooks може да изискват допълнителни пакети, споменати в техните markdown клетки

4. **Azure услуги:**
   - Azure AI услугите изискват активен абонамент
   - Някои функции са специфични за региона
   - Ограниченията на безплатния план важат за GitHub Models

### Път за обучение

Препоръчителна последователност на уроците:
1. **00-course-setup** - Започнете тук за настройка на средата
2. **01-intro-to-ai-agents** - Разберете основите на AI агентите
3. **02-explore-agentic-frameworks** - Научете за различни рамки
4. **03-agentic-design-patterns** - Основни дизайнерски модели
5. Продължете през номерираните уроци последователно

### Избор на рамка

Изберете рамка според целите си:
- **Обучение/Прототипиране**: Semantic Kernel + GitHub Models (безплатно)
- **Системи с множество агенти**: AutoGen
- **Най-нови функции**: Microsoft Agent Framework (MAF)
- **Внедряване в продукция**: Azure AI Agent Service

### Получаване на помощ

- Присъединете се към [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Прегледайте README файловете на уроците за конкретни насоки
- Проверете основния [README.md](./README.md) за преглед на курса
- Вижте [Course Setup](./00-course-setup/README.md) за подробни инструкции за настройка

### Принос

Това е отворен образователен проект. Приветстваме приноси:
- Подобряване на примерния код
- Корекция на грешки или неточности
- Добавяне на пояснителни коментари
- Предлагане на нови теми за уроци
- Превод на допълнителни езици

Вижте [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) за текущи нужди.

## Контекст, специфичен за проекта

### Поддръжка на много езици

Този репозиторий използва автоматизирана система за превод:
- Поддържат се над 50 езика
- Преводите са в директории `/translations/<lang-code>/`
- GitHub Actions workflow обработва актуализациите на преводите
- Изходните файлове са на английски в корена на репозитория

### Структура на уроците

Всеки урок следва последователен модел:
1. Миниатюра на видео с линк
2. Писмено съдържание на урока (README.md)
3. Примерен код в множество рамки
4. Цели на обучението и предварителни изисквания
5. Допълнителни учебни ресурси с линкове

### Именуване на примерен код

Формат: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Урок 4, Semantic Kernel
- `07-autogen.ipynb` - Урок 7, AutoGen
- `14-python-agent-framework.ipynb` - Урок 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Урок 14, MAF .NET

### Специални директории

- `translated_images/` - Локализирани изображения за преводи
- `images/` - Оригинални изображения за съдържание на английски
- `.devcontainer/` - Конфигурация за контейнер за разработка в VS Code
- `.github/` - GitHub Actions workflows и шаблони

### Зависимости

Основни пакети от `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen рамка
- `semantic-kernel` - Semantic Kernel рамка
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI услуги
- `azure-search-documents` - Интеграция на Azure AI Search
- `chromadb` - Векторна база данни за RAG примери
- `chainlit` - Рамка за чат UI
- `browser_use` - Автоматизация на браузър за агенти
- `mcp[cli]` - Поддръжка на Model Context Protocol
- `mem0ai` - Управление на паметта за агенти

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.