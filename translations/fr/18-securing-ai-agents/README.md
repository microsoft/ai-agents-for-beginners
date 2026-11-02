[Regardez la vidéo de la leçon : Sécuriser les agents IA avec des reçus cryptographiques](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Vidéo de la leçon et vignette à ajouter par l'équipe de contenu Microsoft après fusion, suivant le modèle des leçons 14 / 15.)_

# Sécuriser les agents IA avec des reçus cryptographiques

## Introduction

Cette leçon couvrira :

- Pourquoi les pistes d'audit pour les agents IA sont importantes pour la conformité, le débogage et la confiance.
- Ce qu'est un reçu cryptographique et en quoi il diffère d’une ligne de journal non signée.
- Comment produire un reçu signé pour un appel d'outil d’un agent en Python simple.
- Comment vérifier un reçu hors ligne et détecter toute falsification.
- Comment chaîner des reçus de sorte que la suppression ou le réordonnancement d’un reçu casse la chaîne.
- Ce que les reçus prouvent et ce qu’ils ne prouvent explicitement pas.

## Objectifs d’apprentissage

Après avoir suivi cette leçon, vous saurez comment :

- Identifier les modes d'échec qui motivent la provenance cryptographique des actions de l’agent.
- Produire un reçu signé Ed25519 sur une charge utile JSON canonique.
- Vérifier un reçu indépendamment en n'utilisant que la clé publique du signataire.
- Détecter la falsification en relançant la vérification sur un reçu modifié.
- Construire une séquence de reçus en chaîne de hachage et expliquer pourquoi la chaîne est importante.
- Reconnaître la limite entre ce que les reçus prouvent (attribution, intégrité, ordonnancement) et ce qu’ils ne prouvent pas (exactitude de l’action, validité de la politique).

## Le problème : la piste d’audit de votre agent

Imaginez que vous avez déployé un agent IA pour Contoso Travel. L’agent lit les demandes des clients, appelle une API de vols pour rechercher des options, et réserve des sièges au nom du client. Le trimestre dernier, l’agent a traité 50 000 réservations.

Aujourd’hui, un auditeur arrive. Il pose une question simple : « Montrez-moi ce que votre agent a fait. »

Vous remettez vos fichiers de journalisation. L’auditeur les consulte et pose une question plus difficile : « Comment puis-je savoir que ces journaux n'ont pas été modifiés ? »

C’est le problème de la piste d’audit. La plupart des déploiements d’agents aujourd’hui reposent sur :

- **Journaux d’application** : écrits par l’agent lui-même, modifiables par quiconque a accès au système de fichiers.
- **Services de journalisation cloud** : protégés contre la falsification au niveau de la plateforme, mais seulement si l’auditeur fait confiance à l’opérateur de la plateforme.
- **Journaux de transactions de base de données** : bien adaptés aux changements de base de données mais pas pour les appels d’outils arbitraires.

Aucun de ces moyens ne peut répondre à la question de l’auditeur sans que celui-ci ait à faire confiance à quelqu’un (vous, votre fournisseur cloud, votre vendeur de base de données). Pour un usage interne, cette confiance est souvent acceptable. Pour des charges de travail régulées (finance, santé, tout ce qui est soumis au règlement européen sur l’IA), ce n’est pas le cas.

Les reçus cryptographiques réduisent ce problème en rendant une déclaration signée indépendamment
vérifiable. L'auditeur a cependant encore besoin d'une raison hors-bande pour faire confiance à la clé de signature et
au composant qui a produit la déclaration. Une clé intégrée prouve la cohérence interne,
pas l'identité de l'émetteur ni l'emplacement d'exécution.

## Qu’est-ce qu’un reçu cryptographique ?

Un reçu est un objet JSON qui enregistre ce qu’un agent a fait, signé avec une signature numérique.

```mermaid
flowchart LR
    A[Agent invokes a tool] --> B[Build receipt payload]
    B --> C[Canonicalize JSON RFC 8785]
    C --> E[Ed25519 sign canonical bytes]
    E --> F[Receipt with signature]
    F --> G[Auditor verifies offline]
    G --> H{Signature valid?}
    H -- yes --> I[Signed statement is intact]
    H -- no --> J[Receipt rejected]
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

Trois propriétés assurent le fonctionnement :

1. **La signature**. Le reçu est signé par la passerelle de l'agent à l'aide d'une clé privée Ed25519. Toute personne disposant de la clé publique correspondante peut vérifier la signature hors ligne. Une partie s'appuyant sur le reçu doit épingler cette clé ou la résoudre depuis un registre de confiance externe au reçu. La falsification de tout champ signé rend la signature invalide.

2. **Encodage canonique**. Avant la signature, le reçu est sérialisé selon le JSON Canonicalization Scheme (JCS, RFC 8785). Cela garantit que deux implémentations produisant le même reçu logique produisent une sortie identique au niveau octet. Sans canonisation, différents sérialiseurs JSON produiraient des signatures différentes pour un même contenu.

3. **Chaînage de hachage**. Le champ `previous_receipt_hash` relie chaque reçu à celui qui le précède. La suppression ou le réordonnancement d'un reçu brise la séquence présentée. La détection d'une troncature ou d'une réécriture contrôlée par le signataire nécessite également une tête de chaîne actuelle épinglée, un point de contrôle attesté indépendamment, ou un engagement authentifié d'une population fermée.

Ensemble, ces propriétés fournissent trois garanties :

- **Attribution à une clé**: cette clé a signé ce contenu. L'identité organisationnelle ou humaine nécessite une liaison de clé de confiance.
- **Intégrité** : le contenu n’a pas changé depuis la signature.
- **Ordre au sein de la séquence vérifiée**: ce reçu renvoie à ce prédécesseur.

## Produire un reçu en Python

Vous n’avez pas besoin d’une bibliothèque spéciale pour produire un reçu. Les primitives cryptographiques sont largement disponibles et la logique nécessite quelques dizaines de lignes de Python.

Les exercices pratiques de `code_samples/18-signed-receipts.ipynb` parcourent l'ensemble du flux. Le `code_samples/18-signed-receipts.execution-receipt.json`, géré sous contrôle de version, enregistre le hachage exact du notebook, l'environnement Python, le nombre de cellules et les vérifications de la dernière exécution propre sans modifier les sorties enregistrées de la leçon. La version résumée :

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # RFC 8785 canonical JSON

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# Generate or load a signing key (in production, store in a key vault)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key
TRUSTED_PUBLIC_KEYS = {b64url_nopad(bytes(verify_key))}  # pinned out of band by the verifier

# Build the receipt payload (no signature yet)
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

# Canonicalize and sign the JCS bytes directly. PureEdDSA hashes internally.
canonical_bytes = canonicalize(payload)
signature_bytes = signing_key.sign(canonical_bytes).signature

# Attach a structured signature object.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```

C’est toute la chaîne de signature. Les exercices dans le notebook détaillent chaque étape.

## Vérifier un reçu et détecter la falsification

La vérification est l’opération inverse :

```python
import base64
import hashlib
from nacl import signing
from nacl.exceptions import CryptoError
from jcs import canonicalize

def b64url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.b64decode(s + padding, altchars=b"-_", validate=True)

def verify_receipt(receipt: dict, trusted_public_keys: set[str]) -> bool:
    # The signature is a structured object: {"alg", "sig", "public_key"}.
    if not isinstance(receipt, dict):
        return False
    sig_obj = receipt.get("signature")
    if not isinstance(sig_obj, dict) or sig_obj.get("alg") != "EdDSA":
        return False
    try:
        # An inline key proves only self-consistency. Trust is configured out of band.
        public_key = sig_obj.get("public_key")
        signature = sig_obj.get("sig")
        if not isinstance(public_key, str) or not isinstance(signature, str):
            return False
        if public_key not in trusted_public_keys:
            return False
        payload = {k: v for k, v in receipt.items() if k != "signature"}
        canonical_bytes = canonicalize(payload)
        verify_key = signing.VerifyKey(b64url_decode(public_key))
        verify_key.verify(canonical_bytes, b64url_decode(signature))
        return True
    except (CryptoError, TypeError, ValueError, KeyError, OverflowError):
        return False
```

Cette fonction prend un reçu ainsi que l'ensemble de clés épinglées de la partie faisant confiance et renvoie
`True` uniquement si la signature est valide avec une clé acceptée. La vérification ne nécessite aucun
appel réseau, mais la confiance envers la clé reste une décision de configuration externe.

Pour voir la détection de falsification en action, le notebook détaille :

1. Produire un reçu valide et confirmer sa vérification.
2. Modifier un octet dans le champ `tool_args_hash`.
3. Relancer la vérification et constater l’échec.

C’est la démonstration pratique que les reçus sont évidents à falsifier : toute modification, si minime soit-elle, casse la signature.

## Chaîner les reçus pour les agents en plusieurs étapes

Un reçu signé protège une action unique. Une chaîne de reçus protège une séquence.

```mermaid
flowchart LR
    R0[Receipt 0<br/>genesis] --> R1[Receipt 1]
    R1 --> R2[Receipt 2]
    R2 --> R3[Receipt 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

Chaque reçu enregistre le hachage du reçu précédent. Pour supprimer silencieusement le reçu 2, un attaquant devrait soit :

- Modifier le champ `previous_receipt_hash` du reçu 3 (ce qui casse la signature du reçu 3), OU
- Forger une nouvelle signature sur un reçu 3 modifié (ce qui nécessite la clé privée de l’agent).

Si la clé privée est protégée et qu'un vérificateur ancre la tête d'une chaîne attestée indépendamment
ces attaques sont détectables. Publier la clé dans chaque reçu n'est pas
suffisant : un signataire ou un attaquant peut présenter une clé différente, réécrire un suffixe, ou
tronquer la chaîne à moins que la partie qui se fie n'ait une ancre externe de confiance et d'exhaustivité.

Le notebook détaille :

1. La construction d’une chaîne de trois reçus.
2. La vérification que le `previous_receipt_hash` de chaque reçu correspond bien au hachage réel du reçu précédent.
3. La falsification d’un reçu au milieu de la chaîne et la rupture visible de la chaîne à ce point précis.

C'est ainsi que vous produisez une piste d'audit qu'un auditeur externe peut vérifier sous ses
propres clés d'émetteur épinglées et points de contrôle de chaîne, sans faire confiance à votre magasin de journaux modifiable.

## Ce que prouvent les reçus (et ce qu’ils ne prouvent pas)

C’est la section la plus importante de cette leçon. Les reçus sont puissants mais leur puissance a des limites.

**Les reçus prouvent trois choses :**

1. **Attribution** : une clé spécifique a signé une charge utile spécifique.
2. **Intégrité** : la charge utile n’a pas changé depuis la signature.
3. **Ordre au sein d'une séquence présentée et vérifiée**: ce reçu renvoie à ce prédécesseur.

**Les reçus ne prouvent PAS :**

1. **Exactitude** : que l’action de l’agent était la bonne action. Un reçu peut être signé pour une mauvaise réponse aussi proprement que pour une bonne réponse.
2. **Conformité à la politique** : que la politique référencée dans `policy_id` a réellement été évaluée, ou qu’elle aurait permis cette action si elle avait été vérifiée. Le reçu enregistre ce qui a été affirmé, pas ce qui a été appliqué.
3. **Identité au-delà de la clé** : le reçu dit « cette clé a signé ce contenu ». Il ne dit pas « cet humain a autorisé cela ». Relier une clé à une personne ou organisation nécessite une infrastructure d’identité distincte (un annuaire, un registre de clés publiques, etc.)
4. **Véracité des entrées** : si l’agent reçoit un prompt manipulé et agit en conséquence, le reçu enregistre fidèlement l’action. Les reçus sont en aval de la validation des entrées, pas un substitut.
5. **Exécution ou effet dans le monde réel**: un reçu post-appel enregistre ce que son émetteur affirme s'être produit. Prouver une admission ou réconcilier un effet externe exige des preuves provenant de l'exécuteur réel ou de la frontière du fournisseur.
6. **Complétude**: l'absence d'un reçu peut signifier bloqué, omis, perdu ou non instrumenté. L'absence ne devient une preuve que dans une population fermée authentifiée.
7. **Temps de confiance**: un horodatage signé prouve que le signataire détenait cette valeur, pas que la valeur était correcte. Le temps de confiance nécessite une autorité temporelle séparée ou un point de contrôle attesté.

Cette limite importe pour deux raisons :

- Elle indique à quoi servent réellement les reçus : rendre le comportement des agents auditable et évident à falsifier, même à travers des frontières organisationnelles.
- Elle indique quelles couches supplémentaires vous devez encore ajouter : validation des entrées (Leçon 6), application de politique (abordée brièvement ci-dessous), et infrastructure d’identité (hors sujet de cette leçon).

Une erreur fréquente est de supposer que « nous avons des reçus » signifie « nous sommes gouvernés ». Ce n’est pas le cas. Les reçus sont une base. La gouvernance est le système que vous construisez par-dessus.

## Associer la signature d'un approbateur à l'action exacte

Le point 3 ci-dessus mérite sa propre section : un reçu d'action indique "cette clé a signé ce contenu", jamais "un humain a autorisé cela". Pour les actions à haut risque (remboursements, suppressions, virements), une signature d'approbateur distincte peut lier l'action exacte. Relier cette clé à un humain et vérifier la présence humaine restent des responsabilités séparées.

Le notebook de suivi `code_samples/human-authorization-receipts.ipynb` ajoute un deuxième type de reçu, `human.approval.v1`, dans la même forme d'enveloppe que les reçus de la leçon. Cette enveloppe contient une charge utile typée, signée par Ed25519 sur ses octets JCS canoniques, avec l'objet `signature` en dehors des octets signés. Une clé d'approbateur signe l'**action canonique complète et son empreinte**; une clé d'agent signe une revendication portant la **même empreinte de l'action** et un `parent_approval_ref`, le `receipt_hash` de l'approbation, la même convention que `previous_receipt_hash` dans la chaîne que vous avez construite ci-dessus. Un `verify_chain` parcourt les deux artefacts sous **des registres de clés épinglés séparés**. Les clés des approbateurs et les clés des agents restent séparées, donc le chemin du code est partagé mais les autorités ne le sont jamais.

La propriété que cela procure, énoncée avec précision : *la clé d'approbation épinglée a signé cette
action exacte, et la clé de l'agent a ensuite signé une déclaration portant la même empreinte d'action.*
C'est une preuve utile, mais ce n'est pas en soi la preuve que l'action a été exécutée. Pour
contrôler l'exécution, l'approbation exacte doit également être réservée et consommée une seule fois à la
frontière réelle de l'exécuteur ; les résultats inconnus du fournisseur doivent rester inconnus plutôt que d'être
réessayés à l'aveugle. Les fixtures de refus du notebook testent la couche receipt-chain :

- manipulation, député confus, clés falsifiées de part et d'autre, et entrée malformée;
- **autorité périmée**: une signature qui se vérifie encore, refusée malgré tout parce que la version de la politique a changé, la clé de l'approbateur a été retirée du registre épinglé, ou l'approbation a expiré avant l'heure de vérification fournie;
- **substitution de digest** : un reçu d’action signé valide pointant vers une *vraie* approbation qui lie une *action canonique différente*.

Chaque refus est accompagné d'une raison distincte, de sorte qu'un auditeur lisant un refus peut déterminer si l'autorité est devenue obsolète ou si l'action revendiquée a changé. La vérification est en lecture seule et répétable : elle ne consomme pas l'approbation et n'invoque pas de fournisseur. Un exécuteur distinct nécessite une protection durable et atomique contre la relecture ainsi que des résultats explicites de succès, d'échec et d'indétermination. Le reçu d'approbation humaine est une composition pédagogique définie par cette leçon, et non un type de reçu défini par `draft-farley-acta-signed-receipts`.

## Références pour la production

Le code Python de cette leçon est volontairement minimal pour que vous puissiez lire chaque ligne et comprendre précisément ce qui se passe. En production, vous avez deux options :

1. **Construire directement sur les primitives cryptographiques.** Les 50 lignes vues ci-dessus suffisent pour de nombreux cas d’usage. PyNaCl (Ed25519) et le paquet `jcs` (JSON canonique) sont des bibliothèques bien maintenues et auditées.

2. **Utiliser une bibliothèque de reçus prête à l’emploi.** Plusieurs projets open source implémentent ce même modèle avec des fonctionnalités supplémentaires (rotation de clés, vérification par lots, distribution de jeu de clés JWK, intégration avec moteurs de politique) :
   - La chaîne de signature utilise les conventions JCS et scope de signature dans un Internet-Draft indépendant de l’IETF ([`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/), révision 02). Le reçu plat éducatif de cette leçon diffère de l’enveloppe `{payload, signature}` du draft et n’est pas présenté comme une implémentation conforme. Le draft publie une suite de conformité partagée ([agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors)) pour implémentations ciblant ce format.
   - Le Microsoft Agent Governance Toolkit compose des reçus avec des décisions de politique basées sur Cedar ; voir le Tutoriel 33 dans ce dépôt pour un exemple de bout en bout.
   - Les paquets `protect-mcp` (npm) et `@veritasacta/verify` (npm) fournissent une implémentation Node de signature de reçus et vérification hors ligne, destinés à envelopper tout serveur MCP avec une piste d’audit évidente à falsifier, incluant un flux held-for-co-sign dans lequel une action mise en pause émet un reçu d’approbation lié au digest de l’action (soutenu par WebAuthn dans le flux desktop), le même modèle d’approbation que celui du notebook d’autorisation humaine ci-dessus.
   - Le SDK Python **[nobulex](https://github.com/arian-gogani/nobulex)** (`pip install nobulex`) fournit le même modèle de signature Ed25519 + JCS en Python avec intégrations LangChain et CrewAI, incluant des vecteurs de test de validation croisée publiés et une cartographie de conformité contribué via [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210).
- **[EMILIA Protocol](https://github.com/emiliaprotocol/emilia-protocol)** fournit une couche d'application d'actions exactes complémentaire: reçus d'approbation vérifiables hors ligne, WebAuthn épinglé ou autorité de quorum, consommation unique à la frontière de l'exécuteur, et un chemin explicite à issue indéterminée. Ses adaptateurs de framework considèrent un reçu comme une preuve nécessaire plutôt que comme la preuve qu'un effet externe s'est produit.

Le choix entre développer soi-même et utiliser une bibliothèque reflète celui entre écrire sa propre bibliothèque JWT et en utiliser une testée : les deux sont raisonnables ; la bibliothèque fait gagner du temps et réduit la surface d’audit ; la méthode from-scratch vous force à comprendre chaque primitive. Cette leçon enseigne la voie from-scratch pour vous donner la base dans les deux cas.

## Vérification des connaissances

Testez votre compréhension avant de passer à l’exercice pratique.

**1. Un reçu est signé avec la clé privée Ed25519 de l’agent. L’auditeur dispose seulement de la clé publique. L’auditeur peut-il vérifier le reçu hors ligne ?**

<details>
<summary>Réponse</summary>

Oui, la vérification cryptographique nécessite uniquement la clé publique et les octets signés. L'
auditeur doit encore obtenir et épingler la clé publique acceptée indépendamment du reçu.
Aucun appel réseau n'est requis une fois que cette configuration de confiance est établie.
</details>

**2. Un attaquant modifie le champ `policy_id` d’un reçu pour prétendre qu’il était soumis à une politique plus permissive. La signature portait sur la charge utile originale. Que se passe-t-il lors de la vérification ?**

<details>
<summary>Réponse</summary>


La vérification échoue. La signature a été calculée sur les octets canoniques de la charge utile originale ; modifier un champ quelconque change ces octets, ce qui rend la signature invalide. L'attaquant aurait besoin de la clé privée pour produire une nouvelle signature valide, ce qu'il ne possède pas.
</details>

**3. Pourquoi le reçu inclut-il un `tool_args_hash` et un `result_hash` plutôt que les arguments et résultats bruts ?**

<details>
<summary>Réponse</summary>

Deux raisons. Premièrement, le reçu peut devoir être archivé ou transmis dans des environnements où la fuite du contenu brut (Données personnelles, données métier) pose problème. Le hachage maintient le reçu compact et protège le contenu ; l'auditeur vérifie que le hachage correspond à une copie stockée séparément du contenu réel. Deuxièmement, les hachages ont une taille fixe ; un reçu avec des hachages a une taille limitée indépendamment de la taille des entrées et sorties.
</details>

**4. Le champ `previous_receipt_hash` lie chaque reçu à son prédécesseur. Si un attaquant supprime silencieusement un reçu du milieu d'une chaîne, qu'est-ce qui devient invalide ?**

<details>
<summary>Réponse</summary>

Le reçu présenté suivant ne se rattache plus à son prédécesseur attendu, donc la vérification
de cette séquence présentée échoue à partir de l'interruption. Si le signataire contrôle la clé privée,
il peut réécrire ou tronquer un suffixe. La détection de cela nécessite une tête courante épinglée,
un point de contrôle externe, ou un engagement authentifié de la population.
</details>

**5. Un reçu est vérifié avec succès. Cela prouve-t-il que l'action de l'agent était correcte, valide ou conforme à la politique ?**

<details>
<summary>Réponse</summary>

Non. Dans un contexte de clé épinglée et de chaîne, un reçu valide prouve l'attribution de la signature,
l'intégrité du contenu, et un lien vers le prédécesseur présenté. Il NE prouve PAS que l'
action était correcte ou exécutée, que la politique a été évaluée, que l'horodatage est
fiable, ou que l'ensemble des enregistrements est complet. C'est la frontière la plus importante de la leçon.
</details>

## Exercice pratique

Ouvrez `code_samples/18-signed-receipts.ipynb` et complétez les quatre sections :

1. **Section 1** : Signez votre premier reçu et vérifiez-le.
2. **Section 2** : Altérez le reçu et observez l’échec de la vérification.
3. **Section 3** : Construisez une chaîne de trois reçus et vérifiez l'intégrité de la chaîne.
4. **Section 4** : Appliquez le modèle à un agent construit avec le Microsoft Agent Framework : encapsulez un appel d’outil dans la signature de reçu, puis vérifiez le reçu indépendamment.

**Défi supplémentaire 1 :** étendez le schéma de reçu avec un champ supplémentaire de votre choix (par exemple, un ID de requête pour le traçage), mettez à jour la logique de signature canonique pour l’inclure, et confirmez que le reçu passe toujours la vérification bidirectionnelle. Puis modifiez ce champ après signature et confirmez l’échec de la vérification. Cela vous force à comprendre comment chaque octet de l’encodage canonique contribue à la signature.

**Défi supplémentaire 2 :** Hachez avec SHA-256 deux de vos reçus ensemble (concaténez leurs octets canoniques dans un ordre déterministe) et intégrez le digest résultant comme un nouveau champ sur un troisième reçu avant de le signer. Vérifiez que les trois reçus passent toujours la vérification bidirectionnelle. Vous avez ainsi construit une preuve d’inclusion en une étape : toute personne possédant le troisième reçu peut prouver que les deux premiers existaient au moment de sa signature, sans devoir révéler leur contenu. C’est le modèle utilisé à grande échelle dans les reçus à divulgation sélective (engagements de Merkle, RFC 6962).

## Conclusion

Les reçus cryptographiques fournissent aux agents IA une piste d’audit qui est :

- **Vérifiable de manière indépendante sous une confiance épinglée**: une partie disposant de clés publiques acceptées et d'octets signés peut vérifier sans dépendance à un service.
- **À l’épreuve des altérations** : toute modification invalide la signature.
- **Portable** : un reçu est un petit fichier JSON ; il peut être archivé, transmis et vérifié partout.
- **Aligné sur les standards** : construit sur Ed25519 (RFC 8032), JCS (RFC 8785) et SHA-256, des primitives largement déployées.

Ils ne remplacent pas la validation des entrées, l'application des politiques, l'admission des exécuteurs,
les preuves de résultat, les contrôles d'exhaustivité ou l'infrastructure d'identité. Ils constituent une base
pour ces couches. Dans les flux de travail réglementés ou impliquant plusieurs organisations, les reçus rendent les déclarations
spécifiques de l'émetteur vérifiables indépendamment sous la propre configuration de confiance de l'auditeur.

Le point le plus important : les reçus prouvent qu'une clé particulière a signé
un contenu particulier. Un horodatage inclus est une assertion du signataire sauf s'il est attesté séparément dans le temps.
Un reçu ne prouve pas que son contenu était vrai, qu'une action a été exécutée, ou que le
jeu d'enregistrements est complet. Respectez strictement ces distinctions.

## Liste de vérification pour la production

Lorsque vous êtes prêt à passer de cette leçon au déploiement d’agents signant des reçus en environnement réel :

- [ ] **Déplacez la clé de signature hors de l’ordinateur du développeur.** Utilisez Azure Key Vault, AWS KMS ou un module matériel de sécurité. La clé privée signant vos reçus ne doit jamais se trouver dans le contrôle de source ou en clair sur les machines applicatives.
- [ ] **Établir la confiance dans la clé du vérificateur.** Publiez les clés via un JWK Set ou un registre, puis demandez aux parties prenantes de fixer l'identité de l'émetteur acceptée, l'ensemble de clés et la politique de rotation en dehors des reçus individuels. Une clé intégrée seule n'est pas une ancre de confiance.
- [ ] **Ancrez la chaîne à l’extérieur.** Écrivez périodiquement le hash de la tête de chaîne la plus récente dans un journal de transparence (Sigstore Rekor, une autorité de timestamp RFC 3161, ou un second système interne) pour qu’un tiers puisse confirmer « cette chaîne existait à ce moment ».
- [ ] **Stockez les reçus de manière immuable.** Le stockage append-only (Azure Storage avec politiques d’immuabilité, AWS S3 Object Lock) empêche un initié de réécrire l’histoire au niveau du stockage.
- [ ] **Décidez de la durée de conservation.** De nombreux régimes de conformité exigent une conservation de plusieurs années. Prévoyez la croissance des reçus (chaque reçu fait ~500 octets; un agent effectuant 10 000 appels par jour génère ~1.8 Go par an).
- [ ] **Documentez ce que les reçus ne couvrent pas.** Les reçus prouvent l’attribution, l’intégrité et l’ordre. Votre plan d’exploitation doit lister explicitement quels contrôles supplémentaires (validation d’entrée, application des politiques, limitation du taux, infrastructure d’identité) accompagnent les reçus dans votre posture de gouvernance.

### Vous avez d’autres questions sur la sécurisation des agents IA ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les agents IA.

## Au-delà de cette leçon

Cette leçon couvre la signature d’un seul reçu et les séquences en chaîne de hachages. Les mêmes primitives s’assemblent en plusieurs modèles plus avancés que vous pouvez rencontrer à mesure que votre posture de gouvernance mûrit :

- **Divulgation sélective.** Lorsque les champs d’un reçu sont engagés indépendamment (arbre de Merkle style RFC 6962), vous pouvez révéler certains champs à certains auditeurs et prouver que les autres n’ont pas changé sans les exposer. Utile quand un même reçu doit satisfaire à la fois un audit complet (exigeant exhaustivité) et des réglementations de minimisation des données comme le RGPD (qui veulent que l’auditeur voie le moins possible).
- **Révocation de reçus.** Si une clé de signature est compromise, vous devez pouvoir marquer tous les reçus signés par cette clé comme non fiables à partir d’un moment donné. Modèles standards : clés de signature à courte durée de vie plus liste de révocation publiée, ou journal de transparence avec entrées de révocation.
- **Reçus bilatéraux / signature fractionnée.** Certaines implémentations divisent la charge utile signée en deux moitiés, pré-exécution (`authorization_*`) et post-exécution (`result_*`), avec signatures indépendantes, utile lorsque la décision d’autorisation et le résultat observé sont produits par différents acteurs ou à différents moments. Cela s’ajoute de façon additive au format de reçu enseigné dans cette leçon.
- **Composition de charge utile.** Un reçu scelle les octets que vous mettez dans `result_hash`. Les charges utiles réelles sont souvent plus riches qu’un simple résultat d’appel d’outil : raisonnement pré-décision (prédiction modèle, options considérées, preuves et leur complétude, posture de risque, chaîne de responsabilité, résultat du gate) peuvent tous vivre dans la charge utile, scellée par un seul reçu. Cela maintient le format de reçu minimal tout en laissant évoluer les schémas de charge utile domaine par domaine.
- **Conformité inter-implémentation.** Plusieurs implémentations indépendantes du même format de reçu (Python, TypeScript, Rust, Go) se vérifient entre elles avec des vecteurs de test partagés. Si vous créez votre propre implémentation, valider avec les vecteurs publiés confirme la compatibilité sur le fil.
- **Migration post-quantique.** Ed25519 est largement déployé aujourd'hui mais n'est pas résistant aux attaques quantiques. Une étiquette `alg` seule ne constitue pas une migration: un profil doit définir l'encodage des clés ML-DSA, les octets signés canoniques, la vérification, la politique du relying party, la résistance aux rétrogradations, et la sémantique de transition. Planifiez et testez une transition à double signature contre des vecteurs partagés avant d'avancer des revendications de compatibilité.

## Ressources supplémentaires

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">Brouillon IETF : Reçus de décision signés pour le contrôle d’accès machine-à-machine</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vue d’ensemble de l’IA responsable (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032 : Algorithme de signature numérique Edwards-Curve (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785 : Schéma de canonicalisation JSON (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962 : Transparence de certificat</a> (construction en arbre de Merkle utilisée par les reçus à divulgation sélective)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, Tutoriel 33 : Reçus de décision vérifiables hors ligne</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">Vecteurs de test de conformité inter-implémentation</a> pour le format de reçu utilisé dans cette leçon (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">Documentation PyNaCl</a> (Ed25519 en Python)

## Leçon précédente

[Création d’agents IA locaux](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
