[![Godni Zaufania Agenci AI](../../../translated_images/pl/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknij powyższy obraz, aby zobaczyć wideo z tej lekcji)_

# Tworzenie Godnych Zaufania Agentów AI

## Wprowadzenie

Ta lekcja obejmie:

- Jak budować i wdrażać bezpieczne i skuteczne Agentów AI
- Ważne aspekty bezpieczeństwa podczas tworzenia Agentów AI.
- Jak zachować prywatność danych i użytkowników podczas tworzenia Agentów AI.

## Cele Nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

- Identyfikować i łagodzić ryzyka podczas tworzenia Agentów AI.
- Wdrażać środki bezpieczeństwa, aby zapewnić prawidłowe zarządzanie danymi i dostępem.
- Tworzyć Agentów AI, którzy zachowują prywatność danych i zapewniają wysoką jakość doświadczenia użytkownika.

## Bezpieczeństwo

Najpierw przyjrzyjmy się tworzeniu bezpiecznych aplikacji agentowych. Bezpieczeństwo oznacza, że agent AI działa zgodnie z zamierzeniami. Jako twórcy aplikacji agentowych mamy metody i narzędzia maksymalizujące bezpieczeństwo:

### Budowanie Ramy Wiadomości Systemowej

Jeśli kiedykolwiek tworzyłeś aplikację AI korzystającą z dużych modeli językowych (LLM), wiesz jak ważne jest zaprojektowanie solidnego systemowego promptu lub wiadomości systemowej. Te prompta ustanawiają meta zasady, instrukcje i wytyczne dotyczące interakcji LLM z użytkownikiem i danymi.

Dla Agentów AI prompt systemowy jest jeszcze ważniejszy, ponieważ agenci AI potrzebują bardzo precyzyjnych instrukcji do wykonania zadań, które dla nich zaprojektowaliśmy.

Aby tworzyć skalowalne prompta systemowe, możemy użyć ramy wiadomości systemowej do budowy jednego lub więcej agentów w naszej aplikacji:

![Budowanie Ramy Wiadomości Systemowej](../../../translated_images/pl/system-message-framework.3a97368c92d11d68.webp)

#### Krok 1: Utwórz Meta Wiadomość Systemową

Meta prompt będzie używany przez LLM do generowania prompt systemowych dla tworzonych przez nas agentów. Projektujemy go jako szablon, aby efektywnie tworzyć wielu agentów w razie potrzeby.

Oto przykład meta wiadomości systemowej, którą przekazalibyśmy LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Utwórz podstawowy prompt

Następny krok to utworzenie podstawowego promptu opisującego Agenta AI. Powinieneś uwzględnić rolę agenta, zadania do wykonania oraz inne odpowiedzialności agenta.

Oto przykład:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Przekaż Podstawową Wiadomość Systemową do LLM

Teraz możemy zoptymalizować tę wiadomość systemową, przekazując meta wiadomość systemową jako wiadomość systemową wraz z naszą podstawową wiadomością systemową.

To wygeneruje wiadomość systemową lepiej zaprojektowaną do prowadzenia naszych Agentów AI:

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

#### Krok 4: Iteruj i Udoskonalaj

Wartość tej ramy wiadomości systemowej polega na tym, że ułatwia skalowanie tworzenia wiadomości systemowych dla wielu agentów, a także umożliwia ulepszanie wiadomości systemowych z czasem. Rzadko zdarza się, że wiadomość systemowa działa idealnie za pierwszym razem dla całego przypadku użycia. Możliwość wprowadzania drobnych poprawek i ulepszeń poprzez zmianę podstawowej wiadomości systemowej i ponowne jej przetwarzanie pozwala porównywać i oceniać wyniki.

## Zrozumienie Zagrożeń

Aby budować godnych zaufania agentów AI, ważne jest rozumienie i łagodzenie ryzyka oraz zagrożeń dla twojego agenta AI. Przyjrzyjmy się niektórym zagrożeniom dla agentów AI i jak lepiej się do nich przygotować.

![Zrozumienie Zagrożeń](../../../translated_images/pl/understanding-threats.89edeada8a97fc0f.webp)

### Zadanie i Instrukcje

**Opis:** Atakujący próbują zmienić instrukcje lub cele agenta AI poprzez promptowanie lub manipulowanie wejściami.

**Łagodzenie**: Wdrażaj kontrole walidacji i filtry wejściowe, aby wykryć potencjalnie niebezpieczne prompta przed ich przetworzeniem przez Agenta AI. Ponieważ te ataki zwykle wymagają częstej interakcji z Agentem, ograniczenie liczby tur w rozmowie to kolejny sposób zapobiegania tego typu atakom.

### Dostęp do Krytycznych Systemów

**Opis**: Jeśli agent AI ma dostęp do systemów i usług przechowujących wrażliwe dane, atakujący mogą przechwycić komunikację między agentem a tymi usługami. Mogą to być bezpośrednie ataki lub pośrednie próby uzyskania informacji o tych systemach za pośrednictwem agenta.

**Łagodzenie**: Agenci AI powinni mieć dostęp do systemów na zasadzie "potrzeby tylko wtedy, gdy to konieczne", aby zapobiec tego typu atakom. Komunikacja między agentem a systemem powinna być również bezpieczna. Wdrożenie uwierzytelniania i kontroli dostępu to kolejny sposób ochrony tych informacji.

### Przeciążenie Zasobów i Usług

**Opis:** Agenci AI mogą korzystać z różnych narzędzi i usług do wykonywania zadań. Atakujący mogą wykorzystać tę zdolność do atakowania tych usług, wysyłając dużą liczbę żądań za pośrednictwem Agenta AI, co może powodować awarie systemu lub wysokie koszty.

**Łagodzenie:** Wprowadź polityki ograniczające liczbę żądań, jakie agent AI może wysłać do usługi. Ograniczenie liczby tur i żądań do twojego agenta AI to kolejny sposób zapobiegania tego typu atakom.

### Zatrucie Bazy Wiedzy

**Opis:** Ten typ ataku nie jest skierowany bezpośrednio na agenta AI, ale na bazę wiedzy i inne usługi używane przez agenta AI. Może to obejmować uszkodzenie danych lub informacji, których agent AI użyje do wykonania zadania, co prowadzi do stronniczych lub niezamierzonych odpowiedzi dla użytkownika.

**Łagodzenie:** Regularnie weryfikuj dane, które agent AI będzie wykorzystywał w swoich procesach. Upewnij się, że dostęp do tych danych jest zabezpieczony i mogą je zmieniać tylko zaufane osoby, aby uniknąć tego typu ataków.

### Błędne Błędy Kaskadowe

**Opis:** Agenci AI uzyskują dostęp do różnych narzędzi i usług, aby wykonać zadania. Błędy spowodowane przez atakujących mogą prowadzić do awarii innych systemów powiązanych z agentem AI, powodując, że atak stanie się bardziej rozległy i trudniejszy do zdiagnozowania.

**Łagodzenie**: Jedną z metod uniknięcia tego jest działanie Agenta AI w ograniczonym środowisku, na przykład wykonując zadania w kontenerze Docker, aby zapobiec bezpośrednim atakom na system. Tworzenie mechanizmów awaryjnych i logiki ponownych prób, gdy niektóre systemy odpowiadają błędem, to kolejny sposób zapobiegania poważniejszym awariom systemu.

## Człowiek w Pętli

Kolejnym skutecznym sposobem tworzenia godnych zaufania systemów Agentów AI jest zastosowanie człowieka w pętli (Human-in-the-loop). Tworzy to przepływ, w którym użytkownicy mogą przekazywać opinie agentom podczas działania. Użytkownicy w zasadzie działają jako agenci w systemie wieloagentowym, zatwierdzając lub przerywając działanie procesu.

![Człowiek w Pętli](../../../translated_images/pl/human-in-the-loop.5f0068a678f62f4f.webp)

Oto fragment kodu używający Microsoft Agent Framework pokazujący, jak implementuje się tę koncepcję:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Utwórz dostawcę z zatwierdzeniem człowieka w pętli
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Utwórz agenta z etapem zatwierdzenia przez człowieka
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Użytkownik może przeglądać i zatwierdzać odpowiedź
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Podsumowanie

Budowanie godnych zaufania agentów AI wymaga starannego projektowania, solidnych środków bezpieczeństwa oraz ciągłej iteracji. Poprzez wdrożenie ustrukturyzowanych systemów meta prompt, zrozumienie potencjalnych zagrożeń oraz stosowanie strategii łagodzenia, programiści mogą stworzyć agentów AI, którzy są bezpieczni i efektywni. Dodatkowo, włączenie podejścia człowieka w pętli zapewnia, że agenci AI pozostają zgodni z potrzebami użytkowników, minimalizując ryzyko. W miarę rozwoju AI, utrzymywanie proaktywnego podejścia do bezpieczeństwa, prywatności i kwestii etycznych będzie kluczem do budowania zaufania i niezawodności systemów opartych na AI.

## Przykłady Kodów

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Pokaz krok po kroku systemu meta-prompt ramy wiadomości systemowych.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Bramki zatwierdzania przed działaniem, ocena ryzyka i logowanie audytu dla godnych zaufania agentów.

### Masz więcej pytań dotyczących tworzenia godnych zaufania Agentów AI?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

## Dodatkowe Zasoby

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Przegląd odpowiedzialnego AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena modeli generatywnej AI i aplikacji AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Systemowe wiadomości bezpieczeństwa</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Szablon oceny ryzyka</a>

## Poprzednia Lekcja

[Agentic RAG](../05-agentic-rag/README.md)

## Następna Lekcja

[Wzorzec projektowy Planowania](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->