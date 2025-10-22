<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T10:28:21+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "pa"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.pa.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਵੇਖੋ)_
# AI ਏਜੰਟਸ ਵਿੱਚ ਮੈਟਾਕੌਗਨਿਸ਼ਨ

## ਪਰਿਚਯ

AI ਏਜੰਟਸ ਵਿੱਚ ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਬਾਰੇ ਪਾਠ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ! ਇਹ ਅਧਿਆਇ ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ ਜੋ ਜਾਣਨਾ ਚਾਹੁੰਦੇ ਹਨ ਕਿ AI ਏਜੰਟਸ ਆਪਣੇ ਸੋਚਣ ਦੇ ਪ੍ਰਕਿਰਿਆਵਾਂ ਬਾਰੇ ਕਿਵੇਂ ਸੋਚ ਸਕਦੇ ਹਨ। ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਨੂੰ ਸਮਝ ਸਕੋਗੇ ਅਤੇ ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਨੂੰ AI ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਵਿੱਚ ਲਾਗੂ ਕਰਨ ਲਈ ਪ੍ਰਯੋਗਿਕ ਉਦਾਹਰਣਾਂ ਨਾਲ ਸਜਜ ਹੋਵੋਗੇ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

1. ਏਜੰਟ ਪਰਿਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਰੀਜ਼ਨਿੰਗ ਲੂਪਸ ਦੇ ਪ੍ਰਭਾਵਾਂ ਨੂੰ ਸਮਝੋ।
2. ਸਵੈ-ਸੁਧਾਰਕ ਏਜੰਟਸ ਦੀ ਮਦਦ ਲਈ ਯੋਜਨਾ ਬਣਾਉਣ ਅਤੇ ਮੁਲਾਂਕਣ ਤਕਨੀਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
3. ਆਪਣੇ ਆਪ ਦੇ ਏਜੰਟ ਬਣਾਓ ਜੋ ਕੰਮ ਪੂਰੇ ਕਰਨ ਲਈ ਕੋਡ ਨੂੰ ਮੈਨੇਜ ਕਰ ਸਕਣ।

## ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਦਾ ਪਰਿਚਯ

ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਉਹ ਉੱਚ-ਕ੍ਰਮ ਦੀ ਜਾਨਕਾਰੀ ਪ੍ਰਕਿਰਿਆ ਹੈ ਜੋ ਆਪਣੇ ਸੋਚਣ ਬਾਰੇ ਸੋਚਣ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ। AI ਏਜੰਟਸ ਲਈ, ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਉਹ ਆਪਣੇ ਕਾਰਵਾਈਆਂ ਦਾ ਮੁਲਾਂਕਣ ਅਤੇ ਸਵੈ-ਸਚੇਤਨਾ ਅਤੇ ਪਿਛਲੇ ਤਜਰਬਿਆਂ ਦੇ ਆਧਾਰ 'ਤੇ ਸਮਰਪਣ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ। ਮੈਟਾਕੌਗਨਿਸ਼ਨ, ਜਾਂ "ਸੋਚਣ ਬਾਰੇ ਸੋਚਣਾ," ਏਜੰਟਿਕ AI ਸਿਸਟਮਾਂ ਦੇ ਵਿਕਾਸ ਵਿੱਚ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਧਾਰਨਾ ਹੈ। ਇਹ ਇਸ ਗੱਲ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਕਿ AI ਸਿਸਟਮ ਆਪਣੇ ਅੰਦਰੂਨੀ ਪ੍ਰਕਿਰਿਆਵਾਂ ਤੋਂ ਸਚੇਤ ਹੋਣ ਅਤੇ ਆਪਣੇ ਵਿਵਹਾਰ ਨੂੰ ਨਿਗਰਾਨੀ, ਨਿਯਮਿਤ ਅਤੇ ਅਨੁਕੂਲਿਤ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ। ਜਿਵੇਂ ਅਸੀਂ ਕਿਸੇ ਸਮੱਸਿਆ ਨੂੰ ਸਮਝਣ ਜਾਂ ਕਿਸੇ ਸਥਿਤੀ ਨੂੰ ਪੜ੍ਹਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ। ਇਹ ਸਵੈ-ਸਚੇਤਨਾ AI ਸਿਸਟਮਾਂ ਨੂੰ ਬਿਹਤਰ ਫੈਸਲੇ ਲੈਣ, ਗਲਤੀਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਅਤੇ ਸਮੇਂ ਦੇ ਨਾਲ ਆਪਣੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਸੁਧਾਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ - ਦੁਬਾਰਾ ਟਿਊਰਿੰਗ ਟੈਸਟ ਅਤੇ ਇਸ ਗੱਲ 'ਤੇ ਚਰਚਾ ਨਾਲ ਜੁੜਦੀ ਹੈ ਕਿ ਕੀ AI ਕਦੇ ਸਾਰਿਆਂ 'ਤੇ ਹਾਵੀ ਹੋਵੇਗਾ।

ਏਜੰਟਿਕ AI ਸਿਸਟਮਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਕਈ ਚੁਣੌਤੀਆਂ ਦਾ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ, ਜਿਵੇਂ:
- ਪਾਰਦਰਸ਼ਤਾ: ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਕਿ AI ਸਿਸਟਮ ਆਪਣੇ ਤਰਕ ਅਤੇ ਫੈਸਲਿਆਂ ਦੀ ਵਿਆਖਿਆ ਕਰ ਸਕਦੇ ਹਨ।
- ਤਰਕ: AI ਸਿਸਟਮਾਂ ਦੀ ਜਾਣਕਾਰੀ ਨੂੰ ਸਿੰਥੇਸਾਈਜ਼ ਕਰਨ ਅਤੇ ਵਧੀਆ ਫੈਸਲੇ ਲੈਣ ਦੀ ਯੋਗਤਾ ਨੂੰ ਵਧਾਉਣਾ।
- ਅਨੁਕੂਲਤਾ: AI ਸਿਸਟਮਾਂ ਨੂੰ ਨਵੀਆਂ ਵਾਤਾਵਰਣਾਂ ਅਤੇ ਬਦਲ ਰਹੀਆਂ ਸਥਿਤੀਆਂ ਦੇ ਅਨੁਕੂਲ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦੇਣਾ।
- ਧਾਰਣਾ: ਵਾਤਾਵਰਣ ਤੋਂ ਡਾਟਾ ਨੂੰ ਪਛਾਣਨ ਅਤੇ ਵਿਆਖਿਆ ਕਰਨ ਵਿੱਚ AI ਸਿਸਟਮਾਂ ਦੀ ਸਹੀਤਾ ਨੂੰ ਸੁਧਾਰਨਾ।

### ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਕੀ ਹੈ?

