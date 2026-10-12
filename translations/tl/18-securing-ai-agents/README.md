[Panoorin ang video ng leksyon: Pag-seguro sa AI Agents gamit ang Cryptographic Receipts](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Idadagdag ng Microsoft content team ang video ng leksyon at thumbnail pagkatapos pag-merge, na tumutugma sa pattern ng leksyon 14 / 15.)_

# Pag-seguro sa AI Agents gamit ang Cryptographic Receipts

## Panimula

Tatalakayin sa leksyong ito ang:

- Bakit mahalaga ang audit trails para sa AI agents sa pagsunod, debugging, at pagtitiwala.
- Ano ang cryptographic receipt at paano ito naiiba sa unsigned log line.
- Paano gumawa ng signed receipt para sa tool call ng agent gamit ang plain Python.
- Paano beripikahin ang receipt nang offline at matukoy ang pamemeke.
- Paano ikabit ang mga receipt nang ang pagtanggal o pag-reorder ng isa ay nagpapasira sa chain.
- Ano ang pinatutunayan ng mga receipt at ano ang hindi nila pinatutunayan.

## Mga Layunin sa Pagkatuto

Pagkatapos ng leksyong ito, malalaman mo kung paano:

- Tukuyin ang mga failure mode na nagtutulak ng cryptographic provenance para sa aksyon ng agent.
- Gumawa ng Ed25519-signed receipt gamit ang canonical JSON payload.
- Beripikahin ang receipt nang independiyente gamit lamang ang pampublikong susi ng pirma.
- Matukoy ang pamemeke sa pamamagitan ng muling pag-verify sa nabagong receipt.
- Bumuo ng hash-chained sequence ng mga receipt at ipaliwanag kung bakit mahalaga ang chain.
- Kilalanin ang hangganan ng kung ano ang pinatutunayan ng mga receipt (atribusyon, integridad, pagkakasunod-sunod) at kung ano ang hindi nila pinatutunayan (katumpakan ng aksyon, katibayan ng patakaran).

## Ang Problema: Audit Trail ng Iyong Agent

Isipin na nagde-deploy ka ng AI agent para sa Contoso Travel. Binabasa ng agent ang mga kahilingan ng customer, tumatawag sa flights API para maghanap ng mga pagpipilian, at nagbu-book ng mga upuan para sa customer. Noong nakaraang quarter, ang agent ay nakaproseso ng 50,000 bookings.

Dumating ngayon ang isang auditor. Nagtanong siya ng simpleng tanong: "Ipakita mo sa akin kung ano ang ginawa ng iyong agent."

Inabot mo ang iyong mga log file. Tiningnan ito ng auditor at nagtanong ng mas mahirap na tanong: "Paano ko malalaman na hindi na-edit ang mga logs na ito?"

Ito ang problema sa audit trail. Karamihan sa mga deployment ng agent ngayon ay umaasa sa:

- **Application logs**: isinusulat ng mismong agent, maaaring i-edit ng sinumang may access sa file system.
- **Cloud logging services**: may tamper-evident sa platform level ngunit kailangan munang magtiwala ang auditor sa operator ng platform.
- **Database transaction logs**: angkop para sa mga pagbabago sa database ngunit hindi para sa kahit anong tawag sa tool.

Wala sa mga ito ang makakasagot sa tanong ng auditor nang hindi kailangan magtiwala ang auditor sa kahit sino (ikaw, ang iyong cloud provider, ang vendor ng iyong database). Para sa panloob na gamit, madalas ay katanggap-tanggap ang pagtitiwala na iyon. Para sa mga regulated workloads (finance, healthcare, anumang sakop ng EU AI Act), hindi ito pwede.

Nilulutas ng cryptographic receipts ito sa pamamagitan ng paggawa ng bawat aksyon ng agent na independently verifiable. Hindi na kailangang magtiwala ang auditor sa iyo. Kailangan lang nila ang iyong public key at ang mismong receipt.

## Ano ang Cryptographic Receipt?

