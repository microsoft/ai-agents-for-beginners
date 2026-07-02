# Agents IA pour débutants - Guide d'étude

Utilisez ce guide comme compagnon pratique pendant que vous suivez le cours. Il ne
remplace pas les leçons. Il vous aide à décider où commencer, quoi chercher dans
chaque leçon, et comment connecter les idées pour créer une petite démo d'agent
fonctionnel.

Si c'est votre première fois ici, commencez simple :

1. Lisez la [Configuration du cours](./00-course-setup/README.md).
2. Complétez les leçons 01-06 dans l'ordre.
3. Gardez en tête une petite idée de démo pendant que vous apprenez.
4. Après chaque leçon, demandez-vous : « Que peut faire mon agent maintenant qu’il
   ne pouvait pas faire avant ? »

## Une démo simple à garder en tête

Une bonne façon d’apprendre les agents est de suivre une idée de démo tout au
long du cours.

Exemple de démo : **un agent assistant de cours**.

L'utilisateur demande :

> « Je veux apprendre comment les agents utilisent des outils. Trouve les bonnes
> leçons, résume ce que je dois lire en premier, et donne-moi une courte tâche
> pratique. »

Un chatbot classique peut répondre selon ce qu’il sait déjà. Un agent peut faire plus :

1. **Lire ou rechercher dans les fichiers du cours** pour trouver les bonnes leçons.
2. **Utiliser des outils** pour récupérer des liens de leçon, des exemples ou du
   matériel de support.
3. **Planifier** un court parcours d'apprentissage au lieu de donner une longue
   réponse.
4. **Utiliser le contexte** de la conversation en cours pour rester concentré sur
   le but de l’apprenant.
5. **Se souvenir de préférences utiles** si l’application prend en charge la mémoire.
6. **Afficher des traces, citations ou journaux** pour que l'utilisateur puisse
   comprendre ce qui s’est passé.
7. **Appliquer des garde-fous** avant d’agir de manière risquée ou d’utiliser des
   données sensibles.

Au fur et à mesure que vous étudiez chaque leçon, revenez à cette démo et demandez :
quelle nouvelle capacité cette leçon ajouterait-elle ?

## Vers quoi vous construisez

À la fin du cours, vous devriez pouvoir expliquer et construire des systèmes
d’agents qui combinent ces parties :

| Partie          | Sens en langage simple                          | Dans la démo                                      |
|-----------------|------------------------------------------------|--------------------------------------------------|
| Modèle          | Le moteur de raisonnement qui interprète la demande de l'utilisateur | Comprend que l'apprenant veut des leçons sur l'utilisation des outils |
| Outils          | Fonctions, API, fichiers, navigateurs ou services que l'agent peut utiliser | Recherche dans le dépôt ou récupère le contenu des leçons |
| Connaissances   | Documents ou données utilisés pour appuyer la réponse | Fichiers README du cours et matériel de leçon |
| Contexte        | Informations incluses dans l’appel modèle suivant | Le but de l’utilisateur et les résultats des outils |
| Mémoire         | Informations sauvegardées pour une utilisation ultérieure | L’apprenant préfère des exemples Python pratiques |
| Planification   | Décomposer un objectif plus large en étapes plus petites | Trouve des leçons, les résume, suggère une pratique |
| Orchestration   | Acheminer le travail entre outils, étapes, ou agents | Un planificateur appelle un outil de recherche, puis un résumé |
| Confiance       | Sécurité, sûreté, évaluation et observabilité   | Enregistre les appels aux outils et demande avant actions à fort impact |

## Choisissez votre parcours d'apprentissage

Vous pouvez suivre le cours complet dans l’ordre, ou passer directement à un parcours
selon ce que vous voulez construire.

| Si votre objectif est de...              | Commencez par | Puis étudiez            |
|-----------------------------------------|---------------|------------------------|
| Comprendre ce que sont les agents       | 01, 02, 03    | 04, 05, 06             |
| Construire un agent qui utilise des outils | 04            | 05, 07, 14             |
| Construire un agent basé sur RAG         | 05            | 04, 06, 12             |
| Concevoir des workflows multi-étapes     | 07            | 08, 09, 14             |
| Comprendre les systèmes multi-agents     | 08            | 07, 09, 11             |
| Préparer des agents pour la production   | 06, 10        | 12, 13, 18             |
| Explorer les protocoles et l’automatisation navigateur | 11, 15        | 10, 18                 |

