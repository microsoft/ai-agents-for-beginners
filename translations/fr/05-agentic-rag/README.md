[![Agentic RAG](../../../translated_images/fr/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Cliquez sur l’image ci-dessus pour voir la vidéo de cette leçon)_

# Agentic RAG

Cette leçon offre un aperçu complet de l’Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigme émergent de l’IA où de grands modèles de langage (LLM) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations de sources externes. Contrairement aux modèles statiques de récupération-puis-lecture, l’Agentic RAG implique des appels itératifs au LLM, entrecoupés d’appels à des outils ou fonctions et de sorties structurées. Le système évalue les résultats, affine les requêtes, sollicite des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu’à obtenir une solution satisfaisante.

## Introduction

Cette leçon couvrira

- **Comprendre l’Agentic RAG :** Apprenez le paradigme émergent de l’IA où de grands modèles de langage (LLM) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations de sources de données externes.
- **Saisir le style itératif Maker-Checker :** Comprenez la boucle d’appels itératifs au LLM, entrecoupés d’appels à des outils ou fonctions et de sorties structurées, conçus pour améliorer la justesse et gérer les requêtes mal formées.
- **Explorer des applications pratiques :** Identifiez les scénarios où l’Agentic RAG excelle, tels que les environnements axés sur la justesse, les interactions complexes avec des bases de données et les flux de travail étendus.

## Objectifs d’apprentissage

Après avoir terminé cette leçon, vous saurez/comment comprendre :

- **Compréhension de l’Agentic RAG :** Apprenez le paradigme émergent de l’IA où de grands modèles de langage (LLM) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations de sources de données externes.
- **Style itératif Maker-Checker :** Saisissez le concept d’une boucle d’appels itératifs au LLM, entrecoupés d’appels à des outils ou fonctions et de sorties structurées, conçue pour améliorer la justesse et gérer les requêtes mal formées.
- **Maîtriser le processus de raisonnement :** Comprenez la capacité du système à maîtriser son processus de raisonnement, en décidant comment aborder les problèmes sans se baser sur des chemins pré-définis.
- **Flux de travail :** Comprenez comment un modèle agentic décide indépendamment de récupérer des rapports sur les tendances du marché, identifier des données concurrentielles, corréler des métriques internes de ventes, synthétiser les résultats, et évaluer la stratégie.
- **Boucles itératives, intégration d’outils et mémoire :** Découvrez le modèle d’interaction bouclée du système, qui maintient état et mémoire entre les étapes pour éviter les répétitions et prendre des décisions éclairées.
- **Gestion des modes d’échec et autocorrection :** Explorez les mécanismes robustes d’autocorrection du système, incluant l’itération et la nouvelle interrogation, l’utilisation d’outils de diagnostic, et le recours à la supervision humaine.
- **Limites de l’agence :** Comprenez les limites de l’Agentic RAG, en se concentrant sur l’autonomie spécifique au domaine, la dépendance à l’infrastructure, et le respect des garde-fous.
- **Cas d’usage pratiques et valeur :** Identifiez les scénarios où l’Agentic RAG est performant, comme les environnements axés sur la justesse, les interactions complexes avec des bases de données et les flux de travail étendus.
- **Gouvernance, transparence et confiance :** Apprenez l’importance de la gouvernance et de la transparence, incluant le raisonnement explicable, le contrôle des biais et la supervision humaine.

## Qu’est-ce que l’Agentic RAG ?

L’Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent de l’IA où de grands modèles de langage (LLM) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations de sources externes. Contrairement aux schémas statiques de récupération-puis-lecture, l’Agentic RAG implique des appels itératifs au LLM, entrecoupés d’appels à des outils ou fonctions et de sorties structurées. Le système évalue les résultats, affine les requêtes, sollicite des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu’à obtenir une solution satisfaisante. Ce style itératif de type « maker-checker » améliore la justesse, gère les requêtes mal formées, et garantit des résultats de haute qualité.

Le système maîtrise activement son processus de raisonnement, réécrivant les requêtes échouées, choisissant différentes méthodes de récupération et intégrant plusieurs outils — tels que la recherche vectorielle dans Azure AI Search, les bases de données SQL, ou des API personnalisées — avant de finaliser sa réponse. Ce qui distingue un système agentic est sa capacité à maîtriser son propre raisonnement. Les mises en œuvre traditionnelles de RAG reposent sur des chemins pré-définis, mais un système agentic détermine de façon autonome la séquence des étapes en fonction de la qualité des informations qu’il trouve.

## Définition de l’Agentic Retrieval-Augmented Generation (Agentic RAG)

L’Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent dans le développement de l’IA où les LLM non seulement extraient des informations de sources de données externes, mais planifient également de manière autonome leurs prochaines étapes. Contrairement aux schémas statiques de récupération-puis-lecture ou aux séquences de prompts soigneusement scriptées, l’Agentic RAG implique une boucle d’appels itératifs au LLM, entrecoupés d’appels à des outils ou fonctions et de sorties structurées. À chaque étape, le système évalue les résultats obtenus, décide s’il faut affiner ses requêtes, fait appel à des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu’à atteindre une solution satisfaisante.

Ce style itératif d’opération « maker-checker » est conçu pour améliorer la justesse, gérer les requêtes mal formées vers des bases de données structurées (ex. NL2SQL), et garantir des résultats équilibrés et de haute qualité. Plutôt que de se fier uniquement à des chaînes de prompts soigneusement conçues, le système maîtrise activement son processus de raisonnement. Il peut réécrire les requêtes qui échouent, choisir différentes méthodes de récupération, et intégrer plusieurs outils — tels que la recherche vectorielle dans Azure AI Search, les bases de données SQL, ou des API personnalisées — avant de finaliser sa réponse. Cela élimine le besoin de cadres d’orchestration excessivement complexes. À la place, une boucle relativement simple de « appel LLM → utilisation d’outil → appel LLM → … » peut produire des résultats sophistiqués et bien étayés.

![Agentic RAG Core Loop](../../../translated_images/fr/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Maîtriser le processus de raisonnement

Ce qui distingue un système « agentic » est sa capacité à maîtriser son processus de raisonnement. Les implémentations traditionnelles de RAG dépendent souvent d’un chemin pré-défini par des humains pour le modèle : une chaîne de pensée qui indique quoi récupérer et quand.
Mais lorsqu’un système est vraiment agentic, il décide en interne comment aborder le problème. Il n’exécute pas simplement un script ; il détermine de manière autonome la séquence des étapes en fonction de la qualité des informations qu’il trouve.
Par exemple, si on lui demande de créer une stratégie de lancement de produit, il ne se fie pas uniquement à un prompt qui détaille tout le processus de recherche et de prise de décision. Au lieu de cela, le modèle agentic décide de manière indépendante de :

1. Récupérer des rapports actuels sur les tendances du marché en utilisant Bing Web Grounding
2. Identifier les données pertinentes des concurrents via Azure AI Search.
3. Corréler les métriques internes historiques de ventes via Azure SQL Database.
4. Synthétiser les résultats dans une stratégie cohérente orchestrée via Azure OpenAI Service.
5. Évaluer la stratégie pour détecter des lacunes ou incohérences, puis lancer un autre cycle de récupération si nécessaire.
Toutes ces étapes — affiner les requêtes, choisir les sources, itérer jusqu’à être « satisfait » de la réponse — sont décidées par le modèle, pas scriptées à l’avance par un humain.

## Boucles itératives, intégration d’outils, et mémoire

![Tool Integration Architecture](../../../translated_images/fr/tool-integration.0f569710b5c17c10.webp)

Un système agentic repose sur un modèle d’interaction bouclée :

- **Appel initial :** L’objectif de l’utilisateur (c’est-à-dire le prompt utilisateur) est présenté au LLM.
- **Invocation d’outil :** Si le modèle identifie des informations manquantes ou des instructions ambiguës, il choisit un outil ou une méthode de récupération — comme une requête dans une base de données vectorielle (ex. recherche hybride Azure AI Search sur des données privées) ou un appel SQL structuré — pour recueillir plus de contexte.
- **Évaluation & affinement :** Après avoir examiné les données retournées, le modèle décide si l’information est suffisante. Sinon, il affine la requête, essaie un autre outil, ou ajuste son approche.
- **Répéter jusqu’à satisfaction :** Ce cycle se poursuit jusqu’à ce que le modèle détermine qu’il dispose d’assez de clarté et de preuves pour fournir une réponse finale bien raisonnée.
- **Mémoire & état :** Comme le système maintient l’état et la mémoire entre les étapes, il peut se souvenir des tentatives précédentes et de leurs résultats, évitant les boucles répétitives et prenant des décisions plus éclairées au fur et à mesure.

Au fil du temps, cela crée une compréhension évolutive, permettant au modèle de gérer des tâches complexes en plusieurs étapes sans qu’un humain doive constamment intervenir ou reformuler le prompt.

## Gestion des modes d’échec et autocorrection

L’autonomie de l’Agentic RAG inclut aussi des mécanismes robustes d’autocorrection. Lorsque le système rencontre des impasses — comme récupérer des documents non pertinents ou rencontrer des requêtes mal formées — il peut :

- **Itérer et réinterroger :** Au lieu de retourner des réponses de faible valeur, le modèle tente de nouvelles stratégies de recherche, réécrit les requêtes de base de données, ou examine des ensembles de données alternatifs.
- **Utiliser des outils de diagnostic :** Le système peut invoquer des fonctions supplémentaires conçues pour l’aider à déboguer ses étapes de raisonnement ou confirmer la justesse des données récupérées. Des outils comme Azure AI Tracing seront importants pour permettre une observabilité et une surveillance robustes.
- **Recours à la supervision humaine :** Pour les scénarios à enjeux élevés ou en cas d’échecs répétés, le modèle peut signaler une incertitude et demander une guidance humaine. Une fois que l’humain fournit un retour correctif, le modèle peut intégrer cette leçon par la suite.

Cette approche itérative et dynamique permet au modèle de s’améliorer continuellement, assurant qu’il ne s’agit pas simplement d’un système à exécution unique mais d’un système apprenant de ses erreurs durant une session donnée.

![Self Correction Mechanism](../../../translated_images/fr/self-correction.da87f3783b7f174b.webp)

## Limites de l’agence

Malgré son autonomie dans une tâche, l’Agentic RAG n’est pas équivalent à une Intelligence Artificielle Générale. Ses capacités « agentic » se limitent aux outils, sources de données et politiques fournies par des développeurs humains. Il ne peut pas inventer ses propres outils ni sortir des limites du domaine définies. Au contraire, il excelle à orchestrer dynamiquement les ressources disponibles.
Les différences clés avec des formes d’IA plus avancées incluent :

1. **Autonomie spécifique au domaine :** Les systèmes Agentic RAG sont axés sur la réalisation d’objectifs définis par l’utilisateur dans un domaine connu, employant des stratégies telles que la réécriture de requêtes ou la sélection d’outils pour améliorer les résultats.
2. **Dépendance à l’infrastructure :** Les capacités du système dépendent des outils et des données intégrés par les développeurs. Il ne peut pas dépasser ces limites sans intervention humaine.
3. **Respect des garde-fous :** Les lignes directrices éthiques, les règles de conformité et les politiques d’entreprise restent très importantes. La liberté de l’agent est toujours contrainte par des mesures de sécurité et des mécanismes de supervision (espérons-le ?)

## Cas d’usage pratiques et valeur

L’Agentic RAG brille dans les scénarios nécessitant un affinage itératif et de la précision :

1. **Environnements axés sur la justesse :** Lors de vérifications de conformité, analyses réglementaires ou recherches juridiques, le modèle agentic peut vérifier les faits à plusieurs reprises, consulter plusieurs sources, et réécrire les requêtes jusqu’à fournir une réponse rigoureusement validée.
2. **Interactions complexes avec des bases de données :** Lorsqu’il s’agit de données structurées où les requêtes échouent souvent ou nécessitent des ajustements, le système peut affiner de manière autonome ses requêtes avec Azure SQL ou Microsoft Fabric OneLake, garantissant que la récupération finale correspond à l’intention de l’utilisateur.
3. **Flux de travail étendus :** Les sessions de longue durée peuvent évoluer à mesure que de nouvelles informations apparaissent. L’Agentic RAG peut intégrer continuellement de nouvelles données, ajustant ses stratégies à mesure qu’il en apprend davantage sur le problème.

## Gouvernance, transparence et confiance

À mesure que ces systèmes deviennent plus autonomes dans leur raisonnement, la gouvernance et la transparence sont cruciales :

- **Raisonnement explicable :** Le modèle peut fournir une piste d’audit des requêtes qu’il a effectuées, des sources consultées, et des étapes de raisonnement suivies pour atteindre sa conclusion. Des outils comme Azure AI Content Safety et Azure AI Tracing / GenAIOps peuvent aider à maintenir la transparence et atténuer les risques.
- **Contrôle des biais et récupération équilibrée :** Les développeurs peuvent ajuster les stratégies de récupération pour garantir que des sources de données équilibrées et représentatives sont prises en compte, et auditer régulièrement les sorties pour détecter les biais ou les schémas déformés à l’aide de modèles personnalisés pour les organisations avancées de science des données utilisant Azure Machine Learning.
- **Supervision humaine et conformité :** Pour des tâches sensibles, la revue humaine reste essentielle. L’Agentic RAG ne remplace pas le jugement humain dans les décisions à enjeux élevés — il le complète en fournissant des options plus rigoureusement validées.

Disposer d’outils offrant un enregistrement clair des actions est essentiel. Sans cela, déboguer un processus en plusieurs étapes peut être très difficile. Voici un exemple tiré de Literal AI (l’entreprise derrière Chainlit) pour une exécution d’agent :

![AgentRunExample](../../../translated_images/fr/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusion

L’Agentic RAG représente une évolution naturelle dans la façon dont les systèmes d’IA gèrent des tâches complexes et gourmandes en données. En adoptant un modèle d’interaction bouclée, en sélectionnant de manière autonome des outils, et en affinant les requêtes jusqu’à obtenir un résultat de haute qualité, le système dépasse le simple suivi statique de prompts pour devenir un décideur plus adaptatif et conscient du contexte. Bien qu’encore limité par des infrastructures et des directives éthiques définies par l’humain, ces capacités agentic permettent des interactions IA plus riches, plus dynamiques et au final plus utiles tant pour les entreprises que pour les utilisateurs finaux.

### Vous avez d’autres questions sur l’Agentic RAG ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implémentez la Retrieval Augmented Generation (RAG) avec Azure OpenAI Service : Apprenez à utiliser vos propres données avec le service Azure OpenAI. Ce module Microsoft Learn fournit un guide complet sur la mise en œuvre de RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Évaluation des applications d’IA générative avec Microsoft Foundry : Cet article couvre l’évaluation et la comparaison des modèles sur des ensembles de données publiques, y compris les applications Agentic AI et les architectures RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Qu’est-ce que l’Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG : Guide complet de la génération augmentée par récupération basée sur agents – News from generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG : donnez un coup de pouce à votre RAG avec la reformulation de requêtes et l'auto-interrogation ! Recette IA Open-Source Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Ajout de couches agentiques à RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Le futur des assistants de connaissance : Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Comment construire des systèmes RAG agentiques</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utiliser Microsoft Foundry Agent Service pour scaler vos agents IA</a>

### Articles académiques

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine : Affinement itératif avec auto-retour</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion : Agents linguistiques avec apprentissage par renforcement verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC : Les grands modèles de langage peuvent s'auto-corriger grâce à une critique interactive par outils</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Generation augmentée par récupération agentique : une revue sur Agentic RAG</a>

## Test rapide de cet agent (optionnel)

Après avoir appris à déployer des agents dans [Leçon 16](../16-deploying-scalable-agents/README.md), vous pouvez faire un test rapide du `TravelRAGAgent` de cette leçon — en vérifiant que ses réponses restent bien ancrées dans la base de connaissances — avec [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Voir [`tests/README.md`](../tests/README.md) pour comment l’exécuter.

## Leçon précédente

[Modèle d'utilisation d'outil](../04-tool-use/README.md)

## Leçon suivante

[Construire des agents IA fiables](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->