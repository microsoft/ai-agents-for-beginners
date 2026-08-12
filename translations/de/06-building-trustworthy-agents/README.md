[![Vertrauenswürdige KI-Agenten](../../../translated_images/de/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

# Vertrauenswürdige KI-Agenten entwickeln

## Einführung

Diese Lektion behandelt:

- Wie man sichere und effektive KI-Agenten entwickelt und bereitstellt
- Wichtige Sicherheitsaspekte bei der Entwicklung von KI-Agenten.
- Wie man Datenschutz und Privatsphäre bei der Entwicklung von KI-Agenten wahrt.

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Risiken bei der Erstellung von KI-Agenten erkennen und mindern.
- Sicherheitsmaßnahmen implementieren, um zu gewährleisten, dass Daten und Zugriffe ordnungsgemäß verwaltet werden.
- KI-Agenten erstellen, die Datenschutz gewährleisten und eine hochwertige Nutzererfahrung bieten.

## Sicherheit

Schauen wir uns zunächst den Aufbau sicherer agentischer Anwendungen an. Sicherheit bedeutet, dass der KI-Agent wie vorgesehen funktioniert. Als Entwickler agentischer Anwendungen stehen uns Methoden und Werkzeuge zur Verfügung, um die Sicherheit zu maximieren:

### Aufbau eines Systemnachrichten-Frameworks

Wenn Sie schon einmal eine KI-Anwendung mit großen Sprachmodellen (LLMs) gebaut haben, kennen Sie die Bedeutung eines robusten System-Prompts oder einer Systemnachricht. Diese Prompts legen die Metaregeln, Anweisungen und Richtlinien dafür fest, wie das LLM mit dem Nutzer und den Daten interagiert.

Für KI-Agenten ist der System-Prompt noch wichtiger, da die KI-Agenten sehr spezifische Anweisungen benötigen, um die von uns vorgesehenen Aufgaben zu erfüllen.

Um skalierbare System-Prompts zu erstellen, können wir ein Systemnachrichten-Framework verwenden, um einen oder mehrere Agenten in unserer Anwendung zu erstellen:

![Aufbau eines Systemnachrichten-Frameworks](../../../translated_images/de/system-message-framework.3a97368c92d11d68.webp)

#### Schritt 1: Erstellen einer Meta-Systemnachricht

Das Meta-Prompt wird von einem LLM verwendet, um die System-Prompts für die von uns erstellten Agenten zu erzeugen. Wir gestalten es als Vorlage, damit wir bei Bedarf effizient mehrere Agenten erstellen können.

Hier ist ein Beispiel für eine Meta-Systemnachricht, die wir dem LLM geben würden:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Schritt 2: Erstellen eines einfachen Prompts

Der nächste Schritt ist das Erstellen eines einfachen Prompts zur Beschreibung des KI-Agenten. Sie sollten die Rolle des Agenten, die Aufgaben, die er erfüllen wird, und weitere Verantwortlichkeiten einschließen.

Hier ist ein Beispiel:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Schritt 3: Bereitstellen der Basis-Systemnachricht an das LLM

Jetzt können wir diese Systemnachricht optimieren, indem wir die Meta-Systemnachricht als Systemnachricht und unsere Basis-Systemnachricht bereitstellen.

Dies erzeugt eine Systemnachricht, die besser darauf ausgelegt ist, unsere KI-Agenten zu leiten:

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

#### Schritt 4: Iterieren und Verbessern

Der Wert dieses Systemnachrichten-Frameworks liegt darin, das Erstellen von Systemnachrichten mehrerer Agenten leichter zu skalieren und Ihre Systemnachrichten im Laufe der Zeit zu verbessern. Es ist selten, dass Sie die perfekte Systemnachricht direkt beim ersten Mal für Ihren kompletten Anwendungsfall haben. Kleine Anpassungen und Verbesserungen durch Änderung der Basis-Systemnachricht und deren Wiederholung im System ermöglichen es Ihnen, Ergebnisse zu vergleichen und zu bewerten.

## Bedrohungen verstehen

Um vertrauenswürdige KI-Agenten zu entwickeln, ist es wichtig, die Risiken und Bedrohungen für Ihren KI-Agenten zu verstehen und zu mindern. Schauen wir uns einige der verschiedenen Bedrohungen für KI-Agenten an und wie Sie besser planen und vorbereiten können.

![Bedrohungen verstehen](../../../translated_images/de/understanding-threats.89edeada8a97fc0f.webp)

### Aufgabe und Anweisung

**Beschreibung:** Angreifer versuchen, die Anweisungen oder Ziele des KI-Agenten durch Prompts oder Manipulation der Eingaben zu ändern.

**Minderung:** Führen Sie Validierungsprüfungen und Eingabefilter durch, um potenziell gefährliche Prompts zu erkennen, bevor sie vom KI-Agenten verarbeitet werden. Da diese Angriffe typischerweise häufige Interaktionen mit dem Agenten erfordern, ist eine Begrenzung der Gesprächsrunden eine weitere Möglichkeit, diese Angriffe zu verhindern.

### Zugriff auf kritische Systeme

**Beschreibung:** Wenn ein KI-Agent Zugriff auf Systeme und Dienste hat, die sensible Daten speichern, können Angreifer die Kommunikation zwischen dem Agenten und diesen Diensten kompromittieren. Dies können direkte Angriffe oder indirekte Versuche sein, Informationen über diese Systeme durch den Agenten zu erhalten.

**Minderung:** KI-Agenten sollten nur bedarfsorientierten Zugriff auf Systeme haben, um solche Angriffe zu verhindern. Die Kommunikation zwischen Agent und System sollte ebenfalls sicher sein. Die Implementierung von Authentifizierung und Zugangskontrolle schützt diese Informationen zusätzlich.

### Überlastung von Ressourcen und Diensten

**Beschreibung:** KI-Agenten können verschiedene Werkzeuge und Dienste nutzen, um Aufgaben zu erfüllen. Angreifer können diese Fähigkeit nutzen, um Dienste durch eine hohe Anzahl von Anfragen über den KI-Agenten zu attackieren, was zu Systemausfällen oder hohen Kosten führen kann.

**Minderung:** Implementieren Sie Richtlinien, um die Anzahl der Anfragen, die ein KI-Agent an einen Dienst stellen kann, zu begrenzen. Die Begrenzung der Gesprächsrunden und der Anfragen an Ihren KI-Agenten ist eine weitere Methode, solche Angriffe zu verhindern.

### Vergiftung der Wissensbasis

**Beschreibung:** Diese Art von Angriff zielt nicht direkt auf den KI-Agenten ab, sondern auf die Wissensbasis und andere Dienste, die der KI-Agent verwendet. Dies kann das Korrumpieren der Daten oder Informationen beinhalten, die der KI-Agent zur Erfüllung einer Aufgabe nutzt, was zu verzerrten oder unbeabsichtigten Antworten an den Nutzer führt.

**Minderung:** Führen Sie regelmäßige Überprüfungen der Daten durch, die der KI-Agent in seinen Workflows verwendet. Stellen Sie sicher, dass der Zugang zu diesen Daten sicher ist und nur von vertrauenswürdigen Personen geändert wird, um diese Art von Angriff zu vermeiden.

### Kaskadierende Fehler

**Beschreibung:** KI-Agenten greifen auf verschiedene Werkzeuge und Dienste zu, um Aufgaben zu erfüllen. Fehler, die durch Angreifer verursacht werden, können dazu führen, dass auch andere Systeme, die mit dem KI-Agenten verbunden sind, ausfallen, wodurch sich der Angriff ausbreitet und die Fehlerbehebung erschwert wird.

**Minderung:** Eine Methode zur Vermeidung besteht darin, dass der KI-Agent in einer begrenzten Umgebung arbeitet, beispielsweise indem Aufgaben in einem Docker-Container ausgeführt werden, um direkte Systemangriffe zu verhindern. Die Erstellung von Fallback-Mechanismen und Wiederholungslogiken bei Systemfehlern ist eine weitere Möglichkeit, größere Systemausfälle zu vermeiden.

## Mensch in der Schleife (Human-in-the-Loop)

Eine weitere effektive Methode, vertrauenswürdige KI-Agentensysteme zu bauen, ist die Verwendung eines Mensch-in-der-Schleife-Ansatzes. Dies schafft einen Ablauf, bei dem Nutzer Feedback an die Agenten während des Laufs geben können. Nutzer fungieren im Grunde als Agenten in einem Multi-Agenten-System, indem sie die Ausführung genehmigen oder beenden.

![Mensch in der Schleife](../../../translated_images/de/human-in-the-loop.5f0068a678f62f4f.webp)

Hier ist ein Codeausschnitt, der mit dem Microsoft Agent Framework zeigt, wie dieses Konzept implementiert wird:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Erstellen Sie den Anbieter mit menschlicher Einbindung zur Genehmigung
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Erstellen Sie den Agenten mit einem menschlichen Genehmigungsschritt
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

Vertrauenswürdige KI-Agenten zu bauen, erfordert sorgfältiges Design, robuste Sicherheitsmaßnahmen und kontinuierliche Iteration. Durch die Implementierung strukturierter Meta-Prompting-Systeme, das Verständnis potenzieller Bedrohungen und die Anwendung von Gegenmaßnahmen können Entwickler KI-Agenten schaffen, die sowohl sicher als auch effektiv sind. Zusätzlich stellt der Ansatz Mensch-in-der-Schleife sicher, dass KI-Agenten mit den Bedürfnissen der Nutzer übereinstimmen und Risiken minimiert werden. Da KI sich weiterentwickelt, wird eine proaktive Haltung bezüglich Sicherheit, Datenschutz und ethischer Überlegungen entscheidend sein, um Vertrauen und Zuverlässigkeit in KI-gesteuerten Systemen zu fördern.

## Code-Beispiele

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Schritt-für-Schritt-Demonstration des Meta-Prompt-Systemnachrichten-Frameworks.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Genehmigungstore vor Aktionen, Risikostufung und Prüfprotokollierung für vertrauenswürdige Agenten.

### Haben Sie weitere Fragen zum Aufbau vertrauenswürdiger KI-Agenten?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Überblick über verantwortungsbewusste KI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Bewertung generativer KI-Modelle und KI-Anwendungen</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Sicherheits-Systemnachrichten</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Vorlage zur Risikoabschätzung</a>

## Vorherige Lektion

[Agentic RAG](../05-agentic-rag/README.md)

## Nächste Lektion

[Planungs-Designmuster](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->