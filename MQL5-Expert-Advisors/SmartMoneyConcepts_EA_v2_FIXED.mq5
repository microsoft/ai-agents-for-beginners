//+------------------------------------------------------------------+
//|                                  SmartMoneyConcepts_EA_LuxAlgo.mq5 |
//|                                       Expert Advisor Completo v2.0 |
//|                                           VERSIÓN CORREGIDA Y MEJORADA |
//+------------------------------------------------------------------+
#property copyright "Smart Money Concepts EA v2.0"
#property link      ""
#property version   "2.00"
#property description "Expert Advisor basado en conceptos de Smart Money - Versión Corregida"
#property description "Mejoras: Order Filling automático, gestión de memoria, validaciones robustas"

#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>
#include <Trade\OrderInfo.mqh>

CTrade trade;
CPositionInfo positionInfo;
COrderInfo orderInfo;

//--- Enumeraciones
enum ENUM_ENTRY_TYPE
{
   ENTRY_BOS,           // BOS (Break of Structure)
   ENTRY_CHOCH,         // CHoCH (Change of Character)
   ENTRY_OB,            // Order Block
   ENTRY_FVG,           // Fair Value Gap
   ENTRY_COMBINED       // Combinado (múltiples señales)
};

enum ENUM_RISK_TYPE
{
   RISK_FIXED_LOT,      // Lote fijo
   RISK_PERCENT,        // Porcentaje del balance
   RISK_FIXED_MONEY     // Dinero fijo
};

enum ENUM_SL_TYPE
{
   SL_ATR,              // ATR
   SL_FIXED_POINTS,     // Puntos fijos
   SL_STRUCTURE         // Basado en estructura (último swing)
};

enum ENUM_TP_TYPE
{
   TP_RISK_REWARD,      // Risk:Reward ratio
   TP_ATR,              // ATR multiplicador
   TP_FIXED_POINTS,     // Puntos fijos
   TP_STRUCTURE         // Próximo nivel de estructura
};

//--- Inputs Generales
input group "========== Configuración General =========="
input ENUM_ENTRY_TYPE InpEntryType = ENTRY_COMBINED;          // Tipo de Entrada
input bool InpTradeOnlyTrend = true;                          // Operar solo con la tendencia
input bool InpUseInternalStructure = true;                    // Usar Estructura Interna
input int InpMagicNumber = 123456;                            // Magic Number
input string InpTradeComment = "SMC_EA_v2";                   // Comentario de Operaciones

//--- Inputs de Gestión de Riesgo
input group "========== Gestión de Riesgo =========="
input ENUM_RISK_TYPE InpRiskType = RISK_PERCENT;              // Tipo de Riesgo
input double InpRiskPercent = 1.0;                            // Riesgo por Operación (%)
input double InpFixedLot = 0.1;                               // Lote Fijo
input double InpFixedMoney = 100;                             // Dinero Fijo ($)
input ENUM_SL_TYPE InpSLType = SL_STRUCTURE;                  // Tipo de Stop Loss
input double InpSLPoints = 500;                               // Stop Loss en Puntos
input double InpSLATRMultiplier = 2.0;                        // Multiplicador ATR para SL
input ENUM_TP_TYPE InpTPType = TP_RISK_REWARD;                // Tipo de Take Profit
input double InpRiskReward = 2.0;                             // Risk:Reward Ratio
input double InpTPPoints = 1000;                              // Take Profit en Puntos
input double InpTPATRMultiplier = 3.0;                        // Multiplicador ATR para TP

//--- Inputs de Trailing Stop
input group "========== Trailing Stop =========="
input bool InpUseTrailing = true;                             // Usar Trailing Stop
input double InpTrailingStart = 1.0;                          // Iniciar Trailing en R:R
input double InpTrailingStep = 0.5;                           // Paso del Trailing (R:R)
input bool InpUseBreakeven = true;                            // Usar Breakeven
input double InpBreakevenAt = 0.8;                            // Activar Breakeven en R:R
input double InpBreakevenPlus = 0.2;                          // Puntos adicionales en BE (R:R)

//--- Inputs de Estructura
input group "========== Parámetros de Estructura =========="
input int InpSwingLength = 50;                                // Longitud de Swing
input int InpInternalLength = 5;                              // Longitud Estructura Interna
input bool InpConfirmWithOB = true;                           // Confirmar con Order Block
input bool InpConfirmWithFVG = false;                         // Confirmar con FVG

//--- Inputs de Filtros
input group "========== Filtros de Trading =========="
input bool InpUseTimeFilter = true;                           // Usar Filtro de Tiempo
input int InpStartHour = 0;                                   // Hora de Inicio
input int InpEndHour = 23;                                    // Hora de Fin
input bool InpTradeMonday = true;                             // Operar Lunes
input bool InpTradeTuesday = true;                            // Operar Martes
input bool InpTradeWednesday = true;                          // Operar Miércoles
input bool InpTradeThursday = true;                           // Operar Jueves
input bool InpTradeFriday = true;                             // Operar Viernes
input double InpMinATRFilter = 0;                             // ATR Mínimo para operar
input int InpMaxSpreadPoints = 50;                            // Spread Máximo (puntos)

//--- Inputs de Order Blocks
input group "========== Order Blocks =========="
input bool InpUseOrderBlocks = true;                          // Usar Order Blocks
input int InpOBValidityBars = 100;                            // Validez del OB (barras)
input int InpMaxOrderBlocks = 50;                             // Máximo de OBs en memoria

//--- Inputs de Fair Value Gaps
input group "========== Fair Value Gaps =========="
input bool InpUseFVG = true;                                  // Usar Fair Value Gaps
input bool InpFVGAutoThreshold = true;                        // Threshold Automático
input int InpFVGValidityBars = 50;                            // Validez del FVG (barras)
input int InpMaxFVGs = 50;                                    // Máximo de FVGs en memoria

//--- Inputs de Panel
input group "========== Panel de Información =========="
input bool InpShowPanel = true;                               // Mostrar Panel
input int InpPanelX = 20;                                     // Posición X
input int InpPanelY = 50;                                     // Posición Y
input color InpPanelColor = clrDarkSlateGray;                 // Color del Panel

//--- Inputs de Debugging
input group "========== Debugging =========="
input bool InpDebugMode = false;                              // Modo Debug (más logs)
input bool InpDrawStructure = true;                           // Dibujar Estructura en Gráfico

//--- Variables Globales
struct SwingPoint
{
   double price;
   datetime time;
   int bar_index;
   bool is_high;
};

struct OrderBlock
{
   double top;
   double bottom;
   datetime time;
   int type;           // 1 = bullish, -1 = bearish
   int bars_ago;
   bool valid;
};

struct FairValueGap
{
   double top;
   double bottom;
   datetime time;
   int type;           // 1 = bullish, -1 = bearish
   int bars_ago;
   bool filled;
};

// Variables de Estructura
int g_trend = 0;              // 1 = bullish, -1 = bearish
int g_internal_trend = 0;
double g_last_high = 0;
double g_last_low = DBL_MAX;
datetime g_last_high_time = 0;
datetime g_last_low_time = 0;
SwingPoint g_swing_high, g_swing_low;
SwingPoint g_internal_high, g_internal_low;

// Arrays
OrderBlock g_order_blocks[];
FairValueGap g_fvgs[];

// Variables de Trading
bool g_buy_signal = false;
bool g_sell_signal = false;
double g_entry_price = 0;
double g_sl_price = 0;
double g_tp_price = 0;

// Handles de Indicadores
int g_atr_handle = INVALID_HANDLE;

// Variables de Control
datetime g_last_bar_time = 0;
bool g_new_bar = false;

// Estadísticas
int g_total_trades = 0;
int g_winning_trades = 0;
int g_losing_trades = 0;
double g_total_profit = 0;

// Variables de configuración
ENUM_ORDER_TYPE_FILLING g_filling_mode;

