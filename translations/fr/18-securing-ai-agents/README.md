[Regardez la vidéo de la leçon : Sécuriser les agents IA avec des reçus cryptographiques](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Vidéo de la leçon et miniature à ajouter par l’équipe contenu Microsoft après fusion, suivant le modèle des leçons 14 / 15.)_

# Sécuriser les agents IA avec des reçus cryptographiques

## Introduction

Cette leçon couvrira :

- Pourquoi les pistes d’audit pour les agents IA sont importantes pour la conformité, le débogage, et la confiance.
- Ce qu’est un reçu cryptographique et en quoi il diffère d’une ligne de journal non signée.
- Comment produire un reçu signé pour un appel d’outil d’un agent en Python simple.
- Comment vérifier un reçu hors ligne et détecter toute falsification.
- Comment enchaîner les reçus pour que la suppression ou le réarrangement d’un reçu casse la chaîne.
- Ce que les reçus prouvent et ce qu’ils ne prouvent explicitement pas.

## Objectifs d’apprentissage

Après avoir complété cette leçon, vous saurez comment :

- Identifier les modes de défaillance qui motivent la provenance cryptographique des actions de l’agent.
- Produire un reçu signé Ed25519 sur une charge utile JSON canonique.
- Vérifier un reçu indépendamment en utilisant uniquement la clé publique du signataire.
- Détecter une falsification en relançant la vérification sur un reçu modifié.
- Construire une séquence de reçus enchaînés par hachage et expliquer pourquoi la chaîne est importante.
- Reconnaître la limite entre ce que les reçus prouvent (attribution, intégrité, ordre) et ce qu’ils ne prouvent pas (correction de l’action, solidité de la politique).

## Le problème : la piste d’audit de votre agent

Imaginez que vous ayez déployé un agent IA pour Contoso Travel. L’agent lit les demandes des clients, appelle une API de vols pour rechercher des options, et réserve des sièges pour le client. Le trimestre dernier, l’agent a traité 50 000 réservations.

Aujourd’hui, un auditeur arrive. Il pose une question simple : « Montrez-moi ce que votre agent a fait. »

Vous lui remettez vos fichiers journaux. L’auditeur les examine puis pose une question plus difficile : « Comment savoir que ces journaux n’ont pas été modifiés ? »

C’est le problème de la piste d’audit. La plupart des déploiements actuels d’agents s’appuient sur :

- **Journaux d’application** : écrits par l’agent lui-même, modifiables par quiconque a accès au système de fichiers.
- **Services de journalisation cloud** : à preuve de falsification au niveau de la plateforme, mais seulement si l’auditeur fait confiance à l’opérateur plateforme.
- **Journaux de transactions de base de données** : adaptés aux modifications de base de données mais pas aux appels d’outils arbitraires.

Aucun de ces systèmes ne peut répondre à la question de l’auditeur sans que l’auditeur ait à faire confiance à quelqu’un (vous, votre fournisseur cloud, votre fournisseur de base de données). Pour un usage interne, cette confiance est souvent acceptable. Pour les charges réglementées (finance, santé, tout ce qui relève du règlement européen sur l’IA), elle ne l’est pas.

Les reçus cryptographiques règlent ce problème en rendant chaque action de l’agent vérifiable indépendamment. L’auditeur n’a pas besoin de vous faire confiance. Il a seulement besoin de votre clé publique et du reçu lui-même.

## Qu’est-ce qu’un reçu cryptographique ?

Un reçu est un objet JSON qui enregistre ce qu’un agent a fait, signé par une signature numérique.

```mermaid
flowchart LR
    A[Un agent invoque un outil] --> B[Construire la charge utile du reçu]
    B --> C[Canonicaliser JSON RFC 8785]
    C --> D[Hachage SHA-256]
    D --> E[Signature Ed25519]
    E --> F[Reçu avec signature]
    F --> G[L’auditeur vérifie hors ligne]
    G --> H{Signature valide ?}
    H -- oui --> I[Preuve anti-falsification]
    H -- non --> J[Reçu rejeté]
```

Un reçu minimal ressemble à ceci :

