[![Intro to AI Agents](../../../translated_images/fr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Cliquez sur l'image ci-dessus pour regarder la vidéo de cette leçon)_

# Introduction aux agents IA et cas d'utilisation des agents

Bienvenue dans le cours **Agents IA pour débutants** ! Ce cours vous donne les connaissances fondamentales — et du code fonctionnel réel — pour commencer à créer des agents IA depuis zéro.

Venez dire bonjour dans la <a href="https://discord.gg/kzRShWzttr" target="_blank">Communauté Discord Azure AI</a> — elle est pleine d'apprenants et de constructeurs d'IA qui seront heureux de répondre à vos questions.

Avant de nous lancer dans la construction, assurons-nous de bien comprendre ce qu'est un agent IA *et* quand il est pertinent d'en utiliser un.

---

## Introduction

Cette leçon couvre :

- Ce que sont les agents IA, et les différents types qui existent
- Pour quels types de tâches les agents IA sont les mieux adaptés
- Les blocs de construction essentiels que vous utiliserez pour concevoir une solution agentique

## Objectifs d'apprentissage

À la fin de cette leçon, vous devriez être capable de :

- Expliquer ce qu'est un agent IA et comment il se distingue d'une solution IA classique
- Savoir quand utiliser un agent IA (et quand ne pas le faire)
- Esquisser une conception de solution agentique basique pour un problème réel

---

## Définir les agents IA et les types d'agents IA

### Qu'est-ce qu'un agent IA ?

Voici une façon simple d’y penser :

> **Les agents IA sont des systèmes qui permettent aux grands modèles de langage (LLM) de *faire réellement des choses* — en leur fournissant des outils et des connaissances pour interagir avec le monde, pas seulement répondre à des requêtes.**

Décomposons cela un peu :

- **Système** — Un agent IA n’est pas juste une chose unique. C’est un ensemble de composants fonctionnant ensemble. Au cœur de chaque agent, il y a trois pièces :
  - **Environnement** — L’espace dans lequel l’agent travaille. Pour un agent de réservation de voyage, ce serait la plateforme de réservation elle-même.
  - **Capteurs** — Comment l’agent lit l’état actuel de son environnement. Notre agent de voyage pourrait vérifier la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** — Comment l’agent agit. L’agent de voyage pourrait réserver une chambre, envoyer une confirmation, ou annuler une réservation.

![Qu’est-ce qu’un agent IA ?](../../../translated_images/fr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grands modèles de langage** — Les agents existaient avant les LLM, mais ce sont les LLM qui rendent les agents modernes si puissants. Ils peuvent comprendre le langage naturel, raisonner sur le contexte, et transformer une demande vague de l’utilisateur en un plan d’action concret.

- **Exécuter des actions** — Sans système agent, un LLM génère juste du texte. Dans un système agent, le LLM peut réellement *exécuter* des étapes — chercher dans une base de données, appeler une API, envoyer un message.

- **Accès aux outils** — Les outils que l’agent peut utiliser dépendent (1) de l’environnement dans lequel il fonctionne et (2) de ce que le développeur lui a donné. Un agent de voyage pourrait être capable de chercher des vols mais pas de modifier les dossiers clients — tout dépend des connexions que vous configurez.

- **Mémoire + Connaissances** — Les agents peuvent avoir une mémoire à court terme (la conversation en cours) et une mémoire à long terme (une base de données clients, les interactions passées). L’agent de voyage pourrait « se souvenir » que vous préférez des sièges côté fenêtre.

---

### Les différents types d’agents IA

Tous les agents ne sont pas construits de la même manière. Voici un aperçu des principaux types, utilisant un agent de réservation de voyage comme exemple :

| **Type d’agent** | **Ce qu’il fait** | **Exemple d’agent de voyage** |
|---|---|---|
| **Agents réflexes simples** | Suit des règles codées en dur — sans mémoire, sans planification. | Voit un email de plainte → le transfère au service client. C’est tout. |
| **Agents réflexes basés sur un modèle** | Garde un modèle interne du monde et le met à jour au fur et à mesure des changements. | Suit les prix historiques des vols et signale les itinéraires devenus soudainement chers. |
| **Agents basés sur un objectif** | A un objectif en tête et trouve comment l’atteindre étape par étape. | Réserve un voyage complet (vols, voiture, hôtel) en partant de votre position actuelle pour vous amener à votre destination. |
| **Agents basés sur l’utilité** | Ne trouve pas juste *une* solution — cherche la *meilleure* en pesant les compromis. | Équilibre coût vs. commodité pour trouver le voyage le plus adapté à vos préférences. |
| **Agents apprenants** | S’améliore avec le temps en apprenant des retours. | Ajuste les recommandations futures de réservation selon les résultats des enquêtes post-voyage. |
| **Agents hiérarchiques** | Un agent de haut niveau divise le travail en sous-tâches et délègue à des agents de niveau inférieur. | Une demande « annuler le voyage » est divisée en : annuler le vol, annuler l’hôtel, annuler la location de voiture — chacune gérée par un sous-agent. |
| **Systèmes multi-agents (MAS)** | Plusieurs agents indépendants travaillent ensemble (ou en compétition). | Coopératif : agents séparés pour gérer hôtels, vols, divertissements. Compétitif : plusieurs agents rivalisent pour remplir les chambres d’hôtel au meilleur prix. |

---

## Quand utiliser les agents IA

Ce n’est pas parce que vous *pouvez* utiliser un agent IA que vous *devez* toujours le faire. Voici les situations où les agents brillent vraiment :

![Quand utiliser les agents IA ?](../../../translated_images/fr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problèmes à résolution ouverte** — Lorsque les étapes pour résoudre un problème ne peuvent pas être préprogrammées. L’LLM doit déterminer le chemin de façon dynamique.
- **Processus à plusieurs étapes** — Des tâches qui nécessitent d’utiliser des outils à travers plusieurs tours, pas seulement une simple recherche ou génération.
- **Amélioration au fil du temps** — Lorsque vous voulez que le système devienne plus intelligent grâce aux retours des utilisateurs ou aux signaux de l’environnement.

Nous approfondirons plus tard dans le cours, dans la leçon **Construire des agents IA fiables**, quand (et quand *ne pas*) utiliser les agents IA.

---

## Bases des solutions agentiques

### Développement d’agent

La première chose à faire quand on construit un agent est de définir *ce qu’il peut faire* — ses outils, actions, et comportements.

Dans ce cours, nous utilisons le **Azure AI Agent Service** comme plateforme principale. Il prend en charge :

- Des modèles de fournisseurs comme OpenAI, Mistral, et Meta (Llama)
- Des données sous licence de fournisseurs comme Tripadvisor
- Des définitions d’outils standardisées OpenAPI 3.0

### Patterns agentiques

Vous communiquez avec les LLM via des prompts. Avec les agents, vous ne pouvez pas toujours concevoir chaque prompt manuellement — l’agent doit agir sur plusieurs étapes. C’est là que les **patterns agentiques** entrent en jeu. Ce sont des stratégies réutilisables pour susciter et orchestrer les LLM de manière plus évolutive et fiable.

Ce cours est organisé autour des patterns agentiques les plus courants et utiles.

### Frameworks agentiques

Les frameworks agentiques offrent aux développeurs des modèles, outils, et infrastructures prêts à l’emploi pour construire des agents. Ils facilitent :

- Le branchement des outils et capacités
- L’observation des actions de l’agent (et le débogage en cas de problème)
- La collaboration entre plusieurs agents

Dans ce cours, nous nous concentrons sur le **Microsoft Agent Framework (MAF)** pour construire des agents prêts pour la production.

---

## Exemples de code

Prêt à voir ça en action ? Voici les exemples de code pour cette leçon :

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
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->