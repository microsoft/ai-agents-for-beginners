<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T10:05:43+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "es"
}
-->
# Guía de configuración de Azure AI Search

Esta guía te ayudará a configurar Azure AI Search utilizando el portal de Azure. Sigue los pasos a continuación para crear y configurar tu servicio de Azure AI Search.

## Requisitos previos

Antes de comenzar, asegúrate de contar con lo siguiente:

- Una suscripción de Azure. Si no tienes una suscripción de Azure, puedes crear una cuenta gratuita en [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Paso 1: Crear un servicio de Azure AI Search

1. Inicia sesión en el [portal de Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. En el panel de navegación izquierdo, haz clic en **Crear un recurso**.
3. En el cuadro de búsqueda, escribe "Azure Cognitive Search" y selecciona **Azure Cognitive Search** de la lista de resultados.
4. Haz clic en el botón **Crear**.
5. En la pestaña **Básicos**, proporciona la siguiente información:
   - **Suscripción**: Selecciona tu suscripción de Azure.
   - **Grupo de recursos**: Crea un nuevo grupo de recursos o selecciona uno existente.
   - **Nombre del recurso**: Ingresa un nombre único para tu servicio de búsqueda.
   - **Región**: Selecciona la región más cercana a tus usuarios.
   - **Nivel de precios**: Elige un nivel de precios que se adapte a tus necesidades. Puedes comenzar con el nivel gratuito para pruebas.
6. Haz clic en **Revisar y crear**.
7. Revisa la configuración y haz clic en **Crear** para crear el servicio de búsqueda.

## Paso 2: Comenzar con Azure AI Search

1. Una vez que se complete la implementación, navega a tu servicio de búsqueda en el portal de Azure.
2. En la página de resumen del servicio de búsqueda, haz clic en el botón **Inicio rápido**.
3. Sigue los pasos de la guía de inicio rápido para crear un índice, cargar datos y realizar una consulta de búsqueda.

### Crear un índice

1. En la guía de inicio rápido, haz clic en **Crear un índice**.
2. Define el esquema del índice especificando los campos y sus atributos (por ejemplo, tipo de datos, capacidad de búsqueda, capacidad de filtrado).
3. Haz clic en **Crear** para crear el índice.

### Cargar datos

1. En la guía de inicio rápido, haz clic en **Cargar datos**.
2. Elige una fuente de datos (por ejemplo, Azure Blob Storage, Azure SQL Database) y proporciona los detalles de conexión necesarios.
3. Mapea los campos de la fuente de datos con los campos del índice.
4. Haz clic en **Enviar** para cargar los datos al índice.

### Realizar una consulta de búsqueda

1. En la guía de inicio rápido, haz clic en **Explorador de búsqueda**.
2. Ingresa una consulta de búsqueda en el cuadro de búsqueda para probar la funcionalidad de búsqueda.
3. Revisa los resultados de búsqueda y ajusta el esquema del índice o los datos según sea necesario.

## Paso 3: Utilizar herramientas de Azure AI Search

Azure AI Search se integra con varias herramientas para mejorar tus capacidades de búsqueda. Puedes utilizar Azure CLI, Python SDK y otras herramientas para configuraciones y operaciones avanzadas.

### Uso de Azure CLI

1. Instala Azure CLI siguiendo las instrucciones en [Instalar Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Inicia sesión en Azure CLI utilizando el comando:
   ```bash
   az login
   ```
3. Crea un nuevo servicio de búsqueda utilizando Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Crea un índice utilizando Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Uso del SDK de Python

1. Instala la biblioteca cliente de Azure Cognitive Search para Python:
   ```bash
   pip install azure-search-documents
   ```
2. Utiliza el siguiente código en Python para crear un índice y cargar documentos:
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

Para información más detallada, consulta la siguiente documentación:

- [Crear un servicio de Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Comenzar con Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Herramientas de Azure AI Search](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusión

Has configurado exitosamente Azure AI Search utilizando el portal de Azure y las herramientas integradas. Ahora puedes explorar funciones y capacidades avanzadas de Azure AI Search para mejorar tus soluciones de búsqueda.

Para obtener más asistencia, visita la [documentación de Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.