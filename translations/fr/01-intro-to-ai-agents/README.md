[![Intro to AI Agents](../../../translated_images/fr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_


# Introduction aux agents IA et cas d'utilisation des agents

Bienvenue dans le cours "Agents IA pour débutants" ! Ce cours fournit des connaissances fondamentales et des exemples pratiques pour construire des agents IA.

Rejoignez la <a href="https://discord.gg/kzRShWzttr" target="_blank">communauté Discord Azure AI</a> pour rencontrer d'autres apprenants et constructeurs d'agents IA et poser toutes vos questions sur ce cours.

Pour commencer ce cours, nous débutons par une meilleure compréhension de ce que sont les agents IA et comment nous pouvons les utiliser dans les applications et flux de travail que nous développons.

## Introduction

Cette leçon couvre :

- Qu'est-ce qu'un agent IA et quels sont les différents types d'agents ?
- Quels cas d'utilisation sont les plus adaptés aux agents IA et comment peuvent-ils nous aider ?
- Quels sont certains des blocs de base lors de la conception de solutions à base d'agents ?

## Objectifs d'apprentissage
Après avoir terminé cette leçon, vous devriez être capable de :

- Comprendre les concepts d'agents IA et comment ils diffèrent des autres solutions IA.
- Appliquer les agents IA de la manière la plus efficace.
- Concevoir des solutions agentiques de manière productive pour les utilisateurs et les clients.

## Définition des agents IA et types d'agents IA

### Qu'est-ce qu'un agent IA ?

Les agents IA sont des **systèmes** qui permettent aux **Grand Modèles de Langage (LLMs)** de **réaliser des actions** en étendant leurs capacités en donnant aux LLMs **l'accès à des outils** et **des connaissances**.

Décortiquons cette définition en parties plus petites :

- **Système** – Il est important de penser aux agents non pas comme à un seul composant mais comme à un système composé de nombreux composants. Au niveau basique, les composants d’un agent IA sont :
  - **Environnement** – L’espace défini dans lequel l’agent IA opère. Par exemple, si nous avons un agent IA de réservation de voyages, l’environnement pourrait être le système de réservation de voyages que l’agent IA utilise pour accomplir des tâches.
  - **Capteurs** – Les environnements contiennent des informations et fournissent des retours. Les agents IA utilisent des capteurs pour recueillir et interpréter ces informations sur l’état actuel de l’environnement. Dans l’exemple de l’agent de réservation de voyages, le système de réservation peut fournir des informations telles que la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** – Une fois que l’agent IA reçoit l’état actuel de l’environnement, pour la tâche en cours, l’agent détermine quelle action mener pour modifier l’environnement. Pour l’agent de réservation de voyages, cela pourrait être de réserver une chambre disponible pour l’utilisateur.

![What Are AI Agents?](../../../translated_images/fr/what-are-ai-agents.1ec8c4d548af601a.webp)

**Grands Modèles de Langage** – Le concept d’agents existait avant la création des LLMs. L’avantage de construire des agents IA avec des LLMs est leur capacité à interpréter le langage humain et les données. Cette capacité permet aux LLMs d’interpréter les informations de l’environnement et de définir un plan pour changer l’environnement.

**Réaliser des actions** – En dehors des systèmes d’agents IA, les LLMs sont limités aux situations où l’action consiste à générer du contenu ou des informations sur la base d’une requête utilisateur. À l’intérieur des systèmes d’agents IA, les LLMs peuvent accomplir des tâches en interprétant la demande de l’utilisateur et en utilisant les outils disponibles dans leur environnement.

**Accès aux outils** – Les outils auxquels le LLM a accès sont définis par 1) l’environnement dans lequel il opère et 2) le développeur de l’agent IA. Pour notre exemple d’agent de voyage, les outils de l’agent sont limités par les opérations disponibles dans le système de réservation, et/ou le développeur peut limiter l’accès de l’agent aux outils liés aux vols.

**Mémoire + Connaissances** – La mémoire peut être à court terme dans le contexte de la conversation entre l’utilisateur et l’agent. À long terme, en dehors des informations fournies par l’environnement, les agents IA peuvent aussi récupérer des connaissances depuis d’autres systèmes, services, outils et même d’autres agents. Dans l’exemple de l’agent de voyage, ces connaissances pourraient être les informations sur les préférences de voyage de l’utilisateur situées dans une base de données client.

### Les différents types d’agents

Maintenant que nous avons une définition générale des agents IA, voyons certains types spécifiques d’agents et comment ils pourraient être appliqués à un agent IA de réservation de voyages.

