[![Conception multi-agent](../../../translated_images/fr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Cliquez sur l'image ci‑dessus pour voir la vidéo de cette leçon)_

# Modèles de conception multi-agent

Dès que vous commencez à travailler sur un projet impliquant plusieurs agents, vous devrez envisager le modèle de conception multi-agent. Cependant, il n'est pas toujours immédiatement clair quand passer à plusieurs agents et quels sont les avantages.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Quels sont les scénarios où les multi-agents sont applicables ?
- Quels sont les avantages d'utiliser plusieurs agents plutôt qu'un seul agent effectuant plusieurs tâches ?
- Quels sont les éléments constitutifs de la mise en œuvre du modèle de conception multi-agent ?
- Comment avoir de la visibilité sur la façon dont les multiples agents interagissent les uns avec les autres ?

## Objectifs d'apprentissage

Après cette leçon, vous devriez être en mesure de :

- Identifier les scénarios où les multi-agents sont applicables
- Reconnaître les avantages d'utiliser plusieurs agents plutôt qu'un agent unique.
- Comprendre les éléments constitutifs de la mise en œuvre du modèle de conception multi-agent.

Quelle est la vision d'ensemble ?

*Les multi-agents sont un modèle de conception qui permet à plusieurs agents de travailler ensemble pour atteindre un objectif commun*.

Ce modèle est largement utilisé dans divers domaines, notamment la robotique, les systèmes autonomes et l'informatique distribuée.

## Scénarios où les multi-agents sont applicables

Alors quels scénarios sont adaptés à l'utilisation de multi-agents ? La réponse est qu'il existe de nombreux scénarios où l'emploi de plusieurs agents est bénéfique, en particulier dans les cas suivants :

- **Gros volumes de travail** : Les lourdes charges de travail peuvent être divisées en tâches plus petites et attribuées à différents agents, permettant un traitement parallèle et une exécution plus rapide. Un exemple de ceci est dans le cas d'une importante tâche de traitement de données.
- **Tâches complexes** : Les tâches complexes, comme les gros volumes de travail, peuvent être décomposées en sous-tâches plus petites et attribuées à différents agents, chacun se spécialisant dans un aspect spécifique de la tâche. Un bon exemple est dans le cas des véhicules autonomes où différents agents gèrent la navigation, la détection d'obstacles et la communication avec les autres véhicules.
- **Expertises diverses** : Différents agents peuvent posséder des expertises variées, leur permettant de gérer différents aspects d'une tâche plus efficacement qu'un seul agent. Pour ce cas, un bon exemple est dans le domaine de la santé où des agents peuvent gérer le diagnostic, les plans de traitement et la surveillance des patients.

## Avantages d'utiliser plusieurs agents plutôt qu'un agent unique

Un système à agent unique peut fonctionner correctement pour des tâches simples, mais pour des tâches plus complexes, l'utilisation de plusieurs agents peut apporter plusieurs avantages :

- **Spécialisation** : Chaque agent peut être spécialisé pour une tâche spécifique. L'absence de spécialisation dans un agent unique signifie que vous avez un agent capable de tout faire mais qui peut être confus face à une tâche complexe. Il pourrait, par exemple, finir par effectuer une tâche pour laquelle il n'est pas le mieux adapté.
- **Scalabilité** : Il est plus facile de faire évoluer les systèmes en ajoutant plus d'agents plutôt qu'en surchargeant un seul agent.
- **Tolérance aux pannes** : Si un agent échoue, les autres peuvent continuer à fonctionner, garantissant la fiabilité du système.

Prenons un exemple : réservons un voyage pour un utilisateur. Un système à agent unique devrait gérer tous les aspects du processus de réservation, de la recherche de vols à la réservation d'hôtels et de voitures de location. Pour y parvenir avec un agent unique, l'agent devrait disposer d'outils pour gérer toutes ces tâches. Cela pourrait conduire à un système complexe et monolithique difficile à maintenir et à faire évoluer. Un système multi-agent, en revanche, pourrait avoir différents agents spécialisés dans la recherche de vols, la réservation d'hôtels et la location de voitures. Cela rendrait le système plus modulaire, plus facile à maintenir et évolutif.

Comparez cela à une agence de voyage tenue par un commerce familial par rapport à une agence de voyage exploitée en franchise. Le commerce familial aurait un seul agent gérant tous les aspects du processus de réservation, tandis que la franchise aurait différents agents gérant différents aspects du processus de réservation.

## Éléments constitutifs de la mise en œuvre du modèle de conception multi-agent

Avant de pouvoir mettre en œuvre le modèle de conception multi-agent, vous devez comprendre les éléments constitutifs qui composent le modèle.

Rendons cela plus concret en regardant à nouveau l'exemple de la réservation d'un voyage pour un utilisateur. Dans ce cas, les éléments constitutifs comprendraient :

- **Communication entre agents** : Les agents chargés de trouver des vols, de réserver des hôtels et des voitures de location doivent communiquer et partager des informations sur les préférences et les contraintes de l'utilisateur. Vous devez décider des protocoles et des méthodes pour cette communication. Concrètement, cela signifie que l'agent chargé de trouver des vols doit communiquer avec l'agent chargé de réserver les hôtels pour s'assurer que l'hôtel est réservé aux mêmes dates que le vol. Cela signifie que les agents doivent partager des informations sur les dates de voyage de l'utilisateur, ce qui implique que vous devez décider *quels agents partagent des informations et comment ils les partagent*.
- **Mécanismes de coordination** : Les agents doivent coordonner leurs actions pour garantir que les préférences et contraintes de l'utilisateur sont respectées. Une préférence utilisateur pourrait être qu'il souhaite un hôtel proche de l'aéroport tandis qu'une contrainte pourrait être que les voitures de location ne sont disponibles qu'à l'aéroport. Cela signifie que l'agent en charge de la réservation d'hôtels doit se coordonner avec l'agent en charge de la réservation de voitures pour s'assurer que les préférences et contraintes de l'utilisateur sont respectées. Vous devez décider *comment les agents coordonnent leurs actions*.
- **Architecture des agents** : Les agents doivent avoir une structure interne pour prendre des décisions et apprendre de leurs interactions avec l'utilisateur. Cela signifie que l'agent chargé de trouver des vols doit disposer d'une structure interne pour décider quels vols recommander à l'utilisateur. Vous devez décider *comment les agents prennent des décisions et apprennent de leurs interactions avec l'utilisateur*. Des exemples de la manière dont un agent apprend et s'améliore pourraient être que l'agent chargé de trouver des vols utilise un modèle d'apprentissage automatique pour recommander des vols à l'utilisateur en fonction de ses préférences passées.
- **Visibilité des interactions multi-agents** : Vous devez avoir de la visibilité sur la façon dont les multiples agents interagissent les uns avec les autres. Cela signifie que vous devez disposer d'outils et de techniques pour suivre les activités et les interactions des agents. Cela peut prendre la forme d'outils de journalisation et de surveillance, d'outils de visualisation et de métriques de performance.
- **Schémas multi-agents** : Il existe différents schémas pour la mise en œuvre des systèmes multi-agents, tels que les architectures centralisées, décentralisées et hybrides. Vous devez décider du schéma qui correspond le mieux à votre cas d'utilisation.
- **Humain dans la boucle** : Dans la plupart des cas, vous aurez un humain dans la boucle et vous devez indiquer aux agents quand demander une intervention humaine. Cela peut prendre la forme d'un utilisateur demandant un hôtel ou un vol spécifique que les agents n'ont pas recommandé ou demandant une confirmation avant de réserver un vol ou un hôtel.

## Visibilité des interactions multi-agents

Il est important d'avoir de la visibilité sur la façon dont les multiples agents interagissent les uns avec les autres. Cette visibilité est essentielle pour le débogage, l'optimisation et pour garantir l'efficacité globale du système. Pour y parvenir, vous devez disposer d'outils et de techniques pour suivre les activités et les interactions des agents. Cela peut prendre la forme d'outils de journalisation et de surveillance, d'outils de visualisation et de métriques de performance.

Par exemple, dans le cas de la réservation d'un voyage pour un utilisateur, vous pourriez avoir un tableau de bord montrant l'état de chaque agent, les préférences et contraintes de l'utilisateur, et les interactions entre les agents. Ce tableau de bord pourrait afficher les dates de voyage de l'utilisateur, les vols recommandés par l'agent des vols, les hôtels recommandés par l'agent hôtel et les voitures de location recommandées par l'agent de location. Cela vous donnerait une vue claire de la façon dont les agents interagissent entre eux et si les préférences et contraintes de l'utilisateur sont respectées.

Examinons chacun de ces aspects plus en détail.

- **Outils de journalisation et de surveillance** : Vous voulez que chaque action entreprise par un agent soit journalisée. Une entrée de journal pourrait stocker des informations sur l'agent ayant effectué l'action, l'action effectuée, le moment où l'action a été effectuée et le résultat de l'action. Ces informations peuvent ensuite être utilisées pour le débogage, l'optimisation et plus encore.
- **Outils de visualisation** : Les outils de visualisation peuvent vous aider à voir les interactions entre agents de manière plus intuitive. Par exemple, vous pourriez avoir un graphe montrant le flux d'informations entre les agents. Cela pourrait vous aider à identifier les goulots d'étranglement, les inefficacités et d'autres problèmes dans le système.
- **Métriques de performance** : Les métriques de performance peuvent vous aider à suivre l'efficacité du système multi-agent. Par exemple, vous pourriez suivre le temps nécessaire pour accomplir une tâche, le nombre de tâches accomplies par unité de temps, et la précision des recommandations faites par les agents. Ces informations peuvent vous aider à identifier des domaines d'amélioration et à optimiser le système.

## Schémas multi-agents

Plongeons dans quelques schémas concrets que nous pouvons utiliser pour créer des applications multi-agents. Voici quelques schémas intéressants à considérer :

### Chat de groupe

Ce schéma est utile lorsque vous souhaitez créer une application de chat de groupe où plusieurs agents peuvent communiquer entre eux. Les cas d'utilisation typiques pour ce schéma incluent la collaboration d'équipe, le support client et les réseaux sociaux.

Dans ce schéma, chaque agent représente un utilisateur dans le chat de groupe, et les messages sont échangés entre les agents en utilisant un protocole de messagerie. Les agents peuvent envoyer des messages au chat de groupe, recevoir des messages du chat de groupe et répondre aux messages des autres agents.

Ce schéma peut être mis en œuvre en utilisant une architecture centralisée où tous les messages sont routés via un serveur central, ou une architecture décentralisée où les messages sont échangés directement.

![Chat de groupe](../../../translated_images/fr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Transfert

Ce schéma est utile lorsque vous voulez créer une application où plusieurs agents peuvent se transférer des tâches entre eux.

Les cas d'utilisation typiques pour ce schéma incluent le support client, la gestion des tâches et l'automatisation des flux de travail.

Dans ce schéma, chaque agent représente une tâche ou une étape d'un flux de travail, et les agents peuvent transférer des tâches à d'autres agents en fonction de règles prédéfinies.

![Transfert](../../../translated_images/fr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrage collaboratif

Ce schéma est utile lorsque vous voulez créer une application où plusieurs agents peuvent collaborer pour faire des recommandations aux utilisateurs.

La raison pour laquelle vous voudriez que plusieurs agents collaborent est que chaque agent peut avoir une expertise différente et contribuer au processus de recommandation de différentes manières.

Prenons un exemple où un utilisateur souhaite une recommandation sur la meilleure action à acheter en bourse.

- **Expert sectoriel** : Un agent pourrait être un expert dans un secteur spécifique.
- **Analyse technique** : Un autre agent pourrait être un expert en analyse technique.
- **Analyse fondamentale** : Et un autre agent pourrait être un expert en analyse fondamentale. En collaborant, ces agents peuvent fournir une recommandation plus complète à l'utilisateur.

![Recommandation](../../../translated_images/fr/multi-agent-filtering.d959cb129dc9f608.webp)

## Scénario : Processus de remboursement

Considérez un scénario où un client essaie d'obtenir un remboursement pour un produit, plusieurs agents peuvent être impliqués dans ce processus mais divisons-les entre agents spécifiques à ce processus et agents généraux pouvant être utilisés dans d'autres processus.

**Agents spécifiques au processus de remboursement** :

Voici quelques agents qui pourraient être impliqués dans le processus de remboursement :

- **Agent client** : Cet agent représente le client et est responsable d'initier le processus de remboursement.
- **Agent vendeur** : Cet agent représente le vendeur et est responsable du traitement du remboursement.
- **Agent paiement** : Cet agent représente le processus de paiement et est responsable du remboursement du paiement du client.
- **Agent résolution** : Cet agent représente le processus de résolution et est responsable de résoudre tout problème survenant pendant le processus de remboursement.
- **Agent conformité** : Cet agent représente le processus de conformité et est responsable de s'assurer que le processus de remboursement respecte les réglementations et les politiques.

**Agents généraux** :

Ces agents peuvent être utilisés par d'autres parties de votre entreprise.

- **Agent livraison** : Cet agent représente le processus d'expédition et est responsable de renvoyer le produit au vendeur. Cet agent peut être utilisé à la fois pour le processus de remboursement et pour l'expédition générale d'un produit via un achat, par exemple.
- **Agent feedback** : Cet agent représente le processus de retour d'information et est responsable de collecter les retours du client. Les retours peuvent être recueillis à tout moment et pas seulement pendant le processus de remboursement.
- **Agent escalade** : Cet agent représente le processus d'escalade et est responsable d'escalader les problèmes vers un niveau de support supérieur. Vous pouvez utiliser ce type d'agent pour tout processus nécessitant une escalade.
- **Agent notification** : Cet agent représente le processus de notification et est responsable d'envoyer des notifications au client à différentes étapes du processus de remboursement.
- **Agent analytique** : Cet agent représente le processus d'analyse et est responsable d'analyser les données liées au processus de remboursement.
- **Agent audit** : Cet agent représente le processus d'audit et est responsable d'auditer le processus de remboursement pour s'assurer qu'il est correctement exécuté.
- **Agent reporting** : Cet agent représente le processus de reporting et est responsable de générer des rapports sur le processus de remboursement.
- **Agent connaissance** : Cet agent représente le processus de gestion des connaissances et est responsable de maintenir une base de connaissances d'informations liées au processus de remboursement. Cet agent pourrait être compétent à la fois sur les remboursements et sur d'autres parties de votre activité.
- **Agent sécurité** : Cet agent représente le processus de sécurité et est responsable d'assurer la sécurité du processus de remboursement.
- **Agent qualité** : Cet agent représente le processus de qualité et est responsable d'assurer la qualité du processus de remboursement.

Il y a donc plusieurs agents listés précédemment, à la fois pour le processus spécifique de remboursement mais aussi pour les agents généraux qui peuvent être utilisés dans d'autres parties de votre entreprise. Espérons que cela vous donne une idée de la façon dont vous pouvez décider quels agents utiliser dans votre système multi-agent.

## Exercice

Concevez un système multi-agent pour un processus de support client. Identifiez les agents impliqués dans le processus, leurs rôles et responsabilités, et comment ils interagissent entre eux. Envisagez à la fois des agents spécifiques au processus de support client et des agents généraux pouvant être utilisés dans d'autres parties de votre entreprise.
> Réfléchissez avant de lire la solution suivante, vous pourriez avoir besoin de plus d'agents que vous ne le pensez.
> CONSEIL: Pensez aux différentes étapes du processus de support client et considérez également les agents nécessaires pour tout système.

## Solution

[Solution](./solution/solution.md)

## Vérifications des connaissances

Question: Quand devriez-vous envisager d'utiliser des multi-agents?

- [ ] A1: Lorsque vous avez une faible charge de travail et une tâche simple.
- [ ] A2: Lorsque vous avez une charge de travail importante
- [ ] A3: Lorsque vous avez une tâche simple.

[Quiz de la solution](./solution/solution-quiz.md)

## Résumé

Dans cette leçon, nous avons examiné le patron de conception multi-agent, y compris les scénarios où les multi-agents sont applicables, les avantages d'utiliser des multi-agents par rapport à un seul agent, les éléments constitutifs pour implémenter le patron de conception multi-agent, et comment obtenir de la visibilité sur la manière dont les différents agents interagissent entre eux.

### Vous avez d'autres questions sur le patron de conception multi-agent?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d'autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Documentation du Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Patrons de conception agentiques</a>


## Leçon précédente

[Conception de la planification](../07-planning-design/README.md)

## Leçon suivante

[Métacognition dans les agents IA](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avis de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous ne pouvons être tenus responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->