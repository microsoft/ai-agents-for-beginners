# Microsoft Foundry Agent Service Entwicklung

In dieser Übung verwenden Sie die Microsoft Foundry Agent Service-Tools im [Microsoft Foundry Portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst), um einen Agenten für Flugbuchungen zu erstellen. Der Agent wird mit Benutzern interagieren und Informationen zu Flügen bereitstellen können.

## Voraussetzungen

Um diese Übung abzuschließen, benötigen Sie Folgendes:
1. Ein Azure-Konto mit einem aktiven Abonnement. [Erstellen Sie ein kostenloses Konto](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Sie benötigen Berechtigungen, um einen Microsoft Foundry-Hub zu erstellen oder es muss einer für Sie erstellt werden.
    - Wenn Ihre Rolle Mitwirkender oder Besitzer ist, können Sie die Schritte in diesem Tutorial befolgen.

## Erstellen eines Microsoft Foundry-Hubs

> **Hinweis:** Microsoft Foundry war früher als Azure AI Studio bekannt.

1. Folgen Sie den Richtlinien aus dem [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) Blog-Beitrag zum Erstellen eines Microsoft Foundry-Hubs.
2. Nachdem Ihr Projekt erstellt wurde, schließen Sie alle angezeigten Tipps und überprüfen Sie die Projektseite im Microsoft Foundry-Portal, die in etwa wie das folgende Bild aussehen sollte:

    ![Microsoft Foundry Projekt](../../../translated_images/de/azure-ai-foundry.88d0c35298348c2f.webp)

## Modell bereitstellen

1. Wählen Sie im linken Bereich Ihres Projekts im Abschnitt **Meine Assets** die Seite **Modelle + Endpunkte** aus.
2. Auf der Seite **Modelle + Endpunkte** wählen Sie im Tab **Modellbereitstellungen** im Menü **+ Modell bereitstellen** die Option **Basis-Modell bereitstellen**.
3. Suchen Sie das `gpt-4.1-mini` Modell in der Liste, wählen Sie es aus und bestätigen Sie die Auswahl.

    > **Hinweis**: Das Reduzieren der TPM hilft, eine übermäßige Nutzung des im Abonnement verfügbaren Kontingents zu vermeiden.

    ![Modell bereitgestellt](../../../translated_images/de/model-deployment.3749c53fb81e18fd.webp)

## Erstellen eines Agenten

Jetzt, wo Sie ein Modell bereitgestellt haben, können Sie einen Agenten erstellen. Ein Agent ist ein konversationelles KI-Modell, das zur Interaktion mit Benutzern verwendet werden kann.

1. Wählen Sie im linken Bereich Ihres Projekts im Abschnitt **Erstellen & Anpassen** die Seite **Agenten** aus.
2. Klicken Sie auf **+ Agent erstellen**, um einen neuen Agenten zu erstellen. Im Dialogfeld **Agenten-Einrichtung**:
    - Geben Sie einen Namen für den Agenten ein, z. B. `FlightAgent`.
    - Stellen Sie sicher, dass die zuvor erstellte Modellbereitstellung `gpt-4.1-mini` ausgewählt ist.
    - Legen Sie die **Anweisungen** gemäß dem Prompt fest, dem der Agent folgen soll. Hier ist ein Beispiel:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Für einen detaillierten Prompt können Sie sich [dieses Repository](https://github.com/ShivamGoyal03/RoamMind) für weitere Informationen ansehen.
    
> Außerdem können Sie eine **Wissensdatenbank** und **Aktionen** hinzufügen, um die Fähigkeiten des Agenten zu erweitern, mehr Informationen bereitzustellen und automatisierte Aufgaben basierend auf Benutzeranfragen durchzuführen. Für diese Übung können Sie diese Schritte überspringen.
    
![Agenten-Einrichtung](../../../translated_images/de/agent-setup.9bbb8755bf5df672.webp)

3. Um einen neuen Multi-AI-Agenten zu erstellen, klicken Sie einfach auf **Neuer Agent**. Der neu erstellte Agent wird dann auf der Seite Agenten angezeigt.


## Testen des Agenten

Nach der Erstellung des Agenten können Sie ihn testen, um zu sehen, wie er auf Benutzeranfragen im Microsoft Foundry-Portal-Playground reagiert.

1. Wählen Sie oben im Bereich **Einrichtung** für Ihren Agenten **Im Playground testen** aus.
2. Im Bereich **Playground** können Sie mit dem Agenten interagieren, indem Sie Abfragen im Chatfenster eingeben. Zum Beispiel können Sie den Agenten bitten, Flüge von Seattle nach New York am 28. zu suchen.

    > **Hinweis**: Der Agent liefert möglicherweise keine genauen Antworten, da in dieser Übung keine Echtzeitdaten verwendet werden. Der Zweck ist es, die Fähigkeit des Agenten zu testen, Benutzeranfragen basierend auf den bereitgestellten Anweisungen zu verstehen und zu beantworten.

    ![Agenten-Playground](../../../translated_images/de/agent-playground.dc146586de715010.webp)

3. Nach dem Testen des Agenten können Sie ihn weiter anpassen, indem Sie weitere Intents, Trainingsdaten und Aktionen hinzufügen, um seine Fähigkeiten zu erweitern.

## Ressourcen bereinigen

Wenn Sie mit dem Testen des Agenten fertig sind, können Sie ihn löschen, um zusätzliche Kosten zu vermeiden.
1. Öffnen Sie das [Azure-Portal](https://portal.azure.com) und sehen Sie sich den Inhalt der Ressourcengruppe an, in der Sie die im Rahmen dieser Übung verwendeten Hub-Ressourcen bereitgestellt haben.
2. Wählen Sie in der Symbolleiste **Ressourcengruppe löschen** aus.
3. Geben Sie den Namen der Ressourcengruppe ein und bestätigen Sie, dass Sie sie löschen möchten.

## Ressourcen

- [Microsoft Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry Portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Erste Schritte mit Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Grundlagen von KI-Agenten auf Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->