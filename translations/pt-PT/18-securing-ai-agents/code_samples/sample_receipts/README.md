# Exemplos de Recibos

Quatro ficheiros de recibos pré-gerados para inspeção sem necessitar de executar o notebook.

| Ficheiro | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo válido assinado para uma chamada de ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` a ligar cada um ao anterior. |
| `04_resigned_receipt.json` | O mesmo recibo adulterado e depois re-assinado por um atacante, com a chave pública do atacante embutida. Verifica contra a chave nele contida. Falha contra a chave do emissor. |

Os exemplos assinam os bytes canónicos JCS do payload diretamente com Ed25519.
O SHA-256 continua a ser utilizado para resumos de conteúdo e ligações da cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificação dos exemplos

Em `18-signed-receipts.ipynb`, execute primeiro Setup e as Secções 1 até 3.
A Secção 3 define `verify_chain`; as Secções 1 e 2 sozinhas não são suficientes.
Depois execute o bloco seguinte numa nova célula, com o diretório de trabalho do notebook
definido para `18-securing-ai-agents/code_samples`. Os caminhos dos exemplos abaixo são relativos
a esse diretório.

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

### Verificar o exemplo sem Jupyter

A partir da raiz do repositório, instale as dependências da lição e execute:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Estes testes executam os exemplos Python do notebook e o bloco exato do README
acima. Também verificam que adulterações e chaves não fixadas são rejeitadas pelos
verificadores. Os testes ignoram a célula de configuração `%pip` do notebook porque as dependências
são instaladas separadamente. Eles não alteram o notebook nem os exemplos.

## Como estes foram gerados

Os exemplos usam o mesmo caminho de código do notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

`../test_signed_receipts.py` verifica tudo isto automaticamente: executa o
código do notebook, verifica estes quatro exemplos com os
`verify_receipt` e `verify_chain` do notebook, e confirma que regenerar os
exemplos produz bytes idênticos. A partir de `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## O que os estudantes aprendem ao inspecionar JSON cru

Ler o formato cru do recibo desenvolve uma intuição que as células do notebook
nem sempre oferecem. Estudantes que espreitam o JSON frequentemente notam:

1. A assinatura é uma string opaca em base64url, mas todos os outros campos são JSON
   legível simples. A assinatura não encripta o conteúdo; ela atesta o conteúdo.
2. O `public_key` está embutido no recibo, o que torna o ficheiro
   autónomo, mas não é contra o que um auditor verifica. Compare
   `02_tampered_receipt.json` com `04_resigned_receipt.json`: ambos foram
   alterados após a assinatura, mas o segundo foi re-assinado com a
   chave do atacante, pelo que verifica contra a chave que transporta. A chave embutida
   indica que o ficheiro é internamente consistente. Só uma chave obtida
   noutro local indica quem o emitiu.
3. Modificar um único carácter de qualquer campo fora do `signature`, depois
   voltar a comparar este ficheiro com `02_tampered_receipt.json`, torna o
   mecanismo ao nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->