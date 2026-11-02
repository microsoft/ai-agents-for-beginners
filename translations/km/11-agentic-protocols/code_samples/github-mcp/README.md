# Github MCP Server Example

## Description

នេះជាការបង្ហាញ (demo) ដែលបានបង្កើតសម្រាប់ AI Agents Hackathon ដែលបានរៀបចំតាមរយៈ Microsoft Reactor។

ឧបករណ៍នេះត្រូវបានប្រើដើម្បីផ្ដល់អនុសាសន៍គម្រោង hackathon ដែលមានមូលដ្ឋានលើ repos នៃអ្នកប្រើ Github។ វាត្រូវបានធ្វើដោយ៖

1. **Github Agent** - ប្រើ Github MCP Server ដើម្បីទាញយក repos និងព័ត៌មានអំពី repos ទាំងនោះ។
2. **Hackathon Agent** - ទទួលប្រភពទិន្នន័យពី Github Agent ហើយបង្កើតគំនិតគម្រោង hackathon ជាធ្វើច្នៃប្រឌិត ដោយផ្អែកលើគម្រោង ភាសាកម្មវិធីដែលអ្នកប្រើបានប្រើ និង track គម្រោងសម្រាប់ AI Agents hackathon។
3. **Events Agent** - ផ្អែកលើរបាយការណ៍ណែនាំពី hackathon agent នោះ Events Agent នឹងផ្ដល់អនុសាសន៍អំពីព្រឹត្តិការណ៍ដែលពាក់ព័ន្ធពីស៊េរី AI Agent Hackathon។

## Running the code 

### Environment Variables

ការបង្ហាញនេះប្រើ Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server និង Azure AI Search។

ធ្វើការត្រួតពិនិត្យថាអ្នកបានកំណត់អថេរបរិយាកាសសមរម្យដើម្បីប្រើឧបករណ៍ទាំងនេះ៖

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

ដើម្បីភ្ជាប់ទៅម៉ាស៊ីនមេ MCP ការបង្ហាញនេះប្រើ Chainlit ដើម្បីជាគ'interផេសសារ។

ដើម្បីរត់ម៉ាស៊ីនមេ សូមប្រើពាក្យបញ្ជាខាងក្រោមនៅក្នុង terminal របស់អ្នក៖

```bash
chainlit run app.py -w
```

នេះគួរតែបើកម៉ាស៊ីនមេ Chainlit របស់អ្នកនៅលើ `localhost:8000` និងបញ្ចូល Index នៅក្នុង Azure AI Search របស់អ្នកជាមួយខ្លឹមសារ `event-descriptions.md`។

## Connecting to the MCP Server

ដើម្បីភ្ជាប់ទៅ Github MCP Server សូមជ្រើសរើសរូបតំណភ្ជាប់ "plug" ខាងក្រោមប្រអប់សារ "Type your message here.."៖

![ភ្ជាប់ MCP](../../../../../translated_images/km/mcp-chainlit-1.7ed66d648e3cfb28.webp)

ពីទីនេះ អ្នកអាចចុចលើ "Connect an MCP" ដើម្បីបន្ថែម command សម្រាប់ភ្ជាប់ទៅ Github MCP Server៖

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

ប្តូរ "[YOUR PERSONAL ACCESS TOKEN]" ជា Personal Access Token តែមួយរបស់អ្នក។

បន្ទាប់ពីភ្ជាប់ អ្នកគួរមើលឃើញ (1) ខាងប្រហាក់នឹងរូបតំណភ្ជាប់ ដើម្បីបញ្ជាក់ថាវាភ្ជាប់រួច។ ប្រសិនបើមិនមែន សូមព្យាយាមចាប់ផ្ដើមឡើងវិញម៉ាស៊ីនមេ chainlit ដោយប្រើ `chainlit run app.py -w`។

## Using the Demo 

ដើម្បីចាប់ផ្តើម workflow របស់ agent សម្រាប់ផ្ដល់អនុសាសន៍គម្រោង hackathon អ្នកអាចវាយសារ​ដូចជា៖

"ណែនាំគម្រោង hackathon សម្រាប់អ្នកប្រើ Github koreyspace"

Router Agent នឹងវិភាគសំណើរបស់អ្នក និងកំណត់ថាការរួមបញ្ចូល agent មួយណា (GitHub, Hackathon, និង Events) មានសមត្ថភាពល្អបំផុតក្នុងការដោះស្រាយសំណួររបស់អ្នក។ Agents ទាំងនេះធ្វើការជាមួយគ្នាដើម្បីផ្ដល់អនុសាសន៍ប្រកបដោយភាពទូលំទូលាយ ដោយផ្អែកលើវិភាគ repository របស់ GitHub ការច្នៃប្រឌិតគំនិតគម្រោង និងព្រឹត្តិការណ៍បច្ចេកទេសដែលពាក់ព័ន្ធ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះបីជា​យើងខិតខំរកភាពត្រឹមត្រូវក្តី សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមានព័ត៌មានដែលមិនត្រូវបានបកប្រែបានជាក់លាក់។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានទុកមើលថាជាប្រភពផ្លូវការដោយក្តៅ។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ យើងផ្ដល់អនុសាសន៍ឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនោះ ឬការបកផ្សេងណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->