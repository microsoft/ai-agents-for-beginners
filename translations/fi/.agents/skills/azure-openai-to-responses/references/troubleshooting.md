# Vianetsintä, riskitaulukko ja sudenkuopat

## 400-virheiden vianetsintä

| Virhe | Korjaus |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Työkalun määrittely käyttää vanhaa Chat Completions -sisäkkäistä formaattia | Tasota muodosta `{"type": "function", "function": {"name": ...}}` muotoon `{"type": "function", "name": ..., "parameters": ...}` — nimi, kuvaus ja parametrit siirretään ylimmälle tasolle |
| `unknown_parameter: input[N].tool_calls` | Monivaiheisen työkalun tulokset käyttävät vanhaa Chat Completions -formaattia | Korvaa `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` rakenne `response.output`-kohdilla + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` työkalulta puuttuu `required`-taulukko | Kun `strict: true`, kaikkien ominaisuuksien on oltava listattuna `required`-kentässä ja `additionalProperties: false` on asetettava |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` työkalulta puuttuu `additionalProperties: false` | Lisää `"additionalProperties": false` parametrien objektiin |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call -ID:llä väärä etuliite | Funktiokutsujen ID:iden on aloitettava `fc_` (esim. `fc_example1`), ei `call_` aloitteella |
| `missing_required_parameter: text.format.name` | Lisää `"name"`-avain formaatitietueeseen (esim. `"name": "Output"`) |
| `invalid_type: text.format` | Varmista, että `text.format` on dict, jossa on avaimet `type`, `name`, `strict`, `schema` — ei merkkijono |
| `invalid input content type` | Käytä `input_text`/`output_text` sisältötyyppejä Chatin `text` sijaan |
| `invalid input content type` (kuva) | Kuvasisältö käyttää edelleen `"type": "image_url"` | Vaihda `"type": "input_image"` |
| `Expected object, got string` kohteessa `image_url` | `image_url` on yhä sisäkkäisenä objektina `{"url": "..."}` | Tasota plain-merkkijonoksi: `"image_url": "https://..."` tai `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` kohdassa `max_output_tokens` | Minimimäärä on **16** Azure OpenAI:ssa. Käytä 50+ testaukseen, 1000+ tuotantoon. |
| `429 Too Many Requests` suoratoiston aikana | Liian monta pyyntöä. Kääri suoratoisto `try/except`-rakenteeseen, lähetä virhe JSON- muodossa käyttöliittymään, toteuta takaisinkytkentä/uudelleenyritys. |
| `KeyError: 'innererror'` sisällönsuodattimen virheessä | Sisällönsuodattimen virherakenne muuttunut Responses API:ssa | Chat Completions käytti `error.body["innererror"]["content_filter_result"]`; Responses API käyttää `error.body["content_filters"][0]["content_filter_results"]` (monikollinen, taulukossa). Kirjoita kaikki `innererror`-viittaukset uudelleen. |

---

## Migroinnin riskitaulukko

