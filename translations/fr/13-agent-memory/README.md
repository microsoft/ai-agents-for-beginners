<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T15:58:25+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "fr"
}
-->
# Mémoire pour les agents IA

Lorsqu'on parle des avantages uniques de la création d'agents IA, deux aspects sont principalement abordés : la capacité à utiliser des outils pour accomplir des tâches et la capacité à s'améliorer avec le temps. La mémoire est au cœur de la création d'agents capables de s'améliorer eux-mêmes et d'offrir de meilleures expériences à nos utilisateurs.

Dans cette leçon, nous examinerons ce qu'est la mémoire pour les agents IA, comment la gérer et l'utiliser au profit de nos applications.

## Introduction

Cette leçon couvrira :

• **Comprendre la mémoire des agents IA** : Ce qu'est la mémoire et pourquoi elle est essentielle pour les agents.

• **Implémenter et stocker la mémoire** : Méthodes pratiques pour ajouter des capacités de mémoire à vos agents IA, en mettant l'accent sur la mémoire à court terme et à long terme.

• **Rendre les agents IA auto-améliorants** : Comment la mémoire permet aux agents d'apprendre des interactions passées et de s'améliorer avec le temps.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

• **Différencier les différents types de mémoire des agents IA**, y compris la mémoire de travail, la mémoire à court terme et à long terme, ainsi que des formes spécialisées comme la mémoire de persona et la mémoire épisodique.

• **Implémenter et gérer la mémoire à court terme et à long terme pour les agents IA** en utilisant le framework Semantic Kernel, en exploitant des outils comme Mem0 et la mémoire Whiteboard, et en intégrant Azure AI Search.

• **Comprendre les principes des agents IA auto-améliorants** et comment des systèmes de gestion de mémoire robustes contribuent à l'apprentissage et à l'adaptation continus.

## Comprendre la mémoire des agents IA

Fondamentalement, **la mémoire des agents IA fait référence aux mécanismes qui leur permettent de conserver et de rappeler des informations**. Ces informations peuvent inclure des détails spécifiques sur une conversation, des préférences utilisateur, des actions passées ou même des schémas appris.

Sans mémoire, les applications IA sont souvent sans état, ce qui signifie que chaque interaction commence à zéro. Cela conduit à une expérience utilisateur répétitive et frustrante où l'agent "oublie" le contexte ou les préférences précédentes.

### Pourquoi la mémoire est-elle importante ?

L'intelligence d'un agent est étroitement liée à sa capacité à se souvenir et à utiliser des informations passées. La mémoire permet aux agents d'être :

• **Réfléchis** : Apprendre des actions et résultats passés.

• **Interactifs** : Maintenir le contexte au cours d'une conversation en cours.

• **Proactifs et réactifs** : Anticiper les besoins ou répondre de manière appropriée en fonction des données historiques.

• **Autonomes** : Fonctionner de manière plus indépendante en s'appuyant sur des connaissances stockées.

L'objectif de l'implémentation de la mémoire est de rendre les agents plus **fiables et compétents**.

### Types de mémoire

#### Mémoire de travail

Pensez à cela comme à une feuille de brouillon qu'un agent utilise pendant une tâche ou un processus de réflexion en cours. Elle contient les informations immédiates nécessaires pour effectuer l'étape suivante.

Pour les agents IA, la mémoire de travail capture souvent les informations les plus pertinentes d'une conversation, même si l'historique complet du chat est long ou tronqué. Elle se concentre sur l'extraction des éléments clés tels que les exigences, les propositions, les décisions et les actions.

**Exemple de mémoire de travail**

Dans un agent de réservation de voyage, la mémoire de travail pourrait capturer la demande actuelle de l'utilisateur, comme "Je veux réserver un voyage à Paris". Cette exigence spécifique est conservée dans le contexte immédiat de l'agent pour guider l'interaction en cours.

#### Mémoire à court terme

