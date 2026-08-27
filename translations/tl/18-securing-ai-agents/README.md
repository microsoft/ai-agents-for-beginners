[Panoorin ang video ng leksyon: Pag-secure ng AI Agents gamit ang Cryptographic Receipts](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Ang video ng leksyon at thumbnail ay ida-download ng Microsoft content team pagkatapos ng pagsasama, na tugma sa pattern ng leksyon 14 / 15.)_

# Pag-secure ng AI Agents gamit ang Cryptographic Receipts

## Panimula

Tatalakayin ng leksyon na ito:

- Bakit mahalaga ang audit trails para sa mga AI agent para sa pagsunod, debugging, at pagtitiwala.
- Ano ang cryptographic receipt at paano ito naiiba sa unsigned log line.
- Paano gumawa ng signed receipt para sa tool call ng agent gamit ang plain Python.
- Paano mag-verify ng receipt offline at matukoy ang pamemeke.
- Paano mag-chain ng mga receipt upang kapag tinanggal o ni-reorder ang isa ay masira ang chain.
- Ano ang pinatutunayan ng mga receipt at ano ang hindi nila pinatutunayan nang tahasan.

## Mga Layunin sa Pagkatuto

Pagkatapos tapusin ang leksyon na ito, malalaman mo kung paano:

- Tukuyin ang mga failure modes na nagtutulak sa cryptographic provenance para sa mga kilos ng agent.
- Gumawa ng Ed25519-signed receipt gamit ang canonical JSON payload.
- Mag-verify ng receipt nang independyente gamit lamang ang pampublikong susi ng signer.
- Matukoy ang pamemeke sa pamamagitan ng muling pag-verify ng binagong receipt.
- Bumuo ng hash-chained na sunud-sunod na mga receipt at ipaliwanag kung bakit mahalaga ang chain.
- Kilalanin ang hangganan ng kung ano ang pinatutunayan ng mga receipt (attribution, integridad, ordering) at kung ano ang hindi nila pinatutunayan (katumpakan ng aksyon, kapanatagan ng patakaran).

## Ang Problema: Audit Trail ng Iyong Agent

Isipin na nag-deploy ka ng isang AI agent para sa Contoso Travel. Binabasa ng agent ang mga kahilingan ng customer, tumawag sa flights API upang maghanap ng mga opsyon, at nagbu-book ng mga upuan para sa customer. Noong nakaraang quarter, nakaproseso ang agent ng 50,000 bookings.

Ngayon ay dumating ang isang auditor. Nagtanong siya ng simpleng tanong: "Ipakita ninyo sa akin ang ginawa ng inyong agent."

Ibinigay mo ang mga log file mo. Tiningnan ito ng auditor at nagtanong ng mas mahirap na tanong: "Paano ko malalaman na hindi na-edit ang mga logs na ito?"

Ito ang problema sa audit trail. Karamihan sa mga deployment ng agent ngayon ay umaasa sa:

- **Mga application log**: isinusulat ng agent mismo, pwedeng i-edit ng sinumang may access sa file system.
- **Mga cloud logging service**: tamper-evident sa level ng platform pero lamang kung nagtitiwala ang auditor sa operator ng platform.
- **Mga database transaction log**: mainam para sa mga pagbabago sa database ngunit hindi para sa arbitrary tool calls.

Wala sa mga ito ang makakasagot sa tanong ng auditor nang hindi siya umaasa sa isang tao (ikaw, ang iyong cloud provider, ang iyong database vendor). Para sa internal na gamit, kadalasan ay katanggap-tanggap ang tiwala na iyon. Para sa mga regulated workload (finance, healthcare, anumang sakop ng EU AI Act), hindi ito sapat.

Nilulutas ng cryptographic receipts ito sa pamamagitan ng paggawa ng bawat aksyon ng agent na independently verifiable. Hindi kailangang magtiwala ang auditor sa iyo. Kailangan nila lamang ang iyong public key at ang receipt.

## Ano ang Cryptographic Receipt?

