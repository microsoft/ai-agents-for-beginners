<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:39:45+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sk"
}
-->
# Azure AI Search Sprievodca nastavením

Tento sprievodca vám pomôže nastaviť Azure AI Search pomocou Azure portálu. Postupujte podľa nižšie uvedených krokov na vytvorenie a konfiguráciu služby Azure AI Search.

## Požiadavky

Pred začatím sa uistite, že máte:

- Predplatné Azure. Ak ešte nemáte predplatné Azure, môžete si vytvoriť bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvorenie služby Azure AI Search

1. Prihláste sa do [Azure portálu](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V ľavom navigačnom paneli kliknite na **Create a resource**.
3. Do vyhľadávacieho poľa zadajte "Azure AI Search" a zo zoznamu výsledkov vyberte **Azure AI Search**.
4. Kliknite na tlačidlo **Create**.
5. Na karte **Basics** vyplňte nasledujúce údaje:
   - **Subscription**: Vyberte svoje predplatné Azure.
   - **Resource group**: Vytvorte novú skupinu prostriedkov alebo vyberte existujúcu.
   - **Resource name**: Zadajte jedinečný názov pre vašu vyhľadávaciu službu.
   - **Region**: Vyberte región najbližší vašim používateľom.
   - **Pricing tier**: Zvoľte cenovú úroveň podľa vašich potrieb. Pre testovanie môžete začať s Free tier.
6. Kliknite na **Review + create**.
7. Skontrolujte nastavenia a kliknite na **Create** pre vytvorenie vyhľadávacej služby.

## Krok 2: Začnite používať Azure AI Search

1. Po dokončení nasadenia prejdite na svoju vyhľadávaciu službu v Azure portáli.
2. Na stránke prehľadu vyhľadávacej služby kliknite na tlačidlo **Quickstart**.
3. Postupujte podľa krokov v sprievodcovi Quickstart na vytvorenie indexu, nahranie dát a vykonanie vyhľadávacieho dopytu.

### Vytvorenie indexu

1. V sprievodcovi Quickstart kliknite na **Create an index**.
2. Definujte schému indexu určením polí a ich atribútov (napr. dátový typ, vyhľadávateľné, filtrovatelné).
3. Kliknite na **Create** pre vytvorenie indexu.

### Nahranie dát

1. V sprievodcovi Quickstart kliknite na **Upload data**.
2. Vyberte zdroj dát (napr. Azure Blob Storage, Azure SQL Database) a zadajte potrebné údaje na pripojenie.
3. Namapujte polia zdroja dát na polia indexu.
4. Kliknite na **Submit** pre nahranie dát do indexu.

### Vykonanie vyhľadávacieho dopytu

1. V sprievodcovi Quickstart kliknite na **Search explorer**.
2. Zadajte vyhľadávací dopyt do vyhľadávacieho poľa na otestovanie funkčnosti vyhľadávania.
3. Prezrite si výsledky vyhľadávania a podľa potreby upravte schému indexu alebo dáta.

## Krok 3: Použitie nástrojov Azure AI Search

Azure AI Search sa integruje s rôznymi nástrojmi na rozšírenie vašich vyhľadávacích možností. Môžete použiť Azure CLI, Python SDK a ďalšie nástroje pre pokročilé konfigurácie a operácie.

### Použitie Azure CLI

1. Nainštalujte Azure CLI podľa pokynov na [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Prihláste sa do Azure CLI pomocou príkazu:
   ```bash
   az login
   ```
3. Vytvorte novú vyhľadávaciu službu pomocou Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Vytvorte index pomocou Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Použitie Python SDK

1. Nainštalujte knižnicu Azure Cognitive Search klienta pre Python:
   ```bash
   pip install azure-search-documents
   ```
2. Použite nasledujúci Python kód na vytvorenie indexu a nahranie dokumentov:
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

Pre podrobnejšie informácie si pozrite nasledujúcu dokumentáciu:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Záver

Úspešne ste nastavili Azure AI Search pomocou Azure portálu a integrovaných nástrojov. Teraz môžete preskúmať pokročilejšie funkcie a možnosti Azure AI Search na vylepšenie vašich vyhľadávacích riešení.

Pre ďalšiu pomoc navštívte [Azure Cognitive Search dokumentáciu](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.