# Agents IA en production : Observabilité & Évaluation

[![Agents IA en production](../../../translated_images/fr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

À mesure que les agents IA passent de prototypes expérimentaux à des applications réelles, la capacité à comprendre leur comportement, surveiller leur performance et évaluer systématiquement leurs résultats devient importante.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez/comment comprendre :
- Concepts clés de l'observabilité et de l'évaluation des agents
- Techniques pour améliorer la performance, les coûts et l'efficacité des agents
- Quoi et comment évaluer systématiquement vos agents IA
- Comment contrôler les coûts lors du déploiement des agents IA en production
- Comment instrumenter les agents construits avec Microsoft Agent Framework

L'objectif est de vous doter des connaissances nécessaires pour transformer vos agents « boîte noire » en systèmes transparents, gérables et fiables.

_**Note :** Il est important de déployer des agents IA sûrs et dignes de confiance. Consultez également la leçon [Construire des agents IA dignes de confiance](../06-building-trustworthy-agents/README.md)._

## Traces et Spans

Les outils d'observabilité tels que [Langfuse](https://langfuse.com/) ou [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) représentent généralement les exécutions d'agents sous forme de traces et spans.

- **Trace** représente une tâche complète de l'agent du début à la fin (comme traiter une requête utilisateur).
- **Spans** sont les étapes individuelles à l'intérieur de la trace (comme appeler un modèle de langage ou récupérer des données).

![Arbre de trace dans Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Sans observabilité, un agent IA peut sembler être une « boîte noire » – son état interne et son raisonnement sont opaques, ce qui rend difficile le diagnostic des problèmes ou l'optimisation des performances. Avec l'observabilité, les agents deviennent des « boîtes transparentes », offrant une transparence vitale pour instaurer la confiance et assurer qu’ils fonctionnent comme prévu.

## Pourquoi l'observabilité est essentielle en production

Le passage des agents IA en environnements de production introduit un nouvel ensemble de défis et d'exigences. L'observabilité n'est plus un simple « plus », mais une capacité critique :

*   **Débogage et analyse des causes profondes** : lorsqu'un agent échoue ou produit un résultat inattendu, les outils d'observabilité fournissent les traces nécessaires pour identifier la source de l'erreur. Ceci est particulièrement important dans des agents complexes qui peuvent impliquer plusieurs appels LLM, interactions avec des outils et logique conditionnelle.
*   **Gestion de la latence et des coûts** : les agents IA dépendent souvent de LLM et d'autres API externes facturées au token ou à l'appel. L'observabilité permet un suivi précis de ces appels, aidant à identifier les opérations trop lentes ou coûteuses. Cela permet aux équipes d'optimiser les prompts, de sélectionner des modèles plus efficaces ou de revoir les flux de travail pour gérer les coûts opérationnels et garantir une bonne expérience utilisateur.
*   **Confiance, sécurité et conformité** : dans de nombreuses applications, il est important de garantir que les agents se comportent de manière sûre et éthique. L'observabilité fournit une piste d'audit des actions et décisions de l'agent. Cela peut être utilisé pour détecter et atténuer des problèmes comme l'injection de prompts, la génération de contenu nuisible ou la mauvaise gestion des informations personnelles (PII). Par exemple, vous pouvez examiner les traces pour comprendre pourquoi un agent a donné une certaine réponse ou utilisé un outil spécifique.
*   **Boucles d'amélioration continue** : les données d'observabilité sont la base d'un processus de développement itératif. En surveillant la performance des agents dans le monde réel, les équipes peuvent identifier des axes d'amélioration, recueillir des données pour affiner les modèles et valider l'impact des modifications. Cela crée une boucle de rétroaction où les informations de production issues de l'évaluation en ligne alimentent les expérimentations et raffinements hors ligne, conduisant à une amélioration progressive des performances des agents.

## Principaux indicateurs à suivre

Pour surveiller et comprendre le comportement d'un agent, un ensemble de métriques et signaux doit être suivi. Bien que les indicateurs spécifiques puissent varier en fonction de l’objectif de l'agent, certains sont universellement importants.

Voici quelques-uns des indicateurs les plus couramment surveillés par les outils d'observabilité :

**Latence :** Quelle est la rapidité de réponse de l'agent ? Des temps d'attente longs nuisent à l'expérience utilisateur. Vous devriez mesurer la latence des tâches et des étapes individuelles en traçant les exécutions d'agents. Par exemple, un agent qui met 20 secondes pour tous les appels de modèle pourrait être accéléré en utilisant un modèle plus rapide ou en exécutant les appels en parallèle.

**Coûts :** Quel est le coût par exécution d'agent ? Les agents IA s'appuient sur des appels LLM facturés par token ou sur des API externes. L'usage fréquent d'outils ou les multiples prompts peuvent rapidement augmenter les coûts. Par exemple, si un agent appelle un LLM cinq fois pour une amélioration marginale, il faut évaluer si ce coût est justifié ou si le nombre d'appels peut être réduit ou un modèle moins cher utilisé. La surveillance en temps réel aide aussi à identifier des pics inattendus (par exemple, des bugs provoquant des boucles excessives d'API).

**Erreurs de requête :** Combien de requêtes ont échoué ? Cela peut inclure des erreurs d'API ou des appels d'outil échoués. Pour renforcer la robustesse de votre agent en production, vous pouvez alors mettre en place des mécanismes de secours ou de réessai. Par exemple, si le fournisseur LLM A est indisponible, vous basculez vers le fournisseur B en secours.

**Retour utilisateur :** La mise en place d’évaluations directes par les utilisateurs fournit des informations précieuses. Cela peut inclure des notes explicites (👍pouce levé/👎pouce baissé, ⭐1-5 étoiles) ou des commentaires textuels. Un retour négatif constant doit vous alerter car c’est un signe que l’agent ne fonctionne pas comme attendu.

**Retour implicite utilisateur :** Les comportements utilisateurs fournissent un retour indirect même sans notation explicite. Cela peut inclure une reformulation immédiate de la question, des requêtes répétées ou un clic sur le bouton de réessai. Par exemple, si vous constatez que les utilisateurs posent plusieurs fois la même question, c'est un signe que l'agent ne fonctionne pas comme attendu.

**Précision :** À quelle fréquence l'agent produit-il des résultats corrects ou souhaitables ? Les définitions de la précision varient (par exemple, la justesse dans la résolution de problèmes, la précision de la récupération d’information, la satisfaction utilisateur). La première étape est de définir ce que le succès signifie pour votre agent. Vous pouvez suivre la précision via des contrôles automatisés, des scores d’évaluation ou des étiquettes de réussite des tâches. Par exemple, marquer les traces comme « réussi » ou « échoué ».

**Métriques d’évaluation automatisée :** Vous pouvez aussi configurer des évaluations automatiques. Par exemple, utiliser un LLM pour noter la sortie de l'agent, e.g. si elle est utile, précise ou non. Il existe également plusieurs bibliothèques open source qui aident à scorer différents aspects de l’agent. Par exemple [RAGAS](https://docs.ragas.io/) pour les agents RAG ou [LLM Guard](https://llm-guard.com/) pour détecter le langage nuisible ou l’injection de prompt.

En pratique, une combinaison de ces métriques offre la meilleure couverture de la santé d’un agent IA. Dans le [notebook d'exemple](./code_samples/10-expense_claim-demo.ipynb) de ce chapitre, nous vous montrerons à quoi ressemblent ces métriques sur des exemples réels, mais d'abord, nous apprendrons à quoi ressemble un processus d'évaluation typique.

## Instrumentez votre agent

Pour collecter des données de traçage, vous devrez instrumenter votre code. L’objectif est d’instrumenter le code de l’agent pour émettre des traces et métriques qui peuvent être capturées, traitées et visualisées par une plateforme d'observabilité.

**OpenTelemetry (OTel) :** [OpenTelemetry](https://opentelemetry.io/) est devenu un standard industriel pour l'observabilité des LLM. Il fournit un ensemble d’API, SDK et outils pour générer, collecter et exporter des données de télémétrie.

De nombreuses bibliothèques d'instrumentation encapsulent les frameworks d'agents existants et facilitent l’export des spans OpenTelemetry vers un outil d'observabilité. Microsoft Agent Framework s'intègre nativement avec OpenTelemetry. Voici un exemple d’instrumentation d’un agent MAF :

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # L'exécution de l'agent est tracée automatiquement
    pass
```

Le [notebook d'exemple](./code_samples/10-expense_claim-demo.ipynb) de ce chapitre vous montrera comment instrumenter votre agent MAF.

**Création manuelle de Span :** Bien que les bibliothèques d'instrumentation fournissent une bonne base, il est souvent nécessaire d'ajouter des informations plus détaillées ou personnalisées. Vous pouvez créer manuellement des spans pour ajouter une logique applicative personnalisée. Plus important encore, ils peuvent enrichir des spans créés automatiquement ou manuellement avec des attributs personnalisés (également appelés tags ou métadonnées). Ces attributs peuvent inclure des données métier spécifiques, des calculs intermédiaires ou tout contexte utile pour le débogage ou l'analyse, tels que `user_id`, `session_id` ou `model_version`.

Exemple de création manuelle de traces et spans avec le [SDK Python Langfuse](https://langfuse.com/docs/sdk/python/sdk-v3) :

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Évaluation des agents

L'observabilité nous donne des métriques, mais l’évaluation est le processus d’analyse de ces données (et de réalisation de tests) pour déterminer la performance d’un agent IA et comment l’améliorer. En d’autres termes, une fois que vous avez ces traces et métriques, comment les utilisez-vous pour juger l’agent et prendre des décisions ?

Une évaluation régulière est importante car les agents IA sont souvent non déterministes et peuvent évoluer (via des mises à jour ou la dérive des modèles) – sans évaluation, vous ne sauriez pas si votre « agent intelligent » fait réellement bien son travail ou s’il régresse.

Deux catégories d’évaluation existent pour les agents IA : **évaluation en ligne** et **évaluation hors ligne**. Les deux sont précieuses et se complètent. On commence généralement par l’évaluation hors ligne, qui est l’étape minimale avant tout déploiement.

### Évaluation hors ligne

![Éléments de dataset dans Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Cela consiste à évaluer l’agent dans un cadre contrôlé, typiquement avec des jeux de données tests, pas avec des requêtes utilisateurs en direct. Vous utilisez des datasets curatés où vous connaissez la sortie ou le comportement attendu, puis exécutez l’agent dessus.

Par exemple, si vous avez construit un agent de résolution de problèmes mathématiques, vous pouvez avoir un [jeu de test](https://huggingface.co/datasets/gsm8k) de 100 problèmes avec des réponses connues. L’évaluation hors ligne est souvent réalisée pendant le développement (et peut faire partie des pipelines CI/CD) pour vérifier les améliorations ou éviter les régressions. L’avantage est qu’elle est **répétable et vous pouvez obtenir des métriques claires de précision puisque vous avez la vérité de terrain**. Vous pouvez aussi simuler des requêtes utilisateur et mesurer les réponses de l’agent contre des réponses idéales ou utiliser des métriques automatiques comme décrit plus haut.

Le défi principal avec l’évaluation hors ligne est de garantir que votre jeu de test est complet et reste pertinent – l’agent peut bien performer sur un ensemble fixe mais rencontrer des requêtes très différentes en production. Vous devez donc maintenir les jeux de test à jour avec de nouveaux cas limites et exemples reflétant les scénarios réels. Un mélange de petits cas « smoke test » et de grands jeux d’évaluation est utile : petits sets pour des vérifications rapides et grands pour des métriques de performance plus larges.

### Évaluation en ligne

![Vue d’ensemble des métriques d'observabilité](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Cela désigne l’évaluation de l’agent dans un environnement réel et en direct, c’est-à-dire pendant son utilisation effective en production. L’évaluation en ligne consiste à surveiller la performance de l’agent sur des interactions utilisateur réelles et à analyser continuellement les résultats.

Par exemple, vous pouvez suivre les taux de réussite, les scores de satisfaction utilisateur ou d’autres métriques sur le trafic en direct. L’avantage est qu’elle **capte des éléments qu’on ne peut pas anticiper en laboratoire** – vous pouvez observer la dérive du modèle dans le temps (si l’efficacité de l’agent diminue à mesure que les schémas d’entrée évoluent) et détecter des requêtes ou situations inattendues absentes de vos données de test. Cela donne un portrait réel du comportement de l’agent dans son environnement naturel.

L’évaluation en ligne implique souvent de collecter des retours utilisateurs implicites et explicites, comme vu précédemment, et éventuellement d’exécuter des tests shadow ou A/B (où une nouvelle version de l’agent tourne en parallèle pour comparer avec l’ancienne). Le défi est d’obtenir des labels ou scores fiables pour les interactions en direct – vous pouvez vous appuyer sur les retours utilisateurs ou des métriques aval (par exemple, le clic sur le résultat).

### Combiner les deux

Les évaluations en ligne et hors ligne ne s’excluent pas ; elles sont très complémentaires. Les informations tirées de la surveillance en ligne (par exemple, de nouveaux types de requêtes utilisateur où l’agent performe mal) peuvent améliorer les jeux de tests hors ligne. Inversement, les agents bien testés hors ligne peuvent ensuite être déployés et surveillés plus sereinement en ligne.

En fait, de nombreuses équipes adoptent une boucle de travail :

_évaluer hors ligne -> déployer -> surveiller en ligne -> collecter les cas d’échec -> ajouter au dataset hors ligne -> affiner l’agent -> répéter_.

## Problèmes courants

En déployant des agents IA en production, vous pouvez rencontrer divers défis. Voici quelques problèmes fréquents et leurs solutions potentielles :

| **Problème**    | **Solution potentielle**   |
| ------------- | ------------------ |
| L’agent IA ne réalise pas les tâches de manière cohérente | - Affiner le prompt donné à l’agent IA ; soyez clair sur les objectifs.<br>- Identifier quand diviser les tâches en sous-tâches et les assigner à plusieurs agents peut aider. |
| L’agent IA entre dans des boucles continues  | - Assurez-vous d’avoir des conditions claires d’arrêt pour que l’agent sache quand interrompre le processus.<br>- Pour les tâches complexes nécessitant raisonnement et planification, utilisez un modèle plus large spécialisé pour ces tâches. |
| Les appels d’outils de l’agent IA ne fonctionnent pas bien   | - Tester et valider la sortie de l’outil en dehors du système agent.<br>- Affiner les paramètres définis, prompts, et noms des outils.  |
| Le système multi-agent ne fonctionne pas de manière cohérente | - Affiner les prompts donnés à chaque agent pour qu’ils soient spécifiques et distincts.<br>- Construire un système hiérarchique avec un agent « router » ou contrôleur pour déterminer quel agent est approprié. |

Beaucoup de ces problèmes peuvent être mieux identifiés grâce à l'observabilité. Les traces et métriques évoquées plus tôt aident à localiser précisément où dans le workflow de l’agent les problèmes se produisent, rendant le débogage et l’optimisation beaucoup plus efficaces.

## Gestion des coûts


Voici quelques stratégies pour gérer les coûts de déploiement des agents IA en production :

**Utilisation de modèles plus petits :** Les petits modèles de langage (SLMs) peuvent bien fonctionner pour certains cas d’utilisation agentique et réduiront considérablement les coûts. Comme mentionné précédemment, construire un système d’évaluation pour déterminer et comparer les performances par rapport aux modèles plus grands est la meilleure façon de comprendre la performance d’un SLM pour votre cas d’usage. Envisagez d’utiliser des SLM pour des tâches simples comme la classification d’intention ou l’extraction de paramètres, tout en réservant les modèles plus grands pour un raisonnement complexe.

**Utilisation d’un modèle routeur :** Une stratégie similaire consiste à utiliser une diversité de modèles et de tailles. Vous pouvez utiliser un LLM/SLM ou une fonction serverless pour router les requêtes en fonction de leur complexité vers les modèles les plus adaptés. Cela aidera également à réduire les coûts tout en garantissant des performances pour les tâches appropriées. Par exemple, orientez les requêtes simples vers des modèles plus petits et plus rapides, et n’utilisez les grands modèles coûteux que pour les tâches de raisonnement complexes.

**Mise en cache des réponses :** Identifier les requêtes et tâches courantes et fournir les réponses avant qu’elles ne passent par votre système agentique est un bon moyen de réduire le volume des requêtes similaires. Vous pouvez même mettre en place un flux pour identifier la similitude d’une requête avec vos requêtes en cache en utilisant des modèles d’IA plus simples. Cette stratégie peut considérablement réduire les coûts pour les questions fréquemment posées ou les flux de travail courants.

## Voyons comment cela fonctionne en pratique

Dans le [carnet d’exemples de cette section](./code_samples/10-expense_claim-demo.ipynb), nous verrons des exemples d’utilisation des outils d’observabilité pour surveiller et évaluer notre agent.


### Vous avez plus de questions sur les agents IA en production ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Leçon précédente

[Modèle de conception métacognition](../09-metacognition/README.md)

## Leçon suivante

[Protocoles agentiques](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->