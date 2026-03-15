[![How to Design Good AI Agents](../../../translated_images/pa/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉੱਪਰ ਦੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

# ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ

ਟੁਲ ਦਿਲਚਸਪ ਹਨ ਕਿਉਂਕਿ ਉਹ AI ਏਜੰਟਸ ਨੂੰ ਵਿਆਪਕ ਸਖਮਤਾ ਵਾਲੇ ਬਣਾਉਂਦੇ ਹਨ। ਏਜੰਟ ਕੋਲ ਜਦ ਜੋ ਹੱਦਬੰਦੀ ਸਿਟ ਲਈ ਕਾਰਵਾਈਆਂ ਹੋਣ ਦੀ ਥਾਂ, ਟੁਲ ਸ਼ਾਮਲ ਕਰਨ ਨਾਲ, ਏਜੰਟ ਹੁਣ ਕਈ ਕਿਸਮ ਦੀਆਂ ਕਾਰਵਾਈਆਂ ਕਰ ਸਕਦਾ ਹੈ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਅਸੀਂ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਦੇਖਾਂਗੇ, ਜੋ ਵਰਨਨ ਕਰਦਾ ਹੈ ਕਿ ਕਿਵੇਂ AI ਏਜੰਟ ਕੁਝ ਖਾਸ ਟੁਲਾਂ ਦੀ ਵਰਤੋਂ ਆਪਣੇ ਲਕੜੀਆਂ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਰ ਸਕਦੇ ਹਨ।

## ਪਰਿਚय

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਹੇਠਲੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੱਭਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ:

- ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?
- ਇਹ ਕਿਹੜੇ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਤੇ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ?
- ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਕਿਹੜੇ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ?
- ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਦੇ ਕਿਸ ਖਾਸ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਵਾਲੇ ਮੁੱਦੇ ਕੀ ਹਨ?

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਤੇ ਇਸਦੇ ਮਕਸਦ ਦੀ ਪਰਿਭਾਸ਼ਾ ਕਰਨ ਲਈ।
- ਉਹ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਪਛਾਣਨ ਲਈ ਜਿੱਥੇ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਹੁੰਦਾ ਹੈ।
- ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਜਰੂਰੀ ਮੁੱਖ ਤੱਤ ਸਮਝਣ ਲਈ।
- ਇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਨਾਲ ਭਰੋਸੇਯੋਗਤਾ ਯਕੀਨੀ ਕਰਨ ਲਈ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ।

## ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?

**ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ** LLM ਨੂੰ ਬਾਹਰੀ ਟੁਲਾਂ ਨਾਲ ਮੁਲਾਕਾਤ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੰਦਾ ਹੈ ਤਾਂ ਜੋ ਖਾਸ ਲਕੜੀਆਂ ਹਾਸਲ ਕੀਤੀਆਂ ਜਾ ਸਕਣ। ਟੁਲ ਉਹ ਕੋਡ ਹਨ ਜੋ ਕਿਸੇ ਏਜੰਟ ਵੱਲੋਂ ਚਲਾਏ ਜਾ ਸਕਦੇ ਹਨ ਕਾਰਵਾਈਆਂ ਕਰਨ ਲਈ। ਇੱਕ ਟੁਲ ਇੱਕ ਸਧਾਰਣ ਫੰਕਸ਼ਨ ਜਿਵੇਂ ਕਿ ਕੈਲਕੂਲੇਟਰ ਹੋ ਸਕਦਾ ਹੈ, ਜਾਂ ਤੀਜੀ-ਪੱਖੀ ਸੇਵਾ ਦੇ API ਕਾਲ ਜਿਵੇਂ ਕਿ ਸਟਾਕ ਕੀਮਤ ਦੀ ਖੋਜ ਜਾਂ ਮੌਸਮ ਦਾ ਅੰਦਾਜ਼ਾ। AI ਏਜੰਟਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਟੁਲਾਂ ਨੂੰ ਏਜੰਟ ਵੱਲੋਂ **ਮਾਡਲ-ਤਿਆਰ ਕੀਤੀਆਂ ਫੰਕਸ਼ਨ ਕਾਲਾਂ** ਦੇ ਜਵਾਬ ਵਿੱਚ ਚਲਾਉਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

## ਇਹ ਕਿਹੜੇ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਤੇ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ?

AI ਏਜੰਟ ਟੁਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੁਸ਼ਕਲ ਕੰਮ ਪੂਰੇ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਂ ਫੈਸਲੇ ਕਰ ਸਕਦੇ ਹਨ। ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਕਸਰ ਬਾਹਰੀ ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਡਾਇਨਾਮਿਕ ਇੰਟਰਐਕਸ਼ਨ ਦੀ ਲੋੜ ਵਾਲੇ ਸਥਿਤੀਆਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਵੇਂ ਡੇਟਾਬੇਸ, ਵੈੱਬ ਸੇਵਾਵਾਂ, ਜਾਂ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ। ਇਹ ਸਮਰੱਥਾ ਕਈ ਅਲੱਗ-ਅਲੱਗ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ ਲਾਭਦਾਇਕ ਹੈ ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- **ਡਾਇਨਾਮਿਕ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤੀ:** ਏਜੰਟ ਬਾਹਰੀ API ਜਾਂ ਡੇਟਾਬੇਸ ਨੂੰ ਪੁੱਛਕੇ ਅਪ-ਟੂ-ਡੇਟ ਡੇਟਾ ਲੈ ਸਕਦੇ ਹਨ (ਜਿਵੇਂ SQLite ਡੇਟਾਬੇਸ ਵਿਚਾਲੇ ਡੇਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਪੁੱਛਗਿੱਛ, ਸਟਾਕ ਕੀਮਤਾਂ ਜਾਂ ਮੌਸਮ ਦੀ ਜਾਣਕਾਰੀ ਲੈਣਾ)।
- **ਕੋਡ ਚਲਾਉਣਾ ਅਤੇ ਵਿਆਖਿਆ ਕਰਨਾ:** ਏਜੰਟ ਗਣਿਤੀ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਨ, ਰਿਪੋਰਟ ਤਿਆਰ ਕਰਨ ਜਾਂ ਸਮੂਲੀਕਰਨ ਕਰਨ ਲਈ ਕੋਡ ਜਾਂ ਸਕ੍ਰਿਪਟ ਚਲਾ ਸਕਦੇ ਹਨ।
- **ਵਰਕਫਲੋ ਆਟੋਮੇਸ਼ਨ:** ਟਾਸਕ ਸ਼ੈਡਿਊਲਰ, ਈਮੇਲ ਸੇਵਾਵਾਂ ਜਾਂ ਡੇਟਾ ਪਾਈਪਲਾਈਨਾਂ ਵਰਗੇ ਟੁਲਾਂ ਨੂੰ ਜੋੜਕੇ ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਜਾਂ ਬਹੁ-ਕਦਮੀ ਵਰਕਫਲੋਜ਼ ਆਟੋਮੇਟ ਕਰਨਾ।
- **ਗਾਹਕ ਸਹਾਇਤਾ:** ਏਜੰਟ CRM ਪ੍ਰਣਾਲੀਆਂ, ਟਿਕਟਿੰਗ ਪਲੇਟਫਾਰਮਾਂ ਜਾਂ ਨੋਲੇਜ਼ ਬੇਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਕੇ ਯੂਜ਼ਰਾਂ ਦੇ ਪ੍ਰਸ਼ਨਾਂ ਦਾ ਹੱਲ ਕਰ ਸਕਦੇ ਹਨ।
- **ਸਮੱਗਰੀ ਤਿਆਰ ਕਰਨਾ ਅਤੇ ਸੰਪਾਦਨ:** ਐਜੰਟ ਗ੍ਰੈਮਰ ਚੈਕਰ, ਟੈਕਸਟ ਸਮਰੀ ਵਿੱਚਕਾਰਨਾ, ਜਾਂ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਜਿਹੇ ਟੁਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

## ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਜਰੂਰੀ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕ ਕੀ ਹਨ?

ਇਹ ਬਿਲਡਿੰਗ ਬਲਾਕ AI ਏਜੰਟ ਨੂੰ ਕਈ ਤਰ੍ਹਾਂ ਦੇ ਕਾਰਜ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ। ਆਓ ਮੁੱਖ ਤੱਤ ਵੇਖੀਏ ਜੋ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਹਨ:

- **ਫੰਕਸ਼ਨ/ਟੁਲ ਸਕੀਮਾਕਾਰ:** ਉਪਲੱਬਧ ਟੁਲਾਂ ਦੇ ਵਿਸਥਾਰਿਤ ਪਰਿਭਾਸ਼ਾ, ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਨਾਮ, ਮਕਸਦ, ਜ਼ਰੂਰੀ ਪੈਰਾਮੀਟਰ, ਅਤੇ ਉਮੀਦ ਕੀਤੇ ਨਤੀਜੇ ਸ਼ਾਮਿਲ ਹਨ। ਇਹ ਸਕੀਮਾਵਾਂ LLM ਨੂੰ ਇਹ ਸਮਝਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ ਕਿ ਕਿਹੜੇ ਟੁਲ ਉਪਲੱਬਧ ਹਨ ਅਤੇ ਕਿਵੇਂ ਸਹੀ ਬੇਨਤੀ ਤਿਆਰ ਕੀਤੀ ਜਾਵੇ।

- **ਫੰਕਸ਼ਨ ਚਲਾਉਣ ਵਾਲਾ ਤਰਤੀਬ-ਵਿਧੀ:** ਇਸਦਾ ਨਿਯੰਤਰਣ ਹੁੰਦਾ ਹੈ ਕਿ ਟੁਲ ਕਦੋਂ ਅਤੇ ਕਿਵੇਂ ਕਾਲ ਕੀਤੇ ਜਾਣ, ਉਪਭੋਗਤਾ ਦੀ ਨੀਅਤ ਅਤੇ ਵਿਚਾਰ-ਵਟਾਂਦਰੇ ਦੇ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ। ਇਸ ਵਿੱਚ ਯੋਜਨਾ ਮੌਡੀਊਲ, ਰੂਟਿੰਗ ਮੇਕੈਨੀਜ਼ਮ, ਜਾਂ ਸ਼ਰਤੀ ਫਲੋ ਸ਼ਾਮਿਲ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਟੁਲ ਦੀ ਵਰਤੋਂ ਡਾਇਨਾਮਿਕ ਤੌਰ ਤੇ ਨਿਰਧਾਰਿਤ ਕਰਦੇ ਹਨ।

- **ਸੰਦੇਸ਼ ਸੰਭਾਲਣ ਪ੍ਰਣਾਲੀ:** ਉਹ ਹਿੱਸੇ ਜੋ ਉਪਭੋਗਤਾ ਦੇ ਇਨਪੁੱਟ, LLM ਦੇ ਜਵਾਬ, ਟੁਲ ਕਾਲਾਂ ਅਤੇ ਟੁਲ ਆਉਟਪੁੱਟ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਵਾਹ ਸੰਭਾਲਦੇ ਹਨ।

- **ਟੁਲ ਇੰਟੀਗਰੇਸ਼ਨ ਫਰੇਮਵਰਕ:** ਢਾਂਚਾ ਜੋ ਏਜੰਟ ਨੂੰ ਵੱਖ-ਵੱਖ ਟੁਲਾਂ ਨਾਲ ਜੋੜਦਾ ਹੈ, ਚਾਹੇ ਉਹ ਸਧਾਰਣ ਫੰਕਸ਼ਨ ਹਨ ਜਾਂ ਜਟਿਲ ਬਾਹਰੀ ਸੇਵਾਵਾਂ।

- **ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਵੈਰੀਫਿਕੇਸ਼ਨ:** ਟੁਲ ਚਲਾਉਣ ਵਿੱਚ ਨਾਕਾਮੀਆਂ ਨੂੰ ਹੈਂਡਲ ਕਰਨ, ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਵੈਧ ਕਰਨ, ਅਤੇ ਅਣਉਮੀਦੀਂ ਜਵਾਬਾਂ ਨੂੰ ਮੈਨੇਜ ਕਰਨ ਵਾਲੀ ਯੰਤ੍ਰणा।

- **ਸਟੇਟ ਪ੍ਰਬੰਧਨ:** ਗੱਲਬਾਤ ਦਾ ਸੰਦਰਭ, ਪਹਿਲਾਂ ਟੁਲ ਇੰਟਰਐਕਸ਼ਨ, ਅਤੇ ਲਗਾਤਾਰ ਡੇਟਾ ਨੂੰ ਟ੍ਰੈਕ ਕਰਦਾ ਹੈ ਤਾਂ ਕਿ ਬਹੁ-ਚਰਣ ਇੰਟਰਐਕਸ਼ਨਾਂ ਵਿਚ ਸਥਿਰਤਾ ਬਣੀ ਰਹੇ।

ਹੁਣ, ਆਓ ਫੰਕਸ਼ਨ/ਟੁਲ ਕਾਲਿੰਗ ਦੀ ਵਧੇਰੇ ਵਿਸਥਾਰ ਵਿੱਚ ਚਰਚਾ ਕਰੀਏ।

### ਫੰਕਸ਼ਨ/ਟੁਲ ਕਾਲਿੰਗ

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਮੁੱਖ ਤਰੀਕਾ ਹੈ ਜਿਸ ਨਾਲ ਅਸੀਂ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਨੂੰ ਟੁੱਲਾਂ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਾਂ। ਤੁਸੀਂ ਅਕਸਰ 'ਫੰਕਸ਼ਨ' ਅਤੇ 'ਟੁਲ' ਨੂੰ ਬਰਾਬਰ ਵੇਖੋਂਗੇ ਕਿਉਂਕਿ 'ਫੰਕਸ਼ਨ' (ਪੁਨਰਵਰਤਨੀਯ ਕੋਡ ਬਲਾਕ) ਉਹ 'ਟੁਲ' ਹਨ ਜਿਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਏਜੰਟ ਕਾਰਜ ਕਰਨ ਲਈ ਕਰਦੇ ਹਨ। ਇੱਕ ਫੰਕਸ਼ਨ ਦੇ ਕੋਡ ਨੂੰ ਚਲਾਉਣ ਲਈ, LLM ਨੂੰ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਨਾਲ ਫੰਕਸ਼ਨ ਦੀ ਵਰਣਨਾ ਦੀ ਤੁਲਨਾ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। ਇਸ ਲਈ, ਸਾਰੇ ਉਪਲੱਬਧ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਣਨਾ ਵਾਲਾ ਇੱਕ ਸਕੀਮਾ LLM ਨੂੰ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ। ਫਿਰ LLM ਸਭ ਤੋਂ ਉਚਿਤ ਫੰਕ਼ਸ਼ਨ ਚੁਣਦਾ ਹੈ ਅਤੇ ਇਸਦੇ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਬਿਜ਼ੁਆਉਂਦਾ ਹੈ। ਚੁਣਿਆ ਗਿਆ ਫੰਕਸ਼ਨ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਇਸਦਾ ਜਵਾਬ LLM ਨੂੰ ਵਾਪਸ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਜਾਣਕਾਰੀ ਨੂੰ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਦਾ ਜਵਾਬ ਦੇਣ ਲਈ ਵਰਤਦਾ ਹੈ।

ਡਿਵੈਲਪਰਾਂ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨੂੰ ਏਜੰਟ ਲਈ ਲਾਗੂ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਲੋੜ ਹੋਵੇਗੀ:

1. ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਹਾਇਕ LLM ਮਾਡਲ
2. ਫੰਕਸ਼ਨ ਵਰਣਨ ਵਾਲਾ ਸਕੀਮਾ
3. ਹਰ ਫੰਕਸ਼ਨ ਦਾ ਕੋਡ ਜਿਸਨੂੰ ਵੇਰਵਾ ਦਿੱਤਾ ਗਿਆ ਹੈ

ਚਲੋ ਇੱਕ ਉਦਾਹਰਨ ਦੇਖੀਏ ਜਿੱਥੇ ਸ਼ਹਿਰ ਵਿੱਚ ਮੌਜੂਦਾ ਸਮਾਂ ਲੈਣਾ ਹੈ:

1. **ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨੂੰ ਸਹਾਇਕ ਕਰਦਾ LLM ਇਨੀਸ਼ੀਅਲਾਈਜ਼ ਕਰੋ:**

    ਸਾਰੇ ਮਾਡਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਹਾਇਕ ਨਹੀਂ ਹੁੰਦੇ, ਇਸ ਲਈ ਇਹ ਜਾਂਚਣਾ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਜੋ LLM ਵਰਤ ਰਹੇ ਹੋ ਉਹ ਇਹ ਕਰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨੂੰ ਸਹਾਰਦਾ ਹੈ। ਅਸੀਂ Azure OpenAI ਕਲਾਇੰਟ ਨੂੰ ਸ਼ੁਰੂ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਾਂ।

    ```python
    # Azure OpenAI ਕਲਾਇੰਟ ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ਫੰਕਸ਼ਨ ਸਕੀਮਾ ਬਣਾਓ:**

    ਅੱਗੇ ਅਸੀਂ ਇੱਕ JSON ਸਕੀਮਾ	define ਕਰਾਂਗੇ ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ, ਇਸਦਾ ਵਰਣਨ ਅਤੇ ਫੰਕਸ਼ਨ ਦੇ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਮ ਅਤੇ ਵਰਣਨ ਸ਼ਾਮਿਲ ਹੋਵੇਗਾ।

    ਫਿਰ ਅਸੀਂ ਇਸ ਸਕੀਮਾ ਨੂੰ ਪਿਛਲੀ ਵਾਰ ਬਣਾਏ ਗਏ ਕਲਾਇੰਟ ਨੂੰ ਦੇਵਾਂਗੇ, ਨਾਲ ਹੀ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ "San Francisco ਵਿੱਚ ਸਮਾਂ ਲੱਭੋ" ਵੀ ਭੇਜਾਂਗੇ। ਜ਼ਰੂਰੀ ਗੱਲ ਇਹ ਹੈ ਕਿ ਜੋ ਵਾਪਸੀ ਹੁੰਦੀ ਹੈ, ਉਹ ਇੱਕ **ਟੁਲ ਕਾਲ** ਹੁੰਦਾ ਹੈ, ਪ੍ਰਸ਼ਨ ਦਾ ਅੰਤਿਮ ਜਵਾਬ ਨਹੀਂ। ਜਿਵੇਂ ਪਹਿਲਾਂ ਦੱਸਿਆ, LLM ਕੰਮ ਲਈ ਚੁਣੇ ਗਏ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਦਿੱਤੇ ਜਾਣ ਵਾਲੇ ਆਰਗੁਮੈਂਟ ਵਾਪਸ ਕਰਦਾ ਹੈ।

    ```python
    # ਮਾਡਲ ਲਈ ਫੰਕਸ਼ਨ ਦਾ ਵੇਰਵਾ ਪੜ੍ਹਨ ਲਈ
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # ਸ਼ੁਰੂਆਤੀ ਉਪਭੋक्ता ਸੁਨੇਹਾ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ਪਹਿਲਾ API ਕਾਲ: ਮਾਡਲ ਨੂੰ ਫੰਕਸ਼ਨ ਵਰਤਣ ਲਈ ਕਹੋ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ਮਾਡਲ ਦੀ ਪ੍ਰਤੀਕ੍ਰਿਆ ਨੂੰ ਪ੍ਰਕਿਰਿਆਵੱਧ ਕਰੋ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ਟਾਸਕ ਕਰਨ ਲਈ ਜਰੂਰੀ ਫੰਕਸ਼ਨ ਕੋਡ:**

    ਹੁਣ ਜਦੋਂ LLM ਨੇ ਚੁਣ ਲਿਆ ਕਿ ਕਿਸ ਫੰਕਸ਼ਨ ਨੂੰ ਚਲਾਉਣਾ ਹੈ, ਉਸ ਆਮਲੀ ਟਾਸਕ ਦਾ ਕੋਡ ਲਿਖਣਾ ਅਤੇ ਚਲਾਉਣਾ ਪੈਂਦਾ ਹੈ।

    ਅਸੀਂ Python ਵਿੱਚ ਮੌਜੂਦਾ ਸਮਾਂ ਪ੍ਰਾਪਤ ਕਰਨ ਵਾਲਾ ਕੋਡ ਲਿਖਾਂਗੇ। ਸਾਨੂੰ ਇਹ ਵੀ ਲਿਖਣਾ ਪਵੇਗਾ ਕਿ ਰਿਸਪਾਂਸ_ਮੇਸੇਜ ਵਿੱਚੋਂ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਕਿਵੇਂ ਕੱਢਣੇ ਹਨ ਤਾਂ ਜੋ ਅੰਤਿਮ ਨਤੀਜਾ ਮਿਲ ਜਾਵੇ।

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # ਦੂਜਾ API ਕਾਲ: ਮਾਡਲ ਤੋਂ ਅਖੀਰੀ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰੋ
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਜ਼ਿਆਦਾਤਰ, ਜੇ ਨਾ ਸਾਰੇ, ਏਜੰਟ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਦਾ ਮੂਲ ਹੈ, ਪਰ ਇਸਨੂੰ ਸ਼ੁਰੂ ਤੋਂ ਲਾਗੂ ਕਰਣਾ ਕਈ ਵਾਰ ਚੁਣੌਤੀਪੂਰਨ ਹੋ ਸਕਦਾ ਹੈ। ਜਿਵੇਂ ਅਸੀਂ [Lesson 2](../../../02-explore-agentic-frameworks) ਵਿੱਚ ਸਿੱਖਿਆ, ਏਜੰਟ ਫਰੇਮਵਰਕ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਬਿਲਡਿੰਗ ਬਲਾਕ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨਾਲ ਟੁਲ ਯੂਜ਼ ਨੂੰ ਲਾਗੂ ਕਰਨਾ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ।

## ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਨਾਲ ਟੁਲ ਯੂਜ਼ ਉਦਾਹਰਨ

ਇੱਥੇ ਕੁਝ ਉਦਾਹਰਨ ਹਨ ਕਿ ਕਿਵੇਂ ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹੋ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ AI ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਹ ਤੁਹਾਨੂੰ ਟੁਲਾਂ ਨੂੰ ਪਾਇਥਨ ਫੰਕਸ਼ਨਾਂ ਵਜੋਂ `@tool` ਡੈਕੋਰੇਟਰ ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਦੀ ਆਸਾਨੀ ਦਿੰਦਾ ਹੈ। ਫਰੇਮਵਰਕ ਮਾਡਲ ਅਤੇ ਤੁਹਾਡੇ ਕੋਡ ਦਰਮਿਆਨ ਆਗੇ-پیچھੇ ਸੰਚਾਰ ਸੰਭਾਲਦਾ ਹੈ। ਇਹ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਟੁਲਾਂ ਵਰਗੇ File Search ਅਤੇ Code Interpreter ਦਾ ਐਕਸੈਸ ਵੀ ਦਿੰਦਾ ਹੈ ਜੋ `AzureAIProjectAgentProvider` ਰਾਹੀਂ ਮਿਲਦੇ ਹਨ।

ਹੇਠਾਂ ਦਿੱਤੀ ਡਾਇਗ੍ਰਾਮ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦਰਸਾਂਦੀ ਹੈ:

![function calling](../../../translated_images/pa/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework ਵਿੱਚ, ਟੁਲਾਂ ਨੂੰ ਸਜਾਇਆ ਹੋਇਆ ਫੰਕਸ਼ਨ ਵਜੋਂ ਦੇਖਾਇਆ ਜਾਂਦਾ ਹੈ। ਅਸੀਂ ਪਹਿਲਾਂ ਦੇਖੀ ਗਈ `get_current_time` ਫੰਕਸ਼ਨ ਨੂੰ `@tool` ਡੈਕੋਰੇਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੁਲ ਵਿੱਚ ਬਦਲ ਸਕਦੇ ਹਾਂ। ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਫੰਕਸ਼ਨ ਅਤੇ ਇਸਦੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸੀਰੀਅਲਾਈਜ਼ ਕਰਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਭੇਜਣ ਲਈ ਸਕੀਮਾ ਬਣਾਉਂਦਾ ਹੈ।

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ਗ੍ਰਾਹਕ ਬਣਾਓ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ਇੱਕ ਏਜੰਟ ਬਣਾਓ ਅਤੇ ਸੰਦ ਨਾਲ ਚਲਾਓ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ਨਵਾਂ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ, ਤੇਜ਼, ਅਤੇ ਵਿਆਪਕ AI ਏਜੰਟ ਬਿਨਾਂ ਸੰਚਾਲਨ ਅਤੇ ਸਟੋਰੇਜ ਸਰੋਤਾਂ ਦੀ ਚਿੰਤਾ ਕੀਤੇ ਬਣਾਉਣ ਦੇ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਸੰਸਥਾਵਾਂ ਲਈ ਖਾਸ ਕਰਕੇ ਲਾਭਦਾਇਕ ਹੈ ਕਿਉਂਕਿ ਇਹ ਪੂਰੀ ਤਰ੍ਹਾਂ ਪ੍ਰਬੰਧਿਤ ਅਤੇ ਵਪਾਰਕ ਗ੍ਰੇਡ ਸੁਰੱਖਿਆ ਵਾਲੀ ਸੇਵਾ ਹੈ।

ਸਿੱਧੀ ਤੌਰ ਤੇ LLM API ਨਾਲ ਵਿਕਾਸ ਕਰਨ ਨਾਲ ਤੁਲਨਾ ਕਰਨ 'ਤੇ, Azure AI Agent Service ਕੁਝ ਫਾਇਦੇ ਦਿੰਦਾ ਹੈ:

- ਆਟੋਮੈਟਿਕ ਟੂਲ ਕਾਲਿੰਗ – ਟੂਲ ਕਾਲ ਨੂੰ ਭੱਜਾਣੀ, ਕਾਲ ਕਰਨ, ਅਤੇ ਜਵਾਬ ਸੰਭਾਲਣ ਦੀ ਲੋੜ ਨਹੀਂ; ਇਹ ਸਾਰਾ ਸਰਵਰ-ਸਾਈਡ ਹੁੰਦਾ ਹੈ।
- ਸੁਰੱਖਿਅਤ ਡੇਟਾ ਪ੍ਰਬੰਧਨ – ਆਪਣੀ ਗੱਲਬਾਤ ਦੀ ਸਥਿਤੀ ਨੂੰ ਸੰਭਾਲਣ ਦੀ ਬਜਾਏ ਤੁਸੀਂ ਥ੍ਰੈਡਜ਼ ਤੇ ਨਿਰਭਰ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਸਾਰੀ ਜਾਣਕਾਰੀ ਸੰਭਾਲਦੇ ਹਨ।
- ਤਿਆਰ-ਤਿਆਰ ਟੂਲ – ਸੇਵਾਵਾਂ ਜਿਵੇਂ Bing, Azure AI Search, ਅਤੇ Azure Functions ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਉਪਲੱਬਧ ਹਨ।

Azure AI Agent Service ਵਿੱਚ ਉਪਲੱਬਧ ਟੂਲਾਂ ਨੂੰ ਦੋ ਵਰਗਾਂ ਵਿੱਚ ਵੰਡਿਆ ਜਾ ਸਕਦਾ ਹੈ:

1. ਗਿਆਨ ਟੂਲ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ਨਾਲ ਗਰਾਉਂਡਿੰਗ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ਕਿਰਿਆ ਟੂਲ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ਪਰਿਭਾਸ਼ਿਤ ਟੂਲ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ਏਜੰਟ ਸੇਵਾ ਸਾਨੂੰ ਇਹ ਟੂਲਾਂ ਇੱਕਠੇ `toolset` ਵਜੋਂ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ `threads` ਦੀ ਭੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਗੱਲਬਾਤ ਵਿੱਚ ਭੇਜੇ ਗਏ ਸੁਨੇਹਿਆਂ ਦਾ ਇਤਿਹਾਸ ਰੱਖਦਾ ਹੈ।

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਸੀਂ Contoso ਨਾਮਕ ਕੰਪਨੀ ਵਿਚ ਸੇਲਜ਼ ਏਜੰਟ ਹੋ। ਤੁਸੀਂ ਇੱਕ ਗੱਲਬਾਤੀ ਏਜੰਟ ਵਿਕਸਿਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਤੁਹਾਡੇ ਸੇਲਜ਼ ਡੇਟਾ ਬਾਰੇ ਪ੍ਰਸ਼ਨ ਦਾ ਜਵਾਬ ਦੇ ਸਕੇ।

ਹੇਠਾਂ ਦੀ ਤਸਵੀਰ ਦਰਸਾਉਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ Azure AI Agent Service ਨੂੰ ਵਰਤ ਕੇ ਆਪਣੇ ਸੇਲਜ਼ ਡੇਟੇ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

![Agentic Service In Action](../../../translated_images/pa/agent-service-in-action.34fb465c9a84659e.webp)

ਕਿਸੇ ਵੀ ਇਹਨਾਂ ਟੂਲਾਂ ਦਾ ਸੇਵਾ ਨਾਲ ਵਰਤਣ ਲਈ ਅਸੀਂ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਏਂਗੇ ਅਤੇ ਟੂਲ ਜਾਂ ਟੂਲਸੈੱਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ। ਇਸਦੀ ਕਾਰਵਾਈ ਵਿੱਚ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਪਾਇਥਨ ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ। LLM ਟੂਲਸੈੱਟ ਵੇਖਕੇ ਇਹ ਫੈਸਲਾ ਕਰੇਗਾ ਕਿ ਯੂਜ਼ਰ ਦੁਆਰਾ ਬਣਾਇਆ ਗਿਆ ਫੰਕਸ਼ਨ `fetch_sales_data_using_sqlite_query` ਉਪਯੋਗ ਕਰਨਾ ਹੈ ਜਾਂ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ ਨੂੰ, ਇਹ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ਫੰਕਸ਼ਨ ਜੋ fetch_sales_data_functions.py ਫਾਇਲ ਵਿੱਚ ਮਿਲ ਸਕਦੀ ਹੈ।
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ਟੂਲਸੈੱਟ ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ਫੰਕਸ਼ਨ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਏਜੰਟ ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਇਸ ਨੂੰ ਟੂਲਸੈੱਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ਕੋਡ ਇੰਟਰਪ੍ਰਿਟਰ ਟੂਲ ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਇਸ ਨੂੰ ਟੂਲਸੈੱਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ਭਰੋਸੇਯੋਗ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਵਰਤਣ ਦੇ ਖਾਸ ਧਿਆਨ ਕੀ ਹਨ?

LLM ਦੁਆਰਾ ਗਣਿਤ ਕੀਤਾ ਗਿਆ SQL ਸੁਰੱਖਿਆ ਲਈ ਇੱਕ ਆਮ ਚਿੰਤਾ ਹੈ, ਖਾਸ ਕਰਕੇ SQL injection ਜਾਂ ਦੁਰਪਯੋਗ ਕਾਰਵਾਈਆਂ ਜਿਵੇਂ ਡੇਟਾਬੇਸ ਨੂੰ ਡ੍ਰੌਪ ਕਰਨ ਜਾਂ ਛੇੜਛਾੜ ਕਰਨ ਦੇ ਖ਼ਤਰੇ। ਜਦਕਿ ਇਹ ਚਿੰਤਾਵਾਂ ਬਿਲਕੁਲ ਸਹੀ ਹਨ, ਇਨ੍ਹਾਂ ਨੂੰ ਡੇਟਾਬੇਸ ਐਕਸੇਸ ਅਧਿਕਾਰਾਂ ਨੂੰ ਢੰਗ ਨਾਲ ਸੰਰਚਿਤ ਕਰਕੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਰੋਕਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਡੇਟਾਬੇਸ ਲਈ ਇਹ ਮਤਲਬ ਹੈ ਕਿ ਡੇਟਾਬੇਸ ਨੂੰ ਰੀਡ-ਓਨਲੀ ਬਣਾਇਆ ਜਾਵੇ। PostgreSQL ਜਾਂ Azure SQL ਵਰਗੀਆ ਡੇਟਾਬੇਸ ਸੇਵਾਵਾਂ ਲਈ, ਐਪ ਨੂੰ ਰੀਡ-ਓਨਲੀ (SELECT) ਭੂਮਿਕਾ ਦਿੱਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।

ਐਪ ਨੂੰ ਸੁਰੱਖਿਅਤ ਵਾਤਾਵਰਨ ਵਿੱਚ ਚਲਾਉਣਾ ਸੁਰੱਖਿਆ ਨੂੰ ਹੋਰ ਵੱਧ ਸਕਦਾ ਹੈ। ਉਦਯੋਗਕ ਸਥਿਤੀਆਂ ਵਿੱਚ, ਡੇਟਾ ਆਮ ਤੌਰ ਤੇ ਓਪਰੇਸ਼ਨਲ ਸਿਸਟਮਾਂ ਤੋਂ ਕੱਢਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇੱਕ ਰੀਡ-ਓਨਲੀ ਡੇਟਾਬੇਸ ਜਾਂ ਡੇਟਾ ਵੇਅਰਹਾਊਸ ਵਿੱਚ ਤਬਦੀਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਿਸਦਾ ਸਕੀਮਾ ਉਪਯੋਗਕਾਰ-ਮਿੱਤਰ ਹੁੰਦਾ ਹੈ। ਇਹ ਪਹੁੰਚ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਡੇਟਾ ਸੁਰੱਖਿਅਤ, ਕਾਰਗਰਤਾ ਅਤੇ ਪਹੁੰਚ ਵਾਲੀ ਹੈ ਅਤੇ ਐਪ ਕੋਲ ਸੀਮਤ, ਰੀਡ-ਓਨਲੀ ਪਹੁੰਚ ਹੈ।

## ਸੈਂਪਲ ਕੋਡ

- ਪਾਇਥਨ: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ਟੁਲ ਯੂਜ਼ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਜ਼ ਬਾਰੇ ਹੋਰ ਸਵਾਲ ਹਨ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ, ਦੂਜੇ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਮਿਲੋ, ਦਫ਼ਤਰ ਘੰਟਿਆਂ 'ਚ ਹਾਜ਼ਰੀ ਦਿਓ, ਅਤੇ ਆਪਣੇ AI ਏਜੰਟ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲਵੋ।

## ਹੋਰ ਸਰੋਤ

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ਕਾਰਖਾਨਾ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer ਮਲਟੀ-ਏਜੰਟ ਕਾਰਖਾਨਾ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ਓਵਰਵਿਊ</a>

## ਪਿਛਲਾ ਪਾਠ

[Agentic Design Patterns ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)

## ਅਗਲਾ ਪਾਠ
[ਐਜੈਂਟਿਕ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀ ਤੱਥ ਹੋ ਸਕਦੇ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਵਿਸ਼ੇਸ਼ਗਿਆਨ ਅਦਮੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->