[![Eksploracja frameworków agentów AI](../../../translated_images/pl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknij obraz powyżej, aby obejrzeć wideo z tej lekcji)_

# Eksploracja frameworków agentów AI

Frameworki agentów AI to platformy programistyczne zaprojektowane w celu uproszczenia tworzenia, wdrażania i zarządzania agentami AI. Frameworki te dostarczają programistom gotowe komponenty, abstrakcje i narzędzia, które usprawniają rozwój złożonych systemów AI.

Frameworki te pomagają programistom skupić się na unikalnych aspektach ich aplikacji, zapewniając ustandaryzowane podejścia do powszechnych wyzwań w tworzeniu agentów AI. Zwiększają skalowalność, dostępność i efektywność budowy systemów AI.

## Wprowadzenie

Ta lekcja obejmie:

- Czym są frameworki agentów AI i co pozwalają osiągnąć programistom?
- Jak zespoły mogą wykorzystać je do szybkiego prototypowania, iteracji i ulepszania możliwości swojego agenta?
- Jakie są różnice między frameworkami i narzędziami stworzonymi przez Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> oraz <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Czy mogę zintegrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję rozwiązań niezależnych?
- Czym jest usługa Azure AI Agents i jak może mi pomóc?

## Cele nauki

Celem tej lekcji jest pomóc Ci zrozumieć:

- Rolę frameworków agentów AI w rozwoju AI.
- Jak wykorzystać frameworki agentów AI do budowy inteligentnych agentów.
- Kluczowe możliwości udostępniane przez frameworki agentów AI.
- Różnice między Microsoft Agent Framework a Azure AI Agent Service.

## Czym są frameworki agentów AI i co pozwalają programistom zrobić?

Tradycyjne frameworki AI mogą pomóc Ci zintegrować AI z Twoimi aplikacjami i uczynić je lepszymi na następujące sposoby:

- **Personalizacja**: AI może analizować zachowania i preferencje użytkowników, aby dostarczać spersonalizowane rekomendacje, treści i doświadczenia.
Przykład: Serwisy streamingowe, takie jak Netflix, używają AI do sugerowania filmów i programów na podstawie historii oglądania, zwiększając zaangażowanie i satysfakcję użytkowników.
- **Automatyzacja i efektywność**: AI może automatyzować powtarzalne zadania, usprawniać przepływy pracy i poprawiać efektywność operacyjną.
Przykład: Aplikacje obsługi klienta używają chatbotów zasilanych AI do obsługi typowych zapytań, skracając czas odpowiedzi i odciążając agentów ludzkich w bardziej złożonych kwestiach.
- **Ulepszone doświadczenie użytkownika**: AI może poprawić całokształt doświadczenia użytkownika, dostarczając inteligentne funkcje takie jak rozpoznawanie głosu, przetwarzanie języka naturalnego oraz tekst predykcyjny.
Przykład: Wirtualni asystenci tacy jak Siri i Google Assistant używają AI do rozumienia i reagowania na polecenia głosowe, ułatwiając interakcję z urządzeniami.

### To wszystko brzmi świetnie, prawda? To po co nam framework agentów AI?

Frameworki agentów AI to coś więcej niż zwykłe frameworki AI. Zostały zaprojektowane, by umożliwić tworzenie inteligentnych agentów, którzy mogą wchodzić w interakcje z użytkownikami, innymi agentami i środowiskiem, by osiągać określone cele. Ci agenci mogą wykazywać autonomiczne zachowania, podejmować decyzje i dostosowywać się do zmieniających się warunków. Spójrzmy na niektóre kluczowe możliwości udostępniane przez frameworki agentów AI:

- **Współpraca i koordynacja agentów**: Umożliwiają tworzenie wielu agentów AI, którzy mogą wspólnie pracować, komunikować się i koordynować, by rozwiązywać złożone zadania.
- **Automatyzacja i zarządzanie zadaniami**: Dostarczają mechanizmy automatyzacji wieloetapowych przepływów pracy, delegowania zadań i dynamicznego zarządzania zadaniami wśród agentów.
- **Rozumienie kontekstu i adaptacja**: Wyposażają agentów w umiejętność rozumienia kontekstu, dostosowywania się do zmieniającego się środowiska oraz podejmowania decyzji na podstawie informacji w czasie rzeczywistym.

Podsumowując, agenci pozwalają robić więcej, podnieść automatyzację na wyższy poziom oraz tworzyć inteligentniejsze systemy, które mogą się uczyć i adaptować w swoim otoczeniu.

## Jak szybko prototypować, iterować i ulepszać możliwości agenta?

To dynamicznie rozwijające się środowisko, ale są pewne elementy wspólne dla większości frameworków agentów AI, które mogą pomóc w szybkim prototypowaniu i iteracji, mianowicie komponenty modułowe, narzędzia współpracy oraz uczenie się w czasie rzeczywistym. Przyjrzyjmy się temu bliżej:

- **Używaj komponentów modułowych**: SDK AI oferują gotowe komponenty takie jak konektory AI i pamięci, wywoływanie funkcji za pomocą języka naturalnego lub wtyczek kodu, szablony promptów i inne.
- **Wykorzystuj narzędzia współpracy**: Projektuj agentów z określonymi rolami i zadaniami, umożliwiając testowanie i udoskonalanie współpracy w przepływach pracy.
- **Ucz się w czasie rzeczywistym**: Wdrażaj pętle zwrotne, gdzie agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie.

### Używaj komponentów modułowych

SDK takie jak Microsoft Agent Framework oferują gotowe komponenty, takie jak konektory AI, definicje narzędzi i zarządzanie agentem.

**Jak zespoły mogą tego używać**: Zespoły mogą szybko zestawiać te komponenty, by stworzyć funkcjonalny prototyp bez rozpoczynania od zera, co umożliwia szybkie eksperymenty i iteracje.

**Jak to działa w praktyce**: Możesz użyć gotowego parsera do wyodrębniania informacji z wejścia użytkownika, modułu pamięci do przechowywania i pobierania danych oraz generatora promptów do interakcji z użytkownikami, wszystko bez konieczności budowania tych komponentów od podstaw.

**Przykładowy kod**. Spójrzmy na przykład użycia Microsoft Agent Framework z `AzureAIProjectAgentProvider`, by model odpowiadał na wejście użytkownika z wywoływaniem narzędzi:

``` python
# Przykład Microsoft Agent Framework w Pythonie

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Zdefiniuj przykładową funkcję narzędzia do rezerwacji podróży
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Przykładowe wyjście: Twój lot do Nowego Jorku w dniu 1 stycznia 2025 został pomyślnie zarezerwowany. Udanej podróży! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z tego przykładu widać, jak można wykorzystać gotowy parser do wyodrębniania kluczowych informacji z wejścia użytkownika, takich jak miejsce wylotu, miejsce przeznaczenia i data zapytania o rezerwację lotu. Takie modularne podejście pozwala skupić się na logice wysokiego poziomu.

### Wykorzystuj narzędzia współpracy

Frameworki takie jak Microsoft Agent Framework ułatwiają tworzenie wielu agentów, którzy mogą współpracować.

**Jak zespoły mogą tego używać**: Zespoły mogą projektować agentów z określonymi rolami i zadaniami, umożliwiając testowanie i udoskonalanie współpracy w przepływach pracy, co zwiększa efektywność systemu.

**Jak to działa w praktyce**: Możesz stworzyć zespół agentów, z których każdy ma specjalistyczną funkcję, na przykład pobieranie danych, analizę lub podejmowanie decyzji. Agenci ci komunikują się i dzielą informacjami, by osiągnąć wspólny cel, np. odpowiedzieć na zapytanie użytkownika lub wykonać zadanie.

**Przykładowy kod (Microsoft Agent Framework)**:

```python
# Tworzenie wielu agentów współpracujących ze sobą przy użyciu Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent pobierania danych
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent analizy danych
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Uruchamianie agentów sekwencyjnie dla zadania
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Z powyższego kodu wynika, jak można stworzyć zadanie obejmujące współpracę wielu agentów do analizy danych. Każdy agent pełni określoną funkcję, a zadanie jest wykonywane poprzez koordynację agentów, aby osiągnąć pożądany wynik. Tworząc dedykowanych agentów ze specjalistycznymi rolami, można poprawić efektywność i wydajność zadania.

### Ucz się w czasie rzeczywistym

Zaawansowane frameworki oferują możliwości zrozumienia kontekstu i adaptacji w czasie rzeczywistym.

**Jak zespoły mogą tego używać**: Zespoły mogą wdrażać pętle zwrotne, w których agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie, prowadząc do ciągłego ulepszania i udoskonalania możliwości.

**Jak to działa w praktyce**: Agenci mogą analizować opinie użytkowników, dane środowiskowe i wyniki zadań, by aktualizować swoją bazę wiedzy, dostosowywać algorytmy podejmowania decyzji i poprawiać wydajność w czasie. Ten iteracyjny proces uczenia pozwala agentom adaptować się do zmieniających się warunków i preferencji użytkowników, zwiększając skuteczność całego systemu.

## Jakie są różnice między Microsoft Agent Framework a Azure AI Agent Service?

Istnieje wiele sposobów porównania tych podejść, spójrzmy na kluczowe różnice pod względem projektowania, możliwości i docelowych zastosowań:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework dostarcza uproszczone SDK do tworzenia agentów AI za pomocą `AzureAIProjectAgentProvider`. Pozwala programistom tworzyć agentów wykorzystujących modele Azure OpenAI z wbudowanym wywoływaniem narzędzi, zarządzaniem konwersacją i bezpieczeństwem klasy enterprise poprzez identyfikację Azure.

**Zastosowania**: Budowanie gotowych do produkcji agentów AI z wywoływaniem narzędzi, wieloetapowymi przepływami pracy i scenariuszami integracji enterprise.

Oto ważne podstawowe pojęcia Microsoft Agent Framework:

- **Agenci**. Agent jest tworzony za pomocą `AzureAIProjectAgentProvider` i konfigurowany z nazwą, instrukcjami oraz narzędziami. Agent może:
  - **Przetwarzać wiadomości użytkownika** i generować odpowiedzi z użyciem modeli Azure OpenAI.
  - **Automatycznie wywoływać narzędzia** zgodnie z kontekstem rozmowy.
  - **Utrzymywać stan konwersacji** przez wiele interakcji.

  Oto fragment kodu pokazujący, jak stworzyć agenta:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Narzędzia**. Framework pozwala definiować narzędzia jako funkcje Pythona, które agent może wywoływać automatycznie. Narzędzia są rejestrowane podczas tworzenia agenta:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Wielu agentów i koordynacja**. Można tworzyć wielu agentów o różnych specjalizacjach i koordynować ich pracę:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integracja z Azure Identity**. Framework używa `AzureCliCredential` (lub `DefaultAzureCredential`), zapewniając bezpieczną, bezkluczową autoryzację, eliminując potrzebę zarządzania kluczami API.

## Azure AI Agent Service

Azure AI Agent Service to nowsze rozwiązanie, wprowadzone podczas Microsoft Ignite 2024. Pozwala na rozwój i wdrażanie agentów AI z bardziej elastycznymi modelami, takimi jak bezpośrednie wywoływanie open-source’owych LLM, np. Llama 3, Mistral czy Cohere.

Azure AI Agent Service oferuje silniejsze mechanizmy zabezpieczeń klasy enterprise i metody przechowywania danych, co czyni go odpowiednim dla aplikacji enterprise.

Działa natywnie z Microsoft Agent Framework do budowania i wdrażania agentów.

Usługa jest obecnie w publicznej wersji zapoznawczej (Public Preview) i wspiera Pythona oraz C# do tworzenia agentów.

Korzystając z Python SDK Azure AI Agent Service, możemy stworzyć agenta z narzędziem zdefiniowanym przez użytkownika:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Zdefiniuj funkcje narzędziowe
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

### Podstawowe koncepcje

Azure AI Agent Service zawiera następujące kluczowe pojęcia:

- **Agent**. Usługa integruje się z Microsoft Foundry. W ramach AI Foundry agent AI działa jako „inteligentna” mikrousługa, mogąca odpowiadać na pytania (RAG), wykonywać działania lub całkowicie automatyzować przepływy pracy. Osiąga to przez połączenie mocy generatywnych modeli AI z narzędziami pozwalającymi na dostęp i interakcję z rzeczywistymi źródłami danych. Oto przykład agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    W tym przykładzie agent jest tworzony z modelem `gpt-4o-mini`, nazwą `my-agent` i instrukcją `You are helpful agent`. Agent jest wyposażony w narzędzia i zasoby do wykonywania zadań interpretacji kodu.

- **Wątki i wiadomości**. Wątek to kolejne ważne pojęcie. Reprezentuje rozmowę lub interakcję między agentem a użytkownikiem. Wątki mogą służyć do śledzenia przebiegu konwersacji, przechowywania informacji kontekstowych i zarządzania stanem interakcji. Oto przykład wątku:

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

    W powyższym kodzie tworzony jest wątek, na który później wysyłana jest wiadomość. Poprzez wywołanie `create_and_process_run` agent jest proszony o wykonanie pracy na tym wątku. Na końcu pobierane i logowane są wiadomości, aby zobaczyć odpowiedź agenta. Wiadomości wskazują na postęp rozmowy między użytkownikiem a agentem. Ważne jest też zrozumienie, że wiadomości mogą mieć różne typy, takie jak tekst, obraz czy plik, co oznacza, że praca agenta zaowocowała np. obrazem lub tekstową odpowiedzią. Jako programista możesz wykorzystać te informacje do dalszego przetwarzania odpowiedzi lub jej prezentacji użytkownikowi.

- **Integracja z Microsoft Agent Framework**. Azure AI Agent Service działa bezproblemowo z Microsoft Agent Framework, co oznacza, że możesz budować agentów za pomocą `AzureAIProjectAgentProvider` i wdrażać je przez Agent Service do zastosowań produkcyjnych.

**Zastosowania**: Azure AI Agent Service jest zaprojektowany dla aplikacji enterprise, które wymagają bezpiecznego, skalowalnego i elastycznego wdrożenia agentów AI.

## Jaka jest różnica między tymi podejściami?

Można dostrzec pewne nakładanie się, ale istnieją kluczowe różnice pod względem konstrukcji, możliwości i docelowych zastosowań:

- **Microsoft Agent Framework (MAF)**: To gotowe do produkcji SDK do budowy agentów AI. Dostarcza usprawnione API do tworzenia agentów z wywoływaniem narzędzi, zarządzaniem rozmową oraz integracją z Azure Identity.
- **Azure AI Agent Service**: To platforma i usługa wdrażania w Azure Foundry dla agentów. Oferuje natywne połączenia z usługami takimi jak Azure OpenAI, Azure AI Search, Bing Search i wykonywanie kodu.

Wciąż nie wiesz, który wybrać?

### Przypadki użycia

Spróbujmy pomóc, przechodząc przez popularne przypadki użycia:

> P: Buduję produkcyjne aplikacje agentów AI i chcę zacząć szybko
>

>O: Microsoft Agent Framework to świetny wybór. Oferuje prostą, pythonową API przez `AzureAIProjectAgentProvider`, która pozwala zdefiniować agentów z narzędziami i instrukcjami w kilku linijkach kodu.

> P: Potrzebuję wdrożenia klasy enterprise z integracjami Azure takimi jak Search i wykonywanie kodu
>
> O: Azure AI Agent Service jest najlepszym wyborem. To usługa platformowa z wbudowanymi możliwościami dla wielu modeli, Azure AI Search, Bing Search i Azure Functions. Umożliwia łatwe budowanie agentów w portalu Foundry i wdrażanie ich na dużą skalę.

> P: Wciąż się zastanawiam, podaj mi jedną opcję
>
> O: Zacznij od Microsoft Agent Framework do tworzenia agentów, a potem użyj Azure AI Agent Service, gdy potrzebujesz wdrożyć i skalować ich pracę w produkcji. Takie podejście pozwoli szybko iterować na logice agenta, mając jednocześnie jasną drogę do wdrożenia enterprise.

Podsumujmy kluczowe różnice w tabeli:

| Framework | Skupienie | Podstawowe pojęcia | Zastosowania |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Uproszczone SDK agentów z wywoływaniem narzędzi | Agenci, Narzędzia, Tożsamość Azure | Tworzenie agentów AI, użycie narzędzi, wieloetapowe przepływy pracy |
| Azure AI Agent Service | Elastyczne modele, bezpieczeństwo enterprise, generowanie kodu, wywoływanie narzędzi | Modularność, Współpraca, Orkiestracja procesów | Bezpieczne, skalowalne i elastyczne wdrażanie agentów AI |

## Czy mogę integrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję rozwiązań niezależnych?
Odpowiedź brzmi tak, możesz zintegrować swoje istniejące narzędzia ekosystemu Azure bezpośrednio z usługą Azure AI Agent Service, zwłaszcza że została ona zaprojektowana do bezproblemowej współpracy z innymi usługami Azure. Na przykład możesz zintegrować Bing, Azure AI Search oraz Azure Functions. Istnieje również głęboka integracja z Microsoft Foundry.

Microsoft Agent Framework integruje się również z usługami Azure za pośrednictwem `AzureAIProjectAgentProvider` oraz tożsamości Azure, co pozwala na bezpośrednie wywoływanie usług Azure z narzędzi agenta.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących AI Agent Frameworks?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące AI Agents.

## Referencje

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Poprzednia lekcja

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Następna lekcja

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było prawidłowe, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za ewentualne nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->