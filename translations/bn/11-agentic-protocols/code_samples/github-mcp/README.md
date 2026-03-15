# Github MCP সার্ভার উদাহরণ

## বিবরণ

এটি Microsoft Reactor-এর মাধ্যমে আবহাওয়াকার AI Agents Hackathon-এর জন্য তৈরি করা একটি ডেমো ছিল।

এই টুলটি ব্যবহারকারীর Github রিপোগুলির উপর ভিত্তি করে হ্যাকাথন প্রকল্প সুপারিশ করার জন্য ব্যবহৃত হয়।
এটি করা হয়:

1. **Github Agent** - Github MCP সার্ভার ব্যবহার করে রিপো এবং সেই রিপো সম্পর্কে তথ্য সংগ্রহ করা।
2. **Hackathon Agent** - Github Agent থেকে প্রাপ্ত ডেটা নিয়ে ব্যবহারকারীর প্রকল্প, ব্যবহৃত ভাষাগুলো এবং AI Agents hackathon-এর প্রকল্প ট্র্যাকের ভিত্তিতে সৃজনশীল হ্যাকাথন প্রকল্প আইডিয়া বের করে।
3. **Events Agent** - Hackathon agent-এর পরামর্শের ভিত্তিতে, Events Agent AI Agent Hackathon সিরিজ থেকে প্রাসঙ্গিক ইভেন্ট সুপারিশ করবে।
## Running the code 

### Environment Variables

এই ডেমোটি Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server এবং Azure AI Search ব্যবহার করে।

এই টুলগুলোর জন্য সঠিক environment variables সেট করা আছে তা নিশ্চিত করুন:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

MCP সার্ভারের সাথে সংযোগ স্থাপনের জন্য, এই ডেমোটি Chainlit-কে একটি চ্যাট ইন্টারফেস হিসেবে ব্যবহার করে। 

সার্ভার চালানোর জন্য, আপনার টার্মিনালে নিম্নলিখিত কমান্ডটি ব্যবহার করুন:

```bash
chainlit run app.py -w
```

এটি আপনার Chainlit সার্ভার `localhost:8000`-এ চালু করা উচিত এবং একই সাথে `event-descriptions.md` কনটেন্ট দিয়ে আপনার Azure AI Search Index পূরণ করা উচিত। 

## Connecting to the MCP Server

Github MCP সার্ভারের সাথে সংযোগ করতে, চ্যাট বক্সের "Type your message here.." এর নিচে থাকা "plug" আইকনটি নির্বাচন করুন:

![MCP সংযোগ](../../../../../translated_images/bn/mcp-chainlit-1.7ed66d648e3cfb28.webp)

সেখান থেকে আপনি "Connect an MCP" ক্লিক করে Github MCP সার্ভারে সংযোগের কমান্ডটি যোগ করতে পারেন:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]"-কে আপনার বাস্তব Personal Access Token দিয়ে প্রতিস্থাপন করুন। 

সংযোগ করার পরে, নিশ্চিত করার জন্য plug আইকনটির পাশে একটি (1) দেখা উচিত। না দেখা গেলে, `chainlit run app.py -w` দিয়ে chainlit সার্ভারটি পুনরায় চালু করে দেখুন।

## Using the Demo 

হ্যাকাথন প্রকল্প সুপারিশের এজেন্ট ওয়ার্কফ্লো শুরু করতে, আপনি নিম্নলিখিত ধরনের একটি বার্তা টাইপ করতে পারেন: 

"Github ব্যবহারকারী koreyspace-এর জন্য হ্যাকাথন প্রকল্প সুপারিশ করুন"

Router Agent আপনার অনুরোধ বিশ্লেষণ করে নির্ধারণ করবে কোন এজেন্টগুলোর (GitHub, Hackathon, এবং Events) সংমিশ্রণ আপনার কুয়েরি পরিচালনার জন্য সবচেয়ে উপযুক্ত। এজেন্টগুলো একসাথে কাজ করে GitHub রিপোজিটরি বিশ্লেষণ, প্রকল্প ধারণা তৈরি, এবং প্রাসঙ্গিক টেক ইভেন্টের উপর ভিত্তি করে ব্যাপক সুপারিশ প্রদান করে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
দায়-অস্বীকৃতি:
এই নথিটি AI অনুবাদ সেবা Co-op Translator (https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যতটা সম্ভব নির্ভুলতার চেষ্টা করি, তবু অনুগ্রহ করে জানুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটিকে তার নিজ ভাষায় প্রামাণ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ নেওয়ার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে যে কোনও ভুল বোঝাবুঝি বা ভ্রান্ত ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->