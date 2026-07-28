# Journal des modifications

Tous les changements notables du cours **Agents IA pour Débutants** sont documentés dans ce fichier.

## [Publié] — 2026-07-14

Cette version migre le cours hors de deux modèles désormais obsolètes, migre les carnets de notes restants de la leçon vers l'API stable de Microsoft Agent Framework, et valide les carnets Python avec un déploiement Microsoft Foundry en direct.

### Modifications

- **Migration hors des modèles obsolètes (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Les modèles `gpt-4.1` et `gpt-4.1-mini` sont maintenant obsolètes (date officielle de retrait **14 octobre 2026**). Toutes les références du cours (docs, `.env.example`, carnets Python/.NET et exemples) ont été remplacées par le modèle non obsolète `gpt-5-mini`. L'exemple de routage du modèle de la leçon 16 conserve un contraste petit/grand avec `gpt-5-nano` (petit) et `gpt-5-mini` (grand). Les fichiers tiers intégrés ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), le texte historique des modèles GitHub, et les notes des capacités de la compétence `azure-openai-to-responses` ont volontairement été laissés inchangés.
- **Carnet de remise de la leçon 14 migré vers l’API stable.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) utilise désormais `agent_framework.orchestrations.HandoffBuilder` avec `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, le streaming basé sur `event.type`, et `FoundryChatClient` (remplaçant les symboles supprimés pré-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Carnet humain dans la boucle de la leçon 14 migré vers l’API stable.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) fait désormais une pause via `ctx.request_info(...)` + `@response_handler` (remplaçant `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` supprimés), construit avec `WorkflowBuilder(start_executor=..., output_executors=[...])`, génère une sortie structurée via `default_options={"response_format": ...}`, et utilise une réponse scriptée pour un fonctionnement autonome (sans `input()` bloquant).
- **Configuration de l’environnement** ([.env.example](../../.env.example)) : noms des déploiements de modèle changés en `gpt-5-mini`; ajout de `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (routage de la leçon 16) et du `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` précédemment manquant (leçon 15 utilisation navigateur).
- **Dépendances** ([requirements.txt](../../requirements.txt)) : verrous `agent-framework`, `agent-framework-foundry`, et `agent-framework-openai` à `~=1.10.0` pour un ensemble cohérent et validé (la version 1.11.0 introduit des changements expérimentaux incompatibles sur les surfaces utilisées par ces leçons).

### Notes et limitations connues

