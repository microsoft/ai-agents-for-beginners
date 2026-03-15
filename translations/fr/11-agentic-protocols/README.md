# Utilisation des Protocoles Agentiques (MCP, A2A et NLWeb)

[![Agentic Protocols](../../../translated_images/fr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

À mesure que l'utilisation des agents IA se développe, le besoin de protocoles garantissant la normalisation, la sécurité et favorisant l'innovation ouverte grandit également. Dans cette leçon, nous couvrirons 3 protocoles cherchant à répondre à ce besoin - le Model Context Protocol (MCP), Agent to Agent (A2A) et Natural Language Web (NLWeb).

## Introduction

Dans cette leçon, nous aborderons :

• Comment **MCP** permet aux agents IA d'accéder à des outils externes et des données pour accomplir les tâches des utilisateurs.

• Comment **A2A** facilite la communication et la collaboration entre différents agents IA.

• Comment **NLWeb** apporte des interfaces en langage naturel à n'importe quel site web, permettant aux agents IA de découvrir et d'interagir avec le contenu.

## Objectifs d'apprentissage

• **Identifier** l'objectif principal et les avantages de MCP, A2A et NLWeb dans le contexte des agents IA.

• **Expliquer** comment chaque protocole facilite la communication et l'interaction entre LLMs, outils et autres agents.

• **Reconnaître** les rôles distincts que joue chaque protocole dans la création de systèmes agentiques complexes.

## Model Context Protocol

Le **Model Context Protocol (MCP)** est une norme ouverte qui fournit un moyen standardisé pour les applications d'offrir du contexte et des outils aux LLMs. Cela permet un "adaptateur universel" vers différentes sources de données et outils auxquels les agents IA peuvent se connecter de manière cohérente.

Examinons les composants de MCP, les avantages comparés à l'utilisation directe d'API et un exemple de l'utilisation d'un serveur MCP par des agents IA.

### Composants principaux de MCP

MCP fonctionne selon une **architecture client-serveur** et les composants clés sont :

• **Hôtes** : applications LLM (par exemple un éditeur de code comme VSCode) qui initient les connexions vers un serveur MCP.

• **Clients** : composants au sein de l'application hôte qui maintiennent des connexions individuelles avec les serveurs.

• **Serveurs** : programmes légers qui exposent des capacités spécifiques.

Inclus dans le protocole, trois primitives fondamentales qui définissent les capacités d'un serveur MCP :

• **Outils** : Actions ou fonctions distinctes qu’un agent IA peut appeler pour exécuter une tâche. Par exemple, un service météo pourrait exposer un outil "obtenir la météo", ou un serveur e-commerce un outil "acheter un produit". Les serveurs MCP annoncent le nom de chaque outil, sa description, et le schéma d'entrée/sortie dans leur liste de capacités.

• **Ressources** : Eléments de données ou documents en lecture seule qu’un serveur MCP peut fournir, pouvant être récupérés à la demande par les clients. Exemples : contenu de fichiers, enregistrements de bases de données ou fichiers journaux. Les ressources peuvent être du texte (comme du code ou JSON) ou du binaire (comme images ou PDF).

• **Prompts** : Modèles prédéfinis fournissant des suggestions de prompts, permettant des workflows plus complexes.

### Avantages de MCP

MCP offre des avantages substantiels pour les agents IA :

• **Découverte dynamique des outils** : Les agents peuvent recevoir dynamiquement une liste d’outils disponibles d’un serveur accompagnée de descriptions. Contrairement aux APIs traditionnelles souvent nécessitant un codage statique pour intégration, où tout changement d’API demande une mise à jour de code, MCP offre une approche "intégrer une fois", augmentant ainsi l’adaptabilité.

• **Interopérabilité entre LLMs** : MCP fonctionne à travers différents LLMs, fournissant la flexibilité de changer de modèle principal pour optimiser la performance.

• **Sécurité standardisée** : MCP inclut un mode d’authentification standard, améliorant la scalabilité lors de l’ajout d’accès à plusieurs serveurs MCP. C’est plus simple que de gérer différentes clés et modes d’authentification pour des APIs traditionnelles variées.

### Exemple MCP

![MCP Diagram](../../../translated_images/fr/mcp-diagram.e4ca1cbd551444a1.webp)

Imaginez qu’un utilisateur souhaite réserver un vol via un assistant IA alimenté par MCP.

1. **Connexion** : L’assistant IA (client MCP) se connecte à un serveur MCP fourni par une compagnie aérienne.

2. **Découverte des outils** : Le client interroge le serveur MCP de la compagnie : « Quels outils avez-vous de disponibles ? » Le serveur répond avec des outils tels que "rechercher vols" et "réserver vols".

3. **Invocation de l’outil** : Vous demandez ensuite à l’assistant IA : « Veuillez chercher un vol de Portland à Honolulu. » L’assistant IA, via son LLM, identifie qu’il doit appeler l’outil "rechercher vols" et transmet les paramètres pertinents (origine, destination) au serveur MCP.

4. **Exécution et Réponse** : Le serveur MCP, servant d’enveloppe, effectue l’appel réel à l’API interne de réservation de la compagnie aérienne. Il reçoit les informations de vol (ex : données JSON) et les renvoie à l’assistant IA.

5. **Interaction complémentaire** : L’assistant IA présente les options de vol. Une fois que vous sélectionnez un vol, l’assistant peut invoquer l’outil "réserver vol" sur le même serveur MCP, finalisant la réservation.

## Protocole Agent-à-Agent (A2A)

Alors que MCP se concentre sur la connexion des LLMs aux outils, le **protocole Agent-à-Agent (A2A)** va plus loin en permettant la communication et la collaboration entre différents agents IA. A2A connecte des agents IA à travers différents organismes, environnements et stacks technologiques pour accomplir une tâche partagée.

Nous examinerons les composants et avantages d’A2A, avec un exemple d’application dans notre scénario de voyage.

### Composants principaux d’A2A

A2A vise à autoriser la communication entre agents et leur travail conjoint pour effectuer une sous-tâche utilisateur. Chaque composant du protocole contribue à cela :

#### Carte d’Agent

Similaire à la manière dont un serveur MCP partage sa liste d’outils, une Carte d’Agent comprend :
- Le nom de l’agent.
- Une **description des tâches générales** qu’il accomplit.
- Une **liste des compétences spécifiques** avec descriptions pour aider d’autres agents (ou même des utilisateurs humains) à comprendre quand et pourquoi appeler cet agent.
- L’**URL de Point de Terminaison (Endpoint)** actuelle de l’agent.
- La **version** et les **capacités** de l’agent telles que réponses en streaming et notifications push.

#### Exécuteur d’Agent

L’Exécuteur d’Agent est responsable de **transmettre le contexte de la conversation utilisateur à l’agent distant** ; cet agent distant a besoin de ce contexte pour comprendre la tâche à accomplir. Dans un serveur A2A, un agent utilise son propre modèle de langage (LLM) pour analyser les requêtes entrantes et exécuter les tâches via ses propres outils internes.

#### Artefact

Une fois la tâche terminée par l’agent distant, son produit de travail est créé sous forme d’artefact. Un artefact **contient le résultat du travail de l’agent**, une **description de ce qui a été réalisé** et le **contexte textuel** transmis via le protocole. Après l’envoi de l’artefact, la connexion avec l’agent distant est fermée jusqu’à sa prochaine utilisation.

#### File d’événements

Ce composant est utilisé pour **gérer les mises à jour et le passage de messages**. Il est particulièrement important en production avec des systèmes agentiques pour empêcher que la connexion entre agents soit fermée avant la complétion d’une tâche, surtout lorsque certaines tâches prennent plus de temps.

### Avantages d’A2A

• **Collaboration améliorée** : Permet à des agents de différents fournisseurs et plateformes d’interagir, partager du contexte et collaborer, facilitant l’automatisation fluide entre des systèmes traditionnellement déconnectés.

• **Flexibilité de sélection de modèles** : Chaque agent A2A peut choisir le LLM qu’il utilise pour répondre à ses requêtes, permettant d’optimiser ou d’affiner les modèles par agent, contrairement à une connexion unique à un LLM dans certains cas MCP.

• **Authentification intégrée** : L’authentification est incluse directement dans le protocole A2A, offrant un cadre de sécurité robuste pour les interactions entre agents.

### Exemple A2A

![A2A Diagram](../../../translated_images/fr/A2A-Diagram.8666928d648acc26.webp)

Développons notre scénario de réservation de voyage, mais cette fois en utilisant A2A.

1. **Requête utilisateur vers multi-agent** : Un utilisateur interagit avec un client/agent A2A "Agent de voyage", par exemple en disant : « Veuillez réserver un voyage complet à Honolulu pour la semaine prochaine, incluant vols, hôtel et location de voiture ».

2. **Orchestration par l’Agent de voyage** : L’agent de voyage reçoit cette requête complexe. Il utilise son LLM pour raisonner sur la tâche et déterminer qu’il doit interagir avec d’autres agents spécialisés.

3. **Communication inter-agents** : L’agent de voyage utilise le protocole A2A pour se connecter à des agents en aval, tels que un "Agent compagnie aérienne", un "Agent hôtel" et un "Agent location de voiture" créés par différentes sociétés.

4. **Exécution déléguée des tâches** : L’agent de voyage envoie des tâches spécifiques à ces agents spécialisés (ex : "Trouver vols vers Honolulu", "Réserver un hôtel", "Louer une voiture"). Chacun de ces agents, utilisant son propre LLM et ses propres outils (qui pourraient eux-mêmes être des serveurs MCP), exécute sa partie de la réservation.

5. **Réponse consolidée** : Une fois que tous les agents en aval ont terminé, l’agent de voyage compile les résultats (détails vol, confirmation hôtel, réservation voiture) et renvoie une réponse complète au format conversationnel à l’utilisateur.

## Natural Language Web (NLWeb)

Les sites web ont de tout temps été le moyen principal pour les utilisateurs d’accéder à l’information et aux données sur Internet.

Regardons les différents composants de NLWeb, les avantages de NLWeb et un exemple de fonctionnement de NLWeb dans notre application de voyage.

### Composants de NLWeb

- **Application NLWeb (code core du service)** : Le système qui traite les questions en langage naturel. Il connecte différentes parties de la plateforme pour créer les réponses. On peut le considérer comme le **moteur qui alimente les fonctionnalités en langage naturel** d’un site web.

- **Protocole NLWeb** : Il s’agit d’un **ensemble de règles basiques pour l’interaction en langage naturel** avec un site web. Il renvoie des réponses au format JSON (souvent utilisant Schema.org). Son objectif est de créer une base simple pour le « Web IA », tout comme HTML a rendu possible le partage de documents en ligne.

- **Serveur MCP (point de terminaison Model Context Protocol)** : Chaque installation NLWeb fonctionne aussi comme un **serveur MCP**. Cela signifie qu’il peut **partager des outils (comme une méthode “ask”) et des données** avec d’autres systèmes IA. En pratique, cela rend le contenu et les capacités du site accessibles aux agents IA, permettant au site de devenir partie intégrante de l’« écosystème agent » plus large.

- **Modèles d’Embarquement (Embedding Models)** : Ces modèles sont utilisés pour **convertir le contenu du site en représentations numériques appelées vecteurs (embeddings)**. Ces vecteurs capturent le sens de manière que les ordinateurs peuvent comparer et rechercher. Ils sont stockés dans une base de données spéciale. Les utilisateurs peuvent choisir le modèle d’embedding qu’ils souhaitent utiliser.

- **Base de données vectorielle (mécanisme de recherche)** : Cette base **stocke les embeddings du contenu du site web**. Lorsqu’une question est posée, NLWeb interroge cette base pour trouver rapidement les informations les plus pertinentes. Elle fournit une liste rapide des réponses possibles, classées par similarité. NLWeb fonctionne avec différents systèmes de stockage vectoriel tels que Qdrant, Snowflake, Milvus, Azure AI Search et Elasticsearch.

### Exemple NLWeb

![NLWeb](../../../translated_images/fr/nlweb-diagram.c1e2390b310e5fe4.webp)

Considérons encore une fois notre site de réservation de voyage, mais cette fois, il est alimenté par NLWeb.

1. **Ingestion des données** : Les catalogues produits existants du site de voyage (par exemple, listings de vols, descriptions d’hôtels, forfaits touristiques) sont formatés via Schema.org ou chargés via des flux RSS. Les outils de NLWeb ingèrent ces données structurées, créent des embeddings, et les stockent dans une base vectorielle locale ou distante.

2. **Requête en langage naturel (humaine)** : Un utilisateur visite le site et, au lieu de naviguer dans les menus, tape dans une interface de chat : « Trouve-moi un hôtel familial à Honolulu avec piscine pour la semaine prochaine ».

3. **Traitement NLWeb** : L’application NLWeb reçoit cette requête. Elle l’envoie à un LLM pour compréhension et en parallèle elle recherche dans sa base vectorielle les listings d’hôtels pertinents.

4. **Résultats précis** : Le LLM aide à interpréter les résultats de la base, identifie les meilleures correspondances selon les critères "familial", "piscine" et "Honolulu", puis formate une réponse en langage naturel. Crucialement, la réponse fait référence à des hôtels réels du catalogue du site, évitant les informations inventées.

5. **Interaction agent IA** : Parce que NLWeb agit comme un serveur MCP, un agent IA de voyage externe pourrait également se connecter à cette instance NLWeb du site. L’agent IA pourrait utiliser la méthode MCP `ask` pour interroger directement le site : `ask("Y a-t-il des restaurants végétaliens recommandés par l’hôtel dans la région de Honolulu ?")`. NLWeb traiterait cette demande en tirant parti de sa base d’informations sur les restaurants (si chargée) et retournerait une réponse JSON structurée.

### Vous avez plus de questions sur MCP/A2A/NLWeb ?

Rejoignez le [Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, participer aux heures de support, et obtenir des réponses à vos questions sur les agents IA.

## Ressources

- [MCP pour débutants](https://aka.ms/mcp-for-beginners)  
- [Documentation MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Répertoire NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->