<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:45:21+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sw"
}
-->
# Usanidi wa Kozi

## Utangulizi

Somo hili litafundisha jinsi ya kuendesha sampuli za msimbo wa kozi hii.

## Jiunge na Wanafunzi Wengine na Pata Msaada

Kabla ya kuanza kunakili repo yako, jiunge na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ili kupata msaada wowote wa usanidi, maswali yoyote kuhusu kozi, au kuungana na wanafunzi wengine.

## Nakili au Fork Repo Hii

Ili kuanza, tafadhali nakili au fork Hifadhi ya GitHub. Hii itakupa toleo lako la nyenzo za kozi ili uweze kuendesha, kujaribu, na kurekebisha msimbo!

Hii inaweza kufanyika kwa kubofya kiungo cha <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

Sasa unapaswa kuwa na toleo lako la forked la kozi hii katika kiungo kinachofuata:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sw.png)

### Nakili ya Kawaida (inapendekezwa kwa warsha / Codespaces)

  >Hifadhi nzima inaweza kuwa kubwa (~3 GB) unapopakua historia kamili na faili zote. Ikiwa unahudhuria tu warsha au unahitaji tu folda chache za somo, nakili ya kawaida (au nakili ya sparse) huepuka upakuaji mwingi kwa kufupisha historia na/au kuruka blobs.

#### Nakili ya haraka ya kawaida — historia ndogo, faili zote

Badilisha `<your-username>` katika amri zilizo hapa chini na URL ya fork yako (au URL ya upstream ikiwa unapendelea).

Ili kunakili historia ya commit ya hivi karibuni pekee (upakuaji mdogo):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ili kunakili tawi maalum:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Nakili ya sehemu (sparse) — blobs ndogo + folda zilizochaguliwa pekee

Hii inatumia nakili ya sehemu na sparse-checkout (inahitaji Git 2.25+ na Git ya kisasa inayopendekezwa na msaada wa nakili ya sehemu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ingia kwenye folda ya repo:

Kwa bash:

```bash
cd ai-agents-for-beginners
```

Kwa Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Kisha taja ni folda zipi unazotaka (mfano hapa chini unaonyesha folda mbili):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Baada ya kunakili na kuthibitisha faili, ikiwa unahitaji tu faili na unataka kuokoa nafasi (hakuna historia ya git), tafadhali futa metadata ya hifadhi (💀isiyoweza kubadilishwa — utapoteza utendaji wote wa Git: hakuna commits, pulls, pushes, au ufikiaji wa historia).

Kwa Linux/macOS:

```bash
rm -rf .git
```

Kwa Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inapendekezwa kuepuka upakuaji mkubwa wa ndani)

- Unda Codespace mpya kwa repo hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya Codespace mpya iliyoundwa, endesha moja ya amri za nakili ya kawaida/sehemu zilizo hapo juu ili kuleta folda za somo unazohitaji tu kwenye workspace ya Codespace.
- Hiari: baada ya kunakili ndani ya Codespaces, ondoa .git ili kurejesha nafasi ya ziada (tazama amri za kuondoa hapo juu).
- Kumbuka: Ikiwa unapendelea kufungua repo moja kwa moja ndani ya Codespaces (bila nakili ya ziada), fahamu Codespaces itajenga mazingira ya devcontainer na inaweza bado kutoa zaidi ya unavyohitaji. Kunakili nakili ya kawaida ndani ya Codespace mpya hukupa udhibiti zaidi wa matumizi ya diski.

#### Vidokezo

- Badilisha URL ya nakili kila wakati na fork yako ikiwa unataka kuhariri/commit.
- Ikiwa baadaye unahitaji historia zaidi au faili, unaweza kuzichukua au kurekebisha sparse-checkout ili kujumuisha folda za ziada.

## Kuendesha Msimbo

Kozi hii inatoa mfululizo wa Jupyter Notebooks ambazo unaweza kuendesha ili kupata uzoefu wa vitendo wa kujenga AI Agents.

Sampuli za msimbo zinatumia:

