# Majaribio ya Mwamvuli ya Wakala

Folda hii ina **katalogi za majaribio ya mwamvuli** kwa wakala mnaojenga katika kozi.
Jaribio la mwamvuli ni ukaguzi wa gharama nafuu, haraka kwamba **wakala aliyetumika mwenyeji
wa Microsoft Foundry** anapatikana, anajibu, na anafuata matarajio yake ya kiundani ya haraka.
Ni lango la kwanza — si kuchukua nafasi ya mchakato kamili wa tathmini
unaojifunza katika [Somo la 10](../10-ai-agents-production/README.md) na
[Somo la 16](../16-deploying-scalable-agents/README.md).

Katalogi hutumika na Hatua za GitHub ya [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
kupitia mtiririko wa kazi wa [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Jinsi ya kuendesha

1. **Tumia wakala wa somo** katika Microsoft Foundry kama wakala mwenyeji (angalia
   Somo la 16 kwa mtiririko wa utumiaji). Kumbuka **jina la wakala** na
   **sehemu ya mradi ya Foundry**.
2. Ongeza siri hizi za hifadhi (Mipangilio → Siri na vigezo → Hatua):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Kitambulisho cha umoja
   kinahitaji jukumu la **Mtumiaji wa Azure AI** katika **uwanja wa mradi wa Foundry**.
3. Kutoka kwenye kichupo cha **Hatua**, endesha **Majaribio ya mwamvuli ya wakala wenyeji**
   na chagua `tests_file` ya somo, kisha toa `agent_name` na `project_endpoint`
   zinazolingana.

## Katalogi → somo → jina la wakala

| Katalogi | Somo | Tumia wakala kama |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Utangulizi kwa Wakala wa AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Matumizi ya Zana](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Kuweka Wakala Waloweza Kupanuliwa](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Ni masomo gani yana majaribio ya mwamvuli?

Majaribio ya mwamvuli yanahusu masomo ambapo una **tumia wakala** jibu la maandishi ya
huweza kuthibitishwa dhidi ya yaliyomo yanayojulikana. Masomo ambayo ni dhana, yanayotekelezwa tu
kisheria, au yanayotengeneza matokeo yasiyotabirika kwa ubunifu hayajumuishwi kwa makusudi:

- **Somo la 17 (Kuunda Wakala wa AI wa Ndani)** linaendeshwa kabisa kwenye stesheni yako
  kwa kutumia Foundry Local na haliwezi kufikia muktadha wa Majibu ya Foundry, hivyo
  hatua hii haifanyi kazi. Thibitisha kwa kuendesha kitabu cha kumbukumbu kwa ndani.
- Masomo ya muundo wa muundo na nadharia (02, 03, 06, 07, 09, 12) hayatumiwi
  kama wakala mmoja wa kujaribiwa.

## Muundo wa katalogi (marejeleo ya haraka)

Katalogi kila moja ni hati ya JSON yenye safu ya juu ya `tests`. Kila kipengele hutuma
maelezo moja na kuthibitisha jibu:

| Sehemu | Maana |
|-------|---------|
| `id` | Kitambulisho cha kipekee cha hatua kilichoandikwa kwenye kumbukumbu. |
| `description` | Kusudi linaloweza kusomeka na binadamu. |
| `prompt` | Ujumbe unaotumwa kwa wakala. |
| `assertions.status` | Hali ya HTTP inayotarajiwa (kwa kawaida 200). |
| `assertions.contains_any` | Panua ikiwa jibu lina sehemu yoyote kati ya hizi. |
| `assertions.contains_all` | Panua ikiwa jibu lina kila sehemu ndogo. |
| `assertions.contains_none` | Panua ikiwa jibu halina hata sehemu ndogo ya hizi. |
| `save_response_id_as` | Hifadhi kitambulisho cha jibu kwa hatua ya mzunguko wa baadaye. |
| `use_previous_response_id` | Tumia mzunguko huu ukifuatana na kitambulisho cha jibu kilichohifadhiwa. |

Thibitisho ni ukaguzi wa sehemu ndogo usiojali herufi kubwa au ndogo. Angalia
[nyaraka za hatua](https://github.com/marketplace/actions/ai-smoke-test) kwa
muundo kamili, pamoja na rasilimali za mazungumzo zinazodhibitiwa na Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->