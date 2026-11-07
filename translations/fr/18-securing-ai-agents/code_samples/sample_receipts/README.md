# Exemples de Reçus

Quatre fichiers de reçus pré-générés pour inspection sans exécuter le notebook.

| Fichier | Ce que c'est |
|---|---|
| `01_valid_receipt.json` | Un reçu valide signé pour un appel d'outil `lookup_flights`. La vérification retourne True. |
| `02_tampered_receipt.json` | Le même reçu avec un champ modifié après signature. La vérification retourne False. |
| `03_chain_three_receipts.json` | Une chaîne de trois reçus valides (search, hold, book) avec `previous_receipt_hash` reliant chacun à celui d'avant. |
| `04_resigned_receipt.json` | Le même reçu altéré puis re-signé par un attaquant, avec la clé publique de l'attaquant intégrée. Vérifie avec la clé qu'il contient. Échoue avec la clé de l'émetteur. |

Les exemples signent directement les octets JCS canoniques de la charge utile avec Ed25519.
SHA-256 reste utilisé pour les condensats de contenu et les liens de la chaîne de reçus, pas comme un
préhachage supplémentaire avant la signature.

## Vérification des exemples

Dans `18-signed-receipts.ipynb`, exécutez d'abord Setup et les Sections 1 à 3.
La Section 3 définit `verify_chain` ; les Sections 1 et 2 seules ne suffisent pas.
Ensuite, exécutez le bloc suivant dans une nouvelle cellule, avec le répertoire de travail du notebook
réglé sur `18-securing-ai-agents/code_samples`. Les chemins des exemples ci-dessous sont relatifs
à ce répertoire.

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

### Vérification de l'exemple sans Jupyter

Depuis la racine du dépôt, installez les dépendances de la leçon et exécutez :

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ces tests exécutent les exemples Python du notebook et le bloc README exact
ci-dessus. Ils vérifient aussi que la falsification et les clés non épinglées sont rejetées par les
vérificateurs. Les tests sautent la cellule de configuration `%pip` du notebook car les dépendances
sont installées séparément. Ils ne modifient ni le notebook ni les exemples.

## Comment ces fichiers ont été générés

Les exemples utilisent le même chemin de code que le notebook, avec une clé de signature fixe
et des horodatages fixes pour la reproductibilité des octets. Pour régénérer :

```bash
python3 generate_fixtures.py
```

(Le script est dans `generate_fixtures.py` dans ce répertoire.)

`../test_signed_receipts.py` vérifie tout cela automatiquement : il exécute le
le code du carnet, vérifie ces quatre fixtures avec le carnet
`verify_receipt` et `verify_chain`, et confirme que la régénération des
fixtures donne des octets identiques. Extrait de `code_samples` :

```bash
python -m unittest test_signed_receipts
```

## Ce que les étudiants apprennent en inspectant le JSON brut

La lecture du format brut du reçu construit une intuition que les cellules du carnet
ne fournissent pas toujours. Les étudiants qui survolent le JSON remarquent souvent :

1. La signature est une chaîne opaque en base64url, mais tous les autres champs sont du JSON
   lisible en clair. La signature n’encrypte pas le contenu ; elle l’atteste.
2. Le `public_key` est incorporé dans le reçu, ce qui rend le fichier
   autonome mais ce n’est pas ce que vérifie un auditeur. Comparez
   `02_tampered_receipt.json` avec `04_resigned_receipt.json` : les deux ont été
   modifiés après la signature, mais le second a été re-signé avec la
   clé de l’attaquant, donc il vérifie avec la clé qu’il contient. La clé
   incorporée indique que le fichier est cohérent en interne. Seule une clé
   obtenue ailleurs vous dit qui l’a émise.
3. Modifier un seul caractère de n’importe quel champ en dehors de `signature`, puis
   re-comparer ce fichier avec `02_tampered_receipt.json`, concrétise le
   mécanisme au niveau des octets.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->