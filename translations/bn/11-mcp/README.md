<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:12:45+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "bn"
}
-->
# পাঠ ১১: মডেল কনটেক্সট প্রোটোকল (MCP) ইন্টিগ্রেশন

## মডেল কনটেক্সট প্রোটোকল (MCP) পরিচিতি

মডেল কনটেক্সট প্রোটোকল (MCP) একটি আধুনিক ফ্রেমওয়ার্ক যা AI মডেল এবং ক্লায়েন্ট অ্যাপ্লিকেশনের মধ্যে যোগাযোগকে মানসম্মত করার জন্য ডিজাইন করা হয়েছে। MCP AI মডেল এবং সেগুলো ব্যবহারকারী অ্যাপ্লিকেশনের মধ্যে একটি সেতু হিসেবে কাজ করে, যা মডেলের বাস্তবায়ন যাই হোক না কেন একটি সঙ্গতিপূর্ণ ইন্টারফেস প্রদান করে।

MCP-এর গুরুত্বপূর্ণ দিকগুলো:

- **মানসম্মত যোগাযোগ**: MCP অ্যাপ্লিকেশন এবং AI মডেলের মধ্যে যোগাযোগের জন্য একটি সাধারণ ভাষা প্রতিষ্ঠা করে
- **উন্নত কনটেক্সট ব্যবস্থাপনা**: AI মডেলে প্রাসঙ্গিক তথ্য দক্ষতার সাথে প্রেরণ করার সুযোগ দেয়
- **ক্রস-প্ল্যাটফর্ম সামঞ্জস্য**: C#, Java, JavaScript, Python, এবং TypeScript সহ বিভিন্ন প্রোগ্রামিং ভাষায় কাজ করে
- **সহজ ইন্টিগ্রেশন**: ডেভেলপারদের জন্য বিভিন্ন AI মডেল তাদের অ্যাপ্লিকেশনে সহজে সংযুক্ত করার সুযোগ দেয়

AI এজেন্ট ডেভেলপমেন্টে MCP বিশেষভাবে গুরুত্বপূর্ণ কারণ এটি এজেন্টদের বিভিন্ন সিস্টেম এবং ডেটা সোর্সের সাথে একটি একক প্রোটোকলের মাধ্যমে যোগাযোগ করতে সক্ষম করে, যা এজেন্টদের আরও নমনীয় এবং শক্তিশালী করে তোলে।

## শেখার লক্ষ্য
- MCP কী এবং AI এজেন্ট ডেভেলপমেন্টে এর ভূমিকা বোঝা
- GitHub ইন্টিগ্রেশনের জন্য MCP সার্ভার সেটআপ এবং কনফিগার করা
- MCP টুল ব্যবহার করে একটি মাল্টি-এজেন্ট সিস্টেম তৈরি করা
- Azure Cognitive Search ব্যবহার করে RAG (Retrieval Augmented Generation) বাস্তবায়ন করা

## পূর্বশর্ত
- Python 3.8+
- Node.js 14+
- Azure সাবস্ক্রিপশন
- GitHub অ্যাকাউন্ট
- Semantic Kernel সম্পর্কে মৌলিক ধারণা

## সেটআপ নির্দেশনা

1. **পরিবেশ সেটআপ**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure সার্ভিস কনফিগার করুন**
   - একটি Azure Cognitive Search রিসোর্স তৈরি করুন
   - Azure OpenAI সার্ভিস সেটআপ করুন
   - `.env` ফাইলে পরিবেশ ভেরিয়েবল কনফিগার করুন

3. **MCP সার্ভার সেটআপ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## প্রকল্পের কাঠামো

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

## মূল উপাদান

### ১. মাল্টি-এজেন্ট সিস্টেম
- GitHub এজেন্ট: রিপোজিটরি বিশ্লেষণ
- Hackathon এজেন্ট: প্রকল্পের সুপারিশ
- Events এজেন্ট: প্রযুক্তি ইভেন্টের পরামর্শ

### ২. Azure ইন্টিগ্রেশন
- ইভেন্ট ইনডেক্সিংয়ের জন্য Cognitive Search
- এজেন্ট ইন্টেলিজেন্সের জন্য Azure OpenAI
- RAG প্যাটার্ন বাস্তবায়ন

### ৩. MCP টুল
- GitHub রিপোজিটরি বিশ্লেষণ
- কোড পরিদর্শন
- মেটাডেটা এক্সট্রাকশন

## কোড ওয়াকথ্রু

উদাহরণটি প্রদর্শন করে:
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

বিস্তারিত সেটআপ নির্দেশনা এবং আরও তথ্যের জন্য [Github MCP Server Example README](./code_samples/github-mcp/README.md) দেখুন।

1. MCP সার্ভার চালু করুন:
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

## সমস্যার সমাধান

সাধারণ সমস্যা এবং সমাধান:
1. MCP সংযোগ সমস্যা
   - নিশ্চিত করুন সার্ভার চালু আছে
   - পোর্ট উপলব্ধতা পরীক্ষা করুন
   - GitHub টোকেন যাচাই করুন

2. Azure Search সমস্যা
   - সংযোগ স্ট্রিং যাচাই করুন
   - ইনডেক্সের অস্তিত্ব পরীক্ষা করুন
   - ডকুমেন্ট আপলোড যাচাই করুন

## পরবর্তী পদক্ষেপ
- অতিরিক্ত MCP টুল অন্বেষণ করুন
- কাস্টম এজেন্ট বাস্তবায়ন করুন
- RAG সক্ষমতা উন্নত করুন
- আরও ইভেন্ট সোর্স যোগ করুন
- **উন্নত**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) দেখুন এজেন্ট-টু-এজেন্ট যোগাযোগের উদাহরণের জন্য

## রিসোর্স
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।