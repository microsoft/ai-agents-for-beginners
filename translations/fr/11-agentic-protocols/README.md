# Utilisation des Protocoles Agentiques (MCP, A2A et NLWeb)

[![Protocoles Agentiques](../../../translated_images/fr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

À mesure que l'utilisation des agents IA se développe, la nécessité de protocoles garantissant la standardisation, la sécurité et favorisant l'innovation ouverte grandit également. Dans cette leçon, nous aborderons 3 protocoles visant à répondre à ce besoin - le Model Context Protocol (MCP), Agent to Agent (A2A) et Natural Language Web (NLWeb).

## Introduction

Dans cette leçon, nous couvrirons :

• Comment **MCP** permet aux agents IA d'accéder à des outils et données externes pour accomplir les tâches des utilisateurs.

• Comment **A2A** facilite la communication et la collaboration entre différents agents IA.

• Comment **NLWeb** apporte des interfaces en langage naturel à n'importe quel site web, permettant aux agents IA de découvrir et d'interagir avec le contenu.

## Objectifs d'apprentissage

• **Identifier** le but principal et les avantages de MCP, A2A et NLWeb dans le contexte des agents IA.

• **Expliquer** comment chaque protocole facilite la communication et l'interaction entre LLM, outils et autres agents.

• **Reconnaître** les rôles distincts que chaque protocole joue dans la construction de systèmes agentiques complexes.

## Model Context Protocol

Le **Model Context Protocol (MCP)** est une norme ouverte qui fournit une méthode standardisée pour que les applications fournissent un contexte et des outils aux LLM. Cela permet un "adaptateur universel" vers différentes sources de données et outils auxquels les agents IA peuvent se connecter de manière cohérente.

Examinons les composants du MCP, ses avantages par rapport à l'utilisation directe d'API, et un exemple de la manière dont les agents IA pourraient utiliser un serveur MCP.

### Composants principaux du MCP

MCP fonctionne sur une **architecture client-serveur** et les composants principaux sont :

• Les **Hôtes** sont des applications LLM (par exemple un éditeur de code comme VSCode) qui initient les connexions à un serveur MCP.

• Les **Clients** sont des composants au sein de l'application hôte qui maintiennent des connexions un-à-un avec les serveurs.

• Les **Serveurs** sont des programmes légers qui exposent des capacités spécifiques.

Le protocole inclut trois primitives principales qui représentent les capacités d'un serveur MCP :

• **Outils** : Ce sont des actions ou fonctions discrètes qu'un agent IA peut appeler pour réaliser une action. Par exemple, un service météo pourrait exposer un outil "obtenir la météo", ou un serveur e-commerce un outil "acheter un produit". Les serveurs MCP annoncent le nom, la description et le schéma d'entrée/sortie de chaque outil dans leur liste de capacités.

• **Ressources** : Ce sont des données ou documents en lecture seule qu'un serveur MCP peut fournir, et que les clients peuvent récupérer à la demande. Exemples : contenus de fichiers, enregistrements de base de données ou fichiers journaux. Les ressources peuvent être du texte (comme du code ou JSON) ou binaires (comme des images ou PDF).

• **Prompts** : Ce sont des modèles prédéfinis fournissant des invites suggérées, permettant des flux de travail plus complexes.

### Avantages du MCP

MCP offre des avantages significatifs pour les agents IA :

• **Découverte dynamique d'outils** : Les agents peuvent recevoir dynamiquement une liste des outils disponibles d'un serveur avec leur description. Contrairement aux API traditionnelles qui nécessitent souvent une intégration statique, ce qui implique une mise à jour du code à chaque changement d'API, MCP propose une approche "intégrer une fois" plus adaptable.

• **Interopérabilité entre LLMs** : MCP fonctionne avec différents LLM, offrant la flexibilité de changer de modèle de base pour évaluer de meilleures performances.

• **Sécurité standardisée** : MCP inclut une méthode d'authentification standardisée, améliorant l'évolutivité lors de l'ajout d'accès à plusieurs serveurs MCP. C'est plus simple que de gérer différentes clés et types d'authentification pour diverses API traditionnelles.

### Exemple MCP

![Diagramme MCP](../../../translated_images/fr/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginez qu'un utilisateur souhaite réserver un vol via un assistant IA propulsé par MCP.

1. **Connexion** : L’assistant IA (le client MCP) se connecte à un serveur MCP fourni par une compagnie aérienne.

2. **Découverte des outils** : Le client demande au serveur MCP de la compagnie aérienne : "Quels outils avez-vous disponibles ?" Le serveur répond avec des outils comme "chercher des vols" et "réserver des vols".

3. **Invocation de l'outil** : Vous demandez alors à l'assistant IA : "Veuillez rechercher un vol de Portland à Honolulu." L'assistant IA, via son LLM, identifie qu'il doit appeler l'outil "chercher des vols" et transmet les paramètres pertinents (origine, destination) au serveur MCP.

4. **Exécution et réponse** : Le serveur MCP, agissant comme un wrapper, effectue l'appel réel à l'API interne de réservation de la compagnie aérienne. Il reçoit ensuite l'information du vol (par exemple des données JSON) et la renvoie à l'assistant IA.

5. **Interaction supplémentaire** : L'assistant IA présente les options de vol. Une fois un vol sélectionné, l'assistant peut invoquer l'outil "réserver le vol" sur le même serveur MCP, complétant ainsi la réservation.

## Protocole Agent-à-Agent (A2A)

Tandis que MCP se concentre sur la connexion des LLM aux outils, le **protocole Agent-à-Agent (A2A)** va plus loin en permettant la communication et la collaboration entre différents agents IA. A2A connecte des agents IA à travers différentes organisations, environnements et stacks technologiques pour accomplir une tâche commune.

Nous examinerons les composants et avantages de l’A2A, ainsi qu’un exemple d’application dans notre scénario de voyage.

### Composants principaux d’A2A

A2A se concentre sur la communication entre agents et leur collaboration pour accomplir une sous-tâche utilisateur. Chaque composant du protocole y contribue :

#### Carte d'Agent

À l’image d’un serveur MCP qui partage une liste d’outils, une Carte d'Agent comprend :
- Le nom de l’agent.
- Une **description des tâches générales** qu’il accomplit.
- Une **liste de compétences spécifiques** avec leurs descriptions pour aider les autres agents (ou même utilisateurs humains) à comprendre quand et pourquoi ils devraient appeler cet agent.
- L’**URL de point de terminaison** actuelle de l’agent
- La **version** et les **capacités** de l’agent telles que les réponses en streaming et notifications push.

#### Exécuteur d'Agent

L'Exécuteur d’Agent est responsable de **transmettre le contexte de la conversation utilisateur à l’agent distant**, ce dernier en a besoin pour comprendre la tâche à réaliser. Dans un serveur A2A, un agent utilise son propre Large Language Model (LLM) pour analyser les requêtes entrantes et exécuter les tâches avec ses propres outils internes.

#### Artefact

Une fois la tâche demandée complétée, le travail de l’agent distant est créé sous forme d’artefact. Un artefact **contient le résultat du travail de l’agent**, une **description de ce qui a été accompli**, et le **contexte textuel** transmis via le protocole. Après envoi de l’artefact, la connexion avec l’agent distant est fermée jusqu’à la prochaine utilisation.

#### File d’attente d’événements

Ce composant gère les **mises à jour et le passage de messages**. Il est particulièrement important en production pour les systèmes agentiques afin d’éviter que la connexion entre agents ne soit fermée avant la fin d’une tâche, surtout lorsque les délais peuvent être longs.

### Avantages d’A2A

• **Collaboration renforcée** : Il permet à des agents de vendeurs et plateformes différentes d’interagir, partager le contexte et collaborer, facilitant une automatisation fluide entre des systèmes traditionnellement déconnectés.

• **Flexibilité de sélection du modèle** : Chaque agent A2A peut choisir le LLM qu’il utilise pour ses requêtes, permettant d’optimiser ou d’affiner les modèles pour chaque agent, contrairement à la connexion unique à un LLM dans certains scénarios MCP.

• **Authentification intégrée** : L’authentification est directement intégrée dans le protocole A2A, fournissant un cadre de sécurité robuste pour les interactions agentiques.

### Exemple A2A

![Diagramme A2A](../../../translated_images/fr/A2A-Diagram.8666928d648acc26.webp)

Développons notre scénario de réservation de voyage, mais cette fois en utilisant A2A.

1. **Demande utilisateur au multi-agent** : Un utilisateur interagit avec un agent/client A2A "Agent de Voyage", par exemple en disant : "Veuillez réserver un voyage complet à Honolulu pour la semaine prochaine, incluant vols, hôtel et voiture de location".

2. **Orchestration par l’Agent de Voyage** : L’Agent de Voyage reçoit cette demande complexe. Il utilise son LLM pour raisonner sur la tâche et déterminer qu’il doit interagir avec d’autres agents spécialisés.

3. **Communication inter-agent** : L’Agent de Voyage utilise alors le protocole A2A pour se connecter à des agents en aval, comme un "Agent Compagnie Aérienne", un "Agent Hôtel" et un "Agent Location de Voiture", créés par différentes entreprises.

4. **Exécution déléguée des tâches** : L’Agent de Voyage envoie des tâches spécifiques à ces agents spécialisés (ex : "Trouve des vols pour Honolulu", "Réserve un hôtel", "Loue une voiture"). Chacun de ces agents spécialisés, exécutant leur propre LLM et utilisant leurs outils (qui pourraient eux-mêmes être des serveurs MCP), accomplit sa partie spécifique de la réservation.

5. **Réponse consolidée** : Une fois que tous les agents en aval ont terminé leurs tâches, l’Agent de Voyage compile les résultats (détails des vols, confirmation hôtel, réservation voiture) et envoie une réponse complète sous forme de chat à l’utilisateur.

## Natural Language Web (NLWeb)

Les sites web ont longtemps été la principale manière pour les utilisateurs d’accéder à l’information et aux données sur internet.

Voyons les différents composants de NLWeb, ses avantages et un exemple de fonctionnement de NLWeb avec notre application de voyage.

### Composants de NLWeb

- **Application NLWeb (Code du service principal)** : Le système qui traite les questions en langage naturel. Il connecte les différentes parties de la plateforme pour générer des réponses. On peut le voir comme **le moteur qui alimente les fonctionnalités en langage naturel** d’un site web.

- **Protocole NLWeb** : C’est un **ensemble basique de règles pour l’interaction en langage naturel** avec un site web. Il renvoie des réponses au format JSON (souvent en utilisant Schema.org). Son but est de créer une base simple pour le « Web IA », de la même manière qu’HTML a permis de partager des documents en ligne.

- **Serveur MCP (point de terminaison Model Context Protocol)** : Chaque configuration NLWeb fonctionne aussi comme un **serveur MCP**. Cela signifie qu’il peut **partager des outils (comme une méthode « ask ») et des données** avec d’autres systèmes IA. En pratique, cela rend le contenu et les capacités du site accessibles aux agents IA, permettant au site de faire partie de l’écosystème plus large des agents.

- **Modèles d’Embedding** : Ces modèles sont utilisés pour **convertir le contenu du site web en représentations numériques appelées vecteurs** (embeddings). Ces vecteurs capturent le sens d’une manière que les ordinateurs peuvent comparer et rechercher. Ils sont stockés dans une base de données spéciale, et les utilisateurs peuvent choisir le modèle d’embedding qu’ils souhaitent utiliser.

- **Base de données vectorielle (mécanisme de recherche)** : Cette base stocke **les embeddings du contenu du site**. Lorsqu’une question est posée, NLWeb consulte la base vectorielle pour trouver rapidement l’information la plus pertinente. Elle retourne une liste rapide de réponses possibles, classées par similarité. NLWeb fonctionne avec différentes solutions de stockage vectoriel telles que Qdrant, Snowflake, Milvus, Azure AI Search et Elasticsearch.

### NLWeb par l'exemple

![NLWeb](../../../translated_images/fr/nlweb-diagram.c1e2390b310e5fe4.webp)

Considérons à nouveau notre site de réservation de voyage, mais cette fois propulsé par NLWeb.

1. **Ingestion de données** : Les catalogues produits existants du site (par exemple listes de vols, descriptions d’hôtels, forfaits touristiques) sont formatés en utilisant Schema.org ou chargés via des flux RSS. Les outils de NLWeb ingèrent ces données structurées, créent des embeddings, et les stockent dans une base vectorielle locale ou distante.

2. **Requête en langage naturel (humain)** : Un utilisateur visite le site et, au lieu de naviguer dans des menus, tape dans une interface de chat : « Trouve-moi un hôtel familial à Honolulu avec piscine pour la semaine prochaine ».

3. **Traitement NLWeb** : L’application NLWeb reçoit cette requête. Elle l’envoie à un LLM pour compréhension et recherche simultanément dans sa base vectorielle les listings d’hôtels pertinents.

4. **Résultats précis** : Le LLM aide à interpréter les résultats issus de la base, identifie les meilleures correspondances selon les critères "familial", "piscine" et "Honolulu", puis formate une réponse en langage naturel. Crucialement, la réponse fait référence aux hôtels réels du catalogue, évitant les informations inventées.

5. **Interaction avec un agent IA** : Parce que NLWeb sert de serveur MCP, un agent IA de voyage externe pourrait aussi se connecter à cette instance NLWeb du site. L’agent IA pourrait alors utiliser la méthode `ask` MCP pour interroger directement le site : `ask("Y a-t-il des restaurants vegan-friendly dans la région d’Honolulu recommandés par l’hôtel ?")`. L’instance NLWeb traiterait cela, exploitant sa base de données d’informations sur les restaurants (si chargée), et retournerait une réponse JSON structurée.

### Vous avez d’autres questions sur MCP/A2A/NLWeb ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources

- [MCP pour débutants](https://aka.ms/mcp-for-beginners)  
- [Documentation MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Répertoire NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Leçon précédente

[Agents IA en production](../10-ai-agents-production/README.md)

## Leçon suivante

[Ingénierie de contexte pour agents IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->