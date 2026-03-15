# Mémoire pour les agents IA  
[![Agent Memory](../../../translated_images/fr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Lorsqu'on parle des avantages uniques de la création d'agents IA, deux aspects sont principalement abordés : la capacité à appeler des outils pour accomplir des tâches et la capacité à s'améliorer au fil du temps. La mémoire est à la base de la création d’un agent auto-améliorant capable de créer de meilleures expériences pour nos utilisateurs.

Dans cette leçon, nous verrons ce qu’est la mémoire pour les agents IA, comment la gérer et l’utiliser au bénéfice de nos applications.

## Introduction

Cette leçon couvrira :

• **Comprendre la mémoire des agents IA** : Ce qu’est la mémoire et pourquoi elle est essentielle aux agents.

• **Mettre en œuvre et stocker la mémoire** : Méthodes pratiques pour ajouter des capacités mémorielles à vos agents IA, en mettant l’accent sur la mémoire à court terme et à long terme.

• **Rendre les agents IA auto-améliorants** : Comment la mémoire permet aux agents d’apprendre de leurs interactions passées et de s’améliorer avec le temps.

## Implémentations disponibles

Cette leçon comprend deux tutoriels complets sous forme de notebooks :

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)** : Implémente la mémoire en utilisant Mem0 et Azure AI Search avec Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)** : Implémente une mémoire structurée avec Cognee, construisant automatiquement un graphe de connaissances basé sur des embeddings, visualisant le graphe et un système de recherche intelligent

## Objectifs pédagogiques

Après avoir terminé cette leçon, vous saurez comment :

• **Différencier les divers types de mémoire d’un agent IA**, y compris la mémoire de travail, à court terme, à long terme, ainsi que des formes spécialisées comme la mémoire de persona et épisodique.

• **Implémenter et gérer la mémoire à court et long terme chez les agents IA** avec Microsoft Agent Framework, en tirant parti d’outils tels que Mem0, Cognee, Whiteboard memory et l’intégration avec Azure AI Search.

• **Comprendre les principes derrière les agents IA auto-améliorants** et comment des systèmes robustes de gestion de mémoire contribuent à un apprentissage et une adaptation continus.

## Comprendre la mémoire des agents IA

Au fond, **la mémoire pour les agents IA désigne les mécanismes qui leur permettent de conserver et de rappeler des informations**. Ces informations peuvent être des détails spécifiques d’une conversation, des préférences utilisateur, des actions passées ou même des schémas appris.

Sans mémoire, les applications IA sont souvent sans état, ce qui signifie que chaque interaction commence de zéro. Cela conduit à une expérience utilisateur répétitive et frustrante où l’agent « oublie » le contexte ou les préférences précédentes.

### Pourquoi la mémoire est-elle importante ?

L’intelligence d’un agent est profondément liée à sa capacité à se souvenir et à utiliser les informations passées. La mémoire permet aux agents d’être :

• **Réfléchis** : Apprendre des actions et résultats passés.

• **Interactifs** : Maintenir le contexte d’une conversation en cours.

• **Proactifs et réactifs** : Anticiper les besoins ou répondre de manière appropriée basé sur les données historiques.

• **Autonomes** : Opérer plus indépendamment en s’appuyant sur des connaissances stockées.

Le but de l’implémentation de la mémoire est de rendre les agents plus **fiables et capables**.

### Types de mémoire

#### Mémoire de travail

Considérez cela comme un brouillon que l’agent utilise pendant une tâche ou un processus de pensée en cours. Elle contient les informations immédiates nécessaires pour calculer la prochaine étape.

Pour les agents IA, la mémoire de travail capture souvent les informations les plus pertinentes d’une conversation, même si l’historique complet est long ou tronqué. Elle se concentre sur l’extraction d’éléments clés tels que besoins, propositions, décisions et actions.

**Exemple de mémoire de travail**

Dans un agent de réservation de voyages, la mémoire de travail pourrait contenir la demande actuelle de l’utilisateur, comme « Je veux réserver un voyage à Paris ». Cette exigence spécifique est retenue dans le contexte immédiat de l’agent pour guider l’interaction en cours.

#### Mémoire à court terme

