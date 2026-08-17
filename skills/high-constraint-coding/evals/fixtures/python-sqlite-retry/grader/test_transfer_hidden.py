import sqlite3
import tempfile
import unittest
from pathlib import Path

from transfer import RetryableTransactionError, transfer


class TrackingConnection:
    def __init__(self, connection, closed):
        self.connection = connection
        self.closed = closed

    def execute(self, *args):
        return self.connection.execute(*args)

    def commit(self):
        return self.connection.commit()

    def rollback(self):
        return self.connection.rollback()

    def close(self):
        self.connection.close()
        self.closed.append(True)


class HiddenTransferTests(unittest.TestCase):
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
        connection = sqlite3.connect(self.database, timeout=0.1)
        try:
            return connection.execute(
                "SELECT id, balance FROM accounts ORDER BY id"
            ).fetchall()
        finally:
            connection.close()

    def test_published_event_observes_committed_balances(self):
        observed = []

        def publish(event):
            observed.append((event, self.balances()))

        transfer(self.database, 1, 2, 25, publish)

        self.assertEqual([(1, 75), (2, 75)], observed[0][1])

    def test_retry_exhaustion_raises_last_error_and_preserves_balances(self):
        attempts = []

        def fail(attempt, connection):
            attempts.append(attempt)
            raise RetryableTransactionError("database_busy", f"attempt {attempt}")

        with self.assertRaisesRegex(RetryableTransactionError, "attempt 3"):
            transfer(self.database, 1, 2, 25, lambda event: None, fault_hook=fail)

        self.assertEqual([1, 2, 3], attempts)
        self.assertEqual([(1, 100), (2, 50)], self.balances())

    def test_non_retryable_error_is_not_retried(self):
        attempts = []

        def fail(attempt, connection):
            attempts.append(attempt)
            raise RuntimeError("terminal")

        with self.assertRaisesRegex(RuntimeError, "terminal"):
            transfer(self.database, 1, 2, 25, lambda event: None, fault_hook=fail)

        self.assertEqual([1], attempts)
        self.assertEqual([(1, 100), (2, 50)], self.balances())

    def test_failed_attempt_is_rolled_back_before_retry(self):
        attempts = []

        def fail_once(attempt, connection):
            attempts.append(attempt)
            if attempt == 1:
                raise RetryableTransactionError("database_busy", "try again")

        transfer(self.database, 1, 2, 25, lambda event: None, fault_hook=fail_once)

        self.assertEqual([1, 2], attempts)
        self.assertEqual([(1, 75), (2, 75)], self.balances())

    def test_connections_are_closed_on_success_and_failure(self):
        success_closes = []

        def success_factory(database):
            return TrackingConnection(sqlite3.connect(database), success_closes)

        transfer(
            self.database,
            1,
            2,
            10,
            lambda event: None,
            connection_factory=success_factory,
        )

        self.assertEqual([True], success_closes)

        failure_closes = []

        def failure_factory(database):
            return TrackingConnection(sqlite3.connect(database), failure_closes)

        def fail(attempt, connection):
            raise RuntimeError("terminal")

        with self.assertRaises(RuntimeError):
            transfer(
                self.database,
                1,
                2,
                10,
                lambda event: None,
                fault_hook=fail,
                connection_factory=failure_factory,
            )

        self.assertEqual([True], failure_closes)


if __name__ == "__main__":
    unittest.main()