**Inahitaji Akaunti ya GitHub - Bure**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Imewekwa alama kama (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Imewekwa alama kama (autogen.ipynb)

**Inahitaji Usajili wa Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Imewekwa alama kama (azureaiagent.ipynb)

Tunapendekeza ujaribu aina zote tatu za mifano ili kuona ni ipi inakufaa zaidi.

Chaguo lolote unalochagua, litaamua hatua za usanidi unazohitaji kufuata hapa chini:

## Mahitaji

- Python 3.12+
  - **NOTE**: Ikiwa huna Python3.12 iliyosakinishwa, hakikisha unaisakinisha. Kisha unda venv yako ukitumia python3.12 ili kuhakikisha matoleo sahihi yamesakinishwa kutoka kwa faili ya requirements.txt.
  
    >Mfano

    Unda folda ya Python venv:

    ``` bash
    python3 -m venv venv
    ```

    Kisha wezesha mazingira ya venv kwa:

    macOS na Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- Akaunti ya GitHub - Kwa Ufikiaji wa GitHub Models Marketplace
- Usajili wa Azure - Kwa Ufikiaji wa Azure AI Foundry
- Akaunti ya Azure AI Foundry - Kwa Ufikiaji wa Azure AI Agent Service

Tumeshirikisha faili ya `requirements.txt` katika mzizi wa hifadhi hii ambayo ina pakiti zote za Python zinazohitajika kuendesha sampuli za msimbo.

Unaweza kuzisakinisha kwa kuendesha amri ifuatayo katika terminal yako kwenye mzizi wa hifadhi:

```bash
pip install -r requirements.txt
```
Tunapendekeza kuunda mazingira ya Python virtual ili kuepuka migogoro na matatizo.

## Usanidi wa VSCode
Hakikisha unatumia toleo sahihi la Python katika VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Usanidi wa Sampuli zinazotumia GitHub Models 

### Hatua ya 1: Pata Token ya Ufikiaji wa Kibinafsi ya GitHub (PAT)

Kozi hii inatumia GitHub Models Marketplace, ikitoa ufikiaji wa bure kwa Large Language Models (LLMs) ambazo utatumia kujenga AI Agents.

Ili kutumia GitHub Models, utahitaji kuunda [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Hii inaweza kufanyika kwa kwenda kwenye <a href="https://github.com/settings/personal-access-tokens" target="_blank">mipangilio ya Personal Access Tokens</a> katika Akaunti yako ya GitHub.

Tafadhali fuata [Kanuni ya Upendeleo wa Chini](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) unapounda token yako. Hii inamaanisha unapaswa tu kutoa token ruhusa zinazohitajika kuendesha sampuli za msimbo katika kozi hii.

1. Chagua chaguo la `Fine-grained tokens` upande wa kushoto wa skrini yako kwa kwenda kwenye **Developer settings**
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sw.png)

    Kisha chagua `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sw.png)

2. Weka jina la kuelezea kwa token yako linaloonyesha kusudi lake, ili iwe rahisi kutambua baadaye.


    🔐 Pendekezo la Muda wa Token

    Muda uliopendekezwa: siku 30
    Kwa usalama zaidi, unaweza kuchagua muda mfupi—kama siku 7 🛡️
    Ni njia nzuri ya kuweka lengo la kibinafsi na kukamilisha kozi huku kasi yako ya kujifunza ikiwa juu 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sw.png)

3. Punguza wigo wa token kwa fork yako ya hifadhi hii.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sw.png)

4. Punguza ruhusa za token: Chini ya **Permissions**, bofya kichupo cha **Account**, na bofya kitufe cha "+ Add permissions". Kutakuwa na dropdown. Tafadhali tafuta **Models** na weka alama kwenye kisanduku chake.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sw.png)

5. Thibitisha ruhusa zinazohitajika kabla ya kuunda token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sw.png)

6. Kabla ya kuunda token, hakikisha uko tayari kuhifadhi token katika sehemu salama kama hifadhi ya meneja wa nywila, kwani haitatolewa tena baada ya kuundwa. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sw.png)

Nakili token yako mpya ambayo umekuja kuunda. Sasa utaongeza hii kwenye faili yako ya `.env` iliyojumuishwa katika kozi hii.


### Hatua ya 2: Unda Faili Yako ya `.env`

Ili kuunda faili yako ya `.env` endesha amri ifuatayo katika terminal yako.

```bash
cp .env.example .env
```

Hii itanakili faili ya mfano na kuunda `.env` katika folda yako ambapo utaweka maadili ya vigezo vya mazingira.

Kwa token yako iliyokopiwa, fungua faili ya `.env` katika mhariri wako wa maandishi unaopenda na weka token yako kwenye sehemu ya `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sw.png)


Sasa unapaswa kuwa na uwezo wa kuendesha sampuli za msimbo wa kozi hii.

## Usanidi wa Sampuli zinazotumia Azure AI Foundry na Azure AI Agent Service

### Hatua ya 1: Pata Endpoint ya Mradi wa Azure


