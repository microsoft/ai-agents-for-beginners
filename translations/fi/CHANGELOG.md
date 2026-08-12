# Muutokset

Kaikki merkittävät muutokset **AI Agents for Beginners** -kurssilla on dokumentoitu tässä tiedostossa.

## [Julkaistu] — 2026-07-14

Tämä julkaisu siirtää kurssin kahdelta juuri poistuneelta mallilta, siirtää jäljellä olevat Oppitunti-muistikirjat vakaaseen Microsoft Agent Framework -sovellusliittymään ja validoi Python-muistikirjat elävällä Microsoft Foundry -ympäristöllä.

### Muutettu

- **Siirretty pois poistuneista malleista (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Sekä `gpt-4.1` että `gpt-4.1-mini` on nyt poistettu käytöstä (julkaistu poistopäivämäärä **14. lokakuuta 2026**). Korvattu kaikki kurssiviittaukset (dokumentit, `.env.example`, Python/.NET-muistikirjat ja esimerkit) ei-poistuneella `gpt-5-mini` -mallilla. Oppitunnin 16 mallin reititysesimerkki säilyttää pienet/suuret erot käyttäen `gpt-5-nano` (pieni) ja `gpt-5-mini` (iso). Kolmannen osapuolen tiedostot ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historiallinen GitHub Models -teksti ja `azure-openai-to-responses` -taidon kyvytiedot jätettiin tahallaan muuttumattomiksi.
- **Oppitunti 14 siirto-muistikirja siirretty vakaaseen sovellusliittymään.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) käyttää nyt `agent_framework.orchestrations.HandoffBuilder` -luokkaa, jonka metodeina ovat `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-pohjainen striimaus ja `FoundryChatClient` (korvaa poistuneet pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` symbolit).
- **Oppitunti 14 ihmisen-ohjaus -muistikirja siirretty vakaaseen sovellusliittymään.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pysähtyy `ctx.request_info(...)` + `@response_handler` yhdistelmällä (korvaa poistuneet `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), rakentuu `WorkflowBuilder(start_executor=..., output_executors=[...])` avulla, ohjaa jäsenneltyä ulostuloa `default_options={"response_format": ...}` kautta ja käyttää käsikirjoitettua vastausta, jolloin muistikirja toimii itsenäisesti (ei estävää `input()`-komentoa).
- **Ympäristöasetukset** ([.env.example](../../.env.example)): mallin käyttöönoton nimet vaihdettiin `gpt-5-mini`:ksi; lisättiin `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Oppitunti 16 reititys) ja aiemmin puuttunut `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Oppitunti 15 selainkäyttö).
- **Riippuvuudet** ([requirements.txt](../../requirements.txt)): lukittu `agent-framework`, `agent-framework-foundry` ja `agent-framework-openai` versioon `~=1.10.0` itseään vastaavaksi ja validoiduksi sarjaksi (versio 1.11.0 tuo kokeellisia yhteensopimattomia muutoksia näihin oppitunteihin liittyviin pintaosiin).

### Huomiot ja tunnetut rajoitteet

- **Validoitu elävää Microsoft Foundry -ympäristöä vastaan.** Python-muistikirjat suoritettiin ilman käyttöliittymää `nbconvert`-työkalulla Microsoft Foundry -hankkeen ympäristössä käyttäen `gpt-5-mini` (ja `gpt-5-nano` Oppitunti 16 reititykseen). Ota käyttöön vastaavat ei-poistetut mallit omassa projektissasi; muistikirjat lukevat käyttöönoton nimen ympäristömuuttujista `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Jotkin oppitunnit vaativat edelleen lisäresursseja.** Oppitunti 05 tarvitsee Azure AI Searchin; Oppitunti 08 Bing-taustoitus työnkulku (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) tarvitsee Bing-yhteyden ja Microsoft Foundry Agent Service -ismääriteltyjä työkaluja; Oppitunti 13 (Cognee) ja Oppitunti 17 (Foundry Local) tarvitsevat omat suoritusaikansa.

## [Julkaistu] — 2026-07-13

Tämä julkaisu sisältää kaksi uutta oppituntia, jotka täydentävät käyttöönottoa — agenttien skaalaamisen Microsoft Foundryyn ja alas yhdelle työasemalle — sekä savutestausputken, uudistetun kurssisivuston, uusia oppijataitoja ja päivitetyn brändäyksen.

### Lisätty

