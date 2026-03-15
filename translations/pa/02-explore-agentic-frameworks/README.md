[![ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦੀ ਖੋਜ](../../../translated_images/pa/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਵੇਖਣ ਲਈ ਉਪਰ ਦੀ ਛਵੀ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦੀ ਖੋਜ

ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕ ਉਹ ਸਾਫਟਵੇਅਰ ਪਲੇਟਫਾਰਮ ਹਨ ਜੋ ਏਆਈ ਏਜੰਟਾਂ ਦੀ ਰਚਨਾ, ਤੈਨਾਤੀ ਅਤੇ ਪ੍ਰਬੰਧਨ ਨੂੰ ਸਰਲ ਬਣਾਉਣ ਲਈ ਡਿਜ਼ਾਇਨ ਕੀਤੇ ਗਏ ਹਨ। ਇਹ ਫਰੇਮਵਰਕ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਪਹਿਲਾਂ ਤੋਂ ਬਣਾਏ ਗਏ ਕੰਪੋਨੈਂਟ, ਅਬਸਟ੍ਰੈਕਸ਼ਨ ਅਤੇ ਟੂਲ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੇ ਹਨ ਜੋ ਜਟਿਲ ਏਆਈ ਸਿਸਟਮਾਂ ਦੇ ਵਿਕਾਸ ਨੂੰ ਸੁਗਮ ਬਣਾਉਂਦੇ ਹਨ।

ਇਹ ਫਰੇਮਵਰਕ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਉਨ੍ਹਾਂ ਦੀਆਂ ਐਪਲਿਕੇਸ਼ਨਾਂ ਦੇ ਵਿਲੱਖਣ ਪਹਲੂਆਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ ਕਿਉਂਕਿ ਇਹ ਏਆਈ ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਆਮ ਚੈਲੰਜਾਂ ਲਈ ਮਿਆਰੀ ਤਰੀਕੇ ਮੁਹੱਈਆ ਕਰਦੇ ਹਨ। ਇਹ ਸਕੇਲੇਬਿਲਿਟੀ, ਪਹੁੰਚਯੋਗਤਾ ਅਤੇ ਕਾਰਗੁਜ਼ਾਰੀ ਵਿੱਚ ਸੁਧਾਰ ਕਰਦੇ ਹਨ।

## ਪਰਿਚਿਆ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹਨਾਂ ਗੱਲਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਵੇਗਾ:

- ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕ ਕੀ ਹਨ ਅਤੇ ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਕੀ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ?
- ਟੀਮਾਂ ਕਿਵੇਂ ਇਨ੍ਹਾਂ ਦਾ ਉਪਯੋਗ ਕਰਕੇ ਆਪਣੀਆਂ ਏਜੰਟ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਦੁਹਰਾਉਂ ਅਤੇ ਸੁਧਾਰ ਸਕਦੀਆਂ ਹਨ?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ਅਤੇ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ਦੁਆਰਾ ਬਣਾਏ ਗਏ ਫਰੇਮਵਰਕਾਂ ਅਤੇ ਟੂਲਾਂ ਵਿੱਚ ਕੀ ਫਰਕ ਹਨ?
- ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਪਰਿਵਾਰਕ ਟੂਲਾਂ ਨੂੰ ਸਿੱਧੇ ਇਕੀਕ੍ਰਿਤ ਕਰ ਸਕਦਾ/ਸਕਦੀ ਹਾਂ, ਜਾਂ ਕੀ ਮੈਨੂੰ standalone ਹੱਲਾਂ ਦੀ ਲੋੜ ਹੈ?
- Azure AI Agents service ਕੀ ਹੈ ਅਤੇ ਇਹ ਮੇਰੀ ਸਹਾਇਤਾ ਕਿਵੇਂ ਕਰ ਰਹੀ ਹੈ?

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਦੇ ਲਕਸ਼ ਇਹ ਹਨ ਕਿ ਤੁਹਾਨੂੰ ਸਮਝ ਆਵੇ:

- ਏਆਈ ਵਿਕਾਸ ਵਿੱਚ ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦੀ ਭੂਮਿਕਾ।
- ਹੁਸ਼ਿਆਰ ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦਾ ਕਿਵੇਂ ਲਾਭ ਉਠਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦੁਆਰਾ ਸੰਭਵ ਮੁੱਖ ਸਮਰੱਥਾਵਾਂ।
- Microsoft Agent Framework ਅਤੇ Azure AI Agent Service ਦਰਮਿਆਨ ਅੰਤਰ।

## ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕ ਕੀ ਹਨ ਅਤੇ ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਕੀ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ?

ਰਵਾਇਤੀ ਏਆਈ ਫਰੇਮਵਰਕ ਤੁਹਾਨੂੰ ਆਪਣੇ ਐਪਾਂ ਵਿੱਚ ਏਆਈ ਨੂੰ ਜੋੜਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਇਹਨਾਂ ਵਿਧੀਆਂ ਨਾਲ ਤੁਹਾਡੇ ਐਪ ਬਿਹਤਰ ਬਣ ਸਕਦੇ ਹਨ:

- **ਵੈਯਕਤੀਗਤਕਰਨ**: ਏਆਈ ਉਪਭੋਗਤਾ ਦੇ ਵਰਤੋਂ ਦੇ ਨਮੂਨੇ ਅਤੇ ਪਸੰਦਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਨਿੱਜੀ ਸਿਫਾਰਿਸ਼ਾਂ, ਸਮੱਗਰੀ ਅਤੇ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ।
Example: Netflix ਵਰਗੀਆਂ ਸਟਰੀਮਿੰਗ ਸੇਵਾਵਾਂ ਦੇਖਣ ਦੇ ਇਤਿਹਾਸ ਦੇ ਆਧਾਰ 'ਤੇ ਫਿਲਮਾਂ ਅਤੇ ਸ਼ੋਅਜ਼ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਨ ਲਈ ਏਆਈ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾ ਦੀ ਭਾਗੀਦਾਰੀ ਅਤੇ ਸੰਤੁਸ਼ਟੀ ਵਧਦੀ ਹੈ।
- **ਸਵਚਾਲਨ ਅਤੇ ਕੁਸ਼ਲਤਾ**: ਏਆਈ ਕੁਝ ਦੋਹਰਾਏ ਜਾਣ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਸਵਚਾਲਿਤ ਕਰ ਸਕਦਾ ਹੈ, ਵਰਕਫ਼ਲੋਜ਼ ਨੂੰ ਉਦੋਂਮ ਨਾਲ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਸਰਗਰਮੀ ਵਿੱਚ ਸੁਧਾਰ ਕਰਦਾ ਹੈ।
Example: ਗਾਹਕ ਸੇਵਾ ਵਾਲੀਆਂ ਐਪਸ ਅਕਸਰ ਆਮ ਪੁੱਛਗਿੱਛਾਂ ਸੰਭਾਲਣ ਲਈ ਏਆਈ-ਚਲਿਤ ਚੈਟਬੋਟਸ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਪ੍ਰਤਿਕ੍ਰਿਆ ਸਮਾਂ ਘਟਦਾ ਹੈ ਅਤੇ ਨਿੱਜੀ ਏਜੰਟਾਂ ਨੂੰ ਜਟਿਲ ਮੁਦਿਆਂ ਲਈ ਖਾਲੀ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
- **ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਵਿੱਚ ਸੁਧਾਰ**: ਏਆਈ ਅਵਾਜ਼ ਪਛਾਣ, ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੋਸੈਸਿੰਗ ਅਤੇ ਭਵਿੱਖਬਾਣੀ ਟੈਕਸਟ ਵਰਗੀਆਂ ਹੋਸ਼ਿਆਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਕੇ ਆਮ ਤੌਰ 'ਤੇ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਨੂੰ ਬਿਹਤਰ ਕਰ ਸਕਦਾ ਹੈ।
Example: Siri ਅਤੇ Google Assistant ਵਰਗੇ ਵਰਚੁਅਲ ਸਹਾਇਕ ਆਵਾਜ਼ ਕਮਾਂਡ ਨੂੰ ਸਮਝਣ ਅਤੇ ਜਵਾਬ ਦੇਣ ਲਈ ਏਆਈ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਉਪਭੋਗਤਾਂ ਲਈ ਉਨ੍ਹਾਂ ਦੇ ਡਿਵਾਈਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨਾ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ।

### ਇਹ ਸਭ ਚੰਗਾ ਲੱਗਦਾ ਹੈ, ਤਾਂ ਫਿਰ ਸanu AEਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਲੋੜ ਕਿਉਂ ਹੈ?

ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕ ਸਿਰਫ਼ ਆਮ ਏਆਈ ਫਰੇਮਵਰਕਾਂ ਤੋਂ ਵੱਧ ਕੁਝ ਹਨ। ਇਹ ਹੋਸ਼ਿਆਰ ਏਜੰਟਾਂ ਦੀ ਰਚਨਾ ਯੋਗ ਬਣਾਉਣ ਲਈ ਡਿਜ਼ਾਇਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਜੋ ਉਪਭੋਗਤਾਂ, ਹੋਰ ਏਜੰਟਾਂ ਅਤੇ ਵਾਤਾਵਰਨ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਕੇ ਨਿਰਧਾਰਤ ਲੱਕੜਾਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ। ਇਹ ਏਜੰਟ ਸੁਤੰਤਰ ਵਿਹਾਰ ਦਿਖਾ ਸਕਦੇ ਹਨ, ਫੈਸਲੇ ਲੈ ਸਕਦੇ ਹਨ, ਅਤੇ ਬਦਲਦੀਆਂ ਸ਼ਰਤਾਂ ਅਨੁਸਾਰ ਢਲ ਸਕਦੇ ਹਨ। ਆਓ ਕੁਝ ਮੁੱਖ ਸਮਰੱਥਾਵਾਂ ਵੇਖੀਏ ਜੋ ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਦੁਆਰਾ ਸੰਭਵ ਹੋਂਦੀਆਂ ਹਨ:

- **ਏਜੰਟ ਸਹਿਯੋਗ ਅਤੇ ਤੇਤੰਤਰਤਾ**: ਕਈ ਏਜੰਟ ਬਣਾਉਣਾ ਜੋ ਇਕੱਠੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ, ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਜਟਿਲ ਕਾਰਜਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਸਮਨਵੀ ਕਰ ਸਕਦੇ ਹਨ।
- **ਕਾਰਜ ਸਵਚਾਲਨ ਅਤੇ ਪ੍ਰਬੰਧਨ**: ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋਜ਼, ਕਾਰਜ ਸੌਪਣਾ, ਅਤੇ ਏਜੰਟਾਂ ਵਿੱਚ ਗਤੀਸ਼ੀਲ ਕਾਰਜ ਪ੍ਰਬੰਧਨ ਲਈ ਯੰਤਰ ਮੁਹੱਈਆ ਕਰਨਾ।
- **ਸੰਦੇਭਜਨ ਸਮਝਦਾਰੀ ਅਤੇ ਅਨੁਕੂਲਤਾ**: ਏਜੰਟਾਂ ਨੂੰ ਸੰਦਰਭ ਸਮਝਣ, ਬਦਲਦੇ ਵਾਤਾਵਰਨ ਦੇ ਅਨੁਕੂਲ ਹੋਣ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਜਾਣਕਾਰੀ ਆਧਾਰ 'ਤੇ ਫੈਸਲਿਆਂ ਬਣਾਉਣ ਦੇ ਯੋਗ ਬਣਾਉਣਾ।

ਸੰਖੇਪ ਵਿੱਚ, ਏਜੰਟ ਤੁਹਾਨੂੰ ਹੋਰ ਬਹੁਤ ਕੁਝ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ — ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਇੱਕ ਨਵੇਂ ਪੱਧਰ 'ਤੇ ਲੈ ਜਾਣਾ, ਹੋਰ ਹੋਸ਼ਿਆਰ ਸਿਸਟਮ ਬਣਾਉਣਾ ਜੋ ਆਪਣੇ ਵਾਤਾਵਰਨ ਤੋਂ ਢਲਦੇ ਅਤੇ ਸਿੱਖਦੇ ਹਨ।

## ਏਜੰਟ ਦੀ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ, ਦੁਹਰਾਉਂ ਅਤੇ ਸੁਧਾਰ ਕਿਵੇਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ?

ਇਹ ਖੇਤਰ ਤੇਜ਼ੀ ਨਾਲ ਬਦਲ ਰਿਹਾ ਹੈ, ਪਰ ਬਹੁਤ ਸਾਰੇ ਏਆਈ ਏਜੰਟ ਫਰੇਮਵਰਕਾਂ ਵਿੱਚ ਕੁਝ ਆਮ ਚੀਜ਼ਾਂ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਅਤੇ ਦੁਹਰਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀਆਂ ਹਨ — ਜਿਵੇਂ ਮੋਡੀਊਲਰ ਕੰਪੋਨੈਂਟ, ਸਹਿਯੋਗੀ ਟੂਲ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਸਿੱਖਿਆ. ਆਓ ਇਨ੍ਹਾਂ ਨੂੰ ਵੇਖੀਏ:

- **ਮੋਡੀਊਲਰ ਕੰਪੋਨੈਂਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ**: ਏਆਈ SDKs ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਕੰਪੋਨੈਂਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਵੇਂ AI ਅਤੇ ਮੈਮੋਰੀ ਕਨੈਕਟਰ, ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਪ੍ਰਕਿਰਿਆਵਾਂ ਲਈ ਨੈਚਰਲ ਲੈਂਗਵੇਜ ਜਾਂ ਕੋਡ ਪਲੱਗਇਨਾਂ, ਪ੍ਰੋੰਪਟ ਟੈਂਪਲੇਟ ਆਦਿ।
- **ਸਹਿਯੋਗੀ ਟੂਲਾਂ ਤੋਂ ਲਾਭ ਉਠਾਓ**: ਨਿਰਧਾਰਿਤ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਕਾਰਜਾਂ ਨਾਲ ਏਜੰਟ ਡਿਜ਼ਾਇਨ ਕਰੋ, ਤਾਂ ਜੋ ਉਹ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਦੀ ਜਾਂਚ ਅਤੇ ਸੁਧਾਰ ਕਰ ਸਕਣ।
- **ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਿੱਖੋ**: ਫੀਡਬੈੱਕ ਲੂਪ ਲਾਗੂ ਕਰੋ ਜਿੱਥੇ ਏਜੰਟ ਇੰਟਰੈਕਸ਼ਨਾਂ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣਾ ਵਿਹਾਰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਢਾਲਦੇ ਹਨ।

### ਮੋਡੀਊਲਰ ਕੰਪੋਨੈਂਟ ਦੀ ਵਰਤੋਂ

Microsoft Agent Framework ਵਰਗੇ SDKs ਐਸੇ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਕੰਪੋਨੈਂਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਵੇਂ AI ਕਨੈਕਟਰ, ਟੂਲ ਪਰਿਭਾਸ਼ਾਵਾਂ, ਅਤੇ ਏਜੰਟ ਪ੍ਰਬੰਧਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਤੁਰੰਤ ਇਹ ਕੰਪੋਨੈਂਟ ਜੋੜ ਕੇ ਇੱਕ ਕਾਰਗਰ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉ ਸਕਦੀਆਂ ਹਨ ਬਿਨਾਂ ਸ਼ੁਰੂ ਤੋਂ ਬਣਾਉਣ ਦੇ, ਜਿਸ ਨਾਲ ਤਜਰਬਾ ਤੇ ਦੁਹਰਾਉਣ ਤੇਜ਼ ਹੁੰਦਾ ਹੈ।

**ਅਮਲ ਵਿੱਚ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਜਾਣਕਾਰੀ ਖਿੱਚਣ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ, ਡੇਟਾ ਸਟੋਰ ਅਤੇ ਰੀਟਰੀਵਲ ਲਈ ਮੈਮੋਰੀ ਮਾਡਿਊਲ, ਅਤੇ ਉਪਭੋਗਤਾਂ ਨਾਲ ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਪ੍ਰੋੰਪਟ ਜਨਰੇਟਰ, ਇਹ ਸਾਰੀਆਂ ਚੀਜ਼ਾਂ ਬਿਨਾਂ ਜ਼ੈਰੋ ਤੋਂ ਬਣਾਉਣ ਦੇ।

**Example code**. ਆਓ ਵੇਖੀਏ ਕਿ ਕਿੱਵੇਂ ਤੁਸੀਂ `AzureAIProjectAgentProvider` ਨਾਲ Microsoft Agent Framework ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਮਾਡਲ ਯੂਜ਼ਰ ਇਨਪੁਟ ਦਾ ਜਵਾਬ ਟੂਲ ਕਾਲਿੰਗ ਨਾਲ ਦੇਵੇ:

``` python
# ਮਾਈਕ੍ਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਪਾਇਥਨ ਉਦਾਹਰਨ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ਯਾਤਰਾ ਬੁੱਕ ਕਰਨ ਲਈ ਇੱਕ ਨਮੂਨਾ ਟੂਲ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ਉਦਾਹਰਨ ਨਤੀਜਾ: ਤੁਹਾਡੀ 1 ਜਨਵਰੀ 2025 ਨੂੰ ਨਿਊਯਾਰਕ ਜਾਣ ਵਾਲੀ ਉਡਾਣ ਸਫਲਤਾਪੂਰਵਕ ਬੁੱਕ ਹੋ ਗਈ ਹੈ। ਸੁਰੱਖਿਅਤ ਯਾਤਰਾ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ਤੁਸੀਂ ਇਸ ਉਦਾਹਰਨ ਤੋਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਯੂਜ਼ਰ ਇਨਪੁਟ ਤੋਂ ਮੂਲ ਜਾਣਕਾਰੀ ਨਿਕਾਲਣ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਪਾਰਸਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਉਤਪੱਤੀ, ਮੰਜ਼ਿਲ, ਅਤੇ ਤਾਰੀਖ ਫਲਾਈਟ ਬੁਕਿੰਗ ਬੇਨਤੀ ਲਈ। ਇਹ ਮੋਡੀਊਲਰ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਉੱਚ-ਸਤਹ ਲੋਜਿਕ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

### ਸਹਿਯੋਗੀ ਟੂਲਾਂ ਤੋਂ ਲਾਭ ਉਠਾਓ

Microsoft Agent Framework ਵਰਗੇ ਫਰੇਮਵਰਕ ਕਈ ਏਜੰਟ ਬਣਾਉਣ ਦੀ ਸਹੂਲਤ ਦਿੰਦے ਹਨ ਜੋ ਇਕੱਠੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਕਾਰਜਾਂ ਵਾਲੇ ਏਜੰਟ ਡਿਜ਼ਾਇਨ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਤਾਂ ਜੋ ਉਹ ਸਹਿਯੋਗੀ ਵਰਕਫਲੋਜ਼ ਦੀ ਜਾਂਚ ਅਤੇ ਸੂਧਾਰ ਕਰ ਸਕਣ ਅਤੇ ਸਮੁੱਚੇ ਸਿਸਟਮ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ ਬਿਹਤਰ ਕਰ ਸਕਣ।

**ਅਮਲ ਵਿੱਚ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਤੁਸੀਂ ਏਜੰਟਾਂ ਦੀ ਇੱਕ ਟੀਮ ਬਣਾਉ ਸਕਦੇ ਹੋ ਜਿੱਥੇ ਹਰ ਏਜੰਟ ਦੀ ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾ ਹੋਵੇ, ਜਿਵੇਂ ਡੇਟਾ ਰੀਟਰੀਵਲ, ਵਿਸ਼ਲੇਸ਼ਣ, ਜਾਂ ਫੈਸਲਾ-ਲੇਣਾ। ਇਹ ਏਜੰਟ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਸਾਂਝੀ ਜਾਣਕਾਰੀ ਸਾਂਝੀ ਕਰਕੇ ਇੱਕ ਸਾਂਝੇ ਲਕੜ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਇੱਕ ਯੂਜ਼ਰ ਸਵਾਲ ਦਾ ਜਵਾਬ ਦੇਣਾ ਜਾਂ ਕੋਈ ਕਾਰਜ ਪੂਰਾ ਕਰਨਾ।

**Example code (Microsoft Agent Framework)**:

```python
# ਮਾਇਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਈ ਏਜੰਟ ਬਣਾਉਣਾ ਜੋ ਮਿਲਕੇ ਕੰਮ ਕਰਦੇ ਹਨ

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ਡਾਟਾ ਪ੍ਰਾਪਤੀ ਏਜੰਟ
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਏਜੰਟ
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ਕਿਸੇ ਕਾਰਜ ਉੱਤੇ ਐਜੰਟਾਂ ਨੂੰ ਕ੍ਰਮ ਵਿੱਚ ਚਲਾਉਣਾ
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਕਿਵੇਂ ਤੁਸੀਂ ਡੇਟਾ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ ਕਈ ਏਜੰਟਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਕੇ ਇੱਕ ਕਾਰਜ ਬਣਾਂਦੇ ਹੋ। ਹਰ ਏਜੰਟ ਇੱਕ ਨਿਰਧਾਰਿਤ ਫੰਕਸ਼ਨ ਕਰਦਾ ਹੈ, ਅਤੇ ਕਾਰਜ ਉਹਨਾਂ ਏਜੰਟਾਂ ਦੀ ਸਹਿਕਾਰਤਾ ਰਾਹੀਂ ਨਿਰਵਾਹ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਵਿਸ਼ੇਸ਼ ਭੂਮਿਕਾਵਾਂ ਵਾਲੇ ਨਿਰਧਾਰਿਤ ਏਜੰਟਾਂ ਨੂੰ ਬਣਾਕੇ, ਤੁਸੀਂ ਕਾਰਜ ਦੀ ਕੁਸ਼ਲਤਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਸੁਧਾਰ ਸਕਦੇ ਹੋ।

### ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਿੱਖੋ

ਉੱਨਤ ਫਰੇਮਵਰਕ ਰੀਅਲ-ਟਾਈਮ ਸੰਦਰਭ ਸਮਝਦਾਰੀ ਅਤੇ ਅਨੁਕੂਲਤਾ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਟੀਮਾਂ ਇਹਨਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੀਆਂ ਹਨ**: ਟੀਮਾਂ ਐਸੇ ਫੀਡਬੈਕ ਲੂਪ ਲਾਗੂ ਕਰ ਸਕਦੀਆਂ ਹਨ ਜਿੱਥੇ ਏਜੰਟ ਇੰਟਰੈਕਸ਼ਨਾਂ ਤੋਂ ਸਿੱਖਦੇ ਹਨ ਅਤੇ ਆਪਣਾ ਵਿਹਾਰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਢਾਲਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਸਮਰੱਥਾਵਾਂ ਦੀ ਲਗਾਤਾਰ ਸੁਧਾਰ ਅਤੇ ਕੌਸ਼ਲਤਾ ਹੁੰਦੀ ਹੈ।

**ਅਮਲ ਵਿੱਚ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ**: ਏਜੰਟ ਯੂਜ਼ਰ ਫੀਡਬੈਕ, ਬਾਹਰੀ ਡેટਾ ਅਤੇ ਕਾਰਜ ਨਤੀਜਿਆਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਆਪਣਾ ਗਿਆਨ ਅਧਾਰ ਅੱਪਡੇਟ ਕਰ ਸਕਦੇ ਹਨ, ਫੈਸਲਾ-ਲੈਣ ਦੀਆਂ алгоритਮਾਂ ਨੂੰ ਐਡਜਸਟ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਸਮੇਂ ਨਾਲ ਪ੍ਰਦਰਸ਼ਨ ਸੁਧਾਰ ਸਕਦੇ ਹਨ। ਇਹ ਦੁਹਰਾਉਣਯੋਗ ਸਿੱਖਣ ਵਾਲੀ ਪ੍ਰਕਿਰਿਆ ਏਜੰਟਾਂ ਨੂੰ ਬਦਲਦੀਆਂ ਸ਼ਰਤਾਂ ਅਤੇ ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਦੇ ਅਨੁਕੂਲ ਬਣਾਉਂਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਸਮੂਹਿਕ ਸਿਸਟਮ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਵਧਦੀ ਹੈ।

## Microsoft Agent Framework ਅਤੇ Azure AI Agent Service ਵਿੱਚ ਕੀ ਫਰਕ ਹਨ?

ਇਨ੍ਹਾਂ ਦ੍ਰਿਸ਼ਟਿਕੋਣਾਂ ਨੂੰ ਤੁਲਨਾ ਕਰਨ ਦੇ ਕਈ ਤਰੀਕੇ ਹਨ, ਪਰ ਆਓ ਉਨ੍ਹਾਂ ਦੀ ਡਿਜ਼ਾਈਨ, ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਲਕੜਾਂ ਦੇ ਅਨੁਸਾਰ ਕੁਝ ਮੁੱਖ ਫਰਕ ਵੇਖੀਏ:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ਇੱਕ ਸਧਾਰਨ SDK ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ `AzureAIProjectAgentProvider` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ Azure OpenAI ਮਾਡਲਾਂ ਨਾਲ ਟੂਲ ਕਾਲਿੰਗ, ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ ਅਤੇ Azure identity ਰਾਹੀਂ ਐਂਟਰਪ੍ਰਾਈਜ਼-ਗਰੇਡ ਸੁਰੱਖਿਆ ਦੇਣ ਵਾਲੇ ਏਜੰਟ ਬਣਾਉਣ ਯੋਗ ਕਰਦਾ ਹੈ।

**ਵਰਤੋਂ ਦੇ ਕੇਸ**: ਟੂਲ ਉਪਯੋਗ, ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋ ਅਤੇ ਏਂਟਰਪ੍ਰਾਈਜ਼ ਇੰਟੇਗ੍ਰੇਸ਼ਨ ਸਿਨਾਰਿਓਜ਼ ਲਈ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਏਆਈ ਏਜੰਟ ਬਣਾਉਣਾ।

ਇਹ ਰਹੇ Microsoft Agent Framework ਦੇ ਕੁਝ ਮਹੱਤਵਪੂਰਨ ਮੁੱਖ ਸੰਕਲਪ:

- **ਏਜੰਟ**. ਇੱਕ ਏਜੰਟ `AzureAIProjectAgentProvider` ਰਾਹੀਂ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇੱਕ ਨਾਮ, ਹਦਾਇਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਕਨਫਿਗਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਏਜੰਟ ਇਹ ਕਰ ਸਕਦਾ ਹੈ:
  - **ਯੂਜ਼ਰ ਸੁਨੇਹਿਆਂ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨਾ** ਅਤੇ Azure OpenAI ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ।
  - **ਸੰਵਾਦ ਦੇ ਸੰਦਰਭ ਅਨੁਸਾਰ ਟੂਲਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਾਲ ਕਰਨਾ**।
  - **ਕਈ ਇੰਟਰੈਕਸ਼ਨਾਂ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦੀ ਸਥਿਤੀ ਬਣਾਈ ਰੱਖਣਾ**।

  ਹੇਠਾਂ ਇੱਕ ਕੋਡ ਟੁਕੜਾ ਦਿੱਤਾ ਗਿਆ ਹੈ ਜੋ ਏਜੰਟ ਬਣਾਉਣ ਵਿਖਾਉਂਦਾ ਹੈ:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ਟੂਲ**. ਫਰੇਮਵਰਕ ਟੂਲਾਂ ਨੂੰ Python ਫੰਕਸ਼ਨਾਂ ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੰਦਾ ਹੈ ਜੋ ਏਜੰਟ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਬੁਲਾ ਸਕਦਾ ਹੈ। ਟੂਲਾਂ ਨੂੰ ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਰਜਿਸਟਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ਮਲਟੀ-ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ**. ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਾਲੇ ਕਈ ਏਜੰਟ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਕੰਮ ਨੂੰ ਕੋਆਰਡੀਨেট ਕਰ ਸਕਦੇ ਹੋ:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity ਇਨਟੀਗਰੇਸ਼ਨ**. ਫਰੇਮਵਰਕ `AzureCliCredential` (ਜਾਂ `DefaultAzureCredential`) ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਸੁਰੱਖਿਅਤ, ਬਿਨਾਂ ਕੀ-ਕੇ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ, ਜਿਸ ਨਾਲ API ਕੀਜ਼ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ ਜ਼ਰੂਰੀ ਨਹੀਂ ਰਹਿੰਦਾ।

## Azure AI Agent Service

Azure AI Agent Service Microsoft Ignite 2024 'ਚ ਪਹਿਲਾਂ ਪੇਸ਼ ਕੀਤੀ ਗਈ ਇਕ ਨਵੀਨਤਮ ਸੇਵਾ ਹੈ। ਇਹ ਜ਼ਿਆਦਾ ਲਚਕੀਲੇ ਮਾਡਲਾਂ ਦੇ ਨਾਲ ਏਜੰਟ ਵਿਕਾਸ ਅਤੇ ਤੈਨਾਤੀ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ, ਜਿਵੇਂ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਦੇ LLMs ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰਨਾ (ਜਿਵੇਂ Llama 3, Mistral, ਅਤੇ Cohere)।

Azure AI Agent Service ਔਰ ਧਿਰ-ਵਧੀਏ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ ਮਕੈਨਿਜ਼ਮ ਅਤੇ ਡੇਟਾ ਸਟੋਰੇਜ ਮੈਥਡਸ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਪਯੋਗੀ ਬਣਦੀ ਹੈ।

ਇਹ Microsoft Agent Framework ਨਾਲ ਬਾਹਰੋਂ-ਦੇ-ਬਾਕਸ ਕੰਮ ਕਰਦੀ ਹੈ ਤਾਂ ਜੋ ਏਜੰਟ ਬਣਾਉਣ ਅਤੇ ਤੈਨਾਤ ਕਰਨ ਦੇ ਕੰਮ ਆਸਾਨ ਹੋ ਜਾਣ।

ਇਹ ਸੇਵਾ ਇਸ ਸਮੇਂ Public Preview ਵਿੱਚ ਹੈ ਅਤੇ ਏਜੰਟ ਬਿਲਡ ਕਰਨ ਲਈ Python ਅਤੇ C# ਦਾ ਸਮਰਥਨ ਦਿੰਦੀ ਹੈ।

Azure AI Agent Service Python SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਸੀਂ ਇੱਕ ਯੂਜ਼ਰ-Defined ਟੂਲ ਨਾਲ ਏਜੰਟ ਬਣਾਉ ਸਕਦੇ ਹਾਂ:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ਟੂਲ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
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
        model="gpt-4o-mini",
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

### ਮੁੱਖ ਸੰਕਲਪ

Azure AI Agent Service ਦੇ ਹੇਠਾਂ ਇਹ ਮੁੱਖ ਸੰਕਲਪ ਹਨ:

- **Agent**. Azure AI Agent Service Microsoft Foundry ਨਾਲ ਇਕੀਕ੍ਰਿਤ ਹੁੰਦੀ ਹੈ। AI Foundry ਦੇ ਅੰਦਰ, ਇੱਕ AI Agent ਇੱਕ "ਸਮਾਰਟ" ਮਾਇਕ੍ਰੋਸੇਵਾ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜਿਸ ਦਾ ਉਪਯੋਗ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ (RAG), ਕਾਰਵਾਈ ਕਰਨ ਜਾਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਵਰਕਫਲੋਜ਼ ਆਟੋਮੇਟ ਕਰਨ ਲਈ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਜਨਰੇਟਿਵ ਏਆਈ ਮਾਡਲਾਂ ਦੀ ਸ਼ਕਤੀ ਨੂੰ ਉਹਨਾਂ ਟੂਲਾਂ ਨਾਲ ਮਿਲਾ ਕੇ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਜੋ ਇਸ ਨੂੰ ਅਸਲ-ਦੁਨੀਆ ਦੇ ਡੇਟਾ ਸੌਰਸਾਂ ਤੱਕ ਪਹੁੰਚ ਅਤੇ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀਆਂ ਹਨ। ਹੇਠਾਂ ਏਜੰਟ ਦਾ ਇੱਕ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਇੱਕ ਏਜੰਟ `gpt-4o-mini` ਮਾਡਲ ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਨਾਮ `my-agent`, ਅਤੇ ਹਦਾਇਤਾਂ `You are helpful agent`। ਏਜੰਟ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟੇਸ਼ਨ ਕਾਰਜ ਕਰਨ ਲਈ ਟੂਲ ਅਤੇ ਸਰੋਤਾਂ ਨਾਲ ਲੈਸ ਕੀਤਾ ਗਿਆ ਹੈ।

- **ਥ੍ਰੇਡ ਅਤੇ ਸੁਨੇਹੇ**. ਥ੍ਰੇਡ ਇੱਕ ਹੋਰ ਮਹੱਤਵਪੂਰਨ ਸੰਕਲਪ ਹੈ। ਇਹ ਏਜੰਟ ਅਤੇ ਯੂਜ਼ਰ ਦਰਮਿਆਨ ਗੱਲਬਾਤ ਜਾਂ ਇੰਟਰੈਕਸ਼ਨ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਥ੍ਰੇਡਾਂ ਨੂੰ ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ, ਸੰਦਰਭ ਜਾਣਕਾਰੀ ਸਟੋਰ ਕਰਨ ਅਤੇ ਇੰਟਰੈਕਸ਼ਨ ਦੀ ਸਥਿਤੀ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਹੇਠਾਂ ਥ੍ਰੇਡ ਦੀ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ, ਇੱਕ ਥ੍ਰੇਡ ਬਣਾਈ ਗਈ। ਇਸ ਤੋਂ ਬਾਅਦ, ਥ੍ਰੇਡ ਨੂੰ ਇੱਕ ਸੁਨੇਹਾ ਭੇਜਿਆ ਗਿਆ। `create_and_process_run` ਨੂੰ ਕਾਲ ਕਰਕੇ, ਏਜੰਟ ਨੂੰ ਥ੍ਰੇਡ 'ਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕਿਹਾ ਗਿਆ। ਆਖਿਰਕਾਰ, ਸੁਨੇਹਿਆਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕੀਤਾ ਅਤੇ ਲੌਗ ਕੀਤਾ ਗਿਆ ਤਾਂ ਜੋ ਏਜੰਟ ਦੇ ਜਵਾਬ ਨੂੰ ਦੇਖਿਆ ਜਾ ਸਕੇ। ਸੁਨੇਹੇ ਗੱਲਬਾਤ ਦੀ ਪ੍ਰਗਤੀ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ ਜੋ ਯੂਜ਼ਰ ਅਤੇ ਏਜੰਟ ਵਿਚਕਾਰ ਹੋਈ ਹੈ। ਇਹ ਵੀ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਸੁਨੇਹੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਹੋ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਟੈਕਸਟ, ਚਿੱਤਰ ਜਾਂ ਫ਼ਾਇਲ; ਉਦਾਹਰਨ ਲਈ ਏਜੰਟ ਦਾ ਕੰਮ ਇੱਕ ਚਿੱਤਰ ਜਾਂ ਟੈਕਸਟ ਜਵਾਬ ਦੇ ਰੂਪ ਵਿੱਚ ਨਤੀਜਾ ਦੇ ਸਕਦਾ ਹੈ। ਇੱਕ ਡਿਵੈਲਪਰ ਵਜੋਂ, ਤੁਸੀਂ ਫਿਰ ਇਸ ਜਾਣਕਾਰੀ ਦਾ ਉਪਯੋਗ ਜਵਾਬ ਨੂੰ ਅੱਗੇ ਪ੍ਰੋਸੈਸ ਕਰਨ ਜਾਂ ਉਪਭੋਗਤਾ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਕਰ ਸਕਦੇ ਹੋ।

- **Microsoft Agent Framework ਨਾਲ ਇੱਕੀਕ੍ਰਿਤ**. Azure AI Agent Service Microsoft Agent Framework ਨਾਲ ਰਾਹਤ ਨਾਲ ਕੰਮ ਕਰਦੀ ਹੈ, ਜਿਸ ਦਾ ਅਰਥ ਹੈ ਕਿ ਤੁਸੀਂ `AzureAIProjectAgentProvider` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਬਣਾਉ ਸਕਦੇ ਹੋ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਪ੍ਰੋਡਕਸ਼ਨ ਹਾਲਾਤਾਂ ਲਈ Agent Service ਰਾਹੀਂ ਤੈਨਾਤ ਕਰ ਸਕਦੇ ਹੋ।

**ਵਰਤੋਂ ਦੇ ਕੇਸ**: Azure AI Agent Service ਐਂਟਰਪ੍ਰਾਈਜ਼ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ ਅਤੇ ਲਚਕੀਲਾ ਏਆਈ ਏਜੰਟ ਤੈਨਾਤੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

## ਇਹਨਾਂ ਦ੍ਰਿਸ਼ਟਿਕੋਣਾਂ ਵਿਚਕਾਰ ਕੀ ਫਰਕ ਹੈ?

ਇਹ ਲੱਗਦਾ ਹੈ ਕਿ ਓਵਰਲੈਪ ਹੈ, ਪਰ ਡਿਜ਼ਾਈਨ, ਸਮਰੱਥਾ ਅਤੇ ਲਕੜਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਕੁਝ ਮੁੱਖ ਫਰਕ ਹਨ:

- **Microsoft Agent Framework (MAF)**: ਏਜੰਟਾਂ ਬਣਾਉਣ ਲਈ ਇੱਕ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ SDK ਹੈ। ਇਹ ਟੂਲ ਕਾਲਿੰਗ, ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ, ਅਤੇ Azure identity ਇਨਟੀਗਰੇਸ਼ਨ ਨਾਲ ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸਧਾਰਨ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- **Azure AI Agent Service**: Agents ਲਈ Azure Foundry ਵਿੱਚ ਇੱਕ ਪਲੇਟਫਾਰਮ ਅਤੇ ਤੈਨਾਤੀ ਸੇਵਾ ਹੈ। ਇਹ Azure OpenAI, Azure AI Search, Bing Search ਅਤੇ ਕੋਡ ਐਕਜ਼ਿਕਿਊਸ਼ਨ ਵਰਗੀਆਂ ਸੇਵਾਵਾਂ ਨਾਲ ਬਣਿਆ ਹੋਇਆ ਕਨੈਕਟੀਵੀਟੀ ਦਿੰਦੀ ਹੈ।

ਅਜੇ ਵੀ ਪਖੰਡੀ ਹੋ? ਕਿਹੜਾ ਚੁਣਣਾ ਹੈ ਐ ਨਿਰਣੈ ਨਹੀਂ ਹੋ ਰਿਹਾ?

### ਵਰਤੋਂ ਦੇ ਕੇਸ

ਆਓ ਕੁਝ ਆਮ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ 'ਤੇ ਜਾਣ ਕੇ ਤੁਹਾਡੀ ਮਦਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ:

> Q: ਮੈਂ ਪ੍ਰੋਡਕਸ਼ਨ ਏਆਈ ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾ ਰਿਹਾ/ਰਹੀ ਹਾਂ ਅਤੇ ਤੁਰੰਤ ਸ਼ੁਰੂ ਕਰਨਾ ਚਾਹੁੰਦਾ/ਚਾਹੁੰਦੀ ਹਾਂ
>

> A: Microsoft Agent Framework ਇੱਕ ਬਹੁਤ ਵਧੀਆ ਚੋਣ ਹੈ। ਇਹ `AzureAIProjectAgentProvider` ਰਾਹੀਂ ਇੱਕ ਸਧਾਰਨ, Python-ਮੈਤਰਿਕ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਕੁਝ ਹੀ ਲਾਈਨਾਂ ਕੋਡ ਵਿੱਚ ਟੂਲ ਅਤੇ ਹਦਾਇਤਾਂ ਨਾਲ ਏਜੰਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

>Q: ਮੈਨੂੰ ਐਂਟਰਪ੍ਰਾਈਜ਼-ਗਰੇਡ ਤੈਨਾਤੀ ਚਾਹੀਦੀ ਹੈ ਜਿਸ ਵਿੱਚ Azure ਇੰਟੀਗ੍ਰੇਸ਼ਨਾਂ ਜਿਵੇਂ Search ਅਤੇ ਕੋਡ ਐਕਜ਼ਿਕਿਊਸ਼ਨ ਹੋਣ
>
> A: Azure AI Agent Service ਸਭ ਤੋਂ ਵਧੀਆ ਫਿੱਟ ਹੈ। ਇਹ ਇੱਕ ਪਲੇਟਫਾਰਮ ਸੇਵਾ ਹੈ ਜੋ ਕਈ ਮਾਡਲਾਂ, Azure AI Search, Bing Search ਅਤੇ Azure Functions ਲਈ ਬਿਲਟ-ਇਨ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਹ Foundry ਪੋਰਟਲ ਵਿੱਚ ਤੁਹਾਡੇ ਏਜੰਟ ਬਣਾਉਣਾ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਸਕੇਲ 'ਤੇ ਤੈਨਾਤ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦਾ ਹੈ।
 
> Q: ਮੈਂ ਅਜੇ ਵੀ ਗੁੰਝਲਤ ਹਾਂ, ਸਿਰਫ ਇੱਕ ਚੋਣ ਦਿਓ
>
> A: Microsoft Agent Framework ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟਾਂ ਦਾ ਵਿਕਾਸ ਕਰ ਸਕੋ, ਅਤੇ ਜਦੋਂ ਤੁਹਾਨੂੰ ਉਨ੍ਹਾਂ ਨੂੰ ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਤੈਨਾਤ ਅਤੇ ਸਕੇਲ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇ ਤਦ Azure AI Agent Service ਵਰਤੋ। ਇਹ ਪਹੁੰਚ ਤੁਹਾਨੂੰ ਏਜੰਟ ਲੋਜਿਕ 'ਤੇ ਤੇਜ਼ੀ ਨਾਲ ਦੁਹਰਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਅਤੇ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਤੈਨਾਤੀ ਲਈ ਇੱਕ ਸਾਫ ਰਸਤਾ ਦਿੰਦੀ ਹੈ।

ਚਲੋ ਮੁੱਖ ਫਰਕਾਂ ਨੂੰ ਇੱਕ ਸਾਰਣੀ ਵਿੱਚ ਸੰਖੇਪ ਕਰੀਏ:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ਟੂਲ ਕਾਲਿੰਗ ਨਾਲ ਸਧਾਰਨ ਏਜੰਟ SDK | ਏਜੰਟ, ਟੂਲ, Azure Identity | ਏਆਈ ਏਜੰਟ ਬਣਾਉਣਾ, ਟੂਲ ਦੀ ਵਰਤੋਂ, ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋ |
| Azure AI Agent Service | ਲਚਕੀਲੇ ਮਾਡਲ, ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ, ਕੋਡ ਜਨਰੇਸ਼ਨ, ਟੂਲ ਕਾਲਿੰਗ | ਮੋਡੀਊਲਰਿਟੀ, ਸਹਿਯੋਗ, ਪ੍ਰਕਿਰਿਆ ਆਯੋਜਨ | ਸੁਰੱਖਿਅਤ, ਸਕੇਲਯੋਗ ਅਤੇ ਲਚਕੀਲਾ ਏਆਈ ਏਜੰਟ ਤੈਨਾਤੀ |

## ਕੀ ਮੈਂ ਆਪਣੇ ਮੌਜੂਦਾ Azure ਪਰਿਵਾਰਕ ਟੂਲਾਂ ਨੂੰ ਸਿੱਧਾ ਇਕੀਕ੍ਰਿਤ ਕਰ ਸਕਦਾ/ਸਕਦੀ ਹਾਂ, ਜਾਂ ਕੀ ਮੈਨੂੰ standalone ਹੱਲਾਂ ਦੀ ਲੋੜ ਹੈ?
The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, as it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Microsoft Foundry.

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## ਨਮੂਨਾ ਕੋਡ

- Python: [ਏਜੈਂਟ ਫ੍ਰੇਮਵਰਕ](./code_samples/02-python-agent-framework.ipynb)
- .NET: [ਏਜੈਂਟ ਫ੍ਰੇਮਵਰਕ](./code_samples/02-dotnet-agent-framework.md)

## AI ਏਜੈਂਟ ਫ੍ਰੇਮਵਰਕਸ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਲਰਨਰਾਂ ਨਾਲ ਮਿਲਣ, ਆਫਿਸ ਆਵਰਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣ ਅਤੇ ਆਪਣੇ AI ਏਜੰਟਸ ਦੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੈਣ ਲਈ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 'ਚ ਸ਼ਾਮਲ ਹੋਵੋ।

## ਸੰਦਰਭ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ਏਜੈਂਟ ਸਰਵਿਸ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI ਜਵਾਬ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ਏਜੈਂਟ ਸਰਵਿਸ</a>

## ਪਿਛਲਾ ਪਾਠ

[AI ਏਜੈਂਟਸ ਅਤੇ ਏਜੈਂਟ ਉਪਯੋਗ ਕੇਸਾਂ ਦਾ ਪਰਚਿਆ](../01-intro-to-ai-agents/README.md)

## ਅਗਲਾ ਪਾਠ

[ਏਜੈਂਟਿਕ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਸ ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਅਸਵੀਕਾਰਨ:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ Co-op Translator (https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸ਼ੁੱਧਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਦਸਤਾਵੇਜ਼ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਨਾਲ ਹੋਈਆਂ ਕਿਸੇ ਵੀ ਗਲਤ-ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->