[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite gornju sliku za pregled videa ovog lekcija)_

# Dizajnerski obrazac korištenja alata

Alati su zanimljivi jer omogućuju AI agentima širi raspon sposobnosti. Umjesto da agent ima ograničen skup radnji koje može izvesti, dodavanjem alata, agent sada može izvesti širok spektar radnji. U ovom poglavlju proučit ćemo dizajnerski obrazac korištenja alata, koji opisuje kako AI agenti mogu koristiti specifične alate za postizanje svojih ciljeva.

## Uvod

U ovoj lekciji želimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac korištenja alata?
- U kojim slučajevima se može primijeniti?
- Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca?
- Koje su posebne razmatranja pri korištenju dizajnerskog obrasca korištenja alata za izgradnju pouzdanih AI agenata?

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Definirati dizajnerski obrazac korištenja alata i njegovu svrhu.
- Identificirati slučajeve uporabe gdje se dizajnerski obrazac korištenja alata primjenjuje.
- Razumjeti ključne elemente potrebne za implementaciju dizajnerskog obrasca.
- Prepoznati razmatranja za osiguranje pouzdanosti AI agenata koji koriste ovaj dizajnerski obrazac.

## Što je dizajnerski obrazac korištenja alata?

**Dizajnerski obrazac korištenja alata** fokusira se na davanje LLM-ovima sposobnosti interakcije s vanjskim alatima za postizanje specifičnih ciljeva. Alati su kod koji agent može izvršiti za obavljanje radnji. Alat može biti jednostavna funkcija poput kalkulatora ili poziv API-ju treće strane, poput pregleda cijena dionica ili vremenske prognoze. U kontekstu AI agenata, alati su dizajnirani da ih agenti pokreću kao odgovor na **pozive funkcijama generiranim modelom**.

## U kojim slučajevima se može primijeniti?

AI agenti mogu koristiti alate za dovršavanje složenih zadataka, dohvat informacija ili donošenje odluka. Dizajnerski obrazac korištenja alata često se koristi u scenarijima koji zahtijevaju dinamičku interakciju s vanjskim sustavima, poput baza podataka, web usluga ili interpreter koda. Ta sposobnost korisna je u brojnim slučajevima, uključujući:

- **Dinamičko dohvaćanje informacija:** Agenti mogu upitivati vanjske API-je ili baze podataka za dohvat najnovijih podataka (npr. upit SQLite baze za analizu podataka, dohvat cijena dionica ili vremenskih informacija).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili izvođenje simulacija.
- **Automatizacija tijeka rada:** Automatizacija ponavljajućih ili višekorakih tijekova rada integracijom alata poput upravitelja zadataka, email servisa ili cjevovoda podataka.
- **Korisnička podrška:** Agenti mogu komunicirati s CRM sustavima, platformama za ticketing ili bazama znanja za rješavanje korisničkih upita.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimanja teksta ili evaluacije sigurnosti sadržaja za pomoć u zadacima kreiranja sadržaja.

## Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca korištenja alata?

Ovi gradivni blokovi omogućuju AI agentu da izvršava širok spektar zadataka. Pogledajmo ključne elemente potrebne za implementaciju dizajnerskog obrasca korištenja alata:

- **Sheme funkcija/alata**: Detaljni opisi dostupnih alata, uključujući naziv funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućuju LLM-u razumijevanje dostupnih alata i kako konstruirati valjane zahtjeve.

- **Logika izvršavanja funkcija**: Određuje kako i kada se alati pozivaju na temelju korisnikove namjere i konteksta razgovora. Ovo može uključivati module planera, mehanizme usmjeravanja ili uvjetne tokove koji dinamički odlučuju o korištenju alata.

- **Sustav rukovanja porukama**: Komponente koje upravljaju konverzacijskim tijekom između korisničkih unosa, odgovora LLM-a, poziva alata i izlaza alata.

- **Okvir integracije alata**: Infrastruktura koja povezuje agenta s različitim alatima, bilo jednostavnim funkcijama ili složenim vanjskim uslugama.

- **Rukovanje pogreškama i validacija**: Mehanizmi za rukovanje neuspjesima u izvršavanju alata, provjeru parametara i upravljanje neočekivanim odgovorima.

- **Upravljanje stanjem**: Prati kontekst razgovora, prethodne interakcije s alatima i trajne podatke kako bi se osigurala konzistentnost tijekom višekratnih interakcija.