Ang receipt ay isang JSON object na nagrerekord kung ano ang ginawa ng agent, na nilagdaan gamit ang digital signature.

```mermaid
flowchart LR
    A[Ang ahente ay nagpapagana ng isang tool] --> B[Bumuo ng payload ng resibo]
    B --> C[I-canonicalize ang JSON RFC 8785]
    C --> E[Ed25519 lagdaan ang mga canonical na byte]
    E --> F[Resibo na may lagda]
    F --> G[Sinusuri ng auditor sa offline]
    G --> H{Valid ba ang lagda?}
    H -- yes --> I[Patunay na hindi na-tamper]
    H -- no --> J[Tinanggihan ang resibo]
```

Ang pinakamababang receipt ay ganito:

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

Tatlong katangian ang gumagana:

1. **Ang lagda**. Nilalagdaan ang receipt ng gateway ng agent gamit ang Ed25519 private key. Sinumang may kaukulang public key ay maaaring mag-verify ng lagda offline. Ang pagmanipula sa kahit anong field ay nagpapawalang-saysay sa lagda.

2. **Canonical encoding**. Bago lagdaan, isinasalarawan ang receipt gamit ang JSON Canonicalization Scheme (JCS, RFC 8785). Sinisiguro nito na ang dalawang implementasyon na gumagawa ng parehong lohikal na receipt ay gumagawa ng byte-identical na output. Kung walang canonicalization, magkakaiba ang magiging lagda para sa parehong laman kapag iba-ibang JSON serializer ang ginamit.

3. **Hash chaining**. Ang field na `previous_receipt_hash` ay nag-uugnay ng bawat receipt sa naunang isa. Ang pagtanggal o pagre-reorder ng isang receipt ay sisira sa lahat ng mga receipt pagkatapos nito. Nagiging halata ang pamemeke sa level ng chain kahit bypass ang mga indibidwal na lagda.

Pinagsama-samang nagbibigay ang mga katangiang ito ng tatlong garantiya:

- **Attribution**: ang key na ito ang pumirma sa nilalaman.
- **Integridad**: hindi nagbago ang nilalaman mula nang pirmahan.
- **Pagkakasunod-sunod**: ang receipt na ito ay sumunod sa receipt na iyon sa chain.

## Paggawa ng Receipt sa Python

Hindi mo kailangang gumamit ng espesyal na library para gumawa ng receipt. Malawak ang pagkakaroon ng cryptographic primitives at ilang dosenang linya lang ng Python ang kailangan.

Ang mga hands-on exercise sa `code_samples/18-signed-receipts.ipynb` ay nagpapakita ng buong proseso. Ang maikling bersyon:

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

# Bumuo o mag-load ng signing key (sa produksyon, itago sa isang key vault)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# Bumuo ng payload ng resibo (wala pang pirma)
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

# I-canonicalize at pirmahan nang direkta ang mga byte ng JCS. PureEdDSA ang naga-hash nang internal.
canonical_bytes = canonicalize(payload)
signature_bytes = signing_key.sign(canonical_bytes).signature

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

Iyan ang buong signing pipeline. Pinapakita ng mga exercise sa notebook ang bawat hakbang.

## Pag-verify ng Receipt at Pagtukoy ng Pamemeke

Ang verification ay ang kabaligtaran na operasyon:

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
    # Ang lagda ay isang nakabalangkas na bagay: {"alg", "sig", "public_key"}.
    sig_obj = receipt.get("signature")
    if not sig_obj or sig_obj.get("alg") != "EdDSA":
        return False

    # Ibalik ang payload na talagang nilagdaan (lahat maliban sa lagda).
    payload = {k: v for k, v in receipt.items() if k != "signature"}

    canonical_bytes = canonicalize(payload)

    try:
        verify_key = signing.VerifyKey(b64url_decode(sig_obj["public_key"]))
        verify_key.verify(canonical_bytes, b64url_decode(sig_obj["sig"]))
        return True
    except BadSignatureError:
        return False
