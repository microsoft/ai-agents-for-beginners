# AGENTS.md

## Resumen del Proyecto

Este repositorio contiene "Agentes de IA para Principiantes": un curso educativo completo que enseña todo lo necesario para construir Agentes de IA. El curso consta de 18 lecciones (numeradas del 00 al 18) que cubren fundamentos, patrones de diseño, frameworks, despliegue en producción, agentes locales/en dispositivo, y seguridad de agentes de IA.

**Tecnologías clave:**
- Python 3.12+
- Jupyter Notebooks para aprendizaje interactivo
- Frameworks de IA: Microsoft Agent Framework (MAF)
- Servicios de Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arquitectura:**
- Estructura basada en lecciones (directorios 00-18)
- Cada lección contiene: documentación README, ejemplos de código (Jupyter notebooks), e imágenes
- Soporte multilingüe mediante sistema de traducción automatizado
- Un notebook Python por lección usando Microsoft Agent Framework

## Comandos de Configuración

### Requisitos Previos
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

3. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   ```bash
   cp .env.example .env
   # Edita el archivo .env con tus claves API y puntos finales
   ```

### Variables de Entorno Requeridas

Para **Microsoft Foundry** (Obligatorio):
- `AZURE_AI_PROJECT_ENDPOINT` - punto final del proyecto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nombre del despliegue del modelo (ej., gpt-5-mini)

