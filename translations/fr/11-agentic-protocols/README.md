# Utilisation des Protocoles Agentics (MCP, A2A et NLWeb)

[![Protocoles Agentics](../../../translated_images/fr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

À mesure que l’utilisation des agents IA se développe, le besoin de protocoles assurant la standardisation, la sécurité et soutenant l'innovation ouverte augmente également. Dans cette leçon, nous aborderons 3 protocoles visant à répondre à ce besoin - Model Context Protocol (MCP), Agent to Agent (A2A) et Natural Language Web (NLWeb).

## Introduction

Dans cette leçon, nous couvrirons :

• Comment **MCP** permet aux agents IA d’accéder à des outils et données externes pour accomplir les tâches utilisateurs.

• Comment **A2A** facilite la communication et la collaboration entre différents agents IA.

• Comment **NLWeb** apporte des interfaces en langage naturel à n'importe quel site web permettant aux agents IA de découvrir et interagir avec le contenu.

## Objectifs d’apprentissage

• **Identifier** le but principal et les avantages de MCP, A2A, et NLWeb dans le contexte des agents IA.

• **Expliquer** comment chaque protocole facilite la communication et l’interaction entre LLM, outils et autres agents.

• **Reconnaître** les rôles distincts que chaque protocole joue dans la construction de systèmes agentiques complexes.

## Model Context Protocol

Le **Model Context Protocol (MCP)** est une norme ouverte qui fournit une manière standardisée pour les applications de fournir contexte et outils aux LLM. Cela permet un « adaptateur universel » aux différentes sources de données et outils auxquels les agents IA peuvent se connecter de façon cohérente.

Examinons les composants de MCP, ses avantages par rapport à l’utilisation directe d’API, et un exemple d’utilisation d’un serveur MCP par des agents IA.

### Composants principaux de MCP

MCP fonctionne sur une **architecture client-serveur** et les composants principaux sont :

• **Hôtes** : ce sont des applications LLM (par exemple un éditeur de code comme VSCode) qui initient les connexions à un serveur MCP.

• **Clients** : ce sont des composants au sein de l’application hôte qui maintiennent des connexions individuelles avec les serveurs.

• **Serveurs** : ce sont des programmes légers exposant des capacités spécifiques.

Le protocole inclut trois primitives principales qui correspondent aux capacités d’un serveur MCP :

• **Outils** : ce sont des actions ou fonctions distinctes qu’un agent IA peut appeler pour effectuer une action. Par exemple, un service météo pourrait exposer un outil « obtenir météo », ou un serveur e-commerce un outil « acheter produit ». Les serveurs MCP affichent dans leur liste de capacités chaque outil avec son nom, description et schéma d’entrée/sortie.

• **Ressources** : ce sont des éléments de données ou documents en lecture seule qu’un serveur MCP peut fournir et que les clients peuvent récupérer à la demande. Exemples : contenus de fichiers, enregistrements de bases de données, ou fichiers journaux. Les ressources peuvent être du texte (comme du code ou JSON) ou des données binaires (images ou PDF).

• **Prompts** : ce sont des modèles prédéfinis qui offrent des suggestions de requêtes, permettant des flux de travail plus complexes.

### Avantages de MCP

MCP offre des avantages significatifs pour les agents IA :

• **Découverte dynamique des outils** : Les agents peuvent recevoir dynamiquement une liste des outils disponibles d’un serveur avec les descriptions de leur fonctionnement. Contrairement aux API traditionnelles nécessitant une codification statique pour les intégrations, tout changement d'API exige des mises à jour de code. MCP propose une approche « s'intègre une fois », améliorant ainsi l'adaptabilité.

• **Interopérabilité entre LLM** : MCP fonctionne avec différents LLM, offrant la flexibilité de changer de modèle principal pour améliorer les performances.

• **Sécurité standardisée** : MCP comprend une méthode d’authentification standard, améliorant la montée en charge lors de l’ajout d’accès à plusieurs serveurs MCP. C’est plus simple que gérer différentes clés et types d’authentification pour diverses API traditionnelles.

### Exemple MCP

![Diagramme MCP](../../../translated_images/fr/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginez qu’un utilisateur souhaite réserver un vol via un assistant IA alimenté par MCP.

1. **Connexion** : L’assistant IA (client MCP) se connecte à un serveur MCP fourni par une compagnie aérienne.

2. **Découverte des outils** : Le client demande au serveur MCP de la compagnie, « Quels outils avez-vous disponibles ? » Le serveur affiche des outils comme « recherche vols » et « réserver vols ».

3. **Invocation d'outil** : Vous demandez alors à l’assistant IA : « Trouve un vol de Portland à Honolulu. » L’assistant utilise son LLM pour identifier la nécessité d’appeler l’outil « recherche vols » et transmet les paramètres (origine, destination) au serveur MCP.

4. **Exécution et réponse** : Le serveur MCP, jouant le rôle d’intermédiaire, effectue l’appel réel à l’API interne de réservation de la compagnie. Il reçoit ensuite les informations de vol (par ex. données JSON) et les transmet à l’assistant IA.

5. **Interaction supplémentaire** : L’assistant IA présente les options de vol. Une fois qu’un vol est sélectionné, l’assistant peut invoquer l’outil « réserver vol » sur le même serveur MCP pour finaliser la réservation.

## Protocole Agent-à-Agent (A2A)

Tandis que MCP se concentre sur la connexion des LLM aux outils, le **protocole Agent-à-Agent (A2A)** va plus loin en permettant la communication et la collaboration entre différents agents IA. A2A connecte des agents IA à travers différentes organisations, environnements et stacks technologiques pour accomplir une tâche partagée.

Nous examinerons les composants et avantages d’A2A ainsi qu’un exemple d’application dans notre scénario de voyage.

### Composants principaux d’A2A

A2A se concentre sur la communication entre agents et leur collaboration pour réaliser une sous-tâche de l’utilisateur. Chaque composant du protocole contribue à cela :

#### Fiche Agent

À l’instar d’un serveur MCP qui partage une liste d’outils, une Fiche Agent contient :
- Le nom de l’agent.
- Une **description des tâches générales** qu’il accomplit.
- Une **liste des compétences spécifiques** avec descriptions pour aider les autres agents (ou utilisateurs humains) à comprendre quand et pourquoi faire appel à cet agent.
- L’**URL actuelle du point d’accès** de l’agent.
- La **version** et les **capacités** de l’agent comme les réponses en streaming et notifications push.

#### Exécuteur d’Agent

L’Exécuteur d’Agent est responsable de **transmettre le contexte du chat utilisateur à l’agent distant**, ce dernier a besoin de ce contexte pour comprendre la tâche à accomplir. Dans un serveur A2A, un agent utilise son propre LLM pour analyser les requêtes entrantes et exécuter des tâches en utilisant ses outils internes.

#### Artefact

Une fois qu’un agent distant a terminé la tâche demandée, le produit de son travail est créé sous forme d’artefact. Un artefact **contient le résultat du travail de l’agent**, une **description de ce qui a été accompli**, et le **contexte texte** transmis via le protocole. Après l’envoi de l’artefact, la connexion avec l’agent distant est fermée jusqu’à ce qu’elle soit nécessaire à nouveau.

#### File d’événements

Ce composant sert à **gérer les mises à jour et transmettre les messages**. Il est particulièrement important en production pour les systèmes agentics afin d’éviter que la connexion entre agents ne soit fermée avant qu’une tâche soit terminée, surtout lorsque les temps de traitement peuvent être longs.

### Avantages d’A2A

• **Collaboration améliorée** : Permet aux agents de différents fournisseurs et plateformes d’interagir, partager le contexte et travailler ensemble, facilitant une automatisation fluide entre des systèmes traditionnellement déconnectés.

• **Flexibilité dans le choix du modèle** : Chaque agent A2A peut décider du LLM utilisé pour gérer ses requêtes, permettant d’optimiser ou d’ajuster les modèles pour chaque agent, contrairement à une connexion LLM unique dans certains cas MCP.

• **Authentification intégrée** : L’authentification est intégrée directement dans le protocole A2A, assurant un cadre de sécurité robuste pour les interactions entre agents.

### Exemple A2A

![Diagramme A2A](../../../translated_images/fr/A2A-Diagram.8666928d648acc26.webp)

Développons notre scénario de réservation de voyage, mais cette fois en utilisant A2A.

1. **Requête utilisateur vers multi-agents** : Un utilisateur interagit avec un client/agent A2A « Agent de Voyage », par exemple en disant : « Réserve-moi un voyage complet à Honolulu pour la semaine prochaine, vols, hôtel et voiture de location compris ».

2. **Orchestration par l’Agent de Voyage** : L’agent de voyage reçoit cette requête complexe. Il utilise son LLM pour raisonner sur la tâche et déterminer qu’il doit interagir avec d’autres agents spécialisés.

3. **Communication inter-agents** : L’agent de voyage utilise alors le protocole A2A pour se connecter aux agents en aval, tels qu’un « Agent Compagnie Aérienne », un « Agent Hôtel » et un « Agent Location de Voiture » créés par différentes entreprises.

4. **Exécution déléguée des tâches** : L’agent de voyage transmet des tâches spécifiques à ces agents spécialisés (ex. : « Trouve des vols pour Honolulu », « Réserve un hôtel », « Loue une voiture »). Chacun de ces agents spécialisés, utilisant leurs propres LLM et outils (qui peuvent être eux-mêmes des serveurs MCP), exécute sa partie spécifique de la réservation.

5. **Réponse consolidée** : Une fois que tous les agents en aval ont terminé leurs tâches, l’agent de voyage compile les résultats (détails des vols, confirmation d’hôtel, réservation de voiture) et renvoie une réponse complète au format conversationnel à l’utilisateur.

## Natural Language Web (NLWeb)

Les sites web sont depuis longtemps le moyen principal pour les utilisateurs d’accéder à l’information et aux données sur Internet.

Examinons les différents composants de NLWeb, les avantages de NLWeb et un exemple de fonctionnement de NLWeb via notre application de voyage.

### Composants de NLWeb

- **Application NLWeb (code du service principal)** : Le système qui traite les questions en langage naturel. Il connecte les différentes parties de la plateforme pour créer des réponses. On peut le voir comme **le moteur qui alimente les fonctions en langage naturel** d’un site web.

- **Protocole NLWeb** : C’est un **ensemble basique de règles pour l’interaction en langage naturel** avec un site web. Il renvoie des réponses au format JSON (souvent utilisant Schema.org). Son but est de créer une base simple pour le « Web IA », de la même manière que HTML a rendu possible le partage de documents en ligne.

- **Serveur MCP (point d’accès Model Context Protocol)** : Chaque installation NLWeb fait également office de **serveur MCP**. Cela signifie qu’elle peut **partager outils (comme une méthode « ask ») et données** avec d’autres systèmes IA. En pratique, cela rend le contenu et les fonctionnalités du site web accessibles aux agents IA, intégrant le site dans un écosystème agent plus large.

- **Modèles d’Embedding** : Ces modèles servent à **convertir le contenu du site web en représentations numériques appelées vecteurs** (embeddings). Ces vecteurs capturent la signification d’une manière exploitable par les ordinateurs pour comparer et rechercher. Ils sont stockés dans une base de données spéciale et l’utilisateur peut choisir le modèle d’embedding à utiliser.

- **Base de données vectorielle (mécanisme de recherche)** : Cette base stocke **les embeddings du contenu du site web**. Lorsqu’une question est posée, NLWeb interroge la base vectorielle pour retrouver rapidement l’information la plus pertinente. Elle fournit une liste rapide de réponses possibles, classées par similarité. NLWeb fonctionne avec différents systèmes de stockage vectoriel tels que Qdrant, Snowflake, Milvus, Azure AI Search, et Elasticsearch.

### NLWeb par exemple

![NLWeb](../../../translated_images/fr/nlweb-diagram.c1e2390b310e5fe4.webp)

Considérons à nouveau notre site de réservation de voyage, cette fois alimenté par NLWeb.

1. **Ingestion de données** : Les catalogues produits existants du site (ex. listes de vols, descriptions d’hôtels, packs touristiques) sont formatés avec Schema.org ou chargés via des flux RSS. Les outils de NLWeb ingèrent ces données structurées, créent des embeddings, et les stockent dans une base vectorielle locale ou distante.

2. **Requête en langage naturel (humain)** : Un utilisateur visite le site et, au lieu de naviguer dans les menus, tape dans une interface de chat : « Trouve-moi un hôtel familial à Honolulu avec piscine pour la semaine prochaine ».

3. **Traitement NLWeb** : L’application NLWeb reçoit la requête. Elle l’envoie à un LLM pour compréhension et simultanément interroge sa base vectorielle pour des listes d’hôtels pertinentes.

4. **Résultats précis** : Le LLM aide à interpréter les résultats de recherche dans la base, à identifier les meilleures correspondances selon les critères « familial », « piscine », « Honolulu », puis formule une réponse en langage naturel. Crucialement, la réponse fait référence aux vrais hôtels du catalogue du site, évitant les informations inventées.

5. **Interaction agent IA** : Parce que NLWeb fait aussi office de serveur MCP, un agent de voyage IA externe pourrait se connecter à cette instance NLWeb du site. L’agent IA pourrait alors utiliser la méthode `ask` MCP pour interroger directement le site : `ask("Y a-t-il des restaurants vegan-friendly dans la zone de Honolulu recommandés par l’hôtel ?")`. L’instance NLWeb traiterait cela, exploitant sa base de données d’informations sur les restaurants (si chargée), et renverrait une réponse JSON structurée.

### Vous avez encore des questions sur MCP/A2A/NLWeb ?

Rejoignez le [Discord Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister aux sessions d’aide et faire répondre vos questions sur les agents IA.

## Ressources

- [MCP pour débutants](https://aka.ms/mcp-for-beginners)  
- [Documentation MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Dépôt NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Framework Microsoft Agent](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Leçon précédente

[Agents IA en production](../10-ai-agents-production/README.md)

## Prochaine leçon

[Conception de contexte pour agents IA](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->