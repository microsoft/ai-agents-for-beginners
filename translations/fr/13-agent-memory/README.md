# Mémoire pour les agents IA  
[![Agent Memory](../../../translated_images/fr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Lorsque l'on parle des avantages uniques de la création d'agents IA, deux choses sont principalement abordées : la capacité à utiliser des outils pour accomplir des tâches et la capacité à s'améliorer au fil du temps. La mémoire est à la base de la création d’agents auto-améliorants capables d’offrir de meilleures expériences à nos utilisateurs.

Dans cette leçon, nous examinerons ce qu’est la mémoire pour les agents IA et comment nous pouvons la gérer et l’utiliser au bénéfice de nos applications.

## Introduction

Cette leçon couvrira :

• **Comprendre la mémoire des agents IA** : Qu’est-ce que la mémoire et pourquoi elle est essentielle pour les agents.

• **Implémenter et stocker la mémoire** : Méthodes pratiques pour ajouter des capacités de mémoire à vos agents IA, en mettant l’accent sur la mémoire à court terme et à long terme.

• **Rendre les agents IA auto-améliorants** : Comment la mémoire permet aux agents d’apprendre des interactions passées et de s’améliorer au fil du temps.

## Implémentations disponibles

Cette leçon comprend deux tutoriels complets au format notebook :

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)** : Implémente la mémoire en utilisant Mem0 et Azure AI Search avec Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)** : Implémente la mémoire structurée avec Cognee, construisant automatiquement un graphe de connaissances soutenu par des embeddings, visualisant le graphe et réalisant une récupération intelligente

## Objectifs d’apprentissage

Après avoir terminé cette leçon, vous saurez :

• **Différencier entre les différents types de mémoire des agents IA**, incluant la mémoire de travail, la mémoire à court terme et à long terme, ainsi que des formes spécialisées comme la mémoire de persona et la mémoire épisodique.

• **Implémenter et gérer la mémoire à court terme et à long terme pour les agents IA** en utilisant Microsoft Agent Framework, en tirant parti d’outils comme Mem0, Cognee, la mémoire Whiteboard et l’intégration avec Azure AI Search.

• **Comprendre les principes derrière les agents IA auto-améliorants** et comment des systèmes de gestion de mémoire robustes contribuent à l’apprentissage continu et à l’adaptation.

## Comprendre la mémoire des agents IA

Au fond, **la mémoire pour les agents IA désigne les mécanismes qui leur permettent de retenir et de rappeler des informations**. Ces informations peuvent être des détails spécifiques sur une conversation, les préférences d’un utilisateur, des actions passées, ou même des schémas appris.

Sans mémoire, les applications IA sont souvent sans état, ce qui signifie que chaque interaction recommence à zéro. Cela conduit à une expérience utilisateur répétitive et frustrante où l’agent « oublie » le contexte ou les préférences précédentes.

### Pourquoi la mémoire est-elle importante ?

L’intelligence d’un agent est profondément liée à sa capacité à rappeler et utiliser des informations passées. La mémoire permet aux agents d’être :

• **Réfléchis** : Apprendre des actions passées et de leurs résultats.

• **Interatifs** : Maintenir le contexte au cours d’une conversation en cours.

• **Proactifs et réactifs** : Anticiper les besoins ou répondre de manière appropriée en se basant sur des données historiques.

• **Autonomes** : Fonctionner plus indépendamment en s’appuyant sur des connaissances stockées.

L’objectif de l’implémentation de la mémoire est de rendre les agents plus **fiables et performants**.

### Types de mémoire

#### Mémoire de travail

Pensez à cela comme une feuille de brouillon qu’un agent utilise pendant une tâche unique et en cours ou un processus de réflexion. Elle contient les informations immédiates nécessaires pour calculer l’étape suivante.

Pour les agents IA, la mémoire de travail capture souvent les informations les plus pertinentes d’une conversation, même si l’historique complet du chat est long ou tronqué. Elle se concentre sur l’extraction d’éléments clés comme les exigences, les propositions, les décisions et les actions.

**Exemple de mémoire de travail**

Dans un agent de réservation de voyage, la mémoire de travail pourrait capturer la demande actuelle de l’utilisateur, par exemple « Je veux réserver un voyage à Paris ». Cette exigence spécifique est maintenue dans le contexte immédiat de l’agent pour guider l’interaction en cours.

#### Mémoire à court terme

Ce type de mémoire conserve l’information pendant une seule conversation ou session. C’est le contexte du chat actuel, permettant à l’agent de se référer aux tours précédents du dialogue.

