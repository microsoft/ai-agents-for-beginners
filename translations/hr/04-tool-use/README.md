<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-30T09:07:51+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "hr"
}
-->
[![Kako dizajnirati dobre AI agente](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.hr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

# Dizajnerski obrazac za korištenje alata

Alati su zanimljivi jer omogućuju AI agentima širi raspon sposobnosti. Umjesto da agent ima ograničen skup radnji koje može izvršiti, dodavanjem alata agent sada može izvoditi širok raspon radnji. U ovom poglavlju razmotrit ćemo dizajnerski obrazac za korištenje alata, koji opisuje kako AI agenti mogu koristiti specifične alate za postizanje svojih ciljeva.

## Uvod

U ovoj lekciji nastojimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac za korištenje alata?
- Na koje slučajeve upotrebe se može primijeniti?
- Koji su elementi/građevni blokovi potrebni za implementaciju ovog dizajnerskog obrasca?
- Koje su posebne razmatranja za korištenje dizajnerskog obrasca za korištenje alata kako bi se izgradili pouzdani AI agenti?

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Definirati dizajnerski obrazac za korištenje alata i njegovu svrhu.
- Prepoznati slučajeve upotrebe gdje je ovaj obrazac primjenjiv.
- Razumjeti ključne elemente potrebne za implementaciju ovog dizajnerskog obrasca.
- Prepoznati razmatranja za osiguranje pouzdanosti AI agenata koji koriste ovaj obrazac.

## Što je dizajnerski obrazac za korištenje alata?

**Dizajnerski obrazac za korištenje alata** fokusira se na omogućavanje LLM-ovima (velikim jezičnim modelima) da komuniciraju s vanjskim alatima kako bi postigli specifične ciljeve. Alati su kod koji agent može izvršiti kako bi obavio radnje. Alat može biti jednostavna funkcija poput kalkulatora ili API poziv prema usluzi treće strane, poput pretraživanja cijena dionica ili vremenske prognoze. U kontekstu AI agenata, alati su dizajnirani da ih agenti izvršavaju kao odgovor na **funkcijske pozive generirane modelom**.

## Na koje slučajeve upotrebe se može primijeniti?

AI agenti mogu koristiti alate za obavljanje složenih zadataka, dohvaćanje informacija ili donošenje odluka. Dizajnerski obrazac za korištenje alata često se koristi u scenarijima koji zahtijevaju dinamičku interakciju s vanjskim sustavima, poput baza podataka, web usluga ili interpretera koda. Ova sposobnost korisna je za brojne slučajeve upotrebe, uključujući:

- **Dinamičko dohvaćanje informacija:** Agenti mogu upitima prema vanjskim API-jevima ili bazama podataka dohvaćati ažurirane podatke (npr. upit prema SQLite bazi za analizu podataka, dohvaćanje cijena dionica ili vremenskih informacija).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili izvođenje simulacija.
- **Automatizacija radnih procesa:** Automatizacija ponavljajućih ili višekorakih radnih procesa integracijom alata poput planera zadataka, usluga e-pošte ili podatkovnih cjevovoda.
- **Korisnička podrška:** Agenti mogu komunicirati s CRM sustavima, platformama za izdavanje ulaznica ili bazama znanja kako bi riješili korisničke upite.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimanja teksta ili procjene sigurnosti sadržaja kako bi pomogli u zadacima stvaranja sadržaja.

## Koji su elementi/građevni blokovi potrebni za implementaciju dizajnerskog obrasca za korištenje alata?

Ovi građevni blokovi omogućuju AI agentu obavljanje širokog raspona zadataka. Pogledajmo ključne elemente potrebne za implementaciju dizajnerskog obrasca za korištenje alata:

- **Sheme funkcija/alata:** Detaljne definicije dostupnih alata, uključujući naziv funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućuju LLM-u razumijevanje dostupnih alata i kako konstruirati valjane zahtjeve.
- **Logika izvršavanja funkcija:** Upravljanje načinom i vremenom pozivanja alata na temelju korisničke namjere i konteksta razgovora. Ovo može uključivati module za planiranje, mehanizme usmjeravanja ili uvjetne tokove koji dinamički određuju korištenje alata.
- **Sustav za upravljanje porukama:** Komponente koje upravljaju tokom razgovora između korisničkih unosa, odgovora LLM-a, poziva alata i izlaza alata.
- **Okvir za integraciju alata:** Infrastruktura koja povezuje agenta s raznim alatima, bilo da su to jednostavne funkcije ili složene vanjske usluge.
- **Rukovanje pogreškama i validacija:** Mehanizmi za upravljanje neuspjesima u izvršavanju alata, validaciju parametara i upravljanje neočekivanim odgovorima.
- **Upravljanje stanjem:** Praćenje konteksta razgovora, prethodnih interakcija s alatima i trajnih podataka kako bi se osigurala konzistentnost tijekom višekratnih interakcija.

Sljedeće ćemo detaljnije pogledati pozivanje funkcija/alata.

### Pozivanje funkcija/alata

Pozivanje funkcija je primarni način na koji omogućujemo velikim jezičnim modelima (LLM-ovima) interakciju s alatima. Često ćete vidjeti da se "funkcija" i "alat" koriste naizmjenično jer su "funkcije" (blokovi ponovljivog koda) "alati" koje agenti koriste za obavljanje zadataka. Kako bi se kod funkcije pozvao, LLM mora usporediti korisnički zahtjev s opisom funkcije. Za to se LLM-u šalje shema koja sadrži opise svih dostupnih funkcija. LLM tada odabire najprikladniju funkciju za zadatak i vraća njezino ime i argumente. Odabrana funkcija se poziva, njezin odgovor se vraća LLM-u, koji koristi informacije za odgovor na korisnički zahtjev.

Za implementaciju pozivanja funkcija za agente, programeri trebaju:

1. LLM model koji podržava pozivanje funkcija
2. Shemu koja sadrži opise funkcija
3. Kod za svaku opisanu funkciju

Pogledajmo primjer dobivanja trenutnog vremena u određenom gradu kako bismo to ilustrirali:

1. **Inicijalizacija LLM-a koji podržava pozivanje funkcija:**

    Nisu svi modeli podržavaju pozivanje funkcija, stoga je važno provjeriti podržava li LLM koji koristite ovu značajku. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti inicijalizacijom Azure OpenAI klijenta.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Kreiranje sheme funkcije:**

    Zatim ćemo definirati JSON shemu koja sadrži naziv funkcije, opis onoga što funkcija radi te nazive i opise parametara funkcije. Ovu shemu ćemo zatim proslijediti prethodno kreiranom klijentu, zajedno s korisničkim zahtjevom za pronalaženje vremena u San Franciscu. Važno je napomenuti da se vraća **poziv alata**, a ne konačan odgovor na pitanje. Kao što je ranije spomenuto, LLM vraća naziv funkcije koju je odabrao za zadatak i argumente koji će joj biti proslijeđeni.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
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

    Sada kada je LLM odabrao koju funkciju treba pokrenuti, potrebno je implementirati i izvršiti kod koji obavlja zadatak. Kod za dobivanje trenutnog vremena možemo implementirati u Pythonu. Također ćemo trebati napisati kod za izdvajanje naziva i argumenata iz response_message kako bismo dobili konačan rezultat.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Pozivanje funkcija je srž većine, ako ne i svih dizajna alata za agente, no implementacija od nule ponekad može biti izazovna. Kao što smo naučili u [Lekciji 2](../../../02-explore-agentic-frameworks), agentni okviri pružaju nam unaprijed izgrađene građevne blokove za implementaciju korištenja alata.

## Primjeri korištenja alata s agentnim okvirima

Evo nekoliko primjera kako možete implementirati dizajnerski obrazac za korištenje alata koristeći različite agentne okvire:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je open-source AI okvir za .NET, Python i Java programere koji rade s velikim jezičnim modelima (LLM-ovima). Pojednostavljuje proces korištenja pozivanja funkcija automatskim opisivanjem vaših funkcija i njihovih parametara modelu kroz proces nazvan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializacija</a>. Također upravlja komunikacijom između modela i vašeg koda. Još jedna prednost korištenja agentnog okvira poput Semantic Kernel-a je ta što omogućuje pristup unaprijed izgrađenim alatima poput <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">pretraživanja datoteka</a> i <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">interpretera koda</a>.

Sljedeći dijagram ilustrira proces pozivanja funkcija sa Semantic Kernel-om:

![pozivanje funkcija](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.hr.png)

U Semantic Kernel-u funkcije/alati nazivaju se <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Dodaci (Plugins)</a>. Funkciju `get_current_time` koju smo ranije vidjeli možemo pretvoriti u dodatak tako da je pretvorimo u klasu s funkcijom unutar nje. Također možemo uvesti dekorator `kernel_function`, koji prima opis funkcije. Kada zatim kreirate kernel s dodatkom GetCurrentTimePlugin, kernel će automatski serializirati funkciju i njezine parametre, stvarajući shemu za slanje LLM-u u tom procesu.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je noviji agentni okvir dizajniran za omogućavanje programerima da sigurno izgrade, implementiraju i skaliraju visokokvalitetne i proširive AI agente bez potrebe za upravljanjem osnovnim računalnim i skladišnim resursima. Posebno je koristan za poslovne aplikacije jer je potpuno upravljana usluga s razinom sigurnosti prilagođenom poduzećima.

U usporedbi s razvojem izravno s LLM API-jem, Azure AI Agent Service pruža neke prednosti, uključujući:

- Automatsko pozivanje alata – nema potrebe za parsiranjem poziva alata, pozivanjem alata i rukovanjem odgovorom; sve se to sada obavlja na strani poslužitelja
- Sigurno upravljanje podacima – umjesto upravljanja vlastitim stanjem razgovora, možete se osloniti na niti za pohranu svih potrebnih informacija
- Alati spremni za upotrebu – alati koje možete koristiti za interakciju s vašim izvorima podataka, poput Binga, Azure AI Search-a i Azure Functions-a.

Alati dostupni u Azure AI Agent Service-u mogu se podijeliti u dvije kategorije:

1. Alati za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Utemeljenje s Bing pretraživanjem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraživanje datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alati za radnje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter koda</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani OpenAI-jem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service omogućuje korištenje ovih alata zajedno kao `toolset`. Također koristi `threads` koje prate povijest poruka iz određenog razgovora.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti konverzacijskog agenta koji može odgovarati na pitanja o vašim prodajnim podacima.

Sljedeća slika ilustrira kako biste mogli koristiti Azure AI Agent Service za analizu svojih prodajnih podataka:

![Agent Service u akciji](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.hr.jpg)

Za korištenje bilo kojeg od ovih alata s uslugom možemo kreirati klijenta i definirati alat ili skup alata. Za praktičnu implementaciju možemo koristiti sljedeći Python kod. LLM će moći pogledati skup alata i odlučiti hoće li koristiti korisnički definiranu funkciju `fetch_sales_data_using_sqlite_query` ili unaprijed izgrađeni Code Interpreter, ovisno o korisničkom zahtjevu.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koje su posebne razmatranja za korištenje dizajnerskog obrasca za korištenje alata kako bi se izgradili pouzdani AI agenti?

Česta zabrinutost kod SQL-a dinamički generiranog od strane LLM-ova je sigurnost, posebno rizik od SQL injekcija ili zlonamjernih radnji, poput brisanja ili manipulacije bazom podataka. Iako su ove zabrinutosti valjane, mogu se učinkovito ublažiti pravilnom konfiguracijom dozvola za pristup bazi podataka. Za većinu baza podataka to uključuje konfiguriranje baze kao samo za čitanje. Za usluge baza podataka poput PostgreSQL-a ili Azure SQL-a, aplikaciji treba dodijeliti ulogu samo za čitanje (SELECT).

Pokretanje aplikacije u sigurnom okruženju dodatno povećava zaštitu. U poslovnim scenarijima, podaci se obično izvlače i transformiraju iz operativnih sustava u bazu podataka samo za čitanje ili skladište podataka s korisnički prilagođenom shemom. Ovaj pristup osigurava da su podaci sigurni, optimizirani za performanse i pristupačnost te da aplikacija ima ograničen, samo za čitanje pristup.

### Imate dodatna pitanja o dizajnerskom obrascu za korištenje alata?
Pridružite se [Azure AI Foundry Discordu](https://aka.ms/ai-agents/discord) kako biste upoznali druge polaznike, sudjelovali u uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

## Prethodna lekcija

[Razumijevanje obrazaca agentičkog dizajna](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija

[Agentički RAG](../05-agentic-rag/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.