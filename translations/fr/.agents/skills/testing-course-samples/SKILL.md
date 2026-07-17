---
name: testing-course-samples
---
# Test des exemples de cours

Validez que les cahiers de leçon et les exemples de code fonctionnent avec une configuration Microsoft Foundry / Azure OpenAI en direct.
Le dépôt propose un exécuteur dans
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) qui
exécute tous les cahiers Python en mode sans tête et affiche une matrice PASS/FAIL.

## Quand l'utiliser
- « Valider tous les cahiers / exemples avec mon abonnement Azure. »
- « Test rapide du cours après mise à jour des packages ou changement des modèles. »
- « Quelles leçons passent / échouent encore en direct ? »

Ne l’utilisez **pas** pour l’Action GitHub de Smoke Test AI (qui valide les agents *déployés*
hébergés — voir [`tests/README.md`](../../../tests/README.md)). Cette compétence
exécute les cahiers localement.

## Prérequis (vérifiez d'abord)
1. **Python 3.12+** avec les dépendances du cours : `python -m pip install -r requirements.txt`
   plus l’exécuteur : `python -m pip install nbconvert ipykernel`.
2. **`.env` à la racine du dépôt** (copiez depuis [`.env.example`](../../../../../.env.example)) avec au minimum :
   - `AZURE_AI_PROJECT_ENDPOINT` — point de terminaison du projet Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un déploiement non déprécié (ex. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) et `AZURE_OPENAI_DEPLOYMENT`
     pour les leçons qui appellent directement Azure OpenAI (Leçon 06, 02-azure-openai, 14 handoff/human-loop).
3. **Connexion `az login`** effectuée — les exemples s’authentifient avec `AzureCliCredential` (Entra ID, sans clé).
4. Vérifiez que le déploiement du modèle existe :
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Exécution de la validation
```powershell
# Tous les notebooks Python (exclut .NET, .venv, site-packages, traductions, ressources des compétences)
pwsh scripts/validate-notebooks.ps1

# Une seule leçon, avec un délai d'attente plus long par cellule
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Liste simplement ce qui s'exécuterait (pas d'exécution)
pwsh scripts/validate-notebooks.ps1 -List

# Interpréteur explicite (si `python` n'est pas dans le PATH, par ex. alias du Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Le script écrit des copies exécutées, des journaux par cahier et `results.json` dans
`$env:TEMP\aiab-nbval` et se termine avec le nombre d’échecs.

## Interprétation des résultats
- `PASS` — le cahier s’est exécuté en entier sans erreur dans les cellules.
- `FAIL` — la première ligne `*Error` / `*Exception` est affichée ; ouvrez le fichier
  `log_*.txt` correspondant dans le répertoire de sortie pour la trace complète.
- L’échec d’un seul cahier est limité par `-Timeout` (par cellule), donc une cellule en attente
  avec intervention humaine produit une `StdinNotImplementedError` plutôt que de bloquer.

## Leçons nécessitant des ressources supplémentaires (échec attendu sans elles)
| Leçon | Exigence supplémentaire |
|--------|----------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, clé) — prévoit une solution de secours en mémoire |
| 11 MCP / GitHub | Serveur MCP GitHub + PAT |
| 13 mémoire (cognee) | `cognee` configuré avec un fournisseur de modèles |
| 15 utilisation du navigateur | Navigateurs Playwright installés (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agent local | Runtime Foundry Local + modèle Qwen téléchargé (sur l’appareil, sans cloud) |
| cahiers `*-dotnet-*` | noyau .NET Interactive (exclu par défaut ; utiliser `-IncludeDotnet`) |

## Rapport
Résumez sous forme de tableau PASS/FAIL groupé par leçon. Séparez les régressions réelles
(bugs de code/configuration à corriger) des lacunes d’environnement (recherche/Foundry Local/PAT manquants),
et citez le fichier `log_*.txt` en échec pour chaque vrai échec.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->