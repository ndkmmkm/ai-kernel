# agents/architect.py

class ArchitectAI:
    def __init__(self):
        self.version = 1

    def design(self, task, previous_feedback=None):
        if previous_feedback and previous_feedback.get("score", 0) < 8:
            self.version += 1
            return {
                "task": task,
                "model_type": "improved_rule_based",
                "logic": "Add input validation + fallback",
                "version": self.version
            }

        return {
            "task": task,
            "model_type": "rule_based",
            "logic": "If number % 2 == 0 then even else odd",
            "version": self.version
        }
