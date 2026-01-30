# AGENTS.md

## Resumen del Proyecto

Este repositorio contiene "Agentes de IA para Principiantes", un curso educativo completo que enseña todo lo necesario para construir agentes de IA. El curso consta de más de 15 lecciones que abarcan fundamentos, patrones de diseño, frameworks y despliegue en producción de agentes de IA.

**Tecnologías Clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Servicios de Azure AI: Azure AI Foundry, Azure AI Agent Service
- Marketplace de Modelos de GitHub (disponible en nivel gratuito)

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-15+)
- Cada lección incluye: documentación README, ejemplos de código (notebooks de Jupyter) e imágenes
- Soporte multilingüe mediante sistema de traducción automatizado
- Opciones de múltiples frameworks por lección (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Comandos de Configuración

### Requisitos Previos
- Python 3.12 o superior
- Cuenta de GitHub (para Modelos de GitHub - nivel gratuito)
- Suscripción a Azure (opcional, para servicios de Azure AI)

### Configuración Inicial

1. **Clonar o bifurcar el repositorio:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crear y activar un entorno virtual de Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Variables de Entorno Requeridas

Para **Modelos de GitHub (Gratis)**:
- `GITHUB_TOKEN` - Token de acceso personal de GitHub

Para **Servicios de Azure AI** (opcional):
- `PROJECT_ENDPOINT` - Endpoint del proyecto Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Clave API de Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL del endpoint de Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nombre del despliegue para el modelo de chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nombre del despliegue para embeddings
- Configuración adicional de Azure como se muestra en `.env.example`

## Flujo de Trabajo de Desarrollo

### Ejecutar Jupyter Notebooks

Cada lección contiene múltiples notebooks de Jupyter para diferentes frameworks:

1. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar a un directorio de lección** (por ejemplo, `01-intro-to-ai-agents/code_samples/`)

3. **Abrir y ejecutar notebooks:**
   - `*-semantic-kernel.ipynb` - Usando el framework Semantic Kernel
   - `*-autogen.ipynb` - Usando el framework AutoGen
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Usando Azure AI Agent Service

### Trabajar con Diferentes Frameworks

**Semantic Kernel + Modelos de GitHub:**
- Nivel gratuito disponible con cuenta de GitHub
- Ideal para aprendizaje y experimentación
- Patrón de archivo: `*-semantic-kernel*.ipynb`

**AutoGen + Modelos de GitHub:**
- Nivel gratuito disponible con cuenta de GitHub
- Capacidades de orquestación multi-agente
- Patrón de archivo: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Framework más reciente de Microsoft
- Disponible en Python y .NET
- Patrón de archivo: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Requiere suscripción a Azure
- Funciones listas para producción
- Patrón de archivo: `*-azureaiagent.ipynb`

## Instrucciones de Pruebas

Este es un repositorio educativo con código de ejemplo en lugar de código de producción con pruebas automatizadas. Para verificar tu configuración y cambios:

### Pruebas Manuales

1. **Probar el entorno de Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Probar la ejecución de notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificar las variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Ejecutar Notebooks Individuales

Abre los notebooks en Jupyter y ejecuta las celdas de forma secuencial. Cada notebook es autónomo e incluye:
- Declaraciones de importación
- Carga de configuración
- Implementaciones de agentes de ejemplo
- Resultados esperados en celdas de markdown

## Estilo de Código

### Convenciones de Python

- **Versión de Python**: 3.12+
- **Estilo de Código**: Seguir las convenciones estándar de Python PEP 8
- **Notebooks**: Usar celdas de markdown claras para explicar conceptos
- **Importaciones**: Agrupar por biblioteca estándar, terceros, importaciones locales

### Convenciones de Jupyter Notebook

- Incluir celdas de markdown descriptivas antes de las celdas de código
- Agregar ejemplos de salida en los notebooks como referencia
- Usar nombres de variables claros que coincidan con los conceptos de la lección
- Mantener el orden de ejecución del notebook lineal (celda 1 → 2 → 3...)

### Organización de Archivos

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Construcción y Despliegue

### Construcción de Documentación

Este repositorio utiliza Markdown para la documentación:
- Archivos README.md en cada carpeta de lección
- README.md principal en la raíz del repositorio
- Sistema de traducción automatizado mediante GitHub Actions

### Pipeline de CI/CD

Ubicado en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a los creadores de nuevos issues
3. **welcome-pr.yml** - Da la bienvenida a los contribuyentes de nuevos pull requests

### Despliegue

Este es un repositorio educativo - no hay proceso de despliegue. Los usuarios:
1. Bifurcan o clonan el repositorio
2. Ejecutan los notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con los ejemplos

## Directrices para Pull Requests

### Antes de Enviar

1. **Probar tus cambios:**
   - Ejecutar completamente los notebooks afectados
   - Verificar que todas las celdas se ejecuten sin errores
   - Comprobar que las salidas sean apropiadas

2. **Actualizaciones de documentación:**
   - Actualizar README.md si se agregan nuevos conceptos
   - Agregar comentarios en los notebooks para código complejo
   - Asegurarse de que las celdas de markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evitar comprometer archivos `.env` (usar `.env.example`)
   - No comprometer directorios `venv/` o `__pycache__/`
   - Mantener las salidas de los notebooks cuando demuestren conceptos
   - Eliminar archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato de Título de PR

Usar títulos descriptivos:
- `[Lesson-XX] Agregar nuevo ejemplo para <concepto>`
- `[Fix] Corregir error tipográfico en README de la lección-XX`
- `[Update] Mejorar ejemplo de código en la lección-XX`
- `[Docs] Actualizar instrucciones de configuración`

### Verificaciones Requeridas

- Los notebooks deben ejecutarse sin errores
- Los archivos README deben ser claros y precisos
- Seguir los patrones de código existentes en el repositorio
- Mantener consistencia con otras lecciones

## Notas Adicionales

### Problemas Comunes

1. **Incompatibilidad de versión de Python:**
   - Asegurarse de usar Python 3.12+
   - Algunos paquetes pueden no funcionar con versiones anteriores
   - Usar `python3 -m venv` para especificar la versión de Python explícitamente

2. **Variables de entorno:**
   - Siempre crear `.env` a partir de `.env.example`
   - No comprometer el archivo `.env` (está en `.gitignore`)
   - El token de GitHub necesita permisos adecuados

3. **Conflictos de paquetes:**
   - Usar un entorno virtual nuevo
   - Instalar desde `requirements.txt` en lugar de paquetes individuales
   - Algunos notebooks pueden requerir paquetes adicionales mencionados en sus celdas de markdown

4. **Servicios de Azure:**
   - Los servicios de Azure AI requieren una suscripción activa
   - Algunas funciones son específicas de la región
   - Las limitaciones del nivel gratuito se aplican a los Modelos de GitHub

### Ruta de Aprendizaje

Progresión recomendada a través de las lecciones:
1. **00-course-setup** - Comienza aquí para configurar el entorno
2. **01-intro-to-ai-agents** - Comprender los fundamentos de los agentes de IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño principales
5. Continuar con las lecciones numeradas de forma secuencial

### Selección de Framework

Elegir el framework según tus objetivos:
- **Aprendizaje/Prototipado**: Semantic Kernel + Modelos de GitHub (gratis)
- **Sistemas multi-agente**: AutoGen
- **Últimas características**: Microsoft Agent Framework (MAF)
- **Despliegue en producción**: Azure AI Agent Service

### Obtener Ayuda

- Únete al [Discord de la Comunidad Azure AI Foundry](https://aka.ms/ai-agents/discord)
- Revisa los archivos README de las lecciones para orientación específica
- Consulta el [README.md principal](./README.md) para una visión general del curso
- Refiérete a [Configuración del Curso](./00-course-setup/README.md) para instrucciones detalladas de configuración

### Contribuir

Este es un proyecto educativo abierto. Contribuciones bienvenidas:
- Mejorar ejemplos de código
- Corregir errores tipográficos o errores
- Agregar comentarios aclaratorios
- Sugerir nuevos temas de lección
- Traducir a idiomas adicionales

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto Específico del Proyecto

### Soporte Multilingüe

Este repositorio utiliza un sistema de traducción automatizado:
- Más de 50 idiomas soportados
- Traducciones en directorios `/translations/<lang-code>/`
- El flujo de trabajo de GitHub Actions maneja las actualizaciones de traducción
- Los archivos fuente están en inglés en la raíz del repositorio

### Estructura de las Lecciones

Cada lección sigue un patrón consistente:
1. Miniatura de video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y requisitos previos
5. Recursos de aprendizaje adicionales enlazados

### Nomenclatura de Ejemplos de Código

Formato: `<número-lección>-<nombre-framework>.ipynb`
- `04-semantic-kernel.ipynb` - Lección 4, Semantic Kernel
- `07-autogen.ipynb` - Lección 7, AutoGen
- `14-python-agent-framework.ipynb` - Lección 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lección 14, MAF .NET

### Directorios Especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración del contenedor de desarrollo de VS Code
- `.github/` - Flujos de trabajo y plantillas de GitHub Actions

### Dependencias

Paquetes clave de `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Framework AutoGen
- `semantic-kernel` - Framework Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Servicios de Azure AI
- `azure-search-documents` - Integración de búsqueda de Azure AI
- `chromadb` - Base de datos vectorial para ejemplos RAG
- `chainlit` - Framework de interfaz de chat
- `browser_use` - Automatización de navegador para agentes
- `mcp[cli]` - Soporte para Model Context Protocol
- `mem0ai` - Gestión de memoria para agentes

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.