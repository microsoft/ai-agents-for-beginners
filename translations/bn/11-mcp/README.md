<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:03:19+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "bn"
}
-->
# পাঠ ১১: মডেল কনটেক্সট প্রোটোকল (MCP) ইন্টিগ্রেশন

## মডেল কনটেক্সট প্রোটোকল (MCP)-এর পরিচিতি

মডেল কনটেক্সট প্রোটোকল (MCP) হলো একটি আধুনিক ফ্রেমওয়ার্ক, যা AI মডেল এবং ক্লায়েন্ট অ্যাপ্লিকেশনের মধ্যে যোগাযোগকে মানসম্মত করার জন্য ডিজাইন করা হয়েছে। MCP AI মডেল এবং সেগুলো ব্যবহারের অ্যাপ্লিকেশনের মধ্যে একটি সেতু হিসেবে কাজ করে, মডেলের বাস্তবায়ন যাই হোক না কেন, একটি সুনির্দিষ্ট ইন্টারফেস প্রদান করে।

MCP-এর মূল দিকগুলো:

- **মানসম্মত যোগাযোগ**: MCP অ্যাপ্লিকেশন এবং AI মডেলের মধ্যে যোগাযোগের জন্য একটি সাধারণ ভাষা প্রতিষ্ঠা করে
- **উন্নত কনটেক্সট ব্যবস্থাপনা**: AI মডেলের কাছে প্রাসঙ্গিক তথ্য দক্ষতার সাথে প্রেরণ করার সুযোগ দেয়
- **ক্রস-প্ল্যাটফর্ম সামঞ্জস্যতা**: C#, Java, JavaScript, Python, এবং TypeScript সহ বিভিন্ন প্রোগ্রামিং ভাষায় কাজ করে
- **সহজ ইন্টিগ্রেশন**: ডেভেলপারদের জন্য বিভিন্ন AI মডেল তাদের অ্যাপ্লিকেশনে সহজে সংযুক্ত করার সুযোগ দেয়

MCP AI এজেন্ট ডেভেলপমেন্টে বিশেষভাবে গুরুত্বপূর্ণ, কারণ এটি এজেন্টদের বিভিন্ন সিস্টেম এবং ডেটা সোর্সের সাথে একটি একীভূত প্রোটোকলের মাধ্যমে যোগাযোগ করতে সক্ষম করে, যা এজেন্টদের আরও নমনীয় এবং শক্তিশালী করে তোলে।

## শেখার লক্ষ্য
- MCP কী এবং AI এজেন্ট ডেভেলপমেন্টে এর ভূমিকা বোঝা
- GitHub ইন্টিগ্রেশনের জন্য MCP সার্ভার সেটআপ এবং কনফিগার করা
- MCP টুল ব্যবহার করে একটি মাল্টি-এজেন্ট সিস্টেম তৈরি করা
- Azure Cognitive Search-এর সাথে RAG (Retrieval Augmented Generation) বাস্তবায়ন করা

## প্রয়োজনীয়তা
- Python 3.8+
- Node.js 14+
- Azure সাবস্ক্রিপশন
- GitHub অ্যাকাউন্ট
- Semantic Kernel-এর মৌলিক ধারণা

## সেটআপ নির্দেশাবলী

1. **পরিবেশ সেটআপ**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure পরিষেবাগুলি কনফিগার করুন**
   - একটি Azure Cognitive Search রিসোর্স তৈরি করুন
   - Azure OpenAI পরিষেবা সেটআপ করুন
   - `.env` ফাইলে পরিবেশ ভেরিয়েবল কনফিগার করুন

3. **MCP সার্ভার সেটআপ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## প্রকল্প কাঠামো

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## মূল উপাদানসমূহ

### ১. মাল্টি-এজেন্ট সিস্টেম
- GitHub এজেন্ট: রিপোজিটরি বিশ্লেষণ
- Hackathon এজেন্ট: প্রকল্পের সুপারিশ
- Events এজেন্ট: প্রযুক্তি ইভেন্টের পরামর্শ

### ২. Azure ইন্টিগ্রেশন
- ইভেন্ট ইনডেক্সিংয়ের জন্য Cognitive Search
- এজেন্ট ইন্টেলিজেন্সের জন্য Azure OpenAI
- RAG প্যাটার্ন বাস্তবায়ন

### ৩. MCP টুলস
- GitHub রিপোজিটরি বিশ্লেষণ
- কোড পরিদর্শন
- মেটাডেটা এক্সট্রাকশন

## কোড ওয়াকথ্রু

এই নমুনাটি প্রদর্শন করে:
1. MCP সার্ভার ইন্টিগ্রেশন
2. মাল্টি-এজেন্ট অর্কেস্ট্রেশন
3. Azure Cognitive Search ইন্টিগ্রেশন
4. RAG প্যাটার্ন বাস্তবায়ন

মূল বৈশিষ্ট্য:
- রিয়েল-টাইম GitHub রিপোজিটরি বিশ্লেষণ
- বুদ্ধিমান প্রকল্পের সুপারিশ
- Azure Search ব্যবহার করে ইভেন্ট ম্যাচিং
- Chainlit দিয়ে স্ট্রিমিং রেসপন্স

## নমুনা চালানো

বিস্তারিত সেটআপ নির্দেশাবলী এবং আরও তথ্যের জন্য, [Github MCP Server Example README](./code_samples/github-mcp/README.md) দেখুন।

1. MCP সার্ভার শুরু করুন:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. অ্যাপ্লিকেশন চালু করুন:
   ```bash
   chainlit run app.py -w
   ```

3. ইন্টিগ্রেশন পরীক্ষা করুন:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## সমস্যা সমাধান

সাধারণ সমস্যা এবং সমাধান:
1. MCP সংযোগ সমস্যা
   - নিশ্চিত করুন সার্ভার চালু আছে
   - পোর্টের প্রাপ্যতা পরীক্ষা করুন
   - GitHub টোকেন যাচাই করুন

2. Azure Search সমস্যা
   - সংযোগ স্ট্রিং যাচাই করুন
   - ইনডেক্সের অস্তিত্ব নিশ্চিত করুন
   - ডকুমেন্ট আপলোড যাচাই করুন

## পরবর্তী ধাপ
- অতিরিক্ত MCP টুলস অন্বেষণ করুন
- কাস্টম এজেন্ট বাস্তবায়ন করুন
- RAG ক্ষমতাগুলি উন্নত করুন
- আরও ইভেন্ট সোর্স যোগ করুন
- **উন্নত**: এজেন্ট-টু-এজেন্ট যোগাযোগের উদাহরণের জন্য [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) দেখুন

## রিসোর্স
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP ডকুমেন্টেশন](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search ডকস](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel গাইড](https://learn.microsoft.com/semantic-kernel/)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা তার জন্য দায়ী থাকব না।