Ang receipt ay isang JSON object na nagtatala kung ano ang ginawa ng agent, na may digital signature.

```mermaid
flowchart LR
    A[Gumagamit ang ahente ng isang kasangkapan] --> B[Buuhin ang payload ng resibo]
    B --> C[I-canonicalize ang JSON RFC 8785]
    C --> E[Lagdaan ng Ed25519 ang mga canonical na bytes]
    E --> F[Resibo na may pirma]
    F --> G[Suriin offline ng auditor]
    G --> H{Valid ba ang pirma?}
    H -- yes --> I[Patunay na nagpapakita ng pamemeke]
    H -- no --> J[Tinanggihan ang resibo]
```

Ang minimal na receipt ay ganito ang hitsura:

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

Tatlong katangian ang gumagana dito:

1. **Ang pirma**. Nilagdaan ang receipt ng gateway ng agent gamit ang Ed25519 private key. Mayroon ang sinumang may kaugnay na public key para magberipika ng pirma nang offline. Ang pamemeke ng anumang field ay nagpapawalang-bisa sa pirma.

2. **Canonical encoding**. Bago pumirma, ang receipt ay na-serialize gamit ang JSON Canonicalization Scheme (JCS, RFC 8785). Tinitiyak nito na ang dalawang implementations na lumilikha ng parehong lohikal na receipt ay gumagawa ng byte-identical output. Kung walang canonicalization, iba't ibang JSON serializers ang magbibigay ng iba't ibang pirma para sa parehong nilalaman.

3. **Hash chaining**. Ang field na `previous_receipt_hash` ay nag-uugnay sa bawat receipt sa nakaraang receipt. Ang pagtanggal o pag-reorder ng isang receipt ay nagpapasira sa lahat ng sumusunod na receipts. Nakikita ang pamemeke sa antas ng chain kahit ma-bypass ang mga individual na pirma.

Sama-sama, ang mga katangiang ito ay nagbibigay ng tatlong garantiya:

- **Atribusyon**: ang key na ito ang pumirma sa mga nilalaman.
- **Integridad**: hindi nagbago ang nilalaman mula noong napirmahan.
- **Pagkakasunod-sunod**: ang receipt na ito ay sumunod sa receipt na iyon sa chain.

## Paggawa ng Receipt sa Python

Hindi mo kailangan ng espesyal na library para gumawa ng receipt. Malawak na available ang cryptographic primitives at ang lohika ay ilang dosenang linya ng Python lang.

Ang mga hands-on na ehersisyo sa `code_samples/18-signed-receipts.ipynb` ay naglalakad sa buong flow. Ang summary na bersyon:

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # RFC 8785 canoniko JSON

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# Gumawa o mag-load ng isang signing key (sa produksyon, itago sa isang key vault)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# Bumuo ng payload ng resibo (walang lagda pa)
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

# I-canonicalize at lagdaan ang mga bytes ng JCS nang direkta. Naghahash ang PureEdDSA nang internal.
canonical_bytes = canonicalize(payload)
signature_bytes = signing_key.sign(canonical_bytes).signature

# Ikabit ang isang istrukturadong signature na bagay.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```

Iyan ang buong pipeline ng pag-pirma. Tinatalakay ng mga ehersisyo sa notebook ang bawat hakbang.

## Pag-beripika ng Receipt at Pagtukoy ng Pamemeke

Ang pag-beripika ay ang kabaligtaran na operasyon:

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
    # Ang lagda ay isang istrukturadong bagay: {"alg", "sig", "public_key"}.
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

Tumatanggap ang function na ito ng receipt at bumabalik ng `True` kung tama ang pirma, `False` kung hindi. Walang network call, walang service dependency, walang kinakailangang tiwala sa kahit anong third party.

Upang makita ang pagtukoy ng pamemeke sa aksyon, tinatalakay ng notebook ang:

1. Paggawa ng valid na receipt at pagkumpirma na ito ay nae-verify.
2. Pagbabago ng isang byte sa field na `tool_args_hash`.
3. Muling pag-verify at pagtanggap ng pagkabigo.

