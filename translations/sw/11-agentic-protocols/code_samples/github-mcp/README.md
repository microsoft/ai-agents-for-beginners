<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T21:22:29+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "sw"
}
-->
# Mfano wa Server ya Github MCP

## Maelezo

Hii ni demo iliyotengenezwa kwa ajili ya Hackathon ya Mawakala wa AI iliyoandaliwa kupitia Microsoft Reactor.

Zana hii inatumika kupendekeza miradi ya hackathon kulingana na repos za mtumiaji wa Github. Hii inafanyika kwa:

1. **Github Agent** - Kutumia Server ya Github MCP kupata repos na taarifa kuhusu repos hizo.
2. **Hackathon Agent** - Inachukua data kutoka kwa Github Agent na kuja na mawazo ya ubunifu ya miradi ya hackathon kulingana na miradi, lugha zinazotumiwa na mtumiaji, na nyimbo za miradi kwa hackathon ya Mawakala wa AI.
3. **Events Agent** - Kulingana na mapendekezo ya Hackathon Agent, Events Agent itapendekeza matukio yanayohusiana kutoka kwenye mfululizo wa Hackathon ya Mawakala wa AI.

## Kuendesha Msimbo

### Vigezo vya Mazingira

Demo hii inatumia Azure Open AI Service, Semantic Kernel, Server ya Github MCP, na Azure AI Search.

Hakikisha unaweka vigezo sahihi vya mazingira ili kutumia zana hizi:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kuendesha Server ya Chainlit

Ili kuunganishwa na server ya MCP, demo hii inatumia Chainlit kama kiolesura cha mazungumzo.

Ili kuendesha server, tumia amri ifuatayo kwenye terminal yako:

```bash
chainlit run app.py -w
```

Hii inapaswa kuanzisha server yako ya Chainlit kwenye `localhost:8000` pamoja na kujaza Azure AI Search Index yako na maudhui ya `event-descriptions.md`.

## Kuunganishwa na Server ya MCP

Ili kuunganishwa na Server ya Github MCP, chagua ikoni ya "plug" chini ya kisanduku cha mazungumzo "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.sw.png)

Kutoka hapo unaweza kubofya "Connect an MCP" ili kuongeza amri ya kuunganishwa na Server ya Github MCP:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Badilisha "[YOUR PERSONAL ACCESS TOKEN]" na Token yako halisi ya Ufikiaji wa Kibinafsi.

Baada ya kuunganishwa, unapaswa kuona (1) karibu na ikoni ya plug kuthibitisha kuwa imeunganishwa. Ikiwa sivyo, jaribu kuanzisha upya server ya Chainlit kwa `chainlit run app.py -w`.

## Kutumia Demo

Ili kuanza mtiririko wa wakala wa kupendekeza miradi ya hackathon, unaweza kuandika ujumbe kama:

"Pendekeza miradi ya hackathon kwa mtumiaji wa Github koreyspace"

Router Agent itachambua ombi lako na kuamua ni mchanganyiko gani wa mawakala (GitHub, Hackathon, na Events) unaofaa kushughulikia swali lako. Mawakala hufanya kazi pamoja kutoa mapendekezo ya kina kulingana na uchambuzi wa repos za Github, mawazo ya miradi, na matukio ya teknolojia yanayohusiana.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.