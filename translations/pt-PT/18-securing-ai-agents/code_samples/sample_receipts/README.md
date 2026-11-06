# Exemplos de Recibos

Três ficheiros de recibo pré-gerados para inspeção sem necessitar de correr o notebook.

| Ficheiro | O que é |
|---|---|
| `01_valid_receipt.json` | Um recibo válido assinado para uma chamada da ferramenta `lookup_flights`. A verificação retorna True. |
| `02_tampered_receipt.json` | O mesmo recibo com um campo modificado após a assinatura. A verificação retorna False. |
| `03_chain_three_receipts.json` | Uma cadeia de três recibos válidos (search, hold, book) com `previous_receipt_hash` a ligar cada um ao anterior. |

Os exemplos assinam diretamente os bytes JCS canónicos do conteúdo com Ed25519.
O SHA-256 continua a ser usado para digerir conteúdo e ligações de cadeias de recibos, não como um
pré-hash adicional antes da assinatura.

## Verificar os exemplos

Em `18-signed-receipts.ipynb`, execute primeiro Setup e as Secções 1 a 3.
A Secção 3 define `verify_chain`; só as Secções 1 e 2 não são suficientes.
Depois execute o bloco seguinte numa nova célula, com o diretório de trabalho do notebook
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

### Verificar o exemplo sem Jupyter

A partir da raiz do repositório, instale as dependências da lição e execute:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Estes testes executam os exemplos Python do notebook e o bloco exato do README
acima. Também verificam que adulterações e chaves não fixadas são rejeitadas pelos
verificadores. Os testes saltam a célula de configuração `%pip` do notebook pois as dependências
são instaladas separadamente. Não alteram o notebook nem os exemplos.

## Como estes foram gerados

Os exemplos utilizam o mesmo caminho de código que o notebook, com uma chave de assinatura fixa
e marcas temporais fixas para reprodutibilidade em bytes. Para regenerar:

```bash
python3 generate_fixtures.py
```

(O script está em `generate_fixtures.py` neste diretório.)

## O que os alunos aprendem ao inspecionar JSON cru

Ler o formato cru do recibo constrói uma intuição que as células no notebook
nem sempre proporcionam. Alunos que examinam o JSON frequentemente notam:

1. A assinatura é uma cadeia opaca base64url, mas todos os outros campos são JSON legível
   simples. A assinatura não encripta o conteúdo; atesta-o.
2. O `public_key` está embutido no recibo, o que é suficiente para verificar
   a auto-consistência mas não a confiança no emissor. Um auditor deve compará-lo com uma chave
   fixada fora do recibo ou resolvida através de um registo confiável.
3. Modificar um único caractere de qualquer campo, depois re-comparar este ficheiro com
   `02_tampered_receipt.json`, torna o mecanismo a nível de bytes concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->