# Configuración del Curso

## Introducción

Esta lección cubrirá cómo ejecutar los ejemplos de código de este curso.

## Únete a Otros Estudiantes y Obtén Ayuda

Antes de comenzar a clonar tu repositorio, únete al [canal de Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obtener ayuda con la configuración, cualquier pregunta sobre el curso o para conectar con otros estudiantes.

## Clona o Haz Fork de este Repo

Para comenzar, por favor clona o haz un fork del repositorio de GitHub. Esto creará tu propia versión del material del curso para que puedas ejecutar, probar y modificar el código.

Esto se puede hacer haciendo clic en el enlace para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">hacer fork del repositorio</a>

Ahora deberías tener tu propia versión bifurcada de este curso en el siguiente enlace:

![Forked Repo](../../../translated_images/es/forked-repo.33f27ca1901baa6a.webp)

### Clonación superficial (recomendada para taller / Codespaces)

  >El repositorio completo puede ser grande (~3 GB) cuando descargas todo el historial y todos los archivos. Si solo asistirás al taller o solo necesitas algunas carpetas de lecciones, una clonación superficial (o clonación parcial) evita la mayor parte de esa descarga al truncar el historial y/o saltarse blobs.

#### Clonación superficial rápida — historial mínimo, todos los archivos

Reemplaza `<your-username>` en los comandos a continuación con la URL de tu fork (o la URL upstream si prefieres).

Para clonar solo el historial del último commit (descarga pequeña):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar una rama específica:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonación parcial (sparse) — blobs mínimos + solo carpetas seleccionadas

Esto utiliza clonación parcial y sparse-checkout (requiere Git 2.25+ y se recomienda usar una versión moderna de Git con soporte para clonación parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Entra en la carpeta del repo:

```bash|powershell
cd ai-agents-for-beginners
```

Luego especifica qué carpetas quieres (el ejemplo a continuación muestra dos carpetas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Después de clonar y verificar los archivos, si solo necesitas los archivos y quieres liberar espacio (sin historial git), elimina los metadatos del repositorio (💀irreversible — perderás toda la funcionalidad de Git: sin commits, pulls, pushes ni acceso al historial).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usando GitHub Codespaces (recomendado para evitar descargas grandes locales)

- Crea un nuevo Codespace para este repo mediante la [interfaz de GitHub](https://github.com/codespaces).  

- En la terminal del codespace recién creado, ejecuta uno de los comandos de clonación superficial/parcial anteriores para traer solo las carpetas de lecciones que necesitas al espacio de trabajo del Codespace.
- Opcional: después de clonar dentro de Codespaces, elimina .git para recuperar espacio adicional (consulta los comandos de eliminación arriba).
- Nota: Si prefieres abrir el repo directamente en Codespaces (sin una clonación extra), ten en cuenta que Codespaces construirá el entorno devcontainer y podría provisionarte más de lo que necesitas. Clonar una copia superficial dentro de un Codespace nuevo te da más control sobre el uso del disco.

#### Consejos

- Siempre reemplaza la URL de clonación con tu fork si quieres editar / hacer commits.
- Si luego necesitas más historial o archivos, puedes obtenerlos o ajustar sparse-checkout para incluir carpetas adicionales.

## Ejecución del Código

Este curso ofrece una serie de Jupyter Notebooks que puedes ejecutar para obtener experiencia práctica construyendo Agentes de IA.

Los ejemplos de código usan **Microsoft Agent Framework (MAF)** con el `AzureAIProjectAgentProvider`, que se conecta a **Azure AI Agent Service V2** (la API de respuestas) a través de **Microsoft Foundry**.

Todos los notebooks Python están etiquetados como `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Si no tienes instalado Python3.12, asegúrate de instalarlo. Luego crea tu entorno virtual usando python3.12 para asegurarte de que se instalen las versiones correctas desde el archivo requirements.txt.
  
    >Ejemplo

    Crea el directorio del entorno virtual Python:

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

- .NET 10+: Para los códigos de ejemplo que usan .NET, asegúrate de instalar el [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o una versión posterior. Luego, verifica la versión SDK de .NET instalada:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Requerido para autenticación. Instálalo desde [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Suscripción de Azure** — Para acceder a Microsoft Foundry y Azure AI Agent Service.
- **Proyecto de Microsoft Foundry** — Un proyecto con un modelo desplegado (p.ej., `gpt-4o`). Ver [Paso 1](../../../00-course-setup) a continuación.

Hemos incluido un archivo `requirements.txt` en la raíz de este repositorio que contiene todos los paquetes Python necesarios para ejecutar los ejemplos de código.

Puedes instalarlos ejecutando el siguiente comando en tu terminal, desde la raíz del repositorio:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos crear un entorno virtual Python para evitar conflictos y problemas.

## Configura VSCode

Asegúrate de estar usando la versión correcta de Python en VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configura Microsoft Foundry y Azure AI Agent Service

### Paso 1: Crea un Proyecto Microsoft Foundry

Necesitas un **hub** y un **proyecto** de Azure AI Foundry con un modelo desplegado para ejecutar los notebooks.

1. Ve a [ai.azure.com](https://ai.azure.com) e inicia sesión con tu cuenta de Azure.
2. Crea un **hub** (o usa uno existente). Consulta: [Resumen de recursos del Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro del hub, crea un **proyecto**.
4. Despliega un modelo (p.ej., `gpt-4o`) desde **Modelos + Endpoints** → **Desplegar modelo**.

### Paso 2: Recupera el Endpoint de tu Proyecto y el Nombre de la Implementación del Modelo

Desde tu proyecto en el portal de Microsoft Foundry:

- **Endpoint del Proyecto** — Ve a la página de **Resumen** y copia la URL del endpoint.

![Project Connection String](../../../translated_images/es/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nombre de Despliegue del Modelo** — Ve a **Modelos + Endpoints**, selecciona tu modelo desplegado y anota el **Nombre del despliegue** (p.ej., `gpt-4o`).

### Paso 3: Inicia sesión en Azure con `az login`

Todos los notebooks utilizan **`AzureCliCredential`** para la autenticación — no hay claves API que administrar. Esto requiere que hayas iniciado sesión mediante la CLI de Azure.

1. **Instala Azure CLI** si aún no lo has hecho: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Inicia sesión** ejecutando:

    ```bash|powershell
    az login
    ```

    O si estás en un entorno remoto/Codespace sin navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecciona tu suscripción** si te lo solicita — elige la que contiene tu proyecto Foundry.

4. **Verifica** que estás conectado:

    ```bash|powershell
    az account show
    ```

> **¿Por qué `az login`?** Los notebooks se autentican usando `AzureCliCredential` del paquete `azure-identity`. Esto significa que tu sesión de Azure CLI proporciona las credenciales — no necesitas claves API ni secretos en tu archivo `.env`. Esto es una [mejor práctica de seguridad](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Abre `.env` y completa estos dos valores:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Dónde encontrarlo |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → tu proyecto → página de **Resumen** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Modelos + Endpoints** → nombre del modelo desplegado |

¡Eso es todo para la mayoría de las lecciones! Los notebooks se autenticarán automáticamente a través de tu sesión `az login`.

### Paso 5: Instala las Dependencias de Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos ejecutar esto dentro del entorno virtual que creaste antes.

## Configuración Adicional para la Lección 5 (Agentic RAG)

La lección 5 usa **Azure AI Search** para generación aumentada por recuperación. Si planeas ejecutar esa lección, añade estas variables a tu archivo `.env`:

| Variable | Dónde encontrarlo |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → tu recurso **Azure AI Search** → **Resumen** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → tu recurso **Azure AI Search** → **Configuración** → **Claves** → clave principal de administrador |

## Configuración Adicional para las Lecciones 6 y 8 (Modelos GitHub)

Algunos notebooks en las lecciones 6 y 8 usan **Modelos GitHub** en lugar de Azure AI Foundry. Si planeas ejecutar esos ejemplos, añade estas variables a tu archivo `.env`:

| Variable | Dónde encontrarlo |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Configuración** → **Configuración de desarrollador** → **Tokens de acceso personal** |
| `GITHUB_ENDPOINT` | Usa `https://models.inference.ai.azure.com` (valor predeterminado) |
| `GITHUB_MODEL_ID` | Nombre del modelo a usar (e.g., `gpt-4o-mini`) |

## Configuración Adicional para la Lección 8 (Flujo de Trabajo Bing Grounding)

El notebook de flujo de trabajo condicional en la lección 8 usa **Bing grounding** vía Azure AI Foundry. Si planeas ejecutar ese ejemplo, añade esta variable a tu archivo `.env`:

| Variable | Dónde encontrarlo |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Azure AI Foundry → tu proyecto → **Administración** → **Recursos conectados** → tu conexión Bing → copia el ID de conexión |

## Resolución de Problemas

### Errores de Verificación de Certificado SSL en macOS

Si estás en macOS y ves un error así:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este es un problema conocido con Python en macOS donde los certificados SSL del sistema no se confían automáticamente. Prueba las siguientes soluciones en orden:

**Opción 1: Ejecuta el script Install Certificates de Python (recomendado)**

```bash
# Reemplace 3.XX con la versión de Python que tiene instalada (por ejemplo, 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opción 2: Usa `connection_verify=False` en tu notebook (solo para notebooks de Modelos GitHub)**

En el notebook de la Lección 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ya hay una solución alternativa comentada. Descomenta `connection_verify=False` cuando crees el cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deshabilitar la verificación SSL si encuentra errores de certificado
)
```

> **⚠️ Advertencia:** Deshabilitar la verificación SSL (`connection_verify=False`) reduce la seguridad al omitir la validación del certificado. Utilízalo solo como una solución temporal en entornos de desarrollo, nunca en producción.

**Opción 3: Instala y usa `truststore`**

```bash
pip install truststore
```

Luego añade lo siguiente al inicio de tu notebook o script antes de hacer cualquier llamada en red:

```python
import truststore
truststore.inject_into_ssl()
```

## ¿Atascado en algún punto?

Si tienes problemas para ejecutar esta configuración, únete a nuestro <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord de la Comunidad Azure AI</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crea un issue</a>.

## Próxima Lección

Ahora ya estás listo para ejecutar el código de este curso. ¡Disfruta aprendiendo más sobre el mundo de los Agentes de IA!

[Introducción a Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la exactitud, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->