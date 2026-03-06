# Agents IA en Production : Observabilité & Évaluation

[![AI Agents in Production](../../../translated_images/fr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À mesure que les agents IA passent de prototypes expérimentaux à des applications réelles, la capacité à comprendre leur comportement, à surveiller leurs performances et à évaluer systématiquement leurs résultats devient importante.

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous saurez/comment comprendre :
- Les concepts fondamentaux de l'observabilité et de l'évaluation des agents
- Les techniques pour améliorer la performance, les coûts et l'efficacité des agents
- Ce qu'il faut évaluer et comment évaluer systématiquement vos agents IA
- Comment contrôler les coûts lors du déploiement des agents IA en production
- Comment instrumenter les agents construits avec Microsoft Agent Framework

L'objectif est de vous fournir les connaissances pour transformer vos agents « boîte noire » en systèmes transparents, gérables et fiables.

_**Note :** Il est important de déployer des agents IA sûrs et dignes de confiance. Consultez également la leçon [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces et Spans

Les outils d'observabilité comme [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) représentent généralement les exécutions d'agents sous forme de traces et spans.

- **Trace** représente une tâche complète d'agent du début à la fin (comme la gestion d'une requête utilisateur).
- **Spans** sont des étapes individuelles au sein de la trace (comme appeler un modèle de langage ou récupérer des données).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sans observabilité, un agent IA peut sembler être une « boîte noire » — son état interne et son raisonnement sont opaques, ce qui complique le diagnostic des problèmes ou l'optimisation des performances. Avec l'observabilité, les agents deviennent des « boîtes transparentes », offrant une transparence essentielle pour instaurer la confiance et garantir leur bon fonctionnement.

## Pourquoi l'Observabilité est Importante en Production

Le passage des agents IA aux environnements de production introduit un nouvel ensemble de défis et d'exigences. L'observabilité n'est plus un « bonus », mais une capacité critique :

*   **Débogage et Analyse des Causes Racines** : Quand un agent échoue ou produit un résultat inattendu, les outils d'observabilité fournissent les traces nécessaires pour identifier la source de l'erreur. Ceci est particulièrement important dans des agents complexes impliquant plusieurs appels LLM, interactions avec des outils, et logique conditionnelle.
*   **Gestion de la Latence et des Coûts** : Les agents IA s'appuient souvent sur des LLM et d'autres API externes facturées au token ou à l'appel. L'observabilité permet un suivi précis de ces appels, facilitant l'identification des opérations trop lentes ou coûteuses. Cela permet aux équipes d'optimiser les prompts, choisir des modèles plus efficaces ou repenser les workflows pour gérer les coûts opérationnels et garantir une bonne expérience utilisateur.
*   **Confiance, Sécurité et Conformité** : Dans de nombreuses applications, il est important de garantir que les agents se comportent de façon sûre et éthique. L'observabilité fournit une piste d'audit des actions et décisions de l'agent. Celle-ci peut servir à détecter et atténuer des problèmes tels que l'injection de prompt, la génération de contenus nuisibles, ou la mauvaise gestion des informations personnelles (PII). Par exemple, vous pouvez consulter les traces pour comprendre pourquoi un agent a fourni une certaine réponse ou utilisé un outil spécifique.
*   **Boucles d'Amélioration Continue** : Les données d'observabilité sont la base d'un processus de développement itératif. En surveillant les performances des agents dans le monde réel, les équipes peuvent identifier des pistes d'amélioration, collecter des données pour affiner les modèles et valider l'impact des changements. Cela crée une boucle de rétroaction où les insights de production issus de l’évaluation en ligne alimentent l'expérimentation hors ligne et le raffinement, conduisant à des performances d'agent progressivement meilleures.

## Principaux Indicateurs à Suivre

Pour surveiller et comprendre le comportement des agents, différentes métriques et signaux doivent être suivis. Si certaines métriques varient selon l'objectif de l'agent, d'autres sont universellement importantes.

Voici quelques-unes des métriques les plus courantes surveillées par les outils d'observabilité :

**Latence :** À quelle vitesse l'agent répond-il ? Les temps d'attente longs nuisent à l'expérience utilisateur. Vous devez mesurer la latence pour les tâches et chaque étape en retraçant les exécutions d'agents. Par exemple, un agent qui met 20 secondes pour tous ses appels au modèle pourrait être accéléré en utilisant un modèle plus rapide ou en exécutant les appels en parallèle.

**Coûts :** Quel est le coût par exécution d'agent ? Les agents IA dépendent d'appels LLM facturés au token ou d'API externes. Une utilisation fréquente d'outils ou plusieurs prompts peuvent rapidement faire grimper les coûts. Par exemple, si un agent appelle un LLM cinq fois pour une amélioration marginale de qualité, vous devez évaluer si ce coût est justifié ou si vous pourriez réduire le nombre d'appels ou utiliser un modèle moins cher. La surveillance en temps réel peut aussi aider à détecter des pics inattendus (bug provoquant des boucles excessives sur l'API).

**Erreurs de Requête :** Combien de requêtes l’agent a-t-il échouées ? Cela peut inclure des erreurs API ou des échecs d'appels d’outils. Pour rendre votre agent plus robuste en production, vous pouvez mettre en place des plans de secours ou des réessayages. Par ex., si le fournisseur LLM A est indisponible, vous basculez vers le fournisseur LLM B en secours.

**Retour Utilisateur :** Implanter des évaluations directes des utilisateurs fournit des informations précieuses. Cela peut inclure des évaluations explicites (👍pouce levé/👎pouce baissé, ⭐1-5 étoiles) ou des commentaires textuels. Un feedback négatif constant doit vous alerter car c’est un signe que l’agent ne fonctionne pas comme prévu.

**Retour Utilisateur Implicite :** Les comportements des utilisateurs offrent un retour indirect même sans évaluations explicites. Cela peut inclure la reformulation immédiate de questions, la répétition de requêtes ou le clic sur un bouton de réessai. Par ex., si vous voyez que les utilisateurs posent plusieurs fois la même question, c’est un signe que l’agent ne répond pas correctement.

**Précision :** À quelle fréquence l’agent produit-il des sorties correctes ou souhaitables ? Les définitions de précision varient (par ex., exactitude de résolution de problèmes, précision de récupération d’information, satisfaction utilisateur). Il est essentiel de définir d'abord ce qu’est le succès pour votre agent. Vous pouvez suivre la précision via des contrôles automatisés, des scores d’évaluation, ou des labels de tâche complétée. Par exemple, marquer les traces comme « réussies » ou « échouées ».

**Métriques d'Évaluation Automatisées :** Vous pouvez aussi mettre en place des évaluations automatisées. Par exemple, utiliser un LLM pour noter la sortie de l'agent, par ex. si elle est utile, précise ou non. Il existe plusieurs bibliothèques open source qui aident à évaluer différents aspects de l’agent. Par ex., [RAGAS](https://docs.ragas.io/) pour agents RAG ou [LLM Guard](https://llm-guard.com/) pour détecter le langage nuisible ou l'injection de prompt.

En pratique, une combinaison de ces métriques offre la meilleure couverture de la santé d’un agent IA. Dans le [notebook d'exemple](./code_samples/10-expense_claim-demo.ipynb) de ce chapitre, nous vous montrerons comment ces métriques apparaissent dans des exemples réels, mais d’abord, voyons à quoi ressemble un workflow typique d’évaluation.

## Instrumentez votre Agent

Pour collecter des données de traçage, vous devez instrumenter votre code. L’objectif est d’instrumenter le code de l’agent pour émettre des traces et métriques capturables, traitables, et visualisables par une plateforme d’observabilité.

**OpenTelemetry (OTel) :** [OpenTelemetry](https://opentelemetry.io/) est devenu un standard industriel pour l’observabilité des LLM. Il fournit un ensemble d’API, SDKs et outils pour générer, collecter et exporter des données télémétriques.

Il existe de nombreuses bibliothèques d'instrumentation qui enveloppent les frameworks d’agents existants et facilitent l’export des spans OpenTelemetry vers un outil d’observabilité. Microsoft Agent Framework s’intègre nativement à OpenTelemetry. Voici un exemple d’instrumentation d’un agent MAF :

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # L'exécution de l'agent est tracée automatiquement
    pass
```

Le [notebook d'exemple](./code_samples/10-expense_claim-demo.ipynb) de ce chapitre démontrera comment instrumenter votre agent MAF.

**Création Manuelle de Spans :** Bien que les bibliothèques d’instrumentation offrent une bonne base, il existe souvent des cas où des informations plus détaillées ou personnalisées sont nécessaires. Vous pouvez créer manuellement des spans pour ajouter une logique applicative personnalisée. Plus important encore, ils peuvent enrichir des spans créés automatiquement ou manuellement avec des attributs personnalisés (également appelés tags ou métadonnées). Ces attributs peuvent inclure des données spécifiques métier, des calculs intermédiaires, ou tout contexte utile au débogage ou à l’analyse, comme `user_id`, `session_id` ou `model_version`.

Exemple de création manuelle de traces et spans avec le [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) :

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Évaluation de l'Agent

L'observabilité nous donne des métriques, mais l’évaluation est le processus d’analyse de ces données (et la réalisation de tests) pour déterminer la performance d'un agent IA et comment l'améliorer. En d'autres termes, une fois que vous avez ces traces et métriques, comment les utilisez-vous pour juger l’agent et prendre des décisions ?

L’évaluation régulière est importante car les agents IA sont souvent non déterministes et peuvent évoluer (via mises à jour ou dérive de comportement du modèle) – sans évaluation, vous ne sauriez pas si votre « agent intelligent » fait bien son travail ou s’il régresse.

Il existe deux catégories d’évaluations pour les agents IA : **évaluation en ligne** et **évaluation hors ligne**. Les deux sont précieuses et se complètent. On commence généralement par l’évaluation hors ligne, car c’est l’étape minimale nécessaire avant de déployer un agent.

### Évaluation Hors Ligne

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Cela consiste à évaluer l’agent dans un cadre contrôlé, typiquement avec des jeux de données tests, non des requêtes utilisateurs en direct. Vous utilisez des jeux de données soigneusement sélectionnés où vous connaissez la sortie attendue ou le comportement correct, puis vous exécutez votre agent dessus.

Par exemple, si vous avez construit un agent résolvant des problèmes mathématiques de type texte, vous pourriez avoir un [jeu de données test](https://huggingface.co/datasets/gsm8k) de 100 problèmes avec réponses connues. L’évaluation hors ligne se fait souvent en développement (et peut faire partie des pipelines CI/CD) pour vérifier des améliorations ou éviter des régressions. L’avantage est que c’est **répétable et vous obtenez des métriques de précision claires car vous avez la vérité terrain**. Vous pouvez aussi simuler des requêtes utilisateur et mesurer les réponses de l’agent par rapport à des réponses idéales ou utiliser des métriques automatisées comme décrit précédemment.

Le défi clé avec l’évaluation hors ligne est de garantir que votre jeu de test est exhaustif et reste pertinent – l’agent peut bien performer sur un test fixe mais rencontrer des requêtes très différentes en production. Vous devez donc mettre à jour les jeux de test avec de nouveaux cas limites et exemples reflétant les scénarios réels. Un mélange de petits cas de test « smoke test » et de jeux plus larges est utile : petits pour des vérifications rapides, grands pour des métriques globales de performance.

### Évaluation En Ligne

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ceci désigne l’évaluation de l’agent dans un environnement réel, en direct, c’est-à-dire pendant son utilisation en production. L’évaluation en ligne implique de surveiller la performance de l’agent sur les interactions utilisateurs réelles et d’analyser continuellement les résultats.

Par exemple, vous pouvez suivre les taux de succès, les scores de satisfaction utilisateur ou d’autres métriques sur le trafic réel. L’avantage de l’évaluation en ligne est qu’elle **capture des aspects que vous n’auriez peut-être pas anticipés en laboratoire** – vous pouvez observer la dérive du modèle au fil du temps (si l’efficacité de l’agent décline à mesure que les patterns d’entrées changent) et détecter des requêtes ou situations inattendues absentes du jeu de test. Elle donne une image fidèle du comportement de l’agent sur le terrain.

L’évaluation en ligne implique souvent de collecter retours utilisateurs implicites et explicites, comme discuté, et éventuellement de réaliser des tests en parallèle ou A/B (où une nouvelle version de l’agent fonctionne en parallèle pour comparaison). Le défi est qu’il peut être difficile d’obtenir des labels ou scores fiables pour les interactions en direct – vous pouvez vous appuyer sur les retours utilisateurs ou des métriques aval (ex. l’utilisateur a-t-il cliqué sur le résultat).

### Combinaison des Deux

Les évaluations en ligne et hors ligne ne sont pas exclusives ; elles se complètent fortement. Les insights tirés de la surveillance en ligne (ex. nouveaux types de requêtes mal gérées par l’agent) peuvent servir à enrichir et améliorer les jeux de test hors ligne. Inversement, des agents performants hors ligne peuvent ensuite être déployés avec plus de confiance et surveillés en ligne.

En fait, de nombreuses équipes adoptent une boucle :

_évaluer hors ligne -> déployer -> surveiller en ligne -> collecter de nouveaux cas d’échec -> ajouter au jeu de données hors ligne -> affiner l’agent -> répéter_.

## Problèmes Courants

Au fur et à mesure que vous déployez des agents IA en production, vous pouvez rencontrer divers défis. Voici quelques problèmes courants et leurs solutions potentielles :

| **Problème**    | **Solution Potentielle**   |
| ------------- | ------------------ |
| L'agent IA ne réalise pas les tâches de manière cohérente | - Affiner le prompt donné à l’agent IA ; être clair sur les objectifs.<br>- Identifier s’il est utile de diviser la tâche en sous-tâches traitées par plusieurs agents. |
| L'agent IA entre dans des boucles continues  | - Assurer des termes et conditions d’arrêt clairs pour que l’agent sache quand arrêter.<br>- Pour les tâches complexes demandant raisonnement et planification, utiliser un modèle plus grand spécialisé dans ces domaines. |
| Les appels d’outils de l'agent IA ne fonctionnent pas bien   | - Tester et valider la sortie de l’outil en dehors du système d’agent.<br>- Affiner les paramètres, prompts et noms d’outils définis.  |
| Le système multi-agent ne fonctionne pas de manière cohérente | - Affiner les prompts fournis à chaque agent pour qu’ils soient spécifiques et distincts.<br>- Construire un système hiérarchique avec un agent « de routage » ou contrôleur pour déterminer quel agent est approprié. |

Beaucoup de ces problèmes peuvent être identifiés plus efficacement grâce à l’observabilité. Les traces et métriques précédemment évoquées aident à localiser précisément où dans le flux de travail de l’agent les problèmes se produisent, rendant le débogage et l’optimisation bien plus efficaces.

## Gestion des Coûts
Voici quelques stratégies pour gérer les coûts de déploiement des agents IA en production :

**Utiliser des modèles plus petits :** Les petits modèles de langage (SLM) peuvent bien fonctionner sur certains cas d’usage agentiques et réduiront considérablement les coûts. Comme mentionné précédemment, construire un système d’évaluation pour déterminer et comparer les performances par rapport aux modèles plus grands est la meilleure façon de comprendre comment un SLM se comportera sur votre cas d’usage. Envisagez d’utiliser des SLM pour des tâches plus simples comme la classification d’intention ou l’extraction de paramètres, tout en réservant les modèles plus grands pour le raisonnement complexe.

**Utiliser un modèle routeur :** Une stratégie similaire consiste à utiliser une diversité de modèles et de tailles. Vous pouvez utiliser un LLM/SLM ou une fonction serverless pour diriger les requêtes en fonction de leur complexité vers les modèles les mieux adaptés. Cela aidera également à réduire les coûts tout en garantissant la performance sur les bonnes tâches. Par exemple, acheminer les requêtes simples vers des modèles plus petits et plus rapides, et n’utiliser les modèles coûteux de grande taille que pour les tâches de raisonnement complexes.

**Mise en cache des réponses :** Identifier les requêtes et tâches courantes et fournir les réponses avant qu’elles ne passent par votre système agentique est un bon moyen de réduire le volume de requêtes similaires. Vous pouvez même mettre en place un flux pour déterminer la similarité d’une requête avec celles mises en cache en utilisant des modèles IA plus basiques. Cette stratégie peut réduire significativement les coûts pour les questions fréquemment posées ou les flux de travail communs.

## Voyons comment cela fonctionne en pratique

Dans le [carnet d’exemples de cette section](./code_samples/10-expense_claim-demo.ipynb), nous verrons des exemples d’utilisation des outils d’observabilité pour surveiller et évaluer notre agent.


### Vous avez d’autres questions sur les agents IA en production ?

Rejoignez le [Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Leçon précédente

[Metacognition Design Pattern](../09-metacognition/README.md)

## Leçon suivante

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->