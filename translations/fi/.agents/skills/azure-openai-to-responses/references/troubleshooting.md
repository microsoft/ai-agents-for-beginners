# Vianmääritys, Riskitaulukko & Varoitukset

## Vianmääritys 400-virheisiin

| Virhe | Korjaus |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Työkalun määrittely käyttää vanhaa Chat Completionsin sisäkkäistä rakennetta | Muunna rakenteesta `{"type": "function", "function": {"name": ...}}` muotoon `{"type": "function", "name": ..., "parameters": ...}` — nimi, kuvaus ja parametrit ovat ylimmällä tasolla |
| `unknown_parameter: input[N].tool_calls` | Monivaiheisen työkalun tulokset käyttävät vanhaa Chat Completionsin rakennetta | Korvaa `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` kohteilla `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` -työkalulta puuttuu `required`-taulukko | Kun `strict: true`, kaikkien ominaisuuksien on oltava listattuna `required`, ja `additionalProperties: false` on asetettava |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` -työkalulta puuttuu `additionalProperties: false` | Lisää `"additionalProperties": false` parametrien objektiin |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call -tunnuksen etuliite on väärä | Funktion kutsun tunnuksen on aloitettava `fc_` (esim. `fc_example1`), ei `call_` |
| `missing_required_parameter: text.format.name` | Lisää `name`-avain formaatin sanakirjaan (esim. `"name": "Output"` ) |
| `invalid_type: text.format` | Varmista, että `text.format` on sanakirja, jossa on `type`, `name`, `strict`, `schema` avaimet — ei merkkijono |
| `invalid input content type` | Käytä `input_text` / `output_text` sisältötyyppejä Chatin `text` sijaan |
| `invalid input content type` (kuva) | Kuvasisältö käyttää edelleen `"type": "image_url"` | Vaihda tyyppiin `"type": "input_image"` |
| `Expected object, got string` `image_url`:ssa | `image_url` on yhä sisäkkäinen objekti `{"url": "..."}` | Muuta yksinkertaiseksi merkkijonoksi: `"image_url": "https://..."` tai `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` `max_output_tokens`:lle | Azure OpenAI:n minimi on **16**. Testeissä käytä yli 50, tuotannossa yli 1000. |
| `429 Too Many Requests` streamauksen aikana | Rajoitettu käytön mukaan. Kääri streaming `try/except`-lohkolla, tuota virhe-JSON frontendiin, toteuta palaute ja uusiyritys. |
| `KeyError: 'innererror'` sisältö suodattimen virheessä | Sisältösuodattimen virherakenteet muuttuneet Responses API:ssa | Chat Completions käytti `error.body["innererror"]["content_filter_result"]`; Responses API käyttää `error.body["content_filters"][0]["content_filter_results"]` (monikossa, taulukossa). Muuta kaikki `innererror`-viittaukset. |

---

## Siirtymän Riskitaulukko

| Oire | Todennäköinen Virhe | Korjaus |
|---------|---------------|-----|
| Tyhjä `output_text` / katkaistu vastaus | `max_output_tokens` liian pieni päättelymalleille | Aseta `max_output_tokens=1000` tai suurempi — päättelytokenit luetaan mukaan rajaan |
| `400 invalid_type: text.format` | Annettu `response_format` merkkijono `text.format`-sanakirjan sijaan | Käytä `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` `/openai/v1/responses`-polussa | Väärä `base_url` — puuttuu `/openai/v1/` loppu | Varmista `base_url=f"{endpoint}/openai/v1/"` (viimeisellä kauttaviivalla) |
| `401 Unauthorized` vaihdon jälkeen `OpenAI()`-käyttöön | `api_key` ei asetettu tai token provideria ei annettu oikein | Entralle: `api_key=token_provider` (kutsuttava). API-avaimelle: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Malli palauttaa `deployment not found` | `model`-parametri ei vastaa Azure-jakelusi nimeä | Käytä `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — tämä on jakelun nimi, ei mallin nimi |
| `json.loads(resp.output_text)` aiheuttaa `JSONDecodeError`-virheen | Skeemaa ei ole pakotettu tai malli ei tue tiukkaa JSON:ia | Varmista, että skeemassa on `"strict": True` ja tarkista, että malli tukee jäsenneltyä ulostuloa |
| Streaming ei tuota `delta`-tapahtumia | Tarkistetaan väärää tapahtumatyyppiä | Suodata `event.type == "response.output_text.delta"`, ei Chatin `chat.completion.chunk` |
| `400` virhe kuvan syötteelle siirtymän jälkeen | Kuvasisältötyyppiä ei ole päivitetty | Muuta `"type": "image_url"` → `"type": "input_image"` ja tasoita `"image_url": {"url": "..."}` → `"image_url": "..."` (pelkkä merkkijono) |
| Työkalukutsut ajautuvat loputtomaan silmukkaan | Seuraavan pyynnön `input`:stä puuttuu työkalun tulos | Työkalun suorittamisen jälkeen lisää `input`-listaan kohde `{"type": "function_call_output", "call_id": ..., "output": ...}` seuraavaan pyyntöön |
| `temperature`-virhe GPT-5:n tai o-sarjan kanssa | Muuten kuin 1 asetettu eksplisiittisesti | Poista `temperature` tai aseta se arvoon `1` GPT-5:lle ja o-sarjan malleille (o1, o3-mini, o3, o4-mini) |
| `top_p`-virhe o-sarjan kanssa | `top_p` ei tuettu | Poista `top_p`, kun käytät o-sarjan malleja |
| `max_completion_tokens` ei tunnisteta | Azure-spesifinen parametri käytössä | Korvaa `max_completion_tokens` parametrilla `max_output_tokens`. Aseta 4096+ o-sarjalle (päättelytokenit lasketaan mukaan) |
| Tyhjä tai katkaistu vastaus o-sarjalta | `max_output_tokens` liian pieni | O-sarja käyttää sisäisesti päättelytokeneita. Aseta `max_output_tokens=4096` tai suurempi — ei 500–1000. |
| `400 integer_below_min_value` `max_output_tokens`:lle | Arvo alle 16 | Azure OpenAI vaatii `max_output_tokens >= 16`. Käytä 50+ savutesteissä, 1000+ tuotannossa. |
| `429 Too Many Requests` kesken streamauksen | Rajoitus Azure OpenAI:sta | Stream katkeaa hiljaa ilman virheilmoitusta. Kääri `async for event in await coroutine:` aina `try/except` lohkoon ja tuota virhe-JSON frontendiin. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Väärä tenantti tai ei kirjautunut sisään | Anna `tenant_id=os.getenv("AZURE_TENANT_ID")` selkeästi. Suorita `azd auth login --tenant <tenant-id>` paikallisesti. |
| `404 Not Found` GitHub-malleilla (`models.github.ai`) | GitHub-mallit eivät tue Responses API:a | Poista GitHub-mallien koodipolku kokonaan. Käytä Azure OpenAI:ta, OpenAI:ta tai yhteensopivaa paikallista päätepistettä (esim. Ollama, jossa on Responses-tuki). |
| MAF `OpenAIChatCompletionClient` käyttää edelleen Chat Completionseja | Käytössä vanha MAF-asiakasversio 1.0.0+ | MAF 1.0.0+ käyttää oletuksena Responses API:a `OpenAIChatClient`-luokassa. Vaihda `OpenAIChatCompletionClient` luokasta `OpenAIChatClient`:iin. Ennen 1.0.0 versiota päivitä `agent-framework-openai>=1.0.0`. |
| LangChain-agentti palauttaa tyhjän tai epäonnistuu työkalukutsuissa | `ChatOpenAI` ei käytä Responses API:a | Lisää `use_responses_api=True` `ChatOpenAI(...)`:n argumentteihin. Vaihda myös vastausviestien `.content` → `.text` käyttöön. |
| `KeyError: 'innererror'` sisältösuodattimen virheen käsittelijässä | Virherakenteet muuttuneet Responses API:ssa | Muuta `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror`-kääre on poistettu; sisältösuodattimen tiedot ovat nyt ylimmällä tasolla `content_filters`-taulukossa, jossa sisällä `content_filter_results` (monikossa). |
| Raw HTTP -kutsussa `/openai/deployments/.../chat/completions` tulee 404 | Vanha Chat Completions REST-päätepiste | Vaihda URL-osoitteeksi `/openai/v1/responses`. Muuta pyynnön runko: `messages` → `input`, lisää `max_output_tokens` + `store: false`, poista `api-version`-kyselyparametri. Muuta vastausparsing: `choices[0].message.content` → `output[0].content[0].text` (huomaa, että `output_text` on SDK:n helpotustoiminto, ei raakassa REST-JSONissa). |