//+------------------------------------------------------------------+
//| Obtener modo de llenado de órdenes compatible                    |
//+------------------------------------------------------------------+
ENUM_ORDER_TYPE_FILLING GetFillingMode(string symbol)
{
   int filling = (int)SymbolInfoInteger(symbol, SYMBOL_FILLING_MODE);

   // Verificar modos soportados en orden de preferencia
   if((filling & SYMBOL_FILLING_FOK) == SYMBOL_FILLING_FOK)
   {
      if(InpDebugMode)
         Print("✅ Modo de llenado: FOK (Fill or Kill)");
      return ORDER_FILLING_FOK;
   }
   else if((filling & SYMBOL_FILLING_IOC) == SYMBOL_FILLING_IOC)
   {
      if(InpDebugMode)
         Print("✅ Modo de llenado: IOC (Immediate or Cancel)");
      return ORDER_FILLING_IOC;
   }

   if(InpDebugMode)
      Print("✅ Modo de llenado: RETURN (Return order)");
   return ORDER_FILLING_RETURN;
}

//+------------------------------------------------------------------+
//| Validar parámetros de entrada                                    |
//+------------------------------------------------------------------+
bool ValidateInputs()
{
   bool valid = true;

   if(InpRiskPercent <= 0 || InpRiskPercent > 100)
   {
      Print("❌ Error: Riesgo debe estar entre 0 y 100%");
      valid = false;
   }

   if(InpFixedLot <= 0)
   {
      Print("❌ Error: Lote fijo debe ser mayor que 0");
      valid = false;
   }

   if(InpRiskReward <= 0)
   {
      Print("❌ Error: Risk:Reward debe ser mayor que 0");
      valid = false;
   }

   if(InpSwingLength <= 0)
   {
      Print("❌ Error: Longitud de Swing debe ser mayor que 0");
      valid = false;
   }

   if(InpMaxOrderBlocks <= 0)
   {
      Print("⚠️  Advertencia: MaxOrderBlocks ajustado a 50");
      //InpMaxOrderBlocks = 50; // No se puede modificar input
   }

   if(InpMaxFVGs <= 0)
   {
      Print("⚠️  Advertencia: MaxFVGs ajustado a 50");
      //InpMaxFVGs = 50;
   }

   return valid;
}

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
{
   Print("========================================");
   Print("🚀 Inicializando Smart Money Concepts EA v2.0");
   Print("========================================");

   // Validar inputs
   if(!ValidateInputs())
   {
      Print("❌ Validación de parámetros falló");
      return INIT_PARAMETERS_INCORRECT;
   }

   // Obtener modo de llenado compatible
   g_filling_mode = GetFillingMode(_Symbol);

   // Configurar Trade
   trade.SetExpertMagicNumber(InpMagicNumber);
   trade.SetDeviationInPoints(50);
   trade.SetTypeFilling(g_filling_mode);
   trade.SetAsyncMode(false);

   // Inicializar ATR
   g_atr_handle = iATR(_Symbol, _Period, 14);
   if(g_atr_handle == INVALID_HANDLE)
   {
      Print("❌ Error al crear indicador ATR: ", GetLastError());
      return INIT_FAILED;
   }

   // Esperar a que el indicador esté listo
   if(CopyBuffer(g_atr_handle, 0, 0, 1, g_atr_buffer_test) <= 0)
   {
      Print("⚠️  Esperando datos del ATR...");
      Sleep(1000);
   }

   // Inicializar arrays con capacidad
   ArrayResize(g_order_blocks, 0, InpMaxOrderBlocks);
   ArrayResize(g_fvgs, 0, InpMaxFVGs);

   // Inicializar valores
   g_last_high = 0;
   g_last_low = DBL_MAX;
   g_swing_high.price = 0;
   g_swing_low.price = DBL_MAX;
   g_internal_high.price = 0;
   g_internal_low.price = DBL_MAX;

   // Cargar estadísticas
   LoadStatistics();

   // Crear panel
   if(InpShowPanel)
      CreatePanel();

   Print("========================================");
   Print("✅ Smart Money Concepts EA Inicializado");
   Print("Símbolo: ", _Symbol);
   Print("Timeframe: ", EnumToString(_Period));
   Print("Magic Number: ", InpMagicNumber);
   Print("Modo Llenado: ", EnumToString(g_filling_mode));
   Print("========================================");

   return INIT_SUCCEEDED;
}

// Variable temporal para test de ATR
double g_atr_buffer_test[];

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   // Liberar indicadores
   if(g_atr_handle != INVALID_HANDLE)
      IndicatorRelease(g_atr_handle);

   // Eliminar objetos gráficos
   ObjectsDeleteAll(0, "SMC_EA_");

   // Liberar memoria
   ArrayFree(g_order_blocks);
   ArrayFree(g_fvgs);

   // Guardar estadísticas
   SaveStatistics();

   string reason_text = "";
   switch(reason)
   {
      case REASON_PROGRAM: reason_text = "EA eliminado del gráfico"; break;
      case REASON_REMOVE: reason_text = "EA eliminado del gráfico"; break;
      case REASON_RECOMPILE: reason_text = "EA recompilado"; break;
      case REASON_CHARTCHANGE: reason_text = "Cambio de símbolo/período"; break;
      case REASON_CHARTCLOSE: reason_text = "Gráfico cerrado"; break;
      case REASON_PARAMETERS: reason_text = "Parámetros cambiados"; break;
      case REASON_ACCOUNT: reason_text = "Cambio de cuenta"; break;
      default: reason_text = "Razón desconocida";
   }

   Print("========================================");
   Print("👋 Smart Money Concepts EA Removido");
   Print("Razón: ", reason_text);
   Print("========================================");
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
{
   // Detectar nueva barra
   g_new_bar = IsNewBar();

   if(!g_new_bar)
      return;

   if(InpDebugMode)
      Print("🔄 Nueva barra detectada: ", TimeToString(TimeCurrent()));

   // Actualizar panel
   if(InpShowPanel)
      UpdatePanel();

   // Verificar filtros
   if(!CheckFilters())
   {
      if(InpDebugMode)
         Print("⏸️  Filtros no pasados - esperando...");
      return;
   }

   // Actualizar estructura de mercado
   UpdateMarketStructure();

   // Actualizar Order Blocks
   if(InpUseOrderBlocks)
      UpdateOrderBlocks();

   // Actualizar Fair Value Gaps
   if(InpUseFVG)
      UpdateFVG();

   // Gestionar posiciones abiertas
   ManageOpenPositions();

   // Buscar señales de entrada
   if(CountOpenPositions() == 0)
   {
      CheckEntrySignals();

      if(g_buy_signal)
         OpenBuyPosition();

      if(g_sell_signal)
         OpenSellPosition();
   }
}

//+------------------------------------------------------------------+
//| Detectar nueva barra                                             |
//+------------------------------------------------------------------+
bool IsNewBar()
{
   datetime current_time = iTime(_Symbol, _Period, 0);

   if(current_time != g_last_bar_time)
   {
      g_last_bar_time = current_time;
      return true;
   }

   return false;
}

//+------------------------------------------------------------------+
//| Verificar filtros                                                |
//+------------------------------------------------------------------+
bool CheckFilters()
{
   // Filtro de tiempo
   if(InpUseTimeFilter)
   {
      MqlDateTime dt;
      TimeToStruct(TimeCurrent(), dt);

      // Verificar hora
      if(dt.hour < InpStartHour || dt.hour >= InpEndHour)
         return false;

      // Verificar día de la semana
      switch(dt.day_of_week)
      {
         case 1: if(!InpTradeMonday) return false; break;
         case 2: if(!InpTradeTuesday) return false; break;
         case 3: if(!InpTradeWednesday) return false; break;
         case 4: if(!InpTradeThursday) return false; break;
         case 5: if(!InpTradeFriday) return false; break;
         default: return false; // Sábado/Domingo
      }
   }

   // Filtro de ATR
   if(InpMinATRFilter > 0)
   {
      double atr[];
      ArraySetAsSeries(atr, true);

      if(CopyBuffer(g_atr_handle, 0, 0, 1, atr) <= 0)
      {
         Print("❌ Error copiando ATR para filtro: ", GetLastError());
         return false;
      }

      if(atr[0] < InpMinATRFilter * _Point)
      {
         if(InpDebugMode)
            Print("⏸️  ATR muy bajo: ", atr[0], " < ", InpMinATRFilter * _Point);
         return false;
      }
   }

   // Filtro de spread - CORREGIDO
   long spread = SymbolInfoInteger(_Symbol, SYMBOL_SPREAD);
   if(spread > InpMaxSpreadPoints)
   {
      if(InpDebugMode)
         Print("⏸️  Spread muy alto: ", spread, " > ", InpMaxSpreadPoints);
      return false;
   }

   return true;
}

