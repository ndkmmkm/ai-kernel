# agents/builder.py

class BuilderAI:
    def build(self, design):
        if design["model_type"] == "improved_rule_based":
            return """
def model(input_number):
    try:
        if not isinstance(input_number, int):
            return "invalid"
        return "even" if input_number % 2 == 0 else "odd"
    except Exception:
        return "error"
"""
        return """
def model(input_number):
    if input_number % 2 == 0:
        return "even"
    else:
        return "odd"
"""
