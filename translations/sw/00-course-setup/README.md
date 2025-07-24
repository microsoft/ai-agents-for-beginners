<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-24T08:52:10+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Usanidi wa Kozi

## Utangulizi

Somo hili litafundisha jinsi ya kuendesha sampuli za msimbo wa kozi hii.

## Kuiga au Kufanya Fork ya Repo Hii

Ili kuanza, tafadhali iga au fanya fork ya Hifadhi ya GitHub. Hii itakupa toleo lako mwenyewe la nyenzo za kozi ili uweze kuendesha, kujaribu, na kurekebisha msimbo!

Hii inaweza kufanyika kwa kubofya kiungo cha

Unapaswa sasa kuwa na toleo lako la fork la kozi hii katika kiungo kifuatacho:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sw.png)

## Kuendesha Msimbo

Kozi hii inatoa mfululizo wa Jupyter Notebooks ambazo unaweza kuendesha ili kupata uzoefu wa vitendo wa kujenga Mawakala wa AI.

Sampuli za msimbo zinatumia mojawapo ya:

**Inahitaji Akaunti ya GitHub - Bure**:

1) Mfumo wa Semantic Kernel Agent + Soko la Miundo la GitHub. Imeandikwa kama (semantic-kernel.ipynb)  
2) Mfumo wa AutoGen + Soko la Miundo la GitHub. Imeandikwa kama (autogen.ipynb)  

**Inahitaji Usajili wa Azure**:  
3) Azure AI Foundry + Huduma ya Wakala wa Azure AI. Imeandikwa kama (azureaiagent.ipynb)  

Tunapendekeza ujaribu aina zote tatu za mifano ili kuona ipi inakufaa zaidi.

Chaguo lolote utakaloamua, litaamua hatua za usanidi unazohitaji kufuata hapa chini:

## Mahitaji

- Python 3.12+  
  - **NOTE**: Ikiwa huna Python3.12 iliyosakinishwa, hakikisha unaisakinisha. Kisha unda venv yako ukitumia python3.12 ili kuhakikisha matoleo sahihi yanasakinishwa kutoka kwenye faili ya requirements.txt.  
- Akaunti ya GitHub - Kwa Ufikiaji wa Soko la Miundo la GitHub  
- Usajili wa Azure - Kwa Ufikiaji wa Azure AI Foundry  
- Akaunti ya Azure AI Foundry - Kwa Ufikiaji wa Huduma ya Wakala wa Azure AI  

Tumejumuisha faili ya `requirements.txt` kwenye mzizi wa hifadhi hii ambayo ina vifurushi vyote vya Python vinavyohitajika kuendesha sampuli za msimbo.

Unaweza kuvisakinisha kwa kuendesha amri ifuatayo kwenye terminal yako ukiwa kwenye mzizi wa hifadhi:

```bash
pip install -r requirements.txt
```  
Tunapendekeza kuunda mazingira ya kawaida ya Python ili kuepuka migongano na matatizo yoyote.

## Usanidi wa VSCode  
Hakikisha unatumia toleo sahihi la Python ndani ya VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Usanidi wa Sampuli zinazotumia Miundo ya GitHub  

### Hatua ya 1: Pata Tokeni Yako ya Ufikiaji wa Kibinafsi ya GitHub (PAT)  

Kozi hii inatumia Soko la Miundo la GitHub, likitoa ufikiaji wa bure kwa Miundo Mikubwa ya Lugha (LLMs) ambayo utatumia kujenga Mawakala wa AI.

