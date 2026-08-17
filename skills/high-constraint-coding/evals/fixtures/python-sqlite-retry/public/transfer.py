import sqlite3


class RetryableTransactionError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def transfer(
    database,
    source_account,
    destination_account,
    amount,
    publish,
    max_attempts=3,
    fault_hook=None,
    connection_factory=sqlite3.connect,
):
    connection = connection_factory(database)

    for attempt in range(1, max_attempts + 1):
        try:
            connection.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, source_account),
            )
            connection.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (amount, destination_account),
            )

            if fault_hook is not None:
                fault_hook(attempt, connection)

            publish(
                {
                    "source_account": source_account,
                    "destination_account": destination_account,
                    "amount": amount,
                }
            )
            connection.commit()
            return
        except RetryableTransactionError:
            if attempt == max_attempts:
                raise
        except Exception:
            raise

    connection.close()
