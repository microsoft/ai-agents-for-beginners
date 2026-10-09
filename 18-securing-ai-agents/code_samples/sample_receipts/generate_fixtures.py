"""
Generate the sample receipt fixtures in this directory.

Uses a fixed Ed25519 signing key and a fixed timestamp so the output is
byte-reproducible. Run this from the repo root or from within this folder.

Output:
  01_valid_receipt.json
  02_tampered_receipt.json
  03_chain_three_receipts.json
  04_resigned_receipt.json
"""
import copy
import hashlib
import json
import base64
from pathlib import Path

from nacl import signing
from jcs import canonicalize


# Fixed key for byte-reproducible fixtures. NEVER reuse in production.
FIXED_SK_HEX = "9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60"

# A second, unrelated key standing in for an attacker. Used only to build
# fixture 04, which is a forgery that verifies against the key inside it.
ATTACKER_SK_HEX = "4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb8a6fb"

FIXED_TS = "2026-04-25T14:30:00Z"


def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def sha256_canonical(obj) -> str:
    canonical = canonicalize(obj)
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def sign_receipt(payload: dict, signing_key, verify_key) -> dict:
    canonical = canonicalize(payload)
    sig_bytes = signing_key.sign(canonical).signature
    return {
        **payload,
        "signature": {
            "alg": "EdDSA",
            "sig": b64url_nopad(sig_bytes),
            "public_key": b64url_nopad(bytes(verify_key)),
        },
    }


def receipt_hash(receipt: dict) -> str:
    canonical = canonicalize(receipt)
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def make_receipt(tool_name, tool_args, tool_result, sequence,
                 previous_receipt_hash, signing_key, verify_key,
                 timestamp=FIXED_TS):
    payload = {
        "type": "agent.tool_call.v1",
        "agent_id": "contoso-travel-bot",
        "tool_name": tool_name,
        "tool_args_hash": sha256_canonical(tool_args),
        "result_hash": sha256_canonical(tool_result),
        "policy_id": "contoso-travel-policy-v3",
        "timestamp": timestamp,
        "sequence": sequence,
        "previous_receipt_hash": previous_receipt_hash,
    }
    return sign_receipt(payload, signing_key, verify_key)


def main():
    here = Path(__file__).parent
    sk = signing.SigningKey(bytes.fromhex(FIXED_SK_HEX))
    vk = sk.verify_key

    # Fixture 1: a valid receipt
    valid = make_receipt(
        tool_name="lookup_flights",
        tool_args={"origin": "SYD", "destination": "LAX",
                   "departure_date": "2026-06-15", "passengers": 2},
        tool_result=[
            {"flight": "QF11", "price": 1850, "stops": 0},
            {"flight": "UA864", "price": 1620, "stops": 1},
        ],
        sequence=0,
        previous_receipt_hash=None,
        signing_key=sk,
        verify_key=vk,
    )
    (here / "01_valid_receipt.json").write_text(
        json.dumps(valid, indent=2) + "\n"
    )

    # Fixture 2: tamper with one field after signing
    tampered = copy.deepcopy(valid)
    tampered["policy_id"] = "contoso-travel-policy-PERMISSIVE"
    (here / "02_tampered_receipt.json").write_text(
        json.dumps(tampered, indent=2) + "\n"
    )

    # Fixture 3: chain of three receipts
    r0 = make_receipt(
        tool_name="lookup_flights",
        tool_args={"origin": "SYD", "destination": "LAX"},
        tool_result=[{"flight": "QF11", "price": 1850}],
        sequence=0,
        previous_receipt_hash=None,
        signing_key=sk,
        verify_key=vk,
    )
    r1 = make_receipt(
        tool_name="hold_seat",
        tool_args={"flight": "QF11", "seat": "14A", "hold_minutes": 30},
        tool_result={"hold_id": "H8472", "expires_at": "2026-06-15T15:00:00Z"},
        sequence=1,
        previous_receipt_hash=receipt_hash(r0),
        signing_key=sk,
        verify_key=vk,
    )
    r2 = make_receipt(
        tool_name="confirm_booking",
        tool_args={"hold_id": "H8472", "payment_token": "tok_redacted"},
        tool_result={"booking_ref": "CT-09182", "status": "confirmed"},
        sequence=2,
        previous_receipt_hash=receipt_hash(r1),
        signing_key=sk,
        verify_key=vk,
    )
    (here / "03_chain_three_receipts.json").write_text(
        json.dumps([r0, r1, r2], indent=2) + "\n"
    )

    # Fixture 4: tamper, then re-sign with an attacker's own key and embed
    # that key in the receipt. This is internally consistent: it verifies
    # against the key it carries. It is caught only by verifying against the
    # issuer's key obtained from somewhere other than the receipt.
    attacker_sk = signing.SigningKey(bytes.fromhex(ATTACKER_SK_HEX))
    forged_payload = {k: v for k, v in valid.items() if k != "signature"}
    forged_payload["policy_id"] = "contoso-travel-policy-PERMISSIVE"
    forged = sign_receipt(forged_payload, attacker_sk, attacker_sk.verify_key)
    (here / "04_resigned_receipt.json").write_text(
        json.dumps(forged, indent=2) + "\n"
    )

    print(f"Wrote four fixtures to {here}")


if __name__ == "__main__":
    main()
