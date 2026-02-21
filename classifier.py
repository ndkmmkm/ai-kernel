def classify(text):
    text_lower = text.lower()

    if "how to make a bomb" in text_lower:
        return {"action": "refuse", "level": 4}

    if "how to hack" in text_lower:
        return {"action": "refuse", "level": 3}

    return {"action": "allow", "level": 0}