```json
{
  "type": "agent.tool_call.v1",
  "agent_id": "contoso-travel-bot",
  "tool_name": "lookup_flights",
  "tool_args_hash": "sha256:a3f9c1...",
  "result_hash": "sha256:7b2e1d...",
  "policy_id": "contoso-travel-policy-v3",
  "timestamp": "2026-04-25T14:30:00Z",
  "sequence": 47,
  "previous_receipt_hash": "sha256:9d4e6a...",
  "signature": {
    "alg": "EdDSA",
    "sig": "c5af83...",
    "public_key": "8f3b2c..."
  }
}
```

Trois propriétés font le travail :

1. **La signature**. Le reçu est signé par la passerelle de l’agent via une clé privée Ed25519. Toute personne possédant la clé publique correspondante peut vérifier la signature hors ligne. Toute modification d’un champ rend la signature invalide.

2. **Encodage canonique**. Avant la signature, le reçu est sérialisé selon le JSON Canonicalization Scheme (JCS, RFC 8785). Cela garantit que deux implémentations produisant un même reçu logique génèrent une sortie identique octet par octet. Sans canonisation, différents sérialiseurs JSON produiraient des signatures différentes pour le même contenu.

3. **Chaînage par hachage**. Le champ `previous_receipt_hash` relie chaque reçu au précédent. Supprimer ou réordonner un reçu casse tous les reçus qui le suivent. La falsification devient visible au niveau de la chaîne, même si on contournait les signatures individuelles.

Ensemble, ces propriétés fournissent trois garanties :

- **Attribution** : cette clé a signé ce contenu.
- **Intégrité** : le contenu n’a pas changé depuis la signature.
- **Ordre** : ce reçu est postérieur à ce reçu dans la chaîne.

## Produire un reçu en Python

Vous n’avez pas besoin d’une bibliothèque spéciale pour produire un reçu. Les primitives cryptographiques sont largement disponibles et la logique tient en quelques dizaines de lignes de Python.

Les exercices pratiques dans `code_samples/18-signed-receipts.ipynb` parcourent tout le processus. La version résumée :

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # JSON canonique RFC 8785

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# Générer ou charger une clé de signature (en production, stocker dans un coffre à clés)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# Construire la charge utile du reçu (pas encore de signature)
tool_args = {"origin": "SYD", "destination": "LAX"}
tool_result = [{"flight": "QF11", "price": 1850, "stops": 0}]

payload = {
    "type": "agent.tool_call.v1",
    "agent_id": "contoso-travel-bot",
    "tool_name": "lookup_flights",
    "tool_args_hash": sha256_canonical(tool_args),
    "result_hash": sha256_canonical(tool_result),
    "policy_id": "contoso-travel-policy-v3",
    "timestamp": "2026-04-25T14:30:00Z",
    "sequence": 0,
    "previous_receipt_hash": None,
}

# Canoniquer, hacher, signer.
canonical_bytes = canonicalize(payload)
message_hash = hashlib.sha256(canonical_bytes).digest()
signature_bytes = signing_key.sign(message_hash).signature

# Joindre un objet de signature structuré.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```

C’est tout le pipeline de signature. Les exercices dans le notebook vous guident à chaque étape.

## Vérifier un reçu et détecter une falsification

La vérification est l’opération inverse :

```python
import base64
import hashlib
from nacl import signing
from nacl.exceptions import BadSignatureError
from jcs import canonicalize

def b64url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode(s + padding)

def verify_receipt(receipt: dict) -> bool:
    # La signature est un objet structuré : {"alg", "sig", "public_key"}.
    sig_obj = receipt.get("signature")
    if not sig_obj or sig_obj.get("alg") != "EdDSA":
        return False

    # Reconstruire la charge utile qui a réellement été signée (tout sauf la signature).
    payload = {k: v for k, v in receipt.items() if k != "signature"}

    canonical_bytes = canonicalize(payload)
    message_hash = hashlib.sha256(canonical_bytes).digest()

    try:
        verify_key = signing.VerifyKey(b64url_decode(sig_obj["public_key"]))
        verify_key.verify(message_hash, b64url_decode(sig_obj["sig"]))
        return True
    except BadSignatureError:
        return False
```

Cette fonction prend un reçu et retourne `True` si la signature est valide, `False` sinon. Pas d’appel réseau, pas de dépendance à un service, aucune confiance requise envers un tiers.

