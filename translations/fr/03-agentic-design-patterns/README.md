[![Comment concevoir de bons agents IA](../../../translated_images/fr/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_
# Principes de conception agentique pour l'IA

## Introduction

Il existe de nombreuses façons de penser la création de systèmes IA agentiques. Étant donné que l'ambiguïté est une caractéristique et non un défaut dans la conception de l'IA générative, il est parfois difficile pour les ingénieurs de savoir par où commencer. Nous avons créé un ensemble de principes de conception UX centrés sur l'humain pour permettre aux développeurs de construire des systèmes agentiques centrés sur le client afin de répondre à leurs besoins métier. Ces principes de conception ne constituent pas une architecture prescriptive mais plutôt un point de départ pour les équipes qui définissent et construisent des expériences agentiques.

En général, les agents doivent :

- Élargir et accroître les capacités humaines (brainstorming, résolution de problèmes, automatisation, etc.)
- Combler les lacunes de connaissances (me mettre à jour sur des domaines de connaissances, traduction, etc.)
- Faciliter et soutenir la collaboration de la manière dont nous, en tant qu'individus, préférons travailler avec les autres
- Faire de nous de meilleures versions de nous-mêmes (par ex., coach de vie/gestionnaire de tâches, nous aider à apprendre la régulation émotionnelle et la pleine conscience, construire la résilience, etc.)

## Ce que couvrira cette leçon

- Qu'est-ce que les principes de conception agentique
- Quelles sont les lignes directrices à suivre lors de la mise en œuvre de ces principes de conception
- Quels sont quelques exemples d'utilisation des principes de conception

## Objectifs d'apprentissage

À l'issue de cette leçon, vous serez capable de :

1. Expliquer ce que sont les principes de conception agentique
2. Expliquer les directives pour l'utilisation des principes de conception agentique
3. Comprendre comment construire un agent en utilisant les principes de conception agentique

## Les principes de conception agentique

![Principes de conception agentique](../../../translated_images/fr/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Espace)

C'est l'environnement dans lequel l'agent opère. Ces principes guident la conception des agents pour qu'ils s'engagent dans des mondes physiques et numériques.

- **Connecter, ne pas écraser** – aider à connecter les personnes à d'autres personnes, événements et connaissances exploitables pour permettre collaboration et connexion.
- Les agents aident à relier événements, connaissances et personnes.
- Les agents rapprochent les gens. Ils ne sont pas conçus pour remplacer ou diminuer les personnes.
- **Facilement accessibles mais parfois invisibles** – l'agent opère largement en arrière-plan et ne nous sollicite que lorsqu'il est pertinent et approprié.
  - L'agent est facilement découvrable et accessible pour les utilisateurs autorisés sur tout appareil ou plateforme.
  - L'agent supporte des entrées et sorties multimodales (son, voix, texte, etc.).
  - L'agent peut passer sans effort de premier plan à arrière-plan ; réagir de manière proactive ou réactive selon sa perception des besoins de l'utilisateur.
  - L'agent peut opérer sous une forme invisible, mais son chemin de processus en arrière-plan et sa collaboration avec d'autres agents sont transparents et contrôlables par l'utilisateur.

### Agent (Temps)

C'est la manière dont l'agent fonctionne dans le temps. Ces principes guident la conception des agents interagissant à travers passé, présent et futur.

- **Passé** : Refléter l'histoire qui comprend à la fois état et contexte.
  - L'agent fournit des résultats plus pertinents basés sur l'analyse de données historiques plus riches au-delà de l'événement, des personnes ou des états seuls.
  - L'agent crée des connexions à partir d'événements passés et réfléchit activement à la mémoire pour s'engager dans les situations présentes.
- **Maintenant** : Encourager plus que notifier.
  - L'agent incarne une approche complète d'interaction avec les personnes. Lorsqu'un événement se produit, l'agent va au-delà d'une simple notification statique ou autre forme statique. L'agent peut simplifier les flux ou générer dynamiquement des indices pour diriger l'attention de l'utilisateur au bon moment.
  - L'agent délivre l'information basée sur l'environnement contextuel, les changements sociaux et culturels et adaptés à l'intention de l'utilisateur.
  - L'interaction avec l'agent peut être progressive, évoluant en complexité pour autonomiser long terme les utilisateurs.
- **Futur** : S'adapter et évoluer.
  - L'agent s'adapte à divers appareils, plateformes et modalités.
  - L'agent s'adapte au comportement utilisateur, aux besoins d'accessibilité, et est librement personnalisable.
  - L'agent est façonné par et évolue à travers une interaction continue avec l'utilisateur.

### Agent (Noyau)

Ce sont les éléments clés au cœur de la conception d’un agent.

- **Accepter l'incertitude mais établir la confiance**.
  - Un certain niveau d'incertitude de l'agent est attendu. L'incertitude est un élément clé de la conception des agents.
  - La confiance et la transparence sont les fondations de la conception des agents.
  - Les humains contrôlent l’activation/désactivation de l’agent et le statut de l’agent est clairement visible en permanence.

## Les directives pour appliquer ces principes

Lorsque vous utilisez les principes de conception précédents, appliquez les directives suivantes :

1. **Transparence** : Informez l'utilisateur que l'IA est impliquée, comment elle fonctionne (y compris les actions passées) et comment donner un retour et modifier le système.
2. **Contrôle** : Permettez à l'utilisateur de personnaliser, spécifier ses préférences et personnaliser, et de garder le contrôle sur le système et ses attributs (y compris la capacité à oublier).
3. **Cohérence** : Visez des expériences cohérentes et multimodales sur les appareils et points d’accès. Utilisez des éléments UI/UX familiers lorsque possible (par ex., icône microphone pour interaction vocale) et réduisez la charge cognitive du client autant que possible (par ex., réponses concises, aides visuelles et contenu « En savoir plus »).

## Comment concevoir un agent de voyage avec ces principes et directives

Imaginez que vous concevez un agent de voyage, voici comment vous pourriez penser à utiliser les principes et directives de conception :

1. **Transparence** – Informez l'utilisateur que l'agent de voyage est un agent activé par IA. Fournissez des instructions de base sur la manière de commencer (par ex., un message « Bonjour », des exemples de prompts). Documentez clairement cela sur la page produit. Montrez la liste des prompts qu'un utilisateur a demandés auparavant. Indiquez clairement comment donner un retour (pouces levés et baissés, bouton Envoyer un retour, etc.). Articulez clairement si l’agent a des restrictions d’utilisation ou de sujet.
2. **Contrôle** – Assurez-vous qu’il soit clair comment l’utilisateur peut modifier l'agent après sa création avec des éléments comme le System Prompt. Permettez à l’utilisateur de choisir la verbosité de l’agent, son style d’écriture, et toute mise en garde sur les sujets que l’agent ne doit pas aborder. Autorisez l’utilisateur à visualiser et supprimer tous fichiers ou données associés, prompts et conversations passées.
3. **Cohérence** – Assurez-vous que les icônes pour Partager un prompt, ajouter un fichier ou une photo et taguer quelqu’un ou quelque chose soient standard et reconnaissables. Utilisez l’icône trombone pour indiquer le téléchargement/partage de fichiers avec l’agent, et une icône image pour indiquer le téléchargement de graphiques.

## Exemples de codes

- Python : [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET : [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Vous avez plus de questions sur les modèles de conception agentiques en IA ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://openai.com" target="_blank">Pratiques pour la gouvernance des systèmes d’IA agentiques | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Le projet HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Boîte à outils IA responsable</a>

## Leçon précédente

[Explorer les cadres agentiques](../02-explore-agentic-frameworks/README.md)

## Leçon suivante

[Modèle de conception pour l’usage d’outils](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->