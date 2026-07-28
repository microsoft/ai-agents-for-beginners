---
name: testing-course-samples
---
# Test des exemples du cours

Valider que les notebooks de cours et les exemples de code s'exécutent avec une configuration Microsoft Foundry / Azure OpenAI en direct.  
Le dépôt propose un script d'exécution dans  
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) qui  
exécute chaque notebook Python en mode headless et affiche une matrice PASS/FAIL.  

## Quand l'utiliser
- « Valider tous les notebooks / exemples avec mon abonnement Azure. »
- « Test rapide du cours après mise à jour des packages ou changement de modèles. »
- « Quelles leçons passent encore / échouent en direct ? »

Ne **pas** utiliser ceci pour l'action GitHub AI Smoke Test (qui valide les agents hébergés *déployés*  
— voir [`tests/README.md`](../../../tests/README.md)). Cette compétence  
exécute les notebooks localement.  

## Prérequis (vérifier d'abord)
1. **Python 3.12+** avec les dépendances du cours : `python -m pip install -r requirements.txt`  
   plus l’exécuteur : `python -m pip install nbconvert ipykernel`.  
2. **`.env` à la racine du dépôt** (copiez depuis [`.env.example`](../../../../../.env.example)) avec au minimum :  
   - `AZURE_AI_PROJECT_ENDPOINT` — point de terminaison du projet Foundry  
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)  
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un déploiement non obsolète (ex. `gpt-5-mini`)  
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) et `AZURE_OPENAI_DEPLOYMENT`  
     pour les leçons appelant directement Azure OpenAI (Leçon 06, 02-azure-openai, 14 handoff/human-loop).  
3. **`az login`** effectué — les exemples s’authentifient avec `AzureCliCredential` (Entra ID, sans clé).  
4. Vérifier que le déploiement du modèle existe :  
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.  

## Exécution de la validation
```powershell
# Tous les notebooks Python (ignore .NET, .venv, site-packages, traductions, ressources de compétences)
pwsh scripts/validate-notebooks.ps1

# Une seule leçon, avec un délai d'attente plus long par cellule
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Liste simplement ce qui serait exécuté (pas d'exécution)
pwsh scripts/validate-notebooks.ps1 -List

# Interpréteur explicite (si `python` n'est pas dans le PATH, par ex. alias du Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Le script écrit des copies exécutées, des logs par notebook, et un `results.json` dans  
`$env:TEMP\aiab-nbval` et se termine avec le nombre d’échecs.  

Les échecs transitoires (limites de quota HTTP 429 partagés par abonnement, un hic occasionnel  
du token `AzureCliCredential`, ou un timeout) sont retentés automatiquement  
(`-Retries`, par défaut 2, avec un délai `-RetryDelaySeconds` en recul, par défaut 20). Si un  
déploiement modèle donne fréquemment des 429, vérifier le quota TPM GlobalStandard de l’abonnement  
(`az cognitiveservices usage list -l <region>`) — augmenter la capacité d’un unique  
déploiement ne sert à rien si le quota *abonnement* est épuisé.  

## Interprétation des résultats
- `PASS` — le notebook a tourné de bout en bout sans erreur de cellule.  
- `FAIL` — la première ligne `*Error` / `*Exception` est montrée ; ouvrez le  
  fichier `log_*.txt` correspondant dans le répertoire de sortie pour la trace complète.  
- L’échec d’un seul notebook est limité par `-Timeout` (par cellule), ainsi une cellule avec  
  intervention humaine suspendue renvoie `StdinNotImplementedError` au lieu de rester bloquée.  

## Leçons nécessitant des ressources supplémentaires (échec attendu sans elles)
| Leçon | Exigence supplémentaire |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, clé) — dispose d’un chemin de secours en mémoire |
| 11 MCP / GitHub | Serveur MCP GitHub + PAT |
| 13 mémoire (cognee) | `cognee` configuré avec un fournisseur de modèles |
| 15 utilisation navigateur | Navigateurs Playwright installés (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agent local | Runtime local Foundry + un modèle Qwen téléchargé (sur le périphérique, sans cloud) |
| notebooks `*-dotnet-*` | Kernel .NET Interactive (exclu par défaut ; utiliser `-IncludeDotnet`) |

## Rapport de retour
Résumer sous forme de tableau PASS/FAIL regroupé par leçon. Séparer les régressions réelles  
(bugs de code/config à corriger) des lacunes d’environnement (recherche/Search manquante / Foundry Local / PAT),  
et citer les `log_*.txt` en échec pour chaque vrai échec.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->