# Construire des Agents d’Utilisation Informatique (CUI)

Les agents d’utilisation informatique peuvent interagir avec les sites web de la même manière qu’une personne : en ouvrant un navigateur, en inspectant la page, et en prenant la prochaine meilleure action selon ce qu’ils voient. Dans cette leçon, vous construirez un agent d’automatisation de navigateur qui recherche sur Airbnb, extrait des données structurées de listings, et identifie le séjour le moins cher à Stockholm.

La leçon combine Browser-Use pour une navigation pilotée par IA, Playwright et le Chrome DevTools Protocol (CDP) pour le contrôle du navigateur, Azure OpenAI pour le raisonnement avec vision intégrée, et Pydantic pour l’extraction structurée.

## Introduction

Cette leçon couvrira :

- Comprendre quand les agents d’utilisation informatique sont plus adaptés qu’une automatisation uniquement par API
- Combiner Browser-Use avec Playwright et CDP pour une gestion fiable du cycle de vie du navigateur
- Utiliser Azure OpenAI vision et la sortie structurée Pydantic pour extraire des données de listings depuis des pages web dynamiques
- Décider quand utiliser un flux d’automatisation du navigateur centré sur l’agent, l’acteur, ou un hybride

## Objectifs d’apprentissage

Après avoir complété cette leçon, vous saurez comment :

- Configurer Browser-Use avec Azure OpenAI et Playwright
- Construire un flux d’automatisation de navigateur qui navigue sur un site réel et gère des éléments d’interface utilisateur dynamiques
- Extraire des résultats typés à partir du contenu visible de la page et les transformer en logique métier en aval
- Choisir entre les patrons agent et acteur selon la prévisibilité de la tâche navigateur

## Exemple de Code

Cette leçon inclut un tutoriel en notebook :

- [15-browser-user.ipynb](./15-browser-user.ipynb) : Lance une session Chrome via CDP, recherche des listings Airbnb à Stockholm, extrait les prix avec la vision Browser-Use, et retourne l’option la moins chère sous forme de données structurées.

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

