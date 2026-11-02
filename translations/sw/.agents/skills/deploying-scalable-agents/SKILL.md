---
name: deploying-scalable-agents
license: MIT
---
# Kueneza Wakala Wanaoweza Kupandishwa Kiwango na Microsoft Foundry

> Ujuzi wa mpenzi kwa [Somo la 16 – Kueneza Wakala Wanaoweza Kupandishwa Kiwango](../../../16-deploying-scalable-agents/README.md).
> Utilize kusaidia mwanafunzi kuhamisha wakala kutoka mfano wa awali hadi utekelezaji
> wa uzalishaji unaoweza kupimwa, unaoonekana. Weka kila pendekezo kulingana na yaliyomo
> ya somo na daftari la kuendesha; usitengeneze API za Foundry.

## Vichocheo

Washa ujuzi huu wakati mwanafunzi anapotaka:
- Kueneza wakala kwenye Microsoft Foundry kama **wakala aliyehifadhiwa** na kuufanya uwe na matoleo/uwezekano wa kuonekana.
- Kuchagua kati ya mifumo ya uenezi ya **mteja-aliyahifadhiwa, wakala aliyehifadhiwa, na mtiririko wa kazi wa wakala**.
- Ongeza **upaliliaji wa mfano**, **uhifadhi wa majibu**, au **udhihirisho wa concurrency uliopimwa** kudhibiti ucheleweshaji na gharama.
- Ongeza **lango la tathmini** ili toleo baya la wakala lisiletwe sokoni.
- Ongeza hatua ya **idhini ya binadamu katika mzunguko** kwa vitendo vya hatari kubwa.
- Pandisha kifaa wakala kwa **uchunguzi wa OpenTelemetry** kwa kuonekana kwa uzalishaji.
- **Jaribio la moshi** la wakala aliyeenea kama lango la haraka baada ya uenezi.

## Mfano wa kimsingi wa kichwa

Wakala wa uzalishaji kwa kiasi kikubwa ni mifupa ya kiutendaji *karibu* na mfano (~80%),
sio mfano yenyewe. Changanua kila pendekezo kwa moja ya mambo haya:

| Juhudi | Mfano wa awali → Uzalishaji |
|---------|------------------------|
| Ukaribishaji | daftari → huduma iliyohifadhiwa yenye toleo |
| Utambulisho | `az login` yako → utambulisho uliosimamiwa + RBAC uliofadhiliwa |
| Hali | kumbukumbu ya ndani → hifadhi ya thread/kumbukumbu ya nje |
| Kosa | debugu → jaribio tena, mbadala, onyo |
| Gharama | "senti chache" → kufuatiliwa, kupitishwa, kuhifadhiwa, bajeti |
| Ubora | kutazama tu → lango la tathmini kiotomatiki |
| Uaminifu | wewe urangia → sera + binadamu katika mzunguko |

## Mifumo ya uenezi (chagua moja, au changanya)

1. **Mteja-aliyahifadhiwa** — mzunguko wa hoja unaendeshwa katika mchakato wako. Udhibiti mkubwa; unamiliki upanuzi/hali.
2. **Wakala aliyehifadhiwa (Huduma ya Wakala wa Foundry)** — Foundry inaendesha mzunguko, huhifadhi thread, hutekeleza RBAC/usalama wa maudhui, huonesha wakala kwenye lango la mtandao. Udhibiti mdogo, uso mdogo wa uendeshaji.
3. **Mtiririko wa kazi wa wakala** — wakala/vifaa vingi vimeunganishwa katika mchoro wenye matawi, nodi za idhini, na vituo vinavyoeza kuwepo.

## Mzunguko wa maisha (mzunguko unaosambaza wakala)

`unda → toa toleo → tathmini (mlango) → weka kwenye mwenyeji → tasa mtandaoni → kusanya makosa → rudia`.
**Tathmini isiyokuwa mtandaoni ni lango, sio jambo la baada** — toleo halitoshi
isipokuwa litakapopita kiwango. Uwezekano mtandaoni hurudisha makosa halisi
kwenye seti ya majaribio isiyokuwa mtandaoni.

## Viashiria vya kupanua na gharama (kwa mpangilio wa kipaumbele)

1. **Chagua mfano sahihi** — tumia mfano mdogo kabisa unaopita lango la tathmini.
2. **Pitia kulingana na ugumu** — mfano mdogo/haraka kwa maombi rahisi, mfano mkubwa kwa hoja halisi (mchambuzi wa DIY au Mpita Modeli wa Foundry).
3. **Hifadhi ya muda** — hudumia maombi ya karibu-kirudufu bila simu ya mfano.
4. **Muundo usiotuama hali + concurrency iliyopimwa** — hifadhi hali nje; jaribu tena kwa marefusho.

## Mifumo muhimu ya kuiga

Elekeza mwanafunzi kwa haya kutoka kwenye daftari
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Msimamizi wa maombi**: hifadhi → pitia kulingana na ugumu → ufuatiliaji span → endesha → hifadhi.
- **Lango la tathmini**: pima seti ya majaribio isiyo mtandaoni; rudisha `pass_rate >= threshold` na weka tu kama ni kweli.
- **Idhini ya binadamu**: `@tool(approval_mode="always_require")` kwa vitendo kama kurejesha fedha nyingi.
- **Ufuatiliaji**: zungusha kila ombi ndani ya `tracer.start_as_current_span(...)` na weka tabia kama `routed.model`, `customer.id`.

## Jaribio la moshi la wakala aliyeenea

Baada ya kuweka, hakikisha eneo la mwisho lina jibu kweli (uenezi wa kijani bado unaweza
kuwa kimya). Tumia kitendo cha [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
kupitia [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
na orodha ya majaribio katika [`tests/`](../../../tests/README.md). Mtendaji hutuma POST kila
agizo kwa `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
na kuthibitisha maandishi ya jibu. Utambulisho unahitaji jukumu la **Azure AI User**
katika wigo wa mradi wa Foundry; hadhira ya tokeni lazima iwe `https://ai.azure.com/`.

Panga milango: **jaribio la moshi** (inayofikika/inayojibu, kila uenezi) → **tathmini
isiyokuwa mtandaoni** (inayotosha kusambaza, kabla ya kukuza) → **tathmini mtandaoni**
(inafanya vipi kwa mazingira halisi, mfululizo).

## Udhibiti wa mashirika

- **RBAC**: mpe kila wakala aliyehifadhiwa utambulisho uliosimamiwa mwenye mapungufu machache.
- **MCP katika uzalishaji**: chukulia kila seva MCP kama mpaka usioaminika — adhimishe toleo, fadilia utambulisho wake, thibitisha matokeo, zuia kiwango, usiwafichue siri.

## Mipaka ya msaidizi

- Pendelea muundo halisi wa `FoundryChatClient(...)` + `provider.as_agent(...)` unaotumika kote kozi.
- Usiahidi matokeo ya moja kwa moja ya Azure ambayo hujathibitisha; pendekeza mtiririko wa jaribio la moshi kuthibitisha uenezi.
- Wahifadhi tathmini na ushauri wa gharama pamoja: tathmini huweka kiwango cha ubora, njia/hifadhi huwaweka gharama karibu na kiwango hicho.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->