//+------------------------------------------------------------------+
//| Actualizar estructura de mercado                                 |
//+------------------------------------------------------------------+
void UpdateMarketStructure()
{
   // Detectar swing points principales
   DetectSwingPoints(InpSwingLength, false);

   // Detectar estructura interna
   if(InpUseInternalStructure)
      DetectSwingPoints(InpInternalLength, true);

   // Determinar tendencia principal
   if(g_swing_high.price > 0 && g_swing_low.price < DBL_MAX)
   {
      double high_array[], low_array[];
      ArraySetAsSeries(high_array, true);
      ArraySetAsSeries(low_array, true);

      // VALIDACIÓN AGREGADA
      if(CopyHigh(_Symbol, _Period, 0, 100, high_array) <= 0)
      {
         Print("❌ Error copiando High en UpdateMarketStructure: ", GetLastError());
         return;
      }

      if(CopyLow(_Symbol, _Period, 0, 100, low_array) <= 0)
      {
         Print("❌ Error copiando Low en UpdateMarketStructure: ", GetLastError());
         return;
      }

      // Verificar quiebre de estructura
      double current_close = iClose(_Symbol, _Period, 0);

      // BOS/CHoCH Alcista
      if(current_close > g_swing_high.price)
      {
         if(g_trend < 0)
         {
            // CHoCH - Cambio de tendencia
            if(InpDrawStructure)
               DrawStructureLabel(g_swing_high.time, g_swing_high.price, "CHoCH ↑", clrLime);

            if(InpDebugMode)
               Print("📊 CHoCH Alcista detectado en: ", g_swing_high.price);
         }
         else
         {
            // BOS - Continuación de tendencia
            if(InpDrawStructure)
               DrawStructureLabel(g_swing_high.time, g_swing_high.price, "BOS ↑", clrLime);

            if(InpDebugMode)
               Print("📊 BOS Alcista detectado en: ", g_swing_high.price);
         }

         g_trend = 1;

         // Crear Order Block
         if(InpUseOrderBlocks)
            CreateOrderBlock(false);
      }

      // BOS/CHoCH Bajista
      if(current_close < g_swing_low.price)
      {
         if(g_trend > 0)
         {
            // CHoCH - Cambio de tendencia
            if(InpDrawStructure)
               DrawStructureLabel(g_swing_low.time, g_swing_low.price, "CHoCH ↓", clrRed);

            if(InpDebugMode)
               Print("📊 CHoCH Bajista detectado en: ", g_swing_low.price);
         }
         else
         {
            // BOS - Continuación de tendencia
            if(InpDrawStructure)
               DrawStructureLabel(g_swing_low.time, g_swing_low.price, "BOS ↓", clrRed);

            if(InpDebugMode)
               Print("📊 BOS Bajista detectado en: ", g_swing_low.price);
         }

         g_trend = -1;

         // Crear Order Block
         if(InpUseOrderBlocks)
            CreateOrderBlock(true);
      }
   }
}

//+------------------------------------------------------------------+
//| Detectar swing points                                            |
//+------------------------------------------------------------------+
void DetectSwingPoints(int length, bool is_internal)
{
   double high_array[], low_array[];
   datetime time_array[];

   ArraySetAsSeries(high_array, true);
   ArraySetAsSeries(low_array, true);
   ArraySetAsSeries(time_array, true);

   int bars_needed = length * 2 + 5;

   // VALIDACIÓN AGREGADA
   if(CopyHigh(_Symbol, _Period, 0, bars_needed, high_array) <= 0)
   {
      if(InpDebugMode)
         Print("❌ Error copiando High en DetectSwingPoints: ", GetLastError());
      return;
   }

   if(CopyLow(_Symbol, _Period, 0, bars_needed, low_array) <= 0)
   {
      if(InpDebugMode)
         Print("❌ Error copiando Low en DetectSwingPoints: ", GetLastError());
      return;
   }

   if(CopyTime(_Symbol, _Period, 0, bars_needed, time_array) <= 0)
   {
      if(InpDebugMode)
         Print("❌ Error copiando Time en DetectSwingPoints: ", GetLastError());
      return;
   }

   // Detectar pivot high
   bool is_pivot_high = true;
   for(int i = 1; i <= length; i++)
   {
      if(high_array[length] <= high_array[length - i] ||
         high_array[length] <= high_array[length + i])
      {
         is_pivot_high = false;
         break;
      }
   }

   if(is_pivot_high)
   {
      if(is_internal)
      {
         g_internal_high.price = high_array[length];
         g_internal_high.time = time_array[length];
         g_internal_high.bar_index = length;
         g_internal_high.is_high = true;
      }
      else
      {
         g_swing_high.price = high_array[length];
         g_swing_high.time = time_array[length];
         g_swing_high.bar_index = length;
         g_swing_high.is_high = true;

         g_last_high = g_swing_high.price;
         g_last_high_time = g_swing_high.time;

         if(InpDebugMode)
            Print("🔺 Nuevo Swing High: ", g_last_high);
      }
   }

   // Detectar pivot low
   bool is_pivot_low = true;
   for(int i = 1; i <= length; i++)
   {
      if(low_array[length] >= low_array[length - i] ||
         low_array[length] >= low_array[length + i])
      {
         is_pivot_low = false;
         break;
      }
   }

   if(is_pivot_low)
   {
      if(is_internal)
      {
         g_internal_low.price = low_array[length];
         g_internal_low.time = time_array[length];
         g_internal_low.bar_index = length;
         g_internal_low.is_high = false;
      }
      else
      {
         g_swing_low.price = low_array[length];
         g_swing_low.time = time_array[length];
         g_swing_low.bar_index = length;
         g_swing_low.is_high = false;

         g_last_low = g_swing_low.price;
         g_last_low_time = g_swing_low.time;

         if(InpDebugMode)
            Print("🔻 Nuevo Swing Low: ", g_last_low);
      }
   }
}

//+------------------------------------------------------------------+
//| Crear Order Block                                                |
//+------------------------------------------------------------------+
void CreateOrderBlock(bool is_bearish)
{
   // Verificar límite de OBs
   if(ArraySize(g_order_blocks) >= InpMaxOrderBlocks)
   {
      if(InpDebugMode)
         Print("⚠️  Límite de Order Blocks alcanzado, limpiando...");
      CleanInvalidOrderBlocks();
   }

   double high_array[], low_array[], atr[];
   datetime time_array[];

   ArraySetAsSeries(high_array, true);
   ArraySetAsSeries(low_array, true);
   ArraySetAsSeries(time_array, true);
   ArraySetAsSeries(atr, true);

   // VALIDACIÓN AGREGADA
   if(CopyHigh(_Symbol, _Period, 0, 50, high_array) <= 0)
   {
      Print("❌ Error copiando High en CreateOrderBlock: ", GetLastError());
      return;
   }

   if(CopyLow(_Symbol, _Period, 0, 50, low_array) <= 0)
   {
      Print("❌ Error copiando Low en CreateOrderBlock: ", GetLastError());
      return;
   }

   if(CopyTime(_Symbol, _Period, 0, 50, time_array) <= 0)
   {
      Print("❌ Error copiando Time en CreateOrderBlock: ", GetLastError());
      return;
   }

   if(CopyBuffer(g_atr_handle, 0, 0, 1, atr) <= 0)
   {
      Print("❌ Error copiando ATR en CreateOrderBlock: ", GetLastError());
      return;
   }

   double ob_threshold = atr[0] * 2;

   double best_top = 0;
   double best_bottom = DBL_MAX;
   int best_index = 1;

   // Buscar mejor vela para OB
   for(int i = 1; i < 20; i++)
   {
      double range = high_array[i] - low_array[i];

      if(range < ob_threshold)
      {
         if(is_bearish)
         {
            if(high_array[i] > best_top || best_top == 0)
            {
               best_top = high_array[i];
               best_bottom = low_array[i];
               best_index = i;
            }
         }
         else
         {
            if(low_array[i] < best_bottom)
            {
               best_bottom = low_array[i];
               best_top = high_array[i];
               best_index = i;
            }
         }
      }
   }

   if(best_top > 0 && best_bottom < DBL_MAX)
   {
      int size = ArraySize(g_order_blocks);
      ArrayResize(g_order_blocks, size + 1);

      g_order_blocks[size].top = best_top;
      g_order_blocks[size].bottom = best_bottom;
      g_order_blocks[size].time = time_array[best_index];
      g_order_blocks[size].type = is_bearish ? -1 : 1;
      g_order_blocks[size].bars_ago = 0;
      g_order_blocks[size].valid = true;

      // Dibujar OB
      if(InpDrawStructure)
         DrawOrderBlock(size);

      if(InpDebugMode)
      {
         Print("📦 Order Block creado: ", (is_bearish ? "Bearish" : "Bullish"),
               " Top: ", best_top, " Bottom: ", best_bottom);
      }
   }
}

