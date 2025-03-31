<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T10:18:40+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "fr"
}
-->
[![Exploration des Cadres d'Agents IA](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.fr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

# Explorer les Cadres d'Agents IA

Les cadres d'agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion des agents IA. Ces cadres offrent aux développeurs des composants préconstruits, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces cadres permettent aux développeurs de se concentrer sur les aspects uniques de leurs applications en fournissant des approches standardisées pour relever les défis courants dans le développement d'agents IA. Ils améliorent la scalabilité, l'accessibilité et l'efficacité dans la construction de systèmes IA.

## Introduction 

Cette leçon abordera :

- Ce que sont les cadres d'agents IA et ce qu'ils permettent aux développeurs de réaliser.
- Comment les équipes peuvent les utiliser pour prototyper rapidement, itérer et améliorer les capacités de leurs agents.
- Quelles sont les différences entre les cadres et outils créés par Microsoft, et entre eux ?
- Puis-je intégrer directement mes outils existants de l'écosystème Azure ou dois-je utiliser des solutions autonomes ?
- Qu'est-ce que le service Azure AI Agents et comment cela peut m'aider ?

## Objectifs d'apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des cadres d'agents IA dans le développement IA.
- Comment exploiter les cadres d'agents IA pour construire des agents intelligents.
- Les principales capacités permises par les cadres d'agents IA.
- Les différences entre AutoGen, Semantic Kernel et le service Azure AI Agent.

## Qu'est-ce que les cadres d'agents IA et que permettent-ils aux développeurs de faire ?

Les cadres IA traditionnels peuvent vous aider à intégrer l'IA dans vos applications et améliorer ces dernières de plusieurs façons :

- **Personnalisation** : L'IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations, du contenu et des expériences personnalisés.
Exemple : Les services de streaming comme Netflix utilisent l'IA pour suggérer des films et des séries basés sur l'historique de visionnage, améliorant ainsi l'engagement et la satisfaction des utilisateurs.
- **Automatisation et efficacité** : L'IA peut automatiser les tâches répétitives, rationaliser les flux de travail et améliorer l'efficacité opérationnelle.
Exemple : Les applications de service client utilisent des chatbots alimentés par l'IA pour traiter les demandes courantes, réduisant les temps de réponse et libérant les agents humains pour des problèmes plus complexes.
- **Amélioration de l'expérience utilisateur** : L'IA peut améliorer l'expérience utilisateur globale en fournissant des fonctionnalités intelligentes telles que la reconnaissance vocale, le traitement du langage naturel et le texte prédictif.
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l'IA pour comprendre et répondre aux commandes vocales, facilitant ainsi l'interaction des utilisateurs avec leurs appareils.

### Cela semble génial, n'est-ce pas ? Alors pourquoi avons-nous besoin des cadres d'agents IA ?

Les cadres d'agents IA représentent quelque chose de plus qu'un simple cadre IA. Ils sont conçus pour permettre la création d'agents intelligents capables d'interagir avec les utilisateurs, d'autres agents et l'environnement pour atteindre des objectifs spécifiques. Ces agents peuvent exhiber un comportement autonome, prendre des décisions et s'adapter à des conditions changeantes. Regardons quelques capacités clés permises par les cadres d'agents IA :

- **Collaboration et coordination entre agents** : Permet la création de multiples agents IA capables de travailler ensemble, de communiquer et de se coordonner pour résoudre des tâches complexes.
- **Automatisation et gestion des tâches** : Fournit des mécanismes pour automatiser les flux de travail en plusieurs étapes, déléguer des tâches et gérer dynamiquement les tâches entre les agents.
- **Compréhension contextuelle et adaptation** : Équipe les agents de la capacité à comprendre le contexte, s'adapter à des environnements changeants et prendre des décisions basées sur des informations en temps réel.

En résumé, les agents vous permettent de faire plus, d'amener l'automatisation à un niveau supérieur, de créer des systèmes plus intelligents capables de s'adapter et d'apprendre de leur environnement.

## Comment prototyper rapidement, itérer et améliorer les capacités des agents ?

C'est un domaine en constante évolution, mais il y a des éléments communs à la plupart des cadres d'agents IA qui peuvent vous aider à prototyper et itérer rapidement, notamment les composants modulaires, les outils collaboratifs et l'apprentissage en temps réel. Plongeons dans ces éléments :

- **Utiliser des composants modulaires** : Les SDK IA offrent des composants préconstruits tels que des connecteurs IA et mémoire, des appels de fonction utilisant le langage naturel ou des plugins de code, des modèles de prompts, et bien plus encore.
- **Exploiter des outils collaboratifs** : Concevez des agents avec des rôles et des tâches spécifiques, leur permettant de tester et d'affiner des flux de travail collaboratifs.
- **Apprendre en temps réel** : Implémentez des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique.

### Utiliser des composants modulaires

Les SDK comme Microsoft Semantic Kernel et LangChain offrent des composants préconstruits tels que des connecteurs IA, des modèles de prompts et la gestion de mémoire.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent assembler rapidement ces composants pour créer un prototype fonctionnel sans partir de zéro, permettant une expérimentation et une itération rapides.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur, un module de mémoire pour stocker et récupérer des données, et un générateur de prompts pour interagir avec les utilisateurs, le tout sans avoir à construire ces composants à partir de zéro.

**Exemple de code**. Regardons des exemples de comment utiliser un connecteur IA préconstruit avec Semantic Kernel Python et .Net qui utilise des appels de fonction automatiques pour que le modèle réponde aux entrées utilisateur :

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Ce que vous pouvez voir dans cet exemple, c'est comment utiliser un analyseur préconstruit pour extraire des informations clés des entrées utilisateur, telles que l'origine, la destination et la date d'une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Exploiter des outils collaboratifs

Les cadres comme CrewAI, Microsoft AutoGen et Semantic Kernel facilitent la création de multiples agents capables de travailler ensemble.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et des tâches spécifiques, leur permettant de tester et d'affiner des flux de travail collaboratifs et d'améliorer l'efficacité globale du système.

**Comment cela fonctionne en pratique** : Vous pouvez créer une équipe d'agents où chaque agent a une fonction spécialisée, comme la récupération de données, l'analyse ou la prise de décision. Ces agents peuvent communiquer et partager des informations pour atteindre un objectif commun, comme répondre à une requête utilisateur ou accomplir une tâche.

**Exemple de code (AutoGen)** :

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Ce que vous voyez dans le code précédent, c'est comment créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent remplit une fonction spécifique, et la tâche est exécutée en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous pouvez améliorer l'efficacité et les performances des tâches.

### Apprendre en temps réel

Les cadres avancés offrent des capacités de compréhension contextuelle et d'adaptation en temps réel.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent implémenter des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique, conduisant à une amélioration continue et au raffinement des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours des utilisateurs, les données environnementales et les résultats des tâches pour mettre à jour leur base de connaissances, ajuster leurs algorithmes de prise de décision et améliorer leurs performances au fil du temps. Ce processus d'apprentissage itératif permet aux agents de s'adapter aux conditions changeantes et aux préférences des utilisateurs, améliorant l'efficacité globale du système.

## Quelles sont les différences entre les cadres AutoGen, Semantic Kernel et Azure AI Agent Service ?

Il existe de nombreuses façons de comparer ces cadres, mais examinons quelques différences clés en termes de conception, de capacités et de cas d'utilisation ciblés :

## AutoGen

AutoGen est un cadre open-source développé par le laboratoire AI Frontiers de Microsoft Research. Il se concentre sur les applications *agentiques* distribuées et basées sur les événements, permettant de multiples LLMs et SLMs, outils, et des modèles de conception avancés pour les systèmes multi-agents.

AutoGen est construit autour du concept central des agents, qui sont des entités autonomes capables de percevoir leur environnement, de prendre des décisions et de mener des actions pour atteindre des objectifs spécifiques. Les agents communiquent par des messages asynchrones, leur permettant de travailler de manière indépendante et en parallèle, ce qui améliore la scalabilité et la réactivité du système.
Modularité, Collaboration, Orchestration des processus | Déploiement d'agents IA sécurisé, évolutif et flexible | Quel est le cas d'utilisation idéal pour chacun de ces frameworks ?

## Puis-je intégrer directement mes outils existants de l'écosystème Azure ou ai-je besoin de solutions autonomes ?

La réponse est oui, vous pouvez intégrer directement vos outils existants de l'écosystème Azure avec Azure AI Agent Service, notamment parce qu'il a été conçu pour fonctionner de manière fluide avec d'autres services Azure. Par exemple, vous pourriez intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration poussée avec Azure AI Foundry.

Pour AutoGen et Semantic Kernel, vous pouvez également intégrer des services Azure, mais cela pourrait nécessiter d'appeler les services Azure depuis votre code. Une autre manière d'intégrer consiste à utiliser les SDK Azure pour interagir avec les services Azure depuis vos agents.

De plus, comme mentionné, vous pouvez utiliser Azure AI Agent Service comme orchestrateur pour vos agents construits avec AutoGen ou Semantic Kernel, ce qui offrirait un accès simplifié à l'écosystème Azure.

## Références

## Leçon précédente

[Introduction aux agents IA et cas d'utilisation des agents](../01-intro-to-ai-agents/README.md)

## Leçon suivante

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.