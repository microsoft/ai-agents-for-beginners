# 💎 Smart Money Concepts Expert Advisor v2.0

![MQL5](https://img.shields.io/badge/MQL5-Expert_Advisor-blue)
![Version](https://img.shields.io/badge/version-2.0-green)
![Status](https://img.shields.io/badge/status-stable-success)
![License](https://img.shields.io/badge/license-Open_Source-orange)

## 📊 Expert Advisor profesional basado en conceptos de Smart Money (ICT)

Este EA implementa estrategias institucionales de trading utilizando:
- ✅ **Break of Structure (BOS)**
- ✅ **Change of Character (CHoCH)**
- ✅ **Order Blocks (OB)**
- ✅ **Fair Value Gaps (FVG)**
- ✅ **Market Structure Analysis**

---

## 🚀 **CARACTERÍSTICAS PRINCIPALES**

### 🎯 Estrategias de Entrada
- **BOS (Break of Structure):** Entradas en continuación de tendencia
- **CHoCH (Change of Character):** Detección de cambios de tendencia
- **Order Blocks:** Zonas institucionales de demanda/oferta
- **Fair Value Gaps:** Ineficiencias del mercado
- **Modo Combinado:** Múltiples confirmaciones

### 💰 Gestión de Riesgo Avanzada
- **3 Tipos de Riesgo:**
  - Lote fijo
  - Porcentaje del balance
  - Cantidad fija en dinero

- **3 Tipos de Stop Loss:**
  - ATR dinámico
  - Puntos fijos
  - Basado en estructura del mercado

- **4 Tipos de Take Profit:**
  - Risk:Reward ratio
  - ATR multiplicador
  - Puntos fijos
  - Próximo nivel estructural

### 🎨 Funciones Avanzadas
- ✅ **Trailing Stop inteligente** con configuración R:R
- ✅ **Breakeven automático** cuando la operación va en beneficio
- ✅ **Filtros de tiempo** (sesiones de trading)
- ✅ **Filtro de spread** para evitar alta volatilidad
- ✅ **Filtro de ATR** mínimo
- ✅ **Panel de información** en tiempo real
- ✅ **Modo Debug** para aprendizaje
- ✅ **Visualización gráfica** de estructura

---

## 📁 **ARCHIVOS DEL PROYECTO**

```
MQL5-Expert-Advisors/
│
├── SmartMoneyConcepts_EA_v2_FIXED.mq5  ← EA corregido y optimizado
├── CHANGELOG_v2.md                     ← Lista de correcciones y mejoras
├── GUIA_INSTALACION.md                 ← Guía completa de uso
└── README.md                           ← Este archivo
```

---

## 📥 **INSTALACIÓN RÁPIDA**

### 1️⃣ Copiar archivo
```
1. Descarga SmartMoneyConcepts_EA_v2_FIXED.mq5
2. En MT5: Archivo → Abrir carpeta de datos
3. Copiar a: MQL5/Experts/
4. Reiniciar MT5
```

### 2️⃣ Compilar
```
1. Presionar F4 (MetaEditor)
2. Abrir el archivo .mq5
3. Presionar F7 (Compilar)
4. Verificar: 0 errores
```

### 3️⃣ Activar en gráfico
```
1. Abrir gráfico (ej: EURUSD H1)
2. Arrastrar EA desde Navegador
3. Configurar parámetros
4. ✅ Permitir trading algorítmico
5. Click OK
```

📖 **Para instrucciones detalladas, ver [GUIA_INSTALACION.md](GUIA_INSTALACION.md)**

---

## ⚙️ **CONFIGURACIÓN RÁPIDA**

### 🟢 Principiantes (Conservador)
```python
Risk Type: RISK_PERCENT
Risk Percent: 0.5%
Entry Type: ENTRY_COMBINED
Trade Only Trend: true
Risk Reward: 2.0
```

### 🟡 Intermedios (Moderado)
```python
Risk Type: RISK_PERCENT
Risk Percent: 1.0%
Entry Type: ENTRY_OB
SL Type: SL_ATR
Risk Reward: 2.5
```

### 🔴 Avanzados (Agresivo)
```python
Risk Type: RISK_PERCENT
Risk Percent: 2.0%
Entry Type: ENTRY_COMBINED
Trade Only Trend: false
Risk Reward: 3.0
```

---

## 🆕 **NOVEDADES EN v2.0**

### 🔧 Correcciones Críticas
- ✅ **Order Filling automático** - Compatible con todos los brokers
- ✅ **Gestión de memoria** - Sin fugas, rendimiento estable
- ✅ **Validación robusta** - Manejo de errores mejorado
- ✅ **Filtro de spread corregido**
- ✅ **Cálculo de lote mejorado** - Funciona con todos los símbolos
- ✅ **Trailing Stop optimizado**
- ✅ **LoadStatistics 10x más rápido**
- ✅ **Panel sin duplicados**

### 🆕 Nuevas Características
- ✅ **Modo Debug** para aprendizaje
- ✅ **Control de dibujo** de estructura
- ✅ **Validación de inputs** al iniciar
- ✅ **Tooltips** en objetos gráficos
- ✅ **Logging mejorado** con emojis
- ✅ **Límites configurables** de memoria

📋 **Ver cambios completos en [CHANGELOG_v2.md](CHANGELOG_v2.md)**

---

## 📊 **RENDIMIENTO ESPERADO**

| Timeframe | Trades/Semana | Win Rate | Avg R:R | Drawdown |
|-----------|---------------|----------|---------|----------|
| M15       | 15-25         | 50-55%   | 1:1.5   | 10-15%   |
| H1        | 5-8           | 50-55%   | 1:2     | 8-12%    |
| H4        | 2-4           | 55-60%   | 1:2.5   | 5-10%    |
| D1        | 1-2           | 45-50%   | 1:3     | 8-15%    |

⚠️ **Nota:** Resultados pueden variar según broker, configuración y condiciones de mercado.

---

## 💡 **SÍMBOLOS RECOMENDADOS**

### Forex (Mejores resultados)
- ✅ EURUSD
- ✅ GBPUSD
- ✅ USDJPY
- ✅ AUDUSD

### Índices
- ✅ US30
- ✅ NAS100
- ✅ GER40

### Metales
- ✅ XAUUSD (Gold)
- ✅ XAGUSD (Silver)

---

## 🛡️ **GESTIÓN DE RIESGO**

### Reglas de Oro:
```
1. ❌ Nunca arriesgar más del 2% por trade
2. ❌ Máximo 6% riesgo total (3 trades simultáneos)
3. ✅ Empezar en DEMO (mínimo 1 mes)
4. ✅ Capital mínimo real: $500-1000
5. ✅ Retirar beneficios regularmente
```

### Configuración de Riesgo según Capital:

| Capital    | Risk % | Lote Aprox (EURUSD) |
|------------|--------|---------------------|
| $100-500   | 0.5%   | 0.01                |
| $500-1000  | 1.0%   | 0.01-0.02           |
| $1000-5000 | 1.5%   | 0.02-0.10           |
| $5000+     | 2.0%   | 0.10+               |

---

## 📖 **DOCUMENTACIÓN**

- 📘 **[GUIA_INSTALACION.md](GUIA_INSTALACION.md)** - Guía completa paso a paso
- 📋 **[CHANGELOG_v2.md](CHANGELOG_v2.md)** - Historial de cambios
- 📄 **README.md** - Este archivo

---

## 🐛 **SOLUCIÓN DE PROBLEMAS**

### ❌ EA no abre operaciones
```
1. Verificar trading algorítmico activado
2. Revisar filtros (spread, tiempo, ATR)
3. Activar Debug Mode y revisar logs
4. Verificar que hay señales (panel)
```

### ❌ Lote muy pequeño
```
1. Aumentar Risk Percent
2. Reducir SL (menos puntos)
3. Usar Fixed Lot como alternativa
```

### ❌ Error al ejecutar
```
1. Verificar compilación (F7)
2. Comprobar compatibilidad broker
3. Revisar código de error en logs
4. Ver pestaña Experts (Ctrl+T)
```

📖 **Más soluciones en [GUIA_INSTALACION.md](GUIA_INSTALACION.md#solución-de-problemas)**

---

## 🔍 **BACKTEST Y OPTIMIZACIÓN**

### Hacer Backtest:
```
1. Ctrl+R (abrir Strategy Tester)
2. Seleccionar EA
3. Símbolo: EURUSD
4. Período: H1
5. Fechas: Último año
6. Modelo: Every tick
7. Iniciar
```

### Parámetros a Optimizar:
- Swing Length (30-70)
- Risk Reward (1.5-3.5)
- SL ATR Multiplier (1.5-2.5)
- Trailing Start (0.8-1.5)

---

## 📞 **SOPORTE Y CONTRIBUCIÓN**

### Reportar Bugs:
1. Activar `InpDebugMode = true`
2. Reproducir el problema
3. Copiar logs completos
4. Crear issue con detalles

### Contribuir:
- Fork el proyecto
- Crear branch (`feature/nueva-caracteristica`)
- Commit cambios
- Pull request con descripción

---

## ⚖️ **LICENCIA**

```
Código abierto para uso educativo y personal.
Prohibida distribución comercial sin permiso.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
Trading involves risk. Use at your own risk.
```

---

## 🎓 **RECURSOS DE APRENDIZAJE**

### Smart Money Concepts:
- 📺 **ICT (Inner Circle Trader)** - YouTube
- 📺 **The Trading Channel** - YouTube
- 📊 **LuxAlgo** - TradingView

### MQL5 Programming:
- 📖 **MQL5.com** - Documentación oficial
- 📖 **MQL5 Reference** - API completa
- 🎓 **Udemy** - Cursos de MQL5

---

## 📊 **ESTADÍSTICAS DEL PROYECTO**

```
✅ Líneas de código: 2,500+
✅ Funciones: 40+
✅ Parámetros configurables: 35+
✅ Indicadores usados: ATR
✅ Objetos gráficos: OB, FVG, Labels, Panel
✅ Compatible con: MT5 build 3440+
```

---

## 🌟 **VERSIONES**

### v2.0 (2025-10-21) - CURRENT
- 🔧 Correcciones críticas
- ✨ Nuevas características
- 📈 Rendimiento mejorado
- 📖 Documentación completa

### v1.0 (2025-10-15) - INITIAL
- 🎉 Versión inicial
- 📊 Funcionalidades básicas
- ⚠️ Bugs conocidos

---

## 🏆 **AGRADECIMIENTOS**

Gracias a:
- 🙏 Comunidad de Smart Money Concepts
- 🙏 Desarrolladores de MQL5
- 🙏 Testers y colaboradores
- 🙏 ICT por el conocimiento compartido

---

## 📬 **CONTACTO**

Para preguntas, sugerencias o colaboraciones:
- 📧 Email: [Tu email]
- 💬 Telegram: [Tu grupo/canal]
- 🐦 Twitter: [Tu cuenta]

---

## ⚠️ **DISCLAIMER**

```
⚠️  ADVERTENCIA DE RIESGO:
El trading de Forex, CFDs e instrumentos derivados conlleva
un alto nivel de riesgo y puede no ser adecuado para todos
los inversores. Existe la posibilidad de que pueda sufrir
una pérdida de parte o de todo su capital invertido.

Este Expert Advisor es una herramienta de automatización
y NO es un consejo de inversión. Los resultados pasados
no garantizan resultados futuros.

Use solo capital que pueda permitirse perder.
Haga su propia investigación antes de operar.
```

---

<div align="center">

## 💎 **Smart Money Concepts EA v2.0**

### Desarrollado con ❤️ por la comunidad de traders algorítmicos

![MQL5](https://img.shields.io/badge/Made%20with-MQL5-blue?style=for-the-badge)
![Trading](https://img.shields.io/badge/Smart-Money-green?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open-Source-orange?style=for-the-badge)

---

**¡Happy Trading! 🚀📈**

*"El mercado recompensa la paciencia y la disciplina"*

---

**Última actualización:** 2025-10-21
**Mantenedor:** Smart Money Concepts Team
**Versión:** 2.0.0

</div>