- **Oppitunti 16 — Skaalautuvien agenttien käyttöönotto Microsoft Foundrylla.** Uusi oppitunti [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ja suoritettava muistikirja [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) rakentaa tuotantoasiakastuen agentin (työkalut, RAG, muisti, mallin reititys, vastausten välimuisti, ihmisen hyväksyntä, arviointipiste ja OpenTelemetry-jäljitys), mukana kehitys-/käyttöönottovaiheen Mermaid-kaaviot, tietovisan, tehtävän ja haasteen.
- **Oppitunti 17 — Paikallisten AI-agenttien rakentaminen Foundry Localilla ja Qwenillä.** Uusi oppitunti [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ja muistikirja [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), joka rakentaa täysin laitteella toimivan teknisen avustajan (Qwen-funktiokutsut Foundry Localin kautta, hiekkalaatikkotiedostotyökalut, paikallinen RAG Chroman avulla, valinnainen paikallinen MCP), sisältäen paikalliset / paikallinen RAG / työkalukutsujen kaaviot, tietovisan, tehtävän ja haasteen.
- **Savutestausputki.** Uusi [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) -työnkulku [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) sekä oppitunnikohtaiset luettelot [tests/](./tests/README.md) deployattavien agenttien testaukseen Oppitunneilla 01, 04, 05 ja 16, sisältäen hakemiston README:n jolla luettelot liitetään oppitunteihin ja isäntäagenttien nimiin. Oppitunti 16 saa "Validoidaan käyttöönotettu agentti savutesteillä" -osion; Oppitunnit 01/04/05 saavat valinnaisen savutestausosoittimen.
- **Oppijat taidot.** Uudet Agent Skills -taidot kansiossa `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (paketoivat Oppituntien 16 ja 17 ohjeistukset) ja [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kuinka validoida muistikirjaesimerkit elävää Microsoft Foundry / Azure OpenAI -ympäristöä vastaan).
- **Muistikirjojen validoija.** Uusi [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) joka suorittaa kaikki Python-muistikirjat ilman käyttöliittymää `nbconvert`-työkalulla ja tulostaa PASS/FAIL-matriisin (sekä `results.json`). Se tunnistaa automaattisesti pääkansion ja Pythonin, sulkee oletuksena pois ei-kurssimuistikirjat (`.venv`, `site-packages`, `translations`, taitomallien resurssit) sekä `.NET`-muistikirjat ja tukee `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ja `-Python` asetuksia.
- **Kurssin navigointi.** Lisätty Edellinen/Seuraava oppitunti -linkit Oppitunneille 11–15 (jotka aiemmin puuttuivat) joten koko kurssi on sidottu ketjuksi 00 → 18 molempiin suuntiin.
- **Uudet pikkukuvat.** Oppituntien 16 ja 17 pikkukuvat, sekä päivitetty arkiston sosiaalinen kuva [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (mainostaen kahta uutta oppituntia ja URL-osoitetta `aka.ms/ai-agents-beginners`).
- **Riippuvuudet** ([requirements.txt](../../requirements.txt)): lisätty `foundry-local-sdk` ja `chromadb` Oppituntaa 17 varten.

### Muutettu

- **Pää-README-taulukko:** Oppitunnit 16 ja 17 nyt linkitetty sisältöönsä (aikaisemmin "Tulossa pian"); arkiston kuva päivitetty `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Oppitunnit 16 ja 17 lisätty oppitunti-oppaan ja oppimispolkujen joukkoon, sekä "Validoidaan käyttöönotetut agentit savutesteillä" -osio.
- **[AGENTS.md](./AGENTS.md)**: päivitetty oppituntien lukumäärä/kuvaus (00–18), lisätty savutestausvalidaatio-osio ja oppituntien 16/17 esimerkkinimet.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Edellinen oppitunti" osoittaa nyt Oppitunti 17:ään (aiemmin Oppitunti 15), sulkien ketjun.
- **Standardoitu malliviittaukset ei-poistuneille malleille.** Korvattu kaikki `gpt-4o` / `gpt-4o-mini` viittaukset kurssilla (dokumentit, `.env.example`, Python/.NET-muistikirjat ja esimerkit) `gpt-4.1-mini`:llä — `gpt-4o` (kaikki versiot) jää eläkkeelle vuonna 2026. Oppitunnin 16 mallin reititysesimerkki säilyttää pienet/suuret erot käyttäen `gpt-4.1-mini` (pieni) ja `gpt-4.1` (iso). Python-muistikirjat valitsevat nyt mallin ympäristömuuttujista (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) kovakoodatun mallin nimen sijaan.

### Huomiot ja tunnetut rajoitteet

- **Ei suoritettu elävää Azure-ympäristöä vasten.** Uusien oppituntien muistikirjat ovat opetusesimerkkejä; suorita ja validoi ne omassa Microsoft Foundry / Foundry Local -ympäristössä. Savutestausprosessissa vaaditaan, että otat käyttöön oppitunnin agentin ja konfiguroit Azure OIDC -salaisuudet (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) käyttäen **Azure AI User** -roolia Foundryn hankkeen tasolla.
- **Oppitunti 17 on vain paikallinen.** Siinä ei ole Foundry Responses -päätepistettä, joten savutestaustoiminto ei koske sitä; validoi suorittamalla muistikirja työasemallasi.

## [Julkaistu] — 2026-07-06

Tämä julkaisu siirtää kurssin **Azure OpenAI Responses API -rajapintaan**, vakioi tuotemerkit **Microsoft Foundry** ja **Microsoft Agent Framework (MAF)** nimien ympärille, poistaa GitHub Modelsin käytöstä, päivittää SDK-versioita ja lisää uutta sisältöä paikallisista malleista ja muiden kehysten isännöinnistä Foundryssa.

### Lisätty

- **Migraatiotaito** — Asennettu [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (lähteestä [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) kansioon `.agents/skills/`, mukaan lukien viitteet ja skannauskomentosarja.
- **Foundry Local (ajetaan malleja laitteessa)** — Uusi "Vaihtoehtoinen tarjoaja: Foundry Local" -osio [00-course-setup/README.md](./00-course-setup/README.md), joka kattaa asennuksen (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ja `FoundryLocalManager`-kytkennän Microsoft Agent Frameworkiin `OpenAIChatClient`-kautta.
- **LangChain / LangGraph agenttien isännöinti Microsoft Foundryssa** — Uusi osio [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ja suoritettava esimerkki [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), joka käyttää `langchain-azure-ai[hosting]` ja `ResponsesHostServer`-protokollaa (`/responses`) Microsoft Learn -ohjeistuksen perusteella.
- **Microsoft Project Opal** — Uusi "Todellisen maailman esimerkki: Microsoft Project Opal" -osio [15-browser-use/README.md](./15-browser-use/README.md), joka esittelee Opalin yritystason tietokoneen käyttöagenttina ja liittää sen kurssin käsitteisiin (ihmisen ohjaus, luottamus/turva, suunnittelu, taidot).
- **Toinen Oppitunti 02 Python-esimerkki** — Lisätty [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (katso "Muutettu" — siirtynyt aiemmasta Semantic Kernel -muistikirjasta) ja lisätty linkki oppitunnin README-tiedostoon.
- **Mallit ja tarjoajat** -osio lisätty [STUDY_GUIDE.md](./STUDY_GUIDE.md) tiedostoon.

### Muutettu

- **Chat Completions → Responses API (Python).** Mallia kutsuneet esimerkit siirrettiin Chat Completionsista käyttämään Responses API:a (`client.responses.create(input=..., store=False)`, `resp.output_text`), käyttäen `OpenAI`-asiakasta vakaan Azure OpenAI `/openai/v1/` rajapinnan kanssa (ilman `api_version`-parametria). Vaikutetut esimerkit sisältävät:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — koko funktiokutsun läpikäynti (työkalun skeema muutettu Responses-muotoon, työkalun tulokset palautetaan `function_call_output`, `max_output_tokens` jne. muuttujina).

- **GitHub Models → Azure OpenAI.** GitHub Models on vanhentunut (poistuu käytöstä **heinäkuussa 2026**) eikä tue Responses API:a. Kaikki GitHub Models -koodipolut muunnettiin Azure OpenAI / Microsoft Foundry -käyttöön Python- ja .NET-esimerkeissä:
  - Python: Lesson 08 työnkulkujen muistikirjat (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + näiden kumppanidokumentit `.md`-muodossa, sekä Lesson 08 dotNET-työnkulkujen muistikirjat/`.md` (`01`–`03`) käyttävät nyt `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` `AzureCliCredential`-tunnistetiedoilla.
- **Semantic Kernel → Microsoft Agent Framework.** Entinen `02-semantic-kernel.ipynb` kirjoitettiin uudelleen käyttämään Microsoft Agent Frameworkia Azure OpenAI:n (Responses API) kanssa ja nimettiin uudelleen `02-python-agent-framework-azure-openai.ipynb`.
- **Standardoitu `FoundryChatClient` + `as_agent` käyttöön.** README- ja muistikirjakoodissa, joka viittasi `AzureAIProjectAgentProvider`iin, on standardoitu kanoniseen kaavaan, jota käytetään Lesson 01:ssa ja kehyksen omissa esimerkeissä: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ja `provider.as_agent(...)`. Päivitetty Lesson 02–14 READMEn ja muistikirjojen kautta (esim. Lesson 13 muisti, kaikki Lesson 14 muistikirjat, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Tuotenimikkeistö.** Nimettiin englanninkielisessä sisällössä kauttaaltaan:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Säilyi ennallaan: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ja ympäristömuuttujien nimet.)
- **Riippuvuudet** ([requirements.txt](../../requirements.txt)):
  - Lukittu `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Lukittu `openai>=1.108.1` (vähimmäisvaatimus Responses API:lle).
  - Poistettu `azure-ai-inference` (käytettiin vain siirretyissä GitHub Models -esimerkeissä).
- **Ympäristöasetukset** ([.env.example](../../.env.example)): poistettu GitHub Models -muuttujat (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lisätty `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ja valinnainen `AZURE_OPENAI_API_KEY`; päivitetty Microsoft Foundry -nimeämisen mukaiseksi.
- **Dokumentaatio** — Päivitetty [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ja [STUDY_GUIDE.md](./STUDY_GUIDE.md) yllämainittujen mukaisesti (ympäristömuuttujat, tarkistusliuska, toimittajan ohjeistus, nimeäminen).

### Poistettu

- GitHub Models onboarding-vaiheet ja ympäristömuuttujat asennusdokumenteista (korvattu Azure OpenAI / Microsoft Foundry -käytöllä).

### Turvallisuus / Yksityisyys (julkisen jakamisen siivous)

- Tyhjennetty Jupyter-muistikirjojen suoritustulokset, jotka vuodattivat todellisen **Azure-tilauksen tunnuksen**, resurssiryhmän / resurssien nimet ja Bing-yhteystunnuksen, sekä kehittäjien **paikalliset tiedostopolut ja käyttäjänimet** seuraavissa tiedostoissa:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Varmistettu, ettei API-avaimia, tunnuksia, tilauksien tunnuksia tai henkilökohtaisia polkuja ole jäljellä seuratuissa englanninkielisissä sisällöissä (jäljelle jääneet `GITHUB_TOKEN`-viittaukset ovat GitHub Actions -tunnuksia työnkuluissa ja GitHub MCP -palvelimen PAT Lesson 11:n asennuksessa — molemmat laillisia ja eivät liity GitHub Modelsiin).

### Huomautuksia ja tunnettuja rajoituksia

- **Ei ajettu/käännetty.** Nämä ovat opetusesimerkkejä, jotka on päivitetty API-/nimikkeiden oikeellisuuden mukaisiksi; niitä ei ajettu reaaliaikaisissa Azure-resursseissa, eikä .NET-esimerkkejä käännetty tässä ympäristössä. Varmista oma Microsoft Foundry / Azure OpenAI -asennuksesi.
- **Mallin käyttöönoton on tuettava Responses API:a.** Käytä käyttöönottoa kuten `gpt-4.1-mini`, `gpt-4.1` tai `gpt-5.x` -mallia. Vanhemmat mallit tukevat Responses-perustoimintoja, mutta eivät kaikkia ominaisuuksia.
- **Agent-framework -versio.** Esimerkit on suunnattu uusimpaan MAF-versioon (`>=1.10.0`). Kanoninen agentin luontikutsu on `client.as_agent(...)`; rajapinnat on validoitu kehyksen julkaistujen dokumenttien ja asennetun buildin kanssa. Jos lukitset eri version, varmista metodin saatavuus (`as_agent` vs `create_agent`).
- **Lesson 08 työnkulun muistikirja 04** pitää tarkoituksella `AzureAIAgentClient`in (from `agent-framework-azure-ai`), koska se käyttää Microsoft Foundry Agent Service -isännöityjä työkaluja (Bing-lähtöisyys, kooditulkitseja); se perustuu jo Responses-rajapintaan.
- **.NET oletuskäyttöönotto.** Kaksi Lesson 08 dotNET-työnkulun esimerkkiä asetti aikaisemmin kovakoodatun mallin; ne käyttävät nyt oletuksena `AZURE_OPENAI_DEPLOYMENT`-arvoa (`gpt-4.1-mini`). Jos esimerkki tarvitsee multimodaalisen/näkösyötteen, aseta `AZURE_OPENAI_DEPLOYMENT` sopivaan malliin.
- **Foundry Local** tarjoaa OpenAI-yhteensopivan **Chat Completions** -päätepisteen ja on tarkoitettu paikalliseen kehitykseen; käytä Azure OpenAI / Microsoft Foundrytä koko Responses API -ominaisuusjoukon käyttöön.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->