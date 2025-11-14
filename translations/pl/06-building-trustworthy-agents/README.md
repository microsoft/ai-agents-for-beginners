<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-30T14:24:32+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "pl"
}
-->
[![Zaufani Agenci AI](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.pl.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

# Tworzenie Zaufanych Agentów AI

## Wprowadzenie

W tej lekcji omówimy:

- Jak budować i wdrażać bezpiecznych i skutecznych Agentów AI.
- Ważne kwestie związane z bezpieczeństwem podczas tworzenia Agentów AI.
- Jak zapewnić prywatność danych i użytkowników podczas tworzenia Agentów AI.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

- Identyfikować i minimalizować ryzyka podczas tworzenia Agentów AI.
- Wdrażać środki bezpieczeństwa, aby zapewnić właściwe zarządzanie danymi i dostępem.
- Tworzyć Agentów AI, którzy zachowują prywatność danych i zapewniają wysoką jakość doświadczenia użytkownika.

## Bezpieczeństwo

Najpierw przyjrzyjmy się, jak budować bezpieczne aplikacje agentowe. Bezpieczeństwo oznacza, że agent AI działa zgodnie z założeniami. Jako twórcy aplikacji agentowych mamy metody i narzędzia, które pozwalają maksymalizować bezpieczeństwo:

### Tworzenie Ram Systemowych Wiadomości

Jeśli kiedykolwiek budowałeś aplikację AI wykorzystującą duże modele językowe (LLM), wiesz, jak ważne jest zaprojektowanie solidnego systemowego promptu lub wiadomości systemowej. Te prompty ustalają meta zasady, instrukcje i wytyczne dotyczące interakcji LLM z użytkownikiem i danymi.

Dla Agentów AI wiadomość systemowa jest jeszcze ważniejsza, ponieważ agenci potrzebują bardzo precyzyjnych instrukcji, aby wykonać zaprojektowane dla nich zadania.

Aby tworzyć skalowalne wiadomości systemowe, możemy użyć ram systemowych wiadomości do budowy jednego lub więcej agentów w naszej aplikacji:

![Tworzenie Ram Systemowych Wiadomości](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.pl.png)

#### Krok 1: Stwórz Meta Wiadomość Systemową

Meta prompt będzie używany przez LLM do generowania wiadomości systemowych dla agentów, których tworzymy. Projektujemy go jako szablon, aby móc efektywnie tworzyć wielu agentów, jeśli zajdzie taka potrzeba.

Oto przykład meta wiadomości systemowej, którą moglibyśmy przekazać LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Krok 2: Stwórz podstawowy prompt

Kolejnym krokiem jest stworzenie podstawowego promptu opisującego Agenta AI. Powinien on zawierać rolę agenta, zadania, które ma wykonać, oraz inne jego obowiązki.

Oto przykład:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Krok 3: Przekaż Podstawową Wiadomość Systemową do LLM

Teraz możemy zoptymalizować tę wiadomość systemową, przekazując meta wiadomość systemową jako wiadomość systemową oraz naszą podstawową wiadomość systemową.

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

#### Krok 4: Iteracja i Ulepszanie

Wartość tej ramy wiadomości systemowych polega na możliwości łatwego skalowania tworzenia wiadomości systemowych dla wielu agentów oraz ulepszania ich z czasem. Rzadko zdarza się, aby wiadomość systemowa działała idealnie za pierwszym razem dla całego przypadku użycia. Możliwość wprowadzania drobnych poprawek i ulepszeń poprzez zmianę podstawowej wiadomości systemowej i ponowne jej przetworzenie pozwala na porównanie i ocenę wyników.

## Zrozumienie Zagrożeń

Aby budować zaufanych agentów AI, ważne jest zrozumienie i minimalizowanie ryzyk oraz zagrożeń związanych z agentem AI. Przyjrzyjmy się niektórym z różnych zagrożeń dla agentów AI i sposobom ich lepszego planowania i przygotowania.

![Zrozumienie Zagrożeń](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.pl.png)

### Zadania i Instrukcje

**Opis:** Atakujący próbują zmienić instrukcje lub cele agenta AI poprzez manipulację promptami lub wejściami.

**Minimalizacja ryzyka:** Wykonuj walidację i filtrowanie wejść, aby wykrywać potencjalnie niebezpieczne prompty przed ich przetworzeniem przez agenta AI. Ponieważ tego typu ataki zwykle wymagają częstej interakcji z agentem, ograniczenie liczby wymian w rozmowie to kolejny sposób na zapobieganie tego typu atakom.

### Dostęp do Krytycznych Systemów

**Opis:** Jeśli agent AI ma dostęp do systemów i usług przechowujących wrażliwe dane, atakujący mogą skompromitować komunikację między agentem a tymi usługami. Mogą to być bezpośrednie ataki lub próby pośredniego uzyskania informacji o tych systemach za pośrednictwem agenta.

**Minimalizacja ryzyka:** Agenci AI powinni mieć dostęp do systemów wyłącznie w razie potrzeby, aby zapobiec tego typu atakom. Komunikacja między agentem a systemem powinna być również zabezpieczona. Wdrożenie uwierzytelniania i kontroli dostępu to kolejny sposób na ochronę tych informacji.

### Przeciążenie Zasobów i Usług

**Opis:** Agenci AI mogą korzystać z różnych narzędzi i usług do wykonywania zadań. Atakujący mogą wykorzystać tę zdolność do atakowania tych usług, wysyłając dużą liczbę żądań za pośrednictwem agenta AI, co może prowadzić do awarii systemu lub wysokich kosztów.

**Minimalizacja ryzyka:** Wdrożenie polityk ograniczających liczbę żądań, jakie agent AI może wysłać do usługi. Ograniczenie liczby wymian w rozmowie i żądań do agenta AI to kolejny sposób na zapobieganie tego typu atakom.

### Zatrucie Bazy Wiedzy

**Opis:** Ten rodzaj ataku nie jest skierowany bezpośrednio na agenta AI, ale na bazę wiedzy i inne usługi, z których korzysta agent AI. Może to obejmować uszkodzenie danych lub informacji, które agent AI wykorzystuje do wykonania zadania, co prowadzi do stronniczych lub niezamierzonych odpowiedzi dla użytkownika.

**Minimalizacja ryzyka:** Regularnie weryfikuj dane, z których agent AI korzysta w swoich procesach. Upewnij się, że dostęp do tych danych jest zabezpieczony i zmieniany wyłącznie przez zaufane osoby, aby uniknąć tego typu ataków.

### Błędy Kaskadowe

**Opis:** Agenci AI korzystają z różnych narzędzi i usług do wykonywania zadań. Błędy spowodowane przez atakujących mogą prowadzić do awarii innych systemów, z którymi agent AI jest połączony, powodując, że atak staje się bardziej rozległy i trudniejszy do rozwiązania.

**Minimalizacja ryzyka:** Jednym ze sposobów uniknięcia tego jest działanie agenta AI w ograniczonym środowisku, takim jak wykonywanie zadań w kontenerze Docker, aby zapobiec bezpośrednim atakom na system. Tworzenie mechanizmów awaryjnych i logiki ponawiania prób, gdy określone systemy odpowiadają błędem, to kolejny sposób na zapobieganie większym awariom systemowym.

## Człowiek w Pętli

Innym skutecznym sposobem budowania zaufanych systemów Agentów AI jest wykorzystanie człowieka w pętli. Tworzy to przepływ, w którym użytkownicy mogą dostarczać agentom opinii podczas ich działania. Użytkownicy zasadniczo działają jako agenci w systemie wieloagentowym, zapewniając zatwierdzenie lub zakończenie procesu.

![Człowiek w Pętli](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.pl.png)

Oto fragment kodu wykorzystujący AutoGen, który pokazuje, jak ta koncepcja jest wdrażana:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Podsumowanie

Tworzenie zaufanych agentów AI wymaga starannego projektowania, solidnych środków bezpieczeństwa i ciągłej iteracji. Wdrażając strukturalne systemy meta promptów, rozumiejąc potencjalne zagrożenia i stosując strategie minimalizacji ryzyka, programiści mogą tworzyć agentów AI, którzy są zarówno bezpieczni, jak i skuteczni. Dodatkowo, włączenie człowieka w pętli zapewnia, że agenci AI pozostają zgodni z potrzebami użytkowników, minimalizując jednocześnie ryzyko. W miarę rozwoju AI, utrzymanie proaktywnego podejścia do bezpieczeństwa, prywatności i kwestii etycznych będzie kluczowe dla budowania zaufania i niezawodności w systemach opartych na AI.

### Masz więcej pytań dotyczących tworzenia zaufanych Agentów AI?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacyjnych i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Przegląd odpowiedzialnego korzystania z AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ocena modeli generatywnych AI i aplikacji AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Wiadomości systemowe dotyczące bezpieczeństwa</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Szablon oceny ryzyka</a>

## Poprzednia lekcja

[Agentic RAG](../05-agentic-rag/README.md)

## Następna lekcja

[Wzorzec projektowania planowania](../07-planning-design/README.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.