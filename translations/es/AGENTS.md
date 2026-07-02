# AGENTS.md

## Descripción general del proyecto

Este repositorio contiene "Agentes de IA para Principiantes": un curso educativo completo que enseña todo lo necesario para construir Agentes de IA. El curso consta de 18 lecciones que cubren fundamentos, patrones de diseño, frameworks y despliegue en producción de agentes de IA.

**Tecnologías clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Servicios de Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-15+)
- Cada lección contiene: documentación README, ejemplos de código (notebooks de Jupyter) e imágenes
- Soporte multilingüe mediante sistema automatizado de traducción
- Un notebook de Python por lección usando Microsoft Agent Framework

## Comandos de configuración

### Requisitos previos
- Python 3.12 o superior
- Suscripción a Azure (para Azure AI Foundry)
- CLI de Azure instalada y autenticada (`az login`)

### Configuración inicial

1. **Clona o bifurca el repositorio:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crea y activa un entorno virtual de Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   ```bash
   cp .env.example .env
   # Edita .env con tus claves API y puntos de acceso
   ```

### Variables de entorno requeridas

Para **Azure AI Foundry** (Requerido):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint del proyecto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nombre del despliegue del modelo (por ejemplo, gpt-4o)

Para **Azure AI Search** (Lección 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint de Azure AI Search
- `AZURE_SEARCH_API_KEY` - Clave API de Azure AI Search

Autenticación: Ejecuta `az login` antes de correr los notebooks (usa `AzureCliCredential`).

## Flujo de desarrollo

### Ejecución de Jupyter Notebooks

Cada lección contiene múltiples notebooks para diferentes frameworks:

1. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar al directorio de una lección** (p. ej., `01-intro-to-ai-agents/code_samples/`)

3. **Abrir y ejecutar notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabajando con Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requiere suscripción a Azure
- Utiliza `AzureAIProjectAgentProvider` para Agent Service V2 (agentes visibles en portal Foundry)
- Listo para producción con observabilidad incorporada
- Patrón de archivo: `*-python-agent-framework.ipynb`

## Instrucciones de prueba

Este es un repositorio educativo con código de ejemplo y no código de producción con pruebas automatizadas. Para verificar tu configuración y cambios:

### Pruebas manuales

1. **Prueba el entorno Python:**
   ```bash
   python --version  # Debe ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Prueba la ejecución del notebook:**
   ```bash
   # Convertir el cuaderno a script y ejecutar (prueba de importaciones)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica las variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Ejecución de notebooks individuales

Abre los notebooks en Jupyter y ejecuta las celdas secuencialmente. Cada notebook es autónomo e incluye:
- Declaraciones de importación
- Carga de configuración
- Implementaciones de agentes de ejemplo
- Salidas esperadas en celdas markdown

## Estilo de código

### Convenciones de Python

- **Versión Python**: 3.12+
- **Estilo de código**: Sigue las convenciones estándar PEP 8 de Python
- **Notebooks**: Utiliza celdas de markdown claras para explicar conceptos
- **Imports**: Agrupa por biblioteca estándar, terceros, importaciones locales

### Convenciones para Jupyter Notebook

- Incluye celdas de markdown descriptivas antes de las de código
- Añade ejemplos de salida en los notebooks como referencia
- Usa nombres de variables claros que coincidan con conceptos de la lección
- Mantén el orden de ejecución lineal del notebook (celda 1 → 2 → 3...)

### Organización de archivos

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construcción y despliegue

### Construcción de documentación

Este repositorio usa Markdown para la documentación:
- Archivos README.md en cada carpeta de lección
- README.md principal en la raíz del repositorio
- Sistema automatizado de traducción vía GitHub Actions

### Pipeline CI/CD

Ubicado en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a creadores de nuevos issues
3. **welcome-pr.yml** - Da la bienvenida a colaboradores de pull requests

### Despliegue

Este es un repositorio educativo - no hay proceso de despliegue. Los usuarios:
1. Hacen fork o clonación del repositorio
2. Ejecutan los notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con los ejemplos

## Directrices para Pull Requests

### Antes de enviar

1. **Prueba tus cambios:**
   - Ejecuta completamente los notebooks afectados
   - Verifica que todas las celdas se ejecuten sin errores
   - Comprueba que las salidas sean apropiadas

2. **Actualizaciones de documentación:**
   - Actualiza README.md si agregas nuevos conceptos
   - Añade comentarios en notebooks para código complejo
   - Asegúrate de que las celdas markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evita subir archivos `.env` (usa `.env.example`)
   - No subas directorios `venv/` o `__pycache__/`
   - Mantén las salidas de notebooks cuando demuestren conceptos
   - Elimina archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato de título para PR

Usa títulos descriptivos:
- `[Lesson-XX] Añadir nuevo ejemplo para <concepto>`
- `[Fix] Corregir error tipográfico en README de la lección XX`
- `[Update] Mejorar ejemplo de código en la lección XX`
- `[Docs] Actualizar instrucciones de configuración`

### Chequeos requeridos

- Los notebooks deben ejecutarse sin errores
- Archivos README deben ser claros y precisos
- Sigue los patrones de código existentes en el repositorio
- Mantén la consistencia con otras lecciones

## Notas adicionales

### Errores comunes

1. **Incompatibilidad de versión de Python:**
   - Asegúrate de usar Python 3.12+
   - Algunos paquetes pueden no funcionar con versiones anteriores
   - Usa `python3 -m venv` para especificar la versión explícitamente

2. **Variables de entorno:**
   - Siempre crea `.env` a partir de `.env.example`
   - No subas el archivo `.env` (está en `.gitignore`)
   - El token de GitHub requiere permisos adecuados

3. **Conflictos de paquetes:**
   - Usa un entorno virtual limpio
   - Instala desde `requirements.txt` en vez de paquetes individuales
   - Algunos notebooks pueden requerir paquetes adicionales mencionados en sus celdas markdown

4. **Servicios de Azure:**
   - Los servicios de Azure AI requieren suscripción activa
   - Algunas características son específicas de región
   - Aplican limitaciones de nivel gratuito para GitHub Models

### Ruta de aprendizaje

Progresión recomendada a través de las lecciones:
1. **00-course-setup** - Comienza aquí para configuración del entorno
2. **01-intro-to-ai-agents** - Entiende los fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Aprende sobre diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño clave
5. Continúa con las lecciones numeradas secuencialmente

### Selección de framework

Elige el framework según tus objetivos:
- **Todas las lecciones**: Microsoft Agent Framework (MAF) con `AzureAIProjectAgentProvider`
- **Agentes se registran del lado servidor** en Azure AI Foundry Agent Service V2 y son visibles en el portal Foundry

### Obtener ayuda

- Únete a la [Comunidad Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)
- Revisa los archivos README de las lecciones para guías específicas
- Consulta el [README.md principal](./README.md) para visión general del curso
- Consulta [Course Setup](./00-course-setup/README.md) para instrucciones detalladas

### Colaboración

Este es un proyecto educativo abierto. Se aceptan contribuciones:
- Mejorar ejemplos de código
- Corregir errores tipográficos o de código
- Añadir comentarios aclaratorios
- Sugerir nuevos temas para lecciones
- Traducir a idiomas adicionales

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto específico del proyecto

### Soporte multilingüe

Este repositorio usa un sistema automatizado de traducción:
- Soporte para más de 50 idiomas
- Traducciones en directorios `/translations/<código-idoma>/`
- Workflow de GitHub Actions maneja actualizaciones de traducción
- Archivos fuente están en inglés en la raíz del repositorio

### Estructura de las lecciones

Cada lección sigue un patrón consistente:
1. Miniatura de video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y prerrequisitos
5. Recursos adicionales vinculados

### Nomenclatura de ejemplos de código

Formato: `<número-lección>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lección 1, MAF Python
- `14-sequential.ipynb` - Lección 14, patrones avanzados MAF

### Directorios especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración de contenedor de desarrollo para VS Code
- `.github/` - Workflows y plantillas de GitHub Actions

### Dependencias

Paquetes clave desde `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Soporte para protocolo Agente a Agente
- `azure-ai-inference`, `azure-ai-projects` - Servicios Azure AI
- `azure-identity` - Autenticación Azure (AzureCliCredential)
- `azure-search-documents` - Integración Azure AI Search
- `mcp[cli]` - Soporte para Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->