Ce type de mémoire conserve les informations pendant la durée d'une seule conversation ou session. C'est le contexte du chat actuel, permettant à l'agent de se référer aux tours précédents du dialogue.

**Exemple de mémoire à court terme**

Si un utilisateur demande : "Combien coûterait un vol pour Paris ?" puis enchaîne avec "Et pour l'hébergement là-bas ?", la mémoire à court terme garantit que l'agent sait que "là-bas" fait référence à "Paris" dans la même conversation.

#### Mémoire à long terme

Il s'agit d'informations qui persistent au-delà de plusieurs conversations ou sessions. Elle permet aux agents de se souvenir des préférences utilisateur, des interactions historiques ou des connaissances générales sur de longues périodes. Cela est essentiel pour la personnalisation.

**Exemple de mémoire à long terme**

Une mémoire à long terme pourrait conserver que "Ben aime le ski et les activités de plein air, préfère le café avec vue sur la montagne, et souhaite éviter les pistes de ski avancées en raison d'une blessure passée". Ces informations, apprises lors d'interactions précédentes, influencent les recommandations lors de futures sessions de planification de voyage, les rendant hautement personnalisées.

#### Mémoire de persona

Ce type de mémoire spécialisé aide un agent à développer une "personnalité" ou un "persona" cohérent. Elle permet à l'agent de se souvenir de détails sur lui-même ou sur son rôle prévu, rendant les interactions plus fluides et ciblées.

**Exemple de mémoire de persona**

Si l'agent de voyage est conçu pour être un "expert en planification de ski", la mémoire de persona pourrait renforcer ce rôle, influençant ses réponses pour qu'elles s'alignent sur le ton et les connaissances d'un expert.

#### Mémoire épisodique/de workflow

Cette mémoire stocke la séquence des étapes qu'un agent suit lors d'une tâche complexe, y compris les succès et les échecs. C'est comme se souvenir de "épisodes" spécifiques ou d'expériences passées pour en tirer des leçons.

**Exemple de mémoire épisodique**

Si l'agent a tenté de réserver un vol spécifique mais a échoué en raison d'une indisponibilité, la mémoire épisodique pourrait enregistrer cet échec, permettant à l'agent d'essayer des vols alternatifs ou d'informer l'utilisateur du problème de manière plus éclairée lors d'une tentative ultérieure.

#### Mémoire d'entité

Cela implique d'extraire et de se souvenir d'entités spécifiques (comme des personnes, des lieux ou des objets) et d'événements issus des conversations. Cela permet à l'agent de construire une compréhension structurée des éléments clés discutés.

**Exemple de mémoire d'entité**

À partir d'une conversation sur un voyage passé, l'agent pourrait extraire "Paris", "Tour Eiffel" et "dîner au restaurant Le Chat Noir" comme entités. Lors d'une interaction future, l'agent pourrait se souvenir de "Le Chat Noir" et proposer de faire une nouvelle réservation là-bas.

#### RAG structuré (Retrieval Augmented Generation)

Bien que le RAG soit une technique plus large, le "RAG structuré" est mis en avant comme une technologie de mémoire puissante. Il extrait des informations denses et structurées de diverses sources (conversations, e-mails, images) et les utilise pour améliorer la précision, le rappel et la rapidité des réponses. Contrairement au RAG classique qui repose uniquement sur la similarité sémantique, le RAG structuré travaille avec la structure inhérente des informations.

**Exemple de RAG structuré**

Au lieu de simplement faire correspondre des mots-clés, le RAG structuré pourrait analyser les détails d'un vol (destination, date, heure, compagnie aérienne) à partir d'un e-mail et les stocker de manière structurée. Cela permet des requêtes précises comme "Quel vol ai-je réservé pour Paris mardi ?"

## Implémenter et stocker la mémoire

