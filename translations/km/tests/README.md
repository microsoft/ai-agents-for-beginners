# ការធ្វើតេស្តជាភ្នែកតំណាង

បង្ហាញនេះផ្ទុក **កាតាឡុកតេស្តឆេះ** សម្រាប់ភ្នាក់ងារដែលអ្នកបង្កើតក្នុងវគ្គសិក្សា។
ការតេស្តឆេះគឺជាការត្រួតពិនិត្យថោក និងលឿនមួយដែលភ្នាក់ងារ **Microsoft Foundry ដែលបានចែកចាយ
អាចទំនាក់ទំនងបាន តបស្នង ហើយអនុវត្តតាមការរំពឹងទុកនៃបញ្ជាបឋមរបស់វា។
វាជាការសាកល្បងដំបូងមួយ — មិនមែនជាផ្ទេរជំនួសសម្រាប់ដំណាក់កាលប៉ោងតម្លៃពេញលេញដែលអ្នករៀនក្នុង
[មេរៀនទី ១០](../10-ai-agents-production/README.md) និង
[មេរៀនទី ១៦](../16-deploying-scalable-agents/README.md)។

កាតាឡុកទាំងនោះត្រូវបានប្រើប្រាស់ដោយ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action តាមរយៈ [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
workflow។

## របៀបរត់

1. **ដាក់ឱ្យដំណើរការ agent សម្រាប់មេរៀន** ទៅ Microsoft Foundry ជា agent ដែលរដ្ឋបាល (មើល
   មេរៀនទី 16 សម្រាប់ workflow ការដាក់ចេញ)។ សូមចំណាំ **ឈ្មោះ agent** និង
   **ចុងបញ្ចប់គម្រោង Foundry** របស់អ្នក។
2. បន្ថែមសម្ងាត់ repository ទាំងនេះ (Settings → Secrets and variables → Actions)៖
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`។ អត្តសញ្ញាណសហជីព
   ត្រូវការរាល់តួនាទី **Azure AI User** នៅ **កម្រិតគម្រោង Foundry**។
3. ពីផ្ទាំង **Actions**, រត់ **Smoke-test hosted agents** និងជ្រើសរើស
   `tests_file` សម្រាប់មេរៀន, បន្ទាប់មកផ្គត់ផ្គង់ `agent_name` និង
   `project_endpoint` ដែលផ្គូផ្គងគ្នា។

## កាតាឡុក → មេរៀន → ឈ្មោះ agent

| កាតាឡុក | មេរៀន | ដាក់ agent ជា |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## មេរៀនណាខ្លះមាន smoke tests?

ការសាកល្បង smoke ត្រូវបានអនុវត្តសម្រាប់មេរៀនដែលអ្នក **ដាក់ agent** ដែលចម្លើយអត្ថបទរបស់វា
អាចត្រូវបានបញ្ជាក់ប្រឆាំងនឹងមាតិកាដែលបានស្គាល់។ មេរៀនដែលជាសេចក្ដីគំនិត ទៅតែប្រតិបត្តិការត្រឹមក្នុងតំបន់
ឬបង្កើតលទ្ធផលច្នៃប្រឌិតដែលមិនអាចកំណត់ទិសបាន ត្រូវបានដកចេញយ៉ាងច្បាស់៖

- **មេរៀនទី 17 (បង្កើត Local AI Agents)** រត់ពេញលេញនៅលើកុំព្យូទ័ររបស់អ្នកជាមួយ
  Foundry Local ហើយមិនបង្ហាញចុងបញ្ចប់ Foundry Responses ទេ ដូច្នេះ
  សកម្មភាពនេះមិនអាចអនុវត្តបាន។ សូមផ្ទៀងផ្ទាត់វាតាមរយៈការរត់ notebook ដោយផ្ទាល់។
- មេរៀនលំដាប់រចនា និងទ្រឹស្តី (02, 03, 06, 07, 09, 12) មិនផ្តល់ agent ដែលអាចដាក់ចេញមួយកន្លែងសម្រាប់
  ការសាកល្បង smoke ទេ។

## ស្ដង់ដារកាតាឡុក (យោងយ៉ាងឆាប់រហ័ស)

គ្រប់កាតាឡុកគឺជាឯកសារ JSON ដែលមានអារេ `tests` កម្រាស់កំពូល។ គ្រប់វត្ថុចូលបញ្ចូលបញ្ចូន POST
ជាការជំរុញដំណើរការ​មួយ និងធានាលើការឆ្លើយតប៖

| វាល | អត្ថន័យ |
|-------|---------|
| `id` | អត្តសញ្ញាណជំហានតែមួយដែលបានបោះពុម្ពនៅក្នុងកំណត់ហេតុ។ |
| `description` | គោលបំណងដែលអាចអានដោយមនុស្សបាន។ |
| `prompt` | សារ​ដែលបានផ្ញើទៅភ្នាក់ងារ។ |
| `assertions.status` | ស្ថានភាព HTTP ប្រើរង់ចាំ (លំនាំដើម 200)។ |
| `assertions.contains_any` | អនុញ្ញាតបើការឆ្លើយមានអត្ថបទខ្នាតតូចណាមួយក្នុងចំណោមទាំងនេះ។ |
| `assertions.contains_all` | អនុញ្ញាតបើការឆ្លើយមានអត្ថបទខ្នាតតូចទាំងអស់។ |
| `assertions.contains_none` | អនុញ្ញាតបើការឆ្លើយគ្មានអត្ថបទខ្នាតតូចណាមួយផងដែរ។ |
| `save_response_id_as` | រក្សាទុក id ចម្លើយសម្រាប់ជំហានមួយចំនួនបន្ទាប់។ |
| `use_previous_response_id` | ផ្ញើជុំសងខាងនេះភ្ជាប់ជាមួយ id ចម្លើយដែលបានរក្សាទុក។ |

ការត្រួតពិនិត្យគឺជាការត្រួតពិនិត្យអត្ថបទខ្នាតតូចមិនគិតបំណង។ មើល
[ឯកសារសកម្មភាព](https://github.com/marketplace/actions/ai-smoke-test) សម្រាប់
ស្កីម៉ាផ្ទៀងផ្ទាត់ពេញលេញ រួមទាំងធនធានសន្ទនា​ដែលគ្រប់គ្រងដោយ Foundry។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->