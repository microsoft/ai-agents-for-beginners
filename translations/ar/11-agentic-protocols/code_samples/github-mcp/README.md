# مثال خادم Github MCP

## الوصف

هذا عرض توضيحي تم إنشاؤه لمسابقة AI Agents Hackathon المستضافة عبر Microsoft Reactor.

تُستخدم هذه الأدوات للتوصية بمشاريع هاكاثون بناءً على مستودعات Github للمستخدم. يتم ذلك من خلال:

1. **Github Agent** - استخدام خادم Github MCP لاسترداد المستودعات والمعلومات حول تلك المستودعات.
2. **Hackathon Agent** - يأخذ البيانات من Github Agent ويبتكر أفكار مشاريع هاكاثون إبداعية بناءً على المشاريع واللغات المستخدمة من قبل المستخدم ومسارات المشاريع لمسابقة AI Agents Hackathon.
3. **Events Agent** - استنادًا إلى اقتراحات Hackathon Agent، سيقوم Events Agent بتوصية فعاليات ذات صلة من سلسلة AI Agent Hackathon.

## تشغيل الكود 

### متغيرات البيئة

يستخدم هذا العرض التوضيحي Microsoft Agent Framework وAzure OpenAI Service وخادم Github MCP وAzure AI Search.

تأكد من تعيين متغيرات البيئة المناسبة لاستخدام هذه الأدوات:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## تشغيل خادم Chainlit

للاتصال بخادم MCP، يستخدم هذا العرض التوضيحي Chainlit كواجهة دردشة. 

لتشغيل الخادم، استخدم الأمر التالي في الطرفية الخاصة بك:

```bash
chainlit run app.py -w
```

ينبغي أن يبدأ هذا خادم Chainlit على `localhost:8000` بالإضافة إلى ملء فهرس Azure AI Search بمحتوى `event-descriptions.md`. 

## الاتصال بخادم MCP

للاتصال بخادم Github MCP، اختر أيقونة "plug" أسفل مربع الدردشة "Type your message here..":

![الاتصال بـ MCP](../../../../../translated_images/ar/mcp-chainlit-1.7ed66d648e3cfb28.webp)

من هناك يمكنك النقر على "Connect an MCP" لإضافة الأمر للاتصال بخادم Github MCP:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

استبدل "[YOUR PERSONAL ACCESS TOKEN]" برمز Personal Access Token الفعلي الخاص بك. 

بعد الاتصال، ينبغي أن ترى (1) بجانب أيقونة plug لتأكيد أنه متصل. إذا لم يظهر، حاول إعادة تشغيل خادم chainlit باستخدام `chainlit run app.py -w`.

## استخدام العرض التوضيحي 

لبدء سير عمل الوكلاء لتوصية مشاريع الهاكاثون، يمكنك كتابة رسالة مثل: 

"قم بتوصية مشاريع هاكاثون لمستخدم Github koreyspace"

سيقوم Router Agent بتحليل طلبك وتحديد أي مجموعة من الوكلاء (GitHub وHackathon وEvents) هي الأنسب لمعالجة استفسارك. يعمل الوكلاء معًا لتقديم توصيات شاملة بناءً على تحليل مستودعات GitHub وتوليد أفكار المشاريع والفعاليات التقنية ذات الصلة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co‑op Translator (https://github.com/Azure/co-op-translator). بينما نسعى إلى الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي والموثوق. للمعلومات الحساسة أو الحيوية، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناشئ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->