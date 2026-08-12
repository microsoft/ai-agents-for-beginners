[![Introduction aux agents IA](../../../translated_images/fr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Cliquez sur l'image ci-dessus pour regarder la vidéo de cette leçon)_

# Introduction aux agents IA et cas d'utilisation des agents

Bienvenue dans le cours **Agents IA pour débutants** ! Ce cours vous donne les connaissances fondamentales — et du code fonctionnel — pour commencer à construire des agents IA à partir de zéro.

Venez dire bonjour dans la <a href="https://discord.gg/kzRShWzttr" target="_blank">communauté Discord Azure AI</a> — elle est remplie d’apprenants et de créateurs IA heureux de répondre à vos questions.

Avant de nous lancer dans la construction, assurons-nous d’abord de bien comprendre ce qu’est un agent IA et dans quelles situations il est pertinent d’en utiliser un.

---

## Introduction

Cette leçon couvre :

- Ce que sont les agents IA, et les différents types qui existent
- Pour quelles tâches les agents IA sont les plus adaptés
- Les éléments fondamentaux que vous utiliserez pour concevoir une solution agentique

## Objectifs d’apprentissage

À la fin de cette leçon, vous devriez être capable de :

- Expliquer ce qu’est un agent IA et en quoi il diffère d’une solution IA classique
- Savoir quand recourir à un agent IA (et quand ne pas le faire)
- Esquisser une conception basique de solution agentique pour un problème du monde réel

---

## Définir les agents IA et les types d’agents IA

### Qu’est-ce qu’un agent IA ?

Voici une façon simple d’y penser :

> **Les agents IA sont des systèmes qui permettent aux grands modèles de langage (LLM) de réellement *agir* — en leur fournissant des outils et des connaissances pour agir sur le monde, pas seulement répondre à des requêtes.**

Décomposons cela un peu :

- **Système** — Un agent IA n’est pas une seule chose. C’est un ensemble de parties qui fonctionnent ensemble. Au cœur, chaque agent comporte trois éléments :
  - **Environnement** — L’espace dans lequel l’agent travaille. Pour un agent de réservation de voyage, c’est la plateforme de réservation elle-même.
  - **Capteurs** — Comment l’agent lit l’état actuel de son environnement. Notre agent de voyage peut vérifier la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** — Comment l’agent agit. L’agent de voyage peut réserver une chambre, envoyer une confirmation ou annuler une réservation.

![Qu’est-ce que les agents IA ?](../../../translated_images/fr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Grands modèles de langage** — Les agents existaient avant les LLM, mais ce sont les LLM qui rendent les agents modernes si puissants. Ils peuvent comprendre le langage naturel, raisonner sur le contexte et transformer une demande vague en un plan d’action concret.

- **Effectuer des actions** — Sans un système agentique, un LLM ne fait que générer du texte. Dans un système agentique, le LLM peut réellement *exécuter* des étapes — chercher dans une base de données, appeler une API, envoyer un message.

- **Accès aux outils** — Les outils que l’agent peut utiliser dépendent (1) de l’environnement dans lequel il fonctionne et (2) de ce que le développeur a choisi de lui donner. Un agent de voyage pourrait pouvoir rechercher des vols mais pas modifier des dossiers clients — tout dépend de ce que vous connectez.

- **Mémoire + Connaissances** — Les agents peuvent avoir une mémoire à court terme (la conversation en cours) et une mémoire à long terme (une base de données client, des interactions passées). L’agent de voyage pourrait "se souvenir" que vous préférez les sièges côté fenêtre.

---

### Les différents types d’agents IA

Tous les agents ne sont pas construits de la même façon. Voici un aperçu des principaux types, avec un agent de réservation de voyage comme exemple récurrent :

| **Type d’agent** | **Ce qu’il fait** | **Exemple d’agent de voyage** |
|---|---|---|
| **Agents à réflexe simple** | Suit des règles codées en dur — pas de mémoire, pas de planification. | Reçoit un email de plainte → le transfère au service client. C’est tout. |
| **Agents à réflexe basé sur un modèle** | Maintient un modèle interne du monde et le met à jour au fur et à mesure que les choses changent. | Suit les prix historiques des vols et signale les trajets qui deviennent soudainement chers. |
| **Agents basés sur un objectif** | A un objectif en tête et trouve comment l’atteindre étape par étape. | Réserve un voyage complet (vols, voiture, hôtel) à partir de votre lieu actuel pour vous amener à destination. |
| **Agents basés sur l’utilité** | Ne trouve pas simplement *une* solution — trouve la *meilleure* en pesant les compromis. | Équilibre coût vs commodité pour trouver le voyage qui correspond le mieux à vos préférences. |
| **Agents apprenants** | S’améliore avec le temps en apprenant des retours. | Ajuste les recommandations futures de réservation selon les résultats des enquêtes post-voyage. |
| **Agents hiérarchiques** | Un agent de haut niveau décompose le travail en sous-tâches et délègue aux agents de niveau inférieur. | Une demande "annuler le voyage" est divisée en : annuler vol, annuler hôtel, annuler location de voiture — chacun géré par un sous-agent. |
| **Systèmes multi-agents (MAS)** | Plusieurs agents indépendants travaillant ensemble (ou en compétition). | Coopératif : agents séparés gèrent hôtels, vols et divertissements. Compétitif : plusieurs agents se disputent les chambres d’hôtel au meilleur prix. |

---

## Quand utiliser les agents IA

Ce n’est pas parce que vous *pouvez* utiliser un agent IA que vous *devez* toujours le faire. Voici les situations où les agents excellent vraiment :

![Quand utiliser les agents IA ?](../../../translated_images/fr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problèmes ouverts** — Lorsque les étapes pour résoudre un problème ne peuvent pas être préprogrammées. Vous avez besoin que le LLM détermine le chemin dynamiquement.
- **Processus multi-étapes** — Tâches nécessitant l’utilisation d’outils sur plusieurs séquences, pas juste une recherche ou génération unique.
- **Amélioration dans le temps** — Quand vous voulez que le système devienne plus intelligent grâce aux retours utilisateurs ou aux signaux environnementaux.

Nous approfondirons quand (et quand *pas*) utiliser des agents IA dans la leçon **Construire des agents IA fiables** plus tard dans le cours.

---

## Bases des solutions agentiques

### Développement d’agents

La première chose à faire lors de la construction d’un agent est de définir *ce qu’il peut faire* — ses outils, actions et comportements.

Dans ce cours, nous utilisons le **Microsoft Foundry Agent Service** comme plateforme principale. Il supporte :

- Modèles de fournisseurs comme OpenAI, Mistral et Meta (Llama)
- Données sous licence de fournisseurs comme Tripadvisor
- Définitions d’outils standardisées OpenAPI 3.0

### Schémas agentiques

Vous communiquez avec les LLM via des invites (prompts). Avec les agents, vous ne pouvez pas toujours créer manuellement chaque prompt — l’agent doit agir sur plusieurs étapes. C’est là qu’interviennent les **schémas agentiques**. Ce sont des stratégies réutilisables pour inviter et orchestrer les LLM de manière plus évolutive et fiable.

Ce cours est structuré autour des schémas agentiques les plus courants et utiles.

### Frameworks agentiques

Les frameworks agentiques offrent aux développeurs des modèles, outils et infrastructures prêts à l’emploi pour construire des agents. Ils facilitent :

- Le raccordement des outils et capacités
- L’observation de ce que fait l’agent (et le débogage en cas d’erreur)
- La collaboration entre plusieurs agents

Dans ce cours, nous nous concentrons sur le **Microsoft Agent Framework (MAF)** pour construire des agents prêts à la production.

---

## Exemples de code

Prêt à voir cela en action ? Voici les exemples de code pour cette leçon :

- 🐍 Python : [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET : [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Des questions ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour connecter avec d’autres apprenants, assister aux heures de bureau et faire répondre vos questions sur les agents IA par la communauté.


---

## Test rapide de cet agent (optionnel)

Une fois que vous aurez appris à déployer des agents dans la [Leçon 16](../16-deploying-scalable-agents/README.md), vous pourrez ajouter un contrôle rapide de santé post-déploiement pour le `TravelAgent` de cette leçon avec le catalogue prêt à l’emploi [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Voir le fichier [`tests/README.md`](../tests/README.md) pour savoir comment l’exécuter.

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