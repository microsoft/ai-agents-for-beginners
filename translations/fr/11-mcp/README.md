<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T11:55:29+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "fr"
}
-->
# Leçon 11 : Intégration du protocole de contexte de modèle (MCP)

## Introduction au protocole de contexte de modèle (MCP)

Le protocole de contexte de modèle (MCP) est un cadre de pointe conçu pour standardiser les interactions entre les modèles d'IA et les applications clientes. MCP agit comme un pont entre les modèles d'IA et les applications qui les utilisent, offrant une interface cohérente quel que soit le modèle sous-jacent.

Aspects clés du MCP :

- **Communication standardisée** : MCP établit un langage commun pour que les applications communiquent avec les modèles d'IA
- **Gestion améliorée du contexte** : Permet un transfert efficace des informations contextuelles aux modèles d'IA
- **Compatibilité multiplateforme** : Fonctionne avec divers langages de programmation, notamment C#, Java, JavaScript, Python et TypeScript
- **Intégration transparente** : Permet aux développeurs d'intégrer facilement différents modèles d'IA dans leurs applications

MCP est particulièrement utile dans le développement d'agents d'IA, car il permet aux agents d'interagir avec divers systèmes et sources de données via un protocole unifié, rendant les agents plus flexibles et puissants.

## Objectifs d'apprentissage
- Comprendre ce qu'est MCP et son rôle dans le développement d'agents d'IA
- Configurer et paramétrer un serveur MCP pour une intégration avec GitHub
- Construire un système multi-agents en utilisant les outils MCP
- Implémenter RAG (Retrieval Augmented Generation) avec Azure Cognitive Search

## Prérequis
- Python 3.8+
- Node.js 14+
- Abonnement Azure
- Compte GitHub
- Compréhension de base de Semantic Kernel

## Instructions de configuration

1. **Configuration de l'environnement**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurer les services Azure**
   - Créer une ressource Azure Cognitive Search
   - Configurer le service Azure OpenAI
   - Définir les variables d'environnement dans `.env`

3. **Configuration du serveur MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Structure du projet

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Composants principaux

### 1. Système multi-agents
- Agent GitHub : Analyse des dépôts
- Agent Hackathon : Recommandations de projets
- Agent Événements : Suggestions d'événements technologiques

### 2. Intégration Azure
- Cognitive Search pour l'indexation des événements
- Azure OpenAI pour l'intelligence des agents
- Implémentation du modèle RAG

### 3. Outils MCP
- Analyse des dépôts GitHub
- Inspection de code
- Extraction de métadonnées

## Analyse du code

L'exemple démontre :
1. Intégration du serveur MCP
2. Orchestration multi-agents
3. Intégration avec Azure Cognitive Search
4. Implémentation du modèle RAG

Fonctionnalités clés :
- Analyse en temps réel des dépôts GitHub
- Recommandations intelligentes de projets
- Correspondance d'événements via Azure Search
- Réponses en streaming avec Chainlit

## Exécution de l'exemple

Pour des instructions détaillées de configuration et plus d'informations, consultez le [README Exemple de serveur MCP GitHub](./code_samples/github-mcp/README.md).

1. Démarrer le serveur MCP :
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lancer l'application :
   ```bash
   chainlit run app.py -w
   ```

3. Tester l'intégration :
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Résolution des problèmes

Problèmes courants et solutions :
1. Problèmes de connexion MCP
   - Vérifiez que le serveur est en cours d'exécution
   - Vérifiez la disponibilité du port
   - Confirmez les jetons GitHub

2. Problèmes avec Azure Search
   - Validez les chaînes de connexion
   - Vérifiez l'existence de l'index
   - Confirmez le téléchargement des documents

## Prochaines étapes
- Explorer des outils MCP supplémentaires
- Implémenter des agents personnalisés
- Améliorer les capacités RAG
- Ajouter davantage de sources d'événements
- **Avancé** : Consultez [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) pour des exemples de communication entre agents

## Ressources
- [MCP pour les débutants](https://aka.ms/mcp-for-beginners)  
- [Documentation MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Docs Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Guides Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.