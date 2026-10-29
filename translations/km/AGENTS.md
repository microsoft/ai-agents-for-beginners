# AGENTS.md

## សង្ខេបគម្រោង

ទីតាំងនេះមាន "ភ្នាក់ងារបច្ចេកវិទ្យាបញ្ញាសិប្បនិម្មិត (AI Agents) សម្រាប់អ្នកចាប់ផ្តើម" - មេរៀនសិក្សាដ៏ពេញលេញដែលបង្រៀនអ្វីគ្រប់យ៉ាងដែលត្រូវការ ដើម្បីបង្កើតភ្នាក់ងារ AI។ មេរៀននេះមានចំនួន ១៨ មេរៀន (សំរុបលេខ ០០-១៨) ដែលគ្របដណ្តប់មូលដ្ឋាន, រចនាបថ, ស៊ុមប្រើប្រាស់, ការបញ្ចូលផលិតកម្ម, ភ្នាក់ងារផ្ទាល់ក្នុងឧបករណ៍ និងសុវត្ថិភាពនៃភ្នាក់ងារ AI។

**បច្ចេកវិទ្យាសំខាន់ៗៈ**
- Python 3.12+
- Jupyter Notebooks សម្រាប់ការសិក្សាផ្ទាល់បែបអន្តរកម្ម
- ស៊ុម AI: Microsoft Agent Framework (MAF)
- សេវាកម្ម AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ស្ថាបត្យកម្មៈ**
- រចនាបថមេរៀន (ថត ០០-១៨)
- មេរៀននីមួយៗមាន: ឯកសារ README, ឧទាហរណ៍កូដ (Jupyter notebooks) និងរូបភាព
- គាំទ្រភាសាច្រើនតាមប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ
- Jupyter notebook មួយសម្រាប់ Python ក្នុងមេរៀនប្រើ Microsoft Agent Framework

## ពាក្យបញ្ជាររៀបចំ

### លក្ខខណ្ឌមុន
- Python 3.12 ឬខ្ពស់ជាងនេះ
- ការជាវ Azure (សម្រាប់ Microsoft Foundry)
- Azure CLI បានដំឡើង និង បានត្រូវបានAuthenticate (`az login`)

### ការរៀបចំដំបូង

1. **ចម្លង ឬ Fork ទីតាំងនេះ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **បង្កើត និង ចាប់ផ្តើមបរិយាកាស Python virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **ដំឡើងបណ្ណាល័យដែលចាំបាច់:**
   ```bash
   pip install -r requirements.txt
   ```

4. **កំណត់បរិយាកាសប៉ារ៉ាម៉ែត្រ:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### បរិយាកាសប៉ារ៉ាម៉ែត្រចាំបាច់

សម្រាប់ **Microsoft Foundry** (ចាំបាច់):
- `AZURE_AI_PROJECT_ENDPOINT` - ចំណុចចុះចតគម្រោង Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ឈ្មោះដាក់បណ្ដេញម៉ូដែល (ឧ. gpt-5-mini)

