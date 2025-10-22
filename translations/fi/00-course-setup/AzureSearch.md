<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:37:54+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "fi"
}
-->
# Azure AI Search -asennusopas

Tämä opas auttaa sinua ottamaan Azure AI Searchin käyttöön Azure-portaalin kautta. Seuraa alla olevia ohjeita luodaksesi ja määrittääksesi Azure AI Search -palvelusi.

## Ennen aloittamista

Varmista ennen aloittamista, että sinulla on seuraavat asiat:

- Azure-tilaus. Jos sinulla ei vielä ole Azure-tilausta, voit luoda ilmaisen tilin osoitteessa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Vaihe 1: Luo Azure AI Search -palvelu

1. Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Vasemman reunan navigointipaneelissa valitse **Luo resurssi**.
3. Hakukenttään kirjoita "Azure AI Search" ja valitse tuloksista **Azure AI Search**.
4. Klikkaa **Luo**-painiketta.
5. **Perustiedot**-välilehdellä anna seuraavat tiedot:
   - **Tilaus**: Valitse Azure-tilauksesi.
   - **Resurssiryhmä**: Luo uusi resurssiryhmä tai valitse olemassa oleva.
   - **Resurssin nimi**: Anna hakupalvelullesi yksilöllinen nimi.
   - **Alue**: Valitse käyttäjiäsi lähinnä oleva alue.
   - **Hinnoittelutaso**: Valitse tarpeisiisi sopiva hinnoittelutaso. Voit aloittaa ilmaisella tasolla testaukseen.
6. Klikkaa **Tarkista + luo**.
7. Tarkista asetukset ja klikkaa **Luo** luodaksesi hakupalvelun.

## Vaihe 2: Aloita Azure AI Searchin käyttö

1. Kun käyttöönotto on valmis, siirry hakupalvelusi sivulle Azure-portaalissa.
2. Hakupalvelun yleiskatsaus-sivulla klikkaa **Pika-aloitus**-painiketta.
3. Seuraa Pika-aloitus -oppaan ohjeita luodaksesi indeksi, ladata dataa ja suorittaaksesi hakukyselyn.

### Luo indeksi

1. Pika-aloitus -oppaassa klikkaa **Luo indeksi**.
2. Määritä indeksin rakenne määrittelemällä kentät ja niiden ominaisuudet (esim. tietotyyppi, haettavuus, suodatettavuus).
3. Klikkaa **Luo** luodaksesi indeksin.

### Lataa dataa

1. Pika-aloitus -oppaassa klikkaa **Lataa dataa**.
2. Valitse tietolähde (esim. Azure Blob Storage, Azure SQL Database) ja anna tarvittavat yhteystiedot.
3. Määritä tietolähteen kentät vastaamaan indeksin kenttiä.
4. Klikkaa **Lähetä** ladataksesi datan indeksiin.

### Suorita hakukysely

1. Pika-aloitus -oppaassa klikkaa **Search explorer**.
2. Kirjoita hakukysely hakukenttään testataksesi hakutoimintoa.
3. Tarkastele hakutuloksia ja säädä tarvittaessa indeksin rakennetta tai dataa.

## Vaihe 3: Käytä Azure AI Search -työkaluja

Azure AI Search integroituu useiden työkalujen kanssa, jotka parantavat hakutoimintojasi. Voit käyttää Azure CLI:tä, Python SDK:ta ja muita työkaluja edistyneisiin määrityksiin ja toimintoihin.

### Azure CLI:n käyttö

1. Asenna Azure CLI noudattamalla ohjeita osoitteessa [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Kirjaudu Azure CLI:hin komennolla:
   ```bash
   az login
   ```
3. Luo uusi hakupalvelu Azure CLI:llä:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Luo indeksi Azure CLI:llä:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK:n käyttö

1. Asenna Azure Cognitive Search -asiakas kirjasto Pythonille:
   ```bash
   pip install azure-search-documents
   ```
2. Käytä seuraavaa Python-koodia luodaksesi indeksi ja ladataksesi dokumentteja:
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

Lisätietoja löydät seuraavista dokumenteista:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Yhteenveto

Olet onnistuneesti ottanut Azure AI Searchin käyttöön Azure-portaalin ja integroitujen työkalujen avulla. Voit nyt tutustua Azure AI Searchin edistyneempiin ominaisuuksiin ja hyödyntää niitä hakuratkaisujesi parantamiseksi.

Lisäapua saat osoitteesta [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.