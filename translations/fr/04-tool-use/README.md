[![Comment concevoir de bons agents IA](../../../translated_images/fr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

# Modèle de conception pour l'utilisation d'outils

Les outils sont intéressants car ils permettent aux agents IA de disposer d'un éventail plus large de capacités. Au lieu que l'agent ait un ensemble limité d'actions qu'il peut effectuer, en ajoutant un outil, l'agent peut désormais réaliser une large gamme d'actions. Dans ce chapitre, nous allons examiner le modèle de conception pour l'utilisation d'outils, qui décrit comment les agents IA peuvent utiliser des outils spécifiques pour atteindre leurs objectifs.

## Introduction

Dans cette leçon, nous chercherons à répondre aux questions suivantes :

- Qu'est-ce que le modèle de conception pour l'utilisation d'outils ?
- À quels cas d'utilisation peut-il s'appliquer ?
- Quels sont les éléments/blocs de construction nécessaires pour implémenter ce modèle de conception ?
- Quelles sont les considérations particulières pour utiliser le modèle de conception pour l'utilisation d'outils afin de construire des agents IA dignes de confiance ?

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez en mesure de :

- Définir le modèle de conception pour l'utilisation d'outils et son objectif.
- Identifier les cas d'utilisation où ce modèle de conception est applicable.
- Comprendre les éléments clés nécessaires pour implémenter le modèle de conception.
- Reconnaître les considérations pour assurer la fiabilité des agents IA utilisant ce modèle de conception.

## Qu'est-ce que le modèle de conception pour l'utilisation d'outils ?

Le **modèle de conception pour l'utilisation d'outils** se concentre sur la capacité des grands modèles de langage (LLM) à interagir avec des outils externes afin d'atteindre des objectifs spécifiques. Les outils sont des codes pouvant être exécutés par un agent pour accomplir des actions. Un outil peut être une fonction simple telle qu'une calculatrice, ou un appel d'API vers un service tiers comme la consultation du cours d'une action ou les prévisions météorologiques. Dans le contexte des agents IA, les outils sont conçus pour être exécutés par les agents en réponse à des **appels de fonctions générés par le modèle**.

## À quels cas d'utilisation peut-il s'appliquer ?

Les agents IA peuvent exploiter des outils pour réaliser des tâches complexes, récupérer des informations ou prendre des décisions. Le modèle de conception pour l'utilisation d'outils est souvent utilisé dans des scénarios nécessitant une interaction dynamique avec des systèmes externes, tels que des bases de données, des services web ou des interprètes de code. Cette capacité est utile pour plusieurs cas d'utilisation, notamment :

- **Récupération dynamique d'informations :** les agents peuvent interroger des API externes ou des bases de données pour obtenir des données à jour (par exemple, interroger une base de données SQLite pour l’analyse de données, récupérer les prix des actions ou les informations météorologiques).
- **Exécution et interprétation de code :** les agents peuvent exécuter du code ou des scripts pour résoudre des problèmes mathématiques, générer des rapports ou effectuer des simulations.
- **Automatisation des flux de travail :** automatiser des flux de travail répétitifs ou en plusieurs étapes en intégrant des outils tels que des planificateurs de tâches, des services de messagerie ou des pipelines de données.
- **Support client :** les agents peuvent interagir avec des systèmes CRM, des plateformes de tickets ou des bases de connaissances pour résoudre les demandes des utilisateurs.
- **Génération et édition de contenu :** les agents peuvent utiliser des outils tels que des correcteurs grammaticaux, des résumeurs de texte ou des évaluateurs de sécurité du contenu pour aider aux tâches de création de contenu.

## Quels sont les éléments/blocs de construction nécessaires pour implémenter le modèle de conception pour l'utilisation d'outils ?

Ces blocs de construction permettent à l'agent IA d'exécuter une variété de tâches. Examinons les éléments clés nécessaires pour implémenter le modèle de conception pour l'utilisation d'outils :

- **Schémas de fonctions/outils :** définitions détaillées des outils disponibles, incluant le nom de la fonction, son objectif, les paramètres requis et les sorties attendues. Ces schémas permettent au LLM de comprendre quels outils sont disponibles et comment formuler des requêtes valides.

- **Logique d'exécution des fonctions :** régit comment et quand les outils sont invoqués en fonction de l'intention de l'utilisateur et du contexte de la conversation. Cela peut inclure des modules planificateurs, des mécanismes de routage ou des flux conditionnels qui déterminent dynamiquement l’utilisation des outils.

- **Système de gestion des messages :** composants qui gèrent le flux conversationnel entre les entrées utilisateur, les réponses du LLM, les appels d'outils et les sorties des outils.

- **Cadre d’intégration des outils :** infrastructure qui connecte l’agent à différents outils, qu'il s'agisse de fonctions simples ou de services externes complexes.

- **Gestion des erreurs et validation :** mécanismes pour gérer les échecs d’exécution des outils, valider les paramètres et gérer les réponses inattendues.

- **Gestion de l’état :** suit le contexte de la conversation, les interactions précédentes avec les outils et les données persistantes pour assurer la cohérence sur plusieurs échanges.

Regardons maintenant plus en détail les appels de fonctions/outils.
 
### Appel de fonctions/outils

L'appel de fonction est la principale manière dont nous permettons aux grands modèles de langage (LLM) d’interagir avec des outils. Vous verrez souvent « fonction » et « outil » utilisés de manière interchangeable parce que les « fonctions » (blocs de code réutilisables) sont les « outils » que les agents utilisent pour accomplir des tâches. Pour que le code d'une fonction soit invoqué, un LLM doit comparer la requête de l'utilisateur à la description des fonctions. Pour cela, un schéma contenant les descriptions de toutes les fonctions disponibles est envoyé au LLM. Celui-ci sélectionne alors la fonction la plus appropriée pour la tâche et renvoie son nom et ses arguments. La fonction sélectionnée est invoquée, sa réponse est renvoyée au LLM, qui utilise l’information pour répondre à la requête de l’utilisateur.

Pour les développeurs souhaitant implémenter l'appel de fonctions pour les agents, vous aurez besoin de :

1. Un modèle LLM supportant l’appel de fonctions
2. Un schéma contenant les descriptions de fonctions
3. Le code de chaque fonction décrite

Prenons l'exemple de l'obtention de l'heure actuelle dans une ville pour illustrer :

1. **Initialiser un LLM supportant les appels de fonctions :**

    Tous les modèles ne supportent pas l’appel de fonctions, il est donc important de vérifier que le LLM utilisé le fait.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporte l’appel de fonctions. Nous pouvons commencer par initier le client OpenAI contre l’API **Responses** d’Azure OpenAI (le point d’accès stable `/openai/v1/` — aucun `api_version` nécessaire). 

    ```python
    # Initialiser le client OpenAI pour Azure OpenAI (API de réponses, point de terminaison v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Créer un schéma de fonction :**

    Ensuite nous allons définir un schéma JSON contenant le nom de la fonction, une description de ce que fait la fonction, ainsi que les noms et descriptions des paramètres de la fonction.
    Nous transmettrons ce schéma au client créé précédemment, ainsi que la requête de l'utilisateur pour trouver l'heure à San Francisco. Il est important de noter qu’un **appel d’outil** est ce qui est retourné, **et non** la réponse finale à la question. Comme mentionné précédemment, le LLM retourne le nom de la fonction qu’il a sélectionnée pour la tâche, ainsi que les arguments qui lui seront passés.

    ```python
    # Description de la fonction pour que le modèle lise (format outil plat API de réponses)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Message initial de l'utilisateur
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Premier appel API : Demander au modèle d'utiliser la fonction
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # L'API des réponses renvoie les appels d'outil sous forme d'éléments function_call dans response.output.
    # Les ajouter à la conversation pour que le modèle ait tout le contexte au tour suivant.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Le code fonctionnel nécessaire pour exécuter la tâche :**

    Maintenant que le LLM a choisi quelle fonction doit être exécutée, le code qui réalise la tâche doit être implémenté et exécuté.
    Nous pouvons implémenter ce code en Python pour obtenir l'heure actuelle. Il faudra aussi écrire le code pour extraire le nom et les arguments de la response_message afin d’obtenir le résultat final.

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
    # Gérer les appels de fonction
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Retourner le résultat de l'outil comme un élément function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Deuxième appel API : Obtenir la réponse finale du modèle
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

L’appel de fonction est au cœur de la plupart, sinon de tous, les modèles de conception pour l’utilisation d’outils par les agents, mais le mettre en œuvre à partir de zéro peut parfois être complexe.
Comme nous l’avons appris dans [Leçon 2](../../../02-explore-agentic-frameworks), les frameworks agentiques nous fournissent des blocs préconstruits pour implémenter l’utilisation d’outils.
 
## Exemples d’utilisation d’outils avec des frameworks agentiques

Voici quelques exemples de la façon dont vous pouvez implémenter le modèle de conception pour l’utilisation d’outils en utilisant différents frameworks agentiques :

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> est un framework IA open-source pour construire des agents IA. Il simplifie le processus d’appel de fonctions en vous permettant de définir des outils sous forme de fonctions Python avec le décorateur `@tool`. Le framework gère la communication entre le modèle et votre code. Il fournit également l’accès à des outils préconstruits comme la recherche de fichiers et l’interpréteur de code via `FoundryChatClient`.

Le schéma suivant illustre le processus d'appel de fonctions avec le Microsoft Agent Framework :

![appel de fonction](../../../translated_images/fr/functioncalling-diagram.a84006fc287f6014.webp)

Dans Microsoft Agent Framework, les outils sont définis comme des fonctions décorées. Nous pouvons convertir la fonction `get_current_time` vue précédemment en un outil en utilisant le décorateur `@tool`. Le framework sérialisera automatiquement la fonction et ses paramètres, créant le schéma à envoyer au LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Créer le client
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Créer un agent et exécuter avec l'outil
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> est un framework agentique plus récent conçu pour permettre aux développeurs de créer, déployer et faire évoluer des agents IA sécurisés, de haute qualité et extensibles, sans avoir à gérer les ressources de calcul et de stockage sous-jacentes. Il est particulièrement utile pour les applications d'entreprise car il s'agit d'un service entièrement géré avec une sécurité de niveau entreprise.

Comparé au développement directement via l’API LLM, Microsoft Foundry Agent Service offre certains avantages, notamment :

- Appel d’outils automatique – plus besoin de parser un appel d’outil, d’invoquer l’outil et de gérer la réponse ; tout ceci se fait désormais côté serveur
- Données gérées en toute sécurité – au lieu de gérer votre propre état de conversation, vous pouvez compter sur des threads pour stocker toutes les informations nécessaires
- Outils prêts à l'emploi – outils permettant d’interagir avec vos sources de données, tels que Bing, Azure AI Search et Azure Functions.

Les outils disponibles dans Microsoft Foundry Agent Service peuvent être divisés en deux catégories :

1. Outils de connaissance :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Mise à la terre avec Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Recherche de fichiers</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Recherche Azure AI</a>

2. Outils d'action :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Appel de fonctions</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpréteur de code</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Outils définis par OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Le service Agent nous permet d’utiliser ces outils ensemble en tant que `toolset`. Il utilise également des `threads` qui suivent l’historique des messages d’une conversation particulière.

Imaginez que vous êtes un agent commercial chez une entreprise appelée Contoso. Vous souhaitez développer un agent conversationnel capable de répondre aux questions sur vos données de ventes.

L’image suivante illustre comment vous pourriez utiliser Microsoft Foundry Agent Service pour analyser vos données de ventes :

![Agentic Service en action](../../../translated_images/fr/agent-service-in-action.34fb465c9a84659e.webp)

Pour utiliser l’un de ces outils avec ce service, nous pouvons créer un client et définir un outil ou un ensemble d’outils. Pour implémenter cela concrètement, nous pouvons utiliser le code Python suivant. Le LLM pourra examiner cet ensemble d’outils et décider d’utiliser la fonction créée par l’utilisateur, `fetch_sales_data_using_sqlite_query`, ou l’interpréteur de code préconstruit selon la requête de l’utilisateur.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fonction fetch_sales_data_using_sqlite_query que l'on trouve dans un fichier fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser l'ensemble d'outils
toolset = ToolSet()

# Initialiser l'agent d'appel de fonction avec la fonction fetch_sales_data_using_sqlite_query et l'ajouter à l'ensemble d'outils
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser l'outil Code Interpreter et l'ajouter à l'ensemble d'outils.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quelles sont les considérations particulières pour utiliser le modèle de conception pour l’utilisation d’outils afin de construire des agents IA dignes de confiance ?

Une préoccupation courante avec le SQL généré dynamiquement par les LLM est la sécurité, notamment le risque d’injection SQL ou d’actions malveillantes comme la suppression ou la falsification de la base de données. Bien que ces craintes soient valides, elles peuvent être efficacement atténuées par une configuration correcte des permissions d’accès à la base de données. Pour la plupart des bases de données, cela implique de configurer la base de données en lecture seule. Pour des services de base de données comme PostgreSQL ou Azure SQL, l’application doit se voir attribuer un rôle en lecture seule (SELECT).

Exécuter l’application dans un environnement sécurisé renforce encore la protection. Dans des scénarios d’entreprise, les données sont généralement extraites et transformées depuis des systèmes opérationnels dans une base de données ou un entrepôt de données en lecture seule avec un schéma facile à utiliser. Cette approche garantit que les données sont sécurisées, optimisées pour la performance et l’accessibilité, et que l’application a un accès restreint en lecture seule.

## Exemples de codes

- Python : [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Vous avez d’autres questions sur le modèle de conception pour l’utilisation d’outils ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Atelier Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelier Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Vue d'ensemble du Microsoft Agent Framework</a>


## Test rapide de cet agent (optionnel)

Après avoir appris à déployer des agents dans [Leçon 16](../16-deploying-scalable-agents/README.md), vous pouvez faire un test rapide du `TravelToolAgent` de cette leçon (est-ce qu'il appelle toujours ses outils et répond ?) avec [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Voir [`tests/README.md`](../tests/README.md) pour savoir comment l'exécuter.

## Leçon précédente

[Comprendre les motifs de conception agentique](../03-agentic-design-patterns/README.md)

## Leçon suivante

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->