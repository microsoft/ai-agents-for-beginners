# Exemplos de Recibos

Três ficheiros de recibos pré-gerados para inspeção sem a necessidade de executar o notebook.

| Ficheiro | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo assinado válido para uma chamada à ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` a ligar cada um ao anterior. |

Os exemplos assinam directamente os bytes canónicos JCS do payload com Ed25519.
O SHA-256 continua a ser usado para digerir conteúdos e ligações na cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificação dos exemplos

O notebook percorre a verificação em quatro secções. Para verificar estes exemplos
directamente, sem passar pela narrativa do notebook:

```python
import json
from pathlib import Path

# Assume que completou as importações e funções auxiliares
# das secções 1 e 2 do 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Verdadeiro

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Como foram gerados

Os exemplos usam o mesmo percurso de código do notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade byte-a-byte. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os alunos aprendem ao inspecionar JSON bruto

Ler o formato bruto do recibo cria intuição que as células do notebook
por vezes não fornecem. Alunos que olham de relance para o JSON frequentemente notam:

1. A assinatura é uma string opaca base64url, mas todos os outros campos são JSON simples e
   legíveis. A assinatura não encripta o conteúdo; atesta-o.
2. A `public_key` está embutida no recibo. Um auditor não precisa de mais nada
   para verificar (desde que confie que a chave realmente pertence ao
   emissor alegado; veja o README da lição sobre infraestruturas de identidade).
3. Modificar um único carácter de qualquer campo e depois comparar novamente este ficheiro com
   `02_tampered_receipt.json` torna o mecanismo ao nível dos bytes concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->