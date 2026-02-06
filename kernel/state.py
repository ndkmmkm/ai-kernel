import time
from collections import defaultdict

class SessionState:
    def __init__(self):
        self.last_seen = None
        self.trust = 1.0

        # learning / shadow state
        self.learning_enabled = False
        self.shadow_logs = []

        self.history = []

sessions = defaultdict(SessionState)

def get_session(client_id):
    return sessions[client_id]

class KernelState:
    def __init__(self):
        self.trust = 0.5
        self.meaning = 1.0
        self.constraint = 0.0
        self.entropy = 0.0
        self.cooldown = False
