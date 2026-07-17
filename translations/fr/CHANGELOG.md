# Journal des modifications

Tous les changements notables du cours **Agents IA pour débutants** sont documentés dans ce fichier.

## [Publié] — 2026-07-13

Cette version ajoute deux nouvelles leçons qui complètent l’arc de déploiement — mise à l’échelle des agents vers Microsoft Foundry et réduction à un seul poste de travail — ainsi qu’un pipeline de test de fumée, une navigation actualisée du cours, de nouvelles compétences pour les apprenants et une mise à jour de la marque.

### Ajouté

- **Leçon 16 — Déploiement d’agents évolutifs avec Microsoft Foundry.** Nouvelle leçon [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) et carnet exécutable [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) construisant un agent de support client en production (outils, RAG, mémoire, routage de modèle, mise en cache des réponses, approbation humaine, porte d’évaluation, et traçage OpenTelemetry), avec diagrammes Mermaid de développement/déploiement/exécution, questions de vérification des connaissances, devoir et défi.
- **Leçon 17 — Création d’agents IA locaux avec Foundry Local et Qwen.** Nouvelle leçon [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) et carnet [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construisant un assistant ingénieur entièrement sur appareil (appel de fonction Qwen via Foundry Local, outils de fichiers sandboxés, RAG local avec Chroma, MCP local optionnel), avec diagrammes local uniquement / RAG local / appel d’outils, questions de vérification des connaissances, devoir et défi.
- **Pipeline de test de fumée.** Nouveau workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) avec catalogues par leçon sous [tests/](./tests/README.md) pour les agents déployables des Leçons 01, 04, 05 et 16, avec un README d’index associant chaque catalogue à sa leçon et nom d’agent hébergé. La Leçon 16 gagne une section "Validation d’un agent déployé avec des tests de fumée" ; les Leçons 01/04/05 gagnent un pointeur optionnel vers le test de fumée.
- **Compétences apprenants.** Nouvelles compétences Agent sous `.agents/skills/` : [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (regroupant les conseils des Leçons 16 et 17), et [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (comment valider les exemples de notebooks contre une configuration live Microsoft Foundry / Azure OpenAI).
- **Exécuteur de validation des notebooks.** Nouveau [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) qui exécute chaque notebook Python sans interface avec `nbconvert` et affiche une matrice PASS/FAIL (plus `results.json`). Il détecte automatiquement la racine du dépôt et Python, exclut par défaut les notebooks hors cours (`.venv`, `site-packages`, `translations`, ressources de modèle de compétence) et les notebooks `.NET`, et supporte `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, et `-Python`.
- **Navigation du cours.** Ajout des liens Leçon précédente / suivante aux Leçons 11–15 (auparavant absents) pour que tout le cours soit chaîné 00 → 18 dans les deux directions.
- **Nouvelles miniatures.** Miniatures des Leçons 16 et 17, plus une image sociale du dépôt rafraîchie [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (mettant en avant les deux nouvelles leçons et l’URL `aka.ms/ai-agents-beginners`).
- **Dépendances** ([requirements.txt](../../requirements.txt)) : ajout de `foundry-local-sdk` et `chromadb` pour la Leçon 17.

### Modifié

- **Tableau principal de la leçon dans [README.md](./README.md)** : les Leçons 16 et 17 renvoient désormais à leur contenu (auparavant "Bientôt disponible") ; image du dépôt mise à jour en `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)** : ajout des Leçons 16 et 17 au guide leçon par leçon et aux parcours d’apprentissage, ainsi qu’une section "Validation des agents déployés avec des tests de fumée".
- **[AGENTS.md](./AGENTS.md)** : mise à jour du compte/de la description des leçons (00–18), ajout d’une section de validation par test de fumée et exemples de nommage dans la Leçon 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)** : "Leçon précédente" pointe désormais sur la Leçon 17 (auparavant Leçon 15), bouclant la chaîne.
- **Références normalisées des modèles non dépréciés.** Remplacement de toutes les références `gpt-4o` / `gpt-4o-mini` dans le cours (docs, `.env.example`, notebooks Python/.NET et exemples) par `gpt-4.1-mini` — `gpt-4o` (toutes versions) sera retiré en 2026. L’exemple de routage du modèle de la Leçon 16 conserve un contraste petit/grand utilisant `gpt-4.1-mini` (petit) et `gpt-4.1` (grand). Les notebooks Python sélectionnent désormais le modèle à partir des variables d’environnement (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) au lieu d’un nom codé en dur.

