# Construire des applications multi-agents avec Microsoft Agent Framework Workflow

Ce tutoriel vous guidera dans la compréhension et la construction d'applications multi-agents en utilisant Microsoft Agent Framework. Nous explorerons les concepts fondamentaux des systèmes multi-agents, plongerons dans l'architecture du composant Workflow du framework, et parcourrons des exemples pratiques en Python et .NET pour différents modèles de workflow.

## 1\. Comprendre les systèmes multi-agents

Un agent IA est un système qui va au-delà des capacités d'un modèle de langage large standard (LLM). Il peut percevoir son environnement, prendre des décisions et agir pour atteindre des objectifs spécifiques. Un système multi-agent implique plusieurs de ces agents collaborant pour résoudre un problème qui serait difficile ou impossible à gérer par un agent seul.

### Scénarios d'application courants

  * **Résolution de problèmes complexes** : Décomposer une grande tâche (par exemple, organiser un événement à l'échelle de l'entreprise) en sous-tâches plus petites traitées par des agents spécialisés (par exemple, un agent budget, un agent logistique, un agent marketing).
  * **Assistants virtuels** : Un agent assistant principal délègue des tâches telles que la planification, la recherche et la réservation à d'autres agents spécialisés.
  * **Création de contenu automatisée** : Un workflow où un agent rédige un contenu, un autre le révise pour exactitude et tonalité, et un troisième le publie.

### Modèles multi-agents

Les systèmes multi-agents peuvent être organisés selon plusieurs modèles, qui déterminent leur mode d'interaction :

  * **Séquentiel** : Les agents travaillent dans un ordre prédéfini, comme une chaîne de montage. La sortie d'un agent devient l'entrée du suivant.
  * **Concurent** : Les agents travaillent en parallèle sur différentes parties d'une tâche, et leurs résultats sont agrégés à la fin.
  * **Conditionnel** : Le workflow suit différents chemins selon la sortie d'un agent, similaire à une structure if-then-else.

## 2\. L'architecture du Microsoft Agent Framework Workflow

Le système de workflow du Agent Framework est un moteur d'orchestration avancé conçu pour gérer des interactions complexes entre plusieurs agents. Il est basé sur une architecture en graphes qui utilise un [modèle d'exécution de type Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), où le traitement se fait en étapes synchronisées appelées "supersteps".

### Composants clés

L'architecture est composée de trois parties principales :

1.  **Exécuteurs** : Ce sont les unités de traitement fondamentales. Dans nos exemples, un `Agent` est un type d'exécuteur. Chaque exécuteur peut avoir plusieurs gestionnaires de messages invoqués automatiquement selon le type de message reçu.
2.  **Arêtes** : Elles définissent le chemin que prennent les messages entre les exécuteurs. Les arêtes peuvent avoir des conditions, permettant un routage dynamique de l'information à travers le graphe du workflow.
3.  **Workflow** : Ce composant orchestre l'ensemble du processus, gère les exécuteurs, les arêtes et le flux global d'exécution. Il garantit que les messages sont traités dans le bon ordre et diffuse des événements pour l'observabilité.

*Un diagramme illustrant les composants clés du système de workflow.*

Cette structure permet de construire des applications robustes et évolutives en utilisant des modèles fondamentaux comme les chaînes séquentielles, fan-out/fan-in pour le traitement parallèle, et la logique switch-case pour les flux conditionnels.

## 3\. Exemples pratiques et analyse de code

Explorons maintenant comment implémenter différents modèles de workflow en utilisant le framework. Nous examinerons du code à la fois en Python et en .NET pour chaque exemple.

### Cas 1 : Workflow séquentiel basique

C'est le modèle le plus simple, où la sortie d'un agent est passée directement à un autre. Notre scénario implique un agent `FrontDesk` d'hôtel qui fait une recommandation de voyage, revue ensuite par un agent `Concierge`.

*Diagramme du workflow basique FrontDesk -> Concierge.*

#### Contexte du scénario

Un voyageur demande une recommandation à Paris.

1.  L'agent `FrontDesk`, conçu pour la concision, suggère de visiter le musée du Louvre.
2.  L'agent `Concierge`, qui privilégie les expériences authentiques, reçoit cette suggestion. Il révise la recommandation et fournit un retour, suggérant une alternative plus locale et moins touristique.

#### Analyse de l'implémentation Python

Dans l'exemple Python, nous définissons et créons d'abord les deux agents, chacun avec des instructions spécifiques.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Définir les rôles et instructions des agents
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Créer des instances d'agents
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Ensuite, `WorkflowBuilder` est utilisé pour construire le graphe. L'agent `front_desk_agent` est positionné comme point de départ, et une arête est créée pour connecter sa sortie à `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Enfin, le workflow est exécuté avec la consigne utilisateur initiale.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run exécute le flux de travail ; get_outputs() renvoie le résultat de l'exécuteur de sortie.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analyse de l'implémentation .NET (C#)

