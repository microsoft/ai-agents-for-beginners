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
