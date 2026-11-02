# Mémoire pour les agents IA
[![Agent Memory](../../../translated_images/fr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Lorsque l'on discute des avantages uniques à créer des agents IA, deux points sont principalement abordés : la capacité à utiliser des outils pour accomplir des tâches et la capacité à s'améliorer avec le temps. La mémoire est à la base de la création d’agents auto-améliorants capables d’offrir de meilleures expériences à nos utilisateurs.

Dans cette leçon, nous allons examiner ce qu’est la mémoire pour les agents IA, comment nous pouvons la gérer et l’utiliser au bénéfice de nos applications.

## Introduction

Cette leçon couvre :

• **Comprendre la mémoire des agents IA** : Ce qu’est la mémoire et pourquoi elle est essentielle pour les agents.

• **Implémenter et stocker la mémoire** : Méthodes pratiques pour ajouter des capacités de mémoire à vos agents IA, en se concentrant sur la mémoire à court terme et à long terme.

• **Rendre les agents IA auto-améliorants** : Comment la mémoire permet aux agents d’apprendre des interactions passées et de s’améliorer avec le temps.

## Implémentations disponibles

Cette leçon comprend deux tutoriels complets en notebook :

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)** : Implémente la mémoire avec Mem0 et Azure AI Search utilisant le Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)** : Implémente une mémoire structurée avec Cognee, construisant automatiquement un graphe de connaissances avec des embeddings, visualisant le graphe et une récupération intelligente

## Objectifs d’apprentissage

Après avoir terminé cette leçon, vous saurez comment :

• **Différencier les divers types de mémoire des agents IA**, incluant la mémoire de travail, à court terme et à long terme, ainsi que des formes spécialisées comme la mémoire de persona et la mémoire épisodique.

• **Implémenter et gérer la mémoire à court terme et à long terme pour les agents IA** en utilisant Microsoft Agent Framework, avec des outils comme Mem0, Cognee, la mémoire tableau blanc, et en intégrant Azure AI Search.

• **Comprendre les principes derrière les agents IA auto-améliorants** et comment des systèmes robustes de gestion de la mémoire contribuent à l’apprentissage continu et à l’adaptation.

## Comprendre la mémoire des agents IA

Fondamentalement, **la mémoire des agents IA désigne les mécanismes qui leur permettent de retenir et de rappeler des informations**. Ces informations peuvent être des détails spécifiques sur une conversation, des préférences utilisateur, des actions passées ou même des schémas appris.

Sans mémoire, les applications IA sont souvent sans état, ce qui signifie que chaque interaction repart de zéro. Cela conduit à une expérience utilisateur répétitive et frustrante où l’agent « oublie » le contexte ou les préférences précédentes.

### Pourquoi la mémoire est-elle importante ?

L’intelligence d’un agent est étroitement liée à sa capacité à se souvenir et à utiliser les informations passées. La mémoire permet aux agents d’être :

• **Réfléchis** : Apprendre des actions et résultats passés.

• **Interactifs** : Maintenir le contexte pendant une conversation en cours.

• **Proactifs et réactifs** : Anticiper les besoins ou répondre de manière appropriée en se basant sur des données historiques.

• **Autonomes** : Fonctionner plus indépendamment en s’appuyant sur les connaissances stockées.

L’objectif de l’implémentation de la mémoire est de rendre les agents plus **fiables et performants**.

### Types de mémoire

#### Mémoire de travail

Considérez-la comme une feuille de brouillon qu’un agent utilise pendant une tâche ou un processus de pensée unique et en cours. Elle contient les informations immédiates nécessaires pour calculer l’étape suivante.

Pour les agents IA, la mémoire de travail capture souvent les informations les plus pertinentes d’une conversation, même si tout l’historique du chat est long ou tronqué. Elle se concentre sur l’extraction d’éléments clés tels que les exigences, propositions, décisions et actions.

**Exemple de mémoire de travail**

Dans un agent de réservation de voyage, la mémoire de travail pourrait capturer la demande actuelle de l’utilisateur, par exemple « Je veux réserver un voyage à Paris ». Cette exigence spécifique est maintenue dans le contexte immédiat de l’agent pour guider l’interaction en cours.

#### Mémoire à court terme

Ce type de mémoire conserve l’information pendant la durée d’une seule conversation ou session. C’est le contexte du chat actuel, permettant à l’agent de faire référence aux tours précédents du dialogue.

