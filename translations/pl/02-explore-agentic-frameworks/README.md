<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:21:14+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pl"
}
-->
[![Eksplorowanie Frameworków Agentów AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.pl.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

# Eksplorowanie Frameworków Agentów AI

Frameworki agentów AI to platformy programowe zaprojektowane w celu uproszczenia tworzenia, wdrażania i zarządzania agentami AI. Dostarczają one programistom gotowe komponenty, abstrakcje i narzędzia, które usprawniają rozwój złożonych systemów AI.

Frameworki te pomagają programistom skupić się na unikalnych aspektach ich aplikacji, oferując ustandaryzowane podejścia do typowych wyzwań w rozwoju agentów AI. Zwiększają skalowalność, dostępność i efektywność w budowaniu systemów AI.

## Wprowadzenie

W tej lekcji omówimy:

- Czym są frameworki agentów AI i co umożliwiają programistom osiągnąć?
- Jak zespoły mogą ich używać do szybkiego prototypowania, iteracji i ulepszania możliwości swoich agentów?
- Jakie są różnice między frameworkami i narzędziami stworzonymi przez Microsoft: <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> i <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Czy mogę zintegrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję samodzielnych rozwiązań?
- Czym jest usługa Azure AI Agents i jak może mi pomóc?

## Cele nauki

Celem tej lekcji jest pomóc Ci zrozumieć:

- Rolę frameworków agentów AI w rozwoju AI.
- Jak wykorzystać frameworki agentów AI do budowy inteligentnych agentów.
- Kluczowe możliwości oferowane przez frameworki agentów AI.
- Różnice między AutoGen, Semantic Kernel i Azure AI Agent Service.

## Czym są frameworki agentów AI i co umożliwiają programistom?

Tradycyjne frameworki AI mogą pomóc w integracji AI z aplikacjami i poprawić je w następujący sposób:

- **Personalizacja**: AI może analizować zachowanie użytkowników i ich preferencje, aby dostarczać spersonalizowane rekomendacje, treści i doświadczenia.  
Przykład: Usługi streamingowe, takie jak Netflix, wykorzystują AI do sugerowania filmów i seriali na podstawie historii oglądania, zwiększając zaangażowanie i satysfakcję użytkowników.
- **Automatyzacja i efektywność**: AI może automatyzować powtarzalne zadania, usprawniać przepływy pracy i poprawiać efektywność operacyjną.  
Przykład: Aplikacje obsługi klienta wykorzystują chatboty zasilane AI do obsługi typowych zapytań, skracając czas odpowiedzi i odciążając ludzkich agentów w bardziej złożonych sprawach.
- **Ulepszone doświadczenie użytkownika**: AI może poprawić ogólne doświadczenie użytkownika, oferując inteligentne funkcje, takie jak rozpoznawanie głosu, przetwarzanie języka naturalnego i przewidywanie tekstu.  
Przykład: Wirtualni asystenci, tacy jak Siri i Google Assistant, wykorzystują AI do rozumienia i odpowiadania na polecenia głosowe, ułatwiając użytkownikom interakcję z urządzeniami.

### Brzmi świetnie, prawda? Więc dlaczego potrzebujemy frameworków agentów AI?

Frameworki agentów AI to coś więcej niż tylko frameworki AI. Są zaprojektowane, aby umożliwić tworzenie inteligentnych agentów, którzy mogą wchodzić w interakcje z użytkownikami, innymi agentami i środowiskiem, aby osiągać określone cele. Agenci ci mogą wykazywać autonomiczne zachowanie, podejmować decyzje i dostosowywać się do zmieniających się warunków. Przyjrzyjmy się kluczowym możliwościom oferowanym przez frameworki agentów AI:

- **Współpraca i koordynacja agentów**: Umożliwiają tworzenie wielu agentów AI, którzy mogą współpracować, komunikować się i koordynować, aby rozwiązywać złożone zadania.
- **Automatyzacja i zarządzanie zadaniami**: Dostarczają mechanizmy do automatyzacji wieloetapowych przepływów pracy, delegowania zadań i dynamicznego zarządzania zadaniami między agentami.
- **Zrozumienie kontekstu i adaptacja**: Wyposażają agentów w zdolność do rozumienia kontekstu, dostosowywania się do zmieniających się środowisk i podejmowania decyzji na podstawie informacji w czasie rzeczywistym.

Podsumowując, agenci pozwalają robić więcej, przenosić automatyzację na wyższy poziom, tworzyć bardziej inteligentne systemy, które mogą uczyć się i adaptować do swojego środowiska.

## Jak szybko prototypować, iterować i ulepszać możliwości agenta?

To dynamicznie rozwijający się obszar, ale istnieją pewne wspólne elementy w większości frameworków agentów AI, które mogą pomóc w szybkim prototypowaniu i iteracji, takie jak modułowe komponenty, narzędzia do współpracy i uczenie w czasie rzeczywistym. Przyjrzyjmy się im bliżej:

- **Wykorzystaj modułowe komponenty**: SDK AI oferują gotowe komponenty, takie jak konektory AI i pamięci, wywoływanie funkcji za pomocą języka naturalnego lub wtyczek kodu, szablony podpowiedzi i inne.
- **Wykorzystaj narzędzia do współpracy**: Projektuj agentów z określonymi rolami i zadaniami, umożliwiając testowanie i udoskonalanie współpracy w ramach przepływów pracy.
- **Ucz się w czasie rzeczywistym**: Wdrażaj pętle zwrotne, w których agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie.

### Wykorzystaj modułowe komponenty

SDK, takie jak Microsoft Semantic Kernel i LangChain, oferują gotowe komponenty, takie jak konektory AI, szablony podpowiedzi i zarządzanie pamięcią.

**Jak zespoły mogą ich używać**: Zespoły mogą szybko złożyć te komponenty, aby stworzyć funkcjonalny prototyp bez konieczności zaczynania od zera, co pozwala na szybkie eksperymentowanie i iterację.

**Jak to działa w praktyce**: Możesz użyć gotowego parsera do wyodrębniania informacji z danych wejściowych użytkownika, modułu pamięci do przechowywania i pobierania danych oraz generatora podpowiedzi do interakcji z użytkownikami, wszystko to bez konieczności budowania tych komponentów od podstaw.

**Przykład kodu**. Przyjrzyjmy się przykładom, jak można użyć gotowego konektora AI z Semantic Kernel w Pythonie i .Net, który wykorzystuje automatyczne wywoływanie funkcji, aby model odpowiadał na dane wejściowe użytkownika:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Z tego przykładu widać, jak można wykorzystać gotowy parser do wyodrębniania kluczowych informacji z danych wejściowych użytkownika, takich jak miejsce wylotu, miejsce docelowe i data rezerwacji lotu. Takie modułowe podejście pozwala skupić się na logice wysokiego poziomu.

### Wykorzystaj narzędzia do współpracy

Frameworki, takie jak CrewAI, Microsoft AutoGen i Semantic Kernel, ułatwiają tworzenie wielu agentów, którzy mogą współpracować.

**Jak zespoły mogą ich używać**: Zespoły mogą projektować agentów z określonymi rolami i zadaniami, umożliwiając testowanie i udoskonalanie współpracy w ramach przepływów pracy oraz poprawę ogólnej efektywności systemu.

**Jak to działa w praktyce**: Możesz stworzyć zespół agentów, gdzie każdy agent ma wyspecjalizowaną funkcję, taką jak pobieranie danych, analiza lub podejmowanie decyzji. Agenci ci mogą komunikować się i dzielić informacjami, aby osiągnąć wspólny cel, taki jak odpowiedź na zapytanie użytkownika lub wykonanie zadania.

**Przykład kodu (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

W poprzednim kodzie widać, jak można stworzyć zadanie, które obejmuje współpracę wielu agentów w celu analizy danych. Każdy agent wykonuje określoną funkcję, a zadanie jest realizowane poprzez koordynację agentów w celu osiągnięcia pożądanego wyniku. Tworząc dedykowanych agentów z wyspecjalizowanymi rolami, można poprawić efektywność i wydajność zadań.

### Ucz się w czasie rzeczywistym

Zaawansowane frameworki oferują możliwości zrozumienia kontekstu w czasie rzeczywistym i adaptacji.

**Jak zespoły mogą ich używać**: Zespoły mogą wdrażać pętle zwrotne, w których agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie, co prowadzi do ciągłego doskonalenia i udoskonalania możliwości.

**Jak to działa w praktyce**: Agenci mogą analizować opinie użytkowników, dane środowiskowe i wyniki zadań, aby aktualizować swoją bazę wiedzy, dostosowywać algorytmy podejmowania decyzji i poprawiać wydajność w czasie. Ten iteracyjny proces uczenia się pozwala agentom dostosowywać się do zmieniających się warunków i preferencji użytkowników, zwiększając ogólną skuteczność systemu.

## Jakie są różnice między frameworkami AutoGen, Semantic Kernel i Azure AI Agent Service?

Istnieje wiele sposobów porównania tych frameworków, ale przyjrzyjmy się kluczowym różnicom w zakresie ich projektowania, możliwości i docelowych przypadków użycia:

## AutoGen

AutoGen to open-source'owy framework opracowany przez Microsoft Research's AI Frontiers Lab. Skupia się na aplikacjach agentowych opartych na zdarzeniach i rozproszonych, umożliwiając wykorzystanie wielu LLM, SLM, narzędzi i zaawansowanych wzorców projektowych dla wielu agentów.

AutoGen opiera się na podstawowej koncepcji agentów, czyli autonomicznych jednostek, które mogą postrzegać swoje środowisko, podejmować decyzje i podejmować działania w celu osiągnięcia określonych celów. Agenci komunikują się za pomocą asynchronicznych wiadomości, co pozwala im działać niezależnie i równolegle, zwiększając skalowalność i responsywność systemu.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenci opierają się na modelu aktora</a>. Według Wikipedii aktor to _podstawowy element obliczeń współbieżnych. W odpowiedzi na otrzymaną wiadomość aktor może: podejmować lokalne decyzje, tworzyć więcej aktorów, wysyłać więcej wiadomości i określać, jak odpowiedzieć na kolejną otrzymaną wiadomość_.

**Przypadki użycia**: Automatyzacja generowania kodu, zadania analizy danych i budowanie niestandardowych agentów do funkcji planowania i badań.

Oto kilka ważnych podstawowych koncepcji AutoGen:

- **Agenci**. Agent to jednostka programowa, która:
  - **Komunikuje się za pomocą wiadomości**, które mogą być synchroniczne lub asynchroniczne.
  - **Utrzymuje swój własny stan**, który może być modyfikowany przez przychodzące wiadomości.
  - **Wykonuje działania** w odpowiedzi na otrzymane wiadomości lub zmiany w swoim stanie. Działania te mogą modyfikować stan agenta i wywoływać efekty zewnętrzne, takie jak aktualizacja dzienników wiadomości, wysyłanie nowych wiadomości, wykonywanie kodu lub wywoływanie API.
    
  Oto krótki fragment kodu, w którym tworzysz własnego agenta z funkcjami czatu:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    W powyższym kodzie utworzono `MyAgent`, który dziedziczy po `RoutedAgent`. Ma on obsługę wiadomości, która drukuje treść wiadomości, a następnie wysyła odpowiedź za pomocą delegata `AssistantAgent`. Szczególnie warto zwrócić uwagę, jak przypisujemy do `self._delegate` instancję `AssistantAgent`, który jest wstępnie zbudowanym agentem obsługującym zakończenia czatu.


    Następnie poinformujmy AutoGen o tym typie agenta i uruchommy program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    W powyższym kodzie agenci są rejestrowani w środowisku wykonawczym, a następnie wysyłana jest wiadomość do agenta, co skutkuje następującym wynikiem:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Wielu agentów**. AutoGen obsługuje tworzenie wielu agentów, którzy mogą współpracować w celu realizacji złożonych zadań. Agenci mogą komunikować się, dzielić informacjami i koordynować swoje działania, aby efektywniej rozwiązywać problemy. Aby stworzyć system wieloagentowy, możesz zdefiniować różne typy agentów o wyspecjalizowanych funkcjach i rolach, takich jak pobieranie danych, analiza, podejmowanie decyzji i interakcja z użytkownikiem. Zobaczmy, jak wygląda takie tworzenie:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    W powyższym kodzie mamy `GroupChatManager`, który jest rejestrowany w środowisku wykonawczym. Menedżer ten odpowiada za koordynację interakcji między różnymi typami agentów, takimi jak pisarze, ilustratorzy, redaktorzy i użytkownicy.

- **Środowisko wykonawcze agenta**. Framework zapewnia środowisko wykonawcze, umożliwiające komunikację między agentami, zarządzanie ich tożsamościami i cyklami życia oraz egzekwowanie granic bezpieczeństwa i prywatności. Oznacza to, że możesz uruchamiać swoich agentów w bezpiecznym i kontrolowanym środowisku, zapewniając, że mogą one wchodzić w interakcje w sposób bezpieczny i efektywny. Istnieją dwa interesujące środowiska wykonawcze:
  - **Samodzielne środowisko wykonawcze**. To dobry wybór dla aplikacji jednoprzebiegowych, w których wszyscy agenci są zaimplementowani w tym samym języku programowania i działają w tym samym procesie. Oto ilustracja, jak to działa:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Samodzielne środowisko wykonawcze</a>   
Stos aplikacji

    *agenci komunikują się za pomocą wiadomości przez środowisko wykonawcze, a środowisko zarządza cyklem życia agentów*

  - **Rozproszone środowisko wykonawcze agentów**, odpowiednie dla aplikacji wieloprocesowych, w których agenci mogą być zaimplementowani w różnych językach programowania i działać na różnych maszynach. Oto ilustracja, jak to działa:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Rozproszone środowisko wykonawcze</a>

## Semantic Kernel + Framework Agentów

Semantic Kernel to gotowe do zastosowań w przedsiębiorstwach SDK do orkiestracji AI. Składa się z konektorów AI i pamięci oraz Frameworka Agentów.

Najpierw omówmy kilka podstawowych komponentów:

- **Konektory AI**: To interfejsy z zewnętrznymi usługami AI i źródłami danych, dostępne zarówno w Pythonie, jak i C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Tutaj masz prosty przykład, jak można utworzyć kernel i dodać usługę zakończenia czatu. Semantic Kernel tworzy połączenie z zewnętrzną usługą AI, w tym przypadku Azure OpenAI Chat Completion.

- **Wtyczki**: Te kapsułkują funkcje, które aplikacja może wykorzystać. Istnieją zarówno gotowe wtyczki, jak i niestandardowe, które możesz stworzyć. Powiązanym pojęciem są "funkcje podpowiedzi". Zamiast dostarczać wskazówki w języku naturalnym do wywoływania funkcji, transmitujesz pewne funkcje do modelu. Na podstawie bieżącego kontekstu czatu model może wybrać wywołanie jednej z tych funkcji, aby ukończyć żądanie lub zapytanie. Oto przykład:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Tutaj najpierw masz szablon podpowiedzi `skPrompt`, który pozostawia miejsce na dane wejściowe użytkownika, `$userInput`.
Te fakty są następnie przechowywane w kolekcji pamięci `SummarizedAzureDocs`. To bardzo uproszczony przykład, ale pokazuje, jak można przechowywać informacje w pamięci, aby LLM mógł z nich korzystać.

To są podstawy frameworka Semantic Kernel, a co z Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service to nowszy dodatek, wprowadzony na Microsoft Ignite 2024. Umożliwia rozwój i wdrażanie agentów AI z bardziej elastycznymi modelami, takimi jak bezpośrednie wywoływanie otwartych modeli LLM, takich jak Llama 3, Mistral i Cohere.

Azure AI Agent Service oferuje silniejsze mechanizmy bezpieczeństwa dla przedsiębiorstw oraz metody przechowywania danych, co czyni go odpowiednim dla aplikacji korporacyjnych.

Działa od razu z frameworkami do orkiestracji wieloagentowej, takimi jak AutoGen i Semantic Kernel.

Usługa jest obecnie w Public Preview i wspiera Python oraz C# do tworzenia agentów.

Korzystając z Semantic Kernel Python, możemy stworzyć agenta Azure AI z własnym pluginem:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Podstawowe pojęcia

Azure AI Agent Service opiera się na następujących podstawowych pojęciach:

- **Agent**. Azure AI Agent Service integruje się z Azure AI Foundry. W ramach AI Foundry, agent AI działa jako "inteligentna" mikrousługa, która może odpowiadać na pytania (RAG), wykonywać działania lub całkowicie automatyzować przepływy pracy. Osiąga to, łącząc moc generatywnych modeli AI z narzędziami umożliwiającymi dostęp do rzeczywistych źródeł danych i interakcję z nimi. Oto przykład agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    W tym przykładzie agent został stworzony z modelem `gpt-4o-mini`, nazwą `my-agent` i instrukcjami `You are helpful agent`. Agent jest wyposażony w narzędzia i zasoby do wykonywania zadań interpretacji kodu.

- **Wątek i wiadomości**. Wątek to kolejne ważne pojęcie. Reprezentuje rozmowę lub interakcję między agentem a użytkownikiem. Wątki mogą być używane do śledzenia postępu rozmowy, przechowywania informacji o kontekście i zarządzania stanem interakcji. Oto przykład wątku:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    W poprzednim kodzie utworzono wątek. Następnie wysłano wiadomość do wątku. Wywołując `create_and_process_run`, agent został poproszony o wykonanie pracy na wątku. Na koniec wiadomości zostały pobrane i zapisane, aby zobaczyć odpowiedź agenta. Wiadomości wskazują na postęp rozmowy między użytkownikiem a agentem. Ważne jest również zrozumienie, że wiadomości mogą mieć różne typy, takie jak tekst, obraz lub plik, co oznacza, że praca agenta mogła skutkować na przykład obrazem lub odpowiedzią tekstową. Jako programista możesz następnie wykorzystać te informacje do dalszego przetwarzania odpowiedzi lub przedstawienia jej użytkownikowi.

- **Integracja z innymi frameworkami AI**. Usługa Azure AI Agent może współpracować z innymi frameworkami, takimi jak AutoGen i Semantic Kernel, co oznacza, że możesz zbudować część swojej aplikacji w jednym z tych frameworków, na przykład używając Agent Service jako orkiestratora, lub możesz zbudować wszystko w Agent Service.

**Zastosowania**: Azure AI Agent Service jest przeznaczony dla aplikacji korporacyjnych wymagających bezpiecznego, skalowalnego i elastycznego wdrażania agentów AI.

## Jaka jest różnica między tymi frameworkami?

Wydaje się, że istnieje wiele podobieństw między tymi frameworkami, ale są pewne kluczowe różnice w ich projektowaniu, możliwościach i docelowych zastosowaniach:

- **AutoGen**: To framework eksperymentalny skoncentrowany na najnowszych badaniach nad systemami wieloagentowymi. Jest najlepszym miejscem do eksperymentowania i prototypowania zaawansowanych systemów wieloagentowych.
- **Semantic Kernel**: To gotowa do produkcji biblioteka agentów do budowy aplikacji korporacyjnych. Skupia się na aplikacjach agentowych opartych na zdarzeniach, rozproszonych, umożliwiając wykorzystanie wielu LLM i SLM, narzędzi oraz wzorców projektowych dla pojedynczych/wieloagentowych systemów.
- **Azure AI Agent Service**: To platforma i usługa wdrożeniowa w Azure Foundry dla agentów. Oferuje budowanie połączeń z usługami wspieranymi przez Azure, takimi jak Azure OpenAI, Azure AI Search, Bing Search i wykonywanie kodu.

Wciąż nie wiesz, który wybrać?

### Zastosowania

Spróbujmy pomóc, przechodząc przez kilka typowych scenariuszy:

> P: Eksperymentuję, uczę się i buduję aplikacje agentowe jako proof-of-concept, chcę szybko budować i eksperymentować
>

> O: AutoGen byłby dobrym wyborem w tym scenariuszu, ponieważ koncentruje się na aplikacjach agentowych opartych na zdarzeniach i wspiera zaawansowane wzorce projektowe dla systemów wieloagentowych.

> P: Co sprawia, że AutoGen jest lepszym wyborem niż Semantic Kernel i Azure AI Agent Service w tym przypadku?
>
> O: AutoGen jest specjalnie zaprojektowany do aplikacji agentowych opartych na zdarzeniach, co czyni go dobrze dostosowanym do automatyzacji zadań generowania kodu i analizy danych. Zapewnia niezbędne narzędzia i możliwości do efektywnego budowania złożonych systemów wieloagentowych.

> P: Wygląda na to, że Azure AI Agent Service też by tu pasował, ma narzędzia do generowania kodu i więcej?
>
> O: Tak, Azure AI Agent Service to platforma dla agentów z wbudowanymi możliwościami dla wielu modeli, Azure AI Search, Bing Search i Azure Functions. Ułatwia budowanie agentów w Foundry Portal i ich wdrażanie na dużą skalę.

> P: Wciąż jestem zdezorientowany, po prostu podaj mi jedną opcję
>
> O: Świetnym wyborem jest najpierw zbudowanie aplikacji w Semantic Kernel, a następnie użycie Azure AI Agent Service do wdrożenia agenta. Takie podejście pozwala łatwo utrwalić agentów, jednocześnie wykorzystując możliwości budowy systemów wieloagentowych w Semantic Kernel. Dodatkowo Semantic Kernel ma konektor w AutoGen, co ułatwia korzystanie z obu frameworków razem.

Podsumujmy kluczowe różnice w tabeli:

| Framework | Skupienie | Podstawowe pojęcia | Zastosowania |
| --- | --- | --- | --- |
| AutoGen | Aplikacje agentowe oparte na zdarzeniach, rozproszone | Agenci, Persony, Funkcje, Dane | Generowanie kodu, zadania analizy danych |
| Semantic Kernel | Rozumienie i generowanie tekstu podobnego do ludzkiego | Agenci, Modułowe komponenty, Współpraca | Rozumienie języka naturalnego, generowanie treści |
| Azure AI Agent Service | Elastyczne modele, bezpieczeństwo korporacyjne, Generowanie kodu, Wywoływanie narzędzi | Modularność, Współpraca, Orkiestracja procesów | Bezpieczne, skalowalne i elastyczne wdrażanie agentów AI |

Jakie są idealne zastosowania dla każdego z tych frameworków?

## Czy mogę bezpośrednio zintegrować moje istniejące narzędzia ekosystemu Azure, czy potrzebuję samodzielnych rozwiązań?

Odpowiedź brzmi tak, możesz bezpośrednio zintegrować swoje istniejące narzędzia ekosystemu Azure z Azure AI Agent Service, ponieważ została ona zaprojektowana do bezproblemowej współpracy z innymi usługami Azure. Możesz na przykład zintegrować Bing, Azure AI Search i Azure Functions. Istnieje również głęboka integracja z Azure AI Foundry.

Dla AutoGen i Semantic Kernel również możesz zintegrować się z usługami Azure, ale może być konieczne wywoływanie usług Azure z poziomu kodu. Innym sposobem integracji jest użycie SDK Azure do interakcji z usługami Azure z poziomu agentów. Dodatkowo, jak wspomniano, możesz użyć Azure AI Agent Service jako orkiestratora dla agentów zbudowanych w AutoGen lub Semantic Kernel, co zapewni łatwy dostęp do ekosystemu Azure.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących frameworków agentów AI?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Źródła

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel i AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Korzystanie z Azure AI Agent Service z AutoGen / Semantic Kernel do budowy rozwiązania wieloagentowego</a>

## Poprzednia lekcja

[Wprowadzenie do agentów AI i ich zastosowań](../01-intro-to-ai-agents/README.md)

## Następna lekcja

[Zrozumienie wzorców projektowych agentów](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->