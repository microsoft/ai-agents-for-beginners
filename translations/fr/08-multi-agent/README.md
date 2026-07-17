[![Conception multi-agent](../../../translated_images/fr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

# Modèles de conception multi-agent

Dès que vous commencez à travailler sur un projet impliquant plusieurs agents, vous devrez envisager le modèle de conception multi-agent. Cependant, il n'est pas toujours évident de savoir quand passer à un système multi-agent et quels en sont les avantages.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Dans quels scénarios les multi-agents sont-ils applicables ?
- Quels sont les avantages d'utiliser plusieurs agents plutôt qu'un seul agent effectuant plusieurs tâches ?
- Quels sont les éléments de base pour implémenter le modèle de conception multi-agent ?
- Comment avoir une visibilité sur la façon dont les multiples agents interagissent entre eux ?

## Objectifs d'apprentissage

Après cette leçon, vous devriez être capable de :

- Identifier les scénarios où les multi-agents sont applicables
- Reconnaître les avantages d'utiliser plusieurs agents plutôt qu'un agent unique.
- Comprendre les éléments de base pour implémenter le modèle de conception multi-agent.

Quelle est la vision d'ensemble ?

*Les multi-agents sont un modèle de conception qui permet à plusieurs agents de travailler ensemble pour atteindre un objectif commun*.

Ce modèle est largement utilisé dans divers domaines, y compris la robotique, les systèmes autonomes et l'informatique distribuée.

## Scénarios où les multi-agents sont applicables

Alors, quels scénarios sont de bons cas d'utilisation pour les multi-agents ? La réponse est qu’il existe beaucoup de situations où l’emploi de plusieurs agents est bénéfique, notamment dans les cas suivants :

- **Charges de travail importantes** : Les charges de travail importantes peuvent être divisées en tâches plus petites et attribuées à différents agents, permettant un traitement parallèle et une réalisation plus rapide. Un exemple est celui d'une grande tâche de traitement de données.
- **Tâches complexes** : Comme pour les charges de travail importantes, les tâches complexes peuvent être décomposées en sous-tâches plus petites et attribuées à différents agents, chacun spécialisé dans un aspect spécifique de la tâche. Un bon exemple est celui des véhicules autonomes où différents agents gèrent la navigation, la détection des obstacles et la communication avec d'autres véhicules.
- **Expertises diversifiées** : Différents agents peuvent avoir des expertises variées, leur permettant de gérer différents aspects d'une tâche plus efficacement qu’un agent unique. Un bon exemple est le domaine de la santé où des agents peuvent gérer le diagnostic, les plans de traitement et la surveillance du patient.

## Avantages d’utiliser plusieurs agents plutôt qu’un agent unique

Un système à agent unique peut convenir pour les tâches simples, mais pour des tâches plus complexes, l’utilisation de plusieurs agents offre plusieurs avantages :

- **Spécialisation** : Chaque agent peut être spécialisé pour une tâche spécifique. L’absence de spécialisation dans un agent unique signifie que vous avez un agent qui peut tout faire mais qui peut être confus face à une tâche complexe. Il peut par exemple finir par effectuer une tâche pour laquelle il n’est pas le plus qualifié.
- **Scalabilité** : Il est plus facile de faire évoluer un système en ajoutant des agents plutôt qu’en surchargeant un seul agent.
- **Tolérance aux pannes** : Si un agent échoue, les autres peuvent continuer à fonctionner, garantissant la fiabilité du système.

Prenons un exemple, réservons un voyage pour un utilisateur. Un système à agent unique devrait gérer tous les aspects du processus de réservation, de la recherche de vols à la réservation d'hôtels et de voitures de location. Pour réaliser cela avec un seul agent, cet agent aurait besoin d’outils pour gérer toutes ces tâches. Cela pourrait conduire à un système complexe et monolithique, difficile à maintenir et à faire évoluer. Un système multi-agent, en revanche, pourrait avoir différents agents spécialisés dans la recherche de vols, la réservation d'hôtels et de voitures de location. Cela rendrait le système plus modulaire, plus facile à maintenir et évolutif.

Comparez cela à une agence de voyage gérée par un petit commerce familial versus une agence de voyage opérée en franchise. Le commerce familial aurait un agent unique gérant tous les aspects de la réservation, tandis que la franchise aurait différents agents gérant chaque aspect du processus de réservation.

## Éléments de base pour implémenter le modèle de conception multi-agent

Avant de pouvoir implémenter le modèle multi-agent, vous devez comprendre les éléments de base qui composent ce modèle.

Rendons cela plus concret en regardant de nouveau l’exemple de la réservation d’un voyage pour un utilisateur. Dans ce cas, les éléments de base incluent :

- **Communication entre agents** : Les agents en charge de la recherche de vols, de la réservation d'hôtels et de voitures doivent communiquer et partager des informations concernant les préférences et contraintes de l’utilisateur. Concrètement, cela signifie que l’agent de recherche de vols doit communiquer avec celui de réservation d’hôtels pour garantir que l’hôtel est réservé pour les mêmes dates que le vol. Cela implique que les agents partagent des informations sur les dates de voyage de l'utilisateur, donc vous devez décider *quels agents partagent quelles informations et comment ils les partagent*.
- **Mécanismes de coordination** : Les agents doivent coordonner leurs actions pour s’assurer que les préférences et contraintes de l’utilisateur sont respectées. Par exemple, une préférence utilisateur pourrait être un hôtel proche de l’aéroport alors qu’une contrainte pourrait être que les voitures de location ne sont disponibles qu’à l’aéroport. Cela signifie que l’agent de réservation d’hôtel doit se coordonner avec l’agent de réservation de voitures pour respecter les préférences et contraintes. Vous devez alors décider *comment les agents coordonnent leurs actions*.
- **Architecture des agents** : Les agents doivent posséder une structure interne permettant de prendre des décisions et d’apprendre de leurs interactions avec l’utilisateur. Ainsi, l’agent chargé de la recherche de vols doit avoir une structure interne pour décider quels vols recommander. Vous devez alors décider *comment les agents prennent leurs décisions et apprennent de leurs interactions avec l’utilisateur*. Par exemple, un agent de recherche de vols pourrait utiliser un modèle d’apprentissage automatique pour recommander des vols en fonction des préférences passées.
- **Visibilité sur les interactions multi-agents** : Vous devez avoir une visibilité sur la façon dont les agents interagissent entre eux. Cela implique d’avoir des outils et techniques pour suivre les activités et interactions des agents. Cela peut passer par des outils de journalisation et de monitoring, des outils de visualisation et des indicateurs de performance.
- **Modèles multi-agents** : Il existe différents modèles pour implémenter des systèmes multi-agents, tels que les architectures centralisées, décentralisées et hybrides. Vous devez choisir le modèle qui convient le mieux à votre cas d’usage.
- **Humain dans la boucle** : Dans la plupart des cas, un humain intervient dans la boucle et il faut indiquer aux agents quand demander une intervention humaine. Cela peut se traduire par un utilisateur demandant un hôtel ou un vol spécifique que les agents n’ont pas recommandé, ou une demande de confirmation avant réservation.

## Visibilité sur les interactions multi-agents

Il est important que vous ayez une visibilité sur la façon dont plusieurs agents interagissent entre eux. Cette visibilité est essentielle pour déboguer, optimiser et garantir l’efficacité globale du système. Pour cela, il faut disposer d’outils et techniques pour suivre les activités et interactions des agents. Cela peut prendre la forme d’outils de journalisation et surveillance, de visualisation, et d’indicateurs de performance.

Par exemple, dans le cas d’une réservation de voyage, vous pourriez disposer d’un tableau de bord affichant l’état de chaque agent, les préférences et contraintes de l’utilisateur, ainsi que les interactions entre agents. Ce tableau de bord pourrait montrer les dates de voyage de l’utilisateur, les vols recommandés par l’agent de vol, les hôtels recommandés par l’agent hôtelier et les voitures de location recommandées par l’agent voiture. Cela vous donnerait une vue claire des interactions entre agents et si les préférences et contraintes de l’utilisateur sont respectées.

Regardons ces aspects plus en détail.

- **Outils de journalisation et de surveillance** : Vous voulez journaliser chaque action entreprise par un agent. Une entrée de journal pourrait stocker des informations sur l’agent qui a réalisé l’action, l’action elle-même, le moment où elle a été effectuée, et le résultat obtenu. Ces informations peuvent ensuite être utilisées pour déboguer, optimiser, etc.

- **Outils de visualisation** : Les outils de visualisation peuvent vous aider à voir plus intuitivement les interactions entre agents. Par exemple, vous pourriez avoir un graphique montrant le flux d’information entre agents. Cela peut aider à identifier les goulets d’étranglement, inefficacités et autres problèmes.

- **Indicateurs de performance** : Les indicateurs de performance peuvent aider à suivre l’efficacité du système multi-agent. Par exemple, vous pouvez suivre le temps nécessaire pour accomplir une tâche, le nombre de tâches achevées par unité de temps, et la précision des recommandations fournies par les agents. Ces données peuvent aider à identifier les axes d’amélioration et optimiser le système.

## Modèles multi-agent

Approfondissons quelques modèles concrets à utiliser pour créer des applications multi-agent. Voici des modèles intéressants à considérer :

### Chat de groupe

Ce modèle est utile lorsque vous souhaitez créer une application de chat de groupe où plusieurs agents peuvent communiquer entre eux. Les cas d’utilisation typiques incluent la collaboration en équipe, le support client et les réseaux sociaux.

Dans ce modèle, chaque agent représente un utilisateur dans la discussion de groupe, et les messages sont échangés entre agents via un protocole de messagerie. Les agents peuvent envoyer des messages au groupe, recevoir des messages du groupe, et répondre aux messages d’autres agents.

Ce modèle peut être implémenté avec une architecture centralisée où tous les messages passent par un serveur central, ou une architecture décentralisée où les messages sont échangés directement.

![Chat de groupe](../../../translated_images/fr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transmission de tâche

Ce modèle est utile lorsque vous souhaitez créer une application où plusieurs agents peuvent se transmettre des tâches.

Les cas d’utilisation typiques incluent le support client, la gestion des tâches et l’automatisation des flux de travail.

Dans ce modèle, chaque agent représente une tâche ou une étape d’un workflow, et les agents peuvent transmettre des tâches à d’autres agents selon des règles prédéfinies.

![Transmission de tâche](../../../translated_images/fr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrage collaboratif

Ce modèle est utile lorsque vous souhaitez créer une application où plusieurs agents collaborent pour faire des recommandations aux utilisateurs.

La raison de vouloir plusieurs agents collaboratifs est que chaque agent peut avoir une expertise différente et contribuer au processus de recommandation de manière variée.

Prenons l’exemple d’un utilisateur qui souhaite une recommandation sur la meilleure action à acheter en bourse.

- **Expert de secteur** : Un agent pourrait être expert dans un secteur spécifique.
- **Analyse technique** : Un autre agent pourrait être expert en analyse technique.
- **Analyse fondamentale** : Un autre agent encore pourrait être expert en analyse fondamentale. En collaborant, ces agents peuvent fournir une recommandation plus complète à l’utilisateur.

![Recommandation](../../../translated_images/fr/multi-agent-filtering.d959cb129dc9f608.webp)

## Scénario : Processus de remboursement

Considérez un scénario où un client cherche à obtenir un remboursement pour un produit, plusieurs agents peuvent être impliqués dans ce processus, mais divisons-les entre agents spécifiques à ce processus et agents généraux utilisables ailleurs.

**Agents spécifiques au processus de remboursement** :

Voici quelques agents qui pourraient être impliqués dans le processus de remboursement :

- **Agent client** : Cet agent représente le client et est responsable d’initier le processus de remboursement.
- **Agent vendeur** : Cet agent représente le vendeur et est responsable du traitement du remboursement.
- **Agent paiement** : Cet agent représente le processus de paiement et est responsable de rembourser le client.
- **Agent résolution** : Cet agent représente le processus de résolution et est responsable de résoudre tout problème survenant durant le processus de remboursement.
- **Agent conformité** : Cet agent représente le processus de conformité et veille à ce que le processus de remboursement respecte les réglementations et politiques.

**Agents généraux** :

Ces agents peuvent être utilisés par d’autres parties de votre entreprise.

- **Agent expédition** : Cet agent représente le processus d’expédition et est responsable du renvoi du produit au vendeur. Il peut être utilisé à la fois pour le remboursement et pour l’expédition générale d’un produit, par exemple après un achat.
- **Agent retour d’information** : Cet agent représente le processus de collecte des retours client. Les retours peuvent être collectés à tout moment, pas seulement durant le remboursement.
- **Agent escalade** : Cet agent représente le processus d’escalade et est responsable de transférer les problèmes à un niveau de support supérieur. Ce type d’agent peut être utilisé pour tout processus nécessitant une escalade.
- **Agent notification** : Cet agent représente l’envoi de notifications au client aux différentes étapes du remboursement.
- **Agent analytique** : Cet agent gère l’analyse des données liées au processus de remboursement.
- **Agent audit** : Cet agent assure l’audit du processus de remboursement pour garantir qu’il est correctement réalisé.
- **Agent reporting** : Cet agent génère des rapports sur le processus de remboursement.
- **Agent connaissance** : Cet agent maintient une base de connaissances contenant des informations liées au processus de remboursement. Il peut être informé à la fois sur les remboursements et sur d’autres aspects de votre entreprise.
- **Agent sécurité** : Cet agent veille à la sécurité du processus de remboursement.
- **Agent qualité** : Cet agent est responsable de veiller à la qualité du processus de remboursement.

Il y a donc beaucoup d’agents listés ci-dessus, à la fois pour le processus spécifique de remboursement et pour les agents généraux utilisables ailleurs dans votre entreprise. Cela vous donne une idée de comment décider quels agents utiliser dans votre système multi-agent.

## Exercice

Concevez un système multi-agent pour un processus de support client. Identifiez les agents impliqués dans le processus, leurs rôles et responsabilités, ainsi que leurs interactions. Prenez en compte à la fois les agents spécifiques au support client et les agents généraux pouvant être utilisés dans d’autres parties de votre entreprise.


> Réfléchissez un peu avant de lire la solution suivante, vous pourriez avoir besoin de plus d’agents que vous ne le pensez.

> ASTUCE : Pensez aux différentes étapes du processus de support client et considérez également les agents nécessaires pour tout système.

## Solution

[Solution](./solution/solution.md)

## Contrôles des connaissances

### Question 1

Quel scénario est le plus adapté à un système multi-agent ?

- [ ] A1 : Un bot de support répond aux questions courantes en utilisant une base de connaissances unique et un petit ensemble d’outils.
- [ ] A2 : Un flux de travail pour les remboursements nécessite des rôles distincts pour la fraude, le paiement et la conformité, chacun avec ses propres outils, et leurs résultats doivent être coordonnés.
- [ ] A3 : La même demande simple de classification arrive des milliers de fois par heure.

### Question 2

Quand un agent unique est-il généralement le meilleur choix ?

- [ ] A1 : La tâche peut être traitée avec un seul ensemble d’instructions et d’outils, sans transfert à des spécialistes.
- [ ] A2 : L’agent a accès à plus d’un outil.
- [ ] A3 : Le flux de travail nécessite des rôles distincts avec des permissions différentes et des pistes d’audit indépendantes.

[Solution quiz](./solution/solution-quiz.md)

## Résumé

Dans cette leçon, nous avons examiné le modèle de conception multi-agent, y compris les scénarios où les multi-agents sont applicables, les avantages d’utiliser plusieurs agents plutôt qu’un agent unique, les blocs de construction pour implémenter le modèle multi-agent, et comment avoir une visibilité sur la manière dont les agents multiples interagissent entre eux.

### Encore des questions sur le modèle de conception multi-agent ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentation Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Modèles de conception agentiques</a>


## Leçon précédente

[Planning Design](../07-planning-design/README.md)

## Leçon suivante

[Métacognition dans les agents IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->