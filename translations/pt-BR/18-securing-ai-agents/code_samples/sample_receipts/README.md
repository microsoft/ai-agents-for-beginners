# Exemplos de Recibos

Três arquivos de recibos pré-gerados para inspeção sem executar o notebook.

| Arquivo | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo assinado válido para uma chamada da ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (busca, reserva temporária, reserva) com `previous_receipt_hash` ligando cada um ao anterior. |

Os exemplos assinam diretamente os bytes canônicos JCS da carga útil com Ed25519.
SHA-256 continua sendo usado para digerir conteúdos e links da cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificando os exemplos

O notebook explica a verificação em quatro seções. Para verificar esses exemplos
diretamente sem passar pela narrativa do notebook:

```python
import json
from pathlib import Path

# Assume que você completou as importações e as funções auxiliares
# das seções 1 e 2 do 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Verdadeiro

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Como estes foram gerados

Os exemplos usam o mesmo caminho de código do notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os estudantes aprendem ao inspecionar o JSON bruto

Ler o formato bruto do recibo constrói uma intuição que as células no notebook
nem sempre proporcionam. Estudantes que examinam o JSON frequentemente percebem:

1. A assinatura é uma string opaca base64url, mas todo outro campo é um JSON
   legível simples. A assinatura não criptografa o conteúdo; ela o atesta.
2. A `public_key` está embutida no recibo. Um auditor não precisa de mais nada
   para verificar (sujeito a confiar que a chave realmente pertence ao emissor
   declarado; veja o README da lição sobre infraestrutura de identidade).
3. Modificar um único caractere de qualquer campo, e então comparar este arquivo com
   `02_tampered_receipt.json`, torna o mecanismo em nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->