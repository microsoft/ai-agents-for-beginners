[![Kako dizajnirati dobre AI agente](../../../translated_images/hr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Dizajnerski obrazac korištenja alata

Alati su zanimljivi jer omogućuju AI agentima da imaju širi spektar sposobnosti. Umjesto da agent ima ograničeni skup radnji koje može izvršiti, dodavanjem alata agent sada može izvršavati širok raspon radnji. U ovom poglavlju razmotrit ćemo Dizajnerski obrazac korištenja alata, koji opisuje kako AI agenti mogu koristiti određene alate za postizanje svojih ciljeva.

## Uvod

U ovoj lekciji nastojimo odgovoriti na sljedeća pitanja:

- Što je dizajnerski obrazac korištenja alata?
- Za koje se slučajeve upotrebe može primijeniti?
- Koji su elementi/gradivni blokovi potrebni za implementaciju obrasca?
- Koje su posebne napomene za korištenje dizajnerskog obrasca korištenja alata pri izgradnji pouzdanih AI agenata?

## Ciljevi učenja

Nakon završetka ove lekcije moći ćete:

- Definirati dizajnerski obrazac korištenja alata i njegovu svrhu.
- Identificirati slučajeve upotrebe gdje je ovaj obrazac primjenjiv.
- Razumjeti ključne elemente potrebne za provedbu obrasca.
- Prepoznati razmatranja za osiguranje pouzdanosti AI agenata koji koriste ovaj obrazac.

## Što je dizajnerski obrazac korištenja alata?

**Dizajnerski obrazac korištenja alata** fokusira se na omogućavanje LLM-ovima sposobnosti interakcije s vanjskim alatima radi postizanja specifičnih ciljeva. Alati su kod koji agent može izvršavati kako bi obavljao radnje. Alat može biti jednostavna funkcija poput kalkulatora ili poziv API-ja treće strane za usluge poput provjere cijena dionica ili vremenske prognoze. U kontekstu AI agenata, alati su dizajnirani da budu izvršavani od strane agenata kao odgovor na **funkcijske pozive koje generira model**.

## Za koje se slučajeve upotrebe može primijeniti?

AI agenti mogu koristiti alate kako bi dovršili složene zadatke, dohvatili informacije ili donijeli odluke. Dizajnerski obrazac korištenja alata često se koristi u scenarijima koji zahtijevaju dinamičku interakciju s vanjskim sustavima, kao što su baze podataka, web servisi ili interpretatori koda. Ova sposobnost je korisna za mnoge različite slučajeve upotrebe, uključujući:

- **Dinamički dohvat informacija:** Agenti mogu upitavati vanjske API-je ili baze podataka za ažurirane podatke (npr., upit SQLite baze za analizu podataka, dohvat cijena dionica ili informacije o vremenu).
- **Izvršavanje i interpretacija koda:** Agenti mogu izvršavati kod ili skripte za rješavanje matematičkih problema, generiranje izvještaja ili provođenje simulacija.
- **Automatizacija tijeka rada:** Automatizacija ponavljajućih ili višestupanjskih tijekova rada integracijom alata poput raspoređivača zadataka, usluga e-pošte ili podatkovnih cjevovoda.
- **Podrška korisnicima:** Agenti mogu komunicirati s CRM sustavima, platformama za podršku ili bazama znanja radi rješavanja korisničkih upita.
- **Generiranje i uređivanje sadržaja:** Agenti mogu koristiti alate poput provjere gramatike, sažimatelja teksta ili procjenitelja sigurnosti sadržaja kako bi pomogli u zadacima stvaranja sadržaja.

## Koji su elementi/gradivni blokovi potrebni za implementaciju dizajnerskog obrasca korištenja alata?

Ovi gradivni blokovi omogućuju AI agentu izvođenje širokog spektra zadataka. Pogledajmo ključne elemente potrebne za implementaciju Dizajnerskog obrasca korištenja alata:

- **Sheme funkcija/alata**: Detaljni opisi dostupnih alata, uključujući naziv funkcije, svrhu, potrebne parametre i očekivane izlaze. Ove sheme omogućavaju LLM-u razumijevanje dostupnih alata i kako sastaviti valjane zahtjeve.

- **Logika izvršavanja funkcija**: Upravljanja kada i kako se alati pozivaju na temelju korisnikove namjere i konteksta razgovora. Ovo može uključivati module za planiranje, mehanizme usmjeravanja ili uvjetne tokove koji dinamički odlučuju o korištenju alata.

- **Sustav rukovanja porukama**: Komponente koje upravljaju komunikacijskim tokom između korisničkih unosa, LLM odgovora, poziva alata i izlaza alata.

- **Okvir za integraciju alata**: Infrastruktura koja povezuje agenta s različitim alatima, bilo da su jednostavne funkcije ili složene vanjske usluge.

- **Rukovanje pogreškama i validacija**: Mehanizmi za upravljanje neuspjesima u izvršavanju alata, validaciju parametara i upravljanje neočekivanim odgovorima.

- **Upravljanje stanjima**: Praćenje konteksta razgovora, prethodnih interakcija s alatima i trajnih podataka kako bi se osigurala dosljednost kroz višekratne okretaje.

Sljedeće, pogledajmo detaljnije pozivanje funkcija/alata.

### Pozivanje funkcija/alata

Pozivanje funkcija je primarni način na koji omogućavamo Velikim Jezičnim Modelima (LLM-ovima) interakciju s alatima. Često ćete vidjeti da se pojmovi 'funkcija' i 'alat' koriste naizmjenično jer su 'funkcije' (blokovi višekratno upotrebljivog koda) alati koje agenti koriste za izvršavanje zadataka. Da bi se kod funkcije pozvao, LLM mora usporediti korisnički zahtjev s opisom funkcije. Za to se šalje shema koja sadrži opise svih dostupnih funkcija LLM-u. LLM zatim odabire najprikladniju funkciju za zadatak i vraća jej naziv i argumente. Odabrana funkcija se poziva, njezin odgovor se šalje natrag LLM-u, koji koristi informacije za odgovor korisniku.

Da bi developeri implementirali pozivanje funkcija za agente, potrebni su vam:

1. LLM model koji podržava pozivanje funkcija
2. Shema koja sadrži opise funkcija
3. Kod za svaku opisanu funkciju

Iskoristit ćemo primjer dobivanja trenutnog vremena u gradu za ilustraciju:

1. **Inicijalizirajte LLM koji podržava pozivanje funkcija:**

    Nisu svi modeli podržavaju pozivanje funkcija, stoga je važno provjeriti da li model koji koristite podržava tu značajku. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podržava pozivanje funkcija. Možemo započeti iniciranjem Azure OpenAI klijenta.

    ```python
    # Inicijalizirajte Azure OpenAI klijenta
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Kreirajte shemu funkcije:**

    Zatim ćemo definirati JSON shemu koja sadrži naziv funkcije, opis što funkcija radi i nazive te opise parametara funkcije.
    Ovu shemu ćemo proslijediti ranije kreiranom klijentu zajedno sa zahtjevom korisnika za pronalaženjem vremena u San Franciscu. Važno je istaknuti da je **poziv alata** ono što se vraća, **a ne** konačni odgovor na pitanje. Kao što je ranije spomenuto, LLM vraća naziv funkcije koju je odabrao za zadatak i argumente koji će joj biti proslijeđeni.

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
  
    # Početna korisnička poruka
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi API poziv: Zatraži od modela da koristi funkciju
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obradi odgovor modela
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

    Sada kada je LLM odabrao koju funkciju treba pokrenuti, potrebno je implementirati i izvršiti kod koji izvršava zadatak.
    Možemo napisati kod za dobivanje trenutnog vremena u Pythonu. Također ćemo pisati kod za izvlačenje naziva i argumenata iz response_message kako bismo dobili konačni rezultat.

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
  
      # Drugi poziv API-ja: Dobivanje konačnog odgovora od modela
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

Pozivanje funkcija je u srcu većine, ako ne i svih dizajnerskih obrazaca korištenja alata za agente, međutim implementacija od nule može ponekad biti izazovna.
Kao što smo naučili u [Lekcija 2](../../../02-explore-agentic-frameworks), agentni okviri nam pružaju unaprijed izrađene gradivne blokove za implementaciju korištenja alata.
 
## Primjeri korištenja alata s agentnim okvirima

Evo nekoliko primjera kako možete implementirati Dizajnerski obrazac korištenja alata koristeći različite agentne okvire:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI okvir za izgradnju AI agenata. Pojednostavljuje proces korištenja poziva funkcija dozvoljavajući vam da definirate alate kao Python funkcije s dekoratorom `@tool`. Okvir rukuje dvosmjernom komunikacijom između modela i vašeg koda. Također pruža pristup unaprijed izrađenim alatima poput Pretrage datoteka i Interpretatora koda putem `AzureAIProjectAgentProvider`.

Sljedeća dijagrama ilustrira proces pozivanja funkcija s Microsoft Agent Frameworkom:

![pozivanje funkcija](../../../translated_images/hr/functioncalling-diagram.a84006fc287f6014.webp)

U Microsoft Agent Frameworku alati su definirani kao dekorirane funkcije. Možemo pretvoriti funkciju `get_current_time` koju smo ranije vidjeli u alat koristeći dekorator `@tool`. Okvir će automatski serijalizirati funkciju i njene parametre, stvarajući shemu za slanje LLM-u.

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

# Kreirajte agenta i pokrenite alat
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je noviji agentni okvir dizajniran da osnaži developere za sigurno izgradnju, implementaciju i skaliranje visokokvalitetnih i proširivih AI agenata bez potrebe za upravljanjem osnovnim računskim i skladišnim resursima. Posebno je koristan za enterprise aplikacije jer je potpuno upravljana usluga s enterprise razinom sigurnosti.

U usporedbi s razvojem direktno s LLM API-jem, Azure AI Agent Service pruža neke prednosti, uključujući:

- Automatsko pozivanje alata – nema potrebe za parsiranjem poziva alata, izvršavanjem poziva i obradom odgovora; sve se to sada radi na strani servera
- Sigurno upravljanje podacima – umjesto upravljanja stanjem razgovora, možete se osloniti na teme (threads) za pohranu sve potrebne informacije
- Alati spremni za korištenje – alati kojima možete pristupati za interakciju s vašim izvorima podataka, poput Binga, Azure AI Search i Azure funkcija.

Alati dostupni u Azure AI Agent Service mogu se podijeliti u dvije kategorije:

1. Alati za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezanost s Bing pretraživanjem</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pretraga datoteka</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alati za akcije:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pozivanje funkcija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretator koda</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alati definirani po OpenAPI specifikaciji</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure funkcije</a>

Agent Service nam omogućuje da koristimo ove alate zajedno kao `skup alata` (toolset). Također koristi `teme` (threads) koje prate povijest poruka iz određenog razgovora.

Zamislite da ste prodajni agent u tvrtki Contoso. Želite razviti konverzacijski agent koji može odgovarati na pitanja o vašim prodajnim podacima.

Sljedeća slika ilustrira kako biste mogli koristiti Azure AI Agent Service za analizu vaših prodajnih podataka:

![Agentna usluga u akciji](../../../translated_images/hr/agent-service-in-action.34fb465c9a84659e.webp)

Za korištenje bilo kojeg od ovih alata s uslugom možemo kreirati klijenta i definirati alat ili skup alata. Za praktičnu implementaciju možemo koristiti sljedeći Python kod. LLM će moći pregledati skup alata i odlučiti hoće li koristiti korisnički definiranu funkciju `fetch_sales_data_using_sqlite_query` ili unaprijed izrađeni Interpretator koda ovisno o korisničkom zahtjevu.

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

# Inicijaliziraj alat Code Interpreter i dodaj ga u skup alata.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Koje su posebne napomene za korištenje dizajnerskog obrasca korištenja alata pri izgradnji pouzdanih AI agenata?

Česta zabrinutost kod dinamički generiranog SQL-a od strane LLM-ova je sigurnost, osobito rizik od SQL injekcija ili zlonamjernih radnji poput brisanja ili manipulacije bazom podataka. Iako su ove zabrinutosti opravdane, mogu se učinkovito ublažiti pravilnim konfiguriranjem dopuštenja pristupa bazi podataka. Za većinu baza podataka to znači konfiguriranje baze kao samo za čitanje. Za usluge baza podataka poput PostgreSQL ili Azure SQL, aplikaciji treba biti dodijeljena uloga samo za čitanje (SELECT).

Pokretanje aplikacije u sigurnom okruženju dodatno pojačava zaštitu. U enterprise scenarijima podaci se obično izvlače i transformiraju iz operativnih sustava u bazu podataka samo za čitanje ili skladište podataka s korisnički prilagođenom shemom. Ovaj pristup osigurava da su podaci sigurni, optimizirani za performanse i pristupačnost, te da aplikacija ima ograničen pristup samo za čitanje.

## Primjeri koda

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate li dodatna pitanja o Dizajnerskim obrascima korištenja alata?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) zajednici kako biste upoznali druge učenike, sudjelovali u radnim satima i dobili odgovore na svoja pitanja o AI agentima.

## Dodatni resursi

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Radionica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Radionica za višestruke agente Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Frameworka</a>

## Prethodna lekcija

[Razumijevanje agenstkih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

## Sljedeća lekcija
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->