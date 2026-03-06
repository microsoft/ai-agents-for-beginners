# Explorer Microsoft Agent Framework

![Framework d'Agent](../../../translated_images/fr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Cette leçon couvrira :

- Comprendre Microsoft Agent Framework : fonctionnalités clés et valeur  
- Explorer les concepts clés de Microsoft Agent Framework
- Patrons avancés de MAF : flux de travail, middleware et mémoire

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Créer des agents IA prêts pour la production en utilisant Microsoft Agent Framework
- Appliquer les fonctionnalités principales de Microsoft Agent Framework à vos cas d'utilisation axés sur des agents
- Utiliser des patrons avancés incluant les flux de travail, le middleware et l'observabilité

## Exemples de code 

Les exemples de code pour [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Comprendre Microsoft Agent Framework

![Introduction au Framework](../../../translated_images/fr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) est le framework unifié de Microsoft pour construire des agents IA. Il offre la flexibilité nécessaire pour couvrir la grande variété de cas d'utilisation axés sur des agents rencontrés en production comme en recherche, notamment :

- **Orchestration séquentielle d'agents** dans des scénarios nécessitant des flux de travail étape par étape.
- **Orchestration concurrente** dans des scénarios où les agents doivent achever des tâches simultanément.
- **Orchestration de chat de groupe** dans des scénarios où des agents peuvent collaborer sur une même tâche.
- **Orchestration de transfert** dans des scénarios où les agents se transfèrent la tâche au fur et à mesure que les sous-tâches sont accomplies.
- **Orchestration magnétique** dans des scénarios où un agent responsable crée et modifie une liste de tâches et gère la coordination des sous-agents pour accomplir la tâche.

Pour déployer des agents IA en production, MAF inclut également des fonctionnalités pour :

- **Observabilité** via OpenTelemetry où chaque action de l'agent IA, y compris l'invocation d'outils, les étapes d'orchestration, les flux de raisonnement et la surveillance des performances via les tableaux de bord Microsoft Foundry.
- **Sécurité** en hébergeant les agents nativement sur Microsoft Foundry, qui inclut des contrôles de sécurité tels que l'accès basé sur les rôles, la gestion des données privées et la sécurité de contenu intégrée.
- **Durabilité** : les threads et flux de travail des agents peuvent être mis en pause, repris et récupérés après des erreurs, ce qui permet des processus de plus longue durée.
- **Contrôle** : les workflows avec intervention humaine sont pris en charge, où des tâches sont marquées comme nécessitant une approbation humaine.

Microsoft Agent Framework vise également l'interopérabilité en :

- **Être agnostique au cloud** - Les agents peuvent s'exécuter dans des conteneurs, sur site et à travers plusieurs clouds différents.
- **Être agnostique vis-à-vis des fournisseurs** - Les agents peuvent être créés via le SDK de votre choix, y compris Azure OpenAI et OpenAI
- **Intégration de standards ouverts** - Les agents peuvent utiliser des protocoles tels que Agent-to-Agent(A2A) et Model Context Protocol (MCP) pour découvrir et utiliser d'autres agents et outils.
- **Plugins et connecteurs** - Des connexions peuvent être établies vers des services de données et de mémoire tels que Microsoft Fabric, SharePoint, Pinecone et Qdrant.

Regardons comment ces fonctionnalités s'appliquent à certains des concepts centraux de Microsoft Agent Framework.

## Concepts clés de Microsoft Agent Framework

### Agents

![Composants de l'Agent](../../../translated_images/fr/agent-components.410a06daf87b4fef.webp)

**Création d'agents**

La création d'un agent se fait en définissant le service d'inférence (LLM Provider), un ensemble d'instructions que l'agent IA doit suivre, et un `name` assigné :

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ce qui précède utilise `Azure OpenAI`, mais les agents peuvent être créés en utilisant une variété de services, y compris `Microsoft Foundry Agent Service` :

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

ou des agents distants utilisant le protocole A2A :

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Exécution des agents**

Les agents sont exécutés en utilisant les méthodes `.run` ou `.run_stream` pour des réponses non-streaming ou streamées.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Chaque exécution d'agent peut également inclure des options pour personnaliser des paramètres tels que `max_tokens` utilisés par l'agent, les `tools` que l'agent peut appeler, et même le `model` lui-même utilisé par l'agent.

Ceci est utile lorsque des modèles ou outils spécifiques sont nécessaires pour accomplir la tâche d'un utilisateur.

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

**Threads d'agent**

Les threads d'agent sont utilisés pour gérer des conversations multi-tours. Les threads peuvent être créés de deux manières :

- En utilisant `get_new_thread()` qui permet de sauvegarder le thread au fil du temps
- En créant un thread automatiquement lors de l'exécution d'un agent, le thread ne durant alors que pendant l'exécution en cours.

Pour créer un thread, le code ressemble à ceci :

```python
# Créer un nouveau fil d'exécution.
thread = agent.get_new_thread() # Exécuter l'agent avec le fil d'exécution.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vous pouvez ensuite sérialiser le thread pour le stocker et l'utiliser ultérieurement :

```python
# Créer un nouveau fil d'exécution.
thread = agent.get_new_thread() 

# Exécuter l'agent avec le fil d'exécution.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sérialiser le fil d'exécution pour le stockage.

serialized_thread = await thread.serialize() 

# Désérialiser l'état du fil d'exécution après le chargement depuis le stockage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware d'agent**

Les agents interagissent avec des outils et des LLM pour accomplir les tâches des utilisateurs. Dans certains scénarios, nous souhaitons exécuter ou suivre des actions entre ces interactions. Le middleware d'agent nous permet de faire cela via :

*Middleware de fonction*

Ce middleware nous permet d'exécuter une action entre l'agent et une fonction/outil qu'il appelle. Un exemple d'utilisation serait lorsqu'on souhaite effectuer du logging sur l'appel de la fonction.

Dans le code ci-dessous, `next` définit si le middleware suivant ou la fonction réelle doit être appelée.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-traitement : consigner avant l'exécution de la fonction
    print(f"[Function] Calling {context.function.name}")

    # Continuer vers le middleware suivant ou l'exécution de la fonction
    await next(context)

    # Post-traitement : consigner après l'exécution de la fonction
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Ce middleware nous permet d'exécuter ou d'enregistrer une action entre l'agent et les requêtes envoyées au LLM.

Cela contient des informations importantes telles que les `messages` qui sont envoyés au service d'IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-traitement : consigner avant l'appel à l'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuer vers le middleware suivant ou le service d'IA
    await next(context)

    # Post-traitement : consigner après la réponse de l'IA
    print("[Chat] AI response received")

```

**Mémoire d'agent**

Comme abordé dans la leçon `Agentic Memory`, la mémoire est un élément important pour permettre à l'agent d'opérer sur différents contextes. MAF propose plusieurs types de mémoires :

*Stockage en mémoire*

Il s'agit de la mémoire stockée dans les threads pendant l'exécution de l'application.

```python
# Créer un nouveau thread.
thread = agent.get_new_thread() # Exécuter l'agent avec le thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messages persistants*

Cette mémoire est utilisée pour stocker l'historique des conversations entre différentes sessions. Elle est définie en utilisant le `chat_message_store_factory` :

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

Cette mémoire est ajoutée au contexte avant l'exécution des agents. Ces mémoires peuvent être stockées dans des services externes tels que mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Utilisation de Mem0 pour des capacités de mémoire avancées
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

L'observabilité est importante pour construire des systèmes agentiques fiables et faciles à maintenir. MAF s'intègre avec OpenTelemetry pour fournir du traçage et des métriques afin d'améliorer l'observabilité.

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

MAF propose des flux de travail composés d'étapes prédéfinies pour accomplir une tâche et incluant des agents IA comme composants de ces étapes.

Les flux de travail sont constitués de différents composants permettant un meilleur contrôle du déroulement. Ils permettent également l'**orchestration multi-agent** et le **point de contrôle (checkpointing)** pour sauvegarder l'état des flux de travail.

Les composants de base d'un flux de travail sont :

**Exécuteurs**

Les exécuteurs reçoivent des messages d'entrée, effectuent les tâches qui leur sont assignées, puis produisent un message de sortie. Cela fait avancer le flux de travail vers l'achèvement de la tâche globale. Les exécuteurs peuvent être des agents IA ou une logique personnalisée.

**Arêtes**

Les arêtes sont utilisées pour définir le flux des messages dans un flux de travail. Celles-ci peuvent être :

*Arêtes directes* - Connexions simples un-à-un entre exécuteurs :

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arêtes conditionnelles* - Activées après qu'une certaine condition est remplie. Par exemple, lorsque des chambres d'hôtel ne sont pas disponibles, un exécuteur peut suggérer d'autres options.

*Arêtes de type switch-case* - Dirigent les messages vers différents exécuteurs en fonction de conditions définies. Par exemple, si un client voyageur a un accès prioritaire, ses tâches seront traitées via un autre flux de travail.

*Arêtes de fan-out* - Envoient un message vers plusieurs cibles.

*Arêtes de fan-in* - Collectent plusieurs messages de différents exécuteurs et les envoient vers une cible.

**Événements**

Pour offrir une meilleure observabilité des flux de travail, MAF propose des événements intégrés pour l'exécution, notamment :

- `WorkflowStartedEvent`  - Le flux de travail commence l'exécution
- `WorkflowOutputEvent` - Le flux de travail produit une sortie
- `WorkflowErrorEvent` - Le flux de travail rencontre une erreur
- `ExecutorInvokeEvent`  - L'exécuteur commence le traitement
- `ExecutorCompleteEvent`  -  L'exécuteur termine le traitement
- `RequestInfoEvent` - Une requête est émise

## Patrons avancés de MAF

Les sections ci-dessus couvrent les concepts clés de Microsoft Agent Framework. Lorsque vous construisez des agents plus complexes, voici quelques patrons avancés à considérer :

- **Composition de middleware** : enchaînez plusieurs gestionnaires de middleware (journalisation, authentification, limitation de débit) en utilisant le middleware de fonction et de chat pour un contrôle fin du comportement des agents.
- **Checkpointing des workflows** : utilisez les événements de workflow et la sérialisation pour sauvegarder et reprendre des processus d'agents de longue durée.
- **Sélection dynamique d'outils** : combinez la RAG sur les descriptions d'outils avec l'enregistrement d'outils de MAF pour ne présenter que les outils pertinents par requête.
- **Transfert entre agents (Multi-Agent Handoff)** : utilisez les arêtes de workflow et le routage conditionnel pour orchestrer les transferts entre agents spécialisés.

## Exemples de code 

Les exemples de code pour Microsoft Agent Framework se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Vous avez d'autres questions sur Microsoft Agent Framework ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Clause de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'en garantir l'exactitude, veuillez noter que les traductions automatiques peuvent comporter des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->