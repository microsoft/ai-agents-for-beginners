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
