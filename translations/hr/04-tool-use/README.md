[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Dizajnerski obrazac upotrebe alata

Alati su zanimljivi jer omogućuju AI agentima da imaju širi raspon sposobnosti. Umjesto da agent ima ograničen skup radnji koje može izvršiti, dodavanjem alata agent sada može obavljati širok spektar radnji. U ovom poglavlju proučit ćemo Dizajnerski obrazac upotrebe alata, koji opisuje kako AI agenti mogu koristiti specifične alate za postizanje svojih ciljeva.

## Uvod

U ovoj lekciji nastojimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac upotrebe alata?
- Za koje slučajeve upotrebe se može primijeniti?
- Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca?
- Koje su posebne razmatranja pri korištenju Dizajnerskog obrasca upotrebe alata za izgradnju pouzdanih AI agenata?

## Ciljevi učenja

Nakon završetka ove lekcije moći ćete:

- Definirati Dizajnerski obrazac upotrebe alata i njegovu svrhu.
- Identificirati slučajeve upotrebe gdje se Dizajnerski obrazac upotrebe alata može primijeniti.
- Razumjeti ključne elemente potrebne za implementaciju dizajnerskog obrasca.
- Prepoznati razmatranja za osiguranje pouzdanosti AI agenata koji koriste ovaj dizajnerski obrazac.

## Što je Dizajnerski obrazac upotrebe alata?

**Dizajnerski obrazac upotrebe alata** usredotočen je na davanje sposobnosti velikim jezičnim modelima (LLM-ovima) da komuniciraju s vanjskim alatima za postizanje specifičnih ciljeva. Alati su kod koji agent može izvršiti za obavljanje radnji. Alat može biti jednostavna funkcija poput kalkulatora ili API poziv ka usluzi treće strane, kao što je dohvaćanje cijena dionica ili vremenske prognoze. U kontekstu AI agenata, alati su dizajnirani da budu izvršeni od strane agenata kao odgovor na **funkcijske pozive generirane modelom**.

## Za koje slučajeve upotrebe se može primijeniti?

AI agenti mogu koristiti alate za dovršavanje složenih zadataka, dohvaćanje informacija ili donošenje odluka. Dizajnerski obrazac upotrebe alata često se koristi u scenarijima koji zahtijevaju dinamičku interakciju s vanjskim sustavima, poput baza podataka, web servisa ili interpretera koda. Ova sposobnost korisna je za niz različitih slučajeva uporabe, uključujući:

- **Dinamičko dohvaćanje informacija:** Agenti mogu upitavati vanjske API-je ili baze podataka za dobivanje najnovijih podataka (npr. upit u SQLite bazu radi analize podataka, dohvaćanje cijena dionica ili vremenske prognoze).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili izvođenje simulacija.
- **Automatizacija radnih tokova:** Automatizacija ponavljajućih ili višestepenih radnih procesa integrirajući alate poput raspoređivača zadataka, email servisa ili podatkovnih cjevovoda.
- **Podrška korisnicima:** Agenti mogu komunicirati s CRM sustavima, platformama za tiketiranje ili bazama znanja za rješavanje korisničkih upita.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimatelja teksta ili evaluatora sigurnosti sadržaja za pomoć u zadacima kreiranja sadržaja.

## Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca upotrebe alata?

Ovi gradivni blokovi omogućuju AI agentu obavljanje širokog spektra zadataka. Pogledajmo ključne elemente potrebne za implementaciju Dizajnerskog obrasca upotrebe alata:

- **Sheme funkcija/alata**: Detaljni opisi dostupnih alata, uključujući naziv funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućuju LLM-u da razumije koje su alate dostupne i kako izgraditi valjane zahtjeve.

- **Logika izvršavanja funkcija**: Upravlja načinom i vremenom pozivanja alata na temelju korisnikovog cilja i konteksta konverzacije. To može uključivati module planera, mehanizme usmjeravanja ili uvjetne tokove koji dinamički određuju korištenje alata.

- **Sustav upravljanja porukama**: Komponente koje upravljaju protokom konverzacije između korisničkih unosa, LLM odgovora, poziva alata i izlaza iz alata.

- **Okvir za integraciju alata**: Infrastruktura koja povezuje agenta s različitim alatima, bilo da su to jednostavne funkcije ili složeni vanjski servisi.

- **Rukovanje pogreškama i validacija**: Mehanizmi za rješavanje neuspjeha u izvršavanju alata, provjeru parametara i upravljanje neočekivanim odgovorima.

- **Upravljanje stanjem**: Praćenje konteksta konverzacije, prethodnih interakcija s alatima i trajnih podataka radi osiguravanja konzistentnosti tijekom višekratnih razgovora.

Dalje, pogledajmo detaljnije pozivanje funkcija/alata.

### Pozivanje funkcija/alata

Pozivanje funkcija je primarni način na koji omogućujemo velikim jezičnim modelima (LLM) interakciju s alatima. Često ćete vidjeti da se 'Funkcija' i 'Alat' koriste naizmjenično jer su 'funkcije' (blokovi ponovno iskoristivog koda) alati koje agenti koriste za izvršavanje zadataka. Kako bi se kod funkcije mogao pozvati, LLM mora usporediti zahtjev korisnika s opisom funkcije. Za to se šalje shema koja sadrži opise svih dostupnih funkcija LLM-u. LLM zatim odabire najprikladniju funkciju za zadatak i vraća njen naziv i argumente. Izabrana funkcija se poziva, njen odgovor se šalje natrag LLM-u, koji koristi informacije za odgovor korisnikovom zahtjevu.

Da bi programeri implementirali pozivanje funkcija za agente, potreban je:

1. LLM model koji podržava pozivanje funkcija
2. Shema koja sadrži opise funkcija
3. Kod za svaku opisana funkciju

Koristimo primjer dobivanja trenutnog vremena u gradu kako bismo ilustrirali:

1. **Inicijalizirajte LLM koji podržava pozivanje funkcija:**

    Nisu svi modeli podržani za pozivanje funkcija, stoga je važno provjeriti da vaš LLM to podržava. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti iniciranjem Azure OpenAI klijenta.

    ```python
    # Inicijalizirajte Azure OpenAI klijent
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Izrada sheme funkcije:**

    Zatim definiramo JSON shemu koja sadrži naziv funkcije, opis što funkcija radi te nazive i opise parametara funkcije.
    Ovu shemu zatim prosljeđujemo prethodno kreiranom klijentu zajedno s korisnikovim zahtjevom za pronalazak vremena u San Franciscu. Važno je napomenuti da je vraćen **poziv alatu**, **ne** konačan odgovor na pitanje. Kao što je ranije spomenuto, LLM vraća ime funkcije koju je odabrao za zadatak i argumente koji će joj se proslijediti.

    ```python
    # Opis funkcije za čitanje modela
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
  
    # Početna korisnička poruka
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi poziv API-ja: Zatražite od modela da koristi funkciju
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obrada odgovora modela
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kod funkcije potreban za izvršenje zadatka:**

    Sada kada je LLM odabrao funkciju koju treba pokrenuti, potrebno je implementirati i izvršiti kod koji obavlja zadatak.
    Kod za dohvat trenutnog vremena možemo implementirati u Pythonu. Također ćemo trebati napisati kod za izdvajanje naziva i argumenata iz response_message da bismo dobili konačni rezultat.

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
     # Obrada poziva funkcije
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

Pozivanje funkcija je u srcu većine, ako ne i svih, dizajnerskih obrazaca upotrebe alata za agente, no ponekad može biti izazovno implementirati ga od nule.
Kao što smo naučili u [Lekciji 2](../../../02-explore-agentic-frameworks), agentic frameworki nam pružaju unaprijed izrađene gradivne blokove za implementaciju upotrebe alata.
 
## Primjeri upotrebe alata s agentic frameworkima

Evo nekoliko primjera kako možete implementirati Dizajnerski obrazac upotrebe alata koristeći različite agentic frameworke:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je open-source AI okvir za .NET, Python i Java programere koji rade s velikim jezičnim modelima (LLM). Pojednostavljuje proces korištenja poziva funkcija automatski opisujući vaše funkcije i njihove parametre modelu kroz proces nazvan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serijalizacijom</a>. Također upravlja dvosmjernom komunikacijom između modela i vašeg koda. Još jedna prednost korištenja agentic frameworka poput Semantic Kernel jest što vam omogućuje pristup unaprijed izrađenim alatima poput <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> i <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Sljedeća dijagrama ilustrira proces poziva funkcija s Semantic Kernel:

![function calling](../../../translated_images/hr/functioncalling-diagram.a84006fc287f6014.webp)

U Semantic Kernel funkcije/alati nazivaju se <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Funkciju `get_current_time` koju smo ranije vidjeli možemo pretvoriti u plugin tako da je stavimo u klasu. Također možemo uvesti dekorator `kernel_function` koji prima opis funkcije. Kada zatim kreirate kernel s GetCurrentTimePlugin, kernel će automatski serijalizirati funkciju i njene parametre te u tom procesu kreirati shemu za slanje LLM-u.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Kreiraj kernel
kernel = Kernel()

# Kreiraj dodatak
get_current_time_plugin = GetCurrentTimePlugin(location)

# Dodaj dodatak u kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je noviji agentic framework dizajniran da omogući programerima sigurno izgradnju, implementaciju i skaliranje visokokvalitetnih i proširivih AI agenata bez potrebe za upravljanjem osnovnim računalnim i spremišnim resursima. Posebno je koristan za poslovne aplikacije jer je potpuno upravljana usluga razine poduzeća s naprednom sigurnošću.

U usporedbi s razvojem direktno putem LLM API-ja, Azure AI Agent Service nudi neke prednosti, uključujući:

- Automatsko pozivanje alata – nema potrebe za parsiranjem poziva alatu, pozivanjem alata i upravljanjem odgovorom; sve se sada obavlja na strani servera
- Sigurno upravljanje podacima – umjesto upravljanja vlastitim stanjem konverzacije, možete se osloniti na threadove koji pohranjuju sve potrebne informacije
- Alati spremni za upotrebu – Alati koje možete koristiti za interakciju s vašim izvorima podataka, poput Bing-a, Azure AI Search i Azure Functions.

Alati dostupni u Azure AI Agent Service mogu se podijeliti u dvije kategorije:

1. Alati za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezivanje s Bing pretragom</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraživanje datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alati za akcije:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter koda</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani OpenAPI-jem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service omogućuje da ove alate koristimo zajedno kao `toolset`. Također koristi `threadove` koji prate povijest poruka iz određene konverzacije.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti konverzacijski agent koji može odgovarati na pitanja o vašim prodajnim podacima.

Slika ispod ilustrira kako možete koristiti Azure AI Agent Service za analizu vaših prodajnih podataka:

![Agentic Service In Action](../../../translated_images/hr/agent-service-in-action.34fb465c9a84659e.webp)

Za korištenje bilo kojeg od ovih alata s uslugom možemo kreirati klijenta i definirati alat ili skup alata. Za praktičnu implementaciju možemo koristiti sljedeći Python kod. LLM će moći pogledati skup alata i odlučiti hoće li koristiti korisnički definiranu funkciju `fetch_sales_data_using_sqlite_query` ili unaprijed izrađeni Code Interpreter, ovisno o zahtjevu korisnika.

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

# Inicijaliziraj agenta za pozivanje funkcija s funkcijom fetch_sales_data_using_sqlite_query i dodaj je u skup alata
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicijaliziraj alat za interpretaciju koda i dodaj ga u skup alata.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koje su posebne razmatranja pri korištenju Dizajnerskog obrasca upotrebe alata za izgradnju pouzdanih AI agenata?

Česta zabrinutost vezana za SQL dinamički generirani od strane LLM-ova jest sigurnost, posebno rizik od SQL injekcija ili zlonamjernih radnji poput brisanja ili izmjena baze podataka. Iako su ove zabrinutosti opravdane, mogu se učinkovito ublažiti pravilnom konfiguracijom dozvola pristupa bazi podataka. Za većinu baza podataka to uključuje konfiguraciju baze kao samo za čitanje. Za baze podataka poput PostgreSQL ili Azure SQL aplikaciji treba dodijeliti ulogu samo za čitanje (SELECT).
Pokretanje aplikacije u sigurnom okruženju dodatno pojačava zaštitu. U poslovnim scenarijima, podaci se obično ekstrahiraju i transformiraju iz operativnih sustava u bazu podataka ili skladište podataka samo za čitanje s korisnički prilagođenom shemom. Ovaj pristup osigurava da su podaci sigurni, optimizirani za izvedbu i pristupačnost, te da aplikacija ima ograničen pristup samo za čitanje.

## Primjeri koda

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate li više pitanja o alatu Upotreba oblikovnih obrazaca?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se upoznali s ostalim učenicima, sudjelovali na radnim satima i dobili odgovore na pitanja vezana uz AI agente.

## Dodatni resursi

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Prethodni lekcija

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden pomoću AI prijevoda usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->