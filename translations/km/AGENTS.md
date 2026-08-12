# AGENTS.md

## គម្របគម្រោង

បាង្គនេះ មាន "ភ្នាក់ងារចម្បងសម្រាប់អ្នកដំបូង" - មេរៀនសិក្សាសម្រាប់បង្រៀនជា​ពេញលេញ​អំពី​អ្វីៗគ្រប់យ៉ាង​ដែល​ត្រូវការដើម្បីបង្កើតភ្នាក់ងារ AI។ មេរៀន​មានចំនួន 18 មេរៀន (លេខ 00-18) ដែលគ្របដណ្តប់​ទៅលើមូលដ្ឋាន​គ្រឹះ និទស្សនាប្រព័ន្ធរចនារ ស៊េរីវដ្ឋានការ ប្រតិបត្តិការ​ផលិតកម្ម ភ្នាក់ងារត្រូវបានដំណើរការក្នុងមុខងារផ្ទាល់ខ្លួន ឬលើឧបករណ៍ និងសន្តិសុខនៃភ្នាក់ងារ AI។

**បច្ចេកវិទ្យាសំខាន់ៗ៖**
- Python 3.12+
- សៀវភៅកំណត់ត្រារ Jupyter សម្រាប់ការសិក្សាដោយអន្តរកម្ម
- ស៊េរីវដ្ឋាន AI: Microsoft Agent Framework (MAF)
- សេវាកម្ម Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**សំណុំស្ថាបត្យកម្ម៖**
- រចនាសម្ព័ន្ធផ្អែកលើមេរៀន (ថត 00-15+)
- មេរៀននីមួយៗ​មាន៖ ឯកសារ README, ឧទាហរណ៍កូដ (សៀវភៅ Jupyter), និងរូបភាព
- គាំទ្រភាសាច្រើនតាមប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ
- បណ្ណាល័យ Python មួយសៀវភៅក្នុងមេរៀននីមួយៗប្រើ Microsoft Agent Framework

## ពាក្យបញ្ជាសំរាប់តំឡើង

### លក្ខខណ្ឌមុនតំឡើង
- Python 3.12 ឬខ្ពស់ជាងនេះ
- មានជាវ Azure (សម្រាប់ Microsoft Foundry)
- មាន Azure CLI តំឡើង និងបាន Authenticate (`az login`)

### តំឡើងដំបូង

1. **Clone ឬ fork ឃ្លាំងកូដ៖**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ឬ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **បង្កើត និងបញ្ចូលបរិស្ថាន Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # លើ Windows: venv\Scripts\activate
   ```

3. **ដំឡើង dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **កំណត់ environment variables:**
   ```bash
   cp .env.example .env
   # កែសម្រួល .env ជាមួយកូនសោ API និងចំណុចចូលរបស់អ្នក
   ```

### Environment Variables ចាំបាច់

សម្រាប់ **Microsoft Foundry** (ចាំបាច់):
- `AZURE_AI_PROJECT_ENDPOINT` - ចំណុចបញ្ចប់គំរោង Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ឈ្មោះការដាក់ម៉ូដែល (ឧ. gpt-5-mini)

សម្រាប់ **Azure AI Search** (មេរៀន 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - ចំណុចបញ្ចប់ Azure AI Search
- `AZURE_SEARCH_API_KEY` - ក្តារទិន្នន័យ API Azure AI Search

ការផ្ទៀងផ្ទាត់គោលអ្នកប្រើៈ បច្ចុប្បន្នរត់ `az login` មុនរត់សៀវភៅកំណត់ត្រា (ប្រើ `AzureCliCredential`)។

## ចលនាការអភិវឌ្ឍន៍

### រត់សៀវភៅកំណត់ត្រារ Jupyter

មេរៀននីមួយៗមានសៀវភៅកំណត់ត្រា Jupyter ច្រើនសម្រាប់ស៊េរីវដ្ឋានផ្សេងៗគ្នា:

1. **ចាប់ផ្តើម Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ចូលទៅកាន់ថតមេរៀន** (ឧ. `01-intro-to-ai-agents/code_samples/`)

3. **បើក និងរត់សៀវភៅកំណត់ត្រា:**
   - `*-python-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (.NET)

### ធ្វើការជាមួយ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- តំរូវជាវ Azure
- ប្រើ `FoundryChatClient` សម្រាប់ Agent Service V2 (ភ្នាក់ងារច្បាស់ក្នុងរបារ Foundry)
- មានស្រាប់ក្នុងនិន្ទានុភាពផលិតកម្ម
- លំនាំឯកសារ៖ `*-python-agent-framework.ipynb`

## សេចក្តីណែនាំសម្រាប់សាកល្បង