Dans les exemples du SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), cela correspond à `AgentSession`, créé avec `agent.create_session()`. La session est la mémoire à court terme intégrée au framework : elle garde le contexte de la conversation disponible tant que cette même session est réutilisée, mais ce contexte n’est pas conservé lorsque la session se termine ou que l’application redémarre. Utilisez la mémoire à long terme pour les faits et préférences qui doivent survivre entre les sessions, généralement via une base de données, un index vectoriel ou un autre stockage persistant.

**Exemple de mémoire à court terme**

Si un utilisateur demande « Combien coûte un vol pour Paris ? » puis enchaîne avec « Et pour l’hébergement là-bas ? », la mémoire à court terme garantit que l’agent comprend que « là-bas » réfère à « Paris » dans la même conversation.

#### Mémoire à long terme

Ce sont des informations qui persistent à travers plusieurs conversations ou sessions. Elle permet aux agents de se souvenir des préférences utilisateur, des interactions historiques ou des connaissances générales sur une longue période. C’est important pour la personnalisation.

**Exemple de mémoire à long terme**

Une mémoire à long terme pourrait stocker que « Ben aime le ski et les activités en plein air, apprécie le café avec vue sur la montagne, et souhaite éviter les pistes de ski avancées à cause d’une blessure passée ». Cette information, apprise lors d’interactions précédentes, influence les recommandations lors des prochaines sessions de planification de voyage, les rendant très personnalisées.

#### Mémoire de persona

Ce type de mémoire spécialisé aide un agent à développer une « personnalité » ou « persona » cohérente. Il permet à l’agent de retenir des détails sur lui-même ou son rôle prévu, rendant les interactions plus fluides et ciblées.

**Exemple de mémoire de persona**
Si l’agent de voyage est conçu pour être un « expert en planification de ski », la mémoire de persona pourrait renforcer ce rôle, influençant ses réponses pour s’aligner avec le ton et les connaissances d’un expert.

#### Mémoire de workflow/épisodique

Cette mémoire stocke la séquence des étapes qu’un agent suit durant une tâche complexe, incluant succès et échecs. C’est comme se souvenir d’« épisodes » ou expériences passées afin d’apprendre d’eux.

**Exemple de mémoire épisodique**

Si l’agent a tenté de réserver un vol spécifique mais que cela a échoué à cause d’une indisponibilité, la mémoire épisodique pourrait enregistrer cet échec, permettant à l’agent d’essayer des vols alternatifs ou d’informer l’utilisateur plus précisément lors d’une tentative ultérieure.

#### Mémoire d’entité

Cela implique d’extraire et de mémoriser des entités spécifiques (comme des personnes, lieux, ou objets) et des événements à partir des conversations. Cela permet à l’agent de construire une compréhension structurée des éléments clés discutés.

**Exemple de mémoire d’entité**

D’une conversation sur un voyage passé, l’agent pourrait extraire « Paris », « Tour Eiffel », et « dîner au restaurant Le Chat Noir » comme entités. Lors d’une interaction future, l’agent pourrait se souvenir de « Le Chat Noir » et proposer d’y faire une nouvelle réservation.

#### RAG structuré (Retrieval Augmented Generation)

Bien que RAG soit une technique plus large, le « RAG structuré » est mis en avant comme une technologie de mémoire puissante. Il extrait des informations denses et structurées de différentes sources (conversations, courriels, images) et les utilise pour améliorer la précision, le rappel et la rapidité des réponses. Contrairement au RAG classique qui repose uniquement sur la similarité sémantique, le RAG structuré exploite la structure inhérente des informations.

**Exemple de RAG structuré**

Plutôt que d’associer seulement des mots-clés, le RAG structuré pourrait analyser les détails d’un vol (destination, date, heure, compagnie aérienne) à partir d’un email et les stocker de manière structurée. Cela permet des requêtes précises comme « Quel vol ai-je réservé pour Paris mardi ? »

## Implémenter et stocker la mémoire

Implémenter la mémoire pour les agents IA implique un processus systématique de **gestion de la mémoire**, incluant la génération, le stockage, la récupération, l’intégration, la mise à jour, et même l’« oubli » (ou suppression) des informations. La récupération est un aspect particulièrement crucial.

### Outils de mémoire spécialisés

#### Mem0

Une façon de stocker et gérer la mémoire des agents est d’utiliser des outils spécialisés comme Mem0. Mem0 fonctionne comme une couche de mémoire persistante, permettant aux agents de rappeler des interactions pertinentes, stocker les préférences utilisateur et le contexte factuel, et apprendre des succès et échecs au fil du temps. L’idée est que des agents sans état deviennent des agents avec état.