L'implémentation .NET suit une logique très similaire. D'abord, les constantes sont définies pour les noms et instructions des agents.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Les agents sont créés via un `AzureOpenAIClient` (API Responses), puis `WorkflowBuilder` définit le flux séquentiel en ajoutant une arête de `frontDeskAgent` à `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Le workflow est ensuite lancé avec le message utilisateur, et les résultats sont retransmis en flux.

### Cas 2 : Workflow séquentiel multi-étapes

Ce modèle étend la séquence de base pour inclure plus d'agents. Il est idéal pour des processus nécessitant plusieurs étapes de raffinement ou de transformation.

#### Contexte du scénario

Un utilisateur fournit une image de salon et demande un devis mobilier.

1.  **Agent de vente** : Identifie les meubles sur l'image et crée une liste.
2.  **Agent de prix** : Prend la liste des articles et fournit une ventilation détaillée des prix, incluant options budget, milieu de gamme et premium.
3.  **Agent de devis** : Reçoit la liste tarifée et la formate en un document formel de devis en Markdown.

*Diagramme du workflow Sales -> Price -> Quote.*

#### Analyse de l'implémentation Python

Trois agents sont définis, chacun avec un rôle spécialisé. Le workflow est construit avec `add_edge` pour créer une chaîne : `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Créer trois agents spécialisés
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construire le workflow séquentiel
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

L'entrée est un `ChatMessage` incluant à la fois du texte et l'URI de l'image. Le framework gère le passage de la sortie de chaque agent au suivant dans la séquence jusqu'à ce que le devis final soit généré.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Le message de l'utilisateur contient à la fois du texte et une image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Exécuter le flux de travail
events = await workflow.run(message)
```

#### Analyse de l'implémentation .NET (C#)

L'exemple .NET reflète la version Python. Trois agents (`salesagent`, `priceagent`, `quoteagent`) sont créés. Le `WorkflowBuilder` les relie de manière séquentielle.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Le message utilisateur est construit avec les données image (en bytes) et le texte de la consigne. La méthode `InProcessExecution.RunStreamingAsync` lance le workflow, et la sortie finale est récupérée depuis le flux.

### Cas 3 : Workflow concurrent

Ce modèle est utilisé lorsque des tâches peuvent être effectuées simultanément pour gagner du temps. Il implique un "fan-out" vers plusieurs agents puis un "fan-in" pour agréger les résultats.

#### Contexte du scénario

Un utilisateur demande d'organiser un voyage à Seattle.

1.  **Dispatcher (fan-out)** : La demande de l'utilisateur est envoyée simultanément à deux agents.
2.  **Agent chercheur** : Recherche les attractions, la météo et les points clés pour un voyage à Seattle en décembre.
3.  **Agent planificateur** : Crée indépendamment un itinéraire détaillé jour par jour.
4.  **Agrégateur (fan-in)** : Les sorties du chercheur et du planificateur sont collectées et présentées ensemble comme résultat final.

*Diagramme du workflow concurrent Researcher et Planner.*

#### Analyse de l'implémentation Python

`ConcurrentBuilder` simplifie la création de ce modèle. Il suffit de lister les agents participants, et le builder crée automatiquement la logique fan-out et fan-in nécessaire.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder gère la logique de dispersion/agrégation
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Exécuter le workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Le framework assure que `research_agent` et `plan_agent` s'exécutent en parallèle, et que leurs sorties finales sont collectées dans une liste.

#### Analyse de l'implémentation .NET (C#)

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

Les workflows conditionnels introduisent une logique de branchement, permettant au système de suivre différents chemins selon les résultats intermédiaires.

#### Contexte du scénario

Ce workflow automatise la création et la publication d'un tutoriel technique.

1.  **Agent évangéliste** : Rédige un brouillon du tutoriel basé sur un plan et des URL fournis.
2.  **Agent relecteur** : Revoit le brouillon. Il vérifie si le nombre de mots dépasse 200.
3.  **Branche conditionnelle** :
      * **Si approuvé (`Oui`)** : Le workflow poursuit vers l'agent éditeur.
      * **Si rejeté (`Non`)** : Le workflow s'arrête et affiche la raison du rejet.
4.  **Agent éditeur**: Si le brouillon est approuvé, cet agent sauvegarde le contenu dans un fichier Markdown.

#### Analyse de l'implémentation Python

Cet exemple utilise une fonction personnalisée, `select_targets`, pour implémenter la logique conditionnelle. Cette fonction est passée à `add_multi_selection_edge_group` et dirige le workflow en fonction du champ `review_result` issu de la sortie du relecteur.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Cette fonction détermine l'étape suivante en fonction du résultat de la révision
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Si approuvé, passez à l'exécuteur 'save_draft'
        return [save_draft_id]
    else:
        # En cas de rejet, passez à l'exécuteur 'handle_review' pour signaler l'échec
        return [handle_review_id]

# Le générateur de workflow utilise la fonction de sélection pour le routage
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Le bord multi-sélection implémente la logique conditionnelle
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

#### Analyse de l'implémentation .NET (C#)

La version .NET utilise une approche similaire avec une fonction de condition. Un `Func<object?, bool>` est défini pour vérifier la propriété `Result` de l'objet `ReviewResult`.

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

Le paramètre `condition` de la méthode `AddEdge` permet au `WorkflowBuilder` de créer un chemin de branchement. Le workflow ne suit l'arête vers `publishExecutor` que si la condition `GetCondition(expectedResult: "Yes")` retourne vrai. Sinon, il suit le chemin vers `sendReviewerExecutor`.

## Conclusion

Le Microsoft Agent Framework Workflow offre une base robuste et flexible pour orchestrer des systèmes multi-agents complexes. En tirant parti de son architecture basée sur des graphes et de ses composants clés, les développeurs peuvent concevoir et implémenter des workflows sophistiqués en Python comme en .NET. Que votre application nécessite un traitement séquentiel simple, une exécution parallèle ou une logique conditionnelle dynamique, le framework propose les outils pour construire des solutions IA puissantes, évolutives et sûres en termes de typage.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->