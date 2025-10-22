<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-08-30T15:03:47+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "lt"
}
-->
# Azure AI Search Nustatymo Vadovas

Šis vadovas padės jums nustatyti Azure AI Search naudojant Azure portalą. Sekite žemiau pateiktus veiksmus, kad sukurtumėte ir sukonfigūruotumėte savo Azure AI Search paslaugą.

## Reikalavimai

Prieš pradėdami, įsitikinkite, kad turite:

- Azure prenumeratą. Jei neturite Azure prenumeratos, galite sukurti nemokamą paskyrą adresu [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## 1 žingsnis: Sukurkite Azure AI Search Paslaugą

1. Prisijunkite prie [Azure portalo](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Kairiajame navigacijos meniu spustelėkite **Create a resource**.
3. Paieškos laukelyje įveskite „Azure AI Search“ ir pasirinkite **Azure AI Search** iš rezultatų sąrašo.
4. Spustelėkite mygtuką **Create**.
5. Skiltyje **Basics** pateikite šią informaciją:
   - **Subscription**: Pasirinkite savo Azure prenumeratą.
   - **Resource group**: Sukurkite naują išteklių grupę arba pasirinkite esamą.
   - **Resource name**: Įveskite unikalų savo paieškos paslaugos pavadinimą.
   - **Region**: Pasirinkite regioną, artimiausią jūsų naudotojams.
   - **Pricing tier**: Pasirinkite kainodaros planą, kuris atitinka jūsų poreikius. Pradžiai galite pasirinkti nemokamą planą.
6. Spustelėkite **Review + create**.
7. Peržiūrėkite nustatymus ir spustelėkite **Create**, kad sukurtumėte paieškos paslaugą.

## 2 žingsnis: Pradėkite Naudoti Azure AI Search

1. Kai diegimas bus baigtas, eikite į savo paieškos paslaugą Azure portale.
2. Paieškos paslaugos apžvalgos puslapyje spustelėkite mygtuką **Quickstart**.
3. Sekite Quickstart vadovo veiksmus, kad sukurtumėte indeksą, įkeltumėte duomenis ir atliktumėte paieškos užklausą.

### Sukurkite Indeksą

1. Quickstart vadove spustelėkite **Create an index**.
2. Apibrėžkite indekso schemą, nurodydami laukus ir jų atributus (pvz., duomenų tipą, paieškos galimybę, filtravimą).
3. Spustelėkite **Create**, kad sukurtumėte indeksą.

### Įkelkite Duomenis

1. Quickstart vadove spustelėkite **Upload data**.
2. Pasirinkite duomenų šaltinį (pvz., Azure Blob Storage, Azure SQL Database) ir pateikite reikiamus prisijungimo duomenis.
3. Susiekite duomenų šaltinio laukus su indekso laukais.
4. Spustelėkite **Submit**, kad įkeltumėte duomenis į indeksą.

### Atlikite Paieškos Užklausą

1. Quickstart vadove spustelėkite **Search explorer**.
2. Įveskite paieškos užklausą į paieškos laukelį, kad išbandytumėte paieškos funkcionalumą.
3. Peržiūrėkite paieškos rezultatus ir, jei reikia, koreguokite indekso schemą ar duomenis.

## 3 žingsnis: Naudokite Azure AI Search Įrankius

Azure AI Search integruojasi su įvairiais įrankiais, kad pagerintų jūsų paieškos galimybes. Galite naudoti Azure CLI, Python SDK ir kitus įrankius pažangesniems nustatymams ir operacijoms.

### Naudojant Azure CLI

1. Įdiekite Azure CLI, sekdami instrukcijas adresu [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prisijunkite prie Azure CLI naudodami komandą:
   ```bash
   az login
   ```
3. Sukurkite naują paieškos paslaugą naudodami Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Sukurkite indeksą naudodami Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Naudojant Python SDK

1. Įdiekite Azure Cognitive Search klientų biblioteką Python kalbai:
   ```bash
   pip install azure-search-documents
   ```
2. Naudokite šį Python kodą, kad sukurtumėte indeksą ir įkeltumėte dokumentus:
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

Daugiau informacijos rasite šiuose dokumentuose:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Išvada

Jūs sėkmingai nustatėte Azure AI Search naudodami Azure portalą ir integruotus įrankius. Dabar galite tyrinėti pažangesnes Azure AI Search funkcijas ir galimybes, kad pagerintumėte savo paieškos sprendimus.

Dėl papildomos pagalbos apsilankykite [Azure Cognitive Search dokumentacijoje](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.