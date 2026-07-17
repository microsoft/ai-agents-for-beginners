# Création d'agents d'utilisation informatique (CUA)

Les agents d'utilisation informatique peuvent interagir avec les sites web de la même manière qu'une personne : en ouvrant un navigateur, en inspectant la page, et en prenant la meilleure action suivante à partir de ce qu'ils voient. Dans cette leçon, vous construirez un agent d'automatisation de navigateur qui recherche sur Airbnb, extrait des données structurées des annonces, et identifie le séjour le moins cher à Stockholm.

La leçon combine Browser-Use pour la navigation pilotée par IA, Playwright et Chrome DevTools Protocol (CDP) pour le contrôle du navigateur, Azure OpenAI pour le raisonnement activé par vision, et Pydantic pour l'extraction structurée.

## Introduction

Cette leçon couvrira :

- Comprendre quand les agents d'utilisation informatique sont plus adaptés que l'automatisation uniquement par API
- Combiner Browser-Use avec Playwright et CDP pour une gestion fiable du cycle de vie du navigateur
- Utiliser la vision Azure OpenAI et la sortie structurée Pydantic pour extraire les données des annonces à partir de pages web dynamiques
- Décider quand utiliser un workflow d'automatisation du navigateur basé sur un agent, un acteur, ou hybride

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Configurer Browser-Use avec Azure OpenAI et Playwright
- Construire un workflow d'automatisation de navigateur qui navigue sur un site web réel et gère les éléments d'interface utilisateur dynamiques
- Extraire des résultats typés à partir du contenu visible de la page et les transformer en logique métier en aval
- Choisir entre les modèles agent et acteur selon la prévisibilité de la tâche du navigateur

## Exemple de code

Cette leçon inclut un tutoriel notebook :

- [15-browser-user.ipynb](./15-browser-user.ipynb) : Lance une session Chrome via CDP, recherche les annonces Airbnb pour Stockholm, extrait les prix avec la vision Browser-Use, et retourne l'option la moins chère sous forme de données structurées.

## Prérequis

- Python 3.12+
- Déploiement Azure OpenAI configuré dans votre environnement
- Chrome ou Chromium installé localement
- Dépendances Playwright installées
- Familiarité de base avec Python asynchrone

## Installation

