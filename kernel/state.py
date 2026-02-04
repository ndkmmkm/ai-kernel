import time
from collections import defaultdict

class SessionState:
    def __init__(self):
        self.last_seen = None
        self.trust = 1.0
        self.history = []

sessions = defaultdict(SessionState)

def get_session(client_id):
    return sessions[client_id]