### Notes et limitations connues

- **Non exécuté contre Azure live.** Les notebooks des nouvelles leçons sont des exemples pédagogiques ; exécutez-les et validez-les contre votre propre configuration Microsoft Foundry / Foundry Local. Le workflow de test de fumée nécessite de déployer l’agent de la leçon et configurer les secrets Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) avec le rôle **Azure AI User** au niveau du projet Foundry.
- **La Leçon 17 est uniquement locale.** Elle ne dispose pas de point de terminaison Foundry Responses, donc l’action de test de fumée ne s’applique pas ; validez-la en exécutant le notebook sur votre poste de travail.

## [Publié] — 2026-07-06

Cette version migre le cours vers l’**API Azure OpenAI Responses**, standardise la dénomination produit sur **Microsoft Foundry** et le **Microsoft Agent Framework (MAF)**, retire GitHub Models, met à jour les versions des SDK, et ajoute du contenu sur les modèles locaux et l’hébergement d’autres frameworks sur Foundry.

### Ajouté

- **Compétence de migration** — Installation de la compétence d’agent [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (depuis [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sous `.agents/skills/`, incluant ses références et script de scanner.
- **Foundry Local (exécution de modèles sur appareil)** — Nouvelle section "Fournisseur alternatif : Foundry Local" dans [00-course-setup/README.md](./00-course-setup/README.md) couvrant l’installation (`winget` / `brew`), `foundry model run`, le `foundry-local-sdk` et le raccordement de `FoundryLocalManager` au Microsoft Agent Framework via `OpenAIChatClient`.
- **Hébergement d’agents LangChain / LangGraph sur Microsoft Foundry** — Nouvelle section dans [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) et exemple exécutable [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) utilisant `langchain-azure-ai[hosting]` et `ResponsesHostServer` (protocole `/responses`), basé sur [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nouvelle section "Exemple réel : Microsoft Project Opal" dans [15-browser-use/README.md](./15-browser-use/README.md) présentant Opal comme un agent d’utilisation informatique en entreprise et le reliant aux concepts du cours (humain en boucle, confiance/sécurité, planification, Compétences).
- **Second exemple Python pour la Leçon 02** — Ajout de [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (voir "Modifié" — migration de l’ancien notebook Semantic Kernel) et lien dans le README de la leçon.
- **Section Modèles et Fournisseurs** ajoutée à [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Modifié

- **Chat Completions → Responses API (Python).** Les exemples qui appelaient le modèle directement ont été migrés de Chat Completions à l’API Responses (`client.responses.create(input=..., store=False)`, `resp.output_text`) en utilisant le client `OpenAI` contre le point de terminaison Azure OpenAI stable `/openai/v1/` (sans `api_version`). Exemples concernés :
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — parcours complet de l’appel de fonction (schéma d’outil aplati au format Responses, résultats d’outil retournés comme `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models est déprécié (retrait en **juillet 2026**) et ne supporte pas l’API Responses. Tous les chemins de code GitHub Models ont été convertis à Azure OpenAI / Microsoft Foundry dans les exemples Python et .NET :
  - Python : notebooks de workflow de la Leçon 08 (`01`–`03`), Leçon 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET : `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + docs `.md` associées, et notebooks/`.md` de workflow dotNET de la Leçon 08 (`01`–`03`) utilisant désormais `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` avec `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** L’ancien `02-semantic-kernel.ipynb` a été réécrit pour utiliser Microsoft Agent Framework avec Azure OpenAI (API Responses) et renommé en `02-python-agent-framework-azure-openai.ipynb`.
- **Standardisation sur `FoundryChatClient` + `as_agent`.** README et code de notebooks qui référençaient `AzureAIProjectAgentProvider` ont été standardisés sur le modèle canonique utilisé par la Leçon 01 et les exemples du framework lui-même : `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` avec `provider.as_agent(...)`. Mise à jour dans les README et notebooks des Leçons 02–14 (par ex., mémoire Leçon 13, tous les notebooks de la Leçon 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Dénomination produit.** Renommage dans tout le contenu en anglais :
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Non modifié : "Azure OpenAI", "Azure AI Search", "Azure AI Inference", et noms des variables d’environnement.)
- **Dépendances** ([requirements.txt](../../requirements.txt)) :
  - Version figée `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Version figée `openai>=1.108.1` (minimum pour l’API Responses).
  - Suppression de `azure-ai-inference` (utilisé uniquement par les exemples migrés de GitHub Models).
- **Configuration d’environnement** ([.env.example](../../.env.example)) : suppression des variables GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ; ajout de `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, et optionnel `AZURE_OPENAI_API_KEY` ; mise à jour de la dénomination pour Microsoft Foundry.
- **Docs** — mise à jour de [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), et [STUDY_GUIDE.md](./STUDY_GUIDE.md) pour ce qui précède (variables d’environnement setup, extrait de vérification, guide fournisseur, noms).

### Supprimé

- Étapes d’intégration GitHub Models et variables d’environnement des docs d’installation (remplacés par Azure OpenAI / Microsoft Foundry).

### Sécurité / Confidentialité (nettoyage du partage public)

- Suppression des sorties d’exécution Jupyter notebook qui divulguaient un vrai **ID d’abonnement Azure**, noms de groupe de ressources / ressources, et ID de connexion Bing, ainsi que des **chemins de fichiers locaux et noms d’utilisateurs** des développeurs, dans :
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Vérifié qu'aucune clé API, token, ID d'abonnement ou chemin personnel ne subsiste dans le contenu anglais suivi (les références `GITHUB_TOKEN` restantes correspondent au token GitHub Actions dans les workflows et au PAT serveur GitHub MCP dans la configuration de la leçon 11 — tous deux légitimes et sans rapport avec GitHub Models).

### Notes et limitations connues

- **Non exécutés/compilés.** Ce sont des exemples éducatifs mis à jour pour la correction API/nommage ; ils n’ont pas été lancés contre des ressources Azure actives, et les exemples .NET n’ont pas été compilés dans cet environnement. Validez avec votre propre déploiement Microsoft Foundry / Azure OpenAI.
- **Le déploiement du modèle doit supporter l’API Responses.** Utilisez un déploiement tel que `gpt-4.1-mini`, `gpt-4.1`, ou un modèle `gpt-5.x`. Les modèles plus anciens prennent en charge les fonctionnalités principales de Responses mais pas toutes les options.
- **Version du agent-framework.** Les exemples ciblent la dernière version MAF (`>=1.10.0`). L’appel canonique pour créer un agent est `client.as_agent(...)` ; les API ont été validées avec la documentation publiée du framework et une version installée. Si vous fixez une autre version, confirmez la disponibilité des méthodes (`as_agent` vs `create_agent`).
- **Le notebook workflow de la leçon 08, exemple 04** garde intentionnellement `AzureAIAgentClient` (depuis `agent-framework-azure-ai`) car il utilise des outils hébergés du Microsoft Foundry Agent Service (Bing grounding, interprète de code) ; il est déjà basé sur Responses.
- **Déploiement par défaut .NET.** Deux exemples de workflow dotNET de la leçon 08 avaient auparavant un modèle spécifique codé en dur ; ils utilisent désormais par défaut `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Si un exemple nécessite une entrée multimodale/vision, configurez `AZURE_OPENAI_DEPLOYMENT` sur un modèle approprié.
- **Foundry Local** expose un endpoint **Chat Completions** compatible OpenAI et est destiné au développement local ; utilisez Azure OpenAI / Microsoft Foundry pour l’ensemble complet des fonctionnalités de l’API Responses.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->