[![Raziščite okvire AI agentov](../../../translated_images/sl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Raziščite okvire AI agentov

Okviri AI agentov so programske platforme zasnovane za poenostavitev ustvarjanja, uvajanja in upravljanja AI agentov. Ti okviri razvijalcem nudijo vnaprej pripravljene komponente, abstrakcije in orodja, ki poenostavijo razvoj zapletenih AI sistemov.

Ti okviri pomagajo razvijalcem, da se osredotočijo na edinstvene vidike svojih aplikacij z zagotavljanjem standardiziranih pristopov k pogostim izzivom pri razvoju AI agentov. Izboljšujejo skalabilnost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod

Ta lekcija bo zajemala:

- Kaj so okviri AI agentov in kaj razvijalcem omogočajo?
- Kako lahko ekipe uporabijo te okvire za hitro izdelavo prototipov, iteracijo in izboljšanje zmogljivosti agenta?
- Kakšne so razlike med okviri in orodji, ki jih je ustvaril Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> in <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ali lahko neposredno integriram obstoječa orodja Azure, ali potrebujem samostojne rešitve?
- Kaj je Microsoft Foundry Agent Service in kako mi pomaga?

## Cilji učenja

Cilji te lekcije so, da vam pomagajo razumeti:

- Vlogo okvirov AI agentov pri razvoju AI.
- Kako izkoristiti okvire AI agentov za gradnjo inteligentnih agentov.
- Ključne zmogljivosti, ki jih omogočajo okviri AI agentov.
- Razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service.

## Kaj so okviri AI agentov in kaj razvijalcem omogočajo?

Tradicionalni AI okviri vam lahko pomagajo integrirati AI v vaše aplikacije in te aplikacije izboljšajo na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov ter nudi personalizirane priporočila, vsebine in izkušnje.
Primer: Pretakalne storitve kot Netflix uporabljajo AI za predlaganje filmov in oddaj na podlagi zgodovine gledanja, kar povečuje angažiranost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoča se opravila, optimizira delovne procese in izboljša operativno učinkovitost.
Primer: Aplikacije za podporo strankam uporabljajo AI pogonjene klepetalne bote za upravljanje pogostih vprašanj, kar zmanjšuje čase odziva in sprošča človeške agente za zahtevnejše naloge.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša celotno uporabniško izkušnjo z inteligentnimi funkcijami, kot so prepoznavanje glasu, obdelava naravnega jezika in napovedno vnašanje besedila.
Primer: Virtualni asistenti kot Siri in Google Assistant uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, kar uporabnikom olajša interakcijo z napravami.

### Vse to se sliši odlično, zakaj potem potrebujemo okvir AI agentov?

Okviri AI agentov predstavljajo nekaj več kot le AI okvire. Zasnovani so za omogočanje ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem, da dosežejo določene cilje. Ti agenti lahko kažejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se pogojem. Oglejmo si nekaj ključnih zmogljivosti, ki jih omogočajo okviri AI agentov:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in usklajujejo reševanje zahtevnih nalog.
- **Avtomatizacija in upravljanje nalog**: Nudijo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, dodeljevanje nalog in dinamično upravljanje nalog med agenti.
- **Razumevanje konteksta in prilagajanje**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočim se okoljem in sprejemanja odločitev na podlagi informacij v realnem času.

Povzetek: agenti vam omogočajo več – popeljati avtomatizacijo na višjo raven, ustvariti bolj inteligentne sisteme, ki se znajo prilagajati in učiti iz svojega okolja.

## Kako hitro izdelati prototip, iterirati in izboljšati zmogljivosti agenta?

To je hitrorastoče področje, vendar obstajajo nekatere skupne značilnosti večine okvirov AI agentov, ki vam pomagajo hitro izdelati prototip in iterirati, torej modularne komponente, orodja za sodelovanje in učenje v realnem času. Poglobimo se v te:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej pripravljene komponente, kot so AI in pomnilniške povezave, klicanje funkcij z naravnim jezikom ali kodo, predloge pozivov in drugo.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente z določenimi vlogami in nalogami, kar omogoča testiranje in izboljševanje sodelovalnih delovnih tokov.
- **Učite se v realnem času**: Implementirajte povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporaba modularnih komponent

SDK-ji, kot je Microsoft Agent Framework, nudijo vnaprej pripravljene komponente, kot so AI konektorji, opisi orodij in upravljanje agentov.

**Kako to uporabljajo ekipe**: Ekipe lahko hitro sestavijo te komponente za ustvarjanje funkcionalnega prototipa brez začetka od začetka, kar omogoča hitro eksperimentiranje in iteracijo.

**Kako deluje v praksi**: Uporabite lahko vnaprej pripravljen razčlenjevalec za izvlečenje informacij iz uporabniškega vnosa, modul pomnilnika za shranjevanje in pridobivanje podatkov ter generator pozivov za interakcijo z uporabniki, vse brez potrebe po gradnji teh komponent od začetka.

**Primer kode**. Poglejmo primer, kako lahko uporabite Microsoft Agent Framework z `FoundryChatClient`, da model odgovarja na uporabniški vnos z uporabo klica orodij:

``` python
# Microsoft Agent Framework Primer v Pythonu

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Določi vzorčno orodje za rezervacijo potovanja
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Primer izpisa: Vaš let za New York dne 1. januar 2025 je bil uspešno rezerviran. Srečno potovanje! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iz tega primera lahko vidite, kako lahko izkoristite vnaprej pripravljen razčlenjevalec za izvlečenje ključnih informacij iz uporabniškega vnosa, kot so izvor, cilj in datum za zahtevo po rezervaciji leta. Ta modularni pristop vam omogoča osredotočanje na visokonivojsko logiko.

### Izkoristite orodja za sodelovanje

Okviri, kot je Microsoft Agent Framework, olajšajo ustvarjanje več agentov, ki lahko skupaj delajo.

**Kako to uporabljajo ekipe**: Ekipe lahko oblikujejo agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljševanje sodelovalnih delovnih tokov ter povečanje učinkovitosti sistema.

**Kako deluje v praksi**: Lahko ustvarite skupino agentov, kjer ima vsak agent specializirano funkcijo, kot je pridobivanje podatkov, analiza ali odločanje. Ti agenti lahko komunicirajo in delijo informacije za dosego skupnega cilja, na primer odgovora na uporabniško vprašanje ali izvedbo naloge.

**Primer kode (Microsoft Agent Framework)**:

```python
# Ustvarjanje več agentov, ki skupaj delujejo z uporabo Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent za pridobivanje podatkov
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent za analizo podatkov
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Zaženite agente zaporedno za nalogo
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V zgornji kodi lahko vidite, kako ustvariti nalogo, ki vključuje več agentov, ki skupaj analizirajo podatke. Vsak agent opravlja določeno funkcijo, naloga pa se izvaja s koordinacijo agentov za dosego želenega rezultata. Z ustvarjanjem namensko specializiranih agentov lahko izboljšate učinkovitost in zmogljivost nalog.

### Učenje v realnem času

Napredni okviri ponujajo zmogljivosti za razumevanje konteksta in prilagajanje v realnem času.

**Kako to uporabljajo ekipe**: Ekipe lahko implementirajo povratne zanke, kjer se agenti učijo iz interakcij in dinamično spreminjajo svoje vedenje, kar vodi do neprekinjenega izboljševanja in izpopolnjevanja zmogljivosti.

**Kako deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, okoljske podatke in rezultate nalog za posodabljanje svoje baze znanja, prilagoditev algoritmov odločanja in izboljšavo zmogljivosti skozi čas. Ta iterativni proces učenja omogoča agentom prilagajanje spreminjajočim se pogojem in željam uporabnikov ter izboljšuje učinkovitost celotnega sistema.

## Kakšne so razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service?

Obstaja veliko načinov za primerjavo teh pristopov, poglejmo nekatere ključne razlike glede na njihovo zasnovo, zmogljivosti in ciljne primere uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework zagotavlja optimiziran SDK za izdelavo AI agentov z uporabo `FoundryChatClient`. Omogoča razvijalcem ustvarjanje agentov, ki izkoriščajo Azure OpenAI modele z vgrajenim klicem orodij, upravljanjem pogovorov in varnostjo na podlagi Azure identitete za poslovno raven.

**Primeri uporabe**: Izdelava produkcijsko pripravljenih AI agentov z uporabo orodij, večstopenjskimi delovnimi tokovi in scenariji integracije v podjetju.

Tu so nekateri pomembni osnovni koncepti Microsoft Agent Framework:

- **Agenti**. Agent se ustvari prek `FoundryChatClient` in konfigurira z imenom, navodili in orodji. Agent lahko:
  - **Obdeluje sporočila uporabnikov** in generira odzive z uporabo Azure OpenAI modelov.
  - **Samodejno kliče orodja** glede na kontekst pogovora.
  - **Vzdržuje stanje pogovora** čez več interakcij.

  Tu je primer kode, ki prikazuje, kako ustvariti agenta:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Orodja**. Okvir podpira definiranje orodij kot Python funkcij, ki jih agent lahko samodejno kliče. Orodja se registrirajo ob ustvarjanju agenta:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Koordinacija več agentov**. Lahko ustvarite več agentov s različnimi specializacijami in koordinirate njihovo delo:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integracija identitete Azure**. Okvir uporablja `AzureCliCredential` (ali `DefaultAzureCredential`) za varno, brezključavno overjanje, kar odpravlja potrebo po neposrednem upravljanju API ključev.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novejša storitev, predstavljena na Microsoft Ignite 2024. Omogoča razvoj in uvajanje AI agentov z bolj prilagodljivimi modeli, kot so neposredni klici odprtokodnih LLM-jev, kot so Llama 3, Mistral in Cohere.

Microsoft Foundry Agent Service zagotavlja močnejše mehanizme varnosti na podjetniški ravni in metode shranjevanja podatkov, zaradi česar je primeren za podjetniške aplikacije.

Deluje takoj z Microsoft Agent Framework za gradnjo in uvajanje agentov.

Ta storitev je trenutno v javnem pregledu in podpira Python in C# za izdelavo agentov.

Z uporabo Python SDK-ja Microsoft Foundry Agent Service lahko ustvarimo agenta z orodjem, ki ga definira uporabnik:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Določite funkcije orodja
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Osnovni koncepti

Microsoft Foundry Agent Service ima naslednje osnovne koncepte:

- **Agent**. Microsoft Foundry Agent Service se integrira z Microsoft Foundry. V Microsoft Foundry AI agent deluje kot "pametna" mikrostoritvena enota, ki lahko odgovarja na vprašanja (RAG), izvaja dejanja ali popolnoma avtomatizira delovne tokove. Doseže to z združitvijo moči generativnih AI modelov z orodji, ki jim omogočajo dostop in interakcijo z realnimi podatkovnimi viri. Tukaj je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-5-mini`, imenom `my-agent`, in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Niti in sporočila**. Niti so še en pomemben koncept. Predstavljajo pogovor ali interakcijo med agentom in uporabnikom. Niti se uporabljajo za sledenje napredka pogovora, shranjevanje informacij o kontekstu in upravljanje stanja interakcije. Tukaj je primer niti:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Prosite agenta, naj opravi delo na niti
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Pridobite in zabeležite vsa sporočila, da vidite odziv agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V prej prikazani kodi je ustvarjena nit. Nato je niti poslano sporočilo. Z klicem `create_and_process_run` je agent pozvan k delu na niti. Na koncu so sporočila pridobljena in zabeležena za ogled odgovora agenta. Sporočila kažejo napredek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da so lahko sporočila različnih vrst, kot so besedilo, slika ali datoteka, kar pomeni, da je delo agenta npr. slika ali besedilni odgovor. Kot razvijalec lahko te informacije uporabite za nadaljnjo obdelavo odgovora ali prikaz uporabniku.

- **Integracija z Microsoft Agent Framework**. Microsoft Foundry Agent Service deluje brezhibno z Microsoft Agent Framework, kar pomeni, da lahko agente gradite z `FoundryChatClient` in jih uvajate prek Agent Service za produkcijske scenarije.

**Primeri uporabe**: Microsoft Foundry Agent Service je zasnovan za podjetniške aplikacije, ki zahtevajo varno, skalabilno in prilagodljivo uvajanje AI agentov.

## Kakšna je razlika med tema pristopoma?
 
Zdi se, da obstaja prekrivanje, vendar so tu nekatere ključne razlike glede na zasnovo, zmogljivosti in ciljne primere uporabe:
 
- **Microsoft Agent Framework (MAF)**: Je produkcijsko pripravljen SDK za gradnjo AI agentov. Ponuja poenostavljen API za ustvarjanje agentov z možnostjo klicanja orodij, upravljanjem pogovorov in integracijo Azure identitete.
- **Microsoft Foundry Agent Service**: Je platforma in storitev uvajanja v Microsoft Foundry za agente. Ponuja vgrajeno povezljivost do storitev, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.
 
Še vedno niste prepričani, katerega izbrati?

### Primeri uporabe
 
Poskusimo vam pomagati z nekaj pogostimi primeri uporabe:
 
> Vprašanje: Gradim produkcijske aplikacije AI agentov in želim hitro začeti
>

>Odgovor: Microsoft Agent Framework je odlična izbira. Ponuja preprost, pythonovski API preko `FoundryChatClient`, ki vam omogoča definiranje agentov z orodji in navodili v samo nekaj vrsticah kode.

>Vprašanje: Potrebujem uvajanje na podjetniški ravni z Azure integracijami, kot so Search in izvajanje kode
>
> Odgovor: Microsoft Foundry Agent Service je najbolj primeren. Je platformna storitev, ki zagotavlja vgrajene zmogljivosti za več modelov, Azure AI Search, Bing Search in Azure Functions. Omogoča enostavno gradnjo agentov v Foundry Portalu in njihovo uvajanje v velikem obsegu.
 
> Vprašanje: Še vedno sem zmeden, samo dajte mi eno možnost
>
> Odgovor: Začnite z Microsoft Agent Framework za izdelavo agentov, nato pa uporabite Microsoft Foundry Agent Service, ko jih boste potrebovali uvajati in skalirati v produkciji. Ta pristop vam omogoča hitro iteracijo na logiki agenta, hkrati pa imate jasno pot do uvajanja na podjetniški ravni.
 
Povzemimo ključne razlike v tabeli:

| Okvir | Osrednjost | Osnovni koncepti | Primeri uporabe |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Optimiziran SDK za agente z možnostjo klicanja orodij | Agenti, Orodja, Azure identiteta | Gradnja AI agentov, uporaba orodij, večstopenjski delovni tokovi |
| Microsoft Foundry Agent Service | Prilagodljivi modeli, varnost na podjetniški ravni, generiranje kode, klic orodij | Modularnost, Sodelovanje, Orkestracija procesov | Varno, skalabilno in prilagodljivo uvajanje AI agentov |

## Ali lahko neposredno integriram svoja obstoječa orodja v Azure ekosistemu ali potrebujem samostojne rešitve?


Odgovor je da, lahko integrirate svoje obstoječe Azure ekosistemske pripomočke neposredno z Microsoft Foundry Agent Service, še posebej, ker je bil zasnovan za brezhibno delovanje z drugimi Azure storitvami. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Obstaja tudi globoka integracija z Microsoft Foundry.

Microsoft Agent Framework se prav tako povezuje z Azure storitvami preko `FoundryChatClient` in Azure identitete, kar vam omogoča, da neposredno kličete Azure storitve iz svojih pripomočkov za agente.

## Primeri kod

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate še vprašanja o AI Agent Frameworkih?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje agentnih vzorcev oblikovanja](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->