Pour voir la détection de falsification en action, le notebook parcourt :

1. Produire un reçu valide et confirmer qu’il se vérifie.
2. Modifier un octet du champ `tool_args_hash`.
3. Relancer la vérification et constater l’échec.

C’est la démonstration pratique que les reçus sont à preuve de falsification : toute modification, même minime, casse la signature.

## Enchaîner les reçus pour les agents multi-étapes

Un reçu signé protège une action. Une chaîne de reçus protège une séquence.

```mermaid
flowchart LR
    R0[Reçu 0<br/>genèse] --> R1[Reçu 1]
    R1 --> R2[Reçu 2]
    R2 --> R3[Reçu 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

Chaque reçu enregistre le hachage du reçu précédent. Pour supprimer silencieusement le reçu 2, un attaquant devrait soit :

- Modifier le champ `previous_receipt_hash` du reçu 3 (ce qui casse la signature du reçu 3), OU
- Forger une nouvelle signature sur un reçu 3 modifié (ce qui nécessite la clé privée de l’agent).

Si la clé privée est stockée dans un coffre matériel et que vous publiez la clé publique avec chaque reçu, aucune de ces attaques n’est réalisable sans être détectée.

Le notebook fait voir :

1. La construction d’une chaîne de trois reçus.
2. La vérification que le `previous_receipt_hash` de chaque reçu correspond bien au hachage effectif du reçu précédent.
3. La falsification d’un reçu intermédiaire et l’observation de la rupture de la chaîne à cet endroit précis.

C’est ainsi que vous produisez une piste d’audit qu’un auditeur externe peut vérifier sans vous faire confiance.

## Ce que les reçus prouvent (et ce qu’ils ne prouvent pas)

C’est la section la plus importante de cette leçon. Les reçus sont puissants mais leur puissance est limitée.

**Les reçus prouvent trois choses :**

1. **Attribution** : une clé spécifique a signé une charge utile spécifique.
2. **Intégrité** : la charge utile n’a pas changé depuis la signature.
3. **Ordre** : ce reçu est postérieur à ce reçu dans la chaîne de hachage.

**Les reçus ne prouvent PAS :**

1. **Exactitude** : que l’action de l’agent était la bonne action. Un reçu peut être signé pour une mauvaise réponse aussi proprement que pour une bonne.
2. **Conformité à la politique** : que la politique référencée dans `policy_id` a effectivement été évaluée, ou qu’elle aurait permis cette action si elle avait été vérifiée. Le reçu enregistre ce qui a été revendiqué, pas ce qui a été appliqué.
3. **Identité au-delà de la clé** : le reçu dit « cette clé a signé ce contenu. » Il ne dit pas « cet humain a autorisé cela. » Relier une clé à une personne ou organisation exige une infrastructure d’identité distincte (un annuaire, un registre de clés publiques, etc.).
4. **Véracité des entrées** : si l’agent reçoit un prompt manipulé et agit en conséquence, le reçu enregistre fidèlement l’action. Les reçus sont en aval de la validation des entrées, pas un substitut.

Cette limite est importante pour deux raisons :

- Elle dit à quoi les reçus servent : rendre le comportement d’un agent auditable et à preuve de falsification, même entre différentes organisations.
- Elle dit quelles couches supplémentaires vous avez encore besoin : validation des entrées (Leçon 6), application de politiques (voir ci-dessous brièvement), infrastructure d’identité (hors de portée de cette leçon).

Une erreur courante est de supposer que « nous avons des reçus » signifie « nous sommes gouvernés ». Ce n’est pas le cas. Les reçus sont une fondation. La gouvernance est le système que vous construisez dessus.

## Références de production

Le code Python de cette leçon est volontairement minimal pour que vous puissiez lire chaque ligne et comprendre précisément ce qui se passe. En production, vous avez deux options :

1. **Construire directement sur les primitives cryptographiques.** Les 50 lignes vues plus haut suffisent pour de nombreux cas d’usage. PyNaCl (Ed25519) et le paquet `jcs` (JSON canonique) sont des bibliothèques bien maintenues et auditées.

2. **Utiliser une bibliothèque de reçus en production.** Plusieurs projets open source implémentent le même pattern avec des fonctionnalités supplémentaires (rotation de clés, vérification par lots, distribution JWK Set, intégration aux moteurs de politiques) :
   - Le format de reçu utilisé dans cette leçon suit un Internet-Draft IETF (`draft-farley-acta-signed-receipts`) actuellement en cours de normalisation.
   - Le Microsoft Agent Governance Toolkit compose des reçus avec des décisions politiques basées sur Cedar ; voir le Tutoriel 33 dans ce dépôt pour un exemple complet.
   - Les paquets `protect-mcp` (npm) et `@veritasacta/verify` (npm) fournissent une implémentation Node de la signature et vérification hors ligne de reçus, destinés à envelopper tout serveur MCP avec une piste d’audit inviolable.
   - Le SDK Python **[nobulex](https://github.com/arian-gogani/nobulex)** (`pip install nobulex`) fournit le même schéma de signature Ed25519 + JCS en Python avec les intégrations LangChain et CrewAI, incluant des vecteurs de test de validation croisée publiés et une cartographie de conformité contribué via [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210).

La décision entre écrire son propre code ou utiliser une bibliothèque reflète la même décision que pour une bibliothèque JWT : les deux sont valables ; la bibliothèque économise du temps et réduit la surface d’audit ; le développement from-scratch vous force à comprendre chaque primitive. Cette leçon enseigne la voie from-scratch pour vous donner la base pour l’un ou l’autre choix.

## Vérification des connaissances

Testez votre compréhension avant de passer à l’exercice pratique.

**1. Un reçu est signé avec la clé privée Ed25519 de l’agent. L’auditeur ne dispose que de la clé publique. L’auditeur peut-il vérifier le reçu hors ligne ?**

<details>
<summary>Réponse</summary>

Oui. La vérification Ed25519 nécessite uniquement la clé publique et les octets signés. Pas d’appel réseau, pas de dépendance à un service. C’est cette propriété qui rend les reçus utiles dans les environnements cloisonnés, multi-organisation, ou à faible confiance.
</details>

**2. Un attaquant modifie le champ `policy_id` d’un reçu pour prétendre qu’il était gouverné par une politique plus permissive. La signature portait sur la charge utile originale. Que se passe-t-il lors de la vérification ?**

<details>
<summary>Réponse</summary>

La vérification échoue. La signature a été calculée sur les octets canoniques de la charge utile originale ; modifier un champ change ces octets canoniques, ce qui change le hachage SHA-256, ce qui invalide la signature. L’attaquant devrait avoir la clé privée pour produire une nouvelle signature valide, ce qu’il n’a pas.
</details>

**3. Pourquoi le reçu inclut-il un `tool_args_hash` et un `result_hash` plutôt que les arguments bruts et le résultat ?**

<details>
<summary>Réponse</summary>

Deux raisons. Premièrement, le reçu peut devoir être archivé ou transmis dans des environnements où la fuite du contenu brut (Données personnelles, données métier) pose un problème. Le hachage garde le reçu petit et le contenu privé ; l’auditeur vérifie que le hachage correspond à une copie stockée séparément du contenu réel. Deuxièmement, les hachages ont une taille fixe ; un reçu avec des hachages a une taille limitée quel que soit la taille des entrées et sorties.
</details>

**4. Le champ `previous_receipt_hash` relie chaque reçu à son prédécesseur. Si un attaquant supprime silencieusement un reçu au milieu d’une chaîne, qu’est-ce qui devient invalide ?**

<details>
<summary>Réponse</summary>

Tous les reçus qui suivaient celui supprimé. Les champs `previous_receipt_hash` ne correspondent plus à la chaîne réelle (car le reçu référencé n’existe plus, ou la chaîne pointe désormais vers un prédécesseur différent). Pour cacher cette suppression, l’attaquant devrait re-signer tous les reçus suivants, ce qui nécessite la clé privée.
</details>

**5. Un reçu se vérifie proprement. Cela prouve-t-il que l’action de l’agent était correcte, solide, ou conforme à la politique ?**

<details>
<summary>Réponse</summary>

Non. Un reçu valide prouve trois choses : attribution (cette clé a signé ce contenu), intégrité (le contenu n’a pas changé), et ordre (ce reçu est postérieur à ce reçu). Il ne prouve PAS que l’action était correcte, que la politique nommée dans `policy_id` a été effectivement évaluée, ou que l’agent a respecté toutes les règles. Les reçus rendent le comportement de l’agent auditable, pas nécessairement correct. C’est la limite la plus importante de la leçon.
</details>

## Exercice pratique

Ouvrez `code_samples/18-signed-receipts.ipynb` et complétez les quatre sections :

1. **Section 1** : Signez votre premier reçu et vérifiez-le.
2. **Section 2** : Falsifiez le reçu et observez l’échec de la vérification.
3. **Section 3** : Construisez une chaîne de trois reçus et vérifiez l’intégrité de la chaîne.
4. **Section 4** : Appliquez le schéma à un agent construit avec le Microsoft Agent Framework : enveloppez un appel d’outil dans la signature du reçu, puis vérifiez ce reçu indépendamment.
**Défi supplémentaire 1 :** étendez le schéma du reçu avec un champ supplémentaire de votre choix (par exemple, un ID de requête pour le traçage), mettez à jour la logique de signature canonique pour l'inclure, et confirmez que le reçu peut toujours être vérifié correctement. Puis modifiez ce champ après la signature et confirmez que la vérification échoue. Cela vous oblige à comprendre comment chaque octet de l'encodage canonique contribue à la signature.

**Défi supplémentaire 2 :** effectuez un hachage SHA-256 de deux de vos reçus ensemble (concaténez leurs octets canoniques dans un ordre déterministe) et insérez le digest résultant comme un nouveau champ sur un troisième reçu avant de le signer. Vérifiez que les trois reçus peuvent toujours être vérifiés correctement. Vous venez de créer une preuve d'inclusion en une étape : toute personne détenant le troisième reçu peut prouver que les deux premiers existaient au moment de sa signature, sans avoir besoin de révéler leur contenu. C’est le modèle utilisé à grande échelle par les reçus à divulgation sélective (engagements de Merkle, RFC 6962).

## Conclusion

Les reçus cryptographiques fournissent aux agents IA une piste d’audit qui est :

- **Indépendamment vérifiable** : toute partie disposant de la clé publique peut vérifier, sans dépendance à un service.
- **À preuve de falsification** : toute modification invalide la signature.
- **Portable** : un reçu est un petit fichier JSON ; il peut être archivé, transmis et vérifié partout.
- **Conforme aux standards** : basé sur Ed25519 (RFC 8032), JCS (RFC 8785) et SHA-256, tous des primitives largement déployées.

Ils ne remplacent pas la validation d’entrée, l’application des politiques ou l’infrastructure d’identité. Ils fondent ces couches. Lorsque vous déployez des agents dans des environnements régulés, des workflows multi-organisations ou tout contexte où un auditeur futur ne peut être supposé vous faire confiance, les reçus rendent la piste d’audit honnête.

Le point le plus important : les reçus prouvent qui a dit quoi, quand. Ils ne prouvent pas que ce qui a été dit est vrai ou juste. Gardez cette distinction bien en tête. C’est la différence entre un système de traçabilité honnête et un système trompeur.

## Liste de contrôle pour la production

Quand vous êtes prêt à passer de cette leçon au déploiement d’agents signant des reçus dans un environnement réel :

- [ ] **Déplacez la clé de signature hors du poste développeur.** Utilisez Azure Key Vault, AWS KMS ou un module de sécurité matériel. La clé privée signant vos reçus ne doit jamais vivre dans le contrôle de source ou en clair sur les machines applicatives.
- [ ] **Publiez la clé publique de vérification.** Les auditeurs en ont besoin pour vérifier hors ligne. Le modèle standard est un ensemble JWK à une URL connue (RFC 7517), par ex. `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **Ancrez la chaîne de manière externe.** Écrivez périodiquement le hash de la tête de chaîne la plus récente dans un journal de transparence (Sigstore Rekor, autorité de timestamp RFC 3161, ou un second système interne) afin qu’une partie externe puisse confirmer « cette chaîne existait à cette date ».
- [ ] **Stockez les reçus de manière immuable.** Un stockage blob append-only (Azure Storage avec politiques d’immuabilité, AWS S3 Object Lock) empêche un initié de réécrire l’historique depuis la couche stockage.
- [ ] **Décidez de la rétention.** Plusieurs régimes de conformité requièrent plusieurs années de conservation. Planifiez la croissance des reçus (chaque reçu pèse ~500 octets ; un agent effectuant 10 000 appels par jour produit ~1,8 Go par an).
- [ ] **Documentez ce que les reçus ne couvrent pas.** Les reçus prouvent l’attribution, l’intégrité et l’ordre. Votre guide d’exploitation doit lister explicitement quels contrôles supplémentaires (validation d’entrée, application de politique, limitation de débit, infrastructure d’identité) s’ajoutent aux reçus dans votre posture de gouvernance.