---

## Varoitukset

1. Jos käytit aiemmin Chat Completionsia keskustelutilan hallintaan, hallitse tila itse eksplisiittisesti Responses avulla.
2. Suosi `max_output_tokens`-parametria vanhan `max_tokens` sijaan.
3. Siirtyessäsi `gpt-5`:een varmista, ettei `temperature`-parametriä anneta tai sen arvo on `1`.
4. Korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"` -muodolla käyttäjä- tai järjestelmäsisääntuloissa.
5. `text.format`-kenttään toimita asianmukainen sanakirja (esim. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ei pelkkää merkkijonoa.
6. `seed`-parametriä ei tueta Responses API:ssa, poista se pyyntöjen yhteydestä.
7. **Päättely**: Sisällytä `reasoning`-parametri vain, jos alkuperäinen koodi sitä käytti. Älä lisää `reasoning`-parametria API-kutsuihin, joissa sitä ei ollut — monet ei-päättelymallit eivät tue sitä.
8. **`max_output_tokens` koko**: Päättelymalleille (GPT-5-mini, GPT-5, o-sarja) käytä `max_output_tokens=4096` tai suurempi — ei 50–1000. Malleilla on sisäinen päättelytokenien käyttö ennen näkyvää vastausta; liian pienet arvot aiheuttavat katkaisuja tai tyhjiä vastauksia.
9. **O-sarjan `max_completion_tokens`**: Jos alkuperäinen koodi käytti `max_completion_tokens` (Azure-spesifi o-sarjalle), korvaa se `max_output_tokens`:lla. Responses API ei tue `max_completion_tokens`-parametria.
10. **O-sarjan `reasoning_effort`**: Jos alkuperäinen koodi käyttää `reasoning_effort` (low/medium/high), siirrä se muotoon `reasoning={"effort": "<arvo>"}` Responses API -kutsussa.
11. **O-sarjan streamauksen viive**: O-sarjan mallit suorittavat sisäistä päättelyä ennen ulostulon generointia. Streamatessa odota pidempää viivettä ennen ensimmäistä `response.output_text.delta` tapahtumaa. Tämä on normaalia — malli miettii, ei jää jumiin.
9. **`_azure_ad_token_provider` on poistettu**: `AsyncOpenAI` / `OpenAI` -luokilla ei ole `_azure_ad_token_provider`-attribuuttia. Testit tai koodi, jotka yrittävät käyttää sitä, epäonnistuvat `AttributeError`-virheeseen. Token provider annetaan `api_key`-parametrina eikä sitä voi tarkastella asiakasobjektista.
10. **Snapshot / kultaiset tiedostot**: Jos testisetti käyttää snapshot-testausta, **kaikki** snapshot-tiedostot, jotka sisältävät Chat Completionsin streaming-muotoja (`choices[0]`, `content_filter_results`, `function_call` jne.) on päivitävä uuteen Responses-muotoon. Tämä on helposti unohtuva seikka, joka aiheuttaa snapshot-vertailuvirheitä.
11. **Mock monkeypatchin polku**: Monkeypatchin kohde muuttuu polusta `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (tai synkroniselle `Responses.create`). Vanhaa polkua käyttäen miksaus ei estä oikeaa API-kutsua eikä mockkaus onnistu.
12. **`input` ei `messages`**: Mock-funktioiden tulee lukea `kwargs.get("input")` ei `kwargs.get("messages")`. Responses API käyttää `input`-kenttää keskusteluhistorialle.
13. **Ympäristömuuttujien nimet**: Azure Identity SDK käyttää `AZURE_CLIENT_ID` (ei `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` käyttöön. Nimeä uudelleen testeissä, `.env`-tiedostoissa, sovellusasetuksissa ja Bicep/infrastruktuurissa.
14. **`max_output_tokens`:n minimi on 16**: Azure OpenAI hylkää arvot alle 16 virheilmoituksella `400 integer_below_min_value`. Käytä 50 savutesteissä, 1000 tai enemmän tuotannossa. Vanhemmalla `max_tokens`-parametrilla ei ollut tällaista minimivaatimusta.
15. **`tenant_id` `AzureDeveloperCliCredential`-konstruktorissa**: Kun Azure OpenAI -resurssi on eri tenantissa, sinun **täytyy** välittää `tenant_id` eksplisiittisesti — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Ilman sitä tunniste käyttää hiljaa väärää tenanttia ja palauttaa 401-virheen.
16. **Rajoitukset näkyvät eri tavalla streamauksessa**: Chat Completionsissa 429-virhe tavallisesti esti streamin aloittamisen. Responses API:n streamauksessa 429 voi tapahtua kesken streamin — asynkroninen iteraattori heittää poikkeuksen. Kääri streamaus silmukka aina `try/except`-lohkolla ja tuota virhe-JSON-rivi, jotta frontend voi käsitellä tilanteen sujuvasti.

17. **Virheiden käsittely suoratoistossa on pakollista verkkosovelluksissa**: Malli `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` on ratkaisevan tärkeä. Ilman sitä SSE/JSONL-suodin kuolee hiljaisesti mihin tahansa palvelinpuolen virheeseen ja käyttöliittymä jää jumiin.
18. **Työkalujen määritelmien on käytettävä tasaista rakennetta**: Responses API odottaa `{"type": "function", "name": ..., "parameters": ...}` — ei Chat Completionsin sisäkkäistä `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Tämä on yleisin migraatiovirhe funktionkutsua koodissa tehtäessä.
19. **`pydantic_function_tool()` ei ole yhteensopiva**: `openai.pydantic_function_tool()` -apufunktio tuottaa edelleen vanhan sisäkkäisen rakenteen. Älä käytä sitä yhdessä `responses.create()` kanssa. Määrittele työkalujen skeemat manuaalisesti tai suorista ulostulo.
20. **Työkalujen tulokset käyttävät `function_call_output`, eivät `role: tool`**: Työkalun suorittamisen jälkeen lisää `{"type": "function_call_output", "call_id": ..., "output": ...}` — ei `{"role": "tool", "tool_call_id": ..., "content": ...}`. Assistentin työkalupyynnössä käytä `messages.extend(response.output)` — älä manuaalista `{"role": "assistant", "tool_calls": [...]}` sanakirjaa.
21. **`strict: true` vaatii `required` + `additionalProperties: false`**: Käytettäessä `strict: true` työkalussa, jokainen ominaisuus on listattava `required`-taulukossa ja `additionalProperties` on oltava `false`. Kumpi tahansa puuttuminen aiheuttaa 400-virheen.
22. **Funktiokutsun tunnuksilla on tietyt etuliitteet**: Kun annetaan few-shot `function_call` -kohteita `input`-kentässä, `id`-kentän on aloitettava `fc_` ja `call_id`-kentän `call_` (esim. `"id": "fc_example1", "call_id": "call_example1"`). Vanhan Chat Completionsin `call_`-etuliitteen käyttö `id`-kentässä hylätään.
23. **GitHub Models ei tue Responses APIa**: Jos sovelluksessa on GitHub Models -koodipolku (`base_url` osoittaa `models.github.ai` tai `models.inference.ai.azure.com`), poista se kokonaan. Migrointipolkua ei ole — vaihda Azure OpenAI:hin, OpenAI:hin tai yhteensopivaan paikalliseen päätepisteeseen.
24. **Sisällönsuodattimen virherakenne muuttui**: Chat Completions -virheet käyttivät `error.body["innererror"]["content_filter_result"]` (yksikkömuoto). Responses API -virheet käyttävät `error.body["content_filters"][0]["content_filter_results"]` (monikko ja taulukossa). `innererror`-avain ei ole enää olemassa. Koodi, joka suorastaan käyttää `innererror`:ia, aiheuttaa suoritusaikaisen `KeyError`-poikkeuksen — tämä on helppo ohittaa migraatiossa, koska se ilmenee vain, kun sisältösuodatin todella aktivoituu. Etsi aina `innererror`-kohtia migraation yhteydessä.
25. **Raakaa HTTP-kutsua varten tarvitaan URL:n ja rungon uudelleenkirjoitus**: Sovellukset, jotka kutsuvat Azure OpenAI RESTiä suoraan (käyttäen `requests`, `httpx`, `aiohttp`) polulla `/openai/deployments/{name}/chat/completions?api-version=...`, on vaihdettava osoitteeseen `/openai/v1/responses`. Pyyntöjen rungossa käytetään `input`ia `messages`in sijaan, vaaditaan `max_output_tokens` ja `store`, ja `api-version` -kyselyparametri poistetaan. Vastauksen rungon teksti löytyy `output[0].content[0].text` — **ei** `output_text`, joka on SDK:n mukavuusominaisuus eikä esiinny raakassa REST JSONissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->