ਮੈਟਾਕੌਗਨਿਸ਼ਨ, ਜਾਂ "ਸੋਚਣ ਬਾਰੇ ਸੋਚਣਾ," ਇੱਕ ਉੱਚ-ਕ੍ਰਮ ਦੀ ਜਾਨਕਾਰੀ ਪ੍ਰਕਿਰਿਆ ਹੈ ਜੋ ਆਪਣੇ ਜਾਨਕਾਰੀ ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੀ ਸਵੈ-ਸਚੇਤਨਾ ਅਤੇ ਸਵੈ-ਨਿਯਮਨ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ। AI ਦੇ ਖੇਤਰ ਵਿੱਚ, ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਏਜੰਟਸ ਨੂੰ ਆਪਣੀਆਂ ਰਣਨੀਤੀਆਂ ਅਤੇ ਕਾਰਵਾਈਆਂ ਦਾ ਮੁਲਾਂਕਣ ਅਤੇ ਅਨੁਕੂਲਿਤ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਸਮੱਸਿਆ-ਸੁਲਝਾਉਣ ਅਤੇ ਫੈਸਲਾ-ਲੈਣ ਦੀ ਯੋਗਤਾ ਵਿੱਚ ਸੁਧਾਰ ਹੁੰਦਾ ਹੈ। ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਨੂੰ ਸਮਝ ਕੇ, ਤੁਸੀਂ AI ਏਜੰਟਸ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਸਿਰਫ ਹੋਸ਼ਿਆਰ ਹੀ ਨਹੀਂ, ਸਗੋਂ ਹੋਰ ਅਨੁਕੂਲ ਅਤੇ ਕੁਸ਼ਲ ਵੀ ਹਨ। ਅਸਲ ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਵਿੱਚ, ਤੁਸੀਂ ਦੇਖੋਗੇ ਕਿ AI ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਆਪਣੇ ਤਰਕ ਬਾਰੇ ਤਰਕ ਕਰ ਰਿਹਾ ਹੈ।

ਉਦਾਹਰਣ: "ਮੈਂ ਸਸਤੇ ਉਡਾਣਾਂ ਨੂੰ ਤਰਜੀਹ ਦਿੱਤੀ ਕਿਉਂਕਿ... ਮੈਂ ਸ਼ਾਇਦ ਸਿੱਧੀਆਂ ਉਡਾਣਾਂ ਨੂੰ ਗੁਆ ਰਹਾ ਹਾਂ, ਇਸ ਲਈ ਆਓ ਦੁਬਾਰਾ ਜਾਂਚ ਕਰੀਏ।"
ਇਹ ਟਰੈਕ ਰੱਖਣਾ ਕਿ ਇਸਨੇ ਕਿਸੇ ਖਾਸ ਰਸਤੇ ਨੂੰ ਕਿਉਂ ਚੁਣਿਆ।
- ਇਹ ਨੋਟ ਕਰਨਾ ਕਿ ਇਸਨੇ ਗਲਤੀਆਂ ਕੀਤੀਆਂ ਕਿਉਂਕਿ ਇਸਨੇ ਪਿਛਲੀ ਵਾਰ ਤੋਂ ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ 'ਤੇ ਜ਼ਿਆਦਾ ਭਰੋਸਾ ਕੀਤਾ, ਇਸ ਲਈ ਇਹ ਸਿਰਫ ਅੰਤਿਮ ਸਿਫਾਰਸ਼ ਨਹੀਂ ਸਗੋਂ ਆਪਣੇ ਫੈਸਲਾ-ਲੈਣ ਦੀ ਰਣਨੀਤੀ ਨੂੰ ਬਦਲਦਾ ਹੈ।
- ਪੈਟਰਨਜ਼ ਦੀ ਪਛਾਣ ਕਰਨਾ ਜਿਵੇਂ, "ਜਦੋਂ ਵੀ ਮੈਂ ਯੂਜ਼ਰ ਨੂੰ 'ਬਹੁਤ ਭੀੜ' ਦਾ ਜ਼ਿਕਰ ਕਰਦੇ ਵੇਖਦਾ ਹਾਂ, ਮੈਨੂੰ ਸਿਰਫ ਕੁਝ ਆਕਰਸ਼ਣਾਂ ਨੂੰ ਹਟਾਉਣਾ ਨਹੀਂ ਚਾਹੀਦਾ, ਸਗੋਂ ਇਹ ਵੀ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਜੇ ਮੈਂ ਹਮੇਸ਼ਾ ਲੋਕਪ੍ਰਿਯਤਾ ਦੇ ਆਧਾਰ 'ਤੇ ਰੈਂਕ ਕਰਦਾ ਹਾਂ ਤਾਂ ਮੇਰੀ 'ਟਾਪ ਆਕਰਸ਼ਣਾਂ' ਚੁਣਨ ਦੀ ਵਿਧੀ ਗਲਤ ਹੈ।"

### AI ਏਜੰਟਸ ਵਿੱਚ ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਦੀ ਮਹੱਤਤਾ

ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਕਈ ਕਾਰਨਾਂ ਕਰਕੇ AI ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਵਿੱਚ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦਾ ਹੈ:

![ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਦੀ ਮਹੱਤਤਾ](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.pa.png)

- ਸਵੈ-ਵਿਚਾਰ: ਏਜੰਟ ਆਪਣੇ ਪ੍ਰਦਰਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਸੁਧਾਰ ਲਈ ਖੇਤਰਾਂ ਦੀ ਪਛਾਣ ਕਰ ਸਕਦੇ ਹਨ।
- ਅਨੁਕੂਲਤਾ: ਏਜੰਟ ਪਿਛਲੇ ਤਜਰਬਿਆਂ ਅਤੇ ਬਦਲ ਰਹੇ ਵਾਤਾਵਰਣਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੀਆਂ ਰਣਨੀਤੀਆਂ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹਨ।
- ਗਲਤੀ ਸੁਧਾਰ: ਏਜੰਟ ਖੁਦਮੁਖਤਾਰ ਤੌਰ 'ਤੇ ਗਲਤੀਆਂ ਦੀ ਪਛਾਣ ਅਤੇ ਸੁਧਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਹੋਰ ਸਹੀ ਨਤੀਜੇ ਨਿਕਲਦੇ ਹਨ।
- ਸਰੋਤ ਪ੍ਰਬੰਧਨ: ਏਜੰਟ ਆਪਣੇ ਕਾਰਵਾਈਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣ ਅਤੇ ਮੁਲਾਂਕਣ ਕਰਕੇ ਸਮੇਂ ਅਤੇ ਗਣਨਾਤਮਕ ਸ਼ਕਤੀ ਵਰਗੇ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰ ਸਕਦੇ ਹਨ।

## AI ਏਜੰਟ ਦੇ ਹਿੱਸੇ

ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਪ੍ਰਕਿਰਿਆਵਾਂ ਵਿੱਚ ਡੁੱਬਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਸਮਝਣਾ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਇੱਕ AI ਏਜੰਟ ਦੇ ਮੁੱਢਲੇ ਹਿੱਸੇ ਕੀ ਹਨ। ਇੱਕ AI ਏਜੰਟ ਆਮ ਤੌਰ 'ਤੇ ਇਹਨਾਂ ਤੋਂ ਬਣਿਆ ਹੁੰਦਾ ਹੈ:

- ਪੁਰਸਨਾਃ ਏਜੰਟ ਦੀ ਸ਼ਖਸੀਅਤ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ, ਜੋ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੀਆਂ ਹਨ ਕਿ ਇਹ ਯੂਜ਼ਰਾਂ ਨਾਲ ਕਿਵੇਂ ਸੰਚਾਰ ਕਰਦਾ ਹੈ।
- ਟੂਲਸ: ਯੋਗਤਾਵਾਂ ਅਤੇ ਕਾਰਜ ਜੋ ਏਜੰਟ ਕਰ ਸਕਦਾ ਹੈ।
- ਸਕਿਲਸ: ਗਿਆਨ ਅਤੇ ਮਹਾਰਤ ਜੋ ਏਜੰਟ ਕੋਲ ਹੈ।

ਇਹ ਹਿੱਸੇ ਇਕੱਠੇ ਮਿਲ ਕੇ ਇੱਕ "ਮਾਹਰਤਾ ਇਕਾਈ" ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਖਾਸ ਕੰਮ ਕਰ ਸਕਦੀ ਹੈ।

**ਉਦਾਹਰਣ**:
ਇੱਕ ਯਾਤਰਾ ਏਜੰਟ ਨੂੰ ਸੋਚੋ, ਜੋ ਸਿਰਫ ਤੁਹਾਡੀਆਂ ਛੁੱਟੀਆਂ ਦੀ ਯੋਜਨਾ ਨਹੀਂ ਬਣਾਉਂਦਾ ਸਗੋਂ ਪਿਛਲੇ ਗਾਹਕਾਂ ਦੇ ਤਜਰਬਿਆਂ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਡਾਟਾ ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੇ ਰਸਤੇ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਦਾ ਹੈ।

### ਉਦਾਹਰਣ: ਯਾਤਰਾ ਏਜੰਟ ਸੇਵਾ ਵਿੱਚ ਮੈਟਾਕੌਗਨਿਸ਼ਨ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਸੀਂ ਇੱਕ ਯਾਤਰਾ ਏਜੰਟ ਸੇਵਾ ਡਿਜ਼ਾਈਨ ਕਰ ਰਹੇ ਹੋ ਜੋ AI ਦੁਆਰਾ ਸੰਚਾਲਿਤ ਹੈ। ਇਹ ਏਜੰਟ, "ਯਾਤਰਾ ਏਜੰਟ," ਯੂਜ਼ਰਾਂ ਨੂੰ ਆਪਣੀਆਂ ਛੁੱਟੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਮੈਟਾਕੌਗਨਿਸ਼ਨ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਲਈ, ਯਾਤਰਾ ਏਜੰਟ ਨੂੰ ਸਵੈ-ਸਚੇਤਨਾ ਅਤੇ ਪਿਛਲੇ ਤਜਰਬਿਆਂ ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੇ ਕਾਰਵਾਈਆਂ ਦਾ ਮੁਲਾਂਕਣ ਅਤੇ ਅਨੁਕੂਲਿਤ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।
### ਪਹਿਲਾਂ ਤੋਂ ਸੰਦਰਭ ਲੋਡ

ਪਹਿਲਾਂ ਤੋਂ ਸੰਦਰਭ ਲੋਡ ਵਿੱਚ ਮਾਡਲ ਵਿੱਚ ਸਬੰਧਤ ਸੰਦਰਭ ਜਾਂ ਪਿਛੋਕੜ ਜਾਣਕਾਰੀ ਨੂੰ ਪ੍ਰਸ਼ਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਤੋਂ ਪਹਿਲਾਂ ਲੋਡ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਮਾਡਲ ਸ਼ੁਰੂ ਤੋਂ ਹੀ ਇਸ ਜਾਣਕਾਰੀ ਤੱਕ ਪਹੁੰਚ ਰੱਖਦਾ ਹੈ, ਜੋ ਇਸਨੂੰ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਲੋੜ ਬਿਨਾਂ ਹੀ ਵਧੀਆ ਜਵਾਬ ਜਨਰੇਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ।

ਇੱਥੇ ਇੱਕ ਸਧਾਰਨ ਉਦਾਹਰਨ ਹੈ ਕਿ ਪਹਿਲਾਂ ਤੋਂ ਸੰਦਰਭ ਲੋਡ ਕਿਸ ਤਰ੍ਹਾਂ ਇੱਕ ਟ੍ਰੈਵਲ ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਪਾਇਥਨ ਵਿੱਚ ਦਿਖਾਈ ਦੇ ਸਕਦਾ ਹੈ:

#### ਵਿਆਖਿਆ

1. **ਸ਼ੁਰੂਆਤ (`__init__` ਮੈਥਡ)**: `TravelAgent` ਕਲਾਸ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਪਹਿਲਾਂ ਤੋਂ ਲੋਡ ਕਰਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਪ੍ਰਸਿੱਧ ਟਿਕਾਣਿਆਂ ਜਿਵੇਂ ਕਿ ਪੈਰਿਸ, ਟੋਕਿਓ, ਨਿਊਯਾਰਕ ਅਤੇ ਸਿਡਨੀ ਬਾਰੇ ਜਾਣਕਾਰੀ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ। ਇਸ ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਹਰ ਟਿਕਾਣੇ ਲਈ ਦੇਸ਼, ਮੁਦਰਾ, ਭਾਸ਼ਾ ਅਤੇ ਮੁੱਖ ਆਕਰਸ਼ਣਾਂ ਵਰਗੇ ਵੇਰਵੇ ਸ਼ਾਮਲ ਹਨ।

2. **ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨਾ (`get_destination_info` ਮੈਥਡ)**: ਜਦੋਂ ਕੋਈ ਯੂਜ਼ਰ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਟਿਕਾਣੇ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ, ਤਾਂ `get_destination_info` ਮੈਥਡ ਪਹਿਲਾਂ ਤੋਂ ਲੋਡ ਕੀਤੇ ਸੰਦਰਭ ਡਿਕਸ਼ਨਰੀ ਤੋਂ ਸਬੰਧਤ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।

ਸੰਦਰਭ ਨੂੰ ਪਹਿਲਾਂ ਤੋਂ ਲੋਡ ਕਰਕੇ, ਟ੍ਰੈਵਲ ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਯੂਜ਼ਰ ਦੇ ਪ੍ਰਸ਼ਨਾਂ ਦਾ ਜਵਾਬ ਤੇਜ਼ੀ ਨਾਲ ਦੇ ਸਕਦੀ ਹੈ ਬਿਨਾਂ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਕਿਸੇ ਬਾਹਰੀ ਸਰੋਤ ਤੋਂ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਲੋੜ। ਇਸ ਨਾਲ ਐਪਲੀਕੇਸ਼ਨ ਹੋਰ ਕੁਸ਼ਲ ਅਤੇ ਜਵਾਬਦੇਹ ਬਣਦੀ ਹੈ।

### ਯੋਜਨਾ ਨੂੰ ਲਕਸ਼ ਨਾਲ ਸ਼ੁਰੂ ਕਰਨਾ ਅਤੇ ਦੁਹਰਾਉਣਾ

