[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na sliku iznad za gledanje videa ove lekcije)_

# Dizajnerski obrazac korištenja alata

Alati su zanimljivi jer AI agentima omogućuju širi raspon mogućnosti. Umjesto da agent ima ograničen skup radnji koje može izvesti, dodavanjem alata agent sada može izvršavati širok spektar radnji. U ovom poglavlju ćemo pogledati Dizajnerski obrazac korištenja alata, koji opisuje kako AI agenti mogu koristiti specifične alate za postizanje svojih ciljeva.

## Uvod

U ovoj lekciji želimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac korištenja alata?
- Koje su primjene na koje se može primijeniti?
- Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca?
- Koje su posebne napomene za korištenje dizajnerskog obrasca korištenja alata u izgradnji pouzdanih AI agenata?

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Definirati dizajnerski obrazac korištenja alata i njegovu svrhu.
- Identificirati primjene gdje je dizajnerski obrazac korištenja alata primjenjiv.
- Razumjeti ključne elemente potrebne za implementaciju dizajnerskog obrasca.
- Prepoznati napomene za osiguravanje pouzdanosti AI agenata koji koriste ovaj dizajnerski obrazac.

## Što je dizajnerski obrazac korištenja alata?

**Dizajnerski obrazac korištenja alata** fokusira se na pružanje mogućnosti LLM-ovima da komuniciraju s vanjskim alatima kako bi postigli specifične ciljeve. Alati su kodovi koje agent može izvršiti za izvođenje radnji. Alat može biti jednostavna funkcija poput kalkulatora, ili API poziv prema trećoj strani kao što je provjera cijena dionica ili meteorološka prognoza. U kontekstu AI agenata, alati su dizajnirani da budu izvršeni od strane agenata kao odgovor na **pozive funkcijama generirane od modela**.

## Koje su primjene na koje se može primijeniti?

AI agenti mogu koristiti alate za obavljanje složenih zadataka, dohvat informacija ili donošenje odluka. Dizajnerski obrazac korištenja alata često se koristi u scenarijima koji zahtijevaju dinamičnu interakciju s vanjskim sustavima, poput baza podataka, web usluga ili interpreterima koda. Ova sposobnost korisna je za različite slučajeve upotrebe uključujući:

- **Dinamičan dohvat informacija:** Agenti mogu upitavati vanjske API-je ili baze podataka kako bi dohvatili najnovije podatke (npr. upit SQLite baze za analizu podataka, dohvat cijena dionica ili vremenske prognoze).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili izvođenje simulacija.
- **Automatizacija radnih tijekova:** Automatiziranje ponavljajućih ili višestepenih radnih tijekova integriranjem alata kao što su raspoređivači zadataka, e-mail usluge ili podatkovni tokovi.
- **Korisnička podrška:** Agenti mogu komunicirati s CRM sustavima, platformama za upravljanje zahtjevima ili bazama znanja za rješavanje korisničkih upita.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimanja teksta ili evaluacije sigurnosti sadržaja za pomoć u zadacima stvaranja sadržaja.

## Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca korištenja alata?

Ovi gradivni blokovi omogućuju AI agentu da izvršava širok spektar zadataka. Pogledajmo ključne elemente potrebne za implementaciju dizajnerskog obrasca korištenja alata:

- **Sheme funkcija/alata**: Detaljni opisi dostupnih alata, uključujući naziv funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućuju LLM-u da razumije koji su alati dostupni i kako konstruirati valjane zahtjeve.

- **Logika izvršavanja funkcija**: Upravljanje načinom i vremenom pozivanja alata na temelju korisničke namjere i konteksta razgovora. To može uključivati planere, mehanizme usmjeravanja ili uvjetne tokove koje dinamički određuju korištenje alata.

- **Sustav za rukovanje porukama**: Komponente koje upravljaju razgovornim tokom između korisničkih unosa, LLM odgovora, poziva alata i izlaza iz alata.

- **Okvir za integraciju alata**: Infrastruktura koja povezuje agenta s različitim alatima, bilo da se radi o jednostavnim funkcijama ili složenim vanjskim uslugama.

- **Rukovanje pogreškama i validacija**: Mehanizmi za upravljanje neuspjesima u izvršavanju alata, validaciju parametara i rukovanje neočekivanim odgovorima.

- **Upravljanje stanjem**: Praćenje konteksta razgovora, prethodnih interakcija s alatima i trajnih podataka kako bi se osigurala dosljednost tijekom višekratnih interakcija.

