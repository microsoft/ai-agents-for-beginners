# Muutosloki

Kaikki merkittävät muutokset **AI Agents for Beginners** -kurssilla on dokumentoitu tässä tiedostossa.

## [Julkaisematon] — 2026-07-06

Tässä julkaisussa kurssi siirretään käyttämään **Azure OpenAI Responses APIa**, yhtenäistetään tuotteen nimitykset **Microsoft Foundryn** ja **Microsoft Agent Frameworkin (MAF)** osalta, poistetaan GitHub Models -tuki, päivitetään SDK-versioita ja lisätään uutta sisältöä paikallisista malleista sekä muiden kehysten ylläpidosta Foundryssa.

### Lisätty

- **Migration skill** — Asennettu [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (lähteestä [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) hakemistoon `.agents/skills/`, mukaan lukien siihen liittyvät viittaukset ja skannauskomentosarja.
- **Foundry Local (ajetaan malleja laitteella)** — Uusi "Vaihtoehtoinen tarjoaja: Foundry Local" -osio tiedostossa [00-course-setup/README.md](./00-course-setup/README.md), joka käsittelee asennuksen (`winget` / `brew`), `foundry model run` -komennon, `foundry-local-sdk:n` ja `FoundryLocalManager` -yhdistämisen Microsoft Agent Frameworkiin `OpenAIChatClient` kautta.
- **LangChain / LangGraph -agenttien ylläpito Microsoft Foundryssa** — Uusi osio tiedostossa [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) sekä ajettava esimerkkikoodi [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), joka käyttää `langchain-azure-ai[hosting]` ja `ResponsesHostServer` (protocol `/responses`), pohjautuen [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) -aineistoon.
- **Microsoft Project Opal** — Uusi "Käytännön esimerkki: Microsoft Project Opal" -osio tiedostossa [15-browser-use/README.md](./15-browser-use/README.md), jossa Opal esitellään yrityskäyttöön tarkoitetuksi tietokoneen käyttöagentiksi ja sen yhteys kurssin käsitteisiin (human-in-the-loop, luottamus/turvallisuus, suunnittelu, taidot).
- **Toinen 02 Python -esimerkki** — Lisätty tiedosto [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (katso "Muutokset" — siirretty aiemmasta Semantic Kernel -muistikirjasta) ja linkitetty se oppitunnin READMEen.
- Lisätty osio **Models and Providers** tiedostoon [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Muutettu

- **Chat Completions → Responses API (Python).** Malleja suoraan kutsuneet esimerkit on siirretty Chat Completions -käytöstä Responses APIin (`client.responses.create(input=..., store=False)`, `resp.output_text`) käyttämällä `OpenAI`-asiakasta vakaassa Azure OpenAI `/openai/v1/` -päätepisteessä (ilman `api_version`-parametria). Vaikutetut esimerkit:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — täydellinen funktiokutsun läpikäynti (työkalun skeemat litistetty Responses-formaattiin, työkalun tulokset palautetaan `function_call_output`, `max_output_tokens` jne.).
- **GitHub Models → Azure OpenAI.** GitHub Models on poistumassa käytöstä (poistuu käytöstä **heinäkuussa 2026**) eikä tue Responses APIa. Kaikki GitHub Models -koodipolut on muutettu Azure OpenAI / Microsoft Foundry -käyttöön Python- ja .NET-esimerkeissä:
  - Python: Oppitunnin 08 työnkulun muistikirjat (`01`–`03`), Oppitunti 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + mukana tulevat `.md`-dokumentaatiot, sekä Oppitunnin 08 dotNET työnkulun muistikirjat/`.md` (`01`–`03`) käyttävät nyt `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` `AzureCliCredential`-todennuksella.
- **Semantic Kernel → Microsoft Agent Framework.** Aiempi `02-semantic-kernel.ipynb` on kirjoitettu uudelleen Microsoft Agent Frameworkin käyttöön Azure OpenAI:n (Responses API) kanssa ja nimetty uudelleen `02-python-agent-framework-azure-openai.ipynb`-tiedostoksi.
- **Yhtenäistetty `FoundryChatClient` + `as_agent`.** README- ja muistikirjakoodi, joka viittasi `AzureAIProjectAgentProvider`-luokkaan, on yhtenäistetty käyttämään oppitunti 01:n ja kehyksen omien esimerkkien vakiintunutta mallia: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` käyttäen `provider.as_agent(...)`. Päivitetty oppituntien 02–14 READMEissä ja muistikirjoissa (esim. Oppitunti 13 muisti, kaikki Oppitunti 14 muistikirjat, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Tuotenimet.** Nimet on uusittu englanninkielisessä aineistossa:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Ei muutosta: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ja ympäristömuuttujien nimet.)
- **Riippuvuudet** ([requirements.txt](../../requirements.txt)):
  - Lukittu `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Lukittu `openai>=1.108.1` (vähimmäisvaatimus Responses API:lle).
  - Poistettu `azure-ai-inference` (käytettiin ainoastaan siirretyissä GitHub Models -esimerkeissä).
- **Ympäristöasetukset** ([.env.example](../../.env.example)): poistettu GitHub Modelsiin liittyvät muuttujat (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lisätty `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ja valinnainen `AZURE_OPENAI_API_KEY`; nimitykset päivitetty Microsoft Foundryn mukaisiksi.
- **Dokumentaatio** — Päivitetty [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ja [STUDY_GUIDE.md](./STUDY_GUIDE.md) yllä mainittujen muutosten mukaisesti (asetukset ympäristömuuttujille, tarkistuspalaset, tarjoajaohjeistus, nimitykset).

### Poistettu

- GitHub Models -onboarding-vaiheet ja ympäristömuuttujat asetusten dokumentaatiosta (korvattu Azure OpenAI / Microsoft Foundrylla).

### Turvallisuus / Yksityisyys (julkisen jakamisen siivous)

- Tyhjennetty Jupyter-muistikirjojen suoritustulokset, jotka paljastivat aidon **Azure-tilauksen tunnuksen**, resurssiryhmän / resurssin nimet ja Bing-yhteystunnuksen sekä kehittäjän **paikalliset tiedostopolut ja käyttäjätunnukset**, seuraavissa tiedostoissa:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Varmistettu, ettei API-avaimia, tunnuksia, tilauksen tunnuksia tai henkilökohtaisia polkuja ole jäljellä seuratussa englanninkielisessä aineistossa (jäljelle jääneet `GITHUB_TOKEN`-viittaukset ovat GitHub Actions -tunnuksia työnkuluissa ja GitHub MCP palvelimen PAT Oppitunnin 11 asetuksissa — molemmat laillisia ja eivät liity GitHub Modelsiin).

### Huomioita ja tunnettuja rajoituksia

- **Ei suoritettu/käännetty.** Nämä ovat opetusesimerkkejä, jotka on päivitetty API:n ja nimien oikeellisuuden mukaan; niitä ei ole ajettu oikeilla Azure-resursseilla, eikä .NET-esimerkkejä ole käännetty tässä ympäristössä. Varmista toimivuus omassa Microsoft Foundry / Azure OpenAI -ympäristössäsi.
- **Mallin käyttöönoton on tuettava Responses APIa.** Käytä käyttöönottoa kuten `gpt-4o-mini`, `gpt-4.1` tai `gpt-5.x` -malleja. Vanhemmat mallit tukevat Responses-perustoimintoja, mutta eivät kaikkia ominaisuuksia.
- **Agent-frameworkin versio.** Esimerkit käyttävät uusinta MAF-versiota (`>=1.10.0`). Vakioagentin luontikutsu on `client.as_agent(...)`; API:t on validoitu kehyksen julkaistujen dokumenttien ja asennetun buildin perusteella. Jos lukitset eri version, varmista metodin saatavuus (`as_agent` vs `create_agent`).
- **Oppitunnin 08 työnkulun muistikirja 04** pitää tietoisesti `AzureAIAgentClient` (osana `agent-framework-azure-ai`), koska se käyttää Microsoft Foundry Agent Servicen ylläpitämiä työkaluja (Bing-perustainen, kooditulkkio); se käyttää jo Responses-pohjaista arkkitehtuuria.
- **.NET oletuskäyttöönotto.** Kaksi Oppitunnin 08 dotNET työnkulun esimerkkiä kovakoodasivat aiemmin mallin `gpt-4o`; ne käyttävät nyt oletuksena `AZURE_OPENAI_DEPLOYMENT`-ympäristömuuttujaa (`gpt-4o-mini`). Jos esimerkki käyttää multimodaalista/näkösyötettä, aseta `AZURE_OPENAI_DEPLOYMENT` sopivaksi malliksi.
- **Foundry Local** tarjoaa OpenAI-yhteensopivan **Chat Completions** -päätepisteen ja on tarkoitettu paikalliseen kehitykseen; käytä Azure OpenAI / Microsoft Foundrytä täydellisen Responses API -toiminnallisuuden saamiseksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->