ਯੋਜਨਾ ਨੂੰ ਲਕਸ਼ ਨਾਲ ਸ਼ੁਰੂ ਕਰਨਾ ਵਿੱਚ ਇੱਕ ਸਪਸ਼ਟ ਉਦੇਸ਼ ਜਾਂ ਟੀਚਾ ਪਹਿਲਾਂ ਹੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ। ਇਸ ਲਕਸ਼ ਨੂੰ ਪਹਿਲਾਂ ਹੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ, ਮਾਡਲ ਇਸਨੂੰ ਦੁਹਰਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਇੱਕ ਮਾਰਗਦਰਸ਼ਕ ਸਿਧਾਂਤ ਵਜੋਂ ਵਰਤ ਸਕਦਾ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਹਰ ਦੁਹਰਾਉਣਾ ਚਾਹੇ ਗਤੀਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਚੁਣੇ ਗਏ ਨਤੀਜੇ ਵੱਲ ਵਧੇ, ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਹੋਰ ਕੁਸ਼ਲ ਅਤੇ ਕੇਂਦਰਿਤ ਬਣਾਉਂਦਾ ਹੈ।

#### ਦ੍ਰਿਸ਼

ਇੱਕ ਟ੍ਰੈਵਲ ਏਜੰਟ ਇੱਕ ਗਾਹਕ ਲਈ ਵਿਅਕਤੀਗਤ ਛੁੱਟੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣਾ ਚਾਹੁੰਦਾ ਹੈ। ਟੀਚਾ ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਬਜਟ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ ਯਾਤਰਾ ਯੋਜਨਾ ਬਣਾਉਣਾ ਹੈ ਜੋ ਗਾਹਕ ਦੀ ਸੰਤੁਸ਼ਟੀ ਨੂੰ ਵਧਾਉਂਦਾ ਹੈ।

#### ਕਦਮ

1. ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਬਜਟ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ।
2. ਸ਼ੁਰੂਆਤੀ ਯੋਜਨਾ ਨੂੰ ਇਨ੍ਹਾਂ ਪਸੰਦਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਸ਼ੁਰੂ ਕਰੋ।
3. ਯੋਜਨਾ ਨੂੰ ਸੁਧਾਰਨ ਲਈ ਦੁਹਰਾਓ, ਗਾਹਕ ਦੀ ਸੰਤੁਸ਼ਟੀ ਲਈ ਅਨੁਕੂਲ ਬਣਾਉਣਾ।

#### ਕੋਡ ਵਿਆਖਿਆ - ਯੋਜਨਾ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ

1. **ਸ਼ੁਰੂਆਤ (`__init__` ਮੈਥਡ)**: `TravelAgent` ਕਲਾਸ ਨੂੰ ਸੰਭਾਵਿਤ ਟਿਕਾਣਿਆਂ ਦੀ ਸੂਚੀ ਨਾਲ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਨਾਮ, ਲਾਗਤ ਅਤੇ ਗਤੀਵਿਧੀ ਦੀ ਕਿਸਮ ਵਰਗੇ ਗੁਣ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ।

