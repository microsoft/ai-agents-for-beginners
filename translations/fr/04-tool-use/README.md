[![Comment concevoir de bons agents d'IA](../../../translated_images/fr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Cliquez sur l'image ci-dessus pour regarder la vidéo de cette leçon)_

# Modèle de conception : Utilisation d'outils

Les outils sont intéressants parce qu'ils permettent aux agents d'IA d'avoir un éventail de capacités plus large. Au lieu que l'agent dispose d'un ensemble limité d'actions qu'il peut effectuer, en ajoutant un outil, l'agent peut désormais exécuter une grande variété d'actions. Dans ce chapitre, nous examinerons le Modèle de conception d'utilisation d'outils, qui décrit comment les agents d'IA peuvent utiliser des outils spécifiques pour atteindre leurs objectifs.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Qu'est-ce que le modèle de conception d'utilisation d'outils ?
- Dans quels cas d'utilisation peut-il être appliqué ?
- Quels sont les éléments/blocs de construction nécessaires pour implémenter le modèle de conception ?
- Quelles sont les considérations particulières pour utiliser le Modèle de conception d'utilisation d'outils afin de construire des agents d'IA fiables ?

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Définir le Modèle de conception d'utilisation d'outils et son objectif.
- Identifier les cas d'utilisation où le Modèle de conception d'utilisation d'outils est applicable.
- Comprendre les éléments clés nécessaires pour implémenter le modèle de conception.
- Reconnaître les considérations pour assurer la fiabilité des agents d'IA utilisant ce modèle de conception.

## Qu'est-ce que le Modèle de conception d'utilisation d'outils ?

Le **Modèle de conception d'utilisation d'outils** se concentre sur le fait de donner aux LLMs la capacité d'interagir avec des outils externes pour atteindre des objectifs spécifiques. Les outils sont du code qui peut être exécuté par un agent pour effectuer des actions. Un outil peut être une fonction simple telle qu'une calculatrice, ou un appel d'API vers un service tiers tel qu'une consultation de prix d'actions ou une prévision météo. Dans le contexte des agents d'IA, les outils sont conçus pour être exécutés par des agents en réponse à des **appels de fonction générés par le modèle**.

## À quels cas d'utilisation peut-il être appliqué ?

Les agents d'IA peuvent exploiter des outils pour accomplir des tâches complexes, récupérer des informations ou prendre des décisions. Le modèle de conception d'utilisation d'outils est souvent utilisé dans des scénarios nécessitant une interaction dynamique avec des systèmes externes, tels que des bases de données, des services web ou des interprètes de code. Cette capacité est utile pour un certain nombre de cas d'utilisation différents, notamment :

- **Récupération d'informations dynamiques :** Les agents peuvent interroger des API externes ou des bases de données pour obtenir des données à jour (par ex., interroger une base SQLite pour l'analyse de données, récupérer des prix d'actions ou des informations météorologiques).
- **Exécution et interprétation de code :** Les agents peuvent exécuter du code ou des scripts pour résoudre des problèmes mathématiques, générer des rapports ou effectuer des simulations.
- **Automatisation des flux de travail :** Automatiser des flux de travail répétitifs ou multi-étapes en intégrant des outils tels que des planificateurs de tâches, des services de messagerie ou des pipelines de données.
- **Support client :** Les agents peuvent interagir avec des systèmes CRM, des plateformes de ticketing ou des bases de connaissances pour résoudre les demandes des utilisateurs.
- **Génération et édition de contenu :** Les agents peuvent exploiter des outils tels que des correcteurs grammaticaux, des résumeurs de texte ou des évaluateurs de sécurité du contenu pour assister les tâches de création de contenu.

## Quels sont les éléments/blocs de construction nécessaires pour implémenter le modèle de conception d'utilisation d'outils ?

Ces blocs de construction permettent à l'agent d'IA d'exécuter un large éventail de tâches. Examinons les éléments clés nécessaires pour implémenter le Modèle de conception d'utilisation d'outils :

- **Schémas de fonctions/outils :** Définitions détaillées des outils disponibles, incluant le nom de la fonction, l'objectif, les paramètres requis et les sorties attendues. Ces schémas permettent au LLM de comprendre quels outils sont disponibles et comment construire des requêtes valides.

- **Logique d'exécution des fonctions :** Régit la façon et le moment où les outils sont invoqués en fonction de l'intention de l'utilisateur et du contexte de la conversation. Cela peut inclure des modules de planification, des mécanismes de routage ou des flux conditionnels qui déterminent dynamiquement l'utilisation des outils.

- **Système de gestion des messages :** Composants qui gèrent le flux conversationnel entre les entrées utilisateur, les réponses du LLM, les appels d'outil et les sorties des outils.

- **Cadre d'intégration des outils :** Infrastructure qui connecte l'agent à divers outils, qu'il s'agisse de fonctions simples ou de services externes complexes.

- **Gestion des erreurs et validation :** Mécanismes pour gérer les échecs d'exécution d'outils, valider les paramètres et gérer les réponses inattendues.

- **Gestion d'état :** Suit le contexte de la conversation, les interactions précédentes avec les outils et les données persistantes pour garantir la cohérence sur des interactions multi-tours.

Ensuite, examinons l'Appel de fonctions/outils plus en détail.
 
### Appel de fonctions/outils

L'appel de fonctions est la principale façon d'autoriser les modèles de langage étendu (LLMs) à interagir avec des outils. Vous verrez souvent 'Function' et 'Tool' utilisés de manière interchangeable parce que les 'fonctions' (blocs de code réutilisables) sont les 'outils' que les agents utilisent pour accomplir des tâches. Pour qu'un code de fonction soit invoqué, un LLM doit comparer la requête de l'utilisateur avec la description des fonctions. Pour ce faire, un schéma contenant les descriptions de toutes les fonctions disponibles est envoyé au LLM. Le LLM choisit ensuite la fonction la plus appropriée pour la tâche et renvoie son nom et ses arguments. La fonction sélectionnée est invoquée, sa réponse est renvoyée au LLM, qui utilise l'information pour répondre à la requête de l'utilisateur.

Pour que les développeurs implémentent l'appel de fonctions pour les agents, vous aurez besoin de :

1. Un modèle LLM qui prend en charge l'appel de fonctions
2. Un schéma contenant les descriptions des fonctions
3. Le code pour chaque fonction décrite

Utilisons l'exemple d'obtenir l'heure actuelle dans une ville pour illustrer :

1. **Initialiser un LLM qui prend en charge l'appel de fonctions :**

    Tous les modèles ne prennent pas en charge l'appel de fonctions, il est donc important de vérifier que le LLM que vous utilisez le fait.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> prend en charge l'appel de fonctions. Nous pouvons commencer par initier le client Azure OpenAI. 

    ```python
    # Initialiser le client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Créer un schéma de fonction :**

    Ensuite, nous définirons un schéma JSON qui contient le nom de la fonction, la description de ce que fait la fonction, et les noms et descriptions des paramètres de la fonction.
    Nous prendrons ensuite ce schéma et le transmettrons au client créé précédemment, ainsi que la requête de l'utilisateur pour connaître l'heure à San Francisco. Il est important de noter qu'un **appel d'outil** est ce qui est renvoyé, **pas** la réponse finale à la question. Comme mentionné précédemment, le LLM renvoie le nom de la fonction qu'il a sélectionnée pour la tâche, et les arguments qui lui seront passés.

    ```python
    # Description de la fonction que le modèle doit lire.
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Message initial de l'utilisateur
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Premier appel de l'API : demander au modèle d'utiliser la fonction
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Traiter la réponse du modèle
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Le code de la fonction requis pour accomplir la tâche :**

    Maintenant que le LLM a choisi quelle fonction doit être exécutée, le code qui accomplit la tâche doit être implémenté et exécuté.
    Nous pouvons implémenter le code pour obtenir l'heure actuelle en Python. Nous aurons également besoin d'écrire le code pour extraire le nom et les arguments de la response_message afin d'obtenir le résultat final.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Gérer les appels de fonctions
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Deuxième appel API : obtenir la réponse finale du modèle
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

L'appel de fonctions est au cœur de la plupart, sinon de tous, les usages du modèle d'utilisation d'outils ; cependant, l'implémenter à partir de zéro peut parfois être un défi.
Comme nous l'avons appris dans [Leçon 2](../../../02-explore-agentic-frameworks), les frameworks agentiques nous fournissent des blocs de construction préfabriqués pour implémenter l'utilisation d'outils.
 
## Exemples d'utilisation d'outils avec des frameworks agentiques

Voici quelques exemples de la façon dont vous pouvez implémenter le Modèle de conception d'utilisation d'outils en utilisant différents frameworks agentiques :

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> est un framework d'IA open-source pour la construction d'agents d'IA. Il simplifie le processus d'utilisation de l'appel de fonctions en vous permettant de définir des outils comme des fonctions Python avec le décorateur `@tool`. Le framework gère la communication aller-retour entre le modèle et votre code. Il fournit également l'accès à des outils préconstruits tels que File Search et Code Interpreter via le `AzureAIProjectAgentProvider`.

Le diagramme suivant illustre le processus d'appel de fonctions avec le Microsoft Agent Framework :

![appel de fonction](../../../translated_images/fr/functioncalling-diagram.a84006fc287f6014.webp)

Dans le Microsoft Agent Framework, les outils sont définis comme des fonctions décorées. Nous pouvons convertir la fonction `get_current_time` que nous avons vue plus tôt en un outil en utilisant le décorateur `@tool`. Le framework sérialisera automatiquement la fonction et ses paramètres, créant le schéma à envoyer au LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Créer le client
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Créer un agent et l'exécuter avec l'outil
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> est un framework agentique plus récent conçu pour permettre aux développeurs de créer, déployer et faire évoluer de manière sécurisée des agents d'IA de haute qualité et extensibles sans avoir à gérer les ressources de calcul et de stockage sous-jacentes. Il est particulièrement utile pour les applications d'entreprise puisqu'il s'agit d'un service entièrement géré avec une sécurité de niveau entreprise.

Comparé au développement direct avec l'API LLM, Azure AI Agent Service offre certains avantages, notamment :

- Appel d'outils automatique – pas besoin d'analyser un appel d'outil, d'invoquer l'outil et de gérer la réponse ; tout cela est désormais effectué côté serveur
- Données gérées de manière sécurisée – au lieu de gérer votre propre état de conversation, vous pouvez vous appuyer sur les threads pour stocker toutes les informations dont vous avez besoin
- Outils prêts à l'emploi – outils que vous pouvez utiliser pour interagir avec vos sources de données, tels que Bing, Azure AI Search et Azure Functions.

Les outils disponibles dans Azure AI Agent Service peuvent être divisés en deux catégories :

1. Outils de connaissance :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Outils d'action :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Le Agent Service nous permet d'utiliser ces outils ensemble en tant que `toolset`. Il utilise également des `threads` qui gardent une trace de l'historique des messages d'une conversation particulière.

Imaginez que vous êtes un commercial dans une entreprise appelée Contoso. Vous souhaitez développer un agent conversationnel capable de répondre aux questions concernant vos données de vente.

L'image suivante illustre comment vous pourriez utiliser Azure AI Agent Service pour analyser vos données de vente :

![Service agentique en action](../../../translated_images/fr/agent-service-in-action.34fb465c9a84659e.webp)

Pour utiliser n'importe lequel de ces outils avec le service, nous pouvons créer un client et définir un outil ou un ensemble d'outils. Pour l'implémenter pratiquement, nous pouvons utiliser le code Python suivant. Le LLM pourra examiner le toolset et décider d'utiliser la fonction créée par l'utilisateur, `fetch_sales_data_using_sqlite_query`, ou l'outil Code Interpreter préconstruit en fonction de la requête de l'utilisateur.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fonction fetch_sales_data_using_sqlite_query qui se trouve dans le fichier fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser l'ensemble d'outils
toolset = ToolSet()

# Initialiser un agent d'appel de fonction avec la fonction fetch_sales_data_using_sqlite_query et l'ajouter à l'ensemble d'outils
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser l'outil Code Interpreter et l'ajouter à l'ensemble d'outils.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quelles sont les considérations particulières pour utiliser le Modèle de conception d'utilisation d'outils afin de construire des agents d'IA fiables ?

Une préoccupation courante concernant le SQL généré dynamiquement par les LLMs est la sécurité, en particulier le risque d'injection SQL ou d'actions malveillantes, telles que la suppression ou la manipulation de la base de données. Bien que ces préoccupations soient valables, elles peuvent être efficacement atténuées en configurant correctement les autorisations d'accès à la base de données. Pour la plupart des bases de données, cela implique de configurer la base de données en lecture seule. Pour des services de bases de données comme PostgreSQL ou Azure SQL, l'application doit se voir attribuer un rôle en lecture seule (SELECT).

Exécuter l'application dans un environnement sécurisé renforce encore la protection. Dans les scénarios d'entreprise, les données sont généralement extraites et transformées depuis des systèmes opérationnels vers une base de données en lecture seule ou un entrepôt de données avec un schéma convivial. Cette approche garantit que les données sont sécurisées, optimisées pour la performance et l'accessibilité, et que l'application dispose d'un accès restreint en lecture seule.

## Exemples de code

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Vous avez d'autres questions sur le modèle de conception d'utilisation d'outils ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents d'IA.

## Ressources supplémentaires

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Leçon précédente

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

## Leçon suivante
[RAG agentique](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avis de non-responsabilité :

Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne pouvons être tenus responsables de tout malentendu ou mauvaise interprétation résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->