# Agents IA pour débutants - Guide d'étude

Utilisez ce guide comme un compagnon pratique pendant que vous avancez dans le cours. Il ne
remplace pas les leçons. Il vous aide à décider par où commencer, ce qu'il faut
rechercher dans chaque leçon, et comment connecter les idées pour un petit agent
démonstration fonctionnel.

Si c'est votre première fois ici, commencez simple :

1. Lisez la [Configuration du cours](./00-course-setup/README.md).
2. Complétez les leçons 01-06 dans l'ordre.
3. Gardez une petite idée de démonstration en tête pendant que vous apprenez.
4. Après chaque leçon, demandez-vous : "Que peut faire mon agent maintenant qu'il
   ne pouvait pas faire avant ?"

## Une démonstration simple à garder en tête

Une bonne façon d'apprendre les agents est de suivre une idée de démonstration tout au long du cours.

Exemple de démonstration : **un agent assistant de cours**.

L'utilisateur demande :

> "Je veux apprendre comment les agents utilisent des outils. Trouve les bonnes leçons,
> résume ce que je devrais lire en premier, et donne-moi une courte tâche pratique."

Un chatbot classique peut répondre à partir de ce qu'il sait déjà. Un agent peut faire plus :

1. **Lire ou rechercher dans les fichiers du cours** pour trouver les bonnes leçons.
2. **Utiliser des outils** pour récupérer des liens de leçons, des exemples ou du matériel
   de soutien.
3. **Planifier** un parcours d'apprentissage court au lieu de donner une longue réponse.
4. **Utiliser le contexte** de la conversation actuelle pour rester concentré sur
   l'objectif de l'apprenant.
5. **Se souvenir des préférences utiles** si l'application supporte la mémoire.
6. **Montrer des traces, citations ou journaux** pour que l'utilisateur comprenne ce qui s'est passé.


Pendant que vous étudiez chaque leçon, revenez à cette démonstration et demandez : quelle




À la fin du cours, vous devriez être capable d'expliquer et construire des systèmes


| Partie | Signification en français clair | Dans la démonstration |
|------|-------------------------------|---------------------|
| Modèle | Le moteur de raisonnement qui interprète la requête de l'utilisateur | Comprend que l'apprenant veut des leçons sur l'usage des outils |
| Outils | Fonctions, API, fichiers, navigateurs ou services que l'agent peut utiliser | Recherche dans le dépôt ou récupère le contenu des leçons |
| Connaissances | Documents ou données utilisées pour fonder la réponse | Fichiers README du cours et matériel des leçons |
| Contexte | Informations incluses dans l'appel suivant au modèle | L'objectif de l'utilisateur et les résultats des outils |
| Mémoire | Informations sauvegardées pour usage ultérieur | L'apprenant préfère des exemples Python pratiques |
| Planification | Découpage d'un objectif plus grand en étapes plus petites | Trouver des leçons, les résumer, suggérer des exercices |
| Orchestration | Répartition du travail sur les outils, étapes ou agents | Un planificateur appelle un outil de recherche, puis un résumé |






Au fur et à mesure que vous suivez les leçons, vous avez plusieurs options de fournisseur :

- **Microsoft Foundry / Azure OpenAI (API Responses)** — la voie principale utilisée dans les leçons. Connectez-vous avec `az login` pour une authentification Entra ID sans clé.
- **Foundry Local** — exécutez les modèles entièrement sur l'appareil via une API compatible OpenAI (sans cloud, sans clés API). Idéal pour les expérimentations hors ligne ou sans coût. Voir [Configuration du cours](./00-course-setup/README.md).
- **MiniMax** — un fournisseur compatible OpenAI avec modèles à contexte large, utilisable comme alternative clé en main.

> **Note :** GitHub Models est obsolète (retrait prévu en juillet 2026) et ne prend pas en charge l'API Responses. Les exemples ont été mis à jour pour utiliser Azure OpenAI / Microsoft Foundry à la place.

## Choisissez votre parcours d'apprentissage

Vous pouvez suivre le cours complet dans l'ordre, ou passer directement à un parcours selon ce que vous souhaitez
construire.

| Si votre objectif est de... | Commencez par | Étudiez ensuite |
|------------------------|-------------|---------------|
| Comprendre ce qu’est un agent | 01, 02, 03 | 04, 05, 06 |
| Construire un agent qui utilise des outils | 04 | 05, 07, 14 |
| Construire un agent basé sur RAG | 05 | 04, 06, 12 |
| Concevoir des workflows multi-étapes | 07 | 08, 09, 14 |
| Comprendre les systèmes multi-agents | 08 | 07, 09, 11 |
| Préparer des agents pour la production | 06, 10 | 12, 13, 16, 18 |
| Déployer et scaler les agents sur Foundry | 10, 16 | 06, 13, 18 |
| Construire des agents locaux / hors-ligne | 17 | 04, 05, 11 |
| Explorer les protocoles et l'automatisation navigateur | 11, 15 | 10, 18 |

