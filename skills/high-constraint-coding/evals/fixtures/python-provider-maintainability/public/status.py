import json
import sqlite3
import urllib.request


def check_provider(database, provider, endpoint, timeout=5):
    request = urllib.request.Request(endpoint, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        state = "up" if payload.get("status") == "ok" else "degraded"
        error = None
    except Exception as exc:
        state = "down"
        error = str(exc)

    connection = sqlite3.connect(database)
    try:
        connection.execute(
            "INSERT INTO provider_checks (provider, state, error) VALUES (?, ?, ?)",
            (provider, state, error),
        )
        connection.commit()
    finally:
        connection.close()

    return {"provider": provider, "state": state, "error": error}


def render_status(database):
    connection = sqlite3.connect(database)
    try:
        rows = connection.execute(
            "SELECT provider, state, error FROM provider_checks ORDER BY id"
        ).fetchall()
    finally:
        connection.close()
    return [
        {"provider": provider, "state": state, "error": error}
        for provider, state, error in rows
    ]