នេះជាឃ្លាំងសិក្សាមួយមានកូដឧទាហរណ៍ ជាងជាកូដផលិតកម្មជាមួយតេស្តស្វ័យប្រវត្តិ។ ដើម្បីផ្ទៀងផ្ទាត់ការតំឡើង និងការផ្លាស់ប្តូរ:

### សាកល្បងដោយដៃ

1. **សាកល្បងបរិស្ថាន Python:**
   ```bash
   python --version  # គួរតែជា 3.12 ទៅលើ
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **សាកល្បងការរត់សៀវភៅកំណត់ត្រា:**
   ```bash
   # បំលែងសៀវភៅកំណត់ត្រាទៅជារង្វាស់ហើយរត់វា (សាកល្បងការនាំចូល)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ផ្ទៀងផ្ទាត់ environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### រត់សៀវភៅកំណត់ត្រាឯកត្ត

បើកសៀវភៅកំណត់ត្រា Jupyter ហើយអនុវត្តមេរៀនជាលំដាប់។ សៀវភៅនីមួយៗមាន៖
- ការនាំចូល
- ការតំឡើងការកំណត់រចនាសម្ព័ន្ធ
- ឧទាហរណ៍ភ្នាក់ងារ
- លទ្ធផលដែលរំពឹងទុកក្នុង markdown cells

### សាកល្បងភ្នាក់ងារ បានដាក់លើវេទិកា

សម្រាប់មេរៀនដែលមានភ្នាក់ងារត្រូវបានដាក់ស្ថិតនៅជា Microsoft Foundry hosted agent (01, 04, 05, 16) គម្រោងផ្តល់ជូនបញ្ជីសាកល្បង smoke-test នៅក្នុងថត `tests/` ដែលបញ្ជា​ដំណើរការ​តាមលំនាំ `.github/workflows/smoke-test.yml` តាមរយៈសកម្មភាព [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)។ វាជាស្ទង់មុខស្រាលបន្ទាប់ពីដាក់បញ្ចូល (ថាផ្នាក់ងារចូលដំណើរការ និងអនុវត្តបន្ទាត់បញ្ជាបែបមូលដ្ឋានដែរឬទេ) ដែលបន្ថែមទៅកាន់បណ្តាស្ទង់ក្នុងមេរៀន ទី 10 និង 16។ មើល [tests/README.md](./tests/README.md) សម្រាប់ផែនទីបញ្ជីទៅមេរៀន/ភ្នាក់ងារ។ មេរៀនទី 17 រត់នៅក្នុងបរិស្ថាន Foundry Local ដោយផ្ទាល់ ហើយមិនមានចំណុចបញ្ចប់ជាបណ្តោះអាសន្នទេ ដូច្នេះវាត្រូវបានផ្ទៀងផ្ទាត់ដោយការរត់សៀវភៅកំណត់ត្រាដោយផ្ទាល់។

## រចនាបថកូដ

### របៀបប្រើប្រាស់ Python

- **កំណែ Python**៖ 3.12+
- **រចនាបថកូដ**៖ អនុលោមតាមវិធានស្តង់ដារ Python PEP 8
- **សៀវភៅកំណត់ត្រា**៖ ប្រើ markdown cells ច្បាស់លាស់ ដើម្បីពន្យល់យ៉ាងជាក់លាក់
- **ការនាំចូល**៖ ដាក់ជាក្រុម គ្នាតាមបណ្ណាល័យស្តង់ដារ ក្រុមទី៣ និងនាំចូលក្នុងស្រុក

### របៀបប្រើ Jupyter Notebook

- បញ្ចូល markdown cells ពិពណ៌នាមុនពេលកូដ
- បន្ថែមឧទាហរណ៍លទ្ធផលក្នុងសៀវភៅកំណត់ត្រា
- ប្រើឈ្មោះអថេរច្បាស់លាស់ផ្ទៀងផ្ទាត់ជាមួយមេរៀន
- រក្សាលំដាប់រត់សៀវភៅកំណត់ត្រាជាលំដាប់ (cell 1 → 2 → 3...)

### ការៀបចំឯកសារ

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ការកសាង និង ការដំណើរការ

### ការបង្កើតឯកសារពិពណ៌នា

បាង្គនេះប្រើ Markdown សម្រាប់ឯកសារ៖
- ឯកសារ README.md ក្នុងថតមេរៀននីមួយៗ
- README.md សំខាន់នៅចំកណ្តាលឃ្លាំងកូដ
- ប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិតាម GitHub Actions

### ខ្សែការពារការបញ្ចេញ (CI/CD)

ស្ថិតនៅក្នុង `.github/workflows/`:

1. **co-op-translator.yml** - បកប្រែដោយស្វ័យប្រវត្តិតទៅ 50+ ភាសា
2. **welcome-issue.yml** - ស្វាគមន៍អ្នកបង្កើតបញ្ហាថ្មី
3. **welcome-pr.yml** - ស្វាគមន៍អ្នករួមចំណែកប្រែសំណើ Pull Request ថ្មី

