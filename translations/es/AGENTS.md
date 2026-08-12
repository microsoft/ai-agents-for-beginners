# AGENTS.md

## Resumen del Proyecto

Este repositorio contiene "Agentes de IA para Principiantes" - un curso educativo integral que enseña todo lo necesario para construir Agentes de IA. El curso consta de 18 lecciones (numeradas 00-18) que cubren fundamentos, patrones de diseño, frameworks, despliegue en producción, agentes locales/en dispositivo y seguridad de los agentes de IA.

**Tecnologías Clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Servicios de IA de Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-15+)
- Cada lección contiene: documentación README, ejemplos de código (Jupyter notebooks) e imágenes
- Soporte multilingüe mediante sistema de traducción automatizado
- Un notebook Python por lección usando Microsoft Agent Framework

## Comandos de Configuración

### Requisitos Previos
- Python 3.12 o superior
- Suscripción de Azure (para Microsoft Foundry)
- Azure CLI instalado y autenticado (`az login`)

### Configuración Inicial

1. **Clonar o bifurcar el repositorio:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crear y activar entorno virtual Python:**
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
   # Edita el archivo .env con tus claves API y puntos de enlace
   ```

### Variables de Entorno Requeridas

Para **Microsoft Foundry** (Requerido):
- `AZURE_AI_PROJECT_ENDPOINT` - punto final del proyecto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nombre de despliegue del modelo (p. ej., gpt-5-mini)

Para **Azure AI Search** (Lección 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punto final de Azure AI Search
- `AZURE_SEARCH_API_KEY` - clave API de Azure AI Search

Autenticación: Ejecutar `az login` antes de correr los notebooks (usa `AzureCliCredential`).

## Flujo de Trabajo de Desarrollo

### Ejecutar Jupyter Notebooks

Cada lección contiene múltiples notebooks Jupyter para diferentes frameworks:

1. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navegar al directorio de la lección** (p. ej., `01-intro-to-ai-agents/code_samples/`)

3. **Abrir y ejecutar notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabajando con Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requiere suscripción de Azure
- Usa `FoundryChatClient` para Agent Service V2 (agentes visibles en el portal Foundry)
- Listo para producción con observabilidad integrada
- Patrón de archivos: `*-python-agent-framework.ipynb`

## Instrucciones de Pruebas

Este es un repositorio educativo con código de ejemplo más que código de producción con pruebas automatizadas. Para verificar tu configuración y cambios:

### Pruebas Manuales

1. **Probar entorno Python:**
   ```bash
   python --version  # Debe ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Probar ejecución de notebook:**
   ```bash
   # Convertir el cuaderno a script y ejecutar (pruebas importar)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificar variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Ejecutar Notebooks Individuales

Abrir notebooks en Jupyter y ejecutar las celdas secuencialmente. Cada notebook es autónomo e incluye:
- Sentencias de importación
- Carga de configuración
- Implementaciones de agentes de ejemplo
- Resultados esperados en celdas markdown

### Prueba Rápida de Agentes Desplegados

Para lecciones donde un agente está desplegado como agente hospedado por Microsoft Foundry (01, 04, 05, 16), el repositorio incluye catálogos de prueba rápida bajo `tests/` que se ejecutan mediante el flujo de trabajo `.github/workflows/smoke-test.yml` usando la acción [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estas pruebas actúan como una puerta ligera post-despliegue (¿el agente es accesible y sigue expectativas básicas del prompt?), complementando el pipeline de evaluación en las Lecciones 10 y 16. Ver [tests/README.md](./tests/README.md) para el mapeo catálogo-a-lección-a-agente. La Lección 17 se ejecuta localmente con Foundry Local y no tiene punto final hospedado, por lo que se valida ejecutando directamente su notebook.

## Estilo de Código

### Convenciones en Python

- **Versión de Python**: 3.12+
- **Estilo de Código**: Seguir las convenciones estándar PEP 8 de Python
- **Notebooks**: Usar celdas markdown claras para explicar conceptos
- **Imports**: Agrupar por biblioteca estándar, terceros, imports locales

### Convenciones en Jupyter Notebook

- Incluir celdas markdown descriptivas antes de las celdas de código
- Añadir ejemplos de salida en los notebooks para referencia
- Usar nombres de variables claros que coincidan con conceptos de la lección
- Mantener el orden de ejecución lineal del notebook (celda 1 → 2 → 3…)

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

Este repositorio usa Markdown para la documentación:
- Archivos README.md en cada carpeta de la lección
- README.md principal en la raíz del repositorio
- Sistema de traducción automatizado mediante GitHub Actions

### Pipeline de CI/CD

Ubicado en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a creadores de nuevas issues
3. **welcome-pr.yml** - Da la bienvenida a colaboradores de pull requests

### Despliegue

Este es un repositorio educativo - no hay proceso de despliegue. Los usuarios:
1. Bifurcan o clonan el repositorio
2. Ejecutan notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con ejemplos

## Guías para Pull Requests

### Antes de Enviar

1. **Prueba tus cambios:**
   - Ejecuta completamente los notebooks afectados
   - Verifica que todas las celdas se ejecuten sin errores
   - Comprueba que las salidas sean apropiadas

2. **Actualizaciones en la documentación:**
   - Actualiza README.md si añades nuevos conceptos
   - Añade comentarios en notebooks para código complejo
   - Asegúrate de que las celdas markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evita commitear archivos `.env` (usar `.env.example`)
   - No commitear directorios `venv/` o `__pycache__/`
   - Mantén las salidas de notebooks cuando demuestren conceptos
   - Elimina archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato del Título del PR

Usa títulos descriptivos:
- `[Lección-XX] Añadir nuevo ejemplo para <concepto>`
- `[Corregir] Corregir error tipográfico en README de lección-XX`
- `[Actualizar] Mejorar ejemplo de código en lección-XX`
- `[Docs] Actualizar instrucciones de configuración`

### Revisiones Requeridas

- Los notebooks deben ejecutarse sin errores
- Los archivos README deben ser claros y precisos
- Seguir patrones de código existentes en el repositorio
- Mantener consistencia con otras lecciones

## Notas Adicionales

### Errores Comunes

1. **Desajuste de versión de Python:**
   - Asegúrate de usar Python 3.12+
   - Algunos paquetes pueden no funcionar con versiones anteriores
   - Usa `python3 -m venv` para especificar la versión de Python explícitamente

2. **Variables de entorno:**
   - Siempre crea `.env` desde `.env.example`
   - No commitees el archivo `.env` (está en `.gitignore`)
   - Inicia sesión con `az login` para autenticación Entra ID sin clave

3. **Conflictos de paquetes:**
   - Usa un entorno virtual limpio
   - Instala desde `requirements.txt` en lugar de paquetes individuales
   - Algunos notebooks pueden requerir paquetes adicionales mencionados en sus celdas markdown

4. **Servicios de Azure:**
   - Los servicios de IA de Azure requieren suscripción activa
   - Algunas funcionalidades son específicas de regiones
   - Asegúrate de que tu despliegue de modelo Azure OpenAI soporte la API de Respuestas

### Ruta de Aprendizaje

Progresión recomendada a través de las lecciones:
1. **00-course-setup** - Comienza aquí para la configuración del entorno
2. **01-intro-to-ai-agents** - Entender los fundamentos de agentes de IA
3. **02-explore-agentic-frameworks** - Aprender sobre diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño principales
5. Continuar secuencialmente con las lecciones numeradas

### Selección de Framework

Elige framework basado en tus objetivos:
- **Todas las lecciones**: Microsoft Agent Framework (MAF) con `FoundryChatClient`
- **Registro de agentes del lado servidor** en Microsoft Foundry Agent Service V2, visibles en el portal Foundry

### Obtener Ayuda

- Únete a la [Comunidad Discord de Microsoft Foundry](https://aka.ms/ai-agents/discord)
- Revisa los archivos README de las lecciones para guías específicas
- Consulta el [README.md](./README.md) principal para resumen del curso
- Refiérete a [Configuración del Curso](./00-course-setup/README.md) para instrucciones detalladas

### Contribuciones

Este es un proyecto educativo abierto. Se aceptan contribuciones:
- Mejorar ejemplos de código
- Corregir errores tipográficos o de código
- Añadir comentarios aclaratorios
- Sugerir nuevos temas para lecciones
- Traducir a idiomas adicionales

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto Específico del Proyecto

### Soporte Multilingüe

Este repositorio usa un sistema automatizado de traducción:
- Soporta más de 50 idiomas
- Traducciones en directorios `/translations/<lang-code>/`
- Flujo de trabajo GitHub Actions maneja actualizaciones de traducción
- Archivos fuente están en inglés en la raíz del repositorio

### Estructura de la Lección

Cada lección sigue un patrón consistente:
1. Miniatura del video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y prerrequisitos
5. Recursos de aprendizaje adicionales vinculados

### Nombrado de Ejemplos de Código

Formato: `<numero-leccion>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lección 1, MAF Python
- `14-sequential.ipynb` - Lección 14, patrones avanzados de MAF
- `16-python-agent-framework.ipynb` - Lección 16, agente de soporte al cliente en producción
- `17-local-agent-foundry-local.ipynb` - Lección 17, agente local con Foundry Local + Qwen

### Directorios Especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración del contenedor de desarrollo en VS Code
- `.github/` - Flujos de trabajo y plantillas de GitHub Actions

### Dependencias

Paquetes clave de `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Soporte para protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - servicios de IA de Azure
- `azure-identity` - autenticación de Azure (AzureCliCredential)
- `azure-search-documents` - integración Azure AI Search
- `mcp[cli]` - soporte para Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->