---
name: deploying-scalable-agents
license: MIT
---
# Déploiement d'agents évolutifs avec Microsoft Foundry

> Compétence complémentaire pour [Leçon 16 – Déploiement d'agents évolutifs](../../../16-deploying-scalable-agents/README.md).
> Utilisez-la pour aider un apprenant à faire passer un agent du prototype à un déploiement en production évolutif et observable.
> Appuyez chaque recommandation sur le contenu de la leçon et
> le cahier exécutable ; n'inventez pas d'API Foundry.

## Déclencheurs

Activez cette compétence lorsqu'un apprenant souhaite :
- Déployer un agent sur Microsoft Foundry en tant qu'**agent hébergé** et le rendre versionné/observable.
- Choisir entre les modèles de déploiement **client-hébergé, agent hébergé et agent-workflow**.
- Ajouter le **routage de modèle**, le **caching des réponses** ou la **concurrence limitée** pour contrôler la latence et les coûts.
- Ajouter une **porte d'évaluation** afin qu'une mauvaise version d'agent ne puisse pas être mise en production.
- Ajouter une étape d'**approbation humaine** pour les actions à haut risque.
- Instrumenter un agent avec le traçage **OpenTelemetry** pour l'observabilité en production.
- **Test de fumée** d’un agent déployé comme une barrière rapide post-déploiement.

## Modèle mental principal

Un agent en production est principalement le squelette opérationnel *autour* du modèle (~80%),
pas le modèle lui-même. Associez chaque recommandation à l'une de ces préoccupations :

| Préoccupation | Prototype → Production |
|---------|------------------------|
| Hébergement | notebook → service hébergé versionné |
| Identité | votre `az login` → identité gérée + RBAC ciblé |
| État | en mémoire → stockage de thread/mémoire externalisé |
| Échec | trace de pile → réessais, solutions de secours, alertes |
| Coût | "quelques centimes" → suivi, routage, mise en cache, budgeté |
| Qualité | inspection visuelle → porte d'évaluation automatisée |
| Confiance | vous approuvez → politique + intervention humaine |

## Modèles de déploiement (choisissez-en un, ou combinez-les)

1. **Client-hébergé** — la boucle de raisonnement s'exécute dans votre processus. Contrôle maximal ; vous gérez la montée en charge/l'état.
2. **Agent hébergé (Foundry Agent Service)** — Foundry héberge la boucle, stocke les threads, applique le RBAC/la sécurité du contenu, affiche l'agent dans le portail. Moins de contrôle, surface opérationnelle bien moindre.
3. **Agent workflow** — plusieurs agents/outils composés en un graphe avec branches, nœuds d'approbation et points de contrôle durables.

## Cycle de vie (la boucle qui livre un agent)

`créer → versionner → évaluer (porte) → déployer hébergé → observer en ligne → collecter les échecs → répéter`.
**L’évaluation hors ligne est une porte, pas une réflexion après coup** — une version ne sort pas
sauf si elle franchit le seuil. L'observabilité en ligne alimente les échecs réels
dans le jeu de tests hors ligne.

## Leviers d’échelle et de coût (par ordre de priorité)

1. **Dimensionner correctement le modèle** — utilisez le plus petit modèle qui passe la porte d’évaluation.
2. **Router par complexité** — petit modèle rapide pour les requêtes simples, grand modèle pour le vrai raisonnement (classificateur DIY ou Foundry Model Router).
3. **Cache** — servir les requêtes quasi-duplicates sans appeler le modèle.
4. **Conception sans état + concurrence limitée** — externaliser l’état ; retrier avec délai progressif.

## Modèles clés à reproduire

Orientez l'apprenant vers ceux-ci dans le notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) :

- **Gestionnaire de requêtes** : cache → routage par complexité → trace de span → exécution → cache.
- **Porte d’évaluation** : scorer un jeu de tests hors ligne ; retourner `pass_rate >= threshold` et ne déployer que si vrai.
- **Approbation humaine** : `@tool(approval_mode="always_require")` pour des actions comme les gros remboursements.
- **Traçage** : envelopper chaque requête dans `tracer.start_as_current_span(...)` et définir des attributs comme `routed.model`, `customer.id`.

## Test de fumée d’un agent déployé

Après déploiement, vérifiez que le point de terminaison répond bien (un déploiement réussi peut rester
silencieux). Utilisez l’action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
avec le catalogue dans [`tests/`](../../../tests/README.md). Le runner POST chaque
prompt à `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
et vérifie la réponse. L’identité doit avoir le rôle **Azure AI User** au
niveau du périmètre projet Foundry ; le jeton doit viser `https://ai.azure.com/`.

Superposez les portes : **test de fumée** (accessible/réactif, à chaque déploiement) → **évaluation hors ligne** (suffisamment bon pour être mis en production, avant promotion) → **évaluation en ligne** (performance réelle en continu).



## Contrôles d’entreprise

- **RBAC** : donnez à chaque agent hébergé une identité gérée avec le minimum de privilèges.
- **MCP en production** : traitez chaque serveur MCP comme une frontière non fiable — versionnez, limitez son identité, validez les sorties, limitez le débit, ne jamais exposer de secrets.

## Garde-fous pour l’assistant

- Préférez le modèle canonique `FoundryChatClient(...)` + `provider.as_agent(...)` utilisé dans tout le cours.
- Ne promettez pas de résultats Azure en direct non vérifiés ; recommandez le workflow de test de fumée pour confirmer un déploiement.
- Gardez les conseils d’évaluation et de coût liés : l’évaluation fixe le plancher de qualité, le routage/la mise en cache maintiennent les coûts proches de ce plancher.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->