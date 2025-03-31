<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "969885aab5f923f67f134ce115fbbcaf",
  "translation_date": "2025-03-28T10:21:07+00:00",
  "source_file": "03-agentic-design-patterns\\README.md",
  "language_code": "fr"
}
-->
[![Comment concevoir de bons agents IA](../../../translated_images/lesson-3-thumbnail.fc00fd0f7e476e3f6dbe06f4c10d1590953810d345283f825e79bede5e97e6d6.fr.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_
# Principes de conception des agents IA

## Introduction

Il existe de nombreuses façons de réfléchir à la création de systèmes d'agents IA. Étant donné que l'ambiguïté est une caractéristique et non un défaut dans la conception de l'IA générative, il est parfois difficile pour les ingénieurs de savoir par où commencer. Nous avons créé un ensemble de principes de conception UX centrés sur l'humain pour permettre aux développeurs de concevoir des systèmes d'agents centrés sur le client afin de répondre à leurs besoins commerciaux. Ces principes de conception ne constituent pas une architecture prescriptive, mais plutôt un point de départ pour les équipes qui définissent et développent des expériences avec des agents.

En général, les agents doivent :

- Élargir et étendre les capacités humaines (brainstorming, résolution de problèmes, automatisation, etc.)
- Combler les lacunes en matière de connaissances (me mettre à jour sur des domaines de connaissances, traduction, etc.)
- Faciliter et soutenir la collaboration selon les façons dont nous, en tant qu'individus, préférons travailler avec les autres
- Faire de nous de meilleures versions de nous-mêmes (par exemple, coach de vie/gestionnaire de tâches, nous aider à apprendre des compétences de régulation émotionnelle et de pleine conscience, développer la résilience, etc.)

## Cette leçon abordera

- Quels sont les principes de conception des agents
- Quelles sont les directives à suivre lors de la mise en œuvre de ces principes de conception
- Quels sont quelques exemples d'utilisation de ces principes de conception

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

1. Expliquer ce que sont les principes de conception des agents
2. Expliquer les directives pour utiliser les principes de conception des agents
3. Comprendre comment créer un agent en utilisant les principes de conception des agents

## Les principes de conception des agents

![Principes de conception des agents](../../../translated_images/agentic-design-principles.9f32a64bb6e2aa5a1bdffb70111aa724058bc248b1a3dd3c6661344015604cff.fr.png)

### Agent (Espace)

C'est l'environnement dans lequel l'agent opère. Ces principes informent sur la manière de concevoir des agents pour interagir dans les mondes physiques et numériques.

- **Connecter, pas remplacer** – aider à connecter les personnes à d'autres personnes, événements et connaissances exploitables pour permettre la collaboration et le lien.
  - Les agents aident à connecter les événements, les connaissances et les personnes.
  - Les agents rapprochent les gens. Ils ne sont pas conçus pour remplacer ou diminuer l'humain.
- **Facilement accessible mais parfois invisible** – l'agent opère principalement en arrière-plan et ne nous interpelle que lorsqu'il est pertinent et approprié.
  - L'agent est facilement accessible et découvrable pour les utilisateurs autorisés sur n'importe quel appareil ou plateforme.
  - L'agent prend en charge des entrées et sorties multimodales (son, voix, texte, etc.).
  - L'agent peut passer sans effort de l'avant-plan à l'arrière-plan ; entre proactif et réactif, en fonction de sa perception des besoins de l'utilisateur.
  - L'agent peut opérer sous une forme invisible, mais son chemin de processus en arrière-plan et sa collaboration avec d'autres agents sont transparents et contrôlables par l'utilisateur.

### Agent (Temps)

C'est la façon dont l'agent opère dans le temps. Ces principes informent sur la manière de concevoir des agents interagissant à travers le passé, le présent et le futur.

- **Passé** : Réflexion sur l'histoire incluant à la fois l'état et le contexte.
  - L'agent fournit des résultats plus pertinents basés sur l'analyse de données historiques plus riches au-delà de l'événement, des personnes ou des états.
  - L'agent crée des liens avec des événements passés et réfléchit activement à la mémoire pour interagir avec des situations actuelles.
- **Présent** : Encourager plutôt que notifier.
  - L'agent adopte une approche globale pour interagir avec les personnes. Lorsqu'un événement se produit, l'agent va au-delà de la notification statique ou d'autres formalités statiques. Il peut simplifier les flux ou générer dynamiquement des indices pour attirer l'attention de l'utilisateur au bon moment.
  - L'agent fournit des informations basées sur l'environnement contextuel, les changements sociaux et culturels et adaptées à l'intention de l'utilisateur.
  - L'interaction avec l'agent peut être progressive, évoluant en complexité pour autonomiser les utilisateurs sur le long terme.
- **Futur** : S'adapter et évoluer.
  - L'agent s'adapte à divers appareils, plateformes et modalités.
  - L'agent s'adapte au comportement de l'utilisateur, aux besoins en matière d'accessibilité et est librement personnalisable.
  - L'agent est façonné par et évolue grâce à une interaction continue avec l'utilisateur.

### Agent (Noyau)

Ce sont les éléments clés au cœur de la conception d'un agent.

- **Accepter l'incertitude mais établir la confiance**.
  - Un certain niveau d'incertitude de l'agent est attendu. L'incertitude est un élément clé de la conception des agents.
  - La confiance et la transparence sont des couches fondamentales de la conception des agents.
  - Les humains contrôlent quand l'agent est activé/désactivé et le statut de l'agent est clairement visible à tout moment.

## Les directives pour mettre en œuvre ces principes

Lorsque vous utilisez les principes de conception précédents, suivez les directives suivantes :

1. **Transparence** : Informez l'utilisateur que l'IA est impliquée, comment elle fonctionne (y compris les actions passées) et comment fournir des retours et modifier le système.
2. **Contrôle** : Permettez à l'utilisateur de personnaliser, spécifier ses préférences et personnaliser, et d'avoir le contrôle sur le système et ses attributs (y compris la capacité d'oublier).
3. **Cohérence** : Visez des expériences cohérentes et multimodales sur tous les appareils et points de contact. Utilisez des éléments UI/UX familiers lorsque cela est possible (par exemple, une icône de microphone pour l'interaction vocale) et réduisez autant que possible la charge cognitive du client (par exemple, privilégiez des réponses concises, des aides visuelles et du contenu « En savoir plus »).

## Comment concevoir un agent de voyage en utilisant ces principes et directives

Imaginez que vous concevez un agent de voyage, voici comment vous pourriez penser à utiliser les principes et directives de conception :

1. **Transparence** – Informez l'utilisateur que l'agent de voyage est un agent activé par l'IA. Fournissez des instructions de base sur la façon de commencer (par exemple, un message de "Bienvenue", des exemples de commandes). Documentez clairement cela sur la page produit. Affichez la liste des commandes que l'utilisateur a posées dans le passé. Expliquez clairement comment donner des retours (pouces levés ou baissés, bouton Envoyer un retour, etc.). Articulez clairement si l'agent a des restrictions d'utilisation ou de sujet.
2. **Contrôle** – Assurez-vous qu'il est clair comment l'utilisateur peut modifier l'agent après sa création avec des éléments comme le message système. Permettez à l'utilisateur de choisir à quel point l'agent est détaillé, son style d'écriture, et toute restriction sur les sujets que l'agent ne doit pas aborder. Donnez à l'utilisateur la possibilité de visualiser et de supprimer les fichiers ou données associés, les commandes et les conversations passées.
3. **Cohérence** – Assurez-vous que les icônes pour partager une commande, ajouter un fichier ou une photo et identifier quelqu'un ou quelque chose sont standard et reconnaissables. Utilisez l'icône de trombone pour indiquer le téléchargement/le partage de fichiers avec l'agent, et une icône d'image pour indiquer le téléchargement de graphiques.

## Ressources supplémentaires

## Leçon précédente

[Explorer les cadres des agents](../02-explore-agentic-frameworks/README.md)

## Leçon suivante

[Modèle de conception pour l'utilisation d'outils](../04-tool-use/README.md)

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.