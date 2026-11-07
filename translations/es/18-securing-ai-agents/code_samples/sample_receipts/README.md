# Archivos de recibo de ejemplo

Cuatro archivos de recibo pre-generados para inspección sin ejecutar el cuaderno.

| Archivo | Qué es |
|---|---|
| `01_valid_receipt.json` | Un recibo válido firmado para una llamada a la herramienta `lookup_flights`. La verificación devuelve True. |
| `02_tampered_receipt.json` | El mismo recibo con un campo modificado después de firmar. La verificación devuelve False. |
| `03_chain_three_receipts.json` | Una cadena de tres recibos válidos (búsqueda, retención, reserva) con `previous_receipt_hash` enlazando cada uno con el anterior. |
| `04_resigned_receipt.json` | El mismo recibo manipulado y luego firmado de nuevo por un atacante, con la clave pública del atacante incrustada. Verifica contra la clave que contiene. Falla contra la clave del emisor. |

Los archivos firman los bytes canónicos JCS del contenido directamente con Ed25519.
SHA-256 sigue usándose para los resúmenes de contenido y enlaces de la cadena de recibos, no como un 
pre-hash extra antes de firmar.

## Verificación de los ejemplos

En `18-signed-receipts.ipynb`, ejecute primero Setup y las Secciones 1 a 3.
La Sección 3 define `verify_chain`; las Secciones 1 y 2 por sí solas no son suficientes.
Luego ejecute el siguiente bloque en una celda nueva, con el directorio de trabajo del cuaderno
establecido en `18-securing-ai-agents/code_samples`. Las rutas de los archivos de ejemplo a continuación son relativas
a ese directorio.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Comprobando el ejemplo sin Jupyter

Desde la raíz del repositorio, instale las dependencias de la lección y ejecute:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Estas pruebas ejecutan los ejemplos en Python del cuaderno y el bloque exacto del README
de arriba. También comprueban que se rechacen la manipulación y las claves no fijadas por
los verificadores. Las pruebas omiten la celda de configuración `%pip` del cuaderno porque las dependencias
se instalan por separado. No modifican el cuaderno ni los archivos de ejemplo.

## Cómo se generaron

Los archivos usan la misma ruta de código que el cuaderno, con una clave de firma fija
y marcas de tiempo fijas para reproducibilidad byte a byte. Para regenerar:

```bash
python3 generate_fixtures.py
```

(El script está en `generate_fixtures.py` en este directorio.)

`../test_signed_receipts.py` verifica todo esto automáticamente: ejecuta el
código del cuaderno, verifica estos cuatro archivos con el
`verify_receipt` y `verify_chain` del cuaderno, y confirma que regenerar los
archivos da bytes idénticos. Desde `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Lo que los estudiantes aprenden al inspeccionar JSON sin procesar

Leer el formato de recibo sin procesar construye una intuición que las celdas en el cuaderno
no siempre proporcionan. Los estudiantes que hojean el JSON suelen notar:

1. La firma es una cadena opaca base64url, pero todos los demás campos son JSON legible
   plano. La firma no encripta el contenido; lo certifica.
2. El `public_key` está incrustado en el recibo, lo que hace que el archivo sea
   autocontenido, pero no es contra lo que un auditor verifica. Compare
   `02_tampered_receipt.json` con `04_resigned_receipt.json`: ambos fueron
   alterados después de firmar, pero el segundo fue firmado de nuevo con la clave
   propia del atacante, por lo que verifica contra la clave que lleva. La clave incrustada
   indica que el archivo es internamente consistente. Solo una clave obtenida
   en otro lugar indica quién lo emitió.
3. Modificar un solo carácter de cualquier campo fuera de `signature`, luego
   volver a comparar este archivo con `02_tampered_receipt.json`, hace
   concreto el mecanismo a nivel de bytes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->