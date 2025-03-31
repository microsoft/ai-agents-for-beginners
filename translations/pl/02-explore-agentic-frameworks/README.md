<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T09:17:42+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "pl"
}
-->
[![Eksploracja frameworków agentów AI](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.pl.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo do tej lekcji)_

# Eksploracja frameworków agentów AI

Frameworki agentów AI to platformy programistyczne zaprojektowane w celu uproszczenia tworzenia, wdrażania i zarządzania agentami AI. Te frameworki dostarczają programistom gotowe komponenty, abstrakcje i narzędzia, które ułatwiają rozwój zaawansowanych systemów AI.

Frameworki te pomagają programistom skupić się na unikalnych aspektach ich aplikacji, zapewniając ustandaryzowane podejścia do wspólnych wyzwań w rozwoju agentów AI. Zwiększają skalowalność, dostępność i efektywność w budowaniu systemów AI.

## Wprowadzenie 

Ta lekcja obejmie:

- Czym są frameworki agentów AI i co pozwalają osiągnąć programistom?
- Jak zespoły mogą ich używać do szybkiego prototypowania, iteracji i poprawy możliwości swoich agentów?
- Jakie są różnice między frameworkami i narzędziami stworzonymi przez Microsoft?

## Czy mogę zintegrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję samodzielnych rozwiązań?
- Czym jest usługa Azure AI Agents i jak może mi pomóc?

## Cele nauki

Cele tej lekcji to pomoc w zrozumieniu:

- Roli frameworków agentów AI w rozwoju AI.
- Jak wykorzystać frameworki agentów AI do budowy inteligentnych agentów.
- Kluczowych możliwości oferowanych przez frameworki agentów AI.
- Różnic między AutoGen, Semantic Kernel i Azure AI Agent Service.

## Czym są frameworki agentów AI i co pozwalają osiągnąć programistom?

Tradycyjne frameworki AI mogą pomóc w integracji AI z aplikacjami i poprawić ich funkcjonalność w następujący sposób:

- **Personalizacja**: AI może analizować zachowanie użytkownika i preferencje, aby dostarczać spersonalizowane rekomendacje, treści i doświadczenia.
Przykład: Usługi streamingowe, takie jak Netflix, używają AI do sugerowania filmów i programów na podstawie historii oglądania, zwiększając zaangażowanie i satysfakcję użytkownika.
- **Automatyzacja i efektywność**: AI może automatyzować powtarzalne zadania, usprawniać przepływy pracy i poprawiać efektywność operacyjną.
Przykład: Aplikacje obsługi klienta wykorzystują chatboty zasilane AI do obsługi typowych zapytań, skracając czas odpowiedzi i uwalniając ludzkich agentów do bardziej złożonych problemów.
- **Ulepszona interakcja z użytkownikiem**: AI może poprawić ogólne doświadczenie użytkownika, oferując inteligentne funkcje, takie jak rozpoznawanie głosu, przetwarzanie języka naturalnego i przewidywanie tekstu.
Przykład: Wirtualni asystenci, tacy jak Siri i Google Assistant, wykorzystują AI do rozumienia i reagowania na polecenia głosowe, ułatwiając użytkownikom interakcję z urządzeniami.

### Brzmi świetnie, prawda? Więc dlaczego potrzebujemy frameworku agentów AI?

Frameworki agentów AI to coś więcej niż tylko frameworki AI. Są zaprojektowane do tworzenia inteligentnych agentów, którzy mogą wchodzić w interakcje z użytkownikami, innymi agentami i środowiskiem, aby osiągać określone cele. Ci agenci mogą wykazywać autonomiczne zachowanie, podejmować decyzje i dostosowywać się do zmieniających się warunków. Oto kilka kluczowych możliwości oferowanych przez frameworki agentów AI:

- **Współpraca i koordynacja agentów**: Umożliwiają tworzenie wielu agentów AI, którzy mogą współpracować, komunikować się i koordynować działania w celu rozwiązania złożonych zadań.
- **Automatyzacja i zarządzanie zadaniami**: Zapewniają mechanizmy automatyzacji wieloetapowych przepływów pracy, delegowania zadań i dynamicznego zarządzania zadaniami wśród agentów.
- **Zrozumienie kontekstu i adaptacja**: Wyposażają agentów w zdolność rozumienia kontekstu, dostosowywania się do zmieniającego się środowiska i podejmowania decyzji na podstawie informacji w czasie rzeczywistym.

Podsumowując, agenci pozwalają zrobić więcej, wynieść automatyzację na wyższy poziom, tworzyć bardziej inteligentne systemy, które mogą dostosowywać się i uczyć się ze swojego środowiska.

## Jak szybko prototypować, iterować i poprawiać możliwości agentów?

To szybko rozwijający się obszar, ale istnieją pewne wspólne cechy w większości frameworków agentów AI, które mogą pomóc w szybkim prototypowaniu i iteracji, mianowicie modułowe komponenty, narzędzia współpracy i uczenie w czasie rzeczywistym. Przyjrzyjmy się im:

- **Używaj modułowych komponentów**: SDK AI oferują gotowe komponenty, takie jak łączniki AI i pamięci, wywoływanie funkcji za pomocą języka naturalnego lub wtyczek kodu, szablony podpowiedzi i więcej.
- **Wykorzystaj narzędzia współpracy**: Projektuj agentów z określonymi rolami i zadaniami, umożliwiając testowanie i doskonalenie współpracy.
- **Ucz się w czasie rzeczywistym**: Wdrażaj pętle sprzężenia zwrotnego, w których agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie.

### Używaj modułowych komponentów

SDK, takie jak Microsoft Semantic Kernel i LangChain, oferują gotowe komponenty, takie jak łączniki AI, szablony podpowiedzi i zarządzanie pamięcią.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą szybko złożyć te komponenty, aby stworzyć funkcjonalny prototyp bez konieczności zaczynania od zera, co pozwala na szybkie eksperymentowanie i iterację.

**Jak to działa w praktyce**: Możesz użyć gotowego parsera do wyodrębnienia informacji z danych wejściowych użytkownika, modułu pamięci do przechowywania i pobierania danych oraz generatora podpowiedzi do interakcji z użytkownikami, wszystko bez konieczności budowania tych komponentów od podstaw.

**Przykładowy kod**. Oto przykłady, jak można użyć gotowego łącznika AI z Semantic Kernel Python i .Net, który wykorzystuje automatyczne wywoływanie funkcji, aby model odpowiadał na dane wejściowe użytkownika:

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

Jak widać z tego przykładu, można wykorzystać gotowy parser do wyodrębnienia kluczowych informacji z danych wejściowych użytkownika, takich jak miejsce początkowe, miejsce docelowe i data rezerwacji lotu. Podejście modułowe pozwala skupić się na logice wyższego poziomu.

### Wykorzystaj narzędzia współpracy

Frameworki, takie jak CrewAI, Microsoft AutoGen i Semantic Kernel, ułatwiają tworzenie wielu agentów, którzy mogą współpracować.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą projektować agentów z określonymi rolami i zadaniami, umożliwiając testowanie i doskonalenie współpracy oraz poprawę ogólnej efektywności systemu.

**Jak to działa w praktyce**: Możesz stworzyć zespół agentów, w którym każdy agent ma wyspecjalizowaną funkcję, taką jak pobieranie danych, analiza czy podejmowanie decyzji. Ci agenci mogą komunikować się i dzielić informacjami, aby osiągnąć wspólny cel, taki jak odpowiedź na zapytanie użytkownika lub wykonanie zadania.

**Przykładowy kod (AutoGen)**:

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

W poprzednim kodzie pokazano, jak można stworzyć zadanie, które obejmuje współpracę wielu agentów analizujących dane. Każdy agent wykonuje określoną funkcję, a zadanie jest realizowane poprzez koordynację agentów w celu osiągnięcia zamierzonego rezultatu. Tworząc dedykowanych agentów o wyspecjalizowanych rolach, można poprawić efektywność i wydajność zadań.

### Ucz się w czasie rzeczywistym

Zaawansowane frameworki oferują możliwości rozumienia kontekstu w czasie rzeczywistym i adaptacji.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą wdrażać pętle sprzężenia zwrotnego, w których agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie, prowadząc do ciągłego doskonalenia i udoskonalania możliwości.

**Jak to działa w praktyce**: Agenci mogą analizować opinie użytkowników, dane środowiskowe i wyniki zadań, aby aktualizować swoją bazę wiedzy, dostosowywać algorytmy podejmowania decyzji i poprawiać wydajność w czasie. Ten iteracyjny proces uczenia się pozwala agentom dostosowywać się do zmieniających się warunków i preferencji użytkowników, zwiększając ogólną efektywność systemu.

## Jakie są różnice między frameworkami AutoGen, Semantic Kernel i Azure AI Agent Service?

Istnieje wiele sposobów porównania tych frameworków, ale przyjrzyjmy się kilku kluczowym różnicom w ich konstrukcji, możliwościach i docelowych przypadkach użycia:

## AutoGen

AutoGen to otwartoźródłowy framework opracowany przez Microsoft Research's AI Frontiers Lab. Skupia się na aplikacjach opartych na zdarzeniach, rozproszonych i agentowych, umożliwiając współpracę wielu LLM, SLM, narzędzi oraz zaawansowane wzorce projektowe dla wielu agentów.

AutoGen opiera się na podstawowej koncepcji agentów, które są autonomicznymi jednostkami zdolnymi do percepcji środowiska, podejmowania decyzji i działania w celu osiągnięcia określonych celów. Agenci komunikują się za pomocą asynchronicznych wiadomości, co pozwala im działać niezależnie i równolegle, zwiększając skalowalność i responsywność systemu.
Modularność, Współpraca, Orkiestracja Procesów | Bezpieczne, skalowalne i elastyczne wdrażanie agentów AI | Jaki jest idealny przypadek użycia dla każdego z tych frameworków?

## Czy mogę bezpośrednio zintegrować moje istniejące narzędzia ekosystemu Azure, czy potrzebuję niezależnych rozwiązań?

Odpowiedź brzmi tak, możesz bezpośrednio zintegrować swoje istniejące narzędzia ekosystemu Azure z Azure AI Agent Service, szczególnie dlatego, że został on zaprojektowany, aby działać płynnie z innymi usługami Azure. Na przykład możesz zintegrować Bing, Azure AI Search i Azure Functions. Istnieje również głęboka integracja z Azure AI Foundry.

Dla AutoGen i Semantic Kernel również możesz integrować się z usługami Azure, ale może to wymagać wywoływania tych usług bezpośrednio z twojego kodu. Innym sposobem integracji jest użycie SDK Azure do interakcji z usługami Azure z poziomu twoich agentów. Dodatkowo, jak wspomniano, możesz używać Azure AI Agent Service jako orkiestratora dla agentów zbudowanych w AutoGen lub Semantic Kernel, co umożliwi łatwy dostęp do ekosystemu Azure.

## Źródła

---

## Poprzednia lekcja

[Wprowadzenie do agentów AI i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

## Następna lekcja

[Zrozumienie wzorców projektowych agentów](../03-agentic-design-patterns/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.