# AGENTS.md

## Преглед пројекта

Овај репозиторијум садржи "AI агенти за почетнике" - свеобухватан едукативни курс који вас учи свему што је потребно за креирање AI агената. Курс се састоји од више од 15 лекција које покривају основе, дизајн шаблоне, оквире и продукцијско постављање AI агената.

**Кључне технологије:**
- Python 3.12+
- Jupyter Notebooks за интерактивно учење
- AI оквири: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI услуге: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (доступан бесплатан ниво)

**Архитектура:**
- Структура заснована на лекцијама (директоријуми 00-15+)
- Свака лекција садржи: README документацију, узорке кода (Jupyter notebooks) и слике
- Подршка за више језика путем аутоматизованог система превођења
- Више опција оквира по лекцији (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Команде за постављање

### Предуслови
- Python 3.12 или новији
- GitHub налог (за GitHub Models - бесплатан ниво)
- Azure претплата (опционо, за Azure AI услуге)

### Почетно постављање

1. **Клонирајте или форкујте репозиторијум:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Креирајте и активирајте Python виртуелно окружење:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Инсталирајте зависности:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Поставите променљиве окружења:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Потребне променљиве окружења

За **GitHub Models (бесплатно):**
- `GITHUB_TOKEN` - Лични приступни токен са GitHub-а

За **Azure AI услуге** (опционо):
- `PROJECT_ENDPOINT` - Azure AI Foundry крајња тачка пројекта
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API кључ
- `AZURE_OPENAI_ENDPOINT` - URL крајње тачке Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Назив постављања за модел за ћаскање
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Назив постављања за уграђивање
- Додатна Azure конфигурација као што је приказано у `.env.example`

## Радни ток развоја

### Покретање Jupyter Notebooks

Свака лекција садржи више Jupyter notebooks за различите оквире:

1. **Покрените Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Навигирајте до директоријума лекције** (нпр. `01-intro-to-ai-agents/code_samples/`)

3. **Отворите и покрените notebooks:**
   - `*-semantic-kernel.ipynb` - Коришћење Semantic Kernel оквира
   - `*-autogen.ipynb` - Коришћење AutoGen оквира
   - `*-python-agent-framework.ipynb` - Коришћење Microsoft Agent Framework-а (Python)
   - `*-dotnet-agent-framework.ipynb` - Коришћење Microsoft Agent Framework-а (.NET)
   - `*-azureaiagent.ipynb` - Коришћење Azure AI Agent Service-а

### Рад са различитим оквирима

**Semantic Kernel + GitHub Models:**
- Доступан бесплатан ниво са GitHub налогом
- Добар за учење и експериментисање
- Шаблон фајла: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Доступан бесплатан ниво са GitHub налогом
- Способности оркестрације више агената
- Шаблон фајла: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Најновији оквир од Microsoft-а
- Доступан у Python-у и .NET-у
- Шаблон фајла: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Захтева Azure претплату
- Карактеристике спремне за продукцију
- Шаблон фајла: `*-azureaiagent.ipynb`

## Упутства за тестирање

Ово је едукативни репозиторијум са примерима кода, а не продукцијски код са аутоматизованим тестовима. Да бисте проверили своје постављање и измене:

### Ручно тестирање

1. **Тестирајте Python окружење:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Тестирајте извршавање notebook-а:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Проверите променљиве окружења:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Покретање појединачних notebook-а

Отворите notebook-е у Jupyter-у и извршавајте ћелије редом. Сваки notebook је самосталан и укључује:
- Изјаве о увозу
- Учитавање конфигурације
- Примере имплементације агената
- Очекиване излазе у markdown ћелијама

## Стил кода

### Python конвенције

- **Python верзија**: 3.12+
- **Стил кода**: Пратите стандардне Python PEP 8 конвенције
- **Notebooks**: Користите јасне markdown ћелије за објашњење концепата
- **Увоз**: Групишите по стандардној библиотеци, трећим странама, локалним увозима

### Jupyter Notebook конвенције

- Укључите описне markdown ћелије пре ћелија са кодом
- Додајте примере излаза у notebook-има за референцу
- Користите јасна имена променљивих која одговарају концептима лекције
- Одржавајте линеарни редослед извршавања notebook-а (ћелија 1 → 2 → 3...)

### Организација фајлова

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


## Изградња и постављање

### Изградња документације

Овај репозиторијум користи Markdown за документацију:
- README.md фајлови у сваком директоријуму лекције
- Главни README.md у корену репозиторијума
- Аутоматизован систем превођења путем GitHub Actions

### CI/CD Пипелине

Налази се у `.github/workflows/`:

1. **co-op-translator.yml** - Аутоматски превод на више од 50 језика
2. **welcome-issue.yml** - Поздравља нове креаторе проблема
3. **welcome-pr.yml** - Поздравља нове доприносиоце pull захтева

### Постављање

Ово је едукативни репозиторијум - нема процес постављања. Корисници:
1. Форкују или клонирају репозиторијум
2. Покрећу notebook-е локално или у GitHub Codespaces
3. Уче модификујући и експериментишући са примерима

## Упутства за Pull захтеве

### Пре подношења

1. **Тестирајте своје измене:**
   - Потпуно покрените погођене notebook-е
   - Проверите да ли се све ћелије извршавају без грешака
   - Проверите да ли су излази одговарајући

2. **Ажурирања документације:**
   - Ажурирајте README.md ако додајете нове концепте
   - Додајте коментаре у notebook-е за сложен код
   - Осигурајте да markdown ћелије објашњавају сврху

3. **Измене фајлова:**
   - Избегавајте комитовање `.env` фајлова (користите `.env.example`)
   - Не комитујте `venv/` или `__pycache__/` директоријуме
   - Задржите излазе notebook-а када демонстрирају концепте
   - Уклоните привремене фајлове и резервне notebook-е (`*-backup.ipynb`)

### Формат наслова PR-а

Користите описне наслове:
- `[Lesson-XX] Додај нови пример за <концепт>`
- `[Fix] Исправи грешку у README лекције-XX`
- `[Update] Побољшај узорак кода у лекцији-XX`
- `[Docs] Ажурирај упутства за постављање`

### Потребне провере

- Notebook-и треба да се извршавају без грешака
- README фајлови треба да буду јасни и тачни
- Пратите постојеће шаблоне кода у репозиторијуму
- Одржавајте конзистентност са другим лекцијама

## Додатне напомене

### Уобичајени проблеми

1. **Неслагање верзије Python-а:**
   - Осигурајте да користите Python 3.12+
   - Неки пакети можда неће радити са старијим верзијама
   - Користите `python3 -m venv` да експлицитно наведете верзију Python-а

2. **Променљиве окружења:**
   - Увек креирајте `.env` из `.env.example`
   - Не комитујте `.env` фајл (налази се у `.gitignore`)
   - GitHub токен захтева одговарајуће дозволе

3. **Конфликти пакета:**
   - Користите свеже виртуелно окружење
   - Инсталирајте из `requirements.txt` уместо појединачних пакета
   - Неки notebook-и могу захтевати додатне пакете наведене у њиховим markdown ћелијама

4. **Azure услуге:**
   - Azure AI услуге захтевају активну претплату
   - Неке функције су специфичне за регион
   - Ограничења бесплатног нивоа примењују се на GitHub Models

### Пут учења

Препоручени редослед проласка кроз лекције:
1. **00-course-setup** - Почните овде за постављање окружења
2. **01-intro-to-ai-agents** - Разумите основе AI агената
3. **02-explore-agentic-frameworks** - Упознајте различите оквире
4. **03-agentic-design-patterns** - Основни дизајн шаблони
5. Наставите кроз нумерисане лекције редом

### Избор оквира

Изаберите оквир на основу својих циљева:
- **Учење/Прототипирање**: Semantic Kernel + GitHub Models (бесплатно)
- **Системи са више агената**: AutoGen
- **Најновије функције**: Microsoft Agent Framework (MAF)
- **Постављање у продукцију**: Azure AI Agent Service

### Добијање помоћи

- Придружите се [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Прегледајте README фајлове лекција за специфична упутства
- Проверите главни [README.md](./README.md) за преглед курса
- Погледајте [Course Setup](./00-course-setup/README.md) за детаљна упутства за постављање

### Допринос

Ово је отворен едукативни пројекат. Доприноси су добродошли:
- Побољшајте примере кода
- Исправите типографске грешке или грешке
- Додајте разјашњавајуће коментаре
- Предложите нове теме лекција
- Преведите на додатне језике

Погледајте [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) за тренутне потребе.

## Контекст специфичан за пројекат

### Подршка за више језика

Овај репозиторијум користи аутоматизован систем превођења:
- Подржано више од 50 језика
- Преводи у директоријумима `/translations/<lang-code>/`
- GitHub Actions workflow обрађује ажурирања превода
- Изворни фајлови су на енглеском у корену репозиторијума

### Структура лекција

Свака лекција прати конзистентан шаблон:
1. Сличица видеа са линком
2. Писани садржај лекције (README.md)
3. Узорци кода у више оквира
4. Циљеви учења и предуслови
5. Додатни ресурси за учење са линковима

### Именовање узорака кода

Формат: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Лекција 4, Semantic Kernel
- `07-autogen.ipynb` - Лекција 7, AutoGen
- `14-python-agent-framework.ipynb` - Лекција 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Лекција 14, MAF .NET

### Специјални директоријуми

- `translated_images/` - Локализоване слике за преводе
- `images/` - Оригиналне слике за садржај на енглеском
- `.devcontainer/` - Конфигурација развојног окружења за VS Code
- `.github/` - GitHub Actions workflow-и и шаблони

### Зависности

Кључни пакети из `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen оквир
- `semantic-kernel` - Semantic Kernel оквир
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI услуге
- `azure-search-documents` - Интеграција Azure AI Search-а
- `chromadb` - Векторска база података за RAG примере
- `chainlit` - Оквир за UI за ћаскање
- `browser_use` - Аутоматизација претраживача за агенте
- `mcp[cli]` - Подршка за Model Context Protocol
- `mem0ai` - Управљање меморијом за агенте

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.