<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:40:47+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sl"
}
-->
# Azure AI Search Vodnik za namestitev

Ta vodnik vam bo pomagal nastaviti Azure AI Search prek Azure portala. Sledite spodnjim korakom za ustvarjanje in konfiguracijo vaše storitve Azure AI Search.

## Predpogoji

Pred začetkom poskrbite, da imate naslednje:

- Azure naročnino. Če še nimate Azure naročnine, lahko ustvarite brezplačen račun na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Korak 1: Ustvarite storitev Azure AI Search

1. Prijavite se v [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levem navigacijskem meniju kliknite **Create a resource**.
3. V iskalno polje vpišite "Azure AI Search" in izberite **Azure AI Search** s seznama rezultatov.
4. Kliknite gumb **Create**.
5. Na zavihku **Basics** vnesite naslednje podatke:
   - **Subscription**: Izberite vašo Azure naročnino.
   - **Resource group**: Ustvarite novo skupino virov ali izberite obstoječo.
   - **Resource name**: Vnesite edinstveno ime za vašo iskalno storitev.
   - **Region**: Izberite regijo, ki je najbližja vašim uporabnikom.
   - **Pricing tier**: Izberite cenovni razred, ki ustreza vašim potrebam. Za testiranje lahko začnete z brezplačnim razredom.
6. Kliknite **Review + create**.
7. Preglejte nastavitve in kliknite **Create** za ustvarjanje iskalne storitve.

## Korak 2: Začnite z Azure AI Search

1. Ko je namestitev končana, pojdite na vašo iskalno storitev v Azure portalu.
2. Na strani pregleda iskalne storitve kliknite gumb **Quickstart**.
3. Sledite korakom v vodniku Quickstart za ustvarjanje indeksa, nalaganje podatkov in izvajanje iskalnih poizvedb.

### Ustvarite indeks

1. V vodniku Quickstart kliknite **Create an index**.
2. Določite shemo indeksa tako, da navedete polja in njihove lastnosti (npr. tip podatkov, ali je polje iskalno, filtrirno).
3. Kliknite **Create** za ustvarjanje indeksa.

### Naložite podatke

1. V vodniku Quickstart kliknite **Upload data**.
2. Izberite vir podatkov (npr. Azure Blob Storage, Azure SQL Database) in vnesite potrebne podatke za povezavo.
3. Preslikajte polja vira podatkov na polja indeksa.
4. Kliknite **Submit** za nalaganje podatkov v indeks.

### Izvedite iskalno poizvedbo

1. V vodniku Quickstart kliknite **Search explorer**.
2. V iskalno polje vnesite iskalno poizvedbo za testiranje funkcionalnosti iskanja.
3. Preglejte rezultate iskanja in po potrebi prilagodite shemo indeksa ali podatke.

## Korak 3: Uporabite orodja Azure AI Search

Azure AI Search se povezuje z različnimi orodji za izboljšanje vaših iskalnih zmogljivosti. Za napredne nastavitve in operacije lahko uporabite Azure CLI, Python SDK in druga orodja.

### Uporaba Azure CLI

1. Namestite Azure CLI po navodilih na [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prijavite se v Azure CLI z ukazom:
   ```bash
   az login
   ```
3. Ustvarite novo iskalno storitev z uporabo Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Ustvarite indeks z uporabo Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Uporaba Python SDK

1. Namestite knjižnico Azure Cognitive Search za Python:
   ```bash
   pip install azure-search-documents
   ```
2. Uporabite naslednjo Python kodo za ustvarjanje indeksa in nalaganje dokumentov:
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

Za podrobnejše informacije si oglejte naslednjo dokumentacijo:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Zaključek

Uspešno ste nastavili Azure AI Search prek Azure portala in integriranih orodij. Zdaj lahko raziskujete naprednejše funkcije in zmogljivosti Azure AI Search za izboljšanje vaših iskalnih rešitev.

Za dodatno pomoč obiščite [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.