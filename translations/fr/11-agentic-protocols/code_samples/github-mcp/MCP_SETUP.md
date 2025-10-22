<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-28T09:59:35+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "fr"
}
-->
# Guide d'intégration du serveur MCP

## Prérequis
- Node.js installé (version 14 ou supérieure)
- Gestionnaire de paquets npm
- Environnement Python avec les dépendances nécessaires

## Étapes de configuration

1. **Installer le package du serveur MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Démarrer le serveur MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Le serveur devrait démarrer et afficher une URL de connexion.

3. **Vérifier la connexion**  
   - Recherchez l'icône de prise (🔌) dans votre interface Chainlit  
   - Un chiffre (1) devrait apparaître à côté de l'icône de prise, indiquant une connexion réussie  
   - La console devrait afficher : "Configuration du plugin GitHub terminée avec succès" (ainsi que des lignes de statut supplémentaires)

## Résolution des problèmes

### Problèmes courants

1. **Conflit de port**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solution : Changez le port en utilisant :  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problèmes d'authentification**  
   - Assurez-vous que les identifiants GitHub sont correctement configurés  
   - Vérifiez que le fichier .env contient les tokens requis  
   - Confirmez l'accès à l'API GitHub

3. **Échec de la connexion**  
   - Vérifiez que le serveur fonctionne sur le port attendu  
   - Examinez les paramètres du pare-feu  
   - Assurez-vous que l'environnement Python dispose des packages nécessaires

## Vérification de la connexion

Votre serveur MCP est correctement connecté lorsque :  
1. La console affiche "Configuration du plugin GitHub terminée avec succès"  
2. Les journaux de connexion montrent "✓ Statut de connexion MCP : Actif"  
3. Les commandes GitHub fonctionnent dans l'interface de chat

## Variables d'environnement

Requises dans votre fichier .env :  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Tester la connexion

Envoyez ce message de test dans le chat :  
```
Show me the repositories for username: [GitHub Username]
```  
Une réponse réussie affichera les informations du dépôt.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.