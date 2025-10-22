<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:39:20+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hu"
}
-->
# Azure AI Search beállítási útmutató

Ez az útmutató segít az Azure AI Search beállításában az Azure portál használatával. Kövesd az alábbi lépéseket az Azure AI Search szolgáltatás létrehozásához és konfigurálásához.

## Előfeltételek

Mielőtt elkezdenéd, győződj meg róla, hogy rendelkezel a következőkkel:

- Egy Azure előfizetés. Ha még nincs Azure előfizetésed, ingyenes fiókot hozhatsz létre a [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) oldalon.

## 1. lépés: Azure AI Search szolgáltatás létrehozása

1. Jelentkezz be az [Azure portálra](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. A bal oldali navigációs sávban kattints a **Create a resource** lehetőségre.
3. A keresőmezőbe írd be, hogy "Azure AI Search", majd válaszd ki az eredmények közül az **Azure AI Search** szolgáltatást.
4. Kattints a **Create** gombra.
5. A **Basics** fülön add meg a következő adatokat:
   - **Subscription**: Válaszd ki az Azure előfizetésedet.
   - **Resource group**: Hozz létre egy új erőforráscsoportot, vagy válassz egy meglévőt.
   - **Resource name**: Adj meg egy egyedi nevet a keresőszolgáltatásodnak.
   - **Region**: Válaszd ki a felhasználóidhoz legközelebbi régiót.
   - **Pricing tier**: Válassz egy árkategóriát, amely megfelel az igényeidnek. Teszteléshez kezdhetsz az ingyenes (Free) szinttel.
6. Kattints a **Review + create** gombra.
7. Ellenőrizd a beállításokat, majd kattints a **Create** gombra a keresőszolgáltatás létrehozásához.

## 2. lépés: Az Azure AI Search használatának megkezdése

1. A telepítés befejezése után navigálj a keresőszolgáltatásodhoz az Azure portálon.
2. A keresőszolgáltatás áttekintő oldalán kattints a **Quickstart** gombra.
3. Kövesd a Quickstart útmutató lépéseit az index létrehozásához, az adatok feltöltéséhez és a keresési lekérdezés végrehajtásához.

### Index létrehozása

1. A Quickstart útmutatóban kattints a **Create an index** lehetőségre.
2. Határozd meg az index sémáját a mezők és azok tulajdonságainak megadásával (pl. adattípus, kereshető, szűrhető).
3. Kattints a **Create** gombra az index létrehozásához.

### Adatok feltöltése

1. A Quickstart útmutatóban kattints az **Upload data** lehetőségre.
2. Válassz egy adatforrást (pl. Azure Blob Storage, Azure SQL Database), és add meg a szükséges kapcsolati adatokat.
3. Térképezd fel az adatforrás mezőit az index mezőire.
4. Kattints a **Submit** gombra az adatok indexbe történő feltöltéséhez.

### Keresési lekérdezés végrehajtása

1. A Quickstart útmutatóban kattints a **Search explorer** lehetőségre.
2. Írj be egy keresési lekérdezést a keresőmezőbe a keresési funkció teszteléséhez.
3. Tekintsd át a keresési eredményeket, és szükség szerint módosítsd az index sémáját vagy az adatokat.

## 3. lépés: Azure AI Search eszközök használata

Az Azure AI Search különböző eszközökkel integrálható, hogy bővítsd a keresési lehetőségeidet. Használhatod az Azure CLI-t, a Python SDK-t és más eszközöket fejlettebb konfigurációkhoz és műveletekhez.

### Azure CLI használata

1. Telepítsd az Azure CLI-t az alábbi útmutató szerint: [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Jelentkezz be az Azure CLI-be a következő parancs segítségével:
   ```bash
   az login
   ```
3. Hozz létre egy új keresőszolgáltatást az Azure CLI segítségével:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Hozz létre egy indexet az Azure CLI-vel:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK használata

1. Telepítsd az Azure Cognitive Search Python klienskönyvtárát:
   ```bash
   pip install azure-search-documents
   ```
2. Használd az alábbi Python kódot index létrehozásához és dokumentumok feltöltéséhez:
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

Részletesebb információkért tekintsd meg a következő dokumentációkat:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Összefoglalás

Sikeresen beállítottad az Azure AI Search szolgáltatást az Azure portál és az integrált eszközök segítségével. Most már felfedezheted az Azure AI Search fejlettebb funkcióit és lehetőségeit, hogy tovább fejleszd keresési megoldásaidat.

További segítségért látogass el az [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) oldalra.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.