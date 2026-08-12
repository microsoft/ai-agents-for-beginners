# Configuración del Curso

## Introducción

Esta lección cubrirá cómo ejecutar los ejemplos de código de este curso.

## Únete a Otros Estudiantes y Obtén Ayuda

Antes de comenzar a clonar tu repositorio, únete al [canal de Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obtener ayuda con la configuración, cualquier pregunta sobre el curso o para conectar con otros estudiantes.

## Clona o Haz un Fork de este Repositorio

Para comenzar, por favor clona o haz un fork del repositorio de GitHub. Esto creará tu propia versión del material del curso para que puedas ejecutar, probar y modificar el código.

Esto se puede hacer haciendo clic en el enlace para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">hacer un fork del repositorio</a>

Ahora deberías tener tu propia versión bifurcada de este curso en el siguiente enlace:

![Repositorio Bifurcado](../../../translated_images/es/forked-repo.33f27ca1901baa6a.webp)

### Clonación Superficial (recomendado para talleres / Codespaces)

  >El repositorio completo puede ser grande (~3 GB) cuando descargas todo el historial y todos los archivos. Si solo asistirás al taller o solo necesitas algunas carpetas de las lecciones, una clonación superficial (o clonación dispersa) evita la mayoría de esa descarga al truncar el historial y/o saltar los blobs.

#### Clonación rápida superficial — historial mínimo, todos los archivos

Reemplaza `<your-username>` en los comandos siguientes con la URL de tu fork (o la URL original si prefieres).

Para clonar solo el historial del último commit (descarga pequeña):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar una rama específica:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonación parcial (dispersa) — blobs mínimos + solo carpetas seleccionadas

Esto usa clonación parcial y sparse-checkout (requiere Git 2.25+ y se recomienda Git moderno con soporte de clonación parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Entra en la carpeta del repositorio:

```bash|powershell
cd ai-agents-for-beginners
```

Luego especifica qué carpetas quieres (el ejemplo abajo muestra dos carpetas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Después de clonar y verificar los archivos, si solo necesitas los archivos y quieres liberar espacio (sin historial de git), elimina la metadata del repositorio (💀 irreversible — perderás toda funcionalidad de Git: sin commits, pulls, pushes ni acceso al historial).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Uso de GitHub Codespaces (recomendado para evitar grandes descargas locales)

- Crea un nuevo Codespace para este repositorio a través de la [interfaz de GitHub](https://github.com/codespaces).  

- En la terminal del codespace recién creado, ejecuta uno de los comandos de clonación superficial/dispersa arriba para traer solo las carpetas de lección que necesitas al espacio de trabajo de Codespace.
- Opcional: después de clonar dentro de Codespaces, elimina .git para recuperar espacio adicional (ver comandos de eliminación arriba).
- Nota: Si prefieres abrir el repositorio directamente en Codespaces (sin una clonación extra), ten en cuenta que Codespaces construirá el entorno devcontainer y aún podría aprovisionar más de lo que necesitas. Clonar una copia superficial dentro de un Codespace nuevo te da más control sobre el uso del disco.

#### Consejos

- Siempre reemplaza la URL de clonación con tu fork si deseas editar o hacer commits.
- Si luego necesitas más historial o archivos, puedes obtenerlos o ajustar sparse-checkout para incluir carpetas adicionales.

## Ejecutando el Código

Este curso ofrece una serie de Jupyter Notebooks que puedes ejecutar para obtener experiencia práctica construyendo Agentes de IA.

Los ejemplos de código usan **Microsoft Agent Framework (MAF)** con el `FoundryChatClient`, que se conecta con **Microsoft Foundry Agent Service V2** (la API de Respuestas) a través de **Microsoft Foundry**.

Todos los notebooks en Python están etiquetados como `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Si no tienes Python3.12 instalado, asegúrate de instalarlo. Luego crea tu entorno virtual usando python3.12 para garantizar que las versiones correctas se instalen desde el archivo requirements.txt.
  
    >Ejemplo

    Crea el directorio de entorno virtual de Python:

    ```bash|powershell
    python -m venv venv
    ```

    Luego activa el entorno virtual para:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para los códigos de ejemplo que usan .NET, asegúrate de instalar [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superior. Luego, verifica la versión instalada del SDK de .NET:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Requerido para autenticación. Instálalo desde [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Suscripción de Azure** — Para acceder a Microsoft Foundry y Microsoft Foundry Agent Service.
- **Proyecto Microsoft Foundry** — Un proyecto con un modelo desplegado (por ejemplo, `gpt-5-mini`). Ver [Paso 1](#paso-1-crear-un-proyecto-microsoft-foundry) abajo.

Hemos incluido un archivo `requirements.txt` en la raíz de este repositorio que contiene todos los paquetes Python necesarios para ejecutar los ejemplos de código.

Puedes instalarlos ejecutando el siguiente comando en tu terminal en la raíz del repositorio:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos crear un entorno virtual de Python para evitar conflictos y problemas.

## Configurar VSCode

Asegúrate de usar la versión correcta de Python en VSCode.

![imagen](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurar Microsoft Foundry y Microsoft Foundry Agent Service

### Paso 1: Crear un Proyecto Microsoft Foundry

Necesitas un **hub** y un **proyecto** de Microsoft Foundry con un modelo desplegado para ejecutar los notebooks.

1. Ve a [ai.azure.com](https://ai.azure.com) e inicia sesión con tu cuenta de Azure.
2. Crea un **hub** (o usa uno existente). Ver: [Resumen de recursos Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro del hub, crea un **proyecto**.
4. Despliega un modelo (por ejemplo, `gpt-5-mini`) desde **Modelos + Endpoints** → **Desplegar modelo**.

### Paso 2: Obtén el Endpoint de tu Proyecto y el Nombre del Despliegue del Modelo

Desde tu proyecto en el portal de Microsoft Foundry:

- **Endpoint del Proyecto** — Ve a la página **Resumen** y copia la URL del endpoint.

![Cadena de Conexión del Proyecto](../../../translated_images/es/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nombre del Despliegue del Modelo** — Ve a **Modelos + Endpoints**, selecciona tu modelo desplegado y anota el **nombre del despliegue** (por ejemplo, `gpt-5-mini`).

### Paso 3: Inicia sesión en Azure con `az login`

Todos los notebooks usan **`AzureCliCredential`** para autenticación — no hay claves API que gestionar. Esto requiere que estés autenticado vía Azure CLI.

1. **Instala Azure CLI** si aún no lo has hecho: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Inicia sesión** ejecutando:

    ```bash|powershell
    az login
    ```

    O si estás en un entorno remoto/Codespace sin navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecciona tu suscripción** si se solicita — elige la que contenga tu proyecto Foundry.

4. **Verifica** que has iniciado sesión:

    ```bash|powershell
    az account show
    ```

> **¿Por qué `az login`?** Los notebooks se autentican usando `AzureCliCredential` del paquete `azure-identity`. Esto significa que tu sesión Azure CLI proporciona las credenciales — sin claves API o secretos en tu archivo `.env`. Esto es una [práctica recomendada de seguridad](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Paso 4: Crea tu archivo `.env`

Copia el archivo de ejemplo:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Abre `.env` y rellena estos dos valores:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | Dónde encontrarla |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → tu proyecto → página **Resumen** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Modelos + Endpoints** → nombre de tu modelo desplegado |

¡Eso es todo para la mayoría de las lecciones! Los notebooks se autenticarán automáticamente a través de tu sesión `az login`.

### Paso 5: Instala las Dependencias de Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos ejecutar esto dentro del entorno virtual que creaste anteriormente.

## Configuración Adicional para la Lección 5 (Agentic RAG)

La lección 5 usa **Azure AI Search** para generación aumentada por recuperación. Si planeas ejecutar esa lección, agrega estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → tu recurso **Azure AI Search** → **Resumen** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → tu recurso **Azure AI Search** → **Configuración** → **Claves** → clave administrativa primaria |

## Configuración Adicional para Lecciones que Llaman Azure OpenAI Directamente (Lecciones 6 y 8)

Algunos notebooks en las lecciones 6 y 8 llaman a **Azure OpenAI** directamente (usando la **API de Respuestas**) en lugar de pasar por un proyecto Microsoft Foundry. Estos ejemplos usaban anteriormente Modelos de GitHub, que están obsoletos (retiro en julio de 2026) y no soportan la API de Respuestas. Si planeas ejecutar esos ejemplos, agrega estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → tu recurso **Azure OpenAI** → **Claves y Endpoint** → Endpoint (ej. `https://<tu-recurso>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nombre de tu modelo desplegado (ej. `gpt-5-mini`) que soporta la API de Respuestas |
| `AZURE_OPENAI_API_KEY` | Opcional — solo si usas autenticación basada en clave en lugar de `az login` / Entra ID |

> La API de Respuestas usa el endpoint estable `/openai/v1/`, así que no se requiere `api-version`. Inicia sesión con `az login` para usar autenticación Entra ID sin clave.

## Proveedor Alternativo: MiniMax (Compatible con OpenAI)

[MiniMax](https://platform.minimaxi.com/) ofrece modelos de contexto grande (hasta 204K tokens) a través de una API compatible con OpenAI. Como el `OpenAIChatClient` del Microsoft Agent Framework funciona con cualquier endpoint compatible con OpenAI, puedes usar MiniMax como alternativa directa a Azure OpenAI o OpenAI.

Agrega estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Plataforma MiniMax](https://platform.minimaxi.com/) → Claves API |
| `MINIMAX_BASE_URL` | Usa `https://api.minimax.io/v1` (valor por defecto) |
| `MINIMAX_MODEL_ID` | Nombre del modelo a usar (ej., `MiniMax-M3`) |

**Modelos ejemplo**: `MiniMax-M3` (recomendado), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respuestas más rápidas). Los nombres y disponibilidad de modelos pueden cambiar con el tiempo, y el acceso a un modelo dado puede depender de tu cuenta o región — verifica la [Plataforma MiniMax](https://platform.minimaxi.com/) para la lista actual. Si `MiniMax-M3` no está disponible para tu cuenta, configura `MINIMAX_MODEL_ID` a un modelo al que tengas acceso (ej. `MiniMax-M2.7`).

Los ejemplos de código que usan `OpenAIChatClient` (ej., flujo de reserva de hotel de la Lección 14) detectarán y usarán automáticamente tu configuración MiniMax cuando `MINIMAX_API_KEY` esté configurado.

## Proveedor Alternativo: Foundry Local (Ejecuta Modelos en el Dispositivo)

[Foundry Local](https://foundrylocal.ai) es un runtime ligero que descarga, gestiona y sirve modelos de lenguaje **entero en tu propia máquina** a través de una API compatible con OpenAI — sin nube, sin suscripción Azure y sin claves API. Es una gran opción para desarrollo offline, experimentar sin costos en la nube o mantener datos en el dispositivo.

Como el `OpenAIChatClient` del Microsoft Agent Framework trabaja con cualquier endpoint compatible con OpenAI, Foundry Local es una alternativa local que se integra a Azure OpenAI.

**1. Instala Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Descarga y ejecuta un modelo** (esto también inicia el servicio local):

```bash
foundry model list          # ver modelos disponibles
foundry model run phi-4-mini
```

**3. Instala el SDK de Python** usado para descubrir el endpoint local:

```bash
pip install foundry-local-sdk
```

**4. Apunta el Microsoft Agent Framework a tu modelo local:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Descarga (si es necesario) y sirve el modelo localmente, luego descubre el endpoint/puerto.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # p.ej. http://localhost:<port>/v1
    api_key=manager.api_key,        # siempre "no requerido" para Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Nota:** Foundry Local expone un endpoint de **Chat Completions** compatible con OpenAI. Úsalo para desarrollo local y situaciones offline. Para el conjunto completo de funciones de la **API de Respuestas** (conversaciones con estado, orquestación profunda de herramientas y desarrollo estilo agente), usa **Azure OpenAI** o un proyecto **Microsoft Foundry** como se muestra en las lecciones. Consulta la [documentación de Foundry Local](https://foundrylocal.ai) para el catálogo actual de modelos y soporte de plataforma.

## Configuración Adicional para la Lección 8 (Flujo de Trabajo Bing Grounding)


El cuaderno de trabajo condicional en la lección 8 utiliza **Bing grounding** a través de Microsoft Foundry. Si planeas ejecutar ese ejemplo, agrega esta variable a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|------------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → tu proyecto → **Gestión** → **Recursos conectados** → tu conexión Bing → copia el ID de conexión |

## Solución de problemas

### Errores de verificación de certificado SSL en macOS

Si estás en macOS y encuentras un error como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este es un problema conocido con Python en macOS donde los certificados SSL del sistema no son confiados automáticamente. Prueba las siguientes soluciones en orden:

**Opción 1: Ejecutar el script de instalación de certificados de Python (recomendado)**

```bash
# Reemplace 3.XX con su versión de Python instalada (por ejemplo, 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opción 2: Usar `connection_verify=False` en tu cuaderno (solo para cuadernos Models de GitHub)**

En el cuaderno de la Lección 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ya se incluye una solución alternativa comentada. Descomenta `connection_verify=False` al crear el cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deshabilitar la verificación SSL si encuentra errores de certificado
)
```

> **⚠️ Advertencia:** Deshabilitar la verificación SSL (`connection_verify=False`) reduce la seguridad al saltarse la validación de certificados. Usa esto solo como solución temporal en entornos de desarrollo, nunca en producción.

**Opción 3: Instalar y usar `truststore`**

```bash
pip install truststore
```

Luego añade lo siguiente al inicio de tu cuaderno o script antes de hacer cualquier llamada de red:

```python
import truststore
truststore.inject_into_ssl()
```

## ¿Atascado en algún punto?

Si tienes algún problema al ejecutar esta configuración, únete a nuestro <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord de la Comunidad Azure AI</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crea un issue</a>.

## Próxima lección

Ahora estás listo para ejecutar el código de este curso. ¡Feliz aprendizaje sobre el mundo de los Agentes de IA! 

[Introducción a los Agentes de IA y Casos de uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->