```

Tumatanggap ang function na ito ng receipt at nagbabalik ng `True` kung valid ang lagda, `False` kung hindi. Walang network call, walang apela sa serbisyo, walang kailangan na tiwala sa ibang partido.

Upang makita ang pagtukoy ng pamemeke sa aksyon, pinapakita ng notebook:

1. Paggawa ng valid na receipt at pagsigurong ito ay nage-verify.
2. Pagbabago ng isang byte sa field na `tool_args_hash`.
3. Muling pagpapatakbo ng verification at nakikitang pumalya ito.

Ito ang praktikal na demonstrasyon na ang mga receipt ay tamper-evident: anumang pagbabago, kahit maliit lang, ay sisira sa lagda.

## Pag-chain ng Mga Receipt para sa Multi-Step Agents

Isang signed receipt ang nagpoprotekta sa isang aksyon. Ang chain ng mga receipt ang nagpoprotekta sa isang sunud-sunod na aksyon.

```mermaid
flowchart LR
    R0[Resibo 0<br/>simula] --> R1[Resibo 1]
    R1 --> R2[Resibo 2]
    R2 --> R3[Resibo 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

Isinama ng bawat receipt ang hash ng naunang receipt. Para tanggalin nang tahimik ang receipt 2, kailangan ng umaatake na:

- Baguhin ang `previous_receipt_hash` ng receipt 3 (sisira sa lagda ng receipt 3), O
- Gumawa ng bagong lagda sa binagong receipt 3 (kailangan ang private key ng agent).

Kung ang private key ay nasa hardware key vault at inilalathala ang public key sa bawat receipt, walang feasible na atake nang hindi nadedetect.

Pinapakita ng notebook:

1. Pagbuo ng chain ng tatlong receipt.
2. Pag-verify na ang `previous_receipt_hash` ng bawat receipt ay tumutugma sa tamang hash ng naunang receipt.
3. Pagmanipula ng isang receipt sa gitna at makitang nasira ang chain sa eksaktong puntong iyon.

Ganito mo ginagawa ang audit trail na ma-pave na ma-verify ng external auditor nang hindi kailangan ng tiwala sa iyo.

## Ano ang Pinatutunayan ng Mga Receipt (at Ano ang Hindi)

Ito ang pinakamahalagang bahagi ng leksyon na ito. Malakas ang mga receipt ngunit may hangganan ang kanilang kapangyarihan.

**Tatlong bagay ang pinatutunayan ng mga receipt:**

1. **Attribution**: isang tiyak na key ang pumirma sa tiyak na payload.
2. **Integridad**: hindi nagbago ang payload mula nang pirmahan.
3. **Pagkakasunod-sunod**: ang receipt na ito ay sumunod sa receipt na iyon sa hash chain.

**Hindi pinatutunayan ng mga receipt:**

1. **Katumpakan**: na ang kilos ng agent ay tama. Maaaring pirmahan ang receipt para sa maling sagot nang kasing linaw ng para sa tamang sagot.
2. **Pagsunod sa patakaran**: na ang patakarang binanggit sa `policy_id` ay totoong na-evaluate, o na papayagan nito ang aksyon kung ito ay sinuri. Ipinapakita ng receipt kung ano ang sinabing ginawa, hindi kung ano ang ipinatupad.
3. **Pagkakakilanlan lampas sa key**: sinasabi ng receipt na "ang key na ito ang pumirma sa nilalaman na ito." Hindi nito sinasabi na "isang tao ang nag-authorize nito." Ang pagkonekta ng susi sa tao o organisasyon ay nangangailangan ng hiwalay na identity infrastructure (directory, public key registry, atbp.).
4. **Katotohanan ng input**: kung nakatanggap ang agent ng isang manipuladong prompt at kumilos dito, tapat na nire-record ng receipt ang aksyon. Ang mga receipt ay sumusunod sa input validation, hindi kapalit nito.

Mahalaga ang hangganang ito dahil sa dalawang dahilan:

- Sinasabi nito kung para saan kapaki-pakinabang ang mga receipt: para gawing auditable at tamper-evident ang kilos ng agent, kahit sa pagitan ng mga organisasyon.
- Sinasabi nito kung anong mga dagdag na layer pa ang kailangan mo: input validation (Leksiyon 6), pagpapatupad ng patakaran (banayad na tinalakay sa ibaba), at identity infrastructure (hindi saklaw ng leksyon na ito).

Karaniwang maling akala ang isipin na kapag "may mga receipt kami" ay "kami ay pinamamahalaan." Hindi ito totoo. Ang mga receipt ay pundasyon. Ang pamamahala ang sistemang itinatayo mo dito.

## Patunayan na Isang Tao ang Nag-apruba ng Eksaktong Aksyon

Mahalaga ang Item 3 sa itaas: sinasabi ng isang action receipt na "ang key na ito ang pumirma sa nilalaman na ito," hindi "isang tao ang nag-authorize nito." Para sa mga high-risk na aksyon (refund, deletion, wire transfer), mas madalas nang hinihingi ng mga governance framework ang eksaktong pahayag na iyon, at maaari itong gawin gamit ang parehong mga primitives na itinuro sa leksyon na ito.

Ang kasunod na notebook na `code_samples/human-authorization-receipts.ipynb` ay nagdadagdag ng pangalawang uri ng receipt, `human.approval.v1`, sa parehong envelope na hugis ng mga receipt sa leksyon (isang typed payload na nilagdaan gamit ang Ed25519 sa canonical na bytes ng JCS, na may `signature` object sa labas ng pinirmahang bytes). Ang isang pangalanadong approver ang pumipirma sa **buong canonical action at ang digest nito** bago ito isagawa; ang action receipt ng agent ay may dalang **parehong digest ng aksyon** at isang `parent_approval_ref`, ang `receipt_hash` ng approval, na katulad ng convention ng `previous_receipt_hash` sa chain na ginawa mo sa itaas. Isang `verify_chain` lang ang tumitingin sa parehong artifact gamit ang **magkaibang naka-pinned na key registry** (approver keys vs agent keys), kaya pareho ang code path pero hindi pinagsasama ang mga awtoridad.

Ang property na nakukuha dito, maingat na ipinapahayag: *inaprubahan ng tao ang eksaktong aksyon na ito, at tumpak na isinagawa ng agent ang aprubadong aksyon.* Ang mga refusal fixture sa notebook ang nagpapatunay na ito ay totoo at hindi lang panghihikayat:

- ang klasikong hanay: pamemeke, confused deputy, replay attack, pekeng susi sa magkabilang panig, mali ang format ng input;
- **stale authority**: lagdang patunay na valid pa ngunit tinanggihan dahil nagbago ang bersyon ng patakaran, nawala ang approver key sa pinned registry, o nag-expire ang approval bago isagawa;
- **digest substitution**: valid na lagdang action receipt na tumutukoy sa *tunay* na approval na nag-uugnay sa *ibang* canonical na aksyon.

Bawat failure ay tumatanggi gamit ang naiibang dahilan, kaya't ang auditor na nagbabasa ng refusal ay malalaman kung lumuma ang awtoridad o nagbago ang isinagawang aksyon. Ang regla na itinuturo ng notebook: ang signed approval ay hindi awtoridad sa sarili nito. Ang awtoridad ay umiiral lamang kung pareho pa ring naka-bind ang dalawang receipt sa parehong canonical na aksyon sa oras ng pagsasagawa. Ang human-approval receipt ay isang educational na kumbinasyon na itinakda ng leksyon na ito, hindi isang uri ng receipt na itinakda ng `draft-farley-acta-signed-receipts`.

## Mga Sanggunian sa Produksyon

Ang Python code sa leksyon na ito ay sadyang minimal upang mabasa mo ang bawat linya at maunawaan nang eksakto ang nagaganap. Sa produksyon, may dalawang opsyon ka:

1. **Magbuild nang direkta gamit ang cryptographic primitives.** Ang 50 linya na nakita mo sa itaas ay sapat na sa maraming kaso. Maayos na pinananatili at na-audit ang mga library na PyNaCl (Ed25519) at ang package na `jcs` (canonical JSON).

2. **Gumamit ng production receipt library.** Maraming open-source na proyekto ang nagpapatupad ng parehong pattern na may dagdag na mga tampok (key rotation, batch verification, JWK Set distribution, integrasyon sa policy engines):
   - Ang signing pipeline ay gumagamit ng JCS at signature-scope conventions sa isang independenteng IETF Internet-Draft ([`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/), revision 02). Ang flat educational receipt sa leksyon na ito ay naiiba sa draft `{payload, signature}` envelope at hindi ipinapakita bilang isang pormal na implementasyon. Naglalathala ang draft ng isang shared conformance suite ([agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors)) para sa mga implementasyon na tumutok sa wire format nito.
   - Ang Microsoft Agent Governance Toolkit ay gumagawa ng mga receipt na may Cedar-based policy decisions; tingnan ang Tutorial 33 sa repository na iyon para sa halimbawa mula simula hanggang katapusan.
   - Ang mga package na `protect-mcp` (npm) at `@veritasacta/verify` (npm) ay nagbibigay ng Node-based na implementasyon ng receipt signing at offline verification, na inilaan para sa pagsuporta ng MCP server na may tamper-evident audit trail, kabilang ang held-for-co-sign flow kung saan isang paused na aksyon ay gumagawa ng approval receipt na naka-bind sa action digest (WebAuthn-backed sa desktop flow), kapareho ng approval-receipt pattern sa human-authorization notebook sa itaas.
   - Ang **[nobulex](https://github.com/arian-gogani/nobulex)** Python SDK (`pip install nobulex`) ay nagbibigay ng parehong Ed25519 + JCS signing pattern sa Python na may LangChain at CrewAI integration, kabilang ang nalathalang cross-validation test vectors at compliance mapping na naambag sa pamamagitan ng [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210).

Ang pagpili sa pagitan ng paggawa ng sarili at paggamit ng library ay parang pagpili sa pagitan ng pagsusulat ng sariling JWT library at paggamit ng nasubok na library: parehong makatwiran; nakakatipid sa oras at nababawasan ang audit surface ang library; pinipilit ng from-scratch na paraan na maintindihan mo ang bawat primitive. Itinuturo ng leksyon na ito ang from-scratch na paraan para magkaroon ka ng pundasyon sa alinmang pipiliin mo.

## Pagsusulit sa Kaalaman

Subukan ang iyong pag-unawa bago magpatuloy sa practice exercise.

**1. Ang receipt ay nilagdaan gamit ang private Ed25519 key ng agent. Ang auditor ay hawak lamang ang public key. Maaari bang ma-verify ng auditor ang receipt offline?**

<details>
<summary>Sagot</summary>

Oo. Ang Ed25519 verification ay nangangailangan lamang ng public key at ng pinirmahang bytes. Walang network call, walang dependency sa serbisyo. Ito ang katangian na ginagawang kapaki-pakinabang ang mga receipt sa air-gapped, multi-organisasyon, o low-trust audit settings.
</details>

**2. Ang isang umaatake ay nagbago ng field na `policy_id` ng isang receipt upang ipahayag na ito ay sakop ng mas maluwag na patakaran. Ang lagda ay nasa orihinal na payload. Ano ang mangyayari sa pag-verify?**

<details>
<summary>Sagot</summary>


Nabigo ang beripikasyon. Ang lagda ay kinompyut sa canonical bytes ng orihinal na payload; ang pagbabago kahit anumang bahagi ay nagbabago ng mga byte na iyon, na ginagawang hindi wasto ang lagda. Kailangang magkaroon ng pribadong susi ang attacker para makagawa ng bagong wastong lagda, na wala sila.
</details>

**3. Bakit ang resibo ay naglalaman ng `tool_args_hash` at `result_hash` sa halip na mga raw na argumento at resulta?**

<details>
<summary>Sagot</summary>

Dalawang dahilan. Una, maaaring kailanganin ang resibo na ma-archive o maipadala sa mga kapaligirang kung saan ang pag-leak ng raw na nilalaman (PII, datos ng negosyo) ay isang problema. Pinananatili ng pag-hash na maliit ang resibo at pribado ang nilalaman; sinisigurado ng auditor na tumutugma ang hash sa hiwalay na naka-imbak na kopya ng aktwal na nilalaman. Pangalawa, ang mga hash ay may fixed na sukat; ang isang resibo na may mga hash ay may hangganan ang laki kahit gaano kalaki ang inputs at outputs.
</details>

**4. Ang field na `previous_receipt_hash` ay nag-uugnay sa bawat resibo sa naunang resibo nito. Kung tahimik na tatanggalin ng attacker ang isang resibo mula sa gitna ng chain, ano ang nagiging hindi wasto?**

<details>
<summary>Sagot</summary>

Bawat resibo na sumusunod pagkatapos ng tinanggal na resibo. Ang kanilang mga field na `previous_receipt_hash` ay hindi na tumutugma sa aktwal na chain (dahil ang resibo na kanilang dinaanan ay wala na, o ang chain ay tumuturo ngayon sa ibang nauna). Para maitago ang pagtanggal, kailangang muling pirmahan ng attacker ang bawat huling resibo, na nangangailangan ng pribadong susi.
</details>

**5. Ang isang resibo ay malinaw na nabeberipika. Napatutunayan ba nito na ang aksyon ng ahente ay tama, matatag, o alinsunod sa polisiya?**

<details>
<summary>Sagot</summary>

Hindi. Ang isang wastong resibo ay nagpapatunay ng tatlong bagay: atribusyon (ang susi na ito ang pumirma sa nilalamang ito), integridad (hindi nagbago ang nilalaman), at pagkakasunod-sunod (ang resibong ito ay dumating pagkatapos ng ibang resibo). HINDI nito pinatutunayan na tama ang aksyon, na ang polisiya na tinukoy sa `policy_id` ay talagang nasuri, o na sinunod ng ahente lahat ng patakaran. Ginagawa ng mga resibo na ma-audit ang kilos ng ahente, hindi kinakailangang tama. Ito ang pinakamahalagang hangganan sa aralin.
</details>

## Praktis na Ehersisyo

Buksan ang `code_samples/18-signed-receipts.ipynb` at tapusin ang lahat ng apat na bahagi:

1. **Bahagi 1**: Pirmahan ang iyong unang resibo at beripikahin ito.
2. **Bahagi 2**: Gambalain ang resibo at obserbahan ang pagkabigo sa beripikasyon.
3. **Bahagi 3**: Gumawa ng tatlong-resibo na chain at beripikahin ang integridad ng chain.
4. **Bahagi 4**: I-apply ang pattern sa isang ahenteng ginawa gamit ang Microsoft Agent Framework: i-wrap ang pagtawag ng tool sa paglagda ng resibo, pagkatapos ay beripikahin ang resibo nang hiwalay.

**Hamong palawakin 1:** palawakin ang schema ng resibo gamit ang panibagong field na pinili mo (halimbawa, isang request ID para sa pagsubaybay), i-update ang canonical signing logic upang isama ito, at tiyaking maibabalik pa rin ang resibo sa beripikasyon. Pagkatapos ay baguhin ang field pagkatapos ng paglagda at tiyaking mabibigo ang beripikasyon. Pinipilit kang maintindihan kung paano nakakatulong bawat byte ng canonical encoding sa lagda.

**Hamong palawakin 2:** i-SHA-256 hash ang dalawa sa iyong mga resibo na magkakasama (pagdugtungin ang kanilang mga canonical bytes sa isang deterministikong pagkakasunod) at i-embed ang nagresultang digest bilang panibagong field sa pangatlong resibo bago pirmahan. Beripikahin na lahat ng tatlong resibo ay maibabalik pa rin. Nakagawa ka lang ng isang one-step inclusion proof: sinumang may hawak ng pangatlong resibo ay maaaring patunayan na umiiral ang unang dalawang resibo noong pinirmahan ito, nang hindi isiniwalat ang kanilang mga nilalaman. Ito ang pattern na ginagamit ng mga selective-disclosure receipts sa malaking sukat (Merkle commitments, RFC 6962).

## Konklusyon

Ang mga cryptographic na resibo ay nagbibigay sa mga AI agent ng audit trail na:

- **Nababeripika nang independyente**: kahit sino na may public key ay maaaring magberipika, walang dependency sa serbisyo.
- **Tamper-evident**: anumang pagbabago ay nagiging sanhi ng hindi bisa ng lagda.
- **Portatile**: ang resibo ay isang maliit na JSON file; maaari itong i-archive, ipadala, at beripikahin kahit saan.
- **Alinsunod sa mga pamantayan**: nakabatay sa Ed25519 (RFC 8032), JCS (RFC 8785), at SHA-256, na mga malawak na ginagamit na primitives.

Hindi ito kapalit ng input validation, pagpapatupad ng polisiya, o identity infrastructure. Ito ay pundasyon para sa mga layer na iyon. Kapag nagdedeploy ng mga ahente sa mga regulated workloads, multi-organization workflows, o anumang sitwasyon na hindi dapat pagkatiwalaan ng auditor sa hinaharap, ang mga resibo ang paraan upang gawing tapat ang audit trail.

Ang pinakamahalagang takeaway: pinatutunayan ng mga resibo kung sino ang nagsabi ng ano, kailan. Hindi pinatutunayan na ang sinabi ay totoo o tama. Panatilihin ang distinksyong iyon nang mahigpit. Ito ang pagkakaiba sa pagitan ng isang tapat na provenance system at isang nakalilinlang.

## Checklist para sa Produksyon

Kapag handa ka nang lumipat mula sa araling ito papuntang pag-deploy ng mga agent na may pirmahang resibo sa totoong kapaligiran:

- [ ] **Ilipat ang signing key mula sa developer laptop.** Gumamit ng Azure Key Vault, AWS KMS, o hardware security module. Ang pribadong susi na pumipirma sa mga resibo mo ay hindi dapat mabuhay sa source control o nakalantad na plaintext sa makina ng aplikasyon.
- [ ] **I-publish ang verification public key.** Kailangan ito ng mga auditor para mag-verify offline. Ang karaniwang pattern ay isang JWK Set sa kilalang URL (RFC 7517), hal., `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **Ilakip ang anchor ng chain sa labas.** Paminsan-minsang isulat ang pinakabagong chain head hash sa transparency log (Sigstore Rekor, RFC 3161 timestamp authority, o ikalawang internal na sistema) upang makumpirma ng panlabas na partido "umiiral ang chain na ito sa panahong ito."
- [ ] **Itago ang mga resibo nang hindi nababago.** Ang append-only blob storage (Azure Storage na may immutability policies, AWS S3 Object Lock) ay pumipigil sa mga insider na baguhin ang kasaysayan sa storage layer.
- [ ] **Magdesisyon sa retention.** Maraming compliance regime ang nangangailangan ng multi-taong retention. Planuhin ang paglago ng resibo (bawat resibo ay ~500 bytes; ang isang ahente na gumagawa ng 10K na tawag kada araw ay gumagawa ng ~1.8 GB kada taon).
- [ ] **Idokumento kung ano ang hindi sakop ng mga resibo.** Pinapatunayan ng mga resibo ang atribusyon, integridad, at pagkakasunod-sunod. Dapat malinaw kang maglista sa iyong runbook kung anu-anong karagdagang kontrol (input validation, pagpapatupad ng polisiya, rate limiting, identity infrastructure) ang kasabay ng mga resibo sa iyong governance posture.

### May mga Karagdagang Tanong tungkol sa Pagse-secure ng AI Agents?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) para makipagkita sa ibang mag-aaral, dumalo sa office hours, at makuha ang mga sagot sa iyong mga tanong tungkol sa AI Agents.

## Lampas sa Araling Ito

Tinutugunan ng araling ito ang single-receipt signing at mga hash-chained na sunod-sunod. Ang parehong mga primitives ay bumubuo ng ilang mas advanced na mga pattern na maaaring matagpuan habang lumalalim ang iyong governance posture:

- **Selective disclosure.** Kapag ang mga field ng resibo ay independyenteng nakalaan (RFC 6962-style Merkle tree), maaari mong ibunyag ang mga tiyak na field sa mga tiyak na auditor at patunayan na hindi nagbago ang iba nang hindi isiniwalat ang mga ito. Kapaki-pakinabang kapag ang parehong resibo ay kailangang masiyahan sa parehong komprehensibong audit (na gusto ng kompletong impormasyon) at mga regulasyon ng data-minimization tulad ng GDPR (na gusto ng auditor na makita ang kaunti lang).
- **Receipt revocation.** Kapag ang signing key ay na-compromise, kailangan ng paraan upang markahan ang lahat ng resibo na pinirmahan ng key bilang hindi pinagkakatiwalaan mula sa isang punto ng panahon pasulong. Mga karaniwang pattern: mga short-lived signing key kasama ang inilathalang listahan ng revocation, o transparency log na may revocation entries.
- **Bilateral / split-signature receipts.** Ang ilan sa mga implementasyon ay naghahati ng pinirmang payload sa pre-execution (`authorization_*`) at post-execution (`result_*`) na mga bahagi na may hiwalay na mga lagda, na kapaki-pakinabang kapag ang desisyon sa awtorisasyon at ang naobserbahang resulta ay ginawa ng magkaibang aktor o sa magkaibang panahon. Nagsasama ito nang additive sa ibabaw ng format ng resibo na itinuro sa araling ito.
- **Payload composition.** Isinaselyo ng resibo ang anumang byte na inilagay mo sa `result_hash`. Ang mga tunay na payload ay madalas na mayaman kaysa isang resulta ng tool call lang: pre-decision reasoning (model prediction, mga opsyon na pinag-isipang, ebidensya at ang kompletong katangian nito, risk posture, chain ng accountability, kinalabasan ng gate) ay maaaring lahat mabuhay sa loob ng payload, na nakaselyo ng isang resibo lang. Pinananatili nitong minimal ang format ng resibo habang pinapayagan ang mga schema ng payload na umunlad domain-sa-domain.
- **Cross-implementation conformance.** Maraming magkakahiwalay na implementasyon ng parehong format ng resibo (Python, TypeScript, Rust, Go) ay nagka-cross-verify laban sa mga shared na test vector. Kung gagawa ka ng sarili mong implementasyon, ang pag-validate laban sa mga na-publish na vector ay nagpapatunay ng wire compatibility.
- **Post-quantum migration.** Malawak ang deployment ng Ed25519 ngayon pero hindi ito quantum-resistant. Agile ang format ng resibo sa algorithm: ang `signature.alg` field ay maaaring maglaman ng `ML-DSA-65` (ang NIST post-quantum signature standard) kapag kailangan mong mag-migrate. Magplano para sa isang panahon ng transition kung saan double-signed ang mga resibo.

## Karagdagang Mga Sanggunian

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF Internet-Draft: Signed Decision Receipts for Machine-to-Machine Access Control</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785: JSON Canonicalization Scheme (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962: Certificate Transparency</a> (Merkle-tree construction na ginagamit ng selective-disclosure receipts)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, Tutorial 33: Offline-Verifiable Decision Receipts</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">Cross-implementation conformance test vectors</a> para sa format ng resibo na ginamit sa araling ito (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl documentation</a> (Ed25519 sa Python)

## Nakaraang Aralin

[Paglikha ng Lokal na AI Agents](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->