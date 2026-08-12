# Sviluppo del Servizio Microsoft Foundry Agent

In questo esercizio, utilizzi gli strumenti del Servizio Microsoft Foundry Agent nel [portale Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) per creare un agente per la Prenotazione dei Voli. L'agente sarà in grado di interagire con gli utenti e fornire informazioni sui voli.

## Prerequisiti

Per completare questo esercizio, ti servono i seguenti elementi:
1. Un account Azure con una sottoscrizione attiva. [Crea un account gratuitamente](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Devi avere i permessi per creare un hub Microsoft Foundry o farselo creare da qualcuno.
    - Se il tuo ruolo è Collaboratore o Proprietario, puoi seguire i passaggi di questo tutorial.

## Crea un hub Microsoft Foundry

> **Nota:** Microsoft Foundry era precedentemente noto come Azure AI Studio.

1. Segui queste linee guida dal post del blog di [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) per creare un hub Microsoft Foundry.
2. Quando il tuo progetto è creato, chiudi eventuali suggerimenti che vengono mostrati e rivedi la pagina del progetto nel portale Microsoft Foundry, che dovrebbe apparire simile all'immagine seguente:

    ![Microsoft Foundry Project](../../../translated_images/it/azure-ai-foundry.88d0c35298348c2f.webp)

## Distribuisci un modello

1. Nel pannello a sinistra per il tuo progetto, nella sezione **I miei asset**, seleziona la pagina **Modelli + endpoint**.
2. Nella pagina **Modelli + endpoint**, nella scheda **Distribuzioni modello**, nel menu **+ Distribuisci modello**, seleziona **Distribuisci modello base**.
3. Cerca il modello `gpt-5-mini` nella lista, quindi selezionalo e conferma.

    > **Nota**: Ridurre il TPM aiuta a evitare di superare la quota disponibile nella sottoscrizione che stai usando.

    ![Model Deployed](../../../translated_images/it/model-deployment.3749c53fb81e18fd.webp)

## Crea un agente

Ora che hai distribuito un modello, puoi creare un agente. Un agente è un modello AI conversazionale che può essere usato per interagire con gli utenti.

1. Nel pannello a sinistra per il tuo progetto, nella sezione **Costruisci e Personalizza**, seleziona la pagina **Agenti**.
2. Clicca su **+ Crea agente** per creare un nuovo agente. Nel riquadro di dialogo **Configurazione agente**:
    - Inserisci un nome per l'agente, come `FlightAgent`.
    - Assicurati che sia selezionata la distribuzione del modello `gpt-5-mini` creata in precedenza
    - Imposta le **Istruzioni** secondo il prompt che vuoi far seguire all'agente. Ecco un esempio:
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
> Per un prompt dettagliato, puoi dare un'occhiata a [questo repository](https://github.com/ShivamGoyal03/RoamMind) per maggiori informazioni.
    
> Inoltre, puoi aggiungere una **Base di Conoscenza** e **Azioni** per migliorare le capacità dell'agente di fornire più informazioni ed eseguire compiti automatizzati basati sulle richieste dell'utente. Per questo esercizio, puoi saltare questi passaggi.
    
![Agent Setup](../../../translated_images/it/agent-setup.9bbb8755bf5df672.webp)

3. Per creare un nuovo agente multi-AI, clicca semplicemente su **Nuovo Agente**. L'agente appena creato sarà quindi visualizzato nella pagina Agenti.


## Testa l'agente

Dopo aver creato l'agente, puoi testarlo per vedere come risponde alle query degli utenti nel playground del portale Microsoft Foundry.

1. In cima al pannello **Configurazione** per il tuo agente, seleziona **Prova nel playground**.
2. Nel pannello **Playground**, puoi interagire con l'agente digitando query nella finestra di chat. Ad esempio, puoi chiedere all'agente di cercare voli da Seattle a New York per il 28.

    > **Nota**: L'agente potrebbe non fornire risposte accurate, poiché in questo esercizio non vengono utilizzati dati in tempo reale. Lo scopo è testare la capacità dell'agente di comprendere e rispondere alle domande degli utenti basandosi sulle istruzioni fornite.

    ![Agent Playground](../../../translated_images/it/agent-playground.dc146586de715010.webp)

3. Dopo aver testato l'agente, puoi personalizzarlo ulteriormente aggiungendo più intenti, dati di addestramento e azioni per migliorarne le capacità.

## Pulizia delle risorse

Quando hai finito di testare l'agente, puoi eliminarlo per evitare costi aggiuntivi.
1. Apri il [portale Azure](https://portal.azure.com) e visualizza il contenuto del gruppo di risorse dove hai distribuito le risorse hub usate in questo esercizio.
2. Nella barra degli strumenti, seleziona **Elimina gruppo di risorse**.
3. Inserisci il nome del gruppo di risorse e conferma di volerlo eliminare.

## Risorse

- [Documentazione Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portale Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Introduzione a Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fondamenti degli agenti AI su Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Discord Azure AI](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->