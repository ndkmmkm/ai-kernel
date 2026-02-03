import time

def update_trust(session, message):
    now = time.time()

    if session.last_seen:
        delta = now - session.last_seen

        # Too fast = automation signal
        if delta < 1.0:
            session.trust -= 0.1
        elif delta > 5.0:
            session.trust += 0.05

    # Repetition / low entropy detection
    if message in session.history[-3:]:
        session.trust -= 0.2

    session.trust = max(0.0, min(session.trust, 1.0))
    session.last_seen = now
    session.history.append(message)

    return session.trust
