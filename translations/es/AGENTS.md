# AGENTS.md

## Descripción del Proyecto

Este repositorio contiene "Agentes de IA para Principiantes", un curso educativo integral que enseña todo lo necesario para construir agentes de IA. El curso consta de más de 15 lecciones que cubren fundamentos, patrones de diseño, frameworks y despliegue en producción de agentes de IA.

**Tecnologías Clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Servicios de Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-15+)
- Cada lección contiene: documentación README, ejemplos de código (notebooks Jupyter) e imágenes
- Soporte multilenguaje mediante sistema automático de traducción
- Un notebook de Python por lección utilizando Microsoft Agent Framework

## Comandos de Configuración

### Requisitos Previos
- Python 3.12 o superior
- Suscripción a Azure (para Azure AI Foundry)
- Azure CLI instalado y autenticado (`az login`)

### Configuración Inicial

1. **Clonar o bifurcar el repositorio:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crear y activar entorno virtual de Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Edita .env con tus claves API y puntos finales
   ```

### Variables de Entorno Requeridas

Para **Azure AI Foundry** (Obligatorio):
- `AZURE_AI_PROJECT_ENDPOINT` - Punto de acceso del proyecto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nombre del despliegue del modelo (ej., gpt-4o)

Para **Azure AI Search** (Lección 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Punto de acceso de Azure AI Search
- `AZURE_SEARCH_API_KEY` - Clave API de Azure AI Search

Autenticación: Ejecutar `az login` antes de usar los notebooks (usa `AzureCliCredential`).

## Flujo de Desarrollo

### Ejecutando Jupyter Notebooks

Cada lección contiene varios notebooks Jupyter para diferentes frameworks:

1. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar al directorio de una lección** (ejemplo: `01-intro-to-ai-agents/code_samples/`)

3. **Abrir y ejecutar notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabajando con Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requiere suscripción a Azure
- Usa `AzureAIProjectAgentProvider` para el Agent Service V2 (agentes visibles en portal Foundry)
- Listo para producción con observabilidad integrada
- Patrón de archivo: `*-python-agent-framework.ipynb`

## Instrucciones de Pruebas

Este es un repositorio educativo con código de ejemplo, no código de producción con pruebas automatizadas. Para verificar la configuración y cambios:

### Pruebas Manuales

1. **Probar entorno Python:**
   ```bash
   python --version  # Debe ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Probar ejecución de notebooks:**
   ```bash
   # Convertir el cuaderno a script y ejecutar (prueba importaciones)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificar variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Ejecutar Notebooks Individuales

Abrir notebooks en Jupyter y ejecutar celdas secuencialmente. Cada notebook es autónomo e incluye:
- Sentencias de importación
- Carga de configuración
- Implementaciones de agentes de ejemplo
- Resultados esperados en celdas markdown

## Estilo de Código

### Convenciones en Python

- **Versión de Python**: 3.12+
- **Estilo de Código**: Seguir las convenciones estándar PEP 8 de Python
- **Notebooks**: Usar celdas markdown claras para explicar conceptos
- **Imports**: Agrupar por librería estándar, terceros, locales

### Convenciones en Jupyter Notebooks

- Incluir celdas markdown descriptivas antes de las celdas de código
- Añadir ejemplos de salida en los notebooks como referencia
- Usar nombres de variables claros que coincidan con conceptos de la lección
- Mantener orden lineal en la ejecución (celda 1 → 2 → 3...)

### Organización de Archivos

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Construcción y Despliegue

### Construcción de Documentación

Este repositorio utiliza Markdown para documentación:
- Archivos README.md en cada carpeta de lección
- README.md principal en la raíz del repositorio
- Sistema automático de traducción mediante GitHub Actions

### Pipeline CI/CD

Ubicado en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a creadores de Issues nuevos
3. **welcome-pr.yml** - Da la bienvenida a contribuyentes de Pull Requests nuevos

### Despliegue

Este es un repositorio educativo - no hay proceso de despliegue. Los usuarios:
1. Bifurcan o clonan el repositorio
2. Ejecutan notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con los ejemplos

## Directrices para Pull Requests

### Antes de Enviar

1. **Pruebe sus cambios:**
   - Ejecute completamente los notebooks afectados
   - Verifique que todas las celdas se ejecuten sin errores
   - Compruebe que los resultados sean apropiados

2. **Actualizaciones de documentación:**
   - Actualice README.md si agrega nuevos conceptos
   - Añada comentarios en notebooks para código complejo
   - Asegure que las celdas markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evite subir archivos `.env` (usar `.env.example`)
   - No subir directorios `venv/` ni `__pycache__/`
   - Mantenga salidas de notebooks cuando demuestren conceptos
   - Elimine archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato de Título para PR

Use títulos descriptivos:
- `[Lesson-XX] Añadir nuevo ejemplo para <concepto>`
- `[Fix] Corregir error tipográfico en README de lesson-XX`
- `[Update] Mejorar ejemplo de código en lesson-XX`
- `[Docs] Actualizar instrucciones de configuración`

### Verificaciones Requeridas

- Los notebooks deben ejecutarse sin errores
- Los archivos README deben ser claros y precisos
- Seguir patrones de código existentes en el repositorio
- Mantener consistencia con otras lecciones

## Notas Adicionales

### Errores Comunes

1. **Incompatibilidad de versión de Python:**
   - Asegurarse de usar Python 3.12+
   - Algunos paquetes no funcionan con versiones anteriores
   - Usar `python3 -m venv` para especificar versión explícitamente

2. **Variables de entorno:**
   - Siempre crear `.env` a partir de `.env.example`
   - No subir archivo `.env` (está en `.gitignore`)
   - Token de GitHub requiere permisos adecuados

3. **Conflictos de paquetes:**
   - Usar un entorno virtual limpio
   - Instalar desde `requirements.txt` en vez de paquetes individuales
   - Algunos notebooks requieren paquetes adicionales mencionados en sus celdas markdown

4. **Servicios de Azure:**
   - Servicios de IA de Azure requieren suscripción activa
   - Algunas funciones son específicas para regiones
   - Limitaciones de nivel gratuito aplican a Modelos GitHub

### Ruta de Aprendizaje

Progresión recomendada a través de las lecciones:
1. **00-course-setup** - Comenzar aquí para configuración del entorno
2. **01-intro-to-ai-agents** - Entender fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño principales
5. Continuar con las lecciones numeradas secuencialmente

### Selección de Framework

Elija el framework según sus objetivos:
- **Todas las lecciones**: Microsoft Agent Framework (MAF) con `AzureAIProjectAgentProvider`
- **Agentes registrados lado servidor** en Azure AI Foundry Agent Service V2 y visibles en portal Foundry

### Obtención de Ayuda

- Unirse a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Revisar archivos README de cada lección para guía específica
- Consultar el [README.md](./README.md) principal para visión general del curso
- Referirse a [Course Setup](./00-course-setup/README.md) para instrucciones detalladas de instalación

### Contribución

Este es un proyecto educativo abierto. Se reciben contribuciones para:
- Mejorar ejemplos de código
- Corregir errores tipográficos o fallos
- Añadir comentarios aclaratorios
- Sugerir nuevos temas para lecciones
- Traducir a idiomas adicionales

Ver [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto Específico del Proyecto

### Soporte Multilenguaje

Este repositorio utiliza un sistema automático de traducción:
- Más de 50 idiomas soportados
- Traducciones en directorios `/translations/<código-idioma>/`
- Flujo de trabajo GitHub Actions gestiona actualizaciones de traducción
- Archivos fuente en inglés en la raíz del repositorio

### Estructura de la Lección

Cada lección sigue un patrón consistente:
1. Miniatura de video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y prerequisitos
5. Recursos adicionales de aprendizaje vinculados

### Nomenclatura de Ejemplos de Código

Formato: `<número-lección>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lección 1, MAF Python
- `14-sequential.ipynb` - Lección 14, patrones avanzados MAF

### Directorios Especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración del contenedor de desarrollo VS Code
- `.github/` - Workflows y plantillas de GitHub Actions

### Dependencias

Paquetes clave desde `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Soporte protocolo Agente a Agente
- `azure-ai-inference`, `azure-ai-projects` - Servicios de Azure AI
- `azure-identity` - Autenticación Azure (AzureCliCredential)
- `azure-search-documents` - Integración Azure AI Search
- `mcp[cli]` - Soporte para Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->