Para **Azure AI Search** (Lección 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punto final de Azure AI Search
- `AZURE_SEARCH_API_KEY` - clave API de Azure AI Search

Autenticación: Ejecuta `az login` antes de correr los notebooks (usa `AzureCliCredential`).

## Flujo de Trabajo de Desarrollo

### Ejecución de Jupyter Notebooks

Cada lección contiene múltiples notebooks Jupyter para diferentes frameworks:

1. **Inicia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navega al directorio de una lección** (ej., `01-intro-to-ai-agents/code_samples/`)

3. **Abre y ejecuta los notebooks:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Trabajo con Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requiere suscripción de Azure
- Usa `FoundryChatClient` para Agent Service V2 (agentes visibles en el portal Foundry)
- Listo para producción con observabilidad incorporada
- Patrón de archivo: `*-python-agent-framework.ipynb`

## Instrucciones de Pruebas

Este es un repositorio educativo con código de ejemplo más que código de producción con pruebas automatizadas. Para verificar tu configuración y cambios:

### Pruebas Manuales

1. **Prueba el entorno Python:**
   ```bash
   python --version  # Debe ser 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Prueba la ejecución de notebooks:**
   ```bash
   # Convertir el cuaderno a script y ejecutar (prueba las importaciones)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica las variables de entorno:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Ejecución de Notebooks Individuales

Abre los notebooks en Jupyter y ejecuta las celdas secuencialmente. Cada notebook es autónomo e incluye:
- Declaraciones de importación
- Carga de configuración
- Implementaciones ejemplo de agentes
- Salidas esperadas en celdas markdown

### Pruebas Básicas de Agentes Desplegados

Para lecciones donde un agente está desplegado como agente alojado en Microsoft Foundry (01, 04, 05, 16), el repositorio incluye catálogos de prueba rápida bajo `tests/` que son ejecutados por el flujo de trabajo `.github/workflows/smoke-test.yml` mediante la acción [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Estas son una puerta ligera post-despliegue (¿el agente es accesible y sigue expectativas básicas de prompts?), complementando la pipeline de evaluación en las Lecciones 10 y 16. Consulta [tests/README.md](./tests/README.md) para la correspondencia catálogo-lección-agente. La Lección 17 se ejecuta localmente con Foundry Local y no tiene punto final alojado, por lo que se valida ejecutando su notebook directamente.

## Estilo de Código

### Convenciones de Python

- **Versión de Python**: 3.12+
- **Estilo de Código**: Sigue las convenciones estándar PEP 8 de Python
- **Notebooks**: Usa celdas markdown claras para explicar conceptos
- **Importaciones**: Agrupa por biblioteca estándar, terceros, locales

### Convenciones para Jupyter Notebook

- Incluye celdas markdown descriptivas antes de las celdas de código
- Añade ejemplos de salida en notebooks para referencia
- Usa nombres de variables claros que correspondan con los conceptos de la lección
- Mantén el orden lineal de ejecución del notebook (celda 1 → 2 → 3...)

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

Este repositorio utiliza Markdown para la documentación:
- Archivos README.md en cada carpeta de lección
- README.md principal en la raíz del repositorio
- Sistema automatizado de traducción vía GitHub Actions

### Pipeline CI/CD

Ubicada en `.github/workflows/`:

1. **co-op-translator.yml** - Traducción automática a más de 50 idiomas
2. **welcome-issue.yml** - Da la bienvenida a creadores de nuevos issues
3. **welcome-pr.yml** - Da la bienvenida a contribuyentes de pull requests

### Despliegue

Este es un repositorio educativo - no tiene proceso de despliegue. Los usuarios:
1. Bifurcan o clonan el repositorio
2. Ejecutan notebooks localmente o en GitHub Codespaces
3. Aprenden modificando y experimentando con ejemplos

## Guía para Pull Requests

### Antes de Enviar

1. **Prueba tus cambios:**
   - Ejecuta completamente los notebooks afectados
   - Verifica que todas las celdas se ejecuten sin errores
   - Comprueba que las salidas sean adecuadas

2. **Actualizaciones de documentación:**
   - Actualiza README.md si agregas nuevos conceptos
   - Añade comentarios en notebooks para código complejo
   - Asegúrate que las celdas markdown expliquen el propósito

3. **Cambios en archivos:**
   - Evita subir archivos `.env` (usa `.env.example`)
   - No subas directorios `venv/` o `__pycache__/`
   - Conserva salidas del notebook cuando demuestren conceptos
   - Elimina archivos temporales y notebooks de respaldo (`*-backup.ipynb`)

### Formato del Título del PR

Usa títulos descriptivos:
- `[Lesson-XX] Añadir nuevo ejemplo para <concepto>`
- `[Fix] Corregir error tipográfico en README de lesson-XX`
- `[Update] Mejorar ejemplo de código en lesson-XX`
- `[Docs] Actualizar instrucciones de configuración`

### Verificaciones Requeridas

- Los notebooks deben ejecutarse sin errores
- Los archivos README deben ser claros y precisos
- Seguir los patrones de código existentes en el repositorio
- Mantener consistencia con otras lecciones

## Notas Adicionales

### Errores Comunes

1. **Incompatibilidad de versión de Python:**
   - Asegúrate de usar Python 3.12+
   - Algunos paquetes pueden no funcionar con versiones anteriores
   - Usa `python3 -m venv` para especificar la versión de Python explícitamente

2. **Variables de entorno:**
   - Siempre crea `.env` a partir de `.env.example`
   - No subas el archivo `.env` (está en `.gitignore`)
   - Inicia sesión con `az login` para autenticación Entra ID sin claves

3. **Conflictos de paquetes:**
   - Usa un entorno virtual limpio
   - Instala desde `requirements.txt` en lugar de paquetes individuales
   - Algunos notebooks pueden requerir paquetes adicionales mencionados en sus celdas markdown

4. **Servicios de Azure:**
   - Los servicios Azure AI requieren suscripción activa
   - Algunas funciones son específicas por región
   - Asegúrate que el despliegue de tu modelo Azure OpenAI soporta la API de Respuestas

### Ruta de Aprendizaje

Progresión recomendada por lecciones:
1. **00-course-setup** - Comienza aquí para configuración del entorno
2. **01-intro-to-ai-agents** - Comprende fundamentos de agentes IA
3. **02-explore-agentic-frameworks** - Aprende acerca de diferentes frameworks
4. **03-agentic-design-patterns** - Patrones de diseño principales
5. Continua a través de las lecciones numeradas secuencialmente

### Selección de Framework

Elige el framework basado en tus objetivos:
- **Todas las lecciones**: Microsoft Agent Framework (MAF) con `FoundryChatClient`
- **Los agentes se registran del lado servidor** en Microsoft Foundry Agent Service V2 y son visibles en el portal Foundry

### Obtener Ayuda

- Únete a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Revisa los archivos README de las lecciones para guía específica
- Consulta el [README.md](./README.md) principal para resumen del curso
- Referencia a [Course Setup](./00-course-setup/README.md) para instrucciones detalladas de configuración

### Contribuciones

Este es un proyecto educativo abierto. Se aceptan contribuciones:
- Mejorar ejemplos de código
- Corregir errores tipográficos o fallos
- Añadir comentarios aclaratorios
- Sugerir nuevos temas para lecciones
- Traducir a otros idiomas

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para necesidades actuales.

## Contexto Específico del Proyecto

### Soporte Multilingüe

Este repositorio usa un sistema de traducción automatizado:
- Soporte para más de 50 idiomas
- Traducciones en directorios `/translations/<lang-code>/`
- Flujo de trabajo GitHub Actions maneja actualizaciones de traducción
- Archivos fuente están en inglés en la raíz del repositorio

### Estructura de las Lecciones

Cada lección sigue un patrón consistente:
1. Miniatura de video con enlace
2. Contenido escrito de la lección (README.md)
3. Ejemplos de código en múltiples frameworks
4. Objetivos de aprendizaje y prerrequisitos
5. Recursos adicionales de aprendizaje enlazados

### Nomenclatura de Muestras de Código

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lección 1, MAF Python
- `14-sequential.ipynb` - Lección 14, patrones avanzados MAF
- `16-python-agent-framework.ipynb` - Lección 16, agente de soporte al cliente en producción
- `17-local-agent-foundry-local.ipynb` - Lección 17, agente local con Foundry Local + Qwen

### Directorios Especiales

- `translated_images/` - Imágenes localizadas para traducciones
- `images/` - Imágenes originales para contenido en inglés
- `.devcontainer/` - Configuración de contenedor de desarrollo para VS Code
- `.github/` - Flujos de trabajo y plantillas de GitHub Actions

### Dependencias

Paquetes clave desde `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Soporte de protocolo Agente a Agente
- `azure-ai-inference`, `azure-ai-projects` - Servicios Azure AI
- `azure-identity` - Autenticación de Azure (AzureCliCredential)
- `azure-search-documents` - Integración Azure AI Search
- `mcp[cli]` - Soporte Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->