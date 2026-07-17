[![Explorer les cadres d'agents IA](../../../translated_images/fr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

# Explorer les cadres d'agents IA

Les cadres d'agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion d'agents IA. Ces cadres fournissent aux développeurs des composants prêts à l'emploi, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces cadres aident les développeurs à se concentrer sur les aspects uniques de leurs applications en fournissant des approches standardisées aux défis courants du développement d'agents IA. Ils améliorent la scalabilité, l'accessibilité et l'efficacité dans la construction de systèmes IA.

## Introduction 

Cette leçon couvrira :

- Qu'est-ce que les cadres d'agents IA et qu'autorisent-ils les développeurs à accomplir ?
- Comment les équipes peuvent-elles utiliser ces cadres pour prototyper rapidement, itérer et améliorer les capacités de leurs agents ?
- Quelles sont les différences entre les cadres et outils créés par Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> et le <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ?
- Puis-je intégrer directement mes outils existants de l'écosystème Azure, ou ai-je besoin de solutions autonomes ?
- Qu'est-ce que Microsoft Foundry Agent Service et comment cela m'aide-t-il ?

## Objectifs d'apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des cadres d'agents IA dans le développement d'IA.
- Comment tirer parti des cadres d'agents IA pour construire des agents intelligents.
- Les capacités clés autorisées par les cadres d'agents IA.
- Les différences entre le Microsoft Agent Framework et Microsoft Foundry Agent Service.

## Qu'est-ce que les cadres d'agents IA et que permettent-ils aux développeurs de faire ?

Les cadres d'IA traditionnels peuvent vous aider à intégrer l'IA dans vos applications et à améliorer ces applications de la manière suivante :

- **Personnalisation** : L'IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations personnalisées, du contenu et des expériences.
Exemple : Les services de streaming comme Netflix utilisent l'IA pour suggérer des films et séries en fonction de l'historique de visionnage, améliorant l'engagement et la satisfaction des utilisateurs.
- **Automatisation et Efficacité** : L'IA peut automatiser les tâches répétitives, rationaliser les flux de travail, et améliorer l'efficacité opérationnelle.
Exemple : Les applications de service client utilisent des chatbots alimentés par l'IA pour gérer les demandes courantes, réduisant les temps de réponse et libérant les agents humains pour des questions plus complexes.
- **Expérience Utilisateur Améliorée** : L'IA peut améliorer l'expérience utilisateur globale en offrant des fonctionnalités intelligentes telles que la reconnaissance vocale, le traitement du langage naturel et la prédiction de texte.
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l'IA pour comprendre et répondre aux commandes vocales, facilitant l'interaction des utilisateurs avec leurs appareils.

### Tout cela semble parfait, n'est-ce pas ? Alors pourquoi avons-nous besoin du cadre des agents IA ?

Les cadres d'agents IA représentent quelque chose de plus que de simples cadres IA. Ils sont conçus pour permettre la création d'agents intelligents capables d'interagir avec les utilisateurs, d'autres agents et l'environnement pour atteindre des objectifs spécifiques. Ces agents peuvent manifester un comportement autonome, prendre des décisions et s'adapter aux conditions changeantes. Regardons quelques capacités clés permis par les cadres d'agents IA :

- **Collaboration et Coordination des Agents** : Permettre la création de plusieurs agents IA pouvant travailler ensemble, communiquer et coordonner pour résoudre des tâches complexes.
- **Automatisation et Gestion des Tâches** : Fournir des mécanismes d'automatisation des workflows multi-étapes, de délégation des tâches et de gestion dynamique des tâches entre agents.
- **Compréhension Contextuelle et Adaptation** : Équiper les agents de la capacité à comprendre le contexte, s'adapter aux environnements changeants et prendre des décisions basées sur des informations en temps réel.

En résumé, les agents vous permettent d'en faire plus, d'élever l'automatisation à un nouveau niveau, de créer des systèmes plus intelligents capables de s'adapter et d'apprendre de leur environnement.

## Comment prototyper rapidement, itérer et améliorer les capacités de l’agent ?

C'est un domaine en évolution rapide, mais il y a des éléments communs à la plupart des cadres d'agents IA qui vous aident à prototyper et itérer rapidement, notamment des composants modulaires, des outils collaboratifs et un apprentissage en temps réel. Examinons-les :

- **Utiliser des Composants Modulaires** : Les SDK d'IA offrent des composants pré-construits tels que connecteurs AI et mémoire, appels de fonctions via langage naturel ou plugins code, modèles de prompts, et plus encore.
- **Profiter des Outils Collaboratifs** : Concevoir des agents avec des rôles et tâches spécifiques, leur permettant de tester et affiner des flux collaboratifs.
- **Apprendre en Temps Réel** : Implémenter des boucles de rétroaction où les agents apprennent des interactions et ajustent dynamiquement leur comportement.

### Utiliser des Composants Modulaires

Les SDK comme le Microsoft Agent Framework offrent des composants pré-construits tels que connecteurs IA, définitions d'outils et gestion d'agents.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent rapidement assembler ces composants pour créer un prototype fonctionnel sans repartir de zéro, permettant une expérimentation et une itération rapides.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un parseur pré-construit pour extraire des informations des entrées utilisateurs, un module mémoire pour stocker et récupérer des données, et un générateur de prompt pour interagir avec les utilisateurs, le tout sans avoir à construire ces composants vous-même.

**Exemple de code**. Regardons un exemple de l’utilisation du Microsoft Agent Framework avec `FoundryChatClient` pour que le modèle réponde aux entrées utilisateurs avec appel d’outils :

``` python
# Exemple Python du cadre Microsoft Agent

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Définir une fonction d'outil d'exemple pour réserver un voyage
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Exemple de sortie : Votre vol pour New York le 1er janvier 2025 a été réservé avec succès. Bon voyage ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ce que vous voyez dans cet exemple, c'est comment tirer parti d'un parseur pré-construit pour extraire des informations clés des entrées utilisateurs, telles que l'origine, la destination et la date d'une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Profiter des Outils Collaboratifs

Des cadres comme le Microsoft Agent Framework facilitent la création de plusieurs agents pouvant collaborer.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et tâches spécifiques, leur permettant de tester et perfectionner des flux collaboratifs et d'améliorer l'efficacité globale du système.

**Comment cela fonctionne en pratique** : Vous pouvez créer une équipe d'agents où chaque agent a une fonction spécialisée, telle que la récupération de données, l'analyse ou la prise de décision. Ces agents peuvent communiquer et partager des informations pour atteindre un objectif commun, comme répondre à une demande utilisateur ou accomplir une tâche.

**Exemple de code (Microsoft Agent Framework)** :

```python
# Création de plusieurs agents qui travaillent ensemble en utilisant le Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent de récupération de données
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent d'analyse des données
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Exécuter les agents en séquence sur une tâche
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce que vous voyez dans le code précédent, c’est comment créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent exécute une fonction spécifique, et la tâche est accomplie en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous pouvez améliorer l’efficacité et les performances des tâches.

### Apprendre en Temps Réel

Les cadres avancés offrent des capacités de compréhension contextuelle en temps réel et d’adaptation.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent mettre en œuvre des boucles de rétroaction où les agents apprennent des interactions et ajustent dynamiquement leur comportement, conduisant à une amélioration continue et un affinement des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours utilisateurs, les données environnementales et les résultats des tâches pour mettre à jour leur base de connaissances, ajuster leurs algorithmes décisionnels et améliorer leurs performances dans le temps. Ce processus d'apprentissage itératif permet aux agents de s’adapter aux conditions changeantes et aux préférences des utilisateurs, augmentant l’efficacité globale du système.

## Quelles sont les différences entre Microsoft Agent Framework et Microsoft Foundry Agent Service ?

Il existe plusieurs manières de comparer ces approches, mais examinons quelques différences clés en termes de conception, capacités et cas d’usage ciblés :

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework fournit un SDK épuré pour construire des agents IA via `FoundryChatClient`. Il permet aux développeurs de créer des agents qui exploitent les modèles Azure OpenAI avec appels d’outils intégrés, gestion de conversation et sécurité de niveau entreprise via l’identité Azure.

**Cas d'utilisation** : Construction d’agents IA prêts pour la production avec utilisation d’outils, workflows multi-étapes et scénarios d’intégration entreprise.

Voici quelques concepts clés fondamentaux du Microsoft Agent Framework :

- **Agents**. Un agent est créé via `FoundryChatClient` et configuré avec un nom, instructions et outils. L’agent peut :
  - **Traiter les messages utilisateur** et générer des réponses en utilisant les modèles Azure OpenAI.
  - **Appeler des outils** automatiquement selon le contexte de la conversation.
  - **Maintenir l'état de la conversation** sur plusieurs interactions.

  Voici un extrait de code montrant comment créer un agent :

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Outils**. Le cadre supporte la définition d’outils comme fonctions Python que l’agent peut invoquer automatiquement. Les outils sont enregistrés lors de la création de l’agent :

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordination Multi-Agent**. Vous pouvez créer plusieurs agents avec différentes spécialisations et coordonner leur travail :

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Intégration Azure Identity**. Le cadre utilise `AzureCliCredential` (ou `DefaultAzureCredential`) pour une authentification sécurisée sans clé, éliminant la gestion directe des clés API.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service est une nouveauté introduite à Microsoft Ignite 2024. Il permet le développement et le déploiement d’agents IA avec des modèles plus flexibles, notamment en appelant directement des LLM open source comme Llama 3, Mistral et Cohere.

Microsoft Foundry Agent Service offre des mécanismes de sécurité d’entreprise renforcés et des méthodes de stockage des données, le rendant adapté aux applications d’entreprise.

Il fonctionne nativement avec Microsoft Agent Framework pour créer et déployer des agents.

Ce service est actuellement en préversion publique et supporte Python et C# pour construire les agents.

En utilisant le SDK Python Microsoft Foundry Agent Service, on peut créer un agent avec un outil défini par l'utilisateur :

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Définir les fonctions de l'outil
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Concepts fondamentaux

Microsoft Foundry Agent Service possède les concepts clés suivants :

- **Agent**. Microsoft Foundry Agent Service s’intègre à Microsoft Foundry. Dans Microsoft Foundry, un agent IA agit comme un microservice "intelligent" pouvant répondre aux questions (RAG), exécuter des actions ou automatiser complètement les workflows. Il réalise cela en combinant la puissance des modèles d’IA générative avec des outils permettant d’accéder et d’interagir avec des sources de données réelles. Voici un exemple d’agent :

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dans cet exemple, un agent est créé avec le modèle `gpt-4.1-mini`, un nom `my-agent` et des instructions `You are helpful agent`. L'agent est équipé d'outils et de ressources pour effectuer des tâches d'interprétation de code.

- **Fil de discussion et messages**. Le fil est un autre concept important. Il représente une conversation ou une interaction entre un agent et un utilisateur. Les fils peuvent être utilisés pour suivre le progrès d'une conversation, stocker des informations contextuelles et gérer l'état de l'interaction. Voici un exemple de fil :

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Demander à l'agent d'effectuer un travail sur le fil
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Récupérer et enregistrer tous les messages pour voir la réponse de l'agent
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Dans le code précédent, un fil est créé. Puis, un message est envoyé au fil. En appelant `create_and_process_run`, l’agent est invité à effectuer un travail sur le fil. Enfin, les messages sont récupérés et enregistrés pour voir la réponse de l’agent. Les messages indiquent le progrès de la conversation entre l’utilisateur et l’agent. Il est aussi important de comprendre que les messages peuvent être de différents types tels que texte, image ou fichier, résultant du travail des agents, par exemple une image ou une réponse textuelle. En tant que développeur, vous pouvez alors utiliser ces informations pour traiter davantage la réponse ou la présenter à l’utilisateur.

- **S’intègre avec Microsoft Agent Framework**. Microsoft Foundry Agent Service fonctionne parfaitement avec Microsoft Agent Framework, ce qui signifie que vous pouvez construire des agents via `FoundryChatClient` et les déployer via le service Agent pour des scénarios de production.

**Cas d'utilisation** : Microsoft Foundry Agent Service est conçu pour des applications d'entreprise nécessitant un déploiement d’agents IA sécurisé, scalable et flexible.

## Quelle est la différence entre ces approches ?
 
Il semble y avoir un chevauchement, mais il existe des différences clés en termes de conception, capacités et cas d’usage ciblés :
 
- **Microsoft Agent Framework (MAF)** : est un SDK prêt pour la production pour construire des agents IA. Il fournit une API épurée pour créer des agents avec appels d’outils, gestion de conversation et intégration de l’identité Azure.
- **Microsoft Foundry Agent Service** : est une plateforme et un service de déploiement dans Microsoft Foundry pour les agents. Il offre une connectivité intégrée à des services comme Azure OpenAI, Azure AI Search, Bing Search et l’exécution de code.
 
Vous n’êtes toujours pas sûr du choix ?

### Cas d’utilisation
 
Voyons si nous pouvons vous aider en passant en revue quelques cas d’usage courants :
 
> Q : Je construis des applications d’agents IA en production et souhaite démarrer rapidement
>

> R : Microsoft Agent Framework est un excellent choix. Il offre une API simple et “Pythonique” via `FoundryChatClient` qui vous permet de définir des agents avec outils et instructions en quelques lignes de code.

> Q : J’ai besoin d’un déploiement de niveau entreprise avec des intégrations Azure comme Search et l’exécution de code
>
> R : Microsoft Foundry Agent Service est le mieux adapté. C’est un service plateforme fournissant des capacités intégrées pour de multiples modèles, Azure AI Search, Bing Search et Azure Functions. Il facilite la création des agents dans le Portail Foundry et leur déploiement à grande échelle.
 
> Q : Je suis encore confus, donnez-moi juste une option
>
> R : Commencez avec Microsoft Agent Framework pour construire vos agents, puis utilisez Microsoft Foundry Agent Service lorsque vous devez déployer et faire évoluer vos agents en production. Cette approche vous permet d’itérer rapidement sur la logique de votre agent tout en gardant un chemin clair vers le déploiement entreprise.
 
Résumons les différences clés dans un tableau :

| Cadre | Focus | Concepts Clés | Cas d’Usage |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agent épuré avec appels d’outils | Agents, Outils, Identité Azure | Construire des agents IA, usage d’outils, workflows multi-étapes |
| Microsoft Foundry Agent Service | Modèles flexibles, sécurité entreprise, génération de code, appels d’outils | Modularité, Collaboration, Orchestration des processus | Déploiement sécurisé, scalable et flexible d’agents IA |

## Puis-je intégrer directement mes outils existants de l’écosystème Azure, ou ai-je besoin de solutions autonomes ?


La réponse est oui, vous pouvez intégrer vos outils existants de l'écosystème Azure directement avec Microsoft Foundry Agent Service en particulier, car il a été conçu pour fonctionner de manière transparente avec d'autres services Azure. Vous pouvez par exemple intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration approfondie avec Microsoft Foundry.

Le Microsoft Agent Framework s'intègre aussi aux services Azure via `FoundryChatClient` et l'identité Azure, vous permettant d'appeler directement les services Azure depuis vos outils d'agents.

## Exemples de codes

- Python : [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python : [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET : [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Vous avez d'autres questions sur les Frameworks d’Agents IA ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les Agents IA.

## Références

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Leçon précédente

[Introduction aux Agents IA et Cas d’Utilisation des Agents](../01-intro-to-ai-agents/README.md)

## Leçon suivante

[Comprendre les Modèles de Conception Agentique](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->