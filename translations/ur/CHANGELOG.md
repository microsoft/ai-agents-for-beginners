# تبدیلیوں کی فہرست

**AI Agents for Beginners** کورس میں تمام اہم تبدیلیاں اس فائل میں دستاویزی شکل میں موجود ہیں۔

## [ریلیز شدہ] — 2026-07-14

یہ ریلیز کورس کو دو تازہ منسوخ کیے گئے ماڈلز سے ہٹاتا ہے، باقی لیکچر نوٹس کو مستحکم Microsoft Agent Framework API پر منتقل کرتا ہے، اور Python نوٹس کو live Microsoft Foundry تعیناتی کے خلاف توثیق کرتا ہے۔

### تبدیلیاں

- **منسوخ شدہ ماڈلز سے ہٹایا گیا (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)۔** `gpt-4.1` اور `gpt-4.1-mini` دونوں اب منسوخ ہو چکے ہیں (اشاعت کی ریٹائرمنٹ کی تاریخ **14 اکتوبر 2026** ہے)۔ کورس کے تمام حوالہ جات (ڈاکیومنٹس، `.env.example`، Python/.NET نوٹس اور نمونے) کو غیر منسوخ شدہ `gpt-5-mini` سے تبدیل کیا گیا ہے۔ لیکچر 16 کے ماڈل روٹنگ کی مثال میں چھوٹا/بڑا تفریق `gpt-5-nano` (چھوٹا) اور `gpt-5-mini` (بڑا) کے ساتھ برقرار ہے۔ تیسرے فریق کی فائلوں ([15-browser-use/llms.txt](../../15-browser-use/llms.txt))، تاریخی GitHub Models متن، اور `azure-openai-to-responses` اسکل کی صلاحیت کے نوٹس کو جان بوجھ کر بدلا نہیں گیا۔
- **لیکچر 14 ہینڈ آف نوٹ بک کو مستحکم API پر منتقل کیا گیا۔** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) اب `agent_framework.orchestrations.HandoffBuilder` کو `.with_start_agent(...)`، `HandoffAgentUserRequest.create_response(...)`, `event.type` کی بنیاد پر اسٹریمنگ، اور `FoundryChatClient` کے ساتھ استعمال کرتا ہے (پہلے سے ہٹائے گئے pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` علامات کی جگہ)۔
- **لیکچر 14 human-in-the-loop نوٹ بک کو مستحکم API پر منتقل کیا گیا۔** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) اب `ctx.request_info(...)` + `@response_handler` کے ذریعے توقف کرتا ہے (ہٹائے گئے `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` کی جگہ)، `WorkflowBuilder(start_executor=..., output_executors=[...])` کے ساتھ تعمیر کرتا ہے، `default_options={"response_format": ...}` کے ذریعے منظم آؤٹ پٹ دیتا ہے، اور ایک اسکرپٹڈ جواب استعمال کرتا ہے تاکہ نوٹ بک بغیر روک ٹوک کے چل سکے (کوئی `input()` بلاکنگ نہیں)۔
- **ماحول کی ترتیب** ([.env.example](../../.env.example)) : ماڈل کی تعیناتی کے نام `gpt-5-mini` پر تبدیل کیے گئے؛ `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (لیکچر 16 روٹنگ) اور پہلے سے غائب `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (لیکچر 15 براؤزر استعمال) کو شامل کیا گیا۔
- **انحصارات** ([requirements.txt](../../requirements.txt)) : `agent-framework`, `agent-framework-foundry`, اور `agent-framework-openai` کو `~=1.10.0` پر رکھ دیا گیا ہے تاکہ ایک خود مطابقت رکھنے والا، تصدیق شدہ سیٹ ہو (1.11.0 تجرباتی بریکنگ تبدیلیاں لاتا ہے جو ان اسباق میں استعمال ہوتی ہیں)۔

### نوٹس اور معلوم حدود

- **live Microsoft Foundry کے خلاف توثیق کی گئی۔** Python نوٹس کو headless طریقے سے `nbconvert` کے ذریعے Microsoft Foundry پروجیکٹ میں `gpt-5-mini` (اور لیکچر 16 روٹنگ کے لئے `gpt-5-nano`) کے ساتھ چلایا گیا۔ اپنے پروجیکٹ میں مساوی غیر منسوخ شدہ ماڈلز تعینات کریں؛ نوٹس تعیناتی کا نام `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` سے پڑھتے ہیں۔
- **ابھی بھی کچھ اسباق کے لیے اضافی وسائل کی ضرورت ہے۔** لیکچر 05 کو Azure AI سرچ درکار ہے؛ لیکچر 08 کا Bing-گراؤنڈنگ ورک فلو (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) کو Bing کنکشن اور Microsoft Foundry Agent Service ہوسٹڈ ٹولز درکار ہیں؛ لیکچر 13 (Cognee) اور لیکچر 17 (Foundry Local) کو ان کے اپنے رن ٹائمز کی ضرورت ہے۔

## [ریلیز شدہ] — 2026-07-13

یہ ریلیز دو نئے اسباق شامل کرتا ہے جو تعیناتی کا دائرہ مکمل کرتے ہیں — Microsoft Foundry پر ایجنٹس کو بڑھانا اور ایک واحد ورک سٹیشن پر کرنا — نیز ایک سموتھ ٹیسٹ پائپ لائن، ریفریشڈ کورس نیویگیشن، نئے لرنر مہارتیں، اور اپ ڈیٹ شدہ برانڈنگ۔

### شامل کردہ

- **لیکچر 16 — Microsoft Foundry کے ساتھ اسکیل ایبل ایجنٹس کی تعیناتی۔** نیا سبق [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) اور چلنے والا نوٹ بک [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) جو ایک پروڈکشن کسٹمر سپورٹ ایجنٹ بناتا ہے (ٹولز، RAG، میموری، ماڈل روٹنگ، جوابی کیشنگ، انسانی منظوری، ایک تشخیصی گیٹ، اور OpenTelemetry ٹریسنگ)، ساتھ میں ڈیولپمنٹ/تعیناتی/رن ٹائم Mermaid خاکے، علم کی جانچ، ایک اسائنمنٹ، اور چیلنج۔
- **لیکچر 17 — Foundry Local اور Qwen کے ساتھ مقامی AI ایجنٹس بنانا۔** نیا سبق [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) اور نوٹ بک [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) جو مکمل طور پر آلے پر انجینئرنگ اسسٹنٹ بناتا ہے (Foundry Local کے ذریعے Qwen فنکشن کالنگ، سینڈ باکسڈ فائل ٹولز، Chroma کے ساتھ مقامی RAG، اختیاری مقامی MCP)، جس میں مقامی-صرف / مقامی-RAG / ٹول کالنگ خاکے، علم کی جانچ، ایک اسائنمنٹ، اور چیلنج شامل ہیں۔
- **سموک-ٹیسٹ پائپ لائن۔** نیا [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ورک فلو [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) اور اسباق 01, 04, 05, اور 16 میں تعینات ایجنٹس کے لیے ہر اسباق کے کیٹلاگ [tests/](./tests/README.md) میں، ایک انڈکس README کے ساتھ جو ہر کیٹلاگ کو اسباق اور ہوسٹ کیے گئے ایجنٹ کے نام سے جوڑتا ہے۔ لیکچر 16 میں "Validating a Deployed Agent with Smoke Tests" سیکشن شامل کیا گیا؛ لیکچر 01/04/05 میں اختیاری سموک-ٹیسٹ پوائنٹر۔
- **لرنر مہارتیں۔** نئی ایجنٹ مہارتیں `.agents/skills/` میں: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (لیکچر 16 اور 17 کی رہنمائی کو پیکج کرتا ہے)، اور [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (کیسے نوٹ بک نمونوں کو live Microsoft Foundry / Azure OpenAI سیٹ اپ کے خلاف توثیق کیا جائے)۔
- **نوٹ بک توثیق رنر۔** نیا [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) جو ہر Python نوٹ بک کو headless طریقے سے `nbconvert` کے ساتھ چلتا ہے اور PASS/FAIL میٹرکس پرنٹ کرتا ہے (مزید `results.json`). یہ ریپو روٹ اور Python کو خودکار طور پر پتہ لگاتا ہے، عام طور پر غیر کورس نوٹ بکس (`.venv`, `site-packages`, `translations`, اسکل ٹیمپلیٹ ایسٹس) اور `.NET` نوٹ بکس کو خارج کرتا ہے، اور `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, اور `-Python` کی حمایت کرتا ہے۔
- **کورس نیویگیشن۔** لیکچر 11-15 میں پچھلے/اگلے اسباق کے لنکس شامل کیے گئے (جو پہلے غائب تھے) تاکہ پورا کورس 00 → 18 دونوں سمتوں میں مربوط ہو۔
- **نئے تھمب نیلز۔** لیکچر 16 اور 17 کے لیے تھمب نیلز، مزید ریفریشڈ ریپوزٹری سوشل امیج [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (اب دو نئے اسباق اور `aka.ms/ai-agents-beginners` URL کا اشتہار دیتا ہے)۔
- **انحصارات** ([requirements.txt](../../requirements.txt)): لیکچر 17 کے لیے `foundry-local-sdk` اور `chromadb` شامل کیے گئے۔

### تبدیلیاں

- **مین [README.md](./README.md)** اسباق کی فہرست: لیکچر 16 اور 17 اب ان کے مواد سے جڑے ہوئے ہیں (پہلے "جلد آ رہا ہے" کہا جاتا تھا)؛ ریپوزٹری تصویر `repo-thumbnailv3.png` میں اپ ڈیٹ کی گئی۔
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: لیکچر 16 اور 17 کو اسباق کے لحاظ سے رہنما اور لرننگ پاتھس میں شامل کیا گیا، اور "Validating Deployed Agents with Smoke Tests" سیکشن شامل کیا گیا۔
- **[AGENTS.md](./AGENTS.md)**: اسباق کی تعداد/تفصیل (00–18) اپ ڈیٹ کی گئی، سموک-ٹیسٹنگ توثیقی سیکشن شامل کیا گیا، اور لیکچر 16/17 کے نمونے کے ناموں کی مثالیں شامل کی گئیں۔
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "پچھلا سبق" اب لیکچر 17 کی طرف اشارہ کرتا ہے (پہلے لیکچر 15 تھی)، زنجیر کو بند کرتے ہوئے۔
- **غیر منسوخ شدہ ماڈلز پر معیاری ماڈل حوالہ جات۔** پورے کورس (ڈاکس، `.env.example`, Python/.NET نوٹس اور نمونے) میں تمام `gpt-4o` / `gpt-4o-mini` حوالہ جات کو `gpt-4.1-mini` سے بدل دیا گیا ہے — `gpt-4o` (تمام ورژنز) 2026 میں ریٹائر ہو رہا ہے۔ لیکچر 16 کے ماڈل روٹنگ کی مثال میں چھوٹا/بڑا فرق `gpt-4.1-mini` (چھوٹا) اور `gpt-4.1` (بڑا) استعمال کرتی ہے۔ Python نوٹ بکس اب ماحول کی متغیرات (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) سے ماڈل منتخب کرتی ہیں، ہارڈ کوڈڈ ماڈل کے بجائے۔

### نوٹس اور معلوم حدود

- **live Azure کے خلاف نہیں چلایا گیا۔** نئے اسباق کے نوٹ بکس تعلیمی نمونے ہیں؛ انہیں اپنے Microsoft Foundry / Foundry Local سیٹ اپ کے خلاف چلائیں اور تصدیق کریں۔ سموک-ٹیسٹ ورک فلو کو اسباق کے ایجنٹ کی تعیناتی اور Azure OIDC راز (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) کو Foundry پروجیکٹ کے دائرہ کار میں **Azure AI User** کے کردار کے ساتھ ترتیب دینے کی ضرورت ہے۔
- **لیکچر 17 صرف مقامی ہے۔** اس کا کوئی Foundry Responses endpoint نہیں ہے، اس لیے سموک-ٹیسٹ ایکشن لاگو نہیں ہوتا؛ اسے اپنے ورک سٹیشن پر نوٹ بک چلانے سے تصدیق کریں۔

## [ریلیز شدہ] — 2026-07-06

یہ ریلیز کورس کو **Azure OpenAI Responses API** پر منتقل کرتا ہے، Microsoft Foundry اور Microsoft Agent Framework (MAF) پر مصنوعاتی نام کاری کو معیاری بناتا ہے، GitHub Models کو ریٹائر کرتا ہے، SDK ورژنز کو اپ ڈیٹ کرتا ہے، اور مقامی ماڈلز اور Foundry پر دیگر فریم ورکس کی ہوسٹنگ کے بارے میں نیا مواد شامل کرتا ہے۔

### شامل کردہ

- **منتقلی کی مہارت** — `.agents/skills/` کے تحت [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill انسٹال کی گئی ہے، جس میں اس کے حوالہ جات اور سکینر اسکرپٹ شامل ہیں، جو [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) سے ہے۔
- **Foundry Local (آلے پر ماڈلز چلانا)** — [00-course-setup/README.md](./00-course-setup/README.md) میں نیا "متبادل فراہم کنندہ: Foundry Local" سیکشن جو انسٹال (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, اور Microsoft Agent Framework کو `OpenAIChatClient` کے ذریعے FoundryLocalManager سے متصل کرنے پر مشتمل ہے۔
- **Microsoft Foundry پر LangChain / LangGraph ایجنٹس کی ہوسٹنگ** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) میں نیا سیکشن اور چلنے والا نمونہ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) جو `langchain-azure-ai[hosting]` اور `ResponsesHostServer` ( `/responses` پروٹوکول) استعمال کرتا ہے، [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) کی بنیاد پر۔
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) میں نیا "اصلی دنیا کی مثال: Microsoft Project Opal" سیکشن جو Opal کو ایک انٹرپرائز کمپیوٹر استعمال ایجنٹ کے طور پر فریم کرتا ہے اور اسے کورس کے تصورات سے جوڑتا ہے (human-in-the-loop, trust/security, planning, Skills)۔
- **دوسرا لیکچر 02 Python نمونہ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) شامل کیا گیا (دیکھیں "تبدیلیاں" — سابقہ Semantic Kernel نوٹ بک سے منتقل) اور اسے لیکچر README میں لنک کیا گیا۔
- **ماڈلز اور فراہم کنندگان** سیکشن [STUDY_GUIDE.md](./STUDY_GUIDE.md) میں شامل کیا گیا۔