//+------------------------------------------------------------------+
//| Actualizar Order Blocks                                          |
//+------------------------------------------------------------------+
void UpdateOrderBlocks()
{
   double current_price = iClose(_Symbol, _Period, 0);

   for(int i = ArraySize(g_order_blocks) - 1; i >= 0; i--)
   {
      if(!g_order_blocks[i].valid)
         continue;

      g_order_blocks[i].bars_ago++;

      // Invalidar si es muy antiguo
      if(g_order_blocks[i].bars_ago > InpOBValidityBars)
      {
         g_order_blocks[i].valid = false;
         ObjectDelete(0, "SMC_EA_OB_" + IntegerToString(i));

         if(InpDebugMode)
            Print("🗑️  Order Block expirado (", g_order_blocks[i].bars_ago, " barras)");

         continue;
      }

      // Invalidar si el precio lo rompe completamente
      if(g_order_blocks[i].type == 1 && current_price < g_order_blocks[i].bottom)
      {
         g_order_blocks[i].valid = false;
         ObjectDelete(0, "SMC_EA_OB_" + IntegerToString(i));

         if(InpDebugMode)
            Print("🗑️  Order Block Bullish invalidado (precio rompió)");
      }
      else if(g_order_blocks[i].type == -1 && current_price > g_order_blocks[i].top)
      {
         g_order_blocks[i].valid = false;
         ObjectDelete(0, "SMC_EA_OB_" + IntegerToString(i));

         if(InpDebugMode)
            Print("🗑️  Order Block Bearish invalidado (precio rompió)");
      }
   }

   // Limpieza periódica
   static int cleanup_counter = 0;
   cleanup_counter++;

   if(cleanup_counter >= 20) // Cada 20 barras
   {
      CleanInvalidOrderBlocks();
      cleanup_counter = 0;
   }
}

//+------------------------------------------------------------------+
//| Limpiar Order Blocks inválidos - NUEVA FUNCIÓN                   |
//+------------------------------------------------------------------+
void CleanInvalidOrderBlocks()
{
   int valid_count = 0;

   // Contar válidos
   for(int i = 0; i < ArraySize(g_order_blocks); i++)
      if(g_order_blocks[i].valid)
         valid_count++;

   // Si hay muchos inválidos, reorganizar array
   if(valid_count < ArraySize(g_order_blocks) / 2 && ArraySize(g_order_blocks) > 10)
   {
      OrderBlock temp[];
      ArrayResize(temp, valid_count);

      int index = 0;
      for(int i = 0; i < ArraySize(g_order_blocks); i++)
      {
         if(g_order_blocks[i].valid)
         {
            temp[index] = g_order_blocks[i];
            index++;
         }
      }

      ArrayFree(g_order_blocks);
      ArrayCopy(g_order_blocks, temp);

      if(InpDebugMode)
         Print("🧹 Order Blocks limpiados: ", valid_count, " válidos de ", ArraySize(g_order_blocks));
   }
}

//+------------------------------------------------------------------+
//| Actualizar Fair Value Gaps                                       |
//+------------------------------------------------------------------+
void UpdateFVG()
{
   // Verificar límite de FVGs
   if(ArraySize(g_fvgs) >= InpMaxFVGs)
   {
      if(InpDebugMode)
         Print("⚠️  Límite de FVGs alcanzado, limpiando...");
      CleanInvalidFVGs();
   }

   double high_array[], low_array[], close_array[], open_array[];
   datetime time_array[];

   ArraySetAsSeries(high_array, true);
   ArraySetAsSeries(low_array, true);
   ArraySetAsSeries(close_array, true);
   ArraySetAsSeries(open_array, true);
   ArraySetAsSeries(time_array, true);

   // VALIDACIÓN AGREGADA
   if(CopyHigh(_Symbol, _Period, 0, 5, high_array) <= 0)
   {
      Print("❌ Error copiando High en UpdateFVG: ", GetLastError());
      return;
   }

   if(CopyLow(_Symbol, _Period, 0, 5, low_array) <= 0)
   {
      Print("❌ Error copiando Low en UpdateFVG: ", GetLastError());
      return;
   }

   if(CopyClose(_Symbol, _Period, 0, 5, close_array) <= 0)
   {
      Print("❌ Error copiando Close en UpdateFVG: ", GetLastError());
      return;
   }

   if(CopyOpen(_Symbol, _Period, 0, 5, open_array) <= 0)
   {
      Print("❌ Error copiando Open en UpdateFVG: ", GetLastError());
      return;
   }

   if(CopyTime(_Symbol, _Period, 0, 5, time_array) <= 0)
   {
      Print("❌ Error copiando Time en UpdateFVG: ", GetLastError());
      return;
   }

   // Bullish FVG: low[0] > high[2]
   if(low_array[0] > high_array[2] && close_array[1] > high_array[2])
   {
      int size = ArraySize(g_fvgs);
      ArrayResize(g_fvgs, size + 1);

      g_fvgs[size].top = low_array[0];
      g_fvgs[size].bottom = high_array[2];
      g_fvgs[size].time = time_array[1];
      g_fvgs[size].type = 1;
      g_fvgs[size].bars_ago = 0;
      g_fvgs[size].filled = false;

      if(InpDrawStructure)
         DrawFVG(size);

      if(InpDebugMode)
         Print("💚 FVG Bullish creado: Top=", low_array[0], " Bottom=", high_array[2]);
   }

   // Bearish FVG: high[0] < low[2]
   if(high_array[0] < low_array[2] && close_array[1] < low_array[2])
   {
      int size = ArraySize(g_fvgs);
      ArrayResize(g_fvgs, size + 1);

      g_fvgs[size].top = low_array[2];
      g_fvgs[size].bottom = high_array[0];
      g_fvgs[size].time = time_array[1];
      g_fvgs[size].type = -1;
      g_fvgs[size].bars_ago = 0;
      g_fvgs[size].filled = false;

      if(InpDrawStructure)
         DrawFVG(size);

      if(InpDebugMode)
         Print("❤️  FVG Bearish creado: Top=", low_array[2], " Bottom=", high_array[0]);
   }

   // Actualizar FVGs existentes
   double current_high = high_array[0];
   double current_low = low_array[0];

   for(int i = ArraySize(g_fvgs) - 1; i >= 0; i--)
   {
      if(g_fvgs[i].filled)
         continue;

      g_fvgs[i].bars_ago++;

      // Marcar como rellenado
      if(g_fvgs[i].type == 1 && current_low <= g_fvgs[i].bottom)
      {
         g_fvgs[i].filled = true;
         ObjectDelete(0, "SMC_EA_FVG_" + IntegerToString(i));

         if(InpDebugMode)
            Print("✅ FVG Bullish rellenado");
      }
      else if(g_fvgs[i].type == -1 && current_high >= g_fvgs[i].top)
      {
         g_fvgs[i].filled = true;
         ObjectDelete(0, "SMC_EA_FVG_" + IntegerToString(i));

         if(InpDebugMode)
            Print("✅ FVG Bearish rellenado");
      }

      // Invalidar si es muy antiguo
      if(g_fvgs[i].bars_ago > InpFVGValidityBars)
      {
         g_fvgs[i].filled = true;
         ObjectDelete(0, "SMC_EA_FVG_" + IntegerToString(i));

         if(InpDebugMode)
            Print("🗑️  FVG expirado");
      }
   }

   // Limpieza periódica
   static int cleanup_counter = 0;
   cleanup_counter++;

   if(cleanup_counter >= 20)
   {
      CleanInvalidFVGs();
      cleanup_counter = 0;
   }
}

