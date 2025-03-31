<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "233e7a18025a27eae95b653e9b5b5aa5",
  "translation_date": "2025-03-28T10:10:29+00:00",
  "source_file": "01-intro-to-ai-agents\\README.md",
  "language_code": "fr"
}
-->
[![Introduction aux Agents IA](../../../translated_images/lesson-1-thumbnail.062500b037054b99431a123879d8c1f55899d942cfc286f105e8c5ce417fe51e.fr.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

# Introduction aux Agents IA et Cas d'utilisation des Agents

Bienvenue dans le cours "Agents IA pour débutants" ! Ce cours offre des connaissances fondamentales et des exemples pratiques pour créer des Agents IA.

Rejoignez-nous pour rencontrer d'autres apprenants et créateurs d'Agents IA et poser toutes vos questions sur ce cours.

Pour commencer ce cours, nous allons d'abord mieux comprendre ce que sont les Agents IA et comment nous pouvons les utiliser dans les applications et les flux de travail que nous développons.

## Introduction

Cette leçon couvre :

- Que sont les Agents IA et quels sont les différents types d'agents ?
- Quels cas d'utilisation sont les mieux adaptés aux Agents IA et comment peuvent-ils nous aider ?
- Quels sont les principaux éléments à prendre en compte lors de la conception de solutions basées sur des agents ?

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous devriez être capable de :

- Comprendre les concepts des Agents IA et en quoi ils diffèrent des autres solutions IA.
- Utiliser les Agents IA de manière efficace.
- Concevoir des solutions basées sur des agents de manière productive pour les utilisateurs et les clients.

## Définir les Agents IA et leurs types

### Que sont les Agents IA ?

Les Agents IA sont des **systèmes** qui permettent aux **modèles de langage étendus (LLMs)** de **réaliser des actions** en étendant leurs capacités en leur donnant **accès à des outils** et à des **connaissances**.

Décomposons cette définition en plusieurs parties :

- **Système** - Il est important de considérer les agents non pas comme un simple composant, mais comme un système composé de plusieurs éléments. À un niveau basique, les composants d'un Agent IA sont :
  - **Environnement** - L'espace défini où l'Agent IA opère. Par exemple, si nous avions un agent de réservation de voyages, l'environnement pourrait être le système de réservation de voyages que l'Agent IA utilise pour accomplir ses tâches.
  - **Capteurs** - Les environnements fournissent des informations et des retours. Les Agents IA utilisent des capteurs pour collecter et interpréter ces informations sur l'état actuel de l'environnement. Dans l'exemple de l'agent de réservation de voyages, le système de réservation peut fournir des informations telles que la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** - Une fois que l'Agent IA reçoit l'état actuel de l'environnement, pour la tâche en cours, l'agent détermine quelle action effectuer pour modifier l'environnement. Pour l'agent de réservation de voyages, cela pourrait être de réserver une chambre disponible pour l'utilisateur.

![Que sont les Agents IA ?](../../../translated_images/what-are-ai-agents.125520f55950b252a429b04a9f41e0152d4dafa1f1bd9081f4f574631acb759e.fr.png)

**Modèles de langage étendus** - Le concept des agents existait avant la création des LLMs. L'avantage de construire des Agents IA avec des LLMs réside dans leur capacité à interpréter le langage humain et les données. Cette capacité permet aux LLMs d'interpréter les informations environnementales et de définir un plan pour modifier l'environnement.

**Réaliser des actions** - En dehors des systèmes d'Agents IA, les LLMs sont limités à des situations où l'action consiste à générer du contenu ou des informations en fonction de l'invite de l'utilisateur. Dans les systèmes d'Agents IA, les LLMs peuvent accomplir des tâches en interprétant la demande de l'utilisateur et en utilisant les outils disponibles dans leur environnement.

**Accès aux outils** - Les outils auxquels le LLM a accès sont définis par 1) l'environnement dans lequel il opère et 2) le développeur de l'Agent IA. Dans notre exemple d'agent de voyage, les outils de l'agent sont limités par les opérations disponibles dans le système de réservation, et/ou le développeur peut limiter l'accès de l'agent aux outils liés aux vols.

**Connaissances** - En dehors des informations fournies par l'environnement, les Agents IA peuvent également récupérer des connaissances à partir d'autres systèmes, services, outils, et même d'autres agents. Dans l'exemple de l'agent de voyage, ces connaissances pourraient inclure les préférences de voyage de l'utilisateur situées dans une base de données client.

### Les différents types d'agents

Maintenant que nous avons une définition générale des Agents IA, examinons certains types spécifiques d'agents et comment ils pourraient être appliqués à un agent de réservation de voyages.

| **Type d'agent**              | **Description**                                                                                                                       | **Exemple**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agents réflexes simples**   | Effectuent des actions immédiates basées sur des règles prédéfinies.                                                                   | L'agent de voyage interprète le contexte d'un email et transfère les plaintes de voyage au service client.                                                                                                                     |
| **Agents réflexes basés sur un modèle** | Effectuent des actions basées sur un modèle du monde et des changements dans ce modèle.                                                   | L'agent de voyage priorise les itinéraires avec des changements significatifs de prix en se basant sur l'accès à des données historiques de tarification.                                                                      |
| **Agents basés sur des objectifs**     | Créent des plans pour atteindre des objectifs spécifiques en interprétant l'objectif et en déterminant les actions nécessaires pour y parvenir. | L'agent de voyage organise un voyage en déterminant les arrangements nécessaires (voiture, transport public, vols) depuis l'emplacement actuel jusqu'à la destination.                                                         |
| **Agents basés sur l'utilité**        | Prennent en compte les préférences et évaluent les compromis numériquement pour déterminer comment atteindre les objectifs.                | L'agent de voyage maximise l'utilité en pesant la commodité contre le coût lors de la réservation.                                                                                                                             |
| **Agents apprenants**                | S'améliorent avec le temps en répondant aux retours et en ajustant leurs actions en conséquence.                                           | L'agent de voyage s'améliore grâce aux retours des clients via des enquêtes post-voyage pour effectuer des ajustements sur les réservations futures.                                                                            |
| **Agents hiérarchiques**             | Impliquent plusieurs agents dans un système hiérarchique, avec des agents de niveau supérieur divisant les tâches en sous-tâches pour que les agents de niveau inférieur les accomplissent. | L'agent de voyage annule un voyage en divisant la tâche en sous-tâches (par exemple, annuler des réservations spécifiques) et en demandant aux agents de niveau inférieur de les accomplir, tout en rapportant au niveau supérieur. |
| **Systèmes multi-agents (MAS)**      | Les agents accomplissent des tâches de manière indépendante, soit de manière coopérative, soit compétitive.                                  | Coopératif : Plusieurs agents réservent des services spécifiques de voyage tels que des hôtels, des vols et des divertissements. Compétitif : Plusieurs agents gèrent et se disputent un calendrier de réservation d'hôtel partagé pour loger les clients. |

## Quand utiliser les Agents IA

Dans la section précédente, nous avons utilisé le cas d'utilisation de l'agent de voyage pour expliquer comment différents types d'agents peuvent être utilisés dans différents scénarios de réservation de voyages. Nous continuerons à utiliser cette application tout au long du cours.

Examinons les types de cas d'utilisation où les Agents IA sont les mieux adaptés :

![Quand utiliser les Agents IA ?](../../../translated_images/when-to-use-ai-agents.912b9a02e9e0e2af45a3e24faa4e912e334ec23f21f0cf5cb040b7e899b09cd0.fr.png)

- **Problèmes ouverts** - Permettre au LLM de déterminer les étapes nécessaires pour accomplir une tâche parce qu'elles ne peuvent pas toujours être codées en dur dans un flux de travail.
- **Processus multi-étapes** - Tâches nécessitant un niveau de complexité dans lequel l'Agent IA doit utiliser des outils ou des informations sur plusieurs tours au lieu d'une récupération unique.  
- **Amélioration au fil du temps** - Tâches où l'agent peut s'améliorer au fil du temps en recevant des retours de son environnement ou des utilisateurs pour fournir une meilleure utilité.

Nous abordons davantage de considérations sur l'utilisation des Agents IA dans la leçon sur la création d'Agents IA de confiance.

## Bases des solutions basées sur des agents

### Développement des agents

La première étape pour concevoir un système d'Agent IA est de définir les outils, les actions et les comportements. Dans ce cours, nous nous concentrons sur l'utilisation du **Azure AI Agent Service** pour définir nos agents. Il offre des fonctionnalités telles que :

- La sélection de modèles ouverts tels que OpenAI, Mistral et Llama
- L'utilisation de données sous licence via des fournisseurs comme Tripadvisor
- L'utilisation d'outils standardisés OpenAPI 3.0

### Modèles basés sur des agents

La communication avec les LLMs se fait via des invites. Étant donné la nature semi-autonome des Agents IA, il n'est pas toujours possible ou nécessaire de reformuler manuellement l'invite du LLM après un changement dans l'environnement. Nous utilisons des **modèles basés sur des agents** qui nous permettent de formuler des invites au LLM sur plusieurs étapes de manière plus évolutive.

Ce cours est divisé en certains des modèles basés sur des agents actuellement populaires.

### Cadres basés sur des agents

Les cadres basés sur des agents permettent aux développeurs de mettre en œuvre des modèles basés sur des agents via du code. Ces cadres offrent des modèles, des plugins et des outils pour une meilleure collaboration entre Agents IA. Ces avantages permettent une meilleure observabilité et un dépannage des systèmes d'Agents IA.

Dans ce cours, nous explorerons le cadre AutoGen, axé sur la recherche, ainsi que le cadre Agent prêt pour la production de Semantic Kernel.

## Leçon précédente

[Configuration du cours](../00-course-setup/README.md)

## Leçon suivante

[Explorer les cadres basés sur des agents](../02-explore-agentic-frameworks/README.md)

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.