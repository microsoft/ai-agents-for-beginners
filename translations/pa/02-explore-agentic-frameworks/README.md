[![AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਖੋਜ](../../../translated_images/pa/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਨੂੰ ਦੇਖਣ ਲਈ ਉੱਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਦੀ ਖੋਜ ਕਰੋ

AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਸਾਫਟਵੇਅਰ ਮੰਚ ਹਨ ਜੋ AI ਏਜੰਟਾਂ ਦੇ ਬਣਾਉਣ, ਤੈਨਾਤ ਕਰਨ ਅਤੇ ਪ੍ਰਬੰਧਨ ਨੂੰ ਆਸਾਨ ਬਣਾਉਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ। ਇਹ ਫਰੇਮਵਰਕ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਪ੍ਰੀ-ਬਿਲਟ ਭਾਗ, абਸਟ੍ਰੈਕਸ਼ਨ ਅਤੇ ਉਪਕਰਨ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜੋ ਜਟਿਲ AI ਸਿਸਟਮਾਂ ਦੇ ਵਿਕਾਸ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦੇ ਹਨ।

ਇਹ ਫਰੇਮਵਰਕ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਲੱਖਣ ਪੱਖਾਂ 'ਤੇ ਧਿਆਨ ਕేందਰਿਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਕਿਉਂਕਿ ਇਹ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਆਮ ਚੁਣੌਤੀਆਂ ਲਈ ਮਿਆਰੀਕ੍ਰਿਤ ਪਹੁੰਚਾਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। ਇਹ AI ਸਿਸਟਮਾਂ ਨੂੰ ਬਣਾਉਣ ਵਿੱਚ ਸਕੇਲਬਿਲਿਟੀ, ਉਪਲਬਧਤਾ ਅਤੇ ਕੁਸ਼ਲਤਾ ਵਧਾਉਂਦੇ ਹਨ।

## ਪਰਚય

ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:

- AI ਏਜੰਟ ਫਰੇਮਵਰਕ ਕੀ ਹਨ ਅਤੇ ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਕੀ ਪ੍ਰਾਪਤ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ?
- ਟੀਮਾਂ ਇਨ੍ਹਾਂ ਨੂੰ ਕਿਵੇਂ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਸੁਧਾਰ ਅਤੇ ਆਪਣੇ ਏਜੰਟ ਦੀਆਂ صلاحਤਾਂ ਨੂੰ ਵਧਾ ਸਕਦੀਆਂ ਹਨ?
- ਮਾਇਕ੍ਰੋਸੌਫਟ ਦੁਆਰਾ ਬਣਾਏ ਗਏ ਫਰੇਮਵਰਕ ਅਤੇ ਉਪਕਰਨਾਂ ਵਿਚ ਕੀ ਫਰਕ ਹਨ (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ਅਤੇ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਇਕੋਸਿਸਟਮ ਟੂਲਜ਼ ਨੂੰ ਸਿੱਧਾ ਜੋੜ ਸਕਦਾ ਹਾਂ, ਜਾਂ ਕੀ ਮੈਨੂੰ ਅਲੱਗ ਸਟੈਂਡਅਲੋਨ ਹੱਲਾਂ ਦੀ ਲੋੜ ਹੈ?
- Microsoft Foundry Agent Service ਕੀ ਹੈ ਅਤੇ ਇਹ ਮੇਰੀ ਮਦਦ ਕਿਵੇਂ ਕਰ ਰਿਹਾ ਹੈ?

## ਸਿੱਖਣ ਦੇ ਲੱਖੜੇ

ਇਸ ਪਾਠ ਦਾ ਉਦੇਸ਼ ਤੁਹਾਨੂੰ ਸਹਾਇਤਾ ਕਰਨਾ ਹੈ ਕਿ:

- AI Agent Frameworks ਦਾ AI ਵਿਕਾਸ ਵਿੱਚ ਭੂਮਿਕਾ ਸਮਝੋ।
- ਕਿਵੇਂ AI Agent Frameworks ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬੁੱਧਿਮਾਨ ਏਜੰਟ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।
- AI Agent Frameworks ਦੁਆਰਾ ਚਾਲੂ ਕੀਤੀਆਂ ਮੁੱਖ صلاحਤਾਂ।
- Microsoft Agent Framework ਅਤੇ Microsoft Foundry Agent Service ਵਿਚਕਾਰ ਦੇ ਫਰਕਾਂ ਦੀ ਜਾਣਕਾਰੀ।

## AI Agent Frameworks ਕੀ ਹਨ ਅਤੇ ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਕੀ ਕਰਨ ਦੇ ਯੋਗ ਬਨਾਉਂਦੇ ਹਨ?

ਪਰੰਪਰਾਤਮਕ AI ਫਰੇਮਵਰਕ ਤੁਹਾਡੇ ਐਪਾਂ ਵਿੱਚ AI ਨੂੰ ਜੋੜਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਇਹਨਾਂ ਐਪਾਂ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਤਰੀਕਿਆਂ ਨਾਲ ਬਿਹਤਰ ਬਣਾਉਂਦੇ ਹਨ:

- **ਪર્સਨਲਾਈਜੇਸ਼ਨ**: AI ਉਪਭੋਗਤਾ ਦੇ ਵਿਹਾਰ ਅਤੇ ਪਸੰਦਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ ਵਿਅਕਤੀਗਤ ਸਿਫਾਰਸ਼ਾਂ, ਸਮੱਗਰੀ ਅਤੇ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
ਉਦਾਹਰਨ: Netflix ਵਰਗੀਆਂ ਸਟ੍ਰੀਮਿੰਗ ਸੇਵਾਵਾਂ AI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਦੇਖਣ ਦੇ ਇਤਿਹਾਸ ਦੇ ਆਧਾਰ 'ਤੇ ਫਿਲਮਾਂ ਅਤੇ ਸ਼ੋਅਜ਼ ਸੁਝਾਉਂਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾ ਦੀ ਭਾਗੀਦਾਰੀ ਅਤੇ ਸੰਤੁਸ਼ਟੀ ਵਧਦੀ ਹੈ।
- **ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਕੁਸ਼ਲਤਾ**: AI ਦੁਹਰਾਵੇ ਕੰਮਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰ ਸਕਦਾ ਹੈ, ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸਧਾਰਨ ਕਰਦਾ ਹੈ ਅਤੇ ਆਪਰੇਸ਼ਨਲ ਕੁਸ਼ਲਤਾ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ।
ਉਦਾਹਰਨ: ਗਾਹਕ ਸੇਵਾ ਐਪਾਂ AI ਚੈਟਬੌਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਜੋ ਆਮ ਪੁੱਛਗਿੱਛਾਂ ਨੂੰ ਸੰਭਾਲਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਜਵਾਬ ਦੇਣ ਦਾ ਸਮਾਂ ਘਟਾਉਂਦਾ ਹੈ ਅਤੇ ਗੁੰਝਲਦਾਰ ਮੁੱਦੇ ਲਈ ਮਨੁੱਖੀ ਏਜੰਟਾਂ ਨੂੰ ਖਾਲੀ ਕਰਦਾ ਹੈ।
- **ਵਧੀਆ ਉਪਭੋਗਤਾ ਅਨੁਭਵ**: AI ਸਮਾਰਟ ਫੀਚਰ ਜਿਵੇਂ ਵੋਇਸ ਪਛਾਣ, ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੋਸੈਸਿੰਗ ਅਤੇ ਅਨੁਮਾਨੀ ਟੈਕਸਟ ਪ੍ਰਦਾਨ ਕਰਕੇ ਸਮੁੱਚੇ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ।
ਉਦਾਹਰਨ: Siri ਅਤੇ Google Assistant ਵਰਗੇ ਵਰਚੁਅਲ ਸਹਾਇਕ AI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੋਇਸ ਕਮਾਂਡ ਨੂੰ ਸਮਝਦੇ ਅਤੇ ਜਵਾਬ ਦੇਂਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਉਪਕਰਨਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨਾ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ।

### ਇਹ ਸਭ ਵਧੀਆ ਲੱਗਦਾ ਹੈ, ਤਾਂ ਫਿਰ ਸਾਨੂੰ AI Agent Framework ਦੀ ਲੋੜ ਕਿਉਂ ਹੈ?

AI Agent ਫਰੇਮਵਰਕ ਸਿਰਫ AI ਫਰੇਮਵਰਕ ਤੋਂ ਵੱਧ ਚੀਜ਼ ਪ੍ਰਤੀਨਿਧਤ ਕਰਦੇ ਹਨ। ਇਹ ਇੰਟੈਲੀਜੈਂਟ ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ ਜੋ ਉਪਭੋਗਤਾਵਾਂ, ਹੋਰ ਏਜੰਟਾਂ ਅਤੇ ਵਾਤਾਵਰਨ ਨਾਲ ਅੰਤਰਕਿਰਿਆ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਨਿੱਜੀ ਲਕੜੇ ਪ੍ਰਾਪਤ ਕਰ ਸਕਣ। ਇਹ ਏਜੰਟ ਸੁਤੰਤਰ ਵਰਤਾਰਾ ਦਿਖਾ ਸਕਦੇ ਹਨ, ਫੈਸਲੇ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਬਦਲ ਰਹੇ ਹਾਲਾਤ ਦੇ ਅਨੁਕੂਲ ਹੋ ਸਕਦੇ ਹਨ। ਚਲੋ ਕੁਝ ਮੁੱਖ صلاحਤਾਂ ਵੇਖੀਏ ਜੋ AI Agent Frameworks ਦੁਆਰਾ ਕਾਇਮ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ:

- **ਏਜੰਟ ਸਹਿਯੋਗ ਅਤੇ ਸੰਯੋਜਨ**: ਵੱਖ-ਵੱਖ AI ਏਜੰਟ ਬਣਾਉਣ ਯੋਗ ਜੋ ਮਿਲ ਕੇ ਕੰਮ ਕਰ ਸਕਣ, ਗੱਲਬਾਤ ਕਰ ਸਕਣ ਅਤੇ ਪੇਚੀਦਾ ਕੰਮ ਹੱਲ ਕਰਨ ਲਈ ਸੰਯੋਜਿਤ ਹੋ ਸਕਣ।
- **ਟਾਸਕ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਪ੍ਰਬੰਧਨ**: ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋਜ਼, ਟਾਸਕ ਸੌਂਪਣਾ ਅਤੇ ਏਜੰਟਾਂ ਵਿੱਚ ਗਤੀਸ਼ੀਲ ਟਾਸਕ ਪ੍ਰਬੰਧਨ ਦੇ ਆਟੋਮੇਸ਼ਨ ਲਈ ਮਕੈਨਜ਼ਮ ਪ੍ਰਦਾਨ ਕਰਨਾ।
- **ਪ੍ਰਸੰਗਤ ਸਮਝ ਅਤੇ ਅਨੁਕੂਲਤਾ**: ਏਜੰਟਾਂ ਨੂੰ ਸਮੱਗਰੀ ਨੂੰ ਸਮਝਣ, ਬਦਲਦੇ ਵਾਤਾਵਰਨ ਦੇ ਅਨੁਕੂਲ ਬਣਨ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਜਾਣਕਾਰੀ ਦੇ ਆਧਾਰ 'ਤੇ ਫੈਸਲੇ ਕਰਨ ਯੋਗ ਬਨਾਉਣਾ।

ਇਸ ਲਈ ਸੰਖੇਪ ਵਿੱਚ, ਏਜੰਟ ਤੁਹਾਨੂੰ ਹੋਰ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ, ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਅਗਲੇ ਪੱਧਰ 'ਤੇ ਲੈ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਹੋਰ ਬੁੱਧਿਮਾਨ ਸਿਸਟਮ ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਆਪਣੇ ਵਾਤਾਵਰਨ ਤੋਂ ਸਿੱਖ ਸਕਦੇ ਅਤੇ ਅਨੁਕੂਲ ਹੋ ਸਕਦੇ ਹਨ।

## ਏਜੰਟ ਦੀਆਂ صلاحਤਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਸੁਧਾਰ ਅਤੇ ਵਧਾਉਣ ਦਾ ਤਰੀਕਾ?

ਇਹ ਇੱਕ ਤੇਜ਼ੀ ਨਾਲ ਬਦਲਦਾ ਖੇਤਰ ਹੈ, ਪਰ ਜ਼ਿਆਦਾਤਰ AI Agent Frameworks ਵਿੱਚ ਕੁਝ ਸਾਂਝੇ ਤੱਤ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਅਤੇ ਸੁਧਾਰ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਮੋਡੀਊਲ ਭਾਗ, ਸਹਿਯੋਗੀ ਉਪਕਰਨ, ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਸਿੱਖਣਾ। ਚਲੋ ਇਨ੍ਹਾਂ ਵਿੱਚ ਡੁੱਬਕੀ ਮਾਰਦੇ ਹਾਂ:

- **ਮੋਡੀਊਲ ਭਾਗਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ**: AI SDK ਪ੍ਰੀ-ਬਿਲਟ ਭਾਗ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਵੇਂ AI ਅਤੇ ਮੈਮੋਰੀ ਕਨੈਕਟਰ, ਪ੍ਰਾਕ੍ਰਿਤਿਕ ਭਾਸ਼ਾ ਜਾਂ ਕੋਡ ਪਲੱਗਇਨਜ਼ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ, ਪ੍ਰਾਂਪਟ ਟੈਮਪਲੇਟ ਆਦਿ।
- **ਸਹਿਯੋਗੀ ਉਪਕਰਨ ਲਾਭ**: ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਟਾਸਕਾਂ ਵਾਲੇ ਏਜੰਟ ਤਿਆਰ ਕਰੋ, ਜੋ ਮਿਲ ਕੇ ਕੰਮ ਕਰਣ ਅਤੇ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਟੈਸਟ ਅਤੇ ਸੁਧਾਰ ਕਰਨ ਦੀ ਯੋਗਤਾ ਰੱਖਦੇ ਹਨ।
- **ਰੀਅਲ-ਟਾਈਮ ਸਿੱਖੋ**: ਫੀਡਬੈਕ ਲੂਪ ਲਾਗੂ ਕਰੋ ਜਿੱਥੇ ਏਜੰਟ ਇੰਟਰਐਕਸ਼ਨ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣਾ ਵਰਤਾਰਾ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਢਾਲਦੇ ਹਨ।

### ਮੋਡੀਊਲ ਭਾਗਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਮਾਇਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਵਰਗੇ SDK ਮੋਡੀਊਲ ਭਾਗ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਵੇਂ AI ਕਨੈਕਟਰ, ਟੂਲ ਡਿਫਿਨੀਸ਼ਨ, ਅਤੇ ਏਜੰਟ ਪ੍ਰਬੰਧਨ।

**ਟੀਮ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਇਨ੍ਹਾਂ ਭਾਗਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਜੋੜ੍ਹ ਕੇ ਇੱਕ ਕਾਰਗਰ ਪ੍ਰੋਟੋਟਾਈਪ ਤਿਆਰ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਯੋਗਤਮ ਪ੍ਰਯੋਗ ਅਤੇ ਸੁਧਾਰ ਸੰਭਵ ਹੁੰਦਾ ਹੈ।

**ਅਮਲੀ ਤੌਰ 'ਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਇੱਕ ਪ੍ਰੀ-ਬਿਲਟ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਜਾਣਕਾਰੀ ਮਿਲਾ ਸਕਦੇ ਹੋ, ਇਕ ਮੈਮੋਰੀ ਮੋਡੀਊਲ ਵਿੱਚ ਡੇਟਾ ਸਟੋਰ ਅਤੇ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਇੱਕ ਪ੍ਰਾਂਪਟ ਜਨਰੇਟਰ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰ ਸਕਦੇ ਹੋ, ਬਿਨਾਂ ਇਨ੍ਹਾਂ ਭਾਗਾਂ ਨੂੰ ਸਿਰੇ ਤੋਂ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੈ।

**ਕੋਡ ਦਾ ਉਦਾਹਰਨ**: ਚਲੋ ਦੇਖੀਏ ਕਿ ਤੁਸੀਂ Microsoft Agent Framework ਨੂੰ `FoundryChatClient` ਨਾਲ ਕਿਵੇਂ ਵਰਤ ਕੇ ਮਾਡਲ ਨੂੰ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੇ ਟੂਲ ਕਾਲਿੰਗ ਨਾਲ ਜਵਾਬ ਦੇਣ ਲਈ ਕਿਵੇਂ ਬਣਾ ਸਕਦੇ ਹੋ:

``` python
# ਮਾਇਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਪਾਇਥਨ ਉਦਾਹਰਣ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ਯਾਤਰਾ ਬੁੱਕ ਕਰਨ ਲਈ ਇੱਕ ਨਮੂਨਾ ਟੂਲ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ਉਦਾਹਰਣ ਨਤੀਜਾ: ਤੁਹਾਡੀ 1 ਜਨਵਰੀ 2025 ਨੂੰ ਨਿਊਯਾਰਕ ਲਈ ਉਡਾਣ ਸਫਲਤਾਪੂਰਵਕ ਬੁੱਕ ਹੋ ਚੁੱਕੀ ਹੈ। ਸੁਰੱਖਿਅਤ ਯਾਤਰਾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ਇਸ ਉਦਾਹਰਨ ਤੋਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਕਿਸ ਤਰ੍ਹਾਂ ਪ੍ਰੀ-ਬਿਲਟ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਮੁੱਖ ਜਾਣਕਾਰੀ, ਜਿਵੇਂ ਕਿ ਉਤਪੱਤੀ, ਮੰਜ਼ਿਲ, ਅਤੇ ਉਡਾਣ ਦੀ ਮਿਤੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਮੋਡੀਊਲਰ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਉੱਚ-ਸਤਰ ਦੀ ਲਾਜ਼ਿਕ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਨ ਦੀ ਆਜ਼ਾਦੀ ਦਿੰਦੀ ਹੈ।

### ਸਹਿਯੋਗੀ ਉਪਕਰਨ ਲਾਭ

Microsoft Agent Framework ਵਰਗੇ ਫਰੇਮਵਰਕ ਵੱਖ-ਵੱਖ ਏਜੰਟਾਂ ਨੂੰ ਮਿਲ ਕੇ ਕੰਮ ਕਰਨ ਦੀ ਸਮਰਥਾ ਦਿੱਦੇ ਹਨ।

**ਟੀਮ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਟਾਸਕਾਂ ਵਾਲੇ ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਜੋ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਦੀ ਟੈਸਟਿੰਗ ਅਤੇ ਸੁਧਾਰ ਵੱਲ ਮਦਦ ਕਰਦਾ ਹੈ ਅਤੇ ਸਿਸਟਮ ਦੀ ਕੁੱਲ ਕੁਸ਼ਲਤਾ ਵਧਾਉਂਦਾ ਹੈ।

**ਅਮਲੀ ਤੌਰ 'ਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਏਜੰਟਾਂ ਦੀ ਟੀਮ ਬਣਾ ਸਕਦੇ ਹੋ ਜਿੱਥੇ ਹਰ ਏਜੰਟ ਦੀ ਇਕ ਵਿਸ਼ੇਸ਼ ਕਿਰਦਾਰ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ ਡੇਟਾ ਪ੍ਰਾਪਤੀ, ਵਿਸ਼ਲੇਸ਼ਣ ਜਾਂ ਫੈਸਲਾਬੰਦੀ। ਇਹ ਏਜੰਟ ਇੱਕਠੇ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਜਾਣਕਾਰੀ ਸਾਂਝੀ ਕਰਕੇ ਇੱਕ ਸਾਂਝਾ ਲਕੜਾ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਇੱਕ ਉਪਭੋਗਤਾ ਦੇ ਸਵਾਲ ਦਾ ਜਵਾਬ ਦੇਣਾ ਜਾਂ ਕਿਸੇ ਟਾਸਕ ਨੂੰ ਪੂਰਾ ਕਰਨਾ।

**ਕੋਡ ਦਾ ਉਦਾਹਰਨ (Microsoft Agent Framework)**:

```python
# ਮਾਈਕਰੋਸਾਫਟ ਏਜੈਂਟ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇਕੱਠੇ ਕੰਮ ਕਰਨ ਵਾਲੇ ਕਈ ਏਜੈਂਟ ਬਣਾਉਣਾ

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ਡਾਟਾ ਪ੍ਰਾਪਤੀ ਏਜੈਂਟ
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਏਜੈਂਟ
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ਇੱਕ ਟਾਸਕ 'ਤੇ ਕਰਮਬੱਧਤਾ ਨਾਲ ਏਜੈਂਟ ਚਲਾਓ
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ਤੁਹਾਨੂੰ ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਦਿੱਸ ਰਹੀ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਵੱਖ-ਵੱਖ ਵਿਸ਼ੇਸ਼ਤਾ ਵਾਲੇ ਕਈ ਏਜੰਟਾਂ ਦੀ ਟੀਮ ਬਣਾਕੇ ਡਾਟਾ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ ਟਾਸਕ ਸਿਰਜ ਸਕਦੇ ਹੋ। ਹਰ ਏਜੰਟ ਇਕ ਨਿਰਧਾਰਤ ਫੰਕਸ਼ਨ ਕਰਦਾ ਹੈ, ਅਤੇ ਟਾਸਕ ਉਹਨਾਂ ਏਜੰਟਾਂ ਦਾ ਸਹਿਯੋਗ ਕਰਕੇ ਲਕੜਾ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ। ਮਖ਼ਸੂਸ ਭੂਮਿਕਾ ਵਾਲੇ ਸਮਰਪਿਤ ਏਜੰਟਾਂ ਦੀ ਰਚਨਾ ਨਾਲ ਤੁਸੀਂ ਟਾਸਕ ਦੀ ਕੁਸ਼ਲਤਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਵਧਾ ਸਕਦੇ ਹੋ।

### ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਿੱਖਣਾ

ਅੱਗੇ ਵਧੇ ਹੋਏ ਫਰੇਮਵਰਕਸ ਰੀਅਲ-ਟਾਈਮ ਸਮੱਗਰੀ ਸਮਝਣ ਅਤੇ ਅਨੁਕੂਲਤਾ ਦੀਆਂ صلاحਤਾਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਟੀਮ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਫੀਡਬੈਕ ਲੂਪ ਲਾਗੂ ਕਰ ਸਕਦੀਆਂ ਹਨ ਜਿੱਥੇ ਏਜੰਟ ਇੰਟਰਐਕਸ਼ਨਾਂ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣਾ ਵਰਤਾਰਾ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਢਾਲਦੇ ਹਨ, ਜਿਸ ਨਾਲ صلاحਤਾਂ ਦਾ ਲਗਾਤਾਰ ਸੁਧਾਰ ਅਤੇ ਸੰਵਰਧਨ ਹੁੰਦਾ ਹੈ।

**ਅਮਲੀ ਤੌਰ 'ਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਏਜੰਟ ਉਪਭੋਗਤਾ ਫੀਡਬੈਕ, ਵਾਤਾਵਰਨ ਡੇਟਾ ਅਤੇ ਟਾਸਕ ਨਤੀਜੇ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਉਹਨਾਂ ਦਾ ਗਿਆਨ ਬੇਸ ਅਪਡੇਟ ਹੋਵੇ, ਫੈਸਲਾ ਕਰਨ ਵਾਲੇ ਅਲਗੋਰਿਦਮ ਢਾਲੇ ਜਾਣ ਅਤੇ ਸਮੇਂ ਨਾਲ ਪ੍ਰਦਰਸ਼ਨ ਸੁਧਰੇ। ਇਹ ਦੋਹਰਾਇਆ ਜਾਣ ਵਾਲਾ ਸਿੱਖਣ ਵਾਲਾ ਪ੍ਰਕ੍ਰਿਆ ਏਜੰਟਾਂ ਨੂੰ ਬਦਲ ਰਹੀਆਂ ਸਥਿਤੀਆਂ ਅਤੇ ਉਪਭੋਗਤਾ ਦੀਆਂ ਪਸੰਦਾਂ ਦੇ ਅਨੁਕੂਲ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ ਸਮੁੱਚੇ ਸਿਸਟਮ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਵਧਾਉਂਦਾ ਹੈ।

## Microsoft Agent Framework ਅਤੇ Microsoft Foundry Agent Service ਵਿਚਕਾਰ ਕੀ ਫਰਕ ਹਨ?

ਇਨ੍ਹਾਂ ਪਹੁੰਚਾਂ ਦੀ ਤੁਲਨਾ ਕਰਨ ਦੇ ਕਈ ਤਰੀਕੇ ਹਨ, ਪਰ ਆਓ ਕੁਝ ਮੁੱਖ ਫਰਕਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ, صلاحਤਾਂ ਅਤੇ ਲਕੜਾ ਵਰਤੋਂ ਮਾਮਲਿਆਂ ਦੇ ਮੂਡ ਵਿੱਚ ਵੇਖੀਏ:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ਇੱਕ ਸੁਧਾਰਿਆ ਹੋਇਆ SDK ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ ਜੋ `FoundryChatClient` ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI ਏਜੰਟ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ Azure OpenAI ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਨਾਲ ਟੂਲ ਕਾਲਿੰਗ, ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ ਅਤੇ ਐਜ਼ਯੂਰ ਆਈਡੈਂਟਿਟੀ ਦੁਆਰਾ ਏਜੰਟ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

**ਵਰਤੋਂ ਮਾਮਲੇ**: ਟੂਲ ਯੂਜ਼, ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋਜ਼, ਅਤੇ ਇੰਟਰਪਰਾਈਜ਼ ਏਕਤਾ ਸਥਿਤੀਆਂ ਨਾਲ ਪ੍ਰੋਡਕਸ਼ਨ ਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣਾ।

Microsoft Agent Framework ਦੇ ਕੁਝ ਮੁੱਖ ਮੂਲ ਧਾਰਨਾ ਇਹ ਹਨ:

- **ਏਜੰਟ**: ਏਜੰਟ `FoundryChatClient` ਰਾਹੀਂ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਨਾਮ, ਨਿਰਦੇਸ਼ਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਸੰਰਚਿਤ ਹੁੰਦਾ ਹੈ। ਏਜੰਟ ਕਰ ਸਕਦਾ ਹੈ:
  - **ਯੂਜ਼ਰ ਸੁਨੇਹਿਆਂ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨਾ** ਅਤੇ Azure OpenAI ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ।
  - **ਕੰਵਰਸੇਸ਼ਨ ਸੰਦਰਭ ਦੇ ਅਧਾਰ 'ਤੇ ਟੂਲ ਕਾਲ ਕਰਨਾ**।
  - **ਮੁਲਾਕਾਤਾਂ ਦੇ ਦੌਰਾਨ ਗੱਲਬਾਤ ਦੀ ਸਥਿਤੀ ਬਣਾਈ ਰੱਖਣਾ**।

  ਇੱਥੇ ਇੱਕ ਕੋਡ ਸਨਿੱਪੇਟ ਦਿੱਤਾ ਹੈ ਜੋ ਏਜੰਟ ਬਣਾਉਣ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਦਾ ਹੈ:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ਟੂਲ**: ਫਰੇਮਵਰਕ Python ਫੰਕਸ਼ਨਾਂ ਵਜੋਂ ਟੂਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ ਜੋ ਏਜੰਟ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ। ਟੂਲ ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਰਜਿਸਟਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ਬਹੁ-ਏਜੰਟ ਸੰਯੋਜਨ**: ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਖੇਤਰਾਂ ਵਿੱਚ ਵਿਸ਼ੇਸ਼ਤਾ ਰੱਖਣ ਵਾਲੇ ਕਈ ਏਜੰਟ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ ਉਹਨਾਂ ਦਾ ਕੰਮ ਸੰਯੋਜਿਤ ਕਰ ਸਕਦੇ ਹੋ:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **ਐਜ਼ਯੂਰ ਆਈਡੈਂਟਿਟੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਫਰੇਮਵਰਕ `AzureCliCredential` (ਜਾਂ `DefaultAzureCredential`) ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਸੁਰੱਖਿਅਤ, ਕੀਲੇਸ ਪ੍ਰਮਾਣੀਕਰਨ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ ਅਤੇ API ਕੀਜ਼ ਨੂੰ ਸਿੱਧਾ ਸੰਭਾਲਣ ਦੀ ਲੋੜ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ।

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service ਮਾਇਕ੍ਰੋਸੌਫਟ Ignite 2024 ਵਿੱਚ ਪੇਸ਼ ਕੀਤਾ ਗਿਆ ਇੱਕ ਨਵਾਂ ਐਡ-ਆਨ ਹੈ। ਇਹ AI ਏਜੰਟਾਂ ਦਾ ਵਿਕਾਸ ਅਤੇ ਤੈਨਾਤ ਕਰਨ ਲਈ ਵਧੇਰੇ ਲਚਕੀਲੇ ਮਾਡਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਆਪਣੇ ਆਪ Llama 3, Mistral, ਅਤੇ Cohere ਵਰਗੇ ਖੁੱਲ੍ਹਾ ਸਰੋਤ LLMs ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰਨਾ।

Microsoft Foundry Agent Service ਵਧੀਆ ਇੰਟਰਪਰਾਈਜ਼ ਸੁਰੱਖਿਆ ਮਕੈਨਜ਼ਮ ਅਤੇ ਡੇਟਾ ਸਟੋਰੇਜ਼ ਤਰੀਕੇ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਇੰਟਰਪਰਾਈਜ਼ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਚਿਤ ਹੋ ਜਾਂਦਾ ਹੈ।

ਇਹ Microsoft Agent Framework ਦੇ ਨਾਲ ਬਿਨਾਂ ਕਿਸੇ ਰੁਕਾਵਟ ਦੇ ਕੰਮ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਏਜੰਟ ਬਿਲਡਿੰਗ ਅਤੇ ਤੈਨਾਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਮਿਲੇ।

ਇਹ ਸੇਵਾ ਅਜੇ ਜਨਤਾ ਲਈ ਪ੍ਰੀਵੀਊ ਵਿੱਚ ਹੈ ਅਤੇ ਏਜੰਟ ਬਿਲਡਿੰਗ ਲਈ Python ਅਤੇ C# ਲੈਂਗਵੇਜ ਸਹਾਇਤਾ ਕਰਦੀ ਹੈ।

Microsoft Foundry Agent Service Python SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਅਸੀਂ ਇੱਕ ਯੂਜ਼ਰ-ਡਿਫਾਈਨਡ ਟੂਲ ਨਾਲ ਏਜੰਟ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਾਂ:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ਟੂਲ ਫੰਕਸ਼ਨਾਂ ਦੀ ਪਰਿਭਾਸ਼ਾ ਕਰੋ
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### ਮੁੱਖ ਧਾਰਨਾਵਾਂ

Microsoft Foundry Agent Service ਦੇ ਕੁਝ ਮੁੱਖ ਧਾਰਨਾ ਇਹ ਹਨ:

- **ਏਜੰਟ**: Microsoft Foundry Agent Service Microsoft Foundry ਨਾਲ ਮਿਲ ਕੇ ਕੰਮ ਕਰਦਾ ਹੈ। Microsoft Foundry ਵਿੱਚ AI ਏਜੰਟ 'ਸਮਾਰਟ' ਮਾਈਕ੍ਰੋਸਰਵਿਸ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜੋ ਸਵਾਲਾਂ (RAG), ਕਾਰਵਾਈਆਂ ਜਾਂ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਆਟੋਮੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਜੇਨੇਰੇਟਿਵ AI ਮਾਡਲਾਂ ਦੀ ਤਾਕਤ ਅਤੇ ਉਪਕਰਨਾਂ ਨੂੰ ਮਿਲਾ ਕੇ ਹਕੀਕਤੀ ਡੇਟਾ ਸਰੋਤਾਂ ਨਾਲ ਪਹੁੰਚ ਅਤੇ ਅੰਤਰਕਿਰਿਆ ਕਰਨ ਯੋਗ ਬਨਾਉਂਦਾ ਹੈ। ਇੱਥੇ ਇੱਕ ਏਜੰਟ ਦਾ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਇੱਕ ਏਜੰਟ ਮਾਡਲ `gpt-5-mini` ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਨਾਮ `my-agent`, ਅਤੇ ਨਿਰਦੇਸ਼ਾਂ `ਤੁਸੀਂ ਮਦਦਗਾਰ ਏਜੰਟ ਹੋ`. ਇਹ ਏਜੰਟ ਕੋਡ ਵਿਆਖਿਆ ਕਰਨ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਕਰਨ ਲਈ ਟੂਲਾਂ ਅਤੇ ਸਰੋਤਾਂ ਨਾਲ ਸਜਿਆ ਹੋਇਆ ਹੈ।

- **ਥ੍ਰੈਡ ਅਤੇ ਸੁਨੇਹੇ**: ਥ੍ਰੈਡ ਇੱਕ ਹੋਰ ਮਹੱਤਵਪੂਰਨ ਧਾਰਨਾ ਹੈ। ਇਹ ਇੱਕ ਗੱਲਬਾਤ ਜਾਂ ਉਪਭੋਗਤਾ ਅਤੇ ਏਜੰਟ ਵਿਚਕਾਰ ਇੰਟਰਐਕਸ਼ਨ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਥ੍ਰੈਡਾਂ ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਟਰੈਕ ਕਰਨ, ਸੰਦਰਭ ਜਾਣਕਾਰੀ ਸਟੋਰ ਕਰਨ ਅਤੇ ਅੰਤਰਕਿਰਿਆ ਦੀ ਸਥਿਤੀ ਪ੍ਰਬੰਧਤ ਕਰ ਸਕਦੀਆਂ ਹਨ। ਇੱਥੇ ਇੱਕ ਥ੍ਰੈਡ ਦਾ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ਏਜੰਟ ਨੂੰ ਥ੍ਰੇਡ ਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕਹੋ
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ਏਜੰਟ ਦੀ ਪ੍ਰਤੀਕਿਰਿਆ ਵੇਖਣ ਲਈ ਸਾਰੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰੋ ਅਤੇ ਲਾਗ ਕਰੋ
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ, ਇੱਕ ਥ੍ਰੈਡ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਫਿਰ ਥ੍ਰੈਡ ਨੂੰ ਸੁਨੇਹਾ ਭੇਜਿਆ ਗਿਆ। `create_and_process_run` ਕਾਲ ਕਰਕੇ, ਏਜੰਟ ਨੂੰ ਥ੍ਰੈਡ 'ਤੇ ਕੰਮ ਕਰਨ ਨੂੰ ਕਿਹਾ ਗਿਆ। ਆਖ਼ਿਰ ਵਿੱਚ, ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕੀਤੇ ਗਏ ਅਤੇ ਏਜੰਟ ਦੇ ਜਵਾਬ ਨੂੰ ਲੌਗ ਕੀਤਾ ਗਿਆ। ਸੁਨੇਹੇ ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਦਰਸਾਉਂਦੇ ਹਨ। ਇਹ ਸਮਝਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਸੁਨੇਹੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ ਟੈਕਸਟ, ਤਸਵੀਰ ਜਾਂ ਫਾਈਲ, ਮਤਲਬ ਏਜੰਟ ਦਾ ਕੰਮ ਜਿਵੇਂ ਕਿ ਇੱਕ ਤਸਵੀਰ ਜਾਂ ਇੱਕ ਟੈਕਸਟ ਜਵਾਬ ਹੈ। ਇੱਕ ਵਿਕਾਸਕਾਰ ਵਜੋਂ, ਤੁਸੀਂ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਜਵਾਬ ਨੂੰ ਅਗਲੇ ਪ੍ਰਕਿਰਿਆ ਜਾਂ ਯੂਜ਼ਰ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ।

- **Microsoft Agent Framework ਨਾਲ ਇੰਟੈਗਰੇਸ਼ਨ**: Microsoft Foundry Agent Service Microsoft Agent Framework ਨਾਲ ਬਿਨਾਂ ਰੁਕਾਵਟ ਦੇ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਸਦਾ ਅਰਥ ਹੈ ਕਿ ਤੁਸੀਂ `FoundryChatClient` ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਏਜੰਟ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ ਉਹਨਾਂ ਨੂੰ Agent Service ਰਾਹੀਂ ਪ੍ਰੋਡਕਸ਼ਨ ਲਈ ਤੈਨਾਤ ਕਰ ਸਕਦੇ ਹੋ।

**ਵਰਤੋਂ ਮਾਮਲੇ**: Microsoft Foundry Agent Service ਉਹਨਾਂ ਇੰਟਰਪਰਾਈਜ਼ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ ਜਿਹੜੇ ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ ਅਤੇ ਲਚਕੀਲੀ AI ਏਜੰਟ ਤੈਨਾਤੀ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

## ਇਹਨਾਂ ਪਹੁੰਚਾਂ ਵਿਚਕਾਰ ਕੀ ਫਰਕ ਹੈ?
 
ਇਹ ਸਚ ਹੈ ਕਿ ਇਨ੍ਹਾਂ ਵਿੱਚ ਕੁਝ ਓਵਰਲੈਪ ਹੈ, ਪਰ ਡਿਜ਼ਾਈਨ, صلاحਤਾਂ ਅਤੇ ਲਕੜਾ ਵਰਤੋਂ ਮਾਮਲਿਆਂ ਵਿੱਚ ਕੁਝ ਮੁੱਖ ਫਰਕ ਹਨ:
 
- **Microsoft Agent Framework (MAF)**: ਇੱਕ ਪ੍ਰੋਡਕਸ਼ਨ-ਯੋਗ SDK ਹੈ ਜੋ AI ਏਜੰਟ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਟੂਲ ਕਾਲਿੰਗ, ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ ਅਤੇ Azure ਆਈਡੈਂਟਿਟੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ ਇੱਕ ਸਧਾਰਨ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- **Microsoft Foundry Agent Service**: Microsoft Foundry ਵਿੱਚ ਇੱਕ ਪਲੇਟਫਾਰਮ ਅਤੇ ਤੈਨਾਤੀ ਸੇਵਾ ਹੈ। ਇਹ Azure OpenAI, Azure AI Search, Bing Search ਅਤੇ ਕੋਡ ਚਲਾਉਣ ਵਰਗੀਆਂ ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਬਿਲਟ ਕਨੈਕਟੀਵਟੀ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੀ ਹੈ।
 
ਅਜੇ ਵੀ ਇਹ ਪਤਾ ਨਹੀਂ ਕਿ ਕਿਹੜਾ ਚੁਣਨਾ ਹੈ?

### ਵਰਤੋਂ ਮਾਮਲੇ
 
ਆਓ ਕੁਝ ਆਮ ਵਰਤੋਂ ਮਾਮਲਿਆਂ 'ਚੋਂ ਤੁਹਾਡੇ ਲਈ ਮਦਦ ਕਰੀਏ:
 
> ਸਵਾਲ: ਮੈਂ ਪ੍ਰੋਡਕਸ਼ਨ AI ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਵਿਕਾਸ ਕਰ ਰਿਹਾ ਹਾਂ ਅਤੇ ਤੇਜ਼ੀ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨੀ ਚਾਹੁੰਦਾ ਹਾਂ
>

>ਜਵਾਬ: Microsoft Agent Framework ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੈ। ਇਹ `FoundryChatClient` ਰਾਹੀਂ ਇੱਕ ਸਧਾਰਨ, Python ਪ੍ਰਕਾਰ ਦਾ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਕੁਝ ਲਾਈਨਾਂ ਕੋਡ ਨਾਲ ਟੂਲਾਂ ਅਤੇ ਨਿਰਦੇਸ਼ਾਂ ਵਾਲੇ ਏਜੰਟ ਤਿਆਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

>ਸਵਾਲ: ਮੈਨੂੰ ਇੰਟਰਪਰਾਈਜ਼-ਗ੍ਰੇਡ ਤੈਨਾਤੀ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਜਿਸ ਵਿੱਚ Azure ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਜਿਵੇਂ Search ਅਤੇ ਕੋਡ ਚਲਾਉਣਾ ਸ਼ਾਮਲ ਹਨ
>
>ਜਵਾਬ: Microsoft Foundry Agent Service ਸਭ ਤੋਂ ਉਚਿਤ ਹੈ। ਇਹ ਪਲੇਟਫਾਰਮ ਸੇਵਾ ਹੈ ਜੋ ਕਈ ਮਾਡਲ, Azure AI Search, Bing Search ਅਤੇ Azure Functions ਲਈ ਇੰਬਿਲਟ صلاحਤਾਂ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੀ ਹੈ। ਇਹ Foundry ਪੋਰਟਲ ਵਿੱਚ ਤੁਹਾਡੇ ਏਜੰਟ ਬਨਾਉਣ ਅਤੇ ਸਕੇਲ ਤੇ ਤੈਨਾਤ ਕਰਨ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦਾ ਹੈ।
 
> ਸਵਾਲ: ਮੈਂ ਹੁਣ ਵੀ ਗੁੰਝਲ ਵਿੱਚ ਹਾਂ, ਸਿਰਫ ਇੱਕ ਵਿਕਲਪ ਦਿਓ
>
>ਜਵਾਬ: ਆਪਣੇ ਏਜੰਟ ਬਣਾਉਣ ਲਈ Microsoft Agent Framework ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ, ਅਤੇ ਜਦੋਂ ਤੁਹਾਨੂੰ ਉਨ੍ਹਾਂ ਨੂੰ ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਤੈਨਾਤ ਅਤੇ ਸਕੇਲ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ Microsoft Foundry Agent Service ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇਹ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਆਪਣੀ ਏਜੰਟ ਲਾਜਿਕ 'ਤੇ ਕੰਮ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਅਤੇ ਇੰਟਰਪਰਾਈਜ਼ ਤੈਨਾਤੀ ਲਈ ਇੱਕ ਸਾਫ ਰਸਤਾ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।
 
ਆਓ ਕੁਝ ਮੁੱਖ ਫਰਕਾਂ ਬਾਰੇ ਇੱਕ ਟੇਬਲ ਵਿੱਚ ਸੰਖੇਪ ਕਰੀਏ:

| ਫਰੇਮਵਰਕ | ਧਿਆਨ | ਮੁੱਖ ਧਾਰਨਾ | ਵਰਤੋਂ ਮਾਮਲੇ |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ਟੂਲ ਕਾਲਿੰਗ ਨਾਲ ਸੁਧਾਰਿਆ ਗਿਆ ਏਜੰਟ SDK | ਏਜੰਟ, ਟੂਲਜ਼, Azure ਆਈਡੈਂਟਿਟੀ | AI ਏਜੰਟ ਬਣਾਉਣਾ, ਟੂਲ ਵਰਤੋਂ, ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋਜ਼ |
| Microsoft Foundry Agent Service | ਲਚਕੀਲੇ ਮਾਡਲ, ਇੰਟਰਪਰਾਈਜ਼ ਸੁਰੱਖਿਆ, ਕੋਡ ਜਨਰੇਸ਼ਨ, ਟੂਲ ਕਾਲਿੰਗ | ਮੋਡੀਊਲਰਿਟੀ, ਸਹਿਯੋਗ, ਪ੍ਰਕਿਰਿਆ ਆਰਕੀਸਟ੍ਰੇਸ਼ਨ | ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ, ਅਤੇ ਲਚਕੀਲੀ AI ਏਜੰਟ ਤੈਨਾਤੀ |

## ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਇਕੋਸਿਸਟਮ ਟੂਲਜ਼ ਨੂੰ ਸਿੱਧਾ ਜੋੜ ਸਕਦਾ ਹਾਂ, ਜਾਂ ਕੀ ਮੈਨੂੰ ਅਲੱਗ ਸਟੈਂਡਅਲੋਨ ਹੱਲਾਂ ਦੀ ਲੋੜ ਹੈ?


ਜਵਾਬ ਹਾਂ ਹੈ, ਤੁਸੀਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਇੱਕੋਸਿਸਟਮ ਟੂਲਜ਼ ਨੂੰ Microsoft Foundry Agent Service ਨਾਲ ਸਿੱਧਾ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਖਾਸ ਤੌਰ 'ਤੇ ਕਿਉਂਕਿ ਇਹ ਹੋਰ Azure ਸੇਵਾਵਾਂ ਨਾਲ ਬਿਨਾ ਰੁਕਾਵਟ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਤੁਸੀਂ ਉਦਾਹਰਨ ਵਜੋਂ Bing, Azure AI Search, ਅਤੇ Azure Functions ਨੂੰ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦੇ ਹੋ। Microsoft Foundry ਨਾਲ ਵੀ ਗਹਿਰਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹੈ।

Microsoft Agent Framework ਵੀ `FoundryChatClient` ਅਤੇ Azure ਪਹਚਾਣ ਰਾਹੀਂ Azure ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਹੁੰਦਾ ਹੈ, ਇਸ ਨਾਲ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟ ਟੂਲਜ਼ ਤੋਂ ਸਿੱਧਾ Azure ਸੇਵਾਵਾਂ ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹੋ।

## ਨਮੂਨਾ ਕੋਡ

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ਏਜੰਟ ਫਰੇਮਵਰਕਸ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ ਲਈ, ਦਫ਼ਤਰ ਦੇ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਮੂਲੀਅਤ ਲਈ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟਸ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੈਣ ਲਈ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ।

## ਰੇਫਰੰਸز

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## ਪਿਛਲਾ ਪਾਠ

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## ਅਗਲਾ ਪਾਠ

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->