Définissez les variables d’environnement Azure OpenAI utilisées par le notebook :

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Facultatif : utilise la dernière version de l'API par défaut si omis
AZURE_OPENAI_API_VERSION=...
```

## Vue d’ensemble de l’architecture

Le notebook montre un flux d’automatisation du navigateur hybride :

1. Chrome démarre avec CDP activé pour que Playwright et Browser-Use partagent la même session navigateur.
2. Un agent Browser-Use gère les tâches de navigation ouvertes comme ouvrir Airbnb, fermer les pop-ups, et chercher Stockholm.
3. La page active est inspectée avec un schéma Pydantic structuré pour extraire les titres de listings, prix à la nuit, évaluations, et URLs.
4. La logique Python compare les listings extraits et met en avant le résultat le plus économique.

Cette approche conserve le raisonnement flexible basé sur la vision que Browser-Use maîtrise, tout en vous donnant un contrôle déterministe du navigateur quand vous en avez besoin.

## Points-clés et bonnes pratiques

### Quand utiliser Agent vs Acteur

| Scénario | Utiliser Agent | Utiliser Acteur |
|----------|----------------|-----------------|
| Interfaces dynamiques | Oui, l’IA s’adapte aux changements de page | Non, les sélecteurs fragiles peuvent casser |
| Structure connue | Non, un agent est plus lent qu’un contrôle direct | Oui, rapide et précis |
| Recherche d’éléments | Oui, le langage naturel fonctionne bien | Non, des sélecteurs exacts sont requis |
| Contrôle du timing | Non, moins prévisible | Oui, contrôle total des attentes et des tentatives |
| Flux complexes | Oui, gère les états d’UI inattendus | Non, requiert des branches explicites |

### Bonnes pratiques Browser-Use

1. Commencez avec un agent pour l’exploration et la navigation dynamique.
2. Passez au contrôle direct de la page quand l’interaction devient prévisible.
3. Utilisez des modèles de sortie structurés pour que les données extraites soient validées et typées.
4. Ajoutez des délais stratégiques après des actions qui déclenchent des changements visibles dans l’UI.
5. Prenez des captures d’écran pendant l’itération pour faciliter le débogage des échecs.
6. Attendez-vous à ce que les sites changent et concevez des stratégies de repli pour les pop-ups et décalages de mise en page.
7. Mélangez les patrons agent et acteur pour combiner flexibilité et précision.

### Mesures de sécurité pour les agents navigateur

Les agents navigateur opèrent sur des sites en direct, ils ont donc besoin de limites plus strictes qu’un script qui appelle une API connue. Avant de passer d’une démonstration en notebook à un flux réel, définissez les contrôles sur ce que l’agent peut voir, cliquer et soumettre.

1. **Délimitez l’environnement de navigation.** Exécutez l’agent dans un profil navigateur dédié ou sandbox, et limitez-le aux domaines nécessaires pour la tâche.
2. **Séparez observation et action.** Laissez l’agent chercher, lire et extraire les données d’abord ; requérez une étape d’approbation explicite avant qu’il soumette des formulaires, envoie des messages, réserve un voyage, effectue des achats, supprime des enregistrements ou modifie les paramètres du compte.
3. **Gardez les secrets hors des prompts et des traces.** Ne placez pas mots de passe, détails de paiement, cookies de session, ou données personnelles brutes dans le contexte du modèle. Laissez l’utilisateur prendre en charge l’authentification et anonymiser les champs sensibles dans les logs.
4. **Considérez le contenu de la page comme une entrée non fiable.** Un site peut contenir des instructions destinées à l’agent, pas à l’utilisateur. L’agent doit ignorer le texte de la page qui demande de changer l’objectif, révéler des données, désactiver les protections, ou visiter des sites non liés.
5. **Utilisez des vérifications déterministes autour des étapes risquées.** Vérifiez l’URL actuelle, le titre de la page, l’élément sélectionné, le prix, le destinataire et le résumé de l’action avec du code avant de demander à l’utilisateur d’approuver la dernière étape.
6. **Définissez des budgets et conditions d’arrêt.** Limitez le nombre d’actions, de tentatives, d’onglets, et de minutes que l’agent peut utiliser. Arrêtez-vous quand l’état de la page est ambigu plutôt que de continuer à cliquer.
7. **Enregistrez des preuves utiles, pas tout.** Gardez les résumés d’actions, les horodatages, les URLs, descriptions des éléments sélectionnés, et références aux captures d’écran pour pouvoir revoir les échecs sans stocker de contenu sensible inutile.

Dans l’exemple Airbnb, la valeur par défaut sécurisée est de rechercher les listings et extraire les prix. La connexion, le contact avec un hôte, ou la finalisation d’une réservation doivent être des actions distinctes approuvées par l’utilisateur.

### Applications réelles

- Réservation de voyages et surveillance des prix
- Comparaison de prix e-commerce et vérification des disponibilités
- Extraction structurée de sites web dynamiques
- Tests et vérifications UI sensibles à la vision
- Surveillance et alertes de sites web
- Remplissage intelligent de formulaires dans des flux multi-étapes

## Exemple réel : Microsoft Project Opal

L’agent que vous construisez dans cette leçon est une petite version locale d’un **agent d’utilisation informatique (CUI)** — un programme qui pilote un navigateur comme une personne le ferait. Microsoft apporte cette même idée à l’entreprise avec **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, une fonctionnalité dans Microsoft 365 Copilot.

Avec Project Opal, vous décrivez une tâche et l’agent travaille en votre nom en utilisant **l’utilisation informatique sur un PC Cloud Windows 365 sécurisé**, opérant à travers les applications, sites, et données basés sur navigateur de votre organisation. Il fonctionne **de manière asynchrone en arrière-plan**, et vous pouvez guider le travail ou en prendre le contrôle à tout moment. Exemples de tâches incluent :

- Gestion des demandes d’adhésion aux groupes de sécurité
- Collecte et validation des preuves d’audit pour des revues de conformité
- Tri des incidents IT (mise à jour du statut des tickets, assignation des responsables, fermeture des doublons)
- Compilation de données Excel dans un rapport financier de clôture

Opal est une référence utile pour ce à quoi ressemble un agent d’utilisation informatique **de niveau production, fiable** — et il renforce les concepts des leçons précédentes :

| Concept dans ce cours | Application par Project Opal |
|----------------------|----------------------|
| **Humain dans la boucle** (Leçon 06) | Opal fait une pause pour les identifiants de connexion, données sensibles, ou instructions ambiguës, et ne saisit jamais les mots de passe ni ne soumet des formulaires sans confirmation explicite. Vous pouvez *prendre le contrôle* et *le rendre* en cours de tâche. |
| **Agents fiables et sécurisés** (Leçons 06 & 18) | Tourne dans un PC Cloud Windows 365 isolé, est par défaut limité au navigateur (autre accès informatique bloqué via Intune), utilise *votre* identité pour n’accéder qu’à ce pour quoi vous êtes autorisé, et journalise chaque action pour auditabilité. |
| **Planification et métacognition** (Leçons 07 & 09) | Opal génère d’abord un plan pour la tâche, puis surveille sa propre réflexion à chaque étape et fait une pause en cas d’activité suspecte. |
| **Capacités / outils réutilisables** (Leçon 04) | Les **Compétences** vous permettent d’écrire des instructions pour des tâches répétables (importées d’un fichier `.md` ou créées avec Opal) et de les réutiliser dans plusieurs conversations. |

> **Disponibilité :** Project Opal est actuellement disponible pour les utilisateurs du [programme d’accès anticipé Frontier](https://adoption.microsoft.com/copilot/frontier-program/) avec un abonnement Microsoft 365 Copilot, et votre administrateur doit compléter l’installation. Étant une fonctionnalité expérimentale Frontier, les capacités peuvent évoluer avec le temps.

## Vérification des connaissances

Testez votre compréhension avant de passer à la leçon suivante.

**1. Quand un agent d’utilisation informatique basé navigateur est-il plus adapté qu’un flux uniquement API ?**

<details>
<summary>Réponse</summary>

Utilisez un agent navigateur lorsque la tâche dépend de ce qui est visible dans une interface web, que le site n’expose pas l’API nécessaire, ou que la page change suffisamment souvent pour que les APIs ou sélecteurs fixes deviennent fragiles. Si une API stable existe pour la même tâche, préférez l’API car elle est généralement plus rapide, plus facile à tester, et plus sécurisée.
</details>

**2. Dans un flux hybride, quelles parties l’agent doit-il gérer et quelles parties le code Playwright direct doit-il gérer ?**

<details>
<summary>Réponse</summary>

Laissez l’agent gérer la navigation ouverte et les états UI dynamiques, comme trouver la bonne page ou fermer les pop-ups inattendus. Passez au contrôle direct Playwright lorsque la structure de la page est connue et que l’action nécessite précision, tentatives, attentes, ou validation déterministe.
</details>

**3. L’exemple Airbnb trouve un listing que l’utilisateur pourrait vouloir réserver. Que doit-il se passer avant que le flux ne se connecte, contacte un hôte, ou complète une réservation ?**

<details>
<summary>Réponse</summary>

Le flux doit faire une pause et demander une approbation explicite de l’utilisateur. Avant la demande, il doit afficher un résumé clair du listing sélectionné, de l’URL actuelle, du prix, des dates, et de l’action prévue. La recherche et l’extraction des prix peuvent être autonomes ; l’accès au compte, les messages, achats, et réservations doivent être approuvés par l’utilisateur.
</details>

**4. Une page web dit à l’agent d’ignorer ses instructions originales, de visiter un autre site, et de révéler des identifiants sauvegardés. Comment l’agent doit-il traiter ce texte ?**

<details>
<summary>Réponse</summary>

Traitez-le comme un contenu de page non fiable, pas comme une instruction de développeur ou utilisateur. L’agent doit rester dans le domaine et la portée de tâche autorisés, refuser de révéler des secrets, et éviter de suivre des textes de page qui changent l’objectif, désactivent les protections, ou l’envoient vers des sites non liés.
</details>

**5. Quelles preuves est-il utile de conserver quand un agent navigateur s’exécute, et qu’est-il préférable d’éviter ?**

<details>
<summary>Réponse</summary>

Conservez les résumés d’actions, horodatages, URLs, descriptions des éléments sélectionnés, résultats de validation, et références aux captures d’écran pour permettre la revue d’exécution. Évitez de stocker mots de passe, détails de paiement, cookies de session, données personnelles brutes, ou contenu complet de pages sauf si une raison spécifique de conservation et de confidentialité l’exige.
</details>

## Ressources supplémentaires

- [Commencer avec Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Modèle d’intégration Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Paramètres d’acteur Browser-Use et extraction de contenu](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuration du cours](../00-course-setup/README.md)

## Leçon précédente

[Exploration du Framework Agent Microsoft](../14-microsoft-agent-framework/README.md)

## Leçon suivante

[Déploiement d’agents scalables](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->