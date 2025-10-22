<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:39:33+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "cs"
}
-->
# Průvodce nastavením Azure AI Search

Tento průvodce vám pomůže nastavit Azure AI Search pomocí Azure portálu. Postupujte podle níže uvedených kroků pro vytvoření a konfiguraci služby Azure AI Search.

## Požadavky

Než začnete, ujistěte se, že máte následující:

- Azure předplatné. Pokud ještě nemáte Azure předplatné, můžete si vytvořit bezplatný účet na [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Krok 1: Vytvoření služby Azure AI Search

1. Přihlaste se do [Azure portálu](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. V levém navigačním panelu klikněte na **Vytvořit prostředek**.
3. Do vyhledávacího pole zadejte „Azure AI Search“ a vyberte **Azure AI Search** ze seznamu výsledků.
4. Klikněte na tlačítko **Vytvořit**.
5. Na kartě **Základní informace** vyplňte následující údaje:
   - **Předplatné**: Vyberte své Azure předplatné.
   - **Skupina prostředků**: Vytvořte novou skupinu prostředků nebo vyberte existující.
   - **Název prostředku**: Zadejte jedinečný název pro vaši vyhledávací službu.
   - **Oblast**: Vyberte oblast nejblíže vašim uživatelům.
   - **Cenová úroveň**: Zvolte cenovou úroveň, která vyhovuje vašim požadavkům. Pro testování můžete začít s bezplatnou úrovní.
6. Klikněte na **Zkontrolovat + vytvořit**.
7. Zkontrolujte nastavení a klikněte na **Vytvořit** pro vytvoření vyhledávací služby.

## Krok 2: Začínáme s Azure AI Search

1. Po dokončení nasazení přejděte ke své vyhledávací službě v Azure portálu.
2. Na stránce přehledu vyhledávací služby klikněte na tlačítko **Rychlý start**.
3. Postupujte podle kroků v průvodci Rychlý start pro vytvoření indexu, nahrání dat a provedení vyhledávacího dotazu.

### Vytvoření indexu

1. V průvodci Rychlý start klikněte na **Vytvořit index**.
2. Definujte schéma indexu zadáním polí a jejich atributů (např. datový typ, vyhledávatelné, filtrovatelné).
3. Klikněte na **Vytvořit** pro vytvoření indexu.

### Nahrání dat

1. V průvodci Rychlý start klikněte na **Nahrát data**.
2. Vyberte zdroj dat (např. Azure Blob Storage, Azure SQL Database) a zadejte potřebné přihlašovací údaje.
3. Namapujte pole zdroje dat na pole indexu.
4. Klikněte na **Odeslat** pro nahrání dat do indexu.

### Provedení vyhledávacího dotazu

1. V průvodci Rychlý start klikněte na **Prohlížeč vyhledávání**.
2. Zadejte vyhledávací dotaz do vyhledávacího pole pro otestování funkčnosti vyhledávání.
3. Prohlédněte si výsledky vyhledávání a podle potřeby upravte schéma indexu nebo data.

## Krok 3: Použití nástrojů Azure AI Search

Azure AI Search se integruje s různými nástroji, které rozšiřují možnosti vyhledávání. Můžete použít Azure CLI, Python SDK a další nástroje pro pokročilé konfigurace a operace.

### Použití Azure CLI

1. Nainstalujte Azure CLI podle pokynů na [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Přihlaste se do Azure CLI pomocí příkazu:
   ```bash
   az login
   ```
3. Vytvořte novou vyhledávací službu pomocí Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Vytvořte index pomocí Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Použití Python SDK

1. Nainstalujte knihovnu Azure Cognitive Search klienta pro Python:
   ```bash
   pip install azure-search-documents
   ```
2. Použijte následující Python kód pro vytvoření indexu a nahrání dokumentů:
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

Pro podrobnější informace se podívejte do následující dokumentace:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Závěr

Úspěšně jste nastavili Azure AI Search pomocí Azure portálu a integrovaných nástrojů. Nyní můžete prozkoumat pokročilejší funkce a možnosti Azure AI Search, které vám pomohou vylepšit vaše vyhledávací řešení.

Pro další pomoc navštivte [Azure Cognitive Search dokumentaci](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.