Ito ang praktikal na demonstrasyon na ang mga receipt ay tamper-evident: anumang pagbabago, gaano man kaliit, ay nagpapasira ng pirma.

## Pagkabit ng Mga Receipt para sa Multi-Step Agents

Ang isang signed receipt ay nagpoprotekta sa isang aksyon. Ang chain ng mga receipt ay nagpoprotekta sa isang sunod-sunod na proseso.

```mermaid
flowchart LR
    R0[Resibo 0<br/>simula] --> R1[Resibo 1]
    R1 --> R2[Resibo 2]
    R2 --> R3[Resibo 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

Ang bawat receipt ay nagtatala ng hash ng naunang receipt. Upang tahimik na tanggalin ang receipt 2, kailangang ang atacker ay:

- Baguhin ang `previous_receipt_hash` ng receipt 3 (masisira ang pirma ng receipt 3), O
- Gumawa ng bagong pirma sa binagong receipt 3 (kailangan ng private key ng agent).

Kung ang private key ay nasa hardware key vault at inilathala mo ang public key kasama ng bawat receipt, hindi posible ang alinmang atake nang hindi mahahuli.

Tinatalakay ng notebook ang:

1. Pagbuo ng chain ng tatlong receipt.
2. Pag-verify na ang `previous_receipt_hash` ng bawat receipt ay tumutugma sa aktwal na hash ng naunang receipt.
3. Pamemeke sa isang receipt sa gitna at pagtapos ng chain sa puntong iyon.

Ganito mo ginagawa ang audit trail na pwedeng i-verify ng external auditor nang hindi kailangan magtiwala sa iyo.

## Ano ang Pinatutunayan ng Mga Receipt (at Ano ang Hindi)

Ito ang pinakamahalagang seksyon ng leksyong ito. Makapangyarihan ang mga receipt ngunit may hangganan ang kapangyarihan nila.

**Tatlong bagay ang pinatutunayan ng mga Receipt:**

1. **Atribusyon**: isang partikular na key ang pumirma sa isang partikular na payload.
2. **Integridad**: hindi nagbago ang payload mula noong napirmahan.
3. **Pagkakasunod-sunod**: ang receipt na ito ay sumunod sa receipt na iyon sa hash chain.

**Hindi pinatutunayan ng mga Receipt:**

1. **Katumpakan**: na ang aksyon ng agent ay tamang aksyon. Puwedeng lagdaan ang receipt para sa maling sagot nang kasing linaw ng para sa tamang sagot.
2. **Pagsunod sa patakaran**: na ang patakarang tinukoy sa `policy_id` ay talagang sinuri, o na ito ay papayag sa aksyon kung sinuri. Itinatala ng receipt kung ano ang ipinahayag, hindi kung ano ang ipinatupad.
3. **Pagkakakilanlan lampas sa key**: sinasabi ng receipt na "ang key na ito ang pumirma sa nilalaman na ito." Hindi nito sinasabing "isang tao ang nag-autorisa nito." Ang pagkonekta ng key sa tao o organisasyon ay nangangailangan ng hiwalay na identity infrastructure (direktoryo, public key registry, atbp).
4. **Katotohanan ng inputs**: kung ang agent ay tumanggap ng manipuladong prompt at kumilos base rito, tapat na itinatala ng receipt ang aksyon. Ang mga receipt ay nasa ilalim ng input validation, hindi kapalit nito.

Mahalaga ang hangganang ito para sa dalawang dahilan:

- Sinasabi nito kung para saan kapaki-pakinabang ang mga receipt: upang gawing masusuri at may ebidensiya ng pamemeke ang pag-uugali ng agent, kahit lampas pa sa hangganan ng organisasyon.
- Sinasabi nito kung anong karagdagang mga layer pa ang kailangan mo: input validation (Leksiyon 6), pagpapatupad ng patakaran (tatalakayin nang maikli sa ibaba), at identity infrastructure (hindi saklaw ng leksyong ito).

Isang karaniwang pagkakamali ang isipin na "mayroon tayong mga receipt" ay nangangahulugang "nasa ilalim tayo ng pamamahala." Hindi ganoon. Ang mga receipt ay pundasyon. Ang pamamahala ay ang sistemang binubuo mo sa ibabaw nito.

## Papatunayan na Isang Tao ang Nag-apruba ng Eksaktong Aksyon

Ang Item 3 sa itaas ay karapat-dapat sa sariling seksyon: sinasabi ng isang action receipt na "ang key na ito ang pumirma sa nilalaman na ito," hindi kailanman na "isang tao ang nag-autorisa nito." Para sa mga mataas na panganib na aksyon (refunds, deletions, wire transfers), laganap na hinihingi ng mga governance frameworks ang eksaktong nawawalang pahayag na iyon, at maaari itong gawin gamit ang parehong mga primitive na itinuro mo na sa leksyong ito.

Ang kasunod na notebook na `code_samples/human-authorization-receipts.ipynb` ay nagdaragdag ng pangalawang uri ng receipt, `human.approval.v1`, sa parehong envelope na hugis ng mga receipt sa leksyon (isang typed payload na nilagdaan ng Ed25519 sa canonical na JCS bytes nito, na may `signature` object sa labas ng mga nilagdaang bytes). Isang named approver ang pumipirma sa **buong canonical na aksyon at ang digest nito** bago isagawa; ang action receipt ng agent ay may dala ng **parehong action digest** at isang `parent_approval_ref`, ang `receipt_hash` ng pag-apruba, katulad ng convention sa `previous_receipt_hash` sa chain na binuo mo sa itaas. Isang `verify_chain` ang naglalakad sa parehong mga artifacts sa ilalim ng **hiwalay na pinned key registries** (mga susi ng approver kumpara sa mga susi ng agent), kaya ang landas ng code ay ibinabahagi ngunit hindi kailanman ang mga awtoridad.

Ang property na ito na binili, maingat na inilahad: *inaprubahan ng tao ang eksaktong aksyong ito, at isinagawa ng agent ang eksaktong inaprubahang aksyon.* Ang mga refusal fixture ng notebook ang ginagawang totoo ang property sa halip na pahayag lamang:

- ang klasikong set: pamemeke, confused deputy, replay, peke na mga susi sa alinmang panig, maling-input;
- **stale authority**: pirma na patuloy na nagve-verify, tinanggihan pa rin dahil lumipat ang bersyon ng patakaran, ang approver key ay na-rotate palabas ng pinned registry, o ang pag-apruba ay nag-expire bago isagawa;
- **digest substitution**: valid na signed action receipt na tumutukoy sa *tunay* na pag-apruba na nag-uugnay sa *ibang* canonical na aksyon.

Bawat pagkabigo ay tumatanggi na may natatanging dahilan, kaya ang auditor na bumabasa ng pagtanggi ay maaaring malaman kung ang awtoridad ay naging stale o nagbago ang isinagawang aksyon. Ang tuntunin na itinuturo ng notebook: ang isang signed approval ay hindi awtoridad nang mag-isa. Ang awtoridad ay umiiral lamang kung ang parehong mga receipt ay patuloy na nag-uugnay sa parehong canonical na aksyon sa oras ng pagpapatupad. Ang human-approval receipt ay isang educational composition na itinakda ng leksyong ito, hindi isang uri ng receipt na itinakda ng `draft-farley-acta-signed-receipts`.

## Mga Sanggunian sa Produksiyon

Ang Python code sa leksyong ito ay sinadyang minimal upang mabasa mo ang bawat linya at maunawaan nang eksakto kung ano ang nangyayari. Sa produksyon, mayroon kang dalawang pagpipilian:

1. **Direktang bumuo gamit ang cryptographic primitives.** Ang 50 linya na nakita mo sa itaas ay sapat para sa maraming gamit. Ang PyNaCl (Ed25519) at ang `jcs` package (canonical JSON) ay maayos na pinapanatili at sinusuri na mga library.

2. **Gumamit ng production receipt library.** Ilang open-source na proyekto ang nagpapatupad ng parehong pattern na may mga karagdagang tampok (pag-rotate ng susi, batch verification, pamamahagi ng JWK Set, integrasyon sa mga policy engine):
   - Ginagamit ng signing pipeline ang mga convention ng JCS at signature-scope sa isang independenteng IETF Internet-Draft ([`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/), revision 02). Ang flat educational receipt ng leksyong ito ay naiiba sa draft na `{payload, signature}` envelope at hindi ipinapakita bilang isang conformant na implementasyon. Naglalathala ang draft ng shared conformance suite ([agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors)) para sa mga implementasyon na naka-target sa format nito.
   - Ang Microsoft Agent Governance Toolkit ay nagko-compose ng mga receipt gamit ang Cedar-based policy decisions; tingnan ang Tutorial 33 sa repository na iyon para sa isang end-to-end na halimbawa.
   - Ang mga package na `protect-mcp` (npm) at `@veritasacta/verify` (npm) ay nagbibigay ng Node-based na implementasyon ng receipt signing at offline verification, na nilalayon para sa pag-wrap ng anumang MCP server na may tamper-evident audit trail, kabilang ang isang held-for-co-sign flow kung saan ang nai-pause na aksyon ay nag-eemit ng approval receipt na naka-bind sa action digest (WebAuthn-backed sa desktop flow), kaparehong pattern ng approval-receipt gaya ng nasa human-authorization notebook sa itaas.
   - Ang **[nobulex](https://github.com/arian-gogani/nobulex)** Python SDK (`pip install nobulex`) ay nagbibigay ng parehong Ed25519 + JCS signing pattern sa Python kasama ang LangChain at CrewAI integrations, kasama ang mga inilathalang cross-validation test vectors at isang compliance mapping na nilahok sa pamamagitan ng [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210).

Ang pagpili sa pagitan ng paggawa ng sarili mo at paggamit ng library ay parang pagpili sa pagitan ng pagsulat ng sarili mong JWT library at paggamit ng napatunayan nang isa: parehong makatwiran; nakakatipid ang library ng oras at nagpapababa ng audit surface; pinipilit kang maunawaan ng from-scratch na paraan ang bawat primitive. Itinuturo ng leksyong ito ang from-scratch na landas para magkaroon ka ng pundasyon sa alinmang piliin.

## Pagsusulit sa Kaalaman

Subukan ang iyong pagkaunawa bago lumipat sa praktikal na ehersisyo.

**1. Ang receipt ay nilagdaan gamit ang private Ed25519 key ng agent. Ang auditor ay mayroong pampublikong susi lang. Maaari bang beripikahin ng auditor ang receipt offline?**

<details>
<summary>Sagot</summary>

Oo. Kinakailangan ng Ed25519 verification ang pampublikong susi at ang nilagdang bytes lang. Walang network call, walang service dependency. Ito ang property na ginagawang kapaki-pakinabang ang mga receipt sa air-gapped, multi-organisasyon, o mababang-tiwala na mga setting ng audit.
</details>

**2. Binago ng isang atacker ang `policy_id` field ng isang receipt upang i-claim na ito ay pinamamahalaan ng mas permissive na patakaran. Ang pirma ay ginawa sa orihinal na payload. Ano ang mangyayari sa pag-beripika?**

<details>
<summary>Sagot</summary>


Nabigo ang beripikasyon. Ang pirma ay kinakalkula sa canonical bytes ng orihinal na payload; ang pagbabago ng anumang bahagi ay nagbabago sa mga bytes na iyon, na nagiging dahilan upang maging hindi wasto ang pirma. Kailangan ng umaatake ang pribadong susi upang makagawa ng bagong wastong pirma, na wala sila.
</details>

**3. Bakit kasama sa resibo ang `tool_args_hash` at `result_hash` sa halip na ang raw arguments at resulta?**

<details>
<summary>Sagot</summary>

Dalawang dahilan. Una, maaaring kailanganing i-archive o ipadala ang resibo sa mga kapaligiran kung saan ang pagbubunyag ng raw na nilalaman (PII, datos ng negosyo) ay isang problema. Pinananatiling maliit ang resibo at pribado ang nilalaman sa pamamagitan ng pag-hash; sinusuri ng auditor na tumutugma ang hash sa hiwalay na naka-imbak na kopya ng aktwal na nilalaman. Pangalawa, ang mga hash ay may nakatakdang laki; ang resibo na may mga hash ay may limitadong laki gaano man kalaki ang input at output.
</details>

**4. Ang field na `previous_receipt_hash` ay nag-uugnay sa bawat resibo sa nauna nito. Kung tahimik na tatanggalin ng isang umaatake ang isang resibo mula sa gitna ng isang chain, ano ang nagiging hindi wasto?**

<details>
<summary>Sagot</summary>

Bawat resibo na sumunod sa tinanggal. Ang kanilang mga field na `previous_receipt_hash` ay hindi na tumutugma sa aktwal na chain (dahil ang resibo na kanilang ni-refer ay wala na, o ang chain ay tumutok sa ibang nauna). Upang itago ang pagtanggal, kailangang muling pirmahan ng umaatake ang bawat huling resibo, na nangangailangan ng pribadong susi.
</details>

**5. Ang isang resibo ay malinaw na na-verify. Pinapatunayan ba nito na tama, maayos, o sumusunod sa patakaran ang kilos ng ahente?**

<details>
<summary>Sagot</summary>

Hindi. Ang isang valid na resibo ay nagpapatunay ng tatlong bagay: attribution (ang susi na ito ang pumirma sa nilalaman na ito), integridad (hindi nagbago ang nilalaman), at pagkakasunod-sunod (ang resibo na ito ay sumunod sa resibo na iyon). HINDI nito pinapatunayan na tama ang kilos, na ang patakarang nasa `policy_id` ay talaga namang na-evaluate, o na sinunod ng ahente ang bawat patakaran. Ginagawa ng mga resibo na ma-audit ang kilos ng ahente, hindi palaging tama. Ito ang pinakamahalagang hangganan sa aralin.
</details>

## Pagsasanay na Ehersisyo

Buksan ang `code_samples/18-signed-receipts.ipynb` at tapusin ang lahat ng apat na seksyon:

1. **Seksyon 1**: Pirmahan ang iyong unang resibo at i-verify ito.
2. **Seksyon 2**: Manipulahin ang resibo at obserbahan ang pagkabigo ng beripikasyon.
3. **Seksyon 3**: Bumuo ng tatlong-resibo na chain at i-verify ang integridad ng chain.
4. **Seksyon 4**: Ipatupad ang pattern sa isang agent na ginawa gamit ang Microsoft Agent Framework: balutin ang tawag sa tool sa pagbibigay ng pirma sa resibo, pagkatapos ay i-verify ang resibo nang hiwalay.

**Stretch challenge 1:** Palawakin ang schema ng resibo na may dagdag na field na iyong sariling pagpili (halimbawa, isang request ID para sa pagsubaybay), i-update ang canonical signing logic upang maisama ito, at kumpirmahin na ang resibo ay nagpapatuloy sa pagtanggap at pag-verify. Pagkatapos baguhin ang field pagkatapos pirmahan at kumpirmahing mabibigo ang beripikasyon. Pinipilit kang maunawaan kung paano nakakatulong ang bawat byte ng canonical encoding sa pirma.

**Stretch challenge 2:** SHA-256-hash ang dalawang resibo mo nang magkasama (i-konekta ang canonical bytes nila sa deterministikong ayos) at ipaloob ang nagresultang digest bilang bagong field sa ikatlong resibo bago ito pirmahan. I-verify na ang lahat ng tatlong resibo ay nagpapatuloy sa pagtanggap at pag-verify. Nakatayo ka na ngayon ng isang one-step inclusion proof: sinumang may hawak ng ikatlong resibo ay maaaring patunayan na ang unang dalawa ay umiiral noong pirmahan, nang hindi kinakailangang ipakita ang mga nilalaman nila. Ito ang pattern na ginagamit ng selective-disclosure receipts sa malawakang lawak (Merkle commitments, RFC 6962).

## Konklusyon

Ang mga cryptographic na resibo ay nagbibigay sa mga AI agent ng audit trail na:

- **Maaaring i-verify nang hiwalay**: kahit sino na may pampublikong susi ay maaaring mag-verify, walang depensiya sa serbisyo.
- **Nakakadetect ng pamemeke**: anumang pagbabago ay nagbubwelta sa pirma.
- **Madadala**: ang resibo ay isang maliit na JSON file; maaari itong i-archive, ipadala, at i-verify kahit saan.
- **Alinsunod sa pamantayan**: binuo gamit ang Ed25519 (RFC 8032), JCS (RFC 8785), at SHA-256, lahat ay malawakang ginagamit.

Hindi sila kapalit ng input validation, pagpapatupad ng patakaran, o imprastraktura ng pagkakakilanlan. Sila ay pundasyon para sa mga layer na iyon. Kapag nagde-deploy ka ng mga agent sa mga regulated workloads, multi-organisasyon na mga workflow, o anumang sitwasyon kung saan hindi maaaring pagkatiwalaan ng isang auditor sa hinaharap, ang mga resibo ang paraan para gawing matapat ang audit trail.

Ang pinakaimportanteng aral: pinapatunayan ng mga resibo kung sino ang nagsabi ng ano, kailan. Hindi nito pinapatunayan na ang sinabi ay totoo o tama. Mahigpit na hawakan ang pagkakaibang iyon. Ito ang kaibahan ng isang tapat na sistema ng pinagmulan mula sa isang mapanlinlang.

## Checklist para sa Produksyon

Kapag handa ka nang lumipat mula sa araling ito sa pag-deploy ng mga agent na may pirma sa resibo sa totoong kapaligiran:

- [ ] **Ilipat ang signing key mula sa developer laptop.** Gumamit ng Azure Key Vault, AWS KMS, o hardware security module. Ang pribadong susi na pumipirma sa iyong mga resibo ay hindi dapat kailanman mapasakamay sa source control o plain text sa mga makina ng aplikasyon.
- [ ] **I-publish ang pampublikong susi para sa beripikasyon.** Kailangan ito ng mga auditor para mag-verify offline. Ang karaniwang pattern ay isang JWK Set sa kilalang URL (RFC 7517), halimbawa, `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **I-angkla ang chain sa labas.** Paminsan-minsan isulat ang pinakabagong chain head hash sa transparency log (Sigstore Rekor, RFC 3161 timestamp authority, o pangalawang panloob na sistema) upang makumpirma ng panlabas na partido na "umiral ang chain na ito sa oras na ito."
- [ ] **Mag-imbak ng resibo nang hindi mababago.** Ang append-only blob storage (Azure Storage na may immutability policies, AWS S3 Object Lock) ay pumipigil sa isang insider na baguhin ang kasaysayan sa storage layer.
- [ ] **Magdesisyon sa retention.** Maraming mga compliance regime ang nangangailangan ng multi-taong retention. Planuhin ang paglago ng resibo (bawat resibo ay humigit-kumulang 500 bytes; isang agent na gumagawa ng 10K tawag bawat araw ay nagtutustos ng ~1.8 GB bawat taon).
- [ ] **I-documents kung ano ang hindi saklaw ng mga resibo.** Pinapatunayan ng mga resibo ang attribution, integridad, at pagkakasunod-sunod. Ang iyong runbook ay dapat hayagang ilista kung ano pang karagdagang kontrol (input validation, pagpapatupad ng patakaran, rate limiting, imprastraktura ng pagkakakilanlan) ang katabi ng mga resibo sa iyong governance posture.

### May Iba Ka Pang Mga Tanong tungkol sa Pag-secure ng AI Agents?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang nag-aaral, dumalo sa office hours, at sagutin ang iyong mga tanong tungkol sa AI Agents.

## Higit pa sa Araling Ito

Saklaw ng araling ito ang pag-sign ng isang resibo at hash-chained sequences. Ang parehong mga primitives ay bumubuo sa ilang mas advanced na pattern na maaari mong makita habang umuunlad ang iyong governance posture:

- **Selective disclosure.** Kapag ang mga field ng resibo ay independiyenteng naipangako (RFC 6962-style Merkle tree), maaari mong ibunyag ang mga partikular na field sa mga partikular na auditor at patunayan na ang iba ay hindi nabago nang hindi ipinapakita ang mga ito. Kapaki-pakinabang kapag kailangang tugunan ng parehong resibo ang komprehensibong audit (na nais ng pagiging kumpleto) at mga regulasyong may data-minimization tulad ng GDPR (na nais na makita ng auditor ang pinakamaliit na kinakailangan).
- **Receipt revocation.** Kung ang signing key ay nakompromiso, kailangan mo ng paraan upang markahan ang lahat ng resibo na pinirmahan ng susi na iyon bilang hindi mapagkakatiwalaan mula sa isang tiyak na oras pasulong. Mga karaniwang pattern: short-lived signing keys kasama ang isang inilathalang listahan ng revocation, o isang transparency log na may revocation entries.
- **Bilateral / split-signature receipts.** May ilang implementasyon na hinahati ang pinirmang payload sa pre-execution (`authorization_*`) at post-execution (`result_*`) na bahagi na may magkahiwalay na pirma, kapaki-pakinabang kapag ang desisyon sa awtorisasyon at ang naobserbahang resulta ay ginawa ng magkaibang aktor o sa magkaibang oras. Ito ay additive na bumubuo sa ibabaw ng format ng resibo na itinuro sa araling ito.
- **Payload composition.** Nilalagyan ng selyo ng isang resibo ang anumang bytes na ilalagay mo sa `result_hash`. Ang mga totoong payload ay kadalasang mas mayaman kaysa sa isang simpleng resulta ng tawag sa tool: ang pang-unang desisyong pangangatwiran (model prediction, mga opsyon na isinasaalang-alang, ebidensya at ang pagiging kumpleto nito, risk posture, chain ng pananagutan, kinalabasan ng gate) ay maaaring lahat na nasa loob ng payload, na sinelyuhan ng isang resibo. Pinananatiling minimal ang format ng resibo habang pinapayagan ang mga schema ng payload na umunlad sa bawat domain.
- **Cross-implementation conformance.** Maraming independiyenteng implementasyon ng parehong format ng resibo (Python, TypeScript, Rust, Go) ang nagsasagawa ng cross-verify gamit ang mga shared test vector. Kapag gumawa ka ng sarili mong implementasyon, ang pag-validate laban sa mga inilathalang vector ay nagpapatunay ng wire compatibility.
- **Post-quantum migration.** Ang Ed25519 ay malawakang ginagamit ngayon ngunit hindi ito quantum-resistant. Ang format ng resibo ay algorithm-agile: ang field na `signature.alg` ay maaaring maglaman ng `ML-DSA-65` (ang NIST post-quantum signature standard) kapag kailangan mong mag-migrate. Magplano para sa panahon ng transisyon kung saan ang mga resibo ay dual-signed.

## Karagdagang Mga Sanggunian

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF Internet-Draft: Signed Decision Receipts for Machine-to-Machine Access Control</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI overview (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785: JSON Canonicalization Scheme (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962: Certificate Transparency</a> (Merkle-tree construction used by selective-disclosure receipts)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, Tutorial 33: Offline-Verifiable Decision Receipts</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">Cross-implementation conformance test vectors</a> para sa format ng resibo na ginamit sa araling ito (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl documentation</a> (Ed25519 sa Python)

## Nakaraang Aralin

[Creating Local AI Agents](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->