L'implémentation de la mémoire pour les agents IA implique un processus systématique de **gestion de la mémoire**, qui inclut la génération, le stockage, la récupération, l'intégration, la mise à jour et même l'"oubli" (ou la suppression) des informations. La récupération est un aspect particulièrement crucial.

### Outils spécialisés de mémoire

Une façon de stocker et de gérer la mémoire des agents est d'utiliser des outils spécialisés comme Mem0. Mem0 fonctionne comme une couche de mémoire persistante, permettant aux agents de rappeler des interactions pertinentes, de stocker des préférences utilisateur et un contexte factuel, et d'apprendre des succès et des échecs au fil du temps. L'idée ici est que les agents sans état deviennent des agents avec état.

Il fonctionne via un **pipeline de mémoire en deux phases : extraction et mise à jour**. Tout d'abord, les messages ajoutés au fil de l'agent sont envoyés au service Mem0, qui utilise un modèle de langage étendu (LLM) pour résumer l'historique des conversations et extraire de nouvelles mémoires. Ensuite, une phase de mise à jour pilotée par LLM détermine s'il faut ajouter, modifier ou supprimer ces mémoires, en les stockant dans un système de données hybride qui peut inclure des bases de données vectorielles, graphiques et clé-valeur. Ce système prend également en charge divers types de mémoire et peut intégrer une mémoire graphique pour gérer les relations entre les entités.

### Stocker la mémoire avec RAG

Au-delà des outils spécialisés comme Mem0, vous pouvez utiliser des services de recherche robustes comme **Azure AI Search comme backend pour stocker et récupérer des mémoires**, en particulier pour le RAG structuré.

Cela permet de baser les réponses de votre agent sur vos propres données, garantissant des réponses plus pertinentes et précises. Azure AI Search peut être utilisé pour stocker des mémoires de voyage spécifiques à l'utilisateur, des catalogues de produits ou tout autre domaine de connaissances spécifiques.

Azure AI Search prend en charge des fonctionnalités comme **RAG structuré**, qui excelle dans l'extraction et la récupération d'informations denses et structurées à partir de grands ensembles de données comme les historiques de conversation, les e-mails ou même les images. Cela offre une "précision et un rappel surhumains" par rapport aux approches classiques de découpage de texte et d'intégration.

## Rendre les agents IA auto-améliorants

Un modèle courant pour les agents auto-améliorants consiste à introduire un **"agent de connaissance"**. Cet agent distinct observe la conversation principale entre l'utilisateur et l'agent principal. Son rôle est de :

1. **Identifier les informations précieuses** : Déterminer si une partie de la conversation mérite d'être sauvegardée comme connaissance générale ou préférence utilisateur spécifique.

2. **Extraire et résumer** : Distiller l'apprentissage ou la préférence essentielle de la conversation.

3. **Stocker dans une base de connaissances** : Conserver ces informations extraites, souvent dans une base de données vectorielle, pour qu'elles puissent être récupérées plus tard.

4. **Augmenter les requêtes futures** : Lorsque l'utilisateur initie une nouvelle requête, l'agent de connaissance récupère les informations stockées pertinentes et les ajoute à l'invite de l'utilisateur, fournissant un contexte crucial à l'agent principal (similaire au RAG).

### Optimisations pour la mémoire

• **Gestion de la latence** : Pour éviter de ralentir les interactions utilisateur, un modèle moins coûteux et plus rapide peut être utilisé initialement pour vérifier rapidement si une information mérite d'être stockée ou récupérée, en n'invoquant le processus d'extraction/récupération complexe que si nécessaire.

• **Maintenance de la base de connaissances** : Pour une base de connaissances en croissance, les informations moins fréquemment utilisées peuvent être déplacées vers un "stockage froid" pour gérer les coûts.

## Vous avez d'autres questions sur l'ingénierie du contexte ?

Rejoignez le [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister à des heures de bureau et obtenir des réponses à vos questions sur les agents IA.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.