### تبدیلیاں

- **Chat Completions → Responses API (Python).** وہ نمونے جو ماڈل کو براہ راست کال کرتے تھے، Chat Completions سے Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) پر منتقل کیے گئے، مستحکم Azure OpenAI `/openai/v1/` اینڈ پوائنٹ کے خلاف `OpenAI` کلائنٹ کا استعمال کرتے ہوئے (کوئی `api_version` نہیں)۔ متاثرہ نمونے شامل ہیں:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — مکمل فنکشن کالنگ واک تھرو (ٹول اسکیمہ Responses فارمیٹ میں فلیٹن کیا گیا، ٹول کے نتائج `function_call_output`, `max_output_tokens`، وغیرہ کے طور پر واپس کیے گئے)۔

- **GitHub ماڈلز → Azure OpenAI.** GitHub ماڈلز منسوخ ہو چکا ہے (جولائی 2026 میں بند ہو رہا ہے) اور Responses API کی حمایت نہیں کرتا۔ تمام GitHub ماڈلز کے کوڈ راہیں Python اور .NET نمونوں میں Azure OpenAI / Microsoft Foundry میں تبدیل کر دی گئی ہیں:
  - Python: لیسن 08 کے ورک فلو نوٹ بکس (`01`–`03`)، لیسن 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)۔
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ہمراہی `.md` دستاویزات، اور لیسن 08 کے dotNET ورک فلو نوٹ بکس/`.md` (`01`–`03`) اب `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` کے ساتھ `AzureCliCredential` استعمال کرتے ہیں۔
- **Semantic Kernel → Microsoft Agent Framework.** سابقہ `02-semantic-kernel.ipynb` کو Microsoft Agent Framework کے ساتھ Azure OpenAI (Responses API) استعمال کرنے کے لئے دوبارہ لکھا گیا اور اس کا نام `02-python-agent-framework-azure-openai.ipynb` رکھ دیا گیا۔
- **`FoundryChatClient` + `as_agent` پر معیاری تبادلہ۔** README اور نوٹ بک کوڈ جس میں `AzureAIProjectAgentProvider` کا حوالہ تھا، اسے لیسن 01 اور فریم ورک کے اپنے نمونوں میں استعمال ہونے والے معیاری پیٹرن پر مبنی کیا گیا: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` کے ساتھ `provider.as_agent(...)`۔ یہ ترمیمات لیسن 02-14 کے READMEs اور نوٹ بکس میں کی گئیں (جیسے لیسن 13 میموری، تمام لیسن 14 نوٹ بکس، `11-agentic-protocols/code_samples/github-mcp/app.py`)۔
- **مصنوعات کے نام۔** انگریزی مواد میں پورے متن میں نام تبدیل کئے گئے:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (بغیر تبدیلی: "Azure OpenAI", "Azure AI Search", "Azure AI Inference"، اور ماحول متغیرات کے نام۔)
- **انحصارات** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` فکس کیے گئے۔
  - `openai>=1.108.1` (Responses API کے لیے کم از کم) فکس کیا گیا۔
  - `azure-ai-inference` ہٹایا گیا (یہ صرف منتقل شدہ GitHub ماڈلز کے نمونوں کے لیے استعمال ہوتا تھا)۔