### ដំណើរការ

នេះជាឃ្លាំងសិក្សា - មិនមានដំណើរការចេញផ្សាយទេ។ អ្នកប្រើ:
1. Fork ឬ clone គម្រោង
2. រត់សៀវភៅកំណត់ត្រាផ្ទាល់ខ្លួន ឬក្នុង GitHub Codespaces
3. រៀនដោយកែប្រែ និងសាកល្បងឧទាហរណ៍

## ការណែនាំសម្រាប់ Pull Request

### មុនបញ្ចូន

1. **សាកល្បងការផ្លាស់ប្តូររបស់អ្នក:**
   - រត់សៀវភៅកំណត់ត្រាដែលបានប៉ះពាល់ពេញលេញ
   - ពិនិត្យថាគ្រប់សែល execute ឥតកំហុស
   - ពិនិត្យថាលទ្ធផលសមស្រប

2. **បន្ទាន់សម្រួលឯកសារ:**
   - បន្ទាន់សម្រួល README.md ប្រសិនបើបន្ថែមមេរៀនថ្មី
   - បន្ថែមការវាយតម្លៃក្នុងសៀវភៅកំណត់ត្រាដើម្បីបញ្ជាក់កូដស្មុគស្មាញ
   - បញ្ជាក់ markdown cells ពន្យល់បំណង

3. **ការផ្លាស់ប្រើឯកសារ:**
   - កុំបន្ទុក `.env` (ប្រើ `.env.example`)
   - កុំបន្ទុកថត `venv/` ឬ `__pycache__/`
   - រក្សាលទ្ធផលក្នុងសៀវភៅកំណត់ត្រា ប្រសិនបើបង្ហាញមេរៀន
   - កំណត់បញ្ចប់ឯកសារបណ្តោះអាសន្ន និងសៀវភៅកំណត់ត្រាផ្ទុក (`*-backup.ipynb`)

### ទម្រង់ចំណងជើង PR

ប្រើចំណងជើងពន្យល់ដោយច្បាស់៖
- `[Lesson-XX] បន្ថែមឧទាហរណ៍ថ្មីសម្រាប់ <មេរៀន>`
- `[Fix] ពិនិត្យកំហុសវាយបញ្ជីក្នុង lesson-XX README`
- `[Update] បង្កើនគំរូកូដក្នុង lesson-XX`
- `[Docs] បន្ទាន់សម្រួលណែនាំការតំឡើង`

### តេស្តចាំបាច់

- សៀវភៅកំណត់ត្រាត្រូវរត់គ្មានកំហុស
- ឯកសារ README ត្រូវច្បាស់លាស់និងត្រឹមត្រូវ
- អនុលោមលំនាំកូដដែលមាននៅក្នុងគម្រោង
- គោរពភាពតំរូវទូទៅជាមួយមេរៀនផ្សេងទៀត

## សម្គាល់បន្ថែម

### បញ្ហាទូទៅដែលប្រជុំជួប

1. **កំណែ Python មិនត្រូវគ្នា:**
   - ត្រូវប្រាកដពីការប្រើ Python 3.12+
   - កញ្ចប់ខ្លះប្រហែលមិនដំណើរការជាមួយកំណែចាស់
   - ប្រើ `python3 -m venv` ដើម្បីបញ្ជាក់កំណែ Python យ៉ាងច្បាស់

2. **Environment variables:**
   - ត្រូវបង្កើត `.env` ពី `.env.example` តែងតែ
   - កុំបន្ទុក `.env` (វាក្នុង `.gitignore`)
   - ចូលប្រព័ន្ធដោយ `az login` ដើម្បី Authenticate Entra ID គ្មានសោ

3. **បញ្ហាគ្នះលក្ខណៈកញ្ចប់:**
   - ប្រើបរិស្ថាន virtual ថ្មី
   - ដំឡើងតាម `requirements.txt` មិនមែនតាមកញ្ចប់ចំណុច
   - សៀវភៅកំណត់ត្រាខ្លះត្រូវការកញ្ចប់បន្ថែមដែលបានបញ្ជាក់នៅក្នុង markdown cells

4. **សេវាកម្ម Azure:**
   - សេវាកម្ម Azure AI ត្រូវការជាវសកម្ម
   - មុខងារខ្លះមានតែនៅតំបន់ជាក់លាក់
   - ប្រាកដថាការដាក់ម៉ូដែល Azure OpenAI របស់អ្នកគាំទ្រ Responses API

### ផ្លូវសិក្សា