Ce type de mémoire conserve les informations pendant la durée d’une seule conversation ou session. C’est le contexte du chat actuel, permettant à l’agent de revenir sur les tours précédents du dialogue.

**Exemple de mémoire à court terme**

Si un utilisateur demande « Combien coûte un vol pour Paris ? » puis enchaîne avec « Et pour l’hébergement là-bas ? », la mémoire courte garantit que l’agent sait que « là-bas » fait référence à « Paris » dans la même conversation.

#### Mémoire à long terme

Ce sont des informations qui persistent sur plusieurs conversations ou sessions. Elle permet aux agents de se souvenir des préférences utilisateur, des interactions historiques ou d’une connaissance générale sur de longues périodes. C’est important pour la personnalisation.

**Exemple de mémoire à long terme**

Une mémoire à long terme pourrait stocker que « Ben aime le ski et les activités de plein air, apprécie le café avec vue sur la montagne et veut éviter les pistes avancées en raison d’une blessure passée ». Cette information, apprise lors d’interactions précédentes, influence les recommandations lors de futures sessions de planification de voyage, les rendant très personnalisées.

#### Mémoire de persona

Ce type spécialisé aide un agent à développer une « personnalité » ou « persona » cohérente. Elle permet à l’agent de se souvenir de détails sur lui-même ou son rôle prévu, rendant les interactions plus fluides et ciblées.

**Exemple de mémoire de persona**  
Si l’agent de voyage est conçu comme un « expert planificateur de ski », la mémoire de persona pourrait renforcer ce rôle, influençant ses réponses pour qu’elles correspondent au ton et aux connaissances d’un expert.

#### Mémoire de workflow/épisodique

Cette mémoire stocke la séquence d’étapes qu’un agent suit lors d’une tâche complexe, incluant succès et échecs. C’est comme se souvenir d’« épisodes » spécifiques ou d’expériences passées pour en tirer des leçons.

**Exemple de mémoire épisodique**

Si l’agent a tenté de réserver un vol spécifique mais a échoué à cause d’une indisponibilité, la mémoire épisodique peut enregistrer cet échec, permettant à l’agent d’essayer des vols alternatifs ou d’informer l’utilisateur du problème de manière plus informée lors d’une tentative ultérieure.

#### Mémoire d’entité

Elle consiste à extraire et retenir des entités spécifiques (comme des personnes, lieux ou objets) et des événements provenant des conversations. Cela permet à l’agent de construire une compréhension structurée des éléments clés abordés.

**Exemple de mémoire d’entité**

Dans une conversation sur un voyage passé, l’agent pourrait extraire « Paris », « Tour Eiffel » et « dîner au restaurant Le Chat Noir » comme entités. Lors d’une interaction future, l’agent pourrait se souvenir de « Le Chat Noir » et proposer de faire une nouvelle réservation.

#### RAG structuré (Retrieval Augmented Generation)

Bien que RAG soit une technique plus générale, le « RAG structuré » est présenté comme une technologie mémoire puissante. Il extrait des informations denses et structurées de diverses sources (conversations, emails, images) et les utilise pour améliorer la précision, le rappel et la rapidité des réponses. Contrairement au RAG classique qui repose uniquement sur la similarité sémantique, le RAG structuré exploite la structure inhérente des informations.

**Exemple de RAG structuré**

Au lieu de ne faire que correspondre des mots-clés, le RAG structuré peut analyser les détails d’un vol (destination, date, heure, compagnie aérienne) à partir d’un email et les stocker de façon structurée. Cela permet des requêtes précises comme « Quel vol ai-je réservé pour Paris mardi ? »

## Implémenter et stocker la mémoire

Implémenter la mémoire pour des agents IA implique un processus systématique de **gestion mémoire**, incluant la génération, le stockage, la récupération, l’intégration, la mise à jour et même l’« oubli » (ou la suppression) d’informations. La récupération est un aspect particulièrement critique.

### Outils de mémoire spécialisés

#### Mem0

Une manière de stocker et gérer la mémoire des agents est d’utiliser des outils spécialisés comme Mem0. Mem0 fonctionne comme une couche de mémoire persistante, permettant aux agents de se souvenir des interactions pertinentes, de stocker préférences utilisateurs et contexte factuel, et d’apprendre des succès et échecs au fil du temps. L’idée est que les agents sans état deviennent des agents avec état.

