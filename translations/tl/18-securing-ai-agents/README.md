[Panoorin ang video ng leksyon: Pag-seguro ng AI Agents gamit ang Cryptographic Receipts](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Ang video ng leksyon at thumbnail ay idaragdag ng Microsoft content team pagkatapos ng pagsasama, na sumusunod sa pattern ng leksyon 14 / 15.)_

# Pag-seguro ng AI Agents gamit ang Cryptographic Receipts

## Panimula

Saklaw ng leksyon na ito ang mga sumusunod:

- Bakit mahalaga ang audit trails para sa AI agents sa pagsunod, pag-debug, at pagtitiwala.
- Ano ang cryptographic receipt at paano ito naiiba sa unsigned log line.
- Paano gumawa ng signed receipt para sa tool call ng agent gamit ang plain Python.
- Paano mag-verify ng receipt offline at matuklasan ang pagmanipula.
- Paano i-chain ang mga receipt upang ang pagtanggal o pagbabago ng pagkakasunod-sunod ng isa ay magdudulot ng sira sa chain.
- Ano ang pinapatunayan ng mga receipt at ano ang hindi nila pinapatunayan.

## Mga Layunin sa Pag-aaral

Matapos matapos ang leksyon na ito, malalaman mo kung paano:

- Tukuyin ang mga failure modes na nagtutulak ng cryptographic provenance para sa mga aksyon ng agent.
- Gumawa ng Ed25519-signed receipt gamit ang canonical JSON payload.
- Mag-verify ng receipt nang independent gamit lamang ang public key ng signer.
- Matuklasan ang pagmanipula sa pamamagitan ng muling pag-verify sa nabagong receipt.
- Bumuo ng hash-chained sequence ng mga receipt at ipaliwanag kung bakit mahalaga ang chain.
- Kilalanin ang hangganan sa pagitan ng mga pinapatunayan ng receipts (attribution, integridad, pagkakasunod-sunod) at ng hindi nila pinapatunayan (tama ng aksyon, katumpakan ng polisiya).

## Ang Problema: Audit Trail ng Iyong Agent

Isipin mong nag-deploy ka ng AI agent para sa Contoso Travel. Binabasa ng agent ang mga kahilingan ng customer, tumatawag sa flights API para maghanap ng mga opsyon, at nagbu-book ng mga upuan para sa customer. Noong nakaraang quarter, ang agent ay nagproseso ng 50,000 bookings.

Ngayon ay dumating ang isang auditor. Nagtanong sila ng simpleng tanong: "Ipakita mo sa akin ang ginawa ng iyong agent."

Iniabot mo ang iyong mga log file. Tiningnan ng auditor ito at tinanong ang mas mahirap na tanong: "Paano ko malalaman na hindi na-edit ang mga log na ito?"

Ito ang problema sa audit-trail. Karamihan sa mga deployed na agent ngayon ay umaasa sa:

- **Application logs**: sinusulat ng mismong agent, maaaring i-edit ng sinuman na may access sa file system.
- **Cloud logging services**: may tamper-evident sa platform level pero kailangan ng tiwala sa platform operator ng auditor.
- **Database transaction logs**: angkop para sa mga pagbabago sa database ngunit hindi para sa arbitraryong pagtawag sa mga tool.

Walang isa man sa mga ito ang makakasagot ng tanong ng auditor nang hindi kinakailangang magtiwala ang auditor sa isang tao (ikaw, ang iyong cloud provider, ang vendor ng iyong database). Sa panloob na gamit, madalas tanggap ang tiwalang iyon. Sa mga regulated workloads (finance, healthcare, anumang sakop ng EU AI Act), hindi ito tanggap.

Nilulutas ng cryptographic receipts ito sa pamamagitan ng paggawa ng bawat aksyon ng agent na mapapatunayan nang independent. Hindi kailangang magtiwala ang auditor sa iyo. Kailangan lang nila ang iyong public key at ang receipt mismo.

