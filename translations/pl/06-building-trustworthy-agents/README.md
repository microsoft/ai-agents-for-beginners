[![Godne zaufania agenty AI](../../../translated_images/pl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Budowanie godnych zaufania agentów AI

## Wprowadzenie

W tej lekcji omówimy:

- Jak budować i wdrażać bezpieczne i skuteczne agenty AI
- Ważne zagadnienia związane z bezpieczeństwem podczas tworzenia agentów AI
- Jak zachować prywatność danych i użytkowników podczas tworzenia agentów AI

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

- Identyfikować i łagodzić ryzyka podczas tworzenia agentów AI
- Wdrażać środki bezpieczeństwa, aby właściwie zarządzać danymi i dostępem
- Tworzyć agentów AI, którzy chronią prywatność danych i zapewniają wysoką jakość doświadczenia użytkownika

## Bezpieczeństwo

Najpierw przyjrzyjmy się budowaniu bezpiecznych aplikacji agentowych. Bezpieczeństwo oznacza, że agent AI działa zgodnie z założeniami. Jako twórcy aplikacji agentowych mamy metody i narzędzia, aby maksymalizować bezpieczeństwo:

### Budowanie frameworku wiadomości systemowych

Jeśli kiedykolwiek budowałeś aplikację AI wykorzystującą duże modele językowe (LLM), wiesz, jak ważne jest zaprojektowanie solidnego promptu systemowego lub wiadomości systemowej. Te prompti ustalają metazasady, instrukcje i wytyczne dotyczące interakcji modelu LLM z użytkownikiem oraz danymi.

W przypadku agentów AI prompt systemowy jest jeszcze ważniejszy, ponieważ agenci AI potrzebują bardzo precyzyjnych instrukcji, aby wykonać zaprojektowane dla nich zadania.

Aby tworzyć skalowalne prompty systemowe, możemy użyć frameworku wiadomości systemowych do budowania jednego lub więcej agentów w naszej aplikacji:

![Budowanie frameworku wiadomości systemowych](../../../translated_images/pl/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Utwórz wiadomość meta systemu

Meta prompt będzie używany przez LLM do generowania promptów systemowych dla tworzonych agentów. Projektujemy go jako szablon, aby móc efektywnie tworzyć wielu agentów w razie potrzeby.

Oto przykład meta wiadomości systemowej, którą przekazalibyśmy LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Utwórz podstawowy prompt

Następnym krokiem jest stworzenie podstawowego promptu opisującego agenta AI. Powinieneś uwzględnić rolę agenta, zadania, które będzie wykonywał, oraz inne odpowiedzialności agenta.

Oto przykład:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Przekaż podstawową wiadomość systemową do LLM

Teraz możemy zoptymalizować tę wiadomość systemową, przekazując zarówno meta wiadomość systemową, jak i naszą podstawową wiadomość systemową.

To wygeneruje wiadomość systemową lepiej zaprojektowaną do prowadzenia naszych agentów AI:

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

#### Krok 4: Iteruj i udoskonalaj

Wartość tego frameworku wiadomości systemowych polega na łatwiejszym skalowaniu tworzenia wiadomości systemowych dla wielu agentów oraz na możliwości ulepszania swoich wiadomości systemowych w czasie. Rzadko zdarza się, że wiadomość systemowa działa idealnie za pierwszym razem dla całego przypadku użycia. Możliwość wprowadzania drobnych poprawek i usprawnień przez zmianę podstawowej wiadomości systemowej i przetwarzanie jej przez system pozwala porównywać i oceniać wyniki.

## Zrozumienie zagrożeń

Aby budować godnych zaufania agentów AI, ważne jest zrozumienie i łagodzenie ryzyk oraz zagrożeń dla twojego agenta AI. Przyjrzyjmy się niektórym zagrożeniom dla agentów AI i jak można się na nie lepiej przygotować oraz planować działania.

![Zrozumienie zagrożeń](../../../translated_images/pl/understanding-threats.89edeada8a97fc0f.webp)

### Zadanie i instrukcje

**Opis:** Atakujący próbują zmienić instrukcje lub cele agenta AI poprzez promptowanie lub manipulowanie danymi wejściowymi.

**Łagodzenie:** Wykonuj kontrole walidacyjne i filtry wejściowe, aby wykrywać potencjalnie niebezpieczne prompti zanim zostaną przetworzone przez agenta AI. Ponieważ te ataki zwykle wymagają częstej interakcji z agentem, ograniczenie liczby tur w rozmowie jest kolejnym sposobem zapobiegania takim atakom.

### Dostęp do krytycznych systemów

**Opis:** Jeśli agent AI ma dostęp do systemów i usług przechowujących dane wrażliwe, atakujący mogą przejąć komunikację między agentem a tymi usługami. Mogą to być bezpośrednie ataki lub próby pośrednie zdobycia informacji o tych systemach poprzez agenta.

**Łagodzenie:** Agenci AI powinni mieć dostęp do systemów wyłącznie na zasadzie "need-only" (tylko wtedy, gdy jest to potrzebne), aby zapobiec tego typu atakom. Komunikacja między agentem a systemem również powinna być zabezpieczona. Wdrożenie uwierzytelniania i kontroli dostępu jest kolejnym sposobem ochrony tych informacji.

### Przeciążenie zasobów i usług

**Opis:** Agenci AI mogą uzyskiwać dostęp do różnych narzędzi i usług, aby wykonywać zadania. Atakujący mogą wykorzystać tę zdolność do atakowania tych usług, wysyłając dużą liczbę żądań przez agenta AI, co może skutkować awariami systemów lub wysokimi kosztami.

**Łagodzenie:** Wdroż polityki ograniczające liczbę żądań, jakie agent AI może kierować do usługi. Ograniczenie liczby tur konwersacji i żądań do agenta AI jest kolejnym sposobem zapobiegania takim atakom.

### Zatrucie bazy wiedzy

**Opis:** Ten typ ataku nie jest skierowany bezpośrednio na agenta AI, lecz na bazę wiedzy i inne usługi, z których agent AI korzysta. Może to obejmować uszkodzenie danych lub informacji, których używa agent, co prowadzi do stronniczych lub niezamierzonych odpowiedzi dla użytkownika.

**Łagodzenie:** Regularnie weryfikuj dane, z których agent AI korzysta w swoich workflowach. Upewnij się, że dostęp do tych danych jest zabezpieczony i mogą je modyfikować tylko zaufane osoby, aby uniknąć tego typu ataków.

### Kaskadowe błędy

**Opis:** Agenci AI uzyskują dostęp do różnych narzędzi i usług, aby wykonywać zadania. Błędy spowodowane atakami mogą prowadzić do awarii innych systemów, z którymi agent jest powiązany, przez co atak staje się bardziej rozległy i trudniejszy do zdiagnozowania.

**Łagodzenie:** Jednym ze sposobów na uniknięcie tego jest uruchamianie agenta AI w ograniczonym środowisku, np. wykonywanie zadań w kontenerze Docker, aby zapobiec bezpośrednim atakom na system. Tworzenie mechanizmów awaryjnych oraz logiki ponawiania prób, gdy pewne systemy zgłaszają błędy, jest kolejnym sposobem zapobiegania większym awariom systemu.

## Człowiek w pętli

Innym skutecznym sposobem na budowanie godnych zaufania systemów agentów AI jest zastosowanie podejścia Human-in-the-loop. Tworzy to przepływ, w którym użytkownicy mogą na bieżąco przekazywać feedback agentom podczas działania. Użytkownicy w zasadzie pełnią rolę agentów w systemie multi-agentowym, dostarczając zatwierdzenia bądź przerywając wykonywany proces.

![Człowiek w pętli](../../../translated_images/pl/human-in-the-loop.5f0068a678f62f4f.webp)

Oto fragment kodu wykorzystujący Microsoft Agent Framework, pokazujący, jak ten koncept jest implementowany:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Utwórz dostawcę z zatwierdzeniem człowieka w pętli
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

Budowanie godnych zaufania agentów AI wymaga starannego projektowania, solidnych środków bezpieczeństwa i ciągłej iteracji. Wdrażając strukturalne systemy meta-promptów, rozumiejąc potencjalne zagrożenia i stosując strategie łagodzenia, programiści mogą tworzyć agentów AI, którzy są zarówno bezpieczni, jak i skuteczni. Dodatkowo, włączenie podejścia human-in-the-loop zapewnia, że agenci AI pozostają zgodni z potrzebami użytkowników, minimalizując jednocześnie ryzyko. W miarę rozwoju AI kluczowe będzie utrzymywanie proaktywnego podejścia do bezpieczeństwa, prywatności i etycznych aspektów, by wzmacniać zaufanie i niezawodność systemów opartych na AI.

## Przykłady kodu

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Pokaz krok po kroku frameworku systemu wiadomości meta-prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Bramki zatwierdzające przed działaniem, segmentacja ryzyka oraz logowanie audytu dla godnych zaufania agentów.

### Masz więcej pytań dotyczących budowania godnych zaufania agentów AI?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w dyżurach i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Przegląd odpowiedzialnego AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena modeli generatywnego AI i aplikacji AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Wiadomości systemowe związane z bezpieczeństwem</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Szablon oceny ryzyka</a>

## Poprzednia lekcja

[Agentic RAG](../05-agentic-rag/README.md)

## Następna lekcja

[Wzorzec projektowy planowania](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->