សម្រាប់ **Azure AI Search** (មេរៀន 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - ចំណុចចុះចត Azure AI Search
- `AZURE_SEARCH_API_KEY` - កូនសោ API របស់ Azure AI Search

ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ: ដំណើរការ `az login` មុនវាយកូដ notebooks (ប្រើ `AzureCliCredential`)។

## ដំណើរការអភិវឌ្ឍន៍

### រត់ Jupyter Notebooks

មេរៀននីមួយៗមាន Jupyter notebooks ច្រើនសម្រាប់ស៊ុមផ្សេងៗ:

1. **ចាប់ផ្តើម Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ទៅកាន់ថតមេរៀន** (ឧ. `01-intro-to-ai-agents/code_samples/`)

3. **បើក និង រត់ notebooks:**
   - `*-python-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - ប្រើ Microsoft Agent Framework (.NET)

### ធ្វើការជាមួយ Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- តម្រូវមានការជាវ Azure
- ប្រើ `FoundryChatClient` សម្រាប់ Agent Service V2 (ភ្នាក់ងារមានអ្នកមើលបាននៅក្នុងផតថល Foundry)
- ត្រៀមចេញផ្សាយដោយមានការត្រួតពិនិត្យជាស្រេច
- លំនាំឯកសារ៖ `*-python-agent-framework.ipynb`

## សេចក្តីណែនាំសម្រាប់ការ​សាកល្បង

នេះគឺជាទីតាំងសិក្សា ដែលមានកូដទំរង់ឧទាហរណ៍ មិនមែនកូដផលិតកម្មជាមួយការធ្វើតេស្តស្វ័យប្រវត្តិទេ។ ដើម្បីផ្ទៀងផ្ទាត់ការរៀបចំនិងការផ្លាស់ប្តូរ:

### ការតេស្តដោយដៃ

1. **សាកល្បងបរិយាកាស Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **សាកល្បងរត់ notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ផ្ទៀងផ្ទាត់បរិយាកាសប៉ារ៉ាម៉ែត្រ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### រត់ឯកជន notebooks

បើក notebooks ក្នុង Jupyter ហើយរត់នៅលំដាប់។ ខ្ទង់នីមួយៗមាន:
- ពាក្យនាំចូល
- ការផ្ទុកការកំណត់
- ឧទាហរណ៍ភាពការងារភ្នាក់ងារ
- លទ្ធផលដែលរំពឹងទុកនៅក្នុងខ្ទង់ markdown

### សាកល្បងឆ្លងកាត់ភ្នាក់ងារដែលបានដាក់បង្ហាញ

សម្រាប់មេរៀនដែលមានភ្នាក់ងារ​ដាក់ក្នុង Microsoft Foundry (០១, ០៤, ០៥, ១៦) ទីតាំងផ្គត់ផ្គង់បញ្ជីសាកល្បងនៅក្រោម `tests/` ដែលដំណើរការដោយផ្នែកអាជីព `.github/workflows/smoke-test.yml` តាមសកម្មភាព [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)។ វា​ជា​ការតេស្តបន្ទាប់ពីដាក់ (តើភ្នាក់ងារអាចដំណើរការ និងអនុវត្តការស្នើប podstawnian មូលដ្ឋានមែនទេ?), ជួយបន្ថែមលើបន្ទាត់ប្នង់តំលៃក្នុងមេរៀន ១០ និង ១៦។ សូមមើល [tests/README.md](./tests/README.md) សម្រាប់ការតភ្ជាប់បញ្ជីទៅមេរៀននិងភ្នាក់ងារ។ មេរៀន ១៧ រត់ក្នុងជាក់ស្តែងជាមួយ Foundry Local ហើយគ្មានចំណុចធ្វើការចុះចត ដូច្នោះវាត្រូវបានផ្ទៀងផ្ទាត់ដោយរត់ notebook ផ្ទាល់។

## រចនាបថកូដ

### ធម្មតានៃ Python

- **កំណែ Python**: 3.12+
- **រចនាបថកូដ**: អនុវត្តតាមក្បួន PEP 8 នៃ Python
- **Notebooks**: ប្រើខ្ទង់ markdown ច្បាស់លាស់សម្រាប់ពន្យល់គំនិត
- **ការនាំចូល**: បូកគ្នាតាមបណ្ណាល័យស្ដង់ដា, ក្រុមទីបី, ការនាំចូលក្នុងក្នុង

### ធម្មតានៃ Jupyter Notebook

- រួមបញ្ចូលខ្ទង់ markdown រៀបរាប់ មុនខ្ទង់កូដ
- បន្ថែមឧទាហរណ៍លទ្ធផលនៅក្នុង notebooks សម្រាប់យោង
- ប្រើឈ្មោះអថេរច្បាស់លាស់ដែលត្រូវគ្នានឹងមេរៀន
- រក្សាលំដាប់បញ្ជានៃ notebook ត្រង់ (ឯកសារ ១ → ២ → ៣...)

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

## ការសាងសង់ និង ដាក់បញ្ចូល

### ការសាងសង់ឯកសារសម្គាល់

ទីតាំងនេះប្រើ Markdown សម្រាប់ឯកសារ:
- ឯកសារ README.md នៅក្នុងថតមេរៀននីមួយៗ
- README.md ជាឯកសារចម្បងនៅឬតាមដើម repository
- ប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិក្នុង GitHub Actions

### ប្រព័ន្ធ CI/CD

ស្ថិតនៅ `.github/workflows/`:

1. **co-op-translator.yml** - បកប្រែស្វ័យប្រវត្តិទៅជាភាសា 50+ ភាសា
2. **welcome-issue.yml** - ស្វាគមន៍អ្នកបង្កើត បញ្ហាថ្មី
3. **welcome-pr.yml** - ស្វាគមន៍អ្នករួមចំណែក pull request ថ្មី

### ការដាក់បញ្ចូល

នេះគឺជាទីតាំងសិក្សា - គ្មានដំណើរការដាក់បញ្ចូល។ អ្នកប្រើ:
1. Fork ឬ ចម្លងដាក់
2. រត់ notebooks តាមក្នុងផ្ទះ ឬ GitHub Codespaces
3. រៀនដោយកែប្រែមើល និង សាកល្បងឧទាហរណ៍

## ការណែនាំរបស់ Pull Request

### មុនពេលដាក់ស្នើ

1. **សាកល្បងការផ្លាស់ប្តូររបស់អ្នក:**
   - រត់ notebooks ដែលសុទ្ធសឹងទាល់
   - ផ្ទៀងផ្ទាត់ថាខ្ទង់ទាំងអស់រត់ដោយគ្មានកំហុស
   - ពិនិត្យមើលលទ្ធផលអោយត្រឹមត្រូវ

2. **បច្ចុប្បន្នភាពឯកសារ README:**
   - បន្ថែម README.md ប្រសិនបើបន្ថែមគំនិតថ្មី
   - បន្ថែមមតិយោបល់នៅក្នុង notebooks សម្រាប់កូដស្មុគស្មាញ
   - ធ្វើឲ្យខ្ទង់ markdown ពន្យល់ថាគោលបំណងជាអ្វី

3. **ការផ្លាស់ប្តូរឯកសារ:**
   - ជៀសវាងបន្ថែមឯកសារ `.env` (ប្រើ `.env.example`)
   - មិនបន្ថែមថត `venv/` ឬ `__pycache__/`
   - រក្សាលទ្ធផលក្នុង notebook ប្រសិនបើបង្ហាញគំនិត
   - លុបឯកសារថ្មី និង notebook បម្រុង (`*-backup.ipynb`)

### ទម្រង់ចំណងជើង PR

ប្រើចំណងជើងពន្យល់ច្បាស់:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### ការត្រួតពិនិត្យចាំបាច់

- Notebooks ត្រូវរត់ដោយគ្មានកំហុស
- ឯកសារ README ត្រូវច្បាស់លាស់ និងត្រឹមត្រូវ
- អនុវត្តលំនាំកូដដែលមានស្រាប់ក្នុង repository
- រក្សាគោលការណ៍ត្រូវគ្នាជាមួយមេរៀនផ្សេងទៀត

## កំណត់សម្គាល់បន្ថែម

### ចំណុចប្រយ័ត្នទូទៅ

1. **កំណែ Python មិនត្រូវគ្នា:**
   - ត្រូវប្រាកដថាអ្នកប្រើ Python 3.12+
   - បណ្ណាល័យខ្លះអាចមិនដំណើរការជាមួយកំណែមុនៗ
   - ប្រើ `python3 -m venv` ដើម្បីបញ្ជាក់កំណែ Python ព្រមាន

2. **បរិយាកាសប៉ារ៉ាម៉ែត្រ:**
   - តែងតែបង្កើត `.env` ពី `.env.example`
   - មិនបន្ថែមឯកសារ `.env` (វាត្រូវមានក្នុង `.gitignore`)
   - ចូលជាមួយ `az login` សម្រាប់អះអាងអត្តសញ្ញាណ Entra ID ដោយគ្មានសោរចូល

3. **ភាពទាក់ទាញបណ្ណាល័យ:**
   - ប្រើបរិយាកាស virtual ថ្មី
   - ដំឡើងពី `requirements.txt` មិនមែនបណ្ណាល័យឯកជនឡែកៗ
   - ខ្ទង់ notebooks ខ្លះប្រហែលជាត្រូវមានបណ្ណាល័យបន្ថែមដែលបានរាយនៅក្នុង markdown

4. **សេវាកម្ម Azure:**
   - សេវាកម្ម Azure AI ត្រូវការជាវសកម្មភាព
   - មុខងារខ្លះមានកំណត់តំបន់
   - ត្រូវប្រាកដថា ការដាក់បណ្ដេញម៉ូដែល Azure OpenAI របស់អ្នកគាំទ្រ Responses API

### ផ្លូវរៀន

មានការណែនាំថាត្រូវទៅមុខតាមលំដាប់មេរៀនៈ
1. **00-course-setup** - ចាប់ផ្តើមនៅទីទីនេះសម្រាប់រៀបចំបរិយាកាស
2. **01-intro-to-ai-agents** - យល់ដឹងពីមូលដ្ឋានភ្នាក់ងារ AI
3. **02-explore-agentic-frameworks** - រៀនអំពីស៊ុមផ្សេងៗ
4. **03-agentic-design-patterns** - លំនាំរចនា៥សំខាន់
5. បន្តតាមលំដាប់លេខម្ដងៗ

### ការជ្រើសរើសស៊ុម

ជ្រើសយកស៊ុមយោងតាមគោលបំណងរបស់អ្នកៈ
- **មេរៀនទាំងអស់**: Microsoft Agent Framework (MAF) ជាមួយ `FoundryChatClient`
- **ភ្នាក់ងារចុះបញ្ជីនៅបណ្តាញម៉ាស៊ីនមេ** នៅក្នុង Microsoft Foundry Agent Service V2 ហើយអាចមើលឃើញនៅផតថល Foundry

### ទទួលបានជំនួយ

- ចូលរួមក្នុង [សហគមន៍ Discord Microsoft Foundry](https://aka.ms/ai-agents/discord)
- ពិនិត្យឯកសារ README របស់មេរៀនសម្រាប់ដំណឹងជាក់លាក់
- ពិនិត្យ [README.md](./README.md) មេរៀនសង្ខេប
- មើល [រៀបចំមេរៀន](./00-course-setup/README.md) សម្រាប់សេចក្តីណែនាំលំអិត

### ឧបត្ថម្ភរួមចំណែក

នេះគឺជាគម្រោងសិក្សាបើកចំហរ។ ជំនួយទទួលស្វាគមន៍៖
- ធ្វើឲ្យឧទាហរណ៍កូដប្រសើរឡើង
- ដោះស្រាយ តួវចេញ ឬកំហុស
- បន្ថែមមតិយោបល់ច្បាស់លាស់
- ស្នើរសុំមេរៀនថ្មី
- បកប្រែទៅភាសាផ្សេងទៀត

មើល [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) សម្រាប់តម្រូវការបច្ចុប្បន្ន។

## បរិបទជាក់លាក់គម្រោង

### គាំទ្រភាសាច្រើន

ទីតាំងនេះប្រើប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិ:
- គាំទ្រភាសាជាង ៥០
- ការបកប្រែមករកនៅក្នុងថត `/translations/<lang-code>/`
- រត់ដោយកិច្ចការនៅ GitHub Actions គ្រប់គ្រងការបច្ចុប្បន្នភាព
- ឯកសារដើមជាភាសាអង់គ្លេសនៅឬតាមដើម repository

### រចនាសម្ព័ន្ធមេរៀន

មេរៀននីមួយៗអនុវត្តតាមលំដាប់តែមួយ:
1. រូបតុបតែងវីដេអូជាមួយតំណភ្ជាប់
2. មាតិកាមេរៀនសរសេរពីរ (README.md)
3. ឧទាហរណ៍កូដនៅក្នុងស៊ុមពហុ
4. គោលបំណងអប់រំ និងលក្ខខណ្ឌមុន
5. ឯកសាររៀនបន្ថែមភ្ជាប់

### ឈ្មោះឧទាហរណ៍កូដ

ទម្រង់: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - មេរៀន ១, MAF Python
- `14-sequential.ipynb` - មេរៀន ១៤, លំនាំ MAF មុខងារវិញ្ញាណ
- `16-python-agent-framework.ipynb` - មេរៀន ១៦, ភ្នាក់ងារគាំទ្រអតិថិជនផលិតកម្ម
- `17-local-agent-foundry-local.ipynb` - មេរៀន ១៧, ភ្នាក់ងារផ្ទាល់ក្នុងជាមួយ Foundry Local + Qwen

### ថតពិសេស

- `translated_images/` - រូបភាពបញ្ជាក់ភាសាសម្រាប់ការបកប្រែ
- `images/` - រូបភាពដើមសម្រាប់មាតិកាអង់គ្លេស
- `.devcontainer/` - ការកំណត់ឆ្នាំតភ្ជាប់ VS Code container
- `.github/` - កិច្ចការនិងទំរង់នៅ GitHub Actions

### បណ្ណាល័យចាំបាច់

បណ្ណាល័យគន្លឹះពី `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - គាំទ្រពិធីសាស្រ្ត Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - សេវាកម្ម Azure AI
- `azure-identity` - ការផ្ទៀងផ្ទាត់ Azure (AzureCliCredential)
- `azure-search-documents` - បញ្ចូល Azure AI Search
- `mcp[cli]` - គាំទ្រពិធីសាស្រ្ត Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->