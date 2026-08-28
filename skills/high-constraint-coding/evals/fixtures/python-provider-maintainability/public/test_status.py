import http.server
import json
import sqlite3
import tempfile
import threading
import unittest
from pathlib import Path

from status import check_provider, render_status


class StatusHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        return


class ProviderStatusTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database = Path(self.temporary_directory.name) / "status.db"
        connection = sqlite3.connect(self.database)
        connection.execute(
            "CREATE TABLE provider_checks (id INTEGER PRIMARY KEY, provider TEXT, state TEXT, error TEXT)"
        )
        connection.commit()
        connection.close()
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), StatusHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temporary_directory.cleanup()

    def test_success_is_persisted_and_rendered(self):
        endpoint = f"http://127.0.0.1:{self.server.server_port}/health"

        result = check_provider(self.database, "alpha", endpoint)

        self.assertEqual({"provider": "alpha", "state": "up", "error": None}, result)
        self.assertEqual([result], render_status(self.database))

    def test_failed_provider_is_persisted(self):
        result = check_provider(
            self.database,
            "alpha",
            "http://127.0.0.1:1/health",
            timeout=0.1,
        )

        self.assertEqual("down", result["state"])
        self.assertTrue(result["error"])
        self.assertEqual([result], render_status(self.database))


if __name__ == "__main__":
    unittest.main()
