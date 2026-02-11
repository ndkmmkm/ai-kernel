from kernel import doctrine

import time

def update_trust(session, message):
    text = message.lower()

    # naive signal examples (we’ll refine later)
    if len(text) > 500:
        session.trust -= 0.1

    if "ignore previous instructions" in text:
        session.trust -= 0.3

    # clamp using doctrine
    session.trust = max(
        doctrine.MIN_TRUST,
        min(doctrine.MAX_TRUST, session.trust)
    )

    return session.trust

    # Repetition / low entropy detection
    if message in session.history[-3:]:
        session.trust -= 0.2

    session.trust = max(0.0, min(session.trust, 1.0))
    session.last_seen = now
    session.history.append(message)

    return session.trust
