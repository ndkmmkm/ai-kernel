class FakeAI:
    def respond(self, prompt):
        return "Demo mode active."

def get():
    return FakeAI()
