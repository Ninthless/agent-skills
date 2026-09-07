from typing import Any


REQUEST_TIMEOUT_SECONDS = 5
MAX_RETRIES = 2


def submit_checkout(payload: dict[str, Any], idempotency_key: str, transport):
    last_error = None
    for _ in range(MAX_RETRIES + 1):
        try:
            return transport.post(
                "/checkout",
                json=payload,
                headers={"Idempotency-Key": idempotency_key},
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
        except transport.TransientError as error:
            last_error = error
    raise last_error
