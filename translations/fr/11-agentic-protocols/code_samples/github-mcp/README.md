# Exemple de serveur Github MCP

## Description

Ceci est une démo créée pour le Hackathon AI Agents organisé par le Microsoft Reactor.

L'outil est utilisé pour recommander des projets de hackathon basés sur les repos Github d'un utilisateur.
Cela se fait par :

1. **Agent Github** - Utilisation du serveur Github MCP pour récupérer les repos et les informations associées.
2. **Agent Hackathon** - Prend les données de l'agent Github et propose des idées créatives de projets pour le hackathon basées sur les projets, les langages utilisés par l'utilisateur et les pistes de projets pour le hackathon AI Agents.
3. **Agent Événements** - Basé sur la suggestion de l'agent hackathon, l'agent événements recommandera des événements pertinents issus de la série du Hackathon AI Agent.

## Exécution du code

### Variables d'environnement

Cette démo utilise Microsoft Agent Framework, Azure OpenAI Service, le serveur Github MCP et Azure AI Search.

Assurez-vous d’avoir les variables d’environnement appropriées configurées pour utiliser ces outils :

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 


## Exécution du serveur Chainlit

Pour se connecter au serveur MCP, cette démo utilise Chainlit comme interface de chat.

Pour lancer le serveur, utilisez la commande suivante dans votre terminal :

```bash
chainlit run app.py -w
```


Cela devrait démarrer votre serveur Chainlit sur `localhost:8000` ainsi que remplir votre index Azure AI Search avec le contenu de `event-descriptions.md`.

## Connexion au serveur MCP

Pour vous connecter au serveur Github MCP, sélectionnez l'icône de "prise" sous la zone de chat "Tapez votre message ici..":

![MCP Connect](../../../../../translated_images/fr/mcp-chainlit-1.7ed66d648e3cfb28.webp)

De là, vous pouvez cliquer sur "Connect an MCP" pour ajouter la commande permettant de se connecter au serveur Github MCP :

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```


Remplacez "[YOUR PERSONAL ACCESS TOKEN]" par votre jeton d'accès personnel réel.

Après la connexion, vous devriez voir un (1) à côté de l'icône de la prise pour confirmer la connexion. Sinon, essayez de redémarrer le serveur chainlit avec `chainlit run app.py -w`.

## Utilisation de la démo

Pour lancer le workflow de l'agent recommandant des projets de hackathon, vous pouvez taper un message comme :

"Recommander des projets de hackathon pour l'utilisateur Github koreyspace"

L'Agent Routeur analysera votre demande et déterminera quelle combinaison d'agents (GitHub, Hackathon et Événements) est la mieux adaptée pour traiter votre requête. Les agents collaborent pour fournir des recommandations complètes basées sur l'analyse des repos GitHub, l’idéation de projets et les événements tech pertinents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous ne saurions être tenus responsables de tout malentendu ou interprétation erronée résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->