| Oire | Todennäköinen virhe | Korjaus |
|---------|---------------|-----|
| Tyhjä `output_text` / katkaistu vastaus | `max_output_tokens` liian pieni päättelymalleille | Aseta `max_output_tokens=1000` tai korkeammaksi — päättelytokenit lasketaan mukaan rajaan |
| `400 invalid_type: text.format` | Annettiin `response_format` merkkijono `text.format` dictin sijaan | Käytä `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` kohteessa `/openai/v1/responses` | Väärä `base_url` — puuttuu `/openai/v1/` loppuliite | Varmista, että `base_url=f"{endpoint}/openai/v1/"` (kauttaaltaan loppuviivalla) |
| `401 Unauthorized` vaihdettaessa `OpenAI()`-instanssiin | `api_key` ei asetettu tai token provider ei välitetty oikein | Entran ID tapauksessa: `api_key=token_provider` (callable). API-avaimella: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Malli palauttaa virheen `deployment not found` | `model`-parametri ei vastaa Azure-deploynimeäsi | Käytä `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — tämä on deploy-nimi, ei mallin nimi |
| `json.loads(resp.output_text)` antaa `JSONDecodeError`-virheen | Kaavaa ei noudateta tai malli ei tue tiukkaa JSON:ia | Varmista `"strict": True` kaavassa ja tarkista mallin tuki jäsennellylle tulostukselle |
| Streaming ei tuota `delta`-tapahtumia | Tarkastellaan väärää tapahtumatyyppiä | Suodata `event.type == "response.output_text.delta"`, älä Chatin `chat.completion.chunk` |
| `400` virhe kuvasisääntulossa migration jälkeen | Kuvasisältötyyppiä ei päivitetty | Vaihda `"type": "image_url"` → `"type": "input_image"` ja tasota `"image_url": {"url": "..."}` → `"image_url": "..."` (plain string) |
| Työkalukutsut silmukassa | Seuraavan `input` sisältää puuttuvan työkalun tuloksen | Työkalun suorituksen jälkeen lisää `{"type": "function_call_output", "call_id": ..., "output": ...}` seuraavan pyynnön `input`-kohdalle |
| `temperature`-virhe GPT-5 tai o-sarjassa | Määritetty `temperature` muuna kuin arvona 1 | Poista `temperature` tai aseta se arvoksi `1` GPT-5 ja o-sarjassa (o1, o3-mini, o3, o4-mini) |
| `top_p`-virhe o-sarjassa | `top_p` ei ole tuettu | Poista `top_p` käytettäessä o-sarjan malleja |
| `max_completion_tokens` ei tunnistettu | Käytetään Azure-spesifistä parametria | Korvaa `max_completion_tokens` arvolla `max_output_tokens`. Aseta 4096+ arvoksi o-sarjalle (päättelytokenit lasketaan mukaan) |
| Tyhjä / katkaistu output o-sarjassa | `max_output_tokens` liian pieni | O-sarja käyttää päättelytokeneita sisäisesti. Aseta `max_output_tokens=4096` tai korkeampi — ei 500–1000 |
| `400 integer_below_min_value` virhe `max_output_tokens` arvolla | Arvo alle 16 | Azure OpenAI vaatii `max_output_tokens >= 16`. Käytä 50+ savutesteissä, 1000+ tuotannossa. |
| `429 Too Many Requests` suoratoiston aikana | Azure OpenAI rajoittaa pyynnöt | Suoratoisto pysähtyy vaivihkaa ilman virheilmoitusta. Kääri `async for event in await coroutine:` aina `try/except`-rakenteeseen ja lähetä `{"error": str(e)}` käyttöliittymään. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Väärä vuokraaja tai ei kirjautuneena | Välitä `tenant_id=os.getenv("AZURE_TENANT_ID")` nimenomaisesti. Suorita `azd auth login --tenant <tenant-tunnus>` paikallisesti. |
| `404 Not Found` käyttää GitHub-malleja (`models.github.ai`) | GitHub-mallit eivät tue Responses API:a | Poista GitHub-mallien koodipolku kokonaan. Käytä Azure OpenAI:ta, OpenAI:ta tai yhteensopivaa paikallista endpointia (esim. Ollama Responses-tukena). |
| MAF:n `OpenAIChatCompletionClient` käyttää yhä Chat Completionsia | Käytössä vanha MAF-asiakasversio 1.0.0 jälkeen | MAF 1.0.0+:ssa `OpenAIChatClient` käyttää oletuksena Responses API:a. Vaihda `OpenAIChatCompletionClient` → `OpenAIChatClient`. Jos versio on alle 1.0.0, päivitä `agent-framework-openai>=1.0.0`. |
| LangChain-agentti palauttaa tyhjää tai epäonnistuu työkalukutsuissa | `ChatOpenAI` ei käytä Responses API:a | Lisää `use_responses_api=True` `ChatOpenAI(...)`:ssa. Vaihda myös `.content` → `.text` vastauksen viesteissä. |
| `KeyError: 'innererror'` sisällönsuodattimen virheenkäsittelijässä | Virherakenne muuttunut Responses API:ssa | Kirjoita `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror`-kilpi on poistettu; suodattimen tiedot löytyvät nyt pääasiallisesta `content_filters`-taulukosta, jossa kullakin kohteella on `content_filter_results` (monikollinen). |
| Raaka HTTP-pyyntö `/openai/deployments/.../chat/completions` palauttaa 404 | Vanha Chat Completions REST-päätepiste | Kirjoita URL uudelleen `/openai/v1/responses`:ksi. Muuta pyynnön runko: `messages` → `input`, lisää `max_output_tokens` + `store: false`, poista `api-version`-parametri. Muuta vastaustulkinta: `choices[0].message.content` → `output[0].content[0].text` (huom: `output_text` on SDK:n kätevyysominaisuus, ei raaka REST JSON:ssa). |

---

## Sudenkuopat

1. Jos aiemmin käytit Chat Completions -ratkaisua keskustelutilan hallintaan, hallitse oma tilasi nyt eksplisiittisesti Responsesin avulla.
2. Suosi `max_output_tokens` parametria vanhan `max_tokens` sijaan.
3. Siirtyessäsi `gpt-5`-malliin varmista, ettei `temperature` ole määritelty tai se on asetettu arvoon `1`.
4. Korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"`-arvolla käyttäjä- ja järjestelmäsyötteissä.
5. `text.format`-parametrille anna asianmukainen dict (esim. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ei pelkkää merkkijonoa.
6. `seed`-parametri ei ole tuettu Responsesissa; poista se pyynnöistä.
7. **Päätteleminen**: Lisää `reasoning` vain, jos alkuperäinen koodi sitä käytti. Älä lisää `reasoning`-parametria API-kutsuihin, joissa sitä ei ollut — monet mallit (kuten gpt-4o-mini) eivät tue tätä parametria.
8. **`max_output_tokens`-koon optimointi**: Päättelymalleissa (GPT-5-mini, GPT-5, o-sarja) käytä `max_output_tokens=4096` tai enemmän — älä 50–1000. Malli käyttää päättelytokenja sisäisesti ennen näkyvän outputin tuottamista; liian pieni raja katkaisee vastaukset tai tekee ne tyhjiksi.
9. **O-sarjan `max_completion_tokens`**: Jos alkuperäinen koodi käytti `max_completion_tokens` (Azure-spesifi o-sarjalle), korvaa se `max_output_tokens` arvolla. Responses API ei hyväksy `max_completion_tokens`:ia.
10. **O-sarjan `reasoning_effort`**: Jos alkuperäinen koodi käyttää `reasoning_effort` (low/medium/high), migratoi se muotoon `reasoning={"effort": "<arvo>"}` Responses API -kutsussa.
11. **O-sarjan suoratoiston viive**: O-sarjan mallit suorittavat sisäistä päättelyä ennen outputin tuottamista. Suoratoistossa odota pidempää viivettä ennen ensimmäistä `response.output_text.delta`-tapahtumaa. Tämä on normaalia — malli päättelijänä, ei jumiutunut.
9. **`_azure_ad_token_provider` on poistettu**: `AsyncOpenAI` / `OpenAI` eivät enää omaa `_azure_ad_token_provider` attribuuttia. Testit tai koodi, jotka tätä attribuuttia käyttävät, epäonnistuvat `AttributeError`-virheeseen. Token provider välitetään `api_key`-parametrina eikä sitä voi tarkastella client-objektista.
10. **Snapshot- / golden tiedostot**: Jos testikattauksessa käytetään snapshot-testausta, kaikkien snapshot-tiedostojen, jotka sisältävät Chat Completions -suoratoiston muotoja (`choices[0]`, `content_filter_results`, `function_call` jne.) on päivitettävä uuteen Responses-muotoon. Tämä on helppo unohtaa ja aiheuttaa snapshot-assertio-virheitä.
11. **Mock monkeypatch -polku**: Monkeypatch-kohde muuttuu `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (tai synkronisena `Responses.create`). Vanhan polun käyttäminen ei tee mitään - mock ei nappaa kutsuja ja testit osuvat oikeaan API:iin tai epäonnistuvat.
12. **`input` ei `messages`**: Mock-funktioiden pitää lukea `kwargs.get("input")` eikä `kwargs.get("messages")`. Responses API käyttää `input` keskustelun historiaan.
13. **Ympäristömuuttujien nimiketottumus**: Azure Identity SDK käyttää `AZURE_CLIENT_ID` (ei `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` tapauksessa. Nimeä uudelleen testeissä, `.env`-tiedostoissa, app-asetuksissa ja Bicep/infra-konfiguraatiossa.
14. **`max_output_tokens`:in minimi on 16**: Azure OpenAI hylkää alle 16 arvot virheellä `400 integer_below_min_value`. Käytä 50 savutestaukseen, 1000+ tuotantoon. Vanha `max_tokens` ei asettanut tällaista minimirajaa.
15. **`tenant_id` AzureDeveloperCliCredentialille**: Kun Azure OpenAI -resurssi on eri vuokraajassa, sinun **on** annettava `tenant_id` nimenomaisesti — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Ilman tätä tunnistautuminen käyttää hiljaisesti väärää vuokraajaa ja palauttaa `401`-virheen.
16. **Rajapinnat rajoittuvat eri tavalla suoratoistossa**: Chat Completionsissa 429 esti tavallisesti suoratoiston aloittamisen. Responses API -suoratoistossa 429 voi tapahtua **kesken streamin** — async iterator nostaa poikkeuksen. Kääri suoratoistolista silmukka aina `try/except`-rakenteeseen ja lähetä virhe-JSON-rivi, jotta käyttöliittymä voi käsitellä tilanteen siististi.

17. **Reaaliaikainen virheenkäsittely on pakollista verkkosovelluksissa**: Kuvio `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` on kriittinen. Ilman sitä SSE/JSONL virta lakkaa hiljaisesti toimimasta palvelimen puoleisessa virhetilanteessa ja käyttöliittymä jumittuu.
18. **Työkalumäärittelyissä on käytettävä tasaista rakennetta**: Responses API odottaa `{"type": "function", "name": ..., "parameters": ...}` — ei Chat Completionsin sisäkkäistä muotoa `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Tämä on yleisin virhe koodin migraatiossa, joka kutsuu funktioita.
19. **`pydantic_function_tool()` ei ole yhteensopiva**: `openai.pydantic_function_tool()` apuohjelma tuottaa edelleen vanhan sisäkkäisen rakenteen. Älä käytä sitä yhdessä `responses.create()` kanssa. Määrittele työkaluarkkitehtuurit käsin tai tasoita tulos.
20. **Työkalujen tulokset käyttävät `function_call_output`, eivät `role: tool`**: Työkalun suorittamisen jälkeen liitä `{"type": "function_call_output", "call_id": ..., "output": ...}` — ei `{"role": "tool", "tool_call_id": ..., "content": ...}`. Avustajan työkalupyyntöön käytä `messages.extend(response.output)` — ei manuaalista `{"role": "assistant", "tool_calls": [...]}` sanakirjaa.
21. **`strict: true` vaatii `required` + `additionalProperties: false`**: Kun käytät `strict: true` työkalussa, jokaisen ominaisuuden on oltava `required`-arrayn listalla ja `additionalProperties` on oltava `false`. Toisen puuttuminen aiheuttaa 400-virheen.
22. **Funktiokutsujen tunnisteilla on tietyt etuliitteet**: Kun annetaan few-shot `function_call` -kohteita `input`-kentässä, `id`-kentän on aloitettava `fc_` ja `call_id`-kentän `call_` (esim. `"id": "fc_example1", "call_id": "call_example1"`). Vanhan Chat Completionsin `call_`-etuliitteen käyttö `id`-kentässä hylätään.
23. **GitHub Models ei tue Responses APIa**: Jos sovelluksessa on GitHub Modelsin koodipolku (`base_url`, joka osoittaa `models.github.ai` tai `models.inference.ai.azure.com`), poista se kokonaan. Siirtymäpolkua ei ole — vaihda Azure OpenAI:hin, OpenAI:hin tai yhteensopivaan paikalliseen päätepisteeseen.
24. **Sisällönsuodattimen virherakenteet muuttuivat**: Chat Completions -virheet käyttivät `error.body["innererror"]["content_filter_result"]` (yksikkö). Responses API -virheet käyttävät `error.body["content_filters"][0]["content_filter_results"]` (monikko, taulukon sisällä). `innererror`-avain ei enää ole olemassa. Koodi, joka pääsee suoraan `innererror`:iin, heittää `KeyError`-poikkeuksen suoritusaikana — tämä voi helposti jäädä huomaamatta migraatiossa, koska se ilmenee vain, kun sisältösuodatin aktivoituu. Etsi aina `innererror`:ia migraation aikana.
25. **Raakatason HTTP-kutsut vaativat URL:n ja viestin uudelleenkirjoituksen**: Sovellukset, jotka kutsuvat Azure OpenAI RESTiä suoraan (`requests`, `httpx`, `aiohttp`) käyttämällä `/openai/deployments/{name}/chat/completions?api-version=...` on vaihdettava käyttämään `/openai/v1/responses`. Pyyntöviestissä käytetään `input`-kenttää `messages`-kentän sijaan, ja vaaditaan `max_output_tokens` sekä `store`. `api-version`-kyselyparametri poistetaan käytöstä. Vastausviestin teksti on osoitteessa `output[0].content[0].text` — **ei** `output_text`, joka on SDK:n kätevyysominaisuus eikä ole olemassa raakassa REST JSONissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->