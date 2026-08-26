# Exemples de Reçus

Trois fichiers de reçus pré-générés pour inspection sans exécuter le notebook.

| Fichier | Qu'est-ce que c'est |
|---|---|
| `01_valid_receipt.json` | Un reçu signé valide pour un appel à l'outil `lookup_flights`. La vérification retourne True. |
| `02_tampered_receipt.json` | Le même reçu avec un champ modifié après signature. La vérification retourne False. |
| `03_chain_three_receipts.json` | Une chaîne de trois reçus valides (recherche, réservation temporaire, réservation) avec `previous_receipt_hash` reliant chaque reçu au précédent. |

Les exemples signent directement les octets canoniques JCS de la charge utile avec Ed25519.
SHA-256 reste utilisé pour les condensats de contenu et les liens de chaîne de reçus, pas comme un 
pré-hachage supplémentaire avant la signature.

## Vérification des exemples

Le notebook explique la vérification en quatre sections. Pour vérifier ces exemples
directement sans passer par la narration du notebook :

```python
import json
from pathlib import Path

# Suppose que vous avez terminé les imports et les fonctions d'aide
# des sections 1 et 2 de 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Vrai

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Faux

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Comment ces exemples ont été générés

Les exemples utilisent le même chemin de code que le notebook, avec une clé de signature fixe
et des horodatages fixes pour la reproductibilité des octets. Pour régénérer :

```bash
python3 generate_fixtures.py
```

(Le script est dans `generate_fixtures.py` dans ce répertoire.)

## Ce que les étudiants apprennent en inspectant le JSON brut

Lire le format brut du reçu développe une intuition que les cellules du notebook
n'offrent pas toujours. Les étudiants qui parcourent rapidement le JSON remarquent souvent :

1. La signature est une chaîne opaque en base64url, mais tous les autres champs sont du JSON lisible
   ordinaire. La signature ne chiffre pas le contenu ; elle l'atteste.
2. La `public_key` est intégrée dans le reçu. Un auditeur n'a besoin de rien d'autre
   pour vérifier (à condition de faire confiance que la clé appartient bien à l'émetteur
   revendiqué ; voir le README de la leçon sur l'infrastructure d'identité).
3. Modifier un seul caractère de n'importe quel champ, puis comparer ce fichier avec
   `02_tampered_receipt.json`, rend le mécanisme au niveau octet concret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->