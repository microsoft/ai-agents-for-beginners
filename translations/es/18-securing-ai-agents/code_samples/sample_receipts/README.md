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

En `18-signed-receipts.ipynb`, ejecuta primero Setup y las Secciones 1 a 3.
La Sección 3 define `verify_chain`; las Secciones 1 y 2 por sí solas no son suficientes.
Luego ejecuta el siguiente bloque en una nueva celda, con el directorio de trabajo del cuaderno
configurado en `18-securing-ai-agents/code_samples`. Las rutas de los fixtures a continuación son relativas
a ese directorio.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Comprobando el ejemplo sin Jupyter

Desde la raíz del repositorio, instala las dependencias de la lección y ejecuta:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Estas pruebas ejecutan los ejemplos de Python del cuaderno y el bloque exacto del README
anterior. También verifican que las manipulaciones y las claves no ancladas sean rechazadas por los
verificadores. Las pruebas omiten la celda de configuración `%pip` del cuaderno porque las dependencias
se instalan por separado. No cambian el cuaderno ni los fixtures.

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
   en texto plano. La firma no encripta el contenido; lo certifica.
2. El `public_key` está incrustado en el recibo, lo cual es suficiente para verificar
   la autoconsistencia pero no la confianza del emisor. Un auditor debe compararlo con una clave
   fijada fuera del recibo o resuelta mediante un registro confiable.
3. Modificar un solo carácter de cualquier campo, y luego volver a comparar este archivo con
   `02_tampered_receipt.json`, hace que el mecanismo a nivel de bytes sea tangible.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->