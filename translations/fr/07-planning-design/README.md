<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43069833a0412210ad5c3cc93d9c2146",
  "translation_date": "2025-09-18T14:02:17+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "fr"
}
-->
[![Planification et Modèle de Conception](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.fr.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

# Planification et Conception

## Introduction

Cette leçon couvrira :

* Définir un objectif global clair et diviser une tâche complexe en tâches gérables.
* Utiliser des sorties structurées pour des réponses plus fiables et lisibles par machine.
* Appliquer une approche événementielle pour gérer des tâches dynamiques et des entrées inattendues.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous comprendrez :

* Comment identifier et définir un objectif global pour un agent IA, en s'assurant qu'il sait clairement ce qu'il doit accomplir.
* Comment décomposer une tâche complexe en sous-tâches gérables et les organiser dans une séquence logique.
* Comment équiper les agents des bons outils (par exemple, outils de recherche ou d'analyse de données), décider quand et comment les utiliser, et gérer les situations imprévues.
* Comment évaluer les résultats des sous-tâches, mesurer les performances et itérer sur les actions pour améliorer le résultat final.

## Définir l'objectif global et décomposer une tâche

![Définir les objectifs et les tâches](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.fr.png)

La plupart des tâches du monde réel sont trop complexes pour être abordées en une seule étape. Un agent IA a besoin d'un objectif concis pour guider sa planification et ses actions. Par exemple, considérez l'objectif :

    "Créer un itinéraire de voyage de 3 jours."

Bien qu'il soit simple à énoncer, il nécessite encore des précisions. Plus l'objectif est clair, mieux l'agent (et les collaborateurs humains) pourra se concentrer sur l'obtention du bon résultat, comme la création d'un itinéraire complet avec des options de vol, des recommandations d'hôtels et des suggestions d'activités.

### Décomposition des tâches

Les tâches larges ou complexes deviennent plus gérables lorsqu'elles sont divisées en sous-tâches orientées vers un objectif.
Pour l'exemple de l'itinéraire de voyage, vous pourriez décomposer l'objectif en :

* Réservation de vol
* Réservation d'hôtel
* Location de voiture
* Personnalisation

Chaque sous-tâche peut ensuite être prise en charge par des agents ou processus dédiés. Un agent pourrait se spécialiser dans la recherche des meilleures offres de vol, un autre dans les réservations d'hôtel, etc. Un agent coordinateur ou "en aval" peut ensuite compiler ces résultats en un itinéraire cohérent pour l'utilisateur final.

Cette approche modulaire permet également des améliorations progressives. Par exemple, vous pourriez ajouter des agents spécialisés pour les recommandations culinaires ou les suggestions d'activités locales et affiner l'itinéraire au fil du temps.

### Sortie structurée

Les modèles de langage avancés (LLMs) peuvent générer des sorties structurées (par exemple, JSON) qui sont plus faciles à analyser et à traiter par des agents ou services en aval. Cela est particulièrement utile dans un contexte multi-agents, où ces tâches peuvent être exécutées après réception de la sortie de planification. Consultez ceci pour un aperçu rapide.

Le snippet Python suivant démontre un agent de planification simple décomposant un objectif en sous-tâches et générant un plan structuré :

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
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
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Agent de planification avec orchestration multi-agents

Dans cet exemple, un agent routeur sémantique reçoit une demande utilisateur (par exemple, "J'ai besoin d'un plan d'hôtel pour mon voyage.").

Le planificateur :

* Reçoit le plan d'hôtel : Le planificateur prend le message de l'utilisateur et, sur la base d'un prompt système (incluant les détails des agents disponibles), génère un plan de voyage structuré.
* Liste les agents et leurs outils : Le registre d'agents contient une liste d'agents (par exemple, pour les vols, hôtels, locations de voiture et activités) ainsi que les fonctions ou outils qu'ils offrent.
* Route le plan vers les agents concernés : Selon le nombre de sous-tâches, le planificateur envoie soit directement le message à un agent dédié (pour des scénarios à tâche unique), soit coordonne via un gestionnaire de chat de groupe pour une collaboration multi-agents.
* Résume le résultat : Enfin, le planificateur résume le plan généré pour plus de clarté.

Le code Python suivant illustre ces étapes :

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

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Ce qui suit est la sortie du code précédent, que vous pouvez ensuite utiliser pour router vers `assigned_agent` et résumer le plan de voyage pour l'utilisateur final.

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

Un exemple de notebook avec le code précédent est disponible [ici](07-autogen.ipynb).

### Planification itérative

Certaines tâches nécessitent des allers-retours ou une re-planification, où le résultat d'une sous-tâche influence la suivante. Par exemple, si l'agent découvre un format de données inattendu lors de la réservation de vols, il pourrait devoir adapter sa stratégie avant de passer aux réservations d'hôtel.

De plus, les retours utilisateurs (par exemple, un humain décidant qu'il préfère un vol plus tôt) peuvent déclencher une re-planification partielle. Cette approche dynamique et itérative garantit que la solution finale s'aligne sur les contraintes du monde réel et les préférences évolutives de l'utilisateur.

Exemple de code :

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

Pour une planification plus complète, consultez Magnetic One pour résoudre des tâches complexes.

## Résumé

Dans cet article, nous avons examiné un exemple de création d'un planificateur capable de sélectionner dynamiquement les agents disponibles définis. La sortie du planificateur décompose les tâches et assigne les agents pour qu'elles soient exécutées. Il est supposé que les agents ont accès aux fonctions/outils nécessaires pour accomplir la tâche. En plus des agents, vous pouvez inclure d'autres modèles comme la réflexion, le résumé et le chat en rotation pour une personnalisation supplémentaire.

## Ressources supplémentaires

AutoGen Magnetic One - Un système multi-agents généraliste pour résoudre des tâches complexes et qui a obtenu des résultats impressionnants sur plusieurs benchmarks d'agents difficiles. Référence : . Dans cette implémentation, l'orchestrateur crée un plan spécifique à la tâche et délègue ces tâches aux agents disponibles. En plus de la planification, l'orchestrateur utilise également un mécanisme de suivi pour surveiller l'avancement de la tâche et re-planifier si nécessaire.

### Vous avez des questions sur le modèle de conception de planification ?

Rejoignez le [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Leçon précédente

[Créer des agents IA fiables](../06-building-trustworthy-agents/README.md)

## Leçon suivante

[Modèle de conception multi-agents](../08-multi-agent/README.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.