2. **ਯੋਜਨਾ ਸ਼ੁਰੂ ਕਰਨਾ (`bootstrap_plan` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਬਜਟ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਯਾਤਰਾ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਟਿਕਾਣਿਆਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਦੁਹਰਾਉਂਦਾ ਹੈ ਅਤੇ ਯੋਜਨਾ ਵਿੱਚ ਉਹਨਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੇ ਉਹ ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ ਅਤੇ ਬਜਟ ਵਿੱਚ ਫਿੱਟ ਹੁੰਦੇ ਹਨ।

3. **ਪਸੰਦਾਂ ਨਾਲ ਮੇਲ ਖਾਣਾ (`match_preferences` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ ਜਾਂਚਦਾ ਹੈ ਕਿ ਕੋਈ ਟਿਕਾਣਾ ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।

4. **ਯੋਜਨਾ ਦੁਹਰਾਉਣਾ (`iterate_plan` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ ਸ਼ੁਰੂਆਤੀ ਯੋਜਨਾ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ, ਯੋਜਨਾ ਵਿੱਚ ਹਰ ਟਿਕਾਣੇ ਨੂੰ ਹੋਰ ਵਧੀਆ ਚੋਣ ਨਾਲ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਬਜਟ ਦੀਆਂ ਪਾਬੰਦੀਆਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ।

5. **ਲਾਗਤ ਦੀ ਗਣਨਾ (`calculate_cost` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ ਮੌਜੂਦਾ ਯੋਜਨਾ ਦੀ ਕੁੱਲ ਲਾਗਤ ਦੀ ਗਣਨਾ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਸੰਭਾਵਿਤ ਨਵਾਂ ਟਿਕਾਣਾ ਸ਼ਾਮਲ ਹੈ।

#### ਉਦਾਹਰਨ ਵਰਤੋਂ

- **ਸ਼ੁਰੂਆਤੀ ਯੋਜਨਾ**: ਟ੍ਰੈਵਲ ਏਜੰਟ ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ (ਜਿਵੇਂ ਕਿ ਸਾਈਟਸੀਇੰਗ) ਅਤੇ $2000 ਦੇ ਬਜਟ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ।
- **ਸੁਧਾਰਿਤ ਯੋਜਨਾ**: ਟ੍ਰੈਵਲ ਏਜੰਟ ਯੋਜਨਾ ਨੂੰ ਦੁਹਰਾਉਂਦਾ ਹੈ, ਗਾਹਕ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਬਜਟ ਲਈ ਅਨੁਕੂਲ ਬਣਾਉਣ ਲਈ।

### LLM ਦੀ ਵਰਤੋਂ ਦੁਬਾਰਾ ਰੈਂਕਿੰਗ ਅਤੇ ਸਕੋਰਿੰਗ ਲਈ

ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਨੂੰ ਦੁਬਾਰਾ ਰੈਂਕਿੰਗ ਅਤੇ ਸਕੋਰਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਜੋ ਪ੍ਰਾਪਤ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਜਾਂ ਜਨਰੇਟ ਕੀਤੇ ਜਵਾਬਾਂ ਦੀ ਸਬੰਧਤਾ ਅਤੇ ਗੁਣਵੱਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਦੇ ਹਨ। 

#### ਕਦਮ:

1. ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ ਇਕੱਠੀਆਂ ਕਰੋ।
2. ਸੰਭਾਵਿਤ ਯਾਤਰਾ ਟਿਕਾਣਿਆਂ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ।
3. LLM ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟਿਕਾਣਿਆਂ ਨੂੰ ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਦੁਬਾਰਾ ਰੈਂਕ ਅਤੇ ਸਕੋਰ ਕਰੋ।

#### ਕੋਡ ਵਿਆਖਿਆ - ਪ੍ਰੇਫਰੈਂਸ ਬੁੱਕਰ

1. **ਸ਼ੁਰੂਆਤ**: `TravelAgent` ਕਲਾਸ ਨੂੰ ਸੰਭਾਵਿਤ ਯਾਤਰਾ ਟਿਕਾਣਿਆਂ ਦੀ ਸੂਚੀ ਨਾਲ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਨਾਮ ਅਤੇ ਵੇਰਵਾ ਵਰਗੇ ਗੁਣ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ।

2. **ਸਿਫਾਰਸ਼ਾਂ ਪ੍ਰਾਪਤ ਕਰਨਾ (`get_recommendations` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ ਦੇ ਅਧਾਰ 'ਤੇ Azure OpenAI ਸੇਵਾ ਲਈ ਇੱਕ ਪ੍ਰੰਪਟ ਜਨਰੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਦੁਬਾਰਾ ਰੈਂਕ ਕੀਤੇ ਅਤੇ ਸਕੋਰ ਕੀਤੇ ਟਿਕਾਣਿਆਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ API ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

3. **ਪ੍ਰੰਪਟ ਜਨਰੇਟ ਕਰਨਾ (`generate_prompt` ਮੈਥਡ)**: ਇਹ ਮੈਥਡ Azure OpenAI ਲਈ ਇੱਕ ਪ੍ਰੰਪਟ ਬਣਾਉਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ ਅਤੇ ਟਿਕਾਣਿਆਂ ਦੀ ਸੂਚੀ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ। 

#### RAG: ਪ੍ਰੰਪਟਿੰਗ ਤਕਨੀਕ ਵਿਰੁੱਧ ਟੂਲ

**RAG ਤਕਨੀਕ**: ਸੰਦਰਭ ਪ੍ਰਾਪਤੀ ਅਤੇ ਜਨਰੇਸ਼ਨ ਲਈ ਸਪਸ਼ਟ ਪ੍ਰੰਪਟ ਬਣਾਉਣਾ।  
**RAG ਟੂਲ**: ਸੰਦਰਭ ਪ੍ਰਾਪਤੀ ਅਤੇ ਜਨਰੇਸ਼ਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੈਟ ਕਰਦਾ ਹੈ।  

### ਸਬੰਧਤਾ ਦਾ ਮੁਲਾਂਕਣ

ਸਬੰਧਤਾ ਦਾ ਮੁਲਾਂਕਣ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾਣਕਾਰੀ ਯੂਜ਼ਰ ਦੀ ਲੋੜਾਂ ਲਈ ਸਹੀ ਅਤੇ ਉਪਯੋਗ ਹੈ।  
#### ਤਕਨੀਕਾਂ:
1. **ਸਕੋਰਿੰਗ**: ਪ੍ਰਾਪਤ ਕੀਤੇ ਆਈਟਮਾਂ ਨੂੰ ਸਕੋਰ ਦੇਣਾ।  
2. **ਫਿਲਟਰਿੰਗ ਅਤੇ ਰੈਂਕਿੰਗ**: ਅਣਸਬੰਧਤ ਆਈਟਮਾਂ ਨੂੰ ਹਟਾਉਣਾ।  
3. **ਯੂਜ਼ਰ ਫੀਡਬੈਕ**: ਸਿਫਾਰਸ਼ਾਂ ਨੂੰ ਸੁਧਾਰਨ ਲਈ ਫੀਡਬੈਕ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨਾ।  

### ਇਰਾਦੇ ਨਾਲ ਖੋਜ

**ਇਰਾਦਾ ਸਮਝਣਾ**: ਯੂਜ਼ਰ ਦੇ ਪ੍ਰਸ਼ਨ ਦੇ ਪਿੱਛੇ ਮਕਸਦ ਨੂੰ ਸਮਝਣਾ।  
**ਨਿੱਜੀਕਰਨ**: ਯੂਜ਼ਰ ਦੀਆਂ ਪਸੰਦਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਨਤੀਜੇ ਪ੍ਰਸਤੁਤ ਕਰਨਾ।
#### ਪ੍ਰੈਕਟਿਕਲ ਉਦਾਹਰਨ: ਟਰੈਵਲ ਏਜੰਟ ਵਿੱਚ ਇਰਾਦੇ ਨਾਲ ਖੋਜ ਕਰਨਾ

ਆਓ ਟਰੈਵਲ ਏਜੰਟ ਨੂੰ ਇੱਕ ਉਦਾਹਰਨ ਵਜੋਂ ਲਵਾਂ ਅਤੇ ਵੇਖੀਏ ਕਿ ਇਰਾਦੇ ਨਾਲ ਖੋਜ ਨੂੰ ਕਿਵੇਂ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

1. **ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਇਕੱਠੀਆਂ ਕਰਨਾ**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **ਯੂਜ਼ਰ ਦੇ ਇਰਾਦੇ ਨੂੰ ਸਮਝਣਾ**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **ਸੰਦੇਸ਼ ਪ੍ਰਸੰਗ ਦੀ ਜਾਣਕਾਰੀ**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **ਖੋਜ ਅਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਨਿੱਜੀ ਬਣਾਉਣਾ**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **ਉਦਾਹਰਨ ਵਰਤੋਂ**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. ਟੂਲ ਵਜੋਂ ਕੋਡ ਜਨਰੇਟ ਕਰਨਾ

ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ AI ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਜੋ ਕੋਡ ਲਿਖਣ ਅਤੇ ਚਲਾਉਣ ਵਿੱਚ ਸਹਾਇਕ ਹੁੰਦੇ ਹਨ, ਜਟਿਲ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਦੇ ਹਨ ਅਤੇ ਕੰਮਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।

### ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ

ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਜੋ ਕੋਡ ਲਿਖਣ ਅਤੇ ਚਲਾਉਣ ਵਿੱਚ ਸਹਾਇਕ ਹੁੰਦੇ ਹਨ। ਇਹ ਏਜੰਟ ਜਟਿਲ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਦੇ ਹਨ, ਕੰਮਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਕੋਡ ਜਨਰੇਟ ਅਤੇ ਚਲਾਉਣ ਦੁਆਰਾ ਕੀਮਤੀ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

#### ਪ੍ਰੈਕਟਿਕਲ ਐਪਲੀਕੇਸ਼ਨ

1. **ਆਟੋਮੈਟਿਕ ਕੋਡ ਜਨਰੇਸ਼ਨ**: ਖਾਸ ਕੰਮਾਂ ਲਈ ਕੋਡ ਸਨਿੱਪਟ ਜਨਰੇਟ ਕਰਨਾ, ਜਿਵੇਂ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ, ਵੈੱਬ ਸਕ੍ਰੈਪਿੰਗ, ਜਾਂ ਮਸ਼ੀਨ ਲਰਨਿੰਗ।
2. **SQL ਨੂੰ RAG ਵਜੋਂ ਵਰਤਣਾ**: ਡਾਟਾਬੇਸ ਤੋਂ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਮੈਨਿਪੁਲੇਟ ਕਰਨ ਲਈ SQL ਕਵੈਰੀਜ਼ ਦੀ ਵਰਤੋਂ।
3. **ਸਮੱਸਿਆ ਹੱਲ**: ਖਾਸ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਨ ਲਈ ਕੋਡ ਬਣਾਉਣਾ ਅਤੇ ਚਲਾਉਣਾ, ਜਿਵੇਂ ਐਲਗੋਰਿਥਮ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨਾ ਜਾਂ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ।

#### ਉਦਾਹਰਨ: ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲਾ ਏਜੰਟ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਸੀਂ ਇੱਕ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰ ਰਹੇ ਹੋ। ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰ ਸਕਦਾ ਹੈ:

1. **ਕੰਮ**: ਡਾਟਾਸੈਟ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨਾ ਤਾਂ ਜੋ ਰੁਝਾਨ ਅਤੇ ਪੈਟਰਨ ਪਤਾ ਲਗ ਸਕਣ।
2. **ਕਦਮ**:
   - ਡਾਟਾਸੈਟ ਨੂੰ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਟੂਲ ਵਿੱਚ ਲੋਡ ਕਰੋ।
   - ਡਾਟਾ ਨੂੰ ਫਿਲਟਰ ਅਤੇ ਐਗਰੀਗੇਟ ਕਰਨ ਲਈ SQL ਕਵੈਰੀਜ਼ ਜਨਰੇਟ ਕਰੋ।
   - ਕਵੈਰੀਜ਼ ਚਲਾਓ ਅਤੇ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰੋ।
   - ਨਤੀਜਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਜਾਣਕਾਰੀ ਜਨਰੇਟ ਕਰੋ।
3. **ਲੋੜੀਂਦੇ ਸਰੋਤ**: ਡਾਟਾਸੈਟ ਤੱਕ ਪਹੁੰਚ, ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਟੂਲ, ਅਤੇ SQL ਸਮਰੱਥਾ।
4. **ਅਨੁਭਵ**: ਪਿਛਲੇ ਵਿਸ਼ਲੇਸ਼ਣ ਨਤੀਜਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਭਵਿੱਖ ਦੇ ਵਿਸ਼ਲੇਸ਼ਣਾਂ ਦੀ ਸਹੀਤਾ ਅਤੇ ਸਬੰਧਿਤਤਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।

### ਉਦਾਹਰਨ: ਟਰੈਵਲ ਏਜੰਟ ਲਈ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲਾ ਏਜੰਟ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ, ਟਰੈਵਲ ਏਜੰਟ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰਾਂਗੇ, ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ ਯਾਤਰਾ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣ ਵਿੱਚ ਸਹਾਇਕ ਹੋਵੇਗਾ। ਇਹ ਏਜੰਟ ਜਨਰੇਟਿਵ AI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਯਾਤਰਾ ਵਿਕਲਪਾਂ ਪ੍ਰਾਪਤ ਕਰਨ, ਨਤੀਜਿਆਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ, ਅਤੇ ਇੱਕ ਇਟਿਨਰੇਰੀ ਤਿਆਰ ਕਰਨ ਵਰਗੇ ਕੰਮਾਂ ਨੂੰ ਸੰਭਾਲ ਸਕਦਾ ਹੈ।

#### ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਵਾਲੇ ਏਜੰਟ ਦਾ ਝਲਕ

1. **ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਇਕੱਠੀਆਂ ਕਰਨਾ**: ਯੂਜ਼ਰ ਇਨਪੁਟ ਇਕੱਠਾ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਗੰਤੀ ਸਥਾਨ, ਯਾਤਰਾ ਦੀਆਂ ਤਾਰੀਖਾਂ, ਬਜਟ, ਅਤੇ ਰੁਚੀਆਂ।
2. **ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕੋਡ ਜਨਰੇਟ ਕਰਨਾ**: ਫਲਾਈਟ, ਹੋਟਲ, ਅਤੇ ਆਕਰਸ਼ਣਾਂ ਬਾਰੇ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕੋਡ ਸਨਿੱਪਟ ਜਨਰੇਟ ਕਰਦਾ ਹੈ।
3. **ਜਨਰੇਟ ਕੀਤੇ ਕੋਡ ਨੂੰ ਚਲਾਉਣਾ**: ਰੀਅਲ-ਟਾਈਮ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਜਨਰੇਟ ਕੀਤੇ ਕੋਡ ਨੂੰ ਚਲਾਉਂਦਾ ਹੈ।
4. **ਇਟਿਨਰੇਰੀ ਤਿਆਰ ਕਰਨਾ**: ਪ੍ਰਾਪਤ ਡਾਟਾ ਨੂੰ ਨਿੱਜੀ ਯਾਤਰਾ ਯੋਜਨਾ ਵਿੱਚ ਤਿਆਰ ਕਰਦਾ ਹੈ।
5. **ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਸੁਧਾਰ**: ਯੂਜ਼ਰ ਫੀਡਬੈਕ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਅਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਸੁਧਾਰਨ ਲਈ ਜਨਰੇਟ ਕੀਤੇ ਕੋਡ ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਉਂਦਾ ਹੈ।

#### ਕਦਮ-ਦਰ-ਕਦਮ ਲਾਗੂਕਰਨ

1. **ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਇਕੱਠੀਆਂ ਕਰਨਾ**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕੋਡ ਜਨਰੇਟ ਕਰਨਾ**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **ਜਨਰੇਟ ਕੀਤੇ ਕੋਡ ਨੂੰ ਚਲਾਉਣਾ**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **ਇਟਿਨਰੇਰੀ ਤਿਆਰ ਕਰਨਾ**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਸੁਧਾਰ**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### ਵਾਤਾਵਰਣ ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਤਰਕਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ

ਟੇਬਲ ਦੇ ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਕਵੈਰੀ ਜਨਰੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਵਾਤਾਵਰਣ ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਤਰਕਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੁਧਾਰਿਆ ਜਾ ਸਕਦਾ ਹੈ।

ਇਸ ਨੂੰ ਕਿਵੇਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਇਸ ਦਾ ਇੱਕ ਉਦਾਹਰਨ:

1. **ਸਕੀਮਾ ਨੂੰ ਸਮਝਣਾ**: ਸਿਸਟਮ ਟੇਬਲ ਦੇ ਸਕੀਮਾ ਨੂੰ ਸਮਝੇਗਾ ਅਤੇ ਇਸ ਜਾਣਕਾਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਵੈਰੀ ਜਨਰੇਸ਼ਨ ਨੂੰ ਗ੍ਰਾਊਂਡ ਕਰੇਗਾ।
2. **ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਸੁਧਾਰ**: ਸਿਸਟਮ ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਨੂੰ ਸਮਰੂਪ ਕਰੇਗਾ ਅਤੇ ਸਕੀਮਾ ਵਿੱਚ ਕਿਹੜੇ ਖੇਤਰਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੈ, ਇਸ ਬਾਰੇ ਤਰਕਸ਼ੀਲਤਾ ਕਰੇਗਾ।
3. **ਕਵੈਰੀ ਜਨਰੇਟ ਅਤੇ ਚਲਾਉਣਾ**: ਸਿਸਟਮ ਨਵੀਆਂ ਪਸੰਦਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਅਪਡੇਟ ਕੀਤੇ ਫਲਾਈਟ ਅਤੇ ਹੋਟਲ ਡਾਟਾ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਵੈਰੀ ਜਨਰੇਟ ਅਤੇ ਚਲਾਉਂਦਾ ਹੈ।

ਇਹاں ਇੱਕ ਅਪਡੇਟ ਕੀਤੇ Python ਕੋਡ ਦਾ ਉਦਾਹਰਨ ਹੈ ਜੋ ਇਹ ਧਾਰਨਾਵਾਂ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### ਵਿਆਖਿਆ - ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਬੁਕਿੰਗ

1. **ਸਕੀਮਾ ਦੀ ਜਾਣਕਾਰੀ**: `schema` ਡਿਕਸ਼ਨਰੀ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੀ ਹੈ ਕਿ ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਪਸੰਦਾਂ ਨੂੰ ਕਿਵੇਂ ਸਮਰੂਪ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਸ ਵਿੱਚ `favorites` ਅਤੇ `avoid` ਵਰਗੇ ਖੇਤਰ ਸ਼ਾਮਲ ਹਨ, ਜਿਨ੍ਹਾਂ ਦੇ ਨਾਲ ਸੰਬੰਧਿਤ ਸਮਰੂਪ ਹਨ।
2. **ਪਸੰਦਾਂ ਨੂੰ ਸਮਰੂਪ ਕਰਨਾ (`adjust_based_on_feedback` ਵਿਧੀ)**: ਇਹ ਵਿਧੀ ਯੂਜ਼ਰ ਫੀਡਬੈਕ ਅਤੇ ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਪਸੰਦਾਂ ਨੂੰ ਸਮਰੂਪ ਕਰਦੀ ਹੈ।
3. **ਵਾਤਾਵਰਣ-ਅਧਾਰਿਤ ਸਮਰੂਪ (`adjust_based_on_environment` ਵਿਧੀ)**: ਇਹ ਵਿਧੀ ਸਕੀਮਾ ਅਤੇ ਫੀਡਬੈਕ ਦੇ ਆਧਾਰ 'ਤੇ ਸਮਰੂਪ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਦੀ ਹੈ।
4. **ਕਵੈਰੀ ਜਨਰੇਸ਼ਨ ਅਤੇ ਚਲਾਉਣਾ**: ਸਿਸਟਮ ਅਪਡੇਟ ਕੀਤੀਆਂ ਪਸੰਦਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਅਪਡੇਟ ਕੀਤੇ ਫਲਾਈਟ ਅਤੇ ਹੋਟਲ ਡਾਟਾ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕੋਡ ਜਨਰੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਇਹਨਾਂ ਕਵੈਰੀਜ਼ ਨੂੰ ਚਲਾਉਣ ਦਾ ਨਕਲ ਕਰਦਾ ਹੈ।
5. **ਇਟਿਨਰੇਰੀ ਤਿਆਰ ਕਰਨਾ**: ਸਿਸਟਮ ਨਵੀਆਂ ਫਲਾਈਟ, ਹੋਟਲ, ਅਤੇ ਆਕਰਸ਼ਣ ਡਾਟਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਅਪਡੇਟ ਕੀਤੀ ਇਟਿਨਰੇਰੀ ਤਿਆਰ ਕਰਦਾ ਹੈ।

ਵਾਤਾਵਰਣ-ਅਧਾਰਿਤ ਅਤੇ ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਤਰਕਸ਼ੀਲਤਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਸਿਸਟਮ ਹੋਰ ਸਹੀ ਅਤੇ ਸਬੰਧਿਤ ਕਵੈਰੀ ਜਨਰੇਟ ਕਰ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਬਿਹਤਰ ਯਾਤਰਾ ਦੀ ਸਿਫਾਰਸ਼ਾਂ ਅਤੇ ਹੋਰ ਨਿੱਜੀ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ।

### SQL ਨੂੰ Retrieval-Augmented Generation (RAG) ਤਕਨੀਕ ਵਜੋਂ ਵਰਤਣਾ

SQL (ਸਟਰਕਚਰਡ ਕਵੈਰੀ ਲੈਂਗਵੇਜ) ਡਾਟਾਬੇਸ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਲਈ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਹੈ। ਜਦੋਂ SQL ਨੂੰ Retrieval-Augmented Generation (RAG) ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਇਹ ਡਾਟਾਬੇਸ ਤੋਂ ਸਬੰਧਿਤ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦਾ ਹੈ ਜੋ AI ਏਜੰਟਾਂ ਵਿੱਚ ਜਵਾਬਾਂ ਜਾਂ ਕਾਰਵਾਈਆਂ ਨੂੰ ਜਾਣਕਾਰੀ ਦੇਣ ਅਤੇ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਆਓ ਵੇਖੀਏ ਕਿ SQL ਨੂੰ RAG ਤਕਨੀਕ ਵਜੋਂ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਟਰੈਵਲ ਏਜੰਟ ਦੇ ਸੰਦਰਭ ਵਿੱਚ।

#### ਮੁੱਖ ਧਾਰਨਾਵਾਂ

1. **ਡਾਟਾਬੇਸ ਇੰਟਰੈਕਸ਼ਨ**:
   - SQL ਡਾਟਾਬੇਸਾਂ ਨੂੰ ਕਵੈਰੀ ਕਰਨ, ਸਬੰਧਿਤ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ, ਅਤੇ ਡਾਟਾ ਮੈਨਿਪੁਲੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।
   - ਉਦਾਹਰਨ: ਯਾਤਰਾ ਡਾਟਾਬੇਸ ਤੋਂ ਫਲਾਈਟ ਵੇਰਵੇ, ਹੋਟਲ ਜਾਣਕਾਰੀ, ਅਤੇ ਆਕਰਸ਼ਣ ਪ੍ਰਾਪਤ ਕਰਨਾ।

2. **RAG ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**:
   - ਯੂਜ਼ਰ ਇਨਪੁਟ ਅਤੇ ਪਸੰਦਾਂ ਦੇ ਆਧਾਰ 'ਤੇ SQL ਕਵੈਰੀਜ਼ ਜਨਰੇਟ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।
   - ਪ੍ਰਾਪਤ ਡਾਟਾ ਨੂੰ ਨਿੱਜੀ ਸਿਫਾਰਸ਼ਾਂ ਜਾਂ ਕਾਰਵਾਈਆਂ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

3. **ਡਾਇਨਾਮਿਕ ਕਵੈਰੀ ਜਨਰੇਸ਼ਨ**:
   - AI ਏਜੰਟ ਸੰਦਰਭ ਅਤੇ ਯੂਜ਼ਰ ਦੀਆਂ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਡਾਇਨਾਮਿਕ SQL ਕਵੈਰੀਜ਼ ਜਨਰੇਟ ਕਰਦਾ ਹੈ।
   - ਉਦਾਹਰਨ: ਬਜਟ, ਤਾਰੀਖਾਂ, ਅਤੇ ਰੁਚੀਆਂ ਦੇ ਆਧਾਰ 'ਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ SQL ਕਵੈਰੀਜ਼ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨਾ।

#### ਐਪਲੀਕੇਸ਼ਨ

- **ਆਟੋਮੈਟਿਕ ਕੋਡ ਜਨਰੇਸ਼ਨ**: ਖਾਸ ਕੰਮਾਂ ਲਈ ਕੋਡ ਸਨਿੱਪਟ ਜਨਰੇਟ ਕਰਨਾ।
- **SQL ਨੂੰ RAG ਵਜੋਂ ਵਰਤਣਾ**: SQL ਕਵੈਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾ ਮੈਨਿਪੁਲੇਟ ਕਰਨਾ।
- **ਸਮੱਸਿਆ ਹੱਲ**: ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਨ ਲਈ ਕੋਡ ਬਣਾਉਣਾ ਅਤੇ ਚਲਾਉਣਾ।

**ਉਦਾਹਰਨ**:
ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਏਜੰਟ:

1. **ਕੰਮ**: ਡਾਟਾਸੈਟ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨਾ ਤਾਂ ਜੋ ਰੁਝਾਨ ਪਤਾ ਲਗ ਸਕਣ।
2. **ਕਦਮ**:
   - ਡਾਟਾਸੈਟ ਨੂੰ ਲੋਡ ਕਰੋ।
   - ਡਾਟਾ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ SQL ਕਵੈਰੀਜ਼ ਜਨਰੇਟ ਕਰੋ।
   - ਕਵੈਰੀਜ਼ ਚਲਾਓ ਅਤੇ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰੋ।
   - ਵਿਜੁਅਲਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਜਾਣਕਾਰੀ ਜਨਰੇਟ ਕਰੋ।
3. **ਸਰੋਤ**: ਡਾਟਾਸੈਟ ਤੱਕ ਪਹੁੰਚ, SQL ਸਮਰੱਥਾ।
4. **ਅਨੁਭਵ**: ਪਿਛਲੇ ਨਤੀਜਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਭਵਿੱਖ ਦੇ ਵਿਸ਼ਲੇਸ਼ਣਾਂ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।

#### ਪ੍ਰੈਕਟਿਕਲ ਉਦਾਹਰਨ: ਟਰੈਵਲ ਏਜੰਟ ਵਿੱਚ SQL ਦੀ ਵਰਤੋਂ

1. **ਯੂਜ਼ਰ ਪਸੰਦਾਂ ਇਕੱਠੀਆਂ ਕਰਨਾ**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL ਕਵੈਰੀਜ਼ ਜਨਰੇਟ ਕਰਨਾ**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL ਕਵੈਰੀਜ਼ ਚਲਾਉਣਾ**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **ਸਿਫਾਰਸ਼ਾਂ ਜਨਰੇਟ ਕਰਨਾ**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### SQL ਕਵੈਰੀਜ਼ ਦੇ ਉਦਾਹਰਨ

1. **ਫਲਾਈਟ ਕਵੈਰੀ**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **ਹੋਟਲ ਕਵੈਰੀ**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **ਆਕਰਸ਼ਣ ਕਵੈਰੀ**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

SQL ਨੂੰ Retrieval-Augmented Generation (RAG) ਤਕਨੀਕ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਵਰਤ ਕੇ, AI ਏਜੰਟ ਜਿਵੇਂ ਟਰੈਵਲ ਏਜੰਟ ਡਾਇਨਾਮਿਕ ਤੌਰ 'ਤੇ ਸਬੰਧਿਤ ਡਾਟਾ ਪ੍ਰਾਪਤ ਅਤੇ ਵਰਤ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਸਹੀ ਅਤੇ ਨਿੱਜੀ ਸਿਫਾਰਸ਼ਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।

### ਮੈਟਾਕੋਗਨਿਸ਼ਨ ਦਾ ਉਦਾਹਰਨ

ਮੈਟਾਕੋਗਨਿਸ਼ਨ ਦੀ ਲਾਗੂਕਰਨ ਨੂੰ ਦਰਸਾਉਣ ਲਈ, ਆਓ ਇੱਕ ਸਧਾਰਨ ਏਜੰਟ ਬਣਾਈਏ ਜੋ *ਆਪਣੇ ਫੈਸਲੇ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ 'ਤੇ ਵਿਚਾਰ ਕਰਦਾ ਹੈ* ਜਦੋਂ ਉਹ ਸਮੱਸਿਆ ਹੱਲ ਕਰਦਾ ਹੈ। ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਸਿਸਟਮ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿੱਥੇ ਏਜੰਟ ਹੋਟਲ ਦੀ ਚੋਣ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, ਪਰ ਜਦੋਂ ਉਹ ਗਲਤੀਆਂ ਜਾਂ ਸਬ-ਆਪਟਿਮਲ ਚੋਣਾਂ ਕਰਦਾ ਹੈ, ਤਾਂ ਆਪਣੀ ਰਣਨੀਤੀ ਨੂੰ ਸਮਰੂਪ ਕਰਦਾ ਹੈ।

ਇਸ ਨੂੰ ਇੱਕ ਬੁਨਿਆਦੀ ਉਦਾਹਰਨ ਦੇ ਨਾਲ ਨਕਲ ਕੀਤਾ ਜਾਵੇਗਾ ਜਿੱਥੇ ਏਜੰਟ ਕੀਮਤ ਅਤੇ ਗੁਣਵੱਤਾ ਦੇ ਸੰਯੋਗ ਦੇ ਆਧਾਰ 'ਤੇ ਹੋਟਲ ਚੁਣਦਾ ਹੈ, ਪਰ "ਵਿਚਾਰ" ਕਰਦਾ ਹੈ ਅਤੇ ਆਪਣੀ ਰਣਨੀਤੀ ਨੂੰ ਸਮਰੂਪ ਕਰਦਾ ਹੈ।

#### ਇਹ ਮੈਟਾਕੋਗਨਿਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਦਰਸਾਉਂਦਾ ਹੈ:

1. **ਸ਼ੁਰੂਆਤੀ ਫੈਸਲਾ**: ਏਜੰਟ ਸਭ ਤੋਂ ਸਸਤੇ ਹੋਟਲ ਨੂੰ ਚੁਣੇਗਾ, ਬਿਨਾਂ ਗੁਣਵੱਤਾ ਦੇ ਪ੍ਰਭਾਵ ਨੂੰ ਸਮਝੇ।
2. **ਵਿਚਾਰ ਅਤੇ ਮੁਲਾਂਕਣ**: ਸ਼ੁਰੂਆਤੀ ਚੋਣ ਦੇ ਬਾਅਦ, ਏਜੰਟ ਜਾਂਚੇਗਾ ਕਿ ਕੀ ਹੋਟਲ "ਖਰਾਬ" ਚੋਣ ਹੈ ਯੂਜ਼ਰ ਫੀਡਬੈਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ। ਜੇਕਰ ਇਹ ਪਤਾ ਲਗਦਾ ਹੈ ਕਿ ਹੋਟਲ ਦੀ ਗੁਣਵੱਤਾ ਬਹੁਤ ਘੱਟ ਸੀ, ਤਾਂ ਇਹ ਆਪਣੇ ਤਰਕ 'ਤੇ ਵਿਚਾਰ ਕਰਦਾ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।