# AGENTS.md

## សារពត៌មានគំរូគម្រោង

រក្សាទុកនេះមាន "ភ្នាក់ងារបញ្ញាសិប្បនិម្មិតសម្រាប់អ្នកចាប់ផ្តើម" - មេរៀនសិក្សា​ត្រឹមត្រូវ​កម្រិត​ពេញលេញ​ដែល​បង្រៀន​អ្វីៗ​ដែល​ត្រូវ​ការ​ដើម្បី​បង្កើត​ភ្នាក់ងារបញ្ញាសិប្បនិម្មិត។ មេរៀននេះមានចំនួន ១៨ មេរៀន​ដែលគ្របដណ្តប់ពីមូលដ្ឋាន គំរូរចនា រចនាសម្ព័ន្ធ និងការដាក់បញ្ចូលក្នុងការផលិតនៃភ្នាក់ងារបញ្ញាសិប្បនិម្មិត។

**បច្ចេកវិទ្យាសំខាន់ៗ:**
- Python 3.12+
- Jupyter Notebooks សម្រាប់ការសិក្សាប្រតិបត្តិ
- រចនាសម្ព័ន្ធ AI: Microsoft Agent Framework (MAF)
- សេវាកម្ម Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**រចនាសម្ព័ន្ធ:**
- រចនាសម្ព័ន្ធផ្អែកលើមេរៀន (ថតឯកសារ ០០-១៥+)
- មេរៀននិមួយៗមាន: ឯកសារ README, ឯកសារគំរូកូដ (កំណត់ត្រា Jupyter), និងរូបភាព
- គាំទ្រភាសាច្រើនតាមរយៈប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ
- កំណត់ត្រា Python មួយសម្រាប់មេរៀននិមួយៗប្រើ Microsoft Agent Framework

## ពាក្យបញ្ជាសំរាប់ការតំឡើង

### លក្ខខណ្ឌមុន
- Python 3.12 ឬខ្ពស់ជាង
- មានការជាវ Azure (សម្រាប់ Microsoft Foundry)
- តំឡើង និងចូលប្រើ Azure CLI (`az login`)

### ការតំឡើងដំបូង

1. **ចម្លងឬ fork រក្សាទុក:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ឬ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **បង្កើតនិងសកម្មបរិស្ថាន Python virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # នៅលើព្រាណ Windows: venv\Scripts\activate
   ```

3. **តំឡើងការពឹងផ្អែក:**
   ```bash
   pip install -r requirements.txt
   ```

4. **កំណត់អថេរបរិស្ថាន:**
   ```bash
   cp .env.example .env
   # កែសម្រួល .env ជាមួយកូនសោ API និងចំណុចចប់របស់អ្នក
   ```

### អថេរបរិស្ថានដែលត្រូវការ

សម្រាប់ **Microsoft Foundry** (ត្រូវការ):
- `AZURE_AI_PROJECT_ENDPOINT` - ចំណុចបញ្ចប់គម្រោង Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ឈ្មោះការដាក់បញ្ចូលម៉ូដែល (ឧ. gpt-4o)

សម្រាប់ **Azure AI Search** (មេរៀន 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - ចំណុចបញ្ចប់ Azure AI Search
- `AZURE_SEARCH_API_KEY` - កូនសោ API Azure AI Search

ការផ្ទៀងផ្ទាត់: ប្រតិបត្តិ `az login` មុនការរត់កំណត់ត្រា (ប្រើ `AzureCliCredential`)

## សកម្មភាពអភិវឌ្ឍន៍

### រត់កំណត់ត្រា Jupyter

មេរៀននិមួយៗមានកំណត់ត្រា Jupyter ច្រើនសម្រាប់រចនាសម្ព័ន្ធផ្សេងៗ:

1. **ចាប់ផ្តើម Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ទៅថតមេរៀនផ្ទាល់** (ឧ. `01-intro-to-ai-agents/code_samples/`)

3. **បើក និង រត់កំណត់ត្រា:**
   - `*-python-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (.NET)

