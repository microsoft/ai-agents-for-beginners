[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na sliku iznad za pregled videa ovog predavanja)_

# Dizajnerski obrazac korištenja alata

Alati su zanimljivi jer omogućuju AI agentima širok spektar sposobnosti. Umjesto da agent ima ograničen skup akcija koje može izvršiti, dodavanjem alata agent sada može izvršavati širok raspon radnji. U ovom poglavlju pogledat ćemo dizajnerski obrazac korištenja alata, koji opisuje kako AI agenti mogu koristiti specifične alate za ostvarenje svojih ciljeva.

## Uvod

U ovom predavanju želimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac korištenja alata?
- Za koje slučajeve uporabe se može primijeniti?
- Koji su elementi/komponente potrebni za implementaciju ovog dizajnerskog obrasca?
- Koje su posebne razmatranja za korištenje dizajnerskog obrasca korištenja alata u izgradnji pouzdanih AI agenata?

## Ciljevi učenja

Nakon završetka ovog predavanja bit ćete sposobni:

- Definirati dizajnerski obrazac korištenja alata i njegovu svrhu.
- Identificirati slučajeve uporabe u kojima je ovaj dizajnerski obrazac primjenjiv.
- Razumjeti ključne elemente potrebne za implementaciju ovog obrasca.
- Prepoznati razmatranja za osiguranje pouzdanosti AI agenata koji koriste ovaj dizajnerski obrazac.

## Što je dizajnerski obrazac korištenja alata?

**Dizajnerski obrazac korištenja alata** fokusiran je na davanje LLM-ovima sposobnosti interakcije s vanjskim alatima kako bi postigli određene ciljeve. Alati su kod koji agent može izvršiti za obavljanje radnji. Alat može biti jednostavna funkcija poput kalkulatora, ili API poziv prema usluzi treće strane poput provjere cijene dionica ili vremenske prognoze. U kontekstu AI agenata, alati su dizajnirani da budu izvršavani od strane agenata kao odgovor na **funkcijske pozive generirane od modela**.

## Za koje slučajeve uporabe se može primijeniti?

AI agenti mogu koristiti alate za dovršavanje složenih zadataka, dohvat informacija ili donošenje odluka. Dizajnerski obrazac korištenja alata često se koristi u scenarijima koji zahtijevaju dinamičku interakciju s vanjskim sustavima, poput baza podataka, web servisa ili interpretera koda. Ova sposobnost korisna je za mnoge različite slučajeve uporabe, uključujući:

- **Dinamički dohvat informacija:** Agenti mogu upitavati vanjske API-je ili baze podataka za dohvat najnovijih podataka (npr. upit prema SQLite bazi za analizu podataka, dohvat cijena dionica ili vremenskih informacija).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili izvođenje simulacija.
- **Automatizacija radnih tokova:** Automatiziranje ponavljajućih ili višestupanjskih radnih procesa integracijom alata poput raspoređivača zadataka, usluga e-pošte ili podatkovnih kanala.
- **Podrška korisnicima:** Agenti mogu komunicirati sa CRM sustavima, platformama za upravljanje zahtjevima ili bazama znanja kako bi riješili korisničke upite.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimatelja teksta ili ocjenjivača sigurnosti sadržaja kao pomoć u zadacima kreiranja sadržaja.

## Koji su elementi/komponente potrebni za implementaciju dizajnerskog obrasca korištenja alata?

Ove komponente omogućuju AI agentu da izvrši širok raspon zadataka. Pogledajmo ključne elemente potrebne za implementaciju dizajnerskog obrasca korištenja alata:

- **Sheme funkcija/alata**: Detaljni opisi dostupnih alata, uključujući ime funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućuju LLM-u da razumije koji su alati dostupni i kako sastaviti valjane zahtjeve.

- **Logika izvršavanja funkcija**: Upravljanje načinom i vremenom kad se alati pozivaju, ovisno o namjeri korisnika i kontekstu razgovora. To može uključivati module za planiranje, mehanizme usmjeravanja ili uvjetne tokove koji dinamički određuju korištenje alata.

- **Sustav za upravljanje porukama**: Komponente koje upravljaju razgovornim tokom između korisničkih unosa, LLM odgovora, poziva alata i izlaza alata.

