# Construire des applications multi-agents avec le Workflow du Microsoft Agent Framework

Ce tutoriel vous guidera pour comprendre et construire des applications multi-agents en utilisant le Microsoft Agent Framework. Nous explorerons les concepts fondamentaux des systèmes multi-agents, plongerons dans l'architecture du composant Workflow du framework, et passerons en revue des exemples pratiques en Python et .NET pour différents modèles de workflow.

## 1\. Comprendre les systèmes multi-agents

Un agent d'IA est un système qui dépasse les capacités d'un modèle de langage standard (LLM). Il peut percevoir son environnement, prendre des décisions et effectuer des actions pour atteindre des objectifs spécifiques. Un système multi-agents implique plusieurs de ces agents collaborant pour résoudre un problème complexe ou impossible à gérer par un seul agent.

### Scénarios d'application courants

  * **Résolution de problèmes complexes** : Diviser une tâche importante (par exemple, organiser un événement à l'échelle de l'entreprise) en sous-tâches gérées par des agents spécialisés (par exemple, un agent de budget, un agent de logistique, un agent de marketing).
  * **Assistants virtuels** : Un agent assistant principal délègue des tâches comme la planification, la recherche et les réservations à d'autres agents spécialisés.
  * **Création de contenu automatisée** : Un workflow où un agent rédige du contenu, un autre le vérifie pour l'exactitude et le ton, et un troisième le publie.

### Modèles multi-agents

Les systèmes multi-agents peuvent être organisés selon plusieurs modèles, qui déterminent leur mode d'interaction :

  * **Séquentiel** : Les agents travaillent dans un ordre prédéfini, comme une chaîne de montage. La sortie d'un agent devient l'entrée du suivant.
  * **Concurrent** : Les agents travaillent en parallèle sur différentes parties d'une tâche, et leurs résultats sont agrégés à la fin.
  * **Conditionnel** : Le workflow suit différents chemins en fonction de la sortie d'un agent, similaire à une instruction if-then-else.

## 2\. L'architecture du Workflow du Microsoft Agent Framework

Le système de workflow du Agent Framework est un moteur d'orchestration avancé conçu pour gérer des interactions complexes entre plusieurs agents. Il repose sur une architecture basée sur des graphes utilisant un [modèle d'exécution de style Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), où le traitement se déroule en étapes synchronisées appelées "supersteps".

### Composants principaux

L'architecture se compose de trois parties principales :

1.  **Exécuteurs** : Ce sont les unités de traitement fondamentales. Dans nos exemples, un `Agent` est un type d'exécuteur. Chaque exécuteur peut avoir plusieurs gestionnaires de messages qui sont automatiquement invoqués en fonction du type de message reçu.
2.  **Arêtes** : Elles définissent le chemin que les messages empruntent entre les exécuteurs. Les arêtes peuvent avoir des conditions, permettant un routage dynamique des informations à travers le graphe de workflow.
3.  **Workflow** : Ce composant orchestre l'ensemble du processus, gérant les exécuteurs, les arêtes et le flux global d'exécution. Il garantit que les messages sont traités dans le bon ordre et diffuse des événements pour l'observabilité.

*Un diagramme illustrant les composants principaux du système de workflow.*

Cette structure permet de construire des applications robustes et évolutives en utilisant des modèles fondamentaux comme les chaînes séquentielles, le fan-out/fan-in pour le traitement parallèle, et la logique switch-case pour les flux conditionnels.

## 3\. Exemples pratiques et analyse de code

Passons maintenant à la mise en œuvre de différents modèles de workflow en utilisant le framework. Nous examinerons des exemples de code en Python et .NET pour chaque cas.

### Cas 1 : Workflow séquentiel de base

C'est le modèle le plus simple, où la sortie d'un agent est directement transmise à un autre. Notre scénario implique un agent `FrontDesk` d'hôtel qui fait une recommandation de voyage, laquelle est ensuite examinée par un agent `Concierge`.

*Diagramme du workflow de base FrontDesk -\> Concierge.*

#### Contexte du scénario

Un voyageur demande une recommandation à Paris.

1.  L'agent `FrontDesk`, conçu pour être concis, suggère de visiter le musée du Louvre.
2.  L'agent `Concierge`, qui privilégie les expériences authentiques, reçoit cette suggestion. Il examine la recommandation et propose une alternative plus locale et moins touristique.

#### Analyse de l'implémentation en Python

Dans l'exemple Python, nous définissons et créons d'abord les deux agents, chacun avec des instructions spécifiques.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Ensuite, le `WorkflowBuilder` est utilisé pour construire le graphe. L'agent `front_desk_agent` est défini comme point de départ, et une arête est créée pour connecter sa sortie à l'agent `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Enfin, le workflow est exécuté avec l'invite utilisateur initiale.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analyse de l'implémentation en .NET (C#)

L'implémentation en .NET suit une logique très similaire. Tout d'abord, des constantes sont définies pour les noms et instructions des agents.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Les agents sont créés à l'aide d'un `OpenAIClient`, puis le `WorkflowBuilder` définit le flux séquentiel en ajoutant une arête entre `frontDeskAgent` et `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Le workflow est ensuite exécuté avec le message de l'utilisateur, et les résultats sont diffusés en retour.

### Cas 2 : Workflow séquentiel multi-étapes

Ce modèle étend la séquence de base pour inclure davantage d'agents. Il est idéal pour les processus nécessitant plusieurs étapes de raffinement ou de transformation.

#### Contexte du scénario