### ធ្វើការជាមួយ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- ត្រូវការការជាវ Azure
- ប្រើ `FoundryChatClient` សម្រាប់ Agent Service V2 (ភ្នាក់ងារមើលឃើញនៅក្នុងវេទិកា Foundry)
- រៀបចំសម្រាប់ផលិតកម្មជាមួយការត្រួតពិនិត្យបញ្ញាក់ទាំងអស់
- គំរូឯកសារ: `*-python-agent-framework.ipynb`

## សេចក្តីណែនាំសម្រាប់ការ​ធ្វើតេស្ត

នេះគឺជារក្សាទុកសិក្សាមួយមានកូដគំរូ មិនមែនកូដផលិតកម្មជាមួយតេស្តស្វ័យប្រវត្តិទេ។ ដើម្បីផ្ទៀងផ្ទាត់ការតំឡើង និងការផ្លាស់ប្តូរ:

### តេស្តដោយដៃ

1. **ពិនិត្យបរិស្ថាន Python:**
   ```bash
   python --version  # គួរតែ 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ពិនិត្យការរត់កំណត់ត្រា:**
   ```bash
   # បម្លែងសៀវភៅកំណត់ត្រាទៅជាស្គ្រីប និងរត់ (សាកល្បងការនាំចូល)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ផ្ទៀងផ្ទាត់អថេរបរិស្ថាន:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### រត់កំណត់ត្រាឯករាជ្យ

បើកកំណត់ត្រានៅក្នុង Jupyter ហើយអនុវត្តន៍កោសិកា​ជា​លំដាប់។ កំណត់ត្រាម្នាក់ម្នាក់ទាំងអស់មាន:
- ពាក្យនាំចូល
- ការផ្ទុកកំណត់ចំណាំ
- ឧទាហរណ៍ការអនុវត្តភ្នាក់ងារ
- លទ្ធផលរំពឹងទុកនៅក្នុងកោសិកា markdown

## រចនាប័ទ្មកូដ

### ធម្មតារបស់ Python

- **កំណែ Python**: 3.12+
- **រចនាប័ទ្មកូដ**: អនុវត្តតាមប្រពៃណី PEP 8 របស់ Python
- **កំណត់ត្រា**: ប្រើកោសិកា markdown ច្បាស់សម្រាប់ពន្យល់មូលដ្ឋាន
- **នាំចូល**: ចែក according to standard library, third-party, local imports

### ធម្មតារបស់កំណត់ត្រា Jupyter

- បញ្ចូលកោសិកា markdown ពណ៌នាមុនកោសិកាកូដ
- បន្ថែមឧទាហរណ៍លទ្ធផលនៅក្នុងកំណត់ត្រាសម្រាប់យោង
- ប្រើឈ្មោះអថេរច្បាស់ដែលសមរម្យនឹងមេរៀន
- រក្សាលំដាប់ការអនុវត្តកំណត់ត្រា (កោសិកា ១ → ២ → ៣...)

### អង្គភាពឯកសារ

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ការសាងសង់ និង ការដាក់បញ្ចេញ

### ការសាងសង់ឯកសារព័ត៌មាន

រក្សាទុកនេះប្រើ Markdown សម្រាប់ឯកសារព័ត៌មាន:
- ឯកសារ README.md នៅក្នុងថតមេរៀននីមួយៗ
- README.md សំខាន់នៅដើមកន្លែងរក្សាទុក
- ប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិតាម GitHub Actions

### លំហូរ CI/CD

ត្រូវបានដាក់នៅក្នុង `.github/workflows/`:

1. **co-op-translator.yml** - បកប្រែស្វ័យប្រវត្តិទៅ ៥០+ ភាសា
2. **welcome-issue.yml** - ស្វាគមន៍អ្នកបង្កើតបញ្ហាថ្មី
3. **welcome-pr.yml** - ស្វាគមន៍អ្នករួមចំណែកក្នុង pull request ថ្មី

### ការដាក់បញ្ចេញ

នេះគឺជារក្សាទុកសិក្សា - មិនមានដំណើរដាក់បញ្ចេញ។ អ្នកប្រើប្រាស់:
1. Fork ឬ ចម្លងរក្សាទុក
2. រត់កំណត់ត្រាក្នុងកុំព្យូទ័រផ្ទាល់ ឬ GitHub Codespaces
3. សិក្សាតាមរយៈការផ្លាស់ប្តូរនិងចូល into ឧទាហរណ៍

