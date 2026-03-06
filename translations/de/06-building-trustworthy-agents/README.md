[![Vertrauenswürdige KI-Agenten](../../../translated_images/de/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Aufbau vertrauenswürdiger KI-Agenten

## Einführung

Diese Lektion behandelt:

- Wie man sichere und effektive KI-Agenten entwickelt und bereitstellt
- Wichtige Sicherheitsüberlegungen bei der Entwicklung von KI-Agenten
- Wie man Datenschutz und Privatsphäre der Nutzer bei der Entwicklung von KI-Agenten wahrt

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Risiken bei der Erstellung von KI-Agenten identifizieren und mindern
- Sicherheitsmaßnahmen implementieren, um sicherzustellen, dass Daten und Zugriffe ordnungsgemäß verwaltet werden
- KI-Agenten erstellen, die Datenschutz gewährleisten und eine qualitativ hochwertige Nutzererfahrung bieten

## Sicherheit

Lassen Sie uns zunächst den Aufbau sicherer agentischer Anwendungen betrachten. Sicherheit bedeutet, dass der KI-Agent wie vorgesehen funktioniert. Als Entwickler agentischer Anwendungen verfügen wir über Methoden und Werkzeuge, um die Sicherheit zu maximieren:

### Aufbau eines Systemnachrichten-Frameworks

Wenn Sie schon einmal eine KI-Anwendung mit großen Sprachmodellen (LLMs) entwickelt haben, kennen Sie die Bedeutung eines robusten System-Prompts oder einer Systemnachricht. Diese Prompts legen die Meta-Regeln, Anweisungen und Richtlinien fest, wie das LLM mit dem Nutzer und Daten interagiert.

Für KI-Agenten ist der System-Prompt noch wichtiger, da die Agenten sehr spezifische Anweisungen benötigen, um die Aufgaben zu erfüllen, die wir für sie entworfen haben.

Um skalierbare System-Prompts zu erstellen, können wir ein Systemnachrichten-Framework nutzen, um einen oder mehrere Agenten in unserer Anwendung zu bauen:

![Aufbau eines Systemnachrichten-Frameworks](../../../translated_images/de/system-message-framework.3a97368c92d11d68.webp)

#### Schritt 1: Erstellen einer Meta-Systemnachricht

Die Meta-Prompt wird von einem LLM verwendet, um die System-Prompts für die Agenten zu erzeugen, die wir erstellen. Wir gestalten sie als Vorlage, damit wir bei Bedarf effizient mehrere Agenten anlegen können.

Hier ein Beispiel einer Meta-Systemnachricht, die wir dem LLM geben würden:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Schritt 2: Erstellen eines grundlegenden Prompts

Der nächste Schritt ist, einen grundlegenden Prompt zu erstellen, der den KI-Agenten beschreibt. Sie sollten die Rolle des Agenten, die Aufgaben, die der Agent erledigen soll, sowie weitere Verantwortlichkeiten des Agenten einschließen.

Hier ein Beispiel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Schritt 3: Basis-Systemnachricht an LLM übergeben

Jetzt können wir diese Systemnachricht optimieren, indem wir die Meta-Systemnachricht als Systemnachricht und unsere grundlegende Systemnachricht übergeben.

Dies erzeugt eine Systemnachricht, die besser dafür ausgelegt ist, unsere KI-Agenten zu steuern:

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

#### Schritt 4: Iterieren und verbessern

Der Wert dieses Systemnachrichten-Frameworks liegt darin, die Erstellung von Systemnachrichten für mehrere Agenten leichter skalieren sowie die Systemnachrichten im Laufe der Zeit verbessern zu können. Es ist selten, dass eine Systemnachricht beim ersten Mal für den kompletten Anwendungsfall funktioniert. Kleine Anpassungen und Verbesserungen durch Änderungen am grundlegenden Systemprompt und dessen Ausführen durch das System erlauben es, Ergebnisse zu vergleichen und zu bewerten.

## Bedrohungen verstehen

Um vertrauenswürdige KI-Agenten zu bauen, ist es wichtig, die Risiken und Bedrohungen für Ihren KI-Agenten zu verstehen und zu mindern. Lassen Sie uns einige der verschiedenen Bedrohungen für KI-Agenten betrachten und wie Sie besser planen und sich darauf vorbereiten können.

![Bedrohungen verstehen](../../../translated_images/de/understanding-threats.89edeada8a97fc0f.webp)

### Aufgabe und Anweisung

**Beschreibung:** Angreifer versuchen, die Anweisungen oder Ziele des KI-Agenten durch Prompting oder Manipulation der Eingaben zu ändern.

**Minderung:** Führen Sie Validierungsprüfungen und Eingabefilter durch, um potenziell gefährliche Prompts zu erkennen, bevor diese vom KI-Agenten verarbeitet werden. Da diese Angriffe typischerweise häufige Interaktionen mit dem Agenten erfordern, ist die Begrenzung der Anzahl der Gesprächsrunden eine weitere Möglichkeit, diese Angriffe zu verhindern.

### Zugriff auf kritische Systeme

**Beschreibung:** Wenn ein KI-Agent Zugang zu Systemen und Diensten hat, die sensible Daten speichern, können Angreifer die Kommunikation zwischen dem Agenten und diesen Diensten kompromittieren. Das können direkte Angriffe oder indirekte Versuche sein, Informationen über diese Systeme durch den Agenten zu gewinnen.

**Minderung:** KI-Agenten sollten nur bei Bedarf Zugang zu Systemen erhalten, um diese Arten von Angriffen zu verhindern. Die Kommunikation zwischen Agent und System sollte außerdem gesichert sein. Die Implementierung von Authentifizierung und Zugriffskontrolle ist ein weiterer Weg, diese Informationen zu schützen.

### Überlastung von Ressourcen und Diensten

**Beschreibung:** KI-Agenten können verschiedene Werkzeuge und Dienste nutzen, um Aufgaben zu erledigen. Angreifer können diese Fähigkeit ausnutzen, um diese Dienste anzugreifen, indem sie eine hohe Anzahl von Anfragen über den KI-Agenten senden, was zu Systemausfällen oder hohen Kosten führen kann.

**Minderung:** Implementieren Sie Richtlinien, die die Anzahl der Anfragen begrenzen, die ein KI-Agent an einen Dienst richten kann. Die Begrenzung der Anzahl der Gesprächsrunden und Anfragen an Ihren KI-Agenten ist eine weitere Möglichkeit, diese Angriffe zu verhindern.

### Vergiftung der Wissensbasis

**Beschreibung:** Dieser Angriff richtet sich nicht direkt gegen den KI-Agenten, sondern gegen die Wissensbasis und andere Dienste, die der Agent nutzt. Dies kann bedeuten, dass die Daten oder Informationen, die der KI-Agent zur Erfüllung einer Aufgabe verwendet, manipuliert werden, was zu verzerrten oder unbeabsichtigten Antworten für den Nutzer führt.

**Minderung:** Führen Sie regelmäßige Überprüfungen der Daten durch, die der KI-Agent in seinen Abläufen verwendet. Stellen Sie sicher, dass der Zugriff auf diese Daten sicher ist und nur von vertrauenswürdigen Personen verändert werden kann, um diese Art von Angriff zu vermeiden.

### Kaskadierende Fehler

**Beschreibung:** KI-Agenten greifen auf verschiedene Werkzeuge und Dienste zu, um Aufgaben zu erfüllen. Fehler, die durch Angreifer verursacht werden, können zu Ausfällen anderer Systeme führen, mit denen der KI-Agent verbunden ist, wodurch der Angriff sich ausbreitet und schwerer zu beheben ist.

**Minderung:** Eine Möglichkeit, dies zu vermeiden, ist, den KI-Agenten in einer begrenzten Umgebung arbeiten zu lassen, z. B. indem Aufgaben in einem Docker-Container ausgeführt werden, um direkte Systemangriffe zu verhindern. Das Einrichten von Fallback-Mechanismen und Wiederholungslogik, wenn bestimmte Systeme mit einem Fehler reagieren, ist eine weitere Methode, größere Systemausfälle zu verhindern.

## Mensch in der Schleife

Eine weitere effektive Möglichkeit, vertrauenswürdige KI-Agentensysteme zu entwickeln, ist die Verwendung eines Mensch-in-der-Schleife-Ansatzes. Dies erzeugt einen Ablauf, bei dem Nutzer während der Laufzeit Feedback an die Agenten geben können. Nutzer agieren im Wesentlichen als Agenten in einem Multi-Agenten-System und können die Ausführung genehmigen oder beenden.

![Mensch in der Schleife](../../../translated_images/de/human-in-the-loop.5f0068a678f62f4f.webp)

Hier ist ein Codebeispiel, das mit dem Microsoft Agent Framework zeigt, wie dieses Konzept umgesetzt wird:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Erstelle den Anbieter mit menschlicher Genehmigung im Prozess
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Erstelle den Agenten mit einem menschlichen Genehmigungsschritt
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Der Benutzer kann die Antwort überprüfen und genehmigen
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Fazit

Der Aufbau vertrauenswürdiger KI-Agenten erfordert sorgfältiges Design, robuste Sicherheitsmaßnahmen und kontinuierliche Iterationen. Durch die Implementierung strukturierter Meta-Prompting-Systeme, das Verständnis möglicher Bedrohungen und die Anwendung von Minderungsstrategien können Entwickler KI-Agenten erstellen, die sowohl sicher als auch effektiv sind. Zudem stellt die Einbindung eines Mensch-in-der-Schleife-Ansatzes sicher, dass KI-Agenten auf die Bedürfnisse der Nutzer abgestimmt bleiben und gleichzeitig Risiken minimiert werden. Mit der Weiterentwicklung der KI wird es entscheidend sein, eine proaktive Haltung gegenüber Sicherheit, Datenschutz und ethischen Überlegungen einzunehmen, um Vertrauen und Zuverlässigkeit in KI-gesteuerten Systemen zu fördern.

### Haben Sie weitere Fragen zum Aufbau vertrauenswürdiger KI-Agenten?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Überblick zu verantwortungsbewusster KI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Bewertung von generativen KI-Modellen und KI-Anwendungen</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sicherheits-Systemnachrichten</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Vorlage zur Risikoabschätzung</a>

## Vorherige Lektion

[Agentic RAG](../05-agentic-rag/README.md)

## Nächste Lektion

[Planungsmuster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->