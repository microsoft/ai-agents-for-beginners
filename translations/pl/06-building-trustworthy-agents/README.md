[![Godni zaufania agenci AI](../../../translated_images/pl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Tworzenie godnych zaufania agentów AI

## Wprowadzenie

Ta lekcja obejmie:

- Jak tworzyć i wdrażać bezpieczne i skuteczne agentów AI.
- Ważne kwestie bezpieczeństwa podczas tworzenia agentów AI.
- Jak utrzymać prywatność danych i użytkowników podczas tworzenia agentów AI.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

- Identyfikować i łagodzić ryzyka przy tworzeniu agentów AI.
- Wdrażać środki bezpieczeństwa, aby zapewnić właściwe zarządzanie danymi i dostępem.
- Tworzyć agentów AI, którzy zachowują prywatność danych i zapewniają wysoką jakość doświadczenia użytkownika.

## Bezpieczeństwo

Najpierw przyjrzyjmy się tworzeniu bezpiecznych aplikacji agentowych. Bezpieczeństwo oznacza, że agent AI działa zgodnie z zamierzeniem. Jako twórcy aplikacji agentowych mamy metody i narzędzia maksymalizujące bezpieczeństwo:

### Tworzenie ram dla wiadomości systemowej

Jeśli kiedykolwiek tworzyłeś aplikację AI wykorzystującą duże modele językowe (LLMs), wiesz, jak ważne jest zaprojektowanie solidnego systemowego promptu lub wiadomości systemowej. Te prompty ustanawiają meta zasady, instrukcje i wytyczne dotyczące interakcji LLM z użytkownikiem i danymi.

W przypadku agentów AI prompt systemowy jest jeszcze ważniejszy, ponieważ agenci AI będą potrzebować bardzo specyficznych instrukcji, aby wykonywać zaprojektowane dla nich zadania.

Aby tworzyć skalowalne prompt'y systemowe, możemy użyć ram wiadomości systemowej do budowania jednego lub wielu agentów w naszej aplikacji:

![Tworzenie ram wiadomości systemowej](../../../translated_images/pl/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Utwórz meta wiadomość systemową 

Meta prompt będzie używany przez LLM do generowania promptów systemowych dla agentów, których tworzymy. Projektujemy go jako szablon, aby móc efektywnie tworzyć wielu agentów w razie potrzeby.

Oto przykład meta wiadomości systemowej, którą przekazalibyśmy LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Utwórz podstawowy prompt

Następnym krokiem jest stworzenie podstawowego promptu opisującego agenta AI. Powinieneś uwzględnić rolę agenta, zadania, które agent wykona, oraz inne obowiązki agenta.

Oto przykład:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Przekaż podstawową wiadomość systemową do LLM

Teraz możemy zoptymalizować tę wiadomość systemową, dostarczając meta wiadomość systemową jako wiadomość systemową oraz naszą podstawową wiadomość systemową.

To wygeneruje wiadomość systemową lepiej zaprojektowaną do kierowania naszymi agentami AI:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Krok 4: Iteruj i ulepszaj

Wartość tego frameworku wiadomości systemowej polega na ułatwieniu skalowania tworzenia wiadomości systemowych dla wielu agentów, a także na możliwości ulepszania wiadomości systemowych w czasie. Rzadko zdarza się, że wiadomość systemowa zadziała od razu dla całego przypadku użycia. Możliwość wprowadzania drobnych poprawek i ulepszeń poprzez zmianę podstawowej wiadomości systemowej i uruchamianie jej w systemie pozwoli na porównywanie i ocenę wyników.

## Zrozumienie zagrożeń

Aby tworzyć godnych zaufania agentów AI, ważne jest zrozumienie i złagodzenie ryzyk i zagrożeń dla twojego agenta AI. Przyjrzyjmy się niektórym z różnych zagrożeń dla agentów AI i temu, jak lepiej się na nie przygotować.

![Zrozumienie zagrożeń](../../../translated_images/pl/understanding-threats.89edeada8a97fc0f.webp)

### Zadanie i instrukcje

**Opis:** Atakujący próbują zmienić instrukcje lub cele agenta AI poprzez promptowanie lub manipulowanie danymi wejściowymi.

**Złagodzenie**: Wykonuj kontrole walidacji i filtry wejściowe, aby wykrywać potencjalnie niebezpieczne prompt'y zanim zostaną przetworzone przez agenta AI. Ponieważ te ataki na ogół wymagają częstej interakcji z agentem, ograniczenie liczby tur w rozmowie to kolejny sposób zapobiegania tego typu atakom.

### Dostęp do krytycznych systemów

**Opis**: Jeśli agent AI ma dostęp do systemów i usług przechowujących dane wrażliwe, atakujący mogą skompromitować komunikację między agentem a tymi usługami. Mogą to być ataki bezpośrednie lub pośrednie próby uzyskania informacji o tych systemach za pośrednictwem agenta.

**Złagodzenie**: Agenci AI powinni mieć dostęp do systemów wyłącznie na zasadzie konieczności, aby zapobiec tego rodzaju atakom. Komunikacja między agentem a systemem powinna być również zabezpieczona. Wdrożenie mechanizmów uwierzytelniania i kontroli dostępu to kolejny sposób ochrony tych informacji.

### Przeciążenie zasobów i usług

**Opis:** Agenci AI mogą uzyskiwać dostęp do różnych narzędzi i usług, aby wykonywać zadania. Atakujący mogą wykorzystać tę zdolność, aby zaatakować te usługi, wysyłając dużą liczbę żądań przez agenta AI, co może skutkować awariami systemu lub wysokimi kosztami.

**Złagodzenie:** Wdroż polityki ograniczające liczbę żądań, które agent AI może wysyłać do usługi. Ograniczenie liczby tur rozmowy i żądań kierowanych do agenta AI to kolejny sposób zapobiegania tego typu atakom.

### Zatrucie bazy wiedzy

**Opis:** Ten typ ataku nie celuje bezpośrednio w agenta AI, lecz w bazę wiedzy i inne usługi, których agent AI będzie używać. Może to polegać na uszkodzeniu danych lub informacji, których agent AI użyje do wykonania zadania, co doprowadzi do tendencyjnych lub niezamierzonych odpowiedzi dla użytkownika.

**Złagodzenie:** Regularnie weryfikuj dane, których agent AI będzie używać w swoich przepływach pracy. Upewnij się, że dostęp do tych danych jest zabezpieczony i może być zmieniany tylko przez zaufane osoby, aby uniknąć tego typu ataku.

### Błędy kaskadowe

**Opis:** Agenci AI korzystają z różnych narzędzi i usług, aby wykonywać zadania. Błędy spowodowane przez atakujących mogą prowadzić do awarii innych systemów, z którymi agent AI jest połączony, powodując, że atak staje się bardziej rozległy i trudniejszy do zdiagnozowania.

**Złagodzenie**: Jedną z metod uniknięcia tego jest uruchamianie agenta AI w ograniczonym środowisku, na przykład wykonywanie zadań w kontenerze Docker, aby zapobiec bezpośrednim atakom na system. Tworzenie mechanizmów awaryjnych i logiki ponawiania prób, gdy niektóre systemy odpowiadają błędem, to kolejny sposób zapobiegania większym awariom systemu.

## Człowiek w pętli

Innym skutecznym sposobem budowania systemów godnych zaufania opartych na agentach AI jest zastosowanie podejścia 'człowiek w pętli'. Tworzy to przepływ, w którym użytkownicy mogą przekazywać opinię agentom podczas działania. Użytkownicy w zasadzie działają jako agenci w systemie wieloagentowym, udzielając zgody lub przerywając działający proces.

![Człowiek w pętli](../../../translated_images/pl/human-in-the-loop.5f0068a678f62f4f.webp)

Poniżej znajduje się fragment kodu używający Microsoft Agent Framework, pokazujący, jak to pojęcie jest implementowane:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Utwórz dostawcę z zatwierdzeniem przez człowieka
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Utwórz agenta z krokiem zatwierdzenia przez człowieka
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Użytkownik może przejrzeć i zatwierdzić odpowiedź
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Podsumowanie

Tworzenie godnych zaufania agentów AI wymaga starannego projektowania, solidnych środków bezpieczeństwa i ciągłej iteracji. Implementując ustrukturyzowane systemy meta promptów, rozumiejąc potencjalne zagrożenia i stosując strategie łagodzenia, deweloperzy mogą tworzyć agentów AI, którzy są zarówno bezpieczni, jak i skuteczni. Dodatkowo włączenie podejścia człowiek w pętli zapewnia, że agenci AI pozostają zgodni z potrzebami użytkowników przy minimalizacji ryzyka. W miarę rozwoju AI utrzymanie proaktywnego podejścia do bezpieczeństwa, prywatności i kwestii etycznych będzie kluczowe dla budowania zaufania i niezawodności w systemach opartych na AI.

### Masz więcej pytań dotyczących tworzenia godnych zaufania agentów AI?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) , aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Przegląd odpowiedzialnego użycia AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena modeli generatywnej AI i aplikacji AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Wiadomości systemowe dotyczące bezpieczeństwa</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Szablon oceny ryzyka</a>

## Poprzednia lekcja

[Agentic RAG](../05-agentic-rag/README.md)

## Następna lekcja

[Planning Design Pattern](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeniowej opartej na AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za wersję autorytatywną. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->