Cela fonctionne via un **pipeline mémoire en deux phases : extraction et mise à jour**. D’abord, les messages ajoutés à un fil d’agent sont envoyés au service Mem0, qui utilise un grand modèle de langage (LLM) pour résumer l’historique de la conversation et extraire de nouveaux souvenirs. Ensuite, une phase de mise à jour pilotée par LLM détermine s’il faut ajouter, modifier ou supprimer ces souvenirs, les stockant dans un magasin de données hybride pouvant inclure des bases vectorielles, des graphes et des bases clé-valeur. Ce système supporte également divers types de mémoire et peut incorporer une mémoire graphe pour gérer les relations entre entités.

#### Cognee

Une autre approche puissante est d’utiliser **Cognee**, une mémoire sémantique open source pour agents IA qui transforme des données structurées et non structurées en graphes de connaissances interrogeables soutenus par des embeddings. Cognee propose une **architecture à double stockage** combinant la recherche par similarité vectorielle avec les relations graphiques, permettant aux agents de comprendre non seulement quelles informations sont similaires, mais aussi comment les concepts sont liés.

Il excelle dans la **récupération hybride** qui mêle similarité vectorielle, structure graphique et raisonnement par LLM – de la recherche dans des morceaux bruts à une réponse à questions consciente du graphe. Le système maintient une **mémoire vivante** qui évolue et grandit tout en restant interrogeable comme un graphe connecté, supportant à la fois le contexte de session court terme et la mémoire persistante long terme.

Le tutoriel du notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) démontre la construction de cette couche mémoire unifiée, avec des exemples pratiques d’ingestion de sources de données diverses, de visualisation du graphe de connaissances, et d’interrogation avec différentes stratégies de recherche adaptées aux besoins spécifiques des agents.

### Stocker la mémoire avec RAG

En plus des outils spécialisés comme Mem0, vous pouvez exploiter des services de recherche robustes comme **Azure AI Search en tant que backend pour stocker et récupérer des souvenirs**, en particulier pour le RAG structuré.

Cela vous permet de fonder les réponses de votre agent sur vos propres données, assurant des réponses plus pertinentes et précises. Azure AI Search peut être utilisé pour stocker des souvenirs de voyage spécifiques à l’utilisateur, des catalogues de produits ou toute autre connaissance spécifique au domaine.

Azure AI Search prend en charge des capacités comme le **RAG structuré**, qui excelle à extraire et récupérer des informations denses et structurées à partir de grands ensembles de données comme les historiques de conversations, les emails, ou même des images. Cela fournit une « précision et rappel surhumains » comparé aux approches traditionnelles de découpage de texte et d’embedding.

## Rendre les agents IA auto-améliorants

Un schéma courant pour les agents auto-améliorants consiste à introduire un **« agent de connaissance »**. Cet agent distinct observe la conversation principale entre l’utilisateur et l’agent primaire. Son rôle est de :

1. **Identifier les informations précieuses** : Déterminer si une partie de la conversation mérite d’être sauvegardée comme connaissance générale ou préférence utilisateur spécifique.

2. **Extraire et résumer** : Distiller l’apprentissage ou préférence essentiel(le) de la conversation.

3. **Stocker dans une base de connaissances** : Persister cette information extraite, souvent dans une base vectorielle, pour pouvoir la récupérer ensuite.

4. **Augmenter les futures requêtes** : Lorsqu’un utilisateur initie une nouvelle requête, l’agent de connaissance récupère les informations stockées pertinentes et les ajoute à l’invite de l’utilisateur, fournissant un contexte crucial à l’agent principal (similaire au RAG).

### Optimisations pour la mémoire

• **Gestion de la latence** : Pour ne pas ralentir les interactions utilisateur, un modèle moins coûteux et plus rapide peut être utilisé initialement pour vérifier rapidement si l’information mérite d’être stockée ou récupérée, n’appelant le processus plus complexe d’extraction/récupération que lorsque nécessaire.

• **Maintenance de la base de connaissances** : Pour une base de connaissances croissante, les informations moins souvent utilisées peuvent être déplacées en « stockage froid » pour gérer les coûts.

## Vous avez plus de questions sur la mémoire des agents ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.
## Leçon précédente

[Génie du contexte pour agents IA](../12-context-engineering/README.md)

## Leçon suivante

[Explorer Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->