## គោលការណ៍សម្រាប់ Pull Request

### មុនដាក់ស្នើ

1. **ពិនិត្យប្រែប្រាស់របស់អ្នក:**
   - រត់កំណត់ត្រាដែលទាក់ទងពេញលេញ
   - ផ្ទៀងផ្ទាត់ថាកោសិកាទាំងអស់ដំណើរការដោយគ្មានកំហុស
   - ពិនិត្យថាលទ្ធផលសមរម្យ

2. **បច្ចុប្បន្នភាពឯកសារព័ត៌មាន:**
   - បន្ទាន់បរិវេណ README.md ប្រសិនបើបន្ថែមមូលដ្ឋានថ្មី
   - បន្ថែមមតិយោបល់ក្នុងកំណត់ត្រាសម្រាប់កូដស្មុគស្មាញ
   - ធានាថាកោសិកា markdown ពន្យល់គោលបំណង

3. **ការផ្លាស់ប្តូរឯកសារ:**
   - ជៀសវាងបញ្ជូនឯកសារ `.env` (ប្រើ `.env.example`)
   - មិនបញ្ជូនថត `venv/` ឬ `__pycache__/`
   - រក្សាលទ្ធផលកំណត់ត្រា ក្នុងករណីបង្ហាញមូលដ្ឋាន
   - លុបឯកសារបណ្ដាក់និងកំណត់ត្រាសម្រាប់បម្រុង (`*-backup.ipynb`)

### រចនាសម្ព័ន្ធចំណងជើង PR

ប្រើចំណងជើងពណ៌នាឲ្យច្បាស់:
- `[Lesson-XX] បន្ថែមឧទាហរណ៍ថ្មីសម្រាប់ <concept>`
- `[Fix] កែសម្រួលកំហុសក្នុង README មេរៀន-XX`
- `[Update] លើកស្ទួយឧទាហរណ៍កូដនៅមេរៀន-XX`
- `[Docs] បន្ថែមសេចក្តីណែនាំតំឡើង`

### ពិនិត្យដែលត្រូវការ

- កំណត់ត្រា​គួរតែរត់បានគ្មានកំហុស
- ឯកសារ README គួរតែច្បាស់លាស់ និងត្រឹមត្រូវ
- ធ្វើតាមគំរូកូដនៅក្នុងរក្សាទុក
- រក្សាសំរបសំរួលជាមួយមេរៀនផ្សេងទៀត

## កំណត់សម្គាល់បន្ថែម

### បញ្ហាធម្មតា

1. **កំណែ Python ខុសគ្នា:**
   - ធានាប្រើ Python 3.12+
   - កញ្ចប់ខ្លះអាចមិនដំណើរការ ជាមួយកំណែចាស់
   - ប្រើ `python3 -m venv` ដាក់កំណែ Python ឲ្យច្បាស់

2. **អថេរបរិស្ថាន:**
   - តែងតែបង្កើត `.env` ពី `.env.example`
   - មិនបញ្ជូនឯកសារ `.env` (វានៅក្នុង `.gitignore`)
   - ចូលដោយ `az login` សម្រាប់ការផ្ទៀងផ្ទាត់ Entra ID គ្មានសោ

3. **ជម្លោះកញ្ចប់:**
   - ប្រើបរិស្ថាន virtual ថ្មី
   - តំឡើងពី `requirements.txt` ជាជាងតំឡើងកញ្ចប់បុគ្នា
   - កំណត់ត្រាខ្លះត្រូវការកញ្ចប់បន្ថែមដែលបានពិពណ៌នានៅកោសិកា markdown

4. **សេវាកម្ម Azure:**
   - សេវាកម្ម Azure AI ត្រូវការជាវសកម្ម
   - មុខងារខ្លះពាក់ព័ន្ធតំបន់ជាក់លាក់
   - ធានាថាការដាក់បញ្ចូលម៉ូដែល Azure OpenAI របស់អ្នកគាំទ្រ Responses API

### ផ្លូវរៀន

