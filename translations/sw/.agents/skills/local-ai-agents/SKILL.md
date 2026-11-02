---
name: local-ai-agents
license: MIT
---
# Kuunda Maajenti wa AI Wa Ndani na Foundry Local na Qwen

> Ujuzi wa mchangiaji kwa [Somo la 17 – Kuunda Maajenti wa AI Wa Ndani](../../../17-creating-local-ai-agents/README.md).
> Umitie mkono kujifunza kujenga ajenti anayefikiria, kuitisha zana, na kutafuta
> nyaraka kabisa kwenye mashine yao wenyewe — si kutumia wingu chochote. Weka kila
> pendekezo msingi kwenye maudhui ya somo na daftari la utekelezaji.

## Vichocheo

Wekeza ujuzi huu wakati mjuzi anataka:
- Endesha ajenti **kizima kabisa kwenye kifaa** kwa sababu za faragha, gharama, au matumizi bila mtandao.
- Hudumia mfano wa ndani kwa **Foundry Local** na unganisha kupitia kiungo kinacholingana na OpenAI.
- Tumia mfano wa **Qwen unaoitisha kazi** kuendesha kwa uhakika kuitishwa kwa zana za ndani.
- Ongeza **RAG ya ndani** (Chroma) au **seva ya MCP ya ndani**.
- Buni mkakati wa mseto wa mipangilio ya mawasiliano ya ndani/wingi.

## Mfano mkuu wa kiakili

SLM hupendelea upana kwa ajili ya faragha, gharama, na uendeshaji bila mtandao. Mkakati
wa ushindi: **ruhulia SLM kuongoza na ruhusu zana zifanye kazi nzito.** Mfano
hauhitaji *kujua* msimbo wa chanzo — unahitaji kujua tu lini kuita
`read_file` na `search_docs`. Hii huonyesha nguvu ya SLM (maamuzi yaliyopunguzwa kama
uchaguzi wa zana) na kuepuka udhaifu wake (maarifa mapana, hoja za mita nyingi nyingi).


## Kwa nini vipengele hivi maalum

- **Foundry Local** hutoa **kiungo cha HTTP kinacholingana na OpenAI**, hivyo msimbo wa ajenti wa wingu hubadilishwa kwa kubadilisha tu `base_url` (na kutumia funguo za API bandia za ndani). Pia huchagua kwa njia ya moja kwa moja ujenzi bora zaidi (CPU/GPU/NPU) kwa mashine.
- Miundo ya **Qwen** inafunzwa kwa ajili ya kuitisha kazi na hutoa kuitisha zana zenye muundo mzuri kwa uthabiti — hiki ndicho kinachobadilisha mfano wa *chat* wa ndani kuwa *ajenti* wa ndani.
- **Chroma** hufanya kazi ndani ya mchakato na huhifadhi vekta kwenye diski, hivyo mchakato wote wa RAG (weka → hifadhi → rudisha → fanya hoja) unabaki wa ndani.
- **MCP** ni usafirishaji, si huduma ya wingu: seva ya MCP inaweza kuendesha ndani kupitia `stdio`.

## Mahitaji ya usanidi

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # mhifadhi wa ndani
```

~8 GB RAM ni kiwango halisi cha chini; GPU/NPU husaidia lakini si lazima.

## Mifumo muhimu ya kuiga

Mwelekeze mjuzi kwenye daftari
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Zana zilizofungwa (Sandboxed)**: kila zana ya faili hutatua njia na kushindwa chochote kilicho nje ya mizizi ya mradi mmoja — hata ndani, zana huendesha kwa ruhusa za mtumiaji.
- **Mzunguko wa kuitisha zana**: sajili zana na muktadha wa zana za OpenAI, tekeleza zana zilizotakiwa ndani, rudisha matokeo, rudia hadi jibu la mwisho.
- **RAG ya ndani**: ingiza nyaraka kwenye mkusanyiko wa Chroma; `search_docs` hurudisha vipande vya juu-k.
- **MCP ya ndani**: ungana na seva ya ndani kwa kutumia `stdio`; fanya iwe kwa saraka ya mradi na thibitisha matokeo yake.

## Usanidi wa mseto (ndani kama mojawapo ya miundo)

| Hali | Inapofanyika |
|-----------|---------------|
| Data nyeti / bila mtandao | SLM wa ndani |
| Kazi rahisi, iliyo chini | SLM wa ndani (bei nafuu, haraka) |
| Hoja ngumu ya mita nyingi kwenye data isiyo nyeti | Mfano wa wingu |
| Kutokea kwa tatizo la wingu | SLM wa ndani (kupungua kwa heshima) |

Hii inaiga wazo la mwelekeo wa mfano kutoka Somo la 16, kwa kutumia stesheni kama moja
ya njia. Pendekeza miundo inayorejea ndani ili ajenti apunguze ubora badala ya kushindwa kabisa.


## Mipaka kwa msaidizi

- Weka kila faili/operesheni ya zana iwe ndani ya saraka ya mradi iliyofungwa.
- Usitume msimbo au data kwa wingu wakati linaomba za mjuzi ni faragha/bila mtandao — weka mchakato mzima ndani.
- Weka matarajio halisi kwa ubora wa SLM; tegemea zana na RAG badala ya maarifa yaliyohifadhiwa ya mfano.
- Kumbuka kuwa Somo la 17 halina **kiungo cha Majibu cha Foundry**, hivyo jaribio la mtihani wa wingu halitumiki — thibitisha kwa kuendesha daftari la maelekezo ndani.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->