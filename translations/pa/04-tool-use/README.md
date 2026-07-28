[![ਵਧੀਆ AI ਏਜੰਟ ਕਿਵੇਂ ਡਿਜ਼ਾਈਨ ਕਰੀਏ](../../../translated_images/pa/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਵੇਖਣ ਲਈ ਉੱਪਰ ਦਿਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ

ਟੂਲ ਸਧਾਰਨ ਨਹੀਂ ਹਾਂ ਕਿਉਂਕਿ ਇਹ AI ਏਜੰਟਾਂ ਨੂੰ ਵਿਆਪਕ ਸਮਰੱਥਾਵਾਂ ਦੁੰਦਵਾਉਂਦੇ ਹਨ। ਇਸ ਦੀ ਬਜਾਏ ਕਿ ਏਜੰਟ ਕੋਲ ਸਿਰਫ਼ ਕੁਝ ਥਾਪੇ ਕਰਦਾ ਹੈ, ਇੱਕ ਟੂਲ ਜੋੜ ਕੇ ਉਹ ਹੁਣ ਵੱਖ-ਵੱਖ ਕਾਰਜ ਕਰ ਸਕਦਾ ਹੈ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਤੇ ਚਰਚਾ ਕਰਾਂਗੇ, ਜੋ AI ਏਜੰਟਾਂ ਨੂੰ ਆਪਣੇ ਲਛਣਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਨਿਰਧਾਰਿਤ ਟੂਲਾਂ ਨੂੰ ਵਰਤਣ ਦੀ ਵਿਧੀ ਵੇਖਾਉਂਦਾ ਹੈ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੱਭ ਰਹੇ ਹਾਂ:

- ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?
- ਇਹ ਕਿਹੜੇ ਪਰੇਖੇ ਵਿੱਚ ਲਾਗੂ ਹੁੰਦਾ ਹੈ?
- ਇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਕਿਹੜੇ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕ ਲੋੜੀਂਦੇ ਹਨ?
- ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਵਰਤਣ ਬਾਰੇ ਖਾਸ ਧਿਆਨ ਕਿਹੜੇ ਹਨ?

## ਸਿੱਖਣ ਦੇ ਲੱਖਣ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਤੇ ਇਸ ਦਾ ਉਦੇਸ਼ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ।
- ਉਹ ਸਥਿਤੀਆਂ ਪਛਾਣਣ ਜਿੱਥੇ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
- ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਮੁੱਖ ਤੱਤ ਸਮਝਣਾ।
- ਇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਾਲੇ AI ਏਜੰਟਾਂ ਵਿੱਚ ਭਰੋਸੇਯੋਗਤਾ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਧਿਆਨਾਂ ਦੀ ਪਛਾਣ ਕਰਨਾ।

## ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?

**ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ** LLMs ਨੂੰ ਬਾਹਰੀ ਟੂਲਾਂ ਨਾਲ ਗੱਲ-ਬਾਤ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੰਦਾ ਹੈ ਤਾਂ ਜੋ ਵਿਸ਼ੇਸ਼ ਲਛਣਾਂ ਪ੍ਰਾਪਤ ਕੀਤੇ ਜਾ ਸਕਣ। ਟੂਲ ਇਕ ਕੋਡ ਹੁੰਦਾ ਹੈ ਜੋ ਏਜੰਟ ਵੱਲੋਂ ਕਾਰਜ ਕਰਨ ਲਈ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। ਇੱਕ ਟੂਲ ਸਧਾਰਨ ਫੰਕਸ਼ਨ ਜਿਵੇਂ ਕਿ ਕੈਲਕुलेਟਰ ਹੋ ਸਕਦਾ ਹੈ, ਜਾਂ ਕਿਸੇ ਤੀਜੇ ਪਾਸੇ ਲਘੂ ਸੇਵਾ ਲਈ API ਕਾਲ ਜਿਵੇਂ ਸ਼ੇਅਰ ਕੀਮਤ ਜਾਂ ਮੌਸਮ ਦੀ ਭਵਿੱਖਬਾਣੀ। AI ਏਜੰਟਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਟੂਲਾਂ ਨੂੰ ਐਜੰਟ ਵੱਲੋਂ **ਮਾਡਲ-ਜਨਰਲ ਫੰਕਸ਼ਨ ਕਾਲਾਂ** ਦੇ ਜਵਾਬ ਵਿੱਚ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ।

## ਇਹ ਕਿਹੜੇ ਪਰੇਖੇ ਵਿੱਚ ਲਾਗੂ ਹੁੰਦਾ ਹੈ?

AI ਏਜੰਟ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੁਸ਼ਕਿਲ ਕੰਮ ਮੁਕੰਮਲ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਂ ਫੈਸਲੇ ਲੈ ਸਕਦੇ ਹਨ। ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਕਸਰ ਐਸੇ ਸੰਦਰਭਾਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਜਿੱਥੇ ਬਾਹਰੀ ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਗਤੀਸ਼ੀਲ ਸੰਵਾਦ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ ਡੇਟਾਬੇਸ, ਵੈਬ ਸਰਵਿਸ, ਜਾਂ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ। ਇਹ ਸਮਰੱਥਾ ਕਈ ਕਿਸਮਾਂ ਦੇ ਪ੍ਰਯੋਗਾਂ ਲਈ ਲਾਭਕਾਰੀ ਹੈ ਜਿਵੇਂ:

- **ਗਤੀਸ਼ੀਲ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤੀ:** ਏਜੰਟ ਬਾਹਰੀ API ਜਾਂ ਡੇਟਾਬੇਸ ਤੋਂ ਤਾਜ਼ਾ ਡੇਟਾ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ (ਜਿਵੇਂ ਕਿ SQLite ਡੇਟਾਬੇਸ ਤੋਂ ਡਾਟਾ ਐਨਾਲਿਸਿਸ, ਸ਼ੇਅਰ ਕੀਮਤਾਂ ਜਾਂ ਮੌਸਮ ਦੀ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨਾ)।
- **ਕੋਡ ਚਲਾਉਣਾ ਅਤੇ ਵਿਵੇਚਨਾ:** ਏਜੰਟ ਕੋਡ ਜਾਂ ਸਕ੍ਰਿਪਟ ਚਲਾ ਕੇ ਗਣਿਤ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰ ਸਕਦੇ ਹਨ, ਰਿਪੋਰਟ ਬਣਾ ਸਕਦੇ ਹਨ ਜਾਂ ਸਿਮੂਲੇਸ਼ਨ ਕਰ ਸਕਦੇ ਹਨ।
- **ਕਾਰਜ ਪ੍ਰਵਾਹ ਆਟੋਮੇਸ਼ਨ:** ਟਾਸਕ ਸ਼ੈਡਿਊਲਰ, ਈਮੇਲ ਸੇਵਾਵਾਂ, ਜਾਂ ਡੇਟਾ ਪਾਈਪਲਾਈਨ ਲਈ ਟੂਲਾਂ ਨੂੰ ਜੋੜਕੇ ਦੁਹਰਾਉਣ ਵਾਲੇ ਜਾਂ ਕਈ ਕਦਮਾਂ ਵਾਲੇ ਕਾਰਜਾਂ ਦਾ ਆਟੋਮੇਸ਼ਨ।
- **ਗਾਹਕ ਸਹਾਇਤਾ:** ਏਜੰਟ CRM ਪ੍ਰਣਾਲੀ, ਟਿਕਟਿੰਗ ਪਲੇਟਫਾਰਮ ਜਾਂ ਗਿਆਨ ਬੇਸ ਨਾਲ ਸੰਵਾਦ ਕਰ ਕੇ ਯੂਜ਼ਰ ਦੀਆਂ ਪੁੱਛਾਂ ਨੂੰ ਹੱਲ ਕਰ ਸਕਦੇ ਹਨ।
- **ਸਮੱਗਰੀ ਪੈਦਾਵਾਰ ਅਤੇ ਸੰਪਾਦਨ:** ਏਜੰਟ ਵਿਅਾਕਰਨ ਚੈੱਕਰ, ਲਿਖਤ ਸੰਖੇਪਕਾਰ, ਜਾਂ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਮੂਲਿਆਂਕਣ ਵਰਗੇ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮੱਗਰੀ ਬਣਾਉਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰ ਸਕਦੇ ਹਨ।

## ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰਨ ਲਈ ਕਿਹੜੇ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕ ਲੋੜੀਂਦੇ ਹਨ?

ਇਹ ਬਿਲਡਿੰਗ ਬਲਾਕ AI ਏਜੰਟ ਨੂੰ ਵਿਆਪਕ ਕਾਰਜ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ। ਆਓ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਮੁੱਖ ਤੱਤਾਂ ਨੂੰ ਵੇਖੀਏ:

- **ਫੰਕਸ਼ਨ/ਟੂਲ ਸਕੀਮਾਂ**: ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਵਿਸਥਾਰਿਤ ਪਰਿਭਾਸ਼ਾ, ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ, ਉਦੇਸ਼, ਜ਼ਰੂਰੀ ਪੈਰਾਮੀਟਰ ਅਤੇ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਆਉਟਪੁੱਟ ਸ਼ਾਮਿਲ ਹੈ। ਇਹ ਸਕੀਮਾਂ LLM ਨੂੰ ਸਮਝਦਾਰ ਬੇਨਤੀ ਬਣਾਉਣ ਅਤੇ ਉਪਲਬਧ ਟੂਲਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦੀਆਂ ਹਨ।

- **ਫੰਕਸ਼ਨ ਚਲਾਉਣ ਦੀ ਤਰਕੀਬ**: ਵਰਤੋਂਕਾਰ ਦੀ ਇੱਛਾ ਅਤੇ ਗੱਲਬਾਤ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦਿਆਂ ਟੂਲਾਂ ਕਿਵੇਂ ਅਤੇ ਕਦੋਂ ਕਾਲ ਕੀਤੀਆਂ ਜਾਣਗੀਆਂ ਇਹ ਨਿਯੰਤ੍ਰਿਤ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਯੋਜਨਾ ਬਨਾਉਣ ਵਾਲਾ ਮੋਡੀਊਲ, ਮਾਰਗਦਰਸ਼ਨ ਮਕੈਨਿਜ਼ਮ ਜਾਂ ਸ਼ਰਤੀ ਪ੍ਰਵਾਹ ਸ਼ਾਮਿਲ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਟੂਲ ਦੀ ਵਰਤੋਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਬਣਾਉਂਦੇ ਹਨ।

- **ਸੰਦੇਸ਼ ਸੰਭਾਲਣ ਪ੍ਰਣਾਲੀ**: ਇਹ ਉਪਭੋਗਤਾ ਦੀਆਂ ਇਨਪੁੱਟ, LLM ਦੇ ਜਵਾਬ, ਟੂਲ ਕਾਲਾਂ ਅਤੇ ਟੂਲ ਦੇ ਨਤੀਜਿਆਂ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦੇ ਪ੍ਰਵਾਹ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ।

- **ਟੂਲ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਫਰੇਮਵਰਕ**: ਏਜੰਟ ਨੂੰ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲ ਜੋੜਨ ਲਈ ਢਾਂਚਾ, ਚਾਹੇ ਉਹ ਸਧਾਰਨ ਫੰਕਸ਼ਨ ਹੋਣ ਜਾਂ ਜਟਿਲ ਬਾਹਰੀ ਸੇਵਾਵਾਂ।

- **ਗਲਤੀਆਂ ਸੰਭਾਲਣਾ ਅਤੇ ਵੈਰੀਫ਼ਿਕੇਸ਼ਨ**: ਟੂਲ ਚਲਾਉਣ ਦੀਆਂ ਅਸਫਲਤਾਵਾਂ ਸੰਭਾਲਣ, ਪੈਰਾਮੀਟਰਾਂ ਦਾ ਜਾਇਜ਼ਾ ਲੈਣ ਅਤੇ ਅਣਮੁੜੇ ਜਵਾਬਾਂ ਨੂੰ ਮੈਨੇਜ ਕਰਨ ਦੀ ਪ੍ਰਣਾਲੀ।

- **ਸਟੇਟ ਮੈਨੇਜਮੈਂਟ**: ਗੱਲਬਾਤ ਦਾ ਸੰਦਰਭ, ਪਹਿਲਾਂ ਹੋਈਆਂ ਟੂਲ ਕਾਰਵਾਈਆਂ ਅਤੇ ਪੈਰਿਸਥਿਤਿਕ ਡੇਟਾ ਦਾ ਟ੍ਰੈਕ ਰੱਖਦਾ ਹੈ ਤਾਂ ਜੋ ਕਈ ਵਾਰੀ ਹੋਣ ਵਾਲੇ ਇੰਟਰੈਕਸ਼ਨਾਂ ਵਿੱਚ ਇਕਸਾਰਤਾ ਬਣੀ ਰਹੇ।

ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਹੌਲੀ ਜਿਹੀ ਛਾਨਬੀਨ ਕਰਾਂਗੇ ਫੰਕਸ਼ਨ/ਟੂਲ ਕਾਲਿੰਗ ਬਾਰੇ।
 
### ਫੰਕਸ਼ਨ/ਟੂਲ ਕਾਲਿੰਗ

ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨਾ ਪ੍ਰਮੁੱਖ ਢੰਗ ਹੈ ਜਿਸ ਨਾਲ ਅਸੀਂ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਨੂੰ ਟੂਲਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾ ਹੁੰਦੇ ਹਾਂ। ਤੁਸੀਂ ਅਕਸਰ 'ਫੰਕਸ਼ਨ' ਅਤੇ 'ਟੂਲ' ਨੂੰ ਬਦਲ ਕੇ ਵਰਤਦੇ ਵੇਖੋਗੇ ਕਿਉਂਕਿ 'ਫੰਕਸ਼ਨ' (ਡੁਬਾਰਾ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਕੋਡ ਦੇ ਹਿੱਸੇ) ਉਹ 'ਟੂਲ' ਹਨ ਜੋ ਏਜੰਟ ਕਾਰਜ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹਨ। ਕਿਸੇ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ, LLM ਨੂੰ ਵਰਤੋਂਕਾਰ ਦੀ ਬੇਨਤੀ ਨੂੰ ਉਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਣਨਾ ਨਾਲ ਤੁਲਨਾ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। ਇਸ ਲਈ ਹਰ ਉਪਲਬਧ ਫੰਕਸ਼ਨ ਦੀ ਵਰਣਨ ਵਾਲਾ ਇੱਕ ਸਕੀਮਾ LLM ਨੂੰ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ। LLM ਫਿਰ ਟਾਸਕ ਲਈ ਸਭ ਤੋਂ ਮੁਆਫਕ ਫੰਕਸ਼ਨ ਦੀ ਚੋਣ ਕਰਦਾ ਹੈ ਅਤੇ ਉਸ ਦਾ ਨਾਮ ਅਤੇ ਤਰਕ ਸਮੇਤ ਵਾਪਸ ਭੇਜਦਾ ਹੈ। ਚੁਣਿਆ ਗਿਆ ਫੰਕਸ਼ਨ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਇਸਦਾ ਜਵਾਬ LLM ਨੂੰ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ ਜੋ ਇਸ ਜਾਣਕਾਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਤੋਂਕਾਰ ਦੀ ਬੇਨਤੀ ਦਾ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

ਡਿਵੈਲਪਰਾਂ ਲਈ ਕਿ ਏਜੰਟਾਂ ਵਾਸਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਲਾਗੂ ਕਰਨੀ ਹੋਵੇ, ਤੁਹਾਨੂੰ ਲੋੜ ਹੋਵੇਗੀ:

1. ਇੱਕ LLM ਮਾਡਲ ਜੋ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਮਰਥਿਤ ਕਰਦਾ ਹੋਵੇ
2. ਫੰਕਸ਼ਨ ਵਰਣਨਾ ਵਾਲਾ ਇੱਕ ਸਕੀਮਾ
3. ਹਰ ਫੰਕਸ਼ਨ ਲਈ ਲਿਖਿਆ ਹੋਇਆ ਕੋਡ

ਆਓ ਇੱਕ ਉਦਾਹਰਨ ਦੇ ਨਾਲ ਸਮਝਦੇ ਹਾਂ ਜਿਵੇਂ ਕਿਸੇ ਸ਼ਹਿਰ ਦਾ ਹਾਲੀਆ ਸਮਾਂ ਪਤਾ ਕਰਨਾ:

1. **ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਮਰਥਿਤ LLM ਸ਼ੁਰੂ ਕਰੋ:**

    ਸਾਰੇ ਮਾਡਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਮਰਥਿਤ ਨਹੀਂ ਕਰਦੇ, ਇਸ ਲਈ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਇਸ ਦੀ ਜਾਂਚ ਕਰੋ ਕਿ ਤੁਸੀਂ ਜੋ LLM ਵਰਤ ਰਹੇ ਹੋ ਉਹ ਕਰਦਾ ਹੈ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਅਸੀਂ Azure OpenAI **Responses API** ਦੇ ਖਿਲਾਫ OpenAI ਕਲਾਇਟ ਸੈਟਅੱਪ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਾਂ (ਥਿਰ `/openai/v1/` ਐਂਡਪੌਇੰਟ — ਕੋਈ `api_version` ਲੋੜ ਨਹੀਂ)।

    ```python
    # Azure OpenAI (Responses API, v1 ਐਂਡਪੌਇੰਟ) ਲਈ OpenAI ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰੋ
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ਫੰਕਸ਼ਨ ਸਕੀਮਾ ਬਣਾਓ**:

    ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਅਸੀਂ ਇੱਕ JSON ਸਕੀਮਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਨਾਮ, ਉਹ ਕੀ ਕਰਦਾ ਹੈ ਦਾ ਵੇਰਵਾ ਅਤੇ ਫੰਕਸ਼ਨ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਮ ਅਤੇ ਵਰਣਨ ਹੋਵੇਗਾ।
    ਫਿਰ ਅਸੀਂ ਇਹ ਸਕੀਮਾ ਉਸ ਕਲਾਇਟ ਨੂੰ ਦੇਵਾਂਗੇ ਜੋ ਅੱਗੇ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਅਤੇ ਵਰਤੋਂਕਾਰ ਦੇ ਸੈਨ ਫ੍ਰਾਂਸਿਸਕੋ ਵਿੱਚ ਸਮਾਂ ਲੱਭਣ ਲਈ ਬੇਨਤੀ ਨਾਲ ਸਾਂਝਾ ਕਰਾਂਗੇ। ਗੱਲ ਇਹ ਹੈ ਕਿ ਇੱਕ **ਟੂਲ ਕਾਲ** ਵਾਪਸ ਹੁੰਦੀ ਹੈ, **ਸਵਾਲ ਦਾ ਅੰਤਿਮ ਜਵਾਬ ਨਹੀਂ**। ਜਿਵੇਂ ਪਹਿਲਾਂ ਕਿਹਾ ਗਿਆ, LLM ਉਸ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਉਸ ਨੇ ਟਾਸਕ ਲਈ ਚੁਣਿਆ ਹੈ, ਨਾਲ ਹੀ ਉਹ ਤਰਕ ਜੋ ਉਸ ਨੂੰ ਪਾਸ ਕੀਤੇ ਜਾਣਗੇ।

    ```python
    # ਮਾਡਲ ਲਈ ਕੰਮ ਦਾ ਵੇਰਵਾ (Responses API ਫਲੈਟ ਟੂਲ ਫਾਰਮੈਟ)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # ਸ਼ੁਰੂਆਤੀ ਉਪਭੋਗਤਾ ਸੁਨੇਹਾ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # ਪਹਿਲੀ API ਕਾਲ: ਮਾਡਲ ਨੂੰ ਫੰਕਸ਼ਨ ਵਰਤਣ ਦੀ ਬੇਨਤੀ ਕਰੋ
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ਜਵਾਬ ਵਿੱਚ function_call ਆਈਟਮਾਂ ਵਜੋਂ ਟੂਲ ਕਾਲਜ਼ ਨੂੰ response.output ਵਿੱਚ ਵਾਪਸ ਕਰਦਾ ਹੈ।
    # ਮਾਡਲ ਕੋਲ ਅਗਲੇ ਮੁੜੇ ਵਿੱਚ ਪੂਰਾ ਸੰਦਰਭ ਹੋਵੇ ਇਸ ਲਈ ਉਨ੍ਹਾਂ ਨੂੰ ਗੱਲਬਾਤ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **ਕੋਡ ਜੋ ਟਾਸਕ ਪੂਰਾ ਕਰੇ:**

    ਹੁਣ ਜਦ LLM ਨੇ ਚੁਣਿਆ ਹੈ ਕਿ ਕਿਹੜਾ ਫੰਕਸ਼ਨ ਚਲਾਉਣਾ ਹੈ, ਉਸ ਕਾਰਜ ਲਈ ਲਿਖਿਆ ਗਿਆ ਕੋਡ ਲਾਗੂ ਅਤੇ ਚਲਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।
    ਅਸੀਂ ਪਾਇਥਨ ਵਿੱਚ ਮੌਜੂਦਾ ਸਮਾਂ ਪ੍ਰਾਪਤ ਕਰਨ ਵਾਲਾ ਕੋਡ ਲਿਖ ਸਕਦੇ ਹਾਂ। ਸਾਡੇ ਨੂੰ response_message ਵਿੱਚੋਂ ਨਾਮ ਅਤੇ ਤਰਕ ਕੱਢਣ ਲਈ ਕੋਡ ਵੀ ਲਿਖਣਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਅੰਤਿਮ ਨਤੀਜਾ ਮਿਲ ਸਕੇ।

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲੋ
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ਟੂਲ ਨਤੀਜੇ ਨੂੰ function_call_output ਆਈਟਮ ਵਜੋਂ ਵਾਪਸ ਕਰੋ
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # ਦੂਜੀ API ਕਾਲ: ਮਾਡਲ ਤੋਂ ਆਖਰੀ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰੋ
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਜ਼ਿਆਦਾਤਰ, ਜੇ ਸਾਰੇ ਨਾ ਹੋਣ, ਤਾਂ ਵੀ ਏਜੰਟ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਦਾ ਕੇਂਦਰ ਹੈ, ਪਰ ਇਸਨੂੰ ਮੂਲ ਤੌਰ 'ਤੇ ਲਾਗੂ ਕਰਨਾ ਕਈ ਵਾਰੀ ਚੁਣੌਤੀਪੂਰਕ ਹੋ ਸਕਦਾ ਹੈ।
ਜਿਵੇਂ ਅਸੀਂ [ਪਾਠ 2](../../../02-explore-agentic-frameworks) ਵਿੱਚ ਸਿੱਖਿਆ ਸੀ, ਏਜੰਟ ਫਰੇਮਵਰਕ ਸਾਨੂੰ ਟੂਲ ਯੂਜ਼ ਲਾਗੂ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਹੀ ਤਿਆਰ ਬਿਲਡਿੰਗ ਬਲਾਕ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।
 
## ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਨਾਲ ਟੂਲ ਯੂਜ਼ ਦੇ ਉਦਾਹਰਨ

ਹੇਠਾਂ ਕੁਝ ਉਦਾਹਰਨ ਹਨ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਵੱਖ-ਵੱਖ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਵਰਤ ਕੇ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹੋ:

### ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ</a> AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਇੱਕ ਖੁੱਲ੍ਹਾ ਸੋਰਸ ਫਰੇਮਵਰਕ ਹੈ। ਇਹ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਨਾਲ ਤੁਸੀਂ `@tool` ਡੈਕੇਰੇਟਰ ਨਾਲ ਪਾਇਥਨ ਫੰਕਸ਼ਨਾਂ ਵਜੋਂ ਟੂਲ DEFINE ਕਰ ਸਕਦੇ ਹੋ। ਫਰੇਮਵਰਕ ਮਾਡਲ ਅਤੇ ਤੁਹਾਡੇ ਕੋਡ ਵਿਚਕਾਰ ਸੰਚਾਰ ਦਾ ਪ੍ਰਬੰਧ ਕਰਦਾ ਹੈ। ਇਸ ਨਾਲ ਤੁਹਾਨੂੰ File Search ਅਤੇ Code Interpreter ਵਰਗੇ ਪਹਿਲਾਂ ਤਿਆਰ ਕੀਤੇ ਟੂਲਾਂ ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਹੁੰਦੀ ਹੈ `FoundryChatClient` ਰਾਹੀਂ।

ਹੇਠਾਂ ਦਿੱਤਾ ਡਾਇਗ੍ਰਾਮ ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ:

![function calling](../../../translated_images/pa/functioncalling-diagram.a84006fc287f6014.webp)

ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਵਿੱਚ, ਟੂਲ ਨਿਯੋਜਿਤ ਫੰਕਸ਼ਨ ਆਖੇ ਜਾਂਦੇ ਹਨ। ਅਸੀਂ ਪਹਿਲਾਂ ਵੱਖ ਵੱਖ ਵੇਖੀ ਗਈ `get_current_time` ਫੰਕਸ਼ਨ ਨੂੰ `@tool` ਡੈਕੇਰੇਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੂਲ ਵਿੱਚ ਬਦਲ ਸਕਦੇ ਹਾਂ। ਫਰੇਮਵਰਕ ਅਪਣੇ ਆਪ ਫੰਕਸ਼ਨ ਤੇ ਇਸਦੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸੀਰੀਅਲਾਈਜ਼ ਕਰਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਭੇਜਣ ਲਈ ਸਕੀਮਾ ਬਣਾ ਲੈਂਦਾ ਹੈ।

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ਕਲਾਇੰਟ ਬਣਾਓ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ਇੱਕ ਏਜੰਟ ਬਣਾਓ ਅਤੇ ਟੂਲ ਨਾਲ ਚਲਾਓ
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### ਮਾਈਕਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਏਜੰਟ ਸੇਵਾ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ਮਾਈਕਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਏਜੰਟ ਸੇਵਾ</a> ਇਕ ਨਵਾਂ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਬਿਨਾਂ ਇੰਫਰਾਸਟ੍ਰਕਚਰ ਦਾ ਪ੍ਰਬੰਧ ਕੀਤੇ ਬਿਹਤਰ ਗੁਣਵੱਤਾ, ਵਿਸ਼ਤਾਰਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ, ਤੈਅ ਕਰਨ ਅਤੇ ਪੈਮਾਨਾ ਵਧਾਉਣ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਖਾਸ ਕਰਕੇ ਉਦਯੋਗਿਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਲਾਭਕਾਰੀ ਹੈ ਕਿਉਂਕਿ ਇਹ ਪੂਰੀ ਤਰਾਂ ਮੈਨੇਜ ਕੀਤੀ ਸੇਵਾ ਹੈ ਜਿਸ ਵਿੱਚ ਉਦਯੋਗ ਸਰਕਾਣਾ ਸੁਰੱਖਿਆ ਮੌਜੂਦ ਹੈ।

LLM API ਨਾਲ ਸਿੱਧਾ ਵਿਕਾਸ ਕਰਨ ਦੇ ਮੁਕਾਬਲੇ, ਮਾਈਕਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਏਜੰਟ ਸੇਵਾ ਕੁਝ ਲਾਭ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ:

- ਸਵੈਚਾਲਿਤ ਟੂਲ ਕਾਲ - ਹੁਣ ਸਰਵਰ-ਸਾਈਡ ਇਸਤੇਮਾਲ ਵਿੱਚ ਟੂਲ ਕਾਲ ਨੂੰ ਪਾਰਸ ਕਰਨ, ਕਾਲ ਕਰਨ ਅਤੇ ਜਵਾਬ ਸੰਭਾਲਣ ਦੀ ਲੋੜ ਨਹੀਂ ਰਹੀ
- ਸੁਰੱਖਿਅਤ ਡੇਟਾ ਪ੍ਰਬੰਧਨ - ਆਪਣੇ ਗੱਲਬਾਤ ਸਥਿਤੀ ਦੇ ਪ੍ਰਬੰਧਨ ਦੀ ਥਾਂ ਤੁਸੀਂ ਥ੍ਰੈਡਾਂ 'ਤੇ ਭਰੋਸਾ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਸਾਰੀ ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਸਟੋਰ ਕਰਦੀਆਂ ਹਨ
- ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਦਿਸਣ ਵਾਲੇ ਟੂਲ - ਟੂਲਾਂ ਜਿਨ੍ਹਾਂ ਨਾਲ ਤੁਸੀਂ ਆਪਣੇ ਡੇਟਾ ਸਰੋਤਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ Bing, Azure AI Search ਅਤੇ Azure Functions।

ਮਾਈਕਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਏਜੰਟ ਸੇਵਾ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲਾਂ ਨੂੰ ਦੁਹਿ ਵੰਡਿਆ ਜਾ ਸਕਦਾ ਹੈ:

1. ਗਿਆਨ ਟੂਲ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ਨਾਲ ਗ੍ਰਾਊਂਡਿੰਗ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ਫਾਈਲ ਖੋਜ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI ਖੋਜ</a>

2. ਕਾਰਵਾਈ ਟੂਲ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ਪਰਿਭਾਸ਼ਿਤ ਟੂਲ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ਏਜੰਟ ਸੇਵਾ ਸਾਨੂੰ ਇਹ ਟੂਲ ਇਕੱਠੇ `toolset` ਵਜੋਂ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਇਸ ਨਾਲ `threads` ਦੀ ਵਰਤੋਂ ਹੁੰਦੀ ਹੈ ਜੋ ਕਿਸੇ ਖਾਸ ਗੱਲਬਾਤ ਵਿੱਚ ਸਨੇਹਿਆਂ ਦਾ ਇਤਿਹਾਸ ਰੱਖਦੇ ਹਨ।

ਸੋਚੋ ਕਿ ਤੁਸੀਂ Contoso ਕੰਪਨੀ ਵਿੱਚ सेलਜ਼ ਏਜੰਟ ਹੋ। ਤੁਸੀਂ ਇਕ ਸੰਵਾਦਾਤਮਕ ਏਜੰਟ ਵਿਕਸਿਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਤੁਹਾਡੇ ਵਿਕਰੀ ਡੇਟਾ ਬਾਰੇ ਸਵਾਲਾਂ ਦਾ ਜਵਾਬ ਦੇ ਸਕੇ।

ਹੇਠਾਂ ਦਿੱਤੀ ਤਸਵੀਰ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ Microsoft Foundry Agent Service ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਕੇ ਆਪਣਾ ਵਿਕਰੀ ਡੇਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰ ਸਕਦੇ ਹੋ:

![ਏਜੰਟਿਕ ਸੇਵਾ ਕਾਰਵਾਈ ਵਿੱਚ](../../../translated_images/pa/agent-service-in-action.34fb465c9a84659e.webp)

ਇਨ੍ਹਾਂ ਟੂਲਾਂ ਨੂੰ ਸੇਵਾ ਨਾਲ ਵਰਤਣ ਲਈ ਅਸੀਂ ਇੱਕ ਕਲਾਇਟ ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਇੱਕ ਟੂਲ ਜਾਂ ਟੂਲਸੈੱਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ। ਇਸਨੂੰ ਅਮਲੀ ਜਾਮਾ ਪਹਨਾਉਣ ਲਈ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤਾ ਪਾਇਥਨ ਕੋਡ ਵਰਤ ਸਕਦੇ ਹਾਂ। LLM ਟੂਲਸੈੱਟ ਨੂੰ ਵੇਖ ਕੇ ਫ਼ੈਸਲਾ ਕਰੇਗਾ ਕਿ ਵਰਤੋਂਕਾਰ ਵੱਲੋਂ ਬਣਾਇਆ ਫੰਕਸ਼ਨ `fetch_sales_data_using_sqlite_query` ਵਰਤਣਾ ਹੈ ਜਾਂ ਪਹਿਲਾਂ ਤੋਂ ਬਣਿਆ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ਫੰਕਸ਼ਨ ਜੋ कि fetch_sales_data_functions.py ਫਾਈਲ ਵਿੱਚ ਮਿਲ ਸਕਦਾ ਹੈ।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ਟੂਲਸੈੱਟ ਸ਼ੁਰੂ ਕਰੋ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ਫੰਕਸ਼ਨ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਏਜੰਟ ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਇਸਨੂੰ ਟੂਲਸੈੱਟ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ਕੋਡ ਇੰਟਰਪੀਟਰ ਟੂਲ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਇਸਨੂੰ ਟੂਲਸੈੱਟ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ।
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਵਰਤਦੇ ਸਮੇਂ ਖਾਸ ਧਿਆਨ

LLMs ਵੱਲੋਂ ਡਾਇਨਾਮਿਕ ਤੌਰ 'ਤੇ ਬਣਾਇਆ SQL ਸੁਰੱਖਿਆ ਲਈ ਚਿੰਤਾ ਹੈ, ਖ਼ਾਸ ਕਰਕੇ SQL ਇੰਜੈਕਸ਼ਨ ਜਾਂ ਖ਼ਰਾਬ ਇਰਾਦੇ ਵਾਲੇ ਕੰਮਾਂ ਦਾ ਖ਼ਤਰਾ ਜਿਵੇਂ ਡੇਟਾਬੇਸ ਨੂੰ ਡ੍ਰੌਪ ਕਰਨਾ ਜਾਂ ਚੋਣ-ਚਲਾਉਣਾ। ਇਹ ਚਿੰਤਾ ਸਹੀ ਹਨ ਪਰ ਡੇਟਾਬੇਸ ਐਕਸੈੱਸ ਪਰਮੀਸ਼ਨਸ ਨੂੰ ਢੰਗ ਨਾਲ ਸੰਰਚਿਤ ਕਰਕੇ ਇਹਨਾਂ ਨੂੰ ਸਹੀ ਢੰਗ ਨਾਲ ਰੋਕਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਡੇਟਾਬੇਸਾਂ ਲਈ ਇਹਨਾਂ ਨੂੰ ਰੀਡ-ਓਨਲੀ ਬਣਾਉਣਾ ਸ਼ਾਮਿਲ ਹੈ। PostgreSQL ਜਾਂ Azure SQL ਵਰਗੀਆਂ ਡੇਟਾਬੇਸ ਸੇਵਾਵਾਂ ਲਈ ਐਪ ਨੂੰ ਰੀਡ-ਓਨਲੀ (SELECT) ਰੋਲ ਅਲੌਕ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

ਐਪ ਨੂੰ ਸੁਰੱਖਿਅਤ ਮਾਹੌਲ ਵਿੱਚ ਚਲਾਉਣਾ ਰੱਖਵਾਲ ਨੂੰ ਹੋਰ ਮਜ਼ਬੂਤ ਕਰਦਾ ਹੈ। ਉਦਯੋਗਿਕ ਸੰਦਰਭਾਂ ਵਿੱਚ, ਡੇਟਾ ਆਮ ਤੌਰ ਤੇ ਪ੍ਰਚਾਲਨ ਪ੍ਰਣਾਲੀਆਂ ਤੋਂ ਇੱਕ ਰੀਡ-ਓਨਲੀ ਡੇਟਾਬੇਸ ਜਾਂ ਡੇਟਾ ਵੇਅਰਹਾਊਸ ਵਿੱਚ ਨਿਕਾਲਿਆ ਅਤੇ ਬਦਲਿਆ ਜਾਂਦਾ ਹੈ ਜਿਸ ਦੀ ਵਿਵਸਥਾ ਯੂਜ਼ਰ-ਫਰੈਂਡਲੀ ਸਕੀਮਾ ਨਾਲ ਹੁੰਦੀ ਹੈ। ਇਸ ਤਰੀਕੇ ਨਾਲ ਡੇਟਾ ਸੁਕੂਨਤਮ, ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਪਹੁੰਚ ਲਈ ਆਪਟੀਮਾਈਜ਼ਡ ਹੁੰਦਾ ਹੈ ਅਤੇ ਐਪ ਕੋਲ ਸਿਰਫ ਰੀਡ-ਓਨਲੀ ਪਹੁੰਚ ਹੁੰਦੀ ਹੈ।

## ਨਮੂਨਾ ਕੋਡ

- ਪਾਇਥਨ: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ਟੂਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲਣ ਲਈ, ਦਫਤਰ ਘੰਟਿਆਂ ਵਿੱਚ ਸ਼ਿਰਕਤ ਕਰਨ ਲਈ ਅਤੇ ਤੁਹਾਡੇ AI ਏਜੰਟ ਸਵਾਲਾਂ ਦਾ ਜਵਾਬ ਲੈਣ ਲਈ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ।

## ਵਾਧੂ ਸਰੋਤ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI ਏਜੰਟ ਸੇਵਾ ਵਰਕਸ਼ਾਪ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer ਮੁਲਟੀ-ਏਜੰਟ ਵਰਕਸ਼ਾਪ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ਏਜੰਟ ਫਰੇਮਵਰਕ ਸੰਗ੍ਰਹਿ</a>


## ਇਸ ਏਜੰਟ ਨੂੰ ਸਿਮਟੈਸਟ ਕਰਨਾ (ਵੈਕਲਪਿਕ)

ਜਦੋਂ ਤੁਸੀਂ [Lesson 16](../16-deploying-scalable-agents/README.md) ਵਿਚ ਏਜੰਟ ਤਾਇਨਾਤ ਕਰਨਾ ਸਿੱਖ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਪਾਠ ਦੇ `TravelToolAgent` ਦਾ ਸਿਮਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ (ਕੀ ਇਹ ਹਾਲੇ ਵੀ ਆਪਣੇ ਟੂਲ ਕਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ਨਾਲ। ਇਹ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ ਦੇਖਣ ਲਈ [`tests/README.md`](../tests/README.md) ਵੇਖੋ।

## ਪਿਛਲਾ ਪਾਠ

[Agentic Design Patterns ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)

## ਅਗਲਾ ਪਾਠ

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->