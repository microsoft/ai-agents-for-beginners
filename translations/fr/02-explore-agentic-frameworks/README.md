<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T10:49:23+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fr"
}
-->
[![Explorer les cadres d'agents IA](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.fr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

# Explorer les cadres d'agents IA

Les cadres d'agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion des agents IA. Ces cadres offrent aux développeurs des composants préconstruits, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces cadres permettent aux développeurs de se concentrer sur les aspects uniques de leurs applications en proposant des approches standardisées pour relever les défis courants dans le développement d'agents IA. Ils améliorent la scalabilité, l'accessibilité et l'efficacité dans la construction de systèmes IA.

## Introduction 

Cette leçon couvrira :

- Qu'est-ce qu'un cadre d'agents IA et que permettent-ils aux développeurs de réaliser ?
- Comment les équipes peuvent-elles les utiliser pour prototyper rapidement, itérer et améliorer les capacités de leurs agents ?
- Quelles sont les différences entre les cadres et outils créés par Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, et <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ?
- Puis-je intégrer directement mes outils existants de l'écosystème Azure ou ai-je besoin de solutions autonomes ?
- Qu'est-ce que le service Azure AI Agents et comment cela m'aide-t-il ?

## Objectifs d'apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des cadres d'agents IA dans le développement IA.
- Comment exploiter les cadres d'agents IA pour construire des agents intelligents.
- Les principales capacités offertes par les cadres d'agents IA.
- Les différences entre AutoGen, Semantic Kernel et Azure AI Agent Service.

## Qu'est-ce qu'un cadre d'agents IA et que permettent-ils aux développeurs de faire ?

Les cadres IA traditionnels peuvent vous aider à intégrer l'IA dans vos applications et à améliorer ces applications de la manière suivante :

- **Personnalisation** : L'IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations, du contenu et des expériences personnalisés.  
Exemple : Les services de streaming comme Netflix utilisent l'IA pour suggérer des films et des séries en fonction de l'historique de visionnage, améliorant ainsi l'engagement et la satisfaction des utilisateurs.
- **Automatisation et efficacité** : L'IA peut automatiser les tâches répétitives, rationaliser les flux de travail et améliorer l'efficacité opérationnelle.  
Exemple : Les applications de service client utilisent des chatbots alimentés par l'IA pour gérer les demandes courantes, réduisant ainsi les temps de réponse et libérant les agents humains pour des problèmes plus complexes.
- **Amélioration de l'expérience utilisateur** : L'IA peut améliorer l'expérience utilisateur globale en fournissant des fonctionnalités intelligentes telles que la reconnaissance vocale, le traitement du langage naturel et le texte prédictif.  
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l'IA pour comprendre et répondre aux commandes vocales, facilitant ainsi l'interaction des utilisateurs avec leurs appareils.

### Tout cela semble génial, n'est-ce pas ? Alors pourquoi avons-nous besoin des cadres d'agents IA ?

Les cadres d'agents IA représentent quelque chose de plus que de simples cadres IA. Ils sont conçus pour permettre la création d'agents intelligents capables d'interagir avec les utilisateurs, d'autres agents et l'environnement pour atteindre des objectifs spécifiques. Ces agents peuvent adopter un comportement autonome, prendre des décisions et s'adapter à des conditions changeantes. Examinons quelques capacités clés offertes par les cadres d'agents IA :

- **Collaboration et coordination entre agents** : Permet la création de plusieurs agents IA capables de travailler ensemble, de communiquer et de se coordonner pour résoudre des tâches complexes.
- **Automatisation et gestion des tâches** : Fournit des mécanismes pour automatiser des flux de travail en plusieurs étapes, déléguer des tâches et gérer dynamiquement les tâches entre agents.
- **Compréhension contextuelle et adaptation** : Équipe les agents de la capacité à comprendre le contexte, à s'adapter à des environnements changeants et à prendre des décisions basées sur des informations en temps réel.

En résumé, les agents vous permettent d'aller plus loin, de pousser l'automatisation à un niveau supérieur, de créer des systèmes plus intelligents capables de s'adapter et d'apprendre de leur environnement.

## Comment prototyper rapidement, itérer et améliorer les capacités de l'agent ?

C'est un domaine en constante évolution, mais il existe des éléments communs à la plupart des cadres d'agents IA qui peuvent vous aider à prototyper et itérer rapidement, à savoir les composants modulaires, les outils collaboratifs et l'apprentissage en temps réel. Explorons ces éléments :

- **Utiliser des composants modulaires** : Les SDK IA offrent des composants préconstruits tels que des connecteurs IA et mémoire, des appels de fonctions utilisant le langage naturel ou des plugins de code, des modèles d'invite, et plus encore.
- **Exploiter des outils collaboratifs** : Concevez des agents avec des rôles et des tâches spécifiques, leur permettant de tester et d'affiner les flux de travail collaboratifs.
- **Apprendre en temps réel** : Implémentez des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique.

### Utiliser des composants modulaires

Les SDK comme Microsoft Semantic Kernel et LangChain offrent des composants préconstruits tels que des connecteurs IA, des modèles d'invite et une gestion de la mémoire.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent assembler rapidement ces composants pour créer un prototype fonctionnel sans partir de zéro, permettant ainsi une expérimentation et une itération rapides.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur, un module mémoire pour stocker et récupérer des données, et un générateur d'invites pour interagir avec les utilisateurs, le tout sans avoir à construire ces composants à partir de zéro.

**Exemple de code**. Voici des exemples de l'utilisation d'un connecteur IA préconstruit avec Semantic Kernel Python et .Net qui utilise des appels de fonctions automatiques pour que le modèle réponde aux entrées utilisateur :

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
  
Ce que vous pouvez voir dans cet exemple, c'est comment vous pouvez exploiter un analyseur préconstruit pour extraire des informations clés des entrées utilisateur, telles que l'origine, la destination et la date d'une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Exploiter des outils collaboratifs

Des cadres comme CrewAI, Microsoft AutoGen et Semantic Kernel facilitent la création de plusieurs agents capables de travailler ensemble.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et des tâches spécifiques, leur permettant de tester et d'affiner les flux de travail collaboratifs et d'améliorer l'efficacité globale du système.

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
  
Ce que vous voyez dans le code précédent, c'est comment vous pouvez créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent remplit une fonction spécifique, et la tâche est exécutée en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous pouvez améliorer l'efficacité et les performances des tâches.

### Apprendre en temps réel

Les cadres avancés offrent des capacités de compréhension contextuelle et d'adaptation en temps réel.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent implémenter des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique, conduisant à une amélioration continue et à un raffinement des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours des utilisateurs, les données environnementales et les résultats des tâches pour mettre à jour leur base de connaissances, ajuster les algorithmes de prise de décision et améliorer leurs performances au fil du temps. Ce processus d'apprentissage itératif permet aux agents de s'adapter à des conditions changeantes et aux préférences des utilisateurs, améliorant ainsi l'efficacité globale du système.

## Quelles sont les différences entre les cadres AutoGen, Semantic Kernel et Azure AI Agent Service ?

Il existe de nombreuses façons de comparer ces cadres, mais examinons quelques différences clés en termes de conception, de capacités et de cas d'utilisation ciblés :

## AutoGen

AutoGen est un cadre open-source développé par le laboratoire AI Frontiers de Microsoft Research. Il se concentre sur les applications *agentiques* distribuées et pilotées par des événements, permettant plusieurs LLMs et SLMs, outils, et modèles de conception avancés pour les agents multiples.

AutoGen est construit autour du concept central des agents, qui sont des entités autonomes capables de percevoir leur environnement, de prendre des décisions et d'agir pour atteindre des objectifs spécifiques. Les agents communiquent via des messages asynchrones, leur permettant de travailler de manière indépendante et en parallèle, améliorant ainsi la scalabilité et la réactivité du système.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Les agents sont basés sur le modèle acteur</a>. Selon Wikipédia, un acteur est _l'élément de base du calcul concurrent. En réponse à un message qu'il reçoit, un acteur peut : prendre des décisions locales, créer d'autres acteurs, envoyer d'autres messages et déterminer comment répondre au prochain message reçu_.

**Cas d'utilisation** : Automatisation de la génération de code, des tâches d'analyse de données, et création d'agents personnalisés pour des fonctions de planification et de recherche.

Voici quelques concepts clés d'AutoGen :

- **Agents**. Un agent est une entité logicielle qui :
  - **Communique via des messages**, ces messages peuvent être synchrones ou asynchrones.
  - **Maintient son propre état**, qui peut être modifié par des messages entrants.
  - **Effectue des actions** en réponse aux messages reçus ou aux changements dans son état. Ces actions peuvent modifier l'état de l'agent et produire des effets externes, tels que la mise à jour des journaux de messages, l'envoi de nouveaux messages, l'exécution de code ou l'appel d'API.
    
  Voici un court extrait de code dans lequel vous créez votre propre agent avec des capacités de chat :

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Dans le code précédent, `MyAgent` a été créé et hérite de `RoutedAgent`. Il dispose d'un gestionnaire de messages qui imprime le contenu du message, puis envoie une réponse en utilisant le délégué `AssistantAgent`. Notez particulièrement comment nous assignons à `self._delegate` une instance de `AssistantAgent`, qui est un agent préconstruit capable de gérer des complétions de chat.

    Faisons savoir à AutoGen à propos de ce type d'agent et lançons le programme ensuite :

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Dans le code précédent, les agents sont enregistrés avec le runtime, puis un message est envoyé à l'agent, ce qui donne la sortie suivante :

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agents**. AutoGen prend en charge la création de plusieurs agents capables de travailler ensemble pour accomplir des tâches complexes. Les agents peuvent communiquer, partager des informations et coordonner leurs actions pour résoudre des problèmes plus efficacement. Pour créer un système multi-agents, vous pouvez définir différents types d'agents avec des fonctions et des rôles spécialisés, tels que la récupération de données, l'analyse, la prise de décision et l'interaction utilisateur. Voyons à quoi ressemble une telle création pour en avoir une idée :

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Dans le code précédent, nous avons un `GroupChatManager` qui est enregistré avec le runtime. Ce gestionnaire est responsable de la coordination des interactions entre différents types d'agents, tels que les rédacteurs, les illustrateurs, les éditeurs et les utilisateurs.

- **Runtime des agents**. Le cadre fournit un environnement d'exécution, permettant la communication entre agents, gérant leurs identités et cycles de vie, et appliquant des limites de sécurité et de confidentialité. Cela signifie que vous pouvez exécuter vos agents dans un environnement sécurisé et contrôlé, garantissant qu'ils peuvent interagir de manière sûre et efficace. Il existe deux environnements d'exécution d'intérêt :
  - **Runtime autonome**. C'est un bon choix pour les applications à processus unique où tous les agents sont implémentés dans le même langage de programmation et s'exécutent dans le même processus. Voici une illustration de son fonctionnement :
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime autonome</a>   
Application stack

    *les agents communiquent via des messages à travers le runtime, et le runtime gère le cycle de vie des agents*

  - **Runtime d'agents distribués**, convient aux applications multi-processus où les agents peuvent être implémentés dans différents langages de programmation et s'exécuter sur différentes machines. Voici une illustration de son fonctionnement :
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime distribué</a>

## Semantic Kernel + Cadre d'agents

Semantic Kernel est un SDK d'orchestration IA prêt pour l'entreprise. Il se compose de connecteurs IA et mémoire, ainsi que d'un cadre d'agents.

Commençons par couvrir quelques composants clés :

- **Connecteurs IA** : Il s'agit d'une interface avec des services IA externes et des sources de données utilisables à la fois en Python et en C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Voici un exemple simple de création d'un kernel et d'ajout d'un service de complétion de chat. Semantic Kernel crée une connexion à un service IA externe, dans ce cas, Azure OpenAI Chat Completion.

- **Plugins** : Ceux-ci encapsulent des fonctions qu'une application peut utiliser. Il existe à la fois des plugins prêts à l'emploi et des plugins personnalisés que vous pouvez créer. Un concept connexe est celui des "fonctions d'invite". Au lieu de fournir des indices en langage naturel pour l'invocation de fonctions, vous diffusez certaines fonctions au modèle. En fonction du contexte actuel du chat, le modèle peut choisir d'appeler l'une de ces fonctions pour compléter une demande ou une requête. Voici un exemple :

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Ici, vous avez d'abord un modèle d'invite `skPrompt` qui laisse de la place à l'utilisateur pour entrer du texte, `$userInput`. Ensuite, vous créez la fonction kernel `SummarizeText` et l'importez dans le kernel avec le nom de plugin `SemanticFunctions`. Notez le nom de la fonction qui aide Semantic Kernel à comprendre ce que fait la fonction et quand elle doit être appelée.

- **Fonction native** : Il existe également des fonctions natives que le cadre peut appeler directement pour effectuer la tâche. Voici un exemple d'une telle fonction récupérant le contenu d'un fichier :

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Mémoire** : Abstrait et simplifie la gestion du contexte pour les applications IA. L'idée avec la mémoire est que c'est quelque chose que le LLM devrait connaître. Vous pouvez stocker ces informations dans un magasin de vecteurs qui finit par être une base de données en mémoire ou une base de données vectorielle ou similaire. Voici un exemple d'un scénario très simplifié où des *faits* sont ajoutés à la mémoire :

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

Ces faits sont ensuite stockés dans la collection de mémoire `SummarizedAzureDocs`. C'est un exemple très simplifié, mais vous pouvez voir comment vous pouvez stocker des informations dans la mémoire pour que le LLM les utilise.

Voilà pour les bases du framework Semantic Kernel, qu'en est-il du framework Agent ?

## Service Azure AI Agent

Le service Azure AI Agent est une nouveauté introduite lors de Microsoft Ignite 2024. Il permet de développer et de déployer des agents IA avec des modèles plus flexibles, comme l'appel direct à des LLM open-source tels que Llama 3, Mistral et Cohere.

Le service Azure AI Agent offre des mécanismes de sécurité renforcés pour les entreprises et des méthodes de stockage de données, ce qui le rend adapté aux applications d'entreprise.

Il fonctionne directement avec des frameworks d'orchestration multi-agents comme AutoGen et Semantic Kernel.

Ce service est actuellement en aperçu public et prend en charge Python et C# pour la création d'agents.

Avec Semantic Kernel Python, nous pouvons créer un agent Azure AI avec un plugin défini par l'utilisateur :

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Concepts clés

Le service Azure AI Agent repose sur les concepts clés suivants :

- **Agent**. Le service Azure AI Agent s'intègre à Azure AI Foundry. Dans AI Foundry, un agent IA agit comme un microservice "intelligent" qui peut répondre à des questions (RAG), effectuer des actions ou automatiser complètement des workflows. Il y parvient en combinant la puissance des modèles IA génératifs avec des outils qui lui permettent d'accéder à des sources de données réelles et d'interagir avec elles. Voici un exemple d'agent :

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dans cet exemple, un agent est créé avec le modèle `gpt-4o-mini`, un nom `my-agent`, et des instructions `You are helpful agent`. L'agent est équipé d'outils et de ressources pour effectuer des tâches d'interprétation de code.

- **Thread et messages**. Le thread est un autre concept important. Il représente une conversation ou une interaction entre un agent et un utilisateur. Les threads peuvent être utilisés pour suivre l'avancement d'une conversation, stocker des informations contextuelles et gérer l'état de l'interaction. Voici un exemple de thread :

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

    Dans le code précédent, un thread est créé. Ensuite, un message est envoyé au thread. En appelant `create_and_process_run`, l'agent est invité à effectuer un travail sur le thread. Enfin, les messages sont récupérés et enregistrés pour voir la réponse de l'agent. Les messages indiquent l'avancement de la conversation entre l'utilisateur et l'agent. Il est également important de comprendre que les messages peuvent être de différents types, tels que texte, image ou fichier, c'est-à-dire que le travail de l'agent a abouti, par exemple, à une image ou une réponse textuelle. En tant que développeur, vous pouvez ensuite utiliser ces informations pour traiter davantage la réponse ou la présenter à l'utilisateur.

- **Intégration avec d'autres frameworks IA**. Le service Azure AI Agent peut interagir avec d'autres frameworks comme AutoGen et Semantic Kernel, ce qui signifie que vous pouvez construire une partie de votre application dans l'un de ces frameworks et, par exemple, utiliser le service Agent comme orchestrateur ou tout construire dans le service Agent.

**Cas d'utilisation** : Le service Azure AI Agent est conçu pour les applications d'entreprise nécessitant un déploiement d'agents IA sécurisé, évolutif et flexible.

## Quelle est la différence entre ces frameworks ?

Il semble qu'il y ait beaucoup de chevauchements entre ces frameworks, mais il existe des différences clés en termes de conception, de capacités et de cas d'utilisation ciblés :

- **AutoGen** : Un framework d'expérimentation axé sur la recherche de pointe sur les systèmes multi-agents. C'est l'endroit idéal pour expérimenter et prototyper des systèmes multi-agents sophistiqués.
- **Semantic Kernel** : Une bibliothèque d'agents prête pour la production pour construire des applications agentiques d'entreprise. Se concentre sur des applications agentiques distribuées et basées sur des événements, permettant plusieurs LLM et SLM, outils, et modèles de conception d'agents simples/multi-agents.
- **Service Azure AI Agent** : Une plateforme et un service de déploiement dans Azure Foundry pour les agents. Offre une connectivité aux services pris en charge par Azure, tels que Azure OpenAI, Azure AI Search, Bing Search et l'exécution de code.

Vous ne savez toujours pas lequel choisir ?

### Cas d'utilisation

Voyons si nous pouvons vous aider en passant en revue quelques cas d'utilisation courants :

> Q : Je fais des expérimentations, j'apprends et je construis des applications d'agents en preuve de concept, et je veux pouvoir construire et expérimenter rapidement.

> R : AutoGen serait un bon choix pour ce scénario, car il se concentre sur des applications agentiques distribuées et basées sur des événements et prend en charge des modèles de conception multi-agents avancés.

> Q : Qu'est-ce qui rend AutoGen meilleur que Semantic Kernel et le service Azure AI Agent pour ce cas d'utilisation ?

> R : AutoGen est spécifiquement conçu pour des applications agentiques distribuées et basées sur des événements, ce qui le rend bien adapté pour automatiser des tâches de génération de code et d'analyse de données. Il fournit les outils et capacités nécessaires pour construire efficacement des systèmes multi-agents complexes.

> Q : Il semble que le service Azure AI Agent pourrait aussi fonctionner ici, il a des outils pour la génération de code et plus encore ?

> R : Oui, le service Azure AI Agent est une plateforme de service pour les agents et ajoute des capacités intégrées pour plusieurs modèles, Azure AI Search, Bing Search et Azure Functions. Il facilite la création de vos agents dans le portail Foundry et leur déploiement à grande échelle.

> Q : Je suis toujours confus, donnez-moi juste une option.

> R : Un excellent choix est de construire votre application dans Semantic Kernel d'abord, puis d'utiliser le service Azure AI Agent pour déployer votre agent. Cette approche vous permet de persister facilement vos agents tout en tirant parti de la puissance de la construction de systèmes multi-agents dans Semantic Kernel. De plus, Semantic Kernel dispose d'un connecteur dans AutoGen, ce qui facilite l'utilisation des deux frameworks ensemble.

Résumons les différences clés dans un tableau :

| Framework | Focus | Concepts clés | Cas d'utilisation |
| --- | --- | --- | --- |
| AutoGen | Applications agentiques distribuées et basées sur des événements | Agents, Personas, Fonctions, Données | Génération de code, tâches d'analyse de données |
| Semantic Kernel | Compréhension et génération de contenu textuel humain | Agents, Composants modulaires, Collaboration | Compréhension du langage naturel, génération de contenu |
| Service Azure AI Agent | Modèles flexibles, sécurité d'entreprise, Génération de code, Appels d'outils | Modularité, Collaboration, Orchestration de processus | Déploiement d'agents IA sécurisé, évolutif et flexible |

Quel est le cas d'utilisation idéal pour chacun de ces frameworks ?

## Puis-je intégrer directement mes outils existants de l'écosystème Azure ou ai-je besoin de solutions autonomes ?

La réponse est oui, vous pouvez intégrer directement vos outils existants de l'écosystème Azure avec le service Azure AI Agent, notamment parce qu'il a été conçu pour fonctionner parfaitement avec d'autres services Azure. Vous pourriez, par exemple, intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration profonde avec Azure AI Foundry.

Pour AutoGen et Semantic Kernel, vous pouvez également intégrer avec les services Azure, mais cela peut nécessiter d'appeler les services Azure depuis votre code. Une autre façon d'intégrer est d'utiliser les SDK Azure pour interagir avec les services Azure depuis vos agents. De plus, comme mentionné, vous pouvez utiliser le service Azure AI Agent comme orchestrateur pour vos agents construits dans AutoGen ou Semantic Kernel, ce qui permet un accès facile à l'écosystème Azure.

## Codes d'exemple

- Python : [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Vous avez d'autres questions sur les frameworks d'agents IA ?

Rejoignez le [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Références

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Service Azure Agent</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel et AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Framework d'agent Python Semantic Kernel</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Framework d'agent .Net Semantic Kernel</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Service Azure AI Agent</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Utilisation du service Azure AI Agent avec AutoGen / Semantic Kernel pour construire une solution multi-agents</a>

## Leçon précédente

[Introduction aux agents IA et cas d'utilisation des agents](../01-intro-to-ai-agents/README.md)

## Leçon suivante

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->