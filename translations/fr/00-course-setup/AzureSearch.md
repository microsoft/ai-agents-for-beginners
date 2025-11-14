<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:22:09+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "fr"
}
-->
# Guide de configuration d'Azure AI Search

Ce guide vous aidera à configurer Azure AI Search en utilisant le portail Azure. Suivez les étapes ci-dessous pour créer et configurer votre service Azure AI Search.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- Un abonnement Azure. Si vous n'avez pas d'abonnement Azure, vous pouvez créer un compte gratuit sur [Compte gratuit Azure](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Étape 1 : Créer un compte de stockage Azure

1. Suivez cette instruction, [Créer un compte de stockage Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), pour créer un nouveau compte de stockage Azure.  
   **NOTE** : Assurez-vous que le type de compte de stockage est Standard General Purpose V2.

## Étape 2 : Créer un service Azure AI Search

1. Connectez-vous au [portail Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Dans le volet de navigation à gauche, cliquez sur **Créer une ressource**.
3. Dans la barre de recherche, tapez "Azure AI Search" et sélectionnez **Azure AI Search** dans la liste des résultats.
4. Cliquez sur le bouton **Créer**.
5. Dans l'onglet **Basique**, fournissez les informations suivantes :
   - **Abonnement** : Sélectionnez votre abonnement Azure.
   - **Groupe de ressources** : Créez un nouveau groupe de ressources ou sélectionnez-en un existant.
   - **Nom de la ressource** : Entrez un nom unique pour votre service de recherche.
   - **Région** : Sélectionnez la région la plus proche de vos utilisateurs.
   - **Niveau de tarification** : Choisissez un niveau de tarification adapté à vos besoins. Vous pouvez commencer avec le niveau gratuit pour tester.
6. Cliquez sur **Vérifier + créer**.
7. Vérifiez les paramètres et cliquez sur **Créer** pour créer le service de recherche.

## Étape 3 : Commencer avec Azure AI Search

1. Une fois le déploiement terminé, accédez à votre service de recherche dans le portail Azure.
2. Dans le volet d'aperçu du service de recherche, copiez l'URL. Elle devrait ressembler à `https://<service-name>.search.windows.net`.
3. Dans le volet Paramètres > Clés, copiez la clé de requête.
4. Suivez les étapes de la page [Guide de démarrage rapide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pour créer un index, télécharger des données et effectuer une requête de recherche.

## Étape 4 : Utiliser les outils Azure AI Search

Azure AI Search s'intègre à divers outils pour améliorer vos capacités de recherche. Vous pouvez utiliser Azure CLI, Python SDK, .NET SDK et d'autres outils pour des configurations et opérations avancées.

### Utilisation d'Azure CLI

1. Installez Azure CLI en suivant les instructions sur [Installer Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Connectez-vous à Azure CLI en utilisant la commande :

   ```bash
   az login
   ```

3. Stockez à la fois l'endpoint et la clé API de l'instance Azure AI Search dans des variables d'environnement.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Utilisation du SDK Python

1. Installez la bibliothèque cliente Azure Cognitive Search pour Python :

   ```bash
   pip install azure-search-documents
   ```

2. Utilisez le code Python suivant pour créer un index et télécharger des documents :

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
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

1. Exécutez la commande suivante pour créer un index et télécharger des documents :

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Voici le code .NET de `AzureSearch.cs` :

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
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
- [Outils Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

Vous avez configuré avec succès Azure AI Search en utilisant le portail Azure et les outils intégrés. Vous pouvez maintenant explorer des fonctionnalités et capacités avancées d'Azure AI Search pour améliorer vos solutions de recherche.

Pour toute assistance supplémentaire, visitez la [documentation Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.