កំណត់ត្រាសម្រាប់មេរៀន៖
1. **00-course-setup** - ចាប់ផ្តើមនៅទីនេះសម្រាប់កំណត់បរិស្ថាន
2. **01-intro-to-ai-agents** - យល់ដឹងពីមូលដ្ឋានភ្នាក់ងារ AI
3. **02-explore-agentic-frameworks** - រៀនអំពីស៊េរីវដ្ឋានផ្សេងៗ
4. **03-agentic-design-patterns** - លំនាំរចនាសម្ព័ន្ធសំខាន់
5. កំណត់ត្រាតាមលេខមេរៀនជាថ្នាក់

### ជម្រើសស៊េរីវដ្ឋាន

ជ្រើសស៊េរីវដ្ឋានផ្អែកលើគោលដៅរបស់អ្នក:
- **មេរៀនទាំងអស់**: Microsoft Agent Framework (MAF) ជាមួយ `FoundryChatClient`
- **ភ្នាក់ងារចុះបញ្ជីនៅSERVER** ក្នុង Microsoft Foundry Agent Service V2 និងអាចមើលឃើញក្នុងទំព័រផ្ទៃ Foundry

### ការជួយគាំទ្រ

- ចូលរួមក្នុង [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- សូមពិនិត្យឯកសារ README មេរៀនសម្រាប់ណែនាំពិសេស
- មើល [README.md](./README.md) សម្រាប់ទិដ្ឋភាព​ទូទៅនៃកូដ
- ពិនិត្យ [ការតំឡើងមេរៀន](./00-course-setup/README.md) សម្រាប់មុខងារតំឡើងលម្អិត

### ការរួមចំណែក

នេះជាគម្រោងអប់រំបើកចំហជាសាធារណៈ។ សូមស្វាគមន៍ការរួមចំណែក៖
- កែលម្អឧទាហរណ៍កូដ
- បញ្ចេញកំហុសឬវាយបញ្ជីមិនត្រឹមត្រូវ
- បន្ថែមមតិពន្យល់
- ស្នើសុំនូវប្រធានបទមេរៀនថ្មី
- បកប្រែទៅភាសាបន្ថែមផ្សេងទៀត

មើល [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) សម្រាប់តម្រូវការបច្ចុប្បន្ន។

## បរិបទជាក់លាក់នៃគម្រោង

### គាំទ្រភាសាច្រើន

បាង្គនេះប្រើប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ៖
- គាំទ្រភាសាច្រើនជាង 50 ភាសា
- បកប្រែស្ថិតក្នុងថត `/translations/<lang-code>/`
- GitHub Actions workflow គ្រប់គ្រងការអាប់ដេតបកប្រែ
- ឯកសារផ្លូវការជាភាសាអង់គ្លេសនៅឯធម្មតា repository

### រចនាសម្ព័ន្ធមេរៀន

មេរៀននីមួយៗអនុវត្តតាមលំនាំដូចជា៖
1. រូបតំណាងវីដេអូជាមួយតំណភ្ជាប់
2. មាតិកាមេរៀនសរសេរជាឯកសារ README.md
3. ឧទាហរណ៍កូដក្នុងស៊េរីវដ្ឋានច្រើន
4. គោលបំណងសិក្សា និងលក្ខខណ្ឌមុន
5. ឧបករណ៍បន្ថែមសិក្សាតាមតំណភ្ជាប់

### ឈ្មោះឯកសារឧទាហរណ៍កូដ

ទម្រង់៖ `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - មេរៀន 1, MAF Python
- `14-sequential.ipynb` - មេរៀន 14, លំនាំ MAF អច្ឆរិយៈ
- `16-python-agent-framework.ipynb` - មេរៀន 16, ភ្នាក់ងារគាំទ្រអតិថិជនក្នុងផលិតកម្ម
- `17-local-agent-foundry-local.ipynb` - មេរៀន 17, ភ្នាក់ងារផ្ទាល់ខ្លួនជាមួយ Foundry Local + Qwen

### ថតពិសេស

- `translated_images/` - រូបភាពបកប្រែសម្រាប់ការបកប្រែ
- `images/` - រូបភាពដើមសម្រាប់មាតិកាភាសាអង់គ្លេស
- `.devcontainer/` - ការកំណត់ VS Code បរិយាកាសអភិវឌ្ឍនា
- `.github/` - GitHub Actions workflows និងគំរូ

### កញ្ចប់នាំចូល

កញ្ចប់សំខាន់ៗក្នុង `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - គាំទ្រប្រាក់ប្រតិបត្តិកម្ម Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - សេវាកម្ម Azure AI
- `azure-identity` - ការផ្ទៀងផ្ទាត់ Azure (AzureCliCredential)
- `azure-search-documents` - រួមបញ្ចូល Azure AI Search
- `mcp[cli]` - គាំទ្រប្រាក់ប្រតិបត្តិការកម្មវិធី Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->