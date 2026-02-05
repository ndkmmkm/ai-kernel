# agents/critic.py

class CriticAI:
    def critique(self, code):
        issues = []

        if "try" not in code:
            issues.append("No error handling")

        if "isinstance" not in code:
            issues.append("No input validation")

        score = max(10 - len(issues) * 2, 1)

        return {
            "score": score,
            "issues": issues,
            "suggestion": "Add edge case handling"
        }