## Ano ang Cryptographic Receipt?

Ang receipt ay isang JSON object na nagrerecord kung ano ang ginawa ng agent, na nilagdaan gamit ang digital signature.

```mermaid
flowchart LR
    A[Gumagamit ng ahente ng isang kasangkapan] --> B[Bumuo ng payload ng resibo]
    B --> C[Canonicalize JSON RFC 8785]
    C --> D[SHA-256 hash]
    D --> E[Ed25519 lagdaan]
    E --> F[Resibo na may pirma]
    F --> G[Beripikahin ng auditor offline]
    G --> H{Valid ba ang pirma?}
    H -- yes --> I[Patunay na hindi nabago]
    H -- no --> J[Tinanggihan ang resibo]
```

Ang minimal na receipt ay ganito:

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

Tatlong katangian ang gumagawa ng trabaho:

1. **Ang lagda**. Nilagdaan ang receipt ng gateway ng agent gamit ang isang Ed25519 private key. Sinuman na may katumbas na public key ay maaaring mag-verify ng lagda offline. Ang pagmanipula sa kahit anong field ay nagpapawalang-bisa sa lagda.

2. **Canonical encoding**. Bago pumirma, ang receipt ay naisalin sa pamamagitan ng JSON Canonicalization Scheme (JCS, RFC 8785). Tinitiyak nito na dalawang implementations na gumagawa ng magkaparehong logical receipt ay gumagawa ng byte-identical na output. Kung walang canonicalization, iba't ibang JSON serializers ay gagawa ng ibang mga lagda para sa parehong nilalaman.

3. **Hash chaining**. Ang field na `previous_receipt_hash` ay nag-uugnay sa bawat receipt sa naunang receipt. Ang pagtanggal o pagbabago ng pagkakasunod-sunod ng receipt ay sisira sa bawat receipt na sumunod dito. Makikita ang pagmanipula sa antas ng chain kahit mapalampas ang mga indibidwal na lagda.

Sama-samang nagbibigay ang mga katangiang ito ng tatlong garantiya:

- **Pagkilala (Attribution)**: nilagdaan ng key na ito ang nilalamang ito.
- **Integridad (Integrity)**: hindi nagbago ang nilalaman mula nang mapirmahan.
- **Pagkakasunod-sunod (Ordering)**: ang receipt na ito ay sumunod sa receipt na iyon sa chain.

## Paggawa ng Receipt sa Python

Hindi mo kailangan ng espesyal na library para gumawa ng receipt. Malawak ang availability ng mga cryptographic primitives at ang logic ay ilang dosenang linya ng Python lang.

Ang mga hands-on exercise sa `code_samples/18-signed-receipts.ipynb` ay nagpapakita ng buong proseso. Ang buod:

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

# Gumawa o mag-load ng signing key (sa produksyon, itago sa key vault)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# Buoin ang receipt payload (wala pang lagda)
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

# Canonicalize, hash, pirmahan.
canonical_bytes = canonicalize(payload)
message_hash = hashlib.sha256(canonical_bytes).digest()
signature_bytes = signing_key.sign(message_hash).signature

# Ikabit ang isang istrukturadong signature object.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```

Iyan ang buong signing pipeline. Ang mga exercise sa notebook ay nagpapaliwanag ng bawat hakbang.

## Pag-verify ng Receipt at Pagtuklas ng Pagmanipula

Ang pag-verify ay ang kabaligtaran ng operasyon:

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
    # Ang lagda ay isang estrukturadong bagay: {"alg", "sig", "public_key"}.
    sig_obj = receipt.get("signature")
    if not sig_obj or sig_obj.get("alg") != "EdDSA":
        return False

    # I-reconstruct ang payload na aktwal na nilagdaan (lahat maliban sa lagda).
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

