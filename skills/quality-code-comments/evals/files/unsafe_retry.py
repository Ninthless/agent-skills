MAX_RETRIES = 2


def submit_order(payload, transport):
    last_error = None
    for _ in range(MAX_RETRIES + 1):
        try:
            return transport.post("/orders", json=payload)
        except transport.TransientError as error:
            last_error = error
    raise last_error
