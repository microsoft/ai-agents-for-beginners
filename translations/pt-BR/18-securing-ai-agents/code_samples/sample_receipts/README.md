# Exemplos de Recibos

Três arquivos de recibos pré-gerados para inspeção sem executar o notebook.

| Arquivo | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo assinado válido para uma chamada de ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` ligando cada um ao anterior. |

Os exemplos assinam diretamente os bytes canônicos JCS da carga útil com Ed25519.
SHA-256 permanece em uso para resumos de conteúdo e links da cadeia de recibos, não como um
pré-hash extra antes da assinatura.

## Verificando os exemplos

No `18-signed-receipts.ipynb`, execute Primeiro Setup e as Seções de 1 a 3.
A Seção 3 define `verify_chain`; apenas as Seções 1 e 2 não são suficientes.
Em seguida, execute o bloco abaixo em uma nova célula, com o diretório de trabalho do notebook
definido para `18-securing-ai-agents/code_samples`. Os caminhos dos exemplos abaixo são relativos
a esse diretório.

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

### Verificando o exemplo sem Jupyter

A partir da raiz do repositório, instale as dependências da lição e execute:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Esses testes executam os exemplos de Python do notebook e o mesmo bloco exato do README
acima. Eles também verificam que manipulações e chaves não fixadas são rejeitadas pelos
verificadores. Os testes pulam a célula de configuração `%pip` do notebook porque as dependências
são instaladas separadamente. Eles não alteram o notebook ou os exemplos.

## Como estes foram gerados

Os exemplos usam o mesmo caminho de código do notebook, com uma chave de assinatura fixa
e timestamps fixos para reprodutibilidade de bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os estudantes aprendem ao inspecionar JSON bruto

Ler o formato bruto do recibo constrói uma intuição que as células no notebook
nem sempre oferecem. Estudantes que examinam o JSON frequentemente notam:

1. A assinatura é uma string opaca base64url, mas todo outro campo é JSON
   legível simples. A assinatura não criptografa o conteúdo; ela atesta para ele.
2. O `public_key` está embutido no recibo, o que é suficiente para checar
   a auto-consistência mas não a confiança no emissor. Um auditor deve compará-lo com uma chave
   fixada fora do recibo ou resolvida através de um registro confiável.
3. Modificar um único caractere de qualquer campo, e então recomparar este arquivo com
   `02_tampered_receipt.json`, torna o mecanismo a nível de byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->