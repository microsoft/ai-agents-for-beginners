[![Raziskovanje ogrodij AI agentov](../../../translated_images/sl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite zgornjo sliko za ogled videoposnetka tega lekcije)_

# Raziskovanje ogrodij AI agentov

Ogrodja AI agentov so programske platforme, zasnovane za poenostavitev ustvarjanja, nameščanja in upravljanja AI agentov. Ta ogrodja razvijalcem nudijo vnaprej izdelane komponente, abstrakcije in orodja, ki poenostavljajo razvoj zapletenih AI sistemov.

Ta ogrodja razvijalcem pomagajo osredotočiti se na edinstvene vidike njihovih aplikacij, saj zagotavljajo standardizirane pristope k pogostim izzivom pri razvoju AI agentov. Izboljšujejo razširljivost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod

Ta lekcija bo obravnavala:

- Kaj so ogrodja AI agentov in kaj razvijalcem omogočajo?
- Kako lahko ekipe z njimi hitro izdelajo prototipe, iterirajo in izboljšajo zmogljivosti svojih agentov?
- Kakšne so razlike med ogrodji in orodji, ki jih ustvarja Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> in <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ali lahko neposredno integriram svoja obstoječa orodja iz Azure ekosistema, ali potrebujem samostojne rešitve?
- Kaj je Microsoft Foundry Agent Service in kako mi pomaga?

## Cilji učenja

Cilji te lekcije so vam pomagati razumeti:

- Vlogo ogrodij AI agentov pri razvoju AI.
- Kako izkoristiti ogrodja AI agentov za gradnjo inteligentnih agentov.
- Ključne zmogljivosti, ki jih omogočajo ogrodja AI agentov.
- Razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service.

## Kaj so ogrodja AI agentov in kaj razvijalcem omogočajo?

Tradicionalna AI ogrodja vam lahko pomagajo integrirati AI v vaše aplikacije in te aplikacije izboljšati na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov za zagotavljanje osebnih priporočil, vsebin in izkušenj.
Primer: Streaming storitve, kot je Netflix, uporabljajo AI za predlaganje filmov in serij na podlagi zgodovine gledanja, kar povečuje vključenost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoče se naloge, poenostavi delovne procese in izboljša operativno učinkovitost.
Primer: Aplikacije za podporo strankam uporabljajo AI-poganjane chatbote za obravnavanje pogostih vprašanj, s čimer zmanjšajo čas odziva in sprostijo človeške agente za bolj zapletene zadeve.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša celotno uporabniško izkušnjo z inteligentnimi funkcijami, kot so prepoznavanje glasu, obdelava naravnega jezika in prediktivno besedilo.
Primer: Virtualni asistenti, kot sta Siri in Google Assistant, uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, kar olajša interakcijo uporabnikov z napravami.

### Vse to se sliši odlično, zakaj potem potrebujemo ogrodje AI agentov?

Ogrodja AI agentov predstavljajo nekaj več kot zgolj AI ogrodja. Namenjena so omogočanju ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem, da dosežejo specifične cilje. Ti agenti lahko kažejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se pogojem. Oglejmo si nekatere ključne zmogljivosti, ki jih omogočajo ogrodja AI agentov:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in usklajujejo delo za reševanje kompleksnih nalog.
- **Avtomatizacija in upravljanje nalog**: Zagotavljajo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, delegiranje nalog in dinamično upravljanje med agenti.
- **Kontekstualno razumevanje in prilagajanje**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočim se okoljem in sprejemanja odločitev na podlagi informacij v realnem času.

Povzemimo: agenti vam omogočajo več, da dvignete avtomatizacijo na višjo raven in ustvarite bolj inteligentne sisteme, ki se lahko prilagajajo in učijo iz svojega okolja.

## Kako hitro izdelati prototip, iterirati in izboljšati zmogljivosti agenta?

To je hitro spreminjajoče se področje, a obstajajo skupne značilnosti pri večini ogrodij AI agentov, ki vam lahko pomagajo hitro izdelati prototip in iterirati, na primer modularni sestavni deli, orodja za sodelovanje in učenje v realnem času. Pogledamo te podrobneje:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej izdelane komponente, kot so AI in pomnilniški priključki, klic funkcij z uporabo naravnega jezika ali vtičnikov kode, predloge spodbujanja itd.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente z določenimi vlogami in nalogami, ki omogočajo testiranje in izboljševanje sodelovalnih delovnih tokov.
- **Učite se v realnem času**: Uvedite povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporabite modularne komponente

SDK-ji, kot je Microsoft Agent Framework, ponujajo vnaprej izdelane komponente, kot so AI priključki, definicije orodij in upravljanje agentov.

**Kako ekipe lahko to uporabijo**: Ekipe lahko hitro sestavijo te komponente za ustvarjanje funkcionalnega prototipa brez začetka iz nič, kar omogoča hitro eksperimentiranje in iteracijo.

**Kako to deluje v praksi**: Uporabite lahko vnaprej izdelan parser za izvleček informacij iz uporabniškega vnosa, modul pomnilnika za shranjevanje in pridobivanje podatkov ter generator spodbujanja za interakcijo z uporabniki, vse to brez gradnje teh komponent iz nič.

**Primer kode**. Poglejmo primer, kako uporabiti Microsoft Agent Framework z `FoundryChatClient`, da model odgovarja na uporabniški vnos s klicem orodij:

``` python
# Microsoft Agent Framework Python Primer

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Določite vzorčno funkcijo orodja za rezervacijo potovanja
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

Iz tega primera je razvidno, kako lahko uporabite vnaprej izdelan parser za izvleček ključnih informacij iz uporabniškega vnosa, kot so izvor, cilj in datum zahteve za rezervacijo leta. Ta modularni pristop vam omogoča osredotočenje na logiko višje ravni.

### Izkoristite orodja za sodelovanje

Ogrodja, kot je Microsoft Agent Framework, omogočajo ustvarjanje več agentov, ki lahko sodelujejo.

**Kako ekipe lahko to uporabijo**: Ekipe lahko oblikujejo agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljševanje sodelovalnih delovnih tokov ter izboljšanje učinkovitosti sistema.

**Kako to deluje v praksi**: Ustvarite lahko ekipo agentov, kjer ima vsak agent specializirano funkcijo, na primer pridobivanje podatkov, analizo ali sprejemanje odločitev. Ti agenti lahko komunicirajo in si delijo informacije za dosego skupnega cilja, kot je odgovor na uporabniško poizvedbo ali dokončanje naloge.

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

# Zagon agentov zaporedno za nalogo
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V zgornji kodi vidite, kako ustvariti nalogo, ki vključuje več agentov, ki sodelujejo pri analizi podatkov. Vsak agent opravlja določeno funkcijo, naloga pa se izvaja s koordinacijo agentov za dosego želenega rezultata. Z ustvarjanjem namensko specializiranih agentov lahko izboljšate učinkovitost in uspešnost naloge.

### Učenje v realnem času

Napredna ogrodja omogočajo razumevanje konteksta in prilagajanje v realnem času.

**Kako ekipe lahko to uporabijo**: Ekipe lahko uvedejo povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje, kar vodi v neprestano izboljševanje in izpopolnjevanje zmogljivosti.

**Kako to deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, okoljske podatke in rezultate nalog ter posodabljajo svojo bazo znanja, prilagajajo algoritme odločanja in izboljšujejo uspešnost skozi čas. Ta iterativni postopek učenja omogoča agentom prilagajanje na spreminjajoče se pogoje in uporabniške preference ter izboljšuje učinkovitost sistema kot celote.

## Kakšne so razlike med Microsoft Agent Framework in Microsoft Foundry Agent Service?

Obstaja veliko načinov za primerjavo teh pristopov, a oglejmo si nekatere ključne razlike glede njihove zasnove, zmogljivosti in ciljnih primerov uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework nudi poenostavljen SDK za gradnjo AI agentov z uporabo `FoundryChatClient`. Razvijalcem omogoča ustvarjanje agentov, ki izkoriščajo Azure OpenAI modele s vgrajenim klicanjem orodij, upravljanjem pogovorov ter varnostjo na podlagi Azure identitete.

**Primeri uporabe**: Gradnja produkcijsko pripravljenih AI agentov z uporabo orodij, večstopenjskih delovnih tokov in scenarijev integracije za podjetja.

Tu je nekaj pomembnih osnovnih konceptov Microsoft Agent Framework:

- **Agenti**. Agent je ustvarjen preko `FoundryChatClient` in konfiguriran z imenom, navodili in orodji. Agent lahko:
  - **Obdeluje uporabniška sporočila** in ustvarja odgovore z uporabo Azure OpenAI modelov.
  - **Samodejno kliče orodja** glede na kontekst pogovora.
  - **Vzdržuje stanje pogovora** skozi več interakcij.

  Tukaj je primer kode, ki prikazuje, kako ustvariti agenta:

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

- **Orodja**. Ogrodje podpira definiranje orodij kot Python funkcij, ki jih lahko agent samodejno kliče. Orodja se registrirajo ob ustvarjanju agenta:

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

- **Koordinacija več agentov**. Lahko ustvarite več agentov z različnimi specializacijami in usklajujete njihovo delo:

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

- **Integracija Azure identitete**. Ogrodje uporablja `AzureCliCredential` (ali `DefaultAzureCredential`) za varno, brezključeno avtentikacijo, kar odpravlja zadrževanje in upravljanje API ključev.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novejša storitev, predstavljena na Microsoft Ignite 2024. Omogoča razvoj in nameščanje AI agentov z bolj prilagodljivimi modeli, kot je neposredno klicanje odprtokodnih LLM-jev, na primer Llama 3, Mistral in Cohere.

Microsoft Foundry Agent Service zagotavlja močnejše mehanizme varnosti za podjetja in metode shranjevanja podatkov, zaradi česar je primeren za poslovne aplikacije.

Deluje out-of-the-box z Microsoft Agent Framework za gradnjo in nameščanje agentov.

Storitev je trenutno v javnem pregledu in podpira Python ter C# za izdelavo agentov.

Z uporabo Python SDK-ja za Microsoft Foundry Agent Service lahko ustvarimo agenta z orodjem, ki ga definira uporabnik:

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
        model="gpt-4o-mini",
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

- **Agent**. Microsoft Foundry Agent Service je integriran z Microsoft Foundry. V Microsoft Foundry deluje AI Agent kot "pametna" mikrostoritvena enota, ki lahko odgovarja na vprašanja (RAG), izvaja dejanja ali povsem avtomatizira delovne tokove. To doseže z združevanjem moči generativnih AI modelov z orodji, ki omogočajo dostop in interakcijo z realnimi podatkovnimi viri. Tukaj je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-4o-mini`, imenom `my-agent` in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Teme in sporočila**. Tema je še en pomemben koncept. Predstavlja pogovor ali interakcijo med agentom in uporabnikom. Teme se uporabljajo za spremljanje napredka pogovora, shranjevanje kontekstualnih informacij in upravljanje stanja interakcije. Tukaj je primer teme:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Prosite agenta, naj opravi delo na nitki
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Pridobite in zabeležite vsa sporočila, da vidite odziv agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V prejšnji kodi je ustvarjena tema. Nato je poslano sporočilo temi. Z uporabo `create_and_process_run` je agentu naročeno, naj opravi delo na temi. Na koncu so sporočila pridobljena in zabeležena za ogled odziva agenta. Sporočila prikazujejo potek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da sporočila lahko vsebujejo različne tipe, kot so besedilo, slike ali datoteke, kar pomeni, da je delo agenta privedlo do na primer slike ali besedilnega odgovora. Kot razvijalec lahko te informacije uporabite za nadaljnjo obdelavo odgovora ali za predstavitev uporabniku.

- **Integracija z Microsoft Agent Framework**. Microsoft Foundry Agent Service deluje brezhibno z Microsoft Agent Framework, kar pomeni, da lahko z `FoundryChatClient` gradite agente in jih pri produkciji nameščate preko Agent Service.

**Primeri uporabe**: Microsoft Foundry Agent Service je zasnovan za poslovne aplikacije, ki zahtevajo varno, razširljivo in prilagodljivo nameščanje AI agentov.

## Kakšna je razlika med tema pristopoma?
 
Res se zdi, da obstaja prekrivanje, a obstajajo ključne razlike v zasnovi, zmogljivostih in ciljni uporabi:
 
- **Microsoft Agent Framework (MAF)**: Produkcijsko pripravljen SDK za gradnjo AI agentov. Nudi poenostavljen API za ustvarjanje agentov z klicem orodij, upravljanjem pogovorov in integracijo Azure identitete.
- **Microsoft Foundry Agent Service**: Platforma in storitev za nameščanje v Microsoft Foundry za agente. Ponuja vgrajeno povezljivost do storitev, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.
 
Še vedno niste prepričani, katerega izbrati?

### Primeri uporabe
 
Poglejmo, če vam lahko pomagamo s pogovorom o nekaterih pogostih primerih uporabe:
 
> V: Gradim produkcijske AI agentne aplikacije in želim hitro začeti.
>

>O: Microsoft Agent Framework je odlična izbira. Ponuja preprost, Python-prijazen API preko `FoundryChatClient`, ki vam omogoča definiranje agentov z orodji in navodili v nekaj vrsticah kode.

>V: Potrebujem proizvodno namestitev za podjetja z integracijami Azure, kot je Search in izvajanje kode.
>
> O: Microsoft Foundry Agent Service je najbolj primeren. Je platformna storitev, ki nudi vgrajene zmogljivosti za različne modele, Azure AI Search, Bing Search in Azure Functions. Omogoča enostavno gradnjo agentov v Foundry Portalu in njihovo razširjanje v merilu.
 
> V: Še vedno sem zmeden, dajte mi samo eno možnost.
>
> O: Začnite z Microsoft Agent Framework za gradnjo agentov in nato uporabite Microsoft Foundry Agent Service, ko boste potrebovali njihovo namestitev in razširjanje v produkciji. Ta pristop vam omogoča hitro iteracijo na logiki agenta, hkrati pa zagotavlja jasen varen način za poslovno namestitev.
 
Povzemimo ključne razlike v tabeli:

| Ogrodje | Fokus | Osnovni koncepti | Primeri uporabe |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Poenostavljen SDK za agente z klicem orodij | Agenti, Orodja, Azure identiteta | Gradnja AI agentov, uporaba orodij, večstopenjski delovni tokovi |
| Microsoft Foundry Agent Service | Prilagodljivi modeli, varnost za podjetja, Generiranje kode, Klic orodij | Modularnost, Sodelovanje, Orkestracija procesov | Varnostno, razširljivo in prilagodljivo nameščanje AI agentov |

## Ali lahko neposredno integriram svoja obstoječa orodja iz Azure ekosistema, ali potrebujem samostojne rešitve?


Odgovor je da, lahko integrirate vaše obstoječe Azure ekosistemske orodja neposredno z Microsoft Foundry Agent Service, še posebej, ker je ta zasnovan za brezšivno delovanje z drugimi Azure storitvami. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Obstaja tudi globoka integracija z Microsoft Foundry.

Microsoft Agent Framework se prav tako povezuje z Azure storitvami preko `FoundryChatClient` in identitete Azure, kar omogoča klic Azure storitev neposredno iz vaših agentnih orodij.

## Primeri kode

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate več vprašanj o AI Agent Frameworkih?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z drugimi učenci, udeležite ur odprtih vrat in dobite odgovore na vprašanja o vaših AI agentih.

## Viri

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje agentnih oblikovalskih vzorcev](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->