# Exemplos de Recibos

Três ficheiros de recibos pré-gerados para inspeção sem executar o notebook.

| Ficheiro | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo assinado válido para uma chamada à ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (pesquisa, reserva temporária, reserva) com `previous_receipt_hash` a ligar cada um ao anterior. |

Os exemplos assinam diretamente os bytes canónicos JCS da carga útil com Ed25519.
O SHA-256 mantém-se em uso para digests de conteúdo e ligações na cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificar os exemplos

O notebook explica a verificação em quatro secções. Para verificar estes exemplos
diretamente sem passar pela narrativa do notebook:

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

## Como estes foram gerados

Os exemplos usam o mesmo caminho de código que o notebook, com uma chave de assinatura fixa
e carimbos de data/hora fixos para reprodutibilidade dos bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os estudantes aprendem ao inspecionar JSON bruto

Ler o formato bruto do recibo constrói intuição que as células no notebook
nem sempre proporcionam. Estudantes que olham rapidamente para o JSON geralmente notam:

1. A assinatura é uma string opaca em base64url, mas todos os outros campos são JSON
   legíveis em texto simples. A assinatura não encripta o conteúdo; atesta-o.
2. A `public_key` está embutida no recibo. Um auditor não precisa de mais nada
   para verificar (sujeito a confiar que a chave pertence realmente ao emissor reivindicado;
   veja o README da lição sobre infraestrutura de identidade).
3. Modificar um único carácter de qualquer campo e depois comparar este ficheiro com
   `02_tampered_receipt.json` torna o mecanismo ao nível dos bytes concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->