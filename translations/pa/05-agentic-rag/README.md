[![Agentic RAG](../../../translated_images/pa/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਵੇਖੋ)_

# Agentic RAG

ਇਹ ਪਾਠ Agentic Retrieval-Augmented Generation (Agentic RAG) ਦਾ ਵਿਸਤ੍ਰਿਤ ਜਾਇਜ਼ਾ ਦਿੰਦਾ ਹੈ, ਜੋ ਕਿ ਇੱਕ ਨਵਾਂ AI ਪੈਰਾਡਾਇਮ ਹੈ ਜਿੱਥੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਬਾਹਰੀ ਸਰੋਤਾਂ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਦੇ ਹੋਏ ਆਪਣੇ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਯੋਜਨਾ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਂਦੇ ਹਨ। ਸਥਿਰ retrieval-then-read ਪੈਟਰਨਾਂ ਦੇ ਵਿਰੁੱਧ, Agentic RAG ਵਿੱਚ LLM ਨੂੰ ਵਾਰ-ਵਾਰ ਕਾਲ ਕਰਨਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਟੂਲ ਜਾਂ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ ਸੰਰਚਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ। ਸਿਸਟਮ ਨਤੀਜਿਆਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ, ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ, ਜਰੂਰਤ ਪੈਣ 'ਤੇ ਵਾਧੂ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਇਹ ਚੱਕਰ ਤਦ ਤੱਕ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਜਦ ਤੱਕ ਸੰਤੋਸ਼ਜਨਕ ਹੱਲ ਨਹੀਂ ਮਿਲ ਜਾਂਦਾ।

## ਜਾਣ ਪਛਾਣ

ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖੋਗੇ:

- **Agentic RAG ਨੂੰ ਸਮਝੋ:** AI ਦੇ ਇਸ ਨਵੇਂ ਪੈਰਾਡਾਇਮ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ ਜਿੱਥੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਦੇ ਹੋਏ ਆਪਣੇ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਯੋਜਨਾ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਂਦੇ ਹਨ।
- **Iterative Maker-Checker Style ਨੂੰ ਸਮਝੋ:** LLM ਨੂੰ ਵਾਰ-ਵਾਰ ਕਾਲ ਕਰਨ ਦਾ ਚੱਕਰ ਸਮਝੋ, ਜਿਸ ਵਿੱਚ ਟੂਲ ਜਾਂ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ ਸੰਰਚਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ, ਜੋ ਸਹੀ ਨਤੀਜਿਆਂ ਨੂੰ ਸੁਧਾਰਨ ਅਤੇ ਗਲਤ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।
- **ਵਰਤੋਂ ਦੇ ਪ੍ਰਯੋਗਾਤਮਕ ਪੱਖ:** ਉਹ ਸਥਿਤੀਆਂ ਪਛਾਣੋ ਜਿੱਥੇ Agentic RAG ਬਹੁਤ ਵਧੀਆ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ correctness-first environments, ਜਟਿਲ ਡਾਟਾਬੇਸ ਇੰਟਰੈਕਸ਼ਨ, ਅਤੇ ਲੰਬੇ workflows।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਹ ਸਮਝ ਪਾ ਲੋਗੇ:

- **Agentic RAG ਦੀ ਸਮਝ:** AI ਦੇ ਇਸ ਨਵੇਂ ਪੈਰਾਡਾਇਮ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ ਜਿੱਥੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਦੇ ਹੋਏ ਆਪਣੇ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਯੋਜਨਾ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਂਦੇ ਹਨ।
- **Iterative Maker-Checker Style:** LLM ਨੂੰ ਵਾਰ-ਵਾਰ ਕਾਲ ਕਰਨ ਦਾ ਚੱਕਰ ਸਮਝੋ, ਜਿਸ ਵਿੱਚ ਟੂਲ ਜਾਂ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ ਸੰਰਚਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ, ਜੋ ਸਹੀ ਨਤੀਜਿਆਂ ਨੂੰ ਸੁਧਾਰਨ ਅਤੇ ਗਲਤ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।
- **ਤਰਕ ਪ੍ਰਕਿਰਿਆ ਦੀ ਮਾਲਕੀ:** ਸਿਸਟਮ ਦੀ ਸਮਝ ਪਾਓ ਕਿ ਇਹ ਆਪਣੀ reasoning process ਨੂੰ ਮਾਲਕਾਨਾ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਦਾ ਹੈ, ਅਤੇ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਪੂਰਨ ਤੌਰ 'ਤੇ ਆਪਣੇ ਫੈਸਲੇ ਲੈਂਦਾ ਹੈ।
- **Workflow:** ਸਮਝੋ ਕਿ ਇੱਕ agentic ਮਾਡਲ ਕਿਵੇਂ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਮਾਰਕੀਟ ਟ੍ਰੈਂਡ ਰਿਪੋਰਟਾਂ ਨੂੰ ਰਿਟਰੀਵ ਕਰਦਾ ਹੈ, ਮੁਕਾਬਲੇਦਾਰ ਡਾਟਾ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ, ਅੰਦਰੂਨੀ ਵਿਕਰੀ ਮੈਟ੍ਰਿਕਸ ਨੂੰ ਸਬੰਧਿਤ ਕਰਦਾ ਹੈ, ਨਤੀਜਿਆਂ ਨੂੰ ਸੰਕਲਿਤ ਕਰਦਾ ਹੈ, ਅਤੇ ਰਣਨੀਤੀ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ।
- **Iterative Loops, Tool Integration, ਅਤੇ Memory:** ਸਿਸਟਮ ਦੇ ਲੂਪਡ ਇੰਟਰੈਕਸ਼ਨ ਪੈਟਰਨ, ਸਟੇਟ ਅਤੇ ਮੈਮਰੀ ਨੂੰ ਕਾਇਮ ਰੱਖਣ ਦੀ ਸਮਝ ਪਾਓ, ਤਾਂ ਜੋ ਦੁਹਰਾਏ ਗਏ ਲੂਪਾਂ ਤੋਂ ਬਚਿਆ ਜਾ ਸਕੇ ਅਤੇ ਸੂਚਿਤ ਫੈਸਲੇ ਲਏ ਜਾ ਸਕਣ।
- **Failure Modes ਅਤੇ Self-Correction ਨੂੰ ਹੱਲ ਕਰਨਾ:** ਸਿਸਟਮ ਦੇ ਮਜ਼ਬੂਤ self-correction mechanisms ਦੀ ਖੋਜ ਕਰੋ, ਜਿਸ ਵਿੱਚ iteration, re-querying, diagnostic tools ਦੀ ਵਰਤੋਂ, ਅਤੇ ਮਨੁੱਖੀ ਨਿਗਰਾਨੀ ਸ਼ਾਮਲ ਹੈ।
- **Agency ਦੀਆਂ ਹੱਦਾਂ:** Agentic RAG ਦੀਆਂ ਸੀਮਾਵਾਂ ਨੂੰ ਸਮਝੋ, ਜਿਸ ਵਿੱਚ ਡੋਮੇਨ-ਵਿਸ਼ੇਸ਼ ਸਵੈ-ਚਾਲਤ, infrastructure dependence, ਅਤੇ guardrails ਦਾ ਆਦਰ ਸ਼ਾਮਲ ਹੈ।
- **ਵਰਤੋਂ ਦੇ ਪ੍ਰਯੋਗ ਅਤੇ ਮੁੱਲ:** ਉਹ ਸਥਿਤੀਆਂ ਪਛਾਣੋ ਜਿੱਥੇ Agentic RAG ਬਹੁਤ ਵਧੀਆ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ correctness-first environments, ਜਟਿਲ ਡਾਟਾਬੇਸ ਇੰਟਰੈਕਸ਼ਨ, ਅਤੇ ਲੰਬੇ workflows।
- **Governance, Transparency, ਅਤੇ Trust:** ਗਵਰਨੈਂਸ ਅਤੇ ਪਾਰਦਰਸ਼ਤਾ ਦੀ ਮਹੱਤਤਾ ਬਾਰੇ ਸਿੱਖੋ, ਜਿਸ ਵਿੱਚ explainable reasoning, bias control, ਅਤੇ ਮਨੁੱਖੀ ਨਿਗਰਾਨੀ ਸ਼ਾਮਲ ਹੈ।

## Agentic RAG ਕੀ ਹੈ?

Agentic Retrieval-Augmented Generation (Agentic RAG) ਇੱਕ ਨਵਾਂ AI ਪੈਰਾਡਾਇਮ ਹੈ ਜਿੱਥੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਬਾਹਰੀ ਸਰੋਤਾਂ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਦੇ ਹੋਏ ਆਪਣੇ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਯੋਜਨਾ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਂਦੇ ਹਨ। ਸਥਿਰ retrieval-then-read ਪੈਟਰਨਾਂ ਦੇ ਵਿਰੁੱਧ, Agentic RAG ਵਿੱਚ LLM ਨੂੰ ਵਾਰ-ਵਾਰ ਕਾਲ ਕਰਨਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਟੂਲ ਜਾਂ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ ਸੰਰਚਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ। ਸਿਸਟਮ ਨਤੀਜਿਆਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ, ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ, ਜਰੂਰਤ ਪੈਣ 'ਤੇ ਵਾਧੂ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਇਹ ਚੱਕਰ ਤਦ ਤੱਕ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਜਦ ਤੱਕ ਸੰਤੋਸ਼ਜਨਕ ਹੱਲ ਨਹੀਂ ਮਿਲ ਜਾਂਦਾ। 

ਇਹ iterative “maker-checker” ਸਟਾਈਲ ਸਹੀ ਨਤੀਜਿਆਂ ਨੂੰ ਸੁਧਾਰਨ, ਗਲਤ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਹੱਲ ਕਰਨ, ਅਤੇ ਉੱਚ-ਗੁਣਵੱਤਾ ਵਾਲੇ ਨਤੀਜੇ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਸਿਸਟਮ ਆਪਣੀ reasoning process ਨੂੰ ਮਾਲਕਾਨਾ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਦਾ ਹੈ, ਗਲਤ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਦੁਬਾਰਾ ਲਿਖਦਾ ਹੈ, ਵੱਖ-ਵੱਖ retrieval methods ਦੀ ਚੋਣ ਕਰਦਾ ਹੈ, ਅਤੇ ਕਈ ਟੂਲਾਂ ਨੂੰ ਇੰਟਿਗਰੇਟ ਕਰਦਾ ਹੈ—ਜਿਵੇਂ ਕਿ Azure AI Search ਵਿੱਚ vector search, SQL ਡਾਟਾਬੇਸ, ਜਾਂ custom APIs—ਅੰਤਮ ਜਵਾਬ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ। 

## Agentic Retrieval-Augmented Generation (Agentic RAG) ਦੀ ਪਰਿਭਾਸ਼ਾ

Agentic Retrieval-Augmented Generation (Agentic RAG) AI ਵਿਕਾਸ ਵਿੱਚ ਇੱਕ ਨਵਾਂ ਪੈਰਾਡਾਇਮ ਹੈ ਜਿੱਥੇ LLMs ਸਿਰਫ਼ ਬਾਹਰੀ ਡਾਟਾ ਸਰੋਤਾਂ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਦੇ ਹੀ ਨਹੀਂ, ਸਗੋਂ ਆਪਣੇ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਯੋਜਨਾ ਸਵੈ-ਚਾਲਤ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਂਦੇ ਹਨ। ਸਥਿਰ retrieval-then-read ਪੈਟਰਨਾਂ ਜਾਂ ਧਿਆਨ ਨਾਲ ਲਿਖੀਆਂ prompt sequences ਦੇ ਵਿਰੁੱਧ, Agentic RAG ਵਿੱਚ LLM ਨੂੰ ਵਾਰ-ਵਾਰ ਕਾਲ ਕਰਨਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਟੂਲ ਜਾਂ ਫੰਕਸ਼ਨ ਕਾਲ ਅਤੇ ਸੰਰਚਿਤ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ। 

## Reasoning Process ਦੀ ਮਾਲਕੀ

ਇੱਕ ਸਿਸਟਮ ਨੂੰ “agentic” ਬਣਾਉਣ ਵਾਲੀ ਵਿਸ਼ੇਸ਼ ਗੁਣਵੱਤਾ ਇਹ ਹੈ ਕਿ ਇਹ ਆਪਣੀ reasoning process ਨੂੰ ਮਾਲਕਾਨਾ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਦਾ ਹੈ। ਰਵਾਇਤੀ RAG implementations ਅਕਸਰ ਮਨੁੱਖਾਂ 'ਤੇ ਨਿਰਭਰ ਹੁੰਦੇ ਹਨ ਜੋ ਮਾਡਲ ਲਈ ਇੱਕ predefined path ਬਣਾਉਂਦੇ ਹਨ। 

## Iterative Loops, Tool Integration, ਅਤੇ Memory

Agentic ਸਿਸਟਮ ਇੱਕ ਲੂਪਡ ਇੰਟਰੈਕਸ਼ਨ ਪੈਟਰਨ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ:

- **Initial Call:** ਯੂਜ਼ਰ ਦਾ goal (ਯੂਜ਼ਰ ਪ੍ਰੰਪਟ) LLM ਨੂੰ ਪੇਸ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
- **Tool Invocation:** ਜੇ ਮਾਡਲ ਨੂੰ ਜਾਣਕਾਰੀ ਦੀ ਘਾਟ ਜਾਂ ਅਸਪਸ਼ਟ ਹਦਾਇਤਾਂ ਮਿਲਦੀਆਂ ਹਨ, ਤਾਂ ਇਹ ਇੱਕ ਟੂਲ ਜਾਂ retrieval method ਦੀ ਚੋਣ ਕਰਦਾ ਹੈ।
- **Assessment & Refinement:** ਵਾਪਸ ਆਈ ਜਾਣਕਾਰੀ ਦੀ ਸਮੀਖਿਆ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਮਾਡਲ ਫੈਸਲਾ ਕਰਦਾ ਹੈ ਕਿ ਕੀ ਜਾਣਕਾਰੀ ਕਾਫ਼ੀ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ ਇਹ ਪ੍ਰਸ਼ਨ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ, ਵੱਖ-ਵੱਖ ਟੂਲ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, ਜਾਂ ਆਪਣਾ ਰਵੱਈਆ ਬਦਲਦਾ ਹੈ।
- **Repeat Until Satisfied:** ਇਹ ਚੱਕਰ ਤਦ ਤੱਕ ਜਾਰੀ ਰਹਿੰਦਾ ਹੈ ਜਦ ਤੱਕ ਮਾਡਲ ਨੂੰ ਲਗਦਾ ਹੈ ਕਿ ਇਹ ਇੱਕ ਅੰਤਮ, ਸਹੀ ਜਵਾਬ ਦੇਣ ਲਈ ਕਾਫ਼ੀ ਸਪਸ਼ਟਤਾ ਅਤੇ ਸਬੂਤ ਪ੍ਰਾਪਤ ਕਰ ਚੁੱਕਾ ਹੈ।
- **Memory & State:** ਸਿਸਟਮ ਸਟੇਟ ਅਤੇ ਮੈਮਰੀ ਨੂੰ ਕਾਇਮ ਰੱਖਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਪਿਛਲੇ ਯਤਨਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਨਤੀਜਿਆਂ ਨੂੰ ਯਾਦ ਰੱਖ ਸਕਦਾ ਹੈ।

## Failure Modes ਅਤੇ Self-Correction ਨੂੰ ਹੱਲ ਕਰਨਾ

Agentic RAG ਦੀ ਸਵੈ-ਚਾਲਤਤਾ ਵਿੱਚ ਮਜ਼ਬੂਤ self-correction mechanisms ਸ਼ਾਮਲ ਹਨ। ਜਦੋਂ ਸਿਸਟਮ dead ends 'ਤੇ ਪਹੁੰਚਦਾ ਹੈ, ਤਾਂ ਇਹ:

- **Iterate and Re-Query:** ਨੀਵਾਂ ਮੁੱਲ ਵਾਲੇ ਜਵਾਬ ਦੇਣ ਦੀ ਬਜਾਏ, ਮਾਡਲ ਨਵੇਂ search strategies ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ।
- **Use Diagnostic Tools:** ਸਿਸਟਮ ਵਾਧੂ functions ਨੂੰ invoke ਕਰ ਸਕਦਾ ਹੈ।
- **Fallback on Human Oversight:** ਉੱਚ-ਦਾਅਵਾਂ ਵਾਲੇ ਜਾਂ ਬਾਰ-ਬਾਰ ਫੇਲ੍ਹ ਹੋਣ ਵਾਲੇ ਸਥਿਤੀਆਂ ਲਈ, ਮਾਡਲ uncertainty ਨੂੰ flag ਕਰਦਾ ਹੈ।

## Agency ਦੀਆਂ ਹੱਦਾਂ

Agentic RAG ਦੀਆਂ "agentic" ਸਮਰੱਥਾਵਾਂ ਮਨੁੱਖਾਂ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਟੂਲਾਂ, ਡਾਟਾ ਸਰੋਤਾਂ, ਅਤੇ ਨੀਤੀਆਂ ਤੱਕ ਸੀਮਿਤ ਹਨ। 

## ਵਰਤੋਂ ਦੇ ਪ੍ਰਯੋਗ ਅਤੇ ਮੁੱਲ

Agentic RAG ਉਹ ਸਥਿਤੀਆਂ ਵਿੱਚ ਚਮਕਦਾ ਹੈ ਜਿੱਥੇ iterative refinement ਅਤੇ precision ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ:

1. **Correctness-First Environments:** Compliance checks, regulatory analysis, ਜਾਂ legal research ਵਿੱਚ, agentic ਮਾਡਲ ਵਾਰ-ਵਾਰ ਤਥਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰ ਸਕਦਾ ਹੈ।
2. **Complex Database Interactions:** ਜਦੋਂ ਸੰਰਚਿਤ ਡਾਟਾ ਨਾਲ ਕੰਮ ਕਰਦੇ ਹੋ, ਸਿਸਟਮ ਆਪਣੇ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਸੁਧਾਰ ਸਕਦਾ ਹੈ।
3. **Extended Workflows:** ਲੰਬੇ-running sessions ਵਿੱਚ, Agentic RAG ਨਵੇਂ ਡਾਟਾ ਨੂੰ ਲਗਾਤਾਰ ਸ਼ਾਮਲ ਕਰ ਸਕਦਾ ਹੈ।

## Governance, Transparency, ਅਤੇ Trust

ਜਿਵੇਂ ਕਿ ਇਹ ਸਿਸਟਮ reasoning ਵਿੱਚ ਜ਼ਿਆਦਾ ਸਵੈ-ਚਾਲਤ ਬਣਦੇ ਹਨ, ਗਵਰਨੈਂਸ ਅਤੇ ਪਾਰਦਰਸ਼ਤਾ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹਨ:

- **Explainable Reasoning:** ਮਾਡਲ ਇੱਕ audit trail ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ।
- **Bias Control and Balanced Retrieval:** ਡਿਵੈਲਪਰ retrieval strategies ਨੂੰ ਟਿਊਨ ਕਰ ਸਕਦੇ ਹਨ।
- **Human Oversight and Compliance:** ਸੰਵੇਦਨਸ਼ੀਲ ਕੰਮਾਂ ਲਈ, ਮਨੁੱਖੀ ਸਮੀਖਿਆ ਅਹਿਮ ਰਹਿੰਦੀ ਹੈ।

## ਨਤੀਜਾ

Agentic RAG ਇੱਕ ਕੁਦਰਤੀ ਵਿਕਾਸ ਦਾ ਪ੍ਰਤੀਕ ਹੈ ਕਿ AI ਸਿਸਟਮ ਜਟਿਲ, ਡਾਟਾ-ਗਹਿਰਾਈ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਕਿਵੇਂ ਸੰਭਾਲਦੇ ਹਨ। 

### Agentic RAG ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ।

## ਵਾਧੂ ਸਰੋਤ

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Azure OpenAI Service ਨਾਲ Retrieval Augmented Generation (RAG) ਨੂੰ ਲਾਗੂ ਕਰੋ</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Azure AI Foundry ਨਾਲ Generative AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੁਲਾਂਕਣ</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG ਕੀ ਹੈ | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: ਏਜੰਟ-ਅਧਾਰਿਤ ਰੀਟਰੀਵਲ ਅੱਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ ਲਈ ਪੂਰੀ ਗਾਈਡ – ਜਨਰੇਸ਼ਨ RAG ਤੋਂ ਖ਼ਬਰਾਂ</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: ਆਪਣੇ RAG ਨੂੰ ਕੁਐਰੀ ਰੀਫਾਰਮੂਲੇਸ਼ਨ ਅਤੇ ਸੈਲਫ-ਕੁਐਰੀ ਨਾਲ ਤੇਜ਼ ਬਣਾਓ! Hugging Face ਖੁੱਲ੍ਹੇ-ਸਰੋਤ AI ਕੂਕਬੁੱਕ</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">RAG ਵਿੱਚ Agentic ਲੇਅਰਜ਼ ਸ਼ਾਮਲ ਕਰਨਾ</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">ਗਿਆਨ ਸਹਾਇਕਾਂ ਦਾ ਭਵਿੱਖ: ਜੈਰੀ ਲਿਊ</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Agentic RAG ਸਿਸਟਮ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">ਆਪਣੇ AI ਏਜੰਟਾਂ ਨੂੰ ਵਧਾਉਣ ਲਈ Azure AI Foundry Agent Service ਦੀ ਵਰਤੋਂ</a>

### ਅਕਾਦਮਿਕ ਪੇਪਰ

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: ਸੈਲਫ-ਫੀਡਬੈਕ ਨਾਲ ਦੁਹਰਾਉਂਦੇ ਸੁਧਾਰ</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: ਵਰਬਲ ਰੀਇਨਫੋਰਸਮੈਂਟ ਲਰਨਿੰਗ ਨਾਲ ਭਾਸ਼ਾ ਏਜੰਟ</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ ਟੂਲ-ਇੰਟਰਐਕਟਿਵ ਕ੍ਰਿਟੀਕਿੰਗ ਨਾਲ ਸਵੈ-ਸੁਧਾਰ ਕਰ ਸਕਦੇ ਹਨ</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Agentic RAG 'ਤੇ ਸਰਵੇਖਣ</a>

## ਪਿਛਲਾ ਪਾਠ

[ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](../04-tool-use/README.md)

## ਅਗਲਾ ਪਾਠ

[ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣਾ](../06-building-trustworthy-agents/README.md)

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।