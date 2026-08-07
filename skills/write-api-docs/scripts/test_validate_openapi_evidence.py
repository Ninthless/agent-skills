import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_openapi_evidence.py")
SPEC = importlib.util.spec_from_file_location("validate_openapi_evidence", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateOpenApiEvidenceTests(unittest.TestCase):
    def test_accepts_exact_claims(self):
        specification = {
            "info": {"version": "TBD"},
            "paths": {
                "/accounts/{accountId}": {
                    "get": {"security": [{"oauth": ["accounts:read"]}]}
                }
            },
            "components": {
                "schemas": {
                    "AccountId": {
                        "type": "string",
                        "pattern": "^acct_[A-Za-z0-9]+$",
                    }
                }
            },
        }
        evidence = {
            "claims": [
                {
                    "pointer": "/info/version",
                    "value": "TBD",
                    "evidence": "No version exists; this artifact is an explicit draft.",
                },
                {
                    "pointer": "/paths/~1accounts~1{accountId}/get/security",
                    "value": [{"oauth": ["accounts:read"]}],
                    "evidence": "Focused authorization test.",
                },
                {
                    "pointer": (
                        "/components/schemas/AccountId/pattern"
                    ),
                    "value": "^acct_[A-Za-z0-9]+$",
                    "evidence": "Route validation rule.",
                },
            ]
        }

        self.assertEqual(MODULE.validate(specification, evidence), [])

    def test_rejects_unproven_schema_constraints(self):
        specification = {
            "info": {"version": "1.0.0"},
            "components": {
                "schemas": {
                    "Account": {
                        "required": ["id", "state"],
                        "properties": {
                            "id": {"type": "string", "format": "uuid"},
                            "state": {"type": "string", "enum": ["active"]},
                            "nickname": {"type": ["string", "null"]},
                        },
                    }
                }
            },
        }

        errors = MODULE.validate(specification, {"claims": []})

        self.assertEqual(len(errors), 5)
        self.assertTrue(any("/info/version" in error for error in errors))
        self.assertTrue(any("/required" in error for error in errors))
        self.assertTrue(any("/format" in error for error in errors))
        self.assertTrue(any("/enum" in error for error in errors))
        self.assertTrue(any("/nickname/type" in error for error in errors))

    def test_rejects_mismatched_and_unused_claims(self):
        specification = {
            "info": {"version": "TBD"},
            "components": {
                "schemas": {
                    "Value": {"type": "string", "maxLength": 20}
                }
            },
        }
        evidence = {
            "claims": [
                {
                    "pointer": "/info/version",
                    "value": "1.0.0",
                    "evidence": "Repository metadata.",
                },
                {
                    "pointer": "/components/schemas/Value/minLength",
                    "value": 1,
                    "evidence": "Validation rule.",
                },
            ]
        }

        errors = MODULE.validate(specification, evidence)

        self.assertEqual(len(errors), 3)
        self.assertTrue(any("mismatch" in error for error in errors))
        self.assertTrue(any("unsupported" in error for error in errors))
        self.assertTrue(any("unused" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