Sljedeće ćemo detaljnije pogledati pozivanje funkcija/alata.
 
### Pozivanje funkcija/alata

Pozivanje funkcija je glavni način na koji omogućavamo Large Language Models (LLM-ovima) interakciju s alatima. Često ćete vidjeti da se "funkcija" i "alat" koriste naizmjenično jer su "funkcije" (blokovi ponovo iskoristivog koda) alati koje agenti koriste za obavljanje zadataka. Da bi kod funkcije bio pozvan, LLM mora usporediti korisnički zahtjev s opisom funkcije. Za to se šalje shema koja sadrži opise svih dostupnih funkcija LLM-u. LLM tada odabire najprikladniju funkciju za zadatak i vraća njen naziv i argumente. Odabrana funkcija se poziva, njen odgovor se šalje natrag LLM-u, koji koristi informacije za odgovor na korisnički zahtjev.

Za programere koji žele implementirati pozivanje funkcija za agente, potrebni su:

1. LLM model koji podržava pozivanje funkcija
2. Shema koja sadrži opise funkcija
3. Kod za svaku opisanu funkciju

Upotrijebimo primjer kako dobiti trenutno vrijeme u gradu:

1. **Inicijalizirajte LLM koji podržava pozivanje funkcija:**

    Nisu svi modeli podržavaju pozivanje funkcija, pa je važno provjeriti podržava li LLM koji koristite. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti inicijalizacijom OpenAI klijenta prema Azure OpenAI **Responses API** (stabilni `/openai/v1/` endpoint — nije potreban `api_version`). 

    ```python
    # Inicijalizirajte OpenAI klijent za Azure OpenAI (Responses API, v1 endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Kreirajte shemu funkcije**:

    Sljedeće definiramo JSON shemu koja sadrži naziv funkcije, opis onoga što funkcija radi, te nazive i opise parametara funkcije.
    Nakon toga ćemo tu shemu poslati klijentu kreiranom ranije zajedno s korisničkim zahtjevom za pronalaskom vremena u San Franciscu. Važno je napomenuti da se vraća **poziv alatu**, a **ne** konačan odgovor na pitanje. Kao što je spomenuto ranije, LLM vraća naziv funkcije koju je odabrao za zadatak i argumente koji će joj biti proslijeđeni.

    ```python
    # Opis funkcije za model da pročita (format alata Responses API flat)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # Početna korisnička poruka
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Prvi API poziv: Zatražite od modela da koristi funkciju
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API vraća pozive alata kao stavke function_call u response.output.
    # Dodajte ih u razgovor kako bi model imao puni kontekst u sljedećem koraku.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kod funkcije potreban za izvođenje zadatka:**

    Sada kada je LLM odabrao koju funkciju treba pokrenuti, potrebno je implementirati i izvršiti kod koji obavlja zadatak.
    Kod za dohvat trenutnog vremena možemo implementirati u Pythonu. Također treba napisati kod za izdvajanje naziva i argumenata iz response_message kako bismo dobili konačni rezultat.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # Obrada poziva funkcija
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Vratite rezultat alata kao stavku function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Drugi API poziv: Dohvatite konačni odgovor iz modela
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Pozivanje funkcija je u srcu većine, ako ne i svih dizajna korištenja alata u agentima, no implementacija od nule ponekad može biti izazovna.
Kao što smo naučili u [Lekciji 2](../../../02-explore-agentic-frameworks), agentni okviri pružaju nam predizrađene gradivne blokove za implementaciju korištenja alata.
 
## Primjeri korištenja alata s agentnim okvirima

Evo nekoliko primjera kako možete implementirati dizajnerski obrazac korištenja alata koristeći različite agentne okvire:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI okvir za izgradnju AI agenata. Pojednostavljuje proces korištenja pozivanja funkcija omogućujući vam da definirate alate kao Python funkcije s dekoratorom `@tool`. Okvir upravlja komunikacijom između modela i vašeg koda. Također pruža pristup predizgrađenim alatima poput File Search i Code Interpreter putem `FoundryChatClient`.

Sljedeća shema ilustrira proces pozivanja funkcija s Microsoft Agent Frameworkom:

![pozivanje funkcija](../../../translated_images/hr/functioncalling-diagram.a84006fc287f6014.webp)

