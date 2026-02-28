[![Exploring AI Agent Frameworks](../../../translated_images/fr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Cliquez sur l’image ci-dessus pour visionner la vidéo de cette leçon)_

# Explorer les frameworks d’agents IA

Les frameworks d’agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion d’agents IA. Ces frameworks fournissent aux développeurs des composants préconstruits, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces frameworks aident les développeurs à se concentrer sur les aspects uniques de leurs applications en offrant des approches standardisées aux défis courants dans le développement d’agents IA. Ils améliorent la scalabilité, l’accessibilité et l’efficacité dans la construction de systèmes IA.

## Introduction 

Cette leçon couvrira :

- Qu’est-ce que les frameworks d’agents IA et qu’est-ce qu’ils permettent aux développeurs de réaliser ?
- Comment les équipes peuvent-elles utiliser ces frameworks pour prototyper rapidement, itérer et améliorer les capacités de leur agent ?
- Quelles sont les différences entre les frameworks et outils créés par Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> et le <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ?
- Puis-je intégrer directement mes outils existants de l’écosystème Azure, ou ai-je besoin de solutions autonomes ?
- Qu’est-ce que le service Azure AI Agents et comment cela m’aide-t-il ?

## Objectifs d’apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des frameworks d’agents IA dans le développement IA.
- Comment exploiter les frameworks d’agents IA pour construire des agents intelligents.
- Les capacités clés offertes par les frameworks d’agents IA.
- Les différences entre le Microsoft Agent Framework et le Azure AI Agent Service.

## Qu’est-ce que les frameworks d’agents IA et qu’est-ce qu’ils permettent aux développeurs de faire ?

Les frameworks IA traditionnels peuvent vous aider à intégrer l’IA dans vos applications et à améliorer ces applications de la manière suivante :

- **Personnalisation** : L’IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations, contenus et expériences personnalisés.  
Exemple : Les services de streaming comme Netflix utilisent l’IA pour suggérer des films et séries en fonction de l’historique de visionnage, augmentant ainsi l’engagement et la satisfaction des utilisateurs.  
- **Automatisation et efficacité** : L’IA peut automatiser les tâches répétitives, rationaliser les flux de travail et améliorer l’efficacité opérationnelle.  
Exemple : Les applications de service client utilisent des chatbots alimentés par l’IA pour gérer les questions courantes, réduisant les temps de réponse et libérant les agents humains pour les problèmes plus complexes.  
- **Expérience utilisateur améliorée** : L’IA peut améliorer l’expérience globale utilisateur en fournissant des fonctionnalités intelligentes telles que la reconnaissance vocale, le traitement du langage naturel et la saisie prédictive.  
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l’IA pour comprendre et répondre aux commandes vocales, facilitant l’interaction des utilisateurs avec leurs appareils.

### Cela semble parfait, alors pourquoi avons-nous besoin des frameworks d’agents IA ?

Les frameworks d’agents IA représentent quelque chose de plus que de simples frameworks IA. Ils sont conçus pour permettre la création d’agents intelligents capables d’interagir avec les utilisateurs, d’autres agents, et l’environnement afin d’atteindre des objectifs spécifiques. Ces agents peuvent adopter un comportement autonome, prendre des décisions et s’adapter aux conditions changeantes. Voici quelques capacités clés offertes par les frameworks d’agents IA :

- **Collaboration et coordination entre agents** : Permet la création de plusieurs agents IA pouvant travailler ensemble, communiquer et se coordonner pour résoudre des tâches complexes.  
- **Automatisation et gestion des tâches** : Fournit des mécanismes pour automatiser des workflows multi-étapes, la délégation de tâches et la gestion dynamique des tâches entre agents.  
- **Compréhension contextuelle et adaptation** : Équipe les agents de la capacité à comprendre le contexte, à s’adapter aux environnements changeants et à prendre des décisions basées sur des informations en temps réel.

En résumé, les agents vous permettent d’en faire plus, de porter l’automatisation à un niveau supérieur, de créer des systèmes plus intelligents capables de s’adapter et d’apprendre de leur environnement.

## Comment prototyper rapidement, itérer et améliorer les capacités de l’agent ?

C’est un domaine en constante évolution, mais certains éléments communs à la plupart des frameworks d’agents IA peuvent vous aider à prototyper et itérer rapidement, à savoir les composants modulaires, les outils collaboratifs et l’apprentissage en temps réel. Regardons cela de plus près :

- **Utiliser des composants modulaires** : Les SDK IA offrent des composants préconstruits tels que des connecteurs IA et mémoire, l’appel de fonctions via langage naturel ou plugins code, des modèles de prompts, et plus encore.  
- **Exploiter les outils collaboratifs** : Concevez des agents avec des rôles et tâches spécifiques, leur permettant de tester et affiner des workflows collaboratifs.  
- **Apprendre en temps réel** : Implémentez des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement dynamiquement.

### Utiliser des composants modulaires

Les SDK comme le Microsoft Agent Framework offrent des composants préconstruits tels que des connecteurs IA, des définitions d’outils et la gestion des agents.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent assembler rapidement ces composants pour créer un prototype fonctionnel sans partir de zéro, permettant une expérimentation et une itération rapide.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un analyseur préconstruit pour extraire des informations à partir des saisies utilisateur, un module mémoire pour stocker et récupérer des données, et un générateur de prompts pour interagir avec les utilisateurs, le tout sans devoir construire ces composants vous-même.

**Exemple de code**. Regardons un exemple montrant comment utiliser le Microsoft Agent Framework avec `AzureAIProjectAgentProvider` pour faire répondre le modèle à une saisie utilisateur avec appel d’outils :

``` python
# Exemple Python du Microsoft Agent Framework

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Définir une fonction d'exemple d'outil pour réserver un voyage
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
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

Ce que vous voyez dans cet exemple est comment exploiter un analyseur préconstruit pour extraire les informations clés à partir de la saisie utilisateur, telles que l’origine, la destination, et la date d’une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Exploiter les outils collaboratifs

Les frameworks comme le Microsoft Agent Framework facilitent la création de plusieurs agents qui peuvent travailler ensemble.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et des tâches spécifiques, leur permettant de tester et affiner des workflows collaboratifs et d’améliorer l’efficacité globale du système.

**Comment cela fonctionne en pratique** : Vous pouvez créer une équipe d’agents où chaque agent a une fonction spécialisée, comme la récupération de données, l’analyse ou la prise de décision. Ces agents peuvent communiquer et partager des informations pour atteindre un objectif commun, comme répondre à une requête utilisateur ou réaliser une tâche.

**Exemple de code (Microsoft Agent Framework)** :

```python
# Créer plusieurs agents qui travaillent ensemble en utilisant le Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent de récupération de données
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent d'analyse de données
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Exécuter les agents en séquence sur une tâche
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ce que vous voyez dans ce code précédent, c’est comment créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent accomplit une fonction spécifique, et la tâche est exécutée en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous améliorez l’efficacité et la performance des tâches.

### Apprendre en temps réel

Les frameworks avancés offrent des capacités de compréhension contextuelle et d’adaptation en temps réel.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent implémenter des boucles de rétroaction où les agents apprennent des interactions et ajustent dynamiquement leur comportement, conduisant à une amélioration continue et à un affinage des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours utilisateurs, les données environnementales et les résultats de tâches pour mettre à jour leur base de connaissances, ajuster les algorithmes de décision et améliorer leur performance au fil du temps. Ce processus d’apprentissage itératif permet aux agents de s’adapter aux conditions changeantes et aux préférences des utilisateurs, augmentant ainsi l’efficacité globale du système.

## Quelles sont les différences entre le Microsoft Agent Framework et l’Azure AI Agent Service ?

Il existe plusieurs façons de comparer ces approches, mais regardons quelques différences clés en termes de conception, capacités et cas d’usage ciblés :

## Microsoft Agent Framework (MAF)

Le Microsoft Agent Framework fournit un SDK simplifié pour construire des agents IA en utilisant `AzureAIProjectAgentProvider`. Il permet aux développeurs de créer des agents qui exploitent les modèles Azure OpenAI avec appel d’outils intégré, gestion de la conversation et sécurité de niveau entreprise grâce à l’identité Azure.

**Cas d’usage** : Construire des agents IA prêts pour la production avec utilisation d’outils, workflows multi-étapes, et scénarios d’intégration entreprise.

Voici quelques concepts clés du Microsoft Agent Framework :

- **Agents**. Un agent est créé via `AzureAIProjectAgentProvider` et configuré avec un nom, des instructions et des outils. L’agent peut :  
  - **Traiter les messages utilisateurs** et générer des réponses avec les modèles Azure OpenAI.  
  - **Appeler automatiquement des outils** en fonction du contexte de la conversation.  
  - **Maintenir l’état de la conversation** à travers plusieurs interactions.

  Voici un extrait de code montrant comment créer un agent :

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Outils**. Le framework prend en charge la définition d’outils sous forme de fonctions Python que l’agent peut invoquer automatiquement. Les outils sont enregistrés lors de la création de l’agent :

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Coordination multi-agent**. Vous pouvez créer plusieurs agents avec des spécialisations différentes et coordonner leur travail :

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Intégration Azure Identity**. Le framework utilise `AzureCliCredential` (ou `DefaultAzureCredential`) pour une authentification sécurisée sans clé, éliminant le besoin de gérer les clés API directement.

## Azure AI Agent Service

Azure AI Agent Service est une addition plus récente, annoncée à Microsoft Ignite 2024. Il permet le développement et déploiement d’agents IA avec des modèles plus flexibles, comme l’appel direct de LLM open source tels que Llama 3, Mistral, et Cohere.

Azure AI Agent Service offre des mécanismes de sécurité entreprise renforcés et des méthodes de stockage des données, le rendant adapté aux applications d’entreprise.

Il fonctionne directement avec le Microsoft Agent Framework pour construire et déployer des agents.

Ce service est actuellement en aperçu public et supporte Python et C# pour la construction d’agents.

Avec le SDK Python de Azure AI Agent Service, nous pouvons créer un agent avec un outil défini par l’utilisateur :

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Définir les fonctions utilitaires
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
        model="gpt-4o-mini",
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

### Concepts clés

Azure AI Agent Service a les concepts suivants :

- **Agent**. Azure AI Agent Service s’intègre avec Microsoft Foundry. Dans AI Foundry, un agent IA agit comme un microservice « intelligent » pouvant répondre à des questions (RAG), exécuter des actions ou automatiser entièrement des workflows. Il combine la puissance des modèles IA génératifs avec des outils permettant d’accéder et d’interagir avec des sources de données réelles. Voici un exemple d’agent :

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dans cet exemple, un agent est créé avec le modèle `gpt-4o-mini`, un nom `my-agent` et les instructions `You are helpful agent`. L’agent est équipé d’outils et ressources pour effectuer des tâches d’interprétation de code.

- **Fil de discussion et messages**. Le fil est un autre concept important. Il représente une conversation ou interaction entre un agent et un utilisateur. Les fils peuvent servir à suivre la progression d’une conversation, stocker des informations contextuelles et gérer l’état de l’interaction. Voici un exemple de fil :

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Dans ce code précédent, un fil est créé. Ensuite, un message est envoyé dans ce fil. En appelant `create_and_process_run`, on demande à l’agent d’exécuter un travail dans le fil. Enfin, les messages sont récupérés et enregistrés pour voir la réponse de l’agent. Les messages indiquent la progression de la conversation entre l’utilisateur et l’agent. Il est aussi important de comprendre que les messages peuvent être de différents types, tels que texte, image ou fichier, c’est-à-dire que le travail de l’agent a pu générer, par exemple, une image ou une réponse textuelle. En tant que développeur, vous pouvez alors utiliser cette information pour traiter davantage la réponse ou la présenter à l’utilisateur.

- **S’intègre avec le Microsoft Agent Framework**. Azure AI Agent Service fonctionne de manière fluide avec le Microsoft Agent Framework, ce qui signifie que vous pouvez construire des agents avec `AzureAIProjectAgentProvider` et les déployer via le Agent Service pour des scénarios de production.

**Cas d’usage** : Azure AI Agent Service est conçu pour les applications entreprises nécessitant un déploiement sécurisé, scalable et flexible d’agents IA.

## Quelle est la différence entre ces approches ?

Il peut sembler y avoir un chevauchement, mais quelques différences clés en termes de conception, capacités et cas d’usage :

- **Microsoft Agent Framework (MAF)** : Un SDK prêt pour la production pour construire des agents IA. Il fournit une API simplifiée pour créer des agents avec appel d’outils, gestion des conversations et intégration Azure Identity.  
- **Azure AI Agent Service** : Une plateforme et un service de déploiement dans Azure Foundry pour agents. Il offre une connectivité intégrée à des services tels qu’Azure OpenAI, Azure AI Search, Bing Search et l’exécution de code.

Vous hésitez encore ?

### Cas d’utilisation

Voyons si cela peut vous aider en passant par quelques cas courants :

> Q : Je développe des applications agents IA en production et souhaite démarrer rapidement  
>  
> R : Microsoft Agent Framework est un excellent choix. Il fournit une API Python simple via `AzureAIProjectAgentProvider` qui vous permet de définir des agents avec outils et instructions en quelques lignes de code.

> Q : J’ai besoin d’un déploiement de niveau entreprise avec des intégrations Azure comme Search et exécution de code  
>  
> R : Azure AI Agent Service est le mieux adapté. C’est un service plateforme offrant des capacités intégrées pour plusieurs modèles, Azure AI Search, Bing Search et Azure Functions. Il facilite la construction de vos agents dans le portail Foundry et leur déploiement à grande échelle.

> Q : Je suis toujours confus, donnez-moi juste une option  
>  
> R : Commencez avec le Microsoft Agent Framework pour construire vos agents, puis utilisez Azure AI Agent Service lorsque vous devez les déployer et les mettre à l’échelle en production. Cette approche vous permet d’itérer rapidement sur votre logique d’agent tout en ayant une voie claire vers le déploiement entreprise.

Résumons les différences clés dans un tableau :

| Framework | Focus | Concepts Clés | Cas d’Usage |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agent simplifié avec appel d’outils | Agents, Outils, Azure Identity | Construction d’agents IA, utilisation d’outils, workflows multi-étapes |
| Azure AI Agent Service | Modèles flexibles, sécurité entreprise, génération de code, appel d’outils | Modularité, Collaboration, Orchestration de processus | Déploiement sécurisé, scalable et flexible d’agents IA |

## Puis-je intégrer directement mes outils existants de l’écosystème Azure, ou ai-je besoin de solutions autonomes ?
La réponse est oui, vous pouvez intégrer vos outils existants de l'écosystème Azure directement avec Azure AI Agent Service en particulier, car il a été conçu pour fonctionner parfaitement avec d'autres services Azure. Vous pouvez par exemple intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration approfondie avec Microsoft Foundry.

Le Microsoft Agent Framework s'intègre également aux services Azure via `AzureAIProjectAgentProvider` et l'identité Azure, vous permettant d'appeler les services Azure directement depuis vos outils d'agent.

## Exemples de code

- Python : [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Vous avez plus de questions sur les frameworks d'agents IA ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, participer à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Références

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Leçon précédente

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Leçon suivante

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour des informations critiques, une traduction professionnelle humaine est recommandée. Nous ne saurions être tenus responsables de tout malentendu ou mauvaise interprétation résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->