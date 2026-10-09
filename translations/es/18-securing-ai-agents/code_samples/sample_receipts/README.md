# Archivos de recibo de ejemplo

Tres archivos de recibo pre-generados para inspección sin ejecutar el cuaderno.

| Archivo | Qué es |
|---|---|
| `01_valid_receipt.json` | Un recibo firmado válido para una llamada a la herramienta `lookup_flights`. La verificación devuelve True. |
| `02_tampered_receipt.json` | El mismo recibo con un campo modificado después de la firma. La verificación devuelve False. |
| `03_chain_three_receipts.json` | Una cadena de tres recibos válidos (buscar, reservar provisionalmente, reservar) con `previous_receipt_hash` vinculando cada uno al anterior. |

Los archivos firman directamente los bytes canónicos JCS del contenido con Ed25519.
SHA-256 se sigue usando para digerir contenido y enlaces en la cadena de recibos, no como un
pre-hash adicional antes de firmar.

## Verificando las muestras

El cuaderno recorre la verificación en cuatro secciones. Para verificar estos archivos
directamente sin seguir la narrativa del cuaderno:

```python
import json
from pathlib import Path

# Asume que has completado las importaciones y funciones auxiliares
# de las secciones 1 y 2 de 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Verdadero

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cómo se generaron

Los archivos usan el mismo código que el cuaderno, con una clave de firma fija
y marcas de tiempo fijas para reproducibilidad a nivel de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(El script está en `generate_fixtures.py` en este directorio.)

## Qué aprenden los estudiantes al inspeccionar el JSON bruto

Leer el formato bruto del recibo construye intuición que las celdas del cuaderno
no siempre proporcionan. Los estudiantes que examinan el JSON a menudo notan:

1. La firma es una cadena opaca base64url, pero todos los demás campos son JSON legible
   en texto plano. La firma no encripta el contenido; lo atestigua.
2. La `public_key` está incrustada en el recibo. Un auditor no necesita nada más
   para verificar (sujeto a confiar que la clave realmente pertenece al emisor
   reclamado; vea el README de la lección sobre infraestructura de identidad).
3. Modificar un solo carácter de cualquier campo y luego comparar este archivo con
   `02_tampered_receipt.json`, hace que el mecanismo a nivel de bytes sea concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->