Il fonctionne via un **pipeline mémoire en deux phases : extraction et mise à jour**. D’abord, les messages ajoutés à un fil d’agent sont envoyés au service Mem0, qui utilise un grand modèle de langage (LLM) pour résumer l’historique de conversation et extraire de nouvelles mémoires. Ensuite, une phase de mise à jour pilotée par LLM détermine s’il faut ajouter, modifier ou supprimer ces mémoires, les stockant dans un magasin de données hybride incluant bases vectorielles, graphes et bases clé-valeur. Ce système supporte aussi divers types de mémoire et peut incorporer une mémoire graphe pour gérer les relations entre entités.

#### Cognee

Une autre approche puissante est l’utilisation de **Cognee**, une mémoire sémantique open-source pour agents IA qui transforme données structurées et non structurées en graphes de connaissances interrogeables soutenus par des embeddings. Cognee fournit une **architecture à double stockage** combinant recherche vectorielle de similarité avec relations de graphe, permettant aux agents de comprendre non seulement ce qui est similaire mais comment les concepts sont reliés.

Il excelle dans la **récupération hybride** qui mêle similarité vectorielle, structure de graphe et raisonnement LLM – de la recherche brute dans des morceaux d’information au questionnement prenant en compte le graphe. Le système maintient une **mémoire vivante** qui évolue et grandit tout en restant interrogeable comme un graphe connecté, supportant à la fois le contexte de session court terme et la mémoire persistante à long terme.

Le tutoriel notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) montre comment construire cette couche mémoire unifiée, avec des exemples pratiques d’ingestion de sources de données diverses, de visualisation du graphe de connaissances, et d’interrogations avec différentes stratégies de recherche adaptées aux besoins spécifiques des agents.

### Stockage de la mémoire avec RAG

Au-delà d’outils spécialisés comme mem0 , vous pouvez exploiter des services de recherche robustes tels que **Azure AI Search comme backend pour stocker et récupérer des mémoires**, particulièrement pour le RAG structuré.

Cela vous permet d’appuyer les réponses de votre agent sur vos propres données, garantissant des réponses plus pertinentes et précises. Azure AI Search peut être utilisé pour stocker les souvenirs de voyages d’un utilisateur, des catalogues de produits ou toute autre connaissance spécifique à un domaine.

Azure AI Search supporte des fonctionnalités comme le **RAG structuré**, qui excelle à extraire et récupérer des informations denses et structurées de grands ensembles de données comme historiques de conversation, emails ou même images. Cela offre une « précision et un rappel surhumains » comparé aux approches classiques de découpage de texte et d’embeddings.

## Rendre les agents IA auto-améliorants

Un schéma courant pour les agents auto-améliorants consiste à introduire un **« agent de connaissance »**. Cet agent séparé observe la conversation principale entre l’utilisateur et l’agent principal. Son rôle est de :

1. **Identifier les informations précieuses** : Déterminer si une partie de la conversation mérite d’être sauvegardée comme connaissance générale ou préférence utilisateur spécifique.

2. **Extraire et résumer** : Dégager l’apprentissage ou la préférence essentielle de la conversation.

3. **Stocker dans une base de connaissances** : Persister cette information extraite, souvent dans une base vectorielle, pour pouvoir la récupérer ultérieurement.

4. **Augmenter les futures requêtes** : Lorsqu’un utilisateur lance une nouvelle requête, l’agent de connaissance récupère les informations pertinentes stockées et les ajoute dans l’invite de l’utilisateur, fournissant un contexte crucial à l’agent principal (similaire au RAG).

### Optimisations pour la mémoire

• **Gestion de la latence** : Pour ne pas ralentir les interactions utilisateur, un modèle plus simple et rapide peut être utilisé initialement pour vérifier rapidement si l’information vaut la peine d’être stockée ou récupérée, ne faisant appel au processus plus complexe d’extraction/récupération que lorsque nécessaire.

• **Maintenance de la base de connaissances** : Pour une base de connaissances en croissance, les informations moins fréquemment utilisées peuvent être déplacées en « stockage froid » pour gérer les coûts.

## Vous avez plus de questions sur la mémoire des agents ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->