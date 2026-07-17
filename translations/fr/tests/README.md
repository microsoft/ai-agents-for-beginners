# Tests de fumée pour agent

Ce dossier contient des **catalogues de tests de fumée** pour les agents que vous créez dans le cours.
Un test de fumée est une vérification rapide et peu coûteuse qu'un **agent hébergé Microsoft Foundry déployé**
est accessible, répond, et respecte ses attentes de prompt les plus basiques.
C’est un premier filtre — pas un remplacement pour la chaîne d’évaluation complète
que vous apprenez dans [Leçon 10](../10-ai-agents-production/README.md) et
[Leçon 16](../16-deploying-scalable-agents/README.md).

Les catalogues sont utilisés par l’action GitHub [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
via le workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Comment exécuter

1. **Déployez l’agent de la leçon** sur Microsoft Foundry en tant qu’agent hébergé (voir
   la Leçon 16 pour le workflow de déploiement). Notez le **nom de l’agent** et votre
   **point de terminaison de projet Foundry**.
2. Ajoutez ces secrets de dépôt (Paramètres → Secrets et variables → Actions) :
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. L’identité fédérée
   doit avoir le rôle **Azure AI User** au **niveau du projet Foundry**.
3. Depuis l’onglet **Actions**, lancez **Smoke-test hosted agents** et choisissez le
   `tests_file` correspondant à la leçon, puis fournissez le `agent_name`
   et le `project_endpoint` correspondants.

## Catalogue → leçon → nom de l’agent

| Catalogue | Leçon | Déployer l’agent en tant que |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Introduction aux agents IA](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Utilisation d’outils](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Déploiement d’agents évolutifs](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Quelles leçons ont des tests de fumée ?

Les tests de fumée s’appliquent aux leçons où vous **déployez un agent** dont les réponses textuelles peuvent être
validées par rapport à un contenu connu. Les leçons conceptuelles, exécutées uniquement localement,
ou produisant un contenu créatif non déterministe sont intentionnellement exclues :

- **Leçon 17 (Création d’agents IA locaux)** s’exécute entièrement sur votre poste avec
  Foundry Local et n’expose **pas** de point de terminaison Foundry Responses, donc cette
  action ne s’applique pas. Validez-la en exécutant le notebook localement.
- Les leçons de théorie et de modèles de conception (02, 03, 06, 07, 09, 12) ne livrent pas un seul
  agent déployable pour les tests de fumée.

## Schéma du catalogue (référence rapide)

Chaque catalogue est un document JSON avec un tableau `tests` de premier niveau. Chaque entrée POSTe
un prompt et vérifie la réponse :

| Champ | Signification |
|-------|--------------|
| `id` | Identifiant unique de l’étape, affiché dans le journal. |
| `description` | But lisible par l’humain. |
| `prompt` | Le message envoyé à l’agent. |
| `assertions.status` | Statut HTTP attendu (par défaut 200). |
| `assertions.contains_any` | Réussite si la réponse contient au moins une des sous-chaînes. |
| `assertions.contains_all` | Réussite si la réponse contient toutes les sous-chaînes. |
| `assertions.contains_none` | Réussite si la réponse ne contient aucune de ces sous-chaînes. |
| `save_response_id_as` | Stocker l’identifiant de la réponse pour une étape ultérieure en plusieurs tours. |
| `use_previous_response_id` | Envoyer ce tour en chaînant l’identifiant de réponse sauvegardé. |

Les assertions sont des vérifications de sous-chaînes insensibles à la casse. Voir la
[documentation de l’action](https://github.com/marketplace/actions/ai-smoke-test) pour
le schéma complet, incluant les ressources de conversation gérées par Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->