Dans les exemples du SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), cela correspond à `AgentSession`, créé avec `agent.create_session()`. La session est la mémoire à court terme intégrée du framework : elle garde le contexte de la conversation disponible tant que la session est réutilisée, mais ce contexte n’est pas conservé lorsque la session se termine ou que l’application redémarre. Utilisez la mémoire à long terme pour les faits et préférences devant survivre aux sessions, typiquement via une base de données, un index vectoriel, ou un autre stockage persistant.

**Exemple de mémoire à court terme**

Si un utilisateur demande « Combien coûterait un vol pour Paris ? » puis enchaîne avec « Qu’en est-il de l’hébergement là-bas ? », la mémoire à court terme permet à l’agent de savoir que « là-bas » fait référence à « Paris » dans la même conversation.

#### Mémoire à long terme

Il s’agit d’informations qui persistent sur plusieurs conversations ou sessions. Elle permet aux agents de se souvenir des préférences utilisateur, des interactions historiques ou de connaissances générales sur de longues périodes. Cette mémoire est importante pour la personnalisation.

**Exemple de mémoire à long terme**

Une mémoire à long terme pourrait stocker que « Ben aime le ski et les activités en plein air, préfère le café avec vue sur la montagne, et veut éviter les pistes de ski avancées à cause d’une blessure passée ». Cette information, apprise lors d’interactions précédentes, influence les recommandations lors de futures sessions de planification de voyage, les rendant très personnalisées.

#### Mémoire de persona

Ce type de mémoire spécialisé aide un agent à développer une « personnalité » ou un « persona » cohérent. Il permet à l’agent de se souvenir de détails sur lui-même ou son rôle prévu, rendant les interactions plus fluides et ciblées.

**Exemple de mémoire de persona**  
Si l’agent de voyage est conçu pour être un « expert en planification de ski », la mémoire de persona pourrait renforcer ce rôle, influençant ses réponses pour s’aligner sur le ton et les connaissances d’un expert.

#### Mémoire de workflow/épisodique

Cette mémoire stocke la séquence d’étapes qu’un agent suit pendant une tâche complexe, incluant les succès et les échecs. C’est comme se rappeler d’« épisodes » ou d’expériences passées pour en tirer des enseignements.

**Exemple de mémoire épisodique**

Si l’agent a tenté de réserver un vol spécifique mais a échoué en raison d’une indisponibilité, la mémoire épisodique pourrait enregistrer cet échec, permettant à l’agent d’essayer des vols alternatifs ou d’informer l’utilisateur du problème de manière plus avisée lors d’une tentative ultérieure.

#### Mémoire d’entités

Cela consiste à extraire et retenir des entités spécifiques (comme des personnes, lieux ou objets) et des événements à partir des conversations. Cela permet à l’agent de construire une compréhension structurée des éléments clés discutés.

**Exemple de mémoire d’entités**

Dans une conversation à propos d’un voyage passé, l’agent pourrait extraire « Paris », « Tour Eiffel » et « dîner au restaurant Le Chat Noir » comme entités. Lors d’une interaction future, l’agent pourrait se souvenir de « Le Chat Noir » et proposer d’y faire une nouvelle réservation.

#### RAG structuré (Retrieval Augmented Generation structuré)

Bien que RAG soit une technique plus large, le « RAG structuré » est mis en avant comme une technologie puissante de mémoire. Il extrait des informations denses et structurées à partir de diverses sources (conversations, emails, images) et les utilise pour améliorer la précision, le rappel et la rapidité des réponses. Contrairement au RAG classique qui repose uniquement sur la similarité sémantique, le RAG structuré exploite la structure inhérente des informations.

**Exemple de RAG structuré**

Au lieu de simplement faire correspondre des mots-clés, le RAG structuré pourrait analyser les détails d’un vol (destination, date, heure, compagnie) à partir d’un email et les stocker de manière structurée. Cela permet des requêtes précises comme « Quel vol ai-je réservé pour Paris mardi ? »

## Implémenter et stocker la mémoire

Implémenter la mémoire pour les agents IA implique un processus systématique de **gestion de la mémoire**, qui comprend la génération, le stockage, la récupération, l’intégration, la mise à jour et même l’« oubli » (ou suppression) d’informations. La récupération est un aspect particulièrement crucial.

### Outils mémoire spécialisés

#### Mem0

