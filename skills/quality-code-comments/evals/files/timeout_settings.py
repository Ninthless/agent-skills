REQUEST_TIMEOUT_SECONDS = 30


def request_options() -> dict[str, int]:
    return {"timeout": REQUEST_TIMEOUT_SECONDS}
