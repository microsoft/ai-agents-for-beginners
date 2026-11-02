[![Eksploracja frameworków agentów AI](../../../translated_images/pl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Eksploracja frameworków agentów AI

Frameworki agentów AI to platformy programowe zaprojektowane w celu uproszczenia tworzenia, wdrażania i zarządzania agentami AI. Frameworki te dostarczają deweloperom gotowe komponenty, abstrakcje i narzędzia, które usprawniają rozwój złożonych systemów AI.

Frameworki te pomagają programistom skupić się na unikalnych aspektach ich aplikacji, oferując ustandaryzowane podejścia do powszechnych wyzwań w rozwoju agentów AI. Zwiększają skalowalność, dostępność i efektywność w budowaniu systemów AI.

## Wprowadzenie 

Ta lekcja obejmie:

- Czym są frameworki agentów AI i co umożliwiają programistom?
- Jak zespoły mogą szybko prototypować, iterować i ulepszać możliwości swoich agentów?
- Jakie są różnice między frameworkami i narzędziami stworzonymi przez Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> oraz <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Czy mogę zintegrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję samodzielnych rozwiązań?
- Czym jest Microsoft Foundry Agent Service i jak może mi pomóc?

## Cele nauki

Celem tej lekcji jest pomoc w zrozumieniu:

- Roli frameworków agentów AI w rozwoju AI.
- Jak wykorzystać frameworki agentów AI do tworzenia inteligentnych agentów.
- Kluczowych możliwości, które oferują frameworki agentów AI.
- Różnic między Microsoft Agent Framework oraz Microsoft Foundry Agent Service.

## Czym są frameworki agentów AI i co umożliwiają programistom?

Tradycyjne frameworki AI mogą pomóc zintegrować AI z aplikacjami i ulepszyć je na następujące sposoby:

- **Personalizacja**: AI może analizować zachowania i preferencje użytkowników, aby dostarczać spersonalizowane rekomendacje, treści i doświadczenia.
Przykład: Serwisy streamingowe takie jak Netflix wykorzystują AI do sugerowania filmów i seriali na podstawie historii oglądania, zwiększając zaangażowanie i satysfakcję użytkowników.
- **Automatyzacja i wydajność**: AI może automatyzować powtarzalne zadania, usprawniać procesy i zwiększać efektywność operacyjną.
Przykład: Aplikacje obsługi klienta wykorzystują chatboty zasilane AI do odpowiadania na typowe zapytania, skracając czas reakcji i odciążając pracowników w bardziej skomplikowanych sprawach.
- **Ulepszone doświadczenie użytkownika**: AI może poprawić ogólne doświadczenie użytkownika, oferując inteligentne funkcje, takie jak rozpoznawanie głosu, przetwarzanie języka naturalnego i podpowiedzi tekstowe.
Przykład: Wirtualni asystenci, tacy jak Siri czy Google Assistant, używają AI do rozumienia i reagowania na polecenia głosowe, ułatwiając interakcję użytkowników z urządzeniami.

### To brzmi świetnie, prawda? To dlaczego potrzebujemy frameworku agentów AI?

Frameworki agentów AI to coś więcej niż standardowe frameworki AI. Zaprojektowane są, aby umożliwić tworzenie inteligentnych agentów, którzy mogą wchodzić w interakcję z użytkownikami, innymi agentami i środowiskiem, aby realizować określone cele. Agenci ci mogą wykazywać autonomiczne zachowanie, podejmować decyzje i adaptować się do zmieniających się warunków. Spójrzmy na niektóre kluczowe możliwości, które oferują frameworki agentów AI:

- **Współpraca i koordynacja agentów**: Umożliwiają tworzenie wielu agentów AI, którzy mogą ze sobą współpracować, komunikować się i koordynować działania, aby rozwiązywać złożone zadania.
- **Automatyzacja i zarządzanie zadaniami**: Dostarczają mechanizmy automatyzacji wieloetapowych procesów, delegowania zadań i dynamicznego zarządzania zadaniami między agentami.
- **Zrozumienie kontekstu i adaptacja**: Wyposażają agentów w zdolność rozumienia kontekstu, dostosowywania się do zmieniającego się otoczenia oraz podejmowania decyzji na podstawie informacji w czasie rzeczywistym.

Podsumowując, agenci pozwalają zrobić więcej, podnieść automatyzację na wyższy poziom oraz tworzyć inteligentniejsze systemy, które mogą się uczyć i dostosowywać do środowiska.

## Jak szybko prototypować, iterować i ulepszać możliwości agenta?

To dynamiczne środowisko, ale istnieją pewne cechy wspólne w większości frameworków agentów AI, które pomagają szybko prototypować i iterować, mianowicie: składniki modułowe, narzędzia współpracy i uczenie się w czasie rzeczywistym. Przyjrzyjmy się im bliżej:

- **Używaj komponentów modułowych**: SDK AI oferują gotowe komponenty, takie jak konektory AI i pamięci, wywoływanie funkcji za pomocą języka naturalnego lub wtyczek kodu, szablony podpowiedzi i inne.
- **Wykorzystaj narzędzia współpracy**: Projektuj agentów z określonymi rolami i zadaniami, umożliwiając im testowanie i udoskonalanie procesów współpracy.
- **Ucz się w czasie rzeczywistym**: Implementuj pętle sprzężenia zwrotnego, w których agenci uczą się z interakcji i dynamicznie dostosowują swoje zachowanie.

### Używaj komponentów modułowych

SDK, takie jak Microsoft Agent Framework, oferują gotowe komponenty, jak konektory AI, definicje narzędzi i zarządzanie agentami.

**Jak zespoły mogą to wykorzystać**: Zespoły mogą szybko zestawić te komponenty, aby stworzyć funkcjonalny prototyp bez konieczności zaczynania od zera, co pozwala na szybkie eksperymenty i iteracje.

**Jak to działa w praktyce**: Możesz użyć gotowego parsera do wydobycia informacji z danych wejściowych użytkownika, modułu pamięci do zapisywania i pobierania danych oraz generatora podpowiedzi do interakcji z użytkownikami, wszystko bez konieczności budowania tych komponentów od podstaw.

**Przykład kodu**. Spójrzmy na przykład użycia Microsoft Agent Framework z `FoundryChatClient`, aby model odpowiadał na dane wejściowe użytkownika z wywoływaniem narzędzi:

``` python
# Przykład użycia Microsoft Agent Framework w Pythonie

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Zdefiniuj przykładową funkcję narzędzia do rezerwacji podróży
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
    # Przykładowy wynik: Twój lot do Nowego Jorku w dniu 1 stycznia 2025 został pomyślnie zarezerwowany. Bezpiecznej podróży! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

W tym przykładzie widać, jak można wykorzystać gotowy parser do wydobycia kluczowych informacji z danych użytkownika, takich jak miejsce startu, cel i data rezerwacji lotu. Podejście modułowe pozwala skoncentrować się na logice wysokiego poziomu.

### Wykorzystaj narzędzia współpracy

Frameworki takie jak Microsoft Agent Framework umożliwiają tworzenie wielu agentów, którzy mogą ze sobą współpracować.

**Jak zespoły mogą to wykorzystać**: Zespoły mogą projektować agentów z określonymi rolami i zadaniami, co pozwala testować i udoskonalać procesy współpracy oraz zwiększać efektywność systemu.

**Jak to działa w praktyce**: Można stworzyć zespół agentów, z których każdy ma specjalistyczną funkcję, np. pobieranie danych, analizę czy podejmowanie decyzji. Agenci komunikują się i wymieniają informacje, aby osiągnąć wspólny cel, np. odpowiedzieć na zapytanie użytkownika lub wykonać zadanie.

**Przykład kodu (Microsoft Agent Framework)**:

```python
# Tworzenie wielu agentów współpracujących za pomocą Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent pobierania danych
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent analizy danych
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Uruchamianie agentów kolejno na zadaniu
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

W powyższym kodzie widać, jak stworzyć zadanie obejmujące współpracę wielu agentów do analizy danych. Każdy agent wykonuje określoną funkcję, a zadanie jest realizowane poprzez koordynację pracy agentów, aby osiągnąć zamierzony wynik. Tworząc dedykowanych agentów o specjalistycznych rolach, można poprawić wydajność i efektywność wykonywania zadań.

### Ucz się w czasie rzeczywistym

Zaawansowane frameworki oferują funkcje rozumienia kontekstu i adaptacji w czasie rzeczywistym.

**Jak zespoły mogą to wykorzystać**: Zespoły mogą implementować pętle sprzężenia zwrotnego, gdzie agenci uczą się z interakcji i dynamicznie dostosowują swoje zachowanie, co prowadzi do ciągłego doskonalenia i ulepszania możliwości.

**Jak to działa w praktyce**: Agenci analizują opinie użytkowników, dane środowiskowe oraz wyniki zadań, aby aktualizować swoją bazę wiedzy, dostosowywać algorytmy podejmowania decyzji i podnosić wydajność z czasem. Ten iteracyjny proces uczenia pozwala agentom adaptować się do zmieniających się warunków oraz preferencji użytkowników, zwiększając skuteczność systemu.

## Jakie są różnice między Microsoft Agent Framework a Microsoft Foundry Agent Service?

Istnieje wiele aspektów do porównania tych rozwiązań, ale spójrzmy na kluczowe różnice pod względem konstrukcji, możliwości i docelowych zastosowań:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework to uproszczone SDK do tworzenia agentów AI za pomocą `FoundryChatClient`. Umożliwia programistom tworzenie agentów wykorzystujących modele Azure OpenAI z wbudowanym wywoływaniem narzędzi, zarządzaniem rozmową oraz bezpieczeństwem klasy korporacyjnej dzięki tożsamości Azure.

**Zastosowania**: Budowanie produkcyjnych agentów AI z obsługą narzędzi, procesów wieloetapowych i integracji korporacyjnych.

Oto kilka ważnych podstawowych koncepcji Microsoft Agent Framework:

- **Agenci**. Agent jest tworzony przez `FoundryChatClient` i konfigurowany nazwą, instrukcjami i narzędziami. Agent może:
  - **Przetwarzać wiadomości użytkownika** i generować odpowiedzi wykorzystując modele Azure OpenAI.
  - **Wywoływać narzędzia** automatycznie na podstawie kontekstu rozmowy.
  - **Utrzymywać stan rozmowy** podczas wielu interakcji.

  Oto fragment kodu pokazujący, jak utworzyć agenta:

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

- **Narzędzia**. Framework wspiera definiowanie narzędzi jako funkcji Pythona, które agent może wywoływać automatycznie. Narzędzia rejestruje się podczas tworzenia agenta:

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

- **Koordynacja wielu agentów**. Możesz tworzyć wielu agentów o różnych specjalizacjach i koordynować ich pracę:

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

- **Integracja tożsamości Azure**. Framework korzysta z `AzureCliCredential` (lub `DefaultAzureCredential`) do bezpiecznej, bezkluczowej autoryzacji, eliminując konieczność zarządzania kluczami API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service to nowsze rozwiązanie, przedstawione na Microsoft Ignite 2024. Umożliwia rozwój i wdrażanie agentów AI z większą elastycznością modeli, np. bezpośrednie wywoływanie otwartoźródłowych LLM, takich jak Llama 3, Mistral czy Cohere.

Microsoft Foundry Agent Service oferuje silniejsze mechanizmy bezpieczeństwa korporacyjnego i metody przechowywania danych, co czyni go odpowiednim dla zastosowań korporacyjnych.

Świetnie współpracuje z Microsoft Agent Framework w zakresie tworzenia i wdrażania agentów.

Usługa jest obecnie w Public Preview i wspiera Pythona oraz C# do tworzenia agentów.

Korzystając z Python SDK Microsoft Foundry Agent Service, możemy stworzyć agenta z narzędziem zdefiniowanym przez użytkownika:

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

### Podstawowe koncepcje

Microsoft Foundry Agent Service ma następujące podstawowe koncepcje:

- **Agent**. Microsoft Foundry Agent Service integruje się z Microsoft Foundry. W ramach Microsoft Foundry agent AI działa jako "inteligentny" mikrousługa, która może odpowiadać na pytania (RAG), wykonywać akcje lub całkowicie automatyzować przepływy pracy. Osiąga to przez łączenie generatywnych modeli AI z narzędziami umożliwiającymi dostęp i interakcję z rzeczywistymi źródłami danych. Oto przykład agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    W tym przykładzie agent jest tworzony z modelem `gpt-5-mini`, nazwą `my-agent` i instrukcjami `Jesteś pomocnym agentem`. Agent jest wyposażony w narzędzia i zasoby do zadań interpretacji kodu.

- **Wątki i wiadomości**. Wątek to kolejna ważna koncepcja. Reprezentuje rozmowę lub interakcję między agentem a użytkownikiem. Wątki mogą służyć do śledzenia postępu rozmowy, przechowywania informacji kontekstowych i zarządzania stanem interakcji. Oto przykład wątku:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Poproś agenta o wykonanie pracy na wątku
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Pobierz i zapisz wszystkie wiadomości, aby zobaczyć odpowiedź agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    W powyższym kodzie tworzony jest wątek. Następnie wysyłana jest wiadomość do wątku. Poprzez wywołanie `create_and_process_run` agent zostaje poproszony o wykonanie pracy na wątku. Ostatecznie pobierane są wiadomości i logowane, aby zobaczyć odpowiedź agenta. Wiadomości wskazują na postęp rozmowy między użytkownikiem a agentem. Ważne jest również zrozumienie, że wiadomości mogą być różnego typu, jak tekst, obraz czy plik – to znaczy, że praca agenta mogła skutkować na przykład obrazem lub odpowiedzią tekstową. Jako deweloper możesz wykorzystać te informacje do dalszego przetwarzania odpowiedzi lub przedstawienia jej użytkownikowi.

- **Integracja z Microsoft Agent Framework**. Microsoft Foundry Agent Service działa bezproblemowo z Microsoft Agent Framework, co oznacza, że można budować agentów za pomocą `FoundryChatClient` i wdrażać ich przez Agent Service w scenariuszach produkcyjnych.

**Zastosowania**: Microsoft Foundry Agent Service jest przeznaczony dla aplikacji korporacyjnych wymagających bezpiecznego, skalowalnego i elastycznego wdrażania agentów AI.

## Jaka jest różnica między tymi podejściami?
 
Rzeczywiście istnieją nakładające się cechy, ale są kluczowe różnice pod względem konstrukcji, możliwości i zastosowań:
 
- **Microsoft Agent Framework (MAF)**: Produkcyjne SDK do budowy agentów AI. Zapewnia uproszczone API do tworzenia agentów z wywoływaniem narzędzi, zarządzaniem rozmową i integracją tożsamości Azure.
- **Microsoft Foundry Agent Service**: Platforma i usługa wdrożeniowa w Microsoft Foundry dla agentów. Oferuje wbudowaną łączność z usługami takimi jak Azure OpenAI, Azure AI Search, Bing Search oraz wykonanie kodu.
 
Nadal nie jesteś pewien, co wybrać?

### Zastosowania
 
Sprawdźmy, czy możemy pomóc, przechodząc przez kilka typowych zastosowań:
 
> P: Buduję produkcyjne aplikacje agentów AI i chcę zacząć szybko
>

>O: Microsoft Agent Framework to świetny wybór. Zapewnia proste, Pythoniczne API przez `FoundryChatClient`, które pozwala definiować agentów z narzędziami i instrukcjami w zaledwie kilku linijkach kodu.

>P: Potrzebuję wdrożenia klasy korporacyjnej z integracjami Azure, takimi jak Search i wykonanie kodu
>
> O: Microsoft Foundry Agent Service jest najlepszym rozwiązaniem. To platforma oferująca wbudowane funkcje dla wielu modeli, Azure AI Search, Bing Search i Azure Functions. Umożliwia łatwe tworzenie agentów w Foundry Portal i ich wdrażanie na dużą skalę.
 
> P: Nadal jestem zagubiony, podaj mi jedną opcję
>
> O: Zacznij od Microsoft Agent Framework do budowy agentów, a następnie użyj Microsoft Foundry Agent Service, gdy będziesz potrzebować wdrożenia i skalowania w produkcji. Takie podejście pozwala szybko iterować nad logiką agenta, mając jednocześnie jasno określoną ścieżkę do wdrożenia korporacyjnego.
 
Podsumujmy kluczowe różnice w tabeli:

| Framework | Fokus | Podstawowe koncepcje | Zastosowania |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Uproszczone SDK dla agentów z wywoływaniem narzędzi | Agenci, Narzędzia, Tożsamość Azure | Budowa agentów AI, użycie narzędzi, procesy wieloetapowe |
| Microsoft Foundry Agent Service | Elastyczne modele, bezpieczeństwo korporacyjne, generowanie kodu, wywoływanie narzędzi | Modułowość, współpraca, orkiestracja procesów | Bezpieczne, skalowalne i elastyczne wdrażanie agentów AI |

## Czy mogę zintegrować moje istniejące narzędzia ekosystemu Azure bezpośrednio, czy potrzebuję samodzielnych rozwiązań?


Odpowiedź brzmi tak, możesz zintegrować swoje istniejące narzędzia ekosystemu Azure bezpośrednio z usługą Microsoft Foundry Agent Service, zwłaszcza że została ona zaprojektowana tak, aby współpracować bezproblemowo z innymi usługami Azure. Możesz na przykład zintegrować Bing, Azure AI Search oraz Azure Functions. Istnieje także głęboka integracja z Microsoft Foundry.

Microsoft Agent Framework również integruje się z usługami Azure za pośrednictwem `FoundryChatClient` i tożsamości Azure, co pozwala wywoływać usługi Azure bezpośrednio z narzędzi Twojego agenta.

## Przykładowe Kody

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących AI Agent Frameworks?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Twoich agentów AI.

## Źródła

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Poprzednia Lekcja

[Wprowadzenie do agentów AI i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

## Następna Lekcja

[Zrozumienie wzorców projektowych Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->