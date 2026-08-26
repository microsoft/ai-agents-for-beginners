# Utilisation des Protocoles Agentiques (MCP, A2A et NLWeb)

[![Protocoles Agentiques](../../../translated_images/fr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

À mesure que l'utilisation des agents IA se développe, le besoin de protocoles garantissant la normalisation, la sécurité et le soutien à l'innovation ouverte augmente également. Dans cette leçon, nous aborderons 3 protocoles visant à répondre à ce besoin - Model Context Protocol (MCP), Agent to Agent (A2A) et Natural Language Web (NLWeb).

## Introduction

Dans cette leçon, nous couvrirons :

• Comment **MCP** permet aux agents IA d’accéder à des outils et des données externes pour accomplir les tâches utilisateur.

• Comment **A2A** facilite la communication et la collaboration entre différents agents IA.

• Comment **NLWeb** apporte des interfaces en langage naturel à n'importe quel site web, permettant aux agents IA de découvrir et d'interagir avec le contenu.

## Objectifs d’apprentissage

• **Identifier** le but principal et les avantages du MCP, du A2A et du NLWeb dans le contexte des agents IA.

• **Expliquer** comment chaque protocole facilite la communication et l’interaction entre les LLM, les outils et d’autres agents.

• **Reconnaître** les rôles distincts que chaque protocole joue dans la construction de systèmes agentiques complexes.

## Model Context Protocol

Le **Model Context Protocol (MCP)** est une norme ouverte qui offre une manière standardisée aux applications de fournir du contexte et des outils aux LLM. Cela permet un "adapteur universel" à différentes sources de données et outils auxquels les agents IA peuvent se connecter de manière cohérente.

Regardons les composants du MCP, les avantages par rapport à l’utilisation directe d’API, et un exemple de comment des agents IA pourraient utiliser un serveur MCP.

### Composants principaux du MCP

Le MCP fonctionne selon une **architecture client-serveur** et les composants principaux sont :

• Les **Hôtes** sont des applications LLM (par exemple un éditeur de code comme VSCode) qui initient les connexions à un serveur MCP.

• Les **Clients** sont des composants au sein de l’application hôte qui maintiennent des connexions individuelles avec les serveurs.

• Les **Serveurs** sont des programmes légers qui exposent des capacités spécifiques.

Le protocole inclut trois primitives principales qui sont les capacités d’un serveur MCP :

• **Outils** : Ce sont des actions ou fonctions discrètes qu’un agent IA peut appeler pour effectuer une action. Par exemple, un service météo pourrait exposer un outil « obtenir la météo », ou un serveur e-commerce pourrait proposer un outil « acheter un produit ». Les serveurs MCP annoncent le nom, la description et le schéma d’entrée/sortie de chaque outil dans leur liste de capacités.

• **Ressources** : Ce sont des éléments de données ou documents en lecture seule qu’un serveur MCP peut fournir, et les clients peuvent les récupérer à la demande. Exemples : contenus de fichiers, enregistrements de base de données, fichiers journaux. Les ressources peuvent être du texte (comme du code ou JSON) ou du binaire (images ou PDF).

• **Prompts** : Ce sont des modèles prédéfinis qui fournissent des suggestions de prompts, permettant des flux de travail plus complexes.

### Avantages du MCP

MCP offre des avantages significatifs pour les agents IA :

• **Découverte dynamique d’outils** : Les agents peuvent recevoir dynamiquement une liste des outils disponibles d’un serveur avec des descriptions de leurs fonctions. Cela contraste avec les API traditionnelles qui exigent souvent une programmation statique pour les intégrations, ce qui nécessite une mise à jour du code à chaque modification d’API. MCP propose une approche « intégrer une fois », menant à une plus grande adaptabilité.

• **Interopérabilité entre LLM** : MCP fonctionne avec différents LLM, offrant la flexibilité de changer de modèle principal pour évaluer des performances améliorées.

• **Sécurité standardisée** : MCP inclut une méthode d’authentification standard, améliorant la scalabilité lors de l’ajout d’accès à d'autres serveurs MCP. Ceci est plus simple que la gestion de clés et types d’authentification variés pour différentes API traditionnelles.

### Exemple MCP

![Diagramme MCP](../../../translated_images/fr/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginez qu’un utilisateur souhaite réserver un vol avec un assistant IA alimenté par MCP.

1. **Connexion** : L’assistant IA (le client MCP) se connecte à un serveur MCP fourni par une compagnie aérienne.

2. **Découverte des outils** : Le client demande au serveur MCP de la compagnie aérienne : « Quels outils avez-vous disponibles ? » Le serveur répond avec des outils comme « rechercher des vols » et « réserver des vols ».

3. **Invocation de l’outil** : Vous demandez alors à l’assistant IA : « Veuillez chercher un vol de Portland à Honolulu ». L’assistant IA, utilisant son LLM, identifie qu’il doit appeler l’outil « rechercher des vols » et transmet les paramètres pertinents (origine, destination) au serveur MCP.

4. **Exécution et réponse** : Le serveur MCP, agissant comme un intermédiaire, effectue l’appel réel à l’API interne de réservation de la compagnie. Il reçoit ensuite les informations du vol (par ex., données JSON) et les renvoie à l’assistant IA.

5. **Interaction supplémentaire** : L’assistant IA présente les options de vol. Une fois le vol sélectionné, il peut invoquer l’outil « réserver un vol » sur le même serveur MCP, finalisant la réservation.

## Protocole Agent-à-Agent (A2A)

Alors que le MCP se concentre sur la connexion des LLM aux outils, le **protocole Agent-à-Agent (A2A)** va plus loin en permettant la communication et la collaboration entre différents agents IA. A2A connecte des agents IA à travers différentes organisations, environnements et technologies pour accomplir une tâche partagée.

Nous examinerons les composants et avantages du A2A, ainsi qu'un exemple d'application dans notre scénario de voyage.

### Composants principaux du A2A

A2A met l'accent sur permettre aux agents de communiquer et de collaborer pour accomplir une sous-tâche utilisateur. Chaque composant du protocole contribue à cela :

#### Fiche de l’Agent

Tout comme un serveur MCP partage une liste d'outils, une fiche d’agent contient :
- Le nom de l'agent.
- Une **description des tâches générales** qu’il accomplit.
- Une **liste des compétences spécifiques** avec des descriptions pour aider les autres agents (ou même les utilisateurs humains) à comprendre quand et pourquoi ils voudraient appeler cet agent.
- L'**URL de point de terminaison actuelle** de l'agent.
- La **version** et les **capacités** de l'agent, comme la diffusion en continu des réponses et les notifications push.

#### Exécuteur d’Agent

L’Exécuteur d’Agent est responsable de **transmettre le contexte de la discussion utilisateur à l’agent distant** ; l'agent distant en a besoin pour comprendre la tâche à accomplir. Dans un serveur A2A, un agent utilise son propre Large Language Model (LLM) pour analyser les demandes entrantes et exécuter les tâches avec ses propres outils internes.

#### Artefact

Une fois qu’un agent distant a terminé la tâche demandée, le produit de son travail est créé sous forme d’un artefact. Un artefact **contient le résultat du travail de l’agent**, une **description de ce qui a été accompli** et le **contexte textuel** envoyé via le protocole. Après l’envoi de l’artefact, la connexion avec l’agent distant est fermée jusqu’à la prochaine nécessité.

#### File d’Événements

Ce composant est utilisé pour **gérer les mises à jour et transmettre les messages**. C’est particulièrement important en production pour les systèmes agentiques afin d’éviter que la connexion entre agents ne soit fermée avant la fin d’une tâche, surtout lorsque la durée d’exécution peut être longue.

### Avantages du A2A

• **Collaboration améliorée** : Il permet à des agents provenant de différents fournisseurs et plateformes d’interagir, partager le contexte et collaborer, facilitant l’automatisation fluide entre des systèmes habituellement déconnectés.

• **Flexibilité dans le choix du modèle** : Chaque agent A2A peut décider quel LLM il utilise pour gérer ses requêtes, permettant d’optimiser ou de spécialiser les modèles par agent, contrairement à une connexion LLM unique dans certains scénarios MCP.

• **Authentification intégrée** : L’authentification est directement intégrée dans le protocole A2A, offrant un cadre de sécurité robuste pour l’interaction entre agents.

### Exemple A2A

![Diagramme A2A](../../../translated_images/fr/A2A-Diagram.8666928d648acc26.webp)

Développons notre scénario de réservation de voyage, mais cette fois en utilisant A2A.

1. **Demande utilisateur à multi-agents** : Un utilisateur interagit avec un client/agent A2A « Agent de voyage », par exemple en disant : « Veuillez réserver un voyage complet à Honolulu pour la semaine prochaine, incluant vols, hôtel et voiture de location ».

2. **Orchestration par l’Agent de Voyage** : L’agent reçoit cette demande complexe. Il utilise son LLM pour réfléchir à la tâche et déterminer qu’il doit interagir avec d’autres agents spécialisés.

3. **Communication inter-agents** : L’agent de voyage utilise ensuite le protocole A2A pour se connecter aux agents aval, comme un « Agent Compagnie Aérienne », un « Agent Hôtel » et un « Agent Location de Voiture » créés par différentes entreprises.

4. **Exécution déléguée des tâches** : L’agent de voyage envoie des tâches spécifiques à ces agents spécialisés (par ex., « Trouve des vols vers Honolulu », « Réserve un hôtel », « Loue une voiture »). Chacun de ces agents spécialisés, qui exécutent leurs propres LLM et utilisent leurs propres outils (qui peuvent eux-mêmes être des serveurs MCP), réalise sa partie spécifique de la réservation.

5. **Réponse consolidée** : Une fois que tous les agents aval ont terminé leurs tâches, l’agent de voyage compile les résultats (détails du vol, confirmation d’hôtel, réservation de voiture) et envoie une réponse complète, au format conversationnel, à l’utilisateur.

## Natural Language Web (NLWeb)

Les sites web ont longtemps été la principale manière pour les utilisateurs d’accéder à l’information et aux données sur Internet.

Examinons les différents composants de NLWeb, ses avantages et un exemple de fonctionnement de NLWeb via notre application de voyage.

### Composants de NLWeb

- **Application NLWeb (Code du service principal)** : Le système qui traite les questions en langage naturel. Il connecte les différentes parties de la plateforme pour créer des réponses. On peut le considérer comme **le moteur qui alimente les fonctionnalités en langage naturel** d’un site web.

- **Protocole NLWeb** : C’est un **ensemble basique de règles pour l’interaction en langage naturel** avec un site web. Il renvoie des réponses au format JSON (souvent en utilisant Schema.org). Son objectif est de créer une base simple pour le « Web IA », de la même manière que HTML a rendu possible le partage de documents en ligne.

- **Serveur MCP (Point de terminaison Model Context Protocol)** : Chaque configuration NLWeb fonctionne aussi comme un **serveur MCP**. Cela signifie qu’il peut **partager des outils (comme une méthode « ask ») et des données** avec d’autres systèmes IA. En pratique, cela rend le contenu et les capacités du site utilisables par des agents IA, permettant au site de devenir partie intégrante de « l’écosystème des agents ».

- **Modèles d’Embedding** : Ces modèles sont utilisés pour **convertir le contenu du site en représentations numériques appelées vecteurs** (embeddings). Ces vecteurs capturent le sens d’une manière exploitable par les ordinateurs pour comparer et rechercher. Ils sont stockés dans une base de données spécialisée, et les utilisateurs peuvent choisir quel modèle d’embedding ils souhaitent utiliser.

- **Base de données vectorielle (mécanisme de recherche)** : Cette base stocke **les embeddings du contenu du site**. Lorsqu’une question est posée, NLWeb consulte la base de vecteurs pour trouver rapidement l’information la plus pertinente. Elle fournit une liste rapide de réponses possibles, classées selon leur similarité. NLWeb fonctionne avec différents systèmes de stockage vectoriel tels que Qdrant, Snowflake, Milvus, Azure AI Search et Elasticsearch.

### NLWeb en exemple

![NLWeb](../../../translated_images/fr/nlweb-diagram.c1e2390b310e5fe4.webp)

Considérons à nouveau notre site de réservation de voyage, mais cette fois propulsé par NLWeb.

1. **Ingestion de données** : Les catalogues produits existants du site (par ex., listes de vols, descriptions d’hôtels, forfaits touristiques) sont formatés avec Schema.org ou chargés via des flux RSS. Les outils de NLWeb ingèrent ces données structurées, créent les embeddings et les stockent dans une base vectorielle locale ou distante.

2. **Requête en langage naturel (humain)** : Un utilisateur visite le site et, au lieu de naviguer dans des menus, tape dans une interface de chat : « Trouve-moi un hôtel familial à Honolulu avec piscine pour la semaine prochaine ».

3. **Traitement NLWeb** : L’application NLWeb reçoit cette requête. Elle l’envoie à un LLM pour compréhension et recherche simultanément dans sa base de données vectorielle les listes d’hôtels pertinentes.

4. **Résultats précis** : Le LLM aide à interpréter les résultats de recherche de la base, identifie les meilleures correspondances selon les critères « familial », « piscine » et « Honolulu », puis formate une réponse en langage naturel. Crucialement, la réponse fait référence aux hôtels réels du catalogue du site, évitant les informations inventées.

5. **Interaction avec un agent IA** : Parce que NLWeb sert de serveur MCP, un agent de voyage IA externe pourrait aussi se connecter à cette instance NLWeb. L’agent IA pourrait alors utiliser la méthode MCP `ask` pour interroger directement le site : `ask("Y a-t-il des restaurants végétaliens recommandés par l’hôtel dans la zone de Honolulu ?")`. L’instance NLWeb traiterait cela, exploitant sa base de données d’informations sur les restaurants (si chargée), et retournerait une réponse JSON structurée.

### Vous avez d’autres questions sur MCP/A2A/NLWeb ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources

- [MCP pour Débutants](https://aka.ms/mcp-for-beginners)  
- [Documentation MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Dépôt NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Leçon précédente

[Agents IA en production](../10-ai-agents-production/README.md)

## Leçon suivante

[Ingénierie du contexte pour agents IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->