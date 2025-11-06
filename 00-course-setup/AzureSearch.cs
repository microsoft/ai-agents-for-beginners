#:package Azure.Search.Documents@11.*
#:property PublishAot=false

using Azure;
using Azure.Search.Documents;
using Azure.Search.Documents.Indexes;
using Azure.Search.Documents.Indexes.Models;

var serviceEndpoint = new Uri("https://<service-name>.search.windows.net");
var apiKey = "<api-key>";
var indexName = "sample-index";

var credential = new AzureKeyCredential(apiKey);
var indexClient = new SearchIndexClient(serviceEndpoint, credential);

var fields = new List<SearchField>()
{
    new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
    new SearchableField("content")
};

var index = new SearchIndex(name: indexName, fields: fields);

await indexClient.CreateOrUpdateIndexAsync(index);

var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

var documents = new[]
{
    new { id = "1", content = "Hello world" },
    new { id = "2", content = "Azure Cognitive Search" }
};

await searchClient.UploadDocumentsAsync(documents);