- **ماحولیاتی ترتیب** ([.env.example](../../.env.example)): GitHub ماڈلز کے متغیرات (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ختم کر دیے گئے؛ `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, اور اختیاری `AZURE_OPENAI_API_KEY` شامل کی گئی؛ اور نام گذاری Microsoft Foundry کے مطابق اپ ڈیٹ کی گئی۔
- **دستاویزات** — [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), اور [STUDY_GUIDE.md](./STUDY_GUIDE.md) کو اپ ڈیٹ کیا گیا (ماحول متغیرات سیٹ کرنا، تصدیقی اسنیپٹ، فراہم کنندہ کی رہنمائی، نام کاری)۔

### ہٹایا گیا

- GitHub ماڈلز کے شروع کرنے کے مراحل اور ماحول متغیرات کو سیٹ اپ دستاویزات سے ہٹا دیا گیا ہے (جسے Azure OpenAI / Microsoft Foundry نے تبدیل کر دیا ہے)۔

### سیکیورٹی / پرائیویسی (عوامی شیئرنگ کی صفائی)

- Jupyter نوٹ بک کی عملدرآمد کی آؤٹ پٹ صاف کی گئی جو حقیقی **Azure سبسکرپشن ID**, resource-group/ resource نام، اور Bing کنکشن ID کے علاوہ ڈویلپر کے **لوکل فائل کے راستے اور یوزر نام** ظاہر کر رہی تھیں، درج ذیل میں:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- تصدیق کی گئی کہ انگریزی متن میں کوئی API کیز، ٹوکنز، سبسکرپشن IDs، یا ذاتی راستے باقی نہیں ہیں (جو `GITHUB_TOKEN` حوالے باقی ہیں وہ GitHub Actions کے ٹوکن اور GitHub MCP سرور PAT ہیں جو جائز ہیں اور GitHub ماڈلز سے متعلق نہیں ہیں)۔

### نوٹس اور معروف حدود

- **عملدرآمد یا مرتب نہیں کیا گیا۔** یہ تعلیمی نمونے ہیں جو API/نام کاری کی درستگی کے لیے اپ ڈیٹ کیے گئے ہیں؛ انہیں لائیو Azure وسائل پر نہیں چلایا گیا اور .NET نمونہ جات اس ماحول میں مرتب نہیں کیے گئے۔ اپنے Microsoft Foundry / Azure OpenAI کی تعیناتی کے خلاف تصدیق کریں۔
- **ماڈل تعیناتی کو Responses API کی حمایت کرنا ضروری ہے۔** `gpt-4.1-mini`, `gpt-4.1`, یا `gpt-5.x` ماڈلز جیسی تعیناتی استعمال کریں۔ پرانے ماڈلز Responses کی بنیادی فعالیت کی حمایت کرتے ہیں لیکن ہر فیچر کی نہیں۔
- **اے جنٹ فریم ورک ورژن۔** نمونے تازہ ترین MAF (`>=1.10.0`) کو ہدف رکھتے ہیں۔ معیاری ایجنٹ سازی کال `client.as_agent(...)` ہے؛ APIs کو فریم ورک کی شائع شدہ دستاویزات اور انسٹال شدہ بلڈ کے خلاف تصدیق کیا گیا۔ اگر آپ کوئی مختلف ورژن استعمال کرتے ہیں تو میتھڈ کی دستیابی ( `as_agent` بمقابلہ `create_agent`) کی تصدیق کریں۔
- **لیسن 08 ورک فلو نوٹ بک 04** جان بوجھ کر `AzureAIAgentClient` (جو `agent-framework-azure-ai` سے ہے) کو برقرار رکھا گیا ہے کیونکہ یہ Microsoft Foundry Agent Service کی میزبانی کرنے والے ٹولز (Bing grounding, code interpreter) استعمال کرتا ہے؛ یہ پہلے سے Responses پر مبنی ہے۔
- **.NET کی ڈیفالٹ تعیناتی۔** دو لیسن 08 کے dotNET ورک فلو نمونے پہلے کسی خاص ماڈل کو ہارڈ کوڈ کرتے تھے؛ اب وہ ڈیفالٹ طور پر `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) استعمال کرتے ہیں۔ اگر کوئی نمونہ ملٹی موڈل/ویژن ان پٹ پر انحصار کرتا ہے تو `AZURE_OPENAI_DEPLOYMENT` کو مناسب ماڈل پر سیٹ کریں۔
- **Foundry Local** ایک OpenAI-مطابقت پذیر **Chat Completions** اینڈ پوائنٹ فراہم کرتا ہے اور مقامی ترقی کے لیے بنایا گیا ہے؛ مکمل Responses API فیچر سیٹ کے لیے Azure OpenAI / Microsoft Foundry استعمال کریں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->