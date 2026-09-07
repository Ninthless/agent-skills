SESSION_TTL_SECONDS = 55


def cache_session(cache, session_id, payload):
    cache.set(session_id, payload, ttl=SESSION_TTL_SECONDS)
