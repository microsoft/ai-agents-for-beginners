# Mfano wa Github MCP Server

## Maelezo

Hii ilikuwa demo iliyotengenezwa kwa ajili ya AI Agents Hackathon iliyoandaliwa kupitia Microsoft Reactor.

Zana hizi zinatumika kupendekeza miradi ya hackathon kulingana na repos za Github za mtumiaji.
Hii inafanywa kwa njia zifuatazo:

1. **Github Agent** - Kutumia Github MCP Server kupata repos na taarifa kuhusu repos hizo.
2. **Hackathon Agent** - Huchukua data kutoka kwa Github Agent na kuja na mawazo ya ubunifu ya miradi ya hackathon kulingana na miradi, lugha ambazo mtumiaji ametumia, na njia za mradi za AI Agents hackathon.
3. **Events Agent** - Kulingana na mapendekezo ya Hackathon Agent, Events Agent atapendekeza matukio yanayofaa kutoka katika mfululizo wa AI Agent Hackathon.
## Kukimbia msimbo 

### Vigezo vya Mazingira

Demo hii inatumia Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server na Azure AI Search.

Hakikisha kwamba umeweka vigezo vya mazingira vinavyofaa ili kutumia zana hizi:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kukimbia seva ya Chainlit

Ili kuungana na MCP server, demo hii inatumia Chainlit kama kiolesura cha mazungumzo. 

Ili kuendesha seva, tumia amri ifuatayo kwenye terminal yako:

```bash
chainlit run app.py -w
```

Hii inapaswa kuanza seva yako ya Chainlit kwenye `localhost:8000` pamoja na kujaza Index ya Azure AI Search na yaliyomo ya `event-descriptions.md`. 

## Kuungana na MCP Server

Ili kuungana na Github MCP Server, chagua ikoni ya "plug" chini ya kisanduku cha mazungumzo cha "Andika ujumbe wako hapa..":

![Unganisha MCP](../../../../../translated_images/sw/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Kutoka hapo unaweza kubofya "Unganisha MCP" ili kuongeza amri ya kuunganishwa na Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

Baada ya kuunganisha, unapaswa kuona (1) karibu na ikoni ya plug kuthibitisha kuwa imeunganishwa. Ikiwa sivyo, jaribu kuzindua tena seva ya chainlit kwa kutumia `chainlit run app.py -w`.

## Kutumia Demo 

Ili kuanza mtiririko wa wakala wa kupendekeza miradi ya hackathon, unaweza kuandika ujumbe kama: 

"Pendekeza miradi ya hackathon kwa mtumiaji wa Github koreyspace"

Wakala wa Router atachambua ombi lako na kuamua ni mchanganyiko gani wa wakala (GitHub, Hackathon, na Events) unaofaa zaidi kushughulikia ombi lako. Wakala hao hufanya kazi pamoja kutoa mapendekezo ya kina yanayotokana na uchambuzi wa repos za GitHub, ubunifu wa miradi, na matukio ya teknolojia yanayofaa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Taarifa ya kutokuhusika**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya kutafsiri inayotumia akili bandia [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Nyaraka ya asili katika lugha yake inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inapendekezwa kutumia huduma za mtafsiri mtaalamu wa kibinadamu. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->