Sljedeće ćemo detaljnije pogledati pozivanje funkcija/alata.
 
### Pozivanje funkcija/alata

Pozivanje funkcija primarni je način na koji omogućujemo velikim jezičnim modelima (LLM-ovima) interakciju s alatima. Često ćete vidjeti da se 'funkcija' i 'alat' koriste naizmjenično jer su 'funkcije' (blokovi ponovno upotrebljivog koda) alati koje agenti koriste za izvršavanje zadataka. Da bi se izvršio kôd funkcije, LLM mora usporediti zahtjev korisnika s opisom funkcije. Za to se šalje shema koja sadrži opise svih dostupnih funkcija LLM-u. LLM zatim odabire najprikladniju funkciju za zadatak i vraća njezin naziv i argumente. Odabrana funkcija se izvršava, odgovor se šalje natrag LLM-u, koji koristi informacije kako bi odgovorio na korisnikov zahtjev.

Da bi programeri implementirali pozivanje funkcija za agente, potrebni su:

1. LLM model koji podržava pozivanje funkcija
2. Shema koja sadrži opise funkcija
3. Kôd za svaku opisanu funkciju

Koristimo primjer dobivanja trenutnog vremena u nekom gradu da ilustriramo:

1. **Inicijalizirajte LLM koji podržava pozivanje funkcija:**

    Nisu svi modeli podržavaju pozivanje funkcija, stoga je važno provjeriti da onaj koji koristite to podržava.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti inicijaliziranjem OpenAI klijenta koristeći Azure OpenAI **Responses API** (stabilna `/openai/v1/` točka — nije potreban `api_version`).

    ```python
    # Inicijalizirajte OpenAI klijent za Azure OpenAI (Responses API, v1 krajnja točka)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Napravite shemu funkcije**:

    Zatim ćemo definirati JSON shemu koja sadrži naziv funkcije, opis što funkcija radi, te nazive i opise parametara funkcije.
    Tu shemu ćemo proslijediti klijentu koji smo prethodno kreirali, zajedno sa zahtjevom korisnika za pronalaženje vremena u San Franciscu. Važno je naglasiti da je vraćeni rezultat **poziv alatu**, **a ne** konačan odgovor na pitanje. Kao što je ranije spomenuto, LLM vraća naziv funkcije koju je odabrao za zadatak, kao i argumente koji će joj biti proslijeđeni.

    ```python
    # Opis funkcije za model za čitanje (Responses API flat tool format)
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

    # Prvi API poziv: Zamolite model da koristi funkciju
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API vraća pozive alata kao function_call stavke u response.output.
    # Dodajte ih u razgovor kako bi model imao puni kontekst u sljedećem koraku.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kôd funkcije potreban za izvršenje zadatka:**

    Sad kad je LLM odabrao koju funkciju treba pokrenuti, kôd koji izvršava zadatak treba implementirati i pokrenuti.
    Kôd za dobivanje trenutnog vremena možemo implementirati u Pythonu. Također ćemo trebati napisati kôd za izdvajanje naziva i argumenata iz response_message kako bismo dobili konačni rezultat.

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

                # Vrati rezultat alata kao stavku function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Drugi API poziv: Dobivanje konačnog odgovora od modela
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

Pozivanje funkcija je u središtu većine, ako ne i svih dizajnerskih obrazaca korištenja alata, no implementacija od nule ponekad može biti zahtjevna.
Kao što smo naučili u [Lesson 2](../../../02-explore-agentic-frameworks), agenti okviri pružaju nam unaprijed izrađene gradivne blokove za implementaciju korištenja alata.
 
## Primjeri korištenja alata s agentnim okvirima

Evo nekoliko primjera kako možete implementirati dizajnerski obrazac korištenja alata koristeći različite agentne okvire:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI okvir za izgradnju AI agenata. Pojednostavljuje proces korištenja pozivanja funkcija omogućavajući da se alati definiraju kao Python funkcije s dekoratorom `@tool`. Okvir upravlja komunikacijom između modela i vašeg koda. Također pruža pristup unaprijed izgrađenim alatima poput Pretraživanja datoteka i Code Interpreter kroz `FoundryChatClient`.

Sljedeći dijagram ilustrira proces pozivanja funkcija s Microsoft Agent Framework:

![pozivanje funkcija](../../../translated_images/hr/functioncalling-diagram.a84006fc287f6014.webp)

