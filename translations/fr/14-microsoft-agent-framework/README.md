# Explorer Microsoft Agent Framework

![Framework d'agent](../../../translated_images/fr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Cette leçon couvrira :

- Comprendre Microsoft Agent Framework : fonctionnalités clés et valeur  
- Explorer les concepts clés de Microsoft Agent Framework
- Modèles MAF avancés : workflows, middleware et mémoire

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Construire des agents IA prêts pour la production en utilisant Microsoft Agent Framework
- Appliquer les fonctionnalités principales de Microsoft Agent Framework à vos cas d'utilisation agentiques
- Utiliser des modèles avancés incluant workflows, middleware et observabilité

## Exemples de code 

Les exemples de code pour [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Comprendre Microsoft Agent Framework

![Introduction au Framework](../../../translated_images/fr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) est le cadre unifié de Microsoft pour la construction d'agents IA. Il offre la flexibilité nécessaire pour traiter la grande variété de cas d'utilisation agentiques observés en production et en recherche, notamment :

- **Orchestration séquentielle d'agents** dans des scénarios où des workflows étape par étape sont nécessaires.
- **Orchestration concurrente** dans des scénarios où les agents doivent accomplir des tâches en même temps.
- **Orchestration de chat de groupe** dans des scénarios où les agents peuvent collaborer ensemble sur une même tâche.
- **Orchestration de transfert (Handoff)** dans des scénarios où les agents se transfèrent la tâche les uns aux autres à mesure que les sous-tâches sont terminées.
- **Orchestration magnétique** dans des scénarios où un agent manager crée et modifie une liste de tâches et gère la coordination des sous-agents pour accomplir la tâche.

Pour délivrer des agents IA en production, MAF inclut également des fonctionnalités pour :

- **Observabilité** via l'utilisation d'OpenTelemetry où chaque action de l'agent IA, y compris l'invocation d'outils, les étapes d'orchestration, les flux de raisonnement et la surveillance des performances, est disponible via les tableaux de bord Microsoft Foundry.
- **Sécurité** en hébergeant les agents nativement sur Microsoft Foundry, qui inclut des contrôles de sécurité tels que l'accès basé sur les rôles, la gestion des données privées et la sécurité de contenu intégrée.
- **Durabilité** puisque les threads et workflows d'agent peuvent faire une pause, reprendre et récupérer des erreurs, ce qui permet des processus de plus longue durée.
- **Contrôle** avec le support des workflows « humain dans la boucle » où les tâches sont marquées comme nécessitant une approbation humaine.

Microsoft Agent Framework est également axé sur l'interopérabilité en :

- **Étant agnostique au cloud** - Les agents peuvent s'exécuter dans des conteneurs, sur site et à travers plusieurs clouds différents.
- **Étant agnostique au fournisseur** - Les agents peuvent être créés via votre SDK préféré, y compris Azure OpenAI et OpenAI
- **Intégrant des standards ouverts** - Les agents peuvent utiliser des protocoles tels que Agent-to-Agent (A2A) et Model Context Protocol (MCP) pour découvrir et utiliser d'autres agents et outils.
- **Plugins et connecteurs** - Des connexions peuvent être établies vers des services de données et de mémoire tels que Microsoft Fabric, SharePoint, Pinecone et Qdrant.

Voyons comment ces fonctionnalités s'appliquent à certains des concepts clés de Microsoft Agent Framework.

## Concepts clés de Microsoft Agent Framework

### Agents

![Framework d'agent](../../../translated_images/fr/agent-components.410a06daf87b4fef.webp)

**Création d'agents**

La création d'un agent se fait en définissant le service d'inférence (LLM Provider), un ensemble d'instructions que l'agent IA doit suivre, et un `name` attribué :

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ce qui précède utilise `Azure OpenAI` mais les agents peuvent être créés en utilisant une variété de services incluant `Microsoft Foundry Agent Service` :

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou des agents distants en utilisant le protocole A2A :

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Exécution des agents**

Les agents sont exécutés en utilisant les méthodes `.run` ou `.run_stream` pour des réponses non-streaming ou en streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Chaque exécution d'agent peut également avoir des options pour personnaliser des paramètres tels que `max_tokens` utilisés par l'agent, les `tools` que l'agent peut appeler, et même le `model` lui-même utilisé par l'agent.

Ceci est utile dans les cas où des modèles ou outils spécifiques sont requis pour accomplir la tâche d'un utilisateur.

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

Les threads d'agent sont utilisés pour gérer des conversations à plusieurs tours. Les threads peuvent être créés soit :

- En utilisant `get_new_thread()` ce qui permet de sauvegarder le thread au fil du temps
- En créant un thread automatiquement lors de l'exécution d'un agent et en ne faisant durer le thread que pendant l'exécution en cours.

Pour créer un thread, le code ressemble à ceci :

```python
# Créer un nouveau thread.
thread = agent.get_new_thread() # Exécuter l'agent avec le thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vous pouvez ensuite sérialiser le thread pour le stocker et l'utiliser ultérieurement :

```python
# Créer un nouveau fil d'exécution.
thread = agent.get_new_thread() 

# Lancer l'agent dans le fil d'exécution.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sérialiser le fil d'exécution pour le stockage.

serialized_thread = await thread.serialize() 

# Désérialiser l'état du fil d'exécution après le chargement depuis le stockage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware d'agent**

Les agents interagissent avec des outils et des LLM pour accomplir les tâches des utilisateurs. Dans certains scénarios, nous voulons exécuter ou suivre des actions entre ces interactions. Le middleware d'agent nous permet de le faire via :

*Middleware de fonction*

Ce middleware nous permet d'exécuter une action entre l'agent et une fonction/outil qu'il appellera. Un exemple d'utilisation est lorsque vous souhaitez effectuer des journaux (logging) sur l'appel de fonction.

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

Ce middleware nous permet d'exécuter ou d'enregistrer une action entre l'agent et les requêtes vers le LLM.

Il contient des informations importantes telles que les `messages` qui sont envoyés au service IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-traitement : journaliser avant l'appel à l'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Passer au middleware suivant ou au service d'IA
    await next(context)

    # Post-traitement : journaliser après la réponse de l'IA
    print("[Chat] AI response received")

```

**Mémoire d'agent**

Comme abordé dans la leçon `Agentic Memory`, la mémoire est un élément important pour permettre à l'agent d'opérer sur différents contextes. MAF propose plusieurs types de mémoires :

*Stockage en mémoire*

Il s'agit de la mémoire stockée dans les threads pendant l'exécution de l'application.

```python
# Créer un nouveau fil d'exécution.
thread = agent.get_new_thread() # Exécuter l'agent avec le fil d'exécution.
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

Cette mémoire est ajoutée au contexte avant que les agents ne soient exécutés. Ces mémoires peuvent être stockées dans des services externes tels que mem0 :

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

L'observabilité est importante pour construire des systèmes agentiques fiables et maintenables. MAF s'intègre avec OpenTelemetry pour fournir des traces et des compteurs pour une meilleure observabilité.

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

MAF propose des workflows qui sont des étapes pré-définies pour accomplir une tâche et incluent des agents IA comme composants de ces étapes.

Les workflows sont composés de différents composants qui permettent un meilleur contrôle du flux. Les workflows permettent également l'**orchestration multi-agent** et le **checkpointing** pour sauvegarder les états du workflow.

Les composants principaux d'un workflow sont :

**Exécuteurs**

Les exécuteurs reçoivent des messages d'entrée, effectuent les tâches qui leur sont assignées, puis produisent un message de sortie. Cela fait avancer le workflow vers l'accomplissement de la tâche globale. Les exécuteurs peuvent être soit des agents IA soit de la logique personnalisée.

**Arêtes**

Les arêtes sont utilisées pour définir le flux des messages dans un workflow. Celles-ci peuvent être :

*Arêtes directes* - Connexions simples un-à-un entre exécuteurs :

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arêtes conditionnelles* - Activées après qu'une certaine condition est remplie. Par exemple, lorsque des chambres d'hôtel ne sont pas disponibles, un exécuteur peut suggérer d'autres options.

*Arêtes de type switch-case* - Acheminent les messages vers différents exécuteurs en fonction de conditions définies. Par exemple, si un client voyageur a un accès prioritaire, ses tâches seront traitées via un autre workflow.

*Arêtes de fan-out* - Envoyer un message à plusieurs cibles.

*Arêtes de fan-in* - Collecter plusieurs messages provenant de différents exécuteurs et les envoyer à une seule cible.

**Événements**

Pour fournir une meilleure observabilité des workflows, MAF propose des événements intégrés pour l'exécution, notamment :

- `WorkflowStartedEvent`  - Début d'exécution du workflow
- `WorkflowOutputEvent` - Le workflow produit une sortie
- `WorkflowErrorEvent` - Le workflow rencontre une erreur
- `ExecutorInvokeEvent`  - L'exécuteur commence le traitement
- `ExecutorCompleteEvent`  -  L'exécuteur termine le traitement
- `RequestInfoEvent` - Une requête est émise

## Modèles avancés de MAF

Les sections ci-dessus couvrent les concepts clés de Microsoft Agent Framework. À mesure que vous construisez des agents plus complexes, voici quelques modèles avancés à considérer :

- **Composition de middleware** : Chaînez plusieurs gestionnaires de middleware (journaux, auth, limitation de débit) en utilisant le middleware de fonction et de chat pour un contrôle granulaire du comportement des agents.
- **Checkpointing de workflow** : Utilisez les événements de workflow et la sérialisation pour sauvegarder et reprendre les processus d'agent de longue durée.
- **Sélection dynamique d'outils** : Combinez RAG sur les descriptions d'outils avec l'enregistrement d'outils de MAF pour présenter uniquement les outils pertinents par requête.
- **Transfert multi-agent** : Utilisez les arêtes de workflow et le routage conditionnel pour orchestrer les transferts entre agents spécialisés.

## Exemples de code 

Les exemples de code pour Microsoft Agent Framework se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Vous avez d'autres questions sur Microsoft Agent Framework ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->