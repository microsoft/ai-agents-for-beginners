# 📘 Guía Completa de Instalación y Uso
## Smart Money Concepts EA v2.0

---

## 📋 **TABLA DE CONTENIDOS**

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Configuración Inicial](#configuración-inicial)
4. [Configuraciones Recomendadas](#configuraciones-recomendadas)
5. [Interpretación del Panel](#interpretación-del-panel)
6. [Solución de Problemas](#solución-de-problemas)
7. [FAQ](#faq)
8. [Mejores Prácticas](#mejores-prácticas)

---

## 🔧 **REQUISITOS**

### Software:
- ✅ **MetaTrader 5** (build 3440 o superior)
- ✅ **Windows 10/11** o **Linux con Wine**
- ✅ **RAM:** Mínimo 4GB (recomendado 8GB)

### Cuenta de Trading:
- ✅ Broker con soporte MT5
- ✅ Cuenta Demo (para pruebas)
- ✅ Cuenta Real con mínimo $500 (recomendado $1000+)
- ✅ Ejecución Market Execution o Instant Execution

### Símbolos Compatibles:
- ✅ Forex (EURUSD, GBPUSD, USDJPY, etc.)
- ✅ Índices (US30, NAS100, SPX500)
- ✅ Metales (XAUUSD, XAGUSD)
- ✅ Cripto (BTCUSD si tu broker lo ofrece)

### Timeframes Recomendados:
- 🕐 **M15** - Para scalping agresivo
- 🕑 **H1** - Balance entre oportunidades y calidad
- 🕓 **H4** - Swing trading (recomendado para principiantes)
- 🕔 **D1** - Position trading

---

## 📥 **INSTALACIÓN**

### **Método 1: Instalación Manual (Recomendado)**

#### Paso 1: Abrir la carpeta de datos de MT5
1. Abre MetaTrader 5
2. Ve a **Archivo → Abrir carpeta de datos**
3. Se abrirá el explorador de archivos

#### Paso 2: Copiar el archivo
1. Navega a: `MQL5 → Experts`
2. Copia el archivo `SmartMoneyConcepts_EA_v2_FIXED.mq5` aquí
3. Cierra y vuelve a abrir MT5

#### Paso 3: Compilar (si es necesario)
1. Presiona **F4** para abrir MetaEditor
2. Abre el archivo en la carpeta Experts
3. Presiona **F7** para compilar
4. Verifica que no haya errores (0 error(s), 0 warning(s))

#### Paso 4: Verificar instalación
1. En MT5, ve a **Ver → Navegador**
2. Expande **Expert Advisors**
3. Deberías ver "SmartMoneyConcepts_EA_LuxAlgo"

---

### **Método 2: Drag & Drop**

1. Descarga el archivo `.mq5`
2. Arrastra el archivo directamente a cualquier gráfico en MT5
3. MT5 lo copiará automáticamente a la carpeta correcta
4. Compila siguiendo Paso 3 del Método 1

---

## ⚙️ **CONFIGURACIÓN INICIAL**

### **Primera vez - Configuración de Prueba**

#### 1. Preparar gráfico:
```
✅ Símbolo: EURUSD
✅ Timeframe: H1
✅ Cuenta: DEMO
```

#### 2. Arrastrar EA al gráfico:
- Desde el Navegador, arrastra el EA al gráfico
- Aparecerá la ventana de configuración

#### 3. Configuración Básica Segura:

```
========== Configuración General ==========
Tipo de Entrada: ENTRY_COMBINED
Operar solo con la tendencia: true
Magic Number: 123456

========== Gestión de Riesgo ==========
Tipo de Riesgo: RISK_PERCENT
Riesgo por Operación: 0.5%  ← EMPEZAR BAJO
Tipo de Stop Loss: SL_STRUCTURE
Tipo de Take Profit: TP_RISK_REWARD
Risk:Reward Ratio: 2.0

========== Trailing Stop ==========
Usar Trailing Stop: true
Iniciar Trailing en R:R: 1.0
Usar Breakeven: true
Activar Breakeven en R:R: 0.8

========== Filtros de Trading ==========
Usar Filtro de Tiempo: true
Hora de Inicio: 8  ← Apertura Londres
Hora de Fin: 17    ← Cierre NY
Operar Lunes-Viernes: true
Spread Máximo: 20  ← Ajustar según tu broker

========== Panel de Información ==========
Mostrar Panel: true

========== Debugging ==========
Modo Debug: true  ← Para aprendizaje
Dibujar Estructura: true
```

#### 4. Permitir Trading Automatizado:
- ✅ Marca "Permitir trading algorítmico"
- ✅ Marca "Permitir importaciones DLL" (NO necesario para este EA)
- Click en **OK**

#### 5. Verificar activación:
- Verás un emoji 😊 en la esquina superior derecha del gráfico
- El panel de información aparecerá en pantalla

---

## 🎯 **CONFIGURACIONES RECOMENDADAS**

### **Para Principiantes (Conservador)**
```
Risk Type: RISK_PERCENT
Risk Percent: 0.5-1.0%
Entry Type: ENTRY_COMBINED
Trade Only Trend: true
SL Type: SL_STRUCTURE
TP Type: TP_RISK_REWARD
Risk Reward: 2.0
Use Trailing: true
Use Breakeven: true
Max Spread: 20 puntos
```
**Expectativa:** 3-5 trades/semana, Win Rate 55-60%

---

### **Para Traders Intermedios (Moderado)**
```
Risk Type: RISK_PERCENT
Risk Percent: 1.0-2.0%
Entry Type: ENTRY_OB
Trade Only Trend: true
Confirm With OB: true
Confirm With FVG: false
SL Type: SL_ATR
SL ATR Multiplier: 2.0
TP Type: TP_RISK_REWARD
Risk Reward: 2.5-3.0
Use Trailing: true
Trailing Start: 1.2
Use Breakeven: true
Breakeven At: 1.0
Max Spread: 25 puntos
```
**Expectativa:** 5-8 trades/semana, Win Rate 50-55%

---

### **Para Traders Avanzados (Agresivo)**
```
Risk Type: RISK_PERCENT
Risk Percent: 2.0-3.0%
Entry Type: ENTRY_COMBINED
Trade Only Trend: false  ← Opera reversiones
Confirm With OB: true
Confirm With FVG: true
SL Type: SL_ATR
SL ATR Multiplier: 1.5
TP Type: TP_RISK_REWARD
Risk Reward: 3.0-4.0
Use Trailing: true
Trailing Start: 1.0
Trailing Step: 0.3
Use Breakeven: true
Breakeven At: 0.8
Time Filter: true  ← Solo sesiones principales
Max Spread: 30 puntos
```
**Expectativa:** 8-12 trades/semana, Win Rate 45-50%

---

### **Configuración para Scalping (M15)**
```
Risk Percent: 0.5%  ← Bajo por operación
Entry Type: ENTRY_OB
Internal Length: 3  ← Estructura más sensible
SL Type: SL_FIXED_POINTS
SL Points: 150
TP Type: TP_FIXED_POINTS
TP Points: 300  ← R:R 1:2
Use Trailing: true
Trailing Start: 0.8
Trailing Step: 0.2
Max Spread: 10  ← MUY IMPORTANTE para scalping
Time Filter: true
Start Hour: 8
End Hour: 11  ← Solo apertura Londres
```
**Expectativa:** 15-25 trades/semana, Win Rate 50-55%

---

### **Configuración para Swing Trading (H4/D1)**
```
Risk Percent: 1.5-2.0%
Entry Type: ENTRY_COMBINED
Swing Length: 100  ← Estructura más amplia
Trade Only Trend: true
SL Type: SL_STRUCTURE
TP Type: TP_RISK_REWARD
Risk Reward: 3.0-5.0  ← Mayor R:R
Use Trailing: true
Trailing Start: 2.0
Use Breakeven: true
Breakeven At: 1.5
Time Filter: false  ← Sin filtro de tiempo
Max Spread: 50
```
**Expectativa:** 2-4 trades/semana, Win Rate 40-45%

---

### **Configuración para VPS (Mínimos recursos)**
```
Show Panel: false  ← Ahorra memoria
Draw Structure: false  ← No dibujar gráficos
Debug Mode: false  ← Menos logging
Max Order Blocks: 30  ← Límite bajo
Max FVGs: 30
Use Order Blocks: true
Use FVG: true
OB Validity Bars: 50
FVG Validity Bars: 30
```

---

## 📊 **INTERPRETACIÓN DEL PANEL**

### Panel de Información Explicado:

```
┌─────────────────────────────────────┐
│ 💎 Smart Money EA v2.0              │
│ ─────────────────────────────       │
│ Trend: BULLISH 🟢                   │  ← Tendencia actual
│ Positions: 1                        │  ← Operaciones abiertas
│ Total Trades: 15                    │  ← Trades ejecutados
│ Win Rate: 60.0%                     │  ← % de ganadores
│ Profit: +$125.50                    │  ← Beneficio/Pérdida
│ Signal: IN TRADE                    │  ← Estado actual
│ 14:35:42                           │  ← Hora del servidor
│ ✅ EA Active                        │  ← Estado del EA
└─────────────────────────────────────┘
```

### **Significado de los estados:**

#### Trend (Tendencia):
- 🟢 **BULLISH** - Tendencia alcista confirmada
- 🔴 **BEARISH** - Tendencia bajista confirmada
- ⚪ **RANGING** - Sin tendencia clara

#### Signal (Señal):
- 🟢 **BUY** - Señal de compra activa
- 🔴 **SELL** - Señal de venta activa
- 🔵 **IN TRADE** - Operación en curso
- ⚪ **WAITING** - Esperando condiciones

#### Win Rate (Tasa de Éxito):
- 🟢 **Verde (≥60%)** - Excelente
- 🟡 **Amarillo (40-59%)** - Aceptable
- 🟠 **Naranja (<40%)** - Revisar configuración

---

## 🔍 **ELEMENTOS GRÁFICOS**

### **Order Blocks:**
- 🔵 **Azul** - Order Block Alcista (zona de compra)
- 🔴 **Rojo** - Order Block Bajista (zona de venta)

### **Fair Value Gaps (FVG):**
- 🟢 **Verde** - FVG Alcista (gap alcista)
- 🟠 **Naranja** - FVG Bajista (gap bajista)

### **Etiquetas de Estructura:**
- **BOS ↑** - Break of Structure alcista
- **BOS ↓** - Break of Structure bajista
- **CHoCH ↑** - Change of Character alcista
- **CHoCH ↓** - Change of Character bajista

---

## 🐛 **SOLUCIÓN DE PROBLEMAS**

### **Problema 1: EA no abre operaciones**

#### Posibles causas y soluciones:

**A. Trading algorítmico no permitido**
```
Solución:
1. Click derecho en el gráfico
2. Expert Advisors → Propiedades
3. ✅ Permitir trading algorítmico
4. ✅ Permitir trading (en Herramientas → Opciones → Expert Advisors)
```

**B. Filtros muy restrictivos**
```
Revisa:
- Max Spread (aumentar a 30-50)
- Min ATR Filter (poner en 0 para probar)
- Time Filter (desactivar temporalmente)
- Trade Only Trend (poner en false para probar)
```

**C. No hay señales válidas**
```
Activa Debug Mode:
1. InpDebugMode = true
2. Revisa pestaña "Experts" (Ctrl+T)
3. Busca mensajes como "Precio en OB Bullish"
```

---

### **Problema 2: Lote muy pequeño o "Lote calculado muy pequeño"**

#### Causas:
- SL muy amplio para el riesgo configurado
- Balance muy bajo
- Configuración de riesgo muy conservadora

#### Soluciones:
```
Opción 1 - Aumentar riesgo:
Risk Percent: 1.5-2.0%

Opción 2 - Usar lote fijo:
Risk Type: RISK_FIXED_LOT
Fixed Lot: 0.01 (mínimo del broker)

Opción 3 - Reducir SL:
SL Type: SL_FIXED_POINTS
SL Points: 300-500
```

---

### **Problema 3: Error al abrir operación (código 10004, 10006, etc.)**

#### Error 10004 - "Requote":
```
Solución:
- Aumentar Deviation: trade.SetDeviationInPoints(100)
- Cambiar a broker con mejor ejecución
```

#### Error 10006 - "Request rejected":
```
Solución:
- Verificar que el mercado esté abierto
- Revisar que el símbolo permita trading
- Contactar al broker
```

#### Error 10013 - "Invalid request":
```
Solución:
- Verificar que SL/TP estén dentro del Stop Level
- Revisar normalización de precios
- Activar Debug Mode para ver valores exactos
```

---

### **Problema 4: Trailing Stop no funciona**

#### Verificaciones:
```
1. ✅ Use Trailing = true
2. ✅ Trailing Start ≤ R:R actual de la operación
3. ✅ EA sigue activo en el gráfico (emoji 😊)
4. ✅ No hay errores en la pestaña Experts
```

#### Test:
```
1. Configura Trailing Start = 0.5
2. Abre operación manual de prueba
3. Espera que llegue a +50 puntos
4. Verifica que SL se mueva
```

---

### **Problema 5: Panel no aparece**

```
Solución:
1. InpShowPanel = true
2. Verificar posición: InpPanelX = 20, InpPanelY = 50
3. En MT5: Gráficos → Objetos → Mostrar todos
4. Si persiste, reiniciar MT5
```

---

### **Problema 6: Muchos objetos gráficos (lentitud)**

```
Solución:
1. InpDrawStructure = false
2. Max Order Blocks = 20
3. Max FVGs = 20
4. OB Validity Bars = 30
5. FVG Validity Bars = 20

Limpiar manualmente:
- Click derecho → Objetos → Eliminar todos los objetos
```

---

## ❓ **FAQ (Preguntas Frecuentes)**

### **1. ¿Cuántas operaciones abre por día?**
Depende del timeframe:
- M15: 5-10 trades/día
- H1: 2-4 trades/día
- H4: 1-2 trades/día
- D1: 2-5 trades/semana

### **2. ¿Funciona en cuentas de centavos?**
Sí, perfectamente. El EA calcula el lote basado en el balance.

### **3. ¿Puedo usar en múltiples gráficos?**
Sí, pero cambia el Magic Number en cada uno:
- EURUSD: 123456
- GBPUSD: 123457
- XAUUSD: 123458

### **4. ¿Es mejor usar en cuenta real o demo?**
**SIEMPRE** probar en DEMO primero:
- Mínimo 1 mes de pruebas
- Al menos 50 trades ejecutados
- Win Rate consistente
- Drawdown aceptable

### **5. ¿Qué broker recomiendas?**
Características importantes:
- ✅ Spreads bajos (EURUSD < 1.5 pips)
- ✅ Ejecución rápida (< 100ms)
- ✅ Sin requotes
- ✅ Regulado (FCA, ASIC, CySEC)
- ✅ Soporte MT5

### **6. ¿El EA hace martingala?**
No, el EA NO usa martingala. Cada operación es independiente con el mismo riesgo.

### **7. ¿Puedo modificar el código?**
Sí, el código es abierto. Si haces mejoras, ¡compártelas! 😊

### **8. ¿Funciona en modo hedge?**
El EA está diseñado para modo netting (1 posición por símbolo). Para hedge necesitarías modificaciones.

### **9. ¿Qué hacer si el drawdown es muy alto?**
1. Reducir Risk Percent a 0.5%
2. Aumentar Risk:Reward a 3:1
3. Activar Trade Only Trend
4. Aumentar filtros (spread, time, ATR)

### **10. ¿El EA cierra las operaciones solo?**
Sí, el EA gestiona:
- ✅ Stop Loss
- ✅ Take Profit
- ✅ Trailing Stop
- ✅ Breakeven

No necesitas intervención manual.

---

## 🏆 **MEJORES PRÁCTICAS**

### **1. Gestión de Riesgo:**
```
✅ Nunca arriesgar más del 2% por trade
✅ Máximo 6% de riesgo total (3 operaciones simultáneas)
✅ Mantener balance > $1000 en real
✅ Retirar beneficios regularmente
```

### **2. Optimización:**
```
✅ Hacer backtesting de 1 año mínimo
✅ Optimizar parámetros cada 3 meses
✅ Llevar diario de trades
✅ Analizar Win Rate y R:R promedio
```

### **3. Monitoreo:**
```
✅ Revisar el EA al menos 1 vez al día
✅ Verificar logs en pestaña Experts
✅ Comprobar que sigue activo (emoji 😊)
✅ Revisar conexión a internet/VPS
```

### **4. Actualización:**
```
✅ Estar atento a nuevas versiones
✅ Leer changelog antes de actualizar
✅ Probar nuevas versiones en demo
✅ Hacer backup de configuraciones
```

### **5. Diversificación:**
```
✅ No usar solo este EA
✅ Combinar con trading manual
✅ Usar en múltiples pares (max 5)
✅ No invertir todo el capital
```

---

## 📈 **PLAN DE CRECIMIENTO**

### **Mes 1-2: Aprendizaje**
```
- Cuenta demo con $10,000
- Risk 0.5%
- 1 símbolo (EURUSD)
- Debug Mode activo
- Objetivo: Entender el EA
```

### **Mes 3-4: Optimización**
```
- Cuenta demo con $10,000
- Risk 1%
- 2 símbolos (EURUSD, GBPUSD)
- Probar diferentes configuraciones
- Objetivo: Win Rate > 50%
```

### **Mes 5-6: Transición a Real**
```
- Cuenta real con $500-1000
- Risk 0.5% (conservador al inicio)
- 1-2 símbolos
- Monitoreo diario
- Objetivo: Confianza y consistencia
```

### **Mes 7+: Escalado**
```
- Aumentar capital gradualmente
- Risk 1-1.5%
- 3-4 símbolos
- Retirar 50% de beneficios
- Objetivo: Ingresos consistentes
```

---

## ⚠️ **ADVERTENCIAS IMPORTANTES**

1. **⚠️  El trading tiene riesgos** - Puedes perder todo tu capital
2. **⚠️  No es una garantía de ganancias** - Resultados pasados no garantizan futuros
3. **⚠️  Requiere educación** - Aprende sobre Smart Money Concepts
4. **⚠️  Monitoreo necesario** - No es completamente "set and forget"
5. **⚠️  Brokers diferentes = resultados diferentes** - Backtesting puede variar
6. **⚠️  Mantén expectativas realistas** - No esperes duplicar cuenta cada mes

---

## 📚 **RECURSOS ADICIONALES**

### **Aprender Smart Money Concepts:**
- ICT (Inner Circle Trader) - YouTube
- The Trading Channel - YouTube
- LuxAlgo - TradingView

### **Comunidad MT5:**
- MQL5.com - Foros oficiales
- Forex Factory - Foros de trading
- Reddit r/algotrading

### **Herramientas útiles:**
- Strategy Tester de MT5 (Ctrl+R)
- Tester visual para análisis
- MetaEditor para modificaciones

---

## 📞 **SOPORTE**

Para reportar bugs o sugerencias:
1. Activa Debug Mode
2. Copia los logs de la pestaña Experts
3. Toma screenshot del problema
4. Describe pasos para reproducir

---

**Versión de la guía:** 1.0
**Última actualización:** 2025-10-21
**Compatible con:** Smart Money Concepts EA v2.0

---

**¡Éxito en tu trading! 🚀📈**

*Recuerda: La clave del éxito es la paciencia, disciplina y gestión de riesgo adecuada.*
