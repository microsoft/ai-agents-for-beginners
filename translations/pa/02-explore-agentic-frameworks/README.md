<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:17:58+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pa"
}
-->
[![AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਖੋਜ](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.pa.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਵੇਖੋ)_

# AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਖੋਜ

AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਸੌਫਟਵੇਅਰ ਪਲੇਟਫਾਰਮ ਹਨ ਜੋ AI ਏਜੰਟਸ ਦੀ ਰਚਨਾ, ਤੈਨਾਤੀ ਅਤੇ ਪ੍ਰਬੰਧਨ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕੀਤੇ ਗਏ ਹਨ। ਇਹ ਫਰੇਮਵਰਕਸ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ ਗਏ ਕੰਪੋਨੈਂਟਸ, ਐਬਸਟਰੈਕਸ਼ਨ ਅਤੇ ਟੂਲਸ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜੋ ਜਟਿਲ AI ਸਿਸਟਮਾਂ ਦੇ ਵਿਕਾਸ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦੇ ਹਨ।

ਇਹ ਫਰੇਮਵਰਕਸ ਡਿਵੈਲਪਰਾਂ ਨੂੰ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਆਮ ਚੁਣੌਤੀਆਂ ਲਈ ਮਿਆਰੀ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਕੇ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਵਿਲੱਖਣ ਪੱਖਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਇਹ AI ਸਿਸਟਮਾਂ ਦੇ ਨਿਰਮਾਣ ਵਿੱਚ ਸਕੇਲਬਿਲਟੀ, ਪਹੁੰਚਯੋਗਤਾ ਅਤੇ ਕੁਸ਼ਲਤਾ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:

- AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਕੀ ਹਨ ਅਤੇ ਇਹ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਕੀ ਹਾਸਲ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ?
- ਟੀਮਾਂ ਕਿਵੇਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਏਜੰਟ ਦੀਆਂ ਸਮਰਥਾਵਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਦੁਹਰਾਉਣ ਅਤੇ ਸੁਧਾਰ ਸਕਦੀਆਂ ਹਨ?
- ਮਾਈਕਰੋਸਾਫਟ <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, ਅਤੇ <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ਦੁਆਰਾ ਬਣਾਏ ਗਏ ਫਰੇਮਵਰਕਸ ਅਤੇ ਟੂਲਸ ਵਿੱਚ ਕੀ ਅੰਤਰ ਹੈ?
- ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਇਕੋਸਿਸਟਮ ਟੂਲਸ ਨੂੰ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦਾ ਹਾਂ, ਜਾਂ ਮੈਨੂੰ ਸਟੈਂਡਅਲੋਨ ਹੱਲਾਂ ਦੀ ਲੋੜ ਹੈ?
- Azure AI Agents ਸੇਵਾ ਕੀ ਹੈ ਅਤੇ ਇਹ ਮੈਨੂੰ ਕਿਵੇਂ ਮਦਦ ਕਰ ਰਹੀ ਹੈ?

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਦੇ ਲਕਸ਼ ਹਨ:

- AI ਵਿਕਾਸ ਵਿੱਚ AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਸਮਝਣਾ।
- ਬੁੱਧੀਮਾਨ ਏਜੰਟਸ ਬਣਾਉਣ ਲਈ AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ।
- AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੁਆਰਾ ਯੋਗ ਕੀਤੀਆਂ ਮੁੱਖ ਸਮਰਥਾਵਾਂ।
- AutoGen, Semantic Kernel, ਅਤੇ Azure AI Agent Service ਦੇ ਅੰਤਰ।

## AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਕੀ ਹਨ ਅਤੇ ਇਹ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਕੀ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ?

ਪਾਰੰਪਰਿਕ AI ਫਰੇਮਵਰਕਸ ਤੁਹਾਨੂੰ ਆਪਣੇ ਐਪਸ ਵਿੱਚ AI ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਇਹ ਐਪਸ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕਿਆਂ ਵਿੱਚ ਬਿਹਤਰ ਬਣ ਸਕਦੇ ਹਨ:

- **ਪ੍ਰਸਨਲਾਈਜ਼ੇਸ਼ਨ**: AI ਯੂਜ਼ਰ ਦੇ ਵਿਹਾਰ ਅਤੇ ਪਸੰਦਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਵਿਅਕਤੀਗਤ ਸਿਫਾਰਸ਼ਾਂ, ਸਮੱਗਰੀ ਅਤੇ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕੀਤੇ ਜਾ ਸਕਣ।  
ਉਦਾਹਰਨ: Netflix ਵਰਗੇ ਸਟ੍ਰੀਮਿੰਗ ਸੇਵਾਵਾਂ AI ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਦੇਖਣ ਦੇ ਇਤਿਹਾਸ ਦੇ ਆਧਾਰ 'ਤੇ ਫਿਲਮਾਂ ਅਤੇ ਸ਼ੋਅਜ਼ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾ ਸਕੇ, ਜਿਸ ਨਾਲ ਯੂਜ਼ਰ ਦੀ ਸਹਿਭਾਗਤਾ ਅਤੇ ਸੰਤੁਸ਼ਟੀ ਵਧਦੀ ਹੈ।  
- **ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਕੁਸ਼ਲਤਾ**: AI ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰ ਸਕਦਾ ਹੈ, ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸਧਾਰਨ ਬਣਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਓਪਰੇਸ਼ਨਲ ਕੁਸ਼ਲਤਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰ ਸਕਦਾ ਹੈ।  
ਉਦਾਹਰਨ: ਗਾਹਕ ਸੇਵਾ ਐਪਸ AI-ਚਲਿਤ ਚੈਟਬੋਟਸ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਆਮ ਪੁੱਛਗਿੱਛਾਂ ਨੂੰ ਸੰਭਾਲਿਆ ਜਾ ਸਕੇ, ਜਵਾਬ ਦੇਣ ਦੇ ਸਮੇਂ ਨੂੰ ਘਟਾਇਆ ਜਾ ਸਕੇ ਅਤੇ ਜਟਿਲ ਮੁੱਦਿਆਂ ਲਈ ਮਨੁੱਖੀ ਏਜੰਟਾਂ ਨੂੰ ਖਾਲੀ ਕੀਤਾ ਜਾ ਸਕੇ।  
- **ਵਧੀਆ ਯੂਜ਼ਰ ਅਨੁਭਵ**: AI ਆਵਾਜ਼ ਪਛਾਣ, ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੋਸੈਸਿੰਗ, ਅਤੇ ਪੇਸ਼ਗੀ ਟੈਕਸਟ ਵਰਗੀਆਂ ਬੁੱਧੀਮਾਨ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਕੇ ਸਮੁੱਚੇ ਯੂਜ਼ਰ ਅਨੁਭਵ ਵਿੱਚ ਸੁਧਾਰ ਕਰ ਸਕਦਾ ਹੈ।  
ਉਦਾਹਰਨ: Siri ਅਤੇ Google Assistant ਵਰਗੇ ਵਰਚੁਅਲ ਸਹਾਇਕ AI ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਆਵਾਜ਼ ਦੇ ਹੁਕਮਾਂ ਨੂੰ ਸਮਝਿਆ ਜਾ ਸਕੇ ਅਤੇ ਜਵਾਬ ਦਿੱਤਾ ਜਾ ਸਕੇ, ਜਿਸ ਨਾਲ ਯੂਜ਼ਰਾਂ ਲਈ ਆਪਣੇ ਡਿਵਾਈਸਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨਾ ਆਸਾਨ ਬਣਦਾ ਹੈ।

### ਇਹ ਸਭ ਬਹੁਤ ਵਧੀਆ ਲੱਗਦਾ ਹੈ, ਤਾਂ ਫਿਰ ਸਾਨੂੰ AI ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਲੋੜ ਕਿਉਂ ਹੈ?

AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਸਿਰਫ AI ਫਰੇਮਵਰਕਸ ਤੋਂ ਵੱਧ ਕੁਝ ਦਰਸਾਉਂਦੇ ਹਨ। ਇਹ ਬੁੱਧੀਮਾਨ ਏਜੰਟਸ ਦੀ ਰਚਨਾ ਨੂੰ ਯੋਗ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕੀਤੇ ਗਏ ਹਨ ਜੋ ਯੂਜ਼ਰਾਂ, ਹੋਰ ਏਜੰਟਾਂ, ਅਤੇ ਵਾਤਾਵਰਣ ਨਾਲ ਸੰਚਾਰ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਵਿਸ਼ੇਸ਼ ਲਕਸ਼ਾਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ ਏਜੰਟਸ ਸਵੈ-ਚਾਲਤ ਵਿਹਾਰ ਦਰਸਾ ਸਕਦੇ ਹਨ, ਫੈਸਲੇ ਲੈ ਸਕਦੇ ਹਨ, ਅਤੇ ਬਦਲਦੇ ਹਾਲਾਤਾਂ ਅਨੁਸਾਰ ਅਨੁਕੂਲ ਹੋ ਸਕਦੇ ਹਨ। ਆਓ AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੁਆਰਾ ਯੋਗ ਕੀਤੀਆਂ ਕੁਝ ਮੁੱਖ ਸਮਰਥਾਵਾਂ 'ਤੇ ਨਜ਼ਰ ਮਾਰਦੇ ਹਾਂ:

- **ਏਜੰਟ ਸਹਿਯੋਗ ਅਤੇ ਸਮਨਵਯ**: ਕਈ AI ਏਜੰਟਸ ਦੀ ਰਚਨਾ ਨੂੰ ਯੋਗ ਬਣਾਉਣਾ ਜੋ ਇਕੱਠੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ, ਸੰਚਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਅਤੇ ਜਟਿਲ ਕੰਮਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਸਮਨਵਯ ਕਰ ਸਕਦੇ ਹਨ।  
- **ਕੰਮ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਪ੍ਰਬੰਧਨ**: ਬਹੁ-ਕਦਮ ਵਰਕਫਲੋਜ਼, ਕੰਮ ਸੌਂਪਣ, ਅਤੇ ਏਜੰਟਾਂ ਵਿੱਚ ਗਤੀਸ਼ੀਲ ਕੰਮ ਪ੍ਰਬੰਧਨ ਲਈ ਮਕੈਨਿਜ਼ਮ ਪ੍ਰਦਾਨ ਕਰਨਾ।  
- **ਸੰਦੇਸ਼ਕ ਅਨੁਕੂਲਤਾ ਅਤੇ ਅਨੁਕੂਲਨ**: ਏਜੰਟਾਂ ਨੂੰ ਸੰਦਰਭ ਨੂੰ ਸਮਝਣ, ਬਦਲਦੇ ਵਾਤਾਵਰਣਾਂ ਅਨੁਸਾਰ ਅਨੁਕੂਲ ਹੋਣ, ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਜਾਣਕਾਰੀ ਦੇ ਆਧਾਰ 'ਤੇ ਫੈਸਲੇ ਲੈਣ ਦੀ ਸਮਰਥਾ ਨਾਲ ਸਜਾਉਣਾ।

ਸਾਰ ਵਿੱਚ, ਏਜੰਟ ਤੁਹਾਨੂੰ ਹੋਰ ਕੁਝ ਕਰਨ ਦੀ ਯੋਗਤਾ ਦਿੰਦੇ ਹਨ, ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਅਗਲੇ ਪੱਧਰ 'ਤੇ ਲੈ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਹੋਰ ਬੁੱਧੀਮਾਨ ਸਿਸਟਮ ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਆਪਣੇ ਵਾਤਾਵਰਣ ਤੋਂ ਸਿੱਖ ਸਕਦੇ ਹਨ ਅਤੇ ਅਨੁਕੂਲ ਹੋ ਸਕਦੇ ਹਨ।

## ਏਜੰਟ ਦੀਆਂ ਸਮਰਥਾਵਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਦੁਹਰਾਉਣ ਅਤੇ ਸੁਧਾਰ ਕਰਨ ਦਾ ਤਰੀਕਾ?

ਇਹ ਇੱਕ ਤੇਜ਼ੀ ਨਾਲ ਬਦਲਦਾ ਖੇਤਰ ਹੈ, ਪਰ ਜ਼ਿਆਦਾਤਰ AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਵਿੱਚ ਕੁਝ ਆਮ ਚੀਜ਼ਾਂ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਅਤੇ ਦੁਹਰਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਮੋਡਿਊਲ ਕੰਪੋਨੈਂਟਸ, ਸਹਿਯੋਗੀ ਟੂਲਸ, ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਸਿੱਖਣਾ। ਆਓ ਇਹਨਾਂ ਵਿੱਚ ਡੁੱਬੀਏ:

- **ਮੋਡਿਊਲ ਕੰਪੋਨੈਂਟਸ ਦੀ ਵਰਤੋਂ ਕਰੋ**: AI SDKs ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ ਕੰਪੋਨੈਂਟਸ ਜਿਵੇਂ ਕਿ AI ਅਤੇ ਮੈਮਰੀ ਕਨੈਕਟਰਸ, ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਜਾਂ ਕੋਡ ਪਲੱਗਇਨ ਵਰਤੋਂ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ, ਪ੍ਰੋਮਪਟ ਟੈਂਪਲੇਟਸ, ਅਤੇ ਹੋਰ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।  
- **ਸਹਿਯੋਗੀ ਟੂਲਸ ਦੀ ਵਰਤੋਂ ਕਰੋ**: ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਕੰਮਾਂ ਨਾਲ ਏਜੰਟਸ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰੋ, ਜਿਸ ਨਾਲ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਦੀ ਜਾਂਚ ਅਤੇ ਸੁਧਾਰ ਯੋਗ ਬਣਦਾ ਹੈ।  
- **ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਿੱਖੋ**: ਫੀਡਬੈਕ ਲੂਪਸ ਲਾਗੂ ਕਰੋ ਜਿੱਥੇ ਏਜੰਟ ਸੰਚਾਰਾਂ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣੇ ਵਿਹਾਰ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਅਨੁਕੂਲ ਕਰਦੇ ਹਨ।  

### ਮੋਡਿਊਲ ਕੰਪੋਨੈਂਟਸ ਦੀ ਵਰਤੋਂ ਕਰੋ

Microsoft Semantic Kernel ਅਤੇ LangChain ਵਰਗੇ SDKs ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ ਕੰਪੋਨੈਂਟਸ ਜਿਵੇਂ ਕਿ AI ਕਨੈਕਟਰਸ, ਪ੍ਰੋਮਪਟ ਟੈਂਪਲੇਟਸ, ਅਤੇ ਮੈਮਰੀ ਪ੍ਰਬੰਧਨ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਇਹ ਕੰਪੋਨੈਂਟਸ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਇਕੱਠਾ ਕਰਕੇ ਇੱਕ ਕਾਰਗਰ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ ਲਈ ਸ਼ੁਰੂ ਤੋਂ ਸ਼ੁਰੂ ਕੀਤੇ ਬਿਨਾਂ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰਯੋਗ ਅਤੇ ਦੁਹਰਾਉਣ ਕਰ ਸਕਦੀਆਂ ਹਨ।  

**ਇਹ ਅਮਲ ਵਿੱਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਇੱਕ ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਜਾਣਕਾਰੀ ਕੱਢ ਸਕਦੇ ਹੋ, ਇੱਕ ਮੈਮਰੀ ਮੋਡਿਊਲ ਨੂੰ ਡਾਟਾ ਸਟੋਰ ਅਤੇ ਰੀਟਰੀਵ ਕਰਨ ਲਈ, ਅਤੇ ਇੱਕ ਪ੍ਰੋਮਪਟ ਜਨਰੇਟਰ ਨੂੰ ਯੂਜ਼ਰਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ, ਇਹ ਸਭ ਸ਼ੁਰੂ ਤੋਂ ਬਣਾਉਣ ਦੀ ਲੋੜ ਬਿਨਾਂ।  

**ਉਦਾਹਰਨ ਕੋਡ**. ਆਓ ਦੇਖੀਏ ਕਿ Semantic Kernel Python ਅਤੇ .Net ਨਾਲ ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ AI ਕਨੈਕਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਯੂਜ਼ਰ ਇਨਪੁਟ ਦਾ ਜਵਾਬ ਦੇਣ ਲਈ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```
  
ਇਸ ਉਦਾਹਰਨ ਤੋਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਮੁੱਖ ਜਾਣਕਾਰੀ ਕੱਢਣ ਲਈ ਪੂਰਵ-ਤਿਆਰ ਕੀਤੇ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਫਲਾਈਟ ਬੁਕਿੰਗ ਬੇਨਤੀ ਦੇ ਮੂਲ, ਮੰਜ਼ਿਲ, ਅਤੇ ਮਿਤੀ। ਇਹ ਮੋਡਿਊਲ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਉੱਚ-ਪੱਧਰ ਦੇ ਤਰਕ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਨ ਦੀ ਯੋਗਤਾ ਦਿੰਦੀ ਹੈ।  

### ਸਹਿਯੋਗੀ ਟੂਲਸ ਦੀ ਵਰਤੋਂ ਕਰੋ

CrewAI, Microsoft AutoGen, ਅਤੇ Semantic Kernel ਵਰਗੇ ਫਰੇਮਵਰਕਸ ਕਈ ਏਜੰਟਸ ਦੀ ਰਚਨਾ ਨੂੰ ਸਹੂਲਤ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜੋ ਇਕੱਠੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਕੰਮਾਂ ਨਾਲ ਏਜੰਟਸ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਦੀ ਜਾਂਚ ਅਤੇ ਸੁਧਾਰ ਯੋਗ ਬਣਦਾ ਹੈ ਅਤੇ ਸਮੁੱਚੇ ਸਿਸਟਮ ਦੀ ਕੁਸ਼ਲਤਾ ਵਿੱਚ ਸੁਧਾਰ ਹੁੰਦਾ ਹੈ।  

**ਇਹ ਅਮਲ ਵਿੱਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਏਜੰਟਸ ਦੀ ਇੱਕ ਟੀਮ ਬਣਾਉਣ ਲਈ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਾਲੀ ਭੂਮਿਕਾ ਦੇ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਡਾਟਾ ਰੀਟਰੀਵਲ, ਵਿਸ਼ਲੇਸ਼ਣ, ਜਾਂ ਫੈਸਲੇ ਲੈਣਾ। ਇਹ ਏਜੰਟਸ ਸੰਚਾਰ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਜਾਣਕਾਰੀ ਸਾਂਝੀ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਇੱਕ ਸਾਂਝੇ ਲਕਸ਼ ਨੂੰ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ, ਜਿਵੇਂ ਕਿ ਯੂਜ਼ਰ ਪੁੱਛਗਿੱਛ ਦਾ ਜਵਾਬ ਦੇਣਾ ਜਾਂ ਇੱਕ ਕੰਮ ਪੂਰਾ ਕਰਨਾ।  

**ਉਦਾਹਰਨ ਕੋਡ (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```
  
ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਤੁਸੀਂ ਦੇਖਦੇ ਹੋ ਕਿ ਕਿਵੇਂ ਤੁਸੀਂ ਇੱਕ ਕੰਮ ਬਣਾਉਂਦੇ ਹੋ ਜਿਸ ਵਿੱਚ ਕਈ ਏਜੰਟਸ ਡਾਟਾ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ ਹਨ। ਹਰ ਏਜੰਟ ਇੱਕ ਵਿਸ਼ੇਸ਼ ਫੰਕਸ਼ਨ ਕਰਦਾ ਹੈ, ਅਤੇ ਕੰਮ ਨੂੰ ਚਾਹੇ ਗਏ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਏਜੰਟਸ ਨੂੰ ਸਮਨਵਯ ਕਰਕੇ ਅੰਜਾਮ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਾਲੀਆਂ ਭੂਮਿਕਾਵਾਂ ਨਾਲ ਸਮਰਪਿਤ ਏਜੰਟਸ ਬਣਾਉਣ ਦੁਆਰਾ, ਤੁਸੀਂ ਕੰਮ ਦੀ ਕੁਸ਼ਲਤਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸੁਧਾਰ ਕਰ ਸਕਦੇ ਹੋ।  

### ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਿੱਖੋ

ਅਗਰਸਰ ਫਰੇਮਵਰਕਸ ਰੀਅਲ-ਟਾਈਮ ਸੰਦਰਭ ਸਮਝਣ ਅਤੇ ਅਨੁਕੂਲਨ ਲਈ ਸਮਰਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਫੀਡਬੈਕ ਲੂਪਸ ਲਾਗੂ ਕਰ ਸਕਦੀਆਂ ਹਨ ਜਿੱਥੇ ਏਜੰਟ ਸੰਚਾਰਾਂ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣੇ ਵਿਹਾਰ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਅਨੁਕੂਲ ਕਰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਸਮਰਥਾਵਾਂ ਵਿੱਚ ਲਗਾਤਾਰ ਸੁਧਾਰ ਅਤੇ ਸੁਧਾਰ ਹੁੰਦਾ ਹੈ।  

**ਇਹ ਅਮਲ ਵਿੱਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਏਜੰਟਸ ਯੂਜ਼ਰ ਫੀਡਬੈਕ, ਵਾਤਾਵਰਣ ਡਾਟਾ, ਅਤੇ ਕੰਮ ਦੇ ਨਤੀਜਿਆਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਆਪਣੀ ਜਾਣਕਾਰੀ ਦਾ ਅਧਾਰ ਅਪਡੇਟ ਕਰ ਸਕਣ, ਫੈਸਲੇ ਲੈਣ ਦੇ ਅਲਗੋਰਿਥਮਸ ਨੂੰ ਅਨੁਕੂਲ ਕਰ ਸਕਣ, ਅਤੇ ਸਮੇਂ ਦੇ ਨਾਲ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸੁਧਾਰ ਕਰ ਸਕਣ। ਇਹ ਦੁਹਰਾਉਣ ਵਾਲਾ ਸਿੱਖਣ ਪ੍ਰਕਿਰਿਆ ਏਜੰਟਸ ਨੂੰ ਬਦਲਦੇ ਹਾਲਾਤਾਂ ਅਤੇ ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਅਨੁਸਾਰ ਅਨੁਕੂਲ ਹੋਣ ਦੀ ਯੋਗਤਾ ਦਿੰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਸਮੁੱਚੇ ਸਿਸਟਮ ਦੀ ਕੁਸ਼ਲਤਾ ਵਿੱਚ ਸੁਧਾਰ ਹੁੰਦਾ ਹੈ।  

## AutoGen, Semantic Kernel ਅਤੇ Azure AI Agent Service ਦੇ ਫਰੇਮਵਰਕਸ ਵਿੱਚ ਕੀ ਅੰਤਰ ਹੈ?

ਇਹਨਾਂ ਫਰੇਮਵਰਕਸ ਦੀ ਤੁਲਨਾ ਕਰਨ ਦੇ ਕਈ ਤਰੀਕੇ ਹਨ, ਪਰ ਆਓ ਇਹਨਾਂ ਦੇ ਡਿਜ਼ਾਈਨ, ਸਮਰਥਾਵਾਂ, ਅਤੇ ਟਾਰਗਟ ਯੂਜ਼ ਕੇਸਾਂ ਦੇ ਹਿਸਾਬ ਨਾਲ ਕੁਝ ਮੁੱਖ ਅੰਤਰਾਂ 'ਤੇ ਨਜ਼ਰ ਮਾਰਦੇ ਹਾਂ:

## AutoGen

AutoGen ਮਾਈਕਰੋਸਾਫਟ ਰਿਸਰਚ ਦੇ AI Frontiers Lab ਦੁਆਰਾ ਵਿਕਸਿਤ ਇੱਕ ਖੁੱਲ੍ਹੇ-ਸਰੋਤ ਫਰੇਮਵਰਕ ਹੈ। ਇਹ ਇਵੈਂਟ-ਚਲਿਤ, ਵੰਡੇ ਹੋਏ *agentic* ਐਪਲੀ
ਇਹ ਤੱਥਾਂ ਫਿਰ ਮੈਮਰੀ ਕਲੈਕਸ਼ਨ `SummarizedAzureDocs` ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਇੱਕ ਬਹੁਤ ਹੀ ਸਧਾਰਨ ਉਦਾਹਰਨ ਹੈ, ਪਰ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਕਿਵੇਂ LLM ਲਈ ਜਾਣਕਾਰੀ ਮੈਮਰੀ ਵਿੱਚ ਸਟੋਰ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

ਤਾਂ ਇਹ ਸੀਮੈਂਟਿਕ ਕਰਨਲ ਫਰੇਮਵਰਕ ਦੇ ਬੁਨਿਆਦੀ ਅਸੂਲ ਹਨ, ਪਰ ਏਜੰਟ ਫਰੇਮਵਰਕ ਬਾਰੇ ਕੀ?

## Azure AI Agent Service

Azure AI Agent Service ਇੱਕ ਹਾਲ ਹੀ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀ ਗਈ ਸੇਵਾ ਹੈ, ਜੋ ਮਾਈਕਰੋਸਾਫਟ Ignite 2024 ਵਿੱਚ ਪੇਸ਼ ਕੀਤੀ ਗਈ। ਇਹ AI ਏਜੰਟਾਂ ਨੂੰ ਵਿਕਸਿਤ ਅਤੇ ਤੈਨਾਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ Llama 3, Mistral, ਅਤੇ Cohere ਵਰਗੇ ਖੁੱਲ੍ਹੇ-ਸਰੋਤ LLMs ਨੂੰ ਸਿੱਧੇ ਕਾਲ ਕਰਨਾ।

Azure AI Agent Service ਮਜ਼ਬੂਤ ਕਾਰੋਬਾਰੀ ਸੁਰੱਖਿਆ ਮਕੈਨਿਜ਼ਮ ਅਤੇ ਡਾਟਾ ਸਟੋਰੇਜ ਤਰੀਕੇ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਕਾਰੋਬਾਰੀ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਚਿਤ ਬਣਦੀ ਹੈ।

ਇਹ AutoGen ਅਤੇ Semantic Kernel ਵਰਗੇ ਬਹੁ-ਏਜੰਟ ਆਰਕੇਸਟ੍ਰੇਸ਼ਨ ਫਰੇਮਵਰਕਸ ਨਾਲ ਸਿੱਧੇ ਕੰਮ ਕਰਦੀ ਹੈ।

ਇਹ ਸੇਵਾ ਇਸ ਸਮੇਂ ਪਬਲਿਕ ਪ੍ਰੀਵਿਊ ਵਿੱਚ ਹੈ ਅਤੇ ਏਜੰਟ ਬਣਾਉਣ ਲਈ Python ਅਤੇ C# ਨੂੰ ਸਹਾਇਕ ਬਣਾਉਂਦੀ ਹੈ।

Semantic Kernel Python ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਅਸੀਂ ਇੱਕ ਯੂਜ਼ਰ-ਡਿਫਾਈਨਡ ਪਲੱਗਇਨ ਨਾਲ Azure AI Agent ਬਣਾਉਣ ਦੇ ਯੋਗ ਹਾਂ:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### ਮੁੱਖ ਧਾਰਨਾਵਾਂ

Azure AI Agent Service ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਹਨ:

- **Agent**. Azure AI Agent Service, Azure AI Foundry ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਦੀ ਹੈ। AI Foundry ਵਿੱਚ, ਇੱਕ AI Agent "ਸਮਰੱਥ" ਮਾਈਕ੍ਰੋਸਰਵਿਸ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜੋ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇਣ (RAG), ਕਾਰਵਾਈ ਕਰਨ ਜਾਂ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਆਟੋਮੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਦੀ ਤਾਕਤ ਨੂੰ ਹਕੀਕਤੀ ਡਾਟਾ ਸਰੋਤਾਂ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਯੋਗਤਾ ਨਾਲ ਜੋੜ ਕੇ ਇਹ ਹਾਸਲ ਕਰਦਾ ਹੈ। ਇੱਥੇ ਇੱਕ ਏਜੰਟ ਦਾ ਉਦਾਹਰਨ ਹੈ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, `gpt-4o-mini` ਮਾਡਲ, `my-agent` ਨਾਮ, ਅਤੇ `You are helpful agent` ਹਦਾਇਤਾਂ ਨਾਲ ਇੱਕ ਏਜੰਟ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਹ ਏਜੰਟ ਕੋਡ ਇੰਟਰਪ੍ਰਿਟੇਸ਼ਨ ਟਾਸਕਸ ਕਰਨ ਲਈ ਸਾਧਨਾਂ ਅਤੇ ਸਰੋਤਾਂ ਨਾਲ ਲੈਸ ਹੈ।

- **Thread ਅਤੇ Messages**. Thread ਇੱਕ ਹੋਰ ਮਹੱਤਵਪੂਰਨ ਧਾਰਨਾ ਹੈ। ਇਹ ਇੱਕ ਏਜੰਟ ਅਤੇ ਯੂਜ਼ਰ ਦੇ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਜਾਂ ਇੰਟਰੈਕਸ਼ਨ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ। Threads ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ, ਸੰਦਰਭ ਜਾਣਕਾਰੀ ਸਟੋਰ ਕਰਨ, ਅਤੇ ਇੰਟਰੈਕਸ਼ਨ ਦੀ ਸਥਿਤੀ ਨੂੰ ਮੈਨੇਜ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇੱਥੇ ਇੱਕ Thread ਦਾ ਉਦਾਹਰਨ ਹੈ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ, ਇੱਕ Thread ਬਣਾਈ ਗਈ ਹੈ। ਇਸ ਤੋਂ ਬਾਅਦ, Thread ਨੂੰ ਇੱਕ ਸੁਨੇਹਾ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ। `create_and_process_run` ਨੂੰ ਕਾਲ ਕਰਕੇ, ਏਜੰਟ ਨੂੰ Thread 'ਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕਿਹਾ ਜਾਂਦਾ ਹੈ। ਆਖਿਰਕਾਰ, ਸੁਨੇਹੇ ਫੈਚ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਏਜੰਟ ਦੇ ਜਵਾਬ ਨੂੰ ਦੇਖਣ ਲਈ ਲੌਗ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਸੁਨੇਹੇ ਯੂਜ਼ਰ ਅਤੇ ਏਜੰਟ ਦੇ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਇਹ ਵੀ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਸੁਨੇਹੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ ਟੈਕਸਟ, ਚਿੱਤਰ, ਜਾਂ ਫਾਈਲ, ਜੋ ਕਿ ਏਜੰਟ ਦੇ ਕੰਮ ਦਾ ਨਤੀਜਾ ਹੈ। ਇੱਕ ਡਿਵੈਲਪਰ ਵਜੋਂ, ਤੁਸੀਂ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਅੱਗੇ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਜਾਂ ਯੂਜ਼ਰ ਨੂੰ ਪੇਸ਼ ਕਰਨ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ।

- **ਹੋਰ AI ਫਰੇਮਵਰਕਸ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਦਾ ਹੈ**. Azure AI Agent Service AutoGen ਅਤੇ Semantic Kernel ਵਰਗੇ ਹੋਰ ਫਰੇਮਵਰਕਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਸਕਦਾ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਐਪ ਦਾ ਕੁਝ ਹਿੱਸਾ ਇਨ੍ਹਾਂ ਫਰੇਮਵਰਕਸ ਵਿੱਚ ਬਣਾਉਣ ਅਤੇ ਉਦਾਹਰਨ ਵਜੋਂ Agent Service ਨੂੰ ਇੱਕ ਆਰਕੇਸਟ੍ਰੇਟਰ ਵਜੋਂ ਵਰਤ ਸਕਦੇ ਹੋ ਜਾਂ ਤੁਸੀਂ ਸਾਰਾ ਕੁਝ Agent Service ਵਿੱਚ ਬਣਾਉਣ ਲਈ ਚੁਣ ਸਕਦੇ ਹੋ।

**ਵਰਤੋਂ ਦੇ ਕੇਸ**: Azure AI Agent Service ਨੂੰ ਕਾਰੋਬਾਰੀ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ ਜੋ ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ, ਅਤੇ ਲਚਕਦਾਰ AI ਏਜੰਟ ਤੈਨਾਤ ਕਰਨ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

## ਇਨ੍ਹਾਂ ਫਰੇਮਵਰਕਸ ਵਿੱਚ ਕੀ ਅੰਤਰ ਹੈ?

ਇਹ ਲਗਦਾ ਹੈ ਕਿ ਇਨ੍ਹਾਂ ਫਰੇਮਵਰਕਸ ਵਿੱਚ ਕਾਫ਼ੀ ਓਵਰਲੈਪ ਹੈ, ਪਰ ਉਨ੍ਹਾਂ ਦੇ ਡਿਜ਼ਾਈਨ, ਸਮਰੱਥਾਵਾਂ, ਅਤੇ ਟਾਰਗਟ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦੇ ਹਿਸਾਬ ਨਾਲ ਕੁਝ ਮੁੱਖ ਅੰਤਰ ਹਨ:

- **AutoGen**: ਇਹ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮਾਂ 'ਤੇ ਅਗੇਤਨ ਗਹਿਰੇ ਖੋਜ ਲਈ ਇੱਕ ਪ੍ਰਯੋਗਾਤਮਕ ਫਰੇਮਵਰਕ ਹੈ। ਇਹ ਜਟਿਲ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮਾਂ ਨੂੰ ਪ੍ਰੋਟੋਟਾਈਪ ਕਰਨ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਥਾਂ ਹੈ।
- **Semantic Kernel**: ਇਹ ਕਾਰੋਬਾਰੀ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ ਲਈ ਇੱਕ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਏਜੰਟ ਲਾਇਬ੍ਰੇਰੀ ਹੈ। ਇਹ ਘਟਨਾ-ਚਲਿਤ, ਵੰਡੇ ਹੋਏ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਾ ਹੈ, ਕਈ LLMs ਅਤੇ SLMs, ਸਾਧਨਾਂ, ਅਤੇ ਸਿੰਗਲ/ਮਲਟੀ-ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਸ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।
- **Azure AI Agent Service**: ਇਹ Azure Foundry ਵਿੱਚ ਏਜੰਟਾਂ ਲਈ ਇੱਕ ਪਲੇਟਫਾਰਮ ਅਤੇ ਤੈਨਾਤ ਸੇਵਾ ਹੈ। ਇਹ Azure Found ਦੁਆਰਾ ਸਹਾਇਕ ਸੇਵਾਵਾਂ ਨਾਲ ਕਨੈਕਟਿਵਿਟੀ ਬਣਾਉਣ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ Azure OpenAI, Azure AI Search, Bing Search ਅਤੇ ਕੋਡ ਐਗਜ਼ਿਕਿਊਸ਼ਨ।

ਅਜੇ ਵੀ ਪਤਾ ਨਹੀਂ ਕਿ ਕਿਹੜਾ ਚੁਣਨਾ ਹੈ?

### ਵਰਤੋਂ ਦੇ ਕੇਸ

ਆਓ ਕੁਝ ਆਮ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦੇ ਜ਼ਰੀਏ ਤੁਹਾਡੀ ਮਦਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ:

> ਪ੍ਰ: ਮੈਂ ਪ੍ਰਯੋਗ ਕਰ ਰਿਹਾ ਹਾਂ, ਸਿੱਖ ਰਿਹਾ ਹਾਂ ਅਤੇ ਪ੍ਰੂਫ-ਆਫ-ਕੰਸੈਪਟ ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਿਹਾ ਹਾਂ, ਅਤੇ ਮੈਂ ਤੇਜ਼ੀ ਨਾਲ ਬਣਾਉਣ ਅਤੇ ਪ੍ਰਯੋਗ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣਾ ਚਾਹੁੰਦਾ ਹਾਂ।

> ਉ: AutoGen ਇਸ ਸਥਿਤੀ ਲਈ ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੋਵੇਗੀ, ਕਿਉਂਕਿ ਇਹ ਘਟਨਾ-ਚਲਿਤ, ਵੰਡੇ ਹੋਏ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਾ ਹੈ ਅਤੇ ਉੱਚ-ਅਧਿਕਤਮ ਬਹੁ-ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਸ ਨੂੰ ਸਹਾਇਕ ਬਣਾਉਂਦਾ ਹੈ।

> ਪ੍ਰ: ਇਸ ਵਰਤੋਂ ਦੇ ਕੇਸ ਲਈ AutoGen ਨੂੰ Semantic Kernel ਅਤੇ Azure AI Agent Service ਨਾਲੋਂ ਵਧੀਆ ਚੋਣ ਕਿਉਂ ਬਣਾਉਂਦਾ ਹੈ?

> ਉ: AutoGen ਖਾਸ ਤੌਰ 'ਤੇ ਘਟਨਾ-ਚਲਿਤ, ਵੰਡੇ ਹੋਏ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਕੋਡ ਜਨਰੇਸ਼ਨ ਅਤੇ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਾਰਜਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨ ਲਈ ਬਹੁਤ ਹੀ ਉਚਿਤ ਬਣਦਾ ਹੈ। ਇਹ ਜਟਿਲ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮਾਂ ਨੂੰ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਬਣਾਉਣ ਲਈ ਜ਼ਰੂਰੀ ਸਾਧਨ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

> ਪ੍ਰ: ਲਗਦਾ ਹੈ ਕਿ Azure AI Agent Service ਇੱਥੇ ਵੀ ਕੰਮ ਕਰ ਸਕਦਾ ਹੈ, ਇਸ ਵਿੱਚ ਕੋਡ ਜਨਰੇਸ਼ਨ ਅਤੇ ਹੋਰ ਲਈ ਸਾਧਨ ਹਨ?

> ਉ: ਹਾਂ, Azure AI Agent Service ਏਜੰਟਾਂ ਲਈ ਇੱਕ ਪਲੇਟਫਾਰਮ ਸੇਵਾ ਹੈ ਅਤੇ ਕਈ ਮਾਡਲਾਂ, Azure AI Search, Bing Search ਅਤੇ Azure Functions ਲਈ ਬਣਾਈ ਗਈ ਸਮਰੱਥਾਵਾਂ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਇਹ Foundry Portal ਵਿੱਚ ਤੁਹਾਡੇ ਏਜੰਟਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਬਣਾਉਣ ਅਤੇ ਵੱਡੇ ਪੱਧਰ 'ਤੇ ਤੈਨਾਤ ਕਰਨ ਲਈ ਸਹਾਇਕ ਬਣਾਉਂਦਾ ਹੈ।

> ਪ੍ਰ: ਮੈਂ ਅਜੇ ਵੀ ਗੁੰਝਲ ਵਿੱਚ ਹਾਂ, ਮੈਨੂੰ ਸਿਰਫ ਇੱਕ ਵਿਕਲਪ ਦਿਓ।

> ਉ: ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੈ ਕਿ ਪਹਿਲਾਂ Semantic Kernel ਵਿੱਚ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓ ਅਤੇ ਫਿਰ ਆਪਣੇ ਏਜੰਟ ਨੂੰ ਤੈਨਾਤ ਕਰਨ ਲਈ Azure AI Agent Service ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇਹ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਆਪਣੇ ਏਜੰਟਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸਟੋਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਜਦੋਂ ਕਿ Semantic Kernel ਵਿੱਚ ਬਹੁ-ਏਜੰਟ ਸਿਸਟਮਾਂ ਬਣਾਉਣ ਦੀ ਤਾਕਤ ਦਾ ਲਾਭ ਲਿਆ ਜਾਂਦਾ ਹੈ। ਇਸ ਤੋਂ ਇਲਾਵਾ, Semantic Kernel ਵਿੱਚ AutoGen ਵਿੱਚ ਇੱਕ ਕਨੈਕਟਰ ਹੈ, ਜਿਸ ਨਾਲ ਦੋਨੋ ਫਰੇਮਵਰਕਸ ਨੂੰ ਇਕੱਠੇ ਵਰਤਣਾ ਆਸਾਨ ਬਣ ਜਾਂਦਾ ਹੈ।

ਆਓ ਇੱਕ ਟੇਬਲ ਵਿੱਚ ਮੁੱਖ ਅੰਤਰਾਂ ਨੂੰ ਸੰਖੇਪ ਕਰੀਏ:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | ਘਟਨਾ-ਚਲਿਤ, ਵੰਡੇ ਹੋਏ ਏਜੰਟਿਕ ਐਪਲੀਕੇਸ਼ਨ | Agents, Personas, Functions, Data | ਕੋਡ ਜਨਰੇਸ਼ਨ, ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਾਰਜ |
| Semantic Kernel | ਮਨੁੱਖੀ-ਜਿਵੇਂ ਟੈਕਸਟ ਸਮਝਣ ਅਤੇ ਜਨਰੇਟ ਕਰਨ 'ਤੇ ਧਿਆਨ | Agents, Modular Components, Collaboration | ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਸਮਝਣਾ, ਸਮੱਗਰੀ ਜਨਰੇਸ਼ਨ |
| Azure AI Agent Service | ਲਚਕਦਾਰ ਮਾਡਲ, ਕਾਰੋਬਾਰੀ ਸੁਰੱਖਿਆ, ਕੋਡ ਜਨਰੇਸ਼ਨ, ਸਾਧਨ ਕਾਲਿੰਗ | Modularity, Collaboration, Process Orchestration | ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ, ਅਤੇ ਲਚਕਦਾਰ AI ਏਜੰਟ ਤੈਨਾਤ |

ਇਨ੍ਹਾਂ ਫਰੇਮਵਰਕਸ ਲਈ ਆਦਰਸ਼ ਵਰਤੋਂ ਦੇ ਕੇਸ ਕੀ ਹਨ?

## ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ecosystem ਸਾਧਨਾਂ ਨੂੰ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦਾ ਹਾਂ, ਜਾਂ ਮੈਨੂੰ ਸਵਤੰਤਰ ਸੋਲੂਸ਼ਨ ਦੀ ਲੋੜ ਹੈ?

ਜਵਾਬ ਹੈ ਹਾਂ, ਤੁਸੀਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ecosystem ਸਾਧਨਾਂ ਨੂੰ ਸਿੱਧੇ Azure AI Agent Service ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਖਾਸ ਕਰਕੇ ਕਿਉਂਕਿ ਇਹ ਹੋਰ Azure ਸੇਵਾਵਾਂ ਨਾਲ ਬੇਹਤਰੀਨ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਤੁਸੀਂ ਉਦਾਹਰਨ ਵਜੋਂ Bing, Azure AI Search, ਅਤੇ Azure Functions ਨੂੰ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹੋ। ਇਸ ਵਿੱਚ Azure AI Foundry ਨਾਲ ਡੂੰਘੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵੀ ਹੈ।

AutoGen ਅਤੇ Semantic Kernel ਲਈ, ਤੁਸੀਂ Azure ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਪਰ ਇਹ ਤੁਹਾਨੂੰ ਆਪਣੇ ਕੋਡ ਤੋਂ Azure ਸੇਵਾਵਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ। ਇੱਕ ਹੋਰ ਤਰੀਕਾ Azure SDKs ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਏਜੰਟਾਂ ਤੋਂ Azure ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨਾ ਹੈ। ਇਸ ਤੋਂ ਇਲਾਵਾ, ਜਿਵੇਂ ਕਿ ਦੱਸਿਆ ਗਿਆ ਸੀ, ਤੁਸੀਂ AutoGen ਜਾਂ Semantic Kernel ਵਿੱਚ ਬਣਾਏ ਆਪਣੇ ਏਜੰਟਾਂ ਲਈ Azure AI Agent Service ਨੂੰ ਇੱਕ ਆਰਕੇਸਟ੍ਰੇਟਰ ਵਜੋਂ ਵਰਤ ਸਕਦੇ ਹੋ, ਜਿਸ ਨਾਲ Azure ecosystem ਤੱਕ ਆਸਾਨ ਪਹੁੰਚ ਮਿਲਦੀ ਹੈ।

### AI Agent Frameworks ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ, ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲੋ, ਦਫ਼ਤਰ ਦੇ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਿਰਕਤ ਕਰੋ ਅਤੇ ਆਪਣੇ AI Agents ਸਬੰਧੀ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰੋ।

## ਸੰਦਰਭ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel ਅਤੇ AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">AutoGen / Semantic Kernel ਨਾਲ Azure AI Agent Service ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਹੁ-ਏਜੰਟ ਹੱਲ ਬਣਾਉਣਾ</a>

## ਪਿਛਲਾ ਪਾਠ

[AI Agents ਅਤੇ Agent ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦਾ ਪਰਿਚਯ](../01-intro-to-ai-agents/README.md)

## ਅਗਲਾ ਪਾਠ

[Agentic Design Patterns ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਮੂਲ ਰੂਪ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।