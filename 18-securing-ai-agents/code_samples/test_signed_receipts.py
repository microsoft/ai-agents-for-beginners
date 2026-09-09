"""Regression checks for the notebook helpers and the sample README's code.

Run with `python -m unittest discover -s 18-securing-ai-agents/code_samples
-p test_signed_receipts.py -v` from the repository root after installing the
lesson's requirements. No Azure credentials or network calls are needed.

The tests execute the notebook's Python examples in memory. The single %pip
setup cell is skipped because dependencies are installed before testing.
"""

import contextlib
import copy
import io
import json
from pathlib import Path
import re
import unittest


SAMPLES = Path(__file__).resolve().parent
FIXTURES = SAMPLES / "sample_receipts"
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"


class SignedReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        notebook = json.loads(
            (SAMPLES / "18-signed-receipts.ipynb").read_text(encoding="utf-8")
        )
        cls.examples = {}
        with contextlib.redirect_stdout(io.StringIO()):
            for cell in notebook["cells"]:
                if cell["cell_type"] == "markdown" and "".join(
                    cell["source"]
                ).startswith("## Section 4:"):
                    cls.fixture_examples = dict(cls.examples)
                if cell["cell_type"] != "code":
                    continue
                source = "".join(cell["source"])
                if source.strip() == "%pip install -q pynacl jcs":
                    continue
                exec(compile(source, f"notebook:{cell['id']}", "exec"), cls.examples)

    def setUp(self):
        self.valid = json.loads(
            (FIXTURES / "01_valid_receipt.json").read_text(encoding="utf-8")
        )
        self.chain = json.loads(
            (FIXTURES / "03_chain_three_receipts.json").read_text(encoding="utf-8")
        )
        self.trusted_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

    def test_readme_example_runs_from_notebook_directory(self):
        readme = (FIXTURES / "README.md").read_text(encoding="utf-8")
        blocks = re.findall(r"^```python\n(.*?)^```", readme, re.M | re.S)
        self.assertEqual(len(blocks), 1, "Expected one runnable fixture example")
        namespace = dict(self.fixture_examples)
        output = io.StringIO()
        with contextlib.chdir(SAMPLES), contextlib.redirect_stdout(output):
            exec(compile(blocks[0], "sample_receipts/README.md", "exec"), namespace)
        self.assertEqual(output.getvalue().splitlines(), [
            "Valid receipt: True",
            "Tampered receipt: False",
            "  Receipt 0 (lookup_flights): VALID",
            "  Receipt 1 (hold_seat): VALID",
            "  Receipt 2 (confirm_booking): VALID",
        ])
        self.assertEqual(namespace["fixture_trusted_public_keys"], self.trusted_keys)

    def test_valid_fixture_and_three_receipt_chain(self):
        self.assertTrue(self.examples["verify_receipt"](self.valid, self.trusted_keys))
        results = self.examples["verify_chain"](self.chain, self.trusted_keys)
        self.assertEqual(len(results), 3)
        self.assertTrue(all(result["overall_valid"] for result in results))

    def test_tampered_fixture_is_rejected(self):
        tampered = json.loads(
            (FIXTURES / "02_tampered_receipt.json").read_text(encoding="utf-8")
        )
        self.assertFalse(self.examples["verify_receipt"](tampered, self.trusted_keys))

    def test_unpinned_key_is_rejected_by_both_verifiers(self):
        for trusted_keys in (set(), self.examples["TRUSTED_PUBLIC_KEYS"]):
            with self.subTest(trusted_keys=trusted_keys):
                self.assertFalse(self.examples["verify_receipt"](self.valid, trusted_keys))
                results = self.examples["verify_chain"](self.chain, trusted_keys)
                self.assertTrue(all(not result["overall_valid"] for result in results))

    def test_resigning_with_another_embedded_key_does_not_establish_trust(self):
        key = self.examples["signing"].SigningKey.generate()
        payload = {k: v for k, v in self.valid.items() if k != "signature"}
        substituted = self.examples["sign_receipt"](payload, key, key.verify_key)
        self.assertFalse(self.examples["verify_receipt"](substituted, self.trusted_keys))

    def test_chain_tampering_breaks_signature_and_next_link(self):
        chain = copy.deepcopy(self.chain)
        chain[1]["policy_id"] = "tampered-policy"
        results = self.examples["verify_chain"](chain, self.trusted_keys)
        self.assertTrue(results[0]["overall_valid"])
        self.assertFalse(results[1]["signature_valid"])
        self.assertFalse(results[2]["chain_link_valid"])

    def test_notebook_positive_and_negative_controls(self):
        verify = self.examples["verify_receipt"]
        trusted_keys = self.examples["TRUSTED_PUBLIC_KEYS"]
        self.assertTrue(verify(self.examples["receipt"], trusted_keys))
        self.assertFalse(verify(self.examples["prehashed_receipt"], trusted_keys))
        self.assertFalse(verify(self.examples["tampered"], trusted_keys))
        results = self.examples["verify_chain"](self.examples["chain"], trusted_keys)
        self.assertEqual(len(results), 3)
        self.assertTrue(all(result["overall_valid"] for result in results))
        broken = self.examples["verify_chain"](self.examples["tampered_chain"], trusted_keys)
        self.assertFalse(broken[1]["signature_valid"])
        self.assertFalse(broken[2]["chain_link_valid"])

    def test_wrapped_tool_emits_three_valid_receipts(self):
        receipts = self.examples["receipted_lookup"].receipts
        self.assertEqual(len(receipts), 3)
        results = self.examples["verify_chain"](receipts, self.examples["TRUSTED_PUBLIC_KEYS"])
        self.assertTrue(all(result["overall_valid"] for result in results))


if __name__ == "__main__":
    unittest.main()
