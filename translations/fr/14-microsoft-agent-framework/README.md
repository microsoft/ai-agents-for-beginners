# Explorer le Microsoft Agent Framework

![Agent Framework](../../../translated_images/fr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Cette leçon couvrira :

- Comprendre Microsoft Agent Framework : fonctionnalités clés et valeur  
- Explorer les concepts clés de Microsoft Agent Framework
- Modèles avancés de MAF : flux de travail, middleware et mémoire

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Construire des agents IA prêts pour la production avec Microsoft Agent Framework
- Appliquer les fonctionnalités de base de Microsoft Agent Framework à vos cas d'utilisation agentiques
- Utiliser des modèles avancés incluant les flux de travail, le middleware et l'observabilité

## Exemples de code 

Des exemples de code pour [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Comprendre Microsoft Agent Framework

![Framework Intro](../../../translated_images/fr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) est le cadre unifié de Microsoft pour construire des agents IA. Il offre la flexibilité nécessaire pour répondre à la grande variété de cas d'utilisation agentiques observés en production et en recherche, notamment :

- **Orchestration séquentielle d'agents** dans les scénarios où des flux de travail étape par étape sont nécessaires.
- **Orchestration concurrente** dans les scénarios où les agents doivent accomplir des tâches simultanément.
- **Orchestration de groupe de discussion** dans les scénarios où les agents peuvent collaborer ensemble sur une tâche.
- **Orchestration de transfert** dans les scénarios où les agents se transmettent la tâche au fur et à mesure que les sous-tâches sont terminées.
- **Orchestration magnétique** dans les scénarios où un agent gestionnaire crée et modifie une liste de tâches et gère la coordination des sous-agents pour compléter la tâche.

Pour livrer des agents IA en production, MAF comprend également des fonctionnalités pour :

- **Observabilité** via l'utilisation d'OpenTelemetry où chaque action de l'agent IA incluant l'invocation d'outils, les étapes d'orchestration, les flux de raisonnement et la surveillance des performances via les tableaux de bord Microsoft Foundry.
- **Sécurité** en hébergeant les agents nativement sur Microsoft Foundry, qui inclut des contrôles de sécurité tels que l'accès basé sur les rôles, la gestion des données privées et la sécurité intégrée du contenu.
- **Durabilité** car les threads et flux de travail des agents peuvent être mis en pause, repris et récupérer d'erreurs, ce qui permet des processus de longue durée.
- **Contrôle** car les flux de travail avec intervention humaine sont supportés où les tâches sont marquées comme nécessitant une approbation humaine.

Microsoft Agent Framework est également axé sur l'interopérabilité par :

- **Être agnostique au cloud** – les agents peuvent fonctionner dans des conteneurs, sur site et à travers plusieurs clouds différents.
- **Être agnostique au fournisseur** – les agents peuvent être créés via votre SDK préféré incluant Azure OpenAI et OpenAI
- **Intégrer des standards ouverts** – les agents peuvent utiliser des protocoles tels que Agent-to-Agent (A2A) et Model Context Protocol (MCP) pour découvrir et utiliser d'autres agents et outils.
- **Plugins et connecteurs** – des connexions peuvent être faites vers des services de données et de mémoire tels que Microsoft Fabric, SharePoint, Pinecone et Qdrant.

Regardons comment ces fonctionnalités s'appliquent à quelques concepts clés de Microsoft Agent Framework.

## Concepts clés de Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/fr/agent-components.410a06daf87b4fef.webp)

**Création d'agents**

La création d'agent se fait en définissant le service d'inférence (fournisseur LLM), un
ensemble d'instructions que l'agent IA doit suivre, et un `nom` attribué :

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ce qui précède utilise `Azure OpenAI` mais les agents peuvent être créés en utilisant une variété de services incluant `Microsoft Foundry Agent Service` :

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

ou [MiniMax](https://platform.minimaxi.com/), qui offre une API compatible OpenAI avec de grandes fenêtres de contexte (jusqu'à 204K tokens) :

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou des agents distants utilisant le protocole A2A :

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Exécution des agents**

Les agents sont exécutés en utilisant les méthodes `.run` ou `.run_stream` pour des réponses non-streaming ou streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Chaque exécution d'agent peut également avoir des options pour personnaliser des paramètres tels que les `max_tokens` utilisés par l'agent, les `outils` que l'agent est capable d'appeler, et même le `modèle` utilisé pour l'agent.

Ceci est utile dans les cas où des modèles ou outils spécifiques sont nécessaires pour compléter la tâche d'un utilisateur.

**Outils**

Les outils peuvent être définis aussi bien lors de la définition de l'agent :

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Lors de la création directe d'un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

que lors de l'exécution de l'agent :

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Outil fourni uniquement pour cette exécution )
```

**Threads d'agents**

Les threads d'agents sont utilisés pour gérer des conversations multi-tours. Les threads peuvent être créés soit par :

- Utilisation de `get_new_thread()` ce qui permet de sauvegarder le thread au fil du temps
- Création automatique d'un thread lors de l'exécution d'un agent avec le thread valant uniquement pour la durée de l'exécution actuelle.

Pour créer un thread, le code ressemble à ceci :

```python
# Créez un nouveau fil.
thread = agent.get_new_thread() # Exécutez l'agent avec le fil.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vous pouvez ensuite sérialiser le thread pour le stocker et l'utiliser plus tard :

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

**Middleware d'agent**

Les agents interagissent avec des outils et des LLM pour accomplir les tâches des utilisateurs. Dans certains scénarios, on souhaite exécuter ou suivre des actions entre ces interactions. Le middleware d'agent nous permet de faire cela via :

*Middleware fonctionnel*

Ce middleware permet d'exécuter une action entre l'agent et une fonction/outil qu'il va appeler. Un exemple d'utilisation est pour faire des logs sur l'appel de fonction.

Dans le code ci-dessous, `next` définit si le middleware suivant ou la fonction elle-même doit être appelée.

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

Ce middleware permet d'exécuter ou de journaliser une action entre l'agent et les requêtes entre le LLM.

Cela contient des informations importantes telles que les `messages` qui sont envoyés au service IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-traitement : Journaliser avant l'appel à l'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuer vers le middleware ou le service d'IA suivant
    await next(context)

    # Post-traitement : Journaliser après la réponse de l'IA
    print("[Chat] AI response received")

```

**Mémoire d'agent**

Comme abordé dans la leçon `Mémoire agentique`, la mémoire est un élément important pour permettre à l'agent d'opérer sur différents contextes. MAF offre plusieurs types de mémoires :

*Stockage en mémoire*

Ceci est la mémoire stockée dans les threads pendant l'exécution de l'application.

```python
# Créer un nouveau thread.
thread = agent.get_new_thread() # Exécuter l'agent avec le thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messages persistants*

Cette mémoire est utilisée pour stocker l'historique des conversations à travers différentes sessions. Elle est définie en utilisant la `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Créer un magasin de messages personnalisé
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Mémoire dynamique*

Cette mémoire est ajoutée au contexte avant que les agents soient exécutés. Ces mémoires peuvent être stockées dans des services externes tels que mem0 :

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

**Observabilité d'agent**

L'observabilité est importante pour construire des systèmes agentiques fiables et maintenables. MAF s'intègre avec OpenTelemetry pour fournir le traçage et les métriques pour une meilleure observabilité.

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

### Flux de travail

MAF offre des flux de travail constitués d'étapes prédéfinies pour accomplir une tâche et incluant des agents IA comme composants de ces étapes.

Les flux de travail sont composés de différents composants qui permettent un meilleur contrôle du flux. Ils permettent également l'**orchestration multi-agent** et le **point de contrôle** pour sauvegarder les états du flux de travail.

Les composants principaux d'un flux de travail sont :

**Exécuteurs**

Les exécuteurs reçoivent les messages d'entrée, effectuent les tâches qui leur sont assignées, puis produisent un message de sortie. Cela fait avancer le flux de travail vers l'accomplissement de la tâche globale. Les exécuteurs peuvent être un agent IA ou une logique personnalisée.

**Arêtes**

Les arêtes sont utilisées pour définir le flux des messages dans un flux de travail. Celles-ci peuvent être :

*Arêtes directes* – Connexions simples un-à-un entre exécuteurs :

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arêtes conditionnelles* – Activées après qu'une certaine condition est remplie. Par exemple, quand les chambres d'hôtel sont indisponibles, un exécuteur peut proposer d'autres options.

*Arêtes switch-case* – Acheminer les messages vers différents exécuteurs selon des conditions définies. Par exemple, si un client voyageur a un accès prioritaire, ses tâches seront gérées par un autre flux de travail.

*Arêtes en diffusion* – Envoyer un message à plusieurs destinataires.

*Arêtes en collecte* – Collecter plusieurs messages de différents exécuteurs et envoyer à un seul destinataire.

**Événements**

Pour fournir une meilleure observabilité des flux de travail, MAF offre des événements intégrés pour l'exécution dont :

- `WorkflowStartedEvent` – L'exécution du flux de travail commence
- `WorkflowOutputEvent` – Le flux de travail produit une sortie
- `WorkflowErrorEvent` – Le flux de travail rencontre une erreur
- `ExecutorInvokeEvent` – L’exécuteur commence le traitement
- `ExecutorCompleteEvent` – L’exécuteur termine le traitement
- `RequestInfoEvent` – Une requête est émise

## Modèles avancés de MAF

Les sections ci-dessus couvrent les concepts clés de Microsoft Agent Framework. Lorsque vous construisez des agents plus complexes, voici des modèles avancés à considérer :

- **Composition de Middleware** : Chaîner plusieurs gestionnaires de middleware (journalisation, authentification, limitation de débit) en utilisant le middleware fonctionnel et de chat pour un contrôle fin du comportement des agents.
- **Point de contrôle des flux de travail** : Utiliser les événements de flux de travail et la sérialisation pour sauvegarder et reprendre les processus d'agents de longue durée.
- **Sélection dynamique d'outils** : Combiner RAG sur les descriptions d'outils avec l'enregistrement d'outils de MAF pour présenter uniquement les outils pertinents par requête.
- **Transfert multi-agent** : Utiliser les arêtes de flux de travail et le routage conditionnel pour orchestrer les transferts entre agents spécialisés.

## Héberger des agents LangChain / LangGraph sur Microsoft Foundry

Microsoft Agent Framework est **interopérable avec différents frameworks** – vous n’êtes pas limité aux agents écrits avec MAF. Si vous avez déjà un agent construit avec **LangChain** ou **LangGraph**, vous pouvez l'exécuter en tant qu'**agent hébergé Microsoft Foundry** afin que Foundry gère le runtime, les sessions, la mise à l'échelle, l'identité et les points de terminaison de protocole pour vous, tandis que votre logique d’agent reste dans LangGraph.

Ceci se fait avec le package `langchain_azure_ai.agents.hosting` qui expose un graphe LangGraph compilé via les mêmes protocoles que ceux utilisés par les agents hébergés Foundry.

**1. Installez l'extra hosting :**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

L'extra `hosting` installe les bibliothèques de protocole Foundry : `azure-ai-agentserver-responses` (le point de terminaison `/responses` compatible OpenAI) et `azure-ai-agentserver-invocations` (le point de terminaison générique `/invocations`).

**2. Choisissez un protocole d'hébergement :**

| Protocole | Classe d'hôte | Point de terminaison | Utilisation recommandée |
|----------|---------------|---------------------|------------------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Vous voulez un chat compatible OpenAI, streaming, historique des réponses et threading de conversation — le choix par défaut recommandé pour les agents conversationnels. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vous avez besoin d'une forme JSON personnalisée, d'un point de terminaison à la manière webhook ou d'un traitement non conversationnel. |

Comme **l'API Responses est l'API principale pour le développement d'agents dans Foundry**, commencez avec `ResponsesHostServer` pour la plupart des agents.

**3. Configurez les variables d'environnement** (`az login` d'abord pour que `DefaultAzureCredential` puisse s'authentifier) :

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Lorsque l'agent s'exécute plus tard en tant qu'agent hébergé dans Foundry, la plateforme injecte automatiquement `FOUNDRY_PROJECT_ENDPOINT`.

**4. Exposez un agent LangGraph via le protocole Responses :**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
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

- **Conversations** : Les clients continuent une conversation en passant `previous_response_id` ou un ID de `conversation`. Si votre graphe est compilé avec un point de contrôle LangGraph, Foundry associe l'état de conversation au point de contrôle (utilisez un point de contrôle durable en production ; `MemorySaver` convient pour les tests locaux).
- **Intervention humaine** : Si votre graphe utilise `interrupt()` de LangGraph, `ResponsesHostServer` affiche l'interruption en attente comme un item `function_call` / `mcp_approval_request` dans Responses, et les clients reprennent avec un `function_call_output` / `mcp_approval_response` correspondant.
- **Déploiement sur Foundry** : Utilisez Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, nécessite Docker), puis `azd provision` et `azd deploy`. Le déploiement d'agents hébergés requiert le rôle **Foundry Project Manager**.

Une version exécutable de cet exemple se trouve dans [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pour le guide complet (protocole Invocations, schémas de requête personnalisés, dépannage), consultez [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemples de code 

Des exemples de code pour Microsoft Agent Framework sont disponibles dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Vous avez d'autres questions sur Microsoft Agent Framework ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.
## Leçon précédente

[Mémoire pour les agents IA](../13-agent-memory/README.md)

## Leçon suivante

[Construction d'agents d'utilisation informatique (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->