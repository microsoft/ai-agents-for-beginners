# Exploration du Microsoft Agent Framework

![Agent Framework](../../../translated_images/fr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Cette leçon couvrira :

- Comprendre le Microsoft Agent Framework : Caractéristiques clés et valeur  
- Explorer les concepts clés du Microsoft Agent Framework
- Modèles avancés du MAF : Flux de travail, middleware et mémoire

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez :

- Construire des agents IA prêts pour la production en utilisant le Microsoft Agent Framework
- Appliquer les fonctionnalités principales du Microsoft Agent Framework à vos cas d'utilisation agentiques
- Utiliser des modèles avancés incluant les flux de travail, le middleware et l'observabilité

## Exemples de code 

Des exemples de code pour [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Comprendre le Microsoft Agent Framework

![Framework Intro](../../../translated_images/fr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) est le cadre unifié de Microsoft pour construire des agents IA. Il offre la flexibilité nécessaire pour répondre à la grande variété de cas d'utilisation agentique observés à la fois en production et en recherche, notamment :

- **Orchestration séquentielle d’agents** dans des scénarios nécessitant des flux de travail étape par étape.
- **Orchestration concurrente** dans des scénarios où les agents doivent accomplir des tâches simultanément.
- **Orchestration de chat de groupe** dans des scénarios où les agents collaborent ensemble sur une tâche.
- **Orchestration de transfert** dans des scénarios où les agents se transfèrent la tâche les uns aux autres à mesure que les sous-tâches sont complétées.
- **Orchestration magnétique** dans des scénarios où un agent gestionnaire crée et modifie une liste de tâches et gère la coordination des sous-agents pour accomplir la mission.

Pour déployer des agents IA en production, MAF inclut également des fonctionnalités pour :

- **Observabilité** via l’utilisation d’OpenTelemetry où chaque action de l’agent IA, y compris l’appel d’outils, les étapes d’orchestration, les flux de raisonnement et la surveillance des performances via les tableaux de bord Microsoft Foundry, est suivie.
- **Sécurité** en hébergeant nativement les agents sur Microsoft Foundry comprenant des contrôles de sécurité tels que l’accès basé sur les rôles, la gestion de données privées et la sécurité intégrée du contenu.
- **Durabilité** car les threads et flux de travail des agents peuvent être mis en pause, repris et récupérer des erreurs, ce qui permet des processus longue durée.
- **Contrôle** puisque les flux de travail avec intervention humaine sont supportés où les tâches peuvent être marquées comme nécessitant une approbation humaine.

Microsoft Agent Framework met aussi l'accent sur l’interopérabilité en étant :

- **Cloud-agnostique** - Les agents peuvent s’exécuter dans des conteneurs, sur site et à travers plusieurs clouds différents.
- **Fournisseur-agnostique** - Les agents peuvent être créés via votre SDK préféré incluant Azure OpenAI et OpenAI.
- **Intégrant des standards ouverts** - Les agents peuvent utiliser des protocoles tels que Agent-to-Agent (A2A) et Model Context Protocol (MCP) pour découvrir et utiliser d’autres agents et outils.
- **Plugins et connecteurs** - Des connexions peuvent être établies vers des services de données et de mémoire tels que Microsoft Fabric, SharePoint, Pinecone et Qdrant.

Voyons comment ces fonctionnalités sont appliquées à certains des concepts clés du Microsoft Agent Framework.

## Concepts clés du Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/fr/agent-components.410a06daf87b4fef.webp)

**Création d’Agents**

La création d’un agent se fait en définissant le service d'inférence (fournisseur LLM), un ensemble d’instructions pour l’agent IA à suivre, et un `nom` assigné :

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

L’exemple ci-dessus utilise `Azure OpenAI` mais les agents peuvent être créés avec une variété de services incluant `Microsoft Foundry Agent Service` :

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

ou [MiniMax](https://platform.minimaxi.com/), qui fournit une API compatible OpenAI avec de grandes fenêtres contextuelles (jusqu’à 204K tokens) :

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ou des agents distants utilisant le protocole A2A :

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Exécution des Agents**

Les agents s’exécutent via les méthodes `.run` ou `.run_stream` pour des réponses non-streaming ou en streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Chaque exécution d’agent peut aussi inclure des options pour personnaliser des paramètres tels que `max_tokens` utilisés par l’agent, les `tools` que l’agent peut appeler, et même le `model` utilisé par l’agent.

Ceci est utile dans les cas où des modèles spécifiques ou des outils sont requis pour réaliser la tâche d’un utilisateur.

**Outils**

Les outils peuvent être définis à la fois lors de la définition de l’agent :

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Lors de la création directe d'un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

et aussi lors de l’exécution de l’agent :

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Outil fourni uniquement pour cette exécution )
```

**Threads d’Agent**

Les threads d’agent servent à gérer les conversations à plusieurs tours. Les threads peuvent être créés soit par :

- L’utilisation de `get_new_thread()` qui permet de sauvegarder le thread dans le temps
- La création automatique d’un thread lors de l’exécution d’un agent avec un thread ne durant que la session actuelle.

Pour créer un thread, le code ressemble à ceci :

```python
# Créez un nouveau fil.
thread = agent.get_new_thread() # Exécutez l'agent avec le fil.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vous pouvez ensuite sérialiser le thread pour le stocker et l’utiliser ultérieurement :

```python
# Créer un nouveau fil.
thread = agent.get_new_thread() 

# Exécuter l'agent avec le fil.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sérialiser le fil pour le stockage.

serialized_thread = await thread.serialize() 

# Désérialiser l'état du fil après chargement du stockage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware d’Agent**

Les agents interagissent avec des outils et des LLM pour accomplir les tâches des utilisateurs. Dans certains scénarios, on souhaite exécuter ou suivre les interactions entre ces derniers. Le middleware d’agent nous permet de faire cela via :

*Middleware Fonction*

Ce middleware permet d’exécuter une action entre l’agent et une fonction/outils qu’il va appeler. Un exemple d’utilisation est lorsqu’on souhaite faire un journal des appels de fonction.

Dans le code ci-dessous, `next` définit si le middleware suivant ou la fonction réelle doit être appelée.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pré-traitement : Enregistrer avant l'exécution de la fonction
    print(f"[Function] Calling {context.function.name}")

    # Continuer vers le middleware suivant ou l'exécution de la fonction
    await next(context)

    # Post-traitement : Enregistrer après l'exécution de la fonction
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Ce middleware permet d’exécuter ou de journaliser une action entre l’agent et les requêtes entre le LLM.

Cela contient des informations importantes telles que les `messages` envoyés au service IA.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pré-traitement : journal avant l'appel à l'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuer vers le prochain middleware ou service IA
    await next(context)

    # Post-traitement : journal après la réponse de l'IA
    print("[Chat] AI response received")

```

**Mémoire d’Agent**

Comme abordé dans la leçon `Agentic Memory`, la mémoire est un élément important pour permettre à l’agent d’opérer sur différents contextes. MAF offre plusieurs types de mémoires différents :

*Stockage en mémoire vive*

C’est la mémoire stockée dans les threads pendant l’exécution de l’application.

```python
# Créez un nouveau fil.
thread = agent.get_new_thread() # Exécutez l'agent avec le fil.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messages persistants*

Cette mémoire est utilisée pour stocker l’historique des conversations à travers différentes sessions. Elle est définie via la `chat_message_store_factory` :

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

Cette mémoire est ajoutée au contexte avant l’exécution des agents. Ces mémoires peuvent être stockées dans des services externes tels que mem0 :

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

**Observabilité d’Agent**

L’observabilité est essentielle pour construire des systèmes agentiques fiables et maintenables. MAF s’intègre avec OpenTelemetry pour fournir des traces et des compteurs pour une meilleure observabilité.

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

MAF propose des flux de travail qui sont des étapes prédéfinies pour accomplir une tâche et incluent des agents IA comme composants dans ces étapes.

Les flux de travail sont composés de différents éléments permettant un meilleur contrôle du flux. Les flux de travail autorisent aussi l’**orchestration multi-agent** et le **point de contrôle** pour sauvegarder l’état du flux.

Les composants principaux d’un flux de travail sont :

**Exécuteurs**

Les exécuteurs reçoivent des messages d’entrée, accomplissent les tâches qui leur sont assignées, puis produisent un message de sortie. Cela fait avancer le flux de travail vers la réalisation de la tâche globale. Les exécuteurs peuvent être des agents IA ou de la logique personnalisée.

**Arcs**

Les arcs servent à définir le flux des messages dans un flux de travail. Ceux-ci peuvent être :

*Arcs directs* - Connexions simples un-à-un entre exécuteurs :

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Arcs conditionnels* - Activés après qu’une certaine condition est remplie. Par exemple, lorsque les chambres d’hôtel sont indisponibles, un exécuteur peut suggérer d’autres options.

*Arcs switch-case* - Orientent les messages vers différents exécuteurs selon des conditions définies. Par exemple, si un client voyageur a un accès prioritaire, ses tâches seront traitées par un autre flux de travail.

*Arcs de ventilation* - Envoient un message à plusieurs cibles.

*Arcs de convergence* - Rassemblent plusieurs messages de différents exécuteurs et les envoient à une cible unique.

**Événements**

Pour fournir une meilleure observabilité des flux de travail, MAF offre des événements intégrés pour l’exécution, notamment :

- `WorkflowStartedEvent`  - Début de l’exécution du flux de travail
- `WorkflowOutputEvent` - Le flux de travail génère une sortie
- `WorkflowErrorEvent` - Le flux rencontre une erreur
- `ExecutorInvokeEvent`  - L’exécuteur commence son traitement
- `ExecutorCompleteEvent`  - L’exécuteur termine son traitement
- `RequestInfoEvent` - Une requête est envoyée

## Modèles avancés du MAF

Les sections précédentes couvrent les concepts clés du Microsoft Agent Framework. À mesure que vous construisez des agents plus complexes, voici quelques modèles avancés à considérer :

- **Composition de middleware** : Chaînez plusieurs gestionnaires middleware (journalisation, authentification, limitation de débit) en utilisant les middleware fonctionnels et de chat pour un contrôle précis du comportement de l’agent.
- **Point de contrôle des flux de travail** : Utilisez les événements de flux de travail et la sérialisation pour sauvegarder et reprendre les processus d’agents de longue durée.
- **Sélection dynamique d’outils** : Combinez la recherche RAG sur les descriptions d’outils avec l’enregistrement d’outils de MAF pour ne présenter que les outils pertinents par requête.
- **Transfert multi-agent** : Utilisez les arcs de flux de travail et le routage conditionnel pour orchestrer les transferts entre agents spécialisés.

## Exemples de code 

Des exemples de code pour Microsoft Agent Framework se trouvent dans ce dépôt sous les fichiers `xx-python-agent-framework` et `xx-dotnet-agent-framework`.

## Vous avez d’autres questions sur Microsoft Agent Framework ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->