Astuce : si vous êtes nouveau aux agents, ne sautez pas les leçons 01-06. Elles vous
apportent le vocabulaire nécessaire pour le reste du cours.

## Guide leçon par leçon

| Leçon                                                     | Ce que vous apprenez                                                | Essayez ceci après la leçon                                  |
|-----------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| [01 - Introduction aux agents IA](./01-intro-to-ai-agents/README.md)          | Ce qui différencie un agent d’un chatbot basique.                 | Expliquez votre idée de démo comme un agent, pas seulement une application de chat. |
| [02 - Frameworks agentiques](./02-explore-agentic-frameworks/README.md)         | Comment les frameworks gèrent modèles, outils, état et workflows. | Identifiez quelles parties de votre démo un framework gérerait. |
| [03 - Patterns de conception agentique](./03-agentic-design-patterns/README.md) | Les modèles communs pour concevoir le comportement des agents.    | Esquissez le parcours utilisateur avant d’écrire du code.  |
| [04 - Utilisation d'outils](./04-tool-use/README.md)                           | Comment les agents appellent des outils pour obtenir des données ou agir. | Définissez un outil dont votre agent démo aurait besoin.    |
| [05 - RAG agentique](./05-agentic-rag/README.md)                              | Comment la recherche ancre les réponses des agents dans des documents ou données. | Décidez quelle source de connaissances votre démo doit chercher. |
| [06 - Agents dignes de confiance](./06-building-trustworthy-agents/README.md) | Comment ajouter des garde-fous, une supervision et un comportement plus sûr. | Ajoutez une règle pour quand l’agent doit demander à l’utilisateur en premier. |
| [07 - Conception de la planification](./07-planning-design/README.md)         | Comment les agents décomposent un plus grand objectif en petits pas. | Écrivez un plan en trois étapes pour votre requête de démo. |
| [08 - Conception multi-agent](./08-multi-agent/README.md)                     | Quand répartir le travail entre plusieurs agents spécialisés.     | Décidez si votre démo a besoin d’un seul agent ou plusieurs. |
| [09 - Métacognition](./09-metacognition/README.md)                            | Comment les agents peuvent revoir et améliorer leur propre sortie. | Ajoutez une auto-vérification finale avant que l’agent réponde. |
| [10 - Agents IA en production](./10-ai-agents-production/README.md)           | Ce qui change quand un agent passe de démo à production.           | Dressez la liste de ce que vous surveilleriez : qualité, coût, latence, échecs. |
| [11 - Protocoles agentiques](./11-agentic-protocols/README.md)                | Comment les protocoles connectent les agents aux outils et autres agents. | Identifiez où un protocole standard pourrait simplifier l’intégration. |
| [12 - Ingénierie du contexte](./12-context-engineering/README.md)             | Comment sélectionner, couper, isoler et gérer le contexte.        | Décidez ce qui doit être dans l'invite et ce qui doit rester à l'écart. |
| [13 - Mémoire agent](./13-agent-memory/README.md)                            | Comment les agents peuvent sauvegarder des informations utiles entre interactions. | Choisissez une préférence sûre que votre démo pourrait mémoriser. |
| [14 - Framework agent Microsoft](./14-microsoft-agent-framework/README.md)   | Blocs bâtisseurs spécifiques au framework pour agents et workflows. | Reliez les étapes de votre démo aux concepts du framework.  |
| [15 - Agents d’utilisation informatique](./15-browser-use/README.md)         | Comment les agents peuvent interagir avec une interface navigateur ou UI. | Choisissez une tâche navigateur qui devrait toujours nécessiter une confirmation utilisateur. |
| [18 - Sécurisation des agents IA](./18-securing-ai-agents/README.md)          | Comment rendre les actions des agents plus auditables et infalsifiables. | Décidez quelles actions dans votre démo doivent être journalisées ou reçues. |

Les leçons 16 et 17 sont listées dans le README principal comme à venir. Ajoutez-les
à votre plan d’études lorsque le contenu sera disponible.

## Idées clés en termes accessibles aux débutants

### Outils

Un outil est quelque chose que l’agent peut appeler pour faire un travail en dehors
du modèle. Un bon outil a un nom clair, une tâche étroite, des entrées typées, une
sortie prévisible, et une manière sécurisée d’échouer.

Pour la démo de l’assistant de cours, un outil pourrait être :

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG et Connaissances

RAG aide l’agent à répondre à partir de matériel source au lieu de deviner. Dans ce
cours, ce matériel source pourrait être les fichiers README des leçons, des exemples
de code ou des ressources externes liées aux leçons.

Utilisez RAG quand la réponse doit être appuyée par des documents, des données, ou
des fichiers de projet actuels.

### Planification

La planification est utile lorsque la demande comporte plus d’une étape. Gardez les
plans courts et assez visibles pour qu’un développeur ou un utilisateur puisse les
inspecter.

Pour la démo, un plan pourrait être :

1. Trouver les leçons liées à l’utilisation d’outils.  
2. Résumer les leçons les plus pertinentes.  
3. Recommander une tâche pratique.

### Contexte

Le contexte est ce que le modèle voit maintenant. Trop peu de contexte peut faire
manquer des détails importants à l’agent. Trop de contexte peut rendre l’agent plus
lent, plus coûteux, ou plus facile à confondre.

Une bonne ingénierie du contexte signifie choisir la bonne information pour le
prochain appel modèle.

### Mémoire

La mémoire est l’information sauvegardée pour plus tard. Ne sauvegardez pas tout.
Sauvegardez uniquement quand c’est utile, sûr, et facile à mettre à jour ou supprimer.

Par exemple, se souvenir que « l’apprenant préfère les exemples Python » peut être
utile. Se souvenir de données personnelles sensibles en général ne l’est pas.

### Évaluation et Observabilité

L’évaluation demande : l’agent a-t-il fait ce qu’il fallait ?

L’observabilité demande : peut-on voir comment cela s’est passé ?

Pour les agents en production, gardez une trace des appels modèle, des appels outils,
du contexte récupéré, de la latence, des coûts, des échecs, et des retours utilisateurs.

### Confiance et Sécurité

Les agents dignes de confiance ont besoin de plus qu’une simple invite utile. Utilisez
des outils à privilèges minimaux, une approbation humaine pour les actions à fort
impact, une anonymisation des données quand nécessaire, et des journaux ou reçus pour
les actions devant être auditées.

## Une routine de revue de 15 minutes

Utilisez cette routine après chaque leçon :

1. **Résumez la leçon en une phrase.**  
2. **Nommez la nouvelle capacité de l’agent.** Par exemple : utilisation d’outils,
   recherche, planification, mémoire, observabilité ou sécurité.  
3. **Ajoutez-la à la démo assistant de cours.** Qu’est-ce qui change dans la démo ?  
4. **Trouvez le risque.** Que pourrait-il mal se passer si cette capacité est mal utilisée ?  
5. **Écrivez une question de test.** Comment vérifier que l’agent se comporte bien ?  

## Auto-vérification rapide

Avant de continuer, essayez de répondre à ces questions :

1. Que peut faire un agent que ne peut pas faire un chatbot régulier tout seul ?  
2. Quel outil votre agent aurait-il besoin en premier, et pourquoi ?  
3. Quelle source de connaissances devrait appuyer la réponse de l’agent ?  
4. Quel contexte devrait être inclus dans le prochain appel modèle ?  
5. Que devrait se souvenir l’agent, et que devrait-il éviter de stocker ?  
6. Quand l’agent devrait-il demander une approbation humaine ?  
7. Quels journaux, traces ou reçus vous aideraient à déboguer ou auditer l’agent plus tard ?

## Exercice de synthèse suggéré

À la fin du cours, construisez un petit agent qui aide un apprenant à naviguer dans ce
répertoire.

Version minimale :

- Accepter un sujet de l’utilisateur.  
- Trouver les leçons les plus pertinentes.  
- Résumer ce qu'il faut lire en premier.  
- Suggérer une tâche pratique.  
- Montrer quels fichiers ou liens de leçon ont été utilisés.

Version poussée :

- Se souvenir du langage de programmation préféré de l’apprenant.  
- Utiliser un plan simple avant de répondre.  
- Ajouter une étape d’auto-vérification avant la réponse finale.  
- Enregistrer les appels aux outils et les sources récupérées.  
- Demander confirmation avant d’ouvrir des tâches d’automatisation navigateur ou interface.

Cela vous offre un moyen petit mais réaliste de pratiquer outils, RAG, planification,
contexte, mémoire, observabilité et confiance dans un seul projet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->