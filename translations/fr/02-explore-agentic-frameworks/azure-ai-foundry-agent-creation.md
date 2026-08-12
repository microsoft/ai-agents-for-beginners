# Développement du service Microsoft Foundry Agent

Dans cet exercice, vous utilisez les outils Microsoft Foundry Agent Service dans le [portail Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) pour créer un agent de réservation de vols. L'agent pourra interagir avec les utilisateurs et fournir des informations sur les vols.

## Prérequis

Pour compléter cet exercice, vous avez besoin de :
1. Un compte Azure avec un abonnement actif. [Créez un compte gratuitement](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Vous devez avoir les autorisations pour créer un hub Microsoft Foundry ou en faire créer un pour vous.
    - Si votre rôle est Contributeur ou Propriétaire, vous pouvez suivre les étapes de ce tutoriel.

## Créez un hub Microsoft Foundry

> **Note :** Microsoft Foundry était auparavant connu sous le nom d'Azure AI Studio.

1. Suivez ces directives du billet de blog [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) pour créer un hub Microsoft Foundry.
2. Une fois votre projet créé, fermez les conseils affichés et examinez la page du projet dans le portail Microsoft Foundry, qui devrait ressembler à l'image suivante :

    ![Projet Microsoft Foundry](../../../translated_images/fr/azure-ai-foundry.88d0c35298348c2f.webp)

## Déployer un modèle

1. Dans le volet gauche de votre projet, dans la section **Mes ressources**, sélectionnez la page **Modèles + points de terminaison**.
2. Dans la page **Modèles + points de terminaison**, dans l’onglet **Déploiements de modèles**, dans le menu **+ Déployer un modèle**, sélectionnez **Déployer un modèle de base**.
3. Recherchez le modèle `gpt-5-mini` dans la liste, puis sélectionnez-le et confirmez.

    > **Note** : Réduire le TPM permet d’éviter une surutilisation du quota disponible dans l’abonnement que vous utilisez.

    ![Modèle déployé](../../../translated_images/fr/model-deployment.3749c53fb81e18fd.webp)

## Créer un agent

Maintenant que vous avez déployé un modèle, vous pouvez créer un agent. Un agent est un modèle d’IA conversationnelle qui peut être utilisé pour interagir avec les utilisateurs.

1. Dans le volet gauche de votre projet, dans la section **Créer et personnaliser**, sélectionnez la page **Agents**.
2. Cliquez sur **+ Créer un agent** pour créer un nouvel agent. Dans la boîte de dialogue **Configuration de l’agent** :
    - Entrez un nom pour l’agent, par exemple `FlightAgent`.
    - Assurez-vous que le déploiement du modèle `gpt-5-mini` que vous avez créé précédemment est sélectionné
    - Définissez les **Instructions** selon l'invite que vous voulez que l’agent suive. Voici un exemple :
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
> Pour une invite détaillée, vous pouvez consulter [ce dépôt](https://github.com/ShivamGoyal03/RoamMind) pour plus d’informations.
    
> De plus, vous pouvez ajouter une **Base de connaissances** et des **Actions** pour améliorer les capacités de l’agent afin de fournir plus d’informations et d’exécuter des tâches automatisées en fonction des demandes des utilisateurs. Pour cet exercice, vous pouvez ignorer ces étapes.
    
![Configuration de l’agent](../../../translated_images/fr/agent-setup.9bbb8755bf5df672.webp)

3. Pour créer un nouvel agent multi-IA, cliquez simplement sur **Nouvel agent**. L’agent nouvellement créé s’affichera alors sur la page Agents.


## Tester l’agent

Après avoir créé l’agent, vous pouvez le tester pour voir comment il répond aux requêtes des utilisateurs dans l’espace de jeu du portail Microsoft Foundry.

1. En haut du volet **Configuration** de votre agent, sélectionnez **Essayer dans l’espace de jeu**.
2. Dans le volet **Espace de jeu**, vous pouvez interagir avec l’agent en tapant des requêtes dans la fenêtre de chat. Par exemple, vous pouvez demander à l’agent de rechercher des vols de Seattle à New York le 28.

    > **Note** : L’agent peut ne pas fournir de réponses précises, car aucune donnée en temps réel n’est utilisée dans cet exercice. L’objectif est de tester la capacité de l’agent à comprendre et à répondre aux requêtes des utilisateurs en fonction des instructions fournies.

    ![Espace de jeu de l’agent](../../../translated_images/fr/agent-playground.dc146586de715010.webp)

3. Après avoir testé l’agent, vous pouvez le personnaliser davantage en ajoutant plus d’intentions, de données d’entraînement et d’actions pour améliorer ses capacités.

## Nettoyer les ressources

Une fois que vous avez terminé de tester l’agent, vous pouvez le supprimer pour éviter des coûts supplémentaires.
1. Ouvrez le [portail Azure](https://portal.azure.com) et consultez le contenu du groupe de ressources où vous avez déployé les ressources du hub utilisées dans cet exercice.
2. Dans la barre d’outils, sélectionnez **Supprimer le groupe de ressources**.
3. Entrez le nom du groupe de ressources et confirmez que vous souhaitez le supprimer.

## Ressources

- [Documentation Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Portail Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Prise en main de Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Fondamentaux des agents IA sur Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Discord Azure AI](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->