- **Validation contre Microsoft Foundry en direct.** Les carnets Python ont été exécutés sans interface graphique avec `nbconvert` sur un projet Microsoft Foundry utilisant `gpt-5-mini` (et `gpt-5-nano` pour le routage de la leçon 16). Déployez des modèles équivalents non obsolètes dans votre propre projet ; les carnets lisent le nom du déploiement via `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Certaines leçons nécessitent toujours des ressources supplémentaires.** La leçon 05 nécessite Azure AI Search; le workflow de grounding Bing de la leçon 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) a besoin d’une connexion Bing et de services hébergés Microsoft Foundry Agent; les leçons 13 (Cognee) et 17 (Foundry Local) nécessitent leurs propres environnements d’exécution.

## [Publié] — 2026-07-13

Cette version ajoute deux nouvelles leçons complétant l’arc de déploiement — montée en échelle des agents vers Microsoft Foundry et descente à un poste local — ainsi qu’un pipeline de test rapide, une navigation de cours actualisée, de nouvelles compétences pour l’apprenant, et une nouvelle image de marque.

### Ajouts

- **Leçon 16 — Déploiement d’agents évolutifs avec Microsoft Foundry.** Nouvelle leçon [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) et carnet exécutable [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) créant un agent support client en production (outils, RAG, mémoire, routage de modèle, mise en cache des réponses, validation humaine, portail d’évaluation, traçage OpenTelemetry), avec diagrammes Mermaid développement/déploiement/exécution, contrôle des connaissances, devoir, et défi.
- **Leçon 17 — Création d’agents IA locaux avec Foundry Local et Qwen.** Nouvelle leçon [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) et carnet [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construisant un assistant ingénieur entièrement sur appareil (appel de fonction Qwen via Foundry Local, outils fichiers isolés, RAG local avec Chroma, MCP local optionnel), avec diagrammes locaux / RAG local / appel d’outils, contrôle des connaissances, devoir, et défi.
- **Pipeline de test rapide.** Nouveau workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ainsi que catalogues par leçon sous [tests/](./tests/README.md) des agents déployables des leçons 01, 04, 05 et 16, avec fichier README d’index associant chaque catalogue à sa leçon et nom d’agent hébergé. La leçon 16 gagne une section « Validation d’un agent déployé avec tests rapides » ; les leçons 01/04/05 un pointeur optionnel vers les tests rapides.
- **Compétences apprenant.** Nouvelles compétences Agent sous `.agents/skills/` : [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (regroupant les indications des leçons 16 et 17), et [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (validation des exemples de carnets avec Microsoft Foundry / Azure OpenAI en direct).
- **Validateur de carnets.** Nouveau [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) qui exécute toutes les notebooks Python tête-baisse avec `nbconvert` et affiche une matrice PASS/FAIL (plus `results.json`). Il détecte automatiquement la racine du dépôt et Python, exclut par défaut les carnets non liés au cours (`.venv`, `site-packages`, `translations`, assets de modèles de compétences) et les carnets `.NET`, et supporte `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, et `-Python`.
- **Navigation dans le cours.** Ajout des liens Leçon Précédente/Suivante aux leçons 11–15 (manquants auparavant) pour chaîner tout le cours de 00 → 18 dans les deux sens.
- **Nouvelles miniatures.** Miniatures pour les leçons 16 et 17, plus image sociale du dépôt rafraîchie [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (mettant en avant les deux nouvelles leçons et l’URL `aka.ms/ai-agents-beginners`).
- **Dépendances** ([requirements.txt](../../requirements.txt)) : ajout de `foundry-local-sdk` et `chromadb` pour la leçon 17.

### Modifications

- **Tableau des leçons du [README.md](./README.md) principal :** les leçons 16 et 17 sont désormais liées à leur contenu (auparavant « Bientôt disponible ») ; image du dépôt mise à jour vers `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md) :** ajout des leçons 16 et 17 dans le guide détaillé et les parcours d’apprentissage, plus une section « Validation des agents déployés avec tests rapides ».
- **[AGENTS.md](./AGENTS.md) :** mise à jour du nombre/descriptions des leçons (00–18), ajout d’une section de validation par tests rapides, et exemples de nommage pour les leçons 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md) :** « Leçon précédente » pointe maintenant vers la leçon 17 (auparavant leçon 15), fermant la chaîne.
- **Références standardisées aux modèles non obsolètes.** Remplacement de tous les renvois `gpt-4o` / `gpt-4o-mini` à travers le cours (docs, `.env.example`, carnets Python/.NET, exemples) par `gpt-4.1-mini` — `gpt-4o` (toutes versions) sera retiré en 2026. L’exemple de routage modèle de la leçon 16 conserve un contraste petit/grand avec `gpt-4.1-mini` (petit) et `gpt-4.1` (grand). Les carnets Python sélectionnent désormais le modèle depuis les variables d’environnement (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) au lieu d’une valeur codée en dur.

### Notes et limitations connues

- **Non exécuté sur Azure en direct.** Les carnets des nouvelles leçons sont des exemples pédagogiques ; exécutez-les et validez-les avec votre propre configuration Microsoft Foundry / Foundry Local. Le workflow de test rapide requiert de déployer l’agent de la leçon et de configurer les secrets OIDC Azure (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) avec le rôle **Azure AI User** au niveau du projet Foundry.
- **La leçon 17 est locale uniquement.** Elle ne possède pas de point de terminaison Foundry Responses, donc l’action de test rapide ne s’applique pas ; validez-la en exécutant le carnet sur votre poste de travail.

## [Publié] — 2026-07-06

Cette version migre le cours vers l’**API Azure OpenAI Responses**, standardise les noms de produit sur **Microsoft Foundry** et le **Microsoft Agent Framework (MAF)**, retire GitHub Models, met à jour les versions du SDK, et ajoute un nouveau contenu sur les modèles locaux et l’hébergement d'autres frameworks sur Foundry.

### Ajouts

- **Compétence de migration** — Installation de la compétence Agent [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (depuis [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sous `.agents/skills/`, incluant ses références et script scanner.
- **Foundry Local (exécution de modèles sur appareil)** — Nouvelle section « Fournisseur alternatif : Foundry Local » dans [00-course-setup/README.md](./00-course-setup/README.md) couvrant l’installation (`winget` / `brew`), `foundry model run`, le `foundry-local-sdk`, et le branchement de `FoundryLocalManager` au Microsoft Agent Framework via `OpenAIChatClient`.
- **Hébergement d’agents LangChain / LangGraph sur Microsoft Foundry** — Nouvelle section dans [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus exemple exécutable [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) utilisant `langchain-azure-ai[hosting]` et `ResponsesHostServer` (protocole `/responses`), basé sur [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Projet Microsoft Opal** — Nouvelle section « Exemple réel : Microsoft Project Opal » dans [15-browser-use/README.md](./15-browser-use/README.md) présentant Opal comme agent d’usage informatique en entreprise et liant ce cas aux concepts du cours (humain dans la boucle, confiance/sécurité, planification, Compétences).
- **Second exemple Python de la leçon 02** — Ajout de [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (voir « Modifications » — migration depuis l’ancien carnet Semantic Kernel) et lien dans le README de la leçon.
- Ajout d’une section Modèles et Fournisseurs dans [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Modifications

- **Chat Completions → API Responses (Python).** Les exemples appelant directement le modèle ont été migrés des Chat Completions vers l’API Responses (`client.responses.create(input=..., store=False)`, `resp.output_text`), utilisant le client `OpenAI` contre le point d’extrémité stable Azure OpenAI `/openai/v1/` (sans `api_version`). Exemples concernés incluent :
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — le guide complet d’appel de fonction (schéma d’outil aplati au format Responses, résultats des outils retournés en `function_call_output`, `max_output_tokens`, etc.).

- **Modèles GitHub → Azure OpenAI.** Les modèles GitHub sont obsolètes (retrait prévu **juillet 2026**) et ne prennent pas en charge l'API Responses. Tous les chemins de code des modèles GitHub ont été convertis vers Azure OpenAI / Microsoft Foundry dans les exemples Python et .NET :
  - Python : cahiers de travail de la leçon 08 (`01`–`03`), leçon 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET : `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documents `.md` complémentaires, ainsi que les cahiers de travail/.md dotNET de la leçon 08 (`01`–`03`) utilisent désormais `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` avec `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** L'ancien fichier `02-semantic-kernel.ipynb` a été réécrit pour utiliser Microsoft Agent Framework avec Azure OpenAI (API Responses) et renommé en `02-python-agent-framework-azure-openai.ipynb`.
- **Standardisation sur `FoundryChatClient` + `as_agent`.** Le README et le code des cahiers qui mentionnaient `AzureAIProjectAgentProvider` ont été standardisés sur le modèle canonique utilisé dans la leçon 01 et les exemples du framework : `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` avec `provider.as_agent(...)`. Mis à jour dans les README et cahiers de la leçon 02 à 14 (par exemple, mémoire de la leçon 13, tous les cahiers de la leçon 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nommage des produits.** Renommage dans tout le contenu en anglais :
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Inchangé : "Azure OpenAI", "Azure AI Search", "Azure AI Inference", et les noms des variables d'environnement.)
- **Dépendances** ([requirements.txt](../../requirements.txt)) :
  - Version fixée de `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Version fixée de `openai>=1.108.1` (minimum pour l'API Responses).
  - Suppression de `azure-ai-inference` (utilisé uniquement pour les exemples migrés des modèles GitHub).
- **Configuration de l'environnement** ([.env.example](../../.env.example)) : suppression des variables GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ; ajout de `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, et optionnellement `AZURE_OPENAI_API_KEY` ; mise à jour du nommage vers Microsoft Foundry.
- **Docs** — Mise à jour des fichiers [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), et [STUDY_GUIDE.md](./STUDY_GUIDE.md) pour ce qui précède (variables d'environnement de configuration, extrait de vérification, guide fournisseur, nommage).

### Retirés

- Étapes d'intégration et variables d'environnement des modèles GitHub supprimées des docs de configuration (supplantées par Azure OpenAI / Microsoft Foundry).

### Sécurité / Confidentialité (nettoyage partage public)

- Suppression des sorties d'exécution des cahiers Jupyter qui révélaient un vrai **ID d'abonnement Azure**, noms de groupes de ressources / ressources, identifiant de connexion Bing, ainsi que des **chemins locaux fichiers et noms d'utilisateurs** des développeurs, dans :
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Vérification qu'aucune clé API, jeton, ID d'abonnement ou chemin personnel ne reste dans le contenu anglais suivi (les références restantes à `GITHUB_TOKEN` sont le jeton GitHub Actions dans les workflows et le PAT du serveur GitHub MCP dans la configuration de la leçon 11 — tous deux légitimes et sans rapport avec les modèles GitHub).

### Notes et limitations connues

- **Non exécutés/compilés.** Il s'agit d'exemples éducatifs mis à jour pour la justesse des API/nommage ; ils n'ont pas été exécutés contre des ressources Azure en direct, et les exemples .NET n'ont pas été compilés dans cet environnement. Validez dans votre propre déploiement Microsoft Foundry / Azure OpenAI.
- **Le déploiement du modèle doit prendre en charge l'API Responses.** Utilisez un déploiement tel que `gpt-4.1-mini`, `gpt-4.1`, ou un modèle `gpt-5.x`. Les modèles plus anciens prennent en charge les fonctionnalités de base de Responses mais pas toutes les fonctionnalités.
- **Version du agent-framework.** Les exemples ciblent la dernière version de MAF (`>=1.10.0`). L'appel canonique pour créer un agent est `client.as_agent(...)` ; les API ont été vérifiées par rapport à la documentation publiée du framework et une build installée. Si vous fixez une autre version, confirmez la disponibilité des méthodes (`as_agent` vs `create_agent`).
- **Le cahier de travail 04 de la leçon 08** garde intentionnellement `AzureAIAgentClient` (de `agent-framework-azure-ai`) car il utilise des outils hébergés par Microsoft Foundry Agent Service (ancrage Bing, interpréteur de code) ; il est déjà basé sur Responses.
- **Déploiement par défaut .NET.** Deux exemples de flux de travail dotNET de la leçon 08 codaient auparavant un modèle spécifique en dur ; ils utilisent désormais par défaut `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Si un exemple dépend de l'entrée multimodale/vision, définissez `AZURE_OPENAI_DEPLOYMENT` sur un modèle adapté.
- **Foundry Local** expose une API **Chat Completions** compatible OpenAI et est destinée au développement local ; utilisez Azure OpenAI / Microsoft Foundry pour l’ensemble complet des fonctionnalités de l'API Responses.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->