### Vous avez d’autres questions sur la sécurisation des agents IA ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, participer aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Au-delà de cette leçon

Cette leçon couvre la signature d’un seul reçu et les séquences enchaînées par hachage. Les mêmes primitives composent plusieurs schémas plus avancés que vous pourrez rencontrer lorsque votre posture de gouvernance mûrit :

- **Divulgation sélective.** Lorsque les champs d’un reçu sont engagés indépendamment (arbre de Merkle style RFC 6962), vous pouvez révéler certains champs à certains auditeurs et prouver que les autres restent inchangés sans les exposer. Utile quand un même reçu doit satisfaire à la fois un audit complet (souhaitant la complétude) et des régulations de minimisation des données comme le RGPD (souhaitant que l’auditeur voie le moins possible).
- **Révocation de reçus.** Si une clé de signature est compromise, vous devez pouvoir marquer tous les reçus signés par cette clé comme non fiables à partir d’un moment donné. Pratiques courantes : clés de signature à courte durée de vie accompagnées d’une liste de révocation publiée, ou journal de transparence avec entrées de révocation.
- **Reçus à signature bilatérale / scindée.** Certaines implémentations divisent la charge signée en demi-parties pré-exécution (`authorization_*`) et post-exécution (`result_*`) avec des signatures indépendantes, utile lorsque la décision d’autorisation et le résultat observé sont produits par des acteurs ou à des moments différents. Ceci s’ajoute au format de reçu enseigné dans cette leçon.
- **Composition de la charge utile.** Un reçu scelle les octets que vous placez dans `result_hash`. Les charges utiles réelles sont souvent plus riches qu’un simple résultat d’appel d’outil : raisonnement pré-décisionnel (prédiction modèle, options envisagées, preuves et leur complétude, posture de risque, chaîne de responsabilité, verdict de la porte) peut tout vivre dans la charge utile, scellée par un unique reçu. Ça maintient le format du reçu minimal tout en laissant évoluer les schémas de charge domaine par domaine.
- **Conformité entre implémentations.** Plusieurs implémentations indépendantes du même format de reçu (Python, TypeScript, Rust, Go) se vérifient mutuellement via des vecteurs de test communs. Si vous développez votre propre implémentation, valider avec des vecteurs publiés confirme la compatibilité filaire.
- **Migration post-quantique.** Ed25519 est largement déployé aujourd’hui mais n’est pas résistant au quantique. Le format de reçu est agile quant à l’algorithme : le champ `signature.alg` peut porter `ML-DSA-65` (le standard NIST de signature post-quantique) quand vous devez migrer. Prévoyez une période de transition où les reçus sont doublement signés.

## Ressources supplémentaires

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF Internet-Draft : Reçus de décision signés pour contrôle d’accès machine-à-machine</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vue d’ensemble de l’IA responsable (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032 : Algorithme de signature numérique sur courbe Edwards (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785 : Schéma de canonicalisation JSON (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962 : Transparence des certificats</a> (construction Merkle utilisée par les reçus à divulgation sélective)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, tutoriel 33 : reçus de décision vérifiables hors ligne</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">Vecteurs de test de conformité inter-implémentations</a> pour le format de reçu utilisé dans cette leçon (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">Documentation PyNaCl</a> (Ed25519 en Python)

## Leçon précédente

[Création d’agents d’utilisation informatique (CUA)](../15-browser-use/README.md)

## Leçon suivante

_(À déterminer par les mainteneurs du programme)_

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->