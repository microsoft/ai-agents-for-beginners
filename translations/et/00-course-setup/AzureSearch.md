<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-10-11T11:25:44+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "et"
}
-->
# Azure AI Searchi seadistamise juhend

See juhend aitab teil Azure AI Searchi seadistada Azure'i portaalis. Järgige allolevaid samme, et luua ja konfigureerida oma Azure AI Searchi teenus.

## Eeltingimused

Enne alustamist veenduge, et teil on olemas järgmised asjad:

- Azure'i tellimus. Kui teil pole Azure'i tellimust, saate luua tasuta konto aadressil [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Samm 1: Looge Azure AI Searchi teenus

1. Logige sisse [Azure'i portaali](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasakpoolses navigeerimispaneelis klõpsake **Create a resource**.
3. Otsingukasti sisestage "Azure AI Search" ja valige tulemuste loendist **Azure AI Search**.
4. Klõpsake nuppu **Create**.
5. **Basics** vahekaardil täitke järgmised andmed:
   - **Subscription**: Valige oma Azure'i tellimus.
   - **Resource group**: Looge uus ressursigrupp või valige olemasolev.
   - **Resource name**: Sisestage oma otsinguteenusele unikaalne nimi.
   - **Region**: Valige oma kasutajatele lähim piirkond.
   - **Pricing tier**: Valige hinnaklass, mis vastab teie vajadustele. Testimiseks võite alustada tasuta tasemega.
6. Klõpsake **Review + create**.
7. Vaadake seaded üle ja klõpsake **Create**, et otsinguteenust luua.

## Samm 2: Alustage Azure AI Searchi kasutamist

1. Kui juurutamine on lõpule jõudnud, navigeerige Azure'i portaalis oma otsinguteenuse juurde.
2. Otsinguteenuse ülevaate lehel klõpsake nuppu **Quickstart**.
3. Järgige Quickstart-juhendi samme, et luua indeks, laadida andmeid üles ja teha otsingupäring.

### Indeksi loomine

1. Quickstart-juhendis klõpsake **Create an index**.
2. Määratlege indeksi skeem, määrates väljad ja nende atribuudid (nt andmetüüp, otsitav, filtreeritav).
3. Klõpsake **Create**, et indeks luua.

### Andmete üleslaadimine

1. Quickstart-juhendis klõpsake **Upload data**.
2. Valige andmeallikas (nt Azure Blob Storage, Azure SQL Database) ja sisestage vajalikud ühenduse andmed.
3. Kaardistage andmeallika väljad indeksi väljadega.
4. Klõpsake **Submit**, et andmed indeksisse üles laadida.

### Otsingupäringu tegemine

1. Quickstart-juhendis klõpsake **Search explorer**.
2. Sisestage otsingukasti otsingupäring, et testida otsingufunktsiooni.
3. Vaadake otsingutulemusi ja kohandage vajadusel indeksi skeemi või andmeid.

## Samm 3: Kasutage Azure AI Searchi tööriistu

Azure AI Search integreerub erinevate tööriistadega, et täiustada teie otsinguvõimalusi. Saate kasutada Azure CLI-d, Python SDK-d ja muid tööriistu keerukamate seadistuste ja toimingute jaoks.

### Azure CLI kasutamine

1. Installige Azure CLI, järgides juhiseid aadressil [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logige Azure CLI-sse sisse, kasutades käsku:
   ```bash
   az login
   ```
3. Looge uus otsinguteenus Azure CLI abil:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Looge indeks Azure CLI abil:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK kasutamine

1. Installige Azure Cognitive Searchi klienditeek Pythonile:
   ```bash
   pip install azure-search-documents
   ```
2. Kasutage järgmist Python-koodi indeksi loomiseks ja dokumentide üleslaadimiseks:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

Lisateabe saamiseks vaadake järgmist dokumentatsiooni:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kokkuvõte

Olete edukalt seadistanud Azure AI Searchi Azure'i portaalis ja integreerinud tööriistad. Nüüd saate uurida Azure AI Searchi täiustatud funktsioone ja võimalusi, et täiustada oma otsingulahendusi.

Lisateabe saamiseks külastage [Azure Cognitive Searchi dokumentatsiooni](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.