"""
Fixture-backed checks for 18-signed-receipts.ipynb.

Runs the notebook's code cells in order (skipping the %pip line), then checks
its verify_receipt and verify_chain against the fixtures in sample_receipts/,
so the lesson's security results are tested rather than only printed.

Run from this folder. Jupyter is not needed, only the packages in
requirements.txt:

    python -m unittest test_signed_receipts
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

from nacl import signing

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "sample_receipts"
sys.path.insert(0, str(FIXTURES))
import generate_fixtures  # noqa: E402

# The issuer's key, pinned as in sample_receipts/README.md, never read from a receipt.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

FIXTURE_FILES = (
    "01_valid_receipt.json",
    "02_tampered_receipt.json",
    "03_chain_three_receipts.json",
    "04_resigned_receipt.json",
)


def run_notebook() -> dict:
    """Execute the notebook's code cells in one namespace and return it."""
    notebook = json.loads((HERE / "18-signed-receipts.ipynb").read_text(encoding="utf-8"))
    namespace = {"__name__": "lesson18_notebook"}
    with contextlib.redirect_stdout(io.StringIO()):
        for cell in notebook["cells"]:
            source = "".join(cell["source"])
            if cell["cell_type"] != "code" or source.lstrip().startswith("%"):
                continue
            exec(compile(source, "18-signed-receipts.ipynb", "exec"), namespace)
    return namespace


NOTEBOOK = run_notebook()
verify_receipt = NOTEBOOK["verify_receipt"]
verify_chain = NOTEBOOK["verify_chain"]
sign_receipt = NOTEBOOK["sign_receipt"]
ISSUER_SK = signing.SigningKey(bytes.fromhex(generate_fixtures.FIXED_SK_HEX))


def load(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def issuer_signed(payload):
    """Sign a payload with the fixture issuer's own key, so its signature verifies:
    a well-signed receipt the chain checks must still refuse."""
    return sign_receipt(payload, ISSUER_SK, ISSUER_SK.verify_key)


def payload_of(receipt):
    return {k: v for k, v in receipt.items() if k != "signature"}


class SignedReceiptFixtures(unittest.TestCase):
    def test_pinned_key_is_the_fixture_issuers_key(self):
        issuer = signing.SigningKey(bytes.fromhex(generate_fixtures.FIXED_SK_HEX)).verify_key
        self.assertEqual(generate_fixtures.b64url_nopad(bytes(issuer)), ISSUER_KEY)

    def test_valid_receipt_verifies_against_the_issuers_key(self):
        self.assertIs(verify_receipt(load("01_valid_receipt.json"), ISSUER_KEY), True)

    def test_tampered_receipt_fails(self):
        self.assertIs(verify_receipt(load("02_tampered_receipt.json"), ISSUER_KEY), False)

    def test_resigned_forgery_passes_only_against_its_own_key(self):
        forged = load("04_resigned_receipt.json")
        self.assertIs(verify_receipt(forged, forged["signature"]["public_key"]), True)
        self.assertIs(verify_receipt(forged, ISSUER_KEY), False)

    def test_chain_verifies(self):
        results = verify_chain(load("03_chain_three_receipts.json"), ISSUER_KEY)
        self.assertEqual([r["overall_valid"] for r in results], [True, True, True])

    def test_malformed_input_fails_closed(self):
        valid = load("01_valid_receipt.json")
        cases = [
            {"signature": "x"},
            {"signature": {"alg": "EdDSA"}},
            {"signature": {"alg": "EdDSA", "sig": 7}},
            {**valid, "signature": {**valid["signature"], "sig": "not base64url!"}},
            [],
            "not a receipt",
            None,
        ]
        for case in cases:
            with self.subTest(case=case):
                self.assertIs(verify_receipt(case, ISSUER_KEY), False)
        self.assertIs(verify_receipt(valid, "not a key"), False)
        self.assertIs(verify_receipt(valid, None), False)

    def test_a_bad_entry_does_not_stop_the_chain_check(self):
        chain = load("03_chain_three_receipts.json")
        results = verify_chain([chain[0], {"signature": "x"}, chain[2]], ISSUER_KEY)
        self.assertEqual([r["overall_valid"] for r in results], [True, False, False])
        # The entry after the bad one is still checked: its own signature holds,
        # and only its link to the replaced predecessor fails.
        self.assertIs(results[2]["signature_valid"], True)
        self.assertIs(results[2]["chain_link_valid"], False)

    def test_a_genesis_without_its_link_field_fails(self):
        genesis = payload_of(load("03_chain_three_receipts.json")[0])
        del genesis["previous_receipt_hash"]
        results = verify_chain([issuer_signed(genesis)], ISSUER_KEY)
        self.assertIs(results[0]["signature_valid"], True)
        self.assertIs(results[0]["chain_link_valid"], False)
        self.assertIs(results[0]["overall_valid"], False)

    def test_a_boolean_sequence_fails(self):
        chain = load("03_chain_three_receipts.json")
        second = {**payload_of(chain[1]), "sequence": True}  # True == 1 in Python
        results = verify_chain([chain[0], issuer_signed(second)], ISSUER_KEY)
        self.assertIs(results[1]["signature_valid"], True)
        self.assertIs(results[1]["chain_link_valid"], True)
        self.assertIs(results[1]["sequence_valid"], False)
        self.assertEqual([r["overall_valid"] for r in results], [True, False])

    def test_fixtures_regenerate_byte_for_byte(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
            generate_fixtures.main(tmp)
            for name in FIXTURE_FILES:
                with self.subTest(fixture=name):
                    self.assertEqual((Path(tmp) / name).read_bytes(), (FIXTURES / name).read_bytes())


if __name__ == "__main__":
    unittest.main()