//+------------------------------------------------------------------+
//| Limpiar FVGs inválidos - NUEVA FUNCIÓN                           |
//+------------------------------------------------------------------+
void CleanInvalidFVGs()
{
   int valid_count = 0;

   // Contar válidos
   for(int i = 0; i < ArraySize(g_fvgs); i++)
      if(!g_fvgs[i].filled)
         valid_count++;

   // Si hay muchos inválidos, reorganizar
   if(valid_count < ArraySize(g_fvgs) / 2 && ArraySize(g_fvgs) > 10)
   {
      FairValueGap temp[];
      ArrayResize(temp, valid_count);

      int index = 0;
      for(int i = 0; i < ArraySize(g_fvgs); i++)
      {
         if(!g_fvgs[i].filled)
         {
            temp[index] = g_fvgs[i];
            index++;
         }
      }

      ArrayFree(g_fvgs);
      ArrayCopy(g_fvgs, temp);

      if(InpDebugMode)
         Print("🧹 FVGs limpiados: ", valid_count, " válidos");
   }
}

//+------------------------------------------------------------------+
//| Verificar señales de entrada                                     |
//+------------------------------------------------------------------+
void CheckEntrySignals()
{
   g_buy_signal = false;
   g_sell_signal = false;

   double current_close = iClose(_Symbol, _Period, 0);
   double current_high = iHigh(_Symbol, _Period, 0);
   double current_low = iLow(_Symbol, _Period, 0);

   bool bullish_structure = (g_trend == 1);
   bool bearish_structure = (g_trend == -1);

   // Si solo operamos con la tendencia
   if(InpTradeOnlyTrend)
   {
      if(!bullish_structure && !bearish_structure)
         return;
   }

   switch(InpEntryType)
   {
      case ENTRY_BOS:
         // Entrada en Break of Structure
         if(bullish_structure && !InpTradeOnlyTrend)
            g_buy_signal = true;
         if(bearish_structure && !InpTradeOnlyTrend)
            g_sell_signal = true;
         break;

      case ENTRY_CHOCH:
         // Entrada en Change of Character
         // Ya detectado en UpdateMarketStructure
         break;

      case ENTRY_OB:
         // Entrada en retroceso a Order Block
         g_buy_signal = CheckOrderBlockEntry(true);
         g_sell_signal = CheckOrderBlockEntry(false);
         break;

      case ENTRY_FVG:
         // Entrada en Fair Value Gap
         g_buy_signal = CheckFVGEntry(true);
         g_sell_signal = CheckFVGEntry(false);
         break;

      case ENTRY_COMBINED:
         // Entrada combinada (múltiples confirmaciones)
         if(bullish_structure || !InpTradeOnlyTrend)
         {
            bool ob_confirm = !InpConfirmWithOB || CheckOrderBlockEntry(true);
            bool fvg_confirm = !InpConfirmWithFVG || CheckFVGEntry(true);

            if(ob_confirm && fvg_confirm)
            {
               g_buy_signal = true;

               if(InpDebugMode)
                  Print("🟢 Señal de COMPRA confirmada (Combinado)");
            }
         }

         if(bearish_structure || !InpTradeOnlyTrend)
         {
            bool ob_confirm = !InpConfirmWithOB || CheckOrderBlockEntry(false);
            bool fvg_confirm = !InpConfirmWithFVG || CheckFVGEntry(false);

            if(ob_confirm && fvg_confirm)
            {
               g_sell_signal = true;

               if(InpDebugMode)
                  Print("🔴 Señal de VENTA confirmada (Combinado)");
            }
         }
         break;
   }
}

//+------------------------------------------------------------------+
//| Verificar entrada en Order Block                                 |
//+------------------------------------------------------------------+
bool CheckOrderBlockEntry(bool is_buy)
{
   double current_close = iClose(_Symbol, _Period, 0);
   double current_low = iLow(_Symbol, _Period, 0);
   double current_high = iHigh(_Symbol, _Period, 0);

   for(int i = 0; i < ArraySize(g_order_blocks); i++)
   {
      if(!g_order_blocks[i].valid)
         continue;

      if(is_buy && g_order_blocks[i].type == 1)
      {
         // Verificar si el precio está dentro del OB alcista
         if(current_low <= g_order_blocks[i].top &&
            current_close >= g_order_blocks[i].bottom)
         {
            if(InpDebugMode)
               Print("✅ Precio en OB Bullish");
            return true;
         }
      }
      else if(!is_buy && g_order_blocks[i].type == -1)
      {
         // Verificar si el precio está dentro del OB bajista
         if(current_high >= g_order_blocks[i].bottom &&
            current_close <= g_order_blocks[i].top)
         {
            if(InpDebugMode)
               Print("✅ Precio en OB Bearish");
            return true;
         }
      }
   }

   return false;
}

//+------------------------------------------------------------------+
//| Verificar entrada en FVG                                         |
//+------------------------------------------------------------------+
bool CheckFVGEntry(bool is_buy)
{
   double current_close = iClose(_Symbol, _Period, 0);
   double current_low = iLow(_Symbol, _Period, 0);
   double current_high = iHigh(_Symbol, _Period, 0);

   for(int i = 0; i < ArraySize(g_fvgs); i++)
   {
      if(g_fvgs[i].filled)
         continue;

      if(is_buy && g_fvgs[i].type == 1)
      {
         // Precio retrocede al FVG alcista
         if(current_low <= g_fvgs[i].top &&
            current_close >= g_fvgs[i].bottom)
         {
            if(InpDebugMode)
               Print("✅ Precio en FVG Bullish");
            return true;
         }
      }
      else if(!is_buy && g_fvgs[i].type == -1)
      {
         // Precio retrocede al FVG bajista
         if(current_high >= g_fvgs[i].bottom &&
            current_close <= g_fvgs[i].top)
         {
            if(InpDebugMode)
               Print("✅ Precio en FVG Bearish");
            return true;
         }
      }
   }

   return false;
}

//+------------------------------------------------------------------+
//| Abrir posición de compra                                         |
//+------------------------------------------------------------------+
void OpenBuyPosition()
{
   double entry = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   double sl = CalculateStopLoss(true, entry);
   double tp = CalculateTakeProfit(true, entry, sl);
   double lot = CalculateLotSize(entry, sl);

   // Validar SL
   if(sl >= entry)
   {
      Print("❌ Error: SL inválido (", sl, " >= ", entry, ")");
      g_buy_signal = false;
      return;
   }

   // Validar TP
   if(tp <= entry)
   {
      Print("❌ Error: TP inválido (", tp, " <= ", entry, ")");
      g_buy_signal = false;
      return;
   }

   // Validar lote
   double min_lot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   if(lot < min_lot)
   {
      Print("❌ Lote calculado muy pequeño: ", lot, " < ", min_lot);
      g_buy_signal = false;
      return;
   }

   if(trade.Buy(lot, _Symbol, entry, sl, tp, InpTradeComment))
   {
      Print("========================================");
      Print("✅ COMPRA ABIERTA");
      Print("Precio: ", entry);
      Print("SL: ", sl, " (", DoubleToString((entry - sl) / _Point, 0), " puntos)");
      Print("TP: ", tp, " (", DoubleToString((tp - entry) / _Point, 0), " puntos)");
      Print("Lote: ", lot);
      Print("R:R: 1:", DoubleToString((tp - entry) / (entry - sl), 2));
      Print("========================================");

      g_entry_price = entry;
      g_sl_price = sl;
      g_tp_price = tp;
      g_total_trades++;
   }
   else
   {
      Print("========================================");
      Print("❌ ERROR ABRIENDO COMPRA");
      Print("Código de error: ", GetLastError());
      Print("Último precio: ", entry);
      Print("SL: ", sl);
      Print("TP: ", tp);
      Print("Lote: ", lot);
      Print("========================================");
   }

   g_buy_signal = false;
}

