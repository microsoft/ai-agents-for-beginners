[![Raziščite okvire za AI agente](../../../translated_images/sl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite sliko zgoraj za ogled videa te lekcije)_

# Raziskovanje okvirjev za AI agente

Okviri za AI agente so programske platforme, zasnovane za poenostavitev ustvarjanja, uvajanja in upravljanja AI agentov. Ti okvirji razvijalcem zagotavljajo vnaprej izdelane komponente, abstrakcije in orodja, ki poenostavijo razvoj zapletenih AI sistemov.

Ti okvirji razvijalcem pomagajo osredotočiti se na edinstvene vidike svojih aplikacij z zagotavljanjem standardiziranih pristopov k pogostim izzivom pri razvoju AI agentov. Povečujejo razširljivost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod

Ta lekcija bo zajemala:

- Kaj so okviri za AI agente in kaj omogočajo razvijalcem?
- Kako lahko ekipe hitro prototipirajo, ponavljajo in izboljšajo zmogljivosti svojih agentov?
- Kakšne so razlike med okviri in orodji, ki jih je ustvaril Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> in <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ali lahko neposredno integriram obstoječa orodja iz Azure ekosistema ali potrebujem samostojne rešitve?
- Kaj je Microsoft Foundry Agent Service in kako mi pomaga?

## Cilji učenja

Cilj te lekcije je, da vam pomaga razumeti:

- Vlogo okvirjev za AI agente pri razvoju AI.
- Kako izkoristiti okvire za AI agente za gradnjo inteligentnih agentov.
- Ključne zmožnosti, ki jih omogočajo okviri za AI agente.
- Razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service.

## Kaj so okviri za AI agente in kaj omogočajo razvijalcem?

Tradicionalni okviri za AI vam lahko pomagajo integrirati AI v vaše aplikacije in izboljšajo te aplikacije na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov ter zagotavlja prilagojena priporočila, vsebino in izkušnje.
Primer: Streaming storitve, kot je Netflix, uporabljajo AI za predlaganje filmov in oddaj glede na zgodovino ogledov, kar povečuje angažiranost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoča se opravila, poenostavi delovne tokove in izboljša operativno učinkovitost.
Primer: Aplikacije za podporo strankam uporabljajo AI-poganjane klepetalnike za reševanje pogostih poizvedb, skrajšajo čas odziva in sprostijo človeške agente za bolj zapletene zadeve.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša celotno uporabniško izkušnjo z inteligentnimi funkcijami, kot so prepoznavanje glasu, obdelava naravnega jezika in prediktivno besedilo.
Primer: Virtualni asistenti, kot sta Siri in Google Assistant, uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, s čimer olajšajo interakcijo uporabnikov z napravami.

### Vse to zveni odlično, kaj torej potrebujemo AI Agent Framework?

Okviri za AI agente predstavljajo nekaj več kot le AI okvire. Namenjeni so omogočanju ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem za doseganje določenih ciljev. Ti agenti lahko kažejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se pogojem. Oglejmo si nekaj ključnih zmogljivosti, ki jih omogočajo okviri za AI agente:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in se usklajujejo za reševanje zapletenih nalog.
- **Avtomatizacija in upravljanje nalog**: Zagotavljajo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, delegiranje nalog in dinamično upravljanje nalog med agenti.
- **Kontekstualno razumevanje in prilagajanje**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočim se okoljem in sprejemanja odločitev na podlagi informacij v realnem času.

Torej, povzemimo, agenti omogočajo več, dvigujejo avtomatizacijo na višjo raven, ustvarjajo inteligentnejše sisteme, ki se lahko prilagajajo in učijo iz svojega okolja.

## Kako hitro prototipirati, ponavljati in izboljšati zmogljivosti agenta?

To je hitro spreminjajoče se področje, vendar obstajajo nekatere skupne stvari pri večini okvirjev za AI agente, ki vam lahko pomagajo hitro prototipirati in ponavljati, in sicer modularne komponente, orodja za sodelovanje in učenje v realnem času. Raziščimo jih:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej izdelane komponente, kot so povezave AI in pomnilnika, klicanje funkcij z naravnim jezikom ali kode, predloge pozivov in drugo.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljšanje sodelovalnih delovnih tokov.
- **Učite se v realnem času**: Uvedite povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporabite modularne komponente

SDK-ji, kot je Microsoft Agent Framework, ponujajo predpripravljene komponente, kot so AI povezovalci, definicije orodij in upravljanje agentov.

**Kako to uporabljajo ekipe**: Ekipe lahko hitro sestavijo te komponente, da ustvarijo funkcionalen prototip brez začetek iz nič, kar omogoča hitro eksperimentiranje in ponavljanje.

**Kako to deluje v praksi**: Lahko uporabite vnaprej izdelan parser za izločanje informacij iz uporabniškega vnosa, modul pomnilnika za shranjevanje in pridobivanje podatkov ter generator pozivov za interakcijo z uporabniki, vse brez potrebe po gradnji teh komponent od začetka.

**Primer kode**. Oglejmo si primer, kako lahko uporabite Microsoft Agent Framework z `FoundryChatClient`, da model odgovori na uporabniški vnos s klicanjem orodij:

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
    # Primer izhoda: Vaš let v New York dne 1. januar 2025 je bil uspešno rezerviran. Srečno potovanje! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iz tega primera lahko vidite, kako lahko uporabite vnaprej izdelan parser za izločanje ključnih informacij iz uporabniškega vnosa, kot so izvor, cilj in datum zahteve za rezervacijo leta. Ta modularni pristop vam omogoča, da se osredotočite na logiko na višji ravni.

### Izkoristite orodja za sodelovanje

Okviri, kot je Microsoft Agent Framework, omogočajo ustvarjanje več agentov, ki lahko skupaj delujejo.

**Kako to uporabljajo ekipe**: Ekipe lahko oblikujejo agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljševanje sodelovalnih delovnih tokov ter povečanje učinkovitosti sistema.

**Kako to deluje v praksi**: Lahko ustvarite ekipo agentov, kjer ima vsak agent specializirano funkcijo, kot je pridobivanje podatkov, analiza ali sprejemanje odločitev. Ti agenti lahko komunicirajo in si delijo informacije za doseganje skupnega cilja, na primer odgovarjanje na uporabniško vprašanje ali dokončanje naloge.

**Primer kode (Microsoft Agent Framework)**:

```python
# Ustvarjanje več agentov, ki sodelujejo z uporabo Microsoft Agent Framework

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

# Zagon agentov zaporedno za opravljanje naloge
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V prejšnji kodi vidite, kako lahko ustvarite nalogo, ki vključuje več agentov, ki skupaj analizirajo podatke. Vsak agent opravlja določeno funkcijo, naloga pa se izvaja s koordinacijo agentov za doseganje željenega rezultata. Z ustvarjanjem posebnih agentov z dodeljenimi vlogami lahko izboljšate učinkovitost in uspešnost naloge.

### Učenje v realnem času

Napredni okviri zagotavljajo zmožnosti za razumevanje konteksta v realnem času in prilagajanje.

**Kako to uporabljajo ekipe**: Ekipe lahko uvedejo povratne zanke, v katerih se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje, kar vodi do stalnih izboljšav in izpopolnjevanja zmogljivosti.

**Kako to deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, okoljske podatke in rezultate nalog za posodabljanje svoje baze znanja, prilagajanje algoritmov odločanja in izboljšanje učinkovitosti skozi čas. Ta iterativni učni proces omogoča agentom prilagajanje spreminjajočim se pogojem in uporabniškim preferencam, s čimer se izboljša splošna učinkovitost sistema.

## Kakšne so razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service?

Obstaja veliko načinov za primerjavo teh pristopov, poglejmo nekaj ključnih razlik glede njihove zasnove, zmogljivosti in ciljnih primerov uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ponuja poenostavljen SDK za gradnjo AI agentov z uporabo `FoundryChatClient`. Omogoča razvijalcem ustvarjanje agentov, ki uporabljajo Azure OpenAI modele z vgrajenim klicanjem orodij, upravljanjem pogovorov in varnostjo na ravni podjetja preko Azure identitete.

**Primeri uporabe**: Gradnja produkcijsko pripravljenih AI agentov z uporabo orodij, večstopenjskih delovnih tokov in scenarijev integracije v podjetju.

Tukaj so nekateri pomembni osnovni koncepti Microsoft Agent Frameworka:

- **Agenti**. Agenta ustvarite prek `FoundryChatClient` in ga konfigurirate z imenom, navodili in orodji. Agent lahko:
  - **Obdeluje uporabniška sporočila** in generira odzive z uporabo Azure OpenAI modelov.
  - **Samodejno kliče orodja** glede na kontekst pogovora.
  - **Vzdržuje stanje pogovora** skozi več interakcij.

  Tukaj je izsek kode, ki prikazuje, kako ustvariti agenta:

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

- **Orodja**. Okvir podpira definiranje orodij kot Python funkcij, ki jih lahko agent samodejno kliče. Orodja se registrirajo ob ustvarjanju agenta:

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

- **Koordinacija več agentov**. Lahko ustvarite več agentov z različnimi specializacijami in uskladite njihovo delo:

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

- **Integracija Azure identitete**. Okvir uporablja `AzureCliCredential` (ali `DefaultAzureCredential`) za varno, brezključčno avtentikacijo, kar odpravlja potrebo po upravljanju API ključev neposredno.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novejši dodatek, predstavljen na Microsoft Ignite 2024. Omogoča razvoj in uvajanje AI agentov z bolj prilagodljivimi modeli, kot je neposredno klicanje odprtokodnih LLM-jev, kot so Llama 3, Mistral in Cohere.

Microsoft Foundry Agent Service ponuja močnejše varnostne mehanizme za podjetja in metode shranjevanja podatkov, zato je primeren za aplikacije v podjetjih.

Deluje takoj z Microsoft Agent Framework za ustvarjanje in uvajanje agentov.

Ta storitev je trenutno v javnem pregledu in podpira Python ter C# za gradnjo agentov.

Z uporabo Microsoft Foundry Agent Service Python SDK-ja lahko ustvarimo agenta z orodjem, ki ga določi uporabnik:

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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service vključuje naslednje osnovne koncepte:

- **Agent**. Microsoft Foundry Agent Service se integrira z Microsoft Foundry. V okviru Microsoft Foundry AI agent deluje kot "pameten" mikroservis, ki se lahko uporablja za odgovore na vprašanja (RAG), izvajanje dejanj ali popolno avtomatizacijo delovnih tokov. To doseže z združevanjem moči generativnih AI modelov in orodij, ki mu omogočajo dostop do virov podatkov iz resničnega sveta in z njimi interakcijo. Tu je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-4.1-mini`, imenom `my-agent` in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Vrstica in sporočila**. Vrstica je še en pomemben koncept. Predstavlja pogovor ali interakcijo med agentom in uporabnikom. Vrstice se lahko uporabljajo za spremljanje poteka pogovora, shranjevanje kontekstnih informacij in upravljanje stanja interakcije. Tu je primer vrstice:

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

    V prejšnji kodi je vrstica ustvarjena. Nato je poslano sporočilo v vrstico. Z klicem `create_and_process_run` je agentu naročeno, naj opravi delo na vrstici. Na koncu so sporočila pridobljena in zabeležena, da se vidi odgovor agenta. Sporočila kažejo potek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da so sporočila lahko različnih vrst, kot so besedilo, slika ali datoteka, torej delo agenta je lahko rezultat na primer slike ali besedilnega odgovora. Kot razvijalec lahko te informacije uporabite za nadaljnjo obdelavo odgovora ali njegovo predstavitev uporabniku.

- **Integracija z Microsoft Agent Framework**. Microsoft Foundry Agent Service deluje brezhibno z Microsoft Agent Framework, kar pomeni, da lahko gradite agente z `FoundryChatClient` in jih uvajate prek Agent Service za produkcijske scenarije.

**Primeri uporabe**: Microsoft Foundry Agent Service je zasnovan za podjetniške aplikacije, ki zahtevajo varno, razširljivo in prilagodljivo uvajanje AI agentov.

## Kakšna je razlika med tema pristopoma?
 
Res se zdi, da obstajajo prekrivanja, vendar pa so nekatere ključne razlike glede zasnove, zmogljivosti in ciljnih primerov uporabe:
 
- **Microsoft Agent Framework (MAF)**: Je SDK pripravljen za produkcijo za gradnjo AI agentov. Ponuja poenostavljen API za ustvarjanje agentov s klici orodij, upravljanjem pogovorov in integracijo Azure identitete.
- **Microsoft Foundry Agent Service**: Je platforma in storitev za uvajanje agentov v Microsoft Foundry. Ponuja vgrajene povezave s storitvami, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.
 
Še vedno ne veste, kateri izbrati?

### Primeri uporabe
 
Poglejmo, če vam lahko pomagamo z nekaj pogostimi primeri uporabe:
 
> V: Gradim produkcijske aplikacije z AI agenti in želim hitro začeti
>

>O: Microsoft Agent Framework je odlična izbira. Ponuja enostaven, Pythonov API prek `FoundryChatClient`, ki vam omogoča definiranje agentov z orodji in navodili v le nekaj vrsticah kode.

>V: Potrebujem uvajanje na ravni podjetja z integracijami Azure, kot so Search in izvajanje kode
>
> O: Microsoft Foundry Agent Service je najbolj primeren. Je platformna storitev, ki omogoča vgrajene zmogljivosti za več modelov, Azure AI Search, Bing Search in Azure Functions. Omogoča enostavno gradnjo agentov v Foundry Portalu in njihovo uvajanje v obsegu.
 
> V: Še vedno sem zmeden, samo povejte mi eno možnost
>
> O: Začnite z Microsoft Agent Framework za gradnjo agentov, nato pa uporabite Microsoft Foundry Agent Service, ko jih boste morali uvajati in razširjati v produkciji. Ta pristop vam omogoča hitro ponavljanje na logiki agenta z jasno potjo do uvajanja na ravni podjetja.
 
Povzemimo ključne razlike v tabeli:

| Okvir | Poudarek | Osnovni koncepti | Primeri uporabe |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Poenostavljen SDK za agente z klici orodij | Agenti, Orodja, Azure identiteta | Gradnja AI agentov, uporaba orodij, večstopenjski delovni tokovi |
| Microsoft Foundry Agent Service | Prilagodljivi modeli, podjetniška varnost, generiranje kode, klicanje orodij | Modularnost, sodelovanje, orkestracija procesov | Varno, razširljivo in prilagodljivo uvajanje AI agentov |

## Ali lahko neposredno integriram obstoječa orodja iz Azure ekosistema ali potrebujem samostojne rešitve?


Odgovor je da, lahko neposredno integrirate obstoječa orodja iz ekosistema Azure z Microsoft Foundry Agent Service, še posebej, ker je bilo razvito za nemoteno delovanje z drugimi storitvami Azure. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Obstaja tudi globoka integracija z Microsoft Foundry.

Microsoft Agent Framework se prav tako integrira s storitvami Azure preko `FoundryChatClient` in Azure identitete, kar vam omogoča, da kličete storitve Azure neposredno iz vaših agentnih orodij.

## Primeri kode

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate več vprašanj o AI Agent Frameworks?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z ostalimi učenci, se udeležite uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje vzorcev agentnega oblikovanja](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->