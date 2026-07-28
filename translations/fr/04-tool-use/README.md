[![Comment concevoir de bons agents IA](../../../translated_images/fr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

# Modèle de conception d'utilisation d'outils

Les outils sont intéressants car ils permettent aux agents IA d'avoir un éventail plus large de capacités. Au lieu que l'agent ait un ensemble limité d'actions qu'il peut effectuer, en ajoutant un outil, l'agent peut désormais réaliser un large éventail d'actions. Dans ce chapitre, nous allons examiner le modèle de conception d'utilisation d'outils, qui décrit comment les agents IA peuvent utiliser des outils spécifiques pour atteindre leurs objectifs.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Qu'est-ce que le modèle de conception d'utilisation d'outils ?
- À quels cas d'utilisation peut-il s'appliquer ?
- Quels sont les éléments/blocs de construction nécessaires pour implémenter ce modèle de conception ?
- Quelles sont les considérations particulières pour utiliser le modèle de conception d'utilisation d'outils afin de construire des agents IA dignes de confiance ?

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Définir le modèle de conception d'utilisation d'outils et son objectif.
- Identifier les cas d'utilisation où ce modèle est applicable.
- Comprendre les éléments clés nécessaires pour mettre en œuvre ce modèle.
- Reconnaître les considérations pour assurer la fiabilité des agents IA utilisant ce modèle de conception.

## Qu'est-ce que le modèle de conception d'utilisation d'outils ?

Le **modèle de conception d'utilisation d'outils** se concentre sur la capacité des grands modèles de langage (LLM) à interagir avec des outils externes pour atteindre des objectifs spécifiques. Les outils sont des codes que l'agent peut exécuter pour réaliser des actions. Un outil peut être une fonction simple comme une calculatrice, ou un appel API à un service tiers comme une consultation de prix boursiers ou une prévision météo. Dans le contexte des agents IA, les outils sont conçus pour être exécutés par les agents en réponse à des **appels de fonction générés par le modèle**.

## À quels cas d'utilisation peut-il s'appliquer ?

Les agents IA peuvent exploiter des outils pour accomplir des tâches complexes, récupérer des informations ou prendre des décisions. Le modèle d'utilisation d'outils est souvent utilisé dans des scénarios nécessitant une interaction dynamique avec des systèmes externes, tels que des bases de données, services web ou interprètes de code. Cette capacité est utile pour plusieurs cas d'usage, notamment :

- **Récupération dynamique d'informations :** les agents peuvent interroger des API externes ou des bases de données pour obtenir des données à jour (par exemple, interroger une base SQLite pour analyser des données, récupérer des cours boursiers ou des informations météo).
- **Exécution et interprétation de code :** les agents peuvent exécuter du code ou des scripts pour résoudre des problèmes mathématiques, générer des rapports ou effectuer des simulations.
- **Automatisation des flux de travail :** automatiser des flux répétitifs ou à étapes multiples en intégrant des outils tels que des planificateurs de tâches, services de messagerie ou pipelines de données.
- **Support client :** les agents peuvent interagir avec des systèmes CRM, plateformes de tickets ou bases de connaissances pour résoudre les requêtes des utilisateurs.
- **Génération et édition de contenu :** les agents peuvent utiliser des outils comme les correcteurs grammaticaux, résumeurs de texte ou évaluateurs de sécurité de contenu pour aider à la création de contenu.

## Quels sont les éléments/blocs de construction nécessaires pour mettre en œuvre le modèle d'utilisation d'outils ?

Ces éléments permettent à l'agent IA d'effectuer un large éventail de tâches. Regardons les éléments clés requis pour implémenter ce modèle de conception :

- **Schémas des fonctions/outils** : définitions détaillées des outils disponibles, comprenant le nom de la fonction, son but, les paramètres requis et les sorties attendues. Ces schémas permettent au LLM de comprendre quels outils sont disponibles et comment formuler des requêtes valides.

- **Logique d'exécution des fonctions** : régit quand et comment les outils sont invoqués en fonction de l'intention de l'utilisateur et du contexte de la conversation. Cela peut inclure des modules planificateurs, des mécanismes de routage ou des flux conditionnels qui déterminent dynamiquement l'utilisation des outils.

- **Système de gestion des messages** : composants qui gèrent le flux conversationnel entre les entrées utilisateur, réponses du LLM, appels d'outils et résultats d'outils.

- **Cadre d'intégration des outils** : infrastructure qui connecte l'agent à divers outils, qu'il s'agisse de fonctions simples ou de services externes complexes.

- **Gestion des erreurs et validation** : mécanismes pour gérer les échecs d'exécution des outils, valider les paramètres et gérer les réponses inattendues.

- **Gestion de l'état** : suit le contexte de la conversation, les interactions précédentes avec les outils et les données persistantes pour garantir la cohérence lors d'interactions multiples.

Ensuite, examinons plus en détail l'appel de fonctions/outils.
 
### Appel de fonctions/outils

L'appel de fonctions est le moyen principal qui permet aux grands modèles de langage (LLM) d'interagir avec les outils. Vous verrez souvent 'Fonction' et 'Outil' utilisés de manière interchangeable car les 'fonctions' (blocs de code réutilisables) sont les 'outils' que les agents utilisent pour réaliser des tâches. Pour qu'un code de fonction soit invoqué, un LLM doit comparer la requête de l'utilisateur avec la description de la fonction. Pour ce faire, un schéma contenant les descriptions de toutes les fonctions disponibles est envoyé au LLM. Le LLM sélectionne alors la fonction la plus appropriée pour la tâche et retourne son nom et ses arguments. La fonction sélectionnée est invoquée, sa réponse est renvoyée au LLM, qui utilise ces informations pour répondre à la requête de l'utilisateur.

Pour que les développeurs implémentent l'appel de fonctions pour les agents, vous aurez besoin de :

1. Un modèle LLM qui supporte l'appel de fonctions
2. Un schéma contenant les descriptions des fonctions
3. Le code pour chaque fonction décrite

Illustrons cela avec l'exemple de l'obtention de l'heure actuelle dans une ville :

1. **Initialiser un LLM qui supporte l'appel de fonctions :**

    Tous les modèles ne supportent pas l'appel de fonctions, il est donc important de vérifier que le modèle que vous utilisez le fait. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporte l'appel de fonctions. Nous pouvons commencer par initier le client OpenAI via l'API **Responses** Azure OpenAI (le point d'accès stable `/openai/v1/` — pas besoin de `api_version`). 

    ```python
    # Initialiser le client OpenAI pour Azure OpenAI (API Réponses, point de terminaison v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Créer un schéma de fonction** :

    Ensuite, nous définirons un schéma JSON contenant le nom de la fonction, la description de ce qu'elle fait, ainsi que les noms et descriptions des paramètres de la fonction.
    Nous passerons ensuite ce schéma au client créé précédemment avec la requête utilisateur pour obtenir l'heure à San Francisco. Ce qu'il faut noter est qu'un **appel d'outil** est ce qui est renvoyé, **pas** la réponse finale à la question. Comme mentionné plus tôt, le LLM renvoie le nom de la fonction sélectionnée pour la tâche, et les arguments qui lui seront passés.

    ```python
    # Description de la fonction pour que le modèle puisse lire (format outil plat API Réponses)
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

    # L'API Responses renvoie les appels d'outil sous forme d'éléments function_call dans response.output.
    # Les ajouter à la conversation pour que le modèle ait le contexte complet au tour suivant.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Le code de la fonction nécessaire à la réalisation de la tâche :**

    Maintenant que le LLM a choisi la fonction qui doit être exécutée, le code qui réalise la tâche doit être implémenté et exécuté.
    Nous pouvons implémenter le code pour obtenir l'heure actuelle en Python. Nous aurons aussi besoin d'écrire le code pour extraire le nom et les arguments depuis la response_message afin d'obtenir le résultat final.

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

                # Retourner le résultat de l'outil en tant qu'élément function_call_output
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

L'appel de fonctions est au cœur de la plupart, voire de tous, les designs d'utilisation d'outils par des agents, cependant l'implémenter à partir de zéro peut parfois être complexe.
Comme nous l'avons appris dans la [Leçon 2](../../../02-explore-agentic-frameworks), les frameworks agentiques nous fournissent des blocs préconstruits pour implémenter l'utilisation d'outils.
 
## Exemples d'utilisation d'outils avec des frameworks agentiques

Voici quelques exemples de la manière dont vous pouvez mettre en œuvre le modèle de conception d'utilisation d'outils avec différents frameworks agentiques :

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> est un framework IA open-source pour construire des agents IA. Il simplifie le processus d'appel de fonctions en vous permettant de définir des outils comme des fonctions Python avec le décorateur `@tool`. Le framework gère la communication bidirectionnelle entre le modèle et votre code. Il offre aussi l'accès à des outils préconstruits comme File Search et Code Interpreter via `FoundryChatClient`.

Le diagramme suivant illustre le processus d'appel de fonctions avec Microsoft Agent Framework :

![fonction appelante](../../../translated_images/fr/functioncalling-diagram.a84006fc287f6014.webp)

Dans Microsoft Agent Framework, les outils sont définis en tant que fonctions décorées. Nous pouvons convertir la fonction `get_current_time` vue plus tôt en un outil en utilisant le décorateur `@tool`. Le framework sérialisera automatiquement la fonction et ses paramètres, créant le schéma à envoyer au LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> est un framework agentique plus récent conçu pour permettre aux développeurs de construire, déployer et scaler des agents IA de haute qualité et extensibles en toute sécurité, sans avoir à gérer les ressources informatiques et de stockage sous-jacentes. Il est particulièrement utile pour les applications d'entreprise car il s'agit d'un service entièrement géré avec une sécurité de niveau entreprise.

Comparé au développement direct avec l'API LLM, Microsoft Foundry Agent Service offre plusieurs avantages, notamment :

- Appels automatiques d'outils – plus besoin d'analyser un appel d'outil, d'invoquer l'outil et de gérer la réponse ; tout cela est désormais fait côté serveur
- Gestion sécurisée des données – au lieu de gérer vous-même l'état de la conversation, vous pouvez vous appuyer sur des threads pour stocker toutes les informations nécessaires
- Outils prêts à l'emploi – outils que vous pouvez utiliser pour interagir avec vos sources de données, comme Bing, Azure AI Search, et Azure Functions.

Les outils disponibles dans Microsoft Foundry Agent Service peuvent être divisés en deux catégories :

1. Outils de connaissance :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Fondation avec Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Recherche de fichiers</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Recherche Azure AI</a>

2. Outils d'action :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Appel de fonctions</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpréteur de code</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Outils définis par OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Le service Agent nous permet d'utiliser ces outils ensemble en tant que `toolset`. Il utilise aussi des `threads` qui gardent la trace de l'historique des messages d'une conversation particulière.

Imaginez que vous êtes un agent commercial chez une entreprise appelée Contoso. Vous souhaitez développer un agent conversationnel pouvant répondre aux questions concernant vos données de vente.

L'image suivante illustre comment vous pourriez utiliser Microsoft Foundry Agent Service pour analyser vos données de vente :

![Agentic Service en action](../../../translated_images/fr/agent-service-in-action.34fb465c9a84659e.webp)

Pour utiliser l'un de ces outils avec le service, nous pouvons créer un client et définir un outil ou un ensemble d'outils. Pour l'implémenter concrètement, nous pouvons utiliser le code Python suivant. Le LLM pourra examiner l'ensemble d'outils et décider d’utiliser la fonction créée par l'utilisateur, `fetch_sales_data_using_sqlite_query`, ou l'interpréteur de code préconstruit selon la requête de l'utilisateur.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fonction fetch_sales_data_using_sqlite_query que l'on peut trouver dans un fichier fetch_sales_data_functions.py.
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
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quelles sont les considérations particulières pour utiliser le modèle d'utilisation d'outils afin de construire des agents IA dignes de confiance ?

Une préoccupation courante avec le SQL généré dynamiquement par les LLM est la sécurité, notamment le risque d'injection SQL ou d'actions malveillantes, comme la suppression ou la modification de la base de données. Bien que ces préoccupations soient valides, elles peuvent être efficacement atténuées en configurant correctement les permissions d'accès à la base de données. Pour la plupart des bases de données, cela implique de configurer la base en lecture seule. Pour des services de bases de données comme PostgreSQL ou Azure SQL, l’application doit se voir attribuer un rôle en lecture seule (SELECT).

Exécuter l'application dans un environnement sécurisé renforce encore la protection. Dans les scénarios d'entreprise, les données sont généralement extraites et transformées des systèmes opérationnels vers une base ou entrepôt de données en lecture seule avec un schéma convivial. Cette approche garantit que les données sont sécurisées, optimisées pour la performance et l'accessibilité, et que l'application a un accès restreint en lecture seule.

## Exemples de codes

- Python : [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Vous avez d'autres questions sur le modèle d'utilisation d'outils ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, participer aux heures de bureau et faire répondre vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Atelier Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelier multi-agents Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Présentation du Microsoft Agent Framework</a>


## Tester rapidement cet agent (facultatif)

Après avoir appris à déployer des agents dans la [Leçon 16](../16-deploying-scalable-agents/README.md), vous pouvez tester rapidement le `TravelToolAgent` de cette leçon (est-ce qu'il appelle toujours ses outils et répond ?) avec [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Consultez [`tests/README.md`](../tests/README.md) pour savoir comment l'exécuter.

## Leçon précédente

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

## Leçon suivante

[RAG agentique](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->