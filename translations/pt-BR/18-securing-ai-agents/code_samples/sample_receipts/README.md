# Exemplos de Recibos

Quatro arquivos de recibo pré-gerados para inspeção sem executar o notebook.

| Arquivo | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo válido assinado para uma chamada de ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo alterado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` conectando cada um ao anterior. |
| `04_resigned_receipt.json` | O mesmo recibo adulterado e então re-assinado por um atacante, com a chave pública do atacante embutida. Verifica contra a chave dentro dele. Falha contra a chave do emissor. |

Os exemplos assinam diretamente os bytes canônicos JCS da carga útil com Ed25519.
SHA-256 continua sendo usado para digests de conteúdo e links da cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificando os exemplos

Em `18-signed-receipts.ipynb`, execute primeiro Setup e as Seções 1 a 3.
A Seção 3 define `verify_chain`; apenas Seções 1 e 2 não são suficientes.
Depois execute o bloco a seguir em uma nova célula, com o diretório de trabalho do notebook
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

### Verificando o exemplo sem Jupyter

A partir da raiz do repositório, instale as dependências da lição e execute:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Esses testes executam os exemplos em Python do notebook e o mesmo bloco do README
acima. Eles também verificam que adulterações e chaves não fixadas são rejeitadas pelos
validadores. Os testes ignoram a célula de configuração `%pip` do notebook porque as dependências
são instaladas separadamente. Eles não alteram o notebook ou os exemplos.

## Como esses foram gerados

Os exemplos usam o mesmo caminho de código do notebook, com uma chave fixa de assinatura
e timestamps fixos para reprodutibilidade de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

`../test_signed_receipts.py` verifica tudo isso automaticamente: ele executa o
código do notebook, verifica esses quatro exemplos com o
`verify_receipt` e `verify_chain` do notebook, e confirma que regenerar os
exemplos dá bytes idênticos. De `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## O que os estudantes aprendem ao inspecionar JSON bruto

Ler o formato bruto do recibo desenvolve a intuição que as células no notebook
nem sempre fornecem. Estudantes que folheiam o JSON frequentemente notam:

1. A assinatura é uma string opaca base64url, mas todo outro campo é JSON legível
   e simples. A assinatura não criptografa o conteúdo; ela atesta.
2. O `public_key` está embutido no recibo, o que torna o arquivo
   autocontido, mas não é contra o qual um auditor verifica. Compare
   `02_tampered_receipt.json` com `04_resigned_receipt.json`: ambos foram
   alterados após a assinatura, mas o segundo foi re-assinado com a própria
   chave do atacante, então ele verifica contra a chave que carrega. A chave embutida
   indica que o arquivo é internamente consistente. Apenas uma chave obtida
   externamente indica quem o emitiu.
3. Modificar um único caractere de qualquer campo fora de `signature`, e então
   comparar novamente este arquivo com `02_tampered_receipt.json`, torna o
   mecanismo a nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->