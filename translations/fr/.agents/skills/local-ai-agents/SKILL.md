---
name: local-ai-agents
license: MIT
---
# Création d'agents IA locaux avec Foundry Local et Qwen

> Compétence compagnon pour [Leçon 17 – Création d'agents IA locaux](../../../17-creating-local-ai-agents/README.md).
> Utilisez-la pour aider un apprenant à construire un agent qui raisonne, appelle des outils et recherche
> la documentation entièrement sur sa propre machine — sans inférence cloud. Fondez chaque
> recommandation sur le contenu de la leçon et le notebook exécutable.

## Déclencheurs

Activez cette compétence lorsqu'un apprenant souhaite :
- Exécuter un agent **entièrement en local** pour des raisons de confidentialité, de coût ou d'utilisation hors connexion.
- Servir un modèle localement avec **Foundry Local** et se connecter via un endpoint compatible OpenAI.
- Utiliser un modèle **Qwen fonction-appel** pour piloter des appels d'outils locaux fiables.
- Ajouter un **RAG local** (Chroma) ou un **serveur MCP local**.
- Concevoir une stratégie de routage **hybride** locale/cloud.

## Modèle mental central

Un SLM échange la portée contre la confidentialité, le coût et l'opération hors ligne. La stratégie gagnante :
**laisser le SLM orchestrer et laisser les outils faire le travail lourd.** Le
modèle n'a pas besoin de *connaître* la base de code — il doit savoir quand appeler
`read_file` et `search_docs`. Cela joue sur la force d'un SLM (décisions limitées
comme la sélection des outils) et évite sa faiblesse (connaissances larges, raisonnements multi-sauts longs).


## Pourquoi ces éléments spécifiques

- **Foundry Local** expose un **endpoint HTTP compatible OpenAI**, donc le code d'agent cloud se transfère en changeant seulement `base_url` (et en utilisant une clé API fantôme locale). Il sélectionne aussi automatiquement la meilleure version (CPU/GPU/NPU) pour la machine.
- Les modèles **Qwen** sont entraînés pour les appels de fonctions et génèrent systématiquement des appels d'outils bien formés — c'est ce qui transforme un modèle *chat* local en un *agent* local.
- **Chroma** s'exécute en processus et stocke les vecteurs sur disque, donc toute la pipeline RAG (embeddings → stockage → récupération → raisonnement) reste locale.
- **MCP** est un transport, pas un service cloud : un serveur MCP peut fonctionner localement via `stdio`.

## Éléments essentiels d'installation

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # espace réservé local
```

~8 Go de RAM est un minimum réaliste ; un GPU/NPU aide mais n'est pas obligatoire.

## Principaux schémas à reproduire

Orientez l'apprenant vers le notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) :

- **Outils sandboxés** : chaque outil de fichier résout les chemins et rejette tout ce qui est hors d'un seul répertoire racine — même localement, un outil s'exécute avec les permissions de l'utilisateur.
- **Boucle d'appel d'outils** : enregistrer les outils avec le schéma outils OpenAI, exécuter localement les outils demandés, renvoyer les résultats, répéter jusqu'à une réponse finale.
- **RAG local** : insérer/mettre à jour des documents dans une collection Chroma ; `search_docs` retourne les top-k segments.
- **MCP local** : connexion à un serveur local via `stdio` ; limiter le périmètre à un répertoire projet et valider ses sorties.

## Routage hybride (local comme un des modèles)

| Situation | Où ça tourne |
|-----------|---------------|
| Données sensibles / hors ligne | SLM local |
| Tâche simple, limitée | SLM local (pas cher, rapide) |
| Raisonnement multi-sauts complexe sur données non sensibles | Modèle cloud |
| Panne cloud | SLM local (dégradation progressive) |

Cela reflète l'idée de routage de modèle de la Leçon 16, avec la station de travail comme une
des routes. Privilégiez les designs qui retombent sur du local pour que l'agent dégrade en
qualité plutôt que de tomber complètement en panne.

## Garde-fous pour l'assistant

- Garder chaque opération de fichier/outils limitée à un répertoire projet sandboxé.
- Ne pas envoyer de code ni de données au cloud lorsque l'objectif déclaré par l'apprenant est la confidentialité/hors ligne — garder tout le pipeline local.
- Fixer des attentes réalistes sur la qualité du SLM ; s'appuyer davantage sur les outils et RAG que sur les connaissances mémorisées du modèle.
- Noter que la Leçon 17 n'a **pas** d'endpoint Foundry Responses, donc l'action de test rapide cloud ne s'applique pas — validez en exécutant le notebook localement.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->