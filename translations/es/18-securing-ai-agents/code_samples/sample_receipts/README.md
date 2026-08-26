# Archivos de factura de ejemplo

Tres archivos de factura pre-generados para inspección sin ejecutar el cuaderno.

| Archivo | Qué es |
|---|---|
| `01_valid_receipt.json` | Una factura firmada válida para una llamada a la herramienta `lookup_flights`. La verificación devuelve True. |
| `02_tampered_receipt.json` | La misma factura con un campo modificado después de la firma. La verificación devuelve False. |
| `03_chain_three_receipts.json` | Una cadena de tres facturas válidas (búsqueda, retención, reserva) con `previous_receipt_hash` enlazando cada una con la anterior. |

Los archivos firman directamente los bytes canónicos JCS de la carga útil con Ed25519.
SHA-256 sigue usándose para digests de contenido y enlaces de cadena de recibos, no como un
prehash extra antes de firmar.

## Verificación de los ejemplos

El cuaderno recorre la verificación en cuatro secciones. Para verificar estos archivos
directamente sin pasar por la narrativa del cuaderno:

```python
import json
from pathlib import Path

# Se asume que has completado las importaciones y funciones auxiliares
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

Los archivos usan la misma ruta de código que el cuaderno, con una clave de firma fija
y marcas de tiempo fijas para reproducibilidad de bytes. Para regenerarlos:

```bash
python3 generate_fixtures.py
```

(El script está en `generate_fixtures.py` en este directorio.)

## Qué aprenden los estudiantes al inspeccionar el JSON sin procesar

Leer el formato bruto de la factura construye una intuición que las celdas en el cuaderno
no siempre proporcionan. Los estudiantes que ojean el JSON a menudo notan:

1. La firma es una cadena opaca en base64url, pero todos los demás campos son JSON plano
   legible. La firma no cifra el contenido; lo certifica.
2. La `public_key` está incrustada en la factura. Un auditor no necesita nada más
   para verificar (sujeto a confiar en que la clave realmente pertenece al emisario reclamado;
   vea el README de la lección sobre infraestructura de identidad).
3. Modificar un solo carácter de cualquier campo, y luego comparar este archivo con
   `02_tampered_receipt.json`, hace que el mecanismo a nivel de bytes sea concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->