ផ្លូវរៀនដែលបានណែនាំតាមលំដាប់មេរៀន:
1. **00-course-setup** - ចាប់ផ្តើមពីនេះសម្រាប់ការតំឡើងបរិស្ថាន
2. **01-intro-to-ai-agents** - យល់ដឹងពីមូលដ្ឋានភ្នាក់ងារបញ្ញាសិប្បនិម្មិត
3. **02-explore-agentic-frameworks** - រៀនអំពីរចនាសម្ព័ន្ធវិធីផ្សេងៗ
4. **03-agentic-design-patterns** - គំរូរចនាសម្ព័ន្ធសំខាន់
5. បន្តតាមមេរៀន​លេខរៀង​តាមលំដាប់

### ជម្រើសរចនាសម្ព័ន្ធ

ជ្រើសរើសរចនាសម្ព័ន្ធយោងទៅតាមគោលបំណងរបស់អ្នក:
- **មេរៀនទាំងអស់**: Microsoft Agent Framework (MAF) ជាមួយ `FoundryChatClient`
- **ភ្នាក់ងារចុះបញ្ជីនៅលើម៉ាស៊ីនបម្រើ** ក្នុង Microsoft Foundry Agent Service V2 និងមើលឃើញនៅក្នុងវេទិកា Foundry

### រកជំនួយ

- ចូលរួម [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- ពិនិត្យឯកសារ README មេរៀនសម្រាប់សេចក្តីណែនាំជាក់លាក់
- ពិនិត្យ [README.md](./README.md) សម្រាប់ទិដ្ឋភាពទូទៅនៃមេរៀន
- យោងទៅ [Course Setup](./00-course-setup/README.md) សម្រាប់សេចក្តីណែនាំលម្អិត

### រួមចំណែក

នេះគឺជា​គម្រោង​សិក្សា​បើក​ចំហ។ សូមស្វាគមន៍ការរួមចំណែក:
- កែលំអឧទាហរណ៍កូដ
- កែសម្រួលកំហុស ឬកំហុសវេយ្យាករណ៍
- បន្ថែមមតិយោបល់ឲ្យច្បាស់លាស់
- សូមផ្តល់យោបល់ដល់មេរៀនថ្មី
- បកប្រែទៅភាសាផ្សេងទៀត

មើល [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) សម្រាប់តម្រូវការបច្ចុប្បន្ន

## បរិបទពិសេសនៃគម្រោង

### គាំទ្រភាសាច្រើន

រក្សាទុកនេះប្រើប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ:
- គាំទ្រភាសាជាង ៥០
- បកប្រែក្នុងថត `/translations/<lang-code>/`
- លំហូរ GitHub Actions គ្រប់គ្រងការអាប់ដេតបកប្រែ
- ឯកសារមូលដ្ឋានជា​អង់គ្លេស​នៅដើមរក្សាទុក

### រចនាសម្ព័ន្ធមេរៀន

មេរៀននិមួយៗតាមលំដាប់ដែលស្រដៀងគ្នា:
1. រូបតំណាងវីដេអូជាមួយតំណភ្ជាប់
2. បរិយាយមេរៀន (README.md)
3. ឧទាហរណ៍កូដក្នុងរចនាសម្ព័ន្ធច្រើន
4. វិស័យរៀន និងលក្ខខណ្ឌមុន
5. ឯកសារកម្មវិធីបន្ថែមដែលភ្ជាប់

### ឈ្មោះឧទាហរណ៍កូដ

រចនាសម្ព័ន្ធ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - មេរៀន ១, MAF Python
- `14-sequential.ipynb` - មេរៀន ១៤, គំរូ MAF ជាន់ខ្ពស់

### ថតពិសេស

- `translated_images/` - រូបភាពបំលែងភាសា
- `images/` - រូបភាពដើមសម្រាប់មាតិការអង់គ្លេស
- `.devcontainer/` - ការកំណត់កំណែអភិវឌ្ឍ VS Code container
- `.github/` - លំហូរ និងគំរូ GitHub Actions

### កញ្ចប់ការពឹងផ្អែក

កញ្ចប់សំខាន់ពី `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - គាំទ្រពិធី Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - សេវាកម្ម Azure AI
- `azure-identity` - ការផ្ទៀងផ្ទាត់ Azure (AzureCliCredential)
- `azure-search-documents` - ការរួមបញ្ចូល Azure AI Search
- `mcp[cli]` - គាំទ្រពិធី Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->