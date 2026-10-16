# Guide de configuration d’Azure AI Search

Ce guide vous aidera à configurer Azure AI Search en utilisant le portail Azure. Suivez les étapes ci-dessous pour créer et configurer votre service Azure AI Search.

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Un abonnement Azure. Si vous n’avez pas d’abonnement Azure, vous pouvez créer un compte gratuit sur [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Étape 1 : Créer un compte de stockage Azure

1. Suivez cette instruction, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pour créer un nouveau compte de stockage Azure.
   **NOTE** : Assurez-vous que le type de compte de stockage soit Standard General Purpose V2.

## Étape 2 : Créer un service Azure AI Search

1. Connectez-vous au [portail Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Dans le panneau de navigation à gauche, cliquez sur **Créer une ressource**.
3. Dans la barre de recherche, tapez « Azure AI Search » et sélectionnez **Azure AI Search** dans la liste des résultats.
4. Cliquez sur le bouton **Créer**.
5. Dans l’onglet **Informations de base**, fournissez les informations suivantes :
   - **Abonnement** : Sélectionnez votre abonnement Azure.
   - **Groupe de ressources** : Créez un nouveau groupe de ressources ou sélectionnez-en un existant.
   - **Nom de la ressource** : Entrez un nom unique pour votre service de recherche.
   - **Région** : Sélectionnez la région la plus proche de vos utilisateurs.
   - **Niveau tarifaire** : Choisissez un niveau tarifaire qui correspond à vos besoins. Vous pouvez commencer avec le niveau Gratuit pour les tests.
6. Cliquez sur **Revoir + créer**.
7. Vérifiez les paramètres et cliquez sur **Créer** pour créer le service de recherche.

## Étape 3 : Commencer avec Azure AI Search

1. Une fois le déploiement terminé, accédez à votre service de recherche dans le portail Azure.
2. Dans le panneau de présentation du service de recherche, copiez l’URL. Elle devrait ressembler à `https://<service-name>.search.windows.net`.
3. **(Recommandé)** Activez l’accès sans clé avec Microsoft Entra ID (RBAC) comme indiqué à l’étape 4 ci-dessous — aucune clé nécessaire. Les exemples de ce guide créent/modifient des index et téléversent des documents, ce qui nécessite les rôles **Contributeur Service de recherche** et **Contributeur Données d’index de recherche** (ou, pour l’authentification par clé, la **clé admin principale** — pas la clé de requête). Si vous ne pouvez pas utiliser RBAC, ouvrez le panneau **Paramètres > Clés** et copiez la **clé admin principale**.
4. Suivez les étapes de la page du [guide de démarrage rapide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pour créer un index, téléverser des données et effectuer une recherche.

## Étape 4 : Utiliser les outils Azure AI Search

Azure AI Search s’intègre avec divers outils pour améliorer vos capacités de recherche. Vous pouvez utiliser Azure CLI, le SDK Python, le SDK .NET et d’autres outils pour des configurations et opérations avancées.

### Utilisation d’Azure CLI

1. Installez Azure CLI en suivant les instructions sur [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Connectez-vous à Azure CLI en utilisant la commande :

   ```bash
   az login
   ```
3. **(Recommandé) Activez l’accès sans clé avec Microsoft Entra ID (RBAC) :**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show n'a pas de champ "endpoint" ; construisez l'URL à partir du nom du service.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Avec RBAC activé, les exemples Python et .NET SDK ci-dessous s’authentifient avec `DefaultAzureCredential`, qui utilise votre session `az login` lors du développement local — aucune clé admin nécessaire. Voir [Se connecter à Azure AI Search en utilisant les rôles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Alternative) Authentification par clé** — uniquement si vous ne pouvez pas utiliser RBAC, stockez également la clé admin :

#### Stocker à la fois l’endpoint et la clé API de l’instance Azure AI Search dans les variables d’environnement.

    ```bash
    # zsh/bash
    # az search service show n’a pas de champ "endpoint" ; construisez l’URL à partir du nom du service.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show n’a pas de champ "endpoint" ; construisez l’URL à partir du nom du service.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Utilisation du SDK Python

1. Installez la bibliothèque cliente Azure Cognitive Search et Azure Identity pour Python :

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Utilisez le code Python suivant pour créer un index et téléverser des documents :

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Sans clé (recommandé) : utilise votre identité `az login` via Entra ID RBAC.
    # Nécessite les rôles "Contributeur service de recherche" et "Contributeur données d’indexation de recherche".
    credential = DefaultAzureCredential()
    # Solution de repli (authentification par clé) :
    # from azure.core.credentials import AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### Utilisation du SDK .NET

1. Exécutez la commande suivante pour créer un index et téléverser des documents :

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    L’exemple .NET ci-dessous utilise `DefaultAzureCredential`, qui peut utiliser votre connexion Azure CLI via `az login` lors du développement local.

2. Voici le code .NET de `AzureSearch.cs` :

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

Pour des informations plus détaillées, consultez la documentation suivante :

- [Créer un service Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Commencer avec Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Outils Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-exemples?wt.mc_id=studentamb_258691)

## Conclusion

Vous avez configuré avec succès Azure AI Search en utilisant le portail Azure et les outils intégrés. Vous pouvez maintenant explorer des fonctionnalités et capacités plus avancées d’Azure AI Search pour améliorer vos solutions de recherche.

Pour plus d’aide, visitez la [documentation Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->