| **Type d’Agent**              | **Description**                                                                                                                     | **Exemple**                                                                                                                                                                                                                  |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agents réflexes simples**   | Effectuent des actions immédiates basées sur des règles prédéfinies.                                                               | L’agent de voyage interprète le contexte d’un email et transmet les plaintes de voyage au service client.                                                                                                                   |
| **Agents réflexes basés sur un modèle** | Effectuent des actions basées sur un modèle du monde et les changements apportés à ce modèle.                                       | L’agent de voyage priorise les itinéraires avec des changements significatifs de prix en se basant sur l’accès aux données historiques de tarification.                                                                      |
| **Agents basés sur des objectifs** | Créent des plans pour atteindre des objectifs spécifiques en interprétant l’objectif et en déterminant les actions pour l’atteindre. | L’agent de voyage réserve un trajet en déterminant les arrangements nécessaires (voiture, transports en commun, vols) depuis le lieu actuel jusqu’à la destination.                                                         |
| **Agents basés sur l’utilité** | Prennent en compte les préférences et pèsent numériquement les compromis pour déterminer comment atteindre les objectifs.          | L’agent de voyage maximise l’utilité en pesant la commodité versus le coût lors de la réservation de voyages.                                                                                                                |
| **Agents apprentissages**     | S’améliorent avec le temps en répondant aux feedbacks et ajustant les actions en conséquence.                                       | L’agent de voyage s’améliore en utilisant les retours clients issus des enquêtes post-voyage pour ajuster les futures réservations.                                                                                         |
| **Agents hiérarchiques**      | Comptent plusieurs agents dans un système en niveaux, avec des agents de niveau supérieur divisant les tâches en sous-tâches pour les agents de niveau inférieur. | L’agent de voyage annule un voyage en divisant la tâche en sous-tâches (par exemple, annuler des réservations spécifiques) et en faisant réaliser ces sous-tâches par des agents de niveau inférieur, avec compte-rendu à l’agent supérieur. |
| **Systèmes multi-agents (MAS)** | Les agents accomplissent des tâches de manière indépendante, soit de façon coopérative, soit compétitive.                          | Coopératif : Plusieurs agents réservent des services de voyage spécifiques comme hôtels, vols et loisirs. Compétitif : Plusieurs agents gèrent et se disputent un calendrier partagé de réservation d’hôtel pour client réserver dans l’hôtel. |

## Quand utiliser les agents IA

Dans la section précédente, nous avons utilisé le cas d’utilisation d’un agent de voyage pour expliquer comment les différents types d’agents peuvent être utilisés dans divers scénarios de réservation de voyages. Nous continuerons à utiliser cette application tout au long du cours.

Regardons les types de cas d’utilisation pour lesquels les agents IA sont les plus adaptés :

![When to use AI Agents?](../../../translated_images/fr/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problèmes ouverts** – permettant au LLM de déterminer les étapes nécessaires pour accomplir une tâche car elles ne peuvent pas toujours être codées en dur dans un flux de travail.
- **Processus multi-étapes** – tâches nécessitant un certain niveau de complexité dans lequel l’agent IA doit utiliser des outils ou des informations sur plusieurs tours de conversation plutôt qu’une simple récupération unique.  
- **Amélioration au fil du temps** – tâches où l’agent peut s’améliorer avec le temps en recevant des retours soit de son environnement, soit des utilisateurs afin de fournir une meilleure utilité.

Nous abordons plus de considérations sur l’utilisation des agents IA dans la leçon Construire des agents IA dignes de confiance.

## Bases des solutions agentiques

### Développement d’agent

La première étape dans la conception d’un système d’agent IA est de définir les outils, actions et comportements. Dans ce cours, nous nous concentrons sur l’utilisation de **Azure AI Agent Service** pour définir nos agents. Il offre des fonctionnalités telles que :

- Sélection de modèles open source comme OpenAI, Mistral et Llama
- Utilisation de données sous licence via des fournisseurs comme Tripadvisor
- Utilisation d’outils OpenAPI 3.0 standardisés

### Schémas agentiques

La communication avec les LLMs se fait par prompts. Étant donné la nature semi-autonome des agents IA, il n’est pas toujours possible ou nécessaire de solliciter manuellement à nouveau le LLM après un changement dans l’environnement. Nous utilisons des **schémas agentiques** qui permettent de solliciter les LLMs sur plusieurs étapes de manière plus évolutive.

Ce cours est divisé en certains des schémas agentiques populaires actuels.

### Frameworks agentiques

Les frameworks agentiques permettent aux développeurs d’implémenter des schémas agentiques via du code. Ces frameworks offrent des templates, plugins et outils pour une meilleure collaboration entre agents IA. Ces avantages procurent des capacités d’observabilité et de dépannage améliorées des systèmes d’agents IA.

Dans ce cours, nous explorerons le Microsoft Agent Framework (MAF) pour la création d’agents IA prêts pour la production.

## Codes exemples

- Python : [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Vous avez d’autres questions sur les agents IA ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Leçon précédente

[Configuration du cours](../00-course-setup/README.md)

## Leçon suivante

[Exploration des frameworks agentiques](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->