Un utilisateur fournit une image d'un salon et demande un devis pour le mobilier.

1.  **Sales-Agent** : Identifie les articles de mobilier dans l'image et crée une liste.
2.  **Price-Agent** : Prend la liste des articles et fournit une ventilation détaillée des prix, incluant des options économiques, intermédiaires et haut de gamme.
3.  **Quote-Agent** : Reçoit la liste tarifée et la formatte en un document de devis formel en Markdown.

*Diagramme du workflow Sales -\> Price -\> Quote.*

#### Analyse de l'implémentation en Python

Trois agents sont définis, chacun avec un rôle spécialisé. Le workflow est construit en utilisant `add_edge` pour créer une chaîne : `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

L'entrée est un `ChatMessage` qui inclut à la fois du texte et l'URI de l'image. Le framework gère le passage de la sortie de chaque agent au suivant dans la séquence jusqu'à ce que le devis final soit généré.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### Analyse de l'implémentation en .NET (C#)

L'exemple .NET reflète la version Python. Trois agents (`salesagent`, `priceagent`, `quoteagent`) sont créés. Le `WorkflowBuilder` les relie de manière séquentielle.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Le message de l'utilisateur est construit avec les données de l'image (sous forme de bytes) et l'invite textuelle. La méthode `InProcessExecution.StreamAsync` initie le workflow, et la sortie finale est capturée depuis le flux.

### Cas 3 : Workflow concurrent

Ce modèle est utilisé lorsque des tâches peuvent être effectuées simultanément pour gagner du temps. Il implique un "fan-out" vers plusieurs agents et un "fan-in" pour agréger les résultats.

#### Contexte du scénario

Un utilisateur demande à planifier un voyage à Seattle.

1.  **Dispatcher (Fan-Out)** : La demande de l'utilisateur est envoyée à deux agents en même temps.
2.  **Researcher-Agent** : Recherche les attractions, la météo et les considérations clés pour un voyage à Seattle en décembre.
3.  **Plan-Agent** : Crée indépendamment un itinéraire détaillé jour par jour.
4.  **Aggregator (Fan-In)** : Les sorties du chercheur et du planificateur sont collectées et présentées ensemble comme résultat final.

*Diagramme du workflow concurrent Researcher et Planner.*

#### Analyse de l'implémentation en Python

Le `ConcurrentBuilder` simplifie la création de ce modèle. Il suffit de lister les agents participants, et le builder crée automatiquement la logique de fan-out et fan-in nécessaire.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Le framework garantit que `research_agent` et `plan_agent` s'exécutent en parallèle, et leurs sorties finales sont collectées dans une liste.

#### Analyse de l'implémentation en .NET (C#)

En .NET, ce modèle nécessite une définition plus explicite. Des exécuteurs personnalisés (`ConcurrentStartExecutor` et `ConcurrentAggregationExecutor`) sont créés pour gérer la logique de fan-out et fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

Le `WorkflowBuilder` utilise ensuite `AddFanOutEdge` et `AddFanInEdge` pour construire le graphe avec ces exécuteurs personnalisés et les agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Cas 4 : Workflow conditionnel

Les workflows conditionnels introduisent une logique de branchement, permettant au système de suivre différents chemins en fonction des résultats intermédiaires.

#### Contexte du scénario

Ce workflow automatise la création et la publication d'un tutoriel technique.

1.  **Evangelist-Agent** : Rédige un brouillon du tutoriel basé sur un plan donné et des URLs.
2.  **ContentReviewer-Agent** : Examine le brouillon. Il vérifie si le nombre de mots dépasse 200.
3.  **Branchement conditionnel** :
      * **Si approuvé (`Oui`)** : Le workflow passe à l'agent `Publisher-Agent`.
      * **Si rejeté (`Non`)** : Le workflow s'arrête et fournit la raison du rejet.
4.  **Publisher-Agent** : Si le brouillon est approuvé, cet agent sauvegarde le contenu dans un fichier Markdown.

#### Analyse de l'implémentation en Python

Cet exemple utilise une fonction personnalisée, `select_targets`, pour implémenter la logique conditionnelle. Cette fonction est passée à `add_multi_selection_edge_group` et dirige le workflow en fonction du champ `review_result` de la sortie du réviseur.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Des exécuteurs personnalisés comme `to_reviewer_result` sont utilisés pour analyser la sortie JSON des agents et la convertir en objets fortement typés que la fonction de sélection peut inspecter.

#### Analyse de l'implémentation en .NET (C#)

La version .NET utilise une approche similaire avec une fonction conditionnelle. Un `Func<object?, bool>` est défini pour vérifier la propriété `Result` de l'objet `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

Le paramètre `condition` de la méthode `AddEdge` permet au `WorkflowBuilder` de créer un chemin de branchement. Le workflow ne suivra l'arête vers `publishExecutor` que si la condition `GetCondition(expectedResult: "Yes")` retourne vrai. Sinon, il suivra le chemin vers `sendReviewerExecutor`.

## Conclusion

Le Workflow du Microsoft Agent Framework offre une base robuste et flexible pour orchestrer des systèmes multi-agents complexes. En tirant parti de son architecture basée sur des graphes et de ses composants principaux, les développeurs peuvent concevoir et implémenter des workflows sophistiqués en Python et .NET. Que votre application nécessite un traitement séquentiel simple, une exécution parallèle ou une logique conditionnelle dynamique, le framework fournit les outils nécessaires pour construire des solutions puissantes, évolutives et fortement typées alimentées par l'IA.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.