Une façon de stocker et gérer la mémoire des agents consiste à utiliser des outils spécialisés comme Mem0. Mem0 fonctionne comme une couche de mémoire persistante, permettant aux agents de rappeler des interactions pertinentes, stocker les préférences utilisateur et le contexte factuel, et apprendre des succès et des échecs au fil du temps. L’idée est que des agents sans état deviennent des agents avec état.

Cela fonctionne via un **pipeline mémoire en deux phases : extraction et mise à jour**. D’abord, les messages ajoutés au fil d’un agent sont envoyés au service Mem0, qui utilise un modèle de langue large (LLM) pour résumer l’historique de la conversation et extraire de nouveaux souvenirs. Ensuite, une phase de mise à jour pilotée par LLM détermine s’il faut ajouter, modifier ou supprimer ces souvenirs, les stockant dans un magasin de données hybride pouvant inclure des bases vectorielles, des graphes et des bases clé-valeur. Ce système supporte aussi plusieurs types de mémoire et peut incorporer une mémoire graphique pour gérer les relations entre entités.

#### Cognee

Une autre approche puissante est d’utiliser **Cognee**, une mémoire sémantique open source pour agents IA qui transforme données structurées et non structurées en graphes de connaissances interrogeables soutenus par des embeddings. Cognee fournit une **architecture double magasin** combinant recherche de similarité vectorielle et relations graphiques, permettant aux agents de comprendre non seulement quelles informations sont similaires, mais aussi comment les concepts se relient entre eux.

Il excelle dans la **récupération hybride** qui mêle similarité vectorielle, structure graphique et raisonnement LLM — depuis la recherche brute dans les morceaux jusqu’à la réponse aux questions consciente du graphe. Le système maintient une **mémoire vivante** qui évolue et grossit tout en restant interrogeable comme un graphe connecté, supportant à la fois le contexte de session à court terme et la mémoire persistante à long terme.

Le tutoriel notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) montre comment construire cette couche mémoire unifiée, avec des exemples pratiques d’ingestion de sources de données diverses, de visualisation du graphe de connaissances, et de requêtes avec différentes stratégies de recherche adaptées aux besoins spécifiques des agents.

### Stocker la mémoire avec RAG

Au-delà d’outils mémoire spécialisés comme mem0, vous pouvez exploiter des services de recherche robustes comme **Azure AI Search comme backend pour stocker et récupérer les mémoires**, surtout pour le RAG structuré.

Cela vous permet d’ancrer les réponses de votre agent avec vos propres données, assurant des réponses plus pertinentes et précises. Azure AI Search peut être utilisé pour stocker les mémoires spécifiques aux voyages utilisateur, les catalogues produits, ou tout autre domaine de connaissance spécifique.

Azure AI Search prend en charge des capacités comme le **RAG structuré**, qui excelle à extraire et récupérer des informations denses, structurées à partir de grands ensembles de données comme l’historique de conversations, les emails, voire les images. Cela offre une « précision et un rappel surhumains » comparé aux approches classiques de découpage de texte et d’embeddings.

## Rendre les agents IA auto-améliorants

Un modèle courant pour les agents auto-améliorants consiste à introduire un **« agent de connaissance »**. Cet agent distinct observe la conversation principale entre l’utilisateur et l’agent principal. Son rôle est de :

1. **Identifier les informations précieuses** : Déterminer si une partie de la conversation mérite d’être sauvegardée comme savoir général ou préférence spécifique utilisateur.

2. **Extraire et résumer** : Dégager l’apprentissage ou la préférence essentielle issue de la conversation.

3. **Stocker dans une base de connaissances** : Persister cette information extraite, souvent dans une base vectorielle, pour pouvoir la récupérer ultérieurement.

4. **Augmenter les requêtes futures** : Lorsque l’utilisateur initie une nouvelle requête, l’agent de connaissance récupère les informations stockées pertinentes et les ajoute à la consigne de l’utilisateur, fournissant un contexte crucial à l’agent principal (similaire au RAG).

### Optimisations pour la mémoire

• **Gestion de la latence** : Pour éviter de ralentir les interactions utilisateur, un modèle moins coûteux et plus rapide peut être utilisé initialement pour vérifier rapidement si une information vaut la peine d’être stockée ou récupérée, activant seulement le processus d’extraction/récupération plus complexe si nécessaire.

• **Maintenance de la base de connaissances** : Pour une base de connaissances qui grandit, les informations moins utilisées peuvent être déplacées vers un « stockage froid » pour gérer les coûts.

## Vous avez d’autres questions sur la mémoire des agents ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->