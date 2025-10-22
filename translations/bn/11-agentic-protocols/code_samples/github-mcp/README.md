<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T13:30:04+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "bn"
}
-->
# Github MCP Server Example

## বিবরণ

এটি একটি ডেমো যা Microsoft Reactor-এর মাধ্যমে আয়োজিত AI Agents Hackathon-এর জন্য তৈরি করা হয়েছিল।

এই টুলটি ব্যবহারকারীর Github রিপোজিটরির উপর ভিত্তি করে হ্যাকাথন প্রকল্পের সুপারিশ করার জন্য ব্যবহৃত হয়। এটি নিম্নলিখিত উপায়ে কাজ করে:

1. **Github Agent** - Github MCP Server ব্যবহার করে রিপোজিটরি এবং সেগুলোর তথ্য সংগ্রহ করে।
2. **Hackathon Agent** - Github Agent থেকে প্রাপ্ত ডেটা ব্যবহার করে ব্যবহারকারীর প্রকল্প, ব্যবহৃত প্রোগ্রামিং ভাষা এবং AI Agents হ্যাকাথনের প্রকল্প ট্র্যাকের উপর ভিত্তি করে সৃজনশীল হ্যাকাথন প্রকল্পের ধারণা তৈরি করে।
3. **Events Agent** - Hackathon Agent-এর সুপারিশ অনুযায়ী, Events Agent AI Agent Hackathon সিরিজের প্রাসঙ্গিক ইভেন্টগুলোর সুপারিশ করে।

## কোড চালানো

### পরিবেশ ভেরিয়েবল

এই ডেমোতে Azure Open AI Service, Semantic Kernel, Github MCP Server এবং Azure AI Search ব্যবহার করা হয়েছে।

এই টুলগুলো ব্যবহারের জন্য সঠিক পরিবেশ ভেরিয়েবল সেট করা নিশ্চিত করুন:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit সার্ভার চালানো

MCP সার্ভারের সাথে সংযোগ স্থাপনের জন্য এই ডেমোতে Chainlit চ্যাট ইন্টারফেস হিসেবে ব্যবহার করা হয়েছে।

সার্ভার চালানোর জন্য, আপনার টার্মিনালে নিচের কমান্ডটি ব্যবহার করুন:

```bash
chainlit run app.py -w
```

এটি আপনার Chainlit সার্ভার `localhost:8000`-এ চালু করবে এবং `event-descriptions.md` কন্টেন্ট দিয়ে আপনার Azure AI Search Index পূরণ করবে।

## MCP সার্ভারের সাথে সংযোগ স্থাপন

Github MCP Server-এর সাথে সংযোগ স্থাপনের জন্য, "Type your message here.." চ্যাট বক্সের নিচে থাকা "plug" আইকনে ক্লিক করুন:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.bn.png)

এরপর "Connect an MCP" ক্লিক করে Github MCP Server-এর সাথে সংযোগ স্থাপনের কমান্ড যোগ করুন:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" এর জায়গায় আপনার প্রকৃত Personal Access Token বসান।

সংযোগ স্থাপনের পর, প্লাগ আইকনের পাশে একটি (1) দেখতে পাবেন যা নিশ্চিত করবে যে এটি সংযুক্ত হয়েছে। যদি না হয়, তাহলে `chainlit run app.py -w` দিয়ে Chainlit সার্ভার পুনরায় চালু করার চেষ্টা করুন।

## ডেমো ব্যবহার করা

হ্যাকাথন প্রকল্পের সুপারিশের এজেন্ট ওয়ার্কফ্লো শুরু করতে, আপনি একটি বার্তা লিখতে পারেন যেমন:

"Github ব্যবহারকারী koreyspace-এর জন্য হ্যাকাথন প্রকল্পের সুপারিশ করুন"

Router Agent আপনার অনুরোধ বিশ্লেষণ করবে এবং কোন এজেন্টের (GitHub, Hackathon, এবং Events) সংমিশ্রণ আপনার প্রশ্নের জন্য সবচেয়ে উপযুক্ত তা নির্ধারণ করবে। এজেন্টগুলো একসাথে কাজ করে Github রিপোজিটরি বিশ্লেষণ, প্রকল্পের ধারণা এবং প্রাসঙ্গিক প্রযুক্তি ইভেন্টের উপর ভিত্তি করে ব্যাপক সুপারিশ প্রদান করবে।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় লেখা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।