Ili kutumia Miundo ya GitHub, utahitaji kuunda [Tokeni ya Ufikiaji wa Kibinafsi ya GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Hii inaweza kufanyika kwa kwenda kwenye akaunti yako ya GitHub.

Tafadhali fuata [Kanuni ya Upendeleo wa Chini](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) unapounda tokeni yako. Hii inamaanisha unapaswa kutoa tokeni ruhusa zinazohitajika tu kuendesha sampuli za msimbo wa kozi hii.

1. Chagua chaguo la `Fine-grained tokens` upande wa kushoto wa skrini yako.

    Kisha chagua `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.sw.png)

1. Weka jina la kuelezea kwa tokeni yako linaloonyesha madhumuni yake, ili iwe rahisi kuitambua baadaye. Weka tarehe ya kumalizika muda (inapendekezwa: siku 30; unaweza kuchagua kipindi kifupi kama siku 7 ikiwa unapendelea usalama zaidi.)

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sw.png)

1. Punguza wigo wa tokeni kwa fork yako ya hifadhi hii.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.sw.png)

1. Punguza ruhusa za tokeni: Chini ya **Permissions**, wezesha **Account Permissions**, nenda kwenye **Models** na wezesha tu ruhusa ya kusoma inayohitajika kwa Miundo ya GitHub.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.sw.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.sw.png)

Nakili tokeni yako mpya ambayo umeunda. Sasa utaongeza hii kwenye faili yako ya `.env` iliyojumuishwa kwenye kozi hii.

### Hatua ya 2: Unda Faili Yako ya `.env`

Ili kuunda faili yako ya `.env` endesha amri ifuatayo kwenye terminal yako.

```bash
cp .env.example .env
```

Hii itanakili faili ya mfano na kuunda `.env` kwenye saraka yako ambapo utaweka maadili ya vigezo vya mazingira.

Ukiwa na tokeni yako iliyokopiwa, fungua faili ya `.env` kwenye mhariri wa maandishi unaoupenda na ubandike tokeni yako kwenye sehemu ya `GITHUB_TOKEN`.

Sasa unapaswa kuwa na uwezo wa kuendesha sampuli za msimbo wa kozi hii.

## Usanidi wa Sampuli zinazotumia Azure AI Foundry na Huduma ya Wakala wa Azure AI  

### Hatua ya 1: Pata Endpoint ya Mradi Wako wa Azure  

Fuata hatua za kuunda hub na mradi katika Azure AI Foundry zilizopatikana hapa: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Baada ya kuunda mradi wako, utahitaji kupata mnyororo wa muunganisho wa mradi wako.

Hii inaweza kufanyika kwa kwenda kwenye ukurasa wa **Overview** wa mradi wako kwenye portal ya Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sw.png)

### Hatua ya 2: Unda Faili Yako ya `.env`

Ili kuunda faili yako ya `.env` endesha amri ifuatayo kwenye terminal yako.

```bash
cp .env.example .env
```

Hii itanakili faili ya mfano na kuunda `.env` kwenye saraka yako ambapo utaweka maadili ya vigezo vya mazingira.

Ukiwa na tokeni yako iliyokopiwa, fungua faili ya `.env` kwenye mhariri wa maandishi unaoupenda na ubandike tokeni yako kwenye sehemu ya `PROJECT_ENDPOINT`.

### Hatua ya 3: Ingia kwenye Azure  

Kama mazoea bora ya usalama, tutatumia [uthibitishaji bila funguo](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kuingia kwenye Azure OpenAI kwa kutumia Microsoft Entra ID.

Kisha, fungua terminal na endesha `az login --use-device-code` ili kuingia kwenye akaunti yako ya Azure.

Baada ya kuingia, chagua usajili wako kwenye terminal.

## Vigezo vya Mazingira vya Ziada - Azure Search na Azure OpenAI  

Kwa Somo la Agentic RAG - Somo la 5 - kuna sampuli zinazotumia Azure Search na Azure OpenAI.

Ikiwa unataka kuendesha sampuli hizi, utahitaji kuongeza vigezo vifuatavyo vya mazingira kwenye faili yako ya `.env`:

### Ukurasa wa Muhtasari (Mradi)

- `AZURE_SUBSCRIPTION_ID` - Angalia **Project details** kwenye ukurasa wa **Overview** wa mradi wako.

- `AZURE_AI_PROJECT_NAME` - Angalia juu ya ukurasa wa **Overview** wa mradi wako.

- `AZURE_OPENAI_SERVICE` - Pata hii kwenye kichupo cha **Included capabilities** kwa **Azure OpenAI Service** kwenye ukurasa wa **Overview**.

### Kituo cha Usimamizi

- `AZURE_OPENAI_RESOURCE_GROUP` - Nenda kwenye **Project properties** kwenye ukurasa wa **Overview** wa **Management Center**.

- `GLOBAL_LLM_SERVICE` - Chini ya **Connected resources**, pata jina la muunganisho wa **Azure AI Services**. Ikiwa halijaorodheshwa, angalia **Azure portal** chini ya kikundi chako cha rasilimali kwa jina la rasilimali za AI Services.

### Ukurasa wa Miundo + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Chagua mfano wako wa embedding (mfano, `text-embedding-ada-002`) na kumbuka **Deployment name** kutoka kwa maelezo ya mfano.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chagua mfano wako wa mazungumzo (mfano, `gpt-4o-mini`) na kumbuka **Deployment name** kutoka kwa maelezo ya mfano.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Tafuta **Azure AI services**, bofya juu yake, kisha nenda kwenye **Resource Management**, **Keys and Endpoint**, shuka chini hadi "Azure OpenAI endpoints", na nakili ile inayosema "Language APIs".

- `AZURE_OPENAI_API_KEY` - Kutoka skrini hiyo hiyo, nakili KEY 1 au KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Tafuta rasilimali yako ya **Azure AI Search**, bofya juu yake, na uone **Overview**.

- `AZURE_SEARCH_API_KEY` - Kisha nenda kwenye **Settings** na kisha **Keys** ili kunakili ufunguo wa msingi au wa sekondari wa msimamizi.

### Ukurasa wa Nje

- `AZURE_OPENAI_API_VERSION` - Tembelea ukurasa wa [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) chini ya **Latest GA API release**.

### Usanidi wa uthibitishaji bila funguo  

Badala ya kuweka sifa zako moja kwa moja, tutatumia muunganisho bila funguo na Azure OpenAI. Ili kufanya hivyo, tutaingiza `DefaultAzureCredential` na baadaye kuita kazi ya `DefaultAzureCredential` ili kupata sifa.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Umekwama Mahali Fulani?  

Ikiwa unakutana na matatizo yoyote ukiendesha usanidi huu, jiunge na

## Somo Lijalo  

Sasa uko tayari kuendesha msimbo wa kozi hii. Jifunze kwa furaha zaidi kuhusu ulimwengu wa Mawakala wa AI!  

[Utangulizi wa Mawakala wa AI na Matumizi Yake](../01-intro-to-ai-agents/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kibinadamu ya kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.