Installez les paquets utilisés dans le notebook :

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Définissez les variables d'environnement Azure OpenAI utilisées par le notebook :

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Optionnel : utilise la dernière version de l'API si omis
AZURE_OPENAI_API_VERSION=...
```

## Aperçu de l'architecture

Le notebook démontre un workflow d'automatisation de navigateur hybride :

1. Chrome démarre avec CDP activé afin que Playwright et Browser-Use puissent partager la même session navigateur.
2. Un agent Browser-Use gère des tâches de navigation ouvertes telles que l'ouverture d'Airbnb, la fermeture des pop-ups, et la recherche pour Stockholm.
3. La page active est inspectée avec un schéma structuré Pydantic pour extraire les titres des annonces, les prix par nuit, les évaluations, et les URLs.
4. La logique Python compare les annonces extraites et met en évidence le résultat le moins cher.

Cette approche conserve le raisonnement flexible basé sur la vision que Browser-Use maîtrise tout en vous donnant un contrôle déterministe du navigateur quand vous en avez besoin.

## Points clés et bonnes pratiques

### Quand utiliser Agent vs Acteur

| Scénario | Utiliser Agent | Utiliser Acteur |
|----------|---------------|--------------|
| Layouts dynamiques | Oui, l'IA peut s'adapter aux changements de page | Non, les sélecteurs fragiles peuvent casser |
| Structure connue | Non, un agent est plus lent qu'un contrôle direct | Oui, rapide et précis |
| Recherche d'éléments | Oui, le langage naturel fonctionne bien | Non, les sélecteurs exacts sont nécessaires |
| Contrôle du timing | Non, moins prévisible | Oui, contrôle complet des attentes et tentatives |
| Workflows complexes | Oui, gère les états UI inattendus | Non, nécessite un branchement explicite |

### Bonnes pratiques avec Browser-Use

1. Commencez avec un agent pour l'exploration et la navigation dynamique.
2. Passez au contrôle direct de la page lorsque l'interaction devient prévisible.
3. Utilisez des modèles de sortie structurés pour que les données extraites soient validées et typées.
4. Ajoutez des délais stratégiques après les actions qui déclenchent des changements visibles de l'interface.
5. Capturez des captures d'écran lors des itérations pour faciliter le débogage des échecs.
6. Prévoyez que les sites web changent et concevez des stratégies de secours pour les pop-ups et les changements de mise en page.
7. Mixez les modèles agent et acteur pour obtenir à la fois flexibilité et précision.

### Garde-fous pour la sécurité des agents de navigateur

Les agents de navigateur opèrent sur des sites web en direct, ils ont donc besoin de limites plus strictes qu'un script qui appelle uniquement une API connue. Avant de passer d'une démonstration notebook à un workflow réel, définissez les contrôles autour de ce que l'agent peut voir, cliquer et soumettre.

1. **Délimitez l'environnement de navigation.** Faites fonctionner l'agent dans un profil navigateur dédié ou une sandbox, et limitez-le aux domaines nécessaires à la tâche.
2. **Séparez l'observation de l'action.** Laissez l'agent chercher, lire, et extraire les données d'abord ; exigez une étape d'approbation explicite avant qu'il ne soumette des formulaires, envoie des messages, réserve des voyages, effectue des achats, supprime des enregistrements, ou modifie des paramètres de compte.
3. **Ne mettez pas de secrets dans les invites et traces.** Ne placez pas les mots de passe, détails de paiement, cookies de session, ou données personnelles brutes dans le contexte du modèle. Laissez l'utilisateur prendre le relais pour l'authentification et redactez les champs sensibles des journaux.
4. **Considérez le contenu de la page comme une entrée non fiable.** Un site web peut contenir des instructions destinées à l'agent, non à l'utilisateur. L'agent doit ignorer les textes de page qui lui demandent de changer son objectif, révéler des données, désactiver les protections, ou visiter des sites non liés.
5. **Utilisez des vérifications déterministes autour des étapes risquées.** Vérifiez l'URL actuelle, le titre de la page, l'élément sélectionné, le prix, le destinataire, et le résumé d'action par code avant de demander à l'utilisateur d'approuver l'étape finale.
6. **Définissez des budgets et conditions d'arrêt.** Limitez le nombre d'actions, tentatives, onglets, et minutes que l'agent peut utiliser. Arrêtez-vous lorsque l'état de la page est ambigu au lieu de continuer à cliquer.
7. **Enregistrez des preuves utiles, pas tout.** Gardez les résumés d'actions, horodatages, URLs, descriptions des éléments sélectionnés, et références des captures d'écran pour que les échecs puissent être examinés sans stocker de contenu de page sensible inutile.

Dans l'exemple Airbnb, la valeur sûre est de rechercher les annonces et extraire les prix. Se connecter, contacter un hôte, ou finaliser une réservation doit être une action distincte approuvée par l'utilisateur.

### Applications concrètes

- Réservation de voyages et suivi des prix
- Comparaison des prix et contrôles de disponibilité pour le commerce électronique
- Extraction structurée depuis des sites web dynamiques
- Tests UI et vérification grâce à la reconnaissance visuelle
- Surveillance de sites web et alertes
- Remplissage intelligent de formulaires sur des flux multi-étapes

## Exemple réel : Microsoft Project Opal

L'agent que vous construisez dans cette leçon est une petite version locale d'un **agent d'utilisation informatique (CUA)** — un programme qui pilote un navigateur comme le ferait une personne. Microsoft apporte cette même idée à l'entreprise avec **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, une fonctionnalité de Microsoft 365 Copilot.

Avec Project Opal, vous décrivez une tâche et l'agent travaille en votre nom en utilisant **l'utilisation informatique sur un PC Cloud Windows 365 sécurisé**, opérant à travers les applications, sites, et données basés sur navigateur de votre organisation. Il fonctionne **de manière asynchrone en arrière-plan**, et vous pouvez guider le travail ou prendre le contrôle à tout moment. Exemples de tâches :

- Gestion des demandes d'appartenance aux groupes de sécurité
- Collecte et validation des preuves d'audit pour les revues de conformité
- Tri des incidents IT (mise à jour du statut des tickets, assignation des propriétaires, clôture des doublons)
- Compilation de données Excel dans un rapport de clôture financière

Opal est une référence utile de ce à quoi ressemble un agent d'utilisation informatique **de qualité production et de confiance** — et il renforce les concepts des leçons précédentes :

| Concept dans ce cours | Comment Project Opal l'applique |
|---------------------|-------------------------------|
| **Humain dans la boucle** (Leçon 06) | Opal fait une pause pour les identifiants de connexion, données sensibles, ou instructions ambiguës, et ne rentre jamais les mots de passe ni ne soumet les formulaires sans confirmation explicite. Vous pouvez *prendre le contrôle* et *revenir le contrôle* en cours de tâche. |
| **Agents dignes de confiance et sécurisés** (Leçons 06 & 18) | Fonctionne dans un PC Cloud Windows 365 isolé, est par défaut limité au navigateur (autres accès à l'ordinateur bloqués via Intune), utilise *votre* identité donc n'accède qu'à ce pour quoi vous êtes autorisé, et enregistre chaque action pour auditabilité. |
| **Planification & métacognition** (Leçons 07 & 09) | Opal génère d'abord un plan pour la tâche, puis supervise son propre raisonnement à chaque étape et marque une pause s'il détecte une activité suspecte. |
| **Capacités / outils réutilisables** (Leçon 04) | Les **Compétences** vous permettent d'écrire des instructions pour des tâches répétables (importées depuis un fichier `.md` ou écrites avec Opal) et de les réutiliser dans plusieurs conversations. |

> **Disponibilité :** Project Opal est actuellement disponible aux utilisateurs du [programme d'accès anticipé Frontier](https://adoption.microsoft.com/copilot/frontier-program/) avec un abonnement Microsoft 365 Copilot, et votre administrateur doit compléter la configuration. Comme il s'agit d'une fonctionnalité expérimentale Frontier, les capacités peuvent évoluer avec le temps.

## Ressources supplémentaires

- [Commencer avec Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Modèle d'intégration Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Paramètres d'acteur Browser-Use et extraction de contenu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuration du cours](../00-course-setup/README.md)

## Leçon précédente

[Explorer Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Leçon suivante

[Déploiement d'agents évolutifs](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->