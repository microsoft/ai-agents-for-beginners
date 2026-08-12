# Modelos de Recibos de Exemplo

Três arquivos de recibo pré-gerados para inspeção sem precisar rodar o notebook.

| Arquivo | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo assinado válido para uma chamada da ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` ligando cada um ao anterior. |

## Verificando os exemplos

O notebook conduz a verificação em quatro seções. Para verificar esses modelos
diretamente, sem seguir a narrativa do notebook:

```python
import json
from pathlib import Path

# Assume que você tenha completado as importações e funções auxiliares
# das seções 1 e 2 de 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Verdadeiro

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Como eles foram gerados

Os modelos usam o mesmo caminho de código do notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os estudantes aprendem ao inspecionar o JSON bruto

Ler o formato bruto do recibo constrói uma intuição que as células do notebook
nem sempre proporcionam. Estudantes que examinam o JSON frequentemente percebem:

1. A assinatura é uma string opaca base64url, mas todos os outros campos são JSON legíveis
   diretamente. A assinatura não encripta o conteúdo; ela o atesta.
2. A `public_key` está embutida no recibo. Um auditor não precisa de mais nada
   para verificar (desde que confie que a chave realmente pertence ao emissor
   alegado; veja o README da lição sobre infraestrutura de identidade).
3. Modificar um único caractere de qualquer campo, e então re-comparar esse arquivo com
   o `02_tampered_receipt.json`, torna o mecanismo a nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->