U Microsoft Agent Frameworku alati su definirani kao dekorirane funkcije. Funkciju `get_current_time` koju smo ranije vidjeli možemo pretvoriti u alat koristeći dekorator `@tool`. Okvir će automatski serijalizirati funkciju i njene parametre, kreirajući shemu za slanje LLM-u.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Kreirajte klijenta
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Kreirajte agenta i pokrenite ga s alatom
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je noviji agentni okvir dizajniran kako bi programerima omogućio sigurno izgrađivanje, implementaciju i skaliranje visokokvalitetnih i proširivih AI agenata bez potrebe za upravljanjem osnovnim računalnim i spremišnim resursima. Posebno je koristan za enterprise aplikacije jer je potpuno upravljana usluga s enterprise razinom sigurnosti.

U usporedbi s razvojem direktno s LLM API-jem, Microsoft Foundry Agent Service nudi nekoliko prednosti, uključujući:

- Automatsko pozivanje alata – nije potrebno parsirati poziv alatu, pokretati alat i upravljati odgovorom; sve se to sada obavlja na strani servera
- Sigurno upravljani podaci – umjesto upravljanja vlastitim stanjem razgovora, možete se osloniti na teme (threads) za pohranu svih potrebnih informacija
- Alati spremni za korištenje – alati kojima možete upravljati za interakciju s izvorima podataka poput Bing, Azure AI Search i Azure Functions.

Alati dostupni u Microsoft Foundry Agent Service mogu se podijeliti u dvije kategorije:

1. Alati znanja:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezivanje s Bing pretraživanjem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraživanje datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI pretraživanje</a>

2. Alati za akciju:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter koda</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani OpenAPI-jem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogućuje korištenje ovih alata zajedno kao `toolset`. Također koristi `threads` koji prate povijest poruka iz određenog razgovora.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti razgovornog agenta koji može odgovarati na pitanja o vašim prodajnim podacima.

Sljedeća slika ilustrira kako biste mogli koristiti Microsoft Foundry Agent Service za analizu vaših prodajnih podataka:

![Agentni servis u akciji](../../../translated_images/hr/agent-service-in-action.34fb465c9a84659e.webp)

Za korištenje bilo kojeg od ovih alata uz servis možemo kreirati klijenta i definirati alat ili skup alata. Kako to praktično implementirati, možemo koristiti sljedeći Python kod. LLM će moći pogledati skup alata i odlučiti hoće li koristiti korisnički definiranu funkciju `fetch_sales_data_using_sqlite_query`, ili predizgrađeni Code Interpreter, ovisno o korisničkom zahtjevu.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcija fetch_sales_data_using_sqlite_query koja se može pronaći u datoteci fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicijaliziraj skup alata
toolset = ToolSet()

# Inicijaliziraj agenta za pozivanje funkcija s funkcijom fetch_sales_data_using_sqlite_query i dodaj ga u skup alata
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicijaliziraj alat za tumač koda i dodaj ga u skup alata.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koje su posebne napomene za korištenje dizajnerskog obrasca korištenja alata u izgradnji pouzdanih AI agenata?

Česta briga kod SQL-a dinamički generiranog od LLM-a je sigurnost, posebno rizik od SQL injekcija ili zlonamjernih radnji poput brisanja ili izmjene baze podataka. Iako su ove brige opravdane, mogu se učinkovito ublažiti pravilnim konfiguriranjem dozvola pristupa bazi podataka. Za većinu baza to uključuje konfiguriranje baze kao samo za čitanje. Za baze kao što su PostgreSQL ili Azure SQL, aplikaciji se treba dodijeliti samo uloga za čitanje (SELECT).

Pokretanje aplikacije u sigurnom okruženju dodatno povećava zaštitu. U poslovnim scenarijima podaci se obično izvlače i transformiraju iz operativnih sustava u bazu samo za čitanje ili skladište podataka s jednostavnom shemom. Ovaj pristup osigurava sigurnost podataka, optimizaciju za performanse i pristupačnost te da aplikacija ima ograničen pristup samo za čitanje.

## Primjeri koda

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate li dodatnih pitanja o dizajnerskim obrascima korištenja alata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da upoznate druge učenike, sudjelujete u uredskim satima i dobijete odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service radionica</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer radionica s više agenata</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Frameworka</a>


## Osnovno testiranje ovog agenta (neobavezno)

Nakon što naučite kako postaviti agente u [Lekcija 16](../16-deploying-scalable-agents/README.md), možete osnovno testirati `TravelToolAgent` iz ove lekcije (još uvijek poziva svoje alate i odgovara?) s [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Pogledajte [`tests/README.md`](../tests/README.md) kako ga pokrenuti.

## Prethodna lekcija

[Razumijevanje agentičkih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija

[Agentički RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->