- **Okvir za integraciju alata**: Infrastruktura koja povezuje agenta s različitim alatima, bilo da su to jednostavne funkcije ili složeni vanjski servisi.

- **Rukovanje pogreškama i validacija**: Mehanizmi za rukovanje neuspjesima u izvršavanju alata, provjeru parametara i upravljanje neočekivanim odgovorima.

- **Upravljanje stanjem**: Praćenje konteksta razgovora, prethodnih interakcija s alatima i trajnih podataka radi osiguravanja konzistentnosti tijekom višekratnih interakcija.

Sljedeće, pogledajmo detaljnije pozivanje funkcija/alata.

### Pozivanje funkcija/alata

Pozivanje funkcija je primarni način na koji omogućavamo velikim jezičnim modelima (LLM) interakciju s alatima. Često ćete vidjeti da se 'Funkcija' i 'Alat' koriste naizmjenično jer su 'funkcije' (blokovi ponovo upotrebljivog koda) 'alati' koje agenti koriste za izvršavanje zadataka. Kako bi se pozvao kod funkcije, LLM mora usporediti zahtjev korisnika s opisom funkcija. Za to se šalje shema koja sadrži opise svih dostupnih funkcija modelu. LLM zatim bira najprikladniju funkciju za zadatak i vraća njezino ime i argumente. Izabrana funkcija se poziva, njezin odgovor se šalje natrag modelu, koji koristi te informacije za odgovor korisniku.

Za programere koji žele implementirati pozivanje funkcija za agente, potrebno je:

1. LLM model koji podržava pozivanje funkcija
2. Shema s opisima funkcija
3. Kod za svaku opisanu funkciju

Upotrijebimo primjer dobivanja trenutnog vremena u nekom gradu:

1. **Inicijalizirajte LLM koji podržava pozivanje funkcija:**

    Nisu svi modeli podržavaju pozivanje funkcija, stoga je važno provjeriti podršku vašeg LLM-a.
    <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti s inicijalizacijom Azure OpenAI klijenta.

    ```python
    # Inicijalizirajte Azure OpenAI klijenta
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Kreirajte shemu funkcije:**

    Zatim ćemo definirati JSON shemu koja sadrži ime funkcije, opis što funkcija radi, te imena i opise parametara funkcije.
    Tu shemu prosljeđujemo ranije kreiranom klijentu, zajedno s korisničkim zahtjevom za saznanje vremena u San Franciscu. Važno je napomenuti da se vraća **poziv alata**, **ne** konačni odgovor na pitanje. Kao što je ranije spomenuto, LLM vraća ime odabrane funkcije i argumente koji će joj biti poslani.

    ```python
    # Opis funkcije za model da pročita
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Početna poruka korisnika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi API poziv: Zamolite model da koristi funkciju
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obradite odgovor modela
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **Kod funkcije potreban za izvršenje zadatka:**

    Sada kada je LLM odabrao koju funkciju treba pokrenuti, potrebno je implementirati i izvršiti kod koji obavlja zadatak.
    Kod za dobivanje trenutnog vremena možemo napisati u Pythonu. Također trebamo napisati kod za izdvajanje imena i argumenata iz response_message za dobivanje konačnog rezultata.

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Drugi API poziv: Dohvati konačni odgovor od modela
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Pozivanje funkcija je u srcu većine, ako ne i svih dizajnerskih obrazaca korištenja alata u agentima, no njegova implementacija od nule može ponekad biti izazovna.
Kao što smo naučili u [Lekciji 2](../../../02-explore-agentic-frameworks), agentni okviri nam pružaju unaprijed izgrađene komponente za implementaciju korištenja alata.

## Primjeri korištenja alata uz agentne okvire

Evo nekoliko primjera kako možete implementirati dizajnerski obrazac korištenja alata koristeći različite agentne okvire:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI okvir za izgradnju AI agenata. Pojednostavljuje proces pozivanja funkcija dopuštajući vam definiranje alata kao Python funkcija pomoću dekoratora `@tool`. Okvir upravlja komunikacijom između modela i vašeg koda. Također pruža pristup unaprijed izrađenim alatima kao što su Pretraživanje datoteka i Tumač koda kroz `AzureAIProjectAgentProvider`.

Sljedeća shema ilustrira proces pozivanja funkcija u Microsoft Agent Frameworku:

![function calling](../../../translated_images/hr/functioncalling-diagram.a84006fc287f6014.webp)

