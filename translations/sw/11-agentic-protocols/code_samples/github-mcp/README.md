# Mfano wa Seva ya MCP ya Github

## Maelezo

Hii ilikuwa demo iliyoundwa kwa ajili ya AI Agents Hackathon iliyofanyika kupitia Microsoft Reactor.

Zana hizi zinatumika kupendekeza miradi ya hackathon kulingana na hifadhi za mtumiaji za Github.
Hili hufanywa kwa njia zifuatazo:

1. **Github Agent** - Kutumia Seva ya MCP ya Github kupata repos na taarifa kuhusu repos hizo.
2. **Hackathon Agent** - Inachukua data kutoka kwa Github Agent na kubuni mawazo ya ubunifu ya miradi ya hackathon kulingana na miradi, lugha zinazotumika na mtumiaji, na matawi ya mradi ya AI Agents hackathon.
3. **Events Agent** - Kwa mujibu wa mapendekezo ya Hackathon Agent, Events Agent itapendekeza matukio yanayofaa kutoka kwenye mfululizo wa AI Agent Hackathon.
## Kuendesha msimbo 

### Vigezo vya Mazingira

Demo hii inatumia Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server and Azure AI Search.

Hakikisha kuwa umeweka vigezo sahihi vya mazingira ili kutumia zana hizi:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Kuendesha Seva ya Chainlit

Ili kuunganishwa na seva ya MCP, demo hii inatumia Chainlit kama kiolesura cha gumzo. 

Ili kuendesha seva, tumia amri ifuatayo kwenye terminal yako:

```bash
chainlit run app.py -w
```

Hii inapaswa kuanzisha seva yako ya Chainlit kwa `localhost:8000` na pia kujaza Index yako ya Azure AI Search na maudhui ya `event-descriptions.md`. 

## Kuunganishwa na Seva ya MCP

Ili kuunganishwa na Github MCP Server, chagua ikoni ya "plug" chini ya kisanduku cha gumzo cha "Type your message here..":

![Unganisha MCP](../../../../../translated_images/sw/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Kutoka hapo unaweza kubofya "Unganisha MCP" kuongeza amri ya kuunganishia Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Badilisha "[YOUR PERSONAL ACCESS TOKEN]" na Personal Access Token yako halisi. 

Baada ya kuunganishwa, utapaswa kuona (1) kando ya ikoni ya "plug" kuthibitisha kuwa imeunganishwa. Iwapo sivyo, jaribu kuwasha upya seva ya chainlit kwa `chainlit run app.py -w`.

## Kutumia Demo

Ili kuanza mtiririko wa wakala wa kupendekeza miradi ya hackathon, unaweza kuandika ujumbe kama: 

"Pendekeza miradi ya hackathon kwa mtumiaji wa Github koreyspace"

Router Agent itachambua ombi lako na kubaini mchanganyiko gani wa agents (GitHub, Hackathon, and Events) unaofaa kushughulikia ombi lako. Wakala hawa hufanya kazi pamoja kutoa mapendekezo kamili kulingana na GitHub repository analysis, ubunifu wa miradi, na matukio ya teknolojia yanayohusiana.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko la kutokuwa na dhamana:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya awali katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inapendekezwa kutumia tafsiri ya kitaalamu ya binadamu. Hatuwajibiki kwa mifahamo au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->