U Microsoft Agent Framework alati se definiraju kao dekorirane funkcije. Funkciju `get_current_time` koju smo ranije vidjeli možemo pretvoriti u alat korištenjem dekoratora `@tool`. Okvir će automatski serializirati funkciju i njezine parametre, stvarajući shemu za slanje LLM-u.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je noviji agentni okvir dizajniran za omogućavanje programerima sigurnu izgradnju, implementaciju i skaliranje kvalitetnih i proširivih AI agenata bez potrebe za upravljanjem temeljnom infrastrukturom za računalstvo i pohranu. Posebno je koristan u poslovnim aplikacijama jer je u potpunosti upravljana usluga s sigurnošću na razini poduzeća.

U usporedbi s razvojem direktno s LLM API-jem, Microsoft Foundry Agent Service nudi neke prednosti, uključujući:

- Automatsko pozivanje alata – nije potrebno parsirati poziv alatu, pokretati alat i obrađivati odgovor; sve se to sada radi na strani servera
- Sigurno upravljanje podacima – umjesto da upravljate vlastitim stanjem razgovora, možete se osloniti na threadove koji pohranjuju sve potrebne informacije
- Alati spremni za uporabu – alati za rad s vašim izvorima podataka, poput Binga, Azure AI Search i Azure Functions.

Alati dostupni u Microsoft Foundry Agent Service mogu se podijeliti u dvije kategorije:

1. Alati za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezanost s Bing pretraživanjem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraživanje datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI pretraživanje</a>

2. Akcijski alati:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani OpenAPI specifikacijom</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogućuje korištenje ovih alata zajedno kao `toolset`. Također koristi `threadove` koji prate povijest poruka određenog razgovora.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti razgovornog agenta koji može odgovarati na pitanja o vašim prodajnim podacima.

Sljedeća slika ilustrira kako možete koristiti Microsoft Foundry Agent Service za analizu vaših prodajnih podataka:

![Agentic Service U Akciji](../../../translated_images/hr/agent-service-in-action.34fb465c9a84659e.webp)

Da biste koristili bilo koji od ovih alata s uslugom, možemo stvoriti klijenta i definirati alat ili skup alata. Za praktičnu implementaciju možemo koristiti sljedeći Python kôd. LLM će moći pogledati toolset i odlučiti hoće li koristiti korisnički definiranu funkciju, `fetch_sales_data_using_sqlite_query`, ili unaprijed izrađeni Code Interpreter ovisno o zahtjevu korisnika.

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

# Inicijaliziraj alat za interpretaciju koda i dodaj ga u skup alata.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koje su posebne razmatranja pri korištenju dizajnerskog obrasca korištenja alata za izgradnju pouzdanih AI agenata?

Česta zabrinutost vezana uz SQL koji dinamički generiraju LLM-i je sigurnost, posebice rizik od SQL injekcije ili zlonamjernih radnji, poput brisanja ili manipulacije bazom podataka. Iako su te zabrinutosti opravdane, mogu se učinkovito ublažiti pravilnim konfiguriranjem pristupnih prava baze podataka. Za većinu baza to uključuje konfiguraciju baze kao samo za čitanje. Za baze poput PostgreSQL-a ili Azure SQL-a, aplikaciji bi trebalo dodijeliti ulogu samo za čitanje (SELECT).

Pokretanje aplikacije u sigurnom okruženju dodatno pojačava zaštitu. U enterprise scenarijima podaci se obično izvlače i transformiraju iz operativnih sustava u bazu ili skladište podataka samo za čitanje s korisnički prihvatljivom shemom. Taj pristup osigurava da su podaci sigurni, optimizirani za performanse i dostupnost te da aplikacija ima ograničen pristup samo za čitanje.

## Primjeri koda

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate li još pitanja o dizajnerskim obrascima korištenja alata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici kako biste upoznali druge učenike, sudjelovali u radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>


## Testiranje ovog agenta (opcionalno)

Nakon što naučite kako implementirati agente u [Lekciji 16](../16-deploying-scalable-agents/README.md), možete testirati `TravelToolAgent` iz ove lekcije (da li i dalje poziva svoje alate i odgovara?) koristeći [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Pogledajte [`tests/README.md`](../tests/README.md) za upute kako ga pokrenuti.

## Prethodna lekcija

[Razumijevanje agentnih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija

[Agentni RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->