Tumatanggap ang function na ito ng receipt at nagbabalik ng `True` kung valid ang lagda, `False` kung hindi. Walang network call, walang serbisyo, walang pangangailangan ng tiwala sa anumang third party.

Para makita ang pag-detek ng pagmanipula sa aksyon, tinatalakay ng notebook ang:

1. Paggawa ng valid na receipt at pagtiyak na ito ay nako-verify.
2. Pagbabago ng isang byte sa field na `tool_args_hash`.
3. Muling pag-verify na nagpapakita ng pagkabigo.

Ito ang praktikal na demonstrasyon na ang mga receipt ay tamper-evident: kahit anong pagbabago, gaano man kaliit, ay sumisira sa lagda.

## Pag-chain ng Mga Receipt para sa Multi-Step Agents

Isang signed receipt lang ang nagpoprotekta sa isang aksyon. Isang chain ng mga receipt ang nagpoprotekta sa isang sunod-sunod na pangyayari.

```mermaid
flowchart LR
    R0[Resibo 0<br/>pinagmulan] --> R1[Resibo 1]
    R1 --> R2[Resibo 2]
    R2 --> R3[Resibo 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

Nire-record ng bawat receipt ang hash ng naunang receipt. Para tahimik na alisin ang receipt 2, kailangan ng umaatake na:

- Baguhin ang field na `previous_receipt_hash` ng receipt 3 (sisira sa lagda ni receipt 3), O
- Gumawa ng bagong lagda sa binagong receipt 3 (kailangan ang private key ng agent).

Kung ang private key ay nasa hardware key vault at ipinapublish mo ang public key kasama ng bawat receipt, hindi magagawa ang alin mang pag-atakeng ito nang hindi ito nadidiskubre.

Tinalakay sa notebook ang:

1. Pagbuo ng chain ng tatlong receipt.
2. Pag-verify na tugma ang `previous_receipt_hash` ng bawat receipt sa totoong hash ng naunang receipt.
3. Pagmanipula ng isang receipt sa gitna at pagtingin ng pagkabungkag ng chain sa puntong iyon.

Ganito gumagawa ng audit trail na maaring i-verify ng external auditor nang hindi kailangan magtiwala sa iyo.

## Ano ang Pinatutunayan ng Mga Receipt (at Ano ang Hindi)

Ito ang pinakamahalagang bahagi ng leksyon na ito. Malakas ang mga receipt ngunit may hangganan ang kanilang kapangyarihan.

**Tatlong bagay ang pinatutunayan ng mga receipt:**

1. **Pagkilala (Attribution)**: isang tukoy na key ang pumirma sa isang partikular na payload.
2. **Integridad (Integrity)**: hindi nagbago ang payload mula nang mapirmahan.
3. **Pagkakasunod-sunod (Ordering)**: ang receipt na ito ay sumunod sa receipt na iyon sa hash chain.

**Hindi pinatutunayan ng mga receipt:**

1. **Katumpakan (Correctness)**: na ang aksyon ng agent ay ang tamang aksyon. Maaaring pumirma ang receipt para sa maling sagot nang kasing linaw ng tamang sagot.
2. **Pagsunod sa polisiya (Policy compliance)**: na ang polisiya na tinukoy sa `policy_id` ay talagang nasuri, o na papayagan nito ang aksyon kung sinuri. Nagrerecord ang receipt kung ano ang inangkin, hindi kung ano ang ipinagpatupad.
3. **Pagkakakilanlan lampas sa key**: sinasabi ng receipt na "nilagdaan ng key na ito ang nilalamang ito." Hindi nito sinasabi na "inaprubahan ito ng tao." Ang pag-uugnay ng key sa tao o organisasyon ay nangangailangan ng hiwalay na identity infrastructure (directory, public key registry, atbp.).
4. **Katotohanan ng mga input**: kung makatanggap ang agent ng manipulated prompt at kumilos base rito, tapat na nire-record ng receipt ang aksyon. Ang mga receipt ay downstream ng input validation, hindi kapalit nito.

Mahalaga ang hangganang ito sa dalawang dahilan:

- Sinasabi nito kung para saan kapaki-pakinabang ang mga receipt: para gawing ma-audit at tamper-evident ang pag-uugali ng agent, kahit sa pagitan ng mga organisasyon.
- Sinasabi nito kung anong karagdagang layer pa ang kailangan: input validation (Leksiyon 6), pagpapatupad ng polisiya (talakayin sa ibaba), at identity infrastructure (hindi sakop ng leksyon na ito).

Isang karaniwang pagkakamali ang isipin na kapag "may mga receipt tayo" ay nangangahulugang "tayo ay pinamamahalaan." Hindi iyon totoo. Ang mga receipt ay pundasyon lamang. Ang pamamahala ay ang sistemang itinatayo mo sa ibabaw nito.

## Patunayan na Inaprubahan ng Tao ang Eksaktong Aksyon

Ang Item 3 sa itaas ay karapat-dapat ng sarili nitong seksyon: sinasabi ng action receipt na "nilagdaan ng key na ito ang nilalamang ito," hindi kailanman na "inaprubahan ito ng tao." Para sa mga high-risk na aksyon (refunds, deletions, wire transfers), mas lalong kailangan ito sa mga governance frameworks, at maaaring gawin gamit ang parehong primitives na itinuro sa leksyon na ito.

Ang susunod na notebook `code_samples/human-authorization-receipts.ipynb` ay nagdadagdag ng pangalawang uri ng receipt, `human.approval.v1`, sa parehong envelope na hugis ng mga receipt sa leksyon (isang typed payload na nilagdaan ng Ed25519 sa canonical SHA-256 nito, na may `signature` object na nasa labas ng signed bytes). Isang pinangalanang approver ang pumipirma sa **buong canonical action at ang digest nito** bago ito isagawa; ang action receipt ng agent ay nagdadala ng **katulad na action digest** at isang `parent_approval_ref`, ang `receipt_hash` ng approval, ang parehong convention tulad ng `previous_receipt_hash` sa chain na ginawa mo kanina. Isang `verify_chain` ang dumaraan sa parehong artifacts sa ilalim ng **hiwalay na pinned key registries** (approver keys vs agent keys), kaya magkapareho ang code path pero hindi nagsasama ang mga awtoridad.

Ang property na nabibili nito, maingat na sinabi: *inaprubahan ng tao ang eksaktong aksyon na ito, at ang agent ay isinagawa ang eksaktong inaprubahang aksyon.* Ang mga refusal fixtures sa notebook ang nagpapatunay ng property na ito, hindi lang basta pahayag:

- ang klasikong set: pagmanipula, confused deputy, replay, forged keys sa alinmang panig, malformed input;
- **stale authority**: isang lagda na nagpapakita pa rin ng bisa, ngunit tinanggihan dahil lumipat ang bersyon ng polisiya, na-rota ang approver key sa pinned registry, o nag-expire ang approval bago ang execution;
- **digest substitution**: isang valid na signed action receipt na tumutukoy sa isang *tunay* na approval na naka-bind sa isang *ibang* canonical action.

Bawat pagkabigo ay tinatanggihan gamit ang kakaibang dahilan, kaya ang auditor na bumabasa ng refusal ay makakaalam kung ang authority ay nag-stale o nagbago ang isinagawang aksyon. Ang patakarang itinuro ng notebook: ang isang signed approval ay hindi awtoridad mag-isa. May awtoridad lang kung ang parehong receipts ay naka-bind pa rin sa parehong canonical action sa panahon ng pag-execute. Ang co-signature path sa parehong Internet-Draft na sinusundan ng leksyon na ito (`draft-farley-acta-signed-receipts`) ay ang standards-track na hugis ng pattern na ito.

## Mga Sanggunian sa Produksyon

Ang Python code sa leksyon na ito ay sadyang minimal para mabasa mo ang bawat linya at maintindihan nang eksakto ang nangyayari. Sa produksyon, may dalawang opsyon ka:

1. **Direct na gamitin ang cryptographic primitives.** Ang 50 linya na nakita mo sa itaas ay sapat para sa maraming use case. Ang PyNaCl (Ed25519) at ang `jcs` package (canonical JSON) ay maayos ang maintenance at audited na mga library.

2. **Gumamit ng production receipt library.** Ilang open-source projects ang nagpapatupad ng parehong pattern na may karagdagang features (key rotation, batch verification, JWK Set distribution, integrasyon sa mga policy engine):
   - Ang format ng receipt na ginamit sa leksyon na ito ay sumusunod sa isang IETF Internet-Draft ([`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/), revision 02) na kasalukuyang nasa proseso ng standardization, na may shared conformance suite ([agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors)) na pinapatunayan ng mga independent implementations para sa byte-identical canonical output.
   - Ang Microsoft Agent Governance Toolkit ay kumokombina ng mga receipt sa mga Cedar-based policy decisions; tingnan ang Tutorial 33 sa repository na iyon para sa end-to-end na halimbawa.
   - Ang `protect-mcp` (npm) at `@veritasacta/verify` (npm) packages ay nagbibigay ng Node-based implementation ng receipt signing at offline verification, para balutin ang anumang MCP server na may tamper-evident audit trail, kabilang ang held-for-co-sign flow kung saan ang naka-pause na aksyon ay naglalabas ng approval receipt na naka-bind sa action digest (WebAuthn-backed sa desktop flow), katulad ng approval-receipt pattern sa human-authorization notebook sa itaas.
   - Ang **[nobulex](https://github.com/arian-gogani/nobulex)** Python SDK (`pip install nobulex`) ay nagbibigay ng parehong Ed25519 + JCS signing pattern sa Python na may LangChain at CrewAI integrations, kabilang ang na-publish na cross-validation test vectors at compliance mapping na nilikha sa pamamagitan ng [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210).

Ang desisyon sa pagitan ng pagbuo ng sarili o paggamit ng library ay tulad ng desisyon sa pagitan ng pagsulat ng sarili mong JWT library o paggamit ng isang nasubukan na: parehong makatwiran; nakakatipid sa oras at nagpapababa ng audit surface ang library; pinipilit kang intindihin ang bawat primitive kapag sarili ang gawa. Itinuturo ng leksyon na ito ang manual na pamamaraan para may pundasyon ka sa alinman sa pagpili.

## Pagsusulit sa Kaalaman

Subukan ang iyong pagkaunawa bago lumipat sa praktikal na ehersisyo.

**1. Ang receipt ay nilagdaan gamit ang private Ed25519 key ng agent. Ang auditor ay may public key lang. Maaari bang ma-verify ng auditor ang receipt offline?**

<details>
<summary>Sagot</summary>

Oo. Kinakailangan lamang ng Ed25519 verification ang public key at ang signed bytes. Walang network call, walang dependency sa serbisyo. Ito ang katangian na nagpapakinabang sa mga receipt sa mga air-gapped, multi-organization, o mababang-trust audit na mga sitwasyon.
</details>

**2. Binago ng isang umaatake ang field na `policy_id` ng isang receipt upang i-claim na ito ay pinamamahalaan ng mas paluwag na polisiya. Ang lagda ay nasa orihinal na payload. Ano ang mangyayari sa verification?**

<details>
<summary>Sagot</summary>


Nabigo ang beripikasyon. Ang lagda ay kinompyut sa canonical bytes ng orihinal na payload; ang pagbabago ng kahit anong field ay nagbabago sa canonical bytes, na nagbabago sa SHA-256 hash, na nagiging sanhi upang maging hindi wasto ang lagda. Kailangang may hawak ang attacker ng private key upang makagawa ng bagong wastong lagda, na wala sila.
</details>

**3. Bakit ang resibo ay naglalaman ng `tool_args_hash` at `result_hash` sa halip na ang mga raw na argumento at resulta?**

<details>
<summary>Sagot</summary>

Dalawang dahilan. Una, maaaring kailangang i-archive o ipadala ang resibo sa mga kapaligiran kung saan isang problema ang pag-leak ng raw na nilalaman (PII, business data). Pinananatiling maliit at pribado ng pag-hash ang resibo; sine-secure ng auditor na tumutugma ang hash sa isang hiwalay na naka-imbak na kopya ng aktwal na nilalaman. Pangalawa, may fixed size ang mga hash; ang isang resibo na may mga hash ay may hangganan sa laki anuman ang laki ng mga input at output.
</details>

**4. Ang `previous_receipt_hash` na field ay nag-uugnay sa bawat resibo sa nauna nito. Kung tahimik na burahin ng isang attacker ang isang resibo mula sa gitna ng chain, ano ang nagiging hindi wasto?**

<details>
<summary>Sagot</summary>

Bawat resibo na sumunod sa naburang isa. Ang kanilang mga `previous_receipt_hash` na mga field ay hindi na tumutugma sa aktwal na chain (dahil ang resibo na tinutukoy nila ay hindi na umiiral, o ang chain ay tumuturo ngayon sa ibang nauna). Upang itago ang pagtanggal, kailangan ng attacker na muling pirmahan ang bawat sumunod na resibo, na nangangailangan ng private key.
</details>

**5. Ang isang resibo ay beripikadong malinis. Napatunayan ba nito na tama, matibay, o sumusunod sa patakaran ang aksyon ng ahente?**

<details>
<summary>Sagot</summary>

Hindi. Ang isang valid resibo ay nagpapatunay ng tatlong bagay: attribution (ang susi na ito ang pumirma sa nilalaman), integridad (ang nilalaman ay hindi nagbago), at pag-uugma ng pagkakasunod (dumating ang resibo pagkatapos ng isa pa). HINDI nito pinatutunayan na tama ang aksyon, na tunay na nasuri ang patakaran sa `policy_id`, o na sinusunod ng ahente ang bawat alituntunin. Ginagawa ng mga resibo na masusuri ang gawi ng ahente, hindi kinakailangang tama. Ito ang pinakamahalagang hangganan sa aralin.
</details>

## Magsanay na Pagsasanay

Buksan ang `code_samples/18-signed-receipts.ipynb` at tapusin ang apat na seksyon:

1. **Seksiyon 1**: Pirmahan ang iyong unang resibo at beripikahin ito.
2. **Seksiyon 2**: Baguhin ang resibo at obserbahan ang pagkabigo sa beripikasyon.
3. **Seksiyon 3**: Bumuo ng isang tatlong-resibo na chain at beripikahin ang integridad ng chain.
4. **Seksiyon 4**: I-apply ang pattern sa isang ahente na binuo gamit ang Microsoft Agent Framework: balutin ang pagtawag sa tool sa pag-pirma ng resibo, pagkatapos beripikahin ang resibo nang magkahiwalay.

**Stretch challenge 1:** palawakin ang schema ng resibo gamit ang karagdagang field na iyong pinili (halimbawa, isang request ID para sa tracing), i-update ang canonical signing logic upang isama ito, at kumpirmahing dumadaan pa rin ang resibo sa verification. Pagkatapos baguhin ang field matapos pirmahan at kumpirmahing mabibigo ang verification. Pinipilit ka nitong maintindihan kung paano ang bawat byte ng canonical encoding ay nag-aambag sa lagda.

**Stretch challenge 2:** I-SHA-256 hash ang dalawa sa iyong mga resibo nang magkakasama (ikabit ang canonical bytes nila sa deterministic na pagkakasunod) at i-embed ang nagresultang digest bilang bagong field sa ikatlong resibo bago ito pirmahan. Beripikahin na tatlo pa rin ang dumadaan sa round-trip. Nakagawa ka lang ng one-step inclusion proof: kahit sino na may hawak ng ikatlong resibo ay maaaring patunayan na ang unang dalawa ay umiiral noong pinirmahan ito, nang hindi kailangang isiwalat ang kanilang nilalaman. Ito ang pattern na ginagamit ng selective-disclosure receipts sa malawakang paggamit (Merkle commitments, RFC 6962).

## Konklusyon

Nagbibigay ang cryptographic receipts ng audit trail para sa mga AI agent na:

- **Independently verifiable**: anumang partido na may public key ay maaaring mag-verify, walang dependency sa serbisyo.
- **Tamper-evident**: anumang pagbabago ay nagpapawalang-bisa sa lagda.
- **Portable**: ang resibo ay isang maliit na JSON na file; maaaring i-archive, ipadala, at beripikahin kahit saan.
- **Standards-aligned**: naka-base sa Ed25519 (RFC 8032), JCS (RFC 8785), at SHA-256, lahat ay malawak na ginagamit na mga primitive.

Hindi sila kapalit ng input validation, pagpapatupad ng patakaran, o identity infrastructure. Sila ay pundasyon para sa mga layer na iyon. Kapag nagde-deploy ka ng mga agent sa regulated workloads, multi-organization workflows, o kahit anong setting kung saan hindi maaaring ipagpalagay ang pagtitiwala ng isang hinaharap na auditor, ang mga resibo ang nagpapakatotoo sa audit trail.

Ang pinakamahalagang takeaway: pinatutunayan ng mga resibo kung sino ang nagsabi ng ano, kailan. Hindi nila pinatutunayan na ang nasabi ay totoo o tama. Hawakan nang mahigpit ang pagkakaibang iyon. Ito ang pagkakaiba sa pagitan ng isang tapat na sistema ng pinagmulan at isang nakalilito.

## Production Checklist

Kapag handa ka nang magtapos sa araling ito para mag-deploy ng receipt-signed agents sa totoong kapaligiran:

- [ ] **Ilipat ang signing key mula sa developer laptop.** Gamitin ang Azure Key Vault, AWS KMS, o hardware security module. Ang private key na pumipirma sa iyong mga resibo ay hindi kailanman dapat manatili sa source control o plaintext sa mga makina ng aplikasyon.
- [ ] **I-publish ang verification public key.** Kailangan ito ng mga auditor upang mag-verify offline. Ang karaniwang pattern ay isang JWK Set sa isang kilalang URL (RFC 7517), e.g., `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **I-anchor ang chain sa labas.** Paminsan-minsan isulat ang pinakabagong hash ng chain head sa isang transparency log (Sigstore Rekor, RFC 3161 timestamp authority, o isang pangalawang internal na sistema) para mapatunayan ng panlabas na partido na "umiiral ang chain na ito sa oras na ito."
- [ ] **Itago ang mga resibo nang hindi nababago.** Ang append-only blob storage (Azure Storage na may immutability policies, AWS S3 Object Lock) ay pumipigil sa isang insider na baguhin ang kasaysayan sa storage layer.
- [ ] **Magdesisyon sa retention.** Maraming compliance regime ang nangangailangan ng multi-taong retention. Magplano para sa paglago ng resibo (bawat resibo ay ~500 bytes; isang agent na gumagawa ng 10K calls bawat araw ay gumagawa ng ~1.8 GB bawat taon).
- [ ] **Idokumento kung ano ang hindi sakop ng mga resibo.** Pinatutunayan ng mga resibo ang attribution, integridad, at pag-uugma ng pagkakasunod. Dapat na nakalista nang malinaw sa iyong runbook kung ano pang mga kontrol (input validation, pagpapatupad ng patakaran, rate limiting, identity infrastructure) ang kasama ng mga resibo sa iyong governance posture.

### May Karagdagang Tanong Tungkol sa Pag-secure ng AI Agents?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Lampas sa Araling Ito

Tinatakpan ng araling ito ang single-receipt signing at hash-chained sequences. Ang parehong mga primitives ay bumubuo ng ilang mas advanced na mga pattern na maaari mong makita habang umuunlad ang iyong governance posture:

- **Selective disclosure.** Kapag ang mga field ng resibo ay independiyenteng naka-commit (RFC 6962-style Merkle tree), maaari mong ibunyag ang mga espesipikong field sa mga espesipikong auditor at patunayan na hindi nagbago ang iba nang hindi isiniwalat ang mga ito. Kapaki-pakinabang kapag ang parehong resibo ay kailangang matugunan ang isang komprehensibong audit (na gusto ang kumpletong detalye) at regulasyon sa data-minimization tulad ng GDPR (na gustong makita ng auditor ang kaunti lang hangga't maaari).
- **Receipt revocation.** Kung ang isang signing key ay nangyariang kompromiso, kailangan mo ng paraan para markahan ang lahat ng mga resibo na pinirmahan ng key na iyon bilang hindi mapagkakatiwalaan mula sa isang punto ng oras pasulong. Karaniwang mga pattern: panandaliang signing keys plus isang inilathalang revocation list, o isang transparency log na may mga revocation entry.
- **Bilateral / split-signature receipts.** Ang ilang mga implementasyon ay naghahati sa signed payload sa pre-execution (`authorization_*`) at post-execution (`result_*`) mga bahagi na may independiyenteng mga lagda, kapaki-pakinabang kapag ang desisyong Otorizasyon at ang naobserbahang resulta ay ginawa ng magkaibang mga aktor o sa magkaibang oras. Ito ay idinadagdag sa pormat ng resibo na itinuro sa araling ito.
- **Payload composition.** Naka-seal ng resibo ang anumang bytes na inilalagay mo sa `result_hash`. Ang mga real-world payload ay madalas na mas mayaman kaysa isang tool call result lamang: ang pre-decision reasoning (model prediction, mga opsyon na isinasaalang-alang, ebidensya at ang pagiging kumpleto nito, risk posture, chain ng accountability, resulta ng gate) ay maaaring lahat nakapaloob sa payload, na naka-seal ng isang solong resibo. Pinananatili nito ang minimal na pormat ng resibo habang pinapayagan ang mga schema ng payload na umunlad bawat domain.
- **Cross-implementation conformance.** Maraming independiyenteng implementasyon ng parehong pormat ng resibo (Python, TypeScript, Rust, Go) ay nagko-cross-verify laban sa mga shared test vectors. Kapag bumuo ka ng sarili mong implementasyon, ang pag-validate gamit ang mga publishing vectors ay nagpapatunay ng wire compatibility.
- **Post-quantum migration.** Ang Ed25519 ay malawakang ginagamit ngayon ngunit hindi ito quantum-resistant. Ang pormat ng resibo ay algorithm-agile: ang `signature.alg` na field ay maaaring magdala ng `ML-DSA-65` (ang NIST post-quantum signature standard) kapag kailangan mong mag-migrate. Magplano para sa isang panahong paglilipat kung saan ang mga resibo ay dual-signed.

## Mga Karagdagang Mapagkukunan

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF Internet-Draft: Signed Decision Receipts for Machine-to-Machine Access Control</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785: JSON Canonicalization Scheme (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962: Certificate Transparency</a> (Merkle-tree construction used by selective-disclosure receipts)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, Tutorial 33: Offline-Verifiable Decision Receipts</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">Cross-implementation conformance test vectors</a> para sa pormat ng resibo na ginamit sa araling ito (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl documentation</a> (Ed25519 sa Python)

## Nakaraang Aralin

[Creating Local AI Agents](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->