U Microsoft Agent Frameworku alati su definirani kao dekorirane funkcije. Možemo pretvoriti funkciju `get_current_time` koju smo ranije vidjeli u alat koristeći dekorator `@tool`. Okvir će automatski serijalizirati funkciju i njezine parametre, stvarajući shemu za slanje LLM-u.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Kreirajte klijenta
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Kreirajte agenta i pokrenite s alatom
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je noviji agentni okvir dizajniran da omogući razvoj, implementaciju i skaliranje visokokvalitetnih te proširivih AI agenata na siguran način, bez potrebe za upravljanjem osnovnim računalnim i memorijskim resursima. Posebno je koristan za poduzeća jer je u potpunosti upravljana usluga s enterprise razinom sigurnosti.

U usporedbi s razvojem direktno preko LLM API-ja, Azure AI Agent Service pruža neke prednosti, uključujući:

- Automatsko pozivanje alata – nema potrebe za parsiranjem poziva alata, izvršavanjem i rukovanjem odgovorom; sve se to sada odvija na strani servera
- Sigurno upravljanje podacima – umjesto da sami upravljate stanjem razgovora, možete se osloniti na threads da pohrane sve potrebne informacije
- Alati raspoloživi odmah – alati koje možete koristiti za interakciju s vašim izvorima podataka, poput Binga, Azure AI Search i Azure Functions

Alati dostupni u Azure AI Agent Service mogu se podijeliti u dvije kategorije:

1. Alati za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezivanje s Bing pretraživanjem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraživanje datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alati za radnju:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Tumač koda</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani OpenAPI specifikacijom</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogućuje korištenje ovih alata zajedno kao `set alata`. Također koristi `threads` koji prate povijest poruka iz određenog razgovora.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti konverzacijskog agenta koji može odgovarati na pitanja o vašim prodajnim podacima.

Sljedeća slika ilustrira kako biste mogli koristiti Azure AI Agent Service za analizu vaših prodajnih podataka:

![Agentic Service In Action](../../../translated_images/hr/agent-service-in-action.34fb465c9a84659e.webp)

Da biste koristili bilo koji od ovih alata s uslugom možemo kreirati klijenta i definirati alat ili set alata. Za praktičnu implementaciju možemo koristiti sljedeći Python kod. LLM će moći pogledati set alata i odlučiti hoće li koristiti korisnički definiranu funkciju `fetch_sales_data_using_sqlite_query` ili unaprijed izgrađeni tumač koda ovisno o zahtjevu korisnika.

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

# Inicijaliziraj agent za pozivanje funkcija s funkcijom fetch_sales_data_using_sqlite_query i dodaj ga u skup alata
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicijaliziraj alat Code Interpreter i dodaj ga u skup alata.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koja su posebna razmatranja za korištenje dizajnerskog obrasca korištenja alata u izgradnji pouzdanih AI agenata?

Uobičajena zabrinutost vezana uz dinamički generirani SQL od strane LLM-a je sigurnost, posebice rizik od SQL injekcija ili zlonamjernih radnji poput brisanja ili mijenjanja baze podataka. Iako su ove zabrinutosti valjane, mogu se učinkovito ublažiti pravilnom konfiguracijom pristupnih prava baze podataka. Za većinu baza to znači konfiguriranje baze kao samo za čitanje. Za baze poput PostgreSQL-a ili Azure SQL-a, aplikaciji treba dodijeliti ulogu samo za čitanje (SELECT).

Pokretanje aplikacije u sigurnom okruženju dodatno poboljšava zaštitu. U scenarijima poduzeća podaci se obično izvlače i transformiraju iz operativnih sustava u bazu podataka ili skladište podataka samo za čitanje s jednostavnom shemom. Ovaj pristup osigurava da su podaci sigurni, optimizirani za performanse i dostupnost, te da aplikacija ima ograničen pristup samo za čitanje.

## Primjeri koda

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate li dodatnih pitanja o dizajnerskim obrascima korištenja alata?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) zajednici da upoznate druge učenike, sudjelujete na satima pomoći i dobijete odgovore na pitanja o AI agentima.

## Dodatni resursi

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Radionica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Multiaćentna radionica Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Frameworka</a>

## Prethodna lekcija

[Razumijevanje agentnih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->