//+------------------------------------------------------------------+
//| Abrir posición de venta                                          |
//+------------------------------------------------------------------+
void OpenSellPosition()
{
   double entry = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double sl = CalculateStopLoss(false, entry);
   double tp = CalculateTakeProfit(false, entry, sl);
   double lot = CalculateLotSize(entry, sl);

   // Validar SL
   if(sl <= entry)
   {
      Print("❌ Error: SL inválido (", sl, " <= ", entry, ")");
      g_sell_signal = false;
      return;
   }

   // Validar TP
   if(tp >= entry)
   {
      Print("❌ Error: TP inválido (", tp, " >= ", entry, ")");
      g_sell_signal = false;
      return;
   }

   // Validar lote
   double min_lot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   if(lot < min_lot)
   {
      Print("❌ Lote calculado muy pequeño: ", lot, " < ", min_lot);
      g_sell_signal = false;
      return;
   }

   if(trade.Sell(lot, _Symbol, entry, sl, tp, InpTradeComment))
   {
      Print("========================================");
      Print("✅ VENTA ABIERTA");
      Print("Precio: ", entry);
      Print("SL: ", sl, " (", DoubleToString((sl - entry) / _Point, 0), " puntos)");
      Print("TP: ", tp, " (", DoubleToString((entry - tp) / _Point, 0), " puntos)");
      Print("Lote: ", lot);
      Print("R:R: 1:", DoubleToString((entry - tp) / (sl - entry), 2));
      Print("========================================");

      g_entry_price = entry;
      g_sl_price = sl;
      g_tp_price = tp;
      g_total_trades++;
   }
   else
   {
      Print("========================================");
      Print("❌ ERROR ABRIENDO VENTA");
      Print("Código de error: ", GetLastError());
      Print("Último precio: ", entry);
      Print("SL: ", sl);
      Print("TP: ", tp);
      Print("Lote: ", lot);
      Print("========================================");
   }

   g_sell_signal = false;
}

//+------------------------------------------------------------------+
//| Calcular Stop Loss                                               |
//+------------------------------------------------------------------+
double CalculateStopLoss(bool is_buy, double entry)
{
   double sl = 0;

   switch(InpSLType)
   {
      case SL_ATR:
         {
            double atr[];
            ArraySetAsSeries(atr, true);

            if(CopyBuffer(g_atr_handle, 0, 0, 1, atr) <= 0)
            {
               Print("❌ Error copiando ATR para SL: ", GetLastError());
               // Fallback a puntos fijos
               sl = is_buy ? entry - InpSLPoints * _Point : entry + InpSLPoints * _Point;
            }
            else
            {
               if(is_buy)
                  sl = entry - atr[0] * InpSLATRMultiplier;
               else
                  sl = entry + atr[0] * InpSLATRMultiplier;
            }
         }
         break;

      case SL_FIXED_POINTS:
         {
            if(is_buy)
               sl = entry - InpSLPoints * _Point;
            else
               sl = entry + InpSLPoints * _Point;
         }
         break;

      case SL_STRUCTURE:
         {
            if(is_buy)
            {
               if(g_last_low < DBL_MAX)
                  sl = g_last_low - 10 * _Point;  // Debajo del último low
               else
                  sl = entry - InpSLPoints * _Point; // Fallback
            }
            else
            {
               if(g_last_high > 0)
                  sl = g_last_high + 10 * _Point;  // Encima del último high
               else
                  sl = entry + InpSLPoints * _Point; // Fallback
            }
         }
         break;
   }

   return NormalizeDouble(sl, _Digits);
}

//+------------------------------------------------------------------+
//| Calcular Take Profit                                             |
//+------------------------------------------------------------------+
double CalculateTakeProfit(bool is_buy, double entry, double sl)
{
   double tp = 0;
   double sl_distance = MathAbs(entry - sl);

   switch(InpTPType)
   {
      case TP_RISK_REWARD:
         {
            if(is_buy)
               tp = entry + sl_distance * InpRiskReward;
            else
               tp = entry - sl_distance * InpRiskReward;
         }
         break;

      case TP_ATR:
         {
            double atr[];
            ArraySetAsSeries(atr, true);

            if(CopyBuffer(g_atr_handle, 0, 0, 1, atr) <= 0)
            {
               Print("❌ Error copiando ATR para TP: ", GetLastError());
               // Fallback a R:R
               tp = is_buy ? entry + sl_distance * InpRiskReward : entry - sl_distance * InpRiskReward;
            }
            else
            {
               if(is_buy)
                  tp = entry + atr[0] * InpTPATRMultiplier;
               else
                  tp = entry - atr[0] * InpTPATRMultiplier;
            }
         }
         break;

      case TP_FIXED_POINTS:
         {
            if(is_buy)
               tp = entry + InpTPPoints * _Point;
            else
               tp = entry - InpTPPoints * _Point;
         }
         break;

      case TP_STRUCTURE:
         {
            if(is_buy)
            {
               if(g_last_high > 0)
                  tp = g_last_high;  // Último high
               else
                  tp = entry + sl_distance * InpRiskReward; // Fallback
            }
            else
            {
               if(g_last_low < DBL_MAX)
                  tp = g_last_low;   // Último low
               else
                  tp = entry - sl_distance * InpRiskReward; // Fallback
            }
         }
         break;
   }

   return NormalizeDouble(tp, _Digits);
}

//+------------------------------------------------------------------+
//| Calcular tamaño de lote - VERSIÓN MEJORADA                       |
//+------------------------------------------------------------------+
double CalculateLotSize(double entry, double sl)
{
   double lot = 0;
   double sl_distance = MathAbs(entry - sl);

   if(sl_distance == 0)
   {
      Print("⚠️  SL distance es 0, usando lote mínimo");
      return SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   }

   switch(InpRiskType)
   {
      case RISK_FIXED_LOT:
         lot = InpFixedLot;
         break;

      case RISK_PERCENT:
      case RISK_FIXED_MONEY:
         {
            double balance = AccountInfoDouble(ACCOUNT_BALANCE);
            double risk_amount = (InpRiskType == RISK_PERCENT) ?
                                 balance * InpRiskPercent / 100.0 : InpFixedMoney;

            // Obtener valores del símbolo
            double tick_value = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);
            double tick_size = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_SIZE);
            double point = SymbolInfoDouble(_Symbol, SYMBOL_POINT);

            // Validar valores
            if(tick_size <= 0 || tick_value <= 0)
            {
               Print("❌ Error: tick_size=", tick_size, " tick_value=", tick_value);
               return SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
            }

            // Calcular lote basado en riesgo
            // Fórmula: Lote = RiskAmount / (SL_distance / tick_size * tick_value)
            double sl_in_ticks = sl_distance / tick_size;

            if(sl_in_ticks > 0)
               lot = risk_amount / (sl_in_ticks * tick_value);
            else
               lot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);

            if(InpDebugMode)
            {
               Print("📊 Cálculo de Lote:");
               Print("  Balance: ", balance);
               Print("  Risk Amount: $", risk_amount);
               Print("  SL Distance: ", sl_distance);
               Print("  SL in ticks: ", sl_in_ticks);
               Print("  Tick Value: ", tick_value);
               Print("  Lote calculado: ", lot);
            }
         }
         break;
   }

   // Normalizar lote
   double min_lot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double max_lot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double lot_step = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);

   if(lot_step > 0)
      lot = MathFloor(lot / lot_step) * lot_step;

   lot = MathMax(lot, min_lot);
   lot = MathMin(lot, max_lot);

   return NormalizeDouble(lot, 2);
}

