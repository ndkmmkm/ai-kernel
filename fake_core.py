class FakeAI:
    def respond(self, prompt):
        return "Demo mode active. Full intelligence unavailable."

def get():
    return FakeAI()