Astuce : si vous êtes nouveau dans les agents, ne sautez pas les leçons 01-06. Elles vous donnent
le vocabulaire nécessaire pour le reste du cours.

## Guide leçon par leçon

| Leçon | Ce que vous apprenez | Essayez ceci après la leçon |
|-------|----------------------|------------------------------|
| [01 - Introduction aux agents IA](./01-intro-to-ai-agents/README.md) | Ce qui différencie un agent d'un chatbot basique. | Expliquez votre idée de démo en tant qu'agent, pas juste une app de chat. |
| [02 - Cadres agentiques](./02-explore-agentic-frameworks/README.md) | Comment les cadres aident avec les modèles, outils, état et workflows. | Identifiez quelles parties de votre démo un cadre gérerait. |
| [03 - Modèles de conception agentique](./03-agentic-design-patterns/README.md) | Modèles courants pour concevoir le comportement d’un agent. | Esquissez le parcours utilisateur avant de coder. |
| [04 - Utilisation d'outils](./04-tool-use/README.md) | Comment les agents appellent des outils pour obtenir des données ou agir. | Définissez un outil dont votre agent de démo aurait besoin. |
| [05 - RAG agentique](./05-agentic-rag/README.md) | Comment la récupération ancre les réponses d’agent dans des documents ou des données. | Décidez quelle source de connaissance votre démo doit interroger. |

| [06 - Agents dignes de confiance](./06-building-trustworthy-agents/README.md) | Comment ajouter des garde-fous, une supervision et un comportement plus sûr. | Ajoutez une règle pour quand l’agent doit d’abord demander à l’utilisateur. |
| [07 - Conception de la planification](./07-planning-design/README.md) | Comment les agents divisent des objectifs plus grands en étapes plus petites. | Rédigez un plan en trois étapes pour votre demande de démonstration. |
| [08 - Conception multi-agents](./08-multi-agent/README.md) | Quand répartir le travail entre plusieurs agents spécialisés. | Décidez si votre démonstration a besoin d’un agent ou de plusieurs. |
| [09 - Métacognition](./09-metacognition/README.md) | Comment les agents peuvent revoir et améliorer leur propre sortie. | Ajoutez une vérification finale avant que l’agent ne réponde. |
| [10 - Agents IA en production](./10-ai-agents-production/README.md) | Ce qui change lorsqu’un agent passe de la démonstration à la production. | Listez ce que vous surveilleriez : qualité, coût, latence, échecs. |
| [11 - Protocoles agentiques](./11-agentic-protocols/README.md) | Comment les protocoles connectent les agents aux outils et aux autres agents. | Identifiez où un protocole standard pourrait simplifier l’intégration. |
| [12 - Ingénierie du contexte](./12-context-engineering/README.md) | Comment sélectionner, réduire, isoler et gérer le contexte. | Décidez ce qui appartient à l’invite et ce qui doit être exclu. |
| [13 - Mémoire de l’agent](./13-agent-memory/README.md) | Comment les agents peuvent sauvegarder des informations utiles entre les interactions. | Choisissez une préférence sûre que votre démonstration pourrait mémoriser. |
| [14 - Cadre Agent Microsoft](./14-microsoft-agent-framework/README.md) | Blocs de construction spécifiques au cadre pour agents et workflows, plus l’hébergement d’agents LangChain/LangGraph sur Microsoft Foundry. | Faites correspondre les étapes de votre démonstration aux concepts du cadre. |
| [15 - Agents d’utilisation informatique](./15-browser-use/README.md) | Comment les agents peuvent interagir avec des interfaces de navigateur ou UI, avec des exemples réels comme Microsoft Project Opal. | Choisissez une tâche du navigateur qui devrait toujours nécessiter une confirmation utilisateur. |
| [16 - Déploiement d’agents évolutifs](./16-deploying-scalable-agents/README.md) | Comment passer d’un prototype à un déploiement en production évolutif et observable sur Microsoft Foundry (agents hébergés, routage des modèles, mise en cache, portes d’évaluation, tests de fumée). | Listez les préoccupations liées à la production que votre démonstration doit encore traiter : hébergement, routage, coût, évaluation. |
| [17 - Création d’agents IA locaux](./17-creating-local-ai-agents/README.md) | Comment construire des agents "local-first" qui fonctionnent entièrement sur votre machine avec Foundry Local et Qwen (outils locaux, RAG local, MCP local). | Décidez quelles parties de votre démonstration doivent rester privées et s’exécuter localement. |
| [18 - Sécurisation des agents IA](./18-securing-ai-agents/README.md) | Comment rendre les actions des agents plus auditables et à l’épreuve des manipulations. | Décidez quelles actions dans votre démonstration doivent être journalisées ou reçues. |

## Validation des agents déployés avec des tests de fumée

Quand vous déployez un agent (leçon 16), un **test de fumée** est la première vérification la moins coûteuse
pour vérifier que le déploiement répond effectivement. Ce dépôt fournit des catalogues prêts à l’emploi
sous [tests/](./tests/README.md) pour les agents déployables des leçons
01, 04, 05 et 16, connectés au

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Exécutez-les à partir de l’onglet **Actions** après avoir déployé l’agent de la leçon.
Les tests de fumée sont une première étape — évaluation hors ligne et en ligne (Leçons 10 et 16)
vous indiquant à quel point l’agent est *bon*.

## Idées Clés en Termes Simples

### Outils

Un outil est quelque chose que l’agent peut appeler pour effectuer un travail en dehors du modèle. Un bon outil
a un nom clair, une tâche étroite, des entrées typées, une sortie prévisible et un moyen sûr
d’échouer.

Pour la démo d’aide au cours, un outil pourrait être :

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG et Connaissance

RAG aide l’agent à répondre à partir du matériel source au lieu de deviner. Dans ce
cours, ce matériel source pourrait être les README des leçons, des exemples de code ou des
ressources externes liées aux leçons.

Utilisez RAG lorsque la réponse doit être fondée sur des documents, des données ou des
fichiers de projet actuels.

### Planification

La planification est utile lorsque la demande comporte plusieurs étapes. Gardez les plans courts et
suffisamment visibles pour qu’un développeur ou un utilisateur puisse les inspecter.

Pour la démo, un plan pourrait être :

1. Trouver les leçons liées à l’utilisation des outils.
2. Résumer les leçons les plus pertinentes.
3. Recommander une tâche pratique.

### Contexte

Le contexte est ce que le modèle voit actuellement. Un contexte trop faible peut faire
manquer des détails importants à l’agent. Un contexte trop important peut rendre l’agent plus lent, plus
coûteux ou plus facile à confondre.

Une bonne ingénierie du contexte signifie choisir les bonnes informations pour le prochain appel
au modèle.

### Mémoire

La mémoire est l’information sauvegardée pour plus tard. Ne sauvegardez pas tout. Sauvegardez l’information
uniquement quand elle est utile, sûre et facile à mettre à jour ou à supprimer.

Par exemple, se souvenir que « l’apprenant préfère des exemples en Python » peut être utile.
Se souvenir de données personnelles sensibles ne l’est généralement pas.

### Évaluation et Observabilité

L’évaluation demande : est-ce que l’agent a fait ce qu’il fallait ?

L’observabilité demande : peut-on voir comment cela s’est produit ?

Pour les agents en production, suivez les appels au modèle, les appels aux outils, le contexte récupéré,
la latence, le coût, les échecs et les retours utilisateurs.

### Confiance et Sécurité

Les agents fiables ont besoin de plus qu’une simple invite utile. Utilisez des outils à moindre privilège,
l’approbation humaine pour les actions à fort impact, la rédaction des données quand nécessaire, et des journaux ou
des reçus pour les actions qui doivent être auditées.

## Une Routine de Revue de 15 Minutes

Utilisez cette routine après chaque leçon :

1. **Résumez la leçon en une phrase.**
2. **Nommez la nouvelle capacité de l’agent.** Par exemple : utilisation d’outil, récupération,
   planification, mémoire, observabilité ou sécurité.
3. **Ajoutez-la à la démo d’aide au cours.** Qu’est-ce qui change dans la démo maintenant ?
4. **Identifiez le risque.** Que pourrait-il arriver de mal si cette capacité est mal utilisée ?
5. **Écrivez une question de test.** Comment vérifieriez-vous que l’agent se comporte bien ?

## Auto-vérification Rapide

Avant de continuer, essayez de répondre à ces questions :

1. Que peut faire un agent qu’un chatbot classique ne peut pas faire seul ?
2. Quel outil votre agent devrait-il avoir en premier, et pourquoi ?
3. Quelle source de connaissance devrait fonder la réponse de l’agent ?
4. Quel contexte devrait être inclus dans le prochain appel au modèle ?

5. Que doit se souvenir l'agent, et que doit-il éviter de stocker ?
6. Quand l'agent doit-il demander une approbation humaine ?
7. Quels journaux, traces ou reçus vous aideraient à déboguer ou auditer l'agent plus tard ?


## Exercice de synthèse suggéré

À la fin du cours, construisez un petit agent qui aide un apprenant à naviguer dans ce
dépôt.

Version minimale :

- Accepter un sujet de la part de l'utilisateur.
- Trouver les leçons les plus pertinentes.
- Résumer ce qu'il faut lire en premier.
- Suggérer une tâche pratique à réaliser.
- Montrer quels fichiers ou liens de leçons ont été utilisés.

Version avancée :

- Se souvenir du langage de programmation préféré de l'apprenant.
- Utiliser un plan simple avant de répondre.
- Ajouter une étape d'auto-vérification avant la réponse finale.
- Enregistrer les appels d'outils et les sources consultées.
- Demander confirmation avant d'ouvrir le navigateur ou d'exécuter des tâches d'automatisation UI.

Cela vous offre une manière petite mais réaliste de pratiquer les outils, RAG, la planification,
le contexte, la mémoire, l'observabilité, et la confiance dans un seul projet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->