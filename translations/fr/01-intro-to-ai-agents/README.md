[![Introduction aux agents IA](../../../translated_images/fr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Cliquez sur l'image ci-dessus pour regarder la vidéo de cette leçon)_

# Introduction aux agents IA et cas d'utilisation des agents

Bienvenue dans le cours **Agents IA pour débutants** ! Ce cours vous offre les connaissances fondamentales — et du code fonctionnel réel — pour commencer à créer des agents IA depuis zéro.

Venez dire bonjour dans la <a href="https://discord.gg/kzRShWzttr" target="_blank">communauté Discord Azure AI</a> — elle regorge d'apprenants et de créateurs d'IA heureux de répondre à vos questions.

Avant de nous lancer dans la construction, assurons-nous de bien comprendre ce qu'est un agent IA et quand il est pertinent d'en utiliser un.

---

## Introduction

Cette leçon couvre :

- Ce que sont les agents IA, et les différents types qui existent
- Pour quels types de tâches les agents IA sont les mieux adaptés
- Les éléments de base que vous utiliserez pour concevoir une solution agentique

## Objectifs d'apprentissage

À la fin de cette leçon, vous devriez être capable de :

- Expliquer ce qu'est un agent IA et en quoi il diffère d'une solution IA classique
- Savoir quand utiliser un agent IA (et quand ne pas le faire)
- Esquisser une conception basique d'une solution agentique pour un problème réel

---

## Définition des agents IA et types d'agents IA

### Qu'est-ce qu'un agent IA ?

Voici une façon simple de le comprendre :

> **Les agents IA sont des systèmes qui permettent aux grands modèles de langage (LLM) de réellement *faire des choses* — en leur fournissant des outils et des connaissances pour agir sur le monde, pas seulement répondre à des requêtes.**

Décomposons cela un peu :

- **Système** — Un agent IA n'est pas une seule chose. C'est un ensemble de composants qui fonctionnent ensemble. Au cœur, chaque agent comprend trois parties :
  - **Environnement** — L'espace dans lequel l'agent opère. Pour un agent de réservation de voyage, ce serait la plateforme de réservation elle-même.
  - **Capteurs** — La manière dont l'agent lit l'état actuel de son environnement. Notre agent voyage pourrait vérifier la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** — La façon dont l'agent agit. L'agent voyage pourrait réserver une chambre, envoyer une confirmation ou annuler une réservation.

![Qu'est-ce qu'un agent IA ?](../../../translated_images/fr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grands modèles de langage** — Les agents existaient avant les LLM, mais ce sont ces derniers qui rendent les agents modernes si puissants. Ils peuvent comprendre le langage naturel, raisonner sur le contexte, et transformer une requête vague en un plan d'action concret.

- **Effectuer des actions** — Sans système agent, un LLM ne fait que générer du texte. Dans un système agent, le LLM peut réellement *exécuter* des étapes — chercher dans une base de données, appeler une API, envoyer un message.

- **Accès aux outils** — Les outils que l'agent peut utiliser dépendent (1) de l'environnement dans lequel il fonctionne et (2) de ce que le développeur a choisi de lui fournir. Un agent voyage pourrait pouvoir rechercher des vols mais pas modifier les dossiers clients — tout dépend de ce que vous connectez.

- **Mémoire + Connaissances** — Les agents peuvent disposer d'une mémoire à court terme (la conversation en cours) et d'une mémoire à long terme (une base de données clients, interactions passées). L'agent voyage pourrait "se souvenir" que vous préférez les sièges côté fenêtre.

---

### Les différents types d'agents IA

Tous les agents ne sont pas construits de la même manière. Voici un aperçu des principaux types, avec l'exemple récurrent d'un agent de réservation de voyage :

| **Type d'agent** | **Ce qu'il fait** | **Exemple agent voyage** |
|---|---|---|
| **Agents réflexes simples** | Suit des règles codées en dur — pas de mémoire, pas de planification. | Voit un email de plainte → le transfère au service client. C’est tout. |
| **Agents réflexes basés sur un modèle** | Conserve un modèle interne du monde et le met à jour au fil des changements. | Suit l'historique des prix des vols et signale les itinéraires devenus soudainement chers. |
| **Agents basés sur un objectif** | A un objectif en tête et détermine comment l’atteindre étape par étape. | Réserve un voyage complet (vols, voiture, hôtel) depuis votre position actuelle jusqu’à votre destination. |
| **Agents basés sur l’utilité** | Ne trouve pas juste *une* solution — trouve la *meilleure* en évaluant les compromis. | Équilibre coût et commodité pour trouver le voyage qui correspond le mieux à vos préférences. |
| **Agents apprenants** | S'améliore avec le temps en apprenant des retours. | Ajuste les recommandations futures en fonction des résultats des enquêtes post-voyage. |
| **Agents hiérarchiques** | Un agent de haut niveau divise le travail en sous-tâches et délègue à des agents de niveau inférieur. | Une demande "annuler voyage" est divisée en : annuler vol, annuler hôtel, annuler location de voiture — chacun pris en charge par un sous-agent. |
| **Systèmes multi-agents (MAS)** | Plusieurs agents indépendants travaillant ensemble (ou en compétition). | Coopératif : agents distincts gèrent hôtels, vols, et divertissements. Compétitif : plusieurs agents se disputent les chambres d’hôtel au meilleur prix. |

---

## Quand utiliser des agents IA

Ce n’est pas parce que vous *pouvez* utiliser un agent IA que vous *devez* toujours le faire. Voici les situations où les agents brillent vraiment :

![Quand utiliser les agents IA ?](../../../translated_images/fr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problèmes ouverts** — Lorsque les étapes pour résoudre un problème ne peuvent pas être préprogrammées. Il faut que le LLM détermine dynamiquement le chemin.
- **Processus multi-étapes** — Tâches qui nécessitent l’usage d’outils sur plusieurs tours, pas juste une simple recherche ou génération.
- **Amélioration progressive** — Quand vous voulez que le système devienne plus intelligent grâce aux retours utilisateur ou aux signaux de l’environnement.

Nous approfondirons quand (et quand *ne pas*) utiliser des agents IA dans la leçon **Construire des agents IA fiables** plus loin dans le cours.

---

## Bases des solutions agentiques

### Développement d’agents

La première chose à faire lors de la création d’un agent est de définir *ce qu’il peut faire* — ses outils, actions et comportements.

Dans ce cours, nous utilisons le **Azure AI Agent Service** comme plateforme principale. Il supporte :

- Des modèles ouverts comme OpenAI, Mistral et Llama
- Des données sous licence de fournisseurs tels que Tripadvisor
- Des définitions d’outils standardisées OpenAPI 3.0

### Patrons agentiques

Vous communiquez avec les LLM via des prompts. Avec les agents, vous ne pouvez pas toujours concevoir manuellement chaque prompt — l’agent doit agir sur plusieurs étapes. C’est là que les **patrons agentiques** interviennent. Ce sont des stratégies réutilisables pour formuler les prompts et orchestrer les LLM de façon plus évolutive et fiable.

Ce cours est structuré autour des patrons agentiques les plus communs et utiles.

### Frameworks agentiques

Les frameworks agentiques fournissent aux développeurs des modèles, outils et infrastructures prêts à l’emploi pour construire des agents. Ils facilitent :

- La connexion des outils et capacités
- L’observation de l’activité de l’agent (et le débogage en cas de problème)
- La collaboration entre plusieurs agents

Dans ce cours, nous nous concentrons sur le **Microsoft Agent Framework (MAF)** pour créer des agents prêts pour la production.

---

## Exemples de code

Prêt à voir cela en action ? Voici les exemples de code pour cette leçon :

- 🐍 Python : [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET : [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Des questions ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour connecter avec d’autres apprenants, participer aux heures de bureau, et faire répondre vos questions sur les agents IA par la communauté.

---

## Leçon précédente

[Configuration du cours](../00-course-setup/README.md)

## Leçon suivante

[Explorer les frameworks agentiques](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Clause de non-responsabilité** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->