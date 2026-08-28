import sqlite3
import tempfile
import unittest
import inspect
from pathlib import Path
from unittest.mock import patch

import status
from status import check_provider, render_status


class ProviderStatusMaintainabilityTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database = Path(self.temporary_directory.name) / "status.db"
        connection = sqlite3.connect(self.database)
        connection.execute(
            "CREATE TABLE provider_checks (id INTEGER PRIMARY KEY, provider TEXT, state TEXT, error TEXT)"
        )
        connection.commit()
        connection.close()

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_check_provider_coordinates_named_boundaries(self):
        self.assertTrue(callable(getattr(status, "fetch_provider_state", None)))
        self.assertTrue(callable(getattr(status, "save_provider_check", None)))
        source = inspect.getsource(check_provider)
        self.assertNotIn("urlopen", source)
        self.assertNotIn("sqlite3", source)

    def test_provider_specific_behavior_is_not_mixed_into_storage_or_rendering(self):
        with patch("status.urllib.request.urlopen") as urlopen:
            response = urlopen.return_value.__enter__.return_value
            response.read.return_value = b'{"status": "ok"}'
            result = check_provider(self.database, "beta", "https://example.test/health")

        self.assertEqual("up", result["state"])
        self.assertEqual([result], render_status(self.database))
        urlopen.assert_called_once()
        request = urlopen.call_args.args[0]
        self.assertEqual("https://example.test/health", request.full_url)

    def test_existing_contract_handles_provider_failure_without_special_case(self):
        with patch("status.urllib.request.urlopen", side_effect=TimeoutError("slow")):
            result = check_provider(self.database, "beta", "https://example.test/health")

        self.assertEqual(
            [{"provider": "beta", "state": "down", "error": "slow"}],
            render_status(self.database),
        )
        self.assertEqual("down", result["state"])


if __name__ == "__main__":
    unittest.main()
