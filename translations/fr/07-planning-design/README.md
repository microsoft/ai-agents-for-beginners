[![Modèle de conception de planification](../../../translated_images/fr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Cliquez sur l'image ci-dessus pour regarder la vidéo de cette leçon)_

# Conception de la planification

## Introduction

Cette leçon couvrira

* Définir un objectif global clair et décomposer une tâche complexe en tâches gérables.
* Exploiter une sortie structurée pour des réponses plus fiables et lisibles par machine.
* Appliquer une approche pilotée par les événements pour gérer des tâches dynamiques et des entrées inattendues.

## Objectifs d'apprentissage

Après avoir suivi cette leçon, vous aurez une compréhension de :

* Identifier et définir un objectif global pour un agent IA, en s'assurant qu'il sait clairement ce qui doit être accompli.
* Décomposer une tâche complexe en sous-tâches gérables et les organiser dans une séquence logique.
* Équiper les agents des bons outils (par ex., outils de recherche ou d'analyse de données), décider quand et comment les utiliser, et gérer les situations inattendues qui surviennent.
* Évaluer les résultats des sous-tâches, mesurer les performances et itérer les actions pour améliorer le résultat final.

## Définir l'objectif global et décomposer une tâche

![Définition des objectifs et des tâches](../../../translated_images/fr/defining-goals-tasks.d70439e19e37c47a.webp)

Les tâches du monde réel sont généralement trop complexes pour être traitées en une seule étape. Un agent IA a besoin d'un objectif concis pour guider sa planification et ses actions. Par exemple, considérez l'objectif :

    "Générer un itinéraire de voyage de 3 jours."

Bien qu'il soit simple à énoncer, il nécessite encore des ajustements. Plus l'objectif est clair, mieux l'agent (et les collaborateurs humains) peuvent se concentrer sur l'obtention du bon résultat, comme la création d'un itinéraire complet avec des options de vol, des recommandations d'hôtel et des suggestions d'activités.

### Décomposition de la tâche

Les tâches volumineuses ou complexes deviennent plus gérables lorsqu'elles sont divisées en sous-tâches plus petites et orientées vers un objectif.
Pour l'exemple de l'itinéraire de voyage, vous pouvez décomposer l'objectif en :

* Réservation de vol
* Réservation d'hôtel
* Location de voiture
* Personnalisation

Chaque sous-tâche peut ensuite être traitée par des agents ou des processus dédiés. Un agent peut se spécialiser dans la recherche des meilleures offres de vol, un autre se concentrer sur les réservations d'hôtel, etc. Un agent coordonnateur ou « en aval » peut ensuite compiler ces résultats en un itinéraire cohérent pour l'utilisateur final.

Cette approche modulaire permet également des améliorations progressives. Par exemple, vous pourriez ajouter des agents spécialisés pour les recommandations alimentaires ou les suggestions d'activités locales et affiner l'itinéraire au fil du temps.

### Sortie structurée

Les grands modèles de langage (LLMs) peuvent générer des sorties structurées (par ex. JSON) qui sont plus faciles à analyser et à traiter pour les agents ou services en aval. Cela est particulièrement utile dans un contexte multi-agent, où nous pouvons exécuter ces tâches après réception du résultat de la planification.

La capture de code Python suivante montre un agent de planification simple qui décompose un objectif en sous-tâches et génère un plan structuré :

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modèle de sous-tâche de voyage
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # nous voulons attribuer la tâche à l'agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Définir le message de l'utilisateur
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Agent de planification avec orchestration multi-agent

Dans cet exemple, un agent de routage sémantique reçoit une requête utilisateur (par ex., « J'ai besoin d'un plan d'hôtel pour mon voyage. »).

Le planificateur fait ensuite :

* Reçoit le plan d'hôtel : Le planificateur prend le message de l'utilisateur et, sur la base d'un prompt système (incluant les détails des agents disponibles), génère un plan de voyage structuré.
* Énumère les agents et leurs outils : Le registre d'agents contient une liste d'agents (par ex., pour les vols, hôtels, locations de voiture et activités) ainsi que les fonctions ou outils qu'ils offrent.
* Route le plan vers les agents respectifs : Selon le nombre de sous-tâches, le planificateur envoie soit le message directement à un agent dédié (pour les scénarios à tâche unique), soit coordonne via un gestionnaire de chat de groupe pour la collaboration multi-agent.
* Résume le résultat : Enfin, le planificateur résume le plan généré pour plus de clarté.
L'exemple de code Python suivant illustre ces étapes :

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Modèle de sous-tâche de voyage

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Nous voulons attribuer la tâche à l'agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Créer le client

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Définir le message de l'utilisateur

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Afficher le contenu de la réponse après l'avoir chargé au format JSON

pprint(json.loads(response_content))
```

Ce qui suit est la sortie du code précédent et vous pouvez ensuite utiliser cette sortie structurée pour la router vers `assigned_agent` et résumer le plan de voyage pour l'utilisateur final.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Un notebook d'exemple contenant le code précédent est disponible [ici](07-python-agent-framework.ipynb).

### Planification itérative

Certaines tâches nécessitent des allers-retours ou une re-planification, où le résultat d'une sous-tâche influence la suivante. Par exemple, si l'agent découvre un format de données inattendu lors de la réservation des vols, il peut devoir adapter sa stratégie avant de passer aux réservations d'hôtel.

De plus, les retours utilisateur (par ex., un humain décidant qu'il préfère un vol plus tôt) peuvent déclencher une replanification partielle. Cette approche dynamique et itérative garantit que la solution finale s'aligne sur les contraintes réelles et les préférences évolutives de l'utilisateur.

ex. : code d'exemple

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. même que le code précédent et transmettre l'historique de l'utilisateur, le plan actuel

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. réplanifier et envoyer les tâches aux agents respectifs
```

Pour une planification plus complète, consultez Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">billet de blog</a> sur la résolution de tâches complexes.

## Résumé

Dans cet article, nous avons examiné un exemple montrant comment créer un planificateur capable de sélectionner dynamiquement les agents disponibles. La sortie du planificateur décompose les tâches et attribue les agents afin qu'elles puissent être exécutées. On suppose que les agents ont accès aux fonctions/outils nécessaires pour effectuer la tâche. Outre les agents, vous pouvez inclure d'autres modèles tels que la réflexion, le résumé et le chat en rotation (round robin) pour personnaliser davantage.

## Ressources supplémentaires

Magentic One - Un système multi-agent généraliste pour résoudre des tâches complexes qui a obtenu des résultats impressionnants sur de nombreux benchmarks agentiques exigeants. Référence : <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Dans cette implémentation, l'orchestrateur crée des plans spécifiques aux tâches et délègue ces tâches aux agents disponibles. En plus de la planification, l'orchestrateur utilise également un mécanisme de suivi pour surveiller l'avancement de la tâche et re-planifier si nécessaire.

### Vous avez d'autres questions sur le modèle de conception de la planification ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Leçon précédente

[Création d'agents IA fiables](../06-building-trustworthy-agents/README.md)

## Leçon suivante

[Modèle de conception multi-agent](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avis de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'être précis, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant foi. Pour toute information critique, il est recommandé de recourir à une traduction professionnelle effectuée par un traducteur humain. Nous ne pouvons être tenus responsables des malentendus ou des erreurs d'interprétation résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->