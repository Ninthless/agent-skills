import sqlite3
import tempfile
import unittest
from pathlib import Path

from transfer import RetryableTransactionError, transfer


class TransferTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(
            ignore_cleanup_errors=True
        )
        self.database = Path(self.temporary_directory.name) / "accounts.db"
        connection = sqlite3.connect(self.database)
        connection.execute(
            "CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL)"
        )
        connection.executemany(
            "INSERT INTO accounts (id, balance) VALUES (?, ?)",
            [(1, 100), (2, 50)],
        )
        connection.commit()
        connection.close()

    def tearDown(self):
        self.temporary_directory.cleanup()

    def balances(self):
        connection = sqlite3.connect(self.database)
        rows = connection.execute(
            "SELECT id, balance FROM accounts ORDER BY id"
        ).fetchall()
        connection.close()
        return rows

    def test_successful_transfer(self):
        events = []

        transfer(self.database, 1, 2, 25, events.append)

        self.assertEqual([(1, 75), (2, 75)], self.balances())
        self.assertEqual(1, len(events))

    def test_retryable_failure_succeeds_on_second_attempt(self):
        attempts = []
        events = []

        def fail_once(attempt, connection):
            attempts.append(attempt)
            if attempt == 1:
                raise RetryableTransactionError("database_busy", "try again")

        transfer(self.database, 1, 2, 25, events.append, fault_hook=fail_once)

        self.assertEqual([1, 2], attempts)
        self.assertEqual([(1, 75), (2, 75)], self.balances())
        self.assertEqual(1, len(events))

    def test_non_retryable_error_is_raised(self):
        attempts = []

        def fail(attempt, connection):
            attempts.append(attempt)
            raise ValueError("invalid transfer")

        with self.assertRaisesRegex(ValueError, "invalid transfer"):
            transfer(self.database, 1, 2, 25, lambda event: None, fault_hook=fail)

        self.assertEqual([1], attempts)


if __name__ == "__main__":
    unittest.main()
