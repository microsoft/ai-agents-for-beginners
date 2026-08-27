# Fixtures de Recibo de Exemplo

Três arquivos de recibo pré-gerados para inspeção sem precisar rodar o notebook.

| Arquivo | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo válido assinado para uma chamada da ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` linkando cada um ao anterior. |

As fixtures assinam diretamente os bytes canônicos JCS do payload com Ed25519.
SHA-256 continua em uso para digeridos de conteúdo e links da cadeia de recibos, não como
um pré-hash extra antes da assinatura.

## Verificando as amostras

O notebook orienta pela verificação em quatro seções. Para verificar estas fixtures
diretamente sem passar pela narrativa do notebook:

```python
import json
from pathlib import Path

# Assume que você completou as importações e funções auxiliares
# das seções 1 e 2 do 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Verdadeiro

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Como estas foram geradas

As fixtures usam o mesmo caminho de código que o notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade dos bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os estudantes aprendem ao inspecionar o JSON cru

Ler o formato cru do recibo desenvolve intuição que as células do notebook
nem sempre fornecem. Estudantes que examinam o JSON frequentemente notam:

1. A assinatura é uma string opaca base64url, mas todos os outros campos são JSON legíveis
   e claros. A assinatura não criptografa o conteúdo; ela o atesta.
2. A `public_key` está embutida no recibo. Um auditor não precisa de mais nada
   para verificar (sujeito à confiança de que a chave realmente pertence ao emissor alegado;
   veja o README da lição sobre infraestrutura de identidade).
3. Modificar um único caractere de qualquer campo, e então comparar novamente este arquivo com
   `02_tampered_receipt.json`, torna o mecanismo ao nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->