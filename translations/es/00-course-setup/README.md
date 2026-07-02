# Configuración del Curso

## Introducción

Esta lección cubrirá cómo ejecutar los ejemplos de código de este curso.

## Únete a Otros Estudiantes y Obtén Ayuda

Antes de comenzar a clonar tu repositorio, únete al [canal de Discord de AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obtener ayuda con la configuración, cualquier pregunta sobre el curso o para conectar con otros estudiantes.

## Clona o Haz Fork de este Repositorio

Para comenzar, por favor clona o haz fork del repositorio de GitHub. Esto creará tu propia versión del material del curso para que puedas ejecutar, probar y ajustar el código.

Esto se puede hacer haciendo clic en el enlace para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">hacer fork del repositorio</a>.

Ahora deberías tener tu propia versión bifurcada de este curso en el siguiente enlace:

![Forked Repo](../../../translated_images/es/forked-repo.33f27ca1901baa6a.webp)

### Clonación superficial (recomendada para taller / Codespaces)

  >El repositorio completo puede ser grande (~3 GB) cuando descargas todo el historial y todos los archivos. Si sólo vas a asistir al taller o sólo necesitas algunas carpetas de lecciones, una clonación superficial (o clonación parcial) evita la mayor parte de esa descarga truncando el historial y/o saltándose blobs.

#### Clonación superficial rápida — historial mínimo, todos los archivos

Reemplaza `<your-username>` en los comandos a continuación con la URL de tu fork (o con la URL upstream si prefieres).

Para clonar sólo el historial del último commit (descarga pequeña):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para clonar una rama específica:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonación parcial (sparse) — blobs mínimos + sólo carpetas seleccionadas

Esto utiliza clonación parcial y sparse-checkout (requiere Git 2.25+ y se recomienda Git moderno con soporte de clonación parcial):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ingresa a la carpeta del repositorio:

```bash|powershell
cd ai-agents-for-beginners
```

Luego especifica qué carpetas quieres (el ejemplo a continuación muestra dos carpetas):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Después de clonar y verificar los archivos, si sólo necesitas los archivos y quieres liberar espacio (sin historial git), por favor elimina los metadatos del repositorio (💀 irreversible — perderás toda la funcionalidad Git: no commits, pulls, pushes ni acceso al historial).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usando GitHub Codespaces (recomendado para evitar descargas locales grandes)

- Crea un nuevo Codespace para este repositorio vía la [interfaz de GitHub](https://github.com/codespaces).

- En la terminal del codespace recién creado, ejecuta uno de los comandos de clonación superficial o parcial arriba para traer sólo las carpetas de lecciones que necesitas al espacio de trabajo del Codespace.
- Opcional: después de clonar dentro de Codespaces, elimina .git para recuperar espacio adicional (ver comandos de eliminación arriba).
- Nota: Si prefieres abrir el repositorio directamente en Codespaces (sin una clonación extra), ten en cuenta que Codespaces construirá el entorno devcontainer y puede que aún provea más de lo que necesitas. Clonar una copia superficial dentro de un Codespace fresco te da más control sobre el uso de disco.

#### Consejos

- Siempre reemplaza la URL de clonación con la de tu fork si quieres editar/hacer commits.
- Si luego necesitas más historial o archivos, puedes obtenerlos o ajustar sparse-checkout para incluir carpetas adicionales.

## Ejecución del Código

Este curso ofrece una serie de Jupyter Notebooks que puedes ejecutar para obtener experiencia práctica construyendo Agentes de IA.

Los ejemplos de código usan **Microsoft Agent Framework (MAF)** con el `AzureAIProjectAgentProvider`, que conecta a **Azure AI Agent Service V2** (la API Responses) a través de **Microsoft Foundry**.

Todos los notebooks de Python están etiquetados como `*-python-agent-framework.ipynb`.

## Requisitos

- Python 3.12+
  - **NOTA**: Si no tienes instalado Python3.12, asegúrate de instalarlo. Luego crea tu entorno virtual usando python3.12 para garantizar que se instalen las versiones correctas desde el archivo requirements.txt.
  
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

- .NET 10+: Para los ejemplos que usan .NET, asegúrate de instalar [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o posterior. Luego verifica la versión del SDK .NET instalado:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Requerido para autenticación. Instálalo desde [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Suscripción de Azure** — Para acceder a Microsoft Foundry y Azure AI Agent Service.
- **Proyecto Microsoft Foundry** — Un proyecto con un modelo desplegado (e.g., `gpt-4o`). Ver [Paso 1](#paso-1-crea-un-proyecto-microsoft-foundry) abajo.

Hemos incluido un archivo `requirements.txt` en la raíz de este repositorio que contiene todos los paquetes Python requeridos para ejecutar los ejemplos de código.

Puedes instalarlos ejecutando el siguiente comando en tu terminal en la raíz del repositorio:

```bash|powershell
pip install -r requirements.txt
```

Recomendamos crear un entorno virtual Python para evitar cualquier conflicto o problema.

## Configurar VSCode

Asegúrate de que estás usando la versión correcta de Python en VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurar Microsoft Foundry y Azure AI Agent Service

### Paso 1: Crea un Proyecto Microsoft Foundry

Necesitas un hub y proyecto de Azure AI Foundry con un modelo desplegado para ejecutar los notebooks.

1. Ve a [ai.azure.com](https://ai.azure.com) e inicia sesión con tu cuenta de Azure.
2. Crea un **hub** (o usa uno existente). Consulta: [Resumen de recursos de Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Dentro del hub, crea un **proyecto**.
4. Despliega un modelo (e.g., `gpt-4o`) desde **Models + Endpoints** → **Deploy model**.

### Paso 2: Obtén Endpoint del Proyecto y Nombre del Despliegue del Modelo

Desde tu proyecto en el portal Microsoft Foundry:

- **Endpoint del Proyecto** — Ve a la página de **Overview** y copia la URL del endpoint.

![Project Connection String](../../../translated_images/es/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nombre del Despliegue del Modelo** — Ve a **Models + Endpoints**, selecciona tu modelo desplegado y anota el **Deployment name** (e.g., `gpt-4o`).

### Paso 3: Inicia sesión en Azure con `az login`

Todos los notebooks usan **`AzureCliCredential`** para autenticación — no hay claves API que administrar. Esto requiere que inicies sesión mediante la CLI de Azure.

1. **Instala Azure CLI** si no lo tienes: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Inicia sesión** ejecutando:

    ```bash|powershell
    az login
    ```

    O si estás en un entorno remoto o Codespace sin navegador:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecciona tu suscripción** si te lo solicita — elige la que contiene tu proyecto Foundry.

4. **Verifica** que hayas iniciado sesión:

    ```bash|powershell
    az account show
    ```

> **¿Por qué `az login`?** Los notebooks se autentican usando `AzureCliCredential` del paquete `azure-identity`. Esto significa que tu sesión de Azure CLI provee las credenciales — no claves API ni secretos en tu archivo `.env`. Esto es una [mejor práctica de seguridad](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Paso 4: Crea tu Archivo `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Dónde encontrarla |
|----------|-------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → tu proyecto → página de **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nombre del modelo desplegado |

¡Eso es todo para la mayoría de las lecciones! Los notebooks se autenticarán automáticamente mediante tu sesión de `az login`.

### Paso 5: Instala las Dependencias de Python

```bash|powershell
pip install -r requirements.txt
```

Recomendamos ejecutar esto dentro del entorno virtual que creaste antes.

## Configuración Adicional para la Lección 5 (Agentic RAG)

La lección 5 usa **Azure AI Search** para generación aumentada por recuperación. Si planeas ejecutar esa lección, añade estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-------------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → tu recurso de **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → tu recurso de **Azure AI Search** → **Settings** → **Keys** → clave primaria de administrador |

## Configuración Adicional para la Lección 6 y Lección 8 (Modelos GitHub)

Algunos notebooks de las lecciones 6 y 8 usan **Modelos GitHub** en vez de Azure AI Foundry. Si planeas ejecutar esos ejemplos, añade estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-------------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Usa `https://models.inference.ai.azure.com` (valor por defecto) |
| `GITHUB_MODEL_ID` | Nombre del modelo a usar (e.g. `gpt-4o-mini`) |

## Proveedor Alternativo: MiniMax (Compatible con OpenAI)

[MiniMax](https://platform.minimaxi.com/) provee modelos de contexto largo (hasta 204K tokens) mediante una API compatible con OpenAI. Como el `OpenAIChatClient` del Microsoft Agent Framework funciona con cualquier endpoint compatible con OpenAI, puedes usar MiniMax como alternativa directa a Modelos GitHub o OpenAI.

Añade estas variables a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-------------------|
| `MINIMAX_API_KEY` | [Plataforma MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Usa `https://api.minimax.io/v1` (valor por defecto) |
| `MINIMAX_MODEL_ID` | Nombre del modelo a usar (e.g., `MiniMax-M3`) |

**Modelos ejemplo**: `MiniMax-M3` (recomendado), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (respuestas más rápidas). Los nombres y la disponibilidad de modelos pueden cambiar con el tiempo y el acceso puede depender de tu cuenta o región — consulta la [Plataforma MiniMax](https://platform.minimaxi.com/) para la lista actual. Si `MiniMax-M3` no está disponible para tu cuenta, configura `MINIMAX_MODEL_ID` a un modelo al que tengas acceso (e.g., `MiniMax-M2.7`).

Los ejemplos de código que usan `OpenAIChatClient` (e.g., el flujo de reserva de hotel de la Lección 14) detectarán y usarán automáticamente tu configuración MiniMax cuando `MINIMAX_API_KEY` esté definido.

## Configuración Adicional para la Lección 8 (Flujo de Trabajo con Base Bing)

El notebook con flujo condicional en la lección 8 usa **Bing grounding** vía Azure AI Foundry. Si planeas ejecutar ese ejemplo, añade esta variable a tu archivo `.env`:

| Variable | Dónde encontrarla |
|----------|-------------------|
| `BING_CONNECTION_ID` | Portal Azure AI Foundry → tu proyecto → **Management** → **Connected resources** → tu conexión Bing → copia el ID de conexión |

## Solución de Problemas

### Errores de Verificación de Certificado SSL en macOS

Si estás en macOS y encuentras un error como:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Este es un problema conocido con Python en macOS donde los certificados SSL del sistema no son automáticamente confiables. Prueba las siguientes soluciones en orden:

**Opción 1: Ejecuta el script Install Certificates de Python (recomendado)**

```bash
# Reemplace 3.XX con su versión de Python instalada (por ejemplo, 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opción 2: Usa `connection_verify=False` en tu notebook (solo para notebooks de Modelos GitHub)**

En el notebook de la Lección 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ya hay una solución alternativa comentada. Descomenta `connection_verify=False` al crear el cliente:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Desactivar la verificación SSL si encuentras errores de certificado
)
```

> **⚠️ Advertencia:** Deshabilitar la verificación SSL (`connection_verify=False`) reduce la seguridad al omitir la validación del certificado. Usa esto solo como una solución temporal en entornos de desarrollo, nunca en producción.

**Opción 3: Instala y usa `truststore`**

```bash
pip install truststore
```

Luego añade lo siguiente al inicio de tu notebook o script antes de hacer cualquier llamada de red:

```python
import truststore
truststore.inject_into_ssl()
```

## ¿Atascado en algún paso?

Si tienes algún problema ejecutando esta configuración, únete a nuestra <a href="https://discord.gg/kzRShWzttr" target="_blank">Comunidad Azure AI Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crea un issue</a>.
## Próxima lección

Ahora estás listo para ejecutar el código de este curso. ¡Feliz aprendizaje sobre el mundo de los Agentes de IA!

[Introducción a los Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->