//+------------------------------------------------------------------+
//| Gestionar posiciones abiertas - VERSIÓN MEJORADA                 |
//+------------------------------------------------------------------+
void ManageOpenPositions()
{
   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      if(!positionInfo.SelectByIndex(i))
         continue;

      if(positionInfo.Symbol() != _Symbol || positionInfo.Magic() != InpMagicNumber)
         continue;

      ulong ticket = positionInfo.Ticket();
      double entry = positionInfo.PriceOpen();
      double sl = positionInfo.StopLoss();
      double tp = positionInfo.TakeProfit();
      bool is_buy = (positionInfo.Type() == POSITION_TYPE_BUY);

      double current_price = is_buy ? SymbolInfoDouble(_Symbol, SYMBOL_BID) :
                                     SymbolInfoDouble(_Symbol, SYMBOL_ASK);

      double profit_distance = is_buy ? (current_price - entry) : (entry - current_price);
      double sl_distance = MathAbs(entry - sl);

      // Evitar división por cero
      if(sl_distance == 0)
         continue;

      double rr_ratio = profit_distance / sl_distance;

      // Breakeven
      if(InpUseBreakeven && rr_ratio >= InpBreakevenAt)
      {
         double be_price = entry + (is_buy ? 1 : -1) * sl_distance * InpBreakevenPlus;
         be_price = NormalizeDouble(be_price, _Digits);

         bool should_modify = false;

         // Verificar si ya está en BE o mejor
         if(is_buy && sl < be_price - _Point)
            should_modify = true;
         else if(!is_buy && sl > be_price + _Point)
            should_modify = true;

         if(should_modify)
         {
            if(trade.PositionModify(ticket, be_price, tp))
            {
               Print("========================================");
               Print("💚 BREAKEVEN ACTIVADO");
               Print("Ticket: ", ticket);
               Print("Nuevo SL: ", be_price);
               Print("R:R actual: ", DoubleToString(rr_ratio, 2));
               Print("========================================");
            }
            else
            {
               Print("❌ Error en Breakeven: ", GetLastError());
            }
         }
      }

      // Trailing Stop
      if(InpUseTrailing && rr_ratio >= InpTrailingStart)
      {
         double trailing_distance = sl_distance * InpTrailingStep;
         double new_sl = 0;

         if(is_buy)
         {
            new_sl = NormalizeDouble(current_price - trailing_distance, _Digits);

            // Solo mover SL hacia arriba
            if(new_sl > sl + _Point)
            {
               if(trade.PositionModify(ticket, new_sl, tp))
               {
                  Print("========================================");
                  Print("📈 TRAILING STOP ACTUALIZADO (COMPRA)");
                  Print("Ticket: ", ticket);
                  Print("Nuevo SL: ", new_sl);
                  Print("Anterior SL: ", sl);
                  Print("R:R actual: ", DoubleToString(rr_ratio, 2));
                  Print("========================================");
               }
               else
               {
                  Print("❌ Error Trailing Stop: ", GetLastError());
               }
            }
         }
         else
         {
            new_sl = NormalizeDouble(current_price + trailing_distance, _Digits);

            // Solo mover SL hacia abajo
            if(new_sl < sl - _Point)
            {
               if(trade.PositionModify(ticket, new_sl, tp))
               {
                  Print("========================================");
                  Print("📉 TRAILING STOP ACTUALIZADO (VENTA)");
                  Print("Ticket: ", ticket);
                  Print("Nuevo SL: ", new_sl);
                  Print("Anterior SL: ", sl);
                  Print("R:R actual: ", DoubleToString(rr_ratio, 2));
                  Print("========================================");
               }
               else
               {
                  Print("❌ Error Trailing Stop: ", GetLastError());
               }
            }
         }
      }
   }
}

//+------------------------------------------------------------------+
//| Contar posiciones abiertas                                       |
//+------------------------------------------------------------------+
int CountOpenPositions()
{
   int count = 0;

   for(int i = 0; i < PositionsTotal(); i++)
   {
      if(positionInfo.SelectByIndex(i))
      {
         if(positionInfo.Symbol() == _Symbol && positionInfo.Magic() == InpMagicNumber)
            count++;
      }
   }

   return count;
}

//+------------------------------------------------------------------+
//| Crear panel de información                                       |
//+------------------------------------------------------------------+
void CreatePanel()
{
   // Eliminar panel existente primero
   ObjectsDeleteAll(0, "SMC_EA_Panel");

   // Verificar si ya existe
   if(ObjectFind(0, "SMC_EA_Panel_BG") >= 0)
   {
      if(InpDebugMode)
         Print("⚠️  Panel ya existe, recreando...");
      ObjectsDeleteAll(0, "SMC_EA_Panel");
   }

   // Fondo del panel
   ObjectCreate(0, "SMC_EA_Panel_BG", OBJ_RECTANGLE_LABEL, 0, 0, 0);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_XDISTANCE, InpPanelX);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_YDISTANCE, InpPanelY);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_XSIZE, 280);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_YSIZE, 220);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_BGCOLOR, InpPanelColor);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_BORDER_TYPE, BORDER_FLAT);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_CORNER, CORNER_LEFT_UPPER);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_BACK, false);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, "SMC_EA_Panel_BG", OBJPROP_HIDDEN, true);

   // Título
   CreatePanelLabel("SMC_EA_Panel_Title", "💎 Smart Money EA v2.0", InpPanelX + 10, InpPanelY + 10,
                    clrWhite, 10, "Arial Bold");

   // Línea separadora
   CreatePanelLabel("SMC_EA_Panel_Line", "─────────────────────────", InpPanelX + 10, InpPanelY + 30,
                    clrDarkGray, 8, "Arial");

   // Información
   CreatePanelLabel("SMC_EA_Panel_Trend", "Trend: -", InpPanelX + 10, InpPanelY + 50,
                    clrWhite, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_Positions", "Positions: 0", InpPanelX + 10, InpPanelY + 70,
                    clrWhite, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_Trades", "Total Trades: 0", InpPanelX + 10, InpPanelY + 90,
                    clrWhite, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_WinRate", "Win Rate: 0%", InpPanelX + 10, InpPanelY + 110,
                    clrWhite, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_Profit", "Profit: $0.00", InpPanelX + 10, InpPanelY + 130,
                    clrWhite, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_Signal", "Signal: WAITING", InpPanelX + 10, InpPanelY + 155,
                    clrGray, 9, "Arial");
   CreatePanelLabel("SMC_EA_Panel_Time", TimeToString(TimeCurrent(), TIME_SECONDS),
                    InpPanelX + 10, InpPanelY + 180, clrSilver, 8, "Courier New");
   CreatePanelLabel("SMC_EA_Panel_Status", "✅ EA Active", InpPanelX + 10, InpPanelY + 195,
                    clrLime, 8, "Arial");

   if(InpDebugMode)
      Print("✅ Panel creado exitosamente");
}

//+------------------------------------------------------------------+
//| Crear etiqueta del panel                                         |
//+------------------------------------------------------------------+
void CreatePanelLabel(string name, string text, int x, int y, color clr, int font_size, string font = "Arial")
{
   ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, y);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, font_size);
   ObjectSetString(0, name, OBJPROP_FONT, font);
   ObjectSetString(0, name, OBJPROP_TEXT, text);
   ObjectSetInteger(0, name, OBJPROP_CORNER, CORNER_LEFT_UPPER);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
}

//+------------------------------------------------------------------+
//| Actualizar panel                                                 |
//+------------------------------------------------------------------+
void UpdatePanel()
{
   if(!InpShowPanel)
      return;

   // Tendencia
   string trend_text = "Trend: ";
   color trend_color = clrWhite;

   if(g_trend == 1)
   {
      trend_text += "BULLISH 🟢";
      trend_color = clrLime;
   }
   else if(g_trend == -1)
   {
      trend_text += "BEARISH 🔴";
      trend_color = clrRed;
   }
   else
   {
      trend_text += "RANGING ⚪";
      trend_color = clrYellow;
   }

   ObjectSetString(0, "SMC_EA_Panel_Trend", OBJPROP_TEXT, trend_text);
   ObjectSetInteger(0, "SMC_EA_Panel_Trend", OBJPROP_COLOR, trend_color);

   // Posiciones
   int pos_count = CountOpenPositions();
   ObjectSetString(0, "SMC_EA_Panel_Positions", OBJPROP_TEXT,
                   "Positions: " + IntegerToString(pos_count));

   // Trades totales
   ObjectSetString(0, "SMC_EA_Panel_Trades", OBJPROP_TEXT,
                   "Total Trades: " + IntegerToString(g_total_trades));

   // Win Rate
   double win_rate = (g_total_trades > 0) ?
                     (double)g_winning_trades / g_total_trades * 100 : 0;
   string wr_text = "Win Rate: " + DoubleToString(win_rate, 1) + "%";
   color wr_color = clrWhite;

   if(win_rate >= 60)
      wr_color = clrLime;
   else if(win_rate >= 40)
      wr_color = clrYellow;
   else if(g_total_trades > 5)
      wr_color = clrOrange;

   ObjectSetString(0, "SMC_EA_Panel_WinRate", OBJPROP_TEXT, wr_text);
   ObjectSetInteger(0, "SMC_EA_Panel_WinRate", OBJPROP_COLOR, wr_color);

   // Profit
   double current_profit = AccountInfoDouble(ACCOUNT_PROFIT);
   color profit_color = (current_profit >= 0) ? clrLime : clrRed;
   string profit_symbol = (current_profit >= 0) ? "+" : "";

   ObjectSetString(0, "SMC_EA_Panel_Profit", OBJPROP_TEXT,
                   "Profit: " + profit_symbol + "$" + DoubleToString(current_profit, 2));
   ObjectSetInteger(0, "SMC_EA_Panel_Profit", OBJPROP_COLOR, profit_color);

   // Señal
   string signal_text = "Signal: ";
   color signal_color = clrGray;

   if(g_buy_signal)
   {
      signal_text += "BUY 🟢";
      signal_color = clrLime;
   }
   else if(g_sell_signal)
   {
      signal_text += "SELL 🔴";
      signal_color = clrRed;
   }
   else if(pos_count > 0)
   {
      signal_text += "IN TRADE";
      signal_color = clrCyan;
   }
   else
   {
      signal_text += "WAITING";
      signal_color = clrGray;
   }

   ObjectSetString(0, "SMC_EA_Panel_Signal", OBJPROP_TEXT, signal_text);
   ObjectSetInteger(0, "SMC_EA_Panel_Signal", OBJPROP_COLOR, signal_color);

   // Hora
   ObjectSetString(0, "SMC_EA_Panel_Time", OBJPROP_TEXT,
                   TimeToString(TimeCurrent(), TIME_SECONDS));
}