Fuata hatua za kuunda hub na mradi katika Azure AI Foundry zilizopatikana hapa: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Baada ya kuunda mradi wako, utahitaji kupata string ya muunganisho wa mradi wako.

Hii inaweza kufanyika kwa kwenda kwenye ukurasa wa **Overview** wa mradi wako katika portal ya Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sw.png)

### Hatua ya 2: Unda Faili Yako ya `.env`

Ili kuunda faili yako ya `.env` endesha amri ifuatayo katika terminal yako.

```bash
cp .env.example .env
```

Hii itanakili faili ya mfano na kuunda `.env` katika folda yako ambapo utaweka maadili ya vigezo vya mazingira.

Kwa token yako iliyokopiwa, fungua faili ya `.env` katika mhariri wako wa maandishi unaopenda na weka token yako kwenye sehemu ya `PROJECT_ENDPOINT`.

### Hatua ya 3: Ingia kwenye Azure

Kama mazoea bora ya usalama, tutatumia [uthibitishaji bila funguo](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kuingia kwenye Azure OpenAI na Microsoft Entra ID. 

Kisha, fungua terminal na endesha `az login --use-device-code` ili kuingia kwenye akaunti yako ya Azure.

Baada ya kuingia, chagua usajili wako katika terminal.


## Vigezo vya Mazingira vya Ziada - Azure Search na Azure OpenAI 

Kwa Somo la Agentic RAG - Somo la 5 - kuna sampuli zinazotumia Azure Search na Azure OpenAI.

Ikiwa unataka kuendesha sampuli hizi, utahitaji kuongeza vigezo vifuatavyo vya mazingira kwenye faili yako ya `.env`:

### Ukurasa wa Muhtasari (Mradi)

- `AZURE_SUBSCRIPTION_ID` - Angalia **Project details** kwenye ukurasa wa **Overview** wa mradi wako.

- `AZURE_AI_PROJECT_NAME` - Angalia juu ya ukurasa wa **Overview** wa mradi wako.

- `AZURE_OPENAI_SERVICE` - Pata hii katika kichupo cha **Included capabilities** kwa **Azure OpenAI Service** kwenye ukurasa wa **Overview**.

### Kituo cha Usimamizi

- `AZURE_OPENAI_RESOURCE_GROUP` - Nenda kwenye **Project properties** kwenye ukurasa wa **Overview** wa **Management Center**.

- `GLOBAL_LLM_SERVICE` - Chini ya **Connected resources**, pata jina la muunganisho wa **Azure AI Services**. Ikiwa halipo, angalia **Azure portal** chini ya kikundi chako cha rasilimali kwa jina la rasilimali za AI Services.

### Ukurasa wa Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Chagua mfano wako wa embedding (mfano, `text-embedding-ada-002`) na kumbuka **Deployment name** kutoka kwa maelezo ya mfano.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chagua mfano wako wa chat (mfano, `gpt-4o-mini`) na kumbuka **Deployment name** kutoka kwa maelezo ya mfano.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Tafuta **Azure AI services**, bofya juu yake, kisha nenda kwenye **Resource Management**, **Keys and Endpoint**, shuka chini kwenye "Azure OpenAI endpoints", na nakili ile inayosema "Language APIs".

- `AZURE_OPENAI_API_KEY` - Kutoka skrini hiyo hiyo, nakili KEY 1 au KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Pata rasilimali yako ya **Azure AI Search**, bofya juu yake, na angalia **Overview**.

- `AZURE_SEARCH_API_KEY` - Kisha nenda kwenye **Settings** na kisha **Keys** ili kunakili funguo ya msingi au ya sekondari ya admin.

### Ukurasa wa Nje

- `AZURE_OPENAI_API_VERSION` - Tembelea ukurasa wa [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) chini ya **Latest GA API release**.

### Usanidi wa uthibitishaji bila funguo

Badala ya kuweka maelezo yako ya kuingia, tutatumia muunganisho bila funguo na Azure OpenAI. Ili kufanya hivyo, tutaleta `DefaultAzureCredential` na baadaye kuita kazi ya `DefaultAzureCredential` ili kupata uthibitisho.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Umekwama Mahali Fulani?
Ikiwa unakutana na changamoto yoyote wakati wa kuendesha mpangilio huu, jiunge na <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">unda suala</a>.

## Somo Linalofuata

Sasa uko tayari kuendesha msimbo wa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Mawakala wa AI!

[Utangulizi wa Mawakala wa AI na Matumizi ya Mawakala](../01-intro-to-ai-agents/README.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.