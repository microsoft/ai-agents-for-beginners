# Explorer le Microsoft Agent Framework

![Agent Framework](../../../translated_images/fr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Cette leçon couvrira :

- Comprendre le Microsoft Agent Framework : fonctionnalités clés et valeur  
- Explorer les concepts clés du Microsoft Agent Framework
- Modèles avancés MAF : workflows, middleware et mémoire

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Construire des agents IA prêts pour la production en utilisant le Microsoft Agent Framework
- Appliquer les fonctionnalités principales du Microsoft Agent Framework à vos cas d’utilisation agentiques
- Utiliser des modèles avancés incluant workflows, middleware et observabilité

## Exemples de code 

Des exemples de code pour [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) sont disponibles dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Comprendre le Microsoft Agent Framework

![Framework Intro](../../../translated_images/fr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) est le framework unifié de Microsoft pour créer des agents IA. Il offre la flexibilité de répondre à la grande variété des cas d'usage agentiques observés dans les environnements de production et de recherche, notamment :

- **Orchestration séquentielle d’agents** dans les scénarios où des workflows étape par étape sont nécessaires.
- **Orchestration concurrente** dans les scénarios où les agents doivent accomplir des tâches simultanément.
- **Orchestration de chat de groupe** dans les scénarios où les agents collaborent ensemble sur une tâche.
- **Orchestration de transfert** dans les scénarios où les agents se relaient la tâche à mesure que les sous-tâches sont terminées.
- **Orchestration magnétique** dans les scénarios où un agent manager crée et modifie une liste de tâches et gère la coordination des sous-agents pour accomplir la tâche.

Pour délivrer des agents IA en production, MAF inclut également des fonctionnalités pour :

- **Observabilité** grâce à l'utilisation d'OpenTelemetry où chaque action de l'agent IA, y compris l'invocation d'outils, les étapes d'orchestration, les flux de raisonnement et la surveillance des performances via les tableaux de bord Microsoft Foundry.
- **Sécurité** en hébergeant les agents nativement sur Microsoft Foundry, qui comprend des contrôles de sécurité comme l'accès basé sur les rôles, la gestion des données privées et la sécurité intégrée du contenu.
- **Durabilité** car les threads et workflows des agents peuvent être mis en pause, repris et récupérer des erreurs, ce qui permet des processus de longue durée.
- **Contrôle** car les workflows avec intervention humaine sont supportés où les tâches sont marquées comme nécessitant une approbation humaine.

Microsoft Agent Framework est également axé sur l'interopérabilité par :

- **Être agnostique au cloud** - Les agents peuvent fonctionner dans des conteneurs, sur site et à travers plusieurs clouds différents.
- **Être agnostique au fournisseur** - Les agents peuvent être créés via le SDK de votre choix y compris Azure OpenAI et OpenAI
- **Intégrer des standards ouverts** - Les agents peuvent utiliser des protocoles tels que Agent-to-Agent (A2A) et Model Context Protocol (MCP) pour découvrir et utiliser d’autres agents et outils.
- **Plugins et connecteurs** - Des connexions peuvent être établies vers des services de données et mémoire tels que Microsoft Fabric, SharePoint, Pinecone et Qdrant.

Voyons comment ces fonctionnalités sont appliquées à certains des concepts clés du Microsoft Agent Framework.

## Concepts clés du Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/fr/agent-components.410a06daf87b4fef.webp)

**Création des agents**

La création d'agents se fait en définissant le service d'inférence (fournisseur LLM), un
ensemble d'instructions que l'agent IA doit suivre, et un `nom` assigné :

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

L'exemple ci-dessus utilise `Azure OpenAI` mais les agents peuvent être créés avec divers services, y compris `Microsoft Foundry Agent Service` :

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou [MiniMax](https://platform.minimaxi.com/), qui fournit une API compatible OpenAI avec de grandes fenêtres de contexte (jusqu'à 204K tokens) :

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou des agents distants utilisant le protocole A2A :

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Exécution des agents**

Les agents sont exécutés en utilisant les méthodes `.run` ou `.run_stream` pour des réponses non streaming ou streaming respectivement.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Chaque exécution d'agent peut aussi avoir des options pour personnaliser des paramètres tels que `max_tokens` utilisés par l'agent, les `tools` que l'agent peut appeler, et même le `model` utilisé pour l'agent.

Ceci est utile dans les cas où des modèles spécifiques ou des outils sont requis pour accomplir la tâche d'un utilisateur.

**Outils**

Les outils peuvent être définis à la fois lors de la définition de l'agent :

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Lors de la création directe d'un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

et aussi lors de l'exécution de l'agent :

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Outil fourni uniquement pour cette exécution )
```

**Threads d’agents**

Les threads d'agents sont utilisés pour gérer les conversations multi-interactions. Les threads peuvent être créés soit par :

- Utilisation de `get_new_thread()` qui permet de sauvegarder le thread dans le temps
- Création automatique d’un thread lors de l'exécution d’un agent et le thread ne dure que pendant l'exécution actuelle.

Pour créer un thread, le code est le suivant :

```python
# Créez un nouveau thread.
thread = agent.get_new_thread() # Exécutez l'agent avec le thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vous pouvez ensuite sérialiser le thread pour le stocker pour une utilisation ultérieure :

```python
# Créer un nouveau fil.
thread = agent.get_new_thread() 

# Exécuter l'agent avec le fil.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sérialiser le fil pour le stockage.

serialized_thread = await thread.serialize() 

# Désérialiser l'état du fil après le chargement depuis le stockage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware d’agents**

Les agents interagissent avec les outils et les LLM pour accomplir les tâches des utilisateurs. Dans certains scénarios, nous voulons exécuter ou suivre des actions entre ces interactions. Le middleware d'agent nous permet de faire cela via :

*Middleware de fonction*

Ce middleware nous permet d'exécuter une action entre l'agent et une fonction/outil qu'il appelle. Un exemple d’utilisation serait pour faire du logging sur l’appel de fonction.

Dans le code ci-dessous, `next` définit si le middleware suivant ou la fonction réelle doit être appelée.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-traitement : Journaliser avant l'exécution de la fonction
    print(f"[Function] Calling {context.function.name}")

    # Continuer vers le middleware suivant ou l'exécution de la fonction
    await next(context)

    # Post-traitement : Journaliser après l'exécution de la fonction
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Ce middleware nous permet d’exécuter ou enregistrer une action entre l’agent et les requêtes vers le LLM.

Cela contient des informations importantes telles que les `messages` qui sont envoyés au service IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-traitement : Journaliser avant l'appel à l'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuer vers le middleware ou le service IA suivant
    await next(context)

    # Post-traitement : Journaliser après la réponse de l'IA
    print("[Chat] AI response received")

```

**Mémoire d’agents**

Comme expliqué dans la leçon `Agentic Memory`, la mémoire est un élément important pour permettre à l'agent d'opérer sur différents contextes. MAF propose plusieurs types de mémoires :

*Stockage en mémoire vive*

C'est la mémoire stockée dans les threads durant l'exécution de l'application.

```python
# Créer un nouveau thread.
thread = agent.get_new_thread() # Exécuter l'agent avec le thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messages persistants*

Cette mémoire est utilisée pour stocker l’historique de conversation à travers différentes sessions. Elle est définie en utilisant la `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Créez un magasin de messages personnalisé
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Mémoire dynamique*

Cette mémoire est ajoutée au contexte avant que les agents ne soient exécutés. Ces mémoires peuvent être stockées dans des services externes tels que mem0 :

```python
from agent_framework.mem0 import Mem0Provider

# Utilisation de Mem0 pour des capacités mémoire avancées
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Observabilité des agents**

L'observabilité est importante pour construire des systèmes agentiques fiables et maintenables. MAF s'intègre à OpenTelemetry pour fournir du tracing et des métriques pour une meilleure observabilité.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # faire quelque chose
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF propose des workflows qui sont des étapes pré-définies pour accomplir une tâche et intègrent les agents IA comme composants dans ces étapes.

Les workflows sont composés de différents composants qui permettent un meilleur contrôle du flux. Les workflows permettent également une **orchestration multi-agent** et un **checkpointing** pour sauvegarder l'état des workflows.

Les composants principaux d’un workflow sont :

**Exécuteurs**

Les exécuteurs reçoivent des messages d’entrée, réalisent les tâches qui leur sont assignées, puis produisent un message de sortie. Cela fait avancer le workflow vers l’achèvement de la tâche globale. Les exécuteurs peuvent être soit des agents IA soit de la logique personnalisée.

**Arêtes**

Les arêtes servent à définir le flux des messages dans un workflow. Elles peuvent être :

*Arêtes directes* - Connexions simples un-à-un entre exécuteurs :

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arêtes conditionnelles* - Activées après qu’une certaine condition est remplie. Par exemple, quand des chambres d’hôtel ne sont pas disponibles, un exécuteur peut suggérer d’autres options.

*Arêtes de type switch-case* - Routent les messages vers différents exécuteurs basés sur des conditions définies. Par exemple, si un client voyageur a un accès prioritaire, sa tâche sera traitée via un autre workflow.

*Arêtes de type fan-out* - Envoient un message à plusieurs cibles.

*Arêtes de type fan-in* - Collectent plusieurs messages provenant de différents exécuteurs et les envoient vers une cible unique.

**Événements**

Pour offrir une meilleure observabilité des workflows, MAF propose des événements intégrés pour l’exécution tels que :

- `WorkflowStartedEvent`  - Début d’exécution du workflow
- `WorkflowOutputEvent` - Le workflow produit une sortie
- `WorkflowErrorEvent` - Le workflow rencontre une erreur
- `ExecutorInvokeEvent`  - L’exécuteur commence son traitement
- `ExecutorCompleteEvent`  - L’exécuteur termine son traitement
- `RequestInfoEvent` - Une requête est émise

## Modèles avancés MAF

Les sections ci-dessus couvrent les concepts clés du Microsoft Agent Framework. Au fur et à mesure que vous construisez des agents plus complexes, voici quelques modèles avancés à considérer :

- **Composition de middleware** : Chaînez plusieurs gestionnaires middleware (logging, auth, limitation de débit) utilisant le middleware de fonction et de chat pour un contrôle fin du comportement de l’agent.
- **Checkpointing des workflows** : Utilisez les événements de workflow et la sérialisation pour sauvegarder et reprendre des processus d’agents longs.
- **Sélection dynamique d’outils** : Combinez le RAG sur les descriptions d’outils avec l’enregistrement d’outils de MAF pour présenter uniquement les outils pertinents par requête.
- **Transfert multi-agent** : Utilisez les arêtes des workflows et le routage conditionnel pour orchestrer les transferts entre agents spécialisés.

## Héberger des agents LangChain / LangGraph sur Microsoft Foundry

Microsoft Agent Framework est **interopérable avec d’autres frameworks** — vous n’êtes pas limité aux agents écrits avec MAF. Si vous avez déjà un agent construit avec **LangChain** ou **LangGraph**, vous pouvez l’exécuter comme un **agent hébergé Microsoft Foundry** afin que Foundry gère l’exécution, les sessions, la montée en charge, l’identité et les points de terminaison du protocole pour vous, tandis que la logique de votre agent reste dans LangGraph.

Cela se fait avec le paquet `langchain_azure_ai.agents.hosting`, qui expose un graphe LangGraph compilé sur les mêmes protocoles utilisés par les agents hébergés Foundry.

**1. Installez l’extension hosting :**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

L’extension `hosting` installe les bibliothèques du protocole Foundry : `azure-ai-agentserver-responses` (le point de terminaison `/responses` compatible OpenAI) et `azure-ai-agentserver-invocations` (le point générique `/invocations`).

**2. Choisissez un protocole d’hébergement :**

| Protocole | Classe d’hôte | Point de terminaison | Utilisation |
|----------|----------------|---------------------|------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Vous souhaitez un chat compatible OpenAI, streaming, historique des réponses et conversation en threads — recommandé par défaut pour les agents conversationnels. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vous avez besoin d’une forme JSON personnalisée, un point de terminaison de type webhook, ou un traitement non conversationnel. |

Parce que **l’API Responses est l’API principale pour le développement d’agents dans Foundry**, commencez avec `ResponsesHostServer` pour la plupart des agents.

**3. Configurez les variables d’environnement** (`az login` au préalable pour que `DefaultAzureCredential` puisse s’authentifier) :

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Quand l’agent s’exécutera plus tard en tant qu’agent hébergé dans Foundry, la plateforme injectera automatiquement `FOUNDRY_PROJECT_ENDPOINT`.

**4. Exposez un agent LangGraph sur le protocole Responses :**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI ici cible le point de terminaison OpenAI-compatible (Responses) du projet Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Exécutez-le localement avec `python main.py`, puis envoyez une requête Responses à `http://localhost:8088/responses`.

**Comportements clés :**

- **Conversations** : Les clients continuent une conversation en passant `previous_response_id` ou un ID de `conversation`. Si votre graphe est compilé avec un checkpointer LangGraph, Foundry associe l’état de la conversation au checkpoint (utilisez un checkpointer durable en production ; `MemorySaver` suffit pour les tests locaux).
- **Humain dans la boucle** : Si votre graphe utilise `interrupt()` de LangGraph, `ResponsesHostServer` affiche l’interruption en attente en tant qu’élément `function_call` / `mcp_approval_request` de Responses, et les clients reprennent avec un `function_call_output` / `mcp_approval_response` correspondant.
- **Déployer sur Foundry** : Utilisez Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, nécessite Docker), puis `azd provision` et `azd deploy`. Le déploiement d’agent hébergé nécessite le rôle **Foundry Project Manager**.

Une version exécutable de cet exemple se trouve dans [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pour le guide complet (protocole Invocations, schémas de requêtes personnalisés et dépannage), consultez [Héberger des agents LangGraph en tant qu’agents Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemples de code 

Des exemples de code pour Microsoft Agent Framework sont disponibles dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Vous avez plus de questions sur Microsoft Agent Framework ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.
## Leçon précédente

[Mémoire pour les agents IA](../13-agent-memory/README.md)

## Leçon suivante

[Construction d'agents pour l'utilisation de l'ordinateur (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->