//+------------------------------------------------------------------+
//| Dibujar etiqueta de estructura                                   |
//+------------------------------------------------------------------+
void DrawStructureLabel(datetime time, double price, string text, color clr)
{
   string name = "SMC_EA_Label_" + TimeToString(time) + "_" + DoubleToString(price, _Digits);

   // Evitar duplicados
   if(ObjectFind(0, name) >= 0)
      return;

   ObjectCreate(0, name, OBJ_TEXT, 0, time, price);
   ObjectSetString(0, name, OBJPROP_TEXT, text);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, 10);
   ObjectSetString(0, name, OBJPROP_FONT, "Arial Bold");
   ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_CENTER);
   ObjectSetInteger(0, name, OBJPROP_BACK, false);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
}

//+------------------------------------------------------------------+
//| Dibujar Order Block                                              |
//+------------------------------------------------------------------+
void DrawOrderBlock(int index)
{
   string name = "SMC_EA_OB_" + IntegerToString(index);

   // Si ya existe, no duplicar
   if(ObjectFind(0, name) >= 0)
      ObjectDelete(0, name);

   datetime end_time = TimeCurrent() + PeriodSeconds(_Period) * InpOBValidityBars;

   color ob_color = (g_order_blocks[index].type == 1) ?
                    clrDodgerBlue : clrCrimson;

   ObjectCreate(0, name, OBJ_RECTANGLE, 0,
                g_order_blocks[index].time, g_order_blocks[index].top,
                end_time, g_order_blocks[index].bottom);
   ObjectSetInteger(0, name, OBJPROP_COLOR, ob_color);
   ObjectSetInteger(0, name, OBJPROP_FILL, true);
   ObjectSetInteger(0, name, OBJPROP_BACK, true);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 1);
   ObjectSetInteger(0, name, OBJPROP_STYLE, STYLE_SOLID);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetString(0, name, OBJPROP_TOOLTIP, "Order Block " +
                   (g_order_blocks[index].type == 1 ? "Bullish" : "Bearish"));
}

//+------------------------------------------------------------------+
//| Dibujar FVG                                                      |
//+------------------------------------------------------------------+
void DrawFVG(int index)
{
   string name = "SMC_EA_FVG_" + IntegerToString(index);

   // Si ya existe, no duplicar
   if(ObjectFind(0, name) >= 0)
      ObjectDelete(0, name);

   datetime end_time = g_fvgs[index].time + PeriodSeconds(_Period) * InpFVGValidityBars;

   color fvg_color = (g_fvgs[index].type == 1) ?
                     clrLimeGreen : clrOrangeRed;

   ObjectCreate(0, name, OBJ_RECTANGLE, 0,
                g_fvgs[index].time, g_fvgs[index].top,
                end_time, g_fvgs[index].bottom);
   ObjectSetInteger(0, name, OBJPROP_COLOR, fvg_color);
   ObjectSetInteger(0, name, OBJPROP_FILL, true);
   ObjectSetInteger(0, name, OBJPROP_BACK, true);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 1);
   ObjectSetInteger(0, name, OBJPROP_STYLE, STYLE_DOT);
   ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
   ObjectSetString(0, name, OBJPROP_TOOLTIP, "Fair Value Gap " +
                   (g_fvgs[index].type == 1 ? "Bullish" : "Bearish"));
}

//+------------------------------------------------------------------+
//| Cargar estadísticas - VERSIÓN OPTIMIZADA                         |
//+------------------------------------------------------------------+
void LoadStatistics()
{
   // Solo cargar últimos 90 días para mejor performance
   datetime start_date = TimeCurrent() - PeriodSeconds(PERIOD_D1) * 90;

   if(!HistorySelect(start_date, TimeCurrent()))
   {
      if(InpDebugMode)
         Print("⚠️  No se pudo cargar historial");
      return;
   }

   int deals_count = 0;

   for(int i = 0; i < HistoryDealsTotal(); i++)
   {
      ulong ticket = HistoryDealGetTicket(i);

      if(ticket == 0)
         continue;

      if(HistoryDealGetInteger(ticket, DEAL_MAGIC) != InpMagicNumber)
         continue;

      if(HistoryDealGetString(ticket, DEAL_SYMBOL) != _Symbol)
         continue;

      if(HistoryDealGetInteger(ticket, DEAL_ENTRY) == DEAL_ENTRY_OUT)
      {
         double profit = HistoryDealGetDouble(ticket, DEAL_PROFIT);

         if(profit > 0)
            g_winning_trades++;
         else if(profit < 0)
            g_losing_trades++;

         g_total_profit += profit;
         deals_count++;
      }
   }

   g_total_trades = g_winning_trades + g_losing_trades;

   if(InpDebugMode && g_total_trades > 0)
   {
      Print("📊 Estadísticas cargadas:");
      Print("  Total trades: ", g_total_trades);
      Print("  Ganadores: ", g_winning_trades);
      Print("  Perdedores: ", g_losing_trades);
      Print("  Win Rate: ", DoubleToString((double)g_winning_trades/g_total_trades*100, 2), "%");
      Print("  Profit Total: $", DoubleToString(g_total_profit, 2));
   }
}

//+------------------------------------------------------------------+
//| Guardar estadísticas                                             |
//+------------------------------------------------------------------+
void SaveStatistics()
{
   Print("========================================");
   Print("📊 ESTADÍSTICAS FINALES");
   Print("========================================");
   Print("Total Trades: ", g_total_trades);
   Print("Winning Trades: ", g_winning_trades);
   Print("Losing Trades: ", g_losing_trades);

   if(g_total_trades > 0)
   {
      double win_rate = (double)g_winning_trades / g_total_trades * 100;
      Print("Win Rate: ", DoubleToString(win_rate, 2), "%");
   }
   else
   {
      Print("Win Rate: N/A");
   }

   Print("Total Profit: $", DoubleToString(g_total_profit, 2));
   Print("Order Blocks activos: ", CountValidOBs());
   Print("FVGs activos: ", CountValidFVGs());
   Print("========================================");
}

//+------------------------------------------------------------------+
//| Contar Order Blocks válidos                                      |
//+------------------------------------------------------------------+
int CountValidOBs()
{
   int count = 0;
   for(int i = 0; i < ArraySize(g_order_blocks); i++)
      if(g_order_blocks[i].valid)
         count++;
   return count;
}

//+------------------------------------------------------------------+
//| Contar FVGs válidos                                              |
//+------------------------------------------------------------------+
int CountValidFVGs()
{
   int count = 0;
   for(int i = 0; i < ArraySize(g_fvgs); i++)
      if(!g_fvgs[i].filled)
         count++;
   return count;
}

//+------------------------------------------------------------------+
