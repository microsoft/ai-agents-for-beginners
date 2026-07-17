# Ingénierie du Contexte pour Agents IA

[![Ingénierie du Contexte](../../../translated_images/fr/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

Comprendre la complexité de l'application pour laquelle vous construisez un agent IA est important pour en faire un agent fiable. Nous devons construire des agents IA qui gèrent efficacement l'information pour répondre à des besoins complexes au-delà de l'ingénierie de prompt.

Dans cette leçon, nous examinerons ce qu'est l'ingénierie du contexte et son rôle dans la construction d'agents IA.

## Introduction

Cette leçon couvrira :

• **Ce qu'est l'Ingénierie du Contexte** et pourquoi elle diffère de l'ingénierie de prompt.

• **Les stratégies pour une ingénierie efficace du contexte**, y compris comment écrire, sélectionner, compresser et isoler l'information.

• **Les défaillances courantes du contexte** qui peuvent faire dérailler votre agent IA et comment les corriger.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

• **Définir l'ingénierie du contexte** et la différencier de l'ingénierie de prompt.

• **Identifier les composants clés du contexte** dans les applications utilisant les grands modèles de langage (LLM).

• **Appliquer des stratégies pour écrire, sélectionner, compresser et isoler le contexte** afin d'améliorer les performances de l'agent.

• **Reconnaître les défaillances courantes du contexte** telles que l'empoisonnement, la distraction, la confusion, et le conflit, et mettre en œuvre des techniques d'atténuation.

## Qu'est-ce que l'Ingénierie du Contexte ?

Pour les agents IA, le contexte est ce qui guide la planification d'un agent IA pour effectuer certaines actions. L'ingénierie du contexte est la pratique qui consiste à s'assurer que l'agent IA dispose des bonnes informations pour accomplir l'étape suivante de la tâche. La fenêtre de contexte est limitée en taille, donc en tant que concepteurs d'agents, nous devons construire des systèmes et des processus pour gérer l'ajout, la suppression et la condensation des informations dans cette fenêtre de contexte.

### Ingénierie de Prompt vs Ingénierie de Contexte

L'ingénierie de prompt se concentre sur un ensemble unique d'instructions statiques pour guider efficacement les agents IA avec un ensemble de règles. L'ingénierie de contexte concerne la gestion d'un ensemble dynamique d'informations, y compris le prompt initial, afin de garantir que l'agent IA dispose de ce dont il a besoin au fil du temps. L'idée principale autour de l'ingénierie du contexte est de rendre ce processus répétable et fiable.

### Types de Contexte

[![Types de Contexte](../../../translated_images/fr/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Il est important de se rappeler que le contexte n'est pas une seule chose. L'information dont l'agent IA a besoin peut provenir de différentes sources, et c'est à nous de nous assurer que l'agent a accès à ces sources :

Les types de contexte qu'un agent IA pourrait avoir besoin de gérer incluent :

• **Instructions :** Ce sont comme les "règles" de l'agent – les prompts, messages système, exemples few-shot (montrant à l'IA comment faire quelque chose), et descriptions des outils qu'il peut utiliser. C'est là où la focalisation de l'ingénierie de prompt se combine avec l'ingénierie du contexte.

• **Connaissances :** Cela couvre les faits, les informations extraites de bases de données, ou les mémoires à long terme accumulées par l'agent. Cela inclut l'intégration d'un système de génération augmentée par récupération (RAG) si un agent a besoin d'accéder à différentes banques de connaissances et bases de données.

• **Outils :** Ce sont les définitions des fonctions externes, APIs et serveurs MCP que l'agent peut appeler, ainsi que les retours (résultats) qu'il obtient en les utilisant.

• **Historique de Conversation :** Le dialogue en cours avec un utilisateur. Au fil du temps, ces conversations deviennent plus longues et plus complexes, ce qui signifie qu'elles prennent de la place dans la fenêtre de contexte.

• **Préférences Utilisateur :** Informations apprises sur les goûts ou dégoûts d'un utilisateur au fil du temps. Elles peuvent être stockées et utilisées lors de décisions clés pour aider l'utilisateur.

## Stratégies pour une Ingénierie du Contexte Efficace

### Stratégies de Planification

[![Bonnes Pratiques d'Ingénierie du Contexte](../../../translated_images/fr/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Une bonne ingénierie du contexte commence par une bonne planification. Voici une approche qui vous aidera à commencer à penser à la façon d'appliquer le concept d'ingénierie du contexte :

1. **Définir des Résultats Clairs** - Les résultats des tâches assignées aux agents IA doivent être clairement définis. Répondez à la question : "À quoi ressemblera le monde quand l'agent IA aura terminé sa tâche ?" En d'autres termes, quel changement, quelle information ou quelle réponse l'utilisateur doit-il avoir après avoir interagi avec l'agent IA.
2. **Cartographier le Contexte** - Une fois que vous avez défini les résultats de l'agent IA, vous devez répondre à la question : "Quelles informations l'agent IA a-t-il besoin pour accomplir cette tâche ?". Ainsi, vous pouvez commencer à cartographier le contexte et où cette information peut être trouvée.
3. **Créer des Pipelines de Contexte** - Maintenant que vous savez où se trouve l'information, vous devez répondre à la question : "Comment l'agent obtiendra-t-il cette information ?". Cela peut être fait de différentes manières, y compris RAG, l’utilisation de serveurs MCP et d'autres outils.

### Stratégies Pratiques

La planification est importante, mais une fois que l'information commence à affluer dans la fenêtre de contexte de notre agent, nous devons avoir des stratégies pratiques pour la gérer :

#### Gestion du Contexte

Bien que certaines informations soient ajoutées automatiquement à la fenêtre de contexte, l'ingénierie du contexte consiste à prendre un rôle plus actif sur cette information, ce qui peut être fait par quelques stratégies :

 1. **Carnet de Notes de l'Agent**
 Cela permet à un agent IA de prendre des notes sur les informations pertinentes concernant les tâches en cours et les interactions utilisateur durant une session unique. Cela doit exister en dehors de la fenêtre de contexte dans un fichier ou un objet runtime que l'agent pourra récupérer plus tard durant cette session si nécessaire.

 2. **Mémoires**
 Les carnets de notes sont adaptés pour gérer l’information extérieure à la fenêtre de contexte d'une session unique. Les mémoires permettent aux agents de stocker et de récupérer des informations pertinentes à travers plusieurs sessions. Cela pourrait inclure des résumés, des préférences utilisateur, et des retours pour améliorer le futur.

 3. **Compression du Contexte**
  Une fois que la fenêtre de contexte grandit et approche de sa limite, des techniques telles que la synthèse et la réduction peuvent être utilisées. Cela inclut soit de ne garder que les informations les plus pertinentes, soit de supprimer les messages plus anciens.
  
 4. **Systèmes Multi-Agents**
  Développer un système multi-agent est une forme d’ingénierie du contexte car chaque agent a sa propre fenêtre de contexte. La manière dont ce contexte est partagé et transmis entre différents agents est une autre chose à planifier lors de la construction de ces systèmes.
  
 5. **Environnements Sandbox**
  Si un agent doit exécuter un code ou traiter de grandes quantités d’informations dans un document, cela peut nécessiter un grand nombre de tokens pour traiter les résultats. Plutôt que de tout stocker dans la fenêtre de contexte, l’agent peut utiliser un environnement sandbox capable d’exécuter ce code et de ne lire que les résultats et autres informations pertinentes.
  
 6. **Objets d'État au Runtime**
   Cela se fait en créant des conteneurs d'informations pour gérer les situations où l'agent a besoin d'avoir accès à certaines informations. Pour une tâche complexe, cela permettrait à un agent de stocker les résultats de chaque sous-tâche étape par étape, permettant au contexte de rester lié uniquement à cette sous-tâche spécifique.

#### Inspecter le Contexte

Après avoir appliqué une de ces stratégies, il est utile de vérifier ce que l'appel au modèle suivant a réellement reçu. Une question de débogage utile est :

> L'agent a-t-il chargé trop de contexte, un mauvais contexte, ou manqué du contexte dont il avait besoin ?

Vous n'avez pas besoin de journaliser les prompts bruts, les sorties d'outils, ou le contenu des mémoires pour répondre à cette question. En production, préférez des enregistrements d’inspection de contexte petits qui capturent comptages, IDs, hash, et étiquettes de politique :

- **Sélection :** Suivre combien de morceaux candidats, outils, ou mémoires ont été considérés, combien ont été sélectionnés, et quelle règle ou score a fait filtrer les autres.
- **Compression :** Enregistrer la plage source ou l’ID de trace, l’ID du résumé, une estimation du nombre de tokens avant et après compression, et si le contenu brut a été exclu de l'appel suivant.
- **Isolation :** Noter quelle sous-tâche a été exécutée dans un agent, une session ou un sandbox séparé, quel résumé borné a été retourné, et si les grandes sorties d’outils sont restées en dehors du contexte de l’agent principal.
- **Mémoire et RAG :** Stocker les IDs des documents récupérés, IDs de mémoire, scores, IDs sélectionnés, et statut de caviardage au lieu du texte complet récupéré.
- **Sécurité et confidentialité :** Préférez les hash, IDs, compartiments de tokens, et étiquettes de politique plutôt que texte sensible de prompt, arguments d’outils, résultats d’outils, ou corps de mémoire utilisateur.

Le but n'est pas de garder plus de contexte. Il est de laisser suffisamment de preuves pour qu'un développeur puisse dire quelle stratégie de contexte a été utilisée et si elle a modifié l'appel au modèle suivant comme prévu.

### Exemple d'Ingénierie du Contexte

Disons que nous voulons qu'un agent IA **"Réserve-moi un voyage à Paris."**

• Un agent simple utilisant uniquement l'ingénierie de prompt pourrait simplement répondre : **"D'accord, quand souhaitez-vous aller à Paris ?**". Il a seulement traité votre question directe au moment où l'utilisateur a demandé.

• Un agent utilisant les stratégies d'ingénierie du contexte couvertes ferait beaucoup plus. Avant même de répondre, son système pourrait :

  ◦ **Vérifier votre calendrier** pour les dates disponibles (en récupérant des données en temps réel).

 ◦ **Se souvenir des préférences de voyage passées** (depuis la mémoire à long terme) comme votre compagnie aérienne préférée, votre budget, ou si vous préférez les vols directs.

 ◦ **Identifier les outils disponibles** pour la réservation de vols et d'hôtels.

- Puis, une réponse exemple pourrait être : "Salut [Votre Nom] ! Je vois que vous êtes libre la première semaine d'octobre. Dois-je chercher des vols directs vers Paris sur [Compagnie Préférée] dans votre budget habituel de [Budget] ?". Cette réponse plus riche et consciente du contexte démontre le pouvoir de l'ingénierie du contexte.

## Défaillances Courantes du Contexte

### Empoisonnement du Contexte

**Qu'est-ce que c'est :** Lorsqu'une hallucination (fausse information générée par le LLM) ou une erreur entre dans le contexte et est référencée de façon répétée, faisant que l'agent poursuit des objectifs impossibles ou développe des stratégies absurdes.

**Que faire :** Mettez en place une **validation du contexte** et une **quarantaine**. Validez les informations avant qu'elles soient ajoutées à la mémoire à long terme. Si un empoisonnement potentiel est détecté, démarrez de nouveaux fils de contexte pour empêcher la diffusion de la mauvaise information.

**Exemple de Réservation de Voyage :** Votre agent hallucine un **vol direct d'un petit aéroport local vers une ville internationale distante** qui n'offre en réalité pas de vols internationaux. Ce détail de vol inexistant est enregistré dans le contexte. Plus tard, lorsque vous demandez à l'agent de réserver, il continue d'essayer de trouver des billets pour cette route impossible, ce qui provoque des erreurs répétées.

**Solution :** Implémentez une étape qui **valide l'existence des vols et les itinéraires avec une API en temps réel** _avant_ d'ajouter le détail du vol au contexte de travail de l'agent. Si la validation échoue, l'information erronée est "quarantainée" et n'est pas utilisée davantage.

### Distraction du Contexte

**Qu'est-ce que c'est :** Lorsque le contexte devient si volumineux que le modèle se concentre trop sur l'historique accumulé plutôt que d'utiliser ce qu'il a appris durant l'entraînement, menant à des actions répétitives ou inutiles. Les modèles peuvent commencer à faire des erreurs même avant que la fenêtre de contexte soit pleine.

**Que faire :** Utilisez la **synthèse du contexte**. Comprimez périodiquement l'information accumulée en des résumés plus courts, conservant les détails importants tout en éliminant l'historique redondant. Cela aide à "réinitialiser" la concentration.

**Exemple de Réservation de Voyage :** Vous avez discuté de diverses destinations de voyage de rêve pendant longtemps, y compris un récit détaillé de votre voyage sac à dos d'il y a deux ans. Lorsque vous demandez finalement à **"trouver un vol pas cher pour le mois prochain,"** l'agent est embourbé dans les vieux détails non pertinents et continue à poser des questions sur votre équipement de randonnée ou vos itinéraires passés, négligeant votre demande actuelle.

**Solution :** Après un certain nombre d'échanges ou lorsque le contexte devient trop volumineux, l'agent doit **résumer les parties les plus récentes et pertinentes de la conversation** – en se concentrant sur vos dates de voyage actuelles et destination – et utiliser ce résumé condensé pour l'appel LLM suivant, en supprimant la conversation moins pertinente.

### Confusion du Contexte

**Qu'est-ce que c'est :** Lorsque le contexte contient des éléments inutiles, souvent sous la forme d'un trop grand nombre d’outils disponibles, ce qui fait que le modèle génère de mauvaises réponses ou appelle des outils non pertinents. Les modèles plus petits sont particulièrement sujets à cela.

**Que faire :** Mettez en œuvre une **gestion de la charge des outils** utilisant des techniques RAG. Stockez les descriptions des outils dans une base de données vectorielle et sélectionnez _uniquement_ les outils les plus pertinents pour chaque tâche spécifique. La recherche montre qu'il est préférable de limiter la sélection à moins de 30 outils.

**Exemple de Réservation de Voyage :** Votre agent a accès à des dizaines d’outils : `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, etc. Vous demandez, **"Quelle est la meilleure façon de se déplacer à Paris ?"** En raison du grand nombre d'outils, l'agent est confus et tente d'appeler `book_flight` _à l’intérieur_ de Paris, ou `rent_car` alors que vous préférez les transports publics, parce que les descriptions d'outils peuvent se chevaucher ou qu'il n'arrive pas tout simplement pas à discerner le meilleur.

**Solution :** Utilisez **RAG sur les descriptions des outils**. Lorsque vous posez une question sur se déplacer à Paris, le système récupère dynamiquement _seulement_ les outils les plus pertinents comme `rent_car` ou `public_transport_info` selon votre requête, présentant une "charge" d'outils ciblée au LLM.

### Conflit dans le Contexte

**Qu'est-ce que c'est :** Lorsque des informations contradictoires existent dans le contexte, menant à un raisonnement incohérent ou à de mauvaises réponses finales. Cela arrive souvent lorsque l'information arrive par étapes, et que des hypothèses précoces et incorrectes restent dans le contexte.

**Que faire :** Utilisez la **taille du contexte (pruning)** et le **déchargement**. La taille du contexte signifie supprimer les informations obsolètes ou contradictoires à mesure que de nouveaux détails arrivent. Le déchargement donne au modèle un espace de travail "scratchpad" séparé pour traiter l'information sans encombrer le contexte principal.


**Exemple de réservation de voyage :** Vous dites d'abord à votre agent, **"Je veux voyager en classe économique."** Plus tard dans la conversation, vous changez d'avis et dites, **"En fait, pour ce voyage, prenons la classe affaires."** Si les deux instructions restent dans le contexte, l'agent pourrait recevoir des résultats de recherche contradictoires ou être confus quant à la préférence à privilégier.

**Solution :** Mettez en œuvre une **taille du contexte**. Lorsqu'une nouvelle instruction contredit une ancienne, l'instruction plus ancienne est supprimée ou explicitement remplacée dans le contexte. Alternativement, l'agent peut utiliser un **carnet de notes** pour concilier les préférences conflictuelles avant de décider, assurant que seule l'instruction finale et cohérente guide ses actions.

## Vous avez d’autres questions sur l’ingénierie du contexte ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.
## Leçon précédente

[Protocoles agentiques](../11-agentic-protocols/README.md)

## Leçon suivante

[Mémoire pour agents IA](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->