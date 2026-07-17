# AGENTS.md

## Resumen del Proyecto

Este repositorio contiene "Agentes de IA para Principiantes" - un curso educativo integral que enseña todo lo necesario para construir Agentes de IA. El curso consta de 18 lecciones (numeradas 00-18) que cubren fundamentos, patrones de diseño, frameworks, despliegue en producción, agentes locales/en dispositivo, y seguridad de agentes de IA.

**Tecnologías Clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Servicios de Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-15+)
- Cada lección contiene: documentación README, ejemplos de código (notebooks Jupyter) e imágenes
- Soporte multilingüe mediante sistema de traducción automatizada
- Un notebook Python por lección usando Microsoft Agent Framework

## Comandos de Configuración

### Prerrequisitos
- Python 3.12 o superior
- Suscripción de Azure (para Microsoft Foundry)
- Azure CLI instalado y autenticado (`az login`)

### Configuración Inicial

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
   # Edita .env con tus claves API y puntos finales
   ```

### Variables de Entorno Requeridas

Para **Microsoft Foundry** (Requerido):
- `AZURE_AI_PROJECT_ENDPOINT` - Punto de enlace del proyecto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nombre del despliegue del modelo (ej., gpt-4.1-mini)

Para **Azure AI Search** (Lección 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Punto de enlace de Azure AI Search
- `AZURE_SEARCH_API_KEY` - Clave API de Azure AI Search

Autenticación: Ejecuta `az login` antes de correr los notebooks (usa `AzureCliCredential`).

## Flujo de Trabajo de Desarrollo

### Ejecutando Jupyter Notebooks

Cada lección contiene múltiples notebooks Jupyter para diferentes frameworks:

1. **Inicia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navega al directorio de una lección** (ej., `01-intro-to-ai-agents/code_samples/`)

3. **Abre y ejecuta los notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabajando con Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requiere suscripción de Azure
- Usa `FoundryChatClient` para Agent Service V2 (agentes visibles en el portal Foundry)
- Listo para producción con capacidad de observabilidad integrada
- Patrón de archivo: `*-python-agent-framework.ipynb`

## Instrucciones para Pruebas

Este es un repositorio educativo con código de ejemplo en lugar de código de producción con pruebas automatizadas. Para verificar tu configuración y cambios:

### Pruebas Manuales

1. **Prueba el entorno Python:**
   ```bash
   python --version  # Debe ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Prueba la ejecución del notebook:**
   ```bash
   # Convertir el cuaderno a script y ejecutar (pruebas de importaciones)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica las variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Ejecutando Notebooks Individuales

Abre notebooks en Jupyter y ejecuta las celdas secuencialmente. Cada notebook es auto contenido e incluye:
- Sentencias de importación
- Carga de configuración
- Implementaciones de agentes de ejemplo
- Salidas esperadas en celdas markdown

### Pruebas iniciales de Agentes Desplegados

Para lecciones donde un agente está desplegado como agente hospedado en Microsoft Foundry (01, 04, 05, 16), el repositorio incluye catálogos de prueba inicial bajo `tests/` que son ejecutados por el flujo de trabajo `.github/workflows/smoke-test.yml` vía la acción [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estas son una puerta ligera post-despliegue (¿el agente es accesible y cumple con las expectativas básicas del prompt?), complementando la canalización de evaluación en las Lecciones 10 y 16. Consulta [tests/README.md](./tests/README.md) para el mapeo catálogo-lección-agente. La Lección 17 corre localmente con Foundry Local y no tiene punto final hospedado, por lo que se valida ejecutando directamente su notebook.

## Estilo de Código

### Convenciones de Python

- **Versión de Python**: 3.12+
- **Estilo de Código**: Sigue las convenciones estándar de Python PEP 8
- **Notebooks**: Usa celdas markdown claras para explicar conceptos
- **Imports**: Agrupa por biblioteca estándar, terceros, locales

### Convenciones para Jupyter Notebook

- Incluye celdas markdown descriptivas antes de las celdas de código
- Añade ejemplos de salida en los notebooks como referencia
- Usa nombres de variables claros que coincidan con los conceptos de la lección
- Mantén el orden lineal de ejecución (celda 1 → 2 → 3...)

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

## Compilación y Despliegue

### Construcción de Documentación

Este repositorio usa Markdown para documentación:
- Archivos README.md en cada carpeta de lección
- README.md principal en la raíz del repositorio
- Sistema de traducción automatizada mediante GitHub Actions

### Pipeline CI/CD

Ubicado en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a creadores de issues nuevos
3. **welcome-pr.yml** - Da la bienvenida a contribuyentes de pull requests nuevos

### Despliegue

Este es un repositorio educativo - sin proceso de despliegue. Los usuarios:
1. Bifurcan o clonan el repositorio
2. Ejecutan notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con ejemplos

## Directrices para Pull Requests

### Antes de Enviar

1. **Prueba tus cambios:**
   - Ejecuta completamente los notebooks afectados
   - Verifica que todas las celdas se ejecuten sin errores
   - Comprueba que las salidas sean adecuadas

2. **Actualizaciones de documentación:**
   - Actualiza README.md si agregas nuevos conceptos
   - Añade comentarios en notebooks para código complejo
   - Asegura que las celdas markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evita subir archivos `.env` (usa `.env.example`)
   - No subas directorios `venv/` o `__pycache__/`
   - Mantén salidas de notebooks cuando demuestren conceptos
   - Elimina archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato del Título del PR

Usa títulos descriptivos:
- `[Lesson-XX] Añadir nuevo ejemplo para <concepto>`
- `[Fix] Corregir error tipográfico en README de lesson-XX`
- `[Update] Mejorar ejemplo de código en lesson-XX`
- `[Docs] Actualizar instrucciones de configuración`

### Revisiones Requeridas

- Los notebooks deben ejecutarse sin errores
- Los archivos README deben ser claros y precisos
- Seguir patrones de código existentes en el repositorio
- Mantener consistencia con otras lecciones

## Notas Adicionales

### Errores Comunes

1. **Incompatibilidad de versión de Python:**
   - Asegúrate de usar Python 3.12+
   - Algunos paquetes pueden no funcionar con versiones antiguas
   - Usa `python3 -m venv` para especificar explícitamente la versión de Python

2. **Variables de entorno:**
   - Siempre crea `.env` a partir de `.env.example`
   - No subas el archivo `.env` (está en `.gitignore`)
   - Inicia sesión con `az login` para autenticación Entra ID sin llave

3. **Conflictos de paquetes:**
   - Usa un entorno virtual limpio
   - Instala desde `requirements.txt` en lugar de paquetes individuales
   - Algunos notebooks pueden requerir paquetes adicionales mencionados en sus celdas markdown

4. **Servicios de Azure:**
   - Los servicios Azure AI requieren suscripción activa
   - Algunas funcionalidades son específicas por región
   - Asegura que tu despliegue del modelo Azure OpenAI soporte la API de Respuestas

### Ruta de Aprendizaje

Progresión recomendada a través de las lecciones:
1. **00-course-setup** - Comienza aquí para la configuración del entorno
2. **01-intro-to-ai-agents** - Entiende los fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Aprende sobre diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño clave
5. Continúa con las lecciones numeradas secuencialmente

### Selección de Framework

Elige el framework según tus objetivos:
- **Todas las lecciones**: Microsoft Agent Framework (MAF) con `FoundryChatClient`
- **Los agentes se registran en el servidor** en Microsoft Foundry Agent Service V2 y son visibles en el portal Foundry

### Obtener Ayuda

- Únete al [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Revisa los archivos README de las lecciones para guía específica
- Consulta el [README.md](./README.md) principal para resumen del curso
- Refiérete a [Course Setup](./00-course-setup/README.md) para instrucciones detalladas

### Contribuciones

Este es un proyecto educativo abierto. Contribuciones bienvenidas:
- Mejorar ejemplos de código
- Corregir errores tipográficos o de código
- Añadir comentarios aclaratorios
- Sugerir nuevos temas para lecciones
- Traducir a idiomas adicionales

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto Específico del Proyecto

### Soporte Multilingüe

Este repositorio usa un sistema de traducción automatizada:
- Soporta más de 50 idiomas
- Traducciones en directorios `/translations/<lang-code>/`
- El flujo de trabajo GitHub Actions maneja actualizaciones de traducción
- Los archivos fuente están en inglés en la raíz del repositorio

### Estructura de las Lecciones

Cada lección sigue un patrón consistente:
1. Miniatura de video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y prerrequisitos
5. Recursos de aprendizaje extra enlazados

### Nomenclatura de Ejemplos de Código

Formato: `<número-lección>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lección 1, MAF Python
- `14-sequential.ipynb` - Lección 14, patrones avanzados MAF
- `16-python-agent-framework.ipynb` - Lección 16, agente de soporte al cliente en producción
- `17-local-agent-foundry-local.ipynb` - Lección 17, agente local con Foundry Local + Qwen

### Directorios Especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración del contenedor de desarrollo para VS Code
- `.github/` - Flujos de trabajo y plantillas de GitHub Actions

### Dependencias

Paquetes clave de `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Soporte para protocolo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servicios Azure AI
- `azure-identity` - Autenticación Azure (AzureCliCredential)
- `azure-search-documents` - Integración Azure AI Search
- `mcp[cli]` - Soporte para Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->