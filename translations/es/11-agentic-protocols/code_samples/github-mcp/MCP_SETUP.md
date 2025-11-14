<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T14:59:27+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "es"
}
-->
# Guía de Integración del Servidor MCP

## Requisitos Previos
- Node.js instalado (versión 14 o superior)
- Gestor de paquetes npm
- Entorno de Python con las dependencias necesarias

## Pasos de Configuración

1. **Instalar el Paquete del Servidor MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Iniciar el Servidor MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   El servidor debería iniciarse y mostrar una URL de conexión.

3. **Verificar la Conexión**  
   - Busca el ícono de enchufe (🔌) en tu interfaz de Chainlit  
   - Debería aparecer un número (1) junto al ícono de enchufe, indicando una conexión exitosa  
   - La consola debería mostrar: "Configuración del plugin de GitHub completada con éxito" (junto con líneas de estado adicionales)

## Resolución de Problemas

### Problemas Comunes

1. **Conflicto de Puerto**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solución: Cambia el puerto usando:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemas de Autenticación**  
   - Asegúrate de que las credenciales de GitHub estén configuradas correctamente  
   - Verifica que el archivo .env contenga los tokens necesarios  
   - Confirma el acceso a la API de GitHub  

3. **Fallo en la Conexión**  
   - Confirma que el servidor está ejecutándose en el puerto esperado  
   - Revisa la configuración del firewall  
   - Verifica que el entorno de Python tenga los paquetes necesarios  

## Verificación de Conexión

Tu servidor MCP está correctamente conectado cuando:  
1. La consola muestra "Configuración del plugin de GitHub completada con éxito"  
2. Los registros de conexión muestran "✓ Estado de Conexión MCP: Activo"  
3. Los comandos de GitHub funcionan en la interfaz de chat  

## Variables de Entorno

Requeridas en tu archivo .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Prueba de Conexión

Envía